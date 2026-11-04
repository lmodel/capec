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


metamodel_version = "1.12.0"
version = "3.9"


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


linkml_meta = LinkMLMeta({'annotations': {'catalogue_date': {'tag': 'catalogue_date',
                                        'value': '2023-01-24'},
                     'xsd_date': {'tag': 'xsd_date', 'value': '2021-10-21'},
                     'xsd_namespace': {'tag': 'xsd_namespace',
                                       'value': 'http://capec.mitre.org/capec-3'},
                     'xsd_version': {'tag': 'xsd_version', 'value': '3.5'}},
     'comments': ['The version is the version of the catalogue that the schema '
                  'renders, and xsd_version is the version of the XSD that '
                  'catalogue names. upstream/ holds both files unchanged, '
                  'tests/test_coverage.py holds the schema to the XSD, and '
                  'scripts/check_upstream_release.py reports when either moves.',
                  "MITRE's latest catalogue is dated January 2023 and its latest "
                  'news item March 2023. No page says CAPEC has stopped, so the '
                  'watch keeps asking.'],
     'default_prefix': 'capec',
     'default_range': 'string',
     'description': 'A LinkML model of the CAPEC catalogue. It keeps the keys and '
                    "listed values of the catalogue's XML Schema, so the catalogue "
                    'validates as MITRE spells it once scripts/capec_to_json.py '
                    'has turned it into data.',
     'id': 'https://w3id.org/lmodel/capec',
     'imports': ['linkml:types', './capec_core', './capec_entries'],
     'keywords': ['attack pattern',
                  'CAPEC',
                  'threat modelling',
                  'adversary technique',
                  'MITRE'],
     'license': 'Apache-2.0',
     'name': 'capec',
     'prefixes': {'capec': {'prefix_prefix': 'capec',
                            'prefix_reference': 'https://w3id.org/lmodel/capec/'},
                  'dcterms': {'prefix_prefix': 'dcterms',
                              'prefix_reference': 'http://purl.org/dc/terms/'},
                  'linkml': {'prefix_prefix': 'linkml',
                             'prefix_reference': 'https://w3id.org/linkml/'},
                  'schema': {'prefix_prefix': 'schema',
                             'prefix_reference': 'http://schema.org/'},
                  'skos': {'prefix_prefix': 'skos',
                           'prefix_reference': 'http://www.w3.org/2004/02/skos/core#'},
                  'wd': {'prefix_prefix': 'wd',
                         'prefix_reference': 'http://www.wikidata.org/entity/'}},
     'see_also': ['https://lmodel.github.io/capec', 'https://capec.mitre.org/'],
     'source': 'https://capec.mitre.org/data/xsd/ap_schema_v3.5.xsd',
     'source_file': 'src/capec/schema/capec.yaml',
     'title': 'Common Attack Pattern Enumeration and Classification (CAPEC)'} )

class CapecImportance(str, Enum):
    """
    How much a change to an entry matters to anyone relying on it.
    """
    Normal = "Normal"
    """
    A change that leaves the entry's meaning as it was.
    """
    Critical = "Critical"
    """
    A change to the entry's meaning or to how it may be read.
    """


class CapecNoteType(str, Enum):
    """
    What kind of remark a note makes.
    """
    Maintenance = "Maintenance"
    """
    Work on the entry still to be done.
    """
    Relationship = "Relationship"
    """
    Detail on how entries relate.
    """
    Research_Gap = "Research Gap"
    """
    Something the research community could look into further.
    """
    Terminology = "Terminology"
    """
    A question of wording, such as competing uses of one term.
    """
    Other = "Other"
    """
    A remark of no listed kind.
    """


class CapecStatus(str, Enum):
    """
    How far an entry has got through CAPEC's review.
    """
    Deprecated = "Deprecated"
    """
    Withdrawn from the catalogue, though its number stays taken.
    """
    Draft = "Draft"
    Incomplete = "Incomplete"
    Obsolete = "Obsolete"
    Stable = "Stable"
    Usable = "Usable"


class CapecTaxonomyMappingFit(str, Enum):
    """
    How well an entry fits the entry of another taxonomy that it maps to.
    """
    Exact = "Exact"
    CAPEC_More_Abstract = "CAPEC More Abstract"
    CAPEC_More_Specific = "CAPEC More Specific"
    Imprecise = "Imprecise"
    Perspective = "Perspective"


class CapecTaxonomyName(str, Enum):
    """
    The other taxonomies that CAPEC maps to.
    """
    ATTACK = "ATTACK"
    """
    MITRE ATT&CK. An entry's Entry_ID there is the technique's number without its T.
    """
    WASC = "WASC"
    """
    The Web Application Security Consortium's threat classification.
    """
    OWASP_Attacks = "OWASP Attacks"
    """
    The attack list of the Open Worldwide Application Security Project.
    """


class CapecContributionType(str, Enum):
    """
    Whether a contribution changed an entry's content or only commented on it.
    """
    Content = "Content"
    """
    Text given to the entry.
    """
    Feedback = "Feedback"
    """
    Remarks on the entry.
    """


class CapecAbstraction(str, Enum):
    """
    How concrete an attack pattern is.
    """
    Meta = "Meta"
    """
    A broad approach, free of any one technology, for use in design-level threat modelling.
    """
    Standard = "Standard"
    """
    One method or technique, often only a part of a whole attack.
    """
    Detailed = "Detailed"
    """
    One technique against one technology, usually with its steps set out.
    """


class CapecLikelihood(str, Enum):
    """
    How likely something is to happen.
    """
    High = "High"
    Medium = "Medium"
    Low = "Low"
    Unknown = "Unknown"
    """
    Nobody knows how likely it is.
    """


class CapecRelatedNature(str, Enum):
    """
    How one attack pattern relates to another.
    """
    ChildOf = "ChildOf"
    """
    The other pattern is more abstract, and this one specialises it.
    """
    ParentOf = "ParentOf"
    """
    The other pattern is less abstract, and it specialises this one.
    """
    CanFollow = "CanFollow"
    """
    In a chain of attack, this pattern may come after the other.
    """
    CanPrecede = "CanPrecede"
    """
    In a chain of attack, this pattern may come before the other.
    """
    CanAlsoBe = "CanAlsoBe"
    """
    In some settings this pattern can also be read as the other one, though not always the reverse.
    """
    PeerOf = "PeerOf"
    """
    The two are alike in a way that no other nature covers.
    """


class CapecScope(str, Enum):
    """
    The security property that a consequence violates.
    """
    Confidentiality = "Confidentiality"
    Integrity = "Integrity"
    Availability = "Availability"
    Access_Control = "Access Control"
    Accountability = "Accountability"
    Authentication = "Authentication"
    Authorization = "Authorization"
    Non_Repudiation = "Non-Repudiation"
    Other = "Other"


class CapecSeverity(str, Enum):
    """
    How bad the typical outcome of an attack is.
    """
    Very_High = "Very High"
    High = "High"
    Medium = "Medium"
    Low = "Low"
    Very_Low = "Very Low"


