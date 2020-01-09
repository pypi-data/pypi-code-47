
'''
This is auto-generated file,
which includes metadata for module Cisco_IOS_XR_infra_sla_oper
'''

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_LIST, REFERENCE_LEAFLIST, REFERENCE_BITS, REFERENCE_UNION
from ydk._core._dm_meta_info import REFERENCE_CLASS, REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, ANYXML_CLASS
from ydk._core._importer import _yang_ns

_meta_table = {
    'Sla.Protocols.Ethernet.StatisticsOnDemandCurrents.StatisticsOnDemandCurrent.SpecificOptions.ConfiguredOperationOptions' : {
        'meta_info' : _MetaInfoClass('Sla.Protocols.Ethernet.StatisticsOnDemandCurrents.StatisticsOnDemandCurrent.SpecificOptions.ConfiguredOperationOptions', REFERENCE_CLASS,
            '''Parameters for a configured operation''',
            False, 
            [
            _MetaInfoClassMember('profile-name', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                Name of the profile used by the operation
                ''',
                'profile_name',
                'Cisco-IOS-XR-ethernet-cfm-oper', False, is_config=False),
            ],
            'Cisco-IOS-XR-ethernet-cfm-oper',
            'configured-operation-options',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-ethernet-cfm-oper'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_sla_oper',
            is_config=False,
            has_when=True,
        ),
    },
    'Sla.Protocols.Ethernet.StatisticsOnDemandCurrents.StatisticsOnDemandCurrent.SpecificOptions.OndemandOperationOptions' : {
        'meta_info' : _MetaInfoClass('Sla.Protocols.Ethernet.StatisticsOnDemandCurrents.StatisticsOnDemandCurrent.SpecificOptions.OndemandOperationOptions', REFERENCE_CLASS,
            '''Parameters for an ondemand operation''',
            False, 
            [
            _MetaInfoClassMember('ondemand-operation-id', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('0', '4294967295')], [],
                '''                ID of the ondemand operation
                ''',
                'ondemand_operation_id',
                'Cisco-IOS-XR-ethernet-cfm-oper', False, is_config=False),
            _MetaInfoClassMember('probe-count', ATTRIBUTE, 'int', 'uint8',
                None, None,
                [('0', '255')], [],
                '''                Total number of probes sent during the operation
                ''',
                'probe_count',
                'Cisco-IOS-XR-ethernet-cfm-oper', False, is_config=False),
            ],
            'Cisco-IOS-XR-ethernet-cfm-oper',
            'ondemand-operation-options',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-ethernet-cfm-oper'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_sla_oper',
            is_config=False,
            has_when=True,
        ),
    },
    'Sla.Protocols.Ethernet.StatisticsOnDemandCurrents.StatisticsOnDemandCurrent.SpecificOptions' : {
        'meta_info' : _MetaInfoClass('Sla.Protocols.Ethernet.StatisticsOnDemandCurrents.StatisticsOnDemandCurrent.SpecificOptions', REFERENCE_CLASS,
            '''Options specific to the type of operation''',
            False, 
            [
            _MetaInfoClassMember('configured-operation-options', REFERENCE_CLASS, 'ConfiguredOperationOptions', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_sla_oper', 'Sla.Protocols.Ethernet.StatisticsOnDemandCurrents.StatisticsOnDemandCurrent.SpecificOptions.ConfiguredOperationOptions',
                [], [],
                '''                Parameters for a configured operation
                ''',
                'configured_operation_options',
                'Cisco-IOS-XR-ethernet-cfm-oper', False, is_config=False, has_when=True),
            _MetaInfoClassMember('ondemand-operation-options', REFERENCE_CLASS, 'OndemandOperationOptions', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_sla_oper', 'Sla.Protocols.Ethernet.StatisticsOnDemandCurrents.StatisticsOnDemandCurrent.SpecificOptions.OndemandOperationOptions',
                [], [],
                '''                Parameters for an ondemand operation
                ''',
                'ondemand_operation_options',
                'Cisco-IOS-XR-ethernet-cfm-oper', False, is_config=False, has_when=True),
            _MetaInfoClassMember('oper-type', REFERENCE_ENUM_CLASS, 'SlaOperOperation', 'Sla-oper-operation',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper', 'SlaOperOperation',
                [], [],
                '''                OperType
                ''',
                'oper_type',
                'Cisco-IOS-XR-ethernet-cfm-oper', False, is_config=False),
            ],
            'Cisco-IOS-XR-ethernet-cfm-oper',
            'specific-options',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-ethernet-cfm-oper'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_sla_oper',
            is_config=False,
        ),
    },
    'Sla.Protocols.Ethernet.StatisticsOnDemandCurrents.StatisticsOnDemandCurrent.OperationSchedule' : {
        'meta_info' : _MetaInfoClass('Sla.Protocols.Ethernet.StatisticsOnDemandCurrents.StatisticsOnDemandCurrent.OperationSchedule', REFERENCE_CLASS,
            '''Operation schedule''',
            False, 
            [
            _MetaInfoClassMember('start-time', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('0', '4294967295')], [],
                '''                Start time of the first probe, in seconds since
                the Unix Epoch
                ''',
                'start_time',
                'Cisco-IOS-XR-ethernet-cfm-oper', False, is_config=False),
            _MetaInfoClassMember('start-time-configured', ATTRIBUTE, 'bool', 'boolean',
                None, None,
                [], [],
                '''                Whether or not the operation start time was
                explicitly configured
                ''',
                'start_time_configured',
                'Cisco-IOS-XR-ethernet-cfm-oper', False, is_config=False),
            _MetaInfoClassMember('schedule-duration', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('0', '4294967295')], [],
                '''                Duration of a probe for the operation in seconds
                ''',
                'schedule_duration',
                'Cisco-IOS-XR-ethernet-cfm-oper', False, is_config=False),
            _MetaInfoClassMember('schedule-interval', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('0', '4294967295')], [],
                '''                Interval between the start times of consecutive
                probes,  in seconds.
                ''',
                'schedule_interval',
                'Cisco-IOS-XR-ethernet-cfm-oper', False, is_config=False),
            ],
            'Cisco-IOS-XR-ethernet-cfm-oper',
            'operation-schedule',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-ethernet-cfm-oper'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_sla_oper',
            is_config=False,
        ),
    },
    'Sla.Protocols.Ethernet.StatisticsOnDemandCurrents.StatisticsOnDemandCurrent.OperationMetric.Config' : {
        'meta_info' : _MetaInfoClass('Sla.Protocols.Ethernet.StatisticsOnDemandCurrents.StatisticsOnDemandCurrent.OperationMetric.Config', REFERENCE_CLASS,
            '''Configuration of the metric''',
            False, 
            [
            _MetaInfoClassMember('metric-type', REFERENCE_ENUM_CLASS, 'SlaRecordableMetric', 'Sla-recordable-metric',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper', 'SlaRecordableMetric',
                [], [],
                '''                Type of metric to which this configuration
                applies
                ''',
                'metric_type',
                'Cisco-IOS-XR-ethernet-cfm-oper', False, is_config=False),
            _MetaInfoClassMember('bins-count', ATTRIBUTE, 'int', 'uint16',
                None, None,
                [('0', '65535')], [],
                '''                Total number of bins into which to aggregate. 0
                if no aggregation.
                ''',
                'bins_count',
                'Cisco-IOS-XR-ethernet-cfm-oper', False, is_config=False),
            _MetaInfoClassMember('bins-width', ATTRIBUTE, 'int', 'uint16',
                None, None,
                [('0', '65535')], [],
                '''                Width of each bin into which to aggregate. 0 if
                no aggregation. For SLM, the units of this value
                are in single units of percent; for LMM they are
                in tenths of percent; for other measurements
                they are in milliseconds.
                ''',
                'bins_width',
                'Cisco-IOS-XR-ethernet-cfm-oper', False, is_config=False),
            _MetaInfoClassMember('bucket-size', ATTRIBUTE, 'int', 'uint8',
                None, None,
                [('0', '255')], [],
                '''                Size of buckets into which measurements are
                collected
                ''',
                'bucket_size',
                'Cisco-IOS-XR-ethernet-cfm-oper', False, is_config=False),
            _MetaInfoClassMember('bucket-size-unit', REFERENCE_ENUM_CLASS, 'SlaBucketSize', 'Sla-bucket-size',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper', 'SlaBucketSize',
                [], [],
                '''                Whether bucket size is 'per-probe' or 'probes'
                ''',
                'bucket_size_unit',
                'Cisco-IOS-XR-ethernet-cfm-oper', False, is_config=False),
            _MetaInfoClassMember('buckets-archive', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('0', '4294967295')], [],
                '''                Maximum number of buckets to store in memory
                ''',
                'buckets_archive',
                'Cisco-IOS-XR-ethernet-cfm-oper', False, is_config=False),
            ],
            'Cisco-IOS-XR-ethernet-cfm-oper',
            'config',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-ethernet-cfm-oper'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_sla_oper',
            is_config=False,
        ),
    },
    'Sla.Protocols.Ethernet.StatisticsOnDemandCurrents.StatisticsOnDemandCurrent.OperationMetric.Bucket.Contents.Aggregated.Bins' : {
        'meta_info' : _MetaInfoClass('Sla.Protocols.Ethernet.StatisticsOnDemandCurrents.StatisticsOnDemandCurrent.OperationMetric.Bucket.Contents.Aggregated.Bins', REFERENCE_LIST,
            '''The bins of an SLA metric bucket''',
            False, 
            [
            _MetaInfoClassMember('lower-bound', ATTRIBUTE, 'int', 'int32',
                None, None,
                [('-2147483648', '2147483647')], [],
                '''                Lower bound (inclusive) of the bin, in
                milliseconds or single units of percent. This
                field is not used for LMM measurements
                ''',
                'lower_bound',
                'Cisco-IOS-XR-ethernet-cfm-oper', False, is_config=False),
            _MetaInfoClassMember('upper-bound', ATTRIBUTE, 'int', 'int32',
                None, None,
                [('-2147483648', '2147483647')], [],
                '''                Upper bound (exclusive) of the bin, in
                milliseconds or single units of percent. This
                field is not used for LMM measurements
                ''',
                'upper_bound',
                'Cisco-IOS-XR-ethernet-cfm-oper', False, is_config=False),
            _MetaInfoClassMember('lower-bound-tenths', ATTRIBUTE, 'int', 'int32',
                None, None,
                [('-2147483648', '2147483647')], [],
                '''                Lower bound (inclusive) of the bin, in tenths of
                percent. This field is only used for LMM
                measurements
                ''',
                'lower_bound_tenths',
                'Cisco-IOS-XR-ethernet-cfm-oper', False, is_config=False),
            _MetaInfoClassMember('upper-bound-tenths', ATTRIBUTE, 'int', 'int32',
                None, None,
                [('-2147483648', '2147483647')], [],
                '''                Upper bound (exclusive) of the bin, in tenths of
                percent. This field is only used for LMM
                measurements
                ''',
                'upper_bound_tenths',
                'Cisco-IOS-XR-ethernet-cfm-oper', False, is_config=False),
            _MetaInfoClassMember('sum', ATTRIBUTE, 'int', 'int64',
                None, None,
                [('-9223372036854775808', '9223372036854775807')], [],
                '''                The sum of the results in the bin, in
                microseconds or millionths of a percent
                ''',
                'sum',
                'Cisco-IOS-XR-ethernet-cfm-oper', False, is_config=False),
            _MetaInfoClassMember('count', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('0', '4294967295')], [],
                '''                The total number of results in the bin
                ''',
                'count',
                'Cisco-IOS-XR-ethernet-cfm-oper', False, is_config=False),
            ],
            'Cisco-IOS-XR-ethernet-cfm-oper',
            'bins',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-ethernet-cfm-oper'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_sla_oper',
            is_config=False,
        ),
    },
    'Sla.Protocols.Ethernet.StatisticsOnDemandCurrents.StatisticsOnDemandCurrent.OperationMetric.Bucket.Contents.Aggregated' : {
        'meta_info' : _MetaInfoClass('Sla.Protocols.Ethernet.StatisticsOnDemandCurrents.StatisticsOnDemandCurrent.OperationMetric.Bucket.Contents.Aggregated', REFERENCE_CLASS,
            '''Result bins in an SLA metric bucket''',
            False, 
            [
            _MetaInfoClassMember('bins', REFERENCE_LIST, 'Bins', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_sla_oper', 'Sla.Protocols.Ethernet.StatisticsOnDemandCurrents.StatisticsOnDemandCurrent.OperationMetric.Bucket.Contents.Aggregated.Bins',
                [], [],
                '''                The bins of an SLA metric bucket
                ''',
                'bins',
                'Cisco-IOS-XR-ethernet-cfm-oper', False, is_config=False),
            ],
            'Cisco-IOS-XR-ethernet-cfm-oper',
            'aggregated',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-ethernet-cfm-oper'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_sla_oper',
            is_config=False,
            has_when=True,
        ),
    },
    'Sla.Protocols.Ethernet.StatisticsOnDemandCurrents.StatisticsOnDemandCurrent.OperationMetric.Bucket.Contents.Unaggregated.Sample' : {
        'meta_info' : _MetaInfoClass('Sla.Protocols.Ethernet.StatisticsOnDemandCurrents.StatisticsOnDemandCurrent.OperationMetric.Bucket.Contents.Unaggregated.Sample', REFERENCE_LIST,
            '''The samples of an SLA metric bucket''',
            False, 
            [
            _MetaInfoClassMember('sent-at', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('0', '4294967295')], [],
                '''                The time (in milliseconds relative to the start
                time of the bucket) that the sample was sent at
                ''',
                'sent_at',
                'Cisco-IOS-XR-ethernet-cfm-oper', False, is_config=False),
            _MetaInfoClassMember('sent', ATTRIBUTE, 'bool', 'boolean',
                None, None,
                [], [],
                '''                Whether the sample packet was sucessfully sent
                ''',
                'sent',
                'Cisco-IOS-XR-ethernet-cfm-oper', False, is_config=False),
            _MetaInfoClassMember('timed-out', ATTRIBUTE, 'bool', 'boolean',
                None, None,
                [], [],
                '''                Whether the sample packet timed out
                ''',
                'timed_out',
                'Cisco-IOS-XR-ethernet-cfm-oper', False, is_config=False),
            _MetaInfoClassMember('corrupt', ATTRIBUTE, 'bool', 'boolean',
                None, None,
                [], [],
                '''                Whether the sample packet was corrupt
                ''',
                'corrupt',
                'Cisco-IOS-XR-ethernet-cfm-oper', False, is_config=False),
            _MetaInfoClassMember('out-of-order', ATTRIBUTE, 'bool', 'boolean',
                None, None,
                [], [],
                '''                Whether the sample packet was received
                out-of-order
                ''',
                'out_of_order',
                'Cisco-IOS-XR-ethernet-cfm-oper', False, is_config=False),
            _MetaInfoClassMember('no-data-packets', ATTRIBUTE, 'bool', 'boolean',
                None, None,
                [], [],
                '''                Whether a measurement could not be made because
                no data packets were sent in the sample period.
                Only applicable for LMM measurements
                ''',
                'no_data_packets',
                'Cisco-IOS-XR-ethernet-cfm-oper', False, is_config=False),
            _MetaInfoClassMember('result', ATTRIBUTE, 'int', 'int32',
                None, None,
                [('-2147483648', '2147483647')], [],
                '''                The result (in microseconds or millionths of a
                percent) of the sample, if available
                ''',
                'result',
                'Cisco-IOS-XR-ethernet-cfm-oper', False, is_config=False),
            _MetaInfoClassMember('frames-sent', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('0', '4294967295')], [],
                '''                For FLR measurements, the number of frames sent,
                if available
                ''',
                'frames_sent',
                'Cisco-IOS-XR-ethernet-cfm-oper', False, is_config=False),
            _MetaInfoClassMember('frames-lost', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('0', '4294967295')], [],
                '''                For FLR measurements, the number of frames lost,
                if available
                ''',
                'frames_lost',
                'Cisco-IOS-XR-ethernet-cfm-oper', False, is_config=False),
            ],
            'Cisco-IOS-XR-ethernet-cfm-oper',
            'sample',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-ethernet-cfm-oper'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_sla_oper',
            is_config=False,
        ),
    },
    'Sla.Protocols.Ethernet.StatisticsOnDemandCurrents.StatisticsOnDemandCurrent.OperationMetric.Bucket.Contents.Unaggregated' : {
        'meta_info' : _MetaInfoClass('Sla.Protocols.Ethernet.StatisticsOnDemandCurrents.StatisticsOnDemandCurrent.OperationMetric.Bucket.Contents.Unaggregated', REFERENCE_CLASS,
            '''Result samples in an SLA metric bucket''',
            False, 
            [
            _MetaInfoClassMember('sample', REFERENCE_LIST, 'Sample', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_sla_oper', 'Sla.Protocols.Ethernet.StatisticsOnDemandCurrents.StatisticsOnDemandCurrent.OperationMetric.Bucket.Contents.Unaggregated.Sample',
                [], [],
                '''                The samples of an SLA metric bucket
                ''',
                'sample',
                'Cisco-IOS-XR-ethernet-cfm-oper', False, is_config=False),
            ],
            'Cisco-IOS-XR-ethernet-cfm-oper',
            'unaggregated',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-ethernet-cfm-oper'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_sla_oper',
            is_config=False,
            has_when=True,
        ),
    },
    'Sla.Protocols.Ethernet.StatisticsOnDemandCurrents.StatisticsOnDemandCurrent.OperationMetric.Bucket.Contents' : {
        'meta_info' : _MetaInfoClass('Sla.Protocols.Ethernet.StatisticsOnDemandCurrents.StatisticsOnDemandCurrent.OperationMetric.Bucket.Contents', REFERENCE_CLASS,
            '''The contents of the bucket; bins or samples''',
            False, 
            [
            _MetaInfoClassMember('aggregated', REFERENCE_CLASS, 'Aggregated', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_sla_oper', 'Sla.Protocols.Ethernet.StatisticsOnDemandCurrents.StatisticsOnDemandCurrent.OperationMetric.Bucket.Contents.Aggregated',
                [], [],
                '''                Result bins in an SLA metric bucket
                ''',
                'aggregated',
                'Cisco-IOS-XR-ethernet-cfm-oper', False, is_config=False, has_when=True),
            _MetaInfoClassMember('unaggregated', REFERENCE_CLASS, 'Unaggregated', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_sla_oper', 'Sla.Protocols.Ethernet.StatisticsOnDemandCurrents.StatisticsOnDemandCurrent.OperationMetric.Bucket.Contents.Unaggregated',
                [], [],
                '''                Result samples in an SLA metric bucket
                ''',
                'unaggregated',
                'Cisco-IOS-XR-ethernet-cfm-oper', False, is_config=False, has_when=True),
            _MetaInfoClassMember('bucket-type', REFERENCE_ENUM_CLASS, 'SlaOperBucket', 'Sla-oper-bucket',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper', 'SlaOperBucket',
                [], [],
                '''                BucketType
                ''',
                'bucket_type',
                'Cisco-IOS-XR-ethernet-cfm-oper', False, is_config=False),
            ],
            'Cisco-IOS-XR-ethernet-cfm-oper',
            'contents',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-ethernet-cfm-oper'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_sla_oper',
            is_config=False,
        ),
    },
    'Sla.Protocols.Ethernet.StatisticsOnDemandCurrents.StatisticsOnDemandCurrent.OperationMetric.Bucket' : {
        'meta_info' : _MetaInfoClass('Sla.Protocols.Ethernet.StatisticsOnDemandCurrents.StatisticsOnDemandCurrent.OperationMetric.Bucket', REFERENCE_LIST,
            '''Buckets stored for the metric''',
            False, 
            [
            _MetaInfoClassMember('contents', REFERENCE_CLASS, 'Contents', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_sla_oper', 'Sla.Protocols.Ethernet.StatisticsOnDemandCurrents.StatisticsOnDemandCurrent.OperationMetric.Bucket.Contents',
                [], [],
                '''                The contents of the bucket; bins or samples
                ''',
                'contents',
                'Cisco-IOS-XR-ethernet-cfm-oper', False, is_config=False),
            _MetaInfoClassMember('start-at', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('0', '4294967295')], [],
                '''                Absolute time that the bucket started being
                filled at
                ''',
                'start_at',
                'Cisco-IOS-XR-ethernet-cfm-oper', False, is_config=False),
            _MetaInfoClassMember('duration', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('0', '4294967295')], [],
                '''                Length of time for which the bucket is being
                filled in seconds
                ''',
                'duration',
                'Cisco-IOS-XR-ethernet-cfm-oper', False, is_config=False),
            _MetaInfoClassMember('sent', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('0', '4294967295')], [],
                '''                Number of packets sent in the probe
                ''',
                'sent',
                'Cisco-IOS-XR-ethernet-cfm-oper', False, is_config=False),
            _MetaInfoClassMember('lost', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('0', '4294967295')], [],
                '''                Number of lost packets in the probe
                ''',
                'lost',
                'Cisco-IOS-XR-ethernet-cfm-oper', False, is_config=False),
            _MetaInfoClassMember('corrupt', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('0', '4294967295')], [],
                '''                Number of corrupt packets in the probe
                ''',
                'corrupt',
                'Cisco-IOS-XR-ethernet-cfm-oper', False, is_config=False),
            _MetaInfoClassMember('out-of-order', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('0', '4294967295')], [],
                '''                Number of packets recieved out-of-order in the
                probe
                ''',
                'out_of_order',
                'Cisco-IOS-XR-ethernet-cfm-oper', False, is_config=False),
            _MetaInfoClassMember('duplicates', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('0', '4294967295')], [],
                '''                Number of duplicate packets received in the
                probe
                ''',
                'duplicates',
                'Cisco-IOS-XR-ethernet-cfm-oper', False, is_config=False),
            _MetaInfoClassMember('minimum', ATTRIBUTE, 'int', 'int32',
                None, None,
                [('-2147483648', '2147483647')], [],
                '''                Overall minimum result in the probe, in
                microseconds or millionths of a percent
                ''',
                'minimum',
                'Cisco-IOS-XR-ethernet-cfm-oper', False, is_config=False),
            _MetaInfoClassMember('maximum', ATTRIBUTE, 'int', 'int32',
                None, None,
                [('-2147483648', '2147483647')], [],
                '''                Overall minimum result in the probe, in
                microseconds or millionths of a percent
                ''',
                'maximum',
                'Cisco-IOS-XR-ethernet-cfm-oper', False, is_config=False),
            _MetaInfoClassMember('time-of-minimum', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('0', '4294967295')], [],
                '''                Absolute time that the minimum value was
                recorded
                ''',
                'time_of_minimum',
                'Cisco-IOS-XR-ethernet-cfm-oper', False, is_config=False),
            _MetaInfoClassMember('time-of-maximum', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('0', '4294967295')], [],
                '''                Absolute time that the maximum value was
                recorded
                ''',
                'time_of_maximum',
                'Cisco-IOS-XR-ethernet-cfm-oper', False, is_config=False),
            _MetaInfoClassMember('average', ATTRIBUTE, 'int', 'int32',
                None, None,
                [('-2147483648', '2147483647')], [],
                '''                Mean of the results in the probe, in
                microseconds or millionths of a percent
                ''',
                'average',
                'Cisco-IOS-XR-ethernet-cfm-oper', False, is_config=False),
            _MetaInfoClassMember('standard-deviation', ATTRIBUTE, 'int', 'int32',
                None, None,
                [('-2147483648', '2147483647')], [],
                '''                Standard deviation of the results in the probe,
                in microseconds or millionths of a percent
                ''',
                'standard_deviation',
                'Cisco-IOS-XR-ethernet-cfm-oper', False, is_config=False),
            _MetaInfoClassMember('result-count', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('0', '4294967295')], [],
                '''                The count of samples collected in the bucket.
                ''',
                'result_count',
                'Cisco-IOS-XR-ethernet-cfm-oper', False, is_config=False),
            _MetaInfoClassMember('data-sent-count', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('0', '4294967295')], [],
                '''                The number of data packets sent across the
                bucket, used in the calculation of overall FLR.
                ''',
                'data_sent_count',
                'Cisco-IOS-XR-ethernet-cfm-oper', False, is_config=False),
            _MetaInfoClassMember('data-lost-count', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('0', '4294967295')], [],
                '''                The number of data packets lost across the
                bucket, used in the calculation of overall FLR.
                ''',
                'data_lost_count',
                'Cisco-IOS-XR-ethernet-cfm-oper', False, is_config=False),
            _MetaInfoClassMember('overall-flr', ATTRIBUTE, 'int', 'int32',
                None, None,
                [('-2147483648', '2147483647')], [],
                '''                Frame Loss Ratio across the whole bucket, in
                millionths of a percent
                ''',
                'overall_flr',
                'Cisco-IOS-XR-ethernet-cfm-oper', False, is_config=False),
            _MetaInfoClassMember('suspect-start-mid-bucket', ATTRIBUTE, 'bool', 'boolean',
                None, None,
                [], [],
                '''                Results suspect due to a probe starting mid-way
                through a bucket
                ''',
                'suspect_start_mid_bucket',
                'Cisco-IOS-XR-ethernet-cfm-oper', False, is_config=False),
            _MetaInfoClassMember('suspect-schedule-latency', ATTRIBUTE, 'bool', 'boolean',
                None, None,
                [], [],
                '''                Results suspect due to scheduling latency
                causing one or more packets to not be sent
                ''',
                'suspect_schedule_latency',
                'Cisco-IOS-XR-ethernet-cfm-oper', False, is_config=False),
            _MetaInfoClassMember('suspect-send-fail', ATTRIBUTE, 'bool', 'boolean',
                None, None,
                [], [],
                '''                Results suspect due to failure to send one or
                more packets
                ''',
                'suspect_send_fail',
                'Cisco-IOS-XR-ethernet-cfm-oper', False, is_config=False),
            _MetaInfoClassMember('suspect-premature-end', ATTRIBUTE, 'bool', 'boolean',
                None, None,
                [], [],
                '''                Results suspect due to a probe ending
                prematurely
                ''',
                'suspect_premature_end',
                'Cisco-IOS-XR-ethernet-cfm-oper', False, is_config=False),
            _MetaInfoClassMember('suspect-clock-drift', ATTRIBUTE, 'bool', 'boolean',
                None, None,
                [], [],
                '''                Results suspect as more than 10 seconds time
                drift detected
                ''',
                'suspect_clock_drift',
                'Cisco-IOS-XR-ethernet-cfm-oper', False, is_config=False),
            _MetaInfoClassMember('suspect-memory-allocation-failed', ATTRIBUTE, 'bool', 'boolean',
                None, None,
                [], [],
                '''                Results suspect due to a memory allocation
                failure
                ''',
                'suspect_memory_allocation_failed',
                'Cisco-IOS-XR-ethernet-cfm-oper', False, is_config=False),
            _MetaInfoClassMember('suspect-cleared-mid-bucket', ATTRIBUTE, 'bool', 'boolean',
                None, None,
                [], [],
                '''                Results suspect as bucket was cleared mid-way
                through being filled
                ''',
                'suspect_cleared_mid_bucket',
                'Cisco-IOS-XR-ethernet-cfm-oper', False, is_config=False),
            _MetaInfoClassMember('suspect-probe-restarted', ATTRIBUTE, 'bool', 'boolean',
                None, None,
                [], [],
                '''                Results suspect as probe restarted mid-way
                through the bucket
                ''',
                'suspect_probe_restarted',
                'Cisco-IOS-XR-ethernet-cfm-oper', False, is_config=False),
            _MetaInfoClassMember('suspect-management-latency', ATTRIBUTE, 'bool', 'boolean',
                None, None,
                [], [],
                '''                Results suspect as processing of results has
                been delayed
                ''',
                'suspect_management_latency',
                'Cisco-IOS-XR-ethernet-cfm-oper', False, is_config=False),
            _MetaInfoClassMember('suspect-multiple-buckets', ATTRIBUTE, 'bool', 'boolean',
                None, None,
                [], [],
                '''                Results suspect as the probe has been configured
                across multiple buckets
                ''',
                'suspect_multiple_buckets',
                'Cisco-IOS-XR-ethernet-cfm-oper', False, is_config=False),
            _MetaInfoClassMember('suspect-misordering', ATTRIBUTE, 'bool', 'boolean',
                None, None,
                [], [],
                '''                Results suspect as misordering has been detected
                , affecting results
                ''',
                'suspect_misordering',
                'Cisco-IOS-XR-ethernet-cfm-oper', False, is_config=False),
            _MetaInfoClassMember('suspect-flr-low-packet-count', ATTRIBUTE, 'bool', 'boolean',
                None, None,
                [], [],
                '''                Results suspect as FLR calculated based on a low
                packet count
                ''',
                'suspect_flr_low_packet_count',
                'Cisco-IOS-XR-ethernet-cfm-oper', False, is_config=False),
            _MetaInfoClassMember('premature-reason', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('0', '4294967295')], [],
                '''                If the probe ended prematurely, the error that
                caused a probe to end
                ''',
                'premature_reason',
                'Cisco-IOS-XR-ethernet-cfm-oper', False, is_config=False),
            _MetaInfoClassMember('premature-reason-string', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                Description of the error code that caused the
                probe to end prematurely. For informational
                purposes only
                ''',
                'premature_reason_string',
                'Cisco-IOS-XR-ethernet-cfm-oper', False, is_config=False),
            ],
            'Cisco-IOS-XR-ethernet-cfm-oper',
            'bucket',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-ethernet-cfm-oper'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_sla_oper',
            is_config=False,
        ),
    },
    'Sla.Protocols.Ethernet.StatisticsOnDemandCurrents.StatisticsOnDemandCurrent.OperationMetric' : {
        'meta_info' : _MetaInfoClass('Sla.Protocols.Ethernet.StatisticsOnDemandCurrents.StatisticsOnDemandCurrent.OperationMetric', REFERENCE_LIST,
            '''Metrics gathered for the operation''',
            False, 
            [
            _MetaInfoClassMember('config', REFERENCE_CLASS, 'Config', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_sla_oper', 'Sla.Protocols.Ethernet.StatisticsOnDemandCurrents.StatisticsOnDemandCurrent.OperationMetric.Config',
                [], [],
                '''                Configuration of the metric
                ''',
                'config',
                'Cisco-IOS-XR-ethernet-cfm-oper', False, is_config=False),
            _MetaInfoClassMember('bucket', REFERENCE_LIST, 'Bucket', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_sla_oper', 'Sla.Protocols.Ethernet.StatisticsOnDemandCurrents.StatisticsOnDemandCurrent.OperationMetric.Bucket',
                [], [],
                '''                Buckets stored for the metric
                ''',
                'bucket',
                'Cisco-IOS-XR-ethernet-cfm-oper', False, is_config=False),
            ],
            'Cisco-IOS-XR-ethernet-cfm-oper',
            'operation-metric',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-ethernet-cfm-oper'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_sla_oper',
            is_config=False,
        ),
    },
    'Sla.Protocols.Ethernet.StatisticsOnDemandCurrents.StatisticsOnDemandCurrent' : {
        'meta_info' : _MetaInfoClass('Sla.Protocols.Ethernet.StatisticsOnDemandCurrents.StatisticsOnDemandCurrent', REFERENCE_LIST,
            '''Current statistics data for an SLA on-demand
operation''',
            False, 
            [
            _MetaInfoClassMember('operation-id', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('1', '4294967295')], [],
                '''                Operation ID
                ''',
                'operation_id',
                'Cisco-IOS-XR-ethernet-cfm-oper', False, is_config=False),
            _MetaInfoClassMember('domain-name', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                Domain name
                ''',
                'domain_name',
                'Cisco-IOS-XR-ethernet-cfm-oper', False, is_config=False),
            _MetaInfoClassMember('interface-name', ATTRIBUTE, 'str', 'xr:Interface-name',
                None, None,
                [], [b'[a-zA-Z0-9._/-]+'],
                '''                Interface name
                ''',
                'interface_name',
                'Cisco-IOS-XR-ethernet-cfm-oper', False, is_config=False),
            _MetaInfoClassMember('mep-id', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('1', '8191')], [],
                '''                MEP ID in the range 1 to 8191. Either MEP ID
                or MAC address must be specified.
                ''',
                'mep_id',
                'Cisco-IOS-XR-ethernet-cfm-oper', False, is_config=False),
            _MetaInfoClassMember('mac-address', ATTRIBUTE, 'str', 'yang:mac-address',
                None, None,
                [], [b'[0-9a-fA-F]{2}(:[0-9a-fA-F]{2}){5}'],
                '''                Unicast MAC Address in xxxx.xxxx.xxxx format.
                Either MEP ID or MAC address must be
                specified.
                ''',
                'mac_address',
                'Cisco-IOS-XR-ethernet-cfm-oper', False, is_config=False),
            _MetaInfoClassMember('specific-options', REFERENCE_CLASS, 'SpecificOptions', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_sla_oper', 'Sla.Protocols.Ethernet.StatisticsOnDemandCurrents.StatisticsOnDemandCurrent.SpecificOptions',
                [], [],
                '''                Options specific to the type of operation
                ''',
                'specific_options',
                'Cisco-IOS-XR-ethernet-cfm-oper', False, is_config=False),
            _MetaInfoClassMember('operation-schedule', REFERENCE_CLASS, 'OperationSchedule', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_sla_oper', 'Sla.Protocols.Ethernet.StatisticsOnDemandCurrents.StatisticsOnDemandCurrent.OperationSchedule',
                [], [],
                '''                Operation schedule
                ''',
                'operation_schedule',
                'Cisco-IOS-XR-ethernet-cfm-oper', False, is_config=False),
            _MetaInfoClassMember('probe-type', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                Type of probe used by the operation
                ''',
                'probe_type',
                'Cisco-IOS-XR-ethernet-cfm-oper', False, is_config=False),
            _MetaInfoClassMember('display-short', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                Short display name used by the operation
                ''',
                'display_short',
                'Cisco-IOS-XR-ethernet-cfm-oper', False, is_config=False),
            _MetaInfoClassMember('display-long', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                Long display name used by the operation
                ''',
                'display_long',
                'Cisco-IOS-XR-ethernet-cfm-oper', False, is_config=False),
            _MetaInfoClassMember('flr-calculation-interval', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('0', '4294967295')], [],
                '''                Interval between FLR calculations for SLM, in
                milliseconds
                ''',
                'flr_calculation_interval',
                'Cisco-IOS-XR-ethernet-cfm-oper', False, is_config=False),
            _MetaInfoClassMember('operation-metric', REFERENCE_LIST, 'OperationMetric', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_sla_oper', 'Sla.Protocols.Ethernet.StatisticsOnDemandCurrents.StatisticsOnDemandCurrent.OperationMetric',
                [], [],
                '''                Metrics gathered for the operation
                ''',
                'operation_metric',
                'Cisco-IOS-XR-ethernet-cfm-oper', False, is_config=False),
            ],
            'Cisco-IOS-XR-ethernet-cfm-oper',
            'statistics-on-demand-current',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-ethernet-cfm-oper'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_sla_oper',
            is_config=False,
        ),
    },
    'Sla.Protocols.Ethernet.StatisticsOnDemandCurrents' : {
        'meta_info' : _MetaInfoClass('Sla.Protocols.Ethernet.StatisticsOnDemandCurrents', REFERENCE_CLASS,
            '''Table of current statistics for SLA on-demand
operations''',
            False, 
            [
            _MetaInfoClassMember('statistics-on-demand-current', REFERENCE_LIST, 'StatisticsOnDemandCurrent', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_sla_oper', 'Sla.Protocols.Ethernet.StatisticsOnDemandCurrents.StatisticsOnDemandCurrent',
                [], [],
                '''                Current statistics data for an SLA on-demand
                operation
                ''',
                'statistics_on_demand_current',
                'Cisco-IOS-XR-ethernet-cfm-oper', False, is_config=False),
            ],
            'Cisco-IOS-XR-ethernet-cfm-oper',
            'statistics-on-demand-currents',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-ethernet-cfm-oper'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_sla_oper',
            is_config=False,
        ),
    },
    'Sla.Protocols.Ethernet.Operations.Operation.ProfileOptions.PacketPadding' : {
        'meta_info' : _MetaInfoClass('Sla.Protocols.Ethernet.Operations.Operation.ProfileOptions.PacketPadding', REFERENCE_CLASS,
            '''Configuration of the packet padding''',
            False, 
            [
            _MetaInfoClassMember('packet-pad-size', ATTRIBUTE, 'int', 'uint16',
                None, None,
                [('0', '65535')], [],
                '''                Size that packets are being padded to
                ''',
                'packet_pad_size',
                'Cisco-IOS-XR-ethernet-cfm-oper', False, is_config=False),
            _MetaInfoClassMember('test-pattern-pad-scheme', REFERENCE_ENUM_CLASS, 'SlaOperTestPatternScheme', 'Sla-oper-test-pattern-scheme',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper', 'SlaOperTestPatternScheme',
                [], [],
                '''                Test pattern scheme that is used in the packet
                padding
                ''',
                'test_pattern_pad_scheme',
                'Cisco-IOS-XR-ethernet-cfm-oper', False, is_config=False),
            _MetaInfoClassMember('test-pattern-pad-hex-string', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('0', '4294967295')], [],
                '''                Hex string that is used in the packet padding
                ''',
                'test_pattern_pad_hex_string',
                'Cisco-IOS-XR-ethernet-cfm-oper', False, is_config=False),
            ],
            'Cisco-IOS-XR-ethernet-cfm-oper',
            'packet-padding',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-ethernet-cfm-oper'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_sla_oper',
            is_config=False,
        ),
    },
    'Sla.Protocols.Ethernet.Operations.Operation.ProfileOptions.Priority' : {
        'meta_info' : _MetaInfoClass('Sla.Protocols.Ethernet.Operations.Operation.ProfileOptions.Priority', REFERENCE_CLASS,
            '''Priority at which to send the packet, if
configured''',
            False, 
            [
            _MetaInfoClassMember('priority-type', REFERENCE_ENUM_CLASS, 'SlaOperPacketPriority', 'Sla-oper-packet-priority',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper', 'SlaOperPacketPriority',
                [], [],
                '''                PriorityType
                ''',
                'priority_type',
                'Cisco-IOS-XR-ethernet-cfm-oper', False, is_config=False),
            _MetaInfoClassMember('cos', ATTRIBUTE, 'int', 'uint8',
                None, None,
                [('0', '255')], [],
                '''                3-bit COS priority value applied to packets
                ''',
                'cos',
                'Cisco-IOS-XR-ethernet-cfm-oper', False, is_config=False, has_when=True),
            ],
            'Cisco-IOS-XR-ethernet-cfm-oper',
            'priority',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-ethernet-cfm-oper'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_sla_oper',
            is_config=False,
        ),
    },
    'Sla.Protocols.Ethernet.Operations.Operation.ProfileOptions.OperationSchedule' : {
        'meta_info' : _MetaInfoClass('Sla.Protocols.Ethernet.Operations.Operation.ProfileOptions.OperationSchedule', REFERENCE_CLASS,
            '''Operation schedule''',
            False, 
            [
            _MetaInfoClassMember('start-time', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('0', '4294967295')], [],
                '''                Start time of the first probe, in seconds since
                the Unix Epoch
                ''',
                'start_time',
                'Cisco-IOS-XR-ethernet-cfm-oper', False, is_config=False),
            _MetaInfoClassMember('start-time-configured', ATTRIBUTE, 'bool', 'boolean',
                None, None,
                [], [],
                '''                Whether or not the operation start time was
                explicitly configured
                ''',
                'start_time_configured',
                'Cisco-IOS-XR-ethernet-cfm-oper', False, is_config=False),
            _MetaInfoClassMember('schedule-duration', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('0', '4294967295')], [],
                '''                Duration of a probe for the operation in seconds
                ''',
                'schedule_duration',
                'Cisco-IOS-XR-ethernet-cfm-oper', False, is_config=False),
            _MetaInfoClassMember('schedule-interval', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('0', '4294967295')], [],
                '''                Interval between the start times of consecutive
                probes,  in seconds.
                ''',
                'schedule_interval',
                'Cisco-IOS-XR-ethernet-cfm-oper', False, is_config=False),
            ],
            'Cisco-IOS-XR-ethernet-cfm-oper',
            'operation-schedule',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-ethernet-cfm-oper'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_sla_oper',
            is_config=False,
        ),
    },
    'Sla.Protocols.Ethernet.Operations.Operation.ProfileOptions.OperationMetric.MetricConfig' : {
        'meta_info' : _MetaInfoClass('Sla.Protocols.Ethernet.Operations.Operation.ProfileOptions.OperationMetric.MetricConfig', REFERENCE_CLASS,
            '''Configuration of the metric''',
            False, 
            [
            _MetaInfoClassMember('metric-type', REFERENCE_ENUM_CLASS, 'SlaRecordableMetric', 'Sla-recordable-metric',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper', 'SlaRecordableMetric',
                [], [],
                '''                Type of metric to which this configuration
                applies
                ''',
                'metric_type',
                'Cisco-IOS-XR-ethernet-cfm-oper', False, is_config=False),
            _MetaInfoClassMember('bins-count', ATTRIBUTE, 'int', 'uint16',
                None, None,
                [('0', '65535')], [],
                '''                Total number of bins into which to aggregate. 0
                if no aggregation.
                ''',
                'bins_count',
                'Cisco-IOS-XR-ethernet-cfm-oper', False, is_config=False),
            _MetaInfoClassMember('bins-width', ATTRIBUTE, 'int', 'uint16',
                None, None,
                [('0', '65535')], [],
                '''                Width of each bin into which to aggregate. 0 if
                no aggregation. For SLM, the units of this value
                are in single units of percent; for LMM they are
                in tenths of percent; for other measurements
                they are in milliseconds.
                ''',
                'bins_width',
                'Cisco-IOS-XR-ethernet-cfm-oper', False, is_config=False),
            _MetaInfoClassMember('bucket-size', ATTRIBUTE, 'int', 'uint8',
                None, None,
                [('0', '255')], [],
                '''                Size of buckets into which measurements are
                collected
                ''',
                'bucket_size',
                'Cisco-IOS-XR-ethernet-cfm-oper', False, is_config=False),
            _MetaInfoClassMember('bucket-size-unit', REFERENCE_ENUM_CLASS, 'SlaBucketSize', 'Sla-bucket-size',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper', 'SlaBucketSize',
                [], [],
                '''                Whether bucket size is 'per-probe' or 'probes'
                ''',
                'bucket_size_unit',
                'Cisco-IOS-XR-ethernet-cfm-oper', False, is_config=False),
            _MetaInfoClassMember('buckets-archive', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('0', '4294967295')], [],
                '''                Maximum number of buckets to store in memory
                ''',
                'buckets_archive',
                'Cisco-IOS-XR-ethernet-cfm-oper', False, is_config=False),
            ],
            'Cisco-IOS-XR-ethernet-cfm-oper',
            'metric-config',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-ethernet-cfm-oper'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_sla_oper',
            is_config=False,
        ),
    },
    'Sla.Protocols.Ethernet.Operations.Operation.ProfileOptions.OperationMetric' : {
        'meta_info' : _MetaInfoClass('Sla.Protocols.Ethernet.Operations.Operation.ProfileOptions.OperationMetric', REFERENCE_LIST,
            '''Array of the metrics that are measured by the
operation''',
            False, 
            [
            _MetaInfoClassMember('metric-config', REFERENCE_CLASS, 'MetricConfig', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_sla_oper', 'Sla.Protocols.Ethernet.Operations.Operation.ProfileOptions.OperationMetric.MetricConfig',
                [], [],
                '''                Configuration of the metric
                ''',
                'metric_config',
                'Cisco-IOS-XR-ethernet-cfm-oper', False, is_config=False),
            _MetaInfoClassMember('current-buckets-archive', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('0', '4294967295')], [],
                '''                Number of valid buckets currently in the buckets
                archive
                ''',
                'current_buckets_archive',
                'Cisco-IOS-XR-ethernet-cfm-oper', False, is_config=False),
            ],
            'Cisco-IOS-XR-ethernet-cfm-oper',
            'operation-metric',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-ethernet-cfm-oper'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_sla_oper',
            is_config=False,
        ),
    },
    'Sla.Protocols.Ethernet.Operations.Operation.ProfileOptions' : {
        'meta_info' : _MetaInfoClass('Sla.Protocols.Ethernet.Operations.Operation.ProfileOptions', REFERENCE_CLASS,
            '''Options that are only valid if the operation has
a profile''',
            False, 
            [
            _MetaInfoClassMember('packet-padding', REFERENCE_CLASS, 'PacketPadding', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_sla_oper', 'Sla.Protocols.Ethernet.Operations.Operation.ProfileOptions.PacketPadding',
                [], [],
                '''                Configuration of the packet padding
                ''',
                'packet_padding',
                'Cisco-IOS-XR-ethernet-cfm-oper', False, is_config=False),
            _MetaInfoClassMember('priority', REFERENCE_CLASS, 'Priority', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_sla_oper', 'Sla.Protocols.Ethernet.Operations.Operation.ProfileOptions.Priority',
                [], [],
                '''                Priority at which to send the packet, if
                configured
                ''',
                'priority',
                'Cisco-IOS-XR-ethernet-cfm-oper', False, is_config=False),
            _MetaInfoClassMember('operation-schedule', REFERENCE_CLASS, 'OperationSchedule', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_sla_oper', 'Sla.Protocols.Ethernet.Operations.Operation.ProfileOptions.OperationSchedule',
                [], [],
                '''                Operation schedule
                ''',
                'operation_schedule',
                'Cisco-IOS-XR-ethernet-cfm-oper', False, is_config=False),
            _MetaInfoClassMember('probe-type', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                Type of probe used by the operation
                ''',
                'probe_type',
                'Cisco-IOS-XR-ethernet-cfm-oper', False, is_config=False),
            _MetaInfoClassMember('packets-per-burst', ATTRIBUTE, 'int', 'uint16',
                None, None,
                [('0', '65535')], [],
                '''                Number of packets sent per burst
                ''',
                'packets_per_burst',
                'Cisco-IOS-XR-ethernet-cfm-oper', False, is_config=False),
            _MetaInfoClassMember('inter-packet-interval', ATTRIBUTE, 'int', 'uint16',
                None, None,
                [('0', '65535')], [],
                '''                Interval between packets within a burst in
                milliseconds
                ''',
                'inter_packet_interval',
                'Cisco-IOS-XR-ethernet-cfm-oper', False, is_config=False),
            _MetaInfoClassMember('bursts-per-probe', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('0', '4294967295')], [],
                '''                Number of bursts sent per probe
                ''',
                'bursts_per_probe',
                'Cisco-IOS-XR-ethernet-cfm-oper', False, is_config=False),
            _MetaInfoClassMember('inter-burst-interval', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('0', '4294967295')], [],
                '''                Interval between bursts within a probe in
                milliseconds
                ''',
                'inter_burst_interval',
                'Cisco-IOS-XR-ethernet-cfm-oper', False, is_config=False),
            _MetaInfoClassMember('flr-calculation-interval', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('0', '4294967295')], [],
                '''                Interval between FLR calculations for SLM, in
                milliseconds
                ''',
                'flr_calculation_interval',
                'Cisco-IOS-XR-ethernet-cfm-oper', False, is_config=False),
            _MetaInfoClassMember('operation-metric', REFERENCE_LIST, 'OperationMetric', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_sla_oper', 'Sla.Protocols.Ethernet.Operations.Operation.ProfileOptions.OperationMetric',
                [], [],
                '''                Array of the metrics that are measured by the
                operation
                ''',
                'operation_metric',
                'Cisco-IOS-XR-ethernet-cfm-oper', False, is_config=False),
            ],
            'Cisco-IOS-XR-ethernet-cfm-oper',
            'profile-options',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-ethernet-cfm-oper'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_sla_oper',
            is_config=False,
        ),
    },
    'Sla.Protocols.Ethernet.Operations.Operation.SpecificOptions.ConfiguredOperationOptions' : {
        'meta_info' : _MetaInfoClass('Sla.Protocols.Ethernet.Operations.Operation.SpecificOptions.ConfiguredOperationOptions', REFERENCE_CLASS,
            '''Parameters for a configured operation''',
            False, 
            [
            _MetaInfoClassMember('profile-name', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                Name of the profile used by the operation
                ''',
                'profile_name',
                'Cisco-IOS-XR-ethernet-cfm-oper', False, is_config=False),
            ],
            'Cisco-IOS-XR-ethernet-cfm-oper',
            'configured-operation-options',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-ethernet-cfm-oper'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_sla_oper',
            is_config=False,
            has_when=True,
        ),
    },
    'Sla.Protocols.Ethernet.Operations.Operation.SpecificOptions.OndemandOperationOptions' : {
        'meta_info' : _MetaInfoClass('Sla.Protocols.Ethernet.Operations.Operation.SpecificOptions.OndemandOperationOptions', REFERENCE_CLASS,
            '''Parameters for an ondemand operation''',
            False, 
            [
            _MetaInfoClassMember('ondemand-operation-id', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('0', '4294967295')], [],
                '''                ID of the ondemand operation
                ''',
                'ondemand_operation_id',
                'Cisco-IOS-XR-ethernet-cfm-oper', False, is_config=False),
            _MetaInfoClassMember('probe-count', ATTRIBUTE, 'int', 'uint8',
                None, None,
                [('0', '255')], [],
                '''                Total number of probes sent during the operation
                ''',
                'probe_count',
                'Cisco-IOS-XR-ethernet-cfm-oper', False, is_config=False),
            ],
            'Cisco-IOS-XR-ethernet-cfm-oper',
            'ondemand-operation-options',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-ethernet-cfm-oper'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_sla_oper',
            is_config=False,
            has_when=True,
        ),
    },
    'Sla.Protocols.Ethernet.Operations.Operation.SpecificOptions' : {
        'meta_info' : _MetaInfoClass('Sla.Protocols.Ethernet.Operations.Operation.SpecificOptions', REFERENCE_CLASS,
            '''Options specific to the type of operation''',
            False, 
            [
            _MetaInfoClassMember('configured-operation-options', REFERENCE_CLASS, 'ConfiguredOperationOptions', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_sla_oper', 'Sla.Protocols.Ethernet.Operations.Operation.SpecificOptions.ConfiguredOperationOptions',
                [], [],
                '''                Parameters for a configured operation
                ''',
                'configured_operation_options',
                'Cisco-IOS-XR-ethernet-cfm-oper', False, is_config=False, has_when=True),
            _MetaInfoClassMember('ondemand-operation-options', REFERENCE_CLASS, 'OndemandOperationOptions', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_sla_oper', 'Sla.Protocols.Ethernet.Operations.Operation.SpecificOptions.OndemandOperationOptions',
                [], [],
                '''                Parameters for an ondemand operation
                ''',
                'ondemand_operation_options',
                'Cisco-IOS-XR-ethernet-cfm-oper', False, is_config=False, has_when=True),
            _MetaInfoClassMember('oper-type', REFERENCE_ENUM_CLASS, 'SlaOperOperation', 'Sla-oper-operation',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper', 'SlaOperOperation',
                [], [],
                '''                OperType
                ''',
                'oper_type',
                'Cisco-IOS-XR-ethernet-cfm-oper', False, is_config=False),
            ],
            'Cisco-IOS-XR-ethernet-cfm-oper',
            'specific-options',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-ethernet-cfm-oper'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_sla_oper',
            is_config=False,
        ),
    },
    'Sla.Protocols.Ethernet.Operations.Operation' : {
        'meta_info' : _MetaInfoClass('Sla.Protocols.Ethernet.Operations.Operation', REFERENCE_LIST,
            '''SLA operation to get operation data for''',
            False, 
            [
            _MetaInfoClassMember('profile-name', ATTRIBUTE, 'str', 'xr:Cisco-ios-xr-string',
                None, None,
                [], [b'[\\w\\-\\.:,_@#%$\\+=\\|;]+'],
                '''                Profile Name
                ''',
                'profile_name',
                'Cisco-IOS-XR-ethernet-cfm-oper', False, is_config=False),
            _MetaInfoClassMember('domain-name', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                Domain name
                ''',
                'domain_name',
                'Cisco-IOS-XR-ethernet-cfm-oper', False, is_config=False),
            _MetaInfoClassMember('interface-name', ATTRIBUTE, 'str', 'xr:Interface-name',
                None, None,
                [], [b'[a-zA-Z0-9._/-]+'],
                '''                Interface name
                ''',
                'interface_name',
                'Cisco-IOS-XR-ethernet-cfm-oper', False, is_config=False),
            _MetaInfoClassMember('mep-id', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('1', '8191')], [],
                '''                MEP ID in the range 1 to 8191. Either MEP ID
                or MAC address must be specified.
                ''',
                'mep_id',
                'Cisco-IOS-XR-ethernet-cfm-oper', False, is_config=False),
            _MetaInfoClassMember('mac-address', ATTRIBUTE, 'str', 'yang:mac-address',
                None, None,
                [], [b'[0-9a-fA-F]{2}(:[0-9a-fA-F]{2}){5}'],
                '''                Unicast MAC Address in xxxx.xxxx.xxxx format.
                Either MEP ID or MAC address must be
                specified.
                ''',
                'mac_address',
                'Cisco-IOS-XR-ethernet-cfm-oper', False, is_config=False),
            _MetaInfoClassMember('profile-options', REFERENCE_CLASS, 'ProfileOptions', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_sla_oper', 'Sla.Protocols.Ethernet.Operations.Operation.ProfileOptions',
                [], [],
                '''                Options that are only valid if the operation has
                a profile
                ''',
                'profile_options',
                'Cisco-IOS-XR-ethernet-cfm-oper', False, is_config=False),
            _MetaInfoClassMember('specific-options', REFERENCE_CLASS, 'SpecificOptions', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_sla_oper', 'Sla.Protocols.Ethernet.Operations.Operation.SpecificOptions',
                [], [],
                '''                Options specific to the type of operation
                ''',
                'specific_options',
                'Cisco-IOS-XR-ethernet-cfm-oper', False, is_config=False),
            _MetaInfoClassMember('display-short', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                Short display name used by the operation
                ''',
                'display_short',
                'Cisco-IOS-XR-ethernet-cfm-oper', False, is_config=False),
            _MetaInfoClassMember('display-long', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                Long display name used by the operation
                ''',
                'display_long',
                'Cisco-IOS-XR-ethernet-cfm-oper', False, is_config=False),
            _MetaInfoClassMember('last-run', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('0', '4294967295')], [],
                '''                Time that the last probe for the operation was
                run, NULL if never run.
                ''',
                'last_run',
                'Cisco-IOS-XR-ethernet-cfm-oper', False, is_config=False),
            ],
            'Cisco-IOS-XR-ethernet-cfm-oper',
            'operation',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-ethernet-cfm-oper'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_sla_oper',
            is_config=False,
        ),
    },
    'Sla.Protocols.Ethernet.Operations' : {
        'meta_info' : _MetaInfoClass('Sla.Protocols.Ethernet.Operations', REFERENCE_CLASS,
            '''Table of SLA operations''',
            False, 
            [
            _MetaInfoClassMember('operation', REFERENCE_LIST, 'Operation', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_sla_oper', 'Sla.Protocols.Ethernet.Operations.Operation',
                [], [],
                '''                SLA operation to get operation data for
                ''',
                'operation_',
                'Cisco-IOS-XR-ethernet-cfm-oper', False, is_config=False),
            ],
            'Cisco-IOS-XR-ethernet-cfm-oper',
            'operations',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-ethernet-cfm-oper'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_sla_oper',
            is_config=False,
        ),
    },
    'Sla.Protocols.Ethernet.StatisticsHistoricals.StatisticsHistorical.SpecificOptions.ConfiguredOperationOptions' : {
        'meta_info' : _MetaInfoClass('Sla.Protocols.Ethernet.StatisticsHistoricals.StatisticsHistorical.SpecificOptions.ConfiguredOperationOptions', REFERENCE_CLASS,
            '''Parameters for a configured operation''',
            False, 
            [
            _MetaInfoClassMember('profile-name', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                Name of the profile used by the operation
                ''',
                'profile_name',
                'Cisco-IOS-XR-ethernet-cfm-oper', False, is_config=False),
            ],
            'Cisco-IOS-XR-ethernet-cfm-oper',
            'configured-operation-options',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-ethernet-cfm-oper'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_sla_oper',
            is_config=False,
            has_when=True,
        ),
    },
    'Sla.Protocols.Ethernet.StatisticsHistoricals.StatisticsHistorical.SpecificOptions.OndemandOperationOptions' : {
        'meta_info' : _MetaInfoClass('Sla.Protocols.Ethernet.StatisticsHistoricals.StatisticsHistorical.SpecificOptions.OndemandOperationOptions', REFERENCE_CLASS,
            '''Parameters for an ondemand operation''',
            False, 
            [
            _MetaInfoClassMember('ondemand-operation-id', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('0', '4294967295')], [],
                '''                ID of the ondemand operation
                ''',
                'ondemand_operation_id',
                'Cisco-IOS-XR-ethernet-cfm-oper', False, is_config=False),
            _MetaInfoClassMember('probe-count', ATTRIBUTE, 'int', 'uint8',
                None, None,
                [('0', '255')], [],
                '''                Total number of probes sent during the operation
                ''',
                'probe_count',
                'Cisco-IOS-XR-ethernet-cfm-oper', False, is_config=False),
            ],
            'Cisco-IOS-XR-ethernet-cfm-oper',
            'ondemand-operation-options',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-ethernet-cfm-oper'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_sla_oper',
            is_config=False,
            has_when=True,
        ),
    },
    'Sla.Protocols.Ethernet.StatisticsHistoricals.StatisticsHistorical.SpecificOptions' : {
        'meta_info' : _MetaInfoClass('Sla.Protocols.Ethernet.StatisticsHistoricals.StatisticsHistorical.SpecificOptions', REFERENCE_CLASS,
            '''Options specific to the type of operation''',
            False, 
            [
            _MetaInfoClassMember('configured-operation-options', REFERENCE_CLASS, 'ConfiguredOperationOptions', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_sla_oper', 'Sla.Protocols.Ethernet.StatisticsHistoricals.StatisticsHistorical.SpecificOptions.ConfiguredOperationOptions',
                [], [],
                '''                Parameters for a configured operation
                ''',
                'configured_operation_options',
                'Cisco-IOS-XR-ethernet-cfm-oper', False, is_config=False, has_when=True),
            _MetaInfoClassMember('ondemand-operation-options', REFERENCE_CLASS, 'OndemandOperationOptions', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_sla_oper', 'Sla.Protocols.Ethernet.StatisticsHistoricals.StatisticsHistorical.SpecificOptions.OndemandOperationOptions',
                [], [],
                '''                Parameters for an ondemand operation
                ''',
                'ondemand_operation_options',
                'Cisco-IOS-XR-ethernet-cfm-oper', False, is_config=False, has_when=True),
            _MetaInfoClassMember('oper-type', REFERENCE_ENUM_CLASS, 'SlaOperOperation', 'Sla-oper-operation',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper', 'SlaOperOperation',
                [], [],
                '''                OperType
                ''',
                'oper_type',
                'Cisco-IOS-XR-ethernet-cfm-oper', False, is_config=False),
            ],
            'Cisco-IOS-XR-ethernet-cfm-oper',
            'specific-options',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-ethernet-cfm-oper'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_sla_oper',
            is_config=False,
        ),
    },
    'Sla.Protocols.Ethernet.StatisticsHistoricals.StatisticsHistorical.OperationSchedule' : {
        'meta_info' : _MetaInfoClass('Sla.Protocols.Ethernet.StatisticsHistoricals.StatisticsHistorical.OperationSchedule', REFERENCE_CLASS,
            '''Operation schedule''',
            False, 
            [
            _MetaInfoClassMember('start-time', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('0', '4294967295')], [],
                '''                Start time of the first probe, in seconds since
                the Unix Epoch
                ''',
                'start_time',
                'Cisco-IOS-XR-ethernet-cfm-oper', False, is_config=False),
            _MetaInfoClassMember('start-time-configured', ATTRIBUTE, 'bool', 'boolean',
                None, None,
                [], [],
                '''                Whether or not the operation start time was
                explicitly configured
                ''',
                'start_time_configured',
                'Cisco-IOS-XR-ethernet-cfm-oper', False, is_config=False),
            _MetaInfoClassMember('schedule-duration', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('0', '4294967295')], [],
                '''                Duration of a probe for the operation in seconds
                ''',
                'schedule_duration',
                'Cisco-IOS-XR-ethernet-cfm-oper', False, is_config=False),
            _MetaInfoClassMember('schedule-interval', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('0', '4294967295')], [],
                '''                Interval between the start times of consecutive
                probes,  in seconds.
                ''',
                'schedule_interval',
                'Cisco-IOS-XR-ethernet-cfm-oper', False, is_config=False),
            ],
            'Cisco-IOS-XR-ethernet-cfm-oper',
            'operation-schedule',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-ethernet-cfm-oper'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_sla_oper',
            is_config=False,
        ),
    },
    'Sla.Protocols.Ethernet.StatisticsHistoricals.StatisticsHistorical.OperationMetric.Config' : {
        'meta_info' : _MetaInfoClass('Sla.Protocols.Ethernet.StatisticsHistoricals.StatisticsHistorical.OperationMetric.Config', REFERENCE_CLASS,
            '''Configuration of the metric''',
            False, 
            [
            _MetaInfoClassMember('metric-type', REFERENCE_ENUM_CLASS, 'SlaRecordableMetric', 'Sla-recordable-metric',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper', 'SlaRecordableMetric',
                [], [],
                '''                Type of metric to which this configuration
                applies
                ''',
                'metric_type',
                'Cisco-IOS-XR-ethernet-cfm-oper', False, is_config=False),
            _MetaInfoClassMember('bins-count', ATTRIBUTE, 'int', 'uint16',
                None, None,
                [('0', '65535')], [],
                '''                Total number of bins into which to aggregate. 0
                if no aggregation.
                ''',
                'bins_count',
                'Cisco-IOS-XR-ethernet-cfm-oper', False, is_config=False),
            _MetaInfoClassMember('bins-width', ATTRIBUTE, 'int', 'uint16',
                None, None,
                [('0', '65535')], [],
                '''                Width of each bin into which to aggregate. 0 if
                no aggregation. For SLM, the units of this value
                are in single units of percent; for LMM they are
                in tenths of percent; for other measurements
                they are in milliseconds.
                ''',
                'bins_width',
                'Cisco-IOS-XR-ethernet-cfm-oper', False, is_config=False),
            _MetaInfoClassMember('bucket-size', ATTRIBUTE, 'int', 'uint8',
                None, None,
                [('0', '255')], [],
                '''                Size of buckets into which measurements are
                collected
                ''',
                'bucket_size',
                'Cisco-IOS-XR-ethernet-cfm-oper', False, is_config=False),
            _MetaInfoClassMember('bucket-size-unit', REFERENCE_ENUM_CLASS, 'SlaBucketSize', 'Sla-bucket-size',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper', 'SlaBucketSize',
                [], [],
                '''                Whether bucket size is 'per-probe' or 'probes'
                ''',
                'bucket_size_unit',
                'Cisco-IOS-XR-ethernet-cfm-oper', False, is_config=False),
            _MetaInfoClassMember('buckets-archive', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('0', '4294967295')], [],
                '''                Maximum number of buckets to store in memory
                ''',
                'buckets_archive',
                'Cisco-IOS-XR-ethernet-cfm-oper', False, is_config=False),
            ],
            'Cisco-IOS-XR-ethernet-cfm-oper',
            'config',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-ethernet-cfm-oper'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_sla_oper',
            is_config=False,
        ),
    },
    'Sla.Protocols.Ethernet.StatisticsHistoricals.StatisticsHistorical.OperationMetric.Bucket.Contents.Aggregated.Bins' : {
        'meta_info' : _MetaInfoClass('Sla.Protocols.Ethernet.StatisticsHistoricals.StatisticsHistorical.OperationMetric.Bucket.Contents.Aggregated.Bins', REFERENCE_LIST,
            '''The bins of an SLA metric bucket''',
            False, 
            [
            _MetaInfoClassMember('lower-bound', ATTRIBUTE, 'int', 'int32',
                None, None,
                [('-2147483648', '2147483647')], [],
                '''                Lower bound (inclusive) of the bin, in
                milliseconds or single units of percent. This
                field is not used for LMM measurements
                ''',
                'lower_bound',
                'Cisco-IOS-XR-ethernet-cfm-oper', False, is_config=False),
            _MetaInfoClassMember('upper-bound', ATTRIBUTE, 'int', 'int32',
                None, None,
                [('-2147483648', '2147483647')], [],
                '''                Upper bound (exclusive) of the bin, in
                milliseconds or single units of percent. This
                field is not used for LMM measurements
                ''',
                'upper_bound',
                'Cisco-IOS-XR-ethernet-cfm-oper', False, is_config=False),
            _MetaInfoClassMember('lower-bound-tenths', ATTRIBUTE, 'int', 'int32',
                None, None,
                [('-2147483648', '2147483647')], [],
                '''                Lower bound (inclusive) of the bin, in tenths of
                percent. This field is only used for LMM
                measurements
                ''',
                'lower_bound_tenths',
                'Cisco-IOS-XR-ethernet-cfm-oper', False, is_config=False),
            _MetaInfoClassMember('upper-bound-tenths', ATTRIBUTE, 'int', 'int32',
                None, None,
                [('-2147483648', '2147483647')], [],
                '''                Upper bound (exclusive) of the bin, in tenths of
                percent. This field is only used for LMM
                measurements
                ''',
                'upper_bound_tenths',
                'Cisco-IOS-XR-ethernet-cfm-oper', False, is_config=False),
            _MetaInfoClassMember('sum', ATTRIBUTE, 'int', 'int64',
                None, None,
                [('-9223372036854775808', '9223372036854775807')], [],
                '''                The sum of the results in the bin, in
                microseconds or millionths of a percent
                ''',
                'sum',
                'Cisco-IOS-XR-ethernet-cfm-oper', False, is_config=False),
            _MetaInfoClassMember('count', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('0', '4294967295')], [],
                '''                The total number of results in the bin
                ''',
                'count',
                'Cisco-IOS-XR-ethernet-cfm-oper', False, is_config=False),
            ],
            'Cisco-IOS-XR-ethernet-cfm-oper',
            'bins',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-ethernet-cfm-oper'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_sla_oper',
            is_config=False,
        ),
    },
    'Sla.Protocols.Ethernet.StatisticsHistoricals.StatisticsHistorical.OperationMetric.Bucket.Contents.Aggregated' : {
        'meta_info' : _MetaInfoClass('Sla.Protocols.Ethernet.StatisticsHistoricals.StatisticsHistorical.OperationMetric.Bucket.Contents.Aggregated', REFERENCE_CLASS,
            '''Result bins in an SLA metric bucket''',
            False, 
            [
            _MetaInfoClassMember('bins', REFERENCE_LIST, 'Bins', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_sla_oper', 'Sla.Protocols.Ethernet.StatisticsHistoricals.StatisticsHistorical.OperationMetric.Bucket.Contents.Aggregated.Bins',
                [], [],
                '''                The bins of an SLA metric bucket
                ''',
                'bins',
                'Cisco-IOS-XR-ethernet-cfm-oper', False, is_config=False),
            ],
            'Cisco-IOS-XR-ethernet-cfm-oper',
            'aggregated',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-ethernet-cfm-oper'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_sla_oper',
            is_config=False,
            has_when=True,
        ),
    },
    'Sla.Protocols.Ethernet.StatisticsHistoricals.StatisticsHistorical.OperationMetric.Bucket.Contents.Unaggregated.Sample' : {
        'meta_info' : _MetaInfoClass('Sla.Protocols.Ethernet.StatisticsHistoricals.StatisticsHistorical.OperationMetric.Bucket.Contents.Unaggregated.Sample', REFERENCE_LIST,
            '''The samples of an SLA metric bucket''',
            False, 
            [
            _MetaInfoClassMember('sent-at', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('0', '4294967295')], [],
                '''                The time (in milliseconds relative to the start
                time of the bucket) that the sample was sent at
                ''',
                'sent_at',
                'Cisco-IOS-XR-ethernet-cfm-oper', False, is_config=False),
            _MetaInfoClassMember('sent', ATTRIBUTE, 'bool', 'boolean',
                None, None,
                [], [],
                '''                Whether the sample packet was sucessfully sent
                ''',
                'sent',
                'Cisco-IOS-XR-ethernet-cfm-oper', False, is_config=False),
            _MetaInfoClassMember('timed-out', ATTRIBUTE, 'bool', 'boolean',
                None, None,
                [], [],
                '''                Whether the sample packet timed out
                ''',
                'timed_out',
                'Cisco-IOS-XR-ethernet-cfm-oper', False, is_config=False),
            _MetaInfoClassMember('corrupt', ATTRIBUTE, 'bool', 'boolean',
                None, None,
                [], [],
                '''                Whether the sample packet was corrupt
                ''',
                'corrupt',
                'Cisco-IOS-XR-ethernet-cfm-oper', False, is_config=False),
            _MetaInfoClassMember('out-of-order', ATTRIBUTE, 'bool', 'boolean',
                None, None,
                [], [],
                '''                Whether the sample packet was received
                out-of-order
                ''',
                'out_of_order',
                'Cisco-IOS-XR-ethernet-cfm-oper', False, is_config=False),
            _MetaInfoClassMember('no-data-packets', ATTRIBUTE, 'bool', 'boolean',
                None, None,
                [], [],
                '''                Whether a measurement could not be made because
                no data packets were sent in the sample period.
                Only applicable for LMM measurements
                ''',
                'no_data_packets',
                'Cisco-IOS-XR-ethernet-cfm-oper', False, is_config=False),
            _MetaInfoClassMember('result', ATTRIBUTE, 'int', 'int32',
                None, None,
                [('-2147483648', '2147483647')], [],
                '''                The result (in microseconds or millionths of a
                percent) of the sample, if available
                ''',
                'result',
                'Cisco-IOS-XR-ethernet-cfm-oper', False, is_config=False),
            _MetaInfoClassMember('frames-sent', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('0', '4294967295')], [],
                '''                For FLR measurements, the number of frames sent,
                if available
                ''',
                'frames_sent',
                'Cisco-IOS-XR-ethernet-cfm-oper', False, is_config=False),
            _MetaInfoClassMember('frames-lost', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('0', '4294967295')], [],
                '''                For FLR measurements, the number of frames lost,
                if available
                ''',
                'frames_lost',
                'Cisco-IOS-XR-ethernet-cfm-oper', False, is_config=False),
            ],
            'Cisco-IOS-XR-ethernet-cfm-oper',
            'sample',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-ethernet-cfm-oper'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_sla_oper',
            is_config=False,
        ),
    },
    'Sla.Protocols.Ethernet.StatisticsHistoricals.StatisticsHistorical.OperationMetric.Bucket.Contents.Unaggregated' : {
        'meta_info' : _MetaInfoClass('Sla.Protocols.Ethernet.StatisticsHistoricals.StatisticsHistorical.OperationMetric.Bucket.Contents.Unaggregated', REFERENCE_CLASS,
            '''Result samples in an SLA metric bucket''',
            False, 
            [
            _MetaInfoClassMember('sample', REFERENCE_LIST, 'Sample', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_sla_oper', 'Sla.Protocols.Ethernet.StatisticsHistoricals.StatisticsHistorical.OperationMetric.Bucket.Contents.Unaggregated.Sample',
                [], [],
                '''                The samples of an SLA metric bucket
                ''',
                'sample',
                'Cisco-IOS-XR-ethernet-cfm-oper', False, is_config=False),
            ],
            'Cisco-IOS-XR-ethernet-cfm-oper',
            'unaggregated',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-ethernet-cfm-oper'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_sla_oper',
            is_config=False,
            has_when=True,
        ),
    },
    'Sla.Protocols.Ethernet.StatisticsHistoricals.StatisticsHistorical.OperationMetric.Bucket.Contents' : {
        'meta_info' : _MetaInfoClass('Sla.Protocols.Ethernet.StatisticsHistoricals.StatisticsHistorical.OperationMetric.Bucket.Contents', REFERENCE_CLASS,
            '''The contents of the bucket; bins or samples''',
            False, 
            [
            _MetaInfoClassMember('aggregated', REFERENCE_CLASS, 'Aggregated', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_sla_oper', 'Sla.Protocols.Ethernet.StatisticsHistoricals.StatisticsHistorical.OperationMetric.Bucket.Contents.Aggregated',
                [], [],
                '''                Result bins in an SLA metric bucket
                ''',
                'aggregated',
                'Cisco-IOS-XR-ethernet-cfm-oper', False, is_config=False, has_when=True),
            _MetaInfoClassMember('unaggregated', REFERENCE_CLASS, 'Unaggregated', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_sla_oper', 'Sla.Protocols.Ethernet.StatisticsHistoricals.StatisticsHistorical.OperationMetric.Bucket.Contents.Unaggregated',
                [], [],
                '''                Result samples in an SLA metric bucket
                ''',
                'unaggregated',
                'Cisco-IOS-XR-ethernet-cfm-oper', False, is_config=False, has_when=True),
            _MetaInfoClassMember('bucket-type', REFERENCE_ENUM_CLASS, 'SlaOperBucket', 'Sla-oper-bucket',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper', 'SlaOperBucket',
                [], [],
                '''                BucketType
                ''',
                'bucket_type',
                'Cisco-IOS-XR-ethernet-cfm-oper', False, is_config=False),
            ],
            'Cisco-IOS-XR-ethernet-cfm-oper',
            'contents',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-ethernet-cfm-oper'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_sla_oper',
            is_config=False,
        ),
    },
    'Sla.Protocols.Ethernet.StatisticsHistoricals.StatisticsHistorical.OperationMetric.Bucket' : {
        'meta_info' : _MetaInfoClass('Sla.Protocols.Ethernet.StatisticsHistoricals.StatisticsHistorical.OperationMetric.Bucket', REFERENCE_LIST,
            '''Buckets stored for the metric''',
            False, 
            [
            _MetaInfoClassMember('contents', REFERENCE_CLASS, 'Contents', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_sla_oper', 'Sla.Protocols.Ethernet.StatisticsHistoricals.StatisticsHistorical.OperationMetric.Bucket.Contents',
                [], [],
                '''                The contents of the bucket; bins or samples
                ''',
                'contents',
                'Cisco-IOS-XR-ethernet-cfm-oper', False, is_config=False),
            _MetaInfoClassMember('start-at', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('0', '4294967295')], [],
                '''                Absolute time that the bucket started being
                filled at
                ''',
                'start_at',
                'Cisco-IOS-XR-ethernet-cfm-oper', False, is_config=False),
            _MetaInfoClassMember('duration', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('0', '4294967295')], [],
                '''                Length of time for which the bucket is being
                filled in seconds
                ''',
                'duration',
                'Cisco-IOS-XR-ethernet-cfm-oper', False, is_config=False),
            _MetaInfoClassMember('sent', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('0', '4294967295')], [],
                '''                Number of packets sent in the probe
                ''',
                'sent',
                'Cisco-IOS-XR-ethernet-cfm-oper', False, is_config=False),
            _MetaInfoClassMember('lost', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('0', '4294967295')], [],
                '''                Number of lost packets in the probe
                ''',
                'lost',
                'Cisco-IOS-XR-ethernet-cfm-oper', False, is_config=False),
            _MetaInfoClassMember('corrupt', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('0', '4294967295')], [],
                '''                Number of corrupt packets in the probe
                ''',
                'corrupt',
                'Cisco-IOS-XR-ethernet-cfm-oper', False, is_config=False),
            _MetaInfoClassMember('out-of-order', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('0', '4294967295')], [],
                '''                Number of packets recieved out-of-order in the
                probe
                ''',
                'out_of_order',
                'Cisco-IOS-XR-ethernet-cfm-oper', False, is_config=False),
            _MetaInfoClassMember('duplicates', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('0', '4294967295')], [],
                '''                Number of duplicate packets received in the
                probe
                ''',
                'duplicates',
                'Cisco-IOS-XR-ethernet-cfm-oper', False, is_config=False),
            _MetaInfoClassMember('minimum', ATTRIBUTE, 'int', 'int32',
                None, None,
                [('-2147483648', '2147483647')], [],
                '''                Overall minimum result in the probe, in
                microseconds or millionths of a percent
                ''',
                'minimum',
                'Cisco-IOS-XR-ethernet-cfm-oper', False, is_config=False),
            _MetaInfoClassMember('maximum', ATTRIBUTE, 'int', 'int32',
                None, None,
                [('-2147483648', '2147483647')], [],
                '''                Overall minimum result in the probe, in
                microseconds or millionths of a percent
                ''',
                'maximum',
                'Cisco-IOS-XR-ethernet-cfm-oper', False, is_config=False),
            _MetaInfoClassMember('time-of-minimum', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('0', '4294967295')], [],
                '''                Absolute time that the minimum value was
                recorded
                ''',
                'time_of_minimum',
                'Cisco-IOS-XR-ethernet-cfm-oper', False, is_config=False),
            _MetaInfoClassMember('time-of-maximum', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('0', '4294967295')], [],
                '''                Absolute time that the maximum value was
                recorded
                ''',
                'time_of_maximum',
                'Cisco-IOS-XR-ethernet-cfm-oper', False, is_config=False),
            _MetaInfoClassMember('average', ATTRIBUTE, 'int', 'int32',
                None, None,
                [('-2147483648', '2147483647')], [],
                '''                Mean of the results in the probe, in
                microseconds or millionths of a percent
                ''',
                'average',
                'Cisco-IOS-XR-ethernet-cfm-oper', False, is_config=False),
            _MetaInfoClassMember('standard-deviation', ATTRIBUTE, 'int', 'int32',
                None, None,
                [('-2147483648', '2147483647')], [],
                '''                Standard deviation of the results in the probe,
                in microseconds or millionths of a percent
                ''',
                'standard_deviation',
                'Cisco-IOS-XR-ethernet-cfm-oper', False, is_config=False),
            _MetaInfoClassMember('result-count', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('0', '4294967295')], [],
                '''                The count of samples collected in the bucket.
                ''',
                'result_count',
                'Cisco-IOS-XR-ethernet-cfm-oper', False, is_config=False),
            _MetaInfoClassMember('data-sent-count', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('0', '4294967295')], [],
                '''                The number of data packets sent across the
                bucket, used in the calculation of overall FLR.
                ''',
                'data_sent_count',
                'Cisco-IOS-XR-ethernet-cfm-oper', False, is_config=False),
            _MetaInfoClassMember('data-lost-count', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('0', '4294967295')], [],
                '''                The number of data packets lost across the
                bucket, used in the calculation of overall FLR.
                ''',
                'data_lost_count',
                'Cisco-IOS-XR-ethernet-cfm-oper', False, is_config=False),
            _MetaInfoClassMember('overall-flr', ATTRIBUTE, 'int', 'int32',
                None, None,
                [('-2147483648', '2147483647')], [],
                '''                Frame Loss Ratio across the whole bucket, in
                millionths of a percent
                ''',
                'overall_flr',
                'Cisco-IOS-XR-ethernet-cfm-oper', False, is_config=False),
            _MetaInfoClassMember('suspect-start-mid-bucket', ATTRIBUTE, 'bool', 'boolean',
                None, None,
                [], [],
                '''                Results suspect due to a probe starting mid-way
                through a bucket
                ''',
                'suspect_start_mid_bucket',
                'Cisco-IOS-XR-ethernet-cfm-oper', False, is_config=False),
            _MetaInfoClassMember('suspect-schedule-latency', ATTRIBUTE, 'bool', 'boolean',
                None, None,
                [], [],
                '''                Results suspect due to scheduling latency
                causing one or more packets to not be sent
                ''',
                'suspect_schedule_latency',
                'Cisco-IOS-XR-ethernet-cfm-oper', False, is_config=False),
            _MetaInfoClassMember('suspect-send-fail', ATTRIBUTE, 'bool', 'boolean',
                None, None,
                [], [],
                '''                Results suspect due to failure to send one or
                more packets
                ''',
                'suspect_send_fail',
                'Cisco-IOS-XR-ethernet-cfm-oper', False, is_config=False),
            _MetaInfoClassMember('suspect-premature-end', ATTRIBUTE, 'bool', 'boolean',
                None, None,
                [], [],
                '''                Results suspect due to a probe ending
                prematurely
                ''',
                'suspect_premature_end',
                'Cisco-IOS-XR-ethernet-cfm-oper', False, is_config=False),
            _MetaInfoClassMember('suspect-clock-drift', ATTRIBUTE, 'bool', 'boolean',
                None, None,
                [], [],
                '''                Results suspect as more than 10 seconds time
                drift detected
                ''',
                'suspect_clock_drift',
                'Cisco-IOS-XR-ethernet-cfm-oper', False, is_config=False),
            _MetaInfoClassMember('suspect-memory-allocation-failed', ATTRIBUTE, 'bool', 'boolean',
                None, None,
                [], [],
                '''                Results suspect due to a memory allocation
                failure
                ''',
                'suspect_memory_allocation_failed',
                'Cisco-IOS-XR-ethernet-cfm-oper', False, is_config=False),
            _MetaInfoClassMember('suspect-cleared-mid-bucket', ATTRIBUTE, 'bool', 'boolean',
                None, None,
                [], [],
                '''                Results suspect as bucket was cleared mid-way
                through being filled
                ''',
                'suspect_cleared_mid_bucket',
                'Cisco-IOS-XR-ethernet-cfm-oper', False, is_config=False),
            _MetaInfoClassMember('suspect-probe-restarted', ATTRIBUTE, 'bool', 'boolean',
                None, None,
                [], [],
                '''                Results suspect as probe restarted mid-way
                through the bucket
                ''',
                'suspect_probe_restarted',
                'Cisco-IOS-XR-ethernet-cfm-oper', False, is_config=False),
            _MetaInfoClassMember('suspect-management-latency', ATTRIBUTE, 'bool', 'boolean',
                None, None,
                [], [],
                '''                Results suspect as processing of results has
                been delayed
                ''',
                'suspect_management_latency',
                'Cisco-IOS-XR-ethernet-cfm-oper', False, is_config=False),
            _MetaInfoClassMember('suspect-multiple-buckets', ATTRIBUTE, 'bool', 'boolean',
                None, None,
                [], [],
                '''                Results suspect as the probe has been configured
                across multiple buckets
                ''',
                'suspect_multiple_buckets',
                'Cisco-IOS-XR-ethernet-cfm-oper', False, is_config=False),
            _MetaInfoClassMember('suspect-misordering', ATTRIBUTE, 'bool', 'boolean',
                None, None,
                [], [],
                '''                Results suspect as misordering has been detected
                , affecting results
                ''',
                'suspect_misordering',
                'Cisco-IOS-XR-ethernet-cfm-oper', False, is_config=False),
            _MetaInfoClassMember('suspect-flr-low-packet-count', ATTRIBUTE, 'bool', 'boolean',
                None, None,
                [], [],
                '''                Results suspect as FLR calculated based on a low
                packet count
                ''',
                'suspect_flr_low_packet_count',
                'Cisco-IOS-XR-ethernet-cfm-oper', False, is_config=False),
            _MetaInfoClassMember('premature-reason', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('0', '4294967295')], [],
                '''                If the probe ended prematurely, the error that
                caused a probe to end
                ''',
                'premature_reason',
                'Cisco-IOS-XR-ethernet-cfm-oper', False, is_config=False),
            _MetaInfoClassMember('premature-reason-string', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                Description of the error code that caused the
                probe to end prematurely. For informational
                purposes only
                ''',
                'premature_reason_string',
                'Cisco-IOS-XR-ethernet-cfm-oper', False, is_config=False),
            ],
            'Cisco-IOS-XR-ethernet-cfm-oper',
            'bucket',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-ethernet-cfm-oper'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_sla_oper',
            is_config=False,
        ),
    },
    'Sla.Protocols.Ethernet.StatisticsHistoricals.StatisticsHistorical.OperationMetric' : {
        'meta_info' : _MetaInfoClass('Sla.Protocols.Ethernet.StatisticsHistoricals.StatisticsHistorical.OperationMetric', REFERENCE_LIST,
            '''Metrics gathered for the operation''',
            False, 
            [
            _MetaInfoClassMember('config', REFERENCE_CLASS, 'Config', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_sla_oper', 'Sla.Protocols.Ethernet.StatisticsHistoricals.StatisticsHistorical.OperationMetric.Config',
                [], [],
                '''                Configuration of the metric
                ''',
                'config',
                'Cisco-IOS-XR-ethernet-cfm-oper', False, is_config=False),
            _MetaInfoClassMember('bucket', REFERENCE_LIST, 'Bucket', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_sla_oper', 'Sla.Protocols.Ethernet.StatisticsHistoricals.StatisticsHistorical.OperationMetric.Bucket',
                [], [],
                '''                Buckets stored for the metric
                ''',
                'bucket',
                'Cisco-IOS-XR-ethernet-cfm-oper', False, is_config=False),
            ],
            'Cisco-IOS-XR-ethernet-cfm-oper',
            'operation-metric',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-ethernet-cfm-oper'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_sla_oper',
            is_config=False,
        ),
    },
    'Sla.Protocols.Ethernet.StatisticsHistoricals.StatisticsHistorical' : {
        'meta_info' : _MetaInfoClass('Sla.Protocols.Ethernet.StatisticsHistoricals.StatisticsHistorical', REFERENCE_LIST,
            '''Historical statistics data for an SLA
configured operation''',
            False, 
            [
            _MetaInfoClassMember('profile-name', ATTRIBUTE, 'str', 'xr:Cisco-ios-xr-string',
                None, None,
                [], [b'[\\w\\-\\.:,_@#%$\\+=\\|;]+'],
                '''                Profile Name
                ''',
                'profile_name',
                'Cisco-IOS-XR-ethernet-cfm-oper', False, is_config=False),
            _MetaInfoClassMember('domain-name', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                Domain name
                ''',
                'domain_name',
                'Cisco-IOS-XR-ethernet-cfm-oper', False, is_config=False),
            _MetaInfoClassMember('interface-name', ATTRIBUTE, 'str', 'xr:Interface-name',
                None, None,
                [], [b'[a-zA-Z0-9._/-]+'],
                '''                Interface name
                ''',
                'interface_name',
                'Cisco-IOS-XR-ethernet-cfm-oper', False, is_config=False),
            _MetaInfoClassMember('mep-id', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('1', '8191')], [],
                '''                MEP ID in the range 1 to 8191. Either MEP ID
                or MAC address must be specified.
                ''',
                'mep_id',
                'Cisco-IOS-XR-ethernet-cfm-oper', False, is_config=False),
            _MetaInfoClassMember('mac-address', ATTRIBUTE, 'str', 'yang:mac-address',
                None, None,
                [], [b'[0-9a-fA-F]{2}(:[0-9a-fA-F]{2}){5}'],
                '''                Unicast MAC Address in xxxx.xxxx.xxxx format.
                Either MEP ID or MAC address must be
                specified.
                ''',
                'mac_address',
                'Cisco-IOS-XR-ethernet-cfm-oper', False, is_config=False),
            _MetaInfoClassMember('specific-options', REFERENCE_CLASS, 'SpecificOptions', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_sla_oper', 'Sla.Protocols.Ethernet.StatisticsHistoricals.StatisticsHistorical.SpecificOptions',
                [], [],
                '''                Options specific to the type of operation
                ''',
                'specific_options',
                'Cisco-IOS-XR-ethernet-cfm-oper', False, is_config=False),
            _MetaInfoClassMember('operation-schedule', REFERENCE_CLASS, 'OperationSchedule', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_sla_oper', 'Sla.Protocols.Ethernet.StatisticsHistoricals.StatisticsHistorical.OperationSchedule',
                [], [],
                '''                Operation schedule
                ''',
                'operation_schedule',
                'Cisco-IOS-XR-ethernet-cfm-oper', False, is_config=False),
            _MetaInfoClassMember('probe-type', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                Type of probe used by the operation
                ''',
                'probe_type',
                'Cisco-IOS-XR-ethernet-cfm-oper', False, is_config=False),
            _MetaInfoClassMember('display-short', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                Short display name used by the operation
                ''',
                'display_short',
                'Cisco-IOS-XR-ethernet-cfm-oper', False, is_config=False),
            _MetaInfoClassMember('display-long', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                Long display name used by the operation
                ''',
                'display_long',
                'Cisco-IOS-XR-ethernet-cfm-oper', False, is_config=False),
            _MetaInfoClassMember('flr-calculation-interval', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('0', '4294967295')], [],
                '''                Interval between FLR calculations for SLM, in
                milliseconds
                ''',
                'flr_calculation_interval',
                'Cisco-IOS-XR-ethernet-cfm-oper', False, is_config=False),
            _MetaInfoClassMember('operation-metric', REFERENCE_LIST, 'OperationMetric', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_sla_oper', 'Sla.Protocols.Ethernet.StatisticsHistoricals.StatisticsHistorical.OperationMetric',
                [], [],
                '''                Metrics gathered for the operation
                ''',
                'operation_metric',
                'Cisco-IOS-XR-ethernet-cfm-oper', False, is_config=False),
            ],
            'Cisco-IOS-XR-ethernet-cfm-oper',
            'statistics-historical',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-ethernet-cfm-oper'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_sla_oper',
            is_config=False,
        ),
    },
    'Sla.Protocols.Ethernet.StatisticsHistoricals' : {
        'meta_info' : _MetaInfoClass('Sla.Protocols.Ethernet.StatisticsHistoricals', REFERENCE_CLASS,
            '''Table of historical statistics for SLA
operations''',
            False, 
            [
            _MetaInfoClassMember('statistics-historical', REFERENCE_LIST, 'StatisticsHistorical', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_sla_oper', 'Sla.Protocols.Ethernet.StatisticsHistoricals.StatisticsHistorical',
                [], [],
                '''                Historical statistics data for an SLA
                configured operation
                ''',
                'statistics_historical',
                'Cisco-IOS-XR-ethernet-cfm-oper', False, is_config=False),
            ],
            'Cisco-IOS-XR-ethernet-cfm-oper',
            'statistics-historicals',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-ethernet-cfm-oper'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_sla_oper',
            is_config=False,
        ),
    },
    'Sla.Protocols.Ethernet.StatisticsOnDemandHistoricals.StatisticsOnDemandHistorical.SpecificOptions.ConfiguredOperationOptions' : {
        'meta_info' : _MetaInfoClass('Sla.Protocols.Ethernet.StatisticsOnDemandHistoricals.StatisticsOnDemandHistorical.SpecificOptions.ConfiguredOperationOptions', REFERENCE_CLASS,
            '''Parameters for a configured operation''',
            False, 
            [
            _MetaInfoClassMember('profile-name', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                Name of the profile used by the operation
                ''',
                'profile_name',
                'Cisco-IOS-XR-ethernet-cfm-oper', False, is_config=False),
            ],
            'Cisco-IOS-XR-ethernet-cfm-oper',
            'configured-operation-options',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-ethernet-cfm-oper'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_sla_oper',
            is_config=False,
            has_when=True,
        ),
    },
    'Sla.Protocols.Ethernet.StatisticsOnDemandHistoricals.StatisticsOnDemandHistorical.SpecificOptions.OndemandOperationOptions' : {
        'meta_info' : _MetaInfoClass('Sla.Protocols.Ethernet.StatisticsOnDemandHistoricals.StatisticsOnDemandHistorical.SpecificOptions.OndemandOperationOptions', REFERENCE_CLASS,
            '''Parameters for an ondemand operation''',
            False, 
            [
            _MetaInfoClassMember('ondemand-operation-id', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('0', '4294967295')], [],
                '''                ID of the ondemand operation
                ''',
                'ondemand_operation_id',
                'Cisco-IOS-XR-ethernet-cfm-oper', False, is_config=False),
            _MetaInfoClassMember('probe-count', ATTRIBUTE, 'int', 'uint8',
                None, None,
                [('0', '255')], [],
                '''                Total number of probes sent during the operation
                ''',
                'probe_count',
                'Cisco-IOS-XR-ethernet-cfm-oper', False, is_config=False),
            ],
            'Cisco-IOS-XR-ethernet-cfm-oper',
            'ondemand-operation-options',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-ethernet-cfm-oper'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_sla_oper',
            is_config=False,
            has_when=True,
        ),
    },
    'Sla.Protocols.Ethernet.StatisticsOnDemandHistoricals.StatisticsOnDemandHistorical.SpecificOptions' : {
        'meta_info' : _MetaInfoClass('Sla.Protocols.Ethernet.StatisticsOnDemandHistoricals.StatisticsOnDemandHistorical.SpecificOptions', REFERENCE_CLASS,
            '''Options specific to the type of operation''',
            False, 
            [
            _MetaInfoClassMember('configured-operation-options', REFERENCE_CLASS, 'ConfiguredOperationOptions', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_sla_oper', 'Sla.Protocols.Ethernet.StatisticsOnDemandHistoricals.StatisticsOnDemandHistorical.SpecificOptions.ConfiguredOperationOptions',
                [], [],
                '''                Parameters for a configured operation
                ''',
                'configured_operation_options',
                'Cisco-IOS-XR-ethernet-cfm-oper', False, is_config=False, has_when=True),
            _MetaInfoClassMember('ondemand-operation-options', REFERENCE_CLASS, 'OndemandOperationOptions', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_sla_oper', 'Sla.Protocols.Ethernet.StatisticsOnDemandHistoricals.StatisticsOnDemandHistorical.SpecificOptions.OndemandOperationOptions',
                [], [],
                '''                Parameters for an ondemand operation
                ''',
                'ondemand_operation_options',
                'Cisco-IOS-XR-ethernet-cfm-oper', False, is_config=False, has_when=True),
            _MetaInfoClassMember('oper-type', REFERENCE_ENUM_CLASS, 'SlaOperOperation', 'Sla-oper-operation',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper', 'SlaOperOperation',
                [], [],
                '''                OperType
                ''',
                'oper_type',
                'Cisco-IOS-XR-ethernet-cfm-oper', False, is_config=False),
            ],
            'Cisco-IOS-XR-ethernet-cfm-oper',
            'specific-options',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-ethernet-cfm-oper'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_sla_oper',
            is_config=False,
        ),
    },
    'Sla.Protocols.Ethernet.StatisticsOnDemandHistoricals.StatisticsOnDemandHistorical.OperationSchedule' : {
        'meta_info' : _MetaInfoClass('Sla.Protocols.Ethernet.StatisticsOnDemandHistoricals.StatisticsOnDemandHistorical.OperationSchedule', REFERENCE_CLASS,
            '''Operation schedule''',
            False, 
            [
            _MetaInfoClassMember('start-time', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('0', '4294967295')], [],
                '''                Start time of the first probe, in seconds since
                the Unix Epoch
                ''',
                'start_time',
                'Cisco-IOS-XR-ethernet-cfm-oper', False, is_config=False),
            _MetaInfoClassMember('start-time-configured', ATTRIBUTE, 'bool', 'boolean',
                None, None,
                [], [],
                '''                Whether or not the operation start time was
                explicitly configured
                ''',
                'start_time_configured',
                'Cisco-IOS-XR-ethernet-cfm-oper', False, is_config=False),
            _MetaInfoClassMember('schedule-duration', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('0', '4294967295')], [],
                '''                Duration of a probe for the operation in seconds
                ''',
                'schedule_duration',
                'Cisco-IOS-XR-ethernet-cfm-oper', False, is_config=False),
            _MetaInfoClassMember('schedule-interval', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('0', '4294967295')], [],
                '''                Interval between the start times of consecutive
                probes,  in seconds.
                ''',
                'schedule_interval',
                'Cisco-IOS-XR-ethernet-cfm-oper', False, is_config=False),
            ],
            'Cisco-IOS-XR-ethernet-cfm-oper',
            'operation-schedule',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-ethernet-cfm-oper'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_sla_oper',
            is_config=False,
        ),
    },
    'Sla.Protocols.Ethernet.StatisticsOnDemandHistoricals.StatisticsOnDemandHistorical.OperationMetric.Config' : {
        'meta_info' : _MetaInfoClass('Sla.Protocols.Ethernet.StatisticsOnDemandHistoricals.StatisticsOnDemandHistorical.OperationMetric.Config', REFERENCE_CLASS,
            '''Configuration of the metric''',
            False, 
            [
            _MetaInfoClassMember('metric-type', REFERENCE_ENUM_CLASS, 'SlaRecordableMetric', 'Sla-recordable-metric',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper', 'SlaRecordableMetric',
                [], [],
                '''                Type of metric to which this configuration
                applies
                ''',
                'metric_type',
                'Cisco-IOS-XR-ethernet-cfm-oper', False, is_config=False),
            _MetaInfoClassMember('bins-count', ATTRIBUTE, 'int', 'uint16',
                None, None,
                [('0', '65535')], [],
                '''                Total number of bins into which to aggregate. 0
                if no aggregation.
                ''',
                'bins_count',
                'Cisco-IOS-XR-ethernet-cfm-oper', False, is_config=False),
            _MetaInfoClassMember('bins-width', ATTRIBUTE, 'int', 'uint16',
                None, None,
                [('0', '65535')], [],
                '''                Width of each bin into which to aggregate. 0 if
                no aggregation. For SLM, the units of this value
                are in single units of percent; for LMM they are
                in tenths of percent; for other measurements
                they are in milliseconds.
                ''',
                'bins_width',
                'Cisco-IOS-XR-ethernet-cfm-oper', False, is_config=False),
            _MetaInfoClassMember('bucket-size', ATTRIBUTE, 'int', 'uint8',
                None, None,
                [('0', '255')], [],
                '''                Size of buckets into which measurements are
                collected
                ''',
                'bucket_size',
                'Cisco-IOS-XR-ethernet-cfm-oper', False, is_config=False),
            _MetaInfoClassMember('bucket-size-unit', REFERENCE_ENUM_CLASS, 'SlaBucketSize', 'Sla-bucket-size',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper', 'SlaBucketSize',
                [], [],
                '''                Whether bucket size is 'per-probe' or 'probes'
                ''',
                'bucket_size_unit',
                'Cisco-IOS-XR-ethernet-cfm-oper', False, is_config=False),
            _MetaInfoClassMember('buckets-archive', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('0', '4294967295')], [],
                '''                Maximum number of buckets to store in memory
                ''',
                'buckets_archive',
                'Cisco-IOS-XR-ethernet-cfm-oper', False, is_config=False),
            ],
            'Cisco-IOS-XR-ethernet-cfm-oper',
            'config',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-ethernet-cfm-oper'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_sla_oper',
            is_config=False,
        ),
    },
    'Sla.Protocols.Ethernet.StatisticsOnDemandHistoricals.StatisticsOnDemandHistorical.OperationMetric.Bucket.Contents.Aggregated.Bins' : {
        'meta_info' : _MetaInfoClass('Sla.Protocols.Ethernet.StatisticsOnDemandHistoricals.StatisticsOnDemandHistorical.OperationMetric.Bucket.Contents.Aggregated.Bins', REFERENCE_LIST,
            '''The bins of an SLA metric bucket''',
            False, 
            [
            _MetaInfoClassMember('lower-bound', ATTRIBUTE, 'int', 'int32',
                None, None,
                [('-2147483648', '2147483647')], [],
                '''                Lower bound (inclusive) of the bin, in
                milliseconds or single units of percent. This
                field is not used for LMM measurements
                ''',
                'lower_bound',
                'Cisco-IOS-XR-ethernet-cfm-oper', False, is_config=False),
            _MetaInfoClassMember('upper-bound', ATTRIBUTE, 'int', 'int32',
                None, None,
                [('-2147483648', '2147483647')], [],
                '''                Upper bound (exclusive) of the bin, in
                milliseconds or single units of percent. This
                field is not used for LMM measurements
                ''',
                'upper_bound',
                'Cisco-IOS-XR-ethernet-cfm-oper', False, is_config=False),
            _MetaInfoClassMember('lower-bound-tenths', ATTRIBUTE, 'int', 'int32',
                None, None,
                [('-2147483648', '2147483647')], [],
                '''                Lower bound (inclusive) of the bin, in tenths of
                percent. This field is only used for LMM
                measurements
                ''',
                'lower_bound_tenths',
                'Cisco-IOS-XR-ethernet-cfm-oper', False, is_config=False),
            _MetaInfoClassMember('upper-bound-tenths', ATTRIBUTE, 'int', 'int32',
                None, None,
                [('-2147483648', '2147483647')], [],
                '''                Upper bound (exclusive) of the bin, in tenths of
                percent. This field is only used for LMM
                measurements
                ''',
                'upper_bound_tenths',
                'Cisco-IOS-XR-ethernet-cfm-oper', False, is_config=False),
            _MetaInfoClassMember('sum', ATTRIBUTE, 'int', 'int64',
                None, None,
                [('-9223372036854775808', '9223372036854775807')], [],
                '''                The sum of the results in the bin, in
                microseconds or millionths of a percent
                ''',
                'sum',
                'Cisco-IOS-XR-ethernet-cfm-oper', False, is_config=False),
            _MetaInfoClassMember('count', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('0', '4294967295')], [],
                '''                The total number of results in the bin
                ''',
                'count',
                'Cisco-IOS-XR-ethernet-cfm-oper', False, is_config=False),
            ],
            'Cisco-IOS-XR-ethernet-cfm-oper',
            'bins',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-ethernet-cfm-oper'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_sla_oper',
            is_config=False,
        ),
    },
    'Sla.Protocols.Ethernet.StatisticsOnDemandHistoricals.StatisticsOnDemandHistorical.OperationMetric.Bucket.Contents.Aggregated' : {
        'meta_info' : _MetaInfoClass('Sla.Protocols.Ethernet.StatisticsOnDemandHistoricals.StatisticsOnDemandHistorical.OperationMetric.Bucket.Contents.Aggregated', REFERENCE_CLASS,
            '''Result bins in an SLA metric bucket''',
            False, 
            [
            _MetaInfoClassMember('bins', REFERENCE_LIST, 'Bins', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_sla_oper', 'Sla.Protocols.Ethernet.StatisticsOnDemandHistoricals.StatisticsOnDemandHistorical.OperationMetric.Bucket.Contents.Aggregated.Bins',
                [], [],
                '''                The bins of an SLA metric bucket
                ''',
                'bins',
                'Cisco-IOS-XR-ethernet-cfm-oper', False, is_config=False),
            ],
            'Cisco-IOS-XR-ethernet-cfm-oper',
            'aggregated',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-ethernet-cfm-oper'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_sla_oper',
            is_config=False,
            has_when=True,
        ),
    },
    'Sla.Protocols.Ethernet.StatisticsOnDemandHistoricals.StatisticsOnDemandHistorical.OperationMetric.Bucket.Contents.Unaggregated.Sample' : {
        'meta_info' : _MetaInfoClass('Sla.Protocols.Ethernet.StatisticsOnDemandHistoricals.StatisticsOnDemandHistorical.OperationMetric.Bucket.Contents.Unaggregated.Sample', REFERENCE_LIST,
            '''The samples of an SLA metric bucket''',
            False, 
            [
            _MetaInfoClassMember('sent-at', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('0', '4294967295')], [],
                '''                The time (in milliseconds relative to the start
                time of the bucket) that the sample was sent at
                ''',
                'sent_at',
                'Cisco-IOS-XR-ethernet-cfm-oper', False, is_config=False),
            _MetaInfoClassMember('sent', ATTRIBUTE, 'bool', 'boolean',
                None, None,
                [], [],
                '''                Whether the sample packet was sucessfully sent
                ''',
                'sent',
                'Cisco-IOS-XR-ethernet-cfm-oper', False, is_config=False),
            _MetaInfoClassMember('timed-out', ATTRIBUTE, 'bool', 'boolean',
                None, None,
                [], [],
                '''                Whether the sample packet timed out
                ''',
                'timed_out',
                'Cisco-IOS-XR-ethernet-cfm-oper', False, is_config=False),
            _MetaInfoClassMember('corrupt', ATTRIBUTE, 'bool', 'boolean',
                None, None,
                [], [],
                '''                Whether the sample packet was corrupt
                ''',
                'corrupt',
                'Cisco-IOS-XR-ethernet-cfm-oper', False, is_config=False),
            _MetaInfoClassMember('out-of-order', ATTRIBUTE, 'bool', 'boolean',
                None, None,
                [], [],
                '''                Whether the sample packet was received
                out-of-order
                ''',
                'out_of_order',
                'Cisco-IOS-XR-ethernet-cfm-oper', False, is_config=False),
            _MetaInfoClassMember('no-data-packets', ATTRIBUTE, 'bool', 'boolean',
                None, None,
                [], [],
                '''                Whether a measurement could not be made because
                no data packets were sent in the sample period.
                Only applicable for LMM measurements
                ''',
                'no_data_packets',
                'Cisco-IOS-XR-ethernet-cfm-oper', False, is_config=False),
            _MetaInfoClassMember('result', ATTRIBUTE, 'int', 'int32',
                None, None,
                [('-2147483648', '2147483647')], [],
                '''                The result (in microseconds or millionths of a
                percent) of the sample, if available
                ''',
                'result',
                'Cisco-IOS-XR-ethernet-cfm-oper', False, is_config=False),
            _MetaInfoClassMember('frames-sent', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('0', '4294967295')], [],
                '''                For FLR measurements, the number of frames sent,
                if available
                ''',
                'frames_sent',
                'Cisco-IOS-XR-ethernet-cfm-oper', False, is_config=False),
            _MetaInfoClassMember('frames-lost', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('0', '4294967295')], [],
                '''                For FLR measurements, the number of frames lost,
                if available
                ''',
                'frames_lost',
                'Cisco-IOS-XR-ethernet-cfm-oper', False, is_config=False),
            ],
            'Cisco-IOS-XR-ethernet-cfm-oper',
            'sample',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-ethernet-cfm-oper'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_sla_oper',
            is_config=False,
        ),
    },
    'Sla.Protocols.Ethernet.StatisticsOnDemandHistoricals.StatisticsOnDemandHistorical.OperationMetric.Bucket.Contents.Unaggregated' : {
        'meta_info' : _MetaInfoClass('Sla.Protocols.Ethernet.StatisticsOnDemandHistoricals.StatisticsOnDemandHistorical.OperationMetric.Bucket.Contents.Unaggregated', REFERENCE_CLASS,
            '''Result samples in an SLA metric bucket''',
            False, 
            [
            _MetaInfoClassMember('sample', REFERENCE_LIST, 'Sample', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_sla_oper', 'Sla.Protocols.Ethernet.StatisticsOnDemandHistoricals.StatisticsOnDemandHistorical.OperationMetric.Bucket.Contents.Unaggregated.Sample',
                [], [],
                '''                The samples of an SLA metric bucket
                ''',
                'sample',
                'Cisco-IOS-XR-ethernet-cfm-oper', False, is_config=False),
            ],
            'Cisco-IOS-XR-ethernet-cfm-oper',
            'unaggregated',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-ethernet-cfm-oper'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_sla_oper',
            is_config=False,
            has_when=True,
        ),
    },
    'Sla.Protocols.Ethernet.StatisticsOnDemandHistoricals.StatisticsOnDemandHistorical.OperationMetric.Bucket.Contents' : {
        'meta_info' : _MetaInfoClass('Sla.Protocols.Ethernet.StatisticsOnDemandHistoricals.StatisticsOnDemandHistorical.OperationMetric.Bucket.Contents', REFERENCE_CLASS,
            '''The contents of the bucket; bins or samples''',
            False, 
            [
            _MetaInfoClassMember('aggregated', REFERENCE_CLASS, 'Aggregated', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_sla_oper', 'Sla.Protocols.Ethernet.StatisticsOnDemandHistoricals.StatisticsOnDemandHistorical.OperationMetric.Bucket.Contents.Aggregated',
                [], [],
                '''                Result bins in an SLA metric bucket
                ''',
                'aggregated',
                'Cisco-IOS-XR-ethernet-cfm-oper', False, is_config=False, has_when=True),
            _MetaInfoClassMember('unaggregated', REFERENCE_CLASS, 'Unaggregated', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_sla_oper', 'Sla.Protocols.Ethernet.StatisticsOnDemandHistoricals.StatisticsOnDemandHistorical.OperationMetric.Bucket.Contents.Unaggregated',
                [], [],
                '''                Result samples in an SLA metric bucket
                ''',
                'unaggregated',
                'Cisco-IOS-XR-ethernet-cfm-oper', False, is_config=False, has_when=True),
            _MetaInfoClassMember('bucket-type', REFERENCE_ENUM_CLASS, 'SlaOperBucket', 'Sla-oper-bucket',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper', 'SlaOperBucket',
                [], [],
                '''                BucketType
                ''',
                'bucket_type',
                'Cisco-IOS-XR-ethernet-cfm-oper', False, is_config=False),
            ],
            'Cisco-IOS-XR-ethernet-cfm-oper',
            'contents',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-ethernet-cfm-oper'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_sla_oper',
            is_config=False,
        ),
    },
    'Sla.Protocols.Ethernet.StatisticsOnDemandHistoricals.StatisticsOnDemandHistorical.OperationMetric.Bucket' : {
        'meta_info' : _MetaInfoClass('Sla.Protocols.Ethernet.StatisticsOnDemandHistoricals.StatisticsOnDemandHistorical.OperationMetric.Bucket', REFERENCE_LIST,
            '''Buckets stored for the metric''',
            False, 
            [
            _MetaInfoClassMember('contents', REFERENCE_CLASS, 'Contents', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_sla_oper', 'Sla.Protocols.Ethernet.StatisticsOnDemandHistoricals.StatisticsOnDemandHistorical.OperationMetric.Bucket.Contents',
                [], [],
                '''                The contents of the bucket; bins or samples
                ''',
                'contents',
                'Cisco-IOS-XR-ethernet-cfm-oper', False, is_config=False),
            _MetaInfoClassMember('start-at', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('0', '4294967295')], [],
                '''                Absolute time that the bucket started being
                filled at
                ''',
                'start_at',
                'Cisco-IOS-XR-ethernet-cfm-oper', False, is_config=False),
            _MetaInfoClassMember('duration', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('0', '4294967295')], [],
                '''                Length of time for which the bucket is being
                filled in seconds
                ''',
                'duration',
                'Cisco-IOS-XR-ethernet-cfm-oper', False, is_config=False),
            _MetaInfoClassMember('sent', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('0', '4294967295')], [],
                '''                Number of packets sent in the probe
                ''',
                'sent',
                'Cisco-IOS-XR-ethernet-cfm-oper', False, is_config=False),
            _MetaInfoClassMember('lost', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('0', '4294967295')], [],
                '''                Number of lost packets in the probe
                ''',
                'lost',
                'Cisco-IOS-XR-ethernet-cfm-oper', False, is_config=False),
            _MetaInfoClassMember('corrupt', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('0', '4294967295')], [],
                '''                Number of corrupt packets in the probe
                ''',
                'corrupt',
                'Cisco-IOS-XR-ethernet-cfm-oper', False, is_config=False),
            _MetaInfoClassMember('out-of-order', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('0', '4294967295')], [],
                '''                Number of packets recieved out-of-order in the
                probe
                ''',
                'out_of_order',
                'Cisco-IOS-XR-ethernet-cfm-oper', False, is_config=False),
            _MetaInfoClassMember('duplicates', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('0', '4294967295')], [],
                '''                Number of duplicate packets received in the
                probe
                ''',
                'duplicates',
                'Cisco-IOS-XR-ethernet-cfm-oper', False, is_config=False),
            _MetaInfoClassMember('minimum', ATTRIBUTE, 'int', 'int32',
                None, None,
                [('-2147483648', '2147483647')], [],
                '''                Overall minimum result in the probe, in
                microseconds or millionths of a percent
                ''',
                'minimum',
                'Cisco-IOS-XR-ethernet-cfm-oper', False, is_config=False),
            _MetaInfoClassMember('maximum', ATTRIBUTE, 'int', 'int32',
                None, None,
                [('-2147483648', '2147483647')], [],
                '''                Overall minimum result in the probe, in
                microseconds or millionths of a percent
                ''',
                'maximum',
                'Cisco-IOS-XR-ethernet-cfm-oper', False, is_config=False),
            _MetaInfoClassMember('time-of-minimum', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('0', '4294967295')], [],
                '''                Absolute time that the minimum value was
                recorded
                ''',
                'time_of_minimum',
                'Cisco-IOS-XR-ethernet-cfm-oper', False, is_config=False),
            _MetaInfoClassMember('time-of-maximum', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('0', '4294967295')], [],
                '''                Absolute time that the maximum value was
                recorded
                ''',
                'time_of_maximum',
                'Cisco-IOS-XR-ethernet-cfm-oper', False, is_config=False),
            _MetaInfoClassMember('average', ATTRIBUTE, 'int', 'int32',
                None, None,
                [('-2147483648', '2147483647')], [],
                '''                Mean of the results in the probe, in
                microseconds or millionths of a percent
                ''',
                'average',
                'Cisco-IOS-XR-ethernet-cfm-oper', False, is_config=False),
            _MetaInfoClassMember('standard-deviation', ATTRIBUTE, 'int', 'int32',
                None, None,
                [('-2147483648', '2147483647')], [],
                '''                Standard deviation of the results in the probe,
                in microseconds or millionths of a percent
                ''',
                'standard_deviation',
                'Cisco-IOS-XR-ethernet-cfm-oper', False, is_config=False),
            _MetaInfoClassMember('result-count', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('0', '4294967295')], [],
                '''                The count of samples collected in the bucket.
                ''',
                'result_count',
                'Cisco-IOS-XR-ethernet-cfm-oper', False, is_config=False),
            _MetaInfoClassMember('data-sent-count', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('0', '4294967295')], [],
                '''                The number of data packets sent across the
                bucket, used in the calculation of overall FLR.
                ''',
                'data_sent_count',
                'Cisco-IOS-XR-ethernet-cfm-oper', False, is_config=False),
            _MetaInfoClassMember('data-lost-count', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('0', '4294967295')], [],
                '''                The number of data packets lost across the
                bucket, used in the calculation of overall FLR.
                ''',
                'data_lost_count',
                'Cisco-IOS-XR-ethernet-cfm-oper', False, is_config=False),
            _MetaInfoClassMember('overall-flr', ATTRIBUTE, 'int', 'int32',
                None, None,
                [('-2147483648', '2147483647')], [],
                '''                Frame Loss Ratio across the whole bucket, in
                millionths of a percent
                ''',
                'overall_flr',
                'Cisco-IOS-XR-ethernet-cfm-oper', False, is_config=False),
            _MetaInfoClassMember('suspect-start-mid-bucket', ATTRIBUTE, 'bool', 'boolean',
                None, None,
                [], [],
                '''                Results suspect due to a probe starting mid-way
                through a bucket
                ''',
                'suspect_start_mid_bucket',
                'Cisco-IOS-XR-ethernet-cfm-oper', False, is_config=False),
            _MetaInfoClassMember('suspect-schedule-latency', ATTRIBUTE, 'bool', 'boolean',
                None, None,
                [], [],
                '''                Results suspect due to scheduling latency
                causing one or more packets to not be sent
                ''',
                'suspect_schedule_latency',
                'Cisco-IOS-XR-ethernet-cfm-oper', False, is_config=False),
            _MetaInfoClassMember('suspect-send-fail', ATTRIBUTE, 'bool', 'boolean',
                None, None,
                [], [],
                '''                Results suspect due to failure to send one or
                more packets
                ''',
                'suspect_send_fail',
                'Cisco-IOS-XR-ethernet-cfm-oper', False, is_config=False),
            _MetaInfoClassMember('suspect-premature-end', ATTRIBUTE, 'bool', 'boolean',
                None, None,
                [], [],
                '''                Results suspect due to a probe ending
                prematurely
                ''',
                'suspect_premature_end',
                'Cisco-IOS-XR-ethernet-cfm-oper', False, is_config=False),
            _MetaInfoClassMember('suspect-clock-drift', ATTRIBUTE, 'bool', 'boolean',
                None, None,
                [], [],
                '''                Results suspect as more than 10 seconds time
                drift detected
                ''',
                'suspect_clock_drift',
                'Cisco-IOS-XR-ethernet-cfm-oper', False, is_config=False),
            _MetaInfoClassMember('suspect-memory-allocation-failed', ATTRIBUTE, 'bool', 'boolean',
                None, None,
                [], [],
                '''                Results suspect due to a memory allocation
                failure
                ''',
                'suspect_memory_allocation_failed',
                'Cisco-IOS-XR-ethernet-cfm-oper', False, is_config=False),
            _MetaInfoClassMember('suspect-cleared-mid-bucket', ATTRIBUTE, 'bool', 'boolean',
                None, None,
                [], [],
                '''                Results suspect as bucket was cleared mid-way
                through being filled
                ''',
                'suspect_cleared_mid_bucket',
                'Cisco-IOS-XR-ethernet-cfm-oper', False, is_config=False),
            _MetaInfoClassMember('suspect-probe-restarted', ATTRIBUTE, 'bool', 'boolean',
                None, None,
                [], [],
                '''                Results suspect as probe restarted mid-way
                through the bucket
                ''',
                'suspect_probe_restarted',
                'Cisco-IOS-XR-ethernet-cfm-oper', False, is_config=False),
            _MetaInfoClassMember('suspect-management-latency', ATTRIBUTE, 'bool', 'boolean',
                None, None,
                [], [],
                '''                Results suspect as processing of results has
                been delayed
                ''',
                'suspect_management_latency',
                'Cisco-IOS-XR-ethernet-cfm-oper', False, is_config=False),
            _MetaInfoClassMember('suspect-multiple-buckets', ATTRIBUTE, 'bool', 'boolean',
                None, None,
                [], [],
                '''                Results suspect as the probe has been configured
                across multiple buckets
                ''',
                'suspect_multiple_buckets',
                'Cisco-IOS-XR-ethernet-cfm-oper', False, is_config=False),
            _MetaInfoClassMember('suspect-misordering', ATTRIBUTE, 'bool', 'boolean',
                None, None,
                [], [],
                '''                Results suspect as misordering has been detected
                , affecting results
                ''',
                'suspect_misordering',
                'Cisco-IOS-XR-ethernet-cfm-oper', False, is_config=False),
            _MetaInfoClassMember('suspect-flr-low-packet-count', ATTRIBUTE, 'bool', 'boolean',
                None, None,
                [], [],
                '''                Results suspect as FLR calculated based on a low
                packet count
                ''',
                'suspect_flr_low_packet_count',
                'Cisco-IOS-XR-ethernet-cfm-oper', False, is_config=False),
            _MetaInfoClassMember('premature-reason', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('0', '4294967295')], [],
                '''                If the probe ended prematurely, the error that
                caused a probe to end
                ''',
                'premature_reason',
                'Cisco-IOS-XR-ethernet-cfm-oper', False, is_config=False),
            _MetaInfoClassMember('premature-reason-string', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                Description of the error code that caused the
                probe to end prematurely. For informational
                purposes only
                ''',
                'premature_reason_string',
                'Cisco-IOS-XR-ethernet-cfm-oper', False, is_config=False),
            ],
            'Cisco-IOS-XR-ethernet-cfm-oper',
            'bucket',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-ethernet-cfm-oper'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_sla_oper',
            is_config=False,
        ),
    },
    'Sla.Protocols.Ethernet.StatisticsOnDemandHistoricals.StatisticsOnDemandHistorical.OperationMetric' : {
        'meta_info' : _MetaInfoClass('Sla.Protocols.Ethernet.StatisticsOnDemandHistoricals.StatisticsOnDemandHistorical.OperationMetric', REFERENCE_LIST,
            '''Metrics gathered for the operation''',
            False, 
            [
            _MetaInfoClassMember('config', REFERENCE_CLASS, 'Config', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_sla_oper', 'Sla.Protocols.Ethernet.StatisticsOnDemandHistoricals.StatisticsOnDemandHistorical.OperationMetric.Config',
                [], [],
                '''                Configuration of the metric
                ''',
                'config',
                'Cisco-IOS-XR-ethernet-cfm-oper', False, is_config=False),
            _MetaInfoClassMember('bucket', REFERENCE_LIST, 'Bucket', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_sla_oper', 'Sla.Protocols.Ethernet.StatisticsOnDemandHistoricals.StatisticsOnDemandHistorical.OperationMetric.Bucket',
                [], [],
                '''                Buckets stored for the metric
                ''',
                'bucket',
                'Cisco-IOS-XR-ethernet-cfm-oper', False, is_config=False),
            ],
            'Cisco-IOS-XR-ethernet-cfm-oper',
            'operation-metric',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-ethernet-cfm-oper'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_sla_oper',
            is_config=False,
        ),
    },
    'Sla.Protocols.Ethernet.StatisticsOnDemandHistoricals.StatisticsOnDemandHistorical' : {
        'meta_info' : _MetaInfoClass('Sla.Protocols.Ethernet.StatisticsOnDemandHistoricals.StatisticsOnDemandHistorical', REFERENCE_LIST,
            '''Historical statistics data for an SLA
on-demand  operation''',
            False, 
            [
            _MetaInfoClassMember('operation-id', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('1', '4294967295')], [],
                '''                Operation ID
                ''',
                'operation_id',
                'Cisco-IOS-XR-ethernet-cfm-oper', False, is_config=False),
            _MetaInfoClassMember('domain-name', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                Domain name
                ''',
                'domain_name',
                'Cisco-IOS-XR-ethernet-cfm-oper', False, is_config=False),
            _MetaInfoClassMember('interface-name', ATTRIBUTE, 'str', 'xr:Interface-name',
                None, None,
                [], [b'[a-zA-Z0-9._/-]+'],
                '''                Interface name
                ''',
                'interface_name',
                'Cisco-IOS-XR-ethernet-cfm-oper', False, is_config=False),
            _MetaInfoClassMember('mep-id', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('1', '8191')], [],
                '''                MEP ID in the range 1 to 8191. Either MEP ID
                or MAC address must be specified.
                ''',
                'mep_id',
                'Cisco-IOS-XR-ethernet-cfm-oper', False, is_config=False),
            _MetaInfoClassMember('mac-address', ATTRIBUTE, 'str', 'yang:mac-address',
                None, None,
                [], [b'[0-9a-fA-F]{2}(:[0-9a-fA-F]{2}){5}'],
                '''                Unicast MAC Address in xxxx.xxxx.xxxx format.
                Either MEP ID or MAC address must be
                specified.
                ''',
                'mac_address',
                'Cisco-IOS-XR-ethernet-cfm-oper', False, is_config=False),
            _MetaInfoClassMember('specific-options', REFERENCE_CLASS, 'SpecificOptions', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_sla_oper', 'Sla.Protocols.Ethernet.StatisticsOnDemandHistoricals.StatisticsOnDemandHistorical.SpecificOptions',
                [], [],
                '''                Options specific to the type of operation
                ''',
                'specific_options',
                'Cisco-IOS-XR-ethernet-cfm-oper', False, is_config=False),
            _MetaInfoClassMember('operation-schedule', REFERENCE_CLASS, 'OperationSchedule', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_sla_oper', 'Sla.Protocols.Ethernet.StatisticsOnDemandHistoricals.StatisticsOnDemandHistorical.OperationSchedule',
                [], [],
                '''                Operation schedule
                ''',
                'operation_schedule',
                'Cisco-IOS-XR-ethernet-cfm-oper', False, is_config=False),
            _MetaInfoClassMember('probe-type', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                Type of probe used by the operation
                ''',
                'probe_type',
                'Cisco-IOS-XR-ethernet-cfm-oper', False, is_config=False),
            _MetaInfoClassMember('display-short', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                Short display name used by the operation
                ''',
                'display_short',
                'Cisco-IOS-XR-ethernet-cfm-oper', False, is_config=False),
            _MetaInfoClassMember('display-long', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                Long display name used by the operation
                ''',
                'display_long',
                'Cisco-IOS-XR-ethernet-cfm-oper', False, is_config=False),
            _MetaInfoClassMember('flr-calculation-interval', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('0', '4294967295')], [],
                '''                Interval between FLR calculations for SLM, in
                milliseconds
                ''',
                'flr_calculation_interval',
                'Cisco-IOS-XR-ethernet-cfm-oper', False, is_config=False),
            _MetaInfoClassMember('operation-metric', REFERENCE_LIST, 'OperationMetric', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_sla_oper', 'Sla.Protocols.Ethernet.StatisticsOnDemandHistoricals.StatisticsOnDemandHistorical.OperationMetric',
                [], [],
                '''                Metrics gathered for the operation
                ''',
                'operation_metric',
                'Cisco-IOS-XR-ethernet-cfm-oper', False, is_config=False),
            ],
            'Cisco-IOS-XR-ethernet-cfm-oper',
            'statistics-on-demand-historical',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-ethernet-cfm-oper'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_sla_oper',
            is_config=False,
        ),
    },
    'Sla.Protocols.Ethernet.StatisticsOnDemandHistoricals' : {
        'meta_info' : _MetaInfoClass('Sla.Protocols.Ethernet.StatisticsOnDemandHistoricals', REFERENCE_CLASS,
            '''Table of historical statistics for SLA
on-demand operations''',
            False, 
            [
            _MetaInfoClassMember('statistics-on-demand-historical', REFERENCE_LIST, 'StatisticsOnDemandHistorical', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_sla_oper', 'Sla.Protocols.Ethernet.StatisticsOnDemandHistoricals.StatisticsOnDemandHistorical',
                [], [],
                '''                Historical statistics data for an SLA
                on-demand  operation
                ''',
                'statistics_on_demand_historical',
                'Cisco-IOS-XR-ethernet-cfm-oper', False, is_config=False),
            ],
            'Cisco-IOS-XR-ethernet-cfm-oper',
            'statistics-on-demand-historicals',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-ethernet-cfm-oper'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_sla_oper',
            is_config=False,
        ),
    },
    'Sla.Protocols.Ethernet.ConfigErrors.ConfigError' : {
        'meta_info' : _MetaInfoClass('Sla.Protocols.Ethernet.ConfigErrors.ConfigError', REFERENCE_LIST,
            '''SLA operation to get configuration errors data
for''',
            False, 
            [
            _MetaInfoClassMember('profile-name', ATTRIBUTE, 'str', 'xr:Cisco-ios-xr-string',
                None, None,
                [], [b'[\\w\\-\\.:,_@#%$\\+=\\|;]+'],
                '''                Profile Name
                ''',
                'profile_name',
                'Cisco-IOS-XR-ethernet-cfm-oper', False, is_config=False),
            _MetaInfoClassMember('domain-name', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                Domain name
                ''',
                'domain_name',
                'Cisco-IOS-XR-ethernet-cfm-oper', False, is_config=False),
            _MetaInfoClassMember('interface-name', ATTRIBUTE, 'str', 'xr:Interface-name',
                None, None,
                [], [b'[a-zA-Z0-9._/-]+'],
                '''                Interface name
                ''',
                'interface_name',
                'Cisco-IOS-XR-ethernet-cfm-oper', False, is_config=False),
            _MetaInfoClassMember('mep-id', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('1', '8191')], [],
                '''                MEP ID in the range 1 to 8191
                ''',
                'mep_id',
                'Cisco-IOS-XR-ethernet-cfm-oper', False, is_config=False),
            _MetaInfoClassMember('mac-address', ATTRIBUTE, 'str', 'yang:mac-address',
                None, None,
                [], [b'[0-9a-fA-F]{2}(:[0-9a-fA-F]{2}){5}'],
                '''                Unicast MAC Address in xxxx.xxxx.xxxx format
                ''',
                'mac_address',
                'Cisco-IOS-XR-ethernet-cfm-oper', False, is_config=False),
            _MetaInfoClassMember('profile-name-xr', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                The name of the operation profile.
                ''',
                'profile_name_xr',
                'Cisco-IOS-XR-ethernet-cfm-oper', False, is_config=False),
            _MetaInfoClassMember('display-short', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                Short display name used by the operation
                ''',
                'display_short',
                'Cisco-IOS-XR-ethernet-cfm-oper', False, is_config=False),
            _MetaInfoClassMember('rt-delay-inconsistent', ATTRIBUTE, 'bool', 'boolean',
                None, None,
                [], [],
                '''                Is the profile configured to collect RT Delay
                but the packet type doesn't support it?
                ''',
                'rt_delay_inconsistent',
                'Cisco-IOS-XR-ethernet-cfm-oper', False, is_config=False),
            _MetaInfoClassMember('ow-delay-sd-inconsistent', ATTRIBUTE, 'bool', 'boolean',
                None, None,
                [], [],
                '''                Is the profile configured to collect OW Delay
                (SD) but the packet type doesn't support it?
                ''',
                'ow_delay_sd_inconsistent',
                'Cisco-IOS-XR-ethernet-cfm-oper', False, is_config=False),
            _MetaInfoClassMember('ow-delay-ds-inconsistent', ATTRIBUTE, 'bool', 'boolean',
                None, None,
                [], [],
                '''                Is the profile configured to collect OW Delay
                (DS) but the packet type doesn't support it?
                ''',
                'ow_delay_ds_inconsistent',
                'Cisco-IOS-XR-ethernet-cfm-oper', False, is_config=False),
            _MetaInfoClassMember('rt-jitter-inconsistent', ATTRIBUTE, 'bool', 'boolean',
                None, None,
                [], [],
                '''                Is the profile configured to collect RT Jitter
                but the packet type doesn't support it?
                ''',
                'rt_jitter_inconsistent',
                'Cisco-IOS-XR-ethernet-cfm-oper', False, is_config=False),
            _MetaInfoClassMember('ow-jitter-sd-inconsistent', ATTRIBUTE, 'bool', 'boolean',
                None, None,
                [], [],
                '''                Is the profile configured to collect OW Jitter
                (SD) but the packet type doesn't support it?
                ''',
                'ow_jitter_sd_inconsistent',
                'Cisco-IOS-XR-ethernet-cfm-oper', False, is_config=False),
            _MetaInfoClassMember('ow-jitter-ds-inconsistent', ATTRIBUTE, 'bool', 'boolean',
                None, None,
                [], [],
                '''                Is the profile configured to collect OW Delay
                (DS) but the packet type doesn't support it?
                ''',
                'ow_jitter_ds_inconsistent',
                'Cisco-IOS-XR-ethernet-cfm-oper', False, is_config=False),
            _MetaInfoClassMember('ow-loss-sd-inconsistent', ATTRIBUTE, 'bool', 'boolean',
                None, None,
                [], [],
                '''                Is the profile configured to collect OW Frame
                Loss (SD) but the packet type doesn't support it
                ?
                ''',
                'ow_loss_sd_inconsistent',
                'Cisco-IOS-XR-ethernet-cfm-oper', False, is_config=False),
            _MetaInfoClassMember('ow-loss-ds-inconsistent', ATTRIBUTE, 'bool', 'boolean',
                None, None,
                [], [],
                '''                Is the profile configured to collect OW Frame
                Loss (DS) but the packet type doesn't support it
                ?
                ''',
                'ow_loss_ds_inconsistent',
                'Cisco-IOS-XR-ethernet-cfm-oper', False, is_config=False),
            _MetaInfoClassMember('packet-pad-inconsistent', ATTRIBUTE, 'bool', 'boolean',
                None, None,
                [], [],
                '''                Is the profile configured to pad packets but the
                packet type doesn't support it?
                ''',
                'packet_pad_inconsistent',
                'Cisco-IOS-XR-ethernet-cfm-oper', False, is_config=False),
            _MetaInfoClassMember('packet-rand-pad-inconsistent', ATTRIBUTE, 'bool', 'boolean',
                None, None,
                [], [],
                '''                Is the profile configured to pad packets with a
                pseudo-random string but the packet type doesn't
                support it?
                ''',
                'packet_rand_pad_inconsistent',
                'Cisco-IOS-XR-ethernet-cfm-oper', False, is_config=False),
            _MetaInfoClassMember('min-packet-interval-inconsistent', ATTRIBUTE, 'bool', 'boolean',
                None, None,
                [], [],
                '''                Is the profile configured to send packets more
                frequently than the protocol allows?
                ''',
                'min_packet_interval_inconsistent',
                'Cisco-IOS-XR-ethernet-cfm-oper', False, is_config=False),
            _MetaInfoClassMember('priority-inconsistent', ATTRIBUTE, 'bool', 'boolean',
                None, None,
                [], [],
                '''                Is the profile configured to use a packet
                priority scheme that the protocol does not
                support?
                ''',
                'priority_inconsistent',
                'Cisco-IOS-XR-ethernet-cfm-oper', False, is_config=False),
            _MetaInfoClassMember('packet-type-inconsistent', ATTRIBUTE, 'bool', 'boolean',
                None, None,
                [], [],
                '''                Is the profile configured to use a packet type
                that isn't supported by any protocols?
                ''',
                'packet_type_inconsistent',
                'Cisco-IOS-XR-ethernet-cfm-oper', False, is_config=False),
            _MetaInfoClassMember('profile-doesnt-exist', ATTRIBUTE, 'bool', 'boolean',
                None, None,
                [], [],
                '''                Is the operation configured to use a profile
                that is not currently defined for the protocol?
                ''',
                'profile_doesnt_exist',
                'Cisco-IOS-XR-ethernet-cfm-oper', False, is_config=False),
            _MetaInfoClassMember('synthetic-loss-not-supported', ATTRIBUTE, 'bool', 'boolean',
                None, None,
                [], [],
                '''                The profile is configured to use a packet type
                which doesn't support synthetic loss measurement
                and the number of packets per FLR calculation
                has been configured
                ''',
                'synthetic_loss_not_supported',
                'Cisco-IOS-XR-ethernet-cfm-oper', False, is_config=False),
            _MetaInfoClassMember('probe-too-big', ATTRIBUTE, 'bool', 'boolean',
                None, None,
                [], [],
                '''                The profile is configured to use a packet type
                which does not allow more than 72000 packets per
                probe and greater than 72000 packets per probe
                have been configured
                ''',
                'probe_too_big',
                'Cisco-IOS-XR-ethernet-cfm-oper', False, is_config=False),
            _MetaInfoClassMember('error-string', REFERENCE_LEAFLIST, 'str', 'Sla-error-string',
                None, None,
                [], [],
                '''                Displays other issues not indicated from the
                flags above, for example MIB incompatibility
                issues.
                ''',
                'error_string',
                'Cisco-IOS-XR-ethernet-cfm-oper', False, is_config=False),
            ],
            'Cisco-IOS-XR-ethernet-cfm-oper',
            'config-error',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-ethernet-cfm-oper'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_sla_oper',
            is_config=False,
        ),
    },
    'Sla.Protocols.Ethernet.ConfigErrors' : {
        'meta_info' : _MetaInfoClass('Sla.Protocols.Ethernet.ConfigErrors', REFERENCE_CLASS,
            '''Table of SLA configuration errors on configured
operations''',
            False, 
            [
            _MetaInfoClassMember('config-error', REFERENCE_LIST, 'ConfigError', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_sla_oper', 'Sla.Protocols.Ethernet.ConfigErrors.ConfigError',
                [], [],
                '''                SLA operation to get configuration errors data
                for
                ''',
                'config_error',
                'Cisco-IOS-XR-ethernet-cfm-oper', False, is_config=False),
            ],
            'Cisco-IOS-XR-ethernet-cfm-oper',
            'config-errors',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-ethernet-cfm-oper'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_sla_oper',
            is_config=False,
        ),
    },
    'Sla.Protocols.Ethernet.OnDemandOperations.OnDemandOperation.ProfileOptions.PacketPadding' : {
        'meta_info' : _MetaInfoClass('Sla.Protocols.Ethernet.OnDemandOperations.OnDemandOperation.ProfileOptions.PacketPadding', REFERENCE_CLASS,
            '''Configuration of the packet padding''',
            False, 
            [
            _MetaInfoClassMember('packet-pad-size', ATTRIBUTE, 'int', 'uint16',
                None, None,
                [('0', '65535')], [],
                '''                Size that packets are being padded to
                ''',
                'packet_pad_size',
                'Cisco-IOS-XR-ethernet-cfm-oper', False, is_config=False),
            _MetaInfoClassMember('test-pattern-pad-scheme', REFERENCE_ENUM_CLASS, 'SlaOperTestPatternScheme', 'Sla-oper-test-pattern-scheme',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper', 'SlaOperTestPatternScheme',
                [], [],
                '''                Test pattern scheme that is used in the packet
                padding
                ''',
                'test_pattern_pad_scheme',
                'Cisco-IOS-XR-ethernet-cfm-oper', False, is_config=False),
            _MetaInfoClassMember('test-pattern-pad-hex-string', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('0', '4294967295')], [],
                '''                Hex string that is used in the packet padding
                ''',
                'test_pattern_pad_hex_string',
                'Cisco-IOS-XR-ethernet-cfm-oper', False, is_config=False),
            ],
            'Cisco-IOS-XR-ethernet-cfm-oper',
            'packet-padding',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-ethernet-cfm-oper'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_sla_oper',
            is_config=False,
        ),
    },
    'Sla.Protocols.Ethernet.OnDemandOperations.OnDemandOperation.ProfileOptions.Priority' : {
        'meta_info' : _MetaInfoClass('Sla.Protocols.Ethernet.OnDemandOperations.OnDemandOperation.ProfileOptions.Priority', REFERENCE_CLASS,
            '''Priority at which to send the packet, if
configured''',
            False, 
            [
            _MetaInfoClassMember('priority-type', REFERENCE_ENUM_CLASS, 'SlaOperPacketPriority', 'Sla-oper-packet-priority',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper', 'SlaOperPacketPriority',
                [], [],
                '''                PriorityType
                ''',
                'priority_type',
                'Cisco-IOS-XR-ethernet-cfm-oper', False, is_config=False),
            _MetaInfoClassMember('cos', ATTRIBUTE, 'int', 'uint8',
                None, None,
                [('0', '255')], [],
                '''                3-bit COS priority value applied to packets
                ''',
                'cos',
                'Cisco-IOS-XR-ethernet-cfm-oper', False, is_config=False, has_when=True),
            ],
            'Cisco-IOS-XR-ethernet-cfm-oper',
            'priority',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-ethernet-cfm-oper'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_sla_oper',
            is_config=False,
        ),
    },
    'Sla.Protocols.Ethernet.OnDemandOperations.OnDemandOperation.ProfileOptions.OperationSchedule' : {
        'meta_info' : _MetaInfoClass('Sla.Protocols.Ethernet.OnDemandOperations.OnDemandOperation.ProfileOptions.OperationSchedule', REFERENCE_CLASS,
            '''Operation schedule''',
            False, 
            [
            _MetaInfoClassMember('start-time', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('0', '4294967295')], [],
                '''                Start time of the first probe, in seconds since
                the Unix Epoch
                ''',
                'start_time',
                'Cisco-IOS-XR-ethernet-cfm-oper', False, is_config=False),
            _MetaInfoClassMember('start-time-configured', ATTRIBUTE, 'bool', 'boolean',
                None, None,
                [], [],
                '''                Whether or not the operation start time was
                explicitly configured
                ''',
                'start_time_configured',
                'Cisco-IOS-XR-ethernet-cfm-oper', False, is_config=False),
            _MetaInfoClassMember('schedule-duration', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('0', '4294967295')], [],
                '''                Duration of a probe for the operation in seconds
                ''',
                'schedule_duration',
                'Cisco-IOS-XR-ethernet-cfm-oper', False, is_config=False),
            _MetaInfoClassMember('schedule-interval', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('0', '4294967295')], [],
                '''                Interval between the start times of consecutive
                probes,  in seconds.
                ''',
                'schedule_interval',
                'Cisco-IOS-XR-ethernet-cfm-oper', False, is_config=False),
            ],
            'Cisco-IOS-XR-ethernet-cfm-oper',
            'operation-schedule',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-ethernet-cfm-oper'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_sla_oper',
            is_config=False,
        ),
    },
    'Sla.Protocols.Ethernet.OnDemandOperations.OnDemandOperation.ProfileOptions.OperationMetric.MetricConfig' : {
        'meta_info' : _MetaInfoClass('Sla.Protocols.Ethernet.OnDemandOperations.OnDemandOperation.ProfileOptions.OperationMetric.MetricConfig', REFERENCE_CLASS,
            '''Configuration of the metric''',
            False, 
            [
            _MetaInfoClassMember('metric-type', REFERENCE_ENUM_CLASS, 'SlaRecordableMetric', 'Sla-recordable-metric',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper', 'SlaRecordableMetric',
                [], [],
                '''                Type of metric to which this configuration
                applies
                ''',
                'metric_type',
                'Cisco-IOS-XR-ethernet-cfm-oper', False, is_config=False),
            _MetaInfoClassMember('bins-count', ATTRIBUTE, 'int', 'uint16',
                None, None,
                [('0', '65535')], [],
                '''                Total number of bins into which to aggregate. 0
                if no aggregation.
                ''',
                'bins_count',
                'Cisco-IOS-XR-ethernet-cfm-oper', False, is_config=False),
            _MetaInfoClassMember('bins-width', ATTRIBUTE, 'int', 'uint16',
                None, None,
                [('0', '65535')], [],
                '''                Width of each bin into which to aggregate. 0 if
                no aggregation. For SLM, the units of this value
                are in single units of percent; for LMM they are
                in tenths of percent; for other measurements
                they are in milliseconds.
                ''',
                'bins_width',
                'Cisco-IOS-XR-ethernet-cfm-oper', False, is_config=False),
            _MetaInfoClassMember('bucket-size', ATTRIBUTE, 'int', 'uint8',
                None, None,
                [('0', '255')], [],
                '''                Size of buckets into which measurements are
                collected
                ''',
                'bucket_size',
                'Cisco-IOS-XR-ethernet-cfm-oper', False, is_config=False),
            _MetaInfoClassMember('bucket-size-unit', REFERENCE_ENUM_CLASS, 'SlaBucketSize', 'Sla-bucket-size',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper', 'SlaBucketSize',
                [], [],
                '''                Whether bucket size is 'per-probe' or 'probes'
                ''',
                'bucket_size_unit',
                'Cisco-IOS-XR-ethernet-cfm-oper', False, is_config=False),
            _MetaInfoClassMember('buckets-archive', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('0', '4294967295')], [],
                '''                Maximum number of buckets to store in memory
                ''',
                'buckets_archive',
                'Cisco-IOS-XR-ethernet-cfm-oper', False, is_config=False),
            ],
            'Cisco-IOS-XR-ethernet-cfm-oper',
            'metric-config',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-ethernet-cfm-oper'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_sla_oper',
            is_config=False,
        ),
    },
    'Sla.Protocols.Ethernet.OnDemandOperations.OnDemandOperation.ProfileOptions.OperationMetric' : {
        'meta_info' : _MetaInfoClass('Sla.Protocols.Ethernet.OnDemandOperations.OnDemandOperation.ProfileOptions.OperationMetric', REFERENCE_LIST,
            '''Array of the metrics that are measured by the
operation''',
            False, 
            [
            _MetaInfoClassMember('metric-config', REFERENCE_CLASS, 'MetricConfig', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_sla_oper', 'Sla.Protocols.Ethernet.OnDemandOperations.OnDemandOperation.ProfileOptions.OperationMetric.MetricConfig',
                [], [],
                '''                Configuration of the metric
                ''',
                'metric_config',
                'Cisco-IOS-XR-ethernet-cfm-oper', False, is_config=False),
            _MetaInfoClassMember('current-buckets-archive', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('0', '4294967295')], [],
                '''                Number of valid buckets currently in the buckets
                archive
                ''',
                'current_buckets_archive',
                'Cisco-IOS-XR-ethernet-cfm-oper', False, is_config=False),
            ],
            'Cisco-IOS-XR-ethernet-cfm-oper',
            'operation-metric',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-ethernet-cfm-oper'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_sla_oper',
            is_config=False,
        ),
    },
    'Sla.Protocols.Ethernet.OnDemandOperations.OnDemandOperation.ProfileOptions' : {
        'meta_info' : _MetaInfoClass('Sla.Protocols.Ethernet.OnDemandOperations.OnDemandOperation.ProfileOptions', REFERENCE_CLASS,
            '''Options that are only valid if the operation has
a profile''',
            False, 
            [
            _MetaInfoClassMember('packet-padding', REFERENCE_CLASS, 'PacketPadding', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_sla_oper', 'Sla.Protocols.Ethernet.OnDemandOperations.OnDemandOperation.ProfileOptions.PacketPadding',
                [], [],
                '''                Configuration of the packet padding
                ''',
                'packet_padding',
                'Cisco-IOS-XR-ethernet-cfm-oper', False, is_config=False),
            _MetaInfoClassMember('priority', REFERENCE_CLASS, 'Priority', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_sla_oper', 'Sla.Protocols.Ethernet.OnDemandOperations.OnDemandOperation.ProfileOptions.Priority',
                [], [],
                '''                Priority at which to send the packet, if
                configured
                ''',
                'priority',
                'Cisco-IOS-XR-ethernet-cfm-oper', False, is_config=False),
            _MetaInfoClassMember('operation-schedule', REFERENCE_CLASS, 'OperationSchedule', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_sla_oper', 'Sla.Protocols.Ethernet.OnDemandOperations.OnDemandOperation.ProfileOptions.OperationSchedule',
                [], [],
                '''                Operation schedule
                ''',
                'operation_schedule',
                'Cisco-IOS-XR-ethernet-cfm-oper', False, is_config=False),
            _MetaInfoClassMember('probe-type', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                Type of probe used by the operation
                ''',
                'probe_type',
                'Cisco-IOS-XR-ethernet-cfm-oper', False, is_config=False),
            _MetaInfoClassMember('packets-per-burst', ATTRIBUTE, 'int', 'uint16',
                None, None,
                [('0', '65535')], [],
                '''                Number of packets sent per burst
                ''',
                'packets_per_burst',
                'Cisco-IOS-XR-ethernet-cfm-oper', False, is_config=False),
            _MetaInfoClassMember('inter-packet-interval', ATTRIBUTE, 'int', 'uint16',
                None, None,
                [('0', '65535')], [],
                '''                Interval between packets within a burst in
                milliseconds
                ''',
                'inter_packet_interval',
                'Cisco-IOS-XR-ethernet-cfm-oper', False, is_config=False),
            _MetaInfoClassMember('bursts-per-probe', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('0', '4294967295')], [],
                '''                Number of bursts sent per probe
                ''',
                'bursts_per_probe',
                'Cisco-IOS-XR-ethernet-cfm-oper', False, is_config=False),
            _MetaInfoClassMember('inter-burst-interval', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('0', '4294967295')], [],
                '''                Interval between bursts within a probe in
                milliseconds
                ''',
                'inter_burst_interval',
                'Cisco-IOS-XR-ethernet-cfm-oper', False, is_config=False),
            _MetaInfoClassMember('flr-calculation-interval', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('0', '4294967295')], [],
                '''                Interval between FLR calculations for SLM, in
                milliseconds
                ''',
                'flr_calculation_interval',
                'Cisco-IOS-XR-ethernet-cfm-oper', False, is_config=False),
            _MetaInfoClassMember('operation-metric', REFERENCE_LIST, 'OperationMetric', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_sla_oper', 'Sla.Protocols.Ethernet.OnDemandOperations.OnDemandOperation.ProfileOptions.OperationMetric',
                [], [],
                '''                Array of the metrics that are measured by the
                operation
                ''',
                'operation_metric',
                'Cisco-IOS-XR-ethernet-cfm-oper', False, is_config=False),
            ],
            'Cisco-IOS-XR-ethernet-cfm-oper',
            'profile-options',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-ethernet-cfm-oper'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_sla_oper',
            is_config=False,
        ),
    },
    'Sla.Protocols.Ethernet.OnDemandOperations.OnDemandOperation.SpecificOptions.ConfiguredOperationOptions' : {
        'meta_info' : _MetaInfoClass('Sla.Protocols.Ethernet.OnDemandOperations.OnDemandOperation.SpecificOptions.ConfiguredOperationOptions', REFERENCE_CLASS,
            '''Parameters for a configured operation''',
            False, 
            [
            _MetaInfoClassMember('profile-name', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                Name of the profile used by the operation
                ''',
                'profile_name',
                'Cisco-IOS-XR-ethernet-cfm-oper', False, is_config=False),
            ],
            'Cisco-IOS-XR-ethernet-cfm-oper',
            'configured-operation-options',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-ethernet-cfm-oper'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_sla_oper',
            is_config=False,
            has_when=True,
        ),
    },
    'Sla.Protocols.Ethernet.OnDemandOperations.OnDemandOperation.SpecificOptions.OndemandOperationOptions' : {
        'meta_info' : _MetaInfoClass('Sla.Protocols.Ethernet.OnDemandOperations.OnDemandOperation.SpecificOptions.OndemandOperationOptions', REFERENCE_CLASS,
            '''Parameters for an ondemand operation''',
            False, 
            [
            _MetaInfoClassMember('ondemand-operation-id', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('0', '4294967295')], [],
                '''                ID of the ondemand operation
                ''',
                'ondemand_operation_id',
                'Cisco-IOS-XR-ethernet-cfm-oper', False, is_config=False),
            _MetaInfoClassMember('probe-count', ATTRIBUTE, 'int', 'uint8',
                None, None,
                [('0', '255')], [],
                '''                Total number of probes sent during the operation
                ''',
                'probe_count',
                'Cisco-IOS-XR-ethernet-cfm-oper', False, is_config=False),
            ],
            'Cisco-IOS-XR-ethernet-cfm-oper',
            'ondemand-operation-options',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-ethernet-cfm-oper'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_sla_oper',
            is_config=False,
            has_when=True,
        ),
    },
    'Sla.Protocols.Ethernet.OnDemandOperations.OnDemandOperation.SpecificOptions' : {
        'meta_info' : _MetaInfoClass('Sla.Protocols.Ethernet.OnDemandOperations.OnDemandOperation.SpecificOptions', REFERENCE_CLASS,
            '''Options specific to the type of operation''',
            False, 
            [
            _MetaInfoClassMember('configured-operation-options', REFERENCE_CLASS, 'ConfiguredOperationOptions', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_sla_oper', 'Sla.Protocols.Ethernet.OnDemandOperations.OnDemandOperation.SpecificOptions.ConfiguredOperationOptions',
                [], [],
                '''                Parameters for a configured operation
                ''',
                'configured_operation_options',
                'Cisco-IOS-XR-ethernet-cfm-oper', False, is_config=False, has_when=True),
            _MetaInfoClassMember('ondemand-operation-options', REFERENCE_CLASS, 'OndemandOperationOptions', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_sla_oper', 'Sla.Protocols.Ethernet.OnDemandOperations.OnDemandOperation.SpecificOptions.OndemandOperationOptions',
                [], [],
                '''                Parameters for an ondemand operation
                ''',
                'ondemand_operation_options',
                'Cisco-IOS-XR-ethernet-cfm-oper', False, is_config=False, has_when=True),
            _MetaInfoClassMember('oper-type', REFERENCE_ENUM_CLASS, 'SlaOperOperation', 'Sla-oper-operation',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper', 'SlaOperOperation',
                [], [],
                '''                OperType
                ''',
                'oper_type',
                'Cisco-IOS-XR-ethernet-cfm-oper', False, is_config=False),
            ],
            'Cisco-IOS-XR-ethernet-cfm-oper',
            'specific-options',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-ethernet-cfm-oper'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_sla_oper',
            is_config=False,
        ),
    },
    'Sla.Protocols.Ethernet.OnDemandOperations.OnDemandOperation' : {
        'meta_info' : _MetaInfoClass('Sla.Protocols.Ethernet.OnDemandOperations.OnDemandOperation', REFERENCE_LIST,
            '''SLA on-demand operation to get operation data
for''',
            False, 
            [
            _MetaInfoClassMember('operation-id', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('1', '4294967295')], [],
                '''                Operation ID
                ''',
                'operation_id',
                'Cisco-IOS-XR-ethernet-cfm-oper', False, is_config=False),
            _MetaInfoClassMember('domain-name', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                Domain name
                ''',
                'domain_name',
                'Cisco-IOS-XR-ethernet-cfm-oper', False, is_config=False),
            _MetaInfoClassMember('interface-name', ATTRIBUTE, 'str', 'xr:Interface-name',
                None, None,
                [], [b'[a-zA-Z0-9._/-]+'],
                '''                Interface name
                ''',
                'interface_name',
                'Cisco-IOS-XR-ethernet-cfm-oper', False, is_config=False),
            _MetaInfoClassMember('mep-id', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('1', '8191')], [],
                '''                MEP ID in the range 1 to 8191. Either MEP ID
                or MAC address must be specified.
                ''',
                'mep_id',
                'Cisco-IOS-XR-ethernet-cfm-oper', False, is_config=False),
            _MetaInfoClassMember('mac-address', ATTRIBUTE, 'str', 'yang:mac-address',
                None, None,
                [], [b'[0-9a-fA-F]{2}(:[0-9a-fA-F]{2}){5}'],
                '''                Unicast MAC Address in xxxx.xxxx.xxxx format.
                Either MEP ID or MAC address must be
                specified.
                ''',
                'mac_address',
                'Cisco-IOS-XR-ethernet-cfm-oper', False, is_config=False),
            _MetaInfoClassMember('profile-options', REFERENCE_CLASS, 'ProfileOptions', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_sla_oper', 'Sla.Protocols.Ethernet.OnDemandOperations.OnDemandOperation.ProfileOptions',
                [], [],
                '''                Options that are only valid if the operation has
                a profile
                ''',
                'profile_options',
                'Cisco-IOS-XR-ethernet-cfm-oper', False, is_config=False),
            _MetaInfoClassMember('specific-options', REFERENCE_CLASS, 'SpecificOptions', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_sla_oper', 'Sla.Protocols.Ethernet.OnDemandOperations.OnDemandOperation.SpecificOptions',
                [], [],
                '''                Options specific to the type of operation
                ''',
                'specific_options',
                'Cisco-IOS-XR-ethernet-cfm-oper', False, is_config=False),
            _MetaInfoClassMember('display-short', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                Short display name used by the operation
                ''',
                'display_short',
                'Cisco-IOS-XR-ethernet-cfm-oper', False, is_config=False),
            _MetaInfoClassMember('display-long', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                Long display name used by the operation
                ''',
                'display_long',
                'Cisco-IOS-XR-ethernet-cfm-oper', False, is_config=False),
            _MetaInfoClassMember('last-run', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('0', '4294967295')], [],
                '''                Time that the last probe for the operation was
                run, NULL if never run.
                ''',
                'last_run',
                'Cisco-IOS-XR-ethernet-cfm-oper', False, is_config=False),
            ],
            'Cisco-IOS-XR-ethernet-cfm-oper',
            'on-demand-operation',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-ethernet-cfm-oper'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_sla_oper',
            is_config=False,
        ),
    },
    'Sla.Protocols.Ethernet.OnDemandOperations' : {
        'meta_info' : _MetaInfoClass('Sla.Protocols.Ethernet.OnDemandOperations', REFERENCE_CLASS,
            '''Table of SLA on-demand operations''',
            False, 
            [
            _MetaInfoClassMember('on-demand-operation', REFERENCE_LIST, 'OnDemandOperation', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_sla_oper', 'Sla.Protocols.Ethernet.OnDemandOperations.OnDemandOperation',
                [], [],
                '''                SLA on-demand operation to get operation data
                for
                ''',
                'on_demand_operation',
                'Cisco-IOS-XR-ethernet-cfm-oper', False, is_config=False),
            ],
            'Cisco-IOS-XR-ethernet-cfm-oper',
            'on-demand-operations',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-ethernet-cfm-oper'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_sla_oper',
            is_config=False,
        ),
    },
    'Sla.Protocols.Ethernet.StatisticsCurrents.StatisticsCurrent.SpecificOptions.ConfiguredOperationOptions' : {
        'meta_info' : _MetaInfoClass('Sla.Protocols.Ethernet.StatisticsCurrents.StatisticsCurrent.SpecificOptions.ConfiguredOperationOptions', REFERENCE_CLASS,
            '''Parameters for a configured operation''',
            False, 
            [
            _MetaInfoClassMember('profile-name', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                Name of the profile used by the operation
                ''',
                'profile_name',
                'Cisco-IOS-XR-ethernet-cfm-oper', False, is_config=False),
            ],
            'Cisco-IOS-XR-ethernet-cfm-oper',
            'configured-operation-options',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-ethernet-cfm-oper'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_sla_oper',
            is_config=False,
            has_when=True,
        ),
    },
    'Sla.Protocols.Ethernet.StatisticsCurrents.StatisticsCurrent.SpecificOptions.OndemandOperationOptions' : {
        'meta_info' : _MetaInfoClass('Sla.Protocols.Ethernet.StatisticsCurrents.StatisticsCurrent.SpecificOptions.OndemandOperationOptions', REFERENCE_CLASS,
            '''Parameters for an ondemand operation''',
            False, 
            [
            _MetaInfoClassMember('ondemand-operation-id', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('0', '4294967295')], [],
                '''                ID of the ondemand operation
                ''',
                'ondemand_operation_id',
                'Cisco-IOS-XR-ethernet-cfm-oper', False, is_config=False),
            _MetaInfoClassMember('probe-count', ATTRIBUTE, 'int', 'uint8',
                None, None,
                [('0', '255')], [],
                '''                Total number of probes sent during the operation
                ''',
                'probe_count',
                'Cisco-IOS-XR-ethernet-cfm-oper', False, is_config=False),
            ],
            'Cisco-IOS-XR-ethernet-cfm-oper',
            'ondemand-operation-options',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-ethernet-cfm-oper'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_sla_oper',
            is_config=False,
            has_when=True,
        ),
    },
    'Sla.Protocols.Ethernet.StatisticsCurrents.StatisticsCurrent.SpecificOptions' : {
        'meta_info' : _MetaInfoClass('Sla.Protocols.Ethernet.StatisticsCurrents.StatisticsCurrent.SpecificOptions', REFERENCE_CLASS,
            '''Options specific to the type of operation''',
            False, 
            [
            _MetaInfoClassMember('configured-operation-options', REFERENCE_CLASS, 'ConfiguredOperationOptions', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_sla_oper', 'Sla.Protocols.Ethernet.StatisticsCurrents.StatisticsCurrent.SpecificOptions.ConfiguredOperationOptions',
                [], [],
                '''                Parameters for a configured operation
                ''',
                'configured_operation_options',
                'Cisco-IOS-XR-ethernet-cfm-oper', False, is_config=False, has_when=True),
            _MetaInfoClassMember('ondemand-operation-options', REFERENCE_CLASS, 'OndemandOperationOptions', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_sla_oper', 'Sla.Protocols.Ethernet.StatisticsCurrents.StatisticsCurrent.SpecificOptions.OndemandOperationOptions',
                [], [],
                '''                Parameters for an ondemand operation
                ''',
                'ondemand_operation_options',
                'Cisco-IOS-XR-ethernet-cfm-oper', False, is_config=False, has_when=True),
            _MetaInfoClassMember('oper-type', REFERENCE_ENUM_CLASS, 'SlaOperOperation', 'Sla-oper-operation',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper', 'SlaOperOperation',
                [], [],
                '''                OperType
                ''',
                'oper_type',
                'Cisco-IOS-XR-ethernet-cfm-oper', False, is_config=False),
            ],
            'Cisco-IOS-XR-ethernet-cfm-oper',
            'specific-options',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-ethernet-cfm-oper'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_sla_oper',
            is_config=False,
        ),
    },
    'Sla.Protocols.Ethernet.StatisticsCurrents.StatisticsCurrent.OperationSchedule' : {
        'meta_info' : _MetaInfoClass('Sla.Protocols.Ethernet.StatisticsCurrents.StatisticsCurrent.OperationSchedule', REFERENCE_CLASS,
            '''Operation schedule''',
            False, 
            [
            _MetaInfoClassMember('start-time', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('0', '4294967295')], [],
                '''                Start time of the first probe, in seconds since
                the Unix Epoch
                ''',
                'start_time',
                'Cisco-IOS-XR-ethernet-cfm-oper', False, is_config=False),
            _MetaInfoClassMember('start-time-configured', ATTRIBUTE, 'bool', 'boolean',
                None, None,
                [], [],
                '''                Whether or not the operation start time was
                explicitly configured
                ''',
                'start_time_configured',
                'Cisco-IOS-XR-ethernet-cfm-oper', False, is_config=False),
            _MetaInfoClassMember('schedule-duration', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('0', '4294967295')], [],
                '''                Duration of a probe for the operation in seconds
                ''',
                'schedule_duration',
                'Cisco-IOS-XR-ethernet-cfm-oper', False, is_config=False),
            _MetaInfoClassMember('schedule-interval', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('0', '4294967295')], [],
                '''                Interval between the start times of consecutive
                probes,  in seconds.
                ''',
                'schedule_interval',
                'Cisco-IOS-XR-ethernet-cfm-oper', False, is_config=False),
            ],
            'Cisco-IOS-XR-ethernet-cfm-oper',
            'operation-schedule',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-ethernet-cfm-oper'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_sla_oper',
            is_config=False,
        ),
    },
    'Sla.Protocols.Ethernet.StatisticsCurrents.StatisticsCurrent.OperationMetric.Config' : {
        'meta_info' : _MetaInfoClass('Sla.Protocols.Ethernet.StatisticsCurrents.StatisticsCurrent.OperationMetric.Config', REFERENCE_CLASS,
            '''Configuration of the metric''',
            False, 
            [
            _MetaInfoClassMember('metric-type', REFERENCE_ENUM_CLASS, 'SlaRecordableMetric', 'Sla-recordable-metric',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper', 'SlaRecordableMetric',
                [], [],
                '''                Type of metric to which this configuration
                applies
                ''',
                'metric_type',
                'Cisco-IOS-XR-ethernet-cfm-oper', False, is_config=False),
            _MetaInfoClassMember('bins-count', ATTRIBUTE, 'int', 'uint16',
                None, None,
                [('0', '65535')], [],
                '''                Total number of bins into which to aggregate. 0
                if no aggregation.
                ''',
                'bins_count',
                'Cisco-IOS-XR-ethernet-cfm-oper', False, is_config=False),
            _MetaInfoClassMember('bins-width', ATTRIBUTE, 'int', 'uint16',
                None, None,
                [('0', '65535')], [],
                '''                Width of each bin into which to aggregate. 0 if
                no aggregation. For SLM, the units of this value
                are in single units of percent; for LMM they are
                in tenths of percent; for other measurements
                they are in milliseconds.
                ''',
                'bins_width',
                'Cisco-IOS-XR-ethernet-cfm-oper', False, is_config=False),
            _MetaInfoClassMember('bucket-size', ATTRIBUTE, 'int', 'uint8',
                None, None,
                [('0', '255')], [],
                '''                Size of buckets into which measurements are
                collected
                ''',
                'bucket_size',
                'Cisco-IOS-XR-ethernet-cfm-oper', False, is_config=False),
            _MetaInfoClassMember('bucket-size-unit', REFERENCE_ENUM_CLASS, 'SlaBucketSize', 'Sla-bucket-size',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper', 'SlaBucketSize',
                [], [],
                '''                Whether bucket size is 'per-probe' or 'probes'
                ''',
                'bucket_size_unit',
                'Cisco-IOS-XR-ethernet-cfm-oper', False, is_config=False),
            _MetaInfoClassMember('buckets-archive', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('0', '4294967295')], [],
                '''                Maximum number of buckets to store in memory
                ''',
                'buckets_archive',
                'Cisco-IOS-XR-ethernet-cfm-oper', False, is_config=False),
            ],
            'Cisco-IOS-XR-ethernet-cfm-oper',
            'config',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-ethernet-cfm-oper'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_sla_oper',
            is_config=False,
        ),
    },
    'Sla.Protocols.Ethernet.StatisticsCurrents.StatisticsCurrent.OperationMetric.Bucket.Contents.Aggregated.Bins' : {
        'meta_info' : _MetaInfoClass('Sla.Protocols.Ethernet.StatisticsCurrents.StatisticsCurrent.OperationMetric.Bucket.Contents.Aggregated.Bins', REFERENCE_LIST,
            '''The bins of an SLA metric bucket''',
            False, 
            [
            _MetaInfoClassMember('lower-bound', ATTRIBUTE, 'int', 'int32',
                None, None,
                [('-2147483648', '2147483647')], [],
                '''                Lower bound (inclusive) of the bin, in
                milliseconds or single units of percent. This
                field is not used for LMM measurements
                ''',
                'lower_bound',
                'Cisco-IOS-XR-ethernet-cfm-oper', False, is_config=False),
            _MetaInfoClassMember('upper-bound', ATTRIBUTE, 'int', 'int32',
                None, None,
                [('-2147483648', '2147483647')], [],
                '''                Upper bound (exclusive) of the bin, in
                milliseconds or single units of percent. This
                field is not used for LMM measurements
                ''',
                'upper_bound',
                'Cisco-IOS-XR-ethernet-cfm-oper', False, is_config=False),
            _MetaInfoClassMember('lower-bound-tenths', ATTRIBUTE, 'int', 'int32',
                None, None,
                [('-2147483648', '2147483647')], [],
                '''                Lower bound (inclusive) of the bin, in tenths of
                percent. This field is only used for LMM
                measurements
                ''',
                'lower_bound_tenths',
                'Cisco-IOS-XR-ethernet-cfm-oper', False, is_config=False),
            _MetaInfoClassMember('upper-bound-tenths', ATTRIBUTE, 'int', 'int32',
                None, None,
                [('-2147483648', '2147483647')], [],
                '''                Upper bound (exclusive) of the bin, in tenths of
                percent. This field is only used for LMM
                measurements
                ''',
                'upper_bound_tenths',
                'Cisco-IOS-XR-ethernet-cfm-oper', False, is_config=False),
            _MetaInfoClassMember('sum', ATTRIBUTE, 'int', 'int64',
                None, None,
                [('-9223372036854775808', '9223372036854775807')], [],
                '''                The sum of the results in the bin, in
                microseconds or millionths of a percent
                ''',
                'sum',
                'Cisco-IOS-XR-ethernet-cfm-oper', False, is_config=False),
            _MetaInfoClassMember('count', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('0', '4294967295')], [],
                '''                The total number of results in the bin
                ''',
                'count',
                'Cisco-IOS-XR-ethernet-cfm-oper', False, is_config=False),
            ],
            'Cisco-IOS-XR-ethernet-cfm-oper',
            'bins',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-ethernet-cfm-oper'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_sla_oper',
            is_config=False,
        ),
    },
    'Sla.Protocols.Ethernet.StatisticsCurrents.StatisticsCurrent.OperationMetric.Bucket.Contents.Aggregated' : {
        'meta_info' : _MetaInfoClass('Sla.Protocols.Ethernet.StatisticsCurrents.StatisticsCurrent.OperationMetric.Bucket.Contents.Aggregated', REFERENCE_CLASS,
            '''Result bins in an SLA metric bucket''',
            False, 
            [
            _MetaInfoClassMember('bins', REFERENCE_LIST, 'Bins', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_sla_oper', 'Sla.Protocols.Ethernet.StatisticsCurrents.StatisticsCurrent.OperationMetric.Bucket.Contents.Aggregated.Bins',
                [], [],
                '''                The bins of an SLA metric bucket
                ''',
                'bins',
                'Cisco-IOS-XR-ethernet-cfm-oper', False, is_config=False),
            ],
            'Cisco-IOS-XR-ethernet-cfm-oper',
            'aggregated',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-ethernet-cfm-oper'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_sla_oper',
            is_config=False,
            has_when=True,
        ),
    },
    'Sla.Protocols.Ethernet.StatisticsCurrents.StatisticsCurrent.OperationMetric.Bucket.Contents.Unaggregated.Sample' : {
        'meta_info' : _MetaInfoClass('Sla.Protocols.Ethernet.StatisticsCurrents.StatisticsCurrent.OperationMetric.Bucket.Contents.Unaggregated.Sample', REFERENCE_LIST,
            '''The samples of an SLA metric bucket''',
            False, 
            [
            _MetaInfoClassMember('sent-at', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('0', '4294967295')], [],
                '''                The time (in milliseconds relative to the start
                time of the bucket) that the sample was sent at
                ''',
                'sent_at',
                'Cisco-IOS-XR-ethernet-cfm-oper', False, is_config=False),
            _MetaInfoClassMember('sent', ATTRIBUTE, 'bool', 'boolean',
                None, None,
                [], [],
                '''                Whether the sample packet was sucessfully sent
                ''',
                'sent',
                'Cisco-IOS-XR-ethernet-cfm-oper', False, is_config=False),
            _MetaInfoClassMember('timed-out', ATTRIBUTE, 'bool', 'boolean',
                None, None,
                [], [],
                '''                Whether the sample packet timed out
                ''',
                'timed_out',
                'Cisco-IOS-XR-ethernet-cfm-oper', False, is_config=False),
            _MetaInfoClassMember('corrupt', ATTRIBUTE, 'bool', 'boolean',
                None, None,
                [], [],
                '''                Whether the sample packet was corrupt
                ''',
                'corrupt',
                'Cisco-IOS-XR-ethernet-cfm-oper', False, is_config=False),
            _MetaInfoClassMember('out-of-order', ATTRIBUTE, 'bool', 'boolean',
                None, None,
                [], [],
                '''                Whether the sample packet was received
                out-of-order
                ''',
                'out_of_order',
                'Cisco-IOS-XR-ethernet-cfm-oper', False, is_config=False),
            _MetaInfoClassMember('no-data-packets', ATTRIBUTE, 'bool', 'boolean',
                None, None,
                [], [],
                '''                Whether a measurement could not be made because
                no data packets were sent in the sample period.
                Only applicable for LMM measurements
                ''',
                'no_data_packets',
                'Cisco-IOS-XR-ethernet-cfm-oper', False, is_config=False),
            _MetaInfoClassMember('result', ATTRIBUTE, 'int', 'int32',
                None, None,
                [('-2147483648', '2147483647')], [],
                '''                The result (in microseconds or millionths of a
                percent) of the sample, if available
                ''',
                'result',
                'Cisco-IOS-XR-ethernet-cfm-oper', False, is_config=False),
            _MetaInfoClassMember('frames-sent', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('0', '4294967295')], [],
                '''                For FLR measurements, the number of frames sent,
                if available
                ''',
                'frames_sent',
                'Cisco-IOS-XR-ethernet-cfm-oper', False, is_config=False),
            _MetaInfoClassMember('frames-lost', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('0', '4294967295')], [],
                '''                For FLR measurements, the number of frames lost,
                if available
                ''',
                'frames_lost',
                'Cisco-IOS-XR-ethernet-cfm-oper', False, is_config=False),
            ],
            'Cisco-IOS-XR-ethernet-cfm-oper',
            'sample',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-ethernet-cfm-oper'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_sla_oper',
            is_config=False,
        ),
    },
    'Sla.Protocols.Ethernet.StatisticsCurrents.StatisticsCurrent.OperationMetric.Bucket.Contents.Unaggregated' : {
        'meta_info' : _MetaInfoClass('Sla.Protocols.Ethernet.StatisticsCurrents.StatisticsCurrent.OperationMetric.Bucket.Contents.Unaggregated', REFERENCE_CLASS,
            '''Result samples in an SLA metric bucket''',
            False, 
            [
            _MetaInfoClassMember('sample', REFERENCE_LIST, 'Sample', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_sla_oper', 'Sla.Protocols.Ethernet.StatisticsCurrents.StatisticsCurrent.OperationMetric.Bucket.Contents.Unaggregated.Sample',
                [], [],
                '''                The samples of an SLA metric bucket
                ''',
                'sample',
                'Cisco-IOS-XR-ethernet-cfm-oper', False, is_config=False),
            ],
            'Cisco-IOS-XR-ethernet-cfm-oper',
            'unaggregated',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-ethernet-cfm-oper'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_sla_oper',
            is_config=False,
            has_when=True,
        ),
    },
    'Sla.Protocols.Ethernet.StatisticsCurrents.StatisticsCurrent.OperationMetric.Bucket.Contents' : {
        'meta_info' : _MetaInfoClass('Sla.Protocols.Ethernet.StatisticsCurrents.StatisticsCurrent.OperationMetric.Bucket.Contents', REFERENCE_CLASS,
            '''The contents of the bucket; bins or samples''',
            False, 
            [
            _MetaInfoClassMember('aggregated', REFERENCE_CLASS, 'Aggregated', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_sla_oper', 'Sla.Protocols.Ethernet.StatisticsCurrents.StatisticsCurrent.OperationMetric.Bucket.Contents.Aggregated',
                [], [],
                '''                Result bins in an SLA metric bucket
                ''',
                'aggregated',
                'Cisco-IOS-XR-ethernet-cfm-oper', False, is_config=False, has_when=True),
            _MetaInfoClassMember('unaggregated', REFERENCE_CLASS, 'Unaggregated', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_sla_oper', 'Sla.Protocols.Ethernet.StatisticsCurrents.StatisticsCurrent.OperationMetric.Bucket.Contents.Unaggregated',
                [], [],
                '''                Result samples in an SLA metric bucket
                ''',
                'unaggregated',
                'Cisco-IOS-XR-ethernet-cfm-oper', False, is_config=False, has_when=True),
            _MetaInfoClassMember('bucket-type', REFERENCE_ENUM_CLASS, 'SlaOperBucket', 'Sla-oper-bucket',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper', 'SlaOperBucket',
                [], [],
                '''                BucketType
                ''',
                'bucket_type',
                'Cisco-IOS-XR-ethernet-cfm-oper', False, is_config=False),
            ],
            'Cisco-IOS-XR-ethernet-cfm-oper',
            'contents',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-ethernet-cfm-oper'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_sla_oper',
            is_config=False,
        ),
    },
    'Sla.Protocols.Ethernet.StatisticsCurrents.StatisticsCurrent.OperationMetric.Bucket' : {
        'meta_info' : _MetaInfoClass('Sla.Protocols.Ethernet.StatisticsCurrents.StatisticsCurrent.OperationMetric.Bucket', REFERENCE_LIST,
            '''Buckets stored for the metric''',
            False, 
            [
            _MetaInfoClassMember('contents', REFERENCE_CLASS, 'Contents', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_sla_oper', 'Sla.Protocols.Ethernet.StatisticsCurrents.StatisticsCurrent.OperationMetric.Bucket.Contents',
                [], [],
                '''                The contents of the bucket; bins or samples
                ''',
                'contents',
                'Cisco-IOS-XR-ethernet-cfm-oper', False, is_config=False),
            _MetaInfoClassMember('start-at', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('0', '4294967295')], [],
                '''                Absolute time that the bucket started being
                filled at
                ''',
                'start_at',
                'Cisco-IOS-XR-ethernet-cfm-oper', False, is_config=False),
            _MetaInfoClassMember('duration', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('0', '4294967295')], [],
                '''                Length of time for which the bucket is being
                filled in seconds
                ''',
                'duration',
                'Cisco-IOS-XR-ethernet-cfm-oper', False, is_config=False),
            _MetaInfoClassMember('sent', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('0', '4294967295')], [],
                '''                Number of packets sent in the probe
                ''',
                'sent',
                'Cisco-IOS-XR-ethernet-cfm-oper', False, is_config=False),
            _MetaInfoClassMember('lost', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('0', '4294967295')], [],
                '''                Number of lost packets in the probe
                ''',
                'lost',
                'Cisco-IOS-XR-ethernet-cfm-oper', False, is_config=False),
            _MetaInfoClassMember('corrupt', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('0', '4294967295')], [],
                '''                Number of corrupt packets in the probe
                ''',
                'corrupt',
                'Cisco-IOS-XR-ethernet-cfm-oper', False, is_config=False),
            _MetaInfoClassMember('out-of-order', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('0', '4294967295')], [],
                '''                Number of packets recieved out-of-order in the
                probe
                ''',
                'out_of_order',
                'Cisco-IOS-XR-ethernet-cfm-oper', False, is_config=False),
            _MetaInfoClassMember('duplicates', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('0', '4294967295')], [],
                '''                Number of duplicate packets received in the
                probe
                ''',
                'duplicates',
                'Cisco-IOS-XR-ethernet-cfm-oper', False, is_config=False),
            _MetaInfoClassMember('minimum', ATTRIBUTE, 'int', 'int32',
                None, None,
                [('-2147483648', '2147483647')], [],
                '''                Overall minimum result in the probe, in
                microseconds or millionths of a percent
                ''',
                'minimum',
                'Cisco-IOS-XR-ethernet-cfm-oper', False, is_config=False),
            _MetaInfoClassMember('maximum', ATTRIBUTE, 'int', 'int32',
                None, None,
                [('-2147483648', '2147483647')], [],
                '''                Overall minimum result in the probe, in
                microseconds or millionths of a percent
                ''',
                'maximum',
                'Cisco-IOS-XR-ethernet-cfm-oper', False, is_config=False),
            _MetaInfoClassMember('time-of-minimum', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('0', '4294967295')], [],
                '''                Absolute time that the minimum value was
                recorded
                ''',
                'time_of_minimum',
                'Cisco-IOS-XR-ethernet-cfm-oper', False, is_config=False),
            _MetaInfoClassMember('time-of-maximum', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('0', '4294967295')], [],
                '''                Absolute time that the maximum value was
                recorded
                ''',
                'time_of_maximum',
                'Cisco-IOS-XR-ethernet-cfm-oper', False, is_config=False),
            _MetaInfoClassMember('average', ATTRIBUTE, 'int', 'int32',
                None, None,
                [('-2147483648', '2147483647')], [],
                '''                Mean of the results in the probe, in
                microseconds or millionths of a percent
                ''',
                'average',
                'Cisco-IOS-XR-ethernet-cfm-oper', False, is_config=False),
            _MetaInfoClassMember('standard-deviation', ATTRIBUTE, 'int', 'int32',
                None, None,
                [('-2147483648', '2147483647')], [],
                '''                Standard deviation of the results in the probe,
                in microseconds or millionths of a percent
                ''',
                'standard_deviation',
                'Cisco-IOS-XR-ethernet-cfm-oper', False, is_config=False),
            _MetaInfoClassMember('result-count', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('0', '4294967295')], [],
                '''                The count of samples collected in the bucket.
                ''',
                'result_count',
                'Cisco-IOS-XR-ethernet-cfm-oper', False, is_config=False),
            _MetaInfoClassMember('data-sent-count', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('0', '4294967295')], [],
                '''                The number of data packets sent across the
                bucket, used in the calculation of overall FLR.
                ''',
                'data_sent_count',
                'Cisco-IOS-XR-ethernet-cfm-oper', False, is_config=False),
            _MetaInfoClassMember('data-lost-count', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('0', '4294967295')], [],
                '''                The number of data packets lost across the
                bucket, used in the calculation of overall FLR.
                ''',
                'data_lost_count',
                'Cisco-IOS-XR-ethernet-cfm-oper', False, is_config=False),
            _MetaInfoClassMember('overall-flr', ATTRIBUTE, 'int', 'int32',
                None, None,
                [('-2147483648', '2147483647')], [],
                '''                Frame Loss Ratio across the whole bucket, in
                millionths of a percent
                ''',
                'overall_flr',
                'Cisco-IOS-XR-ethernet-cfm-oper', False, is_config=False),
            _MetaInfoClassMember('suspect-start-mid-bucket', ATTRIBUTE, 'bool', 'boolean',
                None, None,
                [], [],
                '''                Results suspect due to a probe starting mid-way
                through a bucket
                ''',
                'suspect_start_mid_bucket',
                'Cisco-IOS-XR-ethernet-cfm-oper', False, is_config=False),
            _MetaInfoClassMember('suspect-schedule-latency', ATTRIBUTE, 'bool', 'boolean',
                None, None,
                [], [],
                '''                Results suspect due to scheduling latency
                causing one or more packets to not be sent
                ''',
                'suspect_schedule_latency',
                'Cisco-IOS-XR-ethernet-cfm-oper', False, is_config=False),
            _MetaInfoClassMember('suspect-send-fail', ATTRIBUTE, 'bool', 'boolean',
                None, None,
                [], [],
                '''                Results suspect due to failure to send one or
                more packets
                ''',
                'suspect_send_fail',
                'Cisco-IOS-XR-ethernet-cfm-oper', False, is_config=False),
            _MetaInfoClassMember('suspect-premature-end', ATTRIBUTE, 'bool', 'boolean',
                None, None,
                [], [],
                '''                Results suspect due to a probe ending
                prematurely
                ''',
                'suspect_premature_end',
                'Cisco-IOS-XR-ethernet-cfm-oper', False, is_config=False),
            _MetaInfoClassMember('suspect-clock-drift', ATTRIBUTE, 'bool', 'boolean',
                None, None,
                [], [],
                '''                Results suspect as more than 10 seconds time
                drift detected
                ''',
                'suspect_clock_drift',
                'Cisco-IOS-XR-ethernet-cfm-oper', False, is_config=False),
            _MetaInfoClassMember('suspect-memory-allocation-failed', ATTRIBUTE, 'bool', 'boolean',
                None, None,
                [], [],
                '''                Results suspect due to a memory allocation
                failure
                ''',
                'suspect_memory_allocation_failed',
                'Cisco-IOS-XR-ethernet-cfm-oper', False, is_config=False),
            _MetaInfoClassMember('suspect-cleared-mid-bucket', ATTRIBUTE, 'bool', 'boolean',
                None, None,
                [], [],
                '''                Results suspect as bucket was cleared mid-way
                through being filled
                ''',
                'suspect_cleared_mid_bucket',
                'Cisco-IOS-XR-ethernet-cfm-oper', False, is_config=False),
            _MetaInfoClassMember('suspect-probe-restarted', ATTRIBUTE, 'bool', 'boolean',
                None, None,
                [], [],
                '''                Results suspect as probe restarted mid-way
                through the bucket
                ''',
                'suspect_probe_restarted',
                'Cisco-IOS-XR-ethernet-cfm-oper', False, is_config=False),
            _MetaInfoClassMember('suspect-management-latency', ATTRIBUTE, 'bool', 'boolean',
                None, None,
                [], [],
                '''                Results suspect as processing of results has
                been delayed
                ''',
                'suspect_management_latency',
                'Cisco-IOS-XR-ethernet-cfm-oper', False, is_config=False),
            _MetaInfoClassMember('suspect-multiple-buckets', ATTRIBUTE, 'bool', 'boolean',
                None, None,
                [], [],
                '''                Results suspect as the probe has been configured
                across multiple buckets
                ''',
                'suspect_multiple_buckets',
                'Cisco-IOS-XR-ethernet-cfm-oper', False, is_config=False),
            _MetaInfoClassMember('suspect-misordering', ATTRIBUTE, 'bool', 'boolean',
                None, None,
                [], [],
                '''                Results suspect as misordering has been detected
                , affecting results
                ''',
                'suspect_misordering',
                'Cisco-IOS-XR-ethernet-cfm-oper', False, is_config=False),
            _MetaInfoClassMember('suspect-flr-low-packet-count', ATTRIBUTE, 'bool', 'boolean',
                None, None,
                [], [],
                '''                Results suspect as FLR calculated based on a low
                packet count
                ''',
                'suspect_flr_low_packet_count',
                'Cisco-IOS-XR-ethernet-cfm-oper', False, is_config=False),
            _MetaInfoClassMember('premature-reason', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('0', '4294967295')], [],
                '''                If the probe ended prematurely, the error that
                caused a probe to end
                ''',
                'premature_reason',
                'Cisco-IOS-XR-ethernet-cfm-oper', False, is_config=False),
            _MetaInfoClassMember('premature-reason-string', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                Description of the error code that caused the
                probe to end prematurely. For informational
                purposes only
                ''',
                'premature_reason_string',
                'Cisco-IOS-XR-ethernet-cfm-oper', False, is_config=False),
            ],
            'Cisco-IOS-XR-ethernet-cfm-oper',
            'bucket',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-ethernet-cfm-oper'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_sla_oper',
            is_config=False,
        ),
    },
    'Sla.Protocols.Ethernet.StatisticsCurrents.StatisticsCurrent.OperationMetric' : {
        'meta_info' : _MetaInfoClass('Sla.Protocols.Ethernet.StatisticsCurrents.StatisticsCurrent.OperationMetric', REFERENCE_LIST,
            '''Metrics gathered for the operation''',
            False, 
            [
            _MetaInfoClassMember('config', REFERENCE_CLASS, 'Config', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_sla_oper', 'Sla.Protocols.Ethernet.StatisticsCurrents.StatisticsCurrent.OperationMetric.Config',
                [], [],
                '''                Configuration of the metric
                ''',
                'config',
                'Cisco-IOS-XR-ethernet-cfm-oper', False, is_config=False),
            _MetaInfoClassMember('bucket', REFERENCE_LIST, 'Bucket', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_sla_oper', 'Sla.Protocols.Ethernet.StatisticsCurrents.StatisticsCurrent.OperationMetric.Bucket',
                [], [],
                '''                Buckets stored for the metric
                ''',
                'bucket',
                'Cisco-IOS-XR-ethernet-cfm-oper', False, is_config=False),
            ],
            'Cisco-IOS-XR-ethernet-cfm-oper',
            'operation-metric',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-ethernet-cfm-oper'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_sla_oper',
            is_config=False,
        ),
    },
    'Sla.Protocols.Ethernet.StatisticsCurrents.StatisticsCurrent' : {
        'meta_info' : _MetaInfoClass('Sla.Protocols.Ethernet.StatisticsCurrents.StatisticsCurrent', REFERENCE_LIST,
            '''Current statistics data for an SLA configured
operation''',
            False, 
            [
            _MetaInfoClassMember('profile-name', ATTRIBUTE, 'str', 'xr:Cisco-ios-xr-string',
                None, None,
                [], [b'[\\w\\-\\.:,_@#%$\\+=\\|;]+'],
                '''                Profile Name
                ''',
                'profile_name',
                'Cisco-IOS-XR-ethernet-cfm-oper', False, is_config=False),
            _MetaInfoClassMember('domain-name', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                Domain name
                ''',
                'domain_name',
                'Cisco-IOS-XR-ethernet-cfm-oper', False, is_config=False),
            _MetaInfoClassMember('interface-name', ATTRIBUTE, 'str', 'xr:Interface-name',
                None, None,
                [], [b'[a-zA-Z0-9._/-]+'],
                '''                Interface name
                ''',
                'interface_name',
                'Cisco-IOS-XR-ethernet-cfm-oper', False, is_config=False),
            _MetaInfoClassMember('mep-id', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('1', '8191')], [],
                '''                MEP ID in the range 1 to 8191. Either MEP ID
                or MAC address must be specified.
                ''',
                'mep_id',
                'Cisco-IOS-XR-ethernet-cfm-oper', False, is_config=False),
            _MetaInfoClassMember('mac-address', ATTRIBUTE, 'str', 'yang:mac-address',
                None, None,
                [], [b'[0-9a-fA-F]{2}(:[0-9a-fA-F]{2}){5}'],
                '''                Unicast MAC Address in xxxx.xxxx.xxxx format.
                Either MEP ID or MAC address must be
                specified.
                ''',
                'mac_address',
                'Cisco-IOS-XR-ethernet-cfm-oper', False, is_config=False),
            _MetaInfoClassMember('specific-options', REFERENCE_CLASS, 'SpecificOptions', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_sla_oper', 'Sla.Protocols.Ethernet.StatisticsCurrents.StatisticsCurrent.SpecificOptions',
                [], [],
                '''                Options specific to the type of operation
                ''',
                'specific_options',
                'Cisco-IOS-XR-ethernet-cfm-oper', False, is_config=False),
            _MetaInfoClassMember('operation-schedule', REFERENCE_CLASS, 'OperationSchedule', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_sla_oper', 'Sla.Protocols.Ethernet.StatisticsCurrents.StatisticsCurrent.OperationSchedule',
                [], [],
                '''                Operation schedule
                ''',
                'operation_schedule',
                'Cisco-IOS-XR-ethernet-cfm-oper', False, is_config=False),
            _MetaInfoClassMember('probe-type', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                Type of probe used by the operation
                ''',
                'probe_type',
                'Cisco-IOS-XR-ethernet-cfm-oper', False, is_config=False),
            _MetaInfoClassMember('display-short', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                Short display name used by the operation
                ''',
                'display_short',
                'Cisco-IOS-XR-ethernet-cfm-oper', False, is_config=False),
            _MetaInfoClassMember('display-long', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                Long display name used by the operation
                ''',
                'display_long',
                'Cisco-IOS-XR-ethernet-cfm-oper', False, is_config=False),
            _MetaInfoClassMember('flr-calculation-interval', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('0', '4294967295')], [],
                '''                Interval between FLR calculations for SLM, in
                milliseconds
                ''',
                'flr_calculation_interval',
                'Cisco-IOS-XR-ethernet-cfm-oper', False, is_config=False),
            _MetaInfoClassMember('operation-metric', REFERENCE_LIST, 'OperationMetric', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_sla_oper', 'Sla.Protocols.Ethernet.StatisticsCurrents.StatisticsCurrent.OperationMetric',
                [], [],
                '''                Metrics gathered for the operation
                ''',
                'operation_metric',
                'Cisco-IOS-XR-ethernet-cfm-oper', False, is_config=False),
            ],
            'Cisco-IOS-XR-ethernet-cfm-oper',
            'statistics-current',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-ethernet-cfm-oper'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_sla_oper',
            is_config=False,
        ),
    },
    'Sla.Protocols.Ethernet.StatisticsCurrents' : {
        'meta_info' : _MetaInfoClass('Sla.Protocols.Ethernet.StatisticsCurrents', REFERENCE_CLASS,
            '''Table of current statistics for SLA operations''',
            False, 
            [
            _MetaInfoClassMember('statistics-current', REFERENCE_LIST, 'StatisticsCurrent', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_sla_oper', 'Sla.Protocols.Ethernet.StatisticsCurrents.StatisticsCurrent',
                [], [],
                '''                Current statistics data for an SLA configured
                operation
                ''',
                'statistics_current',
                'Cisco-IOS-XR-ethernet-cfm-oper', False, is_config=False),
            ],
            'Cisco-IOS-XR-ethernet-cfm-oper',
            'statistics-currents',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-ethernet-cfm-oper'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_sla_oper',
            is_config=False,
        ),
    },
    'Sla.Protocols.Ethernet' : {
        'meta_info' : _MetaInfoClass('Sla.Protocols.Ethernet', REFERENCE_CLASS,
            '''The Ethernet SLA protocol''',
            False, 
            [
            _MetaInfoClassMember('statistics-on-demand-currents', REFERENCE_CLASS, 'StatisticsOnDemandCurrents', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_sla_oper', 'Sla.Protocols.Ethernet.StatisticsOnDemandCurrents',
                [], [],
                '''                Table of current statistics for SLA on-demand
                operations
                ''',
                'statistics_on_demand_currents',
                'Cisco-IOS-XR-ethernet-cfm-oper', False, is_config=False),
            _MetaInfoClassMember('operations', REFERENCE_CLASS, 'Operations', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_sla_oper', 'Sla.Protocols.Ethernet.Operations',
                [], [],
                '''                Table of SLA operations
                ''',
                'operations',
                'Cisco-IOS-XR-ethernet-cfm-oper', False, is_config=False),
            _MetaInfoClassMember('statistics-historicals', REFERENCE_CLASS, 'StatisticsHistoricals', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_sla_oper', 'Sla.Protocols.Ethernet.StatisticsHistoricals',
                [], [],
                '''                Table of historical statistics for SLA
                operations
                ''',
                'statistics_historicals',
                'Cisco-IOS-XR-ethernet-cfm-oper', False, is_config=False),
            _MetaInfoClassMember('statistics-on-demand-historicals', REFERENCE_CLASS, 'StatisticsOnDemandHistoricals', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_sla_oper', 'Sla.Protocols.Ethernet.StatisticsOnDemandHistoricals',
                [], [],
                '''                Table of historical statistics for SLA
                on-demand operations
                ''',
                'statistics_on_demand_historicals',
                'Cisco-IOS-XR-ethernet-cfm-oper', False, is_config=False),
            _MetaInfoClassMember('config-errors', REFERENCE_CLASS, 'ConfigErrors', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_sla_oper', 'Sla.Protocols.Ethernet.ConfigErrors',
                [], [],
                '''                Table of SLA configuration errors on configured
                operations
                ''',
                'config_errors',
                'Cisco-IOS-XR-ethernet-cfm-oper', False, is_config=False),
            _MetaInfoClassMember('on-demand-operations', REFERENCE_CLASS, 'OnDemandOperations', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_sla_oper', 'Sla.Protocols.Ethernet.OnDemandOperations',
                [], [],
                '''                Table of SLA on-demand operations
                ''',
                'on_demand_operations',
                'Cisco-IOS-XR-ethernet-cfm-oper', False, is_config=False),
            _MetaInfoClassMember('statistics-currents', REFERENCE_CLASS, 'StatisticsCurrents', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_sla_oper', 'Sla.Protocols.Ethernet.StatisticsCurrents',
                [], [],
                '''                Table of current statistics for SLA operations
                ''',
                'statistics_currents',
                'Cisco-IOS-XR-ethernet-cfm-oper', False, is_config=False),
            ],
            'Cisco-IOS-XR-ethernet-cfm-oper',
            'ethernet',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-ethernet-cfm-oper'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_sla_oper',
            is_config=False,
        ),
    },
    'Sla.Protocols' : {
        'meta_info' : _MetaInfoClass('Sla.Protocols', REFERENCE_CLASS,
            '''Table of all SLA protocols''',
            False, 
            [
            _MetaInfoClassMember('ethernet', REFERENCE_CLASS, 'Ethernet', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_sla_oper', 'Sla.Protocols.Ethernet',
                [], [],
                '''                The Ethernet SLA protocol
                ''',
                'ethernet',
                'Cisco-IOS-XR-ethernet-cfm-oper', False, is_config=False),
            ],
            'Cisco-IOS-XR-infra-sla-oper',
            'protocols',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-infra-sla-oper'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_sla_oper',
            is_config=False,
        ),
    },
    'Sla' : {
        'meta_info' : _MetaInfoClass('Sla', REFERENCE_CLASS,
            '''SLA oper commands''',
            False, 
            [
            _MetaInfoClassMember('protocols', REFERENCE_CLASS, 'Protocols', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_sla_oper', 'Sla.Protocols',
                [], [],
                '''                Table of all SLA protocols
                ''',
                'protocols',
                'Cisco-IOS-XR-infra-sla-oper', False, is_config=False),
            ],
            'Cisco-IOS-XR-infra-sla-oper',
            'sla',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-infra-sla-oper'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_sla_oper',
            is_config=False,
        ),
    },
    'SlaNodes' : {
        'meta_info' : _MetaInfoClass('SlaNodes', REFERENCE_CLASS,
            '''sla nodes''',
            False, 
            [
            ],
            'Cisco-IOS-XR-infra-sla-oper',
            'sla-nodes',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-infra-sla-oper'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_sla_oper',
            is_config=False,
        ),
    },
}
_meta_table['Sla.Protocols.Ethernet.StatisticsOnDemandCurrents.StatisticsOnDemandCurrent.SpecificOptions.ConfiguredOperationOptions']['meta_info'].parent =_meta_table['Sla.Protocols.Ethernet.StatisticsOnDemandCurrents.StatisticsOnDemandCurrent.SpecificOptions']['meta_info']
_meta_table['Sla.Protocols.Ethernet.StatisticsOnDemandCurrents.StatisticsOnDemandCurrent.SpecificOptions.OndemandOperationOptions']['meta_info'].parent =_meta_table['Sla.Protocols.Ethernet.StatisticsOnDemandCurrents.StatisticsOnDemandCurrent.SpecificOptions']['meta_info']
_meta_table['Sla.Protocols.Ethernet.StatisticsOnDemandCurrents.StatisticsOnDemandCurrent.OperationMetric.Bucket.Contents.Aggregated.Bins']['meta_info'].parent =_meta_table['Sla.Protocols.Ethernet.StatisticsOnDemandCurrents.StatisticsOnDemandCurrent.OperationMetric.Bucket.Contents.Aggregated']['meta_info']
_meta_table['Sla.Protocols.Ethernet.StatisticsOnDemandCurrents.StatisticsOnDemandCurrent.OperationMetric.Bucket.Contents.Unaggregated.Sample']['meta_info'].parent =_meta_table['Sla.Protocols.Ethernet.StatisticsOnDemandCurrents.StatisticsOnDemandCurrent.OperationMetric.Bucket.Contents.Unaggregated']['meta_info']
_meta_table['Sla.Protocols.Ethernet.StatisticsOnDemandCurrents.StatisticsOnDemandCurrent.OperationMetric.Bucket.Contents.Aggregated']['meta_info'].parent =_meta_table['Sla.Protocols.Ethernet.StatisticsOnDemandCurrents.StatisticsOnDemandCurrent.OperationMetric.Bucket.Contents']['meta_info']
_meta_table['Sla.Protocols.Ethernet.StatisticsOnDemandCurrents.StatisticsOnDemandCurrent.OperationMetric.Bucket.Contents.Unaggregated']['meta_info'].parent =_meta_table['Sla.Protocols.Ethernet.StatisticsOnDemandCurrents.StatisticsOnDemandCurrent.OperationMetric.Bucket.Contents']['meta_info']
_meta_table['Sla.Protocols.Ethernet.StatisticsOnDemandCurrents.StatisticsOnDemandCurrent.OperationMetric.Bucket.Contents']['meta_info'].parent =_meta_table['Sla.Protocols.Ethernet.StatisticsOnDemandCurrents.StatisticsOnDemandCurrent.OperationMetric.Bucket']['meta_info']
_meta_table['Sla.Protocols.Ethernet.StatisticsOnDemandCurrents.StatisticsOnDemandCurrent.OperationMetric.Config']['meta_info'].parent =_meta_table['Sla.Protocols.Ethernet.StatisticsOnDemandCurrents.StatisticsOnDemandCurrent.OperationMetric']['meta_info']
_meta_table['Sla.Protocols.Ethernet.StatisticsOnDemandCurrents.StatisticsOnDemandCurrent.OperationMetric.Bucket']['meta_info'].parent =_meta_table['Sla.Protocols.Ethernet.StatisticsOnDemandCurrents.StatisticsOnDemandCurrent.OperationMetric']['meta_info']
_meta_table['Sla.Protocols.Ethernet.StatisticsOnDemandCurrents.StatisticsOnDemandCurrent.SpecificOptions']['meta_info'].parent =_meta_table['Sla.Protocols.Ethernet.StatisticsOnDemandCurrents.StatisticsOnDemandCurrent']['meta_info']
_meta_table['Sla.Protocols.Ethernet.StatisticsOnDemandCurrents.StatisticsOnDemandCurrent.OperationSchedule']['meta_info'].parent =_meta_table['Sla.Protocols.Ethernet.StatisticsOnDemandCurrents.StatisticsOnDemandCurrent']['meta_info']
_meta_table['Sla.Protocols.Ethernet.StatisticsOnDemandCurrents.StatisticsOnDemandCurrent.OperationMetric']['meta_info'].parent =_meta_table['Sla.Protocols.Ethernet.StatisticsOnDemandCurrents.StatisticsOnDemandCurrent']['meta_info']
_meta_table['Sla.Protocols.Ethernet.StatisticsOnDemandCurrents.StatisticsOnDemandCurrent']['meta_info'].parent =_meta_table['Sla.Protocols.Ethernet.StatisticsOnDemandCurrents']['meta_info']
_meta_table['Sla.Protocols.Ethernet.Operations.Operation.ProfileOptions.OperationMetric.MetricConfig']['meta_info'].parent =_meta_table['Sla.Protocols.Ethernet.Operations.Operation.ProfileOptions.OperationMetric']['meta_info']
_meta_table['Sla.Protocols.Ethernet.Operations.Operation.ProfileOptions.PacketPadding']['meta_info'].parent =_meta_table['Sla.Protocols.Ethernet.Operations.Operation.ProfileOptions']['meta_info']
_meta_table['Sla.Protocols.Ethernet.Operations.Operation.ProfileOptions.Priority']['meta_info'].parent =_meta_table['Sla.Protocols.Ethernet.Operations.Operation.ProfileOptions']['meta_info']
_meta_table['Sla.Protocols.Ethernet.Operations.Operation.ProfileOptions.OperationSchedule']['meta_info'].parent =_meta_table['Sla.Protocols.Ethernet.Operations.Operation.ProfileOptions']['meta_info']
_meta_table['Sla.Protocols.Ethernet.Operations.Operation.ProfileOptions.OperationMetric']['meta_info'].parent =_meta_table['Sla.Protocols.Ethernet.Operations.Operation.ProfileOptions']['meta_info']
_meta_table['Sla.Protocols.Ethernet.Operations.Operation.SpecificOptions.ConfiguredOperationOptions']['meta_info'].parent =_meta_table['Sla.Protocols.Ethernet.Operations.Operation.SpecificOptions']['meta_info']
_meta_table['Sla.Protocols.Ethernet.Operations.Operation.SpecificOptions.OndemandOperationOptions']['meta_info'].parent =_meta_table['Sla.Protocols.Ethernet.Operations.Operation.SpecificOptions']['meta_info']
_meta_table['Sla.Protocols.Ethernet.Operations.Operation.ProfileOptions']['meta_info'].parent =_meta_table['Sla.Protocols.Ethernet.Operations.Operation']['meta_info']
_meta_table['Sla.Protocols.Ethernet.Operations.Operation.SpecificOptions']['meta_info'].parent =_meta_table['Sla.Protocols.Ethernet.Operations.Operation']['meta_info']
_meta_table['Sla.Protocols.Ethernet.Operations.Operation']['meta_info'].parent =_meta_table['Sla.Protocols.Ethernet.Operations']['meta_info']
_meta_table['Sla.Protocols.Ethernet.StatisticsHistoricals.StatisticsHistorical.SpecificOptions.ConfiguredOperationOptions']['meta_info'].parent =_meta_table['Sla.Protocols.Ethernet.StatisticsHistoricals.StatisticsHistorical.SpecificOptions']['meta_info']
_meta_table['Sla.Protocols.Ethernet.StatisticsHistoricals.StatisticsHistorical.SpecificOptions.OndemandOperationOptions']['meta_info'].parent =_meta_table['Sla.Protocols.Ethernet.StatisticsHistoricals.StatisticsHistorical.SpecificOptions']['meta_info']
_meta_table['Sla.Protocols.Ethernet.StatisticsHistoricals.StatisticsHistorical.OperationMetric.Bucket.Contents.Aggregated.Bins']['meta_info'].parent =_meta_table['Sla.Protocols.Ethernet.StatisticsHistoricals.StatisticsHistorical.OperationMetric.Bucket.Contents.Aggregated']['meta_info']
_meta_table['Sla.Protocols.Ethernet.StatisticsHistoricals.StatisticsHistorical.OperationMetric.Bucket.Contents.Unaggregated.Sample']['meta_info'].parent =_meta_table['Sla.Protocols.Ethernet.StatisticsHistoricals.StatisticsHistorical.OperationMetric.Bucket.Contents.Unaggregated']['meta_info']
_meta_table['Sla.Protocols.Ethernet.StatisticsHistoricals.StatisticsHistorical.OperationMetric.Bucket.Contents.Aggregated']['meta_info'].parent =_meta_table['Sla.Protocols.Ethernet.StatisticsHistoricals.StatisticsHistorical.OperationMetric.Bucket.Contents']['meta_info']
_meta_table['Sla.Protocols.Ethernet.StatisticsHistoricals.StatisticsHistorical.OperationMetric.Bucket.Contents.Unaggregated']['meta_info'].parent =_meta_table['Sla.Protocols.Ethernet.StatisticsHistoricals.StatisticsHistorical.OperationMetric.Bucket.Contents']['meta_info']
_meta_table['Sla.Protocols.Ethernet.StatisticsHistoricals.StatisticsHistorical.OperationMetric.Bucket.Contents']['meta_info'].parent =_meta_table['Sla.Protocols.Ethernet.StatisticsHistoricals.StatisticsHistorical.OperationMetric.Bucket']['meta_info']
_meta_table['Sla.Protocols.Ethernet.StatisticsHistoricals.StatisticsHistorical.OperationMetric.Config']['meta_info'].parent =_meta_table['Sla.Protocols.Ethernet.StatisticsHistoricals.StatisticsHistorical.OperationMetric']['meta_info']
_meta_table['Sla.Protocols.Ethernet.StatisticsHistoricals.StatisticsHistorical.OperationMetric.Bucket']['meta_info'].parent =_meta_table['Sla.Protocols.Ethernet.StatisticsHistoricals.StatisticsHistorical.OperationMetric']['meta_info']
_meta_table['Sla.Protocols.Ethernet.StatisticsHistoricals.StatisticsHistorical.SpecificOptions']['meta_info'].parent =_meta_table['Sla.Protocols.Ethernet.StatisticsHistoricals.StatisticsHistorical']['meta_info']
_meta_table['Sla.Protocols.Ethernet.StatisticsHistoricals.StatisticsHistorical.OperationSchedule']['meta_info'].parent =_meta_table['Sla.Protocols.Ethernet.StatisticsHistoricals.StatisticsHistorical']['meta_info']
_meta_table['Sla.Protocols.Ethernet.StatisticsHistoricals.StatisticsHistorical.OperationMetric']['meta_info'].parent =_meta_table['Sla.Protocols.Ethernet.StatisticsHistoricals.StatisticsHistorical']['meta_info']
_meta_table['Sla.Protocols.Ethernet.StatisticsHistoricals.StatisticsHistorical']['meta_info'].parent =_meta_table['Sla.Protocols.Ethernet.StatisticsHistoricals']['meta_info']
_meta_table['Sla.Protocols.Ethernet.StatisticsOnDemandHistoricals.StatisticsOnDemandHistorical.SpecificOptions.ConfiguredOperationOptions']['meta_info'].parent =_meta_table['Sla.Protocols.Ethernet.StatisticsOnDemandHistoricals.StatisticsOnDemandHistorical.SpecificOptions']['meta_info']
_meta_table['Sla.Protocols.Ethernet.StatisticsOnDemandHistoricals.StatisticsOnDemandHistorical.SpecificOptions.OndemandOperationOptions']['meta_info'].parent =_meta_table['Sla.Protocols.Ethernet.StatisticsOnDemandHistoricals.StatisticsOnDemandHistorical.SpecificOptions']['meta_info']
_meta_table['Sla.Protocols.Ethernet.StatisticsOnDemandHistoricals.StatisticsOnDemandHistorical.OperationMetric.Bucket.Contents.Aggregated.Bins']['meta_info'].parent =_meta_table['Sla.Protocols.Ethernet.StatisticsOnDemandHistoricals.StatisticsOnDemandHistorical.OperationMetric.Bucket.Contents.Aggregated']['meta_info']
_meta_table['Sla.Protocols.Ethernet.StatisticsOnDemandHistoricals.StatisticsOnDemandHistorical.OperationMetric.Bucket.Contents.Unaggregated.Sample']['meta_info'].parent =_meta_table['Sla.Protocols.Ethernet.StatisticsOnDemandHistoricals.StatisticsOnDemandHistorical.OperationMetric.Bucket.Contents.Unaggregated']['meta_info']
_meta_table['Sla.Protocols.Ethernet.StatisticsOnDemandHistoricals.StatisticsOnDemandHistorical.OperationMetric.Bucket.Contents.Aggregated']['meta_info'].parent =_meta_table['Sla.Protocols.Ethernet.StatisticsOnDemandHistoricals.StatisticsOnDemandHistorical.OperationMetric.Bucket.Contents']['meta_info']
_meta_table['Sla.Protocols.Ethernet.StatisticsOnDemandHistoricals.StatisticsOnDemandHistorical.OperationMetric.Bucket.Contents.Unaggregated']['meta_info'].parent =_meta_table['Sla.Protocols.Ethernet.StatisticsOnDemandHistoricals.StatisticsOnDemandHistorical.OperationMetric.Bucket.Contents']['meta_info']
_meta_table['Sla.Protocols.Ethernet.StatisticsOnDemandHistoricals.StatisticsOnDemandHistorical.OperationMetric.Bucket.Contents']['meta_info'].parent =_meta_table['Sla.Protocols.Ethernet.StatisticsOnDemandHistoricals.StatisticsOnDemandHistorical.OperationMetric.Bucket']['meta_info']
_meta_table['Sla.Protocols.Ethernet.StatisticsOnDemandHistoricals.StatisticsOnDemandHistorical.OperationMetric.Config']['meta_info'].parent =_meta_table['Sla.Protocols.Ethernet.StatisticsOnDemandHistoricals.StatisticsOnDemandHistorical.OperationMetric']['meta_info']
_meta_table['Sla.Protocols.Ethernet.StatisticsOnDemandHistoricals.StatisticsOnDemandHistorical.OperationMetric.Bucket']['meta_info'].parent =_meta_table['Sla.Protocols.Ethernet.StatisticsOnDemandHistoricals.StatisticsOnDemandHistorical.OperationMetric']['meta_info']
_meta_table['Sla.Protocols.Ethernet.StatisticsOnDemandHistoricals.StatisticsOnDemandHistorical.SpecificOptions']['meta_info'].parent =_meta_table['Sla.Protocols.Ethernet.StatisticsOnDemandHistoricals.StatisticsOnDemandHistorical']['meta_info']
_meta_table['Sla.Protocols.Ethernet.StatisticsOnDemandHistoricals.StatisticsOnDemandHistorical.OperationSchedule']['meta_info'].parent =_meta_table['Sla.Protocols.Ethernet.StatisticsOnDemandHistoricals.StatisticsOnDemandHistorical']['meta_info']
_meta_table['Sla.Protocols.Ethernet.StatisticsOnDemandHistoricals.StatisticsOnDemandHistorical.OperationMetric']['meta_info'].parent =_meta_table['Sla.Protocols.Ethernet.StatisticsOnDemandHistoricals.StatisticsOnDemandHistorical']['meta_info']
_meta_table['Sla.Protocols.Ethernet.StatisticsOnDemandHistoricals.StatisticsOnDemandHistorical']['meta_info'].parent =_meta_table['Sla.Protocols.Ethernet.StatisticsOnDemandHistoricals']['meta_info']
_meta_table['Sla.Protocols.Ethernet.ConfigErrors.ConfigError']['meta_info'].parent =_meta_table['Sla.Protocols.Ethernet.ConfigErrors']['meta_info']
_meta_table['Sla.Protocols.Ethernet.OnDemandOperations.OnDemandOperation.ProfileOptions.OperationMetric.MetricConfig']['meta_info'].parent =_meta_table['Sla.Protocols.Ethernet.OnDemandOperations.OnDemandOperation.ProfileOptions.OperationMetric']['meta_info']
_meta_table['Sla.Protocols.Ethernet.OnDemandOperations.OnDemandOperation.ProfileOptions.PacketPadding']['meta_info'].parent =_meta_table['Sla.Protocols.Ethernet.OnDemandOperations.OnDemandOperation.ProfileOptions']['meta_info']
_meta_table['Sla.Protocols.Ethernet.OnDemandOperations.OnDemandOperation.ProfileOptions.Priority']['meta_info'].parent =_meta_table['Sla.Protocols.Ethernet.OnDemandOperations.OnDemandOperation.ProfileOptions']['meta_info']
_meta_table['Sla.Protocols.Ethernet.OnDemandOperations.OnDemandOperation.ProfileOptions.OperationSchedule']['meta_info'].parent =_meta_table['Sla.Protocols.Ethernet.OnDemandOperations.OnDemandOperation.ProfileOptions']['meta_info']
_meta_table['Sla.Protocols.Ethernet.OnDemandOperations.OnDemandOperation.ProfileOptions.OperationMetric']['meta_info'].parent =_meta_table['Sla.Protocols.Ethernet.OnDemandOperations.OnDemandOperation.ProfileOptions']['meta_info']
_meta_table['Sla.Protocols.Ethernet.OnDemandOperations.OnDemandOperation.SpecificOptions.ConfiguredOperationOptions']['meta_info'].parent =_meta_table['Sla.Protocols.Ethernet.OnDemandOperations.OnDemandOperation.SpecificOptions']['meta_info']
_meta_table['Sla.Protocols.Ethernet.OnDemandOperations.OnDemandOperation.SpecificOptions.OndemandOperationOptions']['meta_info'].parent =_meta_table['Sla.Protocols.Ethernet.OnDemandOperations.OnDemandOperation.SpecificOptions']['meta_info']
_meta_table['Sla.Protocols.Ethernet.OnDemandOperations.OnDemandOperation.ProfileOptions']['meta_info'].parent =_meta_table['Sla.Protocols.Ethernet.OnDemandOperations.OnDemandOperation']['meta_info']
_meta_table['Sla.Protocols.Ethernet.OnDemandOperations.OnDemandOperation.SpecificOptions']['meta_info'].parent =_meta_table['Sla.Protocols.Ethernet.OnDemandOperations.OnDemandOperation']['meta_info']
_meta_table['Sla.Protocols.Ethernet.OnDemandOperations.OnDemandOperation']['meta_info'].parent =_meta_table['Sla.Protocols.Ethernet.OnDemandOperations']['meta_info']
_meta_table['Sla.Protocols.Ethernet.StatisticsCurrents.StatisticsCurrent.SpecificOptions.ConfiguredOperationOptions']['meta_info'].parent =_meta_table['Sla.Protocols.Ethernet.StatisticsCurrents.StatisticsCurrent.SpecificOptions']['meta_info']
_meta_table['Sla.Protocols.Ethernet.StatisticsCurrents.StatisticsCurrent.SpecificOptions.OndemandOperationOptions']['meta_info'].parent =_meta_table['Sla.Protocols.Ethernet.StatisticsCurrents.StatisticsCurrent.SpecificOptions']['meta_info']
_meta_table['Sla.Protocols.Ethernet.StatisticsCurrents.StatisticsCurrent.OperationMetric.Bucket.Contents.Aggregated.Bins']['meta_info'].parent =_meta_table['Sla.Protocols.Ethernet.StatisticsCurrents.StatisticsCurrent.OperationMetric.Bucket.Contents.Aggregated']['meta_info']
_meta_table['Sla.Protocols.Ethernet.StatisticsCurrents.StatisticsCurrent.OperationMetric.Bucket.Contents.Unaggregated.Sample']['meta_info'].parent =_meta_table['Sla.Protocols.Ethernet.StatisticsCurrents.StatisticsCurrent.OperationMetric.Bucket.Contents.Unaggregated']['meta_info']
_meta_table['Sla.Protocols.Ethernet.StatisticsCurrents.StatisticsCurrent.OperationMetric.Bucket.Contents.Aggregated']['meta_info'].parent =_meta_table['Sla.Protocols.Ethernet.StatisticsCurrents.StatisticsCurrent.OperationMetric.Bucket.Contents']['meta_info']
_meta_table['Sla.Protocols.Ethernet.StatisticsCurrents.StatisticsCurrent.OperationMetric.Bucket.Contents.Unaggregated']['meta_info'].parent =_meta_table['Sla.Protocols.Ethernet.StatisticsCurrents.StatisticsCurrent.OperationMetric.Bucket.Contents']['meta_info']
_meta_table['Sla.Protocols.Ethernet.StatisticsCurrents.StatisticsCurrent.OperationMetric.Bucket.Contents']['meta_info'].parent =_meta_table['Sla.Protocols.Ethernet.StatisticsCurrents.StatisticsCurrent.OperationMetric.Bucket']['meta_info']
_meta_table['Sla.Protocols.Ethernet.StatisticsCurrents.StatisticsCurrent.OperationMetric.Config']['meta_info'].parent =_meta_table['Sla.Protocols.Ethernet.StatisticsCurrents.StatisticsCurrent.OperationMetric']['meta_info']
_meta_table['Sla.Protocols.Ethernet.StatisticsCurrents.StatisticsCurrent.OperationMetric.Bucket']['meta_info'].parent =_meta_table['Sla.Protocols.Ethernet.StatisticsCurrents.StatisticsCurrent.OperationMetric']['meta_info']
_meta_table['Sla.Protocols.Ethernet.StatisticsCurrents.StatisticsCurrent.SpecificOptions']['meta_info'].parent =_meta_table['Sla.Protocols.Ethernet.StatisticsCurrents.StatisticsCurrent']['meta_info']
_meta_table['Sla.Protocols.Ethernet.StatisticsCurrents.StatisticsCurrent.OperationSchedule']['meta_info'].parent =_meta_table['Sla.Protocols.Ethernet.StatisticsCurrents.StatisticsCurrent']['meta_info']
_meta_table['Sla.Protocols.Ethernet.StatisticsCurrents.StatisticsCurrent.OperationMetric']['meta_info'].parent =_meta_table['Sla.Protocols.Ethernet.StatisticsCurrents.StatisticsCurrent']['meta_info']
_meta_table['Sla.Protocols.Ethernet.StatisticsCurrents.StatisticsCurrent']['meta_info'].parent =_meta_table['Sla.Protocols.Ethernet.StatisticsCurrents']['meta_info']
_meta_table['Sla.Protocols.Ethernet.StatisticsOnDemandCurrents']['meta_info'].parent =_meta_table['Sla.Protocols.Ethernet']['meta_info']
_meta_table['Sla.Protocols.Ethernet.Operations']['meta_info'].parent =_meta_table['Sla.Protocols.Ethernet']['meta_info']
_meta_table['Sla.Protocols.Ethernet.StatisticsHistoricals']['meta_info'].parent =_meta_table['Sla.Protocols.Ethernet']['meta_info']
_meta_table['Sla.Protocols.Ethernet.StatisticsOnDemandHistoricals']['meta_info'].parent =_meta_table['Sla.Protocols.Ethernet']['meta_info']
_meta_table['Sla.Protocols.Ethernet.ConfigErrors']['meta_info'].parent =_meta_table['Sla.Protocols.Ethernet']['meta_info']
_meta_table['Sla.Protocols.Ethernet.OnDemandOperations']['meta_info'].parent =_meta_table['Sla.Protocols.Ethernet']['meta_info']
_meta_table['Sla.Protocols.Ethernet.StatisticsCurrents']['meta_info'].parent =_meta_table['Sla.Protocols.Ethernet']['meta_info']
_meta_table['Sla.Protocols.Ethernet']['meta_info'].parent =_meta_table['Sla.Protocols']['meta_info']
_meta_table['Sla.Protocols']['meta_info'].parent =_meta_table['Sla']['meta_info']
