-- # Class: AttackPatternCatalog Description: The root element used to hold an enumerated catalog of common attack patterns.Each catalog can be organized by optional Views and Categories. The catalog alsocontains a list of all External_References that may be shared throughout theindividual attack patterns. The required Name and Version attributes are used touniquely identify the catalog. The required Date attribute identifies the date whenthis catalog was created or last updated.
--     * Slot: id
--     * Slot: name Description: The name of this catalog, used to uniquely identify it.
--     * Slot: version Description: The version of this catalog, used to uniquely identify it.
--     * Slot: entry_date Description: The date when this catalog was created or last updated.
-- # Class: AttackPattern Description: An attack pattern is an abstraction mechanism for helping describe how an attack isexecuted. Each pattern defines a challenge that an attacker may face, provides adescription of the common technique(s) used to meet the challenge, and presentsrecommended methods for mitigating an actual attack. Attack patterns help categorizeattacks in a meaningful way in an effort to provide a coherent way of teachingdesigners and developers how their systems may be attacked and how they can effectivelydefend them.
--     * Slot: id Description: Unique integer identifier for the entry. Considered static for the lifetime of the entry. If an entry becomes deprecated, the identifier is not reused and a placeholder is left in the catalog.
--     * Slot: name Description: Descriptive title used to give the reader an idea of what the entry represents. All words in the name should be capitalized except for articles and prepositions unless they begin or end the name.
--     * Slot: status Description: The development and usage status level for this entry. Please refer to the StatusEnum enumeration for a list of valid values and their meanings.
--     * Slot: description Description: A high level description of the attack pattern. The description should be nolonger than a few sentences and should include how malicious input is initiallysupplied, the weakness being exploited, and the resulting negative technicalimpact. A full step-by-step description belongs in the Execution_Flow element.
--     * Slot: abstraction Description: The abstraction level for this attack pattern. Defines whether this is a Meta, Standard, or Detailed level pattern.
--     * Slot: extended_description Description: Additional details important to this attack pattern beyond what is conveyed in the main description, but not necessary to understand the fundamental concept.
--     * Slot: likelihood_of_attack Description: An overall average likelihood value for attacks that leverage this attack pattern, with the understanding that it will not be completely accurate for all attacks.
--     * Slot: typical_severity Description: An overall average severity value for attacks that leverage this attack pattern, with the understanding that it will not be completely accurate for all attacks.
--     * Slot: AttackPatternCatalog_id Description: Autocreated FK slot
--     * Slot: content_history_id Description: Tracks the original author of this entry and any subsequent modifications to the content, providing a means of contacting authors and modifiers.
-- # Class: Category Description: A category in CAPEC is a collection of attack patterns based on some commoncharacteristic. More specifically, it is an aggregation of attack patterns based oneffect/intent (as opposed to actions or mechanisms, which would be a meta attackpattern). An aggregation based on effect/intent is not an actionable attack and assuch is not a pattern of attack behavior. Rather, it is a grouping of patterns basedon some common criteria.
--     * Slot: id Description: Unique integer identifier for the entry. Considered static for the lifetime of the entry. If an entry becomes deprecated, the identifier is not reused and a placeholder is left in the catalog.
--     * Slot: name Description: Descriptive title used to give the reader an idea of what the entry represents. All words in the name should be capitalized except for articles and prepositions unless they begin or end the name.
--     * Slot: status Description: The development and usage status level for this entry. Please refer to the StatusEnum enumeration for a list of valid values and their meanings.
--     * Slot: summary Description: A short summary limited to the key points that define this category.
--     * Slot: AttackPatternCatalog_id Description: Autocreated FK slot
--     * Slot: content_history_id Description: Tracks the original author of this entry and any subsequent modifications to the content, providing a means of contacting authors and modifiers.
--     * Slot: relationships_id Description: Relationships of this category with attack patterns, other categories, and views, including Member_Of and Has_Member relationships.
-- # Class: View Description: A view in CAPEC represents a perspective with which one might look at the collectionof attack patterns defined within CAPEC. There are three different types of views asdefined by the Type attribute: graphs, explicit slices, and implicit slices.
--     * Slot: id Description: Unique integer identifier for the entry. Considered static for the lifetime of the entry. If an entry becomes deprecated, the identifier is not reused and a placeholder is left in the catalog.
--     * Slot: name Description: Descriptive title used to give the reader an idea of what the entry represents. All words in the name should be capitalized except for articles and prepositions unless they begin or end the name.
--     * Slot: status Description: The development and usage status level for this entry. Please refer to the StatusEnum enumeration for a list of valid values and their meanings.
--     * Slot: type Description: Describes how this view is constructed. Please refer to ViewTypeEnum for a list of valid values and their meanings.
--     * Slot: objective Description: Describes the perspective from which this view has been constructed and what purpose it serves for its intended audience.
--     * Slot: filter Description: An XSL query used to identify which attack patterns are members of this view. Only applicable to implicit slice view types.
--     * Slot: AttackPatternCatalog_id Description: Autocreated FK slot
--     * Slot: content_history_id Description: Tracks the original author of this entry and any subsequent modifications to the content, providing a means of contacting authors and modifiers.
--     * Slot: members_id Description: The members of this view, defined via Member_Of and Has_Member relationships (applicable to graph and explicit slice view types).
-- # Class: ExternalReference Description: An external reference provides a pointer to where more information and deeper insightcan be obtained about an attack pattern, category, or view. Examples include researchpapers and excerpts from publications. Not all elements need to be used since some aredesigned for web references and others for book references.
--     * Slot: reference_id Description: A globally unique identifier for this external reference (e.g., REF-1). Used by other entries to link to this reference using formats like [REF-1].
--     * Slot: title Description: The title of the referenced material.
--     * Slot: edition Description: The edition of the material being referenced, in the event that multiple editions of the material exist.
--     * Slot: publication Description: The name of the magazine, journal, or other publication that contains the referenced material.
--     * Slot: publication_year Description: The year of publication of the referenced material. Must follow the YYYY format (xs:gYear).
--     * Slot: publication_month Description: The month of publication of the referenced material. Must follow the --MM format (xs:gMonth).
--     * Slot: publication_day Description: The day of publication of the referenced material. Must follow the ---DD format (xs:gDay).
--     * Slot: publisher Description: The name of the publisher of the referenced material.
--     * Slot: url Description: A URL for the material being referenced, if one exists online.
--     * Slot: url_date Description: The date when the URL was validated to be accessible and correct.
--     * Slot: AttackPatternCatalog_id Description: Autocreated FK slot
-- # Class: AlternateTerm Description: Another name or term used to describe an attack pattern. Provides context for the alternate term by which the attack pattern may be known.
--     * Slot: id
--     * Slot: description Description: Context and explanation for each alternate term by which this attack pattern may be known.
--     * Slot: term Description: The actual alternate term or name for the attack pattern.
--     * Slot: AttackPattern_id Description: Autocreated FK slot
-- # Class: Consequence Description: An individual consequence associated with an attack pattern, specifying whichsecurity properties are violated, the technical impact that arises if an adversarysucceeds, the likelihood of this specific consequence occurring, and any additionalcommentary.
--     * Slot: id
--     * Slot: consequence_id Description: Internal CAPEC team identifier for consequences that repeat across many individual patterns. Used to keep repeated consequences synchronized. Format: CC-N (e.g., CC-1).
--     * Slot: likelihood Description: Identifies how likely this specific consequence is expected to be seen relative to the other consequences of the same attack pattern.
--     * Slot: note Description: Additional commentary about this specific consequence.
--     * Slot: AttackPattern_id Description: Autocreated FK slot
-- # Class: Skill Description: A description of the level of skills or specific knowledge needed by an adversary to execute this type of attack. Each skill entry captures both the skill level and a textual description of the knowledge required.
--     * Slot: id
--     * Slot: description Description: Textual description of the specific skills or knowledge the adversary must possess to execute this attack at the given skill level.
--     * Slot: level Description: The skill or knowledge level required (High, Medium, Low, or Unknown).
--     * Slot: AttackPattern_id Description: Autocreated FK slot
-- # Class: Note Description: An additional comment about a CAPEC entry that cannot be captured using the other available elements. Each note has a type indicating its purpose and contains content describing the note.
--     * Slot: id
--     * Slot: type Description: The type of note, indicating its purpose (Maintenance, Relationship, Research Gap, Terminology, or Other).
--     * Slot: content Description: The content of the note, potentially containing XHTML markup.
--     * Slot: AttackPattern_id Description: Autocreated FK slot
--     * Slot: Category_id Description: Autocreated FK slot
--     * Slot: View_id Description: Autocreated FK slot
-- # Class: AttackStep Description: An individual step in the execution flow of an attack pattern. Provides a detaileddescription of a specific action typically performed by an adversary during theattack, along with the phase of the attack it belongs to and any specific techniquesused.
--     * Slot: id
--     * Slot: description Description: A description of the actions taken by the adversary during this step of the attack.
--     * Slot: step Description: The sequential step number within the execution flow.
--     * Slot: phase Description: The phase of the attack this step belongs to (Explore, Experiment, or Exploit).
--     * Slot: AttackPattern_id Description: Autocreated FK slot
-- # Class: Technique Description: A specific technique used by an adversary during an attack step. Extends the structured text description with an optional reference to a related CAPEC entry.
--     * Slot: id
--     * Slot: capec_id Description: Optional reference to a related CAPEC entry ID relevant to this technique.
--     * Slot: description Description: Description of the specific technique, potentially containing XHTML markup.
--     * Slot: AttackStep_id Description: Autocreated FK slot
-- # Class: RelatedAttackPattern Description: A reference to another attack pattern that provides insight to similar items athigher or lower levels of abstraction, or items that are part of a chaining orpeer relationship. Special cases may require Exclude_Related elements to captureancestor IDs for which this relationship is not applicable.
--     * Slot: id
--     * Slot: capec_id Description: The unique CAPEC integer identifier of the related attack pattern.
--     * Slot: nature Description: The nature of the relationship (ChildOf, ParentOf, CanFollow, CanPrecede, CanAlsoBe, or PeerOf).
--     * Slot: AttackPattern_id Description: Autocreated FK slot
-- # Class: ExcludeRelated Description: Captures the CAPEC identifier of an ancestor for which a given relationship isnot applicable. Used in special cases within RelatedAttackPattern and relationshipentries.
--     * Slot: id
--     * Slot: exclude_id Description: The CAPEC integer identifier of the ancestor entry for which the relationship is not applicable.
--     * Slot: RelatedAttackPattern_id Description: Autocreated FK slot
--     * Slot: MemberOf_id Description: Autocreated FK slot
--     * Slot: HasMember_id Description: Autocreated FK slot
-- # Class: RelatedWeakness Description: A reference to a CWE (Common Weakness Enumeration) weakness associated with anattack pattern. The association implies a weakness that must exist for a givenattack to be successful. If multiple weaknesses are listed, any of them (but notnecessarily all) may be present for the attack to succeed.
--     * Slot: id
--     * Slot: cwe_id Description: The CWE integer identifier of the related weakness (e.g., 79 for CWE-79: Improper Neutralization of Input During Web Page Generation).
-- # Class: Relationships Description: A container for relationships associated with a category or view, showingMember_Of relationships with views or categories and Has_Member relationshipswith attack patterns or categories.
--     * Slot: id
-- # Class: MemberOf Description: Represents a Member_Of relationship indicating that the parent category or viewis a member of the specified view or parent category.
--     * Slot: id
--     * Slot: capec_id Description: The CAPEC integer identifier of the target view or category that this entry is a member of.
--     * Slot: Relationships_id Description: Autocreated FK slot
-- # Class: HasMember Description: Represents a Has_Member relationship indicating that the parent category or viewcontains the specified attack pattern or category as a member.
--     * Slot: id
--     * Slot: capec_id Description: The CAPEC integer identifier of the attack pattern or category that is a member of this entry.
--     * Slot: Relationships_id Description: Autocreated FK slot
-- # Class: Reference Description: A link from a CAPEC entry to an external reference defined within the catalog.The External_Reference_ID identifies which external reference is being cited.An optional Section captures a specific section title or page number relevantto this use of the reference.
--     * Slot: id
--     * Slot: external_reference_id Description: The identifier of the external reference entry being linked to (e.g., REF-1). Must match a Reference_ID in the catalog's External_References.
--     * Slot: section Description: A specific section title or page number within the referenced material that is particularly relevant to this use of the reference.
--     * Slot: AttackPattern_id Description: Autocreated FK slot
--     * Slot: Category_id Description: Autocreated FK slot
--     * Slot: View_id Description: Autocreated FK slot
-- # Class: TaxonomyMapping Description: A mapping from a CAPEC entry (AttackPattern or Category) to an equivalent or relatedentry in a different security taxonomy. Identifies the external taxonomy, the ID andname of the external entry, and how closely the CAPEC entry aligns with it.
--     * Slot: id
--     * Slot: taxonomy_name Description: Identifies the external taxonomy to which this mapping is being made.
--     * Slot: entry_id Description: The identifier of the entry in the external taxonomy that this CAPEC entry is being mapped to.
--     * Slot: entry_name Description: The name of the entry in the external taxonomy that this CAPEC entry is being mapped to.
--     * Slot: mapping_fit Description: Identifies how closely the CAPEC entry aligns with the external taxonomy entry (Exact, CAPEC More Abstract, CAPEC More Specific, Imprecise, or Perspective).
--     * Slot: AttackPattern_id Description: Autocreated FK slot
--     * Slot: Category_id Description: Autocreated FK slot
-- # Class: Stakeholder Description: A target stakeholder or group for whom a CAPEC view is relevant. Specifiesthe type of stakeholder and describes which properties of the view they mayfind useful.
--     * Slot: id
--     * Slot: type Description: The type of stakeholder or group that might be interested in the view.
--     * Slot: description Description: A description of what properties of the view this particular stakeholder might find useful and how it applies to their work.
--     * Slot: View_id Description: Autocreated FK slot
-- # Class: ContentHistory Description: Tracks the original author of a CAPEC entry and any subsequent modificationsto the content. Provides a means of contacting authors and modifiers forclarifying ambiguities, merging overlapping contributions, etc.
--     * Slot: id
--     * Slot: submission_id Description: Identifies the original submitter, their organization, the submission date, and any comments related to the initial entry submission.
-- # Class: Submission Description: Information about the original submission of a CAPEC entry, identifying thesubmitter, their organization, the date of submission, and any related comments.
--     * Slot: id
--     * Slot: submission_name Description: The name of the person or team who originally submitted this entry.
--     * Slot: submission_organization Description: The organization of the person who originally submitted this entry.
--     * Slot: submission_date Description: The date on which this entry was originally submitted.
--     * Slot: submission_comment Description: Any comments related to the original submission of this entry.
-- # Class: Modification Description: A record of a modification made to a CAPEC entry, identifying the modifier,their organization, the date of modification, the importance of the change,and any related comments. Modifications that change the meaning of the entryshould be marked as Critical importance.
--     * Slot: id
--     * Slot: modification_name Description: The name of the person or team who made this modification.
--     * Slot: modification_organization Description: The organization of the person who made this modification.
--     * Slot: modification_date Description: The date on which this modification was made.
--     * Slot: modification_importance Description: The importance level of this modification. Modifications that change the meaning of the entry or how it might be interpreted should be marked Critical.
--     * Slot: modification_comment Description: Comments describing the nature and reason for this modification.
--     * Slot: ContentHistory_id Description: Autocreated FK slot
-- # Class: Contribution Description: A record of a contribution made to a CAPEC entry, identifying the contributor,their organization, the date of contribution, the type of contribution (Contentor Feedback), and any related comments.
--     * Slot: id
--     * Slot: type Description: Indicates whether the contribution was donated content or general feedback.
--     * Slot: contribution_name Description: The name of the person or team who made this contribution.
--     * Slot: contribution_organization Description: The organization of the person who made this contribution.
--     * Slot: contribution_date Description: The date on which this contribution was made.
--     * Slot: contribution_comment Description: Comments about the contribution and its significance.
--     * Slot: ContentHistory_id Description: Autocreated FK slot
-- # Class: PreviousEntryName Description: A previous name that was used for a CAPEC entry before a substantive name change.Should align with a corresponding Modification element that records the change.
--     * Slot: id
--     * Slot: name Description: The previous name that was used for this entry.
--     * Slot: entry_date Description: The date on which this name change was made.
--     * Slot: ContentHistory_id Description: Autocreated FK slot
-- # Class: AttackPattern_prerequisites
--     * Slot: AttackPattern_id Description: Autocreated FK slot
--     * Slot: prerequisites Description: The conditions that must exist in order for an attack leveraging this pattern to succeed.
-- # Class: AttackPattern_resources_required
--     * Slot: AttackPattern_id Description: Autocreated FK slot
--     * Slot: resources_required Description: The resources (e.g., CPU cycles, IP addresses, tools) required by an adversary to effectively execute this type of attack.
-- # Class: AttackPattern_indicators
--     * Slot: AttackPattern_id Description: Autocreated FK slot
--     * Slot: indicators Description: Activities, events, conditions or behaviors that may indicate that an attack leveraging this pattern is imminent, in progress, or has occurred.
-- # Class: AttackPattern_mitigations
--     * Slot: AttackPattern_id Description: Autocreated FK slot
--     * Slot: mitigations Description: Actions or approaches to prevent or mitigate the risk of an attack that leverages this attack pattern, aimed at improving system resiliency, reducing attack surface, or reducing impact.
-- # Class: AttackPattern_example_instances
--     * Slot: AttackPattern_id Description: Autocreated FK slot
--     * Slot: example_instances Description: One or more concrete example instances of this attack pattern to help the reader understand its nature, context, and variability in practical terms.
-- # Class: AttackPattern_related_weaknesses
--     * Slot: AttackPattern_id Description: Autocreated FK slot
--     * Slot: related_weaknesses Description: References to CWE weaknesses associated with this attack pattern. Any of the weaknesses (not necessarily all) may be present for the attack to be successful.
-- # Class: ExternalReference_authors
--     * Slot: ExternalReference_reference_id Description: Autocreated FK slot
--     * Slot: authors Description: The author(s) of the referenced material.
-- # Class: Consequence_scope
--     * Slot: Consequence_id Description: Autocreated FK slot
--     * Slot: scope Description: Identifies the security property or properties that are violated when this consequence occurs. Multiple scopes may apply simultaneously.
-- # Class: Consequence_impact
--     * Slot: Consequence_id Description: Autocreated FK slot
--     * Slot: impact Description: Describes the negative technical impact(s) that arise if an adversary successfully achieves this consequence.

