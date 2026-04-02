package None;

/* metamodel_version: 1.7.0 */
import java.util.List;
import lombok.*;

/**
  A link from a CAPEC entry to an external reference defined within the catalog.
The External_Reference_ID identifies which external reference is being cited.
An optional Section captures a specific section title or page number relevant
to this use of the reference.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class Reference  {

  private String externalReferenceId;
  private String section;

}