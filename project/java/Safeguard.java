package None;

/* metamodel_version: 1.7.0 */
/* version: 8.1.2 */
import java.util.List;
import lombok.*;

/**
  A specific, measurable action that an enterprise should take to implement a CIS Control. Formerly called "Sub-Controls" prior to CIS Controls v8.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class Safeguard  {

  private String id;
  private String title;
  private String safeguardNumber;
  private String description;
  private String assetType;
  private String securityFunction;
  private List<String> implementationGroups;

}