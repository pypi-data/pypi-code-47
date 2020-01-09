
'''
This is auto-generated file,
which includes metadata for module Cisco_IOS_XR_ipv6_io_cfg
'''

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_LIST, REFERENCE_LEAFLIST, REFERENCE_BITS, REFERENCE_UNION
from ydk._core._dm_meta_info import REFERENCE_CLASS, REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, ANYXML_CLASS
from ydk._core._importer import _yang_ns

_meta_table = {
    'Ipv6Configuration.Ipv6Assembler' : {
        'meta_info' : _MetaInfoClass('Ipv6Configuration.Ipv6Assembler', REFERENCE_CLASS,
            '''IPv6 fragmented packet assembler''',
            False, 
            [
            _MetaInfoClassMember('timeout', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('1', '120')], [],
                '''                Number of seconds an assembly queue will hold
                before timeout
                ''',
                'timeout',
                'Cisco-IOS-XR-ipv6-io-cfg', False),
            _MetaInfoClassMember('max-packets', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('1', '50')], [],
                '''                Maxinum packets allowed in assembly queues (in
                percent)
                ''',
                'max_packets',
                'Cisco-IOS-XR-ipv6-io-cfg', False),
            ],
            'Cisco-IOS-XR-ipv6-io-cfg',
            'ipv6-assembler',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-ipv6-io-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_io_cfg',
        ),
    },
    'Ipv6Configuration.Ipv6icmp' : {
        'meta_info' : _MetaInfoClass('Ipv6Configuration.Ipv6icmp', REFERENCE_CLASS,
            '''Configure IPv6 ICMP parameters''',
            False, 
            [
            _MetaInfoClassMember('error-interval', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('0', '2147483647')], [],
                '''                Interval between tokens in milliseconds
                ''',
                'error_interval',
                'Cisco-IOS-XR-ipv6-io-cfg', False, is_mandatory=True),
            _MetaInfoClassMember('bucket-size', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('1', '200')], [],
                '''                Bucket size
                ''',
                'bucket_size',
                'Cisco-IOS-XR-ipv6-io-cfg', False, default_value="10"),
            ],
            'Cisco-IOS-XR-ipv6-io-cfg',
            'ipv6icmp',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-ipv6-io-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_io_cfg',
            is_presence=True,
        ),
    },
    'Ipv6Configuration' : {
        'meta_info' : _MetaInfoClass('Ipv6Configuration', REFERENCE_CLASS,
            '''IPv6 Configuration Data''',
            False, 
            [
            _MetaInfoClassMember('ipv6-assembler', REFERENCE_CLASS, 'Ipv6Assembler', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_io_cfg', 'Ipv6Configuration.Ipv6Assembler',
                [], [],
                '''                IPv6 fragmented packet assembler
                ''',
                'ipv6_assembler',
                'Cisco-IOS-XR-ipv6-io-cfg', False),
            _MetaInfoClassMember('ipv6icmp', REFERENCE_CLASS, 'Ipv6icmp', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_io_cfg', 'Ipv6Configuration.Ipv6icmp',
                [], [],
                '''                Configure IPv6 ICMP parameters
                ''',
                'ipv6icmp',
                'Cisco-IOS-XR-ipv6-io-cfg', False, is_presence=True),
            _MetaInfoClassMember('ipv6-pmtu-time-out', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('1', '15')], [],
                '''                Configure IPv6 Path MTU timeout value in minutes
                ''',
                'ipv6_pmtu_time_out',
                'Cisco-IOS-XR-ipv6-io-cfg', False),
            _MetaInfoClassMember('ipv6-source-route', ATTRIBUTE, 'bool', 'boolean',
                None, None,
                [], [],
                '''                TRUE if enabled, FALSE if disabled
                ''',
                'ipv6_source_route',
                'Cisco-IOS-XR-ipv6-io-cfg', False, default_value='True'),
            _MetaInfoClassMember('ipv6-pmtu-enable', ATTRIBUTE, 'bool', 'boolean',
                None, None,
                [], [],
                '''                TRUE if enabled, FALSE if disabled
                ''',
                'ipv6_pmtu_enable',
                'Cisco-IOS-XR-ipv6-io-cfg', False, default_value='False'),
            _MetaInfoClassMember('ipv6-hop-limit', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('1', '255')], [],
                '''                Configure IPv6 hop count limit
                ''',
                'ipv6_hop_limit',
                'Cisco-IOS-XR-ipv6-io-cfg', False),
            ],
            'Cisco-IOS-XR-ipv6-io-cfg',
            'ipv6-configuration',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-ipv6-io-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_io_cfg',
        ),
    },
}
_meta_table['Ipv6Configuration.Ipv6Assembler']['meta_info'].parent =_meta_table['Ipv6Configuration']['meta_info']
_meta_table['Ipv6Configuration.Ipv6icmp']['meta_info'].parent =_meta_table['Ipv6Configuration']['meta_info']
