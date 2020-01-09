
'''
This is auto-generated file,
which includes metadata for module Cisco_IOS_XR_upgrade_fpd_ng_act
'''

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_LIST, REFERENCE_LEAFLIST, REFERENCE_BITS, REFERENCE_UNION
from ydk._core._dm_meta_info import REFERENCE_CLASS, REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, ANYXML_CLASS
from ydk._core._importer import _yang_ns

_meta_table = {
    'UpgradeFpd.Input' : {
        'meta_info' : _MetaInfoClass('UpgradeFpd.Input', REFERENCE_CLASS,
            ''' ''',
            False, 
            [
            _MetaInfoClassMember('location', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                Location of the FPD to be upgraded
                ''',
                'location',
                'Cisco-IOS-XR-upgrade-fpd-ng-act', False, is_mandatory=True),
            _MetaInfoClassMember('fpd', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                name of the fpd to be upgraded
                ''',
                'fpd',
                'Cisco-IOS-XR-upgrade-fpd-ng-act', False, is_mandatory=True),
            _MetaInfoClassMember('force', ATTRIBUTE, 'Empty', 'empty',
                None, None,
                [], [],
                '''                Force the upgrade process
                ''',
                'force',
                'Cisco-IOS-XR-upgrade-fpd-ng-act', False),
            ],
            'Cisco-IOS-XR-upgrade-fpd-ng-act',
            'input',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-upgrade-fpd-ng-act'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_upgrade_fpd_ng_act',
        ),
    },
    'UpgradeFpd' : {
        'meta_info' : _MetaInfoClass('UpgradeFpd', REFERENCE_CLASS,
            '''Execute FPD upgrade''',
            False, 
            [
            _MetaInfoClassMember('input', REFERENCE_CLASS, 'Input', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_upgrade_fpd_ng_act', 'UpgradeFpd.Input',
                [], [],
                '''                ''',
                'input',
                'Cisco-IOS-XR-upgrade-fpd-ng-act', False),
            ],
            'Cisco-IOS-XR-upgrade-fpd-ng-act',
            'upgrade-fpd',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-upgrade-fpd-ng-act'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_upgrade_fpd_ng_act',
        ),
    },
}
_meta_table['UpgradeFpd.Input']['meta_info'].parent =_meta_table['UpgradeFpd']['meta_info']
