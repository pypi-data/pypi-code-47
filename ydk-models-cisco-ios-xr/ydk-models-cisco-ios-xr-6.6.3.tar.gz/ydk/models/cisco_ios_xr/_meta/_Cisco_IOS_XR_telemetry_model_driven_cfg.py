
'''
This is auto-generated file,
which includes metadata for module Cisco_IOS_XR_telemetry_model_driven_cfg
'''

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_LIST, REFERENCE_LEAFLIST, REFERENCE_BITS, REFERENCE_UNION
from ydk._core._dm_meta_info import REFERENCE_CLASS, REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, ANYXML_CLASS
from ydk._core._importer import _yang_ns

_meta_table = {
    'ProtoType' : _MetaInfoEnum('ProtoType',
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_telemetry_model_driven_cfg', 'ProtoType',
        '''Proto type''',
        {
            'grpc':'grpc',
            'tcp':'tcp',
            'udp':'udp',
        }, 'Cisco-IOS-XR-telemetry-model-driven-cfg', _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-telemetry-model-driven-cfg']),
    'EncodeType' : _MetaInfoEnum('EncodeType',
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_telemetry_model_driven_cfg', 'EncodeType',
        '''Encode type''',
        {
            'gpb':'gpb',
            'self-describing-gpb':'self_describing_gpb',
            'json':'json',
        }, 'Cisco-IOS-XR-telemetry-model-driven-cfg', _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-telemetry-model-driven-cfg']),
    'MdtDscpValue' : _MetaInfoEnum('MdtDscpValue',
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_telemetry_model_driven_cfg', 'MdtDscpValue',
        '''Mdt dscp value''',
        {
            'default':'default',
            'cs1':'cs1',
            'af11':'af11',
            'af12':'af12',
            'af13':'af13',
            'cs2':'cs2',
            'af21':'af21',
            'af22':'af22',
            'af23':'af23',
            'cs3':'cs3',
            'af31':'af31',
            'af32':'af32',
            'af33':'af33',
            'cs4':'cs4',
            'af41':'af41',
            'af42':'af42',
            'af43':'af43',
            'cs5':'cs5',
            'ef':'ef',
            'cs6':'cs6',
            'cs7':'cs7',
        }, 'Cisco-IOS-XR-telemetry-model-driven-cfg', _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-telemetry-model-driven-cfg']),
    'TelemetryModelDriven.SensorGroups.SensorGroup.SensorPaths.SensorPath' : {
        'meta_info' : _MetaInfoClass('TelemetryModelDriven.SensorGroups.SensorGroup.SensorPaths.SensorPath', REFERENCE_LIST,
            '''Sensor path configuration''',
            False, 
            [
            _MetaInfoClassMember('telemetry-sensor-path', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                Sensor Path
                ''',
                'telemetry_sensor_path',
                'Cisco-IOS-XR-telemetry-model-driven-cfg', True),
            ],
            'Cisco-IOS-XR-telemetry-model-driven-cfg',
            'sensor-path',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-telemetry-model-driven-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_telemetry_model_driven_cfg',
        ),
    },
    'TelemetryModelDriven.SensorGroups.SensorGroup.SensorPaths' : {
        'meta_info' : _MetaInfoClass('TelemetryModelDriven.SensorGroups.SensorGroup.SensorPaths', REFERENCE_CLASS,
            '''Sensor path configuration''',
            False, 
            [
            _MetaInfoClassMember('sensor-path', REFERENCE_LIST, 'SensorPath', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_telemetry_model_driven_cfg', 'TelemetryModelDriven.SensorGroups.SensorGroup.SensorPaths.SensorPath',
                [], [],
                '''                Sensor path configuration
                ''',
                'sensor_path',
                'Cisco-IOS-XR-telemetry-model-driven-cfg', False),
            ],
            'Cisco-IOS-XR-telemetry-model-driven-cfg',
            'sensor-paths',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-telemetry-model-driven-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_telemetry_model_driven_cfg',
        ),
    },
    'TelemetryModelDriven.SensorGroups.SensorGroup' : {
        'meta_info' : _MetaInfoClass('TelemetryModelDriven.SensorGroups.SensorGroup', REFERENCE_LIST,
            '''Sensor group configuration''',
            False, 
            [
            _MetaInfoClassMember('sensor-group-identifier', ATTRIBUTE, 'str', 'xr:Cisco-ios-xr-string',
                None, None,
                [], [b'[\\w\\-\\.:,_@#%$\\+=\\|;]+'],
                '''                The identifier for this group
                ''',
                'sensor_group_identifier',
                'Cisco-IOS-XR-telemetry-model-driven-cfg', True),
            _MetaInfoClassMember('sensor-paths', REFERENCE_CLASS, 'SensorPaths', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_telemetry_model_driven_cfg', 'TelemetryModelDriven.SensorGroups.SensorGroup.SensorPaths',
                [], [],
                '''                Sensor path configuration
                ''',
                'sensor_paths',
                'Cisco-IOS-XR-telemetry-model-driven-cfg', False),
            ],
            'Cisco-IOS-XR-telemetry-model-driven-cfg',
            'sensor-group',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-telemetry-model-driven-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_telemetry_model_driven_cfg',
        ),
    },
    'TelemetryModelDriven.SensorGroups' : {
        'meta_info' : _MetaInfoClass('TelemetryModelDriven.SensorGroups', REFERENCE_CLASS,
            '''Sensor group configuration''',
            False, 
            [
            _MetaInfoClassMember('sensor-group', REFERENCE_LIST, 'SensorGroup', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_telemetry_model_driven_cfg', 'TelemetryModelDriven.SensorGroups.SensorGroup',
                [], [],
                '''                Sensor group configuration
                ''',
                'sensor_group',
                'Cisco-IOS-XR-telemetry-model-driven-cfg', False),
            ],
            'Cisco-IOS-XR-telemetry-model-driven-cfg',
            'sensor-groups',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-telemetry-model-driven-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_telemetry_model_driven_cfg',
        ),
    },
    'TelemetryModelDriven.Subscriptions.Subscription.SensorProfiles.SensorProfile' : {
        'meta_info' : _MetaInfoClass('TelemetryModelDriven.Subscriptions.Subscription.SensorProfiles.SensorProfile', REFERENCE_LIST,
            '''Associate Sensor Group with Subscription''',
            False, 
            [
            _MetaInfoClassMember('sensorgroupid', ATTRIBUTE, 'str', 'xr:Cisco-ios-xr-string',
                None, None,
                [], [b'[\\w\\-\\.:,_@#%$\\+=\\|;]+'],
                '''                Reference to the telemetry sensor group name
                ''',
                'sensorgroupid',
                'Cisco-IOS-XR-telemetry-model-driven-cfg', True),
            _MetaInfoClassMember('strict-timer', ATTRIBUTE, 'Empty', 'empty',
                None, None,
                [], [],
                '''                use strict timer
                ''',
                'strict_timer',
                'Cisco-IOS-XR-telemetry-model-driven-cfg', False),
            _MetaInfoClassMember('sample-interval', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('0', '4294967295')], [],
                '''                Sample interval in milliseconds
                ''',
                'sample_interval',
                'Cisco-IOS-XR-telemetry-model-driven-cfg', False),
            ],
            'Cisco-IOS-XR-telemetry-model-driven-cfg',
            'sensor-profile',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-telemetry-model-driven-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_telemetry_model_driven_cfg',
        ),
    },
    'TelemetryModelDriven.Subscriptions.Subscription.SensorProfiles' : {
        'meta_info' : _MetaInfoClass('TelemetryModelDriven.Subscriptions.Subscription.SensorProfiles', REFERENCE_CLASS,
            '''Associate Sensor Groups with Subscription''',
            False, 
            [
            _MetaInfoClassMember('sensor-profile', REFERENCE_LIST, 'SensorProfile', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_telemetry_model_driven_cfg', 'TelemetryModelDriven.Subscriptions.Subscription.SensorProfiles.SensorProfile',
                [], [],
                '''                Associate Sensor Group with Subscription
                ''',
                'sensor_profile',
                'Cisco-IOS-XR-telemetry-model-driven-cfg', False),
            ],
            'Cisco-IOS-XR-telemetry-model-driven-cfg',
            'sensor-profiles',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-telemetry-model-driven-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_telemetry_model_driven_cfg',
        ),
    },
    'TelemetryModelDriven.Subscriptions.Subscription.DestinationProfiles.DestinationProfile' : {
        'meta_info' : _MetaInfoClass('TelemetryModelDriven.Subscriptions.Subscription.DestinationProfiles.DestinationProfile', REFERENCE_LIST,
            '''Associate Destination Group with Subscription''',
            False, 
            [
            _MetaInfoClassMember('destination-id', ATTRIBUTE, 'str', 'xr:Cisco-ios-xr-string',
                None, None,
                [], [b'[\\w\\-\\.:,_@#%$\\+=\\|;]+'],
                '''                Destination Id to associate with
                Subscription
                ''',
                'destination_id',
                'Cisco-IOS-XR-telemetry-model-driven-cfg', True),
            ],
            'Cisco-IOS-XR-telemetry-model-driven-cfg',
            'destination-profile',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-telemetry-model-driven-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_telemetry_model_driven_cfg',
        ),
    },
    'TelemetryModelDriven.Subscriptions.Subscription.DestinationProfiles' : {
        'meta_info' : _MetaInfoClass('TelemetryModelDriven.Subscriptions.Subscription.DestinationProfiles', REFERENCE_CLASS,
            '''Associate Destination Groups with Subscription''',
            False, 
            [
            _MetaInfoClassMember('destination-profile', REFERENCE_LIST, 'DestinationProfile', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_telemetry_model_driven_cfg', 'TelemetryModelDriven.Subscriptions.Subscription.DestinationProfiles.DestinationProfile',
                [], [],
                '''                Associate Destination Group with Subscription
                ''',
                'destination_profile',
                'Cisco-IOS-XR-telemetry-model-driven-cfg', False),
            ],
            'Cisco-IOS-XR-telemetry-model-driven-cfg',
            'destination-profiles',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-telemetry-model-driven-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_telemetry_model_driven_cfg',
        ),
    },
    'TelemetryModelDriven.Subscriptions.Subscription' : {
        'meta_info' : _MetaInfoClass('TelemetryModelDriven.Subscriptions.Subscription', REFERENCE_LIST,
            '''Streaming Telemetry Subscription''',
            False, 
            [
            _MetaInfoClassMember('subscription-identifier', ATTRIBUTE, 'str', 'xr:Cisco-ios-xr-string',
                None, None,
                [], [b'[\\w\\-\\.:,_@#%$\\+=\\|;]+'],
                '''                Subscription identifier string
                ''',
                'subscription_identifier',
                'Cisco-IOS-XR-telemetry-model-driven-cfg', True),
            _MetaInfoClassMember('sensor-profiles', REFERENCE_CLASS, 'SensorProfiles', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_telemetry_model_driven_cfg', 'TelemetryModelDriven.Subscriptions.Subscription.SensorProfiles',
                [], [],
                '''                Associate Sensor Groups with Subscription
                ''',
                'sensor_profiles',
                'Cisco-IOS-XR-telemetry-model-driven-cfg', False),
            _MetaInfoClassMember('destination-profiles', REFERENCE_CLASS, 'DestinationProfiles', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_telemetry_model_driven_cfg', 'TelemetryModelDriven.Subscriptions.Subscription.DestinationProfiles',
                [], [],
                '''                Associate Destination Groups with Subscription
                ''',
                'destination_profiles',
                'Cisco-IOS-XR-telemetry-model-driven-cfg', False),
            _MetaInfoClassMember('source-qos-marking', REFERENCE_ENUM_CLASS, 'MdtDscpValue', 'Mdt-dscp-value',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_telemetry_model_driven_cfg', 'MdtDscpValue',
                [], [],
                '''                Outgoing DSCP value
                ''',
                'source_qos_marking',
                'Cisco-IOS-XR-telemetry-model-driven-cfg', False),
            _MetaInfoClassMember('source-interface', ATTRIBUTE, 'str', 'xr:Interface-name',
                None, None,
                [], [b'[a-zA-Z0-9._/-]+'],
                '''                Source address to use for streaming telemetry
                information
                ''',
                'source_interface',
                'Cisco-IOS-XR-telemetry-model-driven-cfg', False),
            ],
            'Cisco-IOS-XR-telemetry-model-driven-cfg',
            'subscription',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-telemetry-model-driven-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_telemetry_model_driven_cfg',
        ),
    },
    'TelemetryModelDriven.Subscriptions' : {
        'meta_info' : _MetaInfoClass('TelemetryModelDriven.Subscriptions', REFERENCE_CLASS,
            '''Streaming Telemetry Subscription''',
            False, 
            [
            _MetaInfoClassMember('subscription', REFERENCE_LIST, 'Subscription', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_telemetry_model_driven_cfg', 'TelemetryModelDriven.Subscriptions.Subscription',
                [], [],
                '''                Streaming Telemetry Subscription
                ''',
                'subscription',
                'Cisco-IOS-XR-telemetry-model-driven-cfg', False),
            ],
            'Cisco-IOS-XR-telemetry-model-driven-cfg',
            'subscriptions',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-telemetry-model-driven-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_telemetry_model_driven_cfg',
        ),
    },
    'TelemetryModelDriven.Include.Empty' : {
        'meta_info' : _MetaInfoClass('TelemetryModelDriven.Include.Empty', REFERENCE_CLASS,
            '''Include fields with empty values in output.''',
            False, 
            [
            _MetaInfoClassMember('values', ATTRIBUTE, 'Empty', 'empty',
                None, None,
                [], [],
                '''                String type fields with empty string value,
                for example, are omitted by default. This
                provides an option to override this behavior
                and include them in the output.
                ''',
                'values',
                'Cisco-IOS-XR-telemetry-model-driven-cfg', False),
            ],
            'Cisco-IOS-XR-telemetry-model-driven-cfg',
            'empty',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-telemetry-model-driven-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_telemetry_model_driven_cfg',
        ),
    },
    'TelemetryModelDriven.Include' : {
        'meta_info' : _MetaInfoClass('TelemetryModelDriven.Include', REFERENCE_CLASS,
            '''Include fields with empty values in output.''',
            False, 
            [
            _MetaInfoClassMember('empty', REFERENCE_CLASS, 'Empty', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_telemetry_model_driven_cfg', 'TelemetryModelDriven.Include.Empty',
                [], [],
                '''                Include fields with empty values in output.
                ''',
                'empty',
                'Cisco-IOS-XR-telemetry-model-driven-cfg', False),
            ],
            'Cisco-IOS-XR-telemetry-model-driven-cfg',
            'include',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-telemetry-model-driven-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_telemetry_model_driven_cfg',
        ),
    },
    'TelemetryModelDriven.DestinationGroups.DestinationGroup.Ipv6Destinations.Ipv6Destination.Protocol' : {
        'meta_info' : _MetaInfoClass('TelemetryModelDriven.DestinationGroups.DestinationGroup.Ipv6Destinations.Ipv6Destination.Protocol', REFERENCE_CLASS,
            '''Transport Protocol used to transmit telemetry
data to the collector''',
            False, 
            [
            _MetaInfoClassMember('protocol', REFERENCE_ENUM_CLASS, 'ProtoType', 'Proto-type',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_telemetry_model_driven_cfg', 'ProtoType',
                [], [],
                '''                protocol
                ''',
                'protocol',
                'Cisco-IOS-XR-telemetry-model-driven-cfg', False, is_mandatory=True),
            _MetaInfoClassMember('tls-hostname', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                tls hostname
                ''',
                'tls_hostname',
                'Cisco-IOS-XR-telemetry-model-driven-cfg', False),
            _MetaInfoClassMember('no-tls', ATTRIBUTE, 'Empty', 'empty',
                None, None,
                [], [],
                '''                no tls
                ''',
                'no_tls',
                'Cisco-IOS-XR-telemetry-model-driven-cfg', False),
            _MetaInfoClassMember('packetsize', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('484', '65507')], [],
                '''                udp packetsize
                ''',
                'packetsize',
                'Cisco-IOS-XR-telemetry-model-driven-cfg', False, default_value="1472"),
            ],
            'Cisco-IOS-XR-telemetry-model-driven-cfg',
            'protocol',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-telemetry-model-driven-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_telemetry_model_driven_cfg',
            is_presence=True,
        ),
    },
    'TelemetryModelDriven.DestinationGroups.DestinationGroup.Ipv6Destinations.Ipv6Destination' : {
        'meta_info' : _MetaInfoClass('TelemetryModelDriven.DestinationGroups.DestinationGroup.Ipv6Destinations.Ipv6Destination', REFERENCE_LIST,
            '''destination IP address''',
            False, 
            [
            _MetaInfoClassMember('ipv6-address', ATTRIBUTE, 'str', 'inet:ipv6-address-no-zone',
                None, None,
                [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'],
                '''                Destination IPv6 address
                ''',
                'ipv6_address',
                'Cisco-IOS-XR-telemetry-model-driven-cfg', True),
            _MetaInfoClassMember('destination-port', ATTRIBUTE, 'int', 'xr:Cisco-ios-xr-port-number',
                None, None,
                [('1', '65535')], [],
                '''                destination port
                ''',
                'destination_port',
                'Cisco-IOS-XR-telemetry-model-driven-cfg', True),
            _MetaInfoClassMember('encoding', REFERENCE_ENUM_CLASS, 'EncodeType', 'Encode-type',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_telemetry_model_driven_cfg', 'EncodeType',
                [], [],
                '''                Encoding used to transmit telemetry data to the
                collector
                ''',
                'encoding',
                'Cisco-IOS-XR-telemetry-model-driven-cfg', False),
            _MetaInfoClassMember('protocol', REFERENCE_CLASS, 'Protocol', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_telemetry_model_driven_cfg', 'TelemetryModelDriven.DestinationGroups.DestinationGroup.Ipv6Destinations.Ipv6Destination.Protocol',
                [], [],
                '''                Transport Protocol used to transmit telemetry
                data to the collector
                ''',
                'protocol',
                'Cisco-IOS-XR-telemetry-model-driven-cfg', False, is_presence=True),
            ],
            'Cisco-IOS-XR-telemetry-model-driven-cfg',
            'ipv6-destination',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-telemetry-model-driven-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_telemetry_model_driven_cfg',
        ),
    },
    'TelemetryModelDriven.DestinationGroups.DestinationGroup.Ipv6Destinations' : {
        'meta_info' : _MetaInfoClass('TelemetryModelDriven.DestinationGroups.DestinationGroup.Ipv6Destinations', REFERENCE_CLASS,
            '''Destination address configuration''',
            False, 
            [
            _MetaInfoClassMember('ipv6-destination', REFERENCE_LIST, 'Ipv6Destination', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_telemetry_model_driven_cfg', 'TelemetryModelDriven.DestinationGroups.DestinationGroup.Ipv6Destinations.Ipv6Destination',
                [], [],
                '''                destination IP address
                ''',
                'ipv6_destination',
                'Cisco-IOS-XR-telemetry-model-driven-cfg', False),
            ],
            'Cisco-IOS-XR-telemetry-model-driven-cfg',
            'ipv6-destinations',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-telemetry-model-driven-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_telemetry_model_driven_cfg',
        ),
    },
    'TelemetryModelDriven.DestinationGroups.DestinationGroup.Ipv4Destinations.Ipv4Destination.Protocol' : {
        'meta_info' : _MetaInfoClass('TelemetryModelDriven.DestinationGroups.DestinationGroup.Ipv4Destinations.Ipv4Destination.Protocol', REFERENCE_CLASS,
            '''Transport Protocol used to transmit telemetry
data to the collector''',
            False, 
            [
            _MetaInfoClassMember('protocol', REFERENCE_ENUM_CLASS, 'ProtoType', 'Proto-type',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_telemetry_model_driven_cfg', 'ProtoType',
                [], [],
                '''                protocol
                ''',
                'protocol',
                'Cisco-IOS-XR-telemetry-model-driven-cfg', False, is_mandatory=True),
            _MetaInfoClassMember('tls-hostname', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                tls hostname
                ''',
                'tls_hostname',
                'Cisco-IOS-XR-telemetry-model-driven-cfg', False),
            _MetaInfoClassMember('no-tls', ATTRIBUTE, 'Empty', 'empty',
                None, None,
                [], [],
                '''                no tls
                ''',
                'no_tls',
                'Cisco-IOS-XR-telemetry-model-driven-cfg', False),
            _MetaInfoClassMember('packetsize', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('484', '65507')], [],
                '''                udp packetsize
                ''',
                'packetsize',
                'Cisco-IOS-XR-telemetry-model-driven-cfg', False, default_value="1472"),
            ],
            'Cisco-IOS-XR-telemetry-model-driven-cfg',
            'protocol',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-telemetry-model-driven-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_telemetry_model_driven_cfg',
            is_presence=True,
        ),
    },
    'TelemetryModelDriven.DestinationGroups.DestinationGroup.Ipv4Destinations.Ipv4Destination' : {
        'meta_info' : _MetaInfoClass('TelemetryModelDriven.DestinationGroups.DestinationGroup.Ipv4Destinations.Ipv4Destination', REFERENCE_LIST,
            '''destination IP address''',
            False, 
            [
            _MetaInfoClassMember('ipv4-address', ATTRIBUTE, 'str', 'inet:ipv4-address-no-zone',
                None, None,
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'],
                '''                Destination IPv4 address
                ''',
                'ipv4_address',
                'Cisco-IOS-XR-telemetry-model-driven-cfg', True),
            _MetaInfoClassMember('destination-port', ATTRIBUTE, 'int', 'xr:Cisco-ios-xr-port-number',
                None, None,
                [('1', '65535')], [],
                '''                destination port
                ''',
                'destination_port',
                'Cisco-IOS-XR-telemetry-model-driven-cfg', True),
            _MetaInfoClassMember('encoding', REFERENCE_ENUM_CLASS, 'EncodeType', 'Encode-type',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_telemetry_model_driven_cfg', 'EncodeType',
                [], [],
                '''                Encoding used to transmit telemetry data to the
                collector
                ''',
                'encoding',
                'Cisco-IOS-XR-telemetry-model-driven-cfg', False),
            _MetaInfoClassMember('protocol', REFERENCE_CLASS, 'Protocol', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_telemetry_model_driven_cfg', 'TelemetryModelDriven.DestinationGroups.DestinationGroup.Ipv4Destinations.Ipv4Destination.Protocol',
                [], [],
                '''                Transport Protocol used to transmit telemetry
                data to the collector
                ''',
                'protocol',
                'Cisco-IOS-XR-telemetry-model-driven-cfg', False, is_presence=True),
            ],
            'Cisco-IOS-XR-telemetry-model-driven-cfg',
            'ipv4-destination',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-telemetry-model-driven-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_telemetry_model_driven_cfg',
        ),
    },
    'TelemetryModelDriven.DestinationGroups.DestinationGroup.Ipv4Destinations' : {
        'meta_info' : _MetaInfoClass('TelemetryModelDriven.DestinationGroups.DestinationGroup.Ipv4Destinations', REFERENCE_CLASS,
            '''Destination address configuration''',
            False, 
            [
            _MetaInfoClassMember('ipv4-destination', REFERENCE_LIST, 'Ipv4Destination', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_telemetry_model_driven_cfg', 'TelemetryModelDriven.DestinationGroups.DestinationGroup.Ipv4Destinations.Ipv4Destination',
                [], [],
                '''                destination IP address
                ''',
                'ipv4_destination',
                'Cisco-IOS-XR-telemetry-model-driven-cfg', False),
            ],
            'Cisco-IOS-XR-telemetry-model-driven-cfg',
            'ipv4-destinations',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-telemetry-model-driven-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_telemetry_model_driven_cfg',
        ),
    },
    'TelemetryModelDriven.DestinationGroups.DestinationGroup' : {
        'meta_info' : _MetaInfoClass('TelemetryModelDriven.DestinationGroups.DestinationGroup', REFERENCE_LIST,
            '''Destination Group''',
            False, 
            [
            _MetaInfoClassMember('destination-id', ATTRIBUTE, 'str', 'xr:Cisco-ios-xr-string',
                None, None,
                [], [b'[\\w\\-\\.:,_@#%$\\+=\\|;]+'],
                '''                destination group id string
                ''',
                'destination_id',
                'Cisco-IOS-XR-telemetry-model-driven-cfg', True),
            _MetaInfoClassMember('ipv6-destinations', REFERENCE_CLASS, 'Ipv6Destinations', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_telemetry_model_driven_cfg', 'TelemetryModelDriven.DestinationGroups.DestinationGroup.Ipv6Destinations',
                [], [],
                '''                Destination address configuration
                ''',
                'ipv6_destinations',
                'Cisco-IOS-XR-telemetry-model-driven-cfg', False),
            _MetaInfoClassMember('ipv4-destinations', REFERENCE_CLASS, 'Ipv4Destinations', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_telemetry_model_driven_cfg', 'TelemetryModelDriven.DestinationGroups.DestinationGroup.Ipv4Destinations',
                [], [],
                '''                Destination address configuration
                ''',
                'ipv4_destinations',
                'Cisco-IOS-XR-telemetry-model-driven-cfg', False),
            _MetaInfoClassMember('vrf', ATTRIBUTE, 'str', 'xr:Cisco-ios-xr-string',
                None, None,
                [(1, 32)], [],
                '''                Vrf for the destination group
                ''',
                'vrf',
                'Cisco-IOS-XR-telemetry-model-driven-cfg', False),
            ],
            'Cisco-IOS-XR-telemetry-model-driven-cfg',
            'destination-group',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-telemetry-model-driven-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_telemetry_model_driven_cfg',
        ),
    },
    'TelemetryModelDriven.DestinationGroups' : {
        'meta_info' : _MetaInfoClass('TelemetryModelDriven.DestinationGroups', REFERENCE_CLASS,
            '''Destination Group configuration''',
            False, 
            [
            _MetaInfoClassMember('destination-group', REFERENCE_LIST, 'DestinationGroup', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_telemetry_model_driven_cfg', 'TelemetryModelDriven.DestinationGroups.DestinationGroup',
                [], [],
                '''                Destination Group
                ''',
                'destination_group',
                'Cisco-IOS-XR-telemetry-model-driven-cfg', False),
            ],
            'Cisco-IOS-XR-telemetry-model-driven-cfg',
            'destination-groups',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-telemetry-model-driven-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_telemetry_model_driven_cfg',
        ),
    },
    'TelemetryModelDriven' : {
        'meta_info' : _MetaInfoClass('TelemetryModelDriven', REFERENCE_CLASS,
            '''Model Driven Telemetry configuration''',
            False, 
            [
            _MetaInfoClassMember('sensor-groups', REFERENCE_CLASS, 'SensorGroups', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_telemetry_model_driven_cfg', 'TelemetryModelDriven.SensorGroups',
                [], [],
                '''                Sensor group configuration
                ''',
                'sensor_groups',
                'Cisco-IOS-XR-telemetry-model-driven-cfg', False),
            _MetaInfoClassMember('subscriptions', REFERENCE_CLASS, 'Subscriptions', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_telemetry_model_driven_cfg', 'TelemetryModelDriven.Subscriptions',
                [], [],
                '''                Streaming Telemetry Subscription
                ''',
                'subscriptions',
                'Cisco-IOS-XR-telemetry-model-driven-cfg', False),
            _MetaInfoClassMember('include', REFERENCE_CLASS, 'Include', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_telemetry_model_driven_cfg', 'TelemetryModelDriven.Include',
                [], [],
                '''                Include fields with empty values in output.
                ''',
                'include',
                'Cisco-IOS-XR-telemetry-model-driven-cfg', False),
            _MetaInfoClassMember('destination-groups', REFERENCE_CLASS, 'DestinationGroups', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_telemetry_model_driven_cfg', 'TelemetryModelDriven.DestinationGroups',
                [], [],
                '''                Destination Group configuration
                ''',
                'destination_groups',
                'Cisco-IOS-XR-telemetry-model-driven-cfg', False),
            _MetaInfoClassMember('strict-timer', ATTRIBUTE, 'Empty', 'empty',
                None, None,
                [], [],
                '''                enable strict-timer for all subscriptions,
                default is relative timer
                ''',
                'strict_timer',
                'Cisco-IOS-XR-telemetry-model-driven-cfg', False),
            _MetaInfoClassMember('enable', ATTRIBUTE, 'Empty', 'empty',
                None, None,
                [], [],
                '''                Enable Model Driven Telemetry
                ''',
                'enable',
                'Cisco-IOS-XR-telemetry-model-driven-cfg', False),
            _MetaInfoClassMember('max-sensor-paths', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('0', '4000')], [],
                '''                Maximum allowed sensor paths, default: 1000
                ''',
                'max_sensor_paths',
                'Cisco-IOS-XR-telemetry-model-driven-cfg', False),
            _MetaInfoClassMember('max-containers-per-path', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('0', '1024')], [],
                '''                Maximum containers allowed per path, 0 disables
                the check
                ''',
                'max_containers_per_path',
                'Cisco-IOS-XR-telemetry-model-driven-cfg', False),
            _MetaInfoClassMember('tcp-send-timeout', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('0', '30')], [],
                '''                TCP send timeout value, default:30 sec,0 will
                disable the timeout
                ''',
                'tcp_send_timeout',
                'Cisco-IOS-XR-telemetry-model-driven-cfg', False),
            ],
            'Cisco-IOS-XR-telemetry-model-driven-cfg',
            'telemetry-model-driven',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-telemetry-model-driven-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_telemetry_model_driven_cfg',
        ),
    },
}
_meta_table['TelemetryModelDriven.SensorGroups.SensorGroup.SensorPaths.SensorPath']['meta_info'].parent =_meta_table['TelemetryModelDriven.SensorGroups.SensorGroup.SensorPaths']['meta_info']
_meta_table['TelemetryModelDriven.SensorGroups.SensorGroup.SensorPaths']['meta_info'].parent =_meta_table['TelemetryModelDriven.SensorGroups.SensorGroup']['meta_info']
_meta_table['TelemetryModelDriven.SensorGroups.SensorGroup']['meta_info'].parent =_meta_table['TelemetryModelDriven.SensorGroups']['meta_info']
_meta_table['TelemetryModelDriven.Subscriptions.Subscription.SensorProfiles.SensorProfile']['meta_info'].parent =_meta_table['TelemetryModelDriven.Subscriptions.Subscription.SensorProfiles']['meta_info']
_meta_table['TelemetryModelDriven.Subscriptions.Subscription.DestinationProfiles.DestinationProfile']['meta_info'].parent =_meta_table['TelemetryModelDriven.Subscriptions.Subscription.DestinationProfiles']['meta_info']
_meta_table['TelemetryModelDriven.Subscriptions.Subscription.SensorProfiles']['meta_info'].parent =_meta_table['TelemetryModelDriven.Subscriptions.Subscription']['meta_info']
_meta_table['TelemetryModelDriven.Subscriptions.Subscription.DestinationProfiles']['meta_info'].parent =_meta_table['TelemetryModelDriven.Subscriptions.Subscription']['meta_info']
_meta_table['TelemetryModelDriven.Subscriptions.Subscription']['meta_info'].parent =_meta_table['TelemetryModelDriven.Subscriptions']['meta_info']
_meta_table['TelemetryModelDriven.Include.Empty']['meta_info'].parent =_meta_table['TelemetryModelDriven.Include']['meta_info']
_meta_table['TelemetryModelDriven.DestinationGroups.DestinationGroup.Ipv6Destinations.Ipv6Destination.Protocol']['meta_info'].parent =_meta_table['TelemetryModelDriven.DestinationGroups.DestinationGroup.Ipv6Destinations.Ipv6Destination']['meta_info']
_meta_table['TelemetryModelDriven.DestinationGroups.DestinationGroup.Ipv6Destinations.Ipv6Destination']['meta_info'].parent =_meta_table['TelemetryModelDriven.DestinationGroups.DestinationGroup.Ipv6Destinations']['meta_info']
_meta_table['TelemetryModelDriven.DestinationGroups.DestinationGroup.Ipv4Destinations.Ipv4Destination.Protocol']['meta_info'].parent =_meta_table['TelemetryModelDriven.DestinationGroups.DestinationGroup.Ipv4Destinations.Ipv4Destination']['meta_info']
_meta_table['TelemetryModelDriven.DestinationGroups.DestinationGroup.Ipv4Destinations.Ipv4Destination']['meta_info'].parent =_meta_table['TelemetryModelDriven.DestinationGroups.DestinationGroup.Ipv4Destinations']['meta_info']
_meta_table['TelemetryModelDriven.DestinationGroups.DestinationGroup.Ipv6Destinations']['meta_info'].parent =_meta_table['TelemetryModelDriven.DestinationGroups.DestinationGroup']['meta_info']
_meta_table['TelemetryModelDriven.DestinationGroups.DestinationGroup.Ipv4Destinations']['meta_info'].parent =_meta_table['TelemetryModelDriven.DestinationGroups.DestinationGroup']['meta_info']
_meta_table['TelemetryModelDriven.DestinationGroups.DestinationGroup']['meta_info'].parent =_meta_table['TelemetryModelDriven.DestinationGroups']['meta_info']
_meta_table['TelemetryModelDriven.SensorGroups']['meta_info'].parent =_meta_table['TelemetryModelDriven']['meta_info']
_meta_table['TelemetryModelDriven.Subscriptions']['meta_info'].parent =_meta_table['TelemetryModelDriven']['meta_info']
_meta_table['TelemetryModelDriven.Include']['meta_info'].parent =_meta_table['TelemetryModelDriven']['meta_info']
_meta_table['TelemetryModelDriven.DestinationGroups']['meta_info'].parent =_meta_table['TelemetryModelDriven']['meta_info']
