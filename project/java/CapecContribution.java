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
  Help given to an entry by someone other than its submitter.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class CapecContribution  {

  private String type;
  private String contributionName;
  private String contributionOrganization;
  private LocalDate contributionDate;
  private String contributionComment;


}