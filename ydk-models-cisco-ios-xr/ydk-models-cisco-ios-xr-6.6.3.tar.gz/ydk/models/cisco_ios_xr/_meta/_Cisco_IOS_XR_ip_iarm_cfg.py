
'''
This is auto-generated file,
which includes metadata for module Cisco_IOS_XR_ip_iarm_cfg
'''

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_LIST, REFERENCE_LEAFLIST, REFERENCE_BITS, REFERENCE_UNION
from ydk._core._dm_meta_info import REFERENCE_CLASS, REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, ANYXML_CLASS
from ydk._core._importer import _yang_ns

_meta_table = {
    'IpArmConflictPolicy' : _MetaInfoEnum('IpArmConflictPolicy',
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_iarm_cfg', 'IpArmConflictPolicy',
        '''Ip arm conflict policy''',
        {
            'lowest-rack-slot':'lowest_rack_slot',
            'static':'static',
            'longest-prefix':'longest_prefix',
            'highest-ip':'highest_ip',
        }, 'Cisco-IOS-XR-ip-iarm-cfg', _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-ip-iarm-cfg']),
    'IpArm.Ipv4.ConflictPolicyTable' : {
        'meta_info' : _MetaInfoClass('IpArm.Ipv4.ConflictPolicyTable', REFERENCE_CLASS,
            '''IP ARM conflict policy configuration''',
            False, 
            [
            _MetaInfoClassMember('conflict-policy', REFERENCE_ENUM_CLASS, 'IpArmConflictPolicy', 'Ip-arm-conflict-policy',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_iarm_cfg', 'IpArmConflictPolicy',
                [], [],
                '''                IP ARM conflict policy value definitions
                ''',
                'conflict_policy',
                'Cisco-IOS-XR-ip-iarm-cfg', False),
            ],
            'Cisco-IOS-XR-ip-iarm-cfg',
            'conflict-policy-table',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-ip-iarm-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_iarm_cfg',
        ),
    },
    'IpArm.Ipv4.MulticastHost' : {
        'meta_info' : _MetaInfoClass('IpArm.Ipv4.MulticastHost', REFERENCE_CLASS,
            '''IP ARM Multicast Host configuration''',
            False, 
            [
            _MetaInfoClassMember('multicast-host-interface', ATTRIBUTE, 'str', 'xr:Interface-name',
                None, None,
                [], [b'[a-zA-Z0-9._/-]+'],
                '''                Default multicast host interface name
                ''',
                'multicast_host_interface',
                'Cisco-IOS-XR-ip-iarm-cfg', False),
            ],
            'Cisco-IOS-XR-ip-iarm-cfg',
            'multicast-host',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-ip-iarm-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_iarm_cfg',
        ),
    },
    'IpArm.Ipv4' : {
        'meta_info' : _MetaInfoClass('IpArm.Ipv4', REFERENCE_CLASS,
            '''IPv4 ARM configuration''',
            False, 
            [
            _MetaInfoClassMember('conflict-policy-table', REFERENCE_CLASS, 'ConflictPolicyTable', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_iarm_cfg', 'IpArm.Ipv4.ConflictPolicyTable',
                [], [],
                '''                IP ARM conflict policy configuration
                ''',
                'conflict_policy_table',
                'Cisco-IOS-XR-ip-iarm-cfg', False),
            _MetaInfoClassMember('multicast-host', REFERENCE_CLASS, 'MulticastHost', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_iarm_cfg', 'IpArm.Ipv4.MulticastHost',
                [], [],
                '''                IP ARM Multicast Host configuration
                ''',
                'multicast_host',
                'Cisco-IOS-XR-ip-iarm-cfg', False),
            ],
            'Cisco-IOS-XR-ip-iarm-cfg',
            'ipv4',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-ip-iarm-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_iarm_cfg',
        ),
    },
    'IpArm.Ipv6.ConflictPolicyTable' : {
        'meta_info' : _MetaInfoClass('IpArm.Ipv6.ConflictPolicyTable', REFERENCE_CLASS,
            '''IP ARM conflict policy configuration''',
            False, 
            [
            _MetaInfoClassMember('conflict-policy', REFERENCE_ENUM_CLASS, 'IpArmConflictPolicy', 'Ip-arm-conflict-policy',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_iarm_cfg', 'IpArmConflictPolicy',
                [], [],
                '''                IP ARM conflict policy value definitions
                ''',
                'conflict_policy',
                'Cisco-IOS-XR-ip-iarm-cfg', False),
            ],
            'Cisco-IOS-XR-ip-iarm-cfg',
            'conflict-policy-table',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-ip-iarm-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_iarm_cfg',
        ),
    },
    'IpArm.Ipv6.MulticastHost' : {
        'meta_info' : _MetaInfoClass('IpArm.Ipv6.MulticastHost', REFERENCE_CLASS,
            '''IP ARM Multicast Host configuration''',
            False, 
            [
            _MetaInfoClassMember('multicast-host-interface', ATTRIBUTE, 'str', 'xr:Interface-name',
                None, None,
                [], [b'[a-zA-Z0-9._/-]+'],
                '''                Default multicast host interface name
                ''',
                'multicast_host_interface',
                'Cisco-IOS-XR-ip-iarm-cfg', False),
            ],
            'Cisco-IOS-XR-ip-iarm-cfg',
            'multicast-host',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-ip-iarm-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_iarm_cfg',
        ),
    },
    'IpArm.Ipv6' : {
        'meta_info' : _MetaInfoClass('IpArm.Ipv6', REFERENCE_CLASS,
            '''IPv6 ARM configuration''',
            False, 
            [
            _MetaInfoClassMember('conflict-policy-table', REFERENCE_CLASS, 'ConflictPolicyTable', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_iarm_cfg', 'IpArm.Ipv6.ConflictPolicyTable',
                [], [],
                '''                IP ARM conflict policy configuration
                ''',
                'conflict_policy_table',
                'Cisco-IOS-XR-ip-iarm-cfg', False),
            _MetaInfoClassMember('multicast-host', REFERENCE_CLASS, 'MulticastHost', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_iarm_cfg', 'IpArm.Ipv6.MulticastHost',
                [], [],
                '''                IP ARM Multicast Host configuration
                ''',
                'multicast_host',
                'Cisco-IOS-XR-ip-iarm-cfg', False),
            ],
            'Cisco-IOS-XR-ip-iarm-cfg',
            'ipv6',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-ip-iarm-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_iarm_cfg',
        ),
    },
    'IpArm' : {
        'meta_info' : _MetaInfoClass('IpArm', REFERENCE_CLASS,
            '''IP Address Repository Manager (IPv4/IPv6 ARM)
configuration data''',
            False, 
            [
            _MetaInfoClassMember('ipv4', REFERENCE_CLASS, 'Ipv4', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_iarm_cfg', 'IpArm.Ipv4',
                [], [],
                '''                IPv4 ARM configuration
                ''',
                'ipv4',
                'Cisco-IOS-XR-ip-iarm-cfg', False),
            _MetaInfoClassMember('ipv6', REFERENCE_CLASS, 'Ipv6', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_iarm_cfg', 'IpArm.Ipv6',
                [], [],
                '''                IPv6 ARM configuration
                ''',
                'ipv6',
                'Cisco-IOS-XR-ip-iarm-cfg', False),
            ],
            'Cisco-IOS-XR-ip-iarm-cfg',
            'ip-arm',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-ip-iarm-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_iarm_cfg',
        ),
    },
}
_meta_table['IpArm.Ipv4.ConflictPolicyTable']['meta_info'].parent =_meta_table['IpArm.Ipv4']['meta_info']
_meta_table['IpArm.Ipv4.MulticastHost']['meta_info'].parent =_meta_table['IpArm.Ipv4']['meta_info']
_meta_table['IpArm.Ipv6.ConflictPolicyTable']['meta_info'].parent =_meta_table['IpArm.Ipv6']['meta_info']
_meta_table['IpArm.Ipv6.MulticastHost']['meta_info'].parent =_meta_table['IpArm.Ipv6']['meta_info']
_meta_table['IpArm.Ipv4']['meta_info'].parent =_meta_table['IpArm']['meta_info']
_meta_table['IpArm.Ipv6']['meta_info'].parent =_meta_table['IpArm']['meta_info']
