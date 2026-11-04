---
type: Playbook
id: https://w3id.org/lmodel/capec/knowledge/playbooks/update-upstream-pins
genre: how-to
title: Move to another version
description: "How to answer the upstream watch when MITRE publishes another CAPEC version or XSD: read what changed, then move `upstream/`, the pins in `scripts/check_upstream_release.py` and the schema headers together, and let the coverage test say what else moved."
references:
  - https://w3id.org/lmodel/capec/knowledge/datasets/upstream-copy
  - https://w3id.org/lmodel/capec/knowledge/references/capec-catalogue
  - https://w3id.org/lmodel/capec/knowledge/references/capec-xsd
sources:
  - id: check_upstream_release.py
    resource: scripts/check_upstream_release.py
    title: the docstring and the pins
  - id: test_upstream.py
    resource: tests/test_upstream.py
  - id: test_coverage.py
    resource: tests/test_coverage.py
    title: the docstring
generated:
  by: process:ktl-librarian
  at: "2026-11-04T02:37:57Z"
status: draft
---

# Move to another version

1. Read what changed in the new version.[^check_upstream_release.py]
2. Replace the files in `upstream/`, and move `PINNED_EDITION`, `PINNED_DATE`, `PINNED_XSD_VERSION`, `PINNED_SOURCE` and `PINNED_BLOBS` together.[^check_upstream_release.py]
3. Move `version` and `source` in each module's header. `tests/test_upstream.py` checks them against the pins.[^test_upstream.py]
4. Run the tests. `tests/test_coverage.py` fails on each key, value or cardinality that moved, and `tests/test_catalogue.py` on each count.[^test_coverage.py]

[^check_upstream_release.py]: scripts/check_upstream_release.py, the docstring and the pins
[^test_upstream.py]: tests/test_upstream.py
[^test_coverage.py]: tests/test_coverage.py, the docstring
