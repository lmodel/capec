# Changelog

All notable changes to this project are documented here. The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/), and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

The `v0.0.0` tag is a baseline, not a release: it marks where versioning starts so the first real release is `0.1.0` rather than `1.0.0`. The schema stays below 1.0.0 until its shape settles, so a breaking change bumps the minor version. See [CONTRIBUTING.md](CONTRIBUTING.md#releasing-maintainers).

## [Unreleased]

### Security

- **The sidecar copies and the skills pin are at Knowledge Trust Ladder [v0.70.4](https://github.com/noelmcloughlin/knowledge-trust-ladder/compare/v0.66.0...v0.70.4).** The release changed `.github/workflows/knowledge-registrar.yaml`, `.github/workflows/knowledge-librarian.yaml`, `.github/workflows/knowledge-release.yaml`, `.github/workflows/knowledge-sync.yaml`, `.github/PULL_REQUEST_TEMPLATE/knowledge-sync.md`, `.lokf/scripts/knowledge-conventions.sh`, `.lokf/scripts/knowledge-conventions.py`, `.lokf/scripts/knowledge-preflight.sh`, `.lokf/scripts/knowledge-provenance.sh`, `.lokf/scripts/knowledge-feedback.sh`, `.lokf/scripts/knowledge-apply.py`, `.lokf/scripts/knowledge-report.sh`, `.lokf/scripts/knowledge-sync.sh`, `.lokf/m365/ktl-docent-m365.md`, `.lokf/justfile`, `website/assets/css/site.css`, `website/assets/js/graph.js`, `website/assets/js/site.js`, `website/content/_content.gotmpl`, `website/content/knowledge/_content.gotmpl`, `website/.gitignore`, `website/hugo.toml`, `website/layouts/_markup/render-blockquote.html`, `website/layouts/_markup/render-codeblock-mermaid.html`, `website/layouts/_markup/render-heading.html`, `website/layouts/_markup/render-link.html`, `website/layouts/_partials/gendoc.html`, `website/layouts/_partials/heroes.html`, `website/layouts/_partials/icon.html`, `website/layouts/_partials/markdown-file.html`, `website/layouts/_partials/nav-key.html`, `website/layouts/_partials/route.html`, `website/layouts/_partials/schema-file.html`, `website/layouts/_partials/sidebar.html`, `website/layouts/_partials/tools.html`, `website/layouts/_partials/vendor.html`, `website/layouts/baseof.html`, `website/layouts/health.html`, `website/layouts/home.badge.json`, `website/layouts/home.llms.txt`, `website/layouts/page.atom.xml`, `website/layouts/page.html`, `website/layouts/schema/section.html`, `website/pyproject.toml`, `website/scripts/build.sh`, `website/scripts/clean-html.py`, `website/scripts/prepare.sh`, `website/uv.lock`, `.github/workflows/knowledge-website.yaml`, `website/layouts/_partials/own.html`, `website/layouts/_partials/spec.html`, `website/scripts/check-svg.py`, `website/scripts/lokf-export.py`, `website/scripts/site-values.py`, `website/scripts/uv-env.sh` and `website/scripts/vendor.sh` here.

## [0.2.3] - 2026-11-16

### Fixed

- **Each GitHub release carries its changelog section as its body**: semantic-release asks for the notes again after the changelog commit, and `changelog-release.mjs notes` now answers with the promoted section instead of the empty Unreleased one.

## [0.2.2] - 2026-11-15

### Changed

- **The release tools are in `.release/`**, outside `.github/`, where Dependabot's pull requests for them were refused.

## [0.2.1] - 2026-11-15

### Added

- **`scorecard.yml` publishes this repository's OpenSSF Scorecard.**
- **The README shows the CI, licence, OpenSSF Scorecard and KTL scorecard badges.**
- **`codeql.yml` scans the Python, the JavaScript and the workflows with CodeQL.**

### Changed

- **The knowledge website is built with Hugo from the ktl-website templates**, set by `website/site.toml`, in place of the Astro site.
- **The project requires Python 3.11 or later**, since Python 3.10's support ended in October 2026.

### Security

- **The sidecar copies are at Knowledge Trust Ladder [v0.66.0](https://github.com/noelmcloughlin/knowledge-trust-ladder/blob/v0.66.0/CHANGELOG.md), and `.lokf/pyproject.toml` pins `ktl==0.66.0`**, which the librarian installs its skill from.

## [0.2.0] - 2026-11-07

### Added

- **The schema as RDF Turtle and the merged schema**, in `project/rdf/` and `project/linkml/`, from `just gen-rdf` and `just gen-merged-schema`.

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
