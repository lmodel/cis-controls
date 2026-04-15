package None;

/* metamodel_version: 1.7.0 */
/* version: 8.1.2 */
import java.util.List;
import lombok.*;

/**
  One of the CIS Critical Security Controls; a high-level defensive action category that enterprises should implement to reduce cyber risk.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class CISControl  {

  private String id;
  private String title;
  private String controlNumber;
  private String overview;
  private String whyCritical;
  private String proceduresAndTools;
  private List<Safeguard> safeguards;

}