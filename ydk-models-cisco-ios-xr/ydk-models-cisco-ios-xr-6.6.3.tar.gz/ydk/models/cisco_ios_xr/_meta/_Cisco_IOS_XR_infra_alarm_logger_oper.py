
'''
This is auto-generated file,
which includes metadata for module Cisco_IOS_XR_infra_alarm_logger_oper
'''

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_LIST, REFERENCE_LEAFLIST, REFERENCE_BITS, REFERENCE_UNION
from ydk._core._dm_meta_info import REFERENCE_CLASS, REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, ANYXML_CLASS
from ydk._core._importer import _yang_ns

_meta_table = {
    'AlAlarmBistate' : _MetaInfoEnum('AlAlarmBistate',
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_alarm_logger_oper', 'AlAlarmBistate',
        '''Al alarm bistate''',
        {
            'not-available':'not_available',
            'active':'active',
            'clear':'clear',
        }, 'Cisco-IOS-XR-infra-alarm-logger-oper', _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-infra-alarm-logger-oper']),
    'AlAlarmSeverity' : _MetaInfoEnum('AlAlarmSeverity',
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_alarm_logger_oper', 'AlAlarmSeverity',
        '''Al alarm severity''',
        {
            'unknown':'unknown',
            'emergency':'emergency',
            'alert':'alert',
            'critical':'critical',
            'error':'error',
            'warning':'warning',
            'notice':'notice',
            'informational':'informational',
            'debugging':'debugging',
        }, 'Cisco-IOS-XR-infra-alarm-logger-oper', _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-infra-alarm-logger-oper']),
    'AlarmLogger.BufferStatus' : {
        'meta_info' : _MetaInfoClass('AlarmLogger.BufferStatus', REFERENCE_CLASS,
            '''Describes buffer utilization and parameters
configured''',
            False, 
            [
            _MetaInfoClassMember('log-buffer-size', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('0', '4294967295')], [],
                '''                Current Logging Buffer Size (Bytes)
                ''',
                'log_buffer_size',
                'Cisco-IOS-XR-infra-alarm-logger-oper', False, is_config=False),
            _MetaInfoClassMember('max-log-buffer-size', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('0', '4294967295')], [],
                '''                Maximum Logging Buffer Size (Bytes) 
                ''',
                'max_log_buffer_size',
                'Cisco-IOS-XR-infra-alarm-logger-oper', False, is_config=False),
            _MetaInfoClassMember('record-count', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('0', '4294967295')], [],
                '''                Number of Records in the Buffer
                ''',
                'record_count',
                'Cisco-IOS-XR-infra-alarm-logger-oper', False, is_config=False),
            _MetaInfoClassMember('capacity-threshold', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('0', '4294967295')], [],
                '''                Percentage of the buffer utilization which, when
                exceeded, triggers the  generation of a
                notification for the clients of the XML agent
                ''',
                'capacity_threshold',
                'Cisco-IOS-XR-infra-alarm-logger-oper', False, is_config=False),
            _MetaInfoClassMember('severity-filter', REFERENCE_ENUM_CLASS, 'AlAlarmSeverity', 'Al-alarm-severity',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_alarm_logger_oper', 'AlAlarmSeverity',
                [], [],
                '''                Severity Filter
                ''',
                'severity_filter',
                'Cisco-IOS-XR-infra-alarm-logger-oper', False, is_config=False),
            ],
            'Cisco-IOS-XR-infra-alarm-logger-oper',
            'buffer-status',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-infra-alarm-logger-oper'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_alarm_logger_oper',
            is_config=False,
        ),
    },
    'AlarmLogger.Alarms.Alarm' : {
        'meta_info' : _MetaInfoClass('AlarmLogger.Alarms.Alarm', REFERENCE_LIST,
            '''One of the logged alarms''',
            False, 
            [
            _MetaInfoClassMember('event-id', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('0', '4294967295')], [],
                '''                Event ID
                ''',
                'event_id',
                'Cisco-IOS-XR-infra-alarm-logger-oper', True, is_config=False),
            _MetaInfoClassMember('source-id', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                Source Identifier(Location).Indicates the node
                in which the alarm was generated
                ''',
                'source_id',
                'Cisco-IOS-XR-infra-alarm-logger-oper', False, is_config=False),
            _MetaInfoClassMember('timestamp', ATTRIBUTE, 'int', 'uint64',
                None, None,
                [('0', '18446744073709551615')], [],
                '''                Time when the alarm was generated. It is
                expressed in number of milliseconds since 00:00
                :00 UTC, January 1, 1970
                ''',
                'timestamp',
                'Cisco-IOS-XR-infra-alarm-logger-oper', False, is_config=False),
            _MetaInfoClassMember('category', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                Category of the alarm
                ''',
                'category',
                'Cisco-IOS-XR-infra-alarm-logger-oper', False, is_config=False),
            _MetaInfoClassMember('group', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                Group of messages to which this alarm belongs to
                ''',
                'group',
                'Cisco-IOS-XR-infra-alarm-logger-oper', False, is_config=False),
            _MetaInfoClassMember('code', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                Alarm code which further qualifies the alarm
                within a message group
                ''',
                'code',
                'Cisco-IOS-XR-infra-alarm-logger-oper', False, is_config=False),
            _MetaInfoClassMember('severity', REFERENCE_ENUM_CLASS, 'AlAlarmSeverity', 'Al-alarm-severity',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_alarm_logger_oper', 'AlAlarmSeverity',
                [], [],
                '''                Severity of the alarm
                ''',
                'severity',
                'Cisco-IOS-XR-infra-alarm-logger-oper', False, is_config=False),
            _MetaInfoClassMember('state', REFERENCE_ENUM_CLASS, 'AlAlarmBistate', 'Al-alarm-bistate',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_alarm_logger_oper', 'AlAlarmBistate',
                [], [],
                '''                State of the alarm (bistate alarms only)
                ''',
                'state',
                'Cisco-IOS-XR-infra-alarm-logger-oper', False, is_config=False),
            _MetaInfoClassMember('correlation-id', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('0', '4294967295')], [],
                '''                Correlation Identifier
                ''',
                'correlation_id',
                'Cisco-IOS-XR-infra-alarm-logger-oper', False, is_config=False),
            _MetaInfoClassMember('is-admin', ATTRIBUTE, 'bool', 'boolean',
                None, None,
                [], [],
                '''                Indicates the event id admin-level
                ''',
                'is_admin',
                'Cisco-IOS-XR-infra-alarm-logger-oper', False, is_config=False),
            _MetaInfoClassMember('additional-text', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                Full text of the Alarm
                ''',
                'additional_text',
                'Cisco-IOS-XR-infra-alarm-logger-oper', False, is_config=False),
            ],
            'Cisco-IOS-XR-infra-alarm-logger-oper',
            'alarm',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-infra-alarm-logger-oper'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_alarm_logger_oper',
            is_config=False,
        ),
    },
    'AlarmLogger.Alarms' : {
        'meta_info' : _MetaInfoClass('AlarmLogger.Alarms', REFERENCE_CLASS,
            '''Table that contains the database of logged
alarms''',
            False, 
            [
            _MetaInfoClassMember('alarm', REFERENCE_LIST, 'Alarm', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_alarm_logger_oper', 'AlarmLogger.Alarms.Alarm',
                [], [],
                '''                One of the logged alarms
                ''',
                'alarm',
                'Cisco-IOS-XR-infra-alarm-logger-oper', False, is_config=False),
            ],
            'Cisco-IOS-XR-infra-alarm-logger-oper',
            'alarms',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-infra-alarm-logger-oper'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_alarm_logger_oper',
            is_config=False,
        ),
    },
    'AlarmLogger' : {
        'meta_info' : _MetaInfoClass('AlarmLogger', REFERENCE_CLASS,
            '''Alarm Logger operational data''',
            False, 
            [
            _MetaInfoClassMember('buffer-status', REFERENCE_CLASS, 'BufferStatus', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_alarm_logger_oper', 'AlarmLogger.BufferStatus',
                [], [],
                '''                Describes buffer utilization and parameters
                configured
                ''',
                'buffer_status',
                'Cisco-IOS-XR-infra-alarm-logger-oper', False, is_config=False),
            _MetaInfoClassMember('alarms', REFERENCE_CLASS, 'Alarms', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_alarm_logger_oper', 'AlarmLogger.Alarms',
                [], [],
                '''                Table that contains the database of logged
                alarms
                ''',
                'alarms',
                'Cisco-IOS-XR-infra-alarm-logger-oper', False, is_config=False),
            ],
            'Cisco-IOS-XR-infra-alarm-logger-oper',
            'alarm-logger',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-infra-alarm-logger-oper'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_alarm_logger_oper',
            is_config=False,
        ),
    },
}
_meta_table['AlarmLogger.Alarms.Alarm']['meta_info'].parent =_meta_table['AlarmLogger.Alarms']['meta_info']
_meta_table['AlarmLogger.BufferStatus']['meta_info'].parent =_meta_table['AlarmLogger']['meta_info']
_meta_table['AlarmLogger.Alarms']['meta_info'].parent =_meta_table['AlarmLogger']['meta_info']
