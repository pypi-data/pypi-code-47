
'''
This is auto-generated file,
which includes metadata for module Cisco_IOS_XR_ppp_ea_oper
'''

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_LIST, REFERENCE_LEAFLIST, REFERENCE_BITS, REFERENCE_UNION
from ydk._core._dm_meta_info import REFERENCE_CLASS, REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, ANYXML_CLASS
from ydk._core._importer import _yang_ns

_meta_table = {
    'PppEaAdjState' : _MetaInfoEnum('PppEaAdjState',
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ppp_ea_oper', 'PppEaAdjState',
        '''Ppp ea adj state''',
        {
            'ppp-ea-adj-state-not-installed':'ppp_ea_adj_state_not_installed',
            'ppp-ea-adj-state-installed':'ppp_ea_adj_state_installed',
        }, 'Cisco-IOS-XR-ppp-ea-oper', _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-ppp-ea-oper']),
    'Pppea.Nodes.Node.EaInterfaceNames.EaInterfaceName' : {
        'meta_info' : _MetaInfoClass('Pppea.Nodes.Node.EaInterfaceNames.EaInterfaceName', REFERENCE_LIST,
            '''Interface name''',
            False, 
            [
            _MetaInfoClassMember('interface-name', ATTRIBUTE, 'str', 'xr:Interface-name',
                None, None,
                [], [b'[a-zA-Z0-9._/-]+'],
                '''                Interface running PPPEA
                ''',
                'interface_name',
                'Cisco-IOS-XR-ppp-ea-oper', True, is_config=False),
            _MetaInfoClassMember('interface', ATTRIBUTE, 'str', 'xr:Interface-name',
                None, None,
                [], [b'[a-zA-Z0-9._/-]+'],
                '''                Interface
                ''',
                'interface',
                'Cisco-IOS-XR-ppp-ea-oper', False, is_config=False),
            _MetaInfoClassMember('is-lcp-running', ATTRIBUTE, 'bool', 'boolean',
                None, None,
                [], [],
                '''                TRUE if LCP is running in the dataplane for the
                interface
                ''',
                'is_lcp_running',
                'Cisco-IOS-XR-ppp-ea-oper', False, is_config=False),
            _MetaInfoClassMember('is-ipcp-running', ATTRIBUTE, 'bool', 'boolean',
                None, None,
                [], [],
                '''                TRUE if IPCP is running in the dataplane for the
                interface
                ''',
                'is_ipcp_running',
                'Cisco-IOS-XR-ppp-ea-oper', False, is_config=False),
            _MetaInfoClassMember('is-ipv6cp-running', ATTRIBUTE, 'bool', 'boolean',
                None, None,
                [], [],
                '''                TRUE if IPV6CP is running in the dataplane for
                the interface
                ''',
                'is_ipv6cp_running',
                'Cisco-IOS-XR-ppp-ea-oper', False, is_config=False),
            _MetaInfoClassMember('is-mplscp-running', ATTRIBUTE, 'bool', 'boolean',
                None, None,
                [], [],
                '''                TRUE if MPLSCP is running in the dataplane for
                the interface
                ''',
                'is_mplscp_running',
                'Cisco-IOS-XR-ppp-ea-oper', False, is_config=False),
            _MetaInfoClassMember('local-mtu', ATTRIBUTE, 'int', 'uint16',
                None, None,
                [('0', '65535')], [],
                '''                Local interface MTU
                ''',
                'local_mtu',
                'Cisco-IOS-XR-ppp-ea-oper', False, is_config=False),
            _MetaInfoClassMember('local-mrru', ATTRIBUTE, 'int', 'uint16',
                None, None,
                [('0', '65535')], [],
                '''                Local MRRU
                ''',
                'local_mrru',
                'Cisco-IOS-XR-ppp-ea-oper', False, is_config=False),
            _MetaInfoClassMember('peer-mrru', ATTRIBUTE, 'int', 'uint16',
                None, None,
                [('0', '65535')], [],
                '''                Peer MRRU
                ''',
                'peer_mrru',
                'Cisco-IOS-XR-ppp-ea-oper', False, is_config=False),
            _MetaInfoClassMember('local-magic', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('0', '4294967295')], [],
                '''                Local magic number
                ''',
                'local_magic',
                'Cisco-IOS-XR-ppp-ea-oper', False, is_config=False),
            _MetaInfoClassMember('peer-magic', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('0', '4294967295')], [],
                '''                Peer magic number
                ''',
                'peer_magic',
                'Cisco-IOS-XR-ppp-ea-oper', False, is_config=False),
            _MetaInfoClassMember('local-mcmp-classes', ATTRIBUTE, 'int', 'uint8',
                None, None,
                [('0', '255')], [],
                '''                Local number of MCMP Suspension classes
                ''',
                'local_mcmp_classes',
                'Cisco-IOS-XR-ppp-ea-oper', False, is_config=False),
            _MetaInfoClassMember('peer-mcmp-classes', ATTRIBUTE, 'int', 'uint8',
                None, None,
                [('0', '255')], [],
                '''                Peer number of MCMP Suspension classes
                ''',
                'peer_mcmp_classes',
                'Cisco-IOS-XR-ppp-ea-oper', False, is_config=False),
            _MetaInfoClassMember('echo-request-interval', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('0', '4294967295')], [],
                '''                Echo-Request interval
                ''',
                'echo_request_interval',
                'Cisco-IOS-XR-ppp-ea-oper', False, is_config=False),
            _MetaInfoClassMember('echo-request-retry-count', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('0', '4294967295')], [],
                '''                Echo-Request retry count
                ''',
                'echo_request_retry_count',
                'Cisco-IOS-XR-ppp-ea-oper', False, is_config=False),
            _MetaInfoClassMember('is-multilink-bundle', ATTRIBUTE, 'bool', 'boolean',
                None, None,
                [], [],
                '''                TRUE if this is a Multilink bundle interface
                ''',
                'is_multilink_bundle',
                'Cisco-IOS-XR-ppp-ea-oper', False, is_config=False),
            _MetaInfoClassMember('synchronized', ATTRIBUTE, 'bool', 'boolean',
                None, None,
                [], [],
                '''                MA synchronization
                ''',
                'synchronized',
                'Cisco-IOS-XR-ppp-ea-oper', False, is_config=False),
            _MetaInfoClassMember('forwarding-enabled', ATTRIBUTE, 'bool', 'boolean',
                None, None,
                [], [],
                '''                Forwarding State
                ''',
                'forwarding_enabled',
                'Cisco-IOS-XR-ppp-ea-oper', False, is_config=False),
            _MetaInfoClassMember('multilink-interface', ATTRIBUTE, 'str', 'xr:Interface-name',
                None, None,
                [], [b'[a-zA-Z0-9._/-]+'],
                '''                Multilink interface that this interface is a
                member of, if any
                ''',
                'multilink_interface',
                'Cisco-IOS-XR-ppp-ea-oper', False, is_config=False),
            _MetaInfoClassMember('l2-tunnel-enabled', ATTRIBUTE, 'bool', 'boolean',
                None, None,
                [], [],
                '''                L2 Tunnel State
                ''',
                'l2_tunnel_enabled',
                'Cisco-IOS-XR-ppp-ea-oper', False, is_config=False),
            _MetaInfoClassMember('l2-provisioned', ATTRIBUTE, 'bool', 'boolean',
                None, None,
                [], [],
                '''                L2 Provisioned State
                ''',
                'l2_provisioned',
                'Cisco-IOS-XR-ppp-ea-oper', False, is_config=False),
            _MetaInfoClassMember('l2ip-interworking-enabled', ATTRIBUTE, 'bool', 'boolean',
                None, None,
                [], [],
                '''                L2 IP Interworking State
                ''',
                'l2ip_interworking_enabled',
                'Cisco-IOS-XR-ppp-ea-oper', False, is_config=False),
            _MetaInfoClassMember('is-vpdn-tunneled', ATTRIBUTE, 'bool', 'boolean',
                None, None,
                [], [],
                '''                Is VPDN tunneled
                ''',
                'is_vpdn_tunneled',
                'Cisco-IOS-XR-ppp-ea-oper', False, is_config=False),
            _MetaInfoClassMember('xconnect-id', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('0', '4294967295')], [],
                '''                XConnect ID
                ''',
                'xconnect_id',
                'Cisco-IOS-XR-ppp-ea-oper', False, is_config=False),
            _MetaInfoClassMember('parent-interface-handle', ATTRIBUTE, 'str', 'xr:Interface-name',
                None, None,
                [], [b'[a-zA-Z0-9._/-]+'],
                '''                Parent Interface Handle
                ''',
                'parent_interface_handle',
                'Cisco-IOS-XR-ppp-ea-oper', False, is_config=False),
            _MetaInfoClassMember('vrf-table-id', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('0', '4294967295')], [],
                '''                IPCP VRF Table ID
                ''',
                'vrf_table_id',
                'Cisco-IOS-XR-ppp-ea-oper', False, is_config=False),
            _MetaInfoClassMember('ipv6vrf-table-id', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('0', '4294967295')], [],
                '''                IPv6CP VRF Table ID
                ''',
                'ipv6vrf_table_id',
                'Cisco-IOS-XR-ppp-ea-oper', False, is_config=False),
            _MetaInfoClassMember('l2-adjacency-state', REFERENCE_ENUM_CLASS, 'PppEaAdjState', 'Ppp-ea-adj-state',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ppp_ea_oper', 'PppEaAdjState',
                [], [],
                '''                L2 adjacency state
                ''',
                'l2_adjacency_state',
                'Cisco-IOS-XR-ppp-ea-oper', False, is_config=False),
            _MetaInfoClassMember('l2ip-interworking-adjacency-state', REFERENCE_ENUM_CLASS, 'PppEaAdjState', 'Ppp-ea-adj-state',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ppp_ea_oper', 'PppEaAdjState',
                [], [],
                '''                L2 IP Interworking adjacency state
                ''',
                'l2ip_interworking_adjacency_state',
                'Cisco-IOS-XR-ppp-ea-oper', False, is_config=False),
            _MetaInfoClassMember('lac-adjacency-state', REFERENCE_ENUM_CLASS, 'PppEaAdjState', 'Ppp-ea-adj-state',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ppp_ea_oper', 'PppEaAdjState',
                [], [],
                '''                LAC adjacency state
                ''',
                'lac_adjacency_state',
                'Cisco-IOS-XR-ppp-ea-oper', False, is_config=False),
            _MetaInfoClassMember('interface-adjacency-state', REFERENCE_ENUM_CLASS, 'PppEaAdjState', 'Ppp-ea-adj-state',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ppp_ea_oper', 'PppEaAdjState',
                [], [],
                '''                Interface adjacency state
                ''',
                'interface_adjacency_state',
                'Cisco-IOS-XR-ppp-ea-oper', False, is_config=False),
            _MetaInfoClassMember('ipv4-adjacency-state', REFERENCE_ENUM_CLASS, 'PppEaAdjState', 'Ppp-ea-adj-state',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ppp_ea_oper', 'PppEaAdjState',
                [], [],
                '''                Ipv4 adjacency state
                ''',
                'ipv4_adjacency_state',
                'Cisco-IOS-XR-ppp-ea-oper', False, is_config=False),
            _MetaInfoClassMember('ipv6-adjacency-state', REFERENCE_ENUM_CLASS, 'PppEaAdjState', 'Ppp-ea-adj-state',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ppp_ea_oper', 'PppEaAdjState',
                [], [],
                '''                IPv6 adjacency state
                ''',
                'ipv6_adjacency_state',
                'Cisco-IOS-XR-ppp-ea-oper', False, is_config=False),
            _MetaInfoClassMember('mpls-adjacency-state', REFERENCE_ENUM_CLASS, 'PppEaAdjState', 'Ppp-ea-adj-state',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ppp_ea_oper', 'PppEaAdjState',
                [], [],
                '''                MPLS adjacency state
                ''',
                'mpls_adjacency_state',
                'Cisco-IOS-XR-ppp-ea-oper', False, is_config=False),
            ],
            'Cisco-IOS-XR-ppp-ea-oper',
            'ea-interface-name',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-ppp-ea-oper'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ppp_ea_oper',
            is_config=False,
        ),
    },
    'Pppea.Nodes.Node.EaInterfaceNames' : {
        'meta_info' : _MetaInfoClass('Pppea.Nodes.Node.EaInterfaceNames', REFERENCE_CLASS,
            '''Show interface related information from the
PPP EA''',
            False, 
            [
            _MetaInfoClassMember('ea-interface-name', REFERENCE_LIST, 'EaInterfaceName', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ppp_ea_oper', 'Pppea.Nodes.Node.EaInterfaceNames.EaInterfaceName',
                [], [],
                '''                Interface name
                ''',
                'ea_interface_name',
                'Cisco-IOS-XR-ppp-ea-oper', False, is_config=False),
            ],
            'Cisco-IOS-XR-ppp-ea-oper',
            'ea-interface-names',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-ppp-ea-oper'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ppp_ea_oper',
            is_config=False,
        ),
    },
    'Pppea.Nodes.Node' : {
        'meta_info' : _MetaInfoClass('Pppea.Nodes.Node', REFERENCE_LIST,
            '''The PPPEA operational data for a particular
node''',
            False, 
            [
            _MetaInfoClassMember('node-name', ATTRIBUTE, 'str', 'xr:Node-id',
                None, None,
                [], [b'([a-zA-Z0-9_]*\\d+/){1,2}([a-zA-Z0-9_]*\\d+)'],
                '''                The identifier for the node
                ''',
                'node_name',
                'Cisco-IOS-XR-ppp-ea-oper', True, is_config=False),
            _MetaInfoClassMember('ea-interface-names', REFERENCE_CLASS, 'EaInterfaceNames', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ppp_ea_oper', 'Pppea.Nodes.Node.EaInterfaceNames',
                [], [],
                '''                Show interface related information from the
                PPP EA
                ''',
                'ea_interface_names',
                'Cisco-IOS-XR-ppp-ea-oper', False, is_config=False),
            ],
            'Cisco-IOS-XR-ppp-ea-oper',
            'node',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-ppp-ea-oper'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ppp_ea_oper',
            is_config=False,
        ),
    },
    'Pppea.Nodes' : {
        'meta_info' : _MetaInfoClass('Pppea.Nodes', REFERENCE_CLASS,
            '''Per node PPPEA operational data''',
            False, 
            [
            _MetaInfoClassMember('node', REFERENCE_LIST, 'Node', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ppp_ea_oper', 'Pppea.Nodes.Node',
                [], [],
                '''                The PPPEA operational data for a particular
                node
                ''',
                'node',
                'Cisco-IOS-XR-ppp-ea-oper', False, is_config=False),
            ],
            'Cisco-IOS-XR-ppp-ea-oper',
            'nodes',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-ppp-ea-oper'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ppp_ea_oper',
            is_config=False,
        ),
    },
    'Pppea' : {
        'meta_info' : _MetaInfoClass('Pppea', REFERENCE_CLASS,
            '''PPPEA operational data''',
            False, 
            [
            _MetaInfoClassMember('nodes', REFERENCE_CLASS, 'Nodes', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ppp_ea_oper', 'Pppea.Nodes',
                [], [],
                '''                Per node PPPEA operational data
                ''',
                'nodes',
                'Cisco-IOS-XR-ppp-ea-oper', False, is_config=False),
            ],
            'Cisco-IOS-XR-ppp-ea-oper',
            'pppea',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-ppp-ea-oper'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ppp_ea_oper',
            is_config=False,
        ),
    },
}
_meta_table['Pppea.Nodes.Node.EaInterfaceNames.EaInterfaceName']['meta_info'].parent =_meta_table['Pppea.Nodes.Node.EaInterfaceNames']['meta_info']
_meta_table['Pppea.Nodes.Node.EaInterfaceNames']['meta_info'].parent =_meta_table['Pppea.Nodes.Node']['meta_info']
_meta_table['Pppea.Nodes.Node']['meta_info'].parent =_meta_table['Pppea.Nodes']['meta_info']
_meta_table['Pppea.Nodes']['meta_info'].parent =_meta_table['Pppea']['meta_info']
