---
type: Explanation
id: https://w3id.org/lmodel/capec/knowledge/explanations/rules-in-python
genre: explanation
title: Rules in Python
description: "Why `tests/capec_rules.py` exists: a JSON Schema looks at one value at a time, so it cannot say that a reference names an entry the catalogue holds, or that no number is used twice. What the data merely shows goes in `tests/test_catalogue.py` with its counts."
about:
  - https://w3id.org/lmodel/capec/knowledge/datasets/capec-linkml-schema
sources:
  - id: capec_rules.py
    resource: tests/capec_rules.py
    title: the docstring
  - id: test_catalogue.py
    resource: tests/test_catalogue.py
    title: the docstring
generated:
  by: process:ktl-librarian
  at: "2026-11-04T02:37:57Z"
status: draft
verified:
  - by: process:ktl-librarian
    at: "2026-11-04T02:47:00Z"
---

# Rules in Python

A JSON Schema looks at one value at a time. So `tests/capec_rules.py` checks that each reference names something the catalogue holds, and that no number or reference identifier is used twice.[^capec_rules.py]

What the data merely shows, such as a deprecated entry's name beginning with `DEPRECATED`, goes in `tests/test_catalogue.py` with its counts, and not in the schema.[^test_catalogue.py]

[^capec_rules.py]: tests/capec_rules.py, the docstring
[^test_catalogue.py]: tests/test_catalogue.py, the docstring
