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
  One later edit to an entry.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class CapecModification  {

  private String modificationName;
  private String modificationOrganization;
  private LocalDate modificationDate;
  private String modificationImportance;
  private String modificationComment;


}