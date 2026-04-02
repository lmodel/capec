package None;

/* metamodel_version: 1.7.0 */
import java.util.List;
import lombok.*;

/**
  A category in CAPEC is a collection of attack patterns based on some common
characteristic. More specifically, it is an aggregation of attack patterns based on
effect/intent (as opposed to actions or mechanisms, which would be a meta attack
pattern). An aggregation based on effect/intent is not an actionable attack and as
such is not a pattern of attack behavior. Rather, it is a grouping of patterns based
on some common criteria.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class Category  {

  private int id;
  private String name;
  private String status;
  private List<Note> notes;
  private ContentHistory contentHistory;
  private List<Reference> references;
  private List<TaxonomyMapping> taxonomyMappings;
  private String summary;
  private Relationships relationships;

}