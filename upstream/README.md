# The upstream's files

This folder holds what the schema renders, unchanged, as The MITRE Corporation publishes it:

- `ap_schema_v3.5.xsd`: the CAPEC XML Schema, version 3.5, from <https://capec.mitre.org/data/xsd/ap_schema_v3.5.xsd>. Its own header calls it 3.5.0, dated 21 October 2021.
- `capec_v3.9.xml`: the CAPEC catalogue, version 3.9, dated 2023-01-24, from <https://capec.mitre.org/data/xml/capec_v3.9.xml>. It is the last release, and it validates against that XSD with no error.
- `TERMS.txt`: the Terms of Use these copies come under.

`scripts/check_upstream_release.py` pins each by its git object hash and watches the addresses each week. Never edit a file here: move the pins and the schema header together for another version.
