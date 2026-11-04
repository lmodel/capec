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
  A publication or page outside CAPEC that entries point to for more detail.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class CapecExternalReference  {

  private String referenceID;
  private List<String> author;
  private String title;
  private String edition;
  private String publication;
  private String publicationYear;
  private String publicationMonth;
  private String publicationDay;
  private String publisher;
  private URI uRL;
  private LocalDate uRLDate;


}