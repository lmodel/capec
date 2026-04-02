package None;

/* metamodel_version: 1.7.0 */
import java.util.List;
import lombok.*;

/**
  An attack pattern is an abstraction mechanism for helping describe how an attack is
executed. Each pattern defines a challenge that an attacker may face, provides a
description of the common technique(s) used to meet the challenge, and presents
recommended methods for mitigating an actual attack. Attack patterns help categorize
attacks in a meaningful way in an effort to provide a coherent way of teaching
designers and developers how their systems may be attacked and how they can effectively
defend them.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class AttackPattern  {

  private int id;
  private String name;
  private String status;
  private String description;
  private List<Note> notes;
  private ContentHistory contentHistory;
  private List<Reference> references;
  private List<TaxonomyMapping> taxonomyMappings;
  private String abstraction;
  private String extendedDescription;
  private List<AlternateTerm> alternateTerms;
  private String likelihoodOfAttack;
  private String typicalSeverity;
  private List<RelatedAttackPattern> relatedAttackPatterns;
  private List<AttackStep> executionFlow;
  private List<String> prerequisites;
  private List<Skill> skillsRequired;
  private List<String> resourcesRequired;
  private List<String> indicators;
  private List<Consequence> consequences;
  private List<String> mitigations;
  private List<String> exampleInstances;
  private List<Integer> relatedWeaknesses;

}