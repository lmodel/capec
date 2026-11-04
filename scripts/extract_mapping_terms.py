#!/usr/bin/env python3
# /// script
# requires-python = ">=3.10"
# dependencies = ["rdflib>=7.1"]
# ///
"""List the terms of the vocabularies the schema's mappings name.

The schema maps its classes and attributes to terms of Dublin Core, schema.org, SKOS
and the SEPSES CAPEC ontology. tests/test_mappings.py checks each mapping against
the list this script writes, tests/upstream/mapping-terms.txt, so that no IRI is
invented. It holds each class and property that a vocabulary's published file
declares in its own namespace, and no label or comment.

The script downloads each file into memory, refuses it unless its SHA-256 is the
pinned one, and writes the list, sorted. Nothing else is written. Terms of STIX and
ATT&CK are checked against the neighbours' released copies in tests/neighbours/
instead, and the Wikidata entities are named by hand below, since an entity on
Wikidata has no fixed file to pin. Usage::

    uv run scripts/extract_mapping_terms.py [OUTPUT_FILE]

When a pinned file moves, move its pin here, rerun this script, and move the list's
checksum in tests/test_mappings.py.
"""

from __future__ import annotations

import hashlib
import sys
import urllib.request
from pathlib import Path

from rdflib import OWL, RDF, RDFS, Graph, URIRef

OUTPUT = (
    Path(__file__).resolve().parent.parent / "tests" / "upstream" / "mapping-terms.txt"
)
USER_AGENT = "lmodel-capec-terms"
MAX_BYTES = 5_000_000

# Each vocabulary, by its prefix, its namespace, the address of its published
# file, the file's syntax and the file's SHA-256 as read on 2026-11-04.
VOCABULARIES = (
    (
        "dcterms",
        "http://purl.org/dc/terms/",
        "https://www.dublincore.org/specifications/dublin-core/dcmi-terms/dublin_core_terms.ttl",
        "turtle",
        "13df401072dd7015bf9d75162f3e41c8138075304b7b9cc1aa1e9c16db976797",
    ),
    (
        "schema",
        "http://schema.org/",
        "https://raw.githubusercontent.com/schemaorg/schemaorg/main/data/releases/30.1/schemaorg-current-http.ttl",
        "turtle",
        "62f11b228082fd5cad332734ae9566c9c93dfe2491aa8048c2954851687390db",
    ),
    (
        "sepses_capec",
        "http://w3id.org/sepses/vocab/ref/capec#",
        "https://www.sepses.org/vocab/ref/capec/ontology.ttl",
        "turtle",
        "22a0aecd885ee1d96c75d97593a0dfda0409696d696cd94fd32b5c9515c9bd16",
    ),
    (
        "skos",
        "http://www.w3.org/2004/02/skos/core#",
        "https://www.w3.org/2009/08/skos-reference/skos.rdf",
        "xml",
        "e79633b8d0564816cee8a99f5c9acf9a0e6fc7257c7209acd684ecad53a89dd6",
    ),
)

# Each read at https://www.wikidata.org/wiki/Special:EntityData/<id>.json on
# 2026-11-04: Q2986817 is "Common Attack Pattern Enumeration and Classification",
# "catalog of known cyber security attack patterns"; P3624 is "CWE ID", whose format
# is [1-9]\d{1,4}. A search of Wikidata's properties for CAPEC finds none.
BY_HAND = (
    "http://www.wikidata.org/entity/Q2986817",
    "http://www.wikidata.org/prop/direct/P3624",
)

TERM_TYPES = {
    RDFS.Class,
    OWL.Class,
    RDF.Property,
    OWL.ObjectProperty,
    OWL.DatatypeProperty,
    OWL.AnnotationProperty,
}


def fetch(url: str) -> bytes:
    """A file's bytes, read into memory and capped at MAX_BYTES."""
    req = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})
    with urllib.request.urlopen(req, timeout=60) as resp:
        data = resp.read(MAX_BYTES + 1)
    if len(data) > MAX_BYTES:
        raise SystemExit(f"{url}: larger than {MAX_BYTES} bytes")
    return data


def main(argv: list[str]) -> int:
    output = Path(argv[1]) if len(argv) > 1 else OUTPUT
    terms = set(BY_HAND)
    header = [
        "# Classes and properties of the vocabularies the schema's mappings name."
    ]
    for prefix, namespace, url, syntax, sha256 in VOCABULARIES:
        data = fetch(url)
        found = hashlib.sha256(data).hexdigest()
        if found != sha256:
            raise SystemExit(f"{url}: SHA-256 {found}, not the pinned {sha256}")
        graph = Graph().parse(data=data, format=syntax)
        terms |= {
            str(subject)
            for subject, kind in graph.subject_objects(RDF.type)
            if isinstance(subject, URIRef)
            and kind in TERM_TYPES
            and str(subject).startswith(namespace)
        }
        header.append(f"# {prefix} {namespace} from {url}, SHA-256 {sha256}.")
    header.append(
        "# Q2986817 and P3624 are named by hand in scripts/extract_mapping_terms.py."
    )
    output.write_text("\n".join([*header, *sorted(terms)]) + "\n", encoding="utf-8")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
