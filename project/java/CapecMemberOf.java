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
  A statement that an entry belongs to a view or a category.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class CapecMemberOf  {

  private CapecEntry cAPECID;
  private List<CapecExcludeRelated> excludeRelated;


}