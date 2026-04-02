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

## Concrete Examples

The snippets below show the exact CAPEC relationship shape across LinkML schema source,
generated JSON Schema, and problem fixtures in this directory.

### 1) LinkML Schema Shape (`docs/schema/capec.yaml`)

```yaml
member_of:
  name: member_of
  description: Member_Of relationships showing that this category or view is a member
    of a given view or parent category, identified by CAPEC_ID.
  range: MemberOf
  multivalued: true
  inlined: true
  inlined_as_list: true

has_member:
  name: has_member
  description: Has_Member relationships showing that this category or view contains
    a given attack pattern or category as a member, identified by CAPEC_ID.
  range: HasMember
  multivalued: true
  inlined: true
  inlined_as_list: true
```

### 2) Generated JSON Schema Shape (`project/jsonschema/capec.schema.json`)

```json
"Relationships": {
  "additionalProperties": false,
  "properties": {
    "has_member": {
      "items": { "$ref": "#/$defs/HasMember" },
      "type": ["array", "null"]
    },
    "member_of": {
      "items": { "$ref": "#/$defs/MemberOf" },
      "type": ["array", "null"]
    }
  }
}
```

This object-array expectation is one source of mismatch when runtime normalization
encounters minimal or shorthand YAML entries.

### 3) Affected Fixture Data (`tests/data/problem/valid`)

`Category-118.yaml` uses the canonical object-array encoding:

```yaml
relationships:
  has_member:
    - capec_id: 116
      exclude_related: []
    - capec_id: 117
      exclude_related: []
```

`View-1000.yaml` shows the same pattern for a view member list:

```yaml
members:
  has_member:
    - capec_id: 156
      exclude_related: []
    - capec_id: 210
      exclude_related: []
```

These fixtures are intentionally placed under `problem/valid` because they model valid
CAPEC content but currently exercise edge behavior in tooling around inlined-list object
normalization.

