package None;

/* metamodel_version: 1.7.0 */
import java.util.List;
import lombok.*;

/**
  An additional comment about a CAPEC entry that cannot be captured using the other available elements. Each note has a type indicating its purpose and contains content describing the note.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class Note  {

  private String type;
  private String content;

}