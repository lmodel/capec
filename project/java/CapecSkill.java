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
  A skill or piece of knowledge an adversary needs.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class CapecSkill  {

  private String level;
  private String value;


}