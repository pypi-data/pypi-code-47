
'''
This is auto-generated file,
which includes metadata for module Cisco_IOS_XR_controller_otu_cfg
'''

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_LIST, REFERENCE_LEAFLIST, REFERENCE_BITS, REFERENCE_UNION
from ydk._core._dm_meta_info import REFERENCE_CLASS, REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, ANYXML_CLASS
from ydk._core._importer import _yang_ns

_meta_table = {
    'OtuForwardErrorCorrection' : _MetaInfoEnum('OtuForwardErrorCorrection',
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_otu_cfg', 'OtuForwardErrorCorrection',
        '''Otu forward error correction''',
        {
            'none':'none',
            'standard':'standard',
            'enhanced-i7':'enhanced_i7',
            'enhanced-i4':'enhanced_i4',
            'enhanced-swizzle':'enhanced_swizzle',
            'enhanced-hg20':'enhanced_hg20',
            'enhanced-hg7':'enhanced_hg7',
            'enhanced-sd15':'enhanced_sd15',
            'enhanced-sd27':'enhanced_sd27',
        }, 'Cisco-IOS-XR-controller-otu-cfg', _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-controller-otu-cfg']),
    'OtnPerMon' : _MetaInfoEnum('OtnPerMon',
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_otu_cfg', 'OtnPerMon',
        '''Otn per mon''',
        {
            'disable':'disable',
            'enable':'enable',
        }, 'Cisco-IOS-XR-controller-otu-cfg', _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-controller-otu-cfg']),
    'OtnSendTtiTypeOs' : _MetaInfoEnum('OtnSendTtiTypeOs',
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_otu_cfg', 'OtnSendTtiTypeOs',
        '''Otn send tti type os''',
        {
            'send-tti-os-ascii/os-ascii':'send_tti_os_ascii__FWD_SLASH__os_ascii',
            'send-tti-os-hex/os-hex':'send_tti_os_hex__FWD_SLASH__os_hex',
        }, 'Cisco-IOS-XR-controller-otu-cfg', _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-controller-otu-cfg']),
    'OtnExpTtiTypeSapi' : _MetaInfoEnum('OtnExpTtiTypeSapi',
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_otu_cfg', 'OtnExpTtiTypeSapi',
        '''Otn exp tti type sapi''',
        {
            'exp-tti-sapi-ascii/sapi-ascii':'exp_tti_sapi_ascii__FWD_SLASH__sapi_ascii',
        }, 'Cisco-IOS-XR-controller-otu-cfg', _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-controller-otu-cfg']),
    'OtnSendTtiTypeSapi' : _MetaInfoEnum('OtnSendTtiTypeSapi',
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_otu_cfg', 'OtnSendTtiTypeSapi',
        '''Otn send tti type sapi''',
        {
            'send-tti-sapi-ascii/sapi-ascii':'send_tti_sapi_ascii__FWD_SLASH__sapi_ascii',
        }, 'Cisco-IOS-XR-controller-otu-cfg', _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-controller-otu-cfg']),
    'OtuMode' : _MetaInfoEnum('OtuMode',
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_otu_cfg', 'OtuMode',
        '''Otu mode''',
        {
            'mode-invalid':'mode_invalid',
            'mode-source':'mode_source',
            'mode-sink':'mode_sink',
            'mode-source-sink':'mode_source_sink',
        }, 'Cisco-IOS-XR-controller-otu-cfg', _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-controller-otu-cfg']),
    'OtnSecAdminState' : _MetaInfoEnum('OtnSecAdminState',
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_otu_cfg', 'OtnSecAdminState',
        '''Otn sec admin state''',
        {
            'normal':'normal',
            'maintenance':'maintenance',
        }, 'Cisco-IOS-XR-controller-otu-cfg', _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-controller-otu-cfg']),
    'OtnExpTtiTypeOs' : _MetaInfoEnum('OtnExpTtiTypeOs',
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_otu_cfg', 'OtnExpTtiTypeOs',
        '''Otn exp tti type os''',
        {
            'exp-tti-os-ascii/os-ascii':'exp_tti_os_ascii__FWD_SLASH__os_ascii',
            'exp-tti-os-hex/os-hex':'exp_tti_os_hex__FWD_SLASH__os_hex',
        }, 'Cisco-IOS-XR-controller-otu-cfg', _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-controller-otu-cfg']),
    'OtnLoopback' : _MetaInfoEnum('OtnLoopback',
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_otu_cfg', 'OtnLoopback',
        '''Otn loopback''',
        {
            'line':'line',
            'internal':'internal',
        }, 'Cisco-IOS-XR-controller-otu-cfg', _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-controller-otu-cfg']),
    'OtuPattern' : _MetaInfoEnum('OtuPattern',
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_otu_cfg', 'OtuPattern',
        '''Otu pattern''',
        {
            'pattern-none':'pattern_none',
            'pattern-pn31':'pattern_pn31',
            'pattern-pn23':'pattern_pn23',
            'pattern-pn11':'pattern_pn11',
            'pattern-inverted-pn31':'pattern_inverted_pn31',
            'pattern-inverted-pn11':'pattern_inverted_pn11',
            'pattern-pn15':'pattern_pn15',
        }, 'Cisco-IOS-XR-controller-otu-cfg', _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-controller-otu-cfg']),
    'OtnExpTtiTypeFull' : _MetaInfoEnum('OtnExpTtiTypeFull',
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_otu_cfg', 'OtnExpTtiTypeFull',
        '''Otn exp tti type full''',
        {
            'exp-tti-full-ascii/full-ascii':'exp_tti_full_ascii__FWD_SLASH__full_ascii',
            'exp-tti-hex/hex':'exp_tti_hex__FWD_SLASH__hex',
        }, 'Cisco-IOS-XR-controller-otu-cfg', _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-controller-otu-cfg']),
    'OtnSendTtiTypeFull' : _MetaInfoEnum('OtnSendTtiTypeFull',
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_otu_cfg', 'OtnSendTtiTypeFull',
        '''Otn send tti type full''',
        {
            'send-tti-full-ascii/full-ascii':'send_tti_full_ascii__FWD_SLASH__full_ascii',
            'send-tti-hex/hex':'send_tti_hex__FWD_SLASH__hex',
        }, 'Cisco-IOS-XR-controller-otu-cfg', _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-controller-otu-cfg']),
    'OtnExpTtiTypeDapi' : _MetaInfoEnum('OtnExpTtiTypeDapi',
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_otu_cfg', 'OtnExpTtiTypeDapi',
        '''Otn exp tti type dapi''',
        {
            'exp-tti-dapi-ascii/dapi-ascii':'exp_tti_dapi_ascii__FWD_SLASH__dapi_ascii',
        }, 'Cisco-IOS-XR-controller-otu-cfg', _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-controller-otu-cfg']),
    'OtnSendTtiTypeDapi' : _MetaInfoEnum('OtnSendTtiTypeDapi',
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_otu_cfg', 'OtnSendTtiTypeDapi',
        '''Otn send tti type dapi''',
        {
            'send-tti-dapi-ascii/dapi-ascii':'send_tti_dapi_ascii__FWD_SLASH__dapi_ascii',
        }, 'Cisco-IOS-XR-controller-otu-cfg', _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-controller-otu-cfg']),
}
