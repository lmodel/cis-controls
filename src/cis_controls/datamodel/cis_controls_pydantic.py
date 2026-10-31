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


metamodel_version = "1.12.0"
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


linkml_meta = LinkMLMeta({'annotations': {'cis_site_version': {'tag': 'cis_site_version',
                                          'value': '8.1'},
                     'pages_read_on': {'tag': 'pages_read_on',
                                       'value': '2026-10-30'},
                     'revision_date': {'tag': 'revision_date', 'value': '2025-03'}},
     'comments': ["The version is the label that the pages of CIS's guide carry "
                  "for its revision of March 2025. CIS's site calls the edition "
                  "Version 8.1. The guide's change log names two minor revisions "
                  'of it, v8.1.1 in August 2024 and v8.1.2 in March 2025. They '
                  'corrected small errors, among them the security function of two '
                  "Safeguards. The source is CIS's page for Version 8.1. "
                  'scripts/check_upstream_release.py holds the same pins and '
                  "reports when CIS's pages name a newer version.",
                  'CIS licenses the CIS Controls under CC BY-NC-ND 4.0 and '
                  'requires its prior approval for commercial use, while this '
                  'schema is Apache-2.0. So the schema carries no CIS text: none '
                  "of the guide's titles, descriptions, overviews or explanations. "
                  "The descriptions here are this project's own words, and so are "
                  'the title and description that '
                  'src/cis_controls/data/cis-controls-8.1.2.yaml gives each '
                  'Control and Safeguard, written from what each requires. The '
                  'text slots, title and description, are optional and hold text '
                  'their user has the right to use; NOTICE states the position.',
                  'The edition holds 18 Controls and 153 Safeguards. '
                  'Implementation Group 1 holds 56 of the Safeguards, '
                  'Implementation Group 2 adds 74 to make 130, and Implementation '
                  "Group 3 adds the last 23, so it holds all 153. CIS's pages on "
                  'the CIS Controls list and on each Implementation Group state '
                  'these numbers.'],
     'default_prefix': 'cis_controls',
     'default_range': 'string',
     'description': 'A LinkML model of the structure of the CIS Critical Security '
                    'Controls (CIS Controls), Version 8.1, which the Center for '
                    'Internet Security (CIS) publishes. It models the Controls and '
                    'the Safeguards of each Control. For each Safeguard it records '
                    'the asset class, the security function and the Implementation '
                    'Groups that include it. It names each Control and Safeguard '
                    "by its number and carries none of CIS's text.",
     'id': 'https://w3id.org/lmodel/cis-controls',
     'imports': ['linkml:types'],
     'license': 'Apache-2.0',
     'name': 'cis_controls',
     'prefixes': {'cis_controls': {'prefix_prefix': 'cis_controls',
                                   'prefix_reference': 'https://w3id.org/lmodel/cis-controls/'},
                  'linkml': {'prefix_prefix': 'linkml',
                             'prefix_reference': 'https://w3id.org/linkml/'},
                  'nist_csf_v2': {'prefix_prefix': 'nist_csf_v2',
                                  'prefix_reference': 'https://w3id.org/lmodel/nist-csf-v2/'},
                  'oscal': {'prefix_prefix': 'oscal',
                            'prefix_reference': 'https://w3id.org/lmodel/oscal/'},
                  'schema': {'prefix_prefix': 'schema',
                             'prefix_reference': 'http://schema.org/'},
                  'xsd': {'prefix_prefix': 'xsd',
                          'prefix_reference': 'http://www.w3.org/2001/XMLSchema#'}},
     'see_also': ['https://lmodel.github.io/cis-controls',
                  'https://www.cisecurity.org/controls/cis-controls-list',
                  'https://www.cisecurity.org/controls/implementation-groups',
                  'https://www.cisecurity.org/insights/white-papers/guide-to-asset-classes-cis-critical-security-controls-v8-1'],
     'source': 'https://www.cisecurity.org/controls/v8-1',
     'source_file': 'src/cis_controls/schema/cis_controls.yaml',
     'title': 'CIS Critical Security Controls',
     'types': {'cis_control_identifier': {'base': 'str',
                                          'description': "A Control's identifier: "
                                                         'its number from 1 to 18, '
                                                         'as CIS writes it, such '
                                                         'as 4 for Control 4.',
                                          'from_schema': 'https://w3id.org/lmodel/cis-controls',
                                          'name': 'cis_control_identifier',
                                          'pattern': '^([1-9]|1[0-8])$',
                                          'typeof': 'string',
                                          'uri': 'xsd:string'},
               'cis_safeguard_identifier': {'base': 'str',
                                            'description': "A Safeguard's "
                                                           'identifier, as CIS '
                                                           'writes it: the number '
                                                           'of its Control, a dot '
                                                           "and the Safeguard's "
                                                           'number within the '
                                                           'Control, such as 4.1 '
                                                           'for Safeguard 4.1.',
                                            'from_schema': 'https://w3id.org/lmodel/cis-controls',
                                            'name': 'cis_safeguard_identifier',
                                            'pattern': '^([1-9]|1[0-8])\\.[1-9][0-9]?$',
                                            'typeof': 'string',
                                            'uri': 'xsd:string'}}} )

