---
type: Service
id: https://w3id.org/lmodel/capec/knowledge/workflows/knowledge-sync
genre: reference
title: Knowledge sync (knowledge-sync.yaml)
description: The weekly workflow that keeps the sidecar's copies and the skills pin at the newest release of Knowledge Trust Ladder, by one pull request that a person merges.
resource: .github/workflows/knowledge-sync.yaml
references:
  - https://w3id.org/lmodel/capec/knowledge/workflows/knowledge-librarian
sources:
  - id: knowledge-sync.yaml
    resource: .github/workflows/knowledge-sync.yaml
    title: the header comment
generated:
  by: process:ktl-librarian
  at: "2026-11-04T02:37:57Z"
status: draft
---

# Knowledge sync (knowledge-sync.yaml)

Each week the workflow compares the skills pin with the newest release of Knowledge Trust Ladder. When the pin is behind, it runs `.lokf/scripts/knowledge-sync.sh` and opens one pull request. It runs no agent and no code from the release, never pushes to the default branch and never merges.[^knowledge-sync.yaml]

[^knowledge-sync.yaml]: .github/workflows/knowledge-sync.yaml, the header comment
