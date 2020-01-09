
'''
This is auto-generated file,
which includes metadata for module Cisco_IOS_XR_parser_cfg
'''

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_LIST, REFERENCE_LEAFLIST, REFERENCE_BITS, REFERENCE_UNION
from ydk._core._dm_meta_info import REFERENCE_CLASS, REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, ANYXML_CLASS
from ydk._core._importer import _yang_ns

_meta_table = {
    'Parser.Indentation' : {
        'meta_info' : _MetaInfoClass('Parser.Indentation', REFERENCE_CLASS,
            '''indentation tracking''',
            False, 
            [
            _MetaInfoClassMember('indentation-disable', ATTRIBUTE, 'bool', 'boolean',
                None, None,
                [], [],
                '''                disable the indentation
                ''',
                'indentation_disable',
                'Cisco-IOS-XR-parser-cfg', False),
            ],
            'Cisco-IOS-XR-parser-cfg',
            'indentation',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-parser-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_parser_cfg',
        ),
    },
    'Parser.Alias.Execs.Exec' : {
        'meta_info' : _MetaInfoClass('Parser.Alias.Execs.Exec', REFERENCE_LIST,
            '''Exec alias name''',
            False, 
            [
            _MetaInfoClassMember('identifier', ATTRIBUTE, 'str', 'string',
                None, None,
                [(1, 30)], [],
                '''                Exec Alias name
                ''',
                'identifier',
                'Cisco-IOS-XR-parser-cfg', True),
            _MetaInfoClassMember('identifier-xr', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                Aliased exec command
                ''',
                'identifier_xr',
                'Cisco-IOS-XR-parser-cfg', False, is_mandatory=True),
            ],
            'Cisco-IOS-XR-parser-cfg',
            'exec',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-parser-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_parser_cfg',
        ),
    },
    'Parser.Alias.Execs' : {
        'meta_info' : _MetaInfoClass('Parser.Alias.Execs', REFERENCE_CLASS,
            '''Exec command alias''',
            False, 
            [
            _MetaInfoClassMember('exec', REFERENCE_LIST, 'Exec', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_parser_cfg', 'Parser.Alias.Execs.Exec',
                [], [],
                '''                Exec alias name
                ''',
                'exec_',
                'Cisco-IOS-XR-parser-cfg', False),
            ],
            'Cisco-IOS-XR-parser-cfg',
            'execs',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-parser-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_parser_cfg',
        ),
    },
    'Parser.Alias.Configurations.Configuration' : {
        'meta_info' : _MetaInfoClass('Parser.Alias.Configurations.Configuration', REFERENCE_LIST,
            '''Configuration Alias name''',
            False, 
            [
            _MetaInfoClassMember('identifier', ATTRIBUTE, 'str', 'string',
                None, None,
                [(1, 30)], [],
                '''                Configuration alias name
                ''',
                'identifier',
                'Cisco-IOS-XR-parser-cfg', True),
            _MetaInfoClassMember('identifier-xr', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                Aliased config command
                ''',
                'identifier_xr',
                'Cisco-IOS-XR-parser-cfg', False, is_mandatory=True),
            ],
            'Cisco-IOS-XR-parser-cfg',
            'configuration',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-parser-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_parser_cfg',
        ),
    },
    'Parser.Alias.Configurations' : {
        'meta_info' : _MetaInfoClass('Parser.Alias.Configurations', REFERENCE_CLASS,
            '''Configuration command alias''',
            False, 
            [
            _MetaInfoClassMember('configuration', REFERENCE_LIST, 'Configuration', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_parser_cfg', 'Parser.Alias.Configurations.Configuration',
                [], [],
                '''                Configuration Alias name
                ''',
                'configuration',
                'Cisco-IOS-XR-parser-cfg', False),
            ],
            'Cisco-IOS-XR-parser-cfg',
            'configurations',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-parser-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_parser_cfg',
        ),
    },
    'Parser.Alias.Alls.All' : {
        'meta_info' : _MetaInfoClass('Parser.Alias.Alls.All', REFERENCE_LIST,
            '''Alias name to command mapping''',
            False, 
            [
            _MetaInfoClassMember('identifier', ATTRIBUTE, 'str', 'string',
                None, None,
                [(1, 30)], [],
                '''                Alias name
                ''',
                'identifier',
                'Cisco-IOS-XR-parser-cfg', True),
            _MetaInfoClassMember('identifier-xr', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                The actual command
                ''',
                'identifier_xr',
                'Cisco-IOS-XR-parser-cfg', False, is_mandatory=True),
            ],
            'Cisco-IOS-XR-parser-cfg',
            'all',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-parser-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_parser_cfg',
        ),
    },
    'Parser.Alias.Alls' : {
        'meta_info' : _MetaInfoClass('Parser.Alias.Alls', REFERENCE_CLASS,
            '''Table of all aliases configured''',
            False, 
            [
            _MetaInfoClassMember('all', REFERENCE_LIST, 'All', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_parser_cfg', 'Parser.Alias.Alls.All',
                [], [],
                '''                Alias name to command mapping
                ''',
                'all',
                'Cisco-IOS-XR-parser-cfg', False),
            ],
            'Cisco-IOS-XR-parser-cfg',
            'alls',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-parser-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_parser_cfg',
        ),
    },
    'Parser.Alias' : {
        'meta_info' : _MetaInfoClass('Parser.Alias', REFERENCE_CLASS,
            '''Alias for command mapping''',
            False, 
            [
            _MetaInfoClassMember('execs', REFERENCE_CLASS, 'Execs', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_parser_cfg', 'Parser.Alias.Execs',
                [], [],
                '''                Exec command alias
                ''',
                'execs',
                'Cisco-IOS-XR-parser-cfg', False),
            _MetaInfoClassMember('configurations', REFERENCE_CLASS, 'Configurations', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_parser_cfg', 'Parser.Alias.Configurations',
                [], [],
                '''                Configuration command alias
                ''',
                'configurations',
                'Cisco-IOS-XR-parser-cfg', False),
            _MetaInfoClassMember('alls', REFERENCE_CLASS, 'Alls', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_parser_cfg', 'Parser.Alias.Alls',
                [], [],
                '''                Table of all aliases configured
                ''',
                'alls',
                'Cisco-IOS-XR-parser-cfg', False),
            ],
            'Cisco-IOS-XR-parser-cfg',
            'alias',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-parser-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_parser_cfg',
        ),
    },
    'Parser.LoggingSuppress' : {
        'meta_info' : _MetaInfoClass('Parser.LoggingSuppress', REFERENCE_CLASS,
            '''logging suppress deprecated''',
            False, 
            [
            _MetaInfoClassMember('deprecated', ATTRIBUTE, 'bool', 'boolean',
                None, None,
                [], [],
                '''                deprecating the logging suppress
                ''',
                'deprecated',
                'Cisco-IOS-XR-parser-cfg', False),
            ],
            'Cisco-IOS-XR-parser-cfg',
            'logging-suppress',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-parser-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_parser_cfg',
        ),
    },
    'Parser.History' : {
        'meta_info' : _MetaInfoClass('Parser.History', REFERENCE_CLASS,
            '''cli commands history''',
            False, 
            [
            _MetaInfoClassMember('size', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('1000', '5000')], [],
                '''                maximum number of commands in history
                ''',
                'size',
                'Cisco-IOS-XR-parser-cfg', False),
            ],
            'Cisco-IOS-XR-parser-cfg',
            'history',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-parser-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_parser_cfg',
        ),
    },
    'Parser.Interactive' : {
        'meta_info' : _MetaInfoClass('Parser.Interactive', REFERENCE_CLASS,
            '''interactive mode''',
            False, 
            [
            _MetaInfoClassMember('interactive-disable', ATTRIBUTE, 'bool', 'boolean',
                None, None,
                [], [],
                '''                disable interactive mode
                ''',
                'interactive_disable',
                'Cisco-IOS-XR-parser-cfg', False),
            ],
            'Cisco-IOS-XR-parser-cfg',
            'interactive',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-parser-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_parser_cfg',
        ),
    },
    'Parser.CommitOptimized' : {
        'meta_info' : _MetaInfoClass('Parser.CommitOptimized', REFERENCE_CLASS,
            '''Enable optimization for regular commit''',
            False, 
            [
            _MetaInfoClassMember('commit-optimized-enable', ATTRIBUTE, 'bool', 'boolean',
                None, None,
                [], [],
                '''                Enable the feature
                ''',
                'commit_optimized_enable',
                'Cisco-IOS-XR-parser-cfg', False),
            ],
            'Cisco-IOS-XR-parser-cfg',
            'commit-optimized',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-parser-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_parser_cfg',
        ),
    },
    'Parser.SysadminLoginBanner' : {
        'meta_info' : _MetaInfoClass('Parser.SysadminLoginBanner', REFERENCE_CLASS,
            '''Configuration to disable sysadmin login banner''',
            False, 
            [
            _MetaInfoClassMember('sysadmin-login-banner-disable', ATTRIBUTE, 'bool', 'boolean',
                None, None,
                [], [],
                '''                Disable sysadmin login banner
                ''',
                'sysadmin_login_banner_disable',
                'Cisco-IOS-XR-parser-cfg', False),
            ],
            'Cisco-IOS-XR-parser-cfg',
            'sysadmin-login-banner',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-parser-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_parser_cfg',
        ),
    },
    'Parser.InterfaceDisplay' : {
        'meta_info' : _MetaInfoClass('Parser.InterfaceDisplay', REFERENCE_CLASS,
            '''Configure the Interface display order''',
            False, 
            [
            _MetaInfoClassMember('slot-order', ATTRIBUTE, 'bool', 'boolean',
                None, None,
                [], [],
                '''                Configure Interface display order as slot order
                ''',
                'slot_order',
                'Cisco-IOS-XR-parser-cfg', False),
            ],
            'Cisco-IOS-XR-parser-cfg',
            'interface-display',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-parser-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_parser_cfg',
        ),
    },
    'Parser.NetmaskFormat' : {
        'meta_info' : _MetaInfoClass('Parser.NetmaskFormat', REFERENCE_CLASS,
            '''Ipv4 netmask-format to be configured''',
            False, 
            [
            _MetaInfoClassMember('bit-count', ATTRIBUTE, 'bool', 'boolean',
                None, None,
                [], [],
                '''                Enable ipv4 netmask-format as bit-count
                ''',
                'bit_count',
                'Cisco-IOS-XR-parser-cfg', False),
            ],
            'Cisco-IOS-XR-parser-cfg',
            'netmask-format',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-parser-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_parser_cfg',
        ),
    },
    'Parser.Configuration.Disable' : {
        'meta_info' : _MetaInfoClass('Parser.Configuration.Disable', REFERENCE_CLASS,
            '''disable for read-only access users''',
            False, 
            [
            _MetaInfoClassMember('usergroup', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                Disable config mode for usergroup
                ''',
                'usergroup',
                'Cisco-IOS-XR-parser-cfg', False),
            ],
            'Cisco-IOS-XR-parser-cfg',
            'disable',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-parser-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_parser_cfg',
        ),
    },
    'Parser.Configuration' : {
        'meta_info' : _MetaInfoClass('Parser.Configuration', REFERENCE_CLASS,
            '''cli configuration services''',
            False, 
            [
            _MetaInfoClassMember('disable', REFERENCE_CLASS, 'Disable', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_parser_cfg', 'Parser.Configuration.Disable',
                [], [],
                '''                disable for read-only access users
                ''',
                'disable',
                'Cisco-IOS-XR-parser-cfg', False),
            ],
            'Cisco-IOS-XR-parser-cfg',
            'configuration',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-parser-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_parser_cfg',
        ),
    },
    'Parser.SubmodeExit' : {
        'meta_info' : _MetaInfoClass('Parser.SubmodeExit', REFERENCE_CLASS,
            '''Exit submode when only '!' seen in interactive
mode''',
            False, 
            [
            _MetaInfoClassMember('enable', ATTRIBUTE, 'bool', 'boolean',
                None, None,
                [], [],
                '''                Enable the feature
                ''',
                'enable',
                'Cisco-IOS-XR-parser-cfg', False),
            ],
            'Cisco-IOS-XR-parser-cfg',
            'submode-exit',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-parser-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_parser_cfg',
        ),
    },
    'Parser' : {
        'meta_info' : _MetaInfoClass('Parser', REFERENCE_CLASS,
            '''Parser configuration''',
            False, 
            [
            _MetaInfoClassMember('indentation', REFERENCE_CLASS, 'Indentation', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_parser_cfg', 'Parser.Indentation',
                [], [],
                '''                indentation tracking
                ''',
                'indentation',
                'Cisco-IOS-XR-parser-cfg', False),
            _MetaInfoClassMember('alias', REFERENCE_CLASS, 'Alias', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_parser_cfg', 'Parser.Alias',
                [], [],
                '''                Alias for command mapping
                ''',
                'alias',
                'Cisco-IOS-XR-parser-cfg', False),
            _MetaInfoClassMember('logging-suppress', REFERENCE_CLASS, 'LoggingSuppress', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_parser_cfg', 'Parser.LoggingSuppress',
                [], [],
                '''                logging suppress deprecated
                ''',
                'logging_suppress',
                'Cisco-IOS-XR-parser-cfg', False),
            _MetaInfoClassMember('history', REFERENCE_CLASS, 'History', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_parser_cfg', 'Parser.History',
                [], [],
                '''                cli commands history
                ''',
                'history',
                'Cisco-IOS-XR-parser-cfg', False),
            _MetaInfoClassMember('interactive', REFERENCE_CLASS, 'Interactive', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_parser_cfg', 'Parser.Interactive',
                [], [],
                '''                interactive mode
                ''',
                'interactive',
                'Cisco-IOS-XR-parser-cfg', False),
            _MetaInfoClassMember('commit-optimized', REFERENCE_CLASS, 'CommitOptimized', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_parser_cfg', 'Parser.CommitOptimized',
                [], [],
                '''                Enable optimization for regular commit
                ''',
                'commit_optimized',
                'Cisco-IOS-XR-parser-cfg', False),
            _MetaInfoClassMember('sysadmin-login-banner', REFERENCE_CLASS, 'SysadminLoginBanner', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_parser_cfg', 'Parser.SysadminLoginBanner',
                [], [],
                '''                Configuration to disable sysadmin login banner
                ''',
                'sysadmin_login_banner',
                'Cisco-IOS-XR-parser-cfg', False),
            _MetaInfoClassMember('interface-display', REFERENCE_CLASS, 'InterfaceDisplay', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_parser_cfg', 'Parser.InterfaceDisplay',
                [], [],
                '''                Configure the Interface display order
                ''',
                'interface_display',
                'Cisco-IOS-XR-parser-cfg', False),
            _MetaInfoClassMember('netmask-format', REFERENCE_CLASS, 'NetmaskFormat', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_parser_cfg', 'Parser.NetmaskFormat',
                [], [],
                '''                Ipv4 netmask-format to be configured
                ''',
                'netmask_format',
                'Cisco-IOS-XR-parser-cfg', False),
            _MetaInfoClassMember('configuration', REFERENCE_CLASS, 'Configuration', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_parser_cfg', 'Parser.Configuration',
                [], [],
                '''                cli configuration services
                ''',
                'configuration',
                'Cisco-IOS-XR-parser-cfg', False),
            _MetaInfoClassMember('submode-exit', REFERENCE_CLASS, 'SubmodeExit', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_parser_cfg', 'Parser.SubmodeExit',
                [], [],
                '''                Exit submode when only '!' seen in interactive
                mode
                ''',
                'submode_exit',
                'Cisco-IOS-XR-parser-cfg', False),
            ],
            'Cisco-IOS-XR-parser-cfg',
            'parser',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-parser-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_parser_cfg',
        ),
    },
}
_meta_table['Parser.Alias.Execs.Exec']['meta_info'].parent =_meta_table['Parser.Alias.Execs']['meta_info']
_meta_table['Parser.Alias.Configurations.Configuration']['meta_info'].parent =_meta_table['Parser.Alias.Configurations']['meta_info']
_meta_table['Parser.Alias.Alls.All']['meta_info'].parent =_meta_table['Parser.Alias.Alls']['meta_info']
_meta_table['Parser.Alias.Execs']['meta_info'].parent =_meta_table['Parser.Alias']['meta_info']
_meta_table['Parser.Alias.Configurations']['meta_info'].parent =_meta_table['Parser.Alias']['meta_info']
_meta_table['Parser.Alias.Alls']['meta_info'].parent =_meta_table['Parser.Alias']['meta_info']
_meta_table['Parser.Configuration.Disable']['meta_info'].parent =_meta_table['Parser.Configuration']['meta_info']
_meta_table['Parser.Indentation']['meta_info'].parent =_meta_table['Parser']['meta_info']
_meta_table['Parser.Alias']['meta_info'].parent =_meta_table['Parser']['meta_info']
_meta_table['Parser.LoggingSuppress']['meta_info'].parent =_meta_table['Parser']['meta_info']
_meta_table['Parser.History']['meta_info'].parent =_meta_table['Parser']['meta_info']
_meta_table['Parser.Interactive']['meta_info'].parent =_meta_table['Parser']['meta_info']
_meta_table['Parser.CommitOptimized']['meta_info'].parent =_meta_table['Parser']['meta_info']
_meta_table['Parser.SysadminLoginBanner']['meta_info'].parent =_meta_table['Parser']['meta_info']
_meta_table['Parser.InterfaceDisplay']['meta_info'].parent =_meta_table['Parser']['meta_info']
_meta_table['Parser.NetmaskFormat']['meta_info'].parent =_meta_table['Parser']['meta_info']
_meta_table['Parser.Configuration']['meta_info'].parent =_meta_table['Parser']['meta_info']
_meta_table['Parser.SubmodeExit']['meta_info'].parent =_meta_table['Parser']['meta_info']
