
'''
This is auto-generated file,
which includes metadata for module Cisco_IOS_XR_linux_os_heap_summary_oper
'''

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_LIST, REFERENCE_LEAFLIST, REFERENCE_BITS, REFERENCE_UNION
from ydk._core._dm_meta_info import REFERENCE_CLASS, REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, ANYXML_CLASS
from ydk._core._importer import _yang_ns

_meta_table = {
    'HeapSummary.LocationDescriptions.LocationDescription' : {
        'meta_info' : _MetaInfoClass('HeapSummary.LocationDescriptions.LocationDescription', REFERENCE_LIST,
            '''Location specified in location''',
            False, 
            [
            _MetaInfoClassMember('node', ATTRIBUTE, 'str', 'xr:Node-id',
                None, None,
                [], [b'([a-zA-Z0-9_]*\\d+/){1,2}([a-zA-Z0-9_]*\\d+)'],
                '''                Node location
                ''',
                'node',
                'Cisco-IOS-XR-linux-os-heap-summary-oper', True, is_config=False),
            _MetaInfoClassMember('show-output', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                string output
                ''',
                'show_output',
                'Cisco-IOS-XR-linux-os-heap-summary-oper', False, is_config=False),
            ],
            'Cisco-IOS-XR-linux-os-heap-summary-oper',
            'location-description',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-linux-os-heap-summary-oper'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_linux_os_heap_summary_oper',
            is_config=False,
        ),
    },
    'HeapSummary.LocationDescriptions' : {
        'meta_info' : _MetaInfoClass('HeapSummary.LocationDescriptions', REFERENCE_CLASS,
            '''Location''',
            False, 
            [
            _MetaInfoClassMember('location-description', REFERENCE_LIST, 'LocationDescription', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_linux_os_heap_summary_oper', 'HeapSummary.LocationDescriptions.LocationDescription',
                [], [],
                '''                Location specified in location
                ''',
                'location_description',
                'Cisco-IOS-XR-linux-os-heap-summary-oper', False, is_config=False),
            ],
            'Cisco-IOS-XR-linux-os-heap-summary-oper',
            'location-descriptions',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-linux-os-heap-summary-oper'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_linux_os_heap_summary_oper',
            is_config=False,
        ),
    },
    'HeapSummary.All' : {
        'meta_info' : _MetaInfoClass('HeapSummary.All', REFERENCE_CLASS,
            '''All locations''',
            False, 
            [
            _MetaInfoClassMember('show-output', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                string output
                ''',
                'show_output',
                'Cisco-IOS-XR-linux-os-heap-summary-oper', False, is_config=False),
            ],
            'Cisco-IOS-XR-linux-os-heap-summary-oper',
            'all',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-linux-os-heap-summary-oper'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_linux_os_heap_summary_oper',
            is_config=False,
        ),
    },
    'HeapSummary' : {
        'meta_info' : _MetaInfoClass('HeapSummary', REFERENCE_CLASS,
            '''Heap Summary''',
            False, 
            [
            _MetaInfoClassMember('location-descriptions', REFERENCE_CLASS, 'LocationDescriptions', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_linux_os_heap_summary_oper', 'HeapSummary.LocationDescriptions',
                [], [],
                '''                Location
                ''',
                'location_descriptions',
                'Cisco-IOS-XR-linux-os-heap-summary-oper', False, is_config=False),
            _MetaInfoClassMember('all', REFERENCE_CLASS, 'All', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_linux_os_heap_summary_oper', 'HeapSummary.All',
                [], [],
                '''                All locations
                ''',
                'all',
                'Cisco-IOS-XR-linux-os-heap-summary-oper', False, is_config=False),
            ],
            'Cisco-IOS-XR-linux-os-heap-summary-oper',
            'heap-summary',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-linux-os-heap-summary-oper'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_linux_os_heap_summary_oper',
            is_config=False,
        ),
    },
}
_meta_table['HeapSummary.LocationDescriptions.LocationDescription']['meta_info'].parent =_meta_table['HeapSummary.LocationDescriptions']['meta_info']
_meta_table['HeapSummary.LocationDescriptions']['meta_info'].parent =_meta_table['HeapSummary']['meta_info']
_meta_table['HeapSummary.All']['meta_info'].parent =_meta_table['HeapSummary']['meta_info']
