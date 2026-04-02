package None;

/* metamodel_version: 1.7.0 */
import java.util.List;
import lombok.*;

/**
  A view in CAPEC represents a perspective with which one might look at the collection
of attack patterns defined within CAPEC. There are three different types of views as
defined by the Type attribute: graphs, explicit slices, and implicit slices.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class View  {

  private int id;
  private String name;
  private String status;
  private String type;
  private List<Note> notes;
  private ContentHistory contentHistory;
  private List<Reference> references;
  private String objective;
  private List<Stakeholder> audience;
  private Relationships members;
  private String filter;

}