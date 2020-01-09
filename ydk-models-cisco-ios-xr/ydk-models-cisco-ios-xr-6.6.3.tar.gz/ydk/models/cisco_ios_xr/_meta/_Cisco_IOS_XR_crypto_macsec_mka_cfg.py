
'''
This is auto-generated file,
which includes metadata for module Cisco_IOS_XR_crypto_macsec_mka_cfg
'''

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_LIST, REFERENCE_LEAFLIST, REFERENCE_BITS, REFERENCE_UNION
from ydk._core._dm_meta_info import REFERENCE_CLASS, REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, ANYXML_CLASS
from ydk._core._importer import _yang_ns

_meta_table = {
    'MacsecMkaSecurityPolicy' : _MetaInfoEnum('MacsecMkaSecurityPolicy',
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_macsec_mka_cfg', 'MacsecMkaSecurityPolicy',
        '''Macsec mka security policy''',
        {
            'should-secure':'should_secure',
            'must-secure':'must_secure',
        }, 'Cisco-IOS-XR-crypto-macsec-mka-cfg', _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-crypto-macsec-mka-cfg']),
    'MacsecMkaPolicyException' : _MetaInfoEnum('MacsecMkaPolicyException',
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_macsec_mka_cfg', 'MacsecMkaPolicyException',
        '''Macsec mka policy exception''',
        {
            'lacp-in-clear':'lacp_in_clear',
        }, 'Cisco-IOS-XR-crypto-macsec-mka-cfg', _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-crypto-macsec-mka-cfg']),
    'MacsecMkaCipherSuite' : _MetaInfoEnum('MacsecMkaCipherSuite',
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_macsec_mka_cfg', 'MacsecMkaCipherSuite',
        '''Macsec mka cipher suite''',
        {
            'gcm-aes-128':'gcm_aes_128',
            'gcm-aes-256':'gcm_aes_256',
            'gcm-aes-xpn-128':'gcm_aes_xpn_128',
            'gcm-aes-xpn-256':'gcm_aes_xpn_256',
        }, 'Cisco-IOS-XR-crypto-macsec-mka-cfg', _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-crypto-macsec-mka-cfg']),
    'MacsecMkaConfOffset' : _MetaInfoEnum('MacsecMkaConfOffset',
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_macsec_mka_cfg', 'MacsecMkaConfOffset',
        '''Macsec mka conf offset''',
        {
            'conf-off-set-0':'conf_off_set_0',
            'conf-off-set-30':'conf_off_set_30',
            'conf-off-set-50':'conf_off_set_50',
        }, 'Cisco-IOS-XR-crypto-macsec-mka-cfg', _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-crypto-macsec-mka-cfg']),
    'Macsec.PolicyNames.PolicyName' : {
        'meta_info' : _MetaInfoClass('Macsec.PolicyNames.PolicyName', REFERENCE_LIST,
            '''MACsec Policy Name''',
            False, 
            [
            _MetaInfoClassMember('name', ATTRIBUTE, 'str', 'xr:Cisco-ios-xr-string',
                None, None,
                [(1, 16)], [],
                '''                Name of the Policy of maximum length 16
                ''',
                'name',
                'Cisco-IOS-XR-crypto-macsec-mka-cfg', True),
            _MetaInfoClassMember('delay-protection', ATTRIBUTE, 'Empty', 'empty',
                None, None,
                [], [],
                '''                Enables data delay protection
                ''',
                'delay_protection',
                'Cisco-IOS-XR-crypto-macsec-mka-cfg', False),
            _MetaInfoClassMember('security-policy', REFERENCE_ENUM_CLASS, 'MacsecMkaSecurityPolicy', 'Macsec-mka-security-policy',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_macsec_mka_cfg', 'MacsecMkaSecurityPolicy',
                [], [],
                '''                Security-Policy of Policy
                ''',
                'security_policy',
                'Cisco-IOS-XR-crypto-macsec-mka-cfg', False),
            _MetaInfoClassMember('key-server-priority', ATTRIBUTE, 'int', 'Macsec-mka-key-server-priority',
                None, None,
                [('0', '255')], [],
                '''                Key-Server-Priority of Policy
                ''',
                'key_server_priority',
                'Cisco-IOS-XR-crypto-macsec-mka-cfg', False),
            _MetaInfoClassMember('conf-offset', REFERENCE_ENUM_CLASS, 'MacsecMkaConfOffset', 'Macsec-mka-conf-offset',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_macsec_mka_cfg', 'MacsecMkaConfOffset',
                [], [],
                '''                Conf-Offset of Policy
                ''',
                'conf_offset',
                'Cisco-IOS-XR-crypto-macsec-mka-cfg', False),
            _MetaInfoClassMember('sak-rekey-interval', ATTRIBUTE, 'int', 'Macsec-mka-sak-rekey-interval',
                None, None,
                [('1', '43200')], [],
                '''                DEPRECATED-Interval(in minutes) after which
                key-server generates new SAK for a Secured
                Session, Default: OFF, recommended to use
                seconds option
                ''',
                'sak_rekey_interval',
                'Cisco-IOS-XR-crypto-macsec-mka-cfg', False),
            _MetaInfoClassMember('policy-exception', REFERENCE_ENUM_CLASS, 'MacsecMkaPolicyException', 'Macsec-mka-policy-exception',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_macsec_mka_cfg', 'MacsecMkaPolicyException',
                [], [],
                '''                Macsec policy exception for packets to be in
                clear
                ''',
                'policy_exception',
                'Cisco-IOS-XR-crypto-macsec-mka-cfg', False),
            _MetaInfoClassMember('window-size', ATTRIBUTE, 'int', 'Macsec-mka-window-size',
                None, None,
                [('0', '1024')], [],
                '''                Window-Size of Policy
                ''',
                'window_size',
                'Cisco-IOS-XR-crypto-macsec-mka-cfg', False),
            _MetaInfoClassMember('cipher-suite', REFERENCE_ENUM_CLASS, 'MacsecMkaCipherSuite', 'Macsec-mka-cipher-suite',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_macsec_mka_cfg', 'MacsecMkaCipherSuite',
                [], [],
                '''                Cipher-suite of Policy
                ''',
                'cipher_suite',
                'Cisco-IOS-XR-crypto-macsec-mka-cfg', False),
            _MetaInfoClassMember('include-icv-indicator', ATTRIBUTE, 'Empty', 'empty',
                None, None,
                [], [],
                '''                Enables Include ICV Indicator paramset in
                MKPDU
                ''',
                'include_icv_indicator',
                'Cisco-IOS-XR-crypto-macsec-mka-cfg', False),
            _MetaInfoClassMember('sak-rekey-interval-sec', ATTRIBUTE, 'int', 'Macsec-mka-sak-rekey-interval-sec',
                None, None,
                [('60', '2592000')], [],
                '''                Interval(in seconds) after which key-server
                generates new SAK for a Secured Session,
                Default: OFF
                ''',
                'sak_rekey_interval_sec',
                'Cisco-IOS-XR-crypto-macsec-mka-cfg', False),
            _MetaInfoClassMember('vlan-tags-in-clear', ATTRIBUTE, 'int', 'Macsec-mka-vlan-tags-in-clear',
                None, None,
                [('1', '2')], [],
                '''                VLAN-Tags-In-Clear of Policy
                ''',
                'vlan_tags_in_clear',
                'Cisco-IOS-XR-crypto-macsec-mka-cfg', False),
            ],
            'Cisco-IOS-XR-crypto-macsec-mka-cfg',
            'policy-name',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-crypto-macsec-mka-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_macsec_mka_cfg',
        ),
    },
    'Macsec.PolicyNames' : {
        'meta_info' : _MetaInfoClass('Macsec.PolicyNames', REFERENCE_CLASS,
            '''MACSec Policy''',
            False, 
            [
            _MetaInfoClassMember('policy-name', REFERENCE_LIST, 'PolicyName', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_macsec_mka_cfg', 'Macsec.PolicyNames.PolicyName',
                [], [],
                '''                MACsec Policy Name
                ''',
                'policy_name',
                'Cisco-IOS-XR-crypto-macsec-mka-cfg', False),
            ],
            'Cisco-IOS-XR-crypto-macsec-mka-cfg',
            'policy-names',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-crypto-macsec-mka-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_macsec_mka_cfg',
        ),
    },
    'Macsec' : {
        'meta_info' : _MetaInfoClass('Macsec', REFERENCE_CLASS,
            '''MACSec MKA''',
            False, 
            [
            _MetaInfoClassMember('policy-names', REFERENCE_CLASS, 'PolicyNames', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_macsec_mka_cfg', 'Macsec.PolicyNames',
                [], [],
                '''                MACSec Policy
                ''',
                'policy_names',
                'Cisco-IOS-XR-crypto-macsec-mka-cfg', False),
            _MetaInfoClassMember('shutdown', ATTRIBUTE, 'Empty', 'empty',
                None, None,
                [], [],
                '''                Disable macsec on all data ports(system wide),
                has no impact on macsec configs
                ''',
                'shutdown',
                'Cisco-IOS-XR-crypto-macsec-mka-cfg', False),
            ],
            'Cisco-IOS-XR-crypto-macsec-mka-cfg',
            'macsec',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-crypto-macsec-mka-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_macsec_mka_cfg',
        ),
    },
}
_meta_table['Macsec.PolicyNames.PolicyName']['meta_info'].parent =_meta_table['Macsec.PolicyNames']['meta_info']
_meta_table['Macsec.PolicyNames']['meta_info'].parent =_meta_table['Macsec']['meta_info']
