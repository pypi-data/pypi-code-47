
'''
This is auto-generated file,
which includes metadata for module Cisco_IOS_XR_Ethernet_SPAN_subscriber_cfg
'''

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_LIST, REFERENCE_LEAFLIST, REFERENCE_BITS, REFERENCE_UNION
from ydk._core._dm_meta_info import REFERENCE_CLASS, REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, ANYXML_CLASS
from ydk._core._importer import _yang_ns

_meta_table = {
    'SpanTrafficDirection' : _MetaInfoEnum('SpanTrafficDirection',
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_Ethernet_SPAN_subscriber_cfg', 'SpanTrafficDirection',
        '''Span traffic direction''',
        {
            'rx-only':'rx_only',
            'tx-only':'tx_only',
        }, 'Cisco-IOS-XR-Ethernet-SPAN-subscriber-cfg', _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-Ethernet-SPAN-subscriber-cfg']),
    'SpanMirrorInterval' : _MetaInfoEnum('SpanMirrorInterval',
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_Ethernet_SPAN_subscriber_cfg', 'SpanMirrorInterval',
        '''Span mirror interval''',
        {
            '512':'Y_512',
            '1k':'Y_1k',
            '2k':'Y_2k',
            '4k':'Y_4k',
            '8k':'Y_8k',
            '16k':'Y_16k',
        }, 'Cisco-IOS-XR-Ethernet-SPAN-subscriber-cfg', _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-Ethernet-SPAN-subscriber-cfg']),
}
