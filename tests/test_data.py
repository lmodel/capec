"""Data tests: every example against the JSON Schema the validator generates, the
rules no generator carries, and the XSD itself."""

import json
from functools import cache
from pathlib import Path

import jsonschema
import pytest
import yaml
from linkml.generators.jsonschemagen import JsonSchemaGenerator
from linkml.validator import validate
from linkml_runtime import SchemaView

from tests import capec_xml
from tests.capec_rules import rule_errors

ROOT = Path(__file__).parent.parent
SCHEMA = ROOT / "src" / "capec" / "schema" / "capec.yaml"
DATA = Path(__file__).parent / "data"
VALID = sorted((DATA / "valid").glob("*.yaml"))
INVALID = sorted((DATA / "invalid").glob("*.yaml"))
PROBLEM_INVALID = sorted((DATA / "problem" / "invalid").glob("*.yaml"))
# The classes that can be built into a catalogue for MITRE's XSD to look at.
WHOLE = {
    "CapecAttackPattern",
    "CapecAttackPatternCatalog",
    "CapecCategory",
    "CapecExternalReference",
    "CapecView",
}


def class_of(path):
    return path.stem.split("-")[0]


ASKABLE_VALID = [p for p in VALID if class_of(p) in WHOLE]
# A missing ID stays out, because nothing can build that element, and the same goes
# for a missing Value. The XSD's own attribute rule still says what a catalogue needs.
ASKABLE_INVALID = [
    p
    for p in INVALID
    if class_of(p) in WHOLE and ("-without-" in p.stem or "-not-listed" in p.stem)
]


@cache
def definitions():
    """The class definitions of the JSON Schema that linkml-validate generates.
    Generating it once keeps the run short; test_validator_agrees checks that
    linkml-validate gives the same answers."""
    generator = JsonSchemaGenerator(str(SCHEMA), mergeimports=True)
    return json.loads(generator.serialize())["$defs"]


def errors(instance, class_name):
    schema = {"$ref": f"#/$defs/{class_name}", "$defs": definitions()}
    validator_class = jsonschema.validators.validator_for(schema)
    validator = validator_class(schema, format_checker=validator_class.FORMAT_CHECKER)
    return list(validator.iter_errors(instance))


def pointer(error):
    return "/" + "/".join(str(part) for part in error.absolute_path)


def fails_at(path):
    first = path.read_text(encoding="utf-8").splitlines()[0]
    assert first.startswith("# Fails at: "), (
        f"{path.name}: the first line names where it fails"
    )
    return first.removeprefix("# Fails at: ").strip()


def places(error):
    """Where an error points: its own place, or, for an anyOf that no branch met, the
    places inside the branch that could have been meant. An optional object's branches
    are the object and null, so its error points inside the object."""
    if error.validator not in ("anyOf", "oneOf") or not error.context:
        return {pointer(error)}
    branches = {}
    for sub in error.context:
        branches.setdefault(sub.relative_schema_path[0], []).append(sub)
    real = [
        subs
        for subs in branches.values()
        if not any(s.validator == "type" and s.validator_value == "null" for s in subs)
    ]
    if len(real) != 1:
        return {pointer(error)}
    found = set()
    for sub in real[0]:
        found |= places(sub)
    return found or {pointer(error)}


def _load(path):
    return yaml.safe_load(path.read_text(encoding="utf-8"))


def test_the_example_folders_hold_examples():
    """The parametrized tests below pass on an empty folder, so this one does not."""
    assert len(VALID) >= 50, len(VALID)
    assert len(INVALID) >= 120, len(INVALID)
    assert len(PROBLEM_INVALID) >= 5, len(PROBLEM_INVALID)


@pytest.mark.parametrize("path", VALID, ids=lambda p: p.stem)
def test_valid_examples_validate(path):
    """Every valid example passes the JSON Schema and the rules in Python."""
    instance = _load(path)
    found = errors(instance, class_of(path))
    assert not found, [f"{pointer(e)}: {e.message[:200]}" for e in found]
    assert not rule_errors(instance, class_of(path))


