---
type: Explanation
id: https://w3id.org/lmodel/capec/knowledge/explanations/xml-to-data
genre: explanation
title: From XML to data
description: "Why a converter stands between the catalogue and the schema, and its rules: MITRE publishes XML, LinkML validates keys and values, and `scripts/capec_to_json.py` turns one into the other without changing a key or a value. A test turns the data back and finds the catalogue."
about:
  - https://w3id.org/lmodel/capec/knowledge/services/xml-converter
sources:
  - id: index.md
    resource: docs/index.md
    title: Validating a catalogue
  - id: capec_to_json.py
    resource: scripts/capec_to_json.py
    title: the docstring
  - id: test_conversion.py
    resource: tests/test_conversion.py
generated:
  by: process:ktl-librarian
  at: "2026-11-04T02:37:57Z"
status: draft
---

# From XML to data

MITRE publishes XML and LinkML validates a tree of keys and values, so the first step turns one into the other. It changes no key and no value.[^index.md]

The script reads what it needs from the XSD:[^capec_to_json.py]

- An attribute or a child element becomes a key of the same name, and a child that may repeat holds a list.
- An element whose whole content is one repeating child becomes a list under its own name.
- An element that holds text and has attributes becomes an object with its text under `Value`.
- Text that may hold XHTML becomes a string with that markup, its namespace prefix removed.

`tests/test_conversion.py` turns the data back into XML, finds it equal to the catalogue, and asks the XSD about it.[^test_conversion.py]

[^index.md]: docs/index.md, Validating a catalogue
[^capec_to_json.py]: scripts/capec_to_json.py, the docstring
[^test_conversion.py]: tests/test_conversion.py
