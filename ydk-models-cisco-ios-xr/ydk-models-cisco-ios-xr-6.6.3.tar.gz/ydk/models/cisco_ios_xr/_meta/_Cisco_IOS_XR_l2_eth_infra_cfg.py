
'''
This is auto-generated file,
which includes metadata for module Cisco_IOS_XR_l2_eth_infra_cfg
'''

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_LIST, REFERENCE_LEAFLIST, REFERENCE_BITS, REFERENCE_UNION
from ydk._core._dm_meta_info import REFERENCE_CLASS, REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, ANYXML_CLASS
from ydk._core._importer import _yang_ns

_meta_table = {
    'L2ProtocolName' : _MetaInfoEnum('L2ProtocolName',
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2_eth_infra_cfg', 'L2ProtocolName',
        '''L2 protocol name''',
        {
            'cdp':'cdp',
            'stp':'stp',
            'vtp':'vtp',
            'pvst':'pvst',
            'cpsv':'cpsv',
        }, 'Cisco-IOS-XR-l2-eth-infra-cfg', _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-l2-eth-infra-cfg']),
    'L2ProtocolMode' : _MetaInfoEnum('L2ProtocolMode',
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2_eth_infra_cfg', 'L2ProtocolMode',
        '''L2 protocol mode''',
        {
            'forward':'forward',
            'drop':'drop',
            'tunnel':'tunnel',
            'reverse-tunnel':'reverse_tunnel',
        }, 'Cisco-IOS-XR-l2-eth-infra-cfg', _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-l2-eth-infra-cfg']),
    'EgressFiltering' : _MetaInfoEnum('EgressFiltering',
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2_eth_infra_cfg', 'EgressFiltering',
        '''Egress filtering''',
        {
            'egress-filtering-type-strict':'egress_filtering_type_strict',
            'egress-filtering-type-disable':'egress_filtering_type_disable',
            'egress-filtering-type-default':'egress_filtering_type_default',
        }, 'Cisco-IOS-XR-l2-eth-infra-cfg', _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-l2-eth-infra-cfg']),
    'Filtering' : _MetaInfoEnum('Filtering',
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2_eth_infra_cfg', 'Filtering',
        '''Filtering''',
        {
            'filtering-type-dot1q':'filtering_type_dot1q',
            'filtering-type-dot1ad':'filtering_type_dot1ad',
        }, 'Cisco-IOS-XR-l2-eth-infra-cfg', _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-l2-eth-infra-cfg']),
    'EthernetFeatures.EgressFiltering' : {
        'meta_info' : _MetaInfoClass('EthernetFeatures.EgressFiltering', REFERENCE_CLASS,
            '''Egress Filtering Configuration''',
            False, 
            [
            _MetaInfoClassMember('egress-filtering-default-on', ATTRIBUTE, 'Empty', 'empty',
                None, None,
                [], [],
                '''                Whether Egress Filtering is on by default
                ''',
                'egress_filtering_default_on',
                'Cisco-IOS-XR-l2-eth-infra-cfg', False),
            ],
            'Cisco-IOS-XR-l2-eth-infra-cfg',
            'egress-filtering',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-l2-eth-infra-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2_eth_infra_cfg',
        ),
    },
    'EthernetFeatures.Cfm.TracerouteCache' : {
        'meta_info' : _MetaInfoClass('EthernetFeatures.Cfm.TracerouteCache', REFERENCE_CLASS,
            '''Traceroute Cache Configuration''',
            False, 
            [
            _MetaInfoClassMember('hold-time', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('1', '525600')], [],
                '''                Hold Time in minutes
                ''',
                'hold_time',
                'Cisco-IOS-XR-ethernet-cfm-cfg', False, default_value="100"),
            _MetaInfoClassMember('cache-size', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('1', '4294967295')], [],
                '''                Cache Size limit (number of replies)
                ''',
                'cache_size',
                'Cisco-IOS-XR-ethernet-cfm-cfg', False, default_value="100"),
            ],
            'Cisco-IOS-XR-ethernet-cfm-cfg',
            'traceroute-cache',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-ethernet-cfm-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2_eth_infra_cfg',
        ),
    },
    'EthernetFeatures.Cfm.Domains.Domain.Services.Service.Efd2' : {
        'meta_info' : _MetaInfoClass('EthernetFeatures.Cfm.Domains.Domain.Services.Service.Efd2', REFERENCE_CLASS,
            '''Enable EFD to bring down ports when MEPs
detect errors''',
            False, 
            [
            _MetaInfoClassMember('enable', ATTRIBUTE, 'Empty', 'empty',
                None, None,
                [], [],
                '''                Enable EFD
                ''',
                'enable',
                'Cisco-IOS-XR-ethernet-cfm-cfg', False, is_mandatory=True),
            _MetaInfoClassMember('protection-switching-enable', ATTRIBUTE, 'Empty', 'empty',
                None, None,
                [], [],
                '''                Enable protection switching notifications
                ''',
                'protection_switching_enable',
                'Cisco-IOS-XR-ethernet-cfm-cfg', False),
            ],
            'Cisco-IOS-XR-ethernet-cfm-cfg',
            'efd2',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-ethernet-cfm-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2_eth_infra_cfg',
            is_presence=True,
        ),
    },
    'EthernetFeatures.Cfm.Domains.Domain.Services.Service.ContinuityCheckInterval' : {
        'meta_info' : _MetaInfoClass('EthernetFeatures.Cfm.Domains.Domain.Services.Service.ContinuityCheckInterval', REFERENCE_CLASS,
            '''Continuity Check Interval and Loss
Threshold.  Configuring the interval
enables Continuity Check.''',
            False, 
            [
            _MetaInfoClassMember('ccm-interval', REFERENCE_ENUM_CLASS, 'CfmCcmInterval', 'dt1:Cfm-ccm-interval',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_datatypes', 'CfmCcmInterval',
                [], [],
                '''                CCM Interval
                ''',
                'ccm_interval',
                'Cisco-IOS-XR-ethernet-cfm-cfg', False, is_mandatory=True),
            _MetaInfoClassMember('loss-threshold', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('2', '255')], [],
                '''                Loss Threshold (default 3)
                ''',
                'loss_threshold',
                'Cisco-IOS-XR-ethernet-cfm-cfg', False),
            ],
            'Cisco-IOS-XR-ethernet-cfm-cfg',
            'continuity-check-interval',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-ethernet-cfm-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2_eth_infra_cfg',
            is_presence=True,
        ),
    },
    'EthernetFeatures.Cfm.Domains.Domain.Services.Service.MipAutoCreation' : {
        'meta_info' : _MetaInfoClass('EthernetFeatures.Cfm.Domains.Domain.Services.Service.MipAutoCreation', REFERENCE_CLASS,
            '''MIP Auto-creation Policy''',
            False, 
            [
            _MetaInfoClassMember('mip-policy', REFERENCE_ENUM_CLASS, 'CfmMipPolicy', 'Cfm-mip-policy',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_cfg', 'CfmMipPolicy',
                [], [],
                '''                MIP Auto-creation Policy
                ''',
                'mip_policy',
                'Cisco-IOS-XR-ethernet-cfm-cfg', False, is_mandatory=True),
            _MetaInfoClassMember('ccm-learning-enable', ATTRIBUTE, 'Empty', 'empty',
                None, None,
                [], [],
                '''                Enable CCM Learning at MIPs in this
                service
                ''',
                'ccm_learning_enable',
                'Cisco-IOS-XR-ethernet-cfm-cfg', False),
            ],
            'Cisco-IOS-XR-ethernet-cfm-cfg',
            'mip-auto-creation',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-ethernet-cfm-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2_eth_infra_cfg',
            is_presence=True,
        ),
    },
    'EthernetFeatures.Cfm.Domains.Domain.Services.Service.Ais.Transmission' : {
        'meta_info' : _MetaInfoClass('EthernetFeatures.Cfm.Domains.Domain.Services.Service.Ais.Transmission', REFERENCE_CLASS,
            '''AIS transmission configuration''',
            False, 
            [
            _MetaInfoClassMember('ais-interval', REFERENCE_ENUM_CLASS, 'CfmAisInterval', 'dt1:Cfm-ais-interval',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_datatypes', 'CfmAisInterval',
                [], [],
                '''                AIS Interval
                ''',
                'ais_interval',
                'Cisco-IOS-XR-ethernet-cfm-cfg', False),
            _MetaInfoClassMember('cos', ATTRIBUTE, 'int', 'dt1:Cfm-cos-bits',
                None, None,
                [('0', '7')], [],
                '''                Class of Service bits
                ''',
                'cos',
                'Cisco-IOS-XR-ethernet-cfm-cfg', False),
            ],
            'Cisco-IOS-XR-ethernet-cfm-cfg',
            'transmission',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-ethernet-cfm-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2_eth_infra_cfg',
            is_presence=True,
        ),
    },
    'EthernetFeatures.Cfm.Domains.Domain.Services.Service.Ais' : {
        'meta_info' : _MetaInfoClass('EthernetFeatures.Cfm.Domains.Domain.Services.Service.Ais', REFERENCE_CLASS,
            '''Service specific AIS configuration''',
            False, 
            [
            _MetaInfoClassMember('transmission', REFERENCE_CLASS, 'Transmission', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2_eth_infra_cfg', 'EthernetFeatures.Cfm.Domains.Domain.Services.Service.Ais.Transmission',
                [], [],
                '''                AIS transmission configuration
                ''',
                'transmission',
                'Cisco-IOS-XR-ethernet-cfm-cfg', False, is_presence=True),
            ],
            'Cisco-IOS-XR-ethernet-cfm-cfg',
            'ais',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-ethernet-cfm-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2_eth_infra_cfg',
        ),
    },
    'EthernetFeatures.Cfm.Domains.Domain.Services.Service.CrossCheck.CrossCheckMeps.CrossCheckMep' : {
        'meta_info' : _MetaInfoClass('EthernetFeatures.Cfm.Domains.Domain.Services.Service.CrossCheck.CrossCheckMeps.CrossCheckMep', REFERENCE_LIST,
            '''MEP ID and optional MAC Address for
Cross-check''',
            False, 
            [
            _MetaInfoClassMember('mep-id', ATTRIBUTE, 'int', 'dt1:Cfm-mep-id',
                None, None,
                [('1', '8191')], [],
                '''                MEP ID
                ''',
                'mep_id',
                'Cisco-IOS-XR-ethernet-cfm-cfg', True),
            _MetaInfoClassMember('enable-mac-address', ATTRIBUTE, 'Empty', 'empty',
                None, None,
                [], [],
                '''                MAC Address is specified
                ''',
                'enable_mac_address',
                'Cisco-IOS-XR-ethernet-cfm-cfg', False),
            _MetaInfoClassMember('mac-address', ATTRIBUTE, 'str', 'yang:mac-address',
                None, None,
                [], [b'[0-9a-fA-F]{2}(:[0-9a-fA-F]{2}){5}'],
                '''                MAC Address
                ''',
                'mac_address',
                'Cisco-IOS-XR-ethernet-cfm-cfg', False),
            ],
            'Cisco-IOS-XR-ethernet-cfm-cfg',
            'cross-check-mep',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-ethernet-cfm-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2_eth_infra_cfg',
        ),
    },
    'EthernetFeatures.Cfm.Domains.Domain.Services.Service.CrossCheck.CrossCheckMeps' : {
        'meta_info' : _MetaInfoClass('EthernetFeatures.Cfm.Domains.Domain.Services.Service.CrossCheck.CrossCheckMeps', REFERENCE_CLASS,
            '''Cross-check MEPs''',
            False, 
            [
            _MetaInfoClassMember('cross-check-mep', REFERENCE_LIST, 'CrossCheckMep', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2_eth_infra_cfg', 'EthernetFeatures.Cfm.Domains.Domain.Services.Service.CrossCheck.CrossCheckMeps.CrossCheckMep',
                [], [],
                '''                MEP ID and optional MAC Address for
                Cross-check
                ''',
                'cross_check_mep',
                'Cisco-IOS-XR-ethernet-cfm-cfg', False),
            ],
            'Cisco-IOS-XR-ethernet-cfm-cfg',
            'cross-check-meps',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-ethernet-cfm-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2_eth_infra_cfg',
        ),
    },
    'EthernetFeatures.Cfm.Domains.Domain.Services.Service.CrossCheck' : {
        'meta_info' : _MetaInfoClass('EthernetFeatures.Cfm.Domains.Domain.Services.Service.CrossCheck', REFERENCE_CLASS,
            '''Cross-check configuration''',
            False, 
            [
            _MetaInfoClassMember('cross-check-meps', REFERENCE_CLASS, 'CrossCheckMeps', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2_eth_infra_cfg', 'EthernetFeatures.Cfm.Domains.Domain.Services.Service.CrossCheck.CrossCheckMeps',
                [], [],
                '''                Cross-check MEPs
                ''',
                'cross_check_meps',
                'Cisco-IOS-XR-ethernet-cfm-cfg', False),
            _MetaInfoClassMember('auto', ATTRIBUTE, 'Empty', 'empty',
                None, None,
                [], [],
                '''                Enable automatic MEP cross-check
                ''',
                'auto',
                'Cisco-IOS-XR-ethernet-cfm-cfg', False),
            ],
            'Cisco-IOS-XR-ethernet-cfm-cfg',
            'cross-check',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-ethernet-cfm-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2_eth_infra_cfg',
        ),
    },
    'EthernetFeatures.Cfm.Domains.Domain.Services.Service.ServiceProperties' : {
        'meta_info' : _MetaInfoClass('EthernetFeatures.Cfm.Domains.Domain.Services.Service.ServiceProperties', REFERENCE_CLASS,
            '''Fundamental properties of the service
(maintenance association)''',
            False, 
            [
            _MetaInfoClassMember('service-type', REFERENCE_ENUM_CLASS, 'CfmService', 'Cfm-service',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_cfg', 'CfmService',
                [], [],
                '''                Type of Service
                ''',
                'service_type',
                'Cisco-IOS-XR-ethernet-cfm-cfg', False, is_mandatory=True),
            _MetaInfoClassMember('group-name', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                Bridge Group or Cross-connect Group, if
                Service Type is BridgeDomain or
                CrossConnect
                ''',
                'group_name',
                'Cisco-IOS-XR-ethernet-cfm-cfg', False),
            _MetaInfoClassMember('switching-name', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                Bridge Domain or Cross-connect name, if
                Service Type is BridgeDomain or
                CrossConnect
                ''',
                'switching_name',
                'Cisco-IOS-XR-ethernet-cfm-cfg', False),
            _MetaInfoClassMember('ce-id', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('1', '16384')], [],
                '''                Local Customer Edge Identifier
                ''',
                'ce_id',
                'Cisco-IOS-XR-ethernet-cfm-cfg', False),
            _MetaInfoClassMember('remote-ce-id', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('1', '16384')], [],
                '''                Remote Customer Edge Identifier
                ''',
                'remote_ce_id',
                'Cisco-IOS-XR-ethernet-cfm-cfg', False),
            _MetaInfoClassMember('evi', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('1', '65534')], [],
                '''                EVPN ID
                ''',
                'evi',
                'Cisco-IOS-XR-ethernet-cfm-cfg', False),
            _MetaInfoClassMember('short-ma-name-format', REFERENCE_ENUM_CLASS, 'CfmShortMaNameFormat', 'Cfm-short-ma-name-format',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_cfg', 'CfmShortMaNameFormat',
                [], [],
                '''                Short MA Name Format
                ''',
                'short_ma_name_format',
                'Cisco-IOS-XR-ethernet-cfm-cfg', False),
            _MetaInfoClassMember('short-ma-name-string', ATTRIBUTE, 'str', 'xr:Cisco-ios-xr-string',
                None, None,
                [(1, 45)], [],
                '''                String Short MA Name, if format is String
                ''',
                'short_ma_name_string',
                'Cisco-IOS-XR-ethernet-cfm-cfg', False),
            _MetaInfoClassMember('short-ma-name-number', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('0', '65535')], [],
                '''                Numeric Short MA Name, if format is VlanID
                or Number
                ''',
                'short_ma_name_number',
                'Cisco-IOS-XR-ethernet-cfm-cfg', False),
            _MetaInfoClassMember('short-ma-name-oui', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('0', '16777215')], [],
                '''                VPN OUI, if Short MA Name format is VPN_ID
                ''',
                'short_ma_name_oui',
                'Cisco-IOS-XR-ethernet-cfm-cfg', False),
            _MetaInfoClassMember('short-ma-name-vpn-index', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('0', '4294967295')], [],
                '''                VPN Index, if Short MA Name format is
                VPN_ID
                ''',
                'short_ma_name_vpn_index',
                'Cisco-IOS-XR-ethernet-cfm-cfg', False),
            _MetaInfoClassMember('short-ma-name-icc', ATTRIBUTE, 'str', 'xr:Cisco-ios-xr-string',
                None, None,
                [(1, 6)], [],
                '''                ITU Carrier Code (ICC), if format is
                ICCBased
                ''',
                'short_ma_name_icc',
                'Cisco-IOS-XR-ethernet-cfm-cfg', False),
            _MetaInfoClassMember('short-ma-name-umc', ATTRIBUTE, 'str', 'xr:Cisco-ios-xr-string',
                None, None,
                [(1, 12)], [],
                '''                Unique MEG ID Code (UMC), if format is
                ICCBased
                ''',
                'short_ma_name_umc',
                'Cisco-IOS-XR-ethernet-cfm-cfg', False),
            ],
            'Cisco-IOS-XR-ethernet-cfm-cfg',
            'service-properties',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-ethernet-cfm-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2_eth_infra_cfg',
            is_presence=True,
        ),
    },
    'EthernetFeatures.Cfm.Domains.Domain.Services.Service' : {
        'meta_info' : _MetaInfoClass('EthernetFeatures.Cfm.Domains.Domain.Services.Service', REFERENCE_LIST,
            '''Configuration for a particular Service
(Maintenance Association)''',
            False, 
            [
            _MetaInfoClassMember('service', ATTRIBUTE, 'str', 'string',
                None, None,
                [(1, 127)], [],
                '''                Service (Maintenance Association)
                ''',
                'service',
                'Cisco-IOS-XR-ethernet-cfm-cfg', True),
            _MetaInfoClassMember('efd2', REFERENCE_CLASS, 'Efd2', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2_eth_infra_cfg', 'EthernetFeatures.Cfm.Domains.Domain.Services.Service.Efd2',
                [], [],
                '''                Enable EFD to bring down ports when MEPs
                detect errors
                ''',
                'efd2',
                'Cisco-IOS-XR-ethernet-cfm-cfg', False, is_presence=True),
            _MetaInfoClassMember('continuity-check-interval', REFERENCE_CLASS, 'ContinuityCheckInterval', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2_eth_infra_cfg', 'EthernetFeatures.Cfm.Domains.Domain.Services.Service.ContinuityCheckInterval',
                [], [],
                '''                Continuity Check Interval and Loss
                Threshold.  Configuring the interval
                enables Continuity Check.
                ''',
                'continuity_check_interval',
                'Cisco-IOS-XR-ethernet-cfm-cfg', False, is_presence=True),
            _MetaInfoClassMember('mip-auto-creation', REFERENCE_CLASS, 'MipAutoCreation', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2_eth_infra_cfg', 'EthernetFeatures.Cfm.Domains.Domain.Services.Service.MipAutoCreation',
                [], [],
                '''                MIP Auto-creation Policy
                ''',
                'mip_auto_creation',
                'Cisco-IOS-XR-ethernet-cfm-cfg', False, is_presence=True),
            _MetaInfoClassMember('ais', REFERENCE_CLASS, 'Ais', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2_eth_infra_cfg', 'EthernetFeatures.Cfm.Domains.Domain.Services.Service.Ais',
                [], [],
                '''                Service specific AIS configuration
                ''',
                'ais',
                'Cisco-IOS-XR-ethernet-cfm-cfg', False),
            _MetaInfoClassMember('cross-check', REFERENCE_CLASS, 'CrossCheck', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2_eth_infra_cfg', 'EthernetFeatures.Cfm.Domains.Domain.Services.Service.CrossCheck',
                [], [],
                '''                Cross-check configuration
                ''',
                'cross_check',
                'Cisco-IOS-XR-ethernet-cfm-cfg', False),
            _MetaInfoClassMember('service-properties', REFERENCE_CLASS, 'ServiceProperties', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2_eth_infra_cfg', 'EthernetFeatures.Cfm.Domains.Domain.Services.Service.ServiceProperties',
                [], [],
                '''                Fundamental properties of the service
                (maintenance association)
                ''',
                'service_properties',
                'Cisco-IOS-XR-ethernet-cfm-cfg', False, is_presence=True),
            _MetaInfoClassMember('maximum-meps', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('2', '8190')], [],
                '''                Limit on the number of MEPs in the service
                ''',
                'maximum_meps',
                'Cisco-IOS-XR-ethernet-cfm-cfg', False, default_value="100"),
            _MetaInfoClassMember('log-cross-check-errors', ATTRIBUTE, 'Empty', 'empty',
                None, None,
                [], [],
                '''                Log Cross-check Errors detected for peer
                MEPs
                ''',
                'log_cross_check_errors',
                'Cisco-IOS-XR-ethernet-cfm-cfg', False),
            _MetaInfoClassMember('continuity-check-archive-hold-time', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('1', '65535')], [],
                '''                How long to store information for peer MEPs
                that have timed out
                ''',
                'continuity_check_archive_hold_time',
                'Cisco-IOS-XR-ethernet-cfm-cfg', False, default_value="100"),
            _MetaInfoClassMember('tags', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('1', '1')], [],
                '''                The number of tags to use when sending CFM
                packets from up MEPs in this Service
                ''',
                'tags',
                'Cisco-IOS-XR-ethernet-cfm-cfg', False),
            _MetaInfoClassMember('log-continuity-check-state-changes', ATTRIBUTE, 'Empty', 'empty',
                None, None,
                [], [],
                '''                Log peer MEPs state changes
                ''',
                'log_continuity_check_state_changes',
                'Cisco-IOS-XR-ethernet-cfm-cfg', False),
            _MetaInfoClassMember('log-efd', ATTRIBUTE, 'Empty', 'empty',
                None, None,
                [], [],
                '''                Enable logging
                ''',
                'log_efd',
                'Cisco-IOS-XR-ethernet-cfm-cfg', False),
            _MetaInfoClassMember('continuity-check-auto-traceroute', ATTRIBUTE, 'Empty', 'empty',
                None, None,
                [], [],
                '''                Automatically trigger a traceroute when a
                peer MEP times out
                ''',
                'continuity_check_auto_traceroute',
                'Cisco-IOS-XR-ethernet-cfm-cfg', False),
            _MetaInfoClassMember('log-continuity-check-errors', ATTRIBUTE, 'Empty', 'empty',
                None, None,
                [], [],
                '''                Log CCM Errors detected for peer MEPs
                ''',
                'log_continuity_check_errors',
                'Cisco-IOS-XR-ethernet-cfm-cfg', False),
            _MetaInfoClassMember('log-ais', ATTRIBUTE, 'Empty', 'empty',
                None, None,
                [], [],
                '''                Log receipt of AIS and LCK messages
                ''',
                'log_ais',
                'Cisco-IOS-XR-ethernet-cfm-cfg', False),
            ],
            'Cisco-IOS-XR-ethernet-cfm-cfg',
            'service',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-ethernet-cfm-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2_eth_infra_cfg',
        ),
    },
    'EthernetFeatures.Cfm.Domains.Domain.Services' : {
        'meta_info' : _MetaInfoClass('EthernetFeatures.Cfm.Domains.Domain.Services', REFERENCE_CLASS,
            '''Service-specific global configuration''',
            False, 
            [
            _MetaInfoClassMember('service', REFERENCE_LIST, 'Service', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2_eth_infra_cfg', 'EthernetFeatures.Cfm.Domains.Domain.Services.Service',
                [], [],
                '''                Configuration for a particular Service
                (Maintenance Association)
                ''',
                'service',
                'Cisco-IOS-XR-ethernet-cfm-cfg', False),
            ],
            'Cisco-IOS-XR-ethernet-cfm-cfg',
            'services',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-ethernet-cfm-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2_eth_infra_cfg',
        ),
    },
    'EthernetFeatures.Cfm.Domains.Domain.DomainProperties' : {
        'meta_info' : _MetaInfoClass('EthernetFeatures.Cfm.Domains.Domain.DomainProperties', REFERENCE_CLASS,
            '''Fundamental properties of the domain''',
            False, 
            [
            _MetaInfoClassMember('level', ATTRIBUTE, 'int', 'dt1:Cfm-level',
                None, None,
                [('0', '7')], [],
                '''                Maintenance Domain Level
                ''',
                'level',
                'Cisco-IOS-XR-ethernet-cfm-cfg', False),
            _MetaInfoClassMember('mdid-format', REFERENCE_ENUM_CLASS, 'CfmMdidFormat', 'Cfm-mdid-format',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_cfg', 'CfmMdidFormat',
                [], [],
                '''                Maintenance Domain ID Format
                ''',
                'mdid_format',
                'Cisco-IOS-XR-ethernet-cfm-cfg', False),
            _MetaInfoClassMember('mdid-mac-address', ATTRIBUTE, 'str', 'yang:mac-address',
                None, None,
                [], [b'[0-9a-fA-F]{2}(:[0-9a-fA-F]{2}){5}'],
                '''                MAC Address, if MDID Format is MACAddress
                ''',
                'mdid_mac_address',
                'Cisco-IOS-XR-ethernet-cfm-cfg', False, has_when=True),
            _MetaInfoClassMember('mdid-number', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('0', '65535')], [],
                '''                Unsigned 16-bit Interger, if MDID Format is
                MACAddress
                ''',
                'mdid_number',
                'Cisco-IOS-XR-ethernet-cfm-cfg', False, has_when=True),
            _MetaInfoClassMember('mdid-string', ATTRIBUTE, 'str', 'string',
                None, None,
                [(1, 43)], [],
                '''                String MDID, if MDID format is String or
                DNSLike
                ''',
                'mdid_string',
                'Cisco-IOS-XR-ethernet-cfm-cfg', False, has_when=True),
            ],
            'Cisco-IOS-XR-ethernet-cfm-cfg',
            'domain-properties',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-ethernet-cfm-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2_eth_infra_cfg',
        ),
    },
    'EthernetFeatures.Cfm.Domains.Domain' : {
        'meta_info' : _MetaInfoClass('EthernetFeatures.Cfm.Domains.Domain', REFERENCE_LIST,
            '''Configuration for a particular Maintenance
Domain''',
            False, 
            [
            _MetaInfoClassMember('domain', ATTRIBUTE, 'str', 'string',
                None, None,
                [(1, 127)], [],
                '''                Maintenance Domain
                ''',
                'domain',
                'Cisco-IOS-XR-ethernet-cfm-cfg', True),
            _MetaInfoClassMember('services', REFERENCE_CLASS, 'Services', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2_eth_infra_cfg', 'EthernetFeatures.Cfm.Domains.Domain.Services',
                [], [],
                '''                Service-specific global configuration
                ''',
                'services',
                'Cisco-IOS-XR-ethernet-cfm-cfg', False),
            _MetaInfoClassMember('domain-properties', REFERENCE_CLASS, 'DomainProperties', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2_eth_infra_cfg', 'EthernetFeatures.Cfm.Domains.Domain.DomainProperties',
                [], [],
                '''                Fundamental properties of the domain
                ''',
                'domain_properties',
                'Cisco-IOS-XR-ethernet-cfm-cfg', False),
            ],
            'Cisco-IOS-XR-ethernet-cfm-cfg',
            'domain',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-ethernet-cfm-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2_eth_infra_cfg',
        ),
    },
    'EthernetFeatures.Cfm.Domains' : {
        'meta_info' : _MetaInfoClass('EthernetFeatures.Cfm.Domains', REFERENCE_CLASS,
            '''Domain-specific global configuration''',
            False, 
            [
            _MetaInfoClassMember('domain', REFERENCE_LIST, 'Domain', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2_eth_infra_cfg', 'EthernetFeatures.Cfm.Domains.Domain',
                [], [],
                '''                Configuration for a particular Maintenance
                Domain
                ''',
                'domain',
                'Cisco-IOS-XR-ethernet-cfm-cfg', False),
            ],
            'Cisco-IOS-XR-ethernet-cfm-cfg',
            'domains',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-ethernet-cfm-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2_eth_infra_cfg',
        ),
    },
    'EthernetFeatures.Cfm' : {
        'meta_info' : _MetaInfoClass('EthernetFeatures.Cfm', REFERENCE_CLASS,
            '''CFM global configuration''',
            False, 
            [
            _MetaInfoClassMember('traceroute-cache', REFERENCE_CLASS, 'TracerouteCache', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2_eth_infra_cfg', 'EthernetFeatures.Cfm.TracerouteCache',
                [], [],
                '''                Traceroute Cache Configuration
                ''',
                'traceroute_cache',
                'Cisco-IOS-XR-ethernet-cfm-cfg', False),
            _MetaInfoClassMember('domains', REFERENCE_CLASS, 'Domains', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2_eth_infra_cfg', 'EthernetFeatures.Cfm.Domains',
                [], [],
                '''                Domain-specific global configuration
                ''',
                'domains',
                'Cisco-IOS-XR-ethernet-cfm-cfg', False),
            _MetaInfoClassMember('nv-satellite-sla-processing-disable', ATTRIBUTE, 'Empty', 'empty',
                None, None,
                [], [],
                '''                Disable processing of Ethernet SLA packets on
                nV Satellite devices
                ''',
                'nv_satellite_sla_processing_disable',
                'Cisco-IOS-XR-ethernet-cfm-cfg', False),
            ],
            'Cisco-IOS-XR-ethernet-cfm-cfg',
            'cfm',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-ethernet-cfm-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2_eth_infra_cfg',
        ),
    },
    'EthernetFeatures.EtherLinkOam.Profiles.Profile.Action' : {
        'meta_info' : _MetaInfoClass('EthernetFeatures.EtherLinkOam.Profiles.Profile.Action', REFERENCE_CLASS,
            '''Configure action parameters''',
            False, 
            [
            _MetaInfoClassMember('dying-gasp', REFERENCE_ENUM_CLASS, 'EtherLinkOamEventActionEnum', 'Ether-link-oam-event-action-enum',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_link_oam_cfg', 'EtherLinkOamEventActionEnum',
                [], [],
                '''                Action to perform when a dying gasp occurs
                ''',
                'dying_gasp',
                'Cisco-IOS-XR-ethernet-link-oam-cfg', False),
            _MetaInfoClassMember('session-up', REFERENCE_ENUM_CLASS, 'EtherLinkOamEventActionPrimEnum', 'Ether-link-oam-event-action-prim-enum',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_link_oam_cfg', 'EtherLinkOamEventActionPrimEnum',
                [], [],
                '''                Action to perform when a session comes up
                ''',
                'session_up',
                'Cisco-IOS-XR-ethernet-link-oam-cfg', False),
            _MetaInfoClassMember('critical-event', REFERENCE_ENUM_CLASS, 'EtherLinkOamEventActionEnum', 'Ether-link-oam-event-action-enum',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_link_oam_cfg', 'EtherLinkOamEventActionEnum',
                [], [],
                '''                Action to perform when a critical event
                occurs
                ''',
                'critical_event',
                'Cisco-IOS-XR-ethernet-link-oam-cfg', False),
            _MetaInfoClassMember('session-down', REFERENCE_ENUM_CLASS, 'EtherLinkOamEventActionEnumEfd', 'Ether-link-oam-event-action-enum-efd',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_link_oam_cfg', 'EtherLinkOamEventActionEnumEfd',
                [], [],
                '''                Action to perform when a session goes down
                ''',
                'session_down',
                'Cisco-IOS-XR-ethernet-link-oam-cfg', False),
            _MetaInfoClassMember('discovery-timeout', REFERENCE_ENUM_CLASS, 'EtherLinkOamEventActionEnumEfd', 'Ether-link-oam-event-action-enum-efd',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_link_oam_cfg', 'EtherLinkOamEventActionEnumEfd',
                [], [],
                '''                Action to perform when discovery timeout
                occurs
                ''',
                'discovery_timeout',
                'Cisco-IOS-XR-ethernet-link-oam-cfg', False),
            _MetaInfoClassMember('high-threshold', REFERENCE_ENUM_CLASS, 'EtherLinkOamEventActionEnum', 'Ether-link-oam-event-action-enum',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_link_oam_cfg', 'EtherLinkOamEventActionEnum',
                [], [],
                '''                Action to perform when a high-threshold
                event occurs
                ''',
                'high_threshold',
                'Cisco-IOS-XR-ethernet-link-oam-cfg', False),
            _MetaInfoClassMember('capabilities-conflict', REFERENCE_ENUM_CLASS, 'EtherLinkOamEventActionEnumEfd', 'Ether-link-oam-event-action-enum-efd',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_link_oam_cfg', 'EtherLinkOamEventActionEnumEfd',
                [], [],
                '''                Action to perform when a capabilities
                conflict occurs
                ''',
                'capabilities_conflict',
                'Cisco-IOS-XR-ethernet-link-oam-cfg', False),
            _MetaInfoClassMember('remote-loopback', REFERENCE_ENUM_CLASS, 'EtherLinkOamEventActionPrimEnum', 'Ether-link-oam-event-action-prim-enum',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_link_oam_cfg', 'EtherLinkOamEventActionPrimEnum',
                [], [],
                '''                Action to perform when remote loopback is
                entered or exited
                ''',
                'remote_loopback',
                'Cisco-IOS-XR-ethernet-link-oam-cfg', False),
            _MetaInfoClassMember('link-fault', REFERENCE_ENUM_CLASS, 'EtherLinkOamEventActionEnumEfd', 'Ether-link-oam-event-action-enum-efd',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_link_oam_cfg', 'EtherLinkOamEventActionEnumEfd',
                [], [],
                '''                Action to perform when a link fault message
                is received
                ''',
                'link_fault',
                'Cisco-IOS-XR-ethernet-link-oam-cfg', False),
            _MetaInfoClassMember('wiring-conflict', REFERENCE_ENUM_CLASS, 'EtherLinkOamEventActionEnumEfd', 'Ether-link-oam-event-action-enum-efd',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_link_oam_cfg', 'EtherLinkOamEventActionEnumEfd',
                [], [],
                '''                Action to perform when a wiring conflict
                occurs
                ''',
                'wiring_conflict',
                'Cisco-IOS-XR-ethernet-link-oam-cfg', False),
            ],
            'Cisco-IOS-XR-ethernet-link-oam-cfg',
            'action',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-ethernet-link-oam-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2_eth_infra_cfg',
        ),
    },
    'EthernetFeatures.EtherLinkOam.Profiles.Profile.RequireRemote' : {
        'meta_info' : _MetaInfoClass('EthernetFeatures.EtherLinkOam.Profiles.Profile.RequireRemote', REFERENCE_CLASS,
            '''Configure remote requirement parameters''',
            False, 
            [
            _MetaInfoClassMember('mib-retrieval', ATTRIBUTE, 'bool', 'boolean',
                None, None,
                [], [],
                '''                Enable or disable MIB retrieval requirement
                ''',
                'mib_retrieval',
                'Cisco-IOS-XR-ethernet-link-oam-cfg', False),
            _MetaInfoClassMember('mode', REFERENCE_ENUM_CLASS, 'EtherLinkOamRequireModeEnum', 'Ether-link-oam-require-mode-enum',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_link_oam_cfg', 'EtherLinkOamRequireModeEnum',
                [], [],
                '''                Possible required OAM modes
                ''',
                'mode',
                'Cisco-IOS-XR-ethernet-link-oam-cfg', False),
            _MetaInfoClassMember('remote-loopback', ATTRIBUTE, 'bool', 'boolean',
                None, None,
                [], [],
                '''                Enable or disable remote loopback
                requirement
                ''',
                'remote_loopback',
                'Cisco-IOS-XR-ethernet-link-oam-cfg', False),
            _MetaInfoClassMember('link-monitoring', ATTRIBUTE, 'bool', 'boolean',
                None, None,
                [], [],
                '''                Enable or disable link monitoring
                requirement
                ''',
                'link_monitoring',
                'Cisco-IOS-XR-ethernet-link-oam-cfg', False),
            ],
            'Cisco-IOS-XR-ethernet-link-oam-cfg',
            'require-remote',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-ethernet-link-oam-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2_eth_infra_cfg',
        ),
    },
    'EthernetFeatures.EtherLinkOam.Profiles.Profile.LinkMonitoring.SymbolPeriod.Window' : {
        'meta_info' : _MetaInfoClass('EthernetFeatures.EtherLinkOam.Profiles.Profile.LinkMonitoring.SymbolPeriod.Window', REFERENCE_CLASS,
            '''Window size configuration for symbol-period
events''',
            False, 
            [
            _MetaInfoClassMember('window', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('1', '4294967295')], [],
                '''                Size of the symbol-period window
                ''',
                'window',
                'Cisco-IOS-XR-ethernet-link-oam-cfg', False, is_mandatory=True),
            _MetaInfoClassMember('units', REFERENCE_ENUM_CLASS, 'EtherLinkOamWindowUnitsSymbolsEnum', 'Ether-link-oam-window-units-symbols-enum',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_link_oam_cfg', 'EtherLinkOamWindowUnitsSymbolsEnum',
                [], [],
                '''                Units to use for this window
                ''',
                'units',
                'Cisco-IOS-XR-ethernet-link-oam-cfg', False, is_mandatory=True),
            _MetaInfoClassMember('multiplier', REFERENCE_ENUM_CLASS, 'EtherLinkOamThresholdWindowMultiplierEnum', 'Ether-link-oam-threshold-window-multiplier-enum',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_link_oam_cfg', 'EtherLinkOamThresholdWindowMultiplierEnum',
                [], [],
                '''                The multiplier to use for this window (only
                valid if 'Units' is Symbols and treated as 1
                if unspecified)
                ''',
                'multiplier',
                'Cisco-IOS-XR-ethernet-link-oam-cfg', False, default_value='Cisco_IOS_XR_ethernet_link_oam_cfg.EtherLinkOamThresholdWindowMultiplierEnum.none'),
            ],
            'Cisco-IOS-XR-ethernet-link-oam-cfg',
            'window',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-ethernet-link-oam-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2_eth_infra_cfg',
            is_presence=True,
        ),
    },
    'EthernetFeatures.EtherLinkOam.Profiles.Profile.LinkMonitoring.SymbolPeriod.Threshold' : {
        'meta_info' : _MetaInfoClass('EthernetFeatures.EtherLinkOam.Profiles.Profile.LinkMonitoring.SymbolPeriod.Threshold', REFERENCE_CLASS,
            '''Threshold configuration for symbol-period
events''',
            False, 
            [
            _MetaInfoClassMember('threshold-low', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('1', '4294967295')], [],
                '''                The low threshold for symbol-period
                ''',
                'threshold_low',
                'Cisco-IOS-XR-ethernet-link-oam-cfg', False, default_value="1", has_must=True),
            _MetaInfoClassMember('threshold-high', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('1', '4294967295')], [],
                '''                The high threshold for symbol-period
                ''',
                'threshold_high',
                'Cisco-IOS-XR-ethernet-link-oam-cfg', False, has_must=True),
            _MetaInfoClassMember('units', REFERENCE_ENUM_CLASS, 'EtherLinkOamThresholdUnitsSymbolsEnum', 'Ether-link-oam-threshold-units-symbols-enum',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_link_oam_cfg', 'EtherLinkOamThresholdUnitsSymbolsEnum',
                [], [],
                '''                The units to use for these thresholds
                ''',
                'units',
                'Cisco-IOS-XR-ethernet-link-oam-cfg', False, default_value='Cisco_IOS_XR_ethernet_link_oam_cfg.EtherLinkOamThresholdUnitsSymbolsEnum.symbols', has_must=True),
            _MetaInfoClassMember('multiplier-low', REFERENCE_ENUM_CLASS, 'EtherLinkOamThresholdWindowMultiplierEnum', 'Ether-link-oam-threshold-window-multiplier-enum',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_link_oam_cfg', 'EtherLinkOamThresholdWindowMultiplierEnum',
                [], [],
                '''                The multiplier to use for the low threshold
                (only valid if 'Units' is Symbols and treated
                as 1 if unspecified)
                ''',
                'multiplier_low',
                'Cisco-IOS-XR-ethernet-link-oam-cfg', False, default_value='Cisco_IOS_XR_ethernet_link_oam_cfg.EtherLinkOamThresholdWindowMultiplierEnum.none', has_must=True),
            _MetaInfoClassMember('multiplier-high', REFERENCE_ENUM_CLASS, 'EtherLinkOamThresholdWindowMultiplierEnum', 'Ether-link-oam-threshold-window-multiplier-enum',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_link_oam_cfg', 'EtherLinkOamThresholdWindowMultiplierEnum',
                [], [],
                '''                The multiplier to use for the high threshold
                (only valid if 'Units' is Symbols and treated
                as 1 if unspecified)
                ''',
                'multiplier_high',
                'Cisco-IOS-XR-ethernet-link-oam-cfg', False, has_must=True),
            ],
            'Cisco-IOS-XR-ethernet-link-oam-cfg',
            'threshold',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-ethernet-link-oam-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2_eth_infra_cfg',
        ),
    },
    'EthernetFeatures.EtherLinkOam.Profiles.Profile.LinkMonitoring.SymbolPeriod' : {
        'meta_info' : _MetaInfoClass('EthernetFeatures.EtherLinkOam.Profiles.Profile.LinkMonitoring.SymbolPeriod', REFERENCE_CLASS,
            '''Symbol-period event configuration''',
            False, 
            [
            _MetaInfoClassMember('window', REFERENCE_CLASS, 'Window', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2_eth_infra_cfg', 'EthernetFeatures.EtherLinkOam.Profiles.Profile.LinkMonitoring.SymbolPeriod.Window',
                [], [],
                '''                Window size configuration for symbol-period
                events
                ''',
                'window',
                'Cisco-IOS-XR-ethernet-link-oam-cfg', False, is_presence=True),
            _MetaInfoClassMember('threshold', REFERENCE_CLASS, 'Threshold', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2_eth_infra_cfg', 'EthernetFeatures.EtherLinkOam.Profiles.Profile.LinkMonitoring.SymbolPeriod.Threshold',
                [], [],
                '''                Threshold configuration for symbol-period
                events
                ''',
                'threshold',
                'Cisco-IOS-XR-ethernet-link-oam-cfg', False),
            ],
            'Cisco-IOS-XR-ethernet-link-oam-cfg',
            'symbol-period',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-ethernet-link-oam-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2_eth_infra_cfg',
        ),
    },
    'EthernetFeatures.EtherLinkOam.Profiles.Profile.LinkMonitoring.FramePeriod.Window' : {
        'meta_info' : _MetaInfoClass('EthernetFeatures.EtherLinkOam.Profiles.Profile.LinkMonitoring.FramePeriod.Window', REFERENCE_CLASS,
            '''Window size configuration for frame-period
events''',
            False, 
            [
            _MetaInfoClassMember('window', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('1', '4294967295')], [],
                '''                Size of the frame-period window
                ''',
                'window',
                'Cisco-IOS-XR-ethernet-link-oam-cfg', False, is_mandatory=True),
            _MetaInfoClassMember('units', REFERENCE_ENUM_CLASS, 'EtherLinkOamWindowUnitsFramesEnum', 'Ether-link-oam-window-units-frames-enum',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_link_oam_cfg', 'EtherLinkOamWindowUnitsFramesEnum',
                [], [],
                '''                The units to use for this window
                ''',
                'units',
                'Cisco-IOS-XR-ethernet-link-oam-cfg', False, is_mandatory=True),
            _MetaInfoClassMember('multiplier', REFERENCE_ENUM_CLASS, 'EtherLinkOamThresholdWindowMultiplierEnum', 'Ether-link-oam-threshold-window-multiplier-enum',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_link_oam_cfg', 'EtherLinkOamThresholdWindowMultiplierEnum',
                [], [],
                '''                The multiplier to use for this window (only
                valid if 'Units' is Frames and treated as 1
                if unspecified)
                ''',
                'multiplier',
                'Cisco-IOS-XR-ethernet-link-oam-cfg', False, default_value='Cisco_IOS_XR_ethernet_link_oam_cfg.EtherLinkOamThresholdWindowMultiplierEnum.none'),
            ],
            'Cisco-IOS-XR-ethernet-link-oam-cfg',
            'window',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-ethernet-link-oam-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2_eth_infra_cfg',
            is_presence=True,
        ),
    },
    'EthernetFeatures.EtherLinkOam.Profiles.Profile.LinkMonitoring.FramePeriod.Threshold' : {
        'meta_info' : _MetaInfoClass('EthernetFeatures.EtherLinkOam.Profiles.Profile.LinkMonitoring.FramePeriod.Threshold', REFERENCE_CLASS,
            '''Threshold configuration for frame-period
events''',
            False, 
            [
            _MetaInfoClassMember('threshold-low', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('1', '4294967295')], [],
                '''                The low threshold for frame-period events
                ''',
                'threshold_low',
                'Cisco-IOS-XR-ethernet-link-oam-cfg', False, default_value="1", has_must=True),
            _MetaInfoClassMember('threshold-high', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('1', '4294967295')], [],
                '''                The high threshold for frame-period events
                ''',
                'threshold_high',
                'Cisco-IOS-XR-ethernet-link-oam-cfg', False, has_must=True),
            _MetaInfoClassMember('units', REFERENCE_ENUM_CLASS, 'EtherLinkOamThresholdUnitsFramesEnum', 'Ether-link-oam-threshold-units-frames-enum',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_link_oam_cfg', 'EtherLinkOamThresholdUnitsFramesEnum',
                [], [],
                '''                The units to use for these thresholds
                ''',
                'units',
                'Cisco-IOS-XR-ethernet-link-oam-cfg', False, default_value='Cisco_IOS_XR_ethernet_link_oam_cfg.EtherLinkOamThresholdUnitsFramesEnum.ppm', has_must=True),
            _MetaInfoClassMember('multiplier-low', REFERENCE_ENUM_CLASS, 'EtherLinkOamThresholdWindowMultiplierEnum', 'Ether-link-oam-threshold-window-multiplier-enum',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_link_oam_cfg', 'EtherLinkOamThresholdWindowMultiplierEnum',
                [], [],
                '''                The multiplier to use for the low threshold
                (only valid if 'Units' is Frames and treated
                as 1 if unspecified)
                ''',
                'multiplier_low',
                'Cisco-IOS-XR-ethernet-link-oam-cfg', False, default_value='Cisco_IOS_XR_ethernet_link_oam_cfg.EtherLinkOamThresholdWindowMultiplierEnum.none', has_must=True),
            _MetaInfoClassMember('multiplier-high', REFERENCE_ENUM_CLASS, 'EtherLinkOamThresholdWindowMultiplierEnum', 'Ether-link-oam-threshold-window-multiplier-enum',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_link_oam_cfg', 'EtherLinkOamThresholdWindowMultiplierEnum',
                [], [],
                '''                The multiplier to use for the high threshold
                (only valid if 'Units' is Frames and treated
                as 1 if unspecified)
                ''',
                'multiplier_high',
                'Cisco-IOS-XR-ethernet-link-oam-cfg', False, has_must=True),
            ],
            'Cisco-IOS-XR-ethernet-link-oam-cfg',
            'threshold',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-ethernet-link-oam-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2_eth_infra_cfg',
        ),
    },
    'EthernetFeatures.EtherLinkOam.Profiles.Profile.LinkMonitoring.FramePeriod' : {
        'meta_info' : _MetaInfoClass('EthernetFeatures.EtherLinkOam.Profiles.Profile.LinkMonitoring.FramePeriod', REFERENCE_CLASS,
            '''Frame-period event configuration''',
            False, 
            [
            _MetaInfoClassMember('window', REFERENCE_CLASS, 'Window', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2_eth_infra_cfg', 'EthernetFeatures.EtherLinkOam.Profiles.Profile.LinkMonitoring.FramePeriod.Window',
                [], [],
                '''                Window size configuration for frame-period
                events
                ''',
                'window',
                'Cisco-IOS-XR-ethernet-link-oam-cfg', False, is_presence=True),
            _MetaInfoClassMember('threshold', REFERENCE_CLASS, 'Threshold', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2_eth_infra_cfg', 'EthernetFeatures.EtherLinkOam.Profiles.Profile.LinkMonitoring.FramePeriod.Threshold',
                [], [],
                '''                Threshold configuration for frame-period
                events
                ''',
                'threshold',
                'Cisco-IOS-XR-ethernet-link-oam-cfg', False),
            ],
            'Cisco-IOS-XR-ethernet-link-oam-cfg',
            'frame-period',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-ethernet-link-oam-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2_eth_infra_cfg',
        ),
    },
    'EthernetFeatures.EtherLinkOam.Profiles.Profile.LinkMonitoring.FrameSeconds.Threshold' : {
        'meta_info' : _MetaInfoClass('EthernetFeatures.EtherLinkOam.Profiles.Profile.LinkMonitoring.FrameSeconds.Threshold', REFERENCE_CLASS,
            '''Threshold configuration for frame-seconds
events''',
            False, 
            [
            _MetaInfoClassMember('threshold-low', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('1', '900')], [],
                '''                The low threshold for frame-seconds events
                ''',
                'threshold_low',
                'Cisco-IOS-XR-ethernet-link-oam-cfg', False, default_value="1"),
            _MetaInfoClassMember('threshold-high', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('1', '900')], [],
                '''                The high threshold for frame-seconds events
                ''',
                'threshold_high',
                'Cisco-IOS-XR-ethernet-link-oam-cfg', False),
            ],
            'Cisco-IOS-XR-ethernet-link-oam-cfg',
            'threshold',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-ethernet-link-oam-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2_eth_infra_cfg',
        ),
    },
    'EthernetFeatures.EtherLinkOam.Profiles.Profile.LinkMonitoring.FrameSeconds' : {
        'meta_info' : _MetaInfoClass('EthernetFeatures.EtherLinkOam.Profiles.Profile.LinkMonitoring.FrameSeconds', REFERENCE_CLASS,
            '''Frame-seconds event configuration''',
            False, 
            [
            _MetaInfoClassMember('threshold', REFERENCE_CLASS, 'Threshold', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2_eth_infra_cfg', 'EthernetFeatures.EtherLinkOam.Profiles.Profile.LinkMonitoring.FrameSeconds.Threshold',
                [], [],
                '''                Threshold configuration for frame-seconds
                events
                ''',
                'threshold',
                'Cisco-IOS-XR-ethernet-link-oam-cfg', False),
            _MetaInfoClassMember('window', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('10000', '900000')], [],
                '''                Window size configuration for frame-seconds
                events
                ''',
                'window',
                'Cisco-IOS-XR-ethernet-link-oam-cfg', False, default_value="60000"),
            ],
            'Cisco-IOS-XR-ethernet-link-oam-cfg',
            'frame-seconds',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-ethernet-link-oam-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2_eth_infra_cfg',
        ),
    },
    'EthernetFeatures.EtherLinkOam.Profiles.Profile.LinkMonitoring.Frame.Threshold' : {
        'meta_info' : _MetaInfoClass('EthernetFeatures.EtherLinkOam.Profiles.Profile.LinkMonitoring.Frame.Threshold', REFERENCE_CLASS,
            '''Threshold configuration for frame events''',
            False, 
            [
            _MetaInfoClassMember('threshold-low', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('1', '4294967295')], [],
                '''                The low threshold for frame events
                ''',
                'threshold_low',
                'Cisco-IOS-XR-ethernet-link-oam-cfg', False, default_value="1"),
            _MetaInfoClassMember('threshold-high', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('1', '4294967295')], [],
                '''                The high threshold for frame events
                ''',
                'threshold_high',
                'Cisco-IOS-XR-ethernet-link-oam-cfg', False),
            _MetaInfoClassMember('multiplier-low', REFERENCE_ENUM_CLASS, 'EtherLinkOamThresholdWindowMultiplierEnum', 'Ether-link-oam-threshold-window-multiplier-enum',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_link_oam_cfg', 'EtherLinkOamThresholdWindowMultiplierEnum',
                [], [],
                '''                The multiplier to use for the low threshold
                (treated as 1 if unspecified)
                ''',
                'multiplier_low',
                'Cisco-IOS-XR-ethernet-link-oam-cfg', False, default_value='Cisco_IOS_XR_ethernet_link_oam_cfg.EtherLinkOamThresholdWindowMultiplierEnum.none', has_must=True),
            _MetaInfoClassMember('multiplier-high', REFERENCE_ENUM_CLASS, 'EtherLinkOamThresholdWindowMultiplierEnum', 'Ether-link-oam-threshold-window-multiplier-enum',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_link_oam_cfg', 'EtherLinkOamThresholdWindowMultiplierEnum',
                [], [],
                '''                The multiplier to use for the high threshold
                (treated as 1 if unspecified)
                ''',
                'multiplier_high',
                'Cisco-IOS-XR-ethernet-link-oam-cfg', False, has_must=True),
            ],
            'Cisco-IOS-XR-ethernet-link-oam-cfg',
            'threshold',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-ethernet-link-oam-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2_eth_infra_cfg',
        ),
    },
    'EthernetFeatures.EtherLinkOam.Profiles.Profile.LinkMonitoring.Frame' : {
        'meta_info' : _MetaInfoClass('EthernetFeatures.EtherLinkOam.Profiles.Profile.LinkMonitoring.Frame', REFERENCE_CLASS,
            '''Frame event configuration''',
            False, 
            [
            _MetaInfoClassMember('threshold', REFERENCE_CLASS, 'Threshold', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2_eth_infra_cfg', 'EthernetFeatures.EtherLinkOam.Profiles.Profile.LinkMonitoring.Frame.Threshold',
                [], [],
                '''                Threshold configuration for frame events
                ''',
                'threshold',
                'Cisco-IOS-XR-ethernet-link-oam-cfg', False),
            _MetaInfoClassMember('window', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('1000', '60000')], [],
                '''                Window size configuration for frame events
                ''',
                'window',
                'Cisco-IOS-XR-ethernet-link-oam-cfg', False, default_value="1000"),
            ],
            'Cisco-IOS-XR-ethernet-link-oam-cfg',
            'frame',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-ethernet-link-oam-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2_eth_infra_cfg',
        ),
    },
    'EthernetFeatures.EtherLinkOam.Profiles.Profile.LinkMonitoring' : {
        'meta_info' : _MetaInfoClass('EthernetFeatures.EtherLinkOam.Profiles.Profile.LinkMonitoring', REFERENCE_CLASS,
            '''Configure link monitor parameters''',
            False, 
            [
            _MetaInfoClassMember('symbol-period', REFERENCE_CLASS, 'SymbolPeriod', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2_eth_infra_cfg', 'EthernetFeatures.EtherLinkOam.Profiles.Profile.LinkMonitoring.SymbolPeriod',
                [], [],
                '''                Symbol-period event configuration
                ''',
                'symbol_period',
                'Cisco-IOS-XR-ethernet-link-oam-cfg', False),
            _MetaInfoClassMember('frame-period', REFERENCE_CLASS, 'FramePeriod', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2_eth_infra_cfg', 'EthernetFeatures.EtherLinkOam.Profiles.Profile.LinkMonitoring.FramePeriod',
                [], [],
                '''                Frame-period event configuration
                ''',
                'frame_period',
                'Cisco-IOS-XR-ethernet-link-oam-cfg', False),
            _MetaInfoClassMember('frame-seconds', REFERENCE_CLASS, 'FrameSeconds', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2_eth_infra_cfg', 'EthernetFeatures.EtherLinkOam.Profiles.Profile.LinkMonitoring.FrameSeconds',
                [], [],
                '''                Frame-seconds event configuration
                ''',
                'frame_seconds',
                'Cisco-IOS-XR-ethernet-link-oam-cfg', False),
            _MetaInfoClassMember('frame', REFERENCE_CLASS, 'Frame', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2_eth_infra_cfg', 'EthernetFeatures.EtherLinkOam.Profiles.Profile.LinkMonitoring.Frame',
                [], [],
                '''                Frame event configuration
                ''',
                'frame',
                'Cisco-IOS-XR-ethernet-link-oam-cfg', False),
            _MetaInfoClassMember('monitoring', ATTRIBUTE, 'bool', 'boolean',
                None, None,
                [], [],
                '''                Enable or disable monitoring
                ''',
                'monitoring',
                'Cisco-IOS-XR-ethernet-link-oam-cfg', False),
            ],
            'Cisco-IOS-XR-ethernet-link-oam-cfg',
            'link-monitoring',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-ethernet-link-oam-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2_eth_infra_cfg',
        ),
    },
    'EthernetFeatures.EtherLinkOam.Profiles.Profile' : {
        'meta_info' : _MetaInfoClass('EthernetFeatures.EtherLinkOam.Profiles.Profile', REFERENCE_LIST,
            '''Name of the profile''',
            False, 
            [
            _MetaInfoClassMember('profile', ATTRIBUTE, 'str', 'xr:Cisco-ios-xr-string',
                None, None,
                [], [b'[\\w\\-\\.:,_@#%$\\+=\\|;]+'],
                '''                none
                ''',
                'profile',
                'Cisco-IOS-XR-ethernet-link-oam-cfg', True),
            _MetaInfoClassMember('action', REFERENCE_CLASS, 'Action', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2_eth_infra_cfg', 'EthernetFeatures.EtherLinkOam.Profiles.Profile.Action',
                [], [],
                '''                Configure action parameters
                ''',
                'action',
                'Cisco-IOS-XR-ethernet-link-oam-cfg', False),
            _MetaInfoClassMember('require-remote', REFERENCE_CLASS, 'RequireRemote', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2_eth_infra_cfg', 'EthernetFeatures.EtherLinkOam.Profiles.Profile.RequireRemote',
                [], [],
                '''                Configure remote requirement parameters
                ''',
                'require_remote',
                'Cisco-IOS-XR-ethernet-link-oam-cfg', False),
            _MetaInfoClassMember('mib-retrieval', ATTRIBUTE, 'bool', 'boolean',
                None, None,
                [], [],
                '''                Enable or disable MIB retrieval support
                ''',
                'mib_retrieval',
                'Cisco-IOS-XR-ethernet-link-oam-cfg', False),
            _MetaInfoClassMember('udlf', ATTRIBUTE, 'bool', 'boolean',
                None, None,
                [], [],
                '''                Enable or disable uni-directional link-fault
                detection support
                ''',
                'udlf',
                'Cisco-IOS-XR-ethernet-link-oam-cfg', False),
            _MetaInfoClassMember('hello-interval', REFERENCE_ENUM_CLASS, 'EtherLinkOamHelloIntervalEnum', 'Ether-link-oam-hello-interval-enum',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_link_oam_cfg', 'EtherLinkOamHelloIntervalEnum',
                [], [],
                '''                Possible Ethernet Link OAM hello intervals
                ''',
                'hello_interval',
                'Cisco-IOS-XR-ethernet-link-oam-cfg', False),
            _MetaInfoClassMember('mode', REFERENCE_ENUM_CLASS, 'EtherLinkOamModeEnum', 'Ether-link-oam-mode-enum',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_link_oam_cfg', 'EtherLinkOamModeEnum',
                [], [],
                '''                Set the OAM mode to passive
                ''',
                'mode',
                'Cisco-IOS-XR-ethernet-link-oam-cfg', False),
            _MetaInfoClassMember('remote-loopback', ATTRIBUTE, 'bool', 'boolean',
                None, None,
                [], [],
                '''                Enable or disable remote loopback support
                ''',
                'remote_loopback',
                'Cisco-IOS-XR-ethernet-link-oam-cfg', False),
            _MetaInfoClassMember('timeout', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('2', '30')], [],
                '''                Connection timeout period in number of lost
                heartbeats
                ''',
                'timeout',
                'Cisco-IOS-XR-ethernet-link-oam-cfg', False),
            _MetaInfoClassMember('link-monitoring', REFERENCE_CLASS, 'LinkMonitoring', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2_eth_infra_cfg', 'EthernetFeatures.EtherLinkOam.Profiles.Profile.LinkMonitoring',
                [], [],
                '''                Configure link monitor parameters
                ''',
                'link_monitoring',
                'Cisco-IOS-XR-ethernet-link-oam-cfg', False),
            ],
            'Cisco-IOS-XR-ethernet-link-oam-cfg',
            'profile',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-ethernet-link-oam-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2_eth_infra_cfg',
        ),
    },
    'EthernetFeatures.EtherLinkOam.Profiles' : {
        'meta_info' : _MetaInfoClass('EthernetFeatures.EtherLinkOam.Profiles', REFERENCE_CLASS,
            '''Table of Ethernet Link OAM profiles''',
            False, 
            [
            _MetaInfoClassMember('profile', REFERENCE_LIST, 'Profile', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2_eth_infra_cfg', 'EthernetFeatures.EtherLinkOam.Profiles.Profile',
                [], [],
                '''                Name of the profile
                ''',
                'profile',
                'Cisco-IOS-XR-ethernet-link-oam-cfg', False),
            ],
            'Cisco-IOS-XR-ethernet-link-oam-cfg',
            'profiles',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-ethernet-link-oam-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2_eth_infra_cfg',
        ),
    },
    'EthernetFeatures.EtherLinkOam' : {
        'meta_info' : _MetaInfoClass('EthernetFeatures.EtherLinkOam', REFERENCE_CLASS,
            '''Ethernet Link OAM Global Configuration''',
            False, 
            [
            _MetaInfoClassMember('profiles', REFERENCE_CLASS, 'Profiles', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2_eth_infra_cfg', 'EthernetFeatures.EtherLinkOam.Profiles',
                [], [],
                '''                Table of Ethernet Link OAM profiles
                ''',
                'profiles',
                'Cisco-IOS-XR-ethernet-link-oam-cfg', False),
            ],
            'Cisco-IOS-XR-ethernet-link-oam-cfg',
            'ether-link-oam',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-ethernet-link-oam-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2_eth_infra_cfg',
        ),
    },
    'EthernetFeatures' : {
        'meta_info' : _MetaInfoClass('EthernetFeatures', REFERENCE_CLASS,
            '''Ethernet Features Configuration''',
            False, 
            [
            _MetaInfoClassMember('egress-filtering', REFERENCE_CLASS, 'EgressFiltering', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2_eth_infra_cfg', 'EthernetFeatures.EgressFiltering',
                [], [],
                '''                Egress Filtering Configuration
                ''',
                'egress_filtering',
                'Cisco-IOS-XR-l2-eth-infra-cfg', False),
            _MetaInfoClassMember('cfm', REFERENCE_CLASS, 'Cfm', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2_eth_infra_cfg', 'EthernetFeatures.Cfm',
                [], [],
                '''                CFM global configuration
                ''',
                'cfm',
                'Cisco-IOS-XR-ethernet-cfm-cfg', False),
            _MetaInfoClassMember('ether-link-oam', REFERENCE_CLASS, 'EtherLinkOam', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2_eth_infra_cfg', 'EthernetFeatures.EtherLinkOam',
                [], [],
                '''                Ethernet Link OAM Global Configuration
                ''',
                'ether_link_oam',
                'Cisco-IOS-XR-ethernet-link-oam-cfg', False),
            ],
            'Cisco-IOS-XR-l2-eth-infra-cfg',
            'ethernet-features',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-l2-eth-infra-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2_eth_infra_cfg',
        ),
    },
}
_meta_table['EthernetFeatures.Cfm.Domains.Domain.Services.Service.Ais.Transmission']['meta_info'].parent =_meta_table['EthernetFeatures.Cfm.Domains.Domain.Services.Service.Ais']['meta_info']
_meta_table['EthernetFeatures.Cfm.Domains.Domain.Services.Service.CrossCheck.CrossCheckMeps.CrossCheckMep']['meta_info'].parent =_meta_table['EthernetFeatures.Cfm.Domains.Domain.Services.Service.CrossCheck.CrossCheckMeps']['meta_info']
_meta_table['EthernetFeatures.Cfm.Domains.Domain.Services.Service.CrossCheck.CrossCheckMeps']['meta_info'].parent =_meta_table['EthernetFeatures.Cfm.Domains.Domain.Services.Service.CrossCheck']['meta_info']
_meta_table['EthernetFeatures.Cfm.Domains.Domain.Services.Service.Efd2']['meta_info'].parent =_meta_table['EthernetFeatures.Cfm.Domains.Domain.Services.Service']['meta_info']
_meta_table['EthernetFeatures.Cfm.Domains.Domain.Services.Service.ContinuityCheckInterval']['meta_info'].parent =_meta_table['EthernetFeatures.Cfm.Domains.Domain.Services.Service']['meta_info']
_meta_table['EthernetFeatures.Cfm.Domains.Domain.Services.Service.MipAutoCreation']['meta_info'].parent =_meta_table['EthernetFeatures.Cfm.Domains.Domain.Services.Service']['meta_info']
_meta_table['EthernetFeatures.Cfm.Domains.Domain.Services.Service.Ais']['meta_info'].parent =_meta_table['EthernetFeatures.Cfm.Domains.Domain.Services.Service']['meta_info']
_meta_table['EthernetFeatures.Cfm.Domains.Domain.Services.Service.CrossCheck']['meta_info'].parent =_meta_table['EthernetFeatures.Cfm.Domains.Domain.Services.Service']['meta_info']
_meta_table['EthernetFeatures.Cfm.Domains.Domain.Services.Service.ServiceProperties']['meta_info'].parent =_meta_table['EthernetFeatures.Cfm.Domains.Domain.Services.Service']['meta_info']
_meta_table['EthernetFeatures.Cfm.Domains.Domain.Services.Service']['meta_info'].parent =_meta_table['EthernetFeatures.Cfm.Domains.Domain.Services']['meta_info']
_meta_table['EthernetFeatures.Cfm.Domains.Domain.Services']['meta_info'].parent =_meta_table['EthernetFeatures.Cfm.Domains.Domain']['meta_info']
_meta_table['EthernetFeatures.Cfm.Domains.Domain.DomainProperties']['meta_info'].parent =_meta_table['EthernetFeatures.Cfm.Domains.Domain']['meta_info']
_meta_table['EthernetFeatures.Cfm.Domains.Domain']['meta_info'].parent =_meta_table['EthernetFeatures.Cfm.Domains']['meta_info']
_meta_table['EthernetFeatures.Cfm.TracerouteCache']['meta_info'].parent =_meta_table['EthernetFeatures.Cfm']['meta_info']
_meta_table['EthernetFeatures.Cfm.Domains']['meta_info'].parent =_meta_table['EthernetFeatures.Cfm']['meta_info']
_meta_table['EthernetFeatures.EtherLinkOam.Profiles.Profile.LinkMonitoring.SymbolPeriod.Window']['meta_info'].parent =_meta_table['EthernetFeatures.EtherLinkOam.Profiles.Profile.LinkMonitoring.SymbolPeriod']['meta_info']
_meta_table['EthernetFeatures.EtherLinkOam.Profiles.Profile.LinkMonitoring.SymbolPeriod.Threshold']['meta_info'].parent =_meta_table['EthernetFeatures.EtherLinkOam.Profiles.Profile.LinkMonitoring.SymbolPeriod']['meta_info']
_meta_table['EthernetFeatures.EtherLinkOam.Profiles.Profile.LinkMonitoring.FramePeriod.Window']['meta_info'].parent =_meta_table['EthernetFeatures.EtherLinkOam.Profiles.Profile.LinkMonitoring.FramePeriod']['meta_info']
_meta_table['EthernetFeatures.EtherLinkOam.Profiles.Profile.LinkMonitoring.FramePeriod.Threshold']['meta_info'].parent =_meta_table['EthernetFeatures.EtherLinkOam.Profiles.Profile.LinkMonitoring.FramePeriod']['meta_info']
_meta_table['EthernetFeatures.EtherLinkOam.Profiles.Profile.LinkMonitoring.FrameSeconds.Threshold']['meta_info'].parent =_meta_table['EthernetFeatures.EtherLinkOam.Profiles.Profile.LinkMonitoring.FrameSeconds']['meta_info']
_meta_table['EthernetFeatures.EtherLinkOam.Profiles.Profile.LinkMonitoring.Frame.Threshold']['meta_info'].parent =_meta_table['EthernetFeatures.EtherLinkOam.Profiles.Profile.LinkMonitoring.Frame']['meta_info']
_meta_table['EthernetFeatures.EtherLinkOam.Profiles.Profile.LinkMonitoring.SymbolPeriod']['meta_info'].parent =_meta_table['EthernetFeatures.EtherLinkOam.Profiles.Profile.LinkMonitoring']['meta_info']
_meta_table['EthernetFeatures.EtherLinkOam.Profiles.Profile.LinkMonitoring.FramePeriod']['meta_info'].parent =_meta_table['EthernetFeatures.EtherLinkOam.Profiles.Profile.LinkMonitoring']['meta_info']
_meta_table['EthernetFeatures.EtherLinkOam.Profiles.Profile.LinkMonitoring.FrameSeconds']['meta_info'].parent =_meta_table['EthernetFeatures.EtherLinkOam.Profiles.Profile.LinkMonitoring']['meta_info']
_meta_table['EthernetFeatures.EtherLinkOam.Profiles.Profile.LinkMonitoring.Frame']['meta_info'].parent =_meta_table['EthernetFeatures.EtherLinkOam.Profiles.Profile.LinkMonitoring']['meta_info']
_meta_table['EthernetFeatures.EtherLinkOam.Profiles.Profile.Action']['meta_info'].parent =_meta_table['EthernetFeatures.EtherLinkOam.Profiles.Profile']['meta_info']
_meta_table['EthernetFeatures.EtherLinkOam.Profiles.Profile.RequireRemote']['meta_info'].parent =_meta_table['EthernetFeatures.EtherLinkOam.Profiles.Profile']['meta_info']
_meta_table['EthernetFeatures.EtherLinkOam.Profiles.Profile.LinkMonitoring']['meta_info'].parent =_meta_table['EthernetFeatures.EtherLinkOam.Profiles.Profile']['meta_info']
_meta_table['EthernetFeatures.EtherLinkOam.Profiles.Profile']['meta_info'].parent =_meta_table['EthernetFeatures.EtherLinkOam.Profiles']['meta_info']
_meta_table['EthernetFeatures.EtherLinkOam.Profiles']['meta_info'].parent =_meta_table['EthernetFeatures.EtherLinkOam']['meta_info']
_meta_table['EthernetFeatures.EgressFiltering']['meta_info'].parent =_meta_table['EthernetFeatures']['meta_info']
_meta_table['EthernetFeatures.Cfm']['meta_info'].parent =_meta_table['EthernetFeatures']['meta_info']
_meta_table['EthernetFeatures.EtherLinkOam']['meta_info'].parent =_meta_table['EthernetFeatures']['meta_info']
