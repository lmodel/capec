package None;

/* metamodel_version: 1.7.0 */
import java.util.List;
import lombok.*;

/**
  A container for relationships associated with a category or view, showing
Member_Of relationships with views or categories and Has_Member relationships
with attack patterns or categories.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class Relationships  {

  private List<MemberOf> memberOf;
  private List<HasMember> hasMember;

}