class CapecSkillLevel(str, Enum):
    """
    How much skill or knowledge an adversary needs.
    """
    High = "High"
    Medium = "Medium"
    Low = "Low"
    Unknown = "Unknown"
    """
    Nobody knows how much is needed.
    """


class CapecStakeholderType(str, Enum):
    """
    The kinds of people a view is meant for.
    """
    Academic_Researchers = "Academic Researchers"
    Applied_Researchers = "Applied Researchers"
    Assessment_Customers = "Assessment Customers"
    Assessment_Vendors = "Assessment Vendors"
    CAPEC_Team = "CAPEC Team"
    Educators = "Educators"
    Information_Providers = "Information Providers"
    Software_Customers = "Software Customers"
    Software_Designers = "Software Designers"
    Software_Developers = "Software Developers"
    Software_Vendors = "Software Vendors"
    Other = "Other"


class CapecTechnicalImpact(str, Enum):
    """
    What a successful attack does to the system, in technical terms.
    """
    Modify_Data = "Modify Data"
    Read_Data = "Read Data"
    Unreliable_Execution = "Unreliable Execution"
    Resource_Consumption = "Resource Consumption"
    Execute_Unauthorized_Commands = "Execute Unauthorized Commands"
    Gain_Privileges = "Gain Privileges"
    Bypass_Protection_Mechanism = "Bypass Protection Mechanism"
    Hide_Activities = "Hide Activities"
    Alter_Execution_Logic = "Alter Execution Logic"
    Other = "Other"


class CapecViewType(str, Enum):
    """
    How a view selects its entries.
    """
    Implicit = "Implicit"
    """
    A slice picked by a filter on an attribute, such as every pattern of one status.
    """
    Explicit = "Explicit"
    """
    A slice picked by hand because of something outside the catalogue, such as a list.
    """
    Graph = "Graph"
    """
    A hierarchy seen from one standpoint, often from category down to detailed pattern.
    """


class CapecAttackStepPhase(str, Enum):
    """
    Which stage of an attack a step belongs to.
    """
    Explore = "Explore"
    Experiment = "Experiment"
    Exploit = "Exploit"



class CapecExternalReference(ConfiguredBaseModel):
    """
    A publication or page outside CAPEC that entries point to for more detail.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'annotations': {'xsd_type': {'tag': 'xsd_type',
                                      'value': 'ExternalReferenceType'}},
         'close_mappings': ['stix:StixExternalReference',
                            'sepses_capec:Reference',
                            'cwe:CweExternalReference'],
         'from_schema': 'https://w3id.org/lmodel/capec/capec_core'})

    Reference_ID: str = Field(default=..., description="""The identifier entries use to cite this reference.""", json_schema_extra = { "linkml_meta": {'broad_mappings': ['dcterms:identifier'],
         'domain_of': ['CapecExternalReference']} })
    Author: Optional[list[str]] = Field(default=None, description="""A person or body who wrote the work.""", json_schema_extra = { "linkml_meta": {'close_mappings': ['dcterms:creator', 'sepses_capec:referenceAuthor'],
         'domain_of': ['CapecExternalReference']} })
    Title: str = Field(default=..., description="""The work's title.""", json_schema_extra = { "linkml_meta": {'close_mappings': ['dcterms:title', 'sepses_capec:referenceTitle'],
         'domain_of': ['CapecExternalReference']} })
    Edition: Optional[str] = Field(default=None, description="""Which edition of the work is meant.""", json_schema_extra = { "linkml_meta": {'close_mappings': ['schema:bookEdition'],
         'domain_of': ['CapecExternalReference']} })
    Publication: Optional[str] = Field(default=None, description="""The journal, conference or larger work that holds it.""", json_schema_extra = { "linkml_meta": {'domain_of': ['CapecExternalReference']} })
    Publication_Year: Optional[str] = Field(default=None, description="""The year it appeared.""", json_schema_extra = { "linkml_meta": {'close_mappings': ['sepses_capec:referencePublicationYear'],
         'domain_of': ['CapecExternalReference']} })
    Publication_Month: Optional[str] = Field(default=None, description="""The month it appeared.""", json_schema_extra = { "linkml_meta": {'close_mappings': ['sepses_capec:referencePublicationMonth'],
         'domain_of': ['CapecExternalReference']} })
    Publication_Day: Optional[str] = Field(default=None, description="""The day of the month it appeared.""", json_schema_extra = { "linkml_meta": {'close_mappings': ['sepses_capec:referencePublicationDay'],
         'domain_of': ['CapecExternalReference']} })
    Publisher: Optional[str] = Field(default=None, description="""Who published it.""", json_schema_extra = { "linkml_meta": {'close_mappings': ['dcterms:publisher', 'sepses_capec:referencePublisher'],
         'domain_of': ['CapecExternalReference']} })
    URL: Optional[str] = Field(default=None, description="""Where it can be read.""", json_schema_extra = { "linkml_meta": {'close_mappings': ['schema:url', 'sepses_capec:referenceUrl'],
         'domain_of': ['CapecExternalReference']} })
    URL_Date: Optional[date] = Field(default=None, description="""The day someone last confirmed the address worked.""", json_schema_extra = { "linkml_meta": {'domain_of': ['CapecExternalReference']} })


class CapecReference(ConfiguredBaseModel):
    """
    One citation by an entry of an external reference.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'annotations': {'xsd_type': {'tag': 'xsd_type',
                                      'value': 'ReferencesType/Reference'}},
         'from_schema': 'https://w3id.org/lmodel/capec/capec_core'})

    External_Reference_ID: str = Field(default=..., description="""The reference cited.""", json_schema_extra = { "linkml_meta": {'domain_of': ['CapecReference']} })
    Section: Optional[str] = Field(default=None, description="""The section title or page that this citation means.""", json_schema_extra = { "linkml_meta": {'domain_of': ['CapecReference']} })

    @field_validator('External_Reference_ID')
    def pattern_External_Reference_ID(cls, v):
        pattern=re.compile(r"^REF-[0-9]+$")
        if isinstance(v, list):
            for element in v:
                if isinstance(element, str) and not pattern.search(element):
                    err_msg = f"Invalid External_Reference_ID format: {element}"
                    raise ValueError(err_msg)
        elif isinstance(v, str) and not pattern.search(v):
            err_msg = f"Invalid External_Reference_ID format: {v}"
            raise ValueError(err_msg)
        return v


class CapecNote(ConfiguredBaseModel):
    """
    A remark on an entry that no other field can hold.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'annotations': {'xsd_type': {'tag': 'xsd_type', 'value': 'NotesType/Note'}},
         'close_mappings': ['skos:note'],
         'from_schema': 'https://w3id.org/lmodel/capec/capec_core'})

    Type: CapecNoteType = Field(default=..., description="""What kind of remark it is.""", json_schema_extra = { "linkml_meta": {'domain_of': ['CapecNote',
                       'CapecContribution',
                       'CapecStakeholder',
                       'CapecView']} })
    Value: str = Field(default=..., description="""The remark itself.""", json_schema_extra = { "linkml_meta": {'domain_of': ['CapecNote',
                       'CapecPreviousEntryName',
                       'CapecTechnique',
                       'CapecSkill']} })


