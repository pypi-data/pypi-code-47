
'''
This is auto-generated file,
which includes metadata for module Cisco_IOS_XR_config_valid_ccv_cfg
'''

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_LIST, REFERENCE_LEAFLIST, REFERENCE_BITS, REFERENCE_UNION
from ydk._core._dm_meta_info import REFERENCE_CLASS, REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, ANYXML_CLASS
from ydk._core._importer import _yang_ns

_meta_table = {
    'FailureAction' : _MetaInfoEnum('FailureAction',
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_config_valid_ccv_cfg', 'FailureAction',
        '''Failure action''',
        {
            'report':'report',
        }, 'Cisco-IOS-XR-config-valid-ccv-cfg', _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-config-valid-ccv-cfg']),
    'Failure' : _MetaInfoEnum('Failure',
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_config_valid_ccv_cfg', 'Failure',
        '''Failure''',
        {
            'unsupported':'unsupported',
        }, 'Cisco-IOS-XR-config-valid-ccv-cfg', _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-config-valid-ccv-cfg']),
    'Configurationvalidation.FailureTypeActions.FailureTypeAction' : {
        'meta_info' : _MetaInfoClass('Configurationvalidation.FailureTypeActions.FailureTypeAction', REFERENCE_LIST,
            '''Failure type action configuration''',
            False, 
            [
            _MetaInfoClassMember('failure', REFERENCE_ENUM_CLASS, 'Failure', 'Failure',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_config_valid_ccv_cfg', 'Failure',
                [], [],
                '''                Failure type
                ''',
                'failure',
                'Cisco-IOS-XR-config-valid-ccv-cfg', True),
            _MetaInfoClassMember('action', REFERENCE_ENUM_CLASS, 'FailureAction', 'Failure-action',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_config_valid_ccv_cfg', 'FailureAction',
                [], [],
                '''                Action configuration for this failure type
                ''',
                'action',
                'Cisco-IOS-XR-config-valid-ccv-cfg', False),
            ],
            'Cisco-IOS-XR-config-valid-ccv-cfg',
            'failure-type-action',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-config-valid-ccv-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_config_valid_ccv_cfg',
        ),
    },
    'Configurationvalidation.FailureTypeActions' : {
        'meta_info' : _MetaInfoClass('Configurationvalidation.FailureTypeActions', REFERENCE_CLASS,
            '''Table for failure type actions''',
            False, 
            [
            _MetaInfoClassMember('failure-type-action', REFERENCE_LIST, 'FailureTypeAction', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_config_valid_ccv_cfg', 'Configurationvalidation.FailureTypeActions.FailureTypeAction',
                [], [],
                '''                Failure type action configuration
                ''',
                'failure_type_action',
                'Cisco-IOS-XR-config-valid-ccv-cfg', False),
            ],
            'Cisco-IOS-XR-config-valid-ccv-cfg',
            'failure-type-actions',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-config-valid-ccv-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_config_valid_ccv_cfg',
        ),
    },
    'Configurationvalidation' : {
        'meta_info' : _MetaInfoClass('Configurationvalidation', REFERENCE_CLASS,
            '''Configuration for the Configuration Validation
feature''',
            False, 
            [
            _MetaInfoClassMember('failure-type-actions', REFERENCE_CLASS, 'FailureTypeActions', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_config_valid_ccv_cfg', 'Configurationvalidation.FailureTypeActions',
                [], [],
                '''                Table for failure type actions
                ''',
                'failure_type_actions',
                'Cisco-IOS-XR-config-valid-ccv-cfg', False),
            _MetaInfoClassMember('enable', ATTRIBUTE, 'Empty', 'empty',
                None, None,
                [], [],
                '''                Enable configuration validation
                ''',
                'enable',
                'Cisco-IOS-XR-config-valid-ccv-cfg', False),
            ],
            'Cisco-IOS-XR-config-valid-ccv-cfg',
            'configurationvalidation',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-config-valid-ccv-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_config_valid_ccv_cfg',
        ),
    },
}
_meta_table['Configurationvalidation.FailureTypeActions.FailureTypeAction']['meta_info'].parent =_meta_table['Configurationvalidation.FailureTypeActions']['meta_info']
_meta_table['Configurationvalidation.FailureTypeActions']['meta_info'].parent =_meta_table['Configurationvalidation']['meta_info']
