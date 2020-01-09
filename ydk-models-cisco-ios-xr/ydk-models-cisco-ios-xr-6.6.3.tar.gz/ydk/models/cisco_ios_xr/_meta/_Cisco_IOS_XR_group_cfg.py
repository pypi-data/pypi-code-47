
'''
This is auto-generated file,
which includes metadata for module Cisco_IOS_XR_group_cfg
'''

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_LIST, REFERENCE_LEAFLIST, REFERENCE_BITS, REFERENCE_UNION
from ydk._core._dm_meta_info import REFERENCE_CLASS, REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, ANYXML_CLASS
from ydk._core._importer import _yang_ns

_meta_table = {
    'Groups.Group' : {
        'meta_info' : _MetaInfoClass('Groups.Group', REFERENCE_LIST,
            '''Group config definition''',
            False, 
            [
            _MetaInfoClassMember('group-name', ATTRIBUTE, 'str', 'xr:Cisco-ios-xr-string',
                None, None,
                [(0, 32)], [],
                '''                Group name
                ''',
                'group_name',
                'Cisco-IOS-XR-group-cfg', True),
            ],
            'Cisco-IOS-XR-group-cfg',
            'group',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-group-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_group_cfg',
        ),
    },
    'Groups' : {
        'meta_info' : _MetaInfoClass('Groups', REFERENCE_CLASS,
            '''config groups''',
            False, 
            [
            _MetaInfoClassMember('group', REFERENCE_LIST, 'Group', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_group_cfg', 'Groups.Group',
                [], [],
                '''                Group config definition
                ''',
                'group',
                'Cisco-IOS-XR-group-cfg', False),
            ],
            'Cisco-IOS-XR-group-cfg',
            'groups',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-group-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_group_cfg',
        ),
    },
    'ApplyGroups' : {
        'meta_info' : _MetaInfoClass('ApplyGroups', REFERENCE_CLASS,
            '''apply groups''',
            False, 
            [
            _MetaInfoClassMember('apply-group', ATTRIBUTE, 'str', 'xr:Cisco-ios-xr-string',
                None, None,
                [], [b'[\\w\\-\\.:,_@#%$\\+=\\|;]+'],
                '''                apply-group name
                ''',
                'apply_group',
                'Cisco-IOS-XR-group-cfg', False),
            ],
            'Cisco-IOS-XR-group-cfg',
            'apply-groups',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-group-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_group_cfg',
        ),
    },
}
_meta_table['Groups.Group']['meta_info'].parent =_meta_table['Groups']['meta_info']
