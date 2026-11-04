"""Turn the schema's data back into the catalogue's XML, for the tests alone.

scripts/capec_to_json.py goes one way. This module goes the other, by the same
reading of the XSD, so that a test can compare the result with the catalogue, and
so that the XSD itself can be asked about an example.
"""

from __future__ import annotations

import importlib.util
import re
import sys
import xml.etree.ElementTree as ET
from functools import cache
from pathlib import Path

from lxml import etree

ROOT = Path(__file__).parent.parent
XSD_FILE = ROOT / "upstream" / "ap_schema_v3.5.xsd"
CATALOGUE_FILE = ROOT / "upstream" / "capec_v3.9.xml"
NAMESPACE = "http://capec.mitre.org/capec-3"
XHTML = "http://www.w3.org/1999/xhtml"
XSI = "{http://www.w3.org/2001/XMLSchema-instance}"


def _load():
    path = ROOT / "scripts" / "capec_to_json.py"
    spec = importlib.util.spec_from_file_location("capec_to_json", path)
    module = importlib.util.module_from_spec(spec)
    # The dataclasses in the script look their module up while they are built.
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


converter = _load()


@cache
def xsd():
    """The XSD, read once."""
    return converter.Xsd(XSD_FILE)


def _text(node: ET.Element, text: str, structured: bool) -> None:
    if not structured:
        node.text = text
        return
    wrapper = ET.fromstring(f'<wrapper xmlns="{XHTML}">{text}</wrapper>')
    node.text = wrapper.text
    node.extend(list(wrapper))


def build(tag: str, data, shape) -> ET.Element:
    """One element from its data, by the rules the converter states."""
    node = ET.Element(f"{{{NAMESPACE}}}{tag}")
    wrapped = shape.wrapped
    if wrapped:
        for item in data:
            node.append(build(wrapped.key, item, wrapped.shape))
        return node
    if shape.is_scalar:
        _text(node, str(data), shape.text == "structured")
        return node
    for attribute in shape.attributes:
        if attribute.key in data:
            node.set(attribute.key, data[attribute.key])
    if shape.text:
        _text(node, data["Value"], shape.text == "structured")
    for child in shape.children:
        if child.key not in data:
            continue
        values = data[child.key] if child.repeats else [data[child.key]]
        for value in values:
            node.append(build(child.key, value, child.shape))
    return node


def catalogue_element(data) -> ET.Element:
    """A whole catalogue as XML."""
    root = xsd().root_element()
    return build(root.key, data, root.shape)


def canonical(node: ET.Element):
    """An element as a comparable tree, ignoring the whitespace around each text and
    the schemaLocation hint, which says nothing about the content."""
    attributes = sorted(
        (name, value) for name, value in node.attrib.items() if not name.startswith(XSI)
    )
    return (
        node.tag,
        attributes,
        (node.text or "").strip(),
        [(canonical(child), (child.tail or "").strip()) for child in node],
    )


@cache
def _validator():
    """The XSD, able to run offline. It imports the XHTML schema from w3.org to
    check the markup inside text, so that import goes and the markup is left
    unchecked, while everything else stays as MITRE wrote it."""
    text = XSD_FILE.read_bytes()
    text = re.sub(rb"<xs:import [^>]*/>", b"", text)
    text = text.replace(b'processContents="strict"', b'processContents="lax"')
    parser = etree.XMLParser(no_network=True, resolve_entities=False, huge_tree=True)
    return etree.XMLSchema(etree.fromstring(text, parser))


def xsd_errors(element: ET.Element) -> list[str]:
    """What the XSD says about a catalogue element."""
    document = etree.fromstring(ET.tostring(element))
    validator = _validator()
    validator.validate(document)
    return [error.message for error in validator.error_log]


def wrapped_in_a_catalogue(class_name: str, data) -> dict | None:
    """An example of an entry or a reference, as the one member of a catalogue."""
    lists = {
        "CapecAttackPattern": "Attack_Patterns",
        "CapecCategory": "Categories",
        "CapecView": "Views",
        "CapecExternalReference": "External_References",
    }
    header = {"Name": "CAPEC", "Version": "3.9", "Date": "2023-01-24"}
    if class_name == "CapecAttackPatternCatalog":
        return data
    if class_name in lists:
        return {**header, lists[class_name]: [data]}
    return None
