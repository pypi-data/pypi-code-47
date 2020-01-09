
'''
This is auto-generated file,
which includes metadata for module Cisco_IOS_XR_ipv6_nd_cfg
'''

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_LIST, REFERENCE_LEAFLIST, REFERENCE_BITS, REFERENCE_UNION
from ydk._core._dm_meta_info import REFERENCE_CLASS, REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, ANYXML_CLASS
from ydk._core._importer import _yang_ns

_meta_table = {
    'Ipv6srpEncapsulation' : _MetaInfoEnum('Ipv6srpEncapsulation',
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_nd_cfg', 'Ipv6srpEncapsulation',
        '''Ipv6srp encapsulation''',
        {
            'srpa':'srpa',
            'srpb':'srpb',
        }, 'Cisco-IOS-XR-ipv6-nd-cfg', _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-ipv6-nd-cfg']),
    'Ipv6ndMonth' : _MetaInfoEnum('Ipv6ndMonth',
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_nd_cfg', 'Ipv6ndMonth',
        '''Ipv6nd month''',
        {
            'january':'january',
            'february':'february',
            'march':'march',
            'april':'april',
            'may':'may',
            'june':'june',
            'july':'july',
            'august':'august',
            'september':'september',
            'october':'october',
            'november':'november',
            'december':'december',
        }, 'Cisco-IOS-XR-ipv6-nd-cfg', _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-ipv6-nd-cfg']),
    'Ipv6NdRouterPref' : _MetaInfoEnum('Ipv6NdRouterPref',
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_nd_cfg', 'Ipv6NdRouterPref',
        '''Ipv6 nd router pref''',
        {
            'high':'high',
            'medium':'medium',
            'low':'low',
        }, 'Cisco-IOS-XR-ipv6-nd-cfg', _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-ipv6-nd-cfg']),
    'Ipv6Neighbor.Neighbors.Neighbor' : {
        'meta_info' : _MetaInfoClass('Ipv6Neighbor.Neighbors.Neighbor', REFERENCE_LIST,
            '''IPv6 neighbor configuration''',
            False, 
            [
            _MetaInfoClassMember('neighbor-address', ATTRIBUTE, 'str', 'inet:ipv6-address-no-zone',
                None, None,
                [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'],
                '''                IPv6 address
                ''',
                'neighbor_address',
                'Cisco-IOS-XR-ipv6-nd-cfg', True),
            _MetaInfoClassMember('interface-name', ATTRIBUTE, 'str', 'xr:Interface-name',
                None, None,
                [], [b'[a-zA-Z0-9._/-]+'],
                '''                Interface name
                ''',
                'interface_name',
                'Cisco-IOS-XR-ipv6-nd-cfg', True),
            _MetaInfoClassMember('zone', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                IPv6 address zone
                ''',
                'zone',
                'Cisco-IOS-XR-ipv6-nd-cfg', False, default_value="'0'"),
            _MetaInfoClassMember('mac-address', ATTRIBUTE, 'str', 'yang:mac-address',
                None, None,
                [], [b'[0-9a-fA-F]{2}(:[0-9a-fA-F]{2}){5}'],
                '''                48-bit hardware address H.H.H
                ''',
                'mac_address',
                'Cisco-IOS-XR-ipv6-nd-cfg', False, is_mandatory=True),
            _MetaInfoClassMember('encapsulation', REFERENCE_ENUM_CLASS, 'Ipv6srpEncapsulation', 'Ipv6srp-encapsulation',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_nd_cfg', 'Ipv6srpEncapsulation',
                [], [],
                '''                Encapsulation type only if interface type is
                SRP
                ''',
                'encapsulation',
                'Cisco-IOS-XR-ipv6-nd-cfg', False),
            ],
            'Cisco-IOS-XR-ipv6-nd-cfg',
            'neighbor',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-ipv6-nd-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_nd_cfg',
        ),
    },
    'Ipv6Neighbor.Neighbors' : {
        'meta_info' : _MetaInfoClass('Ipv6Neighbor.Neighbors', REFERENCE_CLASS,
            '''IPv6 neighbors''',
            False, 
            [
            _MetaInfoClassMember('neighbor', REFERENCE_LIST, 'Neighbor', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_nd_cfg', 'Ipv6Neighbor.Neighbors.Neighbor',
                [], [],
                '''                IPv6 neighbor configuration
                ''',
                'neighbor',
                'Cisco-IOS-XR-ipv6-nd-cfg', False),
            ],
            'Cisco-IOS-XR-ipv6-nd-cfg',
            'neighbors',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-ipv6-nd-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_nd_cfg',
        ),
    },
    'Ipv6Neighbor' : {
        'meta_info' : _MetaInfoClass('Ipv6Neighbor', REFERENCE_CLASS,
            '''IPv6 neighbor or neighbor discovery configuration''',
            False, 
            [
            _MetaInfoClassMember('neighbors', REFERENCE_CLASS, 'Neighbors', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_nd_cfg', 'Ipv6Neighbor.Neighbors',
                [], [],
                '''                IPv6 neighbors
                ''',
                'neighbors',
                'Cisco-IOS-XR-ipv6-nd-cfg', False),
            _MetaInfoClassMember('scavenge-timeout', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('1', '43200')], [],
                '''                Set lifetime for stale neighbor
                ''',
                'scavenge_timeout',
                'Cisco-IOS-XR-ipv6-nd-cfg', False),
            _MetaInfoClassMember('cos', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('0', '7')], [],
                '''                Set cos value for both outer vlan and inner vlan
                (if present) in all ougoing ND control packets
                ''',
                'cos',
                'Cisco-IOS-XR-ipv6-nd-cfg', False),
            ],
            'Cisco-IOS-XR-ipv6-nd-cfg',
            'ipv6-neighbor',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-ipv6-nd-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_nd_cfg',
        ),
    },
}
_meta_table['Ipv6Neighbor.Neighbors.Neighbor']['meta_info'].parent =_meta_table['Ipv6Neighbor.Neighbors']['meta_info']
_meta_table['Ipv6Neighbor.Neighbors']['meta_info'].parent =_meta_table['Ipv6Neighbor']['meta_info']
