
'''
This is auto-generated file,
which includes metadata for module Cisco_IOS_XR_sysadmin_fpd_infra_cli_fpd
'''

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_LIST, REFERENCE_LEAFLIST, REFERENCE_BITS, REFERENCE_UNION
from ydk._core._dm_meta_info import REFERENCE_CLASS, REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, ANYXML_CLASS
from ydk._core._importer import _yang_ns

_meta_table = {
    'Fpd.Config.AutoUpgrade' : _MetaInfoEnum('AutoUpgrade',
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_fpd_infra_cli_fpd', 'Fpd.Config.AutoUpgrade',
        ''' ''',
        {
            'enable':'enable',
            'disable':'disable',
        }, 'Cisco-IOS-XR-sysadmin-fpd-infra-cli-fpd', _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-sysadmin-fpd-infra-cli-fpd']),
    'Fpd.Config' : {
        'meta_info' : _MetaInfoClass('Fpd.Config', REFERENCE_CLASS,
            '''fpd config mode''',
            False, 
            [
            _MetaInfoClassMember('auto-upgrade', REFERENCE_ENUM_CLASS, 'AutoUpgrade', 'enumeration',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_fpd_infra_cli_fpd', 'Fpd.Config.AutoUpgrade',
                [], [],
                '''                ''',
                'auto_upgrade',
                'Cisco-IOS-XR-sysadmin-fpd-infra-cli-fpd', False, default_value='Cisco_IOS_XR_sysadmin_fpd_infra_cli_fpd.Fpd.Config.AutoUpgrade.disable'),
            ],
            'Cisco-IOS-XR-sysadmin-fpd-infra-cli-fpd',
            'config',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-sysadmin-fpd-infra-cli-fpd'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_fpd_infra_cli_fpd',
        ),
    },
    'Fpd' : {
        'meta_info' : _MetaInfoClass('Fpd', REFERENCE_CLASS,
            ''' ''',
            False, 
            [
            _MetaInfoClassMember('config', REFERENCE_CLASS, 'Config', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_fpd_infra_cli_fpd', 'Fpd.Config',
                [], [],
                '''                fpd config mode
                ''',
                'config',
                'Cisco-IOS-XR-sysadmin-fpd-infra-cli-fpd', False),
            ],
            'Cisco-IOS-XR-sysadmin-fpd-infra-cli-fpd',
            'fpd',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-sysadmin-fpd-infra-cli-fpd'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_fpd_infra_cli_fpd',
        ),
    },
}
_meta_table['Fpd.Config']['meta_info'].parent =_meta_table['Fpd']['meta_info']
