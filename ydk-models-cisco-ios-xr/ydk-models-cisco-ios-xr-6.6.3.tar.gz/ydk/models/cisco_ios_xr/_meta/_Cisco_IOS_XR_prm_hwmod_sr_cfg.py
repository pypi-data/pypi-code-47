
'''
This is auto-generated file,
which includes metadata for module Cisco_IOS_XR_prm_hwmod_sr_cfg
'''

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_LIST, REFERENCE_LEAFLIST, REFERENCE_BITS, REFERENCE_UNION
from ydk._core._dm_meta_info import REFERENCE_CLASS, REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, ANYXML_CLASS
from ydk._core._importer import _yang_ns

_meta_table = {
    'HardwareModule.SegmentRouting.Reserve.ServiceLabel' : {
        'meta_info' : _MetaInfoClass('HardwareModule.SegmentRouting.Reserve.ServiceLabel', REFERENCE_CLASS,
            '''Service Label''',
            False, 
            [
            _MetaInfoClassMember('enable', ATTRIBUTE, 'Empty', 'empty',
                None, None,
                [], [],
                '''                Enable
                ''',
                'enable',
                'Cisco-IOS-XR-prm-hwmod-sr-cfg', False),
            ],
            'Cisco-IOS-XR-prm-hwmod-sr-cfg',
            'service-label',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-prm-hwmod-sr-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_prm_hwmod_sr_cfg',
        ),
    },
    'HardwareModule.SegmentRouting.Reserve' : {
        'meta_info' : _MetaInfoClass('HardwareModule.SegmentRouting.Reserve', REFERENCE_CLASS,
            '''Reserve''',
            False, 
            [
            _MetaInfoClassMember('service-label', REFERENCE_CLASS, 'ServiceLabel', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_prm_hwmod_sr_cfg', 'HardwareModule.SegmentRouting.Reserve.ServiceLabel',
                [], [],
                '''                Service Label
                ''',
                'service_label',
                'Cisco-IOS-XR-prm-hwmod-sr-cfg', False),
            ],
            'Cisco-IOS-XR-prm-hwmod-sr-cfg',
            'reserve',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-prm-hwmod-sr-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_prm_hwmod_sr_cfg',
        ),
    },
    'HardwareModule.SegmentRouting' : {
        'meta_info' : _MetaInfoClass('HardwareModule.SegmentRouting', REFERENCE_CLASS,
            '''Segment Routing''',
            False, 
            [
            _MetaInfoClassMember('reserve', REFERENCE_CLASS, 'Reserve', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_prm_hwmod_sr_cfg', 'HardwareModule.SegmentRouting.Reserve',
                [], [],
                '''                Reserve
                ''',
                'reserve',
                'Cisco-IOS-XR-prm-hwmod-sr-cfg', False),
            ],
            'Cisco-IOS-XR-prm-hwmod-sr-cfg',
            'segment-routing',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-prm-hwmod-sr-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_prm_hwmod_sr_cfg',
        ),
    },
    'HardwareModule' : {
        'meta_info' : _MetaInfoClass('HardwareModule', REFERENCE_CLASS,
            '''HardwareModule''',
            False, 
            [
            _MetaInfoClassMember('segment-routing', REFERENCE_CLASS, 'SegmentRouting', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_prm_hwmod_sr_cfg', 'HardwareModule.SegmentRouting',
                [], [],
                '''                Segment Routing
                ''',
                'segment_routing',
                'Cisco-IOS-XR-prm-hwmod-sr-cfg', False),
            ],
            'Cisco-IOS-XR-prm-hwmod-sr-cfg',
            'hardware-module',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-prm-hwmod-sr-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_prm_hwmod_sr_cfg',
        ),
    },
}
_meta_table['HardwareModule.SegmentRouting.Reserve.ServiceLabel']['meta_info'].parent =_meta_table['HardwareModule.SegmentRouting.Reserve']['meta_info']
_meta_table['HardwareModule.SegmentRouting.Reserve']['meta_info'].parent =_meta_table['HardwareModule.SegmentRouting']['meta_info']
_meta_table['HardwareModule.SegmentRouting']['meta_info'].parent =_meta_table['HardwareModule']['meta_info']
