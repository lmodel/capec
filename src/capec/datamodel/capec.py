# Auto generated from capec.yaml by pythongen.py version: 0.0.1
# Generation date: 2026-04-02T15:00:08
# Schema: capec
#
# id: https://w3id.org/lmodel/capec
# description: Common Attack Pattern Enumeration and Classification (CAPEC): A comprehensive dictionary
#   of known patterns of attack employed by adversaries to exploit known weaknesses in
#   cyber-enabled capabilities. CAPEC is a community-developed list maintained by The MITRE
#   Corporation that helps users understand how adversaries exploit weaknesses in applications
#   and other cyber-enabled capabilities. The schema is maintained by The MITRE Corporation
#   and developed in partnership with the public CAPEC Community.
# license: Apache-2.0

import dataclasses
import re
from dataclasses import dataclass
from datetime import (
    date,
    datetime,
    time
)
from typing import (
    Any,
    ClassVar,
    Dict,
    List,
    Optional,
    Union
)

from jsonasobj2 import (
    JsonObj,
    as_dict
)
from linkml_runtime.linkml_model.meta import (
    EnumDefinition,
    PermissibleValue,
    PvFormulaOptions
)
from linkml_runtime.utils.curienamespace import CurieNamespace
from linkml_runtime.utils.enumerations import EnumDefinitionImpl
from linkml_runtime.utils.formatutils import (
    camelcase,
    sfx,
    underscore
)
from linkml_runtime.utils.metamodelcore import (
    bnode,
    empty_dict,
    empty_list
)
from linkml_runtime.utils.slot import Slot
from linkml_runtime.utils.yamlutils import (
    YAMLRoot,
    extended_float,
    extended_int,
    extended_str
)
from rdflib import (
    Namespace,
    URIRef
)

from linkml_runtime.linkml_model.types import Date, Integer, String
from linkml_runtime.utils.metamodelcore import XSDDate

metamodel_version = "1.7.0"
version = None

# Namespaces
ATTACK = CurieNamespace('attack', 'https://attack.mitre.org/')
CAPEC = CurieNamespace('capec', 'https://w3id.org/lmodel/capec/')
DCTERMS = CurieNamespace('dcterms', 'http://purl.org/dc/terms/')
LINKML = CurieNamespace('linkml', 'https://w3id.org/linkml/')
OWASP = CurieNamespace('owasp', 'https://owasp.org/')
SCHEMA = CurieNamespace('schema', 'http://schema.org/')
STIX = CurieNamespace('stix', 'https://w3id.org/lmodel/stix/')
WASC = CurieNamespace('wasc', 'http://projects.webappsec.org/')
XSD = CurieNamespace('xsd', 'http://www.w3.org/2001/XMLSchema#')
DEFAULT_ = CAPEC


# Types
class Uri(str):
    """ URI value represented as a string. """
    type_class_uri = XSD["anyURI"]
    type_class_curie = "xsd:anyURI"
    type_name = "Uri"
    type_model_uri = CAPEC.Uri


class StructuredText(str):
    """ Mixed content type allowing XHTML content embedded within standard string data.
Some common XHTML elements that may appear: BR for line breaks, UL/LI for bulleted
lists, OL/LI for numbered lists, and DIV for indented sections. """
    type_class_uri = XSD["string"]
    type_class_curie = "xsd:string"
    type_name = "StructuredText"
    type_model_uri = CAPEC.StructuredText


# Class references
class AttackPatternId(extended_int):
    pass


class CategoryId(extended_int):
    pass


class ViewId(extended_int):
    pass


class ExternalReferenceReferenceId(extended_str):
    pass


