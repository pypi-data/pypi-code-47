
'''
This is auto-generated file,
which includes metadata for module Cisco_IOS_XR_policy_repository_cfg
'''

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_LIST, REFERENCE_LEAFLIST, REFERENCE_BITS, REFERENCE_UNION
from ydk._core._dm_meta_info import REFERENCE_CLASS, REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, ANYXML_CLASS
from ydk._core._importer import _yang_ns

_meta_table = {
    'RoutingPolicy.RoutePolicies.RoutePolicy' : {
        'meta_info' : _MetaInfoClass('RoutingPolicy.RoutePolicies.RoutePolicy', REFERENCE_LIST,
            '''Information about an individual policy''',
            False, 
            [
            _MetaInfoClassMember('route-policy-name', ATTRIBUTE, 'str', 'xr:Cisco-ios-xr-string',
                None, None,
                [], [b'[\\w\\-\\.:,_@#%$\\+=\\|;]+'],
                '''                Route policy name
                ''',
                'route_policy_name',
                'Cisco-IOS-XR-policy-repository-cfg', True),
            _MetaInfoClassMember('rpl-route-policy', ATTRIBUTE, 'str', 'xr:Rpl-policy',
                None, None,
                [], [],
                '''                policy statements
                ''',
                'rpl_route_policy',
                'Cisco-IOS-XR-policy-repository-cfg', False, is_mandatory=True),
            ],
            'Cisco-IOS-XR-policy-repository-cfg',
            'route-policy',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-policy-repository-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_cfg',
        ),
    },
    'RoutingPolicy.RoutePolicies' : {
        'meta_info' : _MetaInfoClass('RoutingPolicy.RoutePolicies', REFERENCE_CLASS,
            '''All configured policies''',
            False, 
            [
            _MetaInfoClassMember('route-policy', REFERENCE_LIST, 'RoutePolicy', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_cfg', 'RoutingPolicy.RoutePolicies.RoutePolicy',
                [], [],
                '''                Information about an individual policy
                ''',
                'route_policy',
                'Cisco-IOS-XR-policy-repository-cfg', False),
            ],
            'Cisco-IOS-XR-policy-repository-cfg',
            'route-policies',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-policy-repository-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_cfg',
        ),
    },
    'RoutingPolicy.Sets.PrefixSets.PrefixSet' : {
        'meta_info' : _MetaInfoClass('RoutingPolicy.Sets.PrefixSets.PrefixSet', REFERENCE_LIST,
            '''Information about an individual set''',
            False, 
            [
            _MetaInfoClassMember('set-name', ATTRIBUTE, 'str', 'xr:Cisco-ios-xr-string',
                None, None,
                [], [b'[\\w\\-\\.:,_@#%$\\+=\\|;]+'],
                '''                Set name
                ''',
                'set_name',
                'Cisco-IOS-XR-policy-repository-cfg', True),
            _MetaInfoClassMember('rpl-prefix-set', ATTRIBUTE, 'str', 'xr:Rpl-set',
                None, None,
                [], [],
                '''                prefix statements
                ''',
                'rpl_prefix_set',
                'Cisco-IOS-XR-policy-repository-cfg', False, is_mandatory=True),
            ],
            'Cisco-IOS-XR-policy-repository-cfg',
            'prefix-set',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-policy-repository-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_cfg',
        ),
    },
    'RoutingPolicy.Sets.PrefixSets' : {
        'meta_info' : _MetaInfoClass('RoutingPolicy.Sets.PrefixSets', REFERENCE_CLASS,
            '''Information about Prefix sets''',
            False, 
            [
            _MetaInfoClassMember('prefix-set', REFERENCE_LIST, 'PrefixSet', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_cfg', 'RoutingPolicy.Sets.PrefixSets.PrefixSet',
                [], [],
                '''                Information about an individual set
                ''',
                'prefix_set',
                'Cisco-IOS-XR-policy-repository-cfg', False),
            ],
            'Cisco-IOS-XR-policy-repository-cfg',
            'prefix-sets',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-policy-repository-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_cfg',
        ),
    },
    'RoutingPolicy.Sets.LargeCommunitySets.LargeCommunitySet' : {
        'meta_info' : _MetaInfoClass('RoutingPolicy.Sets.LargeCommunitySets.LargeCommunitySet', REFERENCE_LIST,
            '''Information about an individual set''',
            False, 
            [
            _MetaInfoClassMember('set-name', ATTRIBUTE, 'str', 'xr:Cisco-ios-xr-string',
                None, None,
                [], [b'[\\w\\-\\.:,_@#%$\\+=\\|;]+'],
                '''                Set name
                ''',
                'set_name',
                'Cisco-IOS-XR-policy-repository-cfg', True),
            _MetaInfoClassMember('large-community-set-as-text', ATTRIBUTE, 'str', 'xr:Rpl-set',
                None, None,
                [], [],
                '''                Large Community Set
                ''',
                'large_community_set_as_text',
                'Cisco-IOS-XR-policy-repository-cfg', False, is_mandatory=True),
            ],
            'Cisco-IOS-XR-policy-repository-cfg',
            'large-community-set',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-policy-repository-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_cfg',
        ),
    },
    'RoutingPolicy.Sets.LargeCommunitySets' : {
        'meta_info' : _MetaInfoClass('RoutingPolicy.Sets.LargeCommunitySets', REFERENCE_CLASS,
            '''Information about Large Community sets''',
            False, 
            [
            _MetaInfoClassMember('large-community-set', REFERENCE_LIST, 'LargeCommunitySet', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_cfg', 'RoutingPolicy.Sets.LargeCommunitySets.LargeCommunitySet',
                [], [],
                '''                Information about an individual set
                ''',
                'large_community_set',
                'Cisco-IOS-XR-policy-repository-cfg', False),
            ],
            'Cisco-IOS-XR-policy-repository-cfg',
            'large-community-sets',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-policy-repository-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_cfg',
        ),
    },
    'RoutingPolicy.Sets.MacSets.MacSet' : {
        'meta_info' : _MetaInfoClass('RoutingPolicy.Sets.MacSets.MacSet', REFERENCE_LIST,
            '''Information about an individual set''',
            False, 
            [
            _MetaInfoClassMember('set-name', ATTRIBUTE, 'str', 'xr:Cisco-ios-xr-string',
                None, None,
                [], [b'[\\w\\-\\.:,_@#%$\\+=\\|;]+'],
                '''                Set name
                ''',
                'set_name',
                'Cisco-IOS-XR-policy-repository-cfg', True),
            _MetaInfoClassMember('mac-set-as-text', ATTRIBUTE, 'str', 'xr:Rpl-set',
                None, None,
                [], [],
                '''                Mac Set
                ''',
                'mac_set_as_text',
                'Cisco-IOS-XR-policy-repository-cfg', False, is_mandatory=True),
            ],
            'Cisco-IOS-XR-policy-repository-cfg',
            'mac-set',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-policy-repository-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_cfg',
        ),
    },
    'RoutingPolicy.Sets.MacSets' : {
        'meta_info' : _MetaInfoClass('RoutingPolicy.Sets.MacSets', REFERENCE_CLASS,
            '''Information about Mac sets''',
            False, 
            [
            _MetaInfoClassMember('mac-set', REFERENCE_LIST, 'MacSet', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_cfg', 'RoutingPolicy.Sets.MacSets.MacSet',
                [], [],
                '''                Information about an individual set
                ''',
                'mac_set',
                'Cisco-IOS-XR-policy-repository-cfg', False),
            ],
            'Cisco-IOS-XR-policy-repository-cfg',
            'mac-sets',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-policy-repository-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_cfg',
        ),
    },
    'RoutingPolicy.Sets.ExtendedCommunityOpaqueSets.ExtendedCommunityOpaqueSet' : {
        'meta_info' : _MetaInfoClass('RoutingPolicy.Sets.ExtendedCommunityOpaqueSets.ExtendedCommunityOpaqueSet', REFERENCE_LIST,
            '''Information about an individual set''',
            False, 
            [
            _MetaInfoClassMember('set-name', ATTRIBUTE, 'str', 'xr:Cisco-ios-xr-string',
                None, None,
                [], [b'[\\w\\-\\.:,_@#%$\\+=\\|;]+'],
                '''                Set name
                ''',
                'set_name',
                'Cisco-IOS-XR-policy-repository-cfg', True),
            _MetaInfoClassMember('rpl-extended-community-opaque-set', ATTRIBUTE, 'str', 'xr:Rpl-set',
                None, None,
                [], [],
                '''                Extended Community Opaque Set
                ''',
                'rpl_extended_community_opaque_set',
                'Cisco-IOS-XR-policy-repository-cfg', False, is_mandatory=True),
            ],
            'Cisco-IOS-XR-policy-repository-cfg',
            'extended-community-opaque-set',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-policy-repository-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_cfg',
        ),
    },
    'RoutingPolicy.Sets.ExtendedCommunityOpaqueSets' : {
        'meta_info' : _MetaInfoClass('RoutingPolicy.Sets.ExtendedCommunityOpaqueSets', REFERENCE_CLASS,
            '''Information about Opaque sets''',
            False, 
            [
            _MetaInfoClassMember('extended-community-opaque-set', REFERENCE_LIST, 'ExtendedCommunityOpaqueSet', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_cfg', 'RoutingPolicy.Sets.ExtendedCommunityOpaqueSets.ExtendedCommunityOpaqueSet',
                [], [],
                '''                Information about an individual set
                ''',
                'extended_community_opaque_set',
                'Cisco-IOS-XR-policy-repository-cfg', False),
            ],
            'Cisco-IOS-XR-policy-repository-cfg',
            'extended-community-opaque-sets',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-policy-repository-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_cfg',
        ),
    },
    'RoutingPolicy.Sets.OspfAreaSets.OspfAreaSet' : {
        'meta_info' : _MetaInfoClass('RoutingPolicy.Sets.OspfAreaSets.OspfAreaSet', REFERENCE_LIST,
            '''Information about an individual OSPF area set.
Usage: OSPF area set allows to define named
set of area numbers        which can be
referenced in the route-policy. Area sets
may be used during redistribution of the ospf
protocol.  Example: ospf-area-set EXAMPLE
1,
192.168.1.255
end-set
Syntax: OSPF area number can be entered as 32
bit number or in          the ip address
format. See example.
Semantic: Area numbers listed in the set will
be searched for             a match. In the
example these are areas 1 and
192.168.1.255.                                ''',
            False, 
            [
            _MetaInfoClassMember('set-name', ATTRIBUTE, 'str', 'xr:Cisco-ios-xr-string',
                None, None,
                [], [b'[\\w\\-\\.:,_@#%$\\+=\\|;]+'],
                '''                Set name
                ''',
                'set_name',
                'Cisco-IOS-XR-policy-repository-cfg', True),
            _MetaInfoClassMember('rplospf-area-set', ATTRIBUTE, 'str', 'xr:Rpl-set',
                None, None,
                [], [],
                '''                OSPF Area Set
                ''',
                'rplospf_area_set',
                'Cisco-IOS-XR-policy-repository-cfg', False, is_mandatory=True),
            ],
            'Cisco-IOS-XR-policy-repository-cfg',
            'ospf-area-set',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-policy-repository-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_cfg',
        ),
    },
    'RoutingPolicy.Sets.OspfAreaSets' : {
        'meta_info' : _MetaInfoClass('RoutingPolicy.Sets.OspfAreaSets', REFERENCE_CLASS,
            '''Information about OSPF Area sets''',
            False, 
            [
            _MetaInfoClassMember('ospf-area-set', REFERENCE_LIST, 'OspfAreaSet', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_cfg', 'RoutingPolicy.Sets.OspfAreaSets.OspfAreaSet',
                [], [],
                '''                Information about an individual OSPF area set.
                Usage: OSPF area set allows to define named
                set of area numbers        which can be
                referenced in the route-policy. Area sets
                may be used during redistribution of the ospf
                protocol.  Example: ospf-area-set EXAMPLE
                1,
                192.168.1.255
                end-set
                Syntax: OSPF area number can be entered as 32
                bit number or in          the ip address
                format. See example.
                Semantic: Area numbers listed in the set will
                be searched for             a match. In the
                example these are areas 1 and
                192.168.1.255.                                
                ''',
                'ospf_area_set',
                'Cisco-IOS-XR-policy-repository-cfg', False),
            ],
            'Cisco-IOS-XR-policy-repository-cfg',
            'ospf-area-sets',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-policy-repository-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_cfg',
        ),
    },
    'RoutingPolicy.Sets.ExtendedCommunityCostSets.ExtendedCommunityCostSet' : {
        'meta_info' : _MetaInfoClass('RoutingPolicy.Sets.ExtendedCommunityCostSets.ExtendedCommunityCostSet', REFERENCE_LIST,
            '''Information about an individual set''',
            False, 
            [
            _MetaInfoClassMember('set-name', ATTRIBUTE, 'str', 'xr:Cisco-ios-xr-string',
                None, None,
                [], [b'[\\w\\-\\.:,_@#%$\\+=\\|;]+'],
                '''                Set name
                ''',
                'set_name',
                'Cisco-IOS-XR-policy-repository-cfg', True),
            _MetaInfoClassMember('rpl-extended-community-cost-set', ATTRIBUTE, 'str', 'xr:Rpl-set',
                None, None,
                [], [],
                '''                Extended Community Cost Set
                ''',
                'rpl_extended_community_cost_set',
                'Cisco-IOS-XR-policy-repository-cfg', False, is_mandatory=True),
            ],
            'Cisco-IOS-XR-policy-repository-cfg',
            'extended-community-cost-set',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-policy-repository-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_cfg',
        ),
    },
    'RoutingPolicy.Sets.ExtendedCommunityCostSets' : {
        'meta_info' : _MetaInfoClass('RoutingPolicy.Sets.ExtendedCommunityCostSets', REFERENCE_CLASS,
            '''Information about Cost sets''',
            False, 
            [
            _MetaInfoClassMember('extended-community-cost-set', REFERENCE_LIST, 'ExtendedCommunityCostSet', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_cfg', 'RoutingPolicy.Sets.ExtendedCommunityCostSets.ExtendedCommunityCostSet',
                [], [],
                '''                Information about an individual set
                ''',
                'extended_community_cost_set',
                'Cisco-IOS-XR-policy-repository-cfg', False),
            ],
            'Cisco-IOS-XR-policy-repository-cfg',
            'extended-community-cost-sets',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-policy-repository-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_cfg',
        ),
    },
    'RoutingPolicy.Sets.ExtendedCommunitySooSets.ExtendedCommunitySooSet' : {
        'meta_info' : _MetaInfoClass('RoutingPolicy.Sets.ExtendedCommunitySooSets.ExtendedCommunitySooSet', REFERENCE_LIST,
            '''Information about an individual set''',
            False, 
            [
            _MetaInfoClassMember('set-name', ATTRIBUTE, 'str', 'xr:Cisco-ios-xr-string',
                None, None,
                [], [b'[\\w\\-\\.:,_@#%$\\+=\\|;]+'],
                '''                Set name
                ''',
                'set_name',
                'Cisco-IOS-XR-policy-repository-cfg', True),
            _MetaInfoClassMember('rpl-extended-community-soo-set', ATTRIBUTE, 'str', 'xr:Rpl-set',
                None, None,
                [], [],
                '''                Extended Community SOO Set
                ''',
                'rpl_extended_community_soo_set',
                'Cisco-IOS-XR-policy-repository-cfg', False, is_mandatory=True),
            ],
            'Cisco-IOS-XR-policy-repository-cfg',
            'extended-community-soo-set',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-policy-repository-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_cfg',
        ),
    },
    'RoutingPolicy.Sets.ExtendedCommunitySooSets' : {
        'meta_info' : _MetaInfoClass('RoutingPolicy.Sets.ExtendedCommunitySooSets', REFERENCE_CLASS,
            '''Information about SOO sets''',
            False, 
            [
            _MetaInfoClassMember('extended-community-soo-set', REFERENCE_LIST, 'ExtendedCommunitySooSet', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_cfg', 'RoutingPolicy.Sets.ExtendedCommunitySooSets.ExtendedCommunitySooSet',
                [], [],
                '''                Information about an individual set
                ''',
                'extended_community_soo_set',
                'Cisco-IOS-XR-policy-repository-cfg', False),
            ],
            'Cisco-IOS-XR-policy-repository-cfg',
            'extended-community-soo-sets',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-policy-repository-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_cfg',
        ),
    },
    'RoutingPolicy.Sets.EsiSets.EsiSet' : {
        'meta_info' : _MetaInfoClass('RoutingPolicy.Sets.EsiSets.EsiSet', REFERENCE_LIST,
            '''Information about an individual set''',
            False, 
            [
            _MetaInfoClassMember('set-name', ATTRIBUTE, 'str', 'xr:Cisco-ios-xr-string',
                None, None,
                [], [b'[\\w\\-\\.:,_@#%$\\+=\\|;]+'],
                '''                Set name
                ''',
                'set_name',
                'Cisco-IOS-XR-policy-repository-cfg', True),
            _MetaInfoClassMember('esi-set-as-text', ATTRIBUTE, 'str', 'xr:Rpl-set',
                None, None,
                [], [],
                '''                Esi Set
                ''',
                'esi_set_as_text',
                'Cisco-IOS-XR-policy-repository-cfg', False, is_mandatory=True),
            ],
            'Cisco-IOS-XR-policy-repository-cfg',
            'esi-set',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-policy-repository-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_cfg',
        ),
    },
    'RoutingPolicy.Sets.EsiSets' : {
        'meta_info' : _MetaInfoClass('RoutingPolicy.Sets.EsiSets', REFERENCE_CLASS,
            '''Information about Esi sets''',
            False, 
            [
            _MetaInfoClassMember('esi-set', REFERENCE_LIST, 'EsiSet', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_cfg', 'RoutingPolicy.Sets.EsiSets.EsiSet',
                [], [],
                '''                Information about an individual set
                ''',
                'esi_set',
                'Cisco-IOS-XR-policy-repository-cfg', False),
            ],
            'Cisco-IOS-XR-policy-repository-cfg',
            'esi-sets',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-policy-repository-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_cfg',
        ),
    },
    'RoutingPolicy.Sets.ExtendedCommunitySegNhSets.ExtendedCommunitySegNhSet' : {
        'meta_info' : _MetaInfoClass('RoutingPolicy.Sets.ExtendedCommunitySegNhSets.ExtendedCommunitySegNhSet', REFERENCE_LIST,
            '''Information about an individual set''',
            False, 
            [
            _MetaInfoClassMember('set-name', ATTRIBUTE, 'str', 'xr:Cisco-ios-xr-string',
                None, None,
                [], [b'[\\w\\-\\.:,_@#%$\\+=\\|;]+'],
                '''                Set name
                ''',
                'set_name',
                'Cisco-IOS-XR-policy-repository-cfg', True),
            _MetaInfoClassMember('rpl-extended-community-seg-nh-set', ATTRIBUTE, 'str', 'xr:Rpl-set',
                None, None,
                [], [],
                '''                Extended Community SegNH Set
                ''',
                'rpl_extended_community_seg_nh_set',
                'Cisco-IOS-XR-policy-repository-cfg', False, is_mandatory=True),
            ],
            'Cisco-IOS-XR-policy-repository-cfg',
            'extended-community-seg-nh-set',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-policy-repository-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_cfg',
        ),
    },
    'RoutingPolicy.Sets.ExtendedCommunitySegNhSets' : {
        'meta_info' : _MetaInfoClass('RoutingPolicy.Sets.ExtendedCommunitySegNhSets', REFERENCE_CLASS,
            '''Information about SegNH sets''',
            False, 
            [
            _MetaInfoClassMember('extended-community-seg-nh-set', REFERENCE_LIST, 'ExtendedCommunitySegNhSet', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_cfg', 'RoutingPolicy.Sets.ExtendedCommunitySegNhSets.ExtendedCommunitySegNhSet',
                [], [],
                '''                Information about an individual set
                ''',
                'extended_community_seg_nh_set',
                'Cisco-IOS-XR-policy-repository-cfg', False),
            ],
            'Cisco-IOS-XR-policy-repository-cfg',
            'extended-community-seg-nh-sets',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-policy-repository-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_cfg',
        ),
    },
    'RoutingPolicy.Sets.RdSets.RdSet' : {
        'meta_info' : _MetaInfoClass('RoutingPolicy.Sets.RdSets.RdSet', REFERENCE_LIST,
            '''Information about an individual set''',
            False, 
            [
            _MetaInfoClassMember('set-name', ATTRIBUTE, 'str', 'xr:Cisco-ios-xr-string',
                None, None,
                [], [b'[\\w\\-\\.:,_@#%$\\+=\\|;]+'],
                '''                Set name
                ''',
                'set_name',
                'Cisco-IOS-XR-policy-repository-cfg', True),
            _MetaInfoClassMember('rplrd-set', ATTRIBUTE, 'str', 'xr:Rpl-set',
                None, None,
                [], [],
                '''                RD Set
                ''',
                'rplrd_set',
                'Cisco-IOS-XR-policy-repository-cfg', False, is_mandatory=True),
            ],
            'Cisco-IOS-XR-policy-repository-cfg',
            'rd-set',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-policy-repository-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_cfg',
        ),
    },
    'RoutingPolicy.Sets.RdSets' : {
        'meta_info' : _MetaInfoClass('RoutingPolicy.Sets.RdSets', REFERENCE_CLASS,
            '''Information about RD sets''',
            False, 
            [
            _MetaInfoClassMember('rd-set', REFERENCE_LIST, 'RdSet', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_cfg', 'RoutingPolicy.Sets.RdSets.RdSet',
                [], [],
                '''                Information about an individual set
                ''',
                'rd_set',
                'Cisco-IOS-XR-policy-repository-cfg', False),
            ],
            'Cisco-IOS-XR-policy-repository-cfg',
            'rd-sets',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-policy-repository-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_cfg',
        ),
    },
    'RoutingPolicy.Sets.PolicyGlobalSetTable' : {
        'meta_info' : _MetaInfoClass('RoutingPolicy.Sets.PolicyGlobalSetTable', REFERENCE_CLASS,
            '''Information about PolicyGlobal sets''',
            False, 
            [
            _MetaInfoClassMember('policy-global-set', ATTRIBUTE, 'str', 'xr:Rpl-set',
                None, None,
                [], [],
                '''                Information about an individual set
                ''',
                'policy_global_set',
                'Cisco-IOS-XR-policy-repository-cfg', False),
            ],
            'Cisco-IOS-XR-policy-repository-cfg',
            'policy-global-set-table',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-policy-repository-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_cfg',
        ),
    },
    'RoutingPolicy.Sets.ExtendedCommunityBandwidthSets.ExtendedCommunityBandwidthSet' : {
        'meta_info' : _MetaInfoClass('RoutingPolicy.Sets.ExtendedCommunityBandwidthSets.ExtendedCommunityBandwidthSet', REFERENCE_LIST,
            '''Information about an individual set''',
            False, 
            [
            _MetaInfoClassMember('set-name', ATTRIBUTE, 'str', 'xr:Cisco-ios-xr-string',
                None, None,
                [], [b'[\\w\\-\\.:,_@#%$\\+=\\|;]+'],
                '''                Set name
                ''',
                'set_name',
                'Cisco-IOS-XR-policy-repository-cfg', True),
            _MetaInfoClassMember('rpl-extended-community-bandwidth-set', ATTRIBUTE, 'str', 'xr:Rpl-set',
                None, None,
                [], [],
                '''                Extended Community Bandwidth Set
                ''',
                'rpl_extended_community_bandwidth_set',
                'Cisco-IOS-XR-policy-repository-cfg', False, is_mandatory=True),
            ],
            'Cisco-IOS-XR-policy-repository-cfg',
            'extended-community-bandwidth-set',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-policy-repository-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_cfg',
        ),
    },
    'RoutingPolicy.Sets.ExtendedCommunityBandwidthSets' : {
        'meta_info' : _MetaInfoClass('RoutingPolicy.Sets.ExtendedCommunityBandwidthSets', REFERENCE_CLASS,
            '''Information about Bandwidth sets''',
            False, 
            [
            _MetaInfoClassMember('extended-community-bandwidth-set', REFERENCE_LIST, 'ExtendedCommunityBandwidthSet', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_cfg', 'RoutingPolicy.Sets.ExtendedCommunityBandwidthSets.ExtendedCommunityBandwidthSet',
                [], [],
                '''                Information about an individual set
                ''',
                'extended_community_bandwidth_set',
                'Cisco-IOS-XR-policy-repository-cfg', False),
            ],
            'Cisco-IOS-XR-policy-repository-cfg',
            'extended-community-bandwidth-sets',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-policy-repository-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_cfg',
        ),
    },
    'RoutingPolicy.Sets.CommunitySets.CommunitySet' : {
        'meta_info' : _MetaInfoClass('RoutingPolicy.Sets.CommunitySets.CommunitySet', REFERENCE_LIST,
            '''Information about an individual set''',
            False, 
            [
            _MetaInfoClassMember('set-name', ATTRIBUTE, 'str', 'xr:Cisco-ios-xr-string',
                None, None,
                [], [b'[\\w\\-\\.:,_@#%$\\+=\\|;]+'],
                '''                Set name
                ''',
                'set_name',
                'Cisco-IOS-XR-policy-repository-cfg', True),
            _MetaInfoClassMember('rpl-community-set', ATTRIBUTE, 'str', 'xr:Rpl-set',
                None, None,
                [], [],
                '''                Community Set
                ''',
                'rpl_community_set',
                'Cisco-IOS-XR-policy-repository-cfg', False, is_mandatory=True),
            ],
            'Cisco-IOS-XR-policy-repository-cfg',
            'community-set',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-policy-repository-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_cfg',
        ),
    },
    'RoutingPolicy.Sets.CommunitySets' : {
        'meta_info' : _MetaInfoClass('RoutingPolicy.Sets.CommunitySets', REFERENCE_CLASS,
            '''Information about Community sets''',
            False, 
            [
            _MetaInfoClassMember('community-set', REFERENCE_LIST, 'CommunitySet', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_cfg', 'RoutingPolicy.Sets.CommunitySets.CommunitySet',
                [], [],
                '''                Information about an individual set
                ''',
                'community_set',
                'Cisco-IOS-XR-policy-repository-cfg', False),
            ],
            'Cisco-IOS-XR-policy-repository-cfg',
            'community-sets',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-policy-repository-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_cfg',
        ),
    },
    'RoutingPolicy.Sets.AsPathSets.AsPathSet' : {
        'meta_info' : _MetaInfoClass('RoutingPolicy.Sets.AsPathSets.AsPathSet', REFERENCE_LIST,
            '''Information about an individual set''',
            False, 
            [
            _MetaInfoClassMember('set-name', ATTRIBUTE, 'str', 'xr:Cisco-ios-xr-string',
                None, None,
                [], [b'[\\w\\-\\.:,_@#%$\\+=\\|;]+'],
                '''                Set name
                ''',
                'set_name',
                'Cisco-IOS-XR-policy-repository-cfg', True),
            _MetaInfoClassMember('rplas-path-set', ATTRIBUTE, 'str', 'xr:Rpl-set',
                None, None,
                [], [],
                '''                ASPath Set
                ''',
                'rplas_path_set',
                'Cisco-IOS-XR-policy-repository-cfg', False, is_mandatory=True),
            ],
            'Cisco-IOS-XR-policy-repository-cfg',
            'as-path-set',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-policy-repository-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_cfg',
        ),
    },
    'RoutingPolicy.Sets.AsPathSets' : {
        'meta_info' : _MetaInfoClass('RoutingPolicy.Sets.AsPathSets', REFERENCE_CLASS,
            '''Information about AS Path sets''',
            False, 
            [
            _MetaInfoClassMember('as-path-set', REFERENCE_LIST, 'AsPathSet', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_cfg', 'RoutingPolicy.Sets.AsPathSets.AsPathSet',
                [], [],
                '''                Information about an individual set
                ''',
                'as_path_set',
                'Cisco-IOS-XR-policy-repository-cfg', False),
            ],
            'Cisco-IOS-XR-policy-repository-cfg',
            'as-path-sets',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-policy-repository-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_cfg',
        ),
    },
    'RoutingPolicy.Sets.TagSets.TagSet' : {
        'meta_info' : _MetaInfoClass('RoutingPolicy.Sets.TagSets.TagSet', REFERENCE_LIST,
            '''Information about an individual set''',
            False, 
            [
            _MetaInfoClassMember('set-name', ATTRIBUTE, 'str', 'xr:Cisco-ios-xr-string',
                None, None,
                [], [b'[\\w\\-\\.:,_@#%$\\+=\\|;]+'],
                '''                Set name
                ''',
                'set_name',
                'Cisco-IOS-XR-policy-repository-cfg', True),
            _MetaInfoClassMember('rpl-tag-set', ATTRIBUTE, 'str', 'xr:Rpl-set',
                None, None,
                [], [],
                '''                Tag Set
                ''',
                'rpl_tag_set',
                'Cisco-IOS-XR-policy-repository-cfg', False, is_mandatory=True),
            ],
            'Cisco-IOS-XR-policy-repository-cfg',
            'tag-set',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-policy-repository-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_cfg',
        ),
    },
    'RoutingPolicy.Sets.TagSets' : {
        'meta_info' : _MetaInfoClass('RoutingPolicy.Sets.TagSets', REFERENCE_CLASS,
            '''Information about Tag sets''',
            False, 
            [
            _MetaInfoClassMember('tag-set', REFERENCE_LIST, 'TagSet', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_cfg', 'RoutingPolicy.Sets.TagSets.TagSet',
                [], [],
                '''                Information about an individual set
                ''',
                'tag_set',
                'Cisco-IOS-XR-policy-repository-cfg', False),
            ],
            'Cisco-IOS-XR-policy-repository-cfg',
            'tag-sets',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-policy-repository-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_cfg',
        ),
    },
    'RoutingPolicy.Sets.EtagSets.EtagSet' : {
        'meta_info' : _MetaInfoClass('RoutingPolicy.Sets.EtagSets.EtagSet', REFERENCE_LIST,
            '''Information about an individual set''',
            False, 
            [
            _MetaInfoClassMember('set-name', ATTRIBUTE, 'str', 'xr:Cisco-ios-xr-string',
                None, None,
                [], [b'[\\w\\-\\.:,_@#%$\\+=\\|;]+'],
                '''                Set name
                ''',
                'set_name',
                'Cisco-IOS-XR-policy-repository-cfg', True),
            _MetaInfoClassMember('etag-set-as-text', ATTRIBUTE, 'str', 'xr:Rpl-set',
                None, None,
                [], [],
                '''                Etag Set
                ''',
                'etag_set_as_text',
                'Cisco-IOS-XR-policy-repository-cfg', False, is_mandatory=True),
            ],
            'Cisco-IOS-XR-policy-repository-cfg',
            'etag-set',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-policy-repository-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_cfg',
        ),
    },
    'RoutingPolicy.Sets.EtagSets' : {
        'meta_info' : _MetaInfoClass('RoutingPolicy.Sets.EtagSets', REFERENCE_CLASS,
            '''Information about Etag sets''',
            False, 
            [
            _MetaInfoClassMember('etag-set', REFERENCE_LIST, 'EtagSet', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_cfg', 'RoutingPolicy.Sets.EtagSets.EtagSet',
                [], [],
                '''                Information about an individual set
                ''',
                'etag_set',
                'Cisco-IOS-XR-policy-repository-cfg', False),
            ],
            'Cisco-IOS-XR-policy-repository-cfg',
            'etag-sets',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-policy-repository-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_cfg',
        ),
    },
    'RoutingPolicy.Sets.ExtendedCommunityRtSets.ExtendedCommunityRtSet' : {
        'meta_info' : _MetaInfoClass('RoutingPolicy.Sets.ExtendedCommunityRtSets.ExtendedCommunityRtSet', REFERENCE_LIST,
            '''Information about an individual set''',
            False, 
            [
            _MetaInfoClassMember('set-name', ATTRIBUTE, 'str', 'xr:Cisco-ios-xr-string',
                None, None,
                [], [b'[\\w\\-\\.:,_@#%$\\+=\\|;]+'],
                '''                Set name
                ''',
                'set_name',
                'Cisco-IOS-XR-policy-repository-cfg', True),
            _MetaInfoClassMember('rpl-extended-community-rt-set', ATTRIBUTE, 'str', 'xr:Rpl-set',
                None, None,
                [], [],
                '''                Extended Community RT Set
                ''',
                'rpl_extended_community_rt_set',
                'Cisco-IOS-XR-policy-repository-cfg', False, is_mandatory=True),
            ],
            'Cisco-IOS-XR-policy-repository-cfg',
            'extended-community-rt-set',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-policy-repository-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_cfg',
        ),
    },
    'RoutingPolicy.Sets.ExtendedCommunityRtSets' : {
        'meta_info' : _MetaInfoClass('RoutingPolicy.Sets.ExtendedCommunityRtSets', REFERENCE_CLASS,
            '''Information about RT sets''',
            False, 
            [
            _MetaInfoClassMember('extended-community-rt-set', REFERENCE_LIST, 'ExtendedCommunityRtSet', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_cfg', 'RoutingPolicy.Sets.ExtendedCommunityRtSets.ExtendedCommunityRtSet',
                [], [],
                '''                Information about an individual set
                ''',
                'extended_community_rt_set',
                'Cisco-IOS-XR-policy-repository-cfg', False),
            ],
            'Cisco-IOS-XR-policy-repository-cfg',
            'extended-community-rt-sets',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-policy-repository-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_cfg',
        ),
    },
    'RoutingPolicy.Sets' : {
        'meta_info' : _MetaInfoClass('RoutingPolicy.Sets', REFERENCE_CLASS,
            '''All configured sets''',
            False, 
            [
            _MetaInfoClassMember('prefix-sets', REFERENCE_CLASS, 'PrefixSets', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_cfg', 'RoutingPolicy.Sets.PrefixSets',
                [], [],
                '''                Information about Prefix sets
                ''',
                'prefix_sets',
                'Cisco-IOS-XR-policy-repository-cfg', False),
            _MetaInfoClassMember('large-community-sets', REFERENCE_CLASS, 'LargeCommunitySets', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_cfg', 'RoutingPolicy.Sets.LargeCommunitySets',
                [], [],
                '''                Information about Large Community sets
                ''',
                'large_community_sets',
                'Cisco-IOS-XR-policy-repository-cfg', False),
            _MetaInfoClassMember('mac-sets', REFERENCE_CLASS, 'MacSets', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_cfg', 'RoutingPolicy.Sets.MacSets',
                [], [],
                '''                Information about Mac sets
                ''',
                'mac_sets',
                'Cisco-IOS-XR-policy-repository-cfg', False),
            _MetaInfoClassMember('extended-community-opaque-sets', REFERENCE_CLASS, 'ExtendedCommunityOpaqueSets', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_cfg', 'RoutingPolicy.Sets.ExtendedCommunityOpaqueSets',
                [], [],
                '''                Information about Opaque sets
                ''',
                'extended_community_opaque_sets',
                'Cisco-IOS-XR-policy-repository-cfg', False),
            _MetaInfoClassMember('ospf-area-sets', REFERENCE_CLASS, 'OspfAreaSets', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_cfg', 'RoutingPolicy.Sets.OspfAreaSets',
                [], [],
                '''                Information about OSPF Area sets
                ''',
                'ospf_area_sets',
                'Cisco-IOS-XR-policy-repository-cfg', False),
            _MetaInfoClassMember('extended-community-cost-sets', REFERENCE_CLASS, 'ExtendedCommunityCostSets', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_cfg', 'RoutingPolicy.Sets.ExtendedCommunityCostSets',
                [], [],
                '''                Information about Cost sets
                ''',
                'extended_community_cost_sets',
                'Cisco-IOS-XR-policy-repository-cfg', False),
            _MetaInfoClassMember('extended-community-soo-sets', REFERENCE_CLASS, 'ExtendedCommunitySooSets', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_cfg', 'RoutingPolicy.Sets.ExtendedCommunitySooSets',
                [], [],
                '''                Information about SOO sets
                ''',
                'extended_community_soo_sets',
                'Cisco-IOS-XR-policy-repository-cfg', False),
            _MetaInfoClassMember('esi-sets', REFERENCE_CLASS, 'EsiSets', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_cfg', 'RoutingPolicy.Sets.EsiSets',
                [], [],
                '''                Information about Esi sets
                ''',
                'esi_sets',
                'Cisco-IOS-XR-policy-repository-cfg', False),
            _MetaInfoClassMember('extended-community-seg-nh-sets', REFERENCE_CLASS, 'ExtendedCommunitySegNhSets', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_cfg', 'RoutingPolicy.Sets.ExtendedCommunitySegNhSets',
                [], [],
                '''                Information about SegNH sets
                ''',
                'extended_community_seg_nh_sets',
                'Cisco-IOS-XR-policy-repository-cfg', False),
            _MetaInfoClassMember('rd-sets', REFERENCE_CLASS, 'RdSets', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_cfg', 'RoutingPolicy.Sets.RdSets',
                [], [],
                '''                Information about RD sets
                ''',
                'rd_sets',
                'Cisco-IOS-XR-policy-repository-cfg', False),
            _MetaInfoClassMember('policy-global-set-table', REFERENCE_CLASS, 'PolicyGlobalSetTable', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_cfg', 'RoutingPolicy.Sets.PolicyGlobalSetTable',
                [], [],
                '''                Information about PolicyGlobal sets
                ''',
                'policy_global_set_table',
                'Cisco-IOS-XR-policy-repository-cfg', False),
            _MetaInfoClassMember('extended-community-bandwidth-sets', REFERENCE_CLASS, 'ExtendedCommunityBandwidthSets', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_cfg', 'RoutingPolicy.Sets.ExtendedCommunityBandwidthSets',
                [], [],
                '''                Information about Bandwidth sets
                ''',
                'extended_community_bandwidth_sets',
                'Cisco-IOS-XR-policy-repository-cfg', False),
            _MetaInfoClassMember('community-sets', REFERENCE_CLASS, 'CommunitySets', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_cfg', 'RoutingPolicy.Sets.CommunitySets',
                [], [],
                '''                Information about Community sets
                ''',
                'community_sets',
                'Cisco-IOS-XR-policy-repository-cfg', False),
            _MetaInfoClassMember('as-path-sets', REFERENCE_CLASS, 'AsPathSets', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_cfg', 'RoutingPolicy.Sets.AsPathSets',
                [], [],
                '''                Information about AS Path sets
                ''',
                'as_path_sets',
                'Cisco-IOS-XR-policy-repository-cfg', False),
            _MetaInfoClassMember('tag-sets', REFERENCE_CLASS, 'TagSets', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_cfg', 'RoutingPolicy.Sets.TagSets',
                [], [],
                '''                Information about Tag sets
                ''',
                'tag_sets',
                'Cisco-IOS-XR-policy-repository-cfg', False),
            _MetaInfoClassMember('etag-sets', REFERENCE_CLASS, 'EtagSets', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_cfg', 'RoutingPolicy.Sets.EtagSets',
                [], [],
                '''                Information about Etag sets
                ''',
                'etag_sets',
                'Cisco-IOS-XR-policy-repository-cfg', False),
            _MetaInfoClassMember('extended-community-rt-sets', REFERENCE_CLASS, 'ExtendedCommunityRtSets', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_cfg', 'RoutingPolicy.Sets.ExtendedCommunityRtSets',
                [], [],
                '''                Information about RT sets
                ''',
                'extended_community_rt_sets',
                'Cisco-IOS-XR-policy-repository-cfg', False),
            ],
            'Cisco-IOS-XR-policy-repository-cfg',
            'sets',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-policy-repository-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_cfg',
        ),
    },
    'RoutingPolicy.Limits' : {
        'meta_info' : _MetaInfoClass('RoutingPolicy.Limits', REFERENCE_CLASS,
            '''Limits for Routing Policy''',
            False, 
            [
            _MetaInfoClassMember('maximum-lines-of-policy', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('0', '4294967295')], [],
                '''                Maximum number of lines of policy configuration
                that may be configured in total
                ''',
                'maximum_lines_of_policy',
                'Cisco-IOS-XR-policy-repository-cfg', False, default_value="131072"),
            _MetaInfoClassMember('maximum-number-of-policies', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('0', '4294967295')], [],
                '''                Maximum number of policies that may be
                configured
                ''',
                'maximum_number_of_policies',
                'Cisco-IOS-XR-policy-repository-cfg', False, default_value="5000"),
            ],
            'Cisco-IOS-XR-policy-repository-cfg',
            'limits',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-policy-repository-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_cfg',
        ),
    },
    'RoutingPolicy' : {
        'meta_info' : _MetaInfoClass('RoutingPolicy', REFERENCE_CLASS,
            '''Routing policy configuration''',
            False, 
            [
            _MetaInfoClassMember('route-policies', REFERENCE_CLASS, 'RoutePolicies', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_cfg', 'RoutingPolicy.RoutePolicies',
                [], [],
                '''                All configured policies
                ''',
                'route_policies',
                'Cisco-IOS-XR-policy-repository-cfg', False),
            _MetaInfoClassMember('sets', REFERENCE_CLASS, 'Sets', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_cfg', 'RoutingPolicy.Sets',
                [], [],
                '''                All configured sets
                ''',
                'sets',
                'Cisco-IOS-XR-policy-repository-cfg', False),
            _MetaInfoClassMember('limits', REFERENCE_CLASS, 'Limits', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_cfg', 'RoutingPolicy.Limits',
                [], [],
                '''                Limits for Routing Policy
                ''',
                'limits',
                'Cisco-IOS-XR-policy-repository-cfg', False),
            _MetaInfoClassMember('set-exit-as-abort', ATTRIBUTE, 'Empty', 'empty',
                None, None,
                [], [],
                '''                Set exit under RPL config to abort
                ''',
                'set_exit_as_abort',
                'Cisco-IOS-XR-policy-repository-cfg', False),
            _MetaInfoClassMember('editor', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                'emacs' or 'vim' or 'nano'
                ''',
                'editor',
                'Cisco-IOS-XR-policy-repository-cfg', False),
            ],
            'Cisco-IOS-XR-policy-repository-cfg',
            'routing-policy',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-policy-repository-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_cfg',
        ),
    },
}
_meta_table['RoutingPolicy.RoutePolicies.RoutePolicy']['meta_info'].parent =_meta_table['RoutingPolicy.RoutePolicies']['meta_info']
_meta_table['RoutingPolicy.Sets.PrefixSets.PrefixSet']['meta_info'].parent =_meta_table['RoutingPolicy.Sets.PrefixSets']['meta_info']
_meta_table['RoutingPolicy.Sets.LargeCommunitySets.LargeCommunitySet']['meta_info'].parent =_meta_table['RoutingPolicy.Sets.LargeCommunitySets']['meta_info']
_meta_table['RoutingPolicy.Sets.MacSets.MacSet']['meta_info'].parent =_meta_table['RoutingPolicy.Sets.MacSets']['meta_info']
_meta_table['RoutingPolicy.Sets.ExtendedCommunityOpaqueSets.ExtendedCommunityOpaqueSet']['meta_info'].parent =_meta_table['RoutingPolicy.Sets.ExtendedCommunityOpaqueSets']['meta_info']
_meta_table['RoutingPolicy.Sets.OspfAreaSets.OspfAreaSet']['meta_info'].parent =_meta_table['RoutingPolicy.Sets.OspfAreaSets']['meta_info']
_meta_table['RoutingPolicy.Sets.ExtendedCommunityCostSets.ExtendedCommunityCostSet']['meta_info'].parent =_meta_table['RoutingPolicy.Sets.ExtendedCommunityCostSets']['meta_info']
_meta_table['RoutingPolicy.Sets.ExtendedCommunitySooSets.ExtendedCommunitySooSet']['meta_info'].parent =_meta_table['RoutingPolicy.Sets.ExtendedCommunitySooSets']['meta_info']
_meta_table['RoutingPolicy.Sets.EsiSets.EsiSet']['meta_info'].parent =_meta_table['RoutingPolicy.Sets.EsiSets']['meta_info']
_meta_table['RoutingPolicy.Sets.ExtendedCommunitySegNhSets.ExtendedCommunitySegNhSet']['meta_info'].parent =_meta_table['RoutingPolicy.Sets.ExtendedCommunitySegNhSets']['meta_info']
_meta_table['RoutingPolicy.Sets.RdSets.RdSet']['meta_info'].parent =_meta_table['RoutingPolicy.Sets.RdSets']['meta_info']
_meta_table['RoutingPolicy.Sets.ExtendedCommunityBandwidthSets.ExtendedCommunityBandwidthSet']['meta_info'].parent =_meta_table['RoutingPolicy.Sets.ExtendedCommunityBandwidthSets']['meta_info']
_meta_table['RoutingPolicy.Sets.CommunitySets.CommunitySet']['meta_info'].parent =_meta_table['RoutingPolicy.Sets.CommunitySets']['meta_info']
_meta_table['RoutingPolicy.Sets.AsPathSets.AsPathSet']['meta_info'].parent =_meta_table['RoutingPolicy.Sets.AsPathSets']['meta_info']
_meta_table['RoutingPolicy.Sets.TagSets.TagSet']['meta_info'].parent =_meta_table['RoutingPolicy.Sets.TagSets']['meta_info']
_meta_table['RoutingPolicy.Sets.EtagSets.EtagSet']['meta_info'].parent =_meta_table['RoutingPolicy.Sets.EtagSets']['meta_info']
_meta_table['RoutingPolicy.Sets.ExtendedCommunityRtSets.ExtendedCommunityRtSet']['meta_info'].parent =_meta_table['RoutingPolicy.Sets.ExtendedCommunityRtSets']['meta_info']
_meta_table['RoutingPolicy.Sets.PrefixSets']['meta_info'].parent =_meta_table['RoutingPolicy.Sets']['meta_info']
_meta_table['RoutingPolicy.Sets.LargeCommunitySets']['meta_info'].parent =_meta_table['RoutingPolicy.Sets']['meta_info']
_meta_table['RoutingPolicy.Sets.MacSets']['meta_info'].parent =_meta_table['RoutingPolicy.Sets']['meta_info']
_meta_table['RoutingPolicy.Sets.ExtendedCommunityOpaqueSets']['meta_info'].parent =_meta_table['RoutingPolicy.Sets']['meta_info']
_meta_table['RoutingPolicy.Sets.OspfAreaSets']['meta_info'].parent =_meta_table['RoutingPolicy.Sets']['meta_info']
_meta_table['RoutingPolicy.Sets.ExtendedCommunityCostSets']['meta_info'].parent =_meta_table['RoutingPolicy.Sets']['meta_info']
_meta_table['RoutingPolicy.Sets.ExtendedCommunitySooSets']['meta_info'].parent =_meta_table['RoutingPolicy.Sets']['meta_info']
_meta_table['RoutingPolicy.Sets.EsiSets']['meta_info'].parent =_meta_table['RoutingPolicy.Sets']['meta_info']
_meta_table['RoutingPolicy.Sets.ExtendedCommunitySegNhSets']['meta_info'].parent =_meta_table['RoutingPolicy.Sets']['meta_info']
_meta_table['RoutingPolicy.Sets.RdSets']['meta_info'].parent =_meta_table['RoutingPolicy.Sets']['meta_info']
_meta_table['RoutingPolicy.Sets.PolicyGlobalSetTable']['meta_info'].parent =_meta_table['RoutingPolicy.Sets']['meta_info']
_meta_table['RoutingPolicy.Sets.ExtendedCommunityBandwidthSets']['meta_info'].parent =_meta_table['RoutingPolicy.Sets']['meta_info']
_meta_table['RoutingPolicy.Sets.CommunitySets']['meta_info'].parent =_meta_table['RoutingPolicy.Sets']['meta_info']
_meta_table['RoutingPolicy.Sets.AsPathSets']['meta_info'].parent =_meta_table['RoutingPolicy.Sets']['meta_info']
_meta_table['RoutingPolicy.Sets.TagSets']['meta_info'].parent =_meta_table['RoutingPolicy.Sets']['meta_info']
_meta_table['RoutingPolicy.Sets.EtagSets']['meta_info'].parent =_meta_table['RoutingPolicy.Sets']['meta_info']
_meta_table['RoutingPolicy.Sets.ExtendedCommunityRtSets']['meta_info'].parent =_meta_table['RoutingPolicy.Sets']['meta_info']
_meta_table['RoutingPolicy.RoutePolicies']['meta_info'].parent =_meta_table['RoutingPolicy']['meta_info']
_meta_table['RoutingPolicy.Sets']['meta_info'].parent =_meta_table['RoutingPolicy']['meta_info']
_meta_table['RoutingPolicy.Limits']['meta_info'].parent =_meta_table['RoutingPolicy']['meta_info']
