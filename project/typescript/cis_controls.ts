export type CISControlsDocumentId = string;
export type CISControlId = string;
export type SafeguardId = string;
/**
* Self-assessed tier of CIS Controls applicability based on an enterprise's risk profile and resources. Each IG is cumulative — IG2 includes IG1, IG3 includes both. Introduced in CIS Controls v7.1 as the recommended way to prioritize implementation.
*/
export enum ImplementationGroup {
    
    /** Small to medium-sized enterprise with limited IT and cybersecurity expertise to dedicate toward protecting IT assets and personnel. The principal concern is to keep the business operational; limited tolerance for downtime; data sensitivity is low, principally surrounding employee and financial information. Safeguards should be implementable with limited cybersecurity expertise and designed to thwart general, non-targeted attacks using COTS hardware and software. Also called "Essential Cyber Hygiene." */
    IG1 = "IG1",
    /** Enterprise employing individuals responsible for managing and protecting IT infrastructure. Supports multiple departments with differing risk profiles based on job function and mission; may have regulatory compliance burdens; often stores and processes sensitive client or enterprise information and can withstand short interruptions of service. A major concern is loss of public confidence if a breach occurs. Safeguards help security teams cope with increased operational complexity; some depend on enterprise-grade technology and specialized expertise to properly install and configure. Includes all IG1 safeguards. */
    IG2 = "IG2",
    /** Enterprise employing security experts that specialize in the different facets of cybersecurity (e.g., risk management, penetration testing, application security). Assets and data contain sensitive information or functions subject to regulatory and compliance oversight; must address availability of services and the confidentiality and integrity of sensitive data; successful attacks can cause significant harm to the public welfare. Safeguards must abate targeted attacks from a sophisticated adversary and reduce the impact of zero-day attacks. Includes all IG1 and IG2 safeguards. */
    IG3 = "IG3",
};
/**
* The category of enterprise asset primarily addressed by a Safeguard. Aligned with the CIS Controls Asset Classes taxonomy (v8.1, pg. 8). Sub-classes exist within each category but Safeguards reference the top-level class only.
*/
export enum AssetType {
    
    /** Enterprise assets (data processing and storage assets), end-user devices (including portable and mobile devices), servers, Internet of Things (IoT) and non-computing devices, network devices, and removable media. Devices may exist in physical, virtual, or cloud-based environments and can remotely connect to these systems. */
    Devices = "Devices",
    /** Sets of data and instructions used to direct a computer to complete a specific task. Includes applications, operating systems (with their services, libraries, and APIs), and firmware. Both applications and operating systems are considered software assets. */
    Software = "Software",
    /** A collection of facts that can be examined, considered, and used for decision-making. Although data may be physical, the CIS Controls primarily provide protection for digital data stored, transferred, and processed by enterprise assets. Sub-classes: sensitive data, log data, and physical data. */
    Data = "Data",
    /** Employees, third-party vendors, contractors, service providers, consultants, or any other person authorized to access an enterprise asset. Includes workforce, service providers, and user/administrator/service accounts. */
    Users = "Users",
    /** A group of interconnected devices that exchange data. A superset of network infrastructure (hardware and software providing connectivity and communication) and network architecture (the logical and physical design of the network). */
    Network = "Network",
    /** Policies, processes, procedures, plans, diagrams, and other written material (physical or digital), such as compliance reports. Examples include methods of governance for an enterprise, processes users follow, or descriptions of network architecture. Sub-classes: plans, policies, processes, and procedures. */
    Documentation = "Documentation",
};
/**
* NIST Cybersecurity Framework 2.0 security function category to which a Safeguard is primarily mapped. Values correspond exactly to the six CSF 2.0 Functions; enum as a whole is a close match for nist_csf_v2:CSFFunction.
*/
export enum SecurityFunction {
    
    /** Establish and monitor the organization's cybersecurity risk management strategy, expectations, and policy. */
    Govern = "Govern",
    /** Develop an organizational understanding of cybersecurity risk to systems, people, assets, data, and capabilities. */
    Identify = "Identify",
    /** Develop and implement appropriate safeguards to ensure delivery of critical services. */
    Protect = "Protect",
    /** Develop and implement appropriate activities to identify the occurrence of a cybersecurity event. */
    Detect = "Detect",
    /** Develop and implement appropriate activities to take action regarding a detected cybersecurity incident. */
    Respond = "Respond",
    /** Develop and implement appropriate activities to maintain plans for resilience and to restore capabilities impaired by a cybersecurity incident. */
    Recover = "Recover",
};


/**
 * Root container for a versioned edition of the CIS Critical Security Controls publication.
 */
export interface CISControlsDocument {
    /** Unique identifier for the element. */
    id: string,
    /** Human-readable title of the element. */
    title: string,
    /** Descriptive text for the element. */
    description?: string,
    /** Version string of the CIS Controls document (e.g. "8.1"). */
    version?: string,
    /** Publication date of the CIS Controls document (ISO 8601). */
    publication_date?: string,
    /** List of CIS Controls in this document. */
    controls?: CISControl[],
}


/**
 * One of the 18 CIS Critical Security Controls — a high-level defensive action category that enterprises should implement to reduce cyber risk.
 */
export interface CISControl {
    /** Composite identifier for the control (e.g. "CIS-1"). */
    id: string,
    /** Human-readable title of the element. */
    title: string,
    /** Numeric identifier of the parent CIS Control (1–18). */
    control_number: string,
    /** Brief description of the intent of a Control and its utility as a defensive action. */
    overview?: string,
    /** Explanation of the importance of this Control in blocking, mitigating, or identifying attacks, and how attackers exploit its absence. */
    why_critical?: string,
    /** Technical description of the processes and technologies that enable implementation and automation of this Control. */
    procedures_and_tools?: string,
    /** List of Safeguards belonging to a CIS Control. */
    safeguards?: SafeguardId[],
}


/**
 * A specific, measurable action that an enterprise should take to implement a CIS Control. Formerly called "Sub-Controls" prior to CIS Controls v8.
 */
export interface Safeguard {
    /** Composite identifier for the safeguard (e.g. "CIS-1.1"). */
    id: string,
    /** Human-readable title of the element. */
    title: string,
    /** Dotted identifier of this Safeguard (e.g. "1.1"). Combines the parent control number with a sequential Safeguard index. */
    safeguard_number: string,
    /** Descriptive text for the element. */
    description?: string,
    /** The class of enterprise asset primarily addressed by this Safeguard. */
    asset_type: string,
    /** NIST CSF 2.0 function category to which this Safeguard is mapped. */
    security_function: string,
    /** Implementation Group(s) for which this Safeguard is applicable. A Safeguard listed under IG2 is also required for IG3 enterprises; a Safeguard listed under IG1 is required for all enterprises. */
    implementation_groups: string,
}



