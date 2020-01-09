
'''
This is auto-generated file,
which includes metadata for module Cisco_IOS_XR_crypto_sam_cfg
'''

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_LIST, REFERENCE_LEAFLIST, REFERENCE_BITS, REFERENCE_UNION
from ydk._core._dm_meta_info import REFERENCE_CLASS, REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, ANYXML_CLASS
from ydk._core._importer import _yang_ns

_meta_table = {
    'CryptoSamAction' : _MetaInfoEnum('CryptoSamAction',
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_sam_cfg', 'CryptoSamAction',
        '''Crypto sam action''',
        {
            'proceed':'proceed',
            'terminate':'terminate',
        }, 'Cisco-IOS-XR-crypto-sam-cfg', _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-crypto-sam-cfg']),
    'Sam.PromptInterval' : {
        'meta_info' : _MetaInfoClass('Sam.PromptInterval', REFERENCE_CLASS,
            '''Set prompt interval at reboot time''',
            False, 
            [
            _MetaInfoClassMember('action', REFERENCE_ENUM_CLASS, 'CryptoSamAction', 'Crypto-sam-action',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_sam_cfg', 'CryptoSamAction',
                [], [],
                '''                Respond to SAM prompt either Proceed/Terminate
                ''',
                'action',
                'Cisco-IOS-XR-crypto-sam-cfg', False, is_mandatory=True),
            _MetaInfoClassMember('prompt-time', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('0', '300')], [],
                '''                Prompt time from 0 - 300 seconds
                ''',
                'prompt_time',
                'Cisco-IOS-XR-crypto-sam-cfg', False, is_mandatory=True),
            ],
            'Cisco-IOS-XR-crypto-sam-cfg',
            'prompt-interval',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-crypto-sam-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_sam_cfg',
            is_presence=True,
        ),
    },
    'Sam' : {
        'meta_info' : _MetaInfoClass('Sam', REFERENCE_CLASS,
            '''Software Authentication Manager (SAM) Config''',
            False, 
            [
            _MetaInfoClassMember('prompt-interval', REFERENCE_CLASS, 'PromptInterval', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_sam_cfg', 'Sam.PromptInterval',
                [], [],
                '''                Set prompt interval at reboot time
                ''',
                'prompt_interval',
                'Cisco-IOS-XR-crypto-sam-cfg', False, is_presence=True),
            ],
            'Cisco-IOS-XR-crypto-sam-cfg',
            'sam',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-crypto-sam-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_sam_cfg',
        ),
    },
}
_meta_table['Sam.PromptInterval']['meta_info'].parent =_meta_table['Sam']['meta_info']