CREATE TABLE "AttackPatternCatalog" (
	id INTEGER NOT NULL,
	name TEXT NOT NULL,
	version TEXT NOT NULL,
	entry_date DATE NOT NULL,
	PRIMARY KEY (id)
);
CREATE INDEX "ix_AttackPatternCatalog_id" ON "AttackPatternCatalog" (id);

CREATE TABLE "RelatedWeakness" (
	id INTEGER NOT NULL,
	cwe_id INTEGER NOT NULL,
	PRIMARY KEY (id)
);
CREATE INDEX "ix_RelatedWeakness_id" ON "RelatedWeakness" (id);

CREATE TABLE "Relationships" (
	id INTEGER NOT NULL,
	PRIMARY KEY (id)
);
CREATE INDEX "ix_Relationships_id" ON "Relationships" (id);

CREATE TABLE "Submission" (
	id INTEGER NOT NULL,
	submission_name TEXT,
	submission_organization TEXT,
	submission_date DATE,
	submission_comment TEXT,
	PRIMARY KEY (id)
);
CREATE INDEX "ix_Submission_id" ON "Submission" (id);

CREATE TABLE "ExternalReference" (
	reference_id TEXT NOT NULL,
	title TEXT NOT NULL,
	edition TEXT,
	publication TEXT,
	publication_year TEXT,
	publication_month TEXT,
	publication_day TEXT,
	publisher TEXT,
	url TEXT,
	url_date DATE,
	"AttackPatternCatalog_id" INTEGER,
	PRIMARY KEY (reference_id),
	FOREIGN KEY("AttackPatternCatalog_id") REFERENCES "AttackPatternCatalog" (id)
);
CREATE INDEX "ix_ExternalReference_reference_id" ON "ExternalReference" (reference_id);