@dataclass(repr=False)
class AttackPatternCatalog(YAMLRoot):
    """
    The root element used to hold an enumerated catalog of common attack patterns.
    Each catalog can be organized by optional Views and Categories. The catalog also
    contains a list of all External_References that may be shared throughout the
    individual attack patterns. The required Name and Version attributes are used to
    uniquely identify the catalog. The required Date attribute identifies the date when
    this catalog was created or last updated.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CAPEC["AttackPatternCatalog"]
    class_class_curie: ClassVar[str] = "capec:AttackPatternCatalog"
    class_name: ClassVar[str] = "AttackPatternCatalog"
    class_model_uri: ClassVar[URIRef] = CAPEC.AttackPatternCatalog

    name: str = None
    version: str = None
    entry_date: Union[str, XSDDate] = None
    attack_patterns: Optional[Union[dict[Union[int, AttackPatternId], Union[dict, "AttackPattern"]], list[Union[dict, "AttackPattern"]]]] = empty_dict()
    categories: Optional[Union[dict[Union[int, CategoryId], Union[dict, "Category"]], list[Union[dict, "Category"]]]] = empty_dict()
    views: Optional[Union[dict[Union[int, ViewId], Union[dict, "View"]], list[Union[dict, "View"]]]] = empty_dict()
    external_references: Optional[Union[dict[Union[str, ExternalReferenceReferenceId], Union[dict, "ExternalReference"]], list[Union[dict, "ExternalReference"]]]] = empty_dict()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.name):
            self.MissingRequiredField("name")
        if not isinstance(self.name, str):
            self.name = str(self.name)

        if self._is_empty(self.version):
            self.MissingRequiredField("version")
        if not isinstance(self.version, str):
            self.version = str(self.version)

        if self._is_empty(self.entry_date):
            self.MissingRequiredField("entry_date")
        if not isinstance(self.entry_date, XSDDate):
            self.entry_date = XSDDate(self.entry_date)

        self._normalize_inlined_as_list(slot_name="attack_patterns", slot_type=AttackPattern, key_name="id", keyed=True)

        self._normalize_inlined_as_list(slot_name="categories", slot_type=Category, key_name="id", keyed=True)

        self._normalize_inlined_as_list(slot_name="views", slot_type=View, key_name="id", keyed=True)

        self._normalize_inlined_as_list(slot_name="external_references", slot_type=ExternalReference, key_name="reference_id", keyed=True)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class AttackPattern(YAMLRoot):
    """
    An attack pattern is an abstraction mechanism for helping describe how an attack is
    executed. Each pattern defines a challenge that an attacker may face, provides a
    description of the common technique(s) used to meet the challenge, and presents
    recommended methods for mitigating an actual attack. Attack patterns help categorize
    attacks in a meaningful way in an effort to provide a coherent way of teaching
    designers and developers how their systems may be attacked and how they can effectively
    defend them.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CAPEC["AttackPattern"]
    class_class_curie: ClassVar[str] = "capec:AttackPattern"
    class_name: ClassVar[str] = "AttackPattern"
    class_model_uri: ClassVar[URIRef] = CAPEC.AttackPattern

    id: Union[int, AttackPatternId] = None
    name: str = None
    status: Union[str, "StatusEnum"] = None
    description: str = None
    abstraction: Union[str, "AbstractionEnum"] = None
    notes: Optional[Union[Union[dict, "Note"], list[Union[dict, "Note"]]]] = empty_list()
    content_history: Optional[Union[dict, "ContentHistory"]] = None
    references: Optional[Union[Union[dict, "Reference"], list[Union[dict, "Reference"]]]] = empty_list()
    taxonomy_mappings: Optional[Union[Union[dict, "TaxonomyMapping"], list[Union[dict, "TaxonomyMapping"]]]] = empty_list()
    extended_description: Optional[str] = None
    alternate_terms: Optional[Union[Union[dict, "AlternateTerm"], list[Union[dict, "AlternateTerm"]]]] = empty_list()
    likelihood_of_attack: Optional[Union[str, "LikelihoodEnum"]] = None
    typical_severity: Optional[Union[str, "SeverityEnum"]] = None
    related_attack_patterns: Optional[Union[Union[dict, "RelatedAttackPattern"], list[Union[dict, "RelatedAttackPattern"]]]] = empty_list()
    execution_flow: Optional[Union[Union[dict, "AttackStep"], list[Union[dict, "AttackStep"]]]] = empty_list()
    prerequisites: Optional[Union[str, list[str]]] = empty_list()
    skills_required: Optional[Union[Union[dict, "Skill"], list[Union[dict, "Skill"]]]] = empty_list()
    resources_required: Optional[Union[str, list[str]]] = empty_list()
    indicators: Optional[Union[str, list[str]]] = empty_list()
    consequences: Optional[Union[Union[dict, "Consequence"], list[Union[dict, "Consequence"]]]] = empty_list()
    mitigations: Optional[Union[str, list[str]]] = empty_list()
    example_instances: Optional[Union[str, list[str]]] = empty_list()
    related_weaknesses: Optional[Union[int, list[int]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, AttackPatternId):
            self.id = AttackPatternId(self.id)

        if self._is_empty(self.name):
            self.MissingRequiredField("name")
        if not isinstance(self.name, str):
            self.name = str(self.name)

        if self._is_empty(self.status):
            self.MissingRequiredField("status")
        if not isinstance(self.status, StatusEnum):
            self.status = StatusEnum(self.status)

        if self._is_empty(self.description):
            self.MissingRequiredField("description")
        if not isinstance(self.description, str):
            self.description = str(self.description)

        if self._is_empty(self.abstraction):
            self.MissingRequiredField("abstraction")
        if not isinstance(self.abstraction, AbstractionEnum):
            self.abstraction = AbstractionEnum(self.abstraction)

        self._normalize_inlined_as_list(slot_name="notes", slot_type=Note, key_name="type", keyed=False)

        if self.content_history is not None and not isinstance(self.content_history, ContentHistory):
            self.content_history = ContentHistory(**as_dict(self.content_history))

        self._normalize_inlined_as_list(slot_name="references", slot_type=Reference, key_name="external_reference_id", keyed=False)

        self._normalize_inlined_as_list(slot_name="taxonomy_mappings", slot_type=TaxonomyMapping, key_name="taxonomy_name", keyed=False)

        if self.extended_description is not None and not isinstance(self.extended_description, str):
            self.extended_description = str(self.extended_description)

        self._normalize_inlined_as_list(slot_name="alternate_terms", slot_type=AlternateTerm, key_name="term", keyed=False)

        if self.likelihood_of_attack is not None and not isinstance(self.likelihood_of_attack, LikelihoodEnum):
            self.likelihood_of_attack = LikelihoodEnum(self.likelihood_of_attack)

        if self.typical_severity is not None and not isinstance(self.typical_severity, SeverityEnum):
            self.typical_severity = SeverityEnum(self.typical_severity)

        self._normalize_inlined_as_list(slot_name="related_attack_patterns", slot_type=RelatedAttackPattern, key_name="capec_id", keyed=False)

        self._normalize_inlined_as_list(slot_name="execution_flow", slot_type=AttackStep, key_name="description", keyed=False)

        if not isinstance(self.prerequisites, list):
            self.prerequisites = [self.prerequisites] if self.prerequisites is not None else []
        self.prerequisites = [v if isinstance(v, str) else str(v) for v in self.prerequisites]

        self._normalize_inlined_as_list(slot_name="skills_required", slot_type=Skill, key_name="description", keyed=False)

        if not isinstance(self.resources_required, list):
            self.resources_required = [self.resources_required] if self.resources_required is not None else []
        self.resources_required = [v if isinstance(v, str) else str(v) for v in self.resources_required]

        if not isinstance(self.indicators, list):
            self.indicators = [self.indicators] if self.indicators is not None else []
        self.indicators = [v if isinstance(v, str) else str(v) for v in self.indicators]

        self._normalize_inlined_as_list(slot_name="consequences", slot_type=Consequence, key_name="scope", keyed=False)

        if not isinstance(self.mitigations, list):
            self.mitigations = [self.mitigations] if self.mitigations is not None else []
        self.mitigations = [v if isinstance(v, str) else str(v) for v in self.mitigations]

        if not isinstance(self.example_instances, list):
            self.example_instances = [self.example_instances] if self.example_instances is not None else []
        self.example_instances = [v if isinstance(v, str) else str(v) for v in self.example_instances]

        if not isinstance(self.related_weaknesses, list):
            self.related_weaknesses = [self.related_weaknesses] if self.related_weaknesses is not None else []
        self.related_weaknesses = [v if isinstance(v, int) else int(v) for v in self.related_weaknesses]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Category(YAMLRoot):
    """
    A category in CAPEC is a collection of attack patterns based on some common
    characteristic. More specifically, it is an aggregation of attack patterns based on
    effect/intent (as opposed to actions or mechanisms, which would be a meta attack
    pattern). An aggregation based on effect/intent is not an actionable attack and as
    such is not a pattern of attack behavior. Rather, it is a grouping of patterns based
    on some common criteria.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CAPEC["Category"]
    class_class_curie: ClassVar[str] = "capec:Category"
    class_name: ClassVar[str] = "Category"
    class_model_uri: ClassVar[URIRef] = CAPEC.Category

    id: Union[int, CategoryId] = None
    name: str = None
    status: Union[str, "StatusEnum"] = None
    summary: str = None
    notes: Optional[Union[Union[dict, "Note"], list[Union[dict, "Note"]]]] = empty_list()
    content_history: Optional[Union[dict, "ContentHistory"]] = None
    references: Optional[Union[Union[dict, "Reference"], list[Union[dict, "Reference"]]]] = empty_list()
    taxonomy_mappings: Optional[Union[Union[dict, "TaxonomyMapping"], list[Union[dict, "TaxonomyMapping"]]]] = empty_list()
    relationships: Optional[Union[dict, "Relationships"]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, CategoryId):
            self.id = CategoryId(self.id)

        if self._is_empty(self.name):
            self.MissingRequiredField("name")
        if not isinstance(self.name, str):
            self.name = str(self.name)

        if self._is_empty(self.status):
            self.MissingRequiredField("status")
        if not isinstance(self.status, StatusEnum):
            self.status = StatusEnum(self.status)

        if self._is_empty(self.summary):
            self.MissingRequiredField("summary")
        if not isinstance(self.summary, str):
            self.summary = str(self.summary)

        self._normalize_inlined_as_list(slot_name="notes", slot_type=Note, key_name="type", keyed=False)

        if self.content_history is not None and not isinstance(self.content_history, ContentHistory):
            self.content_history = ContentHistory(**as_dict(self.content_history))

        self._normalize_inlined_as_list(slot_name="references", slot_type=Reference, key_name="external_reference_id", keyed=False)

        self._normalize_inlined_as_list(slot_name="taxonomy_mappings", slot_type=TaxonomyMapping, key_name="taxonomy_name", keyed=False)

        if self.relationships is not None and not isinstance(self.relationships, Relationships):
            self.relationships = Relationships(**as_dict(self.relationships))

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class View(YAMLRoot):
    """
    A view in CAPEC represents a perspective with which one might look at the collection
    of attack patterns defined within CAPEC. There are three different types of views as
    defined by the Type attribute: graphs, explicit slices, and implicit slices.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CAPEC["View"]
    class_class_curie: ClassVar[str] = "capec:View"
    class_name: ClassVar[str] = "View"
    class_model_uri: ClassVar[URIRef] = CAPEC.View

    id: Union[int, ViewId] = None
    name: str = None
    status: Union[str, "StatusEnum"] = None
    type: Union[str, "ViewTypeEnum"] = None
    objective: str = None
    notes: Optional[Union[Union[dict, "Note"], list[Union[dict, "Note"]]]] = empty_list()
    content_history: Optional[Union[dict, "ContentHistory"]] = None
    references: Optional[Union[Union[dict, "Reference"], list[Union[dict, "Reference"]]]] = empty_list()
    audience: Optional[Union[Union[dict, "Stakeholder"], list[Union[dict, "Stakeholder"]]]] = empty_list()
    members: Optional[Union[dict, "Relationships"]] = None
    filter: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, ViewId):
            self.id = ViewId(self.id)

        if self._is_empty(self.name):
            self.MissingRequiredField("name")
        if not isinstance(self.name, str):
            self.name = str(self.name)

        if self._is_empty(self.status):
            self.MissingRequiredField("status")
        if not isinstance(self.status, StatusEnum):
            self.status = StatusEnum(self.status)

        if self._is_empty(self.type):
            self.MissingRequiredField("type")
        if not isinstance(self.type, ViewTypeEnum):
            self.type = ViewTypeEnum(self.type)

        if self._is_empty(self.objective):
            self.MissingRequiredField("objective")
        if not isinstance(self.objective, str):
            self.objective = str(self.objective)

        self._normalize_inlined_as_list(slot_name="notes", slot_type=Note, key_name="type", keyed=False)

        if self.content_history is not None and not isinstance(self.content_history, ContentHistory):
            self.content_history = ContentHistory(**as_dict(self.content_history))

        self._normalize_inlined_as_list(slot_name="references", slot_type=Reference, key_name="external_reference_id", keyed=False)

        self._normalize_inlined_as_list(slot_name="audience", slot_type=Stakeholder, key_name="type", keyed=False)

        if self.members is not None and not isinstance(self.members, Relationships):
            self.members = Relationships(**as_dict(self.members))

        if self.filter is not None and not isinstance(self.filter, str):
            self.filter = str(self.filter)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class ExternalReference(YAMLRoot):
    """
    An external reference provides a pointer to where more information and deeper insight
    can be obtained about an attack pattern, category, or view. Examples include research
    papers and excerpts from publications. Not all elements need to be used since some are
    designed for web references and others for book references.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CAPEC["ExternalReference"]
    class_class_curie: ClassVar[str] = "capec:ExternalReference"
    class_name: ClassVar[str] = "ExternalReference"
    class_model_uri: ClassVar[URIRef] = CAPEC.ExternalReference

    reference_id: Union[str, ExternalReferenceReferenceId] = None
    title: str = None
    authors: Optional[Union[str, list[str]]] = empty_list()
    edition: Optional[str] = None
    publication: Optional[str] = None
    publication_year: Optional[str] = None
    publication_month: Optional[str] = None
    publication_day: Optional[str] = None
    publisher: Optional[str] = None
    url: Optional[str] = None
    url_date: Optional[Union[str, XSDDate]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.reference_id):
            self.MissingRequiredField("reference_id")
        if not isinstance(self.reference_id, ExternalReferenceReferenceId):
            self.reference_id = ExternalReferenceReferenceId(self.reference_id)

        if self._is_empty(self.title):
            self.MissingRequiredField("title")
        if not isinstance(self.title, str):
            self.title = str(self.title)

        if not isinstance(self.authors, list):
            self.authors = [self.authors] if self.authors is not None else []
        self.authors = [v if isinstance(v, str) else str(v) for v in self.authors]

        if self.edition is not None and not isinstance(self.edition, str):
            self.edition = str(self.edition)

        if self.publication is not None and not isinstance(self.publication, str):
            self.publication = str(self.publication)

        if self.publication_year is not None and not isinstance(self.publication_year, str):
            self.publication_year = str(self.publication_year)

        if self.publication_month is not None and not isinstance(self.publication_month, str):
            self.publication_month = str(self.publication_month)

        if self.publication_day is not None and not isinstance(self.publication_day, str):
            self.publication_day = str(self.publication_day)

        if self.publisher is not None and not isinstance(self.publisher, str):
            self.publisher = str(self.publisher)

        if self.url is not None and not isinstance(self.url, str):
            self.url = str(self.url)

        if self.url_date is not None and not isinstance(self.url_date, XSDDate):
            self.url_date = XSDDate(self.url_date)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class AlternateTerm(YAMLRoot):
    """
    Another name or term used to describe an attack pattern. Provides context for the alternate term by which the
    attack pattern may be known.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CAPEC["AlternateTerm"]
    class_class_curie: ClassVar[str] = "capec:AlternateTerm"
    class_name: ClassVar[str] = "AlternateTerm"
    class_model_uri: ClassVar[URIRef] = CAPEC.AlternateTerm

    term: str = None
    description: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.term):
            self.MissingRequiredField("term")
        if not isinstance(self.term, str):
            self.term = str(self.term)

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Consequence(YAMLRoot):
    """
    An individual consequence associated with an attack pattern, specifying which
    security properties are violated, the technical impact that arises if an adversary
    succeeds, the likelihood of this specific consequence occurring, and any additional
    commentary.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CAPEC["Consequence"]
    class_class_curie: ClassVar[str] = "capec:Consequence"
    class_name: ClassVar[str] = "Consequence"
    class_model_uri: ClassVar[URIRef] = CAPEC.Consequence

    scope: Union[Union[str, "ScopeEnum"], list[Union[str, "ScopeEnum"]]] = None
    consequence_id: Optional[str] = None
    impact: Optional[Union[Union[str, "TechnicalImpactEnum"], list[Union[str, "TechnicalImpactEnum"]]]] = empty_list()
    likelihood: Optional[Union[str, "LikelihoodEnum"]] = None
    note: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.scope):
            self.MissingRequiredField("scope")
        if not isinstance(self.scope, list):
            self.scope = [self.scope] if self.scope is not None else []
        self.scope = [v if isinstance(v, ScopeEnum) else ScopeEnum(v) for v in self.scope]

        if self.consequence_id is not None and not isinstance(self.consequence_id, str):
            self.consequence_id = str(self.consequence_id)

        if not isinstance(self.impact, list):
            self.impact = [self.impact] if self.impact is not None else []
        self.impact = [v if isinstance(v, TechnicalImpactEnum) else TechnicalImpactEnum(v) for v in self.impact]

        if self.likelihood is not None and not isinstance(self.likelihood, LikelihoodEnum):
            self.likelihood = LikelihoodEnum(self.likelihood)

        if self.note is not None and not isinstance(self.note, str):
            self.note = str(self.note)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Skill(YAMLRoot):
    """
    A description of the level of skills or specific knowledge needed by an adversary to execute this type of attack.
    Each skill entry captures both the skill level and a textual description of the knowledge required.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CAPEC["Skill"]
    class_class_curie: ClassVar[str] = "capec:Skill"
    class_name: ClassVar[str] = "Skill"
    class_model_uri: ClassVar[URIRef] = CAPEC.Skill

    description: str = None
    level: Union[str, "SkillLevelEnum"] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.description):
            self.MissingRequiredField("description")
        if not isinstance(self.description, str):
            self.description = str(self.description)

        if self._is_empty(self.level):
            self.MissingRequiredField("level")
        if not isinstance(self.level, SkillLevelEnum):
            self.level = SkillLevelEnum(self.level)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Note(YAMLRoot):
    """
    An additional comment about a CAPEC entry that cannot be captured using the other available elements. Each note
    has a type indicating its purpose and contains content describing the note.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CAPEC["Note"]
    class_class_curie: ClassVar[str] = "capec:Note"
    class_name: ClassVar[str] = "Note"
    class_model_uri: ClassVar[URIRef] = CAPEC.Note

    type: Union[str, "NoteTypeEnum"] = None
    content: str = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.type):
            self.MissingRequiredField("type")
        if not isinstance(self.type, NoteTypeEnum):
            self.type = NoteTypeEnum(self.type)

        if self._is_empty(self.content):
            self.MissingRequiredField("content")
        if not isinstance(self.content, str):
            self.content = str(self.content)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class AttackStep(YAMLRoot):
    """
    An individual step in the execution flow of an attack pattern. Provides a detailed
    description of a specific action typically performed by an adversary during the
    attack, along with the phase of the attack it belongs to and any specific techniques
    used.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CAPEC["AttackStep"]
    class_class_curie: ClassVar[str] = "capec:AttackStep"
    class_name: ClassVar[str] = "AttackStep"
    class_model_uri: ClassVar[URIRef] = CAPEC.AttackStep

    description: str = None
    step: int = None
    phase: Union[str, "AttackStepPhaseEnum"] = None
    techniques: Optional[Union[Union[dict, "Technique"], list[Union[dict, "Technique"]]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.description):
            self.MissingRequiredField("description")
        if not isinstance(self.description, str):
            self.description = str(self.description)

        if self._is_empty(self.step):
            self.MissingRequiredField("step")
        if not isinstance(self.step, int):
            self.step = int(self.step)

        if self._is_empty(self.phase):
            self.MissingRequiredField("phase")
        if not isinstance(self.phase, AttackStepPhaseEnum):
            self.phase = AttackStepPhaseEnum(self.phase)

        self._normalize_inlined_as_list(slot_name="techniques", slot_type=Technique, key_name="description", keyed=False)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Technique(YAMLRoot):
    """
    A specific technique used by an adversary during an attack step. Extends the structured text description with an
    optional reference to a related CAPEC entry.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CAPEC["Technique"]
    class_class_curie: ClassVar[str] = "capec:Technique"
    class_name: ClassVar[str] = "Technique"
    class_model_uri: ClassVar[URIRef] = CAPEC.Technique

    description: str = None
    capec_id: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.description):
            self.MissingRequiredField("description")
        if not isinstance(self.description, str):
            self.description = str(self.description)

        if self.capec_id is not None and not isinstance(self.capec_id, str):
            self.capec_id = str(self.capec_id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class RelatedAttackPattern(YAMLRoot):
    """
    A reference to another attack pattern that provides insight to similar items at
    higher or lower levels of abstraction, or items that are part of a chaining or
    peer relationship. Special cases may require Exclude_Related elements to capture
    ancestor IDs for which this relationship is not applicable.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CAPEC["RelatedAttackPattern"]
    class_class_curie: ClassVar[str] = "capec:RelatedAttackPattern"
    class_name: ClassVar[str] = "RelatedAttackPattern"
    class_model_uri: ClassVar[URIRef] = CAPEC.RelatedAttackPattern

    capec_id: int = None
    nature: Union[str, "RelatedNatureEnum"] = None
    exclude_related: Optional[Union[Union[dict, "ExcludeRelated"], list[Union[dict, "ExcludeRelated"]]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.capec_id):
            self.MissingRequiredField("capec_id")
        if not isinstance(self.capec_id, int):
            self.capec_id = int(self.capec_id)

        if self._is_empty(self.nature):
            self.MissingRequiredField("nature")
        if not isinstance(self.nature, RelatedNatureEnum):
            self.nature = RelatedNatureEnum(self.nature)

        self._normalize_inlined_as_list(slot_name="exclude_related", slot_type=ExcludeRelated, key_name="exclude_id", keyed=False)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class ExcludeRelated(YAMLRoot):
    """
    Captures the CAPEC identifier of an ancestor for which a given relationship is
    not applicable. Used in special cases within RelatedAttackPattern and relationship
    entries.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CAPEC["ExcludeRelated"]
    class_class_curie: ClassVar[str] = "capec:ExcludeRelated"
    class_name: ClassVar[str] = "ExcludeRelated"
    class_model_uri: ClassVar[URIRef] = CAPEC.ExcludeRelated

    exclude_id: int = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.exclude_id):
            self.MissingRequiredField("exclude_id")
        if not isinstance(self.exclude_id, int):
            self.exclude_id = int(self.exclude_id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class RelatedWeakness(YAMLRoot):
    """
    A reference to a CWE (Common Weakness Enumeration) weakness associated with an
    attack pattern. The association implies a weakness that must exist for a given
    attack to be successful. If multiple weaknesses are listed, any of them (but not
    necessarily all) may be present for the attack to succeed.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CAPEC["RelatedWeakness"]
    class_class_curie: ClassVar[str] = "capec:RelatedWeakness"
    class_name: ClassVar[str] = "RelatedWeakness"
    class_model_uri: ClassVar[URIRef] = CAPEC.RelatedWeakness

    cwe_id: int = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.cwe_id):
            self.MissingRequiredField("cwe_id")
        if not isinstance(self.cwe_id, int):
            self.cwe_id = int(self.cwe_id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Relationships(YAMLRoot):
    """
    A container for relationships associated with a category or view, showing
    Member_Of relationships with views or categories and Has_Member relationships
    with attack patterns or categories.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CAPEC["Relationships"]
    class_class_curie: ClassVar[str] = "capec:Relationships"
    class_name: ClassVar[str] = "Relationships"
    class_model_uri: ClassVar[URIRef] = CAPEC.Relationships

    member_of: Optional[Union[Union[dict, "MemberOf"], list[Union[dict, "MemberOf"]]]] = empty_list()
    has_member: Optional[Union[Union[dict, "HasMember"], list[Union[dict, "HasMember"]]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        self._normalize_inlined_as_list(slot_name="member_of", slot_type=MemberOf, key_name="capec_id", keyed=False)

        self._normalize_inlined_as_list(slot_name="has_member", slot_type=HasMember, key_name="capec_id", keyed=False)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class MemberOf(YAMLRoot):
    """
    Represents a Member_Of relationship indicating that the parent category or view
    is a member of the specified view or parent category.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CAPEC["MemberOf"]
    class_class_curie: ClassVar[str] = "capec:MemberOf"
    class_name: ClassVar[str] = "MemberOf"
    class_model_uri: ClassVar[URIRef] = CAPEC.MemberOf

    capec_id: int = None
    exclude_related: Optional[Union[Union[dict, ExcludeRelated], list[Union[dict, ExcludeRelated]]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.capec_id):
            self.MissingRequiredField("capec_id")
        if not isinstance(self.capec_id, int):
            self.capec_id = int(self.capec_id)

        self._normalize_inlined_as_list(slot_name="exclude_related", slot_type=ExcludeRelated, key_name="exclude_id", keyed=False)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class HasMember(YAMLRoot):
    """
    Represents a Has_Member relationship indicating that the parent category or view
    contains the specified attack pattern or category as a member.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CAPEC["HasMember"]
    class_class_curie: ClassVar[str] = "capec:HasMember"
    class_name: ClassVar[str] = "HasMember"
    class_model_uri: ClassVar[URIRef] = CAPEC.HasMember

    capec_id: int = None
    exclude_related: Optional[Union[Union[dict, ExcludeRelated], list[Union[dict, ExcludeRelated]]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.capec_id):
            self.MissingRequiredField("capec_id")
        if not isinstance(self.capec_id, int):
            self.capec_id = int(self.capec_id)

        self._normalize_inlined_as_list(slot_name="exclude_related", slot_type=ExcludeRelated, key_name="exclude_id", keyed=False)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Reference(YAMLRoot):
    """
    A link from a CAPEC entry to an external reference defined within the catalog.
    The External_Reference_ID identifies which external reference is being cited.
    An optional Section captures a specific section title or page number relevant
    to this use of the reference.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CAPEC["Reference"]
    class_class_curie: ClassVar[str] = "capec:Reference"
    class_name: ClassVar[str] = "Reference"
    class_model_uri: ClassVar[URIRef] = CAPEC.Reference

    external_reference_id: str = None
    section: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.external_reference_id):
            self.MissingRequiredField("external_reference_id")
        if not isinstance(self.external_reference_id, str):
            self.external_reference_id = str(self.external_reference_id)

        if self.section is not None and not isinstance(self.section, str):
            self.section = str(self.section)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class TaxonomyMapping(YAMLRoot):
    """
    A mapping from a CAPEC entry (AttackPattern or Category) to an equivalent or related
    entry in a different security taxonomy. Identifies the external taxonomy, the ID and
    name of the external entry, and how closely the CAPEC entry aligns with it.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CAPEC["TaxonomyMapping"]
    class_class_curie: ClassVar[str] = "capec:TaxonomyMapping"
    class_name: ClassVar[str] = "TaxonomyMapping"
    class_model_uri: ClassVar[URIRef] = CAPEC.TaxonomyMapping

    taxonomy_name: Union[str, "TaxonomyNameEnum"] = None
    entry_id: Optional[str] = None
    entry_name: Optional[str] = None
    mapping_fit: Optional[Union[str, "TaxonomyMappingFitEnum"]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.taxonomy_name):
            self.MissingRequiredField("taxonomy_name")
        if not isinstance(self.taxonomy_name, TaxonomyNameEnum):
            self.taxonomy_name = TaxonomyNameEnum(self.taxonomy_name)

        if self.entry_id is not None and not isinstance(self.entry_id, str):
            self.entry_id = str(self.entry_id)

        if self.entry_name is not None and not isinstance(self.entry_name, str):
            self.entry_name = str(self.entry_name)

        if self.mapping_fit is not None and not isinstance(self.mapping_fit, TaxonomyMappingFitEnum):
            self.mapping_fit = TaxonomyMappingFitEnum(self.mapping_fit)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Stakeholder(YAMLRoot):
    """
    A target stakeholder or group for whom a CAPEC view is relevant. Specifies
    the type of stakeholder and describes which properties of the view they may
    find useful.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CAPEC["Stakeholder"]
    class_class_curie: ClassVar[str] = "capec:Stakeholder"
    class_name: ClassVar[str] = "Stakeholder"
    class_model_uri: ClassVar[URIRef] = CAPEC.Stakeholder

    type: Union[str, "StakeholderEnum"] = None
    description: str = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.type):
            self.MissingRequiredField("type")
        if not isinstance(self.type, StakeholderEnum):
            self.type = StakeholderEnum(self.type)

        if self._is_empty(self.description):
            self.MissingRequiredField("description")
        if not isinstance(self.description, str):
            self.description = str(self.description)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class ContentHistory(YAMLRoot):
    """
    Tracks the original author of a CAPEC entry and any subsequent modifications
    to the content. Provides a means of contacting authors and modifiers for
    clarifying ambiguities, merging overlapping contributions, etc.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CAPEC["ContentHistory"]
    class_class_curie: ClassVar[str] = "capec:ContentHistory"
    class_name: ClassVar[str] = "ContentHistory"
    class_model_uri: ClassVar[URIRef] = CAPEC.ContentHistory

    submission: Optional[Union[dict, "Submission"]] = None
    modifications: Optional[Union[Union[dict, "Modification"], list[Union[dict, "Modification"]]]] = empty_list()
    contributions: Optional[Union[Union[dict, "Contribution"], list[Union[dict, "Contribution"]]]] = empty_list()
    previous_entry_names: Optional[Union[Union[dict, "PreviousEntryName"], list[Union[dict, "PreviousEntryName"]]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.submission is not None and not isinstance(self.submission, Submission):
            self.submission = Submission(**as_dict(self.submission))

        if not isinstance(self.modifications, list):
            self.modifications = [self.modifications] if self.modifications is not None else []
        self.modifications = [v if isinstance(v, Modification) else Modification(**as_dict(v)) for v in self.modifications]

        self._normalize_inlined_as_list(slot_name="contributions", slot_type=Contribution, key_name="type", keyed=False)

        self._normalize_inlined_as_list(slot_name="previous_entry_names", slot_type=PreviousEntryName, key_name="name", keyed=False)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Submission(YAMLRoot):
    """
    Information about the original submission of a CAPEC entry, identifying the
    submitter, their organization, the date of submission, and any related comments.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CAPEC["Submission"]
    class_class_curie: ClassVar[str] = "capec:Submission"
    class_name: ClassVar[str] = "Submission"
    class_model_uri: ClassVar[URIRef] = CAPEC.Submission

    submission_name: Optional[str] = None
    submission_organization: Optional[str] = None
    submission_date: Optional[Union[str, XSDDate]] = None
    submission_comment: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.submission_name is not None and not isinstance(self.submission_name, str):
            self.submission_name = str(self.submission_name)

        if self.submission_organization is not None and not isinstance(self.submission_organization, str):
            self.submission_organization = str(self.submission_organization)

        if self.submission_date is not None and not isinstance(self.submission_date, XSDDate):
            self.submission_date = XSDDate(self.submission_date)

        if self.submission_comment is not None and not isinstance(self.submission_comment, str):
            self.submission_comment = str(self.submission_comment)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Modification(YAMLRoot):
    """
    A record of a modification made to a CAPEC entry, identifying the modifier,
    their organization, the date of modification, the importance of the change,
    and any related comments. Modifications that change the meaning of the entry
    should be marked as Critical importance.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CAPEC["Modification"]
    class_class_curie: ClassVar[str] = "capec:Modification"
    class_name: ClassVar[str] = "Modification"
    class_model_uri: ClassVar[URIRef] = CAPEC.Modification

    modification_name: Optional[str] = None
    modification_organization: Optional[str] = None
    modification_date: Optional[Union[str, XSDDate]] = None
    modification_importance: Optional[Union[str, "ImportanceEnum"]] = None
    modification_comment: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.modification_name is not None and not isinstance(self.modification_name, str):
            self.modification_name = str(self.modification_name)

        if self.modification_organization is not None and not isinstance(self.modification_organization, str):
            self.modification_organization = str(self.modification_organization)

        if self.modification_date is not None and not isinstance(self.modification_date, XSDDate):
            self.modification_date = XSDDate(self.modification_date)

        if self.modification_importance is not None and not isinstance(self.modification_importance, ImportanceEnum):
            self.modification_importance = ImportanceEnum(self.modification_importance)

        if self.modification_comment is not None and not isinstance(self.modification_comment, str):
            self.modification_comment = str(self.modification_comment)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Contribution(YAMLRoot):
    """
    A record of a contribution made to a CAPEC entry, identifying the contributor,
    their organization, the date of contribution, the type of contribution (Content
    or Feedback), and any related comments.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CAPEC["Contribution"]
    class_class_curie: ClassVar[str] = "capec:Contribution"
    class_name: ClassVar[str] = "Contribution"
    class_model_uri: ClassVar[URIRef] = CAPEC.Contribution

    type: Union[str, "ContributionTypeEnum"] = None
    contribution_name: Optional[str] = None
    contribution_organization: Optional[str] = None
    contribution_date: Optional[Union[str, XSDDate]] = None
    contribution_comment: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.type):
            self.MissingRequiredField("type")
        if not isinstance(self.type, ContributionTypeEnum):
            self.type = ContributionTypeEnum(self.type)

        if self.contribution_name is not None and not isinstance(self.contribution_name, str):
            self.contribution_name = str(self.contribution_name)

        if self.contribution_organization is not None and not isinstance(self.contribution_organization, str):
            self.contribution_organization = str(self.contribution_organization)

        if self.contribution_date is not None and not isinstance(self.contribution_date, XSDDate):
            self.contribution_date = XSDDate(self.contribution_date)

        if self.contribution_comment is not None and not isinstance(self.contribution_comment, str):
            self.contribution_comment = str(self.contribution_comment)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class PreviousEntryName(YAMLRoot):
    """
    A previous name that was used for a CAPEC entry before a substantive name change.
    Should align with a corresponding Modification element that records the change.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CAPEC["PreviousEntryName"]
    class_class_curie: ClassVar[str] = "capec:PreviousEntryName"
    class_name: ClassVar[str] = "PreviousEntryName"
    class_model_uri: ClassVar[URIRef] = CAPEC.PreviousEntryName

    name: str = None
    entry_date: Union[str, XSDDate] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.name):
            self.MissingRequiredField("name")
        if not isinstance(self.name, str):
            self.name = str(self.name)

        if self._is_empty(self.entry_date):
            self.MissingRequiredField("entry_date")
        if not isinstance(self.entry_date, XSDDate):
            self.entry_date = XSDDate(self.entry_date)

        super().__post_init__(**kwargs)


# Enumerations
class AbstractionEnum(EnumDefinitionImpl):
    """
    The different abstraction levels that apply to an attack pattern. A Meta level
    attack pattern is a decidedly abstract characterization of a specific methodology
    or technique used in an attack. A Standard level attack pattern is focused on a
    specific methodology or technique. A Detailed level attack pattern provides a low
    level of detail, typically leveraging a specific technique and targeting a specific
    technology, and expresses a complete execution flow.
    """
    Meta = PermissibleValue(
        text="Meta",
        description="""A Meta level attack pattern in CAPEC is a decidedly abstract characterization
