---
type: Explanation
id: https://w3id.org/lmodel/capec/knowledge/explanations/mappings
genre: explanation
title: Mappings
description: "Where the schema crosses to other vocabularies: STIX, ATT&CK, CWE, the SEPSES CAPEC ontology, SKOS, Dublin Core, schema.org and Wikidata. The schema is the one home for mappings, and each is read at its source and held by a test."
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
  at: "2026-11-04T03:04:33Z"
status: draft
verified:
  - by: process:ktl-librarian
    at: "2026-11-04T02:44:15Z"
---

# Mappings

The schema is the one home for mappings, and `tests/test_mappings.py` holds each to a pinned term list or a released copy.[^readme.md]

MITRE publishes the same entries in STIX as attack-pattern objects, in the mitre/cti repository, and marks each with a capec external reference, so the STIX mapping is close. ATT&CK describes a technique an adversary was seen to use, and the taxonomy mappings join it to a pattern, so that mapping is only related.[^capec_entries.yaml]

CWE holds the link between a weakness and an attack pattern from its own side, and CAPEC 3.9 and CWE 5.0 each name the same 1212 pairs. So the two classes are the two ends of one link, and the mapping to lmodel/cwe is `related`.[^capec_entries.yaml]

[^readme.md]: README.md, Mappings
[^capec_entries.yaml]: src/capec/schema/capec_entries.yaml, the comments on CapecAttackPattern
