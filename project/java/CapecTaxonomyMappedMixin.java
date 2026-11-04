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
  The field of an entry that can map to other taxonomies.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class CapecTaxonomyMappedMixin  {

  private List<CapecTaxonomyMapping> taxonomyMappings;


}