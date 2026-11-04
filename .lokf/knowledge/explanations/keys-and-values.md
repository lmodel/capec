---
type: Explanation
id: https://w3id.org/lmodel/capec/knowledge/explanations/keys-and-values
genre: explanation
title: Keys and values
description: "Why the schema's keys and values are spelled as they are: each key is the XSD's own element or attribute name, such as `Related_Attack_Patterns`, each value the XSD's own text, and classes and enums carry a `Capec` prefix."
about:
  - https://w3id.org/lmodel/capec/knowledge/datasets/capec-linkml-schema
sources:
  - id: about.md
    resource: docs/about.md
    title: Keys and values
  - id: test_schema_rules.py
    resource: tests/test_schema_rules.py
    title: test_the_source_holds_every_key_as_an_attribute
  - id: linkmllint
    resource: .linkmllint.yaml
generated:
  by: process:ktl-librarian
  at: "2026-11-04T02:37:57Z"
status: draft
verified:
  - by: process:ktl-librarian
    at: "2026-11-04T02:44:15Z"
---

# Keys and values

The keys and values are the XSD's own, such as `Related_Attack_Patterns`, `CAPEC_ID` and `Access Control`, and the classes and enums carry a `Capec` prefix.[^about.md]

Each key is an attribute of its class and no key is a top-level slot, so a short key such as `Name` takes no slot that a neighbour's merged import could overwrite.[^test_schema_rules.py]

`.linkmllint.yaml` fits the naming rule to these keys and values, and says why.[^linkmllint]

[^about.md]: docs/about.md, Keys and values
[^test_schema_rules.py]: tests/test_schema_rules.py, test_the_source_holds_every_key_as_an_attribute
[^linkmllint]: .linkmllint.yaml
