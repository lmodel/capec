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
  One way of carrying out a step of an attack.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class CapecTechnique  {

  private CapecEntry cAPECID;
  private String value;


}