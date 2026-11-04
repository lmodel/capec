#!/usr/bin/env python3
# /// script
# requires-python = ">=3.10"
# dependencies = []
# ///
"""Turn the CAPEC catalogue's XML into the data the LinkML schema describes.

MITRE publishes the catalogue as XML, and LinkML validates a tree of keys and
values, so something must stand between them. This script is that step. It changes
no key and no value, and it reads what it needs to know from the XSD, by these
rules:

- An attribute becomes a key of the same name.
- A child element becomes a key of the same name, and its value is a list when the
  XSD lets it repeat.
- An element whose whole content is one repeating child is a wrapper. It becomes a
  list under the wrapper's name, so `Related_Attack_Patterns` holds the patterns
  directly and the name `Related_Attack_Pattern` is implied. An element with several
  kinds of child, such as `Content_History`, stays an object of lists.
- An element that holds text and has attributes becomes an object whose text sits
  under the key `Value`, as for `Note`, `Skill` and `Previous_Entry_Name`.
- An element of the XSD's `StructuredTextType` becomes a string holding its inner
  XHTML, with the namespace prefix removed and the outer whitespace stripped.
- An `xs:integer` attribute names an entry, so it stays a string of digits. The one
  `xs:integer` element, `Step`, counts, so it becomes a number.

tests/test_conversion.py turns the output back into XML and finds it equal to the
catalogue, so nothing is lost. The standard library's parser reads no external
entity. Usage::

    python scripts/capec_to_json.py [CATALOGUE [XSD]] [--output FILE]

The defaults are the copies in upstream/, and the output goes to standard output.
"""

from __future__ import annotations

import argparse
import json
import sys
import xml.etree.ElementTree as ET
from dataclasses import dataclass, field
from pathlib import Path
from xml.sax.saxutils import escape, quoteattr

ROOT = Path(__file__).resolve().parent.parent
CATALOGUE = ROOT / "upstream" / "capec_v3.9.xml"
XSD = ROOT / "upstream" / "ap_schema_v3.5.xsd"

XS = "{http://www.w3.org/2001/XMLSchema}"
XSI = "{http://www.w3.org/2001/XMLSchema-instance}"
STRUCTURED = "StructuredTextType"


@dataclass
class Child:
    """A child element the XSD allows, with how often it may appear."""

    key: str
    least: int
    most: int  # 0 means unbounded.
    shape: "Shape"

    @property
    def repeats(self) -> bool:
        return self.most != 1


@dataclass
class Attribute:
    """An attribute the XSD allows."""

    key: str
    required: bool
    xsd_type: str | None
    values: tuple[str, ...] = ()


@dataclass
class Shape:
    """What the XSD says an element holds."""

    # The name by which the test and the schema refer to it: a named type, or the
    # path of an anonymous one, such as ConsequencesType/Consequence.
    name: str
    xsd_type: str | None = None
    text: str | None = None  # None, "plain" or "structured".
    attributes: list[Attribute] = field(default_factory=list)
    children: list[Child] = field(default_factory=list)
    values: tuple[str, ...] = ()

    @property
    def is_scalar(self) -> bool:
        return not self.attributes and not self.children

    @property
    def wrapped(self) -> Child | None:
        """The one repeating child, if this element only wraps it."""
        if (
            not self.attributes
            and not self.text
            and len(self.children) == 1
            and self.children[0].repeats
        ):
            return self.children[0]
        return None


def _local(tag: str) -> str:
    return tag.rsplit("}", 1)[-1]


def _unprefixed(qname: str | None) -> str | None:
    return qname.split(":", 1)[-1] if qname else qname


