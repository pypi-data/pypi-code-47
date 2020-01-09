
'''
This is auto-generated file,
which includes metadata for module Cisco_IOS_XR_ip_domain_oper
'''

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_LIST, REFERENCE_LEAFLIST, REFERENCE_BITS, REFERENCE_UNION
from ydk._core._dm_meta_info import REFERENCE_CLASS, REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, ANYXML_CLASS
from ydk._core._importer import _yang_ns

_meta_table = {
    'ServerDomainLkup' : _MetaInfoEnum('ServerDomainLkup',
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_domain_oper', 'ServerDomainLkup',
        '''Domain look up''',
        {
            'static-mapping':'static_mapping',
            'domain-service':'domain_service',
        }, 'Cisco-IOS-XR-ip-domain-oper', _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-ip-domain-oper']),
    'HostAddressBase' : {
        'meta_info' : _MetaInfoClass('HostAddressBase', REFERENCE_IDENTITY_CLASS,
            '''Base identity for Host-address''',
            False, 
            [
            ],
            'Cisco-IOS-XR-ip-domain-oper',
            'Host-address-base',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-ip-domain-oper'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_domain_oper',
        ),
    },
    'IpDomain.Vrfs.Vrf.Server.ServerAddress' : {
        'meta_info' : _MetaInfoClass('IpDomain.Vrfs.Vrf.Server.ServerAddress', REFERENCE_LIST,
            '''Server address list''',
            False, 
            [
            _MetaInfoClassMember('af-name', REFERENCE_IDENTITY_CLASS, 'HostAddressBase', 'Host-address',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_domain_oper', 'HostAddressBase',
                [], [],
                '''                AFName
                ''',
                'af_name',
                'Cisco-IOS-XR-ip-domain-oper', False, is_config=False),
            _MetaInfoClassMember('ipv4-address', ATTRIBUTE, 'str', 'inet:ipv4-address',
                None, None,
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'],
                '''                IPv4 address
                ''',
                'ipv4_address',
                'Cisco-IOS-XR-ip-domain-oper', False, is_config=False, has_when=True),
            _MetaInfoClassMember('ipv6-address', ATTRIBUTE, 'str', 'Domain-ipv6-address',
                None, None,
                [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'],
                '''                IPv6 address
                ''',
                'ipv6_address',
                'Cisco-IOS-XR-ip-domain-oper', False, is_config=False, has_when=True),
            ],
            'Cisco-IOS-XR-ip-domain-oper',
            'server-address',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-ip-domain-oper'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_domain_oper',
            is_config=False,
        ),
    },
    'IpDomain.Vrfs.Vrf.Server' : {
        'meta_info' : _MetaInfoClass('IpDomain.Vrfs.Vrf.Server', REFERENCE_CLASS,
            '''Domain server data''',
            False, 
            [
            _MetaInfoClassMember('domain-lookup', REFERENCE_ENUM_CLASS, 'ServerDomainLkup', 'Server-domain-lkup',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_domain_oper', 'ServerDomainLkup',
                [], [],
                '''                Domain lookup
                ''',
                'domain_lookup',
                'Cisco-IOS-XR-ip-domain-oper', False, is_config=False),
            _MetaInfoClassMember('domain-name', ATTRIBUTE, 'str', 'string',
                None, None,
                [(0, 256)], [],
                '''                Domain name
                ''',
                'domain_name',
                'Cisco-IOS-XR-ip-domain-oper', False, is_config=False),
            _MetaInfoClassMember('domain', REFERENCE_LEAFLIST, 'str', 'String1',
                None, None,
                [(0, 256)], [],
                '''                Domain list
                ''',
                'domain',
                'Cisco-IOS-XR-ip-domain-oper', False, is_config=False),
            _MetaInfoClassMember('server-address', REFERENCE_LIST, 'ServerAddress', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_domain_oper', 'IpDomain.Vrfs.Vrf.Server.ServerAddress',
                [], [],
                '''                Server address list
                ''',
                'server_address',
                'Cisco-IOS-XR-ip-domain-oper', False, is_config=False),
            ],
            'Cisco-IOS-XR-ip-domain-oper',
            'server',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-ip-domain-oper'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_domain_oper',
            is_config=False,
        ),
    },
    'IpDomain.Vrfs.Vrf.Hosts.Host.HostAliasList' : {
        'meta_info' : _MetaInfoClass('IpDomain.Vrfs.Vrf.Hosts.Host.HostAliasList', REFERENCE_CLASS,
            '''Host alias''',
            False, 
            [
            _MetaInfoClassMember('host-alias', REFERENCE_LEAFLIST, 'str', 'String1',
                None, None,
                [(0, 256)], [],
                '''                Host alias list
                ''',
                'host_alias',
                'Cisco-IOS-XR-ip-domain-oper', False, is_config=False),
            ],
            'Cisco-IOS-XR-ip-domain-oper',
            'host-alias-list',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-ip-domain-oper'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_domain_oper',
            is_config=False,
        ),
    },
    'IpDomain.Vrfs.Vrf.Hosts.Host.HostAddress' : {
        'meta_info' : _MetaInfoClass('IpDomain.Vrfs.Vrf.Hosts.Host.HostAddress', REFERENCE_LIST,
            '''Host address list''',
            False, 
            [
            _MetaInfoClassMember('af-name', REFERENCE_IDENTITY_CLASS, 'HostAddressBase', 'Host-address',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_domain_oper', 'HostAddressBase',
                [], [],
                '''                AFName
                ''',
                'af_name',
                'Cisco-IOS-XR-ip-domain-oper', False, is_config=False),
            _MetaInfoClassMember('ipv4-address', ATTRIBUTE, 'str', 'inet:ipv4-address',
                None, None,
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'],
                '''                IPv4 address
                ''',
                'ipv4_address',
                'Cisco-IOS-XR-ip-domain-oper', False, is_config=False, has_when=True),
            _MetaInfoClassMember('ipv6-address', ATTRIBUTE, 'str', 'Domain-ipv6-address',
                None, None,
                [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'],
                '''                IPv6 address
                ''',
                'ipv6_address',
                'Cisco-IOS-XR-ip-domain-oper', False, is_config=False, has_when=True),
            ],
            'Cisco-IOS-XR-ip-domain-oper',
            'host-address',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-ip-domain-oper'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_domain_oper',
            is_config=False,
        ),
    },
    'IpDomain.Vrfs.Vrf.Hosts.Host' : {
        'meta_info' : _MetaInfoClass('IpDomain.Vrfs.Vrf.Hosts.Host', REFERENCE_LIST,
            '''IP domain-name, lookup style, nameservers for
specific host''',
            False, 
            [
            _MetaInfoClassMember('host-name', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                Hostname
                ''',
                'host_name',
                'Cisco-IOS-XR-ip-domain-oper', True, is_config=False),
            _MetaInfoClassMember('host-alias-list', REFERENCE_CLASS, 'HostAliasList', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_domain_oper', 'IpDomain.Vrfs.Vrf.Hosts.Host.HostAliasList',
                [], [],
                '''                Host alias
                ''',
                'host_alias_list',
                'Cisco-IOS-XR-ip-domain-oper', False, is_config=False),
            _MetaInfoClassMember('af-name', REFERENCE_IDENTITY_CLASS, 'HostAddressBase', 'Host-address',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_domain_oper', 'HostAddressBase',
                [], [],
                '''                Address type
                ''',
                'af_name',
                'Cisco-IOS-XR-ip-domain-oper', False, is_config=False),
            _MetaInfoClassMember('age', ATTRIBUTE, 'int', 'uint16',
                None, None,
                [('0', '65535')], [],
                '''                Age in hours
                ''',
                'age',
                'Cisco-IOS-XR-ip-domain-oper', False, is_config=False),
            _MetaInfoClassMember('host-address', REFERENCE_LIST, 'HostAddress', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_domain_oper', 'IpDomain.Vrfs.Vrf.Hosts.Host.HostAddress',
                [], [],
                '''                Host address list
                ''',
                'host_address',
                'Cisco-IOS-XR-ip-domain-oper', False, is_config=False),
            ],
            'Cisco-IOS-XR-ip-domain-oper',
            'host',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-ip-domain-oper'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_domain_oper',
            is_config=False,
        ),
    },
    'IpDomain.Vrfs.Vrf.Hosts' : {
        'meta_info' : _MetaInfoClass('IpDomain.Vrfs.Vrf.Hosts', REFERENCE_CLASS,
            '''List of domain hosts''',
            False, 
            [
            _MetaInfoClassMember('host', REFERENCE_LIST, 'Host', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_domain_oper', 'IpDomain.Vrfs.Vrf.Hosts.Host',
                [], [],
                '''                IP domain-name, lookup style, nameservers for
                specific host
                ''',
                'host',
                'Cisco-IOS-XR-ip-domain-oper', False, is_config=False),
            ],
            'Cisco-IOS-XR-ip-domain-oper',
            'hosts',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-ip-domain-oper'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_domain_oper',
            is_config=False,
        ),
    },
    'IpDomain.Vrfs.Vrf' : {
        'meta_info' : _MetaInfoClass('IpDomain.Vrfs.Vrf', REFERENCE_LIST,
            '''VRF instance''',
            False, 
            [
            _MetaInfoClassMember('vrf-name', ATTRIBUTE, 'str', 'xr:Cisco-ios-xr-string',
                None, None,
                [], [b'[\\w\\-\\.:,_@#%$\\+=\\|;]+'],
                '''                VRF name
                ''',
                'vrf_name',
                'Cisco-IOS-XR-ip-domain-oper', True, is_config=False),
            _MetaInfoClassMember('server', REFERENCE_CLASS, 'Server', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_domain_oper', 'IpDomain.Vrfs.Vrf.Server',
                [], [],
                '''                Domain server data
                ''',
                'server',
                'Cisco-IOS-XR-ip-domain-oper', False, is_config=False),
            _MetaInfoClassMember('hosts', REFERENCE_CLASS, 'Hosts', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_domain_oper', 'IpDomain.Vrfs.Vrf.Hosts',
                [], [],
                '''                List of domain hosts
                ''',
                'hosts',
                'Cisco-IOS-XR-ip-domain-oper', False, is_config=False),
            ],
            'Cisco-IOS-XR-ip-domain-oper',
            'vrf',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-ip-domain-oper'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_domain_oper',
            is_config=False,
        ),
    },
    'IpDomain.Vrfs' : {
        'meta_info' : _MetaInfoClass('IpDomain.Vrfs', REFERENCE_CLASS,
            '''List of VRFs''',
            False, 
            [
            _MetaInfoClassMember('vrf', REFERENCE_LIST, 'Vrf', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_domain_oper', 'IpDomain.Vrfs.Vrf',
                [], [],
                '''                VRF instance
                ''',
                'vrf',
                'Cisco-IOS-XR-ip-domain-oper', False, is_config=False),
            ],
            'Cisco-IOS-XR-ip-domain-oper',
            'vrfs',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-ip-domain-oper'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_domain_oper',
            is_config=False,
        ),
    },
    'IpDomain' : {
        'meta_info' : _MetaInfoClass('IpDomain', REFERENCE_CLASS,
            '''Domain server and host data''',
            False, 
            [
            _MetaInfoClassMember('vrfs', REFERENCE_CLASS, 'Vrfs', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_domain_oper', 'IpDomain.Vrfs',
                [], [],
                '''                List of VRFs
                ''',
                'vrfs',
                'Cisco-IOS-XR-ip-domain-oper', False, is_config=False),
            ],
            'Cisco-IOS-XR-ip-domain-oper',
            'ip-domain',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-ip-domain-oper'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_domain_oper',
            is_config=False,
        ),
    },
    'Ipv4' : {
        'meta_info' : _MetaInfoClass('Ipv4', REFERENCE_IDENTITY_CLASS,
            '''IPv4 family address''',
            False, 
            [
            ],
            'Cisco-IOS-XR-ip-domain-oper',
            'ipv4',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-ip-domain-oper'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_domain_oper',
        ),
    },
    'Ipv6' : {
        'meta_info' : _MetaInfoClass('Ipv6', REFERENCE_IDENTITY_CLASS,
            '''IPv6 family address''',
            False, 
            [
            ],
            'Cisco-IOS-XR-ip-domain-oper',
            'ipv6',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-ip-domain-oper'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_domain_oper',
        ),
    },
}
_meta_table['IpDomain.Vrfs.Vrf.Server.ServerAddress']['meta_info'].parent =_meta_table['IpDomain.Vrfs.Vrf.Server']['meta_info']
_meta_table['IpDomain.Vrfs.Vrf.Hosts.Host.HostAliasList']['meta_info'].parent =_meta_table['IpDomain.Vrfs.Vrf.Hosts.Host']['meta_info']
_meta_table['IpDomain.Vrfs.Vrf.Hosts.Host.HostAddress']['meta_info'].parent =_meta_table['IpDomain.Vrfs.Vrf.Hosts.Host']['meta_info']
_meta_table['IpDomain.Vrfs.Vrf.Hosts.Host']['meta_info'].parent =_meta_table['IpDomain.Vrfs.Vrf.Hosts']['meta_info']
_meta_table['IpDomain.Vrfs.Vrf.Server']['meta_info'].parent =_meta_table['IpDomain.Vrfs.Vrf']['meta_info']
_meta_table['IpDomain.Vrfs.Vrf.Hosts']['meta_info'].parent =_meta_table['IpDomain.Vrfs.Vrf']['meta_info']
_meta_table['IpDomain.Vrfs.Vrf']['meta_info'].parent =_meta_table['IpDomain.Vrfs']['meta_info']
_meta_table['IpDomain.Vrfs']['meta_info'].parent =_meta_table['IpDomain']['meta_info']