CREATE TABLE "MemberOf" (
	id INTEGER NOT NULL,
	capec_id INTEGER NOT NULL,
	"Relationships_id" INTEGER,
	PRIMARY KEY (id),
	FOREIGN KEY("Relationships_id") REFERENCES "Relationships" (id)
);
CREATE INDEX "ix_MemberOf_id" ON "MemberOf" (id);

CREATE TABLE "HasMember" (
	id INTEGER NOT NULL,
	capec_id INTEGER NOT NULL,
	"Relationships_id" INTEGER,
	PRIMARY KEY (id),
	FOREIGN KEY("Relationships_id") REFERENCES "Relationships" (id)
);
CREATE INDEX "ix_HasMember_id" ON "HasMember" (id);

CREATE TABLE "ContentHistory" (
	id INTEGER NOT NULL,
	submission_id INTEGER,
	PRIMARY KEY (id),
	FOREIGN KEY(submission_id) REFERENCES "Submission" (id)
);
CREATE INDEX "ix_ContentHistory_id" ON "ContentHistory" (id);

CREATE TABLE "AttackPattern" (
	id INTEGER NOT NULL,
	name TEXT NOT NULL,
	status VARCHAR(10) NOT NULL,
	description TEXT NOT NULL,
	abstraction VARCHAR(8) NOT NULL,
	extended_description TEXT,
	likelihood_of_attack VARCHAR(7),
	typical_severity VARCHAR(9),
	"AttackPatternCatalog_id" INTEGER,
	content_history_id INTEGER,
	PRIMARY KEY (id),
	FOREIGN KEY("AttackPatternCatalog_id") REFERENCES "AttackPatternCatalog" (id),
	FOREIGN KEY(content_history_id) REFERENCES "ContentHistory" (id)
);
CREATE INDEX "ix_AttackPattern_id" ON "AttackPattern" (id);

