---
type: Dataset
id: https://w3id.org/lmodel/capec/knowledge/datasets/example-data
genre: reference
title: Example data
description: "The examples `tests/test_data.py` checks: valid examples of each class, a counter-example for each constraint, and catalogues that break the rules a JSON Schema cannot state, in `tests/data/valid/`, `invalid/` and `problem/invalid/`."
resource: tests/data
about:
  - https://w3id.org/lmodel/capec/knowledge/datasets/capec-linkml-schema
sources:
  - id: data-readme
    resource: tests/data/README.md
  - id: test_data.py
    resource: tests/test_data.py
  - resource: tests/capec_xml.py
  - resource: tests/__init__.py
generated:
  by: process:ktl-librarian
  at: "2026-11-04T02:37:57Z"
status: draft
verified:
  - by: process:ktl-librarian
    at: "2026-11-04T02:44:15Z"
---

# Example data

`tests/data/valid/` holds examples of each class, and `tests/data/invalid/` a counter-example for each constraint the validator can state. A counter-example's first line says where it fails.[^data-readme]

`tests/data/problem/invalid/` holds a counter-example for each rule the generated JSON Schema cannot state, which `tests/capec_rules.py` checks.[^data-readme]

`tests/test_data.py` also builds each entry example back into XML and asks the XSD about it.[^test_data.py]

[^data-readme]: tests/data/README.md
[^test_data.py]: tests/test_data.py
