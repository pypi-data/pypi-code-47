
'''
This is auto-generated file,
which includes metadata for module Cisco_IOS_XR_controller_optics_cfg
'''

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_LIST, REFERENCE_LEAFLIST, REFERENCE_BITS, REFERENCE_UNION
from ydk._core._dm_meta_info import REFERENCE_CLASS, REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, ANYXML_CLASS
from ydk._core._importer import _yang_ns

_meta_table = {
    'OpticsFec' : _MetaInfoEnum('OpticsFec',
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_optics_cfg', 'OpticsFec',
        '''Optics fec''',
        {
            'fec-none':'fec_none',
            'fec-h15':'fec_h15',
            'fec-h25':'fec_h25',
            'fec-h15-de':'fec_h15_de',
            'fec-h25-de':'fec_h25_de',
        }, 'Cisco-IOS-XR-controller-optics-cfg', _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-controller-optics-cfg']),
    'OpticsOtsAmpliControlMode' : _MetaInfoEnum('OpticsOtsAmpliControlMode',
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_optics_cfg', 'OpticsOtsAmpliControlMode',
        '''Optics ots ampli control mode''',
        {
            'automatic':'automatic',
            'manual':'manual',
        }, 'Cisco-IOS-XR-controller-optics-cfg', _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-controller-optics-cfg']),
    'Threshold' : _MetaInfoEnum('Threshold',
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_optics_cfg', 'Threshold',
        '''Threshold''',
        {
            'low':'low',
            'high':'high',
        }, 'Cisco-IOS-XR-controller-optics-cfg', _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-controller-optics-cfg']),
    'OpticsDwdmCarrierParam' : _MetaInfoEnum('OpticsDwdmCarrierParam',
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_optics_cfg', 'OpticsDwdmCarrierParam',
        '''Optics dwdm carrier param''',
        {
            'itu-ch':'itu_ch',
            'wavelength':'wavelength',
            'frequency':'frequency',
        }, 'Cisco-IOS-XR-controller-optics-cfg', _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-controller-optics-cfg']),
    'OpticsOtsSafetyControlMode' : _MetaInfoEnum('OpticsOtsSafetyControlMode',
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_optics_cfg', 'OpticsOtsSafetyControlMode',
        '''Optics ots safety control mode''',
        {
            'auto':'auto',
            'disabled':'disabled',
        }, 'Cisco-IOS-XR-controller-optics-cfg', _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-controller-optics-cfg']),
    'OpticsOtsAmpliGainRange' : _MetaInfoEnum('OpticsOtsAmpliGainRange',
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_optics_cfg', 'OpticsOtsAmpliGainRange',
        '''Optics ots ampli gain range''',
        {
            'normal':'normal',
            'extended':'extended',
        }, 'Cisco-IOS-XR-controller-optics-cfg', _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-controller-optics-cfg']),
    'OpticsDwdmCarrierGrid' : _MetaInfoEnum('OpticsDwdmCarrierGrid',
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_optics_cfg', 'OpticsDwdmCarrierGrid',
        '''Optics dwdm carrier grid''',
        {
            '50g-hz-grid':'Y_50g_hz_grid',
            '100mhz-grid':'Y_100mhz_grid',
        }, 'Cisco-IOS-XR-controller-optics-cfg', _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-controller-optics-cfg']),
    'OpticsLoopback' : _MetaInfoEnum('OpticsLoopback',
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_optics_cfg', 'OpticsLoopback',
        '''Optics loopback''',
        {
            'none':'none',
            'internal':'internal',
            'line':'line',
        }, 'Cisco-IOS-XR-controller-optics-cfg', _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-controller-optics-cfg']),
}
