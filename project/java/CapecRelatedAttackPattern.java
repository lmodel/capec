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
  A relation from one attack pattern to another.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class CapecRelatedAttackPattern  {

  private String nature;
  private CapecAttackPattern cAPECID;
  private List<CapecExcludeRelated> excludeRelated;


}