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
  The field of any relation that can leave out some ancestors.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class CapecExclusionsMixin  {

  private List<CapecExcludeRelated> excludeRelated;


}