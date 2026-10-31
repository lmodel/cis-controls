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
  One edition of the CIS Controls as a whole: its Controls, each holding its Safeguards.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class CisControls  {

  private String cisVersion;
  private List<CisControl> cisControls;


}