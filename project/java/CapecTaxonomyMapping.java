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
  A link from an entry to the matching entry of another taxonomy.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class CapecTaxonomyMapping  {

  private String taxonomyName;
  private String entryID;
  private String entryName;
  private String mappingFit;


}