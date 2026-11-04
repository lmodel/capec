"""The whole CAPEC catalogue, against the committed JSON Schema and the rules.

Each count here is what CAPEC 3.9 holds, so that a sentence in the docs or the schema
about the data stays true, and a new version asks a person to read it again. The
faults are pinned the same way, so a fix upstream fails this file too.
"""

import json
import re
from collections import Counter
from functools import cache
from pathlib import Path

import jsonschema
import pytest
import rdflib
from linkml.validator import validate

from tests.capec_rules import rule_errors
from tests.capec_xml import converter

ROOT = Path(__file__).parent.parent
SCHEMA = ROOT / "src" / "capec" / "schema" / "capec.yaml"
COMMITTED = ROOT / "project" / "jsonschema" / "capec.schema.json"
CONTEXT = ROOT / "project" / "jsonld" / "capec.context.jsonld"

# MITRE's own faults in CAPEC 3.9, each a rule or an expectation it breaks. The
# hand-over to MITRE names each. A fix upstream fails the test that pins it.
UNKNOWN_REFERENCE = ("244", "REF-97")
REPEATED_WEAKNESSES = {("545", "1258"), ("644", "308")}
NAMES_WITH_A_TRAILING_SPACE = {"552", "658"}
FLOWS_WITH_A_REPEATED_STEP = {
    "105": [1, 1, 2, 1],
    "221": [1, 2, 2, 4],
    "273": [1, 1, 2, 1],
    "33": [1, 1, 2, 1],
    "34": [1, 1, 2, 1],
    "42": [1, 2, 3, 4, 4],
    "470": [1, 2, 3, 4, 5, 6, 6, 6],
    "522": [1, 2, 3, 3],
}
SKILLS_WITH_NO_TEXT = {"509", "701"}
META_CHILD_OF_STANDARD = {("699", "651")}


@cache
def catalogue():
    return converter.catalogue_data()


def _patterns():
    return catalogue()["Attack_Patterns"]


def _entries():
    data = catalogue()
    return [*data["Attack_Patterns"], *data["Categories"], *data["Views"]]


def test_the_catalogue_passes_the_committed_json_schema():
    """Every key and value of the whole catalogue, as a consumer's validator reads it."""
    schema = json.loads(COMMITTED.read_text(encoding="utf-8"))
    validator = jsonschema.validators.validator_for(schema)(schema)
    found = [
        f"{list(e.absolute_path)}: {e.message[:200]}"
        for e in validator.iter_errors(catalogue())
    ]
    assert not found


def test_linkml_validate_agrees():
    """The LinkML validator, which the docs tell a user to run, finds nothing."""
    report = validate(catalogue(), SCHEMA, "CapecAttackPatternCatalog")
    assert not report.results, [r.message for r in report.results][:5]


def test_each_section_holds_what_the_list_page_counts():
    data = catalogue()
    assert (
        len(data["Attack_Patterns"]),
        len(data["Categories"]),
        len(data["Views"]),
        len(data["External_References"]),
    ) == (615, 78, 13, 440)
    in_force = [p for p in data["Attack_Patterns"] if p["Status"] != "Deprecated"]
    assert len(in_force) == 559


def test_the_rules_find_only_the_known_fault():
    """Every reference resolves but one, and every number is unique."""
    found = rule_errors(catalogue(), "CapecAttackPatternCatalog")
    assert len(found) == 1
    pointer, message = found[0]
    index = int(pointer.split("/")[2])
    assert (_patterns()[index]["ID"], message.split()[0]) == UNKNOWN_REFERENCE


def test_repeated_weakness_rows():
    """Two patterns name one weakness twice, so 1214 rows make 1212 pairs."""
    found = set()
    rows = 0
    for pattern in _patterns():
        ids = [r["CWE_ID"] for r in pattern.get("Related_Weaknesses", [])]
        rows += len(ids)
        found |= {(pattern["ID"], i) for i, n in Counter(ids).items() if n > 1}
    assert found == REPEATED_WEAKNESSES
    assert rows == 1214


def test_names_with_a_trailing_space():
    found = {e["ID"] for e in _entries() if e["Name"] != e["Name"].strip()}
    assert found == NAMES_WITH_A_TRAILING_SPACE


def test_skills_with_no_text():
    found = {
        p["ID"]
        for p in _patterns()
        for skill in p.get("Skills_Required", [])
        if not skill["Value"].strip()
    }
    assert found == SKILLS_WITH_NO_TEXT


def _natures():
    return Counter(
        r["Nature"] for p in _patterns() for r in p.get("Related_Attack_Patterns", [])
    )


def test_the_natures_the_catalogue_uses():
    """ChildOf and never ParentOf, as the enum's comment says."""
    assert _natures() == {
        "ChildOf": 533,
        "CanPrecede": 162,
        "PeerOf": 19,
        "CanFollow": 10,
        "CanAlsoBe": 3,
    }


def test_no_pair_is_recorded_from_both_ends():
    """No pair of inverse natures is written twice, as the enum's comment says."""
    pairs = {
        (p["ID"], r["Nature"], r["CAPEC_ID"])
        for p in _patterns()
        for r in p.get("Related_Attack_Patterns", [])
    }
    inverse = {"CanFollow": "CanPrecede", "CanPrecede": "CanFollow"}
    assert not [
        pair
        for pair in pairs
        if pair[1] in inverse and (pair[2], inverse[pair[1]], pair[0]) in pairs
    ]


