"""Checks the JSON Schema this project commits, as a user of it would read it.

project/jsonschema/capec.schema.json is what a consumer without LinkML validates
with. It is read here under the draft it declares, and held to the generator's
settings in .linkml/generators.yaml.
"""

import json
from functools import cache
from pathlib import Path

import jsonschema
import yaml
from linkml.generators.jsonschemagen import JsonSchemaGenerator

ROOT = Path(__file__).parent.parent
COMMITTED = ROOT / "project" / "jsonschema" / "capec.schema.json"
SCHEMA = ROOT / "src" / "capec" / "schema" / "capec.yaml"
DATA = ROOT / "tests" / "data"


@cache
def schema():
    return json.loads(COMMITTED.read_text(encoding="utf-8"))


def validator():
    return jsonschema.validators.validator_for(schema())(schema())


def _load(path):
    return yaml.safe_load(path.read_text(encoding="utf-8"))


def test_the_schema_is_valid_under_the_draft_it_declares():
    jsonschema.validators.validator_for(schema()).check_schema(schema())


def test_the_committed_file_is_the_generators_output():
    """A schema edit without `just gen-project` fails here."""
    settings = yaml.safe_load((ROOT / ".linkml" / "generators.yaml").read_text())
    args = settings["generator_args"]["jsonschema"]
    generated = JsonSchemaGenerator(str(SCHEMA), **args).serialize()
    assert json.loads(generated) == schema()


def test_the_top_of_the_schema_is_the_catalogue():
    assert schema()["title"] == "capec"
    assert schema()["additionalProperties"] is False
    assert sorted(schema()["required"]) == ["Date", "Name", "Version"]


def test_a_small_catalogue_validates_against_the_file():
    instance = _load(DATA / "valid" / "CapecAttackPatternCatalog-small.yaml")
    assert not list(validator().iter_errors(instance))


def test_every_class_is_closed():
    """A key the XSD lacks fails in every class, so a misspelled key cannot pass."""
    for name, definition in schema()["$defs"].items():
        if "properties" in definition:
            assert definition["additionalProperties"] is False, name


def test_a_reference_carries_its_pattern():
    """A reference to an entry is a string of digits in the file, even though a JSON
    Schema cannot say that the entry exists."""
    defs = schema()["$defs"]
    for name, key in (
        ("CapecRelatedAttackPattern", "CAPEC_ID"),
        ("CapecHasMember", "CAPEC_ID"),
        ("CapecMemberOf", "CAPEC_ID"),
        ("CapecExcludeRelated", "Exclude_ID"),
    ):
        assert defs[name]["properties"][key]["pattern"] == "^[1-9][0-9]*$", name
    pattern = defs["CapecReference"]["properties"]["External_Reference_ID"]["pattern"]
    assert pattern == "^REF-[0-9]+$"


def test_techniques_capec_id_stays_as_open_as_the_xsds_string():
    """The XSD types it as xs:string, and no technique sets it, so any string passes."""
    key = schema()["$defs"]["CapecTechnique"]["properties"]["CAPEC_ID"]
    assert "pattern" not in key
