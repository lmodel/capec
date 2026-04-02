"""Tests for the CAPEC 3.9 XML data file (tests/data/capec/capec_3.9.xml).

Validates that the downloaded CAPEC XML conforms to the expected structure and
that all enumerated attribute values align with the enumerations defined in the
CAPEC LinkML schema (src/capec/schema/capec.yaml).
"""
import xml.etree.ElementTree as ET
from pathlib import Path

import pytest

CAPEC_XML = Path(__file__).parent / "data" / "capec" / "capec_3.9.xml"
NS = {"c": "http://capec.mitre.org/capec-3"}

# Expected counts in the CAPEC 3.9 release (file is named 3.5 but contains 3.9)
EXPECTED_ATTACK_PATTERN_COUNT = 615
EXPECTED_CATEGORY_COUNT = 78
EXPECTED_VIEW_COUNT = 13
EXPECTED_EXTERNAL_REFERENCE_COUNT = 440

# Valid enum values matching capec.yaml schema enumerations
VALID_ABSTRACTIONS = {"Meta", "Standard", "Detailed"}
VALID_STATUSES = {"Deprecated", "Draft", "Incomplete", "Obsolete", "Stable", "Usable"}
VALID_LIKELIHOODS = {"High", "Medium", "Low", "Unknown"}
VALID_SEVERITIES = {"Very High", "High", "Medium", "Low", "Very Low"}
VALID_VIEW_TYPES = {"Implicit", "Explicit", "Graph"}
VALID_RELATED_NATURES = {"ChildOf", "ParentOf", "CanFollow", "CanPrecede", "CanAlsoBe", "PeerOf"}
VALID_SCOPES = {
    "Confidentiality", "Integrity", "Availability", "Access Control",
    "Accountability", "Authentication", "Authorization", "Non-Repudiation", "Other",
}
VALID_IMPACTS = {
    "Modify Data", "Read Data", "Unreliable Execution", "Resource Consumption",
    "Execute Unauthorized Commands", "Gain Privileges", "Bypass Protection Mechanism",
    "Hide Activities", "Alter Execution Logic", "Other",
}
VALID_TAXONOMY_NAMES = {"ATTACK", "WASC", "OWASP Attacks"}
VALID_TAXONOMY_FIT = {"Exact", "CAPEC More Abstract", "CAPEC More Specific", "Imprecise", "Perspective"}


# ---------------------------------------------------------------------------
# Module-scoped fixtures — parse the XML once for the entire test session
# ---------------------------------------------------------------------------

@pytest.fixture(scope="module")
def capec_root():
    """Parse capec_3.9.xml and return the root element."""
    assert CAPEC_XML.exists(), f"CAPEC XML not found: {CAPEC_XML}"
    return ET.parse(CAPEC_XML).getroot()


@pytest.fixture(scope="module")
def attack_patterns(capec_root):
    return capec_root.findall(".//c:Attack_Pattern", NS)


@pytest.fixture(scope="module")
def categories(capec_root):
    return capec_root.findall(".//c:Category", NS)


@pytest.fixture(scope="module")
def views(capec_root):
    return capec_root.findall(".//c:View", NS)


@pytest.fixture(scope="module")
def external_references(capec_root):
    return capec_root.findall(".//c:External_Reference", NS)


# ---------------------------------------------------------------------------
# Catalog-level tests
# ---------------------------------------------------------------------------

class TestCatalog:
    def test_xml_file_exists(self):
        assert CAPEC_XML.exists()

    def test_catalog_name(self, capec_root):
        assert capec_root.get("Name") == "CAPEC"

    def test_catalog_version_present(self, capec_root):
        """File is named 3.5 but contains CAPEC 3.9 data."""
        assert capec_root.get("Version") == "3.9"

    def test_catalog_date_present(self, capec_root):
        assert capec_root.get("Date") == "2023-01-24"

    def test_attack_pattern_count(self, attack_patterns):
        assert len(attack_patterns) == EXPECTED_ATTACK_PATTERN_COUNT

    def test_category_count(self, categories):
        assert len(categories) == EXPECTED_CATEGORY_COUNT

    def test_view_count(self, views):
        assert len(views) == EXPECTED_VIEW_COUNT

    def test_external_reference_count(self, external_references):
        assert len(external_references) == EXPECTED_EXTERNAL_REFERENCE_COUNT


