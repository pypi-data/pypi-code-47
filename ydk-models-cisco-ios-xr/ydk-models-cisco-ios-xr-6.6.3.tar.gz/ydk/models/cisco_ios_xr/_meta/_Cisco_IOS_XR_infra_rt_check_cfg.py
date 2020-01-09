
'''
This is auto-generated file,
which includes metadata for module Cisco_IOS_XR_infra_rt_check_cfg
'''

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_LIST, REFERENCE_LEAFLIST, REFERENCE_BITS, REFERENCE_UNION
from ydk._core._dm_meta_info import REFERENCE_CLASS, REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, ANYXML_CLASS
from ydk._core._importer import _yang_ns

_meta_table = {
    'Rcc.Ipv6.Lcc' : {
        'meta_info' : _MetaInfoClass('Rcc.Ipv6.Lcc', REFERENCE_CLASS,
            '''IPv4/IPv6 LCC (Label Consistency Checker)
configuration''',
            False, 
            [
            _MetaInfoClassMember('period', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('100', '600000')], [],
                '''                Period of check in milliseconds
                ''',
                'period',
                'Cisco-IOS-XR-infra-rt-check-cfg', False),
            _MetaInfoClassMember('enable', ATTRIBUTE, 'Empty', 'empty',
                None, None,
                [], [],
                '''                Enable RCC/LCC
                ''',
                'enable',
                'Cisco-IOS-XR-infra-rt-check-cfg', False),
            ],
            'Cisco-IOS-XR-infra-rt-check-cfg',
            'lcc',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-infra-rt-check-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rt_check_cfg',
        ),
    },
    'Rcc.Ipv6.Unicast' : {
        'meta_info' : _MetaInfoClass('Rcc.Ipv6.Unicast', REFERENCE_CLASS,
            '''RCC configuration for unicast''',
            False, 
            [
            _MetaInfoClassMember('period', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('100', '600000')], [],
                '''                Period of check in milliseconds
                ''',
                'period',
                'Cisco-IOS-XR-infra-rt-check-cfg', False),
            _MetaInfoClassMember('enable', ATTRIBUTE, 'Empty', 'empty',
                None, None,
                [], [],
                '''                Enable RCC/LCC
                ''',
                'enable',
                'Cisco-IOS-XR-infra-rt-check-cfg', False),
            ],
            'Cisco-IOS-XR-infra-rt-check-cfg',
            'unicast',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-infra-rt-check-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rt_check_cfg',
        ),
    },
    'Rcc.Ipv6.Multicast' : {
        'meta_info' : _MetaInfoClass('Rcc.Ipv6.Multicast', REFERENCE_CLASS,
            '''RCC configuration for multicast''',
            False, 
            [
            _MetaInfoClassMember('period', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('100', '600000')], [],
                '''                Period of check in milliseconds
                ''',
                'period',
                'Cisco-IOS-XR-infra-rt-check-cfg', False),
            _MetaInfoClassMember('enable', ATTRIBUTE, 'Empty', 'empty',
                None, None,
                [], [],
                '''                Enable RCC/LCC
                ''',
                'enable',
                'Cisco-IOS-XR-infra-rt-check-cfg', False),
            ],
            'Cisco-IOS-XR-infra-rt-check-cfg',
            'multicast',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-infra-rt-check-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rt_check_cfg',
        ),
    },
    'Rcc.Ipv6' : {
        'meta_info' : _MetaInfoClass('Rcc.Ipv6', REFERENCE_CLASS,
            '''RCC/LCC configuration for IPv6''',
            False, 
            [
            _MetaInfoClassMember('lcc', REFERENCE_CLASS, 'Lcc', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rt_check_cfg', 'Rcc.Ipv6.Lcc',
                [], [],
                '''                IPv4/IPv6 LCC (Label Consistency Checker)
                configuration
                ''',
                'lcc',
                'Cisco-IOS-XR-infra-rt-check-cfg', False),
            _MetaInfoClassMember('unicast', REFERENCE_CLASS, 'Unicast', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rt_check_cfg', 'Rcc.Ipv6.Unicast',
                [], [],
                '''                RCC configuration for unicast
                ''',
                'unicast',
                'Cisco-IOS-XR-infra-rt-check-cfg', False),
            _MetaInfoClassMember('multicast', REFERENCE_CLASS, 'Multicast', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rt_check_cfg', 'Rcc.Ipv6.Multicast',
                [], [],
                '''                RCC configuration for multicast
                ''',
                'multicast',
                'Cisco-IOS-XR-infra-rt-check-cfg', False),
            ],
            'Cisco-IOS-XR-infra-rt-check-cfg',
            'ipv6',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-infra-rt-check-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rt_check_cfg',
        ),
    },
    'Rcc.Ipv4.Lcc' : {
        'meta_info' : _MetaInfoClass('Rcc.Ipv4.Lcc', REFERENCE_CLASS,
            '''IPv4/IPv6 LCC (Label Consistency Checker)
configuration''',
            False, 
            [
            _MetaInfoClassMember('period', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('100', '600000')], [],
                '''                Period of check in milliseconds
                ''',
                'period',
                'Cisco-IOS-XR-infra-rt-check-cfg', False),
            _MetaInfoClassMember('enable', ATTRIBUTE, 'Empty', 'empty',
                None, None,
                [], [],
                '''                Enable RCC/LCC
                ''',
                'enable',
                'Cisco-IOS-XR-infra-rt-check-cfg', False),
            ],
            'Cisco-IOS-XR-infra-rt-check-cfg',
            'lcc',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-infra-rt-check-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rt_check_cfg',
        ),
    },
    'Rcc.Ipv4.Unicast' : {
        'meta_info' : _MetaInfoClass('Rcc.Ipv4.Unicast', REFERENCE_CLASS,
            '''RCC configuration for unicast''',
            False, 
            [
            _MetaInfoClassMember('period', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('100', '600000')], [],
                '''                Period of check in milliseconds
                ''',
                'period',
                'Cisco-IOS-XR-infra-rt-check-cfg', False),
            _MetaInfoClassMember('enable', ATTRIBUTE, 'Empty', 'empty',
                None, None,
                [], [],
                '''                Enable RCC/LCC
                ''',
                'enable',
                'Cisco-IOS-XR-infra-rt-check-cfg', False),
            ],
            'Cisco-IOS-XR-infra-rt-check-cfg',
            'unicast',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-infra-rt-check-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rt_check_cfg',
        ),
    },
    'Rcc.Ipv4.Multicast' : {
        'meta_info' : _MetaInfoClass('Rcc.Ipv4.Multicast', REFERENCE_CLASS,
            '''RCC configuration for multicast''',
            False, 
            [
            _MetaInfoClassMember('period', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('100', '600000')], [],
                '''                Period of check in milliseconds
                ''',
                'period',
                'Cisco-IOS-XR-infra-rt-check-cfg', False),
            _MetaInfoClassMember('enable', ATTRIBUTE, 'Empty', 'empty',
                None, None,
                [], [],
                '''                Enable RCC/LCC
                ''',
                'enable',
                'Cisco-IOS-XR-infra-rt-check-cfg', False),
            ],
            'Cisco-IOS-XR-infra-rt-check-cfg',
            'multicast',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-infra-rt-check-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rt_check_cfg',
        ),
    },
    'Rcc.Ipv4' : {
        'meta_info' : _MetaInfoClass('Rcc.Ipv4', REFERENCE_CLASS,
            '''RCC/LCC configuration for IPv4''',
            False, 
            [
            _MetaInfoClassMember('lcc', REFERENCE_CLASS, 'Lcc', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rt_check_cfg', 'Rcc.Ipv4.Lcc',
                [], [],
                '''                IPv4/IPv6 LCC (Label Consistency Checker)
                configuration
                ''',
                'lcc',
                'Cisco-IOS-XR-infra-rt-check-cfg', False),
            _MetaInfoClassMember('unicast', REFERENCE_CLASS, 'Unicast', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rt_check_cfg', 'Rcc.Ipv4.Unicast',
                [], [],
                '''                RCC configuration for unicast
                ''',
                'unicast',
                'Cisco-IOS-XR-infra-rt-check-cfg', False),
            _MetaInfoClassMember('multicast', REFERENCE_CLASS, 'Multicast', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rt_check_cfg', 'Rcc.Ipv4.Multicast',
                [], [],
                '''                RCC configuration for multicast
                ''',
                'multicast',
                'Cisco-IOS-XR-infra-rt-check-cfg', False),
            ],
            'Cisco-IOS-XR-infra-rt-check-cfg',
            'ipv4',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-infra-rt-check-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rt_check_cfg',
        ),
    },
    'Rcc' : {
        'meta_info' : _MetaInfoClass('Rcc', REFERENCE_CLASS,
            '''RCC (Route Consistency Checker) configuration''',
            False, 
            [
            _MetaInfoClassMember('ipv6', REFERENCE_CLASS, 'Ipv6', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rt_check_cfg', 'Rcc.Ipv6',
                [], [],
                '''                RCC/LCC configuration for IPv6
                ''',
                'ipv6',
                'Cisco-IOS-XR-infra-rt-check-cfg', False),
            _MetaInfoClassMember('ipv4', REFERENCE_CLASS, 'Ipv4', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rt_check_cfg', 'Rcc.Ipv4',
                [], [],
                '''                RCC/LCC configuration for IPv4
                ''',
                'ipv4',
                'Cisco-IOS-XR-infra-rt-check-cfg', False),
            ],
            'Cisco-IOS-XR-infra-rt-check-cfg',
            'rcc',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-infra-rt-check-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rt_check_cfg',
        ),
    },
}
_meta_table['Rcc.Ipv6.Lcc']['meta_info'].parent =_meta_table['Rcc.Ipv6']['meta_info']
_meta_table['Rcc.Ipv6.Unicast']['meta_info'].parent =_meta_table['Rcc.Ipv6']['meta_info']
_meta_table['Rcc.Ipv6.Multicast']['meta_info'].parent =_meta_table['Rcc.Ipv6']['meta_info']
_meta_table['Rcc.Ipv4.Lcc']['meta_info'].parent =_meta_table['Rcc.Ipv4']['meta_info']
_meta_table['Rcc.Ipv4.Unicast']['meta_info'].parent =_meta_table['Rcc.Ipv4']['meta_info']
_meta_table['Rcc.Ipv4.Multicast']['meta_info'].parent =_meta_table['Rcc.Ipv4']['meta_info']
_meta_table['Rcc.Ipv6']['meta_info'].parent =_meta_table['Rcc']['meta_info']
_meta_table['Rcc.Ipv4']['meta_info'].parent =_meta_table['Rcc']['meta_info']
