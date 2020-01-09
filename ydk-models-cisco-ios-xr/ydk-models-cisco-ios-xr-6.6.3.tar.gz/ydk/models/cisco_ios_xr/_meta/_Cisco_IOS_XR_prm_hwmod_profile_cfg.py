
'''
This is auto-generated file,
which includes metadata for module Cisco_IOS_XR_prm_hwmod_profile_cfg
'''

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_LIST, REFERENCE_LEAFLIST, REFERENCE_BITS, REFERENCE_UNION
from ydk._core._dm_meta_info import REFERENCE_CLASS, REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, ANYXML_CLASS
from ydk._core._importer import _yang_ns

_meta_table = {
    'ProfileTypeData' : _MetaInfoEnum('ProfileTypeData',
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_prm_hwmod_profile_cfg', 'ProfileTypeData',
        '''Profile type data''',
        {
            'sp':'sp',
            'dc':'dc',
        }, 'Cisco-IOS-XR-prm-hwmod-profile-cfg', _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-prm-hwmod-profile-cfg']),
    'HardwareModule' : {
        'meta_info' : _MetaInfoClass('HardwareModule', REFERENCE_CLASS,
            '''HardwareModule''',
            False, 
            [
            _MetaInfoClassMember('profile', REFERENCE_ENUM_CLASS, 'ProfileTypeData', 'Profile-type-data',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_prm_hwmod_profile_cfg', 'ProfileTypeData',
                [], [],
                '''                Specify Profile type
                ''',
                'profile',
                'Cisco-IOS-XR-prm-hwmod-profile-cfg', False),
            ],
            'Cisco-IOS-XR-prm-hwmod-profile-cfg',
            'hardware-module',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-prm-hwmod-profile-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_prm_hwmod_profile_cfg',
        ),
    },
}
