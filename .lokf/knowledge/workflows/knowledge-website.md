---
type: Service
id: https://w3id.org/lmodel/capec/knowledge/workflows/knowledge-website
genre: reference
title: Knowledge website (knowledge-website.yaml)
description: The workflow that builds `website/` on each pull request that touches its inputs, and deploys the default branch's build to GitHub Pages once `KNOWLEDGE_WEBSITE_ENABLED` is `true`.
resource: .github/workflows/knowledge-website.yaml
references:
  - https://w3id.org/lmodel/capec/knowledge/services/documentation-site
sources:
  - id: knowledge-website.yaml
    resource: .github/workflows/knowledge-website.yaml
    title: the header comment
generated:
  by: process:ktl-librarian
  at: "2026-11-04T02:37:57Z"
status: draft
---

# Knowledge website (knowledge-website.yaml)

The `build` job runs third-party packages under a read-only token. The `deploy` job holds the Pages scopes, runs for the default branch only, and waits for `KNOWLEDGE_WEBSITE_ENABLED`.[^knowledge-website.yaml]

[^knowledge-website.yaml]: .github/workflows/knowledge-website.yaml, the header comment
