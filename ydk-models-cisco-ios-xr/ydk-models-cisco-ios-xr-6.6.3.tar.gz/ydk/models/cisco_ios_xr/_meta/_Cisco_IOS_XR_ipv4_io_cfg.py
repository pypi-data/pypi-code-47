
'''
This is auto-generated file,
which includes metadata for module Cisco_IOS_XR_ipv4_io_cfg
'''

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_LIST, REFERENCE_LEAFLIST, REFERENCE_BITS, REFERENCE_UNION
from ydk._core._dm_meta_info import REFERENCE_CLASS, REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, ANYXML_CLASS
from ydk._core._importer import _yang_ns

_meta_table = {
    'Ipv4Reachable' : _MetaInfoEnum('Ipv4Reachable',
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_io_cfg', 'Ipv4Reachable',
        '''Ipv4 reachable''',
        {
            'any':'any',
            'received':'received',
        }, 'Cisco-IOS-XR-ipv4-io-cfg', _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-ipv4-io-cfg']),
    'Ipv4SelfPing' : _MetaInfoEnum('Ipv4SelfPing',
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_io_cfg', 'Ipv4SelfPing',
        '''Ipv4 self ping''',
        {
            'disabled':'disabled',
            'enabled':'enabled',
        }, 'Cisco-IOS-XR-ipv4-io-cfg', _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-ipv4-io-cfg']),
    'Ipv4DefaultPing' : _MetaInfoEnum('Ipv4DefaultPing',
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_io_cfg', 'Ipv4DefaultPing',
        '''Ipv4 default ping''',
        {
            'disabled':'disabled',
            'enabled':'enabled',
        }, 'Cisco-IOS-XR-ipv4-io-cfg', _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-ipv4-io-cfg']),
    'Ipv4InterfaceQppb' : _MetaInfoEnum('Ipv4InterfaceQppb',
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_io_cfg', 'Ipv4InterfaceQppb',
        '''Ipv4 interface qppb''',
        {
            'ip-precedence':'ip_precedence',
            'qos-group':'qos_group',
            'both':'both',
        }, 'Cisco-IOS-XR-ipv4-io-cfg', _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-ipv4-io-cfg']),
}
