export type CapecExternalReferenceReferenceID = string;
export type CapecEntryID = string;
export type CapecAttackPatternID = string;
export type CapecCategoryID = string;
export type CapecViewID = string;
/**
* How much a change to an entry matters to anyone relying on it.
*/
export enum CapecImportance {
    
    /** A change that leaves the entry's meaning as it was. */
    Normal = "Normal",
    /** A change to the entry's meaning or to how it may be read. */
    Critical = "Critical",
};
/**
* What kind of remark a note makes.
*/
export enum CapecNoteType {
    
    /** Work on the entry still to be done. */
    Maintenance = "Maintenance",
    /** Detail on how entries relate. */
    Relationship = "Relationship",
    /** Something the research community could look into further. */
    Research_Gap = "Research Gap",
    /** A question of wording, such as competing uses of one term. */
    Terminology = "Terminology",
    /** A remark of no listed kind. */
    Other = "Other",
};
/**
* How far an entry has got through CAPEC's review.
*/
export enum CapecStatus {
    
    /** Withdrawn from the catalogue, though its number stays taken. */
    Deprecated = "Deprecated",
    /** Filled in but still open to change. */
    Draft = "Draft",
    /** Still lacking required content. */
    Incomplete = "Incomplete",
    /** Still correct but no longer current. */
    Obsolete = "Obsolete",
    /** Reviewed, and not expected to change much. */
    Stable = "Stable",
    /** Reviewed closely enough to rely on. */
    Usable = "Usable",
};
/**
* How well an entry fits the entry of another taxonomy that it maps to.
*/
export enum CapecTaxonomyMappingFit {
    
    /** The two mean the same. */
    Exact = "Exact",
    /** The CAPEC entry is the wider of the two. */
    CAPEC_More_Abstract = "CAPEC More Abstract",
    /** The CAPEC entry is the narrower of the two. */
    CAPEC_More_Specific = "CAPEC More Specific",
    /** The two overlap without one holding the other. */
    Imprecise = "Imprecise",
    /** The two look at one subject from different standpoints. */
    Perspective = "Perspective",
};
/**
* The other taxonomies that CAPEC maps to.
*/
export enum CapecTaxonomyName {
    
    /** MITRE ATT&CK. An entry's Entry_ID there is the technique's number without its T. */
    ATTACK = "ATTACK",
    /** The Web Application Security Consortium's threat classification. */
    WASC = "WASC",
    /** The attack list of the Open Worldwide Application Security Project. */
    OWASP_Attacks = "OWASP Attacks",
};
/**
* Whether a contribution changed an entry's content or only commented on it.
*/
export enum CapecContributionType {
    
    /** Text given to the entry. */
    Content = "Content",
    /** Remarks on the entry. */
    Feedback = "Feedback",
};
/**
* How concrete an attack pattern is.
*/
export enum CapecAbstraction {
    
    /** A broad approach, free of any one technology, for use in design-level threat modelling. */
    Meta = "Meta",
    /** One method or technique, often only a part of a whole attack. */
    Standard = "Standard",
    /** One technique against one technology, usually with its steps set out. */
    Detailed = "Detailed",
};
/**
* How likely something is to happen.
*/
export enum CapecLikelihood {
    
    High = "High",
    Medium = "Medium",
    Low = "Low",
    /** Nobody knows how likely it is. */
    Unknown = "Unknown",
};
/**
* How one attack pattern relates to another.
*/
export enum CapecRelatedNature {
    
    /** The other pattern is more abstract, and this one specialises it. */
    ChildOf = "ChildOf",
    /** The other pattern is less abstract, and it specialises this one. */
    ParentOf = "ParentOf",
    /** In a chain of attack, this pattern may come after the other. */
    CanFollow = "CanFollow",
    /** In a chain of attack, this pattern may come before the other. */
    CanPrecede = "CanPrecede",
    /** In some settings this pattern can also be read as the other one, though not always the reverse. */
    CanAlsoBe = "CanAlsoBe",
    /** The two are alike in a way that no other nature covers. */
    PeerOf = "PeerOf",
};
/**
* The security property that a consequence violates.
*/
export enum CapecScope {
    
