---
type: Playbook
id: https://w3id.org/lmodel/capec/knowledge/playbooks/regenerate-and-test
genre: how-to
title: Regenerate and test
description: "How to change the schema: edit `src/capec/schema/`, run `just lint`, `just gen-project`, `just gen-doc`, `just lokf-adapt` and `just test`, and commit what they write. Generated files are never edited by hand."
references:
  - https://w3id.org/lmodel/capec/knowledge/datasets/capec-linkml-schema
  - https://w3id.org/lmodel/capec/knowledge/datasets/generated-artefacts
sources:
  - id: contributing.md
    resource: CONTRIBUTING.md
    title: Before opening a pull request
  - id: main.yaml
    resource: .github/workflows/main.yaml
    title: the lint step
  - id: justfile
    resource: justfile
    title: the test recipe
generated:
  by: process:ktl-librarian
  at: "2026-11-04T02:37:57Z"
status: draft
verified:
  - by: process:ktl-librarian
    at: "2026-11-04T02:44:15Z"
---

# Regenerate and test

1. Edit a file in `src/capec/schema/`.[^contributing.md]
2. Run `just lint`. A warning fails it.[^main.yaml]
3. Run `just gen-project` and `just gen-doc`, then `just lokf-adapt`.[^contributing.md]
4. Run `just test`, which generates into `tmp/`, runs `pytest` and runs the example runner.[^justfile]
5. Commit the output. `project/`, `src/capec/datamodel/`, `docs/schema/` and `.lokf/capec.yaml` are generated.[^contributing.md]

[^contributing.md]: CONTRIBUTING.md, Before opening a pull request
[^main.yaml]: .github/workflows/main.yaml, the lint step
[^justfile]: justfile, the test recipe
