package None;

/* metamodel_version: 1.7.0 */
import java.util.List;
import lombok.*;

/**
  Represents a Member_Of relationship indicating that the parent category or view
is a member of the specified view or parent category.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class MemberOf  {

  private int capecId;
  private List<ExcludeRelated> excludeRelated;

}