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
  One thing that can happen if an attack succeeds.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class CapecConsequence  {

  private String consequenceID;
  private List<String> scope;
  private List<String> impact;
  private String likelihood;
  private String note;


}