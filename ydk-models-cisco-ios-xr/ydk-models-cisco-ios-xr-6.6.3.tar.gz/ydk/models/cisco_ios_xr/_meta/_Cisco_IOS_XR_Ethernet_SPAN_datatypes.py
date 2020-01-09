
'''
This is auto-generated file,
which includes metadata for module Cisco_IOS_XR_Ethernet_SPAN_datatypes
'''

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_LIST, REFERENCE_LEAFLIST, REFERENCE_BITS, REFERENCE_UNION
from ydk._core._dm_meta_info import REFERENCE_CLASS, REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, ANYXML_CLASS
from ydk._core._importer import _yang_ns

_meta_table = {
    'SpanSessionClass' : _MetaInfoEnum('SpanSessionClass',
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_Ethernet_SPAN_datatypes', 'SpanSessionClass',
        '''Span session class''',
        {
            'ethernet':'ethernet',
            'ipv4':'ipv4',
            'ipv6':'ipv6',
            'mpls-ipv4':'mpls_ipv4',
            'mpls-ipv6':'mpls_ipv6',
        }, 'Cisco-IOS-XR-Ethernet-SPAN-datatypes', _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-Ethernet-SPAN-datatypes']),
    'SpanSessionClassOld' : _MetaInfoEnum('SpanSessionClassOld',
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_Ethernet_SPAN_datatypes', 'SpanSessionClassOld',
        '''Span session class old''',
        {
            'true':'true',
        }, 'Cisco-IOS-XR-Ethernet-SPAN-datatypes', _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-Ethernet-SPAN-datatypes']),
}
