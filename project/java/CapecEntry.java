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
  Anything in the catalogue with a CAPEC number, whether an attack pattern, a category or a view.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public abstract class CapecEntry  {

  private String iD;
  private String name;
  private String status;
  private List<CapecReference> references;
  private List<CapecNote> notes;
  private CapecContentHistory contentHistory;


}