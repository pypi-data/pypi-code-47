
'''
This is auto-generated file,
which includes metadata for module Cisco_IOS_XR_lmp_datatypes
'''

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_LIST, REFERENCE_LEAFLIST, REFERENCE_BITS, REFERENCE_UNION
from ydk._core._dm_meta_info import REFERENCE_CLASS, REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, ANYXML_CLASS
from ydk._core._importer import _yang_ns

_meta_table = {
    'OlmAddr' : _MetaInfoEnum('OlmAddr',
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lmp_datatypes', 'OlmAddr',
        '''Olm addr''',
        {
            'ipv4':'ipv4',
            'ipv6':'ipv6',
            'unnumbered':'unnumbered',
            'nsap':'nsap',
        }, 'Cisco-IOS-XR-lmp-datatypes', _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-lmp-datatypes']),
    'OlmSwitchingCap' : _MetaInfoEnum('OlmSwitchingCap',
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lmp_datatypes', 'OlmSwitchingCap',
        '''Olm switching cap''',
        {
            'lsc':'lsc',
            'fsc':'fsc',
        }, 'Cisco-IOS-XR-lmp-datatypes', _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-lmp-datatypes']),
}