class Xsd:
    """The XSD's named types, read into shapes on demand."""

    def __init__(self, path: Path):
        self.root = ET.parse(path).getroot()
        self.types = {
            node.get("name"): node
            for node in self.root
            if node.tag in (XS + "complexType", XS + "simpleType")
        }
        self.cache: dict[str, Shape] = {}

    def enumeration(self, node: ET.Element) -> tuple[str, ...]:
        return tuple(item.get("value") for item in node.iter(XS + "enumeration"))

    def attribute(self, node: ET.Element) -> Attribute:
        kind = _unprefixed(node.get("type"))
        values = self.enumeration(node)
        if kind in self.types:
            values = self.enumeration(self.types[kind])
        return Attribute(
            key=node.get("name"),
            required=node.get("use") == "required",
            xsd_type=kind,
            values=values,
        )

    def named(self, name: str) -> Shape:
        if name not in self.cache:
            self.cache[name] = shape = Shape(name, xsd_type=name)
            self._fill(shape, self.types[name])
        return self.cache[name]

    def _child(self, node: ET.Element, owner: str) -> Child:
        key = node.get("name")
        kind = _unprefixed(node.get("type"))
        if kind in self.types:
            shape = self.named(kind)
        else:
            name = f"{owner}/{key}" if owner else key
            shape = Shape(name, xsd_type=node.get("type"))
            self._fill(shape, node)
        most = node.get("maxOccurs", "1")
        return Child(
            key=key,
            least=int(node.get("minOccurs", "1")),
            most=0 if most == "unbounded" else int(most),
            shape=shape,
        )

    def _fill(self, shape: Shape, node: ET.Element) -> None:
        """Read a type, or an element's anonymous type, into a shape."""
        if node.tag == XS + "simpleType" or node.find(XS + "simpleType") is not None:
            shape.text = "plain"
            shape.values = self.enumeration(node)
            return
        if shape.name == STRUCTURED:
            shape.text = "structured"
            return
        complex_type = (
            node if node.tag == XS + "complexType" else node.find(XS + "complexType")
        )
        if complex_type is None:
            shape.text = "plain"
            return
        content = complex_type
        for holder in ("simpleContent", "complexContent"):
            found = complex_type.find(XS + holder)
            if found is not None:
                content = found.find(XS + "extension")
                base = _unprefixed(content.get("base"))
                shape.text = "structured" if base == STRUCTURED else "plain"
        for sequence in content.findall(XS + "sequence"):
            for child in sequence.findall(XS + "element"):
                shape.children.append(self._child(child, shape.name))
        for attribute in content.findall(XS + "attribute"):
            shape.attributes.append(self.attribute(attribute))

    def root_element(self) -> Child:
        node = self.root.find(XS + "element")
        return self._child(node, "")


def _xhtml(node: ET.Element) -> str:
    """One XHTML element as text, with its namespace prefix removed."""
    tag = _local(node.tag)
    attributes = "".join(
        f" {_local(name)}={quoteattr(value)}" for name, value in node.attrib.items()
    )
    inner = _inner(node)
    return f"<{tag}{attributes}>{inner}</{tag}>" if inner else f"<{tag}{attributes}/>"


def _inner(node: ET.Element) -> str:
    """Everything inside an element, as text."""
    parts = [escape(node.text or "")]
    for child in node:
        parts.append(_xhtml(child))
        parts.append(escape(child.tail or ""))
    return "".join(parts)


def _scalar(node: ET.Element, shape: Shape):
    if shape.text == "structured":
        return _inner(node).strip()
    if shape.xsd_type == "xs:integer":
        return int(node.text)
    return node.text or ""


def convert(node: ET.Element, shape: Shape):
    """The data for one element, by the rules this module opens with."""
    wrapped = shape.wrapped
    if wrapped:
        return [
            convert(item, wrapped.shape) for item in node.findall(f"{{*}}{wrapped.key}")
        ]
    if shape.is_scalar:
        return _scalar(node, shape)
    data = {}
    for attribute in shape.attributes:
        if attribute.key in node.attrib:
            data[attribute.key] = node.attrib[attribute.key]
    for child in shape.children:
        found = node.findall(f"{{*}}{child.key}")
        if child.repeats and found:
            data[child.key] = [convert(item, child.shape) for item in found]
        elif found:
            data[child.key] = convert(found[0], child.shape)
    if shape.text:
        data["Value"] = _scalar(node, shape)
    return data


def catalogue_data(catalogue: Path = CATALOGUE, xsd: Path = XSD) -> dict:
    """The whole catalogue as the data the schema describes."""
    node = ET.parse(catalogue).getroot()
    return convert(node, Xsd(xsd).root_element().shape)


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("catalogue", nargs="?", type=Path, default=CATALOGUE)
    parser.add_argument("xsd", nargs="?", type=Path, default=XSD)
    parser.add_argument(
        "--output", type=Path, help="Write here, not to standard output"
    )
    args = parser.parse_args(argv)
    data = catalogue_data(args.catalogue, args.xsd)
    text = json.dumps(data, ensure_ascii=False, indent=1)
    if args.output:
        args.output.write_text(text + "\n", encoding="utf-8")
    else:
        sys.stdout.write(text + "\n")
    return 0


if __name__ == "__main__":
    sys.exit(main())