# ---------------------------------------------------------------------------
# Attack Pattern tests
# ---------------------------------------------------------------------------

class TestAttackPatterns:
    def test_all_have_id(self, attack_patterns):
        for ap in attack_patterns:
            assert ap.get("ID") is not None

    def test_all_have_name(self, attack_patterns):
        for ap in attack_patterns:
            assert ap.get("Name") not in (None, "")

    def test_all_have_description(self, attack_patterns):
        for ap in attack_patterns:
            desc = ap.find("c:Description", NS)
            assert desc is not None, f"CAPEC-{ap.get('ID')} missing Description"

    def test_abstraction_values_are_valid(self, attack_patterns):
        for ap in attack_patterns:
            assert ap.get("Abstraction") in VALID_ABSTRACTIONS, (
                f"CAPEC-{ap.get('ID')} invalid Abstraction: {ap.get('Abstraction')!r}"
            )

    def test_status_values_are_valid(self, attack_patterns):
        for ap in attack_patterns:
            assert ap.get("Status") in VALID_STATUSES, (
                f"CAPEC-{ap.get('ID')} invalid Status: {ap.get('Status')!r}"
            )

    def test_likelihood_values_are_valid(self, attack_patterns):
        for ap in attack_patterns:
            loa = ap.find("c:Likelihood_Of_Attack", NS)
            if loa is not None and loa.text:
                assert loa.text in VALID_LIKELIHOODS, (
                    f"CAPEC-{ap.get('ID')} invalid Likelihood_Of_Attack: {loa.text!r}"
                )

    def test_severity_values_are_valid(self, attack_patterns):
        for ap in attack_patterns:
            sev = ap.find("c:Typical_Severity", NS)
            if sev is not None and sev.text:
                assert sev.text in VALID_SEVERITIES, (
                    f"CAPEC-{ap.get('ID')} invalid Typical_Severity: {sev.text!r}"
                )

    def test_related_nature_values_are_valid(self, attack_patterns):
        for ap in attack_patterns:
            for rap in ap.findall(".//c:Related_Attack_Pattern", NS):
                assert rap.get("Nature") in VALID_RELATED_NATURES, (
                    f"CAPEC-{ap.get('ID')} invalid Related_Attack_Pattern Nature: {rap.get('Nature')!r}"
                )

    def test_related_attack_pattern_capec_ids_are_integers(self, attack_patterns):
        for ap in attack_patterns:
            for rap in ap.findall(".//c:Related_Attack_Pattern", NS):
                capec_id = rap.get("CAPEC_ID", "")
                assert capec_id.isdigit(), (
                    f"CAPEC-{ap.get('ID')} non-integer CAPEC_ID: {capec_id!r}"
                )

    def test_scope_values_are_valid(self, attack_patterns):
        for ap in attack_patterns:
            for scope_el in ap.findall(".//c:Scope", NS):
                if scope_el.text:
                    assert scope_el.text in VALID_SCOPES, (
                        f"CAPEC-{ap.get('ID')} invalid Scope: {scope_el.text!r}"
                    )

    def test_impact_values_are_valid(self, attack_patterns):
        for ap in attack_patterns:
            for impact_el in ap.findall(".//c:Impact", NS):
                if impact_el.text:
                    assert impact_el.text in VALID_IMPACTS, (
                        f"CAPEC-{ap.get('ID')} invalid Impact: {impact_el.text!r}"
                    )

    def test_related_weakness_cwe_ids_are_integers(self, attack_patterns):
        for ap in attack_patterns:
            for rw in ap.findall(".//c:Related_Weakness", NS):
                cwe_id = rw.get("CWE_ID", "")
                assert cwe_id.isdigit(), (
                    f"CAPEC-{ap.get('ID')} invalid CWE_ID: {cwe_id!r}"
                )

    def test_taxonomy_name_values_are_valid(self, attack_patterns):
        for ap in attack_patterns:
            for tm in ap.findall(".//c:Taxonomy_Mapping", NS):
                name = tm.get("Taxonomy_Name")
                if name:
                    assert name in VALID_TAXONOMY_NAMES, (
                        f"CAPEC-{ap.get('ID')} invalid Taxonomy_Name: {name!r}"
                    )

    def test_taxonomy_fit_values_are_valid(self, attack_patterns):
        for ap in attack_patterns:
            for tm in ap.findall(".//c:Taxonomy_Mapping", NS):
                fit_el = tm.find("c:Mapping_Fit", NS)
                if fit_el is not None and fit_el.text:
                    assert fit_el.text in VALID_TAXONOMY_FIT, (
                        f"CAPEC-{ap.get('ID')} invalid Mapping_Fit: {fit_el.text!r}"
                    )

    def test_ids_are_unique(self, attack_patterns):
        ids = [ap.get("ID") for ap in attack_patterns]
        assert len(ids) == len(set(ids)), "Duplicate Attack Pattern IDs found"

    # --- Known-entry spot-checks ---

    def test_capec_1_attributes(self, attack_patterns):
        """Spot-check CAPEC-1: Accessing Functionality Not Properly Constrained by ACLs."""
        ap = next((a for a in attack_patterns if a.get("ID") == "1"), None)
        assert ap is not None, "CAPEC-1 not found"
        assert ap.get("Name") == "Accessing Functionality Not Properly Constrained by ACLs"
        assert ap.get("Abstraction") == "Standard"
        assert ap.get("Status") == "Draft"
        loa = ap.find("c:Likelihood_Of_Attack", NS)
        assert loa is not None and loa.text == "High"
        sev = ap.find("c:Typical_Severity", NS)
        assert sev is not None and sev.text == "High"

    def test_capec_1_related_patterns(self, attack_patterns):
        ap = next((a for a in attack_patterns if a.get("ID") == "1"), None)
        raps = ap.findall(".//c:Related_Attack_Pattern", NS)
        natures = {r.get("Nature") for r in raps}
        assert "ChildOf" in natures
        assert any(r.get("CAPEC_ID") == "122" for r in raps)

    def test_capec_1_related_weaknesses(self, attack_patterns):
        ap = next((a for a in attack_patterns if a.get("ID") == "1"), None)
        cwe_ids = {rw.get("CWE_ID") for rw in ap.findall(".//c:Related_Weakness", NS)}
        assert "276" in cwe_ids
        assert "285" in cwe_ids

    def test_meta_patterns_exist(self, attack_patterns):
        meta = [ap for ap in attack_patterns if ap.get("Abstraction") == "Meta"]
        assert len(meta) > 0

    def test_detailed_patterns_exist(self, attack_patterns):
        detailed = [ap for ap in attack_patterns if ap.get("Abstraction") == "Detailed"]
        assert len(detailed) > 0

    def test_execution_flow_steps_have_valid_phases(self, attack_patterns):
        valid_phases = {"Explore", "Experiment", "Exploit"}
        for ap in attack_patterns:
            for step in ap.findall(".//c:Attack_Step", NS):
                phase_el = step.find("c:Phase", NS)
                if phase_el is not None and phase_el.text:
                    assert phase_el.text in valid_phases, (
                        f"CAPEC-{ap.get('ID')} invalid Phase: {phase_el.text!r}"
                    )


