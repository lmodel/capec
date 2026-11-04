---
type: Reference
id: https://w3id.org/lmodel/capec/knowledge/references/capec-terms-of-use
genre: reference
title: CAPEC Terms of Use
description: "MITRE's terms for CAPEC: a non-exclusive, royalty-free licence for research, development and commercial use, under which a copy must reproduce MITRE's copyright designation and the licence. NOTICE and `upstream/TERMS.txt` do so."
resource: https://capec.mitre.org/about/termsofuse.html
sources:
  - id: terms.txt
    resource: upstream/TERMS.txt
  - id: notice
    resource: NOTICE
    title: CAPEC
  - id: check_upstream_release.py
    resource: scripts/check_upstream_release.py
    title: _terms_text
generated:
  by: process:ktl-librarian
  at: "2026-11-04T02:37:57Z"
status: draft
---

# CAPEC Terms of Use

The terms grant a licence to use CAPEC for research, development and commercial purposes. A copy is authorised provided it reproduces MITRE's copyright designation and the licence.[^terms.txt]

`NOTICE` and `upstream/TERMS.txt` reproduce them, and the designation is the one in the website's footer.[^notice]

The watch compares the licence and the disclaimer on the page with a pinned hash, leaving out the footer, whose year moves.[^check_upstream_release.py]

[^terms.txt]: upstream/TERMS.txt
[^notice]: NOTICE, CAPEC
[^check_upstream_release.py]: scripts/check_upstream_release.py, _terms_text
