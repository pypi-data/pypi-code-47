
'''
This is auto-generated file,
which includes metadata for module Cisco_IOS_XR_prm_hwmod_cfg
'''

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_LIST, REFERENCE_LEAFLIST, REFERENCE_BITS, REFERENCE_UNION
from ydk._core._dm_meta_info import REFERENCE_CLASS, REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, ANYXML_CLASS
from ydk._core._importer import _yang_ns

_meta_table = {
    'UrpfConfig' : _MetaInfoEnum('UrpfConfig',
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_prm_hwmod_cfg', 'UrpfConfig',
        '''Urpf config''',
        {
            'disable':'disable',
            'enable':'enable',
        }, 'Cisco-IOS-XR-prm-hwmod-cfg', _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-prm-hwmod-cfg']),
    'HardwareModule.Loadbalancing.Bgp3107.Ecmp' : {
        'meta_info' : _MetaInfoClass('HardwareModule.Loadbalancing.Bgp3107.Ecmp', REFERENCE_CLASS,
            '''ECMP ''',
            False, 
            [
            _MetaInfoClassMember('enable', ATTRIBUTE, 'Empty', 'empty',
                None, None,
                [], [],
                '''                Enable Option
                ''',
                'enable',
                'Cisco-IOS-XR-prm-hwmod-cfg', False),
            ],
            'Cisco-IOS-XR-prm-hwmod-cfg',
            'ecmp',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-prm-hwmod-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_prm_hwmod_cfg',
        ),
    },
    'HardwareModule.Loadbalancing.Bgp3107' : {
        'meta_info' : _MetaInfoClass('HardwareModule.Loadbalancing.Bgp3107', REFERENCE_CLASS,
            '''BGP LU''',
            False, 
            [
            _MetaInfoClassMember('ecmp', REFERENCE_CLASS, 'Ecmp', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_prm_hwmod_cfg', 'HardwareModule.Loadbalancing.Bgp3107.Ecmp',
                [], [],
                '''                ECMP 
                ''',
                'ecmp',
                'Cisco-IOS-XR-prm-hwmod-cfg', False),
            ],
            'Cisco-IOS-XR-prm-hwmod-cfg',
            'bgp3107',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-prm-hwmod-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_prm_hwmod_cfg',
        ),
    },
    'HardwareModule.Loadbalancing' : {
        'meta_info' : _MetaInfoClass('HardwareModule.Loadbalancing', REFERENCE_CLASS,
            '''Loadbalance option''',
            False, 
            [
            _MetaInfoClassMember('bgp3107', REFERENCE_CLASS, 'Bgp3107', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_prm_hwmod_cfg', 'HardwareModule.Loadbalancing.Bgp3107',
                [], [],
                '''                BGP LU
                ''',
                'bgp3107',
                'Cisco-IOS-XR-prm-hwmod-cfg', False),
            ],
            'Cisco-IOS-XR-prm-hwmod-cfg',
            'loadbalancing',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-prm-hwmod-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_prm_hwmod_cfg',
        ),
    },
    'HardwareModule' : {
        'meta_info' : _MetaInfoClass('HardwareModule', REFERENCE_CLASS,
            '''HardwareModule''',
            False, 
            [
            _MetaInfoClassMember('loadbalancing', REFERENCE_CLASS, 'Loadbalancing', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_prm_hwmod_cfg', 'HardwareModule.Loadbalancing',
                [], [],
                '''                Loadbalance option
                ''',
                'loadbalancing',
                'Cisco-IOS-XR-prm-hwmod-cfg', False),
            _MetaInfoClassMember('urpf', REFERENCE_ENUM_CLASS, 'UrpfConfig', 'Urpf-config',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_prm_hwmod_cfg', 'UrpfConfig',
                [], [],
                '''                Enabled Disabled
                ''',
                'urpf',
                'Cisco-IOS-XR-prm-hwmod-cfg', False),
            ],
            'Cisco-IOS-XR-prm-hwmod-cfg',
            'hardware-module',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-prm-hwmod-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_prm_hwmod_cfg',
        ),
    },
}
_meta_table['HardwareModule.Loadbalancing.Bgp3107.Ecmp']['meta_info'].parent =_meta_table['HardwareModule.Loadbalancing.Bgp3107']['meta_info']
_meta_table['HardwareModule.Loadbalancing.Bgp3107']['meta_info'].parent =_meta_table['HardwareModule.Loadbalancing']['meta_info']
_meta_table['HardwareModule.Loadbalancing']['meta_info'].parent =_meta_table['HardwareModule']['meta_info']
