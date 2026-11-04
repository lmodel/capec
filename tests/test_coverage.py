"""Walks the XSD beside the classes and enums, in both directions.

Every element and attribute the XSD allows must be a key of the class that names its
type in `xsd_type`, with the same cardinality and kind of value, and every key of a
class must be in the XSD. Each enum must hold exactly the XSD's values, in its order.
Nothing here reads the catalogue: that is tests/test_catalogue.py.
"""

import pytest
from linkml_runtime import SchemaView

from tests.capec_xml import ROOT, xsd

SCHEMA = ROOT / "src" / "capec" / "schema" / "capec.yaml"
VIEW = SchemaView(str(SCHEMA))

# What a simple type of the XSD's becomes.
TYPES = {
    "xs:string": "string",
    "xs:date": "date",
    "xs:anyURI": "capec_uri",
    "xs:gYear": "capec_year",
    "xs:gMonth": "capec_month",
    "xs:gDay": "capec_day",
    "xs:integer": "integer",
    "StructuredTextType": "capec_structured_text",
}

# Where the schema is narrower than the XSD's plain type, each by a decision the
# docs state. The XSD's words say these name another thing, and its xs:integer holds
# a number that names and never counts.
TYPED = {
    ("CapecEntry", "ID"): "capec_numeric_id",
    ("CapecAttackPattern", "ID"): "capec_numeric_id",
    ("CapecCategory", "ID"): "capec_numeric_id",
    ("CapecView", "ID"): "capec_numeric_id",
    ("CapecRelatedWeakness", "CWE_ID"): "capec_numeric_id",
    ("CapecExternalReference", "Reference_ID"): "capec_reference_id",
    ("CapecRelatedAttackPattern", "CAPEC_ID"): "CapecAttackPattern",
    ("CapecMemberOf", "CAPEC_ID"): "CapecEntry",
    ("CapecHasMember", "CAPEC_ID"): "CapecEntry",
    ("CapecTechnique", "CAPEC_ID"): "CapecEntry",
    ("CapecExcludeRelated", "Exclude_ID"): "CapecEntry",
    ("CapecReference", "External_Reference_ID"): "CapecExternalReference",
}


def _shapes():
    """Every shape the XSD reaches from its root, by name."""
    found = {}

    def visit(shape):
        if shape.name in found:
            return
        found[shape.name] = shape
        for child in shape.children:
            visit(child.shape)

    visit(xsd().root_element().shape)
    return found


SHAPES = _shapes()
CLASSES = {
    name: cls
    for name, cls in VIEW.all_classes().items()
    if not cls.abstract and not cls.mixin
}
ENUMS = VIEW.all_enums()


def _annotation(element):
    return element.annotations["xsd_type"].value


def _is_record(shape):
    """A shape that becomes a class: it has fields, and it is not a mere wrapper."""
    return bool(shape.attributes or shape.children) and not shape.wrapped


def _expected(shape):
    """Each key the XSD gives this shape: whether it is required and repeats, and what
    its values are."""
    keys = {}
    for attribute in shape.attributes:
        keys[attribute.key] = (attribute.required, False, attribute)
    for child in shape.children:
        wrapped = child.shape.wrapped
        if wrapped:
            keys[child.key] = (child.least >= 1, True, wrapped.shape)
        else:
            keys[child.key] = (child.least >= 1, child.repeats, child.shape)
    if shape.text:
        keys["Value"] = (True, False, "text")
    return keys


def _kind(value, shape):
    """The range the XSD asks for."""
    if value == "text":
        return TYPES[
            "StructuredTextType" if shape.text == "structured" else "xs:string"
        ]
    if hasattr(value, "required"):  # An attribute.
        if value.values:
            return f"enum:{value.xsd_type or f'{shape.name}/@{value.key}'}"
        return TYPES[f"xs:{value.xsd_type}"] if value.xsd_type else "string"
    if _is_record(value):
        return f"class:{value.name}"
    if value.values:
        return f"enum:{value.name}"
    return TYPES[value.name if value.text == "structured" else value.xsd_type]


def _kind_of_slot(slot):
    """The range the schema gives."""
    if slot.range in ENUMS:
        return f"enum:{_annotation(ENUMS[slot.range])}"
    if slot.range in CLASSES:
        return f"class:{_annotation(CLASSES[slot.range])}"
    return slot.range


@pytest.mark.parametrize("name", sorted(CLASSES))
def test_each_class_names_a_shape_of_the_xsd(name):
    assert _annotation(CLASSES[name]) in SHAPES, name


def test_each_record_of_the_xsd_has_one_class():
    """Nothing in the XSD that needs a class goes without, and none has two."""
    wanted = {name for name, shape in SHAPES.items() if _is_record(shape)}
    named = [_annotation(cls) for cls in CLASSES.values()]
    assert sorted(named) == sorted(wanted)


@pytest.mark.parametrize("name", sorted(CLASSES))
def test_a_class_has_exactly_the_xsds_keys(name):
    shape = SHAPES[_annotation(CLASSES[name])]
    assert set(VIEW.class_slots(name)) == set(_expected(shape))


@pytest.mark.parametrize("name", sorted(CLASSES))
def test_each_key_has_the_xsds_cardinality_and_kind(name):
    shape = SHAPES[_annotation(CLASSES[name])]
    for key, (required, repeats, value) in _expected(shape).items():
        slot = VIEW.induced_slot(key, name)
        assert bool(slot.required or slot.identifier) == required, key
        assert bool(slot.multivalued) == repeats, key
        if (name, key) in TYPED:
            assert slot.range == TYPED[(name, key)], key
        else:
            assert _kind_of_slot(slot) == _kind(value, shape), key


def _enumerations():
    """Each list of values in the XSD: named simple types, and those written inline."""
    found = {}
    for shape in SHAPES.values():
        if shape.values:
            found[shape.name] = shape.values
        for attribute in shape.attributes:
            if attribute.values:
                name = attribute.xsd_type or f"{shape.name}/@{attribute.key}"
                found[name] = attribute.values
    return found


def test_every_enumeration_of_the_xsd_has_an_enum():
    named = sorted(_annotation(enum) for enum in ENUMS.values())
    assert named == sorted(_enumerations())


@pytest.mark.parametrize("name", sorted(ENUMS))
def test_an_enum_holds_the_xsds_values_in_its_order(name):
    values = _enumerations()[_annotation(ENUMS[name])]
    assert tuple(ENUMS[name].permissible_values) == values


def test_the_entry_kinds_share_the_base():
    """The three entry types hold the base's fields in the XSD, and the same ones."""
    for name in ("CapecAttackPattern", "CapecCategory", "CapecView"):
        assert VIEW.get_class(name).is_a == "CapecEntry", name
    for key in VIEW.get_class("CapecEntry").attributes:
        for name in ("AttackPatternType", "CategoryType", "ViewType"):
            assert key in _expected(SHAPES[name]), (key, name)


def test_every_class_and_enum_is_described():
    for name, element in {**VIEW.all_classes(), **ENUMS}.items():
        assert element.description, name
    for name in VIEW.all_classes():
        for key in VIEW.class_slots(name):
            assert VIEW.induced_slot(key, name).description, (name, key)
