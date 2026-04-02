package None;

/* metamodel_version: 1.7.0 */
import java.util.List;
import lombok.*;

/**
  A reference to another attack pattern that provides insight to similar items at
higher or lower levels of abstraction, or items that are part of a chaining or
peer relationship. Special cases may require Exclude_Related elements to capture
ancestor IDs for which this relationship is not applicable.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class RelatedAttackPattern  {

  private int capecId;
  private List<ExcludeRelated> excludeRelated;
  private String nature;

}