
'''
This is auto-generated file,
which includes metadata for module Cisco_IOS_XR_lmp_cfg
'''

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_LIST, REFERENCE_LEAFLIST, REFERENCE_BITS, REFERENCE_UNION
from ydk._core._dm_meta_info import REFERENCE_CLASS, REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, ANYXML_CLASS
from ydk._core._importer import _yang_ns

_meta_table = {
    'OlmAddr' : _MetaInfoEnum('OlmAddr',
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lmp_cfg', 'OlmAddr',
        '''Olm addr''',
        {
            'ipv4':'ipv4',
            'ipv6':'ipv6',
            'unnumbered':'unnumbered',
            'nsap':'nsap',
        }, 'Cisco-IOS-XR-lmp-cfg', _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-lmp-cfg']),
    'OlmSwitchingCap' : _MetaInfoEnum('OlmSwitchingCap',
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lmp_cfg', 'OlmSwitchingCap',
        '''Olm switching cap''',
        {
            'lsc':'lsc',
            'fsc':'fsc',
        }, 'Cisco-IOS-XR-lmp-cfg', _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-lmp-cfg']),
    'Lmp.GmplsUni.Neighbors.Neighbor.Ipcc.Routed' : {
        'meta_info' : _MetaInfoClass('Lmp.GmplsUni.Neighbors.Neighbor.Ipcc.Routed', REFERENCE_CLASS,
            '''Routed IPCC configuration''',
            False, 
            [
            _MetaInfoClassMember('enable', ATTRIBUTE, 'Empty', 'empty',
                None, None,
                [], [],
                '''                Routed IPCC creation
                ''',
                'enable',
                'Cisco-IOS-XR-lmp-cfg', False),
            ],
            'Cisco-IOS-XR-lmp-cfg',
            'routed',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-lmp-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lmp_cfg',
        ),
    },
    'Lmp.GmplsUni.Neighbors.Neighbor.Ipcc' : {
        'meta_info' : _MetaInfoClass('Lmp.GmplsUni.Neighbors.Neighbor.Ipcc', REFERENCE_CLASS,
            '''IPCC configuration''',
            False, 
            [
            _MetaInfoClassMember('routed', REFERENCE_CLASS, 'Routed', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lmp_cfg', 'Lmp.GmplsUni.Neighbors.Neighbor.Ipcc.Routed',
                [], [],
                '''                Routed IPCC configuration
                ''',
                'routed',
                'Cisco-IOS-XR-lmp-cfg', False),
            ],
            'Cisco-IOS-XR-lmp-cfg',
            'ipcc',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-lmp-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lmp_cfg',
        ),
    },
    'Lmp.GmplsUni.Neighbors.Neighbor' : {
        'meta_info' : _MetaInfoClass('Lmp.GmplsUni.Neighbors.Neighbor', REFERENCE_LIST,
            '''Neighbor configuration''',
            False, 
            [
            _MetaInfoClassMember('neighbor-name', ATTRIBUTE, 'str', 'xr:Cisco-ios-xr-string',
                None, None,
                [(1, 64)], [],
                '''                Neighbor name
                ''',
                'neighbor_name',
                'Cisco-IOS-XR-lmp-cfg', True),
            _MetaInfoClassMember('ipcc', REFERENCE_CLASS, 'Ipcc', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lmp_cfg', 'Lmp.GmplsUni.Neighbors.Neighbor.Ipcc',
                [], [],
                '''                IPCC configuration
                ''',
                'ipcc',
                'Cisco-IOS-XR-lmp-cfg', False),
            _MetaInfoClassMember('enable', ATTRIBUTE, 'Empty', 'empty',
                None, None,
                [], [],
                '''                Neighbor creation
                ''',
                'enable',
                'Cisco-IOS-XR-lmp-cfg', False),
            _MetaInfoClassMember('neighbor-router-id', ATTRIBUTE, 'str', 'inet:ipv4-address-no-zone',
                None, None,
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'],
                '''                Neighbor router ID (IPv4 Address)
                ''',
                'neighbor_router_id',
                'Cisco-IOS-XR-lmp-cfg', False),
            ],
            'Cisco-IOS-XR-lmp-cfg',
            'neighbor',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-lmp-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lmp_cfg',
        ),
    },
    'Lmp.GmplsUni.Neighbors' : {
        'meta_info' : _MetaInfoClass('Lmp.GmplsUni.Neighbors', REFERENCE_CLASS,
            '''Neighbor configuration''',
            False, 
            [
            _MetaInfoClassMember('neighbor', REFERENCE_LIST, 'Neighbor', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lmp_cfg', 'Lmp.GmplsUni.Neighbors.Neighbor',
                [], [],
                '''                Neighbor configuration
                ''',
                'neighbor',
                'Cisco-IOS-XR-lmp-cfg', False),
            ],
            'Cisco-IOS-XR-lmp-cfg',
            'neighbors',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-lmp-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lmp_cfg',
        ),
    },
    'Lmp.GmplsUni.RouterId' : {
        'meta_info' : _MetaInfoClass('Lmp.GmplsUni.RouterId', REFERENCE_CLASS,
            '''Local GMPLS UNI router ID''',
            False, 
            [
            _MetaInfoClassMember('interface-name', ATTRIBUTE, 'str', 'xr:Interface-name',
                None, None,
                [], [b'[a-zA-Z0-9._/-]+'],
                '''                Name of interface
                ''',
                'interface_name',
                'Cisco-IOS-XR-lmp-cfg', False),
            _MetaInfoClassMember('address', ATTRIBUTE, 'str', 'inet:ipv4-address-no-zone',
                None, None,
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'],
                '''                Local router ID (IPv4 Address)
                ''',
                'address',
                'Cisco-IOS-XR-lmp-cfg', False),
            ],
            'Cisco-IOS-XR-lmp-cfg',
            'router-id',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-lmp-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lmp_cfg',
            is_presence=True,
        ),
    },
    'Lmp.GmplsUni.Controllers.Controller.LocalLinkId' : {
        'meta_info' : _MetaInfoClass('Lmp.GmplsUni.Controllers.Controller.LocalLinkId', REFERENCE_CLASS,
            '''Local Link ID configuration''',
            False, 
            [
            _MetaInfoClassMember('address-type', REFERENCE_ENUM_CLASS, 'OlmAddr', 'Olm-addr',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lmp_cfg', 'OlmAddr',
                [], [],
                '''                Local link ID address type
                ''',
                'address_type',
                'Cisco-IOS-XR-lmp-cfg', False),
            _MetaInfoClassMember('unnumbered', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('0', '4294967295')], [],
                '''                Local address unnumbered 
                ''',
                'unnumbered',
                'Cisco-IOS-XR-lmp-cfg', False, has_when=True),
            _MetaInfoClassMember('address', ATTRIBUTE, 'str', 'inet:ipv4-address-no-zone',
                None, None,
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'],
                '''                Local link ID address IPv4
                ''',
                'address',
                'Cisco-IOS-XR-lmp-cfg', False, has_when=True),
            ],
            'Cisco-IOS-XR-lmp-cfg',
            'local-link-id',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-lmp-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lmp_cfg',
        ),
    },
    'Lmp.GmplsUni.Controllers.Controller.Adjacency.RemoteNeighbor.InterfaceId' : {
        'meta_info' : _MetaInfoClass('Lmp.GmplsUni.Controllers.Controller.Adjacency.RemoteNeighbor.InterfaceId', REFERENCE_CLASS,
            '''Neighbor Interface ID configuration''',
            False, 
            [
            _MetaInfoClassMember('address-type', REFERENCE_ENUM_CLASS, 'OlmAddr', 'Olm-addr',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lmp_cfg', 'OlmAddr',
                [], [],
                '''                Local link ID address type
                ''',
                'address_type',
                'Cisco-IOS-XR-lmp-cfg', False),
            _MetaInfoClassMember('unnumbered', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('0', '4294967295')], [],
                '''                Local address unnumbered 
                ''',
                'unnumbered',
                'Cisco-IOS-XR-lmp-cfg', False, has_when=True),
            _MetaInfoClassMember('address', ATTRIBUTE, 'str', 'inet:ipv4-address-no-zone',
                None, None,
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'],
                '''                Local link ID address IPv4
                ''',
                'address',
                'Cisco-IOS-XR-lmp-cfg', False, has_when=True),
            ],
            'Cisco-IOS-XR-lmp-cfg',
            'interface-id',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-lmp-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lmp_cfg',
        ),
    },
    'Lmp.GmplsUni.Controllers.Controller.Adjacency.RemoteNeighbor.LinkId' : {
        'meta_info' : _MetaInfoClass('Lmp.GmplsUni.Controllers.Controller.Adjacency.RemoteNeighbor.LinkId', REFERENCE_CLASS,
            '''Neighbor Link ID configuration''',
            False, 
            [
            _MetaInfoClassMember('address-type', REFERENCE_ENUM_CLASS, 'OlmAddr', 'Olm-addr',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lmp_cfg', 'OlmAddr',
                [], [],
                '''                Neighbor link ID address type
                ''',
                'address_type',
                'Cisco-IOS-XR-lmp-cfg', False),
            _MetaInfoClassMember('unnumbered', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('0', '4294967295')], [],
                '''                Neighbor address unnumbered [Not
                supported]
                ''',
                'unnumbered',
                'Cisco-IOS-XR-lmp-cfg', False, has_when=True),
            _MetaInfoClassMember('address', ATTRIBUTE, 'str', 'inet:ipv4-address-no-zone',
                None, None,
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'],
                '''                Neighbor ID address IPv4
                ''',
                'address',
                'Cisco-IOS-XR-lmp-cfg', False, has_when=True),
            ],
            'Cisco-IOS-XR-lmp-cfg',
            'link-id',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-lmp-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lmp_cfg',
        ),
    },
    'Lmp.GmplsUni.Controllers.Controller.Adjacency.RemoteNeighbor' : {
        'meta_info' : _MetaInfoClass('Lmp.GmplsUni.Controllers.Controller.Adjacency.RemoteNeighbor', REFERENCE_CLASS,
            '''Neighbor data''',
            False, 
            [
            _MetaInfoClassMember('interface-id', REFERENCE_CLASS, 'InterfaceId', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lmp_cfg', 'Lmp.GmplsUni.Controllers.Controller.Adjacency.RemoteNeighbor.InterfaceId',
                [], [],
                '''                Neighbor Interface ID configuration
                ''',
                'interface_id',
                'Cisco-IOS-XR-lmp-cfg', False),
            _MetaInfoClassMember('link-id', REFERENCE_CLASS, 'LinkId', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lmp_cfg', 'Lmp.GmplsUni.Controllers.Controller.Adjacency.RemoteNeighbor.LinkId',
                [], [],
                '''                Neighbor Link ID configuration
                ''',
                'link_id',
                'Cisco-IOS-XR-lmp-cfg', False),
            _MetaInfoClassMember('neighbor-association', ATTRIBUTE, 'str', 'xr:Cisco-ios-xr-string',
                None, None,
                [(1, 64)], [],
                '''                Create LMP controller to neighbor
                association
                ''',
                'neighbor_association',
                'Cisco-IOS-XR-lmp-cfg', False),
            _MetaInfoClassMember('link-switching-capability', REFERENCE_ENUM_CLASS, 'OlmSwitchingCap', 'Olm-switching-cap',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lmp_cfg', 'OlmSwitchingCap',
                [], [],
                '''                Neighbor link switching capability
                configuration
                ''',
                'link_switching_capability',
                'Cisco-IOS-XR-lmp-cfg', False, default_value='Cisco_IOS_XR_lmp_cfg.OlmSwitchingCap.lsc'),
            _MetaInfoClassMember('flexi-grid-capable', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('0', '4294967295')], [],
                '''                Remote node flexi grid capability 
                ''',
                'flexi_grid_capable',
                'Cisco-IOS-XR-lmp-cfg', False),
            ],
            'Cisco-IOS-XR-lmp-cfg',
            'remote-neighbor',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-lmp-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lmp_cfg',
        ),
    },
    'Lmp.GmplsUni.Controllers.Controller.Adjacency' : {
        'meta_info' : _MetaInfoClass('Lmp.GmplsUni.Controllers.Controller.Adjacency', REFERENCE_CLASS,
            '''Neighbor controller adjacency configuration''',
            False, 
            [
            _MetaInfoClassMember('remote-neighbor', REFERENCE_CLASS, 'RemoteNeighbor', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lmp_cfg', 'Lmp.GmplsUni.Controllers.Controller.Adjacency.RemoteNeighbor',
                [], [],
                '''                Neighbor data
                ''',
                'remote_neighbor',
                'Cisco-IOS-XR-lmp-cfg', False),
            ],
            'Cisco-IOS-XR-lmp-cfg',
            'adjacency',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-lmp-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lmp_cfg',
        ),
    },
    'Lmp.GmplsUni.Controllers.Controller' : {
        'meta_info' : _MetaInfoClass('Lmp.GmplsUni.Controllers.Controller', REFERENCE_LIST,
            '''Configure an GMPLS UNI OLM/LMP contoller''',
            False, 
            [
            _MetaInfoClassMember('controller-name', ATTRIBUTE, 'str', 'xr:Interface-name',
                None, None,
                [], [b'[a-zA-Z0-9._/-]+'],
                '''                Controller name
                ''',
                'controller_name',
                'Cisco-IOS-XR-lmp-cfg', True),
            _MetaInfoClassMember('local-link-id', REFERENCE_CLASS, 'LocalLinkId', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lmp_cfg', 'Lmp.GmplsUni.Controllers.Controller.LocalLinkId',
                [], [],
                '''                Local Link ID configuration
                ''',
                'local_link_id',
                'Cisco-IOS-XR-lmp-cfg', False),
            _MetaInfoClassMember('adjacency', REFERENCE_CLASS, 'Adjacency', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lmp_cfg', 'Lmp.GmplsUni.Controllers.Controller.Adjacency',
                [], [],
                '''                Neighbor controller adjacency configuration
                ''',
                'adjacency',
                'Cisco-IOS-XR-lmp-cfg', False),
            _MetaInfoClassMember('enable', ATTRIBUTE, 'Empty', 'empty',
                None, None,
                [], [],
                '''                Enable the OLM/LMP application on this
                controller
                ''',
                'enable',
                'Cisco-IOS-XR-lmp-cfg', False),
            ],
            'Cisco-IOS-XR-lmp-cfg',
            'controller',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-lmp-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lmp_cfg',
        ),
    },
    'Lmp.GmplsUni.Controllers' : {
        'meta_info' : _MetaInfoClass('Lmp.GmplsUni.Controllers', REFERENCE_CLASS,
            '''Configure GMPLS UNI OLM/LMP controllers''',
            False, 
            [
            _MetaInfoClassMember('controller', REFERENCE_LIST, 'Controller', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lmp_cfg', 'Lmp.GmplsUni.Controllers.Controller',
                [], [],
                '''                Configure an GMPLS UNI OLM/LMP contoller
                ''',
                'controller',
                'Cisco-IOS-XR-lmp-cfg', False),
            ],
            'Cisco-IOS-XR-lmp-cfg',
            'controllers',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-lmp-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lmp_cfg',
        ),
    },
    'Lmp.GmplsUni' : {
        'meta_info' : _MetaInfoClass('Lmp.GmplsUni', REFERENCE_CLASS,
            '''GMPLS UNI specific OLM/LMP configuration''',
            False, 
            [
            _MetaInfoClassMember('neighbors', REFERENCE_CLASS, 'Neighbors', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lmp_cfg', 'Lmp.GmplsUni.Neighbors',
                [], [],
                '''                Neighbor configuration
                ''',
                'neighbors',
                'Cisco-IOS-XR-lmp-cfg', False),
            _MetaInfoClassMember('router-id', REFERENCE_CLASS, 'RouterId', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lmp_cfg', 'Lmp.GmplsUni.RouterId',
                [], [],
                '''                Local GMPLS UNI router ID
                ''',
                'router_id',
                'Cisco-IOS-XR-lmp-cfg', False, is_presence=True),
            _MetaInfoClassMember('controllers', REFERENCE_CLASS, 'Controllers', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lmp_cfg', 'Lmp.GmplsUni.Controllers',
                [], [],
                '''                Configure GMPLS UNI OLM/LMP controllers
                ''',
                'controllers',
                'Cisco-IOS-XR-lmp-cfg', False),
            ],
            'Cisco-IOS-XR-lmp-cfg',
            'gmpls-uni',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-lmp-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lmp_cfg',
        ),
    },
    'Lmp' : {
        'meta_info' : _MetaInfoClass('Lmp', REFERENCE_CLASS,
            '''Main common OLM/LMP configuration container''',
            False, 
            [
            _MetaInfoClassMember('gmpls-uni', REFERENCE_CLASS, 'GmplsUni', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lmp_cfg', 'Lmp.GmplsUni',
                [], [],
                '''                GMPLS UNI specific OLM/LMP configuration
                ''',
                'gmpls_uni',
                'Cisco-IOS-XR-lmp-cfg', False),
            _MetaInfoClassMember('enable', ATTRIBUTE, 'Empty', 'empty',
                None, None,
                [], [],
                '''                Enable the OLM/LMP application
                ''',
                'enable',
                'Cisco-IOS-XR-lmp-cfg', False),
            ],
            'Cisco-IOS-XR-lmp-cfg',
            'lmp',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-lmp-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lmp_cfg',
        ),
    },
}
_meta_table['Lmp.GmplsUni.Neighbors.Neighbor.Ipcc.Routed']['meta_info'].parent =_meta_table['Lmp.GmplsUni.Neighbors.Neighbor.Ipcc']['meta_info']
_meta_table['Lmp.GmplsUni.Neighbors.Neighbor.Ipcc']['meta_info'].parent =_meta_table['Lmp.GmplsUni.Neighbors.Neighbor']['meta_info']
_meta_table['Lmp.GmplsUni.Neighbors.Neighbor']['meta_info'].parent =_meta_table['Lmp.GmplsUni.Neighbors']['meta_info']
_meta_table['Lmp.GmplsUni.Controllers.Controller.Adjacency.RemoteNeighbor.InterfaceId']['meta_info'].parent =_meta_table['Lmp.GmplsUni.Controllers.Controller.Adjacency.RemoteNeighbor']['meta_info']
_meta_table['Lmp.GmplsUni.Controllers.Controller.Adjacency.RemoteNeighbor.LinkId']['meta_info'].parent =_meta_table['Lmp.GmplsUni.Controllers.Controller.Adjacency.RemoteNeighbor']['meta_info']
_meta_table['Lmp.GmplsUni.Controllers.Controller.Adjacency.RemoteNeighbor']['meta_info'].parent =_meta_table['Lmp.GmplsUni.Controllers.Controller.Adjacency']['meta_info']
_meta_table['Lmp.GmplsUni.Controllers.Controller.LocalLinkId']['meta_info'].parent =_meta_table['Lmp.GmplsUni.Controllers.Controller']['meta_info']
_meta_table['Lmp.GmplsUni.Controllers.Controller.Adjacency']['meta_info'].parent =_meta_table['Lmp.GmplsUni.Controllers.Controller']['meta_info']
_meta_table['Lmp.GmplsUni.Controllers.Controller']['meta_info'].parent =_meta_table['Lmp.GmplsUni.Controllers']['meta_info']
_meta_table['Lmp.GmplsUni.Neighbors']['meta_info'].parent =_meta_table['Lmp.GmplsUni']['meta_info']
_meta_table['Lmp.GmplsUni.RouterId']['meta_info'].parent =_meta_table['Lmp.GmplsUni']['meta_info']
_meta_table['Lmp.GmplsUni.Controllers']['meta_info'].parent =_meta_table['Lmp.GmplsUni']['meta_info']
_meta_table['Lmp.GmplsUni']['meta_info'].parent =_meta_table['Lmp']['meta_info']
