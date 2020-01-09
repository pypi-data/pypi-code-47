
'''
This is auto-generated file,
which includes metadata for module Cisco_IOS_XR_clns_isis_cfg
'''

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_LIST, REFERENCE_LEAFLIST, REFERENCE_BITS, REFERENCE_UNION
from ydk._core._dm_meta_info import REFERENCE_CLASS, REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, ANYXML_CLASS
from ydk._core._importer import _yang_ns

_meta_table = {
    'NflagClear' : _MetaInfoEnum('NflagClear',
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'NflagClear',
        '''Nflag clear''',
        {
            'disable':'disable',
            'enable':'enable',
        }, 'Cisco-IOS-XR-clns-isis-cfg', _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-clns-isis-cfg']),
    'IsisAdvTypeInterLevel' : _MetaInfoEnum('IsisAdvTypeInterLevel',
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'IsisAdvTypeInterLevel',
        '''Isis adv type inter level''',
        {
            'inter-level':'inter_level',
        }, 'Cisco-IOS-XR-clns-isis-cfg', _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-clns-isis-cfg']),
    'IsisEnablePoi' : _MetaInfoEnum('IsisEnablePoi',
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'IsisEnablePoi',
        '''Isis enable poi''',
        {
            'enable-poi-off':'enable_poi_off',
            'enable-poi-on':'enable_poi_on',
        }, 'Cisco-IOS-XR-clns-isis-cfg', _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-clns-isis-cfg']),
    'IsisInterfaceState' : _MetaInfoEnum('IsisInterfaceState',
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'IsisInterfaceState',
        '''Isis interface state''',
        {
            'shutdown':'shutdown',
            'suppressed':'suppressed',
            'passive':'passive',
            'enabled-active':'enabled_active',
        }, 'Cisco-IOS-XR-clns-isis-cfg', _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-clns-isis-cfg']),
    'Isisfrr' : _MetaInfoEnum('Isisfrr',
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'Isisfrr',
        '''Isisfrr''',
        {
            'per-link':'per_link',
            'per-prefix':'per_prefix',
        }, 'Cisco-IOS-XR-clns-isis-cfg', _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-clns-isis-cfg']),
    'IsisfrrLoadSharing' : _MetaInfoEnum('IsisfrrLoadSharing',
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'IsisfrrLoadSharing',
        '''Isisfrr load sharing''',
        {
            'disable':'disable',
        }, 'Cisco-IOS-XR-clns-isis-cfg', _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-clns-isis-cfg']),
    'IsisAuthenticationFailureMode' : _MetaInfoEnum('IsisAuthenticationFailureMode',
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'IsisAuthenticationFailureMode',
        '''Isis authentication failure mode''',
        {
            'drop':'drop',
            'send-only':'send_only',
        }, 'Cisco-IOS-XR-clns-isis-cfg', _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-clns-isis-cfg']),
    'IsisApplyWeight' : _MetaInfoEnum('IsisApplyWeight',
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'IsisApplyWeight',
        '''Isis apply weight''',
        {
            'ecmp-only':'ecmp_only',
            'ucmp-only':'ucmp_only',
            'ecmp-only-bandwidth':'ecmp_only_bandwidth',
        }, 'Cisco-IOS-XR-clns-isis-cfg', _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-clns-isis-cfg']),
    'IsisLabelPreference' : _MetaInfoEnum('IsisLabelPreference',
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'IsisLabelPreference',
        '''Isis label preference''',
        {
            'ldp':'ldp',
            'segment-routing':'segment_routing',
        }, 'Cisco-IOS-XR-clns-isis-cfg', _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-clns-isis-cfg']),
    'Isissid1' : _MetaInfoEnum('Isissid1',
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'Isissid1',
        '''Isissid1''',
        {
            'index':'index',
            'absolute':'absolute',
        }, 'Cisco-IOS-XR-clns-isis-cfg', _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-clns-isis-cfg']),
    'IsisMetric' : _MetaInfoEnum('IsisMetric',
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'IsisMetric',
        '''Isis metric''',
        {
            'internal':'internal',
            'external':'external',
            'rib-internal':'rib_internal',
            'rib-external':'rib_external',
        }, 'Cisco-IOS-XR-clns-isis-cfg', _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-clns-isis-cfg']),
    'IsisAttachedBit' : _MetaInfoEnum('IsisAttachedBit',
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'IsisAttachedBit',
        '''Isis attached bit''',
        {
            'area':'area',
            'on':'on',
            'off':'off',
        }, 'Cisco-IOS-XR-clns-isis-cfg', _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-clns-isis-cfg']),
    'IsisConfigurableLevels' : _MetaInfoEnum('IsisConfigurableLevels',
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'IsisConfigurableLevels',
        '''Isis configurable levels''',
        {
            'level1':'level1',
            'level2':'level2',
            'level1-and2':'level1_and2',
        }, 'Cisco-IOS-XR-clns-isis-cfg', _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-clns-isis-cfg']),
    'IsisConfigurableLevel' : _MetaInfoEnum('IsisConfigurableLevel',
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'IsisConfigurableLevel',
        '''Isis configurable level''',
        {
            'level-12':'level_12',
            'level-1':'level_1',
            'level-2':'level_2',
        }, 'Cisco-IOS-XR-clns-isis-cfg', _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-clns-isis-cfg']),
    'IsisHelloPadding' : _MetaInfoEnum('IsisHelloPadding',
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'IsisHelloPadding',
        '''Isis hello padding''',
        {
            'never':'never',
            'sometimes':'sometimes',
        }, 'Cisco-IOS-XR-clns-isis-cfg', _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-clns-isis-cfg']),
    'IsisSnpAuth' : _MetaInfoEnum('IsisSnpAuth',
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'IsisSnpAuth',
        '''Isis snp auth''',
        {
            'send-only':'send_only',
            'full':'full',
        }, 'Cisco-IOS-XR-clns-isis-cfg', _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-clns-isis-cfg']),
    'IsisInterfaceAfState' : _MetaInfoEnum('IsisInterfaceAfState',
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'IsisInterfaceAfState',
        '''Isis interface af state''',
        {
            'disable':'disable',
        }, 'Cisco-IOS-XR-clns-isis-cfg', _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-clns-isis-cfg']),
    'IsisexplicitNullFlag' : _MetaInfoEnum('IsisexplicitNullFlag',
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'IsisexplicitNullFlag',
        '''Isisexplicit null flag''',
        {
            'disable':'disable',
            'enable':'enable',
        }, 'Cisco-IOS-XR-clns-isis-cfg', _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-clns-isis-cfg']),
    'IsisApplicationAttribute' : _MetaInfoEnum('IsisApplicationAttribute',
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'IsisApplicationAttribute',
        '''Isis application attribute''',
        {
            'srlg':'srlg',
        }, 'Cisco-IOS-XR-clns-isis-cfg', _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-clns-isis-cfg']),
    'IsisfrrSrlgProtection' : _MetaInfoEnum('IsisfrrSrlgProtection',
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'IsisfrrSrlgProtection',
        '''Isisfrr srlg protection''',
        {
            'local':'local',
            'weighted-global':'weighted_global',
        }, 'Cisco-IOS-XR-clns-isis-cfg', _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-clns-isis-cfg']),
    'IsisRedistProto' : _MetaInfoEnum('IsisRedistProto',
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'IsisRedistProto',
        '''Isis redist proto''',
        {
            'connected':'connected',
            'static':'static',
            'ospf':'ospf',
            'bgp':'bgp',
            'isis':'isis',
            'ospfv3':'ospfv3',
            'rip':'rip',
            'eigrp':'eigrp',
            'subscriber':'subscriber',
            'application':'application',
            'mobile':'mobile',
        }, 'Cisco-IOS-XR-clns-isis-cfg', _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-clns-isis-cfg']),
    'IsisTracingMode' : _MetaInfoEnum('IsisTracingMode',
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'IsisTracingMode',
        '''Isis tracing mode''',
        {
            'off':'off',
            'basic':'basic',
            'enhanced':'enhanced',
        }, 'Cisco-IOS-XR-clns-isis-cfg', _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-clns-isis-cfg']),
    'IsisPrefixPriority' : _MetaInfoEnum('IsisPrefixPriority',
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'IsisPrefixPriority',
        '''Isis prefix priority''',
        {
            'critical-priority':'critical_priority',
            'high-priority':'high_priority',
            'medium-priority':'medium_priority',
        }, 'Cisco-IOS-XR-clns-isis-cfg', _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-clns-isis-cfg']),
    'IsisAuthenticationAlgorithm' : _MetaInfoEnum('IsisAuthenticationAlgorithm',
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'IsisAuthenticationAlgorithm',
        '''Isis authentication algorithm''',
        {
            'cleartext':'cleartext',
            'hmac-md5':'hmac_md5',
            'keychain':'keychain',
        }, 'Cisco-IOS-XR-clns-isis-cfg', _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-clns-isis-cfg']),
    'IsisMaxMetricMode' : _MetaInfoEnum('IsisMaxMetricMode',
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'IsisMaxMetricMode',
        '''Isis max metric mode''',
        {
            'permanently-set':'permanently_set',
            'startup-period':'startup_period',
            'wait-for-bgp':'wait_for_bgp',
        }, 'Cisco-IOS-XR-clns-isis-cfg', _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-clns-isis-cfg']),
    'IsisispfState' : _MetaInfoEnum('IsisispfState',
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'IsisispfState',
        '''Isisispf state''',
        {
            'enabled':'enabled',
        }, 'Cisco-IOS-XR-clns-isis-cfg', _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-clns-isis-cfg']),
    'IsisApplication' : _MetaInfoEnum('IsisApplication',
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'IsisApplication',
        '''Isis application''',
        {
            'lfa':'lfa',
        }, 'Cisco-IOS-XR-clns-isis-cfg', _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-clns-isis-cfg']),
    'IsissidProtected' : _MetaInfoEnum('IsissidProtected',
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'IsissidProtected',
        '''Isissid protected''',
        {
            'disable':'disable',
            'enable':'enable',
        }, 'Cisco-IOS-XR-clns-isis-cfg', _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-clns-isis-cfg']),
    'IsisAdvTypeExternal' : _MetaInfoEnum('IsisAdvTypeExternal',
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'IsisAdvTypeExternal',
        '''Isis adv type external''',
        {
            'external':'external',
        }, 'Cisco-IOS-XR-clns-isis-cfg', _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-clns-isis-cfg']),
    'IsisphpFlag' : _MetaInfoEnum('IsisphpFlag',
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'IsisphpFlag',
        '''Isisphp flag''',
        {
            'enable':'enable',
            'disable':'disable',
        }, 'Cisco-IOS-XR-clns-isis-cfg', _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-clns-isis-cfg']),
    'IsisMetricStyle' : _MetaInfoEnum('IsisMetricStyle',
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'IsisMetricStyle',
        '''Isis metric style''',
        {
            'old-metric-style':'old_metric_style',
            'new-metric-style':'new_metric_style',
            'both-metric-style':'both_metric_style',
            'old-metric-style-transition':'old_metric_style_transition',
            'new-metric-style-transition':'new_metric_style_transition',
        }, 'Cisco-IOS-XR-clns-isis-cfg', _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-clns-isis-cfg']),
    'IsisRemoteLfa' : _MetaInfoEnum('IsisRemoteLfa',
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'IsisRemoteLfa',
        '''Isis remote lfa''',
        {
            'remote-lfa-none':'remote_lfa_none',
            'remote-lfa-tunnel-ldp':'remote_lfa_tunnel_ldp',
        }, 'Cisco-IOS-XR-clns-isis-cfg', _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-clns-isis-cfg']),
    'IsisMicroLoopAvoidance' : _MetaInfoEnum('IsisMicroLoopAvoidance',
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'IsisMicroLoopAvoidance',
        '''Isis micro loop avoidance''',
        {
            'not-set':'not_set',
            'micro-loop-avoidance-all':'micro_loop_avoidance_all',
            'micro-loop-avoidance-protected':'micro_loop_avoidance_protected',
            'micro-loop-avoidance-segement-routing':'micro_loop_avoidance_segement_routing',
        }, 'Cisco-IOS-XR-clns-isis-cfg', _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-clns-isis-cfg']),
    'IsisAdjCheck' : _MetaInfoEnum('IsisAdjCheck',
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'IsisAdjCheck',
        '''Isis adj check''',
        {
            'disabled':'disabled',
        }, 'Cisco-IOS-XR-clns-isis-cfg', _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-clns-isis-cfg']),
    'IsisInterfaceFrrTiebreaker' : _MetaInfoEnum('IsisInterfaceFrrTiebreaker',
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'IsisInterfaceFrrTiebreaker',
        '''Isis interface frr tiebreaker''',
        {
            'node-protecting':'node_protecting',
            'srlg-disjoint':'srlg_disjoint',
        }, 'Cisco-IOS-XR-clns-isis-cfg', _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-clns-isis-cfg']),
    'IsisOverloadBitMode' : _MetaInfoEnum('IsisOverloadBitMode',
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'IsisOverloadBitMode',
        '''Isis overload bit mode''',
        {
            'permanently-set':'permanently_set',
            'startup-period':'startup_period',
            'wait-for-bgp':'wait_for_bgp',
        }, 'Cisco-IOS-XR-clns-isis-cfg', _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-clns-isis-cfg']),
    'IsisNsfFlavor' : _MetaInfoEnum('IsisNsfFlavor',
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'IsisNsfFlavor',
        '''Isis nsf flavor''',
        {
            'cisco-proprietary-nsf':'cisco_proprietary_nsf',
            'ietf-standard-nsf':'ietf_standard_nsf',
        }, 'Cisco-IOS-XR-clns-isis-cfg', _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-clns-isis-cfg']),
    'IsisfrrTiebreaker' : _MetaInfoEnum('IsisfrrTiebreaker',
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'IsisfrrTiebreaker',
        '''Isisfrr tiebreaker''',
        {
            'downstream':'downstream',
            'lc-disjoint':'lc_disjoint',
            'lowest-backup-metric':'lowest_backup_metric',
            'node-protecting':'node_protecting',
            'primary-path':'primary_path',
            'secondary-path':'secondary_path',
            'srlg-disjoint':'srlg_disjoint',
        }, 'Cisco-IOS-XR-clns-isis-cfg', _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-clns-isis-cfg']),
    'IsisMibManualAddressDropsBoolean' : _MetaInfoEnum('IsisMibManualAddressDropsBoolean',
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'IsisMibManualAddressDropsBoolean',
        '''Isis mib manual address drops boolean''',
        {
            'false':'false',
            'true':'true',
        }, 'Cisco-IOS-XR-clns-isis-cfg', _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-clns-isis-cfg']),
    'IsisMibAuthenticationTypeFailureBoolean' : _MetaInfoEnum('IsisMibAuthenticationTypeFailureBoolean',
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'IsisMibAuthenticationTypeFailureBoolean',
        '''Isis mib authentication type failure boolean''',
        {
            'false':'false',
            'true':'true',
        }, 'Cisco-IOS-XR-clns-isis-cfg', _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-clns-isis-cfg']),
    'IsisMibMaxAreaAddressMismatchBoolean' : _MetaInfoEnum('IsisMibMaxAreaAddressMismatchBoolean',
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'IsisMibMaxAreaAddressMismatchBoolean',
        '''Isis mib max area address mismatch boolean''',
        {
            'false':'false',
            'true':'true',
        }, 'Cisco-IOS-XR-clns-isis-cfg', _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-clns-isis-cfg']),
    'IsisMibSequenceNumberSkipBoolean' : _MetaInfoEnum('IsisMibSequenceNumberSkipBoolean',
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'IsisMibSequenceNumberSkipBoolean',
        '''Isis mib sequence number skip boolean''',
        {
            'false':'false',
            'true':'true',
        }, 'Cisco-IOS-XR-clns-isis-cfg', _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-clns-isis-cfg']),
    'IsisMibDatabaseOverFlowBoolean' : _MetaInfoEnum('IsisMibDatabaseOverFlowBoolean',
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'IsisMibDatabaseOverFlowBoolean',
        '''Isis mib database over flow boolean''',
        {
            'false':'false',
            'true':'true',
        }, 'Cisco-IOS-XR-clns-isis-cfg', _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-clns-isis-cfg']),
    'IsisMibAllBoolean' : _MetaInfoEnum('IsisMibAllBoolean',
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'IsisMibAllBoolean',
        '''Isis mib all boolean''',
        {
            'false':'false',
            'true':'true',
        }, 'Cisco-IOS-XR-clns-isis-cfg', _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-clns-isis-cfg']),
    'IsisMibLspTooLargeToPropagateBoolean' : _MetaInfoEnum('IsisMibLspTooLargeToPropagateBoolean',
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'IsisMibLspTooLargeToPropagateBoolean',
        '''Isis mib lsp too large to propagate boolean''',
        {
            'false':'false',
            'true':'true',
        }, 'Cisco-IOS-XR-clns-isis-cfg', _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-clns-isis-cfg']),
    'IsisMibOwnLspPurgeBoolean' : _MetaInfoEnum('IsisMibOwnLspPurgeBoolean',
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'IsisMibOwnLspPurgeBoolean',
        '''Isis mib own lsp purge boolean''',
        {
            'false':'false',
            'true':'true',
        }, 'Cisco-IOS-XR-clns-isis-cfg', _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-clns-isis-cfg']),
    'IsisMibAdjacencyChangeBoolean' : _MetaInfoEnum('IsisMibAdjacencyChangeBoolean',
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'IsisMibAdjacencyChangeBoolean',
        '''Isis mib adjacency change boolean''',
        {
            'false':'false',
            'true':'true',
        }, 'Cisco-IOS-XR-clns-isis-cfg', _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-clns-isis-cfg']),
    'IsisMibProtocolsSupportedMismatchBoolean' : _MetaInfoEnum('IsisMibProtocolsSupportedMismatchBoolean',
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'IsisMibProtocolsSupportedMismatchBoolean',
        '''Isis mib protocols supported mismatch boolean''',
        {
            'false':'false',
            'true':'true',
        }, 'Cisco-IOS-XR-clns-isis-cfg', _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-clns-isis-cfg']),
    'IsisMibAttemptToExceedMaxSequenceBoolean' : _MetaInfoEnum('IsisMibAttemptToExceedMaxSequenceBoolean',
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'IsisMibAttemptToExceedMaxSequenceBoolean',
        '''Isis mib attempt to exceed max sequence boolean''',
        {
            'false':'false',
            'true':'true',
        }, 'Cisco-IOS-XR-clns-isis-cfg', _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-clns-isis-cfg']),
    'IsisMibIdLengthMismatchBoolean' : _MetaInfoEnum('IsisMibIdLengthMismatchBoolean',
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'IsisMibIdLengthMismatchBoolean',
        '''Isis mib id length mismatch boolean''',
        {
            'false':'false',
            'true':'true',
        }, 'Cisco-IOS-XR-clns-isis-cfg', _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-clns-isis-cfg']),
    'IsisMibOriginatedLspBufferSizeMismatchBoolean' : _MetaInfoEnum('IsisMibOriginatedLspBufferSizeMismatchBoolean',
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'IsisMibOriginatedLspBufferSizeMismatchBoolean',
        '''Isis mib originated lsp buffer size mismatch
boolean''',
        {
            'false':'false',
            'true':'true',
        }, 'Cisco-IOS-XR-clns-isis-cfg', _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-clns-isis-cfg']),
    'IsisMibAreaMismatchBoolean' : _MetaInfoEnum('IsisMibAreaMismatchBoolean',
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'IsisMibAreaMismatchBoolean',
        '''Isis mib area mismatch boolean''',
        {
            'false':'false',
            'true':'true',
        }, 'Cisco-IOS-XR-clns-isis-cfg', _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-clns-isis-cfg']),
    'IsisMibCorruptedLspDetectedBoolean' : _MetaInfoEnum('IsisMibCorruptedLspDetectedBoolean',
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'IsisMibCorruptedLspDetectedBoolean',
        '''Isis mib corrupted lsp detected boolean''',
        {
            'false':'false',
            'true':'true',
        }, 'Cisco-IOS-XR-clns-isis-cfg', _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-clns-isis-cfg']),
    'IsisMibLspErrorDetectedBoolean' : _MetaInfoEnum('IsisMibLspErrorDetectedBoolean',
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'IsisMibLspErrorDetectedBoolean',
        '''Isis mib lsp error detected boolean''',
        {
            'false':'false',
            'true':'true',
        }, 'Cisco-IOS-XR-clns-isis-cfg', _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-clns-isis-cfg']),
    'IsisMibRejectedAdjacencyBoolean' : _MetaInfoEnum('IsisMibRejectedAdjacencyBoolean',
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'IsisMibRejectedAdjacencyBoolean',
        '''Isis mib rejected adjacency boolean''',
        {
            'false':'false',
            'true':'true',
        }, 'Cisco-IOS-XR-clns-isis-cfg', _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-clns-isis-cfg']),
    'IsisMibVersionSkewBoolean' : _MetaInfoEnum('IsisMibVersionSkewBoolean',
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'IsisMibVersionSkewBoolean',
        '''Isis mib version skew boolean''',
        {
            'false':'false',
            'true':'true',
        }, 'Cisco-IOS-XR-clns-isis-cfg', _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-clns-isis-cfg']),
    'IsisMibAuthenticationFailureBoolean' : _MetaInfoEnum('IsisMibAuthenticationFailureBoolean',
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'IsisMibAuthenticationFailureBoolean',
        '''Isis mib authentication failure boolean''',
        {
            'false':'false',
            'true':'true',
        }, 'Cisco-IOS-XR-clns-isis-cfg', _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-clns-isis-cfg']),
    'Isis.Instances.Instance.Srgb' : {
        'meta_info' : _MetaInfoClass('Isis.Instances.Instance.Srgb', REFERENCE_CLASS,
            '''Segment Routing Global Block configuration''',
            False, 
            [
            _MetaInfoClassMember('lower-bound', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('16000', '1048574')], [],
                '''                The lower bound of the SRGB
                ''',
                'lower_bound',
                'Cisco-IOS-XR-clns-isis-cfg', False, is_mandatory=True),
            _MetaInfoClassMember('upper-bound', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('16001', '1048575')], [],
                '''                The upper bound of the SRGB
                ''',
                'upper_bound',
                'Cisco-IOS-XR-clns-isis-cfg', False, is_mandatory=True),
            ],
            'Cisco-IOS-XR-clns-isis-cfg',
            'srgb',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-clns-isis-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg',
            is_presence=True,
        ),
    },
    'Isis.Instances.Instance.LspGenerationIntervals.LspGenerationInterval' : {
        'meta_info' : _MetaInfoClass('Isis.Instances.Instance.LspGenerationIntervals.LspGenerationInterval', REFERENCE_LIST,
            '''LSP generation scheduling parameters''',
            False, 
            [
            _MetaInfoClassMember('level', REFERENCE_ENUM_CLASS, 'IsisInternalLevel', 'dt1:Isis-internal-level',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_datatypes', 'IsisInternalLevel',
                [], [],
                '''                Level to which configuration applies
                ''',
                'level',
                'Cisco-IOS-XR-clns-isis-cfg', True),
            _MetaInfoClassMember('maximum-wait', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('0', '120000')], [],
                '''                Maximum wait before generating local LSP in
                milliseconds
                ''',
                'maximum_wait',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            _MetaInfoClassMember('initial-wait', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('0', '120000')], [],
                '''                Initial wait before generating local LSP in
                milliseconds
                ''',
                'initial_wait',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            _MetaInfoClassMember('secondary-wait', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('0', '120000')], [],
                '''                Secondary wait before generating local LSP
                in milliseconds
                ''',
                'secondary_wait',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            ],
            'Cisco-IOS-XR-clns-isis-cfg',
            'lsp-generation-interval',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-clns-isis-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg',
        ),
    },
    'Isis.Instances.Instance.LspGenerationIntervals' : {
        'meta_info' : _MetaInfoClass('Isis.Instances.Instance.LspGenerationIntervals', REFERENCE_CLASS,
            '''LSP generation-interval configuration''',
            False, 
            [
            _MetaInfoClassMember('lsp-generation-interval', REFERENCE_LIST, 'LspGenerationInterval', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'Isis.Instances.Instance.LspGenerationIntervals.LspGenerationInterval',
                [], [],
                '''                LSP generation scheduling parameters
                ''',
                'lsp_generation_interval',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            ],
            'Cisco-IOS-XR-clns-isis-cfg',
            'lsp-generation-intervals',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-clns-isis-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg',
        ),
    },
    'Isis.Instances.Instance.LspArrivalTimes.LspArrivalTime' : {
        'meta_info' : _MetaInfoClass('Isis.Instances.Instance.LspArrivalTimes.LspArrivalTime', REFERENCE_LIST,
            '''Minimum LSP arrival time''',
            False, 
            [
            _MetaInfoClassMember('level', REFERENCE_ENUM_CLASS, 'IsisInternalLevel', 'dt1:Isis-internal-level',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_datatypes', 'IsisInternalLevel',
                [], [],
                '''                Level to which configuration applies
                ''',
                'level',
                'Cisco-IOS-XR-clns-isis-cfg', True),
            _MetaInfoClassMember('maximum-wait', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('0', '120000')], [],
                '''                Maximum delay expected to take since last
                LSPin milliseconds
                ''',
                'maximum_wait',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            _MetaInfoClassMember('initial-wait', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('0', '120000')], [],
                '''                Initial delay expected to take since last
                LSPin milliseconds
                ''',
                'initial_wait',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            _MetaInfoClassMember('secondary-wait', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('0', '120000')], [],
                '''                Secondary delay expected to take since last
                LSPin milliseconds
                ''',
                'secondary_wait',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            ],
            'Cisco-IOS-XR-clns-isis-cfg',
            'lsp-arrival-time',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-clns-isis-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg',
        ),
    },
    'Isis.Instances.Instance.LspArrivalTimes' : {
        'meta_info' : _MetaInfoClass('Isis.Instances.Instance.LspArrivalTimes', REFERENCE_CLASS,
            '''LSP arrival time configuration''',
            False, 
            [
            _MetaInfoClassMember('lsp-arrival-time', REFERENCE_LIST, 'LspArrivalTime', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'Isis.Instances.Instance.LspArrivalTimes.LspArrivalTime',
                [], [],
                '''                Minimum LSP arrival time
                ''',
                'lsp_arrival_time',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            ],
            'Cisco-IOS-XR-clns-isis-cfg',
            'lsp-arrival-times',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-clns-isis-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg',
        ),
    },
    'Isis.Instances.Instance.TraceBufferSize' : {
        'meta_info' : _MetaInfoClass('Isis.Instances.Instance.TraceBufferSize', REFERENCE_CLASS,
            '''Trace buffer size configuration''',
            False, 
            [
            _MetaInfoClassMember('detailed', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('1', '1000000')], [],
                '''                Buffer size for detailed traces
                ''',
                'detailed',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            _MetaInfoClassMember('standard', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('1', '1000000')], [],
                '''                Buffer size for standard traces
                ''',
                'standard',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            _MetaInfoClassMember('severe', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('1', '1000000')], [],
                '''                Buffer size for severe trace
                ''',
                'severe',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            _MetaInfoClassMember('hello', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('1', '1000000')], [],
                '''                Buffer size for hello trace
                ''',
                'hello',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            ],
            'Cisco-IOS-XR-clns-isis-cfg',
            'trace-buffer-size',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-clns-isis-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg',
        ),
    },
    'Isis.Instances.Instance.MaxLinkMetrics.MaxLinkMetric' : {
        'meta_info' : _MetaInfoClass('Isis.Instances.Instance.MaxLinkMetrics.MaxLinkMetric', REFERENCE_LIST,
            '''Max Metric''',
            False, 
            [
            _MetaInfoClassMember('level', REFERENCE_ENUM_CLASS, 'IsisInternalLevel', 'dt1:Isis-internal-level',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_datatypes', 'IsisInternalLevel',
                [], [],
                '''                Level to which configuration applies
                ''',
                'level',
                'Cisco-IOS-XR-clns-isis-cfg', True),
            _MetaInfoClassMember('max-metric-mode', REFERENCE_ENUM_CLASS, 'IsisMaxMetricMode', 'Isis-max-metric-mode',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'IsisMaxMetricMode',
                [], [],
                '''                Circumstances under which the max metric is
                advertised in the system LSP
                ''',
                'max_metric_mode',
                'Cisco-IOS-XR-clns-isis-cfg', False, default_value='Cisco_IOS_XR_clns_isis_cfg.IsisMaxMetricMode.permanently_set'),
            _MetaInfoClassMember('max-metric-period', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('5', '86400')], [],
                '''                Time in seconds to advertise max link metric
                after process startup
                ''',
                'max_metric_period',
                'Cisco-IOS-XR-clns-isis-cfg', False, has_when=True),
            _MetaInfoClassMember('external', ATTRIBUTE, 'bool', 'boolean',
                None, None,
                [], [],
                '''                If TRUE, overwrite metric of prefixes
                learned from another protocol with max
                metric
                ''',
                'external',
                'Cisco-IOS-XR-clns-isis-cfg', False, default_value='False'),
            _MetaInfoClassMember('interlevel', ATTRIBUTE, 'bool', 'boolean',
                None, None,
                [], [],
                '''                If TRUE, overwrite metric of prefixes
                learned from another ISIS level with max
                metric
                ''',
                'interlevel',
                'Cisco-IOS-XR-clns-isis-cfg', False, default_value='False'),
            _MetaInfoClassMember('deflt-rt', ATTRIBUTE, 'bool', 'boolean',
                None, None,
                [], [],
                '''                If TRUE, overwrite metric of default route
                with max metric
                ''',
                'deflt_rt',
                'Cisco-IOS-XR-clns-isis-cfg', False, default_value='False'),
            _MetaInfoClassMember('srv6-loc', ATTRIBUTE, 'bool', 'boolean',
                None, None,
                [], [],
                '''                If TRUE, overwrite metric of segment routing
                IPV6 locator with max metric
                ''',
                'srv6_loc',
                'Cisco-IOS-XR-clns-isis-cfg', False, default_value='False'),
            ],
            'Cisco-IOS-XR-clns-isis-cfg',
            'max-link-metric',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-clns-isis-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg',
        ),
    },
    'Isis.Instances.Instance.MaxLinkMetrics' : {
        'meta_info' : _MetaInfoClass('Isis.Instances.Instance.MaxLinkMetrics', REFERENCE_CLASS,
            '''Max Metric configuration''',
            False, 
            [
            _MetaInfoClassMember('max-link-metric', REFERENCE_LIST, 'MaxLinkMetric', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'Isis.Instances.Instance.MaxLinkMetrics.MaxLinkMetric',
                [], [],
                '''                Max Metric
                ''',
                'max_link_metric',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            ],
            'Cisco-IOS-XR-clns-isis-cfg',
            'max-link-metrics',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-clns-isis-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg',
        ),
    },
    'Isis.Instances.Instance.AdjacencyStagger' : {
        'meta_info' : _MetaInfoClass('Isis.Instances.Instance.AdjacencyStagger', REFERENCE_CLASS,
            '''Stagger ISIS adjacency bring up''',
            False, 
            [
            _MetaInfoClassMember('initial-nbr', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('2', '65000')], [],
                '''                Adjacency Stagger: Initial number of
                neighbors to bring up per area
                ''',
                'initial_nbr',
                'Cisco-IOS-XR-clns-isis-cfg', False, default_value="2"),
            _MetaInfoClassMember('max-nbr', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('2', '65000')], [],
                '''                Adjacency Stagger: Subsequent simultaneous
                number of neighbors to bring up
                ''',
                'max_nbr',
                'Cisco-IOS-XR-clns-isis-cfg', False, default_value="64"),
            ],
            'Cisco-IOS-XR-clns-isis-cfg',
            'adjacency-stagger',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-clns-isis-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg',
            is_presence=True,
        ),
    },
    'Isis.Instances.Instance.Afs.Af.AfData.SegmentRouting.Srv6.Srv6Locators.Srv6Locator' : {
        'meta_info' : _MetaInfoClass('Isis.Instances.Instance.Afs.Af.AfData.SegmentRouting.Srv6.Srv6Locators.Srv6Locator', REFERENCE_LIST,
            '''Configuration for a single SRv6 Locator''',
            False, 
            [
            _MetaInfoClassMember('locator-name', ATTRIBUTE, 'str', 'dt1:Isis-locator-name',
                None, None,
                [(1, 60)], [],
                '''                Locator Name
                ''',
                'locator_name',
                'Cisco-IOS-XR-clns-isis-cfg', True),
            _MetaInfoClassMember('running', ATTRIBUTE, 'Empty', 'empty',
                None, None,
                [], [],
                '''                The presence of this object enables a
                SRv6 Locator. This must be the first
                object created under the SRv6Locator
                container, and the last one deleted
                ''',
                'running',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            ],
            'Cisco-IOS-XR-clns-isis-cfg',
            'srv6-locator',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-clns-isis-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg',
        ),
    },
    'Isis.Instances.Instance.Afs.Af.AfData.SegmentRouting.Srv6.Srv6Locators' : {
        'meta_info' : _MetaInfoClass('Isis.Instances.Instance.Afs.Af.AfData.SegmentRouting.Srv6.Srv6Locators', REFERENCE_CLASS,
            '''SRv6 Locator configuration''',
            False, 
            [
            _MetaInfoClassMember('srv6-locator', REFERENCE_LIST, 'Srv6Locator', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'Isis.Instances.Instance.Afs.Af.AfData.SegmentRouting.Srv6.Srv6Locators.Srv6Locator',
                [], [],
                '''                Configuration for a single SRv6 Locator
                ''',
                'srv6_locator',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            ],
            'Cisco-IOS-XR-clns-isis-cfg',
            'srv6-locators',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-clns-isis-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg',
        ),
    },
    'Isis.Instances.Instance.Afs.Af.AfData.SegmentRouting.Srv6' : {
        'meta_info' : _MetaInfoClass('Isis.Instances.Instance.Afs.Af.AfData.SegmentRouting.Srv6', REFERENCE_CLASS,
            '''SRv6 configuration''',
            False, 
            [
            _MetaInfoClassMember('srv6-locators', REFERENCE_CLASS, 'Srv6Locators', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'Isis.Instances.Instance.Afs.Af.AfData.SegmentRouting.Srv6.Srv6Locators',
                [], [],
                '''                SRv6 Locator configuration
                ''',
                'srv6_locators',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            _MetaInfoClassMember('running', ATTRIBUTE, 'Empty', 'empty',
                None, None,
                [], [],
                '''                The presence of this object enables SRv6.
                This must be the first object created
                under the SRV6 container, and the last
                one deleted
                ''',
                'running',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            ],
            'Cisco-IOS-XR-clns-isis-cfg',
            'srv6',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-clns-isis-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg',
        ),
    },
    'Isis.Instances.Instance.Afs.Af.AfData.SegmentRouting.ConnectedPrefixSids.ConnectedPrefixSid' : {
        'meta_info' : _MetaInfoClass('Isis.Instances.Instance.Afs.Af.AfData.SegmentRouting.ConnectedPrefixSids.ConnectedPrefixSid', REFERENCE_LIST,
            '''Segment Routing prefix SID map''',
            False, 
            [
            _MetaInfoClassMember('address-prefix', REFERENCE_UNION, 'str', 'inet:ip-prefix',
                None, None,
                [], [],
                '''                IP address prefix
                ''',
                'address_prefix',
                'Cisco-IOS-XR-clns-isis-cfg', True, [
                    _MetaInfoClassMember('address-prefix', ATTRIBUTE, 'str', 'inet:ipv4-prefix',
                        None, None,
                        [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])/(([0-9])|([1-2][0-9])|(3[0-2]))'],
                        '''                        IP address prefix
                        ''',
                        'address_prefix',
                        'Cisco-IOS-XR-clns-isis-cfg', True),
                    _MetaInfoClassMember('address-prefix', ATTRIBUTE, 'str', 'inet:ipv6-prefix',
                        None, None,
                        [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(/(([0-9])|([0-9]{2})|(1[0-1][0-9])|(12[0-8])))'],
                        '''                        IP address prefix
                        ''',
                        'address_prefix',
                        'Cisco-IOS-XR-clns-isis-cfg', True),
                ]),
            _MetaInfoClassMember('algo', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('0', '255')], [],
                '''                Algo
                ''',
                'algo',
                'Cisco-IOS-XR-clns-isis-cfg', True),
            _MetaInfoClassMember('sid-type', REFERENCE_ENUM_CLASS, 'Isissid1', 'Isissid1',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'Isissid1',
                [], [],
                '''                SID type for the interface
                ''',
                'sid_type',
                'Cisco-IOS-XR-clns-isis-cfg', False, is_mandatory=True),
            _MetaInfoClassMember('sid', ATTRIBUTE, 'int', 'Isissid',
                None, None,
                [('0', '1048575')], [],
                '''                SID value for the interface
                ''',
                'sid',
                'Cisco-IOS-XR-clns-isis-cfg', False, is_mandatory=True),
            _MetaInfoClassMember('sid-range', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('1', '1048575')], [],
                '''                Range of SIDs
                ''',
                'sid_range',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            _MetaInfoClassMember('interface', ATTRIBUTE, 'str', 'string',
                None, None,
                [(1, 64)], [],
                '''                Interface to which prefix belongs
                ''',
                'interface',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            _MetaInfoClassMember('php', REFERENCE_ENUM_CLASS, 'IsisphpFlag', 'Isisphp-flag',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'IsisphpFlag',
                [], [],
                '''                Enable/Disable Penultimate Hop Popping
                ''',
                'php',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            _MetaInfoClassMember('explicit-null', REFERENCE_ENUM_CLASS, 'IsisexplicitNullFlag', 'Isisexplicit-null-flag',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'IsisexplicitNullFlag',
                [], [],
                '''                Enable/Disable Explicit-NULL flag
                ''',
                'explicit_null',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            ],
            'Cisco-IOS-XR-clns-isis-cfg',
            'connected-prefix-sid',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-clns-isis-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg',
        ),
    },
    'Isis.Instances.Instance.Afs.Af.AfData.SegmentRouting.ConnectedPrefixSids' : {
        'meta_info' : _MetaInfoClass('Isis.Instances.Instance.Afs.Af.AfData.SegmentRouting.ConnectedPrefixSids', REFERENCE_CLASS,
            '''Connected Segment Routing prefix SID map
configuration''',
            False, 
            [
            _MetaInfoClassMember('connected-prefix-sid', REFERENCE_LIST, 'ConnectedPrefixSid', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'Isis.Instances.Instance.Afs.Af.AfData.SegmentRouting.ConnectedPrefixSids.ConnectedPrefixSid',
                [], [],
                '''                Segment Routing prefix SID map
                ''',
                'connected_prefix_sid',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            ],
            'Cisco-IOS-XR-clns-isis-cfg',
            'connected-prefix-sids',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-clns-isis-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg',
        ),
    },
    'Isis.Instances.Instance.Afs.Af.AfData.SegmentRouting.PrefixSidMap' : {
        'meta_info' : _MetaInfoClass('Isis.Instances.Instance.Afs.Af.AfData.SegmentRouting.PrefixSidMap', REFERENCE_CLASS,
            '''Enable Segment Routing prefix SID map
configuration''',
            False, 
            [
            _MetaInfoClassMember('advertise-local', ATTRIBUTE, 'Empty', 'empty',
                None, None,
                [], [],
                '''                Enable Segment Routing prefix SID map
                advertise local
                ''',
                'advertise_local',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            _MetaInfoClassMember('receive', ATTRIBUTE, 'bool', 'boolean',
                None, None,
                [], [],
                '''                If TRUE, remote prefix SID map
                advertisements will be used. If FALSE,
                they will not be used.
                ''',
                'receive',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            ],
            'Cisco-IOS-XR-clns-isis-cfg',
            'prefix-sid-map',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-clns-isis-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg',
        ),
    },
    'Isis.Instances.Instance.Afs.Af.AfData.SegmentRouting' : {
        'meta_info' : _MetaInfoClass('Isis.Instances.Instance.Afs.Af.AfData.SegmentRouting', REFERENCE_CLASS,
            '''Enable Segment Routing configuration''',
            False, 
            [
            _MetaInfoClassMember('srv6', REFERENCE_CLASS, 'Srv6', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'Isis.Instances.Instance.Afs.Af.AfData.SegmentRouting.Srv6',
                [], [],
                '''                SRv6 configuration
                ''',
                'srv6',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            _MetaInfoClassMember('connected-prefix-sids', REFERENCE_CLASS, 'ConnectedPrefixSids', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'Isis.Instances.Instance.Afs.Af.AfData.SegmentRouting.ConnectedPrefixSids',
                [], [],
                '''                Connected Segment Routing prefix SID map
                configuration
                ''',
                'connected_prefix_sids',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            _MetaInfoClassMember('prefix-sid-map', REFERENCE_CLASS, 'PrefixSidMap', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'Isis.Instances.Instance.Afs.Af.AfData.SegmentRouting.PrefixSidMap',
                [], [],
                '''                Enable Segment Routing prefix SID map
                configuration
                ''',
                'prefix_sid_map',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            _MetaInfoClassMember('bundle-member-adj-sid', ATTRIBUTE, 'Empty', 'empty',
                None, None,
                [], [],
                '''                Enable per bundle member adjacency SID
                ''',
                'bundle_member_adj_sid',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            _MetaInfoClassMember('labeled-only', ATTRIBUTE, 'Empty', 'empty',
                None, None,
                [], [],
                '''                Only install SR labeled paths
                ''',
                'labeled_only',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            _MetaInfoClassMember('mpls', REFERENCE_ENUM_CLASS, 'IsisLabelPreference', 'Isis-label-preference',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'IsisLabelPreference',
                [], [],
                '''                Prefer segment routing labels over LDP
                labels
                ''',
                'mpls',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            ],
            'Cisco-IOS-XR-clns-isis-cfg',
            'segment-routing',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-clns-isis-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg',
        ),
    },
    'Isis.Instances.Instance.Afs.Af.AfData.MetricStyles.MetricStyle' : {
        'meta_info' : _MetaInfoClass('Isis.Instances.Instance.Afs.Af.AfData.MetricStyles.MetricStyle', REFERENCE_LIST,
            '''Configuration of metric style in LSPs''',
            False, 
            [
            _MetaInfoClassMember('level', REFERENCE_ENUM_CLASS, 'IsisInternalLevel', 'dt1:Isis-internal-level',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_datatypes', 'IsisInternalLevel',
                [], [],
                '''                Level to which configuration applies
                ''',
                'level',
                'Cisco-IOS-XR-clns-isis-cfg', True),
            _MetaInfoClassMember('style', REFERENCE_ENUM_CLASS, 'IsisMetricStyle', 'Isis-metric-style',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'IsisMetricStyle',
                [], [],
                '''                Metric Style
                ''',
                'style',
                'Cisco-IOS-XR-clns-isis-cfg', False, is_mandatory=True),
            ],
            'Cisco-IOS-XR-clns-isis-cfg',
            'metric-style',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-clns-isis-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg',
        ),
    },
    'Isis.Instances.Instance.Afs.Af.AfData.MetricStyles' : {
        'meta_info' : _MetaInfoClass('Isis.Instances.Instance.Afs.Af.AfData.MetricStyles', REFERENCE_CLASS,
            '''Metric-style configuration''',
            False, 
            [
            _MetaInfoClassMember('metric-style', REFERENCE_LIST, 'MetricStyle', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'Isis.Instances.Instance.Afs.Af.AfData.MetricStyles.MetricStyle',
                [], [],
                '''                Configuration of metric style in LSPs
                ''',
                'metric_style',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            ],
            'Cisco-IOS-XR-clns-isis-cfg',
            'metric-styles',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-clns-isis-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg',
        ),
    },
    'Isis.Instances.Instance.Afs.Af.AfData.FrrTable.FrrLoadSharings.FrrLoadSharing' : {
        'meta_info' : _MetaInfoClass('Isis.Instances.Instance.Afs.Af.AfData.FrrTable.FrrLoadSharings.FrrLoadSharing', REFERENCE_LIST,
            '''Disable load sharing''',
            False, 
            [
            _MetaInfoClassMember('level', REFERENCE_ENUM_CLASS, 'IsisInternalLevel', 'dt1:Isis-internal-level',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_datatypes', 'IsisInternalLevel',
                [], [],
                '''                Level to which configuration applies
                ''',
                'level',
                'Cisco-IOS-XR-clns-isis-cfg', True),
            _MetaInfoClassMember('load-sharing', REFERENCE_ENUM_CLASS, 'IsisfrrLoadSharing', 'Isisfrr-load-sharing',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'IsisfrrLoadSharing',
                [], [],
                '''                Load sharing
                ''',
                'load_sharing',
                'Cisco-IOS-XR-clns-isis-cfg', False, is_mandatory=True),
            ],
            'Cisco-IOS-XR-clns-isis-cfg',
            'frr-load-sharing',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-clns-isis-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg',
        ),
    },
    'Isis.Instances.Instance.Afs.Af.AfData.FrrTable.FrrLoadSharings' : {
        'meta_info' : _MetaInfoClass('Isis.Instances.Instance.Afs.Af.AfData.FrrTable.FrrLoadSharings', REFERENCE_CLASS,
            '''Load share prefixes across multiple
backups''',
            False, 
            [
            _MetaInfoClassMember('frr-load-sharing', REFERENCE_LIST, 'FrrLoadSharing', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'Isis.Instances.Instance.Afs.Af.AfData.FrrTable.FrrLoadSharings.FrrLoadSharing',
                [], [],
                '''                Disable load sharing
                ''',
                'frr_load_sharing',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            ],
            'Cisco-IOS-XR-clns-isis-cfg',
            'frr-load-sharings',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-clns-isis-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg',
        ),
    },
    'Isis.Instances.Instance.Afs.Af.AfData.FrrTable.FrrsrlgProtectionTypes.FrrsrlgProtectionType' : {
        'meta_info' : _MetaInfoClass('Isis.Instances.Instance.Afs.Af.AfData.FrrTable.FrrsrlgProtectionTypes.FrrsrlgProtectionType', REFERENCE_LIST,
            '''FRR SRLG Protection Type''',
            False, 
            [
            _MetaInfoClassMember('level', REFERENCE_ENUM_CLASS, 'IsisInternalLevel', 'dt1:Isis-internal-level',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_datatypes', 'IsisInternalLevel',
                [], [],
                '''                Level to which configuration applies
                ''',
                'level',
                'Cisco-IOS-XR-clns-isis-cfg', True),
            _MetaInfoClassMember('protection-type', REFERENCE_ENUM_CLASS, 'IsisfrrSrlgProtection', 'Isisfrr-srlg-protection',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'IsisfrrSrlgProtection',
                [], [],
                '''                Protection Type
                ''',
                'protection_type',
                'Cisco-IOS-XR-clns-isis-cfg', False, is_mandatory=True),
            ],
            'Cisco-IOS-XR-clns-isis-cfg',
            'frrsrlg-protection-type',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-clns-isis-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg',
        ),
    },
    'Isis.Instances.Instance.Afs.Af.AfData.FrrTable.FrrsrlgProtectionTypes' : {
        'meta_info' : _MetaInfoClass('Isis.Instances.Instance.Afs.Af.AfData.FrrTable.FrrsrlgProtectionTypes', REFERENCE_CLASS,
            '''SRLG protection type configuration''',
            False, 
            [
            _MetaInfoClassMember('frrsrlg-protection-type', REFERENCE_LIST, 'FrrsrlgProtectionType', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'Isis.Instances.Instance.Afs.Af.AfData.FrrTable.FrrsrlgProtectionTypes.FrrsrlgProtectionType',
                [], [],
                '''                FRR SRLG Protection Type
                ''',
                'frrsrlg_protection_type',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            ],
            'Cisco-IOS-XR-clns-isis-cfg',
            'frrsrlg-protection-types',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-clns-isis-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg',
        ),
    },
    'Isis.Instances.Instance.Afs.Af.AfData.FrrTable.PriorityLimits.PriorityLimit' : {
        'meta_info' : _MetaInfoClass('Isis.Instances.Instance.Afs.Af.AfData.FrrTable.PriorityLimits.PriorityLimit', REFERENCE_LIST,
            '''Limit backup computation upto the prefix
priority''',
            False, 
            [
            _MetaInfoClassMember('level', REFERENCE_ENUM_CLASS, 'IsisInternalLevel', 'dt1:Isis-internal-level',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_datatypes', 'IsisInternalLevel',
                [], [],
                '''                Level to which configuration applies
                ''',
                'level',
                'Cisco-IOS-XR-clns-isis-cfg', True),
            _MetaInfoClassMember('frr-type', REFERENCE_ENUM_CLASS, 'Isisfrr', 'Isisfrr',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'Isisfrr',
                [], [],
                '''                Computation Type
                ''',
                'frr_type',
                'Cisco-IOS-XR-clns-isis-cfg', True),
            _MetaInfoClassMember('priority', REFERENCE_ENUM_CLASS, 'IsisPrefixPriority', 'Isis-prefix-priority',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'IsisPrefixPriority',
                [], [],
                '''                Compute for all prefixes upto the
                specified priority
                ''',
                'priority',
                'Cisco-IOS-XR-clns-isis-cfg', False, is_mandatory=True),
            ],
            'Cisco-IOS-XR-clns-isis-cfg',
            'priority-limit',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-clns-isis-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg',
        ),
    },
    'Isis.Instances.Instance.Afs.Af.AfData.FrrTable.PriorityLimits' : {
        'meta_info' : _MetaInfoClass('Isis.Instances.Instance.Afs.Af.AfData.FrrTable.PriorityLimits', REFERENCE_CLASS,
            '''FRR prefix-limit configuration''',
            False, 
            [
            _MetaInfoClassMember('priority-limit', REFERENCE_LIST, 'PriorityLimit', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'Isis.Instances.Instance.Afs.Af.AfData.FrrTable.PriorityLimits.PriorityLimit',
                [], [],
                '''                Limit backup computation upto the prefix
                priority
                ''',
                'priority_limit',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            ],
            'Cisco-IOS-XR-clns-isis-cfg',
            'priority-limits',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-clns-isis-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg',
        ),
    },
    'Isis.Instances.Instance.Afs.Af.AfData.FrrTable.FrrRemoteLfaPrefixes.FrrRemoteLfaPrefix' : {
        'meta_info' : _MetaInfoClass('Isis.Instances.Instance.Afs.Af.AfData.FrrTable.FrrRemoteLfaPrefixes.FrrRemoteLfaPrefix', REFERENCE_LIST,
            '''Filter remote LFA router IDs using
prefix-list''',
            False, 
            [
            _MetaInfoClassMember('level', REFERENCE_ENUM_CLASS, 'IsisInternalLevel', 'dt1:Isis-internal-level',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_datatypes', 'IsisInternalLevel',
                [], [],
                '''                Level to which configuration applies
                ''',
                'level',
                'Cisco-IOS-XR-clns-isis-cfg', True),
            _MetaInfoClassMember('prefix-list-name', ATTRIBUTE, 'str', 'xr:Cisco-ios-xr-string',
                None, None,
                [(1, 32)], [],
                '''                Name of the prefix list
                ''',
                'prefix_list_name',
                'Cisco-IOS-XR-clns-isis-cfg', False, is_mandatory=True),
            ],
            'Cisco-IOS-XR-clns-isis-cfg',
            'frr-remote-lfa-prefix',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-clns-isis-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg',
        ),
    },
    'Isis.Instances.Instance.Afs.Af.AfData.FrrTable.FrrRemoteLfaPrefixes' : {
        'meta_info' : _MetaInfoClass('Isis.Instances.Instance.Afs.Af.AfData.FrrTable.FrrRemoteLfaPrefixes', REFERENCE_CLASS,
            '''FRR remote LFA prefix list filter
configuration''',
            False, 
            [
            _MetaInfoClassMember('frr-remote-lfa-prefix', REFERENCE_LIST, 'FrrRemoteLfaPrefix', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'Isis.Instances.Instance.Afs.Af.AfData.FrrTable.FrrRemoteLfaPrefixes.FrrRemoteLfaPrefix',
                [], [],
                '''                Filter remote LFA router IDs using
                prefix-list
                ''',
                'frr_remote_lfa_prefix',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            ],
            'Cisco-IOS-XR-clns-isis-cfg',
            'frr-remote-lfa-prefixes',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-clns-isis-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg',
        ),
    },
    'Isis.Instances.Instance.Afs.Af.AfData.FrrTable.FrrTiebreakers.FrrTiebreaker' : {
        'meta_info' : _MetaInfoClass('Isis.Instances.Instance.Afs.Af.AfData.FrrTable.FrrTiebreakers.FrrTiebreaker', REFERENCE_LIST,
            '''Configure tiebreaker for multiple backups''',
            False, 
            [
            _MetaInfoClassMember('level', REFERENCE_ENUM_CLASS, 'IsisInternalLevel', 'dt1:Isis-internal-level',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_datatypes', 'IsisInternalLevel',
                [], [],
                '''                Level to which configuration applies
                ''',
                'level',
                'Cisco-IOS-XR-clns-isis-cfg', True),
            _MetaInfoClassMember('tiebreaker', REFERENCE_ENUM_CLASS, 'IsisfrrTiebreaker', 'Isisfrr-tiebreaker',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'IsisfrrTiebreaker',
                [], [],
                '''                Tiebreaker for which configuration
                applies
                ''',
                'tiebreaker',
                'Cisco-IOS-XR-clns-isis-cfg', True),
            _MetaInfoClassMember('index', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('1', '255')], [],
                '''                Preference order among tiebreakers
                ''',
                'index',
                'Cisco-IOS-XR-clns-isis-cfg', False, is_mandatory=True),
            ],
            'Cisco-IOS-XR-clns-isis-cfg',
            'frr-tiebreaker',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-clns-isis-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg',
        ),
    },
    'Isis.Instances.Instance.Afs.Af.AfData.FrrTable.FrrTiebreakers' : {
        'meta_info' : _MetaInfoClass('Isis.Instances.Instance.Afs.Af.AfData.FrrTable.FrrTiebreakers', REFERENCE_CLASS,
            '''FRR tiebreakers configuration''',
            False, 
            [
            _MetaInfoClassMember('frr-tiebreaker', REFERENCE_LIST, 'FrrTiebreaker', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'Isis.Instances.Instance.Afs.Af.AfData.FrrTable.FrrTiebreakers.FrrTiebreaker',
                [], [],
                '''                Configure tiebreaker for multiple backups
                ''',
                'frr_tiebreaker',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            ],
            'Cisco-IOS-XR-clns-isis-cfg',
            'frr-tiebreakers',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-clns-isis-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg',
        ),
    },
    'Isis.Instances.Instance.Afs.Af.AfData.FrrTable.FrrUseCandOnlies.FrrUseCandOnly' : {
        'meta_info' : _MetaInfoClass('Isis.Instances.Instance.Afs.Af.AfData.FrrTable.FrrUseCandOnlies.FrrUseCandOnly', REFERENCE_LIST,
            '''Configure use candidate only to exclude
interfaces as backup''',
            False, 
            [
            _MetaInfoClassMember('level', REFERENCE_ENUM_CLASS, 'IsisInternalLevel', 'dt1:Isis-internal-level',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_datatypes', 'IsisInternalLevel',
                [], [],
                '''                Level to which configuration applies
                ''',
                'level',
                'Cisco-IOS-XR-clns-isis-cfg', True),
            _MetaInfoClassMember('frr-type', REFERENCE_ENUM_CLASS, 'Isisfrr', 'Isisfrr',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'Isisfrr',
                [], [],
                '''                Computation Type
                ''',
                'frr_type',
                'Cisco-IOS-XR-clns-isis-cfg', True),
            ],
            'Cisco-IOS-XR-clns-isis-cfg',
            'frr-use-cand-only',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-clns-isis-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg',
        ),
    },
    'Isis.Instances.Instance.Afs.Af.AfData.FrrTable.FrrUseCandOnlies' : {
        'meta_info' : _MetaInfoClass('Isis.Instances.Instance.Afs.Af.AfData.FrrTable.FrrUseCandOnlies', REFERENCE_CLASS,
            '''FRR use candidate only configuration''',
            False, 
            [
            _MetaInfoClassMember('frr-use-cand-only', REFERENCE_LIST, 'FrrUseCandOnly', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'Isis.Instances.Instance.Afs.Af.AfData.FrrTable.FrrUseCandOnlies.FrrUseCandOnly',
                [], [],
                '''                Configure use candidate only to exclude
                interfaces as backup
                ''',
                'frr_use_cand_only',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            ],
            'Cisco-IOS-XR-clns-isis-cfg',
            'frr-use-cand-onlies',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-clns-isis-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg',
        ),
    },
    'Isis.Instances.Instance.Afs.Af.AfData.FrrTable' : {
        'meta_info' : _MetaInfoClass('Isis.Instances.Instance.Afs.Af.AfData.FrrTable', REFERENCE_CLASS,
            '''Fast-ReRoute configuration''',
            False, 
            [
            _MetaInfoClassMember('frr-load-sharings', REFERENCE_CLASS, 'FrrLoadSharings', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'Isis.Instances.Instance.Afs.Af.AfData.FrrTable.FrrLoadSharings',
                [], [],
                '''                Load share prefixes across multiple
                backups
                ''',
                'frr_load_sharings',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            _MetaInfoClassMember('frrsrlg-protection-types', REFERENCE_CLASS, 'FrrsrlgProtectionTypes', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'Isis.Instances.Instance.Afs.Af.AfData.FrrTable.FrrsrlgProtectionTypes',
                [], [],
                '''                SRLG protection type configuration
                ''',
                'frrsrlg_protection_types',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            _MetaInfoClassMember('priority-limits', REFERENCE_CLASS, 'PriorityLimits', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'Isis.Instances.Instance.Afs.Af.AfData.FrrTable.PriorityLimits',
                [], [],
                '''                FRR prefix-limit configuration
                ''',
                'priority_limits',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            _MetaInfoClassMember('frr-remote-lfa-prefixes', REFERENCE_CLASS, 'FrrRemoteLfaPrefixes', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'Isis.Instances.Instance.Afs.Af.AfData.FrrTable.FrrRemoteLfaPrefixes',
                [], [],
                '''                FRR remote LFA prefix list filter
                configuration
                ''',
                'frr_remote_lfa_prefixes',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            _MetaInfoClassMember('frr-tiebreakers', REFERENCE_CLASS, 'FrrTiebreakers', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'Isis.Instances.Instance.Afs.Af.AfData.FrrTable.FrrTiebreakers',
                [], [],
                '''                FRR tiebreakers configuration
                ''',
                'frr_tiebreakers',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            _MetaInfoClassMember('frr-use-cand-onlies', REFERENCE_CLASS, 'FrrUseCandOnlies', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'Isis.Instances.Instance.Afs.Af.AfData.FrrTable.FrrUseCandOnlies',
                [], [],
                '''                FRR use candidate only configuration
                ''',
                'frr_use_cand_onlies',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            _MetaInfoClassMember('frr-initial-delay', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('100', '60000')], [],
                '''                Delay before running FRR (milliseconds)
                ''',
                'frr_initial_delay',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            ],
            'Cisco-IOS-XR-clns-isis-cfg',
            'frr-table',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-clns-isis-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg',
        ),
    },
    'Isis.Instances.Instance.Afs.Af.AfData.RouterId' : {
        'meta_info' : _MetaInfoClass('Isis.Instances.Instance.Afs.Af.AfData.RouterId', REFERENCE_CLASS,
            '''Stable IP address for system. Will only be
applied for the unicast sub-address-family.''',
            False, 
            [
            _MetaInfoClassMember('address', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                IPv4/IPv6 address to be used as a router
                ID. Precisely one of Address and Interface
                must be specified.
                ''',
                'address',
                'Cisco-IOS-XR-clns-isis-cfg', False, has_must=True),
            _MetaInfoClassMember('interface-name', ATTRIBUTE, 'str', 'xr:Interface-name',
                None, None,
                [], [b'[a-zA-Z0-9._/-]+'],
                '''                Interface with designated stable IP
                address to be used as a router ID. This
                must be a Loopback interface. Precisely
                one of Address and Interface must be
                specified.
                ''',
                'interface_name',
                'Cisco-IOS-XR-clns-isis-cfg', False, has_must=True),
            ],
            'Cisco-IOS-XR-clns-isis-cfg',
            'router-id',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-clns-isis-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg',
        ),
    },
    'Isis.Instances.Instance.Afs.Af.AfData.SpfPrefixPriorities.SpfPrefixPriority' : {
        'meta_info' : _MetaInfoClass('Isis.Instances.Instance.Afs.Af.AfData.SpfPrefixPriorities.SpfPrefixPriority', REFERENCE_LIST,
            '''Determine SPF priority for prefixes''',
            False, 
            [
            _MetaInfoClassMember('level', REFERENCE_ENUM_CLASS, 'IsisInternalLevel', 'dt1:Isis-internal-level',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_datatypes', 'IsisInternalLevel',
                [], [],
                '''                SPF Level for prefix prioritization
                ''',
                'level',
                'Cisco-IOS-XR-clns-isis-cfg', True),
            _MetaInfoClassMember('prefix-priority-type', REFERENCE_ENUM_CLASS, 'IsisPrefixPriority', 'Isis-prefix-priority',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'IsisPrefixPriority',
                [], [],
                '''                SPF Priority to assign matching prefixes
                ''',
                'prefix_priority_type',
                'Cisco-IOS-XR-clns-isis-cfg', True),
            _MetaInfoClassMember('admin-tag', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('1', '4294967295')], [],
                '''                Tag value to determine prefixes for this
                priority
                ''',
                'admin_tag',
                'Cisco-IOS-XR-clns-isis-cfg', False, has_must=True),
            _MetaInfoClassMember('access-list-name', ATTRIBUTE, 'str', 'xr:Cisco-ios-xr-string',
                None, None,
                [(1, 64)], [],
                '''                Access List to determine prefixes for
                this priority
                ''',
                'access_list_name',
                'Cisco-IOS-XR-clns-isis-cfg', False, has_must=True),
            ],
            'Cisco-IOS-XR-clns-isis-cfg',
            'spf-prefix-priority',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-clns-isis-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg',
        ),
    },
    'Isis.Instances.Instance.Afs.Af.AfData.SpfPrefixPriorities' : {
        'meta_info' : _MetaInfoClass('Isis.Instances.Instance.Afs.Af.AfData.SpfPrefixPriorities', REFERENCE_CLASS,
            '''SPF Prefix Priority configuration''',
            False, 
            [
            _MetaInfoClassMember('spf-prefix-priority', REFERENCE_LIST, 'SpfPrefixPriority', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'Isis.Instances.Instance.Afs.Af.AfData.SpfPrefixPriorities.SpfPrefixPriority',
                [], [],
                '''                Determine SPF priority for prefixes
                ''',
                'spf_prefix_priority',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            ],
            'Cisco-IOS-XR-clns-isis-cfg',
            'spf-prefix-priorities',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-clns-isis-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg',
        ),
    },
    'Isis.Instances.Instance.Afs.Af.AfData.SummaryPrefixes.SummaryPrefix' : {
        'meta_info' : _MetaInfoClass('Isis.Instances.Instance.Afs.Af.AfData.SummaryPrefixes.SummaryPrefix', REFERENCE_LIST,
            '''Configure IP address prefixes to advertise''',
            False, 
            [
            _MetaInfoClassMember('address-prefix', REFERENCE_UNION, 'str', 'inet:ip-prefix',
                None, None,
                [], [],
                '''                IP summary address prefix
                ''',
                'address_prefix',
                'Cisco-IOS-XR-clns-isis-cfg', True, [
                    _MetaInfoClassMember('address-prefix', ATTRIBUTE, 'str', 'inet:ipv4-prefix',
                        None, None,
                        [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])/(([0-9])|([1-2][0-9])|(3[0-2]))'],
                        '''                        IP summary address prefix
                        ''',
                        'address_prefix',
                        'Cisco-IOS-XR-clns-isis-cfg', True),
                    _MetaInfoClassMember('address-prefix', ATTRIBUTE, 'str', 'inet:ipv6-prefix',
                        None, None,
                        [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(/(([0-9])|([0-9]{2})|(1[0-1][0-9])|(12[0-8])))'],
                        '''                        IP summary address prefix
                        ''',
                        'address_prefix',
                        'Cisco-IOS-XR-clns-isis-cfg', True),
                ]),
            _MetaInfoClassMember('tag', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('1', '4294967295')], [],
                '''                The tag value
                ''',
                'tag',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            _MetaInfoClassMember('level', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('1', '2')], [],
                '''                Level in which to summarize routes
                ''',
                'level',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            ],
            'Cisco-IOS-XR-clns-isis-cfg',
            'summary-prefix',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-clns-isis-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg',
        ),
    },
    'Isis.Instances.Instance.Afs.Af.AfData.SummaryPrefixes' : {
        'meta_info' : _MetaInfoClass('Isis.Instances.Instance.Afs.Af.AfData.SummaryPrefixes', REFERENCE_CLASS,
            '''Summary-prefix configuration''',
            False, 
            [
            _MetaInfoClassMember('summary-prefix', REFERENCE_LIST, 'SummaryPrefix', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'Isis.Instances.Instance.Afs.Af.AfData.SummaryPrefixes.SummaryPrefix',
                [], [],
                '''                Configure IP address prefixes to advertise
                ''',
                'summary_prefix',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            ],
            'Cisco-IOS-XR-clns-isis-cfg',
            'summary-prefixes',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-clns-isis-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg',
        ),
    },
    'Isis.Instances.Instance.Afs.Af.AfData.MicroLoopAvoidance' : {
        'meta_info' : _MetaInfoClass('Isis.Instances.Instance.Afs.Af.AfData.MicroLoopAvoidance', REFERENCE_CLASS,
            '''Micro Loop Avoidance configuration''',
            False, 
            [
            _MetaInfoClassMember('enable', REFERENCE_ENUM_CLASS, 'IsisMicroLoopAvoidance', 'Isis-micro-loop-avoidance',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'IsisMicroLoopAvoidance',
                [], [],
                '''                MicroLoop avoidance enable configuration
                ''',
                'enable',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            _MetaInfoClassMember('rib-update-delay', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('1000', '65535')], [],
                '''                Value of delay in msecs in updating RIB
                ''',
                'rib_update_delay',
                'Cisco-IOS-XR-clns-isis-cfg', False, default_value="5000"),
            ],
            'Cisco-IOS-XR-clns-isis-cfg',
            'micro-loop-avoidance',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-clns-isis-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg',
        ),
    },
    'Isis.Instances.Instance.Afs.Af.AfData.Ucmp.Enable' : {
        'meta_info' : _MetaInfoClass('Isis.Instances.Instance.Afs.Af.AfData.Ucmp.Enable', REFERENCE_CLASS,
            '''UCMP feature enable configuration''',
            False, 
            [
            _MetaInfoClassMember('variance', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('101', '10000')], [],
                '''                Value of variance
                ''',
                'variance',
                'Cisco-IOS-XR-clns-isis-cfg', False, default_value="200"),
            _MetaInfoClassMember('prefix-list-name', ATTRIBUTE, 'str', 'xr:Cisco-ios-xr-string',
                None, None,
                [(1, 32)], [],
                '''                Name of the Prefix List
                ''',
                'prefix_list_name',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            ],
            'Cisco-IOS-XR-clns-isis-cfg',
            'enable',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-clns-isis-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg',
        ),
    },
    'Isis.Instances.Instance.Afs.Af.AfData.Ucmp.ExcludeInterfaces.ExcludeInterface' : {
        'meta_info' : _MetaInfoClass('Isis.Instances.Instance.Afs.Af.AfData.Ucmp.ExcludeInterfaces.ExcludeInterface', REFERENCE_LIST,
            '''Exclude this interface from UCMP path
computation''',
            False, 
            [
            _MetaInfoClassMember('interface-name', ATTRIBUTE, 'str', 'xr:Interface-name',
                None, None,
                [], [b'[a-zA-Z0-9._/-]+'],
                '''                Name of the interface to be excluded
                ''',
                'interface_name',
                'Cisco-IOS-XR-clns-isis-cfg', True),
            ],
            'Cisco-IOS-XR-clns-isis-cfg',
            'exclude-interface',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-clns-isis-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg',
        ),
    },
    'Isis.Instances.Instance.Afs.Af.AfData.Ucmp.ExcludeInterfaces' : {
        'meta_info' : _MetaInfoClass('Isis.Instances.Instance.Afs.Af.AfData.Ucmp.ExcludeInterfaces', REFERENCE_CLASS,
            '''Interfaces excluded from UCMP path
computation''',
            False, 
            [
            _MetaInfoClassMember('exclude-interface', REFERENCE_LIST, 'ExcludeInterface', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'Isis.Instances.Instance.Afs.Af.AfData.Ucmp.ExcludeInterfaces.ExcludeInterface',
                [], [],
                '''                Exclude this interface from UCMP path
                computation
                ''',
                'exclude_interface',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            ],
            'Cisco-IOS-XR-clns-isis-cfg',
            'exclude-interfaces',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-clns-isis-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg',
        ),
    },
    'Isis.Instances.Instance.Afs.Af.AfData.Ucmp' : {
        'meta_info' : _MetaInfoClass('Isis.Instances.Instance.Afs.Af.AfData.Ucmp', REFERENCE_CLASS,
            '''UCMP (UnEqual Cost MultiPath) configuration''',
            False, 
            [
            _MetaInfoClassMember('enable', REFERENCE_CLASS, 'Enable', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'Isis.Instances.Instance.Afs.Af.AfData.Ucmp.Enable',
                [], [],
                '''                UCMP feature enable configuration
                ''',
                'enable',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            _MetaInfoClassMember('exclude-interfaces', REFERENCE_CLASS, 'ExcludeInterfaces', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'Isis.Instances.Instance.Afs.Af.AfData.Ucmp.ExcludeInterfaces',
                [], [],
                '''                Interfaces excluded from UCMP path
                computation
                ''',
                'exclude_interfaces',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            _MetaInfoClassMember('delay-interval', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('100', '65535')], [],
                '''                Delay in msecs between primary SPF and
                UCMP computation
                ''',
                'delay_interval',
                'Cisco-IOS-XR-clns-isis-cfg', False, default_value="100"),
            ],
            'Cisco-IOS-XR-clns-isis-cfg',
            'ucmp',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-clns-isis-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg',
        ),
    },
    'Isis.Instances.Instance.Afs.Af.AfData.MaxRedistPrefixes.MaxRedistPrefix' : {
        'meta_info' : _MetaInfoClass('Isis.Instances.Instance.Afs.Af.AfData.MaxRedistPrefixes.MaxRedistPrefix', REFERENCE_LIST,
            '''An upper limit on the number of
redistributed prefixes which may be
included in the local system's LSP''',
            False, 
            [
            _MetaInfoClassMember('level', REFERENCE_ENUM_CLASS, 'IsisInternalLevel', 'dt1:Isis-internal-level',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_datatypes', 'IsisInternalLevel',
                [], [],
                '''                Level to which configuration applies
                ''',
                'level',
                'Cisco-IOS-XR-clns-isis-cfg', True),
            _MetaInfoClassMember('prefix-limit', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('1', '28000')], [],
                '''                Max number of prefixes
                ''',
                'prefix_limit',
                'Cisco-IOS-XR-clns-isis-cfg', False, is_mandatory=True),
            ],
            'Cisco-IOS-XR-clns-isis-cfg',
            'max-redist-prefix',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-clns-isis-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg',
        ),
    },
    'Isis.Instances.Instance.Afs.Af.AfData.MaxRedistPrefixes' : {
        'meta_info' : _MetaInfoClass('Isis.Instances.Instance.Afs.Af.AfData.MaxRedistPrefixes', REFERENCE_CLASS,
            '''Maximum number of redistributed
prefixesconfiguration''',
            False, 
            [
            _MetaInfoClassMember('max-redist-prefix', REFERENCE_LIST, 'MaxRedistPrefix', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'Isis.Instances.Instance.Afs.Af.AfData.MaxRedistPrefixes.MaxRedistPrefix',
                [], [],
                '''                An upper limit on the number of
                redistributed prefixes which may be
                included in the local system's LSP
                ''',
                'max_redist_prefix',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            ],
            'Cisco-IOS-XR-clns-isis-cfg',
            'max-redist-prefixes',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-clns-isis-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg',
        ),
    },
    'Isis.Instances.Instance.Afs.Af.AfData.Propagations.Propagation' : {
        'meta_info' : _MetaInfoClass('Isis.Instances.Instance.Afs.Af.AfData.Propagations.Propagation', REFERENCE_LIST,
            '''Propagate routes between IS-IS levels''',
            False, 
            [
            _MetaInfoClassMember('source-level', REFERENCE_ENUM_CLASS, 'IsisInternalLevel', 'dt1:Isis-internal-level',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_datatypes', 'IsisInternalLevel',
                [], [],
                '''                Source level for routes
                ''',
                'source_level',
                'Cisco-IOS-XR-clns-isis-cfg', True),
            _MetaInfoClassMember('destination-level', REFERENCE_ENUM_CLASS, 'IsisInternalLevel', 'dt1:Isis-internal-level',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_datatypes', 'IsisInternalLevel',
                [], [],
                '''                Destination level for routes.  Must
                differ from SourceLevel
                ''',
                'destination_level',
                'Cisco-IOS-XR-clns-isis-cfg', True),
            _MetaInfoClassMember('route-policy-name', ATTRIBUTE, 'str', 'xr:Cisco-ios-xr-string',
                None, None,
                [(1, 64)], [],
                '''                Route policy limiting routes to be
                propagated
                ''',
                'route_policy_name',
                'Cisco-IOS-XR-clns-isis-cfg', False, is_mandatory=True),
            ],
            'Cisco-IOS-XR-clns-isis-cfg',
            'propagation',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-clns-isis-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg',
        ),
    },
    'Isis.Instances.Instance.Afs.Af.AfData.Propagations' : {
        'meta_info' : _MetaInfoClass('Isis.Instances.Instance.Afs.Af.AfData.Propagations', REFERENCE_CLASS,
            '''Route propagation configuration''',
            False, 
            [
            _MetaInfoClassMember('propagation', REFERENCE_LIST, 'Propagation', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'Isis.Instances.Instance.Afs.Af.AfData.Propagations.Propagation',
                [], [],
                '''                Propagate routes between IS-IS levels
                ''',
                'propagation',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            ],
            'Cisco-IOS-XR-clns-isis-cfg',
            'propagations',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-clns-isis-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg',
        ),
    },
    'Isis.Instances.Instance.Afs.Af.AfData.Redistributions.Redistribution.ConnectedOrStaticOrRipOrSubscriberOrMobile' : {
        'meta_info' : _MetaInfoClass('Isis.Instances.Instance.Afs.Af.AfData.Redistributions.Redistribution.ConnectedOrStaticOrRipOrSubscriberOrMobile', REFERENCE_CLASS,
            '''connected or static or rip or subscriber
or mobile''',
            False, 
            [
            _MetaInfoClassMember('metric', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('0', '16777215')], [],
                '''                Metric for redistributed routes: <0-63>
                for narrow, <0-16777215> for wide
                ''',
                'metric',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            _MetaInfoClassMember('levels', REFERENCE_ENUM_CLASS, 'IsisConfigurableLevels', 'Isis-configurable-levels',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'IsisConfigurableLevels',
                [], [],
                '''                Levels to redistribute routes into
                ''',
                'levels',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            _MetaInfoClassMember('route-policy-name', ATTRIBUTE, 'str', 'xr:Cisco-ios-xr-string',
                None, None,
                [(1, 64)], [],
                '''                Route policy to control redistribution.
                ''',
                'route_policy_name',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            _MetaInfoClassMember('metric-type', REFERENCE_ENUM_CLASS, 'IsisMetric', 'Isis-metric',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'IsisMetric',
                [], [],
                '''                IS-IS metric type
                ''',
                'metric_type',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            _MetaInfoClassMember('ospf-route-type', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('0', '4294967295')], [],
                '''                OSPF route types to redistribute.  May
                only be specified if Protocol is OSPF.
                ''',
                'ospf_route_type',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            ],
            'Cisco-IOS-XR-clns-isis-cfg',
            'connected-or-static-or-rip-or-subscriber-or-mobile',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-clns-isis-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg',
            is_presence=True,
            has_when=True,
        ),
    },
    'Isis.Instances.Instance.Afs.Af.AfData.Redistributions.Redistribution.OspfOrOspfv3OrIsisOrApplication' : {
        'meta_info' : _MetaInfoClass('Isis.Instances.Instance.Afs.Af.AfData.Redistributions.Redistribution.OspfOrOspfv3OrIsisOrApplication', REFERENCE_LIST,
            '''ospf or ospfv3 or isis or application''',
            False, 
            [
            _MetaInfoClassMember('instance-name', ATTRIBUTE, 'str', 'xr:Cisco-ios-xr-string',
                None, None,
                [(1, 64)], [],
                '''                Protocol Instance Identifier.  Mandatory
                for ISIS, OSPF and application, must not
                be specified otherwise.
                ''',
                'instance_name',
                'Cisco-IOS-XR-clns-isis-cfg', True),
            _MetaInfoClassMember('metric', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('0', '16777215')], [],
                '''                Metric for redistributed routes: <0-63>
                for narrow, <0-16777215> for wide
                ''',
                'metric',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            _MetaInfoClassMember('levels', REFERENCE_ENUM_CLASS, 'IsisConfigurableLevels', 'Isis-configurable-levels',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'IsisConfigurableLevels',
                [], [],
                '''                Levels to redistribute routes into
                ''',
                'levels',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            _MetaInfoClassMember('route-policy-name', ATTRIBUTE, 'str', 'xr:Cisco-ios-xr-string',
                None, None,
                [(1, 64)], [],
                '''                Route policy to control redistribution.
                ''',
                'route_policy_name',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            _MetaInfoClassMember('metric-type', REFERENCE_ENUM_CLASS, 'IsisMetric', 'Isis-metric',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'IsisMetric',
                [], [],
                '''                IS-IS metric type
                ''',
                'metric_type',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            _MetaInfoClassMember('ospf-route-type', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('0', '4294967295')], [],
                '''                OSPF route types to redistribute.  May
                only be specified if Protocol is OSPF.
                ''',
                'ospf_route_type',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            ],
            'Cisco-IOS-XR-clns-isis-cfg',
            'ospf-or-ospfv3-or-isis-or-application',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-clns-isis-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg',
            has_when=True,
        ),
    },
    'Isis.Instances.Instance.Afs.Af.AfData.Redistributions.Redistribution.Bgp' : {
        'meta_info' : _MetaInfoClass('Isis.Instances.Instance.Afs.Af.AfData.Redistributions.Redistribution.Bgp', REFERENCE_LIST,
            '''bgp''',
            False, 
            [
            _MetaInfoClassMember('as-xx', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('0', '65535')], [],
                '''                First half of BGP AS number in XX.YY
                format.  Mandatory if Protocol is BGP
                and must not be specified otherwise.
                Must be a non-zero value if second half
                is zero.
                ''',
                'as_xx',
                'Cisco-IOS-XR-clns-isis-cfg', True),
            _MetaInfoClassMember('as-yy', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('0', '4294967295')], [],
                '''                Second half of BGP AS number in XX.YY
                format. Mandatory if Protocol is BGP and
                must not be specified otherwise. Must be
                a non-zero value if first half is zero.
                ''',
                'as_yy',
                'Cisco-IOS-XR-clns-isis-cfg', True),
            _MetaInfoClassMember('metric', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('0', '16777215')], [],
                '''                Metric for redistributed routes: <0-63>
                for narrow, <0-16777215> for wide
                ''',
                'metric',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            _MetaInfoClassMember('levels', REFERENCE_ENUM_CLASS, 'IsisConfigurableLevels', 'Isis-configurable-levels',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'IsisConfigurableLevels',
                [], [],
                '''                Levels to redistribute routes into
                ''',
                'levels',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            _MetaInfoClassMember('route-policy-name', ATTRIBUTE, 'str', 'xr:Cisco-ios-xr-string',
                None, None,
                [(1, 64)], [],
                '''                Route policy to control redistribution.
                ''',
                'route_policy_name',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            _MetaInfoClassMember('metric-type', REFERENCE_ENUM_CLASS, 'IsisMetric', 'Isis-metric',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'IsisMetric',
                [], [],
                '''                IS-IS metric type
                ''',
                'metric_type',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            _MetaInfoClassMember('ospf-route-type', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('0', '4294967295')], [],
                '''                OSPF route types to redistribute.  May
                only be specified if Protocol is OSPF.
                ''',
                'ospf_route_type',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            ],
            'Cisco-IOS-XR-clns-isis-cfg',
            'bgp',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-clns-isis-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg',
            has_when=True,
        ),
    },
    'Isis.Instances.Instance.Afs.Af.AfData.Redistributions.Redistribution.Eigrp' : {
        'meta_info' : _MetaInfoClass('Isis.Instances.Instance.Afs.Af.AfData.Redistributions.Redistribution.Eigrp', REFERENCE_LIST,
            '''eigrp''',
            False, 
            [
            _MetaInfoClassMember('as-zz', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('1', '65535')], [],
                '''                Eigrp as number.
                ''',
                'as_zz',
                'Cisco-IOS-XR-clns-isis-cfg', True),
            _MetaInfoClassMember('metric', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('0', '16777215')], [],
                '''                Metric for redistributed routes: <0-63>
                for narrow, <0-16777215> for wide
                ''',
                'metric',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            _MetaInfoClassMember('levels', REFERENCE_ENUM_CLASS, 'IsisConfigurableLevels', 'Isis-configurable-levels',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'IsisConfigurableLevels',
                [], [],
                '''                Levels to redistribute routes into
                ''',
                'levels',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            _MetaInfoClassMember('route-policy-name', ATTRIBUTE, 'str', 'xr:Cisco-ios-xr-string',
                None, None,
                [(1, 64)], [],
                '''                Route policy to control redistribution.
                ''',
                'route_policy_name',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            _MetaInfoClassMember('metric-type', REFERENCE_ENUM_CLASS, 'IsisMetric', 'Isis-metric',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'IsisMetric',
                [], [],
                '''                IS-IS metric type
                ''',
                'metric_type',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            _MetaInfoClassMember('ospf-route-type', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('0', '4294967295')], [],
                '''                OSPF route types to redistribute.  May
                only be specified if Protocol is OSPF.
                ''',
                'ospf_route_type',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            ],
            'Cisco-IOS-XR-clns-isis-cfg',
            'eigrp',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-clns-isis-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg',
            has_when=True,
        ),
    },
    'Isis.Instances.Instance.Afs.Af.AfData.Redistributions.Redistribution' : {
        'meta_info' : _MetaInfoClass('Isis.Instances.Instance.Afs.Af.AfData.Redistributions.Redistribution', REFERENCE_LIST,
            '''Redistribution of other protocols into
this IS-IS instance''',
            False, 
            [
            _MetaInfoClassMember('protocol-name', REFERENCE_ENUM_CLASS, 'IsisRedistProto', 'Isis-redist-proto',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'IsisRedistProto',
                [], [],
                '''                The protocol to be redistributed.  OSPFv3
                may not be specified for an IPv4 topology
                and OSPF may not be specified for an IPv6
                topology.
                ''',
                'protocol_name',
                'Cisco-IOS-XR-clns-isis-cfg', True),
            _MetaInfoClassMember('connected-or-static-or-rip-or-subscriber-or-mobile', REFERENCE_CLASS, 'ConnectedOrStaticOrRipOrSubscriberOrMobile', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'Isis.Instances.Instance.Afs.Af.AfData.Redistributions.Redistribution.ConnectedOrStaticOrRipOrSubscriberOrMobile',
                [], [],
                '''                connected or static or rip or subscriber
                or mobile
                ''',
                'connected_or_static_or_rip_or_subscriber_or_mobile',
                'Cisco-IOS-XR-clns-isis-cfg', False, is_presence=True, has_when=True),
            _MetaInfoClassMember('ospf-or-ospfv3-or-isis-or-application', REFERENCE_LIST, 'OspfOrOspfv3OrIsisOrApplication', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'Isis.Instances.Instance.Afs.Af.AfData.Redistributions.Redistribution.OspfOrOspfv3OrIsisOrApplication',
                [], [],
                '''                ospf or ospfv3 or isis or application
                ''',
                'ospf_or_ospfv3_or_isis_or_application',
                'Cisco-IOS-XR-clns-isis-cfg', False, has_when=True),
            _MetaInfoClassMember('bgp', REFERENCE_LIST, 'Bgp', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'Isis.Instances.Instance.Afs.Af.AfData.Redistributions.Redistribution.Bgp',
                [], [],
                '''                bgp
                ''',
                'bgp',
                'Cisco-IOS-XR-clns-isis-cfg', False, has_when=True),
            _MetaInfoClassMember('eigrp', REFERENCE_LIST, 'Eigrp', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'Isis.Instances.Instance.Afs.Af.AfData.Redistributions.Redistribution.Eigrp',
                [], [],
                '''                eigrp
                ''',
                'eigrp',
                'Cisco-IOS-XR-clns-isis-cfg', False, has_when=True),
            ],
            'Cisco-IOS-XR-clns-isis-cfg',
            'redistribution',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-clns-isis-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg',
            has_must=True,
        ),
    },
    'Isis.Instances.Instance.Afs.Af.AfData.Redistributions' : {
        'meta_info' : _MetaInfoClass('Isis.Instances.Instance.Afs.Af.AfData.Redistributions', REFERENCE_CLASS,
            '''Protocol redistribution configuration''',
            False, 
            [
            _MetaInfoClassMember('redistribution', REFERENCE_LIST, 'Redistribution', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'Isis.Instances.Instance.Afs.Af.AfData.Redistributions.Redistribution',
                [], [],
                '''                Redistribution of other protocols into
                this IS-IS instance
                ''',
                'redistribution',
                'Cisco-IOS-XR-clns-isis-cfg', False, has_must=True),
            ],
            'Cisco-IOS-XR-clns-isis-cfg',
            'redistributions',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-clns-isis-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg',
        ),
    },
    'Isis.Instances.Instance.Afs.Af.AfData.ApplicationTables.ApplicationTable.AttributeTable' : {
        'meta_info' : _MetaInfoClass('Isis.Instances.Instance.Afs.Af.AfData.ApplicationTables.ApplicationTable.AttributeTable', REFERENCE_LIST,
            '''Attribute Name''',
            False, 
            [
            _MetaInfoClassMember('app-type', REFERENCE_ENUM_CLASS, 'IsisApplicationAttribute', 'Isis-application-attribute',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'IsisApplicationAttribute',
                [], [],
                '''                Application Type
                ''',
                'app_type',
                'Cisco-IOS-XR-clns-isis-cfg', True),
            _MetaInfoClassMember('enable', ATTRIBUTE, 'bool', 'boolean',
                None, None,
                [], [],
                '''                If TRUE, advertise application link
                attribute in our LSP
                ''',
                'enable',
                'Cisco-IOS-XR-clns-isis-cfg', False, is_mandatory=True),
            ],
            'Cisco-IOS-XR-clns-isis-cfg',
            'attribute-table',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-clns-isis-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg',
        ),
    },
    'Isis.Instances.Instance.Afs.Af.AfData.ApplicationTables.ApplicationTable' : {
        'meta_info' : _MetaInfoClass('Isis.Instances.Instance.Afs.Af.AfData.ApplicationTables.ApplicationTable', REFERENCE_LIST,
            '''Application Name''',
            False, 
            [
            _MetaInfoClassMember('app-type', REFERENCE_ENUM_CLASS, 'IsisApplication', 'Isis-application',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'IsisApplication',
                [], [],
                '''                Application Type
                ''',
                'app_type',
                'Cisco-IOS-XR-clns-isis-cfg', True),
            _MetaInfoClassMember('attribute-table', REFERENCE_LIST, 'AttributeTable', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'Isis.Instances.Instance.Afs.Af.AfData.ApplicationTables.ApplicationTable.AttributeTable',
                [], [],
                '''                Attribute Name
                ''',
                'attribute_table',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            ],
            'Cisco-IOS-XR-clns-isis-cfg',
            'application-table',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-clns-isis-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg',
        ),
    },
    'Isis.Instances.Instance.Afs.Af.AfData.ApplicationTables' : {
        'meta_info' : _MetaInfoClass('Isis.Instances.Instance.Afs.Af.AfData.ApplicationTables', REFERENCE_CLASS,
            '''Advertise application specific values''',
            False, 
            [
            _MetaInfoClassMember('application-table', REFERENCE_LIST, 'ApplicationTable', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'Isis.Instances.Instance.Afs.Af.AfData.ApplicationTables.ApplicationTable',
                [], [],
                '''                Application Name
                ''',
                'application_table',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            ],
            'Cisco-IOS-XR-clns-isis-cfg',
            'application-tables',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-clns-isis-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg',
        ),
    },
    'Isis.Instances.Instance.Afs.Af.AfData.SpfPeriodicIntervals.SpfPeriodicInterval' : {
        'meta_info' : _MetaInfoClass('Isis.Instances.Instance.Afs.Af.AfData.SpfPeriodicIntervals.SpfPeriodicInterval', REFERENCE_LIST,
            '''Maximum interval between spf runs''',
            False, 
            [
            _MetaInfoClassMember('level', REFERENCE_ENUM_CLASS, 'IsisInternalLevel', 'dt1:Isis-internal-level',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_datatypes', 'IsisInternalLevel',
                [], [],
                '''                Level to which configuration applies
                ''',
                'level',
                'Cisco-IOS-XR-clns-isis-cfg', True),
            _MetaInfoClassMember('periodic-interval', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('0', '3600')], [],
                '''                Maximum interval in between SPF runs in
                seconds
                ''',
                'periodic_interval',
                'Cisco-IOS-XR-clns-isis-cfg', False, is_mandatory=True),
            ],
            'Cisco-IOS-XR-clns-isis-cfg',
            'spf-periodic-interval',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-clns-isis-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg',
        ),
    },
    'Isis.Instances.Instance.Afs.Af.AfData.SpfPeriodicIntervals' : {
        'meta_info' : _MetaInfoClass('Isis.Instances.Instance.Afs.Af.AfData.SpfPeriodicIntervals', REFERENCE_CLASS,
            '''Peoridic SPF configuration''',
            False, 
            [
            _MetaInfoClassMember('spf-periodic-interval', REFERENCE_LIST, 'SpfPeriodicInterval', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'Isis.Instances.Instance.Afs.Af.AfData.SpfPeriodicIntervals.SpfPeriodicInterval',
                [], [],
                '''                Maximum interval between spf runs
                ''',
                'spf_periodic_interval',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            ],
            'Cisco-IOS-XR-clns-isis-cfg',
            'spf-periodic-intervals',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-clns-isis-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg',
        ),
    },
    'Isis.Instances.Instance.Afs.Af.AfData.DistributeListIn' : {
        'meta_info' : _MetaInfoClass('Isis.Instances.Instance.Afs.Af.AfData.DistributeListIn', REFERENCE_CLASS,
            '''Filter routes sent to the RIB''',
            False, 
            [
            _MetaInfoClassMember('prefix-list-name', ATTRIBUTE, 'str', 'xr:Cisco-ios-xr-string',
                None, None,
                [(1, 64)], [],
                '''                Prefix list to control routes installed in
                RIB.
                ''',
                'prefix_list_name',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            _MetaInfoClassMember('route-policy-name', ATTRIBUTE, 'str', 'xr:Cisco-ios-xr-string',
                None, None,
                [(1, 64)], [],
                '''                Route policy to control routes installed
                in RIB.
                ''',
                'route_policy_name',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            ],
            'Cisco-IOS-XR-clns-isis-cfg',
            'distribute-list-in',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-clns-isis-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg',
        ),
    },
    'Isis.Instances.Instance.Afs.Af.AfData.SpfIntervals.SpfInterval' : {
        'meta_info' : _MetaInfoClass('Isis.Instances.Instance.Afs.Af.AfData.SpfIntervals.SpfInterval', REFERENCE_LIST,
            '''Route calculation scheduling parameters''',
            False, 
            [
            _MetaInfoClassMember('level', REFERENCE_ENUM_CLASS, 'IsisInternalLevel', 'dt1:Isis-internal-level',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_datatypes', 'IsisInternalLevel',
                [], [],
                '''                Level to which configuration applies
                ''',
                'level',
                'Cisco-IOS-XR-clns-isis-cfg', True),
            _MetaInfoClassMember('maximum-wait', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('0', '120000')], [],
                '''                Maximum wait before running a route
                calculation in milliseconds
                ''',
                'maximum_wait',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            _MetaInfoClassMember('initial-wait', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('0', '120000')], [],
                '''                Initial wait before running a route
                calculation in milliseconds
                ''',
                'initial_wait',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            _MetaInfoClassMember('secondary-wait', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('0', '120000')], [],
                '''                Secondary wait before running a route
                calculation in milliseconds
                ''',
                'secondary_wait',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            ],
            'Cisco-IOS-XR-clns-isis-cfg',
            'spf-interval',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-clns-isis-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg',
        ),
    },
    'Isis.Instances.Instance.Afs.Af.AfData.SpfIntervals' : {
        'meta_info' : _MetaInfoClass('Isis.Instances.Instance.Afs.Af.AfData.SpfIntervals', REFERENCE_CLASS,
            '''SPF-interval configuration''',
            False, 
            [
            _MetaInfoClassMember('spf-interval', REFERENCE_LIST, 'SpfInterval', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'Isis.Instances.Instance.Afs.Af.AfData.SpfIntervals.SpfInterval',
                [], [],
                '''                Route calculation scheduling parameters
                ''',
                'spf_interval',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            ],
            'Cisco-IOS-XR-clns-isis-cfg',
            'spf-intervals',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-clns-isis-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg',
        ),
    },
    'Isis.Instances.Instance.Afs.Af.AfData.MonitorConvergence' : {
        'meta_info' : _MetaInfoClass('Isis.Instances.Instance.Afs.Af.AfData.MonitorConvergence', REFERENCE_CLASS,
            '''Enable convergence monitoring''',
            False, 
            [
            _MetaInfoClassMember('enable', ATTRIBUTE, 'Empty', 'empty',
                None, None,
                [], [],
                '''                Enable convergence monitoring
                ''',
                'enable',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            _MetaInfoClassMember('track-ip-frr', ATTRIBUTE, 'Empty', 'empty',
                None, None,
                [], [],
                '''                Enable the Tracking of IP-Frr Convergence
                ''',
                'track_ip_frr',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            _MetaInfoClassMember('prefix-list', ATTRIBUTE, 'str', 'xr:Cisco-ios-xr-string',
                None, None,
                [(1, 32)], [],
                '''                Enable the monitoring of individual
                prefixes (prefix list name)
                ''',
                'prefix_list',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            ],
            'Cisco-IOS-XR-clns-isis-cfg',
            'monitor-convergence',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-clns-isis-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg',
        ),
    },
    'Isis.Instances.Instance.Afs.Af.AfData.DefaultInformation' : {
        'meta_info' : _MetaInfoClass('Isis.Instances.Instance.Afs.Af.AfData.DefaultInformation', REFERENCE_CLASS,
            '''Control origination of a default route with
the option of using a policy.  If no policy
is specified the default route is
advertised with zero cost in level 2 only.''',
            False, 
            [
            _MetaInfoClassMember('use-policy', ATTRIBUTE, 'bool', 'boolean',
                None, None,
                [], [],
                '''                Flag to indicate whether default
                origination is controlled using a policy
                ''',
                'use_policy',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            _MetaInfoClassMember('policy-name', ATTRIBUTE, 'str', 'xr:Cisco-ios-xr-string',
                None, None,
                [(1, 64)], [],
                '''                Policy name
                ''',
                'policy_name',
                'Cisco-IOS-XR-clns-isis-cfg', False, has_when=True),
            _MetaInfoClassMember('external', ATTRIBUTE, 'Empty', 'empty',
                None, None,
                [], [],
                '''                Flag to indicate that the default prefix
                should be originated as an external route
                ''',
                'external',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            ],
            'Cisco-IOS-XR-clns-isis-cfg',
            'default-information',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-clns-isis-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg',
        ),
    },
    'Isis.Instances.Instance.Afs.Af.AfData.AdminDistances.AdminDistance' : {
        'meta_info' : _MetaInfoClass('Isis.Instances.Instance.Afs.Af.AfData.AdminDistances.AdminDistance', REFERENCE_LIST,
            '''Administrative distance configuration. The
supplied distance is applied to all routes
discovered from the specified source, or
only those that match the supplied prefix
list if this is specified''',
            False, 
            [
            _MetaInfoClassMember('address-prefix', REFERENCE_UNION, 'str', 'inet:ip-prefix',
                None, None,
                [], [],
                '''                IP route source prefix
                ''',
                'address_prefix',
                'Cisco-IOS-XR-clns-isis-cfg', True, [
                    _MetaInfoClassMember('address-prefix', ATTRIBUTE, 'str', 'inet:ipv4-prefix',
                        None, None,
                        [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])/(([0-9])|([1-2][0-9])|(3[0-2]))'],
                        '''                        IP route source prefix
                        ''',
                        'address_prefix',
                        'Cisco-IOS-XR-clns-isis-cfg', True),
                    _MetaInfoClassMember('address-prefix', ATTRIBUTE, 'str', 'inet:ipv6-prefix',
                        None, None,
                        [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(/(([0-9])|([0-9]{2})|(1[0-1][0-9])|(12[0-8])))'],
                        '''                        IP route source prefix
                        ''',
                        'address_prefix',
                        'Cisco-IOS-XR-clns-isis-cfg', True),
                ]),
            _MetaInfoClassMember('distance', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('1', '255')], [],
                '''                Administrative distance
                ''',
                'distance',
                'Cisco-IOS-XR-clns-isis-cfg', False, is_mandatory=True),
            _MetaInfoClassMember('prefix-list', ATTRIBUTE, 'str', 'string',
                None, None,
                [(1, 32)], [],
                '''                List of prefixes to which this distance
                applies
                ''',
                'prefix_list',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            ],
            'Cisco-IOS-XR-clns-isis-cfg',
            'admin-distance',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-clns-isis-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg',
        ),
    },
    'Isis.Instances.Instance.Afs.Af.AfData.AdminDistances' : {
        'meta_info' : _MetaInfoClass('Isis.Instances.Instance.Afs.Af.AfData.AdminDistances', REFERENCE_CLASS,
            '''Per-route administrative
distanceconfiguration''',
            False, 
            [
            _MetaInfoClassMember('admin-distance', REFERENCE_LIST, 'AdminDistance', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'Isis.Instances.Instance.Afs.Af.AfData.AdminDistances.AdminDistance',
                [], [],
                '''                Administrative distance configuration. The
                supplied distance is applied to all routes
                discovered from the specified source, or
                only those that match the supplied prefix
                list if this is specified
                ''',
                'admin_distance',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            ],
            'Cisco-IOS-XR-clns-isis-cfg',
            'admin-distances',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-clns-isis-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg',
        ),
    },
    'Isis.Instances.Instance.Afs.Af.AfData.Ispf.States.State' : {
        'meta_info' : _MetaInfoClass('Isis.Instances.Instance.Afs.Af.AfData.Ispf.States.State', REFERENCE_LIST,
            '''Enable/disable ISPF''',
            False, 
            [
            _MetaInfoClassMember('level', REFERENCE_ENUM_CLASS, 'IsisInternalLevel', 'dt1:Isis-internal-level',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_datatypes', 'IsisInternalLevel',
                [], [],
                '''                Level to which configuration applies
                ''',
                'level',
                'Cisco-IOS-XR-clns-isis-cfg', True),
            _MetaInfoClassMember('state', REFERENCE_ENUM_CLASS, 'IsisispfState', 'Isisispf-state',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'IsisispfState',
                [], [],
                '''                State
                ''',
                'state',
                'Cisco-IOS-XR-clns-isis-cfg', False, is_mandatory=True),
            ],
            'Cisco-IOS-XR-clns-isis-cfg',
            'state',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-clns-isis-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg',
        ),
    },
    'Isis.Instances.Instance.Afs.Af.AfData.Ispf.States' : {
        'meta_info' : _MetaInfoClass('Isis.Instances.Instance.Afs.Af.AfData.Ispf.States', REFERENCE_CLASS,
            '''ISPF state (enable/disable)''',
            False, 
            [
            _MetaInfoClassMember('state', REFERENCE_LIST, 'State', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'Isis.Instances.Instance.Afs.Af.AfData.Ispf.States.State',
                [], [],
                '''                Enable/disable ISPF
                ''',
                'state',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            ],
            'Cisco-IOS-XR-clns-isis-cfg',
            'states',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-clns-isis-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg',
        ),
    },
    'Isis.Instances.Instance.Afs.Af.AfData.Ispf' : {
        'meta_info' : _MetaInfoClass('Isis.Instances.Instance.Afs.Af.AfData.Ispf', REFERENCE_CLASS,
            '''ISPF configuration''',
            False, 
            [
            _MetaInfoClassMember('states', REFERENCE_CLASS, 'States', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'Isis.Instances.Instance.Afs.Af.AfData.Ispf.States',
                [], [],
                '''                ISPF state (enable/disable)
                ''',
                'states',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            ],
            'Cisco-IOS-XR-clns-isis-cfg',
            'ispf',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-clns-isis-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg',
        ),
    },
    'Isis.Instances.Instance.Afs.Af.AfData.MplsLdpGlobal' : {
        'meta_info' : _MetaInfoClass('Isis.Instances.Instance.Afs.Af.AfData.MplsLdpGlobal', REFERENCE_CLASS,
            '''MPLS LDP configuration. MPLS LDP
configuration will only be applied for the
IPv4-unicast address-family.''',
            False, 
            [
            _MetaInfoClassMember('auto-config', ATTRIBUTE, 'bool', 'boolean',
                None, None,
                [], [],
                '''                If TRUE, LDP will be enabled onall IS-IS
                interfaces enabled for this address-family
                ''',
                'auto_config',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            ],
            'Cisco-IOS-XR-clns-isis-cfg',
            'mpls-ldp-global',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-clns-isis-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg',
        ),
    },
    'Isis.Instances.Instance.Afs.Af.AfData.Mpls.RouterId' : {
        'meta_info' : _MetaInfoClass('Isis.Instances.Instance.Afs.Af.AfData.Mpls.RouterId', REFERENCE_CLASS,
            '''Traffic Engineering stable IP address for
system''',
            False, 
            [
            _MetaInfoClassMember('address', ATTRIBUTE, 'str', 'inet:ipv4-address-no-zone',
                None, None,
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'],
                '''                IPv4 address to be used as a router ID.
                Precisely one of Address and Interface
                must be specified.
                ''',
                'address',
                'Cisco-IOS-XR-clns-isis-cfg', False, has_must=True),
            _MetaInfoClassMember('interface-name', ATTRIBUTE, 'str', 'xr:Interface-name',
                None, None,
                [], [b'[a-zA-Z0-9._/-]+'],
                '''                Interface with designated stable IP
                address to be used as a router ID. This
                must be a Loopback interface. Precisely
                one of Address and Interface must be
                specified.
                ''',
                'interface_name',
                'Cisco-IOS-XR-clns-isis-cfg', False, has_must=True),
            ],
            'Cisco-IOS-XR-clns-isis-cfg',
            'router-id',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-clns-isis-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg',
        ),
    },
    'Isis.Instances.Instance.Afs.Af.AfData.Mpls.Level' : {
        'meta_info' : _MetaInfoClass('Isis.Instances.Instance.Afs.Af.AfData.Mpls.Level', REFERENCE_CLASS,
            '''Enable MPLS for an IS-IS at the given
levels''',
            False, 
            [
            _MetaInfoClassMember('level1', ATTRIBUTE, 'bool', 'boolean',
                None, None,
                [], [],
                '''                Level 1 enabled
                ''',
                'level1',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            _MetaInfoClassMember('level2', ATTRIBUTE, 'bool', 'boolean',
                None, None,
                [], [],
                '''                Level 2 enabled
                ''',
                'level2',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            ],
            'Cisco-IOS-XR-clns-isis-cfg',
            'level',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-clns-isis-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg',
        ),
    },
    'Isis.Instances.Instance.Afs.Af.AfData.Mpls' : {
        'meta_info' : _MetaInfoClass('Isis.Instances.Instance.Afs.Af.AfData.Mpls', REFERENCE_CLASS,
            '''MPLS configuration. MPLS configuration will
only be applied for the IPv4-unicast
address-family.''',
            False, 
            [
            _MetaInfoClassMember('router-id', REFERENCE_CLASS, 'RouterId', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'Isis.Instances.Instance.Afs.Af.AfData.Mpls.RouterId',
                [], [],
                '''                Traffic Engineering stable IP address for
                system
                ''',
                'router_id',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            _MetaInfoClassMember('level', REFERENCE_CLASS, 'Level', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'Isis.Instances.Instance.Afs.Af.AfData.Mpls.Level',
                [], [],
                '''                Enable MPLS for an IS-IS at the given
                levels
                ''',
                'level',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            _MetaInfoClassMember('igp-intact', ATTRIBUTE, 'Empty', 'empty',
                None, None,
                [], [],
                '''                Install TE and non-TE nexthops in the RIB
                ''',
                'igp_intact',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            _MetaInfoClassMember('multicast-intact', ATTRIBUTE, 'Empty', 'empty',
                None, None,
                [], [],
                '''                Install non-TE nexthops in the RIB for use
                by multicast
                ''',
                'multicast_intact',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            ],
            'Cisco-IOS-XR-clns-isis-cfg',
            'mpls',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-clns-isis-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg',
        ),
    },
    'Isis.Instances.Instance.Afs.Af.AfData.ManualAdjSids.ManualAdjSid' : {
        'meta_info' : _MetaInfoClass('Isis.Instances.Instance.Afs.Af.AfData.ManualAdjSids.ManualAdjSid', REFERENCE_LIST,
            '''Assign adjancency SID to an interface''',
            False, 
            [
            _MetaInfoClassMember('level', REFERENCE_ENUM_CLASS, 'IsisInternalLevel', 'dt1:Isis-internal-level',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_datatypes', 'IsisInternalLevel',
                [], [],
                '''                Level to which configuration applies
                ''',
                'level',
                'Cisco-IOS-XR-clns-isis-cfg', True),
            _MetaInfoClassMember('sid-type', REFERENCE_ENUM_CLASS, 'Isissid1', 'Isissid1',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'Isissid1',
                [], [],
                '''                Sid type aboslute or index
                ''',
                'sid_type',
                'Cisco-IOS-XR-clns-isis-cfg', True),
            _MetaInfoClassMember('sid', ATTRIBUTE, 'int', 'Isissid',
                None, None,
                [('0', '1048575')], [],
                '''                Sid value
                ''',
                'sid',
                'Cisco-IOS-XR-clns-isis-cfg', True),
            _MetaInfoClassMember('protected', REFERENCE_ENUM_CLASS, 'IsissidProtected', 'Isissid-protected',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'IsissidProtected',
                [], [],
                '''                Enable/Disable SID protection
                ''',
                'protected',
                'Cisco-IOS-XR-clns-isis-cfg', False, is_mandatory=True),
            ],
            'Cisco-IOS-XR-clns-isis-cfg',
            'manual-adj-sid',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-clns-isis-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg',
        ),
    },
    'Isis.Instances.Instance.Afs.Af.AfData.ManualAdjSids' : {
        'meta_info' : _MetaInfoClass('Isis.Instances.Instance.Afs.Af.AfData.ManualAdjSids', REFERENCE_CLASS,
            '''Manual Adjacecy SID configuration''',
            False, 
            [
            _MetaInfoClassMember('manual-adj-sid', REFERENCE_LIST, 'ManualAdjSid', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'Isis.Instances.Instance.Afs.Af.AfData.ManualAdjSids.ManualAdjSid',
                [], [],
                '''                Assign adjancency SID to an interface
                ''',
                'manual_adj_sid',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            ],
            'Cisco-IOS-XR-clns-isis-cfg',
            'manual-adj-sids',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-clns-isis-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg',
        ),
    },
    'Isis.Instances.Instance.Afs.Af.AfData.Metrics.Metric.Metric_' : _MetaInfoEnum('Metric_',
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'Isis.Instances.Instance.Afs.Af.AfData.Metrics.Metric.Metric_',
        ''' ''',
        {
            'maximum':'maximum',
        }, 'Cisco-IOS-XR-clns-isis-cfg', _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-clns-isis-cfg']),
    'Isis.Instances.Instance.Afs.Af.AfData.Metrics.Metric' : {
        'meta_info' : _MetaInfoClass('Isis.Instances.Instance.Afs.Af.AfData.Metrics.Metric', REFERENCE_LIST,
            '''Metric configuration. Legal value depends on
the metric-style specified for the topology. If
the metric-style defined is narrow, then only a
value between <1-63> is allowed and if the
metric-style is defined as wide, then a value
between <1-16777215> is allowed as the metric
value.  All routers exclude links with the
maximum wide metric (16777215) from their SPF''',
            False, 
            [
            _MetaInfoClassMember('level', REFERENCE_ENUM_CLASS, 'IsisInternalLevel', 'dt1:Isis-internal-level',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_datatypes', 'IsisInternalLevel',
                [], [],
                '''                Level to which configuration applies
                ''',
                'level',
                'Cisco-IOS-XR-clns-isis-cfg', True),
            _MetaInfoClassMember('metric', REFERENCE_UNION, 'str', 'union',
                None, None,
                [], [],
                '''                Allowed metric: <1-63> for narrow,
                <1-16777215> for wide
                ''',
                'metric',
                'Cisco-IOS-XR-clns-isis-cfg', False, [
                    _MetaInfoClassMember('metric', REFERENCE_ENUM_CLASS, 'Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.TopologyName.Metrics.Metric.Metric_', 'enumeration',
                        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.TopologyName.Metrics.Metric.Metric_',
                        [], [],
                        '''                        Allowed metric: <1-63> for narrow,
                        <1-16777215> for wide
                        ''',
                        'metric',
                        'Cisco-IOS-XR-clns-isis-cfg', False, is_mandatory=True),
                    _MetaInfoClassMember('metric', ATTRIBUTE, 'int', 'uint32',
                        None, None,
                        [('1', '16777215')], [],
                        '''                        Allowed metric: <1-63> for narrow,
                        <1-16777215> for wide
                        ''',
                        'metric',
                        'Cisco-IOS-XR-clns-isis-cfg', False, is_mandatory=True),
                ], is_mandatory=True),
            ],
            'Cisco-IOS-XR-clns-isis-cfg',
            'metric',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-clns-isis-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg',
        ),
    },
    'Isis.Instances.Instance.Afs.Af.AfData.Metrics' : {
        'meta_info' : _MetaInfoClass('Isis.Instances.Instance.Afs.Af.AfData.Metrics', REFERENCE_CLASS,
            '''Metric configuration''',
            False, 
            [
            _MetaInfoClassMember('metric', REFERENCE_LIST, 'Metric', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'Isis.Instances.Instance.Afs.Af.AfData.Metrics.Metric',
                [], [],
                '''                Metric configuration. Legal value depends on
                the metric-style specified for the topology. If
                the metric-style defined is narrow, then only a
                value between <1-63> is allowed and if the
                metric-style is defined as wide, then a value
                between <1-16777215> is allowed as the metric
                value.  All routers exclude links with the
                maximum wide metric (16777215) from their SPF
                ''',
                'metric',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            ],
            'Cisco-IOS-XR-clns-isis-cfg',
            'metrics',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-clns-isis-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg',
        ),
    },
    'Isis.Instances.Instance.Afs.Af.AfData.Weights.Weight' : {
        'meta_info' : _MetaInfoClass('Isis.Instances.Instance.Afs.Af.AfData.Weights.Weight', REFERENCE_LIST,
            '''Weight configuration under interface for load
balancing''',
            False, 
            [
            _MetaInfoClassMember('level', REFERENCE_ENUM_CLASS, 'IsisInternalLevel', 'dt1:Isis-internal-level',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_datatypes', 'IsisInternalLevel',
                [], [],
                '''                Level to which configuration applies
                ''',
                'level',
                'Cisco-IOS-XR-clns-isis-cfg', True),
            _MetaInfoClassMember('weight', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('1', '16777214')], [],
                '''                Weight to be configured under interface for
                Load Balancing. Allowed weight: <1-16777215>
                ''',
                'weight',
                'Cisco-IOS-XR-clns-isis-cfg', False, is_mandatory=True),
            ],
            'Cisco-IOS-XR-clns-isis-cfg',
            'weight',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-clns-isis-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg',
        ),
    },
    'Isis.Instances.Instance.Afs.Af.AfData.Weights' : {
        'meta_info' : _MetaInfoClass('Isis.Instances.Instance.Afs.Af.AfData.Weights', REFERENCE_CLASS,
            '''Weight configuration''',
            False, 
            [
            _MetaInfoClassMember('weight', REFERENCE_LIST, 'Weight', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'Isis.Instances.Instance.Afs.Af.AfData.Weights.Weight',
                [], [],
                '''                Weight configuration under interface for load
                balancing
                ''',
                'weight',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            ],
            'Cisco-IOS-XR-clns-isis-cfg',
            'weights',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-clns-isis-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg',
        ),
    },
    'Isis.Instances.Instance.Afs.Af.AfData' : {
        'meta_info' : _MetaInfoClass('Isis.Instances.Instance.Afs.Af.AfData', REFERENCE_CLASS,
            '''Data container.''',
            False, 
            [
            _MetaInfoClassMember('segment-routing', REFERENCE_CLASS, 'SegmentRouting', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'Isis.Instances.Instance.Afs.Af.AfData.SegmentRouting',
                [], [],
                '''                Enable Segment Routing configuration
                ''',
                'segment_routing',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            _MetaInfoClassMember('metric-styles', REFERENCE_CLASS, 'MetricStyles', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'Isis.Instances.Instance.Afs.Af.AfData.MetricStyles',
                [], [],
                '''                Metric-style configuration
                ''',
                'metric_styles',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            _MetaInfoClassMember('frr-table', REFERENCE_CLASS, 'FrrTable', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'Isis.Instances.Instance.Afs.Af.AfData.FrrTable',
                [], [],
                '''                Fast-ReRoute configuration
                ''',
                'frr_table',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            _MetaInfoClassMember('router-id', REFERENCE_CLASS, 'RouterId', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'Isis.Instances.Instance.Afs.Af.AfData.RouterId',
                [], [],
                '''                Stable IP address for system. Will only be
                applied for the unicast sub-address-family.
                ''',
                'router_id',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            _MetaInfoClassMember('spf-prefix-priorities', REFERENCE_CLASS, 'SpfPrefixPriorities', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'Isis.Instances.Instance.Afs.Af.AfData.SpfPrefixPriorities',
                [], [],
                '''                SPF Prefix Priority configuration
                ''',
                'spf_prefix_priorities',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            _MetaInfoClassMember('summary-prefixes', REFERENCE_CLASS, 'SummaryPrefixes', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'Isis.Instances.Instance.Afs.Af.AfData.SummaryPrefixes',
                [], [],
                '''                Summary-prefix configuration
                ''',
                'summary_prefixes',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            _MetaInfoClassMember('micro-loop-avoidance', REFERENCE_CLASS, 'MicroLoopAvoidance', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'Isis.Instances.Instance.Afs.Af.AfData.MicroLoopAvoidance',
                [], [],
                '''                Micro Loop Avoidance configuration
                ''',
                'micro_loop_avoidance',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            _MetaInfoClassMember('ucmp', REFERENCE_CLASS, 'Ucmp', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'Isis.Instances.Instance.Afs.Af.AfData.Ucmp',
                [], [],
                '''                UCMP (UnEqual Cost MultiPath) configuration
                ''',
                'ucmp',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            _MetaInfoClassMember('max-redist-prefixes', REFERENCE_CLASS, 'MaxRedistPrefixes', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'Isis.Instances.Instance.Afs.Af.AfData.MaxRedistPrefixes',
                [], [],
                '''                Maximum number of redistributed
                prefixesconfiguration
                ''',
                'max_redist_prefixes',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            _MetaInfoClassMember('propagations', REFERENCE_CLASS, 'Propagations', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'Isis.Instances.Instance.Afs.Af.AfData.Propagations',
                [], [],
                '''                Route propagation configuration
                ''',
                'propagations',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            _MetaInfoClassMember('redistributions', REFERENCE_CLASS, 'Redistributions', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'Isis.Instances.Instance.Afs.Af.AfData.Redistributions',
                [], [],
                '''                Protocol redistribution configuration
                ''',
                'redistributions',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            _MetaInfoClassMember('application-tables', REFERENCE_CLASS, 'ApplicationTables', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'Isis.Instances.Instance.Afs.Af.AfData.ApplicationTables',
                [], [],
                '''                Advertise application specific values
                ''',
                'application_tables',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            _MetaInfoClassMember('spf-periodic-intervals', REFERENCE_CLASS, 'SpfPeriodicIntervals', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'Isis.Instances.Instance.Afs.Af.AfData.SpfPeriodicIntervals',
                [], [],
                '''                Peoridic SPF configuration
                ''',
                'spf_periodic_intervals',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            _MetaInfoClassMember('distribute-list-in', REFERENCE_CLASS, 'DistributeListIn', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'Isis.Instances.Instance.Afs.Af.AfData.DistributeListIn',
                [], [],
                '''                Filter routes sent to the RIB
                ''',
                'distribute_list_in',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            _MetaInfoClassMember('spf-intervals', REFERENCE_CLASS, 'SpfIntervals', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'Isis.Instances.Instance.Afs.Af.AfData.SpfIntervals',
                [], [],
                '''                SPF-interval configuration
                ''',
                'spf_intervals',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            _MetaInfoClassMember('monitor-convergence', REFERENCE_CLASS, 'MonitorConvergence', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'Isis.Instances.Instance.Afs.Af.AfData.MonitorConvergence',
                [], [],
                '''                Enable convergence monitoring
                ''',
                'monitor_convergence',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            _MetaInfoClassMember('default-information', REFERENCE_CLASS, 'DefaultInformation', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'Isis.Instances.Instance.Afs.Af.AfData.DefaultInformation',
                [], [],
                '''                Control origination of a default route with
                the option of using a policy.  If no policy
                is specified the default route is
                advertised with zero cost in level 2 only.
                ''',
                'default_information',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            _MetaInfoClassMember('admin-distances', REFERENCE_CLASS, 'AdminDistances', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'Isis.Instances.Instance.Afs.Af.AfData.AdminDistances',
                [], [],
                '''                Per-route administrative
                distanceconfiguration
                ''',
                'admin_distances',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            _MetaInfoClassMember('ispf', REFERENCE_CLASS, 'Ispf', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'Isis.Instances.Instance.Afs.Af.AfData.Ispf',
                [], [],
                '''                ISPF configuration
                ''',
                'ispf',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            _MetaInfoClassMember('mpls-ldp-global', REFERENCE_CLASS, 'MplsLdpGlobal', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'Isis.Instances.Instance.Afs.Af.AfData.MplsLdpGlobal',
                [], [],
                '''                MPLS LDP configuration. MPLS LDP
                configuration will only be applied for the
                IPv4-unicast address-family.
                ''',
                'mpls_ldp_global',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            _MetaInfoClassMember('mpls', REFERENCE_CLASS, 'Mpls', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'Isis.Instances.Instance.Afs.Af.AfData.Mpls',
                [], [],
                '''                MPLS configuration. MPLS configuration will
                only be applied for the IPv4-unicast
                address-family.
                ''',
                'mpls',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            _MetaInfoClassMember('maximum-paths', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('1', '64')], [],
                '''                Maximum number of active parallel paths per
                route
                ''',
                'maximum_paths',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            _MetaInfoClassMember('topology-id', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('6', '4095')], [],
                '''                Set the topology ID for a named
                (non-default) topology. This object must be
                set before any other configuration is
                supplied for a named (non-default) topology
                , and must be the last configuration object
                to be removed. This item should not be
                supplied for the non-named default
                topologies.
                ''',
                'topology_id',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            _MetaInfoClassMember('single-topology', ATTRIBUTE, 'Empty', 'empty',
                None, None,
                [], [],
                '''                Run IPv6 Unicast using the standard (IPv4
                Unicast) topology
                ''',
                'single_topology',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            _MetaInfoClassMember('adjacency-check', REFERENCE_ENUM_CLASS, 'IsisAdjCheck', 'Isis-adj-check',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'IsisAdjCheck',
                [], [],
                '''                Suppress check for consistent AF support on
                received IIHs
                ''',
                'adjacency_check',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            _MetaInfoClassMember('advertise-link-attributes', ATTRIBUTE, 'bool', 'boolean',
                None, None,
                [], [],
                '''                If TRUE, advertise additional link
                attributes in our LSP
                ''',
                'advertise_link_attributes',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            _MetaInfoClassMember('apply-weight', REFERENCE_ENUM_CLASS, 'IsisApplyWeight', 'Isis-apply-weight',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'IsisApplyWeight',
                [], [],
                '''                Apply weights to UCMP or ECMP only
                ''',
                'apply_weight',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            _MetaInfoClassMember('default-admin-distance', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('1', '255')], [],
                '''                Default IS-IS administrative distance
                configuration.
                ''',
                'default_admin_distance',
                'Cisco-IOS-XR-clns-isis-cfg', False, default_value="115"),
            _MetaInfoClassMember('advertise-passive-only', ATTRIBUTE, 'Empty', 'empty',
                None, None,
                [], [],
                '''                If enabled, advertise prefixes of passive
                interfaces only
                ''',
                'advertise_passive_only',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            _MetaInfoClassMember('ignore-attached-bit', ATTRIBUTE, 'bool', 'boolean',
                None, None,
                [], [],
                '''                If TRUE, Ignore other routers attached bit
                ''',
                'ignore_attached_bit',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            _MetaInfoClassMember('attached-bit', REFERENCE_ENUM_CLASS, 'IsisAttachedBit', 'Isis-attached-bit',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'IsisAttachedBit',
                [], [],
                '''                Set the attached bit in this router's level
                1 System LSP
                ''',
                'attached_bit',
                'Cisco-IOS-XR-clns-isis-cfg', False, default_value='Cisco_IOS_XR_clns_isis_cfg.IsisAttachedBit.area'),
            _MetaInfoClassMember('route-source-first-hop', ATTRIBUTE, 'bool', 'boolean',
                None, None,
                [], [],
                '''                If TRUE, routes will be installed with the
                IP address of the first-hop node as the
                source instead of the originating node
                ''',
                'route_source_first_hop',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            _MetaInfoClassMember('manual-adj-sids', REFERENCE_CLASS, 'ManualAdjSids', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'Isis.Instances.Instance.Afs.Af.AfData.ManualAdjSids',
                [], [],
                '''                Manual Adjacecy SID configuration
                ''',
                'manual_adj_sids',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            _MetaInfoClassMember('metrics', REFERENCE_CLASS, 'Metrics', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'Isis.Instances.Instance.Afs.Af.AfData.Metrics',
                [], [],
                '''                Metric configuration
                ''',
                'metrics',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            _MetaInfoClassMember('weights', REFERENCE_CLASS, 'Weights', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'Isis.Instances.Instance.Afs.Af.AfData.Weights',
                [], [],
                '''                Weight configuration
                ''',
                'weights',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            ],
            'Cisco-IOS-XR-clns-isis-cfg',
            'af-data',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-clns-isis-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg',
            is_presence=True,
        ),
    },
    'Isis.Instances.Instance.Afs.Af.TopologyName.SegmentRouting.Srv6.Srv6Locators.Srv6Locator' : {
        'meta_info' : _MetaInfoClass('Isis.Instances.Instance.Afs.Af.TopologyName.SegmentRouting.Srv6.Srv6Locators.Srv6Locator', REFERENCE_LIST,
            '''Configuration for a single SRv6 Locator''',
            False, 
            [
            _MetaInfoClassMember('locator-name', ATTRIBUTE, 'str', 'dt1:Isis-locator-name',
                None, None,
                [(1, 60)], [],
                '''                Locator Name
                ''',
                'locator_name',
                'Cisco-IOS-XR-clns-isis-cfg', True),
            _MetaInfoClassMember('running', ATTRIBUTE, 'Empty', 'empty',
                None, None,
                [], [],
                '''                The presence of this object enables a
                SRv6 Locator. This must be the first
                object created under the SRv6Locator
                container, and the last one deleted
                ''',
                'running',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            ],
            'Cisco-IOS-XR-clns-isis-cfg',
            'srv6-locator',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-clns-isis-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg',
        ),
    },
    'Isis.Instances.Instance.Afs.Af.TopologyName.SegmentRouting.Srv6.Srv6Locators' : {
        'meta_info' : _MetaInfoClass('Isis.Instances.Instance.Afs.Af.TopologyName.SegmentRouting.Srv6.Srv6Locators', REFERENCE_CLASS,
            '''SRv6 Locator configuration''',
            False, 
            [
            _MetaInfoClassMember('srv6-locator', REFERENCE_LIST, 'Srv6Locator', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'Isis.Instances.Instance.Afs.Af.TopologyName.SegmentRouting.Srv6.Srv6Locators.Srv6Locator',
                [], [],
                '''                Configuration for a single SRv6 Locator
                ''',
                'srv6_locator',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            ],
            'Cisco-IOS-XR-clns-isis-cfg',
            'srv6-locators',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-clns-isis-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg',
        ),
    },
    'Isis.Instances.Instance.Afs.Af.TopologyName.SegmentRouting.Srv6' : {
        'meta_info' : _MetaInfoClass('Isis.Instances.Instance.Afs.Af.TopologyName.SegmentRouting.Srv6', REFERENCE_CLASS,
            '''SRv6 configuration''',
            False, 
            [
            _MetaInfoClassMember('srv6-locators', REFERENCE_CLASS, 'Srv6Locators', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'Isis.Instances.Instance.Afs.Af.TopologyName.SegmentRouting.Srv6.Srv6Locators',
                [], [],
                '''                SRv6 Locator configuration
                ''',
                'srv6_locators',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            _MetaInfoClassMember('running', ATTRIBUTE, 'Empty', 'empty',
                None, None,
                [], [],
                '''                The presence of this object enables SRv6.
                This must be the first object created
                under the SRV6 container, and the last
                one deleted
                ''',
                'running',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            ],
            'Cisco-IOS-XR-clns-isis-cfg',
            'srv6',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-clns-isis-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg',
        ),
    },
    'Isis.Instances.Instance.Afs.Af.TopologyName.SegmentRouting.ConnectedPrefixSids.ConnectedPrefixSid' : {
        'meta_info' : _MetaInfoClass('Isis.Instances.Instance.Afs.Af.TopologyName.SegmentRouting.ConnectedPrefixSids.ConnectedPrefixSid', REFERENCE_LIST,
            '''Segment Routing prefix SID map''',
            False, 
            [
            _MetaInfoClassMember('address-prefix', REFERENCE_UNION, 'str', 'inet:ip-prefix',
                None, None,
                [], [],
                '''                IP address prefix
                ''',
                'address_prefix',
                'Cisco-IOS-XR-clns-isis-cfg', True, [
                    _MetaInfoClassMember('address-prefix', ATTRIBUTE, 'str', 'inet:ipv4-prefix',
                        None, None,
                        [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])/(([0-9])|([1-2][0-9])|(3[0-2]))'],
                        '''                        IP address prefix
                        ''',
                        'address_prefix',
                        'Cisco-IOS-XR-clns-isis-cfg', True),
                    _MetaInfoClassMember('address-prefix', ATTRIBUTE, 'str', 'inet:ipv6-prefix',
                        None, None,
                        [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(/(([0-9])|([0-9]{2})|(1[0-1][0-9])|(12[0-8])))'],
                        '''                        IP address prefix
                        ''',
                        'address_prefix',
                        'Cisco-IOS-XR-clns-isis-cfg', True),
                ]),
            _MetaInfoClassMember('algo', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('0', '255')], [],
                '''                Algo
                ''',
                'algo',
                'Cisco-IOS-XR-clns-isis-cfg', True),
            _MetaInfoClassMember('sid-type', REFERENCE_ENUM_CLASS, 'Isissid1', 'Isissid1',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'Isissid1',
                [], [],
                '''                SID type for the interface
                ''',
                'sid_type',
                'Cisco-IOS-XR-clns-isis-cfg', False, is_mandatory=True),
            _MetaInfoClassMember('sid', ATTRIBUTE, 'int', 'Isissid',
                None, None,
                [('0', '1048575')], [],
                '''                SID value for the interface
                ''',
                'sid',
                'Cisco-IOS-XR-clns-isis-cfg', False, is_mandatory=True),
            _MetaInfoClassMember('sid-range', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('1', '1048575')], [],
                '''                Range of SIDs
                ''',
                'sid_range',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            _MetaInfoClassMember('interface', ATTRIBUTE, 'str', 'string',
                None, None,
                [(1, 64)], [],
                '''                Interface to which prefix belongs
                ''',
                'interface',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            _MetaInfoClassMember('php', REFERENCE_ENUM_CLASS, 'IsisphpFlag', 'Isisphp-flag',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'IsisphpFlag',
                [], [],
                '''                Enable/Disable Penultimate Hop Popping
                ''',
                'php',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            _MetaInfoClassMember('explicit-null', REFERENCE_ENUM_CLASS, 'IsisexplicitNullFlag', 'Isisexplicit-null-flag',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'IsisexplicitNullFlag',
                [], [],
                '''                Enable/Disable Explicit-NULL flag
                ''',
                'explicit_null',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            ],
            'Cisco-IOS-XR-clns-isis-cfg',
            'connected-prefix-sid',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-clns-isis-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg',
        ),
    },
    'Isis.Instances.Instance.Afs.Af.TopologyName.SegmentRouting.ConnectedPrefixSids' : {
        'meta_info' : _MetaInfoClass('Isis.Instances.Instance.Afs.Af.TopologyName.SegmentRouting.ConnectedPrefixSids', REFERENCE_CLASS,
            '''Connected Segment Routing prefix SID map
configuration''',
            False, 
            [
            _MetaInfoClassMember('connected-prefix-sid', REFERENCE_LIST, 'ConnectedPrefixSid', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'Isis.Instances.Instance.Afs.Af.TopologyName.SegmentRouting.ConnectedPrefixSids.ConnectedPrefixSid',
                [], [],
                '''                Segment Routing prefix SID map
                ''',
                'connected_prefix_sid',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            ],
            'Cisco-IOS-XR-clns-isis-cfg',
            'connected-prefix-sids',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-clns-isis-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg',
        ),
    },
    'Isis.Instances.Instance.Afs.Af.TopologyName.SegmentRouting.PrefixSidMap' : {
        'meta_info' : _MetaInfoClass('Isis.Instances.Instance.Afs.Af.TopologyName.SegmentRouting.PrefixSidMap', REFERENCE_CLASS,
            '''Enable Segment Routing prefix SID map
configuration''',
            False, 
            [
            _MetaInfoClassMember('advertise-local', ATTRIBUTE, 'Empty', 'empty',
                None, None,
                [], [],
                '''                Enable Segment Routing prefix SID map
                advertise local
                ''',
                'advertise_local',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            _MetaInfoClassMember('receive', ATTRIBUTE, 'bool', 'boolean',
                None, None,
                [], [],
                '''                If TRUE, remote prefix SID map
                advertisements will be used. If FALSE,
                they will not be used.
                ''',
                'receive',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            ],
            'Cisco-IOS-XR-clns-isis-cfg',
            'prefix-sid-map',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-clns-isis-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg',
        ),
    },
    'Isis.Instances.Instance.Afs.Af.TopologyName.SegmentRouting' : {
        'meta_info' : _MetaInfoClass('Isis.Instances.Instance.Afs.Af.TopologyName.SegmentRouting', REFERENCE_CLASS,
            '''Enable Segment Routing configuration''',
            False, 
            [
            _MetaInfoClassMember('srv6', REFERENCE_CLASS, 'Srv6', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'Isis.Instances.Instance.Afs.Af.TopologyName.SegmentRouting.Srv6',
                [], [],
                '''                SRv6 configuration
                ''',
                'srv6',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            _MetaInfoClassMember('connected-prefix-sids', REFERENCE_CLASS, 'ConnectedPrefixSids', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'Isis.Instances.Instance.Afs.Af.TopologyName.SegmentRouting.ConnectedPrefixSids',
                [], [],
                '''                Connected Segment Routing prefix SID map
                configuration
                ''',
                'connected_prefix_sids',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            _MetaInfoClassMember('prefix-sid-map', REFERENCE_CLASS, 'PrefixSidMap', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'Isis.Instances.Instance.Afs.Af.TopologyName.SegmentRouting.PrefixSidMap',
                [], [],
                '''                Enable Segment Routing prefix SID map
                configuration
                ''',
                'prefix_sid_map',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            _MetaInfoClassMember('bundle-member-adj-sid', ATTRIBUTE, 'Empty', 'empty',
                None, None,
                [], [],
                '''                Enable per bundle member adjacency SID
                ''',
                'bundle_member_adj_sid',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            _MetaInfoClassMember('labeled-only', ATTRIBUTE, 'Empty', 'empty',
                None, None,
                [], [],
                '''                Only install SR labeled paths
                ''',
                'labeled_only',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            _MetaInfoClassMember('mpls', REFERENCE_ENUM_CLASS, 'IsisLabelPreference', 'Isis-label-preference',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'IsisLabelPreference',
                [], [],
                '''                Prefer segment routing labels over LDP
                labels
                ''',
                'mpls',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            ],
            'Cisco-IOS-XR-clns-isis-cfg',
            'segment-routing',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-clns-isis-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg',
        ),
    },
    'Isis.Instances.Instance.Afs.Af.TopologyName.MetricStyles.MetricStyle' : {
        'meta_info' : _MetaInfoClass('Isis.Instances.Instance.Afs.Af.TopologyName.MetricStyles.MetricStyle', REFERENCE_LIST,
            '''Configuration of metric style in LSPs''',
            False, 
            [
            _MetaInfoClassMember('level', REFERENCE_ENUM_CLASS, 'IsisInternalLevel', 'dt1:Isis-internal-level',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_datatypes', 'IsisInternalLevel',
                [], [],
                '''                Level to which configuration applies
                ''',
                'level',
                'Cisco-IOS-XR-clns-isis-cfg', True),
            _MetaInfoClassMember('style', REFERENCE_ENUM_CLASS, 'IsisMetricStyle', 'Isis-metric-style',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'IsisMetricStyle',
                [], [],
                '''                Metric Style
                ''',
                'style',
                'Cisco-IOS-XR-clns-isis-cfg', False, is_mandatory=True),
            ],
            'Cisco-IOS-XR-clns-isis-cfg',
            'metric-style',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-clns-isis-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg',
        ),
    },
    'Isis.Instances.Instance.Afs.Af.TopologyName.MetricStyles' : {
        'meta_info' : _MetaInfoClass('Isis.Instances.Instance.Afs.Af.TopologyName.MetricStyles', REFERENCE_CLASS,
            '''Metric-style configuration''',
            False, 
            [
            _MetaInfoClassMember('metric-style', REFERENCE_LIST, 'MetricStyle', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'Isis.Instances.Instance.Afs.Af.TopologyName.MetricStyles.MetricStyle',
                [], [],
                '''                Configuration of metric style in LSPs
                ''',
                'metric_style',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            ],
            'Cisco-IOS-XR-clns-isis-cfg',
            'metric-styles',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-clns-isis-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg',
        ),
    },
    'Isis.Instances.Instance.Afs.Af.TopologyName.FrrTable.FrrLoadSharings.FrrLoadSharing' : {
        'meta_info' : _MetaInfoClass('Isis.Instances.Instance.Afs.Af.TopologyName.FrrTable.FrrLoadSharings.FrrLoadSharing', REFERENCE_LIST,
            '''Disable load sharing''',
            False, 
            [
            _MetaInfoClassMember('level', REFERENCE_ENUM_CLASS, 'IsisInternalLevel', 'dt1:Isis-internal-level',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_datatypes', 'IsisInternalLevel',
                [], [],
                '''                Level to which configuration applies
                ''',
                'level',
                'Cisco-IOS-XR-clns-isis-cfg', True),
            _MetaInfoClassMember('load-sharing', REFERENCE_ENUM_CLASS, 'IsisfrrLoadSharing', 'Isisfrr-load-sharing',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'IsisfrrLoadSharing',
                [], [],
                '''                Load sharing
                ''',
                'load_sharing',
                'Cisco-IOS-XR-clns-isis-cfg', False, is_mandatory=True),
            ],
            'Cisco-IOS-XR-clns-isis-cfg',
            'frr-load-sharing',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-clns-isis-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg',
        ),
    },
    'Isis.Instances.Instance.Afs.Af.TopologyName.FrrTable.FrrLoadSharings' : {
        'meta_info' : _MetaInfoClass('Isis.Instances.Instance.Afs.Af.TopologyName.FrrTable.FrrLoadSharings', REFERENCE_CLASS,
            '''Load share prefixes across multiple
backups''',
            False, 
            [
            _MetaInfoClassMember('frr-load-sharing', REFERENCE_LIST, 'FrrLoadSharing', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'Isis.Instances.Instance.Afs.Af.TopologyName.FrrTable.FrrLoadSharings.FrrLoadSharing',
                [], [],
                '''                Disable load sharing
                ''',
                'frr_load_sharing',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            ],
            'Cisco-IOS-XR-clns-isis-cfg',
            'frr-load-sharings',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-clns-isis-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg',
        ),
    },
    'Isis.Instances.Instance.Afs.Af.TopologyName.FrrTable.FrrsrlgProtectionTypes.FrrsrlgProtectionType' : {
        'meta_info' : _MetaInfoClass('Isis.Instances.Instance.Afs.Af.TopologyName.FrrTable.FrrsrlgProtectionTypes.FrrsrlgProtectionType', REFERENCE_LIST,
            '''FRR SRLG Protection Type''',
            False, 
            [
            _MetaInfoClassMember('level', REFERENCE_ENUM_CLASS, 'IsisInternalLevel', 'dt1:Isis-internal-level',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_datatypes', 'IsisInternalLevel',
                [], [],
                '''                Level to which configuration applies
                ''',
                'level',
                'Cisco-IOS-XR-clns-isis-cfg', True),
            _MetaInfoClassMember('protection-type', REFERENCE_ENUM_CLASS, 'IsisfrrSrlgProtection', 'Isisfrr-srlg-protection',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'IsisfrrSrlgProtection',
                [], [],
                '''                Protection Type
                ''',
                'protection_type',
                'Cisco-IOS-XR-clns-isis-cfg', False, is_mandatory=True),
            ],
            'Cisco-IOS-XR-clns-isis-cfg',
            'frrsrlg-protection-type',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-clns-isis-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg',
        ),
    },
    'Isis.Instances.Instance.Afs.Af.TopologyName.FrrTable.FrrsrlgProtectionTypes' : {
        'meta_info' : _MetaInfoClass('Isis.Instances.Instance.Afs.Af.TopologyName.FrrTable.FrrsrlgProtectionTypes', REFERENCE_CLASS,
            '''SRLG protection type configuration''',
            False, 
            [
            _MetaInfoClassMember('frrsrlg-protection-type', REFERENCE_LIST, 'FrrsrlgProtectionType', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'Isis.Instances.Instance.Afs.Af.TopologyName.FrrTable.FrrsrlgProtectionTypes.FrrsrlgProtectionType',
                [], [],
                '''                FRR SRLG Protection Type
                ''',
                'frrsrlg_protection_type',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            ],
            'Cisco-IOS-XR-clns-isis-cfg',
            'frrsrlg-protection-types',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-clns-isis-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg',
        ),
    },
    'Isis.Instances.Instance.Afs.Af.TopologyName.FrrTable.PriorityLimits.PriorityLimit' : {
        'meta_info' : _MetaInfoClass('Isis.Instances.Instance.Afs.Af.TopologyName.FrrTable.PriorityLimits.PriorityLimit', REFERENCE_LIST,
            '''Limit backup computation upto the prefix
priority''',
            False, 
            [
            _MetaInfoClassMember('level', REFERENCE_ENUM_CLASS, 'IsisInternalLevel', 'dt1:Isis-internal-level',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_datatypes', 'IsisInternalLevel',
                [], [],
                '''                Level to which configuration applies
                ''',
                'level',
                'Cisco-IOS-XR-clns-isis-cfg', True),
            _MetaInfoClassMember('frr-type', REFERENCE_ENUM_CLASS, 'Isisfrr', 'Isisfrr',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'Isisfrr',
                [], [],
                '''                Computation Type
                ''',
                'frr_type',
                'Cisco-IOS-XR-clns-isis-cfg', True),
            _MetaInfoClassMember('priority', REFERENCE_ENUM_CLASS, 'IsisPrefixPriority', 'Isis-prefix-priority',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'IsisPrefixPriority',
                [], [],
                '''                Compute for all prefixes upto the
                specified priority
                ''',
                'priority',
                'Cisco-IOS-XR-clns-isis-cfg', False, is_mandatory=True),
            ],
            'Cisco-IOS-XR-clns-isis-cfg',
            'priority-limit',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-clns-isis-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg',
        ),
    },
    'Isis.Instances.Instance.Afs.Af.TopologyName.FrrTable.PriorityLimits' : {
        'meta_info' : _MetaInfoClass('Isis.Instances.Instance.Afs.Af.TopologyName.FrrTable.PriorityLimits', REFERENCE_CLASS,
            '''FRR prefix-limit configuration''',
            False, 
            [
            _MetaInfoClassMember('priority-limit', REFERENCE_LIST, 'PriorityLimit', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'Isis.Instances.Instance.Afs.Af.TopologyName.FrrTable.PriorityLimits.PriorityLimit',
                [], [],
                '''                Limit backup computation upto the prefix
                priority
                ''',
                'priority_limit',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            ],
            'Cisco-IOS-XR-clns-isis-cfg',
            'priority-limits',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-clns-isis-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg',
        ),
    },
    'Isis.Instances.Instance.Afs.Af.TopologyName.FrrTable.FrrRemoteLfaPrefixes.FrrRemoteLfaPrefix' : {
        'meta_info' : _MetaInfoClass('Isis.Instances.Instance.Afs.Af.TopologyName.FrrTable.FrrRemoteLfaPrefixes.FrrRemoteLfaPrefix', REFERENCE_LIST,
            '''Filter remote LFA router IDs using
prefix-list''',
            False, 
            [
            _MetaInfoClassMember('level', REFERENCE_ENUM_CLASS, 'IsisInternalLevel', 'dt1:Isis-internal-level',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_datatypes', 'IsisInternalLevel',
                [], [],
                '''                Level to which configuration applies
                ''',
                'level',
                'Cisco-IOS-XR-clns-isis-cfg', True),
            _MetaInfoClassMember('prefix-list-name', ATTRIBUTE, 'str', 'xr:Cisco-ios-xr-string',
                None, None,
                [(1, 32)], [],
                '''                Name of the prefix list
                ''',
                'prefix_list_name',
                'Cisco-IOS-XR-clns-isis-cfg', False, is_mandatory=True),
            ],
            'Cisco-IOS-XR-clns-isis-cfg',
            'frr-remote-lfa-prefix',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-clns-isis-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg',
        ),
    },
    'Isis.Instances.Instance.Afs.Af.TopologyName.FrrTable.FrrRemoteLfaPrefixes' : {
        'meta_info' : _MetaInfoClass('Isis.Instances.Instance.Afs.Af.TopologyName.FrrTable.FrrRemoteLfaPrefixes', REFERENCE_CLASS,
            '''FRR remote LFA prefix list filter
configuration''',
            False, 
            [
            _MetaInfoClassMember('frr-remote-lfa-prefix', REFERENCE_LIST, 'FrrRemoteLfaPrefix', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'Isis.Instances.Instance.Afs.Af.TopologyName.FrrTable.FrrRemoteLfaPrefixes.FrrRemoteLfaPrefix',
                [], [],
                '''                Filter remote LFA router IDs using
                prefix-list
                ''',
                'frr_remote_lfa_prefix',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            ],
            'Cisco-IOS-XR-clns-isis-cfg',
            'frr-remote-lfa-prefixes',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-clns-isis-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg',
        ),
    },
    'Isis.Instances.Instance.Afs.Af.TopologyName.FrrTable.FrrTiebreakers.FrrTiebreaker' : {
        'meta_info' : _MetaInfoClass('Isis.Instances.Instance.Afs.Af.TopologyName.FrrTable.FrrTiebreakers.FrrTiebreaker', REFERENCE_LIST,
            '''Configure tiebreaker for multiple backups''',
            False, 
            [
            _MetaInfoClassMember('level', REFERENCE_ENUM_CLASS, 'IsisInternalLevel', 'dt1:Isis-internal-level',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_datatypes', 'IsisInternalLevel',
                [], [],
                '''                Level to which configuration applies
                ''',
                'level',
                'Cisco-IOS-XR-clns-isis-cfg', True),
            _MetaInfoClassMember('tiebreaker', REFERENCE_ENUM_CLASS, 'IsisfrrTiebreaker', 'Isisfrr-tiebreaker',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'IsisfrrTiebreaker',
                [], [],
                '''                Tiebreaker for which configuration
                applies
                ''',
                'tiebreaker',
                'Cisco-IOS-XR-clns-isis-cfg', True),
            _MetaInfoClassMember('index', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('1', '255')], [],
                '''                Preference order among tiebreakers
                ''',
                'index',
                'Cisco-IOS-XR-clns-isis-cfg', False, is_mandatory=True),
            ],
            'Cisco-IOS-XR-clns-isis-cfg',
            'frr-tiebreaker',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-clns-isis-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg',
        ),
    },
    'Isis.Instances.Instance.Afs.Af.TopologyName.FrrTable.FrrTiebreakers' : {
        'meta_info' : _MetaInfoClass('Isis.Instances.Instance.Afs.Af.TopologyName.FrrTable.FrrTiebreakers', REFERENCE_CLASS,
            '''FRR tiebreakers configuration''',
            False, 
            [
            _MetaInfoClassMember('frr-tiebreaker', REFERENCE_LIST, 'FrrTiebreaker', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'Isis.Instances.Instance.Afs.Af.TopologyName.FrrTable.FrrTiebreakers.FrrTiebreaker',
                [], [],
                '''                Configure tiebreaker for multiple backups
                ''',
                'frr_tiebreaker',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            ],
            'Cisco-IOS-XR-clns-isis-cfg',
            'frr-tiebreakers',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-clns-isis-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg',
        ),
    },
    'Isis.Instances.Instance.Afs.Af.TopologyName.FrrTable.FrrUseCandOnlies.FrrUseCandOnly' : {
        'meta_info' : _MetaInfoClass('Isis.Instances.Instance.Afs.Af.TopologyName.FrrTable.FrrUseCandOnlies.FrrUseCandOnly', REFERENCE_LIST,
            '''Configure use candidate only to exclude
interfaces as backup''',
            False, 
            [
            _MetaInfoClassMember('level', REFERENCE_ENUM_CLASS, 'IsisInternalLevel', 'dt1:Isis-internal-level',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_datatypes', 'IsisInternalLevel',
                [], [],
                '''                Level to which configuration applies
                ''',
                'level',
                'Cisco-IOS-XR-clns-isis-cfg', True),
            _MetaInfoClassMember('frr-type', REFERENCE_ENUM_CLASS, 'Isisfrr', 'Isisfrr',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'Isisfrr',
                [], [],
                '''                Computation Type
                ''',
                'frr_type',
                'Cisco-IOS-XR-clns-isis-cfg', True),
            ],
            'Cisco-IOS-XR-clns-isis-cfg',
            'frr-use-cand-only',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-clns-isis-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg',
        ),
    },
    'Isis.Instances.Instance.Afs.Af.TopologyName.FrrTable.FrrUseCandOnlies' : {
        'meta_info' : _MetaInfoClass('Isis.Instances.Instance.Afs.Af.TopologyName.FrrTable.FrrUseCandOnlies', REFERENCE_CLASS,
            '''FRR use candidate only configuration''',
            False, 
            [
            _MetaInfoClassMember('frr-use-cand-only', REFERENCE_LIST, 'FrrUseCandOnly', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'Isis.Instances.Instance.Afs.Af.TopologyName.FrrTable.FrrUseCandOnlies.FrrUseCandOnly',
                [], [],
                '''                Configure use candidate only to exclude
                interfaces as backup
                ''',
                'frr_use_cand_only',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            ],
            'Cisco-IOS-XR-clns-isis-cfg',
            'frr-use-cand-onlies',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-clns-isis-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg',
        ),
    },
    'Isis.Instances.Instance.Afs.Af.TopologyName.FrrTable' : {
        'meta_info' : _MetaInfoClass('Isis.Instances.Instance.Afs.Af.TopologyName.FrrTable', REFERENCE_CLASS,
            '''Fast-ReRoute configuration''',
            False, 
            [
            _MetaInfoClassMember('frr-load-sharings', REFERENCE_CLASS, 'FrrLoadSharings', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'Isis.Instances.Instance.Afs.Af.TopologyName.FrrTable.FrrLoadSharings',
                [], [],
                '''                Load share prefixes across multiple
                backups
                ''',
                'frr_load_sharings',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            _MetaInfoClassMember('frrsrlg-protection-types', REFERENCE_CLASS, 'FrrsrlgProtectionTypes', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'Isis.Instances.Instance.Afs.Af.TopologyName.FrrTable.FrrsrlgProtectionTypes',
                [], [],
                '''                SRLG protection type configuration
                ''',
                'frrsrlg_protection_types',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            _MetaInfoClassMember('priority-limits', REFERENCE_CLASS, 'PriorityLimits', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'Isis.Instances.Instance.Afs.Af.TopologyName.FrrTable.PriorityLimits',
                [], [],
                '''                FRR prefix-limit configuration
                ''',
                'priority_limits',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            _MetaInfoClassMember('frr-remote-lfa-prefixes', REFERENCE_CLASS, 'FrrRemoteLfaPrefixes', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'Isis.Instances.Instance.Afs.Af.TopologyName.FrrTable.FrrRemoteLfaPrefixes',
                [], [],
                '''                FRR remote LFA prefix list filter
                configuration
                ''',
                'frr_remote_lfa_prefixes',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            _MetaInfoClassMember('frr-tiebreakers', REFERENCE_CLASS, 'FrrTiebreakers', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'Isis.Instances.Instance.Afs.Af.TopologyName.FrrTable.FrrTiebreakers',
                [], [],
                '''                FRR tiebreakers configuration
                ''',
                'frr_tiebreakers',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            _MetaInfoClassMember('frr-use-cand-onlies', REFERENCE_CLASS, 'FrrUseCandOnlies', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'Isis.Instances.Instance.Afs.Af.TopologyName.FrrTable.FrrUseCandOnlies',
                [], [],
                '''                FRR use candidate only configuration
                ''',
                'frr_use_cand_onlies',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            _MetaInfoClassMember('frr-initial-delay', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('100', '60000')], [],
                '''                Delay before running FRR (milliseconds)
                ''',
                'frr_initial_delay',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            ],
            'Cisco-IOS-XR-clns-isis-cfg',
            'frr-table',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-clns-isis-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg',
        ),
    },
    'Isis.Instances.Instance.Afs.Af.TopologyName.RouterId' : {
        'meta_info' : _MetaInfoClass('Isis.Instances.Instance.Afs.Af.TopologyName.RouterId', REFERENCE_CLASS,
            '''Stable IP address for system. Will only be
applied for the unicast sub-address-family.''',
            False, 
            [
            _MetaInfoClassMember('address', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                IPv4/IPv6 address to be used as a router
                ID. Precisely one of Address and Interface
                must be specified.
                ''',
                'address',
                'Cisco-IOS-XR-clns-isis-cfg', False, has_must=True),
            _MetaInfoClassMember('interface-name', ATTRIBUTE, 'str', 'xr:Interface-name',
                None, None,
                [], [b'[a-zA-Z0-9._/-]+'],
                '''                Interface with designated stable IP
                address to be used as a router ID. This
                must be a Loopback interface. Precisely
                one of Address and Interface must be
                specified.
                ''',
                'interface_name',
                'Cisco-IOS-XR-clns-isis-cfg', False, has_must=True),
            ],
            'Cisco-IOS-XR-clns-isis-cfg',
            'router-id',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-clns-isis-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg',
        ),
    },
    'Isis.Instances.Instance.Afs.Af.TopologyName.SpfPrefixPriorities.SpfPrefixPriority' : {
        'meta_info' : _MetaInfoClass('Isis.Instances.Instance.Afs.Af.TopologyName.SpfPrefixPriorities.SpfPrefixPriority', REFERENCE_LIST,
            '''Determine SPF priority for prefixes''',
            False, 
            [
            _MetaInfoClassMember('level', REFERENCE_ENUM_CLASS, 'IsisInternalLevel', 'dt1:Isis-internal-level',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_datatypes', 'IsisInternalLevel',
                [], [],
                '''                SPF Level for prefix prioritization
                ''',
                'level',
                'Cisco-IOS-XR-clns-isis-cfg', True),
            _MetaInfoClassMember('prefix-priority-type', REFERENCE_ENUM_CLASS, 'IsisPrefixPriority', 'Isis-prefix-priority',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'IsisPrefixPriority',
                [], [],
                '''                SPF Priority to assign matching prefixes
                ''',
                'prefix_priority_type',
                'Cisco-IOS-XR-clns-isis-cfg', True),
            _MetaInfoClassMember('admin-tag', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('1', '4294967295')], [],
                '''                Tag value to determine prefixes for this
                priority
                ''',
                'admin_tag',
                'Cisco-IOS-XR-clns-isis-cfg', False, has_must=True),
            _MetaInfoClassMember('access-list-name', ATTRIBUTE, 'str', 'xr:Cisco-ios-xr-string',
                None, None,
                [(1, 64)], [],
                '''                Access List to determine prefixes for
                this priority
                ''',
                'access_list_name',
                'Cisco-IOS-XR-clns-isis-cfg', False, has_must=True),
            ],
            'Cisco-IOS-XR-clns-isis-cfg',
            'spf-prefix-priority',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-clns-isis-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg',
        ),
    },
    'Isis.Instances.Instance.Afs.Af.TopologyName.SpfPrefixPriorities' : {
        'meta_info' : _MetaInfoClass('Isis.Instances.Instance.Afs.Af.TopologyName.SpfPrefixPriorities', REFERENCE_CLASS,
            '''SPF Prefix Priority configuration''',
            False, 
            [
            _MetaInfoClassMember('spf-prefix-priority', REFERENCE_LIST, 'SpfPrefixPriority', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'Isis.Instances.Instance.Afs.Af.TopologyName.SpfPrefixPriorities.SpfPrefixPriority',
                [], [],
                '''                Determine SPF priority for prefixes
                ''',
                'spf_prefix_priority',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            ],
            'Cisco-IOS-XR-clns-isis-cfg',
            'spf-prefix-priorities',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-clns-isis-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg',
        ),
    },
    'Isis.Instances.Instance.Afs.Af.TopologyName.SummaryPrefixes.SummaryPrefix' : {
        'meta_info' : _MetaInfoClass('Isis.Instances.Instance.Afs.Af.TopologyName.SummaryPrefixes.SummaryPrefix', REFERENCE_LIST,
            '''Configure IP address prefixes to advertise''',
            False, 
            [
            _MetaInfoClassMember('address-prefix', REFERENCE_UNION, 'str', 'inet:ip-prefix',
                None, None,
                [], [],
                '''                IP summary address prefix
                ''',
                'address_prefix',
                'Cisco-IOS-XR-clns-isis-cfg', True, [
                    _MetaInfoClassMember('address-prefix', ATTRIBUTE, 'str', 'inet:ipv4-prefix',
                        None, None,
                        [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])/(([0-9])|([1-2][0-9])|(3[0-2]))'],
                        '''                        IP summary address prefix
                        ''',
                        'address_prefix',
                        'Cisco-IOS-XR-clns-isis-cfg', True),
                    _MetaInfoClassMember('address-prefix', ATTRIBUTE, 'str', 'inet:ipv6-prefix',
                        None, None,
                        [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(/(([0-9])|([0-9]{2})|(1[0-1][0-9])|(12[0-8])))'],
                        '''                        IP summary address prefix
                        ''',
                        'address_prefix',
                        'Cisco-IOS-XR-clns-isis-cfg', True),
                ]),
            _MetaInfoClassMember('tag', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('1', '4294967295')], [],
                '''                The tag value
                ''',
                'tag',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            _MetaInfoClassMember('level', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('1', '2')], [],
                '''                Level in which to summarize routes
                ''',
                'level',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            ],
            'Cisco-IOS-XR-clns-isis-cfg',
            'summary-prefix',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-clns-isis-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg',
        ),
    },
    'Isis.Instances.Instance.Afs.Af.TopologyName.SummaryPrefixes' : {
        'meta_info' : _MetaInfoClass('Isis.Instances.Instance.Afs.Af.TopologyName.SummaryPrefixes', REFERENCE_CLASS,
            '''Summary-prefix configuration''',
            False, 
            [
            _MetaInfoClassMember('summary-prefix', REFERENCE_LIST, 'SummaryPrefix', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'Isis.Instances.Instance.Afs.Af.TopologyName.SummaryPrefixes.SummaryPrefix',
                [], [],
                '''                Configure IP address prefixes to advertise
                ''',
                'summary_prefix',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            ],
            'Cisco-IOS-XR-clns-isis-cfg',
            'summary-prefixes',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-clns-isis-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg',
        ),
    },
    'Isis.Instances.Instance.Afs.Af.TopologyName.MicroLoopAvoidance' : {
        'meta_info' : _MetaInfoClass('Isis.Instances.Instance.Afs.Af.TopologyName.MicroLoopAvoidance', REFERENCE_CLASS,
            '''Micro Loop Avoidance configuration''',
            False, 
            [
            _MetaInfoClassMember('enable', REFERENCE_ENUM_CLASS, 'IsisMicroLoopAvoidance', 'Isis-micro-loop-avoidance',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'IsisMicroLoopAvoidance',
                [], [],
                '''                MicroLoop avoidance enable configuration
                ''',
                'enable',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            _MetaInfoClassMember('rib-update-delay', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('1000', '65535')], [],
                '''                Value of delay in msecs in updating RIB
                ''',
                'rib_update_delay',
                'Cisco-IOS-XR-clns-isis-cfg', False, default_value="5000"),
            ],
            'Cisco-IOS-XR-clns-isis-cfg',
            'micro-loop-avoidance',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-clns-isis-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg',
        ),
    },
    'Isis.Instances.Instance.Afs.Af.TopologyName.Ucmp.Enable' : {
        'meta_info' : _MetaInfoClass('Isis.Instances.Instance.Afs.Af.TopologyName.Ucmp.Enable', REFERENCE_CLASS,
            '''UCMP feature enable configuration''',
            False, 
            [
            _MetaInfoClassMember('variance', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('101', '10000')], [],
                '''                Value of variance
                ''',
                'variance',
                'Cisco-IOS-XR-clns-isis-cfg', False, default_value="200"),
            _MetaInfoClassMember('prefix-list-name', ATTRIBUTE, 'str', 'xr:Cisco-ios-xr-string',
                None, None,
                [(1, 32)], [],
                '''                Name of the Prefix List
                ''',
                'prefix_list_name',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            ],
            'Cisco-IOS-XR-clns-isis-cfg',
            'enable',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-clns-isis-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg',
        ),
    },
    'Isis.Instances.Instance.Afs.Af.TopologyName.Ucmp.ExcludeInterfaces.ExcludeInterface' : {
        'meta_info' : _MetaInfoClass('Isis.Instances.Instance.Afs.Af.TopologyName.Ucmp.ExcludeInterfaces.ExcludeInterface', REFERENCE_LIST,
            '''Exclude this interface from UCMP path
computation''',
            False, 
            [
            _MetaInfoClassMember('interface-name', ATTRIBUTE, 'str', 'xr:Interface-name',
                None, None,
                [], [b'[a-zA-Z0-9._/-]+'],
                '''                Name of the interface to be excluded
                ''',
                'interface_name',
                'Cisco-IOS-XR-clns-isis-cfg', True),
            ],
            'Cisco-IOS-XR-clns-isis-cfg',
            'exclude-interface',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-clns-isis-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg',
        ),
    },
    'Isis.Instances.Instance.Afs.Af.TopologyName.Ucmp.ExcludeInterfaces' : {
        'meta_info' : _MetaInfoClass('Isis.Instances.Instance.Afs.Af.TopologyName.Ucmp.ExcludeInterfaces', REFERENCE_CLASS,
            '''Interfaces excluded from UCMP path
computation''',
            False, 
            [
            _MetaInfoClassMember('exclude-interface', REFERENCE_LIST, 'ExcludeInterface', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'Isis.Instances.Instance.Afs.Af.TopologyName.Ucmp.ExcludeInterfaces.ExcludeInterface',
                [], [],
                '''                Exclude this interface from UCMP path
                computation
                ''',
                'exclude_interface',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            ],
            'Cisco-IOS-XR-clns-isis-cfg',
            'exclude-interfaces',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-clns-isis-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg',
        ),
    },
    'Isis.Instances.Instance.Afs.Af.TopologyName.Ucmp' : {
        'meta_info' : _MetaInfoClass('Isis.Instances.Instance.Afs.Af.TopologyName.Ucmp', REFERENCE_CLASS,
            '''UCMP (UnEqual Cost MultiPath) configuration''',
            False, 
            [
            _MetaInfoClassMember('enable', REFERENCE_CLASS, 'Enable', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'Isis.Instances.Instance.Afs.Af.TopologyName.Ucmp.Enable',
                [], [],
                '''                UCMP feature enable configuration
                ''',
                'enable',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            _MetaInfoClassMember('exclude-interfaces', REFERENCE_CLASS, 'ExcludeInterfaces', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'Isis.Instances.Instance.Afs.Af.TopologyName.Ucmp.ExcludeInterfaces',
                [], [],
                '''                Interfaces excluded from UCMP path
                computation
                ''',
                'exclude_interfaces',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            _MetaInfoClassMember('delay-interval', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('100', '65535')], [],
                '''                Delay in msecs between primary SPF and
                UCMP computation
                ''',
                'delay_interval',
                'Cisco-IOS-XR-clns-isis-cfg', False, default_value="100"),
            ],
            'Cisco-IOS-XR-clns-isis-cfg',
            'ucmp',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-clns-isis-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg',
        ),
    },
    'Isis.Instances.Instance.Afs.Af.TopologyName.MaxRedistPrefixes.MaxRedistPrefix' : {
        'meta_info' : _MetaInfoClass('Isis.Instances.Instance.Afs.Af.TopologyName.MaxRedistPrefixes.MaxRedistPrefix', REFERENCE_LIST,
            '''An upper limit on the number of
redistributed prefixes which may be
included in the local system's LSP''',
            False, 
            [
            _MetaInfoClassMember('level', REFERENCE_ENUM_CLASS, 'IsisInternalLevel', 'dt1:Isis-internal-level',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_datatypes', 'IsisInternalLevel',
                [], [],
                '''                Level to which configuration applies
                ''',
                'level',
                'Cisco-IOS-XR-clns-isis-cfg', True),
            _MetaInfoClassMember('prefix-limit', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('1', '28000')], [],
                '''                Max number of prefixes
                ''',
                'prefix_limit',
                'Cisco-IOS-XR-clns-isis-cfg', False, is_mandatory=True),
            ],
            'Cisco-IOS-XR-clns-isis-cfg',
            'max-redist-prefix',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-clns-isis-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg',
        ),
    },
    'Isis.Instances.Instance.Afs.Af.TopologyName.MaxRedistPrefixes' : {
        'meta_info' : _MetaInfoClass('Isis.Instances.Instance.Afs.Af.TopologyName.MaxRedistPrefixes', REFERENCE_CLASS,
            '''Maximum number of redistributed
prefixesconfiguration''',
            False, 
            [
            _MetaInfoClassMember('max-redist-prefix', REFERENCE_LIST, 'MaxRedistPrefix', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'Isis.Instances.Instance.Afs.Af.TopologyName.MaxRedistPrefixes.MaxRedistPrefix',
                [], [],
                '''                An upper limit on the number of
                redistributed prefixes which may be
                included in the local system's LSP
                ''',
                'max_redist_prefix',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            ],
            'Cisco-IOS-XR-clns-isis-cfg',
            'max-redist-prefixes',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-clns-isis-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg',
        ),
    },
    'Isis.Instances.Instance.Afs.Af.TopologyName.Propagations.Propagation' : {
        'meta_info' : _MetaInfoClass('Isis.Instances.Instance.Afs.Af.TopologyName.Propagations.Propagation', REFERENCE_LIST,
            '''Propagate routes between IS-IS levels''',
            False, 
            [
            _MetaInfoClassMember('source-level', REFERENCE_ENUM_CLASS, 'IsisInternalLevel', 'dt1:Isis-internal-level',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_datatypes', 'IsisInternalLevel',
                [], [],
                '''                Source level for routes
                ''',
                'source_level',
                'Cisco-IOS-XR-clns-isis-cfg', True),
            _MetaInfoClassMember('destination-level', REFERENCE_ENUM_CLASS, 'IsisInternalLevel', 'dt1:Isis-internal-level',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_datatypes', 'IsisInternalLevel',
                [], [],
                '''                Destination level for routes.  Must
                differ from SourceLevel
                ''',
                'destination_level',
                'Cisco-IOS-XR-clns-isis-cfg', True),
            _MetaInfoClassMember('route-policy-name', ATTRIBUTE, 'str', 'xr:Cisco-ios-xr-string',
                None, None,
                [(1, 64)], [],
                '''                Route policy limiting routes to be
                propagated
                ''',
                'route_policy_name',
                'Cisco-IOS-XR-clns-isis-cfg', False, is_mandatory=True),
            ],
            'Cisco-IOS-XR-clns-isis-cfg',
            'propagation',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-clns-isis-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg',
        ),
    },
    'Isis.Instances.Instance.Afs.Af.TopologyName.Propagations' : {
        'meta_info' : _MetaInfoClass('Isis.Instances.Instance.Afs.Af.TopologyName.Propagations', REFERENCE_CLASS,
            '''Route propagation configuration''',
            False, 
            [
            _MetaInfoClassMember('propagation', REFERENCE_LIST, 'Propagation', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'Isis.Instances.Instance.Afs.Af.TopologyName.Propagations.Propagation',
                [], [],
                '''                Propagate routes between IS-IS levels
                ''',
                'propagation',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            ],
            'Cisco-IOS-XR-clns-isis-cfg',
            'propagations',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-clns-isis-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg',
        ),
    },
    'Isis.Instances.Instance.Afs.Af.TopologyName.Redistributions.Redistribution.ConnectedOrStaticOrRipOrSubscriberOrMobile' : {
        'meta_info' : _MetaInfoClass('Isis.Instances.Instance.Afs.Af.TopologyName.Redistributions.Redistribution.ConnectedOrStaticOrRipOrSubscriberOrMobile', REFERENCE_CLASS,
            '''connected or static or rip or subscriber
or mobile''',
            False, 
            [
            _MetaInfoClassMember('metric', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('0', '16777215')], [],
                '''                Metric for redistributed routes: <0-63>
                for narrow, <0-16777215> for wide
                ''',
                'metric',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            _MetaInfoClassMember('levels', REFERENCE_ENUM_CLASS, 'IsisConfigurableLevels', 'Isis-configurable-levels',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'IsisConfigurableLevels',
                [], [],
                '''                Levels to redistribute routes into
                ''',
                'levels',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            _MetaInfoClassMember('route-policy-name', ATTRIBUTE, 'str', 'xr:Cisco-ios-xr-string',
                None, None,
                [(1, 64)], [],
                '''                Route policy to control redistribution.
                ''',
                'route_policy_name',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            _MetaInfoClassMember('metric-type', REFERENCE_ENUM_CLASS, 'IsisMetric', 'Isis-metric',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'IsisMetric',
                [], [],
                '''                IS-IS metric type
                ''',
                'metric_type',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            _MetaInfoClassMember('ospf-route-type', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('0', '4294967295')], [],
                '''                OSPF route types to redistribute.  May
                only be specified if Protocol is OSPF.
                ''',
                'ospf_route_type',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            ],
            'Cisco-IOS-XR-clns-isis-cfg',
            'connected-or-static-or-rip-or-subscriber-or-mobile',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-clns-isis-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg',
            is_presence=True,
            has_when=True,
        ),
    },
    'Isis.Instances.Instance.Afs.Af.TopologyName.Redistributions.Redistribution.OspfOrOspfv3OrIsisOrApplication' : {
        'meta_info' : _MetaInfoClass('Isis.Instances.Instance.Afs.Af.TopologyName.Redistributions.Redistribution.OspfOrOspfv3OrIsisOrApplication', REFERENCE_LIST,
            '''ospf or ospfv3 or isis or application''',
            False, 
            [
            _MetaInfoClassMember('instance-name', ATTRIBUTE, 'str', 'xr:Cisco-ios-xr-string',
                None, None,
                [(1, 64)], [],
                '''                Protocol Instance Identifier.  Mandatory
                for ISIS, OSPF and application, must not
                be specified otherwise.
                ''',
                'instance_name',
                'Cisco-IOS-XR-clns-isis-cfg', True),
            _MetaInfoClassMember('metric', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('0', '16777215')], [],
                '''                Metric for redistributed routes: <0-63>
                for narrow, <0-16777215> for wide
                ''',
                'metric',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            _MetaInfoClassMember('levels', REFERENCE_ENUM_CLASS, 'IsisConfigurableLevels', 'Isis-configurable-levels',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'IsisConfigurableLevels',
                [], [],
                '''                Levels to redistribute routes into
                ''',
                'levels',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            _MetaInfoClassMember('route-policy-name', ATTRIBUTE, 'str', 'xr:Cisco-ios-xr-string',
                None, None,
                [(1, 64)], [],
                '''                Route policy to control redistribution.
                ''',
                'route_policy_name',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            _MetaInfoClassMember('metric-type', REFERENCE_ENUM_CLASS, 'IsisMetric', 'Isis-metric',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'IsisMetric',
                [], [],
                '''                IS-IS metric type
                ''',
                'metric_type',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            _MetaInfoClassMember('ospf-route-type', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('0', '4294967295')], [],
                '''                OSPF route types to redistribute.  May
                only be specified if Protocol is OSPF.
                ''',
                'ospf_route_type',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            ],
            'Cisco-IOS-XR-clns-isis-cfg',
            'ospf-or-ospfv3-or-isis-or-application',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-clns-isis-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg',
            has_when=True,
        ),
    },
    'Isis.Instances.Instance.Afs.Af.TopologyName.Redistributions.Redistribution.Bgp' : {
        'meta_info' : _MetaInfoClass('Isis.Instances.Instance.Afs.Af.TopologyName.Redistributions.Redistribution.Bgp', REFERENCE_LIST,
            '''bgp''',
            False, 
            [
            _MetaInfoClassMember('as-xx', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('0', '65535')], [],
                '''                First half of BGP AS number in XX.YY
                format.  Mandatory if Protocol is BGP
                and must not be specified otherwise.
                Must be a non-zero value if second half
                is zero.
                ''',
                'as_xx',
                'Cisco-IOS-XR-clns-isis-cfg', True),
            _MetaInfoClassMember('as-yy', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('0', '4294967295')], [],
                '''                Second half of BGP AS number in XX.YY
                format. Mandatory if Protocol is BGP and
                must not be specified otherwise. Must be
                a non-zero value if first half is zero.
                ''',
                'as_yy',
                'Cisco-IOS-XR-clns-isis-cfg', True),
            _MetaInfoClassMember('metric', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('0', '16777215')], [],
                '''                Metric for redistributed routes: <0-63>
                for narrow, <0-16777215> for wide
                ''',
                'metric',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            _MetaInfoClassMember('levels', REFERENCE_ENUM_CLASS, 'IsisConfigurableLevels', 'Isis-configurable-levels',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'IsisConfigurableLevels',
                [], [],
                '''                Levels to redistribute routes into
                ''',
                'levels',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            _MetaInfoClassMember('route-policy-name', ATTRIBUTE, 'str', 'xr:Cisco-ios-xr-string',
                None, None,
                [(1, 64)], [],
                '''                Route policy to control redistribution.
                ''',
                'route_policy_name',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            _MetaInfoClassMember('metric-type', REFERENCE_ENUM_CLASS, 'IsisMetric', 'Isis-metric',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'IsisMetric',
                [], [],
                '''                IS-IS metric type
                ''',
                'metric_type',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            _MetaInfoClassMember('ospf-route-type', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('0', '4294967295')], [],
                '''                OSPF route types to redistribute.  May
                only be specified if Protocol is OSPF.
                ''',
                'ospf_route_type',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            ],
            'Cisco-IOS-XR-clns-isis-cfg',
            'bgp',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-clns-isis-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg',
            has_when=True,
        ),
    },
    'Isis.Instances.Instance.Afs.Af.TopologyName.Redistributions.Redistribution.Eigrp' : {
        'meta_info' : _MetaInfoClass('Isis.Instances.Instance.Afs.Af.TopologyName.Redistributions.Redistribution.Eigrp', REFERENCE_LIST,
            '''eigrp''',
            False, 
            [
            _MetaInfoClassMember('as-zz', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('1', '65535')], [],
                '''                Eigrp as number.
                ''',
                'as_zz',
                'Cisco-IOS-XR-clns-isis-cfg', True),
            _MetaInfoClassMember('metric', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('0', '16777215')], [],
                '''                Metric for redistributed routes: <0-63>
                for narrow, <0-16777215> for wide
                ''',
                'metric',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            _MetaInfoClassMember('levels', REFERENCE_ENUM_CLASS, 'IsisConfigurableLevels', 'Isis-configurable-levels',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'IsisConfigurableLevels',
                [], [],
                '''                Levels to redistribute routes into
                ''',
                'levels',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            _MetaInfoClassMember('route-policy-name', ATTRIBUTE, 'str', 'xr:Cisco-ios-xr-string',
                None, None,
                [(1, 64)], [],
                '''                Route policy to control redistribution.
                ''',
                'route_policy_name',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            _MetaInfoClassMember('metric-type', REFERENCE_ENUM_CLASS, 'IsisMetric', 'Isis-metric',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'IsisMetric',
                [], [],
                '''                IS-IS metric type
                ''',
                'metric_type',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            _MetaInfoClassMember('ospf-route-type', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('0', '4294967295')], [],
                '''                OSPF route types to redistribute.  May
                only be specified if Protocol is OSPF.
                ''',
                'ospf_route_type',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            ],
            'Cisco-IOS-XR-clns-isis-cfg',
            'eigrp',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-clns-isis-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg',
            has_when=True,
        ),
    },
    'Isis.Instances.Instance.Afs.Af.TopologyName.Redistributions.Redistribution' : {
        'meta_info' : _MetaInfoClass('Isis.Instances.Instance.Afs.Af.TopologyName.Redistributions.Redistribution', REFERENCE_LIST,
            '''Redistribution of other protocols into
this IS-IS instance''',
            False, 
            [
            _MetaInfoClassMember('protocol-name', REFERENCE_ENUM_CLASS, 'IsisRedistProto', 'Isis-redist-proto',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'IsisRedistProto',
                [], [],
                '''                The protocol to be redistributed.  OSPFv3
                may not be specified for an IPv4 topology
                and OSPF may not be specified for an IPv6
                topology.
                ''',
                'protocol_name',
                'Cisco-IOS-XR-clns-isis-cfg', True),
            _MetaInfoClassMember('connected-or-static-or-rip-or-subscriber-or-mobile', REFERENCE_CLASS, 'ConnectedOrStaticOrRipOrSubscriberOrMobile', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'Isis.Instances.Instance.Afs.Af.TopologyName.Redistributions.Redistribution.ConnectedOrStaticOrRipOrSubscriberOrMobile',
                [], [],
                '''                connected or static or rip or subscriber
                or mobile
                ''',
                'connected_or_static_or_rip_or_subscriber_or_mobile',
                'Cisco-IOS-XR-clns-isis-cfg', False, is_presence=True, has_when=True),
            _MetaInfoClassMember('ospf-or-ospfv3-or-isis-or-application', REFERENCE_LIST, 'OspfOrOspfv3OrIsisOrApplication', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'Isis.Instances.Instance.Afs.Af.TopologyName.Redistributions.Redistribution.OspfOrOspfv3OrIsisOrApplication',
                [], [],
                '''                ospf or ospfv3 or isis or application
                ''',
                'ospf_or_ospfv3_or_isis_or_application',
                'Cisco-IOS-XR-clns-isis-cfg', False, has_when=True),
            _MetaInfoClassMember('bgp', REFERENCE_LIST, 'Bgp', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'Isis.Instances.Instance.Afs.Af.TopologyName.Redistributions.Redistribution.Bgp',
                [], [],
                '''                bgp
                ''',
                'bgp',
                'Cisco-IOS-XR-clns-isis-cfg', False, has_when=True),
            _MetaInfoClassMember('eigrp', REFERENCE_LIST, 'Eigrp', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'Isis.Instances.Instance.Afs.Af.TopologyName.Redistributions.Redistribution.Eigrp',
                [], [],
                '''                eigrp
                ''',
                'eigrp',
                'Cisco-IOS-XR-clns-isis-cfg', False, has_when=True),
            ],
            'Cisco-IOS-XR-clns-isis-cfg',
            'redistribution',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-clns-isis-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg',
            has_must=True,
        ),
    },
    'Isis.Instances.Instance.Afs.Af.TopologyName.Redistributions' : {
        'meta_info' : _MetaInfoClass('Isis.Instances.Instance.Afs.Af.TopologyName.Redistributions', REFERENCE_CLASS,
            '''Protocol redistribution configuration''',
            False, 
            [
            _MetaInfoClassMember('redistribution', REFERENCE_LIST, 'Redistribution', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'Isis.Instances.Instance.Afs.Af.TopologyName.Redistributions.Redistribution',
                [], [],
                '''                Redistribution of other protocols into
                this IS-IS instance
                ''',
                'redistribution',
                'Cisco-IOS-XR-clns-isis-cfg', False, has_must=True),
            ],
            'Cisco-IOS-XR-clns-isis-cfg',
            'redistributions',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-clns-isis-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg',
        ),
    },
    'Isis.Instances.Instance.Afs.Af.TopologyName.ApplicationTables.ApplicationTable.AttributeTable' : {
        'meta_info' : _MetaInfoClass('Isis.Instances.Instance.Afs.Af.TopologyName.ApplicationTables.ApplicationTable.AttributeTable', REFERENCE_LIST,
            '''Attribute Name''',
            False, 
            [
            _MetaInfoClassMember('app-type', REFERENCE_ENUM_CLASS, 'IsisApplicationAttribute', 'Isis-application-attribute',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'IsisApplicationAttribute',
                [], [],
                '''                Application Type
                ''',
                'app_type',
                'Cisco-IOS-XR-clns-isis-cfg', True),
            _MetaInfoClassMember('enable', ATTRIBUTE, 'bool', 'boolean',
                None, None,
                [], [],
                '''                If TRUE, advertise application link
                attribute in our LSP
                ''',
                'enable',
                'Cisco-IOS-XR-clns-isis-cfg', False, is_mandatory=True),
            ],
            'Cisco-IOS-XR-clns-isis-cfg',
            'attribute-table',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-clns-isis-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg',
        ),
    },
    'Isis.Instances.Instance.Afs.Af.TopologyName.ApplicationTables.ApplicationTable' : {
        'meta_info' : _MetaInfoClass('Isis.Instances.Instance.Afs.Af.TopologyName.ApplicationTables.ApplicationTable', REFERENCE_LIST,
            '''Application Name''',
            False, 
            [
            _MetaInfoClassMember('app-type', REFERENCE_ENUM_CLASS, 'IsisApplication', 'Isis-application',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'IsisApplication',
                [], [],
                '''                Application Type
                ''',
                'app_type',
                'Cisco-IOS-XR-clns-isis-cfg', True),
            _MetaInfoClassMember('attribute-table', REFERENCE_LIST, 'AttributeTable', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'Isis.Instances.Instance.Afs.Af.TopologyName.ApplicationTables.ApplicationTable.AttributeTable',
                [], [],
                '''                Attribute Name
                ''',
                'attribute_table',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            ],
            'Cisco-IOS-XR-clns-isis-cfg',
            'application-table',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-clns-isis-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg',
        ),
    },
    'Isis.Instances.Instance.Afs.Af.TopologyName.ApplicationTables' : {
        'meta_info' : _MetaInfoClass('Isis.Instances.Instance.Afs.Af.TopologyName.ApplicationTables', REFERENCE_CLASS,
            '''Advertise application specific values''',
            False, 
            [
            _MetaInfoClassMember('application-table', REFERENCE_LIST, 'ApplicationTable', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'Isis.Instances.Instance.Afs.Af.TopologyName.ApplicationTables.ApplicationTable',
                [], [],
                '''                Application Name
                ''',
                'application_table',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            ],
            'Cisco-IOS-XR-clns-isis-cfg',
            'application-tables',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-clns-isis-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg',
        ),
    },
    'Isis.Instances.Instance.Afs.Af.TopologyName.SpfPeriodicIntervals.SpfPeriodicInterval' : {
        'meta_info' : _MetaInfoClass('Isis.Instances.Instance.Afs.Af.TopologyName.SpfPeriodicIntervals.SpfPeriodicInterval', REFERENCE_LIST,
            '''Maximum interval between spf runs''',
            False, 
            [
            _MetaInfoClassMember('level', REFERENCE_ENUM_CLASS, 'IsisInternalLevel', 'dt1:Isis-internal-level',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_datatypes', 'IsisInternalLevel',
                [], [],
                '''                Level to which configuration applies
                ''',
                'level',
                'Cisco-IOS-XR-clns-isis-cfg', True),
            _MetaInfoClassMember('periodic-interval', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('0', '3600')], [],
                '''                Maximum interval in between SPF runs in
                seconds
                ''',
                'periodic_interval',
                'Cisco-IOS-XR-clns-isis-cfg', False, is_mandatory=True),
            ],
            'Cisco-IOS-XR-clns-isis-cfg',
            'spf-periodic-interval',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-clns-isis-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg',
        ),
    },
    'Isis.Instances.Instance.Afs.Af.TopologyName.SpfPeriodicIntervals' : {
        'meta_info' : _MetaInfoClass('Isis.Instances.Instance.Afs.Af.TopologyName.SpfPeriodicIntervals', REFERENCE_CLASS,
            '''Peoridic SPF configuration''',
            False, 
            [
            _MetaInfoClassMember('spf-periodic-interval', REFERENCE_LIST, 'SpfPeriodicInterval', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'Isis.Instances.Instance.Afs.Af.TopologyName.SpfPeriodicIntervals.SpfPeriodicInterval',
                [], [],
                '''                Maximum interval between spf runs
                ''',
                'spf_periodic_interval',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            ],
            'Cisco-IOS-XR-clns-isis-cfg',
            'spf-periodic-intervals',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-clns-isis-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg',
        ),
    },
    'Isis.Instances.Instance.Afs.Af.TopologyName.DistributeListIn' : {
        'meta_info' : _MetaInfoClass('Isis.Instances.Instance.Afs.Af.TopologyName.DistributeListIn', REFERENCE_CLASS,
            '''Filter routes sent to the RIB''',
            False, 
            [
            _MetaInfoClassMember('prefix-list-name', ATTRIBUTE, 'str', 'xr:Cisco-ios-xr-string',
                None, None,
                [(1, 64)], [],
                '''                Prefix list to control routes installed in
                RIB.
                ''',
                'prefix_list_name',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            _MetaInfoClassMember('route-policy-name', ATTRIBUTE, 'str', 'xr:Cisco-ios-xr-string',
                None, None,
                [(1, 64)], [],
                '''                Route policy to control routes installed
                in RIB.
                ''',
                'route_policy_name',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            ],
            'Cisco-IOS-XR-clns-isis-cfg',
            'distribute-list-in',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-clns-isis-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg',
        ),
    },
    'Isis.Instances.Instance.Afs.Af.TopologyName.SpfIntervals.SpfInterval' : {
        'meta_info' : _MetaInfoClass('Isis.Instances.Instance.Afs.Af.TopologyName.SpfIntervals.SpfInterval', REFERENCE_LIST,
            '''Route calculation scheduling parameters''',
            False, 
            [
            _MetaInfoClassMember('level', REFERENCE_ENUM_CLASS, 'IsisInternalLevel', 'dt1:Isis-internal-level',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_datatypes', 'IsisInternalLevel',
                [], [],
                '''                Level to which configuration applies
                ''',
                'level',
                'Cisco-IOS-XR-clns-isis-cfg', True),
            _MetaInfoClassMember('maximum-wait', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('0', '120000')], [],
                '''                Maximum wait before running a route
                calculation in milliseconds
                ''',
                'maximum_wait',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            _MetaInfoClassMember('initial-wait', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('0', '120000')], [],
                '''                Initial wait before running a route
                calculation in milliseconds
                ''',
                'initial_wait',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            _MetaInfoClassMember('secondary-wait', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('0', '120000')], [],
                '''                Secondary wait before running a route
                calculation in milliseconds
                ''',
                'secondary_wait',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            ],
            'Cisco-IOS-XR-clns-isis-cfg',
            'spf-interval',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-clns-isis-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg',
        ),
    },
    'Isis.Instances.Instance.Afs.Af.TopologyName.SpfIntervals' : {
        'meta_info' : _MetaInfoClass('Isis.Instances.Instance.Afs.Af.TopologyName.SpfIntervals', REFERENCE_CLASS,
            '''SPF-interval configuration''',
            False, 
            [
            _MetaInfoClassMember('spf-interval', REFERENCE_LIST, 'SpfInterval', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'Isis.Instances.Instance.Afs.Af.TopologyName.SpfIntervals.SpfInterval',
                [], [],
                '''                Route calculation scheduling parameters
                ''',
                'spf_interval',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            ],
            'Cisco-IOS-XR-clns-isis-cfg',
            'spf-intervals',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-clns-isis-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg',
        ),
    },
    'Isis.Instances.Instance.Afs.Af.TopologyName.MonitorConvergence' : {
        'meta_info' : _MetaInfoClass('Isis.Instances.Instance.Afs.Af.TopologyName.MonitorConvergence', REFERENCE_CLASS,
            '''Enable convergence monitoring''',
            False, 
            [
            _MetaInfoClassMember('enable', ATTRIBUTE, 'Empty', 'empty',
                None, None,
                [], [],
                '''                Enable convergence monitoring
                ''',
                'enable',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            _MetaInfoClassMember('track-ip-frr', ATTRIBUTE, 'Empty', 'empty',
                None, None,
                [], [],
                '''                Enable the Tracking of IP-Frr Convergence
                ''',
                'track_ip_frr',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            _MetaInfoClassMember('prefix-list', ATTRIBUTE, 'str', 'xr:Cisco-ios-xr-string',
                None, None,
                [(1, 32)], [],
                '''                Enable the monitoring of individual
                prefixes (prefix list name)
                ''',
                'prefix_list',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            ],
            'Cisco-IOS-XR-clns-isis-cfg',
            'monitor-convergence',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-clns-isis-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg',
        ),
    },
    'Isis.Instances.Instance.Afs.Af.TopologyName.DefaultInformation' : {
        'meta_info' : _MetaInfoClass('Isis.Instances.Instance.Afs.Af.TopologyName.DefaultInformation', REFERENCE_CLASS,
            '''Control origination of a default route with
the option of using a policy.  If no policy
is specified the default route is
advertised with zero cost in level 2 only.''',
            False, 
            [
            _MetaInfoClassMember('use-policy', ATTRIBUTE, 'bool', 'boolean',
                None, None,
                [], [],
                '''                Flag to indicate whether default
                origination is controlled using a policy
                ''',
                'use_policy',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            _MetaInfoClassMember('policy-name', ATTRIBUTE, 'str', 'xr:Cisco-ios-xr-string',
                None, None,
                [(1, 64)], [],
                '''                Policy name
                ''',
                'policy_name',
                'Cisco-IOS-XR-clns-isis-cfg', False, has_when=True),
            _MetaInfoClassMember('external', ATTRIBUTE, 'Empty', 'empty',
                None, None,
                [], [],
                '''                Flag to indicate that the default prefix
                should be originated as an external route
                ''',
                'external',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            ],
            'Cisco-IOS-XR-clns-isis-cfg',
            'default-information',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-clns-isis-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg',
        ),
    },
    'Isis.Instances.Instance.Afs.Af.TopologyName.AdminDistances.AdminDistance' : {
        'meta_info' : _MetaInfoClass('Isis.Instances.Instance.Afs.Af.TopologyName.AdminDistances.AdminDistance', REFERENCE_LIST,
            '''Administrative distance configuration. The
supplied distance is applied to all routes
discovered from the specified source, or
only those that match the supplied prefix
list if this is specified''',
            False, 
            [
            _MetaInfoClassMember('address-prefix', REFERENCE_UNION, 'str', 'inet:ip-prefix',
                None, None,
                [], [],
                '''                IP route source prefix
                ''',
                'address_prefix',
                'Cisco-IOS-XR-clns-isis-cfg', True, [
                    _MetaInfoClassMember('address-prefix', ATTRIBUTE, 'str', 'inet:ipv4-prefix',
                        None, None,
                        [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])/(([0-9])|([1-2][0-9])|(3[0-2]))'],
                        '''                        IP route source prefix
                        ''',
                        'address_prefix',
                        'Cisco-IOS-XR-clns-isis-cfg', True),
                    _MetaInfoClassMember('address-prefix', ATTRIBUTE, 'str', 'inet:ipv6-prefix',
                        None, None,
                        [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(/(([0-9])|([0-9]{2})|(1[0-1][0-9])|(12[0-8])))'],
                        '''                        IP route source prefix
                        ''',
                        'address_prefix',
                        'Cisco-IOS-XR-clns-isis-cfg', True),
                ]),
            _MetaInfoClassMember('distance', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('1', '255')], [],
                '''                Administrative distance
                ''',
                'distance',
                'Cisco-IOS-XR-clns-isis-cfg', False, is_mandatory=True),
            _MetaInfoClassMember('prefix-list', ATTRIBUTE, 'str', 'string',
                None, None,
                [(1, 32)], [],
                '''                List of prefixes to which this distance
                applies
                ''',
                'prefix_list',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            ],
            'Cisco-IOS-XR-clns-isis-cfg',
            'admin-distance',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-clns-isis-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg',
        ),
    },
    'Isis.Instances.Instance.Afs.Af.TopologyName.AdminDistances' : {
        'meta_info' : _MetaInfoClass('Isis.Instances.Instance.Afs.Af.TopologyName.AdminDistances', REFERENCE_CLASS,
            '''Per-route administrative
distanceconfiguration''',
            False, 
            [
            _MetaInfoClassMember('admin-distance', REFERENCE_LIST, 'AdminDistance', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'Isis.Instances.Instance.Afs.Af.TopologyName.AdminDistances.AdminDistance',
                [], [],
                '''                Administrative distance configuration. The
                supplied distance is applied to all routes
                discovered from the specified source, or
                only those that match the supplied prefix
                list if this is specified
                ''',
                'admin_distance',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            ],
            'Cisco-IOS-XR-clns-isis-cfg',
            'admin-distances',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-clns-isis-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg',
        ),
    },
    'Isis.Instances.Instance.Afs.Af.TopologyName.Ispf.States.State' : {
        'meta_info' : _MetaInfoClass('Isis.Instances.Instance.Afs.Af.TopologyName.Ispf.States.State', REFERENCE_LIST,
            '''Enable/disable ISPF''',
            False, 
            [
            _MetaInfoClassMember('level', REFERENCE_ENUM_CLASS, 'IsisInternalLevel', 'dt1:Isis-internal-level',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_datatypes', 'IsisInternalLevel',
                [], [],
                '''                Level to which configuration applies
                ''',
                'level',
                'Cisco-IOS-XR-clns-isis-cfg', True),
            _MetaInfoClassMember('state', REFERENCE_ENUM_CLASS, 'IsisispfState', 'Isisispf-state',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'IsisispfState',
                [], [],
                '''                State
                ''',
                'state',
                'Cisco-IOS-XR-clns-isis-cfg', False, is_mandatory=True),
            ],
            'Cisco-IOS-XR-clns-isis-cfg',
            'state',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-clns-isis-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg',
        ),
    },
    'Isis.Instances.Instance.Afs.Af.TopologyName.Ispf.States' : {
        'meta_info' : _MetaInfoClass('Isis.Instances.Instance.Afs.Af.TopologyName.Ispf.States', REFERENCE_CLASS,
            '''ISPF state (enable/disable)''',
            False, 
            [
            _MetaInfoClassMember('state', REFERENCE_LIST, 'State', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'Isis.Instances.Instance.Afs.Af.TopologyName.Ispf.States.State',
                [], [],
                '''                Enable/disable ISPF
                ''',
                'state',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            ],
            'Cisco-IOS-XR-clns-isis-cfg',
            'states',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-clns-isis-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg',
        ),
    },
    'Isis.Instances.Instance.Afs.Af.TopologyName.Ispf' : {
        'meta_info' : _MetaInfoClass('Isis.Instances.Instance.Afs.Af.TopologyName.Ispf', REFERENCE_CLASS,
            '''ISPF configuration''',
            False, 
            [
            _MetaInfoClassMember('states', REFERENCE_CLASS, 'States', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'Isis.Instances.Instance.Afs.Af.TopologyName.Ispf.States',
                [], [],
                '''                ISPF state (enable/disable)
                ''',
                'states',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            ],
            'Cisco-IOS-XR-clns-isis-cfg',
            'ispf',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-clns-isis-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg',
        ),
    },
    'Isis.Instances.Instance.Afs.Af.TopologyName.MplsLdpGlobal' : {
        'meta_info' : _MetaInfoClass('Isis.Instances.Instance.Afs.Af.TopologyName.MplsLdpGlobal', REFERENCE_CLASS,
            '''MPLS LDP configuration. MPLS LDP
configuration will only be applied for the
IPv4-unicast address-family.''',
            False, 
            [
            _MetaInfoClassMember('auto-config', ATTRIBUTE, 'bool', 'boolean',
                None, None,
                [], [],
                '''                If TRUE, LDP will be enabled onall IS-IS
                interfaces enabled for this address-family
                ''',
                'auto_config',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            ],
            'Cisco-IOS-XR-clns-isis-cfg',
            'mpls-ldp-global',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-clns-isis-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg',
        ),
    },
    'Isis.Instances.Instance.Afs.Af.TopologyName.Mpls.RouterId' : {
        'meta_info' : _MetaInfoClass('Isis.Instances.Instance.Afs.Af.TopologyName.Mpls.RouterId', REFERENCE_CLASS,
            '''Traffic Engineering stable IP address for
system''',
            False, 
            [
            _MetaInfoClassMember('address', ATTRIBUTE, 'str', 'inet:ipv4-address-no-zone',
                None, None,
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'],
                '''                IPv4 address to be used as a router ID.
                Precisely one of Address and Interface
                must be specified.
                ''',
                'address',
                'Cisco-IOS-XR-clns-isis-cfg', False, has_must=True),
            _MetaInfoClassMember('interface-name', ATTRIBUTE, 'str', 'xr:Interface-name',
                None, None,
                [], [b'[a-zA-Z0-9._/-]+'],
                '''                Interface with designated stable IP
                address to be used as a router ID. This
                must be a Loopback interface. Precisely
                one of Address and Interface must be
                specified.
                ''',
                'interface_name',
                'Cisco-IOS-XR-clns-isis-cfg', False, has_must=True),
            ],
            'Cisco-IOS-XR-clns-isis-cfg',
            'router-id',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-clns-isis-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg',
        ),
    },
    'Isis.Instances.Instance.Afs.Af.TopologyName.Mpls.Level' : {
        'meta_info' : _MetaInfoClass('Isis.Instances.Instance.Afs.Af.TopologyName.Mpls.Level', REFERENCE_CLASS,
            '''Enable MPLS for an IS-IS at the given
levels''',
            False, 
            [
            _MetaInfoClassMember('level1', ATTRIBUTE, 'bool', 'boolean',
                None, None,
                [], [],
                '''                Level 1 enabled
                ''',
                'level1',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            _MetaInfoClassMember('level2', ATTRIBUTE, 'bool', 'boolean',
                None, None,
                [], [],
                '''                Level 2 enabled
                ''',
                'level2',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            ],
            'Cisco-IOS-XR-clns-isis-cfg',
            'level',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-clns-isis-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg',
        ),
    },
    'Isis.Instances.Instance.Afs.Af.TopologyName.Mpls' : {
        'meta_info' : _MetaInfoClass('Isis.Instances.Instance.Afs.Af.TopologyName.Mpls', REFERENCE_CLASS,
            '''MPLS configuration. MPLS configuration will
only be applied for the IPv4-unicast
address-family.''',
            False, 
            [
            _MetaInfoClassMember('router-id', REFERENCE_CLASS, 'RouterId', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'Isis.Instances.Instance.Afs.Af.TopologyName.Mpls.RouterId',
                [], [],
                '''                Traffic Engineering stable IP address for
                system
                ''',
                'router_id',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            _MetaInfoClassMember('level', REFERENCE_CLASS, 'Level', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'Isis.Instances.Instance.Afs.Af.TopologyName.Mpls.Level',
                [], [],
                '''                Enable MPLS for an IS-IS at the given
                levels
                ''',
                'level',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            _MetaInfoClassMember('igp-intact', ATTRIBUTE, 'Empty', 'empty',
                None, None,
                [], [],
                '''                Install TE and non-TE nexthops in the RIB
                ''',
                'igp_intact',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            _MetaInfoClassMember('multicast-intact', ATTRIBUTE, 'Empty', 'empty',
                None, None,
                [], [],
                '''                Install non-TE nexthops in the RIB for use
                by multicast
                ''',
                'multicast_intact',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            ],
            'Cisco-IOS-XR-clns-isis-cfg',
            'mpls',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-clns-isis-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg',
        ),
    },
    'Isis.Instances.Instance.Afs.Af.TopologyName.ManualAdjSids.ManualAdjSid' : {
        'meta_info' : _MetaInfoClass('Isis.Instances.Instance.Afs.Af.TopologyName.ManualAdjSids.ManualAdjSid', REFERENCE_LIST,
            '''Assign adjancency SID to an interface''',
            False, 
            [
            _MetaInfoClassMember('level', REFERENCE_ENUM_CLASS, 'IsisInternalLevel', 'dt1:Isis-internal-level',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_datatypes', 'IsisInternalLevel',
                [], [],
                '''                Level to which configuration applies
                ''',
                'level',
                'Cisco-IOS-XR-clns-isis-cfg', True),
            _MetaInfoClassMember('sid-type', REFERENCE_ENUM_CLASS, 'Isissid1', 'Isissid1',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'Isissid1',
                [], [],
                '''                Sid type aboslute or index
                ''',
                'sid_type',
                'Cisco-IOS-XR-clns-isis-cfg', True),
            _MetaInfoClassMember('sid', ATTRIBUTE, 'int', 'Isissid',
                None, None,
                [('0', '1048575')], [],
                '''                Sid value
                ''',
                'sid',
                'Cisco-IOS-XR-clns-isis-cfg', True),
            _MetaInfoClassMember('protected', REFERENCE_ENUM_CLASS, 'IsissidProtected', 'Isissid-protected',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'IsissidProtected',
                [], [],
                '''                Enable/Disable SID protection
                ''',
                'protected',
                'Cisco-IOS-XR-clns-isis-cfg', False, is_mandatory=True),
            ],
            'Cisco-IOS-XR-clns-isis-cfg',
            'manual-adj-sid',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-clns-isis-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg',
        ),
    },
    'Isis.Instances.Instance.Afs.Af.TopologyName.ManualAdjSids' : {
        'meta_info' : _MetaInfoClass('Isis.Instances.Instance.Afs.Af.TopologyName.ManualAdjSids', REFERENCE_CLASS,
            '''Manual Adjacecy SID configuration''',
            False, 
            [
            _MetaInfoClassMember('manual-adj-sid', REFERENCE_LIST, 'ManualAdjSid', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'Isis.Instances.Instance.Afs.Af.TopologyName.ManualAdjSids.ManualAdjSid',
                [], [],
                '''                Assign adjancency SID to an interface
                ''',
                'manual_adj_sid',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            ],
            'Cisco-IOS-XR-clns-isis-cfg',
            'manual-adj-sids',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-clns-isis-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg',
        ),
    },
    'Isis.Instances.Instance.Afs.Af.TopologyName.Metrics.Metric.Metric_' : _MetaInfoEnum('Metric_',
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'Isis.Instances.Instance.Afs.Af.TopologyName.Metrics.Metric.Metric_',
        ''' ''',
        {
            'maximum':'maximum',
        }, 'Cisco-IOS-XR-clns-isis-cfg', _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-clns-isis-cfg']),
    'Isis.Instances.Instance.Afs.Af.TopologyName.Metrics.Metric' : {
        'meta_info' : _MetaInfoClass('Isis.Instances.Instance.Afs.Af.TopologyName.Metrics.Metric', REFERENCE_LIST,
            '''Metric configuration. Legal value depends on
the metric-style specified for the topology. If
the metric-style defined is narrow, then only a
value between <1-63> is allowed and if the
metric-style is defined as wide, then a value
between <1-16777215> is allowed as the metric
value.  All routers exclude links with the
maximum wide metric (16777215) from their SPF''',
            False, 
            [
            _MetaInfoClassMember('level', REFERENCE_ENUM_CLASS, 'IsisInternalLevel', 'dt1:Isis-internal-level',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_datatypes', 'IsisInternalLevel',
                [], [],
                '''                Level to which configuration applies
                ''',
                'level',
                'Cisco-IOS-XR-clns-isis-cfg', True),
            _MetaInfoClassMember('metric', REFERENCE_UNION, 'str', 'union',
                None, None,
                [], [],
                '''                Allowed metric: <1-63> for narrow,
                <1-16777215> for wide
                ''',
                'metric',
                'Cisco-IOS-XR-clns-isis-cfg', False, [
                    _MetaInfoClassMember('metric', REFERENCE_ENUM_CLASS, 'Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.TopologyName.Metrics.Metric.Metric_', 'enumeration',
                        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.TopologyName.Metrics.Metric.Metric_',
                        [], [],
                        '''                        Allowed metric: <1-63> for narrow,
                        <1-16777215> for wide
                        ''',
                        'metric',
                        'Cisco-IOS-XR-clns-isis-cfg', False, is_mandatory=True),
                    _MetaInfoClassMember('metric', ATTRIBUTE, 'int', 'uint32',
                        None, None,
                        [('1', '16777215')], [],
                        '''                        Allowed metric: <1-63> for narrow,
                        <1-16777215> for wide
                        ''',
                        'metric',
                        'Cisco-IOS-XR-clns-isis-cfg', False, is_mandatory=True),
                ], is_mandatory=True),
            ],
            'Cisco-IOS-XR-clns-isis-cfg',
            'metric',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-clns-isis-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg',
        ),
    },
    'Isis.Instances.Instance.Afs.Af.TopologyName.Metrics' : {
        'meta_info' : _MetaInfoClass('Isis.Instances.Instance.Afs.Af.TopologyName.Metrics', REFERENCE_CLASS,
            '''Metric configuration''',
            False, 
            [
            _MetaInfoClassMember('metric', REFERENCE_LIST, 'Metric', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'Isis.Instances.Instance.Afs.Af.TopologyName.Metrics.Metric',
                [], [],
                '''                Metric configuration. Legal value depends on
                the metric-style specified for the topology. If
                the metric-style defined is narrow, then only a
                value between <1-63> is allowed and if the
                metric-style is defined as wide, then a value
                between <1-16777215> is allowed as the metric
                value.  All routers exclude links with the
                maximum wide metric (16777215) from their SPF
                ''',
                'metric',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            ],
            'Cisco-IOS-XR-clns-isis-cfg',
            'metrics',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-clns-isis-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg',
        ),
    },
    'Isis.Instances.Instance.Afs.Af.TopologyName.Weights.Weight' : {
        'meta_info' : _MetaInfoClass('Isis.Instances.Instance.Afs.Af.TopologyName.Weights.Weight', REFERENCE_LIST,
            '''Weight configuration under interface for load
balancing''',
            False, 
            [
            _MetaInfoClassMember('level', REFERENCE_ENUM_CLASS, 'IsisInternalLevel', 'dt1:Isis-internal-level',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_datatypes', 'IsisInternalLevel',
                [], [],
                '''                Level to which configuration applies
                ''',
                'level',
                'Cisco-IOS-XR-clns-isis-cfg', True),
            _MetaInfoClassMember('weight', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('1', '16777214')], [],
                '''                Weight to be configured under interface for
                Load Balancing. Allowed weight: <1-16777215>
                ''',
                'weight',
                'Cisco-IOS-XR-clns-isis-cfg', False, is_mandatory=True),
            ],
            'Cisco-IOS-XR-clns-isis-cfg',
            'weight',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-clns-isis-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg',
        ),
    },
    'Isis.Instances.Instance.Afs.Af.TopologyName.Weights' : {
        'meta_info' : _MetaInfoClass('Isis.Instances.Instance.Afs.Af.TopologyName.Weights', REFERENCE_CLASS,
            '''Weight configuration''',
            False, 
            [
            _MetaInfoClassMember('weight', REFERENCE_LIST, 'Weight', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'Isis.Instances.Instance.Afs.Af.TopologyName.Weights.Weight',
                [], [],
                '''                Weight configuration under interface for load
                balancing
                ''',
                'weight',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            ],
            'Cisco-IOS-XR-clns-isis-cfg',
            'weights',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-clns-isis-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg',
        ),
    },
    'Isis.Instances.Instance.Afs.Af.TopologyName' : {
        'meta_info' : _MetaInfoClass('Isis.Instances.Instance.Afs.Af.TopologyName', REFERENCE_LIST,
            '''keys: topology-name''',
            False, 
            [
            _MetaInfoClassMember('topology-name', ATTRIBUTE, 'str', 'dt1:Isis-topology-name',
                None, None,
                [(1, 32)], [],
                '''                Topology Name
                ''',
                'topology_name',
                'Cisco-IOS-XR-clns-isis-cfg', True),
            _MetaInfoClassMember('segment-routing', REFERENCE_CLASS, 'SegmentRouting', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'Isis.Instances.Instance.Afs.Af.TopologyName.SegmentRouting',
                [], [],
                '''                Enable Segment Routing configuration
                ''',
                'segment_routing',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            _MetaInfoClassMember('metric-styles', REFERENCE_CLASS, 'MetricStyles', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'Isis.Instances.Instance.Afs.Af.TopologyName.MetricStyles',
                [], [],
                '''                Metric-style configuration
                ''',
                'metric_styles',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            _MetaInfoClassMember('frr-table', REFERENCE_CLASS, 'FrrTable', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'Isis.Instances.Instance.Afs.Af.TopologyName.FrrTable',
                [], [],
                '''                Fast-ReRoute configuration
                ''',
                'frr_table',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            _MetaInfoClassMember('router-id', REFERENCE_CLASS, 'RouterId', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'Isis.Instances.Instance.Afs.Af.TopologyName.RouterId',
                [], [],
                '''                Stable IP address for system. Will only be
                applied for the unicast sub-address-family.
                ''',
                'router_id',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            _MetaInfoClassMember('spf-prefix-priorities', REFERENCE_CLASS, 'SpfPrefixPriorities', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'Isis.Instances.Instance.Afs.Af.TopologyName.SpfPrefixPriorities',
                [], [],
                '''                SPF Prefix Priority configuration
                ''',
                'spf_prefix_priorities',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            _MetaInfoClassMember('summary-prefixes', REFERENCE_CLASS, 'SummaryPrefixes', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'Isis.Instances.Instance.Afs.Af.TopologyName.SummaryPrefixes',
                [], [],
                '''                Summary-prefix configuration
                ''',
                'summary_prefixes',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            _MetaInfoClassMember('micro-loop-avoidance', REFERENCE_CLASS, 'MicroLoopAvoidance', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'Isis.Instances.Instance.Afs.Af.TopologyName.MicroLoopAvoidance',
                [], [],
                '''                Micro Loop Avoidance configuration
                ''',
                'micro_loop_avoidance',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            _MetaInfoClassMember('ucmp', REFERENCE_CLASS, 'Ucmp', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'Isis.Instances.Instance.Afs.Af.TopologyName.Ucmp',
                [], [],
                '''                UCMP (UnEqual Cost MultiPath) configuration
                ''',
                'ucmp',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            _MetaInfoClassMember('max-redist-prefixes', REFERENCE_CLASS, 'MaxRedistPrefixes', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'Isis.Instances.Instance.Afs.Af.TopologyName.MaxRedistPrefixes',
                [], [],
                '''                Maximum number of redistributed
                prefixesconfiguration
                ''',
                'max_redist_prefixes',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            _MetaInfoClassMember('propagations', REFERENCE_CLASS, 'Propagations', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'Isis.Instances.Instance.Afs.Af.TopologyName.Propagations',
                [], [],
                '''                Route propagation configuration
                ''',
                'propagations',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            _MetaInfoClassMember('redistributions', REFERENCE_CLASS, 'Redistributions', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'Isis.Instances.Instance.Afs.Af.TopologyName.Redistributions',
                [], [],
                '''                Protocol redistribution configuration
                ''',
                'redistributions',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            _MetaInfoClassMember('application-tables', REFERENCE_CLASS, 'ApplicationTables', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'Isis.Instances.Instance.Afs.Af.TopologyName.ApplicationTables',
                [], [],
                '''                Advertise application specific values
                ''',
                'application_tables',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            _MetaInfoClassMember('spf-periodic-intervals', REFERENCE_CLASS, 'SpfPeriodicIntervals', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'Isis.Instances.Instance.Afs.Af.TopologyName.SpfPeriodicIntervals',
                [], [],
                '''                Peoridic SPF configuration
                ''',
                'spf_periodic_intervals',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            _MetaInfoClassMember('distribute-list-in', REFERENCE_CLASS, 'DistributeListIn', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'Isis.Instances.Instance.Afs.Af.TopologyName.DistributeListIn',
                [], [],
                '''                Filter routes sent to the RIB
                ''',
                'distribute_list_in',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            _MetaInfoClassMember('spf-intervals', REFERENCE_CLASS, 'SpfIntervals', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'Isis.Instances.Instance.Afs.Af.TopologyName.SpfIntervals',
                [], [],
                '''                SPF-interval configuration
                ''',
                'spf_intervals',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            _MetaInfoClassMember('monitor-convergence', REFERENCE_CLASS, 'MonitorConvergence', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'Isis.Instances.Instance.Afs.Af.TopologyName.MonitorConvergence',
                [], [],
                '''                Enable convergence monitoring
                ''',
                'monitor_convergence',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            _MetaInfoClassMember('default-information', REFERENCE_CLASS, 'DefaultInformation', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'Isis.Instances.Instance.Afs.Af.TopologyName.DefaultInformation',
                [], [],
                '''                Control origination of a default route with
                the option of using a policy.  If no policy
                is specified the default route is
                advertised with zero cost in level 2 only.
                ''',
                'default_information',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            _MetaInfoClassMember('admin-distances', REFERENCE_CLASS, 'AdminDistances', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'Isis.Instances.Instance.Afs.Af.TopologyName.AdminDistances',
                [], [],
                '''                Per-route administrative
                distanceconfiguration
                ''',
                'admin_distances',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            _MetaInfoClassMember('ispf', REFERENCE_CLASS, 'Ispf', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'Isis.Instances.Instance.Afs.Af.TopologyName.Ispf',
                [], [],
                '''                ISPF configuration
                ''',
                'ispf',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            _MetaInfoClassMember('mpls-ldp-global', REFERENCE_CLASS, 'MplsLdpGlobal', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'Isis.Instances.Instance.Afs.Af.TopologyName.MplsLdpGlobal',
                [], [],
                '''                MPLS LDP configuration. MPLS LDP
                configuration will only be applied for the
                IPv4-unicast address-family.
                ''',
                'mpls_ldp_global',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            _MetaInfoClassMember('mpls', REFERENCE_CLASS, 'Mpls', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'Isis.Instances.Instance.Afs.Af.TopologyName.Mpls',
                [], [],
                '''                MPLS configuration. MPLS configuration will
                only be applied for the IPv4-unicast
                address-family.
                ''',
                'mpls',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            _MetaInfoClassMember('maximum-paths', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('1', '64')], [],
                '''                Maximum number of active parallel paths per
                route
                ''',
                'maximum_paths',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            _MetaInfoClassMember('topology-id', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('6', '4095')], [],
                '''                Set the topology ID for a named
                (non-default) topology. This object must be
                set before any other configuration is
                supplied for a named (non-default) topology
                , and must be the last configuration object
                to be removed. This item should not be
                supplied for the non-named default
                topologies.
                ''',
                'topology_id',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            _MetaInfoClassMember('single-topology', ATTRIBUTE, 'Empty', 'empty',
                None, None,
                [], [],
                '''                Run IPv6 Unicast using the standard (IPv4
                Unicast) topology
                ''',
                'single_topology',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            _MetaInfoClassMember('adjacency-check', REFERENCE_ENUM_CLASS, 'IsisAdjCheck', 'Isis-adj-check',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'IsisAdjCheck',
                [], [],
                '''                Suppress check for consistent AF support on
                received IIHs
                ''',
                'adjacency_check',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            _MetaInfoClassMember('advertise-link-attributes', ATTRIBUTE, 'bool', 'boolean',
                None, None,
                [], [],
                '''                If TRUE, advertise additional link
                attributes in our LSP
                ''',
                'advertise_link_attributes',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            _MetaInfoClassMember('apply-weight', REFERENCE_ENUM_CLASS, 'IsisApplyWeight', 'Isis-apply-weight',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'IsisApplyWeight',
                [], [],
                '''                Apply weights to UCMP or ECMP only
                ''',
                'apply_weight',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            _MetaInfoClassMember('default-admin-distance', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('1', '255')], [],
                '''                Default IS-IS administrative distance
                configuration.
                ''',
                'default_admin_distance',
                'Cisco-IOS-XR-clns-isis-cfg', False, default_value="115"),
            _MetaInfoClassMember('advertise-passive-only', ATTRIBUTE, 'Empty', 'empty',
                None, None,
                [], [],
                '''                If enabled, advertise prefixes of passive
                interfaces only
                ''',
                'advertise_passive_only',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            _MetaInfoClassMember('ignore-attached-bit', ATTRIBUTE, 'bool', 'boolean',
                None, None,
                [], [],
                '''                If TRUE, Ignore other routers attached bit
                ''',
                'ignore_attached_bit',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            _MetaInfoClassMember('attached-bit', REFERENCE_ENUM_CLASS, 'IsisAttachedBit', 'Isis-attached-bit',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'IsisAttachedBit',
                [], [],
                '''                Set the attached bit in this router's level
                1 System LSP
                ''',
                'attached_bit',
                'Cisco-IOS-XR-clns-isis-cfg', False, default_value='Cisco_IOS_XR_clns_isis_cfg.IsisAttachedBit.area'),
            _MetaInfoClassMember('route-source-first-hop', ATTRIBUTE, 'bool', 'boolean',
                None, None,
                [], [],
                '''                If TRUE, routes will be installed with the
                IP address of the first-hop node as the
                source instead of the originating node
                ''',
                'route_source_first_hop',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            _MetaInfoClassMember('manual-adj-sids', REFERENCE_CLASS, 'ManualAdjSids', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'Isis.Instances.Instance.Afs.Af.TopologyName.ManualAdjSids',
                [], [],
                '''                Manual Adjacecy SID configuration
                ''',
                'manual_adj_sids',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            _MetaInfoClassMember('metrics', REFERENCE_CLASS, 'Metrics', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'Isis.Instances.Instance.Afs.Af.TopologyName.Metrics',
                [], [],
                '''                Metric configuration
                ''',
                'metrics',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            _MetaInfoClassMember('weights', REFERENCE_CLASS, 'Weights', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'Isis.Instances.Instance.Afs.Af.TopologyName.Weights',
                [], [],
                '''                Weight configuration
                ''',
                'weights',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            ],
            'Cisco-IOS-XR-clns-isis-cfg',
            'topology-name',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-clns-isis-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg',
        ),
    },
    'Isis.Instances.Instance.Afs.Af' : {
        'meta_info' : _MetaInfoClass('Isis.Instances.Instance.Afs.Af', REFERENCE_LIST,
            '''Configuration for an IS-IS address-family. If
a named (non-default) topology is being
created it must be multicast.''',
            False, 
            [
            _MetaInfoClassMember('af-name', REFERENCE_ENUM_CLASS, 'IsisAddressFamily', 'dt1:Isis-address-family',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_datatypes', 'IsisAddressFamily',
                [], [],
                '''                Address family
                ''',
                'af_name',
                'Cisco-IOS-XR-clns-isis-cfg', True),
            _MetaInfoClassMember('saf-name', REFERENCE_ENUM_CLASS, 'IsisSubAddressFamily', 'dt1:Isis-sub-address-family',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_datatypes', 'IsisSubAddressFamily',
                [], [],
                '''                Sub address family
                ''',
                'saf_name',
                'Cisco-IOS-XR-clns-isis-cfg', True),
            _MetaInfoClassMember('af-data', REFERENCE_CLASS, 'AfData', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'Isis.Instances.Instance.Afs.Af.AfData',
                [], [],
                '''                Data container.
                ''',
                'af_data',
                'Cisco-IOS-XR-clns-isis-cfg', False, is_presence=True),
            _MetaInfoClassMember('topology-name', REFERENCE_LIST, 'TopologyName', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'Isis.Instances.Instance.Afs.Af.TopologyName',
                [], [],
                '''                keys: topology-name
                ''',
                'topology_name',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            ],
            'Cisco-IOS-XR-clns-isis-cfg',
            'af',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-clns-isis-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg',
        ),
    },
    'Isis.Instances.Instance.Afs' : {
        'meta_info' : _MetaInfoClass('Isis.Instances.Instance.Afs', REFERENCE_CLASS,
            '''Per-address-family configuration''',
            False, 
            [
            _MetaInfoClassMember('af', REFERENCE_LIST, 'Af', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'Isis.Instances.Instance.Afs.Af',
                [], [],
                '''                Configuration for an IS-IS address-family. If
                a named (non-default) topology is being
                created it must be multicast.
                ''',
                'af',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            ],
            'Cisco-IOS-XR-clns-isis-cfg',
            'afs',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-clns-isis-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg',
        ),
    },
    'Isis.Instances.Instance.LspRefreshIntervals.LspRefreshInterval' : {
        'meta_info' : _MetaInfoClass('Isis.Instances.Instance.LspRefreshIntervals.LspRefreshInterval', REFERENCE_LIST,
            '''Interval between re-flooding of unchanged
LSPs''',
            False, 
            [
            _MetaInfoClassMember('level', REFERENCE_ENUM_CLASS, 'IsisInternalLevel', 'dt1:Isis-internal-level',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_datatypes', 'IsisInternalLevel',
                [], [],
                '''                Level to which configuration applies
                ''',
                'level',
                'Cisco-IOS-XR-clns-isis-cfg', True),
            _MetaInfoClassMember('interval', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('1', '65535')], [],
                '''                Seconds
                ''',
                'interval',
                'Cisco-IOS-XR-clns-isis-cfg', False, is_mandatory=True),
            ],
            'Cisco-IOS-XR-clns-isis-cfg',
            'lsp-refresh-interval',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-clns-isis-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg',
        ),
    },
    'Isis.Instances.Instance.LspRefreshIntervals' : {
        'meta_info' : _MetaInfoClass('Isis.Instances.Instance.LspRefreshIntervals', REFERENCE_CLASS,
            '''LSP refresh-interval configuration''',
            False, 
            [
            _MetaInfoClassMember('lsp-refresh-interval', REFERENCE_LIST, 'LspRefreshInterval', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'Isis.Instances.Instance.LspRefreshIntervals.LspRefreshInterval',
                [], [],
                '''                Interval between re-flooding of unchanged
                LSPs
                ''',
                'lsp_refresh_interval',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            ],
            'Cisco-IOS-XR-clns-isis-cfg',
            'lsp-refresh-intervals',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-clns-isis-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg',
        ),
    },
    'Isis.Instances.Instance.Distribute' : {
        'meta_info' : _MetaInfoClass('Isis.Instances.Instance.Distribute', REFERENCE_CLASS,
            '''Distribute link-state configuration''',
            False, 
            [
            _MetaInfoClassMember('dist-inst-id', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('32', '4294967295')], [],
                '''                Instance ID
                ''',
                'dist_inst_id',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            _MetaInfoClassMember('level', REFERENCE_ENUM_CLASS, 'IsisConfigurableLevels', 'Isis-configurable-levels',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'IsisConfigurableLevels',
                [], [],
                '''                Level
                ''',
                'level',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            _MetaInfoClassMember('dist-throttle', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('1', '20')], [],
                '''                Seconds
                ''',
                'dist_throttle',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            ],
            'Cisco-IOS-XR-clns-isis-cfg',
            'distribute',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-clns-isis-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg',
            is_presence=True,
        ),
    },
    'Isis.Instances.Instance.FlexAlgos.FlexAlgo.AffinityExcludeAnies' : {
        'meta_info' : _MetaInfoClass('Isis.Instances.Instance.FlexAlgos.FlexAlgo.AffinityExcludeAnies', REFERENCE_CLASS,
            '''Set the exclude-any affinity''',
            False, 
            [
            _MetaInfoClassMember('affinity-exclude-any', REFERENCE_LEAFLIST, 'str', 'string',
                None, None,
                [], [],
                '''                Array of Attribute Names
                ''',
                'affinity_exclude_any',
                'Cisco-IOS-XR-clns-isis-cfg', False, max_elements=32),
            ],
            'Cisco-IOS-XR-clns-isis-cfg',
            'affinity-exclude-anies',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-clns-isis-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg',
        ),
    },
    'Isis.Instances.Instance.FlexAlgos.FlexAlgo' : {
        'meta_info' : _MetaInfoClass('Isis.Instances.Instance.FlexAlgos.FlexAlgo', REFERENCE_LIST,
            '''Configuration for an IS-IS Flex-Algo''',
            False, 
            [
            _MetaInfoClassMember('flex-algo', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('128', '255')], [],
                '''                Flex Algo
                ''',
                'flex_algo',
                'Cisco-IOS-XR-clns-isis-cfg', True),
            _MetaInfoClassMember('affinity-exclude-anies', REFERENCE_CLASS, 'AffinityExcludeAnies', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'Isis.Instances.Instance.FlexAlgos.FlexAlgo.AffinityExcludeAnies',
                [], [],
                '''                Set the exclude-any affinity
                ''',
                'affinity_exclude_anies',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            _MetaInfoClassMember('running', ATTRIBUTE, 'Empty', 'empty',
                None, None,
                [], [],
                '''                This object must be set before any other
                configuration is supplied for an interface,
                and must be the last per-interface
                configuration object to be removed.
                ''',
                'running',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            _MetaInfoClassMember('metric-type', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('1', '1')], [],
                '''                Set the Flex-Algo metric-type
                ''',
                'metric_type',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            _MetaInfoClassMember('priority', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('0', '255')], [],
                '''                Set the Flex-Algo priority
                ''',
                'priority',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            _MetaInfoClassMember('frr-disable', ATTRIBUTE, 'bool', 'boolean',
                None, None,
                [], [],
                '''                If TRUE, FRR protectinn is disabled for the
                Flex-Algo.
                ''',
                'frr_disable',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            _MetaInfoClassMember('advertise-definition', ATTRIBUTE, 'bool', 'boolean',
                None, None,
                [], [],
                '''                If TRUE, Flex-Algo definition is advertised
                ''',
                'advertise_definition',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            ],
            'Cisco-IOS-XR-clns-isis-cfg',
            'flex-algo',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-clns-isis-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg',
        ),
    },
    'Isis.Instances.Instance.FlexAlgos' : {
        'meta_info' : _MetaInfoClass('Isis.Instances.Instance.FlexAlgos', REFERENCE_CLASS,
            '''Flex-Algo Table''',
            False, 
            [
            _MetaInfoClassMember('flex-algo', REFERENCE_LIST, 'FlexAlgo', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'Isis.Instances.Instance.FlexAlgos.FlexAlgo',
                [], [],
                '''                Configuration for an IS-IS Flex-Algo
                ''',
                'flex_algo',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            ],
            'Cisco-IOS-XR-clns-isis-cfg',
            'flex-algos',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-clns-isis-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg',
        ),
    },
    'Isis.Instances.Instance.AffinityMappings.AffinityMapping' : {
        'meta_info' : _MetaInfoClass('Isis.Instances.Instance.AffinityMappings.AffinityMapping', REFERENCE_LIST,
            '''Affinity Mapping configuration''',
            False, 
            [
            _MetaInfoClassMember('affinity-name', ATTRIBUTE, 'str', 'xr:Cisco-ios-xr-string',
                None, None,
                [(1, 32)], [],
                '''                Affinity Name
                ''',
                'affinity_name',
                'Cisco-IOS-XR-clns-isis-cfg', True),
            _MetaInfoClassMember('value', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('0', '255')], [],
                '''                Bit position
                ''',
                'value',
                'Cisco-IOS-XR-clns-isis-cfg', False, is_mandatory=True),
            ],
            'Cisco-IOS-XR-clns-isis-cfg',
            'affinity-mapping',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-clns-isis-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg',
        ),
    },
    'Isis.Instances.Instance.AffinityMappings' : {
        'meta_info' : _MetaInfoClass('Isis.Instances.Instance.AffinityMappings', REFERENCE_CLASS,
            '''Affinity Mapping Table''',
            False, 
            [
            _MetaInfoClassMember('affinity-mapping', REFERENCE_LIST, 'AffinityMapping', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'Isis.Instances.Instance.AffinityMappings.AffinityMapping',
                [], [],
                '''                Affinity Mapping configuration
                ''',
                'affinity_mapping',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            ],
            'Cisco-IOS-XR-clns-isis-cfg',
            'affinity-mappings',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-clns-isis-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg',
        ),
    },
    'Isis.Instances.Instance.LspAcceptPasswords.LspAcceptPassword' : {
        'meta_info' : _MetaInfoClass('Isis.Instances.Instance.LspAcceptPasswords.LspAcceptPassword', REFERENCE_LIST,
            '''LSP/SNP accept passwords. This requires the
existence of an LSPPassword of the same level
.''',
            False, 
            [
            _MetaInfoClassMember('level', REFERENCE_ENUM_CLASS, 'IsisInternalLevel', 'dt1:Isis-internal-level',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_datatypes', 'IsisInternalLevel',
                [], [],
                '''                Level to which configuration applies
                ''',
                'level',
                'Cisco-IOS-XR-clns-isis-cfg', True),
            _MetaInfoClassMember('password', ATTRIBUTE, 'str', 'xr:Proprietary-password',
                None, None,
                [], [b'(!.+)|([^!].+)'],
                '''                Password
                ''',
                'password',
                'Cisco-IOS-XR-clns-isis-cfg', False, is_mandatory=True),
            ],
            'Cisco-IOS-XR-clns-isis-cfg',
            'lsp-accept-password',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-clns-isis-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg',
        ),
    },
    'Isis.Instances.Instance.LspAcceptPasswords' : {
        'meta_info' : _MetaInfoClass('Isis.Instances.Instance.LspAcceptPasswords', REFERENCE_CLASS,
            '''LSP/SNP accept password configuration''',
            False, 
            [
            _MetaInfoClassMember('lsp-accept-password', REFERENCE_LIST, 'LspAcceptPassword', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'Isis.Instances.Instance.LspAcceptPasswords.LspAcceptPassword',
                [], [],
                '''                LSP/SNP accept passwords. This requires the
                existence of an LSPPassword of the same level
                .
                ''',
                'lsp_accept_password',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            ],
            'Cisco-IOS-XR-clns-isis-cfg',
            'lsp-accept-passwords',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-clns-isis-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg',
        ),
    },
    'Isis.Instances.Instance.LspMtus.LspMtu' : {
        'meta_info' : _MetaInfoClass('Isis.Instances.Instance.LspMtus.LspMtu', REFERENCE_LIST,
            '''LSP MTU''',
            False, 
            [
            _MetaInfoClassMember('level', REFERENCE_ENUM_CLASS, 'IsisInternalLevel', 'dt1:Isis-internal-level',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_datatypes', 'IsisInternalLevel',
                [], [],
                '''                Level to which configuration applies
                ''',
                'level',
                'Cisco-IOS-XR-clns-isis-cfg', True),
            _MetaInfoClassMember('mtu', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('128', '8979')], [],
                '''                Bytes
                ''',
                'mtu',
                'Cisco-IOS-XR-clns-isis-cfg', False, is_mandatory=True),
            ],
            'Cisco-IOS-XR-clns-isis-cfg',
            'lsp-mtu',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-clns-isis-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg',
        ),
    },
    'Isis.Instances.Instance.LspMtus' : {
        'meta_info' : _MetaInfoClass('Isis.Instances.Instance.LspMtus', REFERENCE_CLASS,
            '''LSP MTU configuration''',
            False, 
            [
            _MetaInfoClassMember('lsp-mtu', REFERENCE_LIST, 'LspMtu', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'Isis.Instances.Instance.LspMtus.LspMtu',
                [], [],
                '''                LSP MTU
                ''',
                'lsp_mtu',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            ],
            'Cisco-IOS-XR-clns-isis-cfg',
            'lsp-mtus',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-clns-isis-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg',
        ),
    },
    'Isis.Instances.Instance.SrlgTable.SrlgNames.SrlgName.FromTos.FromTo' : {
        'meta_info' : _MetaInfoClass('Isis.Instances.Instance.SrlgTable.SrlgNames.SrlgName.FromTos.FromTo', REFERENCE_LIST,
            '''Local and remote addresses of a link''',
            False, 
            [
            _MetaInfoClassMember('local-ipv4-address', ATTRIBUTE, 'str', 'inet:ipv4-address-no-zone',
                None, None,
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'],
                '''                Local IPv4 address
                ''',
                'local_ipv4_address',
                'Cisco-IOS-XR-clns-isis-cfg', True),
            _MetaInfoClassMember('remote-ipv4-address', ATTRIBUTE, 'str', 'inet:ipv4-address-no-zone',
                None, None,
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'],
                '''                Remote IPv4 address
                ''',
                'remote_ipv4_address',
                'Cisco-IOS-XR-clns-isis-cfg', True),
            ],
            'Cisco-IOS-XR-clns-isis-cfg',
            'from-to',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-clns-isis-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg',
        ),
    },
    'Isis.Instances.Instance.SrlgTable.SrlgNames.SrlgName.FromTos' : {
        'meta_info' : _MetaInfoClass('Isis.Instances.Instance.SrlgTable.SrlgNames.SrlgName.FromTos', REFERENCE_CLASS,
            '''Configure Static Remote SRLG''',
            False, 
            [
            _MetaInfoClassMember('from-to', REFERENCE_LIST, 'FromTo', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'Isis.Instances.Instance.SrlgTable.SrlgNames.SrlgName.FromTos.FromTo',
                [], [],
                '''                Local and remote addresses of a link
                ''',
                'from_to',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            ],
            'Cisco-IOS-XR-clns-isis-cfg',
            'from-tos',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-clns-isis-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg',
        ),
    },
    'Isis.Instances.Instance.SrlgTable.SrlgNames.SrlgName' : {
        'meta_info' : _MetaInfoClass('Isis.Instances.Instance.SrlgTable.SrlgNames.SrlgName', REFERENCE_LIST,
            '''Configuration for an IS-IS SRLG''',
            False, 
            [
            _MetaInfoClassMember('srlg-name', ATTRIBUTE, 'str', 'xr:Cisco-ios-xr-string',
                None, None,
                [(1, 64)], [],
                '''                Srlg name
                ''',
                'srlg_name',
                'Cisco-IOS-XR-clns-isis-cfg', True),
            _MetaInfoClassMember('from-tos', REFERENCE_CLASS, 'FromTos', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'Isis.Instances.Instance.SrlgTable.SrlgNames.SrlgName.FromTos',
                [], [],
                '''                Configure Static Remote SRLG
                ''',
                'from_tos',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            _MetaInfoClassMember('admin-weight', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('0', '16777215')], [],
                '''                Configure SRLG Admin Weight
                ''',
                'admin_weight',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            ],
            'Cisco-IOS-XR-clns-isis-cfg',
            'srlg-name',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-clns-isis-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg',
        ),
    },
    'Isis.Instances.Instance.SrlgTable.SrlgNames' : {
        'meta_info' : _MetaInfoClass('Isis.Instances.Instance.SrlgTable.SrlgNames', REFERENCE_CLASS,
            '''SRLG named configuration''',
            False, 
            [
            _MetaInfoClassMember('srlg-name', REFERENCE_LIST, 'SrlgName', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'Isis.Instances.Instance.SrlgTable.SrlgNames.SrlgName',
                [], [],
                '''                Configuration for an IS-IS SRLG
                ''',
                'srlg_name',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            ],
            'Cisco-IOS-XR-clns-isis-cfg',
            'srlg-names',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-clns-isis-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg',
        ),
    },
    'Isis.Instances.Instance.SrlgTable' : {
        'meta_info' : _MetaInfoClass('Isis.Instances.Instance.SrlgTable', REFERENCE_CLASS,
            '''SRLG configuration''',
            False, 
            [
            _MetaInfoClassMember('srlg-names', REFERENCE_CLASS, 'SrlgNames', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'Isis.Instances.Instance.SrlgTable.SrlgNames',
                [], [],
                '''                SRLG named configuration
                ''',
                'srlg_names',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            _MetaInfoClassMember('srlg-admin-weight-default', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('0', '16777215')], [],
                '''                Configure Default SRLG Admin Weight
                ''',
                'srlg_admin_weight_default',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            ],
            'Cisco-IOS-XR-clns-isis-cfg',
            'srlg-table',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-clns-isis-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg',
        ),
    },
    'Isis.Instances.Instance.Nsf' : {
        'meta_info' : _MetaInfoClass('Isis.Instances.Instance.Nsf', REFERENCE_CLASS,
            '''IS-IS NSF configuration''',
            False, 
            [
            _MetaInfoClassMember('flavor', REFERENCE_ENUM_CLASS, 'IsisNsfFlavor', 'Isis-nsf-flavor',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'IsisNsfFlavor',
                [], [],
                '''                NSF not configured if item is deleted
                ''',
                'flavor',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            _MetaInfoClassMember('interface-timer', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('1', '20')], [],
                '''                Per-interface time period to wait for a
                restart ACK during an IETF-NSF restart. This
                configuration has no effect if IETF-NSF is
                not configured
                ''',
                'interface_timer',
                'Cisco-IOS-XR-clns-isis-cfg', False, default_value="1"),
            _MetaInfoClassMember('max-interface-timer-expiry', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('1', '10')], [],
                '''                Maximum number of times an interface timer
                may expire during an IETF-NSF restart before
                the NSF restart is aborted. This
                configuration has no effect if IETF NSF is
                not configured.
                ''',
                'max_interface_timer_expiry',
                'Cisco-IOS-XR-clns-isis-cfg', False, default_value="10"),
            _MetaInfoClassMember('lifetime', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('5', '300')], [],
                '''                Maximum route lifetime following restart.
                When this lifetime expires, old routes will
                be purged from the RIB.
                ''',
                'lifetime',
                'Cisco-IOS-XR-clns-isis-cfg', False, default_value="90"),
            ],
            'Cisco-IOS-XR-clns-isis-cfg',
            'nsf',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-clns-isis-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg',
        ),
    },
    'Isis.Instances.Instance.LinkGroups.LinkGroup' : {
        'meta_info' : _MetaInfoClass('Isis.Instances.Instance.LinkGroups.LinkGroup', REFERENCE_LIST,
            '''Configuration for link group name''',
            False, 
            [
            _MetaInfoClassMember('link-group-name', ATTRIBUTE, 'str', 'dt1:Isis-link-group-name',
                None, None,
                [(1, 40)], [],
                '''                Link Group Name
                ''',
                'link_group_name',
                'Cisco-IOS-XR-clns-isis-cfg', True),
            _MetaInfoClassMember('metric-offset', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('0', '16777215')], [],
                '''                Metric for redistributed routes: <0-63> for
                narrow, <0-16777215> for wide
                ''',
                'metric_offset',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            _MetaInfoClassMember('revert-members', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('2', '64')], [],
                '''                Revert Members
                ''',
                'revert_members',
                'Cisco-IOS-XR-clns-isis-cfg', False, default_value="2"),
            _MetaInfoClassMember('minimum-members', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('2', '64')], [],
                '''                Minimum Members
                ''',
                'minimum_members',
                'Cisco-IOS-XR-clns-isis-cfg', False, default_value="2"),
            ],
            'Cisco-IOS-XR-clns-isis-cfg',
            'link-group',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-clns-isis-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg',
        ),
    },
    'Isis.Instances.Instance.LinkGroups' : {
        'meta_info' : _MetaInfoClass('Isis.Instances.Instance.LinkGroups', REFERENCE_CLASS,
            '''Link Group''',
            False, 
            [
            _MetaInfoClassMember('link-group', REFERENCE_LIST, 'LinkGroup', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'Isis.Instances.Instance.LinkGroups.LinkGroup',
                [], [],
                '''                Configuration for link group name
                ''',
                'link_group',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            ],
            'Cisco-IOS-XR-clns-isis-cfg',
            'link-groups',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-clns-isis-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg',
        ),
    },
    'Isis.Instances.Instance.LspCheckIntervals.LspCheckInterval' : {
        'meta_info' : _MetaInfoClass('Isis.Instances.Instance.LspCheckIntervals.LspCheckInterval', REFERENCE_LIST,
            '''LSP checksum check interval parameters''',
            False, 
            [
            _MetaInfoClassMember('level', REFERENCE_ENUM_CLASS, 'IsisInternalLevel', 'dt1:Isis-internal-level',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_datatypes', 'IsisInternalLevel',
                [], [],
                '''                Level to which configuration applies
                ''',
                'level',
                'Cisco-IOS-XR-clns-isis-cfg', True),
            _MetaInfoClassMember('interval', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('10', '65535')], [],
                '''                LSP checksum check interval time in seconds
                ''',
                'interval',
                'Cisco-IOS-XR-clns-isis-cfg', False, is_mandatory=True),
            ],
            'Cisco-IOS-XR-clns-isis-cfg',
            'lsp-check-interval',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-clns-isis-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg',
        ),
    },
    'Isis.Instances.Instance.LspCheckIntervals' : {
        'meta_info' : _MetaInfoClass('Isis.Instances.Instance.LspCheckIntervals', REFERENCE_CLASS,
            '''LSP checksum check interval configuration''',
            False, 
            [
            _MetaInfoClassMember('lsp-check-interval', REFERENCE_LIST, 'LspCheckInterval', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'Isis.Instances.Instance.LspCheckIntervals.LspCheckInterval',
                [], [],
                '''                LSP checksum check interval parameters
                ''',
                'lsp_check_interval',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            ],
            'Cisco-IOS-XR-clns-isis-cfg',
            'lsp-check-intervals',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-clns-isis-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg',
        ),
    },
    'Isis.Instances.Instance.LspPasswords.LspPassword' : {
        'meta_info' : _MetaInfoClass('Isis.Instances.Instance.LspPasswords.LspPassword', REFERENCE_LIST,
            '''LSP/SNP passwords. This must exist if an
LSPAcceptPassword of the same level exists.''',
            False, 
            [
            _MetaInfoClassMember('level', REFERENCE_ENUM_CLASS, 'IsisInternalLevel', 'dt1:Isis-internal-level',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_datatypes', 'IsisInternalLevel',
                [], [],
                '''                Level to which configuration applies
                ''',
                'level',
                'Cisco-IOS-XR-clns-isis-cfg', True),
            _MetaInfoClassMember('algorithm', REFERENCE_ENUM_CLASS, 'IsisAuthenticationAlgorithm', 'Isis-authentication-algorithm',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'IsisAuthenticationAlgorithm',
                [], [],
                '''                Algorithm
                ''',
                'algorithm',
                'Cisco-IOS-XR-clns-isis-cfg', False, is_mandatory=True),
            _MetaInfoClassMember('failure-mode', REFERENCE_ENUM_CLASS, 'IsisAuthenticationFailureMode', 'Isis-authentication-failure-mode',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'IsisAuthenticationFailureMode',
                [], [],
                '''                Failure Mode
                ''',
                'failure_mode',
                'Cisco-IOS-XR-clns-isis-cfg', False, is_mandatory=True),
            _MetaInfoClassMember('authentication-type', REFERENCE_ENUM_CLASS, 'IsisSnpAuth', 'Isis-snp-auth',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'IsisSnpAuth',
                [], [],
                '''                SNP packet authentication mode
                ''',
                'authentication_type',
                'Cisco-IOS-XR-clns-isis-cfg', False, is_mandatory=True),
            _MetaInfoClassMember('password', ATTRIBUTE, 'str', 'xr:Proprietary-password',
                None, None,
                [], [b'(!.+)|([^!].+)'],
                '''                Password or unencrypted Key Chain name
                ''',
                'password',
                'Cisco-IOS-XR-clns-isis-cfg', False, is_mandatory=True),
            _MetaInfoClassMember('enable-poi', REFERENCE_ENUM_CLASS, 'IsisEnablePoi', 'Isis-enable-poi',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'IsisEnablePoi',
                [], [],
                '''                Enable POI
                ''',
                'enable_poi',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            ],
            'Cisco-IOS-XR-clns-isis-cfg',
            'lsp-password',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-clns-isis-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg',
        ),
    },
    'Isis.Instances.Instance.LspPasswords' : {
        'meta_info' : _MetaInfoClass('Isis.Instances.Instance.LspPasswords', REFERENCE_CLASS,
            '''LSP/SNP password configuration''',
            False, 
            [
            _MetaInfoClassMember('lsp-password', REFERENCE_LIST, 'LspPassword', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'Isis.Instances.Instance.LspPasswords.LspPassword',
                [], [],
                '''                LSP/SNP passwords. This must exist if an
                LSPAcceptPassword of the same level exists.
                ''',
                'lsp_password',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            ],
            'Cisco-IOS-XR-clns-isis-cfg',
            'lsp-passwords',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-clns-isis-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg',
        ),
    },
    'Isis.Instances.Instance.Nets.Net' : {
        'meta_info' : _MetaInfoClass('Isis.Instances.Instance.Nets.Net', REFERENCE_LIST,
            '''Network Entity Title (NET)''',
            False, 
            [
            _MetaInfoClassMember('net-name', ATTRIBUTE, 'str', 'xr:Osi-net',
                None, None,
                [], [b'[a-fA-F0-9]{2}(\\.[a-fA-F0-9]{4}){3,9}\\.[a-fA-F0-9]{2}'],
                '''                Network Entity Title
                ''',
                'net_name',
                'Cisco-IOS-XR-clns-isis-cfg', True),
            ],
            'Cisco-IOS-XR-clns-isis-cfg',
            'net',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-clns-isis-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg',
        ),
    },
    'Isis.Instances.Instance.Nets' : {
        'meta_info' : _MetaInfoClass('Isis.Instances.Instance.Nets', REFERENCE_CLASS,
            '''NET configuration''',
            False, 
            [
            _MetaInfoClassMember('net', REFERENCE_LIST, 'Net', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'Isis.Instances.Instance.Nets.Net',
                [], [],
                '''                Network Entity Title (NET)
                ''',
                'net',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            ],
            'Cisco-IOS-XR-clns-isis-cfg',
            'nets',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-clns-isis-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg',
        ),
    },
    'Isis.Instances.Instance.LspLifetimes.LspLifetime' : {
        'meta_info' : _MetaInfoClass('Isis.Instances.Instance.LspLifetimes.LspLifetime', REFERENCE_LIST,
            '''Maximum LSP lifetime''',
            False, 
            [
            _MetaInfoClassMember('level', REFERENCE_ENUM_CLASS, 'IsisInternalLevel', 'dt1:Isis-internal-level',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_datatypes', 'IsisInternalLevel',
                [], [],
                '''                Level to which configuration applies
                ''',
                'level',
                'Cisco-IOS-XR-clns-isis-cfg', True),
            _MetaInfoClassMember('lifetime', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('1', '65535')], [],
                '''                Seconds
                ''',
                'lifetime',
                'Cisco-IOS-XR-clns-isis-cfg', False, is_mandatory=True),
            ],
            'Cisco-IOS-XR-clns-isis-cfg',
            'lsp-lifetime',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-clns-isis-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg',
        ),
    },
    'Isis.Instances.Instance.LspLifetimes' : {
        'meta_info' : _MetaInfoClass('Isis.Instances.Instance.LspLifetimes', REFERENCE_CLASS,
            '''LSP lifetime configuration''',
            False, 
            [
            _MetaInfoClassMember('lsp-lifetime', REFERENCE_LIST, 'LspLifetime', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'Isis.Instances.Instance.LspLifetimes.LspLifetime',
                [], [],
                '''                Maximum LSP lifetime
                ''',
                'lsp_lifetime',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            ],
            'Cisco-IOS-XR-clns-isis-cfg',
            'lsp-lifetimes',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-clns-isis-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg',
        ),
    },
    'Isis.Instances.Instance.OverloadBits.OverloadBit' : {
        'meta_info' : _MetaInfoClass('Isis.Instances.Instance.OverloadBits.OverloadBit', REFERENCE_LIST,
            '''Set the overload bit in the System LSP so
that other routers avoid this one in SPF
calculations. This may be done either
unconditionally, or on startup until either a
set time has passed or IS-IS is informed that
BGP has converged. This is an Object with a
union discriminated on an integer value of
the ISISOverloadBitModeType.''',
            False, 
            [
            _MetaInfoClassMember('level', REFERENCE_ENUM_CLASS, 'IsisInternalLevel', 'dt1:Isis-internal-level',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_datatypes', 'IsisInternalLevel',
                [], [],
                '''                Level to which configuration applies
                ''',
                'level',
                'Cisco-IOS-XR-clns-isis-cfg', True),
            _MetaInfoClassMember('overload-bit-mode', REFERENCE_ENUM_CLASS, 'IsisOverloadBitMode', 'Isis-overload-bit-mode',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'IsisOverloadBitMode',
                [], [],
                '''                Circumstances under which the overload bit
                is set in the system LSP
                ''',
                'overload_bit_mode',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            _MetaInfoClassMember('hippity-period', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('5', '86400')], [],
                '''                Time in seconds to advertise ourself as
                overloaded after process startup
                ''',
                'hippity_period',
                'Cisco-IOS-XR-clns-isis-cfg', False, has_when=True),
            _MetaInfoClassMember('external-adv-type', REFERENCE_ENUM_CLASS, 'IsisAdvTypeExternal', 'Isis-adv-type-external',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'IsisAdvTypeExternal',
                [], [],
                '''                Advertise prefixes from other protocols
                ''',
                'external_adv_type',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            _MetaInfoClassMember('inter-level-adv-type', REFERENCE_ENUM_CLASS, 'IsisAdvTypeInterLevel', 'Isis-adv-type-inter-level',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'IsisAdvTypeInterLevel',
                [], [],
                '''                Advertise prefixes across ISIS levels
                ''',
                'inter_level_adv_type',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            ],
            'Cisco-IOS-XR-clns-isis-cfg',
            'overload-bit',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-clns-isis-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg',
        ),
    },
    'Isis.Instances.Instance.OverloadBits' : {
        'meta_info' : _MetaInfoClass('Isis.Instances.Instance.OverloadBits', REFERENCE_CLASS,
            '''LSP overload-bit configuration''',
            False, 
            [
            _MetaInfoClassMember('overload-bit', REFERENCE_LIST, 'OverloadBit', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'Isis.Instances.Instance.OverloadBits.OverloadBit',
                [], [],
                '''                Set the overload bit in the System LSP so
                that other routers avoid this one in SPF
                calculations. This may be done either
                unconditionally, or on startup until either a
                set time has passed or IS-IS is informed that
                BGP has converged. This is an Object with a
                union discriminated on an integer value of
                the ISISOverloadBitModeType.
                ''',
                'overload_bit',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            ],
            'Cisco-IOS-XR-clns-isis-cfg',
            'overload-bits',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-clns-isis-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg',
        ),
    },
    'Isis.Instances.Instance.Interfaces.Interface.IntAffinityTable.FlexAlgos' : {
        'meta_info' : _MetaInfoClass('Isis.Instances.Instance.Interfaces.Interface.IntAffinityTable.FlexAlgos', REFERENCE_CLASS,
            '''Set the interface affinities used by
Flex-Algo''',
            False, 
            [
            _MetaInfoClassMember('flex-algo', REFERENCE_LEAFLIST, 'str', 'string',
                None, None,
                [], [],
                '''                Array of Attribute Names
                ''',
                'flex_algo',
                'Cisco-IOS-XR-clns-isis-cfg', False, max_elements=32),
            ],
            'Cisco-IOS-XR-clns-isis-cfg',
            'flex-algos',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-clns-isis-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg',
        ),
    },
    'Isis.Instances.Instance.Interfaces.Interface.IntAffinityTable' : {
        'meta_info' : _MetaInfoClass('Isis.Instances.Instance.Interfaces.Interface.IntAffinityTable', REFERENCE_CLASS,
            '''Interface Affinity Table''',
            False, 
            [
            _MetaInfoClassMember('flex-algos', REFERENCE_CLASS, 'FlexAlgos', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'Isis.Instances.Instance.Interfaces.Interface.IntAffinityTable.FlexAlgos',
                [], [],
                '''                Set the interface affinities used by
                Flex-Algo
                ''',
                'flex_algos',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            ],
            'Cisco-IOS-XR-clns-isis-cfg',
            'int-affinity-table',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-clns-isis-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg',
        ),
    },
    'Isis.Instances.Instance.Interfaces.Interface.LspRetransmitThrottleIntervals.LspRetransmitThrottleInterval' : {
        'meta_info' : _MetaInfoClass('Isis.Instances.Instance.Interfaces.Interface.LspRetransmitThrottleIntervals.LspRetransmitThrottleInterval', REFERENCE_LIST,
            '''Minimum interval betwen retransissions of
different LSPs''',
            False, 
            [
            _MetaInfoClassMember('level', REFERENCE_ENUM_CLASS, 'IsisInternalLevel', 'dt1:Isis-internal-level',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_datatypes', 'IsisInternalLevel',
                [], [],
                '''                Level to which configuration applies
                ''',
                'level',
                'Cisco-IOS-XR-clns-isis-cfg', True),
            _MetaInfoClassMember('interval', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('0', '65535')], [],
                '''                Milliseconds
                ''',
                'interval',
                'Cisco-IOS-XR-clns-isis-cfg', False, is_mandatory=True),
            ],
            'Cisco-IOS-XR-clns-isis-cfg',
            'lsp-retransmit-throttle-interval',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-clns-isis-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg',
        ),
    },
    'Isis.Instances.Instance.Interfaces.Interface.LspRetransmitThrottleIntervals' : {
        'meta_info' : _MetaInfoClass('Isis.Instances.Instance.Interfaces.Interface.LspRetransmitThrottleIntervals', REFERENCE_CLASS,
            '''LSP-retransmission-throttle-interval
configuration''',
            False, 
            [
            _MetaInfoClassMember('lsp-retransmit-throttle-interval', REFERENCE_LIST, 'LspRetransmitThrottleInterval', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'Isis.Instances.Instance.Interfaces.Interface.LspRetransmitThrottleIntervals.LspRetransmitThrottleInterval',
                [], [],
                '''                Minimum interval betwen retransissions of
                different LSPs
                ''',
                'lsp_retransmit_throttle_interval',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            ],
            'Cisco-IOS-XR-clns-isis-cfg',
            'lsp-retransmit-throttle-intervals',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-clns-isis-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg',
        ),
    },
    'Isis.Instances.Instance.Interfaces.Interface.LspRetransmitIntervals.LspRetransmitInterval' : {
        'meta_info' : _MetaInfoClass('Isis.Instances.Instance.Interfaces.Interface.LspRetransmitIntervals.LspRetransmitInterval', REFERENCE_LIST,
            '''Interval between retransmissions of the
same LSP''',
            False, 
            [
            _MetaInfoClassMember('level', REFERENCE_ENUM_CLASS, 'IsisInternalLevel', 'dt1:Isis-internal-level',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_datatypes', 'IsisInternalLevel',
                [], [],
                '''                Level to which configuration applies
                ''',
                'level',
                'Cisco-IOS-XR-clns-isis-cfg', True),
            _MetaInfoClassMember('interval', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('0', '65535')], [],
                '''                Seconds
                ''',
                'interval',
                'Cisco-IOS-XR-clns-isis-cfg', False, is_mandatory=True),
            ],
            'Cisco-IOS-XR-clns-isis-cfg',
            'lsp-retransmit-interval',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-clns-isis-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg',
        ),
    },
    'Isis.Instances.Instance.Interfaces.Interface.LspRetransmitIntervals' : {
        'meta_info' : _MetaInfoClass('Isis.Instances.Instance.Interfaces.Interface.LspRetransmitIntervals', REFERENCE_CLASS,
            '''LSP-retransmission-interval configuration''',
            False, 
            [
            _MetaInfoClassMember('lsp-retransmit-interval', REFERENCE_LIST, 'LspRetransmitInterval', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'Isis.Instances.Instance.Interfaces.Interface.LspRetransmitIntervals.LspRetransmitInterval',
                [], [],
                '''                Interval between retransmissions of the
                same LSP
                ''',
                'lsp_retransmit_interval',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            ],
            'Cisco-IOS-XR-clns-isis-cfg',
            'lsp-retransmit-intervals',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-clns-isis-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg',
        ),
    },
    'Isis.Instances.Instance.Interfaces.Interface.Bfd' : {
        'meta_info' : _MetaInfoClass('Isis.Instances.Instance.Interfaces.Interface.Bfd', REFERENCE_CLASS,
            '''BFD configuration''',
            False, 
            [
            _MetaInfoClassMember('enable-ipv6', ATTRIBUTE, 'bool', 'boolean',
                None, None,
                [], [],
                '''                TRUE to enable BFD. FALSE to disable and to
                prevent inheritance from a parent
                ''',
                'enable_ipv6',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            _MetaInfoClassMember('enable-ipv4', ATTRIBUTE, 'bool', 'boolean',
                None, None,
                [], [],
                '''                TRUE to enable BFD. FALSE to disable and to
                prevent inheritance from a parent
                ''',
                'enable_ipv4',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            _MetaInfoClassMember('interval', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('3', '30000')], [],
                '''                Hello interval for BFD sessions created by
                isis
                ''',
                'interval',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            _MetaInfoClassMember('detection-multiplier', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('2', '50')], [],
                '''                Detection multiplier for BFD sessions
                created by isis
                ''',
                'detection_multiplier',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            ],
            'Cisco-IOS-XR-clns-isis-cfg',
            'bfd',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-clns-isis-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg',
        ),
    },
    'Isis.Instances.Instance.Interfaces.Interface.Priorities.Priority' : {
        'meta_info' : _MetaInfoClass('Isis.Instances.Instance.Interfaces.Interface.Priorities.Priority', REFERENCE_LIST,
            '''DIS-election priority''',
            False, 
            [
            _MetaInfoClassMember('level', REFERENCE_ENUM_CLASS, 'IsisInternalLevel', 'dt1:Isis-internal-level',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_datatypes', 'IsisInternalLevel',
                [], [],
                '''                Level to which configuration applies
                ''',
                'level',
                'Cisco-IOS-XR-clns-isis-cfg', True),
            _MetaInfoClassMember('priority-value', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('0', '127')], [],
                '''                Priority
                ''',
                'priority_value',
                'Cisco-IOS-XR-clns-isis-cfg', False, is_mandatory=True),
            ],
            'Cisco-IOS-XR-clns-isis-cfg',
            'priority',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-clns-isis-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg',
        ),
    },
    'Isis.Instances.Instance.Interfaces.Interface.Priorities' : {
        'meta_info' : _MetaInfoClass('Isis.Instances.Instance.Interfaces.Interface.Priorities', REFERENCE_CLASS,
            '''DIS-election priority configuration''',
            False, 
            [
            _MetaInfoClassMember('priority', REFERENCE_LIST, 'Priority', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'Isis.Instances.Instance.Interfaces.Interface.Priorities.Priority',
                [], [],
                '''                DIS-election priority
                ''',
                'priority',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            ],
            'Cisco-IOS-XR-clns-isis-cfg',
            'priorities',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-clns-isis-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg',
        ),
    },
    'Isis.Instances.Instance.Interfaces.Interface.HelloAcceptPasswords.HelloAcceptPassword' : {
        'meta_info' : _MetaInfoClass('Isis.Instances.Instance.Interfaces.Interface.HelloAcceptPasswords.HelloAcceptPassword', REFERENCE_LIST,
            '''IIH accept passwords. This requires the
existence of a HelloPassword of the same
level.''',
            False, 
            [
            _MetaInfoClassMember('level', REFERENCE_ENUM_CLASS, 'IsisInternalLevel', 'dt1:Isis-internal-level',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_datatypes', 'IsisInternalLevel',
                [], [],
                '''                Level to which configuration applies
                ''',
                'level',
                'Cisco-IOS-XR-clns-isis-cfg', True),
            _MetaInfoClassMember('password', ATTRIBUTE, 'str', 'xr:Proprietary-password',
                None, None,
                [], [b'(!.+)|([^!].+)'],
                '''                Password
                ''',
                'password',
                'Cisco-IOS-XR-clns-isis-cfg', False, is_mandatory=True),
            ],
            'Cisco-IOS-XR-clns-isis-cfg',
            'hello-accept-password',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-clns-isis-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg',
        ),
    },
    'Isis.Instances.Instance.Interfaces.Interface.HelloAcceptPasswords' : {
        'meta_info' : _MetaInfoClass('Isis.Instances.Instance.Interfaces.Interface.HelloAcceptPasswords', REFERENCE_CLASS,
            '''IIH accept password configuration''',
            False, 
            [
            _MetaInfoClassMember('hello-accept-password', REFERENCE_LIST, 'HelloAcceptPassword', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'Isis.Instances.Instance.Interfaces.Interface.HelloAcceptPasswords.HelloAcceptPassword',
                [], [],
                '''                IIH accept passwords. This requires the
                existence of a HelloPassword of the same
                level.
                ''',
                'hello_accept_password',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            ],
            'Cisco-IOS-XR-clns-isis-cfg',
            'hello-accept-passwords',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-clns-isis-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg',
        ),
    },
    'Isis.Instances.Instance.Interfaces.Interface.HelloPasswords.HelloPassword' : {
        'meta_info' : _MetaInfoClass('Isis.Instances.Instance.Interfaces.Interface.HelloPasswords.HelloPassword', REFERENCE_LIST,
            '''IIH passwords. This must exist if a
HelloAcceptPassword of the same level
exists.''',
            False, 
            [
            _MetaInfoClassMember('level', REFERENCE_ENUM_CLASS, 'IsisInternalLevel', 'dt1:Isis-internal-level',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_datatypes', 'IsisInternalLevel',
                [], [],
                '''                Level to which configuration applies
                ''',
                'level',
                'Cisco-IOS-XR-clns-isis-cfg', True),
            _MetaInfoClassMember('algorithm', REFERENCE_ENUM_CLASS, 'IsisAuthenticationAlgorithm', 'Isis-authentication-algorithm',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'IsisAuthenticationAlgorithm',
                [], [],
                '''                Algorithm
                ''',
                'algorithm',
                'Cisco-IOS-XR-clns-isis-cfg', False, is_mandatory=True),
            _MetaInfoClassMember('failure-mode', REFERENCE_ENUM_CLASS, 'IsisAuthenticationFailureMode', 'Isis-authentication-failure-mode',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'IsisAuthenticationFailureMode',
                [], [],
                '''                Failure Mode
                ''',
                'failure_mode',
                'Cisco-IOS-XR-clns-isis-cfg', False, is_mandatory=True),
            _MetaInfoClassMember('password', ATTRIBUTE, 'str', 'xr:Proprietary-password',
                None, None,
                [], [b'(!.+)|([^!].+)'],
                '''                Password or unencrypted Key Chain name
                ''',
                'password',
                'Cisco-IOS-XR-clns-isis-cfg', False, is_mandatory=True),
            ],
            'Cisco-IOS-XR-clns-isis-cfg',
            'hello-password',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-clns-isis-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg',
        ),
    },
    'Isis.Instances.Instance.Interfaces.Interface.HelloPasswords' : {
        'meta_info' : _MetaInfoClass('Isis.Instances.Instance.Interfaces.Interface.HelloPasswords', REFERENCE_CLASS,
            '''IIH password configuration''',
            False, 
            [
            _MetaInfoClassMember('hello-password', REFERENCE_LIST, 'HelloPassword', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'Isis.Instances.Instance.Interfaces.Interface.HelloPasswords.HelloPassword',
                [], [],
                '''                IIH passwords. This must exist if a
                HelloAcceptPassword of the same level
                exists.
                ''',
                'hello_password',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            ],
            'Cisco-IOS-XR-clns-isis-cfg',
            'hello-passwords',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-clns-isis-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg',
        ),
    },
    'Isis.Instances.Instance.Interfaces.Interface.HelloPaddings.HelloPadding' : {
        'meta_info' : _MetaInfoClass('Isis.Instances.Instance.Interfaces.Interface.HelloPaddings.HelloPadding', REFERENCE_LIST,
            '''Pad IIHs to the interface MTU''',
            False, 
            [
            _MetaInfoClassMember('level', REFERENCE_ENUM_CLASS, 'IsisInternalLevel', 'dt1:Isis-internal-level',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_datatypes', 'IsisInternalLevel',
                [], [],
                '''                Level to which configuration applies
                ''',
                'level',
                'Cisco-IOS-XR-clns-isis-cfg', True),
            _MetaInfoClassMember('padding-type', REFERENCE_ENUM_CLASS, 'IsisHelloPadding', 'Isis-hello-padding',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'IsisHelloPadding',
                [], [],
                '''                Hello padding type value
                ''',
                'padding_type',
                'Cisco-IOS-XR-clns-isis-cfg', False, is_mandatory=True),
            ],
            'Cisco-IOS-XR-clns-isis-cfg',
            'hello-padding',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-clns-isis-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg',
        ),
    },
    'Isis.Instances.Instance.Interfaces.Interface.HelloPaddings' : {
        'meta_info' : _MetaInfoClass('Isis.Instances.Instance.Interfaces.Interface.HelloPaddings', REFERENCE_CLASS,
            '''Hello-padding configuration''',
            False, 
            [
            _MetaInfoClassMember('hello-padding', REFERENCE_LIST, 'HelloPadding', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'Isis.Instances.Instance.Interfaces.Interface.HelloPaddings.HelloPadding',
                [], [],
                '''                Pad IIHs to the interface MTU
                ''',
                'hello_padding',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            ],
            'Cisco-IOS-XR-clns-isis-cfg',
            'hello-paddings',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-clns-isis-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg',
        ),
    },
    'Isis.Instances.Instance.Interfaces.Interface.HelloMultipliers.HelloMultiplier' : {
        'meta_info' : _MetaInfoClass('Isis.Instances.Instance.Interfaces.Interface.HelloMultipliers.HelloMultiplier', REFERENCE_LIST,
            '''Hello-multiplier configuration. The number
of successive IIHs that may be missed on an
adjacency before it is considered down.''',
            False, 
            [
            _MetaInfoClassMember('level', REFERENCE_ENUM_CLASS, 'IsisInternalLevel', 'dt1:Isis-internal-level',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_datatypes', 'IsisInternalLevel',
                [], [],
                '''                Level to which configuration applies
                ''',
                'level',
                'Cisco-IOS-XR-clns-isis-cfg', True),
            _MetaInfoClassMember('multiplier', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('3', '1000')], [],
                '''                Hello multiplier value
                ''',
                'multiplier',
                'Cisco-IOS-XR-clns-isis-cfg', False, is_mandatory=True),
            ],
            'Cisco-IOS-XR-clns-isis-cfg',
            'hello-multiplier',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-clns-isis-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg',
        ),
    },
    'Isis.Instances.Instance.Interfaces.Interface.HelloMultipliers' : {
        'meta_info' : _MetaInfoClass('Isis.Instances.Instance.Interfaces.Interface.HelloMultipliers', REFERENCE_CLASS,
            '''Hello-multiplier configuration''',
            False, 
            [
            _MetaInfoClassMember('hello-multiplier', REFERENCE_LIST, 'HelloMultiplier', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'Isis.Instances.Instance.Interfaces.Interface.HelloMultipliers.HelloMultiplier',
                [], [],
                '''                Hello-multiplier configuration. The number
                of successive IIHs that may be missed on an
                adjacency before it is considered down.
                ''',
                'hello_multiplier',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            ],
            'Cisco-IOS-XR-clns-isis-cfg',
            'hello-multipliers',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-clns-isis-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg',
        ),
    },
    'Isis.Instances.Instance.Interfaces.Interface.LspFastFloodThresholds.LspFastFloodThreshold' : {
        'meta_info' : _MetaInfoClass('Isis.Instances.Instance.Interfaces.Interface.LspFastFloodThresholds.LspFastFloodThreshold', REFERENCE_LIST,
            '''Number of LSPs to send back to back on an
interface.''',
            False, 
            [
            _MetaInfoClassMember('level', REFERENCE_ENUM_CLASS, 'IsisInternalLevel', 'dt1:Isis-internal-level',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_datatypes', 'IsisInternalLevel',
                [], [],
                '''                Level to which configuration applies
                ''',
                'level',
                'Cisco-IOS-XR-clns-isis-cfg', True),
            _MetaInfoClassMember('count', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('1', '4294967295')], [],
                '''                Count
                ''',
                'count',
                'Cisco-IOS-XR-clns-isis-cfg', False, is_mandatory=True),
            ],
            'Cisco-IOS-XR-clns-isis-cfg',
            'lsp-fast-flood-threshold',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-clns-isis-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg',
        ),
    },
    'Isis.Instances.Instance.Interfaces.Interface.LspFastFloodThresholds' : {
        'meta_info' : _MetaInfoClass('Isis.Instances.Instance.Interfaces.Interface.LspFastFloodThresholds', REFERENCE_CLASS,
            '''LSP fast flood threshold configuration''',
            False, 
            [
            _MetaInfoClassMember('lsp-fast-flood-threshold', REFERENCE_LIST, 'LspFastFloodThreshold', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'Isis.Instances.Instance.Interfaces.Interface.LspFastFloodThresholds.LspFastFloodThreshold',
                [], [],
                '''                Number of LSPs to send back to back on an
                interface.
                ''',
                'lsp_fast_flood_threshold',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            ],
            'Cisco-IOS-XR-clns-isis-cfg',
            'lsp-fast-flood-thresholds',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-clns-isis-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg',
        ),
    },
    'Isis.Instances.Instance.Interfaces.Interface.PrefixAttributeNFlagClears.PrefixAttributeNFlagClear' : {
        'meta_info' : _MetaInfoClass('Isis.Instances.Instance.Interfaces.Interface.PrefixAttributeNFlagClears.PrefixAttributeNFlagClear', REFERENCE_LIST,
            '''Clear the N flag in prefix attribute flags
sub-TLV''',
            False, 
            [
            _MetaInfoClassMember('level', REFERENCE_ENUM_CLASS, 'IsisInternalLevel', 'dt1:Isis-internal-level',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_datatypes', 'IsisInternalLevel',
                [], [],
                '''                Level to which configuration applies
                ''',
                'level',
                'Cisco-IOS-XR-clns-isis-cfg', True),
            ],
            'Cisco-IOS-XR-clns-isis-cfg',
            'prefix-attribute-n-flag-clear',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-clns-isis-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg',
        ),
    },
    'Isis.Instances.Instance.Interfaces.Interface.PrefixAttributeNFlagClears' : {
        'meta_info' : _MetaInfoClass('Isis.Instances.Instance.Interfaces.Interface.PrefixAttributeNFlagClears', REFERENCE_CLASS,
            '''Prefix attribute N flag clear configuration''',
            False, 
            [
            _MetaInfoClassMember('prefix-attribute-n-flag-clear', REFERENCE_LIST, 'PrefixAttributeNFlagClear', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'Isis.Instances.Instance.Interfaces.Interface.PrefixAttributeNFlagClears.PrefixAttributeNFlagClear',
                [], [],
                '''                Clear the N flag in prefix attribute flags
                sub-TLV
                ''',
                'prefix_attribute_n_flag_clear',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            ],
            'Cisco-IOS-XR-clns-isis-cfg',
            'prefix-attribute-n-flag-clears',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-clns-isis-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg',
        ),
    },
    'Isis.Instances.Instance.Interfaces.Interface.HelloIntervals.HelloInterval' : {
        'meta_info' : _MetaInfoClass('Isis.Instances.Instance.Interfaces.Interface.HelloIntervals.HelloInterval', REFERENCE_LIST,
            '''Hello-interval configuration. The interval
at which IIH packets will be sent. This
will be three times quicker on a LAN
interface which has been electted DIS.''',
            False, 
            [
            _MetaInfoClassMember('level', REFERENCE_ENUM_CLASS, 'IsisInternalLevel', 'dt1:Isis-internal-level',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_datatypes', 'IsisInternalLevel',
                [], [],
                '''                Level to which configuration applies
                ''',
                'level',
                'Cisco-IOS-XR-clns-isis-cfg', True),
            _MetaInfoClassMember('interval', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('1', '65535')], [],
                '''                Seconds
                ''',
                'interval',
                'Cisco-IOS-XR-clns-isis-cfg', False, is_mandatory=True),
            ],
            'Cisco-IOS-XR-clns-isis-cfg',
            'hello-interval',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-clns-isis-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg',
        ),
    },
    'Isis.Instances.Instance.Interfaces.Interface.HelloIntervals' : {
        'meta_info' : _MetaInfoClass('Isis.Instances.Instance.Interfaces.Interface.HelloIntervals', REFERENCE_CLASS,
            '''Hello-interval configuration''',
            False, 
            [
            _MetaInfoClassMember('hello-interval', REFERENCE_LIST, 'HelloInterval', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'Isis.Instances.Instance.Interfaces.Interface.HelloIntervals.HelloInterval',
                [], [],
                '''                Hello-interval configuration. The interval
                at which IIH packets will be sent. This
                will be three times quicker on a LAN
                interface which has been electted DIS.
                ''',
                'hello_interval',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            ],
            'Cisco-IOS-XR-clns-isis-cfg',
            'hello-intervals',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-clns-isis-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg',
        ),
    },
    'Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.InterfaceAfData.PrefixSid' : {
        'meta_info' : _MetaInfoClass('Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.InterfaceAfData.PrefixSid', REFERENCE_CLASS,
            '''Assign prefix SID to an interface,
ISISPHPFlag will be rejected if set to
disable, ISISEXPLICITNULLFlag will
override the value of ISISPHPFlag''',
            False, 
            [
            _MetaInfoClassMember('type', REFERENCE_ENUM_CLASS, 'Isissid1', 'Isissid1',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'Isissid1',
                [], [],
                '''                SID type for the interface
                ''',
                'type',
                'Cisco-IOS-XR-clns-isis-cfg', False, is_mandatory=True),
            _MetaInfoClassMember('value', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('0', '1048575')], [],
                '''                SID value for the interface
                ''',
                'value',
                'Cisco-IOS-XR-clns-isis-cfg', False, is_mandatory=True),
            _MetaInfoClassMember('php', REFERENCE_ENUM_CLASS, 'IsisphpFlag', 'Isisphp-flag',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'IsisphpFlag',
                [], [],
                '''                Enable/Disable Penultimate Hop Popping
                ''',
                'php',
                'Cisco-IOS-XR-clns-isis-cfg', False, is_mandatory=True),
            _MetaInfoClassMember('explicit-null', REFERENCE_ENUM_CLASS, 'IsisexplicitNullFlag', 'Isisexplicit-null-flag',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'IsisexplicitNullFlag',
                [], [],
                '''                Enable/Disable Explicit-NULL flag
                ''',
                'explicit_null',
                'Cisco-IOS-XR-clns-isis-cfg', False, is_mandatory=True),
            _MetaInfoClassMember('nflag-clear', REFERENCE_ENUM_CLASS, 'NflagClear', 'Nflag-clear',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'NflagClear',
                [], [],
                '''                Clear N-flag for the prefix-SID
                ''',
                'nflag_clear',
                'Cisco-IOS-XR-clns-isis-cfg', False, is_mandatory=True),
            ],
            'Cisco-IOS-XR-clns-isis-cfg',
            'prefix-sid',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-clns-isis-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg',
            is_presence=True,
        ),
    },
    'Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.InterfaceAfData.InterfaceFrrTable.FrrlfaCandidateInterfaces.FrrlfaCandidateInterface' : {
        'meta_info' : _MetaInfoClass('Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.InterfaceAfData.InterfaceFrrTable.FrrlfaCandidateInterfaces.FrrlfaCandidateInterface', REFERENCE_LIST,
            '''Include an interface to LFA candidate
in computation''',
            False, 
            [
            _MetaInfoClassMember('interface-name', ATTRIBUTE, 'str', 'xr:Interface-name',
                None, None,
                [], [b'[a-zA-Z0-9._/-]+'],
                '''                Interface
                ''',
                'interface_name',
                'Cisco-IOS-XR-clns-isis-cfg', True),
            _MetaInfoClassMember('frr-type', REFERENCE_ENUM_CLASS, 'Isisfrr', 'Isisfrr',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'Isisfrr',
                [], [],
                '''                Computation Type
                ''',
                'frr_type',
                'Cisco-IOS-XR-clns-isis-cfg', True),
            _MetaInfoClassMember('level', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('0', '2')], [],
                '''                Level
                ''',
                'level',
                'Cisco-IOS-XR-clns-isis-cfg', False, is_mandatory=True),
            ],
            'Cisco-IOS-XR-clns-isis-cfg',
            'frrlfa-candidate-interface',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-clns-isis-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg',
        ),
    },
    'Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.InterfaceAfData.InterfaceFrrTable.FrrlfaCandidateInterfaces' : {
        'meta_info' : _MetaInfoClass('Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.InterfaceAfData.InterfaceFrrTable.FrrlfaCandidateInterfaces', REFERENCE_CLASS,
            '''FRR LFA candidate configuration''',
            False, 
            [
            _MetaInfoClassMember('frrlfa-candidate-interface', REFERENCE_LIST, 'FrrlfaCandidateInterface', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.InterfaceAfData.InterfaceFrrTable.FrrlfaCandidateInterfaces.FrrlfaCandidateInterface',
                [], [],
                '''                Include an interface to LFA candidate
                in computation
                ''',
                'frrlfa_candidate_interface',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            ],
            'Cisco-IOS-XR-clns-isis-cfg',
            'frrlfa-candidate-interfaces',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-clns-isis-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg',
        ),
    },
    'Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.InterfaceAfData.InterfaceFrrTable.FrrRemoteLfaMaxMetrics.FrrRemoteLfaMaxMetric' : {
        'meta_info' : _MetaInfoClass('Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.InterfaceAfData.InterfaceFrrTable.FrrRemoteLfaMaxMetrics.FrrRemoteLfaMaxMetric', REFERENCE_LIST,
            '''Configure the maximum metric for
selecting a remote LFA node''',
            False, 
            [
            _MetaInfoClassMember('level', REFERENCE_ENUM_CLASS, 'IsisInternalLevel', 'dt1:Isis-internal-level',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_datatypes', 'IsisInternalLevel',
                [], [],
                '''                Level to which configuration applies
                ''',
                'level',
                'Cisco-IOS-XR-clns-isis-cfg', True),
            _MetaInfoClassMember('max-metric', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('1', '16777215')], [],
                '''                Value of the metric
                ''',
                'max_metric',
                'Cisco-IOS-XR-clns-isis-cfg', False, is_mandatory=True),
            ],
            'Cisco-IOS-XR-clns-isis-cfg',
            'frr-remote-lfa-max-metric',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-clns-isis-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg',
        ),
    },
    'Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.InterfaceAfData.InterfaceFrrTable.FrrRemoteLfaMaxMetrics' : {
        'meta_info' : _MetaInfoClass('Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.InterfaceAfData.InterfaceFrrTable.FrrRemoteLfaMaxMetrics', REFERENCE_CLASS,
            '''Remote LFA maxmimum metric''',
            False, 
            [
            _MetaInfoClassMember('frr-remote-lfa-max-metric', REFERENCE_LIST, 'FrrRemoteLfaMaxMetric', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.InterfaceAfData.InterfaceFrrTable.FrrRemoteLfaMaxMetrics.FrrRemoteLfaMaxMetric',
                [], [],
                '''                Configure the maximum metric for
                selecting a remote LFA node
                ''',
                'frr_remote_lfa_max_metric',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            ],
            'Cisco-IOS-XR-clns-isis-cfg',
            'frr-remote-lfa-max-metrics',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-clns-isis-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg',
        ),
    },
    'Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.InterfaceAfData.InterfaceFrrTable.FrrTypes.FrrType' : {
        'meta_info' : _MetaInfoClass('Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.InterfaceAfData.InterfaceFrrTable.FrrTypes.FrrType', REFERENCE_LIST,
            '''Type of computation for prefixes
reachable via interface''',
            False, 
            [
            _MetaInfoClassMember('level', REFERENCE_ENUM_CLASS, 'IsisInternalLevel', 'dt1:Isis-internal-level',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_datatypes', 'IsisInternalLevel',
                [], [],
                '''                Level to which configuration applies
                ''',
                'level',
                'Cisco-IOS-XR-clns-isis-cfg', True),
            _MetaInfoClassMember('type', REFERENCE_ENUM_CLASS, 'Isisfrr', 'Isisfrr',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'Isisfrr',
                [], [],
                '''                Computation Type
                ''',
                'type',
                'Cisco-IOS-XR-clns-isis-cfg', False, is_mandatory=True),
            ],
            'Cisco-IOS-XR-clns-isis-cfg',
            'frr-type',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-clns-isis-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg',
        ),
    },
    'Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.InterfaceAfData.InterfaceFrrTable.FrrTypes' : {
        'meta_info' : _MetaInfoClass('Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.InterfaceAfData.InterfaceFrrTable.FrrTypes', REFERENCE_CLASS,
            '''Type of FRR computation per level''',
            False, 
            [
            _MetaInfoClassMember('frr-type', REFERENCE_LIST, 'FrrType', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.InterfaceAfData.InterfaceFrrTable.FrrTypes.FrrType',
                [], [],
                '''                Type of computation for prefixes
                reachable via interface
                ''',
                'frr_type',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            ],
            'Cisco-IOS-XR-clns-isis-cfg',
            'frr-types',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-clns-isis-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg',
        ),
    },
    'Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.InterfaceAfData.InterfaceFrrTable.FrrRemoteLfaTypes.FrrRemoteLfaType' : {
        'meta_info' : _MetaInfoClass('Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.InterfaceAfData.InterfaceFrrTable.FrrRemoteLfaTypes.FrrRemoteLfaType', REFERENCE_LIST,
            '''Enable remote lfa for a particular
level''',
            False, 
            [
            _MetaInfoClassMember('level', REFERENCE_ENUM_CLASS, 'IsisInternalLevel', 'dt1:Isis-internal-level',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_datatypes', 'IsisInternalLevel',
                [], [],
                '''                Level to which configuration applies
                ''',
                'level',
                'Cisco-IOS-XR-clns-isis-cfg', True),
            _MetaInfoClassMember('type', REFERENCE_ENUM_CLASS, 'IsisRemoteLfa', 'Isis-remote-lfa',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'IsisRemoteLfa',
                [], [],
                '''                Remote LFA Type
                ''',
                'type',
                'Cisco-IOS-XR-clns-isis-cfg', False, is_mandatory=True),
            ],
            'Cisco-IOS-XR-clns-isis-cfg',
            'frr-remote-lfa-type',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-clns-isis-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg',
        ),
    },
    'Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.InterfaceAfData.InterfaceFrrTable.FrrRemoteLfaTypes' : {
        'meta_info' : _MetaInfoClass('Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.InterfaceAfData.InterfaceFrrTable.FrrRemoteLfaTypes', REFERENCE_CLASS,
            '''Remote LFA Enable''',
            False, 
            [
            _MetaInfoClassMember('frr-remote-lfa-type', REFERENCE_LIST, 'FrrRemoteLfaType', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.InterfaceAfData.InterfaceFrrTable.FrrRemoteLfaTypes.FrrRemoteLfaType',
                [], [],
                '''                Enable remote lfa for a particular
                level
                ''',
                'frr_remote_lfa_type',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            ],
            'Cisco-IOS-XR-clns-isis-cfg',
            'frr-remote-lfa-types',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-clns-isis-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg',
        ),
    },
    'Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.InterfaceAfData.InterfaceFrrTable.InterfaceFrrTiebreakerDefaults.InterfaceFrrTiebreakerDefault' : {
        'meta_info' : _MetaInfoClass('Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.InterfaceAfData.InterfaceFrrTable.InterfaceFrrTiebreakerDefaults.InterfaceFrrTiebreakerDefault', REFERENCE_LIST,
            '''Configure default tiebreaker''',
            False, 
            [
            _MetaInfoClassMember('level', REFERENCE_ENUM_CLASS, 'IsisInternalLevel', 'dt1:Isis-internal-level',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_datatypes', 'IsisInternalLevel',
                [], [],
                '''                Level to which configuration applies
                ''',
                'level',
                'Cisco-IOS-XR-clns-isis-cfg', True),
            ],
            'Cisco-IOS-XR-clns-isis-cfg',
            'interface-frr-tiebreaker-default',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-clns-isis-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg',
        ),
    },
    'Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.InterfaceAfData.InterfaceFrrTable.InterfaceFrrTiebreakerDefaults' : {
        'meta_info' : _MetaInfoClass('Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.InterfaceAfData.InterfaceFrrTable.InterfaceFrrTiebreakerDefaults', REFERENCE_CLASS,
            '''Interface FRR Default tiebreaker
configuration''',
            False, 
            [
            _MetaInfoClassMember('interface-frr-tiebreaker-default', REFERENCE_LIST, 'InterfaceFrrTiebreakerDefault', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.InterfaceAfData.InterfaceFrrTable.InterfaceFrrTiebreakerDefaults.InterfaceFrrTiebreakerDefault',
                [], [],
                '''                Configure default tiebreaker
                ''',
                'interface_frr_tiebreaker_default',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            ],
            'Cisco-IOS-XR-clns-isis-cfg',
            'interface-frr-tiebreaker-defaults',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-clns-isis-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg',
        ),
    },
    'Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.InterfaceAfData.InterfaceFrrTable.FrrtilfaTypes.FrrtilfaType' : {
        'meta_info' : _MetaInfoClass('Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.InterfaceAfData.InterfaceFrrTable.FrrtilfaTypes.FrrtilfaType', REFERENCE_LIST,
            '''Enable TI lfa for a particular level''',
            False, 
            [
            _MetaInfoClassMember('level', REFERENCE_ENUM_CLASS, 'IsisInternalLevel', 'dt1:Isis-internal-level',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_datatypes', 'IsisInternalLevel',
                [], [],
                '''                Level to which configuration applies
                ''',
                'level',
                'Cisco-IOS-XR-clns-isis-cfg', True),
            ],
            'Cisco-IOS-XR-clns-isis-cfg',
            'frrtilfa-type',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-clns-isis-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg',
        ),
    },
    'Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.InterfaceAfData.InterfaceFrrTable.FrrtilfaTypes' : {
        'meta_info' : _MetaInfoClass('Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.InterfaceAfData.InterfaceFrrTable.FrrtilfaTypes', REFERENCE_CLASS,
            '''TI LFA Enable''',
            False, 
            [
            _MetaInfoClassMember('frrtilfa-type', REFERENCE_LIST, 'FrrtilfaType', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.InterfaceAfData.InterfaceFrrTable.FrrtilfaTypes.FrrtilfaType',
                [], [],
                '''                Enable TI lfa for a particular level
                ''',
                'frrtilfa_type',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            ],
            'Cisco-IOS-XR-clns-isis-cfg',
            'frrtilfa-types',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-clns-isis-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg',
        ),
    },
    'Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.InterfaceAfData.InterfaceFrrTable.FrrExcludeInterfaces.FrrExcludeInterface' : {
        'meta_info' : _MetaInfoClass('Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.InterfaceAfData.InterfaceFrrTable.FrrExcludeInterfaces.FrrExcludeInterface', REFERENCE_LIST,
            '''Exclude an interface from computation''',
            False, 
            [
            _MetaInfoClassMember('interface-name', ATTRIBUTE, 'str', 'xr:Interface-name',
                None, None,
                [], [b'[a-zA-Z0-9._/-]+'],
                '''                Interface
                ''',
                'interface_name',
                'Cisco-IOS-XR-clns-isis-cfg', True),
            _MetaInfoClassMember('frr-type', REFERENCE_ENUM_CLASS, 'Isisfrr', 'Isisfrr',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'Isisfrr',
                [], [],
                '''                Computation Type
                ''',
                'frr_type',
                'Cisco-IOS-XR-clns-isis-cfg', True),
            _MetaInfoClassMember('level', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('0', '2')], [],
                '''                Level
                ''',
                'level',
                'Cisco-IOS-XR-clns-isis-cfg', False, is_mandatory=True),
            ],
            'Cisco-IOS-XR-clns-isis-cfg',
            'frr-exclude-interface',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-clns-isis-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg',
        ),
    },
    'Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.InterfaceAfData.InterfaceFrrTable.FrrExcludeInterfaces' : {
        'meta_info' : _MetaInfoClass('Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.InterfaceAfData.InterfaceFrrTable.FrrExcludeInterfaces', REFERENCE_CLASS,
            '''FRR exclusion configuration''',
            False, 
            [
            _MetaInfoClassMember('frr-exclude-interface', REFERENCE_LIST, 'FrrExcludeInterface', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.InterfaceAfData.InterfaceFrrTable.FrrExcludeInterfaces.FrrExcludeInterface',
                [], [],
                '''                Exclude an interface from computation
                ''',
                'frr_exclude_interface',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            ],
            'Cisco-IOS-XR-clns-isis-cfg',
            'frr-exclude-interfaces',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-clns-isis-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg',
        ),
    },
    'Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.InterfaceAfData.InterfaceFrrTable.InterfaceFrrTiebreakers.InterfaceFrrTiebreaker' : {
        'meta_info' : _MetaInfoClass('Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.InterfaceAfData.InterfaceFrrTable.InterfaceFrrTiebreakers.InterfaceFrrTiebreaker', REFERENCE_LIST,
            '''Configure tiebreaker for multiple
backups''',
            False, 
            [
            _MetaInfoClassMember('level', REFERENCE_ENUM_CLASS, 'IsisInternalLevel', 'dt1:Isis-internal-level',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_datatypes', 'IsisInternalLevel',
                [], [],
                '''                Level to which configuration applies
                ''',
                'level',
                'Cisco-IOS-XR-clns-isis-cfg', True),
            _MetaInfoClassMember('tiebreaker', REFERENCE_ENUM_CLASS, 'IsisInterfaceFrrTiebreaker', 'Isis-interface-frr-tiebreaker',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'IsisInterfaceFrrTiebreaker',
                [], [],
                '''                Tiebreaker for which configuration
                applies
                ''',
                'tiebreaker',
                'Cisco-IOS-XR-clns-isis-cfg', True),
            _MetaInfoClassMember('index', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('1', '255')], [],
                '''                Preference order among tiebreakers
                ''',
                'index',
                'Cisco-IOS-XR-clns-isis-cfg', False, is_mandatory=True),
            ],
            'Cisco-IOS-XR-clns-isis-cfg',
            'interface-frr-tiebreaker',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-clns-isis-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg',
        ),
    },
    'Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.InterfaceAfData.InterfaceFrrTable.InterfaceFrrTiebreakers' : {
        'meta_info' : _MetaInfoClass('Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.InterfaceAfData.InterfaceFrrTable.InterfaceFrrTiebreakers', REFERENCE_CLASS,
            '''Interface FRR tiebreakers configuration''',
            False, 
            [
            _MetaInfoClassMember('interface-frr-tiebreaker', REFERENCE_LIST, 'InterfaceFrrTiebreaker', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.InterfaceAfData.InterfaceFrrTable.InterfaceFrrTiebreakers.InterfaceFrrTiebreaker',
                [], [],
                '''                Configure tiebreaker for multiple
                backups
                ''',
                'interface_frr_tiebreaker',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            ],
            'Cisco-IOS-XR-clns-isis-cfg',
            'interface-frr-tiebreakers',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-clns-isis-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg',
        ),
    },
    'Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.InterfaceAfData.InterfaceFrrTable' : {
        'meta_info' : _MetaInfoClass('Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.InterfaceAfData.InterfaceFrrTable', REFERENCE_CLASS,
            '''Fast-ReRoute configuration''',
            False, 
            [
            _MetaInfoClassMember('frrlfa-candidate-interfaces', REFERENCE_CLASS, 'FrrlfaCandidateInterfaces', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.InterfaceAfData.InterfaceFrrTable.FrrlfaCandidateInterfaces',
                [], [],
                '''                FRR LFA candidate configuration
                ''',
                'frrlfa_candidate_interfaces',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            _MetaInfoClassMember('frr-remote-lfa-max-metrics', REFERENCE_CLASS, 'FrrRemoteLfaMaxMetrics', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.InterfaceAfData.InterfaceFrrTable.FrrRemoteLfaMaxMetrics',
                [], [],
                '''                Remote LFA maxmimum metric
                ''',
                'frr_remote_lfa_max_metrics',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            _MetaInfoClassMember('frr-types', REFERENCE_CLASS, 'FrrTypes', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.InterfaceAfData.InterfaceFrrTable.FrrTypes',
                [], [],
                '''                Type of FRR computation per level
                ''',
                'frr_types',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            _MetaInfoClassMember('frr-remote-lfa-types', REFERENCE_CLASS, 'FrrRemoteLfaTypes', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.InterfaceAfData.InterfaceFrrTable.FrrRemoteLfaTypes',
                [], [],
                '''                Remote LFA Enable
                ''',
                'frr_remote_lfa_types',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            _MetaInfoClassMember('interface-frr-tiebreaker-defaults', REFERENCE_CLASS, 'InterfaceFrrTiebreakerDefaults', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.InterfaceAfData.InterfaceFrrTable.InterfaceFrrTiebreakerDefaults',
                [], [],
                '''                Interface FRR Default tiebreaker
                configuration
                ''',
                'interface_frr_tiebreaker_defaults',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            _MetaInfoClassMember('frrtilfa-types', REFERENCE_CLASS, 'FrrtilfaTypes', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.InterfaceAfData.InterfaceFrrTable.FrrtilfaTypes',
                [], [],
                '''                TI LFA Enable
                ''',
                'frrtilfa_types',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            _MetaInfoClassMember('frr-exclude-interfaces', REFERENCE_CLASS, 'FrrExcludeInterfaces', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.InterfaceAfData.InterfaceFrrTable.FrrExcludeInterfaces',
                [], [],
                '''                FRR exclusion configuration
                ''',
                'frr_exclude_interfaces',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            _MetaInfoClassMember('interface-frr-tiebreakers', REFERENCE_CLASS, 'InterfaceFrrTiebreakers', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.InterfaceAfData.InterfaceFrrTable.InterfaceFrrTiebreakers',
                [], [],
                '''                Interface FRR tiebreakers configuration
                ''',
                'interface_frr_tiebreakers',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            ],
            'Cisco-IOS-XR-clns-isis-cfg',
            'interface-frr-table',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-clns-isis-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg',
        ),
    },
    'Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.InterfaceAfData.MplsLdp' : {
        'meta_info' : _MetaInfoClass('Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.InterfaceAfData.MplsLdp', REFERENCE_CLASS,
            '''MPLS LDP configuration''',
            False, 
            [
            _MetaInfoClassMember('sync-level', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('0', '2')], [],
                '''                Enable MPLS LDP Synchronization for an
                IS-IS level
                ''',
                'sync_level',
                'Cisco-IOS-XR-clns-isis-cfg', False, default_value="0"),
            ],
            'Cisco-IOS-XR-clns-isis-cfg',
            'mpls-ldp',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-clns-isis-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg',
        ),
    },
    'Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.InterfaceAfData.PrefixSspfsid' : {
        'meta_info' : _MetaInfoClass('Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.InterfaceAfData.PrefixSspfsid', REFERENCE_CLASS,
            '''Assign prefix SSPF SID to an interface,
ISISPHPFlag will be rejected if set to
disable, ISISEXPLICITNULLFlag will
override the value of ISISPHPFlag''',
            False, 
            [
            _MetaInfoClassMember('type', REFERENCE_ENUM_CLASS, 'Isissid1', 'Isissid1',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'Isissid1',
                [], [],
                '''                SID type for the interface
                ''',
                'type',
                'Cisco-IOS-XR-clns-isis-cfg', False, is_mandatory=True),
            _MetaInfoClassMember('value', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('0', '1048575')], [],
                '''                SID value for the interface
                ''',
                'value',
                'Cisco-IOS-XR-clns-isis-cfg', False, is_mandatory=True),
            _MetaInfoClassMember('php', REFERENCE_ENUM_CLASS, 'IsisphpFlag', 'Isisphp-flag',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'IsisphpFlag',
                [], [],
                '''                Enable/Disable Penultimate Hop Popping
                ''',
                'php',
                'Cisco-IOS-XR-clns-isis-cfg', False, is_mandatory=True),
            _MetaInfoClassMember('explicit-null', REFERENCE_ENUM_CLASS, 'IsisexplicitNullFlag', 'Isisexplicit-null-flag',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'IsisexplicitNullFlag',
                [], [],
                '''                Enable/Disable Explicit-NULL flag
                ''',
                'explicit_null',
                'Cisco-IOS-XR-clns-isis-cfg', False, is_mandatory=True),
            _MetaInfoClassMember('nflag-clear', REFERENCE_ENUM_CLASS, 'NflagClear', 'Nflag-clear',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'NflagClear',
                [], [],
                '''                Clear N-flag for the prefix-SID
                ''',
                'nflag_clear',
                'Cisco-IOS-XR-clns-isis-cfg', False, is_mandatory=True),
            ],
            'Cisco-IOS-XR-clns-isis-cfg',
            'prefix-sspfsid',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-clns-isis-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg',
            is_presence=True,
        ),
    },
    'Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.InterfaceAfData.AlgorithmPrefixSids.AlgorithmPrefixSid' : {
        'meta_info' : _MetaInfoClass('Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.InterfaceAfData.AlgorithmPrefixSids.AlgorithmPrefixSid', REFERENCE_LIST,
            '''Assign prefix SID for algorithm to an
interface, ISISPHPFlag will be rejected
if set to disable, ISISEXPLICITNULLFlag
will override the value of ISISPHPFlag''',
            False, 
            [
            _MetaInfoClassMember('algo', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('128', '255')], [],
                '''                Algorithm
                ''',
                'algo',
                'Cisco-IOS-XR-clns-isis-cfg', True),
            _MetaInfoClassMember('type', REFERENCE_ENUM_CLASS, 'Isissid1', 'Isissid1',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'Isissid1',
                [], [],
                '''                SID type for the interface
                ''',
                'type',
                'Cisco-IOS-XR-clns-isis-cfg', False, is_mandatory=True),
            _MetaInfoClassMember('value', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('0', '1048575')], [],
                '''                SID value for the interface
                ''',
                'value',
                'Cisco-IOS-XR-clns-isis-cfg', False, is_mandatory=True),
            _MetaInfoClassMember('php', REFERENCE_ENUM_CLASS, 'IsisphpFlag', 'Isisphp-flag',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'IsisphpFlag',
                [], [],
                '''                Enable/Disable Penultimate Hop Popping
                ''',
                'php',
                'Cisco-IOS-XR-clns-isis-cfg', False, is_mandatory=True),
            _MetaInfoClassMember('explicit-null', REFERENCE_ENUM_CLASS, 'IsisexplicitNullFlag', 'Isisexplicit-null-flag',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'IsisexplicitNullFlag',
                [], [],
                '''                Enable/Disable Explicit-NULL flag
                ''',
                'explicit_null',
                'Cisco-IOS-XR-clns-isis-cfg', False, is_mandatory=True),
            _MetaInfoClassMember('nflag-clear', REFERENCE_ENUM_CLASS, 'NflagClear', 'Nflag-clear',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'NflagClear',
                [], [],
                '''                Clear N-flag for the prefix-SID
                ''',
                'nflag_clear',
                'Cisco-IOS-XR-clns-isis-cfg', False, is_mandatory=True),
            ],
            'Cisco-IOS-XR-clns-isis-cfg',
            'algorithm-prefix-sid',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-clns-isis-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg',
        ),
    },
    'Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.InterfaceAfData.AlgorithmPrefixSids' : {
        'meta_info' : _MetaInfoClass('Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.InterfaceAfData.AlgorithmPrefixSids', REFERENCE_CLASS,
            '''Algorithm SID Table''',
            False, 
            [
            _MetaInfoClassMember('algorithm-prefix-sid', REFERENCE_LIST, 'AlgorithmPrefixSid', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.InterfaceAfData.AlgorithmPrefixSids.AlgorithmPrefixSid',
                [], [],
                '''                Assign prefix SID for algorithm to an
                interface, ISISPHPFlag will be rejected
                if set to disable, ISISEXPLICITNULLFlag
                will override the value of ISISPHPFlag
                ''',
                'algorithm_prefix_sid',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            ],
            'Cisco-IOS-XR-clns-isis-cfg',
            'algorithm-prefix-sids',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-clns-isis-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg',
        ),
    },
    'Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.InterfaceAfData.AutoMetrics.AutoMetric' : {
        'meta_info' : _MetaInfoClass('Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.InterfaceAfData.AutoMetrics.AutoMetric', REFERENCE_LIST,
            '''AutoMetric Proactive-Protect
configuration. Legal value depends on
the metric-style specified for the
topology. If the metric-style defined is
narrow, then only a value between <1-63>
is allowed and if the metric-style is
defined as wide, then a value between
<1-16777214> is allowed as the
auto-metric value.''',
            False, 
            [
            _MetaInfoClassMember('level', REFERENCE_ENUM_CLASS, 'IsisInternalLevel', 'dt1:Isis-internal-level',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_datatypes', 'IsisInternalLevel',
                [], [],
                '''                Level to which configuration applies
                ''',
                'level',
                'Cisco-IOS-XR-clns-isis-cfg', True),
            _MetaInfoClassMember('proactive-protect', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('1', '16777214')], [],
                '''                Allowed auto metric:<1-63> for narrow
                ,<1-16777214> for wide
                ''',
                'proactive_protect',
                'Cisco-IOS-XR-clns-isis-cfg', False, is_mandatory=True),
            ],
            'Cisco-IOS-XR-clns-isis-cfg',
            'auto-metric',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-clns-isis-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg',
        ),
    },
    'Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.InterfaceAfData.AutoMetrics' : {
        'meta_info' : _MetaInfoClass('Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.InterfaceAfData.AutoMetrics', REFERENCE_CLASS,
            '''AutoMetric configuration''',
            False, 
            [
            _MetaInfoClassMember('auto-metric', REFERENCE_LIST, 'AutoMetric', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.InterfaceAfData.AutoMetrics.AutoMetric',
                [], [],
                '''                AutoMetric Proactive-Protect
                configuration. Legal value depends on
                the metric-style specified for the
                topology. If the metric-style defined is
                narrow, then only a value between <1-63>
                is allowed and if the metric-style is
                defined as wide, then a value between
                <1-16777214> is allowed as the
                auto-metric value.
                ''',
                'auto_metric',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            ],
            'Cisco-IOS-XR-clns-isis-cfg',
            'auto-metrics',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-clns-isis-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg',
        ),
    },
    'Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.InterfaceAfData.AdminTags.AdminTag' : {
        'meta_info' : _MetaInfoClass('Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.InterfaceAfData.AdminTags.AdminTag', REFERENCE_LIST,
            '''Admin tag for advertised interface
connected routes''',
            False, 
            [
            _MetaInfoClassMember('level', REFERENCE_ENUM_CLASS, 'IsisInternalLevel', 'dt1:Isis-internal-level',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_datatypes', 'IsisInternalLevel',
                [], [],
                '''                Level to which configuration applies
                ''',
                'level',
                'Cisco-IOS-XR-clns-isis-cfg', True),
            _MetaInfoClassMember('admin-tag', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('1', '4294967295')], [],
                '''                Tag to associate with connected routes
                ''',
                'admin_tag',
                'Cisco-IOS-XR-clns-isis-cfg', False, is_mandatory=True),
            ],
            'Cisco-IOS-XR-clns-isis-cfg',
            'admin-tag',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-clns-isis-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg',
        ),
    },
    'Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.InterfaceAfData.AdminTags' : {
        'meta_info' : _MetaInfoClass('Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.InterfaceAfData.AdminTags', REFERENCE_CLASS,
            '''admin-tag configuration''',
            False, 
            [
            _MetaInfoClassMember('admin-tag', REFERENCE_LIST, 'AdminTag', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.InterfaceAfData.AdminTags.AdminTag',
                [], [],
                '''                Admin tag for advertised interface
                connected routes
                ''',
                'admin_tag',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            ],
            'Cisco-IOS-XR-clns-isis-cfg',
            'admin-tags',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-clns-isis-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg',
        ),
    },
    'Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.InterfaceAfData.InterfaceLinkGroup' : {
        'meta_info' : _MetaInfoClass('Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.InterfaceAfData.InterfaceLinkGroup', REFERENCE_CLASS,
            '''Provide link group name and level''',
            False, 
            [
            _MetaInfoClassMember('link-group', ATTRIBUTE, 'str', 'dt1:Isis-link-group-name',
                None, None,
                [(1, 40)], [],
                '''                Link Group
                ''',
                'link_group',
                'Cisco-IOS-XR-clns-isis-cfg', False, is_mandatory=True),
            _MetaInfoClassMember('level', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('0', '2')], [],
                '''                Level in which link group will be
                effective
                ''',
                'level',
                'Cisco-IOS-XR-clns-isis-cfg', False, default_value="0"),
            ],
            'Cisco-IOS-XR-clns-isis-cfg',
            'interface-link-group',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-clns-isis-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg',
            is_presence=True,
        ),
    },
    'Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.InterfaceAfData.ManualAdjSids.ManualAdjSid' : {
        'meta_info' : _MetaInfoClass('Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.InterfaceAfData.ManualAdjSids.ManualAdjSid', REFERENCE_LIST,
            '''Assign adjancency SID to an interface''',
            False, 
            [
            _MetaInfoClassMember('level', REFERENCE_ENUM_CLASS, 'IsisInternalLevel', 'dt1:Isis-internal-level',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_datatypes', 'IsisInternalLevel',
                [], [],
                '''                Level to which configuration applies
                ''',
                'level',
                'Cisco-IOS-XR-clns-isis-cfg', True),
            _MetaInfoClassMember('sid-type', REFERENCE_ENUM_CLASS, 'Isissid1', 'Isissid1',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'Isissid1',
                [], [],
                '''                Sid type aboslute or index
                ''',
                'sid_type',
                'Cisco-IOS-XR-clns-isis-cfg', True),
            _MetaInfoClassMember('sid', ATTRIBUTE, 'int', 'Isissid',
                None, None,
                [('0', '1048575')], [],
                '''                Sid value
                ''',
                'sid',
                'Cisco-IOS-XR-clns-isis-cfg', True),
            _MetaInfoClassMember('protected', REFERENCE_ENUM_CLASS, 'IsissidProtected', 'Isissid-protected',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'IsissidProtected',
                [], [],
                '''                Enable/Disable SID protection
                ''',
                'protected',
                'Cisco-IOS-XR-clns-isis-cfg', False, is_mandatory=True),
            ],
            'Cisco-IOS-XR-clns-isis-cfg',
            'manual-adj-sid',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-clns-isis-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg',
        ),
    },
    'Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.InterfaceAfData.ManualAdjSids' : {
        'meta_info' : _MetaInfoClass('Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.InterfaceAfData.ManualAdjSids', REFERENCE_CLASS,
            '''Manual Adjacecy SID configuration''',
            False, 
            [
            _MetaInfoClassMember('manual-adj-sid', REFERENCE_LIST, 'ManualAdjSid', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.InterfaceAfData.ManualAdjSids.ManualAdjSid',
                [], [],
                '''                Assign adjancency SID to an interface
                ''',
                'manual_adj_sid',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            ],
            'Cisco-IOS-XR-clns-isis-cfg',
            'manual-adj-sids',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-clns-isis-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg',
        ),
    },
    'Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.InterfaceAfData.Metrics.Metric.Metric_' : _MetaInfoEnum('Metric_',
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.InterfaceAfData.Metrics.Metric.Metric_',
        ''' ''',
        {
            'maximum':'maximum',
        }, 'Cisco-IOS-XR-clns-isis-cfg', _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-clns-isis-cfg']),
    'Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.InterfaceAfData.Metrics.Metric' : {
        'meta_info' : _MetaInfoClass('Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.InterfaceAfData.Metrics.Metric', REFERENCE_LIST,
            '''Metric configuration. Legal value depends on
the metric-style specified for the topology. If
the metric-style defined is narrow, then only a
value between <1-63> is allowed and if the
metric-style is defined as wide, then a value
between <1-16777215> is allowed as the metric
value.  All routers exclude links with the
maximum wide metric (16777215) from their SPF''',
            False, 
            [
            _MetaInfoClassMember('level', REFERENCE_ENUM_CLASS, 'IsisInternalLevel', 'dt1:Isis-internal-level',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_datatypes', 'IsisInternalLevel',
                [], [],
                '''                Level to which configuration applies
                ''',
                'level',
                'Cisco-IOS-XR-clns-isis-cfg', True),
            _MetaInfoClassMember('metric', REFERENCE_UNION, 'str', 'union',
                None, None,
                [], [],
                '''                Allowed metric: <1-63> for narrow,
                <1-16777215> for wide
                ''',
                'metric',
                'Cisco-IOS-XR-clns-isis-cfg', False, [
                    _MetaInfoClassMember('metric', REFERENCE_ENUM_CLASS, 'Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.TopologyName.Metrics.Metric.Metric_', 'enumeration',
                        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.TopologyName.Metrics.Metric.Metric_',
                        [], [],
                        '''                        Allowed metric: <1-63> for narrow,
                        <1-16777215> for wide
                        ''',
                        'metric',
                        'Cisco-IOS-XR-clns-isis-cfg', False, is_mandatory=True),
                    _MetaInfoClassMember('metric', ATTRIBUTE, 'int', 'uint32',
                        None, None,
                        [('1', '16777215')], [],
                        '''                        Allowed metric: <1-63> for narrow,
                        <1-16777215> for wide
                        ''',
                        'metric',
                        'Cisco-IOS-XR-clns-isis-cfg', False, is_mandatory=True),
                ], is_mandatory=True),
            ],
            'Cisco-IOS-XR-clns-isis-cfg',
            'metric',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-clns-isis-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg',
        ),
    },
    'Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.InterfaceAfData.Metrics' : {
        'meta_info' : _MetaInfoClass('Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.InterfaceAfData.Metrics', REFERENCE_CLASS,
            '''Metric configuration''',
            False, 
            [
            _MetaInfoClassMember('metric', REFERENCE_LIST, 'Metric', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.InterfaceAfData.Metrics.Metric',
                [], [],
                '''                Metric configuration. Legal value depends on
                the metric-style specified for the topology. If
                the metric-style defined is narrow, then only a
                value between <1-63> is allowed and if the
                metric-style is defined as wide, then a value
                between <1-16777215> is allowed as the metric
                value.  All routers exclude links with the
                maximum wide metric (16777215) from their SPF
                ''',
                'metric',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            ],
            'Cisco-IOS-XR-clns-isis-cfg',
            'metrics',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-clns-isis-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg',
        ),
    },
    'Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.InterfaceAfData.Weights.Weight' : {
        'meta_info' : _MetaInfoClass('Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.InterfaceAfData.Weights.Weight', REFERENCE_LIST,
            '''Weight configuration under interface for load
balancing''',
            False, 
            [
            _MetaInfoClassMember('level', REFERENCE_ENUM_CLASS, 'IsisInternalLevel', 'dt1:Isis-internal-level',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_datatypes', 'IsisInternalLevel',
                [], [],
                '''                Level to which configuration applies
                ''',
                'level',
                'Cisco-IOS-XR-clns-isis-cfg', True),
            _MetaInfoClassMember('weight', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('1', '16777214')], [],
                '''                Weight to be configured under interface for
                Load Balancing. Allowed weight: <1-16777215>
                ''',
                'weight',
                'Cisco-IOS-XR-clns-isis-cfg', False, is_mandatory=True),
            ],
            'Cisco-IOS-XR-clns-isis-cfg',
            'weight',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-clns-isis-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg',
        ),
    },
    'Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.InterfaceAfData.Weights' : {
        'meta_info' : _MetaInfoClass('Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.InterfaceAfData.Weights', REFERENCE_CLASS,
            '''Weight configuration''',
            False, 
            [
            _MetaInfoClassMember('weight', REFERENCE_LIST, 'Weight', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.InterfaceAfData.Weights.Weight',
                [], [],
                '''                Weight configuration under interface for load
                balancing
                ''',
                'weight',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            ],
            'Cisco-IOS-XR-clns-isis-cfg',
            'weights',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-clns-isis-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg',
        ),
    },
    'Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.InterfaceAfData' : {
        'meta_info' : _MetaInfoClass('Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.InterfaceAfData', REFERENCE_CLASS,
            '''Data container.''',
            False, 
            [
            _MetaInfoClassMember('prefix-sid', REFERENCE_CLASS, 'PrefixSid', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.InterfaceAfData.PrefixSid',
                [], [],
                '''                Assign prefix SID to an interface,
                ISISPHPFlag will be rejected if set to
                disable, ISISEXPLICITNULLFlag will
                override the value of ISISPHPFlag
                ''',
                'prefix_sid',
                'Cisco-IOS-XR-clns-isis-cfg', False, is_presence=True),
            _MetaInfoClassMember('interface-frr-table', REFERENCE_CLASS, 'InterfaceFrrTable', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.InterfaceAfData.InterfaceFrrTable',
                [], [],
                '''                Fast-ReRoute configuration
                ''',
                'interface_frr_table',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            _MetaInfoClassMember('mpls-ldp', REFERENCE_CLASS, 'MplsLdp', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.InterfaceAfData.MplsLdp',
                [], [],
                '''                MPLS LDP configuration
                ''',
                'mpls_ldp',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            _MetaInfoClassMember('prefix-sspfsid', REFERENCE_CLASS, 'PrefixSspfsid', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.InterfaceAfData.PrefixSspfsid',
                [], [],
                '''                Assign prefix SSPF SID to an interface,
                ISISPHPFlag will be rejected if set to
                disable, ISISEXPLICITNULLFlag will
                override the value of ISISPHPFlag
                ''',
                'prefix_sspfsid',
                'Cisco-IOS-XR-clns-isis-cfg', False, is_presence=True),
            _MetaInfoClassMember('algorithm-prefix-sids', REFERENCE_CLASS, 'AlgorithmPrefixSids', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.InterfaceAfData.AlgorithmPrefixSids',
                [], [],
                '''                Algorithm SID Table
                ''',
                'algorithm_prefix_sids',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            _MetaInfoClassMember('auto-metrics', REFERENCE_CLASS, 'AutoMetrics', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.InterfaceAfData.AutoMetrics',
                [], [],
                '''                AutoMetric configuration
                ''',
                'auto_metrics',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            _MetaInfoClassMember('admin-tags', REFERENCE_CLASS, 'AdminTags', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.InterfaceAfData.AdminTags',
                [], [],
                '''                admin-tag configuration
                ''',
                'admin_tags',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            _MetaInfoClassMember('interface-link-group', REFERENCE_CLASS, 'InterfaceLinkGroup', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.InterfaceAfData.InterfaceLinkGroup',
                [], [],
                '''                Provide link group name and level
                ''',
                'interface_link_group',
                'Cisco-IOS-XR-clns-isis-cfg', False, is_presence=True),
            _MetaInfoClassMember('interface-af-state', REFERENCE_ENUM_CLASS, 'IsisInterfaceAfState', 'Isis-interface-af-state',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'IsisInterfaceAfState',
                [], [],
                '''                Interface state
                ''',
                'interface_af_state',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            _MetaInfoClassMember('running', ATTRIBUTE, 'Empty', 'empty',
                None, None,
                [], [],
                '''                The presence of this object allows an
                address-family to be run over the
                interface in question.This must be the
                first object created under the
                InterfaceAddressFamily container, and the
                last one deleted
                ''',
                'running',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            _MetaInfoClassMember('manual-adj-sids', REFERENCE_CLASS, 'ManualAdjSids', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.InterfaceAfData.ManualAdjSids',
                [], [],
                '''                Manual Adjacecy SID configuration
                ''',
                'manual_adj_sids',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            _MetaInfoClassMember('metrics', REFERENCE_CLASS, 'Metrics', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.InterfaceAfData.Metrics',
                [], [],
                '''                Metric configuration
                ''',
                'metrics',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            _MetaInfoClassMember('weights', REFERENCE_CLASS, 'Weights', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.InterfaceAfData.Weights',
                [], [],
                '''                Weight configuration
                ''',
                'weights',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            ],
            'Cisco-IOS-XR-clns-isis-cfg',
            'interface-af-data',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-clns-isis-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg',
        ),
    },
    'Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.TopologyName.PrefixSid' : {
        'meta_info' : _MetaInfoClass('Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.TopologyName.PrefixSid', REFERENCE_CLASS,
            '''Assign prefix SID to an interface,
ISISPHPFlag will be rejected if set to
disable, ISISEXPLICITNULLFlag will
override the value of ISISPHPFlag''',
            False, 
            [
            _MetaInfoClassMember('type', REFERENCE_ENUM_CLASS, 'Isissid1', 'Isissid1',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'Isissid1',
                [], [],
                '''                SID type for the interface
                ''',
                'type',
                'Cisco-IOS-XR-clns-isis-cfg', False, is_mandatory=True),
            _MetaInfoClassMember('value', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('0', '1048575')], [],
                '''                SID value for the interface
                ''',
                'value',
                'Cisco-IOS-XR-clns-isis-cfg', False, is_mandatory=True),
            _MetaInfoClassMember('php', REFERENCE_ENUM_CLASS, 'IsisphpFlag', 'Isisphp-flag',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'IsisphpFlag',
                [], [],
                '''                Enable/Disable Penultimate Hop Popping
                ''',
                'php',
                'Cisco-IOS-XR-clns-isis-cfg', False, is_mandatory=True),
            _MetaInfoClassMember('explicit-null', REFERENCE_ENUM_CLASS, 'IsisexplicitNullFlag', 'Isisexplicit-null-flag',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'IsisexplicitNullFlag',
                [], [],
                '''                Enable/Disable Explicit-NULL flag
                ''',
                'explicit_null',
                'Cisco-IOS-XR-clns-isis-cfg', False, is_mandatory=True),
            _MetaInfoClassMember('nflag-clear', REFERENCE_ENUM_CLASS, 'NflagClear', 'Nflag-clear',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'NflagClear',
                [], [],
                '''                Clear N-flag for the prefix-SID
                ''',
                'nflag_clear',
                'Cisco-IOS-XR-clns-isis-cfg', False, is_mandatory=True),
            ],
            'Cisco-IOS-XR-clns-isis-cfg',
            'prefix-sid',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-clns-isis-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg',
            is_presence=True,
        ),
    },
    'Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.TopologyName.InterfaceFrrTable.FrrlfaCandidateInterfaces.FrrlfaCandidateInterface' : {
        'meta_info' : _MetaInfoClass('Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.TopologyName.InterfaceFrrTable.FrrlfaCandidateInterfaces.FrrlfaCandidateInterface', REFERENCE_LIST,
            '''Include an interface to LFA candidate
in computation''',
            False, 
            [
            _MetaInfoClassMember('interface-name', ATTRIBUTE, 'str', 'xr:Interface-name',
                None, None,
                [], [b'[a-zA-Z0-9._/-]+'],
                '''                Interface
                ''',
                'interface_name',
                'Cisco-IOS-XR-clns-isis-cfg', True),
            _MetaInfoClassMember('frr-type', REFERENCE_ENUM_CLASS, 'Isisfrr', 'Isisfrr',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'Isisfrr',
                [], [],
                '''                Computation Type
                ''',
                'frr_type',
                'Cisco-IOS-XR-clns-isis-cfg', True),
            _MetaInfoClassMember('level', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('0', '2')], [],
                '''                Level
                ''',
                'level',
                'Cisco-IOS-XR-clns-isis-cfg', False, is_mandatory=True),
            ],
            'Cisco-IOS-XR-clns-isis-cfg',
            'frrlfa-candidate-interface',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-clns-isis-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg',
        ),
    },
    'Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.TopologyName.InterfaceFrrTable.FrrlfaCandidateInterfaces' : {
        'meta_info' : _MetaInfoClass('Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.TopologyName.InterfaceFrrTable.FrrlfaCandidateInterfaces', REFERENCE_CLASS,
            '''FRR LFA candidate configuration''',
            False, 
            [
            _MetaInfoClassMember('frrlfa-candidate-interface', REFERENCE_LIST, 'FrrlfaCandidateInterface', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.TopologyName.InterfaceFrrTable.FrrlfaCandidateInterfaces.FrrlfaCandidateInterface',
                [], [],
                '''                Include an interface to LFA candidate
                in computation
                ''',
                'frrlfa_candidate_interface',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            ],
            'Cisco-IOS-XR-clns-isis-cfg',
            'frrlfa-candidate-interfaces',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-clns-isis-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg',
        ),
    },
    'Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.TopologyName.InterfaceFrrTable.FrrRemoteLfaMaxMetrics.FrrRemoteLfaMaxMetric' : {
        'meta_info' : _MetaInfoClass('Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.TopologyName.InterfaceFrrTable.FrrRemoteLfaMaxMetrics.FrrRemoteLfaMaxMetric', REFERENCE_LIST,
            '''Configure the maximum metric for
selecting a remote LFA node''',
            False, 
            [
            _MetaInfoClassMember('level', REFERENCE_ENUM_CLASS, 'IsisInternalLevel', 'dt1:Isis-internal-level',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_datatypes', 'IsisInternalLevel',
                [], [],
                '''                Level to which configuration applies
                ''',
                'level',
                'Cisco-IOS-XR-clns-isis-cfg', True),
            _MetaInfoClassMember('max-metric', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('1', '16777215')], [],
                '''                Value of the metric
                ''',
                'max_metric',
                'Cisco-IOS-XR-clns-isis-cfg', False, is_mandatory=True),
            ],
            'Cisco-IOS-XR-clns-isis-cfg',
            'frr-remote-lfa-max-metric',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-clns-isis-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg',
        ),
    },
    'Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.TopologyName.InterfaceFrrTable.FrrRemoteLfaMaxMetrics' : {
        'meta_info' : _MetaInfoClass('Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.TopologyName.InterfaceFrrTable.FrrRemoteLfaMaxMetrics', REFERENCE_CLASS,
            '''Remote LFA maxmimum metric''',
            False, 
            [
            _MetaInfoClassMember('frr-remote-lfa-max-metric', REFERENCE_LIST, 'FrrRemoteLfaMaxMetric', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.TopologyName.InterfaceFrrTable.FrrRemoteLfaMaxMetrics.FrrRemoteLfaMaxMetric',
                [], [],
                '''                Configure the maximum metric for
                selecting a remote LFA node
                ''',
                'frr_remote_lfa_max_metric',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            ],
            'Cisco-IOS-XR-clns-isis-cfg',
            'frr-remote-lfa-max-metrics',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-clns-isis-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg',
        ),
    },
    'Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.TopologyName.InterfaceFrrTable.FrrTypes.FrrType' : {
        'meta_info' : _MetaInfoClass('Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.TopologyName.InterfaceFrrTable.FrrTypes.FrrType', REFERENCE_LIST,
            '''Type of computation for prefixes
reachable via interface''',
            False, 
            [
            _MetaInfoClassMember('level', REFERENCE_ENUM_CLASS, 'IsisInternalLevel', 'dt1:Isis-internal-level',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_datatypes', 'IsisInternalLevel',
                [], [],
                '''                Level to which configuration applies
                ''',
                'level',
                'Cisco-IOS-XR-clns-isis-cfg', True),
            _MetaInfoClassMember('type', REFERENCE_ENUM_CLASS, 'Isisfrr', 'Isisfrr',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'Isisfrr',
                [], [],
                '''                Computation Type
                ''',
                'type',
                'Cisco-IOS-XR-clns-isis-cfg', False, is_mandatory=True),
            ],
            'Cisco-IOS-XR-clns-isis-cfg',
            'frr-type',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-clns-isis-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg',
        ),
    },
    'Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.TopologyName.InterfaceFrrTable.FrrTypes' : {
        'meta_info' : _MetaInfoClass('Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.TopologyName.InterfaceFrrTable.FrrTypes', REFERENCE_CLASS,
            '''Type of FRR computation per level''',
            False, 
            [
            _MetaInfoClassMember('frr-type', REFERENCE_LIST, 'FrrType', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.TopologyName.InterfaceFrrTable.FrrTypes.FrrType',
                [], [],
                '''                Type of computation for prefixes
                reachable via interface
                ''',
                'frr_type',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            ],
            'Cisco-IOS-XR-clns-isis-cfg',
            'frr-types',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-clns-isis-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg',
        ),
    },
    'Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.TopologyName.InterfaceFrrTable.FrrRemoteLfaTypes.FrrRemoteLfaType' : {
        'meta_info' : _MetaInfoClass('Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.TopologyName.InterfaceFrrTable.FrrRemoteLfaTypes.FrrRemoteLfaType', REFERENCE_LIST,
            '''Enable remote lfa for a particular
level''',
            False, 
            [
            _MetaInfoClassMember('level', REFERENCE_ENUM_CLASS, 'IsisInternalLevel', 'dt1:Isis-internal-level',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_datatypes', 'IsisInternalLevel',
                [], [],
                '''                Level to which configuration applies
                ''',
                'level',
                'Cisco-IOS-XR-clns-isis-cfg', True),
            _MetaInfoClassMember('type', REFERENCE_ENUM_CLASS, 'IsisRemoteLfa', 'Isis-remote-lfa',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'IsisRemoteLfa',
                [], [],
                '''                Remote LFA Type
                ''',
                'type',
                'Cisco-IOS-XR-clns-isis-cfg', False, is_mandatory=True),
            ],
            'Cisco-IOS-XR-clns-isis-cfg',
            'frr-remote-lfa-type',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-clns-isis-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg',
        ),
    },
    'Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.TopologyName.InterfaceFrrTable.FrrRemoteLfaTypes' : {
        'meta_info' : _MetaInfoClass('Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.TopologyName.InterfaceFrrTable.FrrRemoteLfaTypes', REFERENCE_CLASS,
            '''Remote LFA Enable''',
            False, 
            [
            _MetaInfoClassMember('frr-remote-lfa-type', REFERENCE_LIST, 'FrrRemoteLfaType', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.TopologyName.InterfaceFrrTable.FrrRemoteLfaTypes.FrrRemoteLfaType',
                [], [],
                '''                Enable remote lfa for a particular
                level
                ''',
                'frr_remote_lfa_type',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            ],
            'Cisco-IOS-XR-clns-isis-cfg',
            'frr-remote-lfa-types',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-clns-isis-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg',
        ),
    },
    'Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.TopologyName.InterfaceFrrTable.InterfaceFrrTiebreakerDefaults.InterfaceFrrTiebreakerDefault' : {
        'meta_info' : _MetaInfoClass('Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.TopologyName.InterfaceFrrTable.InterfaceFrrTiebreakerDefaults.InterfaceFrrTiebreakerDefault', REFERENCE_LIST,
            '''Configure default tiebreaker''',
            False, 
            [
            _MetaInfoClassMember('level', REFERENCE_ENUM_CLASS, 'IsisInternalLevel', 'dt1:Isis-internal-level',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_datatypes', 'IsisInternalLevel',
                [], [],
                '''                Level to which configuration applies
                ''',
                'level',
                'Cisco-IOS-XR-clns-isis-cfg', True),
            ],
            'Cisco-IOS-XR-clns-isis-cfg',
            'interface-frr-tiebreaker-default',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-clns-isis-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg',
        ),
    },
    'Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.TopologyName.InterfaceFrrTable.InterfaceFrrTiebreakerDefaults' : {
        'meta_info' : _MetaInfoClass('Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.TopologyName.InterfaceFrrTable.InterfaceFrrTiebreakerDefaults', REFERENCE_CLASS,
            '''Interface FRR Default tiebreaker
configuration''',
            False, 
            [
            _MetaInfoClassMember('interface-frr-tiebreaker-default', REFERENCE_LIST, 'InterfaceFrrTiebreakerDefault', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.TopologyName.InterfaceFrrTable.InterfaceFrrTiebreakerDefaults.InterfaceFrrTiebreakerDefault',
                [], [],
                '''                Configure default tiebreaker
                ''',
                'interface_frr_tiebreaker_default',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            ],
            'Cisco-IOS-XR-clns-isis-cfg',
            'interface-frr-tiebreaker-defaults',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-clns-isis-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg',
        ),
    },
    'Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.TopologyName.InterfaceFrrTable.FrrtilfaTypes.FrrtilfaType' : {
        'meta_info' : _MetaInfoClass('Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.TopologyName.InterfaceFrrTable.FrrtilfaTypes.FrrtilfaType', REFERENCE_LIST,
            '''Enable TI lfa for a particular level''',
            False, 
            [
            _MetaInfoClassMember('level', REFERENCE_ENUM_CLASS, 'IsisInternalLevel', 'dt1:Isis-internal-level',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_datatypes', 'IsisInternalLevel',
                [], [],
                '''                Level to which configuration applies
                ''',
                'level',
                'Cisco-IOS-XR-clns-isis-cfg', True),
            ],
            'Cisco-IOS-XR-clns-isis-cfg',
            'frrtilfa-type',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-clns-isis-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg',
        ),
    },
    'Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.TopologyName.InterfaceFrrTable.FrrtilfaTypes' : {
        'meta_info' : _MetaInfoClass('Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.TopologyName.InterfaceFrrTable.FrrtilfaTypes', REFERENCE_CLASS,
            '''TI LFA Enable''',
            False, 
            [
            _MetaInfoClassMember('frrtilfa-type', REFERENCE_LIST, 'FrrtilfaType', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.TopologyName.InterfaceFrrTable.FrrtilfaTypes.FrrtilfaType',
                [], [],
                '''                Enable TI lfa for a particular level
                ''',
                'frrtilfa_type',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            ],
            'Cisco-IOS-XR-clns-isis-cfg',
            'frrtilfa-types',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-clns-isis-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg',
        ),
    },
    'Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.TopologyName.InterfaceFrrTable.FrrExcludeInterfaces.FrrExcludeInterface' : {
        'meta_info' : _MetaInfoClass('Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.TopologyName.InterfaceFrrTable.FrrExcludeInterfaces.FrrExcludeInterface', REFERENCE_LIST,
            '''Exclude an interface from computation''',
            False, 
            [
            _MetaInfoClassMember('interface-name', ATTRIBUTE, 'str', 'xr:Interface-name',
                None, None,
                [], [b'[a-zA-Z0-9._/-]+'],
                '''                Interface
                ''',
                'interface_name',
                'Cisco-IOS-XR-clns-isis-cfg', True),
            _MetaInfoClassMember('frr-type', REFERENCE_ENUM_CLASS, 'Isisfrr', 'Isisfrr',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'Isisfrr',
                [], [],
                '''                Computation Type
                ''',
                'frr_type',
                'Cisco-IOS-XR-clns-isis-cfg', True),
            _MetaInfoClassMember('level', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('0', '2')], [],
                '''                Level
                ''',
                'level',
                'Cisco-IOS-XR-clns-isis-cfg', False, is_mandatory=True),
            ],
            'Cisco-IOS-XR-clns-isis-cfg',
            'frr-exclude-interface',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-clns-isis-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg',
        ),
    },
    'Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.TopologyName.InterfaceFrrTable.FrrExcludeInterfaces' : {
        'meta_info' : _MetaInfoClass('Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.TopologyName.InterfaceFrrTable.FrrExcludeInterfaces', REFERENCE_CLASS,
            '''FRR exclusion configuration''',
            False, 
            [
            _MetaInfoClassMember('frr-exclude-interface', REFERENCE_LIST, 'FrrExcludeInterface', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.TopologyName.InterfaceFrrTable.FrrExcludeInterfaces.FrrExcludeInterface',
                [], [],
                '''                Exclude an interface from computation
                ''',
                'frr_exclude_interface',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            ],
            'Cisco-IOS-XR-clns-isis-cfg',
            'frr-exclude-interfaces',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-clns-isis-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg',
        ),
    },
    'Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.TopologyName.InterfaceFrrTable.InterfaceFrrTiebreakers.InterfaceFrrTiebreaker' : {
        'meta_info' : _MetaInfoClass('Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.TopologyName.InterfaceFrrTable.InterfaceFrrTiebreakers.InterfaceFrrTiebreaker', REFERENCE_LIST,
            '''Configure tiebreaker for multiple
backups''',
            False, 
            [
            _MetaInfoClassMember('level', REFERENCE_ENUM_CLASS, 'IsisInternalLevel', 'dt1:Isis-internal-level',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_datatypes', 'IsisInternalLevel',
                [], [],
                '''                Level to which configuration applies
                ''',
                'level',
                'Cisco-IOS-XR-clns-isis-cfg', True),
            _MetaInfoClassMember('tiebreaker', REFERENCE_ENUM_CLASS, 'IsisInterfaceFrrTiebreaker', 'Isis-interface-frr-tiebreaker',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'IsisInterfaceFrrTiebreaker',
                [], [],
                '''                Tiebreaker for which configuration
                applies
                ''',
                'tiebreaker',
                'Cisco-IOS-XR-clns-isis-cfg', True),
            _MetaInfoClassMember('index', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('1', '255')], [],
                '''                Preference order among tiebreakers
                ''',
                'index',
                'Cisco-IOS-XR-clns-isis-cfg', False, is_mandatory=True),
            ],
            'Cisco-IOS-XR-clns-isis-cfg',
            'interface-frr-tiebreaker',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-clns-isis-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg',
        ),
    },
    'Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.TopologyName.InterfaceFrrTable.InterfaceFrrTiebreakers' : {
        'meta_info' : _MetaInfoClass('Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.TopologyName.InterfaceFrrTable.InterfaceFrrTiebreakers', REFERENCE_CLASS,
            '''Interface FRR tiebreakers configuration''',
            False, 
            [
            _MetaInfoClassMember('interface-frr-tiebreaker', REFERENCE_LIST, 'InterfaceFrrTiebreaker', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.TopologyName.InterfaceFrrTable.InterfaceFrrTiebreakers.InterfaceFrrTiebreaker',
                [], [],
                '''                Configure tiebreaker for multiple
                backups
                ''',
                'interface_frr_tiebreaker',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            ],
            'Cisco-IOS-XR-clns-isis-cfg',
            'interface-frr-tiebreakers',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-clns-isis-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg',
        ),
    },
    'Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.TopologyName.InterfaceFrrTable' : {
        'meta_info' : _MetaInfoClass('Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.TopologyName.InterfaceFrrTable', REFERENCE_CLASS,
            '''Fast-ReRoute configuration''',
            False, 
            [
            _MetaInfoClassMember('frrlfa-candidate-interfaces', REFERENCE_CLASS, 'FrrlfaCandidateInterfaces', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.TopologyName.InterfaceFrrTable.FrrlfaCandidateInterfaces',
                [], [],
                '''                FRR LFA candidate configuration
                ''',
                'frrlfa_candidate_interfaces',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            _MetaInfoClassMember('frr-remote-lfa-max-metrics', REFERENCE_CLASS, 'FrrRemoteLfaMaxMetrics', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.TopologyName.InterfaceFrrTable.FrrRemoteLfaMaxMetrics',
                [], [],
                '''                Remote LFA maxmimum metric
                ''',
                'frr_remote_lfa_max_metrics',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            _MetaInfoClassMember('frr-types', REFERENCE_CLASS, 'FrrTypes', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.TopologyName.InterfaceFrrTable.FrrTypes',
                [], [],
                '''                Type of FRR computation per level
                ''',
                'frr_types',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            _MetaInfoClassMember('frr-remote-lfa-types', REFERENCE_CLASS, 'FrrRemoteLfaTypes', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.TopologyName.InterfaceFrrTable.FrrRemoteLfaTypes',
                [], [],
                '''                Remote LFA Enable
                ''',
                'frr_remote_lfa_types',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            _MetaInfoClassMember('interface-frr-tiebreaker-defaults', REFERENCE_CLASS, 'InterfaceFrrTiebreakerDefaults', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.TopologyName.InterfaceFrrTable.InterfaceFrrTiebreakerDefaults',
                [], [],
                '''                Interface FRR Default tiebreaker
                configuration
                ''',
                'interface_frr_tiebreaker_defaults',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            _MetaInfoClassMember('frrtilfa-types', REFERENCE_CLASS, 'FrrtilfaTypes', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.TopologyName.InterfaceFrrTable.FrrtilfaTypes',
                [], [],
                '''                TI LFA Enable
                ''',
                'frrtilfa_types',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            _MetaInfoClassMember('frr-exclude-interfaces', REFERENCE_CLASS, 'FrrExcludeInterfaces', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.TopologyName.InterfaceFrrTable.FrrExcludeInterfaces',
                [], [],
                '''                FRR exclusion configuration
                ''',
                'frr_exclude_interfaces',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            _MetaInfoClassMember('interface-frr-tiebreakers', REFERENCE_CLASS, 'InterfaceFrrTiebreakers', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.TopologyName.InterfaceFrrTable.InterfaceFrrTiebreakers',
                [], [],
                '''                Interface FRR tiebreakers configuration
                ''',
                'interface_frr_tiebreakers',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            ],
            'Cisco-IOS-XR-clns-isis-cfg',
            'interface-frr-table',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-clns-isis-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg',
        ),
    },
    'Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.TopologyName.MplsLdp' : {
        'meta_info' : _MetaInfoClass('Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.TopologyName.MplsLdp', REFERENCE_CLASS,
            '''MPLS LDP configuration''',
            False, 
            [
            _MetaInfoClassMember('sync-level', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('0', '2')], [],
                '''                Enable MPLS LDP Synchronization for an
                IS-IS level
                ''',
                'sync_level',
                'Cisco-IOS-XR-clns-isis-cfg', False, default_value="0"),
            ],
            'Cisco-IOS-XR-clns-isis-cfg',
            'mpls-ldp',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-clns-isis-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg',
        ),
    },
    'Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.TopologyName.PrefixSspfsid' : {
        'meta_info' : _MetaInfoClass('Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.TopologyName.PrefixSspfsid', REFERENCE_CLASS,
            '''Assign prefix SSPF SID to an interface,
ISISPHPFlag will be rejected if set to
disable, ISISEXPLICITNULLFlag will
override the value of ISISPHPFlag''',
            False, 
            [
            _MetaInfoClassMember('type', REFERENCE_ENUM_CLASS, 'Isissid1', 'Isissid1',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'Isissid1',
                [], [],
                '''                SID type for the interface
                ''',
                'type',
                'Cisco-IOS-XR-clns-isis-cfg', False, is_mandatory=True),
            _MetaInfoClassMember('value', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('0', '1048575')], [],
                '''                SID value for the interface
                ''',
                'value',
                'Cisco-IOS-XR-clns-isis-cfg', False, is_mandatory=True),
            _MetaInfoClassMember('php', REFERENCE_ENUM_CLASS, 'IsisphpFlag', 'Isisphp-flag',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'IsisphpFlag',
                [], [],
                '''                Enable/Disable Penultimate Hop Popping
                ''',
                'php',
                'Cisco-IOS-XR-clns-isis-cfg', False, is_mandatory=True),
            _MetaInfoClassMember('explicit-null', REFERENCE_ENUM_CLASS, 'IsisexplicitNullFlag', 'Isisexplicit-null-flag',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'IsisexplicitNullFlag',
                [], [],
                '''                Enable/Disable Explicit-NULL flag
                ''',
                'explicit_null',
                'Cisco-IOS-XR-clns-isis-cfg', False, is_mandatory=True),
            _MetaInfoClassMember('nflag-clear', REFERENCE_ENUM_CLASS, 'NflagClear', 'Nflag-clear',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'NflagClear',
                [], [],
                '''                Clear N-flag for the prefix-SID
                ''',
                'nflag_clear',
                'Cisco-IOS-XR-clns-isis-cfg', False, is_mandatory=True),
            ],
            'Cisco-IOS-XR-clns-isis-cfg',
            'prefix-sspfsid',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-clns-isis-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg',
            is_presence=True,
        ),
    },
    'Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.TopologyName.AlgorithmPrefixSids.AlgorithmPrefixSid' : {
        'meta_info' : _MetaInfoClass('Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.TopologyName.AlgorithmPrefixSids.AlgorithmPrefixSid', REFERENCE_LIST,
            '''Assign prefix SID for algorithm to an
interface, ISISPHPFlag will be rejected
if set to disable, ISISEXPLICITNULLFlag
will override the value of ISISPHPFlag''',
            False, 
            [
            _MetaInfoClassMember('algo', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('128', '255')], [],
                '''                Algorithm
                ''',
                'algo',
                'Cisco-IOS-XR-clns-isis-cfg', True),
            _MetaInfoClassMember('type', REFERENCE_ENUM_CLASS, 'Isissid1', 'Isissid1',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'Isissid1',
                [], [],
                '''                SID type for the interface
                ''',
                'type',
                'Cisco-IOS-XR-clns-isis-cfg', False, is_mandatory=True),
            _MetaInfoClassMember('value', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('0', '1048575')], [],
                '''                SID value for the interface
                ''',
                'value',
                'Cisco-IOS-XR-clns-isis-cfg', False, is_mandatory=True),
            _MetaInfoClassMember('php', REFERENCE_ENUM_CLASS, 'IsisphpFlag', 'Isisphp-flag',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'IsisphpFlag',
                [], [],
                '''                Enable/Disable Penultimate Hop Popping
                ''',
                'php',
                'Cisco-IOS-XR-clns-isis-cfg', False, is_mandatory=True),
            _MetaInfoClassMember('explicit-null', REFERENCE_ENUM_CLASS, 'IsisexplicitNullFlag', 'Isisexplicit-null-flag',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'IsisexplicitNullFlag',
                [], [],
                '''                Enable/Disable Explicit-NULL flag
                ''',
                'explicit_null',
                'Cisco-IOS-XR-clns-isis-cfg', False, is_mandatory=True),
            _MetaInfoClassMember('nflag-clear', REFERENCE_ENUM_CLASS, 'NflagClear', 'Nflag-clear',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'NflagClear',
                [], [],
                '''                Clear N-flag for the prefix-SID
                ''',
                'nflag_clear',
                'Cisco-IOS-XR-clns-isis-cfg', False, is_mandatory=True),
            ],
            'Cisco-IOS-XR-clns-isis-cfg',
            'algorithm-prefix-sid',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-clns-isis-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg',
        ),
    },
    'Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.TopologyName.AlgorithmPrefixSids' : {
        'meta_info' : _MetaInfoClass('Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.TopologyName.AlgorithmPrefixSids', REFERENCE_CLASS,
            '''Algorithm SID Table''',
            False, 
            [
            _MetaInfoClassMember('algorithm-prefix-sid', REFERENCE_LIST, 'AlgorithmPrefixSid', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.TopologyName.AlgorithmPrefixSids.AlgorithmPrefixSid',
                [], [],
                '''                Assign prefix SID for algorithm to an
                interface, ISISPHPFlag will be rejected
                if set to disable, ISISEXPLICITNULLFlag
                will override the value of ISISPHPFlag
                ''',
                'algorithm_prefix_sid',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            ],
            'Cisco-IOS-XR-clns-isis-cfg',
            'algorithm-prefix-sids',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-clns-isis-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg',
        ),
    },
    'Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.TopologyName.AutoMetrics.AutoMetric' : {
        'meta_info' : _MetaInfoClass('Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.TopologyName.AutoMetrics.AutoMetric', REFERENCE_LIST,
            '''AutoMetric Proactive-Protect
configuration. Legal value depends on
the metric-style specified for the
topology. If the metric-style defined is
narrow, then only a value between <1-63>
is allowed and if the metric-style is
defined as wide, then a value between
<1-16777214> is allowed as the
auto-metric value.''',
            False, 
            [
            _MetaInfoClassMember('level', REFERENCE_ENUM_CLASS, 'IsisInternalLevel', 'dt1:Isis-internal-level',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_datatypes', 'IsisInternalLevel',
                [], [],
                '''                Level to which configuration applies
                ''',
                'level',
                'Cisco-IOS-XR-clns-isis-cfg', True),
            _MetaInfoClassMember('proactive-protect', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('1', '16777214')], [],
                '''                Allowed auto metric:<1-63> for narrow
                ,<1-16777214> for wide
                ''',
                'proactive_protect',
                'Cisco-IOS-XR-clns-isis-cfg', False, is_mandatory=True),
            ],
            'Cisco-IOS-XR-clns-isis-cfg',
            'auto-metric',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-clns-isis-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg',
        ),
    },
    'Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.TopologyName.AutoMetrics' : {
        'meta_info' : _MetaInfoClass('Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.TopologyName.AutoMetrics', REFERENCE_CLASS,
            '''AutoMetric configuration''',
            False, 
            [
            _MetaInfoClassMember('auto-metric', REFERENCE_LIST, 'AutoMetric', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.TopologyName.AutoMetrics.AutoMetric',
                [], [],
                '''                AutoMetric Proactive-Protect
                configuration. Legal value depends on
                the metric-style specified for the
                topology. If the metric-style defined is
                narrow, then only a value between <1-63>
                is allowed and if the metric-style is
                defined as wide, then a value between
                <1-16777214> is allowed as the
                auto-metric value.
                ''',
                'auto_metric',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            ],
            'Cisco-IOS-XR-clns-isis-cfg',
            'auto-metrics',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-clns-isis-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg',
        ),
    },
    'Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.TopologyName.AdminTags.AdminTag' : {
        'meta_info' : _MetaInfoClass('Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.TopologyName.AdminTags.AdminTag', REFERENCE_LIST,
            '''Admin tag for advertised interface
connected routes''',
            False, 
            [
            _MetaInfoClassMember('level', REFERENCE_ENUM_CLASS, 'IsisInternalLevel', 'dt1:Isis-internal-level',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_datatypes', 'IsisInternalLevel',
                [], [],
                '''                Level to which configuration applies
                ''',
                'level',
                'Cisco-IOS-XR-clns-isis-cfg', True),
            _MetaInfoClassMember('admin-tag', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('1', '4294967295')], [],
                '''                Tag to associate with connected routes
                ''',
                'admin_tag',
                'Cisco-IOS-XR-clns-isis-cfg', False, is_mandatory=True),
            ],
            'Cisco-IOS-XR-clns-isis-cfg',
            'admin-tag',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-clns-isis-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg',
        ),
    },
    'Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.TopologyName.AdminTags' : {
        'meta_info' : _MetaInfoClass('Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.TopologyName.AdminTags', REFERENCE_CLASS,
            '''admin-tag configuration''',
            False, 
            [
            _MetaInfoClassMember('admin-tag', REFERENCE_LIST, 'AdminTag', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.TopologyName.AdminTags.AdminTag',
                [], [],
                '''                Admin tag for advertised interface
                connected routes
                ''',
                'admin_tag',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            ],
            'Cisco-IOS-XR-clns-isis-cfg',
            'admin-tags',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-clns-isis-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg',
        ),
    },
    'Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.TopologyName.InterfaceLinkGroup' : {
        'meta_info' : _MetaInfoClass('Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.TopologyName.InterfaceLinkGroup', REFERENCE_CLASS,
            '''Provide link group name and level''',
            False, 
            [
            _MetaInfoClassMember('link-group', ATTRIBUTE, 'str', 'dt1:Isis-link-group-name',
                None, None,
                [(1, 40)], [],
                '''                Link Group
                ''',
                'link_group',
                'Cisco-IOS-XR-clns-isis-cfg', False, is_mandatory=True),
            _MetaInfoClassMember('level', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('0', '2')], [],
                '''                Level in which link group will be
                effective
                ''',
                'level',
                'Cisco-IOS-XR-clns-isis-cfg', False, default_value="0"),
            ],
            'Cisco-IOS-XR-clns-isis-cfg',
            'interface-link-group',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-clns-isis-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg',
            is_presence=True,
        ),
    },
    'Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.TopologyName.ManualAdjSids.ManualAdjSid' : {
        'meta_info' : _MetaInfoClass('Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.TopologyName.ManualAdjSids.ManualAdjSid', REFERENCE_LIST,
            '''Assign adjancency SID to an interface''',
            False, 
            [
            _MetaInfoClassMember('level', REFERENCE_ENUM_CLASS, 'IsisInternalLevel', 'dt1:Isis-internal-level',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_datatypes', 'IsisInternalLevel',
                [], [],
                '''                Level to which configuration applies
                ''',
                'level',
                'Cisco-IOS-XR-clns-isis-cfg', True),
            _MetaInfoClassMember('sid-type', REFERENCE_ENUM_CLASS, 'Isissid1', 'Isissid1',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'Isissid1',
                [], [],
                '''                Sid type aboslute or index
                ''',
                'sid_type',
                'Cisco-IOS-XR-clns-isis-cfg', True),
            _MetaInfoClassMember('sid', ATTRIBUTE, 'int', 'Isissid',
                None, None,
                [('0', '1048575')], [],
                '''                Sid value
                ''',
                'sid',
                'Cisco-IOS-XR-clns-isis-cfg', True),
            _MetaInfoClassMember('protected', REFERENCE_ENUM_CLASS, 'IsissidProtected', 'Isissid-protected',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'IsissidProtected',
                [], [],
                '''                Enable/Disable SID protection
                ''',
                'protected',
                'Cisco-IOS-XR-clns-isis-cfg', False, is_mandatory=True),
            ],
            'Cisco-IOS-XR-clns-isis-cfg',
            'manual-adj-sid',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-clns-isis-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg',
        ),
    },
    'Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.TopologyName.ManualAdjSids' : {
        'meta_info' : _MetaInfoClass('Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.TopologyName.ManualAdjSids', REFERENCE_CLASS,
            '''Manual Adjacecy SID configuration''',
            False, 
            [
            _MetaInfoClassMember('manual-adj-sid', REFERENCE_LIST, 'ManualAdjSid', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.TopologyName.ManualAdjSids.ManualAdjSid',
                [], [],
                '''                Assign adjancency SID to an interface
                ''',
                'manual_adj_sid',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            ],
            'Cisco-IOS-XR-clns-isis-cfg',
            'manual-adj-sids',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-clns-isis-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg',
        ),
    },
    'Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.TopologyName.Metrics.Metric.Metric_' : _MetaInfoEnum('Metric_',
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.TopologyName.Metrics.Metric.Metric_',
        ''' ''',
        {
            'maximum':'maximum',
        }, 'Cisco-IOS-XR-clns-isis-cfg', _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-clns-isis-cfg']),
    'Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.TopologyName.Metrics.Metric' : {
        'meta_info' : _MetaInfoClass('Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.TopologyName.Metrics.Metric', REFERENCE_LIST,
            '''Metric configuration. Legal value depends on
the metric-style specified for the topology. If
the metric-style defined is narrow, then only a
value between <1-63> is allowed and if the
metric-style is defined as wide, then a value
between <1-16777215> is allowed as the metric
value.  All routers exclude links with the
maximum wide metric (16777215) from their SPF''',
            False, 
            [
            _MetaInfoClassMember('level', REFERENCE_ENUM_CLASS, 'IsisInternalLevel', 'dt1:Isis-internal-level',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_datatypes', 'IsisInternalLevel',
                [], [],
                '''                Level to which configuration applies
                ''',
                'level',
                'Cisco-IOS-XR-clns-isis-cfg', True),
            _MetaInfoClassMember('metric', REFERENCE_UNION, 'str', 'union',
                None, None,
                [], [],
                '''                Allowed metric: <1-63> for narrow,
                <1-16777215> for wide
                ''',
                'metric',
                'Cisco-IOS-XR-clns-isis-cfg', False, [
                    _MetaInfoClassMember('metric', REFERENCE_ENUM_CLASS, 'Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.TopologyName.Metrics.Metric.Metric_', 'enumeration',
                        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.TopologyName.Metrics.Metric.Metric_',
                        [], [],
                        '''                        Allowed metric: <1-63> for narrow,
                        <1-16777215> for wide
                        ''',
                        'metric',
                        'Cisco-IOS-XR-clns-isis-cfg', False, is_mandatory=True),
                    _MetaInfoClassMember('metric', ATTRIBUTE, 'int', 'uint32',
                        None, None,
                        [('1', '16777215')], [],
                        '''                        Allowed metric: <1-63> for narrow,
                        <1-16777215> for wide
                        ''',
                        'metric',
                        'Cisco-IOS-XR-clns-isis-cfg', False, is_mandatory=True),
                ], is_mandatory=True),
            ],
            'Cisco-IOS-XR-clns-isis-cfg',
            'metric',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-clns-isis-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg',
        ),
    },
    'Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.TopologyName.Metrics' : {
        'meta_info' : _MetaInfoClass('Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.TopologyName.Metrics', REFERENCE_CLASS,
            '''Metric configuration''',
            False, 
            [
            _MetaInfoClassMember('metric', REFERENCE_LIST, 'Metric', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.TopologyName.Metrics.Metric',
                [], [],
                '''                Metric configuration. Legal value depends on
                the metric-style specified for the topology. If
                the metric-style defined is narrow, then only a
                value between <1-63> is allowed and if the
                metric-style is defined as wide, then a value
                between <1-16777215> is allowed as the metric
                value.  All routers exclude links with the
                maximum wide metric (16777215) from their SPF
                ''',
                'metric',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            ],
            'Cisco-IOS-XR-clns-isis-cfg',
            'metrics',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-clns-isis-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg',
        ),
    },
    'Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.TopologyName.Weights.Weight' : {
        'meta_info' : _MetaInfoClass('Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.TopologyName.Weights.Weight', REFERENCE_LIST,
            '''Weight configuration under interface for load
balancing''',
            False, 
            [
            _MetaInfoClassMember('level', REFERENCE_ENUM_CLASS, 'IsisInternalLevel', 'dt1:Isis-internal-level',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_datatypes', 'IsisInternalLevel',
                [], [],
                '''                Level to which configuration applies
                ''',
                'level',
                'Cisco-IOS-XR-clns-isis-cfg', True),
            _MetaInfoClassMember('weight', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('1', '16777214')], [],
                '''                Weight to be configured under interface for
                Load Balancing. Allowed weight: <1-16777215>
                ''',
                'weight',
                'Cisco-IOS-XR-clns-isis-cfg', False, is_mandatory=True),
            ],
            'Cisco-IOS-XR-clns-isis-cfg',
            'weight',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-clns-isis-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg',
        ),
    },
    'Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.TopologyName.Weights' : {
        'meta_info' : _MetaInfoClass('Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.TopologyName.Weights', REFERENCE_CLASS,
            '''Weight configuration''',
            False, 
            [
            _MetaInfoClassMember('weight', REFERENCE_LIST, 'Weight', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.TopologyName.Weights.Weight',
                [], [],
                '''                Weight configuration under interface for load
                balancing
                ''',
                'weight',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            ],
            'Cisco-IOS-XR-clns-isis-cfg',
            'weights',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-clns-isis-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg',
        ),
    },
    'Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.TopologyName' : {
        'meta_info' : _MetaInfoClass('Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.TopologyName', REFERENCE_LIST,
            '''keys: topology-name''',
            False, 
            [
            _MetaInfoClassMember('topology-name', ATTRIBUTE, 'str', 'dt1:Isis-topology-name',
                None, None,
                [(1, 32)], [],
                '''                Topology Name
                ''',
                'topology_name',
                'Cisco-IOS-XR-clns-isis-cfg', True),
            _MetaInfoClassMember('prefix-sid', REFERENCE_CLASS, 'PrefixSid', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.TopologyName.PrefixSid',
                [], [],
                '''                Assign prefix SID to an interface,
                ISISPHPFlag will be rejected if set to
                disable, ISISEXPLICITNULLFlag will
                override the value of ISISPHPFlag
                ''',
                'prefix_sid',
                'Cisco-IOS-XR-clns-isis-cfg', False, is_presence=True),
            _MetaInfoClassMember('interface-frr-table', REFERENCE_CLASS, 'InterfaceFrrTable', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.TopologyName.InterfaceFrrTable',
                [], [],
                '''                Fast-ReRoute configuration
                ''',
                'interface_frr_table',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            _MetaInfoClassMember('mpls-ldp', REFERENCE_CLASS, 'MplsLdp', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.TopologyName.MplsLdp',
                [], [],
                '''                MPLS LDP configuration
                ''',
                'mpls_ldp',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            _MetaInfoClassMember('prefix-sspfsid', REFERENCE_CLASS, 'PrefixSspfsid', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.TopologyName.PrefixSspfsid',
                [], [],
                '''                Assign prefix SSPF SID to an interface,
                ISISPHPFlag will be rejected if set to
                disable, ISISEXPLICITNULLFlag will
                override the value of ISISPHPFlag
                ''',
                'prefix_sspfsid',
                'Cisco-IOS-XR-clns-isis-cfg', False, is_presence=True),
            _MetaInfoClassMember('algorithm-prefix-sids', REFERENCE_CLASS, 'AlgorithmPrefixSids', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.TopologyName.AlgorithmPrefixSids',
                [], [],
                '''                Algorithm SID Table
                ''',
                'algorithm_prefix_sids',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            _MetaInfoClassMember('auto-metrics', REFERENCE_CLASS, 'AutoMetrics', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.TopologyName.AutoMetrics',
                [], [],
                '''                AutoMetric configuration
                ''',
                'auto_metrics',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            _MetaInfoClassMember('admin-tags', REFERENCE_CLASS, 'AdminTags', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.TopologyName.AdminTags',
                [], [],
                '''                admin-tag configuration
                ''',
                'admin_tags',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            _MetaInfoClassMember('interface-link-group', REFERENCE_CLASS, 'InterfaceLinkGroup', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.TopologyName.InterfaceLinkGroup',
                [], [],
                '''                Provide link group name and level
                ''',
                'interface_link_group',
                'Cisco-IOS-XR-clns-isis-cfg', False, is_presence=True),
            _MetaInfoClassMember('interface-af-state', REFERENCE_ENUM_CLASS, 'IsisInterfaceAfState', 'Isis-interface-af-state',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'IsisInterfaceAfState',
                [], [],
                '''                Interface state
                ''',
                'interface_af_state',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            _MetaInfoClassMember('running', ATTRIBUTE, 'Empty', 'empty',
                None, None,
                [], [],
                '''                The presence of this object allows an
                address-family to be run over the
                interface in question.This must be the
                first object created under the
                InterfaceAddressFamily container, and the
                last one deleted
                ''',
                'running',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            _MetaInfoClassMember('manual-adj-sids', REFERENCE_CLASS, 'ManualAdjSids', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.TopologyName.ManualAdjSids',
                [], [],
                '''                Manual Adjacecy SID configuration
                ''',
                'manual_adj_sids',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            _MetaInfoClassMember('metrics', REFERENCE_CLASS, 'Metrics', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.TopologyName.Metrics',
                [], [],
                '''                Metric configuration
                ''',
                'metrics',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            _MetaInfoClassMember('weights', REFERENCE_CLASS, 'Weights', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.TopologyName.Weights',
                [], [],
                '''                Weight configuration
                ''',
                'weights',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            ],
            'Cisco-IOS-XR-clns-isis-cfg',
            'topology-name',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-clns-isis-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg',
        ),
    },
    'Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf' : {
        'meta_info' : _MetaInfoClass('Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf', REFERENCE_LIST,
            '''Configuration for an IS-IS address-family
on a single interface. If a named
(non-default) topology is being created it
must be multicast. Also the topology ID
mustbe set first and delete last in the
router configuration.''',
            False, 
            [
            _MetaInfoClassMember('af-name', REFERENCE_ENUM_CLASS, 'IsisAddressFamily', 'dt1:Isis-address-family',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_datatypes', 'IsisAddressFamily',
                [], [],
                '''                Address family
                ''',
                'af_name',
                'Cisco-IOS-XR-clns-isis-cfg', True),
            _MetaInfoClassMember('saf-name', REFERENCE_ENUM_CLASS, 'IsisSubAddressFamily', 'dt1:Isis-sub-address-family',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_datatypes', 'IsisSubAddressFamily',
                [], [],
                '''                Sub address family
                ''',
                'saf_name',
                'Cisco-IOS-XR-clns-isis-cfg', True),
            _MetaInfoClassMember('interface-af-data', REFERENCE_CLASS, 'InterfaceAfData', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.InterfaceAfData',
                [], [],
                '''                Data container.
                ''',
                'interface_af_data',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            _MetaInfoClassMember('topology-name', REFERENCE_LIST, 'TopologyName', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.TopologyName',
                [], [],
                '''                keys: topology-name
                ''',
                'topology_name',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            ],
            'Cisco-IOS-XR-clns-isis-cfg',
            'interface-af',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-clns-isis-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg',
            has_must=True,
        ),
    },
    'Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs' : {
        'meta_info' : _MetaInfoClass('Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs', REFERENCE_CLASS,
            '''Per-interface address-family configuration''',
            False, 
            [
            _MetaInfoClassMember('interface-af', REFERENCE_LIST, 'InterfaceAf', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf',
                [], [],
                '''                Configuration for an IS-IS address-family
                on a single interface. If a named
                (non-default) topology is being created it
                must be multicast. Also the topology ID
                mustbe set first and delete last in the
                router configuration.
                ''',
                'interface_af',
                'Cisco-IOS-XR-clns-isis-cfg', False, has_must=True),
            ],
            'Cisco-IOS-XR-clns-isis-cfg',
            'interface-afs',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-clns-isis-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg',
        ),
    },
    'Isis.Instances.Instance.Interfaces.Interface.CsnpIntervals.CsnpInterval' : {
        'meta_info' : _MetaInfoClass('Isis.Instances.Instance.Interfaces.Interface.CsnpIntervals.CsnpInterval', REFERENCE_LIST,
            '''CSNP-interval configuration. No fixed
default value as this depends on the media
type of the interface.''',
            False, 
            [
            _MetaInfoClassMember('level', REFERENCE_ENUM_CLASS, 'IsisInternalLevel', 'dt1:Isis-internal-level',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_datatypes', 'IsisInternalLevel',
                [], [],
                '''                Level to which configuration applies
                ''',
                'level',
                'Cisco-IOS-XR-clns-isis-cfg', True),
            _MetaInfoClassMember('interval', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('0', '65535')], [],
                '''                Seconds
                ''',
                'interval',
                'Cisco-IOS-XR-clns-isis-cfg', False, is_mandatory=True),
            ],
            'Cisco-IOS-XR-clns-isis-cfg',
            'csnp-interval',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-clns-isis-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg',
        ),
    },
    'Isis.Instances.Instance.Interfaces.Interface.CsnpIntervals' : {
        'meta_info' : _MetaInfoClass('Isis.Instances.Instance.Interfaces.Interface.CsnpIntervals', REFERENCE_CLASS,
            '''CSNP-interval configuration''',
            False, 
            [
            _MetaInfoClassMember('csnp-interval', REFERENCE_LIST, 'CsnpInterval', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'Isis.Instances.Instance.Interfaces.Interface.CsnpIntervals.CsnpInterval',
                [], [],
                '''                CSNP-interval configuration. No fixed
                default value as this depends on the media
                type of the interface.
                ''',
                'csnp_interval',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            ],
            'Cisco-IOS-XR-clns-isis-cfg',
            'csnp-intervals',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-clns-isis-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg',
        ),
    },
    'Isis.Instances.Instance.Interfaces.Interface.LspIntervals.LspInterval' : {
        'meta_info' : _MetaInfoClass('Isis.Instances.Instance.Interfaces.Interface.LspIntervals.LspInterval', REFERENCE_LIST,
            '''Interval between transmission of LSPs on
interface.''',
            False, 
            [
            _MetaInfoClassMember('level', REFERENCE_ENUM_CLASS, 'IsisInternalLevel', 'dt1:Isis-internal-level',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_datatypes', 'IsisInternalLevel',
                [], [],
                '''                Level to which configuration applies
                ''',
                'level',
                'Cisco-IOS-XR-clns-isis-cfg', True),
            _MetaInfoClassMember('interval', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('1', '4294967295')], [],
                '''                Milliseconds
                ''',
                'interval',
                'Cisco-IOS-XR-clns-isis-cfg', False, is_mandatory=True),
            ],
            'Cisco-IOS-XR-clns-isis-cfg',
            'lsp-interval',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-clns-isis-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg',
        ),
    },
    'Isis.Instances.Instance.Interfaces.Interface.LspIntervals' : {
        'meta_info' : _MetaInfoClass('Isis.Instances.Instance.Interfaces.Interface.LspIntervals', REFERENCE_CLASS,
            '''LSP-interval configuration''',
            False, 
            [
            _MetaInfoClassMember('lsp-interval', REFERENCE_LIST, 'LspInterval', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'Isis.Instances.Instance.Interfaces.Interface.LspIntervals.LspInterval',
                [], [],
                '''                Interval between transmission of LSPs on
                interface.
                ''',
                'lsp_interval',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            ],
            'Cisco-IOS-XR-clns-isis-cfg',
            'lsp-intervals',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-clns-isis-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg',
        ),
    },
    'Isis.Instances.Instance.Interfaces.Interface.MeshGroup' : _MetaInfoEnum('MeshGroup',
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'Isis.Instances.Instance.Interfaces.Interface.MeshGroup',
        ''' ''',
        {
            'blocked':'blocked',
        }, 'Cisco-IOS-XR-clns-isis-cfg', _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-clns-isis-cfg']),
    'Isis.Instances.Instance.Interfaces.Interface' : {
        'meta_info' : _MetaInfoClass('Isis.Instances.Instance.Interfaces.Interface', REFERENCE_LIST,
            '''Configuration for an IS-IS interface''',
            False, 
            [
            _MetaInfoClassMember('interface-name', ATTRIBUTE, 'str', 'xr:Interface-name',
                None, None,
                [], [b'[a-zA-Z0-9._/-]+'],
                '''                Interface name
                ''',
                'interface_name',
                'Cisco-IOS-XR-clns-isis-cfg', True),
            _MetaInfoClassMember('int-affinity-table', REFERENCE_CLASS, 'IntAffinityTable', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'Isis.Instances.Instance.Interfaces.Interface.IntAffinityTable',
                [], [],
                '''                Interface Affinity Table
                ''',
                'int_affinity_table',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            _MetaInfoClassMember('lsp-retransmit-throttle-intervals', REFERENCE_CLASS, 'LspRetransmitThrottleIntervals', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'Isis.Instances.Instance.Interfaces.Interface.LspRetransmitThrottleIntervals',
                [], [],
                '''                LSP-retransmission-throttle-interval
                configuration
                ''',
                'lsp_retransmit_throttle_intervals',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            _MetaInfoClassMember('lsp-retransmit-intervals', REFERENCE_CLASS, 'LspRetransmitIntervals', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'Isis.Instances.Instance.Interfaces.Interface.LspRetransmitIntervals',
                [], [],
                '''                LSP-retransmission-interval configuration
                ''',
                'lsp_retransmit_intervals',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            _MetaInfoClassMember('bfd', REFERENCE_CLASS, 'Bfd', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'Isis.Instances.Instance.Interfaces.Interface.Bfd',
                [], [],
                '''                BFD configuration
                ''',
                'bfd',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            _MetaInfoClassMember('priorities', REFERENCE_CLASS, 'Priorities', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'Isis.Instances.Instance.Interfaces.Interface.Priorities',
                [], [],
                '''                DIS-election priority configuration
                ''',
                'priorities',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            _MetaInfoClassMember('hello-accept-passwords', REFERENCE_CLASS, 'HelloAcceptPasswords', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'Isis.Instances.Instance.Interfaces.Interface.HelloAcceptPasswords',
                [], [],
                '''                IIH accept password configuration
                ''',
                'hello_accept_passwords',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            _MetaInfoClassMember('hello-passwords', REFERENCE_CLASS, 'HelloPasswords', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'Isis.Instances.Instance.Interfaces.Interface.HelloPasswords',
                [], [],
                '''                IIH password configuration
                ''',
                'hello_passwords',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            _MetaInfoClassMember('hello-paddings', REFERENCE_CLASS, 'HelloPaddings', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'Isis.Instances.Instance.Interfaces.Interface.HelloPaddings',
                [], [],
                '''                Hello-padding configuration
                ''',
                'hello_paddings',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            _MetaInfoClassMember('hello-multipliers', REFERENCE_CLASS, 'HelloMultipliers', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'Isis.Instances.Instance.Interfaces.Interface.HelloMultipliers',
                [], [],
                '''                Hello-multiplier configuration
                ''',
                'hello_multipliers',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            _MetaInfoClassMember('lsp-fast-flood-thresholds', REFERENCE_CLASS, 'LspFastFloodThresholds', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'Isis.Instances.Instance.Interfaces.Interface.LspFastFloodThresholds',
                [], [],
                '''                LSP fast flood threshold configuration
                ''',
                'lsp_fast_flood_thresholds',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            _MetaInfoClassMember('prefix-attribute-n-flag-clears', REFERENCE_CLASS, 'PrefixAttributeNFlagClears', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'Isis.Instances.Instance.Interfaces.Interface.PrefixAttributeNFlagClears',
                [], [],
                '''                Prefix attribute N flag clear configuration
                ''',
                'prefix_attribute_n_flag_clears',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            _MetaInfoClassMember('hello-intervals', REFERENCE_CLASS, 'HelloIntervals', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'Isis.Instances.Instance.Interfaces.Interface.HelloIntervals',
                [], [],
                '''                Hello-interval configuration
                ''',
                'hello_intervals',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            _MetaInfoClassMember('interface-afs', REFERENCE_CLASS, 'InterfaceAfs', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs',
                [], [],
                '''                Per-interface address-family configuration
                ''',
                'interface_afs',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            _MetaInfoClassMember('csnp-intervals', REFERENCE_CLASS, 'CsnpIntervals', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'Isis.Instances.Instance.Interfaces.Interface.CsnpIntervals',
                [], [],
                '''                CSNP-interval configuration
                ''',
                'csnp_intervals',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            _MetaInfoClassMember('lsp-intervals', REFERENCE_CLASS, 'LspIntervals', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'Isis.Instances.Instance.Interfaces.Interface.LspIntervals',
                [], [],
                '''                LSP-interval configuration
                ''',
                'lsp_intervals',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            _MetaInfoClassMember('running', ATTRIBUTE, 'Empty', 'empty',
                None, None,
                [], [],
                '''                This object must be set before any other
                configuration is supplied for an interface,
                and must be the last per-interface
                configuration object to be removed.
                ''',
                'running',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            _MetaInfoClassMember('circuit-type', REFERENCE_ENUM_CLASS, 'IsisConfigurableLevels', 'Isis-configurable-levels',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'IsisConfigurableLevels',
                [], [],
                '''                Configure circuit type for interface
                ''',
                'circuit_type',
                'Cisco-IOS-XR-clns-isis-cfg', False, default_value='Cisco_IOS_XR_clns_isis_cfg.IsisConfigurableLevels.level1_and2'),
            _MetaInfoClassMember('point-to-point', ATTRIBUTE, 'Empty', 'empty',
                None, None,
                [], [],
                '''                IS-IS will attempt to form point-to-point
                over LAN adjacencies over this interface.
                ''',
                'point_to_point',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            _MetaInfoClassMember('state', REFERENCE_ENUM_CLASS, 'IsisInterfaceState', 'Isis-interface-state',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'IsisInterfaceState',
                [], [],
                '''                Enable/Disable routing
                ''',
                'state',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            _MetaInfoClassMember('mesh-group', REFERENCE_UNION, 'str', 'union',
                None, None,
                [], [],
                '''                Mesh-group configuration
                ''',
                'mesh_group',
                'Cisco-IOS-XR-clns-isis-cfg', False, [
                    _MetaInfoClassMember('mesh-group', REFERENCE_ENUM_CLASS, 'Isis.Instances.Instance.Interfaces.Interface.MeshGroup', 'enumeration',
                        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'Isis.Instances.Instance.Interfaces.Interface.MeshGroup',
                        [], [],
                        '''                        Mesh-group configuration
                        ''',
                        'mesh_group',
                        'Cisco-IOS-XR-clns-isis-cfg', False),
                    _MetaInfoClassMember('mesh-group', ATTRIBUTE, 'int', 'uint32',
                        None, None,
                        [('0', '4294967295')], [],
                        '''                        Mesh-group configuration
                        ''',
                        'mesh_group',
                        'Cisco-IOS-XR-clns-isis-cfg', False),
                ]),
            _MetaInfoClassMember('link-down-fast-detect', ATTRIBUTE, 'Empty', 'empty',
                None, None,
                [], [],
                '''                Configure high priority detection of
                interface down event
                ''',
                'link_down_fast_detect',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            ],
            'Cisco-IOS-XR-clns-isis-cfg',
            'interface',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-clns-isis-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg',
        ),
    },
    'Isis.Instances.Instance.Interfaces' : {
        'meta_info' : _MetaInfoClass('Isis.Instances.Instance.Interfaces', REFERENCE_CLASS,
            '''Per-interface configuration''',
            False, 
            [
            _MetaInfoClassMember('interface', REFERENCE_LIST, 'Interface', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'Isis.Instances.Instance.Interfaces.Interface',
                [], [],
                '''                Configuration for an IS-IS interface
                ''',
                'interface',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            ],
            'Cisco-IOS-XR-clns-isis-cfg',
            'interfaces',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-clns-isis-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg',
        ),
    },
    'Isis.Instances.Instance' : {
        'meta_info' : _MetaInfoClass('Isis.Instances.Instance', REFERENCE_LIST,
            '''Configuration for a single IS-IS instance''',
            False, 
            [
            _MetaInfoClassMember('instance-name', ATTRIBUTE, 'str', 'dt1:Isis-instance-name',
                None, None,
                [(1, 36)], [],
                '''                Instance identifier
                ''',
                'instance_name',
                'Cisco-IOS-XR-clns-isis-cfg', True),
            _MetaInfoClassMember('srgb', REFERENCE_CLASS, 'Srgb', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'Isis.Instances.Instance.Srgb',
                [], [],
                '''                Segment Routing Global Block configuration
                ''',
                'srgb',
                'Cisco-IOS-XR-clns-isis-cfg', False, is_presence=True),
            _MetaInfoClassMember('lsp-generation-intervals', REFERENCE_CLASS, 'LspGenerationIntervals', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'Isis.Instances.Instance.LspGenerationIntervals',
                [], [],
                '''                LSP generation-interval configuration
                ''',
                'lsp_generation_intervals',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            _MetaInfoClassMember('lsp-arrival-times', REFERENCE_CLASS, 'LspArrivalTimes', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'Isis.Instances.Instance.LspArrivalTimes',
                [], [],
                '''                LSP arrival time configuration
                ''',
                'lsp_arrival_times',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            _MetaInfoClassMember('trace-buffer-size', REFERENCE_CLASS, 'TraceBufferSize', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'Isis.Instances.Instance.TraceBufferSize',
                [], [],
                '''                Trace buffer size configuration
                ''',
                'trace_buffer_size',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            _MetaInfoClassMember('max-link-metrics', REFERENCE_CLASS, 'MaxLinkMetrics', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'Isis.Instances.Instance.MaxLinkMetrics',
                [], [],
                '''                Max Metric configuration
                ''',
                'max_link_metrics',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            _MetaInfoClassMember('adjacency-stagger', REFERENCE_CLASS, 'AdjacencyStagger', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'Isis.Instances.Instance.AdjacencyStagger',
                [], [],
                '''                Stagger ISIS adjacency bring up
                ''',
                'adjacency_stagger',
                'Cisco-IOS-XR-clns-isis-cfg', False, is_presence=True),
            _MetaInfoClassMember('afs', REFERENCE_CLASS, 'Afs', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'Isis.Instances.Instance.Afs',
                [], [],
                '''                Per-address-family configuration
                ''',
                'afs',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            _MetaInfoClassMember('lsp-refresh-intervals', REFERENCE_CLASS, 'LspRefreshIntervals', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'Isis.Instances.Instance.LspRefreshIntervals',
                [], [],
                '''                LSP refresh-interval configuration
                ''',
                'lsp_refresh_intervals',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            _MetaInfoClassMember('distribute', REFERENCE_CLASS, 'Distribute', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'Isis.Instances.Instance.Distribute',
                [], [],
                '''                Distribute link-state configuration
                ''',
                'distribute',
                'Cisco-IOS-XR-clns-isis-cfg', False, is_presence=True),
            _MetaInfoClassMember('flex-algos', REFERENCE_CLASS, 'FlexAlgos', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'Isis.Instances.Instance.FlexAlgos',
                [], [],
                '''                Flex-Algo Table
                ''',
                'flex_algos',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            _MetaInfoClassMember('affinity-mappings', REFERENCE_CLASS, 'AffinityMappings', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'Isis.Instances.Instance.AffinityMappings',
                [], [],
                '''                Affinity Mapping Table
                ''',
                'affinity_mappings',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            _MetaInfoClassMember('lsp-accept-passwords', REFERENCE_CLASS, 'LspAcceptPasswords', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'Isis.Instances.Instance.LspAcceptPasswords',
                [], [],
                '''                LSP/SNP accept password configuration
                ''',
                'lsp_accept_passwords',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            _MetaInfoClassMember('lsp-mtus', REFERENCE_CLASS, 'LspMtus', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'Isis.Instances.Instance.LspMtus',
                [], [],
                '''                LSP MTU configuration
                ''',
                'lsp_mtus',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            _MetaInfoClassMember('srlg-table', REFERENCE_CLASS, 'SrlgTable', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'Isis.Instances.Instance.SrlgTable',
                [], [],
                '''                SRLG configuration
                ''',
                'srlg_table',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            _MetaInfoClassMember('nsf', REFERENCE_CLASS, 'Nsf', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'Isis.Instances.Instance.Nsf',
                [], [],
                '''                IS-IS NSF configuration
                ''',
                'nsf',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            _MetaInfoClassMember('link-groups', REFERENCE_CLASS, 'LinkGroups', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'Isis.Instances.Instance.LinkGroups',
                [], [],
                '''                Link Group
                ''',
                'link_groups',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            _MetaInfoClassMember('lsp-check-intervals', REFERENCE_CLASS, 'LspCheckIntervals', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'Isis.Instances.Instance.LspCheckIntervals',
                [], [],
                '''                LSP checksum check interval configuration
                ''',
                'lsp_check_intervals',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            _MetaInfoClassMember('lsp-passwords', REFERENCE_CLASS, 'LspPasswords', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'Isis.Instances.Instance.LspPasswords',
                [], [],
                '''                LSP/SNP password configuration
                ''',
                'lsp_passwords',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            _MetaInfoClassMember('nets', REFERENCE_CLASS, 'Nets', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'Isis.Instances.Instance.Nets',
                [], [],
                '''                NET configuration
                ''',
                'nets',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            _MetaInfoClassMember('lsp-lifetimes', REFERENCE_CLASS, 'LspLifetimes', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'Isis.Instances.Instance.LspLifetimes',
                [], [],
                '''                LSP lifetime configuration
                ''',
                'lsp_lifetimes',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            _MetaInfoClassMember('overload-bits', REFERENCE_CLASS, 'OverloadBits', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'Isis.Instances.Instance.OverloadBits',
                [], [],
                '''                LSP overload-bit configuration
                ''',
                'overload_bits',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            _MetaInfoClassMember('interfaces', REFERENCE_CLASS, 'Interfaces', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'Isis.Instances.Instance.Interfaces',
                [], [],
                '''                Per-interface configuration
                ''',
                'interfaces',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            _MetaInfoClassMember('running', ATTRIBUTE, 'Empty', 'empty',
                None, None,
                [], [],
                '''                Flag to indicate that instance should be
                running.  This must be the first object
                created when an IS-IS instance is configured,
                and the last object deleted when it is
                deconfigured.  When this object is deleted,
                the IS-IS instance will exit.
                ''',
                'running',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            _MetaInfoClassMember('log-adjacency-changes', ATTRIBUTE, 'Empty', 'empty',
                None, None,
                [], [],
                '''                Log changes in adjacency state
                ''',
                'log_adjacency_changes',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            _MetaInfoClassMember('ignore-lsp-errors', ATTRIBUTE, 'bool', 'boolean',
                None, None,
                [], [],
                '''                If TRUE, LSPs recieved with bad checksums will
                result in the purging of that LSP from the LSP
                DB. If FALSE or not set, the received LSP will
                just be ignored.
                ''',
                'ignore_lsp_errors',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            _MetaInfoClassMember('is-type', REFERENCE_ENUM_CLASS, 'IsisConfigurableLevels', 'Isis-configurable-levels',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'IsisConfigurableLevels',
                [], [],
                '''                IS type of the IS-IS process
                ''',
                'is_type',
                'Cisco-IOS-XR-clns-isis-cfg', False, default_value='Cisco_IOS_XR_clns_isis_cfg.IsisConfigurableLevels.level1_and2'),
            _MetaInfoClassMember('tracing-mode', REFERENCE_ENUM_CLASS, 'IsisTracingMode', 'Isis-tracing-mode',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'IsisTracingMode',
                [], [],
                '''                Tracing mode configuration
                ''',
                'tracing_mode',
                'Cisco-IOS-XR-clns-isis-cfg', False, default_value='Cisco_IOS_XR_clns_isis_cfg.IsisTracingMode.basic'),
            _MetaInfoClassMember('vrf-context', ATTRIBUTE, 'str', 'xr:Cisco-ios-xr-string',
                None, None,
                [(1, 32)], [],
                '''                VRF context for ISIS process
                ''',
                'vrf_context',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            _MetaInfoClassMember('instance-id', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('0', '65535')], [],
                '''                Instance ID of the IS-IS process
                ''',
                'instance_id',
                'Cisco-IOS-XR-clns-isis-cfg', False, default_value="0"),
            _MetaInfoClassMember('dynamic-host-name', ATTRIBUTE, 'bool', 'boolean',
                None, None,
                [], [],
                '''                If TRUE, dynamic hostname resolution is
                disabled, and system IDs will always be
                displayed by show and debug output.
                ''',
                'dynamic_host_name',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            _MetaInfoClassMember('purge-transmit-strict', REFERENCE_ENUM_CLASS, 'IsisConfigurableLevel', 'Isis-configurable-level',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'IsisConfigurableLevel',
                [], [],
                '''                Allow only authentication TLV in purge LSPs
                ''',
                'purge_transmit_strict',
                'Cisco-IOS-XR-clns-isis-cfg', False, default_value='Cisco_IOS_XR_clns_isis_cfg.IsisConfigurableLevel.level_12'),
            _MetaInfoClassMember('nsr', ATTRIBUTE, 'Empty', 'empty',
                None, None,
                [], [],
                '''                IS-IS NSR configuration
                ''',
                'nsr',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            _MetaInfoClassMember('log-pdu-drops', ATTRIBUTE, 'Empty', 'empty',
                None, None,
                [], [],
                '''                Log PDU drops
                ''',
                'log_pdu_drops',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            ],
            'Cisco-IOS-XR-clns-isis-cfg',
            'instance',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-clns-isis-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg',
        ),
    },
    'Isis.Instances' : {
        'meta_info' : _MetaInfoClass('Isis.Instances', REFERENCE_CLASS,
            '''IS-IS instance configuration''',
            False, 
            [
            _MetaInfoClassMember('instance', REFERENCE_LIST, 'Instance', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'Isis.Instances.Instance',
                [], [],
                '''                Configuration for a single IS-IS instance
                ''',
                'instance',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            ],
            'Cisco-IOS-XR-clns-isis-cfg',
            'instances',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-clns-isis-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg',
        ),
    },
    'Isis' : {
        'meta_info' : _MetaInfoClass('Isis', REFERENCE_CLASS,
            '''IS-IS configuration for all instances''',
            False, 
            [
            _MetaInfoClassMember('instances', REFERENCE_CLASS, 'Instances', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'Isis.Instances',
                [], [],
                '''                IS-IS instance configuration
                ''',
                'instances',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            ],
            'Cisco-IOS-XR-clns-isis-cfg',
            'isis',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-clns-isis-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg',
        ),
    },
}
_meta_table['Isis.Instances.Instance.LspGenerationIntervals.LspGenerationInterval']['meta_info'].parent =_meta_table['Isis.Instances.Instance.LspGenerationIntervals']['meta_info']
_meta_table['Isis.Instances.Instance.LspArrivalTimes.LspArrivalTime']['meta_info'].parent =_meta_table['Isis.Instances.Instance.LspArrivalTimes']['meta_info']
_meta_table['Isis.Instances.Instance.MaxLinkMetrics.MaxLinkMetric']['meta_info'].parent =_meta_table['Isis.Instances.Instance.MaxLinkMetrics']['meta_info']
_meta_table['Isis.Instances.Instance.Afs.Af.AfData.SegmentRouting.Srv6.Srv6Locators.Srv6Locator']['meta_info'].parent =_meta_table['Isis.Instances.Instance.Afs.Af.AfData.SegmentRouting.Srv6.Srv6Locators']['meta_info']
_meta_table['Isis.Instances.Instance.Afs.Af.AfData.SegmentRouting.Srv6.Srv6Locators']['meta_info'].parent =_meta_table['Isis.Instances.Instance.Afs.Af.AfData.SegmentRouting.Srv6']['meta_info']
_meta_table['Isis.Instances.Instance.Afs.Af.AfData.SegmentRouting.ConnectedPrefixSids.ConnectedPrefixSid']['meta_info'].parent =_meta_table['Isis.Instances.Instance.Afs.Af.AfData.SegmentRouting.ConnectedPrefixSids']['meta_info']
_meta_table['Isis.Instances.Instance.Afs.Af.AfData.SegmentRouting.Srv6']['meta_info'].parent =_meta_table['Isis.Instances.Instance.Afs.Af.AfData.SegmentRouting']['meta_info']
_meta_table['Isis.Instances.Instance.Afs.Af.AfData.SegmentRouting.ConnectedPrefixSids']['meta_info'].parent =_meta_table['Isis.Instances.Instance.Afs.Af.AfData.SegmentRouting']['meta_info']
_meta_table['Isis.Instances.Instance.Afs.Af.AfData.SegmentRouting.PrefixSidMap']['meta_info'].parent =_meta_table['Isis.Instances.Instance.Afs.Af.AfData.SegmentRouting']['meta_info']
_meta_table['Isis.Instances.Instance.Afs.Af.AfData.MetricStyles.MetricStyle']['meta_info'].parent =_meta_table['Isis.Instances.Instance.Afs.Af.AfData.MetricStyles']['meta_info']
_meta_table['Isis.Instances.Instance.Afs.Af.AfData.FrrTable.FrrLoadSharings.FrrLoadSharing']['meta_info'].parent =_meta_table['Isis.Instances.Instance.Afs.Af.AfData.FrrTable.FrrLoadSharings']['meta_info']
_meta_table['Isis.Instances.Instance.Afs.Af.AfData.FrrTable.FrrsrlgProtectionTypes.FrrsrlgProtectionType']['meta_info'].parent =_meta_table['Isis.Instances.Instance.Afs.Af.AfData.FrrTable.FrrsrlgProtectionTypes']['meta_info']
_meta_table['Isis.Instances.Instance.Afs.Af.AfData.FrrTable.PriorityLimits.PriorityLimit']['meta_info'].parent =_meta_table['Isis.Instances.Instance.Afs.Af.AfData.FrrTable.PriorityLimits']['meta_info']
_meta_table['Isis.Instances.Instance.Afs.Af.AfData.FrrTable.FrrRemoteLfaPrefixes.FrrRemoteLfaPrefix']['meta_info'].parent =_meta_table['Isis.Instances.Instance.Afs.Af.AfData.FrrTable.FrrRemoteLfaPrefixes']['meta_info']
_meta_table['Isis.Instances.Instance.Afs.Af.AfData.FrrTable.FrrTiebreakers.FrrTiebreaker']['meta_info'].parent =_meta_table['Isis.Instances.Instance.Afs.Af.AfData.FrrTable.FrrTiebreakers']['meta_info']
_meta_table['Isis.Instances.Instance.Afs.Af.AfData.FrrTable.FrrUseCandOnlies.FrrUseCandOnly']['meta_info'].parent =_meta_table['Isis.Instances.Instance.Afs.Af.AfData.FrrTable.FrrUseCandOnlies']['meta_info']
_meta_table['Isis.Instances.Instance.Afs.Af.AfData.FrrTable.FrrLoadSharings']['meta_info'].parent =_meta_table['Isis.Instances.Instance.Afs.Af.AfData.FrrTable']['meta_info']
_meta_table['Isis.Instances.Instance.Afs.Af.AfData.FrrTable.FrrsrlgProtectionTypes']['meta_info'].parent =_meta_table['Isis.Instances.Instance.Afs.Af.AfData.FrrTable']['meta_info']
_meta_table['Isis.Instances.Instance.Afs.Af.AfData.FrrTable.PriorityLimits']['meta_info'].parent =_meta_table['Isis.Instances.Instance.Afs.Af.AfData.FrrTable']['meta_info']
_meta_table['Isis.Instances.Instance.Afs.Af.AfData.FrrTable.FrrRemoteLfaPrefixes']['meta_info'].parent =_meta_table['Isis.Instances.Instance.Afs.Af.AfData.FrrTable']['meta_info']
_meta_table['Isis.Instances.Instance.Afs.Af.AfData.FrrTable.FrrTiebreakers']['meta_info'].parent =_meta_table['Isis.Instances.Instance.Afs.Af.AfData.FrrTable']['meta_info']
_meta_table['Isis.Instances.Instance.Afs.Af.AfData.FrrTable.FrrUseCandOnlies']['meta_info'].parent =_meta_table['Isis.Instances.Instance.Afs.Af.AfData.FrrTable']['meta_info']
_meta_table['Isis.Instances.Instance.Afs.Af.AfData.SpfPrefixPriorities.SpfPrefixPriority']['meta_info'].parent =_meta_table['Isis.Instances.Instance.Afs.Af.AfData.SpfPrefixPriorities']['meta_info']
_meta_table['Isis.Instances.Instance.Afs.Af.AfData.SummaryPrefixes.SummaryPrefix']['meta_info'].parent =_meta_table['Isis.Instances.Instance.Afs.Af.AfData.SummaryPrefixes']['meta_info']
_meta_table['Isis.Instances.Instance.Afs.Af.AfData.Ucmp.ExcludeInterfaces.ExcludeInterface']['meta_info'].parent =_meta_table['Isis.Instances.Instance.Afs.Af.AfData.Ucmp.ExcludeInterfaces']['meta_info']
_meta_table['Isis.Instances.Instance.Afs.Af.AfData.Ucmp.Enable']['meta_info'].parent =_meta_table['Isis.Instances.Instance.Afs.Af.AfData.Ucmp']['meta_info']
_meta_table['Isis.Instances.Instance.Afs.Af.AfData.Ucmp.ExcludeInterfaces']['meta_info'].parent =_meta_table['Isis.Instances.Instance.Afs.Af.AfData.Ucmp']['meta_info']
_meta_table['Isis.Instances.Instance.Afs.Af.AfData.MaxRedistPrefixes.MaxRedistPrefix']['meta_info'].parent =_meta_table['Isis.Instances.Instance.Afs.Af.AfData.MaxRedistPrefixes']['meta_info']
_meta_table['Isis.Instances.Instance.Afs.Af.AfData.Propagations.Propagation']['meta_info'].parent =_meta_table['Isis.Instances.Instance.Afs.Af.AfData.Propagations']['meta_info']
_meta_table['Isis.Instances.Instance.Afs.Af.AfData.Redistributions.Redistribution.ConnectedOrStaticOrRipOrSubscriberOrMobile']['meta_info'].parent =_meta_table['Isis.Instances.Instance.Afs.Af.AfData.Redistributions.Redistribution']['meta_info']
_meta_table['Isis.Instances.Instance.Afs.Af.AfData.Redistributions.Redistribution.OspfOrOspfv3OrIsisOrApplication']['meta_info'].parent =_meta_table['Isis.Instances.Instance.Afs.Af.AfData.Redistributions.Redistribution']['meta_info']
_meta_table['Isis.Instances.Instance.Afs.Af.AfData.Redistributions.Redistribution.Bgp']['meta_info'].parent =_meta_table['Isis.Instances.Instance.Afs.Af.AfData.Redistributions.Redistribution']['meta_info']
_meta_table['Isis.Instances.Instance.Afs.Af.AfData.Redistributions.Redistribution.Eigrp']['meta_info'].parent =_meta_table['Isis.Instances.Instance.Afs.Af.AfData.Redistributions.Redistribution']['meta_info']
_meta_table['Isis.Instances.Instance.Afs.Af.AfData.Redistributions.Redistribution']['meta_info'].parent =_meta_table['Isis.Instances.Instance.Afs.Af.AfData.Redistributions']['meta_info']
_meta_table['Isis.Instances.Instance.Afs.Af.AfData.ApplicationTables.ApplicationTable.AttributeTable']['meta_info'].parent =_meta_table['Isis.Instances.Instance.Afs.Af.AfData.ApplicationTables.ApplicationTable']['meta_info']
_meta_table['Isis.Instances.Instance.Afs.Af.AfData.ApplicationTables.ApplicationTable']['meta_info'].parent =_meta_table['Isis.Instances.Instance.Afs.Af.AfData.ApplicationTables']['meta_info']
_meta_table['Isis.Instances.Instance.Afs.Af.AfData.SpfPeriodicIntervals.SpfPeriodicInterval']['meta_info'].parent =_meta_table['Isis.Instances.Instance.Afs.Af.AfData.SpfPeriodicIntervals']['meta_info']
_meta_table['Isis.Instances.Instance.Afs.Af.AfData.SpfIntervals.SpfInterval']['meta_info'].parent =_meta_table['Isis.Instances.Instance.Afs.Af.AfData.SpfIntervals']['meta_info']
_meta_table['Isis.Instances.Instance.Afs.Af.AfData.AdminDistances.AdminDistance']['meta_info'].parent =_meta_table['Isis.Instances.Instance.Afs.Af.AfData.AdminDistances']['meta_info']
_meta_table['Isis.Instances.Instance.Afs.Af.AfData.Ispf.States.State']['meta_info'].parent =_meta_table['Isis.Instances.Instance.Afs.Af.AfData.Ispf.States']['meta_info']
_meta_table['Isis.Instances.Instance.Afs.Af.AfData.Ispf.States']['meta_info'].parent =_meta_table['Isis.Instances.Instance.Afs.Af.AfData.Ispf']['meta_info']
_meta_table['Isis.Instances.Instance.Afs.Af.AfData.Mpls.RouterId']['meta_info'].parent =_meta_table['Isis.Instances.Instance.Afs.Af.AfData.Mpls']['meta_info']
_meta_table['Isis.Instances.Instance.Afs.Af.AfData.Mpls.Level']['meta_info'].parent =_meta_table['Isis.Instances.Instance.Afs.Af.AfData.Mpls']['meta_info']
_meta_table['Isis.Instances.Instance.Afs.Af.AfData.ManualAdjSids.ManualAdjSid']['meta_info'].parent =_meta_table['Isis.Instances.Instance.Afs.Af.AfData.ManualAdjSids']['meta_info']
_meta_table['Isis.Instances.Instance.Afs.Af.AfData.Metrics.Metric']['meta_info'].parent =_meta_table['Isis.Instances.Instance.Afs.Af.AfData.Metrics']['meta_info']
_meta_table['Isis.Instances.Instance.Afs.Af.AfData.Weights.Weight']['meta_info'].parent =_meta_table['Isis.Instances.Instance.Afs.Af.AfData.Weights']['meta_info']
_meta_table['Isis.Instances.Instance.Afs.Af.AfData.SegmentRouting']['meta_info'].parent =_meta_table['Isis.Instances.Instance.Afs.Af.AfData']['meta_info']
_meta_table['Isis.Instances.Instance.Afs.Af.AfData.MetricStyles']['meta_info'].parent =_meta_table['Isis.Instances.Instance.Afs.Af.AfData']['meta_info']
_meta_table['Isis.Instances.Instance.Afs.Af.AfData.FrrTable']['meta_info'].parent =_meta_table['Isis.Instances.Instance.Afs.Af.AfData']['meta_info']
_meta_table['Isis.Instances.Instance.Afs.Af.AfData.RouterId']['meta_info'].parent =_meta_table['Isis.Instances.Instance.Afs.Af.AfData']['meta_info']
_meta_table['Isis.Instances.Instance.Afs.Af.AfData.SpfPrefixPriorities']['meta_info'].parent =_meta_table['Isis.Instances.Instance.Afs.Af.AfData']['meta_info']
_meta_table['Isis.Instances.Instance.Afs.Af.AfData.SummaryPrefixes']['meta_info'].parent =_meta_table['Isis.Instances.Instance.Afs.Af.AfData']['meta_info']
_meta_table['Isis.Instances.Instance.Afs.Af.AfData.MicroLoopAvoidance']['meta_info'].parent =_meta_table['Isis.Instances.Instance.Afs.Af.AfData']['meta_info']
_meta_table['Isis.Instances.Instance.Afs.Af.AfData.Ucmp']['meta_info'].parent =_meta_table['Isis.Instances.Instance.Afs.Af.AfData']['meta_info']
_meta_table['Isis.Instances.Instance.Afs.Af.AfData.MaxRedistPrefixes']['meta_info'].parent =_meta_table['Isis.Instances.Instance.Afs.Af.AfData']['meta_info']
_meta_table['Isis.Instances.Instance.Afs.Af.AfData.Propagations']['meta_info'].parent =_meta_table['Isis.Instances.Instance.Afs.Af.AfData']['meta_info']
_meta_table['Isis.Instances.Instance.Afs.Af.AfData.Redistributions']['meta_info'].parent =_meta_table['Isis.Instances.Instance.Afs.Af.AfData']['meta_info']
_meta_table['Isis.Instances.Instance.Afs.Af.AfData.ApplicationTables']['meta_info'].parent =_meta_table['Isis.Instances.Instance.Afs.Af.AfData']['meta_info']
_meta_table['Isis.Instances.Instance.Afs.Af.AfData.SpfPeriodicIntervals']['meta_info'].parent =_meta_table['Isis.Instances.Instance.Afs.Af.AfData']['meta_info']
_meta_table['Isis.Instances.Instance.Afs.Af.AfData.DistributeListIn']['meta_info'].parent =_meta_table['Isis.Instances.Instance.Afs.Af.AfData']['meta_info']
_meta_table['Isis.Instances.Instance.Afs.Af.AfData.SpfIntervals']['meta_info'].parent =_meta_table['Isis.Instances.Instance.Afs.Af.AfData']['meta_info']
_meta_table['Isis.Instances.Instance.Afs.Af.AfData.MonitorConvergence']['meta_info'].parent =_meta_table['Isis.Instances.Instance.Afs.Af.AfData']['meta_info']
_meta_table['Isis.Instances.Instance.Afs.Af.AfData.DefaultInformation']['meta_info'].parent =_meta_table['Isis.Instances.Instance.Afs.Af.AfData']['meta_info']
_meta_table['Isis.Instances.Instance.Afs.Af.AfData.AdminDistances']['meta_info'].parent =_meta_table['Isis.Instances.Instance.Afs.Af.AfData']['meta_info']
_meta_table['Isis.Instances.Instance.Afs.Af.AfData.Ispf']['meta_info'].parent =_meta_table['Isis.Instances.Instance.Afs.Af.AfData']['meta_info']
_meta_table['Isis.Instances.Instance.Afs.Af.AfData.MplsLdpGlobal']['meta_info'].parent =_meta_table['Isis.Instances.Instance.Afs.Af.AfData']['meta_info']
_meta_table['Isis.Instances.Instance.Afs.Af.AfData.Mpls']['meta_info'].parent =_meta_table['Isis.Instances.Instance.Afs.Af.AfData']['meta_info']
_meta_table['Isis.Instances.Instance.Afs.Af.AfData.ManualAdjSids']['meta_info'].parent =_meta_table['Isis.Instances.Instance.Afs.Af.AfData']['meta_info']
_meta_table['Isis.Instances.Instance.Afs.Af.AfData.Metrics']['meta_info'].parent =_meta_table['Isis.Instances.Instance.Afs.Af.AfData']['meta_info']
_meta_table['Isis.Instances.Instance.Afs.Af.AfData.Weights']['meta_info'].parent =_meta_table['Isis.Instances.Instance.Afs.Af.AfData']['meta_info']
_meta_table['Isis.Instances.Instance.Afs.Af.TopologyName.SegmentRouting.Srv6.Srv6Locators.Srv6Locator']['meta_info'].parent =_meta_table['Isis.Instances.Instance.Afs.Af.TopologyName.SegmentRouting.Srv6.Srv6Locators']['meta_info']
_meta_table['Isis.Instances.Instance.Afs.Af.TopologyName.SegmentRouting.Srv6.Srv6Locators']['meta_info'].parent =_meta_table['Isis.Instances.Instance.Afs.Af.TopologyName.SegmentRouting.Srv6']['meta_info']
_meta_table['Isis.Instances.Instance.Afs.Af.TopologyName.SegmentRouting.ConnectedPrefixSids.ConnectedPrefixSid']['meta_info'].parent =_meta_table['Isis.Instances.Instance.Afs.Af.TopologyName.SegmentRouting.ConnectedPrefixSids']['meta_info']
_meta_table['Isis.Instances.Instance.Afs.Af.TopologyName.SegmentRouting.Srv6']['meta_info'].parent =_meta_table['Isis.Instances.Instance.Afs.Af.TopologyName.SegmentRouting']['meta_info']
_meta_table['Isis.Instances.Instance.Afs.Af.TopologyName.SegmentRouting.ConnectedPrefixSids']['meta_info'].parent =_meta_table['Isis.Instances.Instance.Afs.Af.TopologyName.SegmentRouting']['meta_info']
_meta_table['Isis.Instances.Instance.Afs.Af.TopologyName.SegmentRouting.PrefixSidMap']['meta_info'].parent =_meta_table['Isis.Instances.Instance.Afs.Af.TopologyName.SegmentRouting']['meta_info']
_meta_table['Isis.Instances.Instance.Afs.Af.TopologyName.MetricStyles.MetricStyle']['meta_info'].parent =_meta_table['Isis.Instances.Instance.Afs.Af.TopologyName.MetricStyles']['meta_info']
_meta_table['Isis.Instances.Instance.Afs.Af.TopologyName.FrrTable.FrrLoadSharings.FrrLoadSharing']['meta_info'].parent =_meta_table['Isis.Instances.Instance.Afs.Af.TopologyName.FrrTable.FrrLoadSharings']['meta_info']
_meta_table['Isis.Instances.Instance.Afs.Af.TopologyName.FrrTable.FrrsrlgProtectionTypes.FrrsrlgProtectionType']['meta_info'].parent =_meta_table['Isis.Instances.Instance.Afs.Af.TopologyName.FrrTable.FrrsrlgProtectionTypes']['meta_info']
_meta_table['Isis.Instances.Instance.Afs.Af.TopologyName.FrrTable.PriorityLimits.PriorityLimit']['meta_info'].parent =_meta_table['Isis.Instances.Instance.Afs.Af.TopologyName.FrrTable.PriorityLimits']['meta_info']
_meta_table['Isis.Instances.Instance.Afs.Af.TopologyName.FrrTable.FrrRemoteLfaPrefixes.FrrRemoteLfaPrefix']['meta_info'].parent =_meta_table['Isis.Instances.Instance.Afs.Af.TopologyName.FrrTable.FrrRemoteLfaPrefixes']['meta_info']
_meta_table['Isis.Instances.Instance.Afs.Af.TopologyName.FrrTable.FrrTiebreakers.FrrTiebreaker']['meta_info'].parent =_meta_table['Isis.Instances.Instance.Afs.Af.TopologyName.FrrTable.FrrTiebreakers']['meta_info']
_meta_table['Isis.Instances.Instance.Afs.Af.TopologyName.FrrTable.FrrUseCandOnlies.FrrUseCandOnly']['meta_info'].parent =_meta_table['Isis.Instances.Instance.Afs.Af.TopologyName.FrrTable.FrrUseCandOnlies']['meta_info']
_meta_table['Isis.Instances.Instance.Afs.Af.TopologyName.FrrTable.FrrLoadSharings']['meta_info'].parent =_meta_table['Isis.Instances.Instance.Afs.Af.TopologyName.FrrTable']['meta_info']
_meta_table['Isis.Instances.Instance.Afs.Af.TopologyName.FrrTable.FrrsrlgProtectionTypes']['meta_info'].parent =_meta_table['Isis.Instances.Instance.Afs.Af.TopologyName.FrrTable']['meta_info']
_meta_table['Isis.Instances.Instance.Afs.Af.TopologyName.FrrTable.PriorityLimits']['meta_info'].parent =_meta_table['Isis.Instances.Instance.Afs.Af.TopologyName.FrrTable']['meta_info']
_meta_table['Isis.Instances.Instance.Afs.Af.TopologyName.FrrTable.FrrRemoteLfaPrefixes']['meta_info'].parent =_meta_table['Isis.Instances.Instance.Afs.Af.TopologyName.FrrTable']['meta_info']
_meta_table['Isis.Instances.Instance.Afs.Af.TopologyName.FrrTable.FrrTiebreakers']['meta_info'].parent =_meta_table['Isis.Instances.Instance.Afs.Af.TopologyName.FrrTable']['meta_info']
_meta_table['Isis.Instances.Instance.Afs.Af.TopologyName.FrrTable.FrrUseCandOnlies']['meta_info'].parent =_meta_table['Isis.Instances.Instance.Afs.Af.TopologyName.FrrTable']['meta_info']
_meta_table['Isis.Instances.Instance.Afs.Af.TopologyName.SpfPrefixPriorities.SpfPrefixPriority']['meta_info'].parent =_meta_table['Isis.Instances.Instance.Afs.Af.TopologyName.SpfPrefixPriorities']['meta_info']
_meta_table['Isis.Instances.Instance.Afs.Af.TopologyName.SummaryPrefixes.SummaryPrefix']['meta_info'].parent =_meta_table['Isis.Instances.Instance.Afs.Af.TopologyName.SummaryPrefixes']['meta_info']
_meta_table['Isis.Instances.Instance.Afs.Af.TopologyName.Ucmp.ExcludeInterfaces.ExcludeInterface']['meta_info'].parent =_meta_table['Isis.Instances.Instance.Afs.Af.TopologyName.Ucmp.ExcludeInterfaces']['meta_info']
_meta_table['Isis.Instances.Instance.Afs.Af.TopologyName.Ucmp.Enable']['meta_info'].parent =_meta_table['Isis.Instances.Instance.Afs.Af.TopologyName.Ucmp']['meta_info']
_meta_table['Isis.Instances.Instance.Afs.Af.TopologyName.Ucmp.ExcludeInterfaces']['meta_info'].parent =_meta_table['Isis.Instances.Instance.Afs.Af.TopologyName.Ucmp']['meta_info']
_meta_table['Isis.Instances.Instance.Afs.Af.TopologyName.MaxRedistPrefixes.MaxRedistPrefix']['meta_info'].parent =_meta_table['Isis.Instances.Instance.Afs.Af.TopologyName.MaxRedistPrefixes']['meta_info']
_meta_table['Isis.Instances.Instance.Afs.Af.TopologyName.Propagations.Propagation']['meta_info'].parent =_meta_table['Isis.Instances.Instance.Afs.Af.TopologyName.Propagations']['meta_info']
_meta_table['Isis.Instances.Instance.Afs.Af.TopologyName.Redistributions.Redistribution.ConnectedOrStaticOrRipOrSubscriberOrMobile']['meta_info'].parent =_meta_table['Isis.Instances.Instance.Afs.Af.TopologyName.Redistributions.Redistribution']['meta_info']
_meta_table['Isis.Instances.Instance.Afs.Af.TopologyName.Redistributions.Redistribution.OspfOrOspfv3OrIsisOrApplication']['meta_info'].parent =_meta_table['Isis.Instances.Instance.Afs.Af.TopologyName.Redistributions.Redistribution']['meta_info']
_meta_table['Isis.Instances.Instance.Afs.Af.TopologyName.Redistributions.Redistribution.Bgp']['meta_info'].parent =_meta_table['Isis.Instances.Instance.Afs.Af.TopologyName.Redistributions.Redistribution']['meta_info']
_meta_table['Isis.Instances.Instance.Afs.Af.TopologyName.Redistributions.Redistribution.Eigrp']['meta_info'].parent =_meta_table['Isis.Instances.Instance.Afs.Af.TopologyName.Redistributions.Redistribution']['meta_info']
_meta_table['Isis.Instances.Instance.Afs.Af.TopologyName.Redistributions.Redistribution']['meta_info'].parent =_meta_table['Isis.Instances.Instance.Afs.Af.TopologyName.Redistributions']['meta_info']
_meta_table['Isis.Instances.Instance.Afs.Af.TopologyName.ApplicationTables.ApplicationTable.AttributeTable']['meta_info'].parent =_meta_table['Isis.Instances.Instance.Afs.Af.TopologyName.ApplicationTables.ApplicationTable']['meta_info']
_meta_table['Isis.Instances.Instance.Afs.Af.TopologyName.ApplicationTables.ApplicationTable']['meta_info'].parent =_meta_table['Isis.Instances.Instance.Afs.Af.TopologyName.ApplicationTables']['meta_info']
_meta_table['Isis.Instances.Instance.Afs.Af.TopologyName.SpfPeriodicIntervals.SpfPeriodicInterval']['meta_info'].parent =_meta_table['Isis.Instances.Instance.Afs.Af.TopologyName.SpfPeriodicIntervals']['meta_info']
_meta_table['Isis.Instances.Instance.Afs.Af.TopologyName.SpfIntervals.SpfInterval']['meta_info'].parent =_meta_table['Isis.Instances.Instance.Afs.Af.TopologyName.SpfIntervals']['meta_info']
_meta_table['Isis.Instances.Instance.Afs.Af.TopologyName.AdminDistances.AdminDistance']['meta_info'].parent =_meta_table['Isis.Instances.Instance.Afs.Af.TopologyName.AdminDistances']['meta_info']
_meta_table['Isis.Instances.Instance.Afs.Af.TopologyName.Ispf.States.State']['meta_info'].parent =_meta_table['Isis.Instances.Instance.Afs.Af.TopologyName.Ispf.States']['meta_info']
_meta_table['Isis.Instances.Instance.Afs.Af.TopologyName.Ispf.States']['meta_info'].parent =_meta_table['Isis.Instances.Instance.Afs.Af.TopologyName.Ispf']['meta_info']
_meta_table['Isis.Instances.Instance.Afs.Af.TopologyName.Mpls.RouterId']['meta_info'].parent =_meta_table['Isis.Instances.Instance.Afs.Af.TopologyName.Mpls']['meta_info']
_meta_table['Isis.Instances.Instance.Afs.Af.TopologyName.Mpls.Level']['meta_info'].parent =_meta_table['Isis.Instances.Instance.Afs.Af.TopologyName.Mpls']['meta_info']
_meta_table['Isis.Instances.Instance.Afs.Af.TopologyName.ManualAdjSids.ManualAdjSid']['meta_info'].parent =_meta_table['Isis.Instances.Instance.Afs.Af.TopologyName.ManualAdjSids']['meta_info']
_meta_table['Isis.Instances.Instance.Afs.Af.TopologyName.Metrics.Metric']['meta_info'].parent =_meta_table['Isis.Instances.Instance.Afs.Af.TopologyName.Metrics']['meta_info']
_meta_table['Isis.Instances.Instance.Afs.Af.TopologyName.Weights.Weight']['meta_info'].parent =_meta_table['Isis.Instances.Instance.Afs.Af.TopologyName.Weights']['meta_info']
_meta_table['Isis.Instances.Instance.Afs.Af.TopologyName.SegmentRouting']['meta_info'].parent =_meta_table['Isis.Instances.Instance.Afs.Af.TopologyName']['meta_info']
_meta_table['Isis.Instances.Instance.Afs.Af.TopologyName.MetricStyles']['meta_info'].parent =_meta_table['Isis.Instances.Instance.Afs.Af.TopologyName']['meta_info']
_meta_table['Isis.Instances.Instance.Afs.Af.TopologyName.FrrTable']['meta_info'].parent =_meta_table['Isis.Instances.Instance.Afs.Af.TopologyName']['meta_info']
_meta_table['Isis.Instances.Instance.Afs.Af.TopologyName.RouterId']['meta_info'].parent =_meta_table['Isis.Instances.Instance.Afs.Af.TopologyName']['meta_info']
_meta_table['Isis.Instances.Instance.Afs.Af.TopologyName.SpfPrefixPriorities']['meta_info'].parent =_meta_table['Isis.Instances.Instance.Afs.Af.TopologyName']['meta_info']
_meta_table['Isis.Instances.Instance.Afs.Af.TopologyName.SummaryPrefixes']['meta_info'].parent =_meta_table['Isis.Instances.Instance.Afs.Af.TopologyName']['meta_info']
_meta_table['Isis.Instances.Instance.Afs.Af.TopologyName.MicroLoopAvoidance']['meta_info'].parent =_meta_table['Isis.Instances.Instance.Afs.Af.TopologyName']['meta_info']
_meta_table['Isis.Instances.Instance.Afs.Af.TopologyName.Ucmp']['meta_info'].parent =_meta_table['Isis.Instances.Instance.Afs.Af.TopologyName']['meta_info']
_meta_table['Isis.Instances.Instance.Afs.Af.TopologyName.MaxRedistPrefixes']['meta_info'].parent =_meta_table['Isis.Instances.Instance.Afs.Af.TopologyName']['meta_info']
_meta_table['Isis.Instances.Instance.Afs.Af.TopologyName.Propagations']['meta_info'].parent =_meta_table['Isis.Instances.Instance.Afs.Af.TopologyName']['meta_info']
_meta_table['Isis.Instances.Instance.Afs.Af.TopologyName.Redistributions']['meta_info'].parent =_meta_table['Isis.Instances.Instance.Afs.Af.TopologyName']['meta_info']
_meta_table['Isis.Instances.Instance.Afs.Af.TopologyName.ApplicationTables']['meta_info'].parent =_meta_table['Isis.Instances.Instance.Afs.Af.TopologyName']['meta_info']
_meta_table['Isis.Instances.Instance.Afs.Af.TopologyName.SpfPeriodicIntervals']['meta_info'].parent =_meta_table['Isis.Instances.Instance.Afs.Af.TopologyName']['meta_info']
_meta_table['Isis.Instances.Instance.Afs.Af.TopologyName.DistributeListIn']['meta_info'].parent =_meta_table['Isis.Instances.Instance.Afs.Af.TopologyName']['meta_info']
_meta_table['Isis.Instances.Instance.Afs.Af.TopologyName.SpfIntervals']['meta_info'].parent =_meta_table['Isis.Instances.Instance.Afs.Af.TopologyName']['meta_info']
_meta_table['Isis.Instances.Instance.Afs.Af.TopologyName.MonitorConvergence']['meta_info'].parent =_meta_table['Isis.Instances.Instance.Afs.Af.TopologyName']['meta_info']
_meta_table['Isis.Instances.Instance.Afs.Af.TopologyName.DefaultInformation']['meta_info'].parent =_meta_table['Isis.Instances.Instance.Afs.Af.TopologyName']['meta_info']
_meta_table['Isis.Instances.Instance.Afs.Af.TopologyName.AdminDistances']['meta_info'].parent =_meta_table['Isis.Instances.Instance.Afs.Af.TopologyName']['meta_info']
_meta_table['Isis.Instances.Instance.Afs.Af.TopologyName.Ispf']['meta_info'].parent =_meta_table['Isis.Instances.Instance.Afs.Af.TopologyName']['meta_info']
_meta_table['Isis.Instances.Instance.Afs.Af.TopologyName.MplsLdpGlobal']['meta_info'].parent =_meta_table['Isis.Instances.Instance.Afs.Af.TopologyName']['meta_info']
_meta_table['Isis.Instances.Instance.Afs.Af.TopologyName.Mpls']['meta_info'].parent =_meta_table['Isis.Instances.Instance.Afs.Af.TopologyName']['meta_info']
_meta_table['Isis.Instances.Instance.Afs.Af.TopologyName.ManualAdjSids']['meta_info'].parent =_meta_table['Isis.Instances.Instance.Afs.Af.TopologyName']['meta_info']
_meta_table['Isis.Instances.Instance.Afs.Af.TopologyName.Metrics']['meta_info'].parent =_meta_table['Isis.Instances.Instance.Afs.Af.TopologyName']['meta_info']
_meta_table['Isis.Instances.Instance.Afs.Af.TopologyName.Weights']['meta_info'].parent =_meta_table['Isis.Instances.Instance.Afs.Af.TopologyName']['meta_info']
_meta_table['Isis.Instances.Instance.Afs.Af.AfData']['meta_info'].parent =_meta_table['Isis.Instances.Instance.Afs.Af']['meta_info']
_meta_table['Isis.Instances.Instance.Afs.Af.TopologyName']['meta_info'].parent =_meta_table['Isis.Instances.Instance.Afs.Af']['meta_info']
_meta_table['Isis.Instances.Instance.Afs.Af']['meta_info'].parent =_meta_table['Isis.Instances.Instance.Afs']['meta_info']
_meta_table['Isis.Instances.Instance.LspRefreshIntervals.LspRefreshInterval']['meta_info'].parent =_meta_table['Isis.Instances.Instance.LspRefreshIntervals']['meta_info']
_meta_table['Isis.Instances.Instance.FlexAlgos.FlexAlgo.AffinityExcludeAnies']['meta_info'].parent =_meta_table['Isis.Instances.Instance.FlexAlgos.FlexAlgo']['meta_info']
_meta_table['Isis.Instances.Instance.FlexAlgos.FlexAlgo']['meta_info'].parent =_meta_table['Isis.Instances.Instance.FlexAlgos']['meta_info']
_meta_table['Isis.Instances.Instance.AffinityMappings.AffinityMapping']['meta_info'].parent =_meta_table['Isis.Instances.Instance.AffinityMappings']['meta_info']
_meta_table['Isis.Instances.Instance.LspAcceptPasswords.LspAcceptPassword']['meta_info'].parent =_meta_table['Isis.Instances.Instance.LspAcceptPasswords']['meta_info']
_meta_table['Isis.Instances.Instance.LspMtus.LspMtu']['meta_info'].parent =_meta_table['Isis.Instances.Instance.LspMtus']['meta_info']
_meta_table['Isis.Instances.Instance.SrlgTable.SrlgNames.SrlgName.FromTos.FromTo']['meta_info'].parent =_meta_table['Isis.Instances.Instance.SrlgTable.SrlgNames.SrlgName.FromTos']['meta_info']
_meta_table['Isis.Instances.Instance.SrlgTable.SrlgNames.SrlgName.FromTos']['meta_info'].parent =_meta_table['Isis.Instances.Instance.SrlgTable.SrlgNames.SrlgName']['meta_info']
_meta_table['Isis.Instances.Instance.SrlgTable.SrlgNames.SrlgName']['meta_info'].parent =_meta_table['Isis.Instances.Instance.SrlgTable.SrlgNames']['meta_info']
_meta_table['Isis.Instances.Instance.SrlgTable.SrlgNames']['meta_info'].parent =_meta_table['Isis.Instances.Instance.SrlgTable']['meta_info']
_meta_table['Isis.Instances.Instance.LinkGroups.LinkGroup']['meta_info'].parent =_meta_table['Isis.Instances.Instance.LinkGroups']['meta_info']
_meta_table['Isis.Instances.Instance.LspCheckIntervals.LspCheckInterval']['meta_info'].parent =_meta_table['Isis.Instances.Instance.LspCheckIntervals']['meta_info']
_meta_table['Isis.Instances.Instance.LspPasswords.LspPassword']['meta_info'].parent =_meta_table['Isis.Instances.Instance.LspPasswords']['meta_info']
_meta_table['Isis.Instances.Instance.Nets.Net']['meta_info'].parent =_meta_table['Isis.Instances.Instance.Nets']['meta_info']
_meta_table['Isis.Instances.Instance.LspLifetimes.LspLifetime']['meta_info'].parent =_meta_table['Isis.Instances.Instance.LspLifetimes']['meta_info']
_meta_table['Isis.Instances.Instance.OverloadBits.OverloadBit']['meta_info'].parent =_meta_table['Isis.Instances.Instance.OverloadBits']['meta_info']
_meta_table['Isis.Instances.Instance.Interfaces.Interface.IntAffinityTable.FlexAlgos']['meta_info'].parent =_meta_table['Isis.Instances.Instance.Interfaces.Interface.IntAffinityTable']['meta_info']
_meta_table['Isis.Instances.Instance.Interfaces.Interface.LspRetransmitThrottleIntervals.LspRetransmitThrottleInterval']['meta_info'].parent =_meta_table['Isis.Instances.Instance.Interfaces.Interface.LspRetransmitThrottleIntervals']['meta_info']
_meta_table['Isis.Instances.Instance.Interfaces.Interface.LspRetransmitIntervals.LspRetransmitInterval']['meta_info'].parent =_meta_table['Isis.Instances.Instance.Interfaces.Interface.LspRetransmitIntervals']['meta_info']
_meta_table['Isis.Instances.Instance.Interfaces.Interface.Priorities.Priority']['meta_info'].parent =_meta_table['Isis.Instances.Instance.Interfaces.Interface.Priorities']['meta_info']
_meta_table['Isis.Instances.Instance.Interfaces.Interface.HelloAcceptPasswords.HelloAcceptPassword']['meta_info'].parent =_meta_table['Isis.Instances.Instance.Interfaces.Interface.HelloAcceptPasswords']['meta_info']
_meta_table['Isis.Instances.Instance.Interfaces.Interface.HelloPasswords.HelloPassword']['meta_info'].parent =_meta_table['Isis.Instances.Instance.Interfaces.Interface.HelloPasswords']['meta_info']
_meta_table['Isis.Instances.Instance.Interfaces.Interface.HelloPaddings.HelloPadding']['meta_info'].parent =_meta_table['Isis.Instances.Instance.Interfaces.Interface.HelloPaddings']['meta_info']
_meta_table['Isis.Instances.Instance.Interfaces.Interface.HelloMultipliers.HelloMultiplier']['meta_info'].parent =_meta_table['Isis.Instances.Instance.Interfaces.Interface.HelloMultipliers']['meta_info']
_meta_table['Isis.Instances.Instance.Interfaces.Interface.LspFastFloodThresholds.LspFastFloodThreshold']['meta_info'].parent =_meta_table['Isis.Instances.Instance.Interfaces.Interface.LspFastFloodThresholds']['meta_info']
_meta_table['Isis.Instances.Instance.Interfaces.Interface.PrefixAttributeNFlagClears.PrefixAttributeNFlagClear']['meta_info'].parent =_meta_table['Isis.Instances.Instance.Interfaces.Interface.PrefixAttributeNFlagClears']['meta_info']
_meta_table['Isis.Instances.Instance.Interfaces.Interface.HelloIntervals.HelloInterval']['meta_info'].parent =_meta_table['Isis.Instances.Instance.Interfaces.Interface.HelloIntervals']['meta_info']
_meta_table['Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.InterfaceAfData.InterfaceFrrTable.FrrlfaCandidateInterfaces.FrrlfaCandidateInterface']['meta_info'].parent =_meta_table['Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.InterfaceAfData.InterfaceFrrTable.FrrlfaCandidateInterfaces']['meta_info']
_meta_table['Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.InterfaceAfData.InterfaceFrrTable.FrrRemoteLfaMaxMetrics.FrrRemoteLfaMaxMetric']['meta_info'].parent =_meta_table['Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.InterfaceAfData.InterfaceFrrTable.FrrRemoteLfaMaxMetrics']['meta_info']
_meta_table['Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.InterfaceAfData.InterfaceFrrTable.FrrTypes.FrrType']['meta_info'].parent =_meta_table['Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.InterfaceAfData.InterfaceFrrTable.FrrTypes']['meta_info']
_meta_table['Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.InterfaceAfData.InterfaceFrrTable.FrrRemoteLfaTypes.FrrRemoteLfaType']['meta_info'].parent =_meta_table['Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.InterfaceAfData.InterfaceFrrTable.FrrRemoteLfaTypes']['meta_info']
_meta_table['Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.InterfaceAfData.InterfaceFrrTable.InterfaceFrrTiebreakerDefaults.InterfaceFrrTiebreakerDefault']['meta_info'].parent =_meta_table['Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.InterfaceAfData.InterfaceFrrTable.InterfaceFrrTiebreakerDefaults']['meta_info']
_meta_table['Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.InterfaceAfData.InterfaceFrrTable.FrrtilfaTypes.FrrtilfaType']['meta_info'].parent =_meta_table['Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.InterfaceAfData.InterfaceFrrTable.FrrtilfaTypes']['meta_info']
_meta_table['Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.InterfaceAfData.InterfaceFrrTable.FrrExcludeInterfaces.FrrExcludeInterface']['meta_info'].parent =_meta_table['Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.InterfaceAfData.InterfaceFrrTable.FrrExcludeInterfaces']['meta_info']
_meta_table['Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.InterfaceAfData.InterfaceFrrTable.InterfaceFrrTiebreakers.InterfaceFrrTiebreaker']['meta_info'].parent =_meta_table['Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.InterfaceAfData.InterfaceFrrTable.InterfaceFrrTiebreakers']['meta_info']
_meta_table['Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.InterfaceAfData.InterfaceFrrTable.FrrlfaCandidateInterfaces']['meta_info'].parent =_meta_table['Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.InterfaceAfData.InterfaceFrrTable']['meta_info']
_meta_table['Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.InterfaceAfData.InterfaceFrrTable.FrrRemoteLfaMaxMetrics']['meta_info'].parent =_meta_table['Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.InterfaceAfData.InterfaceFrrTable']['meta_info']
_meta_table['Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.InterfaceAfData.InterfaceFrrTable.FrrTypes']['meta_info'].parent =_meta_table['Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.InterfaceAfData.InterfaceFrrTable']['meta_info']
_meta_table['Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.InterfaceAfData.InterfaceFrrTable.FrrRemoteLfaTypes']['meta_info'].parent =_meta_table['Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.InterfaceAfData.InterfaceFrrTable']['meta_info']
_meta_table['Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.InterfaceAfData.InterfaceFrrTable.InterfaceFrrTiebreakerDefaults']['meta_info'].parent =_meta_table['Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.InterfaceAfData.InterfaceFrrTable']['meta_info']
_meta_table['Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.InterfaceAfData.InterfaceFrrTable.FrrtilfaTypes']['meta_info'].parent =_meta_table['Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.InterfaceAfData.InterfaceFrrTable']['meta_info']
_meta_table['Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.InterfaceAfData.InterfaceFrrTable.FrrExcludeInterfaces']['meta_info'].parent =_meta_table['Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.InterfaceAfData.InterfaceFrrTable']['meta_info']
_meta_table['Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.InterfaceAfData.InterfaceFrrTable.InterfaceFrrTiebreakers']['meta_info'].parent =_meta_table['Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.InterfaceAfData.InterfaceFrrTable']['meta_info']
_meta_table['Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.InterfaceAfData.AlgorithmPrefixSids.AlgorithmPrefixSid']['meta_info'].parent =_meta_table['Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.InterfaceAfData.AlgorithmPrefixSids']['meta_info']
_meta_table['Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.InterfaceAfData.AutoMetrics.AutoMetric']['meta_info'].parent =_meta_table['Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.InterfaceAfData.AutoMetrics']['meta_info']
_meta_table['Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.InterfaceAfData.AdminTags.AdminTag']['meta_info'].parent =_meta_table['Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.InterfaceAfData.AdminTags']['meta_info']
_meta_table['Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.InterfaceAfData.ManualAdjSids.ManualAdjSid']['meta_info'].parent =_meta_table['Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.InterfaceAfData.ManualAdjSids']['meta_info']
_meta_table['Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.InterfaceAfData.Metrics.Metric']['meta_info'].parent =_meta_table['Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.InterfaceAfData.Metrics']['meta_info']
_meta_table['Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.InterfaceAfData.Weights.Weight']['meta_info'].parent =_meta_table['Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.InterfaceAfData.Weights']['meta_info']
_meta_table['Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.InterfaceAfData.PrefixSid']['meta_info'].parent =_meta_table['Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.InterfaceAfData']['meta_info']
_meta_table['Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.InterfaceAfData.InterfaceFrrTable']['meta_info'].parent =_meta_table['Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.InterfaceAfData']['meta_info']
_meta_table['Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.InterfaceAfData.MplsLdp']['meta_info'].parent =_meta_table['Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.InterfaceAfData']['meta_info']
_meta_table['Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.InterfaceAfData.PrefixSspfsid']['meta_info'].parent =_meta_table['Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.InterfaceAfData']['meta_info']
_meta_table['Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.InterfaceAfData.AlgorithmPrefixSids']['meta_info'].parent =_meta_table['Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.InterfaceAfData']['meta_info']
_meta_table['Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.InterfaceAfData.AutoMetrics']['meta_info'].parent =_meta_table['Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.InterfaceAfData']['meta_info']
_meta_table['Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.InterfaceAfData.AdminTags']['meta_info'].parent =_meta_table['Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.InterfaceAfData']['meta_info']
_meta_table['Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.InterfaceAfData.InterfaceLinkGroup']['meta_info'].parent =_meta_table['Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.InterfaceAfData']['meta_info']
_meta_table['Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.InterfaceAfData.ManualAdjSids']['meta_info'].parent =_meta_table['Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.InterfaceAfData']['meta_info']
_meta_table['Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.InterfaceAfData.Metrics']['meta_info'].parent =_meta_table['Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.InterfaceAfData']['meta_info']
_meta_table['Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.InterfaceAfData.Weights']['meta_info'].parent =_meta_table['Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.InterfaceAfData']['meta_info']
_meta_table['Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.TopologyName.InterfaceFrrTable.FrrlfaCandidateInterfaces.FrrlfaCandidateInterface']['meta_info'].parent =_meta_table['Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.TopologyName.InterfaceFrrTable.FrrlfaCandidateInterfaces']['meta_info']
_meta_table['Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.TopologyName.InterfaceFrrTable.FrrRemoteLfaMaxMetrics.FrrRemoteLfaMaxMetric']['meta_info'].parent =_meta_table['Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.TopologyName.InterfaceFrrTable.FrrRemoteLfaMaxMetrics']['meta_info']
_meta_table['Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.TopologyName.InterfaceFrrTable.FrrTypes.FrrType']['meta_info'].parent =_meta_table['Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.TopologyName.InterfaceFrrTable.FrrTypes']['meta_info']
_meta_table['Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.TopologyName.InterfaceFrrTable.FrrRemoteLfaTypes.FrrRemoteLfaType']['meta_info'].parent =_meta_table['Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.TopologyName.InterfaceFrrTable.FrrRemoteLfaTypes']['meta_info']
_meta_table['Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.TopologyName.InterfaceFrrTable.InterfaceFrrTiebreakerDefaults.InterfaceFrrTiebreakerDefault']['meta_info'].parent =_meta_table['Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.TopologyName.InterfaceFrrTable.InterfaceFrrTiebreakerDefaults']['meta_info']
_meta_table['Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.TopologyName.InterfaceFrrTable.FrrtilfaTypes.FrrtilfaType']['meta_info'].parent =_meta_table['Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.TopologyName.InterfaceFrrTable.FrrtilfaTypes']['meta_info']
_meta_table['Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.TopologyName.InterfaceFrrTable.FrrExcludeInterfaces.FrrExcludeInterface']['meta_info'].parent =_meta_table['Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.TopologyName.InterfaceFrrTable.FrrExcludeInterfaces']['meta_info']
_meta_table['Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.TopologyName.InterfaceFrrTable.InterfaceFrrTiebreakers.InterfaceFrrTiebreaker']['meta_info'].parent =_meta_table['Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.TopologyName.InterfaceFrrTable.InterfaceFrrTiebreakers']['meta_info']
_meta_table['Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.TopologyName.InterfaceFrrTable.FrrlfaCandidateInterfaces']['meta_info'].parent =_meta_table['Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.TopologyName.InterfaceFrrTable']['meta_info']
_meta_table['Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.TopologyName.InterfaceFrrTable.FrrRemoteLfaMaxMetrics']['meta_info'].parent =_meta_table['Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.TopologyName.InterfaceFrrTable']['meta_info']
_meta_table['Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.TopologyName.InterfaceFrrTable.FrrTypes']['meta_info'].parent =_meta_table['Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.TopologyName.InterfaceFrrTable']['meta_info']
_meta_table['Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.TopologyName.InterfaceFrrTable.FrrRemoteLfaTypes']['meta_info'].parent =_meta_table['Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.TopologyName.InterfaceFrrTable']['meta_info']
_meta_table['Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.TopologyName.InterfaceFrrTable.InterfaceFrrTiebreakerDefaults']['meta_info'].parent =_meta_table['Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.TopologyName.InterfaceFrrTable']['meta_info']
_meta_table['Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.TopologyName.InterfaceFrrTable.FrrtilfaTypes']['meta_info'].parent =_meta_table['Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.TopologyName.InterfaceFrrTable']['meta_info']
_meta_table['Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.TopologyName.InterfaceFrrTable.FrrExcludeInterfaces']['meta_info'].parent =_meta_table['Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.TopologyName.InterfaceFrrTable']['meta_info']
_meta_table['Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.TopologyName.InterfaceFrrTable.InterfaceFrrTiebreakers']['meta_info'].parent =_meta_table['Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.TopologyName.InterfaceFrrTable']['meta_info']
_meta_table['Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.TopologyName.AlgorithmPrefixSids.AlgorithmPrefixSid']['meta_info'].parent =_meta_table['Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.TopologyName.AlgorithmPrefixSids']['meta_info']
_meta_table['Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.TopologyName.AutoMetrics.AutoMetric']['meta_info'].parent =_meta_table['Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.TopologyName.AutoMetrics']['meta_info']
_meta_table['Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.TopologyName.AdminTags.AdminTag']['meta_info'].parent =_meta_table['Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.TopologyName.AdminTags']['meta_info']
_meta_table['Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.TopologyName.ManualAdjSids.ManualAdjSid']['meta_info'].parent =_meta_table['Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.TopologyName.ManualAdjSids']['meta_info']
_meta_table['Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.TopologyName.Metrics.Metric']['meta_info'].parent =_meta_table['Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.TopologyName.Metrics']['meta_info']
_meta_table['Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.TopologyName.Weights.Weight']['meta_info'].parent =_meta_table['Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.TopologyName.Weights']['meta_info']
_meta_table['Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.TopologyName.PrefixSid']['meta_info'].parent =_meta_table['Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.TopologyName']['meta_info']
_meta_table['Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.TopologyName.InterfaceFrrTable']['meta_info'].parent =_meta_table['Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.TopologyName']['meta_info']
_meta_table['Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.TopologyName.MplsLdp']['meta_info'].parent =_meta_table['Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.TopologyName']['meta_info']
_meta_table['Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.TopologyName.PrefixSspfsid']['meta_info'].parent =_meta_table['Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.TopologyName']['meta_info']
_meta_table['Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.TopologyName.AlgorithmPrefixSids']['meta_info'].parent =_meta_table['Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.TopologyName']['meta_info']
_meta_table['Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.TopologyName.AutoMetrics']['meta_info'].parent =_meta_table['Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.TopologyName']['meta_info']
_meta_table['Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.TopologyName.AdminTags']['meta_info'].parent =_meta_table['Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.TopologyName']['meta_info']
_meta_table['Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.TopologyName.InterfaceLinkGroup']['meta_info'].parent =_meta_table['Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.TopologyName']['meta_info']
_meta_table['Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.TopologyName.ManualAdjSids']['meta_info'].parent =_meta_table['Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.TopologyName']['meta_info']
_meta_table['Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.TopologyName.Metrics']['meta_info'].parent =_meta_table['Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.TopologyName']['meta_info']
_meta_table['Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.TopologyName.Weights']['meta_info'].parent =_meta_table['Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.TopologyName']['meta_info']
_meta_table['Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.InterfaceAfData']['meta_info'].parent =_meta_table['Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf']['meta_info']
_meta_table['Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.TopologyName']['meta_info'].parent =_meta_table['Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf']['meta_info']
_meta_table['Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf']['meta_info'].parent =_meta_table['Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs']['meta_info']
_meta_table['Isis.Instances.Instance.Interfaces.Interface.CsnpIntervals.CsnpInterval']['meta_info'].parent =_meta_table['Isis.Instances.Instance.Interfaces.Interface.CsnpIntervals']['meta_info']
_meta_table['Isis.Instances.Instance.Interfaces.Interface.LspIntervals.LspInterval']['meta_info'].parent =_meta_table['Isis.Instances.Instance.Interfaces.Interface.LspIntervals']['meta_info']
_meta_table['Isis.Instances.Instance.Interfaces.Interface.IntAffinityTable']['meta_info'].parent =_meta_table['Isis.Instances.Instance.Interfaces.Interface']['meta_info']
_meta_table['Isis.Instances.Instance.Interfaces.Interface.LspRetransmitThrottleIntervals']['meta_info'].parent =_meta_table['Isis.Instances.Instance.Interfaces.Interface']['meta_info']
_meta_table['Isis.Instances.Instance.Interfaces.Interface.LspRetransmitIntervals']['meta_info'].parent =_meta_table['Isis.Instances.Instance.Interfaces.Interface']['meta_info']
_meta_table['Isis.Instances.Instance.Interfaces.Interface.Bfd']['meta_info'].parent =_meta_table['Isis.Instances.Instance.Interfaces.Interface']['meta_info']
_meta_table['Isis.Instances.Instance.Interfaces.Interface.Priorities']['meta_info'].parent =_meta_table['Isis.Instances.Instance.Interfaces.Interface']['meta_info']
_meta_table['Isis.Instances.Instance.Interfaces.Interface.HelloAcceptPasswords']['meta_info'].parent =_meta_table['Isis.Instances.Instance.Interfaces.Interface']['meta_info']
_meta_table['Isis.Instances.Instance.Interfaces.Interface.HelloPasswords']['meta_info'].parent =_meta_table['Isis.Instances.Instance.Interfaces.Interface']['meta_info']
_meta_table['Isis.Instances.Instance.Interfaces.Interface.HelloPaddings']['meta_info'].parent =_meta_table['Isis.Instances.Instance.Interfaces.Interface']['meta_info']
_meta_table['Isis.Instances.Instance.Interfaces.Interface.HelloMultipliers']['meta_info'].parent =_meta_table['Isis.Instances.Instance.Interfaces.Interface']['meta_info']
_meta_table['Isis.Instances.Instance.Interfaces.Interface.LspFastFloodThresholds']['meta_info'].parent =_meta_table['Isis.Instances.Instance.Interfaces.Interface']['meta_info']
_meta_table['Isis.Instances.Instance.Interfaces.Interface.PrefixAttributeNFlagClears']['meta_info'].parent =_meta_table['Isis.Instances.Instance.Interfaces.Interface']['meta_info']
_meta_table['Isis.Instances.Instance.Interfaces.Interface.HelloIntervals']['meta_info'].parent =_meta_table['Isis.Instances.Instance.Interfaces.Interface']['meta_info']
_meta_table['Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs']['meta_info'].parent =_meta_table['Isis.Instances.Instance.Interfaces.Interface']['meta_info']
_meta_table['Isis.Instances.Instance.Interfaces.Interface.CsnpIntervals']['meta_info'].parent =_meta_table['Isis.Instances.Instance.Interfaces.Interface']['meta_info']
_meta_table['Isis.Instances.Instance.Interfaces.Interface.LspIntervals']['meta_info'].parent =_meta_table['Isis.Instances.Instance.Interfaces.Interface']['meta_info']
_meta_table['Isis.Instances.Instance.Interfaces.Interface']['meta_info'].parent =_meta_table['Isis.Instances.Instance.Interfaces']['meta_info']
_meta_table['Isis.Instances.Instance.Srgb']['meta_info'].parent =_meta_table['Isis.Instances.Instance']['meta_info']
_meta_table['Isis.Instances.Instance.LspGenerationIntervals']['meta_info'].parent =_meta_table['Isis.Instances.Instance']['meta_info']
_meta_table['Isis.Instances.Instance.LspArrivalTimes']['meta_info'].parent =_meta_table['Isis.Instances.Instance']['meta_info']
_meta_table['Isis.Instances.Instance.TraceBufferSize']['meta_info'].parent =_meta_table['Isis.Instances.Instance']['meta_info']
_meta_table['Isis.Instances.Instance.MaxLinkMetrics']['meta_info'].parent =_meta_table['Isis.Instances.Instance']['meta_info']
_meta_table['Isis.Instances.Instance.AdjacencyStagger']['meta_info'].parent =_meta_table['Isis.Instances.Instance']['meta_info']
_meta_table['Isis.Instances.Instance.Afs']['meta_info'].parent =_meta_table['Isis.Instances.Instance']['meta_info']
_meta_table['Isis.Instances.Instance.LspRefreshIntervals']['meta_info'].parent =_meta_table['Isis.Instances.Instance']['meta_info']
_meta_table['Isis.Instances.Instance.Distribute']['meta_info'].parent =_meta_table['Isis.Instances.Instance']['meta_info']
_meta_table['Isis.Instances.Instance.FlexAlgos']['meta_info'].parent =_meta_table['Isis.Instances.Instance']['meta_info']
_meta_table['Isis.Instances.Instance.AffinityMappings']['meta_info'].parent =_meta_table['Isis.Instances.Instance']['meta_info']
_meta_table['Isis.Instances.Instance.LspAcceptPasswords']['meta_info'].parent =_meta_table['Isis.Instances.Instance']['meta_info']
_meta_table['Isis.Instances.Instance.LspMtus']['meta_info'].parent =_meta_table['Isis.Instances.Instance']['meta_info']
_meta_table['Isis.Instances.Instance.SrlgTable']['meta_info'].parent =_meta_table['Isis.Instances.Instance']['meta_info']
_meta_table['Isis.Instances.Instance.Nsf']['meta_info'].parent =_meta_table['Isis.Instances.Instance']['meta_info']
_meta_table['Isis.Instances.Instance.LinkGroups']['meta_info'].parent =_meta_table['Isis.Instances.Instance']['meta_info']
_meta_table['Isis.Instances.Instance.LspCheckIntervals']['meta_info'].parent =_meta_table['Isis.Instances.Instance']['meta_info']
_meta_table['Isis.Instances.Instance.LspPasswords']['meta_info'].parent =_meta_table['Isis.Instances.Instance']['meta_info']
_meta_table['Isis.Instances.Instance.Nets']['meta_info'].parent =_meta_table['Isis.Instances.Instance']['meta_info']
_meta_table['Isis.Instances.Instance.LspLifetimes']['meta_info'].parent =_meta_table['Isis.Instances.Instance']['meta_info']
_meta_table['Isis.Instances.Instance.OverloadBits']['meta_info'].parent =_meta_table['Isis.Instances.Instance']['meta_info']
_meta_table['Isis.Instances.Instance.Interfaces']['meta_info'].parent =_meta_table['Isis.Instances.Instance']['meta_info']
_meta_table['Isis.Instances.Instance']['meta_info'].parent =_meta_table['Isis.Instances']['meta_info']
_meta_table['Isis.Instances']['meta_info'].parent =_meta_table['Isis']['meta_info']
