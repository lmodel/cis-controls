# Auto generated from cis_controls.yaml by pythongen.py version: 0.0.1
# Schema: cis_controls
#
# id: https://w3id.org/lmodel/cis-controls
# description: A LinkML model of the structure of the CIS Critical Security Controls (CIS Controls), Version 8.1, which the Center for Internet Security (CIS) publishes: its Controls, the Safeguards of each Control, and for each Safeguard its asset class, its security function and the Implementation Groups that include it. It names each Control and Safeguard by its number and carries none of CIS's text.
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

metamodel_version = "1.12.0"
version = "8.1.2"

# Namespaces
CIS_CONTROLS = CurieNamespace('cis_controls', 'https://w3id.org/lmodel/cis-controls/')
LINKML = CurieNamespace('linkml', 'https://w3id.org/linkml/')
NIST_CSF_V2 = CurieNamespace('nist_csf_v2', 'https://w3id.org/lmodel/nist-csf-v2/')
OSCAL = CurieNamespace('oscal', 'https://w3id.org/lmodel/oscal/')
SCHEMA = CurieNamespace('schema', 'http://schema.org/')
XSD = CurieNamespace('xsd', 'http://www.w3.org/2001/XMLSchema#')
DEFAULT_ = CIS_CONTROLS


# Types
class CisControlIdentifier(String):
    """ A Control's identifier: CIS, a hyphen and the Control's number from 1 to 18, such as CIS-4 for Control 4. """
    type_class_uri = XSD["string"]
    type_class_curie = "xsd:string"
    type_name = "cis_control_identifier"
    type_model_uri = CIS_CONTROLS.CisControlIdentifier


class CisSafeguardIdentifier(String):
    """ A Safeguard's identifier: CIS, a hyphen, the number of its Control, a dot and the Safeguard's number within the Control, such as CIS-4.1 for Safeguard 4.1. """
    type_class_uri = XSD["string"]
    type_class_curie = "xsd:string"
    type_name = "cis_safeguard_identifier"
    type_model_uri = CIS_CONTROLS.CisSafeguardIdentifier


# Class references



