
'''
This is auto-generated file,
which includes metadata for module Cisco_IOS_XR_clns_isis_datatypes
'''

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_LIST, REFERENCE_LEAFLIST, REFERENCE_BITS, REFERENCE_UNION
from ydk._core._dm_meta_info import REFERENCE_CLASS, REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, ANYXML_CLASS
from ydk._core._importer import _yang_ns

_meta_table = {
    'IsisAddressFamily' : _MetaInfoEnum('IsisAddressFamily',
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_datatypes', 'IsisAddressFamily',
        '''Isis address family''',
        {
            'ipv4':'ipv4',
            'ipv6':'ipv6',
        }, 'Cisco-IOS-XR-clns-isis-datatypes', _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-clns-isis-datatypes']),
    'IsisInternalLevel' : _MetaInfoEnum('IsisInternalLevel',
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_datatypes', 'IsisInternalLevel',
        '''Isis internal level''',
        {
            'not-set':'not_set',
            'level1':'level1',
            'level2':'level2',
        }, 'Cisco-IOS-XR-clns-isis-datatypes', _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-clns-isis-datatypes']),
    'IsisSubAddressFamily' : _MetaInfoEnum('IsisSubAddressFamily',
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_datatypes', 'IsisSubAddressFamily',
        '''Isis sub address family''',
        {
            'unicast':'unicast',
            'multicast':'multicast',
        }, 'Cisco-IOS-XR-clns-isis-datatypes', _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-clns-isis-datatypes']),
}
