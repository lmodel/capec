---
type: CapecExternalReference
id: https://w3id.org/lmodel/capec/knowledge/datasets/example-external-reference
genre: reference
title: "Exploiting Software: How to Break Code"
description: REF-1 from the catalogue, written as a concept of type `CapecExternalReference` in the adapt copy's keys. It shows that the domain schema admits an external reference as a concept.
resource: upstream/capec_v3.9.xml
derivedFrom:
  - https://w3id.org/lmodel/capec/knowledge/datasets/upstream-copy
Author:
  - G. Hoglund
  - G. McGraw
Publication_Year: "2004"
Publication_Month: --02
Publisher: Addison-Wesley
sources:
  - id: readme.md
    resource: README.md
    title: the Knowledge Trust Ladder (KTL) section
  - id: capec_v3.9.xml
    resource: upstream/capec_v3.9.xml
    title: External_Reference REF-1
generated:
  by: process:ktl-librarian
  at: "2026-11-06T21:16:57Z"
status: draft
---

# Exploiting Software: How to Break Code

This concept shows how a host writes an external reference in its bundle. Its type is `CapecExternalReference`, and `lokf validate` checks it against `.lokf/schema/capec.yaml`.[^readme.md]

Its title, authors, date and publisher are the values of REF-1 in the catalogue. LOKF's `id` stands in for the identifier, and the work's title is the `title`.[^capec_v3.9.xml]

[^readme.md]: README.md, the Knowledge Trust Ladder (KTL) section
[^capec_v3.9.xml]: upstream/capec_v3.9.xml, External_Reference REF-1
