// The site's values and options, in one place. scripts/config.mjs reads this
// file, fills in every option left out, settles each "auto" against the
// repository and checks the required values. `node scripts/config.mjs`
// prints the result. Nothing here runs code, so the pages that show the
// title import it too.
//
// The first five values are required. The rest are optional: leave one out,
// or set it to "auto", and the site shows that part of the repository when
// the repository has it. Set it to null to leave that part out.

// The repository, as owner/name, and the site's address: the owner's GitHub
// Pages domain and the path under it. A user site (the <owner>.github.io
// repository) or a custom domain sets BASE to "".
export const REPO = "lmodel/capec";
export const SITE = "https://lmodel.github.io";
export const BASE = "/capec";

// The site's title, in the header and on every social card, and its
// description, for search engines and as the home page's tagline when
// HOME.tagline is not set.
export const TITLE = "capec";
export const DESCRIPTION = "Common Attack Pattern Enumeration and Classification (CAPEC) 3.9 (LinkML)";

// The branch an "Edit page" link opens.
export const BRANCH = "main";

// A custom domain, which the sync writes to public/CNAME, or null for a
// Pages address. The site leaves the domain's DNS to the repository.
export const CUSTOM_DOMAIN = null;

// The logo, as paths from the repository root: a light version, a dark one
// (the light one again when left out) and a favicon (the light logo when it
// is an SVG, else the site's own ladder mark). "auto" takes the Knowledge
// Trust Ladder logo: a knowledge-trust-ladder-logo.svg the repository
// already has, or else the copy in src/assets/. A single path is the light
// version alone. null shows the title as text.
//   export const LOGO = { light: ".assets/logo.svg", dark: ".assets/logo-dark.svg" };
export const LOGO = "auto";

// The folder of figures the README and the docs pages show, served under
// /assets/. "auto" takes .assets/ when there is one.
export const ASSETS = "auto";

// The docs pages: a folder, the sidebar groups its pages sit in (each page
// named by its path under the folder, without .md), and the paths under the
// folder that are not pages of the site, each a file or a folder. With no
// groups, every page sits in one Guides group, by title, with the folder's
// index.md first as its Overview. With groups, the sync stops with an error
// when a group names a missing page or a page has no group, so a new page
// cannot go missing from the sidebar. "auto" takes docs/ when there is one.
// null shows no docs pages.
//   export const DOCS = { dir: "docs", groups: [{ label: "Guides", pages: ["install", "usage"] }], exclude: ["templates-linkml"] };
export const DOCS = { dir: "docs", exclude: ["templates-linkml"] };

// Old addresses under BASE, each redirected to a page of the site, such as
// the addresses a retired mkdocs site gave its pages and a w3id rule still
// names. An entry whose key and value both end in /[...slug] stands for one
// redirect per schema page.
//   export const REDIRECTS = { "/elements": "/schema/", "/elements/[...slug]": "/schema/[...slug]", "/about": "/docs/about/" };
export const REDIRECTS = {
  "/about": "/docs/about/",
  "/elements": "/schema/",
  // The retired schema's element addresses, each to its successor. A name that
  // stayed the same is covered by the /elements/[...slug] entry.
  "/elements/abstraction": "/schema/Abstraction/",
  "/elements/AbstractionEnum": "/schema/CapecAbstraction/",
  "/elements/alternate_terms": "/schema/Alternate_Terms/",
  "/elements/AlternateTerm": "/schema/CapecAlternateTerm/",
  "/elements/attack_patterns": "/schema/Attack_Patterns/",
  "/elements/AttackPattern": "/schema/CapecAttackPattern/",
  "/elements/AttackPatternCatalog": "/schema/CapecAttackPatternCatalog/",
  "/elements/AttackStep": "/schema/CapecAttackStep/",
  "/elements/AttackStepPhaseEnum": "/schema/CapecAttackStepPhase/",
  "/elements/audience": "/schema/Audience/",
  "/elements/authors": "/schema/Author/",
  "/elements/capec_id": "/schema/CAPEC_ID/",
  "/elements/categories": "/schema/Categories/",
  "/elements/Category": "/schema/CapecCategory/",
  "/elements/Consequence": "/schema/CapecConsequence/",
  "/elements/consequence_id": "/schema/Consequence_ID/",
  "/elements/consequences": "/schema/Consequences/",
  "/elements/content": "/schema/Value/",
  "/elements/content_history": "/schema/Content_History/",
  "/elements/ContentHistory": "/schema/CapecContentHistory/",
  "/elements/Contribution": "/schema/CapecContribution/",
  "/elements/contribution_comment": "/schema/Contribution_Comment/",
  "/elements/contribution_date": "/schema/Contribution_Date/",
  "/elements/contribution_name": "/schema/Contribution_Name/",
  "/elements/contribution_organization": "/schema/Contribution_Organization/",
  "/elements/contributions": "/schema/Contribution/",
  "/elements/ContributionTypeEnum": "/schema/CapecContributionType/",
  "/elements/cwe_id": "/schema/CWE_ID/",
  "/elements/description": "/schema/Description/",
  "/elements/edition": "/schema/Edition/",
  "/elements/entry_date": "/schema/CapecAttackPatternCatalog/",
  "/elements/entry_id": "/schema/Entry_ID/",
  "/elements/entry_name": "/schema/Entry_Name/",
  "/elements/example_instances": "/schema/Example_Instances/",
  "/elements/exclude_id": "/schema/Exclude_ID/",
  "/elements/exclude_related": "/schema/Exclude_Related/",
  "/elements/ExcludeRelated": "/schema/CapecExcludeRelated/",
  "/elements/execution_flow": "/schema/Execution_Flow/",
  "/elements/extended_description": "/schema/Extended_Description/",
  "/elements/external_reference_id": "/schema/External_Reference_ID/",
  "/elements/external_references": "/schema/External_References/",
  "/elements/ExternalReference": "/schema/CapecExternalReference/",
  "/elements/filter": "/schema/Filter/",
  "/elements/has_member": "/schema/Has_Member/",
  "/elements/HasMember": "/schema/CapecHasMember/",
  "/elements/id": "/schema/ID/",
  "/elements/impact": "/schema/Impact/",
  "/elements/ImportanceEnum": "/schema/CapecImportance/",
  "/elements/indicators": "/schema/Indicators/",
  "/elements/level": "/schema/Level/",
  "/elements/likelihood": "/schema/Likelihood/",
  "/elements/likelihood_of_attack": "/schema/Likelihood_Of_Attack/",
  "/elements/LikelihoodEnum": "/schema/CapecLikelihood/",
  "/elements/mapping_fit": "/schema/Mapping_Fit/",
  "/elements/member_of": "/schema/Member_Of/",
  "/elements/MemberOf": "/schema/CapecMemberOf/",
  "/elements/members": "/schema/Members/",
  "/elements/mitigations": "/schema/Mitigations/",
  "/elements/Modification": "/schema/CapecModification/",
  "/elements/modification_comment": "/schema/Modification_Comment/",
  "/elements/modification_date": "/schema/Modification_Date/",
  "/elements/modification_importance": "/schema/Modification_Importance/",
  "/elements/modification_name": "/schema/Modification_Name/",
  "/elements/modification_organization": "/schema/Modification_Organization/",
  "/elements/modifications": "/schema/Modification/",
  "/elements/name": "/schema/Name/",
  "/elements/nature": "/schema/Nature/",
  "/elements/Note": "/schema/CapecNote/",
  "/elements/note": "/schema/Note/",
  "/elements/notes": "/schema/Notes/",
  "/elements/NoteTypeEnum": "/schema/CapecNoteType/",
  "/elements/objective": "/schema/Objective/",
  "/elements/phase": "/schema/Phase/",
  "/elements/prerequisites": "/schema/Prerequisites/",
  "/elements/previous_entry_names": "/schema/Previous_Entry_Name/",
  "/elements/PreviousEntryName": "/schema/CapecPreviousEntryName/",
  "/elements/publication": "/schema/Publication/",
  "/elements/publication_day": "/schema/Publication_Day/",
  "/elements/publication_month": "/schema/Publication_Month/",
  "/elements/publication_year": "/schema/Publication_Year/",
  "/elements/publisher": "/schema/Publisher/",
  "/elements/Reference": "/schema/CapecReference/",
  "/elements/reference_id": "/schema/Reference_ID/",
  "/elements/references": "/schema/References/",
  "/elements/related_attack_patterns": "/schema/Related_Attack_Patterns/",
  "/elements/related_weaknesses": "/schema/Related_Weaknesses/",
  "/elements/RelatedAttackPattern": "/schema/CapecRelatedAttackPattern/",
  "/elements/RelatedNatureEnum": "/schema/CapecRelatedNature/",
  "/elements/RelatedWeakness": "/schema/CapecRelatedWeakness/",
  "/elements/Relationships": "/schema/CapecRelationships/",
  "/elements/relationships": "/schema/Relationships/",
  "/elements/resources_required": "/schema/Resources_Required/",
  "/elements/scope": "/schema/Scope/",
  "/elements/ScopeEnum": "/schema/CapecScope/",
  "/elements/section": "/schema/Section/",
  "/elements/SeverityEnum": "/schema/CapecSeverity/",
  "/elements/Skill": "/schema/CapecSkill/",
  "/elements/SkillLevelEnum": "/schema/CapecSkillLevel/",
  "/elements/skills_required": "/schema/Skills_Required/",
  "/elements/Stakeholder": "/schema/CapecStakeholder/",
  "/elements/StakeholderEnum": "/schema/CapecStakeholderType/",
  "/elements/status": "/schema/Status/",
  "/elements/StatusEnum": "/schema/CapecStatus/",
  "/elements/step": "/schema/Step/",
  "/elements/StructuredText": "/schema/CapecStructuredText/",
  "/elements/Submission": "/schema/CapecSubmission/",
  "/elements/submission": "/schema/Submission/",
  "/elements/submission_comment": "/schema/Submission_Comment/",
  "/elements/submission_date": "/schema/Submission_Date/",
  "/elements/submission_name": "/schema/Submission_Name/",
  "/elements/submission_organization": "/schema/Submission_Organization/",
  "/elements/summary": "/schema/Summary/",
  "/elements/taxonomy_mappings": "/schema/Taxonomy_Mappings/",
  "/elements/taxonomy_name": "/schema/Taxonomy_Name/",
  "/elements/TaxonomyMapping": "/schema/CapecTaxonomyMapping/",
  "/elements/TaxonomyMappingFitEnum": "/schema/CapecTaxonomyMappingFit/",
  "/elements/TaxonomyNameEnum": "/schema/CapecTaxonomyName/",
  "/elements/TechnicalImpactEnum": "/schema/CapecTechnicalImpact/",
  "/elements/Technique": "/schema/CapecTechnique/",
  "/elements/techniques": "/schema/Technique/",
  "/elements/term": "/schema/Term/",
  "/elements/title": "/schema/Title/",
  "/elements/type": "/schema/Type/",
  "/elements/typical_severity": "/schema/Typical_Severity/",
  "/elements/url": "/schema/URL/",
  "/elements/url_date": "/schema/URL_Date/",
  "/elements/version": "/schema/Version/",
  "/elements/View": "/schema/CapecView/",
  "/elements/views": "/schema/Views/",
  "/elements/ViewTypeEnum": "/schema/CapecViewType/",
  "/elements/[...slug]": "/schema/[...slug]",
};

// A Keep a Changelog file, read as a page per release. "auto" takes
// CHANGELOG.md when it holds a released version.
export const CHANGELOG = "auto";

// The tag a release carries, with {version} for its number. A release page
// links the repository, the docs and the bundle at that tag, and the release
// itself, when git has the tag. A repository whose tags carry no "v" sets
// "{version}". null links nothing.
export const RELEASE_TAG = "v{version}";

// Pages from files outside the docs folder, each at /<slug>/, listed in the
// Guide sidebar after Home under its label. An entry's `retells` names the
// file whose page it retells, and `level` the words for its reading level
// (the label when left out): both pages then offer each other under their
// titles.
//   export const PAGES = [{ slug: "simple", source: "docs/overview.en-simple.md", label: "In short", retells: "docs/overview.md" }];
export const PAGES = [];

// The LinkML schema's pages, which gen-doc writes, under a Schema topic: a
// folder, and the command that writes it, which the sync runs when the
// folder is missing. "auto" takes the first of the root, a linkmo project
// and .linkml/ whose justfile has a gen-doc recipe, else the sidecar's
// domain schema. null shows no schema.
//   export const SCHEMA = { dir: "docs/elements", build: "just gen-doc" };
export const SCHEMA = "auto";

// The data: a folder of SQLite databases and their Datasette metadata, served
// under /browse/ with a page that opens each in Datasette Lite, and the
// command that writes it. The databases go on the public site, so it is null
// until set. "auto" takes a linkmo project's browse/ folder.
//   export const BROWSE = { dir: "browse", build: "just build-browse" };
export const BROWSE = null;

// The workspace of a domain host, which the knowledge-federation workflow
// serves at workspace/ under the site, and which the graph page offers to
// draw beside the bundle's own graph. "auto" offers it when the repository
// has that workflow; true offers it always, and null never.
export const WORKSPACE = "auto";

// The home page: its source, from the file's `# ` title down ("auto" takes
// the README when it has one, else the bundle's own introduction); the
// tagline under the title (a string, { boldLineOf: <file> } for the first
// line of that file that is bold throughout, or DESCRIPTION when null); and
// the buttons, with site-relative links (Browse the bundle, Architecture when
// the docs have an architecture page, Schema when the site shows the schema,
// Bundle health and Knowledge graph when null).
export const HOME = { source: "auto", tagline: null, actions: null };
