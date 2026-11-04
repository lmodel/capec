# Glossary

* [Attack pattern](attack-pattern.md) - An attack pattern: a catalogued way that adversaries go about an attack, with what it takes and how to resist it. The class is `CapecAttackPattern`.
* [Category](capec-category.md) - A CAPEC category: a group of attack patterns that share an effect or intent, and not itself a pattern of attack. The class is `CapecCategory`, and CAPEC 3.9 holds 78.
* [View](capec-view.md) - A CAPEC view: one way of looking over the catalogue, as a hierarchy (`Graph`) or a slice (`Implicit` by a filter, `Explicit` by hand). The class is `CapecView`, and CAPEC 3.9 holds 13.
* [Abstraction level](abstraction-level.md) - How concrete an attack pattern is: `Meta` for a broad approach, `Standard` for one method or technique, and `Detailed` for one technique against one technology. The enum is `CapecAbstraction`.
* [Execution flow](execution-flow.md) - The steps an adversary typically takes in an attack, each with a number, a phase (`Explore`, `Experiment` or `Exploit`), a description and ways of doing it. The key is `Execution_Flow`, and the class of a step is `CapecAttackStep`.
* [Structured text](structured-text.md) - Text in the catalogue that may hold XHTML markup, such as paragraphs and lists. The XSD's type is `StructuredTextType`, and the schema's is `capec_structured_text`, a string that keeps the markup without its namespace prefix.
* [Adapt copy](adapt-copy.md) - An adapt copy: the copy of a published LinkML schema that `lokf adapt` writes so that it can sit beside LOKF's `lokf.yaml` in a domain schema, with its chosen roots on `Concept`.
