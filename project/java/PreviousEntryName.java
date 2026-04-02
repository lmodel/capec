package None;

/* metamodel_version: 1.7.0 */
import java.util.List;
import lombok.*;

/**
  A previous name that was used for a CAPEC entry before a substantive name change.
Should align with a corresponding Modification element that records the change.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class PreviousEntryName  {

  private String name;
  private LocalDate entryDate;

}