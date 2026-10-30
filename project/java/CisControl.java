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
  One of the CIS Controls: a group of Safeguards on one subject, named by its number, such as Control 4.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class CisControl  {

  private String cisControlId;
  private String title;
  private String description;
  private List<CisSafeguard> controlSafeguards;


}