package None;

/* metamodel_version: 1.7.0 */
import java.util.List;
import lombok.*;

/**
  Tracks the original author of a CAPEC entry and any subsequent modifications
to the content. Provides a means of contacting authors and modifiers for
clarifying ambiguities, merging overlapping contributions, etc.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class ContentHistory  {

  private Submission submission;
  private List<Modification> modifications;
  private List<Contribution> contributions;
  private List<PreviousEntryName> previousEntryNames;

}