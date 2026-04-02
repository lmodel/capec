package None;

/* metamodel_version: 1.7.0 */
import java.util.List;
import lombok.*;

/**
  A mapping from a CAPEC entry (AttackPattern or Category) to an equivalent or related
entry in a different security taxonomy. Identifies the external taxonomy, the ID and
name of the external entry, and how closely the CAPEC entry aligns with it.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class TaxonomyMapping  {

  private String taxonomyName;
  private String entryId;
  private String entryName;
  private String mappingFit;

}