class CapecTaxonomyMapping(ConfiguredBaseModel):
    """
    A link from an entry to the matching entry of another taxonomy.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'annotations': {'xsd_type': {'tag': 'xsd_type',
                                      'value': 'TaxonomyMappingsType/Taxonomy_Mapping'}},
         'close_mappings': ['skos:mappingRelation'],
         'from_schema': 'https://w3id.org/lmodel/capec/capec_core'})

    Taxonomy_Name: CapecTaxonomyName = Field(default=..., description="""The other taxonomy.""", json_schema_extra = { "linkml_meta": {'domain_of': ['CapecTaxonomyMapping']} })
    Entry_ID: Optional[str] = Field(default=None, description="""The other entry's identifier in that taxonomy.""", json_schema_extra = { "linkml_meta": {'domain_of': ['CapecTaxonomyMapping']} })
    Entry_Name: Optional[str] = Field(default=None, description="""The other entry's name in that taxonomy.""", json_schema_extra = { "linkml_meta": {'domain_of': ['CapecTaxonomyMapping']} })
    Mapping_Fit: Optional[CapecTaxonomyMappingFit] = Field(default=None, description="""How well the two entries fit.""", json_schema_extra = { "linkml_meta": {'domain_of': ['CapecTaxonomyMapping']} })


class CapecExcludeRelated(ConfiguredBaseModel):
    """
    An ancestor under which a relation does not hold.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'annotations': {'xsd_type': {'tag': 'xsd_type',
                                      'value': 'ExcludeRelatedType'}},
         'comments': ['The relation it sits on applies through every path up the '
                      'hierarchy except those through this ancestor.'],
         'from_schema': 'https://w3id.org/lmodel/capec/capec_core'})

    Exclude_ID: str = Field(default=..., description="""The number of the ancestor.""", json_schema_extra = { "linkml_meta": {'comments': ['The XSD says only that this is an ancestor, so it ranges over '
                      'any entry. Every one of the 260 in CAPEC 3.9 is a category, '
                      'which tests/test_catalogue.py pins.'],
         'domain_of': ['CapecExcludeRelated']} })

    @field_validator('Exclude_ID')
    def pattern_Exclude_ID(cls, v):
        pattern=re.compile(r"^[1-9][0-9]*$")
        if isinstance(v, list):
            for element in v:
                if isinstance(element, str) and not pattern.search(element):
                    err_msg = f"Invalid Exclude_ID format: {element}"
                    raise ValueError(err_msg)
        elif isinstance(v, str) and not pattern.search(v):
            err_msg = f"Invalid Exclude_ID format: {v}"
            raise ValueError(err_msg)
        return v


class CapecExclusionsMixin(ConfiguredBaseModel):
    """
    The field of any relation that can leave out some ancestors.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/lmodel/capec/capec_core', 'mixin': True})

    Exclude_Related: Optional[list[CapecExcludeRelated]] = Field(default=None, description="""Ancestors under which the relation does not hold.""", json_schema_extra = { "linkml_meta": {'domain_of': ['CapecExclusionsMixin']} })


class CapecTaxonomyMappedMixin(ConfiguredBaseModel):
    """
    The field of an entry that can map to other taxonomies.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/lmodel/capec/capec_core', 'mixin': True})

    Taxonomy_Mappings: Optional[list[CapecTaxonomyMapping]] = Field(default=None, description="""Matching entries in other taxonomies.""", json_schema_extra = { "linkml_meta": {'domain_of': ['CapecTaxonomyMappedMixin']} })


class CapecSubmission(ConfiguredBaseModel):
    """
    Who first put an entry forward, and when.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'annotations': {'xsd_type': {'tag': 'xsd_type',
                                      'value': 'ContentHistoryType/Submission'}},
         'close_mappings': ['sepses_capec:SubmissionHistory'],
         'from_schema': 'https://w3id.org/lmodel/capec/capec_core'})

    Submission_Name: Optional[str] = Field(default=None, description="""The submitter's name.""", json_schema_extra = { "linkml_meta": {'close_mappings': ['sepses_capec:submissionName'],
         'domain_of': ['CapecSubmission']} })
    Submission_Organization: Optional[str] = Field(default=None, description="""The submitter's organisation.""", json_schema_extra = { "linkml_meta": {'close_mappings': ['sepses_capec:submissionOrganization'],
         'domain_of': ['CapecSubmission']} })
    Submission_Date: Optional[date] = Field(default=None, description="""The day it was submitted.""", json_schema_extra = { "linkml_meta": {'close_mappings': ['dcterms:dateSubmitted', 'sepses_capec:submissionDate'],
         'domain_of': ['CapecSubmission']} })
    Submission_Comment: Optional[str] = Field(default=None, description="""A remark on the submission.""", json_schema_extra = { "linkml_meta": {'domain_of': ['CapecSubmission']} })


class CapecModification(ConfiguredBaseModel):
    """
    One later edit to an entry.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'annotations': {'xsd_type': {'tag': 'xsd_type',
                                      'value': 'ContentHistoryType/Modification'}},
         'close_mappings': ['sepses_capec:ModificationHistory'],
         'from_schema': 'https://w3id.org/lmodel/capec/capec_core'})

    Modification_Name: Optional[str] = Field(default=None, description="""The editor's name.""", json_schema_extra = { "linkml_meta": {'close_mappings': ['sepses_capec:modificationName'],
         'domain_of': ['CapecModification']} })
    Modification_Organization: Optional[str] = Field(default=None, description="""The editor's organisation.""", json_schema_extra = { "linkml_meta": {'close_mappings': ['sepses_capec:modificationOrganization'],
         'domain_of': ['CapecModification']} })
    Modification_Date: Optional[date] = Field(default=None, description="""The day of the edit.""", json_schema_extra = { "linkml_meta": {'close_mappings': ['dcterms:modified', 'sepses_capec:modificationDate'],
         'domain_of': ['CapecModification']} })
    Modification_Importance: Optional[CapecImportance] = Field(default=None, description="""How much the edit matters to anyone relying on the entry.""", json_schema_extra = { "linkml_meta": {'domain_of': ['CapecModification']} })
    Modification_Comment: Optional[str] = Field(default=None, description="""What the edit did.""", json_schema_extra = { "linkml_meta": {'close_mappings': ['sepses_capec:modificationComment'],
         'domain_of': ['CapecModification']} })


