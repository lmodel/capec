package None;

/* metamodel_version: 1.7.0 */
import java.util.List;
import lombok.*;

/**
  Information about the original submission of a CAPEC entry, identifying the
submitter, their organization, the date of submission, and any related comments.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class Submission  {

  private String submissionName;
  private String submissionOrganization;
  private LocalDate submissionDate;
  private String submissionComment;

}