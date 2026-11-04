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
  One release of the whole catalogue, with its entries and the references they share.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class CapecAttackPatternCatalog  {

  private String name;
  private String version;
  private LocalDate date;
  private List<CapecAttackPattern> attackPatterns;
  private List<CapecCategory> categories;
  private List<CapecView> views;
  private List<CapecExternalReference> externalReferences;


}