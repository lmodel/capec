package example;

/* metamodel_version: 1.12.0 */
/* version: 3.9 */
import java.net.URI;
import java.time.LocalDate;
import java.time.LocalTime;
import java.time.ZonedDateTime;
import java.util.List;
import lombok.*;

/**
  A catalogued way that adversaries go about an attack, with what it takes and how to resist it.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class CapecAttackPattern extends CapecEntry {

  private String abstraction;
  private String description;
  private String extendedDescription;
  private List<CapecAlternateTerm> alternateTerms;
  private String likelihoodOfAttack;
  private String typicalSeverity;
  private List<CapecRelatedAttackPattern> relatedAttackPatterns;
  private List<CapecAttackStep> executionFlow;
  private List<String> prerequisites;
  private List<CapecSkill> skillsRequired;
  private List<String> resourcesRequired;
  private List<String> indicators;
  private List<CapecConsequence> consequences;
  private List<String> mitigations;
  private List<String> exampleInstances;
  private List<CapecRelatedWeakness> relatedWeaknesses;
  private List<CapecTaxonomyMapping> taxonomyMappings;


}