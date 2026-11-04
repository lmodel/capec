# Services

* [Documentation site](documentation-site.md) - The knowledge website in `website/`, an Astro Starlight site that the Knowledge website workflow publishes to GitHub Pages at `https://lmodel.github.io/capec`, built from the README, `docs/`, the schema's pages and the bundle. It replaces the mkdocs site.
* [XML converter](xml-converter.md) - `scripts/capec_to_json.py`, the command that turns the CAPEC catalogue's XML into the data the schema describes, by rules it reads from the XSD. It uses only the standard library and is deterministic.
