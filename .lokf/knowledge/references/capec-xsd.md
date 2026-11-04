---
type: Reference
id: https://w3id.org/lmodel/capec/knowledge/references/capec-xsd
genre: reference
title: CAPEC XSD
description: The XML Schema of the CAPEC catalogue, version 3.5, namespace `http://capec.mitre.org/capec-3`. Its own header says 3.5.0, dated 21 October 2021. The schema's keys and listed values are this file's.
resource: https://capec.mitre.org/data/xsd/ap_schema_v3.5.xsd
sources:
  - id: test_upstream.py
    resource: tests/test_upstream.py
    title: test_the_xsd_is_this_version and test_the_catalogue_is_this_version_and_names_this_xsd
  - id: check_upstream_release.py
    resource: scripts/check_upstream_release.py
    title: check_schema
generated:
  by: process:ktl-librarian
  at: "2026-11-04T02:37:57Z"
status: draft
---

# CAPEC XSD

The XSD's namespace is `http://capec.mitre.org/capec-3`, and its header gives the version 3.5.0 and the date 21 October 2021. The catalogue names it as `ap_schema_v3.5.xsd`.[^test_upstream.py]

The watch reports when the versioned address or the latest address, `ap_schema_latest.xsd`, stops serving the pinned file.[^check_upstream_release.py]

[^test_upstream.py]: tests/test_upstream.py, test_the_xsd_is_this_version and test_the_catalogue_is_this_version_and_names_this_xsd
[^check_upstream_release.py]: scripts/check_upstream_release.py, check_schema
