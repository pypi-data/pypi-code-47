
'''
This is auto-generated file,
which includes metadata for module Cisco_IOS_XR_ppp_ma_ssrp_cfg
'''

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_LIST, REFERENCE_LEAFLIST, REFERENCE_BITS, REFERENCE_UNION
from ydk._core._dm_meta_info import REFERENCE_CLASS, REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, ANYXML_CLASS
from ydk._core._importer import _yang_ns

_meta_table = {
    'Ssrp.Profiles.Profile' : {
        'meta_info' : _MetaInfoClass('Ssrp.Profiles.Profile', REFERENCE_LIST,
            '''SSRP Profile configuration''',
            False, 
            [
            _MetaInfoClassMember('name', ATTRIBUTE, 'str', 'xr:Cisco-ios-xr-string',
                None, None,
                [], [b'[\\w\\-\\.:,_@#%$\\+=\\|;]+'],
                '''                The name of the profile
                ''',
                'name',
                'Cisco-IOS-XR-ppp-ma-ssrp-cfg', True),
            _MetaInfoClassMember('max-hops', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('1', '255')], [],
                '''                This specifies the maximum number of hops for
                packets on the SSO channel
                ''',
                'max_hops',
                'Cisco-IOS-XR-ppp-ma-ssrp-cfg', False),
            _MetaInfoClassMember('peer-ipv4-address', ATTRIBUTE, 'str', 'inet:ipv4-address-no-zone',
                None, None,
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'],
                '''                This specifies the remote end's IPv4-address
                for the SSO channel
                ''',
                'peer_ipv4_address',
                'Cisco-IOS-XR-ppp-ma-ssrp-cfg', False),
            ],
            'Cisco-IOS-XR-ppp-ma-ssrp-cfg',
            'profile',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-ppp-ma-ssrp-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ppp_ma_ssrp_cfg',
        ),
    },
    'Ssrp.Profiles' : {
        'meta_info' : _MetaInfoClass('Ssrp.Profiles', REFERENCE_CLASS,
            '''Table of SSRP Profiles''',
            False, 
            [
            _MetaInfoClassMember('profile', REFERENCE_LIST, 'Profile', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ppp_ma_ssrp_cfg', 'Ssrp.Profiles.Profile',
                [], [],
                '''                SSRP Profile configuration
                ''',
                'profile',
                'Cisco-IOS-XR-ppp-ma-ssrp-cfg', False),
            ],
            'Cisco-IOS-XR-ppp-ma-ssrp-cfg',
            'profiles',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-ppp-ma-ssrp-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ppp_ma_ssrp_cfg',
        ),
    },
    'Ssrp' : {
        'meta_info' : _MetaInfoClass('Ssrp', REFERENCE_CLASS,
            '''Shared plane SSRP configuration data''',
            False, 
            [
            _MetaInfoClassMember('profiles', REFERENCE_CLASS, 'Profiles', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ppp_ma_ssrp_cfg', 'Ssrp.Profiles',
                [], [],
                '''                Table of SSRP Profiles
                ''',
                'profiles',
                'Cisco-IOS-XR-ppp-ma-ssrp-cfg', False),
            ],
            'Cisco-IOS-XR-ppp-ma-ssrp-cfg',
            'ssrp',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-ppp-ma-ssrp-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ppp_ma_ssrp_cfg',
        ),
    },
}
_meta_table['Ssrp.Profiles.Profile']['meta_info'].parent =_meta_table['Ssrp.Profiles']['meta_info']
_meta_table['Ssrp.Profiles']['meta_info'].parent =_meta_table['Ssrp']['meta_info']
