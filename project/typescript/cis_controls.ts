/**
* One of the three Implementation Groups, CIS's tiers for deciding which Safeguards an enterprise puts in place first. Each group includes every Safeguard of the groups before it.
*/
export enum CisImplementationGroup {
    
    /** The first group, where every enterprise starts. */
    Implementation_Group_1 = "IG1",
    /** The second group, which adds Safeguards to the first. */
    Implementation_Group_2 = "IG2",
    /** The third group, which adds the rest and so holds every Safeguard. */
    Implementation_Group_3 = "IG3",
};
/**
* One of the classes of enterprise asset that the CIS Controls sort their Safeguards by. Each Safeguard is about one class.
*/
export enum CisAssetClass {
    
    /** The enterprise's hardware, wherever it runs. */
    Devices = "DEVICES",
    /** The programs and systems that run on the enterprise's devices. */
    Software = "SOFTWARE",
    /** The information the enterprise holds, uses and moves. */
    Data = "DATA",
    /** The people and accounts with access to the enterprise's assets. */
    Users = "USERS",
    /** How the enterprise's devices connect, and how its networks are laid out. */
    Network = "NETWORK",
    /** The enterprise's written governance, such as its policies and procedures. */
    Documentation = "DOCUMENTATION",
};
/**
* The security function a Safeguard serves. The values are the six functions of the NIST Cybersecurity Framework (CSF) 2.0, to which Version 8.1 aligned the CIS Controls.
*/
export enum CisSecurityFunction {
    
    /** The CSF 2.0 function GOVERN. */
    Govern = "GOVERN",
    /** The CSF 2.0 function IDENTIFY. */
    Identify = "IDENTIFY",
    /** The CSF 2.0 function PROTECT. */
    Protect = "PROTECT",
    /** The CSF 2.0 function DETECT. */
    Detect = "DETECT",
    /** The CSF 2.0 function RESPOND. */
    Respond = "RESPOND",
    /** The CSF 2.0 function RECOVER. */
    Recover = "RECOVER",
};


/**
 * One edition of the CIS Controls as a whole: its Controls, each holding its Safeguards.
 */
export interface CisControls {
    /** The edition, as CIS numbers it, such as 8.1, or the revision the guide's pages carry, such as 8.1.2. */
    cis_version: string,
    /** The Controls, in CIS's order. */
    cis_controls: CisControl[],
}


/**
 * One of the CIS Controls: a group of Safeguards on one subject, named by its number, such as Control 4.
 */
export interface CisControl {
    /** The Control's identifier, its number, such as 4. */
    cis_control_id: string,
    /** A name for the Control or Safeguard, in words its user has the right to use. */
    title?: string,
    /** What the Control or Safeguard means to its user, in words its user has the right to use. */
    description?: string,
    /** The Safeguards of the Control. A knowledge bundle relates a Safeguard to its Control with isPartOf instead. */
    control_safeguards?: CisSafeguard[],
}


/**
 * One Safeguard of a Control: a single action an enterprise takes, named by its Control's number and its own, such as Safeguard 4.1.
 */
export interface CisSafeguard {
    /** The Safeguard's identifier, its number, such as 4.1. */
    cis_safeguard_id: string,
    /** A name for the Control or Safeguard, in words its user has the right to use. */
    title?: string,
    /** What the Control or Safeguard means to its user, in words its user has the right to use. */
    description?: string,
    /** The class of enterprise asset the Safeguard is about. */
    safeguard_asset_class: string,
    /** The security function the Safeguard serves, one of the six functions of the NIST Cybersecurity Framework (CSF) 2.0. */
    safeguard_security_function: string,
    /** The Implementation Groups that include the Safeguard. */
    safeguard_implementation_groups: string,
}