    Confidentiality = "Confidentiality",
    Integrity = "Integrity",
    Availability = "Availability",
    Access_Control = "Access Control",
    Accountability = "Accountability",
    Authentication = "Authentication",
    Authorization = "Authorization",
    Non_Repudiation = "Non-Repudiation",
    Other = "Other",
};
/**
* How bad the typical outcome of an attack is.
*/
export enum CapecSeverity {
    
    Very_High = "Very High",
    High = "High",
    Medium = "Medium",
    Low = "Low",
    Very_Low = "Very Low",
};
/**
* How much skill or knowledge an adversary needs.
*/
export enum CapecSkillLevel {
    
    High = "High",
    Medium = "Medium",
    Low = "Low",
    /** Nobody knows how much is needed. */
    Unknown = "Unknown",
};
/**
* The kinds of people a view is meant for.
*/
export enum CapecStakeholderType {
    
    Academic_Researchers = "Academic Researchers",
    Applied_Researchers = "Applied Researchers",
    Assessment_Customers = "Assessment Customers",
    Assessment_Vendors = "Assessment Vendors",
    CAPEC_Team = "CAPEC Team",
    Educators = "Educators",
    Information_Providers = "Information Providers",
    Software_Customers = "Software Customers",
    Software_Designers = "Software Designers",
    Software_Developers = "Software Developers",
    Software_Vendors = "Software Vendors",
    Other = "Other",
};
/**
* What a successful attack does to the system, in technical terms.
*/
export enum CapecTechnicalImpact {
    
    Modify_Data = "Modify Data",
    Read_Data = "Read Data",
    Unreliable_Execution = "Unreliable Execution",
    Resource_Consumption = "Resource Consumption",
    Execute_Unauthorized_Commands = "Execute Unauthorized Commands",
    Gain_Privileges = "Gain Privileges",
    Bypass_Protection_Mechanism = "Bypass Protection Mechanism",
    Hide_Activities = "Hide Activities",
    Alter_Execution_Logic = "Alter Execution Logic",
    Other = "Other",
};
/**
* How a view selects its entries.
*/
export enum CapecViewType {
    
    /** A slice picked by a filter on an attribute, such as every pattern of one status. */
    Implicit = "Implicit",
    /** A slice picked by hand because of something outside the catalogue, such as a list. */
    Explicit = "Explicit",
    /** A hierarchy seen from one standpoint, often from category down to detailed pattern. */
    Graph = "Graph",
};
/**
* Which stage of an attack a step belongs to.
*/
export enum CapecAttackStepPhase {
    
    /** Looking over the target. */
    Explore = "Explore",
    /** Trying things out against it. */
    Experiment = "Experiment",
    /** Carrying the attack through. */
    Exploit = "Exploit",
};


/**
 * A publication or page outside CAPEC that entries point to for more detail.
 */
export interface CapecExternalReference {
    /** The identifier entries use to cite this reference. */
    Reference_ID: string,
    /** A person or body who wrote the work. */
    Author?: string[],
    /** The work's title. */
    Title: string,
    /** Which edition of the work is meant. */
    Edition?: string,
    /** The journal, conference or larger work that holds it. */
    Publication?: string,
    /** The year it appeared. */
    Publication_Year?: string,
    /** The month it appeared. */
    Publication_Month?: string,
    /** The day of the month it appeared. */
    Publication_Day?: string,
    /** Who published it. */
    Publisher?: string,
    /** Where it can be read. */
    URL?: string,
    /** The day someone last confirmed the address worked. */
    URL_Date?: date,
}


/**
 * One citation by an entry of an external reference.
 */
export interface CapecReference {
    /** The reference cited. */
    External_Reference_ID: CapecExternalReferenceReferenceID,
    /** The section title or page that this citation means. */
    Section?: string,
}


/**
 * A remark on an entry that no other field can hold.
 */
export interface CapecNote {
    /** What kind of remark it is. */
    Type: string,
    /** The remark itself. */
    Value: string,
}


/**
 * A link from an entry to the matching entry of another taxonomy.
 */
export interface CapecTaxonomyMapping {
    /** The other taxonomy. */
    Taxonomy_Name: string,
    /** The other entry's identifier in that taxonomy. */
    Entry_ID?: string,
    /** The other entry's name in that taxonomy. */
    Entry_Name?: string,
    /** How well the two entries fit. */
    Mapping_Fit?: string,
}


/**
 * An ancestor under which a relation does not hold.
 */
