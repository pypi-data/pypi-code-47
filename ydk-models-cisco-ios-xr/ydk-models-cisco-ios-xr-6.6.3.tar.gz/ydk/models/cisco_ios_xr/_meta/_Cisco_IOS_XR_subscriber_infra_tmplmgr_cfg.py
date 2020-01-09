
'''
This is auto-generated file,
which includes metadata for module Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg
'''

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_LIST, REFERENCE_LEAFLIST, REFERENCE_BITS, REFERENCE_UNION
from ydk._core._dm_meta_info import REFERENCE_CLASS, REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, ANYXML_CLASS
from ydk._core._importer import _yang_ns

_meta_table = {
    'DynamicTemplate.Ppps.Ppp.Ipv4Network' : {
        'meta_info' : _MetaInfoClass('DynamicTemplate.Ppps.Ppp.Ipv4Network', REFERENCE_CLASS,
            '''Interface IPv4 Network configuration data''',
            False, 
            [
            _MetaInfoClassMember('unnumbered', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                Enable IP processing without an explicit
                address
                ''',
                'unnumbered',
                'Cisco-IOS-XR-ipv4-ma-subscriber-cfg', False),
            _MetaInfoClassMember('mtu', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('68', '65535')], [],
                '''                The IP Maximum Transmission Unit
                ''',
                'mtu',
                'Cisco-IOS-XR-ipv4-ma-subscriber-cfg', False),
            _MetaInfoClassMember('unreachables', ATTRIBUTE, 'bool', 'boolean',
                None, None,
                [], [],
                '''                TRUE if enabled, FALSE if disabled
                ''',
                'unreachables',
                'Cisco-IOS-XR-ipv4-ma-subscriber-cfg', False, default_value='False'),
            _MetaInfoClassMember('rpf', ATTRIBUTE, 'bool', 'boolean',
                None, None,
                [], [],
                '''                TRUE if enabled, FALSE if disabled
                ''',
                'rpf',
                'Cisco-IOS-XR-ipv4-ma-subscriber-cfg', False, default_value='True'),
            ],
            'Cisco-IOS-XR-ipv4-ma-subscriber-cfg',
            'ipv4-network',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-ipv4-ma-subscriber-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg',
        ),
    },
    'DynamicTemplate.Ppps.Ppp.Accounting.IdleTimeout' : {
        'meta_info' : _MetaInfoClass('DynamicTemplate.Ppps.Ppp.Accounting.IdleTimeout', REFERENCE_CLASS,
            '''Subscriber accounting idle timeout''',
            False, 
            [
            _MetaInfoClassMember('timeout-value', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('60', '4320000')], [],
                '''                Idle timeout value in seconds
                ''',
                'timeout_value',
                'Cisco-IOS-XR-subscriber-accounting-cfg', False),
            _MetaInfoClassMember('threshold', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('1', '10000')], [],
                '''                Threshold in minute(s) per packet
                ''',
                'threshold',
                'Cisco-IOS-XR-subscriber-accounting-cfg', False),
            _MetaInfoClassMember('direction', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                Idle timeout traffic direction
                ''',
                'direction',
                'Cisco-IOS-XR-subscriber-accounting-cfg', False),
            ],
            'Cisco-IOS-XR-subscriber-accounting-cfg',
            'idle-timeout',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-subscriber-accounting-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg',
        ),
    },
    'DynamicTemplate.Ppps.Ppp.Accounting.Session.HoldAcctStart' : _MetaInfoEnum('HoldAcctStart',
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg', 'DynamicTemplate.Ppps.Ppp.Accounting.Session.HoldAcctStart',
        '''Hold Accounting start based on IA_PD''',
        {
            'ipv6-prefix-delegation':'ipv6_prefix_delegation',
        }, 'Cisco-IOS-XR-subscriber-accounting-cfg', _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-subscriber-accounting-cfg']),
    'DynamicTemplate.Ppps.Ppp.Accounting.Session' : {
        'meta_info' : _MetaInfoClass('DynamicTemplate.Ppps.Ppp.Accounting.Session', REFERENCE_CLASS,
            '''Subscriber accounting session accounting''',
            False, 
            [
            _MetaInfoClassMember('method-list-name', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                Session accounting method list name
                ''',
                'method_list_name',
                'Cisco-IOS-XR-subscriber-accounting-cfg', False),
            _MetaInfoClassMember('periodic-interval', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('0', '4294967295')], [],
                '''                Interim accounting interval in minutes
                ''',
                'periodic_interval',
                'Cisco-IOS-XR-subscriber-accounting-cfg', False),
            _MetaInfoClassMember('dual-stack-delay', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('0', '4294967295')], [],
                '''                Dual stack wait delay in seconds
                ''',
                'dual_stack_delay',
                'Cisco-IOS-XR-subscriber-accounting-cfg', False),
            _MetaInfoClassMember('hold-acct-start', REFERENCE_ENUM_CLASS, 'HoldAcctStart', 'enumeration',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg', 'DynamicTemplate.Ppps.Ppp.Accounting.Session.HoldAcctStart',
                [], [],
                '''                Hold Accounting start based on IA_PD
                ''',
                'hold_acct_start',
                'Cisco-IOS-XR-subscriber-accounting-cfg', False),
            ],
            'Cisco-IOS-XR-subscriber-accounting-cfg',
            'session',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-subscriber-accounting-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg',
        ),
    },
    'DynamicTemplate.Ppps.Ppp.Accounting.ServiceAccounting' : {
        'meta_info' : _MetaInfoClass('DynamicTemplate.Ppps.Ppp.Accounting.ServiceAccounting', REFERENCE_CLASS,
            '''Subscriber accounting service accounting''',
            False, 
            [
            _MetaInfoClassMember('method-list-name', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                Service accounting method list name
                ''',
                'method_list_name',
                'Cisco-IOS-XR-subscriber-accounting-cfg', False),
            _MetaInfoClassMember('accounting-interim-interval', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('0', '4294967295')], [],
                '''                Accounting interim interval in minutes
                ''',
                'accounting_interim_interval',
                'Cisco-IOS-XR-subscriber-accounting-cfg', False),
            ],
            'Cisco-IOS-XR-subscriber-accounting-cfg',
            'service-accounting',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-subscriber-accounting-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg',
        ),
    },
    'DynamicTemplate.Ppps.Ppp.Accounting' : {
        'meta_info' : _MetaInfoClass('DynamicTemplate.Ppps.Ppp.Accounting', REFERENCE_CLASS,
            '''Subscriber accounting dynamic-template commands''',
            False, 
            [
            _MetaInfoClassMember('idle-timeout', REFERENCE_CLASS, 'IdleTimeout', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg', 'DynamicTemplate.Ppps.Ppp.Accounting.IdleTimeout',
                [], [],
                '''                Subscriber accounting idle timeout
                ''',
                'idle_timeout',
                'Cisco-IOS-XR-subscriber-accounting-cfg', False),
            _MetaInfoClassMember('session', REFERENCE_CLASS, 'Session', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg', 'DynamicTemplate.Ppps.Ppp.Accounting.Session',
                [], [],
                '''                Subscriber accounting session accounting
                ''',
                'session',
                'Cisco-IOS-XR-subscriber-accounting-cfg', False),
            _MetaInfoClassMember('service-accounting', REFERENCE_CLASS, 'ServiceAccounting', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg', 'DynamicTemplate.Ppps.Ppp.Accounting.ServiceAccounting',
                [], [],
                '''                Subscriber accounting service accounting
                ''',
                'service_accounting',
                'Cisco-IOS-XR-subscriber-accounting-cfg', False),
            _MetaInfoClassMember('monitor-feature', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                Subscriber monitor feature
                ''',
                'monitor_feature',
                'Cisco-IOS-XR-subscriber-accounting-cfg', False),
            _MetaInfoClassMember('prepaid-feature', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                Subscriber accounting prepaid feature
                ''',
                'prepaid_feature',
                'Cisco-IOS-XR-subscriber-accounting-cfg', False),
            ],
            'Cisco-IOS-XR-subscriber-accounting-cfg',
            'accounting',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-subscriber-accounting-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg',
        ),
    },
    'DynamicTemplate.Ppps.Ppp.Qos.ServicePolicy.Input' : {
        'meta_info' : _MetaInfoClass('DynamicTemplate.Ppps.Ppp.Qos.ServicePolicy.Input', REFERENCE_CLASS,
            '''Subscriber ingress policy''',
            False, 
            [
            _MetaInfoClassMember('policy-name', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                Name of policy-map
                ''',
                'policy_name',
                'Cisco-IOS-XR-qos-ma-bng-cfg', False, is_mandatory=True),
            _MetaInfoClassMember('spi-name', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                Name of the SPI
                ''',
                'spi_name',
                'Cisco-IOS-XR-qos-ma-bng-cfg', False),
            _MetaInfoClassMember('merge', ATTRIBUTE, 'bool', 'boolean',
                None, None,
                [], [],
                '''                TRUE for merge enabled for service-policy
                applied on dynamic template.
                ''',
                'merge',
                'Cisco-IOS-XR-qos-ma-bng-cfg', False),
            _MetaInfoClassMember('merge-id', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('0', '255')], [],
                '''                Merge ID value
                ''',
                'merge_id',
                'Cisco-IOS-XR-qos-ma-bng-cfg', False),
            _MetaInfoClassMember('account-stats', ATTRIBUTE, 'bool', 'boolean',
                None, None,
                [], [],
                '''                TRUE for account stats enabled for
                service-policy applied on dynamic template.
                Note: account stats not supported for
                subscriber type 'ppp' and 'ipsubscriber'.
                ''',
                'account_stats',
                'Cisco-IOS-XR-qos-ma-bng-cfg', False),
            ],
            'Cisco-IOS-XR-qos-ma-bng-cfg',
            'input',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-qos-ma-bng-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg',
            is_presence=True,
        ),
    },
    'DynamicTemplate.Ppps.Ppp.Qos.ServicePolicy.Output' : {
        'meta_info' : _MetaInfoClass('DynamicTemplate.Ppps.Ppp.Qos.ServicePolicy.Output', REFERENCE_CLASS,
            '''Subscriber egress policy''',
            False, 
            [
            _MetaInfoClassMember('policy-name', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                Name of policy-map
                ''',
                'policy_name',
                'Cisco-IOS-XR-qos-ma-bng-cfg', False, is_mandatory=True),
            _MetaInfoClassMember('spi-name', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                Name of the SPI
                ''',
                'spi_name',
                'Cisco-IOS-XR-qos-ma-bng-cfg', False),
            _MetaInfoClassMember('merge', ATTRIBUTE, 'bool', 'boolean',
                None, None,
                [], [],
                '''                TRUE for merge enabled for service-policy
                applied on dynamic template.
                ''',
                'merge',
                'Cisco-IOS-XR-qos-ma-bng-cfg', False),
            _MetaInfoClassMember('merge-id', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('0', '255')], [],
                '''                Merge ID value
                ''',
                'merge_id',
                'Cisco-IOS-XR-qos-ma-bng-cfg', False),
            _MetaInfoClassMember('account-stats', ATTRIBUTE, 'bool', 'boolean',
                None, None,
                [], [],
                '''                TRUE for account stats enabled for
                service-policy applied on dynamic template.
                Note: account stats not supported for
                subscriber type 'ppp' and 'ipsubscriber'.
                ''',
                'account_stats',
                'Cisco-IOS-XR-qos-ma-bng-cfg', False),
            ],
            'Cisco-IOS-XR-qos-ma-bng-cfg',
            'output',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-qos-ma-bng-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg',
            is_presence=True,
        ),
    },
    'DynamicTemplate.Ppps.Ppp.Qos.ServicePolicy' : {
        'meta_info' : _MetaInfoClass('DynamicTemplate.Ppps.Ppp.Qos.ServicePolicy', REFERENCE_CLASS,
            '''Service policy to be applied in ingress/egress
direction''',
            False, 
            [
            _MetaInfoClassMember('input', REFERENCE_CLASS, 'Input', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg', 'DynamicTemplate.Ppps.Ppp.Qos.ServicePolicy.Input',
                [], [],
                '''                Subscriber ingress policy
                ''',
                'input',
                'Cisco-IOS-XR-qos-ma-bng-cfg', False, is_presence=True),
            _MetaInfoClassMember('output', REFERENCE_CLASS, 'Output', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg', 'DynamicTemplate.Ppps.Ppp.Qos.ServicePolicy.Output',
                [], [],
                '''                Subscriber egress policy
                ''',
                'output',
                'Cisco-IOS-XR-qos-ma-bng-cfg', False, is_presence=True),
            ],
            'Cisco-IOS-XR-qos-ma-bng-cfg',
            'service-policy',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-qos-ma-bng-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg',
        ),
    },
    'DynamicTemplate.Ppps.Ppp.Qos.Account' : {
        'meta_info' : _MetaInfoClass('DynamicTemplate.Ppps.Ppp.Qos.Account', REFERENCE_CLASS,
            '''QoS L2 overhead accounting''',
            False, 
            [
            _MetaInfoClassMember('aal', REFERENCE_ENUM_CLASS, 'Qosl2DataLink', 'Qosl2-data-link',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_qos_ma_bng_cfg', 'Qosl2DataLink',
                [], [],
                '''                ATM adaptation layer AAL
                ''',
                'aal',
                'Cisco-IOS-XR-qos-ma-bng-cfg', False, has_must=True),
            _MetaInfoClassMember('encapsulation', REFERENCE_ENUM_CLASS, 'Qosl2Encap', 'Qosl2-encap',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_qos_ma_bng_cfg', 'Qosl2Encap',
                [], [],
                '''                Specify encapsulation type
                ''',
                'encapsulation',
                'Cisco-IOS-XR-qos-ma-bng-cfg', False, has_must=True),
            _MetaInfoClassMember('atm-cell-tax', ATTRIBUTE, 'Empty', 'empty',
                None, None,
                [], [],
                '''                ATM cell tax to L2 overhead
                ''',
                'atm_cell_tax',
                'Cisco-IOS-XR-qos-ma-bng-cfg', False, has_must=True),
            _MetaInfoClassMember('user-defined', ATTRIBUTE, 'int', 'int32',
                None, None,
                [('-63', '63')], [],
                '''                Numeric L2 overhead offset
                ''',
                'user_defined',
                'Cisco-IOS-XR-qos-ma-bng-cfg', False, has_must=True),
            ],
            'Cisco-IOS-XR-qos-ma-bng-cfg',
            'account',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-qos-ma-bng-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg',
        ),
    },
    'DynamicTemplate.Ppps.Ppp.Qos.Output' : {
        'meta_info' : _MetaInfoClass('DynamicTemplate.Ppps.Ppp.Qos.Output', REFERENCE_CLASS,
            '''QoS to be applied in egress direction''',
            False, 
            [
            _MetaInfoClassMember('minimum-bandwidth', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('1', '4294967295')], [],
                '''                Minimum bandwidth value for the subscriber (in
                kbps)
                ''',
                'minimum_bandwidth',
                'Cisco-IOS-XR-qos-ma-bng-cfg', False),
            ],
            'Cisco-IOS-XR-qos-ma-bng-cfg',
            'output',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-qos-ma-bng-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg',
        ),
    },
    'DynamicTemplate.Ppps.Ppp.Qos' : {
        'meta_info' : _MetaInfoClass('DynamicTemplate.Ppps.Ppp.Qos', REFERENCE_CLASS,
            '''QoS dynamically applied configuration template''',
            False, 
            [
            _MetaInfoClassMember('service-policy', REFERENCE_CLASS, 'ServicePolicy', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg', 'DynamicTemplate.Ppps.Ppp.Qos.ServicePolicy',
                [], [],
                '''                Service policy to be applied in ingress/egress
                direction
                ''',
                'service_policy',
                'Cisco-IOS-XR-qos-ma-bng-cfg', False),
            _MetaInfoClassMember('account', REFERENCE_CLASS, 'Account', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg', 'DynamicTemplate.Ppps.Ppp.Qos.Account',
                [], [],
                '''                QoS L2 overhead accounting
                ''',
                'account',
                'Cisco-IOS-XR-qos-ma-bng-cfg', False),
            _MetaInfoClassMember('output', REFERENCE_CLASS, 'Output', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg', 'DynamicTemplate.Ppps.Ppp.Qos.Output',
                [], [],
                '''                QoS to be applied in egress direction
                ''',
                'output',
                'Cisco-IOS-XR-qos-ma-bng-cfg', False),
            ],
            'Cisco-IOS-XR-qos-ma-bng-cfg',
            'qos',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-qos-ma-bng-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg',
        ),
    },
    'DynamicTemplate.Ppps.Ppp.Igmp.DefaultVrf.ExplicitTracking' : {
        'meta_info' : _MetaInfoClass('DynamicTemplate.Ppps.Ppp.Igmp.DefaultVrf.ExplicitTracking', REFERENCE_CLASS,
            '''IGMPv3 explicit host tracking''',
            False, 
            [
            _MetaInfoClassMember('enable', ATTRIBUTE, 'bool', 'boolean',
                None, None,
                [], [],
                '''                Enable or disable, when value is TRUE or
                FALSE respectively
                ''',
                'enable',
                'Cisco-IOS-XR-ipv4-igmp-dyn-tmpl-cfg', False, is_mandatory=True),
            _MetaInfoClassMember('access-list-name', ATTRIBUTE, 'str', 'xr:Cisco-ios-xr-string',
                None, None,
                [(1, 64)], [],
                '''                Access list specifying tracking group range
                ''',
                'access_list_name',
                'Cisco-IOS-XR-ipv4-igmp-dyn-tmpl-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-igmp-dyn-tmpl-cfg',
            'explicit-tracking',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-ipv4-igmp-dyn-tmpl-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg',
            is_presence=True,
        ),
    },
    'DynamicTemplate.Ppps.Ppp.Igmp.DefaultVrf' : {
        'meta_info' : _MetaInfoClass('DynamicTemplate.Ppps.Ppp.Igmp.DefaultVrf', REFERENCE_CLASS,
            '''Default VRF''',
            False, 
            [
            _MetaInfoClassMember('explicit-tracking', REFERENCE_CLASS, 'ExplicitTracking', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg', 'DynamicTemplate.Ppps.Ppp.Igmp.DefaultVrf.ExplicitTracking',
                [], [],
                '''                IGMPv3 explicit host tracking
                ''',
                'explicit_tracking',
                'Cisco-IOS-XR-ipv4-igmp-dyn-tmpl-cfg', False, is_presence=True),
            _MetaInfoClassMember('max-groups', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('1', '40000')], [],
                '''                IGMP Max Groups
                ''',
                'max_groups',
                'Cisco-IOS-XR-ipv4-igmp-dyn-tmpl-cfg', False, default_value="25000"),
            _MetaInfoClassMember('access-group', ATTRIBUTE, 'str', 'xr:Cisco-ios-xr-string',
                None, None,
                [(1, 64)], [],
                '''                Access list specifying access-list group range
                ''',
                'access_group',
                'Cisco-IOS-XR-ipv4-igmp-dyn-tmpl-cfg', False),
            _MetaInfoClassMember('version', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('1', '3')], [],
                '''                IGMP Version
                ''',
                'version',
                'Cisco-IOS-XR-ipv4-igmp-dyn-tmpl-cfg', False, default_value="3"),
            _MetaInfoClassMember('query-interval', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('1', '3600')], [],
                '''                Query interval in seconds
                ''',
                'query_interval',
                'Cisco-IOS-XR-ipv4-igmp-dyn-tmpl-cfg', False, default_value="60"),
            _MetaInfoClassMember('query-max-response-time', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('1', '25')], [],
                '''                Query response value in seconds
                ''',
                'query_max_response_time',
                'Cisco-IOS-XR-ipv4-igmp-dyn-tmpl-cfg', False, default_value="10"),
            _MetaInfoClassMember('multicast-mode', REFERENCE_ENUM_CLASS, 'DynTmplMulticastMode', 'Dyn-tmpl-multicast-mode',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_igmp_dyn_tmpl_cfg', 'DynTmplMulticastMode',
                [], [],
                '''                Configure Multicast mode variable
                ''',
                'multicast_mode',
                'Cisco-IOS-XR-ipv4-igmp-dyn-tmpl-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-igmp-dyn-tmpl-cfg',
            'default-vrf',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-ipv4-igmp-dyn-tmpl-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg',
        ),
    },
    'DynamicTemplate.Ppps.Ppp.Igmp' : {
        'meta_info' : _MetaInfoClass('DynamicTemplate.Ppps.Ppp.Igmp', REFERENCE_CLASS,
            '''IGMPconfiguration''',
            False, 
            [
            _MetaInfoClassMember('default-vrf', REFERENCE_CLASS, 'DefaultVrf', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg', 'DynamicTemplate.Ppps.Ppp.Igmp.DefaultVrf',
                [], [],
                '''                Default VRF
                ''',
                'default_vrf',
                'Cisco-IOS-XR-ipv4-igmp-dyn-tmpl-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-igmp-dyn-tmpl-cfg',
            'igmp',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-ipv4-igmp-dyn-tmpl-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg',
        ),
    },
    'DynamicTemplate.Ppps.Ppp.Ipv6Network.Addresses.AutoConfiguration' : {
        'meta_info' : _MetaInfoClass('DynamicTemplate.Ppps.Ppp.Ipv6Network.Addresses.AutoConfiguration', REFERENCE_CLASS,
            '''Auto IPv6 Interface Configuration''',
            False, 
            [
            _MetaInfoClassMember('enable', ATTRIBUTE, 'Empty', 'empty',
                None, None,
                [], [],
                '''                The flag to enable auto ipv6 interface
                configuration
                ''',
                'enable',
                'Cisco-IOS-XR-ipv6-ma-subscriber-cfg', False),
            ],
            'Cisco-IOS-XR-ipv6-ma-subscriber-cfg',
            'auto-configuration',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-ipv6-ma-subscriber-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg',
        ),
    },
    'DynamicTemplate.Ppps.Ppp.Ipv6Network.Addresses' : {
        'meta_info' : _MetaInfoClass('DynamicTemplate.Ppps.Ppp.Ipv6Network.Addresses', REFERENCE_CLASS,
            '''Set the IPv6 address of an interface''',
            False, 
            [
            _MetaInfoClassMember('auto-configuration', REFERENCE_CLASS, 'AutoConfiguration', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg', 'DynamicTemplate.Ppps.Ppp.Ipv6Network.Addresses.AutoConfiguration',
                [], [],
                '''                Auto IPv6 Interface Configuration
                ''',
                'auto_configuration',
                'Cisco-IOS-XR-ipv6-ma-subscriber-cfg', False),
            ],
            'Cisco-IOS-XR-ipv6-ma-subscriber-cfg',
            'addresses',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-ipv6-ma-subscriber-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg',
        ),
    },
    'DynamicTemplate.Ppps.Ppp.Ipv6Network' : {
        'meta_info' : _MetaInfoClass('DynamicTemplate.Ppps.Ppp.Ipv6Network', REFERENCE_CLASS,
            '''Interface IPv6 Network configuration data''',
            False, 
            [
            _MetaInfoClassMember('addresses', REFERENCE_CLASS, 'Addresses', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg', 'DynamicTemplate.Ppps.Ppp.Ipv6Network.Addresses',
                [], [],
                '''                Set the IPv6 address of an interface
                ''',
                'addresses',
                'Cisco-IOS-XR-ipv6-ma-subscriber-cfg', False),
            _MetaInfoClassMember('mtu', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('1280', '65535')], [],
                '''                MTU Setting of Interface
                ''',
                'mtu',
                'Cisco-IOS-XR-ipv6-ma-subscriber-cfg', False),
            _MetaInfoClassMember('rpf', ATTRIBUTE, 'bool', 'boolean',
                None, None,
                [], [],
                '''                TRUE if enabled, FALSE if disabled
                ''',
                'rpf',
                'Cisco-IOS-XR-ipv6-ma-subscriber-cfg', False),
            _MetaInfoClassMember('unreachables', ATTRIBUTE, 'Empty', 'empty',
                None, None,
                [], [],
                '''                Override Sending of ICMP Unreachable Messages
                ''',
                'unreachables',
                'Cisco-IOS-XR-ipv6-ma-subscriber-cfg', False),
            ],
            'Cisco-IOS-XR-ipv6-ma-subscriber-cfg',
            'ipv6-network',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-ipv6-ma-subscriber-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg',
        ),
    },
    'DynamicTemplate.Ppps.Ppp.PppoeTemplate' : {
        'meta_info' : _MetaInfoClass('DynamicTemplate.Ppps.Ppp.PppoeTemplate', REFERENCE_CLASS,
            '''PPPoE template configuration data''',
            False, 
            [
            _MetaInfoClassMember('port-limit', ATTRIBUTE, 'int', 'xr:Cisco-ios-xr-port-number',
                None, None,
                [('1', '65535')], [],
                '''                Specify the Port limit (attr 62) to apply to
                the subscriber
                ''',
                'port_limit',
                'Cisco-IOS-XR-subscriber-pppoe-ma-gbl-cfg', False, is_mandatory=True),
            ],
            'Cisco-IOS-XR-subscriber-pppoe-ma-gbl-cfg',
            'pppoe-template',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-subscriber-pppoe-ma-gbl-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg',
            is_presence=True,
        ),
    },
    'DynamicTemplate.Ppps.Ppp.SpanMonitorSessions.SpanMonitorSession.Attachment' : {
        'meta_info' : _MetaInfoClass('DynamicTemplate.Ppps.Ppp.SpanMonitorSessions.SpanMonitorSession.Attachment', REFERENCE_CLASS,
            '''Attach the interface to a Monitor Session''',
            False, 
            [
            _MetaInfoClassMember('session-name', ATTRIBUTE, 'str', 'dt1:Span-session-name',
                None, None,
                [(1, 79)], [],
                '''                Session Name
                ''',
                'session_name',
                'Cisco-IOS-XR-Ethernet-SPAN-subscriber-cfg', False, is_mandatory=True),
            _MetaInfoClassMember('direction', REFERENCE_ENUM_CLASS, 'SpanTrafficDirection', 'Span-traffic-direction',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_Ethernet_SPAN_subscriber_cfg', 'SpanTrafficDirection',
                [], [],
                '''                Specify the direction of traffic to replicate
                (optional)
                ''',
                'direction',
                'Cisco-IOS-XR-Ethernet-SPAN-subscriber-cfg', False),
            _MetaInfoClassMember('port-level-enable', ATTRIBUTE, 'Empty', 'empty',
                None, None,
                [], [],
                '''                Enable port level traffic mirroring
                ''',
                'port_level_enable',
                'Cisco-IOS-XR-Ethernet-SPAN-subscriber-cfg', False),
            ],
            'Cisco-IOS-XR-Ethernet-SPAN-subscriber-cfg',
            'attachment',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-Ethernet-SPAN-subscriber-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg',
            is_presence=True,
        ),
    },
    'DynamicTemplate.Ppps.Ppp.SpanMonitorSessions.SpanMonitorSession.Acl' : {
        'meta_info' : _MetaInfoClass('DynamicTemplate.Ppps.Ppp.SpanMonitorSessions.SpanMonitorSession.Acl', REFERENCE_CLASS,
            '''Enable ACL matching for traffic mirroring''',
            False, 
            [
            _MetaInfoClassMember('acl-enable', ATTRIBUTE, 'Empty', 'empty',
                None, None,
                [], [],
                '''                Enable ACL
                ''',
                'acl_enable',
                'Cisco-IOS-XR-Ethernet-SPAN-subscriber-cfg', False, is_mandatory=True),
            _MetaInfoClassMember('acl-name', ATTRIBUTE, 'str', 'dt1:Span-acl-name',
                None, None,
                [(1, 80)], [],
                '''                ACL Name
                ''',
                'acl_name',
                'Cisco-IOS-XR-Ethernet-SPAN-subscriber-cfg', False),
            ],
            'Cisco-IOS-XR-Ethernet-SPAN-subscriber-cfg',
            'acl',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-Ethernet-SPAN-subscriber-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg',
            is_presence=True,
        ),
    },
    'DynamicTemplate.Ppps.Ppp.SpanMonitorSessions.SpanMonitorSession' : {
        'meta_info' : _MetaInfoClass('DynamicTemplate.Ppps.Ppp.SpanMonitorSessions.SpanMonitorSession', REFERENCE_LIST,
            '''Configuration for a particular class of Monitor
Session''',
            False, 
            [
            _MetaInfoClassMember('session-class', REFERENCE_ENUM_CLASS, 'SpanSessionClass', 'dt1:Span-session-class',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_Ethernet_SPAN_datatypes', 'SpanSessionClass',
                [], [],
                '''                Session Class
                ''',
                'session_class',
                'Cisco-IOS-XR-Ethernet-SPAN-subscriber-cfg', True),
            _MetaInfoClassMember('mirror-first', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('1', '10000')], [],
                '''                Mirror a specified number of bytes from start of
                packet
                ''',
                'mirror_first',
                'Cisco-IOS-XR-Ethernet-SPAN-subscriber-cfg', False),
            _MetaInfoClassMember('attachment', REFERENCE_CLASS, 'Attachment', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg', 'DynamicTemplate.Ppps.Ppp.SpanMonitorSessions.SpanMonitorSession.Attachment',
                [], [],
                '''                Attach the interface to a Monitor Session
                ''',
                'attachment',
                'Cisco-IOS-XR-Ethernet-SPAN-subscriber-cfg', False, is_presence=True),
            _MetaInfoClassMember('mirror-interval', REFERENCE_ENUM_CLASS, 'SpanMirrorInterval', 'Span-mirror-interval',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_Ethernet_SPAN_subscriber_cfg', 'SpanMirrorInterval',
                [], [],
                '''                Specify the mirror interval
                ''',
                'mirror_interval',
                'Cisco-IOS-XR-Ethernet-SPAN-subscriber-cfg', False),
            _MetaInfoClassMember('acl', REFERENCE_CLASS, 'Acl', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg', 'DynamicTemplate.Ppps.Ppp.SpanMonitorSessions.SpanMonitorSession.Acl',
                [], [],
                '''                Enable ACL matching for traffic mirroring
                ''',
                'acl',
                'Cisco-IOS-XR-Ethernet-SPAN-subscriber-cfg', False, is_presence=True),
            ],
            'Cisco-IOS-XR-Ethernet-SPAN-subscriber-cfg',
            'span-monitor-session',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-Ethernet-SPAN-subscriber-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg',
        ),
    },
    'DynamicTemplate.Ppps.Ppp.SpanMonitorSessions' : {
        'meta_info' : _MetaInfoClass('DynamicTemplate.Ppps.Ppp.SpanMonitorSessions', REFERENCE_CLASS,
            '''Monitor Session container for this template''',
            False, 
            [
            _MetaInfoClassMember('span-monitor-session', REFERENCE_LIST, 'SpanMonitorSession', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg', 'DynamicTemplate.Ppps.Ppp.SpanMonitorSessions.SpanMonitorSession',
                [], [],
                '''                Configuration for a particular class of Monitor
                Session
                ''',
                'span_monitor_session',
                'Cisco-IOS-XR-Ethernet-SPAN-subscriber-cfg', False),
            ],
            'Cisco-IOS-XR-Ethernet-SPAN-subscriber-cfg',
            'span-monitor-sessions',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-Ethernet-SPAN-subscriber-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg',
        ),
    },
    'DynamicTemplate.Ppps.Ppp.Ipv6Neighbor.RaInterval' : {
        'meta_info' : _MetaInfoClass('DynamicTemplate.Ppps.Ppp.Ipv6Neighbor.RaInterval', REFERENCE_CLASS,
            '''Set IPv6 Router Advertisement (RA) interval in
seconds''',
            False, 
            [
            _MetaInfoClassMember('maximum', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('4', '1800')], [],
                '''                Maximum RA interval in seconds
                ''',
                'maximum',
                'Cisco-IOS-XR-ipv6-nd-subscriber-cfg', False, is_mandatory=True),
            _MetaInfoClassMember('minimum', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('3', '1800')], [],
                '''                Minimum RA interval in seconds. Must be less
                than 0.75 * maximum interval
                ''',
                'minimum',
                'Cisco-IOS-XR-ipv6-nd-subscriber-cfg', False),
            ],
            'Cisco-IOS-XR-ipv6-nd-subscriber-cfg',
            'ra-interval',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-ipv6-nd-subscriber-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg',
            is_presence=True,
        ),
    },
    'DynamicTemplate.Ppps.Ppp.Ipv6Neighbor.FramedPrefix' : {
        'meta_info' : _MetaInfoClass('DynamicTemplate.Ppps.Ppp.Ipv6Neighbor.FramedPrefix', REFERENCE_CLASS,
            '''Set the IPv6 framed ipv6 prefix for a
subscriber interface ''',
            False, 
            [
            _MetaInfoClassMember('prefix-length', ATTRIBUTE, 'int', 'xr:Ipv6-prefix-length',
                None, None,
                [('0', '128')], [],
                '''                IPv6 framed prefix length
                ''',
                'prefix_length',
                'Cisco-IOS-XR-ipv6-nd-subscriber-cfg', False, is_mandatory=True),
            _MetaInfoClassMember('prefix', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                IPV6 framed prefix address
                ''',
                'prefix',
                'Cisco-IOS-XR-ipv6-nd-subscriber-cfg', False, is_mandatory=True),
            ],
            'Cisco-IOS-XR-ipv6-nd-subscriber-cfg',
            'framed-prefix',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-ipv6-nd-subscriber-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg',
            is_presence=True,
        ),
    },
    'DynamicTemplate.Ppps.Ppp.Ipv6Neighbor.DuplicateAddressDetection' : {
        'meta_info' : _MetaInfoClass('DynamicTemplate.Ppps.Ppp.Ipv6Neighbor.DuplicateAddressDetection', REFERENCE_CLASS,
            '''Duplicate Address Detection (DAD)''',
            False, 
            [
            _MetaInfoClassMember('attempts', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('0', '600')], [],
                '''                Set IPv6 duplicate address detection transmits
                ''',
                'attempts',
                'Cisco-IOS-XR-ipv6-nd-subscriber-cfg', False),
            ],
            'Cisco-IOS-XR-ipv6-nd-subscriber-cfg',
            'duplicate-address-detection',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-ipv6-nd-subscriber-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg',
        ),
    },
    'DynamicTemplate.Ppps.Ppp.Ipv6Neighbor.RaInitial' : {
        'meta_info' : _MetaInfoClass('DynamicTemplate.Ppps.Ppp.Ipv6Neighbor.RaInitial', REFERENCE_CLASS,
            '''IPv6 ND RA Initial''',
            False, 
            [
            _MetaInfoClassMember('count', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('0', '32')], [],
                '''                Initial RA count
                ''',
                'count',
                'Cisco-IOS-XR-ipv6-nd-subscriber-cfg', False, is_mandatory=True),
            _MetaInfoClassMember('interval', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('4', '1800')], [],
                '''                Initial RA interval in seconds
                ''',
                'interval',
                'Cisco-IOS-XR-ipv6-nd-subscriber-cfg', False, is_mandatory=True),
            ],
            'Cisco-IOS-XR-ipv6-nd-subscriber-cfg',
            'ra-initial',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-ipv6-nd-subscriber-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg',
            is_presence=True,
        ),
    },
    'DynamicTemplate.Ppps.Ppp.Ipv6Neighbor' : {
        'meta_info' : _MetaInfoClass('DynamicTemplate.Ppps.Ppp.Ipv6Neighbor', REFERENCE_CLASS,
            '''Interface IPv6 Network configuration data''',
            False, 
            [
            _MetaInfoClassMember('ra-interval', REFERENCE_CLASS, 'RaInterval', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg', 'DynamicTemplate.Ppps.Ppp.Ipv6Neighbor.RaInterval',
                [], [],
                '''                Set IPv6 Router Advertisement (RA) interval in
                seconds
                ''',
                'ra_interval',
                'Cisco-IOS-XR-ipv6-nd-subscriber-cfg', False, is_presence=True),
            _MetaInfoClassMember('framed-prefix', REFERENCE_CLASS, 'FramedPrefix', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg', 'DynamicTemplate.Ppps.Ppp.Ipv6Neighbor.FramedPrefix',
                [], [],
                '''                Set the IPv6 framed ipv6 prefix for a
                subscriber interface 
                ''',
                'framed_prefix',
                'Cisco-IOS-XR-ipv6-nd-subscriber-cfg', False, is_presence=True),
            _MetaInfoClassMember('duplicate-address-detection', REFERENCE_CLASS, 'DuplicateAddressDetection', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg', 'DynamicTemplate.Ppps.Ppp.Ipv6Neighbor.DuplicateAddressDetection',
                [], [],
                '''                Duplicate Address Detection (DAD)
                ''',
                'duplicate_address_detection',
                'Cisco-IOS-XR-ipv6-nd-subscriber-cfg', False),
            _MetaInfoClassMember('ra-initial', REFERENCE_CLASS, 'RaInitial', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg', 'DynamicTemplate.Ppps.Ppp.Ipv6Neighbor.RaInitial',
                [], [],
                '''                IPv6 ND RA Initial
                ''',
                'ra_initial',
                'Cisco-IOS-XR-ipv6-nd-subscriber-cfg', False, is_presence=True),
            _MetaInfoClassMember('framed-prefix-pool', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                Set the IPv6 framed ipv6 prefix pool for a
                subscriber interface 
                ''',
                'framed_prefix_pool',
                'Cisco-IOS-XR-ipv6-nd-subscriber-cfg', False),
            _MetaInfoClassMember('managed-config', ATTRIBUTE, 'Empty', 'empty',
                None, None,
                [], [],
                '''                Host to use stateful protocol for address
                configuration
                ''',
                'managed_config',
                'Cisco-IOS-XR-ipv6-nd-subscriber-cfg', False),
            _MetaInfoClassMember('other-config', ATTRIBUTE, 'Empty', 'empty',
                None, None,
                [], [],
                '''                Host to use stateful protocol for non-address
                configuration
                ''',
                'other_config',
                'Cisco-IOS-XR-ipv6-nd-subscriber-cfg', False),
            _MetaInfoClassMember('start-ra-on-ipv6-enable', ATTRIBUTE, 'Empty', 'empty',
                None, None,
                [], [],
                '''                Start RA on ipv6-enable config
                ''',
                'start_ra_on_ipv6_enable',
                'Cisco-IOS-XR-ipv6-nd-subscriber-cfg', False),
            _MetaInfoClassMember('nud-enable', ATTRIBUTE, 'Empty', 'empty',
                None, None,
                [], [],
                '''                NUD enable
                ''',
                'nud_enable',
                'Cisco-IOS-XR-ipv6-nd-subscriber-cfg', False),
            _MetaInfoClassMember('ra-lifetime', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('0', '9000')], [],
                '''                Set IPv6 Router Advertisement (RA) lifetime in
                seconds
                ''',
                'ra_lifetime',
                'Cisco-IOS-XR-ipv6-nd-subscriber-cfg', False),
            _MetaInfoClassMember('router-preference', REFERENCE_ENUM_CLASS, 'Ipv6NdRouterPrefTemplate', 'Ipv6-nd-router-pref-template',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_nd_subscriber_cfg', 'Ipv6NdRouterPrefTemplate',
                [], [],
                '''                RA Router Preference
                ''',
                'router_preference',
                'Cisco-IOS-XR-ipv6-nd-subscriber-cfg', False),
            _MetaInfoClassMember('ra-suppress', ATTRIBUTE, 'Empty', 'empty',
                None, None,
                [], [],
                '''                Enable suppress IPv6 router advertisement
                ''',
                'ra_suppress',
                'Cisco-IOS-XR-ipv6-nd-subscriber-cfg', False),
            _MetaInfoClassMember('ra-unicast', ATTRIBUTE, 'Empty', 'empty',
                None, None,
                [], [],
                '''                Enable RA unicast Flag
                ''',
                'ra_unicast',
                'Cisco-IOS-XR-ipv6-nd-subscriber-cfg', False),
            _MetaInfoClassMember('ra-unspecify-hoplimit', ATTRIBUTE, 'Empty', 'empty',
                None, None,
                [], [],
                '''                Unspecify IPv6 Router Advertisement (RA)
                hop-limit
                ''',
                'ra_unspecify_hoplimit',
                'Cisco-IOS-XR-ipv6-nd-subscriber-cfg', False),
            _MetaInfoClassMember('ra-suppress-mtu', ATTRIBUTE, 'Empty', 'empty',
                None, None,
                [], [],
                '''                RA suppress MTU flag
                ''',
                'ra_suppress_mtu',
                'Cisco-IOS-XR-ipv6-nd-subscriber-cfg', False),
            _MetaInfoClassMember('suppress-cache-learning', ATTRIBUTE, 'Empty', 'empty',
                None, None,
                [], [],
                '''                Suppress cache learning flag
                ''',
                'suppress_cache_learning',
                'Cisco-IOS-XR-ipv6-nd-subscriber-cfg', False),
            _MetaInfoClassMember('reachable-time', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('0', '3600000')], [],
                '''                Set advertised reachability time in
                milliseconds
                ''',
                'reachable_time',
                'Cisco-IOS-XR-ipv6-nd-subscriber-cfg', False),
            _MetaInfoClassMember('ns-interval', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('1000', '4294967295')], [],
                '''                Set advertised NS retransmission interval in
                milliseconds
                ''',
                'ns_interval',
                'Cisco-IOS-XR-ipv6-nd-subscriber-cfg', False),
            ],
            'Cisco-IOS-XR-ipv6-nd-subscriber-cfg',
            'ipv6-neighbor',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-ipv6-nd-subscriber-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg',
        ),
    },
    'DynamicTemplate.Ppps.Ppp.PppTemplate.Fsm' : {
        'meta_info' : _MetaInfoClass('DynamicTemplate.Ppps.Ppp.PppTemplate.Fsm', REFERENCE_CLASS,
            '''PPP FSM global template configuration data''',
            False, 
            [
            _MetaInfoClassMember('max-consecutive-conf-naks', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('2', '10')], [],
                '''                This specifies the maximum number of
                consecutive Conf-Naks
                ''',
                'max_consecutive_conf_naks',
                'Cisco-IOS-XR-ppp-ma-gbl-cfg', False, default_value="5"),
            _MetaInfoClassMember('max-unacknowledged-conf-requests', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('4', '20')], [],
                '''                This specifies the maximum number of
                unacknowledged Conf-Requests
                ''',
                'max_unacknowledged_conf_requests',
                'Cisco-IOS-XR-ppp-ma-gbl-cfg', False, default_value="10"),
            _MetaInfoClassMember('retry-timeout', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('1', '10')], [],
                '''                This specifies the maximum time to wait for a
                response during PPP negotiation
                ''',
                'retry_timeout',
                'Cisco-IOS-XR-ppp-ma-gbl-cfg', False, default_value="3"),
            _MetaInfoClassMember('protocol-reject-timeout', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('1', '60')], [],
                '''                This specifies the maximum time to wait before
                sending Protocol Reject
                ''',
                'protocol_reject_timeout',
                'Cisco-IOS-XR-ppp-ma-gbl-cfg', False, default_value="60"),
            ],
            'Cisco-IOS-XR-ppp-ma-gbl-cfg',
            'fsm',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-ppp-ma-gbl-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg',
        ),
    },
    'DynamicTemplate.Ppps.Ppp.PppTemplate.Lcp.AbsoluteTimeout' : {
        'meta_info' : _MetaInfoClass('DynamicTemplate.Ppps.Ppp.PppTemplate.Lcp.AbsoluteTimeout', REFERENCE_CLASS,
            '''This specifies the session absolute timeout
value''',
            False, 
            [
            _MetaInfoClassMember('minutes', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('0', '35000000')], [],
                '''                Minutes
                ''',
                'minutes',
                'Cisco-IOS-XR-ppp-ma-gbl-cfg', False),
            _MetaInfoClassMember('seconds', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('0', '59')], [],
                '''                Seconds
                ''',
                'seconds',
                'Cisco-IOS-XR-ppp-ma-gbl-cfg', False),
            ],
            'Cisco-IOS-XR-ppp-ma-gbl-cfg',
            'absolute-timeout',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-ppp-ma-gbl-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg',
        ),
    },
    'DynamicTemplate.Ppps.Ppp.PppTemplate.Lcp.Delay' : {
        'meta_info' : _MetaInfoClass('DynamicTemplate.Ppps.Ppp.PppTemplate.Lcp.Delay', REFERENCE_CLASS,
            '''This specifies the time to delay before
starting active LCPnegotiations''',
            False, 
            [
            _MetaInfoClassMember('seconds', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('0', '255')], [],
                '''                Seconds
                ''',
                'seconds',
                'Cisco-IOS-XR-ppp-ma-gbl-cfg', False),
            _MetaInfoClassMember('milliseconds', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('0', '999')], [],
                '''                Milliseconds
                ''',
                'milliseconds',
                'Cisco-IOS-XR-ppp-ma-gbl-cfg', False),
            ],
            'Cisco-IOS-XR-ppp-ma-gbl-cfg',
            'delay',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-ppp-ma-gbl-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg',
        ),
    },
    'DynamicTemplate.Ppps.Ppp.PppTemplate.Lcp.Authentication.Methods' : {
        'meta_info' : _MetaInfoClass('DynamicTemplate.Ppps.Ppp.PppTemplate.Lcp.Authentication.Methods', REFERENCE_CLASS,
            '''This specifies the PPP link authentication
method''',
            False, 
            [
            _MetaInfoClassMember('method', REFERENCE_LEAFLIST, 'PppAuthenticationMethodGbl', 'Ppp-authentication-method-gbl',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ppp_ma_gbl_cfg', 'PppAuthenticationMethodGbl',
                [], [],
                '''                Select between one and three authentication
                methods in order of preference
                ''',
                'method',
                'Cisco-IOS-XR-ppp-ma-gbl-cfg', False, max_elements=3),
            ],
            'Cisco-IOS-XR-ppp-ma-gbl-cfg',
            'methods',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-ppp-ma-gbl-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg',
        ),
    },
    'DynamicTemplate.Ppps.Ppp.PppTemplate.Lcp.Authentication' : {
        'meta_info' : _MetaInfoClass('DynamicTemplate.Ppps.Ppp.PppTemplate.Lcp.Authentication', REFERENCE_CLASS,
            '''PPP authentication parameters''',
            False, 
            [
            _MetaInfoClassMember('methods', REFERENCE_CLASS, 'Methods', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg', 'DynamicTemplate.Ppps.Ppp.PppTemplate.Lcp.Authentication.Methods',
                [], [],
                '''                This specifies the PPP link authentication
                method
                ''',
                'methods',
                'Cisco-IOS-XR-ppp-ma-gbl-cfg', False),
            _MetaInfoClassMember('chap-host-name', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                This specifies the CHAP hostname
                ''',
                'chap_host_name',
                'Cisco-IOS-XR-ppp-ma-gbl-cfg', False),
            _MetaInfoClassMember('pap', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('0', '4294967295')], [],
                '''                <1> for accepting null-passwordduring
                authentication
                ''',
                'pap',
                'Cisco-IOS-XR-ppp-ma-gbl-cfg', False),
            _MetaInfoClassMember('mschap-host-name', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                This specifies the MS-CHAP hostname
                ''',
                'mschap_host_name',
                'Cisco-IOS-XR-ppp-ma-gbl-cfg', False),
            _MetaInfoClassMember('max-authentication-failures', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('0', '10')], [],
                '''                This specifies whether to allow multiple
                authentication failures and, if so, how many
                ''',
                'max_authentication_failures',
                'Cisco-IOS-XR-ppp-ma-gbl-cfg', False),
            _MetaInfoClassMember('timeout', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('3', '30')], [],
                '''                Maximum time to wait for an authentication
                response
                ''',
                'timeout',
                'Cisco-IOS-XR-ppp-ma-gbl-cfg', False, default_value="10"),
            ],
            'Cisco-IOS-XR-ppp-ma-gbl-cfg',
            'authentication',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-ppp-ma-gbl-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg',
        ),
    },
    'DynamicTemplate.Ppps.Ppp.PppTemplate.Lcp.Keepalive' : {
        'meta_info' : _MetaInfoClass('DynamicTemplate.Ppps.Ppp.PppTemplate.Lcp.Keepalive', REFERENCE_CLASS,
            '''This specifies the rate at which EchoReq
packets are sent''',
            False, 
            [
            _MetaInfoClassMember('keepalive-disable', ATTRIBUTE, 'bool', 'boolean',
                None, None,
                [], [],
                '''                TRUE to disable keepalives, FALSE to specify
                a new keepalive interval
                ''',
                'keepalive_disable',
                'Cisco-IOS-XR-ppp-ma-gbl-cfg', False),
            _MetaInfoClassMember('interval', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('10', '180')], [],
                '''                The keepalive interval. Leave unspecified
                when disabling keepalives
                ''',
                'interval',
                'Cisco-IOS-XR-ppp-ma-gbl-cfg', False, has_when=True),
            _MetaInfoClassMember('retry-count', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('1', '255')], [],
                '''                The keepalive retry count. Leave unspecified
                when disabling keepalives
                ''',
                'retry_count',
                'Cisco-IOS-XR-ppp-ma-gbl-cfg', False, has_when=True),
            ],
            'Cisco-IOS-XR-ppp-ma-gbl-cfg',
            'keepalive',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-ppp-ma-gbl-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg',
        ),
    },
    'DynamicTemplate.Ppps.Ppp.PppTemplate.Lcp' : {
        'meta_info' : _MetaInfoClass('DynamicTemplate.Ppps.Ppp.PppTemplate.Lcp', REFERENCE_CLASS,
            '''PPP LCP global template configuration data''',
            False, 
            [
            _MetaInfoClassMember('absolute-timeout', REFERENCE_CLASS, 'AbsoluteTimeout', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg', 'DynamicTemplate.Ppps.Ppp.PppTemplate.Lcp.AbsoluteTimeout',
                [], [],
                '''                This specifies the session absolute timeout
                value
                ''',
                'absolute_timeout',
                'Cisco-IOS-XR-ppp-ma-gbl-cfg', False),
            _MetaInfoClassMember('delay', REFERENCE_CLASS, 'Delay', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg', 'DynamicTemplate.Ppps.Ppp.PppTemplate.Lcp.Delay',
                [], [],
                '''                This specifies the time to delay before
                starting active LCPnegotiations
                ''',
                'delay',
                'Cisco-IOS-XR-ppp-ma-gbl-cfg', False),
            _MetaInfoClassMember('authentication', REFERENCE_CLASS, 'Authentication', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg', 'DynamicTemplate.Ppps.Ppp.PppTemplate.Lcp.Authentication',
                [], [],
                '''                PPP authentication parameters
                ''',
                'authentication',
                'Cisco-IOS-XR-ppp-ma-gbl-cfg', False),
            _MetaInfoClassMember('keepalive', REFERENCE_CLASS, 'Keepalive', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg', 'DynamicTemplate.Ppps.Ppp.PppTemplate.Lcp.Keepalive',
                [], [],
                '''                This specifies the rate at which EchoReq
                packets are sent
                ''',
                'keepalive',
                'Cisco-IOS-XR-ppp-ma-gbl-cfg', False),
            _MetaInfoClassMember('renegotiation', ATTRIBUTE, 'Empty', 'empty',
                None, None,
                [], [],
                '''                Specify whether to ignore attempts to
                renegotiate LCP
                ''',
                'renegotiation',
                'Cisco-IOS-XR-ppp-ma-gbl-cfg', False),
            _MetaInfoClassMember('service-type', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('0', '15')], [],
                '''                This is the Service-Type
                ''',
                'service_type',
                'Cisco-IOS-XR-ppp-ma-gbl-cfg', False, default_value="0"),
            _MetaInfoClassMember('send-term-request-on-shut-down', ATTRIBUTE, 'Empty', 'empty',
                None, None,
                [], [],
                '''                Enable Sending LCP Terminate request on
                shutdown
                ''',
                'send_term_request_on_shut_down',
                'Cisco-IOS-XR-ppp-ma-gbl-cfg', False),
            _MetaInfoClassMember('mru-ignore', ATTRIBUTE, 'Empty', 'empty',
                None, None,
                [], [],
                '''                Ignore MRU negotiated with peer while setting
                interface BW
                ''',
                'mru_ignore',
                'Cisco-IOS-XR-ppp-ma-gbl-cfg', False),
            ],
            'Cisco-IOS-XR-ppp-ma-gbl-cfg',
            'lcp',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-ppp-ma-gbl-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg',
        ),
    },
    'DynamicTemplate.Ppps.Ppp.PppTemplate.Ipv6cp' : {
        'meta_info' : _MetaInfoClass('DynamicTemplate.Ppps.Ppp.PppTemplate.Ipv6cp', REFERENCE_CLASS,
            '''PPP IPv6CP global template configuration data''',
            False, 
            [
            _MetaInfoClassMember('passive', ATTRIBUTE, 'Empty', 'empty',
                None, None,
                [], [],
                '''                Specify whether to run IPv6CP in Passive mode
                ''',
                'passive',
                'Cisco-IOS-XR-ppp-ma-gbl-cfg', False),
            _MetaInfoClassMember('renegotiation', ATTRIBUTE, 'Empty', 'empty',
                None, None,
                [], [],
                '''                Specify whether to ignore attempts to
                renegotiate IPv6CP
                ''',
                'renegotiation',
                'Cisco-IOS-XR-ppp-ma-gbl-cfg', False),
            _MetaInfoClassMember('peer-interface-id', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                Specify the Interface-Id to impose on the peer
                ''',
                'peer_interface_id',
                'Cisco-IOS-XR-ppp-ma-gbl-cfg', False),
            _MetaInfoClassMember('protocol-reject', ATTRIBUTE, 'Empty', 'empty',
                None, None,
                [], [],
                '''                Specify whether to protocol reject IPv6CP
                ''',
                'protocol_reject',
                'Cisco-IOS-XR-ppp-ma-gbl-cfg', False),
            ],
            'Cisco-IOS-XR-ppp-ma-gbl-cfg',
            'ipv6cp',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-ppp-ma-gbl-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg',
        ),
    },
    'DynamicTemplate.Ppps.Ppp.PppTemplate.Ipcp.Wins.WinsAddresses' : {
        'meta_info' : _MetaInfoClass('DynamicTemplate.Ppps.Ppp.PppTemplate.Ipcp.Wins.WinsAddresses', REFERENCE_CLASS,
            '''Specify WINS address(es) to provide''',
            False, 
            [
            _MetaInfoClassMember('primary', ATTRIBUTE, 'str', 'inet:ipv4-address-no-zone',
                None, None,
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'],
                '''                Primary WINS IP address
                ''',
                'primary',
                'Cisco-IOS-XR-ppp-ma-gbl-cfg', False),
            _MetaInfoClassMember('secondary', ATTRIBUTE, 'str', 'inet:ipv4-address-no-zone',
                None, None,
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'],
                '''                Secondary WINS IP address
                ''',
                'secondary',
                'Cisco-IOS-XR-ppp-ma-gbl-cfg', False),
            ],
            'Cisco-IOS-XR-ppp-ma-gbl-cfg',
            'wins-addresses',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-ppp-ma-gbl-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg',
        ),
    },
    'DynamicTemplate.Ppps.Ppp.PppTemplate.Ipcp.Wins' : {
        'meta_info' : _MetaInfoClass('DynamicTemplate.Ppps.Ppp.PppTemplate.Ipcp.Wins', REFERENCE_CLASS,
            '''IPCP WINS parameters''',
            False, 
            [
            _MetaInfoClassMember('wins-addresses', REFERENCE_CLASS, 'WinsAddresses', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg', 'DynamicTemplate.Ppps.Ppp.PppTemplate.Ipcp.Wins.WinsAddresses',
                [], [],
                '''                Specify WINS address(es) to provide
                ''',
                'wins_addresses',
                'Cisco-IOS-XR-ppp-ma-gbl-cfg', False),
            ],
            'Cisco-IOS-XR-ppp-ma-gbl-cfg',
            'wins',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-ppp-ma-gbl-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg',
        ),
    },
    'DynamicTemplate.Ppps.Ppp.PppTemplate.Ipcp.Dns.DnsAddresses' : {
        'meta_info' : _MetaInfoClass('DynamicTemplate.Ppps.Ppp.PppTemplate.Ipcp.Dns.DnsAddresses', REFERENCE_CLASS,
            '''Specify DNS address(es) to provide''',
            False, 
            [
            _MetaInfoClassMember('primary', ATTRIBUTE, 'str', 'inet:ipv4-address-no-zone',
                None, None,
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'],
                '''                Primary DNS IP address
                ''',
                'primary',
                'Cisco-IOS-XR-ppp-ma-gbl-cfg', False),
            _MetaInfoClassMember('secondary', ATTRIBUTE, 'str', 'inet:ipv4-address-no-zone',
                None, None,
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'],
                '''                Secondary DNS IP address
                ''',
                'secondary',
                'Cisco-IOS-XR-ppp-ma-gbl-cfg', False),
            ],
            'Cisco-IOS-XR-ppp-ma-gbl-cfg',
            'dns-addresses',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-ppp-ma-gbl-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg',
        ),
    },
    'DynamicTemplate.Ppps.Ppp.PppTemplate.Ipcp.Dns' : {
        'meta_info' : _MetaInfoClass('DynamicTemplate.Ppps.Ppp.PppTemplate.Ipcp.Dns', REFERENCE_CLASS,
            '''IPCP DNS parameters''',
            False, 
            [
            _MetaInfoClassMember('dns-addresses', REFERENCE_CLASS, 'DnsAddresses', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg', 'DynamicTemplate.Ppps.Ppp.PppTemplate.Ipcp.Dns.DnsAddresses',
                [], [],
                '''                Specify DNS address(es) to provide
                ''',
                'dns_addresses',
                'Cisco-IOS-XR-ppp-ma-gbl-cfg', False),
            ],
            'Cisco-IOS-XR-ppp-ma-gbl-cfg',
            'dns',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-ppp-ma-gbl-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg',
        ),
    },
    'DynamicTemplate.Ppps.Ppp.PppTemplate.Ipcp.PeerAddress' : {
        'meta_info' : _MetaInfoClass('DynamicTemplate.Ppps.Ppp.PppTemplate.Ipcp.PeerAddress', REFERENCE_CLASS,
            '''IPCP address parameters''',
            False, 
            [
            _MetaInfoClassMember('default', ATTRIBUTE, 'str', 'inet:ipv4-address-no-zone',
                None, None,
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'],
                '''                Specify an IP address to assign to peers
                through IPCP
                ''',
                'default',
                'Cisco-IOS-XR-ppp-ma-gbl-cfg', False),
            _MetaInfoClassMember('pool', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                Accepts an IP address from the peer if in the
                pool, else allocates one from the pool
                ''',
                'pool',
                'Cisco-IOS-XR-ppp-ma-gbl-cfg', False),
            ],
            'Cisco-IOS-XR-ppp-ma-gbl-cfg',
            'peer-address',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-ppp-ma-gbl-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg',
        ),
    },
    'DynamicTemplate.Ppps.Ppp.PppTemplate.Ipcp' : {
        'meta_info' : _MetaInfoClass('DynamicTemplate.Ppps.Ppp.PppTemplate.Ipcp', REFERENCE_CLASS,
            '''PPP IPCP global template configuration data''',
            False, 
            [
            _MetaInfoClassMember('wins', REFERENCE_CLASS, 'Wins', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg', 'DynamicTemplate.Ppps.Ppp.PppTemplate.Ipcp.Wins',
                [], [],
                '''                IPCP WINS parameters
                ''',
                'wins',
                'Cisco-IOS-XR-ppp-ma-gbl-cfg', False),
            _MetaInfoClassMember('dns', REFERENCE_CLASS, 'Dns', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg', 'DynamicTemplate.Ppps.Ppp.PppTemplate.Ipcp.Dns',
                [], [],
                '''                IPCP DNS parameters
                ''',
                'dns',
                'Cisco-IOS-XR-ppp-ma-gbl-cfg', False),
            _MetaInfoClassMember('peer-address', REFERENCE_CLASS, 'PeerAddress', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg', 'DynamicTemplate.Ppps.Ppp.PppTemplate.Ipcp.PeerAddress',
                [], [],
                '''                IPCP address parameters
                ''',
                'peer_address',
                'Cisco-IOS-XR-ppp-ma-gbl-cfg', False),
            _MetaInfoClassMember('renegotiation', ATTRIBUTE, 'Empty', 'empty',
                None, None,
                [], [],
                '''                Specify whether to ignore attempts to
                renegotiate IPCP
                ''',
                'renegotiation',
                'Cisco-IOS-XR-ppp-ma-gbl-cfg', False),
            _MetaInfoClassMember('passive', ATTRIBUTE, 'Empty', 'empty',
                None, None,
                [], [],
                '''                Specify whether to run IPCP in Passive mode
                ''',
                'passive',
                'Cisco-IOS-XR-ppp-ma-gbl-cfg', False),
            _MetaInfoClassMember('protocol-reject', ATTRIBUTE, 'Empty', 'empty',
                None, None,
                [], [],
                '''                Specify whether to protocol reject IPCP
                ''',
                'protocol_reject',
                'Cisco-IOS-XR-ppp-ma-gbl-cfg', False),
            _MetaInfoClassMember('peer-netmask', ATTRIBUTE, 'str', 'inet:ipv4-address-no-zone',
                None, None,
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'],
                '''                Specify the IPv4 netmask to negotiate for the
                peer
                ''',
                'peer_netmask',
                'Cisco-IOS-XR-ppp-ma-gbl-cfg', False),
            ],
            'Cisco-IOS-XR-ppp-ma-gbl-cfg',
            'ipcp',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-ppp-ma-gbl-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg',
        ),
    },
    'DynamicTemplate.Ppps.Ppp.PppTemplate' : {
        'meta_info' : _MetaInfoClass('DynamicTemplate.Ppps.Ppp.PppTemplate', REFERENCE_CLASS,
            '''PPP template configuration data''',
            False, 
            [
            _MetaInfoClassMember('fsm', REFERENCE_CLASS, 'Fsm', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg', 'DynamicTemplate.Ppps.Ppp.PppTemplate.Fsm',
                [], [],
                '''                PPP FSM global template configuration data
                ''',
                'fsm',
                'Cisco-IOS-XR-ppp-ma-gbl-cfg', False),
            _MetaInfoClassMember('lcp', REFERENCE_CLASS, 'Lcp', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg', 'DynamicTemplate.Ppps.Ppp.PppTemplate.Lcp',
                [], [],
                '''                PPP LCP global template configuration data
                ''',
                'lcp',
                'Cisco-IOS-XR-ppp-ma-gbl-cfg', False),
            _MetaInfoClassMember('ipv6cp', REFERENCE_CLASS, 'Ipv6cp', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg', 'DynamicTemplate.Ppps.Ppp.PppTemplate.Ipv6cp',
                [], [],
                '''                PPP IPv6CP global template configuration data
                ''',
                'ipv6cp',
                'Cisco-IOS-XR-ppp-ma-gbl-cfg', False),
            _MetaInfoClassMember('ipcp', REFERENCE_CLASS, 'Ipcp', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg', 'DynamicTemplate.Ppps.Ppp.PppTemplate.Ipcp',
                [], [],
                '''                PPP IPCP global template configuration data
                ''',
                'ipcp',
                'Cisco-IOS-XR-ppp-ma-gbl-cfg', False),
            ],
            'Cisco-IOS-XR-ppp-ma-gbl-cfg',
            'ppp-template',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-ppp-ma-gbl-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg',
        ),
    },
    'DynamicTemplate.Ppps.Ppp.Pbr.ServicePolicies.ServicePolicy' : {
        'meta_info' : _MetaInfoClass('DynamicTemplate.Ppps.Ppp.Pbr.ServicePolicies.ServicePolicy', REFERENCE_LIST,
            '''Service policy details''',
            False, 
            [
            _MetaInfoClassMember('service-policy', ATTRIBUTE, 'str', 'string',
                None, None,
                [(1, 64)], [],
                '''                Name of policy-map
                ''',
                'service_policy',
                'Cisco-IOS-XR-pbr-subscriber-cfg', True),
            ],
            'Cisco-IOS-XR-pbr-subscriber-cfg',
            'service-policy',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-pbr-subscriber-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg',
        ),
    },
    'DynamicTemplate.Ppps.Ppp.Pbr.ServicePolicies' : {
        'meta_info' : _MetaInfoClass('DynamicTemplate.Ppps.Ppp.Pbr.ServicePolicies', REFERENCE_CLASS,
            '''Ingress service policy''',
            False, 
            [
            _MetaInfoClassMember('service-policy', REFERENCE_LIST, 'ServicePolicy', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg', 'DynamicTemplate.Ppps.Ppp.Pbr.ServicePolicies.ServicePolicy',
                [], [],
                '''                Service policy details
                ''',
                'service_policy',
                'Cisco-IOS-XR-pbr-subscriber-cfg', False),
            ],
            'Cisco-IOS-XR-pbr-subscriber-cfg',
            'service-policies',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-pbr-subscriber-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg',
        ),
    },
    'DynamicTemplate.Ppps.Ppp.Pbr' : {
        'meta_info' : _MetaInfoClass('DynamicTemplate.Ppps.Ppp.Pbr', REFERENCE_CLASS,
            '''Dynamic Template PBR configuration''',
            False, 
            [
            _MetaInfoClassMember('service-policies', REFERENCE_CLASS, 'ServicePolicies', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg', 'DynamicTemplate.Ppps.Ppp.Pbr.ServicePolicies',
                [], [],
                '''                Ingress service policy
                ''',
                'service_policies',
                'Cisco-IOS-XR-pbr-subscriber-cfg', False),
            _MetaInfoClassMember('service-policy-in', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                Class for subscriber ingress policy
                ''',
                'service_policy_in',
                'Cisco-IOS-XR-pbr-subscriber-cfg', False),
            ],
            'Cisco-IOS-XR-pbr-subscriber-cfg',
            'pbr',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-pbr-subscriber-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg',
        ),
    },
    'DynamicTemplate.Ppps.Ppp.Ipv4PacketFilter.Outbound' : {
        'meta_info' : _MetaInfoClass('DynamicTemplate.Ppps.Ppp.Ipv4PacketFilter.Outbound', REFERENCE_CLASS,
            '''IPv4 Packet filter to be applied to outbound
packets''',
            False, 
            [
            _MetaInfoClassMember('common-acl-name', ATTRIBUTE, 'str', 'xr:Cisco-ios-xr-string',
                None, None,
                [(1, 64)], [],
                '''                Not supported (Leave unspecified).
                ''',
                'common_acl_name',
                'Cisco-IOS-XR-ip-pfilter-subscriber-cfg', False),
            _MetaInfoClassMember('name', ATTRIBUTE, 'str', 'xr:Cisco-ios-xr-string',
                None, None,
                [(1, 64)], [],
                '''                IPv4 Packet Filter Name to be applied to
                Outbound packets.
                ''',
                'name',
                'Cisco-IOS-XR-ip-pfilter-subscriber-cfg', False),
            _MetaInfoClassMember('hardware-count', ATTRIBUTE, 'Empty', 'empty',
                None, None,
                [], [],
                '''                Not supported (Leave unspecified).
                ''',
                'hardware_count',
                'Cisco-IOS-XR-ip-pfilter-subscriber-cfg', False),
            _MetaInfoClassMember('interface-statistics', ATTRIBUTE, 'Empty', 'empty',
                None, None,
                [], [],
                '''                Not supported (Leave unspecified).
                ''',
                'interface_statistics',
                'Cisco-IOS-XR-ip-pfilter-subscriber-cfg', False),
            ],
            'Cisco-IOS-XR-ip-pfilter-subscriber-cfg',
            'outbound',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-ip-pfilter-subscriber-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg',
        ),
    },
    'DynamicTemplate.Ppps.Ppp.Ipv4PacketFilter.Inbound' : {
        'meta_info' : _MetaInfoClass('DynamicTemplate.Ppps.Ppp.Ipv4PacketFilter.Inbound', REFERENCE_CLASS,
            '''IPv4 Packet filter to be applied to inbound
packets''',
            False, 
            [
            _MetaInfoClassMember('common-acl-name', ATTRIBUTE, 'str', 'xr:Cisco-ios-xr-string',
                None, None,
                [(1, 64)], [],
                '''                Not supported (Leave unspecified).
                ''',
                'common_acl_name',
                'Cisco-IOS-XR-ip-pfilter-subscriber-cfg', False),
            _MetaInfoClassMember('name', ATTRIBUTE, 'str', 'xr:Cisco-ios-xr-string',
                None, None,
                [(1, 64)], [],
                '''                IPv4 Packet Filter Name to be applied to
                Inbound packets NOTE: This parameter is
                mandatory if 'CommonACLName' is not specified.
                ''',
                'name',
                'Cisco-IOS-XR-ip-pfilter-subscriber-cfg', False),
            _MetaInfoClassMember('hardware-count', ATTRIBUTE, 'Empty', 'empty',
                None, None,
                [], [],
                '''                Not supported (Leave unspecified).
                ''',
                'hardware_count',
                'Cisco-IOS-XR-ip-pfilter-subscriber-cfg', False),
            _MetaInfoClassMember('interface-statistics', ATTRIBUTE, 'Empty', 'empty',
                None, None,
                [], [],
                '''                Not supported (Leave unspecified).
                ''',
                'interface_statistics',
                'Cisco-IOS-XR-ip-pfilter-subscriber-cfg', False),
            ],
            'Cisco-IOS-XR-ip-pfilter-subscriber-cfg',
            'inbound',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-ip-pfilter-subscriber-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg',
        ),
    },
    'DynamicTemplate.Ppps.Ppp.Ipv4PacketFilter' : {
        'meta_info' : _MetaInfoClass('DynamicTemplate.Ppps.Ppp.Ipv4PacketFilter', REFERENCE_CLASS,
            '''IPv4 Packet Filtering configuration for the
template''',
            False, 
            [
            _MetaInfoClassMember('outbound', REFERENCE_CLASS, 'Outbound', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg', 'DynamicTemplate.Ppps.Ppp.Ipv4PacketFilter.Outbound',
                [], [],
                '''                IPv4 Packet filter to be applied to outbound
                packets
                ''',
                'outbound',
                'Cisco-IOS-XR-ip-pfilter-subscriber-cfg', False),
            _MetaInfoClassMember('inbound', REFERENCE_CLASS, 'Inbound', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg', 'DynamicTemplate.Ppps.Ppp.Ipv4PacketFilter.Inbound',
                [], [],
                '''                IPv4 Packet filter to be applied to inbound
                packets
                ''',
                'inbound',
                'Cisco-IOS-XR-ip-pfilter-subscriber-cfg', False),
            ],
            'Cisco-IOS-XR-ip-pfilter-subscriber-cfg',
            'ipv4-packet-filter',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-ip-pfilter-subscriber-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg',
        ),
    },
    'DynamicTemplate.Ppps.Ppp.Ipv6PacketFilter.Inbound' : {
        'meta_info' : _MetaInfoClass('DynamicTemplate.Ppps.Ppp.Ipv6PacketFilter.Inbound', REFERENCE_CLASS,
            '''IPv6 Packet filter to be applied to inbound
packets''',
            False, 
            [
            _MetaInfoClassMember('common-acl-name', ATTRIBUTE, 'str', 'xr:Cisco-ios-xr-string',
                None, None,
                [(1, 64)], [],
                '''                Not supported (Leave unspecified).
                ''',
                'common_acl_name',
                'Cisco-IOS-XR-ip-pfilter-subscriber-cfg', False),
            _MetaInfoClassMember('name', ATTRIBUTE, 'str', 'xr:Cisco-ios-xr-string',
                None, None,
                [(1, 64)], [],
                '''                IPv6 Packet Filter Name to be applied to
                Inbound  NOTE: This parameter is mandatory if
                'CommonACLName' is not specified.
                ''',
                'name',
                'Cisco-IOS-XR-ip-pfilter-subscriber-cfg', False),
            _MetaInfoClassMember('interface-statistics', ATTRIBUTE, 'Empty', 'empty',
                None, None,
                [], [],
                '''                Not supported (Leave unspecified).
                ''',
                'interface_statistics',
                'Cisco-IOS-XR-ip-pfilter-subscriber-cfg', False),
            ],
            'Cisco-IOS-XR-ip-pfilter-subscriber-cfg',
            'inbound',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-ip-pfilter-subscriber-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg',
        ),
    },
    'DynamicTemplate.Ppps.Ppp.Ipv6PacketFilter.Outbound' : {
        'meta_info' : _MetaInfoClass('DynamicTemplate.Ppps.Ppp.Ipv6PacketFilter.Outbound', REFERENCE_CLASS,
            '''IPv6 Packet filter to be applied to outbound
packets''',
            False, 
            [
            _MetaInfoClassMember('common-acl-name', ATTRIBUTE, 'str', 'xr:Cisco-ios-xr-string',
                None, None,
                [(1, 64)], [],
                '''                Not supported (Leave unspecified).
                ''',
                'common_acl_name',
                'Cisco-IOS-XR-ip-pfilter-subscriber-cfg', False),
            _MetaInfoClassMember('name', ATTRIBUTE, 'str', 'xr:Cisco-ios-xr-string',
                None, None,
                [(1, 64)], [],
                '''                IPv6 Packet Filter Name to be applied to
                Outbound packets.
                ''',
                'name',
                'Cisco-IOS-XR-ip-pfilter-subscriber-cfg', False),
            _MetaInfoClassMember('interface-statistics', ATTRIBUTE, 'Empty', 'empty',
                None, None,
                [], [],
                '''                Not supported (Leave unspecified).
                ''',
                'interface_statistics',
                'Cisco-IOS-XR-ip-pfilter-subscriber-cfg', False),
            ],
            'Cisco-IOS-XR-ip-pfilter-subscriber-cfg',
            'outbound',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-ip-pfilter-subscriber-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg',
        ),
    },
    'DynamicTemplate.Ppps.Ppp.Ipv6PacketFilter' : {
        'meta_info' : _MetaInfoClass('DynamicTemplate.Ppps.Ppp.Ipv6PacketFilter', REFERENCE_CLASS,
            '''IPv6 Packet Filtering configuration for the
interface''',
            False, 
            [
            _MetaInfoClassMember('inbound', REFERENCE_CLASS, 'Inbound', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg', 'DynamicTemplate.Ppps.Ppp.Ipv6PacketFilter.Inbound',
                [], [],
                '''                IPv6 Packet filter to be applied to inbound
                packets
                ''',
                'inbound',
                'Cisco-IOS-XR-ip-pfilter-subscriber-cfg', False),
            _MetaInfoClassMember('outbound', REFERENCE_CLASS, 'Outbound', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg', 'DynamicTemplate.Ppps.Ppp.Ipv6PacketFilter.Outbound',
                [], [],
                '''                IPv6 Packet filter to be applied to outbound
                packets
                ''',
                'outbound',
                'Cisco-IOS-XR-ip-pfilter-subscriber-cfg', False),
            ],
            'Cisco-IOS-XR-ip-pfilter-subscriber-cfg',
            'ipv6-packet-filter',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-ip-pfilter-subscriber-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg',
        ),
    },
    'DynamicTemplate.Ppps.Ppp.Dhcpv6.DelegatedPrefix' : {
        'meta_info' : _MetaInfoClass('DynamicTemplate.Ppps.Ppp.Dhcpv6.DelegatedPrefix', REFERENCE_CLASS,
            '''The prefix to be used for Prefix Delegation''',
            False, 
            [
            _MetaInfoClassMember('prefix', ATTRIBUTE, 'str', 'inet:ipv6-address-no-zone',
                None, None,
                [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'],
                '''                IPv6 Prefix
                ''',
                'prefix',
                'Cisco-IOS-XR-ipv6-new-dhcpv6d-subscriber-cfg', False, is_mandatory=True),
            _MetaInfoClassMember('prefix-length', ATTRIBUTE, 'int', 'xr:Ipv6-prefix-length',
                None, None,
                [('0', '128')], [],
                '''                PD Prefix Length
                ''',
                'prefix_length',
                'Cisco-IOS-XR-ipv6-new-dhcpv6d-subscriber-cfg', False, is_mandatory=True),
            ],
            'Cisco-IOS-XR-ipv6-new-dhcpv6d-subscriber-cfg',
            'delegated-prefix',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-ipv6-new-dhcpv6d-subscriber-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg',
            is_presence=True,
        ),
    },
    'DynamicTemplate.Ppps.Ppp.Dhcpv6' : {
        'meta_info' : _MetaInfoClass('DynamicTemplate.Ppps.Ppp.Dhcpv6', REFERENCE_CLASS,
            '''Interface dhcpv6 configuration data''',
            False, 
            [
            _MetaInfoClassMember('delegated-prefix', REFERENCE_CLASS, 'DelegatedPrefix', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg', 'DynamicTemplate.Ppps.Ppp.Dhcpv6.DelegatedPrefix',
                [], [],
                '''                The prefix to be used for Prefix Delegation
                ''',
                'delegated_prefix',
                'Cisco-IOS-XR-ipv6-new-dhcpv6d-subscriber-cfg', False, is_presence=True),
            _MetaInfoClassMember('dns-ipv6address', ATTRIBUTE, 'str', 'inet:ipv6-address-no-zone',
                None, None,
                [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'],
                '''                Dns IPv6 Address
                ''',
                'dns_ipv6address',
                'Cisco-IOS-XR-ipv6-new-dhcpv6d-subscriber-cfg', False),
            _MetaInfoClassMember('mode-class', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                Select proxy/server profile based on mode class
                name
                ''',
                'mode_class',
                'Cisco-IOS-XR-ipv6-new-dhcpv6d-subscriber-cfg', False),
            _MetaInfoClassMember('dhcpv6-iplease', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                Cisco VSA to configure any dhcpv6 ip lease per
                subscriber
                ''',
                'dhcpv6_iplease',
                'Cisco-IOS-XR-ipv6-new-dhcpv6d-subscriber-cfg', False),
            _MetaInfoClassMember('dhcpv6-option', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                Cisco VSA to configure any dhcpv6 option per
                subscriber
                ''',
                'dhcpv6_option',
                'Cisco-IOS-XR-ipv6-new-dhcpv6d-subscriber-cfg', False),
            _MetaInfoClassMember('address-pool', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                The pool to be used for Address assignment
                ''',
                'address_pool',
                'Cisco-IOS-XR-ipv6-new-dhcpv6d-subscriber-cfg', False),
            _MetaInfoClassMember('delegated-prefix-pool', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                The pool to be used for Prefix Delegation
                ''',
                'delegated_prefix_pool',
                'Cisco-IOS-XR-ipv6-new-dhcpv6d-subscriber-cfg', False),
            _MetaInfoClassMember('class', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                The class to be used for proxy/server profile
                ''',
                'class_',
                'Cisco-IOS-XR-ipv6-new-dhcpv6d-subscriber-cfg', False),
            _MetaInfoClassMember('stateful-address', ATTRIBUTE, 'str', 'inet:ipv6-address-no-zone',
                None, None,
                [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'],
                '''                Stateful IPv6 Address
                ''',
                'stateful_address',
                'Cisco-IOS-XR-ipv6-new-dhcpv6d-subscriber-cfg', False),
            ],
            'Cisco-IOS-XR-ipv6-new-dhcpv6d-subscriber-cfg',
            'dhcpv6',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-ipv6-new-dhcpv6d-subscriber-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg',
        ),
    },
    'DynamicTemplate.Ppps.Ppp' : {
        'meta_info' : _MetaInfoClass('DynamicTemplate.Ppps.Ppp', REFERENCE_LIST,
            '''A Template of the PPP Type''',
            False, 
            [
            _MetaInfoClassMember('template-name', ATTRIBUTE, 'str', 'xr:Cisco-ios-xr-string',
                None, None,
                [], [b'[\\w\\-\\.:,_@#%$\\+=\\|;]+'],
                '''                The name of the template
                ''',
                'template_name',
                'Cisco-IOS-XR-subscriber-infra-tmplmgr-cfg', True),
            _MetaInfoClassMember('ipv4-network', REFERENCE_CLASS, 'Ipv4Network', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg', 'DynamicTemplate.Ppps.Ppp.Ipv4Network',
                [], [],
                '''                Interface IPv4 Network configuration data
                ''',
                'ipv4_network',
                'Cisco-IOS-XR-ipv4-ma-subscriber-cfg', False),
            _MetaInfoClassMember('accounting', REFERENCE_CLASS, 'Accounting', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg', 'DynamicTemplate.Ppps.Ppp.Accounting',
                [], [],
                '''                Subscriber accounting dynamic-template commands
                ''',
                'accounting',
                'Cisco-IOS-XR-subscriber-accounting-cfg', False),
            _MetaInfoClassMember('qos', REFERENCE_CLASS, 'Qos', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg', 'DynamicTemplate.Ppps.Ppp.Qos',
                [], [],
                '''                QoS dynamically applied configuration template
                ''',
                'qos',
                'Cisco-IOS-XR-qos-ma-bng-cfg', False),
            _MetaInfoClassMember('igmp', REFERENCE_CLASS, 'Igmp', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg', 'DynamicTemplate.Ppps.Ppp.Igmp',
                [], [],
                '''                IGMPconfiguration
                ''',
                'igmp',
                'Cisco-IOS-XR-ipv4-igmp-dyn-tmpl-cfg', False),
            _MetaInfoClassMember('ipv6-network', REFERENCE_CLASS, 'Ipv6Network', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg', 'DynamicTemplate.Ppps.Ppp.Ipv6Network',
                [], [],
                '''                Interface IPv6 Network configuration data
                ''',
                'ipv6_network',
                'Cisco-IOS-XR-ipv6-ma-subscriber-cfg', False),
            _MetaInfoClassMember('pppoe-template', REFERENCE_CLASS, 'PppoeTemplate', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg', 'DynamicTemplate.Ppps.Ppp.PppoeTemplate',
                [], [],
                '''                PPPoE template configuration data
                ''',
                'pppoe_template',
                'Cisco-IOS-XR-subscriber-pppoe-ma-gbl-cfg', False, is_presence=True),
            _MetaInfoClassMember('span-monitor-sessions', REFERENCE_CLASS, 'SpanMonitorSessions', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg', 'DynamicTemplate.Ppps.Ppp.SpanMonitorSessions',
                [], [],
                '''                Monitor Session container for this template
                ''',
                'span_monitor_sessions',
                'Cisco-IOS-XR-Ethernet-SPAN-subscriber-cfg', False),
            _MetaInfoClassMember('vrf', ATTRIBUTE, 'str', 'xr:Cisco-ios-xr-string',
                None, None,
                [(1, 32)], [],
                '''                Assign the interface to a VRF 
                ''',
                'vrf',
                'Cisco-IOS-XR-infra-rsi-subscriber-cfg', False),
            _MetaInfoClassMember('ipv6-neighbor', REFERENCE_CLASS, 'Ipv6Neighbor', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg', 'DynamicTemplate.Ppps.Ppp.Ipv6Neighbor',
                [], [],
                '''                Interface IPv6 Network configuration data
                ''',
                'ipv6_neighbor',
                'Cisco-IOS-XR-ipv6-nd-subscriber-cfg', False),
            _MetaInfoClassMember('ppp-template', REFERENCE_CLASS, 'PppTemplate', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg', 'DynamicTemplate.Ppps.Ppp.PppTemplate',
                [], [],
                '''                PPP template configuration data
                ''',
                'ppp_template',
                'Cisco-IOS-XR-ppp-ma-gbl-cfg', False),
            _MetaInfoClassMember('pbr', REFERENCE_CLASS, 'Pbr', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg', 'DynamicTemplate.Ppps.Ppp.Pbr',
                [], [],
                '''                Dynamic Template PBR configuration
                ''',
                'pbr',
                'Cisco-IOS-XR-pbr-subscriber-cfg', False),
            _MetaInfoClassMember('ipv4-packet-filter', REFERENCE_CLASS, 'Ipv4PacketFilter', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg', 'DynamicTemplate.Ppps.Ppp.Ipv4PacketFilter',
                [], [],
                '''                IPv4 Packet Filtering configuration for the
                template
                ''',
                'ipv4_packet_filter',
                'Cisco-IOS-XR-ip-pfilter-subscriber-cfg', False),
            _MetaInfoClassMember('ipv6-packet-filter', REFERENCE_CLASS, 'Ipv6PacketFilter', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg', 'DynamicTemplate.Ppps.Ppp.Ipv6PacketFilter',
                [], [],
                '''                IPv6 Packet Filtering configuration for the
                interface
                ''',
                'ipv6_packet_filter',
                'Cisco-IOS-XR-ip-pfilter-subscriber-cfg', False),
            _MetaInfoClassMember('dhcpv6', REFERENCE_CLASS, 'Dhcpv6', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg', 'DynamicTemplate.Ppps.Ppp.Dhcpv6',
                [], [],
                '''                Interface dhcpv6 configuration data
                ''',
                'dhcpv6',
                'Cisco-IOS-XR-ipv6-new-dhcpv6d-subscriber-cfg', False),
            ],
            'Cisco-IOS-XR-subscriber-infra-tmplmgr-cfg',
            'ppp',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-subscriber-infra-tmplmgr-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg',
        ),
    },
    'DynamicTemplate.Ppps' : {
        'meta_info' : _MetaInfoClass('DynamicTemplate.Ppps', REFERENCE_CLASS,
            '''Templates of the PPP Type''',
            False, 
            [
            _MetaInfoClassMember('ppp', REFERENCE_LIST, 'Ppp', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg', 'DynamicTemplate.Ppps.Ppp',
                [], [],
                '''                A Template of the PPP Type
                ''',
                'ppp',
                'Cisco-IOS-XR-subscriber-infra-tmplmgr-cfg', False),
            ],
            'Cisco-IOS-XR-subscriber-infra-tmplmgr-cfg',
            'ppps',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-subscriber-infra-tmplmgr-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg',
        ),
    },
    'DynamicTemplate.IpSubscribers.IpSubscriber.Ipv4Network' : {
        'meta_info' : _MetaInfoClass('DynamicTemplate.IpSubscribers.IpSubscriber.Ipv4Network', REFERENCE_CLASS,
            '''Interface IPv4 Network configuration data''',
            False, 
            [
            _MetaInfoClassMember('unnumbered', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                Enable IP processing without an explicit
                address
                ''',
                'unnumbered',
                'Cisco-IOS-XR-ipv4-ma-subscriber-cfg', False),
            _MetaInfoClassMember('mtu', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('68', '65535')], [],
                '''                The IP Maximum Transmission Unit
                ''',
                'mtu',
                'Cisco-IOS-XR-ipv4-ma-subscriber-cfg', False),
            _MetaInfoClassMember('unreachables', ATTRIBUTE, 'bool', 'boolean',
                None, None,
                [], [],
                '''                TRUE if enabled, FALSE if disabled
                ''',
                'unreachables',
                'Cisco-IOS-XR-ipv4-ma-subscriber-cfg', False, default_value='False'),
            _MetaInfoClassMember('rpf', ATTRIBUTE, 'bool', 'boolean',
                None, None,
                [], [],
                '''                TRUE if enabled, FALSE if disabled
                ''',
                'rpf',
                'Cisco-IOS-XR-ipv4-ma-subscriber-cfg', False, default_value='True'),
            ],
            'Cisco-IOS-XR-ipv4-ma-subscriber-cfg',
            'ipv4-network',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-ipv4-ma-subscriber-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg',
        ),
    },
    'DynamicTemplate.IpSubscribers.IpSubscriber.Accounting.ServiceAccounting' : {
        'meta_info' : _MetaInfoClass('DynamicTemplate.IpSubscribers.IpSubscriber.Accounting.ServiceAccounting', REFERENCE_CLASS,
            '''Subscriber accounting service accounting''',
            False, 
            [
            _MetaInfoClassMember('method-list-name', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                Service accounting method list name
                ''',
                'method_list_name',
                'Cisco-IOS-XR-subscriber-accounting-cfg', False),
            _MetaInfoClassMember('accounting-interim-interval', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('0', '4294967295')], [],
                '''                Accounting interim interval in minutes
                ''',
                'accounting_interim_interval',
                'Cisco-IOS-XR-subscriber-accounting-cfg', False),
            ],
            'Cisco-IOS-XR-subscriber-accounting-cfg',
            'service-accounting',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-subscriber-accounting-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg',
        ),
    },
    'DynamicTemplate.IpSubscribers.IpSubscriber.Accounting.Session.HoldAcctStart' : _MetaInfoEnum('HoldAcctStart',
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg', 'DynamicTemplate.IpSubscribers.IpSubscriber.Accounting.Session.HoldAcctStart',
        '''Hold Accounting start based on IA_PD''',
        {
            'ipv6-prefix-delegation':'ipv6_prefix_delegation',
        }, 'Cisco-IOS-XR-subscriber-accounting-cfg', _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-subscriber-accounting-cfg']),
    'DynamicTemplate.IpSubscribers.IpSubscriber.Accounting.Session' : {
        'meta_info' : _MetaInfoClass('DynamicTemplate.IpSubscribers.IpSubscriber.Accounting.Session', REFERENCE_CLASS,
            '''Subscriber accounting session accounting''',
            False, 
            [
            _MetaInfoClassMember('method-list-name', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                Session accounting method list name
                ''',
                'method_list_name',
                'Cisco-IOS-XR-subscriber-accounting-cfg', False),
            _MetaInfoClassMember('periodic-interval', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('0', '4294967295')], [],
                '''                Interim accounting interval in minutes
                ''',
                'periodic_interval',
                'Cisco-IOS-XR-subscriber-accounting-cfg', False),
            _MetaInfoClassMember('dual-stack-delay', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('0', '4294967295')], [],
                '''                Dual stack wait delay in seconds
                ''',
                'dual_stack_delay',
                'Cisco-IOS-XR-subscriber-accounting-cfg', False),
            _MetaInfoClassMember('hold-acct-start', REFERENCE_ENUM_CLASS, 'HoldAcctStart', 'enumeration',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg', 'DynamicTemplate.IpSubscribers.IpSubscriber.Accounting.Session.HoldAcctStart',
                [], [],
                '''                Hold Accounting start based on IA_PD
                ''',
                'hold_acct_start',
                'Cisco-IOS-XR-subscriber-accounting-cfg', False),
            ],
            'Cisco-IOS-XR-subscriber-accounting-cfg',
            'session',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-subscriber-accounting-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg',
        ),
    },
    'DynamicTemplate.IpSubscribers.IpSubscriber.Accounting.IdleTimeout' : {
        'meta_info' : _MetaInfoClass('DynamicTemplate.IpSubscribers.IpSubscriber.Accounting.IdleTimeout', REFERENCE_CLASS,
            '''Subscriber accounting idle timeout''',
            False, 
            [
            _MetaInfoClassMember('timeout-value', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('60', '4320000')], [],
                '''                Idle timeout value in seconds
                ''',
                'timeout_value',
                'Cisco-IOS-XR-subscriber-accounting-cfg', False),
            _MetaInfoClassMember('threshold', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('1', '10000')], [],
                '''                Threshold in minute(s) per packet
                ''',
                'threshold',
                'Cisco-IOS-XR-subscriber-accounting-cfg', False),
            _MetaInfoClassMember('direction', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                Idle timeout traffic direction
                ''',
                'direction',
                'Cisco-IOS-XR-subscriber-accounting-cfg', False),
            ],
            'Cisco-IOS-XR-subscriber-accounting-cfg',
            'idle-timeout',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-subscriber-accounting-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg',
        ),
    },
    'DynamicTemplate.IpSubscribers.IpSubscriber.Accounting' : {
        'meta_info' : _MetaInfoClass('DynamicTemplate.IpSubscribers.IpSubscriber.Accounting', REFERENCE_CLASS,
            '''Subscriber accounting dynamic-template commands''',
            False, 
            [
            _MetaInfoClassMember('service-accounting', REFERENCE_CLASS, 'ServiceAccounting', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg', 'DynamicTemplate.IpSubscribers.IpSubscriber.Accounting.ServiceAccounting',
                [], [],
                '''                Subscriber accounting service accounting
                ''',
                'service_accounting',
                'Cisco-IOS-XR-subscriber-accounting-cfg', False),
            _MetaInfoClassMember('session', REFERENCE_CLASS, 'Session', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg', 'DynamicTemplate.IpSubscribers.IpSubscriber.Accounting.Session',
                [], [],
                '''                Subscriber accounting session accounting
                ''',
                'session',
                'Cisco-IOS-XR-subscriber-accounting-cfg', False),
            _MetaInfoClassMember('idle-timeout', REFERENCE_CLASS, 'IdleTimeout', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg', 'DynamicTemplate.IpSubscribers.IpSubscriber.Accounting.IdleTimeout',
                [], [],
                '''                Subscriber accounting idle timeout
                ''',
                'idle_timeout',
                'Cisco-IOS-XR-subscriber-accounting-cfg', False),
            _MetaInfoClassMember('monitor-feature', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                Subscriber monitor feature
                ''',
                'monitor_feature',
                'Cisco-IOS-XR-subscriber-accounting-cfg', False),
            _MetaInfoClassMember('prepaid-feature', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                Subscriber accounting prepaid feature
                ''',
                'prepaid_feature',
                'Cisco-IOS-XR-subscriber-accounting-cfg', False),
            ],
            'Cisco-IOS-XR-subscriber-accounting-cfg',
            'accounting',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-subscriber-accounting-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg',
        ),
    },
    'DynamicTemplate.IpSubscribers.IpSubscriber.Qos.ServicePolicy.Input' : {
        'meta_info' : _MetaInfoClass('DynamicTemplate.IpSubscribers.IpSubscriber.Qos.ServicePolicy.Input', REFERENCE_CLASS,
            '''Subscriber ingress policy''',
            False, 
            [
            _MetaInfoClassMember('policy-name', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                Name of policy-map
                ''',
                'policy_name',
                'Cisco-IOS-XR-qos-ma-bng-cfg', False, is_mandatory=True),
            _MetaInfoClassMember('spi-name', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                Name of the SPI
                ''',
                'spi_name',
                'Cisco-IOS-XR-qos-ma-bng-cfg', False),
            _MetaInfoClassMember('merge', ATTRIBUTE, 'bool', 'boolean',
                None, None,
                [], [],
                '''                TRUE for merge enabled for service-policy
                applied on dynamic template.
                ''',
                'merge',
                'Cisco-IOS-XR-qos-ma-bng-cfg', False),
            _MetaInfoClassMember('merge-id', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('0', '255')], [],
                '''                Merge ID value
                ''',
                'merge_id',
                'Cisco-IOS-XR-qos-ma-bng-cfg', False),
            _MetaInfoClassMember('account-stats', ATTRIBUTE, 'bool', 'boolean',
                None, None,
                [], [],
                '''                TRUE for account stats enabled for
                service-policy applied on dynamic template.
                Note: account stats not supported for
                subscriber type 'ppp' and 'ipsubscriber'.
                ''',
                'account_stats',
                'Cisco-IOS-XR-qos-ma-bng-cfg', False),
            ],
            'Cisco-IOS-XR-qos-ma-bng-cfg',
            'input',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-qos-ma-bng-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg',
            is_presence=True,
        ),
    },
    'DynamicTemplate.IpSubscribers.IpSubscriber.Qos.ServicePolicy.Output' : {
        'meta_info' : _MetaInfoClass('DynamicTemplate.IpSubscribers.IpSubscriber.Qos.ServicePolicy.Output', REFERENCE_CLASS,
            '''Subscriber egress policy''',
            False, 
            [
            _MetaInfoClassMember('policy-name', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                Name of policy-map
                ''',
                'policy_name',
                'Cisco-IOS-XR-qos-ma-bng-cfg', False, is_mandatory=True),
            _MetaInfoClassMember('spi-name', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                Name of the SPI
                ''',
                'spi_name',
                'Cisco-IOS-XR-qos-ma-bng-cfg', False),
            _MetaInfoClassMember('merge', ATTRIBUTE, 'bool', 'boolean',
                None, None,
                [], [],
                '''                TRUE for merge enabled for service-policy
                applied on dynamic template.
                ''',
                'merge',
                'Cisco-IOS-XR-qos-ma-bng-cfg', False),
            _MetaInfoClassMember('merge-id', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('0', '255')], [],
                '''                Merge ID value
                ''',
                'merge_id',
                'Cisco-IOS-XR-qos-ma-bng-cfg', False),
            _MetaInfoClassMember('account-stats', ATTRIBUTE, 'bool', 'boolean',
                None, None,
                [], [],
                '''                TRUE for account stats enabled for
                service-policy applied on dynamic template.
                Note: account stats not supported for
                subscriber type 'ppp' and 'ipsubscriber'.
                ''',
                'account_stats',
                'Cisco-IOS-XR-qos-ma-bng-cfg', False),
            ],
            'Cisco-IOS-XR-qos-ma-bng-cfg',
            'output',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-qos-ma-bng-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg',
            is_presence=True,
        ),
    },
    'DynamicTemplate.IpSubscribers.IpSubscriber.Qos.ServicePolicy' : {
        'meta_info' : _MetaInfoClass('DynamicTemplate.IpSubscribers.IpSubscriber.Qos.ServicePolicy', REFERENCE_CLASS,
            '''Service policy to be applied in ingress/egress
direction''',
            False, 
            [
            _MetaInfoClassMember('input', REFERENCE_CLASS, 'Input', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg', 'DynamicTemplate.IpSubscribers.IpSubscriber.Qos.ServicePolicy.Input',
                [], [],
                '''                Subscriber ingress policy
                ''',
                'input',
                'Cisco-IOS-XR-qos-ma-bng-cfg', False, is_presence=True),
            _MetaInfoClassMember('output', REFERENCE_CLASS, 'Output', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg', 'DynamicTemplate.IpSubscribers.IpSubscriber.Qos.ServicePolicy.Output',
                [], [],
                '''                Subscriber egress policy
                ''',
                'output',
                'Cisco-IOS-XR-qos-ma-bng-cfg', False, is_presence=True),
            ],
            'Cisco-IOS-XR-qos-ma-bng-cfg',
            'service-policy',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-qos-ma-bng-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg',
        ),
    },
    'DynamicTemplate.IpSubscribers.IpSubscriber.Qos.Account' : {
        'meta_info' : _MetaInfoClass('DynamicTemplate.IpSubscribers.IpSubscriber.Qos.Account', REFERENCE_CLASS,
            '''QoS L2 overhead accounting''',
            False, 
            [
            _MetaInfoClassMember('aal', REFERENCE_ENUM_CLASS, 'Qosl2DataLink', 'Qosl2-data-link',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_qos_ma_bng_cfg', 'Qosl2DataLink',
                [], [],
                '''                ATM adaptation layer AAL
                ''',
                'aal',
                'Cisco-IOS-XR-qos-ma-bng-cfg', False, has_must=True),
            _MetaInfoClassMember('encapsulation', REFERENCE_ENUM_CLASS, 'Qosl2Encap', 'Qosl2-encap',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_qos_ma_bng_cfg', 'Qosl2Encap',
                [], [],
                '''                Specify encapsulation type
                ''',
                'encapsulation',
                'Cisco-IOS-XR-qos-ma-bng-cfg', False, has_must=True),
            _MetaInfoClassMember('atm-cell-tax', ATTRIBUTE, 'Empty', 'empty',
                None, None,
                [], [],
                '''                ATM cell tax to L2 overhead
                ''',
                'atm_cell_tax',
                'Cisco-IOS-XR-qos-ma-bng-cfg', False, has_must=True),
            _MetaInfoClassMember('user-defined', ATTRIBUTE, 'int', 'int32',
                None, None,
                [('-63', '63')], [],
                '''                Numeric L2 overhead offset
                ''',
                'user_defined',
                'Cisco-IOS-XR-qos-ma-bng-cfg', False, has_must=True),
            ],
            'Cisco-IOS-XR-qos-ma-bng-cfg',
            'account',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-qos-ma-bng-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg',
        ),
    },
    'DynamicTemplate.IpSubscribers.IpSubscriber.Qos.Output' : {
        'meta_info' : _MetaInfoClass('DynamicTemplate.IpSubscribers.IpSubscriber.Qos.Output', REFERENCE_CLASS,
            '''QoS to be applied in egress direction''',
            False, 
            [
            _MetaInfoClassMember('minimum-bandwidth', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('1', '4294967295')], [],
                '''                Minimum bandwidth value for the subscriber (in
                kbps)
                ''',
                'minimum_bandwidth',
                'Cisco-IOS-XR-qos-ma-bng-cfg', False),
            ],
            'Cisco-IOS-XR-qos-ma-bng-cfg',
            'output',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-qos-ma-bng-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg',
        ),
    },
    'DynamicTemplate.IpSubscribers.IpSubscriber.Qos' : {
        'meta_info' : _MetaInfoClass('DynamicTemplate.IpSubscribers.IpSubscriber.Qos', REFERENCE_CLASS,
            '''QoS dynamically applied configuration template''',
            False, 
            [
            _MetaInfoClassMember('service-policy', REFERENCE_CLASS, 'ServicePolicy', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg', 'DynamicTemplate.IpSubscribers.IpSubscriber.Qos.ServicePolicy',
                [], [],
                '''                Service policy to be applied in ingress/egress
                direction
                ''',
                'service_policy',
                'Cisco-IOS-XR-qos-ma-bng-cfg', False),
            _MetaInfoClassMember('account', REFERENCE_CLASS, 'Account', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg', 'DynamicTemplate.IpSubscribers.IpSubscriber.Qos.Account',
                [], [],
                '''                QoS L2 overhead accounting
                ''',
                'account',
                'Cisco-IOS-XR-qos-ma-bng-cfg', False),
            _MetaInfoClassMember('output', REFERENCE_CLASS, 'Output', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg', 'DynamicTemplate.IpSubscribers.IpSubscriber.Qos.Output',
                [], [],
                '''                QoS to be applied in egress direction
                ''',
                'output',
                'Cisco-IOS-XR-qos-ma-bng-cfg', False),
            ],
            'Cisco-IOS-XR-qos-ma-bng-cfg',
            'qos',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-qos-ma-bng-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg',
        ),
    },
    'DynamicTemplate.IpSubscribers.IpSubscriber.Igmp.DefaultVrf.ExplicitTracking' : {
        'meta_info' : _MetaInfoClass('DynamicTemplate.IpSubscribers.IpSubscriber.Igmp.DefaultVrf.ExplicitTracking', REFERENCE_CLASS,
            '''IGMPv3 explicit host tracking''',
            False, 
            [
            _MetaInfoClassMember('enable', ATTRIBUTE, 'bool', 'boolean',
                None, None,
                [], [],
                '''                Enable or disable, when value is TRUE or
                FALSE respectively
                ''',
                'enable',
                'Cisco-IOS-XR-ipv4-igmp-dyn-tmpl-cfg', False, is_mandatory=True),
            _MetaInfoClassMember('access-list-name', ATTRIBUTE, 'str', 'xr:Cisco-ios-xr-string',
                None, None,
                [(1, 64)], [],
                '''                Access list specifying tracking group range
                ''',
                'access_list_name',
                'Cisco-IOS-XR-ipv4-igmp-dyn-tmpl-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-igmp-dyn-tmpl-cfg',
            'explicit-tracking',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-ipv4-igmp-dyn-tmpl-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg',
            is_presence=True,
        ),
    },
    'DynamicTemplate.IpSubscribers.IpSubscriber.Igmp.DefaultVrf' : {
        'meta_info' : _MetaInfoClass('DynamicTemplate.IpSubscribers.IpSubscriber.Igmp.DefaultVrf', REFERENCE_CLASS,
            '''Default VRF''',
            False, 
            [
            _MetaInfoClassMember('explicit-tracking', REFERENCE_CLASS, 'ExplicitTracking', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg', 'DynamicTemplate.IpSubscribers.IpSubscriber.Igmp.DefaultVrf.ExplicitTracking',
                [], [],
                '''                IGMPv3 explicit host tracking
                ''',
                'explicit_tracking',
                'Cisco-IOS-XR-ipv4-igmp-dyn-tmpl-cfg', False, is_presence=True),
            _MetaInfoClassMember('max-groups', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('1', '40000')], [],
                '''                IGMP Max Groups
                ''',
                'max_groups',
                'Cisco-IOS-XR-ipv4-igmp-dyn-tmpl-cfg', False, default_value="25000"),
            _MetaInfoClassMember('access-group', ATTRIBUTE, 'str', 'xr:Cisco-ios-xr-string',
                None, None,
                [(1, 64)], [],
                '''                Access list specifying access-list group range
                ''',
                'access_group',
                'Cisco-IOS-XR-ipv4-igmp-dyn-tmpl-cfg', False),
            _MetaInfoClassMember('version', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('1', '3')], [],
                '''                IGMP Version
                ''',
                'version',
                'Cisco-IOS-XR-ipv4-igmp-dyn-tmpl-cfg', False, default_value="3"),
            _MetaInfoClassMember('query-interval', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('1', '3600')], [],
                '''                Query interval in seconds
                ''',
                'query_interval',
                'Cisco-IOS-XR-ipv4-igmp-dyn-tmpl-cfg', False, default_value="60"),
            _MetaInfoClassMember('query-max-response-time', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('1', '25')], [],
                '''                Query response value in seconds
                ''',
                'query_max_response_time',
                'Cisco-IOS-XR-ipv4-igmp-dyn-tmpl-cfg', False, default_value="10"),
            _MetaInfoClassMember('multicast-mode', REFERENCE_ENUM_CLASS, 'DynTmplMulticastMode', 'Dyn-tmpl-multicast-mode',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_igmp_dyn_tmpl_cfg', 'DynTmplMulticastMode',
                [], [],
                '''                Configure Multicast mode variable
                ''',
                'multicast_mode',
                'Cisco-IOS-XR-ipv4-igmp-dyn-tmpl-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-igmp-dyn-tmpl-cfg',
            'default-vrf',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-ipv4-igmp-dyn-tmpl-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg',
        ),
    },
    'DynamicTemplate.IpSubscribers.IpSubscriber.Igmp' : {
        'meta_info' : _MetaInfoClass('DynamicTemplate.IpSubscribers.IpSubscriber.Igmp', REFERENCE_CLASS,
            '''IGMPconfiguration''',
            False, 
            [
            _MetaInfoClassMember('default-vrf', REFERENCE_CLASS, 'DefaultVrf', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg', 'DynamicTemplate.IpSubscribers.IpSubscriber.Igmp.DefaultVrf',
                [], [],
                '''                Default VRF
                ''',
                'default_vrf',
                'Cisco-IOS-XR-ipv4-igmp-dyn-tmpl-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-igmp-dyn-tmpl-cfg',
            'igmp',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-ipv4-igmp-dyn-tmpl-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg',
        ),
    },
    'DynamicTemplate.IpSubscribers.IpSubscriber.Ipv6Network.Addresses.AutoConfiguration' : {
        'meta_info' : _MetaInfoClass('DynamicTemplate.IpSubscribers.IpSubscriber.Ipv6Network.Addresses.AutoConfiguration', REFERENCE_CLASS,
            '''Auto IPv6 Interface Configuration''',
            False, 
            [
            _MetaInfoClassMember('enable', ATTRIBUTE, 'Empty', 'empty',
                None, None,
                [], [],
                '''                The flag to enable auto ipv6 interface
                configuration
                ''',
                'enable',
                'Cisco-IOS-XR-ipv6-ma-subscriber-cfg', False),
            ],
            'Cisco-IOS-XR-ipv6-ma-subscriber-cfg',
            'auto-configuration',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-ipv6-ma-subscriber-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg',
        ),
    },
    'DynamicTemplate.IpSubscribers.IpSubscriber.Ipv6Network.Addresses' : {
        'meta_info' : _MetaInfoClass('DynamicTemplate.IpSubscribers.IpSubscriber.Ipv6Network.Addresses', REFERENCE_CLASS,
            '''Set the IPv6 address of an interface''',
            False, 
            [
            _MetaInfoClassMember('auto-configuration', REFERENCE_CLASS, 'AutoConfiguration', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg', 'DynamicTemplate.IpSubscribers.IpSubscriber.Ipv6Network.Addresses.AutoConfiguration',
                [], [],
                '''                Auto IPv6 Interface Configuration
                ''',
                'auto_configuration',
                'Cisco-IOS-XR-ipv6-ma-subscriber-cfg', False),
            ],
            'Cisco-IOS-XR-ipv6-ma-subscriber-cfg',
            'addresses',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-ipv6-ma-subscriber-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg',
        ),
    },
    'DynamicTemplate.IpSubscribers.IpSubscriber.Ipv6Network' : {
        'meta_info' : _MetaInfoClass('DynamicTemplate.IpSubscribers.IpSubscriber.Ipv6Network', REFERENCE_CLASS,
            '''Interface IPv6 Network configuration data''',
            False, 
            [
            _MetaInfoClassMember('addresses', REFERENCE_CLASS, 'Addresses', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg', 'DynamicTemplate.IpSubscribers.IpSubscriber.Ipv6Network.Addresses',
                [], [],
                '''                Set the IPv6 address of an interface
                ''',
                'addresses',
                'Cisco-IOS-XR-ipv6-ma-subscriber-cfg', False),
            _MetaInfoClassMember('mtu', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('1280', '65535')], [],
                '''                MTU Setting of Interface
                ''',
                'mtu',
                'Cisco-IOS-XR-ipv6-ma-subscriber-cfg', False),
            _MetaInfoClassMember('rpf', ATTRIBUTE, 'bool', 'boolean',
                None, None,
                [], [],
                '''                TRUE if enabled, FALSE if disabled
                ''',
                'rpf',
                'Cisco-IOS-XR-ipv6-ma-subscriber-cfg', False),
            _MetaInfoClassMember('unreachables', ATTRIBUTE, 'Empty', 'empty',
                None, None,
                [], [],
                '''                Override Sending of ICMP Unreachable Messages
                ''',
                'unreachables',
                'Cisco-IOS-XR-ipv6-ma-subscriber-cfg', False),
            ],
            'Cisco-IOS-XR-ipv6-ma-subscriber-cfg',
            'ipv6-network',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-ipv6-ma-subscriber-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg',
        ),
    },
    'DynamicTemplate.IpSubscribers.IpSubscriber.SpanMonitorSessions.SpanMonitorSession.Attachment' : {
        'meta_info' : _MetaInfoClass('DynamicTemplate.IpSubscribers.IpSubscriber.SpanMonitorSessions.SpanMonitorSession.Attachment', REFERENCE_CLASS,
            '''Attach the interface to a Monitor Session''',
            False, 
            [
            _MetaInfoClassMember('session-name', ATTRIBUTE, 'str', 'dt1:Span-session-name',
                None, None,
                [(1, 79)], [],
                '''                Session Name
                ''',
                'session_name',
                'Cisco-IOS-XR-Ethernet-SPAN-subscriber-cfg', False, is_mandatory=True),
            _MetaInfoClassMember('direction', REFERENCE_ENUM_CLASS, 'SpanTrafficDirection', 'Span-traffic-direction',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_Ethernet_SPAN_subscriber_cfg', 'SpanTrafficDirection',
                [], [],
                '''                Specify the direction of traffic to replicate
                (optional)
                ''',
                'direction',
                'Cisco-IOS-XR-Ethernet-SPAN-subscriber-cfg', False),
            _MetaInfoClassMember('port-level-enable', ATTRIBUTE, 'Empty', 'empty',
                None, None,
                [], [],
                '''                Enable port level traffic mirroring
                ''',
                'port_level_enable',
                'Cisco-IOS-XR-Ethernet-SPAN-subscriber-cfg', False),
            ],
            'Cisco-IOS-XR-Ethernet-SPAN-subscriber-cfg',
            'attachment',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-Ethernet-SPAN-subscriber-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg',
            is_presence=True,
        ),
    },
    'DynamicTemplate.IpSubscribers.IpSubscriber.SpanMonitorSessions.SpanMonitorSession.Acl' : {
        'meta_info' : _MetaInfoClass('DynamicTemplate.IpSubscribers.IpSubscriber.SpanMonitorSessions.SpanMonitorSession.Acl', REFERENCE_CLASS,
            '''Enable ACL matching for traffic mirroring''',
            False, 
            [
            _MetaInfoClassMember('acl-enable', ATTRIBUTE, 'Empty', 'empty',
                None, None,
                [], [],
                '''                Enable ACL
                ''',
                'acl_enable',
                'Cisco-IOS-XR-Ethernet-SPAN-subscriber-cfg', False, is_mandatory=True),
            _MetaInfoClassMember('acl-name', ATTRIBUTE, 'str', 'dt1:Span-acl-name',
                None, None,
                [(1, 80)], [],
                '''                ACL Name
                ''',
                'acl_name',
                'Cisco-IOS-XR-Ethernet-SPAN-subscriber-cfg', False),
            ],
            'Cisco-IOS-XR-Ethernet-SPAN-subscriber-cfg',
            'acl',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-Ethernet-SPAN-subscriber-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg',
            is_presence=True,
        ),
    },
    'DynamicTemplate.IpSubscribers.IpSubscriber.SpanMonitorSessions.SpanMonitorSession' : {
        'meta_info' : _MetaInfoClass('DynamicTemplate.IpSubscribers.IpSubscriber.SpanMonitorSessions.SpanMonitorSession', REFERENCE_LIST,
            '''Configuration for a particular class of Monitor
Session''',
            False, 
            [
            _MetaInfoClassMember('session-class', REFERENCE_ENUM_CLASS, 'SpanSessionClass', 'dt1:Span-session-class',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_Ethernet_SPAN_datatypes', 'SpanSessionClass',
                [], [],
                '''                Session Class
                ''',
                'session_class',
                'Cisco-IOS-XR-Ethernet-SPAN-subscriber-cfg', True),
            _MetaInfoClassMember('mirror-first', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('1', '10000')], [],
                '''                Mirror a specified number of bytes from start of
                packet
                ''',
                'mirror_first',
                'Cisco-IOS-XR-Ethernet-SPAN-subscriber-cfg', False),
            _MetaInfoClassMember('attachment', REFERENCE_CLASS, 'Attachment', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg', 'DynamicTemplate.IpSubscribers.IpSubscriber.SpanMonitorSessions.SpanMonitorSession.Attachment',
                [], [],
                '''                Attach the interface to a Monitor Session
                ''',
                'attachment',
                'Cisco-IOS-XR-Ethernet-SPAN-subscriber-cfg', False, is_presence=True),
            _MetaInfoClassMember('mirror-interval', REFERENCE_ENUM_CLASS, 'SpanMirrorInterval', 'Span-mirror-interval',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_Ethernet_SPAN_subscriber_cfg', 'SpanMirrorInterval',
                [], [],
                '''                Specify the mirror interval
                ''',
                'mirror_interval',
                'Cisco-IOS-XR-Ethernet-SPAN-subscriber-cfg', False),
            _MetaInfoClassMember('acl', REFERENCE_CLASS, 'Acl', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg', 'DynamicTemplate.IpSubscribers.IpSubscriber.SpanMonitorSessions.SpanMonitorSession.Acl',
                [], [],
                '''                Enable ACL matching for traffic mirroring
                ''',
                'acl',
                'Cisco-IOS-XR-Ethernet-SPAN-subscriber-cfg', False, is_presence=True),
            ],
            'Cisco-IOS-XR-Ethernet-SPAN-subscriber-cfg',
            'span-monitor-session',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-Ethernet-SPAN-subscriber-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg',
        ),
    },
    'DynamicTemplate.IpSubscribers.IpSubscriber.SpanMonitorSessions' : {
        'meta_info' : _MetaInfoClass('DynamicTemplate.IpSubscribers.IpSubscriber.SpanMonitorSessions', REFERENCE_CLASS,
            '''Monitor Session container for this template''',
            False, 
            [
            _MetaInfoClassMember('span-monitor-session', REFERENCE_LIST, 'SpanMonitorSession', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg', 'DynamicTemplate.IpSubscribers.IpSubscriber.SpanMonitorSessions.SpanMonitorSession',
                [], [],
                '''                Configuration for a particular class of Monitor
                Session
                ''',
                'span_monitor_session',
                'Cisco-IOS-XR-Ethernet-SPAN-subscriber-cfg', False),
            ],
            'Cisco-IOS-XR-Ethernet-SPAN-subscriber-cfg',
            'span-monitor-sessions',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-Ethernet-SPAN-subscriber-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg',
        ),
    },
    'DynamicTemplate.IpSubscribers.IpSubscriber.Ipv6Neighbor.RaInterval' : {
        'meta_info' : _MetaInfoClass('DynamicTemplate.IpSubscribers.IpSubscriber.Ipv6Neighbor.RaInterval', REFERENCE_CLASS,
            '''Set IPv6 Router Advertisement (RA) interval in
seconds''',
            False, 
            [
            _MetaInfoClassMember('maximum', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('4', '1800')], [],
                '''                Maximum RA interval in seconds
                ''',
                'maximum',
                'Cisco-IOS-XR-ipv6-nd-subscriber-cfg', False, is_mandatory=True),
            _MetaInfoClassMember('minimum', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('3', '1800')], [],
                '''                Minimum RA interval in seconds. Must be less
                than 0.75 * maximum interval
                ''',
                'minimum',
                'Cisco-IOS-XR-ipv6-nd-subscriber-cfg', False),
            ],
            'Cisco-IOS-XR-ipv6-nd-subscriber-cfg',
            'ra-interval',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-ipv6-nd-subscriber-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg',
            is_presence=True,
        ),
    },
    'DynamicTemplate.IpSubscribers.IpSubscriber.Ipv6Neighbor.FramedPrefix' : {
        'meta_info' : _MetaInfoClass('DynamicTemplate.IpSubscribers.IpSubscriber.Ipv6Neighbor.FramedPrefix', REFERENCE_CLASS,
            '''Set the IPv6 framed ipv6 prefix for a
subscriber interface ''',
            False, 
            [
            _MetaInfoClassMember('prefix-length', ATTRIBUTE, 'int', 'xr:Ipv6-prefix-length',
                None, None,
                [('0', '128')], [],
                '''                IPv6 framed prefix length
                ''',
                'prefix_length',
                'Cisco-IOS-XR-ipv6-nd-subscriber-cfg', False, is_mandatory=True),
            _MetaInfoClassMember('prefix', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                IPV6 framed prefix address
                ''',
                'prefix',
                'Cisco-IOS-XR-ipv6-nd-subscriber-cfg', False, is_mandatory=True),
            ],
            'Cisco-IOS-XR-ipv6-nd-subscriber-cfg',
            'framed-prefix',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-ipv6-nd-subscriber-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg',
            is_presence=True,
        ),
    },
    'DynamicTemplate.IpSubscribers.IpSubscriber.Ipv6Neighbor.DuplicateAddressDetection' : {
        'meta_info' : _MetaInfoClass('DynamicTemplate.IpSubscribers.IpSubscriber.Ipv6Neighbor.DuplicateAddressDetection', REFERENCE_CLASS,
            '''Duplicate Address Detection (DAD)''',
            False, 
            [
            _MetaInfoClassMember('attempts', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('0', '600')], [],
                '''                Set IPv6 duplicate address detection transmits
                ''',
                'attempts',
                'Cisco-IOS-XR-ipv6-nd-subscriber-cfg', False),
            ],
            'Cisco-IOS-XR-ipv6-nd-subscriber-cfg',
            'duplicate-address-detection',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-ipv6-nd-subscriber-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg',
        ),
    },
    'DynamicTemplate.IpSubscribers.IpSubscriber.Ipv6Neighbor.RaInitial' : {
        'meta_info' : _MetaInfoClass('DynamicTemplate.IpSubscribers.IpSubscriber.Ipv6Neighbor.RaInitial', REFERENCE_CLASS,
            '''IPv6 ND RA Initial''',
            False, 
            [
            _MetaInfoClassMember('count', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('0', '32')], [],
                '''                Initial RA count
                ''',
                'count',
                'Cisco-IOS-XR-ipv6-nd-subscriber-cfg', False, is_mandatory=True),
            _MetaInfoClassMember('interval', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('4', '1800')], [],
                '''                Initial RA interval in seconds
                ''',
                'interval',
                'Cisco-IOS-XR-ipv6-nd-subscriber-cfg', False, is_mandatory=True),
            ],
            'Cisco-IOS-XR-ipv6-nd-subscriber-cfg',
            'ra-initial',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-ipv6-nd-subscriber-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg',
            is_presence=True,
        ),
    },
    'DynamicTemplate.IpSubscribers.IpSubscriber.Ipv6Neighbor' : {
        'meta_info' : _MetaInfoClass('DynamicTemplate.IpSubscribers.IpSubscriber.Ipv6Neighbor', REFERENCE_CLASS,
            '''Interface IPv6 Network configuration data''',
            False, 
            [
            _MetaInfoClassMember('ra-interval', REFERENCE_CLASS, 'RaInterval', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg', 'DynamicTemplate.IpSubscribers.IpSubscriber.Ipv6Neighbor.RaInterval',
                [], [],
                '''                Set IPv6 Router Advertisement (RA) interval in
                seconds
                ''',
                'ra_interval',
                'Cisco-IOS-XR-ipv6-nd-subscriber-cfg', False, is_presence=True),
            _MetaInfoClassMember('framed-prefix', REFERENCE_CLASS, 'FramedPrefix', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg', 'DynamicTemplate.IpSubscribers.IpSubscriber.Ipv6Neighbor.FramedPrefix',
                [], [],
                '''                Set the IPv6 framed ipv6 prefix for a
                subscriber interface 
                ''',
                'framed_prefix',
                'Cisco-IOS-XR-ipv6-nd-subscriber-cfg', False, is_presence=True),
            _MetaInfoClassMember('duplicate-address-detection', REFERENCE_CLASS, 'DuplicateAddressDetection', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg', 'DynamicTemplate.IpSubscribers.IpSubscriber.Ipv6Neighbor.DuplicateAddressDetection',
                [], [],
                '''                Duplicate Address Detection (DAD)
                ''',
                'duplicate_address_detection',
                'Cisco-IOS-XR-ipv6-nd-subscriber-cfg', False),
            _MetaInfoClassMember('ra-initial', REFERENCE_CLASS, 'RaInitial', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg', 'DynamicTemplate.IpSubscribers.IpSubscriber.Ipv6Neighbor.RaInitial',
                [], [],
                '''                IPv6 ND RA Initial
                ''',
                'ra_initial',
                'Cisco-IOS-XR-ipv6-nd-subscriber-cfg', False, is_presence=True),
            _MetaInfoClassMember('framed-prefix-pool', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                Set the IPv6 framed ipv6 prefix pool for a
                subscriber interface 
                ''',
                'framed_prefix_pool',
                'Cisco-IOS-XR-ipv6-nd-subscriber-cfg', False),
            _MetaInfoClassMember('managed-config', ATTRIBUTE, 'Empty', 'empty',
                None, None,
                [], [],
                '''                Host to use stateful protocol for address
                configuration
                ''',
                'managed_config',
                'Cisco-IOS-XR-ipv6-nd-subscriber-cfg', False),
            _MetaInfoClassMember('other-config', ATTRIBUTE, 'Empty', 'empty',
                None, None,
                [], [],
                '''                Host to use stateful protocol for non-address
                configuration
                ''',
                'other_config',
                'Cisco-IOS-XR-ipv6-nd-subscriber-cfg', False),
            _MetaInfoClassMember('start-ra-on-ipv6-enable', ATTRIBUTE, 'Empty', 'empty',
                None, None,
                [], [],
                '''                Start RA on ipv6-enable config
                ''',
                'start_ra_on_ipv6_enable',
                'Cisco-IOS-XR-ipv6-nd-subscriber-cfg', False),
            _MetaInfoClassMember('nud-enable', ATTRIBUTE, 'Empty', 'empty',
                None, None,
                [], [],
                '''                NUD enable
                ''',
                'nud_enable',
                'Cisco-IOS-XR-ipv6-nd-subscriber-cfg', False),
            _MetaInfoClassMember('ra-lifetime', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('0', '9000')], [],
                '''                Set IPv6 Router Advertisement (RA) lifetime in
                seconds
                ''',
                'ra_lifetime',
                'Cisco-IOS-XR-ipv6-nd-subscriber-cfg', False),
            _MetaInfoClassMember('router-preference', REFERENCE_ENUM_CLASS, 'Ipv6NdRouterPrefTemplate', 'Ipv6-nd-router-pref-template',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_nd_subscriber_cfg', 'Ipv6NdRouterPrefTemplate',
                [], [],
                '''                RA Router Preference
                ''',
                'router_preference',
                'Cisco-IOS-XR-ipv6-nd-subscriber-cfg', False),
            _MetaInfoClassMember('ra-suppress', ATTRIBUTE, 'Empty', 'empty',
                None, None,
                [], [],
                '''                Enable suppress IPv6 router advertisement
                ''',
                'ra_suppress',
                'Cisco-IOS-XR-ipv6-nd-subscriber-cfg', False),
            _MetaInfoClassMember('ra-unicast', ATTRIBUTE, 'Empty', 'empty',
                None, None,
                [], [],
                '''                Enable RA unicast Flag
                ''',
                'ra_unicast',
                'Cisco-IOS-XR-ipv6-nd-subscriber-cfg', False),
            _MetaInfoClassMember('ra-unspecify-hoplimit', ATTRIBUTE, 'Empty', 'empty',
                None, None,
                [], [],
                '''                Unspecify IPv6 Router Advertisement (RA)
                hop-limit
                ''',
                'ra_unspecify_hoplimit',
                'Cisco-IOS-XR-ipv6-nd-subscriber-cfg', False),
            _MetaInfoClassMember('ra-suppress-mtu', ATTRIBUTE, 'Empty', 'empty',
                None, None,
                [], [],
                '''                RA suppress MTU flag
                ''',
                'ra_suppress_mtu',
                'Cisco-IOS-XR-ipv6-nd-subscriber-cfg', False),
            _MetaInfoClassMember('suppress-cache-learning', ATTRIBUTE, 'Empty', 'empty',
                None, None,
                [], [],
                '''                Suppress cache learning flag
                ''',
                'suppress_cache_learning',
                'Cisco-IOS-XR-ipv6-nd-subscriber-cfg', False),
            _MetaInfoClassMember('reachable-time', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('0', '3600000')], [],
                '''                Set advertised reachability time in
                milliseconds
                ''',
                'reachable_time',
                'Cisco-IOS-XR-ipv6-nd-subscriber-cfg', False),
            _MetaInfoClassMember('ns-interval', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('1000', '4294967295')], [],
                '''                Set advertised NS retransmission interval in
                milliseconds
                ''',
                'ns_interval',
                'Cisco-IOS-XR-ipv6-nd-subscriber-cfg', False),
            ],
            'Cisco-IOS-XR-ipv6-nd-subscriber-cfg',
            'ipv6-neighbor',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-ipv6-nd-subscriber-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg',
        ),
    },
    'DynamicTemplate.IpSubscribers.IpSubscriber.Pbr.ServicePolicies.ServicePolicy' : {
        'meta_info' : _MetaInfoClass('DynamicTemplate.IpSubscribers.IpSubscriber.Pbr.ServicePolicies.ServicePolicy', REFERENCE_LIST,
            '''Service policy details''',
            False, 
            [
            _MetaInfoClassMember('service-policy', ATTRIBUTE, 'str', 'string',
                None, None,
                [(1, 64)], [],
                '''                Name of policy-map
                ''',
                'service_policy',
                'Cisco-IOS-XR-pbr-subscriber-cfg', True),
            ],
            'Cisco-IOS-XR-pbr-subscriber-cfg',
            'service-policy',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-pbr-subscriber-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg',
        ),
    },
    'DynamicTemplate.IpSubscribers.IpSubscriber.Pbr.ServicePolicies' : {
        'meta_info' : _MetaInfoClass('DynamicTemplate.IpSubscribers.IpSubscriber.Pbr.ServicePolicies', REFERENCE_CLASS,
            '''Ingress service policy''',
            False, 
            [
            _MetaInfoClassMember('service-policy', REFERENCE_LIST, 'ServicePolicy', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg', 'DynamicTemplate.IpSubscribers.IpSubscriber.Pbr.ServicePolicies.ServicePolicy',
                [], [],
                '''                Service policy details
                ''',
                'service_policy',
                'Cisco-IOS-XR-pbr-subscriber-cfg', False),
            ],
            'Cisco-IOS-XR-pbr-subscriber-cfg',
            'service-policies',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-pbr-subscriber-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg',
        ),
    },
    'DynamicTemplate.IpSubscribers.IpSubscriber.Pbr' : {
        'meta_info' : _MetaInfoClass('DynamicTemplate.IpSubscribers.IpSubscriber.Pbr', REFERENCE_CLASS,
            '''Dynamic Template PBR configuration''',
            False, 
            [
            _MetaInfoClassMember('service-policies', REFERENCE_CLASS, 'ServicePolicies', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg', 'DynamicTemplate.IpSubscribers.IpSubscriber.Pbr.ServicePolicies',
                [], [],
                '''                Ingress service policy
                ''',
                'service_policies',
                'Cisco-IOS-XR-pbr-subscriber-cfg', False),
            _MetaInfoClassMember('service-policy-in', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                Class for subscriber ingress policy
                ''',
                'service_policy_in',
                'Cisco-IOS-XR-pbr-subscriber-cfg', False),
            ],
            'Cisco-IOS-XR-pbr-subscriber-cfg',
            'pbr',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-pbr-subscriber-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg',
        ),
    },
    'DynamicTemplate.IpSubscribers.IpSubscriber.Ipv4PacketFilter.Outbound' : {
        'meta_info' : _MetaInfoClass('DynamicTemplate.IpSubscribers.IpSubscriber.Ipv4PacketFilter.Outbound', REFERENCE_CLASS,
            '''IPv4 Packet filter to be applied to outbound
packets''',
            False, 
            [
            _MetaInfoClassMember('common-acl-name', ATTRIBUTE, 'str', 'xr:Cisco-ios-xr-string',
                None, None,
                [(1, 64)], [],
                '''                Not supported (Leave unspecified).
                ''',
                'common_acl_name',
                'Cisco-IOS-XR-ip-pfilter-subscriber-cfg', False),
            _MetaInfoClassMember('name', ATTRIBUTE, 'str', 'xr:Cisco-ios-xr-string',
                None, None,
                [(1, 64)], [],
                '''                IPv4 Packet Filter Name to be applied to
                Outbound packets.
                ''',
                'name',
                'Cisco-IOS-XR-ip-pfilter-subscriber-cfg', False),
            _MetaInfoClassMember('hardware-count', ATTRIBUTE, 'Empty', 'empty',
                None, None,
                [], [],
                '''                Not supported (Leave unspecified).
                ''',
                'hardware_count',
                'Cisco-IOS-XR-ip-pfilter-subscriber-cfg', False),
            _MetaInfoClassMember('interface-statistics', ATTRIBUTE, 'Empty', 'empty',
                None, None,
                [], [],
                '''                Not supported (Leave unspecified).
                ''',
                'interface_statistics',
                'Cisco-IOS-XR-ip-pfilter-subscriber-cfg', False),
            ],
            'Cisco-IOS-XR-ip-pfilter-subscriber-cfg',
            'outbound',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-ip-pfilter-subscriber-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg',
        ),
    },
    'DynamicTemplate.IpSubscribers.IpSubscriber.Ipv4PacketFilter.Inbound' : {
        'meta_info' : _MetaInfoClass('DynamicTemplate.IpSubscribers.IpSubscriber.Ipv4PacketFilter.Inbound', REFERENCE_CLASS,
            '''IPv4 Packet filter to be applied to inbound
packets''',
            False, 
            [
            _MetaInfoClassMember('common-acl-name', ATTRIBUTE, 'str', 'xr:Cisco-ios-xr-string',
                None, None,
                [(1, 64)], [],
                '''                Not supported (Leave unspecified).
                ''',
                'common_acl_name',
                'Cisco-IOS-XR-ip-pfilter-subscriber-cfg', False),
            _MetaInfoClassMember('name', ATTRIBUTE, 'str', 'xr:Cisco-ios-xr-string',
                None, None,
                [(1, 64)], [],
                '''                IPv4 Packet Filter Name to be applied to
                Inbound packets NOTE: This parameter is
                mandatory if 'CommonACLName' is not specified.
                ''',
                'name',
                'Cisco-IOS-XR-ip-pfilter-subscriber-cfg', False),
            _MetaInfoClassMember('hardware-count', ATTRIBUTE, 'Empty', 'empty',
                None, None,
                [], [],
                '''                Not supported (Leave unspecified).
                ''',
                'hardware_count',
                'Cisco-IOS-XR-ip-pfilter-subscriber-cfg', False),
            _MetaInfoClassMember('interface-statistics', ATTRIBUTE, 'Empty', 'empty',
                None, None,
                [], [],
                '''                Not supported (Leave unspecified).
                ''',
                'interface_statistics',
                'Cisco-IOS-XR-ip-pfilter-subscriber-cfg', False),
            ],
            'Cisco-IOS-XR-ip-pfilter-subscriber-cfg',
            'inbound',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-ip-pfilter-subscriber-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg',
        ),
    },
    'DynamicTemplate.IpSubscribers.IpSubscriber.Ipv4PacketFilter' : {
        'meta_info' : _MetaInfoClass('DynamicTemplate.IpSubscribers.IpSubscriber.Ipv4PacketFilter', REFERENCE_CLASS,
            '''IPv4 Packet Filtering configuration for the
template''',
            False, 
            [
            _MetaInfoClassMember('outbound', REFERENCE_CLASS, 'Outbound', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg', 'DynamicTemplate.IpSubscribers.IpSubscriber.Ipv4PacketFilter.Outbound',
                [], [],
                '''                IPv4 Packet filter to be applied to outbound
                packets
                ''',
                'outbound',
                'Cisco-IOS-XR-ip-pfilter-subscriber-cfg', False),
            _MetaInfoClassMember('inbound', REFERENCE_CLASS, 'Inbound', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg', 'DynamicTemplate.IpSubscribers.IpSubscriber.Ipv4PacketFilter.Inbound',
                [], [],
                '''                IPv4 Packet filter to be applied to inbound
                packets
                ''',
                'inbound',
                'Cisco-IOS-XR-ip-pfilter-subscriber-cfg', False),
            ],
            'Cisco-IOS-XR-ip-pfilter-subscriber-cfg',
            'ipv4-packet-filter',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-ip-pfilter-subscriber-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg',
        ),
    },
    'DynamicTemplate.IpSubscribers.IpSubscriber.Ipv6PacketFilter.Inbound' : {
        'meta_info' : _MetaInfoClass('DynamicTemplate.IpSubscribers.IpSubscriber.Ipv6PacketFilter.Inbound', REFERENCE_CLASS,
            '''IPv6 Packet filter to be applied to inbound
packets''',
            False, 
            [
            _MetaInfoClassMember('common-acl-name', ATTRIBUTE, 'str', 'xr:Cisco-ios-xr-string',
                None, None,
                [(1, 64)], [],
                '''                Not supported (Leave unspecified).
                ''',
                'common_acl_name',
                'Cisco-IOS-XR-ip-pfilter-subscriber-cfg', False),
            _MetaInfoClassMember('name', ATTRIBUTE, 'str', 'xr:Cisco-ios-xr-string',
                None, None,
                [(1, 64)], [],
                '''                IPv6 Packet Filter Name to be applied to
                Inbound  NOTE: This parameter is mandatory if
                'CommonACLName' is not specified.
                ''',
                'name',
                'Cisco-IOS-XR-ip-pfilter-subscriber-cfg', False),
            _MetaInfoClassMember('interface-statistics', ATTRIBUTE, 'Empty', 'empty',
                None, None,
                [], [],
                '''                Not supported (Leave unspecified).
                ''',
                'interface_statistics',
                'Cisco-IOS-XR-ip-pfilter-subscriber-cfg', False),
            ],
            'Cisco-IOS-XR-ip-pfilter-subscriber-cfg',
            'inbound',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-ip-pfilter-subscriber-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg',
        ),
    },
    'DynamicTemplate.IpSubscribers.IpSubscriber.Ipv6PacketFilter.Outbound' : {
        'meta_info' : _MetaInfoClass('DynamicTemplate.IpSubscribers.IpSubscriber.Ipv6PacketFilter.Outbound', REFERENCE_CLASS,
            '''IPv6 Packet filter to be applied to outbound
packets''',
            False, 
            [
            _MetaInfoClassMember('common-acl-name', ATTRIBUTE, 'str', 'xr:Cisco-ios-xr-string',
                None, None,
                [(1, 64)], [],
                '''                Not supported (Leave unspecified).
                ''',
                'common_acl_name',
                'Cisco-IOS-XR-ip-pfilter-subscriber-cfg', False),
            _MetaInfoClassMember('name', ATTRIBUTE, 'str', 'xr:Cisco-ios-xr-string',
                None, None,
                [(1, 64)], [],
                '''                IPv6 Packet Filter Name to be applied to
                Outbound packets.
                ''',
                'name',
                'Cisco-IOS-XR-ip-pfilter-subscriber-cfg', False),
            _MetaInfoClassMember('interface-statistics', ATTRIBUTE, 'Empty', 'empty',
                None, None,
                [], [],
                '''                Not supported (Leave unspecified).
                ''',
                'interface_statistics',
                'Cisco-IOS-XR-ip-pfilter-subscriber-cfg', False),
            ],
            'Cisco-IOS-XR-ip-pfilter-subscriber-cfg',
            'outbound',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-ip-pfilter-subscriber-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg',
        ),
    },
    'DynamicTemplate.IpSubscribers.IpSubscriber.Ipv6PacketFilter' : {
        'meta_info' : _MetaInfoClass('DynamicTemplate.IpSubscribers.IpSubscriber.Ipv6PacketFilter', REFERENCE_CLASS,
            '''IPv6 Packet Filtering configuration for the
interface''',
            False, 
            [
            _MetaInfoClassMember('inbound', REFERENCE_CLASS, 'Inbound', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg', 'DynamicTemplate.IpSubscribers.IpSubscriber.Ipv6PacketFilter.Inbound',
                [], [],
                '''                IPv6 Packet filter to be applied to inbound
                packets
                ''',
                'inbound',
                'Cisco-IOS-XR-ip-pfilter-subscriber-cfg', False),
            _MetaInfoClassMember('outbound', REFERENCE_CLASS, 'Outbound', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg', 'DynamicTemplate.IpSubscribers.IpSubscriber.Ipv6PacketFilter.Outbound',
                [], [],
                '''                IPv6 Packet filter to be applied to outbound
                packets
                ''',
                'outbound',
                'Cisco-IOS-XR-ip-pfilter-subscriber-cfg', False),
            ],
            'Cisco-IOS-XR-ip-pfilter-subscriber-cfg',
            'ipv6-packet-filter',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-ip-pfilter-subscriber-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg',
        ),
    },
    'DynamicTemplate.IpSubscribers.IpSubscriber.Dhcpd' : {
        'meta_info' : _MetaInfoClass('DynamicTemplate.IpSubscribers.IpSubscriber.Dhcpd', REFERENCE_CLASS,
            '''Interface dhcpv4 configuration data''',
            False, 
            [
            _MetaInfoClassMember('dhcpv4-iplease', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                Cisco VSA to configure any dhcp4 ip lease per
                subscriber
                ''',
                'dhcpv4_iplease',
                'Cisco-IOS-XR-ipv4-dhcpd-subscriber-cfg', False),
            _MetaInfoClassMember('class', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                The class to be used for proxy/server profile
                ''',
                'class_',
                'Cisco-IOS-XR-ipv4-dhcpd-subscriber-cfg', False),
            _MetaInfoClassMember('mode-class', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                Select proxy/server profile based on mode class
                name
                ''',
                'mode_class',
                'Cisco-IOS-XR-ipv4-dhcpd-subscriber-cfg', False),
            _MetaInfoClassMember('default-gateway', ATTRIBUTE, 'str', 'inet:ipv4-address-no-zone',
                None, None,
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'],
                '''                The Default Gateway IP address
                ''',
                'default_gateway',
                'Cisco-IOS-XR-ipv4-dhcpd-subscriber-cfg', False),
            _MetaInfoClassMember('session-limit', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('0', '4294967295')], [],
                '''                The pool to be used for Prefix Delegation
                ''',
                'session_limit',
                'Cisco-IOS-XR-ipv4-dhcpd-subscriber-cfg', False),
            _MetaInfoClassMember('dhcpv4-option', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                Cisco VSA to configure any dhcp4 option per
                subscriber
                ''',
                'dhcpv4_option',
                'Cisco-IOS-XR-ipv4-dhcpd-subscriber-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-dhcpd-subscriber-cfg',
            'dhcpd',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-ipv4-dhcpd-subscriber-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg',
        ),
    },
    'DynamicTemplate.IpSubscribers.IpSubscriber.Dhcpv6.DelegatedPrefix' : {
        'meta_info' : _MetaInfoClass('DynamicTemplate.IpSubscribers.IpSubscriber.Dhcpv6.DelegatedPrefix', REFERENCE_CLASS,
            '''The prefix to be used for Prefix Delegation''',
            False, 
            [
            _MetaInfoClassMember('prefix', ATTRIBUTE, 'str', 'inet:ipv6-address-no-zone',
                None, None,
                [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'],
                '''                IPv6 Prefix
                ''',
                'prefix',
                'Cisco-IOS-XR-ipv6-new-dhcpv6d-subscriber-cfg', False, is_mandatory=True),
            _MetaInfoClassMember('prefix-length', ATTRIBUTE, 'int', 'xr:Ipv6-prefix-length',
                None, None,
                [('0', '128')], [],
                '''                PD Prefix Length
                ''',
                'prefix_length',
                'Cisco-IOS-XR-ipv6-new-dhcpv6d-subscriber-cfg', False, is_mandatory=True),
            ],
            'Cisco-IOS-XR-ipv6-new-dhcpv6d-subscriber-cfg',
            'delegated-prefix',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-ipv6-new-dhcpv6d-subscriber-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg',
            is_presence=True,
        ),
    },
    'DynamicTemplate.IpSubscribers.IpSubscriber.Dhcpv6' : {
        'meta_info' : _MetaInfoClass('DynamicTemplate.IpSubscribers.IpSubscriber.Dhcpv6', REFERENCE_CLASS,
            '''Interface dhcpv6 configuration data''',
            False, 
            [
            _MetaInfoClassMember('delegated-prefix', REFERENCE_CLASS, 'DelegatedPrefix', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg', 'DynamicTemplate.IpSubscribers.IpSubscriber.Dhcpv6.DelegatedPrefix',
                [], [],
                '''                The prefix to be used for Prefix Delegation
                ''',
                'delegated_prefix',
                'Cisco-IOS-XR-ipv6-new-dhcpv6d-subscriber-cfg', False, is_presence=True),
            _MetaInfoClassMember('dns-ipv6address', ATTRIBUTE, 'str', 'inet:ipv6-address-no-zone',
                None, None,
                [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'],
                '''                Dns IPv6 Address
                ''',
                'dns_ipv6address',
                'Cisco-IOS-XR-ipv6-new-dhcpv6d-subscriber-cfg', False),
            _MetaInfoClassMember('mode-class', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                Select proxy/server profile based on mode class
                name
                ''',
                'mode_class',
                'Cisco-IOS-XR-ipv6-new-dhcpv6d-subscriber-cfg', False),
            _MetaInfoClassMember('dhcpv6-iplease', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                Cisco VSA to configure any dhcpv6 ip lease per
                subscriber
                ''',
                'dhcpv6_iplease',
                'Cisco-IOS-XR-ipv6-new-dhcpv6d-subscriber-cfg', False),
            _MetaInfoClassMember('dhcpv6-option', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                Cisco VSA to configure any dhcpv6 option per
                subscriber
                ''',
                'dhcpv6_option',
                'Cisco-IOS-XR-ipv6-new-dhcpv6d-subscriber-cfg', False),
            _MetaInfoClassMember('address-pool', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                The pool to be used for Address assignment
                ''',
                'address_pool',
                'Cisco-IOS-XR-ipv6-new-dhcpv6d-subscriber-cfg', False),
            _MetaInfoClassMember('delegated-prefix-pool', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                The pool to be used for Prefix Delegation
                ''',
                'delegated_prefix_pool',
                'Cisco-IOS-XR-ipv6-new-dhcpv6d-subscriber-cfg', False),
            _MetaInfoClassMember('class', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                The class to be used for proxy/server profile
                ''',
                'class_',
                'Cisco-IOS-XR-ipv6-new-dhcpv6d-subscriber-cfg', False),
            _MetaInfoClassMember('stateful-address', ATTRIBUTE, 'str', 'inet:ipv6-address-no-zone',
                None, None,
                [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'],
                '''                Stateful IPv6 Address
                ''',
                'stateful_address',
                'Cisco-IOS-XR-ipv6-new-dhcpv6d-subscriber-cfg', False),
            ],
            'Cisco-IOS-XR-ipv6-new-dhcpv6d-subscriber-cfg',
            'dhcpv6',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-ipv6-new-dhcpv6d-subscriber-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg',
        ),
    },
    'DynamicTemplate.IpSubscribers.IpSubscriber' : {
        'meta_info' : _MetaInfoClass('DynamicTemplate.IpSubscribers.IpSubscriber', REFERENCE_LIST,
            '''A IP Subscriber Type Template ''',
            False, 
            [
            _MetaInfoClassMember('template-name', ATTRIBUTE, 'str', 'xr:Cisco-ios-xr-string',
                None, None,
                [], [b'[\\w\\-\\.:,_@#%$\\+=\\|;]+'],
                '''                The name of the template
                ''',
                'template_name',
                'Cisco-IOS-XR-subscriber-infra-tmplmgr-cfg', True),
            _MetaInfoClassMember('ipv4-network', REFERENCE_CLASS, 'Ipv4Network', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg', 'DynamicTemplate.IpSubscribers.IpSubscriber.Ipv4Network',
                [], [],
                '''                Interface IPv4 Network configuration data
                ''',
                'ipv4_network',
                'Cisco-IOS-XR-ipv4-ma-subscriber-cfg', False),
            _MetaInfoClassMember('accounting', REFERENCE_CLASS, 'Accounting', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg', 'DynamicTemplate.IpSubscribers.IpSubscriber.Accounting',
                [], [],
                '''                Subscriber accounting dynamic-template commands
                ''',
                'accounting',
                'Cisco-IOS-XR-subscriber-accounting-cfg', False),
            _MetaInfoClassMember('qos', REFERENCE_CLASS, 'Qos', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg', 'DynamicTemplate.IpSubscribers.IpSubscriber.Qos',
                [], [],
                '''                QoS dynamically applied configuration template
                ''',
                'qos',
                'Cisco-IOS-XR-qos-ma-bng-cfg', False),
            _MetaInfoClassMember('igmp', REFERENCE_CLASS, 'Igmp', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg', 'DynamicTemplate.IpSubscribers.IpSubscriber.Igmp',
                [], [],
                '''                IGMPconfiguration
                ''',
                'igmp',
                'Cisco-IOS-XR-ipv4-igmp-dyn-tmpl-cfg', False),
            _MetaInfoClassMember('ipv6-network', REFERENCE_CLASS, 'Ipv6Network', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg', 'DynamicTemplate.IpSubscribers.IpSubscriber.Ipv6Network',
                [], [],
                '''                Interface IPv6 Network configuration data
                ''',
                'ipv6_network',
                'Cisco-IOS-XR-ipv6-ma-subscriber-cfg', False),
            _MetaInfoClassMember('span-monitor-sessions', REFERENCE_CLASS, 'SpanMonitorSessions', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg', 'DynamicTemplate.IpSubscribers.IpSubscriber.SpanMonitorSessions',
                [], [],
                '''                Monitor Session container for this template
                ''',
                'span_monitor_sessions',
                'Cisco-IOS-XR-Ethernet-SPAN-subscriber-cfg', False),
            _MetaInfoClassMember('vrf', ATTRIBUTE, 'str', 'xr:Cisco-ios-xr-string',
                None, None,
                [(1, 32)], [],
                '''                Assign the interface to a VRF 
                ''',
                'vrf',
                'Cisco-IOS-XR-infra-rsi-subscriber-cfg', False),
            _MetaInfoClassMember('ipv6-neighbor', REFERENCE_CLASS, 'Ipv6Neighbor', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg', 'DynamicTemplate.IpSubscribers.IpSubscriber.Ipv6Neighbor',
                [], [],
                '''                Interface IPv6 Network configuration data
                ''',
                'ipv6_neighbor',
                'Cisco-IOS-XR-ipv6-nd-subscriber-cfg', False),
            _MetaInfoClassMember('pbr', REFERENCE_CLASS, 'Pbr', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg', 'DynamicTemplate.IpSubscribers.IpSubscriber.Pbr',
                [], [],
                '''                Dynamic Template PBR configuration
                ''',
                'pbr',
                'Cisco-IOS-XR-pbr-subscriber-cfg', False),
            _MetaInfoClassMember('ipv4-packet-filter', REFERENCE_CLASS, 'Ipv4PacketFilter', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg', 'DynamicTemplate.IpSubscribers.IpSubscriber.Ipv4PacketFilter',
                [], [],
                '''                IPv4 Packet Filtering configuration for the
                template
                ''',
                'ipv4_packet_filter',
                'Cisco-IOS-XR-ip-pfilter-subscriber-cfg', False),
            _MetaInfoClassMember('ipv6-packet-filter', REFERENCE_CLASS, 'Ipv6PacketFilter', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg', 'DynamicTemplate.IpSubscribers.IpSubscriber.Ipv6PacketFilter',
                [], [],
                '''                IPv6 Packet Filtering configuration for the
                interface
                ''',
                'ipv6_packet_filter',
                'Cisco-IOS-XR-ip-pfilter-subscriber-cfg', False),
            _MetaInfoClassMember('dhcpd', REFERENCE_CLASS, 'Dhcpd', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg', 'DynamicTemplate.IpSubscribers.IpSubscriber.Dhcpd',
                [], [],
                '''                Interface dhcpv4 configuration data
                ''',
                'dhcpd',
                'Cisco-IOS-XR-ipv4-dhcpd-subscriber-cfg', False),
            _MetaInfoClassMember('dhcpv6', REFERENCE_CLASS, 'Dhcpv6', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg', 'DynamicTemplate.IpSubscribers.IpSubscriber.Dhcpv6',
                [], [],
                '''                Interface dhcpv6 configuration data
                ''',
                'dhcpv6',
                'Cisco-IOS-XR-ipv6-new-dhcpv6d-subscriber-cfg', False),
            ],
            'Cisco-IOS-XR-subscriber-infra-tmplmgr-cfg',
            'ip-subscriber',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-subscriber-infra-tmplmgr-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg',
        ),
    },
    'DynamicTemplate.IpSubscribers' : {
        'meta_info' : _MetaInfoClass('DynamicTemplate.IpSubscribers', REFERENCE_CLASS,
            '''The IP Subscriber Template Table''',
            False, 
            [
            _MetaInfoClassMember('ip-subscriber', REFERENCE_LIST, 'IpSubscriber', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg', 'DynamicTemplate.IpSubscribers.IpSubscriber',
                [], [],
                '''                A IP Subscriber Type Template 
                ''',
                'ip_subscriber',
                'Cisco-IOS-XR-subscriber-infra-tmplmgr-cfg', False),
            ],
            'Cisco-IOS-XR-subscriber-infra-tmplmgr-cfg',
            'ip-subscribers',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-subscriber-infra-tmplmgr-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg',
        ),
    },
    'DynamicTemplate.SubscriberServices.SubscriberService.Ipv4Network' : {
        'meta_info' : _MetaInfoClass('DynamicTemplate.SubscriberServices.SubscriberService.Ipv4Network', REFERENCE_CLASS,
            '''Interface IPv4 Network configuration data''',
            False, 
            [
            _MetaInfoClassMember('unnumbered', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                Enable IP processing without an explicit
                address
                ''',
                'unnumbered',
                'Cisco-IOS-XR-ipv4-ma-subscriber-cfg', False),
            _MetaInfoClassMember('mtu', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('68', '65535')], [],
                '''                The IP Maximum Transmission Unit
                ''',
                'mtu',
                'Cisco-IOS-XR-ipv4-ma-subscriber-cfg', False),
            _MetaInfoClassMember('unreachables', ATTRIBUTE, 'bool', 'boolean',
                None, None,
                [], [],
                '''                TRUE if enabled, FALSE if disabled
                ''',
                'unreachables',
                'Cisco-IOS-XR-ipv4-ma-subscriber-cfg', False, default_value='False'),
            _MetaInfoClassMember('rpf', ATTRIBUTE, 'bool', 'boolean',
                None, None,
                [], [],
                '''                TRUE if enabled, FALSE if disabled
                ''',
                'rpf',
                'Cisco-IOS-XR-ipv4-ma-subscriber-cfg', False, default_value='True'),
            ],
            'Cisco-IOS-XR-ipv4-ma-subscriber-cfg',
            'ipv4-network',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-ipv4-ma-subscriber-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg',
        ),
    },
    'DynamicTemplate.SubscriberServices.SubscriberService.SubscriberAttribute.OpenDns' : {
        'meta_info' : _MetaInfoClass('DynamicTemplate.SubscriberServices.SubscriberService.SubscriberAttribute.OpenDns', REFERENCE_CLASS,
            '''OpenDNS configuration data''',
            False, 
            [
            _MetaInfoClassMember('device-id', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                Specify deviceID to be used for applying
                OpenDNS policies
                ''',
                'device_id',
                'Cisco-IOS-XR-opendns-deviceid-cfg', False),
            ],
            'Cisco-IOS-XR-opendns-deviceid-cfg',
            'open-dns',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-opendns-deviceid-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg',
        ),
    },
    'DynamicTemplate.SubscriberServices.SubscriberService.SubscriberAttribute' : {
        'meta_info' : _MetaInfoClass('DynamicTemplate.SubscriberServices.SubscriberService.SubscriberAttribute', REFERENCE_CLASS,
            '''Subscriber attribute configuration data''',
            False, 
            [
            _MetaInfoClassMember('open-dns', REFERENCE_CLASS, 'OpenDns', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg', 'DynamicTemplate.SubscriberServices.SubscriberService.SubscriberAttribute.OpenDns',
                [], [],
                '''                OpenDNS configuration data
                ''',
                'open_dns',
                'Cisco-IOS-XR-opendns-deviceid-cfg', False),
            ],
            'Cisco-IOS-XR-opendns-deviceid-cfg',
            'subscriber-attribute',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-opendns-deviceid-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg',
        ),
    },
    'DynamicTemplate.SubscriberServices.SubscriberService.Accounting.ServiceAccounting' : {
        'meta_info' : _MetaInfoClass('DynamicTemplate.SubscriberServices.SubscriberService.Accounting.ServiceAccounting', REFERENCE_CLASS,
            '''Subscriber accounting service accounting''',
            False, 
            [
            _MetaInfoClassMember('method-list-name', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                Service accounting method list name
                ''',
                'method_list_name',
                'Cisco-IOS-XR-subscriber-accounting-cfg', False),
            _MetaInfoClassMember('accounting-interim-interval', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('0', '4294967295')], [],
                '''                Accounting interim interval in minutes
                ''',
                'accounting_interim_interval',
                'Cisco-IOS-XR-subscriber-accounting-cfg', False),
            ],
            'Cisco-IOS-XR-subscriber-accounting-cfg',
            'service-accounting',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-subscriber-accounting-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg',
        ),
    },
    'DynamicTemplate.SubscriberServices.SubscriberService.Accounting.Session.HoldAcctStart' : _MetaInfoEnum('HoldAcctStart',
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg', 'DynamicTemplate.SubscriberServices.SubscriberService.Accounting.Session.HoldAcctStart',
        '''Hold Accounting start based on IA_PD''',
        {
            'ipv6-prefix-delegation':'ipv6_prefix_delegation',
        }, 'Cisco-IOS-XR-subscriber-accounting-cfg', _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-subscriber-accounting-cfg']),
    'DynamicTemplate.SubscriberServices.SubscriberService.Accounting.Session' : {
        'meta_info' : _MetaInfoClass('DynamicTemplate.SubscriberServices.SubscriberService.Accounting.Session', REFERENCE_CLASS,
            '''Subscriber accounting session accounting''',
            False, 
            [
            _MetaInfoClassMember('method-list-name', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                Session accounting method list name
                ''',
                'method_list_name',
                'Cisco-IOS-XR-subscriber-accounting-cfg', False),
            _MetaInfoClassMember('periodic-interval', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('0', '4294967295')], [],
                '''                Interim accounting interval in minutes
                ''',
                'periodic_interval',
                'Cisco-IOS-XR-subscriber-accounting-cfg', False),
            _MetaInfoClassMember('dual-stack-delay', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('0', '4294967295')], [],
                '''                Dual stack wait delay in seconds
                ''',
                'dual_stack_delay',
                'Cisco-IOS-XR-subscriber-accounting-cfg', False),
            _MetaInfoClassMember('hold-acct-start', REFERENCE_ENUM_CLASS, 'HoldAcctStart', 'enumeration',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg', 'DynamicTemplate.SubscriberServices.SubscriberService.Accounting.Session.HoldAcctStart',
                [], [],
                '''                Hold Accounting start based on IA_PD
                ''',
                'hold_acct_start',
                'Cisco-IOS-XR-subscriber-accounting-cfg', False),
            ],
            'Cisco-IOS-XR-subscriber-accounting-cfg',
            'session',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-subscriber-accounting-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg',
        ),
    },
    'DynamicTemplate.SubscriberServices.SubscriberService.Accounting.IdleTimeout' : {
        'meta_info' : _MetaInfoClass('DynamicTemplate.SubscriberServices.SubscriberService.Accounting.IdleTimeout', REFERENCE_CLASS,
            '''Subscriber accounting idle timeout''',
            False, 
            [
            _MetaInfoClassMember('timeout-value', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('60', '4320000')], [],
                '''                Idle timeout value in seconds
                ''',
                'timeout_value',
                'Cisco-IOS-XR-subscriber-accounting-cfg', False),
            _MetaInfoClassMember('threshold', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('1', '10000')], [],
                '''                Threshold in minute(s) per packet
                ''',
                'threshold',
                'Cisco-IOS-XR-subscriber-accounting-cfg', False),
            _MetaInfoClassMember('direction', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                Idle timeout traffic direction
                ''',
                'direction',
                'Cisco-IOS-XR-subscriber-accounting-cfg', False),
            ],
            'Cisco-IOS-XR-subscriber-accounting-cfg',
            'idle-timeout',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-subscriber-accounting-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg',
        ),
    },
    'DynamicTemplate.SubscriberServices.SubscriberService.Accounting' : {
        'meta_info' : _MetaInfoClass('DynamicTemplate.SubscriberServices.SubscriberService.Accounting', REFERENCE_CLASS,
            '''Subscriber accounting dynamic-template commands''',
            False, 
            [
            _MetaInfoClassMember('service-accounting', REFERENCE_CLASS, 'ServiceAccounting', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg', 'DynamicTemplate.SubscriberServices.SubscriberService.Accounting.ServiceAccounting',
                [], [],
                '''                Subscriber accounting service accounting
                ''',
                'service_accounting',
                'Cisco-IOS-XR-subscriber-accounting-cfg', False),
            _MetaInfoClassMember('session', REFERENCE_CLASS, 'Session', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg', 'DynamicTemplate.SubscriberServices.SubscriberService.Accounting.Session',
                [], [],
                '''                Subscriber accounting session accounting
                ''',
                'session',
                'Cisco-IOS-XR-subscriber-accounting-cfg', False),
            _MetaInfoClassMember('idle-timeout', REFERENCE_CLASS, 'IdleTimeout', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg', 'DynamicTemplate.SubscriberServices.SubscriberService.Accounting.IdleTimeout',
                [], [],
                '''                Subscriber accounting idle timeout
                ''',
                'idle_timeout',
                'Cisco-IOS-XR-subscriber-accounting-cfg', False),
            _MetaInfoClassMember('monitor-feature', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                Subscriber monitor feature
                ''',
                'monitor_feature',
                'Cisco-IOS-XR-subscriber-accounting-cfg', False),
            _MetaInfoClassMember('prepaid-feature', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                Subscriber accounting prepaid feature
                ''',
                'prepaid_feature',
                'Cisco-IOS-XR-subscriber-accounting-cfg', False),
            ],
            'Cisco-IOS-XR-subscriber-accounting-cfg',
            'accounting',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-subscriber-accounting-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg',
        ),
    },
    'DynamicTemplate.SubscriberServices.SubscriberService.Qos.ServicePolicy.Input' : {
        'meta_info' : _MetaInfoClass('DynamicTemplate.SubscriberServices.SubscriberService.Qos.ServicePolicy.Input', REFERENCE_CLASS,
            '''Subscriber ingress policy''',
            False, 
            [
            _MetaInfoClassMember('policy-name', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                Name of policy-map
                ''',
                'policy_name',
                'Cisco-IOS-XR-qos-ma-bng-cfg', False, is_mandatory=True),
            _MetaInfoClassMember('spi-name', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                Name of the SPI
                ''',
                'spi_name',
                'Cisco-IOS-XR-qos-ma-bng-cfg', False),
            _MetaInfoClassMember('merge', ATTRIBUTE, 'bool', 'boolean',
                None, None,
                [], [],
                '''                TRUE for merge enabled for service-policy
                applied on dynamic template.
                ''',
                'merge',
                'Cisco-IOS-XR-qos-ma-bng-cfg', False),
            _MetaInfoClassMember('merge-id', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('0', '255')], [],
                '''                Merge ID value
                ''',
                'merge_id',
                'Cisco-IOS-XR-qos-ma-bng-cfg', False),
            _MetaInfoClassMember('account-stats', ATTRIBUTE, 'bool', 'boolean',
                None, None,
                [], [],
                '''                TRUE for account stats enabled for
                service-policy applied on dynamic template.
                Note: account stats not supported for
                subscriber type 'ppp' and 'ipsubscriber'.
                ''',
                'account_stats',
                'Cisco-IOS-XR-qos-ma-bng-cfg', False),
            ],
            'Cisco-IOS-XR-qos-ma-bng-cfg',
            'input',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-qos-ma-bng-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg',
            is_presence=True,
        ),
    },
    'DynamicTemplate.SubscriberServices.SubscriberService.Qos.ServicePolicy.Output' : {
        'meta_info' : _MetaInfoClass('DynamicTemplate.SubscriberServices.SubscriberService.Qos.ServicePolicy.Output', REFERENCE_CLASS,
            '''Subscriber egress policy''',
            False, 
            [
            _MetaInfoClassMember('policy-name', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                Name of policy-map
                ''',
                'policy_name',
                'Cisco-IOS-XR-qos-ma-bng-cfg', False, is_mandatory=True),
            _MetaInfoClassMember('spi-name', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                Name of the SPI
                ''',
                'spi_name',
                'Cisco-IOS-XR-qos-ma-bng-cfg', False),
            _MetaInfoClassMember('merge', ATTRIBUTE, 'bool', 'boolean',
                None, None,
                [], [],
                '''                TRUE for merge enabled for service-policy
                applied on dynamic template.
                ''',
                'merge',
                'Cisco-IOS-XR-qos-ma-bng-cfg', False),
            _MetaInfoClassMember('merge-id', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('0', '255')], [],
                '''                Merge ID value
                ''',
                'merge_id',
                'Cisco-IOS-XR-qos-ma-bng-cfg', False),
            _MetaInfoClassMember('account-stats', ATTRIBUTE, 'bool', 'boolean',
                None, None,
                [], [],
                '''                TRUE for account stats enabled for
                service-policy applied on dynamic template.
                Note: account stats not supported for
                subscriber type 'ppp' and 'ipsubscriber'.
                ''',
                'account_stats',
                'Cisco-IOS-XR-qos-ma-bng-cfg', False),
            ],
            'Cisco-IOS-XR-qos-ma-bng-cfg',
            'output',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-qos-ma-bng-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg',
            is_presence=True,
        ),
    },
    'DynamicTemplate.SubscriberServices.SubscriberService.Qos.ServicePolicy' : {
        'meta_info' : _MetaInfoClass('DynamicTemplate.SubscriberServices.SubscriberService.Qos.ServicePolicy', REFERENCE_CLASS,
            '''Service policy to be applied in ingress/egress
direction''',
            False, 
            [
            _MetaInfoClassMember('input', REFERENCE_CLASS, 'Input', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg', 'DynamicTemplate.SubscriberServices.SubscriberService.Qos.ServicePolicy.Input',
                [], [],
                '''                Subscriber ingress policy
                ''',
                'input',
                'Cisco-IOS-XR-qos-ma-bng-cfg', False, is_presence=True),
            _MetaInfoClassMember('output', REFERENCE_CLASS, 'Output', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg', 'DynamicTemplate.SubscriberServices.SubscriberService.Qos.ServicePolicy.Output',
                [], [],
                '''                Subscriber egress policy
                ''',
                'output',
                'Cisco-IOS-XR-qos-ma-bng-cfg', False, is_presence=True),
            ],
            'Cisco-IOS-XR-qos-ma-bng-cfg',
            'service-policy',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-qos-ma-bng-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg',
        ),
    },
    'DynamicTemplate.SubscriberServices.SubscriberService.Qos.Account' : {
        'meta_info' : _MetaInfoClass('DynamicTemplate.SubscriberServices.SubscriberService.Qos.Account', REFERENCE_CLASS,
            '''QoS L2 overhead accounting''',
            False, 
            [
            _MetaInfoClassMember('aal', REFERENCE_ENUM_CLASS, 'Qosl2DataLink', 'Qosl2-data-link',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_qos_ma_bng_cfg', 'Qosl2DataLink',
                [], [],
                '''                ATM adaptation layer AAL
                ''',
                'aal',
                'Cisco-IOS-XR-qos-ma-bng-cfg', False, has_must=True),
            _MetaInfoClassMember('encapsulation', REFERENCE_ENUM_CLASS, 'Qosl2Encap', 'Qosl2-encap',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_qos_ma_bng_cfg', 'Qosl2Encap',
                [], [],
                '''                Specify encapsulation type
                ''',
                'encapsulation',
                'Cisco-IOS-XR-qos-ma-bng-cfg', False, has_must=True),
            _MetaInfoClassMember('atm-cell-tax', ATTRIBUTE, 'Empty', 'empty',
                None, None,
                [], [],
                '''                ATM cell tax to L2 overhead
                ''',
                'atm_cell_tax',
                'Cisco-IOS-XR-qos-ma-bng-cfg', False, has_must=True),
            _MetaInfoClassMember('user-defined', ATTRIBUTE, 'int', 'int32',
                None, None,
                [('-63', '63')], [],
                '''                Numeric L2 overhead offset
                ''',
                'user_defined',
                'Cisco-IOS-XR-qos-ma-bng-cfg', False, has_must=True),
            ],
            'Cisco-IOS-XR-qos-ma-bng-cfg',
            'account',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-qos-ma-bng-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg',
        ),
    },
    'DynamicTemplate.SubscriberServices.SubscriberService.Qos.Output' : {
        'meta_info' : _MetaInfoClass('DynamicTemplate.SubscriberServices.SubscriberService.Qos.Output', REFERENCE_CLASS,
            '''QoS to be applied in egress direction''',
            False, 
            [
            _MetaInfoClassMember('minimum-bandwidth', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('1', '4294967295')], [],
                '''                Minimum bandwidth value for the subscriber (in
                kbps)
                ''',
                'minimum_bandwidth',
                'Cisco-IOS-XR-qos-ma-bng-cfg', False),
            ],
            'Cisco-IOS-XR-qos-ma-bng-cfg',
            'output',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-qos-ma-bng-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg',
        ),
    },
    'DynamicTemplate.SubscriberServices.SubscriberService.Qos' : {
        'meta_info' : _MetaInfoClass('DynamicTemplate.SubscriberServices.SubscriberService.Qos', REFERENCE_CLASS,
            '''QoS dynamically applied configuration template''',
            False, 
            [
            _MetaInfoClassMember('service-policy', REFERENCE_CLASS, 'ServicePolicy', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg', 'DynamicTemplate.SubscriberServices.SubscriberService.Qos.ServicePolicy',
                [], [],
                '''                Service policy to be applied in ingress/egress
                direction
                ''',
                'service_policy',
                'Cisco-IOS-XR-qos-ma-bng-cfg', False),
            _MetaInfoClassMember('account', REFERENCE_CLASS, 'Account', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg', 'DynamicTemplate.SubscriberServices.SubscriberService.Qos.Account',
                [], [],
                '''                QoS L2 overhead accounting
                ''',
                'account',
                'Cisco-IOS-XR-qos-ma-bng-cfg', False),
            _MetaInfoClassMember('output', REFERENCE_CLASS, 'Output', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg', 'DynamicTemplate.SubscriberServices.SubscriberService.Qos.Output',
                [], [],
                '''                QoS to be applied in egress direction
                ''',
                'output',
                'Cisco-IOS-XR-qos-ma-bng-cfg', False),
            ],
            'Cisco-IOS-XR-qos-ma-bng-cfg',
            'qos',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-qos-ma-bng-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg',
        ),
    },
    'DynamicTemplate.SubscriberServices.SubscriberService.Ipv6Network.Addresses.AutoConfiguration' : {
        'meta_info' : _MetaInfoClass('DynamicTemplate.SubscriberServices.SubscriberService.Ipv6Network.Addresses.AutoConfiguration', REFERENCE_CLASS,
            '''Auto IPv6 Interface Configuration''',
            False, 
            [
            _MetaInfoClassMember('enable', ATTRIBUTE, 'Empty', 'empty',
                None, None,
                [], [],
                '''                The flag to enable auto ipv6 interface
                configuration
                ''',
                'enable',
                'Cisco-IOS-XR-ipv6-ma-subscriber-cfg', False),
            ],
            'Cisco-IOS-XR-ipv6-ma-subscriber-cfg',
            'auto-configuration',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-ipv6-ma-subscriber-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg',
        ),
    },
    'DynamicTemplate.SubscriberServices.SubscriberService.Ipv6Network.Addresses' : {
        'meta_info' : _MetaInfoClass('DynamicTemplate.SubscriberServices.SubscriberService.Ipv6Network.Addresses', REFERENCE_CLASS,
            '''Set the IPv6 address of an interface''',
            False, 
            [
            _MetaInfoClassMember('auto-configuration', REFERENCE_CLASS, 'AutoConfiguration', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg', 'DynamicTemplate.SubscriberServices.SubscriberService.Ipv6Network.Addresses.AutoConfiguration',
                [], [],
                '''                Auto IPv6 Interface Configuration
                ''',
                'auto_configuration',
                'Cisco-IOS-XR-ipv6-ma-subscriber-cfg', False),
            ],
            'Cisco-IOS-XR-ipv6-ma-subscriber-cfg',
            'addresses',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-ipv6-ma-subscriber-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg',
        ),
    },
    'DynamicTemplate.SubscriberServices.SubscriberService.Ipv6Network' : {
        'meta_info' : _MetaInfoClass('DynamicTemplate.SubscriberServices.SubscriberService.Ipv6Network', REFERENCE_CLASS,
            '''Interface IPv6 Network configuration data''',
            False, 
            [
            _MetaInfoClassMember('addresses', REFERENCE_CLASS, 'Addresses', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg', 'DynamicTemplate.SubscriberServices.SubscriberService.Ipv6Network.Addresses',
                [], [],
                '''                Set the IPv6 address of an interface
                ''',
                'addresses',
                'Cisco-IOS-XR-ipv6-ma-subscriber-cfg', False),
            _MetaInfoClassMember('mtu', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('1280', '65535')], [],
                '''                MTU Setting of Interface
                ''',
                'mtu',
                'Cisco-IOS-XR-ipv6-ma-subscriber-cfg', False),
            _MetaInfoClassMember('rpf', ATTRIBUTE, 'bool', 'boolean',
                None, None,
                [], [],
                '''                TRUE if enabled, FALSE if disabled
                ''',
                'rpf',
                'Cisco-IOS-XR-ipv6-ma-subscriber-cfg', False),
            _MetaInfoClassMember('unreachables', ATTRIBUTE, 'Empty', 'empty',
                None, None,
                [], [],
                '''                Override Sending of ICMP Unreachable Messages
                ''',
                'unreachables',
                'Cisco-IOS-XR-ipv6-ma-subscriber-cfg', False),
            ],
            'Cisco-IOS-XR-ipv6-ma-subscriber-cfg',
            'ipv6-network',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-ipv6-ma-subscriber-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg',
        ),
    },
    'DynamicTemplate.SubscriberServices.SubscriberService.SpanMonitorSessions.SpanMonitorSession.Attachment' : {
        'meta_info' : _MetaInfoClass('DynamicTemplate.SubscriberServices.SubscriberService.SpanMonitorSessions.SpanMonitorSession.Attachment', REFERENCE_CLASS,
            '''Attach the interface to a Monitor Session''',
            False, 
            [
            _MetaInfoClassMember('session-name', ATTRIBUTE, 'str', 'dt1:Span-session-name',
                None, None,
                [(1, 79)], [],
                '''                Session Name
                ''',
                'session_name',
                'Cisco-IOS-XR-Ethernet-SPAN-subscriber-cfg', False, is_mandatory=True),
            _MetaInfoClassMember('direction', REFERENCE_ENUM_CLASS, 'SpanTrafficDirection', 'Span-traffic-direction',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_Ethernet_SPAN_subscriber_cfg', 'SpanTrafficDirection',
                [], [],
                '''                Specify the direction of traffic to replicate
                (optional)
                ''',
                'direction',
                'Cisco-IOS-XR-Ethernet-SPAN-subscriber-cfg', False),
            _MetaInfoClassMember('port-level-enable', ATTRIBUTE, 'Empty', 'empty',
                None, None,
                [], [],
                '''                Enable port level traffic mirroring
                ''',
                'port_level_enable',
                'Cisco-IOS-XR-Ethernet-SPAN-subscriber-cfg', False),
            ],
            'Cisco-IOS-XR-Ethernet-SPAN-subscriber-cfg',
            'attachment',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-Ethernet-SPAN-subscriber-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg',
            is_presence=True,
        ),
    },
    'DynamicTemplate.SubscriberServices.SubscriberService.SpanMonitorSessions.SpanMonitorSession.Acl' : {
        'meta_info' : _MetaInfoClass('DynamicTemplate.SubscriberServices.SubscriberService.SpanMonitorSessions.SpanMonitorSession.Acl', REFERENCE_CLASS,
            '''Enable ACL matching for traffic mirroring''',
            False, 
            [
            _MetaInfoClassMember('acl-enable', ATTRIBUTE, 'Empty', 'empty',
                None, None,
                [], [],
                '''                Enable ACL
                ''',
                'acl_enable',
                'Cisco-IOS-XR-Ethernet-SPAN-subscriber-cfg', False, is_mandatory=True),
            _MetaInfoClassMember('acl-name', ATTRIBUTE, 'str', 'dt1:Span-acl-name',
                None, None,
                [(1, 80)], [],
                '''                ACL Name
                ''',
                'acl_name',
                'Cisco-IOS-XR-Ethernet-SPAN-subscriber-cfg', False),
            ],
            'Cisco-IOS-XR-Ethernet-SPAN-subscriber-cfg',
            'acl',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-Ethernet-SPAN-subscriber-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg',
            is_presence=True,
        ),
    },
    'DynamicTemplate.SubscriberServices.SubscriberService.SpanMonitorSessions.SpanMonitorSession' : {
        'meta_info' : _MetaInfoClass('DynamicTemplate.SubscriberServices.SubscriberService.SpanMonitorSessions.SpanMonitorSession', REFERENCE_LIST,
            '''Configuration for a particular class of Monitor
Session''',
            False, 
            [
            _MetaInfoClassMember('session-class', REFERENCE_ENUM_CLASS, 'SpanSessionClass', 'dt1:Span-session-class',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_Ethernet_SPAN_datatypes', 'SpanSessionClass',
                [], [],
                '''                Session Class
                ''',
                'session_class',
                'Cisco-IOS-XR-Ethernet-SPAN-subscriber-cfg', True),
            _MetaInfoClassMember('mirror-first', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('1', '10000')], [],
                '''                Mirror a specified number of bytes from start of
                packet
                ''',
                'mirror_first',
                'Cisco-IOS-XR-Ethernet-SPAN-subscriber-cfg', False),
            _MetaInfoClassMember('attachment', REFERENCE_CLASS, 'Attachment', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg', 'DynamicTemplate.SubscriberServices.SubscriberService.SpanMonitorSessions.SpanMonitorSession.Attachment',
                [], [],
                '''                Attach the interface to a Monitor Session
                ''',
                'attachment',
                'Cisco-IOS-XR-Ethernet-SPAN-subscriber-cfg', False, is_presence=True),
            _MetaInfoClassMember('mirror-interval', REFERENCE_ENUM_CLASS, 'SpanMirrorInterval', 'Span-mirror-interval',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_Ethernet_SPAN_subscriber_cfg', 'SpanMirrorInterval',
                [], [],
                '''                Specify the mirror interval
                ''',
                'mirror_interval',
                'Cisco-IOS-XR-Ethernet-SPAN-subscriber-cfg', False),
            _MetaInfoClassMember('acl', REFERENCE_CLASS, 'Acl', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg', 'DynamicTemplate.SubscriberServices.SubscriberService.SpanMonitorSessions.SpanMonitorSession.Acl',
                [], [],
                '''                Enable ACL matching for traffic mirroring
                ''',
                'acl',
                'Cisco-IOS-XR-Ethernet-SPAN-subscriber-cfg', False, is_presence=True),
            ],
            'Cisco-IOS-XR-Ethernet-SPAN-subscriber-cfg',
            'span-monitor-session',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-Ethernet-SPAN-subscriber-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg',
        ),
    },
    'DynamicTemplate.SubscriberServices.SubscriberService.SpanMonitorSessions' : {
        'meta_info' : _MetaInfoClass('DynamicTemplate.SubscriberServices.SubscriberService.SpanMonitorSessions', REFERENCE_CLASS,
            '''Monitor Session container for this template''',
            False, 
            [
            _MetaInfoClassMember('span-monitor-session', REFERENCE_LIST, 'SpanMonitorSession', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg', 'DynamicTemplate.SubscriberServices.SubscriberService.SpanMonitorSessions.SpanMonitorSession',
                [], [],
                '''                Configuration for a particular class of Monitor
                Session
                ''',
                'span_monitor_session',
                'Cisco-IOS-XR-Ethernet-SPAN-subscriber-cfg', False),
            ],
            'Cisco-IOS-XR-Ethernet-SPAN-subscriber-cfg',
            'span-monitor-sessions',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-Ethernet-SPAN-subscriber-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg',
        ),
    },
    'DynamicTemplate.SubscriberServices.SubscriberService.Ipv6Neighbor.RaInterval' : {
        'meta_info' : _MetaInfoClass('DynamicTemplate.SubscriberServices.SubscriberService.Ipv6Neighbor.RaInterval', REFERENCE_CLASS,
            '''Set IPv6 Router Advertisement (RA) interval in
seconds''',
            False, 
            [
            _MetaInfoClassMember('maximum', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('4', '1800')], [],
                '''                Maximum RA interval in seconds
                ''',
                'maximum',
                'Cisco-IOS-XR-ipv6-nd-subscriber-cfg', False, is_mandatory=True),
            _MetaInfoClassMember('minimum', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('3', '1800')], [],
                '''                Minimum RA interval in seconds. Must be less
                than 0.75 * maximum interval
                ''',
                'minimum',
                'Cisco-IOS-XR-ipv6-nd-subscriber-cfg', False),
            ],
            'Cisco-IOS-XR-ipv6-nd-subscriber-cfg',
            'ra-interval',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-ipv6-nd-subscriber-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg',
            is_presence=True,
        ),
    },
    'DynamicTemplate.SubscriberServices.SubscriberService.Ipv6Neighbor.FramedPrefix' : {
        'meta_info' : _MetaInfoClass('DynamicTemplate.SubscriberServices.SubscriberService.Ipv6Neighbor.FramedPrefix', REFERENCE_CLASS,
            '''Set the IPv6 framed ipv6 prefix for a
subscriber interface ''',
            False, 
            [
            _MetaInfoClassMember('prefix-length', ATTRIBUTE, 'int', 'xr:Ipv6-prefix-length',
                None, None,
                [('0', '128')], [],
                '''                IPv6 framed prefix length
                ''',
                'prefix_length',
                'Cisco-IOS-XR-ipv6-nd-subscriber-cfg', False, is_mandatory=True),
            _MetaInfoClassMember('prefix', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                IPV6 framed prefix address
                ''',
                'prefix',
                'Cisco-IOS-XR-ipv6-nd-subscriber-cfg', False, is_mandatory=True),
            ],
            'Cisco-IOS-XR-ipv6-nd-subscriber-cfg',
            'framed-prefix',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-ipv6-nd-subscriber-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg',
            is_presence=True,
        ),
    },
    'DynamicTemplate.SubscriberServices.SubscriberService.Ipv6Neighbor.DuplicateAddressDetection' : {
        'meta_info' : _MetaInfoClass('DynamicTemplate.SubscriberServices.SubscriberService.Ipv6Neighbor.DuplicateAddressDetection', REFERENCE_CLASS,
            '''Duplicate Address Detection (DAD)''',
            False, 
            [
            _MetaInfoClassMember('attempts', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('0', '600')], [],
                '''                Set IPv6 duplicate address detection transmits
                ''',
                'attempts',
                'Cisco-IOS-XR-ipv6-nd-subscriber-cfg', False),
            ],
            'Cisco-IOS-XR-ipv6-nd-subscriber-cfg',
            'duplicate-address-detection',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-ipv6-nd-subscriber-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg',
        ),
    },
    'DynamicTemplate.SubscriberServices.SubscriberService.Ipv6Neighbor.RaInitial' : {
        'meta_info' : _MetaInfoClass('DynamicTemplate.SubscriberServices.SubscriberService.Ipv6Neighbor.RaInitial', REFERENCE_CLASS,
            '''IPv6 ND RA Initial''',
            False, 
            [
            _MetaInfoClassMember('count', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('0', '32')], [],
                '''                Initial RA count
                ''',
                'count',
                'Cisco-IOS-XR-ipv6-nd-subscriber-cfg', False, is_mandatory=True),
            _MetaInfoClassMember('interval', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('4', '1800')], [],
                '''                Initial RA interval in seconds
                ''',
                'interval',
                'Cisco-IOS-XR-ipv6-nd-subscriber-cfg', False, is_mandatory=True),
            ],
            'Cisco-IOS-XR-ipv6-nd-subscriber-cfg',
            'ra-initial',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-ipv6-nd-subscriber-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg',
            is_presence=True,
        ),
    },
    'DynamicTemplate.SubscriberServices.SubscriberService.Ipv6Neighbor' : {
        'meta_info' : _MetaInfoClass('DynamicTemplate.SubscriberServices.SubscriberService.Ipv6Neighbor', REFERENCE_CLASS,
            '''Interface IPv6 Network configuration data''',
            False, 
            [
            _MetaInfoClassMember('ra-interval', REFERENCE_CLASS, 'RaInterval', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg', 'DynamicTemplate.SubscriberServices.SubscriberService.Ipv6Neighbor.RaInterval',
                [], [],
                '''                Set IPv6 Router Advertisement (RA) interval in
                seconds
                ''',
                'ra_interval',
                'Cisco-IOS-XR-ipv6-nd-subscriber-cfg', False, is_presence=True),
            _MetaInfoClassMember('framed-prefix', REFERENCE_CLASS, 'FramedPrefix', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg', 'DynamicTemplate.SubscriberServices.SubscriberService.Ipv6Neighbor.FramedPrefix',
                [], [],
                '''                Set the IPv6 framed ipv6 prefix for a
                subscriber interface 
                ''',
                'framed_prefix',
                'Cisco-IOS-XR-ipv6-nd-subscriber-cfg', False, is_presence=True),
            _MetaInfoClassMember('duplicate-address-detection', REFERENCE_CLASS, 'DuplicateAddressDetection', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg', 'DynamicTemplate.SubscriberServices.SubscriberService.Ipv6Neighbor.DuplicateAddressDetection',
                [], [],
                '''                Duplicate Address Detection (DAD)
                ''',
                'duplicate_address_detection',
                'Cisco-IOS-XR-ipv6-nd-subscriber-cfg', False),
            _MetaInfoClassMember('ra-initial', REFERENCE_CLASS, 'RaInitial', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg', 'DynamicTemplate.SubscriberServices.SubscriberService.Ipv6Neighbor.RaInitial',
                [], [],
                '''                IPv6 ND RA Initial
                ''',
                'ra_initial',
                'Cisco-IOS-XR-ipv6-nd-subscriber-cfg', False, is_presence=True),
            _MetaInfoClassMember('framed-prefix-pool', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                Set the IPv6 framed ipv6 prefix pool for a
                subscriber interface 
                ''',
                'framed_prefix_pool',
                'Cisco-IOS-XR-ipv6-nd-subscriber-cfg', False),
            _MetaInfoClassMember('managed-config', ATTRIBUTE, 'Empty', 'empty',
                None, None,
                [], [],
                '''                Host to use stateful protocol for address
                configuration
                ''',
                'managed_config',
                'Cisco-IOS-XR-ipv6-nd-subscriber-cfg', False),
            _MetaInfoClassMember('other-config', ATTRIBUTE, 'Empty', 'empty',
                None, None,
                [], [],
                '''                Host to use stateful protocol for non-address
                configuration
                ''',
                'other_config',
                'Cisco-IOS-XR-ipv6-nd-subscriber-cfg', False),
            _MetaInfoClassMember('start-ra-on-ipv6-enable', ATTRIBUTE, 'Empty', 'empty',
                None, None,
                [], [],
                '''                Start RA on ipv6-enable config
                ''',
                'start_ra_on_ipv6_enable',
                'Cisco-IOS-XR-ipv6-nd-subscriber-cfg', False),
            _MetaInfoClassMember('nud-enable', ATTRIBUTE, 'Empty', 'empty',
                None, None,
                [], [],
                '''                NUD enable
                ''',
                'nud_enable',
                'Cisco-IOS-XR-ipv6-nd-subscriber-cfg', False),
            _MetaInfoClassMember('ra-lifetime', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('0', '9000')], [],
                '''                Set IPv6 Router Advertisement (RA) lifetime in
                seconds
                ''',
                'ra_lifetime',
                'Cisco-IOS-XR-ipv6-nd-subscriber-cfg', False),
            _MetaInfoClassMember('router-preference', REFERENCE_ENUM_CLASS, 'Ipv6NdRouterPrefTemplate', 'Ipv6-nd-router-pref-template',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_nd_subscriber_cfg', 'Ipv6NdRouterPrefTemplate',
                [], [],
                '''                RA Router Preference
                ''',
                'router_preference',
                'Cisco-IOS-XR-ipv6-nd-subscriber-cfg', False),
            _MetaInfoClassMember('ra-suppress', ATTRIBUTE, 'Empty', 'empty',
                None, None,
                [], [],
                '''                Enable suppress IPv6 router advertisement
                ''',
                'ra_suppress',
                'Cisco-IOS-XR-ipv6-nd-subscriber-cfg', False),
            _MetaInfoClassMember('ra-unicast', ATTRIBUTE, 'Empty', 'empty',
                None, None,
                [], [],
                '''                Enable RA unicast Flag
                ''',
                'ra_unicast',
                'Cisco-IOS-XR-ipv6-nd-subscriber-cfg', False),
            _MetaInfoClassMember('ra-unspecify-hoplimit', ATTRIBUTE, 'Empty', 'empty',
                None, None,
                [], [],
                '''                Unspecify IPv6 Router Advertisement (RA)
                hop-limit
                ''',
                'ra_unspecify_hoplimit',
                'Cisco-IOS-XR-ipv6-nd-subscriber-cfg', False),
            _MetaInfoClassMember('ra-suppress-mtu', ATTRIBUTE, 'Empty', 'empty',
                None, None,
                [], [],
                '''                RA suppress MTU flag
                ''',
                'ra_suppress_mtu',
                'Cisco-IOS-XR-ipv6-nd-subscriber-cfg', False),
            _MetaInfoClassMember('suppress-cache-learning', ATTRIBUTE, 'Empty', 'empty',
                None, None,
                [], [],
                '''                Suppress cache learning flag
                ''',
                'suppress_cache_learning',
                'Cisco-IOS-XR-ipv6-nd-subscriber-cfg', False),
            _MetaInfoClassMember('reachable-time', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('0', '3600000')], [],
                '''                Set advertised reachability time in
                milliseconds
                ''',
                'reachable_time',
                'Cisco-IOS-XR-ipv6-nd-subscriber-cfg', False),
            _MetaInfoClassMember('ns-interval', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('1000', '4294967295')], [],
                '''                Set advertised NS retransmission interval in
                milliseconds
                ''',
                'ns_interval',
                'Cisco-IOS-XR-ipv6-nd-subscriber-cfg', False),
            ],
            'Cisco-IOS-XR-ipv6-nd-subscriber-cfg',
            'ipv6-neighbor',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-ipv6-nd-subscriber-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg',
        ),
    },
    'DynamicTemplate.SubscriberServices.SubscriberService.Pbr.ServicePolicies.ServicePolicy' : {
        'meta_info' : _MetaInfoClass('DynamicTemplate.SubscriberServices.SubscriberService.Pbr.ServicePolicies.ServicePolicy', REFERENCE_LIST,
            '''Service policy details''',
            False, 
            [
            _MetaInfoClassMember('service-policy', ATTRIBUTE, 'str', 'string',
                None, None,
                [(1, 64)], [],
                '''                Name of policy-map
                ''',
                'service_policy',
                'Cisco-IOS-XR-pbr-subscriber-cfg', True),
            ],
            'Cisco-IOS-XR-pbr-subscriber-cfg',
            'service-policy',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-pbr-subscriber-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg',
        ),
    },
    'DynamicTemplate.SubscriberServices.SubscriberService.Pbr.ServicePolicies' : {
        'meta_info' : _MetaInfoClass('DynamicTemplate.SubscriberServices.SubscriberService.Pbr.ServicePolicies', REFERENCE_CLASS,
            '''Ingress service policy''',
            False, 
            [
            _MetaInfoClassMember('service-policy', REFERENCE_LIST, 'ServicePolicy', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg', 'DynamicTemplate.SubscriberServices.SubscriberService.Pbr.ServicePolicies.ServicePolicy',
                [], [],
                '''                Service policy details
                ''',
                'service_policy',
                'Cisco-IOS-XR-pbr-subscriber-cfg', False),
            ],
            'Cisco-IOS-XR-pbr-subscriber-cfg',
            'service-policies',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-pbr-subscriber-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg',
        ),
    },
    'DynamicTemplate.SubscriberServices.SubscriberService.Pbr' : {
        'meta_info' : _MetaInfoClass('DynamicTemplate.SubscriberServices.SubscriberService.Pbr', REFERENCE_CLASS,
            '''Dynamic Template PBR configuration''',
            False, 
            [
            _MetaInfoClassMember('service-policies', REFERENCE_CLASS, 'ServicePolicies', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg', 'DynamicTemplate.SubscriberServices.SubscriberService.Pbr.ServicePolicies',
                [], [],
                '''                Ingress service policy
                ''',
                'service_policies',
                'Cisco-IOS-XR-pbr-subscriber-cfg', False),
            _MetaInfoClassMember('service-policy-in', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                Class for subscriber ingress policy
                ''',
                'service_policy_in',
                'Cisco-IOS-XR-pbr-subscriber-cfg', False),
            ],
            'Cisco-IOS-XR-pbr-subscriber-cfg',
            'pbr',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-pbr-subscriber-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg',
        ),
    },
    'DynamicTemplate.SubscriberServices.SubscriberService.Ipv4PacketFilter.Outbound' : {
        'meta_info' : _MetaInfoClass('DynamicTemplate.SubscriberServices.SubscriberService.Ipv4PacketFilter.Outbound', REFERENCE_CLASS,
            '''IPv4 Packet filter to be applied to outbound
packets''',
            False, 
            [
            _MetaInfoClassMember('common-acl-name', ATTRIBUTE, 'str', 'xr:Cisco-ios-xr-string',
                None, None,
                [(1, 64)], [],
                '''                Not supported (Leave unspecified).
                ''',
                'common_acl_name',
                'Cisco-IOS-XR-ip-pfilter-subscriber-cfg', False),
            _MetaInfoClassMember('name', ATTRIBUTE, 'str', 'xr:Cisco-ios-xr-string',
                None, None,
                [(1, 64)], [],
                '''                IPv4 Packet Filter Name to be applied to
                Outbound packets.
                ''',
                'name',
                'Cisco-IOS-XR-ip-pfilter-subscriber-cfg', False),
            _MetaInfoClassMember('hardware-count', ATTRIBUTE, 'Empty', 'empty',
                None, None,
                [], [],
                '''                Not supported (Leave unspecified).
                ''',
                'hardware_count',
                'Cisco-IOS-XR-ip-pfilter-subscriber-cfg', False),
            _MetaInfoClassMember('interface-statistics', ATTRIBUTE, 'Empty', 'empty',
                None, None,
                [], [],
                '''                Not supported (Leave unspecified).
                ''',
                'interface_statistics',
                'Cisco-IOS-XR-ip-pfilter-subscriber-cfg', False),
            ],
            'Cisco-IOS-XR-ip-pfilter-subscriber-cfg',
            'outbound',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-ip-pfilter-subscriber-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg',
        ),
    },
    'DynamicTemplate.SubscriberServices.SubscriberService.Ipv4PacketFilter.Inbound' : {
        'meta_info' : _MetaInfoClass('DynamicTemplate.SubscriberServices.SubscriberService.Ipv4PacketFilter.Inbound', REFERENCE_CLASS,
            '''IPv4 Packet filter to be applied to inbound
packets''',
            False, 
            [
            _MetaInfoClassMember('common-acl-name', ATTRIBUTE, 'str', 'xr:Cisco-ios-xr-string',
                None, None,
                [(1, 64)], [],
                '''                Not supported (Leave unspecified).
                ''',
                'common_acl_name',
                'Cisco-IOS-XR-ip-pfilter-subscriber-cfg', False),
            _MetaInfoClassMember('name', ATTRIBUTE, 'str', 'xr:Cisco-ios-xr-string',
                None, None,
                [(1, 64)], [],
                '''                IPv4 Packet Filter Name to be applied to
                Inbound packets NOTE: This parameter is
                mandatory if 'CommonACLName' is not specified.
                ''',
                'name',
                'Cisco-IOS-XR-ip-pfilter-subscriber-cfg', False),
            _MetaInfoClassMember('hardware-count', ATTRIBUTE, 'Empty', 'empty',
                None, None,
                [], [],
                '''                Not supported (Leave unspecified).
                ''',
                'hardware_count',
                'Cisco-IOS-XR-ip-pfilter-subscriber-cfg', False),
            _MetaInfoClassMember('interface-statistics', ATTRIBUTE, 'Empty', 'empty',
                None, None,
                [], [],
                '''                Not supported (Leave unspecified).
                ''',
                'interface_statistics',
                'Cisco-IOS-XR-ip-pfilter-subscriber-cfg', False),
            ],
            'Cisco-IOS-XR-ip-pfilter-subscriber-cfg',
            'inbound',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-ip-pfilter-subscriber-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg',
        ),
    },
    'DynamicTemplate.SubscriberServices.SubscriberService.Ipv4PacketFilter' : {
        'meta_info' : _MetaInfoClass('DynamicTemplate.SubscriberServices.SubscriberService.Ipv4PacketFilter', REFERENCE_CLASS,
            '''IPv4 Packet Filtering configuration for the
template''',
            False, 
            [
            _MetaInfoClassMember('outbound', REFERENCE_CLASS, 'Outbound', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg', 'DynamicTemplate.SubscriberServices.SubscriberService.Ipv4PacketFilter.Outbound',
                [], [],
                '''                IPv4 Packet filter to be applied to outbound
                packets
                ''',
                'outbound',
                'Cisco-IOS-XR-ip-pfilter-subscriber-cfg', False),
            _MetaInfoClassMember('inbound', REFERENCE_CLASS, 'Inbound', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg', 'DynamicTemplate.SubscriberServices.SubscriberService.Ipv4PacketFilter.Inbound',
                [], [],
                '''                IPv4 Packet filter to be applied to inbound
                packets
                ''',
                'inbound',
                'Cisco-IOS-XR-ip-pfilter-subscriber-cfg', False),
            ],
            'Cisco-IOS-XR-ip-pfilter-subscriber-cfg',
            'ipv4-packet-filter',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-ip-pfilter-subscriber-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg',
        ),
    },
    'DynamicTemplate.SubscriberServices.SubscriberService.Ipv6PacketFilter.Inbound' : {
        'meta_info' : _MetaInfoClass('DynamicTemplate.SubscriberServices.SubscriberService.Ipv6PacketFilter.Inbound', REFERENCE_CLASS,
            '''IPv6 Packet filter to be applied to inbound
packets''',
            False, 
            [
            _MetaInfoClassMember('common-acl-name', ATTRIBUTE, 'str', 'xr:Cisco-ios-xr-string',
                None, None,
                [(1, 64)], [],
                '''                Not supported (Leave unspecified).
                ''',
                'common_acl_name',
                'Cisco-IOS-XR-ip-pfilter-subscriber-cfg', False),
            _MetaInfoClassMember('name', ATTRIBUTE, 'str', 'xr:Cisco-ios-xr-string',
                None, None,
                [(1, 64)], [],
                '''                IPv6 Packet Filter Name to be applied to
                Inbound  NOTE: This parameter is mandatory if
                'CommonACLName' is not specified.
                ''',
                'name',
                'Cisco-IOS-XR-ip-pfilter-subscriber-cfg', False),
            _MetaInfoClassMember('interface-statistics', ATTRIBUTE, 'Empty', 'empty',
                None, None,
                [], [],
                '''                Not supported (Leave unspecified).
                ''',
                'interface_statistics',
                'Cisco-IOS-XR-ip-pfilter-subscriber-cfg', False),
            ],
            'Cisco-IOS-XR-ip-pfilter-subscriber-cfg',
            'inbound',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-ip-pfilter-subscriber-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg',
        ),
    },
    'DynamicTemplate.SubscriberServices.SubscriberService.Ipv6PacketFilter.Outbound' : {
        'meta_info' : _MetaInfoClass('DynamicTemplate.SubscriberServices.SubscriberService.Ipv6PacketFilter.Outbound', REFERENCE_CLASS,
            '''IPv6 Packet filter to be applied to outbound
packets''',
            False, 
            [
            _MetaInfoClassMember('common-acl-name', ATTRIBUTE, 'str', 'xr:Cisco-ios-xr-string',
                None, None,
                [(1, 64)], [],
                '''                Not supported (Leave unspecified).
                ''',
                'common_acl_name',
                'Cisco-IOS-XR-ip-pfilter-subscriber-cfg', False),
            _MetaInfoClassMember('name', ATTRIBUTE, 'str', 'xr:Cisco-ios-xr-string',
                None, None,
                [(1, 64)], [],
                '''                IPv6 Packet Filter Name to be applied to
                Outbound packets.
                ''',
                'name',
                'Cisco-IOS-XR-ip-pfilter-subscriber-cfg', False),
            _MetaInfoClassMember('interface-statistics', ATTRIBUTE, 'Empty', 'empty',
                None, None,
                [], [],
                '''                Not supported (Leave unspecified).
                ''',
                'interface_statistics',
                'Cisco-IOS-XR-ip-pfilter-subscriber-cfg', False),
            ],
            'Cisco-IOS-XR-ip-pfilter-subscriber-cfg',
            'outbound',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-ip-pfilter-subscriber-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg',
        ),
    },
    'DynamicTemplate.SubscriberServices.SubscriberService.Ipv6PacketFilter' : {
        'meta_info' : _MetaInfoClass('DynamicTemplate.SubscriberServices.SubscriberService.Ipv6PacketFilter', REFERENCE_CLASS,
            '''IPv6 Packet Filtering configuration for the
interface''',
            False, 
            [
            _MetaInfoClassMember('inbound', REFERENCE_CLASS, 'Inbound', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg', 'DynamicTemplate.SubscriberServices.SubscriberService.Ipv6PacketFilter.Inbound',
                [], [],
                '''                IPv6 Packet filter to be applied to inbound
                packets
                ''',
                'inbound',
                'Cisco-IOS-XR-ip-pfilter-subscriber-cfg', False),
            _MetaInfoClassMember('outbound', REFERENCE_CLASS, 'Outbound', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg', 'DynamicTemplate.SubscriberServices.SubscriberService.Ipv6PacketFilter.Outbound',
                [], [],
                '''                IPv6 Packet filter to be applied to outbound
                packets
                ''',
                'outbound',
                'Cisco-IOS-XR-ip-pfilter-subscriber-cfg', False),
            ],
            'Cisco-IOS-XR-ip-pfilter-subscriber-cfg',
            'ipv6-packet-filter',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-ip-pfilter-subscriber-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg',
        ),
    },
    'DynamicTemplate.SubscriberServices.SubscriberService' : {
        'meta_info' : _MetaInfoClass('DynamicTemplate.SubscriberServices.SubscriberService', REFERENCE_LIST,
            '''A Service Type Template ''',
            False, 
            [
            _MetaInfoClassMember('template-name', ATTRIBUTE, 'str', 'xr:Cisco-ios-xr-string',
                None, None,
                [], [b'[\\w\\-\\.:,_@#%$\\+=\\|;]+'],
                '''                The name of the template
                ''',
                'template_name',
                'Cisco-IOS-XR-subscriber-infra-tmplmgr-cfg', True),
            _MetaInfoClassMember('ipv4-network', REFERENCE_CLASS, 'Ipv4Network', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg', 'DynamicTemplate.SubscriberServices.SubscriberService.Ipv4Network',
                [], [],
                '''                Interface IPv4 Network configuration data
                ''',
                'ipv4_network',
                'Cisco-IOS-XR-ipv4-ma-subscriber-cfg', False),
            _MetaInfoClassMember('subscriber-attribute', REFERENCE_CLASS, 'SubscriberAttribute', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg', 'DynamicTemplate.SubscriberServices.SubscriberService.SubscriberAttribute',
                [], [],
                '''                Subscriber attribute configuration data
                ''',
                'subscriber_attribute',
                'Cisco-IOS-XR-opendns-deviceid-cfg', False),
            _MetaInfoClassMember('accounting', REFERENCE_CLASS, 'Accounting', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg', 'DynamicTemplate.SubscriberServices.SubscriberService.Accounting',
                [], [],
                '''                Subscriber accounting dynamic-template commands
                ''',
                'accounting',
                'Cisco-IOS-XR-subscriber-accounting-cfg', False),
            _MetaInfoClassMember('qos', REFERENCE_CLASS, 'Qos', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg', 'DynamicTemplate.SubscriberServices.SubscriberService.Qos',
                [], [],
                '''                QoS dynamically applied configuration template
                ''',
                'qos',
                'Cisco-IOS-XR-qos-ma-bng-cfg', False),
            _MetaInfoClassMember('ipv6-network', REFERENCE_CLASS, 'Ipv6Network', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg', 'DynamicTemplate.SubscriberServices.SubscriberService.Ipv6Network',
                [], [],
                '''                Interface IPv6 Network configuration data
                ''',
                'ipv6_network',
                'Cisco-IOS-XR-ipv6-ma-subscriber-cfg', False),
            _MetaInfoClassMember('span-monitor-sessions', REFERENCE_CLASS, 'SpanMonitorSessions', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg', 'DynamicTemplate.SubscriberServices.SubscriberService.SpanMonitorSessions',
                [], [],
                '''                Monitor Session container for this template
                ''',
                'span_monitor_sessions',
                'Cisco-IOS-XR-Ethernet-SPAN-subscriber-cfg', False),
            _MetaInfoClassMember('vrf', ATTRIBUTE, 'str', 'xr:Cisco-ios-xr-string',
                None, None,
                [(1, 32)], [],
                '''                Assign the interface to a VRF 
                ''',
                'vrf',
                'Cisco-IOS-XR-infra-rsi-subscriber-cfg', False),
            _MetaInfoClassMember('ipv6-neighbor', REFERENCE_CLASS, 'Ipv6Neighbor', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg', 'DynamicTemplate.SubscriberServices.SubscriberService.Ipv6Neighbor',
                [], [],
                '''                Interface IPv6 Network configuration data
                ''',
                'ipv6_neighbor',
                'Cisco-IOS-XR-ipv6-nd-subscriber-cfg', False),
            _MetaInfoClassMember('pbr', REFERENCE_CLASS, 'Pbr', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg', 'DynamicTemplate.SubscriberServices.SubscriberService.Pbr',
                [], [],
                '''                Dynamic Template PBR configuration
                ''',
                'pbr',
                'Cisco-IOS-XR-pbr-subscriber-cfg', False),
            _MetaInfoClassMember('ipv4-packet-filter', REFERENCE_CLASS, 'Ipv4PacketFilter', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg', 'DynamicTemplate.SubscriberServices.SubscriberService.Ipv4PacketFilter',
                [], [],
                '''                IPv4 Packet Filtering configuration for the
                template
                ''',
                'ipv4_packet_filter',
                'Cisco-IOS-XR-ip-pfilter-subscriber-cfg', False),
            _MetaInfoClassMember('ipv6-packet-filter', REFERENCE_CLASS, 'Ipv6PacketFilter', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg', 'DynamicTemplate.SubscriberServices.SubscriberService.Ipv6PacketFilter',
                [], [],
                '''                IPv6 Packet Filtering configuration for the
                interface
                ''',
                'ipv6_packet_filter',
                'Cisco-IOS-XR-ip-pfilter-subscriber-cfg', False),
            ],
            'Cisco-IOS-XR-subscriber-infra-tmplmgr-cfg',
            'subscriber-service',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-subscriber-infra-tmplmgr-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg',
        ),
    },
    'DynamicTemplate.SubscriberServices' : {
        'meta_info' : _MetaInfoClass('DynamicTemplate.SubscriberServices', REFERENCE_CLASS,
            '''The Service Type Template Table''',
            False, 
            [
            _MetaInfoClassMember('subscriber-service', REFERENCE_LIST, 'SubscriberService', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg', 'DynamicTemplate.SubscriberServices.SubscriberService',
                [], [],
                '''                A Service Type Template 
                ''',
                'subscriber_service',
                'Cisco-IOS-XR-subscriber-infra-tmplmgr-cfg', False),
            ],
            'Cisco-IOS-XR-subscriber-infra-tmplmgr-cfg',
            'subscriber-services',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-subscriber-infra-tmplmgr-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg',
        ),
    },
    'DynamicTemplate' : {
        'meta_info' : _MetaInfoClass('DynamicTemplate', REFERENCE_CLASS,
            '''All dynamic template configurations''',
            False, 
            [
            _MetaInfoClassMember('ppps', REFERENCE_CLASS, 'Ppps', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg', 'DynamicTemplate.Ppps',
                [], [],
                '''                Templates of the PPP Type
                ''',
                'ppps',
                'Cisco-IOS-XR-subscriber-infra-tmplmgr-cfg', False),
            _MetaInfoClassMember('ip-subscribers', REFERENCE_CLASS, 'IpSubscribers', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg', 'DynamicTemplate.IpSubscribers',
                [], [],
                '''                The IP Subscriber Template Table
                ''',
                'ip_subscribers',
                'Cisco-IOS-XR-subscriber-infra-tmplmgr-cfg', False),
            _MetaInfoClassMember('subscriber-services', REFERENCE_CLASS, 'SubscriberServices', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg', 'DynamicTemplate.SubscriberServices',
                [], [],
                '''                The Service Type Template Table
                ''',
                'subscriber_services',
                'Cisco-IOS-XR-subscriber-infra-tmplmgr-cfg', False),
            ],
            'Cisco-IOS-XR-subscriber-infra-tmplmgr-cfg',
            'dynamic-template',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-subscriber-infra-tmplmgr-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg',
        ),
    },
}
_meta_table['DynamicTemplate.Ppps.Ppp.Accounting.IdleTimeout']['meta_info'].parent =_meta_table['DynamicTemplate.Ppps.Ppp.Accounting']['meta_info']
_meta_table['DynamicTemplate.Ppps.Ppp.Accounting.Session']['meta_info'].parent =_meta_table['DynamicTemplate.Ppps.Ppp.Accounting']['meta_info']
_meta_table['DynamicTemplate.Ppps.Ppp.Accounting.ServiceAccounting']['meta_info'].parent =_meta_table['DynamicTemplate.Ppps.Ppp.Accounting']['meta_info']
_meta_table['DynamicTemplate.Ppps.Ppp.Qos.ServicePolicy.Input']['meta_info'].parent =_meta_table['DynamicTemplate.Ppps.Ppp.Qos.ServicePolicy']['meta_info']
_meta_table['DynamicTemplate.Ppps.Ppp.Qos.ServicePolicy.Output']['meta_info'].parent =_meta_table['DynamicTemplate.Ppps.Ppp.Qos.ServicePolicy']['meta_info']
_meta_table['DynamicTemplate.Ppps.Ppp.Qos.ServicePolicy']['meta_info'].parent =_meta_table['DynamicTemplate.Ppps.Ppp.Qos']['meta_info']
_meta_table['DynamicTemplate.Ppps.Ppp.Qos.Account']['meta_info'].parent =_meta_table['DynamicTemplate.Ppps.Ppp.Qos']['meta_info']
_meta_table['DynamicTemplate.Ppps.Ppp.Qos.Output']['meta_info'].parent =_meta_table['DynamicTemplate.Ppps.Ppp.Qos']['meta_info']
_meta_table['DynamicTemplate.Ppps.Ppp.Igmp.DefaultVrf.ExplicitTracking']['meta_info'].parent =_meta_table['DynamicTemplate.Ppps.Ppp.Igmp.DefaultVrf']['meta_info']
_meta_table['DynamicTemplate.Ppps.Ppp.Igmp.DefaultVrf']['meta_info'].parent =_meta_table['DynamicTemplate.Ppps.Ppp.Igmp']['meta_info']
_meta_table['DynamicTemplate.Ppps.Ppp.Ipv6Network.Addresses.AutoConfiguration']['meta_info'].parent =_meta_table['DynamicTemplate.Ppps.Ppp.Ipv6Network.Addresses']['meta_info']
_meta_table['DynamicTemplate.Ppps.Ppp.Ipv6Network.Addresses']['meta_info'].parent =_meta_table['DynamicTemplate.Ppps.Ppp.Ipv6Network']['meta_info']
_meta_table['DynamicTemplate.Ppps.Ppp.SpanMonitorSessions.SpanMonitorSession.Attachment']['meta_info'].parent =_meta_table['DynamicTemplate.Ppps.Ppp.SpanMonitorSessions.SpanMonitorSession']['meta_info']
_meta_table['DynamicTemplate.Ppps.Ppp.SpanMonitorSessions.SpanMonitorSession.Acl']['meta_info'].parent =_meta_table['DynamicTemplate.Ppps.Ppp.SpanMonitorSessions.SpanMonitorSession']['meta_info']
_meta_table['DynamicTemplate.Ppps.Ppp.SpanMonitorSessions.SpanMonitorSession']['meta_info'].parent =_meta_table['DynamicTemplate.Ppps.Ppp.SpanMonitorSessions']['meta_info']
_meta_table['DynamicTemplate.Ppps.Ppp.Ipv6Neighbor.RaInterval']['meta_info'].parent =_meta_table['DynamicTemplate.Ppps.Ppp.Ipv6Neighbor']['meta_info']
_meta_table['DynamicTemplate.Ppps.Ppp.Ipv6Neighbor.FramedPrefix']['meta_info'].parent =_meta_table['DynamicTemplate.Ppps.Ppp.Ipv6Neighbor']['meta_info']
_meta_table['DynamicTemplate.Ppps.Ppp.Ipv6Neighbor.DuplicateAddressDetection']['meta_info'].parent =_meta_table['DynamicTemplate.Ppps.Ppp.Ipv6Neighbor']['meta_info']
_meta_table['DynamicTemplate.Ppps.Ppp.Ipv6Neighbor.RaInitial']['meta_info'].parent =_meta_table['DynamicTemplate.Ppps.Ppp.Ipv6Neighbor']['meta_info']
_meta_table['DynamicTemplate.Ppps.Ppp.PppTemplate.Lcp.Authentication.Methods']['meta_info'].parent =_meta_table['DynamicTemplate.Ppps.Ppp.PppTemplate.Lcp.Authentication']['meta_info']
_meta_table['DynamicTemplate.Ppps.Ppp.PppTemplate.Lcp.AbsoluteTimeout']['meta_info'].parent =_meta_table['DynamicTemplate.Ppps.Ppp.PppTemplate.Lcp']['meta_info']
_meta_table['DynamicTemplate.Ppps.Ppp.PppTemplate.Lcp.Delay']['meta_info'].parent =_meta_table['DynamicTemplate.Ppps.Ppp.PppTemplate.Lcp']['meta_info']
_meta_table['DynamicTemplate.Ppps.Ppp.PppTemplate.Lcp.Authentication']['meta_info'].parent =_meta_table['DynamicTemplate.Ppps.Ppp.PppTemplate.Lcp']['meta_info']
_meta_table['DynamicTemplate.Ppps.Ppp.PppTemplate.Lcp.Keepalive']['meta_info'].parent =_meta_table['DynamicTemplate.Ppps.Ppp.PppTemplate.Lcp']['meta_info']
_meta_table['DynamicTemplate.Ppps.Ppp.PppTemplate.Ipcp.Wins.WinsAddresses']['meta_info'].parent =_meta_table['DynamicTemplate.Ppps.Ppp.PppTemplate.Ipcp.Wins']['meta_info']
_meta_table['DynamicTemplate.Ppps.Ppp.PppTemplate.Ipcp.Dns.DnsAddresses']['meta_info'].parent =_meta_table['DynamicTemplate.Ppps.Ppp.PppTemplate.Ipcp.Dns']['meta_info']
_meta_table['DynamicTemplate.Ppps.Ppp.PppTemplate.Ipcp.Wins']['meta_info'].parent =_meta_table['DynamicTemplate.Ppps.Ppp.PppTemplate.Ipcp']['meta_info']
_meta_table['DynamicTemplate.Ppps.Ppp.PppTemplate.Ipcp.Dns']['meta_info'].parent =_meta_table['DynamicTemplate.Ppps.Ppp.PppTemplate.Ipcp']['meta_info']
_meta_table['DynamicTemplate.Ppps.Ppp.PppTemplate.Ipcp.PeerAddress']['meta_info'].parent =_meta_table['DynamicTemplate.Ppps.Ppp.PppTemplate.Ipcp']['meta_info']
_meta_table['DynamicTemplate.Ppps.Ppp.PppTemplate.Fsm']['meta_info'].parent =_meta_table['DynamicTemplate.Ppps.Ppp.PppTemplate']['meta_info']
_meta_table['DynamicTemplate.Ppps.Ppp.PppTemplate.Lcp']['meta_info'].parent =_meta_table['DynamicTemplate.Ppps.Ppp.PppTemplate']['meta_info']
_meta_table['DynamicTemplate.Ppps.Ppp.PppTemplate.Ipv6cp']['meta_info'].parent =_meta_table['DynamicTemplate.Ppps.Ppp.PppTemplate']['meta_info']
_meta_table['DynamicTemplate.Ppps.Ppp.PppTemplate.Ipcp']['meta_info'].parent =_meta_table['DynamicTemplate.Ppps.Ppp.PppTemplate']['meta_info']
_meta_table['DynamicTemplate.Ppps.Ppp.Pbr.ServicePolicies.ServicePolicy']['meta_info'].parent =_meta_table['DynamicTemplate.Ppps.Ppp.Pbr.ServicePolicies']['meta_info']
_meta_table['DynamicTemplate.Ppps.Ppp.Pbr.ServicePolicies']['meta_info'].parent =_meta_table['DynamicTemplate.Ppps.Ppp.Pbr']['meta_info']
_meta_table['DynamicTemplate.Ppps.Ppp.Ipv4PacketFilter.Outbound']['meta_info'].parent =_meta_table['DynamicTemplate.Ppps.Ppp.Ipv4PacketFilter']['meta_info']
_meta_table['DynamicTemplate.Ppps.Ppp.Ipv4PacketFilter.Inbound']['meta_info'].parent =_meta_table['DynamicTemplate.Ppps.Ppp.Ipv4PacketFilter']['meta_info']
_meta_table['DynamicTemplate.Ppps.Ppp.Ipv6PacketFilter.Inbound']['meta_info'].parent =_meta_table['DynamicTemplate.Ppps.Ppp.Ipv6PacketFilter']['meta_info']
_meta_table['DynamicTemplate.Ppps.Ppp.Ipv6PacketFilter.Outbound']['meta_info'].parent =_meta_table['DynamicTemplate.Ppps.Ppp.Ipv6PacketFilter']['meta_info']
_meta_table['DynamicTemplate.Ppps.Ppp.Dhcpv6.DelegatedPrefix']['meta_info'].parent =_meta_table['DynamicTemplate.Ppps.Ppp.Dhcpv6']['meta_info']
_meta_table['DynamicTemplate.Ppps.Ppp.Ipv4Network']['meta_info'].parent =_meta_table['DynamicTemplate.Ppps.Ppp']['meta_info']
_meta_table['DynamicTemplate.Ppps.Ppp.Accounting']['meta_info'].parent =_meta_table['DynamicTemplate.Ppps.Ppp']['meta_info']
_meta_table['DynamicTemplate.Ppps.Ppp.Qos']['meta_info'].parent =_meta_table['DynamicTemplate.Ppps.Ppp']['meta_info']
_meta_table['DynamicTemplate.Ppps.Ppp.Igmp']['meta_info'].parent =_meta_table['DynamicTemplate.Ppps.Ppp']['meta_info']
_meta_table['DynamicTemplate.Ppps.Ppp.Ipv6Network']['meta_info'].parent =_meta_table['DynamicTemplate.Ppps.Ppp']['meta_info']
_meta_table['DynamicTemplate.Ppps.Ppp.PppoeTemplate']['meta_info'].parent =_meta_table['DynamicTemplate.Ppps.Ppp']['meta_info']
_meta_table['DynamicTemplate.Ppps.Ppp.SpanMonitorSessions']['meta_info'].parent =_meta_table['DynamicTemplate.Ppps.Ppp']['meta_info']
_meta_table['DynamicTemplate.Ppps.Ppp.Ipv6Neighbor']['meta_info'].parent =_meta_table['DynamicTemplate.Ppps.Ppp']['meta_info']
_meta_table['DynamicTemplate.Ppps.Ppp.PppTemplate']['meta_info'].parent =_meta_table['DynamicTemplate.Ppps.Ppp']['meta_info']
_meta_table['DynamicTemplate.Ppps.Ppp.Pbr']['meta_info'].parent =_meta_table['DynamicTemplate.Ppps.Ppp']['meta_info']
_meta_table['DynamicTemplate.Ppps.Ppp.Ipv4PacketFilter']['meta_info'].parent =_meta_table['DynamicTemplate.Ppps.Ppp']['meta_info']
_meta_table['DynamicTemplate.Ppps.Ppp.Ipv6PacketFilter']['meta_info'].parent =_meta_table['DynamicTemplate.Ppps.Ppp']['meta_info']
_meta_table['DynamicTemplate.Ppps.Ppp.Dhcpv6']['meta_info'].parent =_meta_table['DynamicTemplate.Ppps.Ppp']['meta_info']
_meta_table['DynamicTemplate.Ppps.Ppp']['meta_info'].parent =_meta_table['DynamicTemplate.Ppps']['meta_info']
_meta_table['DynamicTemplate.IpSubscribers.IpSubscriber.Accounting.ServiceAccounting']['meta_info'].parent =_meta_table['DynamicTemplate.IpSubscribers.IpSubscriber.Accounting']['meta_info']
_meta_table['DynamicTemplate.IpSubscribers.IpSubscriber.Accounting.Session']['meta_info'].parent =_meta_table['DynamicTemplate.IpSubscribers.IpSubscriber.Accounting']['meta_info']
_meta_table['DynamicTemplate.IpSubscribers.IpSubscriber.Accounting.IdleTimeout']['meta_info'].parent =_meta_table['DynamicTemplate.IpSubscribers.IpSubscriber.Accounting']['meta_info']
_meta_table['DynamicTemplate.IpSubscribers.IpSubscriber.Qos.ServicePolicy.Input']['meta_info'].parent =_meta_table['DynamicTemplate.IpSubscribers.IpSubscriber.Qos.ServicePolicy']['meta_info']
_meta_table['DynamicTemplate.IpSubscribers.IpSubscriber.Qos.ServicePolicy.Output']['meta_info'].parent =_meta_table['DynamicTemplate.IpSubscribers.IpSubscriber.Qos.ServicePolicy']['meta_info']
_meta_table['DynamicTemplate.IpSubscribers.IpSubscriber.Qos.ServicePolicy']['meta_info'].parent =_meta_table['DynamicTemplate.IpSubscribers.IpSubscriber.Qos']['meta_info']
_meta_table['DynamicTemplate.IpSubscribers.IpSubscriber.Qos.Account']['meta_info'].parent =_meta_table['DynamicTemplate.IpSubscribers.IpSubscriber.Qos']['meta_info']
_meta_table['DynamicTemplate.IpSubscribers.IpSubscriber.Qos.Output']['meta_info'].parent =_meta_table['DynamicTemplate.IpSubscribers.IpSubscriber.Qos']['meta_info']
_meta_table['DynamicTemplate.IpSubscribers.IpSubscriber.Igmp.DefaultVrf.ExplicitTracking']['meta_info'].parent =_meta_table['DynamicTemplate.IpSubscribers.IpSubscriber.Igmp.DefaultVrf']['meta_info']
_meta_table['DynamicTemplate.IpSubscribers.IpSubscriber.Igmp.DefaultVrf']['meta_info'].parent =_meta_table['DynamicTemplate.IpSubscribers.IpSubscriber.Igmp']['meta_info']
_meta_table['DynamicTemplate.IpSubscribers.IpSubscriber.Ipv6Network.Addresses.AutoConfiguration']['meta_info'].parent =_meta_table['DynamicTemplate.IpSubscribers.IpSubscriber.Ipv6Network.Addresses']['meta_info']
_meta_table['DynamicTemplate.IpSubscribers.IpSubscriber.Ipv6Network.Addresses']['meta_info'].parent =_meta_table['DynamicTemplate.IpSubscribers.IpSubscriber.Ipv6Network']['meta_info']
_meta_table['DynamicTemplate.IpSubscribers.IpSubscriber.SpanMonitorSessions.SpanMonitorSession.Attachment']['meta_info'].parent =_meta_table['DynamicTemplate.IpSubscribers.IpSubscriber.SpanMonitorSessions.SpanMonitorSession']['meta_info']
_meta_table['DynamicTemplate.IpSubscribers.IpSubscriber.SpanMonitorSessions.SpanMonitorSession.Acl']['meta_info'].parent =_meta_table['DynamicTemplate.IpSubscribers.IpSubscriber.SpanMonitorSessions.SpanMonitorSession']['meta_info']
_meta_table['DynamicTemplate.IpSubscribers.IpSubscriber.SpanMonitorSessions.SpanMonitorSession']['meta_info'].parent =_meta_table['DynamicTemplate.IpSubscribers.IpSubscriber.SpanMonitorSessions']['meta_info']
_meta_table['DynamicTemplate.IpSubscribers.IpSubscriber.Ipv6Neighbor.RaInterval']['meta_info'].parent =_meta_table['DynamicTemplate.IpSubscribers.IpSubscriber.Ipv6Neighbor']['meta_info']
_meta_table['DynamicTemplate.IpSubscribers.IpSubscriber.Ipv6Neighbor.FramedPrefix']['meta_info'].parent =_meta_table['DynamicTemplate.IpSubscribers.IpSubscriber.Ipv6Neighbor']['meta_info']
_meta_table['DynamicTemplate.IpSubscribers.IpSubscriber.Ipv6Neighbor.DuplicateAddressDetection']['meta_info'].parent =_meta_table['DynamicTemplate.IpSubscribers.IpSubscriber.Ipv6Neighbor']['meta_info']
_meta_table['DynamicTemplate.IpSubscribers.IpSubscriber.Ipv6Neighbor.RaInitial']['meta_info'].parent =_meta_table['DynamicTemplate.IpSubscribers.IpSubscriber.Ipv6Neighbor']['meta_info']
_meta_table['DynamicTemplate.IpSubscribers.IpSubscriber.Pbr.ServicePolicies.ServicePolicy']['meta_info'].parent =_meta_table['DynamicTemplate.IpSubscribers.IpSubscriber.Pbr.ServicePolicies']['meta_info']
_meta_table['DynamicTemplate.IpSubscribers.IpSubscriber.Pbr.ServicePolicies']['meta_info'].parent =_meta_table['DynamicTemplate.IpSubscribers.IpSubscriber.Pbr']['meta_info']
_meta_table['DynamicTemplate.IpSubscribers.IpSubscriber.Ipv4PacketFilter.Outbound']['meta_info'].parent =_meta_table['DynamicTemplate.IpSubscribers.IpSubscriber.Ipv4PacketFilter']['meta_info']
_meta_table['DynamicTemplate.IpSubscribers.IpSubscriber.Ipv4PacketFilter.Inbound']['meta_info'].parent =_meta_table['DynamicTemplate.IpSubscribers.IpSubscriber.Ipv4PacketFilter']['meta_info']
_meta_table['DynamicTemplate.IpSubscribers.IpSubscriber.Ipv6PacketFilter.Inbound']['meta_info'].parent =_meta_table['DynamicTemplate.IpSubscribers.IpSubscriber.Ipv6PacketFilter']['meta_info']
_meta_table['DynamicTemplate.IpSubscribers.IpSubscriber.Ipv6PacketFilter.Outbound']['meta_info'].parent =_meta_table['DynamicTemplate.IpSubscribers.IpSubscriber.Ipv6PacketFilter']['meta_info']
_meta_table['DynamicTemplate.IpSubscribers.IpSubscriber.Dhcpv6.DelegatedPrefix']['meta_info'].parent =_meta_table['DynamicTemplate.IpSubscribers.IpSubscriber.Dhcpv6']['meta_info']
_meta_table['DynamicTemplate.IpSubscribers.IpSubscriber.Ipv4Network']['meta_info'].parent =_meta_table['DynamicTemplate.IpSubscribers.IpSubscriber']['meta_info']
_meta_table['DynamicTemplate.IpSubscribers.IpSubscriber.Accounting']['meta_info'].parent =_meta_table['DynamicTemplate.IpSubscribers.IpSubscriber']['meta_info']
_meta_table['DynamicTemplate.IpSubscribers.IpSubscriber.Qos']['meta_info'].parent =_meta_table['DynamicTemplate.IpSubscribers.IpSubscriber']['meta_info']
_meta_table['DynamicTemplate.IpSubscribers.IpSubscriber.Igmp']['meta_info'].parent =_meta_table['DynamicTemplate.IpSubscribers.IpSubscriber']['meta_info']
_meta_table['DynamicTemplate.IpSubscribers.IpSubscriber.Ipv6Network']['meta_info'].parent =_meta_table['DynamicTemplate.IpSubscribers.IpSubscriber']['meta_info']
_meta_table['DynamicTemplate.IpSubscribers.IpSubscriber.SpanMonitorSessions']['meta_info'].parent =_meta_table['DynamicTemplate.IpSubscribers.IpSubscriber']['meta_info']
_meta_table['DynamicTemplate.IpSubscribers.IpSubscriber.Ipv6Neighbor']['meta_info'].parent =_meta_table['DynamicTemplate.IpSubscribers.IpSubscriber']['meta_info']
_meta_table['DynamicTemplate.IpSubscribers.IpSubscriber.Pbr']['meta_info'].parent =_meta_table['DynamicTemplate.IpSubscribers.IpSubscriber']['meta_info']
_meta_table['DynamicTemplate.IpSubscribers.IpSubscriber.Ipv4PacketFilter']['meta_info'].parent =_meta_table['DynamicTemplate.IpSubscribers.IpSubscriber']['meta_info']
_meta_table['DynamicTemplate.IpSubscribers.IpSubscriber.Ipv6PacketFilter']['meta_info'].parent =_meta_table['DynamicTemplate.IpSubscribers.IpSubscriber']['meta_info']
_meta_table['DynamicTemplate.IpSubscribers.IpSubscriber.Dhcpd']['meta_info'].parent =_meta_table['DynamicTemplate.IpSubscribers.IpSubscriber']['meta_info']
_meta_table['DynamicTemplate.IpSubscribers.IpSubscriber.Dhcpv6']['meta_info'].parent =_meta_table['DynamicTemplate.IpSubscribers.IpSubscriber']['meta_info']
_meta_table['DynamicTemplate.IpSubscribers.IpSubscriber']['meta_info'].parent =_meta_table['DynamicTemplate.IpSubscribers']['meta_info']
_meta_table['DynamicTemplate.SubscriberServices.SubscriberService.SubscriberAttribute.OpenDns']['meta_info'].parent =_meta_table['DynamicTemplate.SubscriberServices.SubscriberService.SubscriberAttribute']['meta_info']
_meta_table['DynamicTemplate.SubscriberServices.SubscriberService.Accounting.ServiceAccounting']['meta_info'].parent =_meta_table['DynamicTemplate.SubscriberServices.SubscriberService.Accounting']['meta_info']
_meta_table['DynamicTemplate.SubscriberServices.SubscriberService.Accounting.Session']['meta_info'].parent =_meta_table['DynamicTemplate.SubscriberServices.SubscriberService.Accounting']['meta_info']
_meta_table['DynamicTemplate.SubscriberServices.SubscriberService.Accounting.IdleTimeout']['meta_info'].parent =_meta_table['DynamicTemplate.SubscriberServices.SubscriberService.Accounting']['meta_info']
_meta_table['DynamicTemplate.SubscriberServices.SubscriberService.Qos.ServicePolicy.Input']['meta_info'].parent =_meta_table['DynamicTemplate.SubscriberServices.SubscriberService.Qos.ServicePolicy']['meta_info']
_meta_table['DynamicTemplate.SubscriberServices.SubscriberService.Qos.ServicePolicy.Output']['meta_info'].parent =_meta_table['DynamicTemplate.SubscriberServices.SubscriberService.Qos.ServicePolicy']['meta_info']
_meta_table['DynamicTemplate.SubscriberServices.SubscriberService.Qos.ServicePolicy']['meta_info'].parent =_meta_table['DynamicTemplate.SubscriberServices.SubscriberService.Qos']['meta_info']
_meta_table['DynamicTemplate.SubscriberServices.SubscriberService.Qos.Account']['meta_info'].parent =_meta_table['DynamicTemplate.SubscriberServices.SubscriberService.Qos']['meta_info']
_meta_table['DynamicTemplate.SubscriberServices.SubscriberService.Qos.Output']['meta_info'].parent =_meta_table['DynamicTemplate.SubscriberServices.SubscriberService.Qos']['meta_info']
_meta_table['DynamicTemplate.SubscriberServices.SubscriberService.Ipv6Network.Addresses.AutoConfiguration']['meta_info'].parent =_meta_table['DynamicTemplate.SubscriberServices.SubscriberService.Ipv6Network.Addresses']['meta_info']
_meta_table['DynamicTemplate.SubscriberServices.SubscriberService.Ipv6Network.Addresses']['meta_info'].parent =_meta_table['DynamicTemplate.SubscriberServices.SubscriberService.Ipv6Network']['meta_info']
_meta_table['DynamicTemplate.SubscriberServices.SubscriberService.SpanMonitorSessions.SpanMonitorSession.Attachment']['meta_info'].parent =_meta_table['DynamicTemplate.SubscriberServices.SubscriberService.SpanMonitorSessions.SpanMonitorSession']['meta_info']
_meta_table['DynamicTemplate.SubscriberServices.SubscriberService.SpanMonitorSessions.SpanMonitorSession.Acl']['meta_info'].parent =_meta_table['DynamicTemplate.SubscriberServices.SubscriberService.SpanMonitorSessions.SpanMonitorSession']['meta_info']
_meta_table['DynamicTemplate.SubscriberServices.SubscriberService.SpanMonitorSessions.SpanMonitorSession']['meta_info'].parent =_meta_table['DynamicTemplate.SubscriberServices.SubscriberService.SpanMonitorSessions']['meta_info']
_meta_table['DynamicTemplate.SubscriberServices.SubscriberService.Ipv6Neighbor.RaInterval']['meta_info'].parent =_meta_table['DynamicTemplate.SubscriberServices.SubscriberService.Ipv6Neighbor']['meta_info']
_meta_table['DynamicTemplate.SubscriberServices.SubscriberService.Ipv6Neighbor.FramedPrefix']['meta_info'].parent =_meta_table['DynamicTemplate.SubscriberServices.SubscriberService.Ipv6Neighbor']['meta_info']
_meta_table['DynamicTemplate.SubscriberServices.SubscriberService.Ipv6Neighbor.DuplicateAddressDetection']['meta_info'].parent =_meta_table['DynamicTemplate.SubscriberServices.SubscriberService.Ipv6Neighbor']['meta_info']
_meta_table['DynamicTemplate.SubscriberServices.SubscriberService.Ipv6Neighbor.RaInitial']['meta_info'].parent =_meta_table['DynamicTemplate.SubscriberServices.SubscriberService.Ipv6Neighbor']['meta_info']
_meta_table['DynamicTemplate.SubscriberServices.SubscriberService.Pbr.ServicePolicies.ServicePolicy']['meta_info'].parent =_meta_table['DynamicTemplate.SubscriberServices.SubscriberService.Pbr.ServicePolicies']['meta_info']
_meta_table['DynamicTemplate.SubscriberServices.SubscriberService.Pbr.ServicePolicies']['meta_info'].parent =_meta_table['DynamicTemplate.SubscriberServices.SubscriberService.Pbr']['meta_info']
_meta_table['DynamicTemplate.SubscriberServices.SubscriberService.Ipv4PacketFilter.Outbound']['meta_info'].parent =_meta_table['DynamicTemplate.SubscriberServices.SubscriberService.Ipv4PacketFilter']['meta_info']
_meta_table['DynamicTemplate.SubscriberServices.SubscriberService.Ipv4PacketFilter.Inbound']['meta_info'].parent =_meta_table['DynamicTemplate.SubscriberServices.SubscriberService.Ipv4PacketFilter']['meta_info']
_meta_table['DynamicTemplate.SubscriberServices.SubscriberService.Ipv6PacketFilter.Inbound']['meta_info'].parent =_meta_table['DynamicTemplate.SubscriberServices.SubscriberService.Ipv6PacketFilter']['meta_info']
_meta_table['DynamicTemplate.SubscriberServices.SubscriberService.Ipv6PacketFilter.Outbound']['meta_info'].parent =_meta_table['DynamicTemplate.SubscriberServices.SubscriberService.Ipv6PacketFilter']['meta_info']
_meta_table['DynamicTemplate.SubscriberServices.SubscriberService.Ipv4Network']['meta_info'].parent =_meta_table['DynamicTemplate.SubscriberServices.SubscriberService']['meta_info']
_meta_table['DynamicTemplate.SubscriberServices.SubscriberService.SubscriberAttribute']['meta_info'].parent =_meta_table['DynamicTemplate.SubscriberServices.SubscriberService']['meta_info']
_meta_table['DynamicTemplate.SubscriberServices.SubscriberService.Accounting']['meta_info'].parent =_meta_table['DynamicTemplate.SubscriberServices.SubscriberService']['meta_info']
_meta_table['DynamicTemplate.SubscriberServices.SubscriberService.Qos']['meta_info'].parent =_meta_table['DynamicTemplate.SubscriberServices.SubscriberService']['meta_info']
_meta_table['DynamicTemplate.SubscriberServices.SubscriberService.Ipv6Network']['meta_info'].parent =_meta_table['DynamicTemplate.SubscriberServices.SubscriberService']['meta_info']
_meta_table['DynamicTemplate.SubscriberServices.SubscriberService.SpanMonitorSessions']['meta_info'].parent =_meta_table['DynamicTemplate.SubscriberServices.SubscriberService']['meta_info']
_meta_table['DynamicTemplate.SubscriberServices.SubscriberService.Ipv6Neighbor']['meta_info'].parent =_meta_table['DynamicTemplate.SubscriberServices.SubscriberService']['meta_info']
_meta_table['DynamicTemplate.SubscriberServices.SubscriberService.Pbr']['meta_info'].parent =_meta_table['DynamicTemplate.SubscriberServices.SubscriberService']['meta_info']
_meta_table['DynamicTemplate.SubscriberServices.SubscriberService.Ipv4PacketFilter']['meta_info'].parent =_meta_table['DynamicTemplate.SubscriberServices.SubscriberService']['meta_info']
_meta_table['DynamicTemplate.SubscriberServices.SubscriberService.Ipv6PacketFilter']['meta_info'].parent =_meta_table['DynamicTemplate.SubscriberServices.SubscriberService']['meta_info']
_meta_table['DynamicTemplate.SubscriberServices.SubscriberService']['meta_info'].parent =_meta_table['DynamicTemplate.SubscriberServices']['meta_info']
_meta_table['DynamicTemplate.Ppps']['meta_info'].parent =_meta_table['DynamicTemplate']['meta_info']
_meta_table['DynamicTemplate.IpSubscribers']['meta_info'].parent =_meta_table['DynamicTemplate']['meta_info']
_meta_table['DynamicTemplate.SubscriberServices']['meta_info'].parent =_meta_table['DynamicTemplate']['meta_info']
