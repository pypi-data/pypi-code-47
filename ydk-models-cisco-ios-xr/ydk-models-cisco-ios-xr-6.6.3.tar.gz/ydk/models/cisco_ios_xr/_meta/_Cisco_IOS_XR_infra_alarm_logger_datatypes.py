
'''
This is auto-generated file,
which includes metadata for module Cisco_IOS_XR_infra_alarm_logger_datatypes
'''

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_LIST, REFERENCE_LEAFLIST, REFERENCE_BITS, REFERENCE_UNION
from ydk._core._dm_meta_info import REFERENCE_CLASS, REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, ANYXML_CLASS
from ydk._core._importer import _yang_ns

_meta_table = {
    'AlarmLoggerSeverityLevel' : _MetaInfoEnum('AlarmLoggerSeverityLevel',
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_alarm_logger_datatypes', 'AlarmLoggerSeverityLevel',
        '''Alarm logger severity level''',
        {
            'emergency':'emergency',
            'alert':'alert',
            'critical':'critical',
            'error':'error',
            'warning':'warning',
            'notice':'notice',
            'informational':'informational',
        }, 'Cisco-IOS-XR-infra-alarm-logger-datatypes', _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-infra-alarm-logger-datatypes']),
}