class CapecContribution(ConfiguredBaseModel):
    """
    Help given to an entry by someone other than its submitter.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'annotations': {'xsd_type': {'tag': 'xsd_type',
                                      'value': 'ContentHistoryType/Contribution'}},
         'from_schema': 'https://w3id.org/lmodel/capec/capec_core'})

    Type: CapecContributionType = Field(default=..., description="""Whether the help was content or feedback.""", json_schema_extra = { "linkml_meta": {'domain_of': ['CapecNote',
                       'CapecContribution',
                       'CapecStakeholder',
                       'CapecView']} })
    Contribution_Name: Optional[str] = Field(default=None, description="""The contributor's name.""", json_schema_extra = { "linkml_meta": {'domain_of': ['CapecContribution']} })
    Contribution_Organization: Optional[str] = Field(default=None, description="""The contributor's organisation.""", json_schema_extra = { "linkml_meta": {'domain_of': ['CapecContribution']} })
    Contribution_Date: Optional[date] = Field(default=None, description="""The day of the contribution.""", json_schema_extra = { "linkml_meta": {'domain_of': ['CapecContribution']} })
    Contribution_Comment: Optional[str] = Field(default=None, description="""A remark on the contribution.""", json_schema_extra = { "linkml_meta": {'domain_of': ['CapecContribution']} })


class CapecPreviousEntryName(ConfiguredBaseModel):
    """
    A name an entry used to carry.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'annotations': {'xsd_type': {'tag': 'xsd_type',
                                      'value': 'ContentHistoryType/Previous_Entry_Name'}},
         'from_schema': 'https://w3id.org/lmodel/capec/capec_core'})

    Date: date = Field(default=..., description="""The day the name changed.""", json_schema_extra = { "linkml_meta": {'domain_of': ['CapecPreviousEntryName', 'CapecAttackPatternCatalog']} })
    Value: str = Field(default=..., description="""The earlier name.""", json_schema_extra = { "linkml_meta": {'domain_of': ['CapecNote',
                       'CapecPreviousEntryName',
                       'CapecTechnique',
                       'CapecSkill']} })


class CapecContentHistory(ConfiguredBaseModel):
    """
    The record of who wrote and changed an entry.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'annotations': {'xsd_type': {'tag': 'xsd_type',
                                      'value': 'ContentHistoryType'}},
         'from_schema': 'https://w3id.org/lmodel/capec/capec_core'})

    Submission: Optional[CapecSubmission] = Field(default=None, description="""The entry's first submission.""", json_schema_extra = { "linkml_meta": {'domain_of': ['CapecContentHistory']} })
    Modification: Optional[list[CapecModification]] = Field(default=None, description="""Each later edit.""", json_schema_extra = { "linkml_meta": {'domain_of': ['CapecContentHistory']} })
    Contribution: Optional[list[CapecContribution]] = Field(default=None, description="""Each contribution from someone else.""", json_schema_extra = { "linkml_meta": {'domain_of': ['CapecContentHistory']} })
    Previous_Entry_Name: Optional[list[CapecPreviousEntryName]] = Field(default=None, description="""Each name the entry used to carry.""", json_schema_extra = { "linkml_meta": {'domain_of': ['CapecContentHistory']} })


class CapecEntry(ConfiguredBaseModel):
    """
    Anything in the catalogue with a CAPEC number, whether an attack pattern, a category or a view.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'abstract': True,
         'annotations': {'xsd_type': {'tag': 'xsd_type',
                                      'value': 'AttackPatternType CategoryType '
                                               'ViewType'}},
         'comments': ['The XSD has no such base. It repeats these fields on its three '
                      'entry types, whose numbers do not overlap, so a member '
                      'reference can point to any of them.'],
         'from_schema': 'https://w3id.org/lmodel/capec/capec_core'})

    ID: str = Field(default=..., description="""The entry's CAPEC number.""", json_schema_extra = { "linkml_meta": {'broad_mappings': ['dcterms:identifier'], 'domain_of': ['CapecEntry']} })
    Name: str = Field(default=..., description="""The entry's name.""", json_schema_extra = { "linkml_meta": {'close_mappings': ['schema:name'],
         'domain_of': ['CapecEntry', 'CapecAttackPatternCatalog']} })
    Status: CapecStatus = Field(default=..., description="""How far the entry has got through review.""", json_schema_extra = { "linkml_meta": {'close_mappings': ['sepses_capec:status'], 'domain_of': ['CapecEntry']} })
    References: Optional[list[CapecReference]] = Field(default=None, description="""The external references the entry cites.""", json_schema_extra = { "linkml_meta": {'close_mappings': ['sepses_capec:hasReference'], 'domain_of': ['CapecEntry']} })
    Notes: Optional[list[CapecNote]] = Field(default=None, description="""Remarks that no other field can hold.""", json_schema_extra = { "linkml_meta": {'domain_of': ['CapecEntry']} })
    Content_History: Optional[CapecContentHistory] = Field(default=None, description="""Who wrote and changed the entry.""", json_schema_extra = { "linkml_meta": {'domain_of': ['CapecEntry']} })


class CapecAlternateTerm(ConfiguredBaseModel):
    """
    Another name by which an attack pattern is known.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'annotations': {'xsd_type': {'tag': 'xsd_type',
                                      'value': 'AlternateTermsType/Alternate_Term'}},
         'from_schema': 'https://w3id.org/lmodel/capec/capec_entries'})

    Term: str = Field(default=..., description="""The other name.""", json_schema_extra = { "linkml_meta": {'close_mappings': ['skos:altLabel'], 'domain_of': ['CapecAlternateTerm']} })
    Description: Optional[str] = Field(default=None, description="""Where or how the other name is used.""", json_schema_extra = { "linkml_meta": {'domain_of': ['CapecAlternateTerm',
                       'CapecAttackStep',
                       'CapecStakeholder',
                       'CapecAttackPattern']} })


class CapecRelatedAttackPattern(CapecExclusionsMixin):
    """
    A relation from one attack pattern to another.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'annotations': {'xsd_type': {'tag': 'xsd_type',
                                      'value': 'RelatedAttackPatternType/Related_Attack_Pattern'}},
         'close_mappings': ['sepses_capec:RelatedAttackPattern'],
         'from_schema': 'https://w3id.org/lmodel/capec/capec_entries',
         'mixins': ['CapecExclusionsMixin']})

    Nature: CapecRelatedNature = Field(default=..., description="""What kind of relation it is.""", json_schema_extra = { "linkml_meta": {'close_mappings': ['sepses_capec:relatedAttackPatternNature'],
         'domain_of': ['CapecRelatedAttackPattern']} })
    CAPEC_ID: str = Field(default=..., description="""The other attack pattern.""", json_schema_extra = { "linkml_meta": {'close_mappings': ['sepses_capec:relatedAttackPatternCAPECId'],
         'domain_of': ['CapecRelatedAttackPattern',
                       'CapecTechnique',
                       'CapecMemberOf',
                       'CapecHasMember']} })
    Exclude_Related: Optional[list[CapecExcludeRelated]] = Field(default=None, description="""Ancestors under which the relation does not hold.""", json_schema_extra = { "linkml_meta": {'domain_of': ['CapecExclusionsMixin']} })

    @field_validator('CAPEC_ID')
    def pattern_CAPEC_ID(cls, v):
        pattern=re.compile(r"^[1-9][0-9]*$")
        if isinstance(v, list):
            for element in v:
                if isinstance(element, str) and not pattern.search(element):
                    err_msg = f"Invalid CAPEC_ID format: {element}"
                    raise ValueError(err_msg)
        elif isinstance(v, str) and not pattern.search(v):
            err_msg = f"Invalid CAPEC_ID format: {v}"
            raise ValueError(err_msg)
        return v


