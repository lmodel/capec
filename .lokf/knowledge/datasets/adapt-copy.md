---
type: Dataset
id: https://w3id.org/lmodel/capec/knowledge/datasets/adapt-copy
genre: reference
title: The schema's adapt copy
description: "`.lokf/capec.yaml`, the copy `just lokf-adapt` writes from the schema so that it sits beside LOKF's `lokf.yaml`: rooted on `CapecEntry` and `CapecExternalReference`, with `ID` and `Reference_ID` dropped for LOKF's `id`, and five keys folded into `title` and `description`."
resource: .lokf/capec.yaml
derivedFrom:
  - https://w3id.org/lmodel/capec/knowledge/datasets/capec-linkml-schema
about:
  - https://w3id.org/lmodel/capec/knowledge/glossary/adapt-copy
sources:
  - id: project.justfile
    resource: project.justfile
    title: the comment above the recipes
  - id: readme.md
    resource: README.md
    title: the Knowledge Trust Ladder (KTL) section
  - id: test_schema_rules.py
    resource: tests/test_schema_rules.py
    title: FOLDED
  - resource: .lokf/capec.yaml
  - resource: .lokf/justfile
    title: the schema line
  - resource: .lokf/pyproject.toml
    title: the lokf floor and the schema setting
generated:
  by: process:ktl-librarian
  at: "2026-11-04T02:37:57Z"
status: draft
verified:
  - by: process:ktl-librarian
    at: "2026-11-04T02:44:15Z"
---

# The schema's adapt copy

`just lokf-adapt` writes `.lokf/capec.yaml` from `src/capec/schema/capec.yaml`, and `just lokf-adapt-check` fails when it is stale. CI runs the check.[^project.justfile]

A concept may name `CapecAttackPattern`, `CapecCategory`, `CapecView` or `CapecExternalReference` as its `type`. The smaller records stay values inside an entry.[^readme.md]

`Name` and `Title` fold into LOKF's `title`, and `Description`, `Summary` and `Objective` into its `description`.[^test_schema_rules.py]

A release attaches the copy as `schema-<tag>-capec.yaml`.[^readme.md]

[^project.justfile]: project.justfile, the comment above the recipes
[^readme.md]: README.md, the Knowledge Trust Ladder (KTL) section
[^test_schema_rules.py]: tests/test_schema_rules.py, FOLDED
