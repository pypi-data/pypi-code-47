
'''
This is auto-generated file,
which includes metadata for module Cisco_IOS_XR_infra_infra_clock_linux_cfg
'''

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_LIST, REFERENCE_LEAFLIST, REFERENCE_BITS, REFERENCE_UNION
from ydk._core._dm_meta_info import REFERENCE_CLASS, REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, ANYXML_CLASS
from ydk._core._importer import _yang_ns

_meta_table = {
    'Clock.TimeZone' : {
        'meta_info' : _MetaInfoClass('Clock.TimeZone', REFERENCE_CLASS,
            '''Configure time zone''',
            False, 
            [
            _MetaInfoClassMember('time-zone-name', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                Name of time zone
                ''',
                'time_zone_name',
                'Cisco-IOS-XR-infra-infra-clock-linux-cfg', False, is_mandatory=True),
            _MetaInfoClassMember('area-name', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                Area File in zoneinfo package
                ''',
                'area_name',
                'Cisco-IOS-XR-infra-infra-clock-linux-cfg', False, is_mandatory=True),
            ],
            'Cisco-IOS-XR-infra-infra-clock-linux-cfg',
            'time-zone',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-infra-infra-clock-linux-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_infra_clock_linux_cfg',
            is_presence=True,
        ),
    },
    'Clock' : {
        'meta_info' : _MetaInfoClass('Clock', REFERENCE_CLASS,
            '''Configure time-of-day clock''',
            False, 
            [
            _MetaInfoClassMember('time-zone', REFERENCE_CLASS, 'TimeZone', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_infra_clock_linux_cfg', 'Clock.TimeZone',
                [], [],
                '''                Configure time zone
                ''',
                'time_zone',
                'Cisco-IOS-XR-infra-infra-clock-linux-cfg', False, is_presence=True),
            ],
            'Cisco-IOS-XR-infra-infra-clock-linux-cfg',
            'clock',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-infra-infra-clock-linux-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_infra_clock_linux_cfg',
        ),
    },
}
_meta_table['Clock.TimeZone']['meta_info'].parent =_meta_table['Clock']['meta_info']
