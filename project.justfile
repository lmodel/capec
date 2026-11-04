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
