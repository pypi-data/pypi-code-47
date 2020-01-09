
'''
This is auto-generated file,
which includes metadata for module Cisco_IOS_XR_ipv4_arp_cfg
'''

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_LIST, REFERENCE_LEAFLIST, REFERENCE_BITS, REFERENCE_UNION
from ydk._core._dm_meta_info import REFERENCE_CLASS, REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, ANYXML_CLASS
from ydk._core._importer import _yang_ns

_meta_table = {
    'ArpEntry' : _MetaInfoEnum('ArpEntry',
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_arp_cfg', 'ArpEntry',
        '''Arp entry''',
        {
            'static':'static',
            'alias':'alias',
        }, 'Cisco-IOS-XR-ipv4-arp-cfg', _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-ipv4-arp-cfg']),
    'ArpEncap' : _MetaInfoEnum('ArpEncap',
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_arp_cfg', 'ArpEncap',
        '''Arp encap''',
        {
            'arpa':'arpa',
            'srp':'srp',
            'srpa':'srpa',
            'srpb':'srpb',
        }, 'Cisco-IOS-XR-ipv4-arp-cfg', _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-ipv4-arp-cfg']),
    'Arp' : {
        'meta_info' : _MetaInfoClass('Arp', REFERENCE_CLASS,
            '''ARP configuraiton''',
            False, 
            [
            _MetaInfoClassMember('max-entries', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('1', '256000')], [],
                '''                Configure maximum number of safe ARP entries per
                line card
                ''',
                'max_entries',
                'Cisco-IOS-XR-ipv4-arp-cfg', False),
            _MetaInfoClassMember('inner-cos', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('0', '7')], [],
                '''                Configure inner cos values for arp packets
                ''',
                'inner_cos',
                'Cisco-IOS-XR-ipv4-arp-cfg', False),
            _MetaInfoClassMember('outer-cos', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('0', '7')], [],
                '''                Configure outer cos values for arp packets
                ''',
                'outer_cos',
                'Cisco-IOS-XR-ipv4-arp-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-arp-cfg',
            'arp',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-ipv4-arp-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_arp_cfg',
        ),
    },
    'IedgeCfg' : {
        'meta_info' : _MetaInfoClass('IedgeCfg', REFERENCE_CLASS,
            '''iedge cfg''',
            False, 
            [
            _MetaInfoClassMember('subscriber-uncond-proxy', ATTRIBUTE, 'Empty', 'empty',
                None, None,
                [], [],
                '''                ARP Subscriber Enable Unconditional Proxy ARP
                ''',
                'subscriber_uncond_proxy',
                'Cisco-IOS-XR-ipv4-arp-cfg', False),
            _MetaInfoClassMember('subscriber-scale-mode', ATTRIBUTE, 'Empty', 'empty',
                None, None,
                [], [],
                '''                ARP Subscriber Scale Mode Configuration
                ''',
                'subscriber_scale_mode',
                'Cisco-IOS-XR-ipv4-arp-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-arp-cfg',
            'iedge-cfg',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-ipv4-arp-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_arp_cfg',
        ),
    },
    'Arpgmp.Vrf.Entries.Entry' : {
        'meta_info' : _MetaInfoClass('Arpgmp.Vrf.Entries.Entry', REFERENCE_LIST,
            '''ARP static and alias entry configuration item''',
            False, 
            [
            _MetaInfoClassMember('address', ATTRIBUTE, 'str', 'inet:ipv4-address-no-zone',
                None, None,
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'],
                '''                IP Address
                ''',
                'address',
                'Cisco-IOS-XR-ipv4-arp-cfg', True),
            _MetaInfoClassMember('mac-address', ATTRIBUTE, 'str', 'yang:mac-address',
                None, None,
                [], [b'[0-9a-fA-F]{2}(:[0-9a-fA-F]{2}){5}'],
                '''                MAC Address
                ''',
                'mac_address',
                'Cisco-IOS-XR-ipv4-arp-cfg', False),
            _MetaInfoClassMember('encapsulation', REFERENCE_ENUM_CLASS, 'ArpEncap', 'Arp-encap',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_arp_cfg', 'ArpEncap',
                [], [],
                '''                Encapsulation type
                ''',
                'encapsulation',
                'Cisco-IOS-XR-ipv4-arp-cfg', False),
            _MetaInfoClassMember('entry-type', REFERENCE_ENUM_CLASS, 'ArpEntry', 'Arp-entry',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_arp_cfg', 'ArpEntry',
                [], [],
                '''                Entry type
                ''',
                'entry_type',
                'Cisco-IOS-XR-ipv4-arp-cfg', False),
            _MetaInfoClassMember('interface', ATTRIBUTE, 'str', 'xr:Interface-name',
                None, None,
                [], [b'[a-zA-Z0-9._/-]+'],
                '''                Interface name
                ''',
                'interface',
                'Cisco-IOS-XR-ipv4-arp-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-arp-cfg',
            'entry',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-ipv4-arp-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_arp_cfg',
        ),
    },
    'Arpgmp.Vrf.Entries' : {
        'meta_info' : _MetaInfoClass('Arpgmp.Vrf.Entries', REFERENCE_CLASS,
            '''ARP static and alias entry configuration''',
            False, 
            [
            _MetaInfoClassMember('entry', REFERENCE_LIST, 'Entry', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_arp_cfg', 'Arpgmp.Vrf.Entries.Entry',
                [], [],
                '''                ARP static and alias entry configuration item
                ''',
                'entry',
                'Cisco-IOS-XR-ipv4-arp-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-arp-cfg',
            'entries',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-ipv4-arp-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_arp_cfg',
        ),
    },
    'Arpgmp.Vrf' : {
        'meta_info' : _MetaInfoClass('Arpgmp.Vrf', REFERENCE_LIST,
            '''Per VRF configuration, for the default VRF use
'default'''',
            False, 
            [
            _MetaInfoClassMember('vrf-name', ATTRIBUTE, 'str', 'xr:Cisco-ios-xr-string',
                None, None,
                [], [b'[\\w\\-\\.:,_@#%$\\+=\\|;]+'],
                '''                VRF name
                ''',
                'vrf_name',
                'Cisco-IOS-XR-ipv4-arp-cfg', True),
            _MetaInfoClassMember('entries', REFERENCE_CLASS, 'Entries', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_arp_cfg', 'Arpgmp.Vrf.Entries',
                [], [],
                '''                ARP static and alias entry configuration
                ''',
                'entries',
                'Cisco-IOS-XR-ipv4-arp-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-arp-cfg',
            'vrf',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-ipv4-arp-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_arp_cfg',
        ),
    },
    'Arpgmp' : {
        'meta_info' : _MetaInfoClass('Arpgmp', REFERENCE_CLASS,
            '''arpgmp''',
            False, 
            [
            _MetaInfoClassMember('vrf', REFERENCE_LIST, 'Vrf', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_arp_cfg', 'Arpgmp.Vrf',
                [], [],
                '''                Per VRF configuration, for the default VRF use
                'default'
                ''',
                'vrf',
                'Cisco-IOS-XR-ipv4-arp-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-arp-cfg',
            'arpgmp',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-ipv4-arp-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_arp_cfg',
        ),
    },
    'ArpRedundancy.Redundancy.Groups.Group.Peers.Peer' : {
        'meta_info' : _MetaInfoClass('ArpRedundancy.Redundancy.Groups.Group.Peers.Peer', REFERENCE_LIST,
            '''None''',
            False, 
            [
            _MetaInfoClassMember('prefix-string', REFERENCE_UNION, 'str', 'inet:ip-address-no-zone',
                None, None,
                [], [],
                '''                Neighbor IPv4 address
                ''',
                'prefix_string',
                'Cisco-IOS-XR-ipv4-arp-cfg', True, [
                    _MetaInfoClassMember('prefix-string', ATTRIBUTE, 'str', 'inet:ipv4-address-no-zone',
                        None, None,
                        [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'],
                        '''                        Neighbor IPv4 address
                        ''',
                        'prefix_string',
                        'Cisco-IOS-XR-ipv4-arp-cfg', True),
                    _MetaInfoClassMember('prefix-string', ATTRIBUTE, 'str', 'inet:ipv6-address-no-zone',
                        None, None,
                        [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'],
                        '''                        Neighbor IPv4 address
                        ''',
                        'prefix_string',
                        'Cisco-IOS-XR-ipv4-arp-cfg', True),
                ]),
            ],
            'Cisco-IOS-XR-ipv4-arp-cfg',
            'peer',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-ipv4-arp-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_arp_cfg',
        ),
    },
    'ArpRedundancy.Redundancy.Groups.Group.Peers' : {
        'meta_info' : _MetaInfoClass('ArpRedundancy.Redundancy.Groups.Group.Peers', REFERENCE_CLASS,
            '''Table of Peer''',
            False, 
            [
            _MetaInfoClassMember('peer', REFERENCE_LIST, 'Peer', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_arp_cfg', 'ArpRedundancy.Redundancy.Groups.Group.Peers.Peer',
                [], [],
                '''                None
                ''',
                'peer',
                'Cisco-IOS-XR-ipv4-arp-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-arp-cfg',
            'peers',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-ipv4-arp-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_arp_cfg',
        ),
    },
    'ArpRedundancy.Redundancy.Groups.Group.InterfaceList.Interfaces.Interface' : {
        'meta_info' : _MetaInfoClass('ArpRedundancy.Redundancy.Groups.Group.InterfaceList.Interfaces.Interface', REFERENCE_LIST,
            '''Interface for this Group''',
            False, 
            [
            _MetaInfoClassMember('interface-name', ATTRIBUTE, 'str', 'xr:Interface-name',
                None, None,
                [], [b'[a-zA-Z0-9._/-]+'],
                '''                Interface name
                ''',
                'interface_name',
                'Cisco-IOS-XR-ipv4-arp-cfg', True),
            _MetaInfoClassMember('interface-id', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('1', '65535')], [],
                '''                Interface Id for the interface
                ''',
                'interface_id',
                'Cisco-IOS-XR-ipv4-arp-cfg', False, is_mandatory=True),
            ],
            'Cisco-IOS-XR-ipv4-arp-cfg',
            'interface',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-ipv4-arp-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_arp_cfg',
        ),
    },
    'ArpRedundancy.Redundancy.Groups.Group.InterfaceList.Interfaces' : {
        'meta_info' : _MetaInfoClass('ArpRedundancy.Redundancy.Groups.Group.InterfaceList.Interfaces', REFERENCE_CLASS,
            '''Table of Interface''',
            False, 
            [
            _MetaInfoClassMember('interface', REFERENCE_LIST, 'Interface', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_arp_cfg', 'ArpRedundancy.Redundancy.Groups.Group.InterfaceList.Interfaces.Interface',
                [], [],
                '''                Interface for this Group
                ''',
                'interface',
                'Cisco-IOS-XR-ipv4-arp-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-arp-cfg',
            'interfaces',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-ipv4-arp-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_arp_cfg',
        ),
    },
    'ArpRedundancy.Redundancy.Groups.Group.InterfaceList' : {
        'meta_info' : _MetaInfoClass('ArpRedundancy.Redundancy.Groups.Group.InterfaceList', REFERENCE_CLASS,
            '''List of Interfaces for this Group''',
            False, 
            [
            _MetaInfoClassMember('interfaces', REFERENCE_CLASS, 'Interfaces', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_arp_cfg', 'ArpRedundancy.Redundancy.Groups.Group.InterfaceList.Interfaces',
                [], [],
                '''                Table of Interface
                ''',
                'interfaces',
                'Cisco-IOS-XR-ipv4-arp-cfg', False),
            _MetaInfoClassMember('enable', ATTRIBUTE, 'Empty', 'empty',
                None, None,
                [], [],
                '''                Enable List of Interfaces for this Group.
                Deletion of this object also causes deletion
                of all associated objects under
                InterfaceList.
                ''',
                'enable',
                'Cisco-IOS-XR-ipv4-arp-cfg', False, is_mandatory=True),
            ],
            'Cisco-IOS-XR-ipv4-arp-cfg',
            'interface-list',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-ipv4-arp-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_arp_cfg',
            is_presence=True,
        ),
    },
    'ArpRedundancy.Redundancy.Groups.Group' : {
        'meta_info' : _MetaInfoClass('ArpRedundancy.Redundancy.Groups.Group', REFERENCE_LIST,
            '''None''',
            False, 
            [
            _MetaInfoClassMember('group-id', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('1', '32')], [],
                '''                Group ID
                ''',
                'group_id',
                'Cisco-IOS-XR-ipv4-arp-cfg', True),
            _MetaInfoClassMember('peers', REFERENCE_CLASS, 'Peers', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_arp_cfg', 'ArpRedundancy.Redundancy.Groups.Group.Peers',
                [], [],
                '''                Table of Peer
                ''',
                'peers',
                'Cisco-IOS-XR-ipv4-arp-cfg', False),
            _MetaInfoClassMember('interface-list', REFERENCE_CLASS, 'InterfaceList', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_arp_cfg', 'ArpRedundancy.Redundancy.Groups.Group.InterfaceList',
                [], [],
                '''                List of Interfaces for this Group
                ''',
                'interface_list',
                'Cisco-IOS-XR-ipv4-arp-cfg', False, is_presence=True),
            _MetaInfoClassMember('source-interface', ATTRIBUTE, 'str', 'xr:Interface-name',
                None, None,
                [], [b'[a-zA-Z0-9._/-]+'],
                '''                Interface name
                ''',
                'source_interface',
                'Cisco-IOS-XR-ipv4-arp-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-arp-cfg',
            'group',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-ipv4-arp-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_arp_cfg',
        ),
    },
    'ArpRedundancy.Redundancy.Groups' : {
        'meta_info' : _MetaInfoClass('ArpRedundancy.Redundancy.Groups', REFERENCE_CLASS,
            '''Table of Group''',
            False, 
            [
            _MetaInfoClassMember('group', REFERENCE_LIST, 'Group', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_arp_cfg', 'ArpRedundancy.Redundancy.Groups.Group',
                [], [],
                '''                None
                ''',
                'group',
                'Cisco-IOS-XR-ipv4-arp-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-arp-cfg',
            'groups',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-ipv4-arp-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_arp_cfg',
        ),
    },
    'ArpRedundancy.Redundancy' : {
        'meta_info' : _MetaInfoClass('ArpRedundancy.Redundancy', REFERENCE_CLASS,
            '''Configure parameter for ARP Geo redundancy''',
            False, 
            [
            _MetaInfoClassMember('groups', REFERENCE_CLASS, 'Groups', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_arp_cfg', 'ArpRedundancy.Redundancy.Groups',
                [], [],
                '''                Table of Group
                ''',
                'groups',
                'Cisco-IOS-XR-ipv4-arp-cfg', False),
            _MetaInfoClassMember('enable', ATTRIBUTE, 'Empty', 'empty',
                None, None,
                [], [],
                '''                Enable Configure parameter for ARP Geo
                redundancy. Deletion of this object also causes
                deletion of all associated objects under
                ArpRedundancy.
                ''',
                'enable',
                'Cisco-IOS-XR-ipv4-arp-cfg', False, is_mandatory=True),
            ],
            'Cisco-IOS-XR-ipv4-arp-cfg',
            'redundancy',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-ipv4-arp-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_arp_cfg',
            is_presence=True,
        ),
    },
    'ArpRedundancy' : {
        'meta_info' : _MetaInfoClass('ArpRedundancy', REFERENCE_CLASS,
            '''arp redundancy''',
            False, 
            [
            _MetaInfoClassMember('redundancy', REFERENCE_CLASS, 'Redundancy', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_arp_cfg', 'ArpRedundancy.Redundancy',
                [], [],
                '''                Configure parameter for ARP Geo redundancy
                ''',
                'redundancy',
                'Cisco-IOS-XR-ipv4-arp-cfg', False, is_presence=True),
            ],
            'Cisco-IOS-XR-ipv4-arp-cfg',
            'arp-redundancy',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-ipv4-arp-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_arp_cfg',
        ),
    },
}
_meta_table['Arpgmp.Vrf.Entries.Entry']['meta_info'].parent =_meta_table['Arpgmp.Vrf.Entries']['meta_info']
_meta_table['Arpgmp.Vrf.Entries']['meta_info'].parent =_meta_table['Arpgmp.Vrf']['meta_info']
_meta_table['Arpgmp.Vrf']['meta_info'].parent =_meta_table['Arpgmp']['meta_info']
_meta_table['ArpRedundancy.Redundancy.Groups.Group.Peers.Peer']['meta_info'].parent =_meta_table['ArpRedundancy.Redundancy.Groups.Group.Peers']['meta_info']
_meta_table['ArpRedundancy.Redundancy.Groups.Group.InterfaceList.Interfaces.Interface']['meta_info'].parent =_meta_table['ArpRedundancy.Redundancy.Groups.Group.InterfaceList.Interfaces']['meta_info']
_meta_table['ArpRedundancy.Redundancy.Groups.Group.InterfaceList.Interfaces']['meta_info'].parent =_meta_table['ArpRedundancy.Redundancy.Groups.Group.InterfaceList']['meta_info']
_meta_table['ArpRedundancy.Redundancy.Groups.Group.Peers']['meta_info'].parent =_meta_table['ArpRedundancy.Redundancy.Groups.Group']['meta_info']
_meta_table['ArpRedundancy.Redundancy.Groups.Group.InterfaceList']['meta_info'].parent =_meta_table['ArpRedundancy.Redundancy.Groups.Group']['meta_info']
_meta_table['ArpRedundancy.Redundancy.Groups.Group']['meta_info'].parent =_meta_table['ArpRedundancy.Redundancy.Groups']['meta_info']
_meta_table['ArpRedundancy.Redundancy.Groups']['meta_info'].parent =_meta_table['ArpRedundancy.Redundancy']['meta_info']
_meta_table['ArpRedundancy.Redundancy']['meta_info'].parent =_meta_table['ArpRedundancy']['meta_info']
