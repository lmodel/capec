---
type: Service
id: https://w3id.org/lmodel/capec/knowledge/workflows/semantic-release
genre: reference
title: Semantic release (semantic-release.yml)
description: The workflow that computes the next version from Conventional Commits on `main`, promotes the changelog, tags and publishes a GitHub Release, and dispatches the knowledge release once `KNOWLEDGE_RELEASE_ENABLED` is `true`.
resource: .github/workflows/semantic-release.yml
dependsOn:
  - https://w3id.org/lmodel/capec/knowledge/workflows/main
sources:
  - id: semantic-release.yml
    resource: .github/workflows/semantic-release.yml
    title: the header comment
generated:
  by: process:ktl-librarian
  at: "2026-11-04T02:37:57Z"
status: draft
---

# Semantic release (semantic-release.yml)

The `plan` job previews every pull request with `--dry-run`, and the `release` job runs only on a push to `main`, behind the `release` Environment.[^semantic-release.yml]

The `v0.0.0` baseline tag keeps a first release at 0.1.0, and `.releaserc.json` maps a breaking change to a minor bump.[^semantic-release.yml]

[^semantic-release.yml]: .github/workflows/semantic-release.yml, the header comment
