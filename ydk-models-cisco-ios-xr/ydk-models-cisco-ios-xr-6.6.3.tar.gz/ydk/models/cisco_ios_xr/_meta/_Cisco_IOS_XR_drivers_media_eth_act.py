
'''
This is auto-generated file,
which includes metadata for module Cisco_IOS_XR_drivers_media_eth_act
'''

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_LIST, REFERENCE_LEAFLIST, REFERENCE_BITS, REFERENCE_UNION
from ydk._core._dm_meta_info import REFERENCE_CLASS, REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, ANYXML_CLASS
from ydk._core._importer import _yang_ns

_meta_table = {
    'ClearControllerCounters.Input' : {
        'meta_info' : _MetaInfoClass('ClearControllerCounters.Input', REFERENCE_CLASS,
            ''' ''',
            False, 
            [
            _MetaInfoClassMember('controller-name', ATTRIBUTE, 'str', 'csc:Interface-name',
                None, None,
                [], [b'[a-zA-Z0-9._/-]+'],
                '''                Controller name
                ''',
                'controller_name',
                'Cisco-IOS-XR-drivers-media-eth-act', False, is_mandatory=True),
            ],
            'Cisco-IOS-XR-drivers-media-eth-act',
            'input',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-drivers-media-eth-act'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_drivers_media_eth_act',
        ),
    },
    'ClearControllerCounters' : {
        'meta_info' : _MetaInfoClass('ClearControllerCounters', REFERENCE_CLASS,
            '''Clear Ethernet MAC ASIC statistics.''',
            False, 
            [
            _MetaInfoClassMember('input', REFERENCE_CLASS, 'Input', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_drivers_media_eth_act', 'ClearControllerCounters.Input',
                [], [],
                '''                ''',
                'input',
                'Cisco-IOS-XR-drivers-media-eth-act', False),
            ],
            'Cisco-IOS-XR-drivers-media-eth-act',
            'clear-controller-counters',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-drivers-media-eth-act'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_drivers_media_eth_act',
        ),
    },
}
_meta_table['ClearControllerCounters.Input']['meta_info'].parent =_meta_table['ClearControllerCounters']['meta_info']
