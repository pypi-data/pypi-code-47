
'''
This is auto-generated file,
which includes metadata for module Cisco_IOS_XR_lpts_punt_flowtrap_cfg
'''

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_LIST, REFERENCE_LEAFLIST, REFERENCE_BITS, REFERENCE_UNION
from ydk._core._dm_meta_info import REFERENCE_CLASS, REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, ANYXML_CLASS
from ydk._core._importer import _yang_ns

_meta_table = {
    'LptsPuntFlowtrapProtoId' : _MetaInfoEnum('LptsPuntFlowtrapProtoId',
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lpts_punt_flowtrap_cfg', 'LptsPuntFlowtrapProtoId',
        '''Lpts punt flowtrap proto id''',
        {
            'arp':'arp',
            'icmp':'icmp',
            'dhcp':'dhcp',
            'pppoe':'pppoe',
            'ppp':'ppp',
            'igmp':'igmp',
            'ipv4':'ipv4',
            'l2tp':'l2tp',
            'unclassified':'unclassified',
            'ospf':'ospf',
            'bgp':'bgp',
            'default':'default',
        }, 'Cisco-IOS-XR-lpts-punt-flowtrap-cfg', _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-lpts-punt-flowtrap-cfg']),
}