class CisImplementationGroup(str, Enum):
    """
    One of the three Implementation Groups, CIS's tiers for deciding which Safeguards an enterprise puts in place first. Each group includes every Safeguard of the groups before it.
    """
    Implementation_Group_1 = "IG1"
    """
    The first group, where every enterprise starts.
    """
    Implementation_Group_2 = "IG2"
    """
    The second group, which adds Safeguards to the first.
    """
    Implementation_Group_3 = "IG3"
    """
    The third group, which adds the rest and so holds every Safeguard.
    """


class CisAssetClass(str, Enum):
    """
    One of the classes of enterprise asset that the CIS Controls sort their Safeguards by. Each Safeguard is about one class.
    """
    Devices = "DEVICES"
    """
    The enterprise's hardware, wherever it runs.
    """
    Software = "SOFTWARE"
    """
    The programs and systems that run on the enterprise's devices.
    """
    Data = "DATA"
    """
    The information the enterprise holds, uses and moves.
    """
    Users = "USERS"
    """
    The people and accounts with access to the enterprise's assets.
    """
    Network = "NETWORK"
    """
    How the enterprise's devices connect, and how its networks are laid out.
    """
    Documentation = "DOCUMENTATION"
    """
    The enterprise's written governance, such as its policies and procedures.
    """


class CisSecurityFunction(str, Enum):
    """
    The security function a Safeguard serves. The values are the six functions of the NIST Cybersecurity Framework (CSF) 2.0, to which Version 8.1 aligned the CIS Controls.
    """
    Govern = "GOVERN"
    """
    The CSF 2.0 function GOVERN.
    """
    Identify = "IDENTIFY"
    """
    The CSF 2.0 function IDENTIFY.
    """
    Protect = "PROTECT"
    """
    The CSF 2.0 function PROTECT.
    """
    Detect = "DETECT"
    """
    The CSF 2.0 function DETECT.
    """
    Respond = "RESPOND"
    """
    The CSF 2.0 function RESPOND.
    """
    Recover = "RECOVER"
    """
    The CSF 2.0 function RECOVER.
    """



class CisControls(ConfiguredBaseModel):
    """
    One edition of the CIS Controls as a whole: its Controls, each holding its Safeguards.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'broad_mappings': ['oscal:Catalog'],
         'class_uri': 'cis_controls:Controls',
         'from_schema': 'https://w3id.org/lmodel/cis-controls',
         'see_also': ['https://www.cisecurity.org/controls/cis-controls-list'],
         'tree_root': True})

    cis_version: str = Field(default=..., description="""The edition, as CIS numbers it, such as 8.1, or the revision the guide's pages carry, such as 8.1.2.""", json_schema_extra = { "linkml_meta": {'domain_of': ['CisControls']} })
    cis_controls: list[CisControl] = Field(default=..., description="""The Controls, in CIS's order.""", min_length=1, json_schema_extra = { "linkml_meta": {'domain_of': ['CisControls']} })

    @field_validator('cis_version')
    def pattern_cis_version(cls, v):
        pattern=re.compile(r"^[0-9]+\.[0-9]+(\.[0-9]+)?$")
        if isinstance(v, list):
            for element in v:
                if isinstance(element, str) and not pattern.search(element):
                    err_msg = f"Invalid cis_version format: {element}"
                    raise ValueError(err_msg)
        elif isinstance(v, str) and not pattern.search(v):
            err_msg = f"Invalid cis_version format: {v}"
            raise ValueError(err_msg)
        return v


