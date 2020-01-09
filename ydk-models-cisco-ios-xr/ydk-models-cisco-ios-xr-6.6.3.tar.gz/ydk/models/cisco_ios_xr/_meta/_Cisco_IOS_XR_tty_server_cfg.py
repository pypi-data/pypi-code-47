
'''
This is auto-generated file,
which includes metadata for module Cisco_IOS_XR_tty_server_cfg
'''

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_LIST, REFERENCE_LEAFLIST, REFERENCE_BITS, REFERENCE_UNION
from ydk._core._dm_meta_info import REFERENCE_CLASS, REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, ANYXML_CLASS
from ydk._core._importer import _yang_ns

_meta_table = {
    'Tty.TtyLines.TtyLine.General' : {
        'meta_info' : _MetaInfoClass('Tty.TtyLines.TtyLine.General', REFERENCE_CLASS,
            '''TTY line general configuration''',
            False, 
            [
            _MetaInfoClassMember('length', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('0', '512')], [],
                '''                Number of lines on a screen.
                ''',
                'length',
                'Cisco-IOS-XR-tty-server-cfg', False, default_value="24"),
            _MetaInfoClassMember('absolute-timeout', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('0', '10000')], [],
                '''                Absolute timeout for line disconnection
                ''',
                'absolute_timeout',
                'Cisco-IOS-XR-tty-server-cfg', False, default_value="0"),
            _MetaInfoClassMember('width', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('0', '512')], [],
                '''                Number of characters on a screen line.
                ''',
                'width',
                'Cisco-IOS-XR-tty-server-cfg', False, default_value="80"),
            ],
            'Cisco-IOS-XR-tty-server-cfg',
            'general',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-tty-server-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_tty_server_cfg',
        ),
    },
    'Tty.TtyLines.TtyLine.Telnet' : {
        'meta_info' : _MetaInfoClass('Tty.TtyLines.TtyLine.Telnet', REFERENCE_CLASS,
            '''Telnet protocol-specific configuration''',
            False, 
            [
            _MetaInfoClassMember('transparent', ATTRIBUTE, 'Empty', 'empty',
                None, None,
                [], [],
                '''                Send a CR as a CR followed by a NULL instead
                of a CRfollowed by a LF
                ''',
                'transparent',
                'Cisco-IOS-XR-tty-server-cfg', False),
            ],
            'Cisco-IOS-XR-tty-server-cfg',
            'telnet',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-tty-server-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_tty_server_cfg',
        ),
    },
    'Tty.TtyLines.TtyLine.Aaa.UserGroups.UserGroup' : {
        'meta_info' : _MetaInfoClass('Tty.TtyLines.TtyLine.Aaa.UserGroups.UserGroup', REFERENCE_LIST,
            '''Group to which the user will belong''',
            False, 
            [
            _MetaInfoClassMember('name', ATTRIBUTE, 'str', 'xr:Cisco-ios-xr-string',
                None, None,
                [], [b'[\\w\\-\\.:,_@#%$\\+=\\|;]+'],
                '''                Name of the group
                ''',
                'name',
                'Cisco-IOS-XR-tty-server-cfg', True),
            _MetaInfoClassMember('category', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                Specify as 'root-system' for root-system
                group and 'other' for remaining groups
                ''',
                'category',
                'Cisco-IOS-XR-tty-server-cfg', False, is_mandatory=True),
            ],
            'Cisco-IOS-XR-tty-server-cfg',
            'user-group',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-tty-server-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_tty_server_cfg',
        ),
    },
    'Tty.TtyLines.TtyLine.Aaa.UserGroups' : {
        'meta_info' : _MetaInfoClass('Tty.TtyLines.TtyLine.Aaa.UserGroups', REFERENCE_CLASS,
            '''Users characteristics''',
            False, 
            [
            _MetaInfoClassMember('user-group', REFERENCE_LIST, 'UserGroup', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_tty_server_cfg', 'Tty.TtyLines.TtyLine.Aaa.UserGroups.UserGroup',
                [], [],
                '''                Group to which the user will belong
                ''',
                'user_group',
                'Cisco-IOS-XR-tty-server-cfg', False),
            ],
            'Cisco-IOS-XR-tty-server-cfg',
            'user-groups',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-tty-server-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_tty_server_cfg',
        ),
    },
    'Tty.TtyLines.TtyLine.Aaa.Authorization' : {
        'meta_info' : _MetaInfoClass('Tty.TtyLines.TtyLine.Aaa.Authorization', REFERENCE_CLASS,
            '''Authorization parameters''',
            False, 
            [
            _MetaInfoClassMember('exec', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                For starting an exec (shell)
                ''',
                'exec_',
                'Cisco-IOS-XR-tty-server-cfg', False),
            _MetaInfoClassMember('event-manager', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                Specify 'default' or use an authorization
                list with this name
                ''',
                'event_manager',
                'Cisco-IOS-XR-tty-server-cfg', False),
            _MetaInfoClassMember('commands', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                For exec (shell) configuration
                ''',
                'commands',
                'Cisco-IOS-XR-tty-server-cfg', False),
            ],
            'Cisco-IOS-XR-tty-server-cfg',
            'authorization',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-tty-server-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_tty_server_cfg',
        ),
    },
    'Tty.TtyLines.TtyLine.Aaa.Authentication' : {
        'meta_info' : _MetaInfoClass('Tty.TtyLines.TtyLine.Aaa.Authentication', REFERENCE_CLASS,
            '''Authentication parameters''',
            False, 
            [
            _MetaInfoClassMember('login', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                Authentication list name
                ''',
                'login',
                'Cisco-IOS-XR-tty-server-cfg', False),
            ],
            'Cisco-IOS-XR-tty-server-cfg',
            'authentication',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-tty-server-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_tty_server_cfg',
        ),
    },
    'Tty.TtyLines.TtyLine.Aaa.Accounting' : {
        'meta_info' : _MetaInfoClass('Tty.TtyLines.TtyLine.Aaa.Accounting', REFERENCE_CLASS,
            '''Accounting parameters''',
            False, 
            [
            _MetaInfoClassMember('exec', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                For starting an exec (shell)
                ''',
                'exec_',
                'Cisco-IOS-XR-tty-server-cfg', False),
            _MetaInfoClassMember('commands', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                For exec (shell) configuration
                ''',
                'commands',
                'Cisco-IOS-XR-tty-server-cfg', False),
            ],
            'Cisco-IOS-XR-tty-server-cfg',
            'accounting',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-tty-server-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_tty_server_cfg',
        ),
    },
    'Tty.TtyLines.TtyLine.Aaa' : {
        'meta_info' : _MetaInfoClass('Tty.TtyLines.TtyLine.Aaa', REFERENCE_CLASS,
            '''Container class for AAA related TTY
configuration''',
            False, 
            [
            _MetaInfoClassMember('user-groups', REFERENCE_CLASS, 'UserGroups', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_tty_server_cfg', 'Tty.TtyLines.TtyLine.Aaa.UserGroups',
                [], [],
                '''                Users characteristics
                ''',
                'user_groups',
                'Cisco-IOS-XR-tty-server-cfg', False),
            _MetaInfoClassMember('authorization', REFERENCE_CLASS, 'Authorization', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_tty_server_cfg', 'Tty.TtyLines.TtyLine.Aaa.Authorization',
                [], [],
                '''                Authorization parameters
                ''',
                'authorization',
                'Cisco-IOS-XR-tty-server-cfg', False),
            _MetaInfoClassMember('authentication', REFERENCE_CLASS, 'Authentication', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_tty_server_cfg', 'Tty.TtyLines.TtyLine.Aaa.Authentication',
                [], [],
                '''                Authentication parameters
                ''',
                'authentication',
                'Cisco-IOS-XR-tty-server-cfg', False),
            _MetaInfoClassMember('accounting', REFERENCE_CLASS, 'Accounting', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_tty_server_cfg', 'Tty.TtyLines.TtyLine.Aaa.Accounting',
                [], [],
                '''                Accounting parameters
                ''',
                'accounting',
                'Cisco-IOS-XR-tty-server-cfg', False),
            _MetaInfoClassMember('login-timeout', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('0', '300')], [],
                '''                Timeouts for any user input during login
                sequence
                ''',
                'login_timeout',
                'Cisco-IOS-XR-tty-server-cfg', False, default_value="30"),
            _MetaInfoClassMember('secret', ATTRIBUTE, 'str', 'xr:Md5-password',
                None, None,
                [], [b'(!.+)|([^!].+)'],
                '''                Configure a secure one way encrypted password
                ''',
                'secret',
                'Cisco-IOS-XR-tty-server-cfg', False),
            _MetaInfoClassMember('password', ATTRIBUTE, 'str', 'xr:Md5-password',
                None, None,
                [], [b'(!.+)|([^!].+)'],
                '''                Configure the password for the user
                ''',
                'password',
                'Cisco-IOS-XR-tty-server-cfg', False),
            ],
            'Cisco-IOS-XR-tty-server-cfg',
            'aaa',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-tty-server-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_tty_server_cfg',
        ),
    },
    'Tty.TtyLines.TtyLine.Exec.Timeout' : {
        'meta_info' : _MetaInfoClass('Tty.TtyLines.TtyLine.Exec.Timeout', REFERENCE_CLASS,
            '''EXEC Timeout''',
            False, 
            [
            _MetaInfoClassMember('minutes', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('0', '35791')], [],
                '''                Timeout in minutes
                ''',
                'minutes',
                'Cisco-IOS-XR-tty-server-cfg', False, is_mandatory=True),
            _MetaInfoClassMember('seconds', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('0', '2147483')], [],
                '''                Timeout in seconds
                ''',
                'seconds',
                'Cisco-IOS-XR-tty-server-cfg', False, is_mandatory=True),
            ],
            'Cisco-IOS-XR-tty-server-cfg',
            'timeout',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-tty-server-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_tty_server_cfg',
            is_presence=True,
        ),
    },
    'Tty.TtyLines.TtyLine.Exec' : {
        'meta_info' : _MetaInfoClass('Tty.TtyLines.TtyLine.Exec', REFERENCE_CLASS,
            '''EXEC timeout and timestamp configurtion''',
            False, 
            [
            _MetaInfoClassMember('timeout', REFERENCE_CLASS, 'Timeout', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_tty_server_cfg', 'Tty.TtyLines.TtyLine.Exec.Timeout',
                [], [],
                '''                EXEC Timeout
                ''',
                'timeout',
                'Cisco-IOS-XR-tty-server-cfg', False, is_presence=True),
            _MetaInfoClassMember('time-stamp', ATTRIBUTE, 'bool', 'boolean',
                None, None,
                [], [],
                '''                'True' to Enable & 'False' to Disable time
                stamp
                ''',
                'time_stamp',
                'Cisco-IOS-XR-tty-server-cfg', False),
            ],
            'Cisco-IOS-XR-tty-server-cfg',
            'exec',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-tty-server-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_tty_server_cfg',
        ),
    },
    'Tty.TtyLines.TtyLine.Connection.TransportInput' : {
        'meta_info' : _MetaInfoClass('Tty.TtyLines.TtyLine.Connection.TransportInput', REFERENCE_CLASS,
            '''Protocols to use when connecting to the
terminal server''',
            False, 
            [
            _MetaInfoClassMember('select', REFERENCE_ENUM_CLASS, 'TtyTransportProtocolSelect', 'dt1:Tty-transport-protocol-select',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_tty_management_datatypes', 'TtyTransportProtocolSelect',
                [], [],
                '''                Choose transport protocols
                ''',
                'select',
                'Cisco-IOS-XR-tty-management-cfg', False, default_value='Cisco_IOS_XR_tty_management_datatypes.TtyTransportProtocolSelect.all'),
            _MetaInfoClassMember('protocol1', REFERENCE_ENUM_CLASS, 'TtyTransportProtocol', 'dt1:Tty-transport-protocol',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_tty_management_datatypes', 'TtyTransportProtocol',
                [], [],
                '''                Transport protocol1
                ''',
                'protocol1',
                'Cisco-IOS-XR-tty-management-cfg', False, has_when=True),
            _MetaInfoClassMember('protocol2', REFERENCE_ENUM_CLASS, 'TtyTransportProtocol', 'dt1:Tty-transport-protocol',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_tty_management_datatypes', 'TtyTransportProtocol',
                [], [],
                '''                Transport protocol2
                ''',
                'protocol2',
                'Cisco-IOS-XR-tty-management-cfg', False, has_when=True),
            _MetaInfoClassMember('none', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('0', '4294967295')], [],
                '''                Not used
                ''',
                'none',
                'Cisco-IOS-XR-tty-management-cfg', False),
            ],
            'Cisco-IOS-XR-tty-management-cfg',
            'transport-input',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-tty-management-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_tty_server_cfg',
        ),
    },
    'Tty.TtyLines.TtyLine.Connection.TransportOutput' : {
        'meta_info' : _MetaInfoClass('Tty.TtyLines.TtyLine.Connection.TransportOutput', REFERENCE_CLASS,
            '''Protocols to use for outgoing connections''',
            False, 
            [
            _MetaInfoClassMember('select', REFERENCE_ENUM_CLASS, 'TtyTransportProtocolSelect', 'dt1:Tty-transport-protocol-select',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_tty_management_datatypes', 'TtyTransportProtocolSelect',
                [], [],
                '''                Choose transport protocols
                ''',
                'select',
                'Cisco-IOS-XR-tty-management-cfg', False, is_mandatory=True),
            _MetaInfoClassMember('protocol1', REFERENCE_ENUM_CLASS, 'TtyTransportProtocol', 'dt1:Tty-transport-protocol',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_tty_management_datatypes', 'TtyTransportProtocol',
                [], [],
                '''                Transport protocol1
                ''',
                'protocol1',
                'Cisco-IOS-XR-tty-management-cfg', False),
            _MetaInfoClassMember('protocol2', REFERENCE_ENUM_CLASS, 'TtyTransportProtocol', 'dt1:Tty-transport-protocol',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_tty_management_datatypes', 'TtyTransportProtocol',
                [], [],
                '''                Transport protocol2
                ''',
                'protocol2',
                'Cisco-IOS-XR-tty-management-cfg', False),
            _MetaInfoClassMember('none', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('0', '4294967295')], [],
                '''                Not used
                ''',
                'none',
                'Cisco-IOS-XR-tty-management-cfg', False),
            ],
            'Cisco-IOS-XR-tty-management-cfg',
            'transport-output',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-tty-management-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_tty_server_cfg',
            is_presence=True,
        ),
    },
    'Tty.TtyLines.TtyLine.Connection.SessionTimeout' : {
        'meta_info' : _MetaInfoClass('Tty.TtyLines.TtyLine.Connection.SessionTimeout', REFERENCE_CLASS,
            '''Interval for closing connection when there is
no input traffic''',
            False, 
            [
            _MetaInfoClassMember('timeout', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('0', '35791')], [],
                '''                Session timeout interval in minutes
                ''',
                'timeout',
                'Cisco-IOS-XR-tty-management-cfg', False, is_mandatory=True),
            _MetaInfoClassMember('direction', REFERENCE_ENUM_CLASS, 'TtySessionTimeoutDirection', 'dt1:Tty-session-timeout-direction',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_tty_management_datatypes', 'TtySessionTimeoutDirection',
                [], [],
                '''                Include output traffic as well as input
                traffic
                ''',
                'direction',
                'Cisco-IOS-XR-tty-management-cfg', False, is_mandatory=True),
            ],
            'Cisco-IOS-XR-tty-management-cfg',
            'session-timeout',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-tty-management-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_tty_server_cfg',
            is_presence=True,
        ),
    },
    'Tty.TtyLines.TtyLine.Connection' : {
        'meta_info' : _MetaInfoClass('Tty.TtyLines.TtyLine.Connection', REFERENCE_CLASS,
            '''Management connection configuration''',
            False, 
            [
            _MetaInfoClassMember('transport-input', REFERENCE_CLASS, 'TransportInput', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_tty_server_cfg', 'Tty.TtyLines.TtyLine.Connection.TransportInput',
                [], [],
                '''                Protocols to use when connecting to the
                terminal server
                ''',
                'transport_input',
                'Cisco-IOS-XR-tty-management-cfg', False),
            _MetaInfoClassMember('transport-output', REFERENCE_CLASS, 'TransportOutput', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_tty_server_cfg', 'Tty.TtyLines.TtyLine.Connection.TransportOutput',
                [], [],
                '''                Protocols to use for outgoing connections
                ''',
                'transport_output',
                'Cisco-IOS-XR-tty-management-cfg', False, is_presence=True),
            _MetaInfoClassMember('session-timeout', REFERENCE_CLASS, 'SessionTimeout', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_tty_server_cfg', 'Tty.TtyLines.TtyLine.Connection.SessionTimeout',
                [], [],
                '''                Interval for closing connection when there is
                no input traffic
                ''',
                'session_timeout',
                'Cisco-IOS-XR-tty-management-cfg', False, is_presence=True),
            _MetaInfoClassMember('disconnect-character', REFERENCE_UNION, 'str', 'xr:Char-num',
                None, None,
                [], [],
                '''                Disconnect character's decimal equivalent value
                or Character 
                ''',
                'disconnect_character',
                'Cisco-IOS-XR-tty-management-cfg', False, [
                    _MetaInfoClassMember('disconnect-character', ATTRIBUTE, 'str', 'string',
                        None, None,
                        [], [b'(\\p{IsBasicLatin}|\\p{IsLatin-1Supplement})*'],
                        '''                        Disconnect character's decimal equivalent value
                        or Character 
                        ''',
                        'disconnect_character',
                        'Cisco-IOS-XR-tty-management-cfg', False),
                    _MetaInfoClassMember('disconnect-character', ATTRIBUTE, 'int', 'uint8',
                        None, None,
                        [('0', '255')], [],
                        '''                        Disconnect character's decimal equivalent value
                        or Character 
                        ''',
                        'disconnect_character',
                        'Cisco-IOS-XR-tty-management-cfg', False),
                ]),
            _MetaInfoClassMember('acl-in', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                ACL to filter ingoing connections
                ''',
                'acl_in',
                'Cisco-IOS-XR-tty-management-cfg', False),
            _MetaInfoClassMember('acl-out', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                ACL to filter outgoing connections
                ''',
                'acl_out',
                'Cisco-IOS-XR-tty-management-cfg', False),
            _MetaInfoClassMember('cli-white-space-completion', ATTRIBUTE, 'Empty', 'empty',
                None, None,
                [], [],
                '''                Command completion on whitespace
                ''',
                'cli_white_space_completion',
                'Cisco-IOS-XR-tty-management-cfg', False),
            _MetaInfoClassMember('session-limit', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('0', '20')], [],
                '''                The number of outgoing connections
                ''',
                'session_limit',
                'Cisco-IOS-XR-tty-management-cfg', False, default_value="6"),
            _MetaInfoClassMember('escape-character', REFERENCE_UNION, 'str', 'xr:Tty-escape-char-num',
                None, None,
                [], [],
                '''                Escape character or ASCII decimal equivalent
                value orspecial strings NONE,DEFAULT,BREAK
                ''',
                'escape_character',
                'Cisco-IOS-XR-tty-management-cfg', False, [
                    _MetaInfoClassMember('escape-character', ATTRIBUTE, 'str', 'string',
                        None, None,
                        [], [b'(\\p{IsBasicLatin}|\\p{IsLatin-1Supplement})|(DEFAULT)|(BREAK)|(NONE)'],
                        '''                        Escape character or ASCII decimal equivalent
                        value orspecial strings NONE,DEFAULT,BREAK
                        ''',
                        'escape_character',
                        'Cisco-IOS-XR-tty-management-cfg', False, default_value="'30'"),
                    _MetaInfoClassMember('escape-character', ATTRIBUTE, 'int', 'uint8',
                        None, None,
                        [('0', '255')], [],
                        '''                        Escape character or ASCII decimal equivalent
                        value orspecial strings NONE,DEFAULT,BREAK
                        ''',
                        'escape_character',
                        'Cisco-IOS-XR-tty-management-cfg', False, default_value="30"),
                ], default_value="'30'"),
            _MetaInfoClassMember('transport-preferred', REFERENCE_ENUM_CLASS, 'TtyTransportProtocol', 'dt1:Tty-transport-protocol',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_tty_management_datatypes', 'TtyTransportProtocol',
                [], [],
                '''                The preferred protocol to use
                ''',
                'transport_preferred',
                'Cisco-IOS-XR-tty-management-cfg', False),
            ],
            'Cisco-IOS-XR-tty-management-cfg',
            'connection',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-tty-management-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_tty_server_cfg',
        ),
    },
    'Tty.TtyLines.TtyLine.ExecMode' : {
        'meta_info' : _MetaInfoClass('Tty.TtyLines.TtyLine.ExecMode', REFERENCE_CLASS,
            '''Exec Mode Pager  configurtion''',
            False, 
            [
            _MetaInfoClassMember('pager', REFERENCE_ENUM_CLASS, 'TtyPager', 'dt1:Tty-pager',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_tty_management_datatypes', 'TtyPager',
                [], [],
                '''                Preferred Paging Utility
                ''',
                'pager',
                'Cisco-IOS-XR-tty-management-cfg', False, default_value='Cisco_IOS_XR_tty_management_datatypes.TtyPager.more'),
            ],
            'Cisco-IOS-XR-tty-management-cfg',
            'exec-mode',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-tty-management-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_tty_server_cfg',
        ),
    },
    'Tty.TtyLines.TtyLine' : {
        'meta_info' : _MetaInfoClass('Tty.TtyLines.TtyLine', REFERENCE_LIST,
            '''TTY Line,Use string 'console' to configure a
console line,Use string 'default' to configure
a default line,Use any string to configure a
user defined template''',
            False, 
            [
            _MetaInfoClassMember('name', ATTRIBUTE, 'str', 'xr:Cisco-ios-xr-string',
                None, None,
                [], [b'[\\w\\-\\.:,_@#%$\\+=\\|;]+'],
                '''                Name of the template
                ''',
                'name',
                'Cisco-IOS-XR-tty-server-cfg', True),
            _MetaInfoClassMember('general', REFERENCE_CLASS, 'General', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_tty_server_cfg', 'Tty.TtyLines.TtyLine.General',
                [], [],
                '''                TTY line general configuration
                ''',
                'general',
                'Cisco-IOS-XR-tty-server-cfg', False),
            _MetaInfoClassMember('telnet', REFERENCE_CLASS, 'Telnet', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_tty_server_cfg', 'Tty.TtyLines.TtyLine.Telnet',
                [], [],
                '''                Telnet protocol-specific configuration
                ''',
                'telnet',
                'Cisco-IOS-XR-tty-server-cfg', False),
            _MetaInfoClassMember('aaa', REFERENCE_CLASS, 'Aaa', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_tty_server_cfg', 'Tty.TtyLines.TtyLine.Aaa',
                [], [],
                '''                Container class for AAA related TTY
                configuration
                ''',
                'aaa',
                'Cisco-IOS-XR-tty-server-cfg', False),
            _MetaInfoClassMember('exec', REFERENCE_CLASS, 'Exec', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_tty_server_cfg', 'Tty.TtyLines.TtyLine.Exec',
                [], [],
                '''                EXEC timeout and timestamp configurtion
                ''',
                'exec_',
                'Cisco-IOS-XR-tty-server-cfg', False),
            _MetaInfoClassMember('connection', REFERENCE_CLASS, 'Connection', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_tty_server_cfg', 'Tty.TtyLines.TtyLine.Connection',
                [], [],
                '''                Management connection configuration
                ''',
                'connection',
                'Cisco-IOS-XR-tty-management-cfg', False),
            _MetaInfoClassMember('exec-mode', REFERENCE_CLASS, 'ExecMode', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_tty_server_cfg', 'Tty.TtyLines.TtyLine.ExecMode',
                [], [],
                '''                Exec Mode Pager  configurtion
                ''',
                'exec_mode',
                'Cisco-IOS-XR-tty-management-cfg', False),
            ],
            'Cisco-IOS-XR-tty-server-cfg',
            'tty-line',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-tty-server-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_tty_server_cfg',
        ),
    },
    'Tty.TtyLines' : {
        'meta_info' : _MetaInfoClass('Tty.TtyLines', REFERENCE_CLASS,
            '''TTY templates''',
            False, 
            [
            _MetaInfoClassMember('tty-line', REFERENCE_LIST, 'TtyLine', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_tty_server_cfg', 'Tty.TtyLines.TtyLine',
                [], [],
                '''                TTY Line,Use string 'console' to configure a
                console line,Use string 'default' to configure
                a default line,Use any string to configure a
                user defined template
                ''',
                'tty_line',
                'Cisco-IOS-XR-tty-server-cfg', False),
            ],
            'Cisco-IOS-XR-tty-server-cfg',
            'tty-lines',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-tty-server-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_tty_server_cfg',
        ),
    },
    'Tty' : {
        'meta_info' : _MetaInfoClass('Tty', REFERENCE_CLASS,
            '''TTY Line Configuration''',
            False, 
            [
            _MetaInfoClassMember('tty-lines', REFERENCE_CLASS, 'TtyLines', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_tty_server_cfg', 'Tty.TtyLines',
                [], [],
                '''                TTY templates
                ''',
                'tty_lines',
                'Cisco-IOS-XR-tty-server-cfg', False),
            ],
            'Cisco-IOS-XR-tty-server-cfg',
            'tty',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-tty-server-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_tty_server_cfg',
        ),
    },
}
_meta_table['Tty.TtyLines.TtyLine.Aaa.UserGroups.UserGroup']['meta_info'].parent =_meta_table['Tty.TtyLines.TtyLine.Aaa.UserGroups']['meta_info']
_meta_table['Tty.TtyLines.TtyLine.Aaa.UserGroups']['meta_info'].parent =_meta_table['Tty.TtyLines.TtyLine.Aaa']['meta_info']
_meta_table['Tty.TtyLines.TtyLine.Aaa.Authorization']['meta_info'].parent =_meta_table['Tty.TtyLines.TtyLine.Aaa']['meta_info']
_meta_table['Tty.TtyLines.TtyLine.Aaa.Authentication']['meta_info'].parent =_meta_table['Tty.TtyLines.TtyLine.Aaa']['meta_info']
_meta_table['Tty.TtyLines.TtyLine.Aaa.Accounting']['meta_info'].parent =_meta_table['Tty.TtyLines.TtyLine.Aaa']['meta_info']
_meta_table['Tty.TtyLines.TtyLine.Exec.Timeout']['meta_info'].parent =_meta_table['Tty.TtyLines.TtyLine.Exec']['meta_info']
_meta_table['Tty.TtyLines.TtyLine.Connection.TransportInput']['meta_info'].parent =_meta_table['Tty.TtyLines.TtyLine.Connection']['meta_info']
_meta_table['Tty.TtyLines.TtyLine.Connection.TransportOutput']['meta_info'].parent =_meta_table['Tty.TtyLines.TtyLine.Connection']['meta_info']
_meta_table['Tty.TtyLines.TtyLine.Connection.SessionTimeout']['meta_info'].parent =_meta_table['Tty.TtyLines.TtyLine.Connection']['meta_info']
_meta_table['Tty.TtyLines.TtyLine.General']['meta_info'].parent =_meta_table['Tty.TtyLines.TtyLine']['meta_info']
_meta_table['Tty.TtyLines.TtyLine.Telnet']['meta_info'].parent =_meta_table['Tty.TtyLines.TtyLine']['meta_info']
_meta_table['Tty.TtyLines.TtyLine.Aaa']['meta_info'].parent =_meta_table['Tty.TtyLines.TtyLine']['meta_info']
_meta_table['Tty.TtyLines.TtyLine.Exec']['meta_info'].parent =_meta_table['Tty.TtyLines.TtyLine']['meta_info']
_meta_table['Tty.TtyLines.TtyLine.Connection']['meta_info'].parent =_meta_table['Tty.TtyLines.TtyLine']['meta_info']
_meta_table['Tty.TtyLines.TtyLine.ExecMode']['meta_info'].parent =_meta_table['Tty.TtyLines.TtyLine']['meta_info']
_meta_table['Tty.TtyLines.TtyLine']['meta_info'].parent =_meta_table['Tty.TtyLines']['meta_info']
_meta_table['Tty.TtyLines']['meta_info'].parent =_meta_table['Tty']['meta_info']