of a specific methodology or technique used in an attack. A Meta attack pattern
is often void of a specific technology or implementation and is meant to provide
an understanding of a high level approach. A Meta level attack pattern is a
generalization of related group of standard level attack patterns. Meta level
attack patterns are particularly useful for architecture and design level threat
modeling exercises.""")
    Standard = PermissibleValue(
        text="Standard",
        description="""A Standard level attack pattern in CAPEC is focused on a specific methodology
or technique used in an attack. It is often seen as a singular piece of a fully
executed attack. A Standard attack pattern is meant to provide sufficient details
to understand the specific technique and how it attempts to accomplish a desired
goal. A Standard level attack pattern is a specific type of a more abstract meta
level attack pattern.""")
    Detailed = PermissibleValue(
        text="Detailed",
        description="""A Detailed level attack pattern in CAPEC provides a low level of detail, typically
leveraging a specific technique and targeting a specific technology, and expresses
a complete execution flow. Detailed attack patterns are more specific than meta and
standard attack patterns and often require a specific protection mechanism to mitigate
actual attacks. A Detailed level attack pattern often will leverage a number of
different standard level attack patterns chained together to accomplish a goal.""")

    _defn = EnumDefinition(
        name="AbstractionEnum",
        description="""The different abstraction levels that apply to an attack pattern. A Meta level
