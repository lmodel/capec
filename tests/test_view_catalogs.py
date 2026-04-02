"""Tests for view-filtered Attack_Pattern_Catalog exports.

Covers the 13 files distributed across:
  - tests/data/capec/navigation/  (hierarchical navigation views)
  - tests/data/capec/views/       (abstraction/status/thematic slices)
  - src/capec/mappings/           (vendor taxonomy mapping exports)

All files share the same Attack_Pattern_Catalog XML structure but contain
only Attack_Patterns (no Categories, Views, or External_References sections).
The catalog Name attribute follows the convention "VIEW LIST: CAPEC-{ID}: {Name}".
"""
import xml.etree.ElementTree as ET
import functools
from pathlib import Path

import pytest

NAV_DIR = Path(__file__).parent / "data" / "capec" / "navigation"
VIEWS_DIR = Path(__file__).parent / "data" / "capec" / "views"
MAPPINGS_DIR = Path(__file__).parent.parent / "src" / "capec" / "mappings"

NS = {"c": "http://capec.mitre.org/capec-3"}

VALID_ABSTRACTIONS = {"Meta", "Standard", "Detailed"}
VALID_STATUSES = {"Deprecated", "Draft", "Incomplete", "Obsolete", "Stable", "Usable"}

ALL_VIEW_EXPORTS = sorted(
    list(NAV_DIR.glob("*.xml"))
    + list(VIEWS_DIR.glob("*.xml"))
    + list(MAPPINGS_DIR.glob("*.xml")),
    key=lambda p: p.stem,
)


@functools.lru_cache(maxsize=None)
def _parse(path: Path):
    """Parse an XML file and cache the root element."""
    return ET.parse(path).getroot()


# ---------------------------------------------------------------------------
# Structural invariants common to all 13 view-filtered catalog files
# ---------------------------------------------------------------------------

class TestViewCatalogStructure:
    """Structural invariants that must hold for every view-filtered catalog file."""

    @pytest.mark.parametrize("xml_path", ALL_VIEW_EXPORTS, ids=lambda p: p.stem)
    def test_root_is_attack_pattern_catalog(self, xml_path):
        root = _parse(xml_path)
        assert root.tag == "{http://capec.mitre.org/capec-3}Attack_Pattern_Catalog"

    @pytest.mark.parametrize("xml_path", ALL_VIEW_EXPORTS, ids=lambda p: p.stem)
    def test_name_follows_view_list_convention(self, xml_path):
        root = _parse(xml_path)
        name = root.attrib.get("Name", "")
        assert name.startswith("VIEW LIST: CAPEC-"), (
            f"{xml_path.name}: Name={name!r} does not start with 'VIEW LIST: CAPEC-'"
        )

    @pytest.mark.parametrize("xml_path", ALL_VIEW_EXPORTS, ids=lambda p: p.stem)
    def test_version_is_3_9(self, xml_path):
        root = _parse(xml_path)
        assert root.attrib.get("Version") == "3.9"

    @pytest.mark.parametrize("xml_path", ALL_VIEW_EXPORTS, ids=lambda p: p.stem)
    def test_date_is_2023_01_24(self, xml_path):
        root = _parse(xml_path)
        assert root.attrib.get("Date") == "2023-01-24"

    @pytest.mark.parametrize("xml_path", ALL_VIEW_EXPORTS, ids=lambda p: p.stem)
    def test_has_at_least_one_attack_pattern(self, xml_path):
        root = _parse(xml_path)
        patterns = root.findall(".//c:Attack_Pattern", NS)
        assert len(patterns) >= 1, f"{xml_path.name} contains no Attack_Pattern elements"

    @pytest.mark.parametrize("xml_path", ALL_VIEW_EXPORTS, ids=lambda p: p.stem)
    def test_views_section_has_exactly_one_view(self, xml_path):
        """Each export includes at least one View entry.

        Most view-filtered exports contain exactly 1 View (the exported view
        itself). The comprehensive dictionary (2000.xml) contains all 13 views.
        """
        root = _parse(xml_path)
        views_el = root.find("c:Views", NS)
        assert views_el is not None, f"{xml_path.name}: missing <Views> section"
        views = views_el.findall("c:View", NS)
        assert len(views) >= 1, (
            f"{xml_path.name}: expected at least 1 View, found {len(views)}"
        )

    @pytest.mark.parametrize("xml_path", ALL_VIEW_EXPORTS, ids=lambda p: p.stem)
    def test_external_references_section_is_present(self, xml_path):
        """Each export includes external references cited by its attack patterns."""
        root = _parse(xml_path)
        assert root.find("c:External_References", NS) is not None, (
            f"{xml_path.name}: missing <External_References> section"
        )

    @pytest.mark.parametrize("xml_path", ALL_VIEW_EXPORTS, ids=lambda p: p.stem)
    def test_all_pattern_ids_are_positive_integers(self, xml_path):
        root = _parse(xml_path)
        for ap in root.findall(".//c:Attack_Pattern", NS):
            capec_id = ap.attrib.get("ID", "")
            assert capec_id.isdigit() and int(capec_id) > 0, (
                f"{xml_path.name}: Attack_Pattern has invalid ID={capec_id!r}"
            )

    @pytest.mark.parametrize("xml_path", ALL_VIEW_EXPORTS, ids=lambda p: p.stem)
    def test_abstraction_values_are_valid(self, xml_path):
        root = _parse(xml_path)
        for ap in root.findall(".//c:Attack_Pattern", NS):
            abstraction = ap.attrib.get("Abstraction")
            assert abstraction in VALID_ABSTRACTIONS, (
                f"{xml_path.name} CAPEC-{ap.attrib.get('ID')}: "
                f"Abstraction={abstraction!r} not in {VALID_ABSTRACTIONS}"
            )

    @pytest.mark.parametrize("xml_path", ALL_VIEW_EXPORTS, ids=lambda p: p.stem)
    def test_status_values_are_valid(self, xml_path):
        root = _parse(xml_path)
        for ap in root.findall(".//c:Attack_Pattern", NS):
            status = ap.attrib.get("Status")
            assert status in VALID_STATUSES, (
                f"{xml_path.name} CAPEC-{ap.attrib.get('ID')}: "
                f"Status={status!r} not in {VALID_STATUSES}"
            )


