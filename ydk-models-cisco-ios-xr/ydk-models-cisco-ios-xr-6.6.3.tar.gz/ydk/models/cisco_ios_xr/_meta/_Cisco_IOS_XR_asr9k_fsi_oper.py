
'''
This is auto-generated file,
which includes metadata for module Cisco_IOS_XR_asr9k_fsi_oper
'''

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_LIST, REFERENCE_LEAFLIST, REFERENCE_BITS, REFERENCE_UNION
from ydk._core._dm_meta_info import REFERENCE_CLASS, REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, ANYXML_CLASS
from ydk._core._importer import _yang_ns

_meta_table = {
    'FabricStats.Nodes.Node.Statses.Stats.StatsTable.FsiStat' : {
        'meta_info' : _MetaInfoClass('FabricStats.Nodes.Node.Statses.Stats.StatsTable.FsiStat', REFERENCE_LIST,
            '''Stats Table''',
            False, 
            [
            _MetaInfoClassMember('count', ATTRIBUTE, 'int', 'uint64',
                None, None,
                [('0', '18446744073709551615')], [],
                '''                Counter
                ''',
                'count',
                'Cisco-IOS-XR-asr9k-fsi-oper', False, is_config=False),
            _MetaInfoClassMember('counter-name', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                Counter Name
                ''',
                'counter_name',
                'Cisco-IOS-XR-asr9k-fsi-oper', False, is_config=False),
            ],
            'Cisco-IOS-XR-asr9k-fsi-oper',
            'fsi-stat',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-asr9k-fsi-oper'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_fsi_oper',
            is_config=False,
        ),
    },
    'FabricStats.Nodes.Node.Statses.Stats.StatsTable' : {
        'meta_info' : _MetaInfoClass('FabricStats.Nodes.Node.Statses.Stats.StatsTable', REFERENCE_LIST,
            '''Array of counters ''',
            False, 
            [
            _MetaInfoClassMember('fsi-stat', REFERENCE_LIST, 'FsiStat', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_fsi_oper', 'FabricStats.Nodes.Node.Statses.Stats.StatsTable.FsiStat',
                [], [],
                '''                Stats Table
                ''',
                'fsi_stat',
                'Cisco-IOS-XR-asr9k-fsi-oper', False, max_elements=60, is_config=False),
            ],
            'Cisco-IOS-XR-asr9k-fsi-oper',
            'stats-table',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-asr9k-fsi-oper'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_fsi_oper',
            is_config=False,
        ),
    },
    'FabricStats.Nodes.Node.Statses.Stats' : {
        'meta_info' : _MetaInfoClass('FabricStats.Nodes.Node.Statses.Stats', REFERENCE_LIST,
            '''Stats information for a particular type''',
            False, 
            [
            _MetaInfoClassMember('type', ATTRIBUTE, 'str', 'xr:Cisco-ios-xr-string',
                None, None,
                [], [b'[\\w\\-\\.:,_@#%$\\+=\\|;]+'],
                '''                Fabric asic type
                ''',
                'type',
                'Cisco-IOS-XR-asr9k-fsi-oper', True, is_config=False),
            _MetaInfoClassMember('last-clear-time', ATTRIBUTE, 'int', 'uint64',
                None, None,
                [('0', '18446744073709551615')], [],
                '''                Last Clear Time
                ''',
                'last_clear_time',
                'Cisco-IOS-XR-asr9k-fsi-oper', False, is_config=False),
            _MetaInfoClassMember('stat-table-name', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                Stat Table Name
                ''',
                'stat_table_name',
                'Cisco-IOS-XR-asr9k-fsi-oper', False, is_config=False),
            _MetaInfoClassMember('stats-table', REFERENCE_LIST, 'StatsTable', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_fsi_oper', 'FabricStats.Nodes.Node.Statses.Stats.StatsTable',
                [], [],
                '''                Array of counters 
                ''',
                'stats_table',
                'Cisco-IOS-XR-asr9k-fsi-oper', False, is_config=False),
            ],
            'Cisco-IOS-XR-asr9k-fsi-oper',
            'stats',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-asr9k-fsi-oper'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_fsi_oper',
            is_config=False,
        ),
    },
    'FabricStats.Nodes.Node.Statses' : {
        'meta_info' : _MetaInfoClass('FabricStats.Nodes.Node.Statses', REFERENCE_CLASS,
            '''Table of stats information''',
            False, 
            [
            _MetaInfoClassMember('stats', REFERENCE_LIST, 'Stats', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_fsi_oper', 'FabricStats.Nodes.Node.Statses.Stats',
                [], [],
                '''                Stats information for a particular type
                ''',
                'stats',
                'Cisco-IOS-XR-asr9k-fsi-oper', False, is_config=False),
            ],
            'Cisco-IOS-XR-asr9k-fsi-oper',
            'statses',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-asr9k-fsi-oper'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_fsi_oper',
            is_config=False,
        ),
    },
    'FabricStats.Nodes.Node' : {
        'meta_info' : _MetaInfoClass('FabricStats.Nodes.Node', REFERENCE_LIST,
            '''Information about a particular node''',
            False, 
            [
            _MetaInfoClassMember('node-name', ATTRIBUTE, 'str', 'xr:Node-id',
                None, None,
                [], [b'([a-zA-Z0-9_]*\\d+/){1,2}([a-zA-Z0-9_]*\\d+)'],
                '''                Node name
                ''',
                'node_name',
                'Cisco-IOS-XR-asr9k-fsi-oper', True, is_config=False),
            _MetaInfoClassMember('statses', REFERENCE_CLASS, 'Statses', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_fsi_oper', 'FabricStats.Nodes.Node.Statses',
                [], [],
                '''                Table of stats information
                ''',
                'statses',
                'Cisco-IOS-XR-asr9k-fsi-oper', False, is_config=False),
            ],
            'Cisco-IOS-XR-asr9k-fsi-oper',
            'node',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-asr9k-fsi-oper'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_fsi_oper',
            is_config=False,
        ),
    },
    'FabricStats.Nodes' : {
        'meta_info' : _MetaInfoClass('FabricStats.Nodes', REFERENCE_CLASS,
            '''Table of Nodes''',
            False, 
            [
            _MetaInfoClassMember('node', REFERENCE_LIST, 'Node', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_fsi_oper', 'FabricStats.Nodes.Node',
                [], [],
                '''                Information about a particular node
                ''',
                'node',
                'Cisco-IOS-XR-asr9k-fsi-oper', False, is_config=False),
            ],
            'Cisco-IOS-XR-asr9k-fsi-oper',
            'nodes',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-asr9k-fsi-oper'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_fsi_oper',
            is_config=False,
        ),
    },
    'FabricStats' : {
        'meta_info' : _MetaInfoClass('FabricStats', REFERENCE_CLASS,
            '''Fabric stats operational data''',
            False, 
            [
            _MetaInfoClassMember('nodes', REFERENCE_CLASS, 'Nodes', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_fsi_oper', 'FabricStats.Nodes',
                [], [],
                '''                Table of Nodes
                ''',
                'nodes',
                'Cisco-IOS-XR-asr9k-fsi-oper', False, is_config=False),
            ],
            'Cisco-IOS-XR-asr9k-fsi-oper',
            'fabric-stats',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-asr9k-fsi-oper'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_fsi_oper',
            is_config=False,
        ),
    },
}
_meta_table['FabricStats.Nodes.Node.Statses.Stats.StatsTable.FsiStat']['meta_info'].parent =_meta_table['FabricStats.Nodes.Node.Statses.Stats.StatsTable']['meta_info']
_meta_table['FabricStats.Nodes.Node.Statses.Stats.StatsTable']['meta_info'].parent =_meta_table['FabricStats.Nodes.Node.Statses.Stats']['meta_info']
_meta_table['FabricStats.Nodes.Node.Statses.Stats']['meta_info'].parent =_meta_table['FabricStats.Nodes.Node.Statses']['meta_info']
_meta_table['FabricStats.Nodes.Node.Statses']['meta_info'].parent =_meta_table['FabricStats.Nodes.Node']['meta_info']
_meta_table['FabricStats.Nodes.Node']['meta_info'].parent =_meta_table['FabricStats.Nodes']['meta_info']
_meta_table['FabricStats.Nodes']['meta_info'].parent =_meta_table['FabricStats']['meta_info']
