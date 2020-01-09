
'''
This is auto-generated file,
which includes metadata for module Cisco_IOS_XR_ethernet_cfm_cfg
'''

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_LIST, REFERENCE_LEAFLIST, REFERENCE_BITS, REFERENCE_UNION
from ydk._core._dm_meta_info import REFERENCE_CLASS, REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, ANYXML_CLASS
from ydk._core._importer import _yang_ns

_meta_table = {
    'CfmMipPolicy' : _MetaInfoEnum('CfmMipPolicy',
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_cfg', 'CfmMipPolicy',
        '''Cfm mip policy''',
        {
            'all':'all',
            'lower-mep-only':'lower_mep_only',
        }, 'Cisco-IOS-XR-ethernet-cfm-cfg', _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-ethernet-cfm-cfg']),
    'CfmService' : _MetaInfoEnum('CfmService',
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_cfg', 'CfmService',
        '''Cfm service''',
        {
            'bridge-domain':'bridge_domain',
            'p2p-cross-connect':'p2p_cross_connect',
            'mp2mp-cross-connect':'mp2mp_cross_connect',
            'vlan-aware-flexible-cross-connect':'vlan_aware_flexible_cross_connect',
            'vlan-unaware-flexible-cross-connect':'vlan_unaware_flexible_cross_connect',
            'down-meps':'down_meps',
        }, 'Cisco-IOS-XR-ethernet-cfm-cfg', _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-ethernet-cfm-cfg']),
    'CfmShortMaNameFormat' : _MetaInfoEnum('CfmShortMaNameFormat',
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_cfg', 'CfmShortMaNameFormat',
        '''Cfm short ma name format''',
        {
            'vlan-id':'vlan_id',
            'string':'string',
            'number':'number',
            'vpn-id':'vpn_id',
            'icc-based':'icc_based',
        }, 'Cisco-IOS-XR-ethernet-cfm-cfg', _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-ethernet-cfm-cfg']),
    'CfmLmCountersCfg' : _MetaInfoEnum('CfmLmCountersCfg',
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_cfg', 'CfmLmCountersCfg',
        '''Cfm lm counters cfg''',
        {
            'aggregate':'aggregate',
            'list':'list',
            'range':'range',
        }, 'Cisco-IOS-XR-ethernet-cfm-cfg', _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-ethernet-cfm-cfg']),
    'CfmMdidFormat' : _MetaInfoEnum('CfmMdidFormat',
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_cfg', 'CfmMdidFormat',
        '''Cfm mdid format''',
        {
            'null':'null',
            'dns-like':'dns_like',
            'mac-address':'mac_address',
            'string':'string',
        }, 'Cisco-IOS-XR-ethernet-cfm-cfg', _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-ethernet-cfm-cfg']),
}
