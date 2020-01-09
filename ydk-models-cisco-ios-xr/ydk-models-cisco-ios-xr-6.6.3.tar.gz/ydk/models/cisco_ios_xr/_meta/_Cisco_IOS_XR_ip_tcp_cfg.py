
'''
This is auto-generated file,
which includes metadata for module Cisco_IOS_XR_ip_tcp_cfg
'''

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_LIST, REFERENCE_LEAFLIST, REFERENCE_BITS, REFERENCE_UNION
from ydk._core._dm_meta_info import REFERENCE_CLASS, REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, ANYXML_CLASS
from ydk._core._importer import _yang_ns

_meta_table = {
    'IpTcp.Directory' : {
        'meta_info' : _MetaInfoClass('IpTcp.Directory', REFERENCE_CLASS,
            '''TCP directory details''',
            False, 
            [
            _MetaInfoClassMember('directoryname', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                Directory name 
                ''',
                'directoryname',
                'Cisco-IOS-XR-ip-tcp-cfg', False, is_mandatory=True),
            _MetaInfoClassMember('max-debug-files', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('1', '10000')], [],
                '''                Set number of Debug files
                ''',
                'max_debug_files',
                'Cisco-IOS-XR-ip-tcp-cfg', False, default_value="256"),
            _MetaInfoClassMember('max-file-size-files', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('1024', '4294967295')], [],
                '''                Set size of debug files in bytes
                ''',
                'max_file_size_files',
                'Cisco-IOS-XR-ip-tcp-cfg', False),
            ],
            'Cisco-IOS-XR-ip-tcp-cfg',
            'directory',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-ip-tcp-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_tcp_cfg',
            is_presence=True,
        ),
    },
    'IpTcp.Throttle' : {
        'meta_info' : _MetaInfoClass('IpTcp.Throttle', REFERENCE_CLASS,
            '''Throttle TCP receive buffer (in percentage)''',
            False, 
            [
            _MetaInfoClassMember('tcpmin-throttle', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('0', '100')], [],
                '''                Min throttle
                ''',
                'tcpmin_throttle',
                'Cisco-IOS-XR-ip-tcp-cfg', False, is_mandatory=True),
            _MetaInfoClassMember('tcpmaxthrottle', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('0', '100')], [],
                '''                Max throttle
                ''',
                'tcpmaxthrottle',
                'Cisco-IOS-XR-ip-tcp-cfg', False, is_mandatory=True),
            ],
            'Cisco-IOS-XR-ip-tcp-cfg',
            'throttle',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-ip-tcp-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_tcp_cfg',
            is_presence=True,
        ),
    },
    'IpTcp.Ao.Keychains.Keychain.Keys.Key' : {
        'meta_info' : _MetaInfoClass('IpTcp.Ao.Keychains.Keychain.Keys.Key', REFERENCE_LIST,
            '''Key identifier''',
            False, 
            [
            _MetaInfoClassMember('key-id', ATTRIBUTE, 'str', 'xr:Cisco-ios-xr-string',
                None, None,
                [], [b'[\\w\\-\\.:,_@#%$\\+=\\|;]+'],
                '''                48-bit Key identifier in range [0 -
                281474976710655]
                ''',
                'key_id',
                'Cisco-IOS-XR-ip-tcp-cfg', True),
            _MetaInfoClassMember('send-id', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('0', '255')], [],
                '''                Send ID
                ''',
                'send_id',
                'Cisco-IOS-XR-ip-tcp-cfg', False, is_mandatory=True),
            _MetaInfoClassMember('receive-id', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('0', '255')], [],
                '''                Receive ID
                ''',
                'receive_id',
                'Cisco-IOS-XR-ip-tcp-cfg', False, is_mandatory=True),
            ],
            'Cisco-IOS-XR-ip-tcp-cfg',
            'key',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-ip-tcp-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_tcp_cfg',
        ),
    },
    'IpTcp.Ao.Keychains.Keychain.Keys' : {
        'meta_info' : _MetaInfoClass('IpTcp.Ao.Keychains.Keychain.Keys', REFERENCE_CLASS,
            '''Configure a Key''',
            False, 
            [
            _MetaInfoClassMember('key', REFERENCE_LIST, 'Key', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_tcp_cfg', 'IpTcp.Ao.Keychains.Keychain.Keys.Key',
                [], [],
                '''                Key identifier
                ''',
                'key',
                'Cisco-IOS-XR-ip-tcp-cfg', False),
            ],
            'Cisco-IOS-XR-ip-tcp-cfg',
            'keys',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-ip-tcp-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_tcp_cfg',
        ),
    },
    'IpTcp.Ao.Keychains.Keychain' : {
        'meta_info' : _MetaInfoClass('IpTcp.Ao.Keychains.Keychain', REFERENCE_LIST,
            '''Name of the key chain''',
            False, 
            [
            _MetaInfoClassMember('name', ATTRIBUTE, 'str', 'xr:Cisco-ios-xr-string',
                None, None,
                [(1, 32)], [],
                '''                Name of the key chain
                ''',
                'name',
                'Cisco-IOS-XR-ip-tcp-cfg', True),
            _MetaInfoClassMember('keys', REFERENCE_CLASS, 'Keys', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_tcp_cfg', 'IpTcp.Ao.Keychains.Keychain.Keys',
                [], [],
                '''                Configure a Key
                ''',
                'keys',
                'Cisco-IOS-XR-ip-tcp-cfg', False),
            _MetaInfoClassMember('create', ATTRIBUTE, 'Empty', 'empty',
                None, None,
                [], [],
                '''                Create keychain
                ''',
                'create',
                'Cisco-IOS-XR-ip-tcp-cfg', False),
            ],
            'Cisco-IOS-XR-ip-tcp-cfg',
            'keychain',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-ip-tcp-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_tcp_cfg',
        ),
    },
    'IpTcp.Ao.Keychains' : {
        'meta_info' : _MetaInfoClass('IpTcp.Ao.Keychains', REFERENCE_CLASS,
            '''Configure a Key Chain''',
            False, 
            [
            _MetaInfoClassMember('keychain', REFERENCE_LIST, 'Keychain', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_tcp_cfg', 'IpTcp.Ao.Keychains.Keychain',
                [], [],
                '''                Name of the key chain
                ''',
                'keychain',
                'Cisco-IOS-XR-ip-tcp-cfg', False),
            ],
            'Cisco-IOS-XR-ip-tcp-cfg',
            'keychains',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-ip-tcp-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_tcp_cfg',
        ),
    },
    'IpTcp.Ao' : {
        'meta_info' : _MetaInfoClass('IpTcp.Ao', REFERENCE_CLASS,
            '''TCP authentication option configuration mode''',
            False, 
            [
            _MetaInfoClassMember('keychains', REFERENCE_CLASS, 'Keychains', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_tcp_cfg', 'IpTcp.Ao.Keychains',
                [], [],
                '''                Configure a Key Chain
                ''',
                'keychains',
                'Cisco-IOS-XR-ip-tcp-cfg', False),
            _MetaInfoClassMember('enable', ATTRIBUTE, 'Empty', 'empty',
                None, None,
                [], [],
                '''                Create TCP-AO submode
                ''',
                'enable',
                'Cisco-IOS-XR-ip-tcp-cfg', False),
            ],
            'Cisco-IOS-XR-ip-tcp-cfg',
            'ao',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-ip-tcp-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_tcp_cfg',
        ),
    },
    'IpTcp.NumThread' : {
        'meta_info' : _MetaInfoClass('IpTcp.NumThread', REFERENCE_CLASS,
            '''TCP InQueue and OutQueue threads''',
            False, 
            [
            _MetaInfoClassMember('tcp-in-q-threads', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('1', '16')], [],
                '''                InQ Threads
                ''',
                'tcp_in_q_threads',
                'Cisco-IOS-XR-ip-tcp-cfg', False, is_mandatory=True),
            _MetaInfoClassMember('tcp-out-q-threads', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('1', '16')], [],
                '''                OutQ Threads
                ''',
                'tcp_out_q_threads',
                'Cisco-IOS-XR-ip-tcp-cfg', False, is_mandatory=True),
            ],
            'Cisco-IOS-XR-ip-tcp-cfg',
            'num-thread',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-ip-tcp-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_tcp_cfg',
            is_presence=True,
        ),
    },
    'IpTcp' : {
        'meta_info' : _MetaInfoClass('IpTcp', REFERENCE_CLASS,
            '''Global IP TCP configuration''',
            False, 
            [
            _MetaInfoClassMember('directory', REFERENCE_CLASS, 'Directory', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_tcp_cfg', 'IpTcp.Directory',
                [], [],
                '''                TCP directory details
                ''',
                'directory',
                'Cisco-IOS-XR-ip-tcp-cfg', False, is_presence=True),
            _MetaInfoClassMember('throttle', REFERENCE_CLASS, 'Throttle', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_tcp_cfg', 'IpTcp.Throttle',
                [], [],
                '''                Throttle TCP receive buffer (in percentage)
                ''',
                'throttle',
                'Cisco-IOS-XR-ip-tcp-cfg', False, is_presence=True),
            _MetaInfoClassMember('ao', REFERENCE_CLASS, 'Ao', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_tcp_cfg', 'IpTcp.Ao',
                [], [],
                '''                TCP authentication option configuration mode
                ''',
                'ao',
                'Cisco-IOS-XR-ip-tcp-cfg', False),
            _MetaInfoClassMember('num-thread', REFERENCE_CLASS, 'NumThread', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_tcp_cfg', 'IpTcp.NumThread',
                [], [],
                '''                TCP InQueue and OutQueue threads
                ''',
                'num_thread',
                'Cisco-IOS-XR-ip-tcp-cfg', False, is_presence=True),
            _MetaInfoClassMember('accept-rate', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('1', '1000')], [],
                '''                TCP connection accept rate
                ''',
                'accept_rate',
                'Cisco-IOS-XR-ip-tcp-cfg', False, default_value="500"),
            _MetaInfoClassMember('selective-ack', ATTRIBUTE, 'Empty', 'empty',
                None, None,
                [], [],
                '''                Enable TCP selective-ACK
                ''',
                'selective_ack',
                'Cisco-IOS-XR-ip-tcp-cfg', False),
            _MetaInfoClassMember('window-size', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('2048', '65535')], [],
                '''                TCP receive window size (bytes)
                ''',
                'window_size',
                'Cisco-IOS-XR-ip-tcp-cfg', False),
            _MetaInfoClassMember('receive-q', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('40', '800')], [],
                '''                TCP receive Queue Size
                ''',
                'receive_q',
                'Cisco-IOS-XR-ip-tcp-cfg', False),
            _MetaInfoClassMember('maximum-segment-size', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('68', '10000')], [],
                '''                TCP initial maximum segment size
                ''',
                'maximum_segment_size',
                'Cisco-IOS-XR-ip-tcp-cfg', False),
            _MetaInfoClassMember('syn-wait-time', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('5', '30')], [],
                '''                Time to wait on new TCP connections in seconds
                ''',
                'syn_wait_time',
                'Cisco-IOS-XR-ip-tcp-cfg', False),
            _MetaInfoClassMember('timestamp', ATTRIBUTE, 'Empty', 'empty',
                None, None,
                [], [],
                '''                Enable TCP timestamp option
                ''',
                'timestamp',
                'Cisco-IOS-XR-ip-tcp-cfg', False),
            _MetaInfoClassMember('path-mtu-discovery', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('0', '4294967295')], [],
                '''                Aging time; 0 for infinite, and range be (10,30)
                ''',
                'path_mtu_discovery',
                'Cisco-IOS-XR-ip-tcp-cfg', False, default_value="10"),
            ],
            'Cisco-IOS-XR-ip-tcp-cfg',
            'ip-tcp',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-ip-tcp-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_tcp_cfg',
            is_presence=True,
        ),
    },
    'Ip.Cinetd.Services.Ipv4.SmallServers.TcpSmallServers.SmallServer' : _MetaInfoEnum('SmallServer',
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_tcp_cfg', 'Ip.Cinetd.Services.Ipv4.SmallServers.TcpSmallServers.SmallServer',
        ''' ''',
        {
            'no-limit':'no_limit',
        }, 'Cisco-IOS-XR-ip-tcp-cfg', _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-ip-tcp-cfg']),
    'Ip.Cinetd.Services.Ipv4.SmallServers.TcpSmallServers' : {
        'meta_info' : _MetaInfoClass('Ip.Cinetd.Services.Ipv4.SmallServers.TcpSmallServers', REFERENCE_CLASS,
            '''Describing TCP related IPV4 and IPV6 small
servers''',
            False, 
            [
            _MetaInfoClassMember('access-control-list-name', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                Specify the access list
                ''',
                'access_control_list_name',
                'Cisco-IOS-XR-ip-tcp-cfg', False),
            _MetaInfoClassMember('small-server', REFERENCE_UNION, 'str', 'union',
                None, None,
                [], [],
                '''                Set number of allowable TCP small servers,
                specify 0 for no-limit
                ''',
                'small_server',
                'Cisco-IOS-XR-ip-tcp-cfg', False, [
                    _MetaInfoClassMember('small-server', REFERENCE_ENUM_CLASS, 'Ip.Cinetd.Services.Ipv6.SmallServers.TcpSmallServers.SmallServer', 'enumeration',
                        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_tcp_cfg', 'Ip.Cinetd.Services.Ipv6.SmallServers.TcpSmallServers.SmallServer',
                        [], [],
                        '''                        Set number of allowable TCP small servers,
                        specify 0 for no-limit
                        ''',
                        'small_server',
                        'Cisco-IOS-XR-ip-tcp-cfg', False, is_mandatory=True),
                    _MetaInfoClassMember('small-server', ATTRIBUTE, 'int', 'uint32',
                        None, None,
                        [('0', '2147483647')], [],
                        '''                        Set number of allowable TCP small servers,
                        specify 0 for no-limit
                        ''',
                        'small_server',
                        'Cisco-IOS-XR-ip-tcp-cfg', False, is_mandatory=True),
                ], is_mandatory=True),
            ],
            'Cisco-IOS-XR-ip-tcp-cfg',
            'tcp-small-servers',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-ip-tcp-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_tcp_cfg',
            is_presence=True,
        ),
    },
    'Ip.Cinetd.Services.Ipv4.SmallServers.UdpSmallServers.SmallServer' : _MetaInfoEnum('SmallServer',
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_tcp_cfg', 'Ip.Cinetd.Services.Ipv4.SmallServers.UdpSmallServers.SmallServer',
        ''' ''',
        {
            'no-limit':'no_limit',
        }, 'Cisco-IOS-XR-ip-udp-cfg', _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-ip-udp-cfg']),
    'Ip.Cinetd.Services.Ipv4.SmallServers.UdpSmallServers' : {
        'meta_info' : _MetaInfoClass('Ip.Cinetd.Services.Ipv4.SmallServers.UdpSmallServers', REFERENCE_CLASS,
            '''UDP small servers configuration''',
            False, 
            [
            _MetaInfoClassMember('access-control-list-name', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                Specify the access list
                ''',
                'access_control_list_name',
                'Cisco-IOS-XR-ip-udp-cfg', False),
            _MetaInfoClassMember('small-server', REFERENCE_UNION, 'str', 'union',
                None, None,
                [], [],
                '''                Set number of allowable small servers, specify
                0 for no-limit
                ''',
                'small_server',
                'Cisco-IOS-XR-ip-udp-cfg', False, [
                    _MetaInfoClassMember('small-server', REFERENCE_ENUM_CLASS, 'Ip.Cinetd.Services.Ipv4.SmallServers.UdpSmallServers.SmallServer', 'enumeration',
                        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_tcp_cfg', 'Ip.Cinetd.Services.Ipv4.SmallServers.UdpSmallServers.SmallServer',
                        [], [],
                        '''                        Set number of allowable small servers, specify
                        0 for no-limit
                        ''',
                        'small_server',
                        'Cisco-IOS-XR-ip-udp-cfg', False, is_mandatory=True),
                    _MetaInfoClassMember('small-server', ATTRIBUTE, 'int', 'uint32',
                        None, None,
                        [('0', '2147483647')], [],
                        '''                        Set number of allowable small servers, specify
                        0 for no-limit
                        ''',
                        'small_server',
                        'Cisco-IOS-XR-ip-udp-cfg', False, is_mandatory=True),
                ], is_mandatory=True),
            ],
            'Cisco-IOS-XR-ip-udp-cfg',
            'udp-small-servers',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-ip-udp-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_tcp_cfg',
            is_presence=True,
        ),
    },
    'Ip.Cinetd.Services.Ipv4.SmallServers' : {
        'meta_info' : _MetaInfoClass('Ip.Cinetd.Services.Ipv4.SmallServers', REFERENCE_CLASS,
            '''Describing IPV4 and IPV6 small servers''',
            False, 
            [
            _MetaInfoClassMember('tcp-small-servers', REFERENCE_CLASS, 'TcpSmallServers', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_tcp_cfg', 'Ip.Cinetd.Services.Ipv4.SmallServers.TcpSmallServers',
                [], [],
                '''                Describing TCP related IPV4 and IPV6 small
                servers
                ''',
                'tcp_small_servers',
                'Cisco-IOS-XR-ip-tcp-cfg', False, is_presence=True),
            _MetaInfoClassMember('udp-small-servers', REFERENCE_CLASS, 'UdpSmallServers', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_tcp_cfg', 'Ip.Cinetd.Services.Ipv4.SmallServers.UdpSmallServers',
                [], [],
                '''                UDP small servers configuration
                ''',
                'udp_small_servers',
                'Cisco-IOS-XR-ip-udp-cfg', False, is_presence=True),
            ],
            'Cisco-IOS-XR-ip-tcp-cfg',
            'small-servers',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-ip-tcp-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_tcp_cfg',
        ),
    },
    'Ip.Cinetd.Services.Ipv4' : {
        'meta_info' : _MetaInfoClass('Ip.Cinetd.Services.Ipv4', REFERENCE_CLASS,
            '''IPV4 related services''',
            False, 
            [
            _MetaInfoClassMember('small-servers', REFERENCE_CLASS, 'SmallServers', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_tcp_cfg', 'Ip.Cinetd.Services.Ipv4.SmallServers',
                [], [],
                '''                Describing IPV4 and IPV6 small servers
                ''',
                'small_servers',
                'Cisco-IOS-XR-ip-tcp-cfg', False),
            ],
            'Cisco-IOS-XR-ip-tcp-cfg',
            'ipv4',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-ip-tcp-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_tcp_cfg',
        ),
    },
    'Ip.Cinetd.Services.Vrfs.Vrf.Ipv6.Telnet.Tcp' : {
        'meta_info' : _MetaInfoClass('Ip.Cinetd.Services.Vrfs.Vrf.Ipv6.Telnet.Tcp', REFERENCE_CLASS,
            '''TCP details''',
            False, 
            [
            _MetaInfoClassMember('access-list-name', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                Access list
                ''',
                'access_list_name',
                'Cisco-IOS-XR-ip-tcp-cfg', False),
            _MetaInfoClassMember('maximum-server', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('1', '100')], [],
                '''                Set number of allowable servers
                ''',
                'maximum_server',
                'Cisco-IOS-XR-ip-tcp-cfg', False, is_mandatory=True),
            ],
            'Cisco-IOS-XR-ip-tcp-cfg',
            'tcp',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-ip-tcp-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_tcp_cfg',
            is_presence=True,
        ),
    },
    'Ip.Cinetd.Services.Vrfs.Vrf.Ipv6.Telnet' : {
        'meta_info' : _MetaInfoClass('Ip.Cinetd.Services.Vrfs.Vrf.Ipv6.Telnet', REFERENCE_CLASS,
            '''TELNET server configuration commands''',
            False, 
            [
            _MetaInfoClassMember('tcp', REFERENCE_CLASS, 'Tcp', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_tcp_cfg', 'Ip.Cinetd.Services.Vrfs.Vrf.Ipv6.Telnet.Tcp',
                [], [],
                '''                TCP details
                ''',
                'tcp',
                'Cisco-IOS-XR-ip-tcp-cfg', False, is_presence=True),
            ],
            'Cisco-IOS-XR-ip-tcp-cfg',
            'telnet',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-ip-tcp-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_tcp_cfg',
        ),
    },
    'Ip.Cinetd.Services.Vrfs.Vrf.Ipv6.Tftp.Udp' : {
        'meta_info' : _MetaInfoClass('Ip.Cinetd.Services.Vrfs.Vrf.Ipv6.Tftp.Udp', REFERENCE_CLASS,
            '''UDP details''',
            False, 
            [
            _MetaInfoClassMember('access-list-name', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                Access list
                ''',
                'access_list_name',
                'Cisco-IOS-XR-ip-tcp-cfg', False),
            _MetaInfoClassMember('maximum-server', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('0', '2147483647')], [],
                '''                Set number of allowable servers, 0 for
                no-limit
                ''',
                'maximum_server',
                'Cisco-IOS-XR-ip-tcp-cfg', False),
            _MetaInfoClassMember('home-directory', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                Specify device name where file is read from (e
                .g. flash:)
                ''',
                'home_directory',
                'Cisco-IOS-XR-ip-tcp-cfg', False, is_mandatory=True),
            _MetaInfoClassMember('dscp-value', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('0', '4294967295')], [],
                '''                Set IP DSCP (DiffServ CodePoint) for TFTP
                Server Packets
                ''',
                'dscp_value',
                'Cisco-IOS-XR-ip-tcp-cfg', False),
            ],
            'Cisco-IOS-XR-ip-tcp-cfg',
            'udp',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-ip-tcp-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_tcp_cfg',
            is_presence=True,
        ),
    },
    'Ip.Cinetd.Services.Vrfs.Vrf.Ipv6.Tftp' : {
        'meta_info' : _MetaInfoClass('Ip.Cinetd.Services.Vrfs.Vrf.Ipv6.Tftp', REFERENCE_CLASS,
            '''TFTP server configuration commands''',
            False, 
            [
            _MetaInfoClassMember('udp', REFERENCE_CLASS, 'Udp', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_tcp_cfg', 'Ip.Cinetd.Services.Vrfs.Vrf.Ipv6.Tftp.Udp',
                [], [],
                '''                UDP details
                ''',
                'udp',
                'Cisco-IOS-XR-ip-tcp-cfg', False, is_presence=True),
            ],
            'Cisco-IOS-XR-ip-tcp-cfg',
            'tftp',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-ip-tcp-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_tcp_cfg',
        ),
    },
    'Ip.Cinetd.Services.Vrfs.Vrf.Ipv6' : {
        'meta_info' : _MetaInfoClass('Ip.Cinetd.Services.Vrfs.Vrf.Ipv6', REFERENCE_CLASS,
            '''IPV6 related services''',
            False, 
            [
            _MetaInfoClassMember('telnet', REFERENCE_CLASS, 'Telnet', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_tcp_cfg', 'Ip.Cinetd.Services.Vrfs.Vrf.Ipv6.Telnet',
                [], [],
                '''                TELNET server configuration commands
                ''',
                'telnet',
                'Cisco-IOS-XR-ip-tcp-cfg', False),
            _MetaInfoClassMember('tftp', REFERENCE_CLASS, 'Tftp', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_tcp_cfg', 'Ip.Cinetd.Services.Vrfs.Vrf.Ipv6.Tftp',
                [], [],
                '''                TFTP server configuration commands
                ''',
                'tftp',
                'Cisco-IOS-XR-ip-tcp-cfg', False),
            ],
            'Cisco-IOS-XR-ip-tcp-cfg',
            'ipv6',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-ip-tcp-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_tcp_cfg',
        ),
    },
    'Ip.Cinetd.Services.Vrfs.Vrf.Ipv4.Telnet.Tcp' : {
        'meta_info' : _MetaInfoClass('Ip.Cinetd.Services.Vrfs.Vrf.Ipv4.Telnet.Tcp', REFERENCE_CLASS,
            '''TCP details''',
            False, 
            [
            _MetaInfoClassMember('access-list-name', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                Access list
                ''',
                'access_list_name',
                'Cisco-IOS-XR-ip-tcp-cfg', False),
            _MetaInfoClassMember('maximum-server', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('1', '100')], [],
                '''                Set number of allowable servers
                ''',
                'maximum_server',
                'Cisco-IOS-XR-ip-tcp-cfg', False, is_mandatory=True),
            ],
            'Cisco-IOS-XR-ip-tcp-cfg',
            'tcp',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-ip-tcp-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_tcp_cfg',
            is_presence=True,
        ),
    },
    'Ip.Cinetd.Services.Vrfs.Vrf.Ipv4.Telnet' : {
        'meta_info' : _MetaInfoClass('Ip.Cinetd.Services.Vrfs.Vrf.Ipv4.Telnet', REFERENCE_CLASS,
            '''TELNET server configuration commands''',
            False, 
            [
            _MetaInfoClassMember('tcp', REFERENCE_CLASS, 'Tcp', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_tcp_cfg', 'Ip.Cinetd.Services.Vrfs.Vrf.Ipv4.Telnet.Tcp',
                [], [],
                '''                TCP details
                ''',
                'tcp',
                'Cisco-IOS-XR-ip-tcp-cfg', False, is_presence=True),
            ],
            'Cisco-IOS-XR-ip-tcp-cfg',
            'telnet',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-ip-tcp-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_tcp_cfg',
        ),
    },
    'Ip.Cinetd.Services.Vrfs.Vrf.Ipv4.Tftp.Udp' : {
        'meta_info' : _MetaInfoClass('Ip.Cinetd.Services.Vrfs.Vrf.Ipv4.Tftp.Udp', REFERENCE_CLASS,
            '''UDP details''',
            False, 
            [
            _MetaInfoClassMember('access-list-name', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                Access list
                ''',
                'access_list_name',
                'Cisco-IOS-XR-ip-tcp-cfg', False),
            _MetaInfoClassMember('maximum-server', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('0', '2147483647')], [],
                '''                Set number of allowable servers, 0 for
                no-limit
                ''',
                'maximum_server',
                'Cisco-IOS-XR-ip-tcp-cfg', False),
            _MetaInfoClassMember('home-directory', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                Specify device name where file is read from (e
                .g. flash:)
                ''',
                'home_directory',
                'Cisco-IOS-XR-ip-tcp-cfg', False, is_mandatory=True),
            _MetaInfoClassMember('dscp-value', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('0', '4294967295')], [],
                '''                Set IP DSCP (DiffServ CodePoint) for TFTP
                Server Packets
                ''',
                'dscp_value',
                'Cisco-IOS-XR-ip-tcp-cfg', False),
            ],
            'Cisco-IOS-XR-ip-tcp-cfg',
            'udp',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-ip-tcp-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_tcp_cfg',
            is_presence=True,
        ),
    },
    'Ip.Cinetd.Services.Vrfs.Vrf.Ipv4.Tftp' : {
        'meta_info' : _MetaInfoClass('Ip.Cinetd.Services.Vrfs.Vrf.Ipv4.Tftp', REFERENCE_CLASS,
            '''TFTP server configuration commands''',
            False, 
            [
            _MetaInfoClassMember('udp', REFERENCE_CLASS, 'Udp', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_tcp_cfg', 'Ip.Cinetd.Services.Vrfs.Vrf.Ipv4.Tftp.Udp',
                [], [],
                '''                UDP details
                ''',
                'udp',
                'Cisco-IOS-XR-ip-tcp-cfg', False, is_presence=True),
            ],
            'Cisco-IOS-XR-ip-tcp-cfg',
            'tftp',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-ip-tcp-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_tcp_cfg',
        ),
    },
    'Ip.Cinetd.Services.Vrfs.Vrf.Ipv4' : {
        'meta_info' : _MetaInfoClass('Ip.Cinetd.Services.Vrfs.Vrf.Ipv4', REFERENCE_CLASS,
            '''IPV4 related services''',
            False, 
            [
            _MetaInfoClassMember('telnet', REFERENCE_CLASS, 'Telnet', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_tcp_cfg', 'Ip.Cinetd.Services.Vrfs.Vrf.Ipv4.Telnet',
                [], [],
                '''                TELNET server configuration commands
                ''',
                'telnet',
                'Cisco-IOS-XR-ip-tcp-cfg', False),
            _MetaInfoClassMember('tftp', REFERENCE_CLASS, 'Tftp', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_tcp_cfg', 'Ip.Cinetd.Services.Vrfs.Vrf.Ipv4.Tftp',
                [], [],
                '''                TFTP server configuration commands
                ''',
                'tftp',
                'Cisco-IOS-XR-ip-tcp-cfg', False),
            ],
            'Cisco-IOS-XR-ip-tcp-cfg',
            'ipv4',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-ip-tcp-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_tcp_cfg',
        ),
    },
    'Ip.Cinetd.Services.Vrfs.Vrf' : {
        'meta_info' : _MetaInfoClass('Ip.Cinetd.Services.Vrfs.Vrf', REFERENCE_LIST,
            '''VRF specific data''',
            False, 
            [
            _MetaInfoClassMember('vrf-name', ATTRIBUTE, 'str', 'xr:Cisco-ios-xr-string',
                None, None,
                [], [b'[\\w\\-\\.:,_@#%$\\+=\\|;]+'],
                '''                Name of the VRF instance
                ''',
                'vrf_name',
                'Cisco-IOS-XR-ip-tcp-cfg', True),
            _MetaInfoClassMember('ipv6', REFERENCE_CLASS, 'Ipv6', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_tcp_cfg', 'Ip.Cinetd.Services.Vrfs.Vrf.Ipv6',
                [], [],
                '''                IPV6 related services
                ''',
                'ipv6',
                'Cisco-IOS-XR-ip-tcp-cfg', False),
            _MetaInfoClassMember('ipv4', REFERENCE_CLASS, 'Ipv4', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_tcp_cfg', 'Ip.Cinetd.Services.Vrfs.Vrf.Ipv4',
                [], [],
                '''                IPV4 related services
                ''',
                'ipv4',
                'Cisco-IOS-XR-ip-tcp-cfg', False),
            ],
            'Cisco-IOS-XR-ip-tcp-cfg',
            'vrf',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-ip-tcp-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_tcp_cfg',
            has_must=True,
        ),
    },
    'Ip.Cinetd.Services.Vrfs' : {
        'meta_info' : _MetaInfoClass('Ip.Cinetd.Services.Vrfs', REFERENCE_CLASS,
            '''VRF table''',
            False, 
            [
            _MetaInfoClassMember('vrf', REFERENCE_LIST, 'Vrf', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_tcp_cfg', 'Ip.Cinetd.Services.Vrfs.Vrf',
                [], [],
                '''                VRF specific data
                ''',
                'vrf',
                'Cisco-IOS-XR-ip-tcp-cfg', False, has_must=True),
            ],
            'Cisco-IOS-XR-ip-tcp-cfg',
            'vrfs',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-ip-tcp-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_tcp_cfg',
        ),
    },
    'Ip.Cinetd.Services.Ipv6.SmallServers.TcpSmallServers.SmallServer' : _MetaInfoEnum('SmallServer',
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_tcp_cfg', 'Ip.Cinetd.Services.Ipv6.SmallServers.TcpSmallServers.SmallServer',
        ''' ''',
        {
            'no-limit':'no_limit',
        }, 'Cisco-IOS-XR-ip-tcp-cfg', _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-ip-tcp-cfg']),
    'Ip.Cinetd.Services.Ipv6.SmallServers.TcpSmallServers' : {
        'meta_info' : _MetaInfoClass('Ip.Cinetd.Services.Ipv6.SmallServers.TcpSmallServers', REFERENCE_CLASS,
            '''Describing TCP related IPV4 and IPV6 small
servers''',
            False, 
            [
            _MetaInfoClassMember('access-control-list-name', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                Specify the access list
                ''',
                'access_control_list_name',
                'Cisco-IOS-XR-ip-tcp-cfg', False),
            _MetaInfoClassMember('small-server', REFERENCE_UNION, 'str', 'union',
                None, None,
                [], [],
                '''                Set number of allowable TCP small servers,
                specify 0 for no-limit
                ''',
                'small_server',
                'Cisco-IOS-XR-ip-tcp-cfg', False, [
                    _MetaInfoClassMember('small-server', REFERENCE_ENUM_CLASS, 'Ip.Cinetd.Services.Ipv6.SmallServers.TcpSmallServers.SmallServer', 'enumeration',
                        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_tcp_cfg', 'Ip.Cinetd.Services.Ipv6.SmallServers.TcpSmallServers.SmallServer',
                        [], [],
                        '''                        Set number of allowable TCP small servers,
                        specify 0 for no-limit
                        ''',
                        'small_server',
                        'Cisco-IOS-XR-ip-tcp-cfg', False, is_mandatory=True),
                    _MetaInfoClassMember('small-server', ATTRIBUTE, 'int', 'uint32',
                        None, None,
                        [('0', '2147483647')], [],
                        '''                        Set number of allowable TCP small servers,
                        specify 0 for no-limit
                        ''',
                        'small_server',
                        'Cisco-IOS-XR-ip-tcp-cfg', False, is_mandatory=True),
                ], is_mandatory=True),
            ],
            'Cisco-IOS-XR-ip-tcp-cfg',
            'tcp-small-servers',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-ip-tcp-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_tcp_cfg',
            is_presence=True,
        ),
    },
    'Ip.Cinetd.Services.Ipv6.SmallServers.UdpSmallServers.SmallServer' : _MetaInfoEnum('SmallServer',
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_tcp_cfg', 'Ip.Cinetd.Services.Ipv6.SmallServers.UdpSmallServers.SmallServer',
        ''' ''',
        {
            'no-limit':'no_limit',
        }, 'Cisco-IOS-XR-ip-udp-cfg', _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-ip-udp-cfg']),
    'Ip.Cinetd.Services.Ipv6.SmallServers.UdpSmallServers' : {
        'meta_info' : _MetaInfoClass('Ip.Cinetd.Services.Ipv6.SmallServers.UdpSmallServers', REFERENCE_CLASS,
            '''UDP small servers configuration''',
            False, 
            [
            _MetaInfoClassMember('access-control-list-name', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                Specify the access list
                ''',
                'access_control_list_name',
                'Cisco-IOS-XR-ip-udp-cfg', False),
            _MetaInfoClassMember('small-server', REFERENCE_UNION, 'str', 'union',
                None, None,
                [], [],
                '''                Set number of allowable small servers, specify
                0 for no-limit
                ''',
                'small_server',
                'Cisco-IOS-XR-ip-udp-cfg', False, [
                    _MetaInfoClassMember('small-server', REFERENCE_ENUM_CLASS, 'Ip.Cinetd.Services.Ipv6.SmallServers.UdpSmallServers.SmallServer', 'enumeration',
                        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_tcp_cfg', 'Ip.Cinetd.Services.Ipv6.SmallServers.UdpSmallServers.SmallServer',
                        [], [],
                        '''                        Set number of allowable small servers, specify
                        0 for no-limit
                        ''',
                        'small_server',
                        'Cisco-IOS-XR-ip-udp-cfg', False, is_mandatory=True),
                    _MetaInfoClassMember('small-server', ATTRIBUTE, 'int', 'uint32',
                        None, None,
                        [('0', '2147483647')], [],
                        '''                        Set number of allowable small servers, specify
                        0 for no-limit
                        ''',
                        'small_server',
                        'Cisco-IOS-XR-ip-udp-cfg', False, is_mandatory=True),
                ], is_mandatory=True),
            ],
            'Cisco-IOS-XR-ip-udp-cfg',
            'udp-small-servers',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-ip-udp-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_tcp_cfg',
            is_presence=True,
        ),
    },
    'Ip.Cinetd.Services.Ipv6.SmallServers' : {
        'meta_info' : _MetaInfoClass('Ip.Cinetd.Services.Ipv6.SmallServers', REFERENCE_CLASS,
            '''Describing IPV4 and IPV6 small servers''',
            False, 
            [
            _MetaInfoClassMember('tcp-small-servers', REFERENCE_CLASS, 'TcpSmallServers', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_tcp_cfg', 'Ip.Cinetd.Services.Ipv6.SmallServers.TcpSmallServers',
                [], [],
                '''                Describing TCP related IPV4 and IPV6 small
                servers
                ''',
                'tcp_small_servers',
                'Cisco-IOS-XR-ip-tcp-cfg', False, is_presence=True),
            _MetaInfoClassMember('udp-small-servers', REFERENCE_CLASS, 'UdpSmallServers', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_tcp_cfg', 'Ip.Cinetd.Services.Ipv6.SmallServers.UdpSmallServers',
                [], [],
                '''                UDP small servers configuration
                ''',
                'udp_small_servers',
                'Cisco-IOS-XR-ip-udp-cfg', False, is_presence=True),
            ],
            'Cisco-IOS-XR-ip-tcp-cfg',
            'small-servers',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-ip-tcp-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_tcp_cfg',
        ),
    },
    'Ip.Cinetd.Services.Ipv6' : {
        'meta_info' : _MetaInfoClass('Ip.Cinetd.Services.Ipv6', REFERENCE_CLASS,
            '''IPV6 related services''',
            False, 
            [
            _MetaInfoClassMember('small-servers', REFERENCE_CLASS, 'SmallServers', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_tcp_cfg', 'Ip.Cinetd.Services.Ipv6.SmallServers',
                [], [],
                '''                Describing IPV4 and IPV6 small servers
                ''',
                'small_servers',
                'Cisco-IOS-XR-ip-tcp-cfg', False),
            ],
            'Cisco-IOS-XR-ip-tcp-cfg',
            'ipv6',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-ip-tcp-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_tcp_cfg',
        ),
    },
    'Ip.Cinetd.Services' : {
        'meta_info' : _MetaInfoClass('Ip.Cinetd.Services', REFERENCE_CLASS,
            '''Describing services of cinetd''',
            False, 
            [
            _MetaInfoClassMember('ipv4', REFERENCE_CLASS, 'Ipv4', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_tcp_cfg', 'Ip.Cinetd.Services.Ipv4',
                [], [],
                '''                IPV4 related services
                ''',
                'ipv4',
                'Cisco-IOS-XR-ip-tcp-cfg', False),
            _MetaInfoClassMember('vrfs', REFERENCE_CLASS, 'Vrfs', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_tcp_cfg', 'Ip.Cinetd.Services.Vrfs',
                [], [],
                '''                VRF table
                ''',
                'vrfs',
                'Cisco-IOS-XR-ip-tcp-cfg', False),
            _MetaInfoClassMember('ipv6', REFERENCE_CLASS, 'Ipv6', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_tcp_cfg', 'Ip.Cinetd.Services.Ipv6',
                [], [],
                '''                IPV6 related services
                ''',
                'ipv6',
                'Cisco-IOS-XR-ip-tcp-cfg', False),
            ],
            'Cisco-IOS-XR-ip-tcp-cfg',
            'services',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-ip-tcp-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_tcp_cfg',
        ),
    },
    'Ip.Cinetd' : {
        'meta_info' : _MetaInfoClass('Ip.Cinetd', REFERENCE_CLASS,
            '''Cinetd configuration data''',
            False, 
            [
            _MetaInfoClassMember('services', REFERENCE_CLASS, 'Services', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_tcp_cfg', 'Ip.Cinetd.Services',
                [], [],
                '''                Describing services of cinetd
                ''',
                'services',
                'Cisco-IOS-XR-ip-tcp-cfg', False),
            _MetaInfoClassMember('rate-limit', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('1', '100')], [],
                '''                Number of service requests accepted per second
                ''',
                'rate_limit',
                'Cisco-IOS-XR-ipv4-cinetd-cfg', False, default_value="1"),
            ],
            'Cisco-IOS-XR-ip-tcp-cfg',
            'cinetd',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-ip-tcp-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_tcp_cfg',
        ),
    },
    'Ip.ForwardProtocol.Udp.Ports.Port' : {
        'meta_info' : _MetaInfoClass('Ip.ForwardProtocol.Udp.Ports.Port', REFERENCE_LIST,
            '''Well-known ports are enabled by default and
non well-known ports are disabled by default.
It is not allowed to configure the default.''',
            False, 
            [
            _MetaInfoClassMember('port-id', ATTRIBUTE, 'int', 'xr:Cisco-ios-xr-port-number',
                None, None,
                [('1', '65535')], [],
                '''                Port number
                ''',
                'port_id',
                'Cisco-IOS-XR-ip-udp-cfg', True),
            _MetaInfoClassMember('enable', ATTRIBUTE, 'bool', 'boolean',
                None, None,
                [], [],
                '''                Specify 'false' to disable well-known ports
                Domain (53), TFTP (69), NameServer (42),
                TACACS (49), NetBiosNameService (137), or
                NetBiosDatagramService (138).  Specify
                'true' to enable non well-known ports.
                ''',
                'enable',
                'Cisco-IOS-XR-ip-udp-cfg', False, is_mandatory=True),
            ],
            'Cisco-IOS-XR-ip-udp-cfg',
            'port',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-ip-udp-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_tcp_cfg',
        ),
    },
    'Ip.ForwardProtocol.Udp.Ports' : {
        'meta_info' : _MetaInfoClass('Ip.ForwardProtocol.Udp.Ports', REFERENCE_CLASS,
            '''Port configuration''',
            False, 
            [
            _MetaInfoClassMember('port', REFERENCE_LIST, 'Port', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_tcp_cfg', 'Ip.ForwardProtocol.Udp.Ports.Port',
                [], [],
                '''                Well-known ports are enabled by default and
                non well-known ports are disabled by default.
                It is not allowed to configure the default.
                ''',
                'port',
                'Cisco-IOS-XR-ip-udp-cfg', False),
            ],
            'Cisco-IOS-XR-ip-udp-cfg',
            'ports',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-ip-udp-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_tcp_cfg',
        ),
    },
    'Ip.ForwardProtocol.Udp' : {
        'meta_info' : _MetaInfoClass('Ip.ForwardProtocol.Udp', REFERENCE_CLASS,
            '''Packets to a specific UDP port''',
            False, 
            [
            _MetaInfoClassMember('ports', REFERENCE_CLASS, 'Ports', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_tcp_cfg', 'Ip.ForwardProtocol.Udp.Ports',
                [], [],
                '''                Port configuration
                ''',
                'ports',
                'Cisco-IOS-XR-ip-udp-cfg', False),
            _MetaInfoClassMember('disable', ATTRIBUTE, 'Empty', 'empty',
                None, None,
                [], [],
                '''                Disable IP Forward Protocol UDP
                ''',
                'disable',
                'Cisco-IOS-XR-ip-udp-cfg', False),
            ],
            'Cisco-IOS-XR-ip-udp-cfg',
            'udp',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-ip-udp-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_tcp_cfg',
        ),
    },
    'Ip.ForwardProtocol' : {
        'meta_info' : _MetaInfoClass('Ip.ForwardProtocol', REFERENCE_CLASS,
            '''Controls forwarding of physical and directed IP
broadcasts''',
            False, 
            [
            _MetaInfoClassMember('udp', REFERENCE_CLASS, 'Udp', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_tcp_cfg', 'Ip.ForwardProtocol.Udp',
                [], [],
                '''                Packets to a specific UDP port
                ''',
                'udp',
                'Cisco-IOS-XR-ip-udp-cfg', False),
            ],
            'Cisco-IOS-XR-ip-udp-cfg',
            'forward-protocol',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-ip-udp-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_tcp_cfg',
        ),
    },
    'Ip' : {
        'meta_info' : _MetaInfoClass('Ip', REFERENCE_CLASS,
            '''ip''',
            False, 
            [
            _MetaInfoClassMember('cinetd', REFERENCE_CLASS, 'Cinetd', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_tcp_cfg', 'Ip.Cinetd',
                [], [],
                '''                Cinetd configuration data
                ''',
                'cinetd',
                'Cisco-IOS-XR-ip-tcp-cfg', False),
            _MetaInfoClassMember('forward-protocol', REFERENCE_CLASS, 'ForwardProtocol', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_tcp_cfg', 'Ip.ForwardProtocol',
                [], [],
                '''                Controls forwarding of physical and directed IP
                broadcasts
                ''',
                'forward_protocol',
                'Cisco-IOS-XR-ip-udp-cfg', False),
            ],
            'Cisco-IOS-XR-ip-tcp-cfg',
            'ip',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-ip-tcp-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_tcp_cfg',
        ),
    },
}
_meta_table['IpTcp.Ao.Keychains.Keychain.Keys.Key']['meta_info'].parent =_meta_table['IpTcp.Ao.Keychains.Keychain.Keys']['meta_info']
_meta_table['IpTcp.Ao.Keychains.Keychain.Keys']['meta_info'].parent =_meta_table['IpTcp.Ao.Keychains.Keychain']['meta_info']
_meta_table['IpTcp.Ao.Keychains.Keychain']['meta_info'].parent =_meta_table['IpTcp.Ao.Keychains']['meta_info']
_meta_table['IpTcp.Ao.Keychains']['meta_info'].parent =_meta_table['IpTcp.Ao']['meta_info']
_meta_table['IpTcp.Directory']['meta_info'].parent =_meta_table['IpTcp']['meta_info']
_meta_table['IpTcp.Throttle']['meta_info'].parent =_meta_table['IpTcp']['meta_info']
_meta_table['IpTcp.Ao']['meta_info'].parent =_meta_table['IpTcp']['meta_info']
_meta_table['IpTcp.NumThread']['meta_info'].parent =_meta_table['IpTcp']['meta_info']
_meta_table['Ip.Cinetd.Services.Ipv4.SmallServers.TcpSmallServers']['meta_info'].parent =_meta_table['Ip.Cinetd.Services.Ipv4.SmallServers']['meta_info']
_meta_table['Ip.Cinetd.Services.Ipv4.SmallServers.UdpSmallServers']['meta_info'].parent =_meta_table['Ip.Cinetd.Services.Ipv4.SmallServers']['meta_info']
_meta_table['Ip.Cinetd.Services.Ipv4.SmallServers']['meta_info'].parent =_meta_table['Ip.Cinetd.Services.Ipv4']['meta_info']
_meta_table['Ip.Cinetd.Services.Vrfs.Vrf.Ipv6.Telnet.Tcp']['meta_info'].parent =_meta_table['Ip.Cinetd.Services.Vrfs.Vrf.Ipv6.Telnet']['meta_info']
_meta_table['Ip.Cinetd.Services.Vrfs.Vrf.Ipv6.Tftp.Udp']['meta_info'].parent =_meta_table['Ip.Cinetd.Services.Vrfs.Vrf.Ipv6.Tftp']['meta_info']
_meta_table['Ip.Cinetd.Services.Vrfs.Vrf.Ipv6.Telnet']['meta_info'].parent =_meta_table['Ip.Cinetd.Services.Vrfs.Vrf.Ipv6']['meta_info']
_meta_table['Ip.Cinetd.Services.Vrfs.Vrf.Ipv6.Tftp']['meta_info'].parent =_meta_table['Ip.Cinetd.Services.Vrfs.Vrf.Ipv6']['meta_info']
_meta_table['Ip.Cinetd.Services.Vrfs.Vrf.Ipv4.Telnet.Tcp']['meta_info'].parent =_meta_table['Ip.Cinetd.Services.Vrfs.Vrf.Ipv4.Telnet']['meta_info']
_meta_table['Ip.Cinetd.Services.Vrfs.Vrf.Ipv4.Tftp.Udp']['meta_info'].parent =_meta_table['Ip.Cinetd.Services.Vrfs.Vrf.Ipv4.Tftp']['meta_info']
_meta_table['Ip.Cinetd.Services.Vrfs.Vrf.Ipv4.Telnet']['meta_info'].parent =_meta_table['Ip.Cinetd.Services.Vrfs.Vrf.Ipv4']['meta_info']
_meta_table['Ip.Cinetd.Services.Vrfs.Vrf.Ipv4.Tftp']['meta_info'].parent =_meta_table['Ip.Cinetd.Services.Vrfs.Vrf.Ipv4']['meta_info']
_meta_table['Ip.Cinetd.Services.Vrfs.Vrf.Ipv6']['meta_info'].parent =_meta_table['Ip.Cinetd.Services.Vrfs.Vrf']['meta_info']
_meta_table['Ip.Cinetd.Services.Vrfs.Vrf.Ipv4']['meta_info'].parent =_meta_table['Ip.Cinetd.Services.Vrfs.Vrf']['meta_info']
_meta_table['Ip.Cinetd.Services.Vrfs.Vrf']['meta_info'].parent =_meta_table['Ip.Cinetd.Services.Vrfs']['meta_info']
_meta_table['Ip.Cinetd.Services.Ipv6.SmallServers.TcpSmallServers']['meta_info'].parent =_meta_table['Ip.Cinetd.Services.Ipv6.SmallServers']['meta_info']
_meta_table['Ip.Cinetd.Services.Ipv6.SmallServers.UdpSmallServers']['meta_info'].parent =_meta_table['Ip.Cinetd.Services.Ipv6.SmallServers']['meta_info']
_meta_table['Ip.Cinetd.Services.Ipv6.SmallServers']['meta_info'].parent =_meta_table['Ip.Cinetd.Services.Ipv6']['meta_info']
_meta_table['Ip.Cinetd.Services.Ipv4']['meta_info'].parent =_meta_table['Ip.Cinetd.Services']['meta_info']
_meta_table['Ip.Cinetd.Services.Vrfs']['meta_info'].parent =_meta_table['Ip.Cinetd.Services']['meta_info']
_meta_table['Ip.Cinetd.Services.Ipv6']['meta_info'].parent =_meta_table['Ip.Cinetd.Services']['meta_info']
_meta_table['Ip.Cinetd.Services']['meta_info'].parent =_meta_table['Ip.Cinetd']['meta_info']
_meta_table['Ip.ForwardProtocol.Udp.Ports.Port']['meta_info'].parent =_meta_table['Ip.ForwardProtocol.Udp.Ports']['meta_info']
_meta_table['Ip.ForwardProtocol.Udp.Ports']['meta_info'].parent =_meta_table['Ip.ForwardProtocol.Udp']['meta_info']
_meta_table['Ip.ForwardProtocol.Udp']['meta_info'].parent =_meta_table['Ip.ForwardProtocol']['meta_info']
_meta_table['Ip.Cinetd']['meta_info'].parent =_meta_table['Ip']['meta_info']
_meta_table['Ip.ForwardProtocol']['meta_info'].parent =_meta_table['Ip']['meta_info']
