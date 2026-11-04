---
type: GlossaryTerm
id: https://w3id.org/lmodel/capec/knowledge/glossary/structured-text
title: Structured text
description: Text in the catalogue that may hold XHTML markup, such as paragraphs and lists. The XSD's type is `StructuredTextType`, and the schema's is `capec_structured_text`, a string that keeps the markup without its namespace prefix.
definedBy:
  - https://w3id.org/lmodel/capec/knowledge/references/capec-xsd
relatedTo:
  - https://w3id.org/lmodel/capec/knowledge/explanations/xml-to-data
sources:
  - id: capec_core.yaml
    resource: src/capec/schema/capec_core.yaml
    title: capec_structured_text
  - id: security.md
    resource: SECURITY.md
    title: What this repository releases
generated:
  by: process:ktl-librarian
  at: "2026-11-04T02:37:57Z"
status: draft
---

# Structured text

Text that may hold XHTML markup such as paragraphs and lists, with no namespace prefix.[^capec_core.yaml]

A page that shows such text must escape it.[^security.md]

[^capec_core.yaml]: src/capec/schema/capec_core.yaml, capec_structured_text
[^security.md]: SECURITY.md, What this repository releases
