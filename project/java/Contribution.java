package None;

/* metamodel_version: 1.7.0 */
import java.util.List;
import lombok.*;

/**
  A record of a contribution made to a CAPEC entry, identifying the contributor,
their organization, the date of contribution, the type of contribution (Content
or Feedback), and any related comments.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class Contribution  {

  private String type;
  private String contributionName;
  private String contributionOrganization;
  private LocalDate contributionDate;
  private String contributionComment;

}