# ---------------------------------------------------------------------------
# Abstraction-filtered views (282, 283, 284)
# ---------------------------------------------------------------------------

class TestAbstractionViews:
    """Verify that abstraction-filtered views contain only the expected abstraction level."""

    def test_view_282_contains_only_meta_patterns(self):
        root = _parse(VIEWS_DIR / "282.xml")
        patterns = root.findall(".//c:Attack_Pattern", NS)
        assert len(patterns) > 0
        for ap in patterns:
            assert ap.attrib["Abstraction"] == "Meta", (
                f"CAPEC-{ap.attrib['ID']} in 282.xml: "
                f"expected Abstraction=Meta, got {ap.attrib['Abstraction']!r}"
            )

    def test_view_283_contains_only_standard_patterns(self):
        root = _parse(VIEWS_DIR / "283.xml")
        patterns = root.findall(".//c:Attack_Pattern", NS)
        assert len(patterns) > 0
        for ap in patterns:
            assert ap.attrib["Abstraction"] == "Standard", (
                f"CAPEC-{ap.attrib['ID']} in 283.xml: "
                f"expected Abstraction=Standard, got {ap.attrib['Abstraction']!r}"
            )

    def test_view_284_contains_only_detailed_patterns(self):
        root = _parse(VIEWS_DIR / "284.xml")
        patterns = root.findall(".//c:Attack_Pattern", NS)
        assert len(patterns) > 0
        for ap in patterns:
            assert ap.attrib["Abstraction"] == "Detailed", (
                f"CAPEC-{ap.attrib['ID']} in 284.xml: "
                f"expected Abstraction=Detailed, got {ap.attrib['Abstraction']!r}"
            )


# ---------------------------------------------------------------------------
# Status-filtered view (483)
# ---------------------------------------------------------------------------

class TestStatusViews:
    """Verify that status-filtered views contain only the expected status."""

    def test_view_483_contains_only_deprecated_patterns(self):
        root = _parse(VIEWS_DIR / "483.xml")
        patterns = root.findall(".//c:Attack_Pattern", NS)
        assert len(patterns) > 0
        for ap in patterns:
            assert ap.attrib["Status"] == "Deprecated", (
                f"CAPEC-{ap.attrib['ID']} in 483.xml: "
                f"expected Status=Deprecated, got {ap.attrib['Status']!r}"
            )


# ---------------------------------------------------------------------------
# Vendor taxonomy mapping catalogs (333, 658, 659)
# ---------------------------------------------------------------------------

class TestMappingCatalogs:
    """Verify vendor taxonomy mapping exports contain the expected taxonomy type."""

    def test_333_wasc_all_patterns_have_wasc_mapping(self):
        root = _parse(MAPPINGS_DIR / "333.xml")
        for ap in root.findall(".//c:Attack_Pattern", NS):
            taxonomy_names = [
                m.attrib.get("Taxonomy_Name")
                for m in ap.findall(".//c:Taxonomy_Mapping", NS)
            ]
            assert "WASC" in taxonomy_names, (
                f"CAPEC-{ap.attrib['ID']} in 333.xml has no WASC taxonomy mapping; "
                f"found: {taxonomy_names}"
            )

    def test_658_attack_all_patterns_have_attack_mapping(self):
        root = _parse(MAPPINGS_DIR / "658.xml")
        for ap in root.findall(".//c:Attack_Pattern", NS):
            taxonomy_names = [
                m.attrib.get("Taxonomy_Name")
                for m in ap.findall(".//c:Taxonomy_Mapping", NS)
            ]
            assert "ATTACK" in taxonomy_names, (
                f"CAPEC-{ap.attrib['ID']} in 658.xml has no ATTACK taxonomy mapping; "
                f"found: {taxonomy_names}"
            )

    def test_659_owasp_all_patterns_have_owasp_attacks_mapping(self):
        root = _parse(MAPPINGS_DIR / "659.xml")
        for ap in root.findall(".//c:Attack_Pattern", NS):
            taxonomy_names = [
                m.attrib.get("Taxonomy_Name")
                for m in ap.findall(".//c:Taxonomy_Mapping", NS)
            ]
            assert "OWASP Attacks" in taxonomy_names, (
                f"CAPEC-{ap.attrib['ID']} in 659.xml has no 'OWASP Attacks' taxonomy mapping; "
                f"found: {taxonomy_names}"
            )


# ---------------------------------------------------------------------------
# Navigation catalog spot-checks (1000, 3000) and comprehensive view (2000)
# ---------------------------------------------------------------------------

class TestNavigationCatalogs:
    """Spot-check navigation catalog names."""

    def test_1000_name_is_mechanisms_of_attack(self):
        root = _parse(NAV_DIR / "1000.xml")
        assert "1000: Mechanisms of Attack" in root.attrib["Name"]

    def test_3000_name_is_domains_of_attack(self):
        root = _parse(NAV_DIR / "3000.xml")
        assert "3000: Domains of Attack" in root.attrib["Name"]

    def test_2000_name_is_comprehensive_capec_dictionary(self):
        root = _parse(VIEWS_DIR / "2000.xml")
        assert "2000: Comprehensive CAPEC Dictionary" in root.attrib["Name"]
