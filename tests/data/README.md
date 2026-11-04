# Example data for capec

- `valid/` holds examples of each class, which `linkml-run-examples` and `tests/test_data.py` read. Most values come from the catalogue, and a file named `-every-key` holds invented values where CAPEC 3.9 does not use a key the XSD defines.
- `invalid/` holds a counter-example for each constraint the validator can state. Each file's first line, `# Fails at: <JSON pointer>`, names its one failing place, and `tests/test_data.py` holds it there.
- `problem/invalid/` holds a counter-example for each rule the generated JSON Schema cannot state, which `tests/capec_rules.py` checks.

A file name is `ClassName-anything.yaml`, and the class is the part before the first hyphen. `tests/test_data.py` also builds each entry example back into XML and asks MITRE's own XSD about it, so an example here says nothing the XSD does not. The whole catalogue is checked by `tests/test_catalogue.py`.

Values taken from the catalogue fall under MITRE's Terms of Use, which [NOTICE](../../NOTICE) states.