CREATE TABLE "Category" (
	id INTEGER NOT NULL,
	name TEXT NOT NULL,
	status VARCHAR(10) NOT NULL,
	summary TEXT NOT NULL,
	"AttackPatternCatalog_id" INTEGER,
	content_history_id INTEGER,
	relationships_id INTEGER,
	PRIMARY KEY (id),
	FOREIGN KEY("AttackPatternCatalog_id") REFERENCES "AttackPatternCatalog" (id),
	FOREIGN KEY(content_history_id) REFERENCES "ContentHistory" (id),
	FOREIGN KEY(relationships_id) REFERENCES "Relationships" (id)
);
CREATE INDEX "ix_Category_id" ON "Category" (id);

CREATE TABLE "View" (
	id INTEGER NOT NULL,
	name TEXT NOT NULL,
	status VARCHAR(10) NOT NULL,
	type VARCHAR(8) NOT NULL,
	objective TEXT NOT NULL,
	filter TEXT,
	"AttackPatternCatalog_id" INTEGER,
	content_history_id INTEGER,
	members_id INTEGER,
	PRIMARY KEY (id),
	FOREIGN KEY("AttackPatternCatalog_id") REFERENCES "AttackPatternCatalog" (id),
	FOREIGN KEY(content_history_id) REFERENCES "ContentHistory" (id),
	FOREIGN KEY(members_id) REFERENCES "Relationships" (id)
);
CREATE INDEX "ix_View_id" ON "View" (id);

