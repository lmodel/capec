---
type: GlossaryTerm
id: https://w3id.org/lmodel/capec/knowledge/glossary/capec-view
title: View
description: "A CAPEC view: one way of looking over the catalogue, as a hierarchy (`Graph`) or a slice (`Implicit` by a filter, `Explicit` by hand). The class is `CapecView`, and CAPEC 3.9 holds 13."
definedBy:
  - https://w3id.org/lmodel/capec/knowledge/references/capec-xsd
relatedTo:
  - https://w3id.org/lmodel/capec/knowledge/glossary/capec-category
sources:
  - id: capec_entries.yaml
    resource: src/capec/schema/capec_entries.yaml
    title: CapecView and CapecViewType
  - id: test_catalogue.py
    resource: tests/test_catalogue.py
    title: test_a_view_is_a_filter_or_a_member_list
generated:
  by: process:ktl-librarian
  at: "2026-11-04T02:37:57Z"
status: draft
verified:
  - by: process:ktl-librarian
    at: "2026-11-04T02:47:00Z"
---

# View

One way of looking over the catalogue. A `Graph` view is a hierarchy, an `Implicit` view is a slice picked by a filter, and an `Explicit` view is a slice picked by hand.[^capec_entries.yaml]

In CAPEC 3.9 each implicit view has a filter, and each other view lists its members.[^test_catalogue.py]

[^capec_entries.yaml]: src/capec/schema/capec_entries.yaml, CapecView and CapecViewType
[^test_catalogue.py]: tests/test_catalogue.py, test_a_view_is_a_filter_or_a_member_list
