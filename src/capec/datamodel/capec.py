# Auto generated from capec.yaml by pythongen.py version: 0.0.1
# Schema: capec
#
# id: https://w3id.org/lmodel/capec
# description: A LinkML model of the CAPEC catalogue. It keeps the keys and listed values of the catalogue's XML Schema, so the catalogue validates as MITRE spells it once scripts/capec_to_json.py has turned it into data.
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

from linkml_runtime.linkml_model.types import Date, Integer, String, Uri
from linkml_runtime.utils.metamodelcore import URI, XSDDate

metamodel_version = "1.12.0"
version = "3.9"

# Namespaces
ATTACK = CurieNamespace('attack', 'https://w3id.org/lmodel/attack/')
CAPEC = CurieNamespace('capec', 'https://w3id.org/lmodel/capec/')
DCTERMS = CurieNamespace('dcterms', 'http://purl.org/dc/terms/')
LINKML = CurieNamespace('linkml', 'https://w3id.org/linkml/')
SCHEMA = CurieNamespace('schema', 'http://schema.org/')
SEPSES_CAPEC = CurieNamespace('sepses_capec', 'http://w3id.org/sepses/vocab/ref/capec#')
SKOS = CurieNamespace('skos', 'http://www.w3.org/2004/02/skos/core#')
STIX = CurieNamespace('stix', 'https://w3id.org/lmodel/stix/')
WD = CurieNamespace('wd', 'http://www.wikidata.org/entity/')
WDT = CurieNamespace('wdt', 'http://www.wikidata.org/prop/direct/')
XSD = CurieNamespace('xsd', 'http://www.w3.org/2001/XMLSchema#')
DEFAULT_ = CAPEC


# Types
class CapecNumericId(String):
    """ The number of a CAPEC entry or a CWE weakness, written as a string of digits. """
    type_class_uri = XSD["string"]
    type_class_curie = "xsd:string"
    type_name = "capec_numeric_id"
    type_model_uri = CAPEC.CapecNumericId


class CapecReferenceId(String):
    """ The identifier of an external reference, such as REF-1. """
    type_class_uri = XSD["string"]
    type_class_curie = "xsd:string"
    type_name = "capec_reference_id"
    type_model_uri = CAPEC.CapecReferenceId


class CapecStructuredText(String):
    """ Text that may hold XHTML markup such as paragraphs and lists, with no namespace prefix. """
    type_class_uri = XSD["string"]
    type_class_curie = "xsd:string"
    type_name = "capec_structured_text"
    type_model_uri = CAPEC.CapecStructuredText


class CapecUri(Uri):
    """ A web address, as the XSD's xs:anyURI holds it. """
    type_class_uri = XSD["anyURI"]
    type_class_curie = "xsd:anyURI"
    type_name = "capec_uri"
    type_model_uri = CAPEC.CapecUri


class CapecYear(String):
    """ A year in the XSD's xs:gYear form, such as 2004. """
    type_class_uri = XSD["string"]
    type_class_curie = "xsd:string"
    type_name = "capec_year"
    type_model_uri = CAPEC.CapecYear


class CapecMonth(String):
    """ A month in the XSD's xs:gMonth form, such as --02 for February. """
    type_class_uri = XSD["string"]
    type_class_curie = "xsd:string"
    type_name = "capec_month"
    type_model_uri = CAPEC.CapecMonth


class CapecDay(String):
    """ A day of the month in the XSD's xs:gDay form, such as ---08. """
    type_class_uri = XSD["string"]
    type_class_curie = "xsd:string"
    type_name = "capec_day"
    type_model_uri = CAPEC.CapecDay


# Class references
class CapecExternalReferenceReferenceID(CapecReferenceId):
    pass


class CapecEntryID(CapecNumericId):
    pass


class CapecAttackPatternID(CapecEntryID):
    pass


class CapecCategoryID(CapecEntryID):
    pass


class CapecViewID(CapecEntryID):
    pass


@dataclass(repr=False)
class CapecAttackPatternCatalog(YAMLRoot):
    """
    One release of the whole catalogue, with its entries and the references they share.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CAPEC["CapecAttackPatternCatalog"]
    class_class_curie: ClassVar[str] = "capec:CapecAttackPatternCatalog"
    class_name: ClassVar[str] = "CapecAttackPatternCatalog"
    class_model_uri: ClassVar[URIRef] = CAPEC.CapecAttackPatternCatalog

    Name: str = None
    Version: str = None
    Date: Union[str, XSDDate] = None
    Attack_Patterns: Optional[Union[dict[Union[str, CapecAttackPatternID], Union[dict, "CapecAttackPattern"]], list[Union[dict, "CapecAttackPattern"]]]] = empty_dict()
    Categories: Optional[Union[dict[Union[str, CapecCategoryID], Union[dict, "CapecCategory"]], list[Union[dict, "CapecCategory"]]]] = empty_dict()
    Views: Optional[Union[dict[Union[str, CapecViewID], Union[dict, "CapecView"]], list[Union[dict, "CapecView"]]]] = empty_dict()
    External_References: Optional[Union[dict[Union[str, CapecExternalReferenceReferenceID], Union[dict, "CapecExternalReference"]], list[Union[dict, "CapecExternalReference"]]]] = empty_dict()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.Name):
            self.MissingRequiredField("Name")
        if not isinstance(self.Name, str):
            self.Name = str(self.Name)

        if self._is_empty(self.Version):
            self.MissingRequiredField("Version")
        if not isinstance(self.Version, str):
            self.Version = str(self.Version)

        if self._is_empty(self.Date):
            self.MissingRequiredField("Date")
        if not isinstance(self.Date, XSDDate):
            self.Date = XSDDate(self.Date)

        self._normalize_inlined_as_list(slot_name="Attack_Patterns", slot_type=CapecAttackPattern, key_name="ID", keyed=True)

        self._normalize_inlined_as_list(slot_name="Categories", slot_type=CapecCategory, key_name="ID", keyed=True)

        self._normalize_inlined_as_list(slot_name="Views", slot_type=CapecView, key_name="ID", keyed=True)

        self._normalize_inlined_as_list(slot_name="External_References", slot_type=CapecExternalReference, key_name="Reference_ID", keyed=True)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class CapecExternalReference(YAMLRoot):
    """
    A publication or page outside CAPEC that entries point to for more detail.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CAPEC["CapecExternalReference"]
    class_class_curie: ClassVar[str] = "capec:CapecExternalReference"
    class_name: ClassVar[str] = "CapecExternalReference"
    class_model_uri: ClassVar[URIRef] = CAPEC.CapecExternalReference

    Reference_ID: Union[str, CapecExternalReferenceReferenceID] = None
    Title: str = None
    Author: Optional[Union[str, list[str]]] = empty_list()
    Edition: Optional[str] = None
    Publication: Optional[str] = None
    Publication_Year: Optional[Union[str, CapecYear]] = None
    Publication_Month: Optional[Union[str, CapecMonth]] = None
    Publication_Day: Optional[Union[str, CapecDay]] = None
    Publisher: Optional[str] = None
    URL: Optional[Union[str, CapecUri]] = None
    URL_Date: Optional[Union[str, XSDDate]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.Reference_ID):
            self.MissingRequiredField("Reference_ID")
        if not isinstance(self.Reference_ID, CapecExternalReferenceReferenceID):
            self.Reference_ID = CapecExternalReferenceReferenceID(self.Reference_ID)

        if self._is_empty(self.Title):
            self.MissingRequiredField("Title")
        if not isinstance(self.Title, str):
            self.Title = str(self.Title)

        if not isinstance(self.Author, list):
            self.Author = [self.Author] if self.Author is not None else []
        self.Author = [v if isinstance(v, str) else str(v) for v in self.Author]

        if self.Edition is not None and not isinstance(self.Edition, str):
            self.Edition = str(self.Edition)

        if self.Publication is not None and not isinstance(self.Publication, str):
            self.Publication = str(self.Publication)

        if self.Publication_Year is not None and not isinstance(self.Publication_Year, CapecYear):
            self.Publication_Year = CapecYear(self.Publication_Year)

        if self.Publication_Month is not None and not isinstance(self.Publication_Month, CapecMonth):
            self.Publication_Month = CapecMonth(self.Publication_Month)

        if self.Publication_Day is not None and not isinstance(self.Publication_Day, CapecDay):
            self.Publication_Day = CapecDay(self.Publication_Day)

        if self.Publisher is not None and not isinstance(self.Publisher, str):
            self.Publisher = str(self.Publisher)

        if self.URL is not None and not isinstance(self.URL, CapecUri):
            self.URL = CapecUri(self.URL)

        if self.URL_Date is not None and not isinstance(self.URL_Date, XSDDate):
            self.URL_Date = XSDDate(self.URL_Date)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class CapecReference(YAMLRoot):
    """
    One citation by an entry of an external reference.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CAPEC["CapecReference"]
    class_class_curie: ClassVar[str] = "capec:CapecReference"
    class_name: ClassVar[str] = "CapecReference"
    class_model_uri: ClassVar[URIRef] = CAPEC.CapecReference

    External_Reference_ID: Union[str, CapecExternalReferenceReferenceID] = None
    Section: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.External_Reference_ID):
            self.MissingRequiredField("External_Reference_ID")
        if not isinstance(self.External_Reference_ID, CapecExternalReferenceReferenceID):
            self.External_Reference_ID = CapecExternalReferenceReferenceID(self.External_Reference_ID)

        if self.Section is not None and not isinstance(self.Section, str):
            self.Section = str(self.Section)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class CapecNote(YAMLRoot):
    """
    A remark on an entry that no other field can hold.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CAPEC["CapecNote"]
    class_class_curie: ClassVar[str] = "capec:CapecNote"
    class_name: ClassVar[str] = "CapecNote"
    class_model_uri: ClassVar[URIRef] = CAPEC.CapecNote

    Type: Union[str, "CapecNoteType"] = None
    Value: Union[str, CapecStructuredText] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.Type):
            self.MissingRequiredField("Type")
        if not isinstance(self.Type, CapecNoteType):
            self.Type = CapecNoteType(self.Type)

        if self._is_empty(self.Value):
            self.MissingRequiredField("Value")
        if not isinstance(self.Value, CapecStructuredText):
            self.Value = CapecStructuredText(self.Value)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class CapecTaxonomyMapping(YAMLRoot):
    """
    A link from an entry to the matching entry of another taxonomy.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CAPEC["CapecTaxonomyMapping"]
    class_class_curie: ClassVar[str] = "capec:CapecTaxonomyMapping"
    class_name: ClassVar[str] = "CapecTaxonomyMapping"
    class_model_uri: ClassVar[URIRef] = CAPEC.CapecTaxonomyMapping

    Taxonomy_Name: Union[str, "CapecTaxonomyName"] = None
    Entry_ID: Optional[str] = None
    Entry_Name: Optional[str] = None
    Mapping_Fit: Optional[Union[str, "CapecTaxonomyMappingFit"]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.Taxonomy_Name):
            self.MissingRequiredField("Taxonomy_Name")
        if not isinstance(self.Taxonomy_Name, CapecTaxonomyName):
            self.Taxonomy_Name = CapecTaxonomyName(self.Taxonomy_Name)

        if self.Entry_ID is not None and not isinstance(self.Entry_ID, str):
            self.Entry_ID = str(self.Entry_ID)

        if self.Entry_Name is not None and not isinstance(self.Entry_Name, str):
            self.Entry_Name = str(self.Entry_Name)

        if self.Mapping_Fit is not None and not isinstance(self.Mapping_Fit, CapecTaxonomyMappingFit):
            self.Mapping_Fit = CapecTaxonomyMappingFit(self.Mapping_Fit)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class CapecExcludeRelated(YAMLRoot):
    """
    An ancestor under which a relation does not hold.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CAPEC["CapecExcludeRelated"]
    class_class_curie: ClassVar[str] = "capec:CapecExcludeRelated"
    class_name: ClassVar[str] = "CapecExcludeRelated"
    class_model_uri: ClassVar[URIRef] = CAPEC.CapecExcludeRelated

    Exclude_ID: Union[str, CapecEntryID] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.Exclude_ID):
            self.MissingRequiredField("Exclude_ID")
        if not isinstance(self.Exclude_ID, CapecEntryID):
            self.Exclude_ID = CapecEntryID(self.Exclude_ID)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class CapecExclusionsMixin(YAMLRoot):
    """
    The field of any relation that can leave out some ancestors.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CAPEC["CapecExclusionsMixin"]
    class_class_curie: ClassVar[str] = "capec:CapecExclusionsMixin"
    class_name: ClassVar[str] = "CapecExclusionsMixin"
    class_model_uri: ClassVar[URIRef] = CAPEC.CapecExclusionsMixin

    Exclude_Related: Optional[Union[Union[dict, CapecExcludeRelated], list[Union[dict, CapecExcludeRelated]]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if not isinstance(self.Exclude_Related, list):
            self.Exclude_Related = [self.Exclude_Related] if self.Exclude_Related is not None else []
        self.Exclude_Related = [v if isinstance(v, CapecExcludeRelated) else CapecExcludeRelated(**as_dict(v)) for v in self.Exclude_Related]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class CapecTaxonomyMappedMixin(YAMLRoot):
    """
    The field of an entry that can map to other taxonomies.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CAPEC["CapecTaxonomyMappedMixin"]
    class_class_curie: ClassVar[str] = "capec:CapecTaxonomyMappedMixin"
    class_name: ClassVar[str] = "CapecTaxonomyMappedMixin"
    class_model_uri: ClassVar[URIRef] = CAPEC.CapecTaxonomyMappedMixin

    Taxonomy_Mappings: Optional[Union[Union[dict, CapecTaxonomyMapping], list[Union[dict, CapecTaxonomyMapping]]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        self._normalize_inlined_as_list(slot_name="Taxonomy_Mappings", slot_type=CapecTaxonomyMapping, key_name="Taxonomy_Name", keyed=False)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class CapecSubmission(YAMLRoot):
    """
    Who first put an entry forward, and when.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CAPEC["CapecSubmission"]
    class_class_curie: ClassVar[str] = "capec:CapecSubmission"
    class_name: ClassVar[str] = "CapecSubmission"
    class_model_uri: ClassVar[URIRef] = CAPEC.CapecSubmission

    Submission_Name: Optional[str] = None
    Submission_Organization: Optional[str] = None
    Submission_Date: Optional[Union[str, XSDDate]] = None
    Submission_Comment: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.Submission_Name is not None and not isinstance(self.Submission_Name, str):
            self.Submission_Name = str(self.Submission_Name)

        if self.Submission_Organization is not None and not isinstance(self.Submission_Organization, str):
            self.Submission_Organization = str(self.Submission_Organization)

        if self.Submission_Date is not None and not isinstance(self.Submission_Date, XSDDate):
            self.Submission_Date = XSDDate(self.Submission_Date)

        if self.Submission_Comment is not None and not isinstance(self.Submission_Comment, str):
            self.Submission_Comment = str(self.Submission_Comment)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class CapecModification(YAMLRoot):
    """
    One later edit to an entry.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CAPEC["CapecModification"]
    class_class_curie: ClassVar[str] = "capec:CapecModification"
    class_name: ClassVar[str] = "CapecModification"
    class_model_uri: ClassVar[URIRef] = CAPEC.CapecModification

    Modification_Name: Optional[str] = None
    Modification_Organization: Optional[str] = None
    Modification_Date: Optional[Union[str, XSDDate]] = None
    Modification_Importance: Optional[Union[str, "CapecImportance"]] = None
    Modification_Comment: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.Modification_Name is not None and not isinstance(self.Modification_Name, str):
            self.Modification_Name = str(self.Modification_Name)

        if self.Modification_Organization is not None and not isinstance(self.Modification_Organization, str):
            self.Modification_Organization = str(self.Modification_Organization)

        if self.Modification_Date is not None and not isinstance(self.Modification_Date, XSDDate):
            self.Modification_Date = XSDDate(self.Modification_Date)

        if self.Modification_Importance is not None and not isinstance(self.Modification_Importance, CapecImportance):
            self.Modification_Importance = CapecImportance(self.Modification_Importance)

        if self.Modification_Comment is not None and not isinstance(self.Modification_Comment, str):
            self.Modification_Comment = str(self.Modification_Comment)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class CapecContribution(YAMLRoot):
    """
    Help given to an entry by someone other than its submitter.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CAPEC["CapecContribution"]
    class_class_curie: ClassVar[str] = "capec:CapecContribution"
    class_name: ClassVar[str] = "CapecContribution"
    class_model_uri: ClassVar[URIRef] = CAPEC.CapecContribution

    Type: Union[str, "CapecContributionType"] = None
    Contribution_Name: Optional[str] = None
    Contribution_Organization: Optional[str] = None
    Contribution_Date: Optional[Union[str, XSDDate]] = None
    Contribution_Comment: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.Type):
            self.MissingRequiredField("Type")
        if not isinstance(self.Type, CapecContributionType):
            self.Type = CapecContributionType(self.Type)

        if self.Contribution_Name is not None and not isinstance(self.Contribution_Name, str):
            self.Contribution_Name = str(self.Contribution_Name)

        if self.Contribution_Organization is not None and not isinstance(self.Contribution_Organization, str):
            self.Contribution_Organization = str(self.Contribution_Organization)

        if self.Contribution_Date is not None and not isinstance(self.Contribution_Date, XSDDate):
            self.Contribution_Date = XSDDate(self.Contribution_Date)

        if self.Contribution_Comment is not None and not isinstance(self.Contribution_Comment, str):
            self.Contribution_Comment = str(self.Contribution_Comment)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class CapecPreviousEntryName(YAMLRoot):
    """
    A name an entry used to carry.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CAPEC["CapecPreviousEntryName"]
    class_class_curie: ClassVar[str] = "capec:CapecPreviousEntryName"
    class_name: ClassVar[str] = "CapecPreviousEntryName"
    class_model_uri: ClassVar[URIRef] = CAPEC.CapecPreviousEntryName

    Date: Union[str, XSDDate] = None
    Value: str = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.Date):
            self.MissingRequiredField("Date")
        if not isinstance(self.Date, XSDDate):
            self.Date = XSDDate(self.Date)

        if self._is_empty(self.Value):
            self.MissingRequiredField("Value")
        if not isinstance(self.Value, str):
            self.Value = str(self.Value)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class CapecContentHistory(YAMLRoot):
    """
    The record of who wrote and changed an entry.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CAPEC["CapecContentHistory"]
    class_class_curie: ClassVar[str] = "capec:CapecContentHistory"
    class_name: ClassVar[str] = "CapecContentHistory"
    class_model_uri: ClassVar[URIRef] = CAPEC.CapecContentHistory

    Submission: Optional[Union[dict, CapecSubmission]] = None
    Modification: Optional[Union[Union[dict, CapecModification], list[Union[dict, CapecModification]]]] = empty_list()
    Contribution: Optional[Union[Union[dict, CapecContribution], list[Union[dict, CapecContribution]]]] = empty_list()
    Previous_Entry_Name: Optional[Union[Union[dict, CapecPreviousEntryName], list[Union[dict, CapecPreviousEntryName]]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.Submission is not None and not isinstance(self.Submission, CapecSubmission):
            self.Submission = CapecSubmission(**as_dict(self.Submission))

        if not isinstance(self.Modification, list):
            self.Modification = [self.Modification] if self.Modification is not None else []
        self.Modification = [v if isinstance(v, CapecModification) else CapecModification(**as_dict(v)) for v in self.Modification]

        self._normalize_inlined_as_list(slot_name="Contribution", slot_type=CapecContribution, key_name="Type", keyed=False)

        self._normalize_inlined_as_list(slot_name="Previous_Entry_Name", slot_type=CapecPreviousEntryName, key_name="Date", keyed=False)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class CapecEntry(YAMLRoot):
    """
    Anything in the catalogue with a CAPEC number, whether an attack pattern, a category or a view.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CAPEC["CapecEntry"]
    class_class_curie: ClassVar[str] = "capec:CapecEntry"
    class_name: ClassVar[str] = "CapecEntry"
    class_model_uri: ClassVar[URIRef] = CAPEC.CapecEntry

    ID: Union[str, CapecEntryID] = None
    Name: str = None
    Status: Union[str, "CapecStatus"] = None
    References: Optional[Union[Union[dict, CapecReference], list[Union[dict, CapecReference]]]] = empty_list()
    Notes: Optional[Union[Union[dict, CapecNote], list[Union[dict, CapecNote]]]] = empty_list()
    Content_History: Optional[Union[dict, CapecContentHistory]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.ID):
            self.MissingRequiredField("ID")
        if not isinstance(self.ID, CapecEntryID):
            self.ID = CapecEntryID(self.ID)

        if self._is_empty(self.Name):
            self.MissingRequiredField("Name")
        if not isinstance(self.Name, str):
            self.Name = str(self.Name)

        if self._is_empty(self.Status):
            self.MissingRequiredField("Status")
        if not isinstance(self.Status, CapecStatus):
            self.Status = CapecStatus(self.Status)

        if not isinstance(self.References, list):
            self.References = [self.References] if self.References is not None else []
        self.References = [v if isinstance(v, CapecReference) else CapecReference(**as_dict(v)) for v in self.References]

        self._normalize_inlined_as_list(slot_name="Notes", slot_type=CapecNote, key_name="Type", keyed=False)

        if self.Content_History is not None and not isinstance(self.Content_History, CapecContentHistory):
            self.Content_History = CapecContentHistory(**as_dict(self.Content_History))

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class CapecAlternateTerm(YAMLRoot):
    """
    Another name by which an attack pattern is known.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CAPEC["CapecAlternateTerm"]
    class_class_curie: ClassVar[str] = "capec:CapecAlternateTerm"
    class_name: ClassVar[str] = "CapecAlternateTerm"
    class_model_uri: ClassVar[URIRef] = CAPEC.CapecAlternateTerm

    Term: str = None
    Description: Optional[Union[str, CapecStructuredText]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.Term):
            self.MissingRequiredField("Term")
        if not isinstance(self.Term, str):
            self.Term = str(self.Term)

        if self.Description is not None and not isinstance(self.Description, CapecStructuredText):
            self.Description = CapecStructuredText(self.Description)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class CapecRelatedAttackPattern(YAMLRoot):
    """
    A relation from one attack pattern to another.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CAPEC["CapecRelatedAttackPattern"]
    class_class_curie: ClassVar[str] = "capec:CapecRelatedAttackPattern"
    class_name: ClassVar[str] = "CapecRelatedAttackPattern"
    class_model_uri: ClassVar[URIRef] = CAPEC.CapecRelatedAttackPattern

    Nature: Union[str, "CapecRelatedNature"] = None
    CAPEC_ID: Union[str, CapecAttackPatternID] = None
    Exclude_Related: Optional[Union[Union[dict, CapecExcludeRelated], list[Union[dict, CapecExcludeRelated]]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.Nature):
            self.MissingRequiredField("Nature")
        if not isinstance(self.Nature, CapecRelatedNature):
            self.Nature = CapecRelatedNature(self.Nature)

        if self._is_empty(self.CAPEC_ID):
            self.MissingRequiredField("CAPEC_ID")
        if not isinstance(self.CAPEC_ID, CapecAttackPatternID):
            self.CAPEC_ID = CapecAttackPatternID(self.CAPEC_ID)

        if not isinstance(self.Exclude_Related, list):
            self.Exclude_Related = [self.Exclude_Related] if self.Exclude_Related is not None else []
        self.Exclude_Related = [v if isinstance(v, CapecExcludeRelated) else CapecExcludeRelated(**as_dict(v)) for v in self.Exclude_Related]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class CapecTechnique(YAMLRoot):
    """
    One way of carrying out a step of an attack.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CAPEC["CapecTechnique"]
    class_class_curie: ClassVar[str] = "capec:CapecTechnique"
    class_name: ClassVar[str] = "CapecTechnique"
    class_model_uri: ClassVar[URIRef] = CAPEC.CapecTechnique

    Value: Union[str, CapecStructuredText] = None
    CAPEC_ID: Optional[Union[str, CapecEntryID]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.Value):
            self.MissingRequiredField("Value")
        if not isinstance(self.Value, CapecStructuredText):
            self.Value = CapecStructuredText(self.Value)

        if self.CAPEC_ID is not None and not isinstance(self.CAPEC_ID, CapecEntryID):
            self.CAPEC_ID = CapecEntryID(self.CAPEC_ID)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class CapecAttackStep(YAMLRoot):
    """
    One step of the way an adversary typically carries out an attack.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CAPEC["CapecAttackStep"]
    class_class_curie: ClassVar[str] = "capec:CapecAttackStep"
    class_name: ClassVar[str] = "CapecAttackStep"
    class_model_uri: ClassVar[URIRef] = CAPEC.CapecAttackStep

    Step: int = None
    Phase: Union[str, "CapecAttackStepPhase"] = None
    Description: Union[str, CapecStructuredText] = None
    Technique: Optional[Union[Union[dict, CapecTechnique], list[Union[dict, CapecTechnique]]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.Step):
            self.MissingRequiredField("Step")
        if not isinstance(self.Step, int):
            self.Step = int(self.Step)

        if self._is_empty(self.Phase):
            self.MissingRequiredField("Phase")
        if not isinstance(self.Phase, CapecAttackStepPhase):
            self.Phase = CapecAttackStepPhase(self.Phase)

        if self._is_empty(self.Description):
            self.MissingRequiredField("Description")
        if not isinstance(self.Description, CapecStructuredText):
            self.Description = CapecStructuredText(self.Description)

        self._normalize_inlined_as_list(slot_name="Technique", slot_type=CapecTechnique, key_name="Value", keyed=False)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class CapecSkill(YAMLRoot):
    """
    A skill or piece of knowledge an adversary needs.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CAPEC["CapecSkill"]
    class_class_curie: ClassVar[str] = "capec:CapecSkill"
    class_name: ClassVar[str] = "CapecSkill"
    class_model_uri: ClassVar[URIRef] = CAPEC.CapecSkill

    Level: Union[str, "CapecSkillLevel"] = None
    Value: str = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.Level):
            self.MissingRequiredField("Level")
        if not isinstance(self.Level, CapecSkillLevel):
            self.Level = CapecSkillLevel(self.Level)

        if self._is_empty(self.Value):
            self.MissingRequiredField("Value")
        if not isinstance(self.Value, str):
            self.Value = str(self.Value)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class CapecConsequence(YAMLRoot):
    """
    One thing that can happen if an attack succeeds.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CAPEC["CapecConsequence"]
    class_class_curie: ClassVar[str] = "capec:CapecConsequence"
    class_name: ClassVar[str] = "CapecConsequence"
    class_model_uri: ClassVar[URIRef] = CAPEC.CapecConsequence

    Scope: Union[Union[str, "CapecScope"], list[Union[str, "CapecScope"]]] = None
    Consequence_ID: Optional[str] = None
    Impact: Optional[Union[Union[str, "CapecTechnicalImpact"], list[Union[str, "CapecTechnicalImpact"]]]] = empty_list()
    Likelihood: Optional[Union[str, "CapecLikelihood"]] = None
    Note: Optional[Union[str, CapecStructuredText]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.Scope):
            self.MissingRequiredField("Scope")
        if not isinstance(self.Scope, list):
            self.Scope = [self.Scope] if self.Scope is not None else []
        self.Scope = [v if isinstance(v, CapecScope) else CapecScope(v) for v in self.Scope]

        if self.Consequence_ID is not None and not isinstance(self.Consequence_ID, str):
            self.Consequence_ID = str(self.Consequence_ID)

        if not isinstance(self.Impact, list):
            self.Impact = [self.Impact] if self.Impact is not None else []
        self.Impact = [v if isinstance(v, CapecTechnicalImpact) else CapecTechnicalImpact(v) for v in self.Impact]

        if self.Likelihood is not None and not isinstance(self.Likelihood, CapecLikelihood):
            self.Likelihood = CapecLikelihood(self.Likelihood)

        if self.Note is not None and not isinstance(self.Note, CapecStructuredText):
            self.Note = CapecStructuredText(self.Note)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class CapecRelatedWeakness(YAMLRoot):
    """
    A weakness in the Common Weakness Enumeration that can make an attack possible.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CAPEC["CapecRelatedWeakness"]
    class_class_curie: ClassVar[str] = "capec:CapecRelatedWeakness"
    class_name: ClassVar[str] = "CapecRelatedWeakness"
    class_model_uri: ClassVar[URIRef] = CAPEC.CapecRelatedWeakness

    CWE_ID: Union[str, CapecNumericId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.CWE_ID):
            self.MissingRequiredField("CWE_ID")
        if not isinstance(self.CWE_ID, CapecNumericId):
            self.CWE_ID = CapecNumericId(self.CWE_ID)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class CapecMemberOf(YAMLRoot):
    """
    A statement that an entry belongs to a view or a category.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CAPEC["CapecMemberOf"]
    class_class_curie: ClassVar[str] = "capec:CapecMemberOf"
    class_name: ClassVar[str] = "CapecMemberOf"
    class_model_uri: ClassVar[URIRef] = CAPEC.CapecMemberOf

    CAPEC_ID: Union[str, CapecEntryID] = None
    Exclude_Related: Optional[Union[Union[dict, CapecExcludeRelated], list[Union[dict, CapecExcludeRelated]]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.CAPEC_ID):
            self.MissingRequiredField("CAPEC_ID")
        if not isinstance(self.CAPEC_ID, CapecEntryID):
            self.CAPEC_ID = CapecEntryID(self.CAPEC_ID)

        if not isinstance(self.Exclude_Related, list):
            self.Exclude_Related = [self.Exclude_Related] if self.Exclude_Related is not None else []
        self.Exclude_Related = [v if isinstance(v, CapecExcludeRelated) else CapecExcludeRelated(**as_dict(v)) for v in self.Exclude_Related]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class CapecHasMember(YAMLRoot):
    """
    A statement that a view or a category holds an entry.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CAPEC["CapecHasMember"]
    class_class_curie: ClassVar[str] = "capec:CapecHasMember"
    class_name: ClassVar[str] = "CapecHasMember"
    class_model_uri: ClassVar[URIRef] = CAPEC.CapecHasMember

    CAPEC_ID: Union[str, CapecEntryID] = None
    Exclude_Related: Optional[Union[Union[dict, CapecExcludeRelated], list[Union[dict, CapecExcludeRelated]]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.CAPEC_ID):
            self.MissingRequiredField("CAPEC_ID")
        if not isinstance(self.CAPEC_ID, CapecEntryID):
            self.CAPEC_ID = CapecEntryID(self.CAPEC_ID)

        if not isinstance(self.Exclude_Related, list):
            self.Exclude_Related = [self.Exclude_Related] if self.Exclude_Related is not None else []
        self.Exclude_Related = [v if isinstance(v, CapecExcludeRelated) else CapecExcludeRelated(**as_dict(v)) for v in self.Exclude_Related]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class CapecRelationships(YAMLRoot):
    """
    Which entries a category or a view holds, and which it belongs to.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CAPEC["CapecRelationships"]
    class_class_curie: ClassVar[str] = "capec:CapecRelationships"
    class_name: ClassVar[str] = "CapecRelationships"
    class_model_uri: ClassVar[URIRef] = CAPEC.CapecRelationships

    Member_Of: Optional[Union[Union[dict, CapecMemberOf], list[Union[dict, CapecMemberOf]]]] = empty_list()
    Has_Member: Optional[Union[Union[dict, CapecHasMember], list[Union[dict, CapecHasMember]]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if not isinstance(self.Member_Of, list):
            self.Member_Of = [self.Member_Of] if self.Member_Of is not None else []
        self.Member_Of = [v if isinstance(v, CapecMemberOf) else CapecMemberOf(**as_dict(v)) for v in self.Member_Of]

        if not isinstance(self.Has_Member, list):
            self.Has_Member = [self.Has_Member] if self.Has_Member is not None else []
        self.Has_Member = [v if isinstance(v, CapecHasMember) else CapecHasMember(**as_dict(v)) for v in self.Has_Member]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class CapecStakeholder(YAMLRoot):
    """
    One kind of person a view is meant for, and what they would get from it.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CAPEC["CapecStakeholder"]
    class_class_curie: ClassVar[str] = "capec:CapecStakeholder"
    class_name: ClassVar[str] = "CapecStakeholder"
    class_model_uri: ClassVar[URIRef] = CAPEC.CapecStakeholder

    Type: Union[str, "CapecStakeholderType"] = None
    Description: Union[str, CapecStructuredText] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.Type):
            self.MissingRequiredField("Type")
        if not isinstance(self.Type, CapecStakeholderType):
            self.Type = CapecStakeholderType(self.Type)

        if self._is_empty(self.Description):
            self.MissingRequiredField("Description")
        if not isinstance(self.Description, CapecStructuredText):
            self.Description = CapecStructuredText(self.Description)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class CapecAttackPattern(CapecEntry):
    """
    A catalogued way that adversaries go about an attack, with what it takes and how to resist it.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CAPEC["CapecAttackPattern"]
    class_class_curie: ClassVar[str] = "capec:CapecAttackPattern"
    class_name: ClassVar[str] = "CapecAttackPattern"
    class_model_uri: ClassVar[URIRef] = CAPEC.CapecAttackPattern

    ID: Union[str, CapecAttackPatternID] = None
    Name: str = None
    Status: Union[str, "CapecStatus"] = None
    Abstraction: Union[str, "CapecAbstraction"] = None
    Description: Union[str, CapecStructuredText] = None
    Extended_Description: Optional[Union[str, CapecStructuredText]] = None
    Alternate_Terms: Optional[Union[Union[dict, CapecAlternateTerm], list[Union[dict, CapecAlternateTerm]]]] = empty_list()
    Likelihood_Of_Attack: Optional[Union[str, "CapecLikelihood"]] = None
    Typical_Severity: Optional[Union[str, "CapecSeverity"]] = None
    Related_Attack_Patterns: Optional[Union[Union[dict, CapecRelatedAttackPattern], list[Union[dict, CapecRelatedAttackPattern]]]] = empty_list()
    Execution_Flow: Optional[Union[Union[dict, CapecAttackStep], list[Union[dict, CapecAttackStep]]]] = empty_list()
    Prerequisites: Optional[Union[Union[str, CapecStructuredText], list[Union[str, CapecStructuredText]]]] = empty_list()
    Skills_Required: Optional[Union[Union[dict, CapecSkill], list[Union[dict, CapecSkill]]]] = empty_list()
    Resources_Required: Optional[Union[Union[str, CapecStructuredText], list[Union[str, CapecStructuredText]]]] = empty_list()
    Indicators: Optional[Union[Union[str, CapecStructuredText], list[Union[str, CapecStructuredText]]]] = empty_list()
    Consequences: Optional[Union[Union[dict, CapecConsequence], list[Union[dict, CapecConsequence]]]] = empty_list()
    Mitigations: Optional[Union[Union[str, CapecStructuredText], list[Union[str, CapecStructuredText]]]] = empty_list()
    Example_Instances: Optional[Union[Union[str, CapecStructuredText], list[Union[str, CapecStructuredText]]]] = empty_list()
    Related_Weaknesses: Optional[Union[Union[dict, CapecRelatedWeakness], list[Union[dict, CapecRelatedWeakness]]]] = empty_list()
    Taxonomy_Mappings: Optional[Union[Union[dict, CapecTaxonomyMapping], list[Union[dict, CapecTaxonomyMapping]]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.ID):
            self.MissingRequiredField("ID")
        if not isinstance(self.ID, CapecAttackPatternID):
            self.ID = CapecAttackPatternID(self.ID)

        if self._is_empty(self.Abstraction):
            self.MissingRequiredField("Abstraction")
        if not isinstance(self.Abstraction, CapecAbstraction):
            self.Abstraction = CapecAbstraction(self.Abstraction)

        if self._is_empty(self.Description):
            self.MissingRequiredField("Description")
        if not isinstance(self.Description, CapecStructuredText):
            self.Description = CapecStructuredText(self.Description)

        if self.Extended_Description is not None and not isinstance(self.Extended_Description, CapecStructuredText):
            self.Extended_Description = CapecStructuredText(self.Extended_Description)

        self._normalize_inlined_as_list(slot_name="Alternate_Terms", slot_type=CapecAlternateTerm, key_name="Term", keyed=False)

        if self.Likelihood_Of_Attack is not None and not isinstance(self.Likelihood_Of_Attack, CapecLikelihood):
            self.Likelihood_Of_Attack = CapecLikelihood(self.Likelihood_Of_Attack)

        if self.Typical_Severity is not None and not isinstance(self.Typical_Severity, CapecSeverity):
            self.Typical_Severity = CapecSeverity(self.Typical_Severity)

        self._normalize_inlined_as_list(slot_name="Related_Attack_Patterns", slot_type=CapecRelatedAttackPattern, key_name="Nature", keyed=False)

        self._normalize_inlined_as_list(slot_name="Execution_Flow", slot_type=CapecAttackStep, key_name="Step", keyed=False)

        if not isinstance(self.Prerequisites, list):
            self.Prerequisites = [self.Prerequisites] if self.Prerequisites is not None else []
        self.Prerequisites = [v if isinstance(v, CapecStructuredText) else CapecStructuredText(v) for v in self.Prerequisites]

        self._normalize_inlined_as_list(slot_name="Skills_Required", slot_type=CapecSkill, key_name="Level", keyed=False)

        if not isinstance(self.Resources_Required, list):
            self.Resources_Required = [self.Resources_Required] if self.Resources_Required is not None else []
        self.Resources_Required = [v if isinstance(v, CapecStructuredText) else CapecStructuredText(v) for v in self.Resources_Required]

        if not isinstance(self.Indicators, list):
            self.Indicators = [self.Indicators] if self.Indicators is not None else []
        self.Indicators = [v if isinstance(v, CapecStructuredText) else CapecStructuredText(v) for v in self.Indicators]

        self._normalize_inlined_as_list(slot_name="Consequences", slot_type=CapecConsequence, key_name="Scope", keyed=False)

        if not isinstance(self.Mitigations, list):
            self.Mitigations = [self.Mitigations] if self.Mitigations is not None else []
        self.Mitigations = [v if isinstance(v, CapecStructuredText) else CapecStructuredText(v) for v in self.Mitigations]

        if not isinstance(self.Example_Instances, list):
            self.Example_Instances = [self.Example_Instances] if self.Example_Instances is not None else []
        self.Example_Instances = [v if isinstance(v, CapecStructuredText) else CapecStructuredText(v) for v in self.Example_Instances]

        self._normalize_inlined_as_list(slot_name="Related_Weaknesses", slot_type=CapecRelatedWeakness, key_name="CWE_ID", keyed=False)

        self._normalize_inlined_as_list(slot_name="Taxonomy_Mappings", slot_type=CapecTaxonomyMapping, key_name="Taxonomy_Name", keyed=False)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class CapecCategory(CapecEntry):
    """
    A group of attack patterns that share an effect or intent, and not itself a pattern of attack.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CAPEC["CapecCategory"]
    class_class_curie: ClassVar[str] = "capec:CapecCategory"
    class_name: ClassVar[str] = "CapecCategory"
    class_model_uri: ClassVar[URIRef] = CAPEC.CapecCategory

    ID: Union[str, CapecCategoryID] = None
    Name: str = None
    Status: Union[str, "CapecStatus"] = None
    Summary: Union[str, CapecStructuredText] = None
    Relationships: Optional[Union[dict, CapecRelationships]] = None
    Taxonomy_Mappings: Optional[Union[Union[dict, CapecTaxonomyMapping], list[Union[dict, CapecTaxonomyMapping]]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.ID):
            self.MissingRequiredField("ID")
        if not isinstance(self.ID, CapecCategoryID):
            self.ID = CapecCategoryID(self.ID)

        if self._is_empty(self.Summary):
            self.MissingRequiredField("Summary")
        if not isinstance(self.Summary, CapecStructuredText):
            self.Summary = CapecStructuredText(self.Summary)

        if self.Relationships is not None and not isinstance(self.Relationships, CapecRelationships):
            self.Relationships = CapecRelationships(**as_dict(self.Relationships))

        self._normalize_inlined_as_list(slot_name="Taxonomy_Mappings", slot_type=CapecTaxonomyMapping, key_name="Taxonomy_Name", keyed=False)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class CapecView(CapecEntry):
    """
    One way of looking over the catalogue, by a hierarchy or by a slice of its entries.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CAPEC["CapecView"]
    class_class_curie: ClassVar[str] = "capec:CapecView"
    class_name: ClassVar[str] = "CapecView"
    class_model_uri: ClassVar[URIRef] = CAPEC.CapecView

    ID: Union[str, CapecViewID] = None
    Name: str = None
    Status: Union[str, "CapecStatus"] = None
    Type: Union[str, "CapecViewType"] = None
    Objective: Union[str, CapecStructuredText] = None
    Audience: Optional[Union[Union[dict, CapecStakeholder], list[Union[dict, CapecStakeholder]]]] = empty_list()
    Members: Optional[Union[dict, CapecRelationships]] = None
    Filter: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.ID):
            self.MissingRequiredField("ID")
        if not isinstance(self.ID, CapecViewID):
            self.ID = CapecViewID(self.ID)

        if self._is_empty(self.Type):
            self.MissingRequiredField("Type")
        if not isinstance(self.Type, CapecViewType):
            self.Type = CapecViewType(self.Type)

        if self._is_empty(self.Objective):
            self.MissingRequiredField("Objective")
        if not isinstance(self.Objective, CapecStructuredText):
            self.Objective = CapecStructuredText(self.Objective)

        self._normalize_inlined_as_list(slot_name="Audience", slot_type=CapecStakeholder, key_name="Type", keyed=False)

        if self.Members is not None and not isinstance(self.Members, CapecRelationships):
            self.Members = CapecRelationships(**as_dict(self.Members))

        if self.Filter is not None and not isinstance(self.Filter, str):
            self.Filter = str(self.Filter)

        super().__post_init__(**kwargs)


# Enumerations
class CapecImportance(EnumDefinitionImpl):
    """
    How much a change to an entry matters to anyone relying on it.
    """
    Normal = PermissibleValue(
        text="Normal",
        description="A change that leaves the entry's meaning as it was.")
    Critical = PermissibleValue(
        text="Critical",
        description="A change to the entry's meaning or to how it may be read.")

    _defn = EnumDefinition(
        name="CapecImportance",
        description="How much a change to an entry matters to anyone relying on it.",
    )

class CapecNoteType(EnumDefinitionImpl):
    """
    What kind of remark a note makes.
    """
    Maintenance = PermissibleValue(
        text="Maintenance",
        description="Work on the entry still to be done.")
    Relationship = PermissibleValue(
        text="Relationship",
        description="Detail on how entries relate.")
    Terminology = PermissibleValue(
        text="Terminology",
        description="A question of wording, such as competing uses of one term.")
    Other = PermissibleValue(
        text="Other",
        description="A remark of no listed kind.")

    _defn = EnumDefinition(
        name="CapecNoteType",
        description="What kind of remark a note makes.",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "Research Gap",
            PermissibleValue(
                text="Research Gap",
                description="Something the research community could look into further."))

class CapecStatus(EnumDefinitionImpl):
    """
    How far an entry has got through CAPEC's review.
    """
    Deprecated = PermissibleValue(
        text="Deprecated",
        description="Withdrawn from the catalogue, though its number stays taken.")
    Draft = PermissibleValue(
        text="Draft",
        description="Filled in but still open to change.")
    Incomplete = PermissibleValue(
        text="Incomplete",
        description="Still lacking required content.")
    Obsolete = PermissibleValue(
        text="Obsolete",
        description="Still correct but no longer current.")
    Stable = PermissibleValue(
        text="Stable",
        description="Reviewed, and not expected to change much.")
    Usable = PermissibleValue(
        text="Usable",
        description="Reviewed closely enough to rely on.")

    _defn = EnumDefinition(
        name="CapecStatus",
        description="How far an entry has got through CAPEC's review.",
    )

class CapecTaxonomyMappingFit(EnumDefinitionImpl):
    """
    How well an entry fits the entry of another taxonomy that it maps to.
    """
    Exact = PermissibleValue(
        text="Exact",
        description="The two mean the same.")
    Imprecise = PermissibleValue(
        text="Imprecise",
        description="The two overlap without one holding the other.")
    Perspective = PermissibleValue(
        text="Perspective",
        description="The two look at one subject from different standpoints.")

    _defn = EnumDefinition(
        name="CapecTaxonomyMappingFit",
        description="How well an entry fits the entry of another taxonomy that it maps to.",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "CAPEC More Abstract",
            PermissibleValue(
                text="CAPEC More Abstract",
                description="The CAPEC entry is the wider of the two."))
        setattr(cls, "CAPEC More Specific",
            PermissibleValue(
                text="CAPEC More Specific",
                description="The CAPEC entry is the narrower of the two."))

class CapecTaxonomyName(EnumDefinitionImpl):
    """
    The other taxonomies that CAPEC maps to.
    """
    ATTACK = PermissibleValue(
        text="ATTACK",
        description="MITRE ATT&CK. An entry's Entry_ID there is the technique's number without its T.")
    WASC = PermissibleValue(
        text="WASC",
        description="The Web Application Security Consortium's threat classification.")

    _defn = EnumDefinition(
        name="CapecTaxonomyName",
        description="The other taxonomies that CAPEC maps to.",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "OWASP Attacks",
            PermissibleValue(
                text="OWASP Attacks",
                description="The attack list of the Open Worldwide Application Security Project."))

class CapecContributionType(EnumDefinitionImpl):
    """
    Whether a contribution changed an entry's content or only commented on it.
    """
    Content = PermissibleValue(
        text="Content",
        description="Text given to the entry.")
    Feedback = PermissibleValue(
        text="Feedback",
        description="Remarks on the entry.")

    _defn = EnumDefinition(
        name="CapecContributionType",
        description="Whether a contribution changed an entry's content or only commented on it.",
    )

class CapecAbstraction(EnumDefinitionImpl):
    """
    How concrete an attack pattern is.
    """
    Meta = PermissibleValue(
        text="Meta",
        description="A broad approach, free of any one technology, for use in design-level threat modelling.")
    Standard = PermissibleValue(
        text="Standard",
        description="One method or technique, often only a part of a whole attack.")
    Detailed = PermissibleValue(
        text="Detailed",
        description="One technique against one technology, usually with its steps set out.")

    _defn = EnumDefinition(
        name="CapecAbstraction",
        description="How concrete an attack pattern is.",
    )

class CapecLikelihood(EnumDefinitionImpl):
    """
    How likely something is to happen.
    """
    High = PermissibleValue(text="High")
    Medium = PermissibleValue(text="Medium")
    Low = PermissibleValue(text="Low")
    Unknown = PermissibleValue(
        text="Unknown",
        description="Nobody knows how likely it is.")

    _defn = EnumDefinition(
        name="CapecLikelihood",
        description="How likely something is to happen.",
    )

class CapecRelatedNature(EnumDefinitionImpl):
    """
    How one attack pattern relates to another.
    """
    ChildOf = PermissibleValue(
        text="ChildOf",
        description="The other pattern is more abstract, and this one specialises it.")
    ParentOf = PermissibleValue(
        text="ParentOf",
        description="The other pattern is less abstract, and it specialises this one.")
    CanFollow = PermissibleValue(
        text="CanFollow",
        description="In a chain of attack, this pattern may come after the other.")
    CanPrecede = PermissibleValue(
        text="CanPrecede",
        description="In a chain of attack, this pattern may come before the other.")
    CanAlsoBe = PermissibleValue(
        text="CanAlsoBe",
        description="""In some settings this pattern can also be read as the other one, though not always the reverse.""")
    PeerOf = PermissibleValue(
        text="PeerOf",
        description="The two are alike in a way that no other nature covers.")

    _defn = EnumDefinition(
        name="CapecRelatedNature",
        description="How one attack pattern relates to another.",
    )

class CapecScope(EnumDefinitionImpl):
    """
    The security property that a consequence violates.
    """
    Confidentiality = PermissibleValue(text="Confidentiality")
    Integrity = PermissibleValue(text="Integrity")
    Availability = PermissibleValue(text="Availability")
    Accountability = PermissibleValue(text="Accountability")
    Authentication = PermissibleValue(text="Authentication")
    Authorization = PermissibleValue(text="Authorization")
    Other = PermissibleValue(text="Other")

    _defn = EnumDefinition(
        name="CapecScope",
        description="The security property that a consequence violates.",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "Access Control",
            PermissibleValue(text="Access Control"))
        setattr(cls, "Non-Repudiation",
            PermissibleValue(text="Non-Repudiation"))

class CapecSeverity(EnumDefinitionImpl):
    """
    How bad the typical outcome of an attack is.
    """
    High = PermissibleValue(text="High")
    Medium = PermissibleValue(text="Medium")
    Low = PermissibleValue(text="Low")

    _defn = EnumDefinition(
        name="CapecSeverity",
        description="How bad the typical outcome of an attack is.",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "Very High",
            PermissibleValue(text="Very High"))
        setattr(cls, "Very Low",
            PermissibleValue(text="Very Low"))

class CapecSkillLevel(EnumDefinitionImpl):
    """
    How much skill or knowledge an adversary needs.
    """
    High = PermissibleValue(text="High")
    Medium = PermissibleValue(text="Medium")
    Low = PermissibleValue(text="Low")
    Unknown = PermissibleValue(
        text="Unknown",
        description="Nobody knows how much is needed.")

    _defn = EnumDefinition(
        name="CapecSkillLevel",
        description="How much skill or knowledge an adversary needs.",
    )

class CapecStakeholderType(EnumDefinitionImpl):
    """
    The kinds of people a view is meant for.
    """
    Educators = PermissibleValue(text="Educators")
    Other = PermissibleValue(text="Other")

    _defn = EnumDefinition(
        name="CapecStakeholderType",
        description="The kinds of people a view is meant for.",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "Academic Researchers",
            PermissibleValue(text="Academic Researchers"))
        setattr(cls, "Applied Researchers",
            PermissibleValue(text="Applied Researchers"))
        setattr(cls, "Assessment Customers",
            PermissibleValue(text="Assessment Customers"))
        setattr(cls, "Assessment Vendors",
            PermissibleValue(text="Assessment Vendors"))
        setattr(cls, "CAPEC Team",
            PermissibleValue(text="CAPEC Team"))
        setattr(cls, "Information Providers",
            PermissibleValue(text="Information Providers"))
        setattr(cls, "Software Customers",
            PermissibleValue(text="Software Customers"))
        setattr(cls, "Software Designers",
            PermissibleValue(text="Software Designers"))
        setattr(cls, "Software Developers",
            PermissibleValue(text="Software Developers"))
        setattr(cls, "Software Vendors",
            PermissibleValue(text="Software Vendors"))

class CapecTechnicalImpact(EnumDefinitionImpl):
    """
    What a successful attack does to the system, in technical terms.
    """
    Other = PermissibleValue(text="Other")

    _defn = EnumDefinition(
        name="CapecTechnicalImpact",
        description="What a successful attack does to the system, in technical terms.",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "Modify Data",
            PermissibleValue(text="Modify Data"))
        setattr(cls, "Read Data",
            PermissibleValue(text="Read Data"))
        setattr(cls, "Unreliable Execution",
            PermissibleValue(text="Unreliable Execution"))
        setattr(cls, "Resource Consumption",
            PermissibleValue(text="Resource Consumption"))
        setattr(cls, "Execute Unauthorized Commands",
            PermissibleValue(text="Execute Unauthorized Commands"))
        setattr(cls, "Gain Privileges",
            PermissibleValue(text="Gain Privileges"))
        setattr(cls, "Bypass Protection Mechanism",
            PermissibleValue(text="Bypass Protection Mechanism"))
        setattr(cls, "Hide Activities",
            PermissibleValue(text="Hide Activities"))
        setattr(cls, "Alter Execution Logic",
            PermissibleValue(text="Alter Execution Logic"))

class CapecViewType(EnumDefinitionImpl):
    """
    How a view selects its entries.
    """
    Implicit = PermissibleValue(
        text="Implicit",
        description="A slice picked by a filter on an attribute, such as every pattern of one status.")
    Explicit = PermissibleValue(
        text="Explicit",
        description="A slice picked by hand because of something outside the catalogue, such as a list.")
    Graph = PermissibleValue(
        text="Graph",
        description="A hierarchy seen from one standpoint, often from category down to detailed pattern.")

    _defn = EnumDefinition(
        name="CapecViewType",
        description="How a view selects its entries.",
    )

class CapecAttackStepPhase(EnumDefinitionImpl):
    """
    Which stage of an attack a step belongs to.
    """
    Explore = PermissibleValue(
        text="Explore",
        description="Looking over the target.")
    Experiment = PermissibleValue(
        text="Experiment",
        description="Trying things out against it.")
    Exploit = PermissibleValue(
        text="Exploit",
        description="Carrying the attack through.")

    _defn = EnumDefinition(
        name="CapecAttackStepPhase",
        description="Which stage of an attack a step belongs to.",
    )

# Slots
class slots:
    pass

slots.capecAttackPatternCatalog__Name = Slot(uri=CAPEC.Name, name="capecAttackPatternCatalog__Name", curie=CAPEC.curie('Name'),
                   model_uri=CAPEC.capecAttackPatternCatalog__Name, domain=None, range=str)

slots.capecAttackPatternCatalog__Version = Slot(uri=CAPEC.Version, name="capecAttackPatternCatalog__Version", curie=CAPEC.curie('Version'),
                   model_uri=CAPEC.capecAttackPatternCatalog__Version, domain=None, range=str)

slots.capecAttackPatternCatalog__Date = Slot(uri=CAPEC.Date, name="capecAttackPatternCatalog__Date", curie=CAPEC.curie('Date'),
                   model_uri=CAPEC.capecAttackPatternCatalog__Date, domain=None, range=Union[str, XSDDate])

slots.capecAttackPatternCatalog__Attack_Patterns = Slot(uri=CAPEC.Attack_Patterns, name="capecAttackPatternCatalog__Attack_Patterns", curie=CAPEC.curie('Attack_Patterns'),
                   model_uri=CAPEC.capecAttackPatternCatalog__Attack_Patterns, domain=None, range=Optional[Union[dict[Union[str, CapecAttackPatternID], Union[dict, CapecAttackPattern]], list[Union[dict, CapecAttackPattern]]]])

slots.capecAttackPatternCatalog__Categories = Slot(uri=CAPEC.Categories, name="capecAttackPatternCatalog__Categories", curie=CAPEC.curie('Categories'),
                   model_uri=CAPEC.capecAttackPatternCatalog__Categories, domain=None, range=Optional[Union[dict[Union[str, CapecCategoryID], Union[dict, CapecCategory]], list[Union[dict, CapecCategory]]]])

slots.capecAttackPatternCatalog__Views = Slot(uri=CAPEC.Views, name="capecAttackPatternCatalog__Views", curie=CAPEC.curie('Views'),
                   model_uri=CAPEC.capecAttackPatternCatalog__Views, domain=None, range=Optional[Union[dict[Union[str, CapecViewID], Union[dict, CapecView]], list[Union[dict, CapecView]]]])

slots.capecAttackPatternCatalog__External_References = Slot(uri=CAPEC.External_References, name="capecAttackPatternCatalog__External_References", curie=CAPEC.curie('External_References'),
                   model_uri=CAPEC.capecAttackPatternCatalog__External_References, domain=None, range=Optional[Union[dict[Union[str, CapecExternalReferenceReferenceID], Union[dict, CapecExternalReference]], list[Union[dict, CapecExternalReference]]]])

slots.capecExternalReference__Reference_ID = Slot(uri=CAPEC.Reference_ID, name="capecExternalReference__Reference_ID", curie=CAPEC.curie('Reference_ID'),
                   model_uri=CAPEC.capecExternalReference__Reference_ID, domain=None, range=URIRef)

slots.capecExternalReference__Author = Slot(uri=CAPEC.Author, name="capecExternalReference__Author", curie=CAPEC.curie('Author'),
                   model_uri=CAPEC.capecExternalReference__Author, domain=None, range=Optional[Union[str, list[str]]])

slots.capecExternalReference__Title = Slot(uri=CAPEC.Title, name="capecExternalReference__Title", curie=CAPEC.curie('Title'),
                   model_uri=CAPEC.capecExternalReference__Title, domain=None, range=str)

slots.capecExternalReference__Edition = Slot(uri=CAPEC.Edition, name="capecExternalReference__Edition", curie=CAPEC.curie('Edition'),
                   model_uri=CAPEC.capecExternalReference__Edition, domain=None, range=Optional[str])

slots.capecExternalReference__Publication = Slot(uri=CAPEC.Publication, name="capecExternalReference__Publication", curie=CAPEC.curie('Publication'),
                   model_uri=CAPEC.capecExternalReference__Publication, domain=None, range=Optional[str])

slots.capecExternalReference__Publication_Year = Slot(uri=CAPEC.Publication_Year, name="capecExternalReference__Publication_Year", curie=CAPEC.curie('Publication_Year'),
                   model_uri=CAPEC.capecExternalReference__Publication_Year, domain=None, range=Optional[Union[str, CapecYear]])

slots.capecExternalReference__Publication_Month = Slot(uri=CAPEC.Publication_Month, name="capecExternalReference__Publication_Month", curie=CAPEC.curie('Publication_Month'),
                   model_uri=CAPEC.capecExternalReference__Publication_Month, domain=None, range=Optional[Union[str, CapecMonth]])

slots.capecExternalReference__Publication_Day = Slot(uri=CAPEC.Publication_Day, name="capecExternalReference__Publication_Day", curie=CAPEC.curie('Publication_Day'),
                   model_uri=CAPEC.capecExternalReference__Publication_Day, domain=None, range=Optional[Union[str, CapecDay]])

slots.capecExternalReference__Publisher = Slot(uri=CAPEC.Publisher, name="capecExternalReference__Publisher", curie=CAPEC.curie('Publisher'),
                   model_uri=CAPEC.capecExternalReference__Publisher, domain=None, range=Optional[str])

slots.capecExternalReference__URL = Slot(uri=CAPEC.URL, name="capecExternalReference__URL", curie=CAPEC.curie('URL'),
                   model_uri=CAPEC.capecExternalReference__URL, domain=None, range=Optional[Union[str, CapecUri]])

slots.capecExternalReference__URL_Date = Slot(uri=CAPEC.URL_Date, name="capecExternalReference__URL_Date", curie=CAPEC.curie('URL_Date'),
                   model_uri=CAPEC.capecExternalReference__URL_Date, domain=None, range=Optional[Union[str, XSDDate]])

slots.capecReference__External_Reference_ID = Slot(uri=CAPEC.External_Reference_ID, name="capecReference__External_Reference_ID", curie=CAPEC.curie('External_Reference_ID'),
                   model_uri=CAPEC.capecReference__External_Reference_ID, domain=None, range=Union[str, CapecExternalReferenceReferenceID],
                   pattern=re.compile(r'^REF-[0-9]+$'))

slots.capecReference__Section = Slot(uri=CAPEC.Section, name="capecReference__Section", curie=CAPEC.curie('Section'),
                   model_uri=CAPEC.capecReference__Section, domain=None, range=Optional[str])

slots.capecNote__Type = Slot(uri=CAPEC.Type, name="capecNote__Type", curie=CAPEC.curie('Type'),
                   model_uri=CAPEC.capecNote__Type, domain=None, range=Union[str, "CapecNoteType"])

slots.capecNote__Value = Slot(uri=CAPEC.Value, name="capecNote__Value", curie=CAPEC.curie('Value'),
                   model_uri=CAPEC.capecNote__Value, domain=None, range=Union[str, CapecStructuredText])

slots.capecTaxonomyMapping__Taxonomy_Name = Slot(uri=CAPEC.Taxonomy_Name, name="capecTaxonomyMapping__Taxonomy_Name", curie=CAPEC.curie('Taxonomy_Name'),
                   model_uri=CAPEC.capecTaxonomyMapping__Taxonomy_Name, domain=None, range=Union[str, "CapecTaxonomyName"])

slots.capecTaxonomyMapping__Entry_ID = Slot(uri=CAPEC.Entry_ID, name="capecTaxonomyMapping__Entry_ID", curie=CAPEC.curie('Entry_ID'),
                   model_uri=CAPEC.capecTaxonomyMapping__Entry_ID, domain=None, range=Optional[str])

slots.capecTaxonomyMapping__Entry_Name = Slot(uri=CAPEC.Entry_Name, name="capecTaxonomyMapping__Entry_Name", curie=CAPEC.curie('Entry_Name'),
                   model_uri=CAPEC.capecTaxonomyMapping__Entry_Name, domain=None, range=Optional[str])

slots.capecTaxonomyMapping__Mapping_Fit = Slot(uri=CAPEC.Mapping_Fit, name="capecTaxonomyMapping__Mapping_Fit", curie=CAPEC.curie('Mapping_Fit'),
                   model_uri=CAPEC.capecTaxonomyMapping__Mapping_Fit, domain=None, range=Optional[Union[str, "CapecTaxonomyMappingFit"]])

slots.capecExcludeRelated__Exclude_ID = Slot(uri=CAPEC.Exclude_ID, name="capecExcludeRelated__Exclude_ID", curie=CAPEC.curie('Exclude_ID'),
                   model_uri=CAPEC.capecExcludeRelated__Exclude_ID, domain=None, range=Union[str, CapecEntryID],
                   pattern=re.compile(r'^[1-9][0-9]*$'))

slots.capecExclusionsMixin__Exclude_Related = Slot(uri=CAPEC.Exclude_Related, name="capecExclusionsMixin__Exclude_Related", curie=CAPEC.curie('Exclude_Related'),
                   model_uri=CAPEC.capecExclusionsMixin__Exclude_Related, domain=None, range=Optional[Union[Union[dict, CapecExcludeRelated], list[Union[dict, CapecExcludeRelated]]]])

slots.capecTaxonomyMappedMixin__Taxonomy_Mappings = Slot(uri=CAPEC.Taxonomy_Mappings, name="capecTaxonomyMappedMixin__Taxonomy_Mappings", curie=CAPEC.curie('Taxonomy_Mappings'),
                   model_uri=CAPEC.capecTaxonomyMappedMixin__Taxonomy_Mappings, domain=None, range=Optional[Union[Union[dict, CapecTaxonomyMapping], list[Union[dict, CapecTaxonomyMapping]]]])

slots.capecSubmission__Submission_Name = Slot(uri=CAPEC.Submission_Name, name="capecSubmission__Submission_Name", curie=CAPEC.curie('Submission_Name'),
                   model_uri=CAPEC.capecSubmission__Submission_Name, domain=None, range=Optional[str])

slots.capecSubmission__Submission_Organization = Slot(uri=CAPEC.Submission_Organization, name="capecSubmission__Submission_Organization", curie=CAPEC.curie('Submission_Organization'),
                   model_uri=CAPEC.capecSubmission__Submission_Organization, domain=None, range=Optional[str])

slots.capecSubmission__Submission_Date = Slot(uri=CAPEC.Submission_Date, name="capecSubmission__Submission_Date", curie=CAPEC.curie('Submission_Date'),
                   model_uri=CAPEC.capecSubmission__Submission_Date, domain=None, range=Optional[Union[str, XSDDate]])

slots.capecSubmission__Submission_Comment = Slot(uri=CAPEC.Submission_Comment, name="capecSubmission__Submission_Comment", curie=CAPEC.curie('Submission_Comment'),
                   model_uri=CAPEC.capecSubmission__Submission_Comment, domain=None, range=Optional[str])

slots.capecModification__Modification_Name = Slot(uri=CAPEC.Modification_Name, name="capecModification__Modification_Name", curie=CAPEC.curie('Modification_Name'),
                   model_uri=CAPEC.capecModification__Modification_Name, domain=None, range=Optional[str])

slots.capecModification__Modification_Organization = Slot(uri=CAPEC.Modification_Organization, name="capecModification__Modification_Organization", curie=CAPEC.curie('Modification_Organization'),
                   model_uri=CAPEC.capecModification__Modification_Organization, domain=None, range=Optional[str])

slots.capecModification__Modification_Date = Slot(uri=CAPEC.Modification_Date, name="capecModification__Modification_Date", curie=CAPEC.curie('Modification_Date'),
                   model_uri=CAPEC.capecModification__Modification_Date, domain=None, range=Optional[Union[str, XSDDate]])

slots.capecModification__Modification_Importance = Slot(uri=CAPEC.Modification_Importance, name="capecModification__Modification_Importance", curie=CAPEC.curie('Modification_Importance'),
                   model_uri=CAPEC.capecModification__Modification_Importance, domain=None, range=Optional[Union[str, "CapecImportance"]])

slots.capecModification__Modification_Comment = Slot(uri=CAPEC.Modification_Comment, name="capecModification__Modification_Comment", curie=CAPEC.curie('Modification_Comment'),
                   model_uri=CAPEC.capecModification__Modification_Comment, domain=None, range=Optional[str])

slots.capecContribution__Type = Slot(uri=CAPEC.Type, name="capecContribution__Type", curie=CAPEC.curie('Type'),
                   model_uri=CAPEC.capecContribution__Type, domain=None, range=Union[str, "CapecContributionType"])

slots.capecContribution__Contribution_Name = Slot(uri=CAPEC.Contribution_Name, name="capecContribution__Contribution_Name", curie=CAPEC.curie('Contribution_Name'),
                   model_uri=CAPEC.capecContribution__Contribution_Name, domain=None, range=Optional[str])

slots.capecContribution__Contribution_Organization = Slot(uri=CAPEC.Contribution_Organization, name="capecContribution__Contribution_Organization", curie=CAPEC.curie('Contribution_Organization'),
                   model_uri=CAPEC.capecContribution__Contribution_Organization, domain=None, range=Optional[str])

slots.capecContribution__Contribution_Date = Slot(uri=CAPEC.Contribution_Date, name="capecContribution__Contribution_Date", curie=CAPEC.curie('Contribution_Date'),
                   model_uri=CAPEC.capecContribution__Contribution_Date, domain=None, range=Optional[Union[str, XSDDate]])

slots.capecContribution__Contribution_Comment = Slot(uri=CAPEC.Contribution_Comment, name="capecContribution__Contribution_Comment", curie=CAPEC.curie('Contribution_Comment'),
                   model_uri=CAPEC.capecContribution__Contribution_Comment, domain=None, range=Optional[str])

slots.capecPreviousEntryName__Date = Slot(uri=CAPEC.Date, name="capecPreviousEntryName__Date", curie=CAPEC.curie('Date'),
                   model_uri=CAPEC.capecPreviousEntryName__Date, domain=None, range=Union[str, XSDDate])

slots.capecPreviousEntryName__Value = Slot(uri=CAPEC.Value, name="capecPreviousEntryName__Value", curie=CAPEC.curie('Value'),
                   model_uri=CAPEC.capecPreviousEntryName__Value, domain=None, range=str)

slots.capecContentHistory__Submission = Slot(uri=CAPEC.Submission, name="capecContentHistory__Submission", curie=CAPEC.curie('Submission'),
                   model_uri=CAPEC.capecContentHistory__Submission, domain=None, range=Optional[Union[dict, CapecSubmission]])

slots.capecContentHistory__Modification = Slot(uri=CAPEC.Modification, name="capecContentHistory__Modification", curie=CAPEC.curie('Modification'),
                   model_uri=CAPEC.capecContentHistory__Modification, domain=None, range=Optional[Union[Union[dict, CapecModification], list[Union[dict, CapecModification]]]])

slots.capecContentHistory__Contribution = Slot(uri=CAPEC.Contribution, name="capecContentHistory__Contribution", curie=CAPEC.curie('Contribution'),
                   model_uri=CAPEC.capecContentHistory__Contribution, domain=None, range=Optional[Union[Union[dict, CapecContribution], list[Union[dict, CapecContribution]]]])

slots.capecContentHistory__Previous_Entry_Name = Slot(uri=CAPEC.Previous_Entry_Name, name="capecContentHistory__Previous_Entry_Name", curie=CAPEC.curie('Previous_Entry_Name'),
                   model_uri=CAPEC.capecContentHistory__Previous_Entry_Name, domain=None, range=Optional[Union[Union[dict, CapecPreviousEntryName], list[Union[dict, CapecPreviousEntryName]]]])

slots.capecEntry__ID = Slot(uri=CAPEC.ID, name="capecEntry__ID", curie=CAPEC.curie('ID'),
                   model_uri=CAPEC.capecEntry__ID, domain=None, range=URIRef)

slots.capecEntry__Name = Slot(uri=CAPEC.Name, name="capecEntry__Name", curie=CAPEC.curie('Name'),
                   model_uri=CAPEC.capecEntry__Name, domain=None, range=str)

slots.capecEntry__Status = Slot(uri=CAPEC.Status, name="capecEntry__Status", curie=CAPEC.curie('Status'),
                   model_uri=CAPEC.capecEntry__Status, domain=None, range=Union[str, "CapecStatus"])

slots.capecEntry__References = Slot(uri=CAPEC.References, name="capecEntry__References", curie=CAPEC.curie('References'),
                   model_uri=CAPEC.capecEntry__References, domain=None, range=Optional[Union[Union[dict, CapecReference], list[Union[dict, CapecReference]]]])

slots.capecEntry__Notes = Slot(uri=CAPEC.Notes, name="capecEntry__Notes", curie=CAPEC.curie('Notes'),
                   model_uri=CAPEC.capecEntry__Notes, domain=None, range=Optional[Union[Union[dict, CapecNote], list[Union[dict, CapecNote]]]])

slots.capecEntry__Content_History = Slot(uri=CAPEC.Content_History, name="capecEntry__Content_History", curie=CAPEC.curie('Content_History'),
                   model_uri=CAPEC.capecEntry__Content_History, domain=None, range=Optional[Union[dict, CapecContentHistory]])

slots.capecAlternateTerm__Term = Slot(uri=CAPEC.Term, name="capecAlternateTerm__Term", curie=CAPEC.curie('Term'),
                   model_uri=CAPEC.capecAlternateTerm__Term, domain=None, range=str)

slots.capecAlternateTerm__Description = Slot(uri=CAPEC.Description, name="capecAlternateTerm__Description", curie=CAPEC.curie('Description'),
                   model_uri=CAPEC.capecAlternateTerm__Description, domain=None, range=Optional[Union[str, CapecStructuredText]])

slots.capecRelatedAttackPattern__Nature = Slot(uri=CAPEC.Nature, name="capecRelatedAttackPattern__Nature", curie=CAPEC.curie('Nature'),
                   model_uri=CAPEC.capecRelatedAttackPattern__Nature, domain=None, range=Union[str, "CapecRelatedNature"])

slots.capecRelatedAttackPattern__CAPEC_ID = Slot(uri=CAPEC.CAPEC_ID, name="capecRelatedAttackPattern__CAPEC_ID", curie=CAPEC.curie('CAPEC_ID'),
                   model_uri=CAPEC.capecRelatedAttackPattern__CAPEC_ID, domain=None, range=Union[str, CapecAttackPatternID],
                   pattern=re.compile(r'^[1-9][0-9]*$'))

slots.capecTechnique__CAPEC_ID = Slot(uri=CAPEC.CAPEC_ID, name="capecTechnique__CAPEC_ID", curie=CAPEC.curie('CAPEC_ID'),
                   model_uri=CAPEC.capecTechnique__CAPEC_ID, domain=None, range=Optional[Union[str, CapecEntryID]])

slots.capecTechnique__Value = Slot(uri=CAPEC.Value, name="capecTechnique__Value", curie=CAPEC.curie('Value'),
                   model_uri=CAPEC.capecTechnique__Value, domain=None, range=Union[str, CapecStructuredText])

slots.capecAttackStep__Step = Slot(uri=CAPEC.Step, name="capecAttackStep__Step", curie=CAPEC.curie('Step'),
                   model_uri=CAPEC.capecAttackStep__Step, domain=None, range=int)

slots.capecAttackStep__Phase = Slot(uri=CAPEC.Phase, name="capecAttackStep__Phase", curie=CAPEC.curie('Phase'),
                   model_uri=CAPEC.capecAttackStep__Phase, domain=None, range=Union[str, "CapecAttackStepPhase"])

slots.capecAttackStep__Description = Slot(uri=CAPEC.Description, name="capecAttackStep__Description", curie=CAPEC.curie('Description'),
                   model_uri=CAPEC.capecAttackStep__Description, domain=None, range=Union[str, CapecStructuredText])

slots.capecAttackStep__Technique = Slot(uri=CAPEC.Technique, name="capecAttackStep__Technique", curie=CAPEC.curie('Technique'),
                   model_uri=CAPEC.capecAttackStep__Technique, domain=None, range=Optional[Union[Union[dict, CapecTechnique], list[Union[dict, CapecTechnique]]]])

slots.capecSkill__Level = Slot(uri=CAPEC.Level, name="capecSkill__Level", curie=CAPEC.curie('Level'),
                   model_uri=CAPEC.capecSkill__Level, domain=None, range=Union[str, "CapecSkillLevel"])

slots.capecSkill__Value = Slot(uri=CAPEC.Value, name="capecSkill__Value", curie=CAPEC.curie('Value'),
                   model_uri=CAPEC.capecSkill__Value, domain=None, range=str)

slots.capecConsequence__Consequence_ID = Slot(uri=CAPEC.Consequence_ID, name="capecConsequence__Consequence_ID", curie=CAPEC.curie('Consequence_ID'),
                   model_uri=CAPEC.capecConsequence__Consequence_ID, domain=None, range=Optional[str])

slots.capecConsequence__Scope = Slot(uri=CAPEC.Scope, name="capecConsequence__Scope", curie=CAPEC.curie('Scope'),
                   model_uri=CAPEC.capecConsequence__Scope, domain=None, range=Union[Union[str, "CapecScope"], list[Union[str, "CapecScope"]]])

slots.capecConsequence__Impact = Slot(uri=CAPEC.Impact, name="capecConsequence__Impact", curie=CAPEC.curie('Impact'),
                   model_uri=CAPEC.capecConsequence__Impact, domain=None, range=Optional[Union[Union[str, "CapecTechnicalImpact"], list[Union[str, "CapecTechnicalImpact"]]]])

slots.capecConsequence__Likelihood = Slot(uri=CAPEC.Likelihood, name="capecConsequence__Likelihood", curie=CAPEC.curie('Likelihood'),
                   model_uri=CAPEC.capecConsequence__Likelihood, domain=None, range=Optional[Union[str, "CapecLikelihood"]])

slots.capecConsequence__Note = Slot(uri=CAPEC.Note, name="capecConsequence__Note", curie=CAPEC.curie('Note'),
                   model_uri=CAPEC.capecConsequence__Note, domain=None, range=Optional[Union[str, CapecStructuredText]])

slots.capecRelatedWeakness__CWE_ID = Slot(uri=CAPEC.CWE_ID, name="capecRelatedWeakness__CWE_ID", curie=CAPEC.curie('CWE_ID'),
                   model_uri=CAPEC.capecRelatedWeakness__CWE_ID, domain=None, range=Union[str, CapecNumericId])

slots.capecMemberOf__CAPEC_ID = Slot(uri=CAPEC.CAPEC_ID, name="capecMemberOf__CAPEC_ID", curie=CAPEC.curie('CAPEC_ID'),
                   model_uri=CAPEC.capecMemberOf__CAPEC_ID, domain=None, range=Union[str, CapecEntryID],
                   pattern=re.compile(r'^[1-9][0-9]*$'))

slots.capecHasMember__CAPEC_ID = Slot(uri=CAPEC.CAPEC_ID, name="capecHasMember__CAPEC_ID", curie=CAPEC.curie('CAPEC_ID'),
                   model_uri=CAPEC.capecHasMember__CAPEC_ID, domain=None, range=Union[str, CapecEntryID],
                   pattern=re.compile(r'^[1-9][0-9]*$'))

slots.capecRelationships__Member_Of = Slot(uri=CAPEC.Member_Of, name="capecRelationships__Member_Of", curie=CAPEC.curie('Member_Of'),
                   model_uri=CAPEC.capecRelationships__Member_Of, domain=None, range=Optional[Union[Union[dict, CapecMemberOf], list[Union[dict, CapecMemberOf]]]])

slots.capecRelationships__Has_Member = Slot(uri=CAPEC.Has_Member, name="capecRelationships__Has_Member", curie=CAPEC.curie('Has_Member'),
                   model_uri=CAPEC.capecRelationships__Has_Member, domain=None, range=Optional[Union[Union[dict, CapecHasMember], list[Union[dict, CapecHasMember]]]])

slots.capecStakeholder__Type = Slot(uri=CAPEC.Type, name="capecStakeholder__Type", curie=CAPEC.curie('Type'),
                   model_uri=CAPEC.capecStakeholder__Type, domain=None, range=Union[str, "CapecStakeholderType"])

slots.capecStakeholder__Description = Slot(uri=CAPEC.Description, name="capecStakeholder__Description", curie=CAPEC.curie('Description'),
                   model_uri=CAPEC.capecStakeholder__Description, domain=None, range=Union[str, CapecStructuredText])

slots.capecAttackPattern__Abstraction = Slot(uri=CAPEC.Abstraction, name="capecAttackPattern__Abstraction", curie=CAPEC.curie('Abstraction'),
                   model_uri=CAPEC.capecAttackPattern__Abstraction, domain=None, range=Union[str, "CapecAbstraction"])

slots.capecAttackPattern__Description = Slot(uri=CAPEC.Description, name="capecAttackPattern__Description", curie=CAPEC.curie('Description'),
                   model_uri=CAPEC.capecAttackPattern__Description, domain=None, range=Union[str, CapecStructuredText])

slots.capecAttackPattern__Extended_Description = Slot(uri=CAPEC.Extended_Description, name="capecAttackPattern__Extended_Description", curie=CAPEC.curie('Extended_Description'),
                   model_uri=CAPEC.capecAttackPattern__Extended_Description, domain=None, range=Optional[Union[str, CapecStructuredText]])

slots.capecAttackPattern__Alternate_Terms = Slot(uri=CAPEC.Alternate_Terms, name="capecAttackPattern__Alternate_Terms", curie=CAPEC.curie('Alternate_Terms'),
                   model_uri=CAPEC.capecAttackPattern__Alternate_Terms, domain=None, range=Optional[Union[Union[dict, CapecAlternateTerm], list[Union[dict, CapecAlternateTerm]]]])

slots.capecAttackPattern__Likelihood_Of_Attack = Slot(uri=CAPEC.Likelihood_Of_Attack, name="capecAttackPattern__Likelihood_Of_Attack", curie=CAPEC.curie('Likelihood_Of_Attack'),
                   model_uri=CAPEC.capecAttackPattern__Likelihood_Of_Attack, domain=None, range=Optional[Union[str, "CapecLikelihood"]])

slots.capecAttackPattern__Typical_Severity = Slot(uri=CAPEC.Typical_Severity, name="capecAttackPattern__Typical_Severity", curie=CAPEC.curie('Typical_Severity'),
                   model_uri=CAPEC.capecAttackPattern__Typical_Severity, domain=None, range=Optional[Union[str, "CapecSeverity"]])

slots.capecAttackPattern__Related_Attack_Patterns = Slot(uri=CAPEC.Related_Attack_Patterns, name="capecAttackPattern__Related_Attack_Patterns", curie=CAPEC.curie('Related_Attack_Patterns'),
                   model_uri=CAPEC.capecAttackPattern__Related_Attack_Patterns, domain=None, range=Optional[Union[Union[dict, CapecRelatedAttackPattern], list[Union[dict, CapecRelatedAttackPattern]]]])

slots.capecAttackPattern__Execution_Flow = Slot(uri=CAPEC.Execution_Flow, name="capecAttackPattern__Execution_Flow", curie=CAPEC.curie('Execution_Flow'),
                   model_uri=CAPEC.capecAttackPattern__Execution_Flow, domain=None, range=Optional[Union[Union[dict, CapecAttackStep], list[Union[dict, CapecAttackStep]]]])

slots.capecAttackPattern__Prerequisites = Slot(uri=CAPEC.Prerequisites, name="capecAttackPattern__Prerequisites", curie=CAPEC.curie('Prerequisites'),
                   model_uri=CAPEC.capecAttackPattern__Prerequisites, domain=None, range=Optional[Union[Union[str, CapecStructuredText], list[Union[str, CapecStructuredText]]]])

slots.capecAttackPattern__Skills_Required = Slot(uri=CAPEC.Skills_Required, name="capecAttackPattern__Skills_Required", curie=CAPEC.curie('Skills_Required'),
                   model_uri=CAPEC.capecAttackPattern__Skills_Required, domain=None, range=Optional[Union[Union[dict, CapecSkill], list[Union[dict, CapecSkill]]]])

slots.capecAttackPattern__Resources_Required = Slot(uri=CAPEC.Resources_Required, name="capecAttackPattern__Resources_Required", curie=CAPEC.curie('Resources_Required'),
                   model_uri=CAPEC.capecAttackPattern__Resources_Required, domain=None, range=Optional[Union[Union[str, CapecStructuredText], list[Union[str, CapecStructuredText]]]])

slots.capecAttackPattern__Indicators = Slot(uri=CAPEC.Indicators, name="capecAttackPattern__Indicators", curie=CAPEC.curie('Indicators'),
                   model_uri=CAPEC.capecAttackPattern__Indicators, domain=None, range=Optional[Union[Union[str, CapecStructuredText], list[Union[str, CapecStructuredText]]]])

slots.capecAttackPattern__Consequences = Slot(uri=CAPEC.Consequences, name="capecAttackPattern__Consequences", curie=CAPEC.curie('Consequences'),
                   model_uri=CAPEC.capecAttackPattern__Consequences, domain=None, range=Optional[Union[Union[dict, CapecConsequence], list[Union[dict, CapecConsequence]]]])

slots.capecAttackPattern__Mitigations = Slot(uri=CAPEC.Mitigations, name="capecAttackPattern__Mitigations", curie=CAPEC.curie('Mitigations'),
                   model_uri=CAPEC.capecAttackPattern__Mitigations, domain=None, range=Optional[Union[Union[str, CapecStructuredText], list[Union[str, CapecStructuredText]]]])

slots.capecAttackPattern__Example_Instances = Slot(uri=CAPEC.Example_Instances, name="capecAttackPattern__Example_Instances", curie=CAPEC.curie('Example_Instances'),
                   model_uri=CAPEC.capecAttackPattern__Example_Instances, domain=None, range=Optional[Union[Union[str, CapecStructuredText], list[Union[str, CapecStructuredText]]]])

slots.capecAttackPattern__Related_Weaknesses = Slot(uri=CAPEC.Related_Weaknesses, name="capecAttackPattern__Related_Weaknesses", curie=CAPEC.curie('Related_Weaknesses'),
                   model_uri=CAPEC.capecAttackPattern__Related_Weaknesses, domain=None, range=Optional[Union[Union[dict, CapecRelatedWeakness], list[Union[dict, CapecRelatedWeakness]]]])

slots.capecCategory__Summary = Slot(uri=CAPEC.Summary, name="capecCategory__Summary", curie=CAPEC.curie('Summary'),
                   model_uri=CAPEC.capecCategory__Summary, domain=None, range=Union[str, CapecStructuredText])

slots.capecCategory__Relationships = Slot(uri=CAPEC.Relationships, name="capecCategory__Relationships", curie=CAPEC.curie('Relationships'),
                   model_uri=CAPEC.capecCategory__Relationships, domain=None, range=Optional[Union[dict, CapecRelationships]])

slots.capecView__Type = Slot(uri=CAPEC.Type, name="capecView__Type", curie=CAPEC.curie('Type'),
                   model_uri=CAPEC.capecView__Type, domain=None, range=Union[str, "CapecViewType"])

slots.capecView__Objective = Slot(uri=CAPEC.Objective, name="capecView__Objective", curie=CAPEC.curie('Objective'),
                   model_uri=CAPEC.capecView__Objective, domain=None, range=Union[str, CapecStructuredText])

slots.capecView__Audience = Slot(uri=CAPEC.Audience, name="capecView__Audience", curie=CAPEC.curie('Audience'),
                   model_uri=CAPEC.capecView__Audience, domain=None, range=Optional[Union[Union[dict, CapecStakeholder], list[Union[dict, CapecStakeholder]]]])

slots.capecView__Members = Slot(uri=CAPEC.Members, name="capecView__Members", curie=CAPEC.curie('Members'),
                   model_uri=CAPEC.capecView__Members, domain=None, range=Optional[Union[dict, CapecRelationships]])

slots.capecView__Filter = Slot(uri=CAPEC.Filter, name="capecView__Filter", curie=CAPEC.curie('Filter'),
                   model_uri=CAPEC.capecView__Filter, domain=None, range=Optional[str])
