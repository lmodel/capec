---
type: Dataset
id: https://w3id.org/lmodel/capec/knowledge/datasets/neighbour-copies
genre: reference
title: Neighbours' adapt copies
description: The eleven released lmodel adapt copies in `tests/neighbours/` (slsa, github-actions, in-toto, oscal, spdx, stix, attack, uco, cve, kev-catalog and nist-nvd), each pinned by its SHA-256, against which `tests/test_schema_rules.py` holds this schema's copy apart.
resource: tests/neighbours
references:
  - https://w3id.org/lmodel/capec/knowledge/datasets/adapt-copy
sources:
  - id: test_schema_rules.py
    resource: tests/test_schema_rules.py
    title: NEIGHBOURS
  - id: test_mappings.py
    resource: tests/test_mappings.py
    title: neighbour_iris
generated:
  by: process:ktl-librarian
  at: "2026-11-04T02:37:57Z"
status: draft
---

# Neighbours' adapt copies

Each file is the schema asset of a lmodel release, pinned in `tests/test_schema_rules.py` by its checksum.[^test_schema_rules.py]

The test fails on any class, enum, type or key shared with a neighbour. There is none today, since the XSD's keys open with a capital.[^test_schema_rules.py]

`tests/test_mappings.py` also reads these copies, to check the mappings to STIX and ATT&CK.[^test_mappings.py]

[^test_schema_rules.py]: tests/test_schema_rules.py, NEIGHBOURS
[^test_mappings.py]: tests/test_mappings.py, neighbour_iris
