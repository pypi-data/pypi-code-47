
'''
This is auto-generated file,
which includes metadata for module Cisco_IOS_XR_asr9k_fab_cfg
'''

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_LIST, REFERENCE_LEAFLIST, REFERENCE_BITS, REFERENCE_UNION
from ydk._core._dm_meta_info import REFERENCE_CLASS, REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, ANYXML_CLASS
from ydk._core._importer import _yang_ns

_meta_table = {
    'Asr9kFabMode' : _MetaInfoEnum('Asr9kFabMode',
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_fab_cfg', 'Asr9kFabMode',
        '''Asr9k fab mode''',
        {
            'highbandwidth':'highbandwidth',
            'a99-highbandwidth':'a99_highbandwidth',
        }, 'Cisco-IOS-XR-asr9k-fab-cfg', _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-asr9k-fab-cfg']),
    'FabVqiConfig.Mode' : {
        'meta_info' : _MetaInfoClass('FabVqiConfig.Mode', REFERENCE_CLASS,
            '''Mode Type''',
            False, 
            [
            _MetaInfoClassMember('fab-mode-type-xr', REFERENCE_ENUM_CLASS, 'Asr9kFabMode', 'Asr9k-fab-mode',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_fab_cfg', 'Asr9kFabMode',
                [], [],
                '''                Mode Type
                ''',
                'fab_mode_type_xr',
                'Cisco-IOS-XR-asr9k-fab-cfg', False),
            _MetaInfoClassMember('fab-mode-type', REFERENCE_ENUM_CLASS, 'Asr9kFabMode', 'Asr9k-fab-mode',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_fab_cfg', 'Asr9kFabMode',
                [], [],
                '''                Mode Type
                ''',
                'fab_mode_type',
                'Cisco-IOS-XR-asr9k-fab-cfg', False),
            ],
            'Cisco-IOS-XR-asr9k-fab-cfg',
            'mode',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-asr9k-fab-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_fab_cfg',
        ),
    },
    'FabVqiConfig' : {
        'meta_info' : _MetaInfoClass('FabVqiConfig', REFERENCE_CLASS,
            '''Configure Fabric Operation Mode''',
            False, 
            [
            _MetaInfoClassMember('mode', REFERENCE_CLASS, 'Mode', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_fab_cfg', 'FabVqiConfig.Mode',
                [], [],
                '''                Mode Type
                ''',
                'mode',
                'Cisco-IOS-XR-asr9k-fab-cfg', False),
            ],
            'Cisco-IOS-XR-asr9k-fab-cfg',
            'fab-vqi-config',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-asr9k-fab-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_fab_cfg',
        ),
    },
}
_meta_table['FabVqiConfig.Mode']['meta_info'].parent =_meta_table['FabVqiConfig']['meta_info']
