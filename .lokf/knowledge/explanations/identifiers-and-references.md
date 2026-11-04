---
type: Explanation
id: https://w3id.org/lmodel/capec/knowledge/explanations/identifiers-and-references
genre: explanation
title: Identifiers and references
description: "Why a CAPEC number is a string of digits and why references are typed: a number names and never counts, and the rdflib dumper cannot expand a bare identifier, so RDF comes through JSON-LD. `Exclude_ID` ranges over any entry, because the XSD says only that it names an ancestor."
about:
  - https://w3id.org/lmodel/capec/knowledge/datasets/capec-linkml-schema
sources:
  - id: about.md
    resource: docs/about.md
    title: Where the schema is narrower than the XSD
  - id: index.md
    resource: docs/index.md
    title: Getting RDF
generated:
  by: process:ktl-librarian
  at: "2026-11-04T02:37:57Z"
status: draft
---

# Identifiers and references

The XSD types a CAPEC number as `xs:integer`. The schema writes it as a string of digits that does not begin with zero, since a number names and never counts.[^about.md]

`linkml-convert -t rdf` stops with `Unknown CURIE prefix: @base`, because the rdflib dumper in linkml-runtime 1.12.1 cannot expand a bare identifier. The generated JSON-LD context can, and CAPEC-1 is then `capec:1`.[^index.md]

A reference to another entry ranges over the class it names, so OWL and JSON-LD treat it as a link. `Exclude_ID` ranges over any entry, because the XSD says only that it names an ancestor, though all 260 in CAPEC 3.9 name a category.[^about.md]

[^about.md]: docs/about.md, Where the schema is narrower than the XSD
[^index.md]: docs/index.md, Getting RDF
