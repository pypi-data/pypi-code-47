
'''
This is auto-generated file,
which includes metadata for module Cisco_IOS_XR_infra_sla_cfg
'''

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_LIST, REFERENCE_LEAFLIST, REFERENCE_BITS, REFERENCE_UNION
from ydk._core._dm_meta_info import REFERENCE_CLASS, REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, ANYXML_CLASS
from ydk._core._importer import _yang_ns

_meta_table = {
    'Sla.Protocols.Ethernet.Profiles.Profile.Statistics.Statistic.BucketsSize' : {
        'meta_info' : _MetaInfoClass('Sla.Protocols.Ethernet.Profiles.Profile.Statistics.Statistic.BucketsSize', REFERENCE_CLASS,
            '''Size of the buckets into which statistics
are collected''',
            False, 
            [
            _MetaInfoClassMember('buckets-size', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('1', '100')], [],
                '''                Size of each bucket
                ''',
                'buckets_size',
                'Cisco-IOS-XR-ethernet-cfm-cfg', False, is_mandatory=True),
            _MetaInfoClassMember('buckets-size-unit', REFERENCE_ENUM_CLASS, 'SlaBucketsSizeUnitsEnum', 'dt2:Sla-buckets-size-units-enum',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_sla_datatypes', 'SlaBucketsSizeUnitsEnum',
                [], [],
                '''                Unit associated with the BucketsSize
                ''',
                'buckets_size_unit',
                'Cisco-IOS-XR-ethernet-cfm-cfg', False, is_mandatory=True),
            ],
            'Cisco-IOS-XR-ethernet-cfm-cfg',
            'buckets-size',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-ethernet-cfm-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_sla_cfg',
            is_presence=True,
        ),
    },
    'Sla.Protocols.Ethernet.Profiles.Profile.Statistics.Statistic.Actions.Action' : {
        'meta_info' : _MetaInfoClass('Sla.Protocols.Ethernet.Profiles.Profile.Statistics.Statistic.Actions.Action', REFERENCE_LIST,
            '''Action to perform when the threshold is
crossed''',
            False, 
            [
            _MetaInfoClassMember('threshold-type', REFERENCE_ENUM_CLASS, 'SlaThresholdTypeEnum', 'dt2:Sla-threshold-type-enum',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_sla_datatypes', 'SlaThresholdTypeEnum',
                [], [],
                '''                Threshold type
                ''',
                'threshold_type',
                'Cisco-IOS-XR-ethernet-cfm-cfg', True),
            _MetaInfoClassMember('action-type', REFERENCE_ENUM_CLASS, 'SlaActionTypeEnum', 'dt2:Sla-action-type-enum',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_sla_datatypes', 'SlaActionTypeEnum',
                [], [],
                '''                Action to take when the threshold is
                crossed
                ''',
                'action_type',
                'Cisco-IOS-XR-ethernet-cfm-cfg', True),
            _MetaInfoClassMember('condition', REFERENCE_ENUM_CLASS, 'SlaThresholdConditionEnum', 'dt2:Sla-threshold-condition-enum',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_sla_datatypes', 'SlaThresholdConditionEnum',
                [], [],
                '''                Condition to be met to consider the
                threshold crossed
                ''',
                'condition',
                'Cisco-IOS-XR-ethernet-cfm-cfg', True),
            _MetaInfoClassMember('threshold-value', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('1', '2147483647')], [],
                '''                Threshold Value
                ''',
                'threshold_value',
                'Cisco-IOS-XR-ethernet-cfm-cfg', False, is_mandatory=True),
            _MetaInfoClassMember('bin-number', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('2', '100')], [],
                '''                Bin number in-and-above which samples
                contribute towards a sample-count
                threshold (required only when Condition
                is SampleCount)
                ''',
                'bin_number',
                'Cisco-IOS-XR-ethernet-cfm-cfg', False),
            ],
            'Cisco-IOS-XR-ethernet-cfm-cfg',
            'action',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-ethernet-cfm-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_sla_cfg',
        ),
    },
    'Sla.Protocols.Ethernet.Profiles.Profile.Statistics.Statistic.Actions' : {
        'meta_info' : _MetaInfoClass('Sla.Protocols.Ethernet.Profiles.Profile.Statistics.Statistic.Actions', REFERENCE_CLASS,
            '''Thresholds and associated actions for the
given statistics type''',
            False, 
            [
            _MetaInfoClassMember('action', REFERENCE_LIST, 'Action', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_sla_cfg', 'Sla.Protocols.Ethernet.Profiles.Profile.Statistics.Statistic.Actions.Action',
                [], [],
                '''                Action to perform when the threshold is
                crossed
                ''',
                'action',
                'Cisco-IOS-XR-ethernet-cfm-cfg', False),
            ],
            'Cisco-IOS-XR-ethernet-cfm-cfg',
            'actions',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-ethernet-cfm-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_sla_cfg',
        ),
    },
    'Sla.Protocols.Ethernet.Profiles.Profile.Statistics.Statistic.Aggregation' : {
        'meta_info' : _MetaInfoClass('Sla.Protocols.Ethernet.Profiles.Profile.Statistics.Statistic.Aggregation', REFERENCE_CLASS,
            '''Aggregation to apply to results for the
statistic''',
            False, 
            [
            _MetaInfoClassMember('bins-count', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('0', '100')], [],
                '''                Number of bins to aggregate results into
                (0 for no aggregation)
                ''',
                'bins_count',
                'Cisco-IOS-XR-ethernet-cfm-cfg', False, is_mandatory=True),
            _MetaInfoClassMember('bins-width', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('1', '10000')], [],
                '''                Width of each bin
                ''',
                'bins_width',
                'Cisco-IOS-XR-ethernet-cfm-cfg', False, is_mandatory=True),
            _MetaInfoClassMember('bins-width-tenths', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('0', '9')], [],
                '''                Tenths portion of the bin width
                ''',
                'bins_width_tenths',
                'Cisco-IOS-XR-ethernet-cfm-cfg', False),
            ],
            'Cisco-IOS-XR-ethernet-cfm-cfg',
            'aggregation',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-ethernet-cfm-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_sla_cfg',
            is_presence=True,
        ),
    },
    'Sla.Protocols.Ethernet.Profiles.Profile.Statistics.Statistic' : {
        'meta_info' : _MetaInfoClass('Sla.Protocols.Ethernet.Profiles.Profile.Statistics.Statistic', REFERENCE_LIST,
            '''Type of statistic''',
            False, 
            [
            _MetaInfoClassMember('statistic-name', REFERENCE_ENUM_CLASS, 'SlaStatisticTypeEnum', 'dt2:Sla-statistic-type-enum',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_sla_datatypes', 'SlaStatisticTypeEnum',
                [], [],
                '''                The type of statistic to measure
                ''',
                'statistic_name',
                'Cisco-IOS-XR-ethernet-cfm-cfg', True),
            _MetaInfoClassMember('buckets-size', REFERENCE_CLASS, 'BucketsSize', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_sla_cfg', 'Sla.Protocols.Ethernet.Profiles.Profile.Statistics.Statistic.BucketsSize',
                [], [],
                '''                Size of the buckets into which statistics
                are collected
                ''',
                'buckets_size',
                'Cisco-IOS-XR-ethernet-cfm-cfg', False, is_presence=True),
            _MetaInfoClassMember('actions', REFERENCE_CLASS, 'Actions', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_sla_cfg', 'Sla.Protocols.Ethernet.Profiles.Profile.Statistics.Statistic.Actions',
                [], [],
                '''                Thresholds and associated actions for the
                given statistics type
                ''',
                'actions',
                'Cisco-IOS-XR-ethernet-cfm-cfg', False),
            _MetaInfoClassMember('aggregation', REFERENCE_CLASS, 'Aggregation', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_sla_cfg', 'Sla.Protocols.Ethernet.Profiles.Profile.Statistics.Statistic.Aggregation',
                [], [],
                '''                Aggregation to apply to results for the
                statistic
                ''',
                'aggregation',
                'Cisco-IOS-XR-ethernet-cfm-cfg', False, is_presence=True),
            _MetaInfoClassMember('enable', ATTRIBUTE, 'Empty', 'empty',
                None, None,
                [], [],
                '''                Enable statistic gathering of the metric
                ''',
                'enable',
                'Cisco-IOS-XR-ethernet-cfm-cfg', False),
            _MetaInfoClassMember('buckets-archive', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('1', '100')], [],
                '''                Number of buckets to archive in memory
                ''',
                'buckets_archive',
                'Cisco-IOS-XR-ethernet-cfm-cfg', False),
            ],
            'Cisco-IOS-XR-ethernet-cfm-cfg',
            'statistic',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-ethernet-cfm-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_sla_cfg',
        ),
    },
    'Sla.Protocols.Ethernet.Profiles.Profile.Statistics' : {
        'meta_info' : _MetaInfoClass('Sla.Protocols.Ethernet.Profiles.Profile.Statistics', REFERENCE_CLASS,
            '''Statistics configuration for the SLA profile''',
            False, 
            [
            _MetaInfoClassMember('statistic', REFERENCE_LIST, 'Statistic', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_sla_cfg', 'Sla.Protocols.Ethernet.Profiles.Profile.Statistics.Statistic',
                [], [],
                '''                Type of statistic
                ''',
                'statistic',
                'Cisco-IOS-XR-ethernet-cfm-cfg', False),
            ],
            'Cisco-IOS-XR-ethernet-cfm-cfg',
            'statistics',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-ethernet-cfm-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_sla_cfg',
        ),
    },
    'Sla.Protocols.Ethernet.Profiles.Profile.Schedule' : {
        'meta_info' : _MetaInfoClass('Sla.Protocols.Ethernet.Profiles.Profile.Schedule', REFERENCE_CLASS,
            '''Schedule to use for probes within an
operation''',
            False, 
            [
            _MetaInfoClassMember('probe-interval', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('1', '90')], [],
                '''                Interval between probes.  This must be
                specified if, and only if, ProbeIntervalUnit
                is not 'Week' or 'Day'.
                ''',
                'probe_interval',
                'Cisco-IOS-XR-ethernet-cfm-cfg', False),
            _MetaInfoClassMember('probe-interval-day', REFERENCE_ENUM_CLASS, 'SlaProbeIntervalDayEnum', 'dt2:Sla-probe-interval-day-enum',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_sla_datatypes', 'SlaProbeIntervalDayEnum',
                [], [],
                '''                Day of week on which to schedule probes.
                This must be specified if, and only if,
                ProbeIntervalUnit is 'Week'.
                ''',
                'probe_interval_day',
                'Cisco-IOS-XR-ethernet-cfm-cfg', False),
            _MetaInfoClassMember('probe-interval-unit', REFERENCE_ENUM_CLASS, 'SlaProbeIntervalUnitsEnum', 'dt2:Sla-probe-interval-units-enum',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_sla_datatypes', 'SlaProbeIntervalUnitsEnum',
                [], [],
                '''                Time unit associated with the ProbeInterval.
                The value must not be 'Once'.  If 'Week' or
                'Day' is specified, probes are scheduled
                weekly or daily respectively.
                ''',
                'probe_interval_unit',
                'Cisco-IOS-XR-ethernet-cfm-cfg', False, is_mandatory=True),
            _MetaInfoClassMember('start-time-hour', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('0', '23')], [],
                '''                Time after midnight (in UTC) to send the
                first packet each day.
                ''',
                'start_time_hour',
                'Cisco-IOS-XR-ethernet-cfm-cfg', False),
            _MetaInfoClassMember('start-time-minute', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('0', '59')], [],
                '''                Time after midnight (in UTC) to send the
                first packet each day. This must be
                specified if, and only if, StartTimeHour is
                specified.
                ''',
                'start_time_minute',
                'Cisco-IOS-XR-ethernet-cfm-cfg', False),
            _MetaInfoClassMember('start-time-second', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('0', '59')], [],
                '''                Time after midnight (in UTC) to send the
                first packet each day. This must only be
                specified if StartTimeHour is specified, and
                must not be specified if ProbeIntervalUnit
                is 'Week' or 'Day'.
                ''',
                'start_time_second',
                'Cisco-IOS-XR-ethernet-cfm-cfg', False),
            _MetaInfoClassMember('probe-duration', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('1', '3600')], [],
                '''                Duration of each probe.  This must be
                specified if, and only if, ProbeDurationUnit
                is specified.
                ''',
                'probe_duration',
                'Cisco-IOS-XR-ethernet-cfm-cfg', False),
            _MetaInfoClassMember('probe-duration-unit', REFERENCE_ENUM_CLASS, 'SlaProbeDurationUnitsEnum', 'dt2:Sla-probe-duration-units-enum',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_sla_datatypes', 'SlaProbeDurationUnitsEnum',
                [], [],
                '''                Time unit associated with the ProbeDuration.
                The value must not be 'Once'.
                ''',
                'probe_duration_unit',
                'Cisco-IOS-XR-ethernet-cfm-cfg', False),
            ],
            'Cisco-IOS-XR-ethernet-cfm-cfg',
            'schedule',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-ethernet-cfm-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_sla_cfg',
            is_presence=True,
        ),
    },
    'Sla.Protocols.Ethernet.Profiles.Profile.Probe.Send' : {
        'meta_info' : _MetaInfoClass('Sla.Protocols.Ethernet.Profiles.Profile.Probe.Send', REFERENCE_CLASS,
            '''Schedule to use for packets within a burst.
The default value is to send a single packet
once.''',
            False, 
            [
            _MetaInfoClassMember('burst-interval', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('1', '3600')], [],
                '''                Interval between bursts.  This must be
                specified if, and only if, the SendType is
                'Burst' and the 'BurstIntervalUnit' is not
                'Once'.
                ''',
                'burst_interval',
                'Cisco-IOS-XR-ethernet-cfm-cfg', False),
            _MetaInfoClassMember('burst-interval-unit', REFERENCE_ENUM_CLASS, 'SlaBurstIntervalUnitsEnum', 'dt2:Sla-burst-interval-units-enum',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_sla_datatypes', 'SlaBurstIntervalUnitsEnum',
                [], [],
                '''                Time unit associated with the BurstInterval
                .  This must be specified if, and only if,
                SendType is 'Burst'.
                ''',
                'burst_interval_unit',
                'Cisco-IOS-XR-ethernet-cfm-cfg', False),
            _MetaInfoClassMember('packet-interval', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('1', '30000')], [],
                '''                Interval between packets.  This must be
                specified if, and only if,
                PacketIntervalUnit is not 'Once'.
                ''',
                'packet_interval',
                'Cisco-IOS-XR-ethernet-cfm-cfg', False),
            _MetaInfoClassMember('packet-interval-unit', REFERENCE_ENUM_CLASS, 'SlaPacketIntervalUnitsEnum', 'dt2:Sla-packet-interval-units-enum',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_sla_datatypes', 'SlaPacketIntervalUnitsEnum',
                [], [],
                '''                Time unit associated with the
                PacketInterval
                ''',
                'packet_interval_unit',
                'Cisco-IOS-XR-ethernet-cfm-cfg', False, is_mandatory=True),
            _MetaInfoClassMember('packet-count', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('2', '1200')], [],
                '''                The number of packets in each burst.  This
                must be specified if, and only if, the
                SendType is 'Burst'.
                ''',
                'packet_count',
                'Cisco-IOS-XR-ethernet-cfm-cfg', False),
            _MetaInfoClassMember('send-type', REFERENCE_ENUM_CLASS, 'SlaSend', 'dt2:Sla-send',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_sla_datatypes', 'SlaSend',
                [], [],
                '''                The packet distribution: single packets or
                bursts of packets.  If 'Burst' is specified
                , PacketCount and BurstInterval must be
                specified.
                ''',
                'send_type',
                'Cisco-IOS-XR-ethernet-cfm-cfg', False, is_mandatory=True),
            ],
            'Cisco-IOS-XR-ethernet-cfm-cfg',
            'send',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-ethernet-cfm-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_sla_cfg',
            is_presence=True,
        ),
    },
    'Sla.Protocols.Ethernet.Profiles.Profile.Probe.PacketSizeAndPadding' : {
        'meta_info' : _MetaInfoClass('Sla.Protocols.Ethernet.Profiles.Profile.Probe.PacketSizeAndPadding', REFERENCE_CLASS,
            '''Minimum size to pad outgoing packet to''',
            False, 
            [
            _MetaInfoClassMember('size', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('1', '9000')], [],
                '''                Minimum size to pad outgoing packet to
                ''',
                'size',
                'Cisco-IOS-XR-ethernet-cfm-cfg', False, is_mandatory=True),
            _MetaInfoClassMember('padding-type', REFERENCE_ENUM_CLASS, 'SlaPaddingPattern', 'dt2:Sla-padding-pattern',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_sla_datatypes', 'SlaPaddingPattern',
                [], [],
                '''                Type of padding to be used for the packet
                ''',
                'padding_type',
                'Cisco-IOS-XR-ethernet-cfm-cfg', False),
            _MetaInfoClassMember('padding-value', ATTRIBUTE, 'str', 'xr:Hex-integer',
                None, None,
                [], [b'[0-9a-fA-F]{1,8}'],
                '''                Pattern to be used for hex padding. This
                can be specified if, and only if, the
                PaddingType is 'Hex'.
                ''',
                'padding_value',
                'Cisco-IOS-XR-ethernet-cfm-cfg', False),
            ],
            'Cisco-IOS-XR-ethernet-cfm-cfg',
            'packet-size-and-padding',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-ethernet-cfm-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_sla_cfg',
            is_presence=True,
        ),
    },
    'Sla.Protocols.Ethernet.Profiles.Profile.Probe' : {
        'meta_info' : _MetaInfoClass('Sla.Protocols.Ethernet.Profiles.Profile.Probe', REFERENCE_CLASS,
            '''Probe configuration for the SLA profile''',
            False, 
            [
            _MetaInfoClassMember('send', REFERENCE_CLASS, 'Send', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_sla_cfg', 'Sla.Protocols.Ethernet.Profiles.Profile.Probe.Send',
                [], [],
                '''                Schedule to use for packets within a burst.
                The default value is to send a single packet
                once.
                ''',
                'send',
                'Cisco-IOS-XR-ethernet-cfm-cfg', False, is_presence=True),
            _MetaInfoClassMember('packet-size-and-padding', REFERENCE_CLASS, 'PacketSizeAndPadding', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_sla_cfg', 'Sla.Protocols.Ethernet.Profiles.Profile.Probe.PacketSizeAndPadding',
                [], [],
                '''                Minimum size to pad outgoing packet to
                ''',
                'packet_size_and_padding',
                'Cisco-IOS-XR-ethernet-cfm-cfg', False, is_presence=True),
            _MetaInfoClassMember('priority', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('0', '7')], [],
                '''                Priority class to assign to outgoing SLA
                packets
                ''',
                'priority',
                'Cisco-IOS-XR-ethernet-cfm-cfg', False),
            _MetaInfoClassMember('synthetic-loss-calculation-packets', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('10', '12096000')], [],
                '''                Number of packets to use in each FLR
                calculation
                ''',
                'synthetic_loss_calculation_packets',
                'Cisco-IOS-XR-ethernet-cfm-cfg', False),
            ],
            'Cisco-IOS-XR-ethernet-cfm-cfg',
            'probe',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-ethernet-cfm-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_sla_cfg',
        ),
    },
    'Sla.Protocols.Ethernet.Profiles.Profile' : {
        'meta_info' : _MetaInfoClass('Sla.Protocols.Ethernet.Profiles.Profile', REFERENCE_LIST,
            '''Name of the profile''',
            False, 
            [
            _MetaInfoClassMember('profile-name', ATTRIBUTE, 'str', 'xr:Cisco-ios-xr-string',
                None, None,
                [], [b'[\\w\\-\\.:,_@#%$\\+=\\|;]+'],
                '''                Profile name
                ''',
                'profile_name',
                'Cisco-IOS-XR-ethernet-cfm-cfg', True),
            _MetaInfoClassMember('statistics', REFERENCE_CLASS, 'Statistics', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_sla_cfg', 'Sla.Protocols.Ethernet.Profiles.Profile.Statistics',
                [], [],
                '''                Statistics configuration for the SLA profile
                ''',
                'statistics',
                'Cisco-IOS-XR-ethernet-cfm-cfg', False),
            _MetaInfoClassMember('schedule', REFERENCE_CLASS, 'Schedule', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_sla_cfg', 'Sla.Protocols.Ethernet.Profiles.Profile.Schedule',
                [], [],
                '''                Schedule to use for probes within an
                operation
                ''',
                'schedule',
                'Cisco-IOS-XR-ethernet-cfm-cfg', False, is_presence=True),
            _MetaInfoClassMember('probe', REFERENCE_CLASS, 'Probe', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_sla_cfg', 'Sla.Protocols.Ethernet.Profiles.Profile.Probe',
                [], [],
                '''                Probe configuration for the SLA profile
                ''',
                'probe',
                'Cisco-IOS-XR-ethernet-cfm-cfg', False),
            _MetaInfoClassMember('packet-type', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                The possible packet types are cfm-loopback,
                cfm-delay-measurement,
                cfm-delay-measurement-version-0,
                cfm-loss-measurement and
                cfm-synthetic-loss-measurement
                ''',
                'packet_type',
                'Cisco-IOS-XR-ethernet-cfm-cfg', False, is_mandatory=True),
            ],
            'Cisco-IOS-XR-ethernet-cfm-cfg',
            'profile',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-ethernet-cfm-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_sla_cfg',
        ),
    },
    'Sla.Protocols.Ethernet.Profiles' : {
        'meta_info' : _MetaInfoClass('Sla.Protocols.Ethernet.Profiles', REFERENCE_CLASS,
            '''Table of SLA profiles on the protocol''',
            False, 
            [
            _MetaInfoClassMember('profile', REFERENCE_LIST, 'Profile', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_sla_cfg', 'Sla.Protocols.Ethernet.Profiles.Profile',
                [], [],
                '''                Name of the profile
                ''',
                'profile',
                'Cisco-IOS-XR-ethernet-cfm-cfg', False),
            ],
            'Cisco-IOS-XR-ethernet-cfm-cfg',
            'profiles',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-ethernet-cfm-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_sla_cfg',
        ),
    },
    'Sla.Protocols.Ethernet' : {
        'meta_info' : _MetaInfoClass('Sla.Protocols.Ethernet', REFERENCE_CLASS,
            '''The Ethernet SLA protocol''',
            False, 
            [
            _MetaInfoClassMember('profiles', REFERENCE_CLASS, 'Profiles', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_sla_cfg', 'Sla.Protocols.Ethernet.Profiles',
                [], [],
                '''                Table of SLA profiles on the protocol
                ''',
                'profiles',
                'Cisco-IOS-XR-ethernet-cfm-cfg', False),
            ],
            'Cisco-IOS-XR-ethernet-cfm-cfg',
            'ethernet',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-ethernet-cfm-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_sla_cfg',
        ),
    },
    'Sla.Protocols' : {
        'meta_info' : _MetaInfoClass('Sla.Protocols', REFERENCE_CLASS,
            '''Table of all SLA protocols''',
            False, 
            [
            _MetaInfoClassMember('ethernet', REFERENCE_CLASS, 'Ethernet', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_sla_cfg', 'Sla.Protocols.Ethernet',
                [], [],
                '''                The Ethernet SLA protocol
                ''',
                'ethernet',
                'Cisco-IOS-XR-ethernet-cfm-cfg', False),
            ],
            'Cisco-IOS-XR-infra-sla-cfg',
            'protocols',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-infra-sla-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_sla_cfg',
        ),
    },
    'Sla' : {
        'meta_info' : _MetaInfoClass('Sla', REFERENCE_CLASS,
            '''SLA prtocol and profile Configuration''',
            False, 
            [
            _MetaInfoClassMember('protocols', REFERENCE_CLASS, 'Protocols', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_sla_cfg', 'Sla.Protocols',
                [], [],
                '''                Table of all SLA protocols
                ''',
                'protocols',
                'Cisco-IOS-XR-infra-sla-cfg', False),
            ],
            'Cisco-IOS-XR-infra-sla-cfg',
            'sla',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-infra-sla-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_sla_cfg',
        ),
    },
}
_meta_table['Sla.Protocols.Ethernet.Profiles.Profile.Statistics.Statistic.Actions.Action']['meta_info'].parent =_meta_table['Sla.Protocols.Ethernet.Profiles.Profile.Statistics.Statistic.Actions']['meta_info']
_meta_table['Sla.Protocols.Ethernet.Profiles.Profile.Statistics.Statistic.BucketsSize']['meta_info'].parent =_meta_table['Sla.Protocols.Ethernet.Profiles.Profile.Statistics.Statistic']['meta_info']
_meta_table['Sla.Protocols.Ethernet.Profiles.Profile.Statistics.Statistic.Actions']['meta_info'].parent =_meta_table['Sla.Protocols.Ethernet.Profiles.Profile.Statistics.Statistic']['meta_info']
_meta_table['Sla.Protocols.Ethernet.Profiles.Profile.Statistics.Statistic.Aggregation']['meta_info'].parent =_meta_table['Sla.Protocols.Ethernet.Profiles.Profile.Statistics.Statistic']['meta_info']
_meta_table['Sla.Protocols.Ethernet.Profiles.Profile.Statistics.Statistic']['meta_info'].parent =_meta_table['Sla.Protocols.Ethernet.Profiles.Profile.Statistics']['meta_info']
_meta_table['Sla.Protocols.Ethernet.Profiles.Profile.Probe.Send']['meta_info'].parent =_meta_table['Sla.Protocols.Ethernet.Profiles.Profile.Probe']['meta_info']
_meta_table['Sla.Protocols.Ethernet.Profiles.Profile.Probe.PacketSizeAndPadding']['meta_info'].parent =_meta_table['Sla.Protocols.Ethernet.Profiles.Profile.Probe']['meta_info']
_meta_table['Sla.Protocols.Ethernet.Profiles.Profile.Statistics']['meta_info'].parent =_meta_table['Sla.Protocols.Ethernet.Profiles.Profile']['meta_info']
_meta_table['Sla.Protocols.Ethernet.Profiles.Profile.Schedule']['meta_info'].parent =_meta_table['Sla.Protocols.Ethernet.Profiles.Profile']['meta_info']
_meta_table['Sla.Protocols.Ethernet.Profiles.Profile.Probe']['meta_info'].parent =_meta_table['Sla.Protocols.Ethernet.Profiles.Profile']['meta_info']
_meta_table['Sla.Protocols.Ethernet.Profiles.Profile']['meta_info'].parent =_meta_table['Sla.Protocols.Ethernet.Profiles']['meta_info']
_meta_table['Sla.Protocols.Ethernet.Profiles']['meta_info'].parent =_meta_table['Sla.Protocols.Ethernet']['meta_info']
_meta_table['Sla.Protocols.Ethernet']['meta_info'].parent =_meta_table['Sla.Protocols']['meta_info']
_meta_table['Sla.Protocols']['meta_info'].parent =_meta_table['Sla']['meta_info']
