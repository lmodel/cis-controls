from __future__ import annotations

import re
import sys
from datetime import (
    date,
    datetime,
    time
)
from decimal import Decimal
from enum import Enum
from typing import (
    Any,
    ClassVar,
    Literal,
    Optional,
    Union
)

from pydantic import (
    BaseModel,
    ConfigDict,
    Field,
    RootModel,
    SerializationInfo,
    SerializerFunctionWrapHandler,
    field_validator,
    model_serializer
)


metamodel_version = "1.7.0"
version = "8.1.2"


class ConfiguredBaseModel(BaseModel):
    model_config = ConfigDict(
        serialize_by_alias = True,
        validate_by_name = True,
        validate_assignment = True,
        validate_default = True,
        extra = "forbid",
        arbitrary_types_allowed = True,
        use_enum_values = True,
        strict = False,
    )





class LinkMLMeta(RootModel):
    root: dict[str, Any] = {}
    model_config = ConfigDict(frozen=True)

    def __getattr__(self, key:str):
        return getattr(self.root, key)

    def __getitem__(self, key:str):
        return self.root[key]

    def __setitem__(self, key:str, value):
        self.root[key] = value

    def __contains__(self, key:str) -> bool:
        return key in self.root


linkml_meta = LinkMLMeta({'default_prefix': 'cis_controls',
     'default_range': 'string',
     'description': 'LinkML schema for the CIS Critical Security Controls (CIS '
                    'Controls) Version 8.1.2\n'
                    '(March 2025). Models the 18 Controls and their Safeguards, '
                    'including asset types,\n'
                    'security functions, and Implementation Groups as defined by '
                    'the Center for Internet\n'
                    'Security. Source document: CIS Controls v8.1.2 (March 2025),\n'
                    'licensed CC BY-NC-ND 4.0 '
                    '(https://creativecommons.org/licenses/by-nc-nd/4.0/).',
     'id': 'https://w3id.org/lmodel/cis-controls',
     'imports': ['linkml:types'],
     'license': 'Apache-2.0',
     'name': 'cis-controls',
     'prefixes': {'WIKIDATA': {'prefix_prefix': 'WIKIDATA',
                               'prefix_reference': 'https://www.wikidata.org/wiki/'},
                  'cis_controls': {'prefix_prefix': 'cis_controls',
                                   'prefix_reference': 'https://w3id.org/lmodel/cis-controls/'},
                  'dct': {'prefix_prefix': 'dct',
                          'prefix_reference': 'http://purl.org/dc/terms/'},
                  'iso27001': {'prefix_prefix': 'iso27001',
                               'prefix_reference': 'https://w3id.org/lmodel/iso27001/'},
                  'linkml': {'prefix_prefix': 'linkml',
                             'prefix_reference': 'https://w3id.org/linkml/'},
                  'nist_csf_v2': {'prefix_prefix': 'nist_csf_v2',
                                  'prefix_reference': 'https://w3id.org/lmodel/nist-csf-v2/'},
                  'rdfs': {'prefix_prefix': 'rdfs',
                           'prefix_reference': 'http://www.w3.org/2000/01/rdf-schema#'},
                  'schema': {'prefix_prefix': 'schema',
                             'prefix_reference': 'http://schema.org/'},
                  'skos': {'prefix_prefix': 'skos',
                           'prefix_reference': 'http://www.w3.org/2004/02/skos/core#'},
                  'xsd': {'prefix_prefix': 'xsd',
                          'prefix_reference': 'http://www.w3.org/2001/XMLSchema#'}},
     'see_also': ['https://www.cisecurity.org/controls/',
                  'https://lmodel.github.io/cis-controls'],
     'source_file': 'src/cis_controls/schema/cis_controls.yaml',
     'subsets': {'essential_cyber_hygiene': {'description': 'Profile containing '
                                                            'Safeguards where '
                                                            'implementation_groups '
                                                            'includes IG1. The '
                                                            'minimum set every '
                                                            'enterprise should '
                                                            'implement ("Essential '
                                                            'Cyber Hygiene"). 56 '
                                                            'safeguards across all '
                                                            '18 Controls.',
                                             'from_schema': 'https://w3id.org/lmodel/cis-controls',
                                             'name': 'essential_cyber_hygiene'},
                 'ig2_controls': {'description': 'Profile containing Safeguards '
                                                 'where implementation_groups '
                                                 'includes IG2 (a superset of '
                                                 'essential_cyber_hygiene). For '
                                                 'organizations managing sensitive '
                                                 'data with dedicated security '
                                                 'staff.',
                                  'from_schema': 'https://w3id.org/lmodel/cis-controls',
                                  'name': 'ig2_controls'},
                 'ig3_controls': {'description': 'Profile containing Safeguards '
                                                 'where implementation_groups '
                                                 'includes IG3 (a superset of '
                                                 'ig2_controls). For high-risk '
                                                 'profiles with specialist '
                                                 'security expertise. All 153 '
                                                 'safeguards across 18 Controls.',
                                  'from_schema': 'https://w3id.org/lmodel/cis-controls',
                                  'name': 'ig3_controls'}},
     'title': 'CIS Controls',
     'types': {'ControlId': {'base': 'str',
                             'description': 'Identifier for a CIS Control (e.g. '
                                            '"1", "18").',
                             'from_schema': 'https://w3id.org/lmodel/cis-controls',
                             'name': 'ControlId',
                             'pattern': '^([1-9]|1[0-8])$',
                             'uri': 'xsd:string'},
               'SafeguardId': {'base': 'str',
                               'description': 'Identifier for a CIS Safeguard in '
                                              'the form <control>.<safeguard> '
                                              '(e.g. "1.1", "16.14").',
                               'from_schema': 'https://w3id.org/lmodel/cis-controls',
                               'name': 'SafeguardId',
                               'pattern': '^([1-9]|1[0-8])\\.[0-9]+$',
                               'uri': 'xsd:string'}}} )

class ImplementationGroup(str, Enum):
    """
    Self-assessed tier of CIS Controls applicability based on an enterprise's risk profile and resources. Each IG is cumulative — IG2 includes IG1, IG3 includes both. Introduced in CIS Controls v7.1 as the recommended way to prioritize implementation.
    """
    IG1 = "IG1"
    """
    Small to medium-sized enterprise with limited IT and cybersecurity expertise to dedicate toward protecting IT assets and personnel. The principal concern is to keep the business operational; limited tolerance for downtime; data sensitivity is low, principally surrounding employee and financial information. Safeguards should be implementable with limited cybersecurity expertise and designed to thwart general, non-targeted attacks using COTS hardware and software. Also called "Essential Cyber Hygiene."
    """
    IG2 = "IG2"
    """
    Enterprise employing individuals responsible for managing and protecting IT infrastructure. Supports multiple departments with differing risk profiles based on job function and mission; may have regulatory compliance burdens; often stores and processes sensitive client or enterprise information and can withstand short interruptions of service. A major concern is loss of public confidence if a breach occurs. Safeguards help security teams cope with increased operational complexity; some depend on enterprise-grade technology and specialized expertise to properly install and configure. Includes all IG1 safeguards.
    """
    IG3 = "IG3"
    """
    Enterprise employing security experts that specialize in the different facets of cybersecurity (e.g., risk management, penetration testing, application security). Assets and data contain sensitive information or functions subject to regulatory and compliance oversight; must address availability of services and the confidentiality and integrity of sensitive data; successful attacks can cause significant harm to the public welfare. Safeguards must abate targeted attacks from a sophisticated adversary and reduce the impact of zero-day attacks. Includes all IG1 and IG2 safeguards.
    """


class AssetType(str, Enum):
    """
    The category of enterprise asset primarily addressed by a Safeguard. Aligned with the CIS Controls Asset Classes taxonomy (v8.1, pg. 8). Sub-classes exist within each category but Safeguards reference the top-level class only.
    """
    Devices = "Devices"
    """
    Enterprise assets (data processing and storage assets), end-user devices (including portable and mobile devices), servers, Internet of Things (IoT) and non-computing devices, network devices, and removable media. Devices may exist in physical, virtual, or cloud-based environments and can remotely connect to these systems.
    """
    Software = "Software"
    """
    Sets of data and instructions used to direct a computer to complete a specific task. Includes applications, operating systems (with their services, libraries, and APIs), and firmware. Both applications and operating systems are considered software assets.
    """
    Data = "Data"
    """
    A collection of facts that can be examined, considered, and used for decision-making. Although data may be physical, the CIS Controls primarily provide protection for digital data stored, transferred, and processed by enterprise assets. Sub-classes: sensitive data, log data, and physical data.
    """
    Users = "Users"
    """
    Employees, third-party vendors, contractors, service providers, consultants, or any other person authorized to access an enterprise asset. Includes workforce, service providers, and user/administrator/service accounts.
    """
    Network = "Network"
    """
    A group of interconnected devices that exchange data. A superset of network infrastructure (hardware and software providing connectivity and communication) and network architecture (the logical and physical design of the network).
    """
    Documentation = "Documentation"
    """
    Policies, processes, procedures, plans, diagrams, and other written material (physical or digital), such as compliance reports. Examples include methods of governance for an enterprise, processes users follow, or descriptions of network architecture. Sub-classes: plans, policies, processes, and procedures.
    """


class SecurityFunction(str, Enum):
    """
    NIST Cybersecurity Framework 2.0 security function category to which a Safeguard is primarily mapped. Values correspond exactly to the six CSF 2.0 Functions; enum as a whole is a close match for nist_csf_v2:CSFFunction.
    """
    Govern = "Govern"
    """
    Establish and monitor the organization's cybersecurity risk management strategy, expectations, and policy.
    """
    Identify = "Identify"
    """
    Develop an organizational understanding of cybersecurity risk to systems, people, assets, data, and capabilities.
    """
    Protect = "Protect"
    """
    Develop and implement appropriate safeguards to ensure delivery of critical services.
    """
    Detect = "Detect"
    """
    Develop and implement appropriate activities to identify the occurrence of a cybersecurity event.
    """
    Respond = "Respond"
    """
    Develop and implement appropriate activities to take action regarding a detected cybersecurity incident.
    """
    Recover = "Recover"
    """
    Develop and implement appropriate activities to maintain plans for resilience and to restore capabilities impaired by a cybersecurity incident.
    """



class CISControlsDocument(ConfiguredBaseModel):
    """
    Root container for a versioned edition of the CIS Critical Security Controls publication.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'close_mappings': ['nist_csf_v2:CSFDocument'],
         'exact_mappings': ['schema:CreativeWork'],
         'from_schema': 'https://w3id.org/lmodel/cis-controls',
         'id_prefixes': ['cis_controls'],
         'related_mappings': ['iso27001:InformationSecurityManagementSystem'],
         'see_also': ['https://www.cisecurity.org/controls/'],
         'tree_root': True})

    id: str = Field(default=..., description="""Unique identifier for the element.""", json_schema_extra = { "linkml_meta": {'domain_of': ['CISControlsDocument', 'CISControl', 'Safeguard'],
         'exact_mappings': ['nist_csf_v2:id'],
         'slot_uri': 'dct:identifier'} })
    title: str = Field(default=..., description="""Human-readable title of the element.""", json_schema_extra = { "linkml_meta": {'domain_of': ['CISControlsDocument', 'CISControl', 'Safeguard'],
         'exact_mappings': ['nist_csf_v2:title'],
         'slot_uri': 'dct:title'} })
    description: Optional[str] = Field(default=None, description="""Descriptive text for the element.""", json_schema_extra = { "linkml_meta": {'close_mappings': ['nist_csf_v2:prose'],
         'domain_of': ['CISControlsDocument', 'Safeguard'],
         'slot_uri': 'dct:description'} })
    version: Optional[str] = Field(default=None, description="""Version string of the CIS Controls document (e.g. \"8.1\").""", json_schema_extra = { "linkml_meta": {'domain_of': ['CISControlsDocument'],
         'exact_mappings': ['nist_csf_v2:version'],
         'slot_uri': 'dct:hasVersion'} })
    publication_date: Optional[str] = Field(default=None, description="""Publication date of the CIS Controls document (ISO 8601).""", json_schema_extra = { "linkml_meta": {'domain_of': ['CISControlsDocument'], 'slot_uri': 'dct:date'} })
    controls: Optional[list[CISControl]] = Field(default=None, description="""List of CIS Controls in this document.""", json_schema_extra = { "linkml_meta": {'close_mappings': ['nist_csf_v2:groups'], 'domain_of': ['CISControlsDocument']} })


class CISControl(ConfiguredBaseModel):
    """
    One of the 18 CIS Critical Security Controls — a high-level defensive action category that enterprises should implement to reduce cyber risk.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'close_mappings': ['nist_csf_v2:CSFCategory'],
         'exact_mappings': ['schema:Action'],
         'from_schema': 'https://w3id.org/lmodel/cis-controls',
         'id_prefixes': ['cis_controls'],
         'related_mappings': ['WIKIDATA:Q2695280'],
         'see_also': ['https://www.cisecurity.org/controls/'],
         'slot_usage': {'id': {'description': 'Composite identifier for the control '
                                              '(e.g. "CIS-1").',
                               'name': 'id',
                               'pattern': '^CIS-([1-9]|1[0-8])$'}}})

    id: str = Field(default=..., description="""Composite identifier for the control (e.g. \"CIS-1\").""", json_schema_extra = { "linkml_meta": {'domain_of': ['CISControlsDocument', 'CISControl', 'Safeguard'],
         'exact_mappings': ['nist_csf_v2:id'],
         'slot_uri': 'dct:identifier'} })
    title: str = Field(default=..., description="""Human-readable title of the element.""", json_schema_extra = { "linkml_meta": {'domain_of': ['CISControlsDocument', 'CISControl', 'Safeguard'],
         'exact_mappings': ['nist_csf_v2:title'],
         'slot_uri': 'dct:title'} })
    control_number: str = Field(default=..., description="""Numeric identifier of the parent CIS Control (1–18).""", json_schema_extra = { "linkml_meta": {'domain_of': ['CISControl']} })
    overview: Optional[str] = Field(default=None, description="""Brief description of the intent of a Control and its utility as a defensive action.""", json_schema_extra = { "linkml_meta": {'close_mappings': ['nist_csf_v2:prose'], 'domain_of': ['CISControl']} })
    why_critical: Optional[str] = Field(default=None, description="""Explanation of the importance of this Control in blocking, mitigating, or identifying attacks, and how attackers exploit its absence.""", json_schema_extra = { "linkml_meta": {'domain_of': ['CISControl']} })
    procedures_and_tools: Optional[str] = Field(default=None, description="""Technical description of the processes and technologies that enable implementation and automation of this Control.""", json_schema_extra = { "linkml_meta": {'domain_of': ['CISControl']} })
    safeguards: Optional[list[Safeguard]] = Field(default=None, description="""List of Safeguards belonging to a CIS Control.""", json_schema_extra = { "linkml_meta": {'close_mappings': ['nist_csf_v2:controls'], 'domain_of': ['CISControl']} })

    @field_validator('id')
    def pattern_id(cls, v):
        pattern=re.compile(r"^CIS-([1-9]|1[0-8])$")
        if isinstance(v, list):
            for element in v:
                if isinstance(element, str) and not pattern.match(element):
                    err_msg = f"Invalid id format: {element}"
                    raise ValueError(err_msg)
        elif isinstance(v, str) and not pattern.match(v):
            err_msg = f"Invalid id format: {v}"
            raise ValueError(err_msg)
        return v


class Safeguard(ConfiguredBaseModel):
    """
    A specific, measurable action that an enterprise should take to implement a CIS Control. Formerly called \"Sub-Controls\" prior to CIS Controls v8.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'aliases': ['sub-control'],
         'close_mappings': ['nist_csf_v2:CSFSubcategory'],
         'exact_mappings': ['schema:Action'],
         'from_schema': 'https://w3id.org/lmodel/cis-controls',
         'id_prefixes': ['cis_controls'],
         'in_subset': ['essential_cyber_hygiene', 'ig2_controls', 'ig3_controls'],
         'related_mappings': ['iso27001:SecurityControl'],
         'see_also': ['https://www.cisecurity.org/controls/'],
         'slot_usage': {'id': {'description': 'Composite identifier for the safeguard '
                                              '(e.g. "CIS-1.1").',
                               'name': 'id',
                               'pattern': '^CIS-([1-9]|1[0-8])\\.[0-9]+$'},
                        'implementation_groups': {'description': 'Implementation '
                                                                 'Group(s) for which '
                                                                 'this Safeguard is '
                                                                 'applicable. A '
                                                                 'Safeguard listed '
                                                                 'under IG2 is also '
                                                                 'required for IG3 '
                                                                 'enterprises; a '
                                                                 'Safeguard listed '
                                                                 'under IG1 is '
                                                                 'required for all '
                                                                 'enterprises.',
                                                  'name': 'implementation_groups'}}})

    id: str = Field(default=..., description="""Composite identifier for the safeguard (e.g. \"CIS-1.1\").""", json_schema_extra = { "linkml_meta": {'domain_of': ['CISControlsDocument', 'CISControl', 'Safeguard'],
         'exact_mappings': ['nist_csf_v2:id'],
         'slot_uri': 'dct:identifier'} })
    title: str = Field(default=..., description="""Human-readable title of the element.""", json_schema_extra = { "linkml_meta": {'domain_of': ['CISControlsDocument', 'CISControl', 'Safeguard'],
         'exact_mappings': ['nist_csf_v2:title'],
         'slot_uri': 'dct:title'} })
    safeguard_number: str = Field(default=..., description="""Dotted identifier of this Safeguard (e.g. \"1.1\"). Combines the parent control number with a sequential Safeguard index.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Safeguard']} })
    description: Optional[str] = Field(default=None, description="""Descriptive text for the element.""", json_schema_extra = { "linkml_meta": {'close_mappings': ['nist_csf_v2:prose'],
         'domain_of': ['CISControlsDocument', 'Safeguard'],
         'slot_uri': 'dct:description'} })
    asset_type: AssetType = Field(default=..., description="""The class of enterprise asset primarily addressed by this Safeguard.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Safeguard']} })
    security_function: SecurityFunction = Field(default=..., description="""NIST CSF 2.0 function category to which this Safeguard is mapped.""", json_schema_extra = { "linkml_meta": {'close_mappings': ['nist_csf_v2:groups'], 'domain_of': ['Safeguard']} })
    implementation_groups: list[ImplementationGroup] = Field(default=..., description="""Implementation Group(s) for which this Safeguard is applicable. A Safeguard listed under IG2 is also required for IG3 enterprises; a Safeguard listed under IG1 is required for all enterprises.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Safeguard'], 'related_mappings': ['nist_csf_v2:props']} })

    @field_validator('id')
    def pattern_id(cls, v):
        pattern=re.compile(r"^CIS-([1-9]|1[0-8])\.[0-9]+$")
        if isinstance(v, list):
            for element in v:
                if isinstance(element, str) and not pattern.match(element):
                    err_msg = f"Invalid id format: {element}"
                    raise ValueError(err_msg)
        elif isinstance(v, str) and not pattern.match(v):
            err_msg = f"Invalid id format: {v}"
            raise ValueError(err_msg)
        return v


# Model rebuild
# see https://pydantic-docs.helpmanual.io/usage/models/#rebuilding-a-model
CISControlsDocument.model_rebuild()
CISControl.model_rebuild()
Safeguard.model_rebuild()
