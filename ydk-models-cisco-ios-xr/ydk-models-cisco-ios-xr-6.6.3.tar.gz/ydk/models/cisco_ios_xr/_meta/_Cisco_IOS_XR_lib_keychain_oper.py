
'''
This is auto-generated file,
which includes metadata for module Cisco_IOS_XR_lib_keychain_oper
'''

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_LIST, REFERENCE_LEAFLIST, REFERENCE_BITS, REFERENCE_UNION
from ydk._core._dm_meta_info import REFERENCE_CLASS, REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, ANYXML_CLASS
from ydk._core._importer import _yang_ns

_meta_table = {
    'CrytoAlgo' : _MetaInfoEnum('CrytoAlgo',
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_keychain_oper', 'CrytoAlgo',
        '''Cryptographic algorithm type''',
        {
            'not-configured':'not_configured',
            'aes-128-cmac-96':'aes_128_cmac_96',
            'hmac-sha1-12':'hmac_sha1_12',
            'md5':'md5',
            'sha1':'sha1',
            'hmac-md5':'hmac_md5',
            'hmac-sha1-20':'hmac_sha1_20',
            'aes-128-cmac':'aes_128_cmac',
            'aes-256-cmac':'aes_256_cmac',
            'hmac-sha1-96':'hmac_sha1_96',
            'hmac-sha-256':'hmac_sha_256',
        }, 'Cisco-IOS-XR-lib-keychain-oper', _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-lib-keychain-oper']),
    'Enc' : _MetaInfoEnum('Enc',
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_keychain_oper', 'Enc',
        '''Type of password encryption''',
        {
            'password-type7':'password_type7',
            'password-type6':'password_type6',
        }, 'Cisco-IOS-XR-lib-keychain-oper', _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-lib-keychain-oper']),
    'Keychain.Keys.Key.Key_.KeyId.Macsec' : {
        'meta_info' : _MetaInfoClass('Keychain.Keys.Key.Key_.KeyId.Macsec', REFERENCE_CLASS,
            '''To check if it's a macsec key''',
            False, 
            [
            _MetaInfoClassMember('is-macsec-key', ATTRIBUTE, 'bool', 'boolean',
                None, None,
                [], [],
                '''                To check if it's a macsec key
                ''',
                'is_macsec_key',
                'Cisco-IOS-XR-lib-keychain-oper', False, is_config=False),
            ],
            'Cisco-IOS-XR-lib-keychain-oper',
            'macsec',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-lib-keychain-oper'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_keychain_oper',
            is_config=False,
        ),
    },
    'Keychain.Keys.Key.Key_.KeyId.SendLifetime' : {
        'meta_info' : _MetaInfoClass('Keychain.Keys.Key.Key_.KeyId.SendLifetime', REFERENCE_CLASS,
            '''Lifetime of the key''',
            False, 
            [
            _MetaInfoClassMember('start', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                Key life start time in format : day-of-week
                month date-of-month HH:MM:SS year eg: Thu Feb 1
                18:32:14 2011
                ''',
                'start',
                'Cisco-IOS-XR-lib-keychain-oper', False, is_config=False),
            _MetaInfoClassMember('end', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                Key life end time in format : day-of-week month
                date-of-month HH:MM:SS year eg: Thu Feb 1 18:32
                :14 2011
                ''',
                'end',
                'Cisco-IOS-XR-lib-keychain-oper', False, is_config=False),
            _MetaInfoClassMember('duration', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                Duration of the key in seconds. value 0xffffffff
                reflects infinite, never expires, is configured 
                ''',
                'duration',
                'Cisco-IOS-XR-lib-keychain-oper', False, is_config=False),
            _MetaInfoClassMember('is-always-valid', ATTRIBUTE, 'bool', 'boolean',
                None, None,
                [], [],
                '''                Is TRUE if duration is 0xffffffff 
                ''',
                'is_always_valid',
                'Cisco-IOS-XR-lib-keychain-oper', False, is_config=False),
            _MetaInfoClassMember('is-valid-now', ATTRIBUTE, 'bool', 'boolean',
                None, None,
                [], [],
                '''                Is TRUE if current time is betweenstart and end
                lifetime , else FALSE
                ''',
                'is_valid_now',
                'Cisco-IOS-XR-lib-keychain-oper', False, is_config=False),
            ],
            'Cisco-IOS-XR-lib-keychain-oper',
            'send-lifetime',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-lib-keychain-oper'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_keychain_oper',
            is_config=False,
        ),
    },
    'Keychain.Keys.Key.Key_.KeyId.AcceptLifetime' : {
        'meta_info' : _MetaInfoClass('Keychain.Keys.Key.Key_.KeyId.AcceptLifetime', REFERENCE_CLASS,
            '''Accept Lifetime of the key''',
            False, 
            [
            _MetaInfoClassMember('start', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                Key life start time in format : day-of-week
                month date-of-month HH:MM:SS year eg: Thu Feb 1
                18:32:14 2011
                ''',
                'start',
                'Cisco-IOS-XR-lib-keychain-oper', False, is_config=False),
            _MetaInfoClassMember('end', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                Key life end time in format : day-of-week month
                date-of-month HH:MM:SS year eg: Thu Feb 1 18:32
                :14 2011
                ''',
                'end',
                'Cisco-IOS-XR-lib-keychain-oper', False, is_config=False),
            _MetaInfoClassMember('duration', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                Duration of the key in seconds. value 0xffffffff
                reflects infinite, never expires, is configured 
                ''',
                'duration',
                'Cisco-IOS-XR-lib-keychain-oper', False, is_config=False),
            _MetaInfoClassMember('is-always-valid', ATTRIBUTE, 'bool', 'boolean',
                None, None,
                [], [],
                '''                Is TRUE if duration is 0xffffffff 
                ''',
                'is_always_valid',
                'Cisco-IOS-XR-lib-keychain-oper', False, is_config=False),
            _MetaInfoClassMember('is-valid-now', ATTRIBUTE, 'bool', 'boolean',
                None, None,
                [], [],
                '''                Is TRUE if current time is betweenstart and end
                lifetime , else FALSE
                ''',
                'is_valid_now',
                'Cisco-IOS-XR-lib-keychain-oper', False, is_config=False),
            ],
            'Cisco-IOS-XR-lib-keychain-oper',
            'accept-lifetime',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-lib-keychain-oper'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_keychain_oper',
            is_config=False,
        ),
    },
    'Keychain.Keys.Key.Key_.KeyId' : {
        'meta_info' : _MetaInfoClass('Keychain.Keys.Key.Key_.KeyId', REFERENCE_LIST,
            '''key id''',
            False, 
            [
            _MetaInfoClassMember('macsec', REFERENCE_CLASS, 'Macsec', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_keychain_oper', 'Keychain.Keys.Key.Key_.KeyId.Macsec',
                [], [],
                '''                To check if it's a macsec key
                ''',
                'macsec',
                'Cisco-IOS-XR-lib-keychain-oper', False, is_config=False),
            _MetaInfoClassMember('send-lifetime', REFERENCE_CLASS, 'SendLifetime', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_keychain_oper', 'Keychain.Keys.Key.Key_.KeyId.SendLifetime',
                [], [],
                '''                Lifetime of the key
                ''',
                'send_lifetime',
                'Cisco-IOS-XR-lib-keychain-oper', False, is_config=False),
            _MetaInfoClassMember('accept-lifetime', REFERENCE_CLASS, 'AcceptLifetime', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_keychain_oper', 'Keychain.Keys.Key.Key_.KeyId.AcceptLifetime',
                [], [],
                '''                Accept Lifetime of the key
                ''',
                'accept_lifetime',
                'Cisco-IOS-XR-lib-keychain-oper', False, is_config=False),
            _MetaInfoClassMember('key-string', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                Key string
                ''',
                'key_string',
                'Cisco-IOS-XR-lib-keychain-oper', False, is_config=False),
            _MetaInfoClassMember('type', REFERENCE_ENUM_CLASS, 'Enc', 'Enc',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_keychain_oper', 'Enc',
                [], [],
                '''                Type of key encryption
                ''',
                'type',
                'Cisco-IOS-XR-lib-keychain-oper', False, is_config=False),
            _MetaInfoClassMember('key-id', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                Key ID
                ''',
                'key_id',
                'Cisco-IOS-XR-lib-keychain-oper', False, is_config=False),
            _MetaInfoClassMember('cryptographic-algorithm', REFERENCE_ENUM_CLASS, 'CrytoAlgo', 'Cryto-algo',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_keychain_oper', 'CrytoAlgo',
                [], [],
                '''                Cryptographic algorithm
                ''',
                'cryptographic_algorithm',
                'Cisco-IOS-XR-lib-keychain-oper', False, is_config=False),
            ],
            'Cisco-IOS-XR-lib-keychain-oper',
            'key-id',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-lib-keychain-oper'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_keychain_oper',
            is_config=False,
        ),
    },
    'Keychain.Keys.Key.Key_' : {
        'meta_info' : _MetaInfoClass('Keychain.Keys.Key.Key_', REFERENCE_CLASS,
            '''Key properties''',
            False, 
            [
            _MetaInfoClassMember('key-id', REFERENCE_LIST, 'KeyId', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_keychain_oper', 'Keychain.Keys.Key.Key_.KeyId',
                [], [],
                '''                key id
                ''',
                'key_id',
                'Cisco-IOS-XR-lib-keychain-oper', False, is_config=False),
            ],
            'Cisco-IOS-XR-lib-keychain-oper',
            'key',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-lib-keychain-oper'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_keychain_oper',
            is_config=False,
        ),
    },
    'Keychain.Keys.Key' : {
        'meta_info' : _MetaInfoClass('Keychain.Keys.Key', REFERENCE_LIST,
            '''Configured key name''',
            False, 
            [
            _MetaInfoClassMember('key-name', ATTRIBUTE, 'str', 'xr:Cisco-ios-xr-string',
                None, None,
                [], [b'[\\w\\-\\.:,_@#%$\\+=\\|;]+'],
                '''                Key name
                ''',
                'key_name',
                'Cisco-IOS-XR-lib-keychain-oper', True, is_config=False),
            _MetaInfoClassMember('key', REFERENCE_CLASS, 'Key_', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_keychain_oper', 'Keychain.Keys.Key.Key_',
                [], [],
                '''                Key properties
                ''',
                'key',
                'Cisco-IOS-XR-lib-keychain-oper', False, is_config=False),
            _MetaInfoClassMember('accept-tolerance', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                Accept tolerance is infinite if value is
                0xffffffff
                ''',
                'accept_tolerance',
                'Cisco-IOS-XR-lib-keychain-oper', False, is_config=False),
            ],
            'Cisco-IOS-XR-lib-keychain-oper',
            'key',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-lib-keychain-oper'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_keychain_oper',
            is_config=False,
        ),
    },
    'Keychain.Keys' : {
        'meta_info' : _MetaInfoClass('Keychain.Keys', REFERENCE_CLASS,
            '''List of configured key names''',
            False, 
            [
            _MetaInfoClassMember('key', REFERENCE_LIST, 'Key', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_keychain_oper', 'Keychain.Keys.Key',
                [], [],
                '''                Configured key name
                ''',
                'key',
                'Cisco-IOS-XR-lib-keychain-oper', False, is_config=False),
            ],
            'Cisco-IOS-XR-lib-keychain-oper',
            'keys',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-lib-keychain-oper'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_keychain_oper',
            is_config=False,
        ),
    },
    'Keychain' : {
        'meta_info' : _MetaInfoClass('Keychain', REFERENCE_CLASS,
            '''Keychain operational data''',
            False, 
            [
            _MetaInfoClassMember('keys', REFERENCE_CLASS, 'Keys', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_keychain_oper', 'Keychain.Keys',
                [], [],
                '''                List of configured key names
                ''',
                'keys',
                'Cisco-IOS-XR-lib-keychain-oper', False, is_config=False),
            ],
            'Cisco-IOS-XR-lib-keychain-oper',
            'keychain',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-lib-keychain-oper'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_keychain_oper',
            is_config=False,
        ),
    },
}
_meta_table['Keychain.Keys.Key.Key_.KeyId.Macsec']['meta_info'].parent =_meta_table['Keychain.Keys.Key.Key_.KeyId']['meta_info']
_meta_table['Keychain.Keys.Key.Key_.KeyId.SendLifetime']['meta_info'].parent =_meta_table['Keychain.Keys.Key.Key_.KeyId']['meta_info']
_meta_table['Keychain.Keys.Key.Key_.KeyId.AcceptLifetime']['meta_info'].parent =_meta_table['Keychain.Keys.Key.Key_.KeyId']['meta_info']
_meta_table['Keychain.Keys.Key.Key_.KeyId']['meta_info'].parent =_meta_table['Keychain.Keys.Key.Key_']['meta_info']
_meta_table['Keychain.Keys.Key.Key_']['meta_info'].parent =_meta_table['Keychain.Keys.Key']['meta_info']
_meta_table['Keychain.Keys.Key']['meta_info'].parent =_meta_table['Keychain.Keys']['meta_info']
_meta_table['Keychain.Keys']['meta_info'].parent =_meta_table['Keychain']['meta_info']
