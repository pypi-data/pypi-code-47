
'''
This is auto-generated file,
which includes metadata for module Cisco_IOS_XR_wdsysmon_fd_oper
'''

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_LIST, REFERENCE_LEAFLIST, REFERENCE_BITS, REFERENCE_UNION
from ydk._core._dm_meta_info import REFERENCE_CLASS, REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, ANYXML_CLASS
from ydk._core._importer import _yang_ns

_meta_table = {
    'SystemMonitoring.CpuUtilization.ProcessCpu' : {
        'meta_info' : _MetaInfoClass('SystemMonitoring.CpuUtilization.ProcessCpu', REFERENCE_LIST,
            '''Per process CPU utilization''',
            False, 
            [
            _MetaInfoClassMember('process-name', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                Process name
                ''',
                'process_name',
                'Cisco-IOS-XR-wdsysmon-fd-oper', False, is_config=False),
            _MetaInfoClassMember('process-id', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('0', '4294967295')], [],
                '''                Process ID
                ''',
                'process_id',
                'Cisco-IOS-XR-wdsysmon-fd-oper', False, is_config=False),
            _MetaInfoClassMember('process-cpu-one-minute', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('0', '4294967295')], [],
                '''                Process CPU utilization in percent for past 1
                minute
                ''',
                'process_cpu_one_minute',
                'Cisco-IOS-XR-wdsysmon-fd-oper', False, is_config=False),
            _MetaInfoClassMember('process-cpu-five-minute', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('0', '4294967295')], [],
                '''                Process CPU utilization in percent for past 5
                minute
                ''',
                'process_cpu_five_minute',
                'Cisco-IOS-XR-wdsysmon-fd-oper', False, is_config=False),
            _MetaInfoClassMember('process-cpu-fifteen-minute', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('0', '4294967295')], [],
                '''                Process CPU utilization in percent for past 15
                minute
                ''',
                'process_cpu_fifteen_minute',
                'Cisco-IOS-XR-wdsysmon-fd-oper', False, is_config=False),
            ],
            'Cisco-IOS-XR-wdsysmon-fd-oper',
            'process-cpu',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-wdsysmon-fd-oper'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_wdsysmon_fd_oper',
            is_config=False,
        ),
    },
    'SystemMonitoring.CpuUtilization' : {
        'meta_info' : _MetaInfoClass('SystemMonitoring.CpuUtilization', REFERENCE_LIST,
            '''Processes CPU utilization information''',
            False, 
            [
            _MetaInfoClassMember('node-name', ATTRIBUTE, 'str', 'xr:Node-id',
                None, None,
                [], [b'([a-zA-Z0-9_]*\\d+/){1,2}([a-zA-Z0-9_]*\\d+)'],
                '''                Node name
                ''',
                'node_name',
                'Cisco-IOS-XR-wdsysmon-fd-oper', True, is_config=False),
            _MetaInfoClassMember('total-cpu-one-minute', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('0', '4294967295')], [],
                '''                Total CPU utilization in past 1 minute
                ''',
                'total_cpu_one_minute',
                'Cisco-IOS-XR-wdsysmon-fd-oper', False, is_config=False),
            _MetaInfoClassMember('total-cpu-five-minute', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('0', '4294967295')], [],
                '''                Total CPU utilization in past 5 minute
                ''',
                'total_cpu_five_minute',
                'Cisco-IOS-XR-wdsysmon-fd-oper', False, is_config=False),
            _MetaInfoClassMember('total-cpu-fifteen-minute', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('0', '4294967295')], [],
                '''                Total CPU utilization in past 15 minute
                ''',
                'total_cpu_fifteen_minute',
                'Cisco-IOS-XR-wdsysmon-fd-oper', False, is_config=False),
            _MetaInfoClassMember('process-cpu', REFERENCE_LIST, 'ProcessCpu', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_wdsysmon_fd_oper', 'SystemMonitoring.CpuUtilization.ProcessCpu',
                [], [],
                '''                Per process CPU utilization
                ''',
                'process_cpu',
                'Cisco-IOS-XR-wdsysmon-fd-oper', False, is_config=False),
            ],
            'Cisco-IOS-XR-wdsysmon-fd-oper',
            'cpu-utilization',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-wdsysmon-fd-oper'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_wdsysmon_fd_oper',
            is_config=False,
        ),
    },
    'SystemMonitoring' : {
        'meta_info' : _MetaInfoClass('SystemMonitoring', REFERENCE_CLASS,
            '''Processes operational data''',
            False, 
            [
            _MetaInfoClassMember('cpu-utilization', REFERENCE_LIST, 'CpuUtilization', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_wdsysmon_fd_oper', 'SystemMonitoring.CpuUtilization',
                [], [],
                '''                Processes CPU utilization information
                ''',
                'cpu_utilization',
                'Cisco-IOS-XR-wdsysmon-fd-oper', False, is_config=False),
            ],
            'Cisco-IOS-XR-wdsysmon-fd-oper',
            'system-monitoring',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-wdsysmon-fd-oper'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_wdsysmon_fd_oper',
            is_config=False,
        ),
    },
}
_meta_table['SystemMonitoring.CpuUtilization.ProcessCpu']['meta_info'].parent =_meta_table['SystemMonitoring.CpuUtilization']['meta_info']
_meta_table['SystemMonitoring.CpuUtilization']['meta_info'].parent =_meta_table['SystemMonitoring']['meta_info']
