<a href="https://github.com/linkml/linkml-project-copier"><img src="https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/copier-org/copier/master/img/badge/badge-grayscale-inverted-border-teal.json" alt="Copier Badge" style="max-width:100%;"/></a>

# capec

Common Attack Pattern Enumeration and Classification (CAPEC) 3.9 (LinkML)

> **Only want to ask?** Install `ktl-docent` into any agent you use, by a route from [the install page](https://w3id.org/ktl/docs/install/), and ask it about this project. It answers from the bundle and says how far each answer has been checked.
>
> **Agents:** if `.lokf/knowledge/index.md` exists, read it first. `llms.txt` says how to weigh it.

## Documentation Website

[https://lmodel.github.io/capec](https://lmodel.github.io/capec)

## What it models

The schema renders [CAPEC](https://capec.mitre.org/), the catalogue of attack patterns that The MITRE Corporation publishes, at version 3.9 of 24 January 2023 under its XML Schema (XSD) version 3.5. It keeps the XSD's keys and listed values, so the whole catalogue validates as MITRE spells it once `scripts/capec_to_json.py` has turned the XML into data. That is MITRE's latest catalogue, and its latest news item is from March 2023. No page says CAPEC has stopped, so a weekly workflow goes on asking.

`upstream/` holds the XSD and the catalogue, pinned by hash, and `tests/test_coverage.py` holds the schema to the XSD in both directions. [docs/index.md](docs/index.md) says how to validate a catalogue, and what the model leaves out.

## Mappings

The schema is the one home for mappings, and `tests/test_mappings.py` holds each to a pinned term list or a released copy.

* **[lmodel/stix](https://github.com/lmodel/stix)**: `close_mappings` for an attack pattern, an external reference and alternate terms, and `related_mappings` from mitigations to a course of action.
* **[lmodel/attack](https://github.com/lmodel/attack)**: `related_mappings` from an attack pattern to a technique.
* **[SEPSES](https://www.sepses.org/vocab/ref/capec/) CAPEC ontology**: `close_mappings` for attack patterns and the records and fields they hold.
* **[SKOS](https://www.w3.org/TR/skos-reference/)**: `close_mappings` for a pattern, a category, the catalogue, a taxonomy mapping and its fit, and for the parent and child natures.
* **[Dublin Core](https://www.dublincore.org/specifications/dublin-core/dcmi-terms/) and [schema.org](https://schema.org/)**: `close_mappings` for names, dates, descriptions and reference fields, and `broad_mappings` for the identifiers.
* **[Wikidata](https://www.wikidata.org/wiki/Q2986817)**: `close_mappings` on the catalogue to Q2986817, and `exact_mappings` on a weakness's number to the property P3624.

## Repository Structure

* [docs/](docs/): the website's own pages
* [project/](project/): generated project files (do not edit them)
* [scripts/](scripts/): the XML converter, the upstream watch and the mapping term extractor
* [src/capec/schema/](src/capec/schema): the LinkML schema, `capec.yaml`, `capec_entries.yaml` and `capec_core.yaml` (edit these)
* [src/capec/datamodel/](src/capec/datamodel): the generated Python datamodel
* [tests/](tests/): Python tests, with example data in [data/](tests/data), the term list in [upstream/](tests/upstream) and the neighbours' adapt copies in [neighbours/](tests/neighbours)
* [upstream/](upstream/): MITRE's XSD and catalogue at the pinned version, unchanged
* [website/](website/): the Astro Starlight site built from the README, `docs/`, the schema's pages and the knowledge bundle

## Developer Tools

Run `just` to list the project's [just](https://github.com/casey/just/) recipes.

## Knowledge Trust Ladder (KTL)

`.lokf/` holds this project's [KTL](https://w3id.org/ktl/) knowledge bundle. Its domain schema, `.lokf/capec.yaml`, is the copy `just lokf-adapt` writes from `src/capec/schema/capec.yaml`, and `just lokf-adapt-check` says when it is stale. Edit the source, never the copy. A release carries the copy as `schema-<tag>-capec.yaml`, on the terms [CONTRIBUTING.md](CONTRIBUTING.md#releasing-maintainers) gives.

The copy roots `CapecEntry` and `CapecExternalReference` on `Concept`. In Obsidian, add the types a concept may name to the *Known LOKF types* setting of the KTL Registrar and KTL Curator plugins:

```text
CapecAttackPattern, CapecCategory, CapecView, CapecExternalReference
```

LOKF's `id` takes the place of `ID` and `Reference_ID`. `Name` and `Title` fold into LOKF's `title`, and `Description`, `Summary` and `Objective` fold into its `description`. The smaller records stay values inside an entry. No key is another released copy's, since the XSD's keys open with a capital; `tests/test_schema_rules.py` fails on a new overlap. lmodel/cwe uses the same style of key, so a host importing both copies shares `Name`, `Status` and others under two IRIs.

## License

The schema and the code are under the Apache License 2.0 ([LICENSE](LICENSE)), and the knowledge bundle in [.lokf/knowledge/](.lokf/knowledge) is under [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/).

MITRE's XSD and catalogue come under the CAPEC Terms of Use, which allow a copy that reproduces MITRE's designation and licence: see [NOTICE](NOTICE). This is not a project of MITRE, and its use implies no endorsement by MITRE. CAPEC is a trademark of The MITRE Corporation.

## Contributing and security

[CONTRIBUTING.md](CONTRIBUTING.md) is the checklist for pull requests and
releases, [AI_COVENANT.md](AI_COVENANT.md) sets the rules for AI-assisted work,
[SECURITY.md](SECURITY.md) says how to report a vulnerability, and
[CHANGELOG.md](CHANGELOG.md) records the changes.

## Credits

Built from the [linkml-project-copier](https://github.com/linkml/linkml-project-copier) template ([doi:10.5281/zenodo.15163584](https://doi.org/10.5281/zenodo.15163584)).
