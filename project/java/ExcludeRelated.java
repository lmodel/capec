package None;

/* metamodel_version: 1.7.0 */
import java.util.List;
import lombok.*;

/**
  Captures the CAPEC identifier of an ancestor for which a given relationship is
not applicable. Used in special cases within RelatedAttackPattern and relationship
entries.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class ExcludeRelated  {

  private int excludeId;

}