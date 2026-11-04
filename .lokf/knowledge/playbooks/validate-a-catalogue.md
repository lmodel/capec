---
type: Playbook
id: https://w3id.org/lmodel/capec/knowledge/playbooks/validate-a-catalogue
genre: how-to
title: Validate a catalogue
description: "How to validate a CAPEC catalogue: turn the XML into data with `scripts/capec_to_json.py`, run `linkml-validate` with the class `CapecAttackPatternCatalog`, and run `tests/capec_rules.py` for what a JSON Schema cannot state."
references:
  - https://w3id.org/lmodel/capec/knowledge/services/xml-converter
  - https://w3id.org/lmodel/capec/knowledge/explanations/rules-in-python
sources:
  - id: index.md
    resource: docs/index.md
    title: Validating a catalogue
generated:
  by: process:ktl-librarian
  at: "2026-11-04T02:37:57Z"
status: draft
---

# Validate a catalogue

1. Run `uv run scripts/capec_to_json.py upstream/capec_v3.9.xml upstream/ap_schema_v3.5.xsd --output catalogue.json`.[^index.md]
2. Run `uv run linkml-validate -s src/capec/schema/capec.yaml -C CapecAttackPatternCatalog catalogue.json`.[^index.md]
3. Run the checks in `tests/capec_rules.py` to check the references and the numbers.[^index.md]

`just validate-catalogue` runs the first two on the copy in `upstream/`.[^index.md]

[^index.md]: docs/index.md, Validating a catalogue
