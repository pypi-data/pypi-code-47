
'''
This is auto-generated file,
which includes metadata for module Cisco_IOS_XR_ipv6_smiap_cfg
'''

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_LIST, REFERENCE_LEAFLIST, REFERENCE_BITS, REFERENCE_UNION
from ydk._core._dm_meta_info import REFERENCE_CLASS, REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, ANYXML_CLASS
from ydk._core._importer import _yang_ns

_meta_table = {
    'Ipv6Virtual.Vrfs.Vrf.Address' : {
        'meta_info' : _MetaInfoClass('Ipv6Virtual.Vrfs.Vrf.Address', REFERENCE_CLASS,
            '''IPv6 address and mask''',
            False, 
            [
            _MetaInfoClassMember('address', ATTRIBUTE, 'str', 'inet:ipv6-address-no-zone',
                None, None,
                [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'],
                '''                IPv6 address
                ''',
                'address',
                'Cisco-IOS-XR-ipv6-smiap-cfg', False, is_mandatory=True),
            _MetaInfoClassMember('prefix-length', ATTRIBUTE, 'int', 'xr:Ipv6-prefix-length',
                None, None,
                [('0', '128')], [],
                '''                IPv6 address prefix length
                ''',
                'prefix_length',
                'Cisco-IOS-XR-ipv6-smiap-cfg', False, is_mandatory=True),
            ],
            'Cisco-IOS-XR-ipv6-smiap-cfg',
            'address',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-ipv6-smiap-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_smiap_cfg',
            is_presence=True,
        ),
    },
    'Ipv6Virtual.Vrfs.Vrf' : {
        'meta_info' : _MetaInfoClass('Ipv6Virtual.Vrfs.Vrf', REFERENCE_LIST,
            '''A VRF for a virtual IPv6 address.  Specify
'default' for VRF default''',
            False, 
            [
            _MetaInfoClassMember('vrf-name', ATTRIBUTE, 'str', 'xr:Cisco-ios-xr-string',
                None, None,
                [], [b'[\\w\\-\\.:,_@#%$\\+=\\|;]+'],
                '''                Name of VRF
                ''',
                'vrf_name',
                'Cisco-IOS-XR-ipv6-smiap-cfg', True),
            _MetaInfoClassMember('address', REFERENCE_CLASS, 'Address', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_smiap_cfg', 'Ipv6Virtual.Vrfs.Vrf.Address',
                [], [],
                '''                IPv6 address and mask
                ''',
                'address',
                'Cisco-IOS-XR-ipv6-smiap-cfg', False, is_presence=True),
            ],
            'Cisco-IOS-XR-ipv6-smiap-cfg',
            'vrf',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-ipv6-smiap-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_smiap_cfg',
        ),
    },
    'Ipv6Virtual.Vrfs' : {
        'meta_info' : _MetaInfoClass('Ipv6Virtual.Vrfs', REFERENCE_CLASS,
            '''VRFs for the virtual IPv6 addresses''',
            False, 
            [
            _MetaInfoClassMember('vrf', REFERENCE_LIST, 'Vrf', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_smiap_cfg', 'Ipv6Virtual.Vrfs.Vrf',
                [], [],
                '''                A VRF for a virtual IPv6 address.  Specify
                'default' for VRF default
                ''',
                'vrf',
                'Cisco-IOS-XR-ipv6-smiap-cfg', False),
            ],
            'Cisco-IOS-XR-ipv6-smiap-cfg',
            'vrfs',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-ipv6-smiap-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_smiap_cfg',
        ),
    },
    'Ipv6Virtual' : {
        'meta_info' : _MetaInfoClass('Ipv6Virtual', REFERENCE_CLASS,
            '''IPv6 virtual address for management interfaces''',
            False, 
            [
            _MetaInfoClassMember('vrfs', REFERENCE_CLASS, 'Vrfs', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_smiap_cfg', 'Ipv6Virtual.Vrfs',
                [], [],
                '''                VRFs for the virtual IPv6 addresses
                ''',
                'vrfs',
                'Cisco-IOS-XR-ipv6-smiap-cfg', False),
            _MetaInfoClassMember('use-as-source-address', ATTRIBUTE, 'Empty', 'empty',
                None, None,
                [], [],
                '''                Enable use as default source address on sourced
                packets
                ''',
                'use_as_source_address',
                'Cisco-IOS-XR-ipv6-smiap-cfg', False),
            ],
            'Cisco-IOS-XR-ipv6-smiap-cfg',
            'ipv6-virtual',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-ipv6-smiap-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_smiap_cfg',
        ),
    },
}
_meta_table['Ipv6Virtual.Vrfs.Vrf.Address']['meta_info'].parent =_meta_table['Ipv6Virtual.Vrfs.Vrf']['meta_info']
_meta_table['Ipv6Virtual.Vrfs.Vrf']['meta_info'].parent =_meta_table['Ipv6Virtual.Vrfs']['meta_info']
_meta_table['Ipv6Virtual.Vrfs']['meta_info'].parent =_meta_table['Ipv6Virtual']['meta_info']
