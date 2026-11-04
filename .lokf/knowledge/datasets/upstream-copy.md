---
type: Dataset
id: https://w3id.org/lmodel/capec/knowledge/datasets/upstream-copy
genre: reference
title: Copy of the upstream
description: "`upstream/`: MITRE's CAPEC XSD 3.5 and catalogue 3.9, each byte for byte what MITRE serves and pinned by git object hash, with the Terms of Use beside them."
resource: upstream
references:
  - https://w3id.org/lmodel/capec/knowledge/references/capec-xsd
  - https://w3id.org/lmodel/capec/knowledge/references/capec-catalogue
  - https://w3id.org/lmodel/capec/knowledge/references/capec-terms-of-use
sources:
  - id: upstream-readme
    resource: upstream/README.md
  - id: test_upstream.py
    resource: tests/test_upstream.py
    title: the docstring
generated:
  by: process:ktl-librarian
  at: "2026-11-04T02:37:57Z"
status: draft
---

# Copy of the upstream

`upstream/` holds `ap_schema_v3.5.xsd` and `capec_v3.9.xml`, and `TERMS.txt` holds the Terms of Use they come under.[^upstream-readme]

`scripts/check_upstream_release.py` pins each copy by its git object hash, and `tests/test_upstream.py` holds the folder to those pins.[^test_upstream.py]

[^upstream-readme]: upstream/README.md
[^test_upstream.py]: tests/test_upstream.py, the docstring
