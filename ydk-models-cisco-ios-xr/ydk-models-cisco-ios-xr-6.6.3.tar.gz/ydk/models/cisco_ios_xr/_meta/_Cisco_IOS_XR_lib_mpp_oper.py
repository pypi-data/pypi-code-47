
'''
This is auto-generated file,
which includes metadata for module Cisco_IOS_XR_lib_mpp_oper
'''

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_LIST, REFERENCE_LEAFLIST, REFERENCE_BITS, REFERENCE_UNION
from ydk._core._dm_meta_info import REFERENCE_CLASS, REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, ANYXML_CLASS
from ydk._core._importer import _yang_ns

_meta_table = {
    'MppAllow' : _MetaInfoEnum('MppAllow',
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_oper', 'MppAllow',
        '''MPP protocol types''',
        {
            'ssh':'ssh',
            'telnet':'telnet',
            'snmp':'snmp',
            'tftp':'tftp',
            'http':'http',
            'xr-xml':'xr_xml',
            'netconf':'netconf',
            'all':'all',
        }, 'Cisco-IOS-XR-lib-mpp-oper', _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-lib-mpp-oper']),
    'MppAfIdBase' : {
        'meta_info' : _MetaInfoClass('MppAfIdBase', REFERENCE_IDENTITY_CLASS,
            '''Base identity for Mpp-af-id''',
            False, 
            [
            ],
            'Cisco-IOS-XR-lib-mpp-oper',
            'Mpp-af-id-base',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-lib-mpp-oper'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_oper',
        ),
    },
    'ManagementPlaneProtection.Outband.Vrf' : {
        'meta_info' : _MetaInfoClass('ManagementPlaneProtection.Outband.Vrf', REFERENCE_CLASS,
            '''Outband VRF information''',
            False, 
            [
            _MetaInfoClassMember('vrf-name', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                Outband VRF name
                ''',
                'vrf_name',
                'Cisco-IOS-XR-lib-mpp-oper', False, is_config=False),
            ],
            'Cisco-IOS-XR-lib-mpp-oper',
            'vrf',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-lib-mpp-oper'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_oper',
            is_config=False,
        ),
    },
    'ManagementPlaneProtection.Outband.Interfaces.Interface.Protocol.PeerAddress' : {
        'meta_info' : _MetaInfoClass('ManagementPlaneProtection.Outband.Interfaces.Interface.Protocol.PeerAddress', REFERENCE_LIST,
            '''List of peer addresses''',
            False, 
            [
            _MetaInfoClassMember('af-name', REFERENCE_IDENTITY_CLASS, 'MppAfIdBase', 'Mpp-af-id',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_oper', 'MppAfIdBase',
                [], [],
                '''                AFName
                ''',
                'af_name',
                'Cisco-IOS-XR-lib-mpp-oper', False, is_config=False),
            _MetaInfoClassMember('ipv4-address', ATTRIBUTE, 'str', 'Mpp-in-addr',
                None, None,
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'],
                '''                IPv4 address
                ''',
                'ipv4_address',
                'Cisco-IOS-XR-lib-mpp-oper', False, is_config=False, has_when=True),
            _MetaInfoClassMember('ipv6-address', ATTRIBUTE, 'str', 'Mpp-in6-addr',
                None, None,
                [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'],
                '''                IPv6 address
                ''',
                'ipv6_address',
                'Cisco-IOS-XR-lib-mpp-oper', False, is_config=False, has_when=True),
            ],
            'Cisco-IOS-XR-lib-mpp-oper',
            'peer-address',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-lib-mpp-oper'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_oper',
            is_config=False,
        ),
    },
    'ManagementPlaneProtection.Outband.Interfaces.Interface.Protocol' : {
        'meta_info' : _MetaInfoClass('ManagementPlaneProtection.Outband.Interfaces.Interface.Protocol', REFERENCE_LIST,
            '''MPP Interface protocols''',
            False, 
            [
            _MetaInfoClassMember('allow', REFERENCE_ENUM_CLASS, 'MppAllow', 'Mpp-allow',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_oper', 'MppAllow',
                [], [],
                '''                MPP allow
                ''',
                'allow',
                'Cisco-IOS-XR-lib-mpp-oper', False, is_config=False),
            _MetaInfoClassMember('is-all-peers-allowed', ATTRIBUTE, 'bool', 'boolean',
                None, None,
                [], [],
                '''                If TRUE, all peers are allowed
                ''',
                'is_all_peers_allowed',
                'Cisco-IOS-XR-lib-mpp-oper', False, is_config=False),
            _MetaInfoClassMember('peer-address', REFERENCE_LIST, 'PeerAddress', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_oper', 'ManagementPlaneProtection.Outband.Interfaces.Interface.Protocol.PeerAddress',
                [], [],
                '''                List of peer addresses
                ''',
                'peer_address',
                'Cisco-IOS-XR-lib-mpp-oper', False, is_config=False),
            ],
            'Cisco-IOS-XR-lib-mpp-oper',
            'protocol',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-lib-mpp-oper'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_oper',
            is_config=False,
        ),
    },
    'ManagementPlaneProtection.Outband.Interfaces.Interface' : {
        'meta_info' : _MetaInfoClass('ManagementPlaneProtection.Outband.Interfaces.Interface', REFERENCE_LIST,
            '''MPP interface information''',
            False, 
            [
            _MetaInfoClassMember('interface-name', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                Interface name, specify 'all' for all
                interfaces
                ''',
                'interface_name',
                'Cisco-IOS-XR-lib-mpp-oper', True, is_config=False),
            _MetaInfoClassMember('protocol', REFERENCE_LIST, 'Protocol', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_oper', 'ManagementPlaneProtection.Outband.Interfaces.Interface.Protocol',
                [], [],
                '''                MPP Interface protocols
                ''',
                'protocol',
                'Cisco-IOS-XR-lib-mpp-oper', False, is_config=False),
            ],
            'Cisco-IOS-XR-lib-mpp-oper',
            'interface',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-lib-mpp-oper'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_oper',
            is_config=False,
        ),
    },
    'ManagementPlaneProtection.Outband.Interfaces' : {
        'meta_info' : _MetaInfoClass('ManagementPlaneProtection.Outband.Interfaces', REFERENCE_CLASS,
            '''List of inband/outband interfaces''',
            False, 
            [
            _MetaInfoClassMember('interface', REFERENCE_LIST, 'Interface', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_oper', 'ManagementPlaneProtection.Outband.Interfaces.Interface',
                [], [],
                '''                MPP interface information
                ''',
                'interface',
                'Cisco-IOS-XR-lib-mpp-oper', False, is_config=False),
            ],
            'Cisco-IOS-XR-lib-mpp-oper',
            'interfaces',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-lib-mpp-oper'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_oper',
            is_config=False,
        ),
    },
    'ManagementPlaneProtection.Outband' : {
        'meta_info' : _MetaInfoClass('ManagementPlaneProtection.Outband', REFERENCE_CLASS,
            '''Management Plane Protection (MPP) outband
interface data''',
            False, 
            [
            _MetaInfoClassMember('vrf', REFERENCE_CLASS, 'Vrf', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_oper', 'ManagementPlaneProtection.Outband.Vrf',
                [], [],
                '''                Outband VRF information
                ''',
                'vrf',
                'Cisco-IOS-XR-lib-mpp-oper', False, is_config=False),
            _MetaInfoClassMember('interfaces', REFERENCE_CLASS, 'Interfaces', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_oper', 'ManagementPlaneProtection.Outband.Interfaces',
                [], [],
                '''                List of inband/outband interfaces
                ''',
                'interfaces',
                'Cisco-IOS-XR-lib-mpp-oper', False, is_config=False),
            ],
            'Cisco-IOS-XR-lib-mpp-oper',
            'outband',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-lib-mpp-oper'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_oper',
            is_config=False,
        ),
    },
    'ManagementPlaneProtection.Inband.Interfaces.Interface.Protocol.PeerAddress' : {
        'meta_info' : _MetaInfoClass('ManagementPlaneProtection.Inband.Interfaces.Interface.Protocol.PeerAddress', REFERENCE_LIST,
            '''List of peer addresses''',
            False, 
            [
            _MetaInfoClassMember('af-name', REFERENCE_IDENTITY_CLASS, 'MppAfIdBase', 'Mpp-af-id',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_oper', 'MppAfIdBase',
                [], [],
                '''                AFName
                ''',
                'af_name',
                'Cisco-IOS-XR-lib-mpp-oper', False, is_config=False),
            _MetaInfoClassMember('ipv4-address', ATTRIBUTE, 'str', 'Mpp-in-addr',
                None, None,
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'],
                '''                IPv4 address
                ''',
                'ipv4_address',
                'Cisco-IOS-XR-lib-mpp-oper', False, is_config=False, has_when=True),
            _MetaInfoClassMember('ipv6-address', ATTRIBUTE, 'str', 'Mpp-in6-addr',
                None, None,
                [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'],
                '''                IPv6 address
                ''',
                'ipv6_address',
                'Cisco-IOS-XR-lib-mpp-oper', False, is_config=False, has_when=True),
            ],
            'Cisco-IOS-XR-lib-mpp-oper',
            'peer-address',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-lib-mpp-oper'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_oper',
            is_config=False,
        ),
    },
    'ManagementPlaneProtection.Inband.Interfaces.Interface.Protocol' : {
        'meta_info' : _MetaInfoClass('ManagementPlaneProtection.Inband.Interfaces.Interface.Protocol', REFERENCE_LIST,
            '''MPP Interface protocols''',
            False, 
            [
            _MetaInfoClassMember('allow', REFERENCE_ENUM_CLASS, 'MppAllow', 'Mpp-allow',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_oper', 'MppAllow',
                [], [],
                '''                MPP allow
                ''',
                'allow',
                'Cisco-IOS-XR-lib-mpp-oper', False, is_config=False),
            _MetaInfoClassMember('is-all-peers-allowed', ATTRIBUTE, 'bool', 'boolean',
                None, None,
                [], [],
                '''                If TRUE, all peers are allowed
                ''',
                'is_all_peers_allowed',
                'Cisco-IOS-XR-lib-mpp-oper', False, is_config=False),
            _MetaInfoClassMember('peer-address', REFERENCE_LIST, 'PeerAddress', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_oper', 'ManagementPlaneProtection.Inband.Interfaces.Interface.Protocol.PeerAddress',
                [], [],
                '''                List of peer addresses
                ''',
                'peer_address',
                'Cisco-IOS-XR-lib-mpp-oper', False, is_config=False),
            ],
            'Cisco-IOS-XR-lib-mpp-oper',
            'protocol',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-lib-mpp-oper'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_oper',
            is_config=False,
        ),
    },
    'ManagementPlaneProtection.Inband.Interfaces.Interface' : {
        'meta_info' : _MetaInfoClass('ManagementPlaneProtection.Inband.Interfaces.Interface', REFERENCE_LIST,
            '''MPP interface information''',
            False, 
            [
            _MetaInfoClassMember('interface-name', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                Interface name, specify 'all' for all
                interfaces
                ''',
                'interface_name',
                'Cisco-IOS-XR-lib-mpp-oper', True, is_config=False),
            _MetaInfoClassMember('protocol', REFERENCE_LIST, 'Protocol', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_oper', 'ManagementPlaneProtection.Inband.Interfaces.Interface.Protocol',
                [], [],
                '''                MPP Interface protocols
                ''',
                'protocol',
                'Cisco-IOS-XR-lib-mpp-oper', False, is_config=False),
            ],
            'Cisco-IOS-XR-lib-mpp-oper',
            'interface',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-lib-mpp-oper'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_oper',
            is_config=False,
        ),
    },
    'ManagementPlaneProtection.Inband.Interfaces' : {
        'meta_info' : _MetaInfoClass('ManagementPlaneProtection.Inband.Interfaces', REFERENCE_CLASS,
            '''List of inband/outband interfaces''',
            False, 
            [
            _MetaInfoClassMember('interface', REFERENCE_LIST, 'Interface', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_oper', 'ManagementPlaneProtection.Inband.Interfaces.Interface',
                [], [],
                '''                MPP interface information
                ''',
                'interface',
                'Cisco-IOS-XR-lib-mpp-oper', False, is_config=False),
            ],
            'Cisco-IOS-XR-lib-mpp-oper',
            'interfaces',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-lib-mpp-oper'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_oper',
            is_config=False,
        ),
    },
    'ManagementPlaneProtection.Inband' : {
        'meta_info' : _MetaInfoClass('ManagementPlaneProtection.Inband', REFERENCE_CLASS,
            '''Management Plane Protection (MPP) inband
interface data''',
            False, 
            [
            _MetaInfoClassMember('interfaces', REFERENCE_CLASS, 'Interfaces', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_oper', 'ManagementPlaneProtection.Inband.Interfaces',
                [], [],
                '''                List of inband/outband interfaces
                ''',
                'interfaces',
                'Cisco-IOS-XR-lib-mpp-oper', False, is_config=False),
            ],
            'Cisco-IOS-XR-lib-mpp-oper',
            'inband',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-lib-mpp-oper'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_oper',
            is_config=False,
        ),
    },
    'ManagementPlaneProtection' : {
        'meta_info' : _MetaInfoClass('ManagementPlaneProtection', REFERENCE_CLASS,
            '''Management Plane Protection (MPP) operational
data''',
            False, 
            [
            _MetaInfoClassMember('outband', REFERENCE_CLASS, 'Outband', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_oper', 'ManagementPlaneProtection.Outband',
                [], [],
                '''                Management Plane Protection (MPP) outband
                interface data
                ''',
                'outband',
                'Cisco-IOS-XR-lib-mpp-oper', False, is_config=False),
            _MetaInfoClassMember('inband', REFERENCE_CLASS, 'Inband', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_oper', 'ManagementPlaneProtection.Inband',
                [], [],
                '''                Management Plane Protection (MPP) inband
                interface data
                ''',
                'inband',
                'Cisco-IOS-XR-lib-mpp-oper', False, is_config=False),
            ],
            'Cisco-IOS-XR-lib-mpp-oper',
            'management-plane-protection',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-lib-mpp-oper'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_oper',
            is_config=False,
        ),
    },
    'Ipv4' : {
        'meta_info' : _MetaInfoClass('Ipv4', REFERENCE_IDENTITY_CLASS,
            '''IPv4 address family''',
            False, 
            [
            ],
            'Cisco-IOS-XR-lib-mpp-oper',
            'ipv4',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-lib-mpp-oper'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_oper',
        ),
    },
    'Ipv6' : {
        'meta_info' : _MetaInfoClass('Ipv6', REFERENCE_IDENTITY_CLASS,
            '''IPv6 address family''',
            False, 
            [
            ],
            'Cisco-IOS-XR-lib-mpp-oper',
            'ipv6',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-lib-mpp-oper'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_oper',
        ),
    },
}
_meta_table['ManagementPlaneProtection.Outband.Interfaces.Interface.Protocol.PeerAddress']['meta_info'].parent =_meta_table['ManagementPlaneProtection.Outband.Interfaces.Interface.Protocol']['meta_info']
_meta_table['ManagementPlaneProtection.Outband.Interfaces.Interface.Protocol']['meta_info'].parent =_meta_table['ManagementPlaneProtection.Outband.Interfaces.Interface']['meta_info']
_meta_table['ManagementPlaneProtection.Outband.Interfaces.Interface']['meta_info'].parent =_meta_table['ManagementPlaneProtection.Outband.Interfaces']['meta_info']
_meta_table['ManagementPlaneProtection.Outband.Vrf']['meta_info'].parent =_meta_table['ManagementPlaneProtection.Outband']['meta_info']
_meta_table['ManagementPlaneProtection.Outband.Interfaces']['meta_info'].parent =_meta_table['ManagementPlaneProtection.Outband']['meta_info']
_meta_table['ManagementPlaneProtection.Inband.Interfaces.Interface.Protocol.PeerAddress']['meta_info'].parent =_meta_table['ManagementPlaneProtection.Inband.Interfaces.Interface.Protocol']['meta_info']
_meta_table['ManagementPlaneProtection.Inband.Interfaces.Interface.Protocol']['meta_info'].parent =_meta_table['ManagementPlaneProtection.Inband.Interfaces.Interface']['meta_info']
_meta_table['ManagementPlaneProtection.Inband.Interfaces.Interface']['meta_info'].parent =_meta_table['ManagementPlaneProtection.Inband.Interfaces']['meta_info']
_meta_table['ManagementPlaneProtection.Inband.Interfaces']['meta_info'].parent =_meta_table['ManagementPlaneProtection.Inband']['meta_info']
_meta_table['ManagementPlaneProtection.Outband']['meta_info'].parent =_meta_table['ManagementPlaneProtection']['meta_info']
_meta_table['ManagementPlaneProtection.Inband']['meta_info'].parent =_meta_table['ManagementPlaneProtection']['meta_info']
