
'''
This is auto-generated file,
which includes metadata for module Cisco_IOS_XR_ikev2_cfg
'''

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_LIST, REFERENCE_LEAFLIST, REFERENCE_BITS, REFERENCE_UNION
from ydk._core._dm_meta_info import REFERENCE_CLASS, REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, ANYXML_CLASS
from ydk._core._importer import _yang_ns

_meta_table = {
    'Ikev2.KeyringNames.KeyringName.PeerNames.PeerName.Address' : {
        'meta_info' : _MetaInfoClass('Ikev2.KeyringNames.KeyringName.PeerNames.PeerName.Address', REFERENCE_CLASS,
            '''IP Address to identify the peer''',
            False, 
            [
            _MetaInfoClassMember('ip', ATTRIBUTE, 'str', 'inet:ipv4-address-no-zone',
                None, None,
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'],
                '''                IP Address
                ''',
                'ip',
                'Cisco-IOS-XR-ikev2-cfg', False),
            _MetaInfoClassMember('subnet', ATTRIBUTE, 'str', 'inet:ipv4-address-no-zone',
                None, None,
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'],
                '''                Subnet
                ''',
                'subnet',
                'Cisco-IOS-XR-ikev2-cfg', False),
            ],
            'Cisco-IOS-XR-ikev2-cfg',
            'address',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-ikev2-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ikev2_cfg',
        ),
    },
    'Ikev2.KeyringNames.KeyringName.PeerNames.PeerName.Psk.LocalRemoteKey' : {
        'meta_info' : _MetaInfoClass('Ikev2.KeyringNames.KeyringName.PeerNames.PeerName.Psk.LocalRemoteKey', REFERENCE_CLASS,
            '''Local/Remote pre-shared key for the peer''',
            False, 
            [
            _MetaInfoClassMember('string-xr', ATTRIBUTE, 'str', 'xr:Proprietary-password',
                None, None,
                [], [b'(!.+)|([^!].+)'],
                '''                Local pre-shared key
                ''',
                'string_xr',
                'Cisco-IOS-XR-ikev2-cfg', False),
            _MetaInfoClassMember('string', ATTRIBUTE, 'str', 'xr:Proprietary-password',
                None, None,
                [], [b'(!.+)|([^!].+)'],
                '''                Remote pre-shared key
                ''',
                'string',
                'Cisco-IOS-XR-ikev2-cfg', False),
            ],
            'Cisco-IOS-XR-ikev2-cfg',
            'local-remote-key',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-ikev2-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ikev2_cfg',
        ),
    },
    'Ikev2.KeyringNames.KeyringName.PeerNames.PeerName.Psk' : {
        'meta_info' : _MetaInfoClass('Ikev2.KeyringNames.KeyringName.PeerNames.PeerName.Psk', REFERENCE_CLASS,
            '''Pre-shared key for peer''',
            False, 
            [
            _MetaInfoClassMember('local-remote-key', REFERENCE_CLASS, 'LocalRemoteKey', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ikev2_cfg', 'Ikev2.KeyringNames.KeyringName.PeerNames.PeerName.Psk.LocalRemoteKey',
                [], [],
                '''                Local/Remote pre-shared key for the peer
                ''',
                'local_remote_key',
                'Cisco-IOS-XR-ikev2-cfg', False),
            _MetaInfoClassMember('both-key', ATTRIBUTE, 'str', 'xr:Proprietary-password',
                None, None,
                [], [b'(!.+)|([^!].+)'],
                '''                Both pre-shared key for the peer
                ''',
                'both_key',
                'Cisco-IOS-XR-ikev2-cfg', False),
            ],
            'Cisco-IOS-XR-ikev2-cfg',
            'psk',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-ikev2-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ikev2_cfg',
        ),
    },
    'Ikev2.KeyringNames.KeyringName.PeerNames.PeerName' : {
        'meta_info' : _MetaInfoClass('Ikev2.KeyringNames.KeyringName.PeerNames.PeerName', REFERENCE_LIST,
            '''IKEv2 keyring peer name''',
            False, 
            [
            _MetaInfoClassMember('name', ATTRIBUTE, 'str', 'xr:Cisco-ios-xr-string',
                None, None,
                [(1, 32)], [],
                '''                Name of the keyring-peer
                ''',
                'name',
                'Cisco-IOS-XR-ikev2-cfg', True),
            _MetaInfoClassMember('address', REFERENCE_CLASS, 'Address', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ikev2_cfg', 'Ikev2.KeyringNames.KeyringName.PeerNames.PeerName.Address',
                [], [],
                '''                IP Address to identify the peer
                ''',
                'address',
                'Cisco-IOS-XR-ikev2-cfg', False),
            _MetaInfoClassMember('psk', REFERENCE_CLASS, 'Psk', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ikev2_cfg', 'Ikev2.KeyringNames.KeyringName.PeerNames.PeerName.Psk',
                [], [],
                '''                Pre-shared key for peer
                ''',
                'psk',
                'Cisco-IOS-XR-ikev2-cfg', False),
            _MetaInfoClassMember('peer-sub', ATTRIBUTE, 'Empty', 'empty',
                None, None,
                [], [],
                '''                This indicates existence of keyring-peer
                ''',
                'peer_sub',
                'Cisco-IOS-XR-ikev2-cfg', False),
            ],
            'Cisco-IOS-XR-ikev2-cfg',
            'peer-name',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-ikev2-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ikev2_cfg',
        ),
    },
    'Ikev2.KeyringNames.KeyringName.PeerNames' : {
        'meta_info' : _MetaInfoClass('Ikev2.KeyringNames.KeyringName.PeerNames', REFERENCE_CLASS,
            '''IKEv2 keyring peer config commands''',
            False, 
            [
            _MetaInfoClassMember('peer-name', REFERENCE_LIST, 'PeerName', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ikev2_cfg', 'Ikev2.KeyringNames.KeyringName.PeerNames.PeerName',
                [], [],
                '''                IKEv2 keyring peer name
                ''',
                'peer_name',
                'Cisco-IOS-XR-ikev2-cfg', False),
            ],
            'Cisco-IOS-XR-ikev2-cfg',
            'peer-names',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-ikev2-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ikev2_cfg',
        ),
    },
    'Ikev2.KeyringNames.KeyringName' : {
        'meta_info' : _MetaInfoClass('Ikev2.KeyringNames.KeyringName', REFERENCE_LIST,
            '''IKEv2 keyring name''',
            False, 
            [
            _MetaInfoClassMember('name', ATTRIBUTE, 'str', 'xr:Cisco-ios-xr-string',
                None, None,
                [(1, 32)], [],
                '''                Name of the keyring
                ''',
                'name',
                'Cisco-IOS-XR-ikev2-cfg', True),
            _MetaInfoClassMember('peer-names', REFERENCE_CLASS, 'PeerNames', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ikev2_cfg', 'Ikev2.KeyringNames.KeyringName.PeerNames',
                [], [],
                '''                IKEv2 keyring peer config commands
                ''',
                'peer_names',
                'Cisco-IOS-XR-ikev2-cfg', False),
            _MetaInfoClassMember('keyring-sub', ATTRIBUTE, 'Empty', 'empty',
                None, None,
                [], [],
                '''                This indicated existence of keyring
                ''',
                'keyring_sub',
                'Cisco-IOS-XR-ikev2-cfg', False),
            ],
            'Cisco-IOS-XR-ikev2-cfg',
            'keyring-name',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-ikev2-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ikev2_cfg',
        ),
    },
    'Ikev2.KeyringNames' : {
        'meta_info' : _MetaInfoClass('Ikev2.KeyringNames', REFERENCE_CLASS,
            '''IKEv2 keyring config commands''',
            False, 
            [
            _MetaInfoClassMember('keyring-name', REFERENCE_LIST, 'KeyringName', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ikev2_cfg', 'Ikev2.KeyringNames.KeyringName',
                [], [],
                '''                IKEv2 keyring name
                ''',
                'keyring_name',
                'Cisco-IOS-XR-ikev2-cfg', False),
            ],
            'Cisco-IOS-XR-ikev2-cfg',
            'keyring-names',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-ikev2-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ikev2_cfg',
        ),
    },
    'Ikev2.ProfileNames.ProfileName.MatchIdentity.AddressSubs.AddressSub' : {
        'meta_info' : _MetaInfoClass('Ikev2.ProfileNames.ProfileName.MatchIdentity.AddressSubs.AddressSub', REFERENCE_LIST,
            '''Remote ip address for matching identity''',
            False, 
            [
            _MetaInfoClassMember('address', ATTRIBUTE, 'str', 'inet:ipv4-address-no-zone',
                None, None,
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'],
                '''                Address
                ''',
                'address',
                'Cisco-IOS-XR-ikev2-cfg', True),
            _MetaInfoClassMember('address-sub-val', ATTRIBUTE, 'Empty', 'empty',
                None, None,
                [], [],
                '''                This indicates existence of remote ip
                address
                ''',
                'address_sub_val',
                'Cisco-IOS-XR-ikev2-cfg', False),
            _MetaInfoClassMember('mask', ATTRIBUTE, 'str', 'inet:ipv4-address-no-zone',
                None, None,
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'],
                '''                Mask
                ''',
                'mask',
                'Cisco-IOS-XR-ikev2-cfg', False),
            ],
            'Cisco-IOS-XR-ikev2-cfg',
            'address-sub',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-ikev2-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ikev2_cfg',
        ),
    },
    'Ikev2.ProfileNames.ProfileName.MatchIdentity.AddressSubs' : {
        'meta_info' : _MetaInfoClass('Ikev2.ProfileNames.ProfileName.MatchIdentity.AddressSubs', REFERENCE_CLASS,
            '''Match a profile based on remote identity
address''',
            False, 
            [
            _MetaInfoClassMember('address-sub', REFERENCE_LIST, 'AddressSub', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ikev2_cfg', 'Ikev2.ProfileNames.ProfileName.MatchIdentity.AddressSubs.AddressSub',
                [], [],
                '''                Remote ip address for matching identity
                ''',
                'address_sub',
                'Cisco-IOS-XR-ikev2-cfg', False),
            ],
            'Cisco-IOS-XR-ikev2-cfg',
            'address-subs',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-ikev2-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ikev2_cfg',
        ),
    },
    'Ikev2.ProfileNames.ProfileName.MatchIdentity' : {
        'meta_info' : _MetaInfoClass('Ikev2.ProfileNames.ProfileName.MatchIdentity', REFERENCE_CLASS,
            '''Match a profile based on remote identity''',
            False, 
            [
            _MetaInfoClassMember('address-subs', REFERENCE_CLASS, 'AddressSubs', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ikev2_cfg', 'Ikev2.ProfileNames.ProfileName.MatchIdentity.AddressSubs',
                [], [],
                '''                Match a profile based on remote identity
                address
                ''',
                'address_subs',
                'Cisco-IOS-XR-ikev2-cfg', False),
            _MetaInfoClassMember('any', ATTRIBUTE, 'Empty', 'empty',
                None, None,
                [], [],
                '''                Match any peer identity
                ''',
                'any',
                'Cisco-IOS-XR-ikev2-cfg', False),
            ],
            'Cisco-IOS-XR-ikev2-cfg',
            'match-identity',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-ikev2-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ikev2_cfg',
        ),
    },
    'Ikev2.ProfileNames.ProfileName.Dpd' : {
        'meta_info' : _MetaInfoClass('Ikev2.ProfileNames.ProfileName.Dpd', REFERENCE_CLASS,
            '''Enable IKEv2 liveliness for peers''',
            False, 
            [
            _MetaInfoClassMember('interval', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('10', '3600')], [],
                '''                Interval(in sec)
                ''',
                'interval',
                'Cisco-IOS-XR-ikev2-cfg', False),
            _MetaInfoClassMember('retry-time', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('2', '60')], [],
                '''                Retry interval(in sec)
                ''',
                'retry_time',
                'Cisco-IOS-XR-ikev2-cfg', False),
            ],
            'Cisco-IOS-XR-ikev2-cfg',
            'dpd',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-ikev2-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ikev2_cfg',
        ),
    },
    'Ikev2.ProfileNames.ProfileName' : {
        'meta_info' : _MetaInfoClass('Ikev2.ProfileNames.ProfileName', REFERENCE_LIST,
            '''IKEv2 profile name''',
            False, 
            [
            _MetaInfoClassMember('name', ATTRIBUTE, 'str', 'xr:Cisco-ios-xr-string',
                None, None,
                [(1, 32)], [],
                '''                Name of the profile
                ''',
                'name',
                'Cisco-IOS-XR-ikev2-cfg', True),
            _MetaInfoClassMember('match-identity', REFERENCE_CLASS, 'MatchIdentity', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ikev2_cfg', 'Ikev2.ProfileNames.ProfileName.MatchIdentity',
                [], [],
                '''                Match a profile based on remote identity
                ''',
                'match_identity',
                'Cisco-IOS-XR-ikev2-cfg', False),
            _MetaInfoClassMember('dpd', REFERENCE_CLASS, 'Dpd', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ikev2_cfg', 'Ikev2.ProfileNames.ProfileName.Dpd',
                [], [],
                '''                Enable IKEv2 liveliness for peers
                ''',
                'dpd',
                'Cisco-IOS-XR-ikev2-cfg', False),
            _MetaInfoClassMember('profile-sub', ATTRIBUTE, 'Empty', 'empty',
                None, None,
                [], [],
                '''                This indicates existence of profile
                ''',
                'profile_sub',
                'Cisco-IOS-XR-ikev2-cfg', False),
            _MetaInfoClassMember('lifetime', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('120', '86400')], [],
                '''                Lifetime(in sec) for IKEv2 SA
                ''',
                'lifetime',
                'Cisco-IOS-XR-ikev2-cfg', False),
            _MetaInfoClassMember('keyring-in-profile', ATTRIBUTE, 'str', 'xr:Cisco-ios-xr-string',
                None, None,
                [(1, 32)], [],
                '''                Keyring to use with local/remote
                authentication method
                ''',
                'keyring_in_profile',
                'Cisco-IOS-XR-ikev2-cfg', False),
            ],
            'Cisco-IOS-XR-ikev2-cfg',
            'profile-name',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-ikev2-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ikev2_cfg',
        ),
    },
    'Ikev2.ProfileNames' : {
        'meta_info' : _MetaInfoClass('Ikev2.ProfileNames', REFERENCE_CLASS,
            '''IKEv2 profile config commands''',
            False, 
            [
            _MetaInfoClassMember('profile-name', REFERENCE_LIST, 'ProfileName', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ikev2_cfg', 'Ikev2.ProfileNames.ProfileName',
                [], [],
                '''                IKEv2 profile name
                ''',
                'profile_name',
                'Cisco-IOS-XR-ikev2-cfg', False),
            ],
            'Cisco-IOS-XR-ikev2-cfg',
            'profile-names',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-ikev2-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ikev2_cfg',
        ),
    },
    'Ikev2.PolicyNames.PolicyName.AddressVals.AddressVal' : {
        'meta_info' : _MetaInfoClass('Ikev2.PolicyNames.PolicyName.AddressVals.AddressVal', REFERENCE_LIST,
            '''local address used to match policy''',
            False, 
            [
            _MetaInfoClassMember('address', ATTRIBUTE, 'str', 'inet:ipv4-address-no-zone',
                None, None,
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'],
                '''                Address
                ''',
                'address',
                'Cisco-IOS-XR-ikev2-cfg', True),
            ],
            'Cisco-IOS-XR-ikev2-cfg',
            'address-val',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-ikev2-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ikev2_cfg',
        ),
    },
    'Ikev2.PolicyNames.PolicyName.AddressVals' : {
        'meta_info' : _MetaInfoClass('Ikev2.PolicyNames.PolicyName.AddressVals', REFERENCE_CLASS,
            '''Match a policy based on address''',
            False, 
            [
            _MetaInfoClassMember('address-val', REFERENCE_LIST, 'AddressVal', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ikev2_cfg', 'Ikev2.PolicyNames.PolicyName.AddressVals.AddressVal',
                [], [],
                '''                local address used to match policy
                ''',
                'address_val',
                'Cisco-IOS-XR-ikev2-cfg', False),
            ],
            'Cisco-IOS-XR-ikev2-cfg',
            'address-vals',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-ikev2-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ikev2_cfg',
        ),
    },
    'Ikev2.PolicyNames.PolicyName' : {
        'meta_info' : _MetaInfoClass('Ikev2.PolicyNames.PolicyName', REFERENCE_LIST,
            '''IKEv2 policy name''',
            False, 
            [
            _MetaInfoClassMember('name', ATTRIBUTE, 'str', 'xr:Cisco-ios-xr-string',
                None, None,
                [(1, 32)], [],
                '''                Policy name
                ''',
                'name',
                'Cisco-IOS-XR-ikev2-cfg', True),
            _MetaInfoClassMember('address-vals', REFERENCE_CLASS, 'AddressVals', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ikev2_cfg', 'Ikev2.PolicyNames.PolicyName.AddressVals',
                [], [],
                '''                Match a policy based on address
                ''',
                'address_vals',
                'Cisco-IOS-XR-ikev2-cfg', False),
            _MetaInfoClassMember('proposal-in-policy', ATTRIBUTE, 'str', 'xr:Cisco-ios-xr-string',
                None, None,
                [(1, 32)], [],
                '''                Proposal to use with configured policy
                ''',
                'proposal_in_policy',
                'Cisco-IOS-XR-ikev2-cfg', False),
            _MetaInfoClassMember('policy-sub', ATTRIBUTE, 'Empty', 'empty',
                None, None,
                [], [],
                '''                This indicates existence of policy
                ''',
                'policy_sub',
                'Cisco-IOS-XR-ikev2-cfg', False),
            ],
            'Cisco-IOS-XR-ikev2-cfg',
            'policy-name',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-ikev2-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ikev2_cfg',
        ),
    },
    'Ikev2.PolicyNames' : {
        'meta_info' : _MetaInfoClass('Ikev2.PolicyNames', REFERENCE_CLASS,
            '''Configure IKEv2 policies''',
            False, 
            [
            _MetaInfoClassMember('policy-name', REFERENCE_LIST, 'PolicyName', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ikev2_cfg', 'Ikev2.PolicyNames.PolicyName',
                [], [],
                '''                IKEv2 policy name
                ''',
                'policy_name',
                'Cisco-IOS-XR-ikev2-cfg', False),
            ],
            'Cisco-IOS-XR-ikev2-cfg',
            'policy-names',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-ikev2-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ikev2_cfg',
        ),
    },
    'Ikev2.ProposalNames.ProposalName.Prfses' : {
        'meta_info' : _MetaInfoClass('Ikev2.ProposalNames.ProposalName.Prfses', REFERENCE_CLASS,
            '''Specify one or more transforms of prf''',
            False, 
            [
            _MetaInfoClassMember('prfs', REFERENCE_LEAFLIST, 'str', 'string',
                None, None,
                [(1, 8)], [],
                '''                PRF Algorithm
                ''',
                'prfs',
                'Cisco-IOS-XR-ikev2-cfg', False, max_elements=4),
            ],
            'Cisco-IOS-XR-ikev2-cfg',
            'prfses',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-ikev2-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ikev2_cfg',
        ),
    },
    'Ikev2.ProposalNames.ProposalName.Groups' : {
        'meta_info' : _MetaInfoClass('Ikev2.ProposalNames.ProposalName.Groups', REFERENCE_CLASS,
            '''Specify one or more transforms of group''',
            False, 
            [
            _MetaInfoClassMember('group', REFERENCE_LEAFLIST, 'str', 'string',
                None, None,
                [(1, 3)], [],
                '''                Encryption Algorithm
                ''',
                'group',
                'Cisco-IOS-XR-ikev2-cfg', False, max_elements=8),
            ],
            'Cisco-IOS-XR-ikev2-cfg',
            'groups',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-ikev2-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ikev2_cfg',
        ),
    },
    'Ikev2.ProposalNames.ProposalName.Integrities' : {
        'meta_info' : _MetaInfoClass('Ikev2.ProposalNames.ProposalName.Integrities', REFERENCE_CLASS,
            '''Specify one or more transforms of integrity''',
            False, 
            [
            _MetaInfoClassMember('integrity', REFERENCE_LEAFLIST, 'str', 'string',
                None, None,
                [(1, 8)], [],
                '''                Integrity Algorithm
                ''',
                'integrity',
                'Cisco-IOS-XR-ikev2-cfg', False, max_elements=4),
            ],
            'Cisco-IOS-XR-ikev2-cfg',
            'integrities',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-ikev2-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ikev2_cfg',
        ),
    },
    'Ikev2.ProposalNames.ProposalName.Encryptions' : {
        'meta_info' : _MetaInfoClass('Ikev2.ProposalNames.ProposalName.Encryptions', REFERENCE_CLASS,
            '''Specify one or more transforms of encryption''',
            False, 
            [
            _MetaInfoClassMember('encryption', REFERENCE_LEAFLIST, 'str', 'string',
                None, None,
                [(1, 12)], [],
                '''                Encryption Algorithm
                ''',
                'encryption',
                'Cisco-IOS-XR-ikev2-cfg', False, max_elements=5),
            ],
            'Cisco-IOS-XR-ikev2-cfg',
            'encryptions',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-ikev2-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ikev2_cfg',
        ),
    },
    'Ikev2.ProposalNames.ProposalName' : {
        'meta_info' : _MetaInfoClass('Ikev2.ProposalNames.ProposalName', REFERENCE_LIST,
            '''IKEv2 proposal name''',
            False, 
            [
            _MetaInfoClassMember('name', ATTRIBUTE, 'str', 'xr:Cisco-ios-xr-string',
                None, None,
                [(1, 32)], [],
                '''                Proposal name
                ''',
                'name',
                'Cisco-IOS-XR-ikev2-cfg', True),
            _MetaInfoClassMember('prfses', REFERENCE_CLASS, 'Prfses', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ikev2_cfg', 'Ikev2.ProposalNames.ProposalName.Prfses',
                [], [],
                '''                Specify one or more transforms of prf
                ''',
                'prfses',
                'Cisco-IOS-XR-ikev2-cfg', False),
            _MetaInfoClassMember('groups', REFERENCE_CLASS, 'Groups', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ikev2_cfg', 'Ikev2.ProposalNames.ProposalName.Groups',
                [], [],
                '''                Specify one or more transforms of group
                ''',
                'groups',
                'Cisco-IOS-XR-ikev2-cfg', False),
            _MetaInfoClassMember('integrities', REFERENCE_CLASS, 'Integrities', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ikev2_cfg', 'Ikev2.ProposalNames.ProposalName.Integrities',
                [], [],
                '''                Specify one or more transforms of integrity
                ''',
                'integrities',
                'Cisco-IOS-XR-ikev2-cfg', False),
            _MetaInfoClassMember('encryptions', REFERENCE_CLASS, 'Encryptions', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ikev2_cfg', 'Ikev2.ProposalNames.ProposalName.Encryptions',
                [], [],
                '''                Specify one or more transforms of encryption
                ''',
                'encryptions',
                'Cisco-IOS-XR-ikev2-cfg', False),
            _MetaInfoClassMember('proposal-sub', ATTRIBUTE, 'Empty', 'empty',
                None, None,
                [], [],
                '''                This indicates existence of proposal
                ''',
                'proposal_sub',
                'Cisco-IOS-XR-ikev2-cfg', False),
            ],
            'Cisco-IOS-XR-ikev2-cfg',
            'proposal-name',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-ikev2-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ikev2_cfg',
        ),
    },
    'Ikev2.ProposalNames' : {
        'meta_info' : _MetaInfoClass('Ikev2.ProposalNames', REFERENCE_CLASS,
            '''Configure IKEv2 proposals''',
            False, 
            [
            _MetaInfoClassMember('proposal-name', REFERENCE_LIST, 'ProposalName', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ikev2_cfg', 'Ikev2.ProposalNames.ProposalName',
                [], [],
                '''                IKEv2 proposal name
                ''',
                'proposal_name',
                'Cisco-IOS-XR-ikev2-cfg', False),
            ],
            'Cisco-IOS-XR-ikev2-cfg',
            'proposal-names',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-ikev2-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ikev2_cfg',
        ),
    },
    'Ikev2' : {
        'meta_info' : _MetaInfoClass('Ikev2', REFERENCE_CLASS,
            '''Internet key exchange(IKEv2) config commands''',
            False, 
            [
            _MetaInfoClassMember('keyring-names', REFERENCE_CLASS, 'KeyringNames', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ikev2_cfg', 'Ikev2.KeyringNames',
                [], [],
                '''                IKEv2 keyring config commands
                ''',
                'keyring_names',
                'Cisco-IOS-XR-ikev2-cfg', False),
            _MetaInfoClassMember('profile-names', REFERENCE_CLASS, 'ProfileNames', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ikev2_cfg', 'Ikev2.ProfileNames',
                [], [],
                '''                IKEv2 profile config commands
                ''',
                'profile_names',
                'Cisco-IOS-XR-ikev2-cfg', False),
            _MetaInfoClassMember('policy-names', REFERENCE_CLASS, 'PolicyNames', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ikev2_cfg', 'Ikev2.PolicyNames',
                [], [],
                '''                Configure IKEv2 policies
                ''',
                'policy_names',
                'Cisco-IOS-XR-ikev2-cfg', False),
            _MetaInfoClassMember('proposal-names', REFERENCE_CLASS, 'ProposalNames', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ikev2_cfg', 'Ikev2.ProposalNames',
                [], [],
                '''                Configure IKEv2 proposals
                ''',
                'proposal_names',
                'Cisco-IOS-XR-ikev2-cfg', False),
            ],
            'Cisco-IOS-XR-ikev2-cfg',
            'ikev2',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-ikev2-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ikev2_cfg',
        ),
    },
}
_meta_table['Ikev2.KeyringNames.KeyringName.PeerNames.PeerName.Psk.LocalRemoteKey']['meta_info'].parent =_meta_table['Ikev2.KeyringNames.KeyringName.PeerNames.PeerName.Psk']['meta_info']
_meta_table['Ikev2.KeyringNames.KeyringName.PeerNames.PeerName.Address']['meta_info'].parent =_meta_table['Ikev2.KeyringNames.KeyringName.PeerNames.PeerName']['meta_info']
_meta_table['Ikev2.KeyringNames.KeyringName.PeerNames.PeerName.Psk']['meta_info'].parent =_meta_table['Ikev2.KeyringNames.KeyringName.PeerNames.PeerName']['meta_info']
_meta_table['Ikev2.KeyringNames.KeyringName.PeerNames.PeerName']['meta_info'].parent =_meta_table['Ikev2.KeyringNames.KeyringName.PeerNames']['meta_info']
_meta_table['Ikev2.KeyringNames.KeyringName.PeerNames']['meta_info'].parent =_meta_table['Ikev2.KeyringNames.KeyringName']['meta_info']
_meta_table['Ikev2.KeyringNames.KeyringName']['meta_info'].parent =_meta_table['Ikev2.KeyringNames']['meta_info']
_meta_table['Ikev2.ProfileNames.ProfileName.MatchIdentity.AddressSubs.AddressSub']['meta_info'].parent =_meta_table['Ikev2.ProfileNames.ProfileName.MatchIdentity.AddressSubs']['meta_info']
_meta_table['Ikev2.ProfileNames.ProfileName.MatchIdentity.AddressSubs']['meta_info'].parent =_meta_table['Ikev2.ProfileNames.ProfileName.MatchIdentity']['meta_info']
_meta_table['Ikev2.ProfileNames.ProfileName.MatchIdentity']['meta_info'].parent =_meta_table['Ikev2.ProfileNames.ProfileName']['meta_info']
_meta_table['Ikev2.ProfileNames.ProfileName.Dpd']['meta_info'].parent =_meta_table['Ikev2.ProfileNames.ProfileName']['meta_info']
_meta_table['Ikev2.ProfileNames.ProfileName']['meta_info'].parent =_meta_table['Ikev2.ProfileNames']['meta_info']
_meta_table['Ikev2.PolicyNames.PolicyName.AddressVals.AddressVal']['meta_info'].parent =_meta_table['Ikev2.PolicyNames.PolicyName.AddressVals']['meta_info']
_meta_table['Ikev2.PolicyNames.PolicyName.AddressVals']['meta_info'].parent =_meta_table['Ikev2.PolicyNames.PolicyName']['meta_info']
_meta_table['Ikev2.PolicyNames.PolicyName']['meta_info'].parent =_meta_table['Ikev2.PolicyNames']['meta_info']
_meta_table['Ikev2.ProposalNames.ProposalName.Prfses']['meta_info'].parent =_meta_table['Ikev2.ProposalNames.ProposalName']['meta_info']
_meta_table['Ikev2.ProposalNames.ProposalName.Groups']['meta_info'].parent =_meta_table['Ikev2.ProposalNames.ProposalName']['meta_info']
_meta_table['Ikev2.ProposalNames.ProposalName.Integrities']['meta_info'].parent =_meta_table['Ikev2.ProposalNames.ProposalName']['meta_info']
_meta_table['Ikev2.ProposalNames.ProposalName.Encryptions']['meta_info'].parent =_meta_table['Ikev2.ProposalNames.ProposalName']['meta_info']
_meta_table['Ikev2.ProposalNames.ProposalName']['meta_info'].parent =_meta_table['Ikev2.ProposalNames']['meta_info']
_meta_table['Ikev2.KeyringNames']['meta_info'].parent =_meta_table['Ikev2']['meta_info']
_meta_table['Ikev2.ProfileNames']['meta_info'].parent =_meta_table['Ikev2']['meta_info']
_meta_table['Ikev2.PolicyNames']['meta_info'].parent =_meta_table['Ikev2']['meta_info']
_meta_table['Ikev2.ProposalNames']['meta_info'].parent =_meta_table['Ikev2']['meta_info']