attack pattern is a decidedly abstract characterization of a specific methodology
or technique used in an attack. A Standard level attack pattern is focused on a
specific methodology or technique. A Detailed level attack pattern provides a low
level of detail, typically leveraging a specific technique and targeting a specific
technology, and expresses a complete execution flow.""",
    )

class AttackStepPhaseEnum(EnumDefinitionImpl):
    """
    The different phases of an individual attack step within the execution flow.
    """
    Explore = PermissibleValue(
        text="Explore",
        description="The exploration or reconnaissance phase of the attack.")
    Experiment = PermissibleValue(
        text="Experiment",
        description="The experimentation or testing phase of the attack.")
    Exploit = PermissibleValue(
        text="Exploit",
        description="The exploitation phase of the attack where intent is realized.")

    _defn = EnumDefinition(
        name="AttackStepPhaseEnum",
        description="The different phases of an individual attack step within the execution flow.",
    )

class ContributionTypeEnum(EnumDefinitionImpl):
    """
    The type of contribution made to a CAPEC entry.
    """
    Content = PermissibleValue(
        text="Content",
        description="The contribution consisted of actual content donated to the entry.")
    Feedback = PermissibleValue(
        text="Feedback",
        description="The contribution consisted of general feedback about the entry.")

    _defn = EnumDefinition(
        name="ContributionTypeEnum",
        description="The type of contribution made to a CAPEC entry.",
    )

class ImportanceEnum(EnumDefinitionImpl):
    """
    Different values for the importance of a modification to CAPEC content.
    """
    Normal = PermissibleValue(
        text="Normal",
        description="Normal importance modification that does not significantly alter meaning.")
    Critical = PermissibleValue(
        text="Critical",
        description="""Critical importance modification that changes the meaning of the entry, or how it might be interpreted, bringing it to the attention of anyone previously dependent on the attack pattern.""")

    _defn = EnumDefinition(
        name="ImportanceEnum",
        description="Different values for the importance of a modification to CAPEC content.",
    )

class LikelihoodEnum(EnumDefinitionImpl):
    """
    Values corresponding to different likelihoods. The value Unknown should be used
    when the actual likelihood of something occurring is not known.
    """
    High = PermissibleValue(
        text="High",
        description="High likelihood.")
    Medium = PermissibleValue(
        text="Medium",
        description="Medium likelihood.")
    Low = PermissibleValue(
        text="Low",
        description="Low likelihood.")
    Unknown = PermissibleValue(
        text="Unknown",
        description="The likelihood is unknown.")

    _defn = EnumDefinition(
        name="LikelihoodEnum",
        description="""Values corresponding to different likelihoods. The value Unknown should be used
when the actual likelihood of something occurring is not known.""",
    )

class NoteTypeEnum(EnumDefinitionImpl):
    """
    The different types of notes that can be associated with an attack pattern.
    A Maintenance note contains significant maintenance tasks within this entry that
    still need to be addressed, such as clarifying the concepts involved or improving
    relationships. A Relationship note provides clarifying details regarding the
    relationships between entities. A Research Gap note identifies potential opportunities
    for the research community to conduct further exploration. A Terminology note contains
    a discussion of terminology issues related to this attack pattern.
    """
    Maintenance = PermissibleValue(
        text="Maintenance",
        description="""Contains significant maintenance tasks within this entry that still need to be
addressed, such as clarifying the concepts involved or improving relationships.""")
    Relationship = PermissibleValue(
        text="Relationship",
        description="Provides clarifying details regarding the relationships between entities.")
    Terminology = PermissibleValue(
        text="Terminology",
        description="""Contains a discussion of terminology issues related to this attack pattern,
or clarifications when there is no established terminology, or if there are
multiple uses of the same key term.""")
    Other = PermissibleValue(
        text="Other",
        description="Other note type not covered by the defined categories.")

    _defn = EnumDefinition(
        name="NoteTypeEnum",
        description="""The different types of notes that can be associated with an attack pattern.
A Maintenance note contains significant maintenance tasks within this entry that
still need to be addressed, such as clarifying the concepts involved or improving
relationships. A Relationship note provides clarifying details regarding the
relationships between entities. A Research Gap note identifies potential opportunities
for the research community to conduct further exploration. A Terminology note contains
a discussion of terminology issues related to this attack pattern.""",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "Research Gap",
            PermissibleValue(
                text="Research Gap",
                description="""Identifies potential opportunities for the research community to conduct further
exploration of issues related to this attack pattern."""))

class RelatedNatureEnum(EnumDefinitionImpl):
    """
    The different values that can be used to define the nature of a related attack
    pattern. A ChildOf nature denotes a related attack pattern as a higher level of
    abstraction. A ParentOf nature denotes a related attack pattern as a lower level
    of abstraction. The CanPrecede and CanFollow relationships are used to denote
    attack patterns that are part of a chaining structure. The CanAlsoBe relationship
    denotes an attack pattern that, in the proper environment and context, can also be
    perceived as the target attack pattern. Note that the CanAlsoBe relationship is not
    necessarily reciprocal. The PeerOf relationship is used to show some similarity
    with the target attack pattern which does not fit any of the other types.
    """
    ChildOf = PermissibleValue(
        text="ChildOf",
        description="""Denotes a related attack pattern at a higher level of abstraction; the current pattern is a specialization of the related pattern.""")
    ParentOf = PermissibleValue(
        text="ParentOf",
        description="""Denotes a related attack pattern at a lower level of abstraction; the current pattern is a generalization of the related pattern.""")
    CanFollow = PermissibleValue(
        text="CanFollow",
        description="""Denotes an attack pattern that can follow (come after) the current pattern in a chaining structure.""")
    CanPrecede = PermissibleValue(
        text="CanPrecede",
        description="""Denotes an attack pattern that can precede (come before) the current pattern in a chaining structure.""")
    CanAlsoBe = PermissibleValue(
        text="CanAlsoBe",
        description="""Denotes an attack pattern that, in the proper environment and context, can also
be perceived as the target attack pattern. Note that the CanAlsoBe relationship
is not necessarily reciprocal.""")
    PeerOf = PermissibleValue(
        text="PeerOf",
        description="""Used to show some similarity with the target attack pattern which does not fit
any of the other types of relationships.""")

    _defn = EnumDefinition(
        name="RelatedNatureEnum",
        description="""The different values that can be used to define the nature of a related attack
pattern. A ChildOf nature denotes a related attack pattern as a higher level of
abstraction. A ParentOf nature denotes a related attack pattern as a lower level
of abstraction. The CanPrecede and CanFollow relationships are used to denote
attack patterns that are part of a chaining structure. The CanAlsoBe relationship
denotes an attack pattern that, in the proper environment and context, can also be
perceived as the target attack pattern. Note that the CanAlsoBe relationship is not
necessarily reciprocal. The PeerOf relationship is used to show some similarity
with the target attack pattern which does not fit any of the other types.""",
    )

class ScopeEnum(EnumDefinitionImpl):
    """
    The different areas of software security that can be affected by exploiting a weakness.
    """
    Confidentiality = PermissibleValue(
        text="Confidentiality",
        description="The confidentiality security property is violated.")
    Integrity = PermissibleValue(
        text="Integrity",
        description="The integrity security property is violated.")
    Availability = PermissibleValue(
        text="Availability",
        description="The availability security property is violated.")
    Accountability = PermissibleValue(
        text="Accountability",
        description="The accountability security property is violated.")
    Authentication = PermissibleValue(
        text="Authentication",
        description="The authentication security property is violated.")
    Authorization = PermissibleValue(
        text="Authorization",
        description="The authorization security property is violated.")
    Other = PermissibleValue(
        text="Other",
        description="Other security property not covered by the defined categories.")

    _defn = EnumDefinition(
        name="ScopeEnum",
        description="The different areas of software security that can be affected by exploiting a weakness.",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "Access Control",
            PermissibleValue(
                text="Access Control",
                description="The access control security property is violated."))
        setattr(cls, "Non-Repudiation",
            PermissibleValue(
                text="Non-Repudiation",
                description="The non-repudiation security property is violated."))

class SeverityEnum(EnumDefinitionImpl):
    """
    Values corresponding to different severities of attack impact.
    """
    High = PermissibleValue(
        text="High",
        description="High severity impact.")
    Medium = PermissibleValue(
        text="Medium",
        description="Medium severity impact.")
    Low = PermissibleValue(
        text="Low",
        description="Low severity impact.")

    _defn = EnumDefinition(
        name="SeverityEnum",
        description="Values corresponding to different severities of attack impact.",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "Very High",
            PermissibleValue(
                text="Very High",
                description="Very high severity impact."))
        setattr(cls, "Very Low",
            PermissibleValue(
                text="Very Low",
                description="Very low severity impact."))

class SkillLevelEnum(EnumDefinitionImpl):
    """
    Values corresponding to different knowledge levels required to perform an attack.
    The value Unknown should be used when the actual skill level is not known.
    """
    High = PermissibleValue(
        text="High",
        description="High skill level required to perform the attack.")
    Medium = PermissibleValue(
        text="Medium",
        description="Medium skill level required to perform the attack.")
    Low = PermissibleValue(
        text="Low",
        description="Low skill level required to perform the attack.")
    Unknown = PermissibleValue(
        text="Unknown",
        description="The skill level required to perform the attack is unknown.")

    _defn = EnumDefinition(
        name="SkillLevelEnum",
        description="""Values corresponding to different knowledge levels required to perform an attack.
The value Unknown should be used when the actual skill level is not known.""",
    )

class StakeholderEnum(EnumDefinitionImpl):
    """
    The different types of users and stakeholder groups within the CAPEC community.
    """
    Educators = PermissibleValue(
        text="Educators",
        description="Educators teaching courses on cybersecurity concepts using CAPEC.")
    Other = PermissibleValue(
        text="Other",
        description="Other stakeholder type not covered by the defined categories.")

    _defn = EnumDefinition(
        name="StakeholderEnum",
        description="The different types of users and stakeholder groups within the CAPEC community.",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "Academic Researchers",
            PermissibleValue(
                text="Academic Researchers",
                description="Academic researchers studying attack patterns and cybersecurity."))
        setattr(cls, "Applied Researchers",
            PermissibleValue(
                text="Applied Researchers",
                description="Applied researchers using CAPEC for practical security analysis."))
        setattr(cls, "Assessment Customers",
            PermissibleValue(
                text="Assessment Customers",
                description="Customers who commission security assessments and penetration tests."))
        setattr(cls, "Assessment Vendors",
            PermissibleValue(
                text="Assessment Vendors",
                description="Vendors and consultants who provide security assessment services."))
        setattr(cls, "CAPEC Team",
            PermissibleValue(
                text="CAPEC Team",
                description="The core CAPEC development and maintenance team at MITRE."))
        setattr(cls, "Information Providers",
            PermissibleValue(
                text="Information Providers",
                description="Organizations or individuals who provide cybersecurity information services."))
        setattr(cls, "Software Customers",
            PermissibleValue(
                text="Software Customers",
                description="End users and customers of software products concerned about security."))
        setattr(cls, "Software Designers",
            PermissibleValue(
                text="Software Designers",
                description="Software architects and designers involved in secure system design."))
        setattr(cls, "Software Developers",
            PermissibleValue(
                text="Software Developers",
                description="Software developers building and maintaining secure software."))
        setattr(cls, "Software Vendors",
            PermissibleValue(
                text="Software Vendors",
                description="Vendors who produce and distribute software products."))

class StatusEnum(EnumDefinitionImpl):
    """
    The different status values that an entity (view, category, or attack pattern) can have.
    """
    Deprecated = PermissibleValue(
        text="Deprecated",
        description="""The entry has been deprecated and should not be used. A placeholder for the deprecated entry is left in the catalog and the identifier is not reused.""")
    Draft = PermissibleValue(
        text="Draft",
        description="""The entry is a draft and its content may change significantly through future revisions as it is reviewed and refined by the community.""")
    Incomplete = PermissibleValue(
        text="Incomplete",
        description="""The entry exists and is partially filled in, but it does not yet meet the quality bar established for Usable entries.""")
    Obsolete = PermissibleValue(
        text="Obsolete",
        description="""The entry is obsolete and is no longer recommended for use but has not been formally deprecated.""")
    Stable = PermissibleValue(
        text="Stable",
        description="""The entry is stable and unlikely to undergo significant changes unless new information or research warrants it.""")
    Usable = PermissibleValue(
        text="Usable",
        description="""The entry is complete enough to be used in product documentation, assessments, tools, and mapping exercises without significant risk.""")

    _defn = EnumDefinition(
        name="StatusEnum",
        description="The different status values that an entity (view, category, or attack pattern) can have.",
    )

class TaxonomyMappingFitEnum(EnumDefinitionImpl):
    """
    The different values used to describe how closely a mapping between CAPEC and an external taxonomy aligns.
    """
    Exact = PermissibleValue(
        text="Exact",
        description="The CAPEC entry and the external taxonomy entry are an exact match in scope and meaning.")
    Imprecise = PermissibleValue(
        text="Imprecise",
        description="The mapping between CAPEC and the external taxonomy entry is approximate or imprecise.")
    Perspective = PermissibleValue(
        text="Perspective",
        description="""The CAPEC entry and the external taxonomy entry represent different perspectives on the same concept.""")

    _defn = EnumDefinition(
        name="TaxonomyMappingFitEnum",
        description="""The different values used to describe how closely a mapping between CAPEC and an external taxonomy aligns.""",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "CAPEC More Abstract",
            PermissibleValue(
                text="CAPEC More Abstract",
                description="The CAPEC entry is more abstract (broader) than the mapped external taxonomy entry."))
        setattr(cls, "CAPEC More Specific",
            PermissibleValue(
                text="CAPEC More Specific",
                description="The CAPEC entry is more specific (narrower) than the mapped external taxonomy entry."))

class TaxonomyNameEnum(EnumDefinitionImpl):
    """
    The different known taxonomies to which CAPEC entries can be mapped.
    """
    ATTACK = PermissibleValue(
        text="ATTACK",
        description="""The MITRE ATT&CK framework, a globally-accessible knowledge base of adversary tactics and techniques.""")
    WASC = PermissibleValue(
        text="WASC",
        description="The Web Application Security Consortium (WASC) Threat Classification taxonomy.")

    _defn = EnumDefinition(
        name="TaxonomyNameEnum",
        description="The different known taxonomies to which CAPEC entries can be mapped.",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "OWASP Attacks",
            PermissibleValue(
                text="OWASP Attacks",
                description="The OWASP (Open Web Application Security Project) Attacks taxonomy."))

class TechnicalImpactEnum(EnumDefinitionImpl):
    """
    The different negative technical impacts that can result from a successful attack
    leveraging a given attack pattern. A negative technical impact is the specific
    technical effect of successfully violating a reasonable security policy for the
    system or network.
    """
    Other = PermissibleValue(
        text="Other",
        description="Other technical impact not covered by the defined categories.")

    _defn = EnumDefinition(
        name="TechnicalImpactEnum",
        description="""The different negative technical impacts that can result from a successful attack
