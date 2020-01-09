
'''
This is auto-generated file,
which includes metadata for module Cisco_IOS_XR_ip_icmp_cfg
'''

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_LIST, REFERENCE_LEAFLIST, REFERENCE_BITS, REFERENCE_UNION
from ydk._core._dm_meta_info import REFERENCE_CLASS, REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, ANYXML_CLASS
from ydk._core._importer import _yang_ns

_meta_table = {
    'SourcePolicy' : _MetaInfoEnum('SourcePolicy',
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_icmp_cfg', 'SourcePolicy',
        '''Source policy''',
        {
            'vrf':'vrf',
            'rfc':'rfc',
        }, 'Cisco-IOS-XR-ip-icmp-cfg', _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-ip-icmp-cfg']),
    'Icmp.Ipv6.RateLimit.Unreachable' : {
        'meta_info' : _MetaInfoClass('Icmp.Ipv6.RateLimit.Unreachable', REFERENCE_CLASS,
            '''Set unreachable ICMP packets ratelimit''',
            False, 
            [
            _MetaInfoClassMember('rate', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('0', '4294967295')], [],
                '''                Rate Limit of Unreachable ICMP packets
                ''',
                'rate',
                'Cisco-IOS-XR-ip-icmp-cfg', False),
            _MetaInfoClassMember('fragmentation', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('0', '4294967295')], [],
                '''                Rate Limit of Unreachable DF packets
                ''',
                'fragmentation',
                'Cisco-IOS-XR-ip-icmp-cfg', False),
            ],
            'Cisco-IOS-XR-ip-icmp-cfg',
            'unreachable',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-ip-icmp-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_icmp_cfg',
        ),
    },
    'Icmp.Ipv6.RateLimit' : {
        'meta_info' : _MetaInfoClass('Icmp.Ipv6.RateLimit', REFERENCE_CLASS,
            '''Set ratelimit of ICMP packets''',
            False, 
            [
            _MetaInfoClassMember('unreachable', REFERENCE_CLASS, 'Unreachable', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_icmp_cfg', 'Icmp.Ipv6.RateLimit.Unreachable',
                [], [],
                '''                Set unreachable ICMP packets ratelimit
                ''',
                'unreachable',
                'Cisco-IOS-XR-ip-icmp-cfg', False),
            ],
            'Cisco-IOS-XR-ip-icmp-cfg',
            'rate-limit',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-ip-icmp-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_icmp_cfg',
        ),
    },
    'Icmp.Ipv6.Source' : {
        'meta_info' : _MetaInfoClass('Icmp.Ipv6.Source', REFERENCE_CLASS,
            '''IP ICMP Source Address Selection Policy''',
            False, 
            [
            _MetaInfoClassMember('source-address-policy', REFERENCE_ENUM_CLASS, 'SourcePolicy', 'Source-policy',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_icmp_cfg', 'SourcePolicy',
                [], [],
                '''                Configure Source Address Policy
                ''',
                'source_address_policy',
                'Cisco-IOS-XR-ip-icmp-cfg', False),
            ],
            'Cisco-IOS-XR-ip-icmp-cfg',
            'source',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-ip-icmp-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_icmp_cfg',
        ),
    },
    'Icmp.Ipv6' : {
        'meta_info' : _MetaInfoClass('Icmp.Ipv6', REFERENCE_CLASS,
            '''IP Protocol Type''',
            False, 
            [
            _MetaInfoClassMember('rate-limit', REFERENCE_CLASS, 'RateLimit', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_icmp_cfg', 'Icmp.Ipv6.RateLimit',
                [], [],
                '''                Set ratelimit of ICMP packets
                ''',
                'rate_limit',
                'Cisco-IOS-XR-ip-icmp-cfg', False),
            _MetaInfoClassMember('source', REFERENCE_CLASS, 'Source', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_icmp_cfg', 'Icmp.Ipv6.Source',
                [], [],
                '''                IP ICMP Source Address Selection Policy
                ''',
                'source',
                'Cisco-IOS-XR-ip-icmp-cfg', False),
            ],
            'Cisco-IOS-XR-ip-icmp-cfg',
            'ipv6',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-ip-icmp-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_icmp_cfg',
        ),
    },
    'Icmp.Ipv4.RateLimit.Unreachable' : {
        'meta_info' : _MetaInfoClass('Icmp.Ipv4.RateLimit.Unreachable', REFERENCE_CLASS,
            '''Set unreachable ICMP packets ratelimit''',
            False, 
            [
            _MetaInfoClassMember('rate', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('0', '4294967295')], [],
                '''                Rate Limit of Unreachable ICMP packets
                ''',
                'rate',
                'Cisco-IOS-XR-ip-icmp-cfg', False),
            _MetaInfoClassMember('fragmentation', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('0', '4294967295')], [],
                '''                Rate Limit of Unreachable DF packets
                ''',
                'fragmentation',
                'Cisco-IOS-XR-ip-icmp-cfg', False),
            ],
            'Cisco-IOS-XR-ip-icmp-cfg',
            'unreachable',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-ip-icmp-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_icmp_cfg',
        ),
    },
    'Icmp.Ipv4.RateLimit' : {
        'meta_info' : _MetaInfoClass('Icmp.Ipv4.RateLimit', REFERENCE_CLASS,
            '''Set ratelimit of ICMP packets''',
            False, 
            [
            _MetaInfoClassMember('unreachable', REFERENCE_CLASS, 'Unreachable', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_icmp_cfg', 'Icmp.Ipv4.RateLimit.Unreachable',
                [], [],
                '''                Set unreachable ICMP packets ratelimit
                ''',
                'unreachable',
                'Cisco-IOS-XR-ip-icmp-cfg', False),
            ],
            'Cisco-IOS-XR-ip-icmp-cfg',
            'rate-limit',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-ip-icmp-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_icmp_cfg',
        ),
    },
    'Icmp.Ipv4.Source' : {
        'meta_info' : _MetaInfoClass('Icmp.Ipv4.Source', REFERENCE_CLASS,
            '''IP ICMP Source Address Selection Policy''',
            False, 
            [
            _MetaInfoClassMember('source-address-policy', REFERENCE_ENUM_CLASS, 'SourcePolicy', 'Source-policy',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_icmp_cfg', 'SourcePolicy',
                [], [],
                '''                Configure Source Address Policy
                ''',
                'source_address_policy',
                'Cisco-IOS-XR-ip-icmp-cfg', False),
            ],
            'Cisco-IOS-XR-ip-icmp-cfg',
            'source',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-ip-icmp-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_icmp_cfg',
        ),
    },
    'Icmp.Ipv4' : {
        'meta_info' : _MetaInfoClass('Icmp.Ipv4', REFERENCE_CLASS,
            '''IP Protocol Type''',
            False, 
            [
            _MetaInfoClassMember('rate-limit', REFERENCE_CLASS, 'RateLimit', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_icmp_cfg', 'Icmp.Ipv4.RateLimit',
                [], [],
                '''                Set ratelimit of ICMP packets
                ''',
                'rate_limit',
                'Cisco-IOS-XR-ip-icmp-cfg', False),
            _MetaInfoClassMember('source', REFERENCE_CLASS, 'Source', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_icmp_cfg', 'Icmp.Ipv4.Source',
                [], [],
                '''                IP ICMP Source Address Selection Policy
                ''',
                'source',
                'Cisco-IOS-XR-ip-icmp-cfg', False),
            ],
            'Cisco-IOS-XR-ip-icmp-cfg',
            'ipv4',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-ip-icmp-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_icmp_cfg',
        ),
    },
    'Icmp' : {
        'meta_info' : _MetaInfoClass('Icmp', REFERENCE_CLASS,
            '''IP ICMP configuration data''',
            False, 
            [
            _MetaInfoClassMember('ipv6', REFERENCE_CLASS, 'Ipv6', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_icmp_cfg', 'Icmp.Ipv6',
                [], [],
                '''                IP Protocol Type
                ''',
                'ipv6',
                'Cisco-IOS-XR-ip-icmp-cfg', False),
            _MetaInfoClassMember('ipv4', REFERENCE_CLASS, 'Ipv4', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_icmp_cfg', 'Icmp.Ipv4',
                [], [],
                '''                IP Protocol Type
                ''',
                'ipv4',
                'Cisco-IOS-XR-ip-icmp-cfg', False),
            ],
            'Cisco-IOS-XR-ip-icmp-cfg',
            'icmp',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-ip-icmp-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_icmp_cfg',
        ),
    },
}
_meta_table['Icmp.Ipv6.RateLimit.Unreachable']['meta_info'].parent =_meta_table['Icmp.Ipv6.RateLimit']['meta_info']
_meta_table['Icmp.Ipv6.RateLimit']['meta_info'].parent =_meta_table['Icmp.Ipv6']['meta_info']
_meta_table['Icmp.Ipv6.Source']['meta_info'].parent =_meta_table['Icmp.Ipv6']['meta_info']
_meta_table['Icmp.Ipv4.RateLimit.Unreachable']['meta_info'].parent =_meta_table['Icmp.Ipv4.RateLimit']['meta_info']
_meta_table['Icmp.Ipv4.RateLimit']['meta_info'].parent =_meta_table['Icmp.Ipv4']['meta_info']
_meta_table['Icmp.Ipv4.Source']['meta_info'].parent =_meta_table['Icmp.Ipv4']['meta_info']
_meta_table['Icmp.Ipv6']['meta_info'].parent =_meta_table['Icmp']['meta_info']
_meta_table['Icmp.Ipv4']['meta_info'].parent =_meta_table['Icmp']['meta_info']