# ---------------------------------------------------------------------------
# Category tests
# ---------------------------------------------------------------------------

class TestCategories:
    def test_all_have_id_name_status(self, categories):
        for cat in categories:
            assert cat.get("ID") is not None
            assert cat.get("Name") not in (None, "")
            assert cat.get("Status") is not None

    def test_all_have_summary(self, categories):
        for cat in categories:
            summary = cat.find("c:Summary", NS)
            assert summary is not None, f"Category {cat.get('ID')} missing Summary"

    def test_status_values_are_valid(self, categories):
        for cat in categories:
            assert cat.get("Status") in VALID_STATUSES, (
                f"Category {cat.get('ID')} invalid Status: {cat.get('Status')!r}"
            )

    def test_ids_are_unique(self, categories):
        ids = [cat.get("ID") for cat in categories]
        assert len(ids) == len(set(ids)), "Duplicate Category IDs found"

    def test_category_118_details(self, categories):
        """Spot-check Category 118: Collect and Analyze Information."""
        cat = next((c for c in categories if c.get("ID") == "118"), None)
        assert cat is not None, "Category 118 not found"
        assert cat.get("Name") == "Collect and Analyze Information"
        assert cat.get("Status") == "Stable"

    def test_category_118_has_members(self, categories):
        cat = next((c for c in categories if c.get("ID") == "118"), None)
        rels = cat.find("c:Relationships", NS)
        assert rels is not None
        has_members = rels.findall("c:Has_Member", NS)
        assert len(has_members) > 0
        member_ids = {hm.get("CAPEC_ID") for hm in has_members}
        assert "116" in member_ids
        assert "117" in member_ids