def test_a_child_is_rarely_more_abstract_than_its_parent():
    """The XSD says a parent is more abstract, and one pair has it the other way."""
    level = {p["ID"]: p["Abstraction"] for p in _patterns()}
    rows = [
        (p["ID"], r["CAPEC_ID"])
        for p in _patterns()
        for r in p.get("Related_Attack_Patterns", [])
        if r["Nature"] == "ChildOf"
    ]
    assert {
        pair
        for pair in rows
        if level[pair[0]] == "Meta" and level[pair[1]] == "Standard"
    } == META_CHILD_OF_STANDARD
    assert Counter((level[a], level[b]) for a, b in rows) == {
        ("Detailed", "Standard"): 312,
        ("Standard", "Meta"): 183,
        ("Detailed", "Detailed"): 30,
        ("Detailed", "Meta"): 6,
        ("Standard", "Standard"): 1,
        ("Meta", "Standard"): 1,
    }


def test_flows_at_each_level():
    """The XSD says a flow is usually for Detailed patterns. So the schema has no
    rule, as the entries module's comment says."""
    with_flow = Counter(p["Abstraction"] for p in _patterns() if "Execution_Flow" in p)
    assert with_flow == {"Detailed": 149, "Standard": 80, "Meta": 10}
    level = Counter(p["Abstraction"] for p in _patterns())
    assert level == {"Detailed": 341, "Standard": 197, "Meta": 77}


def test_flows_that_repeat_a_step_number():
    """The rest of the 239 flows count 1, 2, 3, and these do not, so the schema
    states no sequence."""
    flows = {
        p["ID"]: [s["Step"] for s in p["Execution_Flow"]]
        for p in _patterns()
        if "Execution_Flow" in p
    }
    assert len(flows) == 239
    uneven = {i: s for i, s in flows.items() if s != list(range(1, len(s) + 1))}
    assert {i: uneven[i] for i in FLOWS_WITH_A_REPEATED_STEP} == (
        FLOWS_WITH_A_REPEATED_STEP
    )
    assert len(uneven) == 11


def test_every_exclusion_names_a_category():
    """The XSD says only an ancestor, as the attribute's comment says."""
    categories = {c["ID"] for c in catalogue()["Categories"]}
    excluded = [
        e["Exclude_ID"]
        for p in _patterns()
        for r in p.get("Related_Attack_Patterns", [])
        for e in r.get("Exclude_Related", [])
    ]
    assert len(excluded) == 260
    assert set(excluded) <= categories


@pytest.mark.parametrize(
    ("kind", "deprecated"), [("Attack_Patterns", 56), ("Categories", 57), ("Views", 0)]
)
def test_a_deprecated_entry_says_so_in_its_name(kind, deprecated):
    """This is only what the data shows, so no rule in the schema states it."""
    entries = catalogue()[kind]
    by_status = {e["ID"] for e in entries if e["Status"] == "Deprecated"}
    by_name = {e["ID"] for e in entries if e["Name"].startswith("DEPRECATED")}
    assert by_status == by_name
    assert len(by_status) == deprecated


def test_a_view_is_a_filter_or_a_member_list():
    """Implicit views filter, and the others list members. This is only what the data
    shows, so no rule in the schema states it."""
    for view in catalogue()["Views"]:
        assert ("Filter" in view) == (view["Type"] == "Implicit"), view["ID"]
        assert ("Members" in view) == (view["Type"] != "Implicit"), view["ID"]


def test_the_keys_no_entry_uses():
    """The XSD defines these, and the docs say CAPEC 3.9 does not use them."""
    text = json.dumps(catalogue())
    for key in (
        "Audience",
        "Member_Of",
        "Contribution",
        "Mapping_Fit",
        "Consequence_ID",
        "Modification_Importance",
        "Submission_Comment",
    ):
        assert f'"{key}"' not in text, key
    assert not [
        t
        for p in _patterns()
        for s in p.get("Execution_Flow", [])
        for t in s.get("Technique", [])
        if "CAPEC_ID" in t
    ]


def test_every_year_month_and_day_has_the_xsds_form():
    """The XSD's words give a day four hyphens, its type three, and the data three."""
    for reference in catalogue()["External_References"]:
        assert re.fullmatch(r"(\d{4})?", reference.get("Publication_Year", ""))
        assert re.fullmatch(r"(--\d\d)?", reference.get("Publication_Month", ""))
        assert re.fullmatch(r"(---\d\d)?", reference.get("Publication_Day", ""))


def test_the_json_ld_route_gives_iris():
    """linkml-convert cannot dump RDF here, because linkml-runtime's rdflib dumper
    expands a bare identifier and finds no base. The generated context can, and a
    reference comes out as an IRI, not as text."""
    context = json.loads(CONTEXT.read_text(encoding="utf-8"))["@context"]
    data = catalogue()
    sample = {
        "@context": context,
        "Name": data["Name"],
        "Attack_Patterns": [p for p in _patterns() if p["ID"] in ("1", "122")],
        "External_References": data["External_References"][:1],
    }
    graph = rdflib.Graph()
    graph.parse(
        data=json.dumps(sample),
        format="json-ld",
        base="https://w3id.org/lmodel/capec/",
    )
    capec = rdflib.Namespace("https://w3id.org/lmodel/capec/")
    assert (capec["1"], capec.Abstraction, rdflib.Literal("Standard")) in graph
    objects = set(graph.objects(None, capec.CAPEC_ID))
    assert capec["122"] in objects
    assert all(isinstance(o, rdflib.URIRef) for o in objects)
