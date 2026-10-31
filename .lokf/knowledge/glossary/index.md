# Glossary

* [Control](control.md) - In the CIS Controls, one of 18 numbered groups of Safeguards, each on one subject. The schema renders a Control as `CisControl`, with its number, 1 to 18, in `cis_control_id`.
* [Safeguard](safeguard.md) - In the CIS Controls, one action an enterprise takes under a Control, named by the Control's number and its own, such as Safeguard 4.1; Version 8.1 has 153. The schema renders a Safeguard as `CisSafeguard`, with its number in `cis_safeguard_id`.
* [Implementation Group](implementation-group.md) - In the CIS Controls, one of three tiers, IG1, IG2 and IG3, that say which Safeguards an enterprise takes up first; each includes the one before it, so IG1 holds 56 Safeguards, IG2 130 and IG3 all 153. The schema renders the tiers as `CisImplementationGroup`.
* [Asset class](asset-class.md) - In the CIS Controls, the kind of enterprise asset a Safeguard is about: Devices, Software, Data, Users, Network or Documentation in Version 8.1. The schema renders the classes as `CisAssetClass`.
* [Security function](security-function.md) - In the CIS Controls, the function of the NIST Cybersecurity Framework (CSF) 2.0 a Safeguard serves: Govern, Identify, Protect, Detect, Respond or Recover. The schema renders the functions as `CisSecurityFunction`, related to lmodel/nist-csf-v2's function class.
