
'''
This is auto-generated file,
which includes metadata for module Cisco_IOS_XR_ipv4_ma_oper
'''

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_LIST, REFERENCE_LEAFLIST, REFERENCE_BITS, REFERENCE_UNION
from ydk._core._dm_meta_info import REFERENCE_CLASS, REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, ANYXML_CLASS
from ydk._core._importer import _yang_ns

_meta_table = {
    'ImStateEnum' : _MetaInfoEnum('ImStateEnum',
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_ma_oper', 'ImStateEnum',
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
        }, 'Cisco-IOS-XR-ipv4-ma-oper', _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-ipv4-ma-oper']),
    'Ipv4MaOperConfig' : _MetaInfoEnum('Ipv4MaOperConfig',
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_ma_oper', 'Ipv4MaOperConfig',
        '''ipv4 client type''',
        {
            'ipv4-ma-oper-client-none':'ipv4_ma_oper_client_none',
            'ipv4-ma-oper-non-oc-client':'ipv4_ma_oper_non_oc_client',
            'ipv4-ma-oper-oc-client':'ipv4_ma_oper_oc_client',
        }, 'Cisco-IOS-XR-ipv4-ma-oper', _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-ipv4-ma-oper']),
    'RpfMode' : _MetaInfoEnum('RpfMode',
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_ma_oper', 'RpfMode',
        '''Interface line states''',
        {
            'strict':'strict',
            'loose':'loose',
        }, 'Cisco-IOS-XR-ipv4-ma-oper', _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-ipv4-ma-oper']),
    'Ipv4MaOperLineState' : _MetaInfoEnum('Ipv4MaOperLineState',
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_ma_oper', 'Ipv4MaOperLineState',
        '''Interface line states''',
        {
            'unknown':'unknown',
            'shutdown':'shutdown',
            'down':'down',
            'up':'up',
        }, 'Cisco-IOS-XR-ipv4-ma-oper', _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-ipv4-ma-oper']),
}
