
'''
This is auto-generated file,
which includes metadata for module Cisco_IOS_XR_ip_iarm_v6_oper
'''

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_LIST, REFERENCE_LEAFLIST, REFERENCE_BITS, REFERENCE_UNION
from ydk._core._dm_meta_info import REFERENCE_CLASS, REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, ANYXML_CLASS
from ydk._core._importer import _yang_ns

_meta_table = {
    'Ipv6arm.Addresses.Vrfs.Vrf.Networks.Network.AddressXr.Address' : {
        'meta_info' : _MetaInfoClass('Ipv6arm.Addresses.Vrfs.Vrf.Networks.Network.AddressXr.Address', REFERENCE_CLASS,
            '''IPv4/IPv6 address''',
            False, 
            [
            _MetaInfoClassMember('afi', ATTRIBUTE, 'int', 'int32',
                None, None,
                [('-2147483648', '2147483647')], [],
                '''                AFI
                ''',
                'afi',
                'Cisco-IOS-XR-ip-iarm-v6-oper', False, is_config=False),
            _MetaInfoClassMember('ipv4-address', ATTRIBUTE, 'str', 'inet:ipv4-address',
                None, None,
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'],
                '''                IPV4 Address
                ''',
                'ipv4_address',
                'Cisco-IOS-XR-ip-iarm-v6-oper', False, is_config=False, has_when=True),
            _MetaInfoClassMember('ipv6-address', ATTRIBUTE, 'str', 'Ipv6-address',
                None, None,
                [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'],
                '''                IPV6 Address
                ''',
                'ipv6_address',
                'Cisco-IOS-XR-ip-iarm-v6-oper', False, is_config=False, has_when=True),
            ],
            'Cisco-IOS-XR-ip-iarm-v6-oper',
            'address',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-ip-iarm-v6-oper'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_iarm_v6_oper',
            is_config=False,
        ),
    },
    'Ipv6arm.Addresses.Vrfs.Vrf.Networks.Network.AddressXr' : {
        'meta_info' : _MetaInfoClass('Ipv6arm.Addresses.Vrfs.Vrf.Networks.Network.AddressXr', REFERENCE_CLASS,
            '''Address info''',
            False, 
            [
            _MetaInfoClassMember('address', REFERENCE_CLASS, 'Address', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_iarm_v6_oper', 'Ipv6arm.Addresses.Vrfs.Vrf.Networks.Network.AddressXr.Address',
                [], [],
                '''                IPv4/IPv6 address
                ''',
                'address',
                'Cisco-IOS-XR-ip-iarm-v6-oper', False, is_config=False),
            _MetaInfoClassMember('prefix-length', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('0', '4294967295')], [],
                '''                Prefix length of theIPv4/IPv6 Address
                ''',
                'prefix_length',
                'Cisco-IOS-XR-ip-iarm-v6-oper', False, is_config=False),
            _MetaInfoClassMember('route-tag', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('0', '4294967295')], [],
                '''                Route Tag of the address
                ''',
                'route_tag',
                'Cisco-IOS-XR-ip-iarm-v6-oper', False, is_config=False),
            _MetaInfoClassMember('is-primary', ATTRIBUTE, 'bool', 'boolean',
                None, None,
                [], [],
                '''                Is address primary - valid only for IPv4
                addresses
                ''',
                'is_primary',
                'Cisco-IOS-XR-ip-iarm-v6-oper', False, is_config=False),
            _MetaInfoClassMember('is-tentative', ATTRIBUTE, 'bool', 'boolean',
                None, None,
                [], [],
                '''                Is address valid/tentative - valid only for IPV6
                addresses
                ''',
                'is_tentative',
                'Cisco-IOS-XR-ip-iarm-v6-oper', False, is_config=False),
            _MetaInfoClassMember('is-prefix-sid', ATTRIBUTE, 'bool', 'boolean',
                None, None,
                [], [],
                '''                Is prefix_sid valid - valid only for IPV6
                addresses
                ''',
                'is_prefix_sid',
                'Cisco-IOS-XR-ip-iarm-v6-oper', False, is_config=False),
            _MetaInfoClassMember('producer', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                Producer Name
                ''',
                'producer',
                'Cisco-IOS-XR-ip-iarm-v6-oper', False, is_config=False),
            ],
            'Cisco-IOS-XR-ip-iarm-v6-oper',
            'address-xr',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-ip-iarm-v6-oper'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_iarm_v6_oper',
            is_config=False,
        ),
    },
    'Ipv6arm.Addresses.Vrfs.Vrf.Networks.Network' : {
        'meta_info' : _MetaInfoClass('Ipv6arm.Addresses.Vrfs.Vrf.Networks.Network', REFERENCE_LIST,
            '''An IPv6 Address in IPv6 ARM''',
            False, 
            [
            _MetaInfoClassMember('address', ATTRIBUTE, 'str', 'inet:ipv6-address-no-zone',
                None, None,
                [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'],
                '''                Ipv6 Address in the Network
                ''',
                'address',
                'Cisco-IOS-XR-ip-iarm-v6-oper', False, is_config=False),
            _MetaInfoClassMember('prefix-length', ATTRIBUTE, 'int', 'Ipv6arm-prefix-length',
                None, None,
                [('0', '128')], [],
                '''                IPv6 Arm prefix length for this address in
                the Network
                ''',
                'prefix_length',
                'Cisco-IOS-XR-ip-iarm-v6-oper', False, is_config=False),
            _MetaInfoClassMember('interface', ATTRIBUTE, 'str', 'xr:Interface-name',
                None, None,
                [], [b'[a-zA-Z0-9._/-]+'],
                '''                Ingress/Egress interface handle for this
                address in the Network
                ''',
                'interface',
                'Cisco-IOS-XR-ip-iarm-v6-oper', False, is_config=False),
            _MetaInfoClassMember('address-xr', REFERENCE_CLASS, 'AddressXr', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_iarm_v6_oper', 'Ipv6arm.Addresses.Vrfs.Vrf.Networks.Network.AddressXr',
                [], [],
                '''                Address info
                ''',
                'address_xr',
                'Cisco-IOS-XR-ip-iarm-v6-oper', False, is_config=False),
            _MetaInfoClassMember('interface-name', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                Ingress/Egress Interface name for this address
                in the Network
                ''',
                'interface_name',
                'Cisco-IOS-XR-ip-iarm-v6-oper', False, is_config=False),
            _MetaInfoClassMember('referenced-interface', ATTRIBUTE, 'str', 'String1',
                None, None,
                [], [],
                '''                Referenced Interface - only valid for an
                unnumbered interface
                ''',
                'referenced_interface',
                'Cisco-IOS-XR-ip-iarm-v6-oper', False, is_config=False),
            _MetaInfoClassMember('vrf-name', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                VRF Name
                ''',
                'vrf_name',
                'Cisco-IOS-XR-ip-iarm-v6-oper', False, is_config=False),
            ],
            'Cisco-IOS-XR-ip-iarm-v6-oper',
            'network',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-ip-iarm-v6-oper'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_iarm_v6_oper',
            is_config=False,
        ),
    },
    'Ipv6arm.Addresses.Vrfs.Vrf.Networks' : {
        'meta_info' : _MetaInfoClass('Ipv6arm.Addresses.Vrfs.Vrf.Networks', REFERENCE_CLASS,
            '''IPv6 ARM address database information by
network''',
            False, 
            [
            _MetaInfoClassMember('network', REFERENCE_LIST, 'Network', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_iarm_v6_oper', 'Ipv6arm.Addresses.Vrfs.Vrf.Networks.Network',
                [], [],
                '''                An IPv6 Address in IPv6 ARM
                ''',
                'network',
                'Cisco-IOS-XR-ip-iarm-v6-oper', False, is_config=False),
            ],
            'Cisco-IOS-XR-ip-iarm-v6-oper',
            'networks',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-ip-iarm-v6-oper'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_iarm_v6_oper',
            is_config=False,
        ),
    },
    'Ipv6arm.Addresses.Vrfs.Vrf.Interfaces.Interface.Address.Address_' : {
        'meta_info' : _MetaInfoClass('Ipv6arm.Addresses.Vrfs.Vrf.Interfaces.Interface.Address.Address_', REFERENCE_CLASS,
            '''IPv4/IPv6 address''',
            False, 
            [
            _MetaInfoClassMember('afi', ATTRIBUTE, 'int', 'int32',
                None, None,
                [('-2147483648', '2147483647')], [],
                '''                AFI
                ''',
                'afi',
                'Cisco-IOS-XR-ip-iarm-v6-oper', False, is_config=False),
            _MetaInfoClassMember('ipv4-address', ATTRIBUTE, 'str', 'inet:ipv4-address',
                None, None,
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'],
                '''                IPV4 Address
                ''',
                'ipv4_address',
                'Cisco-IOS-XR-ip-iarm-v6-oper', False, is_config=False, has_when=True),
            _MetaInfoClassMember('ipv6-address', ATTRIBUTE, 'str', 'Ipv6-address',
                None, None,
                [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'],
                '''                IPV6 Address
                ''',
                'ipv6_address',
                'Cisco-IOS-XR-ip-iarm-v6-oper', False, is_config=False, has_when=True),
            ],
            'Cisco-IOS-XR-ip-iarm-v6-oper',
            'address',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-ip-iarm-v6-oper'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_iarm_v6_oper',
            is_config=False,
        ),
    },
    'Ipv6arm.Addresses.Vrfs.Vrf.Interfaces.Interface.Address' : {
        'meta_info' : _MetaInfoClass('Ipv6arm.Addresses.Vrfs.Vrf.Interfaces.Interface.Address', REFERENCE_LIST,
            '''Address info''',
            False, 
            [
            _MetaInfoClassMember('address', REFERENCE_CLASS, 'Address_', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_iarm_v6_oper', 'Ipv6arm.Addresses.Vrfs.Vrf.Interfaces.Interface.Address.Address_',
                [], [],
                '''                IPv4/IPv6 address
                ''',
                'address',
                'Cisco-IOS-XR-ip-iarm-v6-oper', False, is_config=False),
            _MetaInfoClassMember('prefix-length', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('0', '4294967295')], [],
                '''                Prefix length of theIPv4/IPv6 Address
                ''',
                'prefix_length',
                'Cisco-IOS-XR-ip-iarm-v6-oper', False, is_config=False),
            _MetaInfoClassMember('route-tag', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('0', '4294967295')], [],
                '''                Route Tag of the address
                ''',
                'route_tag',
                'Cisco-IOS-XR-ip-iarm-v6-oper', False, is_config=False),
            _MetaInfoClassMember('is-primary', ATTRIBUTE, 'bool', 'boolean',
                None, None,
                [], [],
                '''                Is address primary - valid only for IPv4
                addresses
                ''',
                'is_primary',
                'Cisco-IOS-XR-ip-iarm-v6-oper', False, is_config=False),
            _MetaInfoClassMember('is-tentative', ATTRIBUTE, 'bool', 'boolean',
                None, None,
                [], [],
                '''                Is address valid/tentative - valid only for IPV6
                addresses
                ''',
                'is_tentative',
                'Cisco-IOS-XR-ip-iarm-v6-oper', False, is_config=False),
            _MetaInfoClassMember('is-prefix-sid', ATTRIBUTE, 'bool', 'boolean',
                None, None,
                [], [],
                '''                Is prefix_sid valid - valid only for IPV6
                addresses
                ''',
                'is_prefix_sid',
                'Cisco-IOS-XR-ip-iarm-v6-oper', False, is_config=False),
            _MetaInfoClassMember('producer', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                Producer Name
                ''',
                'producer',
                'Cisco-IOS-XR-ip-iarm-v6-oper', False, is_config=False),
            ],
            'Cisco-IOS-XR-ip-iarm-v6-oper',
            'address',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-ip-iarm-v6-oper'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_iarm_v6_oper',
            is_config=False,
        ),
    },
    'Ipv6arm.Addresses.Vrfs.Vrf.Interfaces.Interface' : {
        'meta_info' : _MetaInfoClass('Ipv6arm.Addresses.Vrfs.Vrf.Interfaces.Interface', REFERENCE_LIST,
            '''An IPv6 address in IPv6 ARM''',
            False, 
            [
            _MetaInfoClassMember('interface', ATTRIBUTE, 'str', 'xr:Interface-name',
                None, None,
                [], [b'[a-zA-Z0-9._/-]+'],
                '''                Interface
                ''',
                'interface',
                'Cisco-IOS-XR-ip-iarm-v6-oper', True, is_config=False),
            _MetaInfoClassMember('referenced-interface', ATTRIBUTE, 'str', 'String1',
                None, None,
                [], [],
                '''                Referenced Interface - only valid for an
                unnumbered interface
                ''',
                'referenced_interface',
                'Cisco-IOS-XR-ip-iarm-v6-oper', False, is_config=False),
            _MetaInfoClassMember('vrf-name', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                VRF Name
                ''',
                'vrf_name',
                'Cisco-IOS-XR-ip-iarm-v6-oper', False, is_config=False),
            _MetaInfoClassMember('address', REFERENCE_LIST, 'Address', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_iarm_v6_oper', 'Ipv6arm.Addresses.Vrfs.Vrf.Interfaces.Interface.Address',
                [], [],
                '''                Address info
                ''',
                'address',
                'Cisco-IOS-XR-ip-iarm-v6-oper', False, is_config=False),
            ],
            'Cisco-IOS-XR-ip-iarm-v6-oper',
            'interface',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-ip-iarm-v6-oper'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_iarm_v6_oper',
            is_config=False,
        ),
    },
    'Ipv6arm.Addresses.Vrfs.Vrf.Interfaces' : {
        'meta_info' : _MetaInfoClass('Ipv6arm.Addresses.Vrfs.Vrf.Interfaces', REFERENCE_CLASS,
            '''IPv6 ARM address database information by
interface''',
            False, 
            [
            _MetaInfoClassMember('interface', REFERENCE_LIST, 'Interface', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_iarm_v6_oper', 'Ipv6arm.Addresses.Vrfs.Vrf.Interfaces.Interface',
                [], [],
                '''                An IPv6 address in IPv6 ARM
                ''',
                'interface',
                'Cisco-IOS-XR-ip-iarm-v6-oper', False, is_config=False),
            ],
            'Cisco-IOS-XR-ip-iarm-v6-oper',
            'interfaces',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-ip-iarm-v6-oper'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_iarm_v6_oper',
            is_config=False,
        ),
    },
    'Ipv6arm.Addresses.Vrfs.Vrf' : {
        'meta_info' : _MetaInfoClass('Ipv6arm.Addresses.Vrfs.Vrf', REFERENCE_LIST,
            '''IPv6 ARM address database information in a VRF''',
            False, 
            [
            _MetaInfoClassMember('vrf-name', ATTRIBUTE, 'str', 'xr:Cisco-ios-xr-string',
                None, None,
                [(1, 32)], [],
                '''                VRF name
                ''',
                'vrf_name',
                'Cisco-IOS-XR-ip-iarm-v6-oper', True, is_config=False),
            _MetaInfoClassMember('networks', REFERENCE_CLASS, 'Networks', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_iarm_v6_oper', 'Ipv6arm.Addresses.Vrfs.Vrf.Networks',
                [], [],
                '''                IPv6 ARM address database information by
                network
                ''',
                'networks',
                'Cisco-IOS-XR-ip-iarm-v6-oper', False, is_config=False),
            _MetaInfoClassMember('interfaces', REFERENCE_CLASS, 'Interfaces', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_iarm_v6_oper', 'Ipv6arm.Addresses.Vrfs.Vrf.Interfaces',
                [], [],
                '''                IPv6 ARM address database information by
                interface
                ''',
                'interfaces',
                'Cisco-IOS-XR-ip-iarm-v6-oper', False, is_config=False),
            ],
            'Cisco-IOS-XR-ip-iarm-v6-oper',
            'vrf',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-ip-iarm-v6-oper'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_iarm_v6_oper',
            is_config=False,
        ),
    },
    'Ipv6arm.Addresses.Vrfs' : {
        'meta_info' : _MetaInfoClass('Ipv6arm.Addresses.Vrfs', REFERENCE_CLASS,
            '''IPv6 ARM address database information per VRF''',
            False, 
            [
            _MetaInfoClassMember('vrf', REFERENCE_LIST, 'Vrf', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_iarm_v6_oper', 'Ipv6arm.Addresses.Vrfs.Vrf',
                [], [],
                '''                IPv6 ARM address database information in a VRF
                ''',
                'vrf',
                'Cisco-IOS-XR-ip-iarm-v6-oper', False, is_config=False),
            ],
            'Cisco-IOS-XR-ip-iarm-v6-oper',
            'vrfs',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-ip-iarm-v6-oper'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_iarm_v6_oper',
            is_config=False,
        ),
    },
    'Ipv6arm.Addresses' : {
        'meta_info' : _MetaInfoClass('Ipv6arm.Addresses', REFERENCE_CLASS,
            '''IPv6 ARM address database information''',
            False, 
            [
            _MetaInfoClassMember('vrfs', REFERENCE_CLASS, 'Vrfs', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_iarm_v6_oper', 'Ipv6arm.Addresses.Vrfs',
                [], [],
                '''                IPv6 ARM address database information per VRF
                ''',
                'vrfs',
                'Cisco-IOS-XR-ip-iarm-v6-oper', False, is_config=False),
            ],
            'Cisco-IOS-XR-ip-iarm-v6-oper',
            'addresses',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-ip-iarm-v6-oper'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_iarm_v6_oper',
            is_config=False,
        ),
    },
    'Ipv6arm.Summary' : {
        'meta_info' : _MetaInfoClass('Ipv6arm.Summary', REFERENCE_CLASS,
            '''IPv6 ARM summary information''',
            False, 
            [
            _MetaInfoClassMember('producer-count', ATTRIBUTE, 'int', 'int32',
                None, None,
                [('-2147483648', '2147483647')], [],
                '''                Number of producers
                ''',
                'producer_count',
                'Cisco-IOS-XR-ip-iarm-v6-oper', False, is_config=False),
            _MetaInfoClassMember('address-conflict-count', ATTRIBUTE, 'int', 'int32',
                None, None,
                [('-2147483648', '2147483647')], [],
                '''                Number of address conflicts
                ''',
                'address_conflict_count',
                'Cisco-IOS-XR-ip-iarm-v6-oper', False, is_config=False),
            _MetaInfoClassMember('unnumbered-conflict-count', ATTRIBUTE, 'int', 'int32',
                None, None,
                [('-2147483648', '2147483647')], [],
                '''                Number of unnumbered interface conflicts
                ''',
                'unnumbered_conflict_count',
                'Cisco-IOS-XR-ip-iarm-v6-oper', False, is_config=False),
            _MetaInfoClassMember('db-master-version', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('0', '4294967295')], [],
                '''                IP-ARM DB master version
                ''',
                'db_master_version',
                'Cisco-IOS-XR-ip-iarm-v6-oper', False, is_config=False),
            _MetaInfoClassMember('vrf-count', ATTRIBUTE, 'int', 'int32',
                None, None,
                [('-2147483648', '2147483647')], [],
                '''                Number of known VRFs
                ''',
                'vrf_count',
                'Cisco-IOS-XR-ip-iarm-v6-oper', False, is_config=False),
            ],
            'Cisco-IOS-XR-ip-iarm-v6-oper',
            'summary',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-ip-iarm-v6-oper'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_iarm_v6_oper',
            is_config=False,
        ),
    },
    'Ipv6arm.VrfSummaries.VrfSummary' : {
        'meta_info' : _MetaInfoClass('Ipv6arm.VrfSummaries.VrfSummary', REFERENCE_LIST,
            '''IPv6 ARM VRF summary information''',
            False, 
            [
            _MetaInfoClassMember('vrf-name', ATTRIBUTE, 'str', 'xr:Cisco-ios-xr-string',
                None, None,
                [(1, 32)], [],
                '''                VRF name
                ''',
                'vrf_name',
                'Cisco-IOS-XR-ip-iarm-v6-oper', True, is_config=False),
            _MetaInfoClassMember('vrf-id', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('0', '4294967295')], [],
                '''                VRF ID
                ''',
                'vrf_id',
                'Cisco-IOS-XR-ip-iarm-v6-oper', False, is_config=False),
            _MetaInfoClassMember('vrf-name-xr', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                VRF Name
                ''',
                'vrf_name_xr',
                'Cisco-IOS-XR-ip-iarm-v6-oper', False, is_config=False),
            ],
            'Cisco-IOS-XR-ip-iarm-v6-oper',
            'vrf-summary',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-ip-iarm-v6-oper'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_iarm_v6_oper',
            is_config=False,
        ),
    },
    'Ipv6arm.VrfSummaries' : {
        'meta_info' : _MetaInfoClass('Ipv6arm.VrfSummaries', REFERENCE_CLASS,
            '''IPv6 ARM VRFs summary information''',
            False, 
            [
            _MetaInfoClassMember('vrf-summary', REFERENCE_LIST, 'VrfSummary', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_iarm_v6_oper', 'Ipv6arm.VrfSummaries.VrfSummary',
                [], [],
                '''                IPv6 ARM VRF summary information
                ''',
                'vrf_summary',
                'Cisco-IOS-XR-ip-iarm-v6-oper', False, is_config=False),
            ],
            'Cisco-IOS-XR-ip-iarm-v6-oper',
            'vrf-summaries',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-ip-iarm-v6-oper'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_iarm_v6_oper',
            is_config=False,
        ),
    },
    'Ipv6arm' : {
        'meta_info' : _MetaInfoClass('Ipv6arm', REFERENCE_CLASS,
            '''IPv6 Address Repository Manager (IPv6 ARM)
operational data''',
            False, 
            [
            _MetaInfoClassMember('addresses', REFERENCE_CLASS, 'Addresses', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_iarm_v6_oper', 'Ipv6arm.Addresses',
                [], [],
                '''                IPv6 ARM address database information
                ''',
                'addresses',
                'Cisco-IOS-XR-ip-iarm-v6-oper', False, is_config=False),
            _MetaInfoClassMember('summary', REFERENCE_CLASS, 'Summary', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_iarm_v6_oper', 'Ipv6arm.Summary',
                [], [],
                '''                IPv6 ARM summary information
                ''',
                'summary',
                'Cisco-IOS-XR-ip-iarm-v6-oper', False, is_config=False),
            _MetaInfoClassMember('vrf-summaries', REFERENCE_CLASS, 'VrfSummaries', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_iarm_v6_oper', 'Ipv6arm.VrfSummaries',
                [], [],
                '''                IPv6 ARM VRFs summary information
                ''',
                'vrf_summaries',
                'Cisco-IOS-XR-ip-iarm-v6-oper', False, is_config=False),
            _MetaInfoClassMember('multicast-host-interface', ATTRIBUTE, 'str', 'xr:Interface-name',
                None, None,
                [], [b'[a-zA-Z0-9._/-]+'],
                '''                Interface Handle of Default Multicast Host
                ''',
                'multicast_host_interface',
                'Cisco-IOS-XR-ip-iarm-v6-oper', False, is_config=False),
            ],
            'Cisco-IOS-XR-ip-iarm-v6-oper',
            'ipv6arm',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-ip-iarm-v6-oper'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_iarm_v6_oper',
            is_config=False,
        ),
    },
}
_meta_table['Ipv6arm.Addresses.Vrfs.Vrf.Networks.Network.AddressXr.Address']['meta_info'].parent =_meta_table['Ipv6arm.Addresses.Vrfs.Vrf.Networks.Network.AddressXr']['meta_info']
_meta_table['Ipv6arm.Addresses.Vrfs.Vrf.Networks.Network.AddressXr']['meta_info'].parent =_meta_table['Ipv6arm.Addresses.Vrfs.Vrf.Networks.Network']['meta_info']
_meta_table['Ipv6arm.Addresses.Vrfs.Vrf.Networks.Network']['meta_info'].parent =_meta_table['Ipv6arm.Addresses.Vrfs.Vrf.Networks']['meta_info']
_meta_table['Ipv6arm.Addresses.Vrfs.Vrf.Interfaces.Interface.Address.Address_']['meta_info'].parent =_meta_table['Ipv6arm.Addresses.Vrfs.Vrf.Interfaces.Interface.Address']['meta_info']
_meta_table['Ipv6arm.Addresses.Vrfs.Vrf.Interfaces.Interface.Address']['meta_info'].parent =_meta_table['Ipv6arm.Addresses.Vrfs.Vrf.Interfaces.Interface']['meta_info']
_meta_table['Ipv6arm.Addresses.Vrfs.Vrf.Interfaces.Interface']['meta_info'].parent =_meta_table['Ipv6arm.Addresses.Vrfs.Vrf.Interfaces']['meta_info']
_meta_table['Ipv6arm.Addresses.Vrfs.Vrf.Networks']['meta_info'].parent =_meta_table['Ipv6arm.Addresses.Vrfs.Vrf']['meta_info']
_meta_table['Ipv6arm.Addresses.Vrfs.Vrf.Interfaces']['meta_info'].parent =_meta_table['Ipv6arm.Addresses.Vrfs.Vrf']['meta_info']
_meta_table['Ipv6arm.Addresses.Vrfs.Vrf']['meta_info'].parent =_meta_table['Ipv6arm.Addresses.Vrfs']['meta_info']
_meta_table['Ipv6arm.Addresses.Vrfs']['meta_info'].parent =_meta_table['Ipv6arm.Addresses']['meta_info']
_meta_table['Ipv6arm.VrfSummaries.VrfSummary']['meta_info'].parent =_meta_table['Ipv6arm.VrfSummaries']['meta_info']
_meta_table['Ipv6arm.Addresses']['meta_info'].parent =_meta_table['Ipv6arm']['meta_info']
_meta_table['Ipv6arm.Summary']['meta_info'].parent =_meta_table['Ipv6arm']['meta_info']
_meta_table['Ipv6arm.VrfSummaries']['meta_info'].parent =_meta_table['Ipv6arm']['meta_info']
