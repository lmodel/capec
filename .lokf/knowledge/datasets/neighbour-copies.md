---
type: Dataset
id: https://w3id.org/lmodel/capec/knowledge/datasets/neighbour-copies
genre: reference
title: Neighbours' adapt copies
description: The adapt copies of eleven released lmodel repositories (slsa, github-actions, in-toto, oscal, spdx, stix, attack, uco, cve, kev-catalog and nist-nvd) and of lmodel/cwe's branch in `tests/neighbours/`, each pinned by its SHA-256, against which `tests/test_schema_rules.py` holds this schema's copy apart and `tests/test_mappings.py` holds the mappings.
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
  at: "2026-11-04T03:04:33Z"
status: draft
---

# Neighbours' adapt copies

Each file is the schema asset of a lmodel release, pinned in `tests/test_schema_rules.py` by its checksum.[^test_schema_rules.py]

The test fails on any shared class, enum or type, and on a shared key it does not list. It lists none for the eleven released copies, since the XSD's keys open with a capital and theirs do not. It lists 66 for lmodel/cwe, whose XSD MITRE writes in the same style, and whose copy comes from its branch until that repository has a release.[^test_schema_rules.py]

`tests/test_mappings.py` also reads these copies, to check the mappings to STIX, ATT&CK and CWE.[^test_mappings.py]

[^test_schema_rules.py]: tests/test_schema_rules.py, NEIGHBOURS
[^test_mappings.py]: tests/test_mappings.py, neighbour_iris
