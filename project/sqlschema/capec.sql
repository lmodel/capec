-- # Class: CapecAttackPatternCatalog Description: One release of the whole catalogue, with its entries and the references they share.
--     * Slot: id
--     * Slot: Name Description: The catalogue's name.
--     * Slot: Version Description: The catalogue's version, which together with its name identifies it.
--     * Slot: Date Description: The day this catalogue was made or last updated.
-- # Class: CapecExternalReference Description: A publication or page outside CAPEC that entries point to for more detail.
--     * Slot: Reference_ID Description: The identifier entries use to cite this reference.
--     * Slot: Title Description: The work's title.
--     * Slot: Edition Description: Which edition of the work is meant.
--     * Slot: Publication Description: The journal, conference or larger work that holds it.
--     * Slot: Publication_Year Description: The year it appeared.
--     * Slot: Publication_Month Description: The month it appeared.
--     * Slot: Publication_Day Description: The day of the month it appeared.
--     * Slot: Publisher Description: Who published it.
--     * Slot: URL Description: Where it can be read.
--     * Slot: URL_Date Description: The day someone last confirmed the address worked.
--     * Slot: CapecAttackPatternCatalog_id Description: Autocreated FK slot
-- # Class: CapecReference Description: One citation by an entry of an external reference.
--     * Slot: id
--     * Slot: External_Reference_ID Description: The reference cited.
--     * Slot: Section Description: The section title or page that this citation means.
--     * Slot: CapecEntry_ID Description: Autocreated FK slot
--     * Slot: CapecAttackPattern_ID Description: Autocreated FK slot
--     * Slot: CapecCategory_ID Description: Autocreated FK slot
--     * Slot: CapecView_ID Description: Autocreated FK slot
-- # Class: CapecNote Description: A remark on an entry that no other field can hold.
--     * Slot: id
--     * Slot: Type Description: What kind of remark it is.
--     * Slot: Value Description: The remark itself.
--     * Slot: CapecEntry_ID Description: Autocreated FK slot
--     * Slot: CapecAttackPattern_ID Description: Autocreated FK slot
--     * Slot: CapecCategory_ID Description: Autocreated FK slot
--     * Slot: CapecView_ID Description: Autocreated FK slot
-- # Class: CapecTaxonomyMapping Description: A link from an entry to the matching entry of another taxonomy.
--     * Slot: id
--     * Slot: Taxonomy_Name Description: The other taxonomy.
--     * Slot: Entry_ID Description: The other entry's identifier in that taxonomy.
--     * Slot: Entry_Name Description: The other entry's name in that taxonomy.
--     * Slot: Mapping_Fit Description: How well the two entries fit.
--     * Slot: CapecTaxonomyMappedMixin_id Description: Autocreated FK slot
--     * Slot: CapecAttackPattern_ID Description: Autocreated FK slot
--     * Slot: CapecCategory_ID Description: Autocreated FK slot
-- # Class: CapecExcludeRelated Description: An ancestor under which a relation does not hold.
--     * Slot: id
--     * Slot: Exclude_ID Description: The number of the ancestor.
--     * Slot: CapecExclusionsMixin_id Description: Autocreated FK slot
--     * Slot: CapecRelatedAttackPattern_id Description: Autocreated FK slot
--     * Slot: CapecMemberOf_id Description: Autocreated FK slot
--     * Slot: CapecHasMember_id Description: Autocreated FK slot
-- # Class: CapecExclusionsMixin Description: The field of any relation that can leave out some ancestors.
--     * Slot: id
-- # Class: CapecTaxonomyMappedMixin Description: The field of an entry that can map to other taxonomies.
--     * Slot: id
-- # Class: CapecSubmission Description: Who first put an entry forward, and when.
--     * Slot: id
--     * Slot: Submission_Name Description: The submitter's name.
--     * Slot: Submission_Organization Description: The submitter's organisation.
--     * Slot: Submission_Date Description: The day it was submitted.
--     * Slot: Submission_Comment Description: A remark on the submission.
-- # Class: CapecModification Description: One later edit to an entry.
--     * Slot: id
--     * Slot: Modification_Name Description: The editor's name.
--     * Slot: Modification_Organization Description: The editor's organisation.
--     * Slot: Modification_Date Description: The day of the edit.
--     * Slot: Modification_Importance Description: How much the edit matters to anyone relying on the entry.
--     * Slot: Modification_Comment Description: What the edit did.
--     * Slot: CapecContentHistory_id Description: Autocreated FK slot
-- # Class: CapecContribution Description: Help given to an entry by someone other than its submitter.
--     * Slot: id
--     * Slot: Type Description: Whether the help was content or feedback.
--     * Slot: Contribution_Name Description: The contributor's name.
--     * Slot: Contribution_Organization Description: The contributor's organisation.
--     * Slot: Contribution_Date Description: The day of the contribution.
--     * Slot: Contribution_Comment Description: A remark on the contribution.
--     * Slot: CapecContentHistory_id Description: Autocreated FK slot
-- # Class: CapecPreviousEntryName Description: A name an entry used to carry.
--     * Slot: id
--     * Slot: Date Description: The day the name changed.
--     * Slot: Value Description: The earlier name.
--     * Slot: CapecContentHistory_id Description: Autocreated FK slot
-- # Class: CapecContentHistory Description: The record of who wrote and changed an entry.
--     * Slot: id
--     * Slot: Submission_id Description: The entry's first submission.
-- # Abstract Class: CapecEntry Description: Anything in the catalogue with a CAPEC number, whether an attack pattern, a category or a view.
--     * Slot: ID Description: The entry's CAPEC number.
--     * Slot: Name Description: The entry's name.
--     * Slot: Status Description: How far the entry has got through review.
--     * Slot: Content_History_id Description: Who wrote and changed the entry.
-- # Class: CapecAlternateTerm Description: Another name by which an attack pattern is known.
--     * Slot: id
--     * Slot: Term Description: The other name.
--     * Slot: Description Description: Where or how the other name is used.
--     * Slot: CapecAttackPattern_ID Description: Autocreated FK slot
-- # Class: CapecRelatedAttackPattern Description: A relation from one attack pattern to another.
--     * Slot: id
--     * Slot: Nature Description: What kind of relation it is.
--     * Slot: CAPEC_ID Description: The other attack pattern.
--     * Slot: CapecAttackPattern_ID Description: Autocreated FK slot
-- # Class: CapecTechnique Description: One way of carrying out a step of an attack.
--     * Slot: id
--     * Slot: CAPEC_ID Description: The entry that the technique itself amounts to.
--     * Slot: Value Description: The technique.
--     * Slot: CapecAttackStep_id Description: Autocreated FK slot
-- # Class: CapecAttackStep Description: One step of the way an adversary typically carries out an attack.
--     * Slot: id
--     * Slot: Step Description: The step's number.
--     * Slot: Phase Description: The stage of the attack it belongs to.
--     * Slot: Description Description: What the adversary does in this step.
--     * Slot: CapecAttackPattern_ID Description: Autocreated FK slot
-- # Class: CapecSkill Description: A skill or piece of knowledge an adversary needs.
--     * Slot: id
--     * Slot: Level Description: How much of it is needed.
--     * Slot: Value Description: What the skill is.
--     * Slot: CapecAttackPattern_ID Description: Autocreated FK slot
-- # Class: CapecConsequence Description: One thing that can happen if an attack succeeds.
--     * Slot: id
--     * Slot: Consequence_ID Description: The CAPEC team's identifier for a consequence repeated across patterns, in the form CC-1.
--     * Slot: Likelihood Description: How likely this consequence is, beside the pattern's others.
--     * Slot: Note Description: A remark on the consequence.
--     * Slot: CapecAttackPattern_ID Description: Autocreated FK slot
-- # Class: CapecRelatedWeakness Description: A weakness in the Common Weakness Enumeration that can make an attack possible.
--     * Slot: id
--     * Slot: CWE_ID Description: The weakness's number in the Common Weakness Enumeration.
--     * Slot: CapecAttackPattern_ID Description: Autocreated FK slot
-- # Class: CapecMemberOf Description: A statement that an entry belongs to a view or a category.
--     * Slot: id
--     * Slot: CAPEC_ID Description: The view or category it belongs to.
--     * Slot: CapecRelationships_id Description: Autocreated FK slot
-- # Class: CapecHasMember Description: A statement that a view or a category holds an entry.
--     * Slot: id
--     * Slot: CAPEC_ID Description: The attack pattern or category it holds.
--     * Slot: CapecRelationships_id Description: Autocreated FK slot
-- # Class: CapecRelationships Description: Which entries a category or a view holds, and which it belongs to.
--     * Slot: id
-- # Class: CapecStakeholder Description: One kind of person a view is meant for, and what they would get from it.
--     * Slot: id
--     * Slot: Type Description: The kind of person.
--     * Slot: Description Description: What they would find useful in the view.
--     * Slot: CapecView_ID Description: Autocreated FK slot
-- # Class: CapecAttackPattern Description: A catalogued way that adversaries go about an attack, with what it takes and how to resist it.
--     * Slot: Abstraction Description: How concrete the pattern is.
--     * Slot: Description Description: The pattern, in a few sentences.
--     * Slot: Extended_Description Description: A longer account of the pattern.
--     * Slot: Likelihood_Of_Attack Description: How likely an attack of this kind is to succeed.
--     * Slot: Typical_Severity Description: How bad the outcome usually is.
--     * Slot: ID Description: The entry's CAPEC number.
--     * Slot: Name Description: The entry's name.
--     * Slot: Status Description: How far the entry has got through review.
--     * Slot: CapecAttackPatternCatalog_id Description: Autocreated FK slot
--     * Slot: Content_History_id Description: Who wrote and changed the entry.
-- # Class: CapecCategory Description: A group of attack patterns that share an effect or intent, and not itself a pattern of attack.
--     * Slot: Summary Description: What the patterns in this category have in common.
--     * Slot: ID Description: The entry's CAPEC number.
--     * Slot: Name Description: The entry's name.
--     * Slot: Status Description: How far the entry has got through review.
--     * Slot: CapecAttackPatternCatalog_id Description: Autocreated FK slot
--     * Slot: Relationships_id Description: What the category holds and belongs to.
--     * Slot: Content_History_id Description: Who wrote and changed the entry.
-- # Class: CapecView Description: One way of looking over the catalogue, by a hierarchy or by a slice of its entries.
--     * Slot: Type Description: How the view selects its entries.
--     * Slot: Objective Description: What the view is for.
--     * Slot: Filter Description: A query over the catalogue that selects the view's entries.
--     * Slot: ID Description: The entry's CAPEC number.
--     * Slot: Name Description: The entry's name.
--     * Slot: Status Description: How far the entry has got through review.
--     * Slot: CapecAttackPatternCatalog_id Description: Autocreated FK slot
--     * Slot: Members_id Description: The entries the view holds.
--     * Slot: Content_History_id Description: Who wrote and changed the entry.
-- # Class: CapecExternalReference_Author
--     * Slot: CapecExternalReference_Reference_ID Description: Autocreated FK slot
--     * Slot: Author Description: A person or body who wrote the work.
-- # Class: CapecConsequence_Scope
--     * Slot: CapecConsequence_id Description: Autocreated FK slot
--     * Slot: Scope Description: The security properties violated.
-- # Class: CapecConsequence_Impact
--     * Slot: CapecConsequence_id Description: Autocreated FK slot
--     * Slot: Impact Description: What the attack does to the system.
-- # Class: CapecAttackPattern_Prerequisites
--     * Slot: CapecAttackPattern_ID Description: Autocreated FK slot
--     * Slot: Prerequisites Description: Conditions that must hold for the attack to work.
-- # Class: CapecAttackPattern_Resources_Required
--     * Slot: CapecAttackPattern_ID Description: Autocreated FK slot
--     * Slot: Resources_Required Description: What an adversary must have to hand, such as tools or addresses.
-- # Class: CapecAttackPattern_Indicators
--     * Slot: CapecAttackPattern_ID Description: Autocreated FK slot
--     * Slot: Indicators Description: Signs that an attack is near, under way or over.
-- # Class: CapecAttackPattern_Mitigations
--     * Slot: CapecAttackPattern_ID Description: Autocreated FK slot
--     * Slot: Mitigations Description: Ways to prevent the attack or lessen its harm.
-- # Class: CapecAttackPattern_Example_Instances
--     * Slot: CapecAttackPattern_ID Description: Autocreated FK slot
--     * Slot: Example_Instances Description: Concrete examples of the attack.

CREATE TABLE "CapecAttackPatternCatalog" (
	id INTEGER NOT NULL,
	"Name" TEXT NOT NULL,
	"Version" TEXT NOT NULL,
	"Date" DATE NOT NULL,
	PRIMARY KEY (id)
);
CREATE INDEX "ix_CapecAttackPatternCatalog_id" ON "CapecAttackPatternCatalog" (id);

CREATE TABLE "CapecExclusionsMixin" (
	id INTEGER NOT NULL,
	PRIMARY KEY (id)
);
CREATE INDEX "ix_CapecExclusionsMixin_id" ON "CapecExclusionsMixin" (id);

CREATE TABLE "CapecTaxonomyMappedMixin" (
	id INTEGER NOT NULL,
	PRIMARY KEY (id)
);
CREATE INDEX "ix_CapecTaxonomyMappedMixin_id" ON "CapecTaxonomyMappedMixin" (id);

CREATE TABLE "CapecSubmission" (
	id INTEGER NOT NULL,
	"Submission_Name" TEXT,
	"Submission_Organization" TEXT,
	"Submission_Date" DATE,
	"Submission_Comment" TEXT,
	PRIMARY KEY (id)
);
CREATE INDEX "ix_CapecSubmission_id" ON "CapecSubmission" (id);

CREATE TABLE "CapecRelationships" (
	id INTEGER NOT NULL,
	PRIMARY KEY (id)
);
CREATE INDEX "ix_CapecRelationships_id" ON "CapecRelationships" (id);

CREATE TABLE "CapecExternalReference" (
	"Reference_ID" TEXT NOT NULL,
	"Title" TEXT NOT NULL,
	"Edition" TEXT,
	"Publication" TEXT,
	"Publication_Year" TEXT,
	"Publication_Month" TEXT,
	"Publication_Day" TEXT,
	"Publisher" TEXT,
	"URL" TEXT,
	"URL_Date" DATE,
	"CapecAttackPatternCatalog_id" INTEGER,
	PRIMARY KEY ("Reference_ID"),
	FOREIGN KEY("CapecAttackPatternCatalog_id") REFERENCES "CapecAttackPatternCatalog" (id)
);
CREATE INDEX "ix_CapecExternalReference_Reference_ID" ON "CapecExternalReference" ("Reference_ID");

CREATE TABLE "CapecContentHistory" (
	id INTEGER NOT NULL,
	"Submission_id" INTEGER,
	PRIMARY KEY (id),
	FOREIGN KEY("Submission_id") REFERENCES "CapecSubmission" (id)
);
CREATE INDEX "ix_CapecContentHistory_id" ON "CapecContentHistory" (id);

CREATE TABLE "CapecModification" (
	id INTEGER NOT NULL,
	"Modification_Name" TEXT,
	"Modification_Organization" TEXT,
	"Modification_Date" DATE,
	"Modification_Importance" VARCHAR(8),
	"Modification_Comment" TEXT,
	"CapecContentHistory_id" INTEGER,
	PRIMARY KEY (id),
	FOREIGN KEY("CapecContentHistory_id") REFERENCES "CapecContentHistory" (id)
);
CREATE INDEX "ix_CapecModification_id" ON "CapecModification" (id);

CREATE TABLE "CapecContribution" (
	id INTEGER NOT NULL,
	"Type" VARCHAR(8) NOT NULL,
	"Contribution_Name" TEXT,
	"Contribution_Organization" TEXT,
	"Contribution_Date" DATE,
	"Contribution_Comment" TEXT,
	"CapecContentHistory_id" INTEGER,
	PRIMARY KEY (id),
	FOREIGN KEY("CapecContentHistory_id") REFERENCES "CapecContentHistory" (id)
);
CREATE INDEX "ix_CapecContribution_id" ON "CapecContribution" (id);

CREATE TABLE "CapecPreviousEntryName" (
	id INTEGER NOT NULL,
	"Date" DATE NOT NULL,
	"Value" TEXT NOT NULL,
	"CapecContentHistory_id" INTEGER,
	PRIMARY KEY (id),
	FOREIGN KEY("CapecContentHistory_id") REFERENCES "CapecContentHistory" (id)
);
CREATE INDEX "ix_CapecPreviousEntryName_id" ON "CapecPreviousEntryName" (id);

CREATE TABLE "CapecEntry" (
	"ID" TEXT NOT NULL,
	"Name" TEXT NOT NULL,
	"Status" VARCHAR(10) NOT NULL,
	"Content_History_id" INTEGER,
	PRIMARY KEY ("ID"),
	FOREIGN KEY("Content_History_id") REFERENCES "CapecContentHistory" (id)
);
CREATE INDEX "ix_CapecEntry_ID" ON "CapecEntry" ("ID");

CREATE TABLE "CapecAttackPattern" (
	"Abstraction" VARCHAR(8) NOT NULL,
	"Description" TEXT NOT NULL,
	"Extended_Description" TEXT,
	"Likelihood_Of_Attack" VARCHAR(7),
	"Typical_Severity" VARCHAR(9),
	"ID" TEXT NOT NULL,
	"Name" TEXT NOT NULL,
	"Status" VARCHAR(10) NOT NULL,
	"CapecAttackPatternCatalog_id" INTEGER,
	"Content_History_id" INTEGER,
	PRIMARY KEY ("ID"),
	FOREIGN KEY("CapecAttackPatternCatalog_id") REFERENCES "CapecAttackPatternCatalog" (id),
	FOREIGN KEY("Content_History_id") REFERENCES "CapecContentHistory" (id)
);
CREATE INDEX "ix_CapecAttackPattern_ID" ON "CapecAttackPattern" ("ID");

CREATE TABLE "CapecCategory" (
	"Summary" TEXT NOT NULL,
	"ID" TEXT NOT NULL,
	"Name" TEXT NOT NULL,
	"Status" VARCHAR(10) NOT NULL,
	"CapecAttackPatternCatalog_id" INTEGER,
	"Relationships_id" INTEGER,
	"Content_History_id" INTEGER,
	PRIMARY KEY ("ID"),
	FOREIGN KEY("CapecAttackPatternCatalog_id") REFERENCES "CapecAttackPatternCatalog" (id),
	FOREIGN KEY("Relationships_id") REFERENCES "CapecRelationships" (id),
	FOREIGN KEY("Content_History_id") REFERENCES "CapecContentHistory" (id)
);
CREATE INDEX "ix_CapecCategory_ID" ON "CapecCategory" ("ID");

CREATE TABLE "CapecView" (
	"Type" VARCHAR(8) NOT NULL,
	"Objective" TEXT NOT NULL,
	"Filter" TEXT,
	"ID" TEXT NOT NULL,
	"Name" TEXT NOT NULL,
	"Status" VARCHAR(10) NOT NULL,
	"CapecAttackPatternCatalog_id" INTEGER,
	"Members_id" INTEGER,
	"Content_History_id" INTEGER,
	PRIMARY KEY ("ID"),
	FOREIGN KEY("CapecAttackPatternCatalog_id") REFERENCES "CapecAttackPatternCatalog" (id),
	FOREIGN KEY("Members_id") REFERENCES "CapecRelationships" (id),
	FOREIGN KEY("Content_History_id") REFERENCES "CapecContentHistory" (id)
);
CREATE INDEX "ix_CapecView_ID" ON "CapecView" ("ID");

CREATE TABLE "CapecExternalReference_Author" (
	"CapecExternalReference_Reference_ID" TEXT,
	"Author" TEXT,
	PRIMARY KEY ("CapecExternalReference_Reference_ID", "Author"),
	FOREIGN KEY("CapecExternalReference_Reference_ID") REFERENCES "CapecExternalReference" ("Reference_ID")
);
CREATE INDEX "ix_CapecExternalReference_Author_Author" ON "CapecExternalReference_Author" ("Author");
CREATE INDEX "ix_CapecExternalReference_Author_CapecExternalReference_Reference_ID" ON "CapecExternalReference_Author" ("CapecExternalReference_Reference_ID");

CREATE TABLE "CapecReference" (
	id INTEGER NOT NULL,
	"External_Reference_ID" TEXT NOT NULL,
	"Section" TEXT,
	"CapecEntry_ID" TEXT,
	"CapecAttackPattern_ID" TEXT,
	"CapecCategory_ID" TEXT,
	"CapecView_ID" TEXT,
	PRIMARY KEY (id),
	FOREIGN KEY("External_Reference_ID") REFERENCES "CapecExternalReference" ("Reference_ID"),
	FOREIGN KEY("CapecEntry_ID") REFERENCES "CapecEntry" ("ID"),
	FOREIGN KEY("CapecAttackPattern_ID") REFERENCES "CapecAttackPattern" ("ID"),
	FOREIGN KEY("CapecCategory_ID") REFERENCES "CapecCategory" ("ID"),
	FOREIGN KEY("CapecView_ID") REFERENCES "CapecView" ("ID")
);
CREATE INDEX "ix_CapecReference_id" ON "CapecReference" (id);

CREATE TABLE "CapecNote" (
	id INTEGER NOT NULL,
	"Type" VARCHAR(12) NOT NULL,
	"Value" TEXT NOT NULL,
	"CapecEntry_ID" TEXT,
	"CapecAttackPattern_ID" TEXT,
	"CapecCategory_ID" TEXT,
	"CapecView_ID" TEXT,
	PRIMARY KEY (id),
	FOREIGN KEY("CapecEntry_ID") REFERENCES "CapecEntry" ("ID"),
	FOREIGN KEY("CapecAttackPattern_ID") REFERENCES "CapecAttackPattern" ("ID"),
	FOREIGN KEY("CapecCategory_ID") REFERENCES "CapecCategory" ("ID"),
	FOREIGN KEY("CapecView_ID") REFERENCES "CapecView" ("ID")
);
CREATE INDEX "ix_CapecNote_id" ON "CapecNote" (id);

CREATE TABLE "CapecTaxonomyMapping" (
	id INTEGER NOT NULL,
	"Taxonomy_Name" VARCHAR(13) NOT NULL,
	"Entry_ID" TEXT,
	"Entry_Name" TEXT,
	"Mapping_Fit" VARCHAR(19),
	"CapecTaxonomyMappedMixin_id" INTEGER,
	"CapecAttackPattern_ID" TEXT,
	"CapecCategory_ID" TEXT,
	PRIMARY KEY (id),
	FOREIGN KEY("CapecTaxonomyMappedMixin_id") REFERENCES "CapecTaxonomyMappedMixin" (id),
	FOREIGN KEY("CapecAttackPattern_ID") REFERENCES "CapecAttackPattern" ("ID"),
	FOREIGN KEY("CapecCategory_ID") REFERENCES "CapecCategory" ("ID")
);
CREATE INDEX "ix_CapecTaxonomyMapping_id" ON "CapecTaxonomyMapping" (id);

CREATE TABLE "CapecAlternateTerm" (
	id INTEGER NOT NULL,
	"Term" TEXT NOT NULL,
	"Description" TEXT,
	"CapecAttackPattern_ID" TEXT,
	PRIMARY KEY (id),
	FOREIGN KEY("CapecAttackPattern_ID") REFERENCES "CapecAttackPattern" ("ID")
);
CREATE INDEX "ix_CapecAlternateTerm_id" ON "CapecAlternateTerm" (id);

CREATE TABLE "CapecRelatedAttackPattern" (
	id INTEGER NOT NULL,
	"Nature" VARCHAR(10) NOT NULL,
	"CAPEC_ID" TEXT NOT NULL,
	"CapecAttackPattern_ID" TEXT,
	PRIMARY KEY (id),
	FOREIGN KEY("CAPEC_ID") REFERENCES "CapecAttackPattern" ("ID"),
	FOREIGN KEY("CapecAttackPattern_ID") REFERENCES "CapecAttackPattern" ("ID")
);
CREATE INDEX "ix_CapecRelatedAttackPattern_id" ON "CapecRelatedAttackPattern" (id);

CREATE TABLE "CapecAttackStep" (
	id INTEGER NOT NULL,
	"Step" INTEGER NOT NULL,
	"Phase" VARCHAR(10) NOT NULL,
	"Description" TEXT NOT NULL,
	"CapecAttackPattern_ID" TEXT,
	PRIMARY KEY (id),
	FOREIGN KEY("CapecAttackPattern_ID") REFERENCES "CapecAttackPattern" ("ID")
);
CREATE INDEX "ix_CapecAttackStep_id" ON "CapecAttackStep" (id);

CREATE TABLE "CapecSkill" (
	id INTEGER NOT NULL,
	"Level" VARCHAR(7) NOT NULL,
	"Value" TEXT NOT NULL,
	"CapecAttackPattern_ID" TEXT,
	PRIMARY KEY (id),
	FOREIGN KEY("CapecAttackPattern_ID") REFERENCES "CapecAttackPattern" ("ID")
);
CREATE INDEX "ix_CapecSkill_id" ON "CapecSkill" (id);

CREATE TABLE "CapecConsequence" (
	id INTEGER NOT NULL,
	"Consequence_ID" TEXT,
	"Likelihood" VARCHAR(7),
	"Note" TEXT,
	"CapecAttackPattern_ID" TEXT,
	PRIMARY KEY (id),
	FOREIGN KEY("CapecAttackPattern_ID") REFERENCES "CapecAttackPattern" ("ID")
);
CREATE INDEX "ix_CapecConsequence_id" ON "CapecConsequence" (id);

CREATE TABLE "CapecRelatedWeakness" (
	id INTEGER NOT NULL,
	"CWE_ID" TEXT NOT NULL,
	"CapecAttackPattern_ID" TEXT,
	PRIMARY KEY (id),
	FOREIGN KEY("CapecAttackPattern_ID") REFERENCES "CapecAttackPattern" ("ID")
);
CREATE INDEX "ix_CapecRelatedWeakness_id" ON "CapecRelatedWeakness" (id);

CREATE TABLE "CapecMemberOf" (
	id INTEGER NOT NULL,
	"CAPEC_ID" TEXT NOT NULL,
	"CapecRelationships_id" INTEGER,
	PRIMARY KEY (id),
	FOREIGN KEY("CAPEC_ID") REFERENCES "CapecEntry" ("ID"),
	FOREIGN KEY("CapecRelationships_id") REFERENCES "CapecRelationships" (id)
);
CREATE INDEX "ix_CapecMemberOf_id" ON "CapecMemberOf" (id);

CREATE TABLE "CapecHasMember" (
	id INTEGER NOT NULL,
	"CAPEC_ID" TEXT NOT NULL,
	"CapecRelationships_id" INTEGER,
	PRIMARY KEY (id),
	FOREIGN KEY("CAPEC_ID") REFERENCES "CapecEntry" ("ID"),
	FOREIGN KEY("CapecRelationships_id") REFERENCES "CapecRelationships" (id)
);
CREATE INDEX "ix_CapecHasMember_id" ON "CapecHasMember" (id);

CREATE TABLE "CapecStakeholder" (
	id INTEGER NOT NULL,
	"Type" VARCHAR(21) NOT NULL,
	"Description" TEXT NOT NULL,
	"CapecView_ID" TEXT,
	PRIMARY KEY (id),
	FOREIGN KEY("CapecView_ID") REFERENCES "CapecView" ("ID")
);
CREATE INDEX "ix_CapecStakeholder_id" ON "CapecStakeholder" (id);

CREATE TABLE "CapecAttackPattern_Prerequisites" (
	"CapecAttackPattern_ID" TEXT,
	"Prerequisites" TEXT,
	PRIMARY KEY ("CapecAttackPattern_ID", "Prerequisites"),
	FOREIGN KEY("CapecAttackPattern_ID") REFERENCES "CapecAttackPattern" ("ID")
);
CREATE INDEX "ix_CapecAttackPattern_Prerequisites_CapecAttackPattern_ID" ON "CapecAttackPattern_Prerequisites" ("CapecAttackPattern_ID");
CREATE INDEX "ix_CapecAttackPattern_Prerequisites_Prerequisites" ON "CapecAttackPattern_Prerequisites" ("Prerequisites");

CREATE TABLE "CapecAttackPattern_Resources_Required" (
	"CapecAttackPattern_ID" TEXT,
	"Resources_Required" TEXT,
	PRIMARY KEY ("CapecAttackPattern_ID", "Resources_Required"),
	FOREIGN KEY("CapecAttackPattern_ID") REFERENCES "CapecAttackPattern" ("ID")
);
CREATE INDEX "ix_CapecAttackPattern_Resources_Required_Resources_Required" ON "CapecAttackPattern_Resources_Required" ("Resources_Required");
CREATE INDEX "ix_CapecAttackPattern_Resources_Required_CapecAttackPattern_ID" ON "CapecAttackPattern_Resources_Required" ("CapecAttackPattern_ID");

CREATE TABLE "CapecAttackPattern_Indicators" (
	"CapecAttackPattern_ID" TEXT,
	"Indicators" TEXT,
	PRIMARY KEY ("CapecAttackPattern_ID", "Indicators"),
	FOREIGN KEY("CapecAttackPattern_ID") REFERENCES "CapecAttackPattern" ("ID")
);
CREATE INDEX "ix_CapecAttackPattern_Indicators_CapecAttackPattern_ID" ON "CapecAttackPattern_Indicators" ("CapecAttackPattern_ID");
CREATE INDEX "ix_CapecAttackPattern_Indicators_Indicators" ON "CapecAttackPattern_Indicators" ("Indicators");

CREATE TABLE "CapecAttackPattern_Mitigations" (
	"CapecAttackPattern_ID" TEXT,
	"Mitigations" TEXT,
	PRIMARY KEY ("CapecAttackPattern_ID", "Mitigations"),
	FOREIGN KEY("CapecAttackPattern_ID") REFERENCES "CapecAttackPattern" ("ID")
);
CREATE INDEX "ix_CapecAttackPattern_Mitigations_CapecAttackPattern_ID" ON "CapecAttackPattern_Mitigations" ("CapecAttackPattern_ID");
CREATE INDEX "ix_CapecAttackPattern_Mitigations_Mitigations" ON "CapecAttackPattern_Mitigations" ("Mitigations");

CREATE TABLE "CapecAttackPattern_Example_Instances" (
	"CapecAttackPattern_ID" TEXT,
	"Example_Instances" TEXT,
	PRIMARY KEY ("CapecAttackPattern_ID", "Example_Instances"),
	FOREIGN KEY("CapecAttackPattern_ID") REFERENCES "CapecAttackPattern" ("ID")
);
CREATE INDEX "ix_CapecAttackPattern_Example_Instances_CapecAttackPattern_ID" ON "CapecAttackPattern_Example_Instances" ("CapecAttackPattern_ID");
CREATE INDEX "ix_CapecAttackPattern_Example_Instances_Example_Instances" ON "CapecAttackPattern_Example_Instances" ("Example_Instances");

CREATE TABLE "CapecExcludeRelated" (
	id INTEGER NOT NULL,
	"Exclude_ID" TEXT NOT NULL,
	"CapecExclusionsMixin_id" INTEGER,
	"CapecRelatedAttackPattern_id" INTEGER,
	"CapecMemberOf_id" INTEGER,
	"CapecHasMember_id" INTEGER,
	PRIMARY KEY (id),
	FOREIGN KEY("Exclude_ID") REFERENCES "CapecEntry" ("ID"),
	FOREIGN KEY("CapecExclusionsMixin_id") REFERENCES "CapecExclusionsMixin" (id),
	FOREIGN KEY("CapecRelatedAttackPattern_id") REFERENCES "CapecRelatedAttackPattern" (id),
	FOREIGN KEY("CapecMemberOf_id") REFERENCES "CapecMemberOf" (id),
	FOREIGN KEY("CapecHasMember_id") REFERENCES "CapecHasMember" (id)
);
CREATE INDEX "ix_CapecExcludeRelated_id" ON "CapecExcludeRelated" (id);

CREATE TABLE "CapecTechnique" (
	id INTEGER NOT NULL,
	"CAPEC_ID" TEXT,
	"Value" TEXT NOT NULL,
	"CapecAttackStep_id" INTEGER,
	PRIMARY KEY (id),
	FOREIGN KEY("CAPEC_ID") REFERENCES "CapecEntry" ("ID"),
	FOREIGN KEY("CapecAttackStep_id") REFERENCES "CapecAttackStep" (id)
);
CREATE INDEX "ix_CapecTechnique_id" ON "CapecTechnique" (id);

CREATE TABLE "CapecConsequence_Scope" (
	"CapecConsequence_id" INTEGER,
	"Scope" VARCHAR(15) NOT NULL,
	PRIMARY KEY ("CapecConsequence_id", "Scope"),
	FOREIGN KEY("CapecConsequence_id") REFERENCES "CapecConsequence" (id)
);
CREATE INDEX "ix_CapecConsequence_Scope_Scope" ON "CapecConsequence_Scope" ("Scope");
CREATE INDEX "ix_CapecConsequence_Scope_CapecConsequence_id" ON "CapecConsequence_Scope" ("CapecConsequence_id");

CREATE TABLE "CapecConsequence_Impact" (
	"CapecConsequence_id" INTEGER,
	"Impact" VARCHAR(29),
	PRIMARY KEY ("CapecConsequence_id", "Impact"),
	FOREIGN KEY("CapecConsequence_id") REFERENCES "CapecConsequence" (id)
);
CREATE INDEX "ix_CapecConsequence_Impact_Impact" ON "CapecConsequence_Impact" ("Impact");
CREATE INDEX "ix_CapecConsequence_Impact_CapecConsequence_id" ON "CapecConsequence_Impact" ("CapecConsequence_id");
