---
type: Service
id: https://w3id.org/lmodel/capec/knowledge/workflows/upstream-watch
genre: reference
title: Upstream watch (upstream-watch.yaml)
description: "The weekly check that `scripts/check_upstream_release.py` runs: another CAPEC version, a changed XSD or catalogue, changed Terms of Use or a new news item fails the run and opens or updates an issue."
resource: .github/workflows/upstream-watch.yaml
about:
  - https://w3id.org/lmodel/capec/knowledge/references/capec-catalogue
  - https://w3id.org/lmodel/capec/knowledge/references/capec-xsd
  - https://w3id.org/lmodel/capec/knowledge/references/capec-terms-of-use
sources:
  - id: upstream-watch.yaml
    resource: .github/workflows/upstream-watch.yaml
  - id: check_upstream_release.py
    resource: scripts/check_upstream_release.py
    title: the docstring
  - id: test_watch.py
    resource: tests/test_watch.py
    title: the docstring
  - resource: .github/scripts/report-issue.sh
    title: how the issue is opened
generated:
  by: process:ktl-librarian
  at: "2026-11-04T02:37:57Z"
status: draft
---

# Upstream watch (upstream-watch.yaml)

The workflow runs every Monday, and a failing check opens an issue or comments on the one already open.[^upstream-watch.yaml]

The script reads pages and files from `capec.mitre.org`, compares files by git object hash, and reads at most 8 MB of an answer. It follows a redirect only over https to that host, sends no token, and quotes server text as code on one line.[^check_upstream_release.py]

`tests/test_watch.py` runs it against stubbed answers.[^test_watch.py]

[^upstream-watch.yaml]: .github/workflows/upstream-watch.yaml
[^check_upstream_release.py]: scripts/check_upstream_release.py, the docstring
[^test_watch.py]: tests/test_watch.py, the docstring
