package None;

/* metamodel_version: 1.7.0 */
import java.util.List;
import lombok.*;

/**
  Represents a Has_Member relationship indicating that the parent category or view
contains the specified attack pattern or category as a member.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class HasMember  {

  private int capecId;
  private List<ExcludeRelated> excludeRelated;

}