---
type: Explanation
id: https://w3id.org/lmodel/capec/knowledge/explanations/generator-limits
genre: explanation
title: What the generators do with these keys
description: "How LinkML's generators treat the XSD's short keys: `gen-owl` warns that six keys shared across classes are ambiguous and gives them no label, the JSON-LD context gives a key one IRI, and the key `Date` shares a docs page with LinkML's type."
about:
  - https://w3id.org/lmodel/capec/knowledge/datasets/generated-artefacts
sources:
  - id: about.md
    resource: docs/about.md
    title: What the generators do with these keys
generated:
  by: process:ktl-librarian
  at: "2026-11-04T02:37:57Z"
status: draft
---

# What the generators do with these keys

Several classes share a short key, such as `Name`, `Type`, `Value` and `Description`, and each keeps one IRI under the schema's prefix.[^about.md]

`gen-owl` warns that those six keys are ambiguous and gives their properties no label or definition. The class pages still describe each one.[^about.md]

The key `Date` and LinkML's own type `Date` write the same page, and the type's page wins.[^about.md]

[^about.md]: docs/about.md, What the generators do with these keys
