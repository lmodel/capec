---
type: GlossaryTerm
id: https://w3id.org/lmodel/capec/knowledge/glossary/capec-category
title: Category
description: "A CAPEC category: a group of attack patterns that share an effect or intent, and not itself a pattern of attack. The class is `CapecCategory`, and CAPEC 3.9 holds 78."
definedBy:
  - https://w3id.org/lmodel/capec/knowledge/references/capec-xsd
relatedTo:
  - https://w3id.org/lmodel/capec/knowledge/glossary/capec-view
sources:
  - id: capec_entries.yaml
    resource: src/capec/schema/capec_entries.yaml
    title: CapecCategory
  - id: test_catalogue.py
    resource: tests/test_catalogue.py
    title: test_each_section_holds_what_the_list_page_counts
generated:
  by: process:ktl-librarian
  at: "2026-11-04T02:37:57Z"
status: draft
verified:
  - by: process:ktl-librarian
    at: "2026-11-04T02:47:00Z"
---

# Category

A group of attack patterns that share an effect or intent, and not itself a pattern of attack.[^capec_entries.yaml]

CAPEC 3.9 holds 78 categories.[^test_catalogue.py]

[^capec_entries.yaml]: src/capec/schema/capec_entries.yaml, CapecCategory
[^test_catalogue.py]: tests/test_catalogue.py, test_each_section_holds_what_the_list_page_counts
