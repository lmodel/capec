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
  A name an entry used to carry.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class CapecPreviousEntryName  {

  private LocalDate date;
  private String value;


}