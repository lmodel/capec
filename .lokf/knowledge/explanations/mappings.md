---
type: Explanation
id: https://w3id.org/lmodel/capec/knowledge/explanations/mappings
genre: explanation
title: Mappings
description: "Where the schema crosses to other vocabularies: STIX, ATT&CK, the SEPSES CAPEC ontology, SKOS, Dublin Core, schema.org and Wikidata. The schema is the one home for mappings, and each is read at its source and held by a test."
about:
  - https://w3id.org/lmodel/capec/knowledge/datasets/capec-linkml-schema
references:
  - https://w3id.org/lmodel/capec/knowledge/datasets/mapping-term-list
  - https://w3id.org/lmodel/capec/knowledge/datasets/neighbour-copies
sources:
  - id: readme.md
    resource: README.md
    title: Mappings
  - id: capec_entries.yaml
    resource: src/capec/schema/capec_entries.yaml
    title: the comments on CapecAttackPattern
generated:
  by: process:ktl-librarian
  at: "2026-11-04T02:37:57Z"
status: draft
---

# Mappings

The schema is the one home for mappings, and `tests/test_mappings.py` holds each to a pinned term list or a released copy.[^readme.md]

MITRE publishes the same entries in STIX as attack-pattern objects, in the mitre/cti repository, and marks each with a capec external reference, so the STIX mapping is close. ATT&CK describes a technique an adversary was seen to use, and the taxonomy mappings join it to a pattern, so that mapping is only related.[^capec_entries.yaml]

[^readme.md]: README.md, Mappings
[^capec_entries.yaml]: src/capec/schema/capec_entries.yaml, the comments on CapecAttackPattern
