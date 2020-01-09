
'''
This is auto-generated file,
which includes metadata for module Cisco_IOS_XR_man_ipsla_cfg
'''

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_LIST, REFERENCE_LEAFLIST, REFERENCE_BITS, REFERENCE_UNION
from ydk._core._dm_meta_info import REFERENCE_CLASS, REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, ANYXML_CLASS
from ydk._core._importer import _yang_ns

_meta_table = {
    'IpslaSecondaryFrequency' : _MetaInfoEnum('IpslaSecondaryFrequency',
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_ipsla_cfg', 'IpslaSecondaryFrequency',
        '''Ipsla secondary frequency''',
        {
            'connection-loss':'connection_loss',
            'timeout':'timeout',
            'both':'both',
        }, 'Cisco-IOS-XR-man-ipsla-cfg', _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-man-ipsla-cfg']),
    'IpslaMonth' : _MetaInfoEnum('IpslaMonth',
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_ipsla_cfg', 'IpslaMonth',
        '''Ipsla month''',
        {
            'january':'january',
            'february':'february',
            'march':'march',
            'april':'april',
            'may':'may',
            'june':'june',
            'july':'july',
            'august':'august',
            'september':'september',
            'october':'october',
            'november':'november',
            'december':'december',
        }, 'Cisco-IOS-XR-man-ipsla-cfg', _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-man-ipsla-cfg']),
    'IpslaLspPingReplyMode' : _MetaInfoEnum('IpslaLspPingReplyMode',
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_ipsla_cfg', 'IpslaLspPingReplyMode',
        '''Ipsla lsp ping reply mode''',
        {
            'ipv4-udp-router-alert':'ipv4_udp_router_alert',
            'control-channel':'control_channel',
        }, 'Cisco-IOS-XR-man-ipsla-cfg', _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-man-ipsla-cfg']),
    'IpslaLspTraceReplyMode' : _MetaInfoEnum('IpslaLspTraceReplyMode',
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_ipsla_cfg', 'IpslaLspTraceReplyMode',
        '''Ipsla lsp trace reply mode''',
        {
            'ipv4-udp-router-alert':'ipv4_udp_router_alert',
        }, 'Cisco-IOS-XR-man-ipsla-cfg', _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-man-ipsla-cfg']),
    'IpslaLspMonitorReplyMode' : _MetaInfoEnum('IpslaLspMonitorReplyMode',
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_ipsla_cfg', 'IpslaLspMonitorReplyMode',
        '''Ipsla lsp monitor reply mode''',
        {
            'ipv4-udp-router-alert':'ipv4_udp_router_alert',
        }, 'Cisco-IOS-XR-man-ipsla-cfg', _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-man-ipsla-cfg']),
    'IpslaSched' : _MetaInfoEnum('IpslaSched',
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_ipsla_cfg', 'IpslaSched',
        '''Ipsla sched''',
        {
            'pending':'pending',
            'now':'now',
            'after':'after',
            'at':'at',
        }, 'Cisco-IOS-XR-man-ipsla-cfg', _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-man-ipsla-cfg']),
    'IpslaLspReplyDscp' : _MetaInfoEnum('IpslaLspReplyDscp',
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_ipsla_cfg', 'IpslaLspReplyDscp',
        ''' ''',
        {
            'default':'default',
            'af11':'af11',
            'af12':'af12',
            'af13':'af13',
            'af21':'af21',
            'af22':'af22',
            'af23':'af23',
            'af31':'af31',
            'af32':'af32',
            'af33':'af33',
            'af41':'af41',
            'af42':'af42',
            'af43':'af43',
            'cs1':'cs1',
            'cs2':'cs2',
            'cs3':'cs3',
            'cs4':'cs4',
            'cs5':'cs5',
            'cs6':'cs6',
            'cs7':'cs7',
            'ef':'ef',
        }, 'Cisco-IOS-XR-man-ipsla-cfg', _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-man-ipsla-cfg']),
    'IpslaLife' : _MetaInfoEnum('IpslaLife',
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_ipsla_cfg', 'IpslaLife',
        ''' ''',
        {
            'forever':'forever',
        }, 'Cisco-IOS-XR-man-ipsla-cfg', _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-man-ipsla-cfg']),
    'IpslaThresholdTypes' : _MetaInfoEnum('IpslaThresholdTypes',
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_ipsla_cfg', 'IpslaThresholdTypes',
        '''Ipsla threshold types''',
        {
            'immediate':'immediate',
            'consecutive':'consecutive',
            'xof-y':'xof_y',
            'average':'average',
        }, 'Cisco-IOS-XR-man-ipsla-cfg', _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-man-ipsla-cfg']),
    'IpslaLspMonitorThresholdTypes' : _MetaInfoEnum('IpslaLspMonitorThresholdTypes',
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_ipsla_cfg', 'IpslaLspMonitorThresholdTypes',
        '''Ipsla lsp monitor threshold types''',
        {
            'immediate':'immediate',
            'consecutive':'consecutive',
        }, 'Cisco-IOS-XR-man-ipsla-cfg', _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-man-ipsla-cfg']),
    'IpslaHistoryFilter' : _MetaInfoEnum('IpslaHistoryFilter',
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_ipsla_cfg', 'IpslaHistoryFilter',
        '''Ipsla history filter''',
        {
            'failed':'failed',
            'all':'all',
        }, 'Cisco-IOS-XR-man-ipsla-cfg', _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-man-ipsla-cfg']),
    'Ipsla.Common.HardwareTimestamp' : {
        'meta_info' : _MetaInfoClass('Ipsla.Common.HardwareTimestamp', REFERENCE_CLASS,
            '''Hardware Timestamp configuration''',
            False, 
            [
            _MetaInfoClassMember('disable', ATTRIBUTE, 'Empty', 'empty',
                None, None,
                [], [],
                '''                states true if hw-timestamp is disabled
                ''',
                'disable',
                'Cisco-IOS-XR-man-ipsla-cfg', False),
            ],
            'Cisco-IOS-XR-man-ipsla-cfg',
            'hardware-timestamp',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-man-ipsla-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_ipsla_cfg',
        ),
    },
    'Ipsla.Common.Authentication' : {
        'meta_info' : _MetaInfoClass('Ipsla.Common.Authentication', REFERENCE_CLASS,
            '''Authenticaion configuration''',
            False, 
            [
            _MetaInfoClassMember('key-chain', ATTRIBUTE, 'str', 'string',
                None, None,
                [(1, 32)], [],
                '''                Use MD5 authentication for IPSLA control
                message
                ''',
                'key_chain',
                'Cisco-IOS-XR-man-ipsla-cfg', False),
            ],
            'Cisco-IOS-XR-man-ipsla-cfg',
            'authentication',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-man-ipsla-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_ipsla_cfg',
        ),
    },
    'Ipsla.Common' : {
        'meta_info' : _MetaInfoClass('Ipsla.Common', REFERENCE_CLASS,
            '''IPSLA application common configuration''',
            False, 
            [
            _MetaInfoClassMember('hardware-timestamp', REFERENCE_CLASS, 'HardwareTimestamp', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_ipsla_cfg', 'Ipsla.Common.HardwareTimestamp',
                [], [],
                '''                Hardware Timestamp configuration
                ''',
                'hardware_timestamp',
                'Cisco-IOS-XR-man-ipsla-cfg', False),
            _MetaInfoClassMember('authentication', REFERENCE_CLASS, 'Authentication', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_ipsla_cfg', 'Ipsla.Common.Authentication',
                [], [],
                '''                Authenticaion configuration
                ''',
                'authentication',
                'Cisco-IOS-XR-man-ipsla-cfg', False),
            _MetaInfoClassMember('low-memory', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('0', '4294967295')], [],
                '''                Configure low memory water mark (default 20M)
                ''',
                'low_memory',
                'Cisco-IOS-XR-man-ipsla-cfg', False, default_value="20480"),
            ],
            'Cisco-IOS-XR-man-ipsla-cfg',
            'common',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-man-ipsla-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_ipsla_cfg',
        ),
    },
    'Ipsla.MplsLspMonitor.Reactions.Reaction.Condition.LpdTreeTrace.ActionType' : {
        'meta_info' : _MetaInfoClass('Ipsla.MplsLspMonitor.Reactions.Reaction.Condition.LpdTreeTrace.ActionType', REFERENCE_CLASS,
            '''Type of action to be taken on threshold
violation(s)''',
            False, 
            [
            _MetaInfoClassMember('logging', ATTRIBUTE, 'Empty', 'empty',
                None, None,
                [], [],
                '''                Generate a syslog alarm on threshold violation
                ''',
                'logging',
                'Cisco-IOS-XR-man-ipsla-cfg', False),
            ],
            'Cisco-IOS-XR-man-ipsla-cfg',
            'action-type',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-man-ipsla-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_ipsla_cfg',
        ),
    },
    'Ipsla.MplsLspMonitor.Reactions.Reaction.Condition.LpdTreeTrace' : {
        'meta_info' : _MetaInfoClass('Ipsla.MplsLspMonitor.Reactions.Reaction.Condition.LpdTreeTrace', REFERENCE_CLASS,
            '''React on LPD Tree Trace violation for a
monitored MPLSLM''',
            False, 
            [
            _MetaInfoClassMember('action-type', REFERENCE_CLASS, 'ActionType', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_ipsla_cfg', 'Ipsla.MplsLspMonitor.Reactions.Reaction.Condition.LpdTreeTrace.ActionType',
                [], [],
                '''                Type of action to be taken on threshold
                violation(s)
                ''',
                'action_type',
                'Cisco-IOS-XR-man-ipsla-cfg', False),
            ],
            'Cisco-IOS-XR-man-ipsla-cfg',
            'lpd-tree-trace',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-man-ipsla-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_ipsla_cfg',
            is_presence=True,
        ),
    },
    'Ipsla.MplsLspMonitor.Reactions.Reaction.Condition.Timeout.ActionType' : {
        'meta_info' : _MetaInfoClass('Ipsla.MplsLspMonitor.Reactions.Reaction.Condition.Timeout.ActionType', REFERENCE_CLASS,
            '''Type of action to be taken on threshold
violation(s)''',
            False, 
            [
            _MetaInfoClassMember('logging', ATTRIBUTE, 'Empty', 'empty',
                None, None,
                [], [],
                '''                Generate a syslog alarm on threshold violation
                ''',
                'logging',
                'Cisco-IOS-XR-man-ipsla-cfg', False),
            ],
            'Cisco-IOS-XR-man-ipsla-cfg',
            'action-type',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-man-ipsla-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_ipsla_cfg',
        ),
    },
    'Ipsla.MplsLspMonitor.Reactions.Reaction.Condition.Timeout.ThresholdType' : {
        'meta_info' : _MetaInfoClass('Ipsla.MplsLspMonitor.Reactions.Reaction.Condition.Timeout.ThresholdType', REFERENCE_CLASS,
            '''Type of thresholding to perform on the monitored
element''',
            False, 
            [
            _MetaInfoClassMember('thresh-type', REFERENCE_ENUM_CLASS, 'IpslaLspMonitorThresholdTypes', 'Ipsla-lsp-monitor-threshold-types',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_ipsla_cfg', 'IpslaLspMonitorThresholdTypes',
                [], [],
                '''                Type of thresholding to perform
                ''',
                'thresh_type',
                'Cisco-IOS-XR-man-ipsla-cfg', False),
            _MetaInfoClassMember('count1', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('1', '16')], [],
                '''                Probe count for consecutive
                ''',
                'count1',
                'Cisco-IOS-XR-man-ipsla-cfg', False, has_when=True),
            _MetaInfoClassMember('count2', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('1', '16')], [],
                '''                Y value, when threshold type is XofY
                ''',
                'count2',
                'Cisco-IOS-XR-man-ipsla-cfg', False, has_when=True),
            ],
            'Cisco-IOS-XR-man-ipsla-cfg',
            'threshold-type',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-man-ipsla-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_ipsla_cfg',
        ),
    },
    'Ipsla.MplsLspMonitor.Reactions.Reaction.Condition.Timeout' : {
        'meta_info' : _MetaInfoClass('Ipsla.MplsLspMonitor.Reactions.Reaction.Condition.Timeout', REFERENCE_CLASS,
            '''React on probe timeout''',
            False, 
            [
            _MetaInfoClassMember('action-type', REFERENCE_CLASS, 'ActionType', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_ipsla_cfg', 'Ipsla.MplsLspMonitor.Reactions.Reaction.Condition.Timeout.ActionType',
                [], [],
                '''                Type of action to be taken on threshold
                violation(s)
                ''',
                'action_type',
                'Cisco-IOS-XR-man-ipsla-cfg', False),
            _MetaInfoClassMember('threshold-type', REFERENCE_CLASS, 'ThresholdType', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_ipsla_cfg', 'Ipsla.MplsLspMonitor.Reactions.Reaction.Condition.Timeout.ThresholdType',
                [], [],
                '''                Type of thresholding to perform on the monitored
                element
                ''',
                'threshold_type',
                'Cisco-IOS-XR-man-ipsla-cfg', False),
            ],
            'Cisco-IOS-XR-man-ipsla-cfg',
            'timeout',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-man-ipsla-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_ipsla_cfg',
            is_presence=True,
        ),
    },
    'Ipsla.MplsLspMonitor.Reactions.Reaction.Condition.LpdGroup.ActionType' : {
        'meta_info' : _MetaInfoClass('Ipsla.MplsLspMonitor.Reactions.Reaction.Condition.LpdGroup.ActionType', REFERENCE_CLASS,
            '''Type of action to be taken on threshold
violation(s)''',
            False, 
            [
            _MetaInfoClassMember('logging', ATTRIBUTE, 'Empty', 'empty',
                None, None,
                [], [],
                '''                Generate a syslog alarm on threshold violation
                ''',
                'logging',
                'Cisco-IOS-XR-man-ipsla-cfg', False),
            ],
            'Cisco-IOS-XR-man-ipsla-cfg',
            'action-type',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-man-ipsla-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_ipsla_cfg',
        ),
    },
    'Ipsla.MplsLspMonitor.Reactions.Reaction.Condition.LpdGroup' : {
        'meta_info' : _MetaInfoClass('Ipsla.MplsLspMonitor.Reactions.Reaction.Condition.LpdGroup', REFERENCE_CLASS,
            '''React on LPD Group violation for a monitored
MPLSLM''',
            False, 
            [
            _MetaInfoClassMember('action-type', REFERENCE_CLASS, 'ActionType', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_ipsla_cfg', 'Ipsla.MplsLspMonitor.Reactions.Reaction.Condition.LpdGroup.ActionType',
                [], [],
                '''                Type of action to be taken on threshold
                violation(s)
                ''',
                'action_type',
                'Cisco-IOS-XR-man-ipsla-cfg', False),
            ],
            'Cisco-IOS-XR-man-ipsla-cfg',
            'lpd-group',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-man-ipsla-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_ipsla_cfg',
            is_presence=True,
        ),
    },
    'Ipsla.MplsLspMonitor.Reactions.Reaction.Condition.ConnectionLoss.ActionType' : {
        'meta_info' : _MetaInfoClass('Ipsla.MplsLspMonitor.Reactions.Reaction.Condition.ConnectionLoss.ActionType', REFERENCE_CLASS,
            '''Type of action to be taken on threshold
violation(s)''',
            False, 
            [
            _MetaInfoClassMember('logging', ATTRIBUTE, 'Empty', 'empty',
                None, None,
                [], [],
                '''                Generate a syslog alarm on threshold violation
                ''',
                'logging',
                'Cisco-IOS-XR-man-ipsla-cfg', False),
            ],
            'Cisco-IOS-XR-man-ipsla-cfg',
            'action-type',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-man-ipsla-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_ipsla_cfg',
        ),
    },
    'Ipsla.MplsLspMonitor.Reactions.Reaction.Condition.ConnectionLoss.ThresholdType' : {
        'meta_info' : _MetaInfoClass('Ipsla.MplsLspMonitor.Reactions.Reaction.Condition.ConnectionLoss.ThresholdType', REFERENCE_CLASS,
            '''Type of thresholding to perform on the monitored
element''',
            False, 
            [
            _MetaInfoClassMember('thresh-type', REFERENCE_ENUM_CLASS, 'IpslaLspMonitorThresholdTypes', 'Ipsla-lsp-monitor-threshold-types',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_ipsla_cfg', 'IpslaLspMonitorThresholdTypes',
                [], [],
                '''                Type of thresholding to perform
                ''',
                'thresh_type',
                'Cisco-IOS-XR-man-ipsla-cfg', False),
            _MetaInfoClassMember('count1', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('1', '16')], [],
                '''                Probe count for consecutive
                ''',
                'count1',
                'Cisco-IOS-XR-man-ipsla-cfg', False, has_when=True),
            _MetaInfoClassMember('count2', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('1', '16')], [],
                '''                Y value, when threshold type is XofY
                ''',
                'count2',
                'Cisco-IOS-XR-man-ipsla-cfg', False, has_when=True),
            ],
            'Cisco-IOS-XR-man-ipsla-cfg',
            'threshold-type',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-man-ipsla-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_ipsla_cfg',
        ),
    },
    'Ipsla.MplsLspMonitor.Reactions.Reaction.Condition.ConnectionLoss' : {
        'meta_info' : _MetaInfoClass('Ipsla.MplsLspMonitor.Reactions.Reaction.Condition.ConnectionLoss', REFERENCE_CLASS,
            '''React on connection loss for a monitored
MPLSLM''',
            False, 
            [
            _MetaInfoClassMember('action-type', REFERENCE_CLASS, 'ActionType', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_ipsla_cfg', 'Ipsla.MplsLspMonitor.Reactions.Reaction.Condition.ConnectionLoss.ActionType',
                [], [],
                '''                Type of action to be taken on threshold
                violation(s)
                ''',
                'action_type',
                'Cisco-IOS-XR-man-ipsla-cfg', False),
            _MetaInfoClassMember('threshold-type', REFERENCE_CLASS, 'ThresholdType', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_ipsla_cfg', 'Ipsla.MplsLspMonitor.Reactions.Reaction.Condition.ConnectionLoss.ThresholdType',
                [], [],
                '''                Type of thresholding to perform on the monitored
                element
                ''',
                'threshold_type',
                'Cisco-IOS-XR-man-ipsla-cfg', False),
            ],
            'Cisco-IOS-XR-man-ipsla-cfg',
            'connection-loss',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-man-ipsla-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_ipsla_cfg',
            is_presence=True,
        ),
    },
    'Ipsla.MplsLspMonitor.Reactions.Reaction.Condition' : {
        'meta_info' : _MetaInfoClass('Ipsla.MplsLspMonitor.Reactions.Reaction.Condition', REFERENCE_CLASS,
            '''Reaction condition specification''',
            False, 
            [
            _MetaInfoClassMember('lpd-tree-trace', REFERENCE_CLASS, 'LpdTreeTrace', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_ipsla_cfg', 'Ipsla.MplsLspMonitor.Reactions.Reaction.Condition.LpdTreeTrace',
                [], [],
                '''                React on LPD Tree Trace violation for a
                monitored MPLSLM
                ''',
                'lpd_tree_trace',
                'Cisco-IOS-XR-man-ipsla-cfg', False, is_presence=True),
            _MetaInfoClassMember('timeout', REFERENCE_CLASS, 'Timeout', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_ipsla_cfg', 'Ipsla.MplsLspMonitor.Reactions.Reaction.Condition.Timeout',
                [], [],
                '''                React on probe timeout
                ''',
                'timeout',
                'Cisco-IOS-XR-man-ipsla-cfg', False, is_presence=True),
            _MetaInfoClassMember('lpd-group', REFERENCE_CLASS, 'LpdGroup', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_ipsla_cfg', 'Ipsla.MplsLspMonitor.Reactions.Reaction.Condition.LpdGroup',
                [], [],
                '''                React on LPD Group violation for a monitored
                MPLSLM
                ''',
                'lpd_group',
                'Cisco-IOS-XR-man-ipsla-cfg', False, is_presence=True),
            _MetaInfoClassMember('connection-loss', REFERENCE_CLASS, 'ConnectionLoss', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_ipsla_cfg', 'Ipsla.MplsLspMonitor.Reactions.Reaction.Condition.ConnectionLoss',
                [], [],
                '''                React on connection loss for a monitored
                MPLSLM
                ''',
                'connection_loss',
                'Cisco-IOS-XR-man-ipsla-cfg', False, is_presence=True),
            ],
            'Cisco-IOS-XR-man-ipsla-cfg',
            'condition',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-man-ipsla-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_ipsla_cfg',
        ),
    },
    'Ipsla.MplsLspMonitor.Reactions.Reaction' : {
        'meta_info' : _MetaInfoClass('Ipsla.MplsLspMonitor.Reactions.Reaction', REFERENCE_LIST,
            '''Reaction configuration for an MPLSLM instance''',
            False, 
            [
            _MetaInfoClassMember('monitor-id', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('1', '2048')], [],
                '''                Monitor identifier
                ''',
                'monitor_id',
                'Cisco-IOS-XR-man-ipsla-cfg', True),
            _MetaInfoClassMember('condition', REFERENCE_CLASS, 'Condition', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_ipsla_cfg', 'Ipsla.MplsLspMonitor.Reactions.Reaction.Condition',
                [], [],
                '''                Reaction condition specification
                ''',
                'condition',
                'Cisco-IOS-XR-man-ipsla-cfg', False),
            ],
            'Cisco-IOS-XR-man-ipsla-cfg',
            'reaction',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-man-ipsla-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_ipsla_cfg',
        ),
    },
    'Ipsla.MplsLspMonitor.Reactions' : {
        'meta_info' : _MetaInfoClass('Ipsla.MplsLspMonitor.Reactions', REFERENCE_CLASS,
            '''MPLSLM Reaction configuration''',
            False, 
            [
            _MetaInfoClassMember('reaction', REFERENCE_LIST, 'Reaction', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_ipsla_cfg', 'Ipsla.MplsLspMonitor.Reactions.Reaction',
                [], [],
                '''                Reaction configuration for an MPLSLM instance
                ''',
                'reaction',
                'Cisco-IOS-XR-man-ipsla-cfg', False),
            ],
            'Cisco-IOS-XR-man-ipsla-cfg',
            'reactions',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-man-ipsla-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_ipsla_cfg',
        ),
    },
    'Ipsla.MplsLspMonitor.Schedules.Schedule.StartTime' : {
        'meta_info' : _MetaInfoClass('Ipsla.MplsLspMonitor.Schedules.Schedule.StartTime', REFERENCE_CLASS,
            '''Start time of MPLSLM instance''',
            False, 
            [
            _MetaInfoClassMember('schedule-type', REFERENCE_ENUM_CLASS, 'IpslaSched', 'Ipsla-sched',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_ipsla_cfg', 'IpslaSched',
                [], [],
                '''                Type of schedule
                ''',
                'schedule_type',
                'Cisco-IOS-XR-man-ipsla-cfg', False),
            _MetaInfoClassMember('hour', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('0', '23')], [],
                '''                Hour value(hh) in hh:mm:ss specification
                ''',
                'hour',
                'Cisco-IOS-XR-man-ipsla-cfg', False, has_when=True),
            _MetaInfoClassMember('minute', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('0', '59')], [],
                '''                Minute value(mm) in hh:mm:ss specification
                ''',
                'minute',
                'Cisco-IOS-XR-man-ipsla-cfg', False, has_when=True),
            _MetaInfoClassMember('second', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('0', '59')], [],
                '''                Second value(ss) in hh:mm:ss specification
                ''',
                'second',
                'Cisco-IOS-XR-man-ipsla-cfg', False, has_when=True),
            _MetaInfoClassMember('month', REFERENCE_ENUM_CLASS, 'IpslaMonth', 'Ipsla-month',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_ipsla_cfg', 'IpslaMonth',
                [], [],
                '''                Month of the year (optional. Default current
                month)
                ''',
                'month',
                'Cisco-IOS-XR-man-ipsla-cfg', False, has_when=True),
            _MetaInfoClassMember('day', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('1', '31')], [],
                '''                Day of the month(optional. Default today)
                ''',
                'day',
                'Cisco-IOS-XR-man-ipsla-cfg', False, has_when=True),
            _MetaInfoClassMember('year', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('1993', '2035')], [],
                '''                Year (optional. Default current year)
                ''',
                'year',
                'Cisco-IOS-XR-man-ipsla-cfg', False, has_when=True),
            ],
            'Cisco-IOS-XR-man-ipsla-cfg',
            'start-time',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-man-ipsla-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_ipsla_cfg',
        ),
    },
    'Ipsla.MplsLspMonitor.Schedules.Schedule' : {
        'meta_info' : _MetaInfoClass('Ipsla.MplsLspMonitor.Schedules.Schedule', REFERENCE_LIST,
            '''Schedule an MPLSLM instance''',
            False, 
            [
            _MetaInfoClassMember('monitor-id', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('1', '2048')], [],
                '''                Monitor indentifier
                ''',
                'monitor_id',
                'Cisco-IOS-XR-man-ipsla-cfg', True),
            _MetaInfoClassMember('start-time', REFERENCE_CLASS, 'StartTime', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_ipsla_cfg', 'Ipsla.MplsLspMonitor.Schedules.Schedule.StartTime',
                [], [],
                '''                Start time of MPLSLM instance
                ''',
                'start_time',
                'Cisco-IOS-XR-man-ipsla-cfg', False),
            _MetaInfoClassMember('frequency', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('1', '604800')], [],
                '''                Group schedule frequency of the probing
                ''',
                'frequency',
                'Cisco-IOS-XR-man-ipsla-cfg', False),
            _MetaInfoClassMember('period', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('1', '604800')], [],
                '''                Group schedule period range
                ''',
                'period',
                'Cisco-IOS-XR-man-ipsla-cfg', False),
            ],
            'Cisco-IOS-XR-man-ipsla-cfg',
            'schedule',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-man-ipsla-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_ipsla_cfg',
        ),
    },
    'Ipsla.MplsLspMonitor.Schedules' : {
        'meta_info' : _MetaInfoClass('Ipsla.MplsLspMonitor.Schedules', REFERENCE_CLASS,
            '''MPLSLM schedule configuration''',
            False, 
            [
            _MetaInfoClassMember('schedule', REFERENCE_LIST, 'Schedule', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_ipsla_cfg', 'Ipsla.MplsLspMonitor.Schedules.Schedule',
                [], [],
                '''                Schedule an MPLSLM instance
                ''',
                'schedule',
                'Cisco-IOS-XR-man-ipsla-cfg', False),
            ],
            'Cisco-IOS-XR-man-ipsla-cfg',
            'schedules',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-man-ipsla-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_ipsla_cfg',
        ),
    },
    'Ipsla.MplsLspMonitor.Definitions.Definition.OperationType.MplsLspTrace.Reply' : {
        'meta_info' : _MetaInfoClass('Ipsla.MplsLspMonitor.Definitions.Definition.OperationType.MplsLspTrace.Reply', REFERENCE_CLASS,
            '''Echo reply options for the MPLS LSP operation''',
            False, 
            [
            _MetaInfoClassMember('dscp-bits', REFERENCE_UNION, 'str', 'Ipsla-lsp-reply-dscp',
                None, None,
                [], [],
                '''                DSCP bits in the reply IP header
                ''',
                'dscp_bits',
                'Cisco-IOS-XR-man-ipsla-cfg', False, [
                    _MetaInfoClassMember('dscp-bits', REFERENCE_ENUM_CLASS, 'IpslaLspReplyDscp', 'enumeration',
                        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_ipsla_cfg', 'IpslaLspReplyDscp',
                        [], [],
                        '''                        DSCP bits in the reply IP header
                        ''',
                        'dscp_bits',
                        'Cisco-IOS-XR-man-ipsla-cfg', False),
                    _MetaInfoClassMember('dscp-bits', ATTRIBUTE, 'int', 'uint32',
                        None, None,
                        [('0', '63')], [],
                        '''                        DSCP bits in the reply IP header
                        ''',
                        'dscp_bits',
                        'Cisco-IOS-XR-man-ipsla-cfg', False),
                ]),
            _MetaInfoClassMember('mode', REFERENCE_ENUM_CLASS, 'IpslaLspMonitorReplyMode', 'Ipsla-lsp-monitor-reply-mode',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_ipsla_cfg', 'IpslaLspMonitorReplyMode',
                [], [],
                '''                Enables use of router alert in echo reply
                packets
                ''',
                'mode',
                'Cisco-IOS-XR-man-ipsla-cfg', False),
            ],
            'Cisco-IOS-XR-man-ipsla-cfg',
            'reply',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-man-ipsla-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_ipsla_cfg',
        ),
    },
    'Ipsla.MplsLspMonitor.Definitions.Definition.OperationType.MplsLspTrace.Statistics' : {
        'meta_info' : _MetaInfoClass('Ipsla.MplsLspMonitor.Definitions.Definition.OperationType.MplsLspTrace.Statistics', REFERENCE_CLASS,
            '''Statistics collection aggregated over an hour''',
            False, 
            [
            _MetaInfoClassMember('hours', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('0', '2')], [],
                '''                Number of hours for which hourly statistics are
                kept
                ''',
                'hours',
                'Cisco-IOS-XR-man-ipsla-cfg', False, default_value="2"),
            ],
            'Cisco-IOS-XR-man-ipsla-cfg',
            'statistics',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-man-ipsla-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_ipsla_cfg',
        ),
    },
    'Ipsla.MplsLspMonitor.Definitions.Definition.OperationType.MplsLspTrace.Scan' : {
        'meta_info' : _MetaInfoClass('Ipsla.MplsLspMonitor.Definitions.Definition.OperationType.MplsLspTrace.Scan', REFERENCE_CLASS,
            '''Scanning parameters configuration''',
            False, 
            [
            _MetaInfoClassMember('interval', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('1', '70560')], [],
                '''                Time interval for automatic discovery
                ''',
                'interval',
                'Cisco-IOS-XR-man-ipsla-cfg', False, default_value="240"),
            _MetaInfoClassMember('delete-factor', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('0', '2147483647')], [],
                '''                Number of times for automatic deletion
                ''',
                'delete_factor',
                'Cisco-IOS-XR-man-ipsla-cfg', False, default_value="1"),
            ],
            'Cisco-IOS-XR-man-ipsla-cfg',
            'scan',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-man-ipsla-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_ipsla_cfg',
        ),
    },
    'Ipsla.MplsLspMonitor.Definitions.Definition.OperationType.MplsLspTrace' : {
        'meta_info' : _MetaInfoClass('Ipsla.MplsLspMonitor.Definitions.Definition.OperationType.MplsLspTrace', REFERENCE_CLASS,
            '''Perform MPLS LSP Trace operation''',
            False, 
            [
            _MetaInfoClassMember('ttl', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('1', '255')], [],
                '''                Time to live value
                ''',
                'ttl',
                'Cisco-IOS-XR-man-ipsla-cfg', False, default_value="30"),
            _MetaInfoClassMember('exp-bits', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('0', '7')], [],
                '''                EXP bits in MPLS LSP echo request header
                ''',
                'exp_bits',
                'Cisco-IOS-XR-man-ipsla-cfg', False, default_value="0"),
            _MetaInfoClassMember('reply', REFERENCE_CLASS, 'Reply', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_ipsla_cfg', 'Ipsla.MplsLspMonitor.Definitions.Definition.OperationType.MplsLspTrace.Reply',
                [], [],
                '''                Echo reply options for the MPLS LSP operation
                ''',
                'reply',
                'Cisco-IOS-XR-man-ipsla-cfg', False),
            _MetaInfoClassMember('tag', ATTRIBUTE, 'str', 'string',
                None, None,
                [(1, 100)], [],
                '''                Add a tag for this MPLSLM instance
                ''',
                'tag',
                'Cisco-IOS-XR-man-ipsla-cfg', False),
            _MetaInfoClassMember('lsp-selector', ATTRIBUTE, 'str', 'inet:ipv4-address-no-zone',
                None, None,
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'],
                '''                Attributes used for path selection during LSP
                load balancing
                ''',
                'lsp_selector',
                'Cisco-IOS-XR-man-ipsla-cfg', False, default_value="'1.0.0.127'"),
            _MetaInfoClassMember('output-interface', ATTRIBUTE, 'str', 'xr:Interface-name',
                None, None,
                [], [b'[a-zA-Z0-9._/-]+'],
                '''                Echo request output interface
                ''',
                'output_interface',
                'Cisco-IOS-XR-man-ipsla-cfg', False),
            _MetaInfoClassMember('accesslist', ATTRIBUTE, 'str', 'xr:Cisco-ios-xr-string',
                None, None,
                [(1, 32)], [],
                '''                Apply access list to filter PE addresses
                ''',
                'accesslist',
                'Cisco-IOS-XR-man-ipsla-cfg', False),
            _MetaInfoClassMember('output-nexthop', ATTRIBUTE, 'str', 'inet:ipv4-address-no-zone',
                None, None,
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'],
                '''                Echo request output nexthop
                ''',
                'output_nexthop',
                'Cisco-IOS-XR-man-ipsla-cfg', False),
            _MetaInfoClassMember('statistics', REFERENCE_CLASS, 'Statistics', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_ipsla_cfg', 'Ipsla.MplsLspMonitor.Definitions.Definition.OperationType.MplsLspTrace.Statistics',
                [], [],
                '''                Statistics collection aggregated over an hour
                ''',
                'statistics',
                'Cisco-IOS-XR-man-ipsla-cfg', False),
            _MetaInfoClassMember('timeout', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('1', '604800000')], [],
                '''                Probe/Control timeout in milliseconds
                ''',
                'timeout',
                'Cisco-IOS-XR-man-ipsla-cfg', False, default_value="5000"),
            _MetaInfoClassMember('force-explicit-null', ATTRIBUTE, 'Empty', 'empty',
                None, None,
                [], [],
                '''                Forced option for the MPLS LSP operation
                ''',
                'force_explicit_null',
                'Cisco-IOS-XR-man-ipsla-cfg', False),
            _MetaInfoClassMember('scan', REFERENCE_CLASS, 'Scan', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_ipsla_cfg', 'Ipsla.MplsLspMonitor.Definitions.Definition.OperationType.MplsLspTrace.Scan',
                [], [],
                '''                Scanning parameters configuration
                ''',
                'scan',
                'Cisco-IOS-XR-man-ipsla-cfg', False),
            _MetaInfoClassMember('vrf', ATTRIBUTE, 'str', 'xr:Cisco-ios-xr-string',
                None, None,
                [(1, 32)], [],
                '''                Specify a VRF instance to be monitored
                ''',
                'vrf',
                'Cisco-IOS-XR-man-ipsla-cfg', False),
            ],
            'Cisco-IOS-XR-man-ipsla-cfg',
            'mpls-lsp-trace',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-man-ipsla-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_ipsla_cfg',
            is_presence=True,
        ),
    },
    'Ipsla.MplsLspMonitor.Definitions.Definition.OperationType.MplsLspPing.DataSize' : {
        'meta_info' : _MetaInfoClass('Ipsla.MplsLspMonitor.Definitions.Definition.OperationType.MplsLspPing.DataSize', REFERENCE_CLASS,
            '''Protocol data size in payload of probe
packets''',
            False, 
            [
            _MetaInfoClassMember('request', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('100', '17986')], [],
                '''                Payload size in request probe packet
                ''',
                'request',
                'Cisco-IOS-XR-man-ipsla-cfg', False, default_value="100"),
            ],
            'Cisco-IOS-XR-man-ipsla-cfg',
            'data-size',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-man-ipsla-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_ipsla_cfg',
        ),
    },
    'Ipsla.MplsLspMonitor.Definitions.Definition.OperationType.MplsLspPing.PathDiscover.Session' : {
        'meta_info' : _MetaInfoClass('Ipsla.MplsLspMonitor.Definitions.Definition.OperationType.MplsLspPing.PathDiscover.Session', REFERENCE_CLASS,
            '''Session parameters configuration''',
            False, 
            [
            _MetaInfoClassMember('timeout', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('1', '900')], [],
                '''                Timeout value for path discovery request
                ''',
                'timeout',
                'Cisco-IOS-XR-man-ipsla-cfg', False, default_value="120"),
            _MetaInfoClassMember('limit', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('1', '15')], [],
                '''                Number of concurrent active path
                discovery requests at one time
                ''',
                'limit',
                'Cisco-IOS-XR-man-ipsla-cfg', False, default_value="1"),
            ],
            'Cisco-IOS-XR-man-ipsla-cfg',
            'session',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-man-ipsla-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_ipsla_cfg',
        ),
    },
    'Ipsla.MplsLspMonitor.Definitions.Definition.OperationType.MplsLspPing.PathDiscover.Path.SecondaryFrequency' : {
        'meta_info' : _MetaInfoClass('Ipsla.MplsLspMonitor.Definitions.Definition.OperationType.MplsLspPing.PathDiscover.Path.SecondaryFrequency', REFERENCE_CLASS,
            '''Frequency to be used if path failure
condition is detected''',
            False, 
            [
            _MetaInfoClassMember('type', REFERENCE_ENUM_CLASS, 'IpslaSecondaryFrequency', 'Ipsla-secondary-frequency',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_ipsla_cfg', 'IpslaSecondaryFrequency',
                [], [],
                '''                Condition type of path failure
                ''',
                'type',
                'Cisco-IOS-XR-man-ipsla-cfg', False, is_mandatory=True),
            _MetaInfoClassMember('frequency', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('1', '604800')], [],
                '''                Frequency value in seconds
                ''',
                'frequency',
                'Cisco-IOS-XR-man-ipsla-cfg', False, is_mandatory=True),
            ],
            'Cisco-IOS-XR-man-ipsla-cfg',
            'secondary-frequency',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-man-ipsla-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_ipsla_cfg',
            is_presence=True,
        ),
    },
    'Ipsla.MplsLspMonitor.Definitions.Definition.OperationType.MplsLspPing.PathDiscover.Path' : {
        'meta_info' : _MetaInfoClass('Ipsla.MplsLspMonitor.Definitions.Definition.OperationType.MplsLspPing.PathDiscover.Path', REFERENCE_CLASS,
            '''Path parameters configuration''',
            False, 
            [
            _MetaInfoClassMember('secondary-frequency', REFERENCE_CLASS, 'SecondaryFrequency', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_ipsla_cfg', 'Ipsla.MplsLspMonitor.Definitions.Definition.OperationType.MplsLspPing.PathDiscover.Path.SecondaryFrequency',
                [], [],
                '''                Frequency to be used if path failure
                condition is detected
                ''',
                'secondary_frequency',
                'Cisco-IOS-XR-man-ipsla-cfg', False, is_presence=True),
            _MetaInfoClassMember('retry', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('1', '16')], [],
                '''                Number of attempts before declaring the
                path as down
                ''',
                'retry',
                'Cisco-IOS-XR-man-ipsla-cfg', False, default_value="1"),
            ],
            'Cisco-IOS-XR-man-ipsla-cfg',
            'path',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-man-ipsla-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_ipsla_cfg',
        ),
    },
    'Ipsla.MplsLspMonitor.Definitions.Definition.OperationType.MplsLspPing.PathDiscover.Echo.Multipath' : {
        'meta_info' : _MetaInfoClass('Ipsla.MplsLspMonitor.Definitions.Definition.OperationType.MplsLspPing.PathDiscover.Echo.Multipath', REFERENCE_CLASS,
            '''Downstream map multipath settings''',
            False, 
            [
            _MetaInfoClassMember('bitmap-size', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('1', '256')], [],
                '''                Multipath bit size
                ''',
                'bitmap_size',
                'Cisco-IOS-XR-man-ipsla-cfg', False, default_value="32"),
            ],
            'Cisco-IOS-XR-man-ipsla-cfg',
            'multipath',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-man-ipsla-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_ipsla_cfg',
        ),
    },
    'Ipsla.MplsLspMonitor.Definitions.Definition.OperationType.MplsLspPing.PathDiscover.Echo' : {
        'meta_info' : _MetaInfoClass('Ipsla.MplsLspMonitor.Definitions.Definition.OperationType.MplsLspPing.PathDiscover.Echo', REFERENCE_CLASS,
            '''Echo parameters configuration''',
            False, 
            [
            _MetaInfoClassMember('multipath', REFERENCE_CLASS, 'Multipath', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_ipsla_cfg', 'Ipsla.MplsLspMonitor.Definitions.Definition.OperationType.MplsLspPing.PathDiscover.Echo.Multipath',
                [], [],
                '''                Downstream map multipath settings
                ''',
                'multipath',
                'Cisco-IOS-XR-man-ipsla-cfg', False),
            _MetaInfoClassMember('interval', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('0', '3600000')], [],
                '''                Send interval between echo requests
                during path discovery
                ''',
                'interval',
                'Cisco-IOS-XR-man-ipsla-cfg', False, default_value="0"),
            _MetaInfoClassMember('timeout', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('1', '3600')], [],
                '''                Timeout value for echo requests during
                path discovery
                ''',
                'timeout',
                'Cisco-IOS-XR-man-ipsla-cfg', False, default_value="5"),
            _MetaInfoClassMember('retry', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('0', '10')], [],
                '''                Number of timeout retry attempts during
                path discovery
                ''',
                'retry',
                'Cisco-IOS-XR-man-ipsla-cfg', False, default_value="3"),
            _MetaInfoClassMember('maximum-lsp-selector', ATTRIBUTE, 'str', 'inet:ipv4-address-no-zone',
                None, None,
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'],
                '''                Maximum IPv4 address used as destination
                in echo request
                ''',
                'maximum_lsp_selector',
                'Cisco-IOS-XR-man-ipsla-cfg', False, default_value="'127.255.255.255'"),
            ],
            'Cisco-IOS-XR-man-ipsla-cfg',
            'echo',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-man-ipsla-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_ipsla_cfg',
        ),
    },
    'Ipsla.MplsLspMonitor.Definitions.Definition.OperationType.MplsLspPing.PathDiscover' : {
        'meta_info' : _MetaInfoClass('Ipsla.MplsLspMonitor.Definitions.Definition.OperationType.MplsLspPing.PathDiscover', REFERENCE_CLASS,
            '''Path discover configuration''',
            False, 
            [
            _MetaInfoClassMember('session', REFERENCE_CLASS, 'Session', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_ipsla_cfg', 'Ipsla.MplsLspMonitor.Definitions.Definition.OperationType.MplsLspPing.PathDiscover.Session',
                [], [],
                '''                Session parameters configuration
                ''',
                'session',
                'Cisco-IOS-XR-man-ipsla-cfg', False),
            _MetaInfoClassMember('path', REFERENCE_CLASS, 'Path', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_ipsla_cfg', 'Ipsla.MplsLspMonitor.Definitions.Definition.OperationType.MplsLspPing.PathDiscover.Path',
                [], [],
                '''                Path parameters configuration
                ''',
                'path',
                'Cisco-IOS-XR-man-ipsla-cfg', False),
            _MetaInfoClassMember('echo', REFERENCE_CLASS, 'Echo', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_ipsla_cfg', 'Ipsla.MplsLspMonitor.Definitions.Definition.OperationType.MplsLspPing.PathDiscover.Echo',
                [], [],
                '''                Echo parameters configuration
                ''',
                'echo',
                'Cisco-IOS-XR-man-ipsla-cfg', False),
            _MetaInfoClassMember('scan-period', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('0', '7200')], [],
                '''                Time period for finishing path discovery
                ''',
                'scan_period',
                'Cisco-IOS-XR-man-ipsla-cfg', False, default_value="0"),
            ],
            'Cisco-IOS-XR-man-ipsla-cfg',
            'path-discover',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-man-ipsla-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_ipsla_cfg',
            is_presence=True,
        ),
    },
    'Ipsla.MplsLspMonitor.Definitions.Definition.OperationType.MplsLspPing.Reply' : {
        'meta_info' : _MetaInfoClass('Ipsla.MplsLspMonitor.Definitions.Definition.OperationType.MplsLspPing.Reply', REFERENCE_CLASS,
            '''Echo reply options for the MPLS LSP operation''',
            False, 
            [
            _MetaInfoClassMember('dscp-bits', REFERENCE_UNION, 'str', 'Ipsla-lsp-reply-dscp',
                None, None,
                [], [],
                '''                DSCP bits in the reply IP header
                ''',
                'dscp_bits',
                'Cisco-IOS-XR-man-ipsla-cfg', False, [
                    _MetaInfoClassMember('dscp-bits', REFERENCE_ENUM_CLASS, 'IpslaLspReplyDscp', 'enumeration',
                        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_ipsla_cfg', 'IpslaLspReplyDscp',
                        [], [],
                        '''                        DSCP bits in the reply IP header
                        ''',
                        'dscp_bits',
                        'Cisco-IOS-XR-man-ipsla-cfg', False),
                    _MetaInfoClassMember('dscp-bits', ATTRIBUTE, 'int', 'uint32',
                        None, None,
                        [('0', '63')], [],
                        '''                        DSCP bits in the reply IP header
                        ''',
                        'dscp_bits',
                        'Cisco-IOS-XR-man-ipsla-cfg', False),
                ]),
            _MetaInfoClassMember('mode', REFERENCE_ENUM_CLASS, 'IpslaLspMonitorReplyMode', 'Ipsla-lsp-monitor-reply-mode',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_ipsla_cfg', 'IpslaLspMonitorReplyMode',
                [], [],
                '''                Enables use of router alert in echo reply
                packets
                ''',
                'mode',
                'Cisco-IOS-XR-man-ipsla-cfg', False),
            ],
            'Cisco-IOS-XR-man-ipsla-cfg',
            'reply',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-man-ipsla-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_ipsla_cfg',
        ),
    },
    'Ipsla.MplsLspMonitor.Definitions.Definition.OperationType.MplsLspPing.Statistics' : {
        'meta_info' : _MetaInfoClass('Ipsla.MplsLspMonitor.Definitions.Definition.OperationType.MplsLspPing.Statistics', REFERENCE_CLASS,
            '''Statistics collection aggregated over an hour''',
            False, 
            [
            _MetaInfoClassMember('hours', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('0', '2')], [],
                '''                Number of hours for which hourly statistics are
                kept
                ''',
                'hours',
                'Cisco-IOS-XR-man-ipsla-cfg', False, default_value="2"),
            ],
            'Cisco-IOS-XR-man-ipsla-cfg',
            'statistics',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-man-ipsla-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_ipsla_cfg',
        ),
    },
    'Ipsla.MplsLspMonitor.Definitions.Definition.OperationType.MplsLspPing.Scan' : {
        'meta_info' : _MetaInfoClass('Ipsla.MplsLspMonitor.Definitions.Definition.OperationType.MplsLspPing.Scan', REFERENCE_CLASS,
            '''Scanning parameters configuration''',
            False, 
            [
            _MetaInfoClassMember('interval', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('1', '70560')], [],
                '''                Time interval for automatic discovery
                ''',
                'interval',
                'Cisco-IOS-XR-man-ipsla-cfg', False, default_value="240"),
            _MetaInfoClassMember('delete-factor', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('0', '2147483647')], [],
                '''                Number of times for automatic deletion
                ''',
                'delete_factor',
                'Cisco-IOS-XR-man-ipsla-cfg', False, default_value="1"),
            ],
            'Cisco-IOS-XR-man-ipsla-cfg',
            'scan',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-man-ipsla-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_ipsla_cfg',
        ),
    },
    'Ipsla.MplsLspMonitor.Definitions.Definition.OperationType.MplsLspPing' : {
        'meta_info' : _MetaInfoClass('Ipsla.MplsLspMonitor.Definitions.Definition.OperationType.MplsLspPing', REFERENCE_CLASS,
            '''Perform MPLS LSP Ping operation''',
            False, 
            [
            _MetaInfoClassMember('data-size', REFERENCE_CLASS, 'DataSize', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_ipsla_cfg', 'Ipsla.MplsLspMonitor.Definitions.Definition.OperationType.MplsLspPing.DataSize',
                [], [],
                '''                Protocol data size in payload of probe
                packets
                ''',
                'data_size',
                'Cisco-IOS-XR-man-ipsla-cfg', False),
            _MetaInfoClassMember('path-discover', REFERENCE_CLASS, 'PathDiscover', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_ipsla_cfg', 'Ipsla.MplsLspMonitor.Definitions.Definition.OperationType.MplsLspPing.PathDiscover',
                [], [],
                '''                Path discover configuration
                ''',
                'path_discover',
                'Cisco-IOS-XR-man-ipsla-cfg', False, is_presence=True),
            _MetaInfoClassMember('ttl', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('1', '255')], [],
                '''                Time to live value
                ''',
                'ttl',
                'Cisco-IOS-XR-man-ipsla-cfg', False, default_value="255"),
            _MetaInfoClassMember('exp-bits', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('0', '7')], [],
                '''                EXP bits in MPLS LSP echo request header
                ''',
                'exp_bits',
                'Cisco-IOS-XR-man-ipsla-cfg', False, default_value="0"),
            _MetaInfoClassMember('reply', REFERENCE_CLASS, 'Reply', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_ipsla_cfg', 'Ipsla.MplsLspMonitor.Definitions.Definition.OperationType.MplsLspPing.Reply',
                [], [],
                '''                Echo reply options for the MPLS LSP operation
                ''',
                'reply',
                'Cisco-IOS-XR-man-ipsla-cfg', False),
            _MetaInfoClassMember('tag', ATTRIBUTE, 'str', 'string',
                None, None,
                [(1, 100)], [],
                '''                Add a tag for this MPLSLM instance
                ''',
                'tag',
                'Cisco-IOS-XR-man-ipsla-cfg', False),
            _MetaInfoClassMember('lsp-selector', ATTRIBUTE, 'str', 'inet:ipv4-address-no-zone',
                None, None,
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'],
                '''                Attributes used for path selection during LSP
                load balancing
                ''',
                'lsp_selector',
                'Cisco-IOS-XR-man-ipsla-cfg', False, default_value="'1.0.0.127'"),
            _MetaInfoClassMember('output-interface', ATTRIBUTE, 'str', 'xr:Interface-name',
                None, None,
                [], [b'[a-zA-Z0-9._/-]+'],
                '''                Echo request output interface
                ''',
                'output_interface',
                'Cisco-IOS-XR-man-ipsla-cfg', False),
            _MetaInfoClassMember('accesslist', ATTRIBUTE, 'str', 'xr:Cisco-ios-xr-string',
                None, None,
                [(1, 32)], [],
                '''                Apply access list to filter PE addresses
                ''',
                'accesslist',
                'Cisco-IOS-XR-man-ipsla-cfg', False),
            _MetaInfoClassMember('output-nexthop', ATTRIBUTE, 'str', 'inet:ipv4-address-no-zone',
                None, None,
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'],
                '''                Echo request output nexthop
                ''',
                'output_nexthop',
                'Cisco-IOS-XR-man-ipsla-cfg', False),
            _MetaInfoClassMember('statistics', REFERENCE_CLASS, 'Statistics', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_ipsla_cfg', 'Ipsla.MplsLspMonitor.Definitions.Definition.OperationType.MplsLspPing.Statistics',
                [], [],
                '''                Statistics collection aggregated over an hour
                ''',
                'statistics',
                'Cisco-IOS-XR-man-ipsla-cfg', False),
            _MetaInfoClassMember('timeout', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('1', '604800000')], [],
                '''                Probe/Control timeout in milliseconds
                ''',
                'timeout',
                'Cisco-IOS-XR-man-ipsla-cfg', False, default_value="5000"),
            _MetaInfoClassMember('force-explicit-null', ATTRIBUTE, 'Empty', 'empty',
                None, None,
                [], [],
                '''                Forced option for the MPLS LSP operation
                ''',
                'force_explicit_null',
                'Cisco-IOS-XR-man-ipsla-cfg', False),
            _MetaInfoClassMember('scan', REFERENCE_CLASS, 'Scan', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_ipsla_cfg', 'Ipsla.MplsLspMonitor.Definitions.Definition.OperationType.MplsLspPing.Scan',
                [], [],
                '''                Scanning parameters configuration
                ''',
                'scan',
                'Cisco-IOS-XR-man-ipsla-cfg', False),
            _MetaInfoClassMember('vrf', ATTRIBUTE, 'str', 'xr:Cisco-ios-xr-string',
                None, None,
                [(1, 32)], [],
                '''                Specify a VRF instance to be monitored
                ''',
                'vrf',
                'Cisco-IOS-XR-man-ipsla-cfg', False),
            ],
            'Cisco-IOS-XR-man-ipsla-cfg',
            'mpls-lsp-ping',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-man-ipsla-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_ipsla_cfg',
            is_presence=True,
        ),
    },
    'Ipsla.MplsLspMonitor.Definitions.Definition.OperationType' : {
        'meta_info' : _MetaInfoClass('Ipsla.MplsLspMonitor.Definitions.Definition.OperationType', REFERENCE_CLASS,
            '''Operation type specification''',
            False, 
            [
            _MetaInfoClassMember('mpls-lsp-trace', REFERENCE_CLASS, 'MplsLspTrace', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_ipsla_cfg', 'Ipsla.MplsLspMonitor.Definitions.Definition.OperationType.MplsLspTrace',
                [], [],
                '''                Perform MPLS LSP Trace operation
                ''',
                'mpls_lsp_trace',
                'Cisco-IOS-XR-man-ipsla-cfg', False, is_presence=True),
            _MetaInfoClassMember('mpls-lsp-ping', REFERENCE_CLASS, 'MplsLspPing', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_ipsla_cfg', 'Ipsla.MplsLspMonitor.Definitions.Definition.OperationType.MplsLspPing',
                [], [],
                '''                Perform MPLS LSP Ping operation
                ''',
                'mpls_lsp_ping',
                'Cisco-IOS-XR-man-ipsla-cfg', False, is_presence=True),
            ],
            'Cisco-IOS-XR-man-ipsla-cfg',
            'operation-type',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-man-ipsla-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_ipsla_cfg',
        ),
    },
    'Ipsla.MplsLspMonitor.Definitions.Definition' : {
        'meta_info' : _MetaInfoClass('Ipsla.MplsLspMonitor.Definitions.Definition', REFERENCE_LIST,
            '''MPLS LSP Monitor definition''',
            False, 
            [
            _MetaInfoClassMember('monitor-id', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('1', '2048')], [],
                '''                Monitor identifier
                ''',
                'monitor_id',
                'Cisco-IOS-XR-man-ipsla-cfg', True),
            _MetaInfoClassMember('operation-type', REFERENCE_CLASS, 'OperationType', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_ipsla_cfg', 'Ipsla.MplsLspMonitor.Definitions.Definition.OperationType',
                [], [],
                '''                Operation type specification
                ''',
                'operation_type',
                'Cisco-IOS-XR-man-ipsla-cfg', False),
            ],
            'Cisco-IOS-XR-man-ipsla-cfg',
            'definition',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-man-ipsla-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_ipsla_cfg',
        ),
    },
    'Ipsla.MplsLspMonitor.Definitions' : {
        'meta_info' : _MetaInfoClass('Ipsla.MplsLspMonitor.Definitions', REFERENCE_CLASS,
            '''MPLS LSP Monitor definition table''',
            False, 
            [
            _MetaInfoClassMember('definition', REFERENCE_LIST, 'Definition', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_ipsla_cfg', 'Ipsla.MplsLspMonitor.Definitions.Definition',
                [], [],
                '''                MPLS LSP Monitor definition
                ''',
                'definition',
                'Cisco-IOS-XR-man-ipsla-cfg', False),
            ],
            'Cisco-IOS-XR-man-ipsla-cfg',
            'definitions',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-man-ipsla-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_ipsla_cfg',
        ),
    },
    'Ipsla.MplsLspMonitor' : {
        'meta_info' : _MetaInfoClass('Ipsla.MplsLspMonitor', REFERENCE_CLASS,
            '''MPLS LSP Monitor(MPLSLM) configuration''',
            False, 
            [
            _MetaInfoClassMember('reactions', REFERENCE_CLASS, 'Reactions', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_ipsla_cfg', 'Ipsla.MplsLspMonitor.Reactions',
                [], [],
                '''                MPLSLM Reaction configuration
                ''',
                'reactions',
                'Cisco-IOS-XR-man-ipsla-cfg', False),
            _MetaInfoClassMember('schedules', REFERENCE_CLASS, 'Schedules', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_ipsla_cfg', 'Ipsla.MplsLspMonitor.Schedules',
                [], [],
                '''                MPLSLM schedule configuration
                ''',
                'schedules',
                'Cisco-IOS-XR-man-ipsla-cfg', False),
            _MetaInfoClassMember('definitions', REFERENCE_CLASS, 'Definitions', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_ipsla_cfg', 'Ipsla.MplsLspMonitor.Definitions',
                [], [],
                '''                MPLS LSP Monitor definition table
                ''',
                'definitions',
                'Cisco-IOS-XR-man-ipsla-cfg', False),
            ],
            'Cisco-IOS-XR-man-ipsla-cfg',
            'mpls-lsp-monitor',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-man-ipsla-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_ipsla_cfg',
        ),
    },
    'Ipsla.Operation.Schedules.Schedule.StartTime' : {
        'meta_info' : _MetaInfoClass('Ipsla.Operation.Schedules.Schedule.StartTime', REFERENCE_CLASS,
            '''Start time of the operation''',
            False, 
            [
            _MetaInfoClassMember('schedule-type', REFERENCE_ENUM_CLASS, 'IpslaSched', 'Ipsla-sched',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_ipsla_cfg', 'IpslaSched',
                [], [],
                '''                Type of schedule
                ''',
                'schedule_type',
                'Cisco-IOS-XR-man-ipsla-cfg', False),
            _MetaInfoClassMember('hour', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('0', '23')], [],
                '''                Hour value(hh) in hh:mm:ss specification
                ''',
                'hour',
                'Cisco-IOS-XR-man-ipsla-cfg', False, has_when=True),
            _MetaInfoClassMember('minute', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('0', '59')], [],
                '''                Minute value(mm) in hh:mm:ss specification
                ''',
                'minute',
                'Cisco-IOS-XR-man-ipsla-cfg', False, has_when=True),
            _MetaInfoClassMember('second', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('0', '59')], [],
                '''                Second value(ss) in hh:mm:ss specification
                ''',
                'second',
                'Cisco-IOS-XR-man-ipsla-cfg', False, has_when=True),
            _MetaInfoClassMember('month', REFERENCE_ENUM_CLASS, 'IpslaMonth', 'Ipsla-month',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_ipsla_cfg', 'IpslaMonth',
                [], [],
                '''                Month of the year (optional. Default current
                month)
                ''',
                'month',
                'Cisco-IOS-XR-man-ipsla-cfg', False, has_when=True),
            _MetaInfoClassMember('day', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('1', '31')], [],
                '''                Day of the month(optional. Default today)
                ''',
                'day',
                'Cisco-IOS-XR-man-ipsla-cfg', False, has_when=True),
            _MetaInfoClassMember('year', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('1993', '2035')], [],
                '''                Year(optional. Default current year)
                ''',
                'year',
                'Cisco-IOS-XR-man-ipsla-cfg', False, has_when=True),
            ],
            'Cisco-IOS-XR-man-ipsla-cfg',
            'start-time',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-man-ipsla-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_ipsla_cfg',
        ),
    },
    'Ipsla.Operation.Schedules.Schedule' : {
        'meta_info' : _MetaInfoClass('Ipsla.Operation.Schedules.Schedule', REFERENCE_LIST,
            '''Operation schedule configuration''',
            False, 
            [
            _MetaInfoClassMember('operation-id', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('1', '2048')], [],
                '''                Operation number
                ''',
                'operation_id',
                'Cisco-IOS-XR-man-ipsla-cfg', True),
            _MetaInfoClassMember('start-time', REFERENCE_CLASS, 'StartTime', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_ipsla_cfg', 'Ipsla.Operation.Schedules.Schedule.StartTime',
                [], [],
                '''                Start time of the operation
                ''',
                'start_time',
                'Cisco-IOS-XR-man-ipsla-cfg', False),
            _MetaInfoClassMember('life', REFERENCE_UNION, 'str', 'Ipsla-life',
                None, None,
                [], [],
                '''                Length of the time to execute (default 3600
                seconds)
                ''',
                'life',
                'Cisco-IOS-XR-man-ipsla-cfg', False, [
                    _MetaInfoClassMember('life', REFERENCE_ENUM_CLASS, 'IpslaLife', 'enumeration',
                        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_ipsla_cfg', 'IpslaLife',
                        [], [],
                        '''                        Length of the time to execute (default 3600
                        seconds)
                        ''',
                        'life',
                        'Cisco-IOS-XR-man-ipsla-cfg', False),
                    _MetaInfoClassMember('life', ATTRIBUTE, 'int', 'uint32',
                        None, None,
                        [('0', '2147483647')], [],
                        '''                        Length of the time to execute (default 3600
                        seconds)
                        ''',
                        'life',
                        'Cisco-IOS-XR-man-ipsla-cfg', False),
                ]),
            _MetaInfoClassMember('ageout', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('0', '2073600')], [],
                '''                How long to keep this entry after it becomes
                inactive
                ''',
                'ageout',
                'Cisco-IOS-XR-man-ipsla-cfg', False),
            _MetaInfoClassMember('recurring', ATTRIBUTE, 'Empty', 'empty',
                None, None,
                [], [],
                '''                probe to be scheduled automatically every day
                ''',
                'recurring',
                'Cisco-IOS-XR-man-ipsla-cfg', False),
            ],
            'Cisco-IOS-XR-man-ipsla-cfg',
            'schedule',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-man-ipsla-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_ipsla_cfg',
        ),
    },
    'Ipsla.Operation.Schedules' : {
        'meta_info' : _MetaInfoClass('Ipsla.Operation.Schedules', REFERENCE_CLASS,
            '''Schedule an operation''',
            False, 
            [
            _MetaInfoClassMember('schedule', REFERENCE_LIST, 'Schedule', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_ipsla_cfg', 'Ipsla.Operation.Schedules.Schedule',
                [], [],
                '''                Operation schedule configuration
                ''',
                'schedule',
                'Cisco-IOS-XR-man-ipsla-cfg', False),
            ],
            'Cisco-IOS-XR-man-ipsla-cfg',
            'schedules',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-man-ipsla-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_ipsla_cfg',
        ),
    },
    'Ipsla.Operation.Reactions.Reaction.Condition.JitterAverageDs.ThresholdLimits' : {
        'meta_info' : _MetaInfoClass('Ipsla.Operation.Reactions.Reaction.Condition.JitterAverageDs.ThresholdLimits', REFERENCE_CLASS,
            '''Specify threshold limits for the monitored
element''',
            False, 
            [
            _MetaInfoClassMember('lower-limit', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('1', '4294967295')], [],
                '''                Threshold lower limit value
                ''',
                'lower_limit',
                'Cisco-IOS-XR-man-ipsla-cfg', False, is_mandatory=True),
            _MetaInfoClassMember('upper-limit', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('1', '4294967295')], [],
                '''                Threshold upper limit value
                ''',
                'upper_limit',
                'Cisco-IOS-XR-man-ipsla-cfg', False, is_mandatory=True),
            ],
            'Cisco-IOS-XR-man-ipsla-cfg',
            'threshold-limits',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-man-ipsla-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_ipsla_cfg',
            is_presence=True,
        ),
    },
    'Ipsla.Operation.Reactions.Reaction.Condition.JitterAverageDs.ActionType' : {
        'meta_info' : _MetaInfoClass('Ipsla.Operation.Reactions.Reaction.Condition.JitterAverageDs.ActionType', REFERENCE_CLASS,
            '''Type of action to be taken on threshold
violation(s)''',
            False, 
            [
            _MetaInfoClassMember('logging', ATTRIBUTE, 'Empty', 'empty',
                None, None,
                [], [],
                '''                Generate a syslog alarm on threshold violation
                ''',
                'logging',
                'Cisco-IOS-XR-man-ipsla-cfg', False),
            _MetaInfoClassMember('trigger', ATTRIBUTE, 'Empty', 'empty',
                None, None,
                [], [],
                '''                Generate trigger to active reaction triggered
                operation(s)
                ''',
                'trigger',
                'Cisco-IOS-XR-man-ipsla-cfg', False),
            ],
            'Cisco-IOS-XR-man-ipsla-cfg',
            'action-type',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-man-ipsla-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_ipsla_cfg',
        ),
    },
    'Ipsla.Operation.Reactions.Reaction.Condition.JitterAverageDs.ThresholdType' : {
        'meta_info' : _MetaInfoClass('Ipsla.Operation.Reactions.Reaction.Condition.JitterAverageDs.ThresholdType', REFERENCE_CLASS,
            '''Type of thresholding to perform on the monitored
element''',
            False, 
            [
            _MetaInfoClassMember('thresh-type', REFERENCE_ENUM_CLASS, 'IpslaThresholdTypes', 'Ipsla-threshold-types',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_ipsla_cfg', 'IpslaThresholdTypes',
                [], [],
                '''                Type of thresholding to perform
                ''',
                'thresh_type',
                'Cisco-IOS-XR-man-ipsla-cfg', False),
            _MetaInfoClassMember('count1', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('1', '16')], [],
                '''                Probe count for avarage, consecutive case or X
                value for XofY case
                ''',
                'count1',
                'Cisco-IOS-XR-man-ipsla-cfg', False, has_when=True),
            _MetaInfoClassMember('count2', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('1', '16')], [],
                '''                Y value, when threshold type is XofY
                ''',
                'count2',
                'Cisco-IOS-XR-man-ipsla-cfg', False, has_when=True),
            ],
            'Cisco-IOS-XR-man-ipsla-cfg',
            'threshold-type',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-man-ipsla-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_ipsla_cfg',
        ),
    },
    'Ipsla.Operation.Reactions.Reaction.Condition.JitterAverageDs' : {
        'meta_info' : _MetaInfoClass('Ipsla.Operation.Reactions.Reaction.Condition.JitterAverageDs', REFERENCE_CLASS,
            '''React on destination to source jitter
threshold violation''',
            False, 
            [
            _MetaInfoClassMember('threshold-limits', REFERENCE_CLASS, 'ThresholdLimits', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_ipsla_cfg', 'Ipsla.Operation.Reactions.Reaction.Condition.JitterAverageDs.ThresholdLimits',
                [], [],
                '''                Specify threshold limits for the monitored
                element
                ''',
                'threshold_limits',
                'Cisco-IOS-XR-man-ipsla-cfg', False, is_presence=True),
            _MetaInfoClassMember('action-type', REFERENCE_CLASS, 'ActionType', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_ipsla_cfg', 'Ipsla.Operation.Reactions.Reaction.Condition.JitterAverageDs.ActionType',
                [], [],
                '''                Type of action to be taken on threshold
                violation(s)
                ''',
                'action_type',
                'Cisco-IOS-XR-man-ipsla-cfg', False),
            _MetaInfoClassMember('threshold-type', REFERENCE_CLASS, 'ThresholdType', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_ipsla_cfg', 'Ipsla.Operation.Reactions.Reaction.Condition.JitterAverageDs.ThresholdType',
                [], [],
                '''                Type of thresholding to perform on the monitored
                element
                ''',
                'threshold_type',
                'Cisco-IOS-XR-man-ipsla-cfg', False),
            ],
            'Cisco-IOS-XR-man-ipsla-cfg',
            'jitter-average-ds',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-man-ipsla-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_ipsla_cfg',
            is_presence=True,
        ),
    },
    'Ipsla.Operation.Reactions.Reaction.Condition.Timeout.ActionType' : {
        'meta_info' : _MetaInfoClass('Ipsla.Operation.Reactions.Reaction.Condition.Timeout.ActionType', REFERENCE_CLASS,
            '''Type of action to be taken on threshold
violation(s)''',
            False, 
            [
            _MetaInfoClassMember('logging', ATTRIBUTE, 'Empty', 'empty',
                None, None,
                [], [],
                '''                Generate a syslog alarm on threshold violation
                ''',
                'logging',
                'Cisco-IOS-XR-man-ipsla-cfg', False),
            _MetaInfoClassMember('trigger', ATTRIBUTE, 'Empty', 'empty',
                None, None,
                [], [],
                '''                Generate trigger to active reaction triggered
                operation(s)
                ''',
                'trigger',
                'Cisco-IOS-XR-man-ipsla-cfg', False),
            ],
            'Cisco-IOS-XR-man-ipsla-cfg',
            'action-type',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-man-ipsla-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_ipsla_cfg',
        ),
    },
    'Ipsla.Operation.Reactions.Reaction.Condition.Timeout.ThresholdType' : {
        'meta_info' : _MetaInfoClass('Ipsla.Operation.Reactions.Reaction.Condition.Timeout.ThresholdType', REFERENCE_CLASS,
            '''Type of thresholding to perform on the monitored
element''',
            False, 
            [
            _MetaInfoClassMember('thresh-type', REFERENCE_ENUM_CLASS, 'IpslaThresholdTypes', 'Ipsla-threshold-types',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_ipsla_cfg', 'IpslaThresholdTypes',
                [], [],
                '''                Type of thresholding to perform
                ''',
                'thresh_type',
                'Cisco-IOS-XR-man-ipsla-cfg', False),
            _MetaInfoClassMember('count1', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('1', '16')], [],
                '''                Probe count for avarage, consecutive case or X
                value for XofY case
                ''',
                'count1',
                'Cisco-IOS-XR-man-ipsla-cfg', False, has_when=True),
            _MetaInfoClassMember('count2', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('1', '16')], [],
                '''                Y value, when threshold type is XofY
                ''',
                'count2',
                'Cisco-IOS-XR-man-ipsla-cfg', False, has_when=True),
            ],
            'Cisco-IOS-XR-man-ipsla-cfg',
            'threshold-type',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-man-ipsla-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_ipsla_cfg',
        ),
    },
    'Ipsla.Operation.Reactions.Reaction.Condition.Timeout' : {
        'meta_info' : _MetaInfoClass('Ipsla.Operation.Reactions.Reaction.Condition.Timeout', REFERENCE_CLASS,
            '''React on probe timeout''',
            False, 
            [
            _MetaInfoClassMember('action-type', REFERENCE_CLASS, 'ActionType', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_ipsla_cfg', 'Ipsla.Operation.Reactions.Reaction.Condition.Timeout.ActionType',
                [], [],
                '''                Type of action to be taken on threshold
                violation(s)
                ''',
                'action_type',
                'Cisco-IOS-XR-man-ipsla-cfg', False),
            _MetaInfoClassMember('threshold-type', REFERENCE_CLASS, 'ThresholdType', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_ipsla_cfg', 'Ipsla.Operation.Reactions.Reaction.Condition.Timeout.ThresholdType',
                [], [],
                '''                Type of thresholding to perform on the monitored
                element
                ''',
                'threshold_type',
                'Cisco-IOS-XR-man-ipsla-cfg', False),
            ],
            'Cisco-IOS-XR-man-ipsla-cfg',
            'timeout',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-man-ipsla-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_ipsla_cfg',
            is_presence=True,
        ),
    },
    'Ipsla.Operation.Reactions.Reaction.Condition.JitterAverage.ThresholdLimits' : {
        'meta_info' : _MetaInfoClass('Ipsla.Operation.Reactions.Reaction.Condition.JitterAverage.ThresholdLimits', REFERENCE_CLASS,
            '''Specify threshold limits for the monitored
element''',
            False, 
            [
            _MetaInfoClassMember('lower-limit', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('1', '4294967295')], [],
                '''                Threshold lower limit value
                ''',
                'lower_limit',
                'Cisco-IOS-XR-man-ipsla-cfg', False, is_mandatory=True),
            _MetaInfoClassMember('upper-limit', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('1', '4294967295')], [],
                '''                Threshold upper limit value
                ''',
                'upper_limit',
                'Cisco-IOS-XR-man-ipsla-cfg', False, is_mandatory=True),
            ],
            'Cisco-IOS-XR-man-ipsla-cfg',
            'threshold-limits',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-man-ipsla-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_ipsla_cfg',
            is_presence=True,
        ),
    },
    'Ipsla.Operation.Reactions.Reaction.Condition.JitterAverage.ActionType' : {
        'meta_info' : _MetaInfoClass('Ipsla.Operation.Reactions.Reaction.Condition.JitterAverage.ActionType', REFERENCE_CLASS,
            '''Type of action to be taken on threshold
violation(s)''',
            False, 
            [
            _MetaInfoClassMember('logging', ATTRIBUTE, 'Empty', 'empty',
                None, None,
                [], [],
                '''                Generate a syslog alarm on threshold violation
                ''',
                'logging',
                'Cisco-IOS-XR-man-ipsla-cfg', False),
            _MetaInfoClassMember('trigger', ATTRIBUTE, 'Empty', 'empty',
                None, None,
                [], [],
                '''                Generate trigger to active reaction triggered
                operation(s)
                ''',
                'trigger',
                'Cisco-IOS-XR-man-ipsla-cfg', False),
            ],
            'Cisco-IOS-XR-man-ipsla-cfg',
            'action-type',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-man-ipsla-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_ipsla_cfg',
        ),
    },
    'Ipsla.Operation.Reactions.Reaction.Condition.JitterAverage.ThresholdType' : {
        'meta_info' : _MetaInfoClass('Ipsla.Operation.Reactions.Reaction.Condition.JitterAverage.ThresholdType', REFERENCE_CLASS,
            '''Type of thresholding to perform on the monitored
element''',
            False, 
            [
            _MetaInfoClassMember('thresh-type', REFERENCE_ENUM_CLASS, 'IpslaThresholdTypes', 'Ipsla-threshold-types',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_ipsla_cfg', 'IpslaThresholdTypes',
                [], [],
                '''                Type of thresholding to perform
                ''',
                'thresh_type',
                'Cisco-IOS-XR-man-ipsla-cfg', False),
            _MetaInfoClassMember('count1', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('1', '16')], [],
                '''                Probe count for avarage, consecutive case or X
                value for XofY case
                ''',
                'count1',
                'Cisco-IOS-XR-man-ipsla-cfg', False, has_when=True),
            _MetaInfoClassMember('count2', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('1', '16')], [],
                '''                Y value, when threshold type is XofY
                ''',
                'count2',
                'Cisco-IOS-XR-man-ipsla-cfg', False, has_when=True),
            ],
            'Cisco-IOS-XR-man-ipsla-cfg',
            'threshold-type',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-man-ipsla-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_ipsla_cfg',
        ),
    },
    'Ipsla.Operation.Reactions.Reaction.Condition.JitterAverage' : {
        'meta_info' : _MetaInfoClass('Ipsla.Operation.Reactions.Reaction.Condition.JitterAverage', REFERENCE_CLASS,
            '''React on average round trip jitter threshold
violation''',
            False, 
            [
            _MetaInfoClassMember('threshold-limits', REFERENCE_CLASS, 'ThresholdLimits', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_ipsla_cfg', 'Ipsla.Operation.Reactions.Reaction.Condition.JitterAverage.ThresholdLimits',
                [], [],
                '''                Specify threshold limits for the monitored
                element
                ''',
                'threshold_limits',
                'Cisco-IOS-XR-man-ipsla-cfg', False, is_presence=True),
            _MetaInfoClassMember('action-type', REFERENCE_CLASS, 'ActionType', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_ipsla_cfg', 'Ipsla.Operation.Reactions.Reaction.Condition.JitterAverage.ActionType',
                [], [],
                '''                Type of action to be taken on threshold
                violation(s)
                ''',
                'action_type',
                'Cisco-IOS-XR-man-ipsla-cfg', False),
            _MetaInfoClassMember('threshold-type', REFERENCE_CLASS, 'ThresholdType', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_ipsla_cfg', 'Ipsla.Operation.Reactions.Reaction.Condition.JitterAverage.ThresholdType',
                [], [],
                '''                Type of thresholding to perform on the monitored
                element
                ''',
                'threshold_type',
                'Cisco-IOS-XR-man-ipsla-cfg', False),
            ],
            'Cisco-IOS-XR-man-ipsla-cfg',
            'jitter-average',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-man-ipsla-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_ipsla_cfg',
            is_presence=True,
        ),
    },
    'Ipsla.Operation.Reactions.Reaction.Condition.VerifyError.ActionType' : {
        'meta_info' : _MetaInfoClass('Ipsla.Operation.Reactions.Reaction.Condition.VerifyError.ActionType', REFERENCE_CLASS,
            '''Type of action to be taken on threshold
violation(s)''',
            False, 
            [
            _MetaInfoClassMember('logging', ATTRIBUTE, 'Empty', 'empty',
                None, None,
                [], [],
                '''                Generate a syslog alarm on threshold violation
                ''',
                'logging',
                'Cisco-IOS-XR-man-ipsla-cfg', False),
            _MetaInfoClassMember('trigger', ATTRIBUTE, 'Empty', 'empty',
                None, None,
                [], [],
                '''                Generate trigger to active reaction triggered
                operation(s)
                ''',
                'trigger',
                'Cisco-IOS-XR-man-ipsla-cfg', False),
            ],
            'Cisco-IOS-XR-man-ipsla-cfg',
            'action-type',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-man-ipsla-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_ipsla_cfg',
        ),
    },
    'Ipsla.Operation.Reactions.Reaction.Condition.VerifyError.ThresholdType' : {
        'meta_info' : _MetaInfoClass('Ipsla.Operation.Reactions.Reaction.Condition.VerifyError.ThresholdType', REFERENCE_CLASS,
            '''Type of thresholding to perform on the monitored
element''',
            False, 
            [
            _MetaInfoClassMember('thresh-type', REFERENCE_ENUM_CLASS, 'IpslaThresholdTypes', 'Ipsla-threshold-types',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_ipsla_cfg', 'IpslaThresholdTypes',
                [], [],
                '''                Type of thresholding to perform
                ''',
                'thresh_type',
                'Cisco-IOS-XR-man-ipsla-cfg', False),
            _MetaInfoClassMember('count1', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('1', '16')], [],
                '''                Probe count for avarage, consecutive case or X
                value for XofY case
                ''',
                'count1',
                'Cisco-IOS-XR-man-ipsla-cfg', False, has_when=True),
            _MetaInfoClassMember('count2', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('1', '16')], [],
                '''                Y value, when threshold type is XofY
                ''',
                'count2',
                'Cisco-IOS-XR-man-ipsla-cfg', False, has_when=True),
            ],
            'Cisco-IOS-XR-man-ipsla-cfg',
            'threshold-type',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-man-ipsla-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_ipsla_cfg',
        ),
    },
    'Ipsla.Operation.Reactions.Reaction.Condition.VerifyError' : {
        'meta_info' : _MetaInfoClass('Ipsla.Operation.Reactions.Reaction.Condition.VerifyError', REFERENCE_CLASS,
            '''React on error verfication violation''',
            False, 
            [
            _MetaInfoClassMember('action-type', REFERENCE_CLASS, 'ActionType', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_ipsla_cfg', 'Ipsla.Operation.Reactions.Reaction.Condition.VerifyError.ActionType',
                [], [],
                '''                Type of action to be taken on threshold
                violation(s)
                ''',
                'action_type',
                'Cisco-IOS-XR-man-ipsla-cfg', False),
            _MetaInfoClassMember('threshold-type', REFERENCE_CLASS, 'ThresholdType', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_ipsla_cfg', 'Ipsla.Operation.Reactions.Reaction.Condition.VerifyError.ThresholdType',
                [], [],
                '''                Type of thresholding to perform on the monitored
                element
                ''',
                'threshold_type',
                'Cisco-IOS-XR-man-ipsla-cfg', False),
            ],
            'Cisco-IOS-XR-man-ipsla-cfg',
            'verify-error',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-man-ipsla-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_ipsla_cfg',
            is_presence=True,
        ),
    },
    'Ipsla.Operation.Reactions.Reaction.Condition.Rtt.ThresholdLimits' : {
        'meta_info' : _MetaInfoClass('Ipsla.Operation.Reactions.Reaction.Condition.Rtt.ThresholdLimits', REFERENCE_CLASS,
            '''Specify threshold limits for the monitored
element''',
            False, 
            [
            _MetaInfoClassMember('lower-limit', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('1', '4294967295')], [],
                '''                Threshold lower limit value
                ''',
                'lower_limit',
                'Cisco-IOS-XR-man-ipsla-cfg', False, is_mandatory=True),
            _MetaInfoClassMember('upper-limit', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('1', '4294967295')], [],
                '''                Threshold upper limit value
                ''',
                'upper_limit',
                'Cisco-IOS-XR-man-ipsla-cfg', False, is_mandatory=True),
            ],
            'Cisco-IOS-XR-man-ipsla-cfg',
            'threshold-limits',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-man-ipsla-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_ipsla_cfg',
            is_presence=True,
        ),
    },
    'Ipsla.Operation.Reactions.Reaction.Condition.Rtt.ActionType' : {
        'meta_info' : _MetaInfoClass('Ipsla.Operation.Reactions.Reaction.Condition.Rtt.ActionType', REFERENCE_CLASS,
            '''Type of action to be taken on threshold
violation(s)''',
            False, 
            [
            _MetaInfoClassMember('logging', ATTRIBUTE, 'Empty', 'empty',
                None, None,
                [], [],
                '''                Generate a syslog alarm on threshold violation
                ''',
                'logging',
                'Cisco-IOS-XR-man-ipsla-cfg', False),
            _MetaInfoClassMember('trigger', ATTRIBUTE, 'Empty', 'empty',
                None, None,
                [], [],
                '''                Generate trigger to active reaction triggered
                operation(s)
                ''',
                'trigger',
                'Cisco-IOS-XR-man-ipsla-cfg', False),
            ],
            'Cisco-IOS-XR-man-ipsla-cfg',
            'action-type',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-man-ipsla-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_ipsla_cfg',
        ),
    },
    'Ipsla.Operation.Reactions.Reaction.Condition.Rtt.ThresholdType' : {
        'meta_info' : _MetaInfoClass('Ipsla.Operation.Reactions.Reaction.Condition.Rtt.ThresholdType', REFERENCE_CLASS,
            '''Type of thresholding to perform on the monitored
element''',
            False, 
            [
            _MetaInfoClassMember('thresh-type', REFERENCE_ENUM_CLASS, 'IpslaThresholdTypes', 'Ipsla-threshold-types',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_ipsla_cfg', 'IpslaThresholdTypes',
                [], [],
                '''                Type of thresholding to perform
                ''',
                'thresh_type',
                'Cisco-IOS-XR-man-ipsla-cfg', False),
            _MetaInfoClassMember('count1', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('1', '16')], [],
                '''                Probe count for avarage, consecutive case or X
                value for XofY case
                ''',
                'count1',
                'Cisco-IOS-XR-man-ipsla-cfg', False, has_when=True),
            _MetaInfoClassMember('count2', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('1', '16')], [],
                '''                Y value, when threshold type is XofY
                ''',
                'count2',
                'Cisco-IOS-XR-man-ipsla-cfg', False, has_when=True),
            ],
            'Cisco-IOS-XR-man-ipsla-cfg',
            'threshold-type',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-man-ipsla-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_ipsla_cfg',
        ),
    },
    'Ipsla.Operation.Reactions.Reaction.Condition.Rtt' : {
        'meta_info' : _MetaInfoClass('Ipsla.Operation.Reactions.Reaction.Condition.Rtt', REFERENCE_CLASS,
            '''React on round trip time threshold violation''',
            False, 
            [
            _MetaInfoClassMember('threshold-limits', REFERENCE_CLASS, 'ThresholdLimits', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_ipsla_cfg', 'Ipsla.Operation.Reactions.Reaction.Condition.Rtt.ThresholdLimits',
                [], [],
                '''                Specify threshold limits for the monitored
                element
                ''',
                'threshold_limits',
                'Cisco-IOS-XR-man-ipsla-cfg', False, is_presence=True),
            _MetaInfoClassMember('action-type', REFERENCE_CLASS, 'ActionType', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_ipsla_cfg', 'Ipsla.Operation.Reactions.Reaction.Condition.Rtt.ActionType',
                [], [],
                '''                Type of action to be taken on threshold
                violation(s)
                ''',
                'action_type',
                'Cisco-IOS-XR-man-ipsla-cfg', False),
            _MetaInfoClassMember('threshold-type', REFERENCE_CLASS, 'ThresholdType', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_ipsla_cfg', 'Ipsla.Operation.Reactions.Reaction.Condition.Rtt.ThresholdType',
                [], [],
                '''                Type of thresholding to perform on the monitored
                element
                ''',
                'threshold_type',
                'Cisco-IOS-XR-man-ipsla-cfg', False),
            ],
            'Cisco-IOS-XR-man-ipsla-cfg',
            'rtt',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-man-ipsla-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_ipsla_cfg',
            is_presence=True,
        ),
    },
    'Ipsla.Operation.Reactions.Reaction.Condition.PacketLossSd.ThresholdLimits' : {
        'meta_info' : _MetaInfoClass('Ipsla.Operation.Reactions.Reaction.Condition.PacketLossSd.ThresholdLimits', REFERENCE_CLASS,
            '''Specify threshold limits for the monitored
element''',
            False, 
            [
            _MetaInfoClassMember('lower-limit', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('1', '4294967295')], [],
                '''                Threshold lower limit value
                ''',
                'lower_limit',
                'Cisco-IOS-XR-man-ipsla-cfg', False, is_mandatory=True),
            _MetaInfoClassMember('upper-limit', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('1', '4294967295')], [],
                '''                Threshold upper limit value
                ''',
                'upper_limit',
                'Cisco-IOS-XR-man-ipsla-cfg', False, is_mandatory=True),
            ],
            'Cisco-IOS-XR-man-ipsla-cfg',
            'threshold-limits',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-man-ipsla-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_ipsla_cfg',
            is_presence=True,
        ),
    },
    'Ipsla.Operation.Reactions.Reaction.Condition.PacketLossSd.ActionType' : {
        'meta_info' : _MetaInfoClass('Ipsla.Operation.Reactions.Reaction.Condition.PacketLossSd.ActionType', REFERENCE_CLASS,
            '''Type of action to be taken on threshold
violation(s)''',
            False, 
            [
            _MetaInfoClassMember('logging', ATTRIBUTE, 'Empty', 'empty',
                None, None,
                [], [],
                '''                Generate a syslog alarm on threshold violation
                ''',
                'logging',
                'Cisco-IOS-XR-man-ipsla-cfg', False),
            _MetaInfoClassMember('trigger', ATTRIBUTE, 'Empty', 'empty',
                None, None,
                [], [],
                '''                Generate trigger to active reaction triggered
                operation(s)
                ''',
                'trigger',
                'Cisco-IOS-XR-man-ipsla-cfg', False),
            ],
            'Cisco-IOS-XR-man-ipsla-cfg',
            'action-type',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-man-ipsla-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_ipsla_cfg',
        ),
    },
    'Ipsla.Operation.Reactions.Reaction.Condition.PacketLossSd.ThresholdType' : {
        'meta_info' : _MetaInfoClass('Ipsla.Operation.Reactions.Reaction.Condition.PacketLossSd.ThresholdType', REFERENCE_CLASS,
            '''Type of thresholding to perform on the monitored
element''',
            False, 
            [
            _MetaInfoClassMember('thresh-type', REFERENCE_ENUM_CLASS, 'IpslaThresholdTypes', 'Ipsla-threshold-types',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_ipsla_cfg', 'IpslaThresholdTypes',
                [], [],
                '''                Type of thresholding to perform
                ''',
                'thresh_type',
                'Cisco-IOS-XR-man-ipsla-cfg', False),
            _MetaInfoClassMember('count1', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('1', '16')], [],
                '''                Probe count for avarage, consecutive case or X
                value for XofY case
                ''',
                'count1',
                'Cisco-IOS-XR-man-ipsla-cfg', False, has_when=True),
            _MetaInfoClassMember('count2', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('1', '16')], [],
                '''                Y value, when threshold type is XofY
                ''',
                'count2',
                'Cisco-IOS-XR-man-ipsla-cfg', False, has_when=True),
            ],
            'Cisco-IOS-XR-man-ipsla-cfg',
            'threshold-type',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-man-ipsla-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_ipsla_cfg',
        ),
    },
    'Ipsla.Operation.Reactions.Reaction.Condition.PacketLossSd' : {
        'meta_info' : _MetaInfoClass('Ipsla.Operation.Reactions.Reaction.Condition.PacketLossSd', REFERENCE_CLASS,
            '''React on destination to source packet loss
threshold violation''',
            False, 
            [
            _MetaInfoClassMember('threshold-limits', REFERENCE_CLASS, 'ThresholdLimits', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_ipsla_cfg', 'Ipsla.Operation.Reactions.Reaction.Condition.PacketLossSd.ThresholdLimits',
                [], [],
                '''                Specify threshold limits for the monitored
                element
                ''',
                'threshold_limits',
                'Cisco-IOS-XR-man-ipsla-cfg', False, is_presence=True),
            _MetaInfoClassMember('action-type', REFERENCE_CLASS, 'ActionType', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_ipsla_cfg', 'Ipsla.Operation.Reactions.Reaction.Condition.PacketLossSd.ActionType',
                [], [],
                '''                Type of action to be taken on threshold
                violation(s)
                ''',
                'action_type',
                'Cisco-IOS-XR-man-ipsla-cfg', False),
            _MetaInfoClassMember('threshold-type', REFERENCE_CLASS, 'ThresholdType', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_ipsla_cfg', 'Ipsla.Operation.Reactions.Reaction.Condition.PacketLossSd.ThresholdType',
                [], [],
                '''                Type of thresholding to perform on the monitored
                element
                ''',
                'threshold_type',
                'Cisco-IOS-XR-man-ipsla-cfg', False),
            ],
            'Cisco-IOS-XR-man-ipsla-cfg',
            'packet-loss-sd',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-man-ipsla-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_ipsla_cfg',
            is_presence=True,
        ),
    },
    'Ipsla.Operation.Reactions.Reaction.Condition.JitterAverageSd.ThresholdLimits' : {
        'meta_info' : _MetaInfoClass('Ipsla.Operation.Reactions.Reaction.Condition.JitterAverageSd.ThresholdLimits', REFERENCE_CLASS,
            '''Specify threshold limits for the monitored
element''',
            False, 
            [
            _MetaInfoClassMember('lower-limit', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('1', '4294967295')], [],
                '''                Threshold lower limit value
                ''',
                'lower_limit',
                'Cisco-IOS-XR-man-ipsla-cfg', False, is_mandatory=True),
            _MetaInfoClassMember('upper-limit', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('1', '4294967295')], [],
                '''                Threshold upper limit value
                ''',
                'upper_limit',
                'Cisco-IOS-XR-man-ipsla-cfg', False, is_mandatory=True),
            ],
            'Cisco-IOS-XR-man-ipsla-cfg',
            'threshold-limits',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-man-ipsla-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_ipsla_cfg',
            is_presence=True,
        ),
    },
    'Ipsla.Operation.Reactions.Reaction.Condition.JitterAverageSd.ActionType' : {
        'meta_info' : _MetaInfoClass('Ipsla.Operation.Reactions.Reaction.Condition.JitterAverageSd.ActionType', REFERENCE_CLASS,
            '''Type of action to be taken on threshold
violation(s)''',
            False, 
            [
            _MetaInfoClassMember('logging', ATTRIBUTE, 'Empty', 'empty',
                None, None,
                [], [],
                '''                Generate a syslog alarm on threshold violation
                ''',
                'logging',
                'Cisco-IOS-XR-man-ipsla-cfg', False),
            _MetaInfoClassMember('trigger', ATTRIBUTE, 'Empty', 'empty',
                None, None,
                [], [],
                '''                Generate trigger to active reaction triggered
                operation(s)
                ''',
                'trigger',
                'Cisco-IOS-XR-man-ipsla-cfg', False),
            ],
            'Cisco-IOS-XR-man-ipsla-cfg',
            'action-type',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-man-ipsla-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_ipsla_cfg',
        ),
    },
    'Ipsla.Operation.Reactions.Reaction.Condition.JitterAverageSd.ThresholdType' : {
        'meta_info' : _MetaInfoClass('Ipsla.Operation.Reactions.Reaction.Condition.JitterAverageSd.ThresholdType', REFERENCE_CLASS,
            '''Type of thresholding to perform on the monitored
element''',
            False, 
            [
            _MetaInfoClassMember('thresh-type', REFERENCE_ENUM_CLASS, 'IpslaThresholdTypes', 'Ipsla-threshold-types',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_ipsla_cfg', 'IpslaThresholdTypes',
                [], [],
                '''                Type of thresholding to perform
                ''',
                'thresh_type',
                'Cisco-IOS-XR-man-ipsla-cfg', False),
            _MetaInfoClassMember('count1', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('1', '16')], [],
                '''                Probe count for avarage, consecutive case or X
                value for XofY case
                ''',
                'count1',
                'Cisco-IOS-XR-man-ipsla-cfg', False, has_when=True),
            _MetaInfoClassMember('count2', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('1', '16')], [],
                '''                Y value, when threshold type is XofY
                ''',
                'count2',
                'Cisco-IOS-XR-man-ipsla-cfg', False, has_when=True),
            ],
            'Cisco-IOS-XR-man-ipsla-cfg',
            'threshold-type',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-man-ipsla-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_ipsla_cfg',
        ),
    },
    'Ipsla.Operation.Reactions.Reaction.Condition.JitterAverageSd' : {
        'meta_info' : _MetaInfoClass('Ipsla.Operation.Reactions.Reaction.Condition.JitterAverageSd', REFERENCE_CLASS,
            '''React on average source to destination
jitter threshold violation''',
            False, 
            [
            _MetaInfoClassMember('threshold-limits', REFERENCE_CLASS, 'ThresholdLimits', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_ipsla_cfg', 'Ipsla.Operation.Reactions.Reaction.Condition.JitterAverageSd.ThresholdLimits',
                [], [],
                '''                Specify threshold limits for the monitored
                element
                ''',
                'threshold_limits',
                'Cisco-IOS-XR-man-ipsla-cfg', False, is_presence=True),
            _MetaInfoClassMember('action-type', REFERENCE_CLASS, 'ActionType', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_ipsla_cfg', 'Ipsla.Operation.Reactions.Reaction.Condition.JitterAverageSd.ActionType',
                [], [],
                '''                Type of action to be taken on threshold
                violation(s)
                ''',
                'action_type',
                'Cisco-IOS-XR-man-ipsla-cfg', False),
            _MetaInfoClassMember('threshold-type', REFERENCE_CLASS, 'ThresholdType', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_ipsla_cfg', 'Ipsla.Operation.Reactions.Reaction.Condition.JitterAverageSd.ThresholdType',
                [], [],
                '''                Type of thresholding to perform on the monitored
                element
                ''',
                'threshold_type',
                'Cisco-IOS-XR-man-ipsla-cfg', False),
            ],
            'Cisco-IOS-XR-man-ipsla-cfg',
            'jitter-average-sd',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-man-ipsla-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_ipsla_cfg',
            is_presence=True,
        ),
    },
    'Ipsla.Operation.Reactions.Reaction.Condition.ConnectionLoss.ActionType' : {
        'meta_info' : _MetaInfoClass('Ipsla.Operation.Reactions.Reaction.Condition.ConnectionLoss.ActionType', REFERENCE_CLASS,
            '''Type of action to be taken on threshold
violation(s)''',
            False, 
            [
            _MetaInfoClassMember('logging', ATTRIBUTE, 'Empty', 'empty',
                None, None,
                [], [],
                '''                Generate a syslog alarm on threshold violation
                ''',
                'logging',
                'Cisco-IOS-XR-man-ipsla-cfg', False),
            _MetaInfoClassMember('trigger', ATTRIBUTE, 'Empty', 'empty',
                None, None,
                [], [],
                '''                Generate trigger to active reaction triggered
                operation(s)
                ''',
                'trigger',
                'Cisco-IOS-XR-man-ipsla-cfg', False),
            ],
            'Cisco-IOS-XR-man-ipsla-cfg',
            'action-type',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-man-ipsla-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_ipsla_cfg',
        ),
    },
    'Ipsla.Operation.Reactions.Reaction.Condition.ConnectionLoss.ThresholdType' : {
        'meta_info' : _MetaInfoClass('Ipsla.Operation.Reactions.Reaction.Condition.ConnectionLoss.ThresholdType', REFERENCE_CLASS,
            '''Type of thresholding to perform on the monitored
element''',
            False, 
            [
            _MetaInfoClassMember('thresh-type', REFERENCE_ENUM_CLASS, 'IpslaThresholdTypes', 'Ipsla-threshold-types',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_ipsla_cfg', 'IpslaThresholdTypes',
                [], [],
                '''                Type of thresholding to perform
                ''',
                'thresh_type',
                'Cisco-IOS-XR-man-ipsla-cfg', False),
            _MetaInfoClassMember('count1', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('1', '16')], [],
                '''                Probe count for avarage, consecutive case or X
                value for XofY case
                ''',
                'count1',
                'Cisco-IOS-XR-man-ipsla-cfg', False, has_when=True),
            _MetaInfoClassMember('count2', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('1', '16')], [],
                '''                Y value, when threshold type is XofY
                ''',
                'count2',
                'Cisco-IOS-XR-man-ipsla-cfg', False, has_when=True),
            ],
            'Cisco-IOS-XR-man-ipsla-cfg',
            'threshold-type',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-man-ipsla-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_ipsla_cfg',
        ),
    },
    'Ipsla.Operation.Reactions.Reaction.Condition.ConnectionLoss' : {
        'meta_info' : _MetaInfoClass('Ipsla.Operation.Reactions.Reaction.Condition.ConnectionLoss', REFERENCE_CLASS,
            '''React on connection loss for a monitored
operation''',
            False, 
            [
            _MetaInfoClassMember('action-type', REFERENCE_CLASS, 'ActionType', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_ipsla_cfg', 'Ipsla.Operation.Reactions.Reaction.Condition.ConnectionLoss.ActionType',
                [], [],
                '''                Type of action to be taken on threshold
                violation(s)
                ''',
                'action_type',
                'Cisco-IOS-XR-man-ipsla-cfg', False),
            _MetaInfoClassMember('threshold-type', REFERENCE_CLASS, 'ThresholdType', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_ipsla_cfg', 'Ipsla.Operation.Reactions.Reaction.Condition.ConnectionLoss.ThresholdType',
                [], [],
                '''                Type of thresholding to perform on the monitored
                element
                ''',
                'threshold_type',
                'Cisco-IOS-XR-man-ipsla-cfg', False),
            ],
            'Cisco-IOS-XR-man-ipsla-cfg',
            'connection-loss',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-man-ipsla-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_ipsla_cfg',
            is_presence=True,
        ),
    },
    'Ipsla.Operation.Reactions.Reaction.Condition.PacketLossDs.ThresholdLimits' : {
        'meta_info' : _MetaInfoClass('Ipsla.Operation.Reactions.Reaction.Condition.PacketLossDs.ThresholdLimits', REFERENCE_CLASS,
            '''Specify threshold limits for the monitored
element''',
            False, 
            [
            _MetaInfoClassMember('lower-limit', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('1', '4294967295')], [],
                '''                Threshold lower limit value
                ''',
                'lower_limit',
                'Cisco-IOS-XR-man-ipsla-cfg', False, is_mandatory=True),
            _MetaInfoClassMember('upper-limit', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('1', '4294967295')], [],
                '''                Threshold upper limit value
                ''',
                'upper_limit',
                'Cisco-IOS-XR-man-ipsla-cfg', False, is_mandatory=True),
            ],
            'Cisco-IOS-XR-man-ipsla-cfg',
            'threshold-limits',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-man-ipsla-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_ipsla_cfg',
            is_presence=True,
        ),
    },
    'Ipsla.Operation.Reactions.Reaction.Condition.PacketLossDs.ActionType' : {
        'meta_info' : _MetaInfoClass('Ipsla.Operation.Reactions.Reaction.Condition.PacketLossDs.ActionType', REFERENCE_CLASS,
            '''Type of action to be taken on threshold
violation(s)''',
            False, 
            [
            _MetaInfoClassMember('logging', ATTRIBUTE, 'Empty', 'empty',
                None, None,
                [], [],
                '''                Generate a syslog alarm on threshold violation
                ''',
                'logging',
                'Cisco-IOS-XR-man-ipsla-cfg', False),
            _MetaInfoClassMember('trigger', ATTRIBUTE, 'Empty', 'empty',
                None, None,
                [], [],
                '''                Generate trigger to active reaction triggered
                operation(s)
                ''',
                'trigger',
                'Cisco-IOS-XR-man-ipsla-cfg', False),
            ],
            'Cisco-IOS-XR-man-ipsla-cfg',
            'action-type',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-man-ipsla-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_ipsla_cfg',
        ),
    },
    'Ipsla.Operation.Reactions.Reaction.Condition.PacketLossDs.ThresholdType' : {
        'meta_info' : _MetaInfoClass('Ipsla.Operation.Reactions.Reaction.Condition.PacketLossDs.ThresholdType', REFERENCE_CLASS,
            '''Type of thresholding to perform on the monitored
element''',
            False, 
            [
            _MetaInfoClassMember('thresh-type', REFERENCE_ENUM_CLASS, 'IpslaThresholdTypes', 'Ipsla-threshold-types',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_ipsla_cfg', 'IpslaThresholdTypes',
                [], [],
                '''                Type of thresholding to perform
                ''',
                'thresh_type',
                'Cisco-IOS-XR-man-ipsla-cfg', False),
            _MetaInfoClassMember('count1', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('1', '16')], [],
                '''                Probe count for avarage, consecutive case or X
                value for XofY case
                ''',
                'count1',
                'Cisco-IOS-XR-man-ipsla-cfg', False, has_when=True),
            _MetaInfoClassMember('count2', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('1', '16')], [],
                '''                Y value, when threshold type is XofY
                ''',
                'count2',
                'Cisco-IOS-XR-man-ipsla-cfg', False, has_when=True),
            ],
            'Cisco-IOS-XR-man-ipsla-cfg',
            'threshold-type',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-man-ipsla-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_ipsla_cfg',
        ),
    },
    'Ipsla.Operation.Reactions.Reaction.Condition.PacketLossDs' : {
        'meta_info' : _MetaInfoClass('Ipsla.Operation.Reactions.Reaction.Condition.PacketLossDs', REFERENCE_CLASS,
            '''React on source to destination packet loss
threshold violation''',
            False, 
            [
            _MetaInfoClassMember('threshold-limits', REFERENCE_CLASS, 'ThresholdLimits', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_ipsla_cfg', 'Ipsla.Operation.Reactions.Reaction.Condition.PacketLossDs.ThresholdLimits',
                [], [],
                '''                Specify threshold limits for the monitored
                element
                ''',
                'threshold_limits',
                'Cisco-IOS-XR-man-ipsla-cfg', False, is_presence=True),
            _MetaInfoClassMember('action-type', REFERENCE_CLASS, 'ActionType', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_ipsla_cfg', 'Ipsla.Operation.Reactions.Reaction.Condition.PacketLossDs.ActionType',
                [], [],
                '''                Type of action to be taken on threshold
                violation(s)
                ''',
                'action_type',
                'Cisco-IOS-XR-man-ipsla-cfg', False),
            _MetaInfoClassMember('threshold-type', REFERENCE_CLASS, 'ThresholdType', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_ipsla_cfg', 'Ipsla.Operation.Reactions.Reaction.Condition.PacketLossDs.ThresholdType',
                [], [],
                '''                Type of thresholding to perform on the monitored
                element
                ''',
                'threshold_type',
                'Cisco-IOS-XR-man-ipsla-cfg', False),
            ],
            'Cisco-IOS-XR-man-ipsla-cfg',
            'packet-loss-ds',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-man-ipsla-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_ipsla_cfg',
            is_presence=True,
        ),
    },
    'Ipsla.Operation.Reactions.Reaction.Condition' : {
        'meta_info' : _MetaInfoClass('Ipsla.Operation.Reactions.Reaction.Condition', REFERENCE_CLASS,
            '''Reaction condition specification''',
            False, 
            [
            _MetaInfoClassMember('jitter-average-ds', REFERENCE_CLASS, 'JitterAverageDs', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_ipsla_cfg', 'Ipsla.Operation.Reactions.Reaction.Condition.JitterAverageDs',
                [], [],
                '''                React on destination to source jitter
                threshold violation
                ''',
                'jitter_average_ds',
                'Cisco-IOS-XR-man-ipsla-cfg', False, is_presence=True),
            _MetaInfoClassMember('timeout', REFERENCE_CLASS, 'Timeout', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_ipsla_cfg', 'Ipsla.Operation.Reactions.Reaction.Condition.Timeout',
                [], [],
                '''                React on probe timeout
                ''',
                'timeout',
                'Cisco-IOS-XR-man-ipsla-cfg', False, is_presence=True),
            _MetaInfoClassMember('jitter-average', REFERENCE_CLASS, 'JitterAverage', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_ipsla_cfg', 'Ipsla.Operation.Reactions.Reaction.Condition.JitterAverage',
                [], [],
                '''                React on average round trip jitter threshold
                violation
                ''',
                'jitter_average',
                'Cisco-IOS-XR-man-ipsla-cfg', False, is_presence=True),
            _MetaInfoClassMember('verify-error', REFERENCE_CLASS, 'VerifyError', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_ipsla_cfg', 'Ipsla.Operation.Reactions.Reaction.Condition.VerifyError',
                [], [],
                '''                React on error verfication violation
                ''',
                'verify_error',
                'Cisco-IOS-XR-man-ipsla-cfg', False, is_presence=True),
            _MetaInfoClassMember('rtt', REFERENCE_CLASS, 'Rtt', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_ipsla_cfg', 'Ipsla.Operation.Reactions.Reaction.Condition.Rtt',
                [], [],
                '''                React on round trip time threshold violation
                ''',
                'rtt',
                'Cisco-IOS-XR-man-ipsla-cfg', False, is_presence=True),
            _MetaInfoClassMember('packet-loss-sd', REFERENCE_CLASS, 'PacketLossSd', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_ipsla_cfg', 'Ipsla.Operation.Reactions.Reaction.Condition.PacketLossSd',
                [], [],
                '''                React on destination to source packet loss
                threshold violation
                ''',
                'packet_loss_sd',
                'Cisco-IOS-XR-man-ipsla-cfg', False, is_presence=True),
            _MetaInfoClassMember('jitter-average-sd', REFERENCE_CLASS, 'JitterAverageSd', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_ipsla_cfg', 'Ipsla.Operation.Reactions.Reaction.Condition.JitterAverageSd',
                [], [],
                '''                React on average source to destination
                jitter threshold violation
                ''',
                'jitter_average_sd',
                'Cisco-IOS-XR-man-ipsla-cfg', False, is_presence=True),
            _MetaInfoClassMember('connection-loss', REFERENCE_CLASS, 'ConnectionLoss', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_ipsla_cfg', 'Ipsla.Operation.Reactions.Reaction.Condition.ConnectionLoss',
                [], [],
                '''                React on connection loss for a monitored
                operation
                ''',
                'connection_loss',
                'Cisco-IOS-XR-man-ipsla-cfg', False, is_presence=True),
            _MetaInfoClassMember('packet-loss-ds', REFERENCE_CLASS, 'PacketLossDs', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_ipsla_cfg', 'Ipsla.Operation.Reactions.Reaction.Condition.PacketLossDs',
                [], [],
                '''                React on source to destination packet loss
                threshold violation
                ''',
                'packet_loss_ds',
                'Cisco-IOS-XR-man-ipsla-cfg', False, is_presence=True),
            ],
            'Cisco-IOS-XR-man-ipsla-cfg',
            'condition',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-man-ipsla-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_ipsla_cfg',
        ),
    },
    'Ipsla.Operation.Reactions.Reaction' : {
        'meta_info' : _MetaInfoClass('Ipsla.Operation.Reactions.Reaction', REFERENCE_LIST,
            '''Reaction configuration for an operation''',
            False, 
            [
            _MetaInfoClassMember('operation-id', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('1', '2048')], [],
                '''                Operation number
                ''',
                'operation_id',
                'Cisco-IOS-XR-man-ipsla-cfg', True),
            _MetaInfoClassMember('condition', REFERENCE_CLASS, 'Condition', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_ipsla_cfg', 'Ipsla.Operation.Reactions.Reaction.Condition',
                [], [],
                '''                Reaction condition specification
                ''',
                'condition',
                'Cisco-IOS-XR-man-ipsla-cfg', False),
            ],
            'Cisco-IOS-XR-man-ipsla-cfg',
            'reaction',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-man-ipsla-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_ipsla_cfg',
        ),
    },
    'Ipsla.Operation.Reactions' : {
        'meta_info' : _MetaInfoClass('Ipsla.Operation.Reactions', REFERENCE_CLASS,
            '''Reaction configuration''',
            False, 
            [
            _MetaInfoClassMember('reaction', REFERENCE_LIST, 'Reaction', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_ipsla_cfg', 'Ipsla.Operation.Reactions.Reaction',
                [], [],
                '''                Reaction configuration for an operation
                ''',
                'reaction',
                'Cisco-IOS-XR-man-ipsla-cfg', False),
            ],
            'Cisco-IOS-XR-man-ipsla-cfg',
            'reactions',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-man-ipsla-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_ipsla_cfg',
        ),
    },
    'Ipsla.Operation.ReactionTriggers.ReactionTrigger' : {
        'meta_info' : _MetaInfoClass('Ipsla.Operation.ReactionTriggers.ReactionTrigger', REFERENCE_LIST,
            '''Reaction trigger for an operation''',
            False, 
            [
            _MetaInfoClassMember('operation-id', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('1', '2048')], [],
                '''                Operation number of the operation generating
                a trigger
                ''',
                'operation_id',
                'Cisco-IOS-XR-man-ipsla-cfg', True),
            _MetaInfoClassMember('triggered-op-id', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('1', '2048')], [],
                '''                Operation number of the operation to be
                triggered
                ''',
                'triggered_op_id',
                'Cisco-IOS-XR-man-ipsla-cfg', False),
            ],
            'Cisco-IOS-XR-man-ipsla-cfg',
            'reaction-trigger',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-man-ipsla-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_ipsla_cfg',
        ),
    },
    'Ipsla.Operation.ReactionTriggers' : {
        'meta_info' : _MetaInfoClass('Ipsla.Operation.ReactionTriggers', REFERENCE_CLASS,
            '''Reaction trigger configuration''',
            False, 
            [
            _MetaInfoClassMember('reaction-trigger', REFERENCE_LIST, 'ReactionTrigger', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_ipsla_cfg', 'Ipsla.Operation.ReactionTriggers.ReactionTrigger',
                [], [],
                '''                Reaction trigger for an operation
                ''',
                'reaction_trigger',
                'Cisco-IOS-XR-man-ipsla-cfg', False),
            ],
            'Cisco-IOS-XR-man-ipsla-cfg',
            'reaction-triggers',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-man-ipsla-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_ipsla_cfg',
        ),
    },
    'Ipsla.Operation.Definitions.Definition.OperationType.IcmpEcho.DataSize' : {
        'meta_info' : _MetaInfoClass('Ipsla.Operation.Definitions.Definition.OperationType.IcmpEcho.DataSize', REFERENCE_CLASS,
            '''Protocol data size in payload of probe
packets''',
            False, 
            [
            _MetaInfoClassMember('request', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('0', '16384')], [],
                '''                Payload size in request probe packet
                ''',
                'request',
                'Cisco-IOS-XR-man-ipsla-cfg', False, default_value="36"),
            ],
            'Cisco-IOS-XR-man-ipsla-cfg',
            'data-size',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-man-ipsla-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_ipsla_cfg',
        ),
    },
    'Ipsla.Operation.Definitions.Definition.OperationType.IcmpEcho.Statistics' : {
        'meta_info' : _MetaInfoClass('Ipsla.Operation.Definitions.Definition.OperationType.IcmpEcho.Statistics', REFERENCE_CLASS,
            '''Statistics collection aggregated over an hour''',
            False, 
            [
            _MetaInfoClassMember('hours', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('0', '25')], [],
                '''                Number of hours for which hourly statistics are
                kept
                ''',
                'hours',
                'Cisco-IOS-XR-man-ipsla-cfg', False, default_value="2"),
            _MetaInfoClassMember('dist-interval', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('1', '100')], [],
                '''                Specify distribution interval in milliseconds
                ''',
                'dist_interval',
                'Cisco-IOS-XR-man-ipsla-cfg', False, default_value="20"),
            _MetaInfoClassMember('dist-count', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('1', '20')], [],
                '''                Count of distribution intervals maintained
                ''',
                'dist_count',
                'Cisco-IOS-XR-man-ipsla-cfg', False, default_value="1"),
            ],
            'Cisco-IOS-XR-man-ipsla-cfg',
            'statistics',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-man-ipsla-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_ipsla_cfg',
        ),
    },
    'Ipsla.Operation.Definitions.Definition.OperationType.IcmpEcho.History' : {
        'meta_info' : _MetaInfoClass('Ipsla.Operation.Definitions.Definition.OperationType.IcmpEcho.History', REFERENCE_CLASS,
            '''Configure the history parameters for this
operation''',
            False, 
            [
            _MetaInfoClassMember('lives', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('0', '2')], [],
                '''                Specify number of lives to be kept
                ''',
                'lives',
                'Cisco-IOS-XR-man-ipsla-cfg', False, default_value="0"),
            _MetaInfoClassMember('history-filter', REFERENCE_ENUM_CLASS, 'IpslaHistoryFilter', 'Ipsla-history-filter',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_ipsla_cfg', 'IpslaHistoryFilter',
                [], [],
                '''                Choose type of data to be stored in history
                buffer
                ''',
                'history_filter',
                'Cisco-IOS-XR-man-ipsla-cfg', False),
            _MetaInfoClassMember('buckets', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('1', '60')], [],
                '''                Specify number of history buckets
                ''',
                'buckets',
                'Cisco-IOS-XR-man-ipsla-cfg', False, default_value="15"),
            ],
            'Cisco-IOS-XR-man-ipsla-cfg',
            'history',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-man-ipsla-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_ipsla_cfg',
        ),
    },
    'Ipsla.Operation.Definitions.Definition.OperationType.IcmpEcho.EnhancedStats.EnhancedStat' : {
        'meta_info' : _MetaInfoClass('Ipsla.Operation.Definitions.Definition.OperationType.IcmpEcho.EnhancedStats.EnhancedStat', REFERENCE_LIST,
            '''Statistics for a specified time interval''',
            False, 
            [
            _MetaInfoClassMember('interval', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('1', '3600')], [],
                '''                Interval in seconds
                ''',
                'interval',
                'Cisco-IOS-XR-man-ipsla-cfg', True),
            _MetaInfoClassMember('buckets', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('1', '100')], [],
                '''                Buckets of enhanced statistics kept
                ''',
                'buckets',
                'Cisco-IOS-XR-man-ipsla-cfg', False, default_value="15"),
            ],
            'Cisco-IOS-XR-man-ipsla-cfg',
            'enhanced-stat',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-man-ipsla-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_ipsla_cfg',
        ),
    },
    'Ipsla.Operation.Definitions.Definition.OperationType.IcmpEcho.EnhancedStats' : {
        'meta_info' : _MetaInfoClass('Ipsla.Operation.Definitions.Definition.OperationType.IcmpEcho.EnhancedStats', REFERENCE_CLASS,
            '''Table of statistics collection intervals''',
            False, 
            [
            _MetaInfoClassMember('enhanced-stat', REFERENCE_LIST, 'EnhancedStat', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_ipsla_cfg', 'Ipsla.Operation.Definitions.Definition.OperationType.IcmpEcho.EnhancedStats.EnhancedStat',
                [], [],
                '''                Statistics for a specified time interval
                ''',
                'enhanced_stat',
                'Cisco-IOS-XR-man-ipsla-cfg', False),
            ],
            'Cisco-IOS-XR-man-ipsla-cfg',
            'enhanced-stats',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-man-ipsla-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_ipsla_cfg',
        ),
    },
    'Ipsla.Operation.Definitions.Definition.OperationType.IcmpEcho' : {
        'meta_info' : _MetaInfoClass('Ipsla.Operation.Definitions.Definition.OperationType.IcmpEcho', REFERENCE_CLASS,
            '''ICMPEcho Operation type''',
            False, 
            [
            _MetaInfoClassMember('data-size', REFERENCE_CLASS, 'DataSize', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_ipsla_cfg', 'Ipsla.Operation.Definitions.Definition.OperationType.IcmpEcho.DataSize',
                [], [],
                '''                Protocol data size in payload of probe
                packets
                ''',
                'data_size',
                'Cisco-IOS-XR-man-ipsla-cfg', False),
            _MetaInfoClassMember('source-address-v6', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                Enter IPv6 address of the source device
                ''',
                'source_address_v6',
                'Cisco-IOS-XR-man-ipsla-cfg', False),
            _MetaInfoClassMember('dest-address-v6', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                Enter IPv6 address of the destination
                device
                ''',
                'dest_address_v6',
                'Cisco-IOS-XR-man-ipsla-cfg', False),
            _MetaInfoClassMember('source-address', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                Enter IPv4 address of the source device
                ''',
                'source_address',
                'Cisco-IOS-XR-man-ipsla-cfg', False),
            _MetaInfoClassMember('tos', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('0', '255')], [],
                '''                Type of service setting in probe packet
                ''',
                'tos',
                'Cisco-IOS-XR-man-ipsla-cfg', False, default_value="0"),
            _MetaInfoClassMember('statistics', REFERENCE_CLASS, 'Statistics', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_ipsla_cfg', 'Ipsla.Operation.Definitions.Definition.OperationType.IcmpEcho.Statistics',
                [], [],
                '''                Statistics collection aggregated over an hour
                ''',
                'statistics',
                'Cisco-IOS-XR-man-ipsla-cfg', False),
            _MetaInfoClassMember('vrf', ATTRIBUTE, 'str', 'xr:Cisco-ios-xr-string',
                None, None,
                [(1, 32)], [],
                '''                Configure IPSLA for a VPN Routing/Forwarding
                instance)
                ''',
                'vrf',
                'Cisco-IOS-XR-man-ipsla-cfg', False),
            _MetaInfoClassMember('history', REFERENCE_CLASS, 'History', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_ipsla_cfg', 'Ipsla.Operation.Definitions.Definition.OperationType.IcmpEcho.History',
                [], [],
                '''                Configure the history parameters for this
                operation
                ''',
                'history',
                'Cisco-IOS-XR-man-ipsla-cfg', False),
            _MetaInfoClassMember('timeout', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('1', '604800000')], [],
                '''                Probe/Control timeout in milliseconds
                ''',
                'timeout',
                'Cisco-IOS-XR-man-ipsla-cfg', False, default_value="5000"),
            _MetaInfoClassMember('frequency', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('1', '604800')], [],
                '''                Probe interval in seconds
                ''',
                'frequency',
                'Cisco-IOS-XR-man-ipsla-cfg', False, default_value="60"),
            _MetaInfoClassMember('dest-address', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                Enter IPv4 address of the destination device
                ''',
                'dest_address',
                'Cisco-IOS-XR-man-ipsla-cfg', False),
            _MetaInfoClassMember('enhanced-stats', REFERENCE_CLASS, 'EnhancedStats', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_ipsla_cfg', 'Ipsla.Operation.Definitions.Definition.OperationType.IcmpEcho.EnhancedStats',
                [], [],
                '''                Table of statistics collection intervals
                ''',
                'enhanced_stats',
                'Cisco-IOS-XR-man-ipsla-cfg', False),
            _MetaInfoClassMember('tag', ATTRIBUTE, 'str', 'string',
                None, None,
                [(1, 100)], [],
                '''                Add a tag for this operation
                ''',
                'tag',
                'Cisco-IOS-XR-man-ipsla-cfg', False),
            ],
            'Cisco-IOS-XR-man-ipsla-cfg',
            'icmp-echo',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-man-ipsla-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_ipsla_cfg',
            is_presence=True,
        ),
    },
    'Ipsla.Operation.Definitions.Definition.OperationType.MplsLspPing.DataSize' : {
        'meta_info' : _MetaInfoClass('Ipsla.Operation.Definitions.Definition.OperationType.MplsLspPing.DataSize', REFERENCE_CLASS,
            '''Protocol data size in payload of probe
packets''',
            False, 
            [
            _MetaInfoClassMember('request', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('100', '17986')], [],
                '''                Payload size in request probe packet
                ''',
                'request',
                'Cisco-IOS-XR-man-ipsla-cfg', False, default_value="100"),
            ],
            'Cisco-IOS-XR-man-ipsla-cfg',
            'data-size',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-man-ipsla-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_ipsla_cfg',
        ),
    },
    'Ipsla.Operation.Definitions.Definition.OperationType.MplsLspPing.Reply' : {
        'meta_info' : _MetaInfoClass('Ipsla.Operation.Definitions.Definition.OperationType.MplsLspPing.Reply', REFERENCE_CLASS,
            '''Echo reply options for the MPLS LSP
operation''',
            False, 
            [
            _MetaInfoClassMember('mode', REFERENCE_ENUM_CLASS, 'IpslaLspPingReplyMode', 'Ipsla-lsp-ping-reply-mode',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_ipsla_cfg', 'IpslaLspPingReplyMode',
                [], [],
                '''                Enables use of router alert in echo reply
                packets
                ''',
                'mode',
                'Cisco-IOS-XR-man-ipsla-cfg', False),
            _MetaInfoClassMember('dscp-bits', REFERENCE_UNION, 'str', 'Ipsla-lsp-reply-dscp',
                None, None,
                [], [],
                '''                DSCP bits in the reply IP header
                ''',
                'dscp_bits',
                'Cisco-IOS-XR-man-ipsla-cfg', False, [
                    _MetaInfoClassMember('dscp-bits', REFERENCE_ENUM_CLASS, 'IpslaLspReplyDscp', 'enumeration',
                        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_ipsla_cfg', 'IpslaLspReplyDscp',
                        [], [],
                        '''                        DSCP bits in the reply IP header
                        ''',
                        'dscp_bits',
                        'Cisco-IOS-XR-man-ipsla-cfg', False),
                    _MetaInfoClassMember('dscp-bits', ATTRIBUTE, 'int', 'uint32',
                        None, None,
                        [('0', '63')], [],
                        '''                        DSCP bits in the reply IP header
                        ''',
                        'dscp_bits',
                        'Cisco-IOS-XR-man-ipsla-cfg', False),
                ]),
            ],
            'Cisco-IOS-XR-man-ipsla-cfg',
            'reply',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-man-ipsla-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_ipsla_cfg',
        ),
    },
    'Ipsla.Operation.Definitions.Definition.OperationType.MplsLspPing.Target.TrafficEngineering' : {
        'meta_info' : _MetaInfoClass('Ipsla.Operation.Definitions.Definition.OperationType.MplsLspPing.Target.TrafficEngineering', REFERENCE_CLASS,
            '''Traffic engineering target''',
            False, 
            [
            _MetaInfoClassMember('tunnel', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('0', '65535')], [],
                '''                Tunnel interface number
                ''',
                'tunnel',
                'Cisco-IOS-XR-man-ipsla-cfg', False),
            ],
            'Cisco-IOS-XR-man-ipsla-cfg',
            'traffic-engineering',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-man-ipsla-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_ipsla_cfg',
        ),
    },
    'Ipsla.Operation.Definitions.Definition.OperationType.MplsLspPing.Target.Ipv4.FecAddress' : {
        'meta_info' : _MetaInfoClass('Ipsla.Operation.Definitions.Definition.OperationType.MplsLspPing.Target.Ipv4.FecAddress', REFERENCE_CLASS,
            '''Target FEC address with mask''',
            False, 
            [
            _MetaInfoClassMember('address', ATTRIBUTE, 'str', 'inet:ipv4-address-no-zone',
                None, None,
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'],
                '''                IP address for target
                ''',
                'address',
                'Cisco-IOS-XR-man-ipsla-cfg', False, is_mandatory=True),
            _MetaInfoClassMember('mask', ATTRIBUTE, 'str', 'inet:ipv4-address-no-zone',
                None, None,
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'],
                '''                IP netmask for target
                ''',
                'mask',
                'Cisco-IOS-XR-man-ipsla-cfg', False, is_mandatory=True),
            ],
            'Cisco-IOS-XR-man-ipsla-cfg',
            'fec-address',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-man-ipsla-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_ipsla_cfg',
            is_presence=True,
        ),
    },
    'Ipsla.Operation.Definitions.Definition.OperationType.MplsLspPing.Target.Ipv4' : {
        'meta_info' : _MetaInfoClass('Ipsla.Operation.Definitions.Definition.OperationType.MplsLspPing.Target.Ipv4', REFERENCE_CLASS,
            '''Target specified as an IPv4 address''',
            False, 
            [
            _MetaInfoClassMember('fec-address', REFERENCE_CLASS, 'FecAddress', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_ipsla_cfg', 'Ipsla.Operation.Definitions.Definition.OperationType.MplsLspPing.Target.Ipv4.FecAddress',
                [], [],
                '''                Target FEC address with mask
                ''',
                'fec_address',
                'Cisco-IOS-XR-man-ipsla-cfg', False, is_presence=True),
            ],
            'Cisco-IOS-XR-man-ipsla-cfg',
            'ipv4',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-man-ipsla-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_ipsla_cfg',
        ),
    },
    'Ipsla.Operation.Definitions.Definition.OperationType.MplsLspPing.Target.Pseudowire.TargetAddress' : {
        'meta_info' : _MetaInfoClass('Ipsla.Operation.Definitions.Definition.OperationType.MplsLspPing.Target.Pseudowire.TargetAddress', REFERENCE_CLASS,
            '''Target address''',
            False, 
            [
            _MetaInfoClassMember('address', ATTRIBUTE, 'str', 'inet:ipv4-address-no-zone',
                None, None,
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'],
                '''                Target address
                ''',
                'address',
                'Cisco-IOS-XR-man-ipsla-cfg', False, is_mandatory=True),
            _MetaInfoClassMember('vc-id', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('1', '4294967295')], [],
                '''                Virtual circuit ID
                ''',
                'vc_id',
                'Cisco-IOS-XR-man-ipsla-cfg', False, is_mandatory=True),
            ],
            'Cisco-IOS-XR-man-ipsla-cfg',
            'target-address',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-man-ipsla-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_ipsla_cfg',
            is_presence=True,
        ),
    },
    'Ipsla.Operation.Definitions.Definition.OperationType.MplsLspPing.Target.Pseudowire' : {
        'meta_info' : _MetaInfoClass('Ipsla.Operation.Definitions.Definition.OperationType.MplsLspPing.Target.Pseudowire', REFERENCE_CLASS,
            '''Pseudowire target''',
            False, 
            [
            _MetaInfoClassMember('target-address', REFERENCE_CLASS, 'TargetAddress', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_ipsla_cfg', 'Ipsla.Operation.Definitions.Definition.OperationType.MplsLspPing.Target.Pseudowire.TargetAddress',
                [], [],
                '''                Target address
                ''',
                'target_address',
                'Cisco-IOS-XR-man-ipsla-cfg', False, is_presence=True),
            ],
            'Cisco-IOS-XR-man-ipsla-cfg',
            'pseudowire',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-man-ipsla-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_ipsla_cfg',
        ),
    },
    'Ipsla.Operation.Definitions.Definition.OperationType.MplsLspPing.Target' : {
        'meta_info' : _MetaInfoClass('Ipsla.Operation.Definitions.Definition.OperationType.MplsLspPing.Target', REFERENCE_CLASS,
            '''Target for the MPLS LSP operation''',
            False, 
            [
            _MetaInfoClassMember('traffic-engineering', REFERENCE_CLASS, 'TrafficEngineering', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_ipsla_cfg', 'Ipsla.Operation.Definitions.Definition.OperationType.MplsLspPing.Target.TrafficEngineering',
                [], [],
                '''                Traffic engineering target
                ''',
                'traffic_engineering',
                'Cisco-IOS-XR-man-ipsla-cfg', False),
            _MetaInfoClassMember('ipv4', REFERENCE_CLASS, 'Ipv4', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_ipsla_cfg', 'Ipsla.Operation.Definitions.Definition.OperationType.MplsLspPing.Target.Ipv4',
                [], [],
                '''                Target specified as an IPv4 address
                ''',
                'ipv4',
                'Cisco-IOS-XR-man-ipsla-cfg', False),
            _MetaInfoClassMember('pseudowire', REFERENCE_CLASS, 'Pseudowire', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_ipsla_cfg', 'Ipsla.Operation.Definitions.Definition.OperationType.MplsLspPing.Target.Pseudowire',
                [], [],
                '''                Pseudowire target
                ''',
                'pseudowire',
                'Cisco-IOS-XR-man-ipsla-cfg', False),
            ],
            'Cisco-IOS-XR-man-ipsla-cfg',
            'target',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-man-ipsla-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_ipsla_cfg',
        ),
    },
    'Ipsla.Operation.Definitions.Definition.OperationType.MplsLspPing.Statistics' : {
        'meta_info' : _MetaInfoClass('Ipsla.Operation.Definitions.Definition.OperationType.MplsLspPing.Statistics', REFERENCE_CLASS,
            '''Statistics collection aggregated over an hour''',
            False, 
            [
            _MetaInfoClassMember('hours', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('0', '25')], [],
                '''                Number of hours for which hourly statistics are
                kept
                ''',
                'hours',
                'Cisco-IOS-XR-man-ipsla-cfg', False, default_value="2"),
            _MetaInfoClassMember('dist-interval', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('1', '100')], [],
                '''                Specify distribution interval in milliseconds
                ''',
                'dist_interval',
                'Cisco-IOS-XR-man-ipsla-cfg', False, default_value="20"),
            _MetaInfoClassMember('dist-count', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('1', '20')], [],
                '''                Count of distribution intervals maintained
                ''',
                'dist_count',
                'Cisco-IOS-XR-man-ipsla-cfg', False, default_value="1"),
            ],
            'Cisco-IOS-XR-man-ipsla-cfg',
            'statistics',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-man-ipsla-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_ipsla_cfg',
        ),
    },
    'Ipsla.Operation.Definitions.Definition.OperationType.MplsLspPing.History' : {
        'meta_info' : _MetaInfoClass('Ipsla.Operation.Definitions.Definition.OperationType.MplsLspPing.History', REFERENCE_CLASS,
            '''Configure the history parameters for this
operation''',
            False, 
            [
            _MetaInfoClassMember('lives', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('0', '2')], [],
                '''                Specify number of lives to be kept
                ''',
                'lives',
                'Cisco-IOS-XR-man-ipsla-cfg', False, default_value="0"),
            _MetaInfoClassMember('history-filter', REFERENCE_ENUM_CLASS, 'IpslaHistoryFilter', 'Ipsla-history-filter',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_ipsla_cfg', 'IpslaHistoryFilter',
                [], [],
                '''                Choose type of data to be stored in history
                buffer
                ''',
                'history_filter',
                'Cisco-IOS-XR-man-ipsla-cfg', False),
            _MetaInfoClassMember('buckets', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('1', '60')], [],
                '''                Specify number of history buckets
                ''',
                'buckets',
                'Cisco-IOS-XR-man-ipsla-cfg', False, default_value="15"),
            ],
            'Cisco-IOS-XR-man-ipsla-cfg',
            'history',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-man-ipsla-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_ipsla_cfg',
        ),
    },
    'Ipsla.Operation.Definitions.Definition.OperationType.MplsLspPing.EnhancedStats.EnhancedStat' : {
        'meta_info' : _MetaInfoClass('Ipsla.Operation.Definitions.Definition.OperationType.MplsLspPing.EnhancedStats.EnhancedStat', REFERENCE_LIST,
            '''Statistics for a specified time interval''',
            False, 
            [
            _MetaInfoClassMember('interval', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('1', '3600')], [],
                '''                Interval in seconds
                ''',
                'interval',
                'Cisco-IOS-XR-man-ipsla-cfg', True),
            _MetaInfoClassMember('buckets', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('1', '100')], [],
                '''                Buckets of enhanced statistics kept
                ''',
                'buckets',
                'Cisco-IOS-XR-man-ipsla-cfg', False, default_value="15"),
            ],
            'Cisco-IOS-XR-man-ipsla-cfg',
            'enhanced-stat',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-man-ipsla-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_ipsla_cfg',
        ),
    },
    'Ipsla.Operation.Definitions.Definition.OperationType.MplsLspPing.EnhancedStats' : {
        'meta_info' : _MetaInfoClass('Ipsla.Operation.Definitions.Definition.OperationType.MplsLspPing.EnhancedStats', REFERENCE_CLASS,
            '''Table of statistics collection intervals''',
            False, 
            [
            _MetaInfoClassMember('enhanced-stat', REFERENCE_LIST, 'EnhancedStat', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_ipsla_cfg', 'Ipsla.Operation.Definitions.Definition.OperationType.MplsLspPing.EnhancedStats.EnhancedStat',
                [], [],
                '''                Statistics for a specified time interval
                ''',
                'enhanced_stat',
                'Cisco-IOS-XR-man-ipsla-cfg', False),
            ],
            'Cisco-IOS-XR-man-ipsla-cfg',
            'enhanced-stats',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-man-ipsla-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_ipsla_cfg',
        ),
    },
    'Ipsla.Operation.Definitions.Definition.OperationType.MplsLspPing' : {
        'meta_info' : _MetaInfoClass('Ipsla.Operation.Definitions.Definition.OperationType.MplsLspPing', REFERENCE_CLASS,
            '''MPLS LSP Ping Operation type''',
            False, 
            [
            _MetaInfoClassMember('data-size', REFERENCE_CLASS, 'DataSize', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_ipsla_cfg', 'Ipsla.Operation.Definitions.Definition.OperationType.MplsLspPing.DataSize',
                [], [],
                '''                Protocol data size in payload of probe
                packets
                ''',
                'data_size',
                'Cisco-IOS-XR-man-ipsla-cfg', False),
            _MetaInfoClassMember('reply', REFERENCE_CLASS, 'Reply', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_ipsla_cfg', 'Ipsla.Operation.Definitions.Definition.OperationType.MplsLspPing.Reply',
                [], [],
                '''                Echo reply options for the MPLS LSP
                operation
                ''',
                'reply',
                'Cisco-IOS-XR-man-ipsla-cfg', False),
            _MetaInfoClassMember('target', REFERENCE_CLASS, 'Target', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_ipsla_cfg', 'Ipsla.Operation.Definitions.Definition.OperationType.MplsLspPing.Target',
                [], [],
                '''                Target for the MPLS LSP operation
                ''',
                'target',
                'Cisco-IOS-XR-man-ipsla-cfg', False),
            _MetaInfoClassMember('ttl', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('1', '255')], [],
                '''                Time to live value
                ''',
                'ttl',
                'Cisco-IOS-XR-man-ipsla-cfg', False, default_value="255"),
            _MetaInfoClassMember('source-address', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                Enter IPv4 address of the source device
                ''',
                'source_address',
                'Cisco-IOS-XR-man-ipsla-cfg', False),
            _MetaInfoClassMember('output-nexthop', ATTRIBUTE, 'str', 'inet:ipv4-address-no-zone',
                None, None,
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'],
                '''                Echo request output nexthop
                ''',
                'output_nexthop',
                'Cisco-IOS-XR-man-ipsla-cfg', False),
            _MetaInfoClassMember('lsp-selector', ATTRIBUTE, 'str', 'inet:ipv4-address-no-zone',
                None, None,
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'],
                '''                Attributes used for path selection during LSP
                load balancing
                ''',
                'lsp_selector',
                'Cisco-IOS-XR-man-ipsla-cfg', False, default_value="'1.0.0.127'"),
            _MetaInfoClassMember('statistics', REFERENCE_CLASS, 'Statistics', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_ipsla_cfg', 'Ipsla.Operation.Definitions.Definition.OperationType.MplsLspPing.Statistics',
                [], [],
                '''                Statistics collection aggregated over an hour
                ''',
                'statistics',
                'Cisco-IOS-XR-man-ipsla-cfg', False),
            _MetaInfoClassMember('exp-bits', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('0', '7')], [],
                '''                EXP bits in MPLS LSP echo reply header
                ''',
                'exp_bits',
                'Cisco-IOS-XR-man-ipsla-cfg', False, default_value="0"),
            _MetaInfoClassMember('force-explicit-null', ATTRIBUTE, 'Empty', 'empty',
                None, None,
                [], [],
                '''                Forced option for the MPLS LSP operation
                ''',
                'force_explicit_null',
                'Cisco-IOS-XR-man-ipsla-cfg', False),
            _MetaInfoClassMember('history', REFERENCE_CLASS, 'History', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_ipsla_cfg', 'Ipsla.Operation.Definitions.Definition.OperationType.MplsLspPing.History',
                [], [],
                '''                Configure the history parameters for this
                operation
                ''',
                'history',
                'Cisco-IOS-XR-man-ipsla-cfg', False),
            _MetaInfoClassMember('timeout', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('1', '604800000')], [],
                '''                Probe/Control timeout in milliseconds
                ''',
                'timeout',
                'Cisco-IOS-XR-man-ipsla-cfg', False, default_value="5000"),
            _MetaInfoClassMember('output-interface', ATTRIBUTE, 'str', 'xr:Interface-name',
                None, None,
                [], [b'[a-zA-Z0-9._/-]+'],
                '''                Echo request output interface
                ''',
                'output_interface',
                'Cisco-IOS-XR-man-ipsla-cfg', False),
            _MetaInfoClassMember('frequency', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('1', '604800')], [],
                '''                Probe interval in seconds
                ''',
                'frequency',
                'Cisco-IOS-XR-man-ipsla-cfg', False, default_value="60"),
            _MetaInfoClassMember('enhanced-stats', REFERENCE_CLASS, 'EnhancedStats', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_ipsla_cfg', 'Ipsla.Operation.Definitions.Definition.OperationType.MplsLspPing.EnhancedStats',
                [], [],
                '''                Table of statistics collection intervals
                ''',
                'enhanced_stats',
                'Cisco-IOS-XR-man-ipsla-cfg', False),
            _MetaInfoClassMember('tag', ATTRIBUTE, 'str', 'string',
                None, None,
                [(1, 100)], [],
                '''                Add a tag for this operation
                ''',
                'tag',
                'Cisco-IOS-XR-man-ipsla-cfg', False),
            ],
            'Cisco-IOS-XR-man-ipsla-cfg',
            'mpls-lsp-ping',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-man-ipsla-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_ipsla_cfg',
            is_presence=True,
        ),
    },
    'Ipsla.Operation.Definitions.Definition.OperationType.UdpEcho.DataSize' : {
        'meta_info' : _MetaInfoClass('Ipsla.Operation.Definitions.Definition.OperationType.UdpEcho.DataSize', REFERENCE_CLASS,
            '''Protocol data size in payload of probe
packets''',
            False, 
            [
            _MetaInfoClassMember('request', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('16', '1500')], [],
                '''                Payload size in request probe packet
                ''',
                'request',
                'Cisco-IOS-XR-man-ipsla-cfg', False, default_value="16"),
            ],
            'Cisco-IOS-XR-man-ipsla-cfg',
            'data-size',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-man-ipsla-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_ipsla_cfg',
        ),
    },
    'Ipsla.Operation.Definitions.Definition.OperationType.UdpEcho.Statistics' : {
        'meta_info' : _MetaInfoClass('Ipsla.Operation.Definitions.Definition.OperationType.UdpEcho.Statistics', REFERENCE_CLASS,
            '''Statistics collection aggregated over an hour''',
            False, 
            [
            _MetaInfoClassMember('hours', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('0', '25')], [],
                '''                Number of hours for which hourly statistics are
                kept
                ''',
                'hours',
                'Cisco-IOS-XR-man-ipsla-cfg', False, default_value="2"),
            _MetaInfoClassMember('dist-interval', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('1', '100')], [],
                '''                Specify distribution interval in milliseconds
                ''',
                'dist_interval',
                'Cisco-IOS-XR-man-ipsla-cfg', False, default_value="20"),
            _MetaInfoClassMember('dist-count', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('1', '20')], [],
                '''                Count of distribution intervals maintained
                ''',
                'dist_count',
                'Cisco-IOS-XR-man-ipsla-cfg', False, default_value="1"),
            ],
            'Cisco-IOS-XR-man-ipsla-cfg',
            'statistics',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-man-ipsla-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_ipsla_cfg',
        ),
    },
    'Ipsla.Operation.Definitions.Definition.OperationType.UdpEcho.History' : {
        'meta_info' : _MetaInfoClass('Ipsla.Operation.Definitions.Definition.OperationType.UdpEcho.History', REFERENCE_CLASS,
            '''Configure the history parameters for this
operation''',
            False, 
            [
            _MetaInfoClassMember('lives', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('0', '2')], [],
                '''                Specify number of lives to be kept
                ''',
                'lives',
                'Cisco-IOS-XR-man-ipsla-cfg', False, default_value="0"),
            _MetaInfoClassMember('history-filter', REFERENCE_ENUM_CLASS, 'IpslaHistoryFilter', 'Ipsla-history-filter',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_ipsla_cfg', 'IpslaHistoryFilter',
                [], [],
                '''                Choose type of data to be stored in history
                buffer
                ''',
                'history_filter',
                'Cisco-IOS-XR-man-ipsla-cfg', False),
            _MetaInfoClassMember('buckets', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('1', '60')], [],
                '''                Specify number of history buckets
                ''',
                'buckets',
                'Cisco-IOS-XR-man-ipsla-cfg', False, default_value="15"),
            ],
            'Cisco-IOS-XR-man-ipsla-cfg',
            'history',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-man-ipsla-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_ipsla_cfg',
        ),
    },
    'Ipsla.Operation.Definitions.Definition.OperationType.UdpEcho.EnhancedStats.EnhancedStat' : {
        'meta_info' : _MetaInfoClass('Ipsla.Operation.Definitions.Definition.OperationType.UdpEcho.EnhancedStats.EnhancedStat', REFERENCE_LIST,
            '''Statistics for a specified time interval''',
            False, 
            [
            _MetaInfoClassMember('interval', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('1', '3600')], [],
                '''                Interval in seconds
                ''',
                'interval',
                'Cisco-IOS-XR-man-ipsla-cfg', True),
            _MetaInfoClassMember('buckets', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('1', '100')], [],
                '''                Buckets of enhanced statistics kept
                ''',
                'buckets',
                'Cisco-IOS-XR-man-ipsla-cfg', False, default_value="15"),
            ],
            'Cisco-IOS-XR-man-ipsla-cfg',
            'enhanced-stat',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-man-ipsla-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_ipsla_cfg',
        ),
    },
    'Ipsla.Operation.Definitions.Definition.OperationType.UdpEcho.EnhancedStats' : {
        'meta_info' : _MetaInfoClass('Ipsla.Operation.Definitions.Definition.OperationType.UdpEcho.EnhancedStats', REFERENCE_CLASS,
            '''Table of statistics collection intervals''',
            False, 
            [
            _MetaInfoClassMember('enhanced-stat', REFERENCE_LIST, 'EnhancedStat', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_ipsla_cfg', 'Ipsla.Operation.Definitions.Definition.OperationType.UdpEcho.EnhancedStats.EnhancedStat',
                [], [],
                '''                Statistics for a specified time interval
                ''',
                'enhanced_stat',
                'Cisco-IOS-XR-man-ipsla-cfg', False),
            ],
            'Cisco-IOS-XR-man-ipsla-cfg',
            'enhanced-stats',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-man-ipsla-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_ipsla_cfg',
        ),
    },
    'Ipsla.Operation.Definitions.Definition.OperationType.UdpEcho' : {
        'meta_info' : _MetaInfoClass('Ipsla.Operation.Definitions.Definition.OperationType.UdpEcho', REFERENCE_CLASS,
            '''UDPEcho Operation type''',
            False, 
            [
            _MetaInfoClassMember('data-size', REFERENCE_CLASS, 'DataSize', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_ipsla_cfg', 'Ipsla.Operation.Definitions.Definition.OperationType.UdpEcho.DataSize',
                [], [],
                '''                Protocol data size in payload of probe
                packets
                ''',
                'data_size',
                'Cisco-IOS-XR-man-ipsla-cfg', False),
            _MetaInfoClassMember('source-address', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                Enter IPv4 address of the source device
                ''',
                'source_address',
                'Cisco-IOS-XR-man-ipsla-cfg', False),
            _MetaInfoClassMember('tos', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('0', '255')], [],
                '''                Type of service setting in probe packet
                ''',
                'tos',
                'Cisco-IOS-XR-man-ipsla-cfg', False, default_value="0"),
            _MetaInfoClassMember('control-disable', ATTRIBUTE, 'Empty', 'empty',
                None, None,
                [], [],
                '''                Disable control packets
                ''',
                'control_disable',
                'Cisco-IOS-XR-man-ipsla-cfg', False),
            _MetaInfoClassMember('source-port', ATTRIBUTE, 'int', 'inet:port-number',
                None, None,
                [('0', '65535')], [],
                '''                Port number on source device
                ''',
                'source_port',
                'Cisco-IOS-XR-man-ipsla-cfg', False),
            _MetaInfoClassMember('statistics', REFERENCE_CLASS, 'Statistics', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_ipsla_cfg', 'Ipsla.Operation.Definitions.Definition.OperationType.UdpEcho.Statistics',
                [], [],
                '''                Statistics collection aggregated over an hour
                ''',
                'statistics',
                'Cisco-IOS-XR-man-ipsla-cfg', False),
            _MetaInfoClassMember('vrf', ATTRIBUTE, 'str', 'xr:Cisco-ios-xr-string',
                None, None,
                [(1, 32)], [],
                '''                Configure IPSLA for a VPN Routing/Forwarding
                instance)
                ''',
                'vrf',
                'Cisco-IOS-XR-man-ipsla-cfg', False),
            _MetaInfoClassMember('history', REFERENCE_CLASS, 'History', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_ipsla_cfg', 'Ipsla.Operation.Definitions.Definition.OperationType.UdpEcho.History',
                [], [],
                '''                Configure the history parameters for this
                operation
                ''',
                'history',
                'Cisco-IOS-XR-man-ipsla-cfg', False),
            _MetaInfoClassMember('timeout', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('1', '604800000')], [],
                '''                Probe/Control timeout in milliseconds
                ''',
                'timeout',
                'Cisco-IOS-XR-man-ipsla-cfg', False, default_value="5000"),
            _MetaInfoClassMember('frequency', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('1', '604800')], [],
                '''                Probe interval in seconds
                ''',
                'frequency',
                'Cisco-IOS-XR-man-ipsla-cfg', False, default_value="60"),
            _MetaInfoClassMember('dest-port', ATTRIBUTE, 'int', 'inet:port-number',
                None, None,
                [('0', '65535')], [],
                '''                Port number on target device
                ''',
                'dest_port',
                'Cisco-IOS-XR-man-ipsla-cfg', False),
            _MetaInfoClassMember('verify-data', ATTRIBUTE, 'Empty', 'empty',
                None, None,
                [], [],
                '''                Check each IPSLA response for corruption
                ''',
                'verify_data',
                'Cisco-IOS-XR-man-ipsla-cfg', False),
            _MetaInfoClassMember('dest-address', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                Enter IPv4 address of the destination device
                ''',
                'dest_address',
                'Cisco-IOS-XR-man-ipsla-cfg', False),
            _MetaInfoClassMember('enhanced-stats', REFERENCE_CLASS, 'EnhancedStats', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_ipsla_cfg', 'Ipsla.Operation.Definitions.Definition.OperationType.UdpEcho.EnhancedStats',
                [], [],
                '''                Table of statistics collection intervals
                ''',
                'enhanced_stats',
                'Cisco-IOS-XR-man-ipsla-cfg', False),
            _MetaInfoClassMember('tag', ATTRIBUTE, 'str', 'string',
                None, None,
                [(1, 100)], [],
                '''                Add a tag for this operation
                ''',
                'tag',
                'Cisco-IOS-XR-man-ipsla-cfg', False),
            ],
            'Cisco-IOS-XR-man-ipsla-cfg',
            'udp-echo',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-man-ipsla-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_ipsla_cfg',
            is_presence=True,
        ),
    },
    'Ipsla.Operation.Definitions.Definition.OperationType.MplsLspTrace.Target.TrafficEngineering' : {
        'meta_info' : _MetaInfoClass('Ipsla.Operation.Definitions.Definition.OperationType.MplsLspTrace.Target.TrafficEngineering', REFERENCE_CLASS,
            '''Traffic engineering target''',
            False, 
            [
            _MetaInfoClassMember('tunnel', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('0', '65535')], [],
                '''                Tunnel interface number
                ''',
                'tunnel',
                'Cisco-IOS-XR-man-ipsla-cfg', False),
            ],
            'Cisco-IOS-XR-man-ipsla-cfg',
            'traffic-engineering',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-man-ipsla-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_ipsla_cfg',
        ),
    },
    'Ipsla.Operation.Definitions.Definition.OperationType.MplsLspTrace.Target.Ipv4.FecAddress' : {
        'meta_info' : _MetaInfoClass('Ipsla.Operation.Definitions.Definition.OperationType.MplsLspTrace.Target.Ipv4.FecAddress', REFERENCE_CLASS,
            '''Target FEC address with mask''',
            False, 
            [
            _MetaInfoClassMember('address', ATTRIBUTE, 'str', 'inet:ipv4-address-no-zone',
                None, None,
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'],
                '''                IP address for target
                ''',
                'address',
                'Cisco-IOS-XR-man-ipsla-cfg', False, is_mandatory=True),
            _MetaInfoClassMember('mask', ATTRIBUTE, 'str', 'inet:ipv4-address-no-zone',
                None, None,
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'],
                '''                IP netmask for target
                ''',
                'mask',
                'Cisco-IOS-XR-man-ipsla-cfg', False, is_mandatory=True),
            ],
            'Cisco-IOS-XR-man-ipsla-cfg',
            'fec-address',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-man-ipsla-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_ipsla_cfg',
            is_presence=True,
        ),
    },
    'Ipsla.Operation.Definitions.Definition.OperationType.MplsLspTrace.Target.Ipv4' : {
        'meta_info' : _MetaInfoClass('Ipsla.Operation.Definitions.Definition.OperationType.MplsLspTrace.Target.Ipv4', REFERENCE_CLASS,
            '''Target specified as an IPv4 address''',
            False, 
            [
            _MetaInfoClassMember('fec-address', REFERENCE_CLASS, 'FecAddress', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_ipsla_cfg', 'Ipsla.Operation.Definitions.Definition.OperationType.MplsLspTrace.Target.Ipv4.FecAddress',
                [], [],
                '''                Target FEC address with mask
                ''',
                'fec_address',
                'Cisco-IOS-XR-man-ipsla-cfg', False, is_presence=True),
            ],
            'Cisco-IOS-XR-man-ipsla-cfg',
            'ipv4',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-man-ipsla-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_ipsla_cfg',
        ),
    },
    'Ipsla.Operation.Definitions.Definition.OperationType.MplsLspTrace.Target' : {
        'meta_info' : _MetaInfoClass('Ipsla.Operation.Definitions.Definition.OperationType.MplsLspTrace.Target', REFERENCE_CLASS,
            '''Target for the MPLS LSP operation''',
            False, 
            [
            _MetaInfoClassMember('traffic-engineering', REFERENCE_CLASS, 'TrafficEngineering', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_ipsla_cfg', 'Ipsla.Operation.Definitions.Definition.OperationType.MplsLspTrace.Target.TrafficEngineering',
                [], [],
                '''                Traffic engineering target
                ''',
                'traffic_engineering',
                'Cisco-IOS-XR-man-ipsla-cfg', False),
            _MetaInfoClassMember('ipv4', REFERENCE_CLASS, 'Ipv4', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_ipsla_cfg', 'Ipsla.Operation.Definitions.Definition.OperationType.MplsLspTrace.Target.Ipv4',
                [], [],
                '''                Target specified as an IPv4 address
                ''',
                'ipv4',
                'Cisco-IOS-XR-man-ipsla-cfg', False),
            ],
            'Cisco-IOS-XR-man-ipsla-cfg',
            'target',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-man-ipsla-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_ipsla_cfg',
        ),
    },
    'Ipsla.Operation.Definitions.Definition.OperationType.MplsLspTrace.Reply' : {
        'meta_info' : _MetaInfoClass('Ipsla.Operation.Definitions.Definition.OperationType.MplsLspTrace.Reply', REFERENCE_CLASS,
            '''Echo reply options for the MPLS LSP
operation''',
            False, 
            [
            _MetaInfoClassMember('mode', REFERENCE_ENUM_CLASS, 'IpslaLspTraceReplyMode', 'Ipsla-lsp-trace-reply-mode',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_ipsla_cfg', 'IpslaLspTraceReplyMode',
                [], [],
                '''                Enables use of router alert in echo reply
                packets
                ''',
                'mode',
                'Cisco-IOS-XR-man-ipsla-cfg', False),
            _MetaInfoClassMember('dscp-bits', REFERENCE_UNION, 'str', 'Ipsla-lsp-reply-dscp',
                None, None,
                [], [],
                '''                DSCP bits in the reply IP header
                ''',
                'dscp_bits',
                'Cisco-IOS-XR-man-ipsla-cfg', False, [
                    _MetaInfoClassMember('dscp-bits', REFERENCE_ENUM_CLASS, 'IpslaLspReplyDscp', 'enumeration',
                        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_ipsla_cfg', 'IpslaLspReplyDscp',
                        [], [],
                        '''                        DSCP bits in the reply IP header
                        ''',
                        'dscp_bits',
                        'Cisco-IOS-XR-man-ipsla-cfg', False),
                    _MetaInfoClassMember('dscp-bits', ATTRIBUTE, 'int', 'uint32',
                        None, None,
                        [('0', '63')], [],
                        '''                        DSCP bits in the reply IP header
                        ''',
                        'dscp_bits',
                        'Cisco-IOS-XR-man-ipsla-cfg', False),
                ]),
            ],
            'Cisco-IOS-XR-man-ipsla-cfg',
            'reply',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-man-ipsla-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_ipsla_cfg',
        ),
    },
    'Ipsla.Operation.Definitions.Definition.OperationType.MplsLspTrace.Statistics' : {
        'meta_info' : _MetaInfoClass('Ipsla.Operation.Definitions.Definition.OperationType.MplsLspTrace.Statistics', REFERENCE_CLASS,
            '''Statistics collection aggregated over an hour''',
            False, 
            [
            _MetaInfoClassMember('hours', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('0', '25')], [],
                '''                Number of hours for which hourly statistics are
                kept
                ''',
                'hours',
                'Cisco-IOS-XR-man-ipsla-cfg', False, default_value="2"),
            _MetaInfoClassMember('dist-interval', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('1', '100')], [],
                '''                Specify distribution interval in milliseconds
                ''',
                'dist_interval',
                'Cisco-IOS-XR-man-ipsla-cfg', False, default_value="20"),
            _MetaInfoClassMember('dist-count', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('1', '20')], [],
                '''                Count of distribution intervals maintained
                ''',
                'dist_count',
                'Cisco-IOS-XR-man-ipsla-cfg', False, default_value="1"),
            ],
            'Cisco-IOS-XR-man-ipsla-cfg',
            'statistics',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-man-ipsla-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_ipsla_cfg',
        ),
    },
    'Ipsla.Operation.Definitions.Definition.OperationType.MplsLspTrace.History' : {
        'meta_info' : _MetaInfoClass('Ipsla.Operation.Definitions.Definition.OperationType.MplsLspTrace.History', REFERENCE_CLASS,
            '''Configure the history parameters for this
operation''',
            False, 
            [
            _MetaInfoClassMember('lives', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('0', '2')], [],
                '''                Specify number of lives to be kept
                ''',
                'lives',
                'Cisco-IOS-XR-man-ipsla-cfg', False, default_value="0"),
            _MetaInfoClassMember('history-filter', REFERENCE_ENUM_CLASS, 'IpslaHistoryFilter', 'Ipsla-history-filter',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_ipsla_cfg', 'IpslaHistoryFilter',
                [], [],
                '''                Choose type of data to be stored in history
                buffer
                ''',
                'history_filter',
                'Cisco-IOS-XR-man-ipsla-cfg', False),
            _MetaInfoClassMember('buckets', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('1', '60')], [],
                '''                Specify number of history buckets
                ''',
                'buckets',
                'Cisco-IOS-XR-man-ipsla-cfg', False, default_value="15"),
            ],
            'Cisco-IOS-XR-man-ipsla-cfg',
            'history',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-man-ipsla-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_ipsla_cfg',
        ),
    },
    'Ipsla.Operation.Definitions.Definition.OperationType.MplsLspTrace' : {
        'meta_info' : _MetaInfoClass('Ipsla.Operation.Definitions.Definition.OperationType.MplsLspTrace', REFERENCE_CLASS,
            '''MPLS LSP Trace Operation type''',
            False, 
            [
            _MetaInfoClassMember('target', REFERENCE_CLASS, 'Target', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_ipsla_cfg', 'Ipsla.Operation.Definitions.Definition.OperationType.MplsLspTrace.Target',
                [], [],
                '''                Target for the MPLS LSP operation
                ''',
                'target',
                'Cisco-IOS-XR-man-ipsla-cfg', False),
            _MetaInfoClassMember('reply', REFERENCE_CLASS, 'Reply', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_ipsla_cfg', 'Ipsla.Operation.Definitions.Definition.OperationType.MplsLspTrace.Reply',
                [], [],
                '''                Echo reply options for the MPLS LSP
                operation
                ''',
                'reply',
                'Cisco-IOS-XR-man-ipsla-cfg', False),
            _MetaInfoClassMember('ttl', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('1', '255')], [],
                '''                Time to live value
                ''',
                'ttl',
                'Cisco-IOS-XR-man-ipsla-cfg', False, default_value="30"),
            _MetaInfoClassMember('source-address', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                Enter IPv4 address of the source device
                ''',
                'source_address',
                'Cisco-IOS-XR-man-ipsla-cfg', False),
            _MetaInfoClassMember('output-nexthop', ATTRIBUTE, 'str', 'inet:ipv4-address-no-zone',
                None, None,
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'],
                '''                Echo request output nexthop
                ''',
                'output_nexthop',
                'Cisco-IOS-XR-man-ipsla-cfg', False),
            _MetaInfoClassMember('lsp-selector', ATTRIBUTE, 'str', 'inet:ipv4-address-no-zone',
                None, None,
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'],
                '''                Attributes used for path selection during LSP
                load balancing
                ''',
                'lsp_selector',
                'Cisco-IOS-XR-man-ipsla-cfg', False, default_value="'1.0.0.127'"),
            _MetaInfoClassMember('statistics', REFERENCE_CLASS, 'Statistics', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_ipsla_cfg', 'Ipsla.Operation.Definitions.Definition.OperationType.MplsLspTrace.Statistics',
                [], [],
                '''                Statistics collection aggregated over an hour
                ''',
                'statistics',
                'Cisco-IOS-XR-man-ipsla-cfg', False),
            _MetaInfoClassMember('exp-bits', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('0', '7')], [],
                '''                EXP bits in MPLS LSP echo reply header
                ''',
                'exp_bits',
                'Cisco-IOS-XR-man-ipsla-cfg', False, default_value="0"),
            _MetaInfoClassMember('force-explicit-null', ATTRIBUTE, 'Empty', 'empty',
                None, None,
                [], [],
                '''                Forced option for the MPLS LSP operation
                ''',
                'force_explicit_null',
                'Cisco-IOS-XR-man-ipsla-cfg', False),
            _MetaInfoClassMember('history', REFERENCE_CLASS, 'History', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_ipsla_cfg', 'Ipsla.Operation.Definitions.Definition.OperationType.MplsLspTrace.History',
                [], [],
                '''                Configure the history parameters for this
                operation
                ''',
                'history',
                'Cisco-IOS-XR-man-ipsla-cfg', False),
            _MetaInfoClassMember('timeout', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('1', '604800000')], [],
                '''                Probe/Control timeout in milliseconds
                ''',
                'timeout',
                'Cisco-IOS-XR-man-ipsla-cfg', False, default_value="5000"),
            _MetaInfoClassMember('output-interface', ATTRIBUTE, 'str', 'xr:Interface-name',
                None, None,
                [], [b'[a-zA-Z0-9._/-]+'],
                '''                Echo request output interface
                ''',
                'output_interface',
                'Cisco-IOS-XR-man-ipsla-cfg', False),
            _MetaInfoClassMember('frequency', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('1', '604800')], [],
                '''                Probe interval in seconds
                ''',
                'frequency',
                'Cisco-IOS-XR-man-ipsla-cfg', False, default_value="60"),
            _MetaInfoClassMember('tag', ATTRIBUTE, 'str', 'string',
                None, None,
                [(1, 100)], [],
                '''                Add a tag for this operation
                ''',
                'tag',
                'Cisco-IOS-XR-man-ipsla-cfg', False),
            ],
            'Cisco-IOS-XR-man-ipsla-cfg',
            'mpls-lsp-trace',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-man-ipsla-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_ipsla_cfg',
            is_presence=True,
        ),
    },
    'Ipsla.Operation.Definitions.Definition.OperationType.UdpJitter.DataSize' : {
        'meta_info' : _MetaInfoClass('Ipsla.Operation.Definitions.Definition.OperationType.UdpJitter.DataSize', REFERENCE_CLASS,
            '''Protocol data size in payload of probe
packets''',
            False, 
            [
            _MetaInfoClassMember('request', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('28', '1500')], [],
                '''                Payload size in request probe packet
                ''',
                'request',
                'Cisco-IOS-XR-man-ipsla-cfg', False, default_value="32"),
            ],
            'Cisco-IOS-XR-man-ipsla-cfg',
            'data-size',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-man-ipsla-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_ipsla_cfg',
        ),
    },
    'Ipsla.Operation.Definitions.Definition.OperationType.UdpJitter.Packet' : {
        'meta_info' : _MetaInfoClass('Ipsla.Operation.Definitions.Definition.OperationType.UdpJitter.Packet', REFERENCE_CLASS,
            '''Probe packet stream configuration
parameters''',
            False, 
            [
            _MetaInfoClassMember('count', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('1', '60000')], [],
                '''                Number of packets to be transmitted during
                a probe
                ''',
                'count',
                'Cisco-IOS-XR-man-ipsla-cfg', False, default_value="10"),
            _MetaInfoClassMember('interval', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('1', '60000')], [],
                '''                Packet interval in milliseconds
                ''',
                'interval',
                'Cisco-IOS-XR-man-ipsla-cfg', False, default_value="20"),
            ],
            'Cisco-IOS-XR-man-ipsla-cfg',
            'packet',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-man-ipsla-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_ipsla_cfg',
        ),
    },
    'Ipsla.Operation.Definitions.Definition.OperationType.UdpJitter.Statistics' : {
        'meta_info' : _MetaInfoClass('Ipsla.Operation.Definitions.Definition.OperationType.UdpJitter.Statistics', REFERENCE_CLASS,
            '''Statistics collection aggregated over an hour''',
            False, 
            [
            _MetaInfoClassMember('hours', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('0', '25')], [],
                '''                Number of hours for which hourly statistics are
                kept
                ''',
                'hours',
                'Cisco-IOS-XR-man-ipsla-cfg', False, default_value="2"),
            _MetaInfoClassMember('dist-interval', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('1', '100')], [],
                '''                Specify distribution interval in milliseconds
                ''',
                'dist_interval',
                'Cisco-IOS-XR-man-ipsla-cfg', False, default_value="20"),
            _MetaInfoClassMember('dist-count', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('1', '20')], [],
                '''                Count of distribution intervals maintained
                ''',
                'dist_count',
                'Cisco-IOS-XR-man-ipsla-cfg', False, default_value="1"),
            ],
            'Cisco-IOS-XR-man-ipsla-cfg',
            'statistics',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-man-ipsla-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_ipsla_cfg',
        ),
    },
    'Ipsla.Operation.Definitions.Definition.OperationType.UdpJitter.EnhancedStats.EnhancedStat' : {
        'meta_info' : _MetaInfoClass('Ipsla.Operation.Definitions.Definition.OperationType.UdpJitter.EnhancedStats.EnhancedStat', REFERENCE_LIST,
            '''Statistics for a specified time interval''',
            False, 
            [
            _MetaInfoClassMember('interval', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('1', '3600')], [],
                '''                Interval in seconds
                ''',
                'interval',
                'Cisco-IOS-XR-man-ipsla-cfg', True),
            _MetaInfoClassMember('buckets', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('1', '100')], [],
                '''                Buckets of enhanced statistics kept
                ''',
                'buckets',
                'Cisco-IOS-XR-man-ipsla-cfg', False, default_value="15"),
            ],
            'Cisco-IOS-XR-man-ipsla-cfg',
            'enhanced-stat',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-man-ipsla-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_ipsla_cfg',
        ),
    },
    'Ipsla.Operation.Definitions.Definition.OperationType.UdpJitter.EnhancedStats' : {
        'meta_info' : _MetaInfoClass('Ipsla.Operation.Definitions.Definition.OperationType.UdpJitter.EnhancedStats', REFERENCE_CLASS,
            '''Table of statistics collection intervals''',
            False, 
            [
            _MetaInfoClassMember('enhanced-stat', REFERENCE_LIST, 'EnhancedStat', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_ipsla_cfg', 'Ipsla.Operation.Definitions.Definition.OperationType.UdpJitter.EnhancedStats.EnhancedStat',
                [], [],
                '''                Statistics for a specified time interval
                ''',
                'enhanced_stat',
                'Cisco-IOS-XR-man-ipsla-cfg', False),
            ],
            'Cisco-IOS-XR-man-ipsla-cfg',
            'enhanced-stats',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-man-ipsla-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_ipsla_cfg',
        ),
    },
    'Ipsla.Operation.Definitions.Definition.OperationType.UdpJitter' : {
        'meta_info' : _MetaInfoClass('Ipsla.Operation.Definitions.Definition.OperationType.UdpJitter', REFERENCE_CLASS,
            '''UDPJitter Operation type''',
            False, 
            [
            _MetaInfoClassMember('data-size', REFERENCE_CLASS, 'DataSize', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_ipsla_cfg', 'Ipsla.Operation.Definitions.Definition.OperationType.UdpJitter.DataSize',
                [], [],
                '''                Protocol data size in payload of probe
                packets
                ''',
                'data_size',
                'Cisco-IOS-XR-man-ipsla-cfg', False),
            _MetaInfoClassMember('packet', REFERENCE_CLASS, 'Packet', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_ipsla_cfg', 'Ipsla.Operation.Definitions.Definition.OperationType.UdpJitter.Packet',
                [], [],
                '''                Probe packet stream configuration
                parameters
                ''',
                'packet',
                'Cisco-IOS-XR-man-ipsla-cfg', False),
            _MetaInfoClassMember('source-address', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                Enter IPv4 address of the source device
                ''',
                'source_address',
                'Cisco-IOS-XR-man-ipsla-cfg', False),
            _MetaInfoClassMember('tos', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('0', '255')], [],
                '''                Type of service setting in probe packet
                ''',
                'tos',
                'Cisco-IOS-XR-man-ipsla-cfg', False, default_value="0"),
            _MetaInfoClassMember('control-disable', ATTRIBUTE, 'Empty', 'empty',
                None, None,
                [], [],
                '''                Disable control packets
                ''',
                'control_disable',
                'Cisco-IOS-XR-man-ipsla-cfg', False),
            _MetaInfoClassMember('source-port', ATTRIBUTE, 'int', 'inet:port-number',
                None, None,
                [('0', '65535')], [],
                '''                Port number on source device
                ''',
                'source_port',
                'Cisco-IOS-XR-man-ipsla-cfg', False),
            _MetaInfoClassMember('statistics', REFERENCE_CLASS, 'Statistics', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_ipsla_cfg', 'Ipsla.Operation.Definitions.Definition.OperationType.UdpJitter.Statistics',
                [], [],
                '''                Statistics collection aggregated over an hour
                ''',
                'statistics',
                'Cisco-IOS-XR-man-ipsla-cfg', False),
            _MetaInfoClassMember('vrf', ATTRIBUTE, 'str', 'xr:Cisco-ios-xr-string',
                None, None,
                [(1, 32)], [],
                '''                Configure IPSLA for a VPN Routing/Forwarding
                instance)
                ''',
                'vrf',
                'Cisco-IOS-XR-man-ipsla-cfg', False),
            _MetaInfoClassMember('timeout', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('1', '604800000')], [],
                '''                Probe/Control timeout in milliseconds
                ''',
                'timeout',
                'Cisco-IOS-XR-man-ipsla-cfg', False, default_value="5000"),
            _MetaInfoClassMember('frequency', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('1', '604800')], [],
                '''                Probe interval in seconds
                ''',
                'frequency',
                'Cisco-IOS-XR-man-ipsla-cfg', False, default_value="60"),
            _MetaInfoClassMember('dest-port', ATTRIBUTE, 'int', 'inet:port-number',
                None, None,
                [('0', '65535')], [],
                '''                Port number on target device
                ''',
                'dest_port',
                'Cisco-IOS-XR-man-ipsla-cfg', False),
            _MetaInfoClassMember('verify-data', ATTRIBUTE, 'Empty', 'empty',
                None, None,
                [], [],
                '''                Check each IPSLA response for corruption
                ''',
                'verify_data',
                'Cisco-IOS-XR-man-ipsla-cfg', False),
            _MetaInfoClassMember('dest-address', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                Enter IPv4 address of the destination device
                ''',
                'dest_address',
                'Cisco-IOS-XR-man-ipsla-cfg', False),
            _MetaInfoClassMember('enhanced-stats', REFERENCE_CLASS, 'EnhancedStats', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_ipsla_cfg', 'Ipsla.Operation.Definitions.Definition.OperationType.UdpJitter.EnhancedStats',
                [], [],
                '''                Table of statistics collection intervals
                ''',
                'enhanced_stats',
                'Cisco-IOS-XR-man-ipsla-cfg', False),
            _MetaInfoClassMember('tag', ATTRIBUTE, 'str', 'string',
                None, None,
                [(1, 100)], [],
                '''                Add a tag for this operation
                ''',
                'tag',
                'Cisco-IOS-XR-man-ipsla-cfg', False),
            ],
            'Cisco-IOS-XR-man-ipsla-cfg',
            'udp-jitter',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-man-ipsla-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_ipsla_cfg',
            is_presence=True,
        ),
    },
    'Ipsla.Operation.Definitions.Definition.OperationType.IcmpPathEcho.History' : {
        'meta_info' : _MetaInfoClass('Ipsla.Operation.Definitions.Definition.OperationType.IcmpPathEcho.History', REFERENCE_CLASS,
            '''Configure the history parameters for this
operation''',
            False, 
            [
            _MetaInfoClassMember('samples', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('1', '30')], [],
                '''                Specify number of samples to keep
                ''',
                'samples',
                'Cisco-IOS-XR-man-ipsla-cfg', False, default_value="16"),
            _MetaInfoClassMember('buckets', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('1', '60')], [],
                '''                Specify number of history buckets
                ''',
                'buckets',
                'Cisco-IOS-XR-man-ipsla-cfg', False, default_value="15"),
            _MetaInfoClassMember('history-filter', REFERENCE_ENUM_CLASS, 'IpslaHistoryFilter', 'Ipsla-history-filter',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_ipsla_cfg', 'IpslaHistoryFilter',
                [], [],
                '''                Choose type of data to be stored in
                history buffer
                ''',
                'history_filter',
                'Cisco-IOS-XR-man-ipsla-cfg', False),
            _MetaInfoClassMember('lives', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('0', '2')], [],
                '''                Specify number of lives to be kept
                ''',
                'lives',
                'Cisco-IOS-XR-man-ipsla-cfg', False, default_value="0"),
            ],
            'Cisco-IOS-XR-man-ipsla-cfg',
            'history',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-man-ipsla-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_ipsla_cfg',
        ),
    },
    'Ipsla.Operation.Definitions.Definition.OperationType.IcmpPathEcho.DataSize' : {
        'meta_info' : _MetaInfoClass('Ipsla.Operation.Definitions.Definition.OperationType.IcmpPathEcho.DataSize', REFERENCE_CLASS,
            '''Protocol data size in payload of probe
packets''',
            False, 
            [
            _MetaInfoClassMember('request', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('0', '16384')], [],
                '''                Payload size in request probe packet
                ''',
                'request',
                'Cisco-IOS-XR-man-ipsla-cfg', False, default_value="36"),
            ],
            'Cisco-IOS-XR-man-ipsla-cfg',
            'data-size',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-man-ipsla-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_ipsla_cfg',
        ),
    },
    'Ipsla.Operation.Definitions.Definition.OperationType.IcmpPathEcho.Statistics' : {
        'meta_info' : _MetaInfoClass('Ipsla.Operation.Definitions.Definition.OperationType.IcmpPathEcho.Statistics', REFERENCE_CLASS,
            '''Statistics collection aggregated over an
hour''',
            False, 
            [
            _MetaInfoClassMember('paths', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('1', '128')], [],
                '''                Maximum number of paths for which
                statistics are kept
                ''',
                'paths',
                'Cisco-IOS-XR-man-ipsla-cfg', False, default_value="5"),
            _MetaInfoClassMember('dist-interval', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('1', '100')], [],
                '''                Specify distribution interval in
                milliseconds
                ''',
                'dist_interval',
                'Cisco-IOS-XR-man-ipsla-cfg', False, default_value="20"),
            _MetaInfoClassMember('dist-count', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('1', '20')], [],
                '''                Count of distribution intervals maintained
                ''',
                'dist_count',
                'Cisco-IOS-XR-man-ipsla-cfg', False, default_value="1"),
            _MetaInfoClassMember('hours', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('0', '25')], [],
                '''                Number of hours for which hourly
                statistics are kept
                ''',
                'hours',
                'Cisco-IOS-XR-man-ipsla-cfg', False, default_value="2"),
            _MetaInfoClassMember('hops', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('1', '30')], [],
                '''                Maximum hops per path for which statistics
                are kept
                ''',
                'hops',
                'Cisco-IOS-XR-man-ipsla-cfg', False, default_value="16"),
            ],
            'Cisco-IOS-XR-man-ipsla-cfg',
            'statistics',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-man-ipsla-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_ipsla_cfg',
        ),
    },
    'Ipsla.Operation.Definitions.Definition.OperationType.IcmpPathEcho.LsrPath' : {
        'meta_info' : _MetaInfoClass('Ipsla.Operation.Definitions.Definition.OperationType.IcmpPathEcho.LsrPath', REFERENCE_CLASS,
            '''Loose source routing path (up to 8 intermediate
nodes)''',
            False, 
            [
            _MetaInfoClassMember('node1', ATTRIBUTE, 'str', 'inet:ipv4-address-no-zone',
                None, None,
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'],
                '''                IPv4 address of the intermediate node
                ''',
                'node1',
                'Cisco-IOS-XR-man-ipsla-cfg', False, is_mandatory=True),
            _MetaInfoClassMember('node2', ATTRIBUTE, 'str', 'inet:ipv4-address-no-zone',
                None, None,
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'],
                '''                IPv4 address of the intermediate node
                ''',
                'node2',
                'Cisco-IOS-XR-man-ipsla-cfg', False),
            _MetaInfoClassMember('node3', ATTRIBUTE, 'str', 'inet:ipv4-address-no-zone',
                None, None,
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'],
                '''                IPv4 address of the intermediate node
                ''',
                'node3',
                'Cisco-IOS-XR-man-ipsla-cfg', False),
            _MetaInfoClassMember('node4', ATTRIBUTE, 'str', 'inet:ipv4-address-no-zone',
                None, None,
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'],
                '''                IPv4 address of the intermediate node
                ''',
                'node4',
                'Cisco-IOS-XR-man-ipsla-cfg', False),
            _MetaInfoClassMember('node5', ATTRIBUTE, 'str', 'inet:ipv4-address-no-zone',
                None, None,
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'],
                '''                IPv4 address of the intermediate node
                ''',
                'node5',
                'Cisco-IOS-XR-man-ipsla-cfg', False),
            _MetaInfoClassMember('node6', ATTRIBUTE, 'str', 'inet:ipv4-address-no-zone',
                None, None,
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'],
                '''                IPv4 address of the intermediate node
                ''',
                'node6',
                'Cisco-IOS-XR-man-ipsla-cfg', False),
            _MetaInfoClassMember('node7', ATTRIBUTE, 'str', 'inet:ipv4-address-no-zone',
                None, None,
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'],
                '''                IPv4 address of the intermediate node
                ''',
                'node7',
                'Cisco-IOS-XR-man-ipsla-cfg', False),
            _MetaInfoClassMember('node8', ATTRIBUTE, 'str', 'inet:ipv4-address-no-zone',
                None, None,
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'],
                '''                IPv4 address of the intermediate node
                ''',
                'node8',
                'Cisco-IOS-XR-man-ipsla-cfg', False),
            ],
            'Cisco-IOS-XR-man-ipsla-cfg',
            'lsr-path',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-man-ipsla-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_ipsla_cfg',
            is_presence=True,
        ),
    },
    'Ipsla.Operation.Definitions.Definition.OperationType.IcmpPathEcho' : {
        'meta_info' : _MetaInfoClass('Ipsla.Operation.Definitions.Definition.OperationType.IcmpPathEcho', REFERENCE_CLASS,
            '''ICMPPathEcho Operation type''',
            False, 
            [
            _MetaInfoClassMember('history', REFERENCE_CLASS, 'History', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_ipsla_cfg', 'Ipsla.Operation.Definitions.Definition.OperationType.IcmpPathEcho.History',
                [], [],
                '''                Configure the history parameters for this
                operation
                ''',
                'history',
                'Cisco-IOS-XR-man-ipsla-cfg', False),
            _MetaInfoClassMember('data-size', REFERENCE_CLASS, 'DataSize', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_ipsla_cfg', 'Ipsla.Operation.Definitions.Definition.OperationType.IcmpPathEcho.DataSize',
                [], [],
                '''                Protocol data size in payload of probe
                packets
                ''',
                'data_size',
                'Cisco-IOS-XR-man-ipsla-cfg', False),
            _MetaInfoClassMember('statistics', REFERENCE_CLASS, 'Statistics', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_ipsla_cfg', 'Ipsla.Operation.Definitions.Definition.OperationType.IcmpPathEcho.Statistics',
                [], [],
                '''                Statistics collection aggregated over an
                hour
                ''',
                'statistics',
                'Cisco-IOS-XR-man-ipsla-cfg', False),
            _MetaInfoClassMember('source-address', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                Enter IPv4 address of the source device
                ''',
                'source_address',
                'Cisco-IOS-XR-man-ipsla-cfg', False),
            _MetaInfoClassMember('tos', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('0', '255')], [],
                '''                Type of service setting in probe packet
                ''',
                'tos',
                'Cisco-IOS-XR-man-ipsla-cfg', False, default_value="0"),
            _MetaInfoClassMember('lsr-path', REFERENCE_CLASS, 'LsrPath', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_ipsla_cfg', 'Ipsla.Operation.Definitions.Definition.OperationType.IcmpPathEcho.LsrPath',
                [], [],
                '''                Loose source routing path (up to 8 intermediate
                nodes)
                ''',
                'lsr_path',
                'Cisco-IOS-XR-man-ipsla-cfg', False, is_presence=True),
            _MetaInfoClassMember('vrf', ATTRIBUTE, 'str', 'xr:Cisco-ios-xr-string',
                None, None,
                [(1, 32)], [],
                '''                Configure IPSLA for a VPN Routing/Forwarding
                instance)
                ''',
                'vrf',
                'Cisco-IOS-XR-man-ipsla-cfg', False),
            _MetaInfoClassMember('timeout', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('1', '604800000')], [],
                '''                Probe/Control timeout in milliseconds
                ''',
                'timeout',
                'Cisco-IOS-XR-man-ipsla-cfg', False, default_value="5000"),
            _MetaInfoClassMember('frequency', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('1', '604800')], [],
                '''                Probe interval in seconds
                ''',
                'frequency',
                'Cisco-IOS-XR-man-ipsla-cfg', False, default_value="60"),
            _MetaInfoClassMember('dest-address', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                Enter IPv4 address of the destination device
                ''',
                'dest_address',
                'Cisco-IOS-XR-man-ipsla-cfg', False),
            _MetaInfoClassMember('tag', ATTRIBUTE, 'str', 'string',
                None, None,
                [(1, 100)], [],
                '''                Add a tag for this operation
                ''',
                'tag',
                'Cisco-IOS-XR-man-ipsla-cfg', False),
            ],
            'Cisco-IOS-XR-man-ipsla-cfg',
            'icmp-path-echo',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-man-ipsla-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_ipsla_cfg',
            is_presence=True,
        ),
    },
    'Ipsla.Operation.Definitions.Definition.OperationType.IcmpPathJitter.DataSize' : {
        'meta_info' : _MetaInfoClass('Ipsla.Operation.Definitions.Definition.OperationType.IcmpPathJitter.DataSize', REFERENCE_CLASS,
            '''Protocol data size in payload of probe
packets''',
            False, 
            [
            _MetaInfoClassMember('request', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('0', '16384')], [],
                '''                Payload size in request probe packet
                ''',
                'request',
                'Cisco-IOS-XR-man-ipsla-cfg', False, default_value="36"),
            ],
            'Cisco-IOS-XR-man-ipsla-cfg',
            'data-size',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-man-ipsla-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_ipsla_cfg',
        ),
    },
    'Ipsla.Operation.Definitions.Definition.OperationType.IcmpPathJitter.Packet' : {
        'meta_info' : _MetaInfoClass('Ipsla.Operation.Definitions.Definition.OperationType.IcmpPathJitter.Packet', REFERENCE_CLASS,
            '''Probe packet stream configuration
parameters''',
            False, 
            [
            _MetaInfoClassMember('count', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('1', '100')], [],
                '''                Number of packets to be transmitted during
                a probe
                ''',
                'count',
                'Cisco-IOS-XR-man-ipsla-cfg', False, default_value="10"),
            _MetaInfoClassMember('interval', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('1', '60000')], [],
                '''                Packet interval in milliseconds
                ''',
                'interval',
                'Cisco-IOS-XR-man-ipsla-cfg', False, default_value="20"),
            ],
            'Cisco-IOS-XR-man-ipsla-cfg',
            'packet',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-man-ipsla-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_ipsla_cfg',
        ),
    },
    'Ipsla.Operation.Definitions.Definition.OperationType.IcmpPathJitter.LsrPath' : {
        'meta_info' : _MetaInfoClass('Ipsla.Operation.Definitions.Definition.OperationType.IcmpPathJitter.LsrPath', REFERENCE_CLASS,
            '''Loose source routing path (up to 8 intermediate
nodes)''',
            False, 
            [
            _MetaInfoClassMember('node1', ATTRIBUTE, 'str', 'inet:ipv4-address-no-zone',
                None, None,
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'],
                '''                IPv4 address of the intermediate node
                ''',
                'node1',
                'Cisco-IOS-XR-man-ipsla-cfg', False, is_mandatory=True),
            _MetaInfoClassMember('node2', ATTRIBUTE, 'str', 'inet:ipv4-address-no-zone',
                None, None,
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'],
                '''                IPv4 address of the intermediate node
                ''',
                'node2',
                'Cisco-IOS-XR-man-ipsla-cfg', False),
            _MetaInfoClassMember('node3', ATTRIBUTE, 'str', 'inet:ipv4-address-no-zone',
                None, None,
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'],
                '''                IPv4 address of the intermediate node
                ''',
                'node3',
                'Cisco-IOS-XR-man-ipsla-cfg', False),
            _MetaInfoClassMember('node4', ATTRIBUTE, 'str', 'inet:ipv4-address-no-zone',
                None, None,
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'],
                '''                IPv4 address of the intermediate node
                ''',
                'node4',
                'Cisco-IOS-XR-man-ipsla-cfg', False),
            _MetaInfoClassMember('node5', ATTRIBUTE, 'str', 'inet:ipv4-address-no-zone',
                None, None,
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'],
                '''                IPv4 address of the intermediate node
                ''',
                'node5',
                'Cisco-IOS-XR-man-ipsla-cfg', False),
            _MetaInfoClassMember('node6', ATTRIBUTE, 'str', 'inet:ipv4-address-no-zone',
                None, None,
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'],
                '''                IPv4 address of the intermediate node
                ''',
                'node6',
                'Cisco-IOS-XR-man-ipsla-cfg', False),
            _MetaInfoClassMember('node7', ATTRIBUTE, 'str', 'inet:ipv4-address-no-zone',
                None, None,
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'],
                '''                IPv4 address of the intermediate node
                ''',
                'node7',
                'Cisco-IOS-XR-man-ipsla-cfg', False),
            _MetaInfoClassMember('node8', ATTRIBUTE, 'str', 'inet:ipv4-address-no-zone',
                None, None,
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'],
                '''                IPv4 address of the intermediate node
                ''',
                'node8',
                'Cisco-IOS-XR-man-ipsla-cfg', False),
            ],
            'Cisco-IOS-XR-man-ipsla-cfg',
            'lsr-path',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-man-ipsla-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_ipsla_cfg',
            is_presence=True,
        ),
    },
    'Ipsla.Operation.Definitions.Definition.OperationType.IcmpPathJitter' : {
        'meta_info' : _MetaInfoClass('Ipsla.Operation.Definitions.Definition.OperationType.IcmpPathJitter', REFERENCE_CLASS,
            '''ICMPPathJitter Operation type''',
            False, 
            [
            _MetaInfoClassMember('data-size', REFERENCE_CLASS, 'DataSize', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_ipsla_cfg', 'Ipsla.Operation.Definitions.Definition.OperationType.IcmpPathJitter.DataSize',
                [], [],
                '''                Protocol data size in payload of probe
                packets
                ''',
                'data_size',
                'Cisco-IOS-XR-man-ipsla-cfg', False),
            _MetaInfoClassMember('packet', REFERENCE_CLASS, 'Packet', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_ipsla_cfg', 'Ipsla.Operation.Definitions.Definition.OperationType.IcmpPathJitter.Packet',
                [], [],
                '''                Probe packet stream configuration
                parameters
                ''',
                'packet',
                'Cisco-IOS-XR-man-ipsla-cfg', False),
            _MetaInfoClassMember('source-address', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                Enter IPv4 address of the source device
                ''',
                'source_address',
                'Cisco-IOS-XR-man-ipsla-cfg', False),
            _MetaInfoClassMember('tos', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('0', '255')], [],
                '''                Type of service setting in probe packet
                ''',
                'tos',
                'Cisco-IOS-XR-man-ipsla-cfg', False, default_value="0"),
            _MetaInfoClassMember('lsr-path', REFERENCE_CLASS, 'LsrPath', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_ipsla_cfg', 'Ipsla.Operation.Definitions.Definition.OperationType.IcmpPathJitter.LsrPath',
                [], [],
                '''                Loose source routing path (up to 8 intermediate
                nodes)
                ''',
                'lsr_path',
                'Cisco-IOS-XR-man-ipsla-cfg', False, is_presence=True),
            _MetaInfoClassMember('vrf', ATTRIBUTE, 'str', 'xr:Cisco-ios-xr-string',
                None, None,
                [(1, 32)], [],
                '''                Configure IPSLA for a VPN Routing/Forwarding
                instance)
                ''',
                'vrf',
                'Cisco-IOS-XR-man-ipsla-cfg', False),
            _MetaInfoClassMember('timeout', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('1', '604800000')], [],
                '''                Probe/Control timeout in milliseconds
                ''',
                'timeout',
                'Cisco-IOS-XR-man-ipsla-cfg', False, default_value="5000"),
            _MetaInfoClassMember('frequency', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('1', '604800')], [],
                '''                Probe interval in seconds
                ''',
                'frequency',
                'Cisco-IOS-XR-man-ipsla-cfg', False, default_value="60"),
            _MetaInfoClassMember('dest-address', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                Enter IPv4 address of the destination device
                ''',
                'dest_address',
                'Cisco-IOS-XR-man-ipsla-cfg', False),
            _MetaInfoClassMember('tag', ATTRIBUTE, 'str', 'string',
                None, None,
                [(1, 100)], [],
                '''                Add a tag for this operation
                ''',
                'tag',
                'Cisco-IOS-XR-man-ipsla-cfg', False),
            ],
            'Cisco-IOS-XR-man-ipsla-cfg',
            'icmp-path-jitter',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-man-ipsla-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_ipsla_cfg',
            is_presence=True,
        ),
    },
    'Ipsla.Operation.Definitions.Definition.OperationType' : {
        'meta_info' : _MetaInfoClass('Ipsla.Operation.Definitions.Definition.OperationType', REFERENCE_CLASS,
            '''Operation type specification''',
            False, 
            [
            _MetaInfoClassMember('icmp-echo', REFERENCE_CLASS, 'IcmpEcho', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_ipsla_cfg', 'Ipsla.Operation.Definitions.Definition.OperationType.IcmpEcho',
                [], [],
                '''                ICMPEcho Operation type
                ''',
                'icmp_echo',
                'Cisco-IOS-XR-man-ipsla-cfg', False, is_presence=True),
            _MetaInfoClassMember('mpls-lsp-ping', REFERENCE_CLASS, 'MplsLspPing', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_ipsla_cfg', 'Ipsla.Operation.Definitions.Definition.OperationType.MplsLspPing',
                [], [],
                '''                MPLS LSP Ping Operation type
                ''',
                'mpls_lsp_ping',
                'Cisco-IOS-XR-man-ipsla-cfg', False, is_presence=True),
            _MetaInfoClassMember('udp-echo', REFERENCE_CLASS, 'UdpEcho', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_ipsla_cfg', 'Ipsla.Operation.Definitions.Definition.OperationType.UdpEcho',
                [], [],
                '''                UDPEcho Operation type
                ''',
                'udp_echo',
                'Cisco-IOS-XR-man-ipsla-cfg', False, is_presence=True),
            _MetaInfoClassMember('mpls-lsp-trace', REFERENCE_CLASS, 'MplsLspTrace', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_ipsla_cfg', 'Ipsla.Operation.Definitions.Definition.OperationType.MplsLspTrace',
                [], [],
                '''                MPLS LSP Trace Operation type
                ''',
                'mpls_lsp_trace',
                'Cisco-IOS-XR-man-ipsla-cfg', False, is_presence=True),
            _MetaInfoClassMember('udp-jitter', REFERENCE_CLASS, 'UdpJitter', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_ipsla_cfg', 'Ipsla.Operation.Definitions.Definition.OperationType.UdpJitter',
                [], [],
                '''                UDPJitter Operation type
                ''',
                'udp_jitter',
                'Cisco-IOS-XR-man-ipsla-cfg', False, is_presence=True),
            _MetaInfoClassMember('icmp-path-echo', REFERENCE_CLASS, 'IcmpPathEcho', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_ipsla_cfg', 'Ipsla.Operation.Definitions.Definition.OperationType.IcmpPathEcho',
                [], [],
                '''                ICMPPathEcho Operation type
                ''',
                'icmp_path_echo',
                'Cisco-IOS-XR-man-ipsla-cfg', False, is_presence=True),
            _MetaInfoClassMember('icmp-path-jitter', REFERENCE_CLASS, 'IcmpPathJitter', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_ipsla_cfg', 'Ipsla.Operation.Definitions.Definition.OperationType.IcmpPathJitter',
                [], [],
                '''                ICMPPathJitter Operation type
                ''',
                'icmp_path_jitter',
                'Cisco-IOS-XR-man-ipsla-cfg', False, is_presence=True),
            ],
            'Cisco-IOS-XR-man-ipsla-cfg',
            'operation-type',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-man-ipsla-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_ipsla_cfg',
        ),
    },
    'Ipsla.Operation.Definitions.Definition' : {
        'meta_info' : _MetaInfoClass('Ipsla.Operation.Definitions.Definition', REFERENCE_LIST,
            '''Operation definition''',
            False, 
            [
            _MetaInfoClassMember('operation-id', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('1', '2048')], [],
                '''                Operation number
                ''',
                'operation_id',
                'Cisco-IOS-XR-man-ipsla-cfg', True),
            _MetaInfoClassMember('operation-type', REFERENCE_CLASS, 'OperationType', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_ipsla_cfg', 'Ipsla.Operation.Definitions.Definition.OperationType',
                [], [],
                '''                Operation type specification
                ''',
                'operation_type',
                'Cisco-IOS-XR-man-ipsla-cfg', False),
            ],
            'Cisco-IOS-XR-man-ipsla-cfg',
            'definition',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-man-ipsla-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_ipsla_cfg',
        ),
    },
    'Ipsla.Operation.Definitions' : {
        'meta_info' : _MetaInfoClass('Ipsla.Operation.Definitions', REFERENCE_CLASS,
            '''Operation definition table''',
            False, 
            [
            _MetaInfoClassMember('definition', REFERENCE_LIST, 'Definition', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_ipsla_cfg', 'Ipsla.Operation.Definitions.Definition',
                [], [],
                '''                Operation definition
                ''',
                'definition',
                'Cisco-IOS-XR-man-ipsla-cfg', False),
            ],
            'Cisco-IOS-XR-man-ipsla-cfg',
            'definitions',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-man-ipsla-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_ipsla_cfg',
        ),
    },
    'Ipsla.Operation' : {
        'meta_info' : _MetaInfoClass('Ipsla.Operation', REFERENCE_CLASS,
            '''IPSLA Operation configuration''',
            False, 
            [
            _MetaInfoClassMember('schedules', REFERENCE_CLASS, 'Schedules', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_ipsla_cfg', 'Ipsla.Operation.Schedules',
                [], [],
                '''                Schedule an operation
                ''',
                'schedules',
                'Cisco-IOS-XR-man-ipsla-cfg', False),
            _MetaInfoClassMember('reactions', REFERENCE_CLASS, 'Reactions', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_ipsla_cfg', 'Ipsla.Operation.Reactions',
                [], [],
                '''                Reaction configuration
                ''',
                'reactions',
                'Cisco-IOS-XR-man-ipsla-cfg', False),
            _MetaInfoClassMember('reaction-triggers', REFERENCE_CLASS, 'ReactionTriggers', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_ipsla_cfg', 'Ipsla.Operation.ReactionTriggers',
                [], [],
                '''                Reaction trigger configuration
                ''',
                'reaction_triggers',
                'Cisco-IOS-XR-man-ipsla-cfg', False),
            _MetaInfoClassMember('definitions', REFERENCE_CLASS, 'Definitions', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_ipsla_cfg', 'Ipsla.Operation.Definitions',
                [], [],
                '''                Operation definition table
                ''',
                'definitions',
                'Cisco-IOS-XR-man-ipsla-cfg', False),
            ],
            'Cisco-IOS-XR-man-ipsla-cfg',
            'operation',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-man-ipsla-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_ipsla_cfg',
        ),
    },
    'Ipsla.Responder.Twamp' : {
        'meta_info' : _MetaInfoClass('Ipsla.Responder.Twamp', REFERENCE_CLASS,
            '''Responder TWAMP configuration''',
            False, 
            [
            _MetaInfoClassMember('timeout', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('1', '604800')], [],
                '''                Configure responder timeout value in seconds
                ''',
                'timeout',
                'Cisco-IOS-XR-man-ipsla-cfg', False, default_value="900"),
            ],
            'Cisco-IOS-XR-man-ipsla-cfg',
            'twamp',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-man-ipsla-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_ipsla_cfg',
            is_presence=True,
        ),
    },
    'Ipsla.Responder.Type.Udp.Addresses.Address.Ports.Port' : {
        'meta_info' : _MetaInfoClass('Ipsla.Responder.Type.Udp.Addresses.Address.Ports.Port', REFERENCE_LIST,
            '''Configure port number for the permanent
port''',
            False, 
            [
            _MetaInfoClassMember('port', ATTRIBUTE, 'int', 'inet:port-number',
                None, None,
                [('0', '65535')], [],
                '''                Port number to be enabled
                ''',
                'port',
                'Cisco-IOS-XR-man-ipsla-cfg', True),
            ],
            'Cisco-IOS-XR-man-ipsla-cfg',
            'port',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-man-ipsla-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_ipsla_cfg',
        ),
    },
    'Ipsla.Responder.Type.Udp.Addresses.Address.Ports' : {
        'meta_info' : _MetaInfoClass('Ipsla.Responder.Type.Udp.Addresses.Address.Ports', REFERENCE_CLASS,
            '''Configure port''',
            False, 
            [
            _MetaInfoClassMember('port', REFERENCE_LIST, 'Port', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_ipsla_cfg', 'Ipsla.Responder.Type.Udp.Addresses.Address.Ports.Port',
                [], [],
                '''                Configure port number for the permanent
                port
                ''',
                'port',
                'Cisco-IOS-XR-man-ipsla-cfg', False),
            ],
            'Cisco-IOS-XR-man-ipsla-cfg',
            'ports',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-man-ipsla-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_ipsla_cfg',
        ),
    },
    'Ipsla.Responder.Type.Udp.Addresses.Address' : {
        'meta_info' : _MetaInfoClass('Ipsla.Responder.Type.Udp.Addresses.Address', REFERENCE_LIST,
            '''Configure IP address for the permanent port''',
            False, 
            [
            _MetaInfoClassMember('local-address', ATTRIBUTE, 'str', 'inet:ipv4-address-no-zone',
                None, None,
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'],
                '''                IP address of the Responder
                ''',
                'local_address',
                'Cisco-IOS-XR-man-ipsla-cfg', True),
            _MetaInfoClassMember('ports', REFERENCE_CLASS, 'Ports', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_ipsla_cfg', 'Ipsla.Responder.Type.Udp.Addresses.Address.Ports',
                [], [],
                '''                Configure port
                ''',
                'ports',
                'Cisco-IOS-XR-man-ipsla-cfg', False),
            ],
            'Cisco-IOS-XR-man-ipsla-cfg',
            'address',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-man-ipsla-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_ipsla_cfg',
        ),
    },
    'Ipsla.Responder.Type.Udp.Addresses' : {
        'meta_info' : _MetaInfoClass('Ipsla.Responder.Type.Udp.Addresses', REFERENCE_CLASS,
            '''Configure IP address''',
            False, 
            [
            _MetaInfoClassMember('address', REFERENCE_LIST, 'Address', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_ipsla_cfg', 'Ipsla.Responder.Type.Udp.Addresses.Address',
                [], [],
                '''                Configure IP address for the permanent port
                ''',
                'address',
                'Cisco-IOS-XR-man-ipsla-cfg', False),
            ],
            'Cisco-IOS-XR-man-ipsla-cfg',
            'addresses',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-man-ipsla-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_ipsla_cfg',
        ),
    },
    'Ipsla.Responder.Type.Udp' : {
        'meta_info' : _MetaInfoClass('Ipsla.Responder.Type.Udp', REFERENCE_CLASS,
            '''Configure IPSLA Responder UDP address and port''',
            False, 
            [
            _MetaInfoClassMember('addresses', REFERENCE_CLASS, 'Addresses', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_ipsla_cfg', 'Ipsla.Responder.Type.Udp.Addresses',
                [], [],
                '''                Configure IP address
                ''',
                'addresses',
                'Cisco-IOS-XR-man-ipsla-cfg', False),
            ],
            'Cisco-IOS-XR-man-ipsla-cfg',
            'udp',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-man-ipsla-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_ipsla_cfg',
        ),
    },
    'Ipsla.Responder.Type' : {
        'meta_info' : _MetaInfoClass('Ipsla.Responder.Type', REFERENCE_CLASS,
            '''Configure IPSLA Responder port type''',
            False, 
            [
            _MetaInfoClassMember('udp', REFERENCE_CLASS, 'Udp', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_ipsla_cfg', 'Ipsla.Responder.Type.Udp',
                [], [],
                '''                Configure IPSLA Responder UDP address and port
                ''',
                'udp',
                'Cisco-IOS-XR-man-ipsla-cfg', False),
            ],
            'Cisco-IOS-XR-man-ipsla-cfg',
            'type',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-man-ipsla-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_ipsla_cfg',
        ),
    },
    'Ipsla.Responder.TwampLight.SessionIds.SessionId.LocalIp.LocalIpv6Addresses.LocalIpv6Address.LocalPortNumbers.LocalPortNumber.RemoteIp.RemoteIpv4Addresses.RemoteIpv4Address.RemotePortNumbers.RemotePortNumber.VrfNames.VrfName' : {
        'meta_info' : _MetaInfoClass('Ipsla.Responder.TwampLight.SessionIds.SessionId.LocalIp.LocalIpv6Addresses.LocalIpv6Address.LocalPortNumbers.LocalPortNumber.RemoteIp.RemoteIpv4Addresses.RemoteIpv4Address.RemotePortNumbers.RemotePortNumber.VrfNames.VrfName', REFERENCE_LIST,
            '''Configure vrf name value''',
            False, 
            [
            _MetaInfoClassMember('vrf-name', ATTRIBUTE, 'str', 'xr:Cisco-ios-xr-string',
                None, None,
                [(1, 32)], [],
                '''                VRF Name
                ''',
                'vrf_name',
                'Cisco-IOS-XR-man-ipsla-cfg', True),
            ],
            'Cisco-IOS-XR-man-ipsla-cfg',
            'vrf-name',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-man-ipsla-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_ipsla_cfg',
        ),
    },
    'Ipsla.Responder.TwampLight.SessionIds.SessionId.LocalIp.LocalIpv6Addresses.LocalIpv6Address.LocalPortNumbers.LocalPortNumber.RemoteIp.RemoteIpv4Addresses.RemoteIpv4Address.RemotePortNumbers.RemotePortNumber.VrfNames' : {
        'meta_info' : _MetaInfoClass('Ipsla.Responder.TwampLight.SessionIds.SessionId.LocalIp.LocalIpv6Addresses.LocalIpv6Address.LocalPortNumbers.LocalPortNumber.RemoteIp.RemoteIpv4Addresses.RemoteIpv4Address.RemotePortNumbers.RemotePortNumber.VrfNames', REFERENCE_CLASS,
            '''Configuration of vrf''',
            False, 
            [
            _MetaInfoClassMember('vrf-name', REFERENCE_LIST, 'VrfName', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_ipsla_cfg', 'Ipsla.Responder.TwampLight.SessionIds.SessionId.LocalIp.LocalIpv6Addresses.LocalIpv6Address.LocalPortNumbers.LocalPortNumber.RemoteIp.RemoteIpv4Addresses.RemoteIpv4Address.RemotePortNumbers.RemotePortNumber.VrfNames.VrfName',
                [], [],
                '''                Configure vrf name value
                ''',
                'vrf_name',
                'Cisco-IOS-XR-man-ipsla-cfg', False),
            ],
            'Cisco-IOS-XR-man-ipsla-cfg',
            'vrf-names',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-man-ipsla-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_ipsla_cfg',
        ),
    },
    'Ipsla.Responder.TwampLight.SessionIds.SessionId.LocalIp.LocalIpv6Addresses.LocalIpv6Address.LocalPortNumbers.LocalPortNumber.RemoteIp.RemoteIpv4Addresses.RemoteIpv4Address.RemotePortNumbers.RemotePortNumber' : {
        'meta_info' : _MetaInfoClass('Ipsla.Responder.TwampLight.SessionIds.SessionId.LocalIp.LocalIpv6Addresses.LocalIpv6Address.LocalPortNumbers.LocalPortNumber.RemoteIp.RemoteIpv4Addresses.RemoteIpv4Address.RemotePortNumbers.RemotePortNumber', REFERENCE_LIST,
            '''Enter value of remote port''',
            False, 
            [
            _MetaInfoClassMember('remote-port', ATTRIBUTE, 'int', 'inet:port-number',
                None, None,
                [('0', '65535')], [],
                '''                Remote port
                ''',
                'remote_port',
                'Cisco-IOS-XR-man-ipsla-cfg', True),
            _MetaInfoClassMember('vrf-names', REFERENCE_CLASS, 'VrfNames', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_ipsla_cfg', 'Ipsla.Responder.TwampLight.SessionIds.SessionId.LocalIp.LocalIpv6Addresses.LocalIpv6Address.LocalPortNumbers.LocalPortNumber.RemoteIp.RemoteIpv4Addresses.RemoteIpv4Address.RemotePortNumbers.RemotePortNumber.VrfNames',
                [], [],
                '''                Configuration of vrf
                ''',
                'vrf_names',
                'Cisco-IOS-XR-man-ipsla-cfg', False),
            ],
            'Cisco-IOS-XR-man-ipsla-cfg',
            'remote-port-number',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-man-ipsla-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_ipsla_cfg',
        ),
    },
    'Ipsla.Responder.TwampLight.SessionIds.SessionId.LocalIp.LocalIpv6Addresses.LocalIpv6Address.LocalPortNumbers.LocalPortNumber.RemoteIp.RemoteIpv4Addresses.RemoteIpv4Address.RemotePortNumbers' : {
        'meta_info' : _MetaInfoClass('Ipsla.Responder.TwampLight.SessionIds.SessionId.LocalIp.LocalIpv6Addresses.LocalIpv6Address.LocalPortNumbers.LocalPortNumber.RemoteIp.RemoteIpv4Addresses.RemoteIpv4Address.RemotePortNumbers', REFERENCE_CLASS,
            '''Configuration of remote port''',
            False, 
            [
            _MetaInfoClassMember('remote-port-number', REFERENCE_LIST, 'RemotePortNumber', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_ipsla_cfg', 'Ipsla.Responder.TwampLight.SessionIds.SessionId.LocalIp.LocalIpv6Addresses.LocalIpv6Address.LocalPortNumbers.LocalPortNumber.RemoteIp.RemoteIpv4Addresses.RemoteIpv4Address.RemotePortNumbers.RemotePortNumber',
                [], [],
                '''                Enter value of remote port
                ''',
                'remote_port_number',
                'Cisco-IOS-XR-man-ipsla-cfg', False),
            ],
            'Cisco-IOS-XR-man-ipsla-cfg',
            'remote-port-numbers',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-man-ipsla-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_ipsla_cfg',
        ),
    },
    'Ipsla.Responder.TwampLight.SessionIds.SessionId.LocalIp.LocalIpv6Addresses.LocalIpv6Address.LocalPortNumbers.LocalPortNumber.RemoteIp.RemoteIpv4Addresses.RemoteIpv4Address' : {
        'meta_info' : _MetaInfoClass('Ipsla.Responder.TwampLight.SessionIds.SessionId.LocalIp.LocalIpv6Addresses.LocalIpv6Address.LocalPortNumbers.LocalPortNumber.RemoteIp.RemoteIpv4Addresses.RemoteIpv4Address', REFERENCE_LIST,
            '''Enter value of remote ipv4 address''',
            False, 
            [
            _MetaInfoClassMember('remotev4-address', ATTRIBUTE, 'str', 'xr:Cisco-ios-xr-string',
                None, None,
                [], [b'[\\w\\-\\.:,_@#%$\\+=\\|;]+'],
                '''                Remote IPv4 address
                ''',
                'remotev4_address',
                'Cisco-IOS-XR-man-ipsla-cfg', True),
            _MetaInfoClassMember('remote-port-numbers', REFERENCE_CLASS, 'RemotePortNumbers', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_ipsla_cfg', 'Ipsla.Responder.TwampLight.SessionIds.SessionId.LocalIp.LocalIpv6Addresses.LocalIpv6Address.LocalPortNumbers.LocalPortNumber.RemoteIp.RemoteIpv4Addresses.RemoteIpv4Address.RemotePortNumbers',
                [], [],
                '''                Configuration of remote port
                ''',
                'remote_port_numbers',
                'Cisco-IOS-XR-man-ipsla-cfg', False),
            ],
            'Cisco-IOS-XR-man-ipsla-cfg',
            'remote-ipv4-address',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-man-ipsla-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_ipsla_cfg',
        ),
    },
    'Ipsla.Responder.TwampLight.SessionIds.SessionId.LocalIp.LocalIpv6Addresses.LocalIpv6Address.LocalPortNumbers.LocalPortNumber.RemoteIp.RemoteIpv4Addresses' : {
        'meta_info' : _MetaInfoClass('Ipsla.Responder.TwampLight.SessionIds.SessionId.LocalIp.LocalIpv6Addresses.LocalIpv6Address.LocalPortNumbers.LocalPortNumber.RemoteIp.RemoteIpv4Addresses', REFERENCE_CLASS,
            '''Configure IPV4 address''',
            False, 
            [
            _MetaInfoClassMember('remote-ipv4-address', REFERENCE_LIST, 'RemoteIpv4Address', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_ipsla_cfg', 'Ipsla.Responder.TwampLight.SessionIds.SessionId.LocalIp.LocalIpv6Addresses.LocalIpv6Address.LocalPortNumbers.LocalPortNumber.RemoteIp.RemoteIpv4Addresses.RemoteIpv4Address',
                [], [],
                '''                Enter value of remote ipv4 address
                ''',
                'remote_ipv4_address',
                'Cisco-IOS-XR-man-ipsla-cfg', False),
            ],
            'Cisco-IOS-XR-man-ipsla-cfg',
            'remote-ipv4-addresses',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-man-ipsla-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_ipsla_cfg',
        ),
    },
    'Ipsla.Responder.TwampLight.SessionIds.SessionId.LocalIp.LocalIpv6Addresses.LocalIpv6Address.LocalPortNumbers.LocalPortNumber.RemoteIp.RemoteIpv6Addresses.RemoteIpv6Address.RemotePortNumbers.RemotePortNumber.VrfNames.VrfName' : {
        'meta_info' : _MetaInfoClass('Ipsla.Responder.TwampLight.SessionIds.SessionId.LocalIp.LocalIpv6Addresses.LocalIpv6Address.LocalPortNumbers.LocalPortNumber.RemoteIp.RemoteIpv6Addresses.RemoteIpv6Address.RemotePortNumbers.RemotePortNumber.VrfNames.VrfName', REFERENCE_LIST,
            '''Configure vrf name value''',
            False, 
            [
            _MetaInfoClassMember('vrf-name', ATTRIBUTE, 'str', 'xr:Cisco-ios-xr-string',
                None, None,
                [(1, 32)], [],
                '''                VRF Name
                ''',
                'vrf_name',
                'Cisco-IOS-XR-man-ipsla-cfg', True),
            ],
            'Cisco-IOS-XR-man-ipsla-cfg',
            'vrf-name',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-man-ipsla-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_ipsla_cfg',
        ),
    },
    'Ipsla.Responder.TwampLight.SessionIds.SessionId.LocalIp.LocalIpv6Addresses.LocalIpv6Address.LocalPortNumbers.LocalPortNumber.RemoteIp.RemoteIpv6Addresses.RemoteIpv6Address.RemotePortNumbers.RemotePortNumber.VrfNames' : {
        'meta_info' : _MetaInfoClass('Ipsla.Responder.TwampLight.SessionIds.SessionId.LocalIp.LocalIpv6Addresses.LocalIpv6Address.LocalPortNumbers.LocalPortNumber.RemoteIp.RemoteIpv6Addresses.RemoteIpv6Address.RemotePortNumbers.RemotePortNumber.VrfNames', REFERENCE_CLASS,
            '''Configuration of vrf''',
            False, 
            [
            _MetaInfoClassMember('vrf-name', REFERENCE_LIST, 'VrfName', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_ipsla_cfg', 'Ipsla.Responder.TwampLight.SessionIds.SessionId.LocalIp.LocalIpv6Addresses.LocalIpv6Address.LocalPortNumbers.LocalPortNumber.RemoteIp.RemoteIpv6Addresses.RemoteIpv6Address.RemotePortNumbers.RemotePortNumber.VrfNames.VrfName',
                [], [],
                '''                Configure vrf name value
                ''',
                'vrf_name',
                'Cisco-IOS-XR-man-ipsla-cfg', False),
            ],
            'Cisco-IOS-XR-man-ipsla-cfg',
            'vrf-names',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-man-ipsla-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_ipsla_cfg',
        ),
    },
    'Ipsla.Responder.TwampLight.SessionIds.SessionId.LocalIp.LocalIpv6Addresses.LocalIpv6Address.LocalPortNumbers.LocalPortNumber.RemoteIp.RemoteIpv6Addresses.RemoteIpv6Address.RemotePortNumbers.RemotePortNumber' : {
        'meta_info' : _MetaInfoClass('Ipsla.Responder.TwampLight.SessionIds.SessionId.LocalIp.LocalIpv6Addresses.LocalIpv6Address.LocalPortNumbers.LocalPortNumber.RemoteIp.RemoteIpv6Addresses.RemoteIpv6Address.RemotePortNumbers.RemotePortNumber', REFERENCE_LIST,
            '''Enter value of remote port''',
            False, 
            [
            _MetaInfoClassMember('remote-port', ATTRIBUTE, 'int', 'inet:port-number',
                None, None,
                [('0', '65535')], [],
                '''                Remote port
                ''',
                'remote_port',
                'Cisco-IOS-XR-man-ipsla-cfg', True),
            _MetaInfoClassMember('vrf-names', REFERENCE_CLASS, 'VrfNames', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_ipsla_cfg', 'Ipsla.Responder.TwampLight.SessionIds.SessionId.LocalIp.LocalIpv6Addresses.LocalIpv6Address.LocalPortNumbers.LocalPortNumber.RemoteIp.RemoteIpv6Addresses.RemoteIpv6Address.RemotePortNumbers.RemotePortNumber.VrfNames',
                [], [],
                '''                Configuration of vrf
                ''',
                'vrf_names',
                'Cisco-IOS-XR-man-ipsla-cfg', False),
            ],
            'Cisco-IOS-XR-man-ipsla-cfg',
            'remote-port-number',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-man-ipsla-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_ipsla_cfg',
        ),
    },
    'Ipsla.Responder.TwampLight.SessionIds.SessionId.LocalIp.LocalIpv6Addresses.LocalIpv6Address.LocalPortNumbers.LocalPortNumber.RemoteIp.RemoteIpv6Addresses.RemoteIpv6Address.RemotePortNumbers' : {
        'meta_info' : _MetaInfoClass('Ipsla.Responder.TwampLight.SessionIds.SessionId.LocalIp.LocalIpv6Addresses.LocalIpv6Address.LocalPortNumbers.LocalPortNumber.RemoteIp.RemoteIpv6Addresses.RemoteIpv6Address.RemotePortNumbers', REFERENCE_CLASS,
            '''Configuration of remote port''',
            False, 
            [
            _MetaInfoClassMember('remote-port-number', REFERENCE_LIST, 'RemotePortNumber', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_ipsla_cfg', 'Ipsla.Responder.TwampLight.SessionIds.SessionId.LocalIp.LocalIpv6Addresses.LocalIpv6Address.LocalPortNumbers.LocalPortNumber.RemoteIp.RemoteIpv6Addresses.RemoteIpv6Address.RemotePortNumbers.RemotePortNumber',
                [], [],
                '''                Enter value of remote port
                ''',
                'remote_port_number',
                'Cisco-IOS-XR-man-ipsla-cfg', False),
            ],
            'Cisco-IOS-XR-man-ipsla-cfg',
            'remote-port-numbers',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-man-ipsla-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_ipsla_cfg',
        ),
    },
    'Ipsla.Responder.TwampLight.SessionIds.SessionId.LocalIp.LocalIpv6Addresses.LocalIpv6Address.LocalPortNumbers.LocalPortNumber.RemoteIp.RemoteIpv6Addresses.RemoteIpv6Address' : {
        'meta_info' : _MetaInfoClass('Ipsla.Responder.TwampLight.SessionIds.SessionId.LocalIp.LocalIpv6Addresses.LocalIpv6Address.LocalPortNumbers.LocalPortNumber.RemoteIp.RemoteIpv6Addresses.RemoteIpv6Address', REFERENCE_LIST,
            '''Enter value of remote ipv6 address''',
            False, 
            [
            _MetaInfoClassMember('remotev6-address', ATTRIBUTE, 'str', 'xr:Cisco-ios-xr-string',
                None, None,
                [], [b'[\\w\\-\\.:,_@#%$\\+=\\|;]+'],
                '''                Remote IPv6 address
                ''',
                'remotev6_address',
                'Cisco-IOS-XR-man-ipsla-cfg', True),
            _MetaInfoClassMember('remote-port-numbers', REFERENCE_CLASS, 'RemotePortNumbers', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_ipsla_cfg', 'Ipsla.Responder.TwampLight.SessionIds.SessionId.LocalIp.LocalIpv6Addresses.LocalIpv6Address.LocalPortNumbers.LocalPortNumber.RemoteIp.RemoteIpv6Addresses.RemoteIpv6Address.RemotePortNumbers',
                [], [],
                '''                Configuration of remote port
                ''',
                'remote_port_numbers',
                'Cisco-IOS-XR-man-ipsla-cfg', False),
            ],
            'Cisco-IOS-XR-man-ipsla-cfg',
            'remote-ipv6-address',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-man-ipsla-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_ipsla_cfg',
        ),
    },
    'Ipsla.Responder.TwampLight.SessionIds.SessionId.LocalIp.LocalIpv6Addresses.LocalIpv6Address.LocalPortNumbers.LocalPortNumber.RemoteIp.RemoteIpv6Addresses' : {
        'meta_info' : _MetaInfoClass('Ipsla.Responder.TwampLight.SessionIds.SessionId.LocalIp.LocalIpv6Addresses.LocalIpv6Address.LocalPortNumbers.LocalPortNumber.RemoteIp.RemoteIpv6Addresses', REFERENCE_CLASS,
            '''Configure IPV6 address''',
            False, 
            [
            _MetaInfoClassMember('remote-ipv6-address', REFERENCE_LIST, 'RemoteIpv6Address', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_ipsla_cfg', 'Ipsla.Responder.TwampLight.SessionIds.SessionId.LocalIp.LocalIpv6Addresses.LocalIpv6Address.LocalPortNumbers.LocalPortNumber.RemoteIp.RemoteIpv6Addresses.RemoteIpv6Address',
                [], [],
                '''                Enter value of remote ipv6 address
                ''',
                'remote_ipv6_address',
                'Cisco-IOS-XR-man-ipsla-cfg', False),
            ],
            'Cisco-IOS-XR-man-ipsla-cfg',
            'remote-ipv6-addresses',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-man-ipsla-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_ipsla_cfg',
        ),
    },
    'Ipsla.Responder.TwampLight.SessionIds.SessionId.LocalIp.LocalIpv6Addresses.LocalIpv6Address.LocalPortNumbers.LocalPortNumber.RemoteIp' : {
        'meta_info' : _MetaInfoClass('Ipsla.Responder.TwampLight.SessionIds.SessionId.LocalIp.LocalIpv6Addresses.LocalIpv6Address.LocalPortNumbers.LocalPortNumber.RemoteIp', REFERENCE_CLASS,
            '''Configure remote ip address''',
            False, 
            [
            _MetaInfoClassMember('remote-ipv4-addresses', REFERENCE_CLASS, 'RemoteIpv4Addresses', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_ipsla_cfg', 'Ipsla.Responder.TwampLight.SessionIds.SessionId.LocalIp.LocalIpv6Addresses.LocalIpv6Address.LocalPortNumbers.LocalPortNumber.RemoteIp.RemoteIpv4Addresses',
                [], [],
                '''                Configure IPV4 address
                ''',
                'remote_ipv4_addresses',
                'Cisco-IOS-XR-man-ipsla-cfg', False),
            _MetaInfoClassMember('remote-ipv6-addresses', REFERENCE_CLASS, 'RemoteIpv6Addresses', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_ipsla_cfg', 'Ipsla.Responder.TwampLight.SessionIds.SessionId.LocalIp.LocalIpv6Addresses.LocalIpv6Address.LocalPortNumbers.LocalPortNumber.RemoteIp.RemoteIpv6Addresses',
                [], [],
                '''                Configure IPV6 address
                ''',
                'remote_ipv6_addresses',
                'Cisco-IOS-XR-man-ipsla-cfg', False),
            ],
            'Cisco-IOS-XR-man-ipsla-cfg',
            'remote-ip',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-man-ipsla-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_ipsla_cfg',
        ),
    },
    'Ipsla.Responder.TwampLight.SessionIds.SessionId.LocalIp.LocalIpv6Addresses.LocalIpv6Address.LocalPortNumbers.LocalPortNumber' : {
        'meta_info' : _MetaInfoClass('Ipsla.Responder.TwampLight.SessionIds.SessionId.LocalIp.LocalIpv6Addresses.LocalIpv6Address.LocalPortNumbers.LocalPortNumber', REFERENCE_LIST,
            '''Enter value of local port''',
            False, 
            [
            _MetaInfoClassMember('local-port', ATTRIBUTE, 'int', 'inet:port-number',
                None, None,
                [('0', '65535')], [],
                '''                Local port
                ''',
                'local_port',
                'Cisco-IOS-XR-man-ipsla-cfg', True),
            _MetaInfoClassMember('remote-ip', REFERENCE_CLASS, 'RemoteIp', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_ipsla_cfg', 'Ipsla.Responder.TwampLight.SessionIds.SessionId.LocalIp.LocalIpv6Addresses.LocalIpv6Address.LocalPortNumbers.LocalPortNumber.RemoteIp',
                [], [],
                '''                Configure remote ip address
                ''',
                'remote_ip',
                'Cisco-IOS-XR-man-ipsla-cfg', False),
            ],
            'Cisco-IOS-XR-man-ipsla-cfg',
            'local-port-number',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-man-ipsla-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_ipsla_cfg',
        ),
    },
    'Ipsla.Responder.TwampLight.SessionIds.SessionId.LocalIp.LocalIpv6Addresses.LocalIpv6Address.LocalPortNumbers' : {
        'meta_info' : _MetaInfoClass('Ipsla.Responder.TwampLight.SessionIds.SessionId.LocalIp.LocalIpv6Addresses.LocalIpv6Address.LocalPortNumbers', REFERENCE_CLASS,
            '''Configuration of local port''',
            False, 
            [
            _MetaInfoClassMember('local-port-number', REFERENCE_LIST, 'LocalPortNumber', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_ipsla_cfg', 'Ipsla.Responder.TwampLight.SessionIds.SessionId.LocalIp.LocalIpv6Addresses.LocalIpv6Address.LocalPortNumbers.LocalPortNumber',
                [], [],
                '''                Enter value of local port
                ''',
                'local_port_number',
                'Cisco-IOS-XR-man-ipsla-cfg', False),
            ],
            'Cisco-IOS-XR-man-ipsla-cfg',
            'local-port-numbers',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-man-ipsla-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_ipsla_cfg',
        ),
    },
    'Ipsla.Responder.TwampLight.SessionIds.SessionId.LocalIp.LocalIpv6Addresses.LocalIpv6Address' : {
        'meta_info' : _MetaInfoClass('Ipsla.Responder.TwampLight.SessionIds.SessionId.LocalIp.LocalIpv6Addresses.LocalIpv6Address', REFERENCE_LIST,
            '''Enter value of local ip address''',
            False, 
            [
            _MetaInfoClassMember('localv6-address', ATTRIBUTE, 'str', 'xr:Cisco-ios-xr-string',
                None, None,
                [], [b'[\\w\\-\\.:,_@#%$\\+=\\|;]+'],
                '''                Local IPv6 address
                ''',
                'localv6_address',
                'Cisco-IOS-XR-man-ipsla-cfg', True),
            _MetaInfoClassMember('local-port-numbers', REFERENCE_CLASS, 'LocalPortNumbers', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_ipsla_cfg', 'Ipsla.Responder.TwampLight.SessionIds.SessionId.LocalIp.LocalIpv6Addresses.LocalIpv6Address.LocalPortNumbers',
                [], [],
                '''                Configuration of local port
                ''',
                'local_port_numbers',
                'Cisco-IOS-XR-man-ipsla-cfg', False),
            ],
            'Cisco-IOS-XR-man-ipsla-cfg',
            'local-ipv6-address',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-man-ipsla-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_ipsla_cfg',
        ),
    },
    'Ipsla.Responder.TwampLight.SessionIds.SessionId.LocalIp.LocalIpv6Addresses' : {
        'meta_info' : _MetaInfoClass('Ipsla.Responder.TwampLight.SessionIds.SessionId.LocalIp.LocalIpv6Addresses', REFERENCE_CLASS,
            '''Configure IPV6 address''',
            False, 
            [
            _MetaInfoClassMember('local-ipv6-address', REFERENCE_LIST, 'LocalIpv6Address', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_ipsla_cfg', 'Ipsla.Responder.TwampLight.SessionIds.SessionId.LocalIp.LocalIpv6Addresses.LocalIpv6Address',
                [], [],
                '''                Enter value of local ip address
                ''',
                'local_ipv6_address',
                'Cisco-IOS-XR-man-ipsla-cfg', False),
            ],
            'Cisco-IOS-XR-man-ipsla-cfg',
            'local-ipv6-addresses',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-man-ipsla-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_ipsla_cfg',
        ),
    },
    'Ipsla.Responder.TwampLight.SessionIds.SessionId.LocalIp.LocalIpv4Addresses.LocalIpv4Address.LocalPortNumbers.LocalPortNumber.RemoteIp.RemoteIpv4Addresses.RemoteIpv4Address.RemotePortNumbers.RemotePortNumber.VrfNames.VrfName' : {
        'meta_info' : _MetaInfoClass('Ipsla.Responder.TwampLight.SessionIds.SessionId.LocalIp.LocalIpv4Addresses.LocalIpv4Address.LocalPortNumbers.LocalPortNumber.RemoteIp.RemoteIpv4Addresses.RemoteIpv4Address.RemotePortNumbers.RemotePortNumber.VrfNames.VrfName', REFERENCE_LIST,
            '''Configure vrf name value''',
            False, 
            [
            _MetaInfoClassMember('vrf-name', ATTRIBUTE, 'str', 'xr:Cisco-ios-xr-string',
                None, None,
                [(1, 32)], [],
                '''                VRF Name
                ''',
                'vrf_name',
                'Cisco-IOS-XR-man-ipsla-cfg', True),
            ],
            'Cisco-IOS-XR-man-ipsla-cfg',
            'vrf-name',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-man-ipsla-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_ipsla_cfg',
        ),
    },
    'Ipsla.Responder.TwampLight.SessionIds.SessionId.LocalIp.LocalIpv4Addresses.LocalIpv4Address.LocalPortNumbers.LocalPortNumber.RemoteIp.RemoteIpv4Addresses.RemoteIpv4Address.RemotePortNumbers.RemotePortNumber.VrfNames' : {
        'meta_info' : _MetaInfoClass('Ipsla.Responder.TwampLight.SessionIds.SessionId.LocalIp.LocalIpv4Addresses.LocalIpv4Address.LocalPortNumbers.LocalPortNumber.RemoteIp.RemoteIpv4Addresses.RemoteIpv4Address.RemotePortNumbers.RemotePortNumber.VrfNames', REFERENCE_CLASS,
            '''Configuration of vrf''',
            False, 
            [
            _MetaInfoClassMember('vrf-name', REFERENCE_LIST, 'VrfName', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_ipsla_cfg', 'Ipsla.Responder.TwampLight.SessionIds.SessionId.LocalIp.LocalIpv4Addresses.LocalIpv4Address.LocalPortNumbers.LocalPortNumber.RemoteIp.RemoteIpv4Addresses.RemoteIpv4Address.RemotePortNumbers.RemotePortNumber.VrfNames.VrfName',
                [], [],
                '''                Configure vrf name value
                ''',
                'vrf_name',
                'Cisco-IOS-XR-man-ipsla-cfg', False),
            ],
            'Cisco-IOS-XR-man-ipsla-cfg',
            'vrf-names',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-man-ipsla-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_ipsla_cfg',
        ),
    },
    'Ipsla.Responder.TwampLight.SessionIds.SessionId.LocalIp.LocalIpv4Addresses.LocalIpv4Address.LocalPortNumbers.LocalPortNumber.RemoteIp.RemoteIpv4Addresses.RemoteIpv4Address.RemotePortNumbers.RemotePortNumber' : {
        'meta_info' : _MetaInfoClass('Ipsla.Responder.TwampLight.SessionIds.SessionId.LocalIp.LocalIpv4Addresses.LocalIpv4Address.LocalPortNumbers.LocalPortNumber.RemoteIp.RemoteIpv4Addresses.RemoteIpv4Address.RemotePortNumbers.RemotePortNumber', REFERENCE_LIST,
            '''Enter value of remote port''',
            False, 
            [
            _MetaInfoClassMember('remote-port', ATTRIBUTE, 'int', 'inet:port-number',
                None, None,
                [('0', '65535')], [],
                '''                Remote port
                ''',
                'remote_port',
                'Cisco-IOS-XR-man-ipsla-cfg', True),
            _MetaInfoClassMember('vrf-names', REFERENCE_CLASS, 'VrfNames', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_ipsla_cfg', 'Ipsla.Responder.TwampLight.SessionIds.SessionId.LocalIp.LocalIpv4Addresses.LocalIpv4Address.LocalPortNumbers.LocalPortNumber.RemoteIp.RemoteIpv4Addresses.RemoteIpv4Address.RemotePortNumbers.RemotePortNumber.VrfNames',
                [], [],
                '''                Configuration of vrf
                ''',
                'vrf_names',
                'Cisco-IOS-XR-man-ipsla-cfg', False),
            ],
            'Cisco-IOS-XR-man-ipsla-cfg',
            'remote-port-number',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-man-ipsla-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_ipsla_cfg',
        ),
    },
    'Ipsla.Responder.TwampLight.SessionIds.SessionId.LocalIp.LocalIpv4Addresses.LocalIpv4Address.LocalPortNumbers.LocalPortNumber.RemoteIp.RemoteIpv4Addresses.RemoteIpv4Address.RemotePortNumbers' : {
        'meta_info' : _MetaInfoClass('Ipsla.Responder.TwampLight.SessionIds.SessionId.LocalIp.LocalIpv4Addresses.LocalIpv4Address.LocalPortNumbers.LocalPortNumber.RemoteIp.RemoteIpv4Addresses.RemoteIpv4Address.RemotePortNumbers', REFERENCE_CLASS,
            '''Configuration of remote port''',
            False, 
            [
            _MetaInfoClassMember('remote-port-number', REFERENCE_LIST, 'RemotePortNumber', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_ipsla_cfg', 'Ipsla.Responder.TwampLight.SessionIds.SessionId.LocalIp.LocalIpv4Addresses.LocalIpv4Address.LocalPortNumbers.LocalPortNumber.RemoteIp.RemoteIpv4Addresses.RemoteIpv4Address.RemotePortNumbers.RemotePortNumber',
                [], [],
                '''                Enter value of remote port
                ''',
                'remote_port_number',
                'Cisco-IOS-XR-man-ipsla-cfg', False),
            ],
            'Cisco-IOS-XR-man-ipsla-cfg',
            'remote-port-numbers',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-man-ipsla-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_ipsla_cfg',
        ),
    },
    'Ipsla.Responder.TwampLight.SessionIds.SessionId.LocalIp.LocalIpv4Addresses.LocalIpv4Address.LocalPortNumbers.LocalPortNumber.RemoteIp.RemoteIpv4Addresses.RemoteIpv4Address' : {
        'meta_info' : _MetaInfoClass('Ipsla.Responder.TwampLight.SessionIds.SessionId.LocalIp.LocalIpv4Addresses.LocalIpv4Address.LocalPortNumbers.LocalPortNumber.RemoteIp.RemoteIpv4Addresses.RemoteIpv4Address', REFERENCE_LIST,
            '''Enter value of remote ipv4 address''',
            False, 
            [
            _MetaInfoClassMember('remotev4-address', ATTRIBUTE, 'str', 'xr:Cisco-ios-xr-string',
                None, None,
                [], [b'[\\w\\-\\.:,_@#%$\\+=\\|;]+'],
                '''                Remote IPv4 address
                ''',
                'remotev4_address',
                'Cisco-IOS-XR-man-ipsla-cfg', True),
            _MetaInfoClassMember('remote-port-numbers', REFERENCE_CLASS, 'RemotePortNumbers', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_ipsla_cfg', 'Ipsla.Responder.TwampLight.SessionIds.SessionId.LocalIp.LocalIpv4Addresses.LocalIpv4Address.LocalPortNumbers.LocalPortNumber.RemoteIp.RemoteIpv4Addresses.RemoteIpv4Address.RemotePortNumbers',
                [], [],
                '''                Configuration of remote port
                ''',
                'remote_port_numbers',
                'Cisco-IOS-XR-man-ipsla-cfg', False),
            ],
            'Cisco-IOS-XR-man-ipsla-cfg',
            'remote-ipv4-address',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-man-ipsla-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_ipsla_cfg',
        ),
    },
    'Ipsla.Responder.TwampLight.SessionIds.SessionId.LocalIp.LocalIpv4Addresses.LocalIpv4Address.LocalPortNumbers.LocalPortNumber.RemoteIp.RemoteIpv4Addresses' : {
        'meta_info' : _MetaInfoClass('Ipsla.Responder.TwampLight.SessionIds.SessionId.LocalIp.LocalIpv4Addresses.LocalIpv4Address.LocalPortNumbers.LocalPortNumber.RemoteIp.RemoteIpv4Addresses', REFERENCE_CLASS,
            '''Configure IPV4 address''',
            False, 
            [
            _MetaInfoClassMember('remote-ipv4-address', REFERENCE_LIST, 'RemoteIpv4Address', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_ipsla_cfg', 'Ipsla.Responder.TwampLight.SessionIds.SessionId.LocalIp.LocalIpv4Addresses.LocalIpv4Address.LocalPortNumbers.LocalPortNumber.RemoteIp.RemoteIpv4Addresses.RemoteIpv4Address',
                [], [],
                '''                Enter value of remote ipv4 address
                ''',
                'remote_ipv4_address',
                'Cisco-IOS-XR-man-ipsla-cfg', False),
            ],
            'Cisco-IOS-XR-man-ipsla-cfg',
            'remote-ipv4-addresses',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-man-ipsla-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_ipsla_cfg',
        ),
    },
    'Ipsla.Responder.TwampLight.SessionIds.SessionId.LocalIp.LocalIpv4Addresses.LocalIpv4Address.LocalPortNumbers.LocalPortNumber.RemoteIp.RemoteIpv6Addresses.RemoteIpv6Address.RemotePortNumbers.RemotePortNumber.VrfNames.VrfName' : {
        'meta_info' : _MetaInfoClass('Ipsla.Responder.TwampLight.SessionIds.SessionId.LocalIp.LocalIpv4Addresses.LocalIpv4Address.LocalPortNumbers.LocalPortNumber.RemoteIp.RemoteIpv6Addresses.RemoteIpv6Address.RemotePortNumbers.RemotePortNumber.VrfNames.VrfName', REFERENCE_LIST,
            '''Configure vrf name value''',
            False, 
            [
            _MetaInfoClassMember('vrf-name', ATTRIBUTE, 'str', 'xr:Cisco-ios-xr-string',
                None, None,
                [(1, 32)], [],
                '''                VRF Name
                ''',
                'vrf_name',
                'Cisco-IOS-XR-man-ipsla-cfg', True),
            ],
            'Cisco-IOS-XR-man-ipsla-cfg',
            'vrf-name',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-man-ipsla-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_ipsla_cfg',
        ),
    },
    'Ipsla.Responder.TwampLight.SessionIds.SessionId.LocalIp.LocalIpv4Addresses.LocalIpv4Address.LocalPortNumbers.LocalPortNumber.RemoteIp.RemoteIpv6Addresses.RemoteIpv6Address.RemotePortNumbers.RemotePortNumber.VrfNames' : {
        'meta_info' : _MetaInfoClass('Ipsla.Responder.TwampLight.SessionIds.SessionId.LocalIp.LocalIpv4Addresses.LocalIpv4Address.LocalPortNumbers.LocalPortNumber.RemoteIp.RemoteIpv6Addresses.RemoteIpv6Address.RemotePortNumbers.RemotePortNumber.VrfNames', REFERENCE_CLASS,
            '''Configuration of vrf''',
            False, 
            [
            _MetaInfoClassMember('vrf-name', REFERENCE_LIST, 'VrfName', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_ipsla_cfg', 'Ipsla.Responder.TwampLight.SessionIds.SessionId.LocalIp.LocalIpv4Addresses.LocalIpv4Address.LocalPortNumbers.LocalPortNumber.RemoteIp.RemoteIpv6Addresses.RemoteIpv6Address.RemotePortNumbers.RemotePortNumber.VrfNames.VrfName',
                [], [],
                '''                Configure vrf name value
                ''',
                'vrf_name',
                'Cisco-IOS-XR-man-ipsla-cfg', False),
            ],
            'Cisco-IOS-XR-man-ipsla-cfg',
            'vrf-names',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-man-ipsla-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_ipsla_cfg',
        ),
    },
    'Ipsla.Responder.TwampLight.SessionIds.SessionId.LocalIp.LocalIpv4Addresses.LocalIpv4Address.LocalPortNumbers.LocalPortNumber.RemoteIp.RemoteIpv6Addresses.RemoteIpv6Address.RemotePortNumbers.RemotePortNumber' : {
        'meta_info' : _MetaInfoClass('Ipsla.Responder.TwampLight.SessionIds.SessionId.LocalIp.LocalIpv4Addresses.LocalIpv4Address.LocalPortNumbers.LocalPortNumber.RemoteIp.RemoteIpv6Addresses.RemoteIpv6Address.RemotePortNumbers.RemotePortNumber', REFERENCE_LIST,
            '''Enter value of remote port''',
            False, 
            [
            _MetaInfoClassMember('remote-port', ATTRIBUTE, 'int', 'inet:port-number',
                None, None,
                [('0', '65535')], [],
                '''                Remote port
                ''',
                'remote_port',
                'Cisco-IOS-XR-man-ipsla-cfg', True),
            _MetaInfoClassMember('vrf-names', REFERENCE_CLASS, 'VrfNames', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_ipsla_cfg', 'Ipsla.Responder.TwampLight.SessionIds.SessionId.LocalIp.LocalIpv4Addresses.LocalIpv4Address.LocalPortNumbers.LocalPortNumber.RemoteIp.RemoteIpv6Addresses.RemoteIpv6Address.RemotePortNumbers.RemotePortNumber.VrfNames',
                [], [],
                '''                Configuration of vrf
                ''',
                'vrf_names',
                'Cisco-IOS-XR-man-ipsla-cfg', False),
            ],
            'Cisco-IOS-XR-man-ipsla-cfg',
            'remote-port-number',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-man-ipsla-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_ipsla_cfg',
        ),
    },
    'Ipsla.Responder.TwampLight.SessionIds.SessionId.LocalIp.LocalIpv4Addresses.LocalIpv4Address.LocalPortNumbers.LocalPortNumber.RemoteIp.RemoteIpv6Addresses.RemoteIpv6Address.RemotePortNumbers' : {
        'meta_info' : _MetaInfoClass('Ipsla.Responder.TwampLight.SessionIds.SessionId.LocalIp.LocalIpv4Addresses.LocalIpv4Address.LocalPortNumbers.LocalPortNumber.RemoteIp.RemoteIpv6Addresses.RemoteIpv6Address.RemotePortNumbers', REFERENCE_CLASS,
            '''Configuration of remote port''',
            False, 
            [
            _MetaInfoClassMember('remote-port-number', REFERENCE_LIST, 'RemotePortNumber', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_ipsla_cfg', 'Ipsla.Responder.TwampLight.SessionIds.SessionId.LocalIp.LocalIpv4Addresses.LocalIpv4Address.LocalPortNumbers.LocalPortNumber.RemoteIp.RemoteIpv6Addresses.RemoteIpv6Address.RemotePortNumbers.RemotePortNumber',
                [], [],
                '''                Enter value of remote port
                ''',
                'remote_port_number',
                'Cisco-IOS-XR-man-ipsla-cfg', False),
            ],
            'Cisco-IOS-XR-man-ipsla-cfg',
            'remote-port-numbers',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-man-ipsla-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_ipsla_cfg',
        ),
    },
    'Ipsla.Responder.TwampLight.SessionIds.SessionId.LocalIp.LocalIpv4Addresses.LocalIpv4Address.LocalPortNumbers.LocalPortNumber.RemoteIp.RemoteIpv6Addresses.RemoteIpv6Address' : {
        'meta_info' : _MetaInfoClass('Ipsla.Responder.TwampLight.SessionIds.SessionId.LocalIp.LocalIpv4Addresses.LocalIpv4Address.LocalPortNumbers.LocalPortNumber.RemoteIp.RemoteIpv6Addresses.RemoteIpv6Address', REFERENCE_LIST,
            '''Enter value of remote ipv6 address''',
            False, 
            [
            _MetaInfoClassMember('remotev6-address', ATTRIBUTE, 'str', 'xr:Cisco-ios-xr-string',
                None, None,
                [], [b'[\\w\\-\\.:,_@#%$\\+=\\|;]+'],
                '''                Remote IPv6 address
                ''',
                'remotev6_address',
                'Cisco-IOS-XR-man-ipsla-cfg', True),
            _MetaInfoClassMember('remote-port-numbers', REFERENCE_CLASS, 'RemotePortNumbers', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_ipsla_cfg', 'Ipsla.Responder.TwampLight.SessionIds.SessionId.LocalIp.LocalIpv4Addresses.LocalIpv4Address.LocalPortNumbers.LocalPortNumber.RemoteIp.RemoteIpv6Addresses.RemoteIpv6Address.RemotePortNumbers',
                [], [],
                '''                Configuration of remote port
                ''',
                'remote_port_numbers',
                'Cisco-IOS-XR-man-ipsla-cfg', False),
            ],
            'Cisco-IOS-XR-man-ipsla-cfg',
            'remote-ipv6-address',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-man-ipsla-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_ipsla_cfg',
        ),
    },
    'Ipsla.Responder.TwampLight.SessionIds.SessionId.LocalIp.LocalIpv4Addresses.LocalIpv4Address.LocalPortNumbers.LocalPortNumber.RemoteIp.RemoteIpv6Addresses' : {
        'meta_info' : _MetaInfoClass('Ipsla.Responder.TwampLight.SessionIds.SessionId.LocalIp.LocalIpv4Addresses.LocalIpv4Address.LocalPortNumbers.LocalPortNumber.RemoteIp.RemoteIpv6Addresses', REFERENCE_CLASS,
            '''Configure IPV6 address''',
            False, 
            [
            _MetaInfoClassMember('remote-ipv6-address', REFERENCE_LIST, 'RemoteIpv6Address', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_ipsla_cfg', 'Ipsla.Responder.TwampLight.SessionIds.SessionId.LocalIp.LocalIpv4Addresses.LocalIpv4Address.LocalPortNumbers.LocalPortNumber.RemoteIp.RemoteIpv6Addresses.RemoteIpv6Address',
                [], [],
                '''                Enter value of remote ipv6 address
                ''',
                'remote_ipv6_address',
                'Cisco-IOS-XR-man-ipsla-cfg', False),
            ],
            'Cisco-IOS-XR-man-ipsla-cfg',
            'remote-ipv6-addresses',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-man-ipsla-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_ipsla_cfg',
        ),
    },
    'Ipsla.Responder.TwampLight.SessionIds.SessionId.LocalIp.LocalIpv4Addresses.LocalIpv4Address.LocalPortNumbers.LocalPortNumber.RemoteIp' : {
        'meta_info' : _MetaInfoClass('Ipsla.Responder.TwampLight.SessionIds.SessionId.LocalIp.LocalIpv4Addresses.LocalIpv4Address.LocalPortNumbers.LocalPortNumber.RemoteIp', REFERENCE_CLASS,
            '''Configure remote ip address''',
            False, 
            [
            _MetaInfoClassMember('remote-ipv4-addresses', REFERENCE_CLASS, 'RemoteIpv4Addresses', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_ipsla_cfg', 'Ipsla.Responder.TwampLight.SessionIds.SessionId.LocalIp.LocalIpv4Addresses.LocalIpv4Address.LocalPortNumbers.LocalPortNumber.RemoteIp.RemoteIpv4Addresses',
                [], [],
                '''                Configure IPV4 address
                ''',
                'remote_ipv4_addresses',
                'Cisco-IOS-XR-man-ipsla-cfg', False),
            _MetaInfoClassMember('remote-ipv6-addresses', REFERENCE_CLASS, 'RemoteIpv6Addresses', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_ipsla_cfg', 'Ipsla.Responder.TwampLight.SessionIds.SessionId.LocalIp.LocalIpv4Addresses.LocalIpv4Address.LocalPortNumbers.LocalPortNumber.RemoteIp.RemoteIpv6Addresses',
                [], [],
                '''                Configure IPV6 address
                ''',
                'remote_ipv6_addresses',
                'Cisco-IOS-XR-man-ipsla-cfg', False),
            ],
            'Cisco-IOS-XR-man-ipsla-cfg',
            'remote-ip',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-man-ipsla-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_ipsla_cfg',
        ),
    },
    'Ipsla.Responder.TwampLight.SessionIds.SessionId.LocalIp.LocalIpv4Addresses.LocalIpv4Address.LocalPortNumbers.LocalPortNumber' : {
        'meta_info' : _MetaInfoClass('Ipsla.Responder.TwampLight.SessionIds.SessionId.LocalIp.LocalIpv4Addresses.LocalIpv4Address.LocalPortNumbers.LocalPortNumber', REFERENCE_LIST,
            '''Enter value of local port''',
            False, 
            [
            _MetaInfoClassMember('local-port', ATTRIBUTE, 'int', 'inet:port-number',
                None, None,
                [('0', '65535')], [],
                '''                Local port
                ''',
                'local_port',
                'Cisco-IOS-XR-man-ipsla-cfg', True),
            _MetaInfoClassMember('remote-ip', REFERENCE_CLASS, 'RemoteIp', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_ipsla_cfg', 'Ipsla.Responder.TwampLight.SessionIds.SessionId.LocalIp.LocalIpv4Addresses.LocalIpv4Address.LocalPortNumbers.LocalPortNumber.RemoteIp',
                [], [],
                '''                Configure remote ip address
                ''',
                'remote_ip',
                'Cisco-IOS-XR-man-ipsla-cfg', False),
            ],
            'Cisco-IOS-XR-man-ipsla-cfg',
            'local-port-number',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-man-ipsla-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_ipsla_cfg',
        ),
    },
    'Ipsla.Responder.TwampLight.SessionIds.SessionId.LocalIp.LocalIpv4Addresses.LocalIpv4Address.LocalPortNumbers' : {
        'meta_info' : _MetaInfoClass('Ipsla.Responder.TwampLight.SessionIds.SessionId.LocalIp.LocalIpv4Addresses.LocalIpv4Address.LocalPortNumbers', REFERENCE_CLASS,
            '''Configuration of local port''',
            False, 
            [
            _MetaInfoClassMember('local-port-number', REFERENCE_LIST, 'LocalPortNumber', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_ipsla_cfg', 'Ipsla.Responder.TwampLight.SessionIds.SessionId.LocalIp.LocalIpv4Addresses.LocalIpv4Address.LocalPortNumbers.LocalPortNumber',
                [], [],
                '''                Enter value of local port
                ''',
                'local_port_number',
                'Cisco-IOS-XR-man-ipsla-cfg', False),
            ],
            'Cisco-IOS-XR-man-ipsla-cfg',
            'local-port-numbers',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-man-ipsla-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_ipsla_cfg',
        ),
    },
    'Ipsla.Responder.TwampLight.SessionIds.SessionId.LocalIp.LocalIpv4Addresses.LocalIpv4Address' : {
        'meta_info' : _MetaInfoClass('Ipsla.Responder.TwampLight.SessionIds.SessionId.LocalIp.LocalIpv4Addresses.LocalIpv4Address', REFERENCE_LIST,
            '''Enter value of local ipv4 address''',
            False, 
            [
            _MetaInfoClassMember('localv4-address', ATTRIBUTE, 'str', 'xr:Cisco-ios-xr-string',
                None, None,
                [], [b'[\\w\\-\\.:,_@#%$\\+=\\|;]+'],
                '''                Local IPv4 address
                ''',
                'localv4_address',
                'Cisco-IOS-XR-man-ipsla-cfg', True),
            _MetaInfoClassMember('local-port-numbers', REFERENCE_CLASS, 'LocalPortNumbers', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_ipsla_cfg', 'Ipsla.Responder.TwampLight.SessionIds.SessionId.LocalIp.LocalIpv4Addresses.LocalIpv4Address.LocalPortNumbers',
                [], [],
                '''                Configuration of local port
                ''',
                'local_port_numbers',
                'Cisco-IOS-XR-man-ipsla-cfg', False),
            ],
            'Cisco-IOS-XR-man-ipsla-cfg',
            'local-ipv4-address',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-man-ipsla-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_ipsla_cfg',
        ),
    },
    'Ipsla.Responder.TwampLight.SessionIds.SessionId.LocalIp.LocalIpv4Addresses' : {
        'meta_info' : _MetaInfoClass('Ipsla.Responder.TwampLight.SessionIds.SessionId.LocalIp.LocalIpv4Addresses', REFERENCE_CLASS,
            '''Configure IPV4 address''',
            False, 
            [
            _MetaInfoClassMember('local-ipv4-address', REFERENCE_LIST, 'LocalIpv4Address', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_ipsla_cfg', 'Ipsla.Responder.TwampLight.SessionIds.SessionId.LocalIp.LocalIpv4Addresses.LocalIpv4Address',
                [], [],
                '''                Enter value of local ipv4 address
                ''',
                'local_ipv4_address',
                'Cisco-IOS-XR-man-ipsla-cfg', False),
            ],
            'Cisco-IOS-XR-man-ipsla-cfg',
            'local-ipv4-addresses',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-man-ipsla-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_ipsla_cfg',
        ),
    },
    'Ipsla.Responder.TwampLight.SessionIds.SessionId.LocalIp' : {
        'meta_info' : _MetaInfoClass('Ipsla.Responder.TwampLight.SessionIds.SessionId.LocalIp', REFERENCE_CLASS,
            '''Configure local ip address''',
            False, 
            [
            _MetaInfoClassMember('local-ipv6-addresses', REFERENCE_CLASS, 'LocalIpv6Addresses', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_ipsla_cfg', 'Ipsla.Responder.TwampLight.SessionIds.SessionId.LocalIp.LocalIpv6Addresses',
                [], [],
                '''                Configure IPV6 address
                ''',
                'local_ipv6_addresses',
                'Cisco-IOS-XR-man-ipsla-cfg', False),
            _MetaInfoClassMember('local-ipv4-addresses', REFERENCE_CLASS, 'LocalIpv4Addresses', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_ipsla_cfg', 'Ipsla.Responder.TwampLight.SessionIds.SessionId.LocalIp.LocalIpv4Addresses',
                [], [],
                '''                Configure IPV4 address
                ''',
                'local_ipv4_addresses',
                'Cisco-IOS-XR-man-ipsla-cfg', False),
            ],
            'Cisco-IOS-XR-man-ipsla-cfg',
            'local-ip',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-man-ipsla-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_ipsla_cfg',
        ),
    },
    'Ipsla.Responder.TwampLight.SessionIds.SessionId' : {
        'meta_info' : _MetaInfoClass('Ipsla.Responder.TwampLight.SessionIds.SessionId', REFERENCE_LIST,
            '''Configure session ID''',
            False, 
            [
            _MetaInfoClassMember('session-id', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('1', '5')], [],
                '''                SessionID
                ''',
                'session_id',
                'Cisco-IOS-XR-man-ipsla-cfg', True),
            _MetaInfoClassMember('local-ip', REFERENCE_CLASS, 'LocalIp', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_ipsla_cfg', 'Ipsla.Responder.TwampLight.SessionIds.SessionId.LocalIp',
                [], [],
                '''                Configure local ip address
                ''',
                'local_ip',
                'Cisco-IOS-XR-man-ipsla-cfg', False),
            _MetaInfoClassMember('twamp-light-timeout', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('60', '86400')], [],
                '''                Configure session timeout
                ''',
                'twamp_light_timeout',
                'Cisco-IOS-XR-man-ipsla-cfg', False),
            ],
            'Cisco-IOS-XR-man-ipsla-cfg',
            'session-id',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-man-ipsla-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_ipsla_cfg',
        ),
    },
    'Ipsla.Responder.TwampLight.SessionIds' : {
        'meta_info' : _MetaInfoClass('Ipsla.Responder.TwampLight.SessionIds', REFERENCE_CLASS,
            '''Create twamp-light session''',
            False, 
            [
            _MetaInfoClassMember('session-id', REFERENCE_LIST, 'SessionId', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_ipsla_cfg', 'Ipsla.Responder.TwampLight.SessionIds.SessionId',
                [], [],
                '''                Configure session ID
                ''',
                'session_id',
                'Cisco-IOS-XR-man-ipsla-cfg', False),
            ],
            'Cisco-IOS-XR-man-ipsla-cfg',
            'session-ids',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-man-ipsla-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_ipsla_cfg',
        ),
    },
    'Ipsla.Responder.TwampLight' : {
        'meta_info' : _MetaInfoClass('Ipsla.Responder.TwampLight', REFERENCE_CLASS,
            '''Enter twamp-light session details''',
            False, 
            [
            _MetaInfoClassMember('session-ids', REFERENCE_CLASS, 'SessionIds', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_ipsla_cfg', 'Ipsla.Responder.TwampLight.SessionIds',
                [], [],
                '''                Create twamp-light session
                ''',
                'session_ids',
                'Cisco-IOS-XR-man-ipsla-cfg', False),
            ],
            'Cisco-IOS-XR-man-ipsla-cfg',
            'twamp-light',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-man-ipsla-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_ipsla_cfg',
        ),
    },
    'Ipsla.Responder' : {
        'meta_info' : _MetaInfoClass('Ipsla.Responder', REFERENCE_CLASS,
            '''Responder configuration''',
            False, 
            [
            _MetaInfoClassMember('twamp', REFERENCE_CLASS, 'Twamp', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_ipsla_cfg', 'Ipsla.Responder.Twamp',
                [], [],
                '''                Responder TWAMP configuration
                ''',
                'twamp',
                'Cisco-IOS-XR-man-ipsla-cfg', False, is_presence=True),
            _MetaInfoClassMember('type', REFERENCE_CLASS, 'Type', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_ipsla_cfg', 'Ipsla.Responder.Type',
                [], [],
                '''                Configure IPSLA Responder port type
                ''',
                'type',
                'Cisco-IOS-XR-man-ipsla-cfg', False),
            _MetaInfoClassMember('twamp-light', REFERENCE_CLASS, 'TwampLight', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_ipsla_cfg', 'Ipsla.Responder.TwampLight',
                [], [],
                '''                Enter twamp-light session details
                ''',
                'twamp_light',
                'Cisco-IOS-XR-man-ipsla-cfg', False),
            ],
            'Cisco-IOS-XR-man-ipsla-cfg',
            'responder',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-man-ipsla-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_ipsla_cfg',
            is_presence=True,
        ),
    },
    'Ipsla.MplsDiscovery.Vpn' : {
        'meta_info' : _MetaInfoClass('Ipsla.MplsDiscovery.Vpn', REFERENCE_CLASS,
            '''Layer 3 VPN PE discovery configuration''',
            False, 
            [
            _MetaInfoClassMember('interval', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('30', '70560')], [],
                '''                Specify a discovery refresh interval
                ''',
                'interval',
                'Cisco-IOS-XR-man-ipsla-cfg', False, default_value="300"),
            ],
            'Cisco-IOS-XR-man-ipsla-cfg',
            'vpn',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-man-ipsla-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_ipsla_cfg',
        ),
    },
    'Ipsla.MplsDiscovery' : {
        'meta_info' : _MetaInfoClass('Ipsla.MplsDiscovery', REFERENCE_CLASS,
            '''Provider Edge(PE) discovery configuration''',
            False, 
            [
            _MetaInfoClassMember('vpn', REFERENCE_CLASS, 'Vpn', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_ipsla_cfg', 'Ipsla.MplsDiscovery.Vpn',
                [], [],
                '''                Layer 3 VPN PE discovery configuration
                ''',
                'vpn',
                'Cisco-IOS-XR-man-ipsla-cfg', False),
            ],
            'Cisco-IOS-XR-man-ipsla-cfg',
            'mpls-discovery',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-man-ipsla-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_ipsla_cfg',
        ),
    },
    'Ipsla.ServerTwamp' : {
        'meta_info' : _MetaInfoClass('Ipsla.ServerTwamp', REFERENCE_CLASS,
            '''IPPM Server configuration''',
            False, 
            [
            _MetaInfoClassMember('inactivity-timer', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('1', '6000')], [],
                '''                Configure ippmserver inactivity timer value in
                seconds
                ''',
                'inactivity_timer',
                'Cisco-IOS-XR-man-ipsla-cfg', False, default_value="900"),
            _MetaInfoClassMember('port', ATTRIBUTE, 'int', 'xr:Cisco-ios-xr-port-number',
                None, None,
                [('1', '65535')], [],
                '''                Configure port number for ippmserver listening
                port
                ''',
                'port',
                'Cisco-IOS-XR-man-ipsla-cfg', False, default_value="862"),
            ],
            'Cisco-IOS-XR-man-ipsla-cfg',
            'server-twamp',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-man-ipsla-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_ipsla_cfg',
            is_presence=True,
        ),
    },
    'Ipsla' : {
        'meta_info' : _MetaInfoClass('Ipsla', REFERENCE_CLASS,
            '''IPSLA configuration''',
            False, 
            [
            _MetaInfoClassMember('common', REFERENCE_CLASS, 'Common', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_ipsla_cfg', 'Ipsla.Common',
                [], [],
                '''                IPSLA application common configuration
                ''',
                'common',
                'Cisco-IOS-XR-man-ipsla-cfg', False),
            _MetaInfoClassMember('mpls-lsp-monitor', REFERENCE_CLASS, 'MplsLspMonitor', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_ipsla_cfg', 'Ipsla.MplsLspMonitor',
                [], [],
                '''                MPLS LSP Monitor(MPLSLM) configuration
                ''',
                'mpls_lsp_monitor',
                'Cisco-IOS-XR-man-ipsla-cfg', False),
            _MetaInfoClassMember('operation', REFERENCE_CLASS, 'Operation', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_ipsla_cfg', 'Ipsla.Operation',
                [], [],
                '''                IPSLA Operation configuration
                ''',
                'operation_',
                'Cisco-IOS-XR-man-ipsla-cfg', False),
            _MetaInfoClassMember('responder', REFERENCE_CLASS, 'Responder', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_ipsla_cfg', 'Ipsla.Responder',
                [], [],
                '''                Responder configuration
                ''',
                'responder',
                'Cisco-IOS-XR-man-ipsla-cfg', False, is_presence=True),
            _MetaInfoClassMember('mpls-discovery', REFERENCE_CLASS, 'MplsDiscovery', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_ipsla_cfg', 'Ipsla.MplsDiscovery',
                [], [],
                '''                Provider Edge(PE) discovery configuration
                ''',
                'mpls_discovery',
                'Cisco-IOS-XR-man-ipsla-cfg', False),
            _MetaInfoClassMember('server-twamp', REFERENCE_CLASS, 'ServerTwamp', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_ipsla_cfg', 'Ipsla.ServerTwamp',
                [], [],
                '''                IPPM Server configuration
                ''',
                'server_twamp',
                'Cisco-IOS-XR-man-ipsla-cfg', False, is_presence=True),
            ],
            'Cisco-IOS-XR-man-ipsla-cfg',
            'ipsla',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-man-ipsla-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_ipsla_cfg',
        ),
    },
}
_meta_table['Ipsla.Common.HardwareTimestamp']['meta_info'].parent =_meta_table['Ipsla.Common']['meta_info']
_meta_table['Ipsla.Common.Authentication']['meta_info'].parent =_meta_table['Ipsla.Common']['meta_info']
_meta_table['Ipsla.MplsLspMonitor.Reactions.Reaction.Condition.LpdTreeTrace.ActionType']['meta_info'].parent =_meta_table['Ipsla.MplsLspMonitor.Reactions.Reaction.Condition.LpdTreeTrace']['meta_info']
_meta_table['Ipsla.MplsLspMonitor.Reactions.Reaction.Condition.Timeout.ActionType']['meta_info'].parent =_meta_table['Ipsla.MplsLspMonitor.Reactions.Reaction.Condition.Timeout']['meta_info']
_meta_table['Ipsla.MplsLspMonitor.Reactions.Reaction.Condition.Timeout.ThresholdType']['meta_info'].parent =_meta_table['Ipsla.MplsLspMonitor.Reactions.Reaction.Condition.Timeout']['meta_info']
_meta_table['Ipsla.MplsLspMonitor.Reactions.Reaction.Condition.LpdGroup.ActionType']['meta_info'].parent =_meta_table['Ipsla.MplsLspMonitor.Reactions.Reaction.Condition.LpdGroup']['meta_info']
_meta_table['Ipsla.MplsLspMonitor.Reactions.Reaction.Condition.ConnectionLoss.ActionType']['meta_info'].parent =_meta_table['Ipsla.MplsLspMonitor.Reactions.Reaction.Condition.ConnectionLoss']['meta_info']
_meta_table['Ipsla.MplsLspMonitor.Reactions.Reaction.Condition.ConnectionLoss.ThresholdType']['meta_info'].parent =_meta_table['Ipsla.MplsLspMonitor.Reactions.Reaction.Condition.ConnectionLoss']['meta_info']
_meta_table['Ipsla.MplsLspMonitor.Reactions.Reaction.Condition.LpdTreeTrace']['meta_info'].parent =_meta_table['Ipsla.MplsLspMonitor.Reactions.Reaction.Condition']['meta_info']
_meta_table['Ipsla.MplsLspMonitor.Reactions.Reaction.Condition.Timeout']['meta_info'].parent =_meta_table['Ipsla.MplsLspMonitor.Reactions.Reaction.Condition']['meta_info']
_meta_table['Ipsla.MplsLspMonitor.Reactions.Reaction.Condition.LpdGroup']['meta_info'].parent =_meta_table['Ipsla.MplsLspMonitor.Reactions.Reaction.Condition']['meta_info']
_meta_table['Ipsla.MplsLspMonitor.Reactions.Reaction.Condition.ConnectionLoss']['meta_info'].parent =_meta_table['Ipsla.MplsLspMonitor.Reactions.Reaction.Condition']['meta_info']
_meta_table['Ipsla.MplsLspMonitor.Reactions.Reaction.Condition']['meta_info'].parent =_meta_table['Ipsla.MplsLspMonitor.Reactions.Reaction']['meta_info']
_meta_table['Ipsla.MplsLspMonitor.Reactions.Reaction']['meta_info'].parent =_meta_table['Ipsla.MplsLspMonitor.Reactions']['meta_info']
_meta_table['Ipsla.MplsLspMonitor.Schedules.Schedule.StartTime']['meta_info'].parent =_meta_table['Ipsla.MplsLspMonitor.Schedules.Schedule']['meta_info']
_meta_table['Ipsla.MplsLspMonitor.Schedules.Schedule']['meta_info'].parent =_meta_table['Ipsla.MplsLspMonitor.Schedules']['meta_info']
_meta_table['Ipsla.MplsLspMonitor.Definitions.Definition.OperationType.MplsLspTrace.Reply']['meta_info'].parent =_meta_table['Ipsla.MplsLspMonitor.Definitions.Definition.OperationType.MplsLspTrace']['meta_info']
_meta_table['Ipsla.MplsLspMonitor.Definitions.Definition.OperationType.MplsLspTrace.Statistics']['meta_info'].parent =_meta_table['Ipsla.MplsLspMonitor.Definitions.Definition.OperationType.MplsLspTrace']['meta_info']
_meta_table['Ipsla.MplsLspMonitor.Definitions.Definition.OperationType.MplsLspTrace.Scan']['meta_info'].parent =_meta_table['Ipsla.MplsLspMonitor.Definitions.Definition.OperationType.MplsLspTrace']['meta_info']
_meta_table['Ipsla.MplsLspMonitor.Definitions.Definition.OperationType.MplsLspPing.PathDiscover.Path.SecondaryFrequency']['meta_info'].parent =_meta_table['Ipsla.MplsLspMonitor.Definitions.Definition.OperationType.MplsLspPing.PathDiscover.Path']['meta_info']
_meta_table['Ipsla.MplsLspMonitor.Definitions.Definition.OperationType.MplsLspPing.PathDiscover.Echo.Multipath']['meta_info'].parent =_meta_table['Ipsla.MplsLspMonitor.Definitions.Definition.OperationType.MplsLspPing.PathDiscover.Echo']['meta_info']
_meta_table['Ipsla.MplsLspMonitor.Definitions.Definition.OperationType.MplsLspPing.PathDiscover.Session']['meta_info'].parent =_meta_table['Ipsla.MplsLspMonitor.Definitions.Definition.OperationType.MplsLspPing.PathDiscover']['meta_info']
_meta_table['Ipsla.MplsLspMonitor.Definitions.Definition.OperationType.MplsLspPing.PathDiscover.Path']['meta_info'].parent =_meta_table['Ipsla.MplsLspMonitor.Definitions.Definition.OperationType.MplsLspPing.PathDiscover']['meta_info']
_meta_table['Ipsla.MplsLspMonitor.Definitions.Definition.OperationType.MplsLspPing.PathDiscover.Echo']['meta_info'].parent =_meta_table['Ipsla.MplsLspMonitor.Definitions.Definition.OperationType.MplsLspPing.PathDiscover']['meta_info']
_meta_table['Ipsla.MplsLspMonitor.Definitions.Definition.OperationType.MplsLspPing.DataSize']['meta_info'].parent =_meta_table['Ipsla.MplsLspMonitor.Definitions.Definition.OperationType.MplsLspPing']['meta_info']
_meta_table['Ipsla.MplsLspMonitor.Definitions.Definition.OperationType.MplsLspPing.PathDiscover']['meta_info'].parent =_meta_table['Ipsla.MplsLspMonitor.Definitions.Definition.OperationType.MplsLspPing']['meta_info']
_meta_table['Ipsla.MplsLspMonitor.Definitions.Definition.OperationType.MplsLspPing.Reply']['meta_info'].parent =_meta_table['Ipsla.MplsLspMonitor.Definitions.Definition.OperationType.MplsLspPing']['meta_info']
_meta_table['Ipsla.MplsLspMonitor.Definitions.Definition.OperationType.MplsLspPing.Statistics']['meta_info'].parent =_meta_table['Ipsla.MplsLspMonitor.Definitions.Definition.OperationType.MplsLspPing']['meta_info']
_meta_table['Ipsla.MplsLspMonitor.Definitions.Definition.OperationType.MplsLspPing.Scan']['meta_info'].parent =_meta_table['Ipsla.MplsLspMonitor.Definitions.Definition.OperationType.MplsLspPing']['meta_info']
_meta_table['Ipsla.MplsLspMonitor.Definitions.Definition.OperationType.MplsLspTrace']['meta_info'].parent =_meta_table['Ipsla.MplsLspMonitor.Definitions.Definition.OperationType']['meta_info']
_meta_table['Ipsla.MplsLspMonitor.Definitions.Definition.OperationType.MplsLspPing']['meta_info'].parent =_meta_table['Ipsla.MplsLspMonitor.Definitions.Definition.OperationType']['meta_info']
_meta_table['Ipsla.MplsLspMonitor.Definitions.Definition.OperationType']['meta_info'].parent =_meta_table['Ipsla.MplsLspMonitor.Definitions.Definition']['meta_info']
_meta_table['Ipsla.MplsLspMonitor.Definitions.Definition']['meta_info'].parent =_meta_table['Ipsla.MplsLspMonitor.Definitions']['meta_info']
_meta_table['Ipsla.MplsLspMonitor.Reactions']['meta_info'].parent =_meta_table['Ipsla.MplsLspMonitor']['meta_info']
_meta_table['Ipsla.MplsLspMonitor.Schedules']['meta_info'].parent =_meta_table['Ipsla.MplsLspMonitor']['meta_info']
_meta_table['Ipsla.MplsLspMonitor.Definitions']['meta_info'].parent =_meta_table['Ipsla.MplsLspMonitor']['meta_info']
_meta_table['Ipsla.Operation.Schedules.Schedule.StartTime']['meta_info'].parent =_meta_table['Ipsla.Operation.Schedules.Schedule']['meta_info']
_meta_table['Ipsla.Operation.Schedules.Schedule']['meta_info'].parent =_meta_table['Ipsla.Operation.Schedules']['meta_info']
_meta_table['Ipsla.Operation.Reactions.Reaction.Condition.JitterAverageDs.ThresholdLimits']['meta_info'].parent =_meta_table['Ipsla.Operation.Reactions.Reaction.Condition.JitterAverageDs']['meta_info']
_meta_table['Ipsla.Operation.Reactions.Reaction.Condition.JitterAverageDs.ActionType']['meta_info'].parent =_meta_table['Ipsla.Operation.Reactions.Reaction.Condition.JitterAverageDs']['meta_info']
_meta_table['Ipsla.Operation.Reactions.Reaction.Condition.JitterAverageDs.ThresholdType']['meta_info'].parent =_meta_table['Ipsla.Operation.Reactions.Reaction.Condition.JitterAverageDs']['meta_info']
_meta_table['Ipsla.Operation.Reactions.Reaction.Condition.Timeout.ActionType']['meta_info'].parent =_meta_table['Ipsla.Operation.Reactions.Reaction.Condition.Timeout']['meta_info']
_meta_table['Ipsla.Operation.Reactions.Reaction.Condition.Timeout.ThresholdType']['meta_info'].parent =_meta_table['Ipsla.Operation.Reactions.Reaction.Condition.Timeout']['meta_info']
_meta_table['Ipsla.Operation.Reactions.Reaction.Condition.JitterAverage.ThresholdLimits']['meta_info'].parent =_meta_table['Ipsla.Operation.Reactions.Reaction.Condition.JitterAverage']['meta_info']
_meta_table['Ipsla.Operation.Reactions.Reaction.Condition.JitterAverage.ActionType']['meta_info'].parent =_meta_table['Ipsla.Operation.Reactions.Reaction.Condition.JitterAverage']['meta_info']
_meta_table['Ipsla.Operation.Reactions.Reaction.Condition.JitterAverage.ThresholdType']['meta_info'].parent =_meta_table['Ipsla.Operation.Reactions.Reaction.Condition.JitterAverage']['meta_info']
_meta_table['Ipsla.Operation.Reactions.Reaction.Condition.VerifyError.ActionType']['meta_info'].parent =_meta_table['Ipsla.Operation.Reactions.Reaction.Condition.VerifyError']['meta_info']
_meta_table['Ipsla.Operation.Reactions.Reaction.Condition.VerifyError.ThresholdType']['meta_info'].parent =_meta_table['Ipsla.Operation.Reactions.Reaction.Condition.VerifyError']['meta_info']
_meta_table['Ipsla.Operation.Reactions.Reaction.Condition.Rtt.ThresholdLimits']['meta_info'].parent =_meta_table['Ipsla.Operation.Reactions.Reaction.Condition.Rtt']['meta_info']
_meta_table['Ipsla.Operation.Reactions.Reaction.Condition.Rtt.ActionType']['meta_info'].parent =_meta_table['Ipsla.Operation.Reactions.Reaction.Condition.Rtt']['meta_info']
_meta_table['Ipsla.Operation.Reactions.Reaction.Condition.Rtt.ThresholdType']['meta_info'].parent =_meta_table['Ipsla.Operation.Reactions.Reaction.Condition.Rtt']['meta_info']
_meta_table['Ipsla.Operation.Reactions.Reaction.Condition.PacketLossSd.ThresholdLimits']['meta_info'].parent =_meta_table['Ipsla.Operation.Reactions.Reaction.Condition.PacketLossSd']['meta_info']
_meta_table['Ipsla.Operation.Reactions.Reaction.Condition.PacketLossSd.ActionType']['meta_info'].parent =_meta_table['Ipsla.Operation.Reactions.Reaction.Condition.PacketLossSd']['meta_info']
_meta_table['Ipsla.Operation.Reactions.Reaction.Condition.PacketLossSd.ThresholdType']['meta_info'].parent =_meta_table['Ipsla.Operation.Reactions.Reaction.Condition.PacketLossSd']['meta_info']
_meta_table['Ipsla.Operation.Reactions.Reaction.Condition.JitterAverageSd.ThresholdLimits']['meta_info'].parent =_meta_table['Ipsla.Operation.Reactions.Reaction.Condition.JitterAverageSd']['meta_info']
_meta_table['Ipsla.Operation.Reactions.Reaction.Condition.JitterAverageSd.ActionType']['meta_info'].parent =_meta_table['Ipsla.Operation.Reactions.Reaction.Condition.JitterAverageSd']['meta_info']
_meta_table['Ipsla.Operation.Reactions.Reaction.Condition.JitterAverageSd.ThresholdType']['meta_info'].parent =_meta_table['Ipsla.Operation.Reactions.Reaction.Condition.JitterAverageSd']['meta_info']
_meta_table['Ipsla.Operation.Reactions.Reaction.Condition.ConnectionLoss.ActionType']['meta_info'].parent =_meta_table['Ipsla.Operation.Reactions.Reaction.Condition.ConnectionLoss']['meta_info']
_meta_table['Ipsla.Operation.Reactions.Reaction.Condition.ConnectionLoss.ThresholdType']['meta_info'].parent =_meta_table['Ipsla.Operation.Reactions.Reaction.Condition.ConnectionLoss']['meta_info']
_meta_table['Ipsla.Operation.Reactions.Reaction.Condition.PacketLossDs.ThresholdLimits']['meta_info'].parent =_meta_table['Ipsla.Operation.Reactions.Reaction.Condition.PacketLossDs']['meta_info']
_meta_table['Ipsla.Operation.Reactions.Reaction.Condition.PacketLossDs.ActionType']['meta_info'].parent =_meta_table['Ipsla.Operation.Reactions.Reaction.Condition.PacketLossDs']['meta_info']
_meta_table['Ipsla.Operation.Reactions.Reaction.Condition.PacketLossDs.ThresholdType']['meta_info'].parent =_meta_table['Ipsla.Operation.Reactions.Reaction.Condition.PacketLossDs']['meta_info']
_meta_table['Ipsla.Operation.Reactions.Reaction.Condition.JitterAverageDs']['meta_info'].parent =_meta_table['Ipsla.Operation.Reactions.Reaction.Condition']['meta_info']
_meta_table['Ipsla.Operation.Reactions.Reaction.Condition.Timeout']['meta_info'].parent =_meta_table['Ipsla.Operation.Reactions.Reaction.Condition']['meta_info']
_meta_table['Ipsla.Operation.Reactions.Reaction.Condition.JitterAverage']['meta_info'].parent =_meta_table['Ipsla.Operation.Reactions.Reaction.Condition']['meta_info']
_meta_table['Ipsla.Operation.Reactions.Reaction.Condition.VerifyError']['meta_info'].parent =_meta_table['Ipsla.Operation.Reactions.Reaction.Condition']['meta_info']
_meta_table['Ipsla.Operation.Reactions.Reaction.Condition.Rtt']['meta_info'].parent =_meta_table['Ipsla.Operation.Reactions.Reaction.Condition']['meta_info']
_meta_table['Ipsla.Operation.Reactions.Reaction.Condition.PacketLossSd']['meta_info'].parent =_meta_table['Ipsla.Operation.Reactions.Reaction.Condition']['meta_info']
_meta_table['Ipsla.Operation.Reactions.Reaction.Condition.JitterAverageSd']['meta_info'].parent =_meta_table['Ipsla.Operation.Reactions.Reaction.Condition']['meta_info']
_meta_table['Ipsla.Operation.Reactions.Reaction.Condition.ConnectionLoss']['meta_info'].parent =_meta_table['Ipsla.Operation.Reactions.Reaction.Condition']['meta_info']
_meta_table['Ipsla.Operation.Reactions.Reaction.Condition.PacketLossDs']['meta_info'].parent =_meta_table['Ipsla.Operation.Reactions.Reaction.Condition']['meta_info']
_meta_table['Ipsla.Operation.Reactions.Reaction.Condition']['meta_info'].parent =_meta_table['Ipsla.Operation.Reactions.Reaction']['meta_info']
_meta_table['Ipsla.Operation.Reactions.Reaction']['meta_info'].parent =_meta_table['Ipsla.Operation.Reactions']['meta_info']
_meta_table['Ipsla.Operation.ReactionTriggers.ReactionTrigger']['meta_info'].parent =_meta_table['Ipsla.Operation.ReactionTriggers']['meta_info']
_meta_table['Ipsla.Operation.Definitions.Definition.OperationType.IcmpEcho.EnhancedStats.EnhancedStat']['meta_info'].parent =_meta_table['Ipsla.Operation.Definitions.Definition.OperationType.IcmpEcho.EnhancedStats']['meta_info']
_meta_table['Ipsla.Operation.Definitions.Definition.OperationType.IcmpEcho.DataSize']['meta_info'].parent =_meta_table['Ipsla.Operation.Definitions.Definition.OperationType.IcmpEcho']['meta_info']
_meta_table['Ipsla.Operation.Definitions.Definition.OperationType.IcmpEcho.Statistics']['meta_info'].parent =_meta_table['Ipsla.Operation.Definitions.Definition.OperationType.IcmpEcho']['meta_info']
_meta_table['Ipsla.Operation.Definitions.Definition.OperationType.IcmpEcho.History']['meta_info'].parent =_meta_table['Ipsla.Operation.Definitions.Definition.OperationType.IcmpEcho']['meta_info']
_meta_table['Ipsla.Operation.Definitions.Definition.OperationType.IcmpEcho.EnhancedStats']['meta_info'].parent =_meta_table['Ipsla.Operation.Definitions.Definition.OperationType.IcmpEcho']['meta_info']
_meta_table['Ipsla.Operation.Definitions.Definition.OperationType.MplsLspPing.Target.Ipv4.FecAddress']['meta_info'].parent =_meta_table['Ipsla.Operation.Definitions.Definition.OperationType.MplsLspPing.Target.Ipv4']['meta_info']
_meta_table['Ipsla.Operation.Definitions.Definition.OperationType.MplsLspPing.Target.Pseudowire.TargetAddress']['meta_info'].parent =_meta_table['Ipsla.Operation.Definitions.Definition.OperationType.MplsLspPing.Target.Pseudowire']['meta_info']
_meta_table['Ipsla.Operation.Definitions.Definition.OperationType.MplsLspPing.Target.TrafficEngineering']['meta_info'].parent =_meta_table['Ipsla.Operation.Definitions.Definition.OperationType.MplsLspPing.Target']['meta_info']
_meta_table['Ipsla.Operation.Definitions.Definition.OperationType.MplsLspPing.Target.Ipv4']['meta_info'].parent =_meta_table['Ipsla.Operation.Definitions.Definition.OperationType.MplsLspPing.Target']['meta_info']
_meta_table['Ipsla.Operation.Definitions.Definition.OperationType.MplsLspPing.Target.Pseudowire']['meta_info'].parent =_meta_table['Ipsla.Operation.Definitions.Definition.OperationType.MplsLspPing.Target']['meta_info']
_meta_table['Ipsla.Operation.Definitions.Definition.OperationType.MplsLspPing.EnhancedStats.EnhancedStat']['meta_info'].parent =_meta_table['Ipsla.Operation.Definitions.Definition.OperationType.MplsLspPing.EnhancedStats']['meta_info']
_meta_table['Ipsla.Operation.Definitions.Definition.OperationType.MplsLspPing.DataSize']['meta_info'].parent =_meta_table['Ipsla.Operation.Definitions.Definition.OperationType.MplsLspPing']['meta_info']
_meta_table['Ipsla.Operation.Definitions.Definition.OperationType.MplsLspPing.Reply']['meta_info'].parent =_meta_table['Ipsla.Operation.Definitions.Definition.OperationType.MplsLspPing']['meta_info']
_meta_table['Ipsla.Operation.Definitions.Definition.OperationType.MplsLspPing.Target']['meta_info'].parent =_meta_table['Ipsla.Operation.Definitions.Definition.OperationType.MplsLspPing']['meta_info']
_meta_table['Ipsla.Operation.Definitions.Definition.OperationType.MplsLspPing.Statistics']['meta_info'].parent =_meta_table['Ipsla.Operation.Definitions.Definition.OperationType.MplsLspPing']['meta_info']
_meta_table['Ipsla.Operation.Definitions.Definition.OperationType.MplsLspPing.History']['meta_info'].parent =_meta_table['Ipsla.Operation.Definitions.Definition.OperationType.MplsLspPing']['meta_info']
_meta_table['Ipsla.Operation.Definitions.Definition.OperationType.MplsLspPing.EnhancedStats']['meta_info'].parent =_meta_table['Ipsla.Operation.Definitions.Definition.OperationType.MplsLspPing']['meta_info']
_meta_table['Ipsla.Operation.Definitions.Definition.OperationType.UdpEcho.EnhancedStats.EnhancedStat']['meta_info'].parent =_meta_table['Ipsla.Operation.Definitions.Definition.OperationType.UdpEcho.EnhancedStats']['meta_info']
_meta_table['Ipsla.Operation.Definitions.Definition.OperationType.UdpEcho.DataSize']['meta_info'].parent =_meta_table['Ipsla.Operation.Definitions.Definition.OperationType.UdpEcho']['meta_info']
_meta_table['Ipsla.Operation.Definitions.Definition.OperationType.UdpEcho.Statistics']['meta_info'].parent =_meta_table['Ipsla.Operation.Definitions.Definition.OperationType.UdpEcho']['meta_info']
_meta_table['Ipsla.Operation.Definitions.Definition.OperationType.UdpEcho.History']['meta_info'].parent =_meta_table['Ipsla.Operation.Definitions.Definition.OperationType.UdpEcho']['meta_info']
_meta_table['Ipsla.Operation.Definitions.Definition.OperationType.UdpEcho.EnhancedStats']['meta_info'].parent =_meta_table['Ipsla.Operation.Definitions.Definition.OperationType.UdpEcho']['meta_info']
_meta_table['Ipsla.Operation.Definitions.Definition.OperationType.MplsLspTrace.Target.Ipv4.FecAddress']['meta_info'].parent =_meta_table['Ipsla.Operation.Definitions.Definition.OperationType.MplsLspTrace.Target.Ipv4']['meta_info']
_meta_table['Ipsla.Operation.Definitions.Definition.OperationType.MplsLspTrace.Target.TrafficEngineering']['meta_info'].parent =_meta_table['Ipsla.Operation.Definitions.Definition.OperationType.MplsLspTrace.Target']['meta_info']
_meta_table['Ipsla.Operation.Definitions.Definition.OperationType.MplsLspTrace.Target.Ipv4']['meta_info'].parent =_meta_table['Ipsla.Operation.Definitions.Definition.OperationType.MplsLspTrace.Target']['meta_info']
_meta_table['Ipsla.Operation.Definitions.Definition.OperationType.MplsLspTrace.Target']['meta_info'].parent =_meta_table['Ipsla.Operation.Definitions.Definition.OperationType.MplsLspTrace']['meta_info']
_meta_table['Ipsla.Operation.Definitions.Definition.OperationType.MplsLspTrace.Reply']['meta_info'].parent =_meta_table['Ipsla.Operation.Definitions.Definition.OperationType.MplsLspTrace']['meta_info']
_meta_table['Ipsla.Operation.Definitions.Definition.OperationType.MplsLspTrace.Statistics']['meta_info'].parent =_meta_table['Ipsla.Operation.Definitions.Definition.OperationType.MplsLspTrace']['meta_info']
_meta_table['Ipsla.Operation.Definitions.Definition.OperationType.MplsLspTrace.History']['meta_info'].parent =_meta_table['Ipsla.Operation.Definitions.Definition.OperationType.MplsLspTrace']['meta_info']
_meta_table['Ipsla.Operation.Definitions.Definition.OperationType.UdpJitter.EnhancedStats.EnhancedStat']['meta_info'].parent =_meta_table['Ipsla.Operation.Definitions.Definition.OperationType.UdpJitter.EnhancedStats']['meta_info']
_meta_table['Ipsla.Operation.Definitions.Definition.OperationType.UdpJitter.DataSize']['meta_info'].parent =_meta_table['Ipsla.Operation.Definitions.Definition.OperationType.UdpJitter']['meta_info']
_meta_table['Ipsla.Operation.Definitions.Definition.OperationType.UdpJitter.Packet']['meta_info'].parent =_meta_table['Ipsla.Operation.Definitions.Definition.OperationType.UdpJitter']['meta_info']
_meta_table['Ipsla.Operation.Definitions.Definition.OperationType.UdpJitter.Statistics']['meta_info'].parent =_meta_table['Ipsla.Operation.Definitions.Definition.OperationType.UdpJitter']['meta_info']
_meta_table['Ipsla.Operation.Definitions.Definition.OperationType.UdpJitter.EnhancedStats']['meta_info'].parent =_meta_table['Ipsla.Operation.Definitions.Definition.OperationType.UdpJitter']['meta_info']
_meta_table['Ipsla.Operation.Definitions.Definition.OperationType.IcmpPathEcho.History']['meta_info'].parent =_meta_table['Ipsla.Operation.Definitions.Definition.OperationType.IcmpPathEcho']['meta_info']
_meta_table['Ipsla.Operation.Definitions.Definition.OperationType.IcmpPathEcho.DataSize']['meta_info'].parent =_meta_table['Ipsla.Operation.Definitions.Definition.OperationType.IcmpPathEcho']['meta_info']
_meta_table['Ipsla.Operation.Definitions.Definition.OperationType.IcmpPathEcho.Statistics']['meta_info'].parent =_meta_table['Ipsla.Operation.Definitions.Definition.OperationType.IcmpPathEcho']['meta_info']
_meta_table['Ipsla.Operation.Definitions.Definition.OperationType.IcmpPathEcho.LsrPath']['meta_info'].parent =_meta_table['Ipsla.Operation.Definitions.Definition.OperationType.IcmpPathEcho']['meta_info']
_meta_table['Ipsla.Operation.Definitions.Definition.OperationType.IcmpPathJitter.DataSize']['meta_info'].parent =_meta_table['Ipsla.Operation.Definitions.Definition.OperationType.IcmpPathJitter']['meta_info']
_meta_table['Ipsla.Operation.Definitions.Definition.OperationType.IcmpPathJitter.Packet']['meta_info'].parent =_meta_table['Ipsla.Operation.Definitions.Definition.OperationType.IcmpPathJitter']['meta_info']
_meta_table['Ipsla.Operation.Definitions.Definition.OperationType.IcmpPathJitter.LsrPath']['meta_info'].parent =_meta_table['Ipsla.Operation.Definitions.Definition.OperationType.IcmpPathJitter']['meta_info']
_meta_table['Ipsla.Operation.Definitions.Definition.OperationType.IcmpEcho']['meta_info'].parent =_meta_table['Ipsla.Operation.Definitions.Definition.OperationType']['meta_info']
_meta_table['Ipsla.Operation.Definitions.Definition.OperationType.MplsLspPing']['meta_info'].parent =_meta_table['Ipsla.Operation.Definitions.Definition.OperationType']['meta_info']
_meta_table['Ipsla.Operation.Definitions.Definition.OperationType.UdpEcho']['meta_info'].parent =_meta_table['Ipsla.Operation.Definitions.Definition.OperationType']['meta_info']
_meta_table['Ipsla.Operation.Definitions.Definition.OperationType.MplsLspTrace']['meta_info'].parent =_meta_table['Ipsla.Operation.Definitions.Definition.OperationType']['meta_info']
_meta_table['Ipsla.Operation.Definitions.Definition.OperationType.UdpJitter']['meta_info'].parent =_meta_table['Ipsla.Operation.Definitions.Definition.OperationType']['meta_info']
_meta_table['Ipsla.Operation.Definitions.Definition.OperationType.IcmpPathEcho']['meta_info'].parent =_meta_table['Ipsla.Operation.Definitions.Definition.OperationType']['meta_info']
_meta_table['Ipsla.Operation.Definitions.Definition.OperationType.IcmpPathJitter']['meta_info'].parent =_meta_table['Ipsla.Operation.Definitions.Definition.OperationType']['meta_info']
_meta_table['Ipsla.Operation.Definitions.Definition.OperationType']['meta_info'].parent =_meta_table['Ipsla.Operation.Definitions.Definition']['meta_info']
_meta_table['Ipsla.Operation.Definitions.Definition']['meta_info'].parent =_meta_table['Ipsla.Operation.Definitions']['meta_info']
_meta_table['Ipsla.Operation.Schedules']['meta_info'].parent =_meta_table['Ipsla.Operation']['meta_info']
_meta_table['Ipsla.Operation.Reactions']['meta_info'].parent =_meta_table['Ipsla.Operation']['meta_info']
_meta_table['Ipsla.Operation.ReactionTriggers']['meta_info'].parent =_meta_table['Ipsla.Operation']['meta_info']
_meta_table['Ipsla.Operation.Definitions']['meta_info'].parent =_meta_table['Ipsla.Operation']['meta_info']
_meta_table['Ipsla.Responder.Type.Udp.Addresses.Address.Ports.Port']['meta_info'].parent =_meta_table['Ipsla.Responder.Type.Udp.Addresses.Address.Ports']['meta_info']
_meta_table['Ipsla.Responder.Type.Udp.Addresses.Address.Ports']['meta_info'].parent =_meta_table['Ipsla.Responder.Type.Udp.Addresses.Address']['meta_info']
_meta_table['Ipsla.Responder.Type.Udp.Addresses.Address']['meta_info'].parent =_meta_table['Ipsla.Responder.Type.Udp.Addresses']['meta_info']
_meta_table['Ipsla.Responder.Type.Udp.Addresses']['meta_info'].parent =_meta_table['Ipsla.Responder.Type.Udp']['meta_info']
_meta_table['Ipsla.Responder.Type.Udp']['meta_info'].parent =_meta_table['Ipsla.Responder.Type']['meta_info']
_meta_table['Ipsla.Responder.TwampLight.SessionIds.SessionId.LocalIp.LocalIpv6Addresses.LocalIpv6Address.LocalPortNumbers.LocalPortNumber.RemoteIp.RemoteIpv4Addresses.RemoteIpv4Address.RemotePortNumbers.RemotePortNumber.VrfNames.VrfName']['meta_info'].parent =_meta_table['Ipsla.Responder.TwampLight.SessionIds.SessionId.LocalIp.LocalIpv6Addresses.LocalIpv6Address.LocalPortNumbers.LocalPortNumber.RemoteIp.RemoteIpv4Addresses.RemoteIpv4Address.RemotePortNumbers.RemotePortNumber.VrfNames']['meta_info']
_meta_table['Ipsla.Responder.TwampLight.SessionIds.SessionId.LocalIp.LocalIpv6Addresses.LocalIpv6Address.LocalPortNumbers.LocalPortNumber.RemoteIp.RemoteIpv4Addresses.RemoteIpv4Address.RemotePortNumbers.RemotePortNumber.VrfNames']['meta_info'].parent =_meta_table['Ipsla.Responder.TwampLight.SessionIds.SessionId.LocalIp.LocalIpv6Addresses.LocalIpv6Address.LocalPortNumbers.LocalPortNumber.RemoteIp.RemoteIpv4Addresses.RemoteIpv4Address.RemotePortNumbers.RemotePortNumber']['meta_info']
_meta_table['Ipsla.Responder.TwampLight.SessionIds.SessionId.LocalIp.LocalIpv6Addresses.LocalIpv6Address.LocalPortNumbers.LocalPortNumber.RemoteIp.RemoteIpv4Addresses.RemoteIpv4Address.RemotePortNumbers.RemotePortNumber']['meta_info'].parent =_meta_table['Ipsla.Responder.TwampLight.SessionIds.SessionId.LocalIp.LocalIpv6Addresses.LocalIpv6Address.LocalPortNumbers.LocalPortNumber.RemoteIp.RemoteIpv4Addresses.RemoteIpv4Address.RemotePortNumbers']['meta_info']
_meta_table['Ipsla.Responder.TwampLight.SessionIds.SessionId.LocalIp.LocalIpv6Addresses.LocalIpv6Address.LocalPortNumbers.LocalPortNumber.RemoteIp.RemoteIpv4Addresses.RemoteIpv4Address.RemotePortNumbers']['meta_info'].parent =_meta_table['Ipsla.Responder.TwampLight.SessionIds.SessionId.LocalIp.LocalIpv6Addresses.LocalIpv6Address.LocalPortNumbers.LocalPortNumber.RemoteIp.RemoteIpv4Addresses.RemoteIpv4Address']['meta_info']
_meta_table['Ipsla.Responder.TwampLight.SessionIds.SessionId.LocalIp.LocalIpv6Addresses.LocalIpv6Address.LocalPortNumbers.LocalPortNumber.RemoteIp.RemoteIpv4Addresses.RemoteIpv4Address']['meta_info'].parent =_meta_table['Ipsla.Responder.TwampLight.SessionIds.SessionId.LocalIp.LocalIpv6Addresses.LocalIpv6Address.LocalPortNumbers.LocalPortNumber.RemoteIp.RemoteIpv4Addresses']['meta_info']
_meta_table['Ipsla.Responder.TwampLight.SessionIds.SessionId.LocalIp.LocalIpv6Addresses.LocalIpv6Address.LocalPortNumbers.LocalPortNumber.RemoteIp.RemoteIpv6Addresses.RemoteIpv6Address.RemotePortNumbers.RemotePortNumber.VrfNames.VrfName']['meta_info'].parent =_meta_table['Ipsla.Responder.TwampLight.SessionIds.SessionId.LocalIp.LocalIpv6Addresses.LocalIpv6Address.LocalPortNumbers.LocalPortNumber.RemoteIp.RemoteIpv6Addresses.RemoteIpv6Address.RemotePortNumbers.RemotePortNumber.VrfNames']['meta_info']
_meta_table['Ipsla.Responder.TwampLight.SessionIds.SessionId.LocalIp.LocalIpv6Addresses.LocalIpv6Address.LocalPortNumbers.LocalPortNumber.RemoteIp.RemoteIpv6Addresses.RemoteIpv6Address.RemotePortNumbers.RemotePortNumber.VrfNames']['meta_info'].parent =_meta_table['Ipsla.Responder.TwampLight.SessionIds.SessionId.LocalIp.LocalIpv6Addresses.LocalIpv6Address.LocalPortNumbers.LocalPortNumber.RemoteIp.RemoteIpv6Addresses.RemoteIpv6Address.RemotePortNumbers.RemotePortNumber']['meta_info']
_meta_table['Ipsla.Responder.TwampLight.SessionIds.SessionId.LocalIp.LocalIpv6Addresses.LocalIpv6Address.LocalPortNumbers.LocalPortNumber.RemoteIp.RemoteIpv6Addresses.RemoteIpv6Address.RemotePortNumbers.RemotePortNumber']['meta_info'].parent =_meta_table['Ipsla.Responder.TwampLight.SessionIds.SessionId.LocalIp.LocalIpv6Addresses.LocalIpv6Address.LocalPortNumbers.LocalPortNumber.RemoteIp.RemoteIpv6Addresses.RemoteIpv6Address.RemotePortNumbers']['meta_info']
_meta_table['Ipsla.Responder.TwampLight.SessionIds.SessionId.LocalIp.LocalIpv6Addresses.LocalIpv6Address.LocalPortNumbers.LocalPortNumber.RemoteIp.RemoteIpv6Addresses.RemoteIpv6Address.RemotePortNumbers']['meta_info'].parent =_meta_table['Ipsla.Responder.TwampLight.SessionIds.SessionId.LocalIp.LocalIpv6Addresses.LocalIpv6Address.LocalPortNumbers.LocalPortNumber.RemoteIp.RemoteIpv6Addresses.RemoteIpv6Address']['meta_info']
_meta_table['Ipsla.Responder.TwampLight.SessionIds.SessionId.LocalIp.LocalIpv6Addresses.LocalIpv6Address.LocalPortNumbers.LocalPortNumber.RemoteIp.RemoteIpv6Addresses.RemoteIpv6Address']['meta_info'].parent =_meta_table['Ipsla.Responder.TwampLight.SessionIds.SessionId.LocalIp.LocalIpv6Addresses.LocalIpv6Address.LocalPortNumbers.LocalPortNumber.RemoteIp.RemoteIpv6Addresses']['meta_info']
_meta_table['Ipsla.Responder.TwampLight.SessionIds.SessionId.LocalIp.LocalIpv6Addresses.LocalIpv6Address.LocalPortNumbers.LocalPortNumber.RemoteIp.RemoteIpv4Addresses']['meta_info'].parent =_meta_table['Ipsla.Responder.TwampLight.SessionIds.SessionId.LocalIp.LocalIpv6Addresses.LocalIpv6Address.LocalPortNumbers.LocalPortNumber.RemoteIp']['meta_info']
_meta_table['Ipsla.Responder.TwampLight.SessionIds.SessionId.LocalIp.LocalIpv6Addresses.LocalIpv6Address.LocalPortNumbers.LocalPortNumber.RemoteIp.RemoteIpv6Addresses']['meta_info'].parent =_meta_table['Ipsla.Responder.TwampLight.SessionIds.SessionId.LocalIp.LocalIpv6Addresses.LocalIpv6Address.LocalPortNumbers.LocalPortNumber.RemoteIp']['meta_info']
_meta_table['Ipsla.Responder.TwampLight.SessionIds.SessionId.LocalIp.LocalIpv6Addresses.LocalIpv6Address.LocalPortNumbers.LocalPortNumber.RemoteIp']['meta_info'].parent =_meta_table['Ipsla.Responder.TwampLight.SessionIds.SessionId.LocalIp.LocalIpv6Addresses.LocalIpv6Address.LocalPortNumbers.LocalPortNumber']['meta_info']
_meta_table['Ipsla.Responder.TwampLight.SessionIds.SessionId.LocalIp.LocalIpv6Addresses.LocalIpv6Address.LocalPortNumbers.LocalPortNumber']['meta_info'].parent =_meta_table['Ipsla.Responder.TwampLight.SessionIds.SessionId.LocalIp.LocalIpv6Addresses.LocalIpv6Address.LocalPortNumbers']['meta_info']
_meta_table['Ipsla.Responder.TwampLight.SessionIds.SessionId.LocalIp.LocalIpv6Addresses.LocalIpv6Address.LocalPortNumbers']['meta_info'].parent =_meta_table['Ipsla.Responder.TwampLight.SessionIds.SessionId.LocalIp.LocalIpv6Addresses.LocalIpv6Address']['meta_info']
_meta_table['Ipsla.Responder.TwampLight.SessionIds.SessionId.LocalIp.LocalIpv6Addresses.LocalIpv6Address']['meta_info'].parent =_meta_table['Ipsla.Responder.TwampLight.SessionIds.SessionId.LocalIp.LocalIpv6Addresses']['meta_info']
_meta_table['Ipsla.Responder.TwampLight.SessionIds.SessionId.LocalIp.LocalIpv4Addresses.LocalIpv4Address.LocalPortNumbers.LocalPortNumber.RemoteIp.RemoteIpv4Addresses.RemoteIpv4Address.RemotePortNumbers.RemotePortNumber.VrfNames.VrfName']['meta_info'].parent =_meta_table['Ipsla.Responder.TwampLight.SessionIds.SessionId.LocalIp.LocalIpv4Addresses.LocalIpv4Address.LocalPortNumbers.LocalPortNumber.RemoteIp.RemoteIpv4Addresses.RemoteIpv4Address.RemotePortNumbers.RemotePortNumber.VrfNames']['meta_info']
_meta_table['Ipsla.Responder.TwampLight.SessionIds.SessionId.LocalIp.LocalIpv4Addresses.LocalIpv4Address.LocalPortNumbers.LocalPortNumber.RemoteIp.RemoteIpv4Addresses.RemoteIpv4Address.RemotePortNumbers.RemotePortNumber.VrfNames']['meta_info'].parent =_meta_table['Ipsla.Responder.TwampLight.SessionIds.SessionId.LocalIp.LocalIpv4Addresses.LocalIpv4Address.LocalPortNumbers.LocalPortNumber.RemoteIp.RemoteIpv4Addresses.RemoteIpv4Address.RemotePortNumbers.RemotePortNumber']['meta_info']
_meta_table['Ipsla.Responder.TwampLight.SessionIds.SessionId.LocalIp.LocalIpv4Addresses.LocalIpv4Address.LocalPortNumbers.LocalPortNumber.RemoteIp.RemoteIpv4Addresses.RemoteIpv4Address.RemotePortNumbers.RemotePortNumber']['meta_info'].parent =_meta_table['Ipsla.Responder.TwampLight.SessionIds.SessionId.LocalIp.LocalIpv4Addresses.LocalIpv4Address.LocalPortNumbers.LocalPortNumber.RemoteIp.RemoteIpv4Addresses.RemoteIpv4Address.RemotePortNumbers']['meta_info']
_meta_table['Ipsla.Responder.TwampLight.SessionIds.SessionId.LocalIp.LocalIpv4Addresses.LocalIpv4Address.LocalPortNumbers.LocalPortNumber.RemoteIp.RemoteIpv4Addresses.RemoteIpv4Address.RemotePortNumbers']['meta_info'].parent =_meta_table['Ipsla.Responder.TwampLight.SessionIds.SessionId.LocalIp.LocalIpv4Addresses.LocalIpv4Address.LocalPortNumbers.LocalPortNumber.RemoteIp.RemoteIpv4Addresses.RemoteIpv4Address']['meta_info']
_meta_table['Ipsla.Responder.TwampLight.SessionIds.SessionId.LocalIp.LocalIpv4Addresses.LocalIpv4Address.LocalPortNumbers.LocalPortNumber.RemoteIp.RemoteIpv4Addresses.RemoteIpv4Address']['meta_info'].parent =_meta_table['Ipsla.Responder.TwampLight.SessionIds.SessionId.LocalIp.LocalIpv4Addresses.LocalIpv4Address.LocalPortNumbers.LocalPortNumber.RemoteIp.RemoteIpv4Addresses']['meta_info']
_meta_table['Ipsla.Responder.TwampLight.SessionIds.SessionId.LocalIp.LocalIpv4Addresses.LocalIpv4Address.LocalPortNumbers.LocalPortNumber.RemoteIp.RemoteIpv6Addresses.RemoteIpv6Address.RemotePortNumbers.RemotePortNumber.VrfNames.VrfName']['meta_info'].parent =_meta_table['Ipsla.Responder.TwampLight.SessionIds.SessionId.LocalIp.LocalIpv4Addresses.LocalIpv4Address.LocalPortNumbers.LocalPortNumber.RemoteIp.RemoteIpv6Addresses.RemoteIpv6Address.RemotePortNumbers.RemotePortNumber.VrfNames']['meta_info']
_meta_table['Ipsla.Responder.TwampLight.SessionIds.SessionId.LocalIp.LocalIpv4Addresses.LocalIpv4Address.LocalPortNumbers.LocalPortNumber.RemoteIp.RemoteIpv6Addresses.RemoteIpv6Address.RemotePortNumbers.RemotePortNumber.VrfNames']['meta_info'].parent =_meta_table['Ipsla.Responder.TwampLight.SessionIds.SessionId.LocalIp.LocalIpv4Addresses.LocalIpv4Address.LocalPortNumbers.LocalPortNumber.RemoteIp.RemoteIpv6Addresses.RemoteIpv6Address.RemotePortNumbers.RemotePortNumber']['meta_info']
_meta_table['Ipsla.Responder.TwampLight.SessionIds.SessionId.LocalIp.LocalIpv4Addresses.LocalIpv4Address.LocalPortNumbers.LocalPortNumber.RemoteIp.RemoteIpv6Addresses.RemoteIpv6Address.RemotePortNumbers.RemotePortNumber']['meta_info'].parent =_meta_table['Ipsla.Responder.TwampLight.SessionIds.SessionId.LocalIp.LocalIpv4Addresses.LocalIpv4Address.LocalPortNumbers.LocalPortNumber.RemoteIp.RemoteIpv6Addresses.RemoteIpv6Address.RemotePortNumbers']['meta_info']
_meta_table['Ipsla.Responder.TwampLight.SessionIds.SessionId.LocalIp.LocalIpv4Addresses.LocalIpv4Address.LocalPortNumbers.LocalPortNumber.RemoteIp.RemoteIpv6Addresses.RemoteIpv6Address.RemotePortNumbers']['meta_info'].parent =_meta_table['Ipsla.Responder.TwampLight.SessionIds.SessionId.LocalIp.LocalIpv4Addresses.LocalIpv4Address.LocalPortNumbers.LocalPortNumber.RemoteIp.RemoteIpv6Addresses.RemoteIpv6Address']['meta_info']
_meta_table['Ipsla.Responder.TwampLight.SessionIds.SessionId.LocalIp.LocalIpv4Addresses.LocalIpv4Address.LocalPortNumbers.LocalPortNumber.RemoteIp.RemoteIpv6Addresses.RemoteIpv6Address']['meta_info'].parent =_meta_table['Ipsla.Responder.TwampLight.SessionIds.SessionId.LocalIp.LocalIpv4Addresses.LocalIpv4Address.LocalPortNumbers.LocalPortNumber.RemoteIp.RemoteIpv6Addresses']['meta_info']
_meta_table['Ipsla.Responder.TwampLight.SessionIds.SessionId.LocalIp.LocalIpv4Addresses.LocalIpv4Address.LocalPortNumbers.LocalPortNumber.RemoteIp.RemoteIpv4Addresses']['meta_info'].parent =_meta_table['Ipsla.Responder.TwampLight.SessionIds.SessionId.LocalIp.LocalIpv4Addresses.LocalIpv4Address.LocalPortNumbers.LocalPortNumber.RemoteIp']['meta_info']
_meta_table['Ipsla.Responder.TwampLight.SessionIds.SessionId.LocalIp.LocalIpv4Addresses.LocalIpv4Address.LocalPortNumbers.LocalPortNumber.RemoteIp.RemoteIpv6Addresses']['meta_info'].parent =_meta_table['Ipsla.Responder.TwampLight.SessionIds.SessionId.LocalIp.LocalIpv4Addresses.LocalIpv4Address.LocalPortNumbers.LocalPortNumber.RemoteIp']['meta_info']
_meta_table['Ipsla.Responder.TwampLight.SessionIds.SessionId.LocalIp.LocalIpv4Addresses.LocalIpv4Address.LocalPortNumbers.LocalPortNumber.RemoteIp']['meta_info'].parent =_meta_table['Ipsla.Responder.TwampLight.SessionIds.SessionId.LocalIp.LocalIpv4Addresses.LocalIpv4Address.LocalPortNumbers.LocalPortNumber']['meta_info']
_meta_table['Ipsla.Responder.TwampLight.SessionIds.SessionId.LocalIp.LocalIpv4Addresses.LocalIpv4Address.LocalPortNumbers.LocalPortNumber']['meta_info'].parent =_meta_table['Ipsla.Responder.TwampLight.SessionIds.SessionId.LocalIp.LocalIpv4Addresses.LocalIpv4Address.LocalPortNumbers']['meta_info']
_meta_table['Ipsla.Responder.TwampLight.SessionIds.SessionId.LocalIp.LocalIpv4Addresses.LocalIpv4Address.LocalPortNumbers']['meta_info'].parent =_meta_table['Ipsla.Responder.TwampLight.SessionIds.SessionId.LocalIp.LocalIpv4Addresses.LocalIpv4Address']['meta_info']
_meta_table['Ipsla.Responder.TwampLight.SessionIds.SessionId.LocalIp.LocalIpv4Addresses.LocalIpv4Address']['meta_info'].parent =_meta_table['Ipsla.Responder.TwampLight.SessionIds.SessionId.LocalIp.LocalIpv4Addresses']['meta_info']
_meta_table['Ipsla.Responder.TwampLight.SessionIds.SessionId.LocalIp.LocalIpv6Addresses']['meta_info'].parent =_meta_table['Ipsla.Responder.TwampLight.SessionIds.SessionId.LocalIp']['meta_info']
_meta_table['Ipsla.Responder.TwampLight.SessionIds.SessionId.LocalIp.LocalIpv4Addresses']['meta_info'].parent =_meta_table['Ipsla.Responder.TwampLight.SessionIds.SessionId.LocalIp']['meta_info']
_meta_table['Ipsla.Responder.TwampLight.SessionIds.SessionId.LocalIp']['meta_info'].parent =_meta_table['Ipsla.Responder.TwampLight.SessionIds.SessionId']['meta_info']
_meta_table['Ipsla.Responder.TwampLight.SessionIds.SessionId']['meta_info'].parent =_meta_table['Ipsla.Responder.TwampLight.SessionIds']['meta_info']
_meta_table['Ipsla.Responder.TwampLight.SessionIds']['meta_info'].parent =_meta_table['Ipsla.Responder.TwampLight']['meta_info']
_meta_table['Ipsla.Responder.Twamp']['meta_info'].parent =_meta_table['Ipsla.Responder']['meta_info']
_meta_table['Ipsla.Responder.Type']['meta_info'].parent =_meta_table['Ipsla.Responder']['meta_info']
_meta_table['Ipsla.Responder.TwampLight']['meta_info'].parent =_meta_table['Ipsla.Responder']['meta_info']
_meta_table['Ipsla.MplsDiscovery.Vpn']['meta_info'].parent =_meta_table['Ipsla.MplsDiscovery']['meta_info']
_meta_table['Ipsla.Common']['meta_info'].parent =_meta_table['Ipsla']['meta_info']
_meta_table['Ipsla.MplsLspMonitor']['meta_info'].parent =_meta_table['Ipsla']['meta_info']
_meta_table['Ipsla.Operation']['meta_info'].parent =_meta_table['Ipsla']['meta_info']
_meta_table['Ipsla.Responder']['meta_info'].parent =_meta_table['Ipsla']['meta_info']
_meta_table['Ipsla.MplsDiscovery']['meta_info'].parent =_meta_table['Ipsla']['meta_info']
_meta_table['Ipsla.ServerTwamp']['meta_info'].parent =_meta_table['Ipsla']['meta_info']