@pytest.mark.parametrize("path", ASKABLE_VALID, ids=lambda p: p.stem)
def test_the_xsd_accepts_each_entry_example(path):
    """An example of a whole entry, built back into XML, passes MITRE's own XSD, so an
    example here says nothing the XSD does not. The XSD has no global element for the
    smaller records, which the entry examples hold."""
    wrapped = capec_xml.wrapped_in_a_catalogue(class_of(path), _load(path))
    assert capec_xml.xsd_errors(capec_xml.catalogue_element(wrapped)) == []


@pytest.mark.parametrize("path", ASKABLE_INVALID, ids=lambda p: p.stem)
def test_the_xsd_refuses_each_missing_key_and_unlisted_value(path):
    """No such counter-example asks for more than the XSD does: its own rules refuse
    the same thing."""
    wrapped = capec_xml.wrapped_in_a_catalogue(class_of(path), _load(path))
    assert capec_xml.xsd_errors(capec_xml.catalogue_element(wrapped))


@pytest.mark.parametrize("path", INVALID, ids=lambda p: p.stem)
def test_counter_examples_fail_where_they_say(path):
    """Every counter-example fails at the place its first line names, as
    `# Fails at: <JSON pointer>`, and nowhere else but on the way to it, so a file
    that starts failing for another reason fails this test."""
    where = fails_at(path)
    found = errors(_load(path), class_of(path))
    assert found, "it validates"
    reached = set().union(*(places(e) for e in found))
    report = [f"{pointer(e)}: {e.message[:200]}" for e in found]
    assert where in reached, (sorted(reached), report)
    on_the_way = {
        p for p in reached if where == p or where.startswith(p.rstrip("/") + "/")
    }
    assert reached == on_the_way, (sorted(reached - on_the_way), report)


@pytest.mark.parametrize("path", PROBLEM_INVALID, ids=lambda p: p.stem)
def test_rule_counter_examples_fail_where_they_say(path):
    """A counter-example under problem/invalid/ passes the JSON Schema, which cannot
    state its rule, and fails only the rule its first line points to."""
    where = fails_at(path)
    instance = _load(path)
    class_name = class_of(path)
    found = errors(instance, class_name)
    assert not found, [f"{pointer(e)}: {e.message[:200]}" for e in found]
    assert [p for p, _ in rule_errors(instance, class_name)] == [where]


def test_validator_agrees():
    """linkml-validate, which the docs tell a user to run, accepts a valid example and
    rejects a counter-example."""
    good = DATA / "valid" / "CapecAttackPatternCatalog-small.yaml"
    report = validate(_load(good), SCHEMA, "CapecAttackPatternCatalog")
    assert not report.results, [r.message for r in report.results]
    bad = DATA / "invalid" / "CapecAttackPattern-Status-not-listed.yaml"
    report = validate(_load(bad), SCHEMA, "CapecAttackPattern")
    assert any(
        "Status" in r.message or "Not a listed" in r.message for r in report.results
    )


def test_every_concrete_class_has_an_example():
    """Each class the catalogue can hold has a valid example, and so does the root."""
    view = SchemaView(str(SCHEMA))
    concrete = {
        name
        for name, cls in view.all_classes().items()
        if not cls.abstract and not cls.mixin
    }
    examples = {class_of(path) for path in VALID}
    assert concrete == examples, sorted(concrete ^ examples)


def test_each_constraint_has_a_counter_example():
    """Each required key, listed value and patterned value has its counter-example, by
    the file names that say so."""
    view = SchemaView(str(SCHEMA))
    names = {path.stem for path in INVALID}
    missing = []
    for name, cls in view.all_classes().items():
        if cls.abstract or cls.mixin:
            continue
        if f"{name}-key-the-xsd-lacks" not in names:
            missing.append(f"{name}-key-the-xsd-lacks")
        for key in view.class_slots(name):
            slot = view.induced_slot(key, name)
            if slot.required or slot.identifier:
                if f"{name}-without-{key}" not in names:
                    missing.append(f"{name}-without-{key}")
            if slot.range in view.all_enums():
                if f"{name}-{key}-not-listed" not in names:
                    missing.append(f"{name}-{key}-not-listed")
    assert not missing, missing