leveraging a given attack pattern. A negative technical impact is the specific
technical effect of successfully violating a reasonable security policy for the
system or network.""",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "Modify Data",
            PermissibleValue(
                text="Modify Data",
                description="The attacker can modify data stored within or processed by the target system."))
        setattr(cls, "Read Data",
            PermissibleValue(
                text="Read Data",
                description="The attacker can read sensitive or confidential data from the target system."))
        setattr(cls, "Unreliable Execution",
            PermissibleValue(
                text="Unreliable Execution",
                description="The execution of the target system becomes unreliable or unpredictable."))
        setattr(cls, "Resource Consumption",
            PermissibleValue(
                text="Resource Consumption",
                description="Target system resources (CPU, memory, bandwidth) are consumed by the attack."))
        setattr(cls, "Execute Unauthorized Commands",
            PermissibleValue(
                text="Execute Unauthorized Commands",
                description="The attacker can execute unauthorized commands or code on the target system."))
        setattr(cls, "Gain Privileges",
            PermissibleValue(
                text="Gain Privileges",
                description="The attacker gains elevated or unauthorized privileges on the target system."))
        setattr(cls, "Bypass Protection Mechanism",
            PermissibleValue(
                text="Bypass Protection Mechanism",
                description="The attacker can bypass existing security controls or protection mechanisms."))
        setattr(cls, "Hide Activities",
            PermissibleValue(
                text="Hide Activities",
                description="The attacker can conceal malicious activities from detection and monitoring."))
        setattr(cls, "Alter Execution Logic",
            PermissibleValue(
                text="Alter Execution Logic",
                description="""The attacker can alter the normal execution logic or control flow of the target system."""))

class ViewTypeEnum(EnumDefinitionImpl):
    """
    The different types of views that can be found within CAPEC. A graph is a
    hierarchical representation of attack patterns based on a specific vantage point.
    An explicit slice is a subset of attack patterns related through some external
    factor. An implicit slice is a subset of attack patterns related through a specific
    attribute.
    """
    Implicit = PermissibleValue(
        text="Implicit",
        description="""A subset of attack patterns that are related through a specific attribute. For
example, a slice may refer to all attack patterns in draft status, or all existing
meta attack patterns. Members are defined by the Filter element (an XSL query).""")
    Explicit = PermissibleValue(
        text="Explicit",
        description="""A subset of attack patterns that are related through some external factor. For
example, a view may represent mappings to external groupings like a Top-N list.
Members are defined externally through Member_Of relationships.""")
    Graph = PermissibleValue(
        text="Graph",
        description="""A hierarchical representation of attack patterns based on a specific vantage point
that a user may take. The hierarchy often starts with a category, followed by a
meta/standard attack pattern, and ends with a detailed attack pattern. Members are
defined through Member_Of relationships on categories.""")

    _defn = EnumDefinition(
        name="ViewTypeEnum",
        description="""The different types of views that can be found within CAPEC. A graph is a
