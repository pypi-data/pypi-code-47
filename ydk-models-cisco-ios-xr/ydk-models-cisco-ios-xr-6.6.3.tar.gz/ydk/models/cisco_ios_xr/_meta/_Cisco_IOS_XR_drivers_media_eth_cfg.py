
'''
This is auto-generated file,
which includes metadata for module Cisco_IOS_XR_drivers_media_eth_cfg
'''

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_LIST, REFERENCE_LEAFLIST, REFERENCE_BITS, REFERENCE_UNION
from ydk._core._dm_meta_info import REFERENCE_CLASS, REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, ANYXML_CLASS
from ydk._core._importer import _yang_ns

_meta_table = {
    'EthernetAutoNegotiation' : _MetaInfoEnum('EthernetAutoNegotiation',
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_drivers_media_eth_cfg', 'EthernetAutoNegotiation',
        '''Ethernet auto negotiation''',
        {
            'true':'true',
            'override':'override',
        }, 'Cisco-IOS-XR-drivers-media-eth-cfg', _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-drivers-media-eth-cfg']),
    'EthernetFec' : _MetaInfoEnum('EthernetFec',
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_drivers_media_eth_cfg', 'EthernetFec',
        '''Ethernet fec''',
        {
            'none':'none',
            'standard':'standard',
        }, 'Cisco-IOS-XR-drivers-media-eth-cfg', _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-drivers-media-eth-cfg']),
    'EthernetFlowCtrl' : _MetaInfoEnum('EthernetFlowCtrl',
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_drivers_media_eth_cfg', 'EthernetFlowCtrl',
        '''Ethernet flow ctrl''',
        {
            'ingress':'ingress',
            'egress':'egress',
            'bidirectional':'bidirectional',
        }, 'Cisco-IOS-XR-drivers-media-eth-cfg', _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-drivers-media-eth-cfg']),
    'EthernetDuplex' : _MetaInfoEnum('EthernetDuplex',
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_drivers_media_eth_cfg', 'EthernetDuplex',
        '''Ethernet duplex''',
        {
            'full':'full',
            'half':'half',
        }, 'Cisco-IOS-XR-drivers-media-eth-cfg', _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-drivers-media-eth-cfg']),
    'EthernetLoopback' : _MetaInfoEnum('EthernetLoopback',
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_drivers_media_eth_cfg', 'EthernetLoopback',
        '''Ethernet loopback''',
        {
            'external':'external',
            'internal':'internal',
            'line':'line',
        }, 'Cisco-IOS-XR-drivers-media-eth-cfg', _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-drivers-media-eth-cfg']),
    'EthernetSpeed' : _MetaInfoEnum('EthernetSpeed',
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_drivers_media_eth_cfg', 'EthernetSpeed',
        '''Ethernet speed''',
        {
            '10':'Y_10',
            '100':'Y_100',
            '1000':'Y_1000',
        }, 'Cisco-IOS-XR-drivers-media-eth-cfg', _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-drivers-media-eth-cfg']),
    'EthernetIpg' : _MetaInfoEnum('EthernetIpg',
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_drivers_media_eth_cfg', 'EthernetIpg',
        '''Ethernet ipg''',
        {
            'non-standard':'non_standard',
        }, 'Cisco-IOS-XR-drivers-media-eth-cfg', _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-drivers-media-eth-cfg']),
    'EthernetPfc' : _MetaInfoEnum('EthernetPfc',
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_drivers_media_eth_cfg', 'EthernetPfc',
        '''Ethernet pfc''',
        {
            'on':'on',
        }, 'Cisco-IOS-XR-drivers-media-eth-cfg', _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-drivers-media-eth-cfg']),
}
