
'''
This is auto-generated file,
which includes metadata for module Cisco_IOS_XR_lib_keychain_masterkey_aes_cfg
'''

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_LIST, REFERENCE_LEAFLIST, REFERENCE_BITS, REFERENCE_UNION
from ydk._core._dm_meta_info import REFERENCE_CLASS, REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, ANYXML_CLASS
from ydk._core._importer import _yang_ns

_meta_table = {
    'KeyEncryption' : _MetaInfoEnum('KeyEncryption',
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_keychain_masterkey_aes_cfg', 'KeyEncryption',
        '''Key encryption''',
        {
            'type6':'type6',
        }, 'Cisco-IOS-XR-lib-keychain-masterkey-aes-cfg', _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-lib-keychain-masterkey-aes-cfg']),
    'Password.Encryption' : {
        'meta_info' : _MetaInfoClass('Password.Encryption', REFERENCE_CLASS,
            '''Enable password encryption''',
            False, 
            [
            _MetaInfoClassMember('aes', REFERENCE_ENUM_CLASS, 'KeyEncryption', 'Key-encryption',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_keychain_masterkey_aes_cfg', 'KeyEncryption',
                [], [],
                '''                encryption type used to store key
                ''',
                'aes',
                'Cisco-IOS-XR-lib-keychain-masterkey-aes-cfg', False),
            ],
            'Cisco-IOS-XR-lib-keychain-masterkey-aes-cfg',
            'encryption',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-lib-keychain-masterkey-aes-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_keychain_masterkey_aes_cfg',
        ),
    },
    'Password' : {
        'meta_info' : _MetaInfoClass('Password', REFERENCE_CLASS,
            '''Configure masterkey''',
            False, 
            [
            _MetaInfoClassMember('encryption', REFERENCE_CLASS, 'Encryption', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_keychain_masterkey_aes_cfg', 'Password.Encryption',
                [], [],
                '''                Enable password encryption
                ''',
                'encryption',
                'Cisco-IOS-XR-lib-keychain-masterkey-aes-cfg', False),
            ],
            'Cisco-IOS-XR-lib-keychain-masterkey-aes-cfg',
            'password',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-lib-keychain-masterkey-aes-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_keychain_masterkey_aes_cfg',
        ),
    },
}
_meta_table['Password.Encryption']['meta_info'].parent =_meta_table['Password']['meta_info']
