"""Checks each mapping against its source, and the prefixes it needs.

Each mapping names its target by a CURIE whose prefix the schema binds. A target
in an lmodel neighbour's namespace, or under an IRI that a neighbour's released
copy declares, is held to that copy under tests/neighbours/. Every other target is
held to tests/upstream/mapping-terms.txt, which scripts/extract_mapping_terms.py
writes from each vocabulary's pinned file. The schema is the one home for mappings:
no SSSOM file sits beside it.
"""

import hashlib
from functools import cache
from pathlib import Path

import pytest
import yaml
from linkml_runtime import SchemaView

ROOT = Path(__file__).parent.parent
SCHEMA_DIR = ROOT / "src" / "capec" / "schema"
SCHEMA = SCHEMA_DIR / "capec.yaml"
NEIGHBOURS = ROOT / "tests" / "neighbours"
TERMS = ROOT / "tests" / "upstream" / "mapping-terms.txt"
TERMS_SHA256 = "9a044140664499a36722de264a50a8049937ac1131d852341fff561bfe001ff0"
MAPPING_KEYS = (
    "exact_mappings",
    "close_mappings",
    "narrow_mappings",
    "broad_mappings",
    "related_mappings",
    "mappings",
)
# Mappings point to released neighbours only. The name of lmodel/vulnerability-core is
# here because the old schema's relatives pointed to it, and it is gone.
GONE_NAMESPACES = ("https://w3id.org/lmodel/vulnerability-core/",)


def _mappings(node):
    if isinstance(node, dict):
        for key, value in node.items():
            if key in MAPPING_KEYS:
                yield from value if isinstance(value, list) else [value]
            else:
                yield from _mappings(value)
    elif isinstance(node, list):
        for item in node:
            yield from _mappings(item)


def _meanings(node):
    if isinstance(node, dict):
        for key, value in node.items():
            if key == "meaning":
                yield value
            else:
                yield from _meanings(value)
    elif isinstance(node, list):
        for item in node:
            yield from _meanings(item)


MODULES = {
    path.name: yaml.safe_load(path.read_text())
    for path in sorted(SCHEMA_DIR.glob("*.yaml"))
}
TARGETS = sorted(
    {
        (name, curie)
        for name, doc in MODULES.items()
        for curie in [*_mappings(doc), *_meanings(doc)]
    }
)


@cache
def neighbour_iris():
    """Each IRI the neighbours' released copies declare."""
    found = set()
    for path in NEIGHBOURS.glob("*.yaml"):
        doc = yaml.safe_load(path.read_text())
        prefixes = doc.get("prefixes") or {}
        default = doc.get("default_prefix")

        def expand(curie):
            prefix, _, local = curie.partition(":")
            return prefixes[prefix] + local if prefix in prefixes else curie

        def add(kind, uri_key):
            for name, element in (doc.get(kind) or {}).items():
                element = element or {}
                found.add(expand(element.get(uri_key) or f"{default}:{name}"))
                for value in (element.get("permissible_values") or {}).values():
                    if (value or {}).get("meaning"):
                        found.add(expand(value["meaning"]))

        add("classes", "class_uri")
        add("slots", "slot_uri")
        add("enums", "enum_uri")
        for cls in (doc.get("classes") or {}).values():
            for name, slot in ((cls or {}).get("attributes") or {}).items():
                found.add(expand((slot or {}).get("slot_uri") or f"{default}:{name}"))
    return found


@cache
def listed_terms():
    lines = TERMS.read_text(encoding="utf-8").splitlines()
    return {line for line in lines if line and not line.startswith("#")}


def expand(module, curie):
    prefix, _, local = curie.partition(":")
    return MODULES[module]["prefixes"][prefix] + local


def test_the_term_list_is_the_pinned_one():
    """The list is byte for byte what the script wrote from the pinned files."""
    assert hashlib.sha256(TERMS.read_bytes()).hexdigest() == TERMS_SHA256


def test_mappings_exist():
    """The parametrized tests below pass on an empty list, so this one does not."""
    assert len(TARGETS) >= 60, len(TARGETS)


@pytest.mark.parametrize(("module", "curie"), TARGETS)
def test_each_target_has_a_bound_prefix(module, curie):
    """Every mapping names its target by a CURIE whose prefix its module binds, so
    a projection of the adapt copy raises no warning."""
    prefix, separator, _ = curie.partition(":")
    assert separator and prefix in MODULES[module]["prefixes"], curie


@pytest.mark.parametrize(("module", "curie"), TARGETS)
def test_each_target_is_read_at_its_source(module, curie):
    """Every target is a term a pinned vocabulary file or a released neighbour
    copy declares."""
    iri = expand(module, curie)
    assert iri in neighbour_iris() or iri in listed_terms(), iri


@pytest.mark.parametrize(("module", "curie"), TARGETS)
def test_no_mapping_points_at_a_namespace_that_is_gone(module, curie):
    assert not expand(module, curie).startswith(GONE_NAMESPACES), curie


def test_no_sssom_file_sits_beside_the_schema():
    """The schema is the one home for mappings, each held by a test here."""
    assert not list(ROOT.glob("src/**/*.sssom.tsv"))


def test_the_module_imports_are_the_contract():
    """capec_core imports only the LinkML types, so another schema can take it alone,
    and capec_entries imports only it. The umbrella takes both."""
    assert MODULES["capec_core.yaml"]["imports"] == ["linkml:types"]
    assert MODULES["capec_entries.yaml"]["imports"] == ["linkml:types", "./capec_core"]
    assert MODULES["capec.yaml"]["imports"] == [
        "linkml:types",
        "./capec_core",
        "./capec_entries",
    ]
    assert (
        MODULES["capec_core.yaml"]["id"] == "https://w3id.org/lmodel/capec/capec_core"
    )


def test_each_module_loads_on_its_own():
    """Each module can be taken alone, with no import cycle."""
    for name in MODULES:
        view = SchemaView(str(SCHEMA_DIR / name))
        assert view.all_classes(), name