# ---------------------------------------------------------------------------
# View tests
# ---------------------------------------------------------------------------

class TestViews:
    def test_all_have_required_attributes(self, views):
        for v in views:
            assert v.get("ID") is not None
            assert v.get("Name") not in (None, "")
            assert v.get("Type") is not None
            assert v.get("Status") is not None

    def test_all_have_objective(self, views):
        for v in views:
            obj = v.find("c:Objective", NS)
            assert obj is not None, f"View {v.get('ID')} missing Objective"

    def test_type_values_are_valid(self, views):
        for v in views:
            assert v.get("Type") in VALID_VIEW_TYPES, (
                f"View {v.get('ID')} invalid Type: {v.get('Type')!r}"
            )

    def test_status_values_are_valid(self, views):
        for v in views:
            assert v.get("Status") in VALID_STATUSES, (
                f"View {v.get('ID')} invalid Status: {v.get('Status')!r}"
            )

    def test_ids_are_unique(self, views):
        ids = [v.get("ID") for v in views]
        assert len(ids) == len(set(ids)), "Duplicate View IDs found"

    def test_view_1000_details(self, views):
        """Spot-check View 1000: Mechanisms of Attack."""
        v = next((x for x in views if x.get("ID") == "1000"), None)
        assert v is not None, "View 1000 not found"
        assert v.get("Name") == "Mechanisms of Attack"
        assert v.get("Type") == "Graph"
        assert v.get("Status") == "Stable"

    def test_view_1000_has_members(self, views):
        v = next((x for x in views if x.get("ID") == "1000"), None)
        members = v.find("c:Members", NS)
        assert members is not None
        has_m = members.findall("c:Has_Member", NS)
        assert len(has_m) > 0

    def test_all_view_types_present(self, views):
        types = {v.get("Type") for v in views}
        assert "Graph" in types
        assert "Explicit" in types


# ---------------------------------------------------------------------------
# External Reference tests
# ---------------------------------------------------------------------------

class TestExternalReferences:
    def test_all_have_reference_id_and_title(self, external_references):
        for ref in external_references:
            assert ref.get("Reference_ID") not in (None, "")
            title = ref.find("c:Title", NS)
            assert title is not None, f"Ref {ref.get('Reference_ID')} missing Title"

    def test_ids_are_unique(self, external_references):
        ids = [ref.get("Reference_ID") for ref in external_references]
        assert len(ids) == len(set(ids)), "Duplicate External_Reference IDs found"

    def test_ids_follow_ref_prefix_format(self, external_references):
        for ref in external_references:
            ref_id = ref.get("Reference_ID", "")
            assert ref_id.startswith("REF-"), (
                f"Reference_ID does not follow REF-N format: {ref_id!r}"
            )

    def test_url_references_have_uri_attribute(self, external_references):
        for ref in external_references:
            url_el = ref.find("c:URL", NS)
            if url_el is not None and url_el.text:
                assert url_el.text.startswith(("http://", "https://")), (
                    f"Ref {ref.get('Reference_ID')} URL not absolute: {url_el.text!r}"
                )

    def test_ref1_details(self, external_references):
        """Spot-check REF-1: Exploiting Software: How to Break Code."""
        ref = next((r for r in external_references if r.get("Reference_ID") == "REF-1"), None)
        assert ref is not None, "REF-1 not found"
        title = ref.find("c:Title", NS)
        assert title is not None and title.text == "Exploiting Software: How to Break Code"
        authors = ref.findall("c:Author", NS)
        assert len(authors) == 2
        author_names = [a.text for a in authors]
        assert "G. Hoglund" in author_names
        assert "G. McGraw" in author_names
        year = ref.find("c:Publication_Year", NS)
        assert year is not None and year.text == "2004"
        publisher = ref.find("c:Publisher", NS)
        assert publisher is not None and publisher.text == "Addison-Wesley"
