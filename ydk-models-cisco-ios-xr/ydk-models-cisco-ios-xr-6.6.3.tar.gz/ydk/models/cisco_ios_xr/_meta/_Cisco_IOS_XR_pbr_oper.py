
'''
This is auto-generated file,
which includes metadata for module Cisco_IOS_XR_pbr_oper
'''

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_LIST, REFERENCE_LEAFLIST, REFERENCE_BITS, REFERENCE_UNION
from ydk._core._dm_meta_info import REFERENCE_CLASS, REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, ANYXML_CLASS
from ydk._core._importer import _yang_ns

_meta_table = {
    'PolicyState' : _MetaInfoEnum('PolicyState',
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_pbr_oper', 'PolicyState',
        '''Different Interface states''',
        {
            'active':'active',
            'suspended':'suspended',
        }, 'Cisco-IOS-XR-pbr-oper', _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-pbr-oper']),
    'Pbr.Nodes.Node.PolicyMap.Interfaces.Interface.Direction.Input.ClassStat.GeneralStats' : {
        'meta_info' : _MetaInfoClass('Pbr.Nodes.Node.PolicyMap.Interfaces.Interface.Direction.Input.ClassStat.GeneralStats', REFERENCE_CLASS,
            '''general stats''',
            False, 
            [
            _MetaInfoClassMember('transmit-packets', ATTRIBUTE, 'int', 'uint64',
                None, None,
                [('0', '18446744073709551615')], [],
                '''                Transmitted packets (packets/bytes)
                ''',
                'transmit_packets',
                'Cisco-IOS-XR-pbr-oper', False, is_config=False),
            _MetaInfoClassMember('transmit-bytes', ATTRIBUTE, 'int', 'uint64',
                None, None,
                [('0', '18446744073709551615')], [],
                '''                Transmitted bytes (packets/bytes)
                ''',
                'transmit_bytes',
                'Cisco-IOS-XR-pbr-oper', False, is_config=False),
            _MetaInfoClassMember('total-drop-packets', ATTRIBUTE, 'int', 'uint64',
                None, None,
                [('0', '18446744073709551615')], [],
                '''                Dropped packets (packets/bytes)
                ''',
                'total_drop_packets',
                'Cisco-IOS-XR-pbr-oper', False, is_config=False),
            _MetaInfoClassMember('total-drop-bytes', ATTRIBUTE, 'int', 'uint64',
                None, None,
                [('0', '18446744073709551615')], [],
                '''                Dropped bytes (packets/bytes)
                ''',
                'total_drop_bytes',
                'Cisco-IOS-XR-pbr-oper', False, is_config=False),
            _MetaInfoClassMember('total-drop-rate', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('0', '4294967295')], [],
                '''                Total drop rate (packets/bytes)
                ''',
                'total_drop_rate',
                'Cisco-IOS-XR-pbr-oper', False, is_config=False),
            _MetaInfoClassMember('match-data-rate', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('0', '4294967295')], [],
                '''                Incoming matched data rate in kbps
                ''',
                'match_data_rate',
                'Cisco-IOS-XR-pbr-oper', False, is_config=False),
            _MetaInfoClassMember('total-transmit-rate', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('0', '4294967295')], [],
                '''                Total transmit rate in kbps
                ''',
                'total_transmit_rate',
                'Cisco-IOS-XR-pbr-oper', False, is_config=False),
            _MetaInfoClassMember('pre-policy-matched-packets', ATTRIBUTE, 'int', 'uint64',
                None, None,
                [('0', '18446744073709551615')], [],
                '''                Matched pkts before applying policy
                ''',
                'pre_policy_matched_packets',
                'Cisco-IOS-XR-pbr-oper', False, is_config=False),
            _MetaInfoClassMember('pre-policy-matched-bytes', ATTRIBUTE, 'int', 'uint64',
                None, None,
                [('0', '18446744073709551615')], [],
                '''                Matched bytes before applying policy
                ''',
                'pre_policy_matched_bytes',
                'Cisco-IOS-XR-pbr-oper', False, is_config=False),
            ],
            'Cisco-IOS-XR-pbr-oper',
            'general-stats',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-pbr-oper'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_pbr_oper',
            is_config=False,
        ),
    },
    'Pbr.Nodes.Node.PolicyMap.Interfaces.Interface.Direction.Input.ClassStat.HttprStats' : {
        'meta_info' : _MetaInfoClass('Pbr.Nodes.Node.PolicyMap.Interfaces.Interface.Direction.Input.ClassStat.HttprStats', REFERENCE_CLASS,
            '''HTTPR stats''',
            False, 
            [
            _MetaInfoClassMember('rqst-rcvd-packets', ATTRIBUTE, 'int', 'uint64',
                None, None,
                [('0', '18446744073709551615')], [],
                '''                TotalNum of pkts HTTP request received
                ''',
                'rqst_rcvd_packets',
                'Cisco-IOS-XR-pbr-oper', False, is_config=False),
            _MetaInfoClassMember('rqst-rcvd-bytes', ATTRIBUTE, 'int', 'uint64',
                None, None,
                [('0', '18446744073709551615')], [],
                '''                TotalNum of Bytes HTTP request received
                ''',
                'rqst_rcvd_bytes',
                'Cisco-IOS-XR-pbr-oper', False, is_config=False),
            _MetaInfoClassMember('drop-packets', ATTRIBUTE, 'int', 'uint64',
                None, None,
                [('0', '18446744073709551615')], [],
                '''                Dropped  packets
                ''',
                'drop_packets',
                'Cisco-IOS-XR-pbr-oper', False, is_config=False),
            _MetaInfoClassMember('drop-bytes', ATTRIBUTE, 'int', 'uint64',
                None, None,
                [('0', '18446744073709551615')], [],
                '''                Dropped bytes
                ''',
                'drop_bytes',
                'Cisco-IOS-XR-pbr-oper', False, is_config=False),
            _MetaInfoClassMember('resp-sent-packets', ATTRIBUTE, 'int', 'uint64',
                None, None,
                [('0', '18446744073709551615')], [],
                '''                TotalNum of pkts HTTPR response sent
                ''',
                'resp_sent_packets',
                'Cisco-IOS-XR-pbr-oper', False, is_config=False),
            _MetaInfoClassMember('resp-sent-bytes', ATTRIBUTE, 'int', 'uint64',
                None, None,
                [('0', '18446744073709551615')], [],
                '''                TotalNum of Bytes HTTPR response sent
                ''',
                'resp_sent_bytes',
                'Cisco-IOS-XR-pbr-oper', False, is_config=False),
            ],
            'Cisco-IOS-XR-pbr-oper',
            'httpr-stats',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-pbr-oper'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_pbr_oper',
            is_config=False,
        ),
    },
    'Pbr.Nodes.Node.PolicyMap.Interfaces.Interface.Direction.Input.ClassStat.HttpEnrichStats' : {
        'meta_info' : _MetaInfoClass('Pbr.Nodes.Node.PolicyMap.Interfaces.Interface.Direction.Input.ClassStat.HttpEnrichStats', REFERENCE_CLASS,
            '''HTTP Enrichment stats''',
            False, 
            [
            _MetaInfoClassMember('rqst-rcvd-packets', ATTRIBUTE, 'int', 'uint64',
                None, None,
                [('0', '18446744073709551615')], [],
                '''                TotalNum of pkts HTTP request received
                ''',
                'rqst_rcvd_packets',
                'Cisco-IOS-XR-pbr-oper', False, is_config=False),
            _MetaInfoClassMember('rqst-rcvd-bytes', ATTRIBUTE, 'int', 'uint64',
                None, None,
                [('0', '18446744073709551615')], [],
                '''                TotalNum of Bytes HTTP request received
                ''',
                'rqst_rcvd_bytes',
                'Cisco-IOS-XR-pbr-oper', False, is_config=False),
            _MetaInfoClassMember('drop-packets', ATTRIBUTE, 'int', 'uint64',
                None, None,
                [('0', '18446744073709551615')], [],
                '''                Dropped  packets
                ''',
                'drop_packets',
                'Cisco-IOS-XR-pbr-oper', False, is_config=False),
            _MetaInfoClassMember('drop-bytes', ATTRIBUTE, 'int', 'uint64',
                None, None,
                [('0', '18446744073709551615')], [],
                '''                Dropped bytes
                ''',
                'drop_bytes',
                'Cisco-IOS-XR-pbr-oper', False, is_config=False),
            _MetaInfoClassMember('resp-sent-packets', ATTRIBUTE, 'int', 'uint64',
                None, None,
                [('0', '18446744073709551615')], [],
                '''                TotalNum of pkts HTTP Enrichment response sent
                ''',
                'resp_sent_packets',
                'Cisco-IOS-XR-pbr-oper', False, is_config=False),
            _MetaInfoClassMember('resp-sent-bytes', ATTRIBUTE, 'int', 'uint64',
                None, None,
                [('0', '18446744073709551615')], [],
                '''                TotalNum of Bytes HTTP Enrichment response sent
                ''',
                'resp_sent_bytes',
                'Cisco-IOS-XR-pbr-oper', False, is_config=False),
            _MetaInfoClassMember('req-sent-packets', ATTRIBUTE, 'int', 'uint64',
                None, None,
                [('0', '18446744073709551615')], [],
                '''                TotalNum of pkts HTTP Enrichment request sent
                ''',
                'req_sent_packets',
                'Cisco-IOS-XR-pbr-oper', False, is_config=False),
            _MetaInfoClassMember('tcp-sent-packets', ATTRIBUTE, 'int', 'uint64',
                None, None,
                [('0', '18446744073709551615')], [],
                '''                TotalNum of pkts HTTP Enrichment TCP packet sent
                ''',
                'tcp_sent_packets',
                'Cisco-IOS-XR-pbr-oper', False, is_config=False),
            ],
            'Cisco-IOS-XR-pbr-oper',
            'http-enrich-stats',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-pbr-oper'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_pbr_oper',
            is_config=False,
        ),
    },
    'Pbr.Nodes.Node.PolicyMap.Interfaces.Interface.Direction.Input.ClassStat' : {
        'meta_info' : _MetaInfoClass('Pbr.Nodes.Node.PolicyMap.Interfaces.Interface.Direction.Input.ClassStat', REFERENCE_LIST,
            '''Array of classes contained in policy''',
            False, 
            [
            _MetaInfoClassMember('general-stats', REFERENCE_CLASS, 'GeneralStats', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_pbr_oper', 'Pbr.Nodes.Node.PolicyMap.Interfaces.Interface.Direction.Input.ClassStat.GeneralStats',
                [], [],
                '''                general stats
                ''',
                'general_stats',
                'Cisco-IOS-XR-pbr-oper', False, is_config=False),
            _MetaInfoClassMember('httpr-stats', REFERENCE_CLASS, 'HttprStats', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_pbr_oper', 'Pbr.Nodes.Node.PolicyMap.Interfaces.Interface.Direction.Input.ClassStat.HttprStats',
                [], [],
                '''                HTTPR stats
                ''',
                'httpr_stats',
                'Cisco-IOS-XR-pbr-oper', False, is_config=False),
            _MetaInfoClassMember('http-enrich-stats', REFERENCE_CLASS, 'HttpEnrichStats', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_pbr_oper', 'Pbr.Nodes.Node.PolicyMap.Interfaces.Interface.Direction.Input.ClassStat.HttpEnrichStats',
                [], [],
                '''                HTTP Enrichment stats
                ''',
                'http_enrich_stats',
                'Cisco-IOS-XR-pbr-oper', False, is_config=False),
            _MetaInfoClassMember('counter-validity-bitmask', ATTRIBUTE, 'int', 'uint64',
                None, None,
                [('0', '18446744073709551615')], [],
                '''                 Bitmask to indicate which counter or counters
                are undetermined. Counters will be marked
                undetermined when one or more classes share
                queues with class-default because in such cases
                the value of counters for each class is invalid.
                Based on the flag(s) set, the following counters
                will be marked undetermined. For example, if
                value of this object returned is 0x00000101,
                counters
                TransmitPackets/TransmitBytes/TotalTransmitRate
                and DropPackets/DropBytes are undetermined
                .0x00000001 - Transmit
                (TransmitPackets/TransmitBytes/TotalTransmitRate
                ), 0x00000002 - Drop
                (TotalDropPackets/TotalDropBytes/TotalDropRate),
                0x00000004 - Httpr
                (HttprTransmitPackets/HttprTransmitBytes),
                0x00000020 - HttpErich
                (HttpErichTransmitPackets
                /HttpEnrichTransmitBytes), 
                ''',
                'counter_validity_bitmask',
                'Cisco-IOS-XR-pbr-oper', False, is_config=False),
            _MetaInfoClassMember('class-name', ATTRIBUTE, 'str', 'string',
                None, None,
                [(0, 65)], [],
                '''                ClassName
                ''',
                'class_name',
                'Cisco-IOS-XR-pbr-oper', False, is_config=False),
            _MetaInfoClassMember('class-id', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('0', '4294967295')], [],
                '''                ClassId
                ''',
                'class_id',
                'Cisco-IOS-XR-pbr-oper', False, is_config=False),
            ],
            'Cisco-IOS-XR-pbr-oper',
            'class-stat',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-pbr-oper'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_pbr_oper',
            is_config=False,
        ),
    },
    'Pbr.Nodes.Node.PolicyMap.Interfaces.Interface.Direction.Input' : {
        'meta_info' : _MetaInfoClass('Pbr.Nodes.Node.PolicyMap.Interfaces.Interface.Direction.Input', REFERENCE_CLASS,
            '''PBR policy statistics''',
            False, 
            [
            _MetaInfoClassMember('node-name', ATTRIBUTE, 'str', 'string',
                None, None,
                [(0, 42)], [],
                '''                NodeName
                ''',
                'node_name',
                'Cisco-IOS-XR-pbr-oper', False, is_config=False),
            _MetaInfoClassMember('policy-name', ATTRIBUTE, 'str', 'string',
                None, None,
                [(0, 65)], [],
                '''                PolicyName
                ''',
                'policy_name',
                'Cisco-IOS-XR-pbr-oper', False, is_config=False),
            _MetaInfoClassMember('state', REFERENCE_ENUM_CLASS, 'PolicyState', 'Policy-state',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_pbr_oper', 'PolicyState',
                [], [],
                '''                State
                ''',
                'state',
                'Cisco-IOS-XR-pbr-oper', False, is_config=False),
            _MetaInfoClassMember('state-description', ATTRIBUTE, 'str', 'string',
                None, None,
                [(0, 128)], [],
                '''                StateDescription
                ''',
                'state_description',
                'Cisco-IOS-XR-pbr-oper', False, is_config=False),
            _MetaInfoClassMember('class-stat', REFERENCE_LIST, 'ClassStat', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_pbr_oper', 'Pbr.Nodes.Node.PolicyMap.Interfaces.Interface.Direction.Input.ClassStat',
                [], [],
                '''                Array of classes contained in policy
                ''',
                'class_stat',
                'Cisco-IOS-XR-pbr-oper', False, is_config=False),
            ],
            'Cisco-IOS-XR-pbr-oper',
            'input',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-pbr-oper'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_pbr_oper',
            is_config=False,
        ),
    },
    'Pbr.Nodes.Node.PolicyMap.Interfaces.Interface.Direction' : {
        'meta_info' : _MetaInfoClass('Pbr.Nodes.Node.PolicyMap.Interfaces.Interface.Direction', REFERENCE_CLASS,
            '''PBR direction''',
            False, 
            [
            _MetaInfoClassMember('input', REFERENCE_CLASS, 'Input', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_pbr_oper', 'Pbr.Nodes.Node.PolicyMap.Interfaces.Interface.Direction.Input',
                [], [],
                '''                PBR policy statistics
                ''',
                'input',
                'Cisco-IOS-XR-pbr-oper', False, is_config=False),
            ],
            'Cisco-IOS-XR-pbr-oper',
            'direction',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-pbr-oper'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_pbr_oper',
            is_config=False,
        ),
    },
    'Pbr.Nodes.Node.PolicyMap.Interfaces.Interface' : {
        'meta_info' : _MetaInfoClass('Pbr.Nodes.Node.PolicyMap.Interfaces.Interface', REFERENCE_LIST,
            '''PBR action data for a particular interface''',
            False, 
            [
            _MetaInfoClassMember('interface-name', ATTRIBUTE, 'str', 'xr:Interface-name',
                None, None,
                [], [b'[a-zA-Z0-9._/-]+'],
                '''                Name of the interface
                ''',
                'interface_name',
                'Cisco-IOS-XR-pbr-oper', True, is_config=False),
            _MetaInfoClassMember('direction', REFERENCE_CLASS, 'Direction', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_pbr_oper', 'Pbr.Nodes.Node.PolicyMap.Interfaces.Interface.Direction',
                [], [],
                '''                PBR direction
                ''',
                'direction',
                'Cisco-IOS-XR-pbr-oper', False, is_config=False),
            ],
            'Cisco-IOS-XR-pbr-oper',
            'interface',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-pbr-oper'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_pbr_oper',
            is_config=False,
        ),
    },
    'Pbr.Nodes.Node.PolicyMap.Interfaces' : {
        'meta_info' : _MetaInfoClass('Pbr.Nodes.Node.PolicyMap.Interfaces', REFERENCE_CLASS,
            '''Operational data for all interfaces''',
            False, 
            [
            _MetaInfoClassMember('interface', REFERENCE_LIST, 'Interface', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_pbr_oper', 'Pbr.Nodes.Node.PolicyMap.Interfaces.Interface',
                [], [],
                '''                PBR action data for a particular interface
                ''',
                'interface',
                'Cisco-IOS-XR-pbr-oper', False, is_config=False),
            ],
            'Cisco-IOS-XR-pbr-oper',
            'interfaces',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-pbr-oper'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_pbr_oper',
            is_config=False,
        ),
    },
    'Pbr.Nodes.Node.PolicyMap' : {
        'meta_info' : _MetaInfoClass('Pbr.Nodes.Node.PolicyMap', REFERENCE_CLASS,
            '''Operational data for policymaps''',
            False, 
            [
            _MetaInfoClassMember('interfaces', REFERENCE_CLASS, 'Interfaces', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_pbr_oper', 'Pbr.Nodes.Node.PolicyMap.Interfaces',
                [], [],
                '''                Operational data for all interfaces
                ''',
                'interfaces',
                'Cisco-IOS-XR-pbr-oper', False, is_config=False),
            ],
            'Cisco-IOS-XR-pbr-oper',
            'policy-map',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-pbr-oper'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_pbr_oper',
            is_config=False,
        ),
    },
    'Pbr.Nodes.Node' : {
        'meta_info' : _MetaInfoClass('Pbr.Nodes.Node', REFERENCE_LIST,
            '''PBR operational data for a particular node''',
            False, 
            [
            _MetaInfoClassMember('node-name', ATTRIBUTE, 'str', 'xr:Node-id',
                None, None,
                [], [b'([a-zA-Z0-9_]*\\d+/){1,2}([a-zA-Z0-9_]*\\d+)'],
                '''                The node
                ''',
                'node_name',
                'Cisco-IOS-XR-pbr-oper', True, is_config=False),
            _MetaInfoClassMember('policy-map', REFERENCE_CLASS, 'PolicyMap', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_pbr_oper', 'Pbr.Nodes.Node.PolicyMap',
                [], [],
                '''                Operational data for policymaps
                ''',
                'policy_map',
                'Cisco-IOS-XR-pbr-oper', False, is_config=False),
            ],
            'Cisco-IOS-XR-pbr-oper',
            'node',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-pbr-oper'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_pbr_oper',
            is_config=False,
        ),
    },
    'Pbr.Nodes' : {
        'meta_info' : _MetaInfoClass('Pbr.Nodes', REFERENCE_CLASS,
            '''Node-specific PBR operational data''',
            False, 
            [
            _MetaInfoClassMember('node', REFERENCE_LIST, 'Node', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_pbr_oper', 'Pbr.Nodes.Node',
                [], [],
                '''                PBR operational data for a particular node
                ''',
                'node',
                'Cisco-IOS-XR-pbr-oper', False, is_config=False),
            ],
            'Cisco-IOS-XR-pbr-oper',
            'nodes',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-pbr-oper'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_pbr_oper',
            is_config=False,
        ),
    },
    'Pbr' : {
        'meta_info' : _MetaInfoClass('Pbr', REFERENCE_CLASS,
            '''PBR operational data''',
            False, 
            [
            _MetaInfoClassMember('nodes', REFERENCE_CLASS, 'Nodes', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_pbr_oper', 'Pbr.Nodes',
                [], [],
                '''                Node-specific PBR operational data
                ''',
                'nodes',
                'Cisco-IOS-XR-pbr-oper', False, is_config=False),
            ],
            'Cisco-IOS-XR-pbr-oper',
            'pbr',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-pbr-oper'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_pbr_oper',
            is_config=False,
        ),
    },
}
_meta_table['Pbr.Nodes.Node.PolicyMap.Interfaces.Interface.Direction.Input.ClassStat.GeneralStats']['meta_info'].parent =_meta_table['Pbr.Nodes.Node.PolicyMap.Interfaces.Interface.Direction.Input.ClassStat']['meta_info']
_meta_table['Pbr.Nodes.Node.PolicyMap.Interfaces.Interface.Direction.Input.ClassStat.HttprStats']['meta_info'].parent =_meta_table['Pbr.Nodes.Node.PolicyMap.Interfaces.Interface.Direction.Input.ClassStat']['meta_info']
_meta_table['Pbr.Nodes.Node.PolicyMap.Interfaces.Interface.Direction.Input.ClassStat.HttpEnrichStats']['meta_info'].parent =_meta_table['Pbr.Nodes.Node.PolicyMap.Interfaces.Interface.Direction.Input.ClassStat']['meta_info']
_meta_table['Pbr.Nodes.Node.PolicyMap.Interfaces.Interface.Direction.Input.ClassStat']['meta_info'].parent =_meta_table['Pbr.Nodes.Node.PolicyMap.Interfaces.Interface.Direction.Input']['meta_info']
_meta_table['Pbr.Nodes.Node.PolicyMap.Interfaces.Interface.Direction.Input']['meta_info'].parent =_meta_table['Pbr.Nodes.Node.PolicyMap.Interfaces.Interface.Direction']['meta_info']
_meta_table['Pbr.Nodes.Node.PolicyMap.Interfaces.Interface.Direction']['meta_info'].parent =_meta_table['Pbr.Nodes.Node.PolicyMap.Interfaces.Interface']['meta_info']
_meta_table['Pbr.Nodes.Node.PolicyMap.Interfaces.Interface']['meta_info'].parent =_meta_table['Pbr.Nodes.Node.PolicyMap.Interfaces']['meta_info']
_meta_table['Pbr.Nodes.Node.PolicyMap.Interfaces']['meta_info'].parent =_meta_table['Pbr.Nodes.Node.PolicyMap']['meta_info']
_meta_table['Pbr.Nodes.Node.PolicyMap']['meta_info'].parent =_meta_table['Pbr.Nodes.Node']['meta_info']
_meta_table['Pbr.Nodes.Node']['meta_info'].parent =_meta_table['Pbr.Nodes']['meta_info']
_meta_table['Pbr.Nodes']['meta_info'].parent =_meta_table['Pbr']['meta_info']