CREATE TABLE "Modification" (
	id INTEGER NOT NULL,
	modification_name TEXT,
	modification_organization TEXT,
	modification_date DATE,
	modification_importance VARCHAR(8),
	modification_comment TEXT,
	"ContentHistory_id" INTEGER,
	PRIMARY KEY (id),
	FOREIGN KEY("ContentHistory_id") REFERENCES "ContentHistory" (id)
);
CREATE INDEX "ix_Modification_id" ON "Modification" (id);

CREATE TABLE "Contribution" (
	id INTEGER NOT NULL,
	type VARCHAR(8) NOT NULL,
	contribution_name TEXT,
	contribution_organization TEXT,
	contribution_date DATE,
	contribution_comment TEXT,
	"ContentHistory_id" INTEGER,
	PRIMARY KEY (id),
	FOREIGN KEY("ContentHistory_id") REFERENCES "ContentHistory" (id)
);
CREATE INDEX "ix_Contribution_id" ON "Contribution" (id);

CREATE TABLE "PreviousEntryName" (
	id INTEGER NOT NULL,
	name TEXT NOT NULL,
	entry_date DATE NOT NULL,
	"ContentHistory_id" INTEGER,
	PRIMARY KEY (id),
	FOREIGN KEY("ContentHistory_id") REFERENCES "ContentHistory" (id)
);
CREATE INDEX "ix_PreviousEntryName_id" ON "PreviousEntryName" (id);

