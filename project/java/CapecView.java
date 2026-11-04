package example;

/* metamodel_version: 1.12.0 */
/* version: 3.9 */
import java.net.URI;
import java.time.LocalDate;
import java.time.LocalTime;
import java.time.ZonedDateTime;
import java.util.List;
import lombok.*;

/**
  One way of looking over the catalogue, by a hierarchy or by a slice of its entries.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class CapecView extends CapecEntry {

  private String type;
  private String objective;
  private List<CapecStakeholder> audience;
  private CapecRelationships members;
  private String filter;


}