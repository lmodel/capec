package None;

/* metamodel_version: 1.7.0 */
import java.util.List;
import lombok.*;

/**
  Another name or term used to describe an attack pattern. Provides context for the alternate term by which the attack pattern may be known.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class AlternateTerm  {

  private String description;
  private String term;

}