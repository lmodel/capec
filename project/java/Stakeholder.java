package None;

/* metamodel_version: 1.7.0 */
import java.util.List;
import lombok.*;

/**
  A target stakeholder or group for whom a CAPEC view is relevant. Specifies
the type of stakeholder and describes which properties of the view they may
find useful.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class Stakeholder  {

  private String type;
  private String description;

}