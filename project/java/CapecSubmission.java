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
  Who first put an entry forward, and when.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class CapecSubmission  {

  private String submissionName;
  private String submissionOrganization;
  private LocalDate submissionDate;
  private String submissionComment;


}