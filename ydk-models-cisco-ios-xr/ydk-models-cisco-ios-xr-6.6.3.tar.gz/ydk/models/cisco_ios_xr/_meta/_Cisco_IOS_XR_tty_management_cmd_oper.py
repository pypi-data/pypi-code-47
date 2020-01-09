
'''
This is auto-generated file,
which includes metadata for module Cisco_IOS_XR_tty_management_cmd_oper
'''

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_LIST, REFERENCE_LEAFLIST, REFERENCE_BITS, REFERENCE_UNION
from ydk._core._dm_meta_info import REFERENCE_CLASS, REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, ANYXML_CLASS
from ydk._core._importer import _yang_ns

_meta_table = {
    'ShowUsers.Sessions.Session' : {
        'meta_info' : _MetaInfoClass('ShowUsers.Sessions.Session', REFERENCE_LIST,
            '''Show users statistics''',
            False, 
            [
            _MetaInfoClassMember('session-id', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('0', '4294967295')], [],
                '''                Session Id
                ''',
                'session_id',
                'Cisco-IOS-XR-tty-management-cmd-oper', True, is_config=False),
            _MetaInfoClassMember('line', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                Line Number
                ''',
                'line',
                'Cisco-IOS-XR-tty-management-cmd-oper', False, is_config=False),
            _MetaInfoClassMember('user', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                User Name
                ''',
                'user',
                'Cisco-IOS-XR-tty-management-cmd-oper', False, is_config=False),
            _MetaInfoClassMember('service', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                Service Name
                ''',
                'service',
                'Cisco-IOS-XR-tty-management-cmd-oper', False, is_config=False),
            _MetaInfoClassMember('conns', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                No. of Connections
                ''',
                'conns',
                'Cisco-IOS-XR-tty-management-cmd-oper', False, is_config=False),
            _MetaInfoClassMember('idle-string', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                Idle Time
                ''',
                'idle_string',
                'Cisco-IOS-XR-tty-management-cmd-oper', False, is_config=False),
            _MetaInfoClassMember('location', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                location
                ''',
                'location',
                'Cisco-IOS-XR-tty-management-cmd-oper', False, is_config=False),
            ],
            'Cisco-IOS-XR-tty-management-cmd-oper',
            'session',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-tty-management-cmd-oper'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_tty_management_cmd_oper',
            is_config=False,
        ),
    },
    'ShowUsers.Sessions' : {
        'meta_info' : _MetaInfoClass('ShowUsers.Sessions', REFERENCE_CLASS,
            '''Show users statistics''',
            False, 
            [
            _MetaInfoClassMember('session', REFERENCE_LIST, 'Session', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_tty_management_cmd_oper', 'ShowUsers.Sessions.Session',
                [], [],
                '''                Show users statistics
                ''',
                'session',
                'Cisco-IOS-XR-tty-management-cmd-oper', False, is_config=False),
            ],
            'Cisco-IOS-XR-tty-management-cmd-oper',
            'sessions',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-tty-management-cmd-oper'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_tty_management_cmd_oper',
            is_config=False,
        ),
    },
    'ShowUsers' : {
        'meta_info' : _MetaInfoClass('ShowUsers', REFERENCE_CLASS,
            '''Show users statistics''',
            False, 
            [
            _MetaInfoClassMember('sessions', REFERENCE_CLASS, 'Sessions', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_tty_management_cmd_oper', 'ShowUsers.Sessions',
                [], [],
                '''                Show users statistics
                ''',
                'sessions',
                'Cisco-IOS-XR-tty-management-cmd-oper', False, is_config=False),
            ],
            'Cisco-IOS-XR-tty-management-cmd-oper',
            'show-users',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-tty-management-cmd-oper'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_tty_management_cmd_oper',
            is_config=False,
        ),
    },
}
_meta_table['ShowUsers.Sessions.Session']['meta_info'].parent =_meta_table['ShowUsers.Sessions']['meta_info']
_meta_table['ShowUsers.Sessions']['meta_info'].parent =_meta_table['ShowUsers']['meta_info']