class CapecTechnique(ConfiguredBaseModel):
    """
    One way of carrying out a step of an attack.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'annotations': {'xsd_type': {'tag': 'xsd_type',
                                      'value': 'ExecutionFlowType/Attack_Step/Technique'}},
         'from_schema': 'https://w3id.org/lmodel/capec/capec_entries'})

    CAPEC_ID: Optional[str] = Field(default=None, description="""The entry that the technique itself amounts to.""", json_schema_extra = { "linkml_meta": {'comments': ['The XSD types this one as xs:string and not as a number, and no '
                      'technique in CAPEC 3.9 sets it. It has no pattern, so any '
                      'string validates as the XSD allows, and it ranges over an entry '
                      'so that the key means one thing.'],
         'domain_of': ['CapecRelatedAttackPattern',
                       'CapecTechnique',
                       'CapecMemberOf',
                       'CapecHasMember']} })
    Value: str = Field(default=..., description="""The technique.""", json_schema_extra = { "linkml_meta": {'domain_of': ['CapecNote',
                       'CapecPreviousEntryName',
                       'CapecTechnique',
                       'CapecSkill']} })


class CapecAttackStep(ConfiguredBaseModel):
    """
    One step of the way an adversary typically carries out an attack.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'annotations': {'xsd_type': {'tag': 'xsd_type',
                                      'value': 'ExecutionFlowType/Attack_Step'}},
         'close_mappings': ['sepses_capec:ExecutionFlow'],
         'comments': ['Eleven flows in CAPEC 3.9 repeat a step number, as in 1, 1, 2, '
                      '1, and the XSD does not ask for a sequence, so no rule states '
                      'one.'],
         'from_schema': 'https://w3id.org/lmodel/capec/capec_entries'})

    Step: int = Field(default=..., description="""The step's number.""", json_schema_extra = { "linkml_meta": {'close_mappings': ['sepses_capec:attackStep'],
         'domain_of': ['CapecAttackStep']} })
    Phase: CapecAttackStepPhase = Field(default=..., description="""The stage of the attack it belongs to.""", json_schema_extra = { "linkml_meta": {'close_mappings': ['sepses_capec:attackStepPhase'],
         'domain_of': ['CapecAttackStep']} })
    Description: str = Field(default=..., description="""What the adversary does in this step.""", json_schema_extra = { "linkml_meta": {'close_mappings': ['sepses_capec:attackStepDescription'],
         'domain_of': ['CapecAlternateTerm',
                       'CapecAttackStep',
                       'CapecStakeholder',
                       'CapecAttackPattern']} })
    Technique: Optional[list[CapecTechnique]] = Field(default=None, description="""Ways of doing it.""", json_schema_extra = { "linkml_meta": {'close_mappings': ['sepses_capec:attackStepTechnique'],
         'domain_of': ['CapecAttackStep']} })


class CapecSkill(ConfiguredBaseModel):
    """
    A skill or piece of knowledge an adversary needs.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'annotations': {'xsd_type': {'tag': 'xsd_type', 'value': 'SkillsType/Skill'}},
         'close_mappings': ['sepses_capec:SkillRequired'],
         'from_schema': 'https://w3id.org/lmodel/capec/capec_entries'})

    Level: CapecSkillLevel = Field(default=..., description="""How much of it is needed.""", json_schema_extra = { "linkml_meta": {'close_mappings': ['sepses_capec:skillLevel'], 'domain_of': ['CapecSkill']} })
    Value: str = Field(default=..., description="""What the skill is.""", json_schema_extra = { "linkml_meta": {'close_mappings': ['sepses_capec:skillDescription'],
         'comments': ['The XSD allows this text to be empty, and in two skills of '
                      'CAPEC 3.9 it is.'],
         'domain_of': ['CapecNote',
                       'CapecPreviousEntryName',
                       'CapecTechnique',
                       'CapecSkill']} })


class CapecConsequence(ConfiguredBaseModel):
    """
    One thing that can happen if an attack succeeds.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'annotations': {'xsd_type': {'tag': 'xsd_type',
                                      'value': 'ConsequencesType/Consequence'}},
         'close_mappings': ['sepses_capec:Consequence'],
         'from_schema': 'https://w3id.org/lmodel/capec/capec_entries'})

    Consequence_ID: Optional[str] = Field(default=None, description="""The CAPEC team's identifier for a consequence repeated across patterns, in the form CC-1.""", json_schema_extra = { "linkml_meta": {'domain_of': ['CapecConsequence']} })
    Scope: list[CapecScope] = Field(default=..., description="""The security properties violated.""", json_schema_extra = { "linkml_meta": {'close_mappings': ['sepses_capec:consequenceScope'],
         'domain_of': ['CapecConsequence']} })
    Impact: Optional[list[CapecTechnicalImpact]] = Field(default=None, description="""What the attack does to the system.""", json_schema_extra = { "linkml_meta": {'close_mappings': ['sepses_capec:consequenceImpact'],
         'domain_of': ['CapecConsequence']} })
    Likelihood: Optional[CapecLikelihood] = Field(default=None, description="""How likely this consequence is, beside the pattern's others.""", json_schema_extra = { "linkml_meta": {'domain_of': ['CapecConsequence']} })
    Note: Optional[str] = Field(default=None, description="""A remark on the consequence.""", json_schema_extra = { "linkml_meta": {'close_mappings': ['sepses_capec:consequenceNote'],
         'domain_of': ['CapecConsequence']} })


class CapecRelatedWeakness(ConfiguredBaseModel):
    """
    A weakness in the Common Weakness Enumeration that can make an attack possible.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'annotations': {'xsd_type': {'tag': 'xsd_type',
                                      'value': 'RelatedWeaknessesType/Related_Weakness'}},
         'close_mappings': ['sepses_capec:RelatedWeakness'],
         'comments': ["The XSD says that any one of a pattern's weaknesses, not all of "
                      'them, may be enough for the attack to succeed.',
                      'CWE holds the same link from its own side. CAPEC 3.9 and CWE '
                      '5.0 each name the same 1212 pairs, which '
                      'tests/test_catalogue.py holds, so the two classes are the two '
                      'ends of one link and the mapping is related.'],
         'from_schema': 'https://w3id.org/lmodel/capec/capec_entries',
         'related_mappings': ['cwe:CweRelatedAttackPattern']})

    CWE_ID: str = Field(default=..., description="""The weakness's number in the Common Weakness Enumeration.""", json_schema_extra = { "linkml_meta": {'domain_of': ['CapecRelatedWeakness'],
         'exact_mappings': ['wdt:P3624'],
         'related_mappings': ['cwe:CweWeakness']} })


