"""Checks the copy of the upstream, and that the schema names the same version.

upstream/ holds MITRE's XSD and catalogue at the pinned version. These tests hold them
to the git object hashes that scripts/check_upstream_release.py pins, and the schema's
headers to the version that script watches. They run offline.
"""

import hashlib
import importlib.util
import re
import xml.etree.ElementTree as ET
from pathlib import Path

import pytest
import yaml

ROOT = Path(__file__).parent.parent
UPSTREAM = ROOT / "upstream"
SCHEMA_DIR = ROOT / "src" / "capec" / "schema"
WATCH = ROOT / "scripts" / "check_upstream_release.py"
MODULES = {
    path.stem: yaml.safe_load(path.read_text()) for path in SCHEMA_DIR.glob("*.yaml")
}
XS = "{http://www.w3.org/2001/XMLSchema}"
# This project's own two files beside the copies, which the pins do not cover.
OWN_FILES = {"README.md", "TERMS.txt"}


def _watch():
    spec = importlib.util.spec_from_file_location("watch_pins", WATCH)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


PINS = _watch()


def _blob(path):
    data = path.read_bytes()
    return hashlib.sha1(b"blob %d\0" % len(data) + data).hexdigest()


def test_upstream_holds_exactly_the_pinned_files():
    """Nothing is added to the copy, and nothing is missing from it."""
    held = {
        p.relative_to(UPSTREAM).as_posix() for p in UPSTREAM.rglob("*") if p.is_file()
    }
    assert held == set(PINS.PINNED_BLOBS) | OWN_FILES


@pytest.mark.parametrize("name", sorted(PINS.PINNED_BLOBS))
def test_each_copy_is_the_pinned_blob(name):
    """Each file is byte for byte what MITRE serves."""
    assert _blob(UPSTREAM / name) == PINS.PINNED_BLOBS[name]


def test_every_module_names_the_pinned_version():
    """Each module's version is the version the watch pins."""
    for name, doc in MODULES.items():
        assert doc["version"] == PINS.PINNED_EDITION, name
        assert doc["source"] == PINS.PINNED_SOURCE, name
        assert doc["license"] == "Apache-2.0", name


def test_the_header_names_the_xsd_and_the_catalogue():
    annotations = MODULES["capec"]["annotations"]
    assert annotations["xsd_version"] == PINS.PINNED_XSD_VERSION
    assert annotations["xsd_namespace"] == PINS.PINNED_XSD_NAMESPACE
    assert annotations["catalogue_date"] == PINS.PINNED_DATE


def test_the_catalogue_is_this_version_and_names_this_xsd():
    root = ET.parse(UPSTREAM / "capec_v3.9.xml").getroot()
    assert root.tag == f"{{{PINS.PINNED_XSD_NAMESPACE}}}Attack_Pattern_Catalog"
    assert root.get("Version") == PINS.PINNED_EDITION
    assert root.get("Date") == PINS.PINNED_DATE
    location = root.get("{http://www.w3.org/2001/XMLSchema-instance}schemaLocation")
    assert location.endswith(f"ap_schema_v{PINS.PINNED_XSD_VERSION}.xsd")


def test_the_xsd_is_this_version():
    root = ET.parse(UPSTREAM / "ap_schema_v3.5.xsd").getroot()
    assert root.get("targetNamespace") == PINS.PINNED_XSD_NAMESPACE
    assert root.find(f"{XS}annotation/{XS}appinfo/version").text == "3.5.0"
    # The header's date is the XSD's own, written another way.
    assert root.find(f"{XS}annotation/{XS}appinfo/date").text == "21 October 2021"
    assert MODULES["capec"]["annotations"]["xsd_date"] == "2021-10-21"


def test_the_xsd_keeps_its_licence_header():
    """The XSD's header asks that a copy keep it, and a copy here is unchanged."""
    assert "this license header must be included" in (
        UPSTREAM / "ap_schema_v3.5.xsd"
    ).read_text(encoding="utf-8")


def test_notice_says_no_endorsement_and_reproduces_the_terms():
    notice = (ROOT / "NOTICE").read_text(encoding="utf-8")
    assert "endorsement" in notice
    for phrase in (
        "Copyright (c) 2007-2026, The MITRE Corporation",
        "trademarks of The MITRE Corporation",
        "Any copy you make for such",
        "ALL DOCUMENTS AND THE INFORMATION CONTAINED THEREIN",
    ):
        assert phrase in notice, phrase


def test_the_terms_are_beside_the_copies():
    """The Terms of Use ask each copy to reproduce the designation and licence."""
    terms = (UPSTREAM / "TERMS.txt").read_text(encoding="utf-8")
    assert "The MITRE Corporation" in terms
    assert "Any copy you make for such" in terms


def test_the_pinned_terms_hash_covers_this_text():
    """The text in TERMS.txt, read as the watch reads the page, has the pinned hash."""
    terms = (UPSTREAM / "TERMS.txt").read_text(encoding="utf-8")
    body = terms[terms.index("The MITRE Corporation (MITRE) hereby") :]
    text = " ".join(body.replace("DISCLAIMERS", " ").split())
    assert hashlib.sha256(text.encode("utf-8")).hexdigest() == PINS.PINNED_TERMS_SHA256


def _xsd_documentation():
    root = ET.parse(UPSTREAM / "ap_schema_v3.5.xsd").getroot()
    return [node.text or "" for node in root.iter(f"{XS}documentation")]


def _yaml_descriptions(node):
    if isinstance(node, dict):
        for key, value in node.items():
            if key == "description" and isinstance(value, str):
                yield value
            else:
                yield from _yaml_descriptions(value)
    elif isinstance(node, list):
        for item in node:
            yield from _yaml_descriptions(item)


def _words(text):
    return re.findall(r"[a-z0-9']+", text.lower())


def _runs(words, size):
    return {tuple(words[i : i + size]) for i in range(len(words) - size + 1)}


# A run this long cannot arise by chance in a short hint, though a shorter one can.
RUN = 6


def test_no_description_copies_the_upstreams_text():
    """A description here is this project's own: none shares a run of six words with
    the XSD's documentation."""
    upstream = set()
    for text in _xsd_documentation():
        upstream |= _runs(_words(text), RUN)
    shared = []
    for name, doc in MODULES.items():
        for text in _yaml_descriptions(doc):
            found = _runs(_words(text), RUN) & upstream
            if found:
                shared.append((name, text, sorted(found)[:2]))
    assert not shared, shared


def test_each_description_is_short():
    """A description fits a form's hint: one or two sentences, with caveats in
    comments and decisions in notes."""
    long = [
        text
        for doc in MODULES.values()
        for text in _yaml_descriptions(doc)
        if len(re.findall(r"[.!?](?:\s|$)", text)) > 2 or len(text) > 240
    ]
    assert not long, long
