---
type: GlossaryTerm
id: https://w3id.org/lmodel/capec/knowledge/glossary/adapt-copy
title: Adapt copy
description: "An adapt copy: the copy of a published LinkML schema that `lokf adapt` writes so that it can sit beside LOKF's `lokf.yaml` in a domain schema, with its chosen roots on `Concept`."
relatedTo:
  - https://w3id.org/lmodel/capec/knowledge/datasets/adapt-copy
sources:
  - id: project.justfile
    resource: project.justfile
    title: the comment above the recipes
generated:
  by: process:ktl-librarian
  at: "2026-11-04T02:37:57Z"
status: draft
---

# Adapt copy

`lokf adapt` copies a schema so that a bundle can use its classes as concept types. It re-roots the classes named with `--root` on LOKF's `Concept`, and folds the keys named with `--fold` into LOKF's own.[^project.justfile]

[^project.justfile]: project.justfile, the comment above the recipes
