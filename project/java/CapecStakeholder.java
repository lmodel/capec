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
  One kind of person a view is meant for, and what they would get from it.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class CapecStakeholder  {

  private String type;
  private String description;


}