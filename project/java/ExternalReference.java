package None;

/* metamodel_version: 1.7.0 */
import java.util.List;
import lombok.*;

/**
  An external reference provides a pointer to where more information and deeper insight
can be obtained about an attack pattern, category, or view. Examples include research
papers and excerpts from publications. Not all elements need to be used since some are
designed for web references and others for book references.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class ExternalReference  {

  private String referenceId;
  private List<String> authors;
  private String title;
  private String edition;
  private String publication;
  private String publicationYear;
  private String publicationMonth;
  private String publicationDay;
  private String publisher;
  private String url;
  private LocalDate urlDate;

}