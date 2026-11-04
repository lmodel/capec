## Add your own just recipes here. This is imported by the main justfile.

# Overriding recipes from the root justfile by adding a recipe with the same
# name in this file is not possible until a known issue in just is fixed,
# https://github.com/casey/just/issues/2540

# ============ The CAPEC catalogue ============

# Turn the catalogue's XML into tmp/capec_v3.9.json, the data the schema describes
[group('model development')]
catalogue-json:
  mkdir -p tmp
  uv run scripts/capec_to_json.py --output tmp/capec_v3.9.json

# Validate the whole catalogue with linkml-validate, as a consumer would
[group('model development')]
validate-catalogue: catalogue-json
  uv run linkml-validate -s {{source_schema_path}} -C CapecAttackPatternCatalog tmp/capec_v3.9.json

# ============ Knowledge bundle: the adapted domain schema ============

# `.lokf/capec.yaml` is the copy `lokf adapt` writes from the schema so that it can
# sit beside `.lokf/lokf.yaml` (`lokf adapt --help` lists the moves). The roots are
# the two classes that carry an identifier, so a concept can be an attack pattern, a
# category or a view, under CapecEntry, or an external reference. A concept then has
# LOKF's `id` in place of the source's identifier, its Name or Title as its `title`,
# and its Description, Summary or Objective as its `description`.
#
# The recipes run the `lokf` the sidecar's floor pins (0.9.0 or later). LOKF_CMD runs
# another, such as a checkout: LOKF_CMD="uv run --project ../lokf lokf" just lokf-adapt
lokf_cmd := env_var_or_default("LOKF_CMD", "uv run --project .lokf lokf")
lokf_adapt_roots := "--root CapecEntry --root CapecExternalReference --prefix capec --fold CapecEntry.Name=title --fold CapecExternalReference.Title=title --fold CapecAttackPattern.Description=description --fold CapecCategory.Summary=description --fold CapecView.Objective=description"

# Rewrite .lokf/capec.yaml from the schema (run after every schema change)
[group('knowledge bundle')]
lokf-adapt:
  {{lokf_cmd}} adapt {{source_schema_path}} {{lokf_adapt_roots}} --lokf .lokf/lokf.yaml -o .lokf/capec.yaml

# Fail when .lokf/capec.yaml is stale against the schema or .lokf/lokf.yaml
[group('knowledge bundle')]
lokf-adapt-check:
  {{lokf_cmd}} adapt {{source_schema_path}} {{lokf_adapt_roots}} --lokf .lokf/lokf.yaml -o .lokf/capec.yaml --check
