---
type: Service
id: https://w3id.org/lmodel/capec/knowledge/workflows/knowledge-release
genre: reference
title: Knowledge release (knowledge-release.yaml)
description: The workflow that attaches the bundle, a Copilot skill and the schema's adapt copy to a GitHub release, each with a checksum. It starts by hand or, once `KNOWLEDGE_RELEASE_ENABLED` is `true`, on each published release.
resource: .github/workflows/knowledge-release.yaml
references:
  - https://w3id.org/lmodel/capec/knowledge/datasets/adapt-copy
sources:
  - id: knowledge-release.yaml
    resource: .github/workflows/knowledge-release.yaml
    title: the header comment
generated:
  by: process:ktl-librarian
  at: "2026-11-04T02:37:57Z"
status: draft
---

# Knowledge release (knowledge-release.yaml)

The workflow attaches the bundle as a zip file, and the domain schema that `.lokf/justfile` names as `schema-<tag>-<name>.yaml`, each with its `.sha256`. It runs no agent, and never commits or pushes.[^knowledge-release.yaml]

[^knowledge-release.yaml]: .github/workflows/knowledge-release.yaml, the header comment
