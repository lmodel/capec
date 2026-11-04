# capec

This project is a LinkML model of the Common Attack Pattern Enumeration and Classification (CAPEC), the catalogue of attack patterns that The MITRE Corporation publishes. It renders catalogue version 3.9 under XML Schema (XSD) version 3.5, and keeps the XSD's own keys and listed values.

- [Schema documentation](elements/index.md), generated from the schema
- [About](about.md): how the classes fit together and what the model leaves out
- [`capec.yaml`](schema/capec.yaml): the schema, with its modules merged

## Validating a catalogue

MITRE publishes XML, and LinkML validates a tree of keys and values, so the first step turns one into the other. It changes no key and no value, and it stops on a key the XSD does not declare, so a catalogue that leaves its schema is noticed.

```bash
uv run scripts/capec_to_json.py upstream/capec_v3.9.xml upstream/ap_schema_v3.5.xsd --output catalogue.json
uv run linkml-validate -s src/capec/schema/capec.yaml -C CapecAttackPatternCatalog catalogue.json
```

`just validate-catalogue` runs both on the copy in `upstream/`. `project/jsonschema/capec.schema.json` is the same schema for anyone without LinkML. A JSON Schema looks at one value at a time, so a consumer who wants the catalogue checked in full also runs `tests/capec_rules.py`:

- that a reference names an external reference the catalogue holds;
- that a related pattern, a member and an excluded ancestor name an entry the catalogue holds, and a related pattern names an attack pattern;
- that no number is used by two entries, whatever their kind, and no external reference identifier twice.

## Getting RDF

`linkml-convert -t rdf` stops on this schema with `Unknown CURIE prefix: @base`. The identifiers are bare digits, as MITRE writes them, and the rdflib dumper in linkml-runtime 1.12.1 cannot expand one. JSON-LD can: add `project/jsonld/capec.context.jsonld` as the data's `@context`, and parse it with the base `https://w3id.org/lmodel/capec/`. CAPEC-1 is then `capec:1`, and a reference is an IRI, which `tests/test_catalogue.py` checks on a sample.

## What was checked

The whole catalogue validates, with its 615 attack patterns, 78 categories, 13 views and 440 external references. `tests/test_conversion.py` turns the data back into XML and finds it equal to the catalogue, and MITRE's own XSD accepts it. `tests/test_coverage.py` walks the XSD beside the classes and enums and fails on anything missing, added or of another cardinality or kind.

The rules find one fault in the catalogue. CAPEC-244 cites `REF-97`, which it does not hold. `tests/test_catalogue.py` pins that fault and the catalogue's other oddities, so a fix upstream fails it and someone reads the new version.
