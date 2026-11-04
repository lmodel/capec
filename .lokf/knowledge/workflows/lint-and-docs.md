---
type: Service
id: https://w3id.org/lmodel/capec/knowledge/workflows/lint-and-docs
genre: reference
title: Lint and docs (lint-and-docs.yaml)
description: "The static checks on pull requests, on `main` and every Monday: ShellCheck, actionlint, the word budgets of CONTRIBUTING.md and SECURITY.md, markdownlint, lychee and codespell."
resource: .github/workflows/lint-and-docs.yaml
references:
  - https://w3id.org/lmodel/capec/knowledge/policies/security-policy
sources:
  - id: lint-and-docs.yaml
    resource: .github/workflows/lint-and-docs.yaml
generated:
  by: process:ktl-librarian
  at: "2026-11-04T02:37:57Z"
status: draft
---

# Lint and docs (lint-and-docs.yaml)

The workflow never touches the schema or the Python tests. It runs ShellCheck and actionlint, holds `CONTRIBUTING.md` to 1000 words and `SECURITY.md` to 900, and runs markdownlint, lychee and codespell.[^lint-and-docs.yaml]

[^lint-and-docs.yaml]: .github/workflows/lint-and-docs.yaml
