package None;

/* metamodel_version: 1.7.0 */
/* version: 8.1.2 */
import java.util.List;
import lombok.*;

/**
  Root container for a versioned edition of the CIS Critical Security Controls publication.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class CISControlsDocument  {

  private String id;
  private String title;
  private String description;
  private String version;
  private String publicationDate;
  private List<CISControl> controls;

}