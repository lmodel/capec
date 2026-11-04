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
  A statement that a view or a category holds an entry.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class CapecHasMember  {

  private CapecEntry cAPECID;
  private List<CapecExcludeRelated> excludeRelated;


}