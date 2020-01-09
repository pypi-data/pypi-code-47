
'''
This is auto-generated file,
which includes metadata for module Cisco_IOS_XR_tty_management_oper
'''

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_LIST, REFERENCE_LEAFLIST, REFERENCE_BITS, REFERENCE_UNION
from ydk._core._dm_meta_info import REFERENCE_CLASS, REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, ANYXML_CLASS
from ydk._core._importer import _yang_ns

_meta_table = {
    'TransportService' : _MetaInfoEnum('TransportService',
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_tty_management_oper', 'TransportService',
        '''Transport service protocol''',
        {
            'unknown':'unknown',
            'telnet':'telnet',
            'rlogin':'rlogin',
            'ssh':'ssh',
        }, 'Cisco-IOS-XR-tty-management-oper', _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-tty-management-oper']),
    'HostAfIdBase' : {
        'meta_info' : _MetaInfoClass('HostAfIdBase', REFERENCE_IDENTITY_CLASS,
            '''Base identity for Host-af-id''',
            False, 
            [
            ],
            'Cisco-IOS-XR-tty-management-oper',
            'Host-af-id-base',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-tty-management-oper'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_tty_management_oper',
        ),
    },
    'Ipv4' : {
        'meta_info' : _MetaInfoClass('Ipv4', REFERENCE_IDENTITY_CLASS,
            '''IPv4 family''',
            False, 
            [
            ],
            'Cisco-IOS-XR-tty-management-oper',
            'ipv4',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-tty-management-oper'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_tty_management_oper',
        ),
    },
    'Ipv6' : {
        'meta_info' : _MetaInfoClass('Ipv6', REFERENCE_IDENTITY_CLASS,
            '''IPv6 family''',
            False, 
            [
            ],
            'Cisco-IOS-XR-tty-management-oper',
            'ipv6',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-tty-management-oper'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_tty_management_oper',
        ),
    },
}
