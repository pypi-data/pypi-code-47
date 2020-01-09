
'''
This is auto-generated file,
which includes metadata for module Cisco_IOS_XR_infra_rcmd_cfg
'''

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_LIST, REFERENCE_LEAFLIST, REFERENCE_BITS, REFERENCE_UNION
from ydk._core._dm_meta_info import REFERENCE_CLASS, REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, ANYXML_CLASS
from ydk._core._importer import _yang_ns

_meta_table = {
    'RcmdPriority' : _MetaInfoEnum('RcmdPriority',
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_cfg', 'RcmdPriority',
        '''Rcmd priority''',
        {
            'critical':'critical',
            'high':'high',
            'medium':'medium',
            'low':'low',
        }, 'Cisco-IOS-XR-infra-rcmd-cfg', _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-infra-rcmd-cfg']),
    'ProtocolName' : _MetaInfoEnum('ProtocolName',
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_cfg', 'ProtocolName',
        '''Protocol name''',
        {
            'ospf':'ospf',
            'isis':'isis',
        }, 'Cisco-IOS-XR-infra-rcmd-cfg', _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-infra-rcmd-cfg']),
    'RouterConvergence.Protocols.Protocol.Priorities.Priority' : {
        'meta_info' : _MetaInfoClass('RouterConvergence.Protocols.Protocol.Priorities.Priority', REFERENCE_LIST,
            '''Priority''',
            False, 
            [
            _MetaInfoClassMember('rcmd-priority', REFERENCE_ENUM_CLASS, 'RcmdPriority', 'Rcmd-priority',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_cfg', 'RcmdPriority',
                [], [],
                '''                Specify the priority
                ''',
                'rcmd_priority',
                'Cisco-IOS-XR-infra-rcmd-cfg', True),
            _MetaInfoClassMember('threshold', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('0', '4294967295')], [],
                '''                Threshold value for convergence (in msec)
                ''',
                'threshold',
                'Cisco-IOS-XR-infra-rcmd-cfg', False),
            _MetaInfoClassMember('leaf-networks', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('10', '100')], [],
                '''                Specify the maximum number of leaf networks
                monitored
                ''',
                'leaf_networks',
                'Cisco-IOS-XR-infra-rcmd-cfg', False),
            _MetaInfoClassMember('disable', ATTRIBUTE, 'Empty', 'empty',
                None, None,
                [], [],
                '''                Disables the monitoring of route convergence
                for specified priority
                ''',
                'disable',
                'Cisco-IOS-XR-infra-rcmd-cfg', False),
            _MetaInfoClassMember('enable', ATTRIBUTE, 'Empty', 'empty',
                None, None,
                [], [],
                '''                Enable Priority. Deletion of this object
                also causes deletion of all associated
                objects under Priority.
                ''',
                'enable',
                'Cisco-IOS-XR-infra-rcmd-cfg', False),
            _MetaInfoClassMember('frr-threshold', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('1', '100')], [],
                '''                Threshold value for Fast ReRoute Coverage
                (in percentage)
                ''',
                'frr_threshold',
                'Cisco-IOS-XR-infra-rcmd-cfg', False),
            ],
            'Cisco-IOS-XR-infra-rcmd-cfg',
            'priority',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-infra-rcmd-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_cfg',
        ),
    },
    'RouterConvergence.Protocols.Protocol.Priorities' : {
        'meta_info' : _MetaInfoClass('RouterConvergence.Protocols.Protocol.Priorities', REFERENCE_CLASS,
            '''Table of Priority''',
            False, 
            [
            _MetaInfoClassMember('priority', REFERENCE_LIST, 'Priority', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_cfg', 'RouterConvergence.Protocols.Protocol.Priorities.Priority',
                [], [],
                '''                Priority
                ''',
                'priority',
                'Cisco-IOS-XR-infra-rcmd-cfg', False),
            ],
            'Cisco-IOS-XR-infra-rcmd-cfg',
            'priorities',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-infra-rcmd-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_cfg',
        ),
    },
    'RouterConvergence.Protocols.Protocol' : {
        'meta_info' : _MetaInfoClass('RouterConvergence.Protocols.Protocol', REFERENCE_LIST,
            '''Protocol for which to configure RCMD parameters''',
            False, 
            [
            _MetaInfoClassMember('protocol-name', REFERENCE_ENUM_CLASS, 'ProtocolName', 'Protocol-name',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_cfg', 'ProtocolName',
                [], [],
                '''                Specify the protocol
                ''',
                'protocol_name',
                'Cisco-IOS-XR-infra-rcmd-cfg', True),
            _MetaInfoClassMember('priorities', REFERENCE_CLASS, 'Priorities', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_cfg', 'RouterConvergence.Protocols.Protocol.Priorities',
                [], [],
                '''                Table of Priority
                ''',
                'priorities',
                'Cisco-IOS-XR-infra-rcmd-cfg', False),
            _MetaInfoClassMember('enable', ATTRIBUTE, 'Empty', 'empty',
                None, None,
                [], [],
                '''                Enable Protocol for which to configure RCMD
                parameters. Deletion of this object also
                causes deletion of all associated objects
                under Protocol.
                ''',
                'enable',
                'Cisco-IOS-XR-infra-rcmd-cfg', False),
            ],
            'Cisco-IOS-XR-infra-rcmd-cfg',
            'protocol',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-infra-rcmd-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_cfg',
        ),
    },
    'RouterConvergence.Protocols' : {
        'meta_info' : _MetaInfoClass('RouterConvergence.Protocols', REFERENCE_CLASS,
            '''Table of Protocol''',
            False, 
            [
            _MetaInfoClassMember('protocol', REFERENCE_LIST, 'Protocol', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_cfg', 'RouterConvergence.Protocols.Protocol',
                [], [],
                '''                Protocol for which to configure RCMD parameters
                ''',
                'protocol',
                'Cisco-IOS-XR-infra-rcmd-cfg', False),
            ],
            'Cisco-IOS-XR-infra-rcmd-cfg',
            'protocols',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-infra-rcmd-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_cfg',
        ),
    },
    'RouterConvergence.StorageLocation' : {
        'meta_info' : _MetaInfoClass('RouterConvergence.StorageLocation', REFERENCE_CLASS,
            '''Absolute directory path for saving the archive
files. Example /disk0:/rcmd/ or
<tftp-location>/rcmd/''',
            False, 
            [
            _MetaInfoClassMember('diagnostics', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                Absolute directory path for storing diagnostic
                reports. Example /disk0:/rcmd/ or
                <tftp-location>/rcmd/
                ''',
                'diagnostics',
                'Cisco-IOS-XR-infra-rcmd-cfg', False),
            _MetaInfoClassMember('diagnostics-size', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('5', '80')], [],
                '''                Maximum size of diagnostics dir (5% - 80%) for
                local storage.
                ''',
                'diagnostics_size',
                'Cisco-IOS-XR-infra-rcmd-cfg', False),
            _MetaInfoClassMember('reports-size', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('5', '80')], [],
                '''                Maximum size of reports dir (5% - 80%) for
                local storage.
                ''',
                'reports_size',
                'Cisco-IOS-XR-infra-rcmd-cfg', False),
            _MetaInfoClassMember('reports', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                Absolute directory path for storing reports.
                Example /disk0:/rcmd/ or <tftp-location>/rcmd/
                ''',
                'reports',
                'Cisco-IOS-XR-infra-rcmd-cfg', False),
            ],
            'Cisco-IOS-XR-infra-rcmd-cfg',
            'storage-location',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-infra-rcmd-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_cfg',
            is_presence=True,
        ),
    },
    'RouterConvergence.MplsLdp.RemoteLfa' : {
        'meta_info' : _MetaInfoClass('RouterConvergence.MplsLdp.RemoteLfa', REFERENCE_CLASS,
            '''Monitoring configuration for Remote LFA''',
            False, 
            [
            _MetaInfoClassMember('threshold', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('1', '100')], [],
                '''                Threshold value for label coverage (in
                percentage)
                ''',
                'threshold',
                'Cisco-IOS-XR-infra-rcmd-cfg', False),
            ],
            'Cisco-IOS-XR-infra-rcmd-cfg',
            'remote-lfa',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-infra-rcmd-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_cfg',
            is_presence=True,
        ),
    },
    'RouterConvergence.MplsLdp' : {
        'meta_info' : _MetaInfoClass('RouterConvergence.MplsLdp', REFERENCE_CLASS,
            '''RCMD related configuration for MPLS-LDP''',
            False, 
            [
            _MetaInfoClassMember('remote-lfa', REFERENCE_CLASS, 'RemoteLfa', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_cfg', 'RouterConvergence.MplsLdp.RemoteLfa',
                [], [],
                '''                Monitoring configuration for Remote LFA
                ''',
                'remote_lfa',
                'Cisco-IOS-XR-infra-rcmd-cfg', False, is_presence=True),
            ],
            'Cisco-IOS-XR-infra-rcmd-cfg',
            'mpls-ldp',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-infra-rcmd-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_cfg',
            is_presence=True,
        ),
    },
    'RouterConvergence.CollectDiagnostics.CollectDiagnostic' : {
        'meta_info' : _MetaInfoClass('RouterConvergence.CollectDiagnostics.CollectDiagnostic', REFERENCE_LIST,
            '''Collect diagnostics on specified node''',
            False, 
            [
            _MetaInfoClassMember('node-name', ATTRIBUTE, 'str', 'xr:Node-id',
                None, None,
                [], [b'([a-zA-Z0-9_]*\\d+/){1,2}([a-zA-Z0-9_]*\\d+)'],
                '''                Specified location
                ''',
                'node_name',
                'Cisco-IOS-XR-infra-rcmd-cfg', True),
            _MetaInfoClassMember('enable', ATTRIBUTE, 'Empty', 'empty',
                None, None,
                [], [],
                '''                Enables collection of diagnostics on the
                specified location
                ''',
                'enable',
                'Cisco-IOS-XR-infra-rcmd-cfg', False),
            ],
            'Cisco-IOS-XR-infra-rcmd-cfg',
            'collect-diagnostic',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-infra-rcmd-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_cfg',
        ),
    },
    'RouterConvergence.CollectDiagnostics' : {
        'meta_info' : _MetaInfoClass('RouterConvergence.CollectDiagnostics', REFERENCE_CLASS,
            '''Table of CollectDiagnostics''',
            False, 
            [
            _MetaInfoClassMember('collect-diagnostic', REFERENCE_LIST, 'CollectDiagnostic', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_cfg', 'RouterConvergence.CollectDiagnostics.CollectDiagnostic',
                [], [],
                '''                Collect diagnostics on specified node
                ''',
                'collect_diagnostic',
                'Cisco-IOS-XR-infra-rcmd-cfg', False),
            ],
            'Cisco-IOS-XR-infra-rcmd-cfg',
            'collect-diagnostics',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-infra-rcmd-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_cfg',
        ),
    },
    'RouterConvergence.Nodes.Node' : {
        'meta_info' : _MetaInfoClass('RouterConvergence.Nodes.Node', REFERENCE_LIST,
            '''Configure parameters for the specified node
(Partially qualified location allowed)''',
            False, 
            [
            _MetaInfoClassMember('node-name', ATTRIBUTE, 'str', 'xr:Pq-node-id',
                None, None,
                [], [b'((([a-zA-Z0-9_]*\\d+)|(\\*))/){2}(([a-zA-Z0-9_]*\\d+)|(\\*))'],
                '''                Wildcard expression(eg. */*/*, R/*/*, R/S/*,
                R/S/I)
                ''',
                'node_name',
                'Cisco-IOS-XR-infra-rcmd-cfg', True),
            _MetaInfoClassMember('disable', ATTRIBUTE, 'Empty', 'empty',
                None, None,
                [], [],
                '''                Disables the monitoring of route convergence
                on specified location
                ''',
                'disable',
                'Cisco-IOS-XR-infra-rcmd-cfg', False),
            _MetaInfoClassMember('enable', ATTRIBUTE, 'Empty', 'empty',
                None, None,
                [], [],
                '''                Enable Configure parameters for the specified
                node (Partially qualified location allowed).
                Deletion of this object also causes deletion
                of all associated objects under Node.
                ''',
                'enable',
                'Cisco-IOS-XR-infra-rcmd-cfg', False),
            ],
            'Cisco-IOS-XR-infra-rcmd-cfg',
            'node',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-infra-rcmd-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_cfg',
        ),
    },
    'RouterConvergence.Nodes' : {
        'meta_info' : _MetaInfoClass('RouterConvergence.Nodes', REFERENCE_CLASS,
            '''Table of Node''',
            False, 
            [
            _MetaInfoClassMember('node', REFERENCE_LIST, 'Node', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_cfg', 'RouterConvergence.Nodes.Node',
                [], [],
                '''                Configure parameters for the specified node
                (Partially qualified location allowed)
                ''',
                'node',
                'Cisco-IOS-XR-infra-rcmd-cfg', False),
            ],
            'Cisco-IOS-XR-infra-rcmd-cfg',
            'nodes',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-infra-rcmd-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_cfg',
        ),
    },
    'RouterConvergence' : {
        'meta_info' : _MetaInfoClass('RouterConvergence', REFERENCE_CLASS,
            '''Configure Router Convergence Monitoring''',
            False, 
            [
            _MetaInfoClassMember('protocols', REFERENCE_CLASS, 'Protocols', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_cfg', 'RouterConvergence.Protocols',
                [], [],
                '''                Table of Protocol
                ''',
                'protocols',
                'Cisco-IOS-XR-infra-rcmd-cfg', False),
            _MetaInfoClassMember('storage-location', REFERENCE_CLASS, 'StorageLocation', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_cfg', 'RouterConvergence.StorageLocation',
                [], [],
                '''                Absolute directory path for saving the archive
                files. Example /disk0:/rcmd/ or
                <tftp-location>/rcmd/
                ''',
                'storage_location',
                'Cisco-IOS-XR-infra-rcmd-cfg', False, is_presence=True),
            _MetaInfoClassMember('mpls-ldp', REFERENCE_CLASS, 'MplsLdp', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_cfg', 'RouterConvergence.MplsLdp',
                [], [],
                '''                RCMD related configuration for MPLS-LDP
                ''',
                'mpls_ldp',
                'Cisco-IOS-XR-infra-rcmd-cfg', False, is_presence=True),
            _MetaInfoClassMember('collect-diagnostics', REFERENCE_CLASS, 'CollectDiagnostics', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_cfg', 'RouterConvergence.CollectDiagnostics',
                [], [],
                '''                Table of CollectDiagnostics
                ''',
                'collect_diagnostics',
                'Cisco-IOS-XR-infra-rcmd-cfg', False),
            _MetaInfoClassMember('nodes', REFERENCE_CLASS, 'Nodes', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_cfg', 'RouterConvergence.Nodes',
                [], [],
                '''                Table of Node
                ''',
                'nodes',
                'Cisco-IOS-XR-infra-rcmd-cfg', False),
            _MetaInfoClassMember('event-buffer-size', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('100', '500')], [],
                '''                Event buffer size for storing event traces (as
                number of events)
                ''',
                'event_buffer_size',
                'Cisco-IOS-XR-infra-rcmd-cfg', False),
            _MetaInfoClassMember('prefix-monitor-limit', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('0', '100')], [],
                '''                Limits Individual Prefix Monitoring
                ''',
                'prefix_monitor_limit',
                'Cisco-IOS-XR-infra-rcmd-cfg', False),
            _MetaInfoClassMember('disable', ATTRIBUTE, 'Empty', 'empty',
                None, None,
                [], [],
                '''                Disable the monitoring of route convergence on
                the entire router
                ''',
                'disable',
                'Cisco-IOS-XR-infra-rcmd-cfg', False),
            _MetaInfoClassMember('enable', ATTRIBUTE, 'Empty', 'empty',
                None, None,
                [], [],
                '''                Enable Configure Router Convergence Monitoring.
                Deletion of this object also causes deletion of
                all associated objects under RouterConvergence.
                ''',
                'enable',
                'Cisco-IOS-XR-infra-rcmd-cfg', False),
            _MetaInfoClassMember('max-events-stored', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('10', '500')], [],
                '''                Maximum number of events stored in the server
                ''',
                'max_events_stored',
                'Cisco-IOS-XR-infra-rcmd-cfg', False),
            _MetaInfoClassMember('monitoring-interval', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('5', '120')], [],
                '''                Interval in which to collect logs (in mins)
                ''',
                'monitoring_interval',
                'Cisco-IOS-XR-infra-rcmd-cfg', False),
            ],
            'Cisco-IOS-XR-infra-rcmd-cfg',
            'router-convergence',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-infra-rcmd-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_cfg',
        ),
    },
}
_meta_table['RouterConvergence.Protocols.Protocol.Priorities.Priority']['meta_info'].parent =_meta_table['RouterConvergence.Protocols.Protocol.Priorities']['meta_info']
_meta_table['RouterConvergence.Protocols.Protocol.Priorities']['meta_info'].parent =_meta_table['RouterConvergence.Protocols.Protocol']['meta_info']
_meta_table['RouterConvergence.Protocols.Protocol']['meta_info'].parent =_meta_table['RouterConvergence.Protocols']['meta_info']
_meta_table['RouterConvergence.MplsLdp.RemoteLfa']['meta_info'].parent =_meta_table['RouterConvergence.MplsLdp']['meta_info']
_meta_table['RouterConvergence.CollectDiagnostics.CollectDiagnostic']['meta_info'].parent =_meta_table['RouterConvergence.CollectDiagnostics']['meta_info']
_meta_table['RouterConvergence.Nodes.Node']['meta_info'].parent =_meta_table['RouterConvergence.Nodes']['meta_info']
_meta_table['RouterConvergence.Protocols']['meta_info'].parent =_meta_table['RouterConvergence']['meta_info']
_meta_table['RouterConvergence.StorageLocation']['meta_info'].parent =_meta_table['RouterConvergence']['meta_info']
_meta_table['RouterConvergence.MplsLdp']['meta_info'].parent =_meta_table['RouterConvergence']['meta_info']
_meta_table['RouterConvergence.CollectDiagnostics']['meta_info'].parent =_meta_table['RouterConvergence']['meta_info']
_meta_table['RouterConvergence.Nodes']['meta_info'].parent =_meta_table['RouterConvergence']['meta_info']
