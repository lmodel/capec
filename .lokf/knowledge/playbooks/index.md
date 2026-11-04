# Playbooks

* [Validate a catalogue](validate-a-catalogue.md) - How to validate a CAPEC catalogue: turn the XML into data with `scripts/capec_to_json.py`, run `linkml-validate` with the class `CapecAttackPatternCatalog`, and run `tests/capec_rules.py` for what a JSON Schema cannot state.
* [Regenerate and test](regenerate-and-test.md) - How to change the schema: edit `src/capec/schema/`, run `just lint`, `just gen-project`, `just gen-doc`, `just lokf-adapt` and `just test`, and commit what they write. Generated files are never edited by hand.
* [Release](release.md) - How a release happens: `semantic-release.yml` reads Conventional Commits on `main`, promotes the `## [Unreleased]` section, tags and publishes. The first release needs the `v0.0.0` baseline tag on `main`, and PyPI publishing stays off.
* [Move to another version](update-upstream-pins.md) - How to answer the upstream watch when MITRE publishes another CAPEC version or XSD: read what changed, then move `upstream/`, the pins in `scripts/check_upstream_release.py` and the schema headers together, and let the coverage test say what else moved.
* [Knowledge sources map](knowledge-sources.md) - The librarian's scrape map: every repository location and external source this bundle derives concepts from, how to re-check each, and the tracked paths left out with their reasons.
