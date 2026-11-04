---
type: Dataset
id: https://w3id.org/lmodel/capec/knowledge/datasets/generated-artefacts
genre: reference
title: Generated artefacts
description: "What `just gen-project` and `just gen-doc` generate from the capec schema: the projections in `project/`, the Python models in `src/capec/datamodel/`, and the merged schema in `docs/schema/`. None is edited by hand."
resource: project
derivedFrom:
  - https://w3id.org/lmodel/capec/knowledge/datasets/capec-linkml-schema
sources:
  - id: justfile
    resource: justfile
    title: the gen-project and gen-doc recipes
  - id: test_generated_json_schema.py
    resource: tests/test_generated_json_schema.py
    title: the docstring
  - id: generators.yaml
    resource: .linkml/generators.yaml
  - id: test_datamodel.py
    resource: tests/test_datamodel.py
  - resource: project
  - resource: src/capec/datamodel
  - resource: docs/schema
generated:
  by: process:ktl-librarian
  at: "2026-11-04T02:37:57Z"
status: draft
---

# Generated artefacts

`just gen-project` writes the projections in `project/` and the Python models in `src/capec/datamodel/`. `just gen-doc` writes the merged schema to `docs/schema/capec.yaml` and the element pages to `docs/elements/`, which git ignores.[^justfile]

`project/jsonschema/capec.schema.json` is what a consumer without LinkML validates with. `tests/test_generated_json_schema.py` checks it against the generator's output.[^test_generated_json_schema.py]

The generators' settings are in `.linkml/generators.yaml`.[^generators.yaml]

Both Python models load the whole catalogue.[^test_datamodel.py]

[^justfile]: justfile, the gen-project and gen-doc recipes
[^test_generated_json_schema.py]: tests/test_generated_json_schema.py, the docstring
[^generators.yaml]: .linkml/generators.yaml
[^test_datamodel.py]: tests/test_datamodel.py
