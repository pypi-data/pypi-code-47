
'''
This is auto-generated file,
which includes metadata for module Cisco_IOS_XR_perf_meas_cfg
'''

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_LIST, REFERENCE_LEAFLIST, REFERENCE_BITS, REFERENCE_UNION
from ydk._core._dm_meta_info import REFERENCE_CLASS, REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, ANYXML_CLASS
from ydk._core._importer import _yang_ns

_meta_table = {
    'PerformanceMeasurement.DelayProfileInterface.Advertisement.Accelerated' : {
        'meta_info' : _MetaInfoClass('PerformanceMeasurement.DelayProfileInterface.Advertisement.Accelerated', REFERENCE_CLASS,
            '''Accelerated Advertisement Profile''',
            False, 
            [
            _MetaInfoClassMember('threshold', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('0', '100')], [],
                '''                Accelerated advertisement threshold
                percentage
                ''',
                'threshold',
                'Cisco-IOS-XR-perf-meas-cfg', False, default_value="20"),
            _MetaInfoClassMember('minimum-change', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('0', '100000')], [],
                '''                Accelerated advertisement minimum value in
                uSec
                ''',
                'minimum_change',
                'Cisco-IOS-XR-perf-meas-cfg', False, default_value="500"),
            _MetaInfoClassMember('enable', ATTRIBUTE, 'Empty', 'empty',
                None, None,
                [], [],
                '''                Enable Accelerated Advertisement
                ''',
                'enable',
                'Cisco-IOS-XR-perf-meas-cfg', False),
            ],
            'Cisco-IOS-XR-perf-meas-cfg',
            'accelerated',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-perf-meas-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_perf_meas_cfg',
        ),
    },
    'PerformanceMeasurement.DelayProfileInterface.Advertisement.Periodic' : {
        'meta_info' : _MetaInfoClass('PerformanceMeasurement.DelayProfileInterface.Advertisement.Periodic', REFERENCE_CLASS,
            '''Periodic Advertisement Profile''',
            False, 
            [
            _MetaInfoClassMember('interval', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('30', '3600')], [],
                '''                Periodic advertisement interval in seconds
                ''',
                'interval',
                'Cisco-IOS-XR-perf-meas-cfg', False, default_value="120"),
            _MetaInfoClassMember('threshold', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('0', '100')], [],
                '''                Periodic advertisement threshold percentage
                ''',
                'threshold',
                'Cisco-IOS-XR-perf-meas-cfg', False, default_value="10"),
            _MetaInfoClassMember('minimum-change', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('0', '100000')], [],
                '''                Periodic advertisement minimum value in uSec
                ''',
                'minimum_change',
                'Cisco-IOS-XR-perf-meas-cfg', False, default_value="500"),
            _MetaInfoClassMember('disable', ATTRIBUTE, 'Empty', 'empty',
                None, None,
                [], [],
                '''                Enable Performance Measurement Periodic
                Advertisement
                ''',
                'disable',
                'Cisco-IOS-XR-perf-meas-cfg', False),
            ],
            'Cisco-IOS-XR-perf-meas-cfg',
            'periodic',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-perf-meas-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_perf_meas_cfg',
        ),
    },
    'PerformanceMeasurement.DelayProfileInterface.Advertisement' : {
        'meta_info' : _MetaInfoClass('PerformanceMeasurement.DelayProfileInterface.Advertisement', REFERENCE_CLASS,
            '''Advertisement Profile''',
            False, 
            [
            _MetaInfoClassMember('accelerated', REFERENCE_CLASS, 'Accelerated', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_perf_meas_cfg', 'PerformanceMeasurement.DelayProfileInterface.Advertisement.Accelerated',
                [], [],
                '''                Accelerated Advertisement Profile
                ''',
                'accelerated',
                'Cisco-IOS-XR-perf-meas-cfg', False),
            _MetaInfoClassMember('periodic', REFERENCE_CLASS, 'Periodic', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_perf_meas_cfg', 'PerformanceMeasurement.DelayProfileInterface.Advertisement.Periodic',
                [], [],
                '''                Periodic Advertisement Profile
                ''',
                'periodic',
                'Cisco-IOS-XR-perf-meas-cfg', False),
            ],
            'Cisco-IOS-XR-perf-meas-cfg',
            'advertisement',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-perf-meas-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_perf_meas_cfg',
        ),
    },
    'PerformanceMeasurement.DelayProfileInterface.Probe.Burst' : {
        'meta_info' : _MetaInfoClass('PerformanceMeasurement.DelayProfileInterface.Probe.Burst', REFERENCE_CLASS,
            '''PM Delay Profile Probe Burst''',
            False, 
            [
            _MetaInfoClassMember('count', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('1', '30')], [],
                '''                The value for delay profile probe burst count
                ''',
                'count',
                'Cisco-IOS-XR-perf-meas-cfg', False, default_value="10"),
            _MetaInfoClassMember('interval', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('30', '15000')], [],
                '''                The value for delay profile probe burst
                interval
                ''',
                'interval',
                'Cisco-IOS-XR-perf-meas-cfg', False, default_value="3000"),
            ],
            'Cisco-IOS-XR-perf-meas-cfg',
            'burst',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-perf-meas-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_perf_meas_cfg',
        ),
    },
    'PerformanceMeasurement.DelayProfileInterface.Probe' : {
        'meta_info' : _MetaInfoClass('PerformanceMeasurement.DelayProfileInterface.Probe', REFERENCE_CLASS,
            '''PM Delay Profile Probe''',
            False, 
            [
            _MetaInfoClassMember('burst', REFERENCE_CLASS, 'Burst', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_perf_meas_cfg', 'PerformanceMeasurement.DelayProfileInterface.Probe.Burst',
                [], [],
                '''                PM Delay Profile Probe Burst
                ''',
                'burst',
                'Cisco-IOS-XR-perf-meas-cfg', False),
            _MetaInfoClassMember('one-way-measurement', ATTRIBUTE, 'Empty', 'empty',
                None, None,
                [], [],
                '''                Enable one-way measurement
                ''',
                'one_way_measurement',
                'Cisco-IOS-XR-perf-meas-cfg', False),
            _MetaInfoClassMember('interval', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('30', '3600')], [],
                '''                The value for delay profile probe interval in
                seconds
                ''',
                'interval',
                'Cisco-IOS-XR-perf-meas-cfg', False, default_value="30"),
            ],
            'Cisco-IOS-XR-perf-meas-cfg',
            'probe',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-perf-meas-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_perf_meas_cfg',
        ),
    },
    'PerformanceMeasurement.DelayProfileInterface' : {
        'meta_info' : _MetaInfoClass('PerformanceMeasurement.DelayProfileInterface', REFERENCE_CLASS,
            '''PM Delay Profile''',
            False, 
            [
            _MetaInfoClassMember('advertisement', REFERENCE_CLASS, 'Advertisement', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_perf_meas_cfg', 'PerformanceMeasurement.DelayProfileInterface.Advertisement',
                [], [],
                '''                Advertisement Profile
                ''',
                'advertisement',
                'Cisco-IOS-XR-perf-meas-cfg', False),
            _MetaInfoClassMember('probe', REFERENCE_CLASS, 'Probe', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_perf_meas_cfg', 'PerformanceMeasurement.DelayProfileInterface.Probe',
                [], [],
                '''                PM Delay Profile Probe
                ''',
                'probe',
                'Cisco-IOS-XR-perf-meas-cfg', False),
            ],
            'Cisco-IOS-XR-perf-meas-cfg',
            'delay-profile-interface',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-perf-meas-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_perf_meas_cfg',
        ),
    },
    'PerformanceMeasurement.Interfaces.Interface.DelayMeasurement' : {
        'meta_info' : _MetaInfoClass('PerformanceMeasurement.Interfaces.Interface.DelayMeasurement', REFERENCE_CLASS,
            '''Interface delay measurement''',
            False, 
            [
            _MetaInfoClassMember('enable-delay-measurement', ATTRIBUTE, 'Empty', 'empty',
                None, None,
                [], [],
                '''                Enable interface delay measurement
                ''',
                'enable_delay_measurement',
                'Cisco-IOS-XR-perf-meas-cfg', False),
            _MetaInfoClassMember('advertise-delay', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('0', '16777215')], [],
                '''                The value for interface delay measurement
                advertisement delay in uSec
                ''',
                'advertise_delay',
                'Cisco-IOS-XR-perf-meas-cfg', False),
            ],
            'Cisco-IOS-XR-perf-meas-cfg',
            'delay-measurement',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-perf-meas-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_perf_meas_cfg',
        ),
    },
    'PerformanceMeasurement.Interfaces.Interface' : {
        'meta_info' : _MetaInfoClass('PerformanceMeasurement.Interfaces.Interface', REFERENCE_LIST,
            '''Configure a performance-measurement interface''',
            False, 
            [
            _MetaInfoClassMember('interface-name', ATTRIBUTE, 'str', 'xr:Interface-name',
                None, None,
                [], [b'[a-zA-Z0-9._/-]+'],
                '''                Interface name
                ''',
                'interface_name',
                'Cisco-IOS-XR-perf-meas-cfg', True),
            _MetaInfoClassMember('delay-measurement', REFERENCE_CLASS, 'DelayMeasurement', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_perf_meas_cfg', 'PerformanceMeasurement.Interfaces.Interface.DelayMeasurement',
                [], [],
                '''                Interface delay measurement
                ''',
                'delay_measurement',
                'Cisco-IOS-XR-perf-meas-cfg', False),
            _MetaInfoClassMember('enable-interface', ATTRIBUTE, 'Empty', 'empty',
                None, None,
                [], [],
                '''                Enable interface submode
                ''',
                'enable_interface',
                'Cisco-IOS-XR-perf-meas-cfg', False),
            ],
            'Cisco-IOS-XR-perf-meas-cfg',
            'interface',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-perf-meas-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_perf_meas_cfg',
        ),
    },
    'PerformanceMeasurement.Interfaces' : {
        'meta_info' : _MetaInfoClass('PerformanceMeasurement.Interfaces', REFERENCE_CLASS,
            '''Configure performance-measurement interfaces''',
            False, 
            [
            _MetaInfoClassMember('interface', REFERENCE_LIST, 'Interface', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_perf_meas_cfg', 'PerformanceMeasurement.Interfaces.Interface',
                [], [],
                '''                Configure a performance-measurement interface
                ''',
                'interface',
                'Cisco-IOS-XR-perf-meas-cfg', False),
            ],
            'Cisco-IOS-XR-perf-meas-cfg',
            'interfaces',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-perf-meas-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_perf_meas_cfg',
        ),
    },
    'PerformanceMeasurement' : {
        'meta_info' : _MetaInfoClass('PerformanceMeasurement', REFERENCE_CLASS,
            '''The root of performance-measurement configuration''',
            False, 
            [
            _MetaInfoClassMember('delay-profile-interface', REFERENCE_CLASS, 'DelayProfileInterface', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_perf_meas_cfg', 'PerformanceMeasurement.DelayProfileInterface',
                [], [],
                '''                PM Delay Profile
                ''',
                'delay_profile_interface',
                'Cisco-IOS-XR-perf-meas-cfg', False),
            _MetaInfoClassMember('interfaces', REFERENCE_CLASS, 'Interfaces', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_perf_meas_cfg', 'PerformanceMeasurement.Interfaces',
                [], [],
                '''                Configure performance-measurement interfaces
                ''',
                'interfaces',
                'Cisco-IOS-XR-perf-meas-cfg', False),
            _MetaInfoClassMember('enable-performance-measurement', ATTRIBUTE, 'Empty', 'empty',
                None, None,
                [], [],
                '''                Enable the performance measurement feature
                ''',
                'enable_performance_measurement',
                'Cisco-IOS-XR-perf-meas-cfg', False),
            ],
            'Cisco-IOS-XR-perf-meas-cfg',
            'performance-measurement',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-perf-meas-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_perf_meas_cfg',
        ),
    },
}
_meta_table['PerformanceMeasurement.DelayProfileInterface.Advertisement.Accelerated']['meta_info'].parent =_meta_table['PerformanceMeasurement.DelayProfileInterface.Advertisement']['meta_info']
_meta_table['PerformanceMeasurement.DelayProfileInterface.Advertisement.Periodic']['meta_info'].parent =_meta_table['PerformanceMeasurement.DelayProfileInterface.Advertisement']['meta_info']
_meta_table['PerformanceMeasurement.DelayProfileInterface.Probe.Burst']['meta_info'].parent =_meta_table['PerformanceMeasurement.DelayProfileInterface.Probe']['meta_info']
_meta_table['PerformanceMeasurement.DelayProfileInterface.Advertisement']['meta_info'].parent =_meta_table['PerformanceMeasurement.DelayProfileInterface']['meta_info']
_meta_table['PerformanceMeasurement.DelayProfileInterface.Probe']['meta_info'].parent =_meta_table['PerformanceMeasurement.DelayProfileInterface']['meta_info']
_meta_table['PerformanceMeasurement.Interfaces.Interface.DelayMeasurement']['meta_info'].parent =_meta_table['PerformanceMeasurement.Interfaces.Interface']['meta_info']
_meta_table['PerformanceMeasurement.Interfaces.Interface']['meta_info'].parent =_meta_table['PerformanceMeasurement.Interfaces']['meta_info']
_meta_table['PerformanceMeasurement.DelayProfileInterface']['meta_info'].parent =_meta_table['PerformanceMeasurement']['meta_info']
_meta_table['PerformanceMeasurement.Interfaces']['meta_info'].parent =_meta_table['PerformanceMeasurement']['meta_info']