class CapecMemberOf(CapecExclusionsMixin):
    """
    A statement that an entry belongs to a view or a category.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'annotations': {'xsd_type': {'tag': 'xsd_type',
                                      'value': 'RelationshipsType/Member_Of'}},
         'from_schema': 'https://w3id.org/lmodel/capec/capec_entries',
         'mixins': ['CapecExclusionsMixin']})

    CAPEC_ID: str = Field(default=..., description="""The view or category it belongs to.""", json_schema_extra = { "linkml_meta": {'domain_of': ['CapecRelatedAttackPattern',
                       'CapecTechnique',
                       'CapecMemberOf',
                       'CapecHasMember']} })
    Exclude_Related: Optional[list[CapecExcludeRelated]] = Field(default=None, description="""Ancestors under which the relation does not hold.""", json_schema_extra = { "linkml_meta": {'domain_of': ['CapecExclusionsMixin']} })

    @field_validator('CAPEC_ID')
    def pattern_CAPEC_ID(cls, v):
        pattern=re.compile(r"^[1-9][0-9]*$")
        if isinstance(v, list):
            for element in v:
                if isinstance(element, str) and not pattern.search(element):
                    err_msg = f"Invalid CAPEC_ID format: {element}"
                    raise ValueError(err_msg)
        elif isinstance(v, str) and not pattern.search(v):
            err_msg = f"Invalid CAPEC_ID format: {v}"
            raise ValueError(err_msg)
        return v


class CapecHasMember(CapecExclusionsMixin):
    """
    A statement that a view or a category holds an entry.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'annotations': {'xsd_type': {'tag': 'xsd_type',
                                      'value': 'RelationshipsType/Has_Member'}},
         'from_schema': 'https://w3id.org/lmodel/capec/capec_entries',
         'mixins': ['CapecExclusionsMixin']})

    CAPEC_ID: str = Field(default=..., description="""The attack pattern or category it holds.""", json_schema_extra = { "linkml_meta": {'domain_of': ['CapecRelatedAttackPattern',
                       'CapecTechnique',
                       'CapecMemberOf',
                       'CapecHasMember']} })
    Exclude_Related: Optional[list[CapecExcludeRelated]] = Field(default=None, description="""Ancestors under which the relation does not hold.""", json_schema_extra = { "linkml_meta": {'domain_of': ['CapecExclusionsMixin']} })

    @field_validator('CAPEC_ID')
    def pattern_CAPEC_ID(cls, v):
        pattern=re.compile(r"^[1-9][0-9]*$")
        if isinstance(v, list):
            for element in v:
                if isinstance(element, str) and not pattern.search(element):
                    err_msg = f"Invalid CAPEC_ID format: {element}"
                    raise ValueError(err_msg)
        elif isinstance(v, str) and not pattern.search(v):
            err_msg = f"Invalid CAPEC_ID format: {v}"
            raise ValueError(err_msg)
        return v


class CapecRelationships(ConfiguredBaseModel):
    """
    Which entries a category or a view holds, and which it belongs to.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'annotations': {'xsd_type': {'tag': 'xsd_type', 'value': 'RelationshipsType'}},
         'from_schema': 'https://w3id.org/lmodel/capec/capec_entries'})

    Member_Of: Optional[list[CapecMemberOf]] = Field(default=None, description="""What this entry belongs to.""", json_schema_extra = { "linkml_meta": {'domain_of': ['CapecRelationships']} })
    Has_Member: Optional[list[CapecHasMember]] = Field(default=None, description="""What this entry holds.""", json_schema_extra = { "linkml_meta": {'domain_of': ['CapecRelationships']} })


class CapecStakeholder(ConfiguredBaseModel):
    """
    One kind of person a view is meant for, and what they would get from it.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'annotations': {'xsd_type': {'tag': 'xsd_type',
                                      'value': 'AudienceType/Stakeholder'}},
         'from_schema': 'https://w3id.org/lmodel/capec/capec_entries'})

    Type: CapecStakeholderType = Field(default=..., description="""The kind of person.""", json_schema_extra = { "linkml_meta": {'domain_of': ['CapecNote',
                       'CapecContribution',
                       'CapecStakeholder',
                       'CapecView']} })
    Description: str = Field(default=..., description="""What they would find useful in the view.""", json_schema_extra = { "linkml_meta": {'domain_of': ['CapecAlternateTerm',
                       'CapecAttackStep',
                       'CapecStakeholder',
                       'CapecAttackPattern']} })