class CisControl(ConfiguredBaseModel):
    """
    One of the CIS Controls: a group of Safeguards on one subject, named by its number, such as Control 4.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'broad_mappings': ['oscal:Group'],
         'class_uri': 'cis_controls:Control',
         'from_schema': 'https://w3id.org/lmodel/cis-controls',
         'see_also': ['https://www.cisecurity.org/controls/cis-controls-list']})

    cis_control_id: str = Field(default=..., description="""The Control's identifier, its number, such as 4.""", json_schema_extra = { "linkml_meta": {'comments': ["The identifier is CIS's own number, so data joins with CIS's "
                      'guide and with the crosswalks that cite it without a '
                      'translation. It is a string, so quote it in YAML: YAML reads an '
                      'unquoted 4 as a number and an unquoted 1.10 as the number 1.1. '
                      'The validator rejects either as not a string, but a file loaded '
                      'into the generated dataclasses without validation would turn '
                      '1.10 into 1.1.'],
         'domain_of': ['CisControl']} })
    title: Optional[str] = Field(default=None, description="""A name for the Control or Safeguard, in words its user has the right to use.""", json_schema_extra = { "linkml_meta": {'comments': ["It means what LOKF's title means and carries the same IRI, so "
                      "lokf adapt folds it into LOKF's slot and a knowledge bundle "
                      'reads one title key.',
                      "CIS's own names for the Controls and Safeguards are CIS's text "
                      "under CC BY-NC-ND 4.0, so the schema's examples leave them out, "
                      "and the edition file names each element in this project's "
                      'words.'],
         'domain_of': ['CisControl', 'CisSafeguard'],
         'slot_uri': 'schema:name'} })
    description: Optional[str] = Field(default=None, description="""What the Control or Safeguard means to its user, in words its user has the right to use.""", json_schema_extra = { "linkml_meta": {'comments': ["It means what LOKF's description means and carries the same "
                      "IRI, so lokf adapt folds it into LOKF's slot and a knowledge "
                      'bundle reads one description key.'],
         'domain_of': ['CisControl', 'CisSafeguard'],
         'slot_uri': 'schema:description'} })
    control_safeguards: Optional[list[CisSafeguard]] = Field(default=None, description="""The Safeguards of the Control. A knowledge bundle relates a Safeguard to its Control with isPartOf instead.""", json_schema_extra = { "linkml_meta": {'domain_of': ['CisControl']} })


class CisSafeguard(ConfiguredBaseModel):
    """
    One Safeguard of a Control: a single action an enterprise takes, named by its Control's number and its own, such as Safeguard 4.1.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'broad_mappings': ['oscal:Control'],
         'class_uri': 'cis_controls:Safeguard',
         'from_schema': 'https://w3id.org/lmodel/cis-controls',
         'see_also': ['https://www.cisecurity.org/controls/cis-controls-list']})

    cis_safeguard_id: str = Field(default=..., description="""The Safeguard's identifier, its number, such as 4.1.""", json_schema_extra = { "linkml_meta": {'comments': ['It starts with the number of the Control that holds the '
                      'Safeguard. The validator cannot check that against the Control '
                      'a Safeguard is listed under; tests/test_data.py checks it over '
                      'the examples.'],
         'domain_of': ['CisSafeguard']} })
    title: Optional[str] = Field(default=None, description="""A name for the Control or Safeguard, in words its user has the right to use.""", json_schema_extra = { "linkml_meta": {'comments': ["It means what LOKF's title means and carries the same IRI, so "
                      "lokf adapt folds it into LOKF's slot and a knowledge bundle "
                      'reads one title key.',
                      "CIS's own names for the Controls and Safeguards are CIS's text "
                      "under CC BY-NC-ND 4.0, so the schema's examples leave them out, "
                      "and the edition file names each element in this project's "
                      'words.'],
         'domain_of': ['CisControl', 'CisSafeguard'],
         'slot_uri': 'schema:name'} })
    description: Optional[str] = Field(default=None, description="""What the Control or Safeguard means to its user, in words its user has the right to use.""", json_schema_extra = { "linkml_meta": {'comments': ["It means what LOKF's description means and carries the same "
                      "IRI, so lokf adapt folds it into LOKF's slot and a knowledge "
                      'bundle reads one description key.'],
         'domain_of': ['CisControl', 'CisSafeguard'],
         'slot_uri': 'schema:description'} })
    safeguard_asset_class: CisAssetClass = Field(default=..., description="""The class of enterprise asset the Safeguard is about.""", json_schema_extra = { "linkml_meta": {'domain_of': ['CisSafeguard']} })
    safeguard_security_function: CisSecurityFunction = Field(default=..., description="""The security function the Safeguard serves, one of the six functions of the NIST Cybersecurity Framework (CSF) 2.0.""", json_schema_extra = { "linkml_meta": {'domain_of': ['CisSafeguard']} })
    safeguard_implementation_groups: list[CisImplementationGroup] = Field(default=..., description="""The Implementation Groups that include the Safeguard.""", min_length=1, max_length=3, json_schema_extra = { "linkml_meta": {'comments': ['The groups are cumulative: a Safeguard in IG1 is in IG2 and IG3 '
                      'too, and one in IG2 is in IG3. The schema states the part of '
                      'that rule the validator can check, that every Safeguard is in '
                      'IG3. The JSON Schema that LinkML 1.12.1 generates drops the '
                      'rest, so a list of IG1 and IG3 without IG2 passes the '
                      'validator. tests/test_data.py checks the whole rule over the '
                      'examples.'],
         'domain_of': ['CisSafeguard'],
         'has_member': {'equals_string': 'IG3'}} })


# Model rebuild
# see https://pydantic-docs.helpmanual.io/usage/models/#rebuilding-a-model
CisControls.model_rebuild()
CisControl.model_rebuild()
CisSafeguard.model_rebuild()
