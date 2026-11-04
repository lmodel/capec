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
  An ancestor under which a relation does not hold.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class CapecExcludeRelated  {

  private CapecEntry excludeID;


}