class CapecAttackPattern(CapecEntry, CapecTaxonomyMappedMixin):
    """
    A catalogued way that adversaries go about an attack, with what it takes and how to resist it.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'annotations': {'xsd_type': {'tag': 'xsd_type', 'value': 'AttackPatternType'}},
         'close_mappings': ['stix:StixAttackPattern',
                            'sepses_capec:CAPEC',
                            'schema:DefinedTerm',
                            'skos:Concept'],
         'comments': ['MITRE publishes the same entries in STIX as attack-pattern '
                      'objects, in the mitre/cti repository, and marks each with a '
                      'capec external reference, so the STIX mapping is close.',
                      'ATT&CK describes a technique an adversary was seen to use, '
                      'while this describes a general pattern, and the taxonomy '
                      'mappings join them, so that mapping is only related.'],
         'from_schema': 'https://w3id.org/lmodel/capec/capec_entries',
         'mixins': ['CapecTaxonomyMappedMixin'],
         'related_mappings': ['attack:AttackTechnique']})

    Abstraction: CapecAbstraction = Field(default=..., description="""How concrete the pattern is.""", json_schema_extra = { "linkml_meta": {'close_mappings': ['sepses_capec:abstraction'],
         'domain_of': ['CapecAttackPattern']} })
    Description: str = Field(default=..., description="""The pattern, in a few sentences.""", json_schema_extra = { "linkml_meta": {'close_mappings': ['dcterms:description', 'schema:description'],
         'domain_of': ['CapecAlternateTerm',
                       'CapecAttackStep',
                       'CapecStakeholder',
                       'CapecAttackPattern']} })
    Extended_Description: Optional[str] = Field(default=None, description="""A longer account of the pattern.""", json_schema_extra = { "linkml_meta": {'domain_of': ['CapecAttackPattern']} })
    Alternate_Terms: Optional[list[CapecAlternateTerm]] = Field(default=None, description="""Other names for the pattern.""", json_schema_extra = { "linkml_meta": {'close_mappings': ['stix:aliases'], 'domain_of': ['CapecAttackPattern']} })
    Likelihood_Of_Attack: Optional[CapecLikelihood] = Field(default=None, description="""How likely an attack of this kind is to succeed.""", json_schema_extra = { "linkml_meta": {'close_mappings': ['sepses_capec:likelihoodOfAttack'],
         'domain_of': ['CapecAttackPattern']} })
    Typical_Severity: Optional[CapecSeverity] = Field(default=None, description="""How bad the outcome usually is.""", json_schema_extra = { "linkml_meta": {'close_mappings': ['sepses_capec:typicalSeverity'],
         'domain_of': ['CapecAttackPattern']} })
    Related_Attack_Patterns: Optional[list[CapecRelatedAttackPattern]] = Field(default=None, description="""The pattern's relations to others.""", json_schema_extra = { "linkml_meta": {'close_mappings': ['sepses_capec:hasRelatedAttackPattern'],
         'domain_of': ['CapecAttackPattern']} })
    Execution_Flow: Optional[list[CapecAttackStep]] = Field(default=None, description="""The steps an adversary typically takes.""", json_schema_extra = { "linkml_meta": {'close_mappings': ['sepses_capec:hasExecutionFlow'],
         'domain_of': ['CapecAttackPattern']} })
    Prerequisites: Optional[list[str]] = Field(default=None, description="""Conditions that must hold for the attack to work.""", json_schema_extra = { "linkml_meta": {'close_mappings': ['sepses_capec:prerequisite'],
         'domain_of': ['CapecAttackPattern']} })
    Skills_Required: Optional[list[CapecSkill]] = Field(default=None, description="""The skills an adversary needs.""", json_schema_extra = { "linkml_meta": {'close_mappings': ['sepses_capec:hasSkillRequired'],
         'domain_of': ['CapecAttackPattern']} })
    Resources_Required: Optional[list[str]] = Field(default=None, description="""What an adversary must have to hand, such as tools or addresses.""", json_schema_extra = { "linkml_meta": {'close_mappings': ['sepses_capec:resourceRequired'],
         'domain_of': ['CapecAttackPattern']} })
    Indicators: Optional[list[str]] = Field(default=None, description="""Signs that an attack is near, under way or over.""", json_schema_extra = { "linkml_meta": {'close_mappings': ['sepses_capec:indicator'],
         'domain_of': ['CapecAttackPattern']} })
    Consequences: Optional[list[CapecConsequence]] = Field(default=None, description="""What can happen if the attack succeeds.""", json_schema_extra = { "linkml_meta": {'close_mappings': ['sepses_capec:hasConsequence'],
         'domain_of': ['CapecAttackPattern']} })
    Mitigations: Optional[list[str]] = Field(default=None, description="""Ways to prevent the attack or lessen its harm.""", json_schema_extra = { "linkml_meta": {'close_mappings': ['sepses_capec:hasMitigation'],
         'comments': ['The mitre/cti repository publishes each of these as a STIX '
                      'course-of-action joined by a mitigates relationship, so that '
                      'mapping is only related.'],
         'domain_of': ['CapecAttackPattern'],
         'related_mappings': ['stix:StixCourseOfAction']} })
    Example_Instances: Optional[list[str]] = Field(default=None, description="""Concrete examples of the attack.""", json_schema_extra = { "linkml_meta": {'close_mappings': ['skos:example'], 'domain_of': ['CapecAttackPattern']} })
    Related_Weaknesses: Optional[list[CapecRelatedWeakness]] = Field(default=None, description="""The weaknesses that can make the attack possible.""", json_schema_extra = { "linkml_meta": {'close_mappings': ['sepses_capec:hasRelatedWeakness'],
         'domain_of': ['CapecAttackPattern']} })
    Taxonomy_Mappings: Optional[list[CapecTaxonomyMapping]] = Field(default=None, description="""Matching entries in other taxonomies.""", json_schema_extra = { "linkml_meta": {'domain_of': ['CapecTaxonomyMappedMixin']} })
    ID: str = Field(default=..., description="""The entry's CAPEC number.""", json_schema_extra = { "linkml_meta": {'broad_mappings': ['dcterms:identifier'], 'domain_of': ['CapecEntry']} })
    Name: str = Field(default=..., description="""The entry's name.""", json_schema_extra = { "linkml_meta": {'close_mappings': ['schema:name'],
         'domain_of': ['CapecEntry', 'CapecAttackPatternCatalog']} })
    Status: CapecStatus = Field(default=..., description="""How far the entry has got through review.""", json_schema_extra = { "linkml_meta": {'close_mappings': ['sepses_capec:status'], 'domain_of': ['CapecEntry']} })
    References: Optional[list[CapecReference]] = Field(default=None, description="""The external references the entry cites.""", json_schema_extra = { "linkml_meta": {'close_mappings': ['sepses_capec:hasReference'], 'domain_of': ['CapecEntry']} })
    Notes: Optional[list[CapecNote]] = Field(default=None, description="""Remarks that no other field can hold.""", json_schema_extra = { "linkml_meta": {'domain_of': ['CapecEntry']} })
    Content_History: Optional[CapecContentHistory] = Field(default=None, description="""Who wrote and changed the entry.""", json_schema_extra = { "linkml_meta": {'domain_of': ['CapecEntry']} })


class CapecCategory(CapecEntry, CapecTaxonomyMappedMixin):
    """
    A group of attack patterns that share an effect or intent, and not itself a pattern of attack.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'annotations': {'xsd_type': {'tag': 'xsd_type', 'value': 'CategoryType'}},
         'close_mappings': ['skos:Collection'],
         'from_schema': 'https://w3id.org/lmodel/capec/capec_entries',
         'mixins': ['CapecTaxonomyMappedMixin']})

    Summary: str = Field(default=..., description="""What the patterns in this category have in common.""", json_schema_extra = { "linkml_meta": {'close_mappings': ['dcterms:description'], 'domain_of': ['CapecCategory']} })
    Relationships: Optional[CapecRelationships] = Field(default=None, description="""What the category holds and belongs to.""", json_schema_extra = { "linkml_meta": {'domain_of': ['CapecCategory']} })
    Taxonomy_Mappings: Optional[list[CapecTaxonomyMapping]] = Field(default=None, description="""Matching entries in other taxonomies.""", json_schema_extra = { "linkml_meta": {'domain_of': ['CapecTaxonomyMappedMixin']} })
    ID: str = Field(default=..., description="""The entry's CAPEC number.""", json_schema_extra = { "linkml_meta": {'broad_mappings': ['dcterms:identifier'], 'domain_of': ['CapecEntry']} })
    Name: str = Field(default=..., description="""The entry's name.""", json_schema_extra = { "linkml_meta": {'close_mappings': ['schema:name'],
         'domain_of': ['CapecEntry', 'CapecAttackPatternCatalog']} })
    Status: CapecStatus = Field(default=..., description="""How far the entry has got through review.""", json_schema_extra = { "linkml_meta": {'close_mappings': ['sepses_capec:status'], 'domain_of': ['CapecEntry']} })
    References: Optional[list[CapecReference]] = Field(default=None, description="""The external references the entry cites.""", json_schema_extra = { "linkml_meta": {'close_mappings': ['sepses_capec:hasReference'], 'domain_of': ['CapecEntry']} })
    Notes: Optional[list[CapecNote]] = Field(default=None, description="""Remarks that no other field can hold.""", json_schema_extra = { "linkml_meta": {'domain_of': ['CapecEntry']} })
    Content_History: Optional[CapecContentHistory] = Field(default=None, description="""Who wrote and changed the entry.""", json_schema_extra = { "linkml_meta": {'domain_of': ['CapecEntry']} })


