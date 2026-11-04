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
  A group of attack patterns that share an effect or intent, and not itself a pattern of attack.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class CapecCategory extends CapecEntry {

  private String summary;
  private CapecRelationships relationships;
  private List<CapecTaxonomyMapping> taxonomyMappings;


}