
'''
This is auto-generated file,
which includes metadata for module Cisco_IOS_XR_mediasvr_linux_oper
'''

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_LIST, REFERENCE_LEAFLIST, REFERENCE_BITS, REFERENCE_UNION
from ydk._core._dm_meta_info import REFERENCE_CLASS, REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, ANYXML_CLASS
from ydk._core._importer import _yang_ns

_meta_table = {
    'MediaSvr.All' : {
        'meta_info' : _MetaInfoClass('MediaSvr.All', REFERENCE_CLASS,
            '''Show Media bag''',
            False, 
            [
            _MetaInfoClassMember('show-output', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                string output
                ''',
                'show_output',
                'Cisco-IOS-XR-mediasvr-linux-oper', False, is_config=False),
            ],
            'Cisco-IOS-XR-mediasvr-linux-oper',
            'all',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-mediasvr-linux-oper'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mediasvr_linux_oper',
            is_config=False,
        ),
    },
    'MediaSvr.LocationDescriptions.LocationDescription' : {
        'meta_info' : _MetaInfoClass('MediaSvr.LocationDescriptions.LocationDescription', REFERENCE_LIST,
            '''Location specified in location''',
            False, 
            [
            _MetaInfoClassMember('node', ATTRIBUTE, 'str', 'xr:Node-id',
                None, None,
                [], [b'([a-zA-Z0-9_]*\\d+/){1,2}([a-zA-Z0-9_]*\\d+)'],
                '''                Node location
                ''',
                'node',
                'Cisco-IOS-XR-mediasvr-linux-oper', True, is_config=False),
            _MetaInfoClassMember('show-output', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                string output
                ''',
                'show_output',
                'Cisco-IOS-XR-mediasvr-linux-oper', False, is_config=False),
            ],
            'Cisco-IOS-XR-mediasvr-linux-oper',
            'location-description',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-mediasvr-linux-oper'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mediasvr_linux_oper',
            is_config=False,
        ),
    },
    'MediaSvr.LocationDescriptions' : {
        'meta_info' : _MetaInfoClass('MediaSvr.LocationDescriptions', REFERENCE_CLASS,
            '''Show Media''',
            False, 
            [
            _MetaInfoClassMember('location-description', REFERENCE_LIST, 'LocationDescription', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mediasvr_linux_oper', 'MediaSvr.LocationDescriptions.LocationDescription',
                [], [],
                '''                Location specified in location
                ''',
                'location_description',
                'Cisco-IOS-XR-mediasvr-linux-oper', False, is_config=False),
            ],
            'Cisco-IOS-XR-mediasvr-linux-oper',
            'location-descriptions',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-mediasvr-linux-oper'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mediasvr_linux_oper',
            is_config=False,
        ),
    },
    'MediaSvr' : {
        'meta_info' : _MetaInfoClass('MediaSvr', REFERENCE_CLASS,
            '''Media server CLI operations''',
            False, 
            [
            _MetaInfoClassMember('all', REFERENCE_CLASS, 'All', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mediasvr_linux_oper', 'MediaSvr.All',
                [], [],
                '''                Show Media bag
                ''',
                'all',
                'Cisco-IOS-XR-mediasvr-linux-oper', False, is_config=False),
            _MetaInfoClassMember('location-descriptions', REFERENCE_CLASS, 'LocationDescriptions', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mediasvr_linux_oper', 'MediaSvr.LocationDescriptions',
                [], [],
                '''                Show Media
                ''',
                'location_descriptions',
                'Cisco-IOS-XR-mediasvr-linux-oper', False, is_config=False),
            ],
            'Cisco-IOS-XR-mediasvr-linux-oper',
            'media-svr',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-mediasvr-linux-oper'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mediasvr_linux_oper',
            is_config=False,
        ),
    },
}
_meta_table['MediaSvr.LocationDescriptions.LocationDescription']['meta_info'].parent =_meta_table['MediaSvr.LocationDescriptions']['meta_info']
_meta_table['MediaSvr.All']['meta_info'].parent =_meta_table['MediaSvr']['meta_info']
_meta_table['MediaSvr.LocationDescriptions']['meta_info'].parent =_meta_table['MediaSvr']['meta_info']
