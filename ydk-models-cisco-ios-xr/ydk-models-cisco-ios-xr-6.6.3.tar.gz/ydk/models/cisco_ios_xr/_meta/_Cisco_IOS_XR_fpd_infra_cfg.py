
'''
This is auto-generated file,
which includes metadata for module Cisco_IOS_XR_fpd_infra_cfg
'''

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_LIST, REFERENCE_LEAFLIST, REFERENCE_BITS, REFERENCE_UNION
from ydk._core._dm_meta_info import REFERENCE_CLASS, REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, ANYXML_CLASS
from ydk._core._importer import _yang_ns

_meta_table = {
    'AutoReload' : _MetaInfoEnum('AutoReload',
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_fpd_infra_cfg', 'AutoReload',
        '''Auto reload''',
        {
            'disable':'disable',
            'enable':'enable',
        }, 'Cisco-IOS-XR-fpd-infra-cfg', _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-fpd-infra-cfg']),
    'AutoUpgrade' : _MetaInfoEnum('AutoUpgrade',
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_fpd_infra_cfg', 'AutoUpgrade',
        '''Auto upgrade''',
        {
            'disable':'disable',
            'enable':'enable',
        }, 'Cisco-IOS-XR-fpd-infra-cfg', _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-fpd-infra-cfg']),
    'Fpd' : {
        'meta_info' : _MetaInfoClass('Fpd', REFERENCE_CLASS,
            '''Configuration for fpd auto-upgrade enable/disable''',
            False, 
            [
            _MetaInfoClassMember('auto-reload', REFERENCE_ENUM_CLASS, 'AutoReload', 'Auto-reload',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_fpd_infra_cfg', 'AutoReload',
                [], [],
                '''                Variable for fpd auto-reload enable/disable
                ''',
                'auto_reload',
                'Cisco-IOS-XR-fpd-infra-cfg', False),
            _MetaInfoClassMember('auto-upgrade', REFERENCE_ENUM_CLASS, 'AutoUpgrade', 'Auto-upgrade',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_fpd_infra_cfg', 'AutoUpgrade',
                [], [],
                '''                Variable for fpd auto-upgrade enable/disable
                ''',
                'auto_upgrade',
                'Cisco-IOS-XR-fpd-infra-cfg', False),
            ],
            'Cisco-IOS-XR-fpd-infra-cfg',
            'fpd',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-fpd-infra-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_fpd_infra_cfg',
        ),
    },
}
