---
type: Explanation
id: https://w3id.org/lmodel/capec/knowledge/explanations/abstraction-levels
genre: explanation
title: Why abstraction levels are values
description: "Why Meta, Standard and Detailed are values of `Abstraction` and not subclasses: no field depends on them. The XSD says an execution flow is usually for Detailed patterns, and CAPEC 3.9 gives flows to all three levels, so no rule ties them."
about:
  - https://w3id.org/lmodel/capec/knowledge/glossary/abstraction-level
  - https://w3id.org/lmodel/capec/knowledge/glossary/execution-flow
sources:
  - id: about.md
    resource: docs/about.md
    title: How a catalogue is shaped
generated:
  by: process:ktl-librarian
  at: "2026-11-04T02:37:57Z"
status: draft
verified:
  - by: process:ktl-librarian
    at: "2026-11-04T02:44:15Z"
---

# Why abstraction levels are values

Meta, Standard and Detailed are values of `Abstraction`, not subclasses, since no field depends on them.[^about.md]

The XSD says an execution flow is usually for Detailed patterns. In CAPEC 3.9, 149 Detailed patterns have one, and so do 80 Standard patterns and 10 Meta patterns, so no rule ties them.[^about.md]

[^about.md]: docs/about.md, How a catalogue is shaped
