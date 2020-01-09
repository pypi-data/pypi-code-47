
'''
This is auto-generated file,
which includes metadata for module Cisco_IOS_XR_aaa_locald_admin_cfg
'''

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_LIST, REFERENCE_LEAFLIST, REFERENCE_BITS, REFERENCE_UNION
from ydk._core._dm_meta_info import REFERENCE_CLASS, REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, ANYXML_CLASS
from ydk._core._importer import _yang_ns

_meta_table = {
    'AaaAdminPassword' : _MetaInfoEnum('AaaAdminPassword',
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_locald_admin_cfg', 'AaaAdminPassword',
        '''Aaa admin password''',
        {
            'type5':'type5',
            'type8':'type8',
            'type9':'type9',
        }, 'Cisco-IOS-XR-aaa-locald-admin-cfg', _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-aaa-locald-admin-cfg']),
    'Aaa.Usernames.Username.UsergroupUnderUsernames.UsergroupUnderUsername' : {
        'meta_info' : _MetaInfoClass('Aaa.Usernames.Username.UsergroupUnderUsernames.UsergroupUnderUsername', REFERENCE_LIST,
            '''Name of the usergroup''',
            False, 
            [
            _MetaInfoClassMember('name', ATTRIBUTE, 'str', 'xr:Cisco-ios-xr-string',
                None, None,
                [], [b'[\\w\\-\\.:,_@#%$\\+=\\|;]+'],
                '''                Name of the usergroup
                ''',
                'name',
                'Cisco-IOS-XR-aaa-locald-admin-cfg', True),
            ],
            'Cisco-IOS-XR-aaa-locald-admin-cfg',
            'usergroup-under-username',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-aaa-locald-admin-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_locald_admin_cfg',
        ),
    },
    'Aaa.Usernames.Username.UsergroupUnderUsernames' : {
        'meta_info' : _MetaInfoClass('Aaa.Usernames.Username.UsergroupUnderUsernames', REFERENCE_CLASS,
            '''Specify the usergroup to which this admin user
belongs''',
            False, 
            [
            _MetaInfoClassMember('usergroup-under-username', REFERENCE_LIST, 'UsergroupUnderUsername', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_locald_admin_cfg', 'Aaa.Usernames.Username.UsergroupUnderUsernames.UsergroupUnderUsername',
                [], [],
                '''                Name of the usergroup
                ''',
                'usergroup_under_username',
                'Cisco-IOS-XR-aaa-locald-admin-cfg', False),
            ],
            'Cisco-IOS-XR-aaa-locald-admin-cfg',
            'usergroup-under-usernames',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-aaa-locald-admin-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_locald_admin_cfg',
        ),
    },
    'Aaa.Usernames.Username.Secret' : {
        'meta_info' : _MetaInfoClass('Aaa.Usernames.Username.Secret', REFERENCE_CLASS,
            '''Specify the secret for the admin user''',
            False, 
            [
            _MetaInfoClassMember('type', REFERENCE_ENUM_CLASS, 'AaaAdminPassword', 'Aaa-admin-password',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_locald_admin_cfg', 'AaaAdminPassword',
                [], [],
                '''                Password type
                ''',
                'type',
                'Cisco-IOS-XR-aaa-locald-admin-cfg', False),
            _MetaInfoClassMember('secret5', ATTRIBUTE, 'str', 'xr:Md5-password',
                None, None,
                [], [b'(!.+)|([^!].+)'],
                '''                The user's secret password
                ''',
                'secret5',
                'Cisco-IOS-XR-aaa-locald-admin-cfg', False, has_when=True),
            _MetaInfoClassMember('secret8', ATTRIBUTE, 'str', 'xr:Type8-password',
                None, None,
                [], [b'(!.+)|([^!].+)'],
                '''                Type 8 password
                ''',
                'secret8',
                'Cisco-IOS-XR-aaa-locald-admin-cfg', False, has_when=True),
            _MetaInfoClassMember('secret9', ATTRIBUTE, 'str', 'xr:Type9-password',
                None, None,
                [], [b'(!.+)|([^!].+)'],
                '''                Type 9 password
                ''',
                'secret9',
                'Cisco-IOS-XR-aaa-locald-admin-cfg', False, has_when=True),
            ],
            'Cisco-IOS-XR-aaa-locald-admin-cfg',
            'secret',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-aaa-locald-admin-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_locald_admin_cfg',
        ),
    },
    'Aaa.Usernames.Username' : {
        'meta_info' : _MetaInfoClass('Aaa.Usernames.Username', REFERENCE_LIST,
            '''Admin Username''',
            False, 
            [
            _MetaInfoClassMember('name', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                Username
                ''',
                'name',
                'Cisco-IOS-XR-aaa-locald-admin-cfg', True),
            _MetaInfoClassMember('usergroup-under-usernames', REFERENCE_CLASS, 'UsergroupUnderUsernames', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_locald_admin_cfg', 'Aaa.Usernames.Username.UsergroupUnderUsernames',
                [], [],
                '''                Specify the usergroup to which this admin user
                belongs
                ''',
                'usergroup_under_usernames',
                'Cisco-IOS-XR-aaa-locald-admin-cfg', False),
            _MetaInfoClassMember('secret', REFERENCE_CLASS, 'Secret', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_locald_admin_cfg', 'Aaa.Usernames.Username.Secret',
                [], [],
                '''                Specify the secret for the admin user
                ''',
                'secret',
                'Cisco-IOS-XR-aaa-locald-admin-cfg', False),
            ],
            'Cisco-IOS-XR-aaa-locald-admin-cfg',
            'username',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-aaa-locald-admin-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_locald_admin_cfg',
        ),
    },
    'Aaa.Usernames' : {
        'meta_info' : _MetaInfoClass('Aaa.Usernames', REFERENCE_CLASS,
            '''Configure local username''',
            False, 
            [
            _MetaInfoClassMember('username', REFERENCE_LIST, 'Username', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_locald_admin_cfg', 'Aaa.Usernames.Username',
                [], [],
                '''                Admin Username
                ''',
                'username',
                'Cisco-IOS-XR-aaa-locald-admin-cfg', False),
            ],
            'Cisco-IOS-XR-aaa-locald-admin-cfg',
            'usernames',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-aaa-locald-admin-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_locald_admin_cfg',
        ),
    },
    'Aaa' : {
        'meta_info' : _MetaInfoClass('Aaa', REFERENCE_CLASS,
            '''Admin plane AAA configuration''',
            False, 
            [
            _MetaInfoClassMember('usernames', REFERENCE_CLASS, 'Usernames', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_locald_admin_cfg', 'Aaa.Usernames',
                [], [],
                '''                Configure local username
                ''',
                'usernames',
                'Cisco-IOS-XR-aaa-locald-admin-cfg', False),
            ],
            'Cisco-IOS-XR-aaa-locald-admin-cfg',
            'aaa',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-aaa-locald-admin-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_locald_admin_cfg',
        ),
    },
}
_meta_table['Aaa.Usernames.Username.UsergroupUnderUsernames.UsergroupUnderUsername']['meta_info'].parent =_meta_table['Aaa.Usernames.Username.UsergroupUnderUsernames']['meta_info']
_meta_table['Aaa.Usernames.Username.UsergroupUnderUsernames']['meta_info'].parent =_meta_table['Aaa.Usernames.Username']['meta_info']
_meta_table['Aaa.Usernames.Username.Secret']['meta_info'].parent =_meta_table['Aaa.Usernames.Username']['meta_info']
_meta_table['Aaa.Usernames.Username']['meta_info'].parent =_meta_table['Aaa.Usernames']['meta_info']
_meta_table['Aaa.Usernames']['meta_info'].parent =_meta_table['Aaa']['meta_info']
