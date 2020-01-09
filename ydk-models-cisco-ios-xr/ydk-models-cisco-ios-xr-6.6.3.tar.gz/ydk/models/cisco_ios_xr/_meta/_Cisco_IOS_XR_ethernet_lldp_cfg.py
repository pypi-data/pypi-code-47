
'''
This is auto-generated file,
which includes metadata for module Cisco_IOS_XR_ethernet_lldp_cfg
'''

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_LIST, REFERENCE_LEAFLIST, REFERENCE_BITS, REFERENCE_UNION
from ydk._core._dm_meta_info import REFERENCE_CLASS, REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, ANYXML_CLASS
from ydk._core._importer import _yang_ns

_meta_table = {
    'Lldp.TlvSelect.SystemName' : {
        'meta_info' : _MetaInfoClass('Lldp.TlvSelect.SystemName', REFERENCE_CLASS,
            '''System Name TLV''',
            False, 
            [
            _MetaInfoClassMember('disable', ATTRIBUTE, 'bool', 'boolean',
                None, None,
                [], [],
                '''                disable System Name TLV
                ''',
                'disable',
                'Cisco-IOS-XR-ethernet-lldp-cfg', False, default_value='False'),
            ],
            'Cisco-IOS-XR-ethernet-lldp-cfg',
            'system-name',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-ethernet-lldp-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_lldp_cfg',
        ),
    },
    'Lldp.TlvSelect.PortDescription' : {
        'meta_info' : _MetaInfoClass('Lldp.TlvSelect.PortDescription', REFERENCE_CLASS,
            '''Port Description TLV''',
            False, 
            [
            _MetaInfoClassMember('disable', ATTRIBUTE, 'bool', 'boolean',
                None, None,
                [], [],
                '''                disable Port Description TLV
                ''',
                'disable',
                'Cisco-IOS-XR-ethernet-lldp-cfg', False, default_value='False'),
            ],
            'Cisco-IOS-XR-ethernet-lldp-cfg',
            'port-description',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-ethernet-lldp-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_lldp_cfg',
        ),
    },
    'Lldp.TlvSelect.SystemDescription' : {
        'meta_info' : _MetaInfoClass('Lldp.TlvSelect.SystemDescription', REFERENCE_CLASS,
            '''System Description TLV''',
            False, 
            [
            _MetaInfoClassMember('disable', ATTRIBUTE, 'bool', 'boolean',
                None, None,
                [], [],
                '''                disable System Description TLV
                ''',
                'disable',
                'Cisco-IOS-XR-ethernet-lldp-cfg', False, default_value='False'),
            ],
            'Cisco-IOS-XR-ethernet-lldp-cfg',
            'system-description',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-ethernet-lldp-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_lldp_cfg',
        ),
    },
    'Lldp.TlvSelect.SystemCapabilities' : {
        'meta_info' : _MetaInfoClass('Lldp.TlvSelect.SystemCapabilities', REFERENCE_CLASS,
            '''System Capabilities TLV''',
            False, 
            [
            _MetaInfoClassMember('disable', ATTRIBUTE, 'bool', 'boolean',
                None, None,
                [], [],
                '''                disable System Capabilities TLV
                ''',
                'disable',
                'Cisco-IOS-XR-ethernet-lldp-cfg', False, default_value='False'),
            ],
            'Cisco-IOS-XR-ethernet-lldp-cfg',
            'system-capabilities',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-ethernet-lldp-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_lldp_cfg',
        ),
    },
    'Lldp.TlvSelect.ManagementAddress' : {
        'meta_info' : _MetaInfoClass('Lldp.TlvSelect.ManagementAddress', REFERENCE_CLASS,
            '''Management Address TLV''',
            False, 
            [
            _MetaInfoClassMember('disable', ATTRIBUTE, 'bool', 'boolean',
                None, None,
                [], [],
                '''                disable Management Address TLV
                ''',
                'disable',
                'Cisco-IOS-XR-ethernet-lldp-cfg', False, default_value='False'),
            ],
            'Cisco-IOS-XR-ethernet-lldp-cfg',
            'management-address',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-ethernet-lldp-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_lldp_cfg',
        ),
    },
    'Lldp.TlvSelect' : {
        'meta_info' : _MetaInfoClass('Lldp.TlvSelect', REFERENCE_CLASS,
            '''Selection of LLDP TLVs to disable''',
            False, 
            [
            _MetaInfoClassMember('system-name', REFERENCE_CLASS, 'SystemName', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_lldp_cfg', 'Lldp.TlvSelect.SystemName',
                [], [],
                '''                System Name TLV
                ''',
                'system_name',
                'Cisco-IOS-XR-ethernet-lldp-cfg', False),
            _MetaInfoClassMember('port-description', REFERENCE_CLASS, 'PortDescription', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_lldp_cfg', 'Lldp.TlvSelect.PortDescription',
                [], [],
                '''                Port Description TLV
                ''',
                'port_description',
                'Cisco-IOS-XR-ethernet-lldp-cfg', False),
            _MetaInfoClassMember('system-description', REFERENCE_CLASS, 'SystemDescription', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_lldp_cfg', 'Lldp.TlvSelect.SystemDescription',
                [], [],
                '''                System Description TLV
                ''',
                'system_description',
                'Cisco-IOS-XR-ethernet-lldp-cfg', False),
            _MetaInfoClassMember('system-capabilities', REFERENCE_CLASS, 'SystemCapabilities', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_lldp_cfg', 'Lldp.TlvSelect.SystemCapabilities',
                [], [],
                '''                System Capabilities TLV
                ''',
                'system_capabilities',
                'Cisco-IOS-XR-ethernet-lldp-cfg', False),
            _MetaInfoClassMember('management-address', REFERENCE_CLASS, 'ManagementAddress', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_lldp_cfg', 'Lldp.TlvSelect.ManagementAddress',
                [], [],
                '''                Management Address TLV
                ''',
                'management_address',
                'Cisco-IOS-XR-ethernet-lldp-cfg', False),
            _MetaInfoClassMember('tlv-select-enter', ATTRIBUTE, 'bool', 'boolean',
                None, None,
                [], [],
                '''                enter lldp tlv-select submode
                ''',
                'tlv_select_enter',
                'Cisco-IOS-XR-ethernet-lldp-cfg', False, is_mandatory=True),
            ],
            'Cisco-IOS-XR-ethernet-lldp-cfg',
            'tlv-select',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-ethernet-lldp-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_lldp_cfg',
            is_presence=True,
        ),
    },
    'Lldp' : {
        'meta_info' : _MetaInfoClass('Lldp', REFERENCE_CLASS,
            '''Enable LLDP, or configure global LLDP subcommands''',
            False, 
            [
            _MetaInfoClassMember('tlv-select', REFERENCE_CLASS, 'TlvSelect', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_lldp_cfg', 'Lldp.TlvSelect',
                [], [],
                '''                Selection of LLDP TLVs to disable
                ''',
                'tlv_select',
                'Cisco-IOS-XR-ethernet-lldp-cfg', False, is_presence=True),
            _MetaInfoClassMember('holdtime', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('0', '65535')], [],
                '''                Length  of time  (in sec) that receiver must
                keep this packet
                ''',
                'holdtime',
                'Cisco-IOS-XR-ethernet-lldp-cfg', False),
            _MetaInfoClassMember('enable-priority-addr', ATTRIBUTE, 'bool', 'boolean',
                None, None,
                [], [],
                '''                Enable or disable Priority to advertise
                Mgmt-interface Addr First
                ''',
                'enable_priority_addr',
                'Cisco-IOS-XR-ethernet-lldp-cfg', False, default_value='False'),
            _MetaInfoClassMember('extended-show-width', ATTRIBUTE, 'bool', 'boolean',
                None, None,
                [], [],
                '''                Enable or disable LLDP Show LLDP Neighbor
                Extended Width
                ''',
                'extended_show_width',
                'Cisco-IOS-XR-ethernet-lldp-cfg', False, default_value='False'),
            _MetaInfoClassMember('enable-subintf', ATTRIBUTE, 'bool', 'boolean',
                None, None,
                [], [],
                '''                Enable or disable LLDP on Sub-interfaces as well
                globally
                ''',
                'enable_subintf',
                'Cisco-IOS-XR-ethernet-lldp-cfg', False, default_value='False'),
            _MetaInfoClassMember('enable-mgmtintf', ATTRIBUTE, 'bool', 'boolean',
                None, None,
                [], [],
                '''                Enable or disable LLDP on Mgmt interfaces as
                well globally
                ''',
                'enable_mgmtintf',
                'Cisco-IOS-XR-ethernet-lldp-cfg', False, default_value='False'),
            _MetaInfoClassMember('timer', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('5', '65534')], [],
                '''                Specify the rate at which LLDP packets are sent
                (in sec)
                ''',
                'timer',
                'Cisco-IOS-XR-ethernet-lldp-cfg', False, default_value="30"),
            _MetaInfoClassMember('reinit', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('2', '5')], [],
                '''                Delay (in sec) for LLDP initialization on any
                interface
                ''',
                'reinit',
                'Cisco-IOS-XR-ethernet-lldp-cfg', False, default_value="2"),
            _MetaInfoClassMember('enable', ATTRIBUTE, 'bool', 'boolean',
                None, None,
                [], [],
                '''                Enable or disable LLDP globally
                ''',
                'enable',
                'Cisco-IOS-XR-ethernet-lldp-cfg', False, default_value='False'),
            ],
            'Cisco-IOS-XR-ethernet-lldp-cfg',
            'lldp',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-ethernet-lldp-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_lldp_cfg',
        ),
    },
}
_meta_table['Lldp.TlvSelect.SystemName']['meta_info'].parent =_meta_table['Lldp.TlvSelect']['meta_info']
_meta_table['Lldp.TlvSelect.PortDescription']['meta_info'].parent =_meta_table['Lldp.TlvSelect']['meta_info']
_meta_table['Lldp.TlvSelect.SystemDescription']['meta_info'].parent =_meta_table['Lldp.TlvSelect']['meta_info']
_meta_table['Lldp.TlvSelect.SystemCapabilities']['meta_info'].parent =_meta_table['Lldp.TlvSelect']['meta_info']
_meta_table['Lldp.TlvSelect.ManagementAddress']['meta_info'].parent =_meta_table['Lldp.TlvSelect']['meta_info']
_meta_table['Lldp.TlvSelect']['meta_info'].parent =_meta_table['Lldp']['meta_info']
