package None;

/* metamodel_version: 1.7.0 */
import java.util.List;
import lombok.*;

/**
  An individual consequence associated with an attack pattern, specifying which
security properties are violated, the technical impact that arises if an adversary
succeeds, the likelihood of this specific consequence occurring, and any additional
commentary.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class Consequence  {

  private String consequenceId;
  private List<String> scope;
  private List<String> impact;
  private String likelihood;
  private String note;

}