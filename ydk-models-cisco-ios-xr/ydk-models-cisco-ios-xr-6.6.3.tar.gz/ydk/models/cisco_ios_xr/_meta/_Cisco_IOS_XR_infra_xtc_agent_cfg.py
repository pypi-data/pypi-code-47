
'''
This is auto-generated file,
which includes metadata for module Cisco_IOS_XR_infra_xtc_agent_cfg
'''

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_LIST, REFERENCE_LEAFLIST, REFERENCE_BITS, REFERENCE_UNION
from ydk._core._dm_meta_info import REFERENCE_CLASS, REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, ANYXML_CLASS
from ydk._core._importer import _yang_ns

_meta_table = {
    'XtcMetricValue' : _MetaInfoEnum('XtcMetricValue',
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_agent_cfg', 'XtcMetricValue',
        '''Xtc metric value''',
        {
            'relative':'relative',
            'absolute':'absolute',
        }, 'Cisco-IOS-XR-infra-xtc-agent-cfg', _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-infra-xtc-agent-cfg']),
    'XtcAffinityRule' : _MetaInfoEnum('XtcAffinityRule',
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_agent_cfg', 'XtcAffinityRule',
        '''Xtc affinity rule''',
        {
            'affinity-include-all':'affinity_include_all',
            'affinity-exclude-any':'affinity_exclude_any',
            'affinity-include-any':'affinity_include_any',
        }, 'Cisco-IOS-XR-infra-xtc-agent-cfg', _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-infra-xtc-agent-cfg']),
    'XtcEndPoint' : _MetaInfoEnum('XtcEndPoint',
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_agent_cfg', 'XtcEndPoint',
        '''Xtc end point''',
        {
            'end-point-type-ipv4':'end_point_type_ipv4',
            'end-point-type-ipv6':'end_point_type_ipv6',
        }, 'Cisco-IOS-XR-infra-xtc-agent-cfg', _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-infra-xtc-agent-cfg']),
    'XtcBindingSidexplicitRule' : _MetaInfoEnum('XtcBindingSidexplicitRule',
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_agent_cfg', 'XtcBindingSidexplicitRule',
        '''Xtc binding sidexplicit rule''',
        {
            'fallback-dynamic':'fallback_dynamic',
            'enforce-srlb':'enforce_srlb',
        }, 'Cisco-IOS-XR-infra-xtc-agent-cfg', _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-infra-xtc-agent-cfg']),
    'XtcBindingSidDynamicRule' : _MetaInfoEnum('XtcBindingSidDynamicRule',
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_agent_cfg', 'XtcBindingSidDynamicRule',
        '''Xtc binding sid dynamic rule''',
        {
            'disable':'disable',
        }, 'Cisco-IOS-XR-infra-xtc-agent-cfg', _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-infra-xtc-agent-cfg']),
    'XtcPathHop' : _MetaInfoEnum('XtcPathHop',
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_agent_cfg', 'XtcPathHop',
        '''Xtc path hop''',
        {
            'mpls':'mpls',
            'srv6':'srv6',
        }, 'Cisco-IOS-XR-infra-xtc-agent-cfg', _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-infra-xtc-agent-cfg']),
    'XtcCpath' : _MetaInfoEnum('XtcCpath',
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_agent_cfg', 'XtcCpath',
        '''Xtc cpath''',
        {
            'candidate-path-type-all':'candidate_path_type_all',
            'candidate-path-type-local':'candidate_path_type_local',
            'candidate-path-type-bgp-odn':'candidate_path_type_bgp_odn',
            'candidate-path-type-bgp-srte':'candidate_path_type_bgp_srte',
            'candidate-path-type-pcep':'candidate_path_type_pcep',
        }, 'Cisco-IOS-XR-infra-xtc-agent-cfg', _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-infra-xtc-agent-cfg']),
    'XtcSteeringApplication' : _MetaInfoEnum('XtcSteeringApplication',
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_agent_cfg', 'XtcSteeringApplication',
        '''Xtc steering application''',
        {
            'bgp':'bgp',
            'isis':'isis',
            'ospf':'ospf',
        }, 'Cisco-IOS-XR-infra-xtc-agent-cfg', _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-infra-xtc-agent-cfg']),
    'XtcPath' : _MetaInfoEnum('XtcPath',
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_agent_cfg', 'XtcPath',
        '''Xtc path''',
        {
            'explicit':'explicit',
            'dynamic':'dynamic',
        }, 'Cisco-IOS-XR-infra-xtc-agent-cfg', _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-infra-xtc-agent-cfg']),
    'XtcMetric' : _MetaInfoEnum('XtcMetric',
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_agent_cfg', 'XtcMetric',
        '''Xtc metric''',
        {
            'igp':'igp',
            'te':'te',
            'hopcount':'hopcount',
            'latency':'latency',
        }, 'Cisco-IOS-XR-infra-xtc-agent-cfg', _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-infra-xtc-agent-cfg']),
    'XtcAddressFamily' : _MetaInfoEnum('XtcAddressFamily',
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_agent_cfg', 'XtcAddressFamily',
        '''Xtc address family''',
        {
            'af-type-ipv4':'af_type_ipv4',
            'xtc-af-type-ipv6':'xtc_af_type_ipv6',
        }, 'Cisco-IOS-XR-infra-xtc-agent-cfg', _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-infra-xtc-agent-cfg']),
    'XtcSegment' : _MetaInfoEnum('XtcSegment',
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_agent_cfg', 'XtcSegment',
        '''Xtc segment''',
        {
            'ipv4-address':'ipv4_address',
            'mpls-label':'mpls_label',
        }, 'Cisco-IOS-XR-infra-xtc-agent-cfg', _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-infra-xtc-agent-cfg']),
    'XtcBindingSid' : _MetaInfoEnum('XtcBindingSid',
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_agent_cfg', 'XtcBindingSid',
        '''Xtc binding sid''',
        {
            'mpls-label-specified':'mpls_label_specified',
            'mpls-label-any':'mpls_label_any',
        }, 'Cisco-IOS-XR-infra-xtc-agent-cfg', _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-infra-xtc-agent-cfg']),
    'XtcDisjointness' : _MetaInfoEnum('XtcDisjointness',
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_agent_cfg', 'XtcDisjointness',
        '''Xtc disjointness''',
        {
            'link':'link',
            'node':'node',
            'srlg':'srlg',
            'srlg-node':'srlg_node',
        }, 'Cisco-IOS-XR-infra-xtc-agent-cfg', _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-infra-xtc-agent-cfg']),
    'XtcAutoRouteMetric' : _MetaInfoEnum('XtcAutoRouteMetric',
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_agent_cfg', 'XtcAutoRouteMetric',
        '''Xtc auto route metric''',
        {
            'relative':'relative',
            'constant':'constant',
        }, 'Cisco-IOS-XR-infra-xtc-agent-cfg', _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-infra-xtc-agent-cfg']),
}
