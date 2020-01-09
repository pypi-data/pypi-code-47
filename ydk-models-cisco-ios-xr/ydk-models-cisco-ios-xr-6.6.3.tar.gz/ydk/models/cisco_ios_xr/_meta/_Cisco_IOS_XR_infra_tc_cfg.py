
'''
This is auto-generated file,
which includes metadata for module Cisco_IOS_XR_infra_tc_cfg
'''

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_LIST, REFERENCE_LEAFLIST, REFERENCE_BITS, REFERENCE_UNION
from ydk._core._dm_meta_info import REFERENCE_CLASS, REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, ANYXML_CLASS
from ydk._core._importer import _yang_ns

_meta_table = {
    'HistorySize' : _MetaInfoEnum('HistorySize',
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_tc_cfg', 'HistorySize',
        ''' ''',
        {
            'max':'max',
        }, 'Cisco-IOS-XR-infra-tc-cfg', _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-infra-tc-cfg']),
    'CollectIonInterval' : _MetaInfoEnum('CollectIonInterval',
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_tc_cfg', 'CollectIonInterval',
        '''Collect ion interval''',
        {
            '1-minute':'Y_1_minute',
            '2-minutes':'Y_2_minutes',
            '3-minutes':'Y_3_minutes',
            '4-minutes':'Y_4_minutes',
            '5-minutes':'Y_5_minutes',
            '6-minutes':'Y_6_minutes',
            '10-minutes':'Y_10_minutes',
            '12-minutes':'Y_12_minutes',
            '15-minutes':'Y_15_minutes',
            '20-minutes':'Y_20_minutes',
            '30-minutes':'Y_30_minutes',
            '60-minutes':'Y_60_minutes',
        }, 'Cisco-IOS-XR-infra-tc-cfg', _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-infra-tc-cfg']),
    'HistoryTimeout' : _MetaInfoEnum('HistoryTimeout',
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_tc_cfg', 'HistoryTimeout',
        ''' ''',
        {
            'max':'max',
        }, 'Cisco-IOS-XR-infra-tc-cfg', _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-infra-tc-cfg']),
    'TrafficCollector.ExternalInterfaces.ExternalInterface' : {
        'meta_info' : _MetaInfoClass('TrafficCollector.ExternalInterfaces.ExternalInterface', REFERENCE_LIST,
            '''Configure an external internface''',
            False, 
            [
            _MetaInfoClassMember('interface-name', ATTRIBUTE, 'str', 'xr:Interface-name',
                None, None,
                [], [b'[a-zA-Z0-9._/-]+'],
                '''                Name of interface
                ''',
                'interface_name',
                'Cisco-IOS-XR-infra-tc-cfg', True),
            _MetaInfoClassMember('enable', ATTRIBUTE, 'Empty', 'empty',
                None, None,
                [], [],
                '''                Enable traffic collector on this interface
                ''',
                'enable',
                'Cisco-IOS-XR-infra-tc-cfg', False),
            ],
            'Cisco-IOS-XR-infra-tc-cfg',
            'external-interface',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-infra-tc-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_tc_cfg',
        ),
    },
    'TrafficCollector.ExternalInterfaces' : {
        'meta_info' : _MetaInfoClass('TrafficCollector.ExternalInterfaces', REFERENCE_CLASS,
            '''Configure external interfaces''',
            False, 
            [
            _MetaInfoClassMember('external-interface', REFERENCE_LIST, 'ExternalInterface', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_tc_cfg', 'TrafficCollector.ExternalInterfaces.ExternalInterface',
                [], [],
                '''                Configure an external internface
                ''',
                'external_interface',
                'Cisco-IOS-XR-infra-tc-cfg', False),
            ],
            'Cisco-IOS-XR-infra-tc-cfg',
            'external-interfaces',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-infra-tc-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_tc_cfg',
        ),
    },
    'TrafficCollector.Statistics' : {
        'meta_info' : _MetaInfoClass('TrafficCollector.Statistics', REFERENCE_CLASS,
            '''Configure statistics related parameters''',
            False, 
            [
            _MetaInfoClassMember('history-size', REFERENCE_UNION, 'str', 'History-size',
                None, None,
                [], [],
                '''                Configure statistics history size
                ''',
                'history_size',
                'Cisco-IOS-XR-infra-tc-cfg', False, [
                    _MetaInfoClassMember('history-size', REFERENCE_ENUM_CLASS, 'HistorySize', 'enumeration',
                        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_tc_cfg', 'HistorySize',
                        [], [],
                        '''                        Configure statistics history size
                        ''',
                        'history_size',
                        'Cisco-IOS-XR-infra-tc-cfg', False),
                    _MetaInfoClassMember('history-size', ATTRIBUTE, 'int', 'uint32',
                        None, None,
                        [('1', '10')], [],
                        '''                        Configure statistics history size
                        ''',
                        'history_size',
                        'Cisco-IOS-XR-infra-tc-cfg', False),
                ]),
            _MetaInfoClassMember('collection-interval', REFERENCE_ENUM_CLASS, 'CollectIonInterval', 'Collect-ion-interval',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_tc_cfg', 'CollectIonInterval',
                [], [],
                '''                Configure statistics collection interval
                ''',
                'collection_interval',
                'Cisco-IOS-XR-infra-tc-cfg', False),
            _MetaInfoClassMember('enable-traffic-collector-statistics', ATTRIBUTE, 'Empty', 'empty',
                None, None,
                [], [],
                '''                Enable traffic collector statistics
                ''',
                'enable_traffic_collector_statistics',
                'Cisco-IOS-XR-infra-tc-cfg', False),
            _MetaInfoClassMember('history-timeout', REFERENCE_UNION, 'str', 'History-timeout',
                None, None,
                [], [],
                '''                Configure statistics history timeout interval
                ''',
                'history_timeout',
                'Cisco-IOS-XR-infra-tc-cfg', False, [
                    _MetaInfoClassMember('history-timeout', REFERENCE_ENUM_CLASS, 'HistoryTimeout', 'enumeration',
                        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_tc_cfg', 'HistoryTimeout',
                        [], [],
                        '''                        Configure statistics history timeout interval
                        ''',
                        'history_timeout',
                        'Cisco-IOS-XR-infra-tc-cfg', False),
                    _MetaInfoClassMember('history-timeout', ATTRIBUTE, 'int', 'uint32',
                        None, None,
                        [('0', '720')], [],
                        '''                        Configure statistics history timeout interval
                        ''',
                        'history_timeout',
                        'Cisco-IOS-XR-infra-tc-cfg', False),
                ]),
            ],
            'Cisco-IOS-XR-infra-tc-cfg',
            'statistics',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-infra-tc-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_tc_cfg',
        ),
    },
    'TrafficCollector' : {
        'meta_info' : _MetaInfoClass('TrafficCollector', REFERENCE_CLASS,
            '''Global Traffic Collector configuration commands''',
            False, 
            [
            _MetaInfoClassMember('external-interfaces', REFERENCE_CLASS, 'ExternalInterfaces', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_tc_cfg', 'TrafficCollector.ExternalInterfaces',
                [], [],
                '''                Configure external interfaces
                ''',
                'external_interfaces',
                'Cisco-IOS-XR-infra-tc-cfg', False),
            _MetaInfoClassMember('statistics', REFERENCE_CLASS, 'Statistics', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_tc_cfg', 'TrafficCollector.Statistics',
                [], [],
                '''                Configure statistics related parameters
                ''',
                'statistics',
                'Cisco-IOS-XR-infra-tc-cfg', False),
            _MetaInfoClassMember('enable-traffic-collector', ATTRIBUTE, 'Empty', 'empty',
                None, None,
                [], [],
                '''                Enable traffic collector
                ''',
                'enable_traffic_collector',
                'Cisco-IOS-XR-infra-tc-cfg', False),
            ],
            'Cisco-IOS-XR-infra-tc-cfg',
            'traffic-collector',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-infra-tc-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_tc_cfg',
        ),
    },
}
_meta_table['TrafficCollector.ExternalInterfaces.ExternalInterface']['meta_info'].parent =_meta_table['TrafficCollector.ExternalInterfaces']['meta_info']
_meta_table['TrafficCollector.ExternalInterfaces']['meta_info'].parent =_meta_table['TrafficCollector']['meta_info']
_meta_table['TrafficCollector.Statistics']['meta_info'].parent =_meta_table['TrafficCollector']['meta_info']
