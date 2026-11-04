---
type: Reference
id: https://w3id.org/lmodel/capec/knowledge/references/capec-catalogue
genre: reference
title: CAPEC catalogue
description: The Common Attack Pattern Enumeration and Classification, the catalogue of attack patterns that The MITRE Corporation publishes as XML. Version 3.9 of 24 January 2023 is the latest, with 615 attack patterns, 78 categories, 13 views and 440 external references.
resource: https://capec.mitre.org/data/xml/capec_v3.9.xml
sources:
  - id: check_upstream_release.py
    resource: scripts/check_upstream_release.py
    title: the pins
  - id: test_catalogue.py
    resource: tests/test_catalogue.py
    title: test_each_section_holds_what_the_list_page_counts
  - id: capec.yaml
    resource: src/capec/schema/capec.yaml
    title: the comments
generated:
  by: process:ktl-librarian
  at: "2026-11-04T02:37:57Z"
status: draft
verified:
  - by: process:ktl-librarian
    at: "2026-11-04T02:47:00Z"
---

# CAPEC catalogue

The schema renders catalogue version 3.9, dated 2023-01-24. The watch pins that version and file.[^check_upstream_release.py]

The catalogue holds 615 attack patterns, 78 categories, 13 views and 440 external references.[^test_catalogue.py]

MITRE's latest catalogue is dated January 2023 and its latest news item March 2023. No page says CAPEC has stopped, so the watch keeps asking.[^capec.yaml]

[^check_upstream_release.py]: scripts/check_upstream_release.py, the pins
[^test_catalogue.py]: tests/test_catalogue.py, test_each_section_holds_what_the_list_page_counts
[^capec.yaml]: src/capec/schema/capec.yaml, the comments
