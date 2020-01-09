
'''
This is auto-generated file,
which includes metadata for module Cisco_IOS_XR_ip_domain_cfg
'''

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_LIST, REFERENCE_LEAFLIST, REFERENCE_BITS, REFERENCE_UNION
from ydk._core._dm_meta_info import REFERENCE_CLASS, REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, ANYXML_CLASS
from ydk._core._importer import _yang_ns

_meta_table = {
    'IpDomain.Vrfs.Vrf.Ipv6Hosts.Ipv6Host' : {
        'meta_info' : _MetaInfoClass('IpDomain.Vrfs.Vrf.Ipv6Hosts.Ipv6Host', REFERENCE_LIST,
            '''Host name and up to 4 host IPv6 addresses''',
            False, 
            [
            _MetaInfoClassMember('host-name', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                A hostname
                ''',
                'host_name',
                'Cisco-IOS-XR-ip-domain-cfg', True),
            _MetaInfoClassMember('address', REFERENCE_LEAFLIST, 'str', 'inet:ipv6-address-no-zone',
                None, None,
                [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'],
                '''                Host IPv6 addresses
                ''',
                'address',
                'Cisco-IOS-XR-ip-domain-cfg', False, max_elements=4, min_elements=1),
            ],
            'Cisco-IOS-XR-ip-domain-cfg',
            'ipv6-host',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-ip-domain-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_domain_cfg',
        ),
    },
    'IpDomain.Vrfs.Vrf.Ipv6Hosts' : {
        'meta_info' : _MetaInfoClass('IpDomain.Vrfs.Vrf.Ipv6Hosts', REFERENCE_CLASS,
            '''IPv6 host''',
            False, 
            [
            _MetaInfoClassMember('ipv6-host', REFERENCE_LIST, 'Ipv6Host', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_domain_cfg', 'IpDomain.Vrfs.Vrf.Ipv6Hosts.Ipv6Host',
                [], [],
                '''                Host name and up to 4 host IPv6 addresses
                ''',
                'ipv6_host',
                'Cisco-IOS-XR-ip-domain-cfg', False),
            ],
            'Cisco-IOS-XR-ip-domain-cfg',
            'ipv6-hosts',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-ip-domain-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_domain_cfg',
        ),
    },
    'IpDomain.Vrfs.Vrf.Servers.Server' : {
        'meta_info' : _MetaInfoClass('IpDomain.Vrfs.Vrf.Servers.Server', REFERENCE_LIST,
            '''Name server address''',
            False, 
            [
            _MetaInfoClassMember('order', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('0', '4294967295')], [],
                '''                This is used to sort the servers in the
                order of precedence
                ''',
                'order',
                'Cisco-IOS-XR-ip-domain-cfg', True),
            _MetaInfoClassMember('server-address', REFERENCE_UNION, 'str', 'inet:ip-address-no-zone',
                None, None,
                [], [],
                '''                A name server address
                ''',
                'server_address',
                'Cisco-IOS-XR-ip-domain-cfg', True, [
                    _MetaInfoClassMember('server-address', ATTRIBUTE, 'str', 'inet:ipv4-address-no-zone',
                        None, None,
                        [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'],
                        '''                        A name server address
                        ''',
                        'server_address',
                        'Cisco-IOS-XR-ip-domain-cfg', True),
                    _MetaInfoClassMember('server-address', ATTRIBUTE, 'str', 'inet:ipv6-address-no-zone',
                        None, None,
                        [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'],
                        '''                        A name server address
                        ''',
                        'server_address',
                        'Cisco-IOS-XR-ip-domain-cfg', True),
                ]),
            ],
            'Cisco-IOS-XR-ip-domain-cfg',
            'server',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-ip-domain-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_domain_cfg',
        ),
    },
    'IpDomain.Vrfs.Vrf.Servers' : {
        'meta_info' : _MetaInfoClass('IpDomain.Vrfs.Vrf.Servers', REFERENCE_CLASS,
            '''Name server addresses''',
            False, 
            [
            _MetaInfoClassMember('server', REFERENCE_LIST, 'Server', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_domain_cfg', 'IpDomain.Vrfs.Vrf.Servers.Server',
                [], [],
                '''                Name server address
                ''',
                'server',
                'Cisco-IOS-XR-ip-domain-cfg', False),
            ],
            'Cisco-IOS-XR-ip-domain-cfg',
            'servers',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-ip-domain-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_domain_cfg',
        ),
    },
    'IpDomain.Vrfs.Vrf.Lists.List' : {
        'meta_info' : _MetaInfoClass('IpDomain.Vrfs.Vrf.Lists.List', REFERENCE_LIST,
            '''Domain name to complete unqualified host
names''',
            False, 
            [
            _MetaInfoClassMember('order', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('0', '4294967295')], [],
                '''                This is used to sort the names in the order
                of precedence
                ''',
                'order',
                'Cisco-IOS-XR-ip-domain-cfg', True),
            _MetaInfoClassMember('list-name', ATTRIBUTE, 'str', 'xr:Cisco-ios-xr-string',
                None, None,
                [], [b'[\\w\\-\\.:,_@#%$\\+=\\|;]+'],
                '''                A domain name
                ''',
                'list_name',
                'Cisco-IOS-XR-ip-domain-cfg', True),
            ],
            'Cisco-IOS-XR-ip-domain-cfg',
            'list',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-ip-domain-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_domain_cfg',
        ),
    },
    'IpDomain.Vrfs.Vrf.Lists' : {
        'meta_info' : _MetaInfoClass('IpDomain.Vrfs.Vrf.Lists', REFERENCE_CLASS,
            '''Domain names to complete unqualified host
names''',
            False, 
            [
            _MetaInfoClassMember('list', REFERENCE_LIST, 'List', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_domain_cfg', 'IpDomain.Vrfs.Vrf.Lists.List',
                [], [],
                '''                Domain name to complete unqualified host
                names
                ''',
                'list',
                'Cisco-IOS-XR-ip-domain-cfg', False),
            ],
            'Cisco-IOS-XR-ip-domain-cfg',
            'lists',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-ip-domain-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_domain_cfg',
        ),
    },
    'IpDomain.Vrfs.Vrf.Ipv4Hosts.Ipv4Host' : {
        'meta_info' : _MetaInfoClass('IpDomain.Vrfs.Vrf.Ipv4Hosts.Ipv4Host', REFERENCE_LIST,
            '''Host name and up to 8 host IPv4 addresses''',
            False, 
            [
            _MetaInfoClassMember('host-name', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                A hostname
                ''',
                'host_name',
                'Cisco-IOS-XR-ip-domain-cfg', True),
            _MetaInfoClassMember('address', REFERENCE_LEAFLIST, 'str', 'inet:ipv4-address-no-zone',
                None, None,
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'],
                '''                Host IPv4 addresses
                ''',
                'address',
                'Cisco-IOS-XR-ip-domain-cfg', False, max_elements=8, min_elements=1),
            ],
            'Cisco-IOS-XR-ip-domain-cfg',
            'ipv4-host',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-ip-domain-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_domain_cfg',
        ),
    },
    'IpDomain.Vrfs.Vrf.Ipv4Hosts' : {
        'meta_info' : _MetaInfoClass('IpDomain.Vrfs.Vrf.Ipv4Hosts', REFERENCE_CLASS,
            '''IPv4 host''',
            False, 
            [
            _MetaInfoClassMember('ipv4-host', REFERENCE_LIST, 'Ipv4Host', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_domain_cfg', 'IpDomain.Vrfs.Vrf.Ipv4Hosts.Ipv4Host',
                [], [],
                '''                Host name and up to 8 host IPv4 addresses
                ''',
                'ipv4_host',
                'Cisco-IOS-XR-ip-domain-cfg', False),
            ],
            'Cisco-IOS-XR-ip-domain-cfg',
            'ipv4-hosts',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-ip-domain-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_domain_cfg',
        ),
    },
    'IpDomain.Vrfs.Vrf' : {
        'meta_info' : _MetaInfoClass('IpDomain.Vrfs.Vrf', REFERENCE_LIST,
            '''VRF specific data''',
            False, 
            [
            _MetaInfoClassMember('vrf-name', ATTRIBUTE, 'str', 'xr:Cisco-ios-xr-string',
                None, None,
                [], [b'[\\w\\-\\.:,_@#%$\\+=\\|;]+'],
                '''                Name of the VRF instance
                ''',
                'vrf_name',
                'Cisco-IOS-XR-ip-domain-cfg', True),
            _MetaInfoClassMember('ipv6-hosts', REFERENCE_CLASS, 'Ipv6Hosts', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_domain_cfg', 'IpDomain.Vrfs.Vrf.Ipv6Hosts',
                [], [],
                '''                IPv6 host
                ''',
                'ipv6_hosts',
                'Cisco-IOS-XR-ip-domain-cfg', False),
            _MetaInfoClassMember('servers', REFERENCE_CLASS, 'Servers', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_domain_cfg', 'IpDomain.Vrfs.Vrf.Servers',
                [], [],
                '''                Name server addresses
                ''',
                'servers',
                'Cisco-IOS-XR-ip-domain-cfg', False),
            _MetaInfoClassMember('lists', REFERENCE_CLASS, 'Lists', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_domain_cfg', 'IpDomain.Vrfs.Vrf.Lists',
                [], [],
                '''                Domain names to complete unqualified host
                names
                ''',
                'lists',
                'Cisco-IOS-XR-ip-domain-cfg', False),
            _MetaInfoClassMember('ipv4-hosts', REFERENCE_CLASS, 'Ipv4Hosts', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_domain_cfg', 'IpDomain.Vrfs.Vrf.Ipv4Hosts',
                [], [],
                '''                IPv4 host
                ''',
                'ipv4_hosts',
                'Cisco-IOS-XR-ip-domain-cfg', False),
            _MetaInfoClassMember('lookup', ATTRIBUTE, 'Empty', 'empty',
                None, None,
                [], [],
                '''                Disable Domain Name System hostname
                translation
                ''',
                'lookup',
                'Cisco-IOS-XR-ip-domain-cfg', False),
            _MetaInfoClassMember('multicast-domain', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                Default multicast domain name
                ''',
                'multicast_domain',
                'Cisco-IOS-XR-ip-domain-cfg', False),
            _MetaInfoClassMember('source-interface', ATTRIBUTE, 'str', 'xr:Interface-name',
                None, None,
                [], [b'[a-zA-Z0-9._/-]+'],
                '''                Specify interface for source address in
                connections
                ''',
                'source_interface',
                'Cisco-IOS-XR-ip-domain-cfg', False),
            _MetaInfoClassMember('name', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                Default domain name
                ''',
                'name',
                'Cisco-IOS-XR-ip-domain-cfg', False),
            ],
            'Cisco-IOS-XR-ip-domain-cfg',
            'vrf',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-ip-domain-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_domain_cfg',
        ),
    },
    'IpDomain.Vrfs' : {
        'meta_info' : _MetaInfoClass('IpDomain.Vrfs', REFERENCE_CLASS,
            '''VRF table''',
            False, 
            [
            _MetaInfoClassMember('vrf', REFERENCE_LIST, 'Vrf', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_domain_cfg', 'IpDomain.Vrfs.Vrf',
                [], [],
                '''                VRF specific data
                ''',
                'vrf',
                'Cisco-IOS-XR-ip-domain-cfg', False),
            ],
            'Cisco-IOS-XR-ip-domain-cfg',
            'vrfs',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-ip-domain-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_domain_cfg',
        ),
    },
    'IpDomain' : {
        'meta_info' : _MetaInfoClass('IpDomain', REFERENCE_CLASS,
            '''IP domain configuration''',
            False, 
            [
            _MetaInfoClassMember('vrfs', REFERENCE_CLASS, 'Vrfs', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_domain_cfg', 'IpDomain.Vrfs',
                [], [],
                '''                VRF table
                ''',
                'vrfs',
                'Cisco-IOS-XR-ip-domain-cfg', False),
            _MetaInfoClassMember('default-flows-disable', ATTRIBUTE, 'Empty', 'empty',
                None, None,
                [], [],
                '''                Disable default flows programming
                ''',
                'default_flows_disable',
                'Cisco-IOS-XR-ip-domain-cfg', False),
            ],
            'Cisco-IOS-XR-ip-domain-cfg',
            'ip-domain',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-ip-domain-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_domain_cfg',
        ),
    },
}
_meta_table['IpDomain.Vrfs.Vrf.Ipv6Hosts.Ipv6Host']['meta_info'].parent =_meta_table['IpDomain.Vrfs.Vrf.Ipv6Hosts']['meta_info']
_meta_table['IpDomain.Vrfs.Vrf.Servers.Server']['meta_info'].parent =_meta_table['IpDomain.Vrfs.Vrf.Servers']['meta_info']
_meta_table['IpDomain.Vrfs.Vrf.Lists.List']['meta_info'].parent =_meta_table['IpDomain.Vrfs.Vrf.Lists']['meta_info']
_meta_table['IpDomain.Vrfs.Vrf.Ipv4Hosts.Ipv4Host']['meta_info'].parent =_meta_table['IpDomain.Vrfs.Vrf.Ipv4Hosts']['meta_info']
_meta_table['IpDomain.Vrfs.Vrf.Ipv6Hosts']['meta_info'].parent =_meta_table['IpDomain.Vrfs.Vrf']['meta_info']
_meta_table['IpDomain.Vrfs.Vrf.Servers']['meta_info'].parent =_meta_table['IpDomain.Vrfs.Vrf']['meta_info']
_meta_table['IpDomain.Vrfs.Vrf.Lists']['meta_info'].parent =_meta_table['IpDomain.Vrfs.Vrf']['meta_info']
_meta_table['IpDomain.Vrfs.Vrf.Ipv4Hosts']['meta_info'].parent =_meta_table['IpDomain.Vrfs.Vrf']['meta_info']
_meta_table['IpDomain.Vrfs.Vrf']['meta_info'].parent =_meta_table['IpDomain.Vrfs']['meta_info']
_meta_table['IpDomain.Vrfs']['meta_info'].parent =_meta_table['IpDomain']['meta_info']