export interface CapecExcludeRelated {
    /** The number of the ancestor. */
    Exclude_ID: CapecEntryID,
}


/**
 * The field of any relation that can leave out some ancestors.
 */
export interface CapecExclusionsMixin {
    /** Ancestors under which the relation does not hold. */
    Exclude_Related?: CapecExcludeRelated[],
}


/**
 * The field of an entry that can map to other taxonomies.
 */
export interface CapecTaxonomyMappedMixin {
    /** Matching entries in other taxonomies. */
    Taxonomy_Mappings?: CapecTaxonomyMapping[],
}


/**
 * Who first put an entry forward, and when.
 */
export interface CapecSubmission {
    /** The submitter's name. */
    Submission_Name?: string,
    /** The submitter's organisation. */
    Submission_Organization?: string,
    /** The day it was submitted. */
    Submission_Date?: date,
    /** A remark on the submission. */
    Submission_Comment?: string,
}


/**
 * One later edit to an entry.
 */
export interface CapecModification {
    /** The editor's name. */
    Modification_Name?: string,
    /** The editor's organisation. */
    Modification_Organization?: string,
    /** The day of the edit. */
    Modification_Date?: date,
    /** How much the edit matters to anyone relying on the entry. */
    Modification_Importance?: string,
    /** What the edit did. */
    Modification_Comment?: string,
}


/**
 * Help given to an entry by someone other than its submitter.
 */
export interface CapecContribution {
    /** Whether the help was content or feedback. */
    Type: string,
    /** The contributor's name. */
    Contribution_Name?: string,
    /** The contributor's organisation. */
    Contribution_Organization?: string,
    /** The day of the contribution. */
    Contribution_Date?: date,
    /** A remark on the contribution. */
    Contribution_Comment?: string,
}


/**
 * A name an entry used to carry.
 */
export interface CapecPreviousEntryName {
    /** The day the name changed. */
    Date: date,
    /** The earlier name. */
    Value: string,
}


/**
 * The record of who wrote and changed an entry.
 */
export interface CapecContentHistory {
    /** The entry's first submission. */
    Submission?: CapecSubmission,
    /** Each later edit. */
    Modification?: CapecModification[],
    /** Each contribution from someone else. */
    Contribution?: CapecContribution[],
    /** Each name the entry used to carry. */
    Previous_Entry_Name?: CapecPreviousEntryName[],
}


/**
 * Anything in the catalogue with a CAPEC number, whether an attack pattern, a category or a view.
 */
export interface CapecEntry {
    /** The entry's CAPEC number. */
    ID: string,
    /** The entry's name. */
    Name: string,
    /** How far the entry has got through review. */
    Status: string,
    /** The external references the entry cites. */
    References?: CapecReference[],
    /** Remarks that no other field can hold. */
    Notes?: CapecNote[],
    /** Who wrote and changed the entry. */
    Content_History?: CapecContentHistory,
}


/**
 * Another name by which an attack pattern is known.
 */
export interface CapecAlternateTerm {
    /** The other name. */
    Term: string,
    /** Where or how the other name is used. */
    Description?: string,
}


/**
 * A relation from one attack pattern to another.
 */
export interface CapecRelatedAttackPattern extends CapecExclusionsMixin {
    /** What kind of relation it is. */
    Nature: string,
    /** The other attack pattern. */
    CAPEC_ID: CapecAttackPatternID,
}


/**
 * One way of carrying out a step of an attack.
 */
export interface CapecTechnique {
    /** The entry that the technique itself amounts to. */
    CAPEC_ID?: CapecEntryID,
    /** The technique. */
    Value: string,
}


/**
 * One step of the way an adversary typically carries out an attack.
 */
export interface CapecAttackStep {
    /** The step's number. */
    Step: number,
    /** The stage of the attack it belongs to. */
    Phase: string,
    /** What the adversary does in this step. */
    Description: string,
    /** Ways of doing it. */
    Technique?: CapecTechnique[],
}


/**
 * A skill or piece of knowledge an adversary needs.
 */
export interface CapecSkill {
    /** How much of it is needed. */
    Level: string,
    /** What the skill is. */
    Value: string,
}


/**
 * One thing that can happen if an attack succeeds.
 */
