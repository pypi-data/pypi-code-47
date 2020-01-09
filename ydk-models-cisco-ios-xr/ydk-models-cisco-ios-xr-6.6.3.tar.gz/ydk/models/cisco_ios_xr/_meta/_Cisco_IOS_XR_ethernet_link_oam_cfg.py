
'''
This is auto-generated file,
which includes metadata for module Cisco_IOS_XR_ethernet_link_oam_cfg
'''

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_LIST, REFERENCE_LEAFLIST, REFERENCE_BITS, REFERENCE_UNION
from ydk._core._dm_meta_info import REFERENCE_CLASS, REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, ANYXML_CLASS
from ydk._core._importer import _yang_ns

_meta_table = {
    'EtherLinkOamThresholdWindowMultiplierEnum' : _MetaInfoEnum('EtherLinkOamThresholdWindowMultiplierEnum',
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_link_oam_cfg', 'EtherLinkOamThresholdWindowMultiplierEnum',
        '''Ether link oam threshold window multiplier enum''',
        {
            'none':'none',
            'thousand':'thousand',
            'million':'million',
            'billion':'billion',
        }, 'Cisco-IOS-XR-ethernet-link-oam-cfg', _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-ethernet-link-oam-cfg']),
    'EtherLinkOamThresholdUnitsFramesEnum' : _MetaInfoEnum('EtherLinkOamThresholdUnitsFramesEnum',
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_link_oam_cfg', 'EtherLinkOamThresholdUnitsFramesEnum',
        '''Ether link oam threshold units frames enum''',
        {
            'frames':'frames',
            'ppm':'ppm',
        }, 'Cisco-IOS-XR-ethernet-link-oam-cfg', _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-ethernet-link-oam-cfg']),
    'EtherLinkOamThresholdUnitsSymbolsEnum' : _MetaInfoEnum('EtherLinkOamThresholdUnitsSymbolsEnum',
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_link_oam_cfg', 'EtherLinkOamThresholdUnitsSymbolsEnum',
        '''Ether link oam threshold units symbols enum''',
        {
            'symbols':'symbols',
            'ppm':'ppm',
        }, 'Cisco-IOS-XR-ethernet-link-oam-cfg', _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-ethernet-link-oam-cfg']),
    'EtherLinkOamWindowUnitsSymbolsEnum' : _MetaInfoEnum('EtherLinkOamWindowUnitsSymbolsEnum',
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_link_oam_cfg', 'EtherLinkOamWindowUnitsSymbolsEnum',
        '''Ether link oam window units symbols enum''',
        {
            'milliseconds':'milliseconds',
            'symbols':'symbols',
        }, 'Cisco-IOS-XR-ethernet-link-oam-cfg', _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-ethernet-link-oam-cfg']),
    'EtherLinkOamWindowUnitsFramesEnum' : _MetaInfoEnum('EtherLinkOamWindowUnitsFramesEnum',
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_link_oam_cfg', 'EtherLinkOamWindowUnitsFramesEnum',
        '''Ether link oam window units frames enum''',
        {
            'milliseconds':'milliseconds',
            'frames':'frames',
        }, 'Cisco-IOS-XR-ethernet-link-oam-cfg', _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-ethernet-link-oam-cfg']),
    'EtherLinkOamRequireModeEnum' : _MetaInfoEnum('EtherLinkOamRequireModeEnum',
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_link_oam_cfg', 'EtherLinkOamRequireModeEnum',
        '''Ether link oam require mode enum''',
        {
            'passive':'passive',
            'active':'active',
            'dont-care':'dont_care',
        }, 'Cisco-IOS-XR-ethernet-link-oam-cfg', _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-ethernet-link-oam-cfg']),
    'EtherLinkOamEventActionEnumEfd' : _MetaInfoEnum('EtherLinkOamEventActionEnumEfd',
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_link_oam_cfg', 'EtherLinkOamEventActionEnumEfd',
        '''Ether link oam event action enum efd''',
        {
            'disable':'disable',
            'error-disable':'error_disable',
            'log':'log',
            'efd':'efd',
        }, 'Cisco-IOS-XR-ethernet-link-oam-cfg', _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-ethernet-link-oam-cfg']),
    'EtherLinkOamEventActionPrimEnum' : _MetaInfoEnum('EtherLinkOamEventActionPrimEnum',
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_link_oam_cfg', 'EtherLinkOamEventActionPrimEnum',
        '''Ether link oam event action prim enum''',
        {
            'disable':'disable',
            'log':'log',
        }, 'Cisco-IOS-XR-ethernet-link-oam-cfg', _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-ethernet-link-oam-cfg']),
    'EtherLinkOamModeEnum' : _MetaInfoEnum('EtherLinkOamModeEnum',
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_link_oam_cfg', 'EtherLinkOamModeEnum',
        '''Ether link oam mode enum''',
        {
            'passive':'passive',
            'active':'active',
        }, 'Cisco-IOS-XR-ethernet-link-oam-cfg', _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-ethernet-link-oam-cfg']),
    'EtherLinkOamEventActionEnum' : _MetaInfoEnum('EtherLinkOamEventActionEnum',
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_link_oam_cfg', 'EtherLinkOamEventActionEnum',
        '''Ether link oam event action enum''',
        {
            'disable':'disable',
            'error-disable':'error_disable',
            'log':'log',
        }, 'Cisco-IOS-XR-ethernet-link-oam-cfg', _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-ethernet-link-oam-cfg']),
    'EtherLinkOamHelloIntervalEnum' : _MetaInfoEnum('EtherLinkOamHelloIntervalEnum',
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_link_oam_cfg', 'EtherLinkOamHelloIntervalEnum',
        '''Ether link oam hello interval enum''',
        {
            '1s':'Y_1s',
            '100ms':'Y_100ms',
        }, 'Cisco-IOS-XR-ethernet-link-oam-cfg', _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-ethernet-link-oam-cfg']),
}
