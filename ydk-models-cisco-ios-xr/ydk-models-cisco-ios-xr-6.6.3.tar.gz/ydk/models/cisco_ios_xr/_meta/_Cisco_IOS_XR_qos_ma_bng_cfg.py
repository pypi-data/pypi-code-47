
'''
This is auto-generated file,
which includes metadata for module Cisco_IOS_XR_qos_ma_bng_cfg
'''

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_LIST, REFERENCE_LEAFLIST, REFERENCE_BITS, REFERENCE_UNION
from ydk._core._dm_meta_info import REFERENCE_CLASS, REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, ANYXML_CLASS
from ydk._core._importer import _yang_ns

_meta_table = {
    'Qosl2DataLink' : _MetaInfoEnum('Qosl2DataLink',
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_qos_ma_bng_cfg', 'Qosl2DataLink',
        '''Qosl2 data link''',
        {
            'aal5':'aal5',
        }, 'Cisco-IOS-XR-qos-ma-bng-cfg', _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-qos-ma-bng-cfg']),
    'Qosl2Encap' : _MetaInfoEnum('Qosl2Encap',
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_qos_ma_bng_cfg', 'Qosl2Encap',
        '''Qosl2 encap''',
        {
            'snap-pppoa':'snap_pppoa',
            'mux-pppoa':'mux_pppoa',
            'snap1483-routed':'snap1483_routed',
            'mux1483-routed':'mux1483_routed',
            'snap-rbe':'snap_rbe',
            'snap-dot1qrbe':'snap_dot1qrbe',
            'mux-rbe':'mux_rbe',
            'mux-dot1qrbe':'mux_dot1qrbe',
        }, 'Cisco-IOS-XR-qos-ma-bng-cfg', _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-qos-ma-bng-cfg']),
}
