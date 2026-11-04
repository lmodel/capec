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
  Which entries a category or a view holds, and which it belongs to.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class CapecRelationships  {

  private List<CapecMemberOf> memberOf;
  private List<CapecHasMember> hasMember;


}