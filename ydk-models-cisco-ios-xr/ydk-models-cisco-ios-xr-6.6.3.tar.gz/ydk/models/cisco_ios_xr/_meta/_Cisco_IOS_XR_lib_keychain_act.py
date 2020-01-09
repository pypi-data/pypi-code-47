
'''
This is auto-generated file,
which includes metadata for module Cisco_IOS_XR_lib_keychain_act
'''

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_LIST, REFERENCE_LEAFLIST, REFERENCE_BITS, REFERENCE_UNION
from ydk._core._dm_meta_info import REFERENCE_CLASS, REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, ANYXML_CLASS
from ydk._core._importer import _yang_ns

_meta_table = {
    'MasterKeyAdd.Input' : {
        'meta_info' : _MetaInfoClass('MasterKeyAdd.Input', REFERENCE_CLASS,
            ''' ''',
            False, 
            [
            _MetaInfoClassMember('new-key', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                New master key to be added
                ''',
                'new_key',
                'Cisco-IOS-XR-lib-keychain-act', False),
            ],
            'Cisco-IOS-XR-lib-keychain-act',
            'input',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-lib-keychain-act'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_keychain_act',
        ),
    },
    'MasterKeyAdd' : {
        'meta_info' : _MetaInfoClass('MasterKeyAdd', REFERENCE_CLASS,
            '''To add a new master key''',
            False, 
            [
            _MetaInfoClassMember('input', REFERENCE_CLASS, 'Input', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_keychain_act', 'MasterKeyAdd.Input',
                [], [],
                '''                ''',
                'input',
                'Cisco-IOS-XR-lib-keychain-act', False),
            ],
            'Cisco-IOS-XR-lib-keychain-act',
            'master-key-add',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-lib-keychain-act'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_keychain_act',
        ),
    },
    'MasterKeyDelete' : {
        'meta_info' : _MetaInfoClass('MasterKeyDelete', REFERENCE_CLASS,
            '''Remove Master key''',
            False, 
            [
            ],
            'Cisco-IOS-XR-lib-keychain-act',
            'master-key-delete',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-lib-keychain-act'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_keychain_act',
        ),
    },
    'MasterKeyUpdate.Input' : {
        'meta_info' : _MetaInfoClass('MasterKeyUpdate.Input', REFERENCE_CLASS,
            ''' ''',
            False, 
            [
            _MetaInfoClassMember('old-key', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                key already added/key to be replaced
                ''',
                'old_key',
                'Cisco-IOS-XR-lib-keychain-act', False, is_mandatory=True),
            _MetaInfoClassMember('new-key', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                New master key to be added 
                ''',
                'new_key',
                'Cisco-IOS-XR-lib-keychain-act', False, is_mandatory=True),
            ],
            'Cisco-IOS-XR-lib-keychain-act',
            'input',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-lib-keychain-act'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_keychain_act',
        ),
    },
    'MasterKeyUpdate' : {
        'meta_info' : _MetaInfoClass('MasterKeyUpdate', REFERENCE_CLASS,
            '''To update master key''',
            False, 
            [
            _MetaInfoClassMember('input', REFERENCE_CLASS, 'Input', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_keychain_act', 'MasterKeyUpdate.Input',
                [], [],
                '''                ''',
                'input',
                'Cisco-IOS-XR-lib-keychain-act', False),
            ],
            'Cisco-IOS-XR-lib-keychain-act',
            'master-key-update',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-lib-keychain-act'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_keychain_act',
        ),
    },
}
_meta_table['MasterKeyAdd.Input']['meta_info'].parent =_meta_table['MasterKeyAdd']['meta_info']
_meta_table['MasterKeyUpdate.Input']['meta_info'].parent =_meta_table['MasterKeyUpdate']['meta_info']
