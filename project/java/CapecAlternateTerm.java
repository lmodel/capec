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
  Another name by which an attack pattern is known.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class CapecAlternateTerm  {

  private String term;
  private String description;


}