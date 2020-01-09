
'''
This is auto-generated file,
which includes metadata for module Cisco_IOS_XR_asr9k_fia_cfg
'''

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_LIST, REFERENCE_LEAFLIST, REFERENCE_BITS, REFERENCE_UNION
from ydk._core._dm_meta_info import REFERENCE_CLASS, REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, ANYXML_CLASS
from ydk._core._importer import _yang_ns

_meta_table = {
    'FabricFiaConfig.FiaIntfPolicer' : {
        'meta_info' : _MetaInfoClass('FabricFiaConfig.FiaIntfPolicer', REFERENCE_CLASS,
            '''FIA interface rate-limiter on 7-Fabric LC''',
            False, 
            [
            _MetaInfoClassMember('disable', ATTRIBUTE, 'bool', 'boolean',
                None, None,
                [], [],
                '''                disable FIA interface policer 
                ''',
                'disable',
                'Cisco-IOS-XR-asr9k-fia-cfg', False),
            ],
            'Cisco-IOS-XR-asr9k-fia-cfg',
            'fia-intf-policer',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-asr9k-fia-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_fia_cfg',
        ),
    },
    'FabricFiaConfig' : {
        'meta_info' : _MetaInfoClass('FabricFiaConfig', REFERENCE_CLASS,
            '''Configure Global Fabric Fia Settings''',
            False, 
            [
            _MetaInfoClassMember('fia-intf-policer', REFERENCE_CLASS, 'FiaIntfPolicer', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_fia_cfg', 'FabricFiaConfig.FiaIntfPolicer',
                [], [],
                '''                FIA interface rate-limiter on 7-Fabric LC
                ''',
                'fia_intf_policer',
                'Cisco-IOS-XR-asr9k-fia-cfg', False),
            ],
            'Cisco-IOS-XR-asr9k-fia-cfg',
            'fabric-fia-config',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-asr9k-fia-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_fia_cfg',
        ),
    },
}
_meta_table['FabricFiaConfig.FiaIntfPolicer']['meta_info'].parent =_meta_table['FabricFiaConfig']['meta_info']
