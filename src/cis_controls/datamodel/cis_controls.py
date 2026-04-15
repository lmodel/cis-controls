# Auto generated from cis_controls.yaml by pythongen.py version: 0.0.1
# Generation date: 2026-04-15T23:30:14
# Schema: cis-controls
#
# id: https://w3id.org/lmodel/cis-controls
# description: LinkML schema for the CIS Critical Security Controls (CIS Controls) Version 8.1.2 (March 2025). Models the 18 Controls and their Safeguards, including asset types, security functions, and Implementation Groups as defined by the Center for Internet Security. Source document: CIS Controls v8.1.2 (March 2025), licensed CC BY-NC-ND 4.0 (https://creativecommons.org/licenses/by-nc-nd/4.0/).
# license: Apache-2.0

import dataclasses
import re
from dataclasses import dataclass
from datetime import (
    date,
    datetime,
    time
)
from typing import (
    Any,
    ClassVar,
    Dict,
    List,
    Optional,
    Union
)

from jsonasobj2 import (
    JsonObj,
    as_dict
)
from linkml_runtime.linkml_model.meta import (
    EnumDefinition,
    PermissibleValue,
    PvFormulaOptions
)
from linkml_runtime.utils.curienamespace import CurieNamespace
from linkml_runtime.utils.enumerations import EnumDefinitionImpl
from linkml_runtime.utils.formatutils import (
    camelcase,
    sfx,
    underscore
)
from linkml_runtime.utils.metamodelcore import (
    bnode,
    empty_dict,
    empty_list
)
from linkml_runtime.utils.slot import Slot
from linkml_runtime.utils.yamlutils import (
    YAMLRoot,
    extended_float,
    extended_int,
    extended_str
)
from rdflib import (
    Namespace,
    URIRef
)

from linkml_runtime.linkml_model.types import String

metamodel_version = "1.7.0"
version = "8.1.2"

# Namespaces
WIKIDATA = CurieNamespace('WIKIDATA', 'https://www.wikidata.org/wiki/')
CIS_CONTROLS = CurieNamespace('cis_controls', 'https://w3id.org/lmodel/cis-controls/')
DCT = CurieNamespace('dct', 'http://purl.org/dc/terms/')
ISO27001 = CurieNamespace('iso27001', 'https://w3id.org/lmodel/iso27001/')
LINKML = CurieNamespace('linkml', 'https://w3id.org/linkml/')
NIST_CSF_V2 = CurieNamespace('nist_csf_v2', 'https://w3id.org/lmodel/nist-csf-v2/')
RDFS = CurieNamespace('rdfs', 'http://www.w3.org/2000/01/rdf-schema#')
SCHEMA = CurieNamespace('schema', 'http://schema.org/')
SKOS = CurieNamespace('skos', 'http://www.w3.org/2004/02/skos/core#')
XSD = CurieNamespace('xsd', 'http://www.w3.org/2001/XMLSchema#')
DEFAULT_ = CIS_CONTROLS


# Types
class ControlId(str):
    """ Identifier for a CIS Control (e.g. "1", "18"). """
    type_class_uri = XSD["string"]
    type_class_curie = "xsd:string"
    type_name = "ControlId"
    type_model_uri = CIS_CONTROLS.ControlId


class SafeguardId(str):
    """ Identifier for a CIS Safeguard in the form <control>.<safeguard> (e.g. "1.1", "16.14"). """
    type_class_uri = XSD["string"]
    type_class_curie = "xsd:string"
    type_name = "SafeguardId"
    type_model_uri = CIS_CONTROLS.SafeguardId


# Class references
class CISControlsDocumentId(extended_str):
    pass


class CISControlId(extended_str):
    pass


class SafeguardId(extended_str):
    pass


