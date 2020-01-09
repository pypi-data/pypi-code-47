
'''
This is auto-generated file,
which includes metadata for module Cisco_IOS_XR_pbr_vrf_policy_cfg
'''

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_LIST, REFERENCE_LEAFLIST, REFERENCE_BITS, REFERENCE_UNION
from ydk._core._dm_meta_info import REFERENCE_CLASS, REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, ANYXML_CLASS
from ydk._core._importer import _yang_ns

_meta_table = {
    'VrfPolicy.Vrf.Afi' : {
        'meta_info' : _MetaInfoClass('VrfPolicy.Vrf.Afi', REFERENCE_LIST,
            '''address family''',
            False, 
            [
            _MetaInfoClassMember('afi-type', ATTRIBUTE, 'str', 'Pbr-afi',
                None, None,
                [], [b'(ipv4)|(ipv6)'],
                '''                AFI name
                ''',
                'afi_type',
                'Cisco-IOS-XR-pbr-vrf-policy-cfg', True),
            _MetaInfoClassMember('service-policy-in', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                Policy map name
                ''',
                'service_policy_in',
                'Cisco-IOS-XR-pbr-vrf-policy-cfg', False),
            ],
            'Cisco-IOS-XR-pbr-vrf-policy-cfg',
            'afi',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-pbr-vrf-policy-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_pbr_vrf_policy_cfg',
        ),
    },
    'VrfPolicy.Vrf' : {
        'meta_info' : _MetaInfoClass('VrfPolicy.Vrf', REFERENCE_LIST,
            '''VRF Name''',
            False, 
            [
            _MetaInfoClassMember('vrf-name', ATTRIBUTE, 'str', 'xr:Cisco-ios-xr-string',
                None, None,
                [], [b'[\\w\\-\\.:,_@#%$\\+=\\|;]+'],
                '''                VRF name
                ''',
                'vrf_name',
                'Cisco-IOS-XR-pbr-vrf-policy-cfg', True),
            _MetaInfoClassMember('afi', REFERENCE_LIST, 'Afi', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_pbr_vrf_policy_cfg', 'VrfPolicy.Vrf.Afi',
                [], [],
                '''                address family
                ''',
                'afi',
                'Cisco-IOS-XR-pbr-vrf-policy-cfg', False),
            ],
            'Cisco-IOS-XR-pbr-vrf-policy-cfg',
            'vrf',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-pbr-vrf-policy-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_pbr_vrf_policy_cfg',
        ),
    },
    'VrfPolicy' : {
        'meta_info' : _MetaInfoClass('VrfPolicy', REFERENCE_CLASS,
            '''VRF Policy PBR configuration''',
            False, 
            [
            _MetaInfoClassMember('vrf', REFERENCE_LIST, 'Vrf', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_pbr_vrf_policy_cfg', 'VrfPolicy.Vrf',
                [], [],
                '''                VRF Name
                ''',
                'vrf',
                'Cisco-IOS-XR-pbr-vrf-policy-cfg', False),
            ],
            'Cisco-IOS-XR-pbr-vrf-policy-cfg',
            'vrf-policy',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-pbr-vrf-policy-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_pbr_vrf_policy_cfg',
        ),
    },
}
_meta_table['VrfPolicy.Vrf.Afi']['meta_info'].parent =_meta_table['VrfPolicy.Vrf']['meta_info']
_meta_table['VrfPolicy.Vrf']['meta_info'].parent =_meta_table['VrfPolicy']['meta_info']
