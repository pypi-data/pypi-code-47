
'''
This is auto-generated file,
which includes metadata for module Cisco_IOS_XR_pfi_im_cmd_ctrlr_oper
'''

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_LIST, REFERENCE_LEAFLIST, REFERENCE_BITS, REFERENCE_UNION
from ydk._core._dm_meta_info import REFERENCE_CLASS, REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, ANYXML_CLASS
from ydk._core._importer import _yang_ns

_meta_table = {
    'ImStateEnum' : _MetaInfoEnum('ImStateEnum',
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_pfi_im_cmd_ctrlr_oper', 'ImStateEnum',
        '''Im state enum''',
        {
            'im-state-not-ready':'im_state_not_ready',
            'im-state-admin-down':'im_state_admin_down',
            'im-state-down':'im_state_down',
            'im-state-up':'im_state_up',
            'im-state-shutdown':'im_state_shutdown',
            'im-state-err-disable':'im_state_err_disable',
            'im-state-down-immediate':'im_state_down_immediate',
            'im-state-down-immediate-admin':'im_state_down_immediate_admin',
            'im-state-down-graceful':'im_state_down_graceful',
            'im-state-begin-shutdown':'im_state_begin_shutdown',
            'im-state-end-shutdown':'im_state_end_shutdown',
            'im-state-begin-error-disable':'im_state_begin_error_disable',
            'im-state-end-error-disable':'im_state_end_error_disable',
            'im-state-begin-down-graceful':'im_state_begin_down_graceful',
            'im-state-reset':'im_state_reset',
            'im-state-operational':'im_state_operational',
            'im-state-not-operational':'im_state_not_operational',
            'im-state-unknown':'im_state_unknown',
            'im-state-last':'im_state_last',
        }, 'Cisco-IOS-XR-pfi-im-cmd-ctrlr-oper', _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-pfi-im-cmd-ctrlr-oper']),
    'Controllers.Controllers_.Controller' : {
        'meta_info' : _MetaInfoClass('Controllers.Controllers_.Controller', REFERENCE_LIST,
            '''Description for a particular controller''',
            False, 
            [
            _MetaInfoClassMember('interafce-name', ATTRIBUTE, 'str', 'xr:Interface-name',
                None, None,
                [], [b'[a-zA-Z0-9._/-]+'],
                '''                The name of the controller
                ''',
                'interafce_name',
                'Cisco-IOS-XR-pfi-im-cmd-ctrlr-oper', True, is_config=False),
            _MetaInfoClassMember('controller', ATTRIBUTE, 'str', 'xr:Interface-name',
                None, None,
                [], [b'[a-zA-Z0-9._/-]+'],
                '''                Controller
                ''',
                'controller',
                'Cisco-IOS-XR-pfi-im-cmd-ctrlr-oper', False, is_config=False),
            _MetaInfoClassMember('state', REFERENCE_ENUM_CLASS, 'ImStateEnum', 'Im-state-enum',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_pfi_im_cmd_ctrlr_oper', 'ImStateEnum',
                [], [],
                '''                Operational state with no translation of error
                disable or shutdown
                ''',
                'state',
                'Cisco-IOS-XR-pfi-im-cmd-ctrlr-oper', False, is_config=False),
            _MetaInfoClassMember('description', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                Controller description string
                ''',
                'description',
                'Cisco-IOS-XR-pfi-im-cmd-ctrlr-oper', False, is_config=False),
            ],
            'Cisco-IOS-XR-pfi-im-cmd-ctrlr-oper',
            'controller',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-pfi-im-cmd-ctrlr-oper'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_pfi_im_cmd_ctrlr_oper',
            is_config=False,
        ),
    },
    'Controllers.Controllers_' : {
        'meta_info' : _MetaInfoClass('Controllers.Controllers_', REFERENCE_CLASS,
            '''Descriptions for controllers''',
            False, 
            [
            _MetaInfoClassMember('controller', REFERENCE_LIST, 'Controller', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_pfi_im_cmd_ctrlr_oper', 'Controllers.Controllers_.Controller',
                [], [],
                '''                Description for a particular controller
                ''',
                'controller',
                'Cisco-IOS-XR-pfi-im-cmd-ctrlr-oper', False, is_config=False),
            ],
            'Cisco-IOS-XR-pfi-im-cmd-ctrlr-oper',
            'controllers',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-pfi-im-cmd-ctrlr-oper'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_pfi_im_cmd_ctrlr_oper',
            is_config=False,
        ),
    },
    'Controllers' : {
        'meta_info' : _MetaInfoClass('Controllers', REFERENCE_CLASS,
            '''Controller operational data''',
            False, 
            [
            _MetaInfoClassMember('controllers', REFERENCE_CLASS, 'Controllers_', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_pfi_im_cmd_ctrlr_oper', 'Controllers.Controllers_',
                [], [],
                '''                Descriptions for controllers
                ''',
                'controllers',
                'Cisco-IOS-XR-pfi-im-cmd-ctrlr-oper', False, is_config=False),
            ],
            'Cisco-IOS-XR-pfi-im-cmd-ctrlr-oper',
            'controllers',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-pfi-im-cmd-ctrlr-oper'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_pfi_im_cmd_ctrlr_oper',
            is_config=False,
        ),
    },
}
_meta_table['Controllers.Controllers_.Controller']['meta_info'].parent =_meta_table['Controllers.Controllers_']['meta_info']
_meta_table['Controllers.Controllers_']['meta_info'].parent =_meta_table['Controllers']['meta_info']
