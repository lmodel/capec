---
type: GlossaryTerm
id: https://w3id.org/lmodel/capec/knowledge/glossary/abstraction-level
title: Abstraction level
description: "How concrete an attack pattern is: `Meta` for a broad approach, `Standard` for one method or technique, and `Detailed` for one technique against one technology. The enum is `CapecAbstraction`."
definedBy:
  - https://w3id.org/lmodel/capec/knowledge/references/capec-xsd
relatedTo:
  - https://w3id.org/lmodel/capec/knowledge/glossary/attack-pattern
sources:
  - id: capec_entries.yaml
    resource: src/capec/schema/capec_entries.yaml
    title: CapecAbstraction
generated:
  by: process:ktl-librarian
  at: "2026-11-04T02:37:57Z"
status: draft
---

# Abstraction level

How concrete an attack pattern is:[^capec_entries.yaml]

- `Meta` is a broad approach, free of any one technology.
- `Standard` is one method or technique, often only a part of a whole attack.
- `Detailed` is one technique against one technology, usually with its steps set out.

[^capec_entries.yaml]: src/capec/schema/capec_entries.yaml, CapecAbstraction
