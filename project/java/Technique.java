package None;

/* metamodel_version: 1.7.0 */
import java.util.List;
import lombok.*;

/**
  A specific technique used by an adversary during an attack step. Extends the structured text description with an optional reference to a related CAPEC entry.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class Technique  {

  private String capecId;
  private String description;

}