---
type: Dataset
id: https://w3id.org/lmodel/capec/knowledge/datasets/entries-module
genre: reference
title: Entries module
description: "`src/capec/schema/capec_entries.yaml`, the module with `CapecAttackPattern`, `CapecCategory` and `CapecView`, the records an attack pattern holds, and the value lists they use, such as `CapecAbstraction` and `CapecRelatedNature`."
resource: src/capec/schema/capec_entries.yaml
isPartOf:
  - https://w3id.org/lmodel/capec/knowledge/datasets/capec-linkml-schema
dependsOn:
  - https://w3id.org/lmodel/capec/knowledge/datasets/core-module
sources:
  - id: capec_entries.yaml
    resource: src/capec/schema/capec_entries.yaml
generated:
  by: process:ktl-librarian
  at: "2026-11-04T02:37:57Z"
status: draft
verified:
  - by: process:ktl-librarian
    at: "2026-11-04T02:44:15Z"
---

# Entries module

The module declares the three kinds of entry under `CapecEntry`: `CapecAttackPattern`, `CapecCategory` and `CapecView`.[^capec_entries.yaml]

It also holds what those entries contain, such as `CapecAttackStep`, `CapecConsequence`, `CapecSkill`, `CapecRelatedAttackPattern` and `CapecRelatedWeakness`.[^capec_entries.yaml]

[^capec_entries.yaml]: src/capec/schema/capec_entries.yaml
