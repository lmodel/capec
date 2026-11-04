---
type: GlossaryTerm
id: https://w3id.org/lmodel/capec/knowledge/glossary/execution-flow
title: Execution flow
description: The steps an adversary typically takes in an attack, each with a number, a phase (`Explore`, `Experiment` or `Exploit`), a description and ways of doing it. The key is `Execution_Flow`, and the class of a step is `CapecAttackStep`.
definedBy:
  - https://w3id.org/lmodel/capec/knowledge/references/capec-xsd
relatedTo:
  - https://w3id.org/lmodel/capec/knowledge/glossary/attack-pattern
sources:
  - id: capec_entries.yaml
    resource: src/capec/schema/capec_entries.yaml
    title: CapecAttackStep and CapecAttackStepPhase
generated:
  by: process:ktl-librarian
  at: "2026-11-04T02:37:57Z"
status: draft
verified:
  - by: process:ktl-librarian
    at: "2026-11-04T02:44:15Z"
---

# Execution flow

The steps an adversary typically takes. Each step has a number, a phase, a description and ways of doing it.[^capec_entries.yaml]

The phases are `Explore`, `Experiment` and `Exploit`.[^capec_entries.yaml]

[^capec_entries.yaml]: src/capec/schema/capec_entries.yaml, CapecAttackStep and CapecAttackStepPhase
