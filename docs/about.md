# About capec

This page is for anyone reading the schema's elements: it says how the classes fit together and what the model leaves out.

## How a catalogue is shaped

`CapecAttackPatternCatalog` is the tree root. It holds the attack patterns, the categories, the views and the external references that entries cite.

The three kinds of entry share a base, `CapecEntry`, which holds the number, name and status, and the references, notes and history. The XSD has no such base: it repeats those fields on each type. The base is there because the numbers of the three kinds do not overlap, so a member reference can name any kind of entry. The module `capec_core` holds what all of them use, and `capec_entries` the entries themselves.

Meta, Standard and Detailed are values of `Abstraction`, not subclasses, since no field depends on them. The XSD says an execution flow is usually for Detailed patterns. In CAPEC 3.9, 149 Detailed patterns have one, and so do 80 Standard patterns and 10 Meta patterns, so no rule ties them.

## Keys and values

The keys and values are the XSD's own, such as `Related_Attack_Patterns`, `CAPEC_ID` and `Access Control`, and the classes and enums carry a `Capec` prefix. Each class's and enum's `xsd_type` annotation names the XSD type or path that it renders.

`scripts/capec_to_json.py` states the rules that turn XML into data:

- an attribute or a child element becomes a key of the same name, and a child that may repeat holds a list;
- an element whose whole content is one repeating child becomes a list under its own name, so `Related_Attack_Patterns` holds the patterns directly;
- an element that holds text and has attributes becomes an object with its text under `Value`;
- text that may hold XHTML becomes a string holding that markup, with the namespace prefix removed.

## Where the schema is narrower than the XSD

The XSD types a CAPEC number as `xs:integer`, which also admits zero and negative numbers. The schema writes it as a string of digits that does not begin with zero, since a number names and never counts, and every number in the catalogue fits. It keeps `xs:string` for a reference's identifier and adds the form `REF-1`, which the XSD gives as its example and every reference follows.

A reference to another entry ranges over the class it names, so OWL and JSON-LD treat it as a link. `Exclude_ID` ranges over any entry, because the XSD says only that it names an ancestor, though all 260 in CAPEC 3.9 name a category. `Technique`'s `CAPEC_ID` is `xs:string` in the XSD and no technique sets it, so it takes any string, and it ranges over an entry so that the key means one thing.

## What the XSD defines and the catalogue does not use

CAPEC 3.9 uses none of these, and the schema has them because the XSD does: a view's `Audience`, `Member_Of`, a history's `Contribution`, `Mapping_Fit`, `Consequence_ID`, `Modification_Importance`, `Submission_Comment` and `Technique`'s `CAPEC_ID`. Their examples hold invented values.

## What the generators do with these keys

Several classes share a short key, such as `Name`, `Type`, `Value` and `Description`, and each keeps one IRI under the schema's prefix. gen-owl warns that those six keys are ambiguous and gives their properties no label or definition. The class pages still describe each one. The JSON-LD context gives a key one IRI too, so a `Description` of any class projects as `capec:Description`.

The key `Date` and LinkML's own type `Date` write the same page, and the type's page wins, so the site has no page for that key.

## What is left out

Filters in the views are data here and nothing evaluates them. Eight of the nine are XPath 1.0, and view 553's is XPath 2.0, which uses a list of numbers.

The schema says nothing about whether what an entry claims is true.