@dataclass(repr=False)
class CisControls(YAMLRoot):
    """
    One edition of the CIS Controls as a whole: its Controls, each holding its Safeguards.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CIS_CONTROLS["Controls"]
    class_class_curie: ClassVar[str] = "cis_controls:Controls"
    class_name: ClassVar[str] = "CisControls"
    class_model_uri: ClassVar[URIRef] = CIS_CONTROLS.CisControls

    cis_version: str = None
    cis_controls: Union[Union[dict, "CisControl"], list[Union[dict, "CisControl"]]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.cis_version):
            self.MissingRequiredField("cis_version")
        if not isinstance(self.cis_version, str):
            self.cis_version = str(self.cis_version)

        if self._is_empty(self.cis_controls):
            self.MissingRequiredField("cis_controls")
        self._normalize_inlined_as_list(slot_name="cis_controls", slot_type=CisControl, key_name="cis_control_id", keyed=False)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class CisControl(YAMLRoot):
    """
    One of the CIS Controls: a group of Safeguards on one subject, named by its number, such as Control 4.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CIS_CONTROLS["Control"]
    class_class_curie: ClassVar[str] = "cis_controls:Control"
    class_name: ClassVar[str] = "CisControl"
    class_model_uri: ClassVar[URIRef] = CIS_CONTROLS.CisControl

    cis_control_id: Union[str, CisControlIdentifier] = None
    title: Optional[str] = None
    description: Optional[str] = None
    control_safeguards: Optional[Union[Union[dict, "CisSafeguard"], list[Union[dict, "CisSafeguard"]]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.cis_control_id):
            self.MissingRequiredField("cis_control_id")
        if not isinstance(self.cis_control_id, CisControlIdentifier):
            self.cis_control_id = CisControlIdentifier(self.cis_control_id)

        if self.title is not None and not isinstance(self.title, str):
            self.title = str(self.title)

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        self._normalize_inlined_as_list(slot_name="control_safeguards", slot_type=CisSafeguard, key_name="cis_safeguard_id", keyed=False)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class CisSafeguard(YAMLRoot):
    """
    One Safeguard of a Control: a single action an enterprise takes, named by its Control's number and its own, such
    as Safeguard 4.1.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CIS_CONTROLS["Safeguard"]
    class_class_curie: ClassVar[str] = "cis_controls:Safeguard"
    class_name: ClassVar[str] = "CisSafeguard"
    class_model_uri: ClassVar[URIRef] = CIS_CONTROLS.CisSafeguard

    cis_safeguard_id: Union[str, CisSafeguardIdentifier] = None
    safeguard_asset_class: Union[str, "CisAssetClass"] = None
    safeguard_security_function: Union[str, "CisSecurityFunction"] = None
    safeguard_implementation_groups: Union[Union[str, "CisImplementationGroup"], list[Union[str, "CisImplementationGroup"]]] = None
    title: Optional[str] = None
    description: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.cis_safeguard_id):
            self.MissingRequiredField("cis_safeguard_id")
        if not isinstance(self.cis_safeguard_id, CisSafeguardIdentifier):
            self.cis_safeguard_id = CisSafeguardIdentifier(self.cis_safeguard_id)

        if self._is_empty(self.safeguard_asset_class):
            self.MissingRequiredField("safeguard_asset_class")
        if not isinstance(self.safeguard_asset_class, CisAssetClass):
            self.safeguard_asset_class = CisAssetClass(self.safeguard_asset_class)

        if self._is_empty(self.safeguard_security_function):
            self.MissingRequiredField("safeguard_security_function")
        if not isinstance(self.safeguard_security_function, CisSecurityFunction):
            self.safeguard_security_function = CisSecurityFunction(self.safeguard_security_function)

        if self._is_empty(self.safeguard_implementation_groups):
            self.MissingRequiredField("safeguard_implementation_groups")
        if not isinstance(self.safeguard_implementation_groups, list):
            self.safeguard_implementation_groups = [self.safeguard_implementation_groups] if self.safeguard_implementation_groups is not None else []
        self.safeguard_implementation_groups = [v if isinstance(v, CisImplementationGroup) else CisImplementationGroup(v) for v in self.safeguard_implementation_groups]

        if self.title is not None and not isinstance(self.title, str):
            self.title = str(self.title)

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        super().__post_init__(**kwargs)


# Enumerations
class CisImplementationGroup(EnumDefinitionImpl):
    """
    One of the three Implementation Groups, CIS's tiers for deciding which Safeguards an enterprise puts in place
    first. Each group includes every Safeguard of the groups before it.
    """
    IG1 = PermissibleValue(
        text="IG1",
        title="Implementation Group 1",
        description="The first group, where every enterprise starts.")
    IG2 = PermissibleValue(
        text="IG2",
        title="Implementation Group 2",
        description="The second group, which adds Safeguards to the first.")
    IG3 = PermissibleValue(
        text="IG3",
        title="Implementation Group 3",
        description="The third group, which adds the rest and so holds every Safeguard.")

    _defn = EnumDefinition(
        name="CisImplementationGroup",
        description="""One of the three Implementation Groups, CIS's tiers for deciding which Safeguards an enterprise puts in place first. Each group includes every Safeguard of the groups before it.""",
    )

class CisAssetClass(EnumDefinitionImpl):
    """
    One of the classes of enterprise asset that the CIS Controls sort their Safeguards by. Each Safeguard is about one
    class.
    """
    DEVICES = PermissibleValue(
        text="DEVICES",
        title="Devices",
        description="The enterprise's hardware, wherever it runs.")
    SOFTWARE = PermissibleValue(
        text="SOFTWARE",
        title="Software",
        description="The programs and systems that run on the enterprise's devices.")
    DATA = PermissibleValue(
        text="DATA",
        title="Data",
        description="The information the enterprise holds, uses and moves.")
    USERS = PermissibleValue(
        text="USERS",
        title="Users",
        description="The people and accounts with access to the enterprise's assets.")
    NETWORK = PermissibleValue(
        text="NETWORK",
        title="Network",
        description="How the enterprise's devices connect, and how its networks are laid out.")
    DOCUMENTATION = PermissibleValue(
        text="DOCUMENTATION",
        title="Documentation",
        description="The enterprise's written governance, such as its policies and procedures.")

    _defn = EnumDefinition(
        name="CisAssetClass",
        description="""One of the classes of enterprise asset that the CIS Controls sort their Safeguards by. Each Safeguard is about one class.""",
    )

