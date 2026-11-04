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
  The record of who wrote and changed an entry.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class CapecContentHistory  {

  private CapecSubmission submission;
  private List<CapecModification> modification;
  private List<CapecContribution> contribution;
  private List<CapecPreviousEntryName> previousEntryName;


}