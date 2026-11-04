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
  A remark on an entry that no other field can hold.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class CapecNote  {

  private String type;
  private String value;


}