CREATE TABLE "ExternalReference_authors" (
	"ExternalReference_reference_id" TEXT,
	authors TEXT,
	PRIMARY KEY ("ExternalReference_reference_id", authors),
	FOREIGN KEY("ExternalReference_reference_id") REFERENCES "ExternalReference" (reference_id)
);
CREATE INDEX "ix_ExternalReference_authors_authors" ON "ExternalReference_authors" (authors);
CREATE INDEX "ix_ExternalReference_authors_ExternalReference_reference_id" ON "ExternalReference_authors" ("ExternalReference_reference_id");

CREATE TABLE "AlternateTerm" (
	id INTEGER NOT NULL,
	description TEXT,
	term TEXT NOT NULL,
	"AttackPattern_id" INTEGER,
	PRIMARY KEY (id),
	FOREIGN KEY("AttackPattern_id") REFERENCES "AttackPattern" (id)
);
CREATE INDEX "ix_AlternateTerm_id" ON "AlternateTerm" (id);

CREATE TABLE "Consequence" (
	id INTEGER NOT NULL,
	consequence_id TEXT,
	likelihood VARCHAR(7),
	note TEXT,
	"AttackPattern_id" INTEGER,
	PRIMARY KEY (id),
	FOREIGN KEY("AttackPattern_id") REFERENCES "AttackPattern" (id)
);
CREATE INDEX "ix_Consequence_id" ON "Consequence" (id);

CREATE TABLE "Skill" (
	id INTEGER NOT NULL,
	description TEXT NOT NULL,
	level VARCHAR(7) NOT NULL,
	"AttackPattern_id" INTEGER,
	PRIMARY KEY (id),
	FOREIGN KEY("AttackPattern_id") REFERENCES "AttackPattern" (id)
);
CREATE INDEX "ix_Skill_id" ON "Skill" (id);

CREATE TABLE "Note" (
	id INTEGER NOT NULL,
	type VARCHAR(12) NOT NULL,
	content TEXT NOT NULL,
	"AttackPattern_id" INTEGER,
	"Category_id" INTEGER,
	"View_id" INTEGER,
	PRIMARY KEY (id),
	FOREIGN KEY("AttackPattern_id") REFERENCES "AttackPattern" (id),
	FOREIGN KEY("Category_id") REFERENCES "Category" (id),
	FOREIGN KEY("View_id") REFERENCES "View" (id)
);
CREATE INDEX "ix_Note_id" ON "Note" (id);

CREATE TABLE "AttackStep" (
	id INTEGER NOT NULL,
	description TEXT NOT NULL,
	step INTEGER NOT NULL,
	phase VARCHAR(10) NOT NULL,
	"AttackPattern_id" INTEGER,
	PRIMARY KEY (id),
	FOREIGN KEY("AttackPattern_id") REFERENCES "AttackPattern" (id)
);
CREATE INDEX "ix_AttackStep_id" ON "AttackStep" (id);

CREATE TABLE "RelatedAttackPattern" (
	id INTEGER NOT NULL,
	capec_id INTEGER NOT NULL,
	nature VARCHAR(10) NOT NULL,
	"AttackPattern_id" INTEGER,
	PRIMARY KEY (id),
	FOREIGN KEY("AttackPattern_id") REFERENCES "AttackPattern" (id)
);
CREATE INDEX "ix_RelatedAttackPattern_id" ON "RelatedAttackPattern" (id);

CREATE TABLE "Reference" (
	id INTEGER NOT NULL,
	external_reference_id TEXT NOT NULL,
	section TEXT,
	"AttackPattern_id" INTEGER,
	"Category_id" INTEGER,
	"View_id" INTEGER,
	PRIMARY KEY (id),
	FOREIGN KEY("AttackPattern_id") REFERENCES "AttackPattern" (id),
	FOREIGN KEY("Category_id") REFERENCES "Category" (id),
	FOREIGN KEY("View_id") REFERENCES "View" (id)
);
CREATE INDEX "ix_Reference_id" ON "Reference" (id);

CREATE TABLE "TaxonomyMapping" (
	id INTEGER NOT NULL,
	taxonomy_name VARCHAR(13) NOT NULL,
	entry_id TEXT,
	entry_name TEXT,
	mapping_fit VARCHAR(19),
	"AttackPattern_id" INTEGER,
	"Category_id" INTEGER,
	PRIMARY KEY (id),
	FOREIGN KEY("AttackPattern_id") REFERENCES "AttackPattern" (id),
	FOREIGN KEY("Category_id") REFERENCES "Category" (id)
);
CREATE INDEX "ix_TaxonomyMapping_id" ON "TaxonomyMapping" (id);

CREATE TABLE "Stakeholder" (
	id INTEGER NOT NULL,
	type VARCHAR(21) NOT NULL,
	description TEXT NOT NULL,
	"View_id" INTEGER,
	PRIMARY KEY (id),
	FOREIGN KEY("View_id") REFERENCES "View" (id)
);
CREATE INDEX "ix_Stakeholder_id" ON "Stakeholder" (id);

CREATE TABLE "AttackPattern_prerequisites" (
	"AttackPattern_id" INTEGER,
	prerequisites TEXT,
	PRIMARY KEY ("AttackPattern_id", prerequisites),
	FOREIGN KEY("AttackPattern_id") REFERENCES "AttackPattern" (id)
);
CREATE INDEX "ix_AttackPattern_prerequisites_AttackPattern_id" ON "AttackPattern_prerequisites" ("AttackPattern_id");
CREATE INDEX "ix_AttackPattern_prerequisites_prerequisites" ON "AttackPattern_prerequisites" (prerequisites);

CREATE TABLE "AttackPattern_resources_required" (
	"AttackPattern_id" INTEGER,
	resources_required TEXT,
	PRIMARY KEY ("AttackPattern_id", resources_required),
	FOREIGN KEY("AttackPattern_id") REFERENCES "AttackPattern" (id)
);
CREATE INDEX "ix_AttackPattern_resources_required_AttackPattern_id" ON "AttackPattern_resources_required" ("AttackPattern_id");
CREATE INDEX "ix_AttackPattern_resources_required_resources_required" ON "AttackPattern_resources_required" (resources_required);

CREATE TABLE "AttackPattern_indicators" (
	"AttackPattern_id" INTEGER,
	indicators TEXT,
	PRIMARY KEY ("AttackPattern_id", indicators),
	FOREIGN KEY("AttackPattern_id") REFERENCES "AttackPattern" (id)
);
CREATE INDEX "ix_AttackPattern_indicators_indicators" ON "AttackPattern_indicators" (indicators);
CREATE INDEX "ix_AttackPattern_indicators_AttackPattern_id" ON "AttackPattern_indicators" ("AttackPattern_id");

CREATE TABLE "AttackPattern_mitigations" (
	"AttackPattern_id" INTEGER,
	mitigations TEXT,
	PRIMARY KEY ("AttackPattern_id", mitigations),
	FOREIGN KEY("AttackPattern_id") REFERENCES "AttackPattern" (id)
);
CREATE INDEX "ix_AttackPattern_mitigations_mitigations" ON "AttackPattern_mitigations" (mitigations);
CREATE INDEX "ix_AttackPattern_mitigations_AttackPattern_id" ON "AttackPattern_mitigations" ("AttackPattern_id");

CREATE TABLE "AttackPattern_example_instances" (
	"AttackPattern_id" INTEGER,
	example_instances TEXT,
	PRIMARY KEY ("AttackPattern_id", example_instances),
	FOREIGN KEY("AttackPattern_id") REFERENCES "AttackPattern" (id)
);
CREATE INDEX "ix_AttackPattern_example_instances_example_instances" ON "AttackPattern_example_instances" (example_instances);
CREATE INDEX "ix_AttackPattern_example_instances_AttackPattern_id" ON "AttackPattern_example_instances" ("AttackPattern_id");

CREATE TABLE "AttackPattern_related_weaknesses" (
	"AttackPattern_id" INTEGER,
	related_weaknesses INTEGER,
	PRIMARY KEY ("AttackPattern_id", related_weaknesses),
	FOREIGN KEY("AttackPattern_id") REFERENCES "AttackPattern" (id)
);
CREATE INDEX "ix_AttackPattern_related_weaknesses_related_weaknesses" ON "AttackPattern_related_weaknesses" (related_weaknesses);
CREATE INDEX "ix_AttackPattern_related_weaknesses_AttackPattern_id" ON "AttackPattern_related_weaknesses" ("AttackPattern_id");

CREATE TABLE "Technique" (
	id INTEGER NOT NULL,
	capec_id TEXT,
	description TEXT NOT NULL,
	"AttackStep_id" INTEGER,
	PRIMARY KEY (id),
	FOREIGN KEY("AttackStep_id") REFERENCES "AttackStep" (id)
);
CREATE INDEX "ix_Technique_id" ON "Technique" (id);

CREATE TABLE "ExcludeRelated" (
	id INTEGER NOT NULL,
	exclude_id INTEGER NOT NULL,
	"RelatedAttackPattern_id" INTEGER,
	"MemberOf_id" INTEGER,
	"HasMember_id" INTEGER,
	PRIMARY KEY (id),
	FOREIGN KEY("RelatedAttackPattern_id") REFERENCES "RelatedAttackPattern" (id),
	FOREIGN KEY("MemberOf_id") REFERENCES "MemberOf" (id),
	FOREIGN KEY("HasMember_id") REFERENCES "HasMember" (id)
);
CREATE INDEX "ix_ExcludeRelated_id" ON "ExcludeRelated" (id);

CREATE TABLE "Consequence_scope" (
	"Consequence_id" INTEGER,
	scope VARCHAR(15) NOT NULL,
	PRIMARY KEY ("Consequence_id", scope),
	FOREIGN KEY("Consequence_id") REFERENCES "Consequence" (id)
);
CREATE INDEX "ix_Consequence_scope_Consequence_id" ON "Consequence_scope" ("Consequence_id");
CREATE INDEX "ix_Consequence_scope_scope" ON "Consequence_scope" (scope);

CREATE TABLE "Consequence_impact" (
	"Consequence_id" INTEGER,
	impact VARCHAR(29),
	PRIMARY KEY ("Consequence_id", impact),
	FOREIGN KEY("Consequence_id") REFERENCES "Consequence" (id)
);
CREATE INDEX "ix_Consequence_impact_impact" ON "Consequence_impact" (impact);
CREATE INDEX "ix_Consequence_impact_Consequence_id" ON "Consequence_impact" ("Consequence_id");
