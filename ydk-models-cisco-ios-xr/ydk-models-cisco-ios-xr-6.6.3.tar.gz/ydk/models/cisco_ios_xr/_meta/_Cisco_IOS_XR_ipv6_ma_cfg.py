
'''
This is auto-generated file,
which includes metadata for module Cisco_IOS_XR_ipv6_ma_cfg
'''

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_LIST, REFERENCE_LEAFLIST, REFERENCE_BITS, REFERENCE_UNION
from ydk._core._dm_meta_info import REFERENCE_CLASS, REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, ANYXML_CLASS
from ydk._core._importer import _yang_ns

_meta_table = {
    'Ipv6SelfPing' : _MetaInfoEnum('Ipv6SelfPing',
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ma_cfg', 'Ipv6SelfPing',
        '''Ipv6 self ping''',
        {
            'disabled':'disabled',
            'enabled':'enabled',
        }, 'Cisco-IOS-XR-ipv6-ma-cfg', _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-ipv6-ma-cfg']),
    'Ipv6Reachable' : _MetaInfoEnum('Ipv6Reachable',
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ma_cfg', 'Ipv6Reachable',
        '''Ipv6 reachable''',
        {
            'any':'any',
            'received':'received',
        }, 'Cisco-IOS-XR-ipv6-ma-cfg', _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-ipv6-ma-cfg']),
    'Ipv6DefaultPing' : _MetaInfoEnum('Ipv6DefaultPing',
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ma_cfg', 'Ipv6DefaultPing',
        '''Ipv6 default ping''',
        {
            'disabled':'disabled',
            'enabled':'enabled',
        }, 'Cisco-IOS-XR-ipv6-ma-cfg', _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-ipv6-ma-cfg']),
    'Ipv6Qppb' : _MetaInfoEnum('Ipv6Qppb',
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ma_cfg', 'Ipv6Qppb',
        '''Ipv6 qppb''',
        {
            'none':'none',
            'ip-precedence':'ip_precedence',
            'qos-group':'qos_group',
            'both':'both',
        }, 'Cisco-IOS-XR-ipv6-ma-cfg', _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-ipv6-ma-cfg']),
}
