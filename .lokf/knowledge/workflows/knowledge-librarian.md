---
type: Service
id: https://w3id.org/lmodel/capec/knowledge/workflows/knowledge-librarian
genre: reference
title: Knowledge librarian (knowledge-librarian.yaml)
description: The sidecar's scheduled agent run that keeps the bundle in step with the repository and opens a pull request for a person to review. It is inert until `KNOWLEDGE_LIBRARIAN_ENABLED` is `true`.
resource: .github/workflows/knowledge-librarian.yaml
references:
  - https://w3id.org/lmodel/capec/knowledge/playbooks/knowledge-sources
sources:
  - id: knowledge-librarian.yaml
    resource: .github/workflows/knowledge-librarian.yaml
    title: the header comment
generated:
  by: process:ktl-librarian
  at: "2026-11-04T02:37:57Z"
status: draft
---

# Knowledge librarian (knowledge-librarian.yaml)

The workflow runs on Mondays or by hand. It never pushes to the default branch and never merges. It does nothing until `KNOWLEDGE_LIBRARIAN_ENABLED` is `true`.[^knowledge-librarian.yaml]

Its `refresh` job runs the agent with a read-only token and no git credentials. Only its `publish` job can push a branch and open the pull request, and that job runs no agent code.[^knowledge-librarian.yaml]

[^knowledge-librarian.yaml]: .github/workflows/knowledge-librarian.yaml, the header comment
