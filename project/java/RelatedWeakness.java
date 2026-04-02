package None;

/* metamodel_version: 1.7.0 */
import java.util.List;
import lombok.*;

/**
  A reference to a CWE (Common Weakness Enumeration) weakness associated with an
attack pattern. The association implies a weakness that must exist for a given
attack to be successful. If multiple weaknesses are listed, any of them (but not
necessarily all) may be present for the attack to succeed.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class RelatedWeakness  {

  private int cweId;

}