export type AttackPatternId = string;
export type CategoryId = string;
export type ViewId = string;
export type ExternalReferenceReferenceId = string;
/**
* The different abstraction levels that apply to an attack pattern. A Meta level
attack pattern is a decidedly abstract characterization of a specific methodology
or technique used in an attack. A Standard level attack pattern is focused on a
specific methodology or technique. A Detailed level attack pattern provides a low
level of detail, typically leveraging a specific technique and targeting a specific
technology, and expresses a complete execution flow.
*/
export enum AbstractionEnum {
    
    /** A Meta level attack pattern in CAPEC is a decidedly abstract characterization
of a specific methodology or technique used in an attack. A Meta attack pattern
is often void of a specific technology or implementation and is meant to provide
an understanding of a high level approach. A Meta level attack pattern is a
generalization of related group of standard level attack patterns. Meta level
attack patterns are particularly useful for architecture and design level threat
modeling exercises. */
    Meta = "Meta",
    /** A Standard level attack pattern in CAPEC is focused on a specific methodology
or technique used in an attack. It is often seen as a singular piece of a fully
executed attack. A Standard attack pattern is meant to provide sufficient details
to understand the specific technique and how it attempts to accomplish a desired
goal. A Standard level attack pattern is a specific type of a more abstract meta
level attack pattern. */
    Standard = "Standard",
    /** A Detailed level attack pattern in CAPEC provides a low level of detail, typically
leveraging a specific technique and targeting a specific technology, and expresses
a complete execution flow. Detailed attack patterns are more specific than meta and
standard attack patterns and often require a specific protection mechanism to mitigate
actual attacks. A Detailed level attack pattern often will leverage a number of
different standard level attack patterns chained together to accomplish a goal. */
    Detailed = "Detailed",
};
/**
* The different phases of an individual attack step within the execution flow.
*/
export enum AttackStepPhaseEnum {
    
    /** The exploration or reconnaissance phase of the attack. */
    Explore = "Explore",
    /** The experimentation or testing phase of the attack. */
    Experiment = "Experiment",
    /** The exploitation phase of the attack where intent is realized. */
    Exploit = "Exploit",
};
/**
* The type of contribution made to a CAPEC entry.
*/
export enum ContributionTypeEnum {
    
    /** The contribution consisted of actual content donated to the entry. */
    Content = "Content",
    /** The contribution consisted of general feedback about the entry. */
    Feedback = "Feedback",
};
/**
* Different values for the importance of a modification to CAPEC content.
*/
export enum ImportanceEnum {
    
    /** Normal importance modification that does not significantly alter meaning. */
    Normal = "Normal",
    /** Critical importance modification that changes the meaning of the entry, or how it might be interpreted, bringing it to the attention of anyone previously dependent on the attack pattern. */
    Critical = "Critical",
};
/**
* Values corresponding to different likelihoods. The value Unknown should be used
when the actual likelihood of something occurring is not known.
*/
export enum LikelihoodEnum {
    
    /** High likelihood. */
    High = "High",
    /** Medium likelihood. */
    Medium = "Medium",
    /** Low likelihood. */
    Low = "Low",
    /** The likelihood is unknown. */
    Unknown = "Unknown",
};
/**
* The different types of notes that can be associated with an attack pattern.
A Maintenance note contains significant maintenance tasks within this entry that
still need to be addressed, such as clarifying the concepts involved or improving
relationships. A Relationship note provides clarifying details regarding the
relationships between entities. A Research Gap note identifies potential opportunities
for the research community to conduct further exploration. A Terminology note contains
a discussion of terminology issues related to this attack pattern.
*/
export enum NoteTypeEnum {
    
    /** Contains significant maintenance tasks within this entry that still need to be
addressed, such as clarifying the concepts involved or improving relationships. */
    Maintenance = "Maintenance",
    /** Provides clarifying details regarding the relationships between entities. */
    Relationship = "Relationship",
    /** Identifies potential opportunities for the research community to conduct further
exploration of issues related to this attack pattern. */
    Research_Gap = "Research Gap",
    /** Contains a discussion of terminology issues related to this attack pattern,
or clarifications when there is no established terminology, or if there are
multiple uses of the same key term. */
    Terminology = "Terminology",
    /** Other note type not covered by the defined categories. */
    Other = "Other",
};
/**
* The different values that can be used to define the nature of a related attack
pattern. A ChildOf nature denotes a related attack pattern as a higher level of
abstraction. A ParentOf nature denotes a related attack pattern as a lower level
of abstraction. The CanPrecede and CanFollow relationships are used to denote
attack patterns that are part of a chaining structure. The CanAlsoBe relationship
denotes an attack pattern that, in the proper environment and context, can also be
perceived as the target attack pattern. Note that the CanAlsoBe relationship is not
necessarily reciprocal. The PeerOf relationship is used to show some similarity
with the target attack pattern which does not fit any of the other types.
*/
export enum RelatedNatureEnum {
    
    /** Denotes a related attack pattern at a higher level of abstraction; the current pattern is a specialization of the related pattern. */
    ChildOf = "ChildOf",
    /** Denotes a related attack pattern at a lower level of abstraction; the current pattern is a generalization of the related pattern. */
    ParentOf = "ParentOf",
    /** Denotes an attack pattern that can follow (come after) the current pattern in a chaining structure. */
    CanFollow = "CanFollow",
    /** Denotes an attack pattern that can precede (come before) the current pattern in a chaining structure. */
    CanPrecede = "CanPrecede",
    /** Denotes an attack pattern that, in the proper environment and context, can also
be perceived as the target attack pattern. Note that the CanAlsoBe relationship
is not necessarily reciprocal. */
    CanAlsoBe = "CanAlsoBe",
    /** Used to show some similarity with the target attack pattern which does not fit
any of the other types of relationships. */
    PeerOf = "PeerOf",
};
/**
* The different areas of software security that can be affected by exploiting a weakness.
*/
export enum ScopeEnum {
    
    /** The confidentiality security property is violated. */
    Confidentiality = "Confidentiality",
    /** The integrity security property is violated. */
    Integrity = "Integrity",
    /** The availability security property is violated. */
    Availability = "Availability",
    /** The access control security property is violated. */
    Access_Control = "Access Control",
    /** The accountability security property is violated. */
    Accountability = "Accountability",
    /** The authentication security property is violated. */
    Authentication = "Authentication",
    /** The authorization security property is violated. */
    Authorization = "Authorization",
    /** The non-repudiation security property is violated. */
    Non_Repudiation = "Non-Repudiation",
    /** Other security property not covered by the defined categories. */
    Other = "Other",
};
/**
* Values corresponding to different severities of attack impact.
*/
export enum SeverityEnum {
    
    /** Very high severity impact. */
    Very_High = "Very High",
    /** High severity impact. */
    High = "High",
    /** Medium severity impact. */
    Medium = "Medium",
    /** Low severity impact. */
    Low = "Low",
    /** Very low severity impact. */
    Very_Low = "Very Low",
};
/**
* Values corresponding to different knowledge levels required to perform an attack.
The value Unknown should be used when the actual skill level is not known.
*/
export enum SkillLevelEnum {
    
    /** High skill level required to perform the attack. */
    High = "High",
    /** Medium skill level required to perform the attack. */
    Medium = "Medium",
    /** Low skill level required to perform the attack. */
    Low = "Low",
    /** The skill level required to perform the attack is unknown. */
    Unknown = "Unknown",
};
/**
* The different types of users and stakeholder groups within the CAPEC community.
*/
export enum StakeholderEnum {
    
    /** Academic researchers studying attack patterns and cybersecurity. */
    Academic_Researchers = "Academic Researchers",
    /** Applied researchers using CAPEC for practical security analysis. */
    Applied_Researchers = "Applied Researchers",
    /** Customers who commission security assessments and penetration tests. */
    Assessment_Customers = "Assessment Customers",
    /** Vendors and consultants who provide security assessment services. */
    Assessment_Vendors = "Assessment Vendors",
    /** The core CAPEC development and maintenance team at MITRE. */
    CAPEC_Team = "CAPEC Team",
    /** Educators teaching courses on cybersecurity concepts using CAPEC. */
    Educators = "Educators",
    /** Organizations or individuals who provide cybersecurity information services. */
    Information_Providers = "Information Providers",
    /** End users and customers of software products concerned about security. */
    Software_Customers = "Software Customers",
    /** Software architects and designers involved in secure system design. */
    Software_Designers = "Software Designers",
    /** Software developers building and maintaining secure software. */
    Software_Developers = "Software Developers",
    /** Vendors who produce and distribute software products. */
    Software_Vendors = "Software Vendors",
    /** Other stakeholder type not covered by the defined categories. */
    Other = "Other",
};
/**
* The different status values that an entity (view, category, or attack pattern) can have.
*/
export enum StatusEnum {
    
    /** The entry has been deprecated and should not be used. A placeholder for the deprecated entry is left in the catalog and the identifier is not reused. */
    Deprecated = "Deprecated",
    /** The entry is a draft and its content may change significantly through future revisions as it is reviewed and refined by the community. */
    Draft = "Draft",
    /** The entry exists and is partially filled in, but it does not yet meet the quality bar established for Usable entries. */
    Incomplete = "Incomplete",
    /** The entry is obsolete and is no longer recommended for use but has not been formally deprecated. */
    Obsolete = "Obsolete",
    /** The entry is stable and unlikely to undergo significant changes unless new information or research warrants it. */
    Stable = "Stable",
    /** The entry is complete enough to be used in product documentation, assessments, tools, and mapping exercises without significant risk. */
    Usable = "Usable",
};
/**
* The different values used to describe how closely a mapping between CAPEC and an external taxonomy aligns.
*/
export enum TaxonomyMappingFitEnum {
    
    /** The CAPEC entry and the external taxonomy entry are an exact match in scope and meaning. */
    Exact = "Exact",
    /** The CAPEC entry is more abstract (broader) than the mapped external taxonomy entry. */
    CAPEC_More_Abstract = "CAPEC More Abstract",
    /** The CAPEC entry is more specific (narrower) than the mapped external taxonomy entry. */
    CAPEC_More_Specific = "CAPEC More Specific",
    /** The mapping between CAPEC and the external taxonomy entry is approximate or imprecise. */
    Imprecise = "Imprecise",
    /** The CAPEC entry and the external taxonomy entry represent different perspectives on the same concept. */
    Perspective = "Perspective",
};
/**
* The different known taxonomies to which CAPEC entries can be mapped.
*/
export enum TaxonomyNameEnum {
    
    /** The MITRE ATT&CK framework, a globally-accessible knowledge base of adversary tactics and techniques. */
    ATTACK = "ATTACK",
    /** The Web Application Security Consortium (WASC) Threat Classification taxonomy. */
    WASC = "WASC",
    /** The OWASP (Open Web Application Security Project) Attacks taxonomy. */
    OWASP_Attacks = "OWASP Attacks",
};
/**
* The different negative technical impacts that can result from a successful attack
leveraging a given attack pattern. A negative technical impact is the specific
technical effect of successfully violating a reasonable security policy for the
system or network.
*/
export enum TechnicalImpactEnum {
    
    /** The attacker can modify data stored within or processed by the target system. */
    Modify_Data = "Modify Data",
    /** The attacker can read sensitive or confidential data from the target system. */
    Read_Data = "Read Data",
    /** The execution of the target system becomes unreliable or unpredictable. */
    Unreliable_Execution = "Unreliable Execution",
    /** Target system resources (CPU, memory, bandwidth) are consumed by the attack. */
    Resource_Consumption = "Resource Consumption",
    /** The attacker can execute unauthorized commands or code on the target system. */
    Execute_Unauthorized_Commands = "Execute Unauthorized Commands",
    /** The attacker gains elevated or unauthorized privileges on the target system. */
    Gain_Privileges = "Gain Privileges",
    /** The attacker can bypass existing security controls or protection mechanisms. */
    Bypass_Protection_Mechanism = "Bypass Protection Mechanism",
    /** The attacker can conceal malicious activities from detection and monitoring. */
    Hide_Activities = "Hide Activities",
    /** The attacker can alter the normal execution logic or control flow of the target system. */
    Alter_Execution_Logic = "Alter Execution Logic",
    /** Other technical impact not covered by the defined categories. */
    Other = "Other",
};
/**
* The different types of views that can be found within CAPEC. A graph is a
hierarchical representation of attack patterns based on a specific vantage point.
An explicit slice is a subset of attack patterns related through some external
factor. An implicit slice is a subset of attack patterns related through a specific
attribute.
*/
export enum ViewTypeEnum {
    