@dataclass(repr=False)
class CISControlsDocument(YAMLRoot):
    """
    Root container for a versioned edition of the CIS Critical Security Controls publication.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CIS_CONTROLS["CISControlsDocument"]
    class_class_curie: ClassVar[str] = "cis_controls:CISControlsDocument"
    class_name: ClassVar[str] = "CISControlsDocument"
    class_model_uri: ClassVar[URIRef] = CIS_CONTROLS.CISControlsDocument

    id: Union[str, CISControlsDocumentId] = None
    title: str = None
    description: Optional[str] = None
    version: Optional[str] = None
    publication_date: Optional[str] = None
    controls: Optional[Union[dict[Union[str, CISControlId], Union[dict, "CISControl"]], list[Union[dict, "CISControl"]]]] = empty_dict()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, CISControlsDocumentId):
            self.id = CISControlsDocumentId(self.id)

        if self._is_empty(self.title):
            self.MissingRequiredField("title")
        if not isinstance(self.title, str):
            self.title = str(self.title)

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        if self.version is not None and not isinstance(self.version, str):
            self.version = str(self.version)

        if self.publication_date is not None and not isinstance(self.publication_date, str):
            self.publication_date = str(self.publication_date)

        self._normalize_inlined_as_list(slot_name="controls", slot_type=CISControl, key_name="id", keyed=True)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class CISControl(YAMLRoot):
    """
    One of the CIS Critical Security Controls; a high-level defensive action category that enterprises should
    implement to reduce cyber risk.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CIS_CONTROLS["CISControl"]
    class_class_curie: ClassVar[str] = "cis_controls:CISControl"
    class_name: ClassVar[str] = "CISControl"
    class_model_uri: ClassVar[URIRef] = CIS_CONTROLS.CISControl

    id: Union[str, CISControlId] = None
    title: str = None
    control_number: str = None
    overview: Optional[str] = None
    why_critical: Optional[str] = None
    procedures_and_tools: Optional[str] = None
    safeguards: Optional[Union[dict[Union[str, SafeguardId], Union[dict, "Safeguard"]], list[Union[dict, "Safeguard"]]]] = empty_dict()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, CISControlId):
            self.id = CISControlId(self.id)

        if self._is_empty(self.title):
            self.MissingRequiredField("title")
        if not isinstance(self.title, str):
            self.title = str(self.title)

        if self._is_empty(self.control_number):
            self.MissingRequiredField("control_number")
        if not isinstance(self.control_number, str):
            self.control_number = str(self.control_number)

        if self.overview is not None and not isinstance(self.overview, str):
            self.overview = str(self.overview)

        if self.why_critical is not None and not isinstance(self.why_critical, str):
            self.why_critical = str(self.why_critical)

        if self.procedures_and_tools is not None and not isinstance(self.procedures_and_tools, str):
            self.procedures_and_tools = str(self.procedures_and_tools)

        self._normalize_inlined_as_list(slot_name="safeguards", slot_type=Safeguard, key_name="id", keyed=True)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Safeguard(YAMLRoot):
    """
    A specific, measurable action that an enterprise should take to implement a CIS Control. Formerly called
    "Sub-Controls" prior to CIS Controls v8.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CIS_CONTROLS["Safeguard"]
    class_class_curie: ClassVar[str] = "cis_controls:Safeguard"
    class_name: ClassVar[str] = "Safeguard"
    class_model_uri: ClassVar[URIRef] = CIS_CONTROLS.Safeguard

    id: Union[str, SafeguardId] = None
    title: str = None
    safeguard_number: str = None
    asset_type: Union[str, "AssetType"] = None
    security_function: Union[str, "SecurityFunction"] = None
    implementation_groups: Union[Union[str, "ImplementationGroup"], list[Union[str, "ImplementationGroup"]]] = None
    description: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, SafeguardId):
            self.id = SafeguardId(self.id)

        if self._is_empty(self.title):
            self.MissingRequiredField("title")
        if not isinstance(self.title, str):
            self.title = str(self.title)

        if self._is_empty(self.safeguard_number):
            self.MissingRequiredField("safeguard_number")
        if not isinstance(self.safeguard_number, str):
            self.safeguard_number = str(self.safeguard_number)

        if self._is_empty(self.asset_type):
            self.MissingRequiredField("asset_type")
        if not isinstance(self.asset_type, AssetType):
            self.asset_type = AssetType(self.asset_type)

        if self._is_empty(self.security_function):
            self.MissingRequiredField("security_function")
        if not isinstance(self.security_function, SecurityFunction):
            self.security_function = SecurityFunction(self.security_function)

        if self._is_empty(self.implementation_groups):
            self.MissingRequiredField("implementation_groups")
        if not isinstance(self.implementation_groups, list):
            self.implementation_groups = [self.implementation_groups] if self.implementation_groups is not None else []
        self.implementation_groups = [v if isinstance(v, ImplementationGroup) else ImplementationGroup(v) for v in self.implementation_groups]

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        super().__post_init__(**kwargs)


# Enumerations
class ImplementationGroup(EnumDefinitionImpl):
    """
    Self-assessed tier of CIS Controls applicability based on an enterprise's risk profile and resources. Each IG is
    cumulative — IG2 includes IG1, IG3 includes both. Introduced in CIS Controls v7.1 as the recommended way to
    prioritize implementation.
    """
    IG1 = PermissibleValue(
        text="IG1",
        description="""Small to medium-sized enterprise with limited IT and cybersecurity expertise to dedicate toward protecting IT assets and personnel. The principal concern is to keep the business operational; limited tolerance for downtime; data sensitivity is low, principally surrounding employee and financial information. Safeguards should be implementable with limited cybersecurity expertise and designed to thwart general, non-targeted attacks using COTS hardware and software. Also called \"Essential Cyber Hygiene.\"""")
    IG2 = PermissibleValue(
        text="IG2",
        description="""Enterprise employing individuals responsible for managing and protecting IT infrastructure. Supports multiple departments with differing risk profiles based on job function and mission; may have regulatory compliance burdens; often stores and processes sensitive client or enterprise information and can withstand short interruptions of service. A major concern is loss of public confidence if a breach occurs. Safeguards help security teams cope with increased operational complexity; some depend on enterprise-grade technology and specialized expertise to properly install and configure. Includes all IG1 safeguards.""")
    IG3 = PermissibleValue(
        text="IG3",
        description="""Enterprise employing security experts that specialize in the different facets of cybersecurity (e.g., risk management, penetration testing, application security). Assets and data contain sensitive information or functions subject to regulatory and compliance oversight; must address availability of services and the confidentiality and integrity of sensitive data; successful attacks can cause significant harm to the public welfare. Safeguards must abate targeted attacks from a sophisticated adversary and reduce the impact of zero-day attacks. Includes all IG1 and IG2 safeguards.""")

    _defn = EnumDefinition(
        name="ImplementationGroup",
        description="""Self-assessed tier of CIS Controls applicability based on an enterprise's risk profile and resources. Each IG is cumulative — IG2 includes IG1, IG3 includes both. Introduced in CIS Controls v7.1 as the recommended way to prioritize implementation.""",
    )

