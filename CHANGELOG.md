# Changelog

All notable changes to this project are documented here. The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/), and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

The `v0.0.0` tag is a baseline, not a release: it marks where versioning starts so the first real release is `0.1.0` rather than `1.0.0`. The schema stays below 1.0.0 until its shape settles, so a breaking change bumps the minor version. See [CONTRIBUTING.md](CONTRIBUTING.md#releasing-maintainers).

## [Unreleased]

### Changed

- **The bundle's schema files sit in `.lokf/schema/`**: `lokf.yaml` and the `lokf adapt` copy `capec.yaml`, as KTL v0.62.0 lays them out.

## [0.1.0] - 2026-11-04

### Added

- **A LinkML rendering of CAPEC 3.9 and its XSD 3.5**, in three modules, `capec_core`, `capec_entries` and the umbrella `capec`. Keys and values are the XSD's own, and every description is this project's.
- **`scripts/capec_to_json.py`, which turns the catalogue's XML into the data the schema describes**, by rules it reads from the XSD, and stops on a key the XSD does not declare. A test turns the output back into XML and finds it equal to the catalogue.
- **A test that walks the XSD beside the classes and enums**, and fails on anything missing, added or of another cardinality or kind.
- **The whole catalogue in the normal gate**, against the committed JSON Schema and the rules in `tests/capec_rules.py`, with the catalogue's one known fault pinned.
- **A weekly upstream watch** that reports another version, a changed file, changed Terms of Use or a new news item.
- **Mappings to STIX, ATT&CK, the SEPSES CAPEC ontology, SKOS, Dublin Core, schema.org and Wikidata**, each held by a test to a pinned term list or a released copy.
- **`.lokf/capec.yaml`, the schema's `lokf adapt` copy, rooted on `CapecEntry` and `CapecExternalReference`.** The knowledge release attaches it as `schema-<tag>-capec.yaml`.
- **The repository's Knowledge Trust Ladder (KTL) knowledge bundle and its sidecar automation**, from the KTL v0.61.0 templates with the lokf floor at 0.9.0, and a knowledge website that replaces the mkdocs site.

### Changed

- **The template moves to linkml-project-copier v0.5.0**, linkml and linkml-runtime are locked at 1.12.1, and the Python project is named `capec-linkml`. PyPI publishing stays off.
- **Keys take the XSD's own names**, such as `Related_Attack_Patterns`, in place of the old snake_case slots, and classes and enums take the `Capec` prefix.
- **An entry's references to other entries and to external references are typed**, and identifiers are strings of digits.

### Removed

- **The old copies under `src/capec/mappings/`, `src/capec/schema/` and `tests/data/capec/`.** Each was a slice or a copy of what `upstream/` holds.