    /** A subset of attack patterns that are related through a specific attribute. For
example, a slice may refer to all attack patterns in draft status, or all existing
meta attack patterns. Members are defined by the Filter element (an XSL query). */
    Implicit = "Implicit",
    /** A subset of attack patterns that are related through some external factor. For
example, a view may represent mappings to external groupings like a Top-N list.
Members are defined externally through Member_Of relationships. */
    Explicit = "Explicit",
    /** A hierarchical representation of attack patterns based on a specific vantage point
that a user may take. The hierarchy often starts with a category, followed by a
meta/standard attack pattern, and ends with a detailed attack pattern. Members are
defined through Member_Of relationships on categories. */
    Graph = "Graph",
};


/**
 * The root element used to hold an enumerated catalog of common attack patterns.
Each catalog can be organized by optional Views and Categories. The catalog also
contains a list of all External_References that may be shared throughout the
individual attack patterns. The required Name and Version attributes are used to
uniquely identify the catalog. The required Date attribute identifies the date when
this catalog was created or last updated.
 */
export interface AttackPatternCatalog {
    /** The name of this catalog, used to uniquely identify it. */
    name: string,
    /** The version of this catalog, used to uniquely identify it. */
    version: string,
    /** The date when this catalog was created or last updated. */
    entry_date: date,
    /** The collection of attack patterns defined in this catalog. */
    attack_patterns?: AttackPattern[],
    /** The collection of categories organizing attack patterns in this catalog. */
    categories?: Category[],
    /** The collection of views providing perspectives on the attack pattern catalog. */
    views?: View[],
    /** The collection of external references shared throughout the catalog entries. */
    external_references?: ExternalReference[],
}


/**
 * An attack pattern is an abstraction mechanism for helping describe how an attack is
executed. Each pattern defines a challenge that an attacker may face, provides a
description of the common technique(s) used to meet the challenge, and presents
recommended methods for mitigating an actual attack. Attack patterns help categorize
attacks in a meaningful way in an effort to provide a coherent way of teaching
designers and developers how their systems may be attacked and how they can effectively
defend them.
 */
export interface AttackPattern {
    /** Unique integer identifier for the entry. Considered static for the lifetime of the entry. If an entry becomes deprecated, the identifier is not reused and a placeholder is left in the catalog. */
    id: number,
    /** Descriptive title used to give the reader an idea of what the entry represents. All words in the name should be capitalized except for articles and prepositions unless they begin or end the name. */
    name: string,
    /** The development and usage status level for this entry. Please refer to the StatusEnum enumeration for a list of valid values and their meanings. */
    status: string,
    /** A high level description of the attack pattern. The description should be no
longer than a few sentences and should include how malicious input is initially
supplied, the weakness being exploited, and the resulting negative technical
impact. A full step-by-step description belongs in the Execution_Flow element. */
    description: string,
    /** Additional comments and notes about this entry that cannot be captured using the other available elements. */
    notes?: Note[],
    /** Tracks the original author of this entry and any subsequent modifications to the content, providing a means of contacting authors and modifiers. */
    content_history?: ContentHistory,
    /** Links to external references for further reading and insight into this entry. Should be used when the entry is based on external sources or projects. */
    references?: Reference[],
    /** Mappings from this entry to equivalent or related entries in taxonomies outside of CAPEC, such as ATT&CK, WASC, or OWASP Attacks. */
    taxonomy_mappings?: TaxonomyMapping[],
    /** The abstraction level for this attack pattern. Defines whether this is a Meta, Standard, or Detailed level pattern. */
    abstraction: string,
    /** Additional details important to this attack pattern beyond what is conveyed in the main description, but not necessary to understand the fundamental concept. */
    extended_description?: string,
    /** One or more other names by which this attack pattern may be known. */
    alternate_terms?: AlternateTerm[],
    /** An overall average likelihood value for attacks that leverage this attack pattern, with the understanding that it will not be completely accurate for all attacks. */
    likelihood_of_attack?: string,
    /** An overall average severity value for attacks that leverage this attack pattern, with the understanding that it will not be completely accurate for all attacks. */
    typical_severity?: string,
    /** References to other attack patterns that give insight to similar items at higher and lower levels of abstraction. */
    related_attack_patterns?: RelatedAttackPattern[],
    /** A detailed step-by-step flow of the attack pattern, listing the typical steps performed by an adversary when leveraging the given technique. Usually only applicable to Detailed abstraction level attack patterns. */
    execution_flow?: AttackStep[],
    /** The conditions that must exist in order for an attack leveraging this pattern to succeed. */
    prerequisites?: string[],
    /** The level of skills or specific knowledge needed by an adversary to execute this type of attack. */
    skills_required?: Skill[],
    /** The resources (e.g., CPU cycles, IP addresses, tools) required by an adversary to effectively execute this type of attack. */
    resources_required?: string[],
    /** Activities, events, conditions or behaviors that may indicate that an attack leveraging this pattern is imminent, in progress, or has occurred. */
    indicators?: string[],
    /** Individual consequences associated with this attack pattern, specifying the security properties violated, technical impacts, and likelihoods. */
    consequences?: Consequence[],
    /** Actions or approaches to prevent or mitigate the risk of an attack that leverages this attack pattern, aimed at improving system resiliency, reducing attack surface, or reducing impact. */
    mitigations?: string[],
    /** One or more concrete example instances of this attack pattern to help the reader understand its nature, context, and variability in practical terms. */
    example_instances?: string[],
    /** References to CWE weaknesses associated with this attack pattern. Any of the weaknesses (not necessarily all) may be present for the attack to be successful. */
    related_weaknesses?: number[],
}


/**
 * A category in CAPEC is a collection of attack patterns based on some common
characteristic. More specifically, it is an aggregation of attack patterns based on
effect/intent (as opposed to actions or mechanisms, which would be a meta attack
pattern). An aggregation based on effect/intent is not an actionable attack and as
such is not a pattern of attack behavior. Rather, it is a grouping of patterns based
on some common criteria.
 */
export interface Category {
    /** Unique integer identifier for the entry. Considered static for the lifetime of the entry. If an entry becomes deprecated, the identifier is not reused and a placeholder is left in the catalog. */
    id: number,
    /** Descriptive title used to give the reader an idea of what the entry represents. All words in the name should be capitalized except for articles and prepositions unless they begin or end the name. */
    name: string,
    /** The development and usage status level for this entry. Please refer to the StatusEnum enumeration for a list of valid values and their meanings. */
    status: string,
    /** Additional comments and notes about this entry that cannot be captured using the other available elements. */
    notes?: Note[],
    /** Tracks the original author of this entry and any subsequent modifications to the content, providing a means of contacting authors and modifiers. */
    content_history?: ContentHistory,
    /** Links to external references for further reading and insight into this entry. Should be used when the entry is based on external sources or projects. */
    references?: Reference[],
    /** Mappings from this entry to equivalent or related entries in taxonomies outside of CAPEC, such as ATT&CK, WASC, or OWASP Attacks. */
    taxonomy_mappings?: TaxonomyMapping[],
    /** A short summary limited to the key points that define this category. */
    summary: string,
    /** Relationships of this category with attack patterns, other categories, and views, including Member_Of and Has_Member relationships. */
    relationships?: Relationships,
}


/**
 * A view in CAPEC represents a perspective with which one might look at the collection
of attack patterns defined within CAPEC. There are three different types of views as
defined by the Type attribute: graphs, explicit slices, and implicit slices.
 */
