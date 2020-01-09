
'''
This is auto-generated file,
which includes metadata for module Cisco_IOS_XR_ipv4_arp_act
'''

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_LIST, REFERENCE_LEAFLIST, REFERENCE_BITS, REFERENCE_UNION
from ydk._core._dm_meta_info import REFERENCE_CLASS, REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, ANYXML_CLASS
from ydk._core._importer import _yang_ns

_meta_table = {
    'ClearArpApiStatsApi.Input' : {
        'meta_info' : _MetaInfoClass('ClearArpApiStatsApi.Input', REFERENCE_CLASS,
            ''' ''',
            False, 
            [
            _MetaInfoClassMember('name', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                ''',
                'name',
                'Cisco-IOS-XR-ipv4-arp-act', False, is_mandatory=True),
            ],
            'Cisco-IOS-XR-ipv4-arp-act',
            'input',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-ipv4-arp-act'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_arp_act',
        ),
    },
    'ClearArpApiStatsApi' : {
        'meta_info' : _MetaInfoClass('ClearArpApiStatsApi', REFERENCE_CLASS,
            ''' ''',
            False, 
            [
            _MetaInfoClassMember('input', REFERENCE_CLASS, 'Input', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_arp_act', 'ClearArpApiStatsApi.Input',
                [], [],
                '''                ''',
                'input',
                'Cisco-IOS-XR-ipv4-arp-act', False),
            ],
            'Cisco-IOS-XR-ipv4-arp-act',
            'clear-arp-api-stats-api',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-ipv4-arp-act'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_arp_act',
        ),
    },
    'ClearArpApiStatsLocation.Input' : {
        'meta_info' : _MetaInfoClass('ClearArpApiStatsLocation.Input', REFERENCE_CLASS,
            ''' ''',
            False, 
            [
            _MetaInfoClassMember('node-location', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                ''',
                'node_location',
                'Cisco-IOS-XR-ipv4-arp-act', False, is_mandatory=True),
            ],
            'Cisco-IOS-XR-ipv4-arp-act',
            'input',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-ipv4-arp-act'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_arp_act',
        ),
    },
    'ClearArpApiStatsLocation' : {
        'meta_info' : _MetaInfoClass('ClearArpApiStatsLocation', REFERENCE_CLASS,
            ''' ''',
            False, 
            [
            _MetaInfoClassMember('input', REFERENCE_CLASS, 'Input', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_arp_act', 'ClearArpApiStatsLocation.Input',
                [], [],
                '''                ''',
                'input',
                'Cisco-IOS-XR-ipv4-arp-act', False),
            ],
            'Cisco-IOS-XR-ipv4-arp-act',
            'clear-arp-api-stats-location',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-ipv4-arp-act'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_arp_act',
        ),
    },
}
_meta_table['ClearArpApiStatsApi.Input']['meta_info'].parent =_meta_table['ClearArpApiStatsApi']['meta_info']
_meta_table['ClearArpApiStatsLocation.Input']['meta_info'].parent =_meta_table['ClearArpApiStatsLocation']['meta_info']