class CisSecurityFunction(EnumDefinitionImpl):
    """
    The security function a Safeguard serves. The values are the six functions of the NIST Cybersecurity Framework
    (CSF) 2.0, to which Version 8.1 aligned the CIS Controls.
    """
    GOVERN = PermissibleValue(
        text="GOVERN",
        title="Govern",
        description="The CSF 2.0 function GOVERN.")
    IDENTIFY = PermissibleValue(
        text="IDENTIFY",
        title="Identify",
        description="The CSF 2.0 function IDENTIFY.")
    PROTECT = PermissibleValue(
        text="PROTECT",
        title="Protect",
        description="The CSF 2.0 function PROTECT.")
    DETECT = PermissibleValue(
        text="DETECT",
        title="Detect",
        description="The CSF 2.0 function DETECT.")
    RESPOND = PermissibleValue(
        text="RESPOND",
        title="Respond",
        description="The CSF 2.0 function RESPOND.")
    RECOVER = PermissibleValue(
        text="RECOVER",
        title="Recover",
        description="The CSF 2.0 function RECOVER.")

    _defn = EnumDefinition(
        name="CisSecurityFunction",
        description="""The security function a Safeguard serves. The values are the six functions of the NIST Cybersecurity Framework (CSF) 2.0, to which Version 8.1 aligned the CIS Controls.""",
    )

# Slots
class slots:
    pass

slots.cis_control_id = Slot(uri=CIS_CONTROLS.cis_control_id, name="cis_control_id", curie=CIS_CONTROLS.curie('cis_control_id'),
                   model_uri=CIS_CONTROLS.cis_control_id, domain=None, range=Union[str, CisControlIdentifier])

slots.cis_safeguard_id = Slot(uri=CIS_CONTROLS.cis_safeguard_id, name="cis_safeguard_id", curie=CIS_CONTROLS.curie('cis_safeguard_id'),
                   model_uri=CIS_CONTROLS.cis_safeguard_id, domain=None, range=Union[str, CisSafeguardIdentifier])

slots.title = Slot(uri=SCHEMA.name, name="title", curie=SCHEMA.curie('name'),
                   model_uri=CIS_CONTROLS.title, domain=None, range=Optional[str])

slots.description = Slot(uri=SCHEMA.description, name="description", curie=SCHEMA.curie('description'),
                   model_uri=CIS_CONTROLS.description, domain=None, range=Optional[str])

slots.cisControls__cis_version = Slot(uri=CIS_CONTROLS.cis_version, name="cisControls__cis_version", curie=CIS_CONTROLS.curie('cis_version'),
                   model_uri=CIS_CONTROLS.cisControls__cis_version, domain=None, range=str,
                   pattern=re.compile(r'^[0-9]+\.[0-9]+(\.[0-9]+)?$'))

slots.cisControls__cis_controls = Slot(uri=CIS_CONTROLS.cis_controls, name="cisControls__cis_controls", curie=CIS_CONTROLS.curie('cis_controls'),
                   model_uri=CIS_CONTROLS.cisControls__cis_controls, domain=None, range=Union[Union[dict, CisControl], list[Union[dict, CisControl]]])

slots.cisControl__control_safeguards = Slot(uri=CIS_CONTROLS.control_safeguards, name="cisControl__control_safeguards", curie=CIS_CONTROLS.curie('control_safeguards'),
                   model_uri=CIS_CONTROLS.cisControl__control_safeguards, domain=None, range=Optional[Union[Union[dict, CisSafeguard], list[Union[dict, CisSafeguard]]]])

slots.cisSafeguard__safeguard_asset_class = Slot(uri=CIS_CONTROLS.safeguard_asset_class, name="cisSafeguard__safeguard_asset_class", curie=CIS_CONTROLS.curie('safeguard_asset_class'),
                   model_uri=CIS_CONTROLS.cisSafeguard__safeguard_asset_class, domain=None, range=Union[str, "CisAssetClass"])

slots.cisSafeguard__safeguard_security_function = Slot(uri=CIS_CONTROLS.safeguard_security_function, name="cisSafeguard__safeguard_security_function", curie=CIS_CONTROLS.curie('safeguard_security_function'),
                   model_uri=CIS_CONTROLS.cisSafeguard__safeguard_security_function, domain=None, range=Union[str, "CisSecurityFunction"])

slots.cisSafeguard__safeguard_implementation_groups = Slot(uri=CIS_CONTROLS.safeguard_implementation_groups, name="cisSafeguard__safeguard_implementation_groups", curie=CIS_CONTROLS.curie('safeguard_implementation_groups'),
                   model_uri=CIS_CONTROLS.cisSafeguard__safeguard_implementation_groups, domain=None, range=Union[Union[str, "CisImplementationGroup"], list[Union[str, "CisImplementationGroup"]]])