hierarchical representation of attack patterns based on a specific vantage point.
An explicit slice is a subset of attack patterns related through some external
factor. An implicit slice is a subset of attack patterns related through a specific
attribute.""",
    )

# Slots
class slots:
    pass

slots.id = Slot(uri=CAPEC.id, name="id", curie=CAPEC.curie('id'),
                   model_uri=CAPEC.id, domain=None, range=URIRef)

slots.name = Slot(uri=CAPEC.name, name="name", curie=CAPEC.curie('name'),
                   model_uri=CAPEC.name, domain=None, range=str)

slots.version = Slot(uri=CAPEC.version, name="version", curie=CAPEC.curie('version'),
                   model_uri=CAPEC.version, domain=None, range=Optional[str])

slots.entry_date = Slot(uri=CAPEC.entry_date, name="entry_date", curie=CAPEC.curie('entry_date'),
                   model_uri=CAPEC.entry_date, domain=None, range=Optional[Union[str, XSDDate]])

slots.type = Slot(uri=CAPEC.type, name="type", curie=CAPEC.curie('type'),
                   model_uri=CAPEC.type, domain=None, range=Optional[str])

slots.status = Slot(uri=CAPEC.status, name="status", curie=CAPEC.curie('status'),
                   model_uri=CAPEC.status, domain=None, range=Union[str, "StatusEnum"])

slots.description = Slot(uri=CAPEC.description, name="description", curie=CAPEC.curie('description'),
                   model_uri=CAPEC.description, domain=None, range=Optional[str])

slots.capec_id = Slot(uri=CAPEC.capec_id, name="capec_id", curie=CAPEC.curie('capec_id'),
                   model_uri=CAPEC.capec_id, domain=None, range=Optional[int])

slots.exclude_related = Slot(uri=CAPEC.exclude_related, name="exclude_related", curie=CAPEC.curie('exclude_related'),
                   model_uri=CAPEC.exclude_related, domain=None, range=Optional[Union[Union[dict, ExcludeRelated], list[Union[dict, ExcludeRelated]]]])

slots.notes = Slot(uri=CAPEC.notes, name="notes", curie=CAPEC.curie('notes'),
                   model_uri=CAPEC.notes, domain=None, range=Optional[Union[Union[dict, Note], list[Union[dict, Note]]]])

slots.content_history = Slot(uri=CAPEC.content_history, name="content_history", curie=CAPEC.curie('content_history'),
                   model_uri=CAPEC.content_history, domain=None, range=Optional[Union[dict, ContentHistory]])

slots.references = Slot(uri=CAPEC.references, name="references", curie=CAPEC.curie('references'),
                   model_uri=CAPEC.references, domain=None, range=Optional[Union[Union[dict, Reference], list[Union[dict, Reference]]]])

slots.taxonomy_mappings = Slot(uri=CAPEC.taxonomy_mappings, name="taxonomy_mappings", curie=CAPEC.curie('taxonomy_mappings'),
                   model_uri=CAPEC.taxonomy_mappings, domain=None, range=Optional[Union[Union[dict, TaxonomyMapping], list[Union[dict, TaxonomyMapping]]]])

slots.abstraction = Slot(uri=CAPEC.abstraction, name="abstraction", curie=CAPEC.curie('abstraction'),
                   model_uri=CAPEC.abstraction, domain=None, range=Union[str, "AbstractionEnum"])

slots.alternate_terms = Slot(uri=CAPEC.alternate_terms, name="alternate_terms", curie=CAPEC.curie('alternate_terms'),
                   model_uri=CAPEC.alternate_terms, domain=None, range=Optional[Union[Union[dict, AlternateTerm], list[Union[dict, AlternateTerm]]]])

slots.attack_patterns = Slot(uri=CAPEC.attack_patterns, name="attack_patterns", curie=CAPEC.curie('attack_patterns'),
                   model_uri=CAPEC.attack_patterns, domain=None, range=Optional[Union[dict[Union[int, AttackPatternId], Union[dict, AttackPattern]], list[Union[dict, AttackPattern]]]])

slots.audience = Slot(uri=CAPEC.audience, name="audience", curie=CAPEC.curie('audience'),
                   model_uri=CAPEC.audience, domain=None, range=Optional[Union[Union[dict, Stakeholder], list[Union[dict, Stakeholder]]]])

slots.authors = Slot(uri=CAPEC.authors, name="authors", curie=CAPEC.curie('authors'),
                   model_uri=CAPEC.authors, domain=None, range=Optional[Union[str, list[str]]])

slots.categories = Slot(uri=CAPEC.categories, name="categories", curie=CAPEC.curie('categories'),
                   model_uri=CAPEC.categories, domain=None, range=Optional[Union[dict[Union[int, CategoryId], Union[dict, Category]], list[Union[dict, Category]]]])

slots.consequence_id = Slot(uri=CAPEC.consequence_id, name="consequence_id", curie=CAPEC.curie('consequence_id'),
                   model_uri=CAPEC.consequence_id, domain=None, range=Optional[str])

slots.consequences = Slot(uri=CAPEC.consequences, name="consequences", curie=CAPEC.curie('consequences'),
                   model_uri=CAPEC.consequences, domain=None, range=Optional[Union[Union[dict, Consequence], list[Union[dict, Consequence]]]])

slots.content = Slot(uri=CAPEC.content, name="content", curie=CAPEC.curie('content'),
                   model_uri=CAPEC.content, domain=None, range=str)

slots.contribution_comment = Slot(uri=CAPEC.contribution_comment, name="contribution_comment", curie=CAPEC.curie('contribution_comment'),
                   model_uri=CAPEC.contribution_comment, domain=None, range=Optional[str])

slots.contribution_date = Slot(uri=CAPEC.contribution_date, name="contribution_date", curie=CAPEC.curie('contribution_date'),
                   model_uri=CAPEC.contribution_date, domain=None, range=Optional[Union[str, XSDDate]])

slots.contribution_name = Slot(uri=CAPEC.contribution_name, name="contribution_name", curie=CAPEC.curie('contribution_name'),
                   model_uri=CAPEC.contribution_name, domain=None, range=Optional[str])

slots.contribution_organization = Slot(uri=CAPEC.contribution_organization, name="contribution_organization", curie=CAPEC.curie('contribution_organization'),
                   model_uri=CAPEC.contribution_organization, domain=None, range=Optional[str])

slots.contributions = Slot(uri=CAPEC.contributions, name="contributions", curie=CAPEC.curie('contributions'),
                   model_uri=CAPEC.contributions, domain=None, range=Optional[Union[Union[dict, Contribution], list[Union[dict, Contribution]]]])

slots.cwe_id = Slot(uri=CAPEC.cwe_id, name="cwe_id", curie=CAPEC.curie('cwe_id'),
                   model_uri=CAPEC.cwe_id, domain=None, range=int)

slots.edition = Slot(uri=CAPEC.edition, name="edition", curie=CAPEC.curie('edition'),
                   model_uri=CAPEC.edition, domain=None, range=Optional[str])

slots.entry_id = Slot(uri=CAPEC.entry_id, name="entry_id", curie=CAPEC.curie('entry_id'),
                   model_uri=CAPEC.entry_id, domain=None, range=Optional[str])

slots.entry_name = Slot(uri=CAPEC.entry_name, name="entry_name", curie=CAPEC.curie('entry_name'),
                   model_uri=CAPEC.entry_name, domain=None, range=Optional[str])

slots.example_instances = Slot(uri=CAPEC.example_instances, name="example_instances", curie=CAPEC.curie('example_instances'),
                   model_uri=CAPEC.example_instances, domain=None, range=Optional[Union[str, list[str]]])

slots.exclude_id = Slot(uri=CAPEC.exclude_id, name="exclude_id", curie=CAPEC.curie('exclude_id'),
                   model_uri=CAPEC.exclude_id, domain=None, range=int)

slots.execution_flow = Slot(uri=CAPEC.execution_flow, name="execution_flow", curie=CAPEC.curie('execution_flow'),
                   model_uri=CAPEC.execution_flow, domain=None, range=Optional[Union[Union[dict, AttackStep], list[Union[dict, AttackStep]]]])

slots.extended_description = Slot(uri=CAPEC.extended_description, name="extended_description", curie=CAPEC.curie('extended_description'),
                   model_uri=CAPEC.extended_description, domain=None, range=Optional[str])

slots.external_reference_id = Slot(uri=CAPEC.external_reference_id, name="external_reference_id", curie=CAPEC.curie('external_reference_id'),
                   model_uri=CAPEC.external_reference_id, domain=None, range=str)

slots.external_references = Slot(uri=CAPEC.external_references, name="external_references", curie=CAPEC.curie('external_references'),
                   model_uri=CAPEC.external_references, domain=None, range=Optional[Union[dict[Union[str, ExternalReferenceReferenceId], Union[dict, ExternalReference]], list[Union[dict, ExternalReference]]]])

slots.filter = Slot(uri=CAPEC.filter, name="filter", curie=CAPEC.curie('filter'),
                   model_uri=CAPEC.filter, domain=None, range=Optional[str])

slots.has_member = Slot(uri=CAPEC.has_member, name="has_member", curie=CAPEC.curie('has_member'),
                   model_uri=CAPEC.has_member, domain=None, range=Optional[Union[Union[dict, HasMember], list[Union[dict, HasMember]]]])

slots.impact = Slot(uri=CAPEC.impact, name="impact", curie=CAPEC.curie('impact'),
                   model_uri=CAPEC.impact, domain=None, range=Optional[Union[Union[str, "TechnicalImpactEnum"], list[Union[str, "TechnicalImpactEnum"]]]])

slots.indicators = Slot(uri=CAPEC.indicators, name="indicators", curie=CAPEC.curie('indicators'),
                   model_uri=CAPEC.indicators, domain=None, range=Optional[Union[str, list[str]]])

slots.level = Slot(uri=CAPEC.level, name="level", curie=CAPEC.curie('level'),
                   model_uri=CAPEC.level, domain=None, range=Union[str, "SkillLevelEnum"])

slots.likelihood = Slot(uri=CAPEC.likelihood, name="likelihood", curie=CAPEC.curie('likelihood'),
                   model_uri=CAPEC.likelihood, domain=None, range=Optional[Union[str, "LikelihoodEnum"]])

slots.likelihood_of_attack = Slot(uri=CAPEC.likelihood_of_attack, name="likelihood_of_attack", curie=CAPEC.curie('likelihood_of_attack'),
                   model_uri=CAPEC.likelihood_of_attack, domain=None, range=Optional[Union[str, "LikelihoodEnum"]])

slots.mapping_fit = Slot(uri=CAPEC.mapping_fit, name="mapping_fit", curie=CAPEC.curie('mapping_fit'),
                   model_uri=CAPEC.mapping_fit, domain=None, range=Optional[Union[str, "TaxonomyMappingFitEnum"]])

slots.member_of = Slot(uri=CAPEC.member_of, name="member_of", curie=CAPEC.curie('member_of'),
                   model_uri=CAPEC.member_of, domain=None, range=Optional[Union[Union[dict, MemberOf], list[Union[dict, MemberOf]]]])

slots.members = Slot(uri=CAPEC.members, name="members", curie=CAPEC.curie('members'),
                   model_uri=CAPEC.members, domain=None, range=Optional[Union[dict, Relationships]])

slots.mitigations = Slot(uri=CAPEC.mitigations, name="mitigations", curie=CAPEC.curie('mitigations'),
                   model_uri=CAPEC.mitigations, domain=None, range=Optional[Union[str, list[str]]])

slots.modification_comment = Slot(uri=CAPEC.modification_comment, name="modification_comment", curie=CAPEC.curie('modification_comment'),
                   model_uri=CAPEC.modification_comment, domain=None, range=Optional[str])

slots.modification_date = Slot(uri=CAPEC.modification_date, name="modification_date", curie=CAPEC.curie('modification_date'),
                   model_uri=CAPEC.modification_date, domain=None, range=Optional[Union[str, XSDDate]])

slots.modification_importance = Slot(uri=CAPEC.modification_importance, name="modification_importance", curie=CAPEC.curie('modification_importance'),
                   model_uri=CAPEC.modification_importance, domain=None, range=Optional[Union[str, "ImportanceEnum"]])

slots.modification_name = Slot(uri=CAPEC.modification_name, name="modification_name", curie=CAPEC.curie('modification_name'),
                   model_uri=CAPEC.modification_name, domain=None, range=Optional[str])

slots.modification_organization = Slot(uri=CAPEC.modification_organization, name="modification_organization", curie=CAPEC.curie('modification_organization'),
                   model_uri=CAPEC.modification_organization, domain=None, range=Optional[str])

slots.modifications = Slot(uri=CAPEC.modifications, name="modifications", curie=CAPEC.curie('modifications'),
                   model_uri=CAPEC.modifications, domain=None, range=Optional[Union[Union[dict, Modification], list[Union[dict, Modification]]]])

slots.nature = Slot(uri=CAPEC.nature, name="nature", curie=CAPEC.curie('nature'),
                   model_uri=CAPEC.nature, domain=None, range=Union[str, "RelatedNatureEnum"])

slots.note = Slot(uri=CAPEC.note, name="note", curie=CAPEC.curie('note'),
                   model_uri=CAPEC.note, domain=None, range=Optional[str])

slots.objective = Slot(uri=CAPEC.objective, name="objective", curie=CAPEC.curie('objective'),
                   model_uri=CAPEC.objective, domain=None, range=str)

slots.phase = Slot(uri=CAPEC.phase, name="phase", curie=CAPEC.curie('phase'),
                   model_uri=CAPEC.phase, domain=None, range=Union[str, "AttackStepPhaseEnum"])

slots.prerequisites = Slot(uri=CAPEC.prerequisites, name="prerequisites", curie=CAPEC.curie('prerequisites'),
                   model_uri=CAPEC.prerequisites, domain=None, range=Optional[Union[str, list[str]]])

slots.previous_entry_names = Slot(uri=CAPEC.previous_entry_names, name="previous_entry_names", curie=CAPEC.curie('previous_entry_names'),
                   model_uri=CAPEC.previous_entry_names, domain=None, range=Optional[Union[Union[dict, PreviousEntryName], list[Union[dict, PreviousEntryName]]]])

slots.publication = Slot(uri=CAPEC.publication, name="publication", curie=CAPEC.curie('publication'),
                   model_uri=CAPEC.publication, domain=None, range=Optional[str])

slots.publication_day = Slot(uri=CAPEC.publication_day, name="publication_day", curie=CAPEC.curie('publication_day'),
                   model_uri=CAPEC.publication_day, domain=None, range=Optional[str])

slots.publication_month = Slot(uri=CAPEC.publication_month, name="publication_month", curie=CAPEC.curie('publication_month'),
                   model_uri=CAPEC.publication_month, domain=None, range=Optional[str])

slots.publication_year = Slot(uri=CAPEC.publication_year, name="publication_year", curie=CAPEC.curie('publication_year'),
                   model_uri=CAPEC.publication_year, domain=None, range=Optional[str])

slots.publisher = Slot(uri=CAPEC.publisher, name="publisher", curie=CAPEC.curie('publisher'),
                   model_uri=CAPEC.publisher, domain=None, range=Optional[str])

slots.reference_id = Slot(uri=CAPEC.reference_id, name="reference_id", curie=CAPEC.curie('reference_id'),
                   model_uri=CAPEC.reference_id, domain=None, range=URIRef)

slots.related_attack_patterns = Slot(uri=CAPEC.related_attack_patterns, name="related_attack_patterns", curie=CAPEC.curie('related_attack_patterns'),
                   model_uri=CAPEC.related_attack_patterns, domain=None, range=Optional[Union[Union[dict, RelatedAttackPattern], list[Union[dict, RelatedAttackPattern]]]])

slots.related_weaknesses = Slot(uri=CAPEC.related_weaknesses, name="related_weaknesses", curie=CAPEC.curie('related_weaknesses'),
                   model_uri=CAPEC.related_weaknesses, domain=None, range=Optional[Union[int, list[int]]])

slots.relationships = Slot(uri=CAPEC.relationships, name="relationships", curie=CAPEC.curie('relationships'),
                   model_uri=CAPEC.relationships, domain=None, range=Optional[Union[dict, Relationships]])

slots.resources_required = Slot(uri=CAPEC.resources_required, name="resources_required", curie=CAPEC.curie('resources_required'),
                   model_uri=CAPEC.resources_required, domain=None, range=Optional[Union[str, list[str]]])

slots.scope = Slot(uri=CAPEC.scope, name="scope", curie=CAPEC.curie('scope'),
                   model_uri=CAPEC.scope, domain=None, range=Union[Union[str, "ScopeEnum"], list[Union[str, "ScopeEnum"]]])

slots.section = Slot(uri=CAPEC.section, name="section", curie=CAPEC.curie('section'),
                   model_uri=CAPEC.section, domain=None, range=Optional[str])

slots.skills_required = Slot(uri=CAPEC.skills_required, name="skills_required", curie=CAPEC.curie('skills_required'),
                   model_uri=CAPEC.skills_required, domain=None, range=Optional[Union[Union[dict, Skill], list[Union[dict, Skill]]]])

slots.step = Slot(uri=CAPEC.step, name="step", curie=CAPEC.curie('step'),
                   model_uri=CAPEC.step, domain=None, range=int)

slots.submission = Slot(uri=CAPEC.submission, name="submission", curie=CAPEC.curie('submission'),
                   model_uri=CAPEC.submission, domain=None, range=Optional[Union[dict, Submission]])

slots.submission_comment = Slot(uri=CAPEC.submission_comment, name="submission_comment", curie=CAPEC.curie('submission_comment'),
                   model_uri=CAPEC.submission_comment, domain=None, range=Optional[str])

slots.submission_date = Slot(uri=CAPEC.submission_date, name="submission_date", curie=CAPEC.curie('submission_date'),
                   model_uri=CAPEC.submission_date, domain=None, range=Optional[Union[str, XSDDate]])

slots.submission_name = Slot(uri=CAPEC.submission_name, name="submission_name", curie=CAPEC.curie('submission_name'),
                   model_uri=CAPEC.submission_name, domain=None, range=Optional[str])

slots.submission_organization = Slot(uri=CAPEC.submission_organization, name="submission_organization", curie=CAPEC.curie('submission_organization'),
                   model_uri=CAPEC.submission_organization, domain=None, range=Optional[str])

slots.summary = Slot(uri=CAPEC.summary, name="summary", curie=CAPEC.curie('summary'),
                   model_uri=CAPEC.summary, domain=None, range=str)

slots.taxonomy_name = Slot(uri=CAPEC.taxonomy_name, name="taxonomy_name", curie=CAPEC.curie('taxonomy_name'),
                   model_uri=CAPEC.taxonomy_name, domain=None, range=Union[str, "TaxonomyNameEnum"])

slots.techniques = Slot(uri=CAPEC.techniques, name="techniques", curie=CAPEC.curie('techniques'),
                   model_uri=CAPEC.techniques, domain=None, range=Optional[Union[Union[dict, Technique], list[Union[dict, Technique]]]])

slots.term = Slot(uri=CAPEC.term, name="term", curie=CAPEC.curie('term'),
                   model_uri=CAPEC.term, domain=None, range=str)

slots.title = Slot(uri=CAPEC.title, name="title", curie=CAPEC.curie('title'),
                   model_uri=CAPEC.title, domain=None, range=str)

slots.typical_severity = Slot(uri=CAPEC.typical_severity, name="typical_severity", curie=CAPEC.curie('typical_severity'),
                   model_uri=CAPEC.typical_severity, domain=None, range=Optional[Union[str, "SeverityEnum"]])

slots.url = Slot(uri=CAPEC.url, name="url", curie=CAPEC.curie('url'),
                   model_uri=CAPEC.url, domain=None, range=Optional[str])

slots.url_date = Slot(uri=CAPEC.url_date, name="url_date", curie=CAPEC.curie('url_date'),
                   model_uri=CAPEC.url_date, domain=None, range=Optional[Union[str, XSDDate]])

slots.views = Slot(uri=CAPEC.views, name="views", curie=CAPEC.curie('views'),
                   model_uri=CAPEC.views, domain=None, range=Optional[Union[dict[Union[int, ViewId], Union[dict, View]], list[Union[dict, View]]]])

slots.AttackPatternCatalog_name = Slot(uri=CAPEC.name, name="AttackPatternCatalog_name", curie=CAPEC.curie('name'),
                   model_uri=CAPEC.AttackPatternCatalog_name, domain=AttackPatternCatalog, range=str)

slots.AttackPatternCatalog_version = Slot(uri=CAPEC.version, name="AttackPatternCatalog_version", curie=CAPEC.curie('version'),
                   model_uri=CAPEC.AttackPatternCatalog_version, domain=AttackPatternCatalog, range=str)

slots.AttackPatternCatalog_entry_date = Slot(uri=CAPEC.entry_date, name="AttackPatternCatalog_entry_date", curie=CAPEC.curie('entry_date'),
                   model_uri=CAPEC.AttackPatternCatalog_entry_date, domain=AttackPatternCatalog, range=Union[str, XSDDate])

slots.AttackPatternCatalog_attack_patterns = Slot(uri=CAPEC.attack_patterns, name="AttackPatternCatalog_attack_patterns", curie=CAPEC.curie('attack_patterns'),
                   model_uri=CAPEC.AttackPatternCatalog_attack_patterns, domain=AttackPatternCatalog, range=Optional[Union[dict[Union[int, AttackPatternId], Union[dict, "AttackPattern"]], list[Union[dict, "AttackPattern"]]]])

slots.AttackPatternCatalog_categories = Slot(uri=CAPEC.categories, name="AttackPatternCatalog_categories", curie=CAPEC.curie('categories'),
                   model_uri=CAPEC.AttackPatternCatalog_categories, domain=AttackPatternCatalog, range=Optional[Union[dict[Union[int, CategoryId], Union[dict, "Category"]], list[Union[dict, "Category"]]]])

slots.AttackPatternCatalog_views = Slot(uri=CAPEC.views, name="AttackPatternCatalog_views", curie=CAPEC.curie('views'),
                   model_uri=CAPEC.AttackPatternCatalog_views, domain=AttackPatternCatalog, range=Optional[Union[dict[Union[int, ViewId], Union[dict, "View"]], list[Union[dict, "View"]]]])

slots.AttackPatternCatalog_external_references = Slot(uri=CAPEC.external_references, name="AttackPatternCatalog_external_references", curie=CAPEC.curie('external_references'),
                   model_uri=CAPEC.AttackPatternCatalog_external_references, domain=AttackPatternCatalog, range=Optional[Union[dict[Union[str, ExternalReferenceReferenceId], Union[dict, "ExternalReference"]], list[Union[dict, "ExternalReference"]]]])

slots.AttackPattern_description = Slot(uri=CAPEC.description, name="AttackPattern_description", curie=CAPEC.curie('description'),
                   model_uri=CAPEC.AttackPattern_description, domain=AttackPattern, range=str)

slots.AttackPattern_abstraction = Slot(uri=CAPEC.abstraction, name="AttackPattern_abstraction", curie=CAPEC.curie('abstraction'),
                   model_uri=CAPEC.AttackPattern_abstraction, domain=AttackPattern, range=Union[str, "AbstractionEnum"])

slots.AttackPattern_extended_description = Slot(uri=CAPEC.extended_description, name="AttackPattern_extended_description", curie=CAPEC.curie('extended_description'),
                   model_uri=CAPEC.AttackPattern_extended_description, domain=AttackPattern, range=Optional[str])

slots.AttackPattern_alternate_terms = Slot(uri=CAPEC.alternate_terms, name="AttackPattern_alternate_terms", curie=CAPEC.curie('alternate_terms'),
                   model_uri=CAPEC.AttackPattern_alternate_terms, domain=AttackPattern, range=Optional[Union[Union[dict, "AlternateTerm"], list[Union[dict, "AlternateTerm"]]]])

slots.AttackPattern_likelihood_of_attack = Slot(uri=CAPEC.likelihood_of_attack, name="AttackPattern_likelihood_of_attack", curie=CAPEC.curie('likelihood_of_attack'),
                   model_uri=CAPEC.AttackPattern_likelihood_of_attack, domain=AttackPattern, range=Optional[Union[str, "LikelihoodEnum"]])

slots.AttackPattern_typical_severity = Slot(uri=CAPEC.typical_severity, name="AttackPattern_typical_severity", curie=CAPEC.curie('typical_severity'),
                   model_uri=CAPEC.AttackPattern_typical_severity, domain=AttackPattern, range=Optional[Union[str, "SeverityEnum"]])

slots.AttackPattern_related_attack_patterns = Slot(uri=CAPEC.related_attack_patterns, name="AttackPattern_related_attack_patterns", curie=CAPEC.curie('related_attack_patterns'),
                   model_uri=CAPEC.AttackPattern_related_attack_patterns, domain=AttackPattern, range=Optional[Union[Union[dict, "RelatedAttackPattern"], list[Union[dict, "RelatedAttackPattern"]]]])

slots.AttackPattern_execution_flow = Slot(uri=CAPEC.execution_flow, name="AttackPattern_execution_flow", curie=CAPEC.curie('execution_flow'),
                   model_uri=CAPEC.AttackPattern_execution_flow, domain=AttackPattern, range=Optional[Union[Union[dict, "AttackStep"], list[Union[dict, "AttackStep"]]]])

slots.AttackPattern_prerequisites = Slot(uri=CAPEC.prerequisites, name="AttackPattern_prerequisites", curie=CAPEC.curie('prerequisites'),
                   model_uri=CAPEC.AttackPattern_prerequisites, domain=AttackPattern, range=Optional[Union[str, list[str]]])

slots.AttackPattern_skills_required = Slot(uri=CAPEC.skills_required, name="AttackPattern_skills_required", curie=CAPEC.curie('skills_required'),
                   model_uri=CAPEC.AttackPattern_skills_required, domain=AttackPattern, range=Optional[Union[Union[dict, "Skill"], list[Union[dict, "Skill"]]]])

slots.AttackPattern_resources_required = Slot(uri=CAPEC.resources_required, name="AttackPattern_resources_required", curie=CAPEC.curie('resources_required'),
                   model_uri=CAPEC.AttackPattern_resources_required, domain=AttackPattern, range=Optional[Union[str, list[str]]])

slots.AttackPattern_indicators = Slot(uri=CAPEC.indicators, name="AttackPattern_indicators", curie=CAPEC.curie('indicators'),
                   model_uri=CAPEC.AttackPattern_indicators, domain=AttackPattern, range=Optional[Union[str, list[str]]])

slots.AttackPattern_consequences = Slot(uri=CAPEC.consequences, name="AttackPattern_consequences", curie=CAPEC.curie('consequences'),
                   model_uri=CAPEC.AttackPattern_consequences, domain=AttackPattern, range=Optional[Union[Union[dict, "Consequence"], list[Union[dict, "Consequence"]]]])

slots.AttackPattern_mitigations = Slot(uri=CAPEC.mitigations, name="AttackPattern_mitigations", curie=CAPEC.curie('mitigations'),
                   model_uri=CAPEC.AttackPattern_mitigations, domain=AttackPattern, range=Optional[Union[str, list[str]]])

slots.AttackPattern_example_instances = Slot(uri=CAPEC.example_instances, name="AttackPattern_example_instances", curie=CAPEC.curie('example_instances'),
                   model_uri=CAPEC.AttackPattern_example_instances, domain=AttackPattern, range=Optional[Union[str, list[str]]])

slots.AttackPattern_related_weaknesses = Slot(uri=CAPEC.related_weaknesses, name="AttackPattern_related_weaknesses", curie=CAPEC.curie('related_weaknesses'),
                   model_uri=CAPEC.AttackPattern_related_weaknesses, domain=AttackPattern, range=Optional[Union[int, list[int]]])

slots.Category_summary = Slot(uri=CAPEC.summary, name="Category_summary", curie=CAPEC.curie('summary'),
                   model_uri=CAPEC.Category_summary, domain=Category, range=str)

slots.Category_relationships = Slot(uri=CAPEC.relationships, name="Category_relationships", curie=CAPEC.curie('relationships'),
                   model_uri=CAPEC.Category_relationships, domain=Category, range=Optional[Union[dict, "Relationships"]])

slots.View_type = Slot(uri=CAPEC.type, name="View_type", curie=CAPEC.curie('type'),
                   model_uri=CAPEC.View_type, domain=View, range=Union[str, "ViewTypeEnum"])

slots.View_objective = Slot(uri=CAPEC.objective, name="View_objective", curie=CAPEC.curie('objective'),
                   model_uri=CAPEC.View_objective, domain=View, range=str)

slots.View_audience = Slot(uri=CAPEC.audience, name="View_audience", curie=CAPEC.curie('audience'),
                   model_uri=CAPEC.View_audience, domain=View, range=Optional[Union[Union[dict, "Stakeholder"], list[Union[dict, "Stakeholder"]]]])

slots.View_members = Slot(uri=CAPEC.members, name="View_members", curie=CAPEC.curie('members'),
                   model_uri=CAPEC.View_members, domain=View, range=Optional[Union[dict, "Relationships"]])

slots.View_filter = Slot(uri=CAPEC.filter, name="View_filter", curie=CAPEC.curie('filter'),
                   model_uri=CAPEC.View_filter, domain=View, range=Optional[str])

slots.ExternalReference_reference_id = Slot(uri=CAPEC.reference_id, name="ExternalReference_reference_id", curie=CAPEC.curie('reference_id'),
                   model_uri=CAPEC.ExternalReference_reference_id, domain=ExternalReference, range=Union[str, ExternalReferenceReferenceId])

slots.ExternalReference_authors = Slot(uri=CAPEC.authors, name="ExternalReference_authors", curie=CAPEC.curie('authors'),
                   model_uri=CAPEC.ExternalReference_authors, domain=ExternalReference, range=Optional[Union[str, list[str]]])

slots.ExternalReference_title = Slot(uri=CAPEC.title, name="ExternalReference_title", curie=CAPEC.curie('title'),
                   model_uri=CAPEC.ExternalReference_title, domain=ExternalReference, range=str)

slots.ExternalReference_edition = Slot(uri=CAPEC.edition, name="ExternalReference_edition", curie=CAPEC.curie('edition'),
                   model_uri=CAPEC.ExternalReference_edition, domain=ExternalReference, range=Optional[str])

slots.ExternalReference_publication = Slot(uri=CAPEC.publication, name="ExternalReference_publication", curie=CAPEC.curie('publication'),
                   model_uri=CAPEC.ExternalReference_publication, domain=ExternalReference, range=Optional[str])

slots.ExternalReference_publication_year = Slot(uri=CAPEC.publication_year, name="ExternalReference_publication_year", curie=CAPEC.curie('publication_year'),
                   model_uri=CAPEC.ExternalReference_publication_year, domain=ExternalReference, range=Optional[str])

slots.ExternalReference_publication_month = Slot(uri=CAPEC.publication_month, name="ExternalReference_publication_month", curie=CAPEC.curie('publication_month'),
                   model_uri=CAPEC.ExternalReference_publication_month, domain=ExternalReference, range=Optional[str])

slots.ExternalReference_publication_day = Slot(uri=CAPEC.publication_day, name="ExternalReference_publication_day", curie=CAPEC.curie('publication_day'),
                   model_uri=CAPEC.ExternalReference_publication_day, domain=ExternalReference, range=Optional[str])

slots.ExternalReference_publisher = Slot(uri=CAPEC.publisher, name="ExternalReference_publisher", curie=CAPEC.curie('publisher'),
                   model_uri=CAPEC.ExternalReference_publisher, domain=ExternalReference, range=Optional[str])

slots.ExternalReference_url = Slot(uri=CAPEC.url, name="ExternalReference_url", curie=CAPEC.curie('url'),
                   model_uri=CAPEC.ExternalReference_url, domain=ExternalReference, range=Optional[str])

slots.ExternalReference_url_date = Slot(uri=CAPEC.url_date, name="ExternalReference_url_date", curie=CAPEC.curie('url_date'),
                   model_uri=CAPEC.ExternalReference_url_date, domain=ExternalReference, range=Optional[Union[str, XSDDate]])

slots.AlternateTerm_description = Slot(uri=CAPEC.description, name="AlternateTerm_description", curie=CAPEC.curie('description'),
                   model_uri=CAPEC.AlternateTerm_description, domain=AlternateTerm, range=Optional[str])

slots.AlternateTerm_term = Slot(uri=CAPEC.term, name="AlternateTerm_term", curie=CAPEC.curie('term'),
                   model_uri=CAPEC.AlternateTerm_term, domain=AlternateTerm, range=str)

slots.Consequence_consequence_id = Slot(uri=CAPEC.consequence_id, name="Consequence_consequence_id", curie=CAPEC.curie('consequence_id'),
                   model_uri=CAPEC.Consequence_consequence_id, domain=Consequence, range=Optional[str])

slots.Consequence_scope = Slot(uri=CAPEC.scope, name="Consequence_scope", curie=CAPEC.curie('scope'),
                   model_uri=CAPEC.Consequence_scope, domain=Consequence, range=Union[Union[str, "ScopeEnum"], list[Union[str, "ScopeEnum"]]])

slots.Consequence_impact = Slot(uri=CAPEC.impact, name="Consequence_impact", curie=CAPEC.curie('impact'),
                   model_uri=CAPEC.Consequence_impact, domain=Consequence, range=Optional[Union[Union[str, "TechnicalImpactEnum"], list[Union[str, "TechnicalImpactEnum"]]]])

slots.Consequence_likelihood = Slot(uri=CAPEC.likelihood, name="Consequence_likelihood", curie=CAPEC.curie('likelihood'),
                   model_uri=CAPEC.Consequence_likelihood, domain=Consequence, range=Optional[Union[str, "LikelihoodEnum"]])

slots.Consequence_note = Slot(uri=CAPEC.note, name="Consequence_note", curie=CAPEC.curie('note'),
                   model_uri=CAPEC.Consequence_note, domain=Consequence, range=Optional[str])

slots.Skill_description = Slot(uri=CAPEC.description, name="Skill_description", curie=CAPEC.curie('description'),
                   model_uri=CAPEC.Skill_description, domain=Skill, range=str)

slots.Skill_level = Slot(uri=CAPEC.level, name="Skill_level", curie=CAPEC.curie('level'),
                   model_uri=CAPEC.Skill_level, domain=Skill, range=Union[str, "SkillLevelEnum"])

slots.Note_type = Slot(uri=CAPEC.type, name="Note_type", curie=CAPEC.curie('type'),
                   model_uri=CAPEC.Note_type, domain=Note, range=Union[str, "NoteTypeEnum"])

slots.Note_content = Slot(uri=CAPEC.content, name="Note_content", curie=CAPEC.curie('content'),
                   model_uri=CAPEC.Note_content, domain=Note, range=str)

slots.AttackStep_description = Slot(uri=CAPEC.description, name="AttackStep_description", curie=CAPEC.curie('description'),
                   model_uri=CAPEC.AttackStep_description, domain=AttackStep, range=str)

slots.AttackStep_step = Slot(uri=CAPEC.step, name="AttackStep_step", curie=CAPEC.curie('step'),
                   model_uri=CAPEC.AttackStep_step, domain=AttackStep, range=int)

slots.AttackStep_phase = Slot(uri=CAPEC.phase, name="AttackStep_phase", curie=CAPEC.curie('phase'),
                   model_uri=CAPEC.AttackStep_phase, domain=AttackStep, range=Union[str, "AttackStepPhaseEnum"])

slots.AttackStep_techniques = Slot(uri=CAPEC.techniques, name="AttackStep_techniques", curie=CAPEC.curie('techniques'),
                   model_uri=CAPEC.AttackStep_techniques, domain=AttackStep, range=Optional[Union[Union[dict, "Technique"], list[Union[dict, "Technique"]]]])

slots.Technique_capec_id = Slot(uri=CAPEC.capec_id, name="Technique_capec_id", curie=CAPEC.curie('capec_id'),
                   model_uri=CAPEC.Technique_capec_id, domain=Technique, range=Optional[str])

slots.Technique_description = Slot(uri=CAPEC.description, name="Technique_description", curie=CAPEC.curie('description'),
                   model_uri=CAPEC.Technique_description, domain=Technique, range=str)

slots.RelatedAttackPattern_capec_id = Slot(uri=CAPEC.capec_id, name="RelatedAttackPattern_capec_id", curie=CAPEC.curie('capec_id'),
                   model_uri=CAPEC.RelatedAttackPattern_capec_id, domain=RelatedAttackPattern, range=int)

slots.RelatedAttackPattern_exclude_related = Slot(uri=CAPEC.exclude_related, name="RelatedAttackPattern_exclude_related", curie=CAPEC.curie('exclude_related'),
                   model_uri=CAPEC.RelatedAttackPattern_exclude_related, domain=RelatedAttackPattern, range=Optional[Union[Union[dict, "ExcludeRelated"], list[Union[dict, "ExcludeRelated"]]]])

slots.RelatedAttackPattern_nature = Slot(uri=CAPEC.nature, name="RelatedAttackPattern_nature", curie=CAPEC.curie('nature'),
                   model_uri=CAPEC.RelatedAttackPattern_nature, domain=RelatedAttackPattern, range=Union[str, "RelatedNatureEnum"])

slots.ExcludeRelated_exclude_id = Slot(uri=CAPEC.exclude_id, name="ExcludeRelated_exclude_id", curie=CAPEC.curie('exclude_id'),
                   model_uri=CAPEC.ExcludeRelated_exclude_id, domain=ExcludeRelated, range=int)

slots.RelatedWeakness_cwe_id = Slot(uri=CAPEC.cwe_id, name="RelatedWeakness_cwe_id", curie=CAPEC.curie('cwe_id'),
                   model_uri=CAPEC.RelatedWeakness_cwe_id, domain=RelatedWeakness, range=int)

slots.Relationships_member_of = Slot(uri=CAPEC.member_of, name="Relationships_member_of", curie=CAPEC.curie('member_of'),
                   model_uri=CAPEC.Relationships_member_of, domain=Relationships, range=Optional[Union[Union[dict, "MemberOf"], list[Union[dict, "MemberOf"]]]])

slots.Relationships_has_member = Slot(uri=CAPEC.has_member, name="Relationships_has_member", curie=CAPEC.curie('has_member'),
                   model_uri=CAPEC.Relationships_has_member, domain=Relationships, range=Optional[Union[Union[dict, "HasMember"], list[Union[dict, "HasMember"]]]])

slots.MemberOf_capec_id = Slot(uri=CAPEC.capec_id, name="MemberOf_capec_id", curie=CAPEC.curie('capec_id'),
                   model_uri=CAPEC.MemberOf_capec_id, domain=MemberOf, range=int)

slots.MemberOf_exclude_related = Slot(uri=CAPEC.exclude_related, name="MemberOf_exclude_related", curie=CAPEC.curie('exclude_related'),
                   model_uri=CAPEC.MemberOf_exclude_related, domain=MemberOf, range=Optional[Union[Union[dict, ExcludeRelated], list[Union[dict, ExcludeRelated]]]])

slots.HasMember_capec_id = Slot(uri=CAPEC.capec_id, name="HasMember_capec_id", curie=CAPEC.curie('capec_id'),
                   model_uri=CAPEC.HasMember_capec_id, domain=HasMember, range=int)

slots.HasMember_exclude_related = Slot(uri=CAPEC.exclude_related, name="HasMember_exclude_related", curie=CAPEC.curie('exclude_related'),
                   model_uri=CAPEC.HasMember_exclude_related, domain=HasMember, range=Optional[Union[Union[dict, ExcludeRelated], list[Union[dict, ExcludeRelated]]]])

slots.Reference_external_reference_id = Slot(uri=CAPEC.external_reference_id, name="Reference_external_reference_id", curie=CAPEC.curie('external_reference_id'),
                   model_uri=CAPEC.Reference_external_reference_id, domain=Reference, range=str)

slots.Reference_section = Slot(uri=CAPEC.section, name="Reference_section", curie=CAPEC.curie('section'),
                   model_uri=CAPEC.Reference_section, domain=Reference, range=Optional[str])

slots.TaxonomyMapping_taxonomy_name = Slot(uri=CAPEC.taxonomy_name, name="TaxonomyMapping_taxonomy_name", curie=CAPEC.curie('taxonomy_name'),
                   model_uri=CAPEC.TaxonomyMapping_taxonomy_name, domain=TaxonomyMapping, range=Union[str, "TaxonomyNameEnum"])

slots.TaxonomyMapping_entry_id = Slot(uri=CAPEC.entry_id, name="TaxonomyMapping_entry_id", curie=CAPEC.curie('entry_id'),
                   model_uri=CAPEC.TaxonomyMapping_entry_id, domain=TaxonomyMapping, range=Optional[str])

slots.TaxonomyMapping_entry_name = Slot(uri=CAPEC.entry_name, name="TaxonomyMapping_entry_name", curie=CAPEC.curie('entry_name'),
                   model_uri=CAPEC.TaxonomyMapping_entry_name, domain=TaxonomyMapping, range=Optional[str])

slots.TaxonomyMapping_mapping_fit = Slot(uri=CAPEC.mapping_fit, name="TaxonomyMapping_mapping_fit", curie=CAPEC.curie('mapping_fit'),
                   model_uri=CAPEC.TaxonomyMapping_mapping_fit, domain=TaxonomyMapping, range=Optional[Union[str, "TaxonomyMappingFitEnum"]])

slots.Stakeholder_type = Slot(uri=CAPEC.type, name="Stakeholder_type", curie=CAPEC.curie('type'),
                   model_uri=CAPEC.Stakeholder_type, domain=Stakeholder, range=Union[str, "StakeholderEnum"])

slots.Stakeholder_description = Slot(uri=CAPEC.description, name="Stakeholder_description", curie=CAPEC.curie('description'),
                   model_uri=CAPEC.Stakeholder_description, domain=Stakeholder, range=str)

slots.ContentHistory_submission = Slot(uri=CAPEC.submission, name="ContentHistory_submission", curie=CAPEC.curie('submission'),
                   model_uri=CAPEC.ContentHistory_submission, domain=ContentHistory, range=Optional[Union[dict, "Submission"]])

slots.ContentHistory_modifications = Slot(uri=CAPEC.modifications, name="ContentHistory_modifications", curie=CAPEC.curie('modifications'),
                   model_uri=CAPEC.ContentHistory_modifications, domain=ContentHistory, range=Optional[Union[Union[dict, "Modification"], list[Union[dict, "Modification"]]]])

slots.ContentHistory_contributions = Slot(uri=CAPEC.contributions, name="ContentHistory_contributions", curie=CAPEC.curie('contributions'),
                   model_uri=CAPEC.ContentHistory_contributions, domain=ContentHistory, range=Optional[Union[Union[dict, "Contribution"], list[Union[dict, "Contribution"]]]])

slots.ContentHistory_previous_entry_names = Slot(uri=CAPEC.previous_entry_names, name="ContentHistory_previous_entry_names", curie=CAPEC.curie('previous_entry_names'),
                   model_uri=CAPEC.ContentHistory_previous_entry_names, domain=ContentHistory, range=Optional[Union[Union[dict, "PreviousEntryName"], list[Union[dict, "PreviousEntryName"]]]])

slots.Submission_submission_name = Slot(uri=CAPEC.submission_name, name="Submission_submission_name", curie=CAPEC.curie('submission_name'),
                   model_uri=CAPEC.Submission_submission_name, domain=Submission, range=Optional[str])

slots.Submission_submission_organization = Slot(uri=CAPEC.submission_organization, name="Submission_submission_organization", curie=CAPEC.curie('submission_organization'),
                   model_uri=CAPEC.Submission_submission_organization, domain=Submission, range=Optional[str])

slots.Submission_submission_date = Slot(uri=CAPEC.submission_date, name="Submission_submission_date", curie=CAPEC.curie('submission_date'),
                   model_uri=CAPEC.Submission_submission_date, domain=Submission, range=Optional[Union[str, XSDDate]])

slots.Submission_submission_comment = Slot(uri=CAPEC.submission_comment, name="Submission_submission_comment", curie=CAPEC.curie('submission_comment'),
                   model_uri=CAPEC.Submission_submission_comment, domain=Submission, range=Optional[str])

slots.Modification_modification_name = Slot(uri=CAPEC.modification_name, name="Modification_modification_name", curie=CAPEC.curie('modification_name'),
                   model_uri=CAPEC.Modification_modification_name, domain=Modification, range=Optional[str])

slots.Modification_modification_organization = Slot(uri=CAPEC.modification_organization, name="Modification_modification_organization", curie=CAPEC.curie('modification_organization'),
                   model_uri=CAPEC.Modification_modification_organization, domain=Modification, range=Optional[str])

slots.Modification_modification_date = Slot(uri=CAPEC.modification_date, name="Modification_modification_date", curie=CAPEC.curie('modification_date'),
                   model_uri=CAPEC.Modification_modification_date, domain=Modification, range=Optional[Union[str, XSDDate]])

slots.Modification_modification_importance = Slot(uri=CAPEC.modification_importance, name="Modification_modification_importance", curie=CAPEC.curie('modification_importance'),
                   model_uri=CAPEC.Modification_modification_importance, domain=Modification, range=Optional[Union[str, "ImportanceEnum"]])

slots.Modification_modification_comment = Slot(uri=CAPEC.modification_comment, name="Modification_modification_comment", curie=CAPEC.curie('modification_comment'),
                   model_uri=CAPEC.Modification_modification_comment, domain=Modification, range=Optional[str])

slots.Contribution_type = Slot(uri=CAPEC.type, name="Contribution_type", curie=CAPEC.curie('type'),
                   model_uri=CAPEC.Contribution_type, domain=Contribution, range=Union[str, "ContributionTypeEnum"])

slots.Contribution_contribution_name = Slot(uri=CAPEC.contribution_name, name="Contribution_contribution_name", curie=CAPEC.curie('contribution_name'),
                   model_uri=CAPEC.Contribution_contribution_name, domain=Contribution, range=Optional[str])

slots.Contribution_contribution_organization = Slot(uri=CAPEC.contribution_organization, name="Contribution_contribution_organization", curie=CAPEC.curie('contribution_organization'),
                   model_uri=CAPEC.Contribution_contribution_organization, domain=Contribution, range=Optional[str])

slots.Contribution_contribution_date = Slot(uri=CAPEC.contribution_date, name="Contribution_contribution_date", curie=CAPEC.curie('contribution_date'),
                   model_uri=CAPEC.Contribution_contribution_date, domain=Contribution, range=Optional[Union[str, XSDDate]])

slots.Contribution_contribution_comment = Slot(uri=CAPEC.contribution_comment, name="Contribution_contribution_comment", curie=CAPEC.curie('contribution_comment'),
                   model_uri=CAPEC.Contribution_contribution_comment, domain=Contribution, range=Optional[str])

slots.PreviousEntryName_name = Slot(uri=CAPEC.name, name="PreviousEntryName_name", curie=CAPEC.curie('name'),
                   model_uri=CAPEC.PreviousEntryName_name, domain=PreviousEntryName, range=str)

slots.PreviousEntryName_entry_date = Slot(uri=CAPEC.entry_date, name="PreviousEntryName_entry_date", curie=CAPEC.curie('entry_date'),
                   model_uri=CAPEC.PreviousEntryName_entry_date, domain=PreviousEntryName, range=Union[str, XSDDate])
