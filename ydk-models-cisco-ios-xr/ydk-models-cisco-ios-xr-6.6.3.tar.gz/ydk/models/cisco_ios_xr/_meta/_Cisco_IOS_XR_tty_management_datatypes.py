
'''
This is auto-generated file,
which includes metadata for module Cisco_IOS_XR_tty_management_datatypes
'''

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_LIST, REFERENCE_LEAFLIST, REFERENCE_BITS, REFERENCE_UNION
from ydk._core._dm_meta_info import REFERENCE_CLASS, REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, ANYXML_CLASS
from ydk._core._importer import _yang_ns

_meta_table = {
    'TtyPager' : _MetaInfoEnum('TtyPager',
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_tty_management_datatypes', 'TtyPager',
        '''Tty pager''',
        {
            'more':'more',
            'less':'less',
            'none':'none',
        }, 'Cisco-IOS-XR-tty-management-datatypes', _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-tty-management-datatypes']),
    'TtyEscapeChar' : _MetaInfoEnum('TtyEscapeChar',
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_tty_management_datatypes', 'TtyEscapeChar',
        ''' ''',
        {
            'break':'break_',
            'default':'default',
            'none':'none',
        }, 'Cisco-IOS-XR-tty-management-datatypes', _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-tty-management-datatypes']),
    'TtyTransportProtocolSelect' : _MetaInfoEnum('TtyTransportProtocolSelect',
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_tty_management_datatypes', 'TtyTransportProtocolSelect',
        '''Tty transport protocol select''',
        {
            'none':'none',
            'all':'all',
            'some':'some',
        }, 'Cisco-IOS-XR-tty-management-datatypes', _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-tty-management-datatypes']),
    'TtySessionTimeoutDirection' : _MetaInfoEnum('TtySessionTimeoutDirection',
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_tty_management_datatypes', 'TtySessionTimeoutDirection',
        '''Tty session timeout direction''',
        {
            'in':'in_',
            'in-out':'in_out',
        }, 'Cisco-IOS-XR-tty-management-datatypes', _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-tty-management-datatypes']),
    'TtyTransportProtocol' : _MetaInfoEnum('TtyTransportProtocol',
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_tty_management_datatypes', 'TtyTransportProtocol',
        '''Tty transport protocol''',
        {
            'none':'none',
            'telnet':'telnet',
            'ssh':'ssh',
        }, 'Cisco-IOS-XR-tty-management-datatypes', _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-tty-management-datatypes']),
}
