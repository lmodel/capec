---
type: Service
id: https://w3id.org/lmodel/capec/knowledge/services/xml-converter
genre: reference
title: XML converter
description: "`scripts/capec_to_json.py`, the command that turns the CAPEC catalogue's XML into the data the schema describes, by rules it reads from the XSD. It uses only the standard library and is deterministic."
resource: scripts/capec_to_json.py
dependsOn:
  - https://w3id.org/lmodel/capec/knowledge/datasets/upstream-copy
sources:
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

# XML converter

The script reads the catalogue and the XSD, the copies in `upstream/` by default, and writes JSON to standard output or to `--output`.[^capec_to_json.py]

It has a PEP 723 header and uses only the standard library. The standard library's parser reads no external entity.[^capec_to_json.py]

Two runs write the same bytes, and the data turns back into the catalogue.[^test_conversion.py]

[^capec_to_json.py]: scripts/capec_to_json.py, the docstring
[^test_conversion.py]: tests/test_conversion.py
