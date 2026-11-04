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
  One step of the way an adversary typically carries out an attack.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class CapecAttackStep  {

  private int step;
  private String phase;
  private String description;
  private List<CapecTechnique> technique;


}