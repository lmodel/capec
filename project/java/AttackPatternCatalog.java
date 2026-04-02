package None;

/* metamodel_version: 1.7.0 */
import java.util.List;
import lombok.*;

/**
  The root element used to hold an enumerated catalog of common attack patterns.
Each catalog can be organized by optional Views and Categories. The catalog also
contains a list of all External_References that may be shared throughout the
individual attack patterns. The required Name and Version attributes are used to
uniquely identify the catalog. The required Date attribute identifies the date when
this catalog was created or last updated.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class AttackPatternCatalog  {

  private String name;
  private String version;
  private LocalDate entryDate;
  private List<AttackPattern> attackPatterns;
  private List<Category> categories;
  private List<View> views;
  private List<ExternalReference> externalReferences;

}