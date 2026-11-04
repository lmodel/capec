---
lokf_version: "0.2"
okf_version: "0.2"
base_iri: https://w3id.org/lmodel/capec/knowledge/
context: https://w3id.org/lokf/context.jsonld
title: capec Knowledge Bundle
description: Common Attack Pattern Enumeration and Classification (CAPEC) 3.9 (LinkML)
license: https://creativecommons.org/licenses/by/4.0/
publisher:
  type: Person
  id: https://w3id.org/lmodel/capec/knowledge/person/noel-mcloughlin
  name: Noel McLoughlin
---

# capec Knowledge Bundle

A [LOKF](https://lokf.nolan-nichols.com) knowledge base for capec. Every Markdown file under `knowledge/` is one concept; together they form a queryable knowledge graph, derived from this repository's code and docs.

# Services

* [Documentation site](services/documentation-site.md) - The knowledge website in `website/`, an Astro Starlight site that the Knowledge website workflow publishes to GitHub Pages at `https://lmodel.github.io/capec`, built from the README, `docs/`, the schema's pages and the bundle. It replaces the mkdocs site.
* [XML converter](services/xml-converter.md) - `scripts/capec_to_json.py`, the command that turns the CAPEC catalogue's XML into the data the schema describes, by rules it reads from the XSD. It uses only the standard library and is deterministic.

# Datasets

* [capec LinkML schema](datasets/capec-linkml-schema.md) - The LinkML model of CAPEC 3.9 under its XSD 3.5, `src/capec/schema/capec.yaml` (schema id `https://w3id.org/lmodel/capec`): an umbrella that holds only the tree root, `CapecAttackPatternCatalog`, over the modules `capec_entries` and `capec_core`.
* [Core module](datasets/core-module.md) - `src/capec/schema/capec_core.yaml`, the module with the value lists, text types and small records every CAPEC entry shares, and the abstract `CapecEntry`. It imports only `linkml:types`.
* [Entries module](datasets/entries-module.md) - `src/capec/schema/capec_entries.yaml`, the module with `CapecAttackPattern`, `CapecCategory` and `CapecView`, the records an attack pattern holds, and the value lists they use, such as `CapecAbstraction` and `CapecRelatedNature`.
* [Generated artefacts](datasets/generated-artefacts.md) - What `just gen-project` and `just gen-doc` generate from the capec schema: the projections in `project/`, the Python models in `src/capec/datamodel/`, and the merged schema in `docs/schema/`. None is edited by hand.
* [Example data](datasets/example-data.md) - The examples `tests/test_data.py` checks: valid examples of each class, a counter-example for each constraint, and catalogues that break the rules a JSON Schema cannot state, in `tests/data/valid/`, `invalid/` and `problem/invalid/`.
* [Exploiting Software: How to Break Code](datasets/example-external-reference.md) - REF-1 from the catalogue, written as a concept of type `CapecExternalReference` in the adapt copy's keys. It shows that the domain schema admits an external reference as a concept.
* [The schema's adapt copy](datasets/adapt-copy.md) - `.lokf/capec.yaml`, the copy `just lokf-adapt` writes from the schema so that it sits beside LOKF's `lokf.yaml`: rooted on `CapecEntry` and `CapecExternalReference`, with `ID` and `Reference_ID` dropped for LOKF's `id`, and five keys folded into `title` and `description`.
* [Copy of the upstream](datasets/upstream-copy.md) - `upstream/`: MITRE's CAPEC XSD 3.5 and catalogue 3.9, each byte for byte what MITRE serves and pinned by git object hash, with the Terms of Use beside them.
* [Mapping term list](datasets/mapping-term-list.md) - `tests/upstream/mapping-terms.txt`, the classes and properties of Dublin Core, schema.org, SKOS and the SEPSES CAPEC ontology, which `scripts/extract_mapping_terms.py` writes from each vocabulary's pinned file and `tests/test_mappings.py` holds each mapping to.
* [Neighbours' adapt copies](datasets/neighbour-copies.md) - The adapt copies of eleven released lmodel repositories (slsa, github-actions, in-toto, oscal, spdx, stix, attack, uco, cve, kev-catalog and nist-nvd) and of lmodel/cwe's branch in `tests/neighbours/`, each pinned by its SHA-256, against which `tests/test_schema_rules.py` holds this schema's copy apart and `tests/test_mappings.py` holds the mappings.

# References

* [CAPEC catalogue](references/capec-catalogue.md) - The Common Attack Pattern Enumeration and Classification, the catalogue of attack patterns that The MITRE Corporation publishes as XML. Version 3.9 of 24 January 2023 is the latest, with 615 attack patterns, 78 categories, 13 views and 440 external references.
* [CAPEC XSD](references/capec-xsd.md) - The XML Schema of the CAPEC catalogue, version 3.5, namespace `http://capec.mitre.org/capec-3`. Its own header says 3.5.0, dated 21 October 2021. The schema's keys and listed values are this file's.
* [CAPEC Terms of Use](references/capec-terms-of-use.md) - MITRE's terms for CAPEC: a non-exclusive, royalty-free licence for research, development and commercial use, under which a copy must reproduce MITRE's copyright designation and the licence. NOTICE and `upstream/TERMS.txt` do so.

# Explanations

* [Keys and values](explanations/keys-and-values.md) - Why the schema's keys and values are spelled as they are: each key is the XSD's own element or attribute name, such as `Related_Attack_Patterns`, each value the XSD's own text, and classes and enums carry a `Capec` prefix.
* [From XML to data](explanations/xml-to-data.md) - Why a converter stands between the catalogue and the schema, and its rules: MITRE publishes XML, LinkML validates keys and values, and `scripts/capec_to_json.py` turns one into the other without changing a key or a value. A test turns the data back and finds the catalogue.
* [Identifiers and references](explanations/identifiers-and-references.md) - Why a CAPEC number is a string of digits and why references are typed: a number names and never counts, and the rdflib dumper cannot expand a bare identifier, so RDF comes through JSON-LD. `Exclude_ID` ranges over any entry, because the XSD says only that it names an ancestor.
* [Why abstraction levels are values](explanations/abstraction-levels.md) - Why Meta, Standard and Detailed are values of `Abstraction` and not subclasses: no field depends on them. The XSD says an execution flow is usually for Detailed patterns, and CAPEC 3.9 gives flows to all three levels, so no rule ties them.
* [Rules in Python](explanations/rules-in-python.md) - Why `tests/capec_rules.py` exists: a JSON Schema looks at one value at a time, so it cannot say that a reference names an entry the catalogue holds, or that no number is used twice. What the data merely shows goes in `tests/test_catalogue.py` with its counts.
* [Faults in the catalogue](explanations/catalogue-faults.md) - The oddities of CAPEC 3.9 that `tests/test_catalogue.py` pins: CAPEC-244 cites `REF-97`, which the catalogue lacks, two patterns repeat a weakness, two names end in a space, two skills hold no text, eleven flows repeat a step number, and CAPEC-699 is a Meta child of a Standard pattern.
* [Mappings](explanations/mappings.md) - Where the schema crosses to other vocabularies: STIX, ATT&CK, CWE, the SEPSES CAPEC ontology, SKOS, Dublin Core, schema.org and Wikidata. The schema is the one home for mappings, and each is read at its source and held by a test.
* [What the generators do with these keys](explanations/generator-limits.md) - How LinkML's generators treat the XSD's short keys: `gen-owl` warns that six keys shared across classes are ambiguous and gives them no label, the JSON-LD context gives a key one IRI, and the key `Date` shares a docs page with LinkML's type.
* [What the schema leaves out](explanations/scope.md) - What the schema does not do: it says nothing about whether an entry is true, nothing evaluates a view's filter, and it holds the keys the XSD defines even where CAPEC 3.9 uses none, such as `Audience` and `Member_Of`.

# Glossary

* [Attack pattern](glossary/attack-pattern.md) - An attack pattern: a catalogued way that adversaries go about an attack, with what it takes and how to resist it. The class is `CapecAttackPattern`.
* [Category](glossary/capec-category.md) - A CAPEC category: a group of attack patterns that share an effect or intent, and not itself a pattern of attack. The class is `CapecCategory`, and CAPEC 3.9 holds 78.
* [View](glossary/capec-view.md) - A CAPEC view: one way of looking over the catalogue, as a hierarchy (`Graph`) or a slice (`Implicit` by a filter, `Explicit` by hand). The class is `CapecView`, and CAPEC 3.9 holds 13.
* [Abstraction level](glossary/abstraction-level.md) - How concrete an attack pattern is: `Meta` for a broad approach, `Standard` for one method or technique, and `Detailed` for one technique against one technology. The enum is `CapecAbstraction`.
* [Execution flow](glossary/execution-flow.md) - The steps an adversary typically takes in an attack, each with a number, a phase (`Explore`, `Experiment` or `Exploit`), a description and ways of doing it. The key is `Execution_Flow`, and the class of a step is `CapecAttackStep`.
* [Structured text](glossary/structured-text.md) - Text in the catalogue that may hold XHTML markup, such as paragraphs and lists. The XSD's type is `StructuredTextType`, and the schema's is `capec_structured_text`, a string that keeps the markup without its namespace prefix.
* [Adapt copy](glossary/adapt-copy.md) - An adapt copy: the copy of a published LinkML schema that `lokf adapt` writes so that it can sit beside LOKF's `lokf.yaml` in a domain schema, with its chosen roots on `Concept`.

# Playbooks

* [Validate a catalogue](playbooks/validate-a-catalogue.md) - How to validate a CAPEC catalogue: turn the XML into data with `scripts/capec_to_json.py`, run `linkml-validate` with the class `CapecAttackPatternCatalog`, and run `tests/capec_rules.py` for what a JSON Schema cannot state.
* [Regenerate and test](playbooks/regenerate-and-test.md) - How to change the schema: edit `src/capec/schema/`, run `just lint`, `just gen-project`, `just gen-doc`, `just lokf-adapt` and `just test`, and commit what they write. Generated files are never edited by hand.
* [Release](playbooks/release.md) - How a release happens: `semantic-release.yml` reads Conventional Commits on `main`, promotes the `## [Unreleased]` section, tags and publishes. The first release needs the `v0.0.0` baseline tag on `main`, and PyPI publishing stays off.
* [Move to another version](playbooks/update-upstream-pins.md) - How to answer the upstream watch when MITRE publishes another CAPEC version or XSD: read what changed, then move `upstream/`, the pins in `scripts/check_upstream_release.py` and the schema headers together, and let the coverage test say what else moved.
* [Knowledge sources map](playbooks/knowledge-sources.md) - The librarian's scrape map: every repository location and external source this bundle derives concepts from, how to re-check each, and the tracked paths left out with their reasons.

# Policies

* [AI covenant](policies/ai-covenant.md) - The rules for AI-assisted work here: whoever submits owns the contribution, an element says what the XSD says, a rule states only what the upstream states, a mapping is read at its source, and no commit carries an AI co-authorship trailer.
* [Licence and attribution](policies/license-and-attribution.md) - The repository's licences and what it takes from elsewhere: Apache-2.0 for the schema and code, CC BY 4.0 for the bundle, and MITRE's CAPEC Terms of Use for the XSD and catalogue, whose designation and licence NOTICE reproduces. No endorsement is implied.
* [Security policy](policies/security-policy.md) - How to report a vulnerability in this repository, by GitHub's private reporting, what executes here and what holds each surface. A problem in CAPEC itself goes to the CAPEC team.

# Workflows

* [Build and test (main.yaml)](workflows/main.md) - The Build and test workflow: on every pull request and push to `main`, it runs `just test` on Python 3.10 to 3.14, and lints the schema and checks the adapt copy on 3.13.
* [Lint and docs (lint-and-docs.yaml)](workflows/lint-and-docs.md) - The static checks on pull requests, on `main` and every Monday: ShellCheck, actionlint, the word budgets of CONTRIBUTING.md and SECURITY.md, markdownlint, lychee and codespell.
* [Semantic release (semantic-release.yml)](workflows/semantic-release.md) - The workflow that computes the next version from Conventional Commits on `main`, promotes the changelog, tags and publishes a GitHub Release, and dispatches the knowledge release once `KNOWLEDGE_RELEASE_ENABLED` is `true`.
* [Upstream watch (upstream-watch.yaml)](workflows/upstream-watch.md) - The weekly check that `scripts/check_upstream_release.py` runs: another CAPEC version, a changed XSD or catalogue, changed Terms of Use or a new news item fails the run and opens or updates an issue.
* [Knowledge librarian (knowledge-librarian.yaml)](workflows/knowledge-librarian.md) - The sidecar's scheduled agent run that keeps the bundle in step with the repository and opens a pull request for a person to review. It is inert until `KNOWLEDGE_LIBRARIAN_ENABLED` is `true`.
* [Knowledge registrar (knowledge-registrar.yaml)](workflows/knowledge-registrar.md) - The gate on the bundle: it validates the bundle on each pull request that touches it and weekly, and checks that each new `human:` event in a pull request is backed by an approval or a signature. It never judges whether content is true.
* [Knowledge release (knowledge-release.yaml)](workflows/knowledge-release.md) - The workflow that attaches the bundle, a Copilot skill and the schema's adapt copy to a GitHub release, each with a checksum. It starts by hand or, once `KNOWLEDGE_RELEASE_ENABLED` is `true`, on each published release.
* [Knowledge sync (knowledge-sync.yaml)](workflows/knowledge-sync.md) - The weekly workflow that keeps the sidecar's copies and the skills pin at the newest release of Knowledge Trust Ladder, by one pull request that a person merges.
* [Knowledge website (knowledge-website.yaml)](workflows/knowledge-website.md) - The workflow that builds `website/` on each pull request that touches its inputs, and deploys the default branch's build to GitHub Pages once `KNOWLEDGE_WEBSITE_ENABLED` is `true`.