export interface CapecConsequence {
    /** An identifier for this consequence. */
    Consequence_ID?: string,
    /** The security properties violated. */
    Scope: string,
    /** What the attack does to the system. */
    Impact?: string,
    /** How likely this consequence is, beside the pattern's others. */
    Likelihood?: string,
    /** A remark on the consequence. */
    Note?: string,
}


/**
 * A weakness in the Common Weakness Enumeration that can make an attack possible.
 */
export interface CapecRelatedWeakness {
    /** The weakness's number in the Common Weakness Enumeration. */
    CWE_ID: string,
}


/**
 * A statement that an entry belongs to a view or a category.
 */
export interface CapecMemberOf extends CapecExclusionsMixin {
    /** The view or category it belongs to. */
    CAPEC_ID: CapecEntryID,
}


/**
 * A statement that a view or a category holds an entry.
 */
export interface CapecHasMember extends CapecExclusionsMixin {
    /** The attack pattern or category it holds. */
    CAPEC_ID: CapecEntryID,
}


/**
 * Which entries a category or a view holds, and which it belongs to.
 */
export interface CapecRelationships {
    /** What this entry belongs to. */
    Member_Of?: CapecMemberOf[],
    /** What this entry holds. */
    Has_Member?: CapecHasMember[],
}


/**
 * One kind of person a view is meant for, and what they would get from it.
 */
export interface CapecStakeholder {
    /** The kind of person. */
    Type: string,
    /** What they would find useful in the view. */
    Description: string,
}


/**
 * A catalogued way that adversaries go about an attack, with what it takes and how to resist it.
 */
export interface CapecAttackPattern extends CapecEntry, CapecTaxonomyMappedMixin {
    /** How concrete the pattern is. */
    Abstraction: string,
    /** The pattern, in a few sentences. */
    Description: string,
    /** A longer account of the pattern. */
    Extended_Description?: string,
    /** Other names for the pattern. */
    Alternate_Terms?: CapecAlternateTerm[],
    /** How likely an attack of this kind is to succeed. */
    Likelihood_Of_Attack?: string,
    /** How bad the outcome usually is. */
    Typical_Severity?: string,
    /** The pattern's relations to others. */
    Related_Attack_Patterns?: CapecRelatedAttackPattern[],
    /** The steps an adversary typically takes. */
    Execution_Flow?: CapecAttackStep[],
    /** Conditions that must hold for the attack to work. */
    Prerequisites?: string[],
    /** The skills an adversary needs. */
    Skills_Required?: CapecSkill[],
    /** What an adversary must have to hand, such as tools or addresses. */
    Resources_Required?: string[],
    /** Signs that an attack is near, under way or over. */
    Indicators?: string[],
    /** What can happen if the attack succeeds. */
    Consequences?: CapecConsequence[],
    /** Ways to prevent the attack or lessen its harm. */
    Mitigations?: string[],
    /** Concrete examples of the attack. */
    Example_Instances?: string[],
    /** The weaknesses that can make the attack possible. */
    Related_Weaknesses?: CapecRelatedWeakness[],
}


/**
 * A group of attack patterns that share an effect or intent, and not itself a pattern of attack.
 */
export interface CapecCategory extends CapecEntry, CapecTaxonomyMappedMixin {
    /** What the patterns in this category have in common. */
    Summary: string,
    /** What the category holds and belongs to. */
    Relationships?: CapecRelationships,
}


/**
 * One way of looking over the catalogue, by a hierarchy or by a slice of its entries.
 */
export interface CapecView extends CapecEntry {
    /** How the view selects its entries. */
    Type: string,
    /** What the view is for. */
    Objective: string,
    /** Who the view is meant for. */
    Audience?: CapecStakeholder[],
    /** The entries the view holds. */
    Members?: CapecRelationships,
    /** An XPath expression over the catalogue that selects the view's entries. */
    Filter?: string,
}


/**
 * One release of the whole catalogue, with its entries and the references they share.
 */
export interface CapecAttackPatternCatalog {
    /** The catalogue's name. */
    Name: string,
    /** The catalogue's version, which together with its name identifies it. */
    Version: string,
    /** The day this catalogue was made or last updated. */
    Date: date,
    /** The attack patterns. */
    Attack_Patterns?: CapecAttackPattern[],
    /** The categories. */
    Categories?: CapecCategory[],
    /** The views. */
    Views?: CapecView[],
    /** The external references that entries cite. */
    External_References?: CapecExternalReference[],
}