class AssetType(EnumDefinitionImpl):
    """
    The category of enterprise asset primarily addressed by a Safeguard. Aligned with the CIS Controls Asset Classes
    taxonomy (v8.1, pg. 8). Sub-classes exist within each category but Safeguards reference the top-level class only.
    """
    Devices = PermissibleValue(
        text="Devices",
        description="""Enterprise assets (data processing and storage assets), end-user devices (including portable and mobile devices), servers, Internet of Things (IoT) and non-computing devices, network devices, and removable media. Devices may exist in physical, virtual, or cloud-based environments and can remotely connect to these systems.""")
    Software = PermissibleValue(
        text="Software",
        description="""Sets of data and instructions used to direct a computer to complete a specific task. Includes applications, operating systems (with their services, libraries, and APIs), and firmware. Both applications and operating systems are considered software assets.""")
    Data = PermissibleValue(
        text="Data",
        description="""A collection of facts that can be examined, considered, and used for decision-making. Although data may be physical, the CIS Controls primarily provide protection for digital data stored, transferred, and processed by enterprise assets. Sub-classes: sensitive data, log data, and physical data.""")
    Users = PermissibleValue(
        text="Users",
        description="""Employees, third-party vendors, contractors, service providers, consultants, or any other person authorized to access an enterprise asset. Includes workforce, service providers, and user/administrator/service accounts.""")
    Network = PermissibleValue(
        text="Network",
        description="""A group of interconnected devices that exchange data. A superset of network infrastructure (hardware and software providing connectivity and communication) and network architecture (the logical and physical design of the network).""")
    Documentation = PermissibleValue(
        text="Documentation",
        description="""Policies, processes, procedures, plans, diagrams, and other written material (physical or digital), such as compliance reports. Examples include methods of governance for an enterprise, processes users follow, or descriptions of network architecture. Sub-classes: plans, policies, processes, and procedures.""")

    _defn = EnumDefinition(
        name="AssetType",
        description="""The category of enterprise asset primarily addressed by a Safeguard. Aligned with the CIS Controls Asset Classes taxonomy (v8.1, pg. 8). Sub-classes exist within each category but Safeguards reference the top-level class only.""",
    )

class SecurityFunction(EnumDefinitionImpl):
    """
    NIST Cybersecurity Framework 2.0 security function category to which a Safeguard is primarily mapped. Values
    correspond exactly to the six CSF 2.0 Functions; enum as a whole is a close match for nist_csf_v2:CSFFunction.
    """
    Govern = PermissibleValue(
        text="Govern",
        description="""Establish and monitor the organization's cybersecurity risk management strategy, expectations, and policy.""",
        meaning=NIST_CSF_V2["GV"])
    Identify = PermissibleValue(
        text="Identify",
        description="""Develop an organizational understanding of cybersecurity risk to systems, people, assets, data, and capabilities.""",
        meaning=NIST_CSF_V2["ID"])
    Protect = PermissibleValue(
        text="Protect",
        description="Develop and implement appropriate safeguards to ensure delivery of critical services.",
        meaning=NIST_CSF_V2["PR"])
    Detect = PermissibleValue(
        text="Detect",
        description="""Develop and implement appropriate activities to identify the occurrence of a cybersecurity event.""",
        meaning=NIST_CSF_V2["DE"])
    Respond = PermissibleValue(
        text="Respond",
        description="""Develop and implement appropriate activities to take action regarding a detected cybersecurity incident.""",
        meaning=NIST_CSF_V2["RS"])
    Recover = PermissibleValue(
        text="Recover",
        description="""Develop and implement appropriate activities to maintain plans for resilience and to restore capabilities impaired by a cybersecurity incident.""",
        meaning=NIST_CSF_V2["RC"])

    _defn = EnumDefinition(
        name="SecurityFunction",
        description="""NIST Cybersecurity Framework 2.0 security function category to which a Safeguard is primarily mapped. Values correspond exactly to the six CSF 2.0 Functions; enum as a whole is a close match for nist_csf_v2:CSFFunction.""",
    )

# Slots
class slots:
    pass

slots.id = Slot(uri=DCT.identifier, name="id", curie=DCT.curie('identifier'),
                   model_uri=CIS_CONTROLS.id, domain=None, range=URIRef)

slots.title = Slot(uri=DCT.title, name="title", curie=DCT.curie('title'),
                   model_uri=CIS_CONTROLS.title, domain=None, range=str)

slots.description = Slot(uri=DCT.description, name="description", curie=DCT.curie('description'),
                   model_uri=CIS_CONTROLS.description, domain=None, range=Optional[str])

slots.overview = Slot(uri=CIS_CONTROLS.overview, name="overview", curie=CIS_CONTROLS.curie('overview'),
                   model_uri=CIS_CONTROLS.overview, domain=None, range=Optional[str])

slots.why_critical = Slot(uri=CIS_CONTROLS.why_critical, name="why_critical", curie=CIS_CONTROLS.curie('why_critical'),
                   model_uri=CIS_CONTROLS.why_critical, domain=None, range=Optional[str])

slots.procedures_and_tools = Slot(uri=CIS_CONTROLS.procedures_and_tools, name="procedures_and_tools", curie=CIS_CONTROLS.curie('procedures_and_tools'),
                   model_uri=CIS_CONTROLS.procedures_and_tools, domain=None, range=Optional[str])

slots.control_number = Slot(uri=CIS_CONTROLS.control_number, name="control_number", curie=CIS_CONTROLS.curie('control_number'),
                   model_uri=CIS_CONTROLS.control_number, domain=None, range=str)

slots.safeguard_number = Slot(uri=CIS_CONTROLS.safeguard_number, name="safeguard_number", curie=CIS_CONTROLS.curie('safeguard_number'),
                   model_uri=CIS_CONTROLS.safeguard_number, domain=None, range=str)

slots.asset_type = Slot(uri=CIS_CONTROLS.asset_type, name="asset_type", curie=CIS_CONTROLS.curie('asset_type'),
                   model_uri=CIS_CONTROLS.asset_type, domain=None, range=Union[str, "AssetType"])

slots.security_function = Slot(uri=CIS_CONTROLS.security_function, name="security_function", curie=CIS_CONTROLS.curie('security_function'),
                   model_uri=CIS_CONTROLS.security_function, domain=None, range=Union[str, "SecurityFunction"])

slots.implementation_groups = Slot(uri=CIS_CONTROLS.implementation_groups, name="implementation_groups", curie=CIS_CONTROLS.curie('implementation_groups'),
                   model_uri=CIS_CONTROLS.implementation_groups, domain=None, range=Union[Union[str, "ImplementationGroup"], list[Union[str, "ImplementationGroup"]]])

slots.safeguards = Slot(uri=CIS_CONTROLS.safeguards, name="safeguards", curie=CIS_CONTROLS.curie('safeguards'),
                   model_uri=CIS_CONTROLS.safeguards, domain=None, range=Optional[Union[dict[Union[str, SafeguardId], Union[dict, Safeguard]], list[Union[dict, Safeguard]]]])

slots.controls = Slot(uri=CIS_CONTROLS.controls, name="controls", curie=CIS_CONTROLS.curie('controls'),
                   model_uri=CIS_CONTROLS.controls, domain=None, range=Optional[Union[dict[Union[str, CISControlId], Union[dict, CISControl]], list[Union[dict, CISControl]]]])

slots.version = Slot(uri=DCT.hasVersion, name="version", curie=DCT.curie('hasVersion'),
                   model_uri=CIS_CONTROLS.version, domain=None, range=Optional[str])

slots.publication_date = Slot(uri=DCT.date, name="publication_date", curie=DCT.curie('date'),
                   model_uri=CIS_CONTROLS.publication_date, domain=None, range=Optional[str])

slots.CISControl_id = Slot(uri=DCT.identifier, name="CISControl_id", curie=DCT.curie('identifier'),
                   model_uri=CIS_CONTROLS.CISControl_id, domain=CISControl, range=Union[str, CISControlId],
                   pattern=re.compile(r'^CIS-([1-9]|1[0-8])$'))

slots.Safeguard_id = Slot(uri=DCT.identifier, name="Safeguard_id", curie=DCT.curie('identifier'),
                   model_uri=CIS_CONTROLS.Safeguard_id, domain=Safeguard, range=Union[str, SafeguardId],
                   pattern=re.compile(r'^CIS-([1-9]|1[0-8])\.[0-9]+$'))

slots.Safeguard_implementation_groups = Slot(uri=CIS_CONTROLS.implementation_groups, name="Safeguard_implementation_groups", curie=CIS_CONTROLS.curie('implementation_groups'),
                   model_uri=CIS_CONTROLS.Safeguard_implementation_groups, domain=Safeguard, range=Union[Union[str, "ImplementationGroup"], list[Union[str, "ImplementationGroup"]]])
