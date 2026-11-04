---
type: Dataset
id: https://w3id.org/lmodel/capec/knowledge/datasets/core-module
genre: reference
title: Core module
description: "`src/capec/schema/capec_core.yaml`, the module with the value lists, text types and small records every CAPEC entry shares, and the abstract `CapecEntry`. It imports only `linkml:types`."
resource: src/capec/schema/capec_core.yaml
isPartOf:
  - https://w3id.org/lmodel/capec/knowledge/datasets/capec-linkml-schema
sources:
  - id: capec_core.yaml
    resource: src/capec/schema/capec_core.yaml
generated:
  by: process:ktl-librarian
  at: "2026-11-04T02:37:57Z"
status: draft
verified:
  - by: process:ktl-librarian
    at: "2026-11-04T02:44:15Z"
---

# Core module

The module holds the types for a CAPEC number, a reference identifier, text with XHTML, a web address and the XSD's year, month and day forms.[^capec_core.yaml]

It holds the records for an external reference, a citation, a note, a taxonomy mapping, an excluded ancestor and an entry's history, and the two mixins for the fields those classes share.[^capec_core.yaml]

`CapecEntry` is abstract and holds what the three kinds of entry share. The XSD has no such base. It repeats those fields on its three entry types.[^capec_core.yaml]

[^capec_core.yaml]: src/capec/schema/capec_core.yaml
