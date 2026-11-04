"""Checks scripts/capec_to_json.py: its rules, and that it loses nothing."""

import json
import subprocess
import sys
import xml.etree.ElementTree as ET

import pytest

from tests import capec_xml
from tests.capec_xml import CATALOGUE_FILE, canonical, catalogue_element, converter

XS_NAMESPACE = "http://capec.mitre.org/capec-3"
XHTML = "http://www.w3.org/1999/xhtml"


@pytest.fixture(scope="module")
def data():
    return converter.catalogue_data()


def test_turning_the_output_back_gives_the_catalogue(data):
    """Nothing is lost: every element, attribute and text, the XHTML included, comes
    back as it was, in the same order."""
    original = ET.parse(CATALOGUE_FILE).getroot()
    assert canonical(catalogue_element(data)) == canonical(original)


def test_the_output_comes_back_valid_under_the_xsd(data):
    """The XSD accepts the XML built back from the data."""
    assert capec_xml.xsd_errors(catalogue_element(data)) == []


def test_the_keys_at_the_top_are_the_xsds(data):
    assert list(data) == [
        "Name",
        "Version",
        "Date",
        "Attack_Patterns",
        "Categories",
        "Views",
        "External_References",
    ]
    assert (data["Name"], data["Version"], data["Date"]) == (
        "CAPEC",
        "3.9",
        "2023-01-24",
    )


def test_a_wrapper_becomes_a_list_under_its_own_name(data):
    pattern = next(p for p in data["Attack_Patterns"] if p["ID"] == "1")
    assert isinstance(pattern["Related_Attack_Patterns"], list)
    assert pattern["Related_Attack_Patterns"][0] == {
        "Nature": "ChildOf",
        "CAPEC_ID": "122",
    }
    assert isinstance(pattern["Prerequisites"], list)
    assert isinstance(pattern["Prerequisites"][0], str)


def test_an_element_of_several_kinds_of_child_stays_an_object(data):
    pattern = next(p for p in data["Attack_Patterns"] if p["ID"] == "1")
    history = pattern["Content_History"]
    assert isinstance(history["Submission"], dict)
    assert isinstance(history["Modification"], list)


def test_text_with_attributes_sits_under_value():
    node = ET.fromstring(
        f'<Note xmlns="{XS_NAMESPACE}" Type="Other">A <b xmlns="{XHTML}">bold</b> note</Note>'
    )
    shape = capec_xml.xsd().named("NotesType").children[0].shape
    assert converter.convert(node, shape) == {
        "Type": "Other",
        "Value": "A <b>bold</b> note",
    }


def test_structured_text_keeps_its_markup_without_the_prefix():
    node = ET.fromstring(
        f'<Description xmlns="{XS_NAMESPACE}" xmlns:xhtml="{XHTML}">\n'
        '  <xhtml:p class="a">One &amp; two &lt; three</xhtml:p>\n'
        "  <xhtml:br/>tail\n"
        "</Description>"
    )
    shape = capec_xml.xsd().named("StructuredTextType")
    assert converter.convert(node, shape) == (
        '<p class="a">One &amp; two &lt; three</p>\n  <br/>tail'
    )


def test_an_attribute_keeps_digits_as_a_string_and_step_is_a_number(data):
    pattern = next(p for p in data["Attack_Patterns"] if p["ID"] == "1")
    assert pattern["ID"] == "1"
    assert pattern["Execution_Flow"][0]["Step"] == 1


def test_a_value_keeps_its_own_spaces(data):
    """Nothing tidies a value: this name ends in a space upstream."""
    view = next(v for v in data["Views"] if v["ID"] == "658")
    assert view["Name"] == "ATT&CK Related Patterns "


def _catalogue(inside="", attributes=""):
    return ET.fromstring(
        f'<Attack_Pattern_Catalog xmlns="{XS_NAMESPACE}" Name="CAPEC" Version="3.9" '
        f'Date="2023-01-24"{attributes}>{inside}</Attack_Pattern_Catalog>'
    )


def test_the_converter_stops_on_what_the_xsd_does_not_declare():
    """A key from outside the XSD, or a second copy of a key the XSD allows once, is a
    departure to notice, not to drop."""
    shape = capec_xml.xsd().root_element().shape
    with pytest.raises(ValueError, match="declares no element Not_A_Key"):
        converter.convert(_catalogue("<Not_A_Key/>"), shape)
    with pytest.raises(ValueError, match="declares no attribute Not_A_Key"):
        converter.convert(_catalogue(attributes=' Not_A_Key="x"'), shape)
    with pytest.raises(ValueError, match="allows one Views, not 2"):
        converter.convert(_catalogue("<Views/><Views/>"), shape)
    with pytest.raises(ValueError, match="declares no element Not_A_Key"):
        converter.convert(_catalogue("<Views><Not_A_Key/></Views>"), shape)


def test_two_runs_write_the_same_bytes(tmp_path):
    """The conversion is deterministic, and it runs as the docs say it does."""
    script = capec_xml.ROOT / "scripts" / "capec_to_json.py"
    first, second = tmp_path / "1.json", tmp_path / "2.json"
    for output in (first, second):
        subprocess.run(
            [sys.executable, "-I", str(script), "--output", str(output)], check=True
        )
    assert first.read_bytes() == second.read_bytes()
    assert json.loads(first.read_text(encoding="utf-8"))["Version"] == "3.9"
