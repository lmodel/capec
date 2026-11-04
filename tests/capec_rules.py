"""The catalogue's rules that a JSON Schema cannot state.

A JSON Schema looks at one value at a time, so it cannot say that a number names an
entry that exists or that two entries differ. The XSD's unique constraints say the
second, and the XSD's words on each reference say the first, without a keyref to
hold them. This module checks both over a whole catalogue. A consumer who wants the
catalogue checked in full runs it beside the JSON Schema.
"""

from __future__ import annotations

ENTRY_LISTS = ("Attack_Patterns", "Categories", "Views")


def rule_errors(instance, class_name: str) -> list[tuple[str, str]]:
    """Each breach of these rules, as a JSON pointer and a sentence. Only a catalogue
    can break them, since only a catalogue holds what a reference points to."""
    if class_name != "CapecAttackPatternCatalog":
        return []
    return [*_identity_errors(instance), *_reference_errors(instance)]


def _identity_errors(catalogue):
    """An entry's number is unique across the three kinds, and so is a reference's."""
    seen = {}
    for kind in ENTRY_LISTS:
        for index, entry in enumerate(catalogue.get(kind) or []):
            pointer = f"/{kind}/{index}/ID"
            if entry["ID"] in seen:
                yield pointer, f"{entry['ID']} is also at {seen[entry['ID']]}"
            seen.setdefault(entry["ID"], pointer)
    seen = {}
    for index, reference in enumerate(catalogue.get("External_References") or []):
        pointer = f"/External_References/{index}/Reference_ID"
        name = reference["Reference_ID"]
        if name in seen:
            yield pointer, f"{name} is also at {seen[name]}"
        seen.setdefault(name, pointer)


def _reference_errors(catalogue):
    """Each typed reference names something this catalogue holds, of the right kind."""
    patterns = {e["ID"] for e in catalogue.get("Attack_Patterns") or []}
    entries = set(patterns)
    for kind in ("Categories", "Views"):
        entries |= {e["ID"] for e in catalogue.get(kind) or []}
    references = {r["Reference_ID"] for r in catalogue.get("External_References") or []}

    def one(pointer, value, known, what):
        if value not in known:
            yield f"{pointer}", f"{value} names no {what} in this catalogue"

    def excluded(pointer, holder):
        for index, exclude in enumerate(holder.get("Exclude_Related") or []):
            yield from one(
                f"{pointer}/Exclude_Related/{index}/Exclude_ID",
                exclude["Exclude_ID"],
                entries,
                "entry",
            )

    for kind in ENTRY_LISTS:
        for index, entry in enumerate(catalogue.get(kind) or []):
            at = f"/{kind}/{index}"
            for i, cited in enumerate(entry.get("References") or []):
                yield from one(
                    f"{at}/References/{i}/External_Reference_ID",
                    cited["External_Reference_ID"],
                    references,
                    "external reference",
                )
            for i, related in enumerate(entry.get("Related_Attack_Patterns") or []):
                pointer = f"{at}/Related_Attack_Patterns/{i}"
                yield from one(
                    f"{pointer}/CAPEC_ID",
                    related["CAPEC_ID"],
                    patterns,
                    "attack pattern",
                )
                yield from excluded(pointer, related)
            for i, step in enumerate(entry.get("Execution_Flow") or []):
                for j, technique in enumerate(step.get("Technique") or []):
                    if "CAPEC_ID" in technique:
                        yield from one(
                            f"{at}/Execution_Flow/{i}/Technique/{j}/CAPEC_ID",
                            technique["CAPEC_ID"],
                            entries,
                            "entry",
                        )
            for field in ("Relationships", "Members"):
                holder = entry.get(field) or {}
                for key in ("Member_Of", "Has_Member"):
                    for i, member in enumerate(holder.get(key) or []):
                        pointer = f"{at}/{field}/{key}/{i}"
                        yield from one(
                            f"{pointer}/CAPEC_ID",
                            member["CAPEC_ID"],
                            entries,
                            "entry",
                        )
                        yield from excluded(pointer, member)