class CapecView(CapecEntry):
    """
    One way of looking over the catalogue, by a hierarchy or by a slice of its entries.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'annotations': {'xsd_type': {'tag': 'xsd_type', 'value': 'ViewType'}},
         'comments': ['A graph view reads as a concept scheme, while a slice is only a '
                      'selection, so the mapping is related.'],
         'from_schema': 'https://w3id.org/lmodel/capec/capec_entries',
         'related_mappings': ['skos:ConceptScheme']})

    Type: CapecViewType = Field(default=..., description="""How the view selects its entries.""", json_schema_extra = { "linkml_meta": {'domain_of': ['CapecNote',
                       'CapecContribution',
                       'CapecStakeholder',
                       'CapecView']} })
    Objective: str = Field(default=..., description="""What the view is for.""", json_schema_extra = { "linkml_meta": {'close_mappings': ['dcterms:description'], 'domain_of': ['CapecView']} })
    Audience: Optional[list[CapecStakeholder]] = Field(default=None, description="""Who the view is meant for.""", json_schema_extra = { "linkml_meta": {'domain_of': ['CapecView']} })
    Members: Optional[CapecRelationships] = Field(default=None, description="""The entries the view holds.""", json_schema_extra = { "linkml_meta": {'domain_of': ['CapecView']} })
    Filter: Optional[str] = Field(default=None, description="""A query over the catalogue that selects the view's entries.""", json_schema_extra = { "linkml_meta": {'comments': ['The XSD calls this an XSL query. Eight of the nine in CAPEC 3.9 '
                      "are XPath 1.0, and view 553's is XPath 2.0."],
         'domain_of': ['CapecView']} })
    ID: str = Field(default=..., description="""The entry's CAPEC number.""", json_schema_extra = { "linkml_meta": {'broad_mappings': ['dcterms:identifier'], 'domain_of': ['CapecEntry']} })
    Name: str = Field(default=..., description="""The entry's name.""", json_schema_extra = { "linkml_meta": {'close_mappings': ['schema:name'],
         'domain_of': ['CapecEntry', 'CapecAttackPatternCatalog']} })
    Status: CapecStatus = Field(default=..., description="""How far the entry has got through review.""", json_schema_extra = { "linkml_meta": {'close_mappings': ['sepses_capec:status'], 'domain_of': ['CapecEntry']} })
    References: Optional[list[CapecReference]] = Field(default=None, description="""The external references the entry cites.""", json_schema_extra = { "linkml_meta": {'close_mappings': ['sepses_capec:hasReference'], 'domain_of': ['CapecEntry']} })
    Notes: Optional[list[CapecNote]] = Field(default=None, description="""Remarks that no other field can hold.""", json_schema_extra = { "linkml_meta": {'domain_of': ['CapecEntry']} })
    Content_History: Optional[CapecContentHistory] = Field(default=None, description="""Who wrote and changed the entry.""", json_schema_extra = { "linkml_meta": {'domain_of': ['CapecEntry']} })


class CapecAttackPatternCatalog(ConfiguredBaseModel):
    """
    One release of the whole catalogue, with its entries and the references they share.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'annotations': {'xsd_type': {'tag': 'xsd_type',
                                      'value': 'Attack_Pattern_Catalog'}},
         'close_mappings': ['schema:DefinedTermSet', 'skos:ConceptScheme'],
         'comments': ["Wikidata's item is the catalogue in general and this class is "
                      'one release of it, so the item is related.'],
         'from_schema': 'https://w3id.org/lmodel/capec',
         'related_mappings': ['wd:Q2986817'],
         'tree_root': True})

    Name: str = Field(default=..., description="""The catalogue's name.""", json_schema_extra = { "linkml_meta": {'close_mappings': ['schema:name'],
         'domain_of': ['CapecEntry', 'CapecAttackPatternCatalog']} })
    Version: str = Field(default=..., description="""The catalogue's version, which together with its name identifies it.""", json_schema_extra = { "linkml_meta": {'close_mappings': ['schema:version'],
         'domain_of': ['CapecAttackPatternCatalog']} })
    Date: date = Field(default=..., description="""The day this catalogue was made or last updated.""", json_schema_extra = { "linkml_meta": {'close_mappings': ['dcterms:date'],
         'domain_of': ['CapecPreviousEntryName', 'CapecAttackPatternCatalog']} })
    Attack_Patterns: Optional[list[CapecAttackPattern]] = Field(default=None, description="""The attack patterns.""", json_schema_extra = { "linkml_meta": {'domain_of': ['CapecAttackPatternCatalog']} })
    Categories: Optional[list[CapecCategory]] = Field(default=None, description="""The categories.""", json_schema_extra = { "linkml_meta": {'domain_of': ['CapecAttackPatternCatalog']} })
    Views: Optional[list[CapecView]] = Field(default=None, description="""The views.""", json_schema_extra = { "linkml_meta": {'domain_of': ['CapecAttackPatternCatalog']} })
    External_References: Optional[list[CapecExternalReference]] = Field(default=None, description="""The external references that entries cite.""", json_schema_extra = { "linkml_meta": {'domain_of': ['CapecAttackPatternCatalog']} })


# Model rebuild
# see https://pydantic-docs.helpmanual.io/usage/models/#rebuilding-a-model
CapecExternalReference.model_rebuild()
CapecReference.model_rebuild()
CapecNote.model_rebuild()
CapecTaxonomyMapping.model_rebuild()
CapecExcludeRelated.model_rebuild()
CapecExclusionsMixin.model_rebuild()
CapecTaxonomyMappedMixin.model_rebuild()
CapecSubmission.model_rebuild()
CapecModification.model_rebuild()
CapecContribution.model_rebuild()
CapecPreviousEntryName.model_rebuild()
CapecContentHistory.model_rebuild()
CapecEntry.model_rebuild()
CapecAlternateTerm.model_rebuild()
CapecRelatedAttackPattern.model_rebuild()
CapecTechnique.model_rebuild()
CapecAttackStep.model_rebuild()
CapecSkill.model_rebuild()
CapecConsequence.model_rebuild()
CapecRelatedWeakness.model_rebuild()
CapecMemberOf.model_rebuild()
CapecHasMember.model_rebuild()
CapecRelationships.model_rebuild()
CapecStakeholder.model_rebuild()
CapecAttackPattern.model_rebuild()
CapecCategory.model_rebuild()
CapecView.model_rebuild()
CapecAttackPatternCatalog.model_rebuild()
