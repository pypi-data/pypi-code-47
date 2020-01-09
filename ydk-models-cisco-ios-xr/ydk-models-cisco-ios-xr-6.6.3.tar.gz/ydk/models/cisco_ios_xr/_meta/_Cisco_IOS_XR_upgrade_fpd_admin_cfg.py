
'''
This is auto-generated file,
which includes metadata for module Cisco_IOS_XR_upgrade_fpd_admin_cfg
'''

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_LIST, REFERENCE_LEAFLIST, REFERENCE_BITS, REFERENCE_UNION
from ydk._core._dm_meta_info import REFERENCE_CLASS, REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, ANYXML_CLASS
from ydk._core._importer import _yang_ns

_meta_table = {
    'Fpd' : {
        'meta_info' : _MetaInfoClass('Fpd', REFERENCE_CLASS,
            '''Configuration for fpd auto-upgrade''',
            False, 
            [
            _MetaInfoClassMember('auto-upgrade', ATTRIBUTE, 'bool', 'boolean',
                None, None,
                [], [],
                '''                Variable for fpd auto-upgrade enable/disable
                ''',
                'auto_upgrade',
                'Cisco-IOS-XR-upgrade-fpd-admin-cfg', False),
            _MetaInfoClassMember('auto-reload', ATTRIBUTE, 'bool', 'boolean',
                None, None,
                [], [],
                '''                Variable for fpd auto-reload enable/disable
                ''',
                'auto_reload',
                'Cisco-IOS-XR-upgrade-fpd-admin-cfg', False),
            ],
            'Cisco-IOS-XR-upgrade-fpd-admin-cfg',
            'fpd',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-upgrade-fpd-admin-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_upgrade_fpd_admin_cfg',
        ),
    },
}
