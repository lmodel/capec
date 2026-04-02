package None;

/* metamodel_version: 1.7.0 */
import java.util.List;
import lombok.*;

/**
  An individual step in the execution flow of an attack pattern. Provides a detailed
description of a specific action typically performed by an adversary during the
attack, along with the phase of the attack it belongs to and any specific techniques
used.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class AttackStep  {

  private String description;
  private int step;
  private String phase;
  private List<Technique> techniques;

}