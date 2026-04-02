package None;

/* metamodel_version: 1.7.0 */
import java.util.List;
import lombok.*;

/**
  A description of the level of skills or specific knowledge needed by an adversary to execute this type of attack. Each skill entry captures both the skill level and a textual description of the knowledge required.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class Skill  {

  private String description;
  private String level;

}