
'''
This is auto-generated file,
which includes metadata for module INET_ADDRESS_MIB
'''

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_LIST, REFERENCE_LEAFLIST, REFERENCE_BITS, REFERENCE_UNION
from ydk._core._dm_meta_info import REFERENCE_CLASS, REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, ANYXML_CLASS
from ydk._core._importer import _yang_ns

_meta_table = {
    'InetAddressType' : _MetaInfoEnum('InetAddressType',
        'ydk.models.cisco_ios_xr.INET_ADDRESS_MIB', 'InetAddressType',
        ''' ''',
        {
            'unknown':'unknown',
            'ipv4':'ipv4',
            'ipv6':'ipv6',
            'ipv4z':'ipv4z',
            'ipv6z':'ipv6z',
            'dns':'dns',
        }, 'INET-ADDRESS-MIB', _yang_ns.NAMESPACE_LOOKUP['INET-ADDRESS-MIB']),
    'InetScopeType' : _MetaInfoEnum('InetScopeType',
        'ydk.models.cisco_ios_xr.INET_ADDRESS_MIB', 'InetScopeType',
        ''' ''',
        {
            'interfaceLocal':'interfaceLocal',
            'linkLocal':'linkLocal',
            'subnetLocal':'subnetLocal',
            'adminLocal':'adminLocal',
            'siteLocal':'siteLocal',
            'organizationLocal':'organizationLocal',
            'global':'global_',
        }, 'INET-ADDRESS-MIB', _yang_ns.NAMESPACE_LOOKUP['INET-ADDRESS-MIB']),
    'InetVersion' : _MetaInfoEnum('InetVersion',
        'ydk.models.cisco_ios_xr.INET_ADDRESS_MIB', 'InetVersion',
        ''' ''',
        {
            'unknown':'unknown',
            'ipv4':'ipv4',
            'ipv6':'ipv6',
        }, 'INET-ADDRESS-MIB', _yang_ns.NAMESPACE_LOOKUP['INET-ADDRESS-MIB']),
}
