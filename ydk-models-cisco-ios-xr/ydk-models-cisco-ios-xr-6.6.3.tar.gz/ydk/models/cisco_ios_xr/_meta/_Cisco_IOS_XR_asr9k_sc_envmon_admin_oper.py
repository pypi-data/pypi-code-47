
'''
This is auto-generated file,
which includes metadata for module Cisco_IOS_XR_asr9k_sc_envmon_admin_oper
'''

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_LIST, REFERENCE_LEAFLIST, REFERENCE_BITS, REFERENCE_UNION
from ydk._core._dm_meta_info import REFERENCE_CLASS, REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, ANYXML_CLASS
from ydk._core._importer import _yang_ns

_meta_table = {
    'EnvironmentalMonitoring.Racks.Rack.Slots.Slot.Modules.Module.SensorTypes.SensorType.SensorNames.SensorName.Thresholds.Threshold.ValueDetailed' : {
        'meta_info' : _MetaInfoClass('EnvironmentalMonitoring.Racks.Rack.Slots.Slot.Modules.Module.SensorTypes.SensorType.SensorNames.SensorName.Thresholds.Threshold.ValueDetailed', REFERENCE_CLASS,
            '''Detailed sensor threshold
information''',
            False, 
            [
            _MetaInfoClassMember('threshold-severity', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('0', '4294967295')], [],
                '''                Indicates minor, major, critical severities
                ''',
                'threshold_severity',
                'Cisco-IOS-XR-asr9k-sc-envmon-admin-oper', False, is_config=False),
            _MetaInfoClassMember('threshold-relation', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('0', '4294967295')], [],
                '''                Indicates relation between sensor value and
                threshold
                ''',
                'threshold_relation',
                'Cisco-IOS-XR-asr9k-sc-envmon-admin-oper', False, is_config=False),
            _MetaInfoClassMember('threshold-value', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('0', '4294967295')], [],
                '''                Value of the configured threshold
                ''',
                'threshold_value',
                'Cisco-IOS-XR-asr9k-sc-envmon-admin-oper', False, is_config=False),
            _MetaInfoClassMember('threshold-evaluation', ATTRIBUTE, 'bool', 'boolean',
                None, None,
                [], [],
                '''                Indicates the result of the most recent
                evaluation of the thresholD
                ''',
                'threshold_evaluation',
                'Cisco-IOS-XR-asr9k-sc-envmon-admin-oper', False, is_config=False),
            _MetaInfoClassMember('threshold-notification-enabled', ATTRIBUTE, 'bool', 'boolean',
                None, None,
                [], [],
                '''                Indicates whether or not a notification should
                result, in case of threshold violation
                ''',
                'threshold_notification_enabled',
                'Cisco-IOS-XR-asr9k-sc-envmon-admin-oper', False, is_config=False),
            ],
            'Cisco-IOS-XR-asr9k-sc-envmon-admin-oper',
            'value-detailed',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-asr9k-sc-envmon-admin-oper'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_envmon_admin_oper',
            is_config=False,
        ),
    },
    'EnvironmentalMonitoring.Racks.Rack.Slots.Slot.Modules.Module.SensorTypes.SensorType.SensorNames.SensorName.Thresholds.Threshold' : {
        'meta_info' : _MetaInfoClass('EnvironmentalMonitoring.Racks.Rack.Slots.Slot.Modules.Module.SensorTypes.SensorType.SensorNames.SensorName.Thresholds.Threshold', REFERENCE_LIST,
            '''Types of thresholds''',
            False, 
            [
            _MetaInfoClassMember('type', ATTRIBUTE, 'str', 'xr:Cisco-ios-xr-string',
                None, None,
                [], [b'[\\w\\-\\.:,_@#%$\\+=\\|;]+'],
                '''                Threshold type
                ''',
                'type',
                'Cisco-IOS-XR-asr9k-sc-envmon-admin-oper', True, is_config=False),
            _MetaInfoClassMember('value-detailed', REFERENCE_CLASS, 'ValueDetailed', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_envmon_admin_oper', 'EnvironmentalMonitoring.Racks.Rack.Slots.Slot.Modules.Module.SensorTypes.SensorType.SensorNames.SensorName.Thresholds.Threshold.ValueDetailed',
                [], [],
                '''                Detailed sensor threshold
                information
                ''',
                'value_detailed',
                'Cisco-IOS-XR-asr9k-sc-envmon-admin-oper', False, is_config=False),
            _MetaInfoClassMember('trap', ATTRIBUTE, 'bool', 'boolean',
                None, None,
                [], [],
                '''                Threshold trap enable flag
                true-ENABLE, false-DISABLE
                ''',
                'trap',
                'Cisco-IOS-XR-asr9k-sc-envmon-admin-oper', False, is_config=False),
            _MetaInfoClassMember('value-brief', ATTRIBUTE, 'str', 'xr:Hex-integer',
                None, None,
                [], [b'[0-9a-fA-F]{1,8}'],
                '''                Threshold value for the sensor
                ''',
                'value_brief',
                'Cisco-IOS-XR-asr9k-sc-envmon-admin-oper', False, is_config=False),
            ],
            'Cisco-IOS-XR-asr9k-sc-envmon-admin-oper',
            'threshold',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-asr9k-sc-envmon-admin-oper'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_envmon_admin_oper',
            is_config=False,
        ),
    },
    'EnvironmentalMonitoring.Racks.Rack.Slots.Slot.Modules.Module.SensorTypes.SensorType.SensorNames.SensorName.Thresholds' : {
        'meta_info' : _MetaInfoClass('EnvironmentalMonitoring.Racks.Rack.Slots.Slot.Modules.Module.SensorTypes.SensorType.SensorNames.SensorName.Thresholds', REFERENCE_CLASS,
            '''The threshold information''',
            False, 
            [
            _MetaInfoClassMember('threshold', REFERENCE_LIST, 'Threshold', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_envmon_admin_oper', 'EnvironmentalMonitoring.Racks.Rack.Slots.Slot.Modules.Module.SensorTypes.SensorType.SensorNames.SensorName.Thresholds.Threshold',
                [], [],
                '''                Types of thresholds
                ''',
                'threshold',
                'Cisco-IOS-XR-asr9k-sc-envmon-admin-oper', False, is_config=False),
            ],
            'Cisco-IOS-XR-asr9k-sc-envmon-admin-oper',
            'thresholds',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-asr9k-sc-envmon-admin-oper'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_envmon_admin_oper',
            is_config=False,
        ),
    },
    'EnvironmentalMonitoring.Racks.Rack.Slots.Slot.Modules.Module.SensorTypes.SensorType.SensorNames.SensorName.ValueDetailed' : {
        'meta_info' : _MetaInfoClass('EnvironmentalMonitoring.Racks.Rack.Slots.Slot.Modules.Module.SensorTypes.SensorType.SensorNames.SensorName.ValueDetailed', REFERENCE_CLASS,
            '''Detailed sensor information including
the sensor value''',
            False, 
            [
            _MetaInfoClassMember('field-validity-bitmap', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('0', '4294967295')], [],
                '''                Sensor valid bitmap
                ''',
                'field_validity_bitmap',
                'Cisco-IOS-XR-asr9k-sc-envmon-admin-oper', False, is_config=False),
            _MetaInfoClassMember('device-description', ATTRIBUTE, 'str', 'string',
                None, None,
                [(0, 50)], [],
                '''                Device Name
                ''',
                'device_description',
                'Cisco-IOS-XR-asr9k-sc-envmon-admin-oper', False, is_config=False),
            _MetaInfoClassMember('units', ATTRIBUTE, 'str', 'string',
                None, None,
                [(0, 50)], [],
                '''                Units of variable being read
                ''',
                'units',
                'Cisco-IOS-XR-asr9k-sc-envmon-admin-oper', False, is_config=False),
            _MetaInfoClassMember('device-id', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('0', '4294967295')], [],
                '''                Identifier for this device
                ''',
                'device_id',
                'Cisco-IOS-XR-asr9k-sc-envmon-admin-oper', False, is_config=False),
            _MetaInfoClassMember('value', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('0', '4294967295')], [],
                '''                Current reading of sensor
                ''',
                'value',
                'Cisco-IOS-XR-asr9k-sc-envmon-admin-oper', False, is_config=False),
            _MetaInfoClassMember('alarm-type', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('0', '4294967295')], [],
                '''                Indicates threshold violation
                ''',
                'alarm_type',
                'Cisco-IOS-XR-asr9k-sc-envmon-admin-oper', False, is_config=False),
            _MetaInfoClassMember('data-type', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('0', '4294967295')], [],
                '''                Sensor data type enums
                ''',
                'data_type',
                'Cisco-IOS-XR-asr9k-sc-envmon-admin-oper', False, is_config=False),
            _MetaInfoClassMember('scale', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('0', '4294967295')], [],
                '''                Sensor scale enums
                ''',
                'scale',
                'Cisco-IOS-XR-asr9k-sc-envmon-admin-oper', False, is_config=False),
            _MetaInfoClassMember('precision', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('0', '4294967295')], [],
                '''                Sensor precision range
                ''',
                'precision',
                'Cisco-IOS-XR-asr9k-sc-envmon-admin-oper', False, is_config=False),
            _MetaInfoClassMember('status', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('0', '4294967295')], [],
                '''                Sensor operation state enums
                ''',
                'status',
                'Cisco-IOS-XR-asr9k-sc-envmon-admin-oper', False, is_config=False),
            _MetaInfoClassMember('age-time-stamp', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('0', '4294967295')], [],
                '''                Age of the sensor value; set to the current time
                if directly access the value from sensor
                ''',
                'age_time_stamp',
                'Cisco-IOS-XR-asr9k-sc-envmon-admin-oper', False, is_config=False),
            _MetaInfoClassMember('update-rate', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('0', '4294967295')], [],
                '''                Sensor value update rate;set to 0 if sensor
                value is updated and evaluated immediately
                ''',
                'update_rate',
                'Cisco-IOS-XR-asr9k-sc-envmon-admin-oper', False, is_config=False),
            _MetaInfoClassMember('average', ATTRIBUTE, 'int', 'int32',
                None, None,
                [('-2147483648', '2147483647')], [],
                '''                Average sensor value over time interval
                ''',
                'average',
                'Cisco-IOS-XR-asr9k-sc-envmon-admin-oper', False, is_config=False),
            _MetaInfoClassMember('minimum', ATTRIBUTE, 'int', 'int32',
                None, None,
                [('-2147483648', '2147483647')], [],
                '''                Minimum Sensor value over time interval
                ''',
                'minimum',
                'Cisco-IOS-XR-asr9k-sc-envmon-admin-oper', False, is_config=False),
            _MetaInfoClassMember('maximum', ATTRIBUTE, 'int', 'int32',
                None, None,
                [('-2147483648', '2147483647')], [],
                '''                Maximum Sensor value over time interval
                ''',
                'maximum',
                'Cisco-IOS-XR-asr9k-sc-envmon-admin-oper', False, is_config=False),
            _MetaInfoClassMember('interval', ATTRIBUTE, 'int', 'int32',
                None, None,
                [('-2147483648', '2147483647')], [],
                '''                Time Interval over which sensor value is
                monitored
                ''',
                'interval',
                'Cisco-IOS-XR-asr9k-sc-envmon-admin-oper', False, is_config=False),
            ],
            'Cisco-IOS-XR-asr9k-sc-envmon-admin-oper',
            'value-detailed',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-asr9k-sc-envmon-admin-oper'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_envmon_admin_oper',
            is_config=False,
        ),
    },
    'EnvironmentalMonitoring.Racks.Rack.Slots.Slot.Modules.Module.SensorTypes.SensorType.SensorNames.SensorName' : {
        'meta_info' : _MetaInfoClass('EnvironmentalMonitoring.Racks.Rack.Slots.Slot.Modules.Module.SensorTypes.SensorType.SensorNames.SensorName', REFERENCE_LIST,
            '''Name of sensor''',
            False, 
            [
            _MetaInfoClassMember('name', ATTRIBUTE, 'str', 'xr:Cisco-ios-xr-string',
                None, None,
                [], [b'[\\w\\-\\.:,_@#%$\\+=\\|;]+'],
                '''                Sensor name
                ''',
                'name',
                'Cisco-IOS-XR-asr9k-sc-envmon-admin-oper', True, is_config=False),
            _MetaInfoClassMember('thresholds', REFERENCE_CLASS, 'Thresholds', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_envmon_admin_oper', 'EnvironmentalMonitoring.Racks.Rack.Slots.Slot.Modules.Module.SensorTypes.SensorType.SensorNames.SensorName.Thresholds',
                [], [],
                '''                The threshold information
                ''',
                'thresholds',
                'Cisco-IOS-XR-asr9k-sc-envmon-admin-oper', False, is_config=False),
            _MetaInfoClassMember('value-detailed', REFERENCE_CLASS, 'ValueDetailed', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_envmon_admin_oper', 'EnvironmentalMonitoring.Racks.Rack.Slots.Slot.Modules.Module.SensorTypes.SensorType.SensorNames.SensorName.ValueDetailed',
                [], [],
                '''                Detailed sensor information including
                the sensor value
                ''',
                'value_detailed',
                'Cisco-IOS-XR-asr9k-sc-envmon-admin-oper', False, is_config=False),
            _MetaInfoClassMember('value-brief', ATTRIBUTE, 'str', 'xr:Hex-integer',
                None, None,
                [], [b'[0-9a-fA-F]{1,8}'],
                '''                The sensor value
                ''',
                'value_brief',
                'Cisco-IOS-XR-asr9k-sc-envmon-admin-oper', False, is_config=False),
            ],
            'Cisco-IOS-XR-asr9k-sc-envmon-admin-oper',
            'sensor-name',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-asr9k-sc-envmon-admin-oper'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_envmon_admin_oper',
            is_config=False,
        ),
    },
    'EnvironmentalMonitoring.Racks.Rack.Slots.Slot.Modules.Module.SensorTypes.SensorType.SensorNames' : {
        'meta_info' : _MetaInfoClass('EnvironmentalMonitoring.Racks.Rack.Slots.Slot.Modules.Module.SensorTypes.SensorType.SensorNames', REFERENCE_CLASS,
            '''Table of sensors''',
            False, 
            [
            _MetaInfoClassMember('sensor-name', REFERENCE_LIST, 'SensorName', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_envmon_admin_oper', 'EnvironmentalMonitoring.Racks.Rack.Slots.Slot.Modules.Module.SensorTypes.SensorType.SensorNames.SensorName',
                [], [],
                '''                Name of sensor
                ''',
                'sensor_name',
                'Cisco-IOS-XR-asr9k-sc-envmon-admin-oper', False, is_config=False),
            ],
            'Cisco-IOS-XR-asr9k-sc-envmon-admin-oper',
            'sensor-names',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-asr9k-sc-envmon-admin-oper'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_envmon_admin_oper',
            is_config=False,
        ),
    },
    'EnvironmentalMonitoring.Racks.Rack.Slots.Slot.Modules.Module.SensorTypes.SensorType' : {
        'meta_info' : _MetaInfoClass('EnvironmentalMonitoring.Racks.Rack.Slots.Slot.Modules.Module.SensorTypes.SensorType', REFERENCE_LIST,
            '''Type of sensor''',
            False, 
            [
            _MetaInfoClassMember('type', ATTRIBUTE, 'str', 'xr:Cisco-ios-xr-string',
                None, None,
                [], [b'[\\w\\-\\.:,_@#%$\\+=\\|;]+'],
                '''                Sensor type
                ''',
                'type',
                'Cisco-IOS-XR-asr9k-sc-envmon-admin-oper', True, is_config=False),
            _MetaInfoClassMember('sensor-names', REFERENCE_CLASS, 'SensorNames', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_envmon_admin_oper', 'EnvironmentalMonitoring.Racks.Rack.Slots.Slot.Modules.Module.SensorTypes.SensorType.SensorNames',
                [], [],
                '''                Table of sensors
                ''',
                'sensor_names',
                'Cisco-IOS-XR-asr9k-sc-envmon-admin-oper', False, is_config=False),
            ],
            'Cisco-IOS-XR-asr9k-sc-envmon-admin-oper',
            'sensor-type',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-asr9k-sc-envmon-admin-oper'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_envmon_admin_oper',
            is_config=False,
        ),
    },
    'EnvironmentalMonitoring.Racks.Rack.Slots.Slot.Modules.Module.SensorTypes' : {
        'meta_info' : _MetaInfoClass('EnvironmentalMonitoring.Racks.Rack.Slots.Slot.Modules.Module.SensorTypes', REFERENCE_CLASS,
            '''Table of sensor types''',
            False, 
            [
            _MetaInfoClassMember('sensor-type', REFERENCE_LIST, 'SensorType', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_envmon_admin_oper', 'EnvironmentalMonitoring.Racks.Rack.Slots.Slot.Modules.Module.SensorTypes.SensorType',
                [], [],
                '''                Type of sensor
                ''',
                'sensor_type',
                'Cisco-IOS-XR-asr9k-sc-envmon-admin-oper', False, is_config=False),
            ],
            'Cisco-IOS-XR-asr9k-sc-envmon-admin-oper',
            'sensor-types',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-asr9k-sc-envmon-admin-oper'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_envmon_admin_oper',
            is_config=False,
        ),
    },
    'EnvironmentalMonitoring.Racks.Rack.Slots.Slot.Modules.Module.Power.PowerBag' : {
        'meta_info' : _MetaInfoClass('EnvironmentalMonitoring.Racks.Rack.Slots.Slot.Modules.Module.Power.PowerBag', REFERENCE_CLASS,
            '''Detailed power bag information''',
            False, 
            [
            _MetaInfoClassMember('power-value', ATTRIBUTE, 'int', 'int32',
                None, None,
                [('-2147483648', '2147483647')], [],
                '''                Current Power Value of the Unit
                ''',
                'power_value',
                'Cisco-IOS-XR-asr9k-sc-envmon-admin-oper', False, is_config=False),
            _MetaInfoClassMember('power-max-value', ATTRIBUTE, 'int', 'int32',
                None, None,
                [('-2147483648', '2147483647')], [],
                '''                Max Power Value of the Unit
                ''',
                'power_max_value',
                'Cisco-IOS-XR-asr9k-sc-envmon-admin-oper', False, is_config=False),
            _MetaInfoClassMember('power-unit-multiplier', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('0', '4294967295')], [],
                '''                Unit Multiplier of Power
                ''',
                'power_unit_multiplier',
                'Cisco-IOS-XR-asr9k-sc-envmon-admin-oper', False, is_config=False),
            _MetaInfoClassMember('power-accuracy', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('0', '4294967295')], [],
                '''                Accuracy of the Power Value
                ''',
                'power_accuracy',
                'Cisco-IOS-XR-asr9k-sc-envmon-admin-oper', False, is_config=False),
            _MetaInfoClassMember('power-measure-caliber', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('0', '4294967295')], [],
                '''                Measure Caliber
                ''',
                'power_measure_caliber',
                'Cisco-IOS-XR-asr9k-sc-envmon-admin-oper', False, is_config=False),
            _MetaInfoClassMember('power-current-type', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('0', '4294967295')], [],
                '''                Current Type of the Unit
                ''',
                'power_current_type',
                'Cisco-IOS-XR-asr9k-sc-envmon-admin-oper', False, is_config=False),
            _MetaInfoClassMember('power-origin', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('0', '4294967295')], [],
                '''                The Power Origin of the Unit
                ''',
                'power_origin',
                'Cisco-IOS-XR-asr9k-sc-envmon-admin-oper', False, is_config=False),
            _MetaInfoClassMember('power-admin-state', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('0', '4294967295')], [],
                '''                Admin Status of the Unit
                ''',
                'power_admin_state',
                'Cisco-IOS-XR-asr9k-sc-envmon-admin-oper', False, is_config=False),
            _MetaInfoClassMember('power-oper-state', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('0', '4294967295')], [],
                '''                Oper Status of the Unit
                ''',
                'power_oper_state',
                'Cisco-IOS-XR-asr9k-sc-envmon-admin-oper', False, is_config=False),
            _MetaInfoClassMember('power-state-enter-reason', ATTRIBUTE, 'str', 'string',
                None, None,
                [(0, 50)], [],
                '''                Enter Reason for the State
                ''',
                'power_state_enter_reason',
                'Cisco-IOS-XR-asr9k-sc-envmon-admin-oper', False, is_config=False),
            ],
            'Cisco-IOS-XR-asr9k-sc-envmon-admin-oper',
            'power-bag',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-asr9k-sc-envmon-admin-oper'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_envmon_admin_oper',
            is_config=False,
        ),
    },
    'EnvironmentalMonitoring.Racks.Rack.Slots.Slot.Modules.Module.Power' : {
        'meta_info' : _MetaInfoClass('EnvironmentalMonitoring.Racks.Rack.Slots.Slot.Modules.Module.Power', REFERENCE_CLASS,
            '''Module Power Draw''',
            False, 
            [
            _MetaInfoClassMember('power-bag', REFERENCE_CLASS, 'PowerBag', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_envmon_admin_oper', 'EnvironmentalMonitoring.Racks.Rack.Slots.Slot.Modules.Module.Power.PowerBag',
                [], [],
                '''                Detailed power bag information
                ''',
                'power_bag',
                'Cisco-IOS-XR-asr9k-sc-envmon-admin-oper', False, is_config=False),
            ],
            'Cisco-IOS-XR-asr9k-sc-envmon-admin-oper',
            'power',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-asr9k-sc-envmon-admin-oper'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_envmon_admin_oper',
            is_config=False,
        ),
    },
    'EnvironmentalMonitoring.Racks.Rack.Slots.Slot.Modules.Module' : {
        'meta_info' : _MetaInfoClass('EnvironmentalMonitoring.Racks.Rack.Slots.Slot.Modules.Module', REFERENCE_LIST,
            '''Name''',
            False, 
            [
            _MetaInfoClassMember('module', ATTRIBUTE, 'str', 'xr:Cisco-ios-xr-string',
                None, None,
                [], [b'[\\w\\-\\.:,_@#%$\\+=\\|;]+'],
                '''                Module name
                ''',
                'module',
                'Cisco-IOS-XR-asr9k-sc-envmon-admin-oper', True, is_config=False),
            _MetaInfoClassMember('sensor-types', REFERENCE_CLASS, 'SensorTypes', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_envmon_admin_oper', 'EnvironmentalMonitoring.Racks.Rack.Slots.Slot.Modules.Module.SensorTypes',
                [], [],
                '''                Table of sensor types
                ''',
                'sensor_types',
                'Cisco-IOS-XR-asr9k-sc-envmon-admin-oper', False, is_config=False),
            _MetaInfoClassMember('power', REFERENCE_CLASS, 'Power', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_envmon_admin_oper', 'EnvironmentalMonitoring.Racks.Rack.Slots.Slot.Modules.Module.Power',
                [], [],
                '''                Module Power Draw
                ''',
                'power',
                'Cisco-IOS-XR-asr9k-sc-envmon-admin-oper', False, is_config=False),
            ],
            'Cisco-IOS-XR-asr9k-sc-envmon-admin-oper',
            'module',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-asr9k-sc-envmon-admin-oper'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_envmon_admin_oper',
            is_config=False,
        ),
    },
    'EnvironmentalMonitoring.Racks.Rack.Slots.Slot.Modules' : {
        'meta_info' : _MetaInfoClass('EnvironmentalMonitoring.Racks.Rack.Slots.Slot.Modules', REFERENCE_CLASS,
            '''Table of modules''',
            False, 
            [
            _MetaInfoClassMember('module', REFERENCE_LIST, 'Module', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_envmon_admin_oper', 'EnvironmentalMonitoring.Racks.Rack.Slots.Slot.Modules.Module',
                [], [],
                '''                Name
                ''',
                'module',
                'Cisco-IOS-XR-asr9k-sc-envmon-admin-oper', False, is_config=False),
            ],
            'Cisco-IOS-XR-asr9k-sc-envmon-admin-oper',
            'modules',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-asr9k-sc-envmon-admin-oper'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_envmon_admin_oper',
            is_config=False,
        ),
    },
    'EnvironmentalMonitoring.Racks.Rack.Slots.Slot' : {
        'meta_info' : _MetaInfoClass('EnvironmentalMonitoring.Racks.Rack.Slots.Slot', REFERENCE_LIST,
            '''Name''',
            False, 
            [
            _MetaInfoClassMember('slot', ATTRIBUTE, 'str', 'xr:Cisco-ios-xr-string',
                None, None,
                [], [b'[\\w\\-\\.:,_@#%$\\+=\\|;]+'],
                '''                Slot name
                ''',
                'slot',
                'Cisco-IOS-XR-asr9k-sc-envmon-admin-oper', True, is_config=False),
            _MetaInfoClassMember('modules', REFERENCE_CLASS, 'Modules', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_envmon_admin_oper', 'EnvironmentalMonitoring.Racks.Rack.Slots.Slot.Modules',
                [], [],
                '''                Table of modules
                ''',
                'modules',
                'Cisco-IOS-XR-asr9k-sc-envmon-admin-oper', False, is_config=False),
            ],
            'Cisco-IOS-XR-asr9k-sc-envmon-admin-oper',
            'slot',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-asr9k-sc-envmon-admin-oper'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_envmon_admin_oper',
            is_config=False,
        ),
    },
    'EnvironmentalMonitoring.Racks.Rack.Slots' : {
        'meta_info' : _MetaInfoClass('EnvironmentalMonitoring.Racks.Rack.Slots', REFERENCE_CLASS,
            '''Table of slots''',
            False, 
            [
            _MetaInfoClassMember('slot', REFERENCE_LIST, 'Slot', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_envmon_admin_oper', 'EnvironmentalMonitoring.Racks.Rack.Slots.Slot',
                [], [],
                '''                Name
                ''',
                'slot',
                'Cisco-IOS-XR-asr9k-sc-envmon-admin-oper', False, is_config=False),
            ],
            'Cisco-IOS-XR-asr9k-sc-envmon-admin-oper',
            'slots',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-asr9k-sc-envmon-admin-oper'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_envmon_admin_oper',
            is_config=False,
        ),
    },
    'EnvironmentalMonitoring.Racks.Rack' : {
        'meta_info' : _MetaInfoClass('EnvironmentalMonitoring.Racks.Rack', REFERENCE_LIST,
            '''Number''',
            False, 
            [
            _MetaInfoClassMember('rack', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('0', '4294967295')], [],
                '''                Rack number
                ''',
                'rack',
                'Cisco-IOS-XR-asr9k-sc-envmon-admin-oper', True, is_config=False),
            _MetaInfoClassMember('slots', REFERENCE_CLASS, 'Slots', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_envmon_admin_oper', 'EnvironmentalMonitoring.Racks.Rack.Slots',
                [], [],
                '''                Table of slots
                ''',
                'slots',
                'Cisco-IOS-XR-asr9k-sc-envmon-admin-oper', False, is_config=False),
            ],
            'Cisco-IOS-XR-asr9k-sc-envmon-admin-oper',
            'rack',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-asr9k-sc-envmon-admin-oper'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_envmon_admin_oper',
            is_config=False,
        ),
    },
    'EnvironmentalMonitoring.Racks' : {
        'meta_info' : _MetaInfoClass('EnvironmentalMonitoring.Racks', REFERENCE_CLASS,
            '''Table of racks''',
            False, 
            [
            _MetaInfoClassMember('rack', REFERENCE_LIST, 'Rack', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_envmon_admin_oper', 'EnvironmentalMonitoring.Racks.Rack',
                [], [],
                '''                Number
                ''',
                'rack',
                'Cisco-IOS-XR-asr9k-sc-envmon-admin-oper', False, is_config=False),
            ],
            'Cisco-IOS-XR-asr9k-sc-envmon-admin-oper',
            'racks',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-asr9k-sc-envmon-admin-oper'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_envmon_admin_oper',
            is_config=False,
        ),
    },
    'EnvironmentalMonitoring' : {
        'meta_info' : _MetaInfoClass('EnvironmentalMonitoring', REFERENCE_CLASS,
            '''Admin Environmental Monitoring Operational data
space''',
            False, 
            [
            _MetaInfoClassMember('racks', REFERENCE_CLASS, 'Racks', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_envmon_admin_oper', 'EnvironmentalMonitoring.Racks',
                [], [],
                '''                Table of racks
                ''',
                'racks',
                'Cisco-IOS-XR-asr9k-sc-envmon-admin-oper', False, is_config=False),
            ],
            'Cisco-IOS-XR-asr9k-sc-envmon-admin-oper',
            'environmental-monitoring',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-asr9k-sc-envmon-admin-oper'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_envmon_admin_oper',
            is_config=False,
        ),
    },
}
_meta_table['EnvironmentalMonitoring.Racks.Rack.Slots.Slot.Modules.Module.SensorTypes.SensorType.SensorNames.SensorName.Thresholds.Threshold.ValueDetailed']['meta_info'].parent =_meta_table['EnvironmentalMonitoring.Racks.Rack.Slots.Slot.Modules.Module.SensorTypes.SensorType.SensorNames.SensorName.Thresholds.Threshold']['meta_info']
_meta_table['EnvironmentalMonitoring.Racks.Rack.Slots.Slot.Modules.Module.SensorTypes.SensorType.SensorNames.SensorName.Thresholds.Threshold']['meta_info'].parent =_meta_table['EnvironmentalMonitoring.Racks.Rack.Slots.Slot.Modules.Module.SensorTypes.SensorType.SensorNames.SensorName.Thresholds']['meta_info']
_meta_table['EnvironmentalMonitoring.Racks.Rack.Slots.Slot.Modules.Module.SensorTypes.SensorType.SensorNames.SensorName.Thresholds']['meta_info'].parent =_meta_table['EnvironmentalMonitoring.Racks.Rack.Slots.Slot.Modules.Module.SensorTypes.SensorType.SensorNames.SensorName']['meta_info']
_meta_table['EnvironmentalMonitoring.Racks.Rack.Slots.Slot.Modules.Module.SensorTypes.SensorType.SensorNames.SensorName.ValueDetailed']['meta_info'].parent =_meta_table['EnvironmentalMonitoring.Racks.Rack.Slots.Slot.Modules.Module.SensorTypes.SensorType.SensorNames.SensorName']['meta_info']
_meta_table['EnvironmentalMonitoring.Racks.Rack.Slots.Slot.Modules.Module.SensorTypes.SensorType.SensorNames.SensorName']['meta_info'].parent =_meta_table['EnvironmentalMonitoring.Racks.Rack.Slots.Slot.Modules.Module.SensorTypes.SensorType.SensorNames']['meta_info']
_meta_table['EnvironmentalMonitoring.Racks.Rack.Slots.Slot.Modules.Module.SensorTypes.SensorType.SensorNames']['meta_info'].parent =_meta_table['EnvironmentalMonitoring.Racks.Rack.Slots.Slot.Modules.Module.SensorTypes.SensorType']['meta_info']
_meta_table['EnvironmentalMonitoring.Racks.Rack.Slots.Slot.Modules.Module.SensorTypes.SensorType']['meta_info'].parent =_meta_table['EnvironmentalMonitoring.Racks.Rack.Slots.Slot.Modules.Module.SensorTypes']['meta_info']
_meta_table['EnvironmentalMonitoring.Racks.Rack.Slots.Slot.Modules.Module.Power.PowerBag']['meta_info'].parent =_meta_table['EnvironmentalMonitoring.Racks.Rack.Slots.Slot.Modules.Module.Power']['meta_info']
_meta_table['EnvironmentalMonitoring.Racks.Rack.Slots.Slot.Modules.Module.SensorTypes']['meta_info'].parent =_meta_table['EnvironmentalMonitoring.Racks.Rack.Slots.Slot.Modules.Module']['meta_info']
_meta_table['EnvironmentalMonitoring.Racks.Rack.Slots.Slot.Modules.Module.Power']['meta_info'].parent =_meta_table['EnvironmentalMonitoring.Racks.Rack.Slots.Slot.Modules.Module']['meta_info']
_meta_table['EnvironmentalMonitoring.Racks.Rack.Slots.Slot.Modules.Module']['meta_info'].parent =_meta_table['EnvironmentalMonitoring.Racks.Rack.Slots.Slot.Modules']['meta_info']
_meta_table['EnvironmentalMonitoring.Racks.Rack.Slots.Slot.Modules']['meta_info'].parent =_meta_table['EnvironmentalMonitoring.Racks.Rack.Slots.Slot']['meta_info']
_meta_table['EnvironmentalMonitoring.Racks.Rack.Slots.Slot']['meta_info'].parent =_meta_table['EnvironmentalMonitoring.Racks.Rack.Slots']['meta_info']
_meta_table['EnvironmentalMonitoring.Racks.Rack.Slots']['meta_info'].parent =_meta_table['EnvironmentalMonitoring.Racks.Rack']['meta_info']
_meta_table['EnvironmentalMonitoring.Racks.Rack']['meta_info'].parent =_meta_table['EnvironmentalMonitoring.Racks']['meta_info']
_meta_table['EnvironmentalMonitoring.Racks']['meta_info'].parent =_meta_table['EnvironmentalMonitoring']['meta_info']
