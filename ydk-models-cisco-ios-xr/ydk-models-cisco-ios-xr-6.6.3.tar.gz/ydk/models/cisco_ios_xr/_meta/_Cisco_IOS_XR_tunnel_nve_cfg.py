
'''
This is auto-generated file,
which includes metadata for module Cisco_IOS_XR_tunnel_nve_cfg
'''

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_LIST, REFERENCE_LEAFLIST, REFERENCE_BITS, REFERENCE_UNION
from ydk._core._dm_meta_info import REFERENCE_CLASS, REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, ANYXML_CLASS
from ydk._core._importer import _yang_ns

_meta_table = {
    'HostReachProtocol' : _MetaInfoEnum('HostReachProtocol',
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_tunnel_nve_cfg', 'HostReachProtocol',
        '''Host reach protocol''',
        {
            'bgp':'bgp',
        }, 'Cisco-IOS-XR-tunnel-nve-cfg', _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-tunnel-nve-cfg']),
    'VxlanUdpPortEnum' : _MetaInfoEnum('VxlanUdpPortEnum',
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_tunnel_nve_cfg', 'VxlanUdpPortEnum',
        '''Vxlan udp port enum''',
        {
            'ietf-udp-port':'ietf_udp_port',
            'ivx-lan-udp-port':'ivx_lan_udp_port',
        }, 'Cisco-IOS-XR-tunnel-nve-cfg', _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-tunnel-nve-cfg']),
    'OverlayEncapEnum' : _MetaInfoEnum('OverlayEncapEnum',
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_tunnel_nve_cfg', 'OverlayEncapEnum',
        '''Overlay encap enum''',
        {
            'vx-lan-encapsulation':'vx_lan_encapsulation',
            'soft-gre-encapsulation':'soft_gre_encapsulation',
        }, 'Cisco-IOS-XR-tunnel-nve-cfg', _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-tunnel-nve-cfg']),
    'UnknownUnicastFloodingEnum' : _MetaInfoEnum('UnknownUnicastFloodingEnum',
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_tunnel_nve_cfg', 'UnknownUnicastFloodingEnum',
        '''Unknown unicast flooding enum''',
        {
            'suppress-uuf':'suppress_uuf',
        }, 'Cisco-IOS-XR-tunnel-nve-cfg', _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-tunnel-nve-cfg']),
    'LoadBalanceEnum' : _MetaInfoEnum('LoadBalanceEnum',
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_tunnel_nve_cfg', 'LoadBalanceEnum',
        '''Load balance enum''',
        {
            'per-evi':'per_evi',
        }, 'Cisco-IOS-XR-tunnel-nve-cfg', _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-tunnel-nve-cfg']),
    'IrProtocolEnum' : _MetaInfoEnum('IrProtocolEnum',
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_tunnel_nve_cfg', 'IrProtocolEnum',
        '''Ir protocol enum''',
        {
            'bgp':'bgp',
        }, 'Cisco-IOS-XR-tunnel-nve-cfg', _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-tunnel-nve-cfg']),
}
