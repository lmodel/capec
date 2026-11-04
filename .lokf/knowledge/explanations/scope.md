---
type: Explanation
id: https://w3id.org/lmodel/capec/knowledge/explanations/scope
genre: explanation
title: What the schema leaves out
description: "What the schema does not do: it says nothing about whether an entry is true, nothing evaluates a view's filter, and it holds the keys the XSD defines even where CAPEC 3.9 uses none, such as `Audience` and `Member_Of`."
about:
  - https://w3id.org/lmodel/capec/knowledge/datasets/capec-linkml-schema
sources:
  - id: about.md
    resource: docs/about.md
    title: What is left out
generated:
  by: process:ktl-librarian
  at: "2026-11-04T02:37:57Z"
status: draft
verified:
  - by: process:ktl-librarian
    at: "2026-11-04T02:44:15Z"
---

# What the schema leaves out

The schema says nothing about whether what an entry claims is true.[^about.md]

Filters in the views are data here and nothing evaluates them. Eight of the nine are XPath 1.0, and view 553's is XPath 2.0.[^about.md]

The schema holds what the XSD defines even where CAPEC 3.9 uses none of it, such as a view's `Audience`, `Member_Of` and a history's `Contribution`.[^about.md]

[^about.md]: docs/about.md, What is left out