export interface View {
    /** Unique integer identifier for the entry. Considered static for the lifetime of the entry. If an entry becomes deprecated, the identifier is not reused and a placeholder is left in the catalog. */
    id: number,
    /** Descriptive title used to give the reader an idea of what the entry represents. All words in the name should be capitalized except for articles and prepositions unless they begin or end the name. */
    name: string,
    /** The development and usage status level for this entry. Please refer to the StatusEnum enumeration for a list of valid values and their meanings. */
    status: string,
    /** Describes how this view is constructed. Please refer to ViewTypeEnum for a list of valid values and their meanings. */
    type: string,
    /** Additional comments and notes about this entry that cannot be captured using the other available elements. */
    notes?: Note[],
    /** Tracks the original author of this entry and any subsequent modifications to the content, providing a means of contacting authors and modifiers. */
    content_history?: ContentHistory,
    /** Links to external references for further reading and insight into this entry. Should be used when the entry is based on external sources or projects. */
    references?: Reference[],
    /** Describes the perspective from which this view has been constructed and what purpose it serves for its intended audience. */
    objective: string,
    /** Reference to the target stakeholders or groups for whom this view is most relevant, along with descriptions of what properties they may find useful. */
    audience?: Stakeholder[],
    /** The members of this view, defined via Member_Of and Has_Member relationships (applicable to graph and explicit slice view types). */
    members?: Relationships,
    /** An XSL query used to identify which attack patterns are members of this view. Only applicable to implicit slice view types. */
    filter?: string,
}


/**
 * An external reference provides a pointer to where more information and deeper insight
can be obtained about an attack pattern, category, or view. Examples include research
papers and excerpts from publications. Not all elements need to be used since some are
designed for web references and others for book references.
 */
export interface ExternalReference {
    /** A globally unique identifier for this external reference (e.g., REF-1). Used by other entries to link to this reference using formats like [REF-1]. */
    reference_id: string,
    /** The author(s) of the referenced material. */
    authors?: string[],
    /** The title of the referenced material. */
    title: string,
    /** The edition of the material being referenced, in the event that multiple editions of the material exist. */
    edition?: string,
    /** The name of the magazine, journal, or other publication that contains the referenced material. */
    publication?: string,
    /** The year of publication of the referenced material. Must follow the YYYY format (xs:gYear). */
    publication_year?: string,
    /** The month of publication of the referenced material. Must follow the --MM format (xs:gMonth). */
    publication_month?: string,
    /** The day of publication of the referenced material. Must follow the ---DD format (xs:gDay). */
    publication_day?: string,
    /** The name of the publisher of the referenced material. */
    publisher?: string,
    /** A URL for the material being referenced, if one exists online. */
    url?: string,
    /** The date when the URL was validated to be accessible and correct. */
    url_date?: date,
}


/**
 * Another name or term used to describe an attack pattern. Provides context for the alternate term by which the attack pattern may be known.
 */
export interface AlternateTerm {
    /** Context and explanation for each alternate term by which this attack pattern may be known. */
    description?: string,
    /** The actual alternate term or name for the attack pattern. */
    term: string,
}


/**
 * An individual consequence associated with an attack pattern, specifying which
security properties are violated, the technical impact that arises if an adversary
succeeds, the likelihood of this specific consequence occurring, and any additional
commentary.
 */
export interface Consequence {
    /** Internal CAPEC team identifier for consequences that repeat across many individual patterns. Used to keep repeated consequences synchronized. Format: CC-N (e.g., CC-1). */
    consequence_id?: string,
    /** Identifies the security property or properties that are violated when this consequence occurs. Multiple scopes may apply simultaneously. */
    scope: string,
    /** Describes the negative technical impact(s) that arise if an adversary successfully achieves this consequence. */
    impact?: string,
    /** Identifies how likely this specific consequence is expected to be seen relative to the other consequences of the same attack pattern. */
    likelihood?: string,
    /** Additional commentary about this specific consequence. */
    note?: string,
}


/**
 * A description of the level of skills or specific knowledge needed by an adversary to execute this type of attack. Each skill entry captures both the skill level and a textual description of the knowledge required.
 */
export interface Skill {
    /** Textual description of the specific skills or knowledge the adversary must possess to execute this attack at the given skill level. */
    description: string,
    /** The skill or knowledge level required (High, Medium, Low, or Unknown). */
    level: string,
}


/**
 * An additional comment about a CAPEC entry that cannot be captured using the other available elements. Each note has a type indicating its purpose and contains content describing the note.
 */
export interface Note {
    /** The type of note, indicating its purpose (Maintenance, Relationship, Research Gap, Terminology, or Other). */
    type: string,
    /** The content of the note, potentially containing XHTML markup. */
    content: string,
}


/**
 * An individual step in the execution flow of an attack pattern. Provides a detailed
description of a specific action typically performed by an adversary during the
attack, along with the phase of the attack it belongs to and any specific techniques
used.
 */
export interface AttackStep {
    /** A description of the actions taken by the adversary during this step of the attack. */
    description: string,
    /** The sequential step number within the execution flow. */
    step: number,
    /** The phase of the attack this step belongs to (Explore, Experiment, or Exploit). */
    phase: string,
    /** Specific techniques used by the adversary during this attack step. */
    techniques?: Technique[],
}


/**
 * A specific technique used by an adversary during an attack step. Extends the structured text description with an optional reference to a related CAPEC entry.
 */
export interface Technique {
    /** Optional reference to a related CAPEC entry ID relevant to this technique. */
    capec_id?: string,
    /** Description of the specific technique, potentially containing XHTML markup. */
    description: string,
}


/**
 * A reference to another attack pattern that provides insight to similar items at
higher or lower levels of abstraction, or items that are part of a chaining or
peer relationship. Special cases may require Exclude_Related elements to capture
ancestor IDs for which this relationship is not applicable.
 */
export interface RelatedAttackPattern {
    /** The unique CAPEC integer identifier of the related attack pattern. */
    capec_id: number,
    /** One or more CAPEC identifiers of ancestors for which this relationship is not applicable (special cases only). */
    exclude_related?: ExcludeRelated[],
    /** The nature of the relationship (ChildOf, ParentOf, CanFollow, CanPrecede, CanAlsoBe, or PeerOf). */
    nature: string,
}


/**
 * Captures the CAPEC identifier of an ancestor for which a given relationship is
not applicable. Used in special cases within RelatedAttackPattern and relationship
entries.
 */
export interface ExcludeRelated {
    /** The CAPEC integer identifier of the ancestor entry for which the relationship is not applicable. */
    exclude_id: number,
}


/**
 * A reference to a CWE (Common Weakness Enumeration) weakness associated with an
attack pattern. The association implies a weakness that must exist for a given
attack to be successful. If multiple weaknesses are listed, any of them (but not
necessarily all) may be present for the attack to succeed.
 */
export interface RelatedWeakness {
    /** The CWE integer identifier of the related weakness (e.g., 79 for CWE-79: Improper Neutralization of Input During Web Page Generation). */
    cwe_id: number,
}


/**
 * A container for relationships associated with a category or view, showing
Member_Of relationships with views or categories and Has_Member relationships
with attack patterns or categories.
 */
export interface Relationships {
    /** Member_Of relationships showing that this category or view is a member of a given view or parent category, identified by CAPEC_ID. */
    member_of?: MemberOf[],
    /** Has_Member relationships showing that this category or view contains a given attack pattern or category as a member, identified by CAPEC_ID. */
    has_member?: HasMember[],
}


/**
 * Represents a Member_Of relationship indicating that the parent category or view
is a member of the specified view or parent category.
 */
export interface MemberOf {
    /** The CAPEC integer identifier of the target view or category that this entry is a member of. */
    capec_id: number,
    /** CAPEC identifiers of ancestors for which this Member_Of relationship is not applicable (special cases only). */
    exclude_related?: ExcludeRelated[],
}


/**
 * Represents a Has_Member relationship indicating that the parent category or view
contains the specified attack pattern or category as a member.
 */
export interface HasMember {
    /** The CAPEC integer identifier of the attack pattern or category that is a member of this entry. */
    capec_id: number,
    /** CAPEC identifiers of ancestors for which this Has_Member relationship is not applicable (special cases only). */
    exclude_related?: ExcludeRelated[],
}


/**
 * A link from a CAPEC entry to an external reference defined within the catalog.
The External_Reference_ID identifies which external reference is being cited.
An optional Section captures a specific section title or page number relevant
to this use of the reference.
 */
export interface Reference {
    /** The identifier of the external reference entry being linked to (e.g., REF-1). Must match a Reference_ID in the catalog's External_References. */
    external_reference_id: string,
    /** A specific section title or page number within the referenced material that is particularly relevant to this use of the reference. */
    section?: string,
}


/**
 * A mapping from a CAPEC entry (AttackPattern or Category) to an equivalent or related
entry in a different security taxonomy. Identifies the external taxonomy, the ID and
name of the external entry, and how closely the CAPEC entry aligns with it.
 */
export interface TaxonomyMapping {
    /** Identifies the external taxonomy to which this mapping is being made. */
    taxonomy_name: string,
    /** The identifier of the entry in the external taxonomy that this CAPEC entry is being mapped to. */
    entry_id?: string,
    /** The name of the entry in the external taxonomy that this CAPEC entry is being mapped to. */
    entry_name?: string,
    /** Identifies how closely the CAPEC entry aligns with the external taxonomy entry (Exact, CAPEC More Abstract, CAPEC More Specific, Imprecise, or Perspective). */
    mapping_fit?: string,
}


/**
 * A target stakeholder or group for whom a CAPEC view is relevant. Specifies
the type of stakeholder and describes which properties of the view they may
find useful.
 */
export interface Stakeholder {
    /** The type of stakeholder or group that might be interested in the view. */
    type: string,
    /** A description of what properties of the view this particular stakeholder might find useful and how it applies to their work. */
    description: string,
}


/**
 * Tracks the original author of a CAPEC entry and any subsequent modifications
to the content. Provides a means of contacting authors and modifiers for
clarifying ambiguities, merging overlapping contributions, etc.
 */
export interface ContentHistory {
    /** Identifies the original submitter, their organization, the submission date, and any comments related to the initial entry submission. */
    submission?: Submission,
    /** Records of modifications made to the entry content. A new Modification entry should exist for each change made. */
    modifications?: Modification[],
    /** Records of contributions made to the entry, identifying contributors and whether their input was donated content or general feedback. */
    contributions?: Contribution[],
    /** Previous names that were used for this entry. Should be recorded whenever a substantive name change occurs, aligned with a corresponding Modification. */
    previous_entry_names?: PreviousEntryName[],
}


/**
 * Information about the original submission of a CAPEC entry, identifying the
submitter, their organization, the date of submission, and any related comments.
 */
export interface Submission {
    /** The name of the person or team who originally submitted this entry. */
    submission_name?: string,
    /** The organization of the person who originally submitted this entry. */
    submission_organization?: string,
    /** The date on which this entry was originally submitted. */
    submission_date?: date,
    /** Any comments related to the original submission of this entry. */
    submission_comment?: string,
}


/**
 * A record of a modification made to a CAPEC entry, identifying the modifier,
their organization, the date of modification, the importance of the change,
and any related comments. Modifications that change the meaning of the entry
should be marked as Critical importance.
 */
export interface Modification {
    /** The name of the person or team who made this modification. */
    modification_name?: string,
    /** The organization of the person who made this modification. */
    modification_organization?: string,
    /** The date on which this modification was made. */
    modification_date?: date,
    /** The importance level of this modification. Modifications that change the meaning of the entry or how it might be interpreted should be marked Critical. */
    modification_importance?: string,
    /** Comments describing the nature and reason for this modification. */
    modification_comment?: string,
}


/**
 * A record of a contribution made to a CAPEC entry, identifying the contributor,
their organization, the date of contribution, the type of contribution (Content
or Feedback), and any related comments.
 */
export interface Contribution {
    /** Indicates whether the contribution was donated content or general feedback. */
    type: string,
    /** The name of the person or team who made this contribution. */
    contribution_name?: string,
    /** The organization of the person who made this contribution. */
    contribution_organization?: string,
    /** The date on which this contribution was made. */
    contribution_date?: date,
    /** Comments about the contribution and its significance. */
    contribution_comment?: string,
}


/**
 * A previous name that was used for a CAPEC entry before a substantive name change.
Should align with a corresponding Modification element that records the change.
 */
export interface PreviousEntryName {
    /** The previous name that was used for this entry. */
    name: string,
    /** The date on which this name change was made. */
    entry_date: date,
}



