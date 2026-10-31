package example;

/* metamodel_version: 1.12.0 */
/* version: 8.1.2 */
import java.net.URI;
import java.time.LocalDate;
import java.time.LocalTime;
import java.time.ZonedDateTime;
import java.util.List;
import lombok.*;

/**
  One Safeguard of a Control: a single action an enterprise takes, named by its Control's number and its own, such as Safeguard 4.1.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class CisSafeguard  {

  private String cisSafeguardId;
  private String title;
  private String description;
  private String safeguardAssetClass;
  private String safeguardSecurityFunction;
  private List<String> safeguardImplementationGroups;


}