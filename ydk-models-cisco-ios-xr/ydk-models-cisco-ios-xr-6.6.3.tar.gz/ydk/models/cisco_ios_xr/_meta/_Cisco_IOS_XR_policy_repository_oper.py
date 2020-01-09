
'''
This is auto-generated file,
which includes metadata for module Cisco_IOS_XR_policy_repository_oper
'''

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_LIST, REFERENCE_LEAFLIST, REFERENCE_BITS, REFERENCE_UNION
from ydk._core._dm_meta_info import REFERENCE_CLASS, REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, ANYXML_CLASS
from ydk._core._importer import _yang_ns

_meta_table = {
    'Group' : _MetaInfoEnum('Group',
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper', 'Group',
        '''BGP Neighbor Group Type''',
        {
            'address-family-group':'address_family_group',
            'session-group':'session_group',
            'neighbor-group':'neighbor_group',
            'neighbor':'neighbor',
            'error-group':'error_group',
        }, 'Cisco-IOS-XR-policy-repository-oper', _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-policy-repository-oper']),
    'AttachPointDirection' : _MetaInfoEnum('AttachPointDirection',
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper', 'AttachPointDirection',
        '''Attach Point Direction''',
        {
            'in':'in_',
            'out':'out',
        }, 'Cisco-IOS-XR-policy-repository-oper', _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-policy-repository-oper']),
    'SubAddressFamily' : _MetaInfoEnum('SubAddressFamily',
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper', 'SubAddressFamily',
        '''Sub Address Family''',
        {
            'unicast':'unicast',
            'multicast':'multicast',
            'label':'label',
            'tunnel':'tunnel',
            'vpn':'vpn',
            'mdt':'mdt',
            'vpls':'vpls',
            'rt-constraint':'rt_constraint',
            'mvpn':'mvpn',
            'flow':'flow',
            'vpn-mcast':'vpn_mcast',
            'evpn':'evpn',
            'saf-none':'saf_none',
            'saf-unknown':'saf_unknown',
        }, 'Cisco-IOS-XR-policy-repository-oper', _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-policy-repository-oper']),
    'AddressFamily' : _MetaInfoEnum('AddressFamily',
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper', 'AddressFamily',
        '''Address Family''',
        {
            'ipv4':'ipv4',
            'ipv6':'ipv6',
            'l2vpn':'l2vpn',
            'ls':'ls',
            'af-none':'af_none',
            'af-unknown':'af_unknown',
        }, 'Cisco-IOS-XR-policy-repository-oper', _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-policy-repository-oper']),
    'ObjectStatus' : _MetaInfoEnum('ObjectStatus',
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper', 'ObjectStatus',
        '''Whether an RPL object is used/referenced''',
        {
            'active':'active',
            'inactive':'inactive',
            'unused':'unused',
        }, 'Cisco-IOS-XR-policy-repository-oper', _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-policy-repository-oper']),
    'RoutingPolicy.Limits' : {
        'meta_info' : _MetaInfoClass('RoutingPolicy.Limits', REFERENCE_CLASS,
            '''Information about configured limits and the
current values''',
            False, 
            [
            _MetaInfoClassMember('maximum-lines-of-policy', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('0', '4294967295')], [],
                '''                Maximum lines of configuration allowable for all
                policies and sets
                ''',
                'maximum_lines_of_policy',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('current-lines-of-policy-limit', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('0', '4294967295')], [],
                '''                Number of lines of configuration for
                policies/sets currently allowed
                ''',
                'current_lines_of_policy_limit',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('current-lines-of-policy-used', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('0', '4294967295')], [],
                '''                Current number of lines configured for all
                policies and sets
                ''',
                'current_lines_of_policy_used',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('maximum-number-of-policies', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('0', '4294967295')], [],
                '''                Maximum number of policies allowable
                ''',
                'maximum_number_of_policies',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('current-number-of-policies-limit', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('0', '4294967295')], [],
                '''                Number of policies currently allowed
                ''',
                'current_number_of_policies_limit',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('current-number-of-policies-used', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('0', '4294967295')], [],
                '''                Current number of policies configured
                ''',
                'current_number_of_policies_used',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('compiled-policies-length', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('0', '4294967295')], [],
                '''                The total compiled length of all policies
                ''',
                'compiled_policies_length',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            ],
            'Cisco-IOS-XR-policy-repository-oper',
            'limits',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-policy-repository-oper'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper',
            is_config=False,
        ),
    },
    'RoutingPolicy.Policies.RoutePolicies.RoutePolicy.PolicyUses.DirectlyUsedPolicies' : {
        'meta_info' : _MetaInfoClass('RoutingPolicy.Policies.RoutePolicies.RoutePolicy.PolicyUses.DirectlyUsedPolicies', REFERENCE_CLASS,
            '''Policies that this policy uses directly''',
            False, 
            [
            _MetaInfoClassMember('object', REFERENCE_LEAFLIST, 'str', 'String',
                None, None,
                [], [],
                '''                Policy objects
                ''',
                'object',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            ],
            'Cisco-IOS-XR-policy-repository-oper',
            'directly-used-policies',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-policy-repository-oper'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper',
            is_config=False,
        ),
    },
    'RoutingPolicy.Policies.RoutePolicies.RoutePolicy.PolicyUses.AllUsedSets.Sets' : {
        'meta_info' : _MetaInfoClass('RoutingPolicy.Policies.RoutePolicies.RoutePolicy.PolicyUses.AllUsedSets.Sets', REFERENCE_LIST,
            '''List of sets in several domains''',
            False, 
            [
            _MetaInfoClassMember('set-domain', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                Domain of sets
                ''',
                'set_domain',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('set-name', REFERENCE_LEAFLIST, 'str', 'String',
                None, None,
                [], [],
                '''                Names of sets in this domain
                ''',
                'set_name',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            ],
            'Cisco-IOS-XR-policy-repository-oper',
            'sets',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-policy-repository-oper'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper',
            is_config=False,
        ),
    },
    'RoutingPolicy.Policies.RoutePolicies.RoutePolicy.PolicyUses.AllUsedSets' : {
        'meta_info' : _MetaInfoClass('RoutingPolicy.Policies.RoutePolicies.RoutePolicy.PolicyUses.AllUsedSets', REFERENCE_CLASS,
            '''Sets used by this policy, or by policies
that it uses''',
            False, 
            [
            _MetaInfoClassMember('sets', REFERENCE_LIST, 'Sets', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper', 'RoutingPolicy.Policies.RoutePolicies.RoutePolicy.PolicyUses.AllUsedSets.Sets',
                [], [],
                '''                List of sets in several domains
                ''',
                'sets',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            ],
            'Cisco-IOS-XR-policy-repository-oper',
            'all-used-sets',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-policy-repository-oper'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper',
            is_config=False,
        ),
    },
    'RoutingPolicy.Policies.RoutePolicies.RoutePolicy.PolicyUses.DirectlyUsedSets.Sets' : {
        'meta_info' : _MetaInfoClass('RoutingPolicy.Policies.RoutePolicies.RoutePolicy.PolicyUses.DirectlyUsedSets.Sets', REFERENCE_LIST,
            '''List of sets in several domains''',
            False, 
            [
            _MetaInfoClassMember('set-domain', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                Domain of sets
                ''',
                'set_domain',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('set-name', REFERENCE_LEAFLIST, 'str', 'String',
                None, None,
                [], [],
                '''                Names of sets in this domain
                ''',
                'set_name',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            ],
            'Cisco-IOS-XR-policy-repository-oper',
            'sets',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-policy-repository-oper'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper',
            is_config=False,
        ),
    },
    'RoutingPolicy.Policies.RoutePolicies.RoutePolicy.PolicyUses.DirectlyUsedSets' : {
        'meta_info' : _MetaInfoClass('RoutingPolicy.Policies.RoutePolicies.RoutePolicy.PolicyUses.DirectlyUsedSets', REFERENCE_CLASS,
            '''Sets that this policy uses directly''',
            False, 
            [
            _MetaInfoClassMember('sets', REFERENCE_LIST, 'Sets', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper', 'RoutingPolicy.Policies.RoutePolicies.RoutePolicy.PolicyUses.DirectlyUsedSets.Sets',
                [], [],
                '''                List of sets in several domains
                ''',
                'sets',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            ],
            'Cisco-IOS-XR-policy-repository-oper',
            'directly-used-sets',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-policy-repository-oper'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper',
            is_config=False,
        ),
    },
    'RoutingPolicy.Policies.RoutePolicies.RoutePolicy.PolicyUses.AllUsedPolicies' : {
        'meta_info' : _MetaInfoClass('RoutingPolicy.Policies.RoutePolicies.RoutePolicy.PolicyUses.AllUsedPolicies', REFERENCE_CLASS,
            '''Policies used by this policy, or by policies
that it uses''',
            False, 
            [
            _MetaInfoClassMember('object', REFERENCE_LEAFLIST, 'str', 'String',
                None, None,
                [], [],
                '''                Policy objects
                ''',
                'object',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            ],
            'Cisco-IOS-XR-policy-repository-oper',
            'all-used-policies',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-policy-repository-oper'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper',
            is_config=False,
        ),
    },
    'RoutingPolicy.Policies.RoutePolicies.RoutePolicy.PolicyUses' : {
        'meta_info' : _MetaInfoClass('RoutingPolicy.Policies.RoutePolicies.RoutePolicy.PolicyUses', REFERENCE_CLASS,
            '''Information about which policies and sets
this policy uses''',
            False, 
            [
            _MetaInfoClassMember('directly-used-policies', REFERENCE_CLASS, 'DirectlyUsedPolicies', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper', 'RoutingPolicy.Policies.RoutePolicies.RoutePolicy.PolicyUses.DirectlyUsedPolicies',
                [], [],
                '''                Policies that this policy uses directly
                ''',
                'directly_used_policies',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('all-used-sets', REFERENCE_CLASS, 'AllUsedSets', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper', 'RoutingPolicy.Policies.RoutePolicies.RoutePolicy.PolicyUses.AllUsedSets',
                [], [],
                '''                Sets used by this policy, or by policies
                that it uses
                ''',
                'all_used_sets',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('directly-used-sets', REFERENCE_CLASS, 'DirectlyUsedSets', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper', 'RoutingPolicy.Policies.RoutePolicies.RoutePolicy.PolicyUses.DirectlyUsedSets',
                [], [],
                '''                Sets that this policy uses directly
                ''',
                'directly_used_sets',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('all-used-policies', REFERENCE_CLASS, 'AllUsedPolicies', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper', 'RoutingPolicy.Policies.RoutePolicies.RoutePolicy.PolicyUses.AllUsedPolicies',
                [], [],
                '''                Policies used by this policy, or by policies
                that it uses
                ''',
                'all_used_policies',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            ],
            'Cisco-IOS-XR-policy-repository-oper',
            'policy-uses',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-policy-repository-oper'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper',
            is_config=False,
        ),
    },
    'RoutingPolicy.Policies.RoutePolicies.RoutePolicy.UsedBy.Reference' : {
        'meta_info' : _MetaInfoClass('RoutingPolicy.Policies.RoutePolicies.RoutePolicy.UsedBy.Reference', REFERENCE_LIST,
            '''Information about policies referring to this
object''',
            False, 
            [
            _MetaInfoClassMember('route-policy-name', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                Name of policy
                ''',
                'route_policy_name',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('used-directly', ATTRIBUTE, 'bool', 'boolean',
                None, None,
                [], [],
                '''                Whether the policy uses this object directly or
                indirectly
                ''',
                'used_directly',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('status', REFERENCE_ENUM_CLASS, 'ObjectStatus', 'Object-status',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper', 'ObjectStatus',
                [], [],
                '''                Active, Inactive, or Unused
                ''',
                'status',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            ],
            'Cisco-IOS-XR-policy-repository-oper',
            'reference',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-policy-repository-oper'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper',
            is_config=False,
        ),
    },
    'RoutingPolicy.Policies.RoutePolicies.RoutePolicy.UsedBy' : {
        'meta_info' : _MetaInfoClass('RoutingPolicy.Policies.RoutePolicies.RoutePolicy.UsedBy', REFERENCE_CLASS,
            '''Policies that use this object, directly or
indirectly''',
            False, 
            [
            _MetaInfoClassMember('reference', REFERENCE_LIST, 'Reference', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper', 'RoutingPolicy.Policies.RoutePolicies.RoutePolicy.UsedBy.Reference',
                [], [],
                '''                Information about policies referring to this
                object
                ''',
                'reference',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            ],
            'Cisco-IOS-XR-policy-repository-oper',
            'used-by',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-policy-repository-oper'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper',
            is_config=False,
        ),
    },
    'RoutingPolicy.Policies.RoutePolicies.RoutePolicy.Attached.Binding' : {
        'meta_info' : _MetaInfoClass('RoutingPolicy.Policies.RoutePolicies.RoutePolicy.Attached.Binding', REFERENCE_LIST,
            '''bindings list''',
            False, 
            [
            _MetaInfoClassMember('protocol', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                Protocol to which policy attached
                ''',
                'protocol',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('vrf-name', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                VRF name
                ''',
                'vrf_name',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('proto-instance', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                Protocol instance
                ''',
                'proto_instance',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('af-name', REFERENCE_ENUM_CLASS, 'AddressFamily', 'Address-family',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper', 'AddressFamily',
                [], [],
                '''                Address Family Identifier
                ''',
                'af_name',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('saf-name', REFERENCE_ENUM_CLASS, 'SubAddressFamily', 'Sub-address-family',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper', 'SubAddressFamily',
                [], [],
                '''                Subsequent Address Family Identifier
                ''',
                'saf_name',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('neighbor-address', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                Neighbor IP Address
                ''',
                'neighbor_address',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('neighbor-af-name', REFERENCE_ENUM_CLASS, 'AddressFamily', 'Address-family',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper', 'AddressFamily',
                [], [],
                '''                Neighbor IP Address Family
                ''',
                'neighbor_af_name',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('group-name', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                Neighbor Group Name
                ''',
                'group_name',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('direction', REFERENCE_ENUM_CLASS, 'AttachPointDirection', 'Attach-point-direction',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper', 'AttachPointDirection',
                [], [],
                '''                Direction In or Out
                ''',
                'direction',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('group', REFERENCE_ENUM_CLASS, 'Group', 'Group',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper', 'Group',
                [], [],
                '''                Neighbor Group 
                ''',
                'group',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('source-protocol', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                Source Protocol to redistribute, Source Protocol
                can be one of the following values{all,
                connected, local, static, bgp, rip, isis, ospf
                ,ospfv3, eigrp, unknown }
                ''',
                'source_protocol',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('aggregate-network-address', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                Aggregate IP address or Network IP Address in
                IPv4 or IPv6 Format
                ''',
                'aggregate_network_address',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('interface-name', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                Interface Name
                ''',
                'interface_name',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('instance', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                Instance
                ''',
                'instance',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('area-id', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                OSPF Area ID in Decimal Integer Format
                ''',
                'area_id',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('propogate-from', ATTRIBUTE, 'int', 'int32',
                None, None,
                [('-2147483648', '2147483647')], [],
                '''                ISIS Propogate From Level
                ''',
                'propogate_from',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('propogate-to', ATTRIBUTE, 'int', 'int32',
                None, None,
                [('-2147483648', '2147483647')], [],
                '''                ISIS Propogate To Level
                ''',
                'propogate_to',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('route-policy-name', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                Policy that uses object in question
                ''',
                'route_policy_name',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('attached-policy', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                The attached policy that (maybe indirectly) uses
                the object in question
                ''',
                'attached_policy',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('attach-point', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                Name of attach point where policy is attached
                ''',
                'attach_point',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            ],
            'Cisco-IOS-XR-policy-repository-oper',
            'binding',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-policy-repository-oper'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper',
            is_config=False,
        ),
    },
    'RoutingPolicy.Policies.RoutePolicies.RoutePolicy.Attached' : {
        'meta_info' : _MetaInfoClass('RoutingPolicy.Policies.RoutePolicies.RoutePolicy.Attached', REFERENCE_CLASS,
            '''Information about where this policy or set is
attached''',
            False, 
            [
            _MetaInfoClassMember('binding', REFERENCE_LIST, 'Binding', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper', 'RoutingPolicy.Policies.RoutePolicies.RoutePolicy.Attached.Binding',
                [], [],
                '''                bindings list
                ''',
                'binding',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            ],
            'Cisco-IOS-XR-policy-repository-oper',
            'attached',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-policy-repository-oper'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper',
            is_config=False,
        ),
    },
    'RoutingPolicy.Policies.RoutePolicies.RoutePolicy' : {
        'meta_info' : _MetaInfoClass('RoutingPolicy.Policies.RoutePolicies.RoutePolicy', REFERENCE_LIST,
            '''Information about an individual policy''',
            False, 
            [
            _MetaInfoClassMember('route-policy-name', ATTRIBUTE, 'str', 'xr:Cisco-ios-xr-string',
                None, None,
                [], [b'[\\w\\-\\.:,_@#%$\\+=\\|;]+'],
                '''                Route policy name
                ''',
                'route_policy_name',
                'Cisco-IOS-XR-policy-repository-oper', True, is_config=False),
            _MetaInfoClassMember('policy-uses', REFERENCE_CLASS, 'PolicyUses', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper', 'RoutingPolicy.Policies.RoutePolicies.RoutePolicy.PolicyUses',
                [], [],
                '''                Information about which policies and sets
                this policy uses
                ''',
                'policy_uses',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('used-by', REFERENCE_CLASS, 'UsedBy', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper', 'RoutingPolicy.Policies.RoutePolicies.RoutePolicy.UsedBy',
                [], [],
                '''                Policies that use this object, directly or
                indirectly
                ''',
                'used_by',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('attached', REFERENCE_CLASS, 'Attached', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper', 'RoutingPolicy.Policies.RoutePolicies.RoutePolicy.Attached',
                [], [],
                '''                Information about where this policy or set is
                attached
                ''',
                'attached',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            ],
            'Cisco-IOS-XR-policy-repository-oper',
            'route-policy',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-policy-repository-oper'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper',
            is_config=False,
        ),
    },
    'RoutingPolicy.Policies.RoutePolicies' : {
        'meta_info' : _MetaInfoClass('RoutingPolicy.Policies.RoutePolicies', REFERENCE_CLASS,
            '''Information about individual policies''',
            False, 
            [
            _MetaInfoClassMember('route-policy', REFERENCE_LIST, 'RoutePolicy', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper', 'RoutingPolicy.Policies.RoutePolicies.RoutePolicy',
                [], [],
                '''                Information about an individual policy
                ''',
                'route_policy',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            ],
            'Cisco-IOS-XR-policy-repository-oper',
            'route-policies',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-policy-repository-oper'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper',
            is_config=False,
        ),
    },
    'RoutingPolicy.Policies.Unused' : {
        'meta_info' : _MetaInfoClass('RoutingPolicy.Policies.Unused', REFERENCE_CLASS,
            '''All objects of a given type that are not
referenced at all''',
            False, 
            [
            _MetaInfoClassMember('object', REFERENCE_LEAFLIST, 'str', 'String',
                None, None,
                [], [],
                '''                Policy objects
                ''',
                'object',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            ],
            'Cisco-IOS-XR-policy-repository-oper',
            'unused',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-policy-repository-oper'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper',
            is_config=False,
        ),
    },
    'RoutingPolicy.Policies.Inactive' : {
        'meta_info' : _MetaInfoClass('RoutingPolicy.Policies.Inactive', REFERENCE_CLASS,
            '''All objects of a given type that are not
attached to a protocol''',
            False, 
            [
            _MetaInfoClassMember('object', REFERENCE_LEAFLIST, 'str', 'String',
                None, None,
                [], [],
                '''                Policy objects
                ''',
                'object',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            ],
            'Cisco-IOS-XR-policy-repository-oper',
            'inactive',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-policy-repository-oper'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper',
            is_config=False,
        ),
    },
    'RoutingPolicy.Policies.Active' : {
        'meta_info' : _MetaInfoClass('RoutingPolicy.Policies.Active', REFERENCE_CLASS,
            '''All objects of a given type that are attached to
a protocol''',
            False, 
            [
            _MetaInfoClassMember('object', REFERENCE_LEAFLIST, 'str', 'String',
                None, None,
                [], [],
                '''                Policy objects
                ''',
                'object',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            ],
            'Cisco-IOS-XR-policy-repository-oper',
            'active',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-policy-repository-oper'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper',
            is_config=False,
        ),
    },
    'RoutingPolicy.Policies' : {
        'meta_info' : _MetaInfoClass('RoutingPolicy.Policies', REFERENCE_CLASS,
            '''Information about configured route policies''',
            False, 
            [
            _MetaInfoClassMember('route-policies', REFERENCE_CLASS, 'RoutePolicies', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper', 'RoutingPolicy.Policies.RoutePolicies',
                [], [],
                '''                Information about individual policies
                ''',
                'route_policies',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('unused', REFERENCE_CLASS, 'Unused', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper', 'RoutingPolicy.Policies.Unused',
                [], [],
                '''                All objects of a given type that are not
                referenced at all
                ''',
                'unused',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('inactive', REFERENCE_CLASS, 'Inactive', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper', 'RoutingPolicy.Policies.Inactive',
                [], [],
                '''                All objects of a given type that are not
                attached to a protocol
                ''',
                'inactive',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('active', REFERENCE_CLASS, 'Active', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper', 'RoutingPolicy.Policies.Active',
                [], [],
                '''                All objects of a given type that are attached to
                a protocol
                ''',
                'active',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            ],
            'Cisco-IOS-XR-policy-repository-oper',
            'policies',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-policy-repository-oper'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper',
            is_config=False,
        ),
    },
    'RoutingPolicy.Sets.Etag.Sets_.Set.UsedBy.Reference' : {
        'meta_info' : _MetaInfoClass('RoutingPolicy.Sets.Etag.Sets_.Set.UsedBy.Reference', REFERENCE_LIST,
            '''Information about policies referring to this
object''',
            False, 
            [
            _MetaInfoClassMember('route-policy-name', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                Name of policy
                ''',
                'route_policy_name',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('used-directly', ATTRIBUTE, 'bool', 'boolean',
                None, None,
                [], [],
                '''                Whether the policy uses this object directly or
                indirectly
                ''',
                'used_directly',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('status', REFERENCE_ENUM_CLASS, 'ObjectStatus', 'Object-status',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper', 'ObjectStatus',
                [], [],
                '''                Active, Inactive, or Unused
                ''',
                'status',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            ],
            'Cisco-IOS-XR-policy-repository-oper',
            'reference',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-policy-repository-oper'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper',
            is_config=False,
        ),
    },
    'RoutingPolicy.Sets.Etag.Sets_.Set.UsedBy' : {
        'meta_info' : _MetaInfoClass('RoutingPolicy.Sets.Etag.Sets_.Set.UsedBy', REFERENCE_CLASS,
            '''Policies that use this object, directly or
indirectly''',
            False, 
            [
            _MetaInfoClassMember('reference', REFERENCE_LIST, 'Reference', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper', 'RoutingPolicy.Sets.Etag.Sets_.Set.UsedBy.Reference',
                [], [],
                '''                Information about policies referring to this
                object
                ''',
                'reference',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            ],
            'Cisco-IOS-XR-policy-repository-oper',
            'used-by',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-policy-repository-oper'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper',
            is_config=False,
        ),
    },
    'RoutingPolicy.Sets.Etag.Sets_.Set.Attached.Binding' : {
        'meta_info' : _MetaInfoClass('RoutingPolicy.Sets.Etag.Sets_.Set.Attached.Binding', REFERENCE_LIST,
            '''bindings list''',
            False, 
            [
            _MetaInfoClassMember('protocol', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                Protocol to which policy attached
                ''',
                'protocol',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('vrf-name', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                VRF name
                ''',
                'vrf_name',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('proto-instance', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                Protocol instance
                ''',
                'proto_instance',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('af-name', REFERENCE_ENUM_CLASS, 'AddressFamily', 'Address-family',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper', 'AddressFamily',
                [], [],
                '''                Address Family Identifier
                ''',
                'af_name',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('saf-name', REFERENCE_ENUM_CLASS, 'SubAddressFamily', 'Sub-address-family',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper', 'SubAddressFamily',
                [], [],
                '''                Subsequent Address Family Identifier
                ''',
                'saf_name',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('neighbor-address', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                Neighbor IP Address
                ''',
                'neighbor_address',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('neighbor-af-name', REFERENCE_ENUM_CLASS, 'AddressFamily', 'Address-family',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper', 'AddressFamily',
                [], [],
                '''                Neighbor IP Address Family
                ''',
                'neighbor_af_name',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('group-name', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                Neighbor Group Name
                ''',
                'group_name',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('direction', REFERENCE_ENUM_CLASS, 'AttachPointDirection', 'Attach-point-direction',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper', 'AttachPointDirection',
                [], [],
                '''                Direction In or Out
                ''',
                'direction',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('group', REFERENCE_ENUM_CLASS, 'Group', 'Group',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper', 'Group',
                [], [],
                '''                Neighbor Group 
                ''',
                'group',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('source-protocol', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                Source Protocol to redistribute, Source Protocol
                can be one of the following values{all,
                connected, local, static, bgp, rip, isis, ospf
                ,ospfv3, eigrp, unknown }
                ''',
                'source_protocol',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('aggregate-network-address', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                Aggregate IP address or Network IP Address in
                IPv4 or IPv6 Format
                ''',
                'aggregate_network_address',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('interface-name', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                Interface Name
                ''',
                'interface_name',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('instance', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                Instance
                ''',
                'instance',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('area-id', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                OSPF Area ID in Decimal Integer Format
                ''',
                'area_id',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('propogate-from', ATTRIBUTE, 'int', 'int32',
                None, None,
                [('-2147483648', '2147483647')], [],
                '''                ISIS Propogate From Level
                ''',
                'propogate_from',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('propogate-to', ATTRIBUTE, 'int', 'int32',
                None, None,
                [('-2147483648', '2147483647')], [],
                '''                ISIS Propogate To Level
                ''',
                'propogate_to',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('route-policy-name', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                Policy that uses object in question
                ''',
                'route_policy_name',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('attached-policy', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                The attached policy that (maybe indirectly) uses
                the object in question
                ''',
                'attached_policy',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('attach-point', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                Name of attach point where policy is attached
                ''',
                'attach_point',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            ],
            'Cisco-IOS-XR-policy-repository-oper',
            'binding',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-policy-repository-oper'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper',
            is_config=False,
        ),
    },
    'RoutingPolicy.Sets.Etag.Sets_.Set.Attached' : {
        'meta_info' : _MetaInfoClass('RoutingPolicy.Sets.Etag.Sets_.Set.Attached', REFERENCE_CLASS,
            '''Information about where this policy or set is
attached''',
            False, 
            [
            _MetaInfoClassMember('binding', REFERENCE_LIST, 'Binding', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper', 'RoutingPolicy.Sets.Etag.Sets_.Set.Attached.Binding',
                [], [],
                '''                bindings list
                ''',
                'binding',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            ],
            'Cisco-IOS-XR-policy-repository-oper',
            'attached',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-policy-repository-oper'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper',
            is_config=False,
        ),
    },
    'RoutingPolicy.Sets.Etag.Sets_.Set' : {
        'meta_info' : _MetaInfoClass('RoutingPolicy.Sets.Etag.Sets_.Set', REFERENCE_LIST,
            '''Information about an individual set''',
            False, 
            [
            _MetaInfoClassMember('set-name', ATTRIBUTE, 'str', 'xr:Cisco-ios-xr-string',
                None, None,
                [], [b'[\\w\\-\\.:,_@#%$\\+=\\|;]+'],
                '''                Set name
                ''',
                'set_name',
                'Cisco-IOS-XR-policy-repository-oper', True, is_config=False),
            _MetaInfoClassMember('used-by', REFERENCE_CLASS, 'UsedBy', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper', 'RoutingPolicy.Sets.Etag.Sets_.Set.UsedBy',
                [], [],
                '''                Policies that use this object, directly or
                indirectly
                ''',
                'used_by',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('attached', REFERENCE_CLASS, 'Attached', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper', 'RoutingPolicy.Sets.Etag.Sets_.Set.Attached',
                [], [],
                '''                Information about where this policy or set is
                attached
                ''',
                'attached',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            ],
            'Cisco-IOS-XR-policy-repository-oper',
            'set',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-policy-repository-oper'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper',
            is_config=False,
        ),
    },
    'RoutingPolicy.Sets.Etag.Sets_' : {
        'meta_info' : _MetaInfoClass('RoutingPolicy.Sets.Etag.Sets_', REFERENCE_CLASS,
            '''Information about individual sets''',
            False, 
            [
            _MetaInfoClassMember('set', REFERENCE_LIST, 'Set', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper', 'RoutingPolicy.Sets.Etag.Sets_.Set',
                [], [],
                '''                Information about an individual set
                ''',
                'set',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            ],
            'Cisco-IOS-XR-policy-repository-oper',
            'sets',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-policy-repository-oper'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper',
            is_config=False,
        ),
    },
    'RoutingPolicy.Sets.Etag.Unused' : {
        'meta_info' : _MetaInfoClass('RoutingPolicy.Sets.Etag.Unused', REFERENCE_CLASS,
            '''All objects of a given type that are not
referenced at all''',
            False, 
            [
            _MetaInfoClassMember('object', REFERENCE_LEAFLIST, 'str', 'String',
                None, None,
                [], [],
                '''                Policy objects
                ''',
                'object',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            ],
            'Cisco-IOS-XR-policy-repository-oper',
            'unused',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-policy-repository-oper'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper',
            is_config=False,
        ),
    },
    'RoutingPolicy.Sets.Etag.Inactive' : {
        'meta_info' : _MetaInfoClass('RoutingPolicy.Sets.Etag.Inactive', REFERENCE_CLASS,
            '''All objects of a given type that are not
attached to a protocol''',
            False, 
            [
            _MetaInfoClassMember('object', REFERENCE_LEAFLIST, 'str', 'String',
                None, None,
                [], [],
                '''                Policy objects
                ''',
                'object',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            ],
            'Cisco-IOS-XR-policy-repository-oper',
            'inactive',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-policy-repository-oper'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper',
            is_config=False,
        ),
    },
    'RoutingPolicy.Sets.Etag.Active' : {
        'meta_info' : _MetaInfoClass('RoutingPolicy.Sets.Etag.Active', REFERENCE_CLASS,
            '''All objects of a given type that are attached to
a protocol''',
            False, 
            [
            _MetaInfoClassMember('object', REFERENCE_LEAFLIST, 'str', 'String',
                None, None,
                [], [],
                '''                Policy objects
                ''',
                'object',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            ],
            'Cisco-IOS-XR-policy-repository-oper',
            'active',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-policy-repository-oper'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper',
            is_config=False,
        ),
    },
    'RoutingPolicy.Sets.Etag' : {
        'meta_info' : _MetaInfoClass('RoutingPolicy.Sets.Etag', REFERENCE_CLASS,
            '''Information about Etag sets''',
            False, 
            [
            _MetaInfoClassMember('sets', REFERENCE_CLASS, 'Sets_', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper', 'RoutingPolicy.Sets.Etag.Sets_',
                [], [],
                '''                Information about individual sets
                ''',
                'sets',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('unused', REFERENCE_CLASS, 'Unused', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper', 'RoutingPolicy.Sets.Etag.Unused',
                [], [],
                '''                All objects of a given type that are not
                referenced at all
                ''',
                'unused',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('inactive', REFERENCE_CLASS, 'Inactive', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper', 'RoutingPolicy.Sets.Etag.Inactive',
                [], [],
                '''                All objects of a given type that are not
                attached to a protocol
                ''',
                'inactive',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('active', REFERENCE_CLASS, 'Active', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper', 'RoutingPolicy.Sets.Etag.Active',
                [], [],
                '''                All objects of a given type that are attached to
                a protocol
                ''',
                'active',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            ],
            'Cisco-IOS-XR-policy-repository-oper',
            'etag',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-policy-repository-oper'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper',
            is_config=False,
        ),
    },
    'RoutingPolicy.Sets.OspfArea.Sets_.Set.UsedBy.Reference' : {
        'meta_info' : _MetaInfoClass('RoutingPolicy.Sets.OspfArea.Sets_.Set.UsedBy.Reference', REFERENCE_LIST,
            '''Information about policies referring to this
object''',
            False, 
            [
            _MetaInfoClassMember('route-policy-name', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                Name of policy
                ''',
                'route_policy_name',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('used-directly', ATTRIBUTE, 'bool', 'boolean',
                None, None,
                [], [],
                '''                Whether the policy uses this object directly or
                indirectly
                ''',
                'used_directly',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('status', REFERENCE_ENUM_CLASS, 'ObjectStatus', 'Object-status',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper', 'ObjectStatus',
                [], [],
                '''                Active, Inactive, or Unused
                ''',
                'status',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            ],
            'Cisco-IOS-XR-policy-repository-oper',
            'reference',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-policy-repository-oper'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper',
            is_config=False,
        ),
    },
    'RoutingPolicy.Sets.OspfArea.Sets_.Set.UsedBy' : {
        'meta_info' : _MetaInfoClass('RoutingPolicy.Sets.OspfArea.Sets_.Set.UsedBy', REFERENCE_CLASS,
            '''Policies that use this object, directly or
indirectly''',
            False, 
            [
            _MetaInfoClassMember('reference', REFERENCE_LIST, 'Reference', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper', 'RoutingPolicy.Sets.OspfArea.Sets_.Set.UsedBy.Reference',
                [], [],
                '''                Information about policies referring to this
                object
                ''',
                'reference',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            ],
            'Cisco-IOS-XR-policy-repository-oper',
            'used-by',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-policy-repository-oper'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper',
            is_config=False,
        ),
    },
    'RoutingPolicy.Sets.OspfArea.Sets_.Set.Attached.Binding' : {
        'meta_info' : _MetaInfoClass('RoutingPolicy.Sets.OspfArea.Sets_.Set.Attached.Binding', REFERENCE_LIST,
            '''bindings list''',
            False, 
            [
            _MetaInfoClassMember('protocol', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                Protocol to which policy attached
                ''',
                'protocol',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('vrf-name', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                VRF name
                ''',
                'vrf_name',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('proto-instance', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                Protocol instance
                ''',
                'proto_instance',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('af-name', REFERENCE_ENUM_CLASS, 'AddressFamily', 'Address-family',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper', 'AddressFamily',
                [], [],
                '''                Address Family Identifier
                ''',
                'af_name',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('saf-name', REFERENCE_ENUM_CLASS, 'SubAddressFamily', 'Sub-address-family',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper', 'SubAddressFamily',
                [], [],
                '''                Subsequent Address Family Identifier
                ''',
                'saf_name',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('neighbor-address', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                Neighbor IP Address
                ''',
                'neighbor_address',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('neighbor-af-name', REFERENCE_ENUM_CLASS, 'AddressFamily', 'Address-family',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper', 'AddressFamily',
                [], [],
                '''                Neighbor IP Address Family
                ''',
                'neighbor_af_name',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('group-name', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                Neighbor Group Name
                ''',
                'group_name',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('direction', REFERENCE_ENUM_CLASS, 'AttachPointDirection', 'Attach-point-direction',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper', 'AttachPointDirection',
                [], [],
                '''                Direction In or Out
                ''',
                'direction',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('group', REFERENCE_ENUM_CLASS, 'Group', 'Group',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper', 'Group',
                [], [],
                '''                Neighbor Group 
                ''',
                'group',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('source-protocol', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                Source Protocol to redistribute, Source Protocol
                can be one of the following values{all,
                connected, local, static, bgp, rip, isis, ospf
                ,ospfv3, eigrp, unknown }
                ''',
                'source_protocol',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('aggregate-network-address', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                Aggregate IP address or Network IP Address in
                IPv4 or IPv6 Format
                ''',
                'aggregate_network_address',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('interface-name', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                Interface Name
                ''',
                'interface_name',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('instance', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                Instance
                ''',
                'instance',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('area-id', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                OSPF Area ID in Decimal Integer Format
                ''',
                'area_id',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('propogate-from', ATTRIBUTE, 'int', 'int32',
                None, None,
                [('-2147483648', '2147483647')], [],
                '''                ISIS Propogate From Level
                ''',
                'propogate_from',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('propogate-to', ATTRIBUTE, 'int', 'int32',
                None, None,
                [('-2147483648', '2147483647')], [],
                '''                ISIS Propogate To Level
                ''',
                'propogate_to',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('route-policy-name', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                Policy that uses object in question
                ''',
                'route_policy_name',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('attached-policy', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                The attached policy that (maybe indirectly) uses
                the object in question
                ''',
                'attached_policy',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('attach-point', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                Name of attach point where policy is attached
                ''',
                'attach_point',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            ],
            'Cisco-IOS-XR-policy-repository-oper',
            'binding',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-policy-repository-oper'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper',
            is_config=False,
        ),
    },
    'RoutingPolicy.Sets.OspfArea.Sets_.Set.Attached' : {
        'meta_info' : _MetaInfoClass('RoutingPolicy.Sets.OspfArea.Sets_.Set.Attached', REFERENCE_CLASS,
            '''Information about where this policy or set is
attached''',
            False, 
            [
            _MetaInfoClassMember('binding', REFERENCE_LIST, 'Binding', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper', 'RoutingPolicy.Sets.OspfArea.Sets_.Set.Attached.Binding',
                [], [],
                '''                bindings list
                ''',
                'binding',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            ],
            'Cisco-IOS-XR-policy-repository-oper',
            'attached',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-policy-repository-oper'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper',
            is_config=False,
        ),
    },
    'RoutingPolicy.Sets.OspfArea.Sets_.Set' : {
        'meta_info' : _MetaInfoClass('RoutingPolicy.Sets.OspfArea.Sets_.Set', REFERENCE_LIST,
            '''Information about an individual set''',
            False, 
            [
            _MetaInfoClassMember('set-name', ATTRIBUTE, 'str', 'xr:Cisco-ios-xr-string',
                None, None,
                [], [b'[\\w\\-\\.:,_@#%$\\+=\\|;]+'],
                '''                Set name
                ''',
                'set_name',
                'Cisco-IOS-XR-policy-repository-oper', True, is_config=False),
            _MetaInfoClassMember('used-by', REFERENCE_CLASS, 'UsedBy', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper', 'RoutingPolicy.Sets.OspfArea.Sets_.Set.UsedBy',
                [], [],
                '''                Policies that use this object, directly or
                indirectly
                ''',
                'used_by',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('attached', REFERENCE_CLASS, 'Attached', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper', 'RoutingPolicy.Sets.OspfArea.Sets_.Set.Attached',
                [], [],
                '''                Information about where this policy or set is
                attached
                ''',
                'attached',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            ],
            'Cisco-IOS-XR-policy-repository-oper',
            'set',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-policy-repository-oper'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper',
            is_config=False,
        ),
    },
    'RoutingPolicy.Sets.OspfArea.Sets_' : {
        'meta_info' : _MetaInfoClass('RoutingPolicy.Sets.OspfArea.Sets_', REFERENCE_CLASS,
            '''Information about individual sets''',
            False, 
            [
            _MetaInfoClassMember('set', REFERENCE_LIST, 'Set', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper', 'RoutingPolicy.Sets.OspfArea.Sets_.Set',
                [], [],
                '''                Information about an individual set
                ''',
                'set',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            ],
            'Cisco-IOS-XR-policy-repository-oper',
            'sets',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-policy-repository-oper'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper',
            is_config=False,
        ),
    },
    'RoutingPolicy.Sets.OspfArea.Unused' : {
        'meta_info' : _MetaInfoClass('RoutingPolicy.Sets.OspfArea.Unused', REFERENCE_CLASS,
            '''All objects of a given type that are not
referenced at all''',
            False, 
            [
            _MetaInfoClassMember('object', REFERENCE_LEAFLIST, 'str', 'String',
                None, None,
                [], [],
                '''                Policy objects
                ''',
                'object',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            ],
            'Cisco-IOS-XR-policy-repository-oper',
            'unused',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-policy-repository-oper'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper',
            is_config=False,
        ),
    },
    'RoutingPolicy.Sets.OspfArea.Inactive' : {
        'meta_info' : _MetaInfoClass('RoutingPolicy.Sets.OspfArea.Inactive', REFERENCE_CLASS,
            '''All objects of a given type that are not
attached to a protocol''',
            False, 
            [
            _MetaInfoClassMember('object', REFERENCE_LEAFLIST, 'str', 'String',
                None, None,
                [], [],
                '''                Policy objects
                ''',
                'object',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            ],
            'Cisco-IOS-XR-policy-repository-oper',
            'inactive',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-policy-repository-oper'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper',
            is_config=False,
        ),
    },
    'RoutingPolicy.Sets.OspfArea.Active' : {
        'meta_info' : _MetaInfoClass('RoutingPolicy.Sets.OspfArea.Active', REFERENCE_CLASS,
            '''All objects of a given type that are attached to
a protocol''',
            False, 
            [
            _MetaInfoClassMember('object', REFERENCE_LEAFLIST, 'str', 'String',
                None, None,
                [], [],
                '''                Policy objects
                ''',
                'object',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            ],
            'Cisco-IOS-XR-policy-repository-oper',
            'active',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-policy-repository-oper'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper',
            is_config=False,
        ),
    },
    'RoutingPolicy.Sets.OspfArea' : {
        'meta_info' : _MetaInfoClass('RoutingPolicy.Sets.OspfArea', REFERENCE_CLASS,
            '''Information about OSPF Area sets''',
            False, 
            [
            _MetaInfoClassMember('sets', REFERENCE_CLASS, 'Sets_', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper', 'RoutingPolicy.Sets.OspfArea.Sets_',
                [], [],
                '''                Information about individual sets
                ''',
                'sets',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('unused', REFERENCE_CLASS, 'Unused', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper', 'RoutingPolicy.Sets.OspfArea.Unused',
                [], [],
                '''                All objects of a given type that are not
                referenced at all
                ''',
                'unused',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('inactive', REFERENCE_CLASS, 'Inactive', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper', 'RoutingPolicy.Sets.OspfArea.Inactive',
                [], [],
                '''                All objects of a given type that are not
                attached to a protocol
                ''',
                'inactive',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('active', REFERENCE_CLASS, 'Active', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper', 'RoutingPolicy.Sets.OspfArea.Active',
                [], [],
                '''                All objects of a given type that are attached to
                a protocol
                ''',
                'active',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            ],
            'Cisco-IOS-XR-policy-repository-oper',
            'ospf-area',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-policy-repository-oper'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper',
            is_config=False,
        ),
    },
    'RoutingPolicy.Sets.ExtendedCommunityOpaque.Sets_.Set.UsedBy.Reference' : {
        'meta_info' : _MetaInfoClass('RoutingPolicy.Sets.ExtendedCommunityOpaque.Sets_.Set.UsedBy.Reference', REFERENCE_LIST,
            '''Information about policies referring to this
object''',
            False, 
            [
            _MetaInfoClassMember('route-policy-name', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                Name of policy
                ''',
                'route_policy_name',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('used-directly', ATTRIBUTE, 'bool', 'boolean',
                None, None,
                [], [],
                '''                Whether the policy uses this object directly or
                indirectly
                ''',
                'used_directly',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('status', REFERENCE_ENUM_CLASS, 'ObjectStatus', 'Object-status',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper', 'ObjectStatus',
                [], [],
                '''                Active, Inactive, or Unused
                ''',
                'status',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            ],
            'Cisco-IOS-XR-policy-repository-oper',
            'reference',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-policy-repository-oper'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper',
            is_config=False,
        ),
    },
    'RoutingPolicy.Sets.ExtendedCommunityOpaque.Sets_.Set.UsedBy' : {
        'meta_info' : _MetaInfoClass('RoutingPolicy.Sets.ExtendedCommunityOpaque.Sets_.Set.UsedBy', REFERENCE_CLASS,
            '''Policies that use this object, directly or
indirectly''',
            False, 
            [
            _MetaInfoClassMember('reference', REFERENCE_LIST, 'Reference', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper', 'RoutingPolicy.Sets.ExtendedCommunityOpaque.Sets_.Set.UsedBy.Reference',
                [], [],
                '''                Information about policies referring to this
                object
                ''',
                'reference',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            ],
            'Cisco-IOS-XR-policy-repository-oper',
            'used-by',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-policy-repository-oper'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper',
            is_config=False,
        ),
    },
    'RoutingPolicy.Sets.ExtendedCommunityOpaque.Sets_.Set.Attached.Binding' : {
        'meta_info' : _MetaInfoClass('RoutingPolicy.Sets.ExtendedCommunityOpaque.Sets_.Set.Attached.Binding', REFERENCE_LIST,
            '''bindings list''',
            False, 
            [
            _MetaInfoClassMember('protocol', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                Protocol to which policy attached
                ''',
                'protocol',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('vrf-name', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                VRF name
                ''',
                'vrf_name',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('proto-instance', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                Protocol instance
                ''',
                'proto_instance',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('af-name', REFERENCE_ENUM_CLASS, 'AddressFamily', 'Address-family',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper', 'AddressFamily',
                [], [],
                '''                Address Family Identifier
                ''',
                'af_name',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('saf-name', REFERENCE_ENUM_CLASS, 'SubAddressFamily', 'Sub-address-family',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper', 'SubAddressFamily',
                [], [],
                '''                Subsequent Address Family Identifier
                ''',
                'saf_name',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('neighbor-address', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                Neighbor IP Address
                ''',
                'neighbor_address',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('neighbor-af-name', REFERENCE_ENUM_CLASS, 'AddressFamily', 'Address-family',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper', 'AddressFamily',
                [], [],
                '''                Neighbor IP Address Family
                ''',
                'neighbor_af_name',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('group-name', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                Neighbor Group Name
                ''',
                'group_name',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('direction', REFERENCE_ENUM_CLASS, 'AttachPointDirection', 'Attach-point-direction',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper', 'AttachPointDirection',
                [], [],
                '''                Direction In or Out
                ''',
                'direction',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('group', REFERENCE_ENUM_CLASS, 'Group', 'Group',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper', 'Group',
                [], [],
                '''                Neighbor Group 
                ''',
                'group',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('source-protocol', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                Source Protocol to redistribute, Source Protocol
                can be one of the following values{all,
                connected, local, static, bgp, rip, isis, ospf
                ,ospfv3, eigrp, unknown }
                ''',
                'source_protocol',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('aggregate-network-address', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                Aggregate IP address or Network IP Address in
                IPv4 or IPv6 Format
                ''',
                'aggregate_network_address',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('interface-name', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                Interface Name
                ''',
                'interface_name',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('instance', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                Instance
                ''',
                'instance',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('area-id', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                OSPF Area ID in Decimal Integer Format
                ''',
                'area_id',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('propogate-from', ATTRIBUTE, 'int', 'int32',
                None, None,
                [('-2147483648', '2147483647')], [],
                '''                ISIS Propogate From Level
                ''',
                'propogate_from',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('propogate-to', ATTRIBUTE, 'int', 'int32',
                None, None,
                [('-2147483648', '2147483647')], [],
                '''                ISIS Propogate To Level
                ''',
                'propogate_to',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('route-policy-name', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                Policy that uses object in question
                ''',
                'route_policy_name',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('attached-policy', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                The attached policy that (maybe indirectly) uses
                the object in question
                ''',
                'attached_policy',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('attach-point', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                Name of attach point where policy is attached
                ''',
                'attach_point',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            ],
            'Cisco-IOS-XR-policy-repository-oper',
            'binding',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-policy-repository-oper'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper',
            is_config=False,
        ),
    },
    'RoutingPolicy.Sets.ExtendedCommunityOpaque.Sets_.Set.Attached' : {
        'meta_info' : _MetaInfoClass('RoutingPolicy.Sets.ExtendedCommunityOpaque.Sets_.Set.Attached', REFERENCE_CLASS,
            '''Information about where this policy or set is
attached''',
            False, 
            [
            _MetaInfoClassMember('binding', REFERENCE_LIST, 'Binding', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper', 'RoutingPolicy.Sets.ExtendedCommunityOpaque.Sets_.Set.Attached.Binding',
                [], [],
                '''                bindings list
                ''',
                'binding',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            ],
            'Cisco-IOS-XR-policy-repository-oper',
            'attached',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-policy-repository-oper'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper',
            is_config=False,
        ),
    },
    'RoutingPolicy.Sets.ExtendedCommunityOpaque.Sets_.Set' : {
        'meta_info' : _MetaInfoClass('RoutingPolicy.Sets.ExtendedCommunityOpaque.Sets_.Set', REFERENCE_LIST,
            '''Information about an individual set''',
            False, 
            [
            _MetaInfoClassMember('set-name', ATTRIBUTE, 'str', 'xr:Cisco-ios-xr-string',
                None, None,
                [], [b'[\\w\\-\\.:,_@#%$\\+=\\|;]+'],
                '''                Set name
                ''',
                'set_name',
                'Cisco-IOS-XR-policy-repository-oper', True, is_config=False),
            _MetaInfoClassMember('used-by', REFERENCE_CLASS, 'UsedBy', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper', 'RoutingPolicy.Sets.ExtendedCommunityOpaque.Sets_.Set.UsedBy',
                [], [],
                '''                Policies that use this object, directly or
                indirectly
                ''',
                'used_by',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('attached', REFERENCE_CLASS, 'Attached', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper', 'RoutingPolicy.Sets.ExtendedCommunityOpaque.Sets_.Set.Attached',
                [], [],
                '''                Information about where this policy or set is
                attached
                ''',
                'attached',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            ],
            'Cisco-IOS-XR-policy-repository-oper',
            'set',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-policy-repository-oper'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper',
            is_config=False,
        ),
    },
    'RoutingPolicy.Sets.ExtendedCommunityOpaque.Sets_' : {
        'meta_info' : _MetaInfoClass('RoutingPolicy.Sets.ExtendedCommunityOpaque.Sets_', REFERENCE_CLASS,
            '''Information about individual sets''',
            False, 
            [
            _MetaInfoClassMember('set', REFERENCE_LIST, 'Set', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper', 'RoutingPolicy.Sets.ExtendedCommunityOpaque.Sets_.Set',
                [], [],
                '''                Information about an individual set
                ''',
                'set',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            ],
            'Cisco-IOS-XR-policy-repository-oper',
            'sets',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-policy-repository-oper'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper',
            is_config=False,
        ),
    },
    'RoutingPolicy.Sets.ExtendedCommunityOpaque.Unused' : {
        'meta_info' : _MetaInfoClass('RoutingPolicy.Sets.ExtendedCommunityOpaque.Unused', REFERENCE_CLASS,
            '''All objects of a given type that are not
referenced at all''',
            False, 
            [
            _MetaInfoClassMember('object', REFERENCE_LEAFLIST, 'str', 'String',
                None, None,
                [], [],
                '''                Policy objects
                ''',
                'object',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            ],
            'Cisco-IOS-XR-policy-repository-oper',
            'unused',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-policy-repository-oper'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper',
            is_config=False,
        ),
    },
    'RoutingPolicy.Sets.ExtendedCommunityOpaque.Inactive' : {
        'meta_info' : _MetaInfoClass('RoutingPolicy.Sets.ExtendedCommunityOpaque.Inactive', REFERENCE_CLASS,
            '''All objects of a given type that are not
attached to a protocol''',
            False, 
            [
            _MetaInfoClassMember('object', REFERENCE_LEAFLIST, 'str', 'String',
                None, None,
                [], [],
                '''                Policy objects
                ''',
                'object',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            ],
            'Cisco-IOS-XR-policy-repository-oper',
            'inactive',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-policy-repository-oper'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper',
            is_config=False,
        ),
    },
    'RoutingPolicy.Sets.ExtendedCommunityOpaque.Active' : {
        'meta_info' : _MetaInfoClass('RoutingPolicy.Sets.ExtendedCommunityOpaque.Active', REFERENCE_CLASS,
            '''All objects of a given type that are attached to
a protocol''',
            False, 
            [
            _MetaInfoClassMember('object', REFERENCE_LEAFLIST, 'str', 'String',
                None, None,
                [], [],
                '''                Policy objects
                ''',
                'object',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            ],
            'Cisco-IOS-XR-policy-repository-oper',
            'active',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-policy-repository-oper'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper',
            is_config=False,
        ),
    },
    'RoutingPolicy.Sets.ExtendedCommunityOpaque' : {
        'meta_info' : _MetaInfoClass('RoutingPolicy.Sets.ExtendedCommunityOpaque', REFERENCE_CLASS,
            '''Information about Extended Community Opaque
sets''',
            False, 
            [
            _MetaInfoClassMember('sets', REFERENCE_CLASS, 'Sets_', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper', 'RoutingPolicy.Sets.ExtendedCommunityOpaque.Sets_',
                [], [],
                '''                Information about individual sets
                ''',
                'sets',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('unused', REFERENCE_CLASS, 'Unused', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper', 'RoutingPolicy.Sets.ExtendedCommunityOpaque.Unused',
                [], [],
                '''                All objects of a given type that are not
                referenced at all
                ''',
                'unused',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('inactive', REFERENCE_CLASS, 'Inactive', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper', 'RoutingPolicy.Sets.ExtendedCommunityOpaque.Inactive',
                [], [],
                '''                All objects of a given type that are not
                attached to a protocol
                ''',
                'inactive',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('active', REFERENCE_CLASS, 'Active', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper', 'RoutingPolicy.Sets.ExtendedCommunityOpaque.Active',
                [], [],
                '''                All objects of a given type that are attached to
                a protocol
                ''',
                'active',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            ],
            'Cisco-IOS-XR-policy-repository-oper',
            'extended-community-opaque',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-policy-repository-oper'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper',
            is_config=False,
        ),
    },
    'RoutingPolicy.Sets.ExtendedCommunitySegNh.Sets_.Set.UsedBy.Reference' : {
        'meta_info' : _MetaInfoClass('RoutingPolicy.Sets.ExtendedCommunitySegNh.Sets_.Set.UsedBy.Reference', REFERENCE_LIST,
            '''Information about policies referring to this
object''',
            False, 
            [
            _MetaInfoClassMember('route-policy-name', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                Name of policy
                ''',
                'route_policy_name',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('used-directly', ATTRIBUTE, 'bool', 'boolean',
                None, None,
                [], [],
                '''                Whether the policy uses this object directly or
                indirectly
                ''',
                'used_directly',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('status', REFERENCE_ENUM_CLASS, 'ObjectStatus', 'Object-status',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper', 'ObjectStatus',
                [], [],
                '''                Active, Inactive, or Unused
                ''',
                'status',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            ],
            'Cisco-IOS-XR-policy-repository-oper',
            'reference',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-policy-repository-oper'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper',
            is_config=False,
        ),
    },
    'RoutingPolicy.Sets.ExtendedCommunitySegNh.Sets_.Set.UsedBy' : {
        'meta_info' : _MetaInfoClass('RoutingPolicy.Sets.ExtendedCommunitySegNh.Sets_.Set.UsedBy', REFERENCE_CLASS,
            '''Policies that use this object, directly or
indirectly''',
            False, 
            [
            _MetaInfoClassMember('reference', REFERENCE_LIST, 'Reference', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper', 'RoutingPolicy.Sets.ExtendedCommunitySegNh.Sets_.Set.UsedBy.Reference',
                [], [],
                '''                Information about policies referring to this
                object
                ''',
                'reference',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            ],
            'Cisco-IOS-XR-policy-repository-oper',
            'used-by',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-policy-repository-oper'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper',
            is_config=False,
        ),
    },
    'RoutingPolicy.Sets.ExtendedCommunitySegNh.Sets_.Set.Attached.Binding' : {
        'meta_info' : _MetaInfoClass('RoutingPolicy.Sets.ExtendedCommunitySegNh.Sets_.Set.Attached.Binding', REFERENCE_LIST,
            '''bindings list''',
            False, 
            [
            _MetaInfoClassMember('protocol', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                Protocol to which policy attached
                ''',
                'protocol',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('vrf-name', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                VRF name
                ''',
                'vrf_name',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('proto-instance', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                Protocol instance
                ''',
                'proto_instance',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('af-name', REFERENCE_ENUM_CLASS, 'AddressFamily', 'Address-family',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper', 'AddressFamily',
                [], [],
                '''                Address Family Identifier
                ''',
                'af_name',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('saf-name', REFERENCE_ENUM_CLASS, 'SubAddressFamily', 'Sub-address-family',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper', 'SubAddressFamily',
                [], [],
                '''                Subsequent Address Family Identifier
                ''',
                'saf_name',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('neighbor-address', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                Neighbor IP Address
                ''',
                'neighbor_address',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('neighbor-af-name', REFERENCE_ENUM_CLASS, 'AddressFamily', 'Address-family',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper', 'AddressFamily',
                [], [],
                '''                Neighbor IP Address Family
                ''',
                'neighbor_af_name',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('group-name', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                Neighbor Group Name
                ''',
                'group_name',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('direction', REFERENCE_ENUM_CLASS, 'AttachPointDirection', 'Attach-point-direction',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper', 'AttachPointDirection',
                [], [],
                '''                Direction In or Out
                ''',
                'direction',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('group', REFERENCE_ENUM_CLASS, 'Group', 'Group',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper', 'Group',
                [], [],
                '''                Neighbor Group 
                ''',
                'group',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('source-protocol', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                Source Protocol to redistribute, Source Protocol
                can be one of the following values{all,
                connected, local, static, bgp, rip, isis, ospf
                ,ospfv3, eigrp, unknown }
                ''',
                'source_protocol',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('aggregate-network-address', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                Aggregate IP address or Network IP Address in
                IPv4 or IPv6 Format
                ''',
                'aggregate_network_address',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('interface-name', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                Interface Name
                ''',
                'interface_name',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('instance', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                Instance
                ''',
                'instance',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('area-id', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                OSPF Area ID in Decimal Integer Format
                ''',
                'area_id',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('propogate-from', ATTRIBUTE, 'int', 'int32',
                None, None,
                [('-2147483648', '2147483647')], [],
                '''                ISIS Propogate From Level
                ''',
                'propogate_from',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('propogate-to', ATTRIBUTE, 'int', 'int32',
                None, None,
                [('-2147483648', '2147483647')], [],
                '''                ISIS Propogate To Level
                ''',
                'propogate_to',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('route-policy-name', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                Policy that uses object in question
                ''',
                'route_policy_name',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('attached-policy', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                The attached policy that (maybe indirectly) uses
                the object in question
                ''',
                'attached_policy',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('attach-point', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                Name of attach point where policy is attached
                ''',
                'attach_point',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            ],
            'Cisco-IOS-XR-policy-repository-oper',
            'binding',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-policy-repository-oper'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper',
            is_config=False,
        ),
    },
    'RoutingPolicy.Sets.ExtendedCommunitySegNh.Sets_.Set.Attached' : {
        'meta_info' : _MetaInfoClass('RoutingPolicy.Sets.ExtendedCommunitySegNh.Sets_.Set.Attached', REFERENCE_CLASS,
            '''Information about where this policy or set is
attached''',
            False, 
            [
            _MetaInfoClassMember('binding', REFERENCE_LIST, 'Binding', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper', 'RoutingPolicy.Sets.ExtendedCommunitySegNh.Sets_.Set.Attached.Binding',
                [], [],
                '''                bindings list
                ''',
                'binding',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            ],
            'Cisco-IOS-XR-policy-repository-oper',
            'attached',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-policy-repository-oper'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper',
            is_config=False,
        ),
    },
    'RoutingPolicy.Sets.ExtendedCommunitySegNh.Sets_.Set' : {
        'meta_info' : _MetaInfoClass('RoutingPolicy.Sets.ExtendedCommunitySegNh.Sets_.Set', REFERENCE_LIST,
            '''Information about an individual set''',
            False, 
            [
            _MetaInfoClassMember('set-name', ATTRIBUTE, 'str', 'xr:Cisco-ios-xr-string',
                None, None,
                [], [b'[\\w\\-\\.:,_@#%$\\+=\\|;]+'],
                '''                Set name
                ''',
                'set_name',
                'Cisco-IOS-XR-policy-repository-oper', True, is_config=False),
            _MetaInfoClassMember('used-by', REFERENCE_CLASS, 'UsedBy', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper', 'RoutingPolicy.Sets.ExtendedCommunitySegNh.Sets_.Set.UsedBy',
                [], [],
                '''                Policies that use this object, directly or
                indirectly
                ''',
                'used_by',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('attached', REFERENCE_CLASS, 'Attached', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper', 'RoutingPolicy.Sets.ExtendedCommunitySegNh.Sets_.Set.Attached',
                [], [],
                '''                Information about where this policy or set is
                attached
                ''',
                'attached',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            ],
            'Cisco-IOS-XR-policy-repository-oper',
            'set',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-policy-repository-oper'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper',
            is_config=False,
        ),
    },
    'RoutingPolicy.Sets.ExtendedCommunitySegNh.Sets_' : {
        'meta_info' : _MetaInfoClass('RoutingPolicy.Sets.ExtendedCommunitySegNh.Sets_', REFERENCE_CLASS,
            '''Information about individual sets''',
            False, 
            [
            _MetaInfoClassMember('set', REFERENCE_LIST, 'Set', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper', 'RoutingPolicy.Sets.ExtendedCommunitySegNh.Sets_.Set',
                [], [],
                '''                Information about an individual set
                ''',
                'set',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            ],
            'Cisco-IOS-XR-policy-repository-oper',
            'sets',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-policy-repository-oper'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper',
            is_config=False,
        ),
    },
    'RoutingPolicy.Sets.ExtendedCommunitySegNh.Unused' : {
        'meta_info' : _MetaInfoClass('RoutingPolicy.Sets.ExtendedCommunitySegNh.Unused', REFERENCE_CLASS,
            '''All objects of a given type that are not
referenced at all''',
            False, 
            [
            _MetaInfoClassMember('object', REFERENCE_LEAFLIST, 'str', 'String',
                None, None,
                [], [],
                '''                Policy objects
                ''',
                'object',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            ],
            'Cisco-IOS-XR-policy-repository-oper',
            'unused',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-policy-repository-oper'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper',
            is_config=False,
        ),
    },
    'RoutingPolicy.Sets.ExtendedCommunitySegNh.Inactive' : {
        'meta_info' : _MetaInfoClass('RoutingPolicy.Sets.ExtendedCommunitySegNh.Inactive', REFERENCE_CLASS,
            '''All objects of a given type that are not
attached to a protocol''',
            False, 
            [
            _MetaInfoClassMember('object', REFERENCE_LEAFLIST, 'str', 'String',
                None, None,
                [], [],
                '''                Policy objects
                ''',
                'object',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            ],
            'Cisco-IOS-XR-policy-repository-oper',
            'inactive',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-policy-repository-oper'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper',
            is_config=False,
        ),
    },
    'RoutingPolicy.Sets.ExtendedCommunitySegNh.Active' : {
        'meta_info' : _MetaInfoClass('RoutingPolicy.Sets.ExtendedCommunitySegNh.Active', REFERENCE_CLASS,
            '''All objects of a given type that are attached to
a protocol''',
            False, 
            [
            _MetaInfoClassMember('object', REFERENCE_LEAFLIST, 'str', 'String',
                None, None,
                [], [],
                '''                Policy objects
                ''',
                'object',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            ],
            'Cisco-IOS-XR-policy-repository-oper',
            'active',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-policy-repository-oper'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper',
            is_config=False,
        ),
    },
    'RoutingPolicy.Sets.ExtendedCommunitySegNh' : {
        'meta_info' : _MetaInfoClass('RoutingPolicy.Sets.ExtendedCommunitySegNh', REFERENCE_CLASS,
            '''Information about Extended Community SegNH sets''',
            False, 
            [
            _MetaInfoClassMember('sets', REFERENCE_CLASS, 'Sets_', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper', 'RoutingPolicy.Sets.ExtendedCommunitySegNh.Sets_',
                [], [],
                '''                Information about individual sets
                ''',
                'sets',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('unused', REFERENCE_CLASS, 'Unused', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper', 'RoutingPolicy.Sets.ExtendedCommunitySegNh.Unused',
                [], [],
                '''                All objects of a given type that are not
                referenced at all
                ''',
                'unused',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('inactive', REFERENCE_CLASS, 'Inactive', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper', 'RoutingPolicy.Sets.ExtendedCommunitySegNh.Inactive',
                [], [],
                '''                All objects of a given type that are not
                attached to a protocol
                ''',
                'inactive',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('active', REFERENCE_CLASS, 'Active', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper', 'RoutingPolicy.Sets.ExtendedCommunitySegNh.Active',
                [], [],
                '''                All objects of a given type that are attached to
                a protocol
                ''',
                'active',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            ],
            'Cisco-IOS-XR-policy-repository-oper',
            'extended-community-seg-nh',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-policy-repository-oper'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper',
            is_config=False,
        ),
    },
    'RoutingPolicy.Sets.ExtendedCommunitySoo.Sets_.Set.UsedBy.Reference' : {
        'meta_info' : _MetaInfoClass('RoutingPolicy.Sets.ExtendedCommunitySoo.Sets_.Set.UsedBy.Reference', REFERENCE_LIST,
            '''Information about policies referring to this
object''',
            False, 
            [
            _MetaInfoClassMember('route-policy-name', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                Name of policy
                ''',
                'route_policy_name',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('used-directly', ATTRIBUTE, 'bool', 'boolean',
                None, None,
                [], [],
                '''                Whether the policy uses this object directly or
                indirectly
                ''',
                'used_directly',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('status', REFERENCE_ENUM_CLASS, 'ObjectStatus', 'Object-status',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper', 'ObjectStatus',
                [], [],
                '''                Active, Inactive, or Unused
                ''',
                'status',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            ],
            'Cisco-IOS-XR-policy-repository-oper',
            'reference',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-policy-repository-oper'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper',
            is_config=False,
        ),
    },
    'RoutingPolicy.Sets.ExtendedCommunitySoo.Sets_.Set.UsedBy' : {
        'meta_info' : _MetaInfoClass('RoutingPolicy.Sets.ExtendedCommunitySoo.Sets_.Set.UsedBy', REFERENCE_CLASS,
            '''Policies that use this object, directly or
indirectly''',
            False, 
            [
            _MetaInfoClassMember('reference', REFERENCE_LIST, 'Reference', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper', 'RoutingPolicy.Sets.ExtendedCommunitySoo.Sets_.Set.UsedBy.Reference',
                [], [],
                '''                Information about policies referring to this
                object
                ''',
                'reference',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            ],
            'Cisco-IOS-XR-policy-repository-oper',
            'used-by',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-policy-repository-oper'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper',
            is_config=False,
        ),
    },
    'RoutingPolicy.Sets.ExtendedCommunitySoo.Sets_.Set.Attached.Binding' : {
        'meta_info' : _MetaInfoClass('RoutingPolicy.Sets.ExtendedCommunitySoo.Sets_.Set.Attached.Binding', REFERENCE_LIST,
            '''bindings list''',
            False, 
            [
            _MetaInfoClassMember('protocol', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                Protocol to which policy attached
                ''',
                'protocol',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('vrf-name', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                VRF name
                ''',
                'vrf_name',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('proto-instance', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                Protocol instance
                ''',
                'proto_instance',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('af-name', REFERENCE_ENUM_CLASS, 'AddressFamily', 'Address-family',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper', 'AddressFamily',
                [], [],
                '''                Address Family Identifier
                ''',
                'af_name',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('saf-name', REFERENCE_ENUM_CLASS, 'SubAddressFamily', 'Sub-address-family',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper', 'SubAddressFamily',
                [], [],
                '''                Subsequent Address Family Identifier
                ''',
                'saf_name',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('neighbor-address', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                Neighbor IP Address
                ''',
                'neighbor_address',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('neighbor-af-name', REFERENCE_ENUM_CLASS, 'AddressFamily', 'Address-family',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper', 'AddressFamily',
                [], [],
                '''                Neighbor IP Address Family
                ''',
                'neighbor_af_name',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('group-name', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                Neighbor Group Name
                ''',
                'group_name',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('direction', REFERENCE_ENUM_CLASS, 'AttachPointDirection', 'Attach-point-direction',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper', 'AttachPointDirection',
                [], [],
                '''                Direction In or Out
                ''',
                'direction',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('group', REFERENCE_ENUM_CLASS, 'Group', 'Group',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper', 'Group',
                [], [],
                '''                Neighbor Group 
                ''',
                'group',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('source-protocol', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                Source Protocol to redistribute, Source Protocol
                can be one of the following values{all,
                connected, local, static, bgp, rip, isis, ospf
                ,ospfv3, eigrp, unknown }
                ''',
                'source_protocol',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('aggregate-network-address', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                Aggregate IP address or Network IP Address in
                IPv4 or IPv6 Format
                ''',
                'aggregate_network_address',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('interface-name', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                Interface Name
                ''',
                'interface_name',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('instance', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                Instance
                ''',
                'instance',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('area-id', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                OSPF Area ID in Decimal Integer Format
                ''',
                'area_id',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('propogate-from', ATTRIBUTE, 'int', 'int32',
                None, None,
                [('-2147483648', '2147483647')], [],
                '''                ISIS Propogate From Level
                ''',
                'propogate_from',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('propogate-to', ATTRIBUTE, 'int', 'int32',
                None, None,
                [('-2147483648', '2147483647')], [],
                '''                ISIS Propogate To Level
                ''',
                'propogate_to',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('route-policy-name', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                Policy that uses object in question
                ''',
                'route_policy_name',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('attached-policy', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                The attached policy that (maybe indirectly) uses
                the object in question
                ''',
                'attached_policy',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('attach-point', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                Name of attach point where policy is attached
                ''',
                'attach_point',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            ],
            'Cisco-IOS-XR-policy-repository-oper',
            'binding',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-policy-repository-oper'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper',
            is_config=False,
        ),
    },
    'RoutingPolicy.Sets.ExtendedCommunitySoo.Sets_.Set.Attached' : {
        'meta_info' : _MetaInfoClass('RoutingPolicy.Sets.ExtendedCommunitySoo.Sets_.Set.Attached', REFERENCE_CLASS,
            '''Information about where this policy or set is
attached''',
            False, 
            [
            _MetaInfoClassMember('binding', REFERENCE_LIST, 'Binding', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper', 'RoutingPolicy.Sets.ExtendedCommunitySoo.Sets_.Set.Attached.Binding',
                [], [],
                '''                bindings list
                ''',
                'binding',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            ],
            'Cisco-IOS-XR-policy-repository-oper',
            'attached',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-policy-repository-oper'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper',
            is_config=False,
        ),
    },
    'RoutingPolicy.Sets.ExtendedCommunitySoo.Sets_.Set' : {
        'meta_info' : _MetaInfoClass('RoutingPolicy.Sets.ExtendedCommunitySoo.Sets_.Set', REFERENCE_LIST,
            '''Information about an individual set''',
            False, 
            [
            _MetaInfoClassMember('set-name', ATTRIBUTE, 'str', 'xr:Cisco-ios-xr-string',
                None, None,
                [], [b'[\\w\\-\\.:,_@#%$\\+=\\|;]+'],
                '''                Set name
                ''',
                'set_name',
                'Cisco-IOS-XR-policy-repository-oper', True, is_config=False),
            _MetaInfoClassMember('used-by', REFERENCE_CLASS, 'UsedBy', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper', 'RoutingPolicy.Sets.ExtendedCommunitySoo.Sets_.Set.UsedBy',
                [], [],
                '''                Policies that use this object, directly or
                indirectly
                ''',
                'used_by',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('attached', REFERENCE_CLASS, 'Attached', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper', 'RoutingPolicy.Sets.ExtendedCommunitySoo.Sets_.Set.Attached',
                [], [],
                '''                Information about where this policy or set is
                attached
                ''',
                'attached',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            ],
            'Cisco-IOS-XR-policy-repository-oper',
            'set',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-policy-repository-oper'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper',
            is_config=False,
        ),
    },
    'RoutingPolicy.Sets.ExtendedCommunitySoo.Sets_' : {
        'meta_info' : _MetaInfoClass('RoutingPolicy.Sets.ExtendedCommunitySoo.Sets_', REFERENCE_CLASS,
            '''Information about individual sets''',
            False, 
            [
            _MetaInfoClassMember('set', REFERENCE_LIST, 'Set', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper', 'RoutingPolicy.Sets.ExtendedCommunitySoo.Sets_.Set',
                [], [],
                '''                Information about an individual set
                ''',
                'set',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            ],
            'Cisco-IOS-XR-policy-repository-oper',
            'sets',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-policy-repository-oper'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper',
            is_config=False,
        ),
    },
    'RoutingPolicy.Sets.ExtendedCommunitySoo.Unused' : {
        'meta_info' : _MetaInfoClass('RoutingPolicy.Sets.ExtendedCommunitySoo.Unused', REFERENCE_CLASS,
            '''All objects of a given type that are not
referenced at all''',
            False, 
            [
            _MetaInfoClassMember('object', REFERENCE_LEAFLIST, 'str', 'String',
                None, None,
                [], [],
                '''                Policy objects
                ''',
                'object',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            ],
            'Cisco-IOS-XR-policy-repository-oper',
            'unused',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-policy-repository-oper'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper',
            is_config=False,
        ),
    },
    'RoutingPolicy.Sets.ExtendedCommunitySoo.Inactive' : {
        'meta_info' : _MetaInfoClass('RoutingPolicy.Sets.ExtendedCommunitySoo.Inactive', REFERENCE_CLASS,
            '''All objects of a given type that are not
attached to a protocol''',
            False, 
            [
            _MetaInfoClassMember('object', REFERENCE_LEAFLIST, 'str', 'String',
                None, None,
                [], [],
                '''                Policy objects
                ''',
                'object',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            ],
            'Cisco-IOS-XR-policy-repository-oper',
            'inactive',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-policy-repository-oper'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper',
            is_config=False,
        ),
    },
    'RoutingPolicy.Sets.ExtendedCommunitySoo.Active' : {
        'meta_info' : _MetaInfoClass('RoutingPolicy.Sets.ExtendedCommunitySoo.Active', REFERENCE_CLASS,
            '''All objects of a given type that are attached to
a protocol''',
            False, 
            [
            _MetaInfoClassMember('object', REFERENCE_LEAFLIST, 'str', 'String',
                None, None,
                [], [],
                '''                Policy objects
                ''',
                'object',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            ],
            'Cisco-IOS-XR-policy-repository-oper',
            'active',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-policy-repository-oper'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper',
            is_config=False,
        ),
    },
    'RoutingPolicy.Sets.ExtendedCommunitySoo' : {
        'meta_info' : _MetaInfoClass('RoutingPolicy.Sets.ExtendedCommunitySoo', REFERENCE_CLASS,
            '''Information about Extended Community SOO sets''',
            False, 
            [
            _MetaInfoClassMember('sets', REFERENCE_CLASS, 'Sets_', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper', 'RoutingPolicy.Sets.ExtendedCommunitySoo.Sets_',
                [], [],
                '''                Information about individual sets
                ''',
                'sets',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('unused', REFERENCE_CLASS, 'Unused', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper', 'RoutingPolicy.Sets.ExtendedCommunitySoo.Unused',
                [], [],
                '''                All objects of a given type that are not
                referenced at all
                ''',
                'unused',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('inactive', REFERENCE_CLASS, 'Inactive', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper', 'RoutingPolicy.Sets.ExtendedCommunitySoo.Inactive',
                [], [],
                '''                All objects of a given type that are not
                attached to a protocol
                ''',
                'inactive',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('active', REFERENCE_CLASS, 'Active', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper', 'RoutingPolicy.Sets.ExtendedCommunitySoo.Active',
                [], [],
                '''                All objects of a given type that are attached to
                a protocol
                ''',
                'active',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            ],
            'Cisco-IOS-XR-policy-repository-oper',
            'extended-community-soo',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-policy-repository-oper'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper',
            is_config=False,
        ),
    },
    'RoutingPolicy.Sets.Tag.Sets_.Set.UsedBy.Reference' : {
        'meta_info' : _MetaInfoClass('RoutingPolicy.Sets.Tag.Sets_.Set.UsedBy.Reference', REFERENCE_LIST,
            '''Information about policies referring to this
object''',
            False, 
            [
            _MetaInfoClassMember('route-policy-name', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                Name of policy
                ''',
                'route_policy_name',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('used-directly', ATTRIBUTE, 'bool', 'boolean',
                None, None,
                [], [],
                '''                Whether the policy uses this object directly or
                indirectly
                ''',
                'used_directly',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('status', REFERENCE_ENUM_CLASS, 'ObjectStatus', 'Object-status',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper', 'ObjectStatus',
                [], [],
                '''                Active, Inactive, or Unused
                ''',
                'status',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            ],
            'Cisco-IOS-XR-policy-repository-oper',
            'reference',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-policy-repository-oper'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper',
            is_config=False,
        ),
    },
    'RoutingPolicy.Sets.Tag.Sets_.Set.UsedBy' : {
        'meta_info' : _MetaInfoClass('RoutingPolicy.Sets.Tag.Sets_.Set.UsedBy', REFERENCE_CLASS,
            '''Policies that use this object, directly or
indirectly''',
            False, 
            [
            _MetaInfoClassMember('reference', REFERENCE_LIST, 'Reference', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper', 'RoutingPolicy.Sets.Tag.Sets_.Set.UsedBy.Reference',
                [], [],
                '''                Information about policies referring to this
                object
                ''',
                'reference',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            ],
            'Cisco-IOS-XR-policy-repository-oper',
            'used-by',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-policy-repository-oper'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper',
            is_config=False,
        ),
    },
    'RoutingPolicy.Sets.Tag.Sets_.Set.Attached.Binding' : {
        'meta_info' : _MetaInfoClass('RoutingPolicy.Sets.Tag.Sets_.Set.Attached.Binding', REFERENCE_LIST,
            '''bindings list''',
            False, 
            [
            _MetaInfoClassMember('protocol', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                Protocol to which policy attached
                ''',
                'protocol',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('vrf-name', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                VRF name
                ''',
                'vrf_name',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('proto-instance', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                Protocol instance
                ''',
                'proto_instance',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('af-name', REFERENCE_ENUM_CLASS, 'AddressFamily', 'Address-family',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper', 'AddressFamily',
                [], [],
                '''                Address Family Identifier
                ''',
                'af_name',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('saf-name', REFERENCE_ENUM_CLASS, 'SubAddressFamily', 'Sub-address-family',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper', 'SubAddressFamily',
                [], [],
                '''                Subsequent Address Family Identifier
                ''',
                'saf_name',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('neighbor-address', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                Neighbor IP Address
                ''',
                'neighbor_address',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('neighbor-af-name', REFERENCE_ENUM_CLASS, 'AddressFamily', 'Address-family',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper', 'AddressFamily',
                [], [],
                '''                Neighbor IP Address Family
                ''',
                'neighbor_af_name',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('group-name', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                Neighbor Group Name
                ''',
                'group_name',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('direction', REFERENCE_ENUM_CLASS, 'AttachPointDirection', 'Attach-point-direction',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper', 'AttachPointDirection',
                [], [],
                '''                Direction In or Out
                ''',
                'direction',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('group', REFERENCE_ENUM_CLASS, 'Group', 'Group',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper', 'Group',
                [], [],
                '''                Neighbor Group 
                ''',
                'group',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('source-protocol', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                Source Protocol to redistribute, Source Protocol
                can be one of the following values{all,
                connected, local, static, bgp, rip, isis, ospf
                ,ospfv3, eigrp, unknown }
                ''',
                'source_protocol',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('aggregate-network-address', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                Aggregate IP address or Network IP Address in
                IPv4 or IPv6 Format
                ''',
                'aggregate_network_address',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('interface-name', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                Interface Name
                ''',
                'interface_name',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('instance', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                Instance
                ''',
                'instance',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('area-id', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                OSPF Area ID in Decimal Integer Format
                ''',
                'area_id',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('propogate-from', ATTRIBUTE, 'int', 'int32',
                None, None,
                [('-2147483648', '2147483647')], [],
                '''                ISIS Propogate From Level
                ''',
                'propogate_from',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('propogate-to', ATTRIBUTE, 'int', 'int32',
                None, None,
                [('-2147483648', '2147483647')], [],
                '''                ISIS Propogate To Level
                ''',
                'propogate_to',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('route-policy-name', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                Policy that uses object in question
                ''',
                'route_policy_name',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('attached-policy', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                The attached policy that (maybe indirectly) uses
                the object in question
                ''',
                'attached_policy',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('attach-point', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                Name of attach point where policy is attached
                ''',
                'attach_point',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            ],
            'Cisco-IOS-XR-policy-repository-oper',
            'binding',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-policy-repository-oper'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper',
            is_config=False,
        ),
    },
    'RoutingPolicy.Sets.Tag.Sets_.Set.Attached' : {
        'meta_info' : _MetaInfoClass('RoutingPolicy.Sets.Tag.Sets_.Set.Attached', REFERENCE_CLASS,
            '''Information about where this policy or set is
attached''',
            False, 
            [
            _MetaInfoClassMember('binding', REFERENCE_LIST, 'Binding', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper', 'RoutingPolicy.Sets.Tag.Sets_.Set.Attached.Binding',
                [], [],
                '''                bindings list
                ''',
                'binding',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            ],
            'Cisco-IOS-XR-policy-repository-oper',
            'attached',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-policy-repository-oper'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper',
            is_config=False,
        ),
    },
    'RoutingPolicy.Sets.Tag.Sets_.Set' : {
        'meta_info' : _MetaInfoClass('RoutingPolicy.Sets.Tag.Sets_.Set', REFERENCE_LIST,
            '''Information about an individual set''',
            False, 
            [
            _MetaInfoClassMember('set-name', ATTRIBUTE, 'str', 'xr:Cisco-ios-xr-string',
                None, None,
                [], [b'[\\w\\-\\.:,_@#%$\\+=\\|;]+'],
                '''                Set name
                ''',
                'set_name',
                'Cisco-IOS-XR-policy-repository-oper', True, is_config=False),
            _MetaInfoClassMember('used-by', REFERENCE_CLASS, 'UsedBy', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper', 'RoutingPolicy.Sets.Tag.Sets_.Set.UsedBy',
                [], [],
                '''                Policies that use this object, directly or
                indirectly
                ''',
                'used_by',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('attached', REFERENCE_CLASS, 'Attached', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper', 'RoutingPolicy.Sets.Tag.Sets_.Set.Attached',
                [], [],
                '''                Information about where this policy or set is
                attached
                ''',
                'attached',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            ],
            'Cisco-IOS-XR-policy-repository-oper',
            'set',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-policy-repository-oper'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper',
            is_config=False,
        ),
    },
    'RoutingPolicy.Sets.Tag.Sets_' : {
        'meta_info' : _MetaInfoClass('RoutingPolicy.Sets.Tag.Sets_', REFERENCE_CLASS,
            '''Information about individual sets''',
            False, 
            [
            _MetaInfoClassMember('set', REFERENCE_LIST, 'Set', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper', 'RoutingPolicy.Sets.Tag.Sets_.Set',
                [], [],
                '''                Information about an individual set
                ''',
                'set',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            ],
            'Cisco-IOS-XR-policy-repository-oper',
            'sets',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-policy-repository-oper'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper',
            is_config=False,
        ),
    },
    'RoutingPolicy.Sets.Tag.Unused' : {
        'meta_info' : _MetaInfoClass('RoutingPolicy.Sets.Tag.Unused', REFERENCE_CLASS,
            '''All objects of a given type that are not
referenced at all''',
            False, 
            [
            _MetaInfoClassMember('object', REFERENCE_LEAFLIST, 'str', 'String',
                None, None,
                [], [],
                '''                Policy objects
                ''',
                'object',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            ],
            'Cisco-IOS-XR-policy-repository-oper',
            'unused',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-policy-repository-oper'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper',
            is_config=False,
        ),
    },
    'RoutingPolicy.Sets.Tag.Inactive' : {
        'meta_info' : _MetaInfoClass('RoutingPolicy.Sets.Tag.Inactive', REFERENCE_CLASS,
            '''All objects of a given type that are not
attached to a protocol''',
            False, 
            [
            _MetaInfoClassMember('object', REFERENCE_LEAFLIST, 'str', 'String',
                None, None,
                [], [],
                '''                Policy objects
                ''',
                'object',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            ],
            'Cisco-IOS-XR-policy-repository-oper',
            'inactive',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-policy-repository-oper'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper',
            is_config=False,
        ),
    },
    'RoutingPolicy.Sets.Tag.Active' : {
        'meta_info' : _MetaInfoClass('RoutingPolicy.Sets.Tag.Active', REFERENCE_CLASS,
            '''All objects of a given type that are attached to
a protocol''',
            False, 
            [
            _MetaInfoClassMember('object', REFERENCE_LEAFLIST, 'str', 'String',
                None, None,
                [], [],
                '''                Policy objects
                ''',
                'object',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            ],
            'Cisco-IOS-XR-policy-repository-oper',
            'active',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-policy-repository-oper'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper',
            is_config=False,
        ),
    },
    'RoutingPolicy.Sets.Tag' : {
        'meta_info' : _MetaInfoClass('RoutingPolicy.Sets.Tag', REFERENCE_CLASS,
            '''Information about Tag sets''',
            False, 
            [
            _MetaInfoClassMember('sets', REFERENCE_CLASS, 'Sets_', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper', 'RoutingPolicy.Sets.Tag.Sets_',
                [], [],
                '''                Information about individual sets
                ''',
                'sets',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('unused', REFERENCE_CLASS, 'Unused', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper', 'RoutingPolicy.Sets.Tag.Unused',
                [], [],
                '''                All objects of a given type that are not
                referenced at all
                ''',
                'unused',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('inactive', REFERENCE_CLASS, 'Inactive', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper', 'RoutingPolicy.Sets.Tag.Inactive',
                [], [],
                '''                All objects of a given type that are not
                attached to a protocol
                ''',
                'inactive',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('active', REFERENCE_CLASS, 'Active', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper', 'RoutingPolicy.Sets.Tag.Active',
                [], [],
                '''                All objects of a given type that are attached to
                a protocol
                ''',
                'active',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            ],
            'Cisco-IOS-XR-policy-repository-oper',
            'tag',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-policy-repository-oper'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper',
            is_config=False,
        ),
    },
    'RoutingPolicy.Sets.Prefix.Sets_.Set.UsedBy.Reference' : {
        'meta_info' : _MetaInfoClass('RoutingPolicy.Sets.Prefix.Sets_.Set.UsedBy.Reference', REFERENCE_LIST,
            '''Information about policies referring to this
object''',
            False, 
            [
            _MetaInfoClassMember('route-policy-name', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                Name of policy
                ''',
                'route_policy_name',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('used-directly', ATTRIBUTE, 'bool', 'boolean',
                None, None,
                [], [],
                '''                Whether the policy uses this object directly or
                indirectly
                ''',
                'used_directly',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('status', REFERENCE_ENUM_CLASS, 'ObjectStatus', 'Object-status',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper', 'ObjectStatus',
                [], [],
                '''                Active, Inactive, or Unused
                ''',
                'status',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            ],
            'Cisco-IOS-XR-policy-repository-oper',
            'reference',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-policy-repository-oper'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper',
            is_config=False,
        ),
    },
    'RoutingPolicy.Sets.Prefix.Sets_.Set.UsedBy' : {
        'meta_info' : _MetaInfoClass('RoutingPolicy.Sets.Prefix.Sets_.Set.UsedBy', REFERENCE_CLASS,
            '''Policies that use this object, directly or
indirectly''',
            False, 
            [
            _MetaInfoClassMember('reference', REFERENCE_LIST, 'Reference', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper', 'RoutingPolicy.Sets.Prefix.Sets_.Set.UsedBy.Reference',
                [], [],
                '''                Information about policies referring to this
                object
                ''',
                'reference',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            ],
            'Cisco-IOS-XR-policy-repository-oper',
            'used-by',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-policy-repository-oper'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper',
            is_config=False,
        ),
    },
    'RoutingPolicy.Sets.Prefix.Sets_.Set.Attached.Binding' : {
        'meta_info' : _MetaInfoClass('RoutingPolicy.Sets.Prefix.Sets_.Set.Attached.Binding', REFERENCE_LIST,
            '''bindings list''',
            False, 
            [
            _MetaInfoClassMember('protocol', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                Protocol to which policy attached
                ''',
                'protocol',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('vrf-name', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                VRF name
                ''',
                'vrf_name',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('proto-instance', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                Protocol instance
                ''',
                'proto_instance',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('af-name', REFERENCE_ENUM_CLASS, 'AddressFamily', 'Address-family',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper', 'AddressFamily',
                [], [],
                '''                Address Family Identifier
                ''',
                'af_name',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('saf-name', REFERENCE_ENUM_CLASS, 'SubAddressFamily', 'Sub-address-family',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper', 'SubAddressFamily',
                [], [],
                '''                Subsequent Address Family Identifier
                ''',
                'saf_name',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('neighbor-address', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                Neighbor IP Address
                ''',
                'neighbor_address',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('neighbor-af-name', REFERENCE_ENUM_CLASS, 'AddressFamily', 'Address-family',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper', 'AddressFamily',
                [], [],
                '''                Neighbor IP Address Family
                ''',
                'neighbor_af_name',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('group-name', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                Neighbor Group Name
                ''',
                'group_name',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('direction', REFERENCE_ENUM_CLASS, 'AttachPointDirection', 'Attach-point-direction',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper', 'AttachPointDirection',
                [], [],
                '''                Direction In or Out
                ''',
                'direction',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('group', REFERENCE_ENUM_CLASS, 'Group', 'Group',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper', 'Group',
                [], [],
                '''                Neighbor Group 
                ''',
                'group',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('source-protocol', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                Source Protocol to redistribute, Source Protocol
                can be one of the following values{all,
                connected, local, static, bgp, rip, isis, ospf
                ,ospfv3, eigrp, unknown }
                ''',
                'source_protocol',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('aggregate-network-address', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                Aggregate IP address or Network IP Address in
                IPv4 or IPv6 Format
                ''',
                'aggregate_network_address',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('interface-name', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                Interface Name
                ''',
                'interface_name',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('instance', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                Instance
                ''',
                'instance',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('area-id', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                OSPF Area ID in Decimal Integer Format
                ''',
                'area_id',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('propogate-from', ATTRIBUTE, 'int', 'int32',
                None, None,
                [('-2147483648', '2147483647')], [],
                '''                ISIS Propogate From Level
                ''',
                'propogate_from',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('propogate-to', ATTRIBUTE, 'int', 'int32',
                None, None,
                [('-2147483648', '2147483647')], [],
                '''                ISIS Propogate To Level
                ''',
                'propogate_to',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('route-policy-name', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                Policy that uses object in question
                ''',
                'route_policy_name',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('attached-policy', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                The attached policy that (maybe indirectly) uses
                the object in question
                ''',
                'attached_policy',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('attach-point', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                Name of attach point where policy is attached
                ''',
                'attach_point',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            ],
            'Cisco-IOS-XR-policy-repository-oper',
            'binding',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-policy-repository-oper'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper',
            is_config=False,
        ),
    },
    'RoutingPolicy.Sets.Prefix.Sets_.Set.Attached' : {
        'meta_info' : _MetaInfoClass('RoutingPolicy.Sets.Prefix.Sets_.Set.Attached', REFERENCE_CLASS,
            '''Information about where this policy or set is
attached''',
            False, 
            [
            _MetaInfoClassMember('binding', REFERENCE_LIST, 'Binding', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper', 'RoutingPolicy.Sets.Prefix.Sets_.Set.Attached.Binding',
                [], [],
                '''                bindings list
                ''',
                'binding',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            ],
            'Cisco-IOS-XR-policy-repository-oper',
            'attached',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-policy-repository-oper'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper',
            is_config=False,
        ),
    },
    'RoutingPolicy.Sets.Prefix.Sets_.Set' : {
        'meta_info' : _MetaInfoClass('RoutingPolicy.Sets.Prefix.Sets_.Set', REFERENCE_LIST,
            '''Information about an individual set''',
            False, 
            [
            _MetaInfoClassMember('set-name', ATTRIBUTE, 'str', 'xr:Cisco-ios-xr-string',
                None, None,
                [], [b'[\\w\\-\\.:,_@#%$\\+=\\|;]+'],
                '''                Set name
                ''',
                'set_name',
                'Cisco-IOS-XR-policy-repository-oper', True, is_config=False),
            _MetaInfoClassMember('used-by', REFERENCE_CLASS, 'UsedBy', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper', 'RoutingPolicy.Sets.Prefix.Sets_.Set.UsedBy',
                [], [],
                '''                Policies that use this object, directly or
                indirectly
                ''',
                'used_by',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('attached', REFERENCE_CLASS, 'Attached', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper', 'RoutingPolicy.Sets.Prefix.Sets_.Set.Attached',
                [], [],
                '''                Information about where this policy or set is
                attached
                ''',
                'attached',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            ],
            'Cisco-IOS-XR-policy-repository-oper',
            'set',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-policy-repository-oper'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper',
            is_config=False,
        ),
    },
    'RoutingPolicy.Sets.Prefix.Sets_' : {
        'meta_info' : _MetaInfoClass('RoutingPolicy.Sets.Prefix.Sets_', REFERENCE_CLASS,
            '''Information about individual sets''',
            False, 
            [
            _MetaInfoClassMember('set', REFERENCE_LIST, 'Set', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper', 'RoutingPolicy.Sets.Prefix.Sets_.Set',
                [], [],
                '''                Information about an individual set
                ''',
                'set',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            ],
            'Cisco-IOS-XR-policy-repository-oper',
            'sets',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-policy-repository-oper'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper',
            is_config=False,
        ),
    },
    'RoutingPolicy.Sets.Prefix.Unused' : {
        'meta_info' : _MetaInfoClass('RoutingPolicy.Sets.Prefix.Unused', REFERENCE_CLASS,
            '''All objects of a given type that are not
referenced at all''',
            False, 
            [
            _MetaInfoClassMember('object', REFERENCE_LEAFLIST, 'str', 'String',
                None, None,
                [], [],
                '''                Policy objects
                ''',
                'object',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            ],
            'Cisco-IOS-XR-policy-repository-oper',
            'unused',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-policy-repository-oper'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper',
            is_config=False,
        ),
    },
    'RoutingPolicy.Sets.Prefix.Inactive' : {
        'meta_info' : _MetaInfoClass('RoutingPolicy.Sets.Prefix.Inactive', REFERENCE_CLASS,
            '''All objects of a given type that are not
attached to a protocol''',
            False, 
            [
            _MetaInfoClassMember('object', REFERENCE_LEAFLIST, 'str', 'String',
                None, None,
                [], [],
                '''                Policy objects
                ''',
                'object',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            ],
            'Cisco-IOS-XR-policy-repository-oper',
            'inactive',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-policy-repository-oper'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper',
            is_config=False,
        ),
    },
    'RoutingPolicy.Sets.Prefix.Active' : {
        'meta_info' : _MetaInfoClass('RoutingPolicy.Sets.Prefix.Active', REFERENCE_CLASS,
            '''All objects of a given type that are attached to
a protocol''',
            False, 
            [
            _MetaInfoClassMember('object', REFERENCE_LEAFLIST, 'str', 'String',
                None, None,
                [], [],
                '''                Policy objects
                ''',
                'object',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            ],
            'Cisco-IOS-XR-policy-repository-oper',
            'active',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-policy-repository-oper'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper',
            is_config=False,
        ),
    },
    'RoutingPolicy.Sets.Prefix' : {
        'meta_info' : _MetaInfoClass('RoutingPolicy.Sets.Prefix', REFERENCE_CLASS,
            '''Information about AS Path sets''',
            False, 
            [
            _MetaInfoClassMember('sets', REFERENCE_CLASS, 'Sets_', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper', 'RoutingPolicy.Sets.Prefix.Sets_',
                [], [],
                '''                Information about individual sets
                ''',
                'sets',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('unused', REFERENCE_CLASS, 'Unused', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper', 'RoutingPolicy.Sets.Prefix.Unused',
                [], [],
                '''                All objects of a given type that are not
                referenced at all
                ''',
                'unused',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('inactive', REFERENCE_CLASS, 'Inactive', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper', 'RoutingPolicy.Sets.Prefix.Inactive',
                [], [],
                '''                All objects of a given type that are not
                attached to a protocol
                ''',
                'inactive',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('active', REFERENCE_CLASS, 'Active', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper', 'RoutingPolicy.Sets.Prefix.Active',
                [], [],
                '''                All objects of a given type that are attached to
                a protocol
                ''',
                'active',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            ],
            'Cisco-IOS-XR-policy-repository-oper',
            'prefix',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-policy-repository-oper'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper',
            is_config=False,
        ),
    },
    'RoutingPolicy.Sets.Community.Sets_.Set.UsedBy.Reference' : {
        'meta_info' : _MetaInfoClass('RoutingPolicy.Sets.Community.Sets_.Set.UsedBy.Reference', REFERENCE_LIST,
            '''Information about policies referring to this
object''',
            False, 
            [
            _MetaInfoClassMember('route-policy-name', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                Name of policy
                ''',
                'route_policy_name',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('used-directly', ATTRIBUTE, 'bool', 'boolean',
                None, None,
                [], [],
                '''                Whether the policy uses this object directly or
                indirectly
                ''',
                'used_directly',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('status', REFERENCE_ENUM_CLASS, 'ObjectStatus', 'Object-status',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper', 'ObjectStatus',
                [], [],
                '''                Active, Inactive, or Unused
                ''',
                'status',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            ],
            'Cisco-IOS-XR-policy-repository-oper',
            'reference',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-policy-repository-oper'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper',
            is_config=False,
        ),
    },
    'RoutingPolicy.Sets.Community.Sets_.Set.UsedBy' : {
        'meta_info' : _MetaInfoClass('RoutingPolicy.Sets.Community.Sets_.Set.UsedBy', REFERENCE_CLASS,
            '''Policies that use this object, directly or
indirectly''',
            False, 
            [
            _MetaInfoClassMember('reference', REFERENCE_LIST, 'Reference', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper', 'RoutingPolicy.Sets.Community.Sets_.Set.UsedBy.Reference',
                [], [],
                '''                Information about policies referring to this
                object
                ''',
                'reference',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            ],
            'Cisco-IOS-XR-policy-repository-oper',
            'used-by',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-policy-repository-oper'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper',
            is_config=False,
        ),
    },
    'RoutingPolicy.Sets.Community.Sets_.Set.Attached.Binding' : {
        'meta_info' : _MetaInfoClass('RoutingPolicy.Sets.Community.Sets_.Set.Attached.Binding', REFERENCE_LIST,
            '''bindings list''',
            False, 
            [
            _MetaInfoClassMember('protocol', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                Protocol to which policy attached
                ''',
                'protocol',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('vrf-name', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                VRF name
                ''',
                'vrf_name',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('proto-instance', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                Protocol instance
                ''',
                'proto_instance',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('af-name', REFERENCE_ENUM_CLASS, 'AddressFamily', 'Address-family',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper', 'AddressFamily',
                [], [],
                '''                Address Family Identifier
                ''',
                'af_name',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('saf-name', REFERENCE_ENUM_CLASS, 'SubAddressFamily', 'Sub-address-family',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper', 'SubAddressFamily',
                [], [],
                '''                Subsequent Address Family Identifier
                ''',
                'saf_name',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('neighbor-address', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                Neighbor IP Address
                ''',
                'neighbor_address',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('neighbor-af-name', REFERENCE_ENUM_CLASS, 'AddressFamily', 'Address-family',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper', 'AddressFamily',
                [], [],
                '''                Neighbor IP Address Family
                ''',
                'neighbor_af_name',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('group-name', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                Neighbor Group Name
                ''',
                'group_name',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('direction', REFERENCE_ENUM_CLASS, 'AttachPointDirection', 'Attach-point-direction',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper', 'AttachPointDirection',
                [], [],
                '''                Direction In or Out
                ''',
                'direction',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('group', REFERENCE_ENUM_CLASS, 'Group', 'Group',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper', 'Group',
                [], [],
                '''                Neighbor Group 
                ''',
                'group',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('source-protocol', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                Source Protocol to redistribute, Source Protocol
                can be one of the following values{all,
                connected, local, static, bgp, rip, isis, ospf
                ,ospfv3, eigrp, unknown }
                ''',
                'source_protocol',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('aggregate-network-address', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                Aggregate IP address or Network IP Address in
                IPv4 or IPv6 Format
                ''',
                'aggregate_network_address',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('interface-name', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                Interface Name
                ''',
                'interface_name',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('instance', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                Instance
                ''',
                'instance',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('area-id', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                OSPF Area ID in Decimal Integer Format
                ''',
                'area_id',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('propogate-from', ATTRIBUTE, 'int', 'int32',
                None, None,
                [('-2147483648', '2147483647')], [],
                '''                ISIS Propogate From Level
                ''',
                'propogate_from',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('propogate-to', ATTRIBUTE, 'int', 'int32',
                None, None,
                [('-2147483648', '2147483647')], [],
                '''                ISIS Propogate To Level
                ''',
                'propogate_to',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('route-policy-name', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                Policy that uses object in question
                ''',
                'route_policy_name',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('attached-policy', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                The attached policy that (maybe indirectly) uses
                the object in question
                ''',
                'attached_policy',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('attach-point', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                Name of attach point where policy is attached
                ''',
                'attach_point',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            ],
            'Cisco-IOS-XR-policy-repository-oper',
            'binding',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-policy-repository-oper'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper',
            is_config=False,
        ),
    },
    'RoutingPolicy.Sets.Community.Sets_.Set.Attached' : {
        'meta_info' : _MetaInfoClass('RoutingPolicy.Sets.Community.Sets_.Set.Attached', REFERENCE_CLASS,
            '''Information about where this policy or set is
attached''',
            False, 
            [
            _MetaInfoClassMember('binding', REFERENCE_LIST, 'Binding', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper', 'RoutingPolicy.Sets.Community.Sets_.Set.Attached.Binding',
                [], [],
                '''                bindings list
                ''',
                'binding',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            ],
            'Cisco-IOS-XR-policy-repository-oper',
            'attached',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-policy-repository-oper'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper',
            is_config=False,
        ),
    },
    'RoutingPolicy.Sets.Community.Sets_.Set' : {
        'meta_info' : _MetaInfoClass('RoutingPolicy.Sets.Community.Sets_.Set', REFERENCE_LIST,
            '''Information about an individual set''',
            False, 
            [
            _MetaInfoClassMember('set-name', ATTRIBUTE, 'str', 'xr:Cisco-ios-xr-string',
                None, None,
                [], [b'[\\w\\-\\.:,_@#%$\\+=\\|;]+'],
                '''                Set name
                ''',
                'set_name',
                'Cisco-IOS-XR-policy-repository-oper', True, is_config=False),
            _MetaInfoClassMember('used-by', REFERENCE_CLASS, 'UsedBy', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper', 'RoutingPolicy.Sets.Community.Sets_.Set.UsedBy',
                [], [],
                '''                Policies that use this object, directly or
                indirectly
                ''',
                'used_by',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('attached', REFERENCE_CLASS, 'Attached', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper', 'RoutingPolicy.Sets.Community.Sets_.Set.Attached',
                [], [],
                '''                Information about where this policy or set is
                attached
                ''',
                'attached',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            ],
            'Cisco-IOS-XR-policy-repository-oper',
            'set',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-policy-repository-oper'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper',
            is_config=False,
        ),
    },
    'RoutingPolicy.Sets.Community.Sets_' : {
        'meta_info' : _MetaInfoClass('RoutingPolicy.Sets.Community.Sets_', REFERENCE_CLASS,
            '''Information about individual sets''',
            False, 
            [
            _MetaInfoClassMember('set', REFERENCE_LIST, 'Set', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper', 'RoutingPolicy.Sets.Community.Sets_.Set',
                [], [],
                '''                Information about an individual set
                ''',
                'set',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            ],
            'Cisco-IOS-XR-policy-repository-oper',
            'sets',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-policy-repository-oper'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper',
            is_config=False,
        ),
    },
    'RoutingPolicy.Sets.Community.Unused' : {
        'meta_info' : _MetaInfoClass('RoutingPolicy.Sets.Community.Unused', REFERENCE_CLASS,
            '''All objects of a given type that are not
referenced at all''',
            False, 
            [
            _MetaInfoClassMember('object', REFERENCE_LEAFLIST, 'str', 'String',
                None, None,
                [], [],
                '''                Policy objects
                ''',
                'object',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            ],
            'Cisco-IOS-XR-policy-repository-oper',
            'unused',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-policy-repository-oper'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper',
            is_config=False,
        ),
    },
    'RoutingPolicy.Sets.Community.Inactive' : {
        'meta_info' : _MetaInfoClass('RoutingPolicy.Sets.Community.Inactive', REFERENCE_CLASS,
            '''All objects of a given type that are not
attached to a protocol''',
            False, 
            [
            _MetaInfoClassMember('object', REFERENCE_LEAFLIST, 'str', 'String',
                None, None,
                [], [],
                '''                Policy objects
                ''',
                'object',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            ],
            'Cisco-IOS-XR-policy-repository-oper',
            'inactive',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-policy-repository-oper'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper',
            is_config=False,
        ),
    },
    'RoutingPolicy.Sets.Community.Active' : {
        'meta_info' : _MetaInfoClass('RoutingPolicy.Sets.Community.Active', REFERENCE_CLASS,
            '''All objects of a given type that are attached to
a protocol''',
            False, 
            [
            _MetaInfoClassMember('object', REFERENCE_LEAFLIST, 'str', 'String',
                None, None,
                [], [],
                '''                Policy objects
                ''',
                'object',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            ],
            'Cisco-IOS-XR-policy-repository-oper',
            'active',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-policy-repository-oper'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper',
            is_config=False,
        ),
    },
    'RoutingPolicy.Sets.Community' : {
        'meta_info' : _MetaInfoClass('RoutingPolicy.Sets.Community', REFERENCE_CLASS,
            '''Information about Community sets''',
            False, 
            [
            _MetaInfoClassMember('sets', REFERENCE_CLASS, 'Sets_', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper', 'RoutingPolicy.Sets.Community.Sets_',
                [], [],
                '''                Information about individual sets
                ''',
                'sets',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('unused', REFERENCE_CLASS, 'Unused', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper', 'RoutingPolicy.Sets.Community.Unused',
                [], [],
                '''                All objects of a given type that are not
                referenced at all
                ''',
                'unused',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('inactive', REFERENCE_CLASS, 'Inactive', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper', 'RoutingPolicy.Sets.Community.Inactive',
                [], [],
                '''                All objects of a given type that are not
                attached to a protocol
                ''',
                'inactive',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('active', REFERENCE_CLASS, 'Active', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper', 'RoutingPolicy.Sets.Community.Active',
                [], [],
                '''                All objects of a given type that are attached to
                a protocol
                ''',
                'active',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            ],
            'Cisco-IOS-XR-policy-repository-oper',
            'community',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-policy-repository-oper'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper',
            is_config=False,
        ),
    },
    'RoutingPolicy.Sets.AsPath.Sets_.Set.UsedBy.Reference' : {
        'meta_info' : _MetaInfoClass('RoutingPolicy.Sets.AsPath.Sets_.Set.UsedBy.Reference', REFERENCE_LIST,
            '''Information about policies referring to this
object''',
            False, 
            [
            _MetaInfoClassMember('route-policy-name', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                Name of policy
                ''',
                'route_policy_name',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('used-directly', ATTRIBUTE, 'bool', 'boolean',
                None, None,
                [], [],
                '''                Whether the policy uses this object directly or
                indirectly
                ''',
                'used_directly',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('status', REFERENCE_ENUM_CLASS, 'ObjectStatus', 'Object-status',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper', 'ObjectStatus',
                [], [],
                '''                Active, Inactive, or Unused
                ''',
                'status',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            ],
            'Cisco-IOS-XR-policy-repository-oper',
            'reference',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-policy-repository-oper'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper',
            is_config=False,
        ),
    },
    'RoutingPolicy.Sets.AsPath.Sets_.Set.UsedBy' : {
        'meta_info' : _MetaInfoClass('RoutingPolicy.Sets.AsPath.Sets_.Set.UsedBy', REFERENCE_CLASS,
            '''Policies that use this object, directly or
indirectly''',
            False, 
            [
            _MetaInfoClassMember('reference', REFERENCE_LIST, 'Reference', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper', 'RoutingPolicy.Sets.AsPath.Sets_.Set.UsedBy.Reference',
                [], [],
                '''                Information about policies referring to this
                object
                ''',
                'reference',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            ],
            'Cisco-IOS-XR-policy-repository-oper',
            'used-by',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-policy-repository-oper'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper',
            is_config=False,
        ),
    },
    'RoutingPolicy.Sets.AsPath.Sets_.Set.Attached.Binding' : {
        'meta_info' : _MetaInfoClass('RoutingPolicy.Sets.AsPath.Sets_.Set.Attached.Binding', REFERENCE_LIST,
            '''bindings list''',
            False, 
            [
            _MetaInfoClassMember('protocol', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                Protocol to which policy attached
                ''',
                'protocol',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('vrf-name', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                VRF name
                ''',
                'vrf_name',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('proto-instance', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                Protocol instance
                ''',
                'proto_instance',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('af-name', REFERENCE_ENUM_CLASS, 'AddressFamily', 'Address-family',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper', 'AddressFamily',
                [], [],
                '''                Address Family Identifier
                ''',
                'af_name',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('saf-name', REFERENCE_ENUM_CLASS, 'SubAddressFamily', 'Sub-address-family',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper', 'SubAddressFamily',
                [], [],
                '''                Subsequent Address Family Identifier
                ''',
                'saf_name',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('neighbor-address', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                Neighbor IP Address
                ''',
                'neighbor_address',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('neighbor-af-name', REFERENCE_ENUM_CLASS, 'AddressFamily', 'Address-family',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper', 'AddressFamily',
                [], [],
                '''                Neighbor IP Address Family
                ''',
                'neighbor_af_name',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('group-name', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                Neighbor Group Name
                ''',
                'group_name',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('direction', REFERENCE_ENUM_CLASS, 'AttachPointDirection', 'Attach-point-direction',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper', 'AttachPointDirection',
                [], [],
                '''                Direction In or Out
                ''',
                'direction',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('group', REFERENCE_ENUM_CLASS, 'Group', 'Group',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper', 'Group',
                [], [],
                '''                Neighbor Group 
                ''',
                'group',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('source-protocol', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                Source Protocol to redistribute, Source Protocol
                can be one of the following values{all,
                connected, local, static, bgp, rip, isis, ospf
                ,ospfv3, eigrp, unknown }
                ''',
                'source_protocol',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('aggregate-network-address', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                Aggregate IP address or Network IP Address in
                IPv4 or IPv6 Format
                ''',
                'aggregate_network_address',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('interface-name', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                Interface Name
                ''',
                'interface_name',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('instance', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                Instance
                ''',
                'instance',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('area-id', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                OSPF Area ID in Decimal Integer Format
                ''',
                'area_id',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('propogate-from', ATTRIBUTE, 'int', 'int32',
                None, None,
                [('-2147483648', '2147483647')], [],
                '''                ISIS Propogate From Level
                ''',
                'propogate_from',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('propogate-to', ATTRIBUTE, 'int', 'int32',
                None, None,
                [('-2147483648', '2147483647')], [],
                '''                ISIS Propogate To Level
                ''',
                'propogate_to',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('route-policy-name', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                Policy that uses object in question
                ''',
                'route_policy_name',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('attached-policy', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                The attached policy that (maybe indirectly) uses
                the object in question
                ''',
                'attached_policy',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('attach-point', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                Name of attach point where policy is attached
                ''',
                'attach_point',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            ],
            'Cisco-IOS-XR-policy-repository-oper',
            'binding',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-policy-repository-oper'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper',
            is_config=False,
        ),
    },
    'RoutingPolicy.Sets.AsPath.Sets_.Set.Attached' : {
        'meta_info' : _MetaInfoClass('RoutingPolicy.Sets.AsPath.Sets_.Set.Attached', REFERENCE_CLASS,
            '''Information about where this policy or set is
attached''',
            False, 
            [
            _MetaInfoClassMember('binding', REFERENCE_LIST, 'Binding', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper', 'RoutingPolicy.Sets.AsPath.Sets_.Set.Attached.Binding',
                [], [],
                '''                bindings list
                ''',
                'binding',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            ],
            'Cisco-IOS-XR-policy-repository-oper',
            'attached',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-policy-repository-oper'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper',
            is_config=False,
        ),
    },
    'RoutingPolicy.Sets.AsPath.Sets_.Set' : {
        'meta_info' : _MetaInfoClass('RoutingPolicy.Sets.AsPath.Sets_.Set', REFERENCE_LIST,
            '''Information about an individual set''',
            False, 
            [
            _MetaInfoClassMember('set-name', ATTRIBUTE, 'str', 'xr:Cisco-ios-xr-string',
                None, None,
                [], [b'[\\w\\-\\.:,_@#%$\\+=\\|;]+'],
                '''                Set name
                ''',
                'set_name',
                'Cisco-IOS-XR-policy-repository-oper', True, is_config=False),
            _MetaInfoClassMember('used-by', REFERENCE_CLASS, 'UsedBy', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper', 'RoutingPolicy.Sets.AsPath.Sets_.Set.UsedBy',
                [], [],
                '''                Policies that use this object, directly or
                indirectly
                ''',
                'used_by',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('attached', REFERENCE_CLASS, 'Attached', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper', 'RoutingPolicy.Sets.AsPath.Sets_.Set.Attached',
                [], [],
                '''                Information about where this policy or set is
                attached
                ''',
                'attached',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            ],
            'Cisco-IOS-XR-policy-repository-oper',
            'set',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-policy-repository-oper'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper',
            is_config=False,
        ),
    },
    'RoutingPolicy.Sets.AsPath.Sets_' : {
        'meta_info' : _MetaInfoClass('RoutingPolicy.Sets.AsPath.Sets_', REFERENCE_CLASS,
            '''Information about individual sets''',
            False, 
            [
            _MetaInfoClassMember('set', REFERENCE_LIST, 'Set', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper', 'RoutingPolicy.Sets.AsPath.Sets_.Set',
                [], [],
                '''                Information about an individual set
                ''',
                'set',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            ],
            'Cisco-IOS-XR-policy-repository-oper',
            'sets',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-policy-repository-oper'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper',
            is_config=False,
        ),
    },
    'RoutingPolicy.Sets.AsPath.Unused' : {
        'meta_info' : _MetaInfoClass('RoutingPolicy.Sets.AsPath.Unused', REFERENCE_CLASS,
            '''All objects of a given type that are not
referenced at all''',
            False, 
            [
            _MetaInfoClassMember('object', REFERENCE_LEAFLIST, 'str', 'String',
                None, None,
                [], [],
                '''                Policy objects
                ''',
                'object',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            ],
            'Cisco-IOS-XR-policy-repository-oper',
            'unused',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-policy-repository-oper'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper',
            is_config=False,
        ),
    },
    'RoutingPolicy.Sets.AsPath.Inactive' : {
        'meta_info' : _MetaInfoClass('RoutingPolicy.Sets.AsPath.Inactive', REFERENCE_CLASS,
            '''All objects of a given type that are not
attached to a protocol''',
            False, 
            [
            _MetaInfoClassMember('object', REFERENCE_LEAFLIST, 'str', 'String',
                None, None,
                [], [],
                '''                Policy objects
                ''',
                'object',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            ],
            'Cisco-IOS-XR-policy-repository-oper',
            'inactive',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-policy-repository-oper'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper',
            is_config=False,
        ),
    },
    'RoutingPolicy.Sets.AsPath.Active' : {
        'meta_info' : _MetaInfoClass('RoutingPolicy.Sets.AsPath.Active', REFERENCE_CLASS,
            '''All objects of a given type that are attached to
a protocol''',
            False, 
            [
            _MetaInfoClassMember('object', REFERENCE_LEAFLIST, 'str', 'String',
                None, None,
                [], [],
                '''                Policy objects
                ''',
                'object',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            ],
            'Cisco-IOS-XR-policy-repository-oper',
            'active',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-policy-repository-oper'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper',
            is_config=False,
        ),
    },
    'RoutingPolicy.Sets.AsPath' : {
        'meta_info' : _MetaInfoClass('RoutingPolicy.Sets.AsPath', REFERENCE_CLASS,
            '''Information about AS Path sets''',
            False, 
            [
            _MetaInfoClassMember('sets', REFERENCE_CLASS, 'Sets_', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper', 'RoutingPolicy.Sets.AsPath.Sets_',
                [], [],
                '''                Information about individual sets
                ''',
                'sets',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('unused', REFERENCE_CLASS, 'Unused', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper', 'RoutingPolicy.Sets.AsPath.Unused',
                [], [],
                '''                All objects of a given type that are not
                referenced at all
                ''',
                'unused',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('inactive', REFERENCE_CLASS, 'Inactive', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper', 'RoutingPolicy.Sets.AsPath.Inactive',
                [], [],
                '''                All objects of a given type that are not
                attached to a protocol
                ''',
                'inactive',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('active', REFERENCE_CLASS, 'Active', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper', 'RoutingPolicy.Sets.AsPath.Active',
                [], [],
                '''                All objects of a given type that are attached to
                a protocol
                ''',
                'active',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            ],
            'Cisco-IOS-XR-policy-repository-oper',
            'as-path',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-policy-repository-oper'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper',
            is_config=False,
        ),
    },
    'RoutingPolicy.Sets.LargeCommunity.Sets_.Set.UsedBy.Reference' : {
        'meta_info' : _MetaInfoClass('RoutingPolicy.Sets.LargeCommunity.Sets_.Set.UsedBy.Reference', REFERENCE_LIST,
            '''Information about policies referring to this
object''',
            False, 
            [
            _MetaInfoClassMember('route-policy-name', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                Name of policy
                ''',
                'route_policy_name',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('used-directly', ATTRIBUTE, 'bool', 'boolean',
                None, None,
                [], [],
                '''                Whether the policy uses this object directly or
                indirectly
                ''',
                'used_directly',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('status', REFERENCE_ENUM_CLASS, 'ObjectStatus', 'Object-status',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper', 'ObjectStatus',
                [], [],
                '''                Active, Inactive, or Unused
                ''',
                'status',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            ],
            'Cisco-IOS-XR-policy-repository-oper',
            'reference',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-policy-repository-oper'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper',
            is_config=False,
        ),
    },
    'RoutingPolicy.Sets.LargeCommunity.Sets_.Set.UsedBy' : {
        'meta_info' : _MetaInfoClass('RoutingPolicy.Sets.LargeCommunity.Sets_.Set.UsedBy', REFERENCE_CLASS,
            '''Policies that use this object, directly or
indirectly''',
            False, 
            [
            _MetaInfoClassMember('reference', REFERENCE_LIST, 'Reference', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper', 'RoutingPolicy.Sets.LargeCommunity.Sets_.Set.UsedBy.Reference',
                [], [],
                '''                Information about policies referring to this
                object
                ''',
                'reference',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            ],
            'Cisco-IOS-XR-policy-repository-oper',
            'used-by',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-policy-repository-oper'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper',
            is_config=False,
        ),
    },
    'RoutingPolicy.Sets.LargeCommunity.Sets_.Set.Attached.Binding' : {
        'meta_info' : _MetaInfoClass('RoutingPolicy.Sets.LargeCommunity.Sets_.Set.Attached.Binding', REFERENCE_LIST,
            '''bindings list''',
            False, 
            [
            _MetaInfoClassMember('protocol', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                Protocol to which policy attached
                ''',
                'protocol',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('vrf-name', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                VRF name
                ''',
                'vrf_name',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('proto-instance', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                Protocol instance
                ''',
                'proto_instance',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('af-name', REFERENCE_ENUM_CLASS, 'AddressFamily', 'Address-family',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper', 'AddressFamily',
                [], [],
                '''                Address Family Identifier
                ''',
                'af_name',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('saf-name', REFERENCE_ENUM_CLASS, 'SubAddressFamily', 'Sub-address-family',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper', 'SubAddressFamily',
                [], [],
                '''                Subsequent Address Family Identifier
                ''',
                'saf_name',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('neighbor-address', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                Neighbor IP Address
                ''',
                'neighbor_address',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('neighbor-af-name', REFERENCE_ENUM_CLASS, 'AddressFamily', 'Address-family',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper', 'AddressFamily',
                [], [],
                '''                Neighbor IP Address Family
                ''',
                'neighbor_af_name',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('group-name', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                Neighbor Group Name
                ''',
                'group_name',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('direction', REFERENCE_ENUM_CLASS, 'AttachPointDirection', 'Attach-point-direction',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper', 'AttachPointDirection',
                [], [],
                '''                Direction In or Out
                ''',
                'direction',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('group', REFERENCE_ENUM_CLASS, 'Group', 'Group',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper', 'Group',
                [], [],
                '''                Neighbor Group 
                ''',
                'group',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('source-protocol', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                Source Protocol to redistribute, Source Protocol
                can be one of the following values{all,
                connected, local, static, bgp, rip, isis, ospf
                ,ospfv3, eigrp, unknown }
                ''',
                'source_protocol',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('aggregate-network-address', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                Aggregate IP address or Network IP Address in
                IPv4 or IPv6 Format
                ''',
                'aggregate_network_address',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('interface-name', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                Interface Name
                ''',
                'interface_name',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('instance', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                Instance
                ''',
                'instance',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('area-id', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                OSPF Area ID in Decimal Integer Format
                ''',
                'area_id',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('propogate-from', ATTRIBUTE, 'int', 'int32',
                None, None,
                [('-2147483648', '2147483647')], [],
                '''                ISIS Propogate From Level
                ''',
                'propogate_from',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('propogate-to', ATTRIBUTE, 'int', 'int32',
                None, None,
                [('-2147483648', '2147483647')], [],
                '''                ISIS Propogate To Level
                ''',
                'propogate_to',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('route-policy-name', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                Policy that uses object in question
                ''',
                'route_policy_name',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('attached-policy', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                The attached policy that (maybe indirectly) uses
                the object in question
                ''',
                'attached_policy',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('attach-point', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                Name of attach point where policy is attached
                ''',
                'attach_point',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            ],
            'Cisco-IOS-XR-policy-repository-oper',
            'binding',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-policy-repository-oper'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper',
            is_config=False,
        ),
    },
    'RoutingPolicy.Sets.LargeCommunity.Sets_.Set.Attached' : {
        'meta_info' : _MetaInfoClass('RoutingPolicy.Sets.LargeCommunity.Sets_.Set.Attached', REFERENCE_CLASS,
            '''Information about where this policy or set is
attached''',
            False, 
            [
            _MetaInfoClassMember('binding', REFERENCE_LIST, 'Binding', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper', 'RoutingPolicy.Sets.LargeCommunity.Sets_.Set.Attached.Binding',
                [], [],
                '''                bindings list
                ''',
                'binding',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            ],
            'Cisco-IOS-XR-policy-repository-oper',
            'attached',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-policy-repository-oper'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper',
            is_config=False,
        ),
    },
    'RoutingPolicy.Sets.LargeCommunity.Sets_.Set' : {
        'meta_info' : _MetaInfoClass('RoutingPolicy.Sets.LargeCommunity.Sets_.Set', REFERENCE_LIST,
            '''Information about an individual set''',
            False, 
            [
            _MetaInfoClassMember('set-name', ATTRIBUTE, 'str', 'xr:Cisco-ios-xr-string',
                None, None,
                [], [b'[\\w\\-\\.:,_@#%$\\+=\\|;]+'],
                '''                Set name
                ''',
                'set_name',
                'Cisco-IOS-XR-policy-repository-oper', True, is_config=False),
            _MetaInfoClassMember('used-by', REFERENCE_CLASS, 'UsedBy', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper', 'RoutingPolicy.Sets.LargeCommunity.Sets_.Set.UsedBy',
                [], [],
                '''                Policies that use this object, directly or
                indirectly
                ''',
                'used_by',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('attached', REFERENCE_CLASS, 'Attached', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper', 'RoutingPolicy.Sets.LargeCommunity.Sets_.Set.Attached',
                [], [],
                '''                Information about where this policy or set is
                attached
                ''',
                'attached',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            ],
            'Cisco-IOS-XR-policy-repository-oper',
            'set',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-policy-repository-oper'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper',
            is_config=False,
        ),
    },
    'RoutingPolicy.Sets.LargeCommunity.Sets_' : {
        'meta_info' : _MetaInfoClass('RoutingPolicy.Sets.LargeCommunity.Sets_', REFERENCE_CLASS,
            '''Information about individual sets''',
            False, 
            [
            _MetaInfoClassMember('set', REFERENCE_LIST, 'Set', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper', 'RoutingPolicy.Sets.LargeCommunity.Sets_.Set',
                [], [],
                '''                Information about an individual set
                ''',
                'set',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            ],
            'Cisco-IOS-XR-policy-repository-oper',
            'sets',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-policy-repository-oper'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper',
            is_config=False,
        ),
    },
    'RoutingPolicy.Sets.LargeCommunity.Unused' : {
        'meta_info' : _MetaInfoClass('RoutingPolicy.Sets.LargeCommunity.Unused', REFERENCE_CLASS,
            '''All objects of a given type that are not
referenced at all''',
            False, 
            [
            _MetaInfoClassMember('object', REFERENCE_LEAFLIST, 'str', 'String',
                None, None,
                [], [],
                '''                Policy objects
                ''',
                'object',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            ],
            'Cisco-IOS-XR-policy-repository-oper',
            'unused',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-policy-repository-oper'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper',
            is_config=False,
        ),
    },
    'RoutingPolicy.Sets.LargeCommunity.Inactive' : {
        'meta_info' : _MetaInfoClass('RoutingPolicy.Sets.LargeCommunity.Inactive', REFERENCE_CLASS,
            '''All objects of a given type that are not
attached to a protocol''',
            False, 
            [
            _MetaInfoClassMember('object', REFERENCE_LEAFLIST, 'str', 'String',
                None, None,
                [], [],
                '''                Policy objects
                ''',
                'object',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            ],
            'Cisco-IOS-XR-policy-repository-oper',
            'inactive',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-policy-repository-oper'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper',
            is_config=False,
        ),
    },
    'RoutingPolicy.Sets.LargeCommunity.Active' : {
        'meta_info' : _MetaInfoClass('RoutingPolicy.Sets.LargeCommunity.Active', REFERENCE_CLASS,
            '''All objects of a given type that are attached to
a protocol''',
            False, 
            [
            _MetaInfoClassMember('object', REFERENCE_LEAFLIST, 'str', 'String',
                None, None,
                [], [],
                '''                Policy objects
                ''',
                'object',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            ],
            'Cisco-IOS-XR-policy-repository-oper',
            'active',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-policy-repository-oper'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper',
            is_config=False,
        ),
    },
    'RoutingPolicy.Sets.LargeCommunity' : {
        'meta_info' : _MetaInfoClass('RoutingPolicy.Sets.LargeCommunity', REFERENCE_CLASS,
            '''Information about Large Community sets''',
            False, 
            [
            _MetaInfoClassMember('sets', REFERENCE_CLASS, 'Sets_', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper', 'RoutingPolicy.Sets.LargeCommunity.Sets_',
                [], [],
                '''                Information about individual sets
                ''',
                'sets',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('unused', REFERENCE_CLASS, 'Unused', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper', 'RoutingPolicy.Sets.LargeCommunity.Unused',
                [], [],
                '''                All objects of a given type that are not
                referenced at all
                ''',
                'unused',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('inactive', REFERENCE_CLASS, 'Inactive', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper', 'RoutingPolicy.Sets.LargeCommunity.Inactive',
                [], [],
                '''                All objects of a given type that are not
                attached to a protocol
                ''',
                'inactive',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('active', REFERENCE_CLASS, 'Active', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper', 'RoutingPolicy.Sets.LargeCommunity.Active',
                [], [],
                '''                All objects of a given type that are attached to
                a protocol
                ''',
                'active',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            ],
            'Cisco-IOS-XR-policy-repository-oper',
            'large-community',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-policy-repository-oper'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper',
            is_config=False,
        ),
    },
    'RoutingPolicy.Sets.Esi.Sets_.Set.UsedBy.Reference' : {
        'meta_info' : _MetaInfoClass('RoutingPolicy.Sets.Esi.Sets_.Set.UsedBy.Reference', REFERENCE_LIST,
            '''Information about policies referring to this
object''',
            False, 
            [
            _MetaInfoClassMember('route-policy-name', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                Name of policy
                ''',
                'route_policy_name',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('used-directly', ATTRIBUTE, 'bool', 'boolean',
                None, None,
                [], [],
                '''                Whether the policy uses this object directly or
                indirectly
                ''',
                'used_directly',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('status', REFERENCE_ENUM_CLASS, 'ObjectStatus', 'Object-status',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper', 'ObjectStatus',
                [], [],
                '''                Active, Inactive, or Unused
                ''',
                'status',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            ],
            'Cisco-IOS-XR-policy-repository-oper',
            'reference',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-policy-repository-oper'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper',
            is_config=False,
        ),
    },
    'RoutingPolicy.Sets.Esi.Sets_.Set.UsedBy' : {
        'meta_info' : _MetaInfoClass('RoutingPolicy.Sets.Esi.Sets_.Set.UsedBy', REFERENCE_CLASS,
            '''Policies that use this object, directly or
indirectly''',
            False, 
            [
            _MetaInfoClassMember('reference', REFERENCE_LIST, 'Reference', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper', 'RoutingPolicy.Sets.Esi.Sets_.Set.UsedBy.Reference',
                [], [],
                '''                Information about policies referring to this
                object
                ''',
                'reference',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            ],
            'Cisco-IOS-XR-policy-repository-oper',
            'used-by',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-policy-repository-oper'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper',
            is_config=False,
        ),
    },
    'RoutingPolicy.Sets.Esi.Sets_.Set.Attached.Binding' : {
        'meta_info' : _MetaInfoClass('RoutingPolicy.Sets.Esi.Sets_.Set.Attached.Binding', REFERENCE_LIST,
            '''bindings list''',
            False, 
            [
            _MetaInfoClassMember('protocol', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                Protocol to which policy attached
                ''',
                'protocol',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('vrf-name', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                VRF name
                ''',
                'vrf_name',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('proto-instance', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                Protocol instance
                ''',
                'proto_instance',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('af-name', REFERENCE_ENUM_CLASS, 'AddressFamily', 'Address-family',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper', 'AddressFamily',
                [], [],
                '''                Address Family Identifier
                ''',
                'af_name',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('saf-name', REFERENCE_ENUM_CLASS, 'SubAddressFamily', 'Sub-address-family',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper', 'SubAddressFamily',
                [], [],
                '''                Subsequent Address Family Identifier
                ''',
                'saf_name',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('neighbor-address', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                Neighbor IP Address
                ''',
                'neighbor_address',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('neighbor-af-name', REFERENCE_ENUM_CLASS, 'AddressFamily', 'Address-family',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper', 'AddressFamily',
                [], [],
                '''                Neighbor IP Address Family
                ''',
                'neighbor_af_name',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('group-name', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                Neighbor Group Name
                ''',
                'group_name',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('direction', REFERENCE_ENUM_CLASS, 'AttachPointDirection', 'Attach-point-direction',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper', 'AttachPointDirection',
                [], [],
                '''                Direction In or Out
                ''',
                'direction',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('group', REFERENCE_ENUM_CLASS, 'Group', 'Group',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper', 'Group',
                [], [],
                '''                Neighbor Group 
                ''',
                'group',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('source-protocol', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                Source Protocol to redistribute, Source Protocol
                can be one of the following values{all,
                connected, local, static, bgp, rip, isis, ospf
                ,ospfv3, eigrp, unknown }
                ''',
                'source_protocol',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('aggregate-network-address', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                Aggregate IP address or Network IP Address in
                IPv4 or IPv6 Format
                ''',
                'aggregate_network_address',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('interface-name', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                Interface Name
                ''',
                'interface_name',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('instance', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                Instance
                ''',
                'instance',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('area-id', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                OSPF Area ID in Decimal Integer Format
                ''',
                'area_id',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('propogate-from', ATTRIBUTE, 'int', 'int32',
                None, None,
                [('-2147483648', '2147483647')], [],
                '''                ISIS Propogate From Level
                ''',
                'propogate_from',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('propogate-to', ATTRIBUTE, 'int', 'int32',
                None, None,
                [('-2147483648', '2147483647')], [],
                '''                ISIS Propogate To Level
                ''',
                'propogate_to',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('route-policy-name', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                Policy that uses object in question
                ''',
                'route_policy_name',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('attached-policy', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                The attached policy that (maybe indirectly) uses
                the object in question
                ''',
                'attached_policy',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('attach-point', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                Name of attach point where policy is attached
                ''',
                'attach_point',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            ],
            'Cisco-IOS-XR-policy-repository-oper',
            'binding',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-policy-repository-oper'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper',
            is_config=False,
        ),
    },
    'RoutingPolicy.Sets.Esi.Sets_.Set.Attached' : {
        'meta_info' : _MetaInfoClass('RoutingPolicy.Sets.Esi.Sets_.Set.Attached', REFERENCE_CLASS,
            '''Information about where this policy or set is
attached''',
            False, 
            [
            _MetaInfoClassMember('binding', REFERENCE_LIST, 'Binding', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper', 'RoutingPolicy.Sets.Esi.Sets_.Set.Attached.Binding',
                [], [],
                '''                bindings list
                ''',
                'binding',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            ],
            'Cisco-IOS-XR-policy-repository-oper',
            'attached',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-policy-repository-oper'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper',
            is_config=False,
        ),
    },
    'RoutingPolicy.Sets.Esi.Sets_.Set' : {
        'meta_info' : _MetaInfoClass('RoutingPolicy.Sets.Esi.Sets_.Set', REFERENCE_LIST,
            '''Information about an individual set''',
            False, 
            [
            _MetaInfoClassMember('set-name', ATTRIBUTE, 'str', 'xr:Cisco-ios-xr-string',
                None, None,
                [], [b'[\\w\\-\\.:,_@#%$\\+=\\|;]+'],
                '''                Set name
                ''',
                'set_name',
                'Cisco-IOS-XR-policy-repository-oper', True, is_config=False),
            _MetaInfoClassMember('used-by', REFERENCE_CLASS, 'UsedBy', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper', 'RoutingPolicy.Sets.Esi.Sets_.Set.UsedBy',
                [], [],
                '''                Policies that use this object, directly or
                indirectly
                ''',
                'used_by',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('attached', REFERENCE_CLASS, 'Attached', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper', 'RoutingPolicy.Sets.Esi.Sets_.Set.Attached',
                [], [],
                '''                Information about where this policy or set is
                attached
                ''',
                'attached',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            ],
            'Cisco-IOS-XR-policy-repository-oper',
            'set',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-policy-repository-oper'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper',
            is_config=False,
        ),
    },
    'RoutingPolicy.Sets.Esi.Sets_' : {
        'meta_info' : _MetaInfoClass('RoutingPolicy.Sets.Esi.Sets_', REFERENCE_CLASS,
            '''Information about individual sets''',
            False, 
            [
            _MetaInfoClassMember('set', REFERENCE_LIST, 'Set', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper', 'RoutingPolicy.Sets.Esi.Sets_.Set',
                [], [],
                '''                Information about an individual set
                ''',
                'set',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            ],
            'Cisco-IOS-XR-policy-repository-oper',
            'sets',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-policy-repository-oper'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper',
            is_config=False,
        ),
    },
    'RoutingPolicy.Sets.Esi.Unused' : {
        'meta_info' : _MetaInfoClass('RoutingPolicy.Sets.Esi.Unused', REFERENCE_CLASS,
            '''All objects of a given type that are not
referenced at all''',
            False, 
            [
            _MetaInfoClassMember('object', REFERENCE_LEAFLIST, 'str', 'String',
                None, None,
                [], [],
                '''                Policy objects
                ''',
                'object',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            ],
            'Cisco-IOS-XR-policy-repository-oper',
            'unused',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-policy-repository-oper'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper',
            is_config=False,
        ),
    },
    'RoutingPolicy.Sets.Esi.Inactive' : {
        'meta_info' : _MetaInfoClass('RoutingPolicy.Sets.Esi.Inactive', REFERENCE_CLASS,
            '''All objects of a given type that are not
attached to a protocol''',
            False, 
            [
            _MetaInfoClassMember('object', REFERENCE_LEAFLIST, 'str', 'String',
                None, None,
                [], [],
                '''                Policy objects
                ''',
                'object',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            ],
            'Cisco-IOS-XR-policy-repository-oper',
            'inactive',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-policy-repository-oper'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper',
            is_config=False,
        ),
    },
    'RoutingPolicy.Sets.Esi.Active' : {
        'meta_info' : _MetaInfoClass('RoutingPolicy.Sets.Esi.Active', REFERENCE_CLASS,
            '''All objects of a given type that are attached to
a protocol''',
            False, 
            [
            _MetaInfoClassMember('object', REFERENCE_LEAFLIST, 'str', 'String',
                None, None,
                [], [],
                '''                Policy objects
                ''',
                'object',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            ],
            'Cisco-IOS-XR-policy-repository-oper',
            'active',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-policy-repository-oper'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper',
            is_config=False,
        ),
    },
    'RoutingPolicy.Sets.Esi' : {
        'meta_info' : _MetaInfoClass('RoutingPolicy.Sets.Esi', REFERENCE_CLASS,
            '''Information about Esi sets''',
            False, 
            [
            _MetaInfoClassMember('sets', REFERENCE_CLASS, 'Sets_', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper', 'RoutingPolicy.Sets.Esi.Sets_',
                [], [],
                '''                Information about individual sets
                ''',
                'sets',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('unused', REFERENCE_CLASS, 'Unused', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper', 'RoutingPolicy.Sets.Esi.Unused',
                [], [],
                '''                All objects of a given type that are not
                referenced at all
                ''',
                'unused',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('inactive', REFERENCE_CLASS, 'Inactive', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper', 'RoutingPolicy.Sets.Esi.Inactive',
                [], [],
                '''                All objects of a given type that are not
                attached to a protocol
                ''',
                'inactive',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('active', REFERENCE_CLASS, 'Active', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper', 'RoutingPolicy.Sets.Esi.Active',
                [], [],
                '''                All objects of a given type that are attached to
                a protocol
                ''',
                'active',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            ],
            'Cisco-IOS-XR-policy-repository-oper',
            'esi',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-policy-repository-oper'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper',
            is_config=False,
        ),
    },
    'RoutingPolicy.Sets.ExtendedCommunityBandwidth.Sets_.Set.UsedBy.Reference' : {
        'meta_info' : _MetaInfoClass('RoutingPolicy.Sets.ExtendedCommunityBandwidth.Sets_.Set.UsedBy.Reference', REFERENCE_LIST,
            '''Information about policies referring to this
object''',
            False, 
            [
            _MetaInfoClassMember('route-policy-name', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                Name of policy
                ''',
                'route_policy_name',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('used-directly', ATTRIBUTE, 'bool', 'boolean',
                None, None,
                [], [],
                '''                Whether the policy uses this object directly or
                indirectly
                ''',
                'used_directly',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('status', REFERENCE_ENUM_CLASS, 'ObjectStatus', 'Object-status',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper', 'ObjectStatus',
                [], [],
                '''                Active, Inactive, or Unused
                ''',
                'status',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            ],
            'Cisco-IOS-XR-policy-repository-oper',
            'reference',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-policy-repository-oper'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper',
            is_config=False,
        ),
    },
    'RoutingPolicy.Sets.ExtendedCommunityBandwidth.Sets_.Set.UsedBy' : {
        'meta_info' : _MetaInfoClass('RoutingPolicy.Sets.ExtendedCommunityBandwidth.Sets_.Set.UsedBy', REFERENCE_CLASS,
            '''Policies that use this object, directly or
indirectly''',
            False, 
            [
            _MetaInfoClassMember('reference', REFERENCE_LIST, 'Reference', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper', 'RoutingPolicy.Sets.ExtendedCommunityBandwidth.Sets_.Set.UsedBy.Reference',
                [], [],
                '''                Information about policies referring to this
                object
                ''',
                'reference',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            ],
            'Cisco-IOS-XR-policy-repository-oper',
            'used-by',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-policy-repository-oper'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper',
            is_config=False,
        ),
    },
    'RoutingPolicy.Sets.ExtendedCommunityBandwidth.Sets_.Set.Attached.Binding' : {
        'meta_info' : _MetaInfoClass('RoutingPolicy.Sets.ExtendedCommunityBandwidth.Sets_.Set.Attached.Binding', REFERENCE_LIST,
            '''bindings list''',
            False, 
            [
            _MetaInfoClassMember('protocol', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                Protocol to which policy attached
                ''',
                'protocol',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('vrf-name', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                VRF name
                ''',
                'vrf_name',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('proto-instance', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                Protocol instance
                ''',
                'proto_instance',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('af-name', REFERENCE_ENUM_CLASS, 'AddressFamily', 'Address-family',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper', 'AddressFamily',
                [], [],
                '''                Address Family Identifier
                ''',
                'af_name',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('saf-name', REFERENCE_ENUM_CLASS, 'SubAddressFamily', 'Sub-address-family',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper', 'SubAddressFamily',
                [], [],
                '''                Subsequent Address Family Identifier
                ''',
                'saf_name',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('neighbor-address', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                Neighbor IP Address
                ''',
                'neighbor_address',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('neighbor-af-name', REFERENCE_ENUM_CLASS, 'AddressFamily', 'Address-family',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper', 'AddressFamily',
                [], [],
                '''                Neighbor IP Address Family
                ''',
                'neighbor_af_name',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('group-name', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                Neighbor Group Name
                ''',
                'group_name',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('direction', REFERENCE_ENUM_CLASS, 'AttachPointDirection', 'Attach-point-direction',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper', 'AttachPointDirection',
                [], [],
                '''                Direction In or Out
                ''',
                'direction',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('group', REFERENCE_ENUM_CLASS, 'Group', 'Group',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper', 'Group',
                [], [],
                '''                Neighbor Group 
                ''',
                'group',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('source-protocol', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                Source Protocol to redistribute, Source Protocol
                can be one of the following values{all,
                connected, local, static, bgp, rip, isis, ospf
                ,ospfv3, eigrp, unknown }
                ''',
                'source_protocol',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('aggregate-network-address', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                Aggregate IP address or Network IP Address in
                IPv4 or IPv6 Format
                ''',
                'aggregate_network_address',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('interface-name', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                Interface Name
                ''',
                'interface_name',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('instance', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                Instance
                ''',
                'instance',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('area-id', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                OSPF Area ID in Decimal Integer Format
                ''',
                'area_id',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('propogate-from', ATTRIBUTE, 'int', 'int32',
                None, None,
                [('-2147483648', '2147483647')], [],
                '''                ISIS Propogate From Level
                ''',
                'propogate_from',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('propogate-to', ATTRIBUTE, 'int', 'int32',
                None, None,
                [('-2147483648', '2147483647')], [],
                '''                ISIS Propogate To Level
                ''',
                'propogate_to',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('route-policy-name', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                Policy that uses object in question
                ''',
                'route_policy_name',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('attached-policy', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                The attached policy that (maybe indirectly) uses
                the object in question
                ''',
                'attached_policy',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('attach-point', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                Name of attach point where policy is attached
                ''',
                'attach_point',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            ],
            'Cisco-IOS-XR-policy-repository-oper',
            'binding',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-policy-repository-oper'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper',
            is_config=False,
        ),
    },
    'RoutingPolicy.Sets.ExtendedCommunityBandwidth.Sets_.Set.Attached' : {
        'meta_info' : _MetaInfoClass('RoutingPolicy.Sets.ExtendedCommunityBandwidth.Sets_.Set.Attached', REFERENCE_CLASS,
            '''Information about where this policy or set is
attached''',
            False, 
            [
            _MetaInfoClassMember('binding', REFERENCE_LIST, 'Binding', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper', 'RoutingPolicy.Sets.ExtendedCommunityBandwidth.Sets_.Set.Attached.Binding',
                [], [],
                '''                bindings list
                ''',
                'binding',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            ],
            'Cisco-IOS-XR-policy-repository-oper',
            'attached',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-policy-repository-oper'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper',
            is_config=False,
        ),
    },
    'RoutingPolicy.Sets.ExtendedCommunityBandwidth.Sets_.Set' : {
        'meta_info' : _MetaInfoClass('RoutingPolicy.Sets.ExtendedCommunityBandwidth.Sets_.Set', REFERENCE_LIST,
            '''Information about an individual set''',
            False, 
            [
            _MetaInfoClassMember('set-name', ATTRIBUTE, 'str', 'xr:Cisco-ios-xr-string',
                None, None,
                [], [b'[\\w\\-\\.:,_@#%$\\+=\\|;]+'],
                '''                Set name
                ''',
                'set_name',
                'Cisco-IOS-XR-policy-repository-oper', True, is_config=False),
            _MetaInfoClassMember('used-by', REFERENCE_CLASS, 'UsedBy', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper', 'RoutingPolicy.Sets.ExtendedCommunityBandwidth.Sets_.Set.UsedBy',
                [], [],
                '''                Policies that use this object, directly or
                indirectly
                ''',
                'used_by',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('attached', REFERENCE_CLASS, 'Attached', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper', 'RoutingPolicy.Sets.ExtendedCommunityBandwidth.Sets_.Set.Attached',
                [], [],
                '''                Information about where this policy or set is
                attached
                ''',
                'attached',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            ],
            'Cisco-IOS-XR-policy-repository-oper',
            'set',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-policy-repository-oper'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper',
            is_config=False,
        ),
    },
    'RoutingPolicy.Sets.ExtendedCommunityBandwidth.Sets_' : {
        'meta_info' : _MetaInfoClass('RoutingPolicy.Sets.ExtendedCommunityBandwidth.Sets_', REFERENCE_CLASS,
            '''Information about individual sets''',
            False, 
            [
            _MetaInfoClassMember('set', REFERENCE_LIST, 'Set', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper', 'RoutingPolicy.Sets.ExtendedCommunityBandwidth.Sets_.Set',
                [], [],
                '''                Information about an individual set
                ''',
                'set',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            ],
            'Cisco-IOS-XR-policy-repository-oper',
            'sets',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-policy-repository-oper'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper',
            is_config=False,
        ),
    },
    'RoutingPolicy.Sets.ExtendedCommunityBandwidth.Unused' : {
        'meta_info' : _MetaInfoClass('RoutingPolicy.Sets.ExtendedCommunityBandwidth.Unused', REFERENCE_CLASS,
            '''All objects of a given type that are not
referenced at all''',
            False, 
            [
            _MetaInfoClassMember('object', REFERENCE_LEAFLIST, 'str', 'String',
                None, None,
                [], [],
                '''                Policy objects
                ''',
                'object',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            ],
            'Cisco-IOS-XR-policy-repository-oper',
            'unused',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-policy-repository-oper'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper',
            is_config=False,
        ),
    },
    'RoutingPolicy.Sets.ExtendedCommunityBandwidth.Inactive' : {
        'meta_info' : _MetaInfoClass('RoutingPolicy.Sets.ExtendedCommunityBandwidth.Inactive', REFERENCE_CLASS,
            '''All objects of a given type that are not
attached to a protocol''',
            False, 
            [
            _MetaInfoClassMember('object', REFERENCE_LEAFLIST, 'str', 'String',
                None, None,
                [], [],
                '''                Policy objects
                ''',
                'object',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            ],
            'Cisco-IOS-XR-policy-repository-oper',
            'inactive',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-policy-repository-oper'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper',
            is_config=False,
        ),
    },
    'RoutingPolicy.Sets.ExtendedCommunityBandwidth' : {
        'meta_info' : _MetaInfoClass('RoutingPolicy.Sets.ExtendedCommunityBandwidth', REFERENCE_CLASS,
            '''Information about Extended Community Bandwidth
sets''',
            False, 
            [
            _MetaInfoClassMember('sets', REFERENCE_CLASS, 'Sets_', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper', 'RoutingPolicy.Sets.ExtendedCommunityBandwidth.Sets_',
                [], [],
                '''                Information about individual sets
                ''',
                'sets',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('unused', REFERENCE_CLASS, 'Unused', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper', 'RoutingPolicy.Sets.ExtendedCommunityBandwidth.Unused',
                [], [],
                '''                All objects of a given type that are not
                referenced at all
                ''',
                'unused',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('inactive', REFERENCE_CLASS, 'Inactive', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper', 'RoutingPolicy.Sets.ExtendedCommunityBandwidth.Inactive',
                [], [],
                '''                All objects of a given type that are not
                attached to a protocol
                ''',
                'inactive',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            ],
            'Cisco-IOS-XR-policy-repository-oper',
            'extended-community-bandwidth',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-policy-repository-oper'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper',
            is_config=False,
        ),
    },
    'RoutingPolicy.Sets.ExtendedCommunityRt.Sets_.Set.UsedBy.Reference' : {
        'meta_info' : _MetaInfoClass('RoutingPolicy.Sets.ExtendedCommunityRt.Sets_.Set.UsedBy.Reference', REFERENCE_LIST,
            '''Information about policies referring to this
object''',
            False, 
            [
            _MetaInfoClassMember('route-policy-name', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                Name of policy
                ''',
                'route_policy_name',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('used-directly', ATTRIBUTE, 'bool', 'boolean',
                None, None,
                [], [],
                '''                Whether the policy uses this object directly or
                indirectly
                ''',
                'used_directly',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('status', REFERENCE_ENUM_CLASS, 'ObjectStatus', 'Object-status',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper', 'ObjectStatus',
                [], [],
                '''                Active, Inactive, or Unused
                ''',
                'status',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            ],
            'Cisco-IOS-XR-policy-repository-oper',
            'reference',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-policy-repository-oper'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper',
            is_config=False,
        ),
    },
    'RoutingPolicy.Sets.ExtendedCommunityRt.Sets_.Set.UsedBy' : {
        'meta_info' : _MetaInfoClass('RoutingPolicy.Sets.ExtendedCommunityRt.Sets_.Set.UsedBy', REFERENCE_CLASS,
            '''Policies that use this object, directly or
indirectly''',
            False, 
            [
            _MetaInfoClassMember('reference', REFERENCE_LIST, 'Reference', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper', 'RoutingPolicy.Sets.ExtendedCommunityRt.Sets_.Set.UsedBy.Reference',
                [], [],
                '''                Information about policies referring to this
                object
                ''',
                'reference',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            ],
            'Cisco-IOS-XR-policy-repository-oper',
            'used-by',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-policy-repository-oper'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper',
            is_config=False,
        ),
    },
    'RoutingPolicy.Sets.ExtendedCommunityRt.Sets_.Set.Attached.Binding' : {
        'meta_info' : _MetaInfoClass('RoutingPolicy.Sets.ExtendedCommunityRt.Sets_.Set.Attached.Binding', REFERENCE_LIST,
            '''bindings list''',
            False, 
            [
            _MetaInfoClassMember('protocol', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                Protocol to which policy attached
                ''',
                'protocol',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('vrf-name', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                VRF name
                ''',
                'vrf_name',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('proto-instance', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                Protocol instance
                ''',
                'proto_instance',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('af-name', REFERENCE_ENUM_CLASS, 'AddressFamily', 'Address-family',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper', 'AddressFamily',
                [], [],
                '''                Address Family Identifier
                ''',
                'af_name',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('saf-name', REFERENCE_ENUM_CLASS, 'SubAddressFamily', 'Sub-address-family',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper', 'SubAddressFamily',
                [], [],
                '''                Subsequent Address Family Identifier
                ''',
                'saf_name',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('neighbor-address', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                Neighbor IP Address
                ''',
                'neighbor_address',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('neighbor-af-name', REFERENCE_ENUM_CLASS, 'AddressFamily', 'Address-family',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper', 'AddressFamily',
                [], [],
                '''                Neighbor IP Address Family
                ''',
                'neighbor_af_name',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('group-name', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                Neighbor Group Name
                ''',
                'group_name',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('direction', REFERENCE_ENUM_CLASS, 'AttachPointDirection', 'Attach-point-direction',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper', 'AttachPointDirection',
                [], [],
                '''                Direction In or Out
                ''',
                'direction',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('group', REFERENCE_ENUM_CLASS, 'Group', 'Group',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper', 'Group',
                [], [],
                '''                Neighbor Group 
                ''',
                'group',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('source-protocol', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                Source Protocol to redistribute, Source Protocol
                can be one of the following values{all,
                connected, local, static, bgp, rip, isis, ospf
                ,ospfv3, eigrp, unknown }
                ''',
                'source_protocol',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('aggregate-network-address', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                Aggregate IP address or Network IP Address in
                IPv4 or IPv6 Format
                ''',
                'aggregate_network_address',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('interface-name', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                Interface Name
                ''',
                'interface_name',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('instance', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                Instance
                ''',
                'instance',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('area-id', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                OSPF Area ID in Decimal Integer Format
                ''',
                'area_id',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('propogate-from', ATTRIBUTE, 'int', 'int32',
                None, None,
                [('-2147483648', '2147483647')], [],
                '''                ISIS Propogate From Level
                ''',
                'propogate_from',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('propogate-to', ATTRIBUTE, 'int', 'int32',
                None, None,
                [('-2147483648', '2147483647')], [],
                '''                ISIS Propogate To Level
                ''',
                'propogate_to',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('route-policy-name', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                Policy that uses object in question
                ''',
                'route_policy_name',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('attached-policy', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                The attached policy that (maybe indirectly) uses
                the object in question
                ''',
                'attached_policy',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('attach-point', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                Name of attach point where policy is attached
                ''',
                'attach_point',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            ],
            'Cisco-IOS-XR-policy-repository-oper',
            'binding',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-policy-repository-oper'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper',
            is_config=False,
        ),
    },
    'RoutingPolicy.Sets.ExtendedCommunityRt.Sets_.Set.Attached' : {
        'meta_info' : _MetaInfoClass('RoutingPolicy.Sets.ExtendedCommunityRt.Sets_.Set.Attached', REFERENCE_CLASS,
            '''Information about where this policy or set is
attached''',
            False, 
            [
            _MetaInfoClassMember('binding', REFERENCE_LIST, 'Binding', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper', 'RoutingPolicy.Sets.ExtendedCommunityRt.Sets_.Set.Attached.Binding',
                [], [],
                '''                bindings list
                ''',
                'binding',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            ],
            'Cisco-IOS-XR-policy-repository-oper',
            'attached',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-policy-repository-oper'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper',
            is_config=False,
        ),
    },
    'RoutingPolicy.Sets.ExtendedCommunityRt.Sets_.Set' : {
        'meta_info' : _MetaInfoClass('RoutingPolicy.Sets.ExtendedCommunityRt.Sets_.Set', REFERENCE_LIST,
            '''Information about an individual set''',
            False, 
            [
            _MetaInfoClassMember('set-name', ATTRIBUTE, 'str', 'xr:Cisco-ios-xr-string',
                None, None,
                [], [b'[\\w\\-\\.:,_@#%$\\+=\\|;]+'],
                '''                Set name
                ''',
                'set_name',
                'Cisco-IOS-XR-policy-repository-oper', True, is_config=False),
            _MetaInfoClassMember('used-by', REFERENCE_CLASS, 'UsedBy', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper', 'RoutingPolicy.Sets.ExtendedCommunityRt.Sets_.Set.UsedBy',
                [], [],
                '''                Policies that use this object, directly or
                indirectly
                ''',
                'used_by',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('attached', REFERENCE_CLASS, 'Attached', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper', 'RoutingPolicy.Sets.ExtendedCommunityRt.Sets_.Set.Attached',
                [], [],
                '''                Information about where this policy or set is
                attached
                ''',
                'attached',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            ],
            'Cisco-IOS-XR-policy-repository-oper',
            'set',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-policy-repository-oper'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper',
            is_config=False,
        ),
    },
    'RoutingPolicy.Sets.ExtendedCommunityRt.Sets_' : {
        'meta_info' : _MetaInfoClass('RoutingPolicy.Sets.ExtendedCommunityRt.Sets_', REFERENCE_CLASS,
            '''Information about individual sets''',
            False, 
            [
            _MetaInfoClassMember('set', REFERENCE_LIST, 'Set', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper', 'RoutingPolicy.Sets.ExtendedCommunityRt.Sets_.Set',
                [], [],
                '''                Information about an individual set
                ''',
                'set',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            ],
            'Cisco-IOS-XR-policy-repository-oper',
            'sets',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-policy-repository-oper'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper',
            is_config=False,
        ),
    },
    'RoutingPolicy.Sets.ExtendedCommunityRt.Unused' : {
        'meta_info' : _MetaInfoClass('RoutingPolicy.Sets.ExtendedCommunityRt.Unused', REFERENCE_CLASS,
            '''All objects of a given type that are not
referenced at all''',
            False, 
            [
            _MetaInfoClassMember('object', REFERENCE_LEAFLIST, 'str', 'String',
                None, None,
                [], [],
                '''                Policy objects
                ''',
                'object',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            ],
            'Cisco-IOS-XR-policy-repository-oper',
            'unused',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-policy-repository-oper'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper',
            is_config=False,
        ),
    },
    'RoutingPolicy.Sets.ExtendedCommunityRt.Inactive' : {
        'meta_info' : _MetaInfoClass('RoutingPolicy.Sets.ExtendedCommunityRt.Inactive', REFERENCE_CLASS,
            '''All objects of a given type that are not
attached to a protocol''',
            False, 
            [
            _MetaInfoClassMember('object', REFERENCE_LEAFLIST, 'str', 'String',
                None, None,
                [], [],
                '''                Policy objects
                ''',
                'object',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            ],
            'Cisco-IOS-XR-policy-repository-oper',
            'inactive',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-policy-repository-oper'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper',
            is_config=False,
        ),
    },
    'RoutingPolicy.Sets.ExtendedCommunityRt.Active' : {
        'meta_info' : _MetaInfoClass('RoutingPolicy.Sets.ExtendedCommunityRt.Active', REFERENCE_CLASS,
            '''All objects of a given type that are attached to
a protocol''',
            False, 
            [
            _MetaInfoClassMember('object', REFERENCE_LEAFLIST, 'str', 'String',
                None, None,
                [], [],
                '''                Policy objects
                ''',
                'object',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            ],
            'Cisco-IOS-XR-policy-repository-oper',
            'active',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-policy-repository-oper'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper',
            is_config=False,
        ),
    },
    'RoutingPolicy.Sets.ExtendedCommunityRt' : {
        'meta_info' : _MetaInfoClass('RoutingPolicy.Sets.ExtendedCommunityRt', REFERENCE_CLASS,
            '''Information about Extended Community RT sets''',
            False, 
            [
            _MetaInfoClassMember('sets', REFERENCE_CLASS, 'Sets_', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper', 'RoutingPolicy.Sets.ExtendedCommunityRt.Sets_',
                [], [],
                '''                Information about individual sets
                ''',
                'sets',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('unused', REFERENCE_CLASS, 'Unused', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper', 'RoutingPolicy.Sets.ExtendedCommunityRt.Unused',
                [], [],
                '''                All objects of a given type that are not
                referenced at all
                ''',
                'unused',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('inactive', REFERENCE_CLASS, 'Inactive', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper', 'RoutingPolicy.Sets.ExtendedCommunityRt.Inactive',
                [], [],
                '''                All objects of a given type that are not
                attached to a protocol
                ''',
                'inactive',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('active', REFERENCE_CLASS, 'Active', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper', 'RoutingPolicy.Sets.ExtendedCommunityRt.Active',
                [], [],
                '''                All objects of a given type that are attached to
                a protocol
                ''',
                'active',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            ],
            'Cisco-IOS-XR-policy-repository-oper',
            'extended-community-rt',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-policy-repository-oper'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper',
            is_config=False,
        ),
    },
    'RoutingPolicy.Sets.Rd.Sets_.Set.UsedBy.Reference' : {
        'meta_info' : _MetaInfoClass('RoutingPolicy.Sets.Rd.Sets_.Set.UsedBy.Reference', REFERENCE_LIST,
            '''Information about policies referring to this
object''',
            False, 
            [
            _MetaInfoClassMember('route-policy-name', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                Name of policy
                ''',
                'route_policy_name',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('used-directly', ATTRIBUTE, 'bool', 'boolean',
                None, None,
                [], [],
                '''                Whether the policy uses this object directly or
                indirectly
                ''',
                'used_directly',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('status', REFERENCE_ENUM_CLASS, 'ObjectStatus', 'Object-status',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper', 'ObjectStatus',
                [], [],
                '''                Active, Inactive, or Unused
                ''',
                'status',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            ],
            'Cisco-IOS-XR-policy-repository-oper',
            'reference',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-policy-repository-oper'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper',
            is_config=False,
        ),
    },
    'RoutingPolicy.Sets.Rd.Sets_.Set.UsedBy' : {
        'meta_info' : _MetaInfoClass('RoutingPolicy.Sets.Rd.Sets_.Set.UsedBy', REFERENCE_CLASS,
            '''Policies that use this object, directly or
indirectly''',
            False, 
            [
            _MetaInfoClassMember('reference', REFERENCE_LIST, 'Reference', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper', 'RoutingPolicy.Sets.Rd.Sets_.Set.UsedBy.Reference',
                [], [],
                '''                Information about policies referring to this
                object
                ''',
                'reference',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            ],
            'Cisco-IOS-XR-policy-repository-oper',
            'used-by',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-policy-repository-oper'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper',
            is_config=False,
        ),
    },
    'RoutingPolicy.Sets.Rd.Sets_.Set.Attached.Binding' : {
        'meta_info' : _MetaInfoClass('RoutingPolicy.Sets.Rd.Sets_.Set.Attached.Binding', REFERENCE_LIST,
            '''bindings list''',
            False, 
            [
            _MetaInfoClassMember('protocol', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                Protocol to which policy attached
                ''',
                'protocol',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('vrf-name', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                VRF name
                ''',
                'vrf_name',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('proto-instance', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                Protocol instance
                ''',
                'proto_instance',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('af-name', REFERENCE_ENUM_CLASS, 'AddressFamily', 'Address-family',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper', 'AddressFamily',
                [], [],
                '''                Address Family Identifier
                ''',
                'af_name',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('saf-name', REFERENCE_ENUM_CLASS, 'SubAddressFamily', 'Sub-address-family',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper', 'SubAddressFamily',
                [], [],
                '''                Subsequent Address Family Identifier
                ''',
                'saf_name',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('neighbor-address', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                Neighbor IP Address
                ''',
                'neighbor_address',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('neighbor-af-name', REFERENCE_ENUM_CLASS, 'AddressFamily', 'Address-family',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper', 'AddressFamily',
                [], [],
                '''                Neighbor IP Address Family
                ''',
                'neighbor_af_name',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('group-name', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                Neighbor Group Name
                ''',
                'group_name',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('direction', REFERENCE_ENUM_CLASS, 'AttachPointDirection', 'Attach-point-direction',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper', 'AttachPointDirection',
                [], [],
                '''                Direction In or Out
                ''',
                'direction',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('group', REFERENCE_ENUM_CLASS, 'Group', 'Group',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper', 'Group',
                [], [],
                '''                Neighbor Group 
                ''',
                'group',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('source-protocol', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                Source Protocol to redistribute, Source Protocol
                can be one of the following values{all,
                connected, local, static, bgp, rip, isis, ospf
                ,ospfv3, eigrp, unknown }
                ''',
                'source_protocol',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('aggregate-network-address', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                Aggregate IP address or Network IP Address in
                IPv4 or IPv6 Format
                ''',
                'aggregate_network_address',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('interface-name', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                Interface Name
                ''',
                'interface_name',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('instance', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                Instance
                ''',
                'instance',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('area-id', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                OSPF Area ID in Decimal Integer Format
                ''',
                'area_id',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('propogate-from', ATTRIBUTE, 'int', 'int32',
                None, None,
                [('-2147483648', '2147483647')], [],
                '''                ISIS Propogate From Level
                ''',
                'propogate_from',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('propogate-to', ATTRIBUTE, 'int', 'int32',
                None, None,
                [('-2147483648', '2147483647')], [],
                '''                ISIS Propogate To Level
                ''',
                'propogate_to',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('route-policy-name', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                Policy that uses object in question
                ''',
                'route_policy_name',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('attached-policy', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                The attached policy that (maybe indirectly) uses
                the object in question
                ''',
                'attached_policy',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('attach-point', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                Name of attach point where policy is attached
                ''',
                'attach_point',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            ],
            'Cisco-IOS-XR-policy-repository-oper',
            'binding',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-policy-repository-oper'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper',
            is_config=False,
        ),
    },
    'RoutingPolicy.Sets.Rd.Sets_.Set.Attached' : {
        'meta_info' : _MetaInfoClass('RoutingPolicy.Sets.Rd.Sets_.Set.Attached', REFERENCE_CLASS,
            '''Information about where this policy or set is
attached''',
            False, 
            [
            _MetaInfoClassMember('binding', REFERENCE_LIST, 'Binding', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper', 'RoutingPolicy.Sets.Rd.Sets_.Set.Attached.Binding',
                [], [],
                '''                bindings list
                ''',
                'binding',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            ],
            'Cisco-IOS-XR-policy-repository-oper',
            'attached',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-policy-repository-oper'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper',
            is_config=False,
        ),
    },
    'RoutingPolicy.Sets.Rd.Sets_.Set' : {
        'meta_info' : _MetaInfoClass('RoutingPolicy.Sets.Rd.Sets_.Set', REFERENCE_LIST,
            '''Information about an individual set''',
            False, 
            [
            _MetaInfoClassMember('set-name', ATTRIBUTE, 'str', 'xr:Cisco-ios-xr-string',
                None, None,
                [], [b'[\\w\\-\\.:,_@#%$\\+=\\|;]+'],
                '''                Set name
                ''',
                'set_name',
                'Cisco-IOS-XR-policy-repository-oper', True, is_config=False),
            _MetaInfoClassMember('used-by', REFERENCE_CLASS, 'UsedBy', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper', 'RoutingPolicy.Sets.Rd.Sets_.Set.UsedBy',
                [], [],
                '''                Policies that use this object, directly or
                indirectly
                ''',
                'used_by',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('attached', REFERENCE_CLASS, 'Attached', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper', 'RoutingPolicy.Sets.Rd.Sets_.Set.Attached',
                [], [],
                '''                Information about where this policy or set is
                attached
                ''',
                'attached',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            ],
            'Cisco-IOS-XR-policy-repository-oper',
            'set',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-policy-repository-oper'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper',
            is_config=False,
        ),
    },
    'RoutingPolicy.Sets.Rd.Sets_' : {
        'meta_info' : _MetaInfoClass('RoutingPolicy.Sets.Rd.Sets_', REFERENCE_CLASS,
            '''Information about individual sets''',
            False, 
            [
            _MetaInfoClassMember('set', REFERENCE_LIST, 'Set', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper', 'RoutingPolicy.Sets.Rd.Sets_.Set',
                [], [],
                '''                Information about an individual set
                ''',
                'set',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            ],
            'Cisco-IOS-XR-policy-repository-oper',
            'sets',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-policy-repository-oper'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper',
            is_config=False,
        ),
    },
    'RoutingPolicy.Sets.Rd.Unused' : {
        'meta_info' : _MetaInfoClass('RoutingPolicy.Sets.Rd.Unused', REFERENCE_CLASS,
            '''All objects of a given type that are not
referenced at all''',
            False, 
            [
            _MetaInfoClassMember('object', REFERENCE_LEAFLIST, 'str', 'String',
                None, None,
                [], [],
                '''                Policy objects
                ''',
                'object',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            ],
            'Cisco-IOS-XR-policy-repository-oper',
            'unused',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-policy-repository-oper'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper',
            is_config=False,
        ),
    },
    'RoutingPolicy.Sets.Rd.Inactive' : {
        'meta_info' : _MetaInfoClass('RoutingPolicy.Sets.Rd.Inactive', REFERENCE_CLASS,
            '''All objects of a given type that are not
attached to a protocol''',
            False, 
            [
            _MetaInfoClassMember('object', REFERENCE_LEAFLIST, 'str', 'String',
                None, None,
                [], [],
                '''                Policy objects
                ''',
                'object',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            ],
            'Cisco-IOS-XR-policy-repository-oper',
            'inactive',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-policy-repository-oper'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper',
            is_config=False,
        ),
    },
    'RoutingPolicy.Sets.Rd.Active' : {
        'meta_info' : _MetaInfoClass('RoutingPolicy.Sets.Rd.Active', REFERENCE_CLASS,
            '''All objects of a given type that are attached to
a protocol''',
            False, 
            [
            _MetaInfoClassMember('object', REFERENCE_LEAFLIST, 'str', 'String',
                None, None,
                [], [],
                '''                Policy objects
                ''',
                'object',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            ],
            'Cisco-IOS-XR-policy-repository-oper',
            'active',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-policy-repository-oper'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper',
            is_config=False,
        ),
    },
    'RoutingPolicy.Sets.Rd' : {
        'meta_info' : _MetaInfoClass('RoutingPolicy.Sets.Rd', REFERENCE_CLASS,
            '''Information about RD sets''',
            False, 
            [
            _MetaInfoClassMember('sets', REFERENCE_CLASS, 'Sets_', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper', 'RoutingPolicy.Sets.Rd.Sets_',
                [], [],
                '''                Information about individual sets
                ''',
                'sets',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('unused', REFERENCE_CLASS, 'Unused', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper', 'RoutingPolicy.Sets.Rd.Unused',
                [], [],
                '''                All objects of a given type that are not
                referenced at all
                ''',
                'unused',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('inactive', REFERENCE_CLASS, 'Inactive', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper', 'RoutingPolicy.Sets.Rd.Inactive',
                [], [],
                '''                All objects of a given type that are not
                attached to a protocol
                ''',
                'inactive',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('active', REFERENCE_CLASS, 'Active', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper', 'RoutingPolicy.Sets.Rd.Active',
                [], [],
                '''                All objects of a given type that are attached to
                a protocol
                ''',
                'active',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            ],
            'Cisco-IOS-XR-policy-repository-oper',
            'rd',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-policy-repository-oper'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper',
            is_config=False,
        ),
    },
    'RoutingPolicy.Sets.Mac.Sets_.Set.UsedBy.Reference' : {
        'meta_info' : _MetaInfoClass('RoutingPolicy.Sets.Mac.Sets_.Set.UsedBy.Reference', REFERENCE_LIST,
            '''Information about policies referring to this
object''',
            False, 
            [
            _MetaInfoClassMember('route-policy-name', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                Name of policy
                ''',
                'route_policy_name',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('used-directly', ATTRIBUTE, 'bool', 'boolean',
                None, None,
                [], [],
                '''                Whether the policy uses this object directly or
                indirectly
                ''',
                'used_directly',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('status', REFERENCE_ENUM_CLASS, 'ObjectStatus', 'Object-status',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper', 'ObjectStatus',
                [], [],
                '''                Active, Inactive, or Unused
                ''',
                'status',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            ],
            'Cisco-IOS-XR-policy-repository-oper',
            'reference',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-policy-repository-oper'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper',
            is_config=False,
        ),
    },
    'RoutingPolicy.Sets.Mac.Sets_.Set.UsedBy' : {
        'meta_info' : _MetaInfoClass('RoutingPolicy.Sets.Mac.Sets_.Set.UsedBy', REFERENCE_CLASS,
            '''Policies that use this object, directly or
indirectly''',
            False, 
            [
            _MetaInfoClassMember('reference', REFERENCE_LIST, 'Reference', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper', 'RoutingPolicy.Sets.Mac.Sets_.Set.UsedBy.Reference',
                [], [],
                '''                Information about policies referring to this
                object
                ''',
                'reference',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            ],
            'Cisco-IOS-XR-policy-repository-oper',
            'used-by',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-policy-repository-oper'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper',
            is_config=False,
        ),
    },
    'RoutingPolicy.Sets.Mac.Sets_.Set.Attached.Binding' : {
        'meta_info' : _MetaInfoClass('RoutingPolicy.Sets.Mac.Sets_.Set.Attached.Binding', REFERENCE_LIST,
            '''bindings list''',
            False, 
            [
            _MetaInfoClassMember('protocol', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                Protocol to which policy attached
                ''',
                'protocol',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('vrf-name', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                VRF name
                ''',
                'vrf_name',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('proto-instance', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                Protocol instance
                ''',
                'proto_instance',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('af-name', REFERENCE_ENUM_CLASS, 'AddressFamily', 'Address-family',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper', 'AddressFamily',
                [], [],
                '''                Address Family Identifier
                ''',
                'af_name',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('saf-name', REFERENCE_ENUM_CLASS, 'SubAddressFamily', 'Sub-address-family',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper', 'SubAddressFamily',
                [], [],
                '''                Subsequent Address Family Identifier
                ''',
                'saf_name',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('neighbor-address', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                Neighbor IP Address
                ''',
                'neighbor_address',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('neighbor-af-name', REFERENCE_ENUM_CLASS, 'AddressFamily', 'Address-family',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper', 'AddressFamily',
                [], [],
                '''                Neighbor IP Address Family
                ''',
                'neighbor_af_name',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('group-name', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                Neighbor Group Name
                ''',
                'group_name',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('direction', REFERENCE_ENUM_CLASS, 'AttachPointDirection', 'Attach-point-direction',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper', 'AttachPointDirection',
                [], [],
                '''                Direction In or Out
                ''',
                'direction',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('group', REFERENCE_ENUM_CLASS, 'Group', 'Group',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper', 'Group',
                [], [],
                '''                Neighbor Group 
                ''',
                'group',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('source-protocol', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                Source Protocol to redistribute, Source Protocol
                can be one of the following values{all,
                connected, local, static, bgp, rip, isis, ospf
                ,ospfv3, eigrp, unknown }
                ''',
                'source_protocol',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('aggregate-network-address', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                Aggregate IP address or Network IP Address in
                IPv4 or IPv6 Format
                ''',
                'aggregate_network_address',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('interface-name', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                Interface Name
                ''',
                'interface_name',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('instance', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                Instance
                ''',
                'instance',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('area-id', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                OSPF Area ID in Decimal Integer Format
                ''',
                'area_id',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('propogate-from', ATTRIBUTE, 'int', 'int32',
                None, None,
                [('-2147483648', '2147483647')], [],
                '''                ISIS Propogate From Level
                ''',
                'propogate_from',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('propogate-to', ATTRIBUTE, 'int', 'int32',
                None, None,
                [('-2147483648', '2147483647')], [],
                '''                ISIS Propogate To Level
                ''',
                'propogate_to',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('route-policy-name', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                Policy that uses object in question
                ''',
                'route_policy_name',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('attached-policy', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                The attached policy that (maybe indirectly) uses
                the object in question
                ''',
                'attached_policy',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('attach-point', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                Name of attach point where policy is attached
                ''',
                'attach_point',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            ],
            'Cisco-IOS-XR-policy-repository-oper',
            'binding',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-policy-repository-oper'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper',
            is_config=False,
        ),
    },
    'RoutingPolicy.Sets.Mac.Sets_.Set.Attached' : {
        'meta_info' : _MetaInfoClass('RoutingPolicy.Sets.Mac.Sets_.Set.Attached', REFERENCE_CLASS,
            '''Information about where this policy or set is
attached''',
            False, 
            [
            _MetaInfoClassMember('binding', REFERENCE_LIST, 'Binding', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper', 'RoutingPolicy.Sets.Mac.Sets_.Set.Attached.Binding',
                [], [],
                '''                bindings list
                ''',
                'binding',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            ],
            'Cisco-IOS-XR-policy-repository-oper',
            'attached',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-policy-repository-oper'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper',
            is_config=False,
        ),
    },
    'RoutingPolicy.Sets.Mac.Sets_.Set' : {
        'meta_info' : _MetaInfoClass('RoutingPolicy.Sets.Mac.Sets_.Set', REFERENCE_LIST,
            '''Information about an individual set''',
            False, 
            [
            _MetaInfoClassMember('set-name', ATTRIBUTE, 'str', 'xr:Cisco-ios-xr-string',
                None, None,
                [], [b'[\\w\\-\\.:,_@#%$\\+=\\|;]+'],
                '''                Set name
                ''',
                'set_name',
                'Cisco-IOS-XR-policy-repository-oper', True, is_config=False),
            _MetaInfoClassMember('used-by', REFERENCE_CLASS, 'UsedBy', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper', 'RoutingPolicy.Sets.Mac.Sets_.Set.UsedBy',
                [], [],
                '''                Policies that use this object, directly or
                indirectly
                ''',
                'used_by',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('attached', REFERENCE_CLASS, 'Attached', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper', 'RoutingPolicy.Sets.Mac.Sets_.Set.Attached',
                [], [],
                '''                Information about where this policy or set is
                attached
                ''',
                'attached',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            ],
            'Cisco-IOS-XR-policy-repository-oper',
            'set',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-policy-repository-oper'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper',
            is_config=False,
        ),
    },
    'RoutingPolicy.Sets.Mac.Sets_' : {
        'meta_info' : _MetaInfoClass('RoutingPolicy.Sets.Mac.Sets_', REFERENCE_CLASS,
            '''Information about individual sets''',
            False, 
            [
            _MetaInfoClassMember('set', REFERENCE_LIST, 'Set', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper', 'RoutingPolicy.Sets.Mac.Sets_.Set',
                [], [],
                '''                Information about an individual set
                ''',
                'set',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            ],
            'Cisco-IOS-XR-policy-repository-oper',
            'sets',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-policy-repository-oper'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper',
            is_config=False,
        ),
    },
    'RoutingPolicy.Sets.Mac.Unused' : {
        'meta_info' : _MetaInfoClass('RoutingPolicy.Sets.Mac.Unused', REFERENCE_CLASS,
            '''All objects of a given type that are not
referenced at all''',
            False, 
            [
            _MetaInfoClassMember('object', REFERENCE_LEAFLIST, 'str', 'String',
                None, None,
                [], [],
                '''                Policy objects
                ''',
                'object',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            ],
            'Cisco-IOS-XR-policy-repository-oper',
            'unused',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-policy-repository-oper'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper',
            is_config=False,
        ),
    },
    'RoutingPolicy.Sets.Mac.Inactive' : {
        'meta_info' : _MetaInfoClass('RoutingPolicy.Sets.Mac.Inactive', REFERENCE_CLASS,
            '''All objects of a given type that are not
attached to a protocol''',
            False, 
            [
            _MetaInfoClassMember('object', REFERENCE_LEAFLIST, 'str', 'String',
                None, None,
                [], [],
                '''                Policy objects
                ''',
                'object',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            ],
            'Cisco-IOS-XR-policy-repository-oper',
            'inactive',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-policy-repository-oper'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper',
            is_config=False,
        ),
    },
    'RoutingPolicy.Sets.Mac.Active' : {
        'meta_info' : _MetaInfoClass('RoutingPolicy.Sets.Mac.Active', REFERENCE_CLASS,
            '''All objects of a given type that are attached to
a protocol''',
            False, 
            [
            _MetaInfoClassMember('object', REFERENCE_LEAFLIST, 'str', 'String',
                None, None,
                [], [],
                '''                Policy objects
                ''',
                'object',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            ],
            'Cisco-IOS-XR-policy-repository-oper',
            'active',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-policy-repository-oper'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper',
            is_config=False,
        ),
    },
    'RoutingPolicy.Sets.Mac' : {
        'meta_info' : _MetaInfoClass('RoutingPolicy.Sets.Mac', REFERENCE_CLASS,
            '''Information about Mac sets''',
            False, 
            [
            _MetaInfoClassMember('sets', REFERENCE_CLASS, 'Sets_', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper', 'RoutingPolicy.Sets.Mac.Sets_',
                [], [],
                '''                Information about individual sets
                ''',
                'sets',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('unused', REFERENCE_CLASS, 'Unused', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper', 'RoutingPolicy.Sets.Mac.Unused',
                [], [],
                '''                All objects of a given type that are not
                referenced at all
                ''',
                'unused',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('inactive', REFERENCE_CLASS, 'Inactive', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper', 'RoutingPolicy.Sets.Mac.Inactive',
                [], [],
                '''                All objects of a given type that are not
                attached to a protocol
                ''',
                'inactive',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('active', REFERENCE_CLASS, 'Active', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper', 'RoutingPolicy.Sets.Mac.Active',
                [], [],
                '''                All objects of a given type that are attached to
                a protocol
                ''',
                'active',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            ],
            'Cisco-IOS-XR-policy-repository-oper',
            'mac',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-policy-repository-oper'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper',
            is_config=False,
        ),
    },
    'RoutingPolicy.Sets.ExtendedCommunityCost.Sets_.Set.UsedBy.Reference' : {
        'meta_info' : _MetaInfoClass('RoutingPolicy.Sets.ExtendedCommunityCost.Sets_.Set.UsedBy.Reference', REFERENCE_LIST,
            '''Information about policies referring to this
object''',
            False, 
            [
            _MetaInfoClassMember('route-policy-name', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                Name of policy
                ''',
                'route_policy_name',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('used-directly', ATTRIBUTE, 'bool', 'boolean',
                None, None,
                [], [],
                '''                Whether the policy uses this object directly or
                indirectly
                ''',
                'used_directly',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('status', REFERENCE_ENUM_CLASS, 'ObjectStatus', 'Object-status',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper', 'ObjectStatus',
                [], [],
                '''                Active, Inactive, or Unused
                ''',
                'status',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            ],
            'Cisco-IOS-XR-policy-repository-oper',
            'reference',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-policy-repository-oper'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper',
            is_config=False,
        ),
    },
    'RoutingPolicy.Sets.ExtendedCommunityCost.Sets_.Set.UsedBy' : {
        'meta_info' : _MetaInfoClass('RoutingPolicy.Sets.ExtendedCommunityCost.Sets_.Set.UsedBy', REFERENCE_CLASS,
            '''Policies that use this object, directly or
indirectly''',
            False, 
            [
            _MetaInfoClassMember('reference', REFERENCE_LIST, 'Reference', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper', 'RoutingPolicy.Sets.ExtendedCommunityCost.Sets_.Set.UsedBy.Reference',
                [], [],
                '''                Information about policies referring to this
                object
                ''',
                'reference',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            ],
            'Cisco-IOS-XR-policy-repository-oper',
            'used-by',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-policy-repository-oper'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper',
            is_config=False,
        ),
    },
    'RoutingPolicy.Sets.ExtendedCommunityCost.Sets_.Set.Attached.Binding' : {
        'meta_info' : _MetaInfoClass('RoutingPolicy.Sets.ExtendedCommunityCost.Sets_.Set.Attached.Binding', REFERENCE_LIST,
            '''bindings list''',
            False, 
            [
            _MetaInfoClassMember('protocol', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                Protocol to which policy attached
                ''',
                'protocol',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('vrf-name', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                VRF name
                ''',
                'vrf_name',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('proto-instance', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                Protocol instance
                ''',
                'proto_instance',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('af-name', REFERENCE_ENUM_CLASS, 'AddressFamily', 'Address-family',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper', 'AddressFamily',
                [], [],
                '''                Address Family Identifier
                ''',
                'af_name',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('saf-name', REFERENCE_ENUM_CLASS, 'SubAddressFamily', 'Sub-address-family',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper', 'SubAddressFamily',
                [], [],
                '''                Subsequent Address Family Identifier
                ''',
                'saf_name',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('neighbor-address', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                Neighbor IP Address
                ''',
                'neighbor_address',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('neighbor-af-name', REFERENCE_ENUM_CLASS, 'AddressFamily', 'Address-family',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper', 'AddressFamily',
                [], [],
                '''                Neighbor IP Address Family
                ''',
                'neighbor_af_name',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('group-name', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                Neighbor Group Name
                ''',
                'group_name',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('direction', REFERENCE_ENUM_CLASS, 'AttachPointDirection', 'Attach-point-direction',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper', 'AttachPointDirection',
                [], [],
                '''                Direction In or Out
                ''',
                'direction',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('group', REFERENCE_ENUM_CLASS, 'Group', 'Group',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper', 'Group',
                [], [],
                '''                Neighbor Group 
                ''',
                'group',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('source-protocol', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                Source Protocol to redistribute, Source Protocol
                can be one of the following values{all,
                connected, local, static, bgp, rip, isis, ospf
                ,ospfv3, eigrp, unknown }
                ''',
                'source_protocol',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('aggregate-network-address', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                Aggregate IP address or Network IP Address in
                IPv4 or IPv6 Format
                ''',
                'aggregate_network_address',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('interface-name', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                Interface Name
                ''',
                'interface_name',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('instance', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                Instance
                ''',
                'instance',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('area-id', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                OSPF Area ID in Decimal Integer Format
                ''',
                'area_id',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('propogate-from', ATTRIBUTE, 'int', 'int32',
                None, None,
                [('-2147483648', '2147483647')], [],
                '''                ISIS Propogate From Level
                ''',
                'propogate_from',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('propogate-to', ATTRIBUTE, 'int', 'int32',
                None, None,
                [('-2147483648', '2147483647')], [],
                '''                ISIS Propogate To Level
                ''',
                'propogate_to',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('route-policy-name', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                Policy that uses object in question
                ''',
                'route_policy_name',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('attached-policy', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                The attached policy that (maybe indirectly) uses
                the object in question
                ''',
                'attached_policy',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('attach-point', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                Name of attach point where policy is attached
                ''',
                'attach_point',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            ],
            'Cisco-IOS-XR-policy-repository-oper',
            'binding',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-policy-repository-oper'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper',
            is_config=False,
        ),
    },
    'RoutingPolicy.Sets.ExtendedCommunityCost.Sets_.Set.Attached' : {
        'meta_info' : _MetaInfoClass('RoutingPolicy.Sets.ExtendedCommunityCost.Sets_.Set.Attached', REFERENCE_CLASS,
            '''Information about where this policy or set is
attached''',
            False, 
            [
            _MetaInfoClassMember('binding', REFERENCE_LIST, 'Binding', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper', 'RoutingPolicy.Sets.ExtendedCommunityCost.Sets_.Set.Attached.Binding',
                [], [],
                '''                bindings list
                ''',
                'binding',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            ],
            'Cisco-IOS-XR-policy-repository-oper',
            'attached',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-policy-repository-oper'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper',
            is_config=False,
        ),
    },
    'RoutingPolicy.Sets.ExtendedCommunityCost.Sets_.Set' : {
        'meta_info' : _MetaInfoClass('RoutingPolicy.Sets.ExtendedCommunityCost.Sets_.Set', REFERENCE_LIST,
            '''Information about an individual set''',
            False, 
            [
            _MetaInfoClassMember('set-name', ATTRIBUTE, 'str', 'xr:Cisco-ios-xr-string',
                None, None,
                [], [b'[\\w\\-\\.:,_@#%$\\+=\\|;]+'],
                '''                Set name
                ''',
                'set_name',
                'Cisco-IOS-XR-policy-repository-oper', True, is_config=False),
            _MetaInfoClassMember('used-by', REFERENCE_CLASS, 'UsedBy', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper', 'RoutingPolicy.Sets.ExtendedCommunityCost.Sets_.Set.UsedBy',
                [], [],
                '''                Policies that use this object, directly or
                indirectly
                ''',
                'used_by',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('attached', REFERENCE_CLASS, 'Attached', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper', 'RoutingPolicy.Sets.ExtendedCommunityCost.Sets_.Set.Attached',
                [], [],
                '''                Information about where this policy or set is
                attached
                ''',
                'attached',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            ],
            'Cisco-IOS-XR-policy-repository-oper',
            'set',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-policy-repository-oper'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper',
            is_config=False,
        ),
    },
    'RoutingPolicy.Sets.ExtendedCommunityCost.Sets_' : {
        'meta_info' : _MetaInfoClass('RoutingPolicy.Sets.ExtendedCommunityCost.Sets_', REFERENCE_CLASS,
            '''Information about individual sets''',
            False, 
            [
            _MetaInfoClassMember('set', REFERENCE_LIST, 'Set', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper', 'RoutingPolicy.Sets.ExtendedCommunityCost.Sets_.Set',
                [], [],
                '''                Information about an individual set
                ''',
                'set',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            ],
            'Cisco-IOS-XR-policy-repository-oper',
            'sets',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-policy-repository-oper'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper',
            is_config=False,
        ),
    },
    'RoutingPolicy.Sets.ExtendedCommunityCost.Unused' : {
        'meta_info' : _MetaInfoClass('RoutingPolicy.Sets.ExtendedCommunityCost.Unused', REFERENCE_CLASS,
            '''All objects of a given type that are not
referenced at all''',
            False, 
            [
            _MetaInfoClassMember('object', REFERENCE_LEAFLIST, 'str', 'String',
                None, None,
                [], [],
                '''                Policy objects
                ''',
                'object',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            ],
            'Cisco-IOS-XR-policy-repository-oper',
            'unused',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-policy-repository-oper'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper',
            is_config=False,
        ),
    },
    'RoutingPolicy.Sets.ExtendedCommunityCost.Inactive' : {
        'meta_info' : _MetaInfoClass('RoutingPolicy.Sets.ExtendedCommunityCost.Inactive', REFERENCE_CLASS,
            '''All objects of a given type that are not
attached to a protocol''',
            False, 
            [
            _MetaInfoClassMember('object', REFERENCE_LEAFLIST, 'str', 'String',
                None, None,
                [], [],
                '''                Policy objects
                ''',
                'object',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            ],
            'Cisco-IOS-XR-policy-repository-oper',
            'inactive',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-policy-repository-oper'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper',
            is_config=False,
        ),
    },
    'RoutingPolicy.Sets.ExtendedCommunityCost.Active' : {
        'meta_info' : _MetaInfoClass('RoutingPolicy.Sets.ExtendedCommunityCost.Active', REFERENCE_CLASS,
            '''All objects of a given type that are attached to
a protocol''',
            False, 
            [
            _MetaInfoClassMember('object', REFERENCE_LEAFLIST, 'str', 'String',
                None, None,
                [], [],
                '''                Policy objects
                ''',
                'object',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            ],
            'Cisco-IOS-XR-policy-repository-oper',
            'active',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-policy-repository-oper'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper',
            is_config=False,
        ),
    },
    'RoutingPolicy.Sets.ExtendedCommunityCost' : {
        'meta_info' : _MetaInfoClass('RoutingPolicy.Sets.ExtendedCommunityCost', REFERENCE_CLASS,
            '''Information about Extended Community Cost sets''',
            False, 
            [
            _MetaInfoClassMember('sets', REFERENCE_CLASS, 'Sets_', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper', 'RoutingPolicy.Sets.ExtendedCommunityCost.Sets_',
                [], [],
                '''                Information about individual sets
                ''',
                'sets',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('unused', REFERENCE_CLASS, 'Unused', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper', 'RoutingPolicy.Sets.ExtendedCommunityCost.Unused',
                [], [],
                '''                All objects of a given type that are not
                referenced at all
                ''',
                'unused',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('inactive', REFERENCE_CLASS, 'Inactive', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper', 'RoutingPolicy.Sets.ExtendedCommunityCost.Inactive',
                [], [],
                '''                All objects of a given type that are not
                attached to a protocol
                ''',
                'inactive',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('active', REFERENCE_CLASS, 'Active', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper', 'RoutingPolicy.Sets.ExtendedCommunityCost.Active',
                [], [],
                '''                All objects of a given type that are attached to
                a protocol
                ''',
                'active',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            ],
            'Cisco-IOS-XR-policy-repository-oper',
            'extended-community-cost',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-policy-repository-oper'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper',
            is_config=False,
        ),
    },
    'RoutingPolicy.Sets' : {
        'meta_info' : _MetaInfoClass('RoutingPolicy.Sets', REFERENCE_CLASS,
            '''Information about configured sets''',
            False, 
            [
            _MetaInfoClassMember('etag', REFERENCE_CLASS, 'Etag', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper', 'RoutingPolicy.Sets.Etag',
                [], [],
                '''                Information about Etag sets
                ''',
                'etag',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('ospf-area', REFERENCE_CLASS, 'OspfArea', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper', 'RoutingPolicy.Sets.OspfArea',
                [], [],
                '''                Information about OSPF Area sets
                ''',
                'ospf_area',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('extended-community-opaque', REFERENCE_CLASS, 'ExtendedCommunityOpaque', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper', 'RoutingPolicy.Sets.ExtendedCommunityOpaque',
                [], [],
                '''                Information about Extended Community Opaque
                sets
                ''',
                'extended_community_opaque',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('extended-community-seg-nh', REFERENCE_CLASS, 'ExtendedCommunitySegNh', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper', 'RoutingPolicy.Sets.ExtendedCommunitySegNh',
                [], [],
                '''                Information about Extended Community SegNH sets
                ''',
                'extended_community_seg_nh',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('extended-community-soo', REFERENCE_CLASS, 'ExtendedCommunitySoo', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper', 'RoutingPolicy.Sets.ExtendedCommunitySoo',
                [], [],
                '''                Information about Extended Community SOO sets
                ''',
                'extended_community_soo',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('tag', REFERENCE_CLASS, 'Tag', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper', 'RoutingPolicy.Sets.Tag',
                [], [],
                '''                Information about Tag sets
                ''',
                'tag',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('prefix', REFERENCE_CLASS, 'Prefix', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper', 'RoutingPolicy.Sets.Prefix',
                [], [],
                '''                Information about AS Path sets
                ''',
                'prefix',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('community', REFERENCE_CLASS, 'Community', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper', 'RoutingPolicy.Sets.Community',
                [], [],
                '''                Information about Community sets
                ''',
                'community',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('as-path', REFERENCE_CLASS, 'AsPath', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper', 'RoutingPolicy.Sets.AsPath',
                [], [],
                '''                Information about AS Path sets
                ''',
                'as_path',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('large-community', REFERENCE_CLASS, 'LargeCommunity', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper', 'RoutingPolicy.Sets.LargeCommunity',
                [], [],
                '''                Information about Large Community sets
                ''',
                'large_community',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('esi', REFERENCE_CLASS, 'Esi', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper', 'RoutingPolicy.Sets.Esi',
                [], [],
                '''                Information about Esi sets
                ''',
                'esi',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('extended-community-bandwidth', REFERENCE_CLASS, 'ExtendedCommunityBandwidth', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper', 'RoutingPolicy.Sets.ExtendedCommunityBandwidth',
                [], [],
                '''                Information about Extended Community Bandwidth
                sets
                ''',
                'extended_community_bandwidth',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('extended-community-rt', REFERENCE_CLASS, 'ExtendedCommunityRt', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper', 'RoutingPolicy.Sets.ExtendedCommunityRt',
                [], [],
                '''                Information about Extended Community RT sets
                ''',
                'extended_community_rt',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('rd', REFERENCE_CLASS, 'Rd', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper', 'RoutingPolicy.Sets.Rd',
                [], [],
                '''                Information about RD sets
                ''',
                'rd',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('mac', REFERENCE_CLASS, 'Mac', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper', 'RoutingPolicy.Sets.Mac',
                [], [],
                '''                Information about Mac sets
                ''',
                'mac',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('extended-community-cost', REFERENCE_CLASS, 'ExtendedCommunityCost', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper', 'RoutingPolicy.Sets.ExtendedCommunityCost',
                [], [],
                '''                Information about Extended Community Cost sets
                ''',
                'extended_community_cost',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            ],
            'Cisco-IOS-XR-policy-repository-oper',
            'sets',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-policy-repository-oper'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper',
            is_config=False,
        ),
    },
    'RoutingPolicy' : {
        'meta_info' : _MetaInfoClass('RoutingPolicy', REFERENCE_CLASS,
            '''Routing policy operational data''',
            False, 
            [
            _MetaInfoClassMember('limits', REFERENCE_CLASS, 'Limits', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper', 'RoutingPolicy.Limits',
                [], [],
                '''                Information about configured limits and the
                current values
                ''',
                'limits',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('policies', REFERENCE_CLASS, 'Policies', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper', 'RoutingPolicy.Policies',
                [], [],
                '''                Information about configured route policies
                ''',
                'policies',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('sets', REFERENCE_CLASS, 'Sets', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper', 'RoutingPolicy.Sets',
                [], [],
                '''                Information about configured sets
                ''',
                'sets',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            ],
            'Cisco-IOS-XR-policy-repository-oper',
            'routing-policy',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-policy-repository-oper'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper',
            is_config=False,
        ),
    },
    'RoutingPolicyShadow.Limits' : {
        'meta_info' : _MetaInfoClass('RoutingPolicyShadow.Limits', REFERENCE_CLASS,
            '''Information about configured limits and the
current values''',
            False, 
            [
            _MetaInfoClassMember('maximum-lines-of-policy', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('0', '4294967295')], [],
                '''                Maximum lines of configuration allowable for all
                policies and sets
                ''',
                'maximum_lines_of_policy',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('current-lines-of-policy-limit', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('0', '4294967295')], [],
                '''                Number of lines of configuration for
                policies/sets currently allowed
                ''',
                'current_lines_of_policy_limit',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('current-lines-of-policy-used', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('0', '4294967295')], [],
                '''                Current number of lines configured for all
                policies and sets
                ''',
                'current_lines_of_policy_used',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('maximum-number-of-policies', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('0', '4294967295')], [],
                '''                Maximum number of policies allowable
                ''',
                'maximum_number_of_policies',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('current-number-of-policies-limit', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('0', '4294967295')], [],
                '''                Number of policies currently allowed
                ''',
                'current_number_of_policies_limit',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('current-number-of-policies-used', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('0', '4294967295')], [],
                '''                Current number of policies configured
                ''',
                'current_number_of_policies_used',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('compiled-policies-length', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('0', '4294967295')], [],
                '''                The total compiled length of all policies
                ''',
                'compiled_policies_length',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            ],
            'Cisco-IOS-XR-policy-repository-oper',
            'limits',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-policy-repository-oper'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper',
            is_config=False,
        ),
    },
    'RoutingPolicyShadow.Policies.RoutePolicies.RoutePolicy.PolicyUses.DirectlyUsedPolicies' : {
        'meta_info' : _MetaInfoClass('RoutingPolicyShadow.Policies.RoutePolicies.RoutePolicy.PolicyUses.DirectlyUsedPolicies', REFERENCE_CLASS,
            '''Policies that this policy uses directly''',
            False, 
            [
            _MetaInfoClassMember('object', REFERENCE_LEAFLIST, 'str', 'String',
                None, None,
                [], [],
                '''                Policy objects
                ''',
                'object',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            ],
            'Cisco-IOS-XR-policy-repository-oper',
            'directly-used-policies',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-policy-repository-oper'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper',
            is_config=False,
        ),
    },
    'RoutingPolicyShadow.Policies.RoutePolicies.RoutePolicy.PolicyUses.AllUsedSets.Sets' : {
        'meta_info' : _MetaInfoClass('RoutingPolicyShadow.Policies.RoutePolicies.RoutePolicy.PolicyUses.AllUsedSets.Sets', REFERENCE_LIST,
            '''List of sets in several domains''',
            False, 
            [
            _MetaInfoClassMember('set-domain', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                Domain of sets
                ''',
                'set_domain',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('set-name', REFERENCE_LEAFLIST, 'str', 'String',
                None, None,
                [], [],
                '''                Names of sets in this domain
                ''',
                'set_name',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            ],
            'Cisco-IOS-XR-policy-repository-oper',
            'sets',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-policy-repository-oper'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper',
            is_config=False,
        ),
    },
    'RoutingPolicyShadow.Policies.RoutePolicies.RoutePolicy.PolicyUses.AllUsedSets' : {
        'meta_info' : _MetaInfoClass('RoutingPolicyShadow.Policies.RoutePolicies.RoutePolicy.PolicyUses.AllUsedSets', REFERENCE_CLASS,
            '''Sets used by this policy, or by policies
that it uses''',
            False, 
            [
            _MetaInfoClassMember('sets', REFERENCE_LIST, 'Sets', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper', 'RoutingPolicyShadow.Policies.RoutePolicies.RoutePolicy.PolicyUses.AllUsedSets.Sets',
                [], [],
                '''                List of sets in several domains
                ''',
                'sets',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            ],
            'Cisco-IOS-XR-policy-repository-oper',
            'all-used-sets',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-policy-repository-oper'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper',
            is_config=False,
        ),
    },
    'RoutingPolicyShadow.Policies.RoutePolicies.RoutePolicy.PolicyUses.DirectlyUsedSets.Sets' : {
        'meta_info' : _MetaInfoClass('RoutingPolicyShadow.Policies.RoutePolicies.RoutePolicy.PolicyUses.DirectlyUsedSets.Sets', REFERENCE_LIST,
            '''List of sets in several domains''',
            False, 
            [
            _MetaInfoClassMember('set-domain', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                Domain of sets
                ''',
                'set_domain',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('set-name', REFERENCE_LEAFLIST, 'str', 'String',
                None, None,
                [], [],
                '''                Names of sets in this domain
                ''',
                'set_name',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            ],
            'Cisco-IOS-XR-policy-repository-oper',
            'sets',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-policy-repository-oper'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper',
            is_config=False,
        ),
    },
    'RoutingPolicyShadow.Policies.RoutePolicies.RoutePolicy.PolicyUses.DirectlyUsedSets' : {
        'meta_info' : _MetaInfoClass('RoutingPolicyShadow.Policies.RoutePolicies.RoutePolicy.PolicyUses.DirectlyUsedSets', REFERENCE_CLASS,
            '''Sets that this policy uses directly''',
            False, 
            [
            _MetaInfoClassMember('sets', REFERENCE_LIST, 'Sets', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper', 'RoutingPolicyShadow.Policies.RoutePolicies.RoutePolicy.PolicyUses.DirectlyUsedSets.Sets',
                [], [],
                '''                List of sets in several domains
                ''',
                'sets',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            ],
            'Cisco-IOS-XR-policy-repository-oper',
            'directly-used-sets',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-policy-repository-oper'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper',
            is_config=False,
        ),
    },
    'RoutingPolicyShadow.Policies.RoutePolicies.RoutePolicy.PolicyUses.AllUsedPolicies' : {
        'meta_info' : _MetaInfoClass('RoutingPolicyShadow.Policies.RoutePolicies.RoutePolicy.PolicyUses.AllUsedPolicies', REFERENCE_CLASS,
            '''Policies used by this policy, or by policies
that it uses''',
            False, 
            [
            _MetaInfoClassMember('object', REFERENCE_LEAFLIST, 'str', 'String',
                None, None,
                [], [],
                '''                Policy objects
                ''',
                'object',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            ],
            'Cisco-IOS-XR-policy-repository-oper',
            'all-used-policies',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-policy-repository-oper'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper',
            is_config=False,
        ),
    },
    'RoutingPolicyShadow.Policies.RoutePolicies.RoutePolicy.PolicyUses' : {
        'meta_info' : _MetaInfoClass('RoutingPolicyShadow.Policies.RoutePolicies.RoutePolicy.PolicyUses', REFERENCE_CLASS,
            '''Information about which policies and sets
this policy uses''',
            False, 
            [
            _MetaInfoClassMember('directly-used-policies', REFERENCE_CLASS, 'DirectlyUsedPolicies', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper', 'RoutingPolicyShadow.Policies.RoutePolicies.RoutePolicy.PolicyUses.DirectlyUsedPolicies',
                [], [],
                '''                Policies that this policy uses directly
                ''',
                'directly_used_policies',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('all-used-sets', REFERENCE_CLASS, 'AllUsedSets', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper', 'RoutingPolicyShadow.Policies.RoutePolicies.RoutePolicy.PolicyUses.AllUsedSets',
                [], [],
                '''                Sets used by this policy, or by policies
                that it uses
                ''',
                'all_used_sets',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('directly-used-sets', REFERENCE_CLASS, 'DirectlyUsedSets', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper', 'RoutingPolicyShadow.Policies.RoutePolicies.RoutePolicy.PolicyUses.DirectlyUsedSets',
                [], [],
                '''                Sets that this policy uses directly
                ''',
                'directly_used_sets',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('all-used-policies', REFERENCE_CLASS, 'AllUsedPolicies', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper', 'RoutingPolicyShadow.Policies.RoutePolicies.RoutePolicy.PolicyUses.AllUsedPolicies',
                [], [],
                '''                Policies used by this policy, or by policies
                that it uses
                ''',
                'all_used_policies',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            ],
            'Cisco-IOS-XR-policy-repository-oper',
            'policy-uses',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-policy-repository-oper'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper',
            is_config=False,
        ),
    },
    'RoutingPolicyShadow.Policies.RoutePolicies.RoutePolicy.UsedBy.Reference' : {
        'meta_info' : _MetaInfoClass('RoutingPolicyShadow.Policies.RoutePolicies.RoutePolicy.UsedBy.Reference', REFERENCE_LIST,
            '''Information about policies referring to this
object''',
            False, 
            [
            _MetaInfoClassMember('route-policy-name', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                Name of policy
                ''',
                'route_policy_name',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('used-directly', ATTRIBUTE, 'bool', 'boolean',
                None, None,
                [], [],
                '''                Whether the policy uses this object directly or
                indirectly
                ''',
                'used_directly',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('status', REFERENCE_ENUM_CLASS, 'ObjectStatus', 'Object-status',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper', 'ObjectStatus',
                [], [],
                '''                Active, Inactive, or Unused
                ''',
                'status',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            ],
            'Cisco-IOS-XR-policy-repository-oper',
            'reference',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-policy-repository-oper'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper',
            is_config=False,
        ),
    },
    'RoutingPolicyShadow.Policies.RoutePolicies.RoutePolicy.UsedBy' : {
        'meta_info' : _MetaInfoClass('RoutingPolicyShadow.Policies.RoutePolicies.RoutePolicy.UsedBy', REFERENCE_CLASS,
            '''Policies that use this object, directly or
indirectly''',
            False, 
            [
            _MetaInfoClassMember('reference', REFERENCE_LIST, 'Reference', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper', 'RoutingPolicyShadow.Policies.RoutePolicies.RoutePolicy.UsedBy.Reference',
                [], [],
                '''                Information about policies referring to this
                object
                ''',
                'reference',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            ],
            'Cisco-IOS-XR-policy-repository-oper',
            'used-by',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-policy-repository-oper'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper',
            is_config=False,
        ),
    },
    'RoutingPolicyShadow.Policies.RoutePolicies.RoutePolicy.Attached.Binding' : {
        'meta_info' : _MetaInfoClass('RoutingPolicyShadow.Policies.RoutePolicies.RoutePolicy.Attached.Binding', REFERENCE_LIST,
            '''bindings list''',
            False, 
            [
            _MetaInfoClassMember('protocol', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                Protocol to which policy attached
                ''',
                'protocol',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('vrf-name', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                VRF name
                ''',
                'vrf_name',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('proto-instance', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                Protocol instance
                ''',
                'proto_instance',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('af-name', REFERENCE_ENUM_CLASS, 'AddressFamily', 'Address-family',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper', 'AddressFamily',
                [], [],
                '''                Address Family Identifier
                ''',
                'af_name',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('saf-name', REFERENCE_ENUM_CLASS, 'SubAddressFamily', 'Sub-address-family',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper', 'SubAddressFamily',
                [], [],
                '''                Subsequent Address Family Identifier
                ''',
                'saf_name',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('neighbor-address', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                Neighbor IP Address
                ''',
                'neighbor_address',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('neighbor-af-name', REFERENCE_ENUM_CLASS, 'AddressFamily', 'Address-family',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper', 'AddressFamily',
                [], [],
                '''                Neighbor IP Address Family
                ''',
                'neighbor_af_name',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('group-name', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                Neighbor Group Name
                ''',
                'group_name',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('direction', REFERENCE_ENUM_CLASS, 'AttachPointDirection', 'Attach-point-direction',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper', 'AttachPointDirection',
                [], [],
                '''                Direction In or Out
                ''',
                'direction',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('group', REFERENCE_ENUM_CLASS, 'Group', 'Group',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper', 'Group',
                [], [],
                '''                Neighbor Group 
                ''',
                'group',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('source-protocol', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                Source Protocol to redistribute, Source Protocol
                can be one of the following values{all,
                connected, local, static, bgp, rip, isis, ospf
                ,ospfv3, eigrp, unknown }
                ''',
                'source_protocol',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('aggregate-network-address', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                Aggregate IP address or Network IP Address in
                IPv4 or IPv6 Format
                ''',
                'aggregate_network_address',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('interface-name', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                Interface Name
                ''',
                'interface_name',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('instance', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                Instance
                ''',
                'instance',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('area-id', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                OSPF Area ID in Decimal Integer Format
                ''',
                'area_id',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('propogate-from', ATTRIBUTE, 'int', 'int32',
                None, None,
                [('-2147483648', '2147483647')], [],
                '''                ISIS Propogate From Level
                ''',
                'propogate_from',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('propogate-to', ATTRIBUTE, 'int', 'int32',
                None, None,
                [('-2147483648', '2147483647')], [],
                '''                ISIS Propogate To Level
                ''',
                'propogate_to',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('route-policy-name', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                Policy that uses object in question
                ''',
                'route_policy_name',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('attached-policy', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                The attached policy that (maybe indirectly) uses
                the object in question
                ''',
                'attached_policy',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('attach-point', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                Name of attach point where policy is attached
                ''',
                'attach_point',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            ],
            'Cisco-IOS-XR-policy-repository-oper',
            'binding',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-policy-repository-oper'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper',
            is_config=False,
        ),
    },
    'RoutingPolicyShadow.Policies.RoutePolicies.RoutePolicy.Attached' : {
        'meta_info' : _MetaInfoClass('RoutingPolicyShadow.Policies.RoutePolicies.RoutePolicy.Attached', REFERENCE_CLASS,
            '''Information about where this policy or set is
attached''',
            False, 
            [
            _MetaInfoClassMember('binding', REFERENCE_LIST, 'Binding', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper', 'RoutingPolicyShadow.Policies.RoutePolicies.RoutePolicy.Attached.Binding',
                [], [],
                '''                bindings list
                ''',
                'binding',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            ],
            'Cisco-IOS-XR-policy-repository-oper',
            'attached',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-policy-repository-oper'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper',
            is_config=False,
        ),
    },
    'RoutingPolicyShadow.Policies.RoutePolicies.RoutePolicy' : {
        'meta_info' : _MetaInfoClass('RoutingPolicyShadow.Policies.RoutePolicies.RoutePolicy', REFERENCE_LIST,
            '''Information about an individual policy''',
            False, 
            [
            _MetaInfoClassMember('route-policy-name', ATTRIBUTE, 'str', 'xr:Cisco-ios-xr-string',
                None, None,
                [], [b'[\\w\\-\\.:,_@#%$\\+=\\|;]+'],
                '''                Route policy name
                ''',
                'route_policy_name',
                'Cisco-IOS-XR-policy-repository-oper', True, is_config=False),
            _MetaInfoClassMember('policy-uses', REFERENCE_CLASS, 'PolicyUses', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper', 'RoutingPolicyShadow.Policies.RoutePolicies.RoutePolicy.PolicyUses',
                [], [],
                '''                Information about which policies and sets
                this policy uses
                ''',
                'policy_uses',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('used-by', REFERENCE_CLASS, 'UsedBy', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper', 'RoutingPolicyShadow.Policies.RoutePolicies.RoutePolicy.UsedBy',
                [], [],
                '''                Policies that use this object, directly or
                indirectly
                ''',
                'used_by',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('attached', REFERENCE_CLASS, 'Attached', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper', 'RoutingPolicyShadow.Policies.RoutePolicies.RoutePolicy.Attached',
                [], [],
                '''                Information about where this policy or set is
                attached
                ''',
                'attached',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            ],
            'Cisco-IOS-XR-policy-repository-oper',
            'route-policy',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-policy-repository-oper'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper',
            is_config=False,
        ),
    },
    'RoutingPolicyShadow.Policies.RoutePolicies' : {
        'meta_info' : _MetaInfoClass('RoutingPolicyShadow.Policies.RoutePolicies', REFERENCE_CLASS,
            '''Information about individual policies''',
            False, 
            [
            _MetaInfoClassMember('route-policy', REFERENCE_LIST, 'RoutePolicy', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper', 'RoutingPolicyShadow.Policies.RoutePolicies.RoutePolicy',
                [], [],
                '''                Information about an individual policy
                ''',
                'route_policy',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            ],
            'Cisco-IOS-XR-policy-repository-oper',
            'route-policies',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-policy-repository-oper'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper',
            is_config=False,
        ),
    },
    'RoutingPolicyShadow.Policies.Unused' : {
        'meta_info' : _MetaInfoClass('RoutingPolicyShadow.Policies.Unused', REFERENCE_CLASS,
            '''All objects of a given type that are not
referenced at all''',
            False, 
            [
            _MetaInfoClassMember('object', REFERENCE_LEAFLIST, 'str', 'String',
                None, None,
                [], [],
                '''                Policy objects
                ''',
                'object',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            ],
            'Cisco-IOS-XR-policy-repository-oper',
            'unused',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-policy-repository-oper'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper',
            is_config=False,
        ),
    },
    'RoutingPolicyShadow.Policies.Inactive' : {
        'meta_info' : _MetaInfoClass('RoutingPolicyShadow.Policies.Inactive', REFERENCE_CLASS,
            '''All objects of a given type that are not
attached to a protocol''',
            False, 
            [
            _MetaInfoClassMember('object', REFERENCE_LEAFLIST, 'str', 'String',
                None, None,
                [], [],
                '''                Policy objects
                ''',
                'object',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            ],
            'Cisco-IOS-XR-policy-repository-oper',
            'inactive',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-policy-repository-oper'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper',
            is_config=False,
        ),
    },
    'RoutingPolicyShadow.Policies.Active' : {
        'meta_info' : _MetaInfoClass('RoutingPolicyShadow.Policies.Active', REFERENCE_CLASS,
            '''All objects of a given type that are attached to
a protocol''',
            False, 
            [
            _MetaInfoClassMember('object', REFERENCE_LEAFLIST, 'str', 'String',
                None, None,
                [], [],
                '''                Policy objects
                ''',
                'object',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            ],
            'Cisco-IOS-XR-policy-repository-oper',
            'active',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-policy-repository-oper'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper',
            is_config=False,
        ),
    },
    'RoutingPolicyShadow.Policies' : {
        'meta_info' : _MetaInfoClass('RoutingPolicyShadow.Policies', REFERENCE_CLASS,
            '''Information about configured route policies''',
            False, 
            [
            _MetaInfoClassMember('route-policies', REFERENCE_CLASS, 'RoutePolicies', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper', 'RoutingPolicyShadow.Policies.RoutePolicies',
                [], [],
                '''                Information about individual policies
                ''',
                'route_policies',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('unused', REFERENCE_CLASS, 'Unused', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper', 'RoutingPolicyShadow.Policies.Unused',
                [], [],
                '''                All objects of a given type that are not
                referenced at all
                ''',
                'unused',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('inactive', REFERENCE_CLASS, 'Inactive', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper', 'RoutingPolicyShadow.Policies.Inactive',
                [], [],
                '''                All objects of a given type that are not
                attached to a protocol
                ''',
                'inactive',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('active', REFERENCE_CLASS, 'Active', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper', 'RoutingPolicyShadow.Policies.Active',
                [], [],
                '''                All objects of a given type that are attached to
                a protocol
                ''',
                'active',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            ],
            'Cisco-IOS-XR-policy-repository-oper',
            'policies',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-policy-repository-oper'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper',
            is_config=False,
        ),
    },
    'RoutingPolicyShadow.Sets.Etag.Sets_.Set.UsedBy.Reference' : {
        'meta_info' : _MetaInfoClass('RoutingPolicyShadow.Sets.Etag.Sets_.Set.UsedBy.Reference', REFERENCE_LIST,
            '''Information about policies referring to this
object''',
            False, 
            [
            _MetaInfoClassMember('route-policy-name', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                Name of policy
                ''',
                'route_policy_name',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('used-directly', ATTRIBUTE, 'bool', 'boolean',
                None, None,
                [], [],
                '''                Whether the policy uses this object directly or
                indirectly
                ''',
                'used_directly',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('status', REFERENCE_ENUM_CLASS, 'ObjectStatus', 'Object-status',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper', 'ObjectStatus',
                [], [],
                '''                Active, Inactive, or Unused
                ''',
                'status',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            ],
            'Cisco-IOS-XR-policy-repository-oper',
            'reference',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-policy-repository-oper'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper',
            is_config=False,
        ),
    },
    'RoutingPolicyShadow.Sets.Etag.Sets_.Set.UsedBy' : {
        'meta_info' : _MetaInfoClass('RoutingPolicyShadow.Sets.Etag.Sets_.Set.UsedBy', REFERENCE_CLASS,
            '''Policies that use this object, directly or
indirectly''',
            False, 
            [
            _MetaInfoClassMember('reference', REFERENCE_LIST, 'Reference', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper', 'RoutingPolicyShadow.Sets.Etag.Sets_.Set.UsedBy.Reference',
                [], [],
                '''                Information about policies referring to this
                object
                ''',
                'reference',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            ],
            'Cisco-IOS-XR-policy-repository-oper',
            'used-by',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-policy-repository-oper'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper',
            is_config=False,
        ),
    },
    'RoutingPolicyShadow.Sets.Etag.Sets_.Set.Attached.Binding' : {
        'meta_info' : _MetaInfoClass('RoutingPolicyShadow.Sets.Etag.Sets_.Set.Attached.Binding', REFERENCE_LIST,
            '''bindings list''',
            False, 
            [
            _MetaInfoClassMember('protocol', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                Protocol to which policy attached
                ''',
                'protocol',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('vrf-name', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                VRF name
                ''',
                'vrf_name',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('proto-instance', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                Protocol instance
                ''',
                'proto_instance',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('af-name', REFERENCE_ENUM_CLASS, 'AddressFamily', 'Address-family',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper', 'AddressFamily',
                [], [],
                '''                Address Family Identifier
                ''',
                'af_name',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('saf-name', REFERENCE_ENUM_CLASS, 'SubAddressFamily', 'Sub-address-family',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper', 'SubAddressFamily',
                [], [],
                '''                Subsequent Address Family Identifier
                ''',
                'saf_name',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('neighbor-address', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                Neighbor IP Address
                ''',
                'neighbor_address',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('neighbor-af-name', REFERENCE_ENUM_CLASS, 'AddressFamily', 'Address-family',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper', 'AddressFamily',
                [], [],
                '''                Neighbor IP Address Family
                ''',
                'neighbor_af_name',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('group-name', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                Neighbor Group Name
                ''',
                'group_name',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('direction', REFERENCE_ENUM_CLASS, 'AttachPointDirection', 'Attach-point-direction',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper', 'AttachPointDirection',
                [], [],
                '''                Direction In or Out
                ''',
                'direction',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('group', REFERENCE_ENUM_CLASS, 'Group', 'Group',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper', 'Group',
                [], [],
                '''                Neighbor Group 
                ''',
                'group',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('source-protocol', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                Source Protocol to redistribute, Source Protocol
                can be one of the following values{all,
                connected, local, static, bgp, rip, isis, ospf
                ,ospfv3, eigrp, unknown }
                ''',
                'source_protocol',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('aggregate-network-address', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                Aggregate IP address or Network IP Address in
                IPv4 or IPv6 Format
                ''',
                'aggregate_network_address',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('interface-name', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                Interface Name
                ''',
                'interface_name',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('instance', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                Instance
                ''',
                'instance',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('area-id', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                OSPF Area ID in Decimal Integer Format
                ''',
                'area_id',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('propogate-from', ATTRIBUTE, 'int', 'int32',
                None, None,
                [('-2147483648', '2147483647')], [],
                '''                ISIS Propogate From Level
                ''',
                'propogate_from',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('propogate-to', ATTRIBUTE, 'int', 'int32',
                None, None,
                [('-2147483648', '2147483647')], [],
                '''                ISIS Propogate To Level
                ''',
                'propogate_to',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('route-policy-name', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                Policy that uses object in question
                ''',
                'route_policy_name',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('attached-policy', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                The attached policy that (maybe indirectly) uses
                the object in question
                ''',
                'attached_policy',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('attach-point', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                Name of attach point where policy is attached
                ''',
                'attach_point',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            ],
            'Cisco-IOS-XR-policy-repository-oper',
            'binding',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-policy-repository-oper'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper',
            is_config=False,
        ),
    },
    'RoutingPolicyShadow.Sets.Etag.Sets_.Set.Attached' : {
        'meta_info' : _MetaInfoClass('RoutingPolicyShadow.Sets.Etag.Sets_.Set.Attached', REFERENCE_CLASS,
            '''Information about where this policy or set is
attached''',
            False, 
            [
            _MetaInfoClassMember('binding', REFERENCE_LIST, 'Binding', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper', 'RoutingPolicyShadow.Sets.Etag.Sets_.Set.Attached.Binding',
                [], [],
                '''                bindings list
                ''',
                'binding',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            ],
            'Cisco-IOS-XR-policy-repository-oper',
            'attached',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-policy-repository-oper'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper',
            is_config=False,
        ),
    },
    'RoutingPolicyShadow.Sets.Etag.Sets_.Set' : {
        'meta_info' : _MetaInfoClass('RoutingPolicyShadow.Sets.Etag.Sets_.Set', REFERENCE_LIST,
            '''Information about an individual set''',
            False, 
            [
            _MetaInfoClassMember('set-name', ATTRIBUTE, 'str', 'xr:Cisco-ios-xr-string',
                None, None,
                [], [b'[\\w\\-\\.:,_@#%$\\+=\\|;]+'],
                '''                Set name
                ''',
                'set_name',
                'Cisco-IOS-XR-policy-repository-oper', True, is_config=False),
            _MetaInfoClassMember('used-by', REFERENCE_CLASS, 'UsedBy', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper', 'RoutingPolicyShadow.Sets.Etag.Sets_.Set.UsedBy',
                [], [],
                '''                Policies that use this object, directly or
                indirectly
                ''',
                'used_by',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('attached', REFERENCE_CLASS, 'Attached', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper', 'RoutingPolicyShadow.Sets.Etag.Sets_.Set.Attached',
                [], [],
                '''                Information about where this policy or set is
                attached
                ''',
                'attached',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            ],
            'Cisco-IOS-XR-policy-repository-oper',
            'set',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-policy-repository-oper'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper',
            is_config=False,
        ),
    },
    'RoutingPolicyShadow.Sets.Etag.Sets_' : {
        'meta_info' : _MetaInfoClass('RoutingPolicyShadow.Sets.Etag.Sets_', REFERENCE_CLASS,
            '''Information about individual sets''',
            False, 
            [
            _MetaInfoClassMember('set', REFERENCE_LIST, 'Set', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper', 'RoutingPolicyShadow.Sets.Etag.Sets_.Set',
                [], [],
                '''                Information about an individual set
                ''',
                'set',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            ],
            'Cisco-IOS-XR-policy-repository-oper',
            'sets',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-policy-repository-oper'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper',
            is_config=False,
        ),
    },
    'RoutingPolicyShadow.Sets.Etag.Unused' : {
        'meta_info' : _MetaInfoClass('RoutingPolicyShadow.Sets.Etag.Unused', REFERENCE_CLASS,
            '''All objects of a given type that are not
referenced at all''',
            False, 
            [
            _MetaInfoClassMember('object', REFERENCE_LEAFLIST, 'str', 'String',
                None, None,
                [], [],
                '''                Policy objects
                ''',
                'object',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            ],
            'Cisco-IOS-XR-policy-repository-oper',
            'unused',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-policy-repository-oper'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper',
            is_config=False,
        ),
    },
    'RoutingPolicyShadow.Sets.Etag.Inactive' : {
        'meta_info' : _MetaInfoClass('RoutingPolicyShadow.Sets.Etag.Inactive', REFERENCE_CLASS,
            '''All objects of a given type that are not
attached to a protocol''',
            False, 
            [
            _MetaInfoClassMember('object', REFERENCE_LEAFLIST, 'str', 'String',
                None, None,
                [], [],
                '''                Policy objects
                ''',
                'object',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            ],
            'Cisco-IOS-XR-policy-repository-oper',
            'inactive',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-policy-repository-oper'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper',
            is_config=False,
        ),
    },
    'RoutingPolicyShadow.Sets.Etag.Active' : {
        'meta_info' : _MetaInfoClass('RoutingPolicyShadow.Sets.Etag.Active', REFERENCE_CLASS,
            '''All objects of a given type that are attached to
a protocol''',
            False, 
            [
            _MetaInfoClassMember('object', REFERENCE_LEAFLIST, 'str', 'String',
                None, None,
                [], [],
                '''                Policy objects
                ''',
                'object',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            ],
            'Cisco-IOS-XR-policy-repository-oper',
            'active',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-policy-repository-oper'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper',
            is_config=False,
        ),
    },
    'RoutingPolicyShadow.Sets.Etag' : {
        'meta_info' : _MetaInfoClass('RoutingPolicyShadow.Sets.Etag', REFERENCE_CLASS,
            '''Information about Etag sets''',
            False, 
            [
            _MetaInfoClassMember('sets', REFERENCE_CLASS, 'Sets_', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper', 'RoutingPolicyShadow.Sets.Etag.Sets_',
                [], [],
                '''                Information about individual sets
                ''',
                'sets',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('unused', REFERENCE_CLASS, 'Unused', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper', 'RoutingPolicyShadow.Sets.Etag.Unused',
                [], [],
                '''                All objects of a given type that are not
                referenced at all
                ''',
                'unused',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('inactive', REFERENCE_CLASS, 'Inactive', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper', 'RoutingPolicyShadow.Sets.Etag.Inactive',
                [], [],
                '''                All objects of a given type that are not
                attached to a protocol
                ''',
                'inactive',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('active', REFERENCE_CLASS, 'Active', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper', 'RoutingPolicyShadow.Sets.Etag.Active',
                [], [],
                '''                All objects of a given type that are attached to
                a protocol
                ''',
                'active',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            ],
            'Cisco-IOS-XR-policy-repository-oper',
            'etag',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-policy-repository-oper'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper',
            is_config=False,
        ),
    },
    'RoutingPolicyShadow.Sets.OspfArea.Sets_.Set.UsedBy.Reference' : {
        'meta_info' : _MetaInfoClass('RoutingPolicyShadow.Sets.OspfArea.Sets_.Set.UsedBy.Reference', REFERENCE_LIST,
            '''Information about policies referring to this
object''',
            False, 
            [
            _MetaInfoClassMember('route-policy-name', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                Name of policy
                ''',
                'route_policy_name',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('used-directly', ATTRIBUTE, 'bool', 'boolean',
                None, None,
                [], [],
                '''                Whether the policy uses this object directly or
                indirectly
                ''',
                'used_directly',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('status', REFERENCE_ENUM_CLASS, 'ObjectStatus', 'Object-status',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper', 'ObjectStatus',
                [], [],
                '''                Active, Inactive, or Unused
                ''',
                'status',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            ],
            'Cisco-IOS-XR-policy-repository-oper',
            'reference',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-policy-repository-oper'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper',
            is_config=False,
        ),
    },
    'RoutingPolicyShadow.Sets.OspfArea.Sets_.Set.UsedBy' : {
        'meta_info' : _MetaInfoClass('RoutingPolicyShadow.Sets.OspfArea.Sets_.Set.UsedBy', REFERENCE_CLASS,
            '''Policies that use this object, directly or
indirectly''',
            False, 
            [
            _MetaInfoClassMember('reference', REFERENCE_LIST, 'Reference', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper', 'RoutingPolicyShadow.Sets.OspfArea.Sets_.Set.UsedBy.Reference',
                [], [],
                '''                Information about policies referring to this
                object
                ''',
                'reference',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            ],
            'Cisco-IOS-XR-policy-repository-oper',
            'used-by',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-policy-repository-oper'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper',
            is_config=False,
        ),
    },
    'RoutingPolicyShadow.Sets.OspfArea.Sets_.Set.Attached.Binding' : {
        'meta_info' : _MetaInfoClass('RoutingPolicyShadow.Sets.OspfArea.Sets_.Set.Attached.Binding', REFERENCE_LIST,
            '''bindings list''',
            False, 
            [
            _MetaInfoClassMember('protocol', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                Protocol to which policy attached
                ''',
                'protocol',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('vrf-name', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                VRF name
                ''',
                'vrf_name',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('proto-instance', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                Protocol instance
                ''',
                'proto_instance',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('af-name', REFERENCE_ENUM_CLASS, 'AddressFamily', 'Address-family',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper', 'AddressFamily',
                [], [],
                '''                Address Family Identifier
                ''',
                'af_name',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('saf-name', REFERENCE_ENUM_CLASS, 'SubAddressFamily', 'Sub-address-family',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper', 'SubAddressFamily',
                [], [],
                '''                Subsequent Address Family Identifier
                ''',
                'saf_name',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('neighbor-address', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                Neighbor IP Address
                ''',
                'neighbor_address',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('neighbor-af-name', REFERENCE_ENUM_CLASS, 'AddressFamily', 'Address-family',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper', 'AddressFamily',
                [], [],
                '''                Neighbor IP Address Family
                ''',
                'neighbor_af_name',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('group-name', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                Neighbor Group Name
                ''',
                'group_name',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('direction', REFERENCE_ENUM_CLASS, 'AttachPointDirection', 'Attach-point-direction',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper', 'AttachPointDirection',
                [], [],
                '''                Direction In or Out
                ''',
                'direction',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('group', REFERENCE_ENUM_CLASS, 'Group', 'Group',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper', 'Group',
                [], [],
                '''                Neighbor Group 
                ''',
                'group',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('source-protocol', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                Source Protocol to redistribute, Source Protocol
                can be one of the following values{all,
                connected, local, static, bgp, rip, isis, ospf
                ,ospfv3, eigrp, unknown }
                ''',
                'source_protocol',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('aggregate-network-address', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                Aggregate IP address or Network IP Address in
                IPv4 or IPv6 Format
                ''',
                'aggregate_network_address',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('interface-name', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                Interface Name
                ''',
                'interface_name',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('instance', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                Instance
                ''',
                'instance',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('area-id', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                OSPF Area ID in Decimal Integer Format
                ''',
                'area_id',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('propogate-from', ATTRIBUTE, 'int', 'int32',
                None, None,
                [('-2147483648', '2147483647')], [],
                '''                ISIS Propogate From Level
                ''',
                'propogate_from',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('propogate-to', ATTRIBUTE, 'int', 'int32',
                None, None,
                [('-2147483648', '2147483647')], [],
                '''                ISIS Propogate To Level
                ''',
                'propogate_to',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('route-policy-name', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                Policy that uses object in question
                ''',
                'route_policy_name',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('attached-policy', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                The attached policy that (maybe indirectly) uses
                the object in question
                ''',
                'attached_policy',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('attach-point', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                Name of attach point where policy is attached
                ''',
                'attach_point',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            ],
            'Cisco-IOS-XR-policy-repository-oper',
            'binding',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-policy-repository-oper'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper',
            is_config=False,
        ),
    },
    'RoutingPolicyShadow.Sets.OspfArea.Sets_.Set.Attached' : {
        'meta_info' : _MetaInfoClass('RoutingPolicyShadow.Sets.OspfArea.Sets_.Set.Attached', REFERENCE_CLASS,
            '''Information about where this policy or set is
attached''',
            False, 
            [
            _MetaInfoClassMember('binding', REFERENCE_LIST, 'Binding', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper', 'RoutingPolicyShadow.Sets.OspfArea.Sets_.Set.Attached.Binding',
                [], [],
                '''                bindings list
                ''',
                'binding',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            ],
            'Cisco-IOS-XR-policy-repository-oper',
            'attached',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-policy-repository-oper'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper',
            is_config=False,
        ),
    },
    'RoutingPolicyShadow.Sets.OspfArea.Sets_.Set' : {
        'meta_info' : _MetaInfoClass('RoutingPolicyShadow.Sets.OspfArea.Sets_.Set', REFERENCE_LIST,
            '''Information about an individual set''',
            False, 
            [
            _MetaInfoClassMember('set-name', ATTRIBUTE, 'str', 'xr:Cisco-ios-xr-string',
                None, None,
                [], [b'[\\w\\-\\.:,_@#%$\\+=\\|;]+'],
                '''                Set name
                ''',
                'set_name',
                'Cisco-IOS-XR-policy-repository-oper', True, is_config=False),
            _MetaInfoClassMember('used-by', REFERENCE_CLASS, 'UsedBy', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper', 'RoutingPolicyShadow.Sets.OspfArea.Sets_.Set.UsedBy',
                [], [],
                '''                Policies that use this object, directly or
                indirectly
                ''',
                'used_by',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('attached', REFERENCE_CLASS, 'Attached', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper', 'RoutingPolicyShadow.Sets.OspfArea.Sets_.Set.Attached',
                [], [],
                '''                Information about where this policy or set is
                attached
                ''',
                'attached',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            ],
            'Cisco-IOS-XR-policy-repository-oper',
            'set',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-policy-repository-oper'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper',
            is_config=False,
        ),
    },
    'RoutingPolicyShadow.Sets.OspfArea.Sets_' : {
        'meta_info' : _MetaInfoClass('RoutingPolicyShadow.Sets.OspfArea.Sets_', REFERENCE_CLASS,
            '''Information about individual sets''',
            False, 
            [
            _MetaInfoClassMember('set', REFERENCE_LIST, 'Set', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper', 'RoutingPolicyShadow.Sets.OspfArea.Sets_.Set',
                [], [],
                '''                Information about an individual set
                ''',
                'set',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            ],
            'Cisco-IOS-XR-policy-repository-oper',
            'sets',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-policy-repository-oper'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper',
            is_config=False,
        ),
    },
    'RoutingPolicyShadow.Sets.OspfArea.Unused' : {
        'meta_info' : _MetaInfoClass('RoutingPolicyShadow.Sets.OspfArea.Unused', REFERENCE_CLASS,
            '''All objects of a given type that are not
referenced at all''',
            False, 
            [
            _MetaInfoClassMember('object', REFERENCE_LEAFLIST, 'str', 'String',
                None, None,
                [], [],
                '''                Policy objects
                ''',
                'object',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            ],
            'Cisco-IOS-XR-policy-repository-oper',
            'unused',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-policy-repository-oper'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper',
            is_config=False,
        ),
    },
    'RoutingPolicyShadow.Sets.OspfArea.Inactive' : {
        'meta_info' : _MetaInfoClass('RoutingPolicyShadow.Sets.OspfArea.Inactive', REFERENCE_CLASS,
            '''All objects of a given type that are not
attached to a protocol''',
            False, 
            [
            _MetaInfoClassMember('object', REFERENCE_LEAFLIST, 'str', 'String',
                None, None,
                [], [],
                '''                Policy objects
                ''',
                'object',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            ],
            'Cisco-IOS-XR-policy-repository-oper',
            'inactive',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-policy-repository-oper'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper',
            is_config=False,
        ),
    },
    'RoutingPolicyShadow.Sets.OspfArea.Active' : {
        'meta_info' : _MetaInfoClass('RoutingPolicyShadow.Sets.OspfArea.Active', REFERENCE_CLASS,
            '''All objects of a given type that are attached to
a protocol''',
            False, 
            [
            _MetaInfoClassMember('object', REFERENCE_LEAFLIST, 'str', 'String',
                None, None,
                [], [],
                '''                Policy objects
                ''',
                'object',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            ],
            'Cisco-IOS-XR-policy-repository-oper',
            'active',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-policy-repository-oper'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper',
            is_config=False,
        ),
    },
    'RoutingPolicyShadow.Sets.OspfArea' : {
        'meta_info' : _MetaInfoClass('RoutingPolicyShadow.Sets.OspfArea', REFERENCE_CLASS,
            '''Information about OSPF Area sets''',
            False, 
            [
            _MetaInfoClassMember('sets', REFERENCE_CLASS, 'Sets_', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper', 'RoutingPolicyShadow.Sets.OspfArea.Sets_',
                [], [],
                '''                Information about individual sets
                ''',
                'sets',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('unused', REFERENCE_CLASS, 'Unused', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper', 'RoutingPolicyShadow.Sets.OspfArea.Unused',
                [], [],
                '''                All objects of a given type that are not
                referenced at all
                ''',
                'unused',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('inactive', REFERENCE_CLASS, 'Inactive', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper', 'RoutingPolicyShadow.Sets.OspfArea.Inactive',
                [], [],
                '''                All objects of a given type that are not
                attached to a protocol
                ''',
                'inactive',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('active', REFERENCE_CLASS, 'Active', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper', 'RoutingPolicyShadow.Sets.OspfArea.Active',
                [], [],
                '''                All objects of a given type that are attached to
                a protocol
                ''',
                'active',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            ],
            'Cisco-IOS-XR-policy-repository-oper',
            'ospf-area',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-policy-repository-oper'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper',
            is_config=False,
        ),
    },
    'RoutingPolicyShadow.Sets.ExtendedCommunityOpaque.Sets_.Set.UsedBy.Reference' : {
        'meta_info' : _MetaInfoClass('RoutingPolicyShadow.Sets.ExtendedCommunityOpaque.Sets_.Set.UsedBy.Reference', REFERENCE_LIST,
            '''Information about policies referring to this
object''',
            False, 
            [
            _MetaInfoClassMember('route-policy-name', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                Name of policy
                ''',
                'route_policy_name',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('used-directly', ATTRIBUTE, 'bool', 'boolean',
                None, None,
                [], [],
                '''                Whether the policy uses this object directly or
                indirectly
                ''',
                'used_directly',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('status', REFERENCE_ENUM_CLASS, 'ObjectStatus', 'Object-status',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper', 'ObjectStatus',
                [], [],
                '''                Active, Inactive, or Unused
                ''',
                'status',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            ],
            'Cisco-IOS-XR-policy-repository-oper',
            'reference',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-policy-repository-oper'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper',
            is_config=False,
        ),
    },
    'RoutingPolicyShadow.Sets.ExtendedCommunityOpaque.Sets_.Set.UsedBy' : {
        'meta_info' : _MetaInfoClass('RoutingPolicyShadow.Sets.ExtendedCommunityOpaque.Sets_.Set.UsedBy', REFERENCE_CLASS,
            '''Policies that use this object, directly or
indirectly''',
            False, 
            [
            _MetaInfoClassMember('reference', REFERENCE_LIST, 'Reference', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper', 'RoutingPolicyShadow.Sets.ExtendedCommunityOpaque.Sets_.Set.UsedBy.Reference',
                [], [],
                '''                Information about policies referring to this
                object
                ''',
                'reference',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            ],
            'Cisco-IOS-XR-policy-repository-oper',
            'used-by',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-policy-repository-oper'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper',
            is_config=False,
        ),
    },
    'RoutingPolicyShadow.Sets.ExtendedCommunityOpaque.Sets_.Set.Attached.Binding' : {
        'meta_info' : _MetaInfoClass('RoutingPolicyShadow.Sets.ExtendedCommunityOpaque.Sets_.Set.Attached.Binding', REFERENCE_LIST,
            '''bindings list''',
            False, 
            [
            _MetaInfoClassMember('protocol', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                Protocol to which policy attached
                ''',
                'protocol',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('vrf-name', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                VRF name
                ''',
                'vrf_name',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('proto-instance', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                Protocol instance
                ''',
                'proto_instance',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('af-name', REFERENCE_ENUM_CLASS, 'AddressFamily', 'Address-family',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper', 'AddressFamily',
                [], [],
                '''                Address Family Identifier
                ''',
                'af_name',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('saf-name', REFERENCE_ENUM_CLASS, 'SubAddressFamily', 'Sub-address-family',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper', 'SubAddressFamily',
                [], [],
                '''                Subsequent Address Family Identifier
                ''',
                'saf_name',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('neighbor-address', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                Neighbor IP Address
                ''',
                'neighbor_address',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('neighbor-af-name', REFERENCE_ENUM_CLASS, 'AddressFamily', 'Address-family',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper', 'AddressFamily',
                [], [],
                '''                Neighbor IP Address Family
                ''',
                'neighbor_af_name',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('group-name', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                Neighbor Group Name
                ''',
                'group_name',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('direction', REFERENCE_ENUM_CLASS, 'AttachPointDirection', 'Attach-point-direction',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper', 'AttachPointDirection',
                [], [],
                '''                Direction In or Out
                ''',
                'direction',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('group', REFERENCE_ENUM_CLASS, 'Group', 'Group',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper', 'Group',
                [], [],
                '''                Neighbor Group 
                ''',
                'group',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('source-protocol', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                Source Protocol to redistribute, Source Protocol
                can be one of the following values{all,
                connected, local, static, bgp, rip, isis, ospf
                ,ospfv3, eigrp, unknown }
                ''',
                'source_protocol',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('aggregate-network-address', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                Aggregate IP address or Network IP Address in
                IPv4 or IPv6 Format
                ''',
                'aggregate_network_address',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('interface-name', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                Interface Name
                ''',
                'interface_name',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('instance', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                Instance
                ''',
                'instance',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('area-id', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                OSPF Area ID in Decimal Integer Format
                ''',
                'area_id',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('propogate-from', ATTRIBUTE, 'int', 'int32',
                None, None,
                [('-2147483648', '2147483647')], [],
                '''                ISIS Propogate From Level
                ''',
                'propogate_from',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('propogate-to', ATTRIBUTE, 'int', 'int32',
                None, None,
                [('-2147483648', '2147483647')], [],
                '''                ISIS Propogate To Level
                ''',
                'propogate_to',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('route-policy-name', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                Policy that uses object in question
                ''',
                'route_policy_name',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('attached-policy', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                The attached policy that (maybe indirectly) uses
                the object in question
                ''',
                'attached_policy',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('attach-point', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                Name of attach point where policy is attached
                ''',
                'attach_point',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            ],
            'Cisco-IOS-XR-policy-repository-oper',
            'binding',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-policy-repository-oper'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper',
            is_config=False,
        ),
    },
    'RoutingPolicyShadow.Sets.ExtendedCommunityOpaque.Sets_.Set.Attached' : {
        'meta_info' : _MetaInfoClass('RoutingPolicyShadow.Sets.ExtendedCommunityOpaque.Sets_.Set.Attached', REFERENCE_CLASS,
            '''Information about where this policy or set is
attached''',
            False, 
            [
            _MetaInfoClassMember('binding', REFERENCE_LIST, 'Binding', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper', 'RoutingPolicyShadow.Sets.ExtendedCommunityOpaque.Sets_.Set.Attached.Binding',
                [], [],
                '''                bindings list
                ''',
                'binding',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            ],
            'Cisco-IOS-XR-policy-repository-oper',
            'attached',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-policy-repository-oper'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper',
            is_config=False,
        ),
    },
    'RoutingPolicyShadow.Sets.ExtendedCommunityOpaque.Sets_.Set' : {
        'meta_info' : _MetaInfoClass('RoutingPolicyShadow.Sets.ExtendedCommunityOpaque.Sets_.Set', REFERENCE_LIST,
            '''Information about an individual set''',
            False, 
            [
            _MetaInfoClassMember('set-name', ATTRIBUTE, 'str', 'xr:Cisco-ios-xr-string',
                None, None,
                [], [b'[\\w\\-\\.:,_@#%$\\+=\\|;]+'],
                '''                Set name
                ''',
                'set_name',
                'Cisco-IOS-XR-policy-repository-oper', True, is_config=False),
            _MetaInfoClassMember('used-by', REFERENCE_CLASS, 'UsedBy', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper', 'RoutingPolicyShadow.Sets.ExtendedCommunityOpaque.Sets_.Set.UsedBy',
                [], [],
                '''                Policies that use this object, directly or
                indirectly
                ''',
                'used_by',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('attached', REFERENCE_CLASS, 'Attached', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper', 'RoutingPolicyShadow.Sets.ExtendedCommunityOpaque.Sets_.Set.Attached',
                [], [],
                '''                Information about where this policy or set is
                attached
                ''',
                'attached',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            ],
            'Cisco-IOS-XR-policy-repository-oper',
            'set',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-policy-repository-oper'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper',
            is_config=False,
        ),
    },
    'RoutingPolicyShadow.Sets.ExtendedCommunityOpaque.Sets_' : {
        'meta_info' : _MetaInfoClass('RoutingPolicyShadow.Sets.ExtendedCommunityOpaque.Sets_', REFERENCE_CLASS,
            '''Information about individual sets''',
            False, 
            [
            _MetaInfoClassMember('set', REFERENCE_LIST, 'Set', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper', 'RoutingPolicyShadow.Sets.ExtendedCommunityOpaque.Sets_.Set',
                [], [],
                '''                Information about an individual set
                ''',
                'set',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            ],
            'Cisco-IOS-XR-policy-repository-oper',
            'sets',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-policy-repository-oper'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper',
            is_config=False,
        ),
    },
    'RoutingPolicyShadow.Sets.ExtendedCommunityOpaque.Unused' : {
        'meta_info' : _MetaInfoClass('RoutingPolicyShadow.Sets.ExtendedCommunityOpaque.Unused', REFERENCE_CLASS,
            '''All objects of a given type that are not
referenced at all''',
            False, 
            [
            _MetaInfoClassMember('object', REFERENCE_LEAFLIST, 'str', 'String',
                None, None,
                [], [],
                '''                Policy objects
                ''',
                'object',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            ],
            'Cisco-IOS-XR-policy-repository-oper',
            'unused',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-policy-repository-oper'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper',
            is_config=False,
        ),
    },
    'RoutingPolicyShadow.Sets.ExtendedCommunityOpaque.Inactive' : {
        'meta_info' : _MetaInfoClass('RoutingPolicyShadow.Sets.ExtendedCommunityOpaque.Inactive', REFERENCE_CLASS,
            '''All objects of a given type that are not
attached to a protocol''',
            False, 
            [
            _MetaInfoClassMember('object', REFERENCE_LEAFLIST, 'str', 'String',
                None, None,
                [], [],
                '''                Policy objects
                ''',
                'object',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            ],
            'Cisco-IOS-XR-policy-repository-oper',
            'inactive',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-policy-repository-oper'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper',
            is_config=False,
        ),
    },
    'RoutingPolicyShadow.Sets.ExtendedCommunityOpaque.Active' : {
        'meta_info' : _MetaInfoClass('RoutingPolicyShadow.Sets.ExtendedCommunityOpaque.Active', REFERENCE_CLASS,
            '''All objects of a given type that are attached to
a protocol''',
            False, 
            [
            _MetaInfoClassMember('object', REFERENCE_LEAFLIST, 'str', 'String',
                None, None,
                [], [],
                '''                Policy objects
                ''',
                'object',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            ],
            'Cisco-IOS-XR-policy-repository-oper',
            'active',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-policy-repository-oper'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper',
            is_config=False,
        ),
    },
    'RoutingPolicyShadow.Sets.ExtendedCommunityOpaque' : {
        'meta_info' : _MetaInfoClass('RoutingPolicyShadow.Sets.ExtendedCommunityOpaque', REFERENCE_CLASS,
            '''Information about Extended Community Opaque
sets''',
            False, 
            [
            _MetaInfoClassMember('sets', REFERENCE_CLASS, 'Sets_', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper', 'RoutingPolicyShadow.Sets.ExtendedCommunityOpaque.Sets_',
                [], [],
                '''                Information about individual sets
                ''',
                'sets',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('unused', REFERENCE_CLASS, 'Unused', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper', 'RoutingPolicyShadow.Sets.ExtendedCommunityOpaque.Unused',
                [], [],
                '''                All objects of a given type that are not
                referenced at all
                ''',
                'unused',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('inactive', REFERENCE_CLASS, 'Inactive', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper', 'RoutingPolicyShadow.Sets.ExtendedCommunityOpaque.Inactive',
                [], [],
                '''                All objects of a given type that are not
                attached to a protocol
                ''',
                'inactive',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('active', REFERENCE_CLASS, 'Active', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper', 'RoutingPolicyShadow.Sets.ExtendedCommunityOpaque.Active',
                [], [],
                '''                All objects of a given type that are attached to
                a protocol
                ''',
                'active',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            ],
            'Cisco-IOS-XR-policy-repository-oper',
            'extended-community-opaque',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-policy-repository-oper'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper',
            is_config=False,
        ),
    },
    'RoutingPolicyShadow.Sets.ExtendedCommunitySegNh.Sets_.Set.UsedBy.Reference' : {
        'meta_info' : _MetaInfoClass('RoutingPolicyShadow.Sets.ExtendedCommunitySegNh.Sets_.Set.UsedBy.Reference', REFERENCE_LIST,
            '''Information about policies referring to this
object''',
            False, 
            [
            _MetaInfoClassMember('route-policy-name', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                Name of policy
                ''',
                'route_policy_name',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('used-directly', ATTRIBUTE, 'bool', 'boolean',
                None, None,
                [], [],
                '''                Whether the policy uses this object directly or
                indirectly
                ''',
                'used_directly',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('status', REFERENCE_ENUM_CLASS, 'ObjectStatus', 'Object-status',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper', 'ObjectStatus',
                [], [],
                '''                Active, Inactive, or Unused
                ''',
                'status',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            ],
            'Cisco-IOS-XR-policy-repository-oper',
            'reference',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-policy-repository-oper'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper',
            is_config=False,
        ),
    },
    'RoutingPolicyShadow.Sets.ExtendedCommunitySegNh.Sets_.Set.UsedBy' : {
        'meta_info' : _MetaInfoClass('RoutingPolicyShadow.Sets.ExtendedCommunitySegNh.Sets_.Set.UsedBy', REFERENCE_CLASS,
            '''Policies that use this object, directly or
indirectly''',
            False, 
            [
            _MetaInfoClassMember('reference', REFERENCE_LIST, 'Reference', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper', 'RoutingPolicyShadow.Sets.ExtendedCommunitySegNh.Sets_.Set.UsedBy.Reference',
                [], [],
                '''                Information about policies referring to this
                object
                ''',
                'reference',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            ],
            'Cisco-IOS-XR-policy-repository-oper',
            'used-by',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-policy-repository-oper'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper',
            is_config=False,
        ),
    },
    'RoutingPolicyShadow.Sets.ExtendedCommunitySegNh.Sets_.Set.Attached.Binding' : {
        'meta_info' : _MetaInfoClass('RoutingPolicyShadow.Sets.ExtendedCommunitySegNh.Sets_.Set.Attached.Binding', REFERENCE_LIST,
            '''bindings list''',
            False, 
            [
            _MetaInfoClassMember('protocol', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                Protocol to which policy attached
                ''',
                'protocol',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('vrf-name', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                VRF name
                ''',
                'vrf_name',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('proto-instance', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                Protocol instance
                ''',
                'proto_instance',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('af-name', REFERENCE_ENUM_CLASS, 'AddressFamily', 'Address-family',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper', 'AddressFamily',
                [], [],
                '''                Address Family Identifier
                ''',
                'af_name',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('saf-name', REFERENCE_ENUM_CLASS, 'SubAddressFamily', 'Sub-address-family',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper', 'SubAddressFamily',
                [], [],
                '''                Subsequent Address Family Identifier
                ''',
                'saf_name',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('neighbor-address', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                Neighbor IP Address
                ''',
                'neighbor_address',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('neighbor-af-name', REFERENCE_ENUM_CLASS, 'AddressFamily', 'Address-family',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper', 'AddressFamily',
                [], [],
                '''                Neighbor IP Address Family
                ''',
                'neighbor_af_name',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('group-name', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                Neighbor Group Name
                ''',
                'group_name',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('direction', REFERENCE_ENUM_CLASS, 'AttachPointDirection', 'Attach-point-direction',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper', 'AttachPointDirection',
                [], [],
                '''                Direction In or Out
                ''',
                'direction',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('group', REFERENCE_ENUM_CLASS, 'Group', 'Group',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper', 'Group',
                [], [],
                '''                Neighbor Group 
                ''',
                'group',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('source-protocol', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                Source Protocol to redistribute, Source Protocol
                can be one of the following values{all,
                connected, local, static, bgp, rip, isis, ospf
                ,ospfv3, eigrp, unknown }
                ''',
                'source_protocol',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('aggregate-network-address', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                Aggregate IP address or Network IP Address in
                IPv4 or IPv6 Format
                ''',
                'aggregate_network_address',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('interface-name', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                Interface Name
                ''',
                'interface_name',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('instance', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                Instance
                ''',
                'instance',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('area-id', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                OSPF Area ID in Decimal Integer Format
                ''',
                'area_id',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('propogate-from', ATTRIBUTE, 'int', 'int32',
                None, None,
                [('-2147483648', '2147483647')], [],
                '''                ISIS Propogate From Level
                ''',
                'propogate_from',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('propogate-to', ATTRIBUTE, 'int', 'int32',
                None, None,
                [('-2147483648', '2147483647')], [],
                '''                ISIS Propogate To Level
                ''',
                'propogate_to',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('route-policy-name', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                Policy that uses object in question
                ''',
                'route_policy_name',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('attached-policy', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                The attached policy that (maybe indirectly) uses
                the object in question
                ''',
                'attached_policy',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('attach-point', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                Name of attach point where policy is attached
                ''',
                'attach_point',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            ],
            'Cisco-IOS-XR-policy-repository-oper',
            'binding',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-policy-repository-oper'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper',
            is_config=False,
        ),
    },
    'RoutingPolicyShadow.Sets.ExtendedCommunitySegNh.Sets_.Set.Attached' : {
        'meta_info' : _MetaInfoClass('RoutingPolicyShadow.Sets.ExtendedCommunitySegNh.Sets_.Set.Attached', REFERENCE_CLASS,
            '''Information about where this policy or set is
attached''',
            False, 
            [
            _MetaInfoClassMember('binding', REFERENCE_LIST, 'Binding', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper', 'RoutingPolicyShadow.Sets.ExtendedCommunitySegNh.Sets_.Set.Attached.Binding',
                [], [],
                '''                bindings list
                ''',
                'binding',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            ],
            'Cisco-IOS-XR-policy-repository-oper',
            'attached',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-policy-repository-oper'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper',
            is_config=False,
        ),
    },
    'RoutingPolicyShadow.Sets.ExtendedCommunitySegNh.Sets_.Set' : {
        'meta_info' : _MetaInfoClass('RoutingPolicyShadow.Sets.ExtendedCommunitySegNh.Sets_.Set', REFERENCE_LIST,
            '''Information about an individual set''',
            False, 
            [
            _MetaInfoClassMember('set-name', ATTRIBUTE, 'str', 'xr:Cisco-ios-xr-string',
                None, None,
                [], [b'[\\w\\-\\.:,_@#%$\\+=\\|;]+'],
                '''                Set name
                ''',
                'set_name',
                'Cisco-IOS-XR-policy-repository-oper', True, is_config=False),
            _MetaInfoClassMember('used-by', REFERENCE_CLASS, 'UsedBy', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper', 'RoutingPolicyShadow.Sets.ExtendedCommunitySegNh.Sets_.Set.UsedBy',
                [], [],
                '''                Policies that use this object, directly or
                indirectly
                ''',
                'used_by',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('attached', REFERENCE_CLASS, 'Attached', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper', 'RoutingPolicyShadow.Sets.ExtendedCommunitySegNh.Sets_.Set.Attached',
                [], [],
                '''                Information about where this policy or set is
                attached
                ''',
                'attached',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            ],
            'Cisco-IOS-XR-policy-repository-oper',
            'set',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-policy-repository-oper'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper',
            is_config=False,
        ),
    },
    'RoutingPolicyShadow.Sets.ExtendedCommunitySegNh.Sets_' : {
        'meta_info' : _MetaInfoClass('RoutingPolicyShadow.Sets.ExtendedCommunitySegNh.Sets_', REFERENCE_CLASS,
            '''Information about individual sets''',
            False, 
            [
            _MetaInfoClassMember('set', REFERENCE_LIST, 'Set', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper', 'RoutingPolicyShadow.Sets.ExtendedCommunitySegNh.Sets_.Set',
                [], [],
                '''                Information about an individual set
                ''',
                'set',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            ],
            'Cisco-IOS-XR-policy-repository-oper',
            'sets',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-policy-repository-oper'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper',
            is_config=False,
        ),
    },
    'RoutingPolicyShadow.Sets.ExtendedCommunitySegNh.Unused' : {
        'meta_info' : _MetaInfoClass('RoutingPolicyShadow.Sets.ExtendedCommunitySegNh.Unused', REFERENCE_CLASS,
            '''All objects of a given type that are not
referenced at all''',
            False, 
            [
            _MetaInfoClassMember('object', REFERENCE_LEAFLIST, 'str', 'String',
                None, None,
                [], [],
                '''                Policy objects
                ''',
                'object',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            ],
            'Cisco-IOS-XR-policy-repository-oper',
            'unused',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-policy-repository-oper'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper',
            is_config=False,
        ),
    },
    'RoutingPolicyShadow.Sets.ExtendedCommunitySegNh.Inactive' : {
        'meta_info' : _MetaInfoClass('RoutingPolicyShadow.Sets.ExtendedCommunitySegNh.Inactive', REFERENCE_CLASS,
            '''All objects of a given type that are not
attached to a protocol''',
            False, 
            [
            _MetaInfoClassMember('object', REFERENCE_LEAFLIST, 'str', 'String',
                None, None,
                [], [],
                '''                Policy objects
                ''',
                'object',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            ],
            'Cisco-IOS-XR-policy-repository-oper',
            'inactive',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-policy-repository-oper'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper',
            is_config=False,
        ),
    },
    'RoutingPolicyShadow.Sets.ExtendedCommunitySegNh.Active' : {
        'meta_info' : _MetaInfoClass('RoutingPolicyShadow.Sets.ExtendedCommunitySegNh.Active', REFERENCE_CLASS,
            '''All objects of a given type that are attached to
a protocol''',
            False, 
            [
            _MetaInfoClassMember('object', REFERENCE_LEAFLIST, 'str', 'String',
                None, None,
                [], [],
                '''                Policy objects
                ''',
                'object',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            ],
            'Cisco-IOS-XR-policy-repository-oper',
            'active',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-policy-repository-oper'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper',
            is_config=False,
        ),
    },
    'RoutingPolicyShadow.Sets.ExtendedCommunitySegNh' : {
        'meta_info' : _MetaInfoClass('RoutingPolicyShadow.Sets.ExtendedCommunitySegNh', REFERENCE_CLASS,
            '''Information about Extended Community SegNH sets''',
            False, 
            [
            _MetaInfoClassMember('sets', REFERENCE_CLASS, 'Sets_', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper', 'RoutingPolicyShadow.Sets.ExtendedCommunitySegNh.Sets_',
                [], [],
                '''                Information about individual sets
                ''',
                'sets',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('unused', REFERENCE_CLASS, 'Unused', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper', 'RoutingPolicyShadow.Sets.ExtendedCommunitySegNh.Unused',
                [], [],
                '''                All objects of a given type that are not
                referenced at all
                ''',
                'unused',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('inactive', REFERENCE_CLASS, 'Inactive', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper', 'RoutingPolicyShadow.Sets.ExtendedCommunitySegNh.Inactive',
                [], [],
                '''                All objects of a given type that are not
                attached to a protocol
                ''',
                'inactive',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('active', REFERENCE_CLASS, 'Active', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper', 'RoutingPolicyShadow.Sets.ExtendedCommunitySegNh.Active',
                [], [],
                '''                All objects of a given type that are attached to
                a protocol
                ''',
                'active',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            ],
            'Cisco-IOS-XR-policy-repository-oper',
            'extended-community-seg-nh',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-policy-repository-oper'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper',
            is_config=False,
        ),
    },
    'RoutingPolicyShadow.Sets.ExtendedCommunitySoo.Sets_.Set.UsedBy.Reference' : {
        'meta_info' : _MetaInfoClass('RoutingPolicyShadow.Sets.ExtendedCommunitySoo.Sets_.Set.UsedBy.Reference', REFERENCE_LIST,
            '''Information about policies referring to this
object''',
            False, 
            [
            _MetaInfoClassMember('route-policy-name', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                Name of policy
                ''',
                'route_policy_name',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('used-directly', ATTRIBUTE, 'bool', 'boolean',
                None, None,
                [], [],
                '''                Whether the policy uses this object directly or
                indirectly
                ''',
                'used_directly',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('status', REFERENCE_ENUM_CLASS, 'ObjectStatus', 'Object-status',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper', 'ObjectStatus',
                [], [],
                '''                Active, Inactive, or Unused
                ''',
                'status',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            ],
            'Cisco-IOS-XR-policy-repository-oper',
            'reference',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-policy-repository-oper'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper',
            is_config=False,
        ),
    },
    'RoutingPolicyShadow.Sets.ExtendedCommunitySoo.Sets_.Set.UsedBy' : {
        'meta_info' : _MetaInfoClass('RoutingPolicyShadow.Sets.ExtendedCommunitySoo.Sets_.Set.UsedBy', REFERENCE_CLASS,
            '''Policies that use this object, directly or
indirectly''',
            False, 
            [
            _MetaInfoClassMember('reference', REFERENCE_LIST, 'Reference', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper', 'RoutingPolicyShadow.Sets.ExtendedCommunitySoo.Sets_.Set.UsedBy.Reference',
                [], [],
                '''                Information about policies referring to this
                object
                ''',
                'reference',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            ],
            'Cisco-IOS-XR-policy-repository-oper',
            'used-by',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-policy-repository-oper'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper',
            is_config=False,
        ),
    },
    'RoutingPolicyShadow.Sets.ExtendedCommunitySoo.Sets_.Set.Attached.Binding' : {
        'meta_info' : _MetaInfoClass('RoutingPolicyShadow.Sets.ExtendedCommunitySoo.Sets_.Set.Attached.Binding', REFERENCE_LIST,
            '''bindings list''',
            False, 
            [
            _MetaInfoClassMember('protocol', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                Protocol to which policy attached
                ''',
                'protocol',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('vrf-name', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                VRF name
                ''',
                'vrf_name',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('proto-instance', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                Protocol instance
                ''',
                'proto_instance',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('af-name', REFERENCE_ENUM_CLASS, 'AddressFamily', 'Address-family',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper', 'AddressFamily',
                [], [],
                '''                Address Family Identifier
                ''',
                'af_name',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('saf-name', REFERENCE_ENUM_CLASS, 'SubAddressFamily', 'Sub-address-family',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper', 'SubAddressFamily',
                [], [],
                '''                Subsequent Address Family Identifier
                ''',
                'saf_name',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('neighbor-address', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                Neighbor IP Address
                ''',
                'neighbor_address',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('neighbor-af-name', REFERENCE_ENUM_CLASS, 'AddressFamily', 'Address-family',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper', 'AddressFamily',
                [], [],
                '''                Neighbor IP Address Family
                ''',
                'neighbor_af_name',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('group-name', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                Neighbor Group Name
                ''',
                'group_name',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('direction', REFERENCE_ENUM_CLASS, 'AttachPointDirection', 'Attach-point-direction',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper', 'AttachPointDirection',
                [], [],
                '''                Direction In or Out
                ''',
                'direction',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('group', REFERENCE_ENUM_CLASS, 'Group', 'Group',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper', 'Group',
                [], [],
                '''                Neighbor Group 
                ''',
                'group',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('source-protocol', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                Source Protocol to redistribute, Source Protocol
                can be one of the following values{all,
                connected, local, static, bgp, rip, isis, ospf
                ,ospfv3, eigrp, unknown }
                ''',
                'source_protocol',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('aggregate-network-address', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                Aggregate IP address or Network IP Address in
                IPv4 or IPv6 Format
                ''',
                'aggregate_network_address',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('interface-name', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                Interface Name
                ''',
                'interface_name',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('instance', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                Instance
                ''',
                'instance',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('area-id', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                OSPF Area ID in Decimal Integer Format
                ''',
                'area_id',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('propogate-from', ATTRIBUTE, 'int', 'int32',
                None, None,
                [('-2147483648', '2147483647')], [],
                '''                ISIS Propogate From Level
                ''',
                'propogate_from',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('propogate-to', ATTRIBUTE, 'int', 'int32',
                None, None,
                [('-2147483648', '2147483647')], [],
                '''                ISIS Propogate To Level
                ''',
                'propogate_to',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('route-policy-name', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                Policy that uses object in question
                ''',
                'route_policy_name',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('attached-policy', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                The attached policy that (maybe indirectly) uses
                the object in question
                ''',
                'attached_policy',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('attach-point', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                Name of attach point where policy is attached
                ''',
                'attach_point',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            ],
            'Cisco-IOS-XR-policy-repository-oper',
            'binding',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-policy-repository-oper'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper',
            is_config=False,
        ),
    },
    'RoutingPolicyShadow.Sets.ExtendedCommunitySoo.Sets_.Set.Attached' : {
        'meta_info' : _MetaInfoClass('RoutingPolicyShadow.Sets.ExtendedCommunitySoo.Sets_.Set.Attached', REFERENCE_CLASS,
            '''Information about where this policy or set is
attached''',
            False, 
            [
            _MetaInfoClassMember('binding', REFERENCE_LIST, 'Binding', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper', 'RoutingPolicyShadow.Sets.ExtendedCommunitySoo.Sets_.Set.Attached.Binding',
                [], [],
                '''                bindings list
                ''',
                'binding',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            ],
            'Cisco-IOS-XR-policy-repository-oper',
            'attached',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-policy-repository-oper'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper',
            is_config=False,
        ),
    },
    'RoutingPolicyShadow.Sets.ExtendedCommunitySoo.Sets_.Set' : {
        'meta_info' : _MetaInfoClass('RoutingPolicyShadow.Sets.ExtendedCommunitySoo.Sets_.Set', REFERENCE_LIST,
            '''Information about an individual set''',
            False, 
            [
            _MetaInfoClassMember('set-name', ATTRIBUTE, 'str', 'xr:Cisco-ios-xr-string',
                None, None,
                [], [b'[\\w\\-\\.:,_@#%$\\+=\\|;]+'],
                '''                Set name
                ''',
                'set_name',
                'Cisco-IOS-XR-policy-repository-oper', True, is_config=False),
            _MetaInfoClassMember('used-by', REFERENCE_CLASS, 'UsedBy', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper', 'RoutingPolicyShadow.Sets.ExtendedCommunitySoo.Sets_.Set.UsedBy',
                [], [],
                '''                Policies that use this object, directly or
                indirectly
                ''',
                'used_by',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('attached', REFERENCE_CLASS, 'Attached', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper', 'RoutingPolicyShadow.Sets.ExtendedCommunitySoo.Sets_.Set.Attached',
                [], [],
                '''                Information about where this policy or set is
                attached
                ''',
                'attached',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            ],
            'Cisco-IOS-XR-policy-repository-oper',
            'set',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-policy-repository-oper'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper',
            is_config=False,
        ),
    },
    'RoutingPolicyShadow.Sets.ExtendedCommunitySoo.Sets_' : {
        'meta_info' : _MetaInfoClass('RoutingPolicyShadow.Sets.ExtendedCommunitySoo.Sets_', REFERENCE_CLASS,
            '''Information about individual sets''',
            False, 
            [
            _MetaInfoClassMember('set', REFERENCE_LIST, 'Set', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper', 'RoutingPolicyShadow.Sets.ExtendedCommunitySoo.Sets_.Set',
                [], [],
                '''                Information about an individual set
                ''',
                'set',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            ],
            'Cisco-IOS-XR-policy-repository-oper',
            'sets',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-policy-repository-oper'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper',
            is_config=False,
        ),
    },
    'RoutingPolicyShadow.Sets.ExtendedCommunitySoo.Unused' : {
        'meta_info' : _MetaInfoClass('RoutingPolicyShadow.Sets.ExtendedCommunitySoo.Unused', REFERENCE_CLASS,
            '''All objects of a given type that are not
referenced at all''',
            False, 
            [
            _MetaInfoClassMember('object', REFERENCE_LEAFLIST, 'str', 'String',
                None, None,
                [], [],
                '''                Policy objects
                ''',
                'object',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            ],
            'Cisco-IOS-XR-policy-repository-oper',
            'unused',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-policy-repository-oper'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper',
            is_config=False,
        ),
    },
    'RoutingPolicyShadow.Sets.ExtendedCommunitySoo.Inactive' : {
        'meta_info' : _MetaInfoClass('RoutingPolicyShadow.Sets.ExtendedCommunitySoo.Inactive', REFERENCE_CLASS,
            '''All objects of a given type that are not
attached to a protocol''',
            False, 
            [
            _MetaInfoClassMember('object', REFERENCE_LEAFLIST, 'str', 'String',
                None, None,
                [], [],
                '''                Policy objects
                ''',
                'object',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            ],
            'Cisco-IOS-XR-policy-repository-oper',
            'inactive',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-policy-repository-oper'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper',
            is_config=False,
        ),
    },
    'RoutingPolicyShadow.Sets.ExtendedCommunitySoo.Active' : {
        'meta_info' : _MetaInfoClass('RoutingPolicyShadow.Sets.ExtendedCommunitySoo.Active', REFERENCE_CLASS,
            '''All objects of a given type that are attached to
a protocol''',
            False, 
            [
            _MetaInfoClassMember('object', REFERENCE_LEAFLIST, 'str', 'String',
                None, None,
                [], [],
                '''                Policy objects
                ''',
                'object',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            ],
            'Cisco-IOS-XR-policy-repository-oper',
            'active',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-policy-repository-oper'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper',
            is_config=False,
        ),
    },
    'RoutingPolicyShadow.Sets.ExtendedCommunitySoo' : {
        'meta_info' : _MetaInfoClass('RoutingPolicyShadow.Sets.ExtendedCommunitySoo', REFERENCE_CLASS,
            '''Information about Extended Community SOO sets''',
            False, 
            [
            _MetaInfoClassMember('sets', REFERENCE_CLASS, 'Sets_', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper', 'RoutingPolicyShadow.Sets.ExtendedCommunitySoo.Sets_',
                [], [],
                '''                Information about individual sets
                ''',
                'sets',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('unused', REFERENCE_CLASS, 'Unused', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper', 'RoutingPolicyShadow.Sets.ExtendedCommunitySoo.Unused',
                [], [],
                '''                All objects of a given type that are not
                referenced at all
                ''',
                'unused',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('inactive', REFERENCE_CLASS, 'Inactive', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper', 'RoutingPolicyShadow.Sets.ExtendedCommunitySoo.Inactive',
                [], [],
                '''                All objects of a given type that are not
                attached to a protocol
                ''',
                'inactive',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('active', REFERENCE_CLASS, 'Active', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper', 'RoutingPolicyShadow.Sets.ExtendedCommunitySoo.Active',
                [], [],
                '''                All objects of a given type that are attached to
                a protocol
                ''',
                'active',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            ],
            'Cisco-IOS-XR-policy-repository-oper',
            'extended-community-soo',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-policy-repository-oper'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper',
            is_config=False,
        ),
    },
    'RoutingPolicyShadow.Sets.Tag.Sets_.Set.UsedBy.Reference' : {
        'meta_info' : _MetaInfoClass('RoutingPolicyShadow.Sets.Tag.Sets_.Set.UsedBy.Reference', REFERENCE_LIST,
            '''Information about policies referring to this
object''',
            False, 
            [
            _MetaInfoClassMember('route-policy-name', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                Name of policy
                ''',
                'route_policy_name',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('used-directly', ATTRIBUTE, 'bool', 'boolean',
                None, None,
                [], [],
                '''                Whether the policy uses this object directly or
                indirectly
                ''',
                'used_directly',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('status', REFERENCE_ENUM_CLASS, 'ObjectStatus', 'Object-status',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper', 'ObjectStatus',
                [], [],
                '''                Active, Inactive, or Unused
                ''',
                'status',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            ],
            'Cisco-IOS-XR-policy-repository-oper',
            'reference',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-policy-repository-oper'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper',
            is_config=False,
        ),
    },
    'RoutingPolicyShadow.Sets.Tag.Sets_.Set.UsedBy' : {
        'meta_info' : _MetaInfoClass('RoutingPolicyShadow.Sets.Tag.Sets_.Set.UsedBy', REFERENCE_CLASS,
            '''Policies that use this object, directly or
indirectly''',
            False, 
            [
            _MetaInfoClassMember('reference', REFERENCE_LIST, 'Reference', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper', 'RoutingPolicyShadow.Sets.Tag.Sets_.Set.UsedBy.Reference',
                [], [],
                '''                Information about policies referring to this
                object
                ''',
                'reference',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            ],
            'Cisco-IOS-XR-policy-repository-oper',
            'used-by',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-policy-repository-oper'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper',
            is_config=False,
        ),
    },
    'RoutingPolicyShadow.Sets.Tag.Sets_.Set.Attached.Binding' : {
        'meta_info' : _MetaInfoClass('RoutingPolicyShadow.Sets.Tag.Sets_.Set.Attached.Binding', REFERENCE_LIST,
            '''bindings list''',
            False, 
            [
            _MetaInfoClassMember('protocol', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                Protocol to which policy attached
                ''',
                'protocol',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('vrf-name', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                VRF name
                ''',
                'vrf_name',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('proto-instance', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                Protocol instance
                ''',
                'proto_instance',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('af-name', REFERENCE_ENUM_CLASS, 'AddressFamily', 'Address-family',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper', 'AddressFamily',
                [], [],
                '''                Address Family Identifier
                ''',
                'af_name',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('saf-name', REFERENCE_ENUM_CLASS, 'SubAddressFamily', 'Sub-address-family',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper', 'SubAddressFamily',
                [], [],
                '''                Subsequent Address Family Identifier
                ''',
                'saf_name',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('neighbor-address', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                Neighbor IP Address
                ''',
                'neighbor_address',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('neighbor-af-name', REFERENCE_ENUM_CLASS, 'AddressFamily', 'Address-family',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper', 'AddressFamily',
                [], [],
                '''                Neighbor IP Address Family
                ''',
                'neighbor_af_name',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('group-name', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                Neighbor Group Name
                ''',
                'group_name',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('direction', REFERENCE_ENUM_CLASS, 'AttachPointDirection', 'Attach-point-direction',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper', 'AttachPointDirection',
                [], [],
                '''                Direction In or Out
                ''',
                'direction',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('group', REFERENCE_ENUM_CLASS, 'Group', 'Group',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper', 'Group',
                [], [],
                '''                Neighbor Group 
                ''',
                'group',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('source-protocol', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                Source Protocol to redistribute, Source Protocol
                can be one of the following values{all,
                connected, local, static, bgp, rip, isis, ospf
                ,ospfv3, eigrp, unknown }
                ''',
                'source_protocol',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('aggregate-network-address', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                Aggregate IP address or Network IP Address in
                IPv4 or IPv6 Format
                ''',
                'aggregate_network_address',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('interface-name', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                Interface Name
                ''',
                'interface_name',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('instance', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                Instance
                ''',
                'instance',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('area-id', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                OSPF Area ID in Decimal Integer Format
                ''',
                'area_id',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('propogate-from', ATTRIBUTE, 'int', 'int32',
                None, None,
                [('-2147483648', '2147483647')], [],
                '''                ISIS Propogate From Level
                ''',
                'propogate_from',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('propogate-to', ATTRIBUTE, 'int', 'int32',
                None, None,
                [('-2147483648', '2147483647')], [],
                '''                ISIS Propogate To Level
                ''',
                'propogate_to',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('route-policy-name', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                Policy that uses object in question
                ''',
                'route_policy_name',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('attached-policy', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                The attached policy that (maybe indirectly) uses
                the object in question
                ''',
                'attached_policy',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('attach-point', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                Name of attach point where policy is attached
                ''',
                'attach_point',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            ],
            'Cisco-IOS-XR-policy-repository-oper',
            'binding',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-policy-repository-oper'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper',
            is_config=False,
        ),
    },
    'RoutingPolicyShadow.Sets.Tag.Sets_.Set.Attached' : {
        'meta_info' : _MetaInfoClass('RoutingPolicyShadow.Sets.Tag.Sets_.Set.Attached', REFERENCE_CLASS,
            '''Information about where this policy or set is
attached''',
            False, 
            [
            _MetaInfoClassMember('binding', REFERENCE_LIST, 'Binding', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper', 'RoutingPolicyShadow.Sets.Tag.Sets_.Set.Attached.Binding',
                [], [],
                '''                bindings list
                ''',
                'binding',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            ],
            'Cisco-IOS-XR-policy-repository-oper',
            'attached',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-policy-repository-oper'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper',
            is_config=False,
        ),
    },
    'RoutingPolicyShadow.Sets.Tag.Sets_.Set' : {
        'meta_info' : _MetaInfoClass('RoutingPolicyShadow.Sets.Tag.Sets_.Set', REFERENCE_LIST,
            '''Information about an individual set''',
            False, 
            [
            _MetaInfoClassMember('set-name', ATTRIBUTE, 'str', 'xr:Cisco-ios-xr-string',
                None, None,
                [], [b'[\\w\\-\\.:,_@#%$\\+=\\|;]+'],
                '''                Set name
                ''',
                'set_name',
                'Cisco-IOS-XR-policy-repository-oper', True, is_config=False),
            _MetaInfoClassMember('used-by', REFERENCE_CLASS, 'UsedBy', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper', 'RoutingPolicyShadow.Sets.Tag.Sets_.Set.UsedBy',
                [], [],
                '''                Policies that use this object, directly or
                indirectly
                ''',
                'used_by',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('attached', REFERENCE_CLASS, 'Attached', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper', 'RoutingPolicyShadow.Sets.Tag.Sets_.Set.Attached',
                [], [],
                '''                Information about where this policy or set is
                attached
                ''',
                'attached',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            ],
            'Cisco-IOS-XR-policy-repository-oper',
            'set',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-policy-repository-oper'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper',
            is_config=False,
        ),
    },
    'RoutingPolicyShadow.Sets.Tag.Sets_' : {
        'meta_info' : _MetaInfoClass('RoutingPolicyShadow.Sets.Tag.Sets_', REFERENCE_CLASS,
            '''Information about individual sets''',
            False, 
            [
            _MetaInfoClassMember('set', REFERENCE_LIST, 'Set', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper', 'RoutingPolicyShadow.Sets.Tag.Sets_.Set',
                [], [],
                '''                Information about an individual set
                ''',
                'set',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            ],
            'Cisco-IOS-XR-policy-repository-oper',
            'sets',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-policy-repository-oper'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper',
            is_config=False,
        ),
    },
    'RoutingPolicyShadow.Sets.Tag.Unused' : {
        'meta_info' : _MetaInfoClass('RoutingPolicyShadow.Sets.Tag.Unused', REFERENCE_CLASS,
            '''All objects of a given type that are not
referenced at all''',
            False, 
            [
            _MetaInfoClassMember('object', REFERENCE_LEAFLIST, 'str', 'String',
                None, None,
                [], [],
                '''                Policy objects
                ''',
                'object',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            ],
            'Cisco-IOS-XR-policy-repository-oper',
            'unused',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-policy-repository-oper'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper',
            is_config=False,
        ),
    },
    'RoutingPolicyShadow.Sets.Tag.Inactive' : {
        'meta_info' : _MetaInfoClass('RoutingPolicyShadow.Sets.Tag.Inactive', REFERENCE_CLASS,
            '''All objects of a given type that are not
attached to a protocol''',
            False, 
            [
            _MetaInfoClassMember('object', REFERENCE_LEAFLIST, 'str', 'String',
                None, None,
                [], [],
                '''                Policy objects
                ''',
                'object',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            ],
            'Cisco-IOS-XR-policy-repository-oper',
            'inactive',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-policy-repository-oper'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper',
            is_config=False,
        ),
    },
    'RoutingPolicyShadow.Sets.Tag.Active' : {
        'meta_info' : _MetaInfoClass('RoutingPolicyShadow.Sets.Tag.Active', REFERENCE_CLASS,
            '''All objects of a given type that are attached to
a protocol''',
            False, 
            [
            _MetaInfoClassMember('object', REFERENCE_LEAFLIST, 'str', 'String',
                None, None,
                [], [],
                '''                Policy objects
                ''',
                'object',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            ],
            'Cisco-IOS-XR-policy-repository-oper',
            'active',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-policy-repository-oper'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper',
            is_config=False,
        ),
    },
    'RoutingPolicyShadow.Sets.Tag' : {
        'meta_info' : _MetaInfoClass('RoutingPolicyShadow.Sets.Tag', REFERENCE_CLASS,
            '''Information about Tag sets''',
            False, 
            [
            _MetaInfoClassMember('sets', REFERENCE_CLASS, 'Sets_', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper', 'RoutingPolicyShadow.Sets.Tag.Sets_',
                [], [],
                '''                Information about individual sets
                ''',
                'sets',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('unused', REFERENCE_CLASS, 'Unused', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper', 'RoutingPolicyShadow.Sets.Tag.Unused',
                [], [],
                '''                All objects of a given type that are not
                referenced at all
                ''',
                'unused',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('inactive', REFERENCE_CLASS, 'Inactive', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper', 'RoutingPolicyShadow.Sets.Tag.Inactive',
                [], [],
                '''                All objects of a given type that are not
                attached to a protocol
                ''',
                'inactive',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('active', REFERENCE_CLASS, 'Active', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper', 'RoutingPolicyShadow.Sets.Tag.Active',
                [], [],
                '''                All objects of a given type that are attached to
                a protocol
                ''',
                'active',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            ],
            'Cisco-IOS-XR-policy-repository-oper',
            'tag',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-policy-repository-oper'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper',
            is_config=False,
        ),
    },
    'RoutingPolicyShadow.Sets.Prefix.Sets_.Set.UsedBy.Reference' : {
        'meta_info' : _MetaInfoClass('RoutingPolicyShadow.Sets.Prefix.Sets_.Set.UsedBy.Reference', REFERENCE_LIST,
            '''Information about policies referring to this
object''',
            False, 
            [
            _MetaInfoClassMember('route-policy-name', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                Name of policy
                ''',
                'route_policy_name',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('used-directly', ATTRIBUTE, 'bool', 'boolean',
                None, None,
                [], [],
                '''                Whether the policy uses this object directly or
                indirectly
                ''',
                'used_directly',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('status', REFERENCE_ENUM_CLASS, 'ObjectStatus', 'Object-status',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper', 'ObjectStatus',
                [], [],
                '''                Active, Inactive, or Unused
                ''',
                'status',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            ],
            'Cisco-IOS-XR-policy-repository-oper',
            'reference',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-policy-repository-oper'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper',
            is_config=False,
        ),
    },
    'RoutingPolicyShadow.Sets.Prefix.Sets_.Set.UsedBy' : {
        'meta_info' : _MetaInfoClass('RoutingPolicyShadow.Sets.Prefix.Sets_.Set.UsedBy', REFERENCE_CLASS,
            '''Policies that use this object, directly or
indirectly''',
            False, 
            [
            _MetaInfoClassMember('reference', REFERENCE_LIST, 'Reference', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper', 'RoutingPolicyShadow.Sets.Prefix.Sets_.Set.UsedBy.Reference',
                [], [],
                '''                Information about policies referring to this
                object
                ''',
                'reference',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            ],
            'Cisco-IOS-XR-policy-repository-oper',
            'used-by',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-policy-repository-oper'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper',
            is_config=False,
        ),
    },
    'RoutingPolicyShadow.Sets.Prefix.Sets_.Set.Attached.Binding' : {
        'meta_info' : _MetaInfoClass('RoutingPolicyShadow.Sets.Prefix.Sets_.Set.Attached.Binding', REFERENCE_LIST,
            '''bindings list''',
            False, 
            [
            _MetaInfoClassMember('protocol', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                Protocol to which policy attached
                ''',
                'protocol',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('vrf-name', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                VRF name
                ''',
                'vrf_name',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('proto-instance', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                Protocol instance
                ''',
                'proto_instance',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('af-name', REFERENCE_ENUM_CLASS, 'AddressFamily', 'Address-family',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper', 'AddressFamily',
                [], [],
                '''                Address Family Identifier
                ''',
                'af_name',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('saf-name', REFERENCE_ENUM_CLASS, 'SubAddressFamily', 'Sub-address-family',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper', 'SubAddressFamily',
                [], [],
                '''                Subsequent Address Family Identifier
                ''',
                'saf_name',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('neighbor-address', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                Neighbor IP Address
                ''',
                'neighbor_address',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('neighbor-af-name', REFERENCE_ENUM_CLASS, 'AddressFamily', 'Address-family',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper', 'AddressFamily',
                [], [],
                '''                Neighbor IP Address Family
                ''',
                'neighbor_af_name',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('group-name', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                Neighbor Group Name
                ''',
                'group_name',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('direction', REFERENCE_ENUM_CLASS, 'AttachPointDirection', 'Attach-point-direction',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper', 'AttachPointDirection',
                [], [],
                '''                Direction In or Out
                ''',
                'direction',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('group', REFERENCE_ENUM_CLASS, 'Group', 'Group',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper', 'Group',
                [], [],
                '''                Neighbor Group 
                ''',
                'group',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('source-protocol', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                Source Protocol to redistribute, Source Protocol
                can be one of the following values{all,
                connected, local, static, bgp, rip, isis, ospf
                ,ospfv3, eigrp, unknown }
                ''',
                'source_protocol',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('aggregate-network-address', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                Aggregate IP address or Network IP Address in
                IPv4 or IPv6 Format
                ''',
                'aggregate_network_address',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('interface-name', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                Interface Name
                ''',
                'interface_name',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('instance', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                Instance
                ''',
                'instance',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('area-id', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                OSPF Area ID in Decimal Integer Format
                ''',
                'area_id',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('propogate-from', ATTRIBUTE, 'int', 'int32',
                None, None,
                [('-2147483648', '2147483647')], [],
                '''                ISIS Propogate From Level
                ''',
                'propogate_from',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('propogate-to', ATTRIBUTE, 'int', 'int32',
                None, None,
                [('-2147483648', '2147483647')], [],
                '''                ISIS Propogate To Level
                ''',
                'propogate_to',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('route-policy-name', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                Policy that uses object in question
                ''',
                'route_policy_name',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('attached-policy', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                The attached policy that (maybe indirectly) uses
                the object in question
                ''',
                'attached_policy',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('attach-point', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                Name of attach point where policy is attached
                ''',
                'attach_point',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            ],
            'Cisco-IOS-XR-policy-repository-oper',
            'binding',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-policy-repository-oper'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper',
            is_config=False,
        ),
    },
    'RoutingPolicyShadow.Sets.Prefix.Sets_.Set.Attached' : {
        'meta_info' : _MetaInfoClass('RoutingPolicyShadow.Sets.Prefix.Sets_.Set.Attached', REFERENCE_CLASS,
            '''Information about where this policy or set is
attached''',
            False, 
            [
            _MetaInfoClassMember('binding', REFERENCE_LIST, 'Binding', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper', 'RoutingPolicyShadow.Sets.Prefix.Sets_.Set.Attached.Binding',
                [], [],
                '''                bindings list
                ''',
                'binding',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            ],
            'Cisco-IOS-XR-policy-repository-oper',
            'attached',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-policy-repository-oper'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper',
            is_config=False,
        ),
    },
    'RoutingPolicyShadow.Sets.Prefix.Sets_.Set' : {
        'meta_info' : _MetaInfoClass('RoutingPolicyShadow.Sets.Prefix.Sets_.Set', REFERENCE_LIST,
            '''Information about an individual set''',
            False, 
            [
            _MetaInfoClassMember('set-name', ATTRIBUTE, 'str', 'xr:Cisco-ios-xr-string',
                None, None,
                [], [b'[\\w\\-\\.:,_@#%$\\+=\\|;]+'],
                '''                Set name
                ''',
                'set_name',
                'Cisco-IOS-XR-policy-repository-oper', True, is_config=False),
            _MetaInfoClassMember('used-by', REFERENCE_CLASS, 'UsedBy', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper', 'RoutingPolicyShadow.Sets.Prefix.Sets_.Set.UsedBy',
                [], [],
                '''                Policies that use this object, directly or
                indirectly
                ''',
                'used_by',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('attached', REFERENCE_CLASS, 'Attached', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper', 'RoutingPolicyShadow.Sets.Prefix.Sets_.Set.Attached',
                [], [],
                '''                Information about where this policy or set is
                attached
                ''',
                'attached',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            ],
            'Cisco-IOS-XR-policy-repository-oper',
            'set',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-policy-repository-oper'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper',
            is_config=False,
        ),
    },
    'RoutingPolicyShadow.Sets.Prefix.Sets_' : {
        'meta_info' : _MetaInfoClass('RoutingPolicyShadow.Sets.Prefix.Sets_', REFERENCE_CLASS,
            '''Information about individual sets''',
            False, 
            [
            _MetaInfoClassMember('set', REFERENCE_LIST, 'Set', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper', 'RoutingPolicyShadow.Sets.Prefix.Sets_.Set',
                [], [],
                '''                Information about an individual set
                ''',
                'set',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            ],
            'Cisco-IOS-XR-policy-repository-oper',
            'sets',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-policy-repository-oper'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper',
            is_config=False,
        ),
    },
    'RoutingPolicyShadow.Sets.Prefix.Unused' : {
        'meta_info' : _MetaInfoClass('RoutingPolicyShadow.Sets.Prefix.Unused', REFERENCE_CLASS,
            '''All objects of a given type that are not
referenced at all''',
            False, 
            [
            _MetaInfoClassMember('object', REFERENCE_LEAFLIST, 'str', 'String',
                None, None,
                [], [],
                '''                Policy objects
                ''',
                'object',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            ],
            'Cisco-IOS-XR-policy-repository-oper',
            'unused',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-policy-repository-oper'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper',
            is_config=False,
        ),
    },
    'RoutingPolicyShadow.Sets.Prefix.Inactive' : {
        'meta_info' : _MetaInfoClass('RoutingPolicyShadow.Sets.Prefix.Inactive', REFERENCE_CLASS,
            '''All objects of a given type that are not
attached to a protocol''',
            False, 
            [
            _MetaInfoClassMember('object', REFERENCE_LEAFLIST, 'str', 'String',
                None, None,
                [], [],
                '''                Policy objects
                ''',
                'object',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            ],
            'Cisco-IOS-XR-policy-repository-oper',
            'inactive',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-policy-repository-oper'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper',
            is_config=False,
        ),
    },
    'RoutingPolicyShadow.Sets.Prefix.Active' : {
        'meta_info' : _MetaInfoClass('RoutingPolicyShadow.Sets.Prefix.Active', REFERENCE_CLASS,
            '''All objects of a given type that are attached to
a protocol''',
            False, 
            [
            _MetaInfoClassMember('object', REFERENCE_LEAFLIST, 'str', 'String',
                None, None,
                [], [],
                '''                Policy objects
                ''',
                'object',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            ],
            'Cisco-IOS-XR-policy-repository-oper',
            'active',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-policy-repository-oper'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper',
            is_config=False,
        ),
    },
    'RoutingPolicyShadow.Sets.Prefix' : {
        'meta_info' : _MetaInfoClass('RoutingPolicyShadow.Sets.Prefix', REFERENCE_CLASS,
            '''Information about AS Path sets''',
            False, 
            [
            _MetaInfoClassMember('sets', REFERENCE_CLASS, 'Sets_', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper', 'RoutingPolicyShadow.Sets.Prefix.Sets_',
                [], [],
                '''                Information about individual sets
                ''',
                'sets',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('unused', REFERENCE_CLASS, 'Unused', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper', 'RoutingPolicyShadow.Sets.Prefix.Unused',
                [], [],
                '''                All objects of a given type that are not
                referenced at all
                ''',
                'unused',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('inactive', REFERENCE_CLASS, 'Inactive', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper', 'RoutingPolicyShadow.Sets.Prefix.Inactive',
                [], [],
                '''                All objects of a given type that are not
                attached to a protocol
                ''',
                'inactive',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('active', REFERENCE_CLASS, 'Active', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper', 'RoutingPolicyShadow.Sets.Prefix.Active',
                [], [],
                '''                All objects of a given type that are attached to
                a protocol
                ''',
                'active',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            ],
            'Cisco-IOS-XR-policy-repository-oper',
            'prefix',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-policy-repository-oper'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper',
            is_config=False,
        ),
    },
    'RoutingPolicyShadow.Sets.Community.Sets_.Set.UsedBy.Reference' : {
        'meta_info' : _MetaInfoClass('RoutingPolicyShadow.Sets.Community.Sets_.Set.UsedBy.Reference', REFERENCE_LIST,
            '''Information about policies referring to this
object''',
            False, 
            [
            _MetaInfoClassMember('route-policy-name', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                Name of policy
                ''',
                'route_policy_name',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('used-directly', ATTRIBUTE, 'bool', 'boolean',
                None, None,
                [], [],
                '''                Whether the policy uses this object directly or
                indirectly
                ''',
                'used_directly',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('status', REFERENCE_ENUM_CLASS, 'ObjectStatus', 'Object-status',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper', 'ObjectStatus',
                [], [],
                '''                Active, Inactive, or Unused
                ''',
                'status',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            ],
            'Cisco-IOS-XR-policy-repository-oper',
            'reference',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-policy-repository-oper'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper',
            is_config=False,
        ),
    },
    'RoutingPolicyShadow.Sets.Community.Sets_.Set.UsedBy' : {
        'meta_info' : _MetaInfoClass('RoutingPolicyShadow.Sets.Community.Sets_.Set.UsedBy', REFERENCE_CLASS,
            '''Policies that use this object, directly or
indirectly''',
            False, 
            [
            _MetaInfoClassMember('reference', REFERENCE_LIST, 'Reference', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper', 'RoutingPolicyShadow.Sets.Community.Sets_.Set.UsedBy.Reference',
                [], [],
                '''                Information about policies referring to this
                object
                ''',
                'reference',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            ],
            'Cisco-IOS-XR-policy-repository-oper',
            'used-by',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-policy-repository-oper'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper',
            is_config=False,
        ),
    },
    'RoutingPolicyShadow.Sets.Community.Sets_.Set.Attached.Binding' : {
        'meta_info' : _MetaInfoClass('RoutingPolicyShadow.Sets.Community.Sets_.Set.Attached.Binding', REFERENCE_LIST,
            '''bindings list''',
            False, 
            [
            _MetaInfoClassMember('protocol', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                Protocol to which policy attached
                ''',
                'protocol',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('vrf-name', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                VRF name
                ''',
                'vrf_name',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('proto-instance', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                Protocol instance
                ''',
                'proto_instance',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('af-name', REFERENCE_ENUM_CLASS, 'AddressFamily', 'Address-family',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper', 'AddressFamily',
                [], [],
                '''                Address Family Identifier
                ''',
                'af_name',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('saf-name', REFERENCE_ENUM_CLASS, 'SubAddressFamily', 'Sub-address-family',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper', 'SubAddressFamily',
                [], [],
                '''                Subsequent Address Family Identifier
                ''',
                'saf_name',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('neighbor-address', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                Neighbor IP Address
                ''',
                'neighbor_address',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('neighbor-af-name', REFERENCE_ENUM_CLASS, 'AddressFamily', 'Address-family',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper', 'AddressFamily',
                [], [],
                '''                Neighbor IP Address Family
                ''',
                'neighbor_af_name',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('group-name', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                Neighbor Group Name
                ''',
                'group_name',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('direction', REFERENCE_ENUM_CLASS, 'AttachPointDirection', 'Attach-point-direction',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper', 'AttachPointDirection',
                [], [],
                '''                Direction In or Out
                ''',
                'direction',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('group', REFERENCE_ENUM_CLASS, 'Group', 'Group',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper', 'Group',
                [], [],
                '''                Neighbor Group 
                ''',
                'group',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('source-protocol', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                Source Protocol to redistribute, Source Protocol
                can be one of the following values{all,
                connected, local, static, bgp, rip, isis, ospf
                ,ospfv3, eigrp, unknown }
                ''',
                'source_protocol',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('aggregate-network-address', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                Aggregate IP address or Network IP Address in
                IPv4 or IPv6 Format
                ''',
                'aggregate_network_address',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('interface-name', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                Interface Name
                ''',
                'interface_name',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('instance', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                Instance
                ''',
                'instance',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('area-id', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                OSPF Area ID in Decimal Integer Format
                ''',
                'area_id',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('propogate-from', ATTRIBUTE, 'int', 'int32',
                None, None,
                [('-2147483648', '2147483647')], [],
                '''                ISIS Propogate From Level
                ''',
                'propogate_from',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('propogate-to', ATTRIBUTE, 'int', 'int32',
                None, None,
                [('-2147483648', '2147483647')], [],
                '''                ISIS Propogate To Level
                ''',
                'propogate_to',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('route-policy-name', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                Policy that uses object in question
                ''',
                'route_policy_name',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('attached-policy', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                The attached policy that (maybe indirectly) uses
                the object in question
                ''',
                'attached_policy',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('attach-point', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                Name of attach point where policy is attached
                ''',
                'attach_point',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            ],
            'Cisco-IOS-XR-policy-repository-oper',
            'binding',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-policy-repository-oper'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper',
            is_config=False,
        ),
    },
    'RoutingPolicyShadow.Sets.Community.Sets_.Set.Attached' : {
        'meta_info' : _MetaInfoClass('RoutingPolicyShadow.Sets.Community.Sets_.Set.Attached', REFERENCE_CLASS,
            '''Information about where this policy or set is
attached''',
            False, 
            [
            _MetaInfoClassMember('binding', REFERENCE_LIST, 'Binding', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper', 'RoutingPolicyShadow.Sets.Community.Sets_.Set.Attached.Binding',
                [], [],
                '''                bindings list
                ''',
                'binding',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            ],
            'Cisco-IOS-XR-policy-repository-oper',
            'attached',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-policy-repository-oper'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper',
            is_config=False,
        ),
    },
    'RoutingPolicyShadow.Sets.Community.Sets_.Set' : {
        'meta_info' : _MetaInfoClass('RoutingPolicyShadow.Sets.Community.Sets_.Set', REFERENCE_LIST,
            '''Information about an individual set''',
            False, 
            [
            _MetaInfoClassMember('set-name', ATTRIBUTE, 'str', 'xr:Cisco-ios-xr-string',
                None, None,
                [], [b'[\\w\\-\\.:,_@#%$\\+=\\|;]+'],
                '''                Set name
                ''',
                'set_name',
                'Cisco-IOS-XR-policy-repository-oper', True, is_config=False),
            _MetaInfoClassMember('used-by', REFERENCE_CLASS, 'UsedBy', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper', 'RoutingPolicyShadow.Sets.Community.Sets_.Set.UsedBy',
                [], [],
                '''                Policies that use this object, directly or
                indirectly
                ''',
                'used_by',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('attached', REFERENCE_CLASS, 'Attached', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper', 'RoutingPolicyShadow.Sets.Community.Sets_.Set.Attached',
                [], [],
                '''                Information about where this policy or set is
                attached
                ''',
                'attached',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            ],
            'Cisco-IOS-XR-policy-repository-oper',
            'set',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-policy-repository-oper'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper',
            is_config=False,
        ),
    },
    'RoutingPolicyShadow.Sets.Community.Sets_' : {
        'meta_info' : _MetaInfoClass('RoutingPolicyShadow.Sets.Community.Sets_', REFERENCE_CLASS,
            '''Information about individual sets''',
            False, 
            [
            _MetaInfoClassMember('set', REFERENCE_LIST, 'Set', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper', 'RoutingPolicyShadow.Sets.Community.Sets_.Set',
                [], [],
                '''                Information about an individual set
                ''',
                'set',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            ],
            'Cisco-IOS-XR-policy-repository-oper',
            'sets',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-policy-repository-oper'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper',
            is_config=False,
        ),
    },
    'RoutingPolicyShadow.Sets.Community.Unused' : {
        'meta_info' : _MetaInfoClass('RoutingPolicyShadow.Sets.Community.Unused', REFERENCE_CLASS,
            '''All objects of a given type that are not
referenced at all''',
            False, 
            [
            _MetaInfoClassMember('object', REFERENCE_LEAFLIST, 'str', 'String',
                None, None,
                [], [],
                '''                Policy objects
                ''',
                'object',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            ],
            'Cisco-IOS-XR-policy-repository-oper',
            'unused',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-policy-repository-oper'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper',
            is_config=False,
        ),
    },
    'RoutingPolicyShadow.Sets.Community.Inactive' : {
        'meta_info' : _MetaInfoClass('RoutingPolicyShadow.Sets.Community.Inactive', REFERENCE_CLASS,
            '''All objects of a given type that are not
attached to a protocol''',
            False, 
            [
            _MetaInfoClassMember('object', REFERENCE_LEAFLIST, 'str', 'String',
                None, None,
                [], [],
                '''                Policy objects
                ''',
                'object',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            ],
            'Cisco-IOS-XR-policy-repository-oper',
            'inactive',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-policy-repository-oper'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper',
            is_config=False,
        ),
    },
    'RoutingPolicyShadow.Sets.Community.Active' : {
        'meta_info' : _MetaInfoClass('RoutingPolicyShadow.Sets.Community.Active', REFERENCE_CLASS,
            '''All objects of a given type that are attached to
a protocol''',
            False, 
            [
            _MetaInfoClassMember('object', REFERENCE_LEAFLIST, 'str', 'String',
                None, None,
                [], [],
                '''                Policy objects
                ''',
                'object',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            ],
            'Cisco-IOS-XR-policy-repository-oper',
            'active',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-policy-repository-oper'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper',
            is_config=False,
        ),
    },
    'RoutingPolicyShadow.Sets.Community' : {
        'meta_info' : _MetaInfoClass('RoutingPolicyShadow.Sets.Community', REFERENCE_CLASS,
            '''Information about Community sets''',
            False, 
            [
            _MetaInfoClassMember('sets', REFERENCE_CLASS, 'Sets_', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper', 'RoutingPolicyShadow.Sets.Community.Sets_',
                [], [],
                '''                Information about individual sets
                ''',
                'sets',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('unused', REFERENCE_CLASS, 'Unused', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper', 'RoutingPolicyShadow.Sets.Community.Unused',
                [], [],
                '''                All objects of a given type that are not
                referenced at all
                ''',
                'unused',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('inactive', REFERENCE_CLASS, 'Inactive', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper', 'RoutingPolicyShadow.Sets.Community.Inactive',
                [], [],
                '''                All objects of a given type that are not
                attached to a protocol
                ''',
                'inactive',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('active', REFERENCE_CLASS, 'Active', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper', 'RoutingPolicyShadow.Sets.Community.Active',
                [], [],
                '''                All objects of a given type that are attached to
                a protocol
                ''',
                'active',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            ],
            'Cisco-IOS-XR-policy-repository-oper',
            'community',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-policy-repository-oper'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper',
            is_config=False,
        ),
    },
    'RoutingPolicyShadow.Sets.AsPath.Sets_.Set.UsedBy.Reference' : {
        'meta_info' : _MetaInfoClass('RoutingPolicyShadow.Sets.AsPath.Sets_.Set.UsedBy.Reference', REFERENCE_LIST,
            '''Information about policies referring to this
object''',
            False, 
            [
            _MetaInfoClassMember('route-policy-name', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                Name of policy
                ''',
                'route_policy_name',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('used-directly', ATTRIBUTE, 'bool', 'boolean',
                None, None,
                [], [],
                '''                Whether the policy uses this object directly or
                indirectly
                ''',
                'used_directly',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('status', REFERENCE_ENUM_CLASS, 'ObjectStatus', 'Object-status',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper', 'ObjectStatus',
                [], [],
                '''                Active, Inactive, or Unused
                ''',
                'status',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            ],
            'Cisco-IOS-XR-policy-repository-oper',
            'reference',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-policy-repository-oper'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper',
            is_config=False,
        ),
    },
    'RoutingPolicyShadow.Sets.AsPath.Sets_.Set.UsedBy' : {
        'meta_info' : _MetaInfoClass('RoutingPolicyShadow.Sets.AsPath.Sets_.Set.UsedBy', REFERENCE_CLASS,
            '''Policies that use this object, directly or
indirectly''',
            False, 
            [
            _MetaInfoClassMember('reference', REFERENCE_LIST, 'Reference', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper', 'RoutingPolicyShadow.Sets.AsPath.Sets_.Set.UsedBy.Reference',
                [], [],
                '''                Information about policies referring to this
                object
                ''',
                'reference',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            ],
            'Cisco-IOS-XR-policy-repository-oper',
            'used-by',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-policy-repository-oper'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper',
            is_config=False,
        ),
    },
    'RoutingPolicyShadow.Sets.AsPath.Sets_.Set.Attached.Binding' : {
        'meta_info' : _MetaInfoClass('RoutingPolicyShadow.Sets.AsPath.Sets_.Set.Attached.Binding', REFERENCE_LIST,
            '''bindings list''',
            False, 
            [
            _MetaInfoClassMember('protocol', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                Protocol to which policy attached
                ''',
                'protocol',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('vrf-name', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                VRF name
                ''',
                'vrf_name',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('proto-instance', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                Protocol instance
                ''',
                'proto_instance',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('af-name', REFERENCE_ENUM_CLASS, 'AddressFamily', 'Address-family',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper', 'AddressFamily',
                [], [],
                '''                Address Family Identifier
                ''',
                'af_name',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('saf-name', REFERENCE_ENUM_CLASS, 'SubAddressFamily', 'Sub-address-family',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper', 'SubAddressFamily',
                [], [],
                '''                Subsequent Address Family Identifier
                ''',
                'saf_name',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('neighbor-address', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                Neighbor IP Address
                ''',
                'neighbor_address',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('neighbor-af-name', REFERENCE_ENUM_CLASS, 'AddressFamily', 'Address-family',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper', 'AddressFamily',
                [], [],
                '''                Neighbor IP Address Family
                ''',
                'neighbor_af_name',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('group-name', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                Neighbor Group Name
                ''',
                'group_name',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('direction', REFERENCE_ENUM_CLASS, 'AttachPointDirection', 'Attach-point-direction',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper', 'AttachPointDirection',
                [], [],
                '''                Direction In or Out
                ''',
                'direction',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('group', REFERENCE_ENUM_CLASS, 'Group', 'Group',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper', 'Group',
                [], [],
                '''                Neighbor Group 
                ''',
                'group',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('source-protocol', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                Source Protocol to redistribute, Source Protocol
                can be one of the following values{all,
                connected, local, static, bgp, rip, isis, ospf
                ,ospfv3, eigrp, unknown }
                ''',
                'source_protocol',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('aggregate-network-address', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                Aggregate IP address or Network IP Address in
                IPv4 or IPv6 Format
                ''',
                'aggregate_network_address',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('interface-name', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                Interface Name
                ''',
                'interface_name',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('instance', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                Instance
                ''',
                'instance',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('area-id', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                OSPF Area ID in Decimal Integer Format
                ''',
                'area_id',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('propogate-from', ATTRIBUTE, 'int', 'int32',
                None, None,
                [('-2147483648', '2147483647')], [],
                '''                ISIS Propogate From Level
                ''',
                'propogate_from',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('propogate-to', ATTRIBUTE, 'int', 'int32',
                None, None,
                [('-2147483648', '2147483647')], [],
                '''                ISIS Propogate To Level
                ''',
                'propogate_to',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('route-policy-name', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                Policy that uses object in question
                ''',
                'route_policy_name',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('attached-policy', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                The attached policy that (maybe indirectly) uses
                the object in question
                ''',
                'attached_policy',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('attach-point', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                Name of attach point where policy is attached
                ''',
                'attach_point',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            ],
            'Cisco-IOS-XR-policy-repository-oper',
            'binding',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-policy-repository-oper'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper',
            is_config=False,
        ),
    },
    'RoutingPolicyShadow.Sets.AsPath.Sets_.Set.Attached' : {
        'meta_info' : _MetaInfoClass('RoutingPolicyShadow.Sets.AsPath.Sets_.Set.Attached', REFERENCE_CLASS,
            '''Information about where this policy or set is
attached''',
            False, 
            [
            _MetaInfoClassMember('binding', REFERENCE_LIST, 'Binding', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper', 'RoutingPolicyShadow.Sets.AsPath.Sets_.Set.Attached.Binding',
                [], [],
                '''                bindings list
                ''',
                'binding',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            ],
            'Cisco-IOS-XR-policy-repository-oper',
            'attached',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-policy-repository-oper'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper',
            is_config=False,
        ),
    },
    'RoutingPolicyShadow.Sets.AsPath.Sets_.Set' : {
        'meta_info' : _MetaInfoClass('RoutingPolicyShadow.Sets.AsPath.Sets_.Set', REFERENCE_LIST,
            '''Information about an individual set''',
            False, 
            [
            _MetaInfoClassMember('set-name', ATTRIBUTE, 'str', 'xr:Cisco-ios-xr-string',
                None, None,
                [], [b'[\\w\\-\\.:,_@#%$\\+=\\|;]+'],
                '''                Set name
                ''',
                'set_name',
                'Cisco-IOS-XR-policy-repository-oper', True, is_config=False),
            _MetaInfoClassMember('used-by', REFERENCE_CLASS, 'UsedBy', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper', 'RoutingPolicyShadow.Sets.AsPath.Sets_.Set.UsedBy',
                [], [],
                '''                Policies that use this object, directly or
                indirectly
                ''',
                'used_by',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('attached', REFERENCE_CLASS, 'Attached', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper', 'RoutingPolicyShadow.Sets.AsPath.Sets_.Set.Attached',
                [], [],
                '''                Information about where this policy or set is
                attached
                ''',
                'attached',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            ],
            'Cisco-IOS-XR-policy-repository-oper',
            'set',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-policy-repository-oper'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper',
            is_config=False,
        ),
    },
    'RoutingPolicyShadow.Sets.AsPath.Sets_' : {
        'meta_info' : _MetaInfoClass('RoutingPolicyShadow.Sets.AsPath.Sets_', REFERENCE_CLASS,
            '''Information about individual sets''',
            False, 
            [
            _MetaInfoClassMember('set', REFERENCE_LIST, 'Set', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper', 'RoutingPolicyShadow.Sets.AsPath.Sets_.Set',
                [], [],
                '''                Information about an individual set
                ''',
                'set',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            ],
            'Cisco-IOS-XR-policy-repository-oper',
            'sets',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-policy-repository-oper'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper',
            is_config=False,
        ),
    },
    'RoutingPolicyShadow.Sets.AsPath.Unused' : {
        'meta_info' : _MetaInfoClass('RoutingPolicyShadow.Sets.AsPath.Unused', REFERENCE_CLASS,
            '''All objects of a given type that are not
referenced at all''',
            False, 
            [
            _MetaInfoClassMember('object', REFERENCE_LEAFLIST, 'str', 'String',
                None, None,
                [], [],
                '''                Policy objects
                ''',
                'object',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            ],
            'Cisco-IOS-XR-policy-repository-oper',
            'unused',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-policy-repository-oper'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper',
            is_config=False,
        ),
    },
    'RoutingPolicyShadow.Sets.AsPath.Inactive' : {
        'meta_info' : _MetaInfoClass('RoutingPolicyShadow.Sets.AsPath.Inactive', REFERENCE_CLASS,
            '''All objects of a given type that are not
attached to a protocol''',
            False, 
            [
            _MetaInfoClassMember('object', REFERENCE_LEAFLIST, 'str', 'String',
                None, None,
                [], [],
                '''                Policy objects
                ''',
                'object',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            ],
            'Cisco-IOS-XR-policy-repository-oper',
            'inactive',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-policy-repository-oper'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper',
            is_config=False,
        ),
    },
    'RoutingPolicyShadow.Sets.AsPath.Active' : {
        'meta_info' : _MetaInfoClass('RoutingPolicyShadow.Sets.AsPath.Active', REFERENCE_CLASS,
            '''All objects of a given type that are attached to
a protocol''',
            False, 
            [
            _MetaInfoClassMember('object', REFERENCE_LEAFLIST, 'str', 'String',
                None, None,
                [], [],
                '''                Policy objects
                ''',
                'object',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            ],
            'Cisco-IOS-XR-policy-repository-oper',
            'active',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-policy-repository-oper'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper',
            is_config=False,
        ),
    },
    'RoutingPolicyShadow.Sets.AsPath' : {
        'meta_info' : _MetaInfoClass('RoutingPolicyShadow.Sets.AsPath', REFERENCE_CLASS,
            '''Information about AS Path sets''',
            False, 
            [
            _MetaInfoClassMember('sets', REFERENCE_CLASS, 'Sets_', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper', 'RoutingPolicyShadow.Sets.AsPath.Sets_',
                [], [],
                '''                Information about individual sets
                ''',
                'sets',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('unused', REFERENCE_CLASS, 'Unused', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper', 'RoutingPolicyShadow.Sets.AsPath.Unused',
                [], [],
                '''                All objects of a given type that are not
                referenced at all
                ''',
                'unused',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('inactive', REFERENCE_CLASS, 'Inactive', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper', 'RoutingPolicyShadow.Sets.AsPath.Inactive',
                [], [],
                '''                All objects of a given type that are not
                attached to a protocol
                ''',
                'inactive',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('active', REFERENCE_CLASS, 'Active', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper', 'RoutingPolicyShadow.Sets.AsPath.Active',
                [], [],
                '''                All objects of a given type that are attached to
                a protocol
                ''',
                'active',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            ],
            'Cisco-IOS-XR-policy-repository-oper',
            'as-path',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-policy-repository-oper'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper',
            is_config=False,
        ),
    },
    'RoutingPolicyShadow.Sets.LargeCommunity.Sets_.Set.UsedBy.Reference' : {
        'meta_info' : _MetaInfoClass('RoutingPolicyShadow.Sets.LargeCommunity.Sets_.Set.UsedBy.Reference', REFERENCE_LIST,
            '''Information about policies referring to this
object''',
            False, 
            [
            _MetaInfoClassMember('route-policy-name', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                Name of policy
                ''',
                'route_policy_name',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('used-directly', ATTRIBUTE, 'bool', 'boolean',
                None, None,
                [], [],
                '''                Whether the policy uses this object directly or
                indirectly
                ''',
                'used_directly',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('status', REFERENCE_ENUM_CLASS, 'ObjectStatus', 'Object-status',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper', 'ObjectStatus',
                [], [],
                '''                Active, Inactive, or Unused
                ''',
                'status',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            ],
            'Cisco-IOS-XR-policy-repository-oper',
            'reference',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-policy-repository-oper'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper',
            is_config=False,
        ),
    },
    'RoutingPolicyShadow.Sets.LargeCommunity.Sets_.Set.UsedBy' : {
        'meta_info' : _MetaInfoClass('RoutingPolicyShadow.Sets.LargeCommunity.Sets_.Set.UsedBy', REFERENCE_CLASS,
            '''Policies that use this object, directly or
indirectly''',
            False, 
            [
            _MetaInfoClassMember('reference', REFERENCE_LIST, 'Reference', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper', 'RoutingPolicyShadow.Sets.LargeCommunity.Sets_.Set.UsedBy.Reference',
                [], [],
                '''                Information about policies referring to this
                object
                ''',
                'reference',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            ],
            'Cisco-IOS-XR-policy-repository-oper',
            'used-by',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-policy-repository-oper'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper',
            is_config=False,
        ),
    },
    'RoutingPolicyShadow.Sets.LargeCommunity.Sets_.Set.Attached.Binding' : {
        'meta_info' : _MetaInfoClass('RoutingPolicyShadow.Sets.LargeCommunity.Sets_.Set.Attached.Binding', REFERENCE_LIST,
            '''bindings list''',
            False, 
            [
            _MetaInfoClassMember('protocol', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                Protocol to which policy attached
                ''',
                'protocol',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('vrf-name', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                VRF name
                ''',
                'vrf_name',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('proto-instance', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                Protocol instance
                ''',
                'proto_instance',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('af-name', REFERENCE_ENUM_CLASS, 'AddressFamily', 'Address-family',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper', 'AddressFamily',
                [], [],
                '''                Address Family Identifier
                ''',
                'af_name',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('saf-name', REFERENCE_ENUM_CLASS, 'SubAddressFamily', 'Sub-address-family',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper', 'SubAddressFamily',
                [], [],
                '''                Subsequent Address Family Identifier
                ''',
                'saf_name',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('neighbor-address', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                Neighbor IP Address
                ''',
                'neighbor_address',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('neighbor-af-name', REFERENCE_ENUM_CLASS, 'AddressFamily', 'Address-family',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper', 'AddressFamily',
                [], [],
                '''                Neighbor IP Address Family
                ''',
                'neighbor_af_name',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('group-name', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                Neighbor Group Name
                ''',
                'group_name',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('direction', REFERENCE_ENUM_CLASS, 'AttachPointDirection', 'Attach-point-direction',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper', 'AttachPointDirection',
                [], [],
                '''                Direction In or Out
                ''',
                'direction',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('group', REFERENCE_ENUM_CLASS, 'Group', 'Group',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper', 'Group',
                [], [],
                '''                Neighbor Group 
                ''',
                'group',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('source-protocol', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                Source Protocol to redistribute, Source Protocol
                can be one of the following values{all,
                connected, local, static, bgp, rip, isis, ospf
                ,ospfv3, eigrp, unknown }
                ''',
                'source_protocol',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('aggregate-network-address', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                Aggregate IP address or Network IP Address in
                IPv4 or IPv6 Format
                ''',
                'aggregate_network_address',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('interface-name', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                Interface Name
                ''',
                'interface_name',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('instance', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                Instance
                ''',
                'instance',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('area-id', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                OSPF Area ID in Decimal Integer Format
                ''',
                'area_id',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('propogate-from', ATTRIBUTE, 'int', 'int32',
                None, None,
                [('-2147483648', '2147483647')], [],
                '''                ISIS Propogate From Level
                ''',
                'propogate_from',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('propogate-to', ATTRIBUTE, 'int', 'int32',
                None, None,
                [('-2147483648', '2147483647')], [],
                '''                ISIS Propogate To Level
                ''',
                'propogate_to',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('route-policy-name', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                Policy that uses object in question
                ''',
                'route_policy_name',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('attached-policy', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                The attached policy that (maybe indirectly) uses
                the object in question
                ''',
                'attached_policy',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('attach-point', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                Name of attach point where policy is attached
                ''',
                'attach_point',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            ],
            'Cisco-IOS-XR-policy-repository-oper',
            'binding',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-policy-repository-oper'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper',
            is_config=False,
        ),
    },
    'RoutingPolicyShadow.Sets.LargeCommunity.Sets_.Set.Attached' : {
        'meta_info' : _MetaInfoClass('RoutingPolicyShadow.Sets.LargeCommunity.Sets_.Set.Attached', REFERENCE_CLASS,
            '''Information about where this policy or set is
attached''',
            False, 
            [
            _MetaInfoClassMember('binding', REFERENCE_LIST, 'Binding', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper', 'RoutingPolicyShadow.Sets.LargeCommunity.Sets_.Set.Attached.Binding',
                [], [],
                '''                bindings list
                ''',
                'binding',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            ],
            'Cisco-IOS-XR-policy-repository-oper',
            'attached',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-policy-repository-oper'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper',
            is_config=False,
        ),
    },
    'RoutingPolicyShadow.Sets.LargeCommunity.Sets_.Set' : {
        'meta_info' : _MetaInfoClass('RoutingPolicyShadow.Sets.LargeCommunity.Sets_.Set', REFERENCE_LIST,
            '''Information about an individual set''',
            False, 
            [
            _MetaInfoClassMember('set-name', ATTRIBUTE, 'str', 'xr:Cisco-ios-xr-string',
                None, None,
                [], [b'[\\w\\-\\.:,_@#%$\\+=\\|;]+'],
                '''                Set name
                ''',
                'set_name',
                'Cisco-IOS-XR-policy-repository-oper', True, is_config=False),
            _MetaInfoClassMember('used-by', REFERENCE_CLASS, 'UsedBy', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper', 'RoutingPolicyShadow.Sets.LargeCommunity.Sets_.Set.UsedBy',
                [], [],
                '''                Policies that use this object, directly or
                indirectly
                ''',
                'used_by',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('attached', REFERENCE_CLASS, 'Attached', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper', 'RoutingPolicyShadow.Sets.LargeCommunity.Sets_.Set.Attached',
                [], [],
                '''                Information about where this policy or set is
                attached
                ''',
                'attached',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            ],
            'Cisco-IOS-XR-policy-repository-oper',
            'set',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-policy-repository-oper'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper',
            is_config=False,
        ),
    },
    'RoutingPolicyShadow.Sets.LargeCommunity.Sets_' : {
        'meta_info' : _MetaInfoClass('RoutingPolicyShadow.Sets.LargeCommunity.Sets_', REFERENCE_CLASS,
            '''Information about individual sets''',
            False, 
            [
            _MetaInfoClassMember('set', REFERENCE_LIST, 'Set', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper', 'RoutingPolicyShadow.Sets.LargeCommunity.Sets_.Set',
                [], [],
                '''                Information about an individual set
                ''',
                'set',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            ],
            'Cisco-IOS-XR-policy-repository-oper',
            'sets',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-policy-repository-oper'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper',
            is_config=False,
        ),
    },
    'RoutingPolicyShadow.Sets.LargeCommunity.Unused' : {
        'meta_info' : _MetaInfoClass('RoutingPolicyShadow.Sets.LargeCommunity.Unused', REFERENCE_CLASS,
            '''All objects of a given type that are not
referenced at all''',
            False, 
            [
            _MetaInfoClassMember('object', REFERENCE_LEAFLIST, 'str', 'String',
                None, None,
                [], [],
                '''                Policy objects
                ''',
                'object',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            ],
            'Cisco-IOS-XR-policy-repository-oper',
            'unused',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-policy-repository-oper'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper',
            is_config=False,
        ),
    },
    'RoutingPolicyShadow.Sets.LargeCommunity.Inactive' : {
        'meta_info' : _MetaInfoClass('RoutingPolicyShadow.Sets.LargeCommunity.Inactive', REFERENCE_CLASS,
            '''All objects of a given type that are not
attached to a protocol''',
            False, 
            [
            _MetaInfoClassMember('object', REFERENCE_LEAFLIST, 'str', 'String',
                None, None,
                [], [],
                '''                Policy objects
                ''',
                'object',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            ],
            'Cisco-IOS-XR-policy-repository-oper',
            'inactive',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-policy-repository-oper'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper',
            is_config=False,
        ),
    },
    'RoutingPolicyShadow.Sets.LargeCommunity.Active' : {
        'meta_info' : _MetaInfoClass('RoutingPolicyShadow.Sets.LargeCommunity.Active', REFERENCE_CLASS,
            '''All objects of a given type that are attached to
a protocol''',
            False, 
            [
            _MetaInfoClassMember('object', REFERENCE_LEAFLIST, 'str', 'String',
                None, None,
                [], [],
                '''                Policy objects
                ''',
                'object',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            ],
            'Cisco-IOS-XR-policy-repository-oper',
            'active',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-policy-repository-oper'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper',
            is_config=False,
        ),
    },
    'RoutingPolicyShadow.Sets.LargeCommunity' : {
        'meta_info' : _MetaInfoClass('RoutingPolicyShadow.Sets.LargeCommunity', REFERENCE_CLASS,
            '''Information about Large Community sets''',
            False, 
            [
            _MetaInfoClassMember('sets', REFERENCE_CLASS, 'Sets_', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper', 'RoutingPolicyShadow.Sets.LargeCommunity.Sets_',
                [], [],
                '''                Information about individual sets
                ''',
                'sets',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('unused', REFERENCE_CLASS, 'Unused', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper', 'RoutingPolicyShadow.Sets.LargeCommunity.Unused',
                [], [],
                '''                All objects of a given type that are not
                referenced at all
                ''',
                'unused',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('inactive', REFERENCE_CLASS, 'Inactive', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper', 'RoutingPolicyShadow.Sets.LargeCommunity.Inactive',
                [], [],
                '''                All objects of a given type that are not
                attached to a protocol
                ''',
                'inactive',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('active', REFERENCE_CLASS, 'Active', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper', 'RoutingPolicyShadow.Sets.LargeCommunity.Active',
                [], [],
                '''                All objects of a given type that are attached to
                a protocol
                ''',
                'active',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            ],
            'Cisco-IOS-XR-policy-repository-oper',
            'large-community',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-policy-repository-oper'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper',
            is_config=False,
        ),
    },
    'RoutingPolicyShadow.Sets.Esi.Sets_.Set.UsedBy.Reference' : {
        'meta_info' : _MetaInfoClass('RoutingPolicyShadow.Sets.Esi.Sets_.Set.UsedBy.Reference', REFERENCE_LIST,
            '''Information about policies referring to this
object''',
            False, 
            [
            _MetaInfoClassMember('route-policy-name', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                Name of policy
                ''',
                'route_policy_name',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('used-directly', ATTRIBUTE, 'bool', 'boolean',
                None, None,
                [], [],
                '''                Whether the policy uses this object directly or
                indirectly
                ''',
                'used_directly',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('status', REFERENCE_ENUM_CLASS, 'ObjectStatus', 'Object-status',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper', 'ObjectStatus',
                [], [],
                '''                Active, Inactive, or Unused
                ''',
                'status',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            ],
            'Cisco-IOS-XR-policy-repository-oper',
            'reference',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-policy-repository-oper'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper',
            is_config=False,
        ),
    },
    'RoutingPolicyShadow.Sets.Esi.Sets_.Set.UsedBy' : {
        'meta_info' : _MetaInfoClass('RoutingPolicyShadow.Sets.Esi.Sets_.Set.UsedBy', REFERENCE_CLASS,
            '''Policies that use this object, directly or
indirectly''',
            False, 
            [
            _MetaInfoClassMember('reference', REFERENCE_LIST, 'Reference', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper', 'RoutingPolicyShadow.Sets.Esi.Sets_.Set.UsedBy.Reference',
                [], [],
                '''                Information about policies referring to this
                object
                ''',
                'reference',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            ],
            'Cisco-IOS-XR-policy-repository-oper',
            'used-by',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-policy-repository-oper'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper',
            is_config=False,
        ),
    },
    'RoutingPolicyShadow.Sets.Esi.Sets_.Set.Attached.Binding' : {
        'meta_info' : _MetaInfoClass('RoutingPolicyShadow.Sets.Esi.Sets_.Set.Attached.Binding', REFERENCE_LIST,
            '''bindings list''',
            False, 
            [
            _MetaInfoClassMember('protocol', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                Protocol to which policy attached
                ''',
                'protocol',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('vrf-name', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                VRF name
                ''',
                'vrf_name',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('proto-instance', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                Protocol instance
                ''',
                'proto_instance',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('af-name', REFERENCE_ENUM_CLASS, 'AddressFamily', 'Address-family',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper', 'AddressFamily',
                [], [],
                '''                Address Family Identifier
                ''',
                'af_name',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('saf-name', REFERENCE_ENUM_CLASS, 'SubAddressFamily', 'Sub-address-family',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper', 'SubAddressFamily',
                [], [],
                '''                Subsequent Address Family Identifier
                ''',
                'saf_name',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('neighbor-address', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                Neighbor IP Address
                ''',
                'neighbor_address',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('neighbor-af-name', REFERENCE_ENUM_CLASS, 'AddressFamily', 'Address-family',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper', 'AddressFamily',
                [], [],
                '''                Neighbor IP Address Family
                ''',
                'neighbor_af_name',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('group-name', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                Neighbor Group Name
                ''',
                'group_name',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('direction', REFERENCE_ENUM_CLASS, 'AttachPointDirection', 'Attach-point-direction',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper', 'AttachPointDirection',
                [], [],
                '''                Direction In or Out
                ''',
                'direction',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('group', REFERENCE_ENUM_CLASS, 'Group', 'Group',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper', 'Group',
                [], [],
                '''                Neighbor Group 
                ''',
                'group',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('source-protocol', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                Source Protocol to redistribute, Source Protocol
                can be one of the following values{all,
                connected, local, static, bgp, rip, isis, ospf
                ,ospfv3, eigrp, unknown }
                ''',
                'source_protocol',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('aggregate-network-address', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                Aggregate IP address or Network IP Address in
                IPv4 or IPv6 Format
                ''',
                'aggregate_network_address',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('interface-name', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                Interface Name
                ''',
                'interface_name',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('instance', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                Instance
                ''',
                'instance',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('area-id', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                OSPF Area ID in Decimal Integer Format
                ''',
                'area_id',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('propogate-from', ATTRIBUTE, 'int', 'int32',
                None, None,
                [('-2147483648', '2147483647')], [],
                '''                ISIS Propogate From Level
                ''',
                'propogate_from',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('propogate-to', ATTRIBUTE, 'int', 'int32',
                None, None,
                [('-2147483648', '2147483647')], [],
                '''                ISIS Propogate To Level
                ''',
                'propogate_to',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('route-policy-name', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                Policy that uses object in question
                ''',
                'route_policy_name',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('attached-policy', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                The attached policy that (maybe indirectly) uses
                the object in question
                ''',
                'attached_policy',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('attach-point', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                Name of attach point where policy is attached
                ''',
                'attach_point',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            ],
            'Cisco-IOS-XR-policy-repository-oper',
            'binding',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-policy-repository-oper'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper',
            is_config=False,
        ),
    },
    'RoutingPolicyShadow.Sets.Esi.Sets_.Set.Attached' : {
        'meta_info' : _MetaInfoClass('RoutingPolicyShadow.Sets.Esi.Sets_.Set.Attached', REFERENCE_CLASS,
            '''Information about where this policy or set is
attached''',
            False, 
            [
            _MetaInfoClassMember('binding', REFERENCE_LIST, 'Binding', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper', 'RoutingPolicyShadow.Sets.Esi.Sets_.Set.Attached.Binding',
                [], [],
                '''                bindings list
                ''',
                'binding',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            ],
            'Cisco-IOS-XR-policy-repository-oper',
            'attached',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-policy-repository-oper'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper',
            is_config=False,
        ),
    },
    'RoutingPolicyShadow.Sets.Esi.Sets_.Set' : {
        'meta_info' : _MetaInfoClass('RoutingPolicyShadow.Sets.Esi.Sets_.Set', REFERENCE_LIST,
            '''Information about an individual set''',
            False, 
            [
            _MetaInfoClassMember('set-name', ATTRIBUTE, 'str', 'xr:Cisco-ios-xr-string',
                None, None,
                [], [b'[\\w\\-\\.:,_@#%$\\+=\\|;]+'],
                '''                Set name
                ''',
                'set_name',
                'Cisco-IOS-XR-policy-repository-oper', True, is_config=False),
            _MetaInfoClassMember('used-by', REFERENCE_CLASS, 'UsedBy', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper', 'RoutingPolicyShadow.Sets.Esi.Sets_.Set.UsedBy',
                [], [],
                '''                Policies that use this object, directly or
                indirectly
                ''',
                'used_by',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('attached', REFERENCE_CLASS, 'Attached', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper', 'RoutingPolicyShadow.Sets.Esi.Sets_.Set.Attached',
                [], [],
                '''                Information about where this policy or set is
                attached
                ''',
                'attached',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            ],
            'Cisco-IOS-XR-policy-repository-oper',
            'set',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-policy-repository-oper'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper',
            is_config=False,
        ),
    },
    'RoutingPolicyShadow.Sets.Esi.Sets_' : {
        'meta_info' : _MetaInfoClass('RoutingPolicyShadow.Sets.Esi.Sets_', REFERENCE_CLASS,
            '''Information about individual sets''',
            False, 
            [
            _MetaInfoClassMember('set', REFERENCE_LIST, 'Set', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper', 'RoutingPolicyShadow.Sets.Esi.Sets_.Set',
                [], [],
                '''                Information about an individual set
                ''',
                'set',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            ],
            'Cisco-IOS-XR-policy-repository-oper',
            'sets',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-policy-repository-oper'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper',
            is_config=False,
        ),
    },
    'RoutingPolicyShadow.Sets.Esi.Unused' : {
        'meta_info' : _MetaInfoClass('RoutingPolicyShadow.Sets.Esi.Unused', REFERENCE_CLASS,
            '''All objects of a given type that are not
referenced at all''',
            False, 
            [
            _MetaInfoClassMember('object', REFERENCE_LEAFLIST, 'str', 'String',
                None, None,
                [], [],
                '''                Policy objects
                ''',
                'object',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            ],
            'Cisco-IOS-XR-policy-repository-oper',
            'unused',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-policy-repository-oper'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper',
            is_config=False,
        ),
    },
    'RoutingPolicyShadow.Sets.Esi.Inactive' : {
        'meta_info' : _MetaInfoClass('RoutingPolicyShadow.Sets.Esi.Inactive', REFERENCE_CLASS,
            '''All objects of a given type that are not
attached to a protocol''',
            False, 
            [
            _MetaInfoClassMember('object', REFERENCE_LEAFLIST, 'str', 'String',
                None, None,
                [], [],
                '''                Policy objects
                ''',
                'object',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            ],
            'Cisco-IOS-XR-policy-repository-oper',
            'inactive',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-policy-repository-oper'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper',
            is_config=False,
        ),
    },
    'RoutingPolicyShadow.Sets.Esi.Active' : {
        'meta_info' : _MetaInfoClass('RoutingPolicyShadow.Sets.Esi.Active', REFERENCE_CLASS,
            '''All objects of a given type that are attached to
a protocol''',
            False, 
            [
            _MetaInfoClassMember('object', REFERENCE_LEAFLIST, 'str', 'String',
                None, None,
                [], [],
                '''                Policy objects
                ''',
                'object',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            ],
            'Cisco-IOS-XR-policy-repository-oper',
            'active',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-policy-repository-oper'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper',
            is_config=False,
        ),
    },
    'RoutingPolicyShadow.Sets.Esi' : {
        'meta_info' : _MetaInfoClass('RoutingPolicyShadow.Sets.Esi', REFERENCE_CLASS,
            '''Information about Esi sets''',
            False, 
            [
            _MetaInfoClassMember('sets', REFERENCE_CLASS, 'Sets_', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper', 'RoutingPolicyShadow.Sets.Esi.Sets_',
                [], [],
                '''                Information about individual sets
                ''',
                'sets',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('unused', REFERENCE_CLASS, 'Unused', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper', 'RoutingPolicyShadow.Sets.Esi.Unused',
                [], [],
                '''                All objects of a given type that are not
                referenced at all
                ''',
                'unused',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('inactive', REFERENCE_CLASS, 'Inactive', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper', 'RoutingPolicyShadow.Sets.Esi.Inactive',
                [], [],
                '''                All objects of a given type that are not
                attached to a protocol
                ''',
                'inactive',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('active', REFERENCE_CLASS, 'Active', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper', 'RoutingPolicyShadow.Sets.Esi.Active',
                [], [],
                '''                All objects of a given type that are attached to
                a protocol
                ''',
                'active',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            ],
            'Cisco-IOS-XR-policy-repository-oper',
            'esi',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-policy-repository-oper'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper',
            is_config=False,
        ),
    },
    'RoutingPolicyShadow.Sets.ExtendedCommunityBandwidth.Sets_.Set.UsedBy.Reference' : {
        'meta_info' : _MetaInfoClass('RoutingPolicyShadow.Sets.ExtendedCommunityBandwidth.Sets_.Set.UsedBy.Reference', REFERENCE_LIST,
            '''Information about policies referring to this
object''',
            False, 
            [
            _MetaInfoClassMember('route-policy-name', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                Name of policy
                ''',
                'route_policy_name',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('used-directly', ATTRIBUTE, 'bool', 'boolean',
                None, None,
                [], [],
                '''                Whether the policy uses this object directly or
                indirectly
                ''',
                'used_directly',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('status', REFERENCE_ENUM_CLASS, 'ObjectStatus', 'Object-status',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper', 'ObjectStatus',
                [], [],
                '''                Active, Inactive, or Unused
                ''',
                'status',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            ],
            'Cisco-IOS-XR-policy-repository-oper',
            'reference',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-policy-repository-oper'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper',
            is_config=False,
        ),
    },
    'RoutingPolicyShadow.Sets.ExtendedCommunityBandwidth.Sets_.Set.UsedBy' : {
        'meta_info' : _MetaInfoClass('RoutingPolicyShadow.Sets.ExtendedCommunityBandwidth.Sets_.Set.UsedBy', REFERENCE_CLASS,
            '''Policies that use this object, directly or
indirectly''',
            False, 
            [
            _MetaInfoClassMember('reference', REFERENCE_LIST, 'Reference', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper', 'RoutingPolicyShadow.Sets.ExtendedCommunityBandwidth.Sets_.Set.UsedBy.Reference',
                [], [],
                '''                Information about policies referring to this
                object
                ''',
                'reference',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            ],
            'Cisco-IOS-XR-policy-repository-oper',
            'used-by',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-policy-repository-oper'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper',
            is_config=False,
        ),
    },
    'RoutingPolicyShadow.Sets.ExtendedCommunityBandwidth.Sets_.Set.Attached.Binding' : {
        'meta_info' : _MetaInfoClass('RoutingPolicyShadow.Sets.ExtendedCommunityBandwidth.Sets_.Set.Attached.Binding', REFERENCE_LIST,
            '''bindings list''',
            False, 
            [
            _MetaInfoClassMember('protocol', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                Protocol to which policy attached
                ''',
                'protocol',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('vrf-name', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                VRF name
                ''',
                'vrf_name',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('proto-instance', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                Protocol instance
                ''',
                'proto_instance',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('af-name', REFERENCE_ENUM_CLASS, 'AddressFamily', 'Address-family',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper', 'AddressFamily',
                [], [],
                '''                Address Family Identifier
                ''',
                'af_name',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('saf-name', REFERENCE_ENUM_CLASS, 'SubAddressFamily', 'Sub-address-family',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper', 'SubAddressFamily',
                [], [],
                '''                Subsequent Address Family Identifier
                ''',
                'saf_name',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('neighbor-address', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                Neighbor IP Address
                ''',
                'neighbor_address',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('neighbor-af-name', REFERENCE_ENUM_CLASS, 'AddressFamily', 'Address-family',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper', 'AddressFamily',
                [], [],
                '''                Neighbor IP Address Family
                ''',
                'neighbor_af_name',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('group-name', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                Neighbor Group Name
                ''',
                'group_name',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('direction', REFERENCE_ENUM_CLASS, 'AttachPointDirection', 'Attach-point-direction',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper', 'AttachPointDirection',
                [], [],
                '''                Direction In or Out
                ''',
                'direction',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('group', REFERENCE_ENUM_CLASS, 'Group', 'Group',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper', 'Group',
                [], [],
                '''                Neighbor Group 
                ''',
                'group',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('source-protocol', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                Source Protocol to redistribute, Source Protocol
                can be one of the following values{all,
                connected, local, static, bgp, rip, isis, ospf
                ,ospfv3, eigrp, unknown }
                ''',
                'source_protocol',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('aggregate-network-address', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                Aggregate IP address or Network IP Address in
                IPv4 or IPv6 Format
                ''',
                'aggregate_network_address',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('interface-name', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                Interface Name
                ''',
                'interface_name',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('instance', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                Instance
                ''',
                'instance',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('area-id', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                OSPF Area ID in Decimal Integer Format
                ''',
                'area_id',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('propogate-from', ATTRIBUTE, 'int', 'int32',
                None, None,
                [('-2147483648', '2147483647')], [],
                '''                ISIS Propogate From Level
                ''',
                'propogate_from',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('propogate-to', ATTRIBUTE, 'int', 'int32',
                None, None,
                [('-2147483648', '2147483647')], [],
                '''                ISIS Propogate To Level
                ''',
                'propogate_to',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('route-policy-name', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                Policy that uses object in question
                ''',
                'route_policy_name',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('attached-policy', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                The attached policy that (maybe indirectly) uses
                the object in question
                ''',
                'attached_policy',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('attach-point', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                Name of attach point where policy is attached
                ''',
                'attach_point',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            ],
            'Cisco-IOS-XR-policy-repository-oper',
            'binding',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-policy-repository-oper'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper',
            is_config=False,
        ),
    },
    'RoutingPolicyShadow.Sets.ExtendedCommunityBandwidth.Sets_.Set.Attached' : {
        'meta_info' : _MetaInfoClass('RoutingPolicyShadow.Sets.ExtendedCommunityBandwidth.Sets_.Set.Attached', REFERENCE_CLASS,
            '''Information about where this policy or set is
attached''',
            False, 
            [
            _MetaInfoClassMember('binding', REFERENCE_LIST, 'Binding', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper', 'RoutingPolicyShadow.Sets.ExtendedCommunityBandwidth.Sets_.Set.Attached.Binding',
                [], [],
                '''                bindings list
                ''',
                'binding',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            ],
            'Cisco-IOS-XR-policy-repository-oper',
            'attached',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-policy-repository-oper'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper',
            is_config=False,
        ),
    },
    'RoutingPolicyShadow.Sets.ExtendedCommunityBandwidth.Sets_.Set' : {
        'meta_info' : _MetaInfoClass('RoutingPolicyShadow.Sets.ExtendedCommunityBandwidth.Sets_.Set', REFERENCE_LIST,
            '''Information about an individual set''',
            False, 
            [
            _MetaInfoClassMember('set-name', ATTRIBUTE, 'str', 'xr:Cisco-ios-xr-string',
                None, None,
                [], [b'[\\w\\-\\.:,_@#%$\\+=\\|;]+'],
                '''                Set name
                ''',
                'set_name',
                'Cisco-IOS-XR-policy-repository-oper', True, is_config=False),
            _MetaInfoClassMember('used-by', REFERENCE_CLASS, 'UsedBy', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper', 'RoutingPolicyShadow.Sets.ExtendedCommunityBandwidth.Sets_.Set.UsedBy',
                [], [],
                '''                Policies that use this object, directly or
                indirectly
                ''',
                'used_by',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('attached', REFERENCE_CLASS, 'Attached', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper', 'RoutingPolicyShadow.Sets.ExtendedCommunityBandwidth.Sets_.Set.Attached',
                [], [],
                '''                Information about where this policy or set is
                attached
                ''',
                'attached',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            ],
            'Cisco-IOS-XR-policy-repository-oper',
            'set',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-policy-repository-oper'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper',
            is_config=False,
        ),
    },
    'RoutingPolicyShadow.Sets.ExtendedCommunityBandwidth.Sets_' : {
        'meta_info' : _MetaInfoClass('RoutingPolicyShadow.Sets.ExtendedCommunityBandwidth.Sets_', REFERENCE_CLASS,
            '''Information about individual sets''',
            False, 
            [
            _MetaInfoClassMember('set', REFERENCE_LIST, 'Set', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper', 'RoutingPolicyShadow.Sets.ExtendedCommunityBandwidth.Sets_.Set',
                [], [],
                '''                Information about an individual set
                ''',
                'set',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            ],
            'Cisco-IOS-XR-policy-repository-oper',
            'sets',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-policy-repository-oper'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper',
            is_config=False,
        ),
    },
    'RoutingPolicyShadow.Sets.ExtendedCommunityBandwidth.Unused' : {
        'meta_info' : _MetaInfoClass('RoutingPolicyShadow.Sets.ExtendedCommunityBandwidth.Unused', REFERENCE_CLASS,
            '''All objects of a given type that are not
referenced at all''',
            False, 
            [
            _MetaInfoClassMember('object', REFERENCE_LEAFLIST, 'str', 'String',
                None, None,
                [], [],
                '''                Policy objects
                ''',
                'object',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            ],
            'Cisco-IOS-XR-policy-repository-oper',
            'unused',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-policy-repository-oper'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper',
            is_config=False,
        ),
    },
    'RoutingPolicyShadow.Sets.ExtendedCommunityBandwidth.Inactive' : {
        'meta_info' : _MetaInfoClass('RoutingPolicyShadow.Sets.ExtendedCommunityBandwidth.Inactive', REFERENCE_CLASS,
            '''All objects of a given type that are not
attached to a protocol''',
            False, 
            [
            _MetaInfoClassMember('object', REFERENCE_LEAFLIST, 'str', 'String',
                None, None,
                [], [],
                '''                Policy objects
                ''',
                'object',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            ],
            'Cisco-IOS-XR-policy-repository-oper',
            'inactive',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-policy-repository-oper'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper',
            is_config=False,
        ),
    },
    'RoutingPolicyShadow.Sets.ExtendedCommunityBandwidth' : {
        'meta_info' : _MetaInfoClass('RoutingPolicyShadow.Sets.ExtendedCommunityBandwidth', REFERENCE_CLASS,
            '''Information about Extended Community Bandwidth
sets''',
            False, 
            [
            _MetaInfoClassMember('sets', REFERENCE_CLASS, 'Sets_', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper', 'RoutingPolicyShadow.Sets.ExtendedCommunityBandwidth.Sets_',
                [], [],
                '''                Information about individual sets
                ''',
                'sets',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('unused', REFERENCE_CLASS, 'Unused', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper', 'RoutingPolicyShadow.Sets.ExtendedCommunityBandwidth.Unused',
                [], [],
                '''                All objects of a given type that are not
                referenced at all
                ''',
                'unused',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('inactive', REFERENCE_CLASS, 'Inactive', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper', 'RoutingPolicyShadow.Sets.ExtendedCommunityBandwidth.Inactive',
                [], [],
                '''                All objects of a given type that are not
                attached to a protocol
                ''',
                'inactive',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            ],
            'Cisco-IOS-XR-policy-repository-oper',
            'extended-community-bandwidth',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-policy-repository-oper'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper',
            is_config=False,
        ),
    },
    'RoutingPolicyShadow.Sets.ExtendedCommunityRt.Sets_.Set.UsedBy.Reference' : {
        'meta_info' : _MetaInfoClass('RoutingPolicyShadow.Sets.ExtendedCommunityRt.Sets_.Set.UsedBy.Reference', REFERENCE_LIST,
            '''Information about policies referring to this
object''',
            False, 
            [
            _MetaInfoClassMember('route-policy-name', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                Name of policy
                ''',
                'route_policy_name',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('used-directly', ATTRIBUTE, 'bool', 'boolean',
                None, None,
                [], [],
                '''                Whether the policy uses this object directly or
                indirectly
                ''',
                'used_directly',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('status', REFERENCE_ENUM_CLASS, 'ObjectStatus', 'Object-status',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper', 'ObjectStatus',
                [], [],
                '''                Active, Inactive, or Unused
                ''',
                'status',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            ],
            'Cisco-IOS-XR-policy-repository-oper',
            'reference',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-policy-repository-oper'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper',
            is_config=False,
        ),
    },
    'RoutingPolicyShadow.Sets.ExtendedCommunityRt.Sets_.Set.UsedBy' : {
        'meta_info' : _MetaInfoClass('RoutingPolicyShadow.Sets.ExtendedCommunityRt.Sets_.Set.UsedBy', REFERENCE_CLASS,
            '''Policies that use this object, directly or
indirectly''',
            False, 
            [
            _MetaInfoClassMember('reference', REFERENCE_LIST, 'Reference', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper', 'RoutingPolicyShadow.Sets.ExtendedCommunityRt.Sets_.Set.UsedBy.Reference',
                [], [],
                '''                Information about policies referring to this
                object
                ''',
                'reference',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            ],
            'Cisco-IOS-XR-policy-repository-oper',
            'used-by',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-policy-repository-oper'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper',
            is_config=False,
        ),
    },
    'RoutingPolicyShadow.Sets.ExtendedCommunityRt.Sets_.Set.Attached.Binding' : {
        'meta_info' : _MetaInfoClass('RoutingPolicyShadow.Sets.ExtendedCommunityRt.Sets_.Set.Attached.Binding', REFERENCE_LIST,
            '''bindings list''',
            False, 
            [
            _MetaInfoClassMember('protocol', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                Protocol to which policy attached
                ''',
                'protocol',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('vrf-name', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                VRF name
                ''',
                'vrf_name',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('proto-instance', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                Protocol instance
                ''',
                'proto_instance',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('af-name', REFERENCE_ENUM_CLASS, 'AddressFamily', 'Address-family',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper', 'AddressFamily',
                [], [],
                '''                Address Family Identifier
                ''',
                'af_name',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('saf-name', REFERENCE_ENUM_CLASS, 'SubAddressFamily', 'Sub-address-family',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper', 'SubAddressFamily',
                [], [],
                '''                Subsequent Address Family Identifier
                ''',
                'saf_name',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('neighbor-address', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                Neighbor IP Address
                ''',
                'neighbor_address',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('neighbor-af-name', REFERENCE_ENUM_CLASS, 'AddressFamily', 'Address-family',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper', 'AddressFamily',
                [], [],
                '''                Neighbor IP Address Family
                ''',
                'neighbor_af_name',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('group-name', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                Neighbor Group Name
                ''',
                'group_name',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('direction', REFERENCE_ENUM_CLASS, 'AttachPointDirection', 'Attach-point-direction',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper', 'AttachPointDirection',
                [], [],
                '''                Direction In or Out
                ''',
                'direction',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('group', REFERENCE_ENUM_CLASS, 'Group', 'Group',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper', 'Group',
                [], [],
                '''                Neighbor Group 
                ''',
                'group',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('source-protocol', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                Source Protocol to redistribute, Source Protocol
                can be one of the following values{all,
                connected, local, static, bgp, rip, isis, ospf
                ,ospfv3, eigrp, unknown }
                ''',
                'source_protocol',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('aggregate-network-address', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                Aggregate IP address or Network IP Address in
                IPv4 or IPv6 Format
                ''',
                'aggregate_network_address',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('interface-name', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                Interface Name
                ''',
                'interface_name',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('instance', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                Instance
                ''',
                'instance',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('area-id', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                OSPF Area ID in Decimal Integer Format
                ''',
                'area_id',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('propogate-from', ATTRIBUTE, 'int', 'int32',
                None, None,
                [('-2147483648', '2147483647')], [],
                '''                ISIS Propogate From Level
                ''',
                'propogate_from',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('propogate-to', ATTRIBUTE, 'int', 'int32',
                None, None,
                [('-2147483648', '2147483647')], [],
                '''                ISIS Propogate To Level
                ''',
                'propogate_to',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('route-policy-name', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                Policy that uses object in question
                ''',
                'route_policy_name',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('attached-policy', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                The attached policy that (maybe indirectly) uses
                the object in question
                ''',
                'attached_policy',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('attach-point', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                Name of attach point where policy is attached
                ''',
                'attach_point',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            ],
            'Cisco-IOS-XR-policy-repository-oper',
            'binding',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-policy-repository-oper'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper',
            is_config=False,
        ),
    },
    'RoutingPolicyShadow.Sets.ExtendedCommunityRt.Sets_.Set.Attached' : {
        'meta_info' : _MetaInfoClass('RoutingPolicyShadow.Sets.ExtendedCommunityRt.Sets_.Set.Attached', REFERENCE_CLASS,
            '''Information about where this policy or set is
attached''',
            False, 
            [
            _MetaInfoClassMember('binding', REFERENCE_LIST, 'Binding', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper', 'RoutingPolicyShadow.Sets.ExtendedCommunityRt.Sets_.Set.Attached.Binding',
                [], [],
                '''                bindings list
                ''',
                'binding',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            ],
            'Cisco-IOS-XR-policy-repository-oper',
            'attached',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-policy-repository-oper'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper',
            is_config=False,
        ),
    },
    'RoutingPolicyShadow.Sets.ExtendedCommunityRt.Sets_.Set' : {
        'meta_info' : _MetaInfoClass('RoutingPolicyShadow.Sets.ExtendedCommunityRt.Sets_.Set', REFERENCE_LIST,
            '''Information about an individual set''',
            False, 
            [
            _MetaInfoClassMember('set-name', ATTRIBUTE, 'str', 'xr:Cisco-ios-xr-string',
                None, None,
                [], [b'[\\w\\-\\.:,_@#%$\\+=\\|;]+'],
                '''                Set name
                ''',
                'set_name',
                'Cisco-IOS-XR-policy-repository-oper', True, is_config=False),
            _MetaInfoClassMember('used-by', REFERENCE_CLASS, 'UsedBy', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper', 'RoutingPolicyShadow.Sets.ExtendedCommunityRt.Sets_.Set.UsedBy',
                [], [],
                '''                Policies that use this object, directly or
                indirectly
                ''',
                'used_by',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('attached', REFERENCE_CLASS, 'Attached', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper', 'RoutingPolicyShadow.Sets.ExtendedCommunityRt.Sets_.Set.Attached',
                [], [],
                '''                Information about where this policy or set is
                attached
                ''',
                'attached',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            ],
            'Cisco-IOS-XR-policy-repository-oper',
            'set',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-policy-repository-oper'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper',
            is_config=False,
        ),
    },
    'RoutingPolicyShadow.Sets.ExtendedCommunityRt.Sets_' : {
        'meta_info' : _MetaInfoClass('RoutingPolicyShadow.Sets.ExtendedCommunityRt.Sets_', REFERENCE_CLASS,
            '''Information about individual sets''',
            False, 
            [
            _MetaInfoClassMember('set', REFERENCE_LIST, 'Set', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper', 'RoutingPolicyShadow.Sets.ExtendedCommunityRt.Sets_.Set',
                [], [],
                '''                Information about an individual set
                ''',
                'set',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            ],
            'Cisco-IOS-XR-policy-repository-oper',
            'sets',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-policy-repository-oper'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper',
            is_config=False,
        ),
    },
    'RoutingPolicyShadow.Sets.ExtendedCommunityRt.Unused' : {
        'meta_info' : _MetaInfoClass('RoutingPolicyShadow.Sets.ExtendedCommunityRt.Unused', REFERENCE_CLASS,
            '''All objects of a given type that are not
referenced at all''',
            False, 
            [
            _MetaInfoClassMember('object', REFERENCE_LEAFLIST, 'str', 'String',
                None, None,
                [], [],
                '''                Policy objects
                ''',
                'object',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            ],
            'Cisco-IOS-XR-policy-repository-oper',
            'unused',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-policy-repository-oper'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper',
            is_config=False,
        ),
    },
    'RoutingPolicyShadow.Sets.ExtendedCommunityRt.Inactive' : {
        'meta_info' : _MetaInfoClass('RoutingPolicyShadow.Sets.ExtendedCommunityRt.Inactive', REFERENCE_CLASS,
            '''All objects of a given type that are not
attached to a protocol''',
            False, 
            [
            _MetaInfoClassMember('object', REFERENCE_LEAFLIST, 'str', 'String',
                None, None,
                [], [],
                '''                Policy objects
                ''',
                'object',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            ],
            'Cisco-IOS-XR-policy-repository-oper',
            'inactive',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-policy-repository-oper'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper',
            is_config=False,
        ),
    },
    'RoutingPolicyShadow.Sets.ExtendedCommunityRt.Active' : {
        'meta_info' : _MetaInfoClass('RoutingPolicyShadow.Sets.ExtendedCommunityRt.Active', REFERENCE_CLASS,
            '''All objects of a given type that are attached to
a protocol''',
            False, 
            [
            _MetaInfoClassMember('object', REFERENCE_LEAFLIST, 'str', 'String',
                None, None,
                [], [],
                '''                Policy objects
                ''',
                'object',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            ],
            'Cisco-IOS-XR-policy-repository-oper',
            'active',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-policy-repository-oper'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper',
            is_config=False,
        ),
    },
    'RoutingPolicyShadow.Sets.ExtendedCommunityRt' : {
        'meta_info' : _MetaInfoClass('RoutingPolicyShadow.Sets.ExtendedCommunityRt', REFERENCE_CLASS,
            '''Information about Extended Community RT sets''',
            False, 
            [
            _MetaInfoClassMember('sets', REFERENCE_CLASS, 'Sets_', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper', 'RoutingPolicyShadow.Sets.ExtendedCommunityRt.Sets_',
                [], [],
                '''                Information about individual sets
                ''',
                'sets',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('unused', REFERENCE_CLASS, 'Unused', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper', 'RoutingPolicyShadow.Sets.ExtendedCommunityRt.Unused',
                [], [],
                '''                All objects of a given type that are not
                referenced at all
                ''',
                'unused',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('inactive', REFERENCE_CLASS, 'Inactive', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper', 'RoutingPolicyShadow.Sets.ExtendedCommunityRt.Inactive',
                [], [],
                '''                All objects of a given type that are not
                attached to a protocol
                ''',
                'inactive',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('active', REFERENCE_CLASS, 'Active', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper', 'RoutingPolicyShadow.Sets.ExtendedCommunityRt.Active',
                [], [],
                '''                All objects of a given type that are attached to
                a protocol
                ''',
                'active',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            ],
            'Cisco-IOS-XR-policy-repository-oper',
            'extended-community-rt',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-policy-repository-oper'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper',
            is_config=False,
        ),
    },
    'RoutingPolicyShadow.Sets.Rd.Sets_.Set.UsedBy.Reference' : {
        'meta_info' : _MetaInfoClass('RoutingPolicyShadow.Sets.Rd.Sets_.Set.UsedBy.Reference', REFERENCE_LIST,
            '''Information about policies referring to this
object''',
            False, 
            [
            _MetaInfoClassMember('route-policy-name', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                Name of policy
                ''',
                'route_policy_name',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('used-directly', ATTRIBUTE, 'bool', 'boolean',
                None, None,
                [], [],
                '''                Whether the policy uses this object directly or
                indirectly
                ''',
                'used_directly',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('status', REFERENCE_ENUM_CLASS, 'ObjectStatus', 'Object-status',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper', 'ObjectStatus',
                [], [],
                '''                Active, Inactive, or Unused
                ''',
                'status',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            ],
            'Cisco-IOS-XR-policy-repository-oper',
            'reference',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-policy-repository-oper'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper',
            is_config=False,
        ),
    },
    'RoutingPolicyShadow.Sets.Rd.Sets_.Set.UsedBy' : {
        'meta_info' : _MetaInfoClass('RoutingPolicyShadow.Sets.Rd.Sets_.Set.UsedBy', REFERENCE_CLASS,
            '''Policies that use this object, directly or
indirectly''',
            False, 
            [
            _MetaInfoClassMember('reference', REFERENCE_LIST, 'Reference', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper', 'RoutingPolicyShadow.Sets.Rd.Sets_.Set.UsedBy.Reference',
                [], [],
                '''                Information about policies referring to this
                object
                ''',
                'reference',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            ],
            'Cisco-IOS-XR-policy-repository-oper',
            'used-by',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-policy-repository-oper'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper',
            is_config=False,
        ),
    },
    'RoutingPolicyShadow.Sets.Rd.Sets_.Set.Attached.Binding' : {
        'meta_info' : _MetaInfoClass('RoutingPolicyShadow.Sets.Rd.Sets_.Set.Attached.Binding', REFERENCE_LIST,
            '''bindings list''',
            False, 
            [
            _MetaInfoClassMember('protocol', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                Protocol to which policy attached
                ''',
                'protocol',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('vrf-name', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                VRF name
                ''',
                'vrf_name',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('proto-instance', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                Protocol instance
                ''',
                'proto_instance',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('af-name', REFERENCE_ENUM_CLASS, 'AddressFamily', 'Address-family',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper', 'AddressFamily',
                [], [],
                '''                Address Family Identifier
                ''',
                'af_name',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('saf-name', REFERENCE_ENUM_CLASS, 'SubAddressFamily', 'Sub-address-family',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper', 'SubAddressFamily',
                [], [],
                '''                Subsequent Address Family Identifier
                ''',
                'saf_name',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('neighbor-address', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                Neighbor IP Address
                ''',
                'neighbor_address',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('neighbor-af-name', REFERENCE_ENUM_CLASS, 'AddressFamily', 'Address-family',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper', 'AddressFamily',
                [], [],
                '''                Neighbor IP Address Family
                ''',
                'neighbor_af_name',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('group-name', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                Neighbor Group Name
                ''',
                'group_name',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('direction', REFERENCE_ENUM_CLASS, 'AttachPointDirection', 'Attach-point-direction',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper', 'AttachPointDirection',
                [], [],
                '''                Direction In or Out
                ''',
                'direction',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('group', REFERENCE_ENUM_CLASS, 'Group', 'Group',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper', 'Group',
                [], [],
                '''                Neighbor Group 
                ''',
                'group',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('source-protocol', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                Source Protocol to redistribute, Source Protocol
                can be one of the following values{all,
                connected, local, static, bgp, rip, isis, ospf
                ,ospfv3, eigrp, unknown }
                ''',
                'source_protocol',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('aggregate-network-address', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                Aggregate IP address or Network IP Address in
                IPv4 or IPv6 Format
                ''',
                'aggregate_network_address',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('interface-name', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                Interface Name
                ''',
                'interface_name',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('instance', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                Instance
                ''',
                'instance',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('area-id', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                OSPF Area ID in Decimal Integer Format
                ''',
                'area_id',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('propogate-from', ATTRIBUTE, 'int', 'int32',
                None, None,
                [('-2147483648', '2147483647')], [],
                '''                ISIS Propogate From Level
                ''',
                'propogate_from',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('propogate-to', ATTRIBUTE, 'int', 'int32',
                None, None,
                [('-2147483648', '2147483647')], [],
                '''                ISIS Propogate To Level
                ''',
                'propogate_to',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('route-policy-name', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                Policy that uses object in question
                ''',
                'route_policy_name',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('attached-policy', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                The attached policy that (maybe indirectly) uses
                the object in question
                ''',
                'attached_policy',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('attach-point', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                Name of attach point where policy is attached
                ''',
                'attach_point',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            ],
            'Cisco-IOS-XR-policy-repository-oper',
            'binding',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-policy-repository-oper'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper',
            is_config=False,
        ),
    },
    'RoutingPolicyShadow.Sets.Rd.Sets_.Set.Attached' : {
        'meta_info' : _MetaInfoClass('RoutingPolicyShadow.Sets.Rd.Sets_.Set.Attached', REFERENCE_CLASS,
            '''Information about where this policy or set is
attached''',
            False, 
            [
            _MetaInfoClassMember('binding', REFERENCE_LIST, 'Binding', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper', 'RoutingPolicyShadow.Sets.Rd.Sets_.Set.Attached.Binding',
                [], [],
                '''                bindings list
                ''',
                'binding',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            ],
            'Cisco-IOS-XR-policy-repository-oper',
            'attached',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-policy-repository-oper'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper',
            is_config=False,
        ),
    },
    'RoutingPolicyShadow.Sets.Rd.Sets_.Set' : {
        'meta_info' : _MetaInfoClass('RoutingPolicyShadow.Sets.Rd.Sets_.Set', REFERENCE_LIST,
            '''Information about an individual set''',
            False, 
            [
            _MetaInfoClassMember('set-name', ATTRIBUTE, 'str', 'xr:Cisco-ios-xr-string',
                None, None,
                [], [b'[\\w\\-\\.:,_@#%$\\+=\\|;]+'],
                '''                Set name
                ''',
                'set_name',
                'Cisco-IOS-XR-policy-repository-oper', True, is_config=False),
            _MetaInfoClassMember('used-by', REFERENCE_CLASS, 'UsedBy', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper', 'RoutingPolicyShadow.Sets.Rd.Sets_.Set.UsedBy',
                [], [],
                '''                Policies that use this object, directly or
                indirectly
                ''',
                'used_by',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('attached', REFERENCE_CLASS, 'Attached', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper', 'RoutingPolicyShadow.Sets.Rd.Sets_.Set.Attached',
                [], [],
                '''                Information about where this policy or set is
                attached
                ''',
                'attached',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            ],
            'Cisco-IOS-XR-policy-repository-oper',
            'set',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-policy-repository-oper'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper',
            is_config=False,
        ),
    },
    'RoutingPolicyShadow.Sets.Rd.Sets_' : {
        'meta_info' : _MetaInfoClass('RoutingPolicyShadow.Sets.Rd.Sets_', REFERENCE_CLASS,
            '''Information about individual sets''',
            False, 
            [
            _MetaInfoClassMember('set', REFERENCE_LIST, 'Set', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper', 'RoutingPolicyShadow.Sets.Rd.Sets_.Set',
                [], [],
                '''                Information about an individual set
                ''',
                'set',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            ],
            'Cisco-IOS-XR-policy-repository-oper',
            'sets',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-policy-repository-oper'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper',
            is_config=False,
        ),
    },
    'RoutingPolicyShadow.Sets.Rd.Unused' : {
        'meta_info' : _MetaInfoClass('RoutingPolicyShadow.Sets.Rd.Unused', REFERENCE_CLASS,
            '''All objects of a given type that are not
referenced at all''',
            False, 
            [
            _MetaInfoClassMember('object', REFERENCE_LEAFLIST, 'str', 'String',
                None, None,
                [], [],
                '''                Policy objects
                ''',
                'object',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            ],
            'Cisco-IOS-XR-policy-repository-oper',
            'unused',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-policy-repository-oper'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper',
            is_config=False,
        ),
    },
    'RoutingPolicyShadow.Sets.Rd.Inactive' : {
        'meta_info' : _MetaInfoClass('RoutingPolicyShadow.Sets.Rd.Inactive', REFERENCE_CLASS,
            '''All objects of a given type that are not
attached to a protocol''',
            False, 
            [
            _MetaInfoClassMember('object', REFERENCE_LEAFLIST, 'str', 'String',
                None, None,
                [], [],
                '''                Policy objects
                ''',
                'object',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            ],
            'Cisco-IOS-XR-policy-repository-oper',
            'inactive',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-policy-repository-oper'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper',
            is_config=False,
        ),
    },
    'RoutingPolicyShadow.Sets.Rd.Active' : {
        'meta_info' : _MetaInfoClass('RoutingPolicyShadow.Sets.Rd.Active', REFERENCE_CLASS,
            '''All objects of a given type that are attached to
a protocol''',
            False, 
            [
            _MetaInfoClassMember('object', REFERENCE_LEAFLIST, 'str', 'String',
                None, None,
                [], [],
                '''                Policy objects
                ''',
                'object',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            ],
            'Cisco-IOS-XR-policy-repository-oper',
            'active',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-policy-repository-oper'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper',
            is_config=False,
        ),
    },
    'RoutingPolicyShadow.Sets.Rd' : {
        'meta_info' : _MetaInfoClass('RoutingPolicyShadow.Sets.Rd', REFERENCE_CLASS,
            '''Information about RD sets''',
            False, 
            [
            _MetaInfoClassMember('sets', REFERENCE_CLASS, 'Sets_', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper', 'RoutingPolicyShadow.Sets.Rd.Sets_',
                [], [],
                '''                Information about individual sets
                ''',
                'sets',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('unused', REFERENCE_CLASS, 'Unused', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper', 'RoutingPolicyShadow.Sets.Rd.Unused',
                [], [],
                '''                All objects of a given type that are not
                referenced at all
                ''',
                'unused',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('inactive', REFERENCE_CLASS, 'Inactive', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper', 'RoutingPolicyShadow.Sets.Rd.Inactive',
                [], [],
                '''                All objects of a given type that are not
                attached to a protocol
                ''',
                'inactive',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('active', REFERENCE_CLASS, 'Active', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper', 'RoutingPolicyShadow.Sets.Rd.Active',
                [], [],
                '''                All objects of a given type that are attached to
                a protocol
                ''',
                'active',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            ],
            'Cisco-IOS-XR-policy-repository-oper',
            'rd',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-policy-repository-oper'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper',
            is_config=False,
        ),
    },
    'RoutingPolicyShadow.Sets.Mac.Sets_.Set.UsedBy.Reference' : {
        'meta_info' : _MetaInfoClass('RoutingPolicyShadow.Sets.Mac.Sets_.Set.UsedBy.Reference', REFERENCE_LIST,
            '''Information about policies referring to this
object''',
            False, 
            [
            _MetaInfoClassMember('route-policy-name', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                Name of policy
                ''',
                'route_policy_name',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('used-directly', ATTRIBUTE, 'bool', 'boolean',
                None, None,
                [], [],
                '''                Whether the policy uses this object directly or
                indirectly
                ''',
                'used_directly',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('status', REFERENCE_ENUM_CLASS, 'ObjectStatus', 'Object-status',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper', 'ObjectStatus',
                [], [],
                '''                Active, Inactive, or Unused
                ''',
                'status',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            ],
            'Cisco-IOS-XR-policy-repository-oper',
            'reference',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-policy-repository-oper'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper',
            is_config=False,
        ),
    },
    'RoutingPolicyShadow.Sets.Mac.Sets_.Set.UsedBy' : {
        'meta_info' : _MetaInfoClass('RoutingPolicyShadow.Sets.Mac.Sets_.Set.UsedBy', REFERENCE_CLASS,
            '''Policies that use this object, directly or
indirectly''',
            False, 
            [
            _MetaInfoClassMember('reference', REFERENCE_LIST, 'Reference', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper', 'RoutingPolicyShadow.Sets.Mac.Sets_.Set.UsedBy.Reference',
                [], [],
                '''                Information about policies referring to this
                object
                ''',
                'reference',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            ],
            'Cisco-IOS-XR-policy-repository-oper',
            'used-by',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-policy-repository-oper'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper',
            is_config=False,
        ),
    },
    'RoutingPolicyShadow.Sets.Mac.Sets_.Set.Attached.Binding' : {
        'meta_info' : _MetaInfoClass('RoutingPolicyShadow.Sets.Mac.Sets_.Set.Attached.Binding', REFERENCE_LIST,
            '''bindings list''',
            False, 
            [
            _MetaInfoClassMember('protocol', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                Protocol to which policy attached
                ''',
                'protocol',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('vrf-name', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                VRF name
                ''',
                'vrf_name',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('proto-instance', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                Protocol instance
                ''',
                'proto_instance',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('af-name', REFERENCE_ENUM_CLASS, 'AddressFamily', 'Address-family',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper', 'AddressFamily',
                [], [],
                '''                Address Family Identifier
                ''',
                'af_name',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('saf-name', REFERENCE_ENUM_CLASS, 'SubAddressFamily', 'Sub-address-family',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper', 'SubAddressFamily',
                [], [],
                '''                Subsequent Address Family Identifier
                ''',
                'saf_name',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('neighbor-address', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                Neighbor IP Address
                ''',
                'neighbor_address',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('neighbor-af-name', REFERENCE_ENUM_CLASS, 'AddressFamily', 'Address-family',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper', 'AddressFamily',
                [], [],
                '''                Neighbor IP Address Family
                ''',
                'neighbor_af_name',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('group-name', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                Neighbor Group Name
                ''',
                'group_name',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('direction', REFERENCE_ENUM_CLASS, 'AttachPointDirection', 'Attach-point-direction',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper', 'AttachPointDirection',
                [], [],
                '''                Direction In or Out
                ''',
                'direction',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('group', REFERENCE_ENUM_CLASS, 'Group', 'Group',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper', 'Group',
                [], [],
                '''                Neighbor Group 
                ''',
                'group',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('source-protocol', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                Source Protocol to redistribute, Source Protocol
                can be one of the following values{all,
                connected, local, static, bgp, rip, isis, ospf
                ,ospfv3, eigrp, unknown }
                ''',
                'source_protocol',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('aggregate-network-address', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                Aggregate IP address or Network IP Address in
                IPv4 or IPv6 Format
                ''',
                'aggregate_network_address',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('interface-name', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                Interface Name
                ''',
                'interface_name',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('instance', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                Instance
                ''',
                'instance',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('area-id', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                OSPF Area ID in Decimal Integer Format
                ''',
                'area_id',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('propogate-from', ATTRIBUTE, 'int', 'int32',
                None, None,
                [('-2147483648', '2147483647')], [],
                '''                ISIS Propogate From Level
                ''',
                'propogate_from',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('propogate-to', ATTRIBUTE, 'int', 'int32',
                None, None,
                [('-2147483648', '2147483647')], [],
                '''                ISIS Propogate To Level
                ''',
                'propogate_to',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('route-policy-name', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                Policy that uses object in question
                ''',
                'route_policy_name',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('attached-policy', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                The attached policy that (maybe indirectly) uses
                the object in question
                ''',
                'attached_policy',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('attach-point', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                Name of attach point where policy is attached
                ''',
                'attach_point',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            ],
            'Cisco-IOS-XR-policy-repository-oper',
            'binding',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-policy-repository-oper'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper',
            is_config=False,
        ),
    },
    'RoutingPolicyShadow.Sets.Mac.Sets_.Set.Attached' : {
        'meta_info' : _MetaInfoClass('RoutingPolicyShadow.Sets.Mac.Sets_.Set.Attached', REFERENCE_CLASS,
            '''Information about where this policy or set is
attached''',
            False, 
            [
            _MetaInfoClassMember('binding', REFERENCE_LIST, 'Binding', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper', 'RoutingPolicyShadow.Sets.Mac.Sets_.Set.Attached.Binding',
                [], [],
                '''                bindings list
                ''',
                'binding',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            ],
            'Cisco-IOS-XR-policy-repository-oper',
            'attached',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-policy-repository-oper'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper',
            is_config=False,
        ),
    },
    'RoutingPolicyShadow.Sets.Mac.Sets_.Set' : {
        'meta_info' : _MetaInfoClass('RoutingPolicyShadow.Sets.Mac.Sets_.Set', REFERENCE_LIST,
            '''Information about an individual set''',
            False, 
            [
            _MetaInfoClassMember('set-name', ATTRIBUTE, 'str', 'xr:Cisco-ios-xr-string',
                None, None,
                [], [b'[\\w\\-\\.:,_@#%$\\+=\\|;]+'],
                '''                Set name
                ''',
                'set_name',
                'Cisco-IOS-XR-policy-repository-oper', True, is_config=False),
            _MetaInfoClassMember('used-by', REFERENCE_CLASS, 'UsedBy', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper', 'RoutingPolicyShadow.Sets.Mac.Sets_.Set.UsedBy',
                [], [],
                '''                Policies that use this object, directly or
                indirectly
                ''',
                'used_by',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('attached', REFERENCE_CLASS, 'Attached', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper', 'RoutingPolicyShadow.Sets.Mac.Sets_.Set.Attached',
                [], [],
                '''                Information about where this policy or set is
                attached
                ''',
                'attached',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            ],
            'Cisco-IOS-XR-policy-repository-oper',
            'set',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-policy-repository-oper'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper',
            is_config=False,
        ),
    },
    'RoutingPolicyShadow.Sets.Mac.Sets_' : {
        'meta_info' : _MetaInfoClass('RoutingPolicyShadow.Sets.Mac.Sets_', REFERENCE_CLASS,
            '''Information about individual sets''',
            False, 
            [
            _MetaInfoClassMember('set', REFERENCE_LIST, 'Set', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper', 'RoutingPolicyShadow.Sets.Mac.Sets_.Set',
                [], [],
                '''                Information about an individual set
                ''',
                'set',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            ],
            'Cisco-IOS-XR-policy-repository-oper',
            'sets',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-policy-repository-oper'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper',
            is_config=False,
        ),
    },
    'RoutingPolicyShadow.Sets.Mac.Unused' : {
        'meta_info' : _MetaInfoClass('RoutingPolicyShadow.Sets.Mac.Unused', REFERENCE_CLASS,
            '''All objects of a given type that are not
referenced at all''',
            False, 
            [
            _MetaInfoClassMember('object', REFERENCE_LEAFLIST, 'str', 'String',
                None, None,
                [], [],
                '''                Policy objects
                ''',
                'object',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            ],
            'Cisco-IOS-XR-policy-repository-oper',
            'unused',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-policy-repository-oper'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper',
            is_config=False,
        ),
    },
    'RoutingPolicyShadow.Sets.Mac.Inactive' : {
        'meta_info' : _MetaInfoClass('RoutingPolicyShadow.Sets.Mac.Inactive', REFERENCE_CLASS,
            '''All objects of a given type that are not
attached to a protocol''',
            False, 
            [
            _MetaInfoClassMember('object', REFERENCE_LEAFLIST, 'str', 'String',
                None, None,
                [], [],
                '''                Policy objects
                ''',
                'object',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            ],
            'Cisco-IOS-XR-policy-repository-oper',
            'inactive',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-policy-repository-oper'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper',
            is_config=False,
        ),
    },
    'RoutingPolicyShadow.Sets.Mac.Active' : {
        'meta_info' : _MetaInfoClass('RoutingPolicyShadow.Sets.Mac.Active', REFERENCE_CLASS,
            '''All objects of a given type that are attached to
a protocol''',
            False, 
            [
            _MetaInfoClassMember('object', REFERENCE_LEAFLIST, 'str', 'String',
                None, None,
                [], [],
                '''                Policy objects
                ''',
                'object',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            ],
            'Cisco-IOS-XR-policy-repository-oper',
            'active',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-policy-repository-oper'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper',
            is_config=False,
        ),
    },
    'RoutingPolicyShadow.Sets.Mac' : {
        'meta_info' : _MetaInfoClass('RoutingPolicyShadow.Sets.Mac', REFERENCE_CLASS,
            '''Information about Mac sets''',
            False, 
            [
            _MetaInfoClassMember('sets', REFERENCE_CLASS, 'Sets_', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper', 'RoutingPolicyShadow.Sets.Mac.Sets_',
                [], [],
                '''                Information about individual sets
                ''',
                'sets',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('unused', REFERENCE_CLASS, 'Unused', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper', 'RoutingPolicyShadow.Sets.Mac.Unused',
                [], [],
                '''                All objects of a given type that are not
                referenced at all
                ''',
                'unused',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('inactive', REFERENCE_CLASS, 'Inactive', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper', 'RoutingPolicyShadow.Sets.Mac.Inactive',
                [], [],
                '''                All objects of a given type that are not
                attached to a protocol
                ''',
                'inactive',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('active', REFERENCE_CLASS, 'Active', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper', 'RoutingPolicyShadow.Sets.Mac.Active',
                [], [],
                '''                All objects of a given type that are attached to
                a protocol
                ''',
                'active',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            ],
            'Cisco-IOS-XR-policy-repository-oper',
            'mac',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-policy-repository-oper'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper',
            is_config=False,
        ),
    },
    'RoutingPolicyShadow.Sets.ExtendedCommunityCost.Sets_.Set.UsedBy.Reference' : {
        'meta_info' : _MetaInfoClass('RoutingPolicyShadow.Sets.ExtendedCommunityCost.Sets_.Set.UsedBy.Reference', REFERENCE_LIST,
            '''Information about policies referring to this
object''',
            False, 
            [
            _MetaInfoClassMember('route-policy-name', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                Name of policy
                ''',
                'route_policy_name',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('used-directly', ATTRIBUTE, 'bool', 'boolean',
                None, None,
                [], [],
                '''                Whether the policy uses this object directly or
                indirectly
                ''',
                'used_directly',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('status', REFERENCE_ENUM_CLASS, 'ObjectStatus', 'Object-status',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper', 'ObjectStatus',
                [], [],
                '''                Active, Inactive, or Unused
                ''',
                'status',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            ],
            'Cisco-IOS-XR-policy-repository-oper',
            'reference',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-policy-repository-oper'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper',
            is_config=False,
        ),
    },
    'RoutingPolicyShadow.Sets.ExtendedCommunityCost.Sets_.Set.UsedBy' : {
        'meta_info' : _MetaInfoClass('RoutingPolicyShadow.Sets.ExtendedCommunityCost.Sets_.Set.UsedBy', REFERENCE_CLASS,
            '''Policies that use this object, directly or
indirectly''',
            False, 
            [
            _MetaInfoClassMember('reference', REFERENCE_LIST, 'Reference', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper', 'RoutingPolicyShadow.Sets.ExtendedCommunityCost.Sets_.Set.UsedBy.Reference',
                [], [],
                '''                Information about policies referring to this
                object
                ''',
                'reference',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            ],
            'Cisco-IOS-XR-policy-repository-oper',
            'used-by',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-policy-repository-oper'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper',
            is_config=False,
        ),
    },
    'RoutingPolicyShadow.Sets.ExtendedCommunityCost.Sets_.Set.Attached.Binding' : {
        'meta_info' : _MetaInfoClass('RoutingPolicyShadow.Sets.ExtendedCommunityCost.Sets_.Set.Attached.Binding', REFERENCE_LIST,
            '''bindings list''',
            False, 
            [
            _MetaInfoClassMember('protocol', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                Protocol to which policy attached
                ''',
                'protocol',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('vrf-name', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                VRF name
                ''',
                'vrf_name',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('proto-instance', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                Protocol instance
                ''',
                'proto_instance',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('af-name', REFERENCE_ENUM_CLASS, 'AddressFamily', 'Address-family',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper', 'AddressFamily',
                [], [],
                '''                Address Family Identifier
                ''',
                'af_name',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('saf-name', REFERENCE_ENUM_CLASS, 'SubAddressFamily', 'Sub-address-family',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper', 'SubAddressFamily',
                [], [],
                '''                Subsequent Address Family Identifier
                ''',
                'saf_name',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('neighbor-address', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                Neighbor IP Address
                ''',
                'neighbor_address',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('neighbor-af-name', REFERENCE_ENUM_CLASS, 'AddressFamily', 'Address-family',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper', 'AddressFamily',
                [], [],
                '''                Neighbor IP Address Family
                ''',
                'neighbor_af_name',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('group-name', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                Neighbor Group Name
                ''',
                'group_name',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('direction', REFERENCE_ENUM_CLASS, 'AttachPointDirection', 'Attach-point-direction',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper', 'AttachPointDirection',
                [], [],
                '''                Direction In or Out
                ''',
                'direction',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('group', REFERENCE_ENUM_CLASS, 'Group', 'Group',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper', 'Group',
                [], [],
                '''                Neighbor Group 
                ''',
                'group',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('source-protocol', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                Source Protocol to redistribute, Source Protocol
                can be one of the following values{all,
                connected, local, static, bgp, rip, isis, ospf
                ,ospfv3, eigrp, unknown }
                ''',
                'source_protocol',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('aggregate-network-address', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                Aggregate IP address or Network IP Address in
                IPv4 or IPv6 Format
                ''',
                'aggregate_network_address',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('interface-name', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                Interface Name
                ''',
                'interface_name',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('instance', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                Instance
                ''',
                'instance',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('area-id', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                OSPF Area ID in Decimal Integer Format
                ''',
                'area_id',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('propogate-from', ATTRIBUTE, 'int', 'int32',
                None, None,
                [('-2147483648', '2147483647')], [],
                '''                ISIS Propogate From Level
                ''',
                'propogate_from',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('propogate-to', ATTRIBUTE, 'int', 'int32',
                None, None,
                [('-2147483648', '2147483647')], [],
                '''                ISIS Propogate To Level
                ''',
                'propogate_to',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('route-policy-name', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                Policy that uses object in question
                ''',
                'route_policy_name',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('attached-policy', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                The attached policy that (maybe indirectly) uses
                the object in question
                ''',
                'attached_policy',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('attach-point', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                Name of attach point where policy is attached
                ''',
                'attach_point',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            ],
            'Cisco-IOS-XR-policy-repository-oper',
            'binding',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-policy-repository-oper'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper',
            is_config=False,
        ),
    },
    'RoutingPolicyShadow.Sets.ExtendedCommunityCost.Sets_.Set.Attached' : {
        'meta_info' : _MetaInfoClass('RoutingPolicyShadow.Sets.ExtendedCommunityCost.Sets_.Set.Attached', REFERENCE_CLASS,
            '''Information about where this policy or set is
attached''',
            False, 
            [
            _MetaInfoClassMember('binding', REFERENCE_LIST, 'Binding', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper', 'RoutingPolicyShadow.Sets.ExtendedCommunityCost.Sets_.Set.Attached.Binding',
                [], [],
                '''                bindings list
                ''',
                'binding',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            ],
            'Cisco-IOS-XR-policy-repository-oper',
            'attached',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-policy-repository-oper'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper',
            is_config=False,
        ),
    },
    'RoutingPolicyShadow.Sets.ExtendedCommunityCost.Sets_.Set' : {
        'meta_info' : _MetaInfoClass('RoutingPolicyShadow.Sets.ExtendedCommunityCost.Sets_.Set', REFERENCE_LIST,
            '''Information about an individual set''',
            False, 
            [
            _MetaInfoClassMember('set-name', ATTRIBUTE, 'str', 'xr:Cisco-ios-xr-string',
                None, None,
                [], [b'[\\w\\-\\.:,_@#%$\\+=\\|;]+'],
                '''                Set name
                ''',
                'set_name',
                'Cisco-IOS-XR-policy-repository-oper', True, is_config=False),
            _MetaInfoClassMember('used-by', REFERENCE_CLASS, 'UsedBy', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper', 'RoutingPolicyShadow.Sets.ExtendedCommunityCost.Sets_.Set.UsedBy',
                [], [],
                '''                Policies that use this object, directly or
                indirectly
                ''',
                'used_by',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('attached', REFERENCE_CLASS, 'Attached', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper', 'RoutingPolicyShadow.Sets.ExtendedCommunityCost.Sets_.Set.Attached',
                [], [],
                '''                Information about where this policy or set is
                attached
                ''',
                'attached',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            ],
            'Cisco-IOS-XR-policy-repository-oper',
            'set',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-policy-repository-oper'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper',
            is_config=False,
        ),
    },
    'RoutingPolicyShadow.Sets.ExtendedCommunityCost.Sets_' : {
        'meta_info' : _MetaInfoClass('RoutingPolicyShadow.Sets.ExtendedCommunityCost.Sets_', REFERENCE_CLASS,
            '''Information about individual sets''',
            False, 
            [
            _MetaInfoClassMember('set', REFERENCE_LIST, 'Set', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper', 'RoutingPolicyShadow.Sets.ExtendedCommunityCost.Sets_.Set',
                [], [],
                '''                Information about an individual set
                ''',
                'set',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            ],
            'Cisco-IOS-XR-policy-repository-oper',
            'sets',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-policy-repository-oper'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper',
            is_config=False,
        ),
    },
    'RoutingPolicyShadow.Sets.ExtendedCommunityCost.Unused' : {
        'meta_info' : _MetaInfoClass('RoutingPolicyShadow.Sets.ExtendedCommunityCost.Unused', REFERENCE_CLASS,
            '''All objects of a given type that are not
referenced at all''',
            False, 
            [
            _MetaInfoClassMember('object', REFERENCE_LEAFLIST, 'str', 'String',
                None, None,
                [], [],
                '''                Policy objects
                ''',
                'object',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            ],
            'Cisco-IOS-XR-policy-repository-oper',
            'unused',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-policy-repository-oper'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper',
            is_config=False,
        ),
    },
    'RoutingPolicyShadow.Sets.ExtendedCommunityCost.Inactive' : {
        'meta_info' : _MetaInfoClass('RoutingPolicyShadow.Sets.ExtendedCommunityCost.Inactive', REFERENCE_CLASS,
            '''All objects of a given type that are not
attached to a protocol''',
            False, 
            [
            _MetaInfoClassMember('object', REFERENCE_LEAFLIST, 'str', 'String',
                None, None,
                [], [],
                '''                Policy objects
                ''',
                'object',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            ],
            'Cisco-IOS-XR-policy-repository-oper',
            'inactive',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-policy-repository-oper'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper',
            is_config=False,
        ),
    },
    'RoutingPolicyShadow.Sets.ExtendedCommunityCost.Active' : {
        'meta_info' : _MetaInfoClass('RoutingPolicyShadow.Sets.ExtendedCommunityCost.Active', REFERENCE_CLASS,
            '''All objects of a given type that are attached to
a protocol''',
            False, 
            [
            _MetaInfoClassMember('object', REFERENCE_LEAFLIST, 'str', 'String',
                None, None,
                [], [],
                '''                Policy objects
                ''',
                'object',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            ],
            'Cisco-IOS-XR-policy-repository-oper',
            'active',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-policy-repository-oper'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper',
            is_config=False,
        ),
    },
    'RoutingPolicyShadow.Sets.ExtendedCommunityCost' : {
        'meta_info' : _MetaInfoClass('RoutingPolicyShadow.Sets.ExtendedCommunityCost', REFERENCE_CLASS,
            '''Information about Extended Community Cost sets''',
            False, 
            [
            _MetaInfoClassMember('sets', REFERENCE_CLASS, 'Sets_', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper', 'RoutingPolicyShadow.Sets.ExtendedCommunityCost.Sets_',
                [], [],
                '''                Information about individual sets
                ''',
                'sets',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('unused', REFERENCE_CLASS, 'Unused', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper', 'RoutingPolicyShadow.Sets.ExtendedCommunityCost.Unused',
                [], [],
                '''                All objects of a given type that are not
                referenced at all
                ''',
                'unused',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('inactive', REFERENCE_CLASS, 'Inactive', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper', 'RoutingPolicyShadow.Sets.ExtendedCommunityCost.Inactive',
                [], [],
                '''                All objects of a given type that are not
                attached to a protocol
                ''',
                'inactive',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('active', REFERENCE_CLASS, 'Active', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper', 'RoutingPolicyShadow.Sets.ExtendedCommunityCost.Active',
                [], [],
                '''                All objects of a given type that are attached to
                a protocol
                ''',
                'active',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            ],
            'Cisco-IOS-XR-policy-repository-oper',
            'extended-community-cost',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-policy-repository-oper'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper',
            is_config=False,
        ),
    },
    'RoutingPolicyShadow.Sets' : {
        'meta_info' : _MetaInfoClass('RoutingPolicyShadow.Sets', REFERENCE_CLASS,
            '''Information about configured sets''',
            False, 
            [
            _MetaInfoClassMember('etag', REFERENCE_CLASS, 'Etag', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper', 'RoutingPolicyShadow.Sets.Etag',
                [], [],
                '''                Information about Etag sets
                ''',
                'etag',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('ospf-area', REFERENCE_CLASS, 'OspfArea', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper', 'RoutingPolicyShadow.Sets.OspfArea',
                [], [],
                '''                Information about OSPF Area sets
                ''',
                'ospf_area',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('extended-community-opaque', REFERENCE_CLASS, 'ExtendedCommunityOpaque', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper', 'RoutingPolicyShadow.Sets.ExtendedCommunityOpaque',
                [], [],
                '''                Information about Extended Community Opaque
                sets
                ''',
                'extended_community_opaque',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('extended-community-seg-nh', REFERENCE_CLASS, 'ExtendedCommunitySegNh', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper', 'RoutingPolicyShadow.Sets.ExtendedCommunitySegNh',
                [], [],
                '''                Information about Extended Community SegNH sets
                ''',
                'extended_community_seg_nh',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('extended-community-soo', REFERENCE_CLASS, 'ExtendedCommunitySoo', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper', 'RoutingPolicyShadow.Sets.ExtendedCommunitySoo',
                [], [],
                '''                Information about Extended Community SOO sets
                ''',
                'extended_community_soo',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('tag', REFERENCE_CLASS, 'Tag', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper', 'RoutingPolicyShadow.Sets.Tag',
                [], [],
                '''                Information about Tag sets
                ''',
                'tag',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('prefix', REFERENCE_CLASS, 'Prefix', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper', 'RoutingPolicyShadow.Sets.Prefix',
                [], [],
                '''                Information about AS Path sets
                ''',
                'prefix',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('community', REFERENCE_CLASS, 'Community', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper', 'RoutingPolicyShadow.Sets.Community',
                [], [],
                '''                Information about Community sets
                ''',
                'community',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('as-path', REFERENCE_CLASS, 'AsPath', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper', 'RoutingPolicyShadow.Sets.AsPath',
                [], [],
                '''                Information about AS Path sets
                ''',
                'as_path',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('large-community', REFERENCE_CLASS, 'LargeCommunity', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper', 'RoutingPolicyShadow.Sets.LargeCommunity',
                [], [],
                '''                Information about Large Community sets
                ''',
                'large_community',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('esi', REFERENCE_CLASS, 'Esi', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper', 'RoutingPolicyShadow.Sets.Esi',
                [], [],
                '''                Information about Esi sets
                ''',
                'esi',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('extended-community-bandwidth', REFERENCE_CLASS, 'ExtendedCommunityBandwidth', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper', 'RoutingPolicyShadow.Sets.ExtendedCommunityBandwidth',
                [], [],
                '''                Information about Extended Community Bandwidth
                sets
                ''',
                'extended_community_bandwidth',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('extended-community-rt', REFERENCE_CLASS, 'ExtendedCommunityRt', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper', 'RoutingPolicyShadow.Sets.ExtendedCommunityRt',
                [], [],
                '''                Information about Extended Community RT sets
                ''',
                'extended_community_rt',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('rd', REFERENCE_CLASS, 'Rd', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper', 'RoutingPolicyShadow.Sets.Rd',
                [], [],
                '''                Information about RD sets
                ''',
                'rd',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('mac', REFERENCE_CLASS, 'Mac', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper', 'RoutingPolicyShadow.Sets.Mac',
                [], [],
                '''                Information about Mac sets
                ''',
                'mac',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('extended-community-cost', REFERENCE_CLASS, 'ExtendedCommunityCost', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper', 'RoutingPolicyShadow.Sets.ExtendedCommunityCost',
                [], [],
                '''                Information about Extended Community Cost sets
                ''',
                'extended_community_cost',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            ],
            'Cisco-IOS-XR-policy-repository-oper',
            'sets',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-policy-repository-oper'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper',
            is_config=False,
        ),
    },
    'RoutingPolicyShadow' : {
        'meta_info' : _MetaInfoClass('RoutingPolicyShadow', REFERENCE_CLASS,
            '''routing policy shadow''',
            False, 
            [
            _MetaInfoClassMember('limits', REFERENCE_CLASS, 'Limits', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper', 'RoutingPolicyShadow.Limits',
                [], [],
                '''                Information about configured limits and the
                current values
                ''',
                'limits',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('policies', REFERENCE_CLASS, 'Policies', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper', 'RoutingPolicyShadow.Policies',
                [], [],
                '''                Information about configured route policies
                ''',
                'policies',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            _MetaInfoClassMember('sets', REFERENCE_CLASS, 'Sets', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper', 'RoutingPolicyShadow.Sets',
                [], [],
                '''                Information about configured sets
                ''',
                'sets',
                'Cisco-IOS-XR-policy-repository-oper', False, is_config=False),
            ],
            'Cisco-IOS-XR-policy-repository-oper',
            'routing-policy-shadow',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-policy-repository-oper'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper',
            is_config=False,
        ),
    },
}
_meta_table['RoutingPolicy.Policies.RoutePolicies.RoutePolicy.PolicyUses.AllUsedSets.Sets']['meta_info'].parent =_meta_table['RoutingPolicy.Policies.RoutePolicies.RoutePolicy.PolicyUses.AllUsedSets']['meta_info']
_meta_table['RoutingPolicy.Policies.RoutePolicies.RoutePolicy.PolicyUses.DirectlyUsedSets.Sets']['meta_info'].parent =_meta_table['RoutingPolicy.Policies.RoutePolicies.RoutePolicy.PolicyUses.DirectlyUsedSets']['meta_info']
_meta_table['RoutingPolicy.Policies.RoutePolicies.RoutePolicy.PolicyUses.DirectlyUsedPolicies']['meta_info'].parent =_meta_table['RoutingPolicy.Policies.RoutePolicies.RoutePolicy.PolicyUses']['meta_info']
_meta_table['RoutingPolicy.Policies.RoutePolicies.RoutePolicy.PolicyUses.AllUsedSets']['meta_info'].parent =_meta_table['RoutingPolicy.Policies.RoutePolicies.RoutePolicy.PolicyUses']['meta_info']
_meta_table['RoutingPolicy.Policies.RoutePolicies.RoutePolicy.PolicyUses.DirectlyUsedSets']['meta_info'].parent =_meta_table['RoutingPolicy.Policies.RoutePolicies.RoutePolicy.PolicyUses']['meta_info']
_meta_table['RoutingPolicy.Policies.RoutePolicies.RoutePolicy.PolicyUses.AllUsedPolicies']['meta_info'].parent =_meta_table['RoutingPolicy.Policies.RoutePolicies.RoutePolicy.PolicyUses']['meta_info']
_meta_table['RoutingPolicy.Policies.RoutePolicies.RoutePolicy.UsedBy.Reference']['meta_info'].parent =_meta_table['RoutingPolicy.Policies.RoutePolicies.RoutePolicy.UsedBy']['meta_info']
_meta_table['RoutingPolicy.Policies.RoutePolicies.RoutePolicy.Attached.Binding']['meta_info'].parent =_meta_table['RoutingPolicy.Policies.RoutePolicies.RoutePolicy.Attached']['meta_info']
_meta_table['RoutingPolicy.Policies.RoutePolicies.RoutePolicy.PolicyUses']['meta_info'].parent =_meta_table['RoutingPolicy.Policies.RoutePolicies.RoutePolicy']['meta_info']
_meta_table['RoutingPolicy.Policies.RoutePolicies.RoutePolicy.UsedBy']['meta_info'].parent =_meta_table['RoutingPolicy.Policies.RoutePolicies.RoutePolicy']['meta_info']
_meta_table['RoutingPolicy.Policies.RoutePolicies.RoutePolicy.Attached']['meta_info'].parent =_meta_table['RoutingPolicy.Policies.RoutePolicies.RoutePolicy']['meta_info']
_meta_table['RoutingPolicy.Policies.RoutePolicies.RoutePolicy']['meta_info'].parent =_meta_table['RoutingPolicy.Policies.RoutePolicies']['meta_info']
_meta_table['RoutingPolicy.Policies.RoutePolicies']['meta_info'].parent =_meta_table['RoutingPolicy.Policies']['meta_info']
_meta_table['RoutingPolicy.Policies.Unused']['meta_info'].parent =_meta_table['RoutingPolicy.Policies']['meta_info']
_meta_table['RoutingPolicy.Policies.Inactive']['meta_info'].parent =_meta_table['RoutingPolicy.Policies']['meta_info']
_meta_table['RoutingPolicy.Policies.Active']['meta_info'].parent =_meta_table['RoutingPolicy.Policies']['meta_info']
_meta_table['RoutingPolicy.Sets.Etag.Sets_.Set.UsedBy.Reference']['meta_info'].parent =_meta_table['RoutingPolicy.Sets.Etag.Sets_.Set.UsedBy']['meta_info']
_meta_table['RoutingPolicy.Sets.Etag.Sets_.Set.Attached.Binding']['meta_info'].parent =_meta_table['RoutingPolicy.Sets.Etag.Sets_.Set.Attached']['meta_info']
_meta_table['RoutingPolicy.Sets.Etag.Sets_.Set.UsedBy']['meta_info'].parent =_meta_table['RoutingPolicy.Sets.Etag.Sets_.Set']['meta_info']
_meta_table['RoutingPolicy.Sets.Etag.Sets_.Set.Attached']['meta_info'].parent =_meta_table['RoutingPolicy.Sets.Etag.Sets_.Set']['meta_info']
_meta_table['RoutingPolicy.Sets.Etag.Sets_.Set']['meta_info'].parent =_meta_table['RoutingPolicy.Sets.Etag.Sets_']['meta_info']
_meta_table['RoutingPolicy.Sets.Etag.Sets_']['meta_info'].parent =_meta_table['RoutingPolicy.Sets.Etag']['meta_info']
_meta_table['RoutingPolicy.Sets.Etag.Unused']['meta_info'].parent =_meta_table['RoutingPolicy.Sets.Etag']['meta_info']
_meta_table['RoutingPolicy.Sets.Etag.Inactive']['meta_info'].parent =_meta_table['RoutingPolicy.Sets.Etag']['meta_info']
_meta_table['RoutingPolicy.Sets.Etag.Active']['meta_info'].parent =_meta_table['RoutingPolicy.Sets.Etag']['meta_info']
_meta_table['RoutingPolicy.Sets.OspfArea.Sets_.Set.UsedBy.Reference']['meta_info'].parent =_meta_table['RoutingPolicy.Sets.OspfArea.Sets_.Set.UsedBy']['meta_info']
_meta_table['RoutingPolicy.Sets.OspfArea.Sets_.Set.Attached.Binding']['meta_info'].parent =_meta_table['RoutingPolicy.Sets.OspfArea.Sets_.Set.Attached']['meta_info']
_meta_table['RoutingPolicy.Sets.OspfArea.Sets_.Set.UsedBy']['meta_info'].parent =_meta_table['RoutingPolicy.Sets.OspfArea.Sets_.Set']['meta_info']
_meta_table['RoutingPolicy.Sets.OspfArea.Sets_.Set.Attached']['meta_info'].parent =_meta_table['RoutingPolicy.Sets.OspfArea.Sets_.Set']['meta_info']
_meta_table['RoutingPolicy.Sets.OspfArea.Sets_.Set']['meta_info'].parent =_meta_table['RoutingPolicy.Sets.OspfArea.Sets_']['meta_info']
_meta_table['RoutingPolicy.Sets.OspfArea.Sets_']['meta_info'].parent =_meta_table['RoutingPolicy.Sets.OspfArea']['meta_info']
_meta_table['RoutingPolicy.Sets.OspfArea.Unused']['meta_info'].parent =_meta_table['RoutingPolicy.Sets.OspfArea']['meta_info']
_meta_table['RoutingPolicy.Sets.OspfArea.Inactive']['meta_info'].parent =_meta_table['RoutingPolicy.Sets.OspfArea']['meta_info']
_meta_table['RoutingPolicy.Sets.OspfArea.Active']['meta_info'].parent =_meta_table['RoutingPolicy.Sets.OspfArea']['meta_info']
_meta_table['RoutingPolicy.Sets.ExtendedCommunityOpaque.Sets_.Set.UsedBy.Reference']['meta_info'].parent =_meta_table['RoutingPolicy.Sets.ExtendedCommunityOpaque.Sets_.Set.UsedBy']['meta_info']
_meta_table['RoutingPolicy.Sets.ExtendedCommunityOpaque.Sets_.Set.Attached.Binding']['meta_info'].parent =_meta_table['RoutingPolicy.Sets.ExtendedCommunityOpaque.Sets_.Set.Attached']['meta_info']
_meta_table['RoutingPolicy.Sets.ExtendedCommunityOpaque.Sets_.Set.UsedBy']['meta_info'].parent =_meta_table['RoutingPolicy.Sets.ExtendedCommunityOpaque.Sets_.Set']['meta_info']
_meta_table['RoutingPolicy.Sets.ExtendedCommunityOpaque.Sets_.Set.Attached']['meta_info'].parent =_meta_table['RoutingPolicy.Sets.ExtendedCommunityOpaque.Sets_.Set']['meta_info']
_meta_table['RoutingPolicy.Sets.ExtendedCommunityOpaque.Sets_.Set']['meta_info'].parent =_meta_table['RoutingPolicy.Sets.ExtendedCommunityOpaque.Sets_']['meta_info']
_meta_table['RoutingPolicy.Sets.ExtendedCommunityOpaque.Sets_']['meta_info'].parent =_meta_table['RoutingPolicy.Sets.ExtendedCommunityOpaque']['meta_info']
_meta_table['RoutingPolicy.Sets.ExtendedCommunityOpaque.Unused']['meta_info'].parent =_meta_table['RoutingPolicy.Sets.ExtendedCommunityOpaque']['meta_info']
_meta_table['RoutingPolicy.Sets.ExtendedCommunityOpaque.Inactive']['meta_info'].parent =_meta_table['RoutingPolicy.Sets.ExtendedCommunityOpaque']['meta_info']
_meta_table['RoutingPolicy.Sets.ExtendedCommunityOpaque.Active']['meta_info'].parent =_meta_table['RoutingPolicy.Sets.ExtendedCommunityOpaque']['meta_info']
_meta_table['RoutingPolicy.Sets.ExtendedCommunitySegNh.Sets_.Set.UsedBy.Reference']['meta_info'].parent =_meta_table['RoutingPolicy.Sets.ExtendedCommunitySegNh.Sets_.Set.UsedBy']['meta_info']
_meta_table['RoutingPolicy.Sets.ExtendedCommunitySegNh.Sets_.Set.Attached.Binding']['meta_info'].parent =_meta_table['RoutingPolicy.Sets.ExtendedCommunitySegNh.Sets_.Set.Attached']['meta_info']
_meta_table['RoutingPolicy.Sets.ExtendedCommunitySegNh.Sets_.Set.UsedBy']['meta_info'].parent =_meta_table['RoutingPolicy.Sets.ExtendedCommunitySegNh.Sets_.Set']['meta_info']
_meta_table['RoutingPolicy.Sets.ExtendedCommunitySegNh.Sets_.Set.Attached']['meta_info'].parent =_meta_table['RoutingPolicy.Sets.ExtendedCommunitySegNh.Sets_.Set']['meta_info']
_meta_table['RoutingPolicy.Sets.ExtendedCommunitySegNh.Sets_.Set']['meta_info'].parent =_meta_table['RoutingPolicy.Sets.ExtendedCommunitySegNh.Sets_']['meta_info']
_meta_table['RoutingPolicy.Sets.ExtendedCommunitySegNh.Sets_']['meta_info'].parent =_meta_table['RoutingPolicy.Sets.ExtendedCommunitySegNh']['meta_info']
_meta_table['RoutingPolicy.Sets.ExtendedCommunitySegNh.Unused']['meta_info'].parent =_meta_table['RoutingPolicy.Sets.ExtendedCommunitySegNh']['meta_info']
_meta_table['RoutingPolicy.Sets.ExtendedCommunitySegNh.Inactive']['meta_info'].parent =_meta_table['RoutingPolicy.Sets.ExtendedCommunitySegNh']['meta_info']
_meta_table['RoutingPolicy.Sets.ExtendedCommunitySegNh.Active']['meta_info'].parent =_meta_table['RoutingPolicy.Sets.ExtendedCommunitySegNh']['meta_info']
_meta_table['RoutingPolicy.Sets.ExtendedCommunitySoo.Sets_.Set.UsedBy.Reference']['meta_info'].parent =_meta_table['RoutingPolicy.Sets.ExtendedCommunitySoo.Sets_.Set.UsedBy']['meta_info']
_meta_table['RoutingPolicy.Sets.ExtendedCommunitySoo.Sets_.Set.Attached.Binding']['meta_info'].parent =_meta_table['RoutingPolicy.Sets.ExtendedCommunitySoo.Sets_.Set.Attached']['meta_info']
_meta_table['RoutingPolicy.Sets.ExtendedCommunitySoo.Sets_.Set.UsedBy']['meta_info'].parent =_meta_table['RoutingPolicy.Sets.ExtendedCommunitySoo.Sets_.Set']['meta_info']
_meta_table['RoutingPolicy.Sets.ExtendedCommunitySoo.Sets_.Set.Attached']['meta_info'].parent =_meta_table['RoutingPolicy.Sets.ExtendedCommunitySoo.Sets_.Set']['meta_info']
_meta_table['RoutingPolicy.Sets.ExtendedCommunitySoo.Sets_.Set']['meta_info'].parent =_meta_table['RoutingPolicy.Sets.ExtendedCommunitySoo.Sets_']['meta_info']
_meta_table['RoutingPolicy.Sets.ExtendedCommunitySoo.Sets_']['meta_info'].parent =_meta_table['RoutingPolicy.Sets.ExtendedCommunitySoo']['meta_info']
_meta_table['RoutingPolicy.Sets.ExtendedCommunitySoo.Unused']['meta_info'].parent =_meta_table['RoutingPolicy.Sets.ExtendedCommunitySoo']['meta_info']
_meta_table['RoutingPolicy.Sets.ExtendedCommunitySoo.Inactive']['meta_info'].parent =_meta_table['RoutingPolicy.Sets.ExtendedCommunitySoo']['meta_info']
_meta_table['RoutingPolicy.Sets.ExtendedCommunitySoo.Active']['meta_info'].parent =_meta_table['RoutingPolicy.Sets.ExtendedCommunitySoo']['meta_info']
_meta_table['RoutingPolicy.Sets.Tag.Sets_.Set.UsedBy.Reference']['meta_info'].parent =_meta_table['RoutingPolicy.Sets.Tag.Sets_.Set.UsedBy']['meta_info']
_meta_table['RoutingPolicy.Sets.Tag.Sets_.Set.Attached.Binding']['meta_info'].parent =_meta_table['RoutingPolicy.Sets.Tag.Sets_.Set.Attached']['meta_info']
_meta_table['RoutingPolicy.Sets.Tag.Sets_.Set.UsedBy']['meta_info'].parent =_meta_table['RoutingPolicy.Sets.Tag.Sets_.Set']['meta_info']
_meta_table['RoutingPolicy.Sets.Tag.Sets_.Set.Attached']['meta_info'].parent =_meta_table['RoutingPolicy.Sets.Tag.Sets_.Set']['meta_info']
_meta_table['RoutingPolicy.Sets.Tag.Sets_.Set']['meta_info'].parent =_meta_table['RoutingPolicy.Sets.Tag.Sets_']['meta_info']
_meta_table['RoutingPolicy.Sets.Tag.Sets_']['meta_info'].parent =_meta_table['RoutingPolicy.Sets.Tag']['meta_info']
_meta_table['RoutingPolicy.Sets.Tag.Unused']['meta_info'].parent =_meta_table['RoutingPolicy.Sets.Tag']['meta_info']
_meta_table['RoutingPolicy.Sets.Tag.Inactive']['meta_info'].parent =_meta_table['RoutingPolicy.Sets.Tag']['meta_info']
_meta_table['RoutingPolicy.Sets.Tag.Active']['meta_info'].parent =_meta_table['RoutingPolicy.Sets.Tag']['meta_info']
_meta_table['RoutingPolicy.Sets.Prefix.Sets_.Set.UsedBy.Reference']['meta_info'].parent =_meta_table['RoutingPolicy.Sets.Prefix.Sets_.Set.UsedBy']['meta_info']
_meta_table['RoutingPolicy.Sets.Prefix.Sets_.Set.Attached.Binding']['meta_info'].parent =_meta_table['RoutingPolicy.Sets.Prefix.Sets_.Set.Attached']['meta_info']
_meta_table['RoutingPolicy.Sets.Prefix.Sets_.Set.UsedBy']['meta_info'].parent =_meta_table['RoutingPolicy.Sets.Prefix.Sets_.Set']['meta_info']
_meta_table['RoutingPolicy.Sets.Prefix.Sets_.Set.Attached']['meta_info'].parent =_meta_table['RoutingPolicy.Sets.Prefix.Sets_.Set']['meta_info']
_meta_table['RoutingPolicy.Sets.Prefix.Sets_.Set']['meta_info'].parent =_meta_table['RoutingPolicy.Sets.Prefix.Sets_']['meta_info']
_meta_table['RoutingPolicy.Sets.Prefix.Sets_']['meta_info'].parent =_meta_table['RoutingPolicy.Sets.Prefix']['meta_info']
_meta_table['RoutingPolicy.Sets.Prefix.Unused']['meta_info'].parent =_meta_table['RoutingPolicy.Sets.Prefix']['meta_info']
_meta_table['RoutingPolicy.Sets.Prefix.Inactive']['meta_info'].parent =_meta_table['RoutingPolicy.Sets.Prefix']['meta_info']
_meta_table['RoutingPolicy.Sets.Prefix.Active']['meta_info'].parent =_meta_table['RoutingPolicy.Sets.Prefix']['meta_info']
_meta_table['RoutingPolicy.Sets.Community.Sets_.Set.UsedBy.Reference']['meta_info'].parent =_meta_table['RoutingPolicy.Sets.Community.Sets_.Set.UsedBy']['meta_info']
_meta_table['RoutingPolicy.Sets.Community.Sets_.Set.Attached.Binding']['meta_info'].parent =_meta_table['RoutingPolicy.Sets.Community.Sets_.Set.Attached']['meta_info']
_meta_table['RoutingPolicy.Sets.Community.Sets_.Set.UsedBy']['meta_info'].parent =_meta_table['RoutingPolicy.Sets.Community.Sets_.Set']['meta_info']
_meta_table['RoutingPolicy.Sets.Community.Sets_.Set.Attached']['meta_info'].parent =_meta_table['RoutingPolicy.Sets.Community.Sets_.Set']['meta_info']
_meta_table['RoutingPolicy.Sets.Community.Sets_.Set']['meta_info'].parent =_meta_table['RoutingPolicy.Sets.Community.Sets_']['meta_info']
_meta_table['RoutingPolicy.Sets.Community.Sets_']['meta_info'].parent =_meta_table['RoutingPolicy.Sets.Community']['meta_info']
_meta_table['RoutingPolicy.Sets.Community.Unused']['meta_info'].parent =_meta_table['RoutingPolicy.Sets.Community']['meta_info']
_meta_table['RoutingPolicy.Sets.Community.Inactive']['meta_info'].parent =_meta_table['RoutingPolicy.Sets.Community']['meta_info']
_meta_table['RoutingPolicy.Sets.Community.Active']['meta_info'].parent =_meta_table['RoutingPolicy.Sets.Community']['meta_info']
_meta_table['RoutingPolicy.Sets.AsPath.Sets_.Set.UsedBy.Reference']['meta_info'].parent =_meta_table['RoutingPolicy.Sets.AsPath.Sets_.Set.UsedBy']['meta_info']
_meta_table['RoutingPolicy.Sets.AsPath.Sets_.Set.Attached.Binding']['meta_info'].parent =_meta_table['RoutingPolicy.Sets.AsPath.Sets_.Set.Attached']['meta_info']
_meta_table['RoutingPolicy.Sets.AsPath.Sets_.Set.UsedBy']['meta_info'].parent =_meta_table['RoutingPolicy.Sets.AsPath.Sets_.Set']['meta_info']
_meta_table['RoutingPolicy.Sets.AsPath.Sets_.Set.Attached']['meta_info'].parent =_meta_table['RoutingPolicy.Sets.AsPath.Sets_.Set']['meta_info']
_meta_table['RoutingPolicy.Sets.AsPath.Sets_.Set']['meta_info'].parent =_meta_table['RoutingPolicy.Sets.AsPath.Sets_']['meta_info']
_meta_table['RoutingPolicy.Sets.AsPath.Sets_']['meta_info'].parent =_meta_table['RoutingPolicy.Sets.AsPath']['meta_info']
_meta_table['RoutingPolicy.Sets.AsPath.Unused']['meta_info'].parent =_meta_table['RoutingPolicy.Sets.AsPath']['meta_info']
_meta_table['RoutingPolicy.Sets.AsPath.Inactive']['meta_info'].parent =_meta_table['RoutingPolicy.Sets.AsPath']['meta_info']
_meta_table['RoutingPolicy.Sets.AsPath.Active']['meta_info'].parent =_meta_table['RoutingPolicy.Sets.AsPath']['meta_info']
_meta_table['RoutingPolicy.Sets.LargeCommunity.Sets_.Set.UsedBy.Reference']['meta_info'].parent =_meta_table['RoutingPolicy.Sets.LargeCommunity.Sets_.Set.UsedBy']['meta_info']
_meta_table['RoutingPolicy.Sets.LargeCommunity.Sets_.Set.Attached.Binding']['meta_info'].parent =_meta_table['RoutingPolicy.Sets.LargeCommunity.Sets_.Set.Attached']['meta_info']
_meta_table['RoutingPolicy.Sets.LargeCommunity.Sets_.Set.UsedBy']['meta_info'].parent =_meta_table['RoutingPolicy.Sets.LargeCommunity.Sets_.Set']['meta_info']
_meta_table['RoutingPolicy.Sets.LargeCommunity.Sets_.Set.Attached']['meta_info'].parent =_meta_table['RoutingPolicy.Sets.LargeCommunity.Sets_.Set']['meta_info']
_meta_table['RoutingPolicy.Sets.LargeCommunity.Sets_.Set']['meta_info'].parent =_meta_table['RoutingPolicy.Sets.LargeCommunity.Sets_']['meta_info']
_meta_table['RoutingPolicy.Sets.LargeCommunity.Sets_']['meta_info'].parent =_meta_table['RoutingPolicy.Sets.LargeCommunity']['meta_info']
_meta_table['RoutingPolicy.Sets.LargeCommunity.Unused']['meta_info'].parent =_meta_table['RoutingPolicy.Sets.LargeCommunity']['meta_info']
_meta_table['RoutingPolicy.Sets.LargeCommunity.Inactive']['meta_info'].parent =_meta_table['RoutingPolicy.Sets.LargeCommunity']['meta_info']
_meta_table['RoutingPolicy.Sets.LargeCommunity.Active']['meta_info'].parent =_meta_table['RoutingPolicy.Sets.LargeCommunity']['meta_info']
_meta_table['RoutingPolicy.Sets.Esi.Sets_.Set.UsedBy.Reference']['meta_info'].parent =_meta_table['RoutingPolicy.Sets.Esi.Sets_.Set.UsedBy']['meta_info']
_meta_table['RoutingPolicy.Sets.Esi.Sets_.Set.Attached.Binding']['meta_info'].parent =_meta_table['RoutingPolicy.Sets.Esi.Sets_.Set.Attached']['meta_info']
_meta_table['RoutingPolicy.Sets.Esi.Sets_.Set.UsedBy']['meta_info'].parent =_meta_table['RoutingPolicy.Sets.Esi.Sets_.Set']['meta_info']
_meta_table['RoutingPolicy.Sets.Esi.Sets_.Set.Attached']['meta_info'].parent =_meta_table['RoutingPolicy.Sets.Esi.Sets_.Set']['meta_info']
_meta_table['RoutingPolicy.Sets.Esi.Sets_.Set']['meta_info'].parent =_meta_table['RoutingPolicy.Sets.Esi.Sets_']['meta_info']
_meta_table['RoutingPolicy.Sets.Esi.Sets_']['meta_info'].parent =_meta_table['RoutingPolicy.Sets.Esi']['meta_info']
_meta_table['RoutingPolicy.Sets.Esi.Unused']['meta_info'].parent =_meta_table['RoutingPolicy.Sets.Esi']['meta_info']
_meta_table['RoutingPolicy.Sets.Esi.Inactive']['meta_info'].parent =_meta_table['RoutingPolicy.Sets.Esi']['meta_info']
_meta_table['RoutingPolicy.Sets.Esi.Active']['meta_info'].parent =_meta_table['RoutingPolicy.Sets.Esi']['meta_info']
_meta_table['RoutingPolicy.Sets.ExtendedCommunityBandwidth.Sets_.Set.UsedBy.Reference']['meta_info'].parent =_meta_table['RoutingPolicy.Sets.ExtendedCommunityBandwidth.Sets_.Set.UsedBy']['meta_info']
_meta_table['RoutingPolicy.Sets.ExtendedCommunityBandwidth.Sets_.Set.Attached.Binding']['meta_info'].parent =_meta_table['RoutingPolicy.Sets.ExtendedCommunityBandwidth.Sets_.Set.Attached']['meta_info']
_meta_table['RoutingPolicy.Sets.ExtendedCommunityBandwidth.Sets_.Set.UsedBy']['meta_info'].parent =_meta_table['RoutingPolicy.Sets.ExtendedCommunityBandwidth.Sets_.Set']['meta_info']
_meta_table['RoutingPolicy.Sets.ExtendedCommunityBandwidth.Sets_.Set.Attached']['meta_info'].parent =_meta_table['RoutingPolicy.Sets.ExtendedCommunityBandwidth.Sets_.Set']['meta_info']
_meta_table['RoutingPolicy.Sets.ExtendedCommunityBandwidth.Sets_.Set']['meta_info'].parent =_meta_table['RoutingPolicy.Sets.ExtendedCommunityBandwidth.Sets_']['meta_info']
_meta_table['RoutingPolicy.Sets.ExtendedCommunityBandwidth.Sets_']['meta_info'].parent =_meta_table['RoutingPolicy.Sets.ExtendedCommunityBandwidth']['meta_info']
_meta_table['RoutingPolicy.Sets.ExtendedCommunityBandwidth.Unused']['meta_info'].parent =_meta_table['RoutingPolicy.Sets.ExtendedCommunityBandwidth']['meta_info']
_meta_table['RoutingPolicy.Sets.ExtendedCommunityBandwidth.Inactive']['meta_info'].parent =_meta_table['RoutingPolicy.Sets.ExtendedCommunityBandwidth']['meta_info']
_meta_table['RoutingPolicy.Sets.ExtendedCommunityRt.Sets_.Set.UsedBy.Reference']['meta_info'].parent =_meta_table['RoutingPolicy.Sets.ExtendedCommunityRt.Sets_.Set.UsedBy']['meta_info']
_meta_table['RoutingPolicy.Sets.ExtendedCommunityRt.Sets_.Set.Attached.Binding']['meta_info'].parent =_meta_table['RoutingPolicy.Sets.ExtendedCommunityRt.Sets_.Set.Attached']['meta_info']
_meta_table['RoutingPolicy.Sets.ExtendedCommunityRt.Sets_.Set.UsedBy']['meta_info'].parent =_meta_table['RoutingPolicy.Sets.ExtendedCommunityRt.Sets_.Set']['meta_info']
_meta_table['RoutingPolicy.Sets.ExtendedCommunityRt.Sets_.Set.Attached']['meta_info'].parent =_meta_table['RoutingPolicy.Sets.ExtendedCommunityRt.Sets_.Set']['meta_info']
_meta_table['RoutingPolicy.Sets.ExtendedCommunityRt.Sets_.Set']['meta_info'].parent =_meta_table['RoutingPolicy.Sets.ExtendedCommunityRt.Sets_']['meta_info']
_meta_table['RoutingPolicy.Sets.ExtendedCommunityRt.Sets_']['meta_info'].parent =_meta_table['RoutingPolicy.Sets.ExtendedCommunityRt']['meta_info']
_meta_table['RoutingPolicy.Sets.ExtendedCommunityRt.Unused']['meta_info'].parent =_meta_table['RoutingPolicy.Sets.ExtendedCommunityRt']['meta_info']
_meta_table['RoutingPolicy.Sets.ExtendedCommunityRt.Inactive']['meta_info'].parent =_meta_table['RoutingPolicy.Sets.ExtendedCommunityRt']['meta_info']
_meta_table['RoutingPolicy.Sets.ExtendedCommunityRt.Active']['meta_info'].parent =_meta_table['RoutingPolicy.Sets.ExtendedCommunityRt']['meta_info']
_meta_table['RoutingPolicy.Sets.Rd.Sets_.Set.UsedBy.Reference']['meta_info'].parent =_meta_table['RoutingPolicy.Sets.Rd.Sets_.Set.UsedBy']['meta_info']
_meta_table['RoutingPolicy.Sets.Rd.Sets_.Set.Attached.Binding']['meta_info'].parent =_meta_table['RoutingPolicy.Sets.Rd.Sets_.Set.Attached']['meta_info']
_meta_table['RoutingPolicy.Sets.Rd.Sets_.Set.UsedBy']['meta_info'].parent =_meta_table['RoutingPolicy.Sets.Rd.Sets_.Set']['meta_info']
_meta_table['RoutingPolicy.Sets.Rd.Sets_.Set.Attached']['meta_info'].parent =_meta_table['RoutingPolicy.Sets.Rd.Sets_.Set']['meta_info']
_meta_table['RoutingPolicy.Sets.Rd.Sets_.Set']['meta_info'].parent =_meta_table['RoutingPolicy.Sets.Rd.Sets_']['meta_info']
_meta_table['RoutingPolicy.Sets.Rd.Sets_']['meta_info'].parent =_meta_table['RoutingPolicy.Sets.Rd']['meta_info']
_meta_table['RoutingPolicy.Sets.Rd.Unused']['meta_info'].parent =_meta_table['RoutingPolicy.Sets.Rd']['meta_info']
_meta_table['RoutingPolicy.Sets.Rd.Inactive']['meta_info'].parent =_meta_table['RoutingPolicy.Sets.Rd']['meta_info']
_meta_table['RoutingPolicy.Sets.Rd.Active']['meta_info'].parent =_meta_table['RoutingPolicy.Sets.Rd']['meta_info']
_meta_table['RoutingPolicy.Sets.Mac.Sets_.Set.UsedBy.Reference']['meta_info'].parent =_meta_table['RoutingPolicy.Sets.Mac.Sets_.Set.UsedBy']['meta_info']
_meta_table['RoutingPolicy.Sets.Mac.Sets_.Set.Attached.Binding']['meta_info'].parent =_meta_table['RoutingPolicy.Sets.Mac.Sets_.Set.Attached']['meta_info']
_meta_table['RoutingPolicy.Sets.Mac.Sets_.Set.UsedBy']['meta_info'].parent =_meta_table['RoutingPolicy.Sets.Mac.Sets_.Set']['meta_info']
_meta_table['RoutingPolicy.Sets.Mac.Sets_.Set.Attached']['meta_info'].parent =_meta_table['RoutingPolicy.Sets.Mac.Sets_.Set']['meta_info']
_meta_table['RoutingPolicy.Sets.Mac.Sets_.Set']['meta_info'].parent =_meta_table['RoutingPolicy.Sets.Mac.Sets_']['meta_info']
_meta_table['RoutingPolicy.Sets.Mac.Sets_']['meta_info'].parent =_meta_table['RoutingPolicy.Sets.Mac']['meta_info']
_meta_table['RoutingPolicy.Sets.Mac.Unused']['meta_info'].parent =_meta_table['RoutingPolicy.Sets.Mac']['meta_info']
_meta_table['RoutingPolicy.Sets.Mac.Inactive']['meta_info'].parent =_meta_table['RoutingPolicy.Sets.Mac']['meta_info']
_meta_table['RoutingPolicy.Sets.Mac.Active']['meta_info'].parent =_meta_table['RoutingPolicy.Sets.Mac']['meta_info']
_meta_table['RoutingPolicy.Sets.ExtendedCommunityCost.Sets_.Set.UsedBy.Reference']['meta_info'].parent =_meta_table['RoutingPolicy.Sets.ExtendedCommunityCost.Sets_.Set.UsedBy']['meta_info']
_meta_table['RoutingPolicy.Sets.ExtendedCommunityCost.Sets_.Set.Attached.Binding']['meta_info'].parent =_meta_table['RoutingPolicy.Sets.ExtendedCommunityCost.Sets_.Set.Attached']['meta_info']
_meta_table['RoutingPolicy.Sets.ExtendedCommunityCost.Sets_.Set.UsedBy']['meta_info'].parent =_meta_table['RoutingPolicy.Sets.ExtendedCommunityCost.Sets_.Set']['meta_info']
_meta_table['RoutingPolicy.Sets.ExtendedCommunityCost.Sets_.Set.Attached']['meta_info'].parent =_meta_table['RoutingPolicy.Sets.ExtendedCommunityCost.Sets_.Set']['meta_info']
_meta_table['RoutingPolicy.Sets.ExtendedCommunityCost.Sets_.Set']['meta_info'].parent =_meta_table['RoutingPolicy.Sets.ExtendedCommunityCost.Sets_']['meta_info']
_meta_table['RoutingPolicy.Sets.ExtendedCommunityCost.Sets_']['meta_info'].parent =_meta_table['RoutingPolicy.Sets.ExtendedCommunityCost']['meta_info']
_meta_table['RoutingPolicy.Sets.ExtendedCommunityCost.Unused']['meta_info'].parent =_meta_table['RoutingPolicy.Sets.ExtendedCommunityCost']['meta_info']
_meta_table['RoutingPolicy.Sets.ExtendedCommunityCost.Inactive']['meta_info'].parent =_meta_table['RoutingPolicy.Sets.ExtendedCommunityCost']['meta_info']
_meta_table['RoutingPolicy.Sets.ExtendedCommunityCost.Active']['meta_info'].parent =_meta_table['RoutingPolicy.Sets.ExtendedCommunityCost']['meta_info']
_meta_table['RoutingPolicy.Sets.Etag']['meta_info'].parent =_meta_table['RoutingPolicy.Sets']['meta_info']
_meta_table['RoutingPolicy.Sets.OspfArea']['meta_info'].parent =_meta_table['RoutingPolicy.Sets']['meta_info']
_meta_table['RoutingPolicy.Sets.ExtendedCommunityOpaque']['meta_info'].parent =_meta_table['RoutingPolicy.Sets']['meta_info']
_meta_table['RoutingPolicy.Sets.ExtendedCommunitySegNh']['meta_info'].parent =_meta_table['RoutingPolicy.Sets']['meta_info']
_meta_table['RoutingPolicy.Sets.ExtendedCommunitySoo']['meta_info'].parent =_meta_table['RoutingPolicy.Sets']['meta_info']
_meta_table['RoutingPolicy.Sets.Tag']['meta_info'].parent =_meta_table['RoutingPolicy.Sets']['meta_info']
_meta_table['RoutingPolicy.Sets.Prefix']['meta_info'].parent =_meta_table['RoutingPolicy.Sets']['meta_info']
_meta_table['RoutingPolicy.Sets.Community']['meta_info'].parent =_meta_table['RoutingPolicy.Sets']['meta_info']
_meta_table['RoutingPolicy.Sets.AsPath']['meta_info'].parent =_meta_table['RoutingPolicy.Sets']['meta_info']
_meta_table['RoutingPolicy.Sets.LargeCommunity']['meta_info'].parent =_meta_table['RoutingPolicy.Sets']['meta_info']
_meta_table['RoutingPolicy.Sets.Esi']['meta_info'].parent =_meta_table['RoutingPolicy.Sets']['meta_info']
_meta_table['RoutingPolicy.Sets.ExtendedCommunityBandwidth']['meta_info'].parent =_meta_table['RoutingPolicy.Sets']['meta_info']
_meta_table['RoutingPolicy.Sets.ExtendedCommunityRt']['meta_info'].parent =_meta_table['RoutingPolicy.Sets']['meta_info']
_meta_table['RoutingPolicy.Sets.Rd']['meta_info'].parent =_meta_table['RoutingPolicy.Sets']['meta_info']
_meta_table['RoutingPolicy.Sets.Mac']['meta_info'].parent =_meta_table['RoutingPolicy.Sets']['meta_info']
_meta_table['RoutingPolicy.Sets.ExtendedCommunityCost']['meta_info'].parent =_meta_table['RoutingPolicy.Sets']['meta_info']
_meta_table['RoutingPolicy.Limits']['meta_info'].parent =_meta_table['RoutingPolicy']['meta_info']
_meta_table['RoutingPolicy.Policies']['meta_info'].parent =_meta_table['RoutingPolicy']['meta_info']
_meta_table['RoutingPolicy.Sets']['meta_info'].parent =_meta_table['RoutingPolicy']['meta_info']
_meta_table['RoutingPolicyShadow.Policies.RoutePolicies.RoutePolicy.PolicyUses.AllUsedSets.Sets']['meta_info'].parent =_meta_table['RoutingPolicyShadow.Policies.RoutePolicies.RoutePolicy.PolicyUses.AllUsedSets']['meta_info']
_meta_table['RoutingPolicyShadow.Policies.RoutePolicies.RoutePolicy.PolicyUses.DirectlyUsedSets.Sets']['meta_info'].parent =_meta_table['RoutingPolicyShadow.Policies.RoutePolicies.RoutePolicy.PolicyUses.DirectlyUsedSets']['meta_info']
_meta_table['RoutingPolicyShadow.Policies.RoutePolicies.RoutePolicy.PolicyUses.DirectlyUsedPolicies']['meta_info'].parent =_meta_table['RoutingPolicyShadow.Policies.RoutePolicies.RoutePolicy.PolicyUses']['meta_info']
_meta_table['RoutingPolicyShadow.Policies.RoutePolicies.RoutePolicy.PolicyUses.AllUsedSets']['meta_info'].parent =_meta_table['RoutingPolicyShadow.Policies.RoutePolicies.RoutePolicy.PolicyUses']['meta_info']
_meta_table['RoutingPolicyShadow.Policies.RoutePolicies.RoutePolicy.PolicyUses.DirectlyUsedSets']['meta_info'].parent =_meta_table['RoutingPolicyShadow.Policies.RoutePolicies.RoutePolicy.PolicyUses']['meta_info']
_meta_table['RoutingPolicyShadow.Policies.RoutePolicies.RoutePolicy.PolicyUses.AllUsedPolicies']['meta_info'].parent =_meta_table['RoutingPolicyShadow.Policies.RoutePolicies.RoutePolicy.PolicyUses']['meta_info']
_meta_table['RoutingPolicyShadow.Policies.RoutePolicies.RoutePolicy.UsedBy.Reference']['meta_info'].parent =_meta_table['RoutingPolicyShadow.Policies.RoutePolicies.RoutePolicy.UsedBy']['meta_info']
_meta_table['RoutingPolicyShadow.Policies.RoutePolicies.RoutePolicy.Attached.Binding']['meta_info'].parent =_meta_table['RoutingPolicyShadow.Policies.RoutePolicies.RoutePolicy.Attached']['meta_info']
_meta_table['RoutingPolicyShadow.Policies.RoutePolicies.RoutePolicy.PolicyUses']['meta_info'].parent =_meta_table['RoutingPolicyShadow.Policies.RoutePolicies.RoutePolicy']['meta_info']
_meta_table['RoutingPolicyShadow.Policies.RoutePolicies.RoutePolicy.UsedBy']['meta_info'].parent =_meta_table['RoutingPolicyShadow.Policies.RoutePolicies.RoutePolicy']['meta_info']
_meta_table['RoutingPolicyShadow.Policies.RoutePolicies.RoutePolicy.Attached']['meta_info'].parent =_meta_table['RoutingPolicyShadow.Policies.RoutePolicies.RoutePolicy']['meta_info']
_meta_table['RoutingPolicyShadow.Policies.RoutePolicies.RoutePolicy']['meta_info'].parent =_meta_table['RoutingPolicyShadow.Policies.RoutePolicies']['meta_info']
_meta_table['RoutingPolicyShadow.Policies.RoutePolicies']['meta_info'].parent =_meta_table['RoutingPolicyShadow.Policies']['meta_info']
_meta_table['RoutingPolicyShadow.Policies.Unused']['meta_info'].parent =_meta_table['RoutingPolicyShadow.Policies']['meta_info']
_meta_table['RoutingPolicyShadow.Policies.Inactive']['meta_info'].parent =_meta_table['RoutingPolicyShadow.Policies']['meta_info']
_meta_table['RoutingPolicyShadow.Policies.Active']['meta_info'].parent =_meta_table['RoutingPolicyShadow.Policies']['meta_info']
_meta_table['RoutingPolicyShadow.Sets.Etag.Sets_.Set.UsedBy.Reference']['meta_info'].parent =_meta_table['RoutingPolicyShadow.Sets.Etag.Sets_.Set.UsedBy']['meta_info']
_meta_table['RoutingPolicyShadow.Sets.Etag.Sets_.Set.Attached.Binding']['meta_info'].parent =_meta_table['RoutingPolicyShadow.Sets.Etag.Sets_.Set.Attached']['meta_info']
_meta_table['RoutingPolicyShadow.Sets.Etag.Sets_.Set.UsedBy']['meta_info'].parent =_meta_table['RoutingPolicyShadow.Sets.Etag.Sets_.Set']['meta_info']
_meta_table['RoutingPolicyShadow.Sets.Etag.Sets_.Set.Attached']['meta_info'].parent =_meta_table['RoutingPolicyShadow.Sets.Etag.Sets_.Set']['meta_info']
_meta_table['RoutingPolicyShadow.Sets.Etag.Sets_.Set']['meta_info'].parent =_meta_table['RoutingPolicyShadow.Sets.Etag.Sets_']['meta_info']
_meta_table['RoutingPolicyShadow.Sets.Etag.Sets_']['meta_info'].parent =_meta_table['RoutingPolicyShadow.Sets.Etag']['meta_info']
_meta_table['RoutingPolicyShadow.Sets.Etag.Unused']['meta_info'].parent =_meta_table['RoutingPolicyShadow.Sets.Etag']['meta_info']
_meta_table['RoutingPolicyShadow.Sets.Etag.Inactive']['meta_info'].parent =_meta_table['RoutingPolicyShadow.Sets.Etag']['meta_info']
_meta_table['RoutingPolicyShadow.Sets.Etag.Active']['meta_info'].parent =_meta_table['RoutingPolicyShadow.Sets.Etag']['meta_info']
_meta_table['RoutingPolicyShadow.Sets.OspfArea.Sets_.Set.UsedBy.Reference']['meta_info'].parent =_meta_table['RoutingPolicyShadow.Sets.OspfArea.Sets_.Set.UsedBy']['meta_info']
_meta_table['RoutingPolicyShadow.Sets.OspfArea.Sets_.Set.Attached.Binding']['meta_info'].parent =_meta_table['RoutingPolicyShadow.Sets.OspfArea.Sets_.Set.Attached']['meta_info']
_meta_table['RoutingPolicyShadow.Sets.OspfArea.Sets_.Set.UsedBy']['meta_info'].parent =_meta_table['RoutingPolicyShadow.Sets.OspfArea.Sets_.Set']['meta_info']
_meta_table['RoutingPolicyShadow.Sets.OspfArea.Sets_.Set.Attached']['meta_info'].parent =_meta_table['RoutingPolicyShadow.Sets.OspfArea.Sets_.Set']['meta_info']
_meta_table['RoutingPolicyShadow.Sets.OspfArea.Sets_.Set']['meta_info'].parent =_meta_table['RoutingPolicyShadow.Sets.OspfArea.Sets_']['meta_info']
_meta_table['RoutingPolicyShadow.Sets.OspfArea.Sets_']['meta_info'].parent =_meta_table['RoutingPolicyShadow.Sets.OspfArea']['meta_info']
_meta_table['RoutingPolicyShadow.Sets.OspfArea.Unused']['meta_info'].parent =_meta_table['RoutingPolicyShadow.Sets.OspfArea']['meta_info']
_meta_table['RoutingPolicyShadow.Sets.OspfArea.Inactive']['meta_info'].parent =_meta_table['RoutingPolicyShadow.Sets.OspfArea']['meta_info']
_meta_table['RoutingPolicyShadow.Sets.OspfArea.Active']['meta_info'].parent =_meta_table['RoutingPolicyShadow.Sets.OspfArea']['meta_info']
_meta_table['RoutingPolicyShadow.Sets.ExtendedCommunityOpaque.Sets_.Set.UsedBy.Reference']['meta_info'].parent =_meta_table['RoutingPolicyShadow.Sets.ExtendedCommunityOpaque.Sets_.Set.UsedBy']['meta_info']
_meta_table['RoutingPolicyShadow.Sets.ExtendedCommunityOpaque.Sets_.Set.Attached.Binding']['meta_info'].parent =_meta_table['RoutingPolicyShadow.Sets.ExtendedCommunityOpaque.Sets_.Set.Attached']['meta_info']
_meta_table['RoutingPolicyShadow.Sets.ExtendedCommunityOpaque.Sets_.Set.UsedBy']['meta_info'].parent =_meta_table['RoutingPolicyShadow.Sets.ExtendedCommunityOpaque.Sets_.Set']['meta_info']
_meta_table['RoutingPolicyShadow.Sets.ExtendedCommunityOpaque.Sets_.Set.Attached']['meta_info'].parent =_meta_table['RoutingPolicyShadow.Sets.ExtendedCommunityOpaque.Sets_.Set']['meta_info']
_meta_table['RoutingPolicyShadow.Sets.ExtendedCommunityOpaque.Sets_.Set']['meta_info'].parent =_meta_table['RoutingPolicyShadow.Sets.ExtendedCommunityOpaque.Sets_']['meta_info']
_meta_table['RoutingPolicyShadow.Sets.ExtendedCommunityOpaque.Sets_']['meta_info'].parent =_meta_table['RoutingPolicyShadow.Sets.ExtendedCommunityOpaque']['meta_info']
_meta_table['RoutingPolicyShadow.Sets.ExtendedCommunityOpaque.Unused']['meta_info'].parent =_meta_table['RoutingPolicyShadow.Sets.ExtendedCommunityOpaque']['meta_info']
_meta_table['RoutingPolicyShadow.Sets.ExtendedCommunityOpaque.Inactive']['meta_info'].parent =_meta_table['RoutingPolicyShadow.Sets.ExtendedCommunityOpaque']['meta_info']
_meta_table['RoutingPolicyShadow.Sets.ExtendedCommunityOpaque.Active']['meta_info'].parent =_meta_table['RoutingPolicyShadow.Sets.ExtendedCommunityOpaque']['meta_info']
_meta_table['RoutingPolicyShadow.Sets.ExtendedCommunitySegNh.Sets_.Set.UsedBy.Reference']['meta_info'].parent =_meta_table['RoutingPolicyShadow.Sets.ExtendedCommunitySegNh.Sets_.Set.UsedBy']['meta_info']
_meta_table['RoutingPolicyShadow.Sets.ExtendedCommunitySegNh.Sets_.Set.Attached.Binding']['meta_info'].parent =_meta_table['RoutingPolicyShadow.Sets.ExtendedCommunitySegNh.Sets_.Set.Attached']['meta_info']
_meta_table['RoutingPolicyShadow.Sets.ExtendedCommunitySegNh.Sets_.Set.UsedBy']['meta_info'].parent =_meta_table['RoutingPolicyShadow.Sets.ExtendedCommunitySegNh.Sets_.Set']['meta_info']
_meta_table['RoutingPolicyShadow.Sets.ExtendedCommunitySegNh.Sets_.Set.Attached']['meta_info'].parent =_meta_table['RoutingPolicyShadow.Sets.ExtendedCommunitySegNh.Sets_.Set']['meta_info']
_meta_table['RoutingPolicyShadow.Sets.ExtendedCommunitySegNh.Sets_.Set']['meta_info'].parent =_meta_table['RoutingPolicyShadow.Sets.ExtendedCommunitySegNh.Sets_']['meta_info']
_meta_table['RoutingPolicyShadow.Sets.ExtendedCommunitySegNh.Sets_']['meta_info'].parent =_meta_table['RoutingPolicyShadow.Sets.ExtendedCommunitySegNh']['meta_info']
_meta_table['RoutingPolicyShadow.Sets.ExtendedCommunitySegNh.Unused']['meta_info'].parent =_meta_table['RoutingPolicyShadow.Sets.ExtendedCommunitySegNh']['meta_info']
_meta_table['RoutingPolicyShadow.Sets.ExtendedCommunitySegNh.Inactive']['meta_info'].parent =_meta_table['RoutingPolicyShadow.Sets.ExtendedCommunitySegNh']['meta_info']
_meta_table['RoutingPolicyShadow.Sets.ExtendedCommunitySegNh.Active']['meta_info'].parent =_meta_table['RoutingPolicyShadow.Sets.ExtendedCommunitySegNh']['meta_info']
_meta_table['RoutingPolicyShadow.Sets.ExtendedCommunitySoo.Sets_.Set.UsedBy.Reference']['meta_info'].parent =_meta_table['RoutingPolicyShadow.Sets.ExtendedCommunitySoo.Sets_.Set.UsedBy']['meta_info']
_meta_table['RoutingPolicyShadow.Sets.ExtendedCommunitySoo.Sets_.Set.Attached.Binding']['meta_info'].parent =_meta_table['RoutingPolicyShadow.Sets.ExtendedCommunitySoo.Sets_.Set.Attached']['meta_info']
_meta_table['RoutingPolicyShadow.Sets.ExtendedCommunitySoo.Sets_.Set.UsedBy']['meta_info'].parent =_meta_table['RoutingPolicyShadow.Sets.ExtendedCommunitySoo.Sets_.Set']['meta_info']
_meta_table['RoutingPolicyShadow.Sets.ExtendedCommunitySoo.Sets_.Set.Attached']['meta_info'].parent =_meta_table['RoutingPolicyShadow.Sets.ExtendedCommunitySoo.Sets_.Set']['meta_info']
_meta_table['RoutingPolicyShadow.Sets.ExtendedCommunitySoo.Sets_.Set']['meta_info'].parent =_meta_table['RoutingPolicyShadow.Sets.ExtendedCommunitySoo.Sets_']['meta_info']
_meta_table['RoutingPolicyShadow.Sets.ExtendedCommunitySoo.Sets_']['meta_info'].parent =_meta_table['RoutingPolicyShadow.Sets.ExtendedCommunitySoo']['meta_info']
_meta_table['RoutingPolicyShadow.Sets.ExtendedCommunitySoo.Unused']['meta_info'].parent =_meta_table['RoutingPolicyShadow.Sets.ExtendedCommunitySoo']['meta_info']
_meta_table['RoutingPolicyShadow.Sets.ExtendedCommunitySoo.Inactive']['meta_info'].parent =_meta_table['RoutingPolicyShadow.Sets.ExtendedCommunitySoo']['meta_info']
_meta_table['RoutingPolicyShadow.Sets.ExtendedCommunitySoo.Active']['meta_info'].parent =_meta_table['RoutingPolicyShadow.Sets.ExtendedCommunitySoo']['meta_info']
_meta_table['RoutingPolicyShadow.Sets.Tag.Sets_.Set.UsedBy.Reference']['meta_info'].parent =_meta_table['RoutingPolicyShadow.Sets.Tag.Sets_.Set.UsedBy']['meta_info']
_meta_table['RoutingPolicyShadow.Sets.Tag.Sets_.Set.Attached.Binding']['meta_info'].parent =_meta_table['RoutingPolicyShadow.Sets.Tag.Sets_.Set.Attached']['meta_info']
_meta_table['RoutingPolicyShadow.Sets.Tag.Sets_.Set.UsedBy']['meta_info'].parent =_meta_table['RoutingPolicyShadow.Sets.Tag.Sets_.Set']['meta_info']
_meta_table['RoutingPolicyShadow.Sets.Tag.Sets_.Set.Attached']['meta_info'].parent =_meta_table['RoutingPolicyShadow.Sets.Tag.Sets_.Set']['meta_info']
_meta_table['RoutingPolicyShadow.Sets.Tag.Sets_.Set']['meta_info'].parent =_meta_table['RoutingPolicyShadow.Sets.Tag.Sets_']['meta_info']
_meta_table['RoutingPolicyShadow.Sets.Tag.Sets_']['meta_info'].parent =_meta_table['RoutingPolicyShadow.Sets.Tag']['meta_info']
_meta_table['RoutingPolicyShadow.Sets.Tag.Unused']['meta_info'].parent =_meta_table['RoutingPolicyShadow.Sets.Tag']['meta_info']
_meta_table['RoutingPolicyShadow.Sets.Tag.Inactive']['meta_info'].parent =_meta_table['RoutingPolicyShadow.Sets.Tag']['meta_info']
_meta_table['RoutingPolicyShadow.Sets.Tag.Active']['meta_info'].parent =_meta_table['RoutingPolicyShadow.Sets.Tag']['meta_info']
_meta_table['RoutingPolicyShadow.Sets.Prefix.Sets_.Set.UsedBy.Reference']['meta_info'].parent =_meta_table['RoutingPolicyShadow.Sets.Prefix.Sets_.Set.UsedBy']['meta_info']
_meta_table['RoutingPolicyShadow.Sets.Prefix.Sets_.Set.Attached.Binding']['meta_info'].parent =_meta_table['RoutingPolicyShadow.Sets.Prefix.Sets_.Set.Attached']['meta_info']
_meta_table['RoutingPolicyShadow.Sets.Prefix.Sets_.Set.UsedBy']['meta_info'].parent =_meta_table['RoutingPolicyShadow.Sets.Prefix.Sets_.Set']['meta_info']
_meta_table['RoutingPolicyShadow.Sets.Prefix.Sets_.Set.Attached']['meta_info'].parent =_meta_table['RoutingPolicyShadow.Sets.Prefix.Sets_.Set']['meta_info']
_meta_table['RoutingPolicyShadow.Sets.Prefix.Sets_.Set']['meta_info'].parent =_meta_table['RoutingPolicyShadow.Sets.Prefix.Sets_']['meta_info']
_meta_table['RoutingPolicyShadow.Sets.Prefix.Sets_']['meta_info'].parent =_meta_table['RoutingPolicyShadow.Sets.Prefix']['meta_info']
_meta_table['RoutingPolicyShadow.Sets.Prefix.Unused']['meta_info'].parent =_meta_table['RoutingPolicyShadow.Sets.Prefix']['meta_info']
_meta_table['RoutingPolicyShadow.Sets.Prefix.Inactive']['meta_info'].parent =_meta_table['RoutingPolicyShadow.Sets.Prefix']['meta_info']
_meta_table['RoutingPolicyShadow.Sets.Prefix.Active']['meta_info'].parent =_meta_table['RoutingPolicyShadow.Sets.Prefix']['meta_info']
_meta_table['RoutingPolicyShadow.Sets.Community.Sets_.Set.UsedBy.Reference']['meta_info'].parent =_meta_table['RoutingPolicyShadow.Sets.Community.Sets_.Set.UsedBy']['meta_info']
_meta_table['RoutingPolicyShadow.Sets.Community.Sets_.Set.Attached.Binding']['meta_info'].parent =_meta_table['RoutingPolicyShadow.Sets.Community.Sets_.Set.Attached']['meta_info']
_meta_table['RoutingPolicyShadow.Sets.Community.Sets_.Set.UsedBy']['meta_info'].parent =_meta_table['RoutingPolicyShadow.Sets.Community.Sets_.Set']['meta_info']
_meta_table['RoutingPolicyShadow.Sets.Community.Sets_.Set.Attached']['meta_info'].parent =_meta_table['RoutingPolicyShadow.Sets.Community.Sets_.Set']['meta_info']
_meta_table['RoutingPolicyShadow.Sets.Community.Sets_.Set']['meta_info'].parent =_meta_table['RoutingPolicyShadow.Sets.Community.Sets_']['meta_info']
_meta_table['RoutingPolicyShadow.Sets.Community.Sets_']['meta_info'].parent =_meta_table['RoutingPolicyShadow.Sets.Community']['meta_info']
_meta_table['RoutingPolicyShadow.Sets.Community.Unused']['meta_info'].parent =_meta_table['RoutingPolicyShadow.Sets.Community']['meta_info']
_meta_table['RoutingPolicyShadow.Sets.Community.Inactive']['meta_info'].parent =_meta_table['RoutingPolicyShadow.Sets.Community']['meta_info']
_meta_table['RoutingPolicyShadow.Sets.Community.Active']['meta_info'].parent =_meta_table['RoutingPolicyShadow.Sets.Community']['meta_info']
_meta_table['RoutingPolicyShadow.Sets.AsPath.Sets_.Set.UsedBy.Reference']['meta_info'].parent =_meta_table['RoutingPolicyShadow.Sets.AsPath.Sets_.Set.UsedBy']['meta_info']
_meta_table['RoutingPolicyShadow.Sets.AsPath.Sets_.Set.Attached.Binding']['meta_info'].parent =_meta_table['RoutingPolicyShadow.Sets.AsPath.Sets_.Set.Attached']['meta_info']
_meta_table['RoutingPolicyShadow.Sets.AsPath.Sets_.Set.UsedBy']['meta_info'].parent =_meta_table['RoutingPolicyShadow.Sets.AsPath.Sets_.Set']['meta_info']
_meta_table['RoutingPolicyShadow.Sets.AsPath.Sets_.Set.Attached']['meta_info'].parent =_meta_table['RoutingPolicyShadow.Sets.AsPath.Sets_.Set']['meta_info']
_meta_table['RoutingPolicyShadow.Sets.AsPath.Sets_.Set']['meta_info'].parent =_meta_table['RoutingPolicyShadow.Sets.AsPath.Sets_']['meta_info']
_meta_table['RoutingPolicyShadow.Sets.AsPath.Sets_']['meta_info'].parent =_meta_table['RoutingPolicyShadow.Sets.AsPath']['meta_info']
_meta_table['RoutingPolicyShadow.Sets.AsPath.Unused']['meta_info'].parent =_meta_table['RoutingPolicyShadow.Sets.AsPath']['meta_info']
_meta_table['RoutingPolicyShadow.Sets.AsPath.Inactive']['meta_info'].parent =_meta_table['RoutingPolicyShadow.Sets.AsPath']['meta_info']
_meta_table['RoutingPolicyShadow.Sets.AsPath.Active']['meta_info'].parent =_meta_table['RoutingPolicyShadow.Sets.AsPath']['meta_info']
_meta_table['RoutingPolicyShadow.Sets.LargeCommunity.Sets_.Set.UsedBy.Reference']['meta_info'].parent =_meta_table['RoutingPolicyShadow.Sets.LargeCommunity.Sets_.Set.UsedBy']['meta_info']
_meta_table['RoutingPolicyShadow.Sets.LargeCommunity.Sets_.Set.Attached.Binding']['meta_info'].parent =_meta_table['RoutingPolicyShadow.Sets.LargeCommunity.Sets_.Set.Attached']['meta_info']
_meta_table['RoutingPolicyShadow.Sets.LargeCommunity.Sets_.Set.UsedBy']['meta_info'].parent =_meta_table['RoutingPolicyShadow.Sets.LargeCommunity.Sets_.Set']['meta_info']
_meta_table['RoutingPolicyShadow.Sets.LargeCommunity.Sets_.Set.Attached']['meta_info'].parent =_meta_table['RoutingPolicyShadow.Sets.LargeCommunity.Sets_.Set']['meta_info']
_meta_table['RoutingPolicyShadow.Sets.LargeCommunity.Sets_.Set']['meta_info'].parent =_meta_table['RoutingPolicyShadow.Sets.LargeCommunity.Sets_']['meta_info']
_meta_table['RoutingPolicyShadow.Sets.LargeCommunity.Sets_']['meta_info'].parent =_meta_table['RoutingPolicyShadow.Sets.LargeCommunity']['meta_info']
_meta_table['RoutingPolicyShadow.Sets.LargeCommunity.Unused']['meta_info'].parent =_meta_table['RoutingPolicyShadow.Sets.LargeCommunity']['meta_info']
_meta_table['RoutingPolicyShadow.Sets.LargeCommunity.Inactive']['meta_info'].parent =_meta_table['RoutingPolicyShadow.Sets.LargeCommunity']['meta_info']
_meta_table['RoutingPolicyShadow.Sets.LargeCommunity.Active']['meta_info'].parent =_meta_table['RoutingPolicyShadow.Sets.LargeCommunity']['meta_info']
_meta_table['RoutingPolicyShadow.Sets.Esi.Sets_.Set.UsedBy.Reference']['meta_info'].parent =_meta_table['RoutingPolicyShadow.Sets.Esi.Sets_.Set.UsedBy']['meta_info']
_meta_table['RoutingPolicyShadow.Sets.Esi.Sets_.Set.Attached.Binding']['meta_info'].parent =_meta_table['RoutingPolicyShadow.Sets.Esi.Sets_.Set.Attached']['meta_info']
_meta_table['RoutingPolicyShadow.Sets.Esi.Sets_.Set.UsedBy']['meta_info'].parent =_meta_table['RoutingPolicyShadow.Sets.Esi.Sets_.Set']['meta_info']
_meta_table['RoutingPolicyShadow.Sets.Esi.Sets_.Set.Attached']['meta_info'].parent =_meta_table['RoutingPolicyShadow.Sets.Esi.Sets_.Set']['meta_info']
_meta_table['RoutingPolicyShadow.Sets.Esi.Sets_.Set']['meta_info'].parent =_meta_table['RoutingPolicyShadow.Sets.Esi.Sets_']['meta_info']
_meta_table['RoutingPolicyShadow.Sets.Esi.Sets_']['meta_info'].parent =_meta_table['RoutingPolicyShadow.Sets.Esi']['meta_info']
_meta_table['RoutingPolicyShadow.Sets.Esi.Unused']['meta_info'].parent =_meta_table['RoutingPolicyShadow.Sets.Esi']['meta_info']
_meta_table['RoutingPolicyShadow.Sets.Esi.Inactive']['meta_info'].parent =_meta_table['RoutingPolicyShadow.Sets.Esi']['meta_info']
_meta_table['RoutingPolicyShadow.Sets.Esi.Active']['meta_info'].parent =_meta_table['RoutingPolicyShadow.Sets.Esi']['meta_info']
_meta_table['RoutingPolicyShadow.Sets.ExtendedCommunityBandwidth.Sets_.Set.UsedBy.Reference']['meta_info'].parent =_meta_table['RoutingPolicyShadow.Sets.ExtendedCommunityBandwidth.Sets_.Set.UsedBy']['meta_info']
_meta_table['RoutingPolicyShadow.Sets.ExtendedCommunityBandwidth.Sets_.Set.Attached.Binding']['meta_info'].parent =_meta_table['RoutingPolicyShadow.Sets.ExtendedCommunityBandwidth.Sets_.Set.Attached']['meta_info']
_meta_table['RoutingPolicyShadow.Sets.ExtendedCommunityBandwidth.Sets_.Set.UsedBy']['meta_info'].parent =_meta_table['RoutingPolicyShadow.Sets.ExtendedCommunityBandwidth.Sets_.Set']['meta_info']
_meta_table['RoutingPolicyShadow.Sets.ExtendedCommunityBandwidth.Sets_.Set.Attached']['meta_info'].parent =_meta_table['RoutingPolicyShadow.Sets.ExtendedCommunityBandwidth.Sets_.Set']['meta_info']
_meta_table['RoutingPolicyShadow.Sets.ExtendedCommunityBandwidth.Sets_.Set']['meta_info'].parent =_meta_table['RoutingPolicyShadow.Sets.ExtendedCommunityBandwidth.Sets_']['meta_info']
_meta_table['RoutingPolicyShadow.Sets.ExtendedCommunityBandwidth.Sets_']['meta_info'].parent =_meta_table['RoutingPolicyShadow.Sets.ExtendedCommunityBandwidth']['meta_info']
_meta_table['RoutingPolicyShadow.Sets.ExtendedCommunityBandwidth.Unused']['meta_info'].parent =_meta_table['RoutingPolicyShadow.Sets.ExtendedCommunityBandwidth']['meta_info']
_meta_table['RoutingPolicyShadow.Sets.ExtendedCommunityBandwidth.Inactive']['meta_info'].parent =_meta_table['RoutingPolicyShadow.Sets.ExtendedCommunityBandwidth']['meta_info']
_meta_table['RoutingPolicyShadow.Sets.ExtendedCommunityRt.Sets_.Set.UsedBy.Reference']['meta_info'].parent =_meta_table['RoutingPolicyShadow.Sets.ExtendedCommunityRt.Sets_.Set.UsedBy']['meta_info']
_meta_table['RoutingPolicyShadow.Sets.ExtendedCommunityRt.Sets_.Set.Attached.Binding']['meta_info'].parent =_meta_table['RoutingPolicyShadow.Sets.ExtendedCommunityRt.Sets_.Set.Attached']['meta_info']
_meta_table['RoutingPolicyShadow.Sets.ExtendedCommunityRt.Sets_.Set.UsedBy']['meta_info'].parent =_meta_table['RoutingPolicyShadow.Sets.ExtendedCommunityRt.Sets_.Set']['meta_info']
_meta_table['RoutingPolicyShadow.Sets.ExtendedCommunityRt.Sets_.Set.Attached']['meta_info'].parent =_meta_table['RoutingPolicyShadow.Sets.ExtendedCommunityRt.Sets_.Set']['meta_info']
_meta_table['RoutingPolicyShadow.Sets.ExtendedCommunityRt.Sets_.Set']['meta_info'].parent =_meta_table['RoutingPolicyShadow.Sets.ExtendedCommunityRt.Sets_']['meta_info']
_meta_table['RoutingPolicyShadow.Sets.ExtendedCommunityRt.Sets_']['meta_info'].parent =_meta_table['RoutingPolicyShadow.Sets.ExtendedCommunityRt']['meta_info']
_meta_table['RoutingPolicyShadow.Sets.ExtendedCommunityRt.Unused']['meta_info'].parent =_meta_table['RoutingPolicyShadow.Sets.ExtendedCommunityRt']['meta_info']
_meta_table['RoutingPolicyShadow.Sets.ExtendedCommunityRt.Inactive']['meta_info'].parent =_meta_table['RoutingPolicyShadow.Sets.ExtendedCommunityRt']['meta_info']
_meta_table['RoutingPolicyShadow.Sets.ExtendedCommunityRt.Active']['meta_info'].parent =_meta_table['RoutingPolicyShadow.Sets.ExtendedCommunityRt']['meta_info']
_meta_table['RoutingPolicyShadow.Sets.Rd.Sets_.Set.UsedBy.Reference']['meta_info'].parent =_meta_table['RoutingPolicyShadow.Sets.Rd.Sets_.Set.UsedBy']['meta_info']
_meta_table['RoutingPolicyShadow.Sets.Rd.Sets_.Set.Attached.Binding']['meta_info'].parent =_meta_table['RoutingPolicyShadow.Sets.Rd.Sets_.Set.Attached']['meta_info']
_meta_table['RoutingPolicyShadow.Sets.Rd.Sets_.Set.UsedBy']['meta_info'].parent =_meta_table['RoutingPolicyShadow.Sets.Rd.Sets_.Set']['meta_info']
_meta_table['RoutingPolicyShadow.Sets.Rd.Sets_.Set.Attached']['meta_info'].parent =_meta_table['RoutingPolicyShadow.Sets.Rd.Sets_.Set']['meta_info']
_meta_table['RoutingPolicyShadow.Sets.Rd.Sets_.Set']['meta_info'].parent =_meta_table['RoutingPolicyShadow.Sets.Rd.Sets_']['meta_info']
_meta_table['RoutingPolicyShadow.Sets.Rd.Sets_']['meta_info'].parent =_meta_table['RoutingPolicyShadow.Sets.Rd']['meta_info']
_meta_table['RoutingPolicyShadow.Sets.Rd.Unused']['meta_info'].parent =_meta_table['RoutingPolicyShadow.Sets.Rd']['meta_info']
_meta_table['RoutingPolicyShadow.Sets.Rd.Inactive']['meta_info'].parent =_meta_table['RoutingPolicyShadow.Sets.Rd']['meta_info']
_meta_table['RoutingPolicyShadow.Sets.Rd.Active']['meta_info'].parent =_meta_table['RoutingPolicyShadow.Sets.Rd']['meta_info']
_meta_table['RoutingPolicyShadow.Sets.Mac.Sets_.Set.UsedBy.Reference']['meta_info'].parent =_meta_table['RoutingPolicyShadow.Sets.Mac.Sets_.Set.UsedBy']['meta_info']
_meta_table['RoutingPolicyShadow.Sets.Mac.Sets_.Set.Attached.Binding']['meta_info'].parent =_meta_table['RoutingPolicyShadow.Sets.Mac.Sets_.Set.Attached']['meta_info']
_meta_table['RoutingPolicyShadow.Sets.Mac.Sets_.Set.UsedBy']['meta_info'].parent =_meta_table['RoutingPolicyShadow.Sets.Mac.Sets_.Set']['meta_info']
_meta_table['RoutingPolicyShadow.Sets.Mac.Sets_.Set.Attached']['meta_info'].parent =_meta_table['RoutingPolicyShadow.Sets.Mac.Sets_.Set']['meta_info']
_meta_table['RoutingPolicyShadow.Sets.Mac.Sets_.Set']['meta_info'].parent =_meta_table['RoutingPolicyShadow.Sets.Mac.Sets_']['meta_info']
_meta_table['RoutingPolicyShadow.Sets.Mac.Sets_']['meta_info'].parent =_meta_table['RoutingPolicyShadow.Sets.Mac']['meta_info']
_meta_table['RoutingPolicyShadow.Sets.Mac.Unused']['meta_info'].parent =_meta_table['RoutingPolicyShadow.Sets.Mac']['meta_info']
_meta_table['RoutingPolicyShadow.Sets.Mac.Inactive']['meta_info'].parent =_meta_table['RoutingPolicyShadow.Sets.Mac']['meta_info']
_meta_table['RoutingPolicyShadow.Sets.Mac.Active']['meta_info'].parent =_meta_table['RoutingPolicyShadow.Sets.Mac']['meta_info']
_meta_table['RoutingPolicyShadow.Sets.ExtendedCommunityCost.Sets_.Set.UsedBy.Reference']['meta_info'].parent =_meta_table['RoutingPolicyShadow.Sets.ExtendedCommunityCost.Sets_.Set.UsedBy']['meta_info']
_meta_table['RoutingPolicyShadow.Sets.ExtendedCommunityCost.Sets_.Set.Attached.Binding']['meta_info'].parent =_meta_table['RoutingPolicyShadow.Sets.ExtendedCommunityCost.Sets_.Set.Attached']['meta_info']
_meta_table['RoutingPolicyShadow.Sets.ExtendedCommunityCost.Sets_.Set.UsedBy']['meta_info'].parent =_meta_table['RoutingPolicyShadow.Sets.ExtendedCommunityCost.Sets_.Set']['meta_info']
_meta_table['RoutingPolicyShadow.Sets.ExtendedCommunityCost.Sets_.Set.Attached']['meta_info'].parent =_meta_table['RoutingPolicyShadow.Sets.ExtendedCommunityCost.Sets_.Set']['meta_info']
_meta_table['RoutingPolicyShadow.Sets.ExtendedCommunityCost.Sets_.Set']['meta_info'].parent =_meta_table['RoutingPolicyShadow.Sets.ExtendedCommunityCost.Sets_']['meta_info']
_meta_table['RoutingPolicyShadow.Sets.ExtendedCommunityCost.Sets_']['meta_info'].parent =_meta_table['RoutingPolicyShadow.Sets.ExtendedCommunityCost']['meta_info']
_meta_table['RoutingPolicyShadow.Sets.ExtendedCommunityCost.Unused']['meta_info'].parent =_meta_table['RoutingPolicyShadow.Sets.ExtendedCommunityCost']['meta_info']
_meta_table['RoutingPolicyShadow.Sets.ExtendedCommunityCost.Inactive']['meta_info'].parent =_meta_table['RoutingPolicyShadow.Sets.ExtendedCommunityCost']['meta_info']
_meta_table['RoutingPolicyShadow.Sets.ExtendedCommunityCost.Active']['meta_info'].parent =_meta_table['RoutingPolicyShadow.Sets.ExtendedCommunityCost']['meta_info']
_meta_table['RoutingPolicyShadow.Sets.Etag']['meta_info'].parent =_meta_table['RoutingPolicyShadow.Sets']['meta_info']
_meta_table['RoutingPolicyShadow.Sets.OspfArea']['meta_info'].parent =_meta_table['RoutingPolicyShadow.Sets']['meta_info']
_meta_table['RoutingPolicyShadow.Sets.ExtendedCommunityOpaque']['meta_info'].parent =_meta_table['RoutingPolicyShadow.Sets']['meta_info']
_meta_table['RoutingPolicyShadow.Sets.ExtendedCommunitySegNh']['meta_info'].parent =_meta_table['RoutingPolicyShadow.Sets']['meta_info']
_meta_table['RoutingPolicyShadow.Sets.ExtendedCommunitySoo']['meta_info'].parent =_meta_table['RoutingPolicyShadow.Sets']['meta_info']
_meta_table['RoutingPolicyShadow.Sets.Tag']['meta_info'].parent =_meta_table['RoutingPolicyShadow.Sets']['meta_info']
_meta_table['RoutingPolicyShadow.Sets.Prefix']['meta_info'].parent =_meta_table['RoutingPolicyShadow.Sets']['meta_info']
_meta_table['RoutingPolicyShadow.Sets.Community']['meta_info'].parent =_meta_table['RoutingPolicyShadow.Sets']['meta_info']
_meta_table['RoutingPolicyShadow.Sets.AsPath']['meta_info'].parent =_meta_table['RoutingPolicyShadow.Sets']['meta_info']
_meta_table['RoutingPolicyShadow.Sets.LargeCommunity']['meta_info'].parent =_meta_table['RoutingPolicyShadow.Sets']['meta_info']
_meta_table['RoutingPolicyShadow.Sets.Esi']['meta_info'].parent =_meta_table['RoutingPolicyShadow.Sets']['meta_info']
_meta_table['RoutingPolicyShadow.Sets.ExtendedCommunityBandwidth']['meta_info'].parent =_meta_table['RoutingPolicyShadow.Sets']['meta_info']
_meta_table['RoutingPolicyShadow.Sets.ExtendedCommunityRt']['meta_info'].parent =_meta_table['RoutingPolicyShadow.Sets']['meta_info']
_meta_table['RoutingPolicyShadow.Sets.Rd']['meta_info'].parent =_meta_table['RoutingPolicyShadow.Sets']['meta_info']
_meta_table['RoutingPolicyShadow.Sets.Mac']['meta_info'].parent =_meta_table['RoutingPolicyShadow.Sets']['meta_info']
_meta_table['RoutingPolicyShadow.Sets.ExtendedCommunityCost']['meta_info'].parent =_meta_table['RoutingPolicyShadow.Sets']['meta_info']
_meta_table['RoutingPolicyShadow.Limits']['meta_info'].parent =_meta_table['RoutingPolicyShadow']['meta_info']
_meta_table['RoutingPolicyShadow.Policies']['meta_info'].parent =_meta_table['RoutingPolicyShadow']['meta_info']
_meta_table['RoutingPolicyShadow.Sets']['meta_info'].parent =_meta_table['RoutingPolicyShadow']['meta_info']
