# Problem Fixtures

This directory stores known LinkML tooling-gap cases that are currently not suitable for the normal `tests/data/valid` or `tests/data/invalid` suites.

## Why These Cases Live Here

The current LinkML toolchain can diverge between:

1. JSON Schema validation expectations (class-typed inlined list entries are object-shaped).
2. Runtime YAML normalization behavior for inlined lists with minimal one-key objects.

For CAPEC relationship members (for example `HasMember`/`MemberOf`), this can force fixture encodings that are tool-workaround-specific rather than canonical source-model examples.

## Usage

- `problem/valid`: examples that are semantically valid for CAPEC but currently require unsupported or unstable tooling behavior.
- `problem/invalid`: examples that expose known false positives/false negatives in current tooling.

These files document pending tooling limitations and should not be used to drive pass/fail expectations in the primary valid/invalid fixture tests until support improves.
