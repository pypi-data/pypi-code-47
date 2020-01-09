
'''
This is auto-generated file,
which includes metadata for module Cisco_IOS_XR_config_cfgmgr_oper
'''

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_LIST, REFERENCE_LEAFLIST, REFERENCE_BITS, REFERENCE_UNION
from ydk._core._dm_meta_info import REFERENCE_CLASS, REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, ANYXML_CLASS
from ydk._core._importer import _yang_ns

_meta_table = {
    'Config.Global.Validation.UnsupportedConfigs.UnsupportedConfig.Failure' : {
        'meta_info' : _MetaInfoClass('Config.Global.Validation.UnsupportedConfigs.UnsupportedConfig.Failure', REFERENCE_LIST,
            '''Validation failures for this configuration item''',
            False, 
            [
            _MetaInfoClassMember('error-app-tag', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                A unique string that identifies the error;
                equivalent to error-app-tag in RFC 6241
                ''',
                'error_app_tag',
                'Cisco-IOS-XR-config-valid-ccv-oper', False, is_config=False),
            _MetaInfoClassMember('error-message', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                The error message; equivalent to error-message
                in RFC 6241
                ''',
                'error_message',
                'Cisco-IOS-XR-config-valid-ccv-oper', False, is_config=False),
            _MetaInfoClassMember('error-severity', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                The severity of the error; equivalent to
                error-severity in RFC 6241
                ''',
                'error_severity',
                'Cisco-IOS-XR-config-valid-ccv-oper', False, is_config=False),
            ],
            'Cisco-IOS-XR-config-valid-ccv-oper',
            'failure',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-config-valid-ccv-oper'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_config_cfgmgr_oper',
            is_config=False,
        ),
    },
    'Config.Global.Validation.UnsupportedConfigs.UnsupportedConfig' : {
        'meta_info' : _MetaInfoClass('Config.Global.Validation.UnsupportedConfigs.UnsupportedConfig', REFERENCE_LIST,
            '''Information about an unsupported warning''',
            False, 
            [
            _MetaInfoClassMember('xpath', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                XPath of the unsupported configuration
                ''',
                'xpath',
                'Cisco-IOS-XR-config-valid-ccv-oper', True, is_config=False),
            _MetaInfoClassMember('group-name', ATTRIBUTE, 'str', 'Ccv-bag-optional-string',
                None, None,
                [], [],
                '''                The configuration group that this item is
                inherited from, if any
                ''',
                'group_name',
                'Cisco-IOS-XR-config-valid-ccv-oper', False, is_config=False),
            _MetaInfoClassMember('failure', REFERENCE_LIST, 'Failure', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_config_cfgmgr_oper', 'Config.Global.Validation.UnsupportedConfigs.UnsupportedConfig.Failure',
                [], [],
                '''                Validation failures for this configuration item
                ''',
                'failure',
                'Cisco-IOS-XR-config-valid-ccv-oper', False, is_config=False),
            ],
            'Cisco-IOS-XR-config-valid-ccv-oper',
            'unsupported-config',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-config-valid-ccv-oper'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_config_cfgmgr_oper',
            is_config=False,
        ),
    },
    'Config.Global.Validation.UnsupportedConfigs' : {
        'meta_info' : _MetaInfoClass('Config.Global.Validation.UnsupportedConfigs', REFERENCE_CLASS,
            '''Unsupported config warnings present in running
configuration''',
            False, 
            [
            _MetaInfoClassMember('unsupported-config', REFERENCE_LIST, 'UnsupportedConfig', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_config_cfgmgr_oper', 'Config.Global.Validation.UnsupportedConfigs.UnsupportedConfig',
                [], [],
                '''                Information about an unsupported warning
                ''',
                'unsupported_config',
                'Cisco-IOS-XR-config-valid-ccv-oper', False, is_config=False),
            ],
            'Cisco-IOS-XR-config-valid-ccv-oper',
            'unsupported-configs',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-config-valid-ccv-oper'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_config_cfgmgr_oper',
            is_config=False,
        ),
    },
    'Config.Global.Validation.PersistentFailures.PersistentFailure.Failure' : {
        'meta_info' : _MetaInfoClass('Config.Global.Validation.PersistentFailures.PersistentFailure.Failure', REFERENCE_LIST,
            '''Validation failures for this configuration item''',
            False, 
            [
            _MetaInfoClassMember('error-app-tag', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                A unique string that identifies the error;
                equivalent to error-app-tag in RFC 6241
                ''',
                'error_app_tag',
                'Cisco-IOS-XR-config-valid-ccv-oper', False, is_config=False),
            _MetaInfoClassMember('error-message', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                The error message; equivalent to error-message
                in RFC 6241
                ''',
                'error_message',
                'Cisco-IOS-XR-config-valid-ccv-oper', False, is_config=False),
            _MetaInfoClassMember('error-severity', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                The severity of the error; equivalent to
                error-severity in RFC 6241
                ''',
                'error_severity',
                'Cisco-IOS-XR-config-valid-ccv-oper', False, is_config=False),
            ],
            'Cisco-IOS-XR-config-valid-ccv-oper',
            'failure',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-config-valid-ccv-oper'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_config_cfgmgr_oper',
            is_config=False,
        ),
    },
    'Config.Global.Validation.PersistentFailures.PersistentFailure' : {
        'meta_info' : _MetaInfoClass('Config.Global.Validation.PersistentFailures.PersistentFailure', REFERENCE_LIST,
            '''Information about a validation failure''',
            False, 
            [
            _MetaInfoClassMember('xpath', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                XPath of the failed configuration
                ''',
                'xpath',
                'Cisco-IOS-XR-config-valid-ccv-oper', True, is_config=False),
            _MetaInfoClassMember('group-name', ATTRIBUTE, 'str', 'Ccv-bag-optional-string',
                None, None,
                [], [],
                '''                The configuration group that this item is
                inherited from, if any
                ''',
                'group_name',
                'Cisco-IOS-XR-config-valid-ccv-oper', False, is_config=False),
            _MetaInfoClassMember('failure', REFERENCE_LIST, 'Failure', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_config_cfgmgr_oper', 'Config.Global.Validation.PersistentFailures.PersistentFailure.Failure',
                [], [],
                '''                Validation failures for this configuration item
                ''',
                'failure',
                'Cisco-IOS-XR-config-valid-ccv-oper', False, is_config=False),
            ],
            'Cisco-IOS-XR-config-valid-ccv-oper',
            'persistent-failure',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-config-valid-ccv-oper'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_config_cfgmgr_oper',
            is_config=False,
        ),
    },
    'Config.Global.Validation.PersistentFailures' : {
        'meta_info' : _MetaInfoClass('Config.Global.Validation.PersistentFailures', REFERENCE_CLASS,
            '''Validation failures present in running
configuration''',
            False, 
            [
            _MetaInfoClassMember('persistent-failure', REFERENCE_LIST, 'PersistentFailure', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_config_cfgmgr_oper', 'Config.Global.Validation.PersistentFailures.PersistentFailure',
                [], [],
                '''                Information about a validation failure
                ''',
                'persistent_failure',
                'Cisco-IOS-XR-config-valid-ccv-oper', False, is_config=False),
            ],
            'Cisco-IOS-XR-config-valid-ccv-oper',
            'persistent-failures',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-config-valid-ccv-oper'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_config_cfgmgr_oper',
            is_config=False,
        ),
    },
    'Config.Global.Validation' : {
        'meta_info' : _MetaInfoClass('Config.Global.Validation', REFERENCE_CLASS,
            '''Configuration validation operational data''',
            False, 
            [
            _MetaInfoClassMember('unsupported-configs', REFERENCE_CLASS, 'UnsupportedConfigs', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_config_cfgmgr_oper', 'Config.Global.Validation.UnsupportedConfigs',
                [], [],
                '''                Unsupported config warnings present in running
                configuration
                ''',
                'unsupported_configs',
                'Cisco-IOS-XR-config-valid-ccv-oper', False, is_config=False),
            _MetaInfoClassMember('persistent-failures', REFERENCE_CLASS, 'PersistentFailures', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_config_cfgmgr_oper', 'Config.Global.Validation.PersistentFailures',
                [], [],
                '''                Validation failures present in running
                configuration
                ''',
                'persistent_failures',
                'Cisco-IOS-XR-config-valid-ccv-oper', False, is_config=False),
            ],
            'Cisco-IOS-XR-config-valid-ccv-oper',
            'validation',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-config-valid-ccv-oper'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_config_cfgmgr_oper',
            is_config=False,
        ),
    },
    'Config.Global' : {
        'meta_info' : _MetaInfoClass('Config.Global', REFERENCE_CLASS,
            '''Global operational data''',
            False, 
            [
            _MetaInfoClassMember('validation', REFERENCE_CLASS, 'Validation', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_config_cfgmgr_oper', 'Config.Global.Validation',
                [], [],
                '''                Configuration validation operational data
                ''',
                'validation',
                'Cisco-IOS-XR-config-valid-ccv-oper', False, is_config=False),
            ],
            'Cisco-IOS-XR-config-cfgmgr-oper',
            'global',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-config-cfgmgr-oper'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_config_cfgmgr_oper',
            is_config=False,
        ),
    },
    'Config' : {
        'meta_info' : _MetaInfoClass('Config', REFERENCE_CLASS,
            '''Configuration-related operational data''',
            False, 
            [
            _MetaInfoClassMember('global', REFERENCE_CLASS, 'Global', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_config_cfgmgr_oper', 'Config.Global',
                [], [],
                '''                Global operational data
                ''',
                'global_',
                'Cisco-IOS-XR-config-cfgmgr-oper', False, is_config=False),
            ],
            'Cisco-IOS-XR-config-cfgmgr-oper',
            'config',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-config-cfgmgr-oper'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_config_cfgmgr_oper',
            is_config=False,
        ),
    },
}
_meta_table['Config.Global.Validation.UnsupportedConfigs.UnsupportedConfig.Failure']['meta_info'].parent =_meta_table['Config.Global.Validation.UnsupportedConfigs.UnsupportedConfig']['meta_info']
_meta_table['Config.Global.Validation.UnsupportedConfigs.UnsupportedConfig']['meta_info'].parent =_meta_table['Config.Global.Validation.UnsupportedConfigs']['meta_info']
_meta_table['Config.Global.Validation.PersistentFailures.PersistentFailure.Failure']['meta_info'].parent =_meta_table['Config.Global.Validation.PersistentFailures.PersistentFailure']['meta_info']
_meta_table['Config.Global.Validation.PersistentFailures.PersistentFailure']['meta_info'].parent =_meta_table['Config.Global.Validation.PersistentFailures']['meta_info']
_meta_table['Config.Global.Validation.UnsupportedConfigs']['meta_info'].parent =_meta_table['Config.Global.Validation']['meta_info']
_meta_table['Config.Global.Validation.PersistentFailures']['meta_info'].parent =_meta_table['Config.Global.Validation']['meta_info']
_meta_table['Config.Global.Validation']['meta_info'].parent =_meta_table['Config.Global']['meta_info']
_meta_table['Config.Global']['meta_info'].parent =_meta_table['Config']['meta_info']
