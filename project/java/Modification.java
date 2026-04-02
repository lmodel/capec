package None;

/* metamodel_version: 1.7.0 */
import java.util.List;
import lombok.*;

/**
  A record of a modification made to a CAPEC entry, identifying the modifier,
their organization, the date of modification, the importance of the change,
and any related comments. Modifications that change the meaning of the entry
should be marked as Critical importance.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class Modification  {

  private String modificationName;
  private String modificationOrganization;
  private LocalDate modificationDate;
  private String modificationImportance;
  private String modificationComment;

}