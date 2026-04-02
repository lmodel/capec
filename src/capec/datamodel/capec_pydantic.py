from __future__ import annotations

import re
import sys
from datetime import (
    date,
    datetime,
    time
)
from decimal import Decimal
from enum import Enum
from typing import (
    Any,
    ClassVar,
    Literal,
    Optional,
    Union
)

from pydantic import (
    BaseModel,
    ConfigDict,
    Field,
    RootModel,
    SerializationInfo,
    SerializerFunctionWrapHandler,
    field_validator,
    model_serializer
)


metamodel_version = "1.7.0"
version = "None"


class ConfiguredBaseModel(BaseModel):
    model_config = ConfigDict(
        serialize_by_alias = True,
        validate_by_name = True,
        validate_assignment = True,
        validate_default = True,
        extra = "forbid",
        arbitrary_types_allowed = True,
        use_enum_values = True,
        strict = False,
    )





class LinkMLMeta(RootModel):
    root: dict[str, Any] = {}
    model_config = ConfigDict(frozen=True)

    def __getattr__(self, key:str):
        return getattr(self.root, key)

    def __getitem__(self, key:str):
        return self.root[key]

    def __setitem__(self, key:str, value):
        self.root[key] = value

    def __contains__(self, key:str) -> bool:
        return key in self.root


linkml_meta = LinkMLMeta({'annotations': {'copyright': {'tag': 'copyright',
                                   'value': 'Copyright (c) 2007-2021, The MITRE '
                                            'Corporation. All rights reserved.'},
                     'schema': {'tag': 'schema', 'value': 'Core Attack Pattern'},
                     'schema_date': {'tag': 'schema_date',
                                     'value': '21 October 2021'},
                     'schema_version': {'tag': 'schema_version', 'value': '3.5.0'},
                     'source_namespace': {'tag': 'source_namespace',
                                          'value': 'http://capec.mitre.org/capec-3'},
                     'terms_of_use': {'tag': 'terms_of_use',
                                      'value': 'http://capec.mitre.org/about/termsofuse.html'}},
     'default_prefix': 'capec',
     'default_range': 'string',
     'description': 'Common Attack Pattern Enumeration and Classification (CAPEC): '
                    'A comprehensive dictionary\n'
                    'of known patterns of attack employed by adversaries to '
                    'exploit known weaknesses in\n'
                    'cyber-enabled capabilities. CAPEC is a community-developed '
                    'list maintained by The MITRE\n'
                    'Corporation that helps users understand how adversaries '
                    'exploit weaknesses in applications\n'
                    'and other cyber-enabled capabilities. The schema is '
                    'maintained by The MITRE Corporation\n'
                    'and developed in partnership with the public CAPEC Community.',
     'id': 'https://w3id.org/lmodel/capec',
     'imports': ['linkml:types'],
     'license': 'Apache-2.0',
     'name': 'capec',
     'prefixes': {'attack': {'prefix_prefix': 'attack',
                             'prefix_reference': 'https://attack.mitre.org/'},
                  'capec': {'prefix_prefix': 'capec',
                            'prefix_reference': 'https://w3id.org/lmodel/capec/'},
                  'dcterms': {'prefix_prefix': 'dcterms',
                              'prefix_reference': 'http://purl.org/dc/terms/'},
                  'linkml': {'prefix_prefix': 'linkml',
                             'prefix_reference': 'https://w3id.org/linkml/'},
                  'owasp': {'prefix_prefix': 'owasp',
                            'prefix_reference': 'https://owasp.org/'},
                  'schema': {'prefix_prefix': 'schema',
                             'prefix_reference': 'http://schema.org/'},
                  'stix': {'prefix_prefix': 'stix',
                           'prefix_reference': 'https://w3id.org/lmodel/stix/'},
                  'wasc': {'prefix_prefix': 'wasc',
                           'prefix_reference': 'http://projects.webappsec.org/'},
                  'xsd': {'prefix_prefix': 'xsd',
                          'prefix_reference': 'http://www.w3.org/2001/XMLSchema#'}},
     'see_also': ['https://lmodel.github.io/capec', 'https://capec.mitre.org/'],
     'source': 'https://capec.mitre.org/data/xsd/ap_schema_latest.xsd',
     'source_file': 'src/capec/schema/capec.yaml',
     'subsets': {'attack_pattern_content': {'description': 'Supporting types used '
                                                           'within attack pattern '
                                                           'content descriptions, '
                                                           'including consequence, '
                                                           'prerequisite, skill, '
                                                           'indicator, and '
                                                           'mitigation structures.',
                                            'from_schema': 'https://w3id.org/lmodel/capec',
                                            'name': 'attack_pattern_content'},
                 'audience_types': {'description': 'Types for describing target '
                                                   'stakeholder audiences relevant '
                                                   'to CAPEC views.',
                                    'from_schema': 'https://w3id.org/lmodel/capec',
                                    'name': 'audience_types'},
                 'catalog_entries': {'description': 'Top-level CAPEC catalog entry '
                                                    'types (AttackPattern, '
                                                    'Category, View, '
                                                    'ExternalReference) and the '
                                                    'catalog container itself.',
                                     'from_schema': 'https://w3id.org/lmodel/capec',
                                     'name': 'catalog_entries'},
                 'content_history_types': {'description': 'Types for tracking '
                                                          'authorship and '
                                                          'modification history of '
                                                          'CAPEC entries, '
                                                          'including submission, '
                                                          'modification, and '
                                                          'contribution records.',
                                           'from_schema': 'https://w3id.org/lmodel/capec',
                                           'name': 'content_history_types'},
                 'execution_flow_types': {'description': 'Types for describing the '
                                                         'detailed step-by-step '
                                                         'execution flow of attack '
                                                         'patterns, primarily '
                                                         'applicable to Detailed '
                                                         'abstraction level '
                                                         'patterns.',
                                          'from_schema': 'https://w3id.org/lmodel/capec',
                                          'name': 'execution_flow_types'},
                 'relationship_types': {'description': 'Types representing '
                                                       'relationships between '
                                                       'CAPEC entries, including '
                                                       'related attack patterns, '
                                                       'related weaknesses, '
                                                       'member-of and has-member '
                                                       'relationships.',
                                        'from_schema': 'https://w3id.org/lmodel/capec',
                                        'name': 'relationship_types'},
                 'taxonomy_types': {'description': 'Types for mapping CAPEC '
                                                   'entries to entries in external '
                                                   'security taxonomies such as '
                                                   'ATT&CK, WASC, and OWASP.',
                                    'from_schema': 'https://w3id.org/lmodel/capec',
                                    'name': 'taxonomy_types'}},
     'title': 'Common Attack Pattern Enumeration and Classification (CAPEC): '
              'LinkML Schema',
     'types': {'StructuredText': {'base': 'str',
                                  'description': 'Mixed content type allowing '
                                                 'XHTML content embedded within '
                                                 'standard string data.\n'
                                                 'Some common XHTML elements that '
                                                 'may appear: BR for line breaks, '
                                                 'UL/LI for bulleted\n'
                                                 'lists, OL/LI for numbered lists, '
                                                 'and DIV for indented sections.',
                                  'from_schema': 'https://w3id.org/lmodel/capec',
                                  'name': 'StructuredText',
                                  'notes': ['Corresponds to StructuredTextType in '
                                            'the CAPEC XSD which is a mixed '
                                            'complexType allowing xs:any elements '
                                            'from the XHTML namespace '
                                            '(xhtml1-strict). In LinkML this is '
                                            'represented as a plain string that '
                                            'may contain HTML markup.'],
                                  'uri': 'xsd:string'},
               'Uri': {'base': 'str',
                       'description': 'URI value represented as a string.',
                       'from_schema': 'https://w3id.org/lmodel/capec',
                       'name': 'Uri',
                       'uri': 'xsd:anyURI'}}} )

class AbstractionEnum(str, Enum):
    """
    The different abstraction levels that apply to an attack pattern. A Meta level
attack pattern is a decidedly abstract characterization of a specific methodology
or technique used in an attack. A Standard level attack pattern is focused on a
specific methodology or technique. A Detailed level attack pattern provides a low
level of detail, typically leveraging a specific technique and targeting a specific
technology, and expresses a complete execution flow.
    """
    Meta = "Meta"
    """
    A Meta level attack pattern in CAPEC is a decidedly abstract characterization
    of a specific methodology or technique used in an attack. A Meta attack pattern
    is often void of a specific technology or implementation and is meant to provide
    an understanding of a high level approach. A Meta level attack pattern is a
    generalization of related group of standard level attack patterns. Meta level
    attack patterns are particularly useful for architecture and design level threat
    modeling exercises.
    """
    Standard = "Standard"
    """
    A Standard level attack pattern in CAPEC is focused on a specific methodology
    or technique used in an attack. It is often seen as a singular piece of a fully
    executed attack. A Standard attack pattern is meant to provide sufficient details
    to understand the specific technique and how it attempts to accomplish a desired
    goal. A Standard level attack pattern is a specific type of a more abstract meta
    level attack pattern.
    """
    Detailed = "Detailed"
    """
    A Detailed level attack pattern in CAPEC provides a low level of detail, typically
    leveraging a specific technique and targeting a specific technology, and expresses
    a complete execution flow. Detailed attack patterns are more specific than meta and
    standard attack patterns and often require a specific protection mechanism to mitigate
    actual attacks. A Detailed level attack pattern often will leverage a number of
    different standard level attack patterns chained together to accomplish a goal.
    """


class AttackStepPhaseEnum(str, Enum):
    """
    The different phases of an individual attack step within the execution flow.
    """
    Explore = "Explore"
    """
    The exploration or reconnaissance phase of the attack.
    """
    Experiment = "Experiment"
    """
    The experimentation or testing phase of the attack.
    """
    Exploit = "Exploit"
    """
    The exploitation phase of the attack where intent is realized.
    """


class ContributionTypeEnum(str, Enum):
    """
    The type of contribution made to a CAPEC entry.
    """
    Content = "Content"
    """
    The contribution consisted of actual content donated to the entry.
    """
    Feedback = "Feedback"
    """
    The contribution consisted of general feedback about the entry.
    """


class ImportanceEnum(str, Enum):
    """
    Different values for the importance of a modification to CAPEC content.
    """
    Normal = "Normal"
    """
    Normal importance modification that does not significantly alter meaning.
    """
    Critical = "Critical"
    """
    Critical importance modification that changes the meaning of the entry, or how it might be interpreted, bringing it to the attention of anyone previously dependent on the attack pattern.
    """


class LikelihoodEnum(str, Enum):
    """
    Values corresponding to different likelihoods. The value Unknown should be used
when the actual likelihood of something occurring is not known.
    """
    High = "High"
    """
    High likelihood.
    """
    Medium = "Medium"
    """
    Medium likelihood.
    """
    Low = "Low"
    """
    Low likelihood.
    """
    Unknown = "Unknown"
    """
    The likelihood is unknown.
    """


class NoteTypeEnum(str, Enum):
    """
    The different types of notes that can be associated with an attack pattern.
A Maintenance note contains significant maintenance tasks within this entry that
still need to be addressed, such as clarifying the concepts involved or improving
relationships. A Relationship note provides clarifying details regarding the
relationships between entities. A Research Gap note identifies potential opportunities
for the research community to conduct further exploration. A Terminology note contains
a discussion of terminology issues related to this attack pattern.
    """
    Maintenance = "Maintenance"
    """
    Contains significant maintenance tasks within this entry that still need to be
    addressed, such as clarifying the concepts involved or improving relationships.
    """
    Relationship = "Relationship"
    """
    Provides clarifying details regarding the relationships between entities.
    """
    Research_Gap = "Research Gap"
    """
    Identifies potential opportunities for the research community to conduct further
    exploration of issues related to this attack pattern.
    """
    Terminology = "Terminology"
    """
    Contains a discussion of terminology issues related to this attack pattern,
    or clarifications when there is no established terminology, or if there are
    multiple uses of the same key term.
    """
    Other = "Other"
    """
    Other note type not covered by the defined categories.
    """


class RelatedNatureEnum(str, Enum):
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
    ChildOf = "ChildOf"
    """
    Denotes a related attack pattern at a higher level of abstraction; the current pattern is a specialization of the related pattern.
    """
    ParentOf = "ParentOf"
    """
    Denotes a related attack pattern at a lower level of abstraction; the current pattern is a generalization of the related pattern.
    """
    CanFollow = "CanFollow"
    """
    Denotes an attack pattern that can follow (come after) the current pattern in a chaining structure.
    """
    CanPrecede = "CanPrecede"
    """
    Denotes an attack pattern that can precede (come before) the current pattern in a chaining structure.
    """
    CanAlsoBe = "CanAlsoBe"
    """
    Denotes an attack pattern that, in the proper environment and context, can also
    be perceived as the target attack pattern. Note that the CanAlsoBe relationship
    is not necessarily reciprocal.
    """
    PeerOf = "PeerOf"
    """
    Used to show some similarity with the target attack pattern which does not fit
    any of the other types of relationships.
    """


class ScopeEnum(str, Enum):
    """
    The different areas of software security that can be affected by exploiting a weakness.
    """
    Confidentiality = "Confidentiality"
    """
    The confidentiality security property is violated.
    """
    Integrity = "Integrity"
    """
    The integrity security property is violated.
    """
    Availability = "Availability"
    """
    The availability security property is violated.
    """
    Access_Control = "Access Control"
    """
    The access control security property is violated.
    """
    Accountability = "Accountability"
    """
    The accountability security property is violated.
    """
    Authentication = "Authentication"
    """
    The authentication security property is violated.
    """
    Authorization = "Authorization"
    """
    The authorization security property is violated.
    """
    Non_Repudiation = "Non-Repudiation"
    """
    The non-repudiation security property is violated.
    """
    Other = "Other"
    """
    Other security property not covered by the defined categories.
    """


class SeverityEnum(str, Enum):
    """
    Values corresponding to different severities of attack impact.
    """
    Very_High = "Very High"
    """
    Very high severity impact.
    """
    High = "High"
    """
    High severity impact.
    """
    Medium = "Medium"
    """
    Medium severity impact.
    """
    Low = "Low"
    """
    Low severity impact.
    """
    Very_Low = "Very Low"
    """
    Very low severity impact.
    """


class SkillLevelEnum(str, Enum):
    """
    Values corresponding to different knowledge levels required to perform an attack.
The value Unknown should be used when the actual skill level is not known.
    """
    High = "High"
    """
    High skill level required to perform the attack.
    """
    Medium = "Medium"
    """
    Medium skill level required to perform the attack.
    """
    Low = "Low"
    """
    Low skill level required to perform the attack.
    """
    Unknown = "Unknown"
    """
    The skill level required to perform the attack is unknown.
    """


class StakeholderEnum(str, Enum):
    """
    The different types of users and stakeholder groups within the CAPEC community.
    """
    Academic_Researchers = "Academic Researchers"
    """
    Academic researchers studying attack patterns and cybersecurity.
    """
    Applied_Researchers = "Applied Researchers"
    """
    Applied researchers using CAPEC for practical security analysis.
    """
    Assessment_Customers = "Assessment Customers"
    """
    Customers who commission security assessments and penetration tests.
    """
    Assessment_Vendors = "Assessment Vendors"
    """
    Vendors and consultants who provide security assessment services.
    """
    CAPEC_Team = "CAPEC Team"
    """
    The core CAPEC development and maintenance team at MITRE.
    """
    Educators = "Educators"
    """
    Educators teaching courses on cybersecurity concepts using CAPEC.
    """
    Information_Providers = "Information Providers"
    """
    Organizations or individuals who provide cybersecurity information services.
    """
    Software_Customers = "Software Customers"
    """
    End users and customers of software products concerned about security.
    """
    Software_Designers = "Software Designers"
    """
    Software architects and designers involved in secure system design.
    """
    Software_Developers = "Software Developers"
    """
    Software developers building and maintaining secure software.
    """
    Software_Vendors = "Software Vendors"
    """
    Vendors who produce and distribute software products.
    """
    Other = "Other"
    """
    Other stakeholder type not covered by the defined categories.
    """


class StatusEnum(str, Enum):
    """
    The different status values that an entity (view, category, or attack pattern) can have.
    """
    Deprecated = "Deprecated"
    """
    The entry has been deprecated and should not be used. A placeholder for the deprecated entry is left in the catalog and the identifier is not reused.
    """
    Draft = "Draft"
    """
    The entry is a draft and its content may change significantly through future revisions as it is reviewed and refined by the community.
    """
    Incomplete = "Incomplete"
    """
    The entry exists and is partially filled in, but it does not yet meet the quality bar established for Usable entries.
    """
    Obsolete = "Obsolete"
    """
    The entry is obsolete and is no longer recommended for use but has not been formally deprecated.
    """
    Stable = "Stable"
    """
    The entry is stable and unlikely to undergo significant changes unless new information or research warrants it.
    """
    Usable = "Usable"
    """
    The entry is complete enough to be used in product documentation, assessments, tools, and mapping exercises without significant risk.
    """


class TaxonomyMappingFitEnum(str, Enum):
    """
    The different values used to describe how closely a mapping between CAPEC and an external taxonomy aligns.
    """
    Exact = "Exact"
    """
    The CAPEC entry and the external taxonomy entry are an exact match in scope and meaning.
    """
    CAPEC_More_Abstract = "CAPEC More Abstract"
    """
    The CAPEC entry is more abstract (broader) than the mapped external taxonomy entry.
    """
    CAPEC_More_Specific = "CAPEC More Specific"
    """
    The CAPEC entry is more specific (narrower) than the mapped external taxonomy entry.
    """
    Imprecise = "Imprecise"
    """
    The mapping between CAPEC and the external taxonomy entry is approximate or imprecise.
    """
    Perspective = "Perspective"
    """
    The CAPEC entry and the external taxonomy entry represent different perspectives on the same concept.
    """


class TaxonomyNameEnum(str, Enum):
    """
    The different known taxonomies to which CAPEC entries can be mapped.
    """
    ATTACK = "ATTACK"
    """
    The MITRE ATT&CK framework, a globally-accessible knowledge base of adversary tactics and techniques.
    """
    WASC = "WASC"
    """
    The Web Application Security Consortium (WASC) Threat Classification taxonomy.
    """
    OWASP_Attacks = "OWASP Attacks"
    """
    The OWASP (Open Web Application Security Project) Attacks taxonomy.
    """


class TechnicalImpactEnum(str, Enum):
    """
    The different negative technical impacts that can result from a successful attack
leveraging a given attack pattern. A negative technical impact is the specific
technical effect of successfully violating a reasonable security policy for the
system or network.
    """
    Modify_Data = "Modify Data"
    """
    The attacker can modify data stored within or processed by the target system.
    """
    Read_Data = "Read Data"
    """
    The attacker can read sensitive or confidential data from the target system.
    """
    Unreliable_Execution = "Unreliable Execution"
    """
    The execution of the target system becomes unreliable or unpredictable.
    """
    Resource_Consumption = "Resource Consumption"
    """
    Target system resources (CPU, memory, bandwidth) are consumed by the attack.
    """
    Execute_Unauthorized_Commands = "Execute Unauthorized Commands"
    """
    The attacker can execute unauthorized commands or code on the target system.
    """
    Gain_Privileges = "Gain Privileges"
    """
    The attacker gains elevated or unauthorized privileges on the target system.
    """
    Bypass_Protection_Mechanism = "Bypass Protection Mechanism"
    """
    The attacker can bypass existing security controls or protection mechanisms.
    """
    Hide_Activities = "Hide Activities"
    """
    The attacker can conceal malicious activities from detection and monitoring.
    """
    Alter_Execution_Logic = "Alter Execution Logic"
    """
    The attacker can alter the normal execution logic or control flow of the target system.
    """
    Other = "Other"
    """
    Other technical impact not covered by the defined categories.
    """


class ViewTypeEnum(str, Enum):
    """
    The different types of views that can be found within CAPEC. A graph is a
hierarchical representation of attack patterns based on a specific vantage point.
An explicit slice is a subset of attack patterns related through some external
factor. An implicit slice is a subset of attack patterns related through a specific
attribute.
    """
    Implicit = "Implicit"
    """
    A subset of attack patterns that are related through a specific attribute. For
    example, a slice may refer to all attack patterns in draft status, or all existing
    meta attack patterns. Members are defined by the Filter element (an XSL query).
    """
    Explicit = "Explicit"
    """
    A subset of attack patterns that are related through some external factor. For
    example, a view may represent mappings to external groupings like a Top-N list.
    Members are defined externally through Member_Of relationships.
    """
    Graph = "Graph"
    """
    A hierarchical representation of attack patterns based on a specific vantage point
    that a user may take. The hierarchy often starts with a category, followed by a
    meta/standard attack pattern, and ends with a detailed attack pattern. Members are
    defined through Member_Of relationships on categories.
    """



class AttackPatternCatalog(ConfiguredBaseModel):
    """
    The root element used to hold an enumerated catalog of common attack patterns.
    Each catalog can be organized by optional Views and Categories. The catalog also
    contains a list of all External_References that may be shared throughout the
    individual attack patterns. The required Name and Version attributes are used to
    uniquely identify the catalog. The required Date attribute identifies the date when
    this catalog was created or last updated.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'annotations': {'view_export_note': {'tag': 'view_export_note',
                                              'value': 'View-filtered catalog exports '
                                                       'follow the naming convention '
                                                       '"VIEW LIST: CAPEC-{ID}: '
                                                       '{Name}" in the Name attribute. '
                                                       'These exports are '
                                                       'self-contained: they include '
                                                       'the relevant Attack_Patterns, '
                                                       'exactly one View entry (the '
                                                       'view being exported), the '
                                                       'External_References cited by '
                                                       'those patterns, and — when '
                                                       'applicable — the Categories '
                                                       'that are part of the view. '
                                                       'Source files for navigation '
                                                       'hierarchies, '
                                                       'abstraction/status slices, '
                                                       'thematic views, and vendor '
                                                       'taxonomy mappings reside in '
                                                       'tests/data/capec/navigation/, '
                                                       'tests/data/capec/views/, and '
                                                       'src/capec/mappings/ '
                                                       'respectively.'},
                         'xsd_constraint': {'tag': 'xsd_constraint',
                                            'value': 'uniqueAttackPatternID on '
                                                     'Attack_Patterns/Attack_Pattern/@ID; '
                                                     'uniqueCategoryID on '
                                                     'Categories/Category/@ID; '
                                                     'uniqueViewID on Views/View/@ID; '
                                                     'uniqueReferenceID on '
                                                     'External_References/External_Reference/@Reference_ID'},
                         'xsd_element': {'tag': 'xsd_element',
                                         'value': 'Attack_Pattern_Catalog'}},
         'from_schema': 'https://w3id.org/lmodel/capec',
         'in_subset': ['catalog_entries'],
         'slot_usage': {'attack_patterns': {'annotations': {'xsd_element': {'tag': 'xsd_element',
                                                                            'value': 'Attack_Patterns/Attack_Pattern'}},
                                            'description': 'The collection of attack '
                                                           'patterns defined in this '
                                                           'catalog.',
                                            'inlined_as_list': True,
                                            'multivalued': True,
                                            'name': 'attack_patterns',
                                            'range': 'AttackPattern'},
                        'categories': {'annotations': {'xsd_element': {'tag': 'xsd_element',
                                                                       'value': 'Categories/Category'}},
                                       'description': 'The collection of categories '
                                                      'organizing attack patterns in '
                                                      'this catalog.',
                                       'inlined_as_list': True,
                                       'multivalued': True,
                                       'name': 'categories',
                                       'range': 'Category'},
                        'entry_date': {'annotations': {'xsd_attribute': {'tag': 'xsd_attribute',
                                                                         'value': 'Date'},
                                                       'xsd_type': {'tag': 'xsd_type',
                                                                    'value': 'xs:date'}},
                                       'description': 'The date when this catalog was '
                                                      'created or last updated.',
                                       'name': 'entry_date',
                                       'range': 'date',
                                       'required': True},
                        'external_references': {'annotations': {'xsd_element': {'tag': 'xsd_element',
                                                                                'value': 'External_References/External_Reference'}},
                                                'description': 'The collection of '
                                                               'external references '
                                                               'shared throughout the '
                                                               'catalog entries.',
                                                'inlined_as_list': True,
                                                'multivalued': True,
                                                'name': 'external_references',
                                                'range': 'ExternalReference'},
                        'name': {'annotations': {'xsd_attribute': {'tag': 'xsd_attribute',
                                                                   'value': 'Name'}},
                                 'description': 'The name of this catalog, used to '
                                                'uniquely identify it.',
                                 'name': 'name',
                                 'range': 'string',
                                 'required': True},
                        'version': {'annotations': {'xsd_attribute': {'tag': 'xsd_attribute',
                                                                      'value': 'Version'}},
                                    'description': 'The version of this catalog, used '
                                                   'to uniquely identify it.',
                                    'name': 'version',
                                    'range': 'string',
                                    'required': True},
                        'views': {'annotations': {'xsd_element': {'tag': 'xsd_element',
                                                                  'value': 'Views/View'}},
                                  'description': 'The collection of views providing '
                                                 'perspectives on the attack pattern '
                                                 'catalog.',
                                  'inlined_as_list': True,
                                  'multivalued': True,
                                  'name': 'views',
                                  'range': 'View'}},
         'tree_root': True})

    name: str = Field(default=..., description="""The name of this catalog, used to uniquely identify it.""", json_schema_extra = { "linkml_meta": {'annotations': {'xsd_attribute': {'tag': 'xsd_attribute', 'value': 'Name'}},
         'domain_of': ['AttackPatternCatalog',
                       'AttackPattern',
                       'Category',
                       'View',
                       'PreviousEntryName']} })
    version: str = Field(default=..., description="""The version of this catalog, used to uniquely identify it.""", json_schema_extra = { "linkml_meta": {'annotations': {'xsd_attribute': {'tag': 'xsd_attribute', 'value': 'Version'}},
         'domain_of': ['AttackPatternCatalog']} })
    entry_date: date = Field(default=..., description="""The date when this catalog was created or last updated.""", json_schema_extra = { "linkml_meta": {'annotations': {'xsd_attribute': {'tag': 'xsd_attribute', 'value': 'Date'},
                         'xsd_type': {'tag': 'xsd_type', 'value': 'xs:date'}},
         'domain_of': ['AttackPatternCatalog', 'PreviousEntryName']} })
    attack_patterns: Optional[list[AttackPattern]] = Field(default=None, description="""The collection of attack patterns defined in this catalog.""", json_schema_extra = { "linkml_meta": {'annotations': {'xsd_element': {'tag': 'xsd_element',
                                         'value': 'Attack_Patterns/Attack_Pattern'}},
         'domain_of': ['AttackPatternCatalog']} })
    categories: Optional[list[Category]] = Field(default=None, description="""The collection of categories organizing attack patterns in this catalog.""", json_schema_extra = { "linkml_meta": {'annotations': {'xsd_element': {'tag': 'xsd_element',
                                         'value': 'Categories/Category'}},
         'domain_of': ['AttackPatternCatalog']} })
    views: Optional[list[View]] = Field(default=None, description="""The collection of views providing perspectives on the attack pattern catalog.""", json_schema_extra = { "linkml_meta": {'annotations': {'xsd_element': {'tag': 'xsd_element', 'value': 'Views/View'}},
         'domain_of': ['AttackPatternCatalog']} })
    external_references: Optional[list[ExternalReference]] = Field(default=None, description="""The collection of external references shared throughout the catalog entries.""", json_schema_extra = { "linkml_meta": {'annotations': {'xsd_element': {'tag': 'xsd_element',
                                         'value': 'External_References/External_Reference'}},
         'domain_of': ['AttackPatternCatalog']} })


class AttackPattern(ConfiguredBaseModel):
    """
    An attack pattern is an abstraction mechanism for helping describe how an attack is
    executed. Each pattern defines a challenge that an attacker may face, provides a
    description of the common technique(s) used to meet the challenge, and presents
    recommended methods for mitigating an actual attack. Attack patterns help categorize
    attacks in a meaningful way in an effort to provide a coherent way of teaching
    designers and developers how their systems may be attacked and how they can effectively
    defend them.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'annotations': {'description_note': {'tag': 'description_note',
                                              'value': 'The required Description '
                                                       'element represents a high '
                                                       'level description of the '
                                                       'attack pattern (no longer than '
                                                       'a few sentences). The optional '
                                                       'Extended_Description element '
                                                       'provides additional details. '
                                                       'Typical_Severity and '
                                                       'Likelihood_Of_Attack capture '
                                                       'average values with the '
                                                       'understanding they will not be '
                                                       'accurate for all attacks.'},
                         'xsd_type': {'tag': 'xsd_type', 'value': 'AttackPatternType'}},
         'close_mappings': ['stix:attack-pattern'],
         'from_schema': 'https://w3id.org/lmodel/capec',
         'in_subset': ['catalog_entries'],
         'related_mappings': ['attack:Technique', 'wasc:Threat', 'owasp:Attack'],
         'slot_usage': {'abstraction': {'annotations': {'xsd_attribute': {'tag': 'xsd_attribute',
                                                                          'value': 'Abstraction'}},
                                        'description': 'The abstraction level for this '
                                                       'attack pattern. Defines '
                                                       'whether this is a Meta, '
                                                       'Standard, or Detailed level '
                                                       'pattern.',
                                        'name': 'abstraction',
                                        'range': 'AbstractionEnum',
                                        'required': True},
                        'alternate_terms': {'annotations': {'xsd_element': {'tag': 'xsd_element',
                                                                            'value': 'Alternate_Terms/Alternate_Term'},
                                                            'xsd_type': {'tag': 'xsd_type',
                                                                         'value': 'AlternateTermsType'}},
                                            'description': 'One or more other names by '
                                                           'which this attack pattern '
                                                           'may be known.',
                                            'inlined_as_list': True,
                                            'multivalued': True,
                                            'name': 'alternate_terms',
                                            'range': 'AlternateTerm'},
                        'consequences': {'annotations': {'xsd_element': {'tag': 'xsd_element',
                                                                         'value': 'Consequences/Consequence'},
                                                         'xsd_type': {'tag': 'xsd_type',
                                                                      'value': 'ConsequencesType'}},
                                         'description': 'Individual consequences '
                                                        'associated with this attack '
                                                        'pattern, specifying the '
                                                        'security properties violated, '
                                                        'technical impacts, and '
                                                        'likelihoods.',
                                         'inlined_as_list': True,
                                         'multivalued': True,
                                         'name': 'consequences',
                                         'range': 'Consequence'},
                        'description': {'annotations': {'xsd_element': {'tag': 'xsd_element',
                                                                        'value': 'Description'},
                                                        'xsd_type': {'tag': 'xsd_type',
                                                                     'value': 'StructuredTextType'}},
                                        'description': 'A high level description of '
                                                       'the attack pattern. The '
                                                       'description should be no\n'
                                                       'longer than a few sentences '
                                                       'and should include how '
                                                       'malicious input is initially\n'
                                                       'supplied, the weakness being '
                                                       'exploited, and the resulting '
                                                       'negative technical\n'
                                                       'impact. A full step-by-step '
                                                       'description belongs in the '
                                                       'Execution_Flow element.',
                                        'name': 'description',
                                        'range': 'StructuredText',
                                        'required': True},
                        'example_instances': {'annotations': {'xsd_element': {'tag': 'xsd_element',
                                                                              'value': 'Example_Instances/Example'},
                                                              'xsd_type': {'tag': 'xsd_type',
                                                                           'value': 'ExampleInstancesType'}},
                                              'description': 'One or more concrete '
                                                             'example instances of '
                                                             'this attack pattern to '
                                                             'help the reader '
                                                             'understand its nature, '
                                                             'context, and variability '
                                                             'in practical terms.',
                                              'multivalued': True,
                                              'name': 'example_instances',
                                              'range': 'StructuredText'},
                        'execution_flow': {'annotations': {'xsd_element': {'tag': 'xsd_element',
                                                                           'value': 'Execution_Flow/Attack_Step'},
                                                           'xsd_type': {'tag': 'xsd_type',
                                                                        'value': 'ExecutionFlowType'}},
                                           'description': 'A detailed step-by-step '
                                                          'flow of the attack pattern, '
                                                          'listing the typical steps '
                                                          'performed by an adversary '
                                                          'when leveraging the given '
                                                          'technique. Usually only '
                                                          'applicable to Detailed '
                                                          'abstraction level attack '
                                                          'patterns.',
                                           'inlined_as_list': True,
                                           'multivalued': True,
                                           'name': 'execution_flow',
                                           'range': 'AttackStep'},
                        'extended_description': {'annotations': {'xsd_element': {'tag': 'xsd_element',
                                                                                 'value': 'Extended_Description'},
                                                                 'xsd_type': {'tag': 'xsd_type',
                                                                              'value': 'StructuredTextType'}},
                                                 'description': 'Additional details '
                                                                'important to this '
                                                                'attack pattern beyond '
                                                                'what is conveyed in '
                                                                'the main description, '
                                                                'but not necessary to '
                                                                'understand the '
                                                                'fundamental concept.',
                                                 'name': 'extended_description',
                                                 'range': 'StructuredText'},
                        'indicators': {'annotations': {'xsd_element': {'tag': 'xsd_element',
                                                                       'value': 'Indicators/Indicator'},
                                                       'xsd_type': {'tag': 'xsd_type',
                                                                    'value': 'IndicatorsType'}},
                                       'description': 'Activities, events, conditions '
                                                      'or behaviors that may indicate '
                                                      'that an attack leveraging this '
                                                      'pattern is imminent, in '
                                                      'progress, or has occurred.',
                                       'multivalued': True,
                                       'name': 'indicators',
                                       'range': 'StructuredText'},
                        'likelihood_of_attack': {'annotations': {'xsd_element': {'tag': 'xsd_element',
                                                                                 'value': 'Likelihood_Of_Attack'},
                                                                 'xsd_type': {'tag': 'xsd_type',
                                                                              'value': 'LikelihoodEnumeration'}},
                                                 'description': 'An overall average '
                                                                'likelihood value for '
                                                                'attacks that leverage '
                                                                'this attack pattern, '
                                                                'with the '
                                                                'understanding that it '
                                                                'will not be '
                                                                'completely accurate '
                                                                'for all attacks.',
                                                 'name': 'likelihood_of_attack',
                                                 'range': 'LikelihoodEnum'},
                        'mitigations': {'annotations': {'xsd_element': {'tag': 'xsd_element',
                                                                        'value': 'Mitigations/Mitigation'},
                                                        'xsd_type': {'tag': 'xsd_type',
                                                                     'value': 'MitigationsType'}},
                                        'description': 'Actions or approaches to '
                                                       'prevent or mitigate the risk '
                                                       'of an attack that leverages '
                                                       'this attack pattern, aimed at '
                                                       'improving system resiliency, '
                                                       'reducing attack surface, or '
                                                       'reducing impact.',
                                        'multivalued': True,
                                        'name': 'mitigations',
                                        'range': 'StructuredText'},
                        'prerequisites': {'annotations': {'xsd_element': {'tag': 'xsd_element',
                                                                          'value': 'Prerequisites/Prerequisite'},
                                                          'xsd_type': {'tag': 'xsd_type',
                                                                       'value': 'PrerequisitesType'}},
                                          'description': 'The conditions that must '
                                                         'exist in order for an attack '
                                                         'leveraging this pattern to '
                                                         'succeed.',
                                          'multivalued': True,
                                          'name': 'prerequisites',
                                          'range': 'StructuredText'},
                        'related_attack_patterns': {'annotations': {'xsd_element': {'tag': 'xsd_element',
                                                                                    'value': 'Related_Attack_Patterns/Related_Attack_Pattern'},
                                                                    'xsd_type': {'tag': 'xsd_type',
                                                                                 'value': 'RelatedAttackPatternType'}},
                                                    'description': 'References to '
                                                                   'other attack '
                                                                   'patterns that give '
                                                                   'insight to similar '
                                                                   'items at higher '
                                                                   'and lower levels '
                                                                   'of abstraction.',
                                                    'inlined_as_list': True,
                                                    'multivalued': True,
                                                    'name': 'related_attack_patterns',
                                                    'range': 'RelatedAttackPattern'},
                        'related_weaknesses': {'annotations': {'xsd_element': {'tag': 'xsd_element',
                                                                               'value': 'Related_Weaknesses/Related_Weakness'},
                                                               'xsd_type': {'tag': 'xsd_type',
                                                                            'value': 'RelatedWeaknessesType'}},
                                               'description': 'References to CWE '
                                                              'weaknesses associated '
                                                              'with this attack '
                                                              'pattern. Any of the '
                                                              'weaknesses (not '
                                                              'necessarily all) may be '
                                                              'present for the attack '
                                                              'to be successful.',
                                               'inlined_as_list': True,
                                               'multivalued': True,
                                               'name': 'related_weaknesses',
                                               'range': 'integer'},
                        'resources_required': {'annotations': {'xsd_element': {'tag': 'xsd_element',
                                                                               'value': 'Resources_Required/Resource'},
                                                               'xsd_type': {'tag': 'xsd_type',
                                                                            'value': 'RequiredResourcesType'}},
                                               'description': 'The resources (e.g., '
                                                              'CPU cycles, IP '
                                                              'addresses, tools) '
                                                              'required by an '
                                                              'adversary to '
                                                              'effectively execute '
                                                              'this type of attack.',
                                               'multivalued': True,
                                               'name': 'resources_required',
                                               'range': 'StructuredText'},
                        'skills_required': {'annotations': {'xsd_element': {'tag': 'xsd_element',
                                                                            'value': 'Skills_Required/Skill'},
                                                            'xsd_type': {'tag': 'xsd_type',
                                                                         'value': 'SkillsType'}},
                                            'description': 'The level of skills or '
                                                           'specific knowledge needed '
                                                           'by an adversary to execute '
                                                           'this type of attack.',
                                            'inlined_as_list': True,
                                            'multivalued': True,
                                            'name': 'skills_required',
                                            'range': 'Skill'},
                        'typical_severity': {'annotations': {'xsd_element': {'tag': 'xsd_element',
                                                                             'value': 'Typical_Severity'},
                                                             'xsd_type': {'tag': 'xsd_type',
                                                                          'value': 'SeverityEnumeration'}},
                                             'description': 'An overall average '
                                                            'severity value for '
                                                            'attacks that leverage '
                                                            'this attack pattern, with '
                                                            'the understanding that it '
                                                            'will not be completely '
                                                            'accurate for all attacks.',
                                             'name': 'typical_severity',
                                             'range': 'SeverityEnum'}}})

    id: int = Field(default=..., description="""Unique integer identifier for the entry. Considered static for the lifetime of the entry. If an entry becomes deprecated, the identifier is not reused and a placeholder is left in the catalog.""", json_schema_extra = { "linkml_meta": {'annotations': {'xsd_attribute': {'tag': 'xsd_attribute', 'value': 'ID'},
                         'xsd_type': {'tag': 'xsd_type', 'value': 'xs:integer'}},
         'domain_of': ['AttackPattern', 'Category', 'View']} })
    name: str = Field(default=..., description="""Descriptive title used to give the reader an idea of what the entry represents. All words in the name should be capitalized except for articles and prepositions unless they begin or end the name.""", json_schema_extra = { "linkml_meta": {'annotations': {'xsd_attribute': {'tag': 'xsd_attribute', 'value': 'Name'}},
         'domain_of': ['AttackPatternCatalog',
                       'AttackPattern',
                       'Category',
                       'View',
                       'PreviousEntryName']} })
    status: StatusEnum = Field(default=..., description="""The development and usage status level for this entry. Please refer to the StatusEnum enumeration for a list of valid values and their meanings.""", json_schema_extra = { "linkml_meta": {'annotations': {'xsd_attribute': {'tag': 'xsd_attribute', 'value': 'Status'}},
         'domain_of': ['AttackPattern', 'Category', 'View']} })
    description: str = Field(default=..., description="""A high level description of the attack pattern. The description should be no
longer than a few sentences and should include how malicious input is initially
supplied, the weakness being exploited, and the resulting negative technical
impact. A full step-by-step description belongs in the Execution_Flow element.""", json_schema_extra = { "linkml_meta": {'annotations': {'xsd_element': {'tag': 'xsd_element', 'value': 'Description'},
                         'xsd_type': {'tag': 'xsd_type',
                                      'value': 'StructuredTextType'}},
         'domain_of': ['AttackPattern',
                       'AlternateTerm',
                       'Skill',
                       'AttackStep',
                       'Technique',
                       'Stakeholder']} })
    notes: Optional[list[Note]] = Field(default=None, description="""Additional comments and notes about this entry that cannot be captured using the other available elements.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AttackPattern', 'Category', 'View']} })
    content_history: Optional[ContentHistory] = Field(default=None, description="""Tracks the original author of this entry and any subsequent modifications to the content, providing a means of contacting authors and modifiers.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AttackPattern', 'Category', 'View']} })
    references: Optional[list[Reference]] = Field(default=None, description="""Links to external references for further reading and insight into this entry. Should be used when the entry is based on external sources or projects.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AttackPattern', 'Category', 'View']} })
    taxonomy_mappings: Optional[list[TaxonomyMapping]] = Field(default=None, description="""Mappings from this entry to equivalent or related entries in taxonomies outside of CAPEC, such as ATT&CK, WASC, or OWASP Attacks.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AttackPattern', 'Category']} })
    abstraction: AbstractionEnum = Field(default=..., description="""The abstraction level for this attack pattern. Defines whether this is a Meta, Standard, or Detailed level pattern.""", json_schema_extra = { "linkml_meta": {'annotations': {'xsd_attribute': {'tag': 'xsd_attribute',
                                           'value': 'Abstraction'}},
         'domain_of': ['AttackPattern']} })
    extended_description: Optional[str] = Field(default=None, description="""Additional details important to this attack pattern beyond what is conveyed in the main description, but not necessary to understand the fundamental concept.""", json_schema_extra = { "linkml_meta": {'annotations': {'xsd_element': {'tag': 'xsd_element',
                                         'value': 'Extended_Description'},
                         'xsd_type': {'tag': 'xsd_type',
                                      'value': 'StructuredTextType'}},
         'domain_of': ['AttackPattern']} })
    alternate_terms: Optional[list[AlternateTerm]] = Field(default=None, description="""One or more other names by which this attack pattern may be known.""", json_schema_extra = { "linkml_meta": {'annotations': {'xsd_element': {'tag': 'xsd_element',
                                         'value': 'Alternate_Terms/Alternate_Term'},
                         'xsd_type': {'tag': 'xsd_type',
                                      'value': 'AlternateTermsType'}},
         'domain_of': ['AttackPattern']} })
    likelihood_of_attack: Optional[LikelihoodEnum] = Field(default=None, description="""An overall average likelihood value for attacks that leverage this attack pattern, with the understanding that it will not be completely accurate for all attacks.""", json_schema_extra = { "linkml_meta": {'annotations': {'xsd_element': {'tag': 'xsd_element',
                                         'value': 'Likelihood_Of_Attack'},
                         'xsd_type': {'tag': 'xsd_type',
                                      'value': 'LikelihoodEnumeration'}},
         'domain_of': ['AttackPattern']} })
    typical_severity: Optional[SeverityEnum] = Field(default=None, description="""An overall average severity value for attacks that leverage this attack pattern, with the understanding that it will not be completely accurate for all attacks.""", json_schema_extra = { "linkml_meta": {'annotations': {'xsd_element': {'tag': 'xsd_element',
                                         'value': 'Typical_Severity'},
                         'xsd_type': {'tag': 'xsd_type',
                                      'value': 'SeverityEnumeration'}},
         'domain_of': ['AttackPattern']} })
    related_attack_patterns: Optional[list[RelatedAttackPattern]] = Field(default=None, description="""References to other attack patterns that give insight to similar items at higher and lower levels of abstraction.""", json_schema_extra = { "linkml_meta": {'annotations': {'xsd_element': {'tag': 'xsd_element',
                                         'value': 'Related_Attack_Patterns/Related_Attack_Pattern'},
                         'xsd_type': {'tag': 'xsd_type',
                                      'value': 'RelatedAttackPatternType'}},
         'domain_of': ['AttackPattern']} })
    execution_flow: Optional[list[AttackStep]] = Field(default=None, description="""A detailed step-by-step flow of the attack pattern, listing the typical steps performed by an adversary when leveraging the given technique. Usually only applicable to Detailed abstraction level attack patterns.""", json_schema_extra = { "linkml_meta": {'annotations': {'xsd_element': {'tag': 'xsd_element',
                                         'value': 'Execution_Flow/Attack_Step'},
                         'xsd_type': {'tag': 'xsd_type', 'value': 'ExecutionFlowType'}},
         'domain_of': ['AttackPattern']} })
    prerequisites: Optional[list[str]] = Field(default=None, description="""The conditions that must exist in order for an attack leveraging this pattern to succeed.""", json_schema_extra = { "linkml_meta": {'annotations': {'xsd_element': {'tag': 'xsd_element',
                                         'value': 'Prerequisites/Prerequisite'},
                         'xsd_type': {'tag': 'xsd_type', 'value': 'PrerequisitesType'}},
         'domain_of': ['AttackPattern']} })
    skills_required: Optional[list[Skill]] = Field(default=None, description="""The level of skills or specific knowledge needed by an adversary to execute this type of attack.""", json_schema_extra = { "linkml_meta": {'annotations': {'xsd_element': {'tag': 'xsd_element',
                                         'value': 'Skills_Required/Skill'},
                         'xsd_type': {'tag': 'xsd_type', 'value': 'SkillsType'}},
         'domain_of': ['AttackPattern']} })
    resources_required: Optional[list[str]] = Field(default=None, description="""The resources (e.g., CPU cycles, IP addresses, tools) required by an adversary to effectively execute this type of attack.""", json_schema_extra = { "linkml_meta": {'annotations': {'xsd_element': {'tag': 'xsd_element',
                                         'value': 'Resources_Required/Resource'},
                         'xsd_type': {'tag': 'xsd_type',
                                      'value': 'RequiredResourcesType'}},
         'domain_of': ['AttackPattern']} })
    indicators: Optional[list[str]] = Field(default=None, description="""Activities, events, conditions or behaviors that may indicate that an attack leveraging this pattern is imminent, in progress, or has occurred.""", json_schema_extra = { "linkml_meta": {'annotations': {'xsd_element': {'tag': 'xsd_element',
                                         'value': 'Indicators/Indicator'},
                         'xsd_type': {'tag': 'xsd_type', 'value': 'IndicatorsType'}},
         'domain_of': ['AttackPattern']} })
    consequences: Optional[list[Consequence]] = Field(default=None, description="""Individual consequences associated with this attack pattern, specifying the security properties violated, technical impacts, and likelihoods.""", json_schema_extra = { "linkml_meta": {'annotations': {'xsd_element': {'tag': 'xsd_element',
                                         'value': 'Consequences/Consequence'},
                         'xsd_type': {'tag': 'xsd_type', 'value': 'ConsequencesType'}},
         'domain_of': ['AttackPattern']} })
    mitigations: Optional[list[str]] = Field(default=None, description="""Actions or approaches to prevent or mitigate the risk of an attack that leverages this attack pattern, aimed at improving system resiliency, reducing attack surface, or reducing impact.""", json_schema_extra = { "linkml_meta": {'annotations': {'xsd_element': {'tag': 'xsd_element',
                                         'value': 'Mitigations/Mitigation'},
                         'xsd_type': {'tag': 'xsd_type', 'value': 'MitigationsType'}},
         'domain_of': ['AttackPattern']} })
    example_instances: Optional[list[str]] = Field(default=None, description="""One or more concrete example instances of this attack pattern to help the reader understand its nature, context, and variability in practical terms.""", json_schema_extra = { "linkml_meta": {'annotations': {'xsd_element': {'tag': 'xsd_element',
                                         'value': 'Example_Instances/Example'},
                         'xsd_type': {'tag': 'xsd_type',
                                      'value': 'ExampleInstancesType'}},
         'domain_of': ['AttackPattern']} })
    related_weaknesses: Optional[list[int]] = Field(default=None, description="""References to CWE weaknesses associated with this attack pattern. Any of the weaknesses (not necessarily all) may be present for the attack to be successful.""", json_schema_extra = { "linkml_meta": {'annotations': {'xsd_element': {'tag': 'xsd_element',
                                         'value': 'Related_Weaknesses/Related_Weakness'},
                         'xsd_type': {'tag': 'xsd_type',
                                      'value': 'RelatedWeaknessesType'}},
         'domain_of': ['AttackPattern']} })


class Category(ConfiguredBaseModel):
    """
    A category in CAPEC is a collection of attack patterns based on some common
    characteristic. More specifically, it is an aggregation of attack patterns based on
    effect/intent (as opposed to actions or mechanisms, which would be a meta attack
    pattern). An aggregation based on effect/intent is not an actionable attack and as
    such is not a pattern of attack behavior. Rather, it is a grouping of patterns based
    on some common criteria.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'annotations': {'xsd_type': {'tag': 'xsd_type', 'value': 'CategoryType'}},
         'from_schema': 'https://w3id.org/lmodel/capec',
         'in_subset': ['catalog_entries'],
         'slot_usage': {'relationships': {'annotations': {'xsd_element': {'tag': 'xsd_element',
                                                                          'value': 'Relationships'},
                                                          'xsd_type': {'tag': 'xsd_type',
                                                                       'value': 'RelationshipsType'}},
                                          'description': 'Relationships of this '
                                                         'category with attack '
                                                         'patterns, other categories, '
                                                         'and views, including '
                                                         'Member_Of and Has_Member '
                                                         'relationships.',
                                          'inlined': True,
                                          'name': 'relationships',
                                          'range': 'Relationships'},
                        'summary': {'annotations': {'xsd_element': {'tag': 'xsd_element',
                                                                    'value': 'Summary'},
                                                    'xsd_type': {'tag': 'xsd_type',
                                                                 'value': 'StructuredTextType'}},
                                    'description': 'A short summary limited to the key '
                                                   'points that define this category.',
                                    'name': 'summary',
                                    'range': 'StructuredText',
                                    'required': True}}})

    id: int = Field(default=..., description="""Unique integer identifier for the entry. Considered static for the lifetime of the entry. If an entry becomes deprecated, the identifier is not reused and a placeholder is left in the catalog.""", json_schema_extra = { "linkml_meta": {'annotations': {'xsd_attribute': {'tag': 'xsd_attribute', 'value': 'ID'},
                         'xsd_type': {'tag': 'xsd_type', 'value': 'xs:integer'}},
         'domain_of': ['AttackPattern', 'Category', 'View']} })
    name: str = Field(default=..., description="""Descriptive title used to give the reader an idea of what the entry represents. All words in the name should be capitalized except for articles and prepositions unless they begin or end the name.""", json_schema_extra = { "linkml_meta": {'annotations': {'xsd_attribute': {'tag': 'xsd_attribute', 'value': 'Name'}},
         'domain_of': ['AttackPatternCatalog',
                       'AttackPattern',
                       'Category',
                       'View',
                       'PreviousEntryName']} })
    status: StatusEnum = Field(default=..., description="""The development and usage status level for this entry. Please refer to the StatusEnum enumeration for a list of valid values and their meanings.""", json_schema_extra = { "linkml_meta": {'annotations': {'xsd_attribute': {'tag': 'xsd_attribute', 'value': 'Status'}},
         'domain_of': ['AttackPattern', 'Category', 'View']} })
    notes: Optional[list[Note]] = Field(default=None, description="""Additional comments and notes about this entry that cannot be captured using the other available elements.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AttackPattern', 'Category', 'View']} })
    content_history: Optional[ContentHistory] = Field(default=None, description="""Tracks the original author of this entry and any subsequent modifications to the content, providing a means of contacting authors and modifiers.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AttackPattern', 'Category', 'View']} })
    references: Optional[list[Reference]] = Field(default=None, description="""Links to external references for further reading and insight into this entry. Should be used when the entry is based on external sources or projects.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AttackPattern', 'Category', 'View']} })
    taxonomy_mappings: Optional[list[TaxonomyMapping]] = Field(default=None, description="""Mappings from this entry to equivalent or related entries in taxonomies outside of CAPEC, such as ATT&CK, WASC, or OWASP Attacks.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AttackPattern', 'Category']} })
    summary: str = Field(default=..., description="""A short summary limited to the key points that define this category.""", json_schema_extra = { "linkml_meta": {'annotations': {'xsd_element': {'tag': 'xsd_element', 'value': 'Summary'},
                         'xsd_type': {'tag': 'xsd_type',
                                      'value': 'StructuredTextType'}},
         'domain_of': ['Category']} })
    relationships: Optional[Relationships] = Field(default=None, description="""Relationships of this category with attack patterns, other categories, and views, including Member_Of and Has_Member relationships.""", json_schema_extra = { "linkml_meta": {'annotations': {'xsd_element': {'tag': 'xsd_element',
                                         'value': 'Relationships'},
                         'xsd_type': {'tag': 'xsd_type', 'value': 'RelationshipsType'}},
         'domain_of': ['Category']} })


class View(ConfiguredBaseModel):
    """
    A view in CAPEC represents a perspective with which one might look at the collection
    of attack patterns defined within CAPEC. There are three different types of views as
    defined by the Type attribute: graphs, explicit slices, and implicit slices.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'annotations': {'notes': {'tag': 'notes',
                                   'value': 'Members of a view are either defined '
                                            'externally through Member_Of '
                                            'relationships (for graphs and explicit '
                                            'slices) or by the optional Filter element '
                                            'as an XSL query (for implicit slices).'},
                         'xsd_type': {'tag': 'xsd_type', 'value': 'ViewType'}},
         'from_schema': 'https://w3id.org/lmodel/capec',
         'in_subset': ['catalog_entries'],
         'slot_usage': {'audience': {'annotations': {'xsd_element': {'tag': 'xsd_element',
                                                                     'value': 'Audience/Stakeholder'},
                                                     'xsd_type': {'tag': 'xsd_type',
                                                                  'value': 'AudienceType'}},
                                     'description': 'Reference to the target '
                                                    'stakeholders or groups for whom '
                                                    'this view is most relevant, along '
                                                    'with descriptions of what '
                                                    'properties they may find useful.',
                                     'inlined_as_list': True,
                                     'multivalued': True,
                                     'name': 'audience',
                                     'range': 'Stakeholder'},
                        'filter': {'annotations': {'xsd_element': {'tag': 'xsd_element',
                                                                   'value': 'Filter'},
                                                   'xsd_type': {'tag': 'xsd_type',
                                                                'value': 'xs:string'}},
                                   'description': 'An XSL query used to identify which '
                                                  'attack patterns are members of this '
                                                  'view. Only applicable to implicit '
                                                  'slice view types.',
                                   'name': 'filter',
                                   'range': 'string'},
                        'members': {'annotations': {'xsd_element': {'tag': 'xsd_element',
                                                                    'value': 'Members'},
                                                    'xsd_type': {'tag': 'xsd_type',
                                                                 'value': 'RelationshipsType'}},
                                    'description': 'The members of this view, defined '
                                                   'via Member_Of and Has_Member '
                                                   'relationships (applicable to graph '
                                                   'and explicit slice view types).',
                                    'inlined': True,
                                    'name': 'members',
                                    'range': 'Relationships'},
                        'objective': {'annotations': {'xsd_element': {'tag': 'xsd_element',
                                                                      'value': 'Objective'},
                                                      'xsd_type': {'tag': 'xsd_type',
                                                                   'value': 'StructuredTextType'}},
                                      'description': 'Describes the perspective from '
                                                     'which this view has been '
                                                     'constructed and what purpose it '
                                                     'serves for its intended '
                                                     'audience.',
                                      'name': 'objective',
                                      'range': 'StructuredText',
                                      'required': True},
                        'type': {'annotations': {'xsd_attribute': {'tag': 'xsd_attribute',
                                                                   'value': 'Type'}},
                                 'description': 'Describes how this view is '
                                                'constructed. Please refer to '
                                                'ViewTypeEnum for a list of valid '
                                                'values and their meanings.',
                                 'name': 'type',
                                 'range': 'ViewTypeEnum',
                                 'required': True}}})

    id: int = Field(default=..., description="""Unique integer identifier for the entry. Considered static for the lifetime of the entry. If an entry becomes deprecated, the identifier is not reused and a placeholder is left in the catalog.""", json_schema_extra = { "linkml_meta": {'annotations': {'xsd_attribute': {'tag': 'xsd_attribute', 'value': 'ID'},
                         'xsd_type': {'tag': 'xsd_type', 'value': 'xs:integer'}},
         'domain_of': ['AttackPattern', 'Category', 'View']} })
    name: str = Field(default=..., description="""Descriptive title used to give the reader an idea of what the entry represents. All words in the name should be capitalized except for articles and prepositions unless they begin or end the name.""", json_schema_extra = { "linkml_meta": {'annotations': {'xsd_attribute': {'tag': 'xsd_attribute', 'value': 'Name'}},
         'domain_of': ['AttackPatternCatalog',
                       'AttackPattern',
                       'Category',
                       'View',
                       'PreviousEntryName']} })
    status: StatusEnum = Field(default=..., description="""The development and usage status level for this entry. Please refer to the StatusEnum enumeration for a list of valid values and their meanings.""", json_schema_extra = { "linkml_meta": {'annotations': {'xsd_attribute': {'tag': 'xsd_attribute', 'value': 'Status'}},
         'domain_of': ['AttackPattern', 'Category', 'View']} })
    type: ViewTypeEnum = Field(default=..., description="""Describes how this view is constructed. Please refer to ViewTypeEnum for a list of valid values and their meanings.""", json_schema_extra = { "linkml_meta": {'annotations': {'xsd_attribute': {'tag': 'xsd_attribute', 'value': 'Type'}},
         'domain_of': ['View', 'Note', 'Stakeholder', 'Contribution']} })
    notes: Optional[list[Note]] = Field(default=None, description="""Additional comments and notes about this entry that cannot be captured using the other available elements.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AttackPattern', 'Category', 'View']} })
    content_history: Optional[ContentHistory] = Field(default=None, description="""Tracks the original author of this entry and any subsequent modifications to the content, providing a means of contacting authors and modifiers.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AttackPattern', 'Category', 'View']} })
    references: Optional[list[Reference]] = Field(default=None, description="""Links to external references for further reading and insight into this entry. Should be used when the entry is based on external sources or projects.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AttackPattern', 'Category', 'View']} })
    objective: str = Field(default=..., description="""Describes the perspective from which this view has been constructed and what purpose it serves for its intended audience.""", json_schema_extra = { "linkml_meta": {'annotations': {'xsd_element': {'tag': 'xsd_element', 'value': 'Objective'},
                         'xsd_type': {'tag': 'xsd_type',
                                      'value': 'StructuredTextType'}},
         'domain_of': ['View']} })
    audience: Optional[list[Stakeholder]] = Field(default=None, description="""Reference to the target stakeholders or groups for whom this view is most relevant, along with descriptions of what properties they may find useful.""", json_schema_extra = { "linkml_meta": {'annotations': {'xsd_element': {'tag': 'xsd_element',
                                         'value': 'Audience/Stakeholder'},
                         'xsd_type': {'tag': 'xsd_type', 'value': 'AudienceType'}},
         'domain_of': ['View']} })
    members: Optional[Relationships] = Field(default=None, description="""The members of this view, defined via Member_Of and Has_Member relationships (applicable to graph and explicit slice view types).""", json_schema_extra = { "linkml_meta": {'annotations': {'xsd_element': {'tag': 'xsd_element', 'value': 'Members'},
                         'xsd_type': {'tag': 'xsd_type', 'value': 'RelationshipsType'}},
         'domain_of': ['View']} })
    filter: Optional[str] = Field(default=None, description="""An XSL query used to identify which attack patterns are members of this view. Only applicable to implicit slice view types.""", json_schema_extra = { "linkml_meta": {'annotations': {'xsd_element': {'tag': 'xsd_element', 'value': 'Filter'},
                         'xsd_type': {'tag': 'xsd_type', 'value': 'xs:string'}},
         'domain_of': ['View']} })


class ExternalReference(ConfiguredBaseModel):
    """
    An external reference provides a pointer to where more information and deeper insight
    can be obtained about an attack pattern, category, or view. Examples include research
    papers and excerpts from publications. Not all elements need to be used since some are
    designed for web references and others for book references.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'annotations': {'notes': {'tag': 'notes',
                                   'value': 'The Author and Title elements should be '
                                            'filled in for all references if possible. '
                                            'URL and URL_Date are used for web '
                                            'references. Publication_Year must follow '
                                            'YYYY format; Publication_Month must '
                                            'follow --MM format; Publication_Day must '
                                            'follow ---DD format.'},
                         'xsd_type': {'tag': 'xsd_type',
                                      'value': 'ExternalReferenceType'}},
         'from_schema': 'https://w3id.org/lmodel/capec',
         'in_subset': ['catalog_entries'],
         'slot_usage': {'authors': {'annotations': {'xsd_element': {'tag': 'xsd_element',
                                                                    'value': 'Author'}},
                                    'description': 'The author(s) of the referenced '
                                                   'material.',
                                    'multivalued': True,
                                    'name': 'authors',
                                    'range': 'string'},
                        'edition': {'annotations': {'xsd_element': {'tag': 'xsd_element',
                                                                    'value': 'Edition'}},
                                    'description': 'The edition of the material being '
                                                   'referenced, in the event that '
                                                   'multiple editions of the material '
                                                   'exist.',
                                    'name': 'edition',
                                    'range': 'string'},
                        'publication': {'annotations': {'xsd_element': {'tag': 'xsd_element',
                                                                        'value': 'Publication'}},
                                        'description': 'The name of the magazine, '
                                                       'journal, or other publication '
                                                       'that contains the referenced '
                                                       'material.',
                                        'name': 'publication',
                                        'range': 'string'},
                        'publication_day': {'annotations': {'xsd_element': {'tag': 'xsd_element',
                                                                            'value': 'Publication_Day'},
                                                            'xsd_type': {'tag': 'xsd_type',
                                                                         'value': 'xs:gDay'}},
                                            'description': 'The day of publication of '
                                                           'the referenced material. '
                                                           'Must follow the ---DD '
                                                           'format (xs:gDay).',
                                            'name': 'publication_day',
                                            'range': 'string'},
                        'publication_month': {'annotations': {'xsd_element': {'tag': 'xsd_element',
                                                                              'value': 'Publication_Month'},
                                                              'xsd_type': {'tag': 'xsd_type',
                                                                           'value': 'xs:gMonth'}},
                                              'description': 'The month of publication '
                                                             'of the referenced '
                                                             'material. Must follow '
                                                             'the --MM format '
                                                             '(xs:gMonth).',
                                              'name': 'publication_month',
                                              'range': 'string'},
                        'publication_year': {'annotations': {'xsd_element': {'tag': 'xsd_element',
                                                                             'value': 'Publication_Year'},
                                                             'xsd_type': {'tag': 'xsd_type',
                                                                          'value': 'xs:gYear'}},
                                             'description': 'The year of publication '
                                                            'of the referenced '
                                                            'material. Must follow the '
                                                            'YYYY format (xs:gYear).',
                                             'name': 'publication_year',
                                             'range': 'string'},
                        'publisher': {'annotations': {'xsd_element': {'tag': 'xsd_element',
                                                                      'value': 'Publisher'}},
                                      'description': 'The name of the publisher of the '
                                                     'referenced material.',
                                      'name': 'publisher',
                                      'range': 'string'},
                        'reference_id': {'annotations': {'xsd_attribute': {'tag': 'xsd_attribute',
                                                                           'value': 'Reference_ID'}},
                                         'description': 'A globally unique identifier '
                                                        'for this external reference '
                                                        '(e.g., REF-1). Used by other '
                                                        'entries to link to this '
                                                        'reference using formats like '
                                                        '[REF-1].',
                                         'identifier': True,
                                         'name': 'reference_id',
                                         'range': 'string',
                                         'required': True},
                        'title': {'annotations': {'xsd_element': {'tag': 'xsd_element',
                                                                  'value': 'Title'}},
                                  'description': 'The title of the referenced '
                                                 'material.',
                                  'name': 'title',
                                  'range': 'string',
                                  'required': True},
                        'url': {'annotations': {'xsd_element': {'tag': 'xsd_element',
                                                                'value': 'URL'},
                                                'xsd_type': {'tag': 'xsd_type',
                                                             'value': 'xs:anyURI'}},
                                'description': 'A URL for the material being '
                                               'referenced, if one exists online.',
                                'name': 'url',
                                'range': 'Uri'},
                        'url_date': {'annotations': {'xsd_element': {'tag': 'xsd_element',
                                                                     'value': 'URL_Date'},
                                                     'xsd_type': {'tag': 'xsd_type',
                                                                  'value': 'xs:date'}},
                                     'description': 'The date when the URL was '
                                                    'validated to be accessible and '
                                                    'correct.',
                                     'name': 'url_date',
                                     'range': 'date'}}})

    reference_id: str = Field(default=..., description="""A globally unique identifier for this external reference (e.g., REF-1). Used by other entries to link to this reference using formats like [REF-1].""", json_schema_extra = { "linkml_meta": {'annotations': {'xsd_attribute': {'tag': 'xsd_attribute',
                                           'value': 'Reference_ID'}},
         'domain_of': ['ExternalReference']} })
    authors: Optional[list[str]] = Field(default=None, description="""The author(s) of the referenced material.""", json_schema_extra = { "linkml_meta": {'annotations': {'xsd_element': {'tag': 'xsd_element', 'value': 'Author'}},
         'domain_of': ['ExternalReference']} })
    title: str = Field(default=..., description="""The title of the referenced material.""", json_schema_extra = { "linkml_meta": {'annotations': {'xsd_element': {'tag': 'xsd_element', 'value': 'Title'}},
         'domain_of': ['ExternalReference']} })
    edition: Optional[str] = Field(default=None, description="""The edition of the material being referenced, in the event that multiple editions of the material exist.""", json_schema_extra = { "linkml_meta": {'annotations': {'xsd_element': {'tag': 'xsd_element', 'value': 'Edition'}},
         'domain_of': ['ExternalReference']} })
    publication: Optional[str] = Field(default=None, description="""The name of the magazine, journal, or other publication that contains the referenced material.""", json_schema_extra = { "linkml_meta": {'annotations': {'xsd_element': {'tag': 'xsd_element', 'value': 'Publication'}},
         'domain_of': ['ExternalReference']} })
    publication_year: Optional[str] = Field(default=None, description="""The year of publication of the referenced material. Must follow the YYYY format (xs:gYear).""", json_schema_extra = { "linkml_meta": {'annotations': {'xsd_element': {'tag': 'xsd_element',
                                         'value': 'Publication_Year'},
                         'xsd_type': {'tag': 'xsd_type', 'value': 'xs:gYear'}},
         'domain_of': ['ExternalReference']} })
    publication_month: Optional[str] = Field(default=None, description="""The month of publication of the referenced material. Must follow the --MM format (xs:gMonth).""", json_schema_extra = { "linkml_meta": {'annotations': {'xsd_element': {'tag': 'xsd_element',
                                         'value': 'Publication_Month'},
                         'xsd_type': {'tag': 'xsd_type', 'value': 'xs:gMonth'}},
         'domain_of': ['ExternalReference']} })
    publication_day: Optional[str] = Field(default=None, description="""The day of publication of the referenced material. Must follow the ---DD format (xs:gDay).""", json_schema_extra = { "linkml_meta": {'annotations': {'xsd_element': {'tag': 'xsd_element',
                                         'value': 'Publication_Day'},
                         'xsd_type': {'tag': 'xsd_type', 'value': 'xs:gDay'}},
         'domain_of': ['ExternalReference']} })
    publisher: Optional[str] = Field(default=None, description="""The name of the publisher of the referenced material.""", json_schema_extra = { "linkml_meta": {'annotations': {'xsd_element': {'tag': 'xsd_element', 'value': 'Publisher'}},
         'domain_of': ['ExternalReference']} })
    url: Optional[str] = Field(default=None, description="""A URL for the material being referenced, if one exists online.""", json_schema_extra = { "linkml_meta": {'annotations': {'xsd_element': {'tag': 'xsd_element', 'value': 'URL'},
                         'xsd_type': {'tag': 'xsd_type', 'value': 'xs:anyURI'}},
         'domain_of': ['ExternalReference']} })
    url_date: Optional[date] = Field(default=None, description="""The date when the URL was validated to be accessible and correct.""", json_schema_extra = { "linkml_meta": {'annotations': {'xsd_element': {'tag': 'xsd_element', 'value': 'URL_Date'},
                         'xsd_type': {'tag': 'xsd_type', 'value': 'xs:date'}},
         'domain_of': ['ExternalReference']} })


class AlternateTerm(ConfiguredBaseModel):
    """
    Another name or term used to describe an attack pattern. Provides context for the alternate term by which the attack pattern may be known.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'annotations': {'xsd_type': {'tag': 'xsd_type',
                                      'value': 'AlternateTermsType/Alternate_Term '
                                               '(inline)'}},
         'from_schema': 'https://w3id.org/lmodel/capec',
         'in_subset': ['attack_pattern_content'],
         'slot_usage': {'description': {'annotations': {'xsd_element': {'tag': 'xsd_element',
                                                                        'value': 'Description'},
                                                        'xsd_type': {'tag': 'xsd_type',
                                                                     'value': 'StructuredTextType'}},
                                        'description': 'Context and explanation for '
                                                       'each alternate term by which '
                                                       'this attack pattern may be '
                                                       'known.',
                                        'name': 'description',
                                        'range': 'StructuredText'},
                        'term': {'annotations': {'xsd_element': {'tag': 'xsd_element',
                                                                 'value': 'Term'}},
                                 'description': 'The actual alternate term or name for '
                                                'the attack pattern.',
                                 'name': 'term',
                                 'range': 'string',
                                 'required': True}}})

    description: Optional[str] = Field(default=None, description="""Context and explanation for each alternate term by which this attack pattern may be known.""", json_schema_extra = { "linkml_meta": {'annotations': {'xsd_element': {'tag': 'xsd_element', 'value': 'Description'},
                         'xsd_type': {'tag': 'xsd_type',
                                      'value': 'StructuredTextType'}},
         'domain_of': ['AttackPattern',
                       'AlternateTerm',
                       'Skill',
                       'AttackStep',
                       'Technique',
                       'Stakeholder']} })
    term: str = Field(default=..., description="""The actual alternate term or name for the attack pattern.""", json_schema_extra = { "linkml_meta": {'annotations': {'xsd_element': {'tag': 'xsd_element', 'value': 'Term'}},
         'domain_of': ['AlternateTerm']} })


class Consequence(ConfiguredBaseModel):
    """
    An individual consequence associated with an attack pattern, specifying which
    security properties are violated, the technical impact that arises if an adversary
    succeeds, the likelihood of this specific consequence occurring, and any additional
    commentary.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'annotations': {'notes': {'tag': 'notes',
                                   'value': 'The optional Consequence_ID attribute is '
                                            'used internally by the CAPEC team to '
                                            'uniquely identify consequences repeated '
                                            'across patterns. The identifier format is '
                                            'CC-N (e.g., CC-1).'},
                         'xsd_type': {'tag': 'xsd_type',
                                      'value': 'ConsequencesType/Consequence '
                                               '(inline)'}},
         'from_schema': 'https://w3id.org/lmodel/capec',
         'in_subset': ['attack_pattern_content'],
         'slot_usage': {'consequence_id': {'annotations': {'xsd_attribute': {'tag': 'xsd_attribute',
                                                                             'value': 'Consequence_ID'}},
                                           'description': 'Internal CAPEC team '
                                                          'identifier for consequences '
                                                          'that repeat across many '
                                                          'individual patterns. Used '
                                                          'to keep repeated '
                                                          'consequences synchronized. '
                                                          'Format: CC-N (e.g., CC-1).',
                                           'name': 'consequence_id',
                                           'range': 'string'},
                        'impact': {'annotations': {'xsd_element': {'tag': 'xsd_element',
                                                                   'value': 'Impact'},
                                                   'xsd_type': {'tag': 'xsd_type',
                                                                'value': 'TechnicalImpactEnumeration'}},
                                   'description': 'Describes the negative technical '
                                                  'impact(s) that arise if an '
                                                  'adversary successfully achieves '
                                                  'this consequence.',
                                   'multivalued': True,
                                   'name': 'impact',
                                   'range': 'TechnicalImpactEnum'},
                        'likelihood': {'annotations': {'xsd_element': {'tag': 'xsd_element',
                                                                       'value': 'Likelihood'},
                                                       'xsd_type': {'tag': 'xsd_type',
                                                                    'value': 'LikelihoodEnumeration'}},
                                       'description': 'Identifies how likely this '
                                                      'specific consequence is '
                                                      'expected to be seen relative to '
                                                      'the other consequences of the '
                                                      'same attack pattern.',
                                       'name': 'likelihood',
                                       'range': 'LikelihoodEnum'},
                        'note': {'annotations': {'xsd_element': {'tag': 'xsd_element',
                                                                 'value': 'Note'},
                                                 'xsd_type': {'tag': 'xsd_type',
                                                              'value': 'StructuredTextType'}},
                                 'description': 'Additional commentary about this '
                                                'specific consequence.',
                                 'name': 'note',
                                 'range': 'StructuredText'},
                        'scope': {'annotations': {'xsd_element': {'tag': 'xsd_element',
                                                                  'value': 'Scope'},
                                                  'xsd_type': {'tag': 'xsd_type',
                                                               'value': 'ScopeEnumeration'}},
                                  'description': 'Identifies the security property or '
                                                 'properties that are violated when '
                                                 'this consequence occurs. Multiple '
                                                 'scopes may apply simultaneously.',
                                  'multivalued': True,
                                  'name': 'scope',
                                  'range': 'ScopeEnum',
                                  'required': True}}})

    consequence_id: Optional[str] = Field(default=None, description="""Internal CAPEC team identifier for consequences that repeat across many individual patterns. Used to keep repeated consequences synchronized. Format: CC-N (e.g., CC-1).""", json_schema_extra = { "linkml_meta": {'annotations': {'xsd_attribute': {'tag': 'xsd_attribute',
                                           'value': 'Consequence_ID'}},
         'domain_of': ['Consequence']} })
    scope: list[ScopeEnum] = Field(default=..., description="""Identifies the security property or properties that are violated when this consequence occurs. Multiple scopes may apply simultaneously.""", json_schema_extra = { "linkml_meta": {'annotations': {'xsd_element': {'tag': 'xsd_element', 'value': 'Scope'},
                         'xsd_type': {'tag': 'xsd_type', 'value': 'ScopeEnumeration'}},
         'domain_of': ['Consequence']} })
    impact: Optional[list[TechnicalImpactEnum]] = Field(default=None, description="""Describes the negative technical impact(s) that arise if an adversary successfully achieves this consequence.""", json_schema_extra = { "linkml_meta": {'annotations': {'xsd_element': {'tag': 'xsd_element', 'value': 'Impact'},
                         'xsd_type': {'tag': 'xsd_type',
                                      'value': 'TechnicalImpactEnumeration'}},
         'domain_of': ['Consequence']} })
    likelihood: Optional[LikelihoodEnum] = Field(default=None, description="""Identifies how likely this specific consequence is expected to be seen relative to the other consequences of the same attack pattern.""", json_schema_extra = { "linkml_meta": {'annotations': {'xsd_element': {'tag': 'xsd_element', 'value': 'Likelihood'},
                         'xsd_type': {'tag': 'xsd_type',
                                      'value': 'LikelihoodEnumeration'}},
         'domain_of': ['Consequence']} })
    note: Optional[str] = Field(default=None, description="""Additional commentary about this specific consequence.""", json_schema_extra = { "linkml_meta": {'annotations': {'xsd_element': {'tag': 'xsd_element', 'value': 'Note'},
                         'xsd_type': {'tag': 'xsd_type',
                                      'value': 'StructuredTextType'}},
         'domain_of': ['Consequence']} })


class Skill(ConfiguredBaseModel):
    """
    A description of the level of skills or specific knowledge needed by an adversary to execute this type of attack. Each skill entry captures both the skill level and a textual description of the knowledge required.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'annotations': {'xsd_type': {'tag': 'xsd_type',
                                      'value': 'SkillsType/Skill (inline simpleContent '
                                               'extension)'}},
         'from_schema': 'https://w3id.org/lmodel/capec',
         'in_subset': ['attack_pattern_content'],
         'slot_usage': {'description': {'annotations': {'xsd_type': {'tag': 'xsd_type',
                                                                     'value': 'xs:string '
                                                                              '(simpleContent '
                                                                              'base)'}},
                                        'description': 'Textual description of the '
                                                       'specific skills or knowledge '
                                                       'the adversary must possess to '
                                                       'execute this attack at the '
                                                       'given skill level.',
                                        'name': 'description',
                                        'range': 'string',
                                        'required': True},
                        'level': {'annotations': {'xsd_attribute': {'tag': 'xsd_attribute',
                                                                    'value': 'Level'},
                                                  'xsd_type': {'tag': 'xsd_type',
                                                               'value': 'SkillLevelEnumeration'}},
                                  'description': 'The skill or knowledge level '
                                                 'required (High, Medium, Low, or '
                                                 'Unknown).',
                                  'name': 'level',
                                  'range': 'SkillLevelEnum',
                                  'required': True}}})

    description: str = Field(default=..., description="""Textual description of the specific skills or knowledge the adversary must possess to execute this attack at the given skill level.""", json_schema_extra = { "linkml_meta": {'annotations': {'xsd_type': {'tag': 'xsd_type',
                                      'value': 'xs:string (simpleContent base)'}},
         'domain_of': ['AttackPattern',
                       'AlternateTerm',
                       'Skill',
                       'AttackStep',
                       'Technique',
                       'Stakeholder']} })
    level: SkillLevelEnum = Field(default=..., description="""The skill or knowledge level required (High, Medium, Low, or Unknown).""", json_schema_extra = { "linkml_meta": {'annotations': {'xsd_attribute': {'tag': 'xsd_attribute', 'value': 'Level'},
                         'xsd_type': {'tag': 'xsd_type',
                                      'value': 'SkillLevelEnumeration'}},
         'domain_of': ['Skill']} })


class Note(ConfiguredBaseModel):
    """
    An additional comment about a CAPEC entry that cannot be captured using the other available elements. Each note has a type indicating its purpose and contains content describing the note.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'annotations': {'xsd_type': {'tag': 'xsd_type',
                                      'value': 'NotesType/Note (inline complexContent '
                                               'extension of StructuredTextType)'}},
         'from_schema': 'https://w3id.org/lmodel/capec',
         'in_subset': ['attack_pattern_content'],
         'slot_usage': {'content': {'annotations': {'xsd_type': {'tag': 'xsd_type',
                                                                 'value': 'StructuredTextType '
                                                                          '(complexContent '
                                                                          'base)'}},
                                    'description': 'The content of the note, '
                                                   'potentially containing XHTML '
                                                   'markup.',
                                    'name': 'content',
                                    'range': 'StructuredText',
                                    'required': True},
                        'type': {'annotations': {'xsd_attribute': {'tag': 'xsd_attribute',
                                                                   'value': 'Type'},
                                                 'xsd_type': {'tag': 'xsd_type',
                                                              'value': 'NoteTypeEnumeration'}},
                                 'description': 'The type of note, indicating its '
                                                'purpose (Maintenance, Relationship, '
                                                'Research Gap, Terminology, or Other).',
                                 'name': 'type',
                                 'range': 'NoteTypeEnum',
                                 'required': True}}})

    type: NoteTypeEnum = Field(default=..., description="""The type of note, indicating its purpose (Maintenance, Relationship, Research Gap, Terminology, or Other).""", json_schema_extra = { "linkml_meta": {'annotations': {'xsd_attribute': {'tag': 'xsd_attribute', 'value': 'Type'},
                         'xsd_type': {'tag': 'xsd_type',
                                      'value': 'NoteTypeEnumeration'}},
         'domain_of': ['View', 'Note', 'Stakeholder', 'Contribution']} })
    content: str = Field(default=..., description="""The content of the note, potentially containing XHTML markup.""", json_schema_extra = { "linkml_meta": {'annotations': {'xsd_type': {'tag': 'xsd_type',
                                      'value': 'StructuredTextType (complexContent '
                                               'base)'}},
         'domain_of': ['Note']} })


class AttackStep(ConfiguredBaseModel):
    """
    An individual step in the execution flow of an attack pattern. Provides a detailed
    description of a specific action typically performed by an adversary during the
    attack, along with the phase of the attack it belongs to and any specific techniques
    used.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'annotations': {'xsd_type': {'tag': 'xsd_type',
                                      'value': 'ExecutionFlowType/Attack_Step '
                                               '(inline)'}},
         'from_schema': 'https://w3id.org/lmodel/capec',
         'in_subset': ['execution_flow_types'],
         'slot_usage': {'description': {'annotations': {'xsd_element': {'tag': 'xsd_element',
                                                                        'value': 'Description'},
                                                        'xsd_type': {'tag': 'xsd_type',
                                                                     'value': 'StructuredTextType'}},
                                        'description': 'A description of the actions '
                                                       'taken by the adversary during '
                                                       'this step of the attack.',
                                        'name': 'description',
                                        'range': 'StructuredText',
                                        'required': True},
                        'phase': {'annotations': {'xsd_element': {'tag': 'xsd_element',
                                                                  'value': 'Phase'}},
                                  'description': 'The phase of the attack this step '
                                                 'belongs to (Explore, Experiment, or '
                                                 'Exploit).',
                                  'name': 'phase',
                                  'range': 'AttackStepPhaseEnum',
                                  'required': True},
                        'step': {'annotations': {'xsd_element': {'tag': 'xsd_element',
                                                                 'value': 'Step'},
                                                 'xsd_type': {'tag': 'xsd_type',
                                                              'value': 'xs:integer'}},
                                 'description': 'The sequential step number within the '
                                                'execution flow.',
                                 'name': 'step',
                                 'range': 'integer',
                                 'required': True},
                        'techniques': {'annotations': {'xsd_element': {'tag': 'xsd_element',
                                                                       'value': 'Technique'}},
                                       'description': 'Specific techniques used by the '
                                                      'adversary during this attack '
                                                      'step.',
                                       'inlined_as_list': True,
                                       'multivalued': True,
                                       'name': 'techniques',
                                       'range': 'Technique'}}})

    description: str = Field(default=..., description="""A description of the actions taken by the adversary during this step of the attack.""", json_schema_extra = { "linkml_meta": {'annotations': {'xsd_element': {'tag': 'xsd_element', 'value': 'Description'},
                         'xsd_type': {'tag': 'xsd_type',
                                      'value': 'StructuredTextType'}},
         'domain_of': ['AttackPattern',
                       'AlternateTerm',
                       'Skill',
                       'AttackStep',
                       'Technique',
                       'Stakeholder']} })
    step: int = Field(default=..., description="""The sequential step number within the execution flow.""", json_schema_extra = { "linkml_meta": {'annotations': {'xsd_element': {'tag': 'xsd_element', 'value': 'Step'},
                         'xsd_type': {'tag': 'xsd_type', 'value': 'xs:integer'}},
         'domain_of': ['AttackStep']} })
    phase: AttackStepPhaseEnum = Field(default=..., description="""The phase of the attack this step belongs to (Explore, Experiment, or Exploit).""", json_schema_extra = { "linkml_meta": {'annotations': {'xsd_element': {'tag': 'xsd_element', 'value': 'Phase'}},
         'domain_of': ['AttackStep']} })
    techniques: Optional[list[Technique]] = Field(default=None, description="""Specific techniques used by the adversary during this attack step.""", json_schema_extra = { "linkml_meta": {'annotations': {'xsd_element': {'tag': 'xsd_element', 'value': 'Technique'}},
         'domain_of': ['AttackStep']} })


class Technique(ConfiguredBaseModel):
    """
    A specific technique used by an adversary during an attack step. Extends the structured text description with an optional reference to a related CAPEC entry.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'annotations': {'xsd_type': {'tag': 'xsd_type',
                                      'value': 'ExecutionFlowType/Attack_Step/Technique '
                                               '(inline complexContent extension of '
                                               'StructuredTextType)'}},
         'from_schema': 'https://w3id.org/lmodel/capec',
         'in_subset': ['execution_flow_types'],
         'slot_usage': {'capec_id': {'annotations': {'xsd_attribute': {'tag': 'xsd_attribute',
                                                                       'value': 'CAPEC_ID'},
                                                     'xsd_type': {'tag': 'xsd_type',
                                                                  'value': 'xs:string'}},
                                     'description': 'Optional reference to a related '
                                                    'CAPEC entry ID relevant to this '
                                                    'technique.',
                                     'name': 'capec_id',
                                     'range': 'string'},
                        'description': {'annotations': {'xsd_type': {'tag': 'xsd_type',
                                                                     'value': 'StructuredTextType '
                                                                              '(complexContent '
                                                                              'base)'}},
                                        'description': 'Description of the specific '
                                                       'technique, potentially '
                                                       'containing XHTML markup.',
                                        'name': 'description',
                                        'range': 'StructuredText',
                                        'required': True}}})

    capec_id: Optional[str] = Field(default=None, description="""Optional reference to a related CAPEC entry ID relevant to this technique.""", json_schema_extra = { "linkml_meta": {'annotations': {'xsd_attribute': {'tag': 'xsd_attribute', 'value': 'CAPEC_ID'},
                         'xsd_type': {'tag': 'xsd_type', 'value': 'xs:string'}},
         'domain_of': ['Technique', 'RelatedAttackPattern', 'MemberOf', 'HasMember']} })
    description: str = Field(default=..., description="""Description of the specific technique, potentially containing XHTML markup.""", json_schema_extra = { "linkml_meta": {'annotations': {'xsd_type': {'tag': 'xsd_type',
                                      'value': 'StructuredTextType (complexContent '
                                               'base)'}},
         'domain_of': ['AttackPattern',
                       'AlternateTerm',
                       'Skill',
                       'AttackStep',
                       'Technique',
                       'Stakeholder']} })


class RelatedAttackPattern(ConfiguredBaseModel):
    """
    A reference to another attack pattern that provides insight to similar items at
    higher or lower levels of abstraction, or items that are part of a chaining or
    peer relationship. Special cases may require Exclude_Related elements to capture
    ancestor IDs for which this relationship is not applicable.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'annotations': {'xsd_type': {'tag': 'xsd_type',
                                      'value': 'RelatedAttackPatternType/Related_Attack_Pattern '
                                               '(inline)'}},
         'from_schema': 'https://w3id.org/lmodel/capec',
         'in_subset': ['relationship_types'],
         'slot_usage': {'capec_id': {'annotations': {'xsd_attribute': {'tag': 'xsd_attribute',
                                                                       'value': 'CAPEC_ID'},
                                                     'xsd_type': {'tag': 'xsd_type',
                                                                  'value': 'xs:integer'}},
                                     'description': 'The unique CAPEC integer '
                                                    'identifier of the related attack '
                                                    'pattern.',
                                     'name': 'capec_id',
                                     'range': 'integer',
                                     'required': True},
                        'exclude_related': {'annotations': {'xsd_element': {'tag': 'xsd_element',
                                                                            'value': 'Exclude_Related'},
                                                            'xsd_type': {'tag': 'xsd_type',
                                                                         'value': 'ExcludeRelatedType'}},
                                            'description': 'One or more CAPEC '
                                                           'identifiers of ancestors '
                                                           'for which this '
                                                           'relationship is not '
                                                           'applicable (special cases '
                                                           'only).',
                                            'inlined_as_list': True,
                                            'multivalued': True,
                                            'name': 'exclude_related',
                                            'range': 'ExcludeRelated'},
                        'nature': {'annotations': {'xsd_attribute': {'tag': 'xsd_attribute',
                                                                     'value': 'Nature'},
                                                   'xsd_type': {'tag': 'xsd_type',
                                                                'value': 'RelatedNatureEnumeration'}},
                                   'description': 'The nature of the relationship '
                                                  '(ChildOf, ParentOf, CanFollow, '
                                                  'CanPrecede, CanAlsoBe, or PeerOf).',
                                   'name': 'nature',
                                   'range': 'RelatedNatureEnum',
                                   'required': True}}})

    capec_id: int = Field(default=..., description="""The unique CAPEC integer identifier of the related attack pattern.""", json_schema_extra = { "linkml_meta": {'annotations': {'xsd_attribute': {'tag': 'xsd_attribute', 'value': 'CAPEC_ID'},
                         'xsd_type': {'tag': 'xsd_type', 'value': 'xs:integer'}},
         'domain_of': ['Technique', 'RelatedAttackPattern', 'MemberOf', 'HasMember']} })
    exclude_related: Optional[list[ExcludeRelated]] = Field(default=None, description="""One or more CAPEC identifiers of ancestors for which this relationship is not applicable (special cases only).""", json_schema_extra = { "linkml_meta": {'annotations': {'xsd_element': {'tag': 'xsd_element',
                                         'value': 'Exclude_Related'},
                         'xsd_type': {'tag': 'xsd_type',
                                      'value': 'ExcludeRelatedType'}},
         'domain_of': ['RelatedAttackPattern', 'MemberOf', 'HasMember']} })
    nature: RelatedNatureEnum = Field(default=..., description="""The nature of the relationship (ChildOf, ParentOf, CanFollow, CanPrecede, CanAlsoBe, or PeerOf).""", json_schema_extra = { "linkml_meta": {'annotations': {'xsd_attribute': {'tag': 'xsd_attribute', 'value': 'Nature'},
                         'xsd_type': {'tag': 'xsd_type',
                                      'value': 'RelatedNatureEnumeration'}},
         'domain_of': ['RelatedAttackPattern']} })


class ExcludeRelated(ConfiguredBaseModel):
    """
    Captures the CAPEC identifier of an ancestor for which a given relationship is
    not applicable. Used in special cases within RelatedAttackPattern and relationship
    entries.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'annotations': {'xsd_type': {'tag': 'xsd_type',
                                      'value': 'ExcludeRelatedType'}},
         'from_schema': 'https://w3id.org/lmodel/capec',
         'in_subset': ['relationship_types'],
         'slot_usage': {'exclude_id': {'annotations': {'xsd_attribute': {'tag': 'xsd_attribute',
                                                                         'value': 'Exclude_ID'},
                                                       'xsd_type': {'tag': 'xsd_type',
                                                                    'value': 'xs:integer'}},
                                       'description': 'The CAPEC integer identifier of '
                                                      'the ancestor entry for which '
                                                      'the relationship is not '
                                                      'applicable.',
                                       'name': 'exclude_id',
                                       'range': 'integer',
                                       'required': True}}})

    exclude_id: int = Field(default=..., description="""The CAPEC integer identifier of the ancestor entry for which the relationship is not applicable.""", json_schema_extra = { "linkml_meta": {'annotations': {'xsd_attribute': {'tag': 'xsd_attribute',
                                           'value': 'Exclude_ID'},
                         'xsd_type': {'tag': 'xsd_type', 'value': 'xs:integer'}},
         'domain_of': ['ExcludeRelated']} })


class RelatedWeakness(ConfiguredBaseModel):
    """
    A reference to a CWE (Common Weakness Enumeration) weakness associated with an
    attack pattern. The association implies a weakness that must exist for a given
    attack to be successful. If multiple weaknesses are listed, any of them (but not
    necessarily all) may be present for the attack to succeed.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'annotations': {'xsd_type': {'tag': 'xsd_type',
                                      'value': 'RelatedWeaknessesType/Related_Weakness '
                                               '(inline)'}},
         'from_schema': 'https://w3id.org/lmodel/capec',
         'in_subset': ['relationship_types'],
         'slot_usage': {'cwe_id': {'annotations': {'xsd_attribute': {'tag': 'xsd_attribute',
                                                                     'value': 'CWE_ID'},
                                                   'xsd_type': {'tag': 'xsd_type',
                                                                'value': 'xs:integer'}},
                                   'description': 'The CWE integer identifier of the '
                                                  'related weakness (e.g., 79 for '
                                                  'CWE-79: Improper Neutralization of '
                                                  'Input During Web Page Generation).',
                                   'name': 'cwe_id',
                                   'range': 'integer',
                                   'required': True}}})

    cwe_id: int = Field(default=..., description="""The CWE integer identifier of the related weakness (e.g., 79 for CWE-79: Improper Neutralization of Input During Web Page Generation).""", json_schema_extra = { "linkml_meta": {'annotations': {'xsd_attribute': {'tag': 'xsd_attribute', 'value': 'CWE_ID'},
                         'xsd_type': {'tag': 'xsd_type', 'value': 'xs:integer'}},
         'domain_of': ['RelatedWeakness']} })


class Relationships(ConfiguredBaseModel):
    """
    A container for relationships associated with a category or view, showing
    Member_Of relationships with views or categories and Has_Member relationships
    with attack patterns or categories.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'annotations': {'xsd_type': {'tag': 'xsd_type', 'value': 'RelationshipsType'}},
         'from_schema': 'https://w3id.org/lmodel/capec',
         'in_subset': ['relationship_types'],
         'slot_usage': {'has_member': {'annotations': {'xsd_element': {'tag': 'xsd_element',
                                                                       'value': 'Has_Member'}},
                                       'description': 'Has_Member relationships '
                                                      'showing that this category or '
                                                      'view contains a given attack '
                                                      'pattern or category as a '
                                                      'member, identified by CAPEC_ID.',
                                       'inlined_as_list': True,
                                       'multivalued': True,
                                       'name': 'has_member',
                                       'range': 'HasMember'},
                        'member_of': {'annotations': {'xsd_element': {'tag': 'xsd_element',
                                                                      'value': 'Member_Of'}},
                                      'description': 'Member_Of relationships showing '
                                                     'that this category or view is a '
                                                     'member of a given view or parent '
                                                     'category, identified by '
                                                     'CAPEC_ID.',
                                      'inlined_as_list': True,
                                      'multivalued': True,
                                      'name': 'member_of',
                                      'range': 'MemberOf'}}})

    member_of: Optional[list[MemberOf]] = Field(default=None, description="""Member_Of relationships showing that this category or view is a member of a given view or parent category, identified by CAPEC_ID.""", json_schema_extra = { "linkml_meta": {'annotations': {'xsd_element': {'tag': 'xsd_element', 'value': 'Member_Of'}},
         'domain_of': ['Relationships']} })
    has_member: Optional[list[HasMember]] = Field(default=None, description="""Has_Member relationships showing that this category or view contains a given attack pattern or category as a member, identified by CAPEC_ID.""", json_schema_extra = { "linkml_meta": {'annotations': {'xsd_element': {'tag': 'xsd_element', 'value': 'Has_Member'}},
         'domain_of': ['Relationships']} })


class MemberOf(ConfiguredBaseModel):
    """
    Represents a Member_Of relationship indicating that the parent category or view
    is a member of the specified view or parent category.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'annotations': {'xsd_type': {'tag': 'xsd_type',
                                      'value': 'RelationshipsType/Member_Of (inline)'}},
         'from_schema': 'https://w3id.org/lmodel/capec',
         'in_subset': ['relationship_types'],
         'slot_usage': {'capec_id': {'annotations': {'xsd_attribute': {'tag': 'xsd_attribute',
                                                                       'value': 'CAPEC_ID'},
                                                     'xsd_type': {'tag': 'xsd_type',
                                                                  'value': 'xs:integer'}},
                                     'description': 'The CAPEC integer identifier of '
                                                    'the target view or category that '
                                                    'this entry is a member of.',
                                     'name': 'capec_id',
                                     'range': 'integer',
                                     'required': True},
                        'exclude_related': {'annotations': {'xsd_element': {'tag': 'xsd_element',
                                                                            'value': 'Exclude_Related'},
                                                            'xsd_type': {'tag': 'xsd_type',
                                                                         'value': 'ExcludeRelatedType'}},
                                            'description': 'CAPEC identifiers of '
                                                           'ancestors for which this '
                                                           'Member_Of relationship is '
                                                           'not applicable (special '
                                                           'cases only).',
                                            'inlined_as_list': True,
                                            'multivalued': True,
                                            'name': 'exclude_related',
                                            'range': 'ExcludeRelated'}}})

    capec_id: int = Field(default=..., description="""The CAPEC integer identifier of the target view or category that this entry is a member of.""", json_schema_extra = { "linkml_meta": {'annotations': {'xsd_attribute': {'tag': 'xsd_attribute', 'value': 'CAPEC_ID'},
                         'xsd_type': {'tag': 'xsd_type', 'value': 'xs:integer'}},
         'domain_of': ['Technique', 'RelatedAttackPattern', 'MemberOf', 'HasMember']} })
    exclude_related: Optional[list[ExcludeRelated]] = Field(default=None, description="""CAPEC identifiers of ancestors for which this Member_Of relationship is not applicable (special cases only).""", json_schema_extra = { "linkml_meta": {'annotations': {'xsd_element': {'tag': 'xsd_element',
                                         'value': 'Exclude_Related'},
                         'xsd_type': {'tag': 'xsd_type',
                                      'value': 'ExcludeRelatedType'}},
         'domain_of': ['RelatedAttackPattern', 'MemberOf', 'HasMember']} })


class HasMember(ConfiguredBaseModel):
    """
    Represents a Has_Member relationship indicating that the parent category or view
    contains the specified attack pattern or category as a member.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'annotations': {'xsd_type': {'tag': 'xsd_type',
                                      'value': 'RelationshipsType/Has_Member '
                                               '(inline)'}},
         'from_schema': 'https://w3id.org/lmodel/capec',
         'in_subset': ['relationship_types'],
         'slot_usage': {'capec_id': {'annotations': {'xsd_attribute': {'tag': 'xsd_attribute',
                                                                       'value': 'CAPEC_ID'},
                                                     'xsd_type': {'tag': 'xsd_type',
                                                                  'value': 'xs:integer'}},
                                     'description': 'The CAPEC integer identifier of '
                                                    'the attack pattern or category '
                                                    'that is a member of this entry.',
                                     'name': 'capec_id',
                                     'range': 'integer',
                                     'required': True},
                        'exclude_related': {'annotations': {'xsd_element': {'tag': 'xsd_element',
                                                                            'value': 'Exclude_Related'},
                                                            'xsd_type': {'tag': 'xsd_type',
                                                                         'value': 'ExcludeRelatedType'}},
                                            'description': 'CAPEC identifiers of '
                                                           'ancestors for which this '
                                                           'Has_Member relationship is '
                                                           'not applicable (special '
                                                           'cases only).',
                                            'inlined_as_list': True,
                                            'multivalued': True,
                                            'name': 'exclude_related',
                                            'range': 'ExcludeRelated'}}})

    capec_id: int = Field(default=..., description="""The CAPEC integer identifier of the attack pattern or category that is a member of this entry.""", json_schema_extra = { "linkml_meta": {'annotations': {'xsd_attribute': {'tag': 'xsd_attribute', 'value': 'CAPEC_ID'},
                         'xsd_type': {'tag': 'xsd_type', 'value': 'xs:integer'}},
         'domain_of': ['Technique', 'RelatedAttackPattern', 'MemberOf', 'HasMember']} })
    exclude_related: Optional[list[ExcludeRelated]] = Field(default=None, description="""CAPEC identifiers of ancestors for which this Has_Member relationship is not applicable (special cases only).""", json_schema_extra = { "linkml_meta": {'annotations': {'xsd_element': {'tag': 'xsd_element',
                                         'value': 'Exclude_Related'},
                         'xsd_type': {'tag': 'xsd_type',
                                      'value': 'ExcludeRelatedType'}},
         'domain_of': ['RelatedAttackPattern', 'MemberOf', 'HasMember']} })


class Reference(ConfiguredBaseModel):
    """
    A link from a CAPEC entry to an external reference defined within the catalog.
    The External_Reference_ID identifies which external reference is being cited.
    An optional Section captures a specific section title or page number relevant
    to this use of the reference.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'annotations': {'notes': {'tag': 'notes',
                                   'value': 'Text or quotes within an entry can cite '
                                            'the External_Reference_ID using the '
                                            'format [REF-N] as a footnote-style '
                                            'citation.'},
                         'xsd_type': {'tag': 'xsd_type',
                                      'value': 'ReferencesType/Reference (inline)'}},
         'from_schema': 'https://w3id.org/lmodel/capec',
         'in_subset': ['relationship_types'],
         'slot_usage': {'external_reference_id': {'annotations': {'xsd_attribute': {'tag': 'xsd_attribute',
                                                                                    'value': 'External_Reference_ID'},
                                                                  'xsd_type': {'tag': 'xsd_type',
                                                                               'value': 'xs:string'}},
                                                  'description': 'The identifier of '
                                                                 'the external '
                                                                 'reference entry '
                                                                 'being linked to '
                                                                 '(e.g., REF-1). Must '
                                                                 'match a Reference_ID '
                                                                 "in the catalog's "
                                                                 'External_References.',
                                                  'name': 'external_reference_id',
                                                  'range': 'string',
                                                  'required': True},
                        'section': {'annotations': {'xsd_attribute': {'tag': 'xsd_attribute',
                                                                      'value': 'Section'},
                                                    'xsd_type': {'tag': 'xsd_type',
                                                                 'value': 'xs:string'}},
                                    'description': 'A specific section title or page '
                                                   'number within the referenced '
                                                   'material that is particularly '
                                                   'relevant to this use of the '
                                                   'reference.',
                                    'name': 'section',
                                    'range': 'string'}}})

    external_reference_id: str = Field(default=..., description="""The identifier of the external reference entry being linked to (e.g., REF-1). Must match a Reference_ID in the catalog's External_References.""", json_schema_extra = { "linkml_meta": {'annotations': {'xsd_attribute': {'tag': 'xsd_attribute',
                                           'value': 'External_Reference_ID'},
                         'xsd_type': {'tag': 'xsd_type', 'value': 'xs:string'}},
         'domain_of': ['Reference']} })
    section: Optional[str] = Field(default=None, description="""A specific section title or page number within the referenced material that is particularly relevant to this use of the reference.""", json_schema_extra = { "linkml_meta": {'annotations': {'xsd_attribute': {'tag': 'xsd_attribute', 'value': 'Section'},
                         'xsd_type': {'tag': 'xsd_type', 'value': 'xs:string'}},
         'domain_of': ['Reference']} })


class TaxonomyMapping(ConfiguredBaseModel):
    """
    A mapping from a CAPEC entry (AttackPattern or Category) to an equivalent or related
    entry in a different security taxonomy. Identifies the external taxonomy, the ID and
    name of the external entry, and how closely the CAPEC entry aligns with it.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'annotations': {'xsd_type': {'tag': 'xsd_type',
                                      'value': 'TaxonomyMappingsType/Taxonomy_Mapping '
                                               '(inline)'}},
         'from_schema': 'https://w3id.org/lmodel/capec',
         'in_subset': ['taxonomy_types'],
         'slot_usage': {'entry_id': {'annotations': {'xsd_element': {'tag': 'xsd_element',
                                                                     'value': 'Entry_ID'}},
                                     'description': 'The identifier of the entry in '
                                                    'the external taxonomy that this '
                                                    'CAPEC entry is being mapped to.',
                                     'name': 'entry_id',
                                     'range': 'string'},
                        'entry_name': {'annotations': {'xsd_element': {'tag': 'xsd_element',
                                                                       'value': 'Entry_Name'}},
                                       'description': 'The name of the entry in the '
                                                      'external taxonomy that this '
                                                      'CAPEC entry is being mapped to.',
                                       'name': 'entry_name',
                                       'range': 'string'},
                        'mapping_fit': {'annotations': {'xsd_element': {'tag': 'xsd_element',
                                                                        'value': 'Mapping_Fit'},
                                                        'xsd_type': {'tag': 'xsd_type',
                                                                     'value': 'TaxonomyMappingFitEnumeration'}},
                                        'description': 'Identifies how closely the '
                                                       'CAPEC entry aligns with the '
                                                       'external taxonomy entry '
                                                       '(Exact, CAPEC More Abstract, '
                                                       'CAPEC More Specific, '
                                                       'Imprecise, or Perspective).',
                                        'name': 'mapping_fit',
                                        'range': 'TaxonomyMappingFitEnum'},
                        'taxonomy_name': {'annotations': {'xsd_attribute': {'tag': 'xsd_attribute',
                                                                            'value': 'Taxonomy_Name'},
                                                          'xsd_type': {'tag': 'xsd_type',
                                                                       'value': 'TaxonomyNameEnumeration'}},
                                          'description': 'Identifies the external '
                                                         'taxonomy to which this '
                                                         'mapping is being made.',
                                          'name': 'taxonomy_name',
                                          'range': 'TaxonomyNameEnum',
                                          'required': True}}})

    taxonomy_name: TaxonomyNameEnum = Field(default=..., description="""Identifies the external taxonomy to which this mapping is being made.""", json_schema_extra = { "linkml_meta": {'annotations': {'xsd_attribute': {'tag': 'xsd_attribute',
                                           'value': 'Taxonomy_Name'},
                         'xsd_type': {'tag': 'xsd_type',
                                      'value': 'TaxonomyNameEnumeration'}},
         'domain_of': ['TaxonomyMapping']} })
    entry_id: Optional[str] = Field(default=None, description="""The identifier of the entry in the external taxonomy that this CAPEC entry is being mapped to.""", json_schema_extra = { "linkml_meta": {'annotations': {'xsd_element': {'tag': 'xsd_element', 'value': 'Entry_ID'}},
         'domain_of': ['TaxonomyMapping']} })
    entry_name: Optional[str] = Field(default=None, description="""The name of the entry in the external taxonomy that this CAPEC entry is being mapped to.""", json_schema_extra = { "linkml_meta": {'annotations': {'xsd_element': {'tag': 'xsd_element', 'value': 'Entry_Name'}},
         'domain_of': ['TaxonomyMapping']} })
    mapping_fit: Optional[TaxonomyMappingFitEnum] = Field(default=None, description="""Identifies how closely the CAPEC entry aligns with the external taxonomy entry (Exact, CAPEC More Abstract, CAPEC More Specific, Imprecise, or Perspective).""", json_schema_extra = { "linkml_meta": {'annotations': {'xsd_element': {'tag': 'xsd_element', 'value': 'Mapping_Fit'},
                         'xsd_type': {'tag': 'xsd_type',
                                      'value': 'TaxonomyMappingFitEnumeration'}},
         'domain_of': ['TaxonomyMapping']} })


class Stakeholder(ConfiguredBaseModel):
    """
    A target stakeholder or group for whom a CAPEC view is relevant. Specifies
    the type of stakeholder and describes which properties of the view they may
    find useful.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'annotations': {'xsd_type': {'tag': 'xsd_type',
                                      'value': 'AudienceType/Stakeholder (inline)'}},
         'from_schema': 'https://w3id.org/lmodel/capec',
         'in_subset': ['audience_types'],
         'slot_usage': {'description': {'annotations': {'xsd_element': {'tag': 'xsd_element',
                                                                        'value': 'Description'},
                                                        'xsd_type': {'tag': 'xsd_type',
                                                                     'value': 'StructuredTextType'}},
                                        'description': 'A description of what '
                                                       'properties of the view this '
                                                       'particular stakeholder might '
                                                       'find useful and how it applies '
                                                       'to their work.',
                                        'name': 'description',
                                        'range': 'StructuredText',
                                        'required': True},
                        'type': {'annotations': {'xsd_element': {'tag': 'xsd_element',
                                                                 'value': 'Type'},
                                                 'xsd_type': {'tag': 'xsd_type',
                                                              'value': 'StakeholderEnumeration'}},
                                 'description': 'The type of stakeholder or group that '
                                                'might be interested in the view.',
                                 'name': 'type',
                                 'range': 'StakeholderEnum',
                                 'required': True}}})

    type: StakeholderEnum = Field(default=..., description="""The type of stakeholder or group that might be interested in the view.""", json_schema_extra = { "linkml_meta": {'annotations': {'xsd_element': {'tag': 'xsd_element', 'value': 'Type'},
                         'xsd_type': {'tag': 'xsd_type',
                                      'value': 'StakeholderEnumeration'}},
         'domain_of': ['View', 'Note', 'Stakeholder', 'Contribution']} })
    description: str = Field(default=..., description="""A description of what properties of the view this particular stakeholder might find useful and how it applies to their work.""", json_schema_extra = { "linkml_meta": {'annotations': {'xsd_element': {'tag': 'xsd_element', 'value': 'Description'},
                         'xsd_type': {'tag': 'xsd_type',
                                      'value': 'StructuredTextType'}},
         'domain_of': ['AttackPattern',
                       'AlternateTerm',
                       'Skill',
                       'AttackStep',
                       'Technique',
                       'Stakeholder']} })


class ContentHistory(ConfiguredBaseModel):
    """
    Tracks the original author of a CAPEC entry and any subsequent modifications
    to the content. Provides a means of contacting authors and modifiers for
    clarifying ambiguities, merging overlapping contributions, etc.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'annotations': {'xsd_type': {'tag': 'xsd_type',
                                      'value': 'ContentHistoryType'}},
         'from_schema': 'https://w3id.org/lmodel/capec',
         'in_subset': ['content_history_types'],
         'slot_usage': {'contributions': {'annotations': {'xsd_element': {'tag': 'xsd_element',
                                                                          'value': 'Contribution'}},
                                          'description': 'Records of contributions '
                                                         'made to the entry, '
                                                         'identifying contributors and '
                                                         'whether their input was '
                                                         'donated content or general '
                                                         'feedback.',
                                          'inlined_as_list': True,
                                          'multivalued': True,
                                          'name': 'contributions',
                                          'range': 'Contribution'},
                        'modifications': {'annotations': {'xsd_element': {'tag': 'xsd_element',
                                                                          'value': 'Modification'}},
                                          'description': 'Records of modifications '
                                                         'made to the entry content. A '
                                                         'new Modification entry '
                                                         'should exist for each change '
                                                         'made.',
                                          'inlined_as_list': True,
                                          'multivalued': True,
                                          'name': 'modifications',
                                          'range': 'Modification'},
                        'previous_entry_names': {'annotations': {'xsd_element': {'tag': 'xsd_element',
                                                                                 'value': 'Previous_Entry_Name'}},
                                                 'description': 'Previous names that '
                                                                'were used for this '
                                                                'entry. Should be '
                                                                'recorded whenever a '
                                                                'substantive name '
                                                                'change occurs, '
                                                                'aligned with a '
                                                                'corresponding '
                                                                'Modification.',
                                                 'inlined_as_list': True,
                                                 'multivalued': True,
                                                 'name': 'previous_entry_names',
                                                 'range': 'PreviousEntryName'},
                        'submission': {'annotations': {'xsd_element': {'tag': 'xsd_element',
                                                                       'value': 'Submission'}},
                                       'description': 'Identifies the original '
                                                      'submitter, their organization, '
                                                      'the submission date, and any '
                                                      'comments related to the initial '
                                                      'entry submission.',
                                       'inlined': True,
                                       'name': 'submission',
                                       'range': 'Submission'}}})

    submission: Optional[Submission] = Field(default=None, description="""Identifies the original submitter, their organization, the submission date, and any comments related to the initial entry submission.""", json_schema_extra = { "linkml_meta": {'annotations': {'xsd_element': {'tag': 'xsd_element', 'value': 'Submission'}},
         'domain_of': ['ContentHistory']} })
    modifications: Optional[list[Modification]] = Field(default=None, description="""Records of modifications made to the entry content. A new Modification entry should exist for each change made.""", json_schema_extra = { "linkml_meta": {'annotations': {'xsd_element': {'tag': 'xsd_element',
                                         'value': 'Modification'}},
         'domain_of': ['ContentHistory']} })
    contributions: Optional[list[Contribution]] = Field(default=None, description="""Records of contributions made to the entry, identifying contributors and whether their input was donated content or general feedback.""", json_schema_extra = { "linkml_meta": {'annotations': {'xsd_element': {'tag': 'xsd_element',
                                         'value': 'Contribution'}},
         'domain_of': ['ContentHistory']} })
    previous_entry_names: Optional[list[PreviousEntryName]] = Field(default=None, description="""Previous names that were used for this entry. Should be recorded whenever a substantive name change occurs, aligned with a corresponding Modification.""", json_schema_extra = { "linkml_meta": {'annotations': {'xsd_element': {'tag': 'xsd_element',
                                         'value': 'Previous_Entry_Name'}},
         'domain_of': ['ContentHistory']} })


class Submission(ConfiguredBaseModel):
    """
    Information about the original submission of a CAPEC entry, identifying the
    submitter, their organization, the date of submission, and any related comments.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'annotations': {'xsd_type': {'tag': 'xsd_type',
                                      'value': 'ContentHistoryType/Submission '
                                               '(inline)'}},
         'from_schema': 'https://w3id.org/lmodel/capec',
         'in_subset': ['content_history_types'],
         'slot_usage': {'submission_comment': {'annotations': {'xsd_element': {'tag': 'xsd_element',
                                                                               'value': 'Submission_Comment'}},
                                               'description': 'Any comments related to '
                                                              'the original submission '
                                                              'of this entry.',
                                               'name': 'submission_comment',
                                               'range': 'string'},
                        'submission_date': {'annotations': {'xsd_element': {'tag': 'xsd_element',
                                                                            'value': 'Submission_Date'},
                                                            'xsd_type': {'tag': 'xsd_type',
                                                                         'value': 'xs:date'}},
                                            'description': 'The date on which this '
                                                           'entry was originally '
                                                           'submitted.',
                                            'name': 'submission_date',
                                            'range': 'date'},
                        'submission_name': {'annotations': {'xsd_element': {'tag': 'xsd_element',
                                                                            'value': 'Submission_Name'}},
                                            'description': 'The name of the person or '
                                                           'team who originally '
                                                           'submitted this entry.',
                                            'name': 'submission_name',
                                            'range': 'string'},
                        'submission_organization': {'annotations': {'xsd_element': {'tag': 'xsd_element',
                                                                                    'value': 'Submission_Organization'}},
                                                    'description': 'The organization '
                                                                   'of the person who '
                                                                   'originally '
                                                                   'submitted this '
                                                                   'entry.',
                                                    'name': 'submission_organization',
                                                    'range': 'string'}}})

    submission_name: Optional[str] = Field(default=None, description="""The name of the person or team who originally submitted this entry.""", json_schema_extra = { "linkml_meta": {'annotations': {'xsd_element': {'tag': 'xsd_element',
                                         'value': 'Submission_Name'}},
         'domain_of': ['Submission']} })
    submission_organization: Optional[str] = Field(default=None, description="""The organization of the person who originally submitted this entry.""", json_schema_extra = { "linkml_meta": {'annotations': {'xsd_element': {'tag': 'xsd_element',
                                         'value': 'Submission_Organization'}},
         'domain_of': ['Submission']} })
    submission_date: Optional[date] = Field(default=None, description="""The date on which this entry was originally submitted.""", json_schema_extra = { "linkml_meta": {'annotations': {'xsd_element': {'tag': 'xsd_element',
                                         'value': 'Submission_Date'},
                         'xsd_type': {'tag': 'xsd_type', 'value': 'xs:date'}},
         'domain_of': ['Submission']} })
    submission_comment: Optional[str] = Field(default=None, description="""Any comments related to the original submission of this entry.""", json_schema_extra = { "linkml_meta": {'annotations': {'xsd_element': {'tag': 'xsd_element',
                                         'value': 'Submission_Comment'}},
         'domain_of': ['Submission']} })


class Modification(ConfiguredBaseModel):
    """
    A record of a modification made to a CAPEC entry, identifying the modifier,
    their organization, the date of modification, the importance of the change,
    and any related comments. Modifications that change the meaning of the entry
    should be marked as Critical importance.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'annotations': {'xsd_type': {'tag': 'xsd_type',
                                      'value': 'ContentHistoryType/Modification '
                                               '(inline)'}},
         'from_schema': 'https://w3id.org/lmodel/capec',
         'in_subset': ['content_history_types'],
         'slot_usage': {'modification_comment': {'annotations': {'xsd_element': {'tag': 'xsd_element',
                                                                                 'value': 'Modification_Comment'}},
                                                 'description': 'Comments describing '
                                                                'the nature and reason '
                                                                'for this '
                                                                'modification.',
                                                 'name': 'modification_comment',
                                                 'range': 'string'},
                        'modification_date': {'annotations': {'xsd_element': {'tag': 'xsd_element',
                                                                              'value': 'Modification_Date'},
                                                              'xsd_type': {'tag': 'xsd_type',
                                                                           'value': 'xs:date'}},
                                              'description': 'The date on which this '
                                                             'modification was made.',
                                              'name': 'modification_date',
                                              'range': 'date'},
                        'modification_importance': {'annotations': {'xsd_element': {'tag': 'xsd_element',
                                                                                    'value': 'Modification_Importance'},
                                                                    'xsd_type': {'tag': 'xsd_type',
                                                                                 'value': 'ImportanceEnumeration'}},
                                                    'description': 'The importance '
                                                                   'level of this '
                                                                   'modification. '
                                                                   'Modifications that '
                                                                   'change the meaning '
                                                                   'of the entry or '
                                                                   'how it might be '
                                                                   'interpreted should '
                                                                   'be marked '
                                                                   'Critical.',
                                                    'name': 'modification_importance',
                                                    'range': 'ImportanceEnum'},
                        'modification_name': {'annotations': {'xsd_element': {'tag': 'xsd_element',
                                                                              'value': 'Modification_Name'}},
                                              'description': 'The name of the person '
                                                             'or team who made this '
                                                             'modification.',
                                              'name': 'modification_name',
                                              'range': 'string'},
                        'modification_organization': {'annotations': {'xsd_element': {'tag': 'xsd_element',
                                                                                      'value': 'Modification_Organization'}},
                                                      'description': 'The organization '
                                                                     'of the person '
                                                                     'who made this '
                                                                     'modification.',
                                                      'name': 'modification_organization',
                                                      'range': 'string'}}})

    modification_name: Optional[str] = Field(default=None, description="""The name of the person or team who made this modification.""", json_schema_extra = { "linkml_meta": {'annotations': {'xsd_element': {'tag': 'xsd_element',
                                         'value': 'Modification_Name'}},
         'domain_of': ['Modification']} })
    modification_organization: Optional[str] = Field(default=None, description="""The organization of the person who made this modification.""", json_schema_extra = { "linkml_meta": {'annotations': {'xsd_element': {'tag': 'xsd_element',
                                         'value': 'Modification_Organization'}},
         'domain_of': ['Modification']} })
    modification_date: Optional[date] = Field(default=None, description="""The date on which this modification was made.""", json_schema_extra = { "linkml_meta": {'annotations': {'xsd_element': {'tag': 'xsd_element',
                                         'value': 'Modification_Date'},
                         'xsd_type': {'tag': 'xsd_type', 'value': 'xs:date'}},
         'domain_of': ['Modification']} })
    modification_importance: Optional[ImportanceEnum] = Field(default=None, description="""The importance level of this modification. Modifications that change the meaning of the entry or how it might be interpreted should be marked Critical.""", json_schema_extra = { "linkml_meta": {'annotations': {'xsd_element': {'tag': 'xsd_element',
                                         'value': 'Modification_Importance'},
                         'xsd_type': {'tag': 'xsd_type',
                                      'value': 'ImportanceEnumeration'}},
         'domain_of': ['Modification']} })
    modification_comment: Optional[str] = Field(default=None, description="""Comments describing the nature and reason for this modification.""", json_schema_extra = { "linkml_meta": {'annotations': {'xsd_element': {'tag': 'xsd_element',
                                         'value': 'Modification_Comment'}},
         'domain_of': ['Modification']} })


class Contribution(ConfiguredBaseModel):
    """
    A record of a contribution made to a CAPEC entry, identifying the contributor,
    their organization, the date of contribution, the type of contribution (Content
    or Feedback), and any related comments.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'annotations': {'xsd_type': {'tag': 'xsd_type',
                                      'value': 'ContentHistoryType/Contribution '
                                               '(inline)'}},
         'from_schema': 'https://w3id.org/lmodel/capec',
         'in_subset': ['content_history_types'],
         'slot_usage': {'contribution_comment': {'annotations': {'xsd_element': {'tag': 'xsd_element',
                                                                                 'value': 'Contribution_Comment'}},
                                                 'description': 'Comments about the '
                                                                'contribution and its '
                                                                'significance.',
                                                 'name': 'contribution_comment',
                                                 'range': 'string'},
                        'contribution_date': {'annotations': {'xsd_element': {'tag': 'xsd_element',
                                                                              'value': 'Contribution_Date'},
                                                              'xsd_type': {'tag': 'xsd_type',
                                                                           'value': 'xs:date'}},
                                              'description': 'The date on which this '
                                                             'contribution was made.',
                                              'name': 'contribution_date',
                                              'range': 'date'},
                        'contribution_name': {'annotations': {'xsd_element': {'tag': 'xsd_element',
                                                                              'value': 'Contribution_Name'}},
                                              'description': 'The name of the person '
                                                             'or team who made this '
                                                             'contribution.',
                                              'name': 'contribution_name',
                                              'range': 'string'},
                        'contribution_organization': {'annotations': {'xsd_element': {'tag': 'xsd_element',
                                                                                      'value': 'Contribution_Organization'}},
                                                      'description': 'The organization '
                                                                     'of the person '
                                                                     'who made this '
                                                                     'contribution.',
                                                      'name': 'contribution_organization',
                                                      'range': 'string'},
                        'type': {'annotations': {'xsd_attribute': {'tag': 'xsd_attribute',
                                                                   'value': 'Type'}},
                                 'description': 'Indicates whether the contribution '
                                                'was donated content or general '
                                                'feedback.',
                                 'name': 'type',
                                 'range': 'ContributionTypeEnum',
                                 'required': True}}})

    type: ContributionTypeEnum = Field(default=..., description="""Indicates whether the contribution was donated content or general feedback.""", json_schema_extra = { "linkml_meta": {'annotations': {'xsd_attribute': {'tag': 'xsd_attribute', 'value': 'Type'}},
         'domain_of': ['View', 'Note', 'Stakeholder', 'Contribution']} })
    contribution_name: Optional[str] = Field(default=None, description="""The name of the person or team who made this contribution.""", json_schema_extra = { "linkml_meta": {'annotations': {'xsd_element': {'tag': 'xsd_element',
                                         'value': 'Contribution_Name'}},
         'domain_of': ['Contribution']} })
    contribution_organization: Optional[str] = Field(default=None, description="""The organization of the person who made this contribution.""", json_schema_extra = { "linkml_meta": {'annotations': {'xsd_element': {'tag': 'xsd_element',
                                         'value': 'Contribution_Organization'}},
         'domain_of': ['Contribution']} })
    contribution_date: Optional[date] = Field(default=None, description="""The date on which this contribution was made.""", json_schema_extra = { "linkml_meta": {'annotations': {'xsd_element': {'tag': 'xsd_element',
                                         'value': 'Contribution_Date'},
                         'xsd_type': {'tag': 'xsd_type', 'value': 'xs:date'}},
         'domain_of': ['Contribution']} })
    contribution_comment: Optional[str] = Field(default=None, description="""Comments about the contribution and its significance.""", json_schema_extra = { "linkml_meta": {'annotations': {'xsd_element': {'tag': 'xsd_element',
                                         'value': 'Contribution_Comment'}},
         'domain_of': ['Contribution']} })


class PreviousEntryName(ConfiguredBaseModel):
    """
    A previous name that was used for a CAPEC entry before a substantive name change.
    Should align with a corresponding Modification element that records the change.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'annotations': {'xsd_type': {'tag': 'xsd_type',
                                      'value': 'ContentHistoryType/Previous_Entry_Name '
                                               '(inline simpleContent extension)'}},
         'from_schema': 'https://w3id.org/lmodel/capec',
         'in_subset': ['content_history_types'],
         'slot_usage': {'entry_date': {'annotations': {'xsd_attribute': {'tag': 'xsd_attribute',
                                                                         'value': 'Date'},
                                                       'xsd_type': {'tag': 'xsd_type',
                                                                    'value': 'xs:date'}},
                                       'description': 'The date on which this name '
                                                      'change was made.',
                                       'name': 'entry_date',
                                       'range': 'date',
                                       'required': True},
                        'name': {'annotations': {'xsd_type': {'tag': 'xsd_type',
                                                              'value': 'xs:string '
                                                                       '(simpleContent '
                                                                       'base)'}},
                                 'description': 'The previous name that was used for '
                                                'this entry.',
                                 'name': 'name',
                                 'range': 'string',
                                 'required': True}}})

    name: str = Field(default=..., description="""The previous name that was used for this entry.""", json_schema_extra = { "linkml_meta": {'annotations': {'xsd_type': {'tag': 'xsd_type',
                                      'value': 'xs:string (simpleContent base)'}},
         'domain_of': ['AttackPatternCatalog',
                       'AttackPattern',
                       'Category',
                       'View',
                       'PreviousEntryName']} })
    entry_date: date = Field(default=..., description="""The date on which this name change was made.""", json_schema_extra = { "linkml_meta": {'annotations': {'xsd_attribute': {'tag': 'xsd_attribute', 'value': 'Date'},
                         'xsd_type': {'tag': 'xsd_type', 'value': 'xs:date'}},
         'domain_of': ['AttackPatternCatalog', 'PreviousEntryName']} })


# Model rebuild
# see https://pydantic-docs.helpmanual.io/usage/models/#rebuilding-a-model
AttackPatternCatalog.model_rebuild()
AttackPattern.model_rebuild()
Category.model_rebuild()
View.model_rebuild()
ExternalReference.model_rebuild()
AlternateTerm.model_rebuild()
Consequence.model_rebuild()
Skill.model_rebuild()
Note.model_rebuild()
AttackStep.model_rebuild()
Technique.model_rebuild()
RelatedAttackPattern.model_rebuild()
ExcludeRelated.model_rebuild()
RelatedWeakness.model_rebuild()
Relationships.model_rebuild()
MemberOf.model_rebuild()
HasMember.model_rebuild()
Reference.model_rebuild()
TaxonomyMapping.model_rebuild()
Stakeholder.model_rebuild()
ContentHistory.model_rebuild()
Submission.model_rebuild()
Modification.model_rebuild()
Contribution.model_rebuild()
PreviousEntryName.model_rebuild()
