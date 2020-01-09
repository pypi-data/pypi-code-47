
'''
This is auto-generated file,
which includes metadata for module Cisco_IOS_XR_dot1x_cfg
'''

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_LIST, REFERENCE_LEAFLIST, REFERENCE_BITS, REFERENCE_UNION
from ydk._core._dm_meta_info import REFERENCE_CLASS, REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, ANYXML_CLASS
from ydk._core._importer import _yang_ns

_meta_table = {
    'Dot1xServerDeadAction' : _MetaInfoEnum('Dot1xServerDeadAction',
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_dot1x_cfg', 'Dot1xServerDeadAction',
        '''Dot1x server dead action''',
        {
            'auth-fail':'auth_fail',
            'auth-retry':'auth_retry',
        }, 'Cisco-IOS-XR-dot1x-cfg', _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-dot1x-cfg']),
    'Dot1x.Dot1xProfile.Supplicant' : {
        'meta_info' : _MetaInfoClass('Dot1x.Dot1xProfile.Supplicant', REFERENCE_CLASS,
            '''Dot1x Supplicant Related Configuration''',
            False, 
            [
            _MetaInfoClassMember('eap-profile', ATTRIBUTE, 'str', 'string',
                None, None,
                [(1, 63)], [],
                '''                EAP Profile for Supplicant
                ''',
                'eap_profile',
                'Cisco-IOS-XR-dot1x-cfg', False),
            ],
            'Cisco-IOS-XR-dot1x-cfg',
            'supplicant',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-dot1x-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_dot1x_cfg',
        ),
    },
    'Dot1x.Dot1xProfile.Authenticator.Timers.ReauthTime' : {
        'meta_info' : _MetaInfoClass('Dot1x.Dot1xProfile.Authenticator.Timers.ReauthTime', REFERENCE_CLASS,
            '''After this time ReAuthentication will be
trigerred''',
            False, 
            [
            _MetaInfoClassMember('server', ATTRIBUTE, 'bool', 'boolean',
                None, None,
                [], [],
                '''                Reauth will be triggerred based on the EAP
                server configuration
                ''',
                'server',
                'Cisco-IOS-XR-dot1x-cfg', False),
            _MetaInfoClassMember('local', ATTRIBUTE, 'int', 'Dot1x-reauth-local-interval',
                None, None,
                [('60', '5184000')], [],
                '''                Reauth will be triggerred based on the
                configuration in box
                ''',
                'local',
                'Cisco-IOS-XR-dot1x-cfg', False),
            ],
            'Cisco-IOS-XR-dot1x-cfg',
            'reauth-time',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-dot1x-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_dot1x_cfg',
        ),
    },
    'Dot1x.Dot1xProfile.Authenticator.Timers' : {
        'meta_info' : _MetaInfoClass('Dot1x.Dot1xProfile.Authenticator.Timers', REFERENCE_CLASS,
            '''Timers for Authenticator''',
            False, 
            [
            _MetaInfoClassMember('reauth-time', REFERENCE_CLASS, 'ReauthTime', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_dot1x_cfg', 'Dot1x.Dot1xProfile.Authenticator.Timers.ReauthTime',
                [], [],
                '''                After this time ReAuthentication will be
                trigerred
                ''',
                'reauth_time',
                'Cisco-IOS-XR-dot1x-cfg', False),
            ],
            'Cisco-IOS-XR-dot1x-cfg',
            'timers',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-dot1x-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_dot1x_cfg',
        ),
    },
    'Dot1x.Dot1xProfile.Authenticator' : {
        'meta_info' : _MetaInfoClass('Dot1x.Dot1xProfile.Authenticator', REFERENCE_CLASS,
            '''Dot1x Authenticator Related Configuration''',
            False, 
            [
            _MetaInfoClassMember('timers', REFERENCE_CLASS, 'Timers', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_dot1x_cfg', 'Dot1x.Dot1xProfile.Authenticator.Timers',
                [], [],
                '''                Timers for Authenticator
                ''',
                'timers',
                'Cisco-IOS-XR-dot1x-cfg', False),
            _MetaInfoClassMember('eap-profile', ATTRIBUTE, 'str', 'string',
                None, None,
                [(1, 63)], [],
                '''                EAP Profile for Local EAP Server
                ''',
                'eap_profile',
                'Cisco-IOS-XR-dot1x-cfg', False),
            _MetaInfoClassMember('server-dead', REFERENCE_ENUM_CLASS, 'Dot1xServerDeadAction', 'Dot1x-server-dead-action',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_dot1x_cfg', 'Dot1xServerDeadAction',
                [], [],
                '''                dot1x authenticator action on AAA server
                unreachability
                ''',
                'server_dead',
                'Cisco-IOS-XR-dot1x-cfg', False),
            ],
            'Cisco-IOS-XR-dot1x-cfg',
            'authenticator',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-dot1x-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_dot1x_cfg',
        ),
    },
    'Dot1x.Dot1xProfile' : {
        'meta_info' : _MetaInfoClass('Dot1x.Dot1xProfile', REFERENCE_LIST,
            '''Global Dot1x Profile Name''',
            False, 
            [
            _MetaInfoClassMember('profile-name', ATTRIBUTE, 'str', 'xr:Cisco-ios-xr-string',
                None, None,
                [(1, 63)], [],
                '''                Name of the Dot1x Profile
                ''',
                'profile_name',
                'Cisco-IOS-XR-dot1x-cfg', True),
            _MetaInfoClassMember('supplicant', REFERENCE_CLASS, 'Supplicant', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_dot1x_cfg', 'Dot1x.Dot1xProfile.Supplicant',
                [], [],
                '''                Dot1x Supplicant Related Configuration
                ''',
                'supplicant',
                'Cisco-IOS-XR-dot1x-cfg', False),
            _MetaInfoClassMember('authenticator', REFERENCE_CLASS, 'Authenticator', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_dot1x_cfg', 'Dot1x.Dot1xProfile.Authenticator',
                [], [],
                '''                Dot1x Authenticator Related Configuration
                ''',
                'authenticator',
                'Cisco-IOS-XR-dot1x-cfg', False),
            _MetaInfoClassMember('pae', ATTRIBUTE, 'str', 'Dot1xpae',
                None, None,
                [], [b'(supplicant)|(authenticator)|(both)'],
                '''                Dot1x PAE (Port Access Entity) Role
                ''',
                'pae',
                'Cisco-IOS-XR-dot1x-cfg', False),
            ],
            'Cisco-IOS-XR-dot1x-cfg',
            'dot1x-profile',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-dot1x-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_dot1x_cfg',
        ),
    },
    'Dot1x' : {
        'meta_info' : _MetaInfoClass('Dot1x', REFERENCE_CLASS,
            '''Global Dot1x Configuration''',
            False, 
            [
            _MetaInfoClassMember('dot1x-profile', REFERENCE_LIST, 'Dot1xProfile', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_dot1x_cfg', 'Dot1x.Dot1xProfile',
                [], [],
                '''                Global Dot1x Profile Name
                ''',
                'dot1x_profile',
                'Cisco-IOS-XR-dot1x-cfg', False),
            ],
            'Cisco-IOS-XR-dot1x-cfg',
            'dot1x',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-dot1x-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_dot1x_cfg',
        ),
    },
    'Eap.EapProfile.Eaptls' : {
        'meta_info' : _MetaInfoClass('Eap.EapProfile.Eaptls', REFERENCE_CLASS,
            '''EAP TLS Configuration''',
            False, 
            [
            _MetaInfoClassMember('pki-trustpoint', ATTRIBUTE, 'str', 'xr:Cisco-ios-xr-string',
                None, None,
                [(1, 63)], [],
                '''                Configure PKI Trustpoint
                ''',
                'pki_trustpoint',
                'Cisco-IOS-XR-dot1x-cfg', False),
            ],
            'Cisco-IOS-XR-dot1x-cfg',
            'eaptls',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-dot1x-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_dot1x_cfg',
        ),
    },
    'Eap.EapProfile' : {
        'meta_info' : _MetaInfoClass('Eap.EapProfile', REFERENCE_LIST,
            '''Global EAP Profile Configuration''',
            False, 
            [
            _MetaInfoClassMember('profile-name', ATTRIBUTE, 'str', 'xr:Cisco-ios-xr-string',
                None, None,
                [(1, 63)], [],
                '''                Name of the EAP Profile
                ''',
                'profile_name',
                'Cisco-IOS-XR-dot1x-cfg', True),
            _MetaInfoClassMember('eaptls', REFERENCE_CLASS, 'Eaptls', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_dot1x_cfg', 'Eap.EapProfile.Eaptls',
                [], [],
                '''                EAP TLS Configuration
                ''',
                'eaptls',
                'Cisco-IOS-XR-dot1x-cfg', False),
            _MetaInfoClassMember('allow-eap-tls1-0', ATTRIBUTE, 'Empty', 'empty',
                None, None,
                [], [],
                '''                Configure backward compatibility for TLS 1.0
                ''',
                'allow_eap_tls1_0',
                'Cisco-IOS-XR-dot1x-cfg', False),
            _MetaInfoClassMember('identity', ATTRIBUTE, 'str', 'string',
                None, None,
                [(1, 63)], [],
                '''                Configure EAP Identity/UserName
                ''',
                'identity',
                'Cisco-IOS-XR-dot1x-cfg', False),
            ],
            'Cisco-IOS-XR-dot1x-cfg',
            'eap-profile',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-dot1x-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_dot1x_cfg',
        ),
    },
    'Eap' : {
        'meta_info' : _MetaInfoClass('Eap', REFERENCE_CLASS,
            '''eap''',
            False, 
            [
            _MetaInfoClassMember('eap-profile', REFERENCE_LIST, 'EapProfile', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_dot1x_cfg', 'Eap.EapProfile',
                [], [],
                '''                Global EAP Profile Configuration
                ''',
                'eap_profile',
                'Cisco-IOS-XR-dot1x-cfg', False),
            ],
            'Cisco-IOS-XR-dot1x-cfg',
            'eap',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-dot1x-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_dot1x_cfg',
        ),
    },
}
_meta_table['Dot1x.Dot1xProfile.Authenticator.Timers.ReauthTime']['meta_info'].parent =_meta_table['Dot1x.Dot1xProfile.Authenticator.Timers']['meta_info']
_meta_table['Dot1x.Dot1xProfile.Authenticator.Timers']['meta_info'].parent =_meta_table['Dot1x.Dot1xProfile.Authenticator']['meta_info']
_meta_table['Dot1x.Dot1xProfile.Supplicant']['meta_info'].parent =_meta_table['Dot1x.Dot1xProfile']['meta_info']
_meta_table['Dot1x.Dot1xProfile.Authenticator']['meta_info'].parent =_meta_table['Dot1x.Dot1xProfile']['meta_info']
_meta_table['Dot1x.Dot1xProfile']['meta_info'].parent =_meta_table['Dot1x']['meta_info']
_meta_table['Eap.EapProfile.Eaptls']['meta_info'].parent =_meta_table['Eap.EapProfile']['meta_info']
_meta_table['Eap.EapProfile']['meta_info'].parent =_meta_table['Eap']['meta_info']
