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
  One citation by an entry of an external reference.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class CapecReference  {

  private CapecExternalReference externalReferenceID;
  private String section;


}