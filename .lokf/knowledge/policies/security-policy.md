---
type: Policy
id: https://w3id.org/lmodel/capec/knowledge/policies/security-policy
genre: reference
title: Security policy
description: How to report a vulnerability in this repository, by GitHub's private reporting, what executes here and what holds each surface. A problem in CAPEC itself goes to the CAPEC team.
resource: SECURITY.md
references:
  - https://w3id.org/lmodel/capec/knowledge/workflows/upstream-watch
sources:
  - id: security.md
    resource: SECURITY.md
generated:
  by: process:ktl-librarian
  at: "2026-11-04T02:37:57Z"
status: draft
---

# Security policy

Report a vulnerability through GitHub's private vulnerability reporting. Only the latest release receives fixes.[^security.md]

The release carries the adapt copy, the bundle as a zip and a Copilot skill zip, each with a checksum and a build-provenance attestation.[^security.md]

The catalogue is data that this repository treats as data. Tests convert and validate it, and nothing executes it.[^security.md]

The watch reads MITRE's public pages on `capec.mitre.org` only, and sends no token.[^security.md]

Report a problem in CAPEC or its XSD to the CAPEC team.[^security.md]

[^security.md]: SECURITY.md
