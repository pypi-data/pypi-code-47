
'''
This is auto-generated file,
which includes metadata for module Cisco_IOS_XR_ip_rib_cfg
'''

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_LIST, REFERENCE_LEAFLIST, REFERENCE_BITS, REFERENCE_UNION
from ydk._core._dm_meta_info import REFERENCE_CLASS, REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, ANYXML_CLASS
from ydk._core._importer import _yang_ns

_meta_table = {
    'Rib.Af.Ipv4.RedistributionHistory.Keep' : {
        'meta_info' : _MetaInfoClass('Rib.Af.Ipv4.RedistributionHistory.Keep', REFERENCE_CLASS,
            '''Retain redistribution history after disconnect.''',
            False, 
            [
            _MetaInfoClassMember('bcdl', ATTRIBUTE, 'Empty', 'empty',
                None, None,
                [], [],
                '''                Enable retain BCDL history
                ''',
                'bcdl',
                'Cisco-IOS-XR-ip-rib-cfg', False),
            ],
            'Cisco-IOS-XR-ip-rib-cfg',
            'keep',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-ip-rib-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_rib_cfg',
        ),
    },
    'Rib.Af.Ipv4.RedistributionHistory' : {
        'meta_info' : _MetaInfoClass('Rib.Af.Ipv4.RedistributionHistory', REFERENCE_CLASS,
            '''Redistribution history related configs''',
            False, 
            [
            _MetaInfoClassMember('keep', REFERENCE_CLASS, 'Keep', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_rib_cfg', 'Rib.Af.Ipv4.RedistributionHistory.Keep',
                [], [],
                '''                Retain redistribution history after disconnect.
                ''',
                'keep',
                'Cisco-IOS-XR-ip-rib-cfg', False),
            _MetaInfoClassMember('bcdl-client', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('10', '2000000')], [],
                '''                Maximum BCDL redistribution history size.
                ''',
                'bcdl_client',
                'Cisco-IOS-XR-ip-rib-cfg', False),
            _MetaInfoClassMember('protocol-client', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('10', '250000')], [],
                '''                Maximum protocol redistribution history size.
                ''',
                'protocol_client',
                'Cisco-IOS-XR-ip-rib-cfg', False),
            ],
            'Cisco-IOS-XR-ip-rib-cfg',
            'redistribution-history',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-ip-rib-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_rib_cfg',
        ),
    },
    'Rib.Af.Ipv4' : {
        'meta_info' : _MetaInfoClass('Rib.Af.Ipv4', REFERENCE_CLASS,
            '''IPv4 configuration''',
            False, 
            [
            _MetaInfoClassMember('next-hop-dampening-disable', ATTRIBUTE, 'Empty', 'empty',
                None, None,
                [], [],
                '''                Disable next-hop dampening
                ''',
                'next_hop_dampening_disable',
                'Cisco-IOS-XR-ip-rib-cfg', False),
            _MetaInfoClassMember('redistribution-history', REFERENCE_CLASS, 'RedistributionHistory', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_rib_cfg', 'Rib.Af.Ipv4.RedistributionHistory',
                [], [],
                '''                Redistribution history related configs
                ''',
                'redistribution_history',
                'Cisco-IOS-XR-ip-rib-cfg', False),
            ],
            'Cisco-IOS-XR-ip-rib-cfg',
            'ipv4',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-ip-rib-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_rib_cfg',
        ),
    },
    'Rib.Af.Ipv6.RedistributionHistory.Keep' : {
        'meta_info' : _MetaInfoClass('Rib.Af.Ipv6.RedistributionHistory.Keep', REFERENCE_CLASS,
            '''Retain redistribution history after disconnect.''',
            False, 
            [
            _MetaInfoClassMember('bcdl', ATTRIBUTE, 'Empty', 'empty',
                None, None,
                [], [],
                '''                Enable retain BCDL history
                ''',
                'bcdl',
                'Cisco-IOS-XR-ip-rib-cfg', False),
            ],
            'Cisco-IOS-XR-ip-rib-cfg',
            'keep',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-ip-rib-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_rib_cfg',
        ),
    },
    'Rib.Af.Ipv6.RedistributionHistory' : {
        'meta_info' : _MetaInfoClass('Rib.Af.Ipv6.RedistributionHistory', REFERENCE_CLASS,
            '''Redistribution history related configs''',
            False, 
            [
            _MetaInfoClassMember('keep', REFERENCE_CLASS, 'Keep', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_rib_cfg', 'Rib.Af.Ipv6.RedistributionHistory.Keep',
                [], [],
                '''                Retain redistribution history after disconnect.
                ''',
                'keep',
                'Cisco-IOS-XR-ip-rib-cfg', False),
            _MetaInfoClassMember('bcdl-client', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('10', '2000000')], [],
                '''                Maximum BCDL redistribution history size.
                ''',
                'bcdl_client',
                'Cisco-IOS-XR-ip-rib-cfg', False),
            _MetaInfoClassMember('protocol-client', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('10', '250000')], [],
                '''                Maximum protocol redistribution history size.
                ''',
                'protocol_client',
                'Cisco-IOS-XR-ip-rib-cfg', False),
            ],
            'Cisco-IOS-XR-ip-rib-cfg',
            'redistribution-history',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-ip-rib-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_rib_cfg',
        ),
    },
    'Rib.Af.Ipv6' : {
        'meta_info' : _MetaInfoClass('Rib.Af.Ipv6', REFERENCE_CLASS,
            '''IPv6 configuration''',
            False, 
            [
            _MetaInfoClassMember('next-hop-dampening-disable', ATTRIBUTE, 'Empty', 'empty',
                None, None,
                [], [],
                '''                Disable next-hop dampening
                ''',
                'next_hop_dampening_disable',
                'Cisco-IOS-XR-ip-rib-cfg', False),
            _MetaInfoClassMember('redistribution-history', REFERENCE_CLASS, 'RedistributionHistory', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_rib_cfg', 'Rib.Af.Ipv6.RedistributionHistory',
                [], [],
                '''                Redistribution history related configs
                ''',
                'redistribution_history',
                'Cisco-IOS-XR-ip-rib-cfg', False),
            ],
            'Cisco-IOS-XR-ip-rib-cfg',
            'ipv6',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-ip-rib-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_rib_cfg',
        ),
    },
    'Rib.Af' : {
        'meta_info' : _MetaInfoClass('Rib.Af', REFERENCE_CLASS,
            '''RIB address family configuration''',
            False, 
            [
            _MetaInfoClassMember('ipv4', REFERENCE_CLASS, 'Ipv4', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_rib_cfg', 'Rib.Af.Ipv4',
                [], [],
                '''                IPv4 configuration
                ''',
                'ipv4',
                'Cisco-IOS-XR-ip-rib-cfg', False),
            _MetaInfoClassMember('ipv6', REFERENCE_CLASS, 'Ipv6', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_rib_cfg', 'Rib.Af.Ipv6',
                [], [],
                '''                IPv6 configuration
                ''',
                'ipv6',
                'Cisco-IOS-XR-ip-rib-cfg', False),
            ],
            'Cisco-IOS-XR-ip-rib-cfg',
            'af',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-ip-rib-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_rib_cfg',
        ),
    },
    'Rib' : {
        'meta_info' : _MetaInfoClass('Rib', REFERENCE_CLASS,
            '''RIB configuration.''',
            False, 
            [
            _MetaInfoClassMember('af', REFERENCE_CLASS, 'Af', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_rib_cfg', 'Rib.Af',
                [], [],
                '''                RIB address family configuration
                ''',
                'af',
                'Cisco-IOS-XR-ip-rib-cfg', False),
            _MetaInfoClassMember('max-recursion-depth', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('5', '16')], [],
                '''                Set maximum depth for route recursion check
                ''',
                'max_recursion_depth',
                'Cisco-IOS-XR-ip-rib-cfg', False),
            ],
            'Cisco-IOS-XR-ip-rib-cfg',
            'rib',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-ip-rib-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_rib_cfg',
        ),
    },
}
_meta_table['Rib.Af.Ipv4.RedistributionHistory.Keep']['meta_info'].parent =_meta_table['Rib.Af.Ipv4.RedistributionHistory']['meta_info']
_meta_table['Rib.Af.Ipv4.RedistributionHistory']['meta_info'].parent =_meta_table['Rib.Af.Ipv4']['meta_info']
_meta_table['Rib.Af.Ipv6.RedistributionHistory.Keep']['meta_info'].parent =_meta_table['Rib.Af.Ipv6.RedistributionHistory']['meta_info']
_meta_table['Rib.Af.Ipv6.RedistributionHistory']['meta_info'].parent =_meta_table['Rib.Af.Ipv6']['meta_info']
_meta_table['Rib.Af.Ipv4']['meta_info'].parent =_meta_table['Rib.Af']['meta_info']
_meta_table['Rib.Af.Ipv6']['meta_info'].parent =_meta_table['Rib.Af']['meta_info']
_meta_table['Rib.Af']['meta_info'].parent =_meta_table['Rib']['meta_info']
