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
  A weakness in the Common Weakness Enumeration that can make an attack possible.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class CapecRelatedWeakness  {

  private String cWEID;


}