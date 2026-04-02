## Add your own just recipes here. This is imported by the main justfile.

# Overriding recipes from the root justfile by adding a recipe with the same
# name in this file is not possible until a known issue in just is fixed,
# https://github.com/casey/just/issues/2540

# Run all CAPEC-specific tests
[group('tests')]
test-capec:
    uv run python -m pytest tests/ -v

# Run XML structure and enum validation tests only
[group('tests')]
test-xml:
    uv run python -m pytest tests/test_capec_xml.py -v

# Run YAML fixture load tests only (valid + invalid)
[group('tests')]
test-fixtures:
    uv run python -m pytest tests/test_data.py -v

# Run linkml-run-examples on valid/invalid directories
[group('tests')]
test-examples:
    uv run linkml-run-examples \
      --input-formats yaml \
      --output-formats yaml \
      --counter-example-input-directory tests/data/invalid \
      --input-directory tests/data/valid \
      --output-directory examples/output \
      --schema src/capec/schema/capec.yaml

# Run view-filtered catalog XML tests (navigation/, views/, and mappings/)
[group('tests')]
test-view-catalogs:
    uv run python -m pytest tests/test_view_catalogs.py -v
