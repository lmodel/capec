---
type: Explanation
id: https://w3id.org/lmodel/capec/knowledge/explanations/catalogue-faults
genre: explanation
title: Faults in the catalogue
description: "The oddities of CAPEC 3.9 that `tests/test_catalogue.py` pins: CAPEC-244 cites `REF-97`, which the catalogue lacks, two patterns repeat a weakness, two names end in a space, two skills hold no text, eleven flows repeat a step number, and CAPEC-699 is a Meta child of a Standard pattern."
about:
  - https://w3id.org/lmodel/capec/knowledge/references/capec-catalogue
sources:
  - id: test_catalogue.py
    resource: tests/test_catalogue.py
generated:
  by: process:ktl-librarian
  at: "2026-11-04T02:47:00Z"
status: draft
---

# Faults in the catalogue

The rules find one fault: CAPEC-244 cites `REF-97`, which the catalogue does not hold.[^test_catalogue.py]

The tests also pin these:[^test_catalogue.py]

- CAPEC-545 and CAPEC-644 each name one weakness twice, so 1214 rows make 1212 pairs.
- CAPEC-552 and view 658 have a name that ends in a space.
- CAPEC-509 and CAPEC-701 each have a skill with no text.
- Eleven flows repeat a step number.
- The text of CAPEC-86 cites `REF-97`, and the text of CAPEC-197 cites `REF-686`, though neither lists that reference.
- Thirty-three of the 440 external references are cited by no entry.
- CAPEC-699, a Meta pattern, is a child of CAPEC-651, a Standard pattern.

A fix upstream fails the test that pins it, so someone reads the new version.[^test_catalogue.py]

[^test_catalogue.py]: tests/test_catalogue.py
