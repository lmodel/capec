---
type: Dataset
id: https://w3id.org/lmodel/capec/knowledge/datasets/capec-linkml-schema
genre: reference
title: capec LinkML schema
description: "The LinkML model of CAPEC 3.9 under its XSD 3.5, `src/capec/schema/capec.yaml` (schema id `https://w3id.org/lmodel/capec`): an umbrella that holds only the tree root, `CapecAttackPatternCatalog`, over the modules `capec_entries` and `capec_core`."
resource: src/capec/schema/capec.yaml
hasPart:
  - https://w3id.org/lmodel/capec/knowledge/datasets/core-module
  - https://w3id.org/lmodel/capec/knowledge/datasets/entries-module
derivedFrom:
  - https://w3id.org/lmodel/capec/knowledge/references/capec-xsd
  - https://w3id.org/lmodel/capec/knowledge/references/capec-catalogue
sources:
  - id: capec.yaml
    resource: src/capec/schema/capec.yaml
    title: the header and the class
  - id: test_coverage.py
    resource: tests/test_coverage.py
    title: the docstring
generated:
  by: process:ktl-librarian
  at: "2026-11-04T02:37:57Z"
status: draft
---

# capec LinkML schema

`src/capec/schema/capec.yaml` is the file the project names. It imports the two modules and declares one class, `CapecAttackPatternCatalog`, the tree root.[^capec.yaml]

The header's `version` is 3.9, the version of the catalogue that it renders, and its `source` is the address of the XSD. Its annotations name the XSD's version, namespace and date and the catalogue's date. Its `license` is Apache-2.0, the project's own.[^capec.yaml]

Each class and enum carries an `xsd_type` annotation naming the XSD type or path it renders, and `tests/test_coverage.py` compares the XSD with the classes and enums in both directions.[^test_coverage.py]

[^capec.yaml]: src/capec/schema/capec.yaml, the header and the class
[^test_coverage.py]: tests/test_coverage.py, the docstring
