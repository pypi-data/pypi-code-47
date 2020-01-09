
'''
This is auto-generated file,
which includes metadata for module Cisco_IOS_XR_ipv6_acl_cfg
'''

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_LIST, REFERENCE_LEAFLIST, REFERENCE_BITS, REFERENCE_UNION
from ydk._core._dm_meta_info import REFERENCE_CLASS, REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, ANYXML_CLASS
from ydk._core._importer import _yang_ns

_meta_table = {
    'NextHopType' : _MetaInfoEnum('NextHopType',
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_acl_cfg', 'NextHopType',
        '''Next-hop type.''',
        {
            'regular-next-hop':'regular_next_hop',
            'default-next-hop':'default_next_hop',
        }, 'Cisco-IOS-XR-ipv6-acl-cfg', _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-ipv6-acl-cfg']),
    'Ipv6AclAndPrefixList.Prefixes.Prefix.PrefixListEntries.PrefixListEntry' : {
        'meta_info' : _MetaInfoClass('Ipv6AclAndPrefixList.Prefixes.Prefix.PrefixListEntries.PrefixListEntry', REFERENCE_LIST,
            '''A prefix list entry; either a description
(remark) or a prefix to match against''',
            False, 
            [
            _MetaInfoClassMember('sequence-number', ATTRIBUTE, 'int', 'dt1:Acl-sequence-number-range',
                None, None,
                [('1', '2147483646')], [],
                '''                Sequence number of prefix list
                ''',
                'sequence_number',
                'Cisco-IOS-XR-ipv6-acl-cfg', True),
            _MetaInfoClassMember('grant', REFERENCE_ENUM_CLASS, 'Ipv6AclGrantEnum', 'dt2:Ipv6-acl-grant-enum',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_acl_datatypes', 'Ipv6AclGrantEnum',
                [], [],
                '''                Whether to forward or drop packets matching
                the prefix list
                ''',
                'grant',
                'Cisco-IOS-XR-ipv6-acl-cfg', False),
            _MetaInfoClassMember('ipv6-address-as-string', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                The IPv6 address if entered  with the
                ZoneMutually exclusive with Prefix and
                PrefixMask
                ''',
                'ipv6_address_as_string',
                'Cisco-IOS-XR-ipv6-acl-cfg', False),
            _MetaInfoClassMember('zone', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                IPv6 Zone if entered  with the
                IPV6AddressMutually exclusive with Prefix
                and PrefixMask
                ''',
                'zone',
                'Cisco-IOS-XR-ipv6-acl-cfg', False),
            _MetaInfoClassMember('prefix', ATTRIBUTE, 'str', 'inet:ipv6-address-no-zone',
                None, None,
                [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'],
                '''                IPv6 address prefix to match
                ''',
                'prefix',
                'Cisco-IOS-XR-ipv6-acl-cfg', False),
            _MetaInfoClassMember('prefix-mask', ATTRIBUTE, 'int', 'xr:Ipv6-prefix-length',
                None, None,
                [('0', '128')], [],
                '''                MaskLength of IPv6 address prefix
                ''',
                'prefix_mask',
                'Cisco-IOS-XR-ipv6-acl-cfg', False),
            _MetaInfoClassMember('match-exact-length', REFERENCE_ENUM_CLASS, 'Ipv6PrefixMatchExactLength', 'dt2:Ipv6-prefix-match-exact-length',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_acl_datatypes', 'Ipv6PrefixMatchExactLength',
                [], [],
                '''                Set to perform an exact prefix length match.
                Item is mutually exclusive with minimum and
                maximum length match items
                ''',
                'match_exact_length',
                'Cisco-IOS-XR-ipv6-acl-cfg', False),
            _MetaInfoClassMember('exact-prefix-length', ATTRIBUTE, 'int', 'xr:Ipv6-prefix-length',
                None, None,
                [('0', '128')], [],
                '''                If exact prefix length matching specified,
                set the length of prefix to be matched
                ''',
                'exact_prefix_length',
                'Cisco-IOS-XR-ipv6-acl-cfg', False),
            _MetaInfoClassMember('match-max-length', REFERENCE_ENUM_CLASS, 'Ipv6PrefixMatchMaxLength', 'dt2:Ipv6-prefix-match-max-length',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_acl_datatypes', 'Ipv6PrefixMatchMaxLength',
                [], [],
                '''                Set to perform a maximum length prefix match
                .  Item is mutually exclusive with exact
                length match item
                ''',
                'match_max_length',
                'Cisco-IOS-XR-ipv6-acl-cfg', False),
            _MetaInfoClassMember('max-prefix-length', ATTRIBUTE, 'int', 'xr:Ipv6-prefix-length',
                None, None,
                [('0', '128')], [],
                '''                If maximum length prefix matching specified,
                set the maximum length of prefix to be
                matched
                ''',
                'max_prefix_length',
                'Cisco-IOS-XR-ipv6-acl-cfg', False),
            _MetaInfoClassMember('match-min-length', REFERENCE_ENUM_CLASS, 'Ipv6PrefixMatchMinLength', 'dt2:Ipv6-prefix-match-min-length',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_acl_datatypes', 'Ipv6PrefixMatchMinLength',
                [], [],
                '''                Set to perform a minimum length prefix match
                .  Item is mutually exclusive with exact
                length match item
                ''',
                'match_min_length',
                'Cisco-IOS-XR-ipv6-acl-cfg', False),
            _MetaInfoClassMember('min-prefix-length', ATTRIBUTE, 'int', 'xr:Ipv6-prefix-length',
                None, None,
                [('0', '128')], [],
                '''                If minimum length prefix matching specified,
                set the minimum length of prefix to be
                matched
                ''',
                'min_prefix_length',
                'Cisco-IOS-XR-ipv6-acl-cfg', False),
            _MetaInfoClassMember('remark', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                Comments or a description for the prefix
                list.  Item is mutually exclusive with all
                others in the object
                ''',
                'remark',
                'Cisco-IOS-XR-ipv6-acl-cfg', False),
            ],
            'Cisco-IOS-XR-ipv6-acl-cfg',
            'prefix-list-entry',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-ipv6-acl-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_acl_cfg',
        ),
    },
    'Ipv6AclAndPrefixList.Prefixes.Prefix.PrefixListEntries' : {
        'meta_info' : _MetaInfoClass('Ipv6AclAndPrefixList.Prefixes.Prefix.PrefixListEntries', REFERENCE_CLASS,
            '''Sequence of entries forming a prefix list''',
            False, 
            [
            _MetaInfoClassMember('prefix-list-entry', REFERENCE_LIST, 'PrefixListEntry', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_acl_cfg', 'Ipv6AclAndPrefixList.Prefixes.Prefix.PrefixListEntries.PrefixListEntry',
                [], [],
                '''                A prefix list entry; either a description
                (remark) or a prefix to match against
                ''',
                'prefix_list_entry',
                'Cisco-IOS-XR-ipv6-acl-cfg', False),
            ],
            'Cisco-IOS-XR-ipv6-acl-cfg',
            'prefix-list-entries',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-ipv6-acl-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_acl_cfg',
        ),
    },
    'Ipv6AclAndPrefixList.Prefixes.Prefix' : {
        'meta_info' : _MetaInfoClass('Ipv6AclAndPrefixList.Prefixes.Prefix', REFERENCE_LIST,
            '''Name of a prefix list''',
            False, 
            [
            _MetaInfoClassMember('name', ATTRIBUTE, 'str', 'dt2:Ipv6-acl-prefix-list-name',
                None, None,
                [(1, 64)], [],
                '''                Name of a prefix list
                ''',
                'name',
                'Cisco-IOS-XR-ipv6-acl-cfg', True),
            _MetaInfoClassMember('prefix-list-entries', REFERENCE_CLASS, 'PrefixListEntries', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_acl_cfg', 'Ipv6AclAndPrefixList.Prefixes.Prefix.PrefixListEntries',
                [], [],
                '''                Sequence of entries forming a prefix list
                ''',
                'prefix_list_entries',
                'Cisco-IOS-XR-ipv6-acl-cfg', False),
            ],
            'Cisco-IOS-XR-ipv6-acl-cfg',
            'prefix',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-ipv6-acl-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_acl_cfg',
        ),
    },
    'Ipv6AclAndPrefixList.Prefixes' : {
        'meta_info' : _MetaInfoClass('Ipv6AclAndPrefixList.Prefixes', REFERENCE_CLASS,
            '''Table of prefix lists''',
            False, 
            [
            _MetaInfoClassMember('prefix', REFERENCE_LIST, 'Prefix', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_acl_cfg', 'Ipv6AclAndPrefixList.Prefixes.Prefix',
                [], [],
                '''                Name of a prefix list
                ''',
                'prefix',
                'Cisco-IOS-XR-ipv6-acl-cfg', False),
            ],
            'Cisco-IOS-XR-ipv6-acl-cfg',
            'prefixes',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-ipv6-acl-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_acl_cfg',
        ),
    },
    'Ipv6AclAndPrefixList.LogUpdate' : {
        'meta_info' : _MetaInfoClass('Ipv6AclAndPrefixList.LogUpdate', REFERENCE_CLASS,
            '''Control access lists log updates''',
            False, 
            [
            _MetaInfoClassMember('threshold', ATTRIBUTE, 'int', 'dt2:Ipv6-acl-log-threshold-range',
                None, None,
                [('1', '2147483647')], [],
                '''                Log update threshold (number of hits)
                ''',
                'threshold',
                'Cisco-IOS-XR-ipv6-acl-cfg', False),
            _MetaInfoClassMember('rate', ATTRIBUTE, 'int', 'dt2:Ipv6-acl-log-rate-range',
                None, None,
                [('1', '1000')], [],
                '''                Log update rate (log messages per second)
                ''',
                'rate',
                'Cisco-IOS-XR-ipv6-acl-cfg', False),
            ],
            'Cisco-IOS-XR-ipv6-acl-cfg',
            'log-update',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-ipv6-acl-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_acl_cfg',
        ),
    },
    'Ipv6AclAndPrefixList.Accesses.Access.AccessListEntries.AccessListEntry.SourceNetwork' : {
        'meta_info' : _MetaInfoClass('Ipv6AclAndPrefixList.Accesses.Access.AccessListEntries.AccessListEntry.SourceNetwork', REFERENCE_CLASS,
            '''Source network settings.''',
            False, 
            [
            _MetaInfoClassMember('source-address', ATTRIBUTE, 'str', 'inet:ipv6-address',
                None, None,
                [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'],
                '''                Source IPv6 address, leave unspecified
                if inputting as IPv6 address with wildcarding.
                ''',
                'source_address',
                'Cisco-IOS-XR-ipv6-acl-cfg', False),
            _MetaInfoClassMember('source-wild-card-bits', ATTRIBUTE, 'int', 'xr:Ipv6-prefix-length',
                None, None,
                [('0', '128')], [],
                '''                Wildcard bits to apply to source-address
                (if specified), leave unspecified for no
                wildcarding.
                ''',
                'source_wild_card_bits',
                'Cisco-IOS-XR-ipv6-acl-cfg', False),
            _MetaInfoClassMember('source-mask', ATTRIBUTE, 'str', 'inet:ipv6-address-no-zone',
                None, None,
                [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'],
                '''                Source address mask. Either
                source-wild-card-bits or source-mask is.
                supported, not both. Leave unspecified.
                for any.
                ''',
                'source_mask',
                'Cisco-IOS-XR-ipv6-acl-cfg', False),
            ],
            'Cisco-IOS-XR-ipv6-acl-cfg',
            'source-network',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-ipv6-acl-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_acl_cfg',
        ),
    },
    'Ipv6AclAndPrefixList.Accesses.Access.AccessListEntries.AccessListEntry.DestinationNetwork' : {
        'meta_info' : _MetaInfoClass('Ipv6AclAndPrefixList.Accesses.Access.AccessListEntries.AccessListEntry.DestinationNetwork', REFERENCE_CLASS,
            '''Destination network settings.''',
            False, 
            [
            _MetaInfoClassMember('destination-address', ATTRIBUTE, 'str', 'inet:ipv6-address',
                None, None,
                [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'],
                '''                Destination IPv6 address, leave unspecified
                if inputting as IPv6 address with
                wildcarding.
                ''',
                'destination_address',
                'Cisco-IOS-XR-ipv6-acl-cfg', False),
            _MetaInfoClassMember('destination-wild-card-bits', ATTRIBUTE, 'int', 'xr:Ipv6-prefix-length',
                None, None,
                [('0', '128')], [],
                '''                Wildcard bits to apply to destination
                destination-address (if specified),
                leave unspecified for no wildcarding.
                ''',
                'destination_wild_card_bits',
                'Cisco-IOS-XR-ipv6-acl-cfg', False),
            _MetaInfoClassMember('destination-mask', ATTRIBUTE, 'str', 'inet:ipv6-address-no-zone',
                None, None,
                [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'],
                '''                Destination address mask. Either
                destination-wild-card-bits or destination-mask.
                is supported, not both. Leave unspecified
                for any.
                ''',
                'destination_mask',
                'Cisco-IOS-XR-ipv6-acl-cfg', False),
            ],
            'Cisco-IOS-XR-ipv6-acl-cfg',
            'destination-network',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-ipv6-acl-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_acl_cfg',
        ),
    },
    'Ipv6AclAndPrefixList.Accesses.Access.AccessListEntries.AccessListEntry.SourcePort' : {
        'meta_info' : _MetaInfoClass('Ipv6AclAndPrefixList.Accesses.Access.AccessListEntries.AccessListEntry.SourcePort', REFERENCE_CLASS,
            '''Source port settings.''',
            False, 
            [
            _MetaInfoClassMember('source-operator', REFERENCE_ENUM_CLASS, 'Ipv6AclOperatorEnum', 'ipv6-acl-dt:Ipv6-acl-operator-enum',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_acl_datatypes', 'Ipv6AclOperatorEnum',
                [], [],
                '''                Source port comparison operator. This is a required
                field if any source port value is given, otherwise,
                config will be rejected. Leave unspecified
                if no source port comparison is to be done.
                ''',
                'source_operator',
                'Cisco-IOS-XR-ipv6-acl-cfg', False),
            _MetaInfoClassMember('first-source-port', REFERENCE_UNION, 'str', 'ipv6-acl-dt:Ipv6-acl-port-number',
                None, None,
                [], [],
                '''                Lower source port for comparison. It can be used
                for the lower bound (range operator) or single value
                (equal, less, greater..etc). Any value not in the
                permissible range will be rejected. Leave unspecified
                otherwise.
                ''',
                'first_source_port',
                'Cisco-IOS-XR-ipv6-acl-cfg', False, [
                    _MetaInfoClassMember('first-source-port', REFERENCE_ENUM_CLASS, 'Ipv6AclPortNumber', 'enumeration',
                        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_acl_datatypes', 'Ipv6AclPortNumber',
                        [], [],
                        '''                        Lower source port for comparison. It can be used
                        for the lower bound (range operator) or single value
                        (equal, less, greater..etc). Any value not in the
                        permissible range will be rejected. Leave unspecified
                        otherwise.
                        ''',
                        'first_source_port',
                        'Cisco-IOS-XR-ipv6-acl-cfg', False),
                    _MetaInfoClassMember('first-source-port', ATTRIBUTE, 'int', 'uint32',
                        None, None,
                        [('0', '65535')], [],
                        '''                        Lower source port for comparison. It can be used
                        for the lower bound (range operator) or single value
                        (equal, less, greater..etc). Any value not in the
                        permissible range will be rejected. Leave unspecified
                        otherwise.
                        ''',
                        'first_source_port',
                        'Cisco-IOS-XR-ipv6-acl-cfg', False),
                ]),
            _MetaInfoClassMember('second-source-port', REFERENCE_UNION, 'str', 'ipv6-acl-dt:Ipv6-acl-port-number',
                None, None,
                [], [],
                '''                Upper source port for comparion. It is used
                in the upper bound (range operator). Any value not in the
                permissible range will be rejected. Leave unspecified
                otherwise.
                ''',
                'second_source_port',
                'Cisco-IOS-XR-ipv6-acl-cfg', False, [
                    _MetaInfoClassMember('second-source-port', REFERENCE_ENUM_CLASS, 'Ipv6AclPortNumber', 'enumeration',
                        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_acl_datatypes', 'Ipv6AclPortNumber',
                        [], [],
                        '''                        Upper source port for comparion. It is used
                        in the upper bound (range operator). Any value not in the
                        permissible range will be rejected. Leave unspecified
                        otherwise.
                        ''',
                        'second_source_port',
                        'Cisco-IOS-XR-ipv6-acl-cfg', False),
                    _MetaInfoClassMember('second-source-port', ATTRIBUTE, 'int', 'uint32',
                        None, None,
                        [('0', '65535')], [],
                        '''                        Upper source port for comparion. It is used
                        in the upper bound (range operator). Any value not in the
                        permissible range will be rejected. Leave unspecified
                        otherwise.
                        ''',
                        'second_source_port',
                        'Cisco-IOS-XR-ipv6-acl-cfg', False),
                ]),
            ],
            'Cisco-IOS-XR-ipv6-acl-cfg',
            'source-port',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-ipv6-acl-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_acl_cfg',
            has_when=True,
        ),
    },
    'Ipv6AclAndPrefixList.Accesses.Access.AccessListEntries.AccessListEntry.DestinationPort' : {
        'meta_info' : _MetaInfoClass('Ipv6AclAndPrefixList.Accesses.Access.AccessListEntries.AccessListEntry.DestinationPort', REFERENCE_CLASS,
            '''Destination port settings.''',
            False, 
            [
            _MetaInfoClassMember('destination-operator', REFERENCE_ENUM_CLASS, 'Ipv6AclOperatorEnum', 'ipv6-acl-dt:Ipv6-acl-operator-enum',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_acl_datatypes', 'Ipv6AclOperatorEnum',
                [], [],
                '''                Destination port comparison operator. This is a
                required field if any destination port value is
                given, otherwise, config will be rejected.
                Leave unspecified if no destination
                port comparison is to be done.
                ''',
                'destination_operator',
                'Cisco-IOS-XR-ipv6-acl-cfg', False),
            _MetaInfoClassMember('first-destination-port', REFERENCE_UNION, 'str', 'ipv6-acl-dt:Ipv6-acl-port-number',
                None, None,
                [], [],
                '''                Lower destination port for comparison. It can be used
                for the lower bound (range operator) or single value
                (equal, less, greater..etc). Any value not in the
                permissible range will be rejected. Leave unspecified
                otherwise.
                ''',
                'first_destination_port',
                'Cisco-IOS-XR-ipv6-acl-cfg', False, [
                    _MetaInfoClassMember('first-destination-port', REFERENCE_ENUM_CLASS, 'Ipv6AclPortNumber', 'enumeration',
                        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_acl_datatypes', 'Ipv6AclPortNumber',
                        [], [],
                        '''                        Lower destination port for comparison. It can be used
                        for the lower bound (range operator) or single value
                        (equal, less, greater..etc). Any value not in the
                        permissible range will be rejected. Leave unspecified
                        otherwise.
                        ''',
                        'first_destination_port',
                        'Cisco-IOS-XR-ipv6-acl-cfg', False),
                    _MetaInfoClassMember('first-destination-port', ATTRIBUTE, 'int', 'uint32',
                        None, None,
                        [('0', '65535')], [],
                        '''                        Lower destination port for comparison. It can be used
                        for the lower bound (range operator) or single value
                        (equal, less, greater..etc). Any value not in the
                        permissible range will be rejected. Leave unspecified
                        otherwise.
                        ''',
                        'first_destination_port',
                        'Cisco-IOS-XR-ipv6-acl-cfg', False),
                ]),
            _MetaInfoClassMember('second-destination-port', REFERENCE_UNION, 'str', 'ipv6-acl-dt:Ipv6-acl-port-number',
                None, None,
                [], [],
                '''                Upper destination port for comparison. It is used
                in the upper bound (range operator). Any value not in the
                permissible range will be rejected. Leave unspecified
                otherwise.
                ''',
                'second_destination_port',
                'Cisco-IOS-XR-ipv6-acl-cfg', False, [
                    _MetaInfoClassMember('second-destination-port', REFERENCE_ENUM_CLASS, 'Ipv6AclPortNumber', 'enumeration',
                        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_acl_datatypes', 'Ipv6AclPortNumber',
                        [], [],
                        '''                        Upper destination port for comparison. It is used
                        in the upper bound (range operator). Any value not in the
                        permissible range will be rejected. Leave unspecified
                        otherwise.
                        ''',
                        'second_destination_port',
                        'Cisco-IOS-XR-ipv6-acl-cfg', False),
                    _MetaInfoClassMember('second-destination-port', ATTRIBUTE, 'int', 'uint32',
                        None, None,
                        [('0', '65535')], [],
                        '''                        Upper destination port for comparison. It is used
                        in the upper bound (range operator). Any value not in the
                        permissible range will be rejected. Leave unspecified
                        otherwise.
                        ''',
                        'second_destination_port',
                        'Cisco-IOS-XR-ipv6-acl-cfg', False),
                ]),
            ],
            'Cisco-IOS-XR-ipv6-acl-cfg',
            'destination-port',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-ipv6-acl-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_acl_cfg',
            has_when=True,
        ),
    },
    'Ipv6AclAndPrefixList.Accesses.Access.AccessListEntries.AccessListEntry.Icmp' : {
        'meta_info' : _MetaInfoClass('Ipv6AclAndPrefixList.Accesses.Access.AccessListEntries.AccessListEntry.Icmp', REFERENCE_CLASS,
            '''ICMP settings.''',
            False, 
            [
            _MetaInfoClassMember('icmp-type-code', REFERENCE_ENUM_CLASS, 'Ipv6AclIcmpTypeCodeEnum', 'ipv6-acl-dt:Ipv6-acl-icmp-type-code-enum',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_acl_datatypes', 'Ipv6AclIcmpTypeCodeEnum',
                [], [],
                '''                Well known ICMP message code types to match,
                leave unspecified if ICMP message code type
                comparion is not to be performed.
                ''',
                'icmp_type_code',
                'Cisco-IOS-XR-ipv6-acl-cfg', False),
            ],
            'Cisco-IOS-XR-ipv6-acl-cfg',
            'icmp',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-ipv6-acl-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_acl_cfg',
            has_when=True,
        ),
    },
    'Ipv6AclAndPrefixList.Accesses.Access.AccessListEntries.AccessListEntry.Tcp' : {
        'meta_info' : _MetaInfoClass('Ipv6AclAndPrefixList.Accesses.Access.AccessListEntries.AccessListEntry.Tcp', REFERENCE_CLASS,
            '''TCP settings.''',
            False, 
            [
            _MetaInfoClassMember('tcp-bits-match-operator', REFERENCE_ENUM_CLASS, 'Ipv6AclTcpMatchOperatorEnum', 'ipv6-acl-dt:Ipv6-acl-tcp-match-operator-enum',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_acl_datatypes', 'Ipv6AclTcpMatchOperatorEnum',
                [], [],
                '''                TCP Bits match operator. Leave unspecified if
                flexible comparison of TCP bits is not
                required.
                ''',
                'tcp_bits_match_operator',
                'Cisco-IOS-XR-ipv6-acl-cfg', False),
            _MetaInfoClassMember('tcp-bits', REFERENCE_BITS, 'Ipv6AclTcpBitsNumber', 'ipv6-acl-dt:Ipv6-acl-tcp-bits-number',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_acl_datatypes', 'Ipv6AclTcpBitsNumber',
                [], [],
                '''                TCP bits to match. Leave unspecified if
                comparison of TCP bits is not required.
                ''',
                'tcp_bits',
                'Cisco-IOS-XR-ipv6-acl-cfg', False),
            _MetaInfoClassMember('tcp-bits-mask', REFERENCE_BITS, 'Ipv6AclTcpBitsNumber', 'ipv6-acl-dt:Ipv6-acl-tcp-bits-number',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_acl_datatypes', 'Ipv6AclTcpBitsNumber',
                [], [],
                '''                TCP bits mask to use for flexible TCP matching.
                Leave unspecified if it is not required.
                ''',
                'tcp_bits_mask',
                'Cisco-IOS-XR-ipv6-acl-cfg', False),
            ],
            'Cisco-IOS-XR-ipv6-acl-cfg',
            'tcp',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-ipv6-acl-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_acl_cfg',
            has_when=True,
        ),
    },
    'Ipv6AclAndPrefixList.Accesses.Access.AccessListEntries.AccessListEntry.PacketLength' : {
        'meta_info' : _MetaInfoClass('Ipv6AclAndPrefixList.Accesses.Access.AccessListEntries.AccessListEntry.PacketLength', REFERENCE_CLASS,
            '''Packet length settings.''',
            False, 
            [
            _MetaInfoClassMember('packet-length-operator', REFERENCE_ENUM_CLASS, 'Ipv6AclOperatorEnum', 'ipv6-acl-dt:Ipv6-acl-operator-enum',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_acl_datatypes', 'Ipv6AclOperatorEnum',
                [], [],
                '''                Packet length operator applicable if packet length
                is to be compared. This is a required field if any
                packet-length value is given, otherwise, config
                will be rejected.
                ''',
                'packet_length_operator',
                'Cisco-IOS-XR-ipv6-acl-cfg', False),
            _MetaInfoClassMember('packet-length-min', ATTRIBUTE, 'int', 'ipv6-acl-dt:Ipv6-acl-plen-range',
                None, None,
                [('0', '65535')], [],
                '''                Mininum packet length value for comparison. It can be used
                for the lower bound (range operator) or single value
                (equal, less, greater..etc). Any value not in the permissible
                range will be rejected. Leave unspecified otherwise.
                ''',
                'packet_length_min',
                'Cisco-IOS-XR-ipv6-acl-cfg', False),
            _MetaInfoClassMember('packet-length-max', ATTRIBUTE, 'int', 'ipv6-acl-dt:Ipv6-acl-plen-range',
                None, None,
                [('0', '65535')], [],
                '''                Maximum packet length value for comparison. It is used
                in the upper bound (range operator). Any value not in the
                permissible range will be rejected. Leave unspecified
                otherwise.
                ''',
                'packet_length_max',
                'Cisco-IOS-XR-ipv6-acl-cfg', False),
            ],
            'Cisco-IOS-XR-ipv6-acl-cfg',
            'packet-length',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-ipv6-acl-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_acl_cfg',
        ),
    },
    'Ipv6AclAndPrefixList.Accesses.Access.AccessListEntries.AccessListEntry.TimeToLive' : {
        'meta_info' : _MetaInfoClass('Ipv6AclAndPrefixList.Accesses.Access.AccessListEntries.AccessListEntry.TimeToLive', REFERENCE_CLASS,
            '''TTL settings.''',
            False, 
            [
            _MetaInfoClassMember('time-to-live-operator', REFERENCE_ENUM_CLASS, 'Ipv6AclOperatorEnum', 'ipv6-acl-dt:Ipv6-acl-operator-enum',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_acl_datatypes', 'Ipv6AclOperatorEnum',
                [], [],
                '''                TTL operator is applicable if TTL is to be compared.
                This is a required field if any TTL value is given,
                otherwise, config will be rejected. Leave
                unspecified if TTL classification is not required.
                ''',
                'time_to_live_operator',
                'Cisco-IOS-XR-ipv6-acl-cfg', False),
            _MetaInfoClassMember('time-to-live-min', ATTRIBUTE, 'int', 'ipv6-acl-dt:Ipv6-acl-ttl-range',
                None, None,
                [('0', '255')], [],
                '''                Mininum TTL value for comparison. It can be used for the
                lower bound (range operator) or single value (equal, less,
                greater..etc). Any value not in the permissible range will
                be rejected. Leave unspecified otherwise.
                ''',
                'time_to_live_min',
                'Cisco-IOS-XR-ipv6-acl-cfg', False),
            _MetaInfoClassMember('time-to-live-max', ATTRIBUTE, 'int', 'ipv6-acl-dt:Ipv6-acl-ttl-range',
                None, None,
                [('0', '255')], [],
                '''                Maximum TTL value for comparison. It is used in the
                upper bound (range operator). Any value not in the
                permissible range will be rejected. Leave unspecified
                otherwise.
                ''',
                'time_to_live_max',
                'Cisco-IOS-XR-ipv6-acl-cfg', False),
            ],
            'Cisco-IOS-XR-ipv6-acl-cfg',
            'time-to-live',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-ipv6-acl-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_acl_cfg',
        ),
    },
    'Ipv6AclAndPrefixList.Accesses.Access.AccessListEntries.AccessListEntry.DSCPValues' : {
        'meta_info' : _MetaInfoClass('Ipv6AclAndPrefixList.Accesses.Access.AccessListEntries.AccessListEntry.DSCPValues', REFERENCE_CLASS,
            '''DSCP settings.''',
            False, 
            [
            _MetaInfoClassMember('dscp-operator', REFERENCE_ENUM_CLASS, 'Ipv6AclOperatorEnum', 'ipv6-acl-dt:Ipv6-acl-operator-enum',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_acl_datatypes', 'Ipv6AclOperatorEnum',
                [], [],
                '''                Enumerated DSCP operator values. Used when
                operator needs to be configured. Leave unspecified
                if DSCP operator is not required. Note: if the
                dscp operator is not set, it logically behaves
                same as equal operator.
                ''',
                'dscp_operator',
                'Cisco-IOS-XR-ipv6-acl-cfg', False),
            _MetaInfoClassMember('dscp-lower', REFERENCE_UNION, 'str', 'ipv6-acl-dt:Ipv6-acl-dscp-number',
                None, None,
                [], [],
                '''                DSCP value to match (if a value was specified).
                It can be used for the lower bound (range operator) or
                single value (equal, less, greater..etc) or without
                any operator. Any value not in the permissible range
                will be rejected. Leave unspecified if DSCP
                comparison is not to be performed.
                ''',
                'dscp_lower',
                'Cisco-IOS-XR-ipv6-acl-cfg', False, [
                    _MetaInfoClassMember('dscp-lower', REFERENCE_ENUM_CLASS, 'Ipv6AclDscpNumber', 'enumeration',
                        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_acl_datatypes', 'Ipv6AclDscpNumber',
                        [], [],
                        '''                        DSCP value to match (if a value was specified).
                        It can be used for the lower bound (range operator) or
                        single value (equal, less, greater..etc) or without
                        any operator. Any value not in the permissible range
                        will be rejected. Leave unspecified if DSCP
                        comparison is not to be performed.
                        ''',
                        'dscp_lower',
                        'Cisco-IOS-XR-ipv6-acl-cfg', False),
                    _MetaInfoClassMember('dscp-lower', ATTRIBUTE, 'int', 'uint32',
                        None, None,
                        [('0', '63')], [],
                        '''                        DSCP value to match (if a value was specified).
                        It can be used for the lower bound (range operator) or
                        single value (equal, less, greater..etc) or without
                        any operator. Any value not in the permissible range
                        will be rejected. Leave unspecified if DSCP
                        comparison is not to be performed.
                        ''',
                        'dscp_lower',
                        'Cisco-IOS-XR-ipv6-acl-cfg', False),
                ]),
            _MetaInfoClassMember('dscp-upper', REFERENCE_UNION, 'str', 'ipv6-acl-dt:Ipv6-acl-dscp-number',
                None, None,
                [], [],
                '''                DSCP value to match (if a value was specified).
                It can be used in the upper bound (range operator)
                Any value not in the permissible range will be rejected.
                Leave unspecified if DSCP range comparison is not to be
                performed.
                ''',
                'dscp_upper',
                'Cisco-IOS-XR-ipv6-acl-cfg', False, [
                    _MetaInfoClassMember('dscp-upper', REFERENCE_ENUM_CLASS, 'Ipv6AclDscpNumber', 'enumeration',
                        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_acl_datatypes', 'Ipv6AclDscpNumber',
                        [], [],
                        '''                        DSCP value to match (if a value was specified).
                        It can be used in the upper bound (range operator)
                        Any value not in the permissible range will be rejected.
                        Leave unspecified if DSCP range comparison is not to be
                        performed.
                        ''',
                        'dscp_upper',
                        'Cisco-IOS-XR-ipv6-acl-cfg', False),
                    _MetaInfoClassMember('dscp-upper', ATTRIBUTE, 'int', 'uint32',
                        None, None,
                        [('0', '63')], [],
                        '''                        DSCP value to match (if a value was specified).
                        It can be used in the upper bound (range operator)
                        Any value not in the permissible range will be rejected.
                        Leave unspecified if DSCP range comparison is not to be
                        performed.
                        ''',
                        'dscp_upper',
                        'Cisco-IOS-XR-ipv6-acl-cfg', False),
                ]),
            ],
            'Cisco-IOS-XR-ipv6-acl-cfg',
            'DSCPValues',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-ipv6-acl-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_acl_cfg',
        ),
    },
    'Ipv6AclAndPrefixList.Accesses.Access.AccessListEntries.AccessListEntry.NextHop.NextHop1' : {
        'meta_info' : _MetaInfoClass('Ipv6AclAndPrefixList.Accesses.Access.AccessListEntries.AccessListEntry.NextHop.NextHop1', REFERENCE_CLASS,
            '''The first next-hop settings.''',
            False, 
            [
            _MetaInfoClassMember('next-hop', ATTRIBUTE, 'str', 'inet:ipv6-address-no-zone',
                None, None,
                [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'],
                '''                The IPv6 address of the next-hop.
                ''',
                'next_hop',
                'Cisco-IOS-XR-ipv6-acl-cfg', False),
            _MetaInfoClassMember('vrf-name', ATTRIBUTE, 'str', 'string',
                None, None,
                [(1, 32)], [],
                '''                The VRF name of the next-hop.
                ''',
                'vrf_name',
                'Cisco-IOS-XR-ipv6-acl-cfg', False),
            _MetaInfoClassMember('track-name', ATTRIBUTE, 'str', 'string',
                None, None,
                [(1, 32)], [],
                '''                The object tracking name for the next-hop.
                ''',
                'track_name',
                'Cisco-IOS-XR-ipv6-acl-cfg', False),
            ],
            'Cisco-IOS-XR-ipv6-acl-cfg',
            'next-hop-1',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-ipv6-acl-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_acl_cfg',
        ),
    },
    'Ipv6AclAndPrefixList.Accesses.Access.AccessListEntries.AccessListEntry.NextHop.NextHop2' : {
        'meta_info' : _MetaInfoClass('Ipv6AclAndPrefixList.Accesses.Access.AccessListEntries.AccessListEntry.NextHop.NextHop2', REFERENCE_CLASS,
            '''The second next-hop settings.''',
            False, 
            [
            _MetaInfoClassMember('next-hop', ATTRIBUTE, 'str', 'inet:ipv6-address-no-zone',
                None, None,
                [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'],
                '''                The IPv6 address of the next-hop.
                ''',
                'next_hop',
                'Cisco-IOS-XR-ipv6-acl-cfg', False),
            _MetaInfoClassMember('vrf-name', ATTRIBUTE, 'str', 'string',
                None, None,
                [(1, 32)], [],
                '''                The VRF name of the next-hop.
                ''',
                'vrf_name',
                'Cisco-IOS-XR-ipv6-acl-cfg', False),
            _MetaInfoClassMember('track-name', ATTRIBUTE, 'str', 'string',
                None, None,
                [(1, 32)], [],
                '''                The object tracking name for the next-hop.
                ''',
                'track_name',
                'Cisco-IOS-XR-ipv6-acl-cfg', False),
            ],
            'Cisco-IOS-XR-ipv6-acl-cfg',
            'next-hop-2',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-ipv6-acl-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_acl_cfg',
        ),
    },
    'Ipv6AclAndPrefixList.Accesses.Access.AccessListEntries.AccessListEntry.NextHop.NextHop3' : {
        'meta_info' : _MetaInfoClass('Ipv6AclAndPrefixList.Accesses.Access.AccessListEntries.AccessListEntry.NextHop.NextHop3', REFERENCE_CLASS,
            '''The third next-hop settings.''',
            False, 
            [
            _MetaInfoClassMember('next-hop', ATTRIBUTE, 'str', 'inet:ipv6-address-no-zone',
                None, None,
                [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'],
                '''                The IPv6 address of the next-hop.
                ''',
                'next_hop',
                'Cisco-IOS-XR-ipv6-acl-cfg', False),
            _MetaInfoClassMember('vrf-name', ATTRIBUTE, 'str', 'string',
                None, None,
                [(1, 32)], [],
                '''                The VRF name of the next-hop.
                ''',
                'vrf_name',
                'Cisco-IOS-XR-ipv6-acl-cfg', False),
            _MetaInfoClassMember('track-name', ATTRIBUTE, 'str', 'string',
                None, None,
                [(1, 32)], [],
                '''                The object tracking name for the next-hop.
                ''',
                'track_name',
                'Cisco-IOS-XR-ipv6-acl-cfg', False),
            ],
            'Cisco-IOS-XR-ipv6-acl-cfg',
            'next-hop-3',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-ipv6-acl-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_acl_cfg',
        ),
    },
    'Ipv6AclAndPrefixList.Accesses.Access.AccessListEntries.AccessListEntry.NextHop' : {
        'meta_info' : _MetaInfoClass('Ipv6AclAndPrefixList.Accesses.Access.AccessListEntries.AccessListEntry.NextHop', REFERENCE_CLASS,
            '''Next-hop settings.''',
            False, 
            [
            _MetaInfoClassMember('next-hop-type', REFERENCE_ENUM_CLASS, 'NextHopType', 'Next-hop-type',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_acl_cfg', 'NextHopType',
                [], [],
                '''                The nexthop type.
                ''',
                'next_hop_type',
                'Cisco-IOS-XR-ipv6-acl-cfg', False),
            _MetaInfoClassMember('next-hop-1', REFERENCE_CLASS, 'NextHop1', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_acl_cfg', 'Ipv6AclAndPrefixList.Accesses.Access.AccessListEntries.AccessListEntry.NextHop.NextHop1',
                [], [],
                '''                The first next-hop settings.
                ''',
                'next_hop_1',
                'Cisco-IOS-XR-ipv6-acl-cfg', False),
            _MetaInfoClassMember('next-hop-2', REFERENCE_CLASS, 'NextHop2', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_acl_cfg', 'Ipv6AclAndPrefixList.Accesses.Access.AccessListEntries.AccessListEntry.NextHop.NextHop2',
                [], [],
                '''                The second next-hop settings.
                ''',
                'next_hop_2',
                'Cisco-IOS-XR-ipv6-acl-cfg', False),
            _MetaInfoClassMember('next-hop-3', REFERENCE_CLASS, 'NextHop3', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_acl_cfg', 'Ipv6AclAndPrefixList.Accesses.Access.AccessListEntries.AccessListEntry.NextHop.NextHop3',
                [], [],
                '''                The third next-hop settings.
                ''',
                'next_hop_3',
                'Cisco-IOS-XR-ipv6-acl-cfg', False),
            ],
            'Cisco-IOS-XR-ipv6-acl-cfg',
            'next-hop',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-ipv6-acl-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_acl_cfg',
        ),
    },
    'Ipv6AclAndPrefixList.Accesses.Access.AccessListEntries.AccessListEntry.HeaderFlags' : {
        'meta_info' : _MetaInfoClass('Ipv6AclAndPrefixList.Accesses.Access.AccessListEntries.AccessListEntry.HeaderFlags', REFERENCE_CLASS,
            '''Match if header-flag is present.''',
            False, 
            [
            _MetaInfoClassMember('routing', ATTRIBUTE, 'Empty', 'empty',
                None, None,
                [], [],
                '''                Match if routing header is present.
                ''',
                'routing',
                'Cisco-IOS-XR-ipv6-acl-cfg', False),
            _MetaInfoClassMember('destopts', ATTRIBUTE, 'Empty', 'empty',
                None, None,
                [], [],
                '''                Match if destops header is present.
                ''',
                'destopts',
                'Cisco-IOS-XR-ipv6-acl-cfg', False),
            _MetaInfoClassMember('hop-by-hop', ATTRIBUTE, 'Empty', 'empty',
                None, None,
                [], [],
                '''                Match if hop-by-hop header is present.
                ''',
                'hop_by_hop',
                'Cisco-IOS-XR-ipv6-acl-cfg', False),
            _MetaInfoClassMember('fragments', ATTRIBUTE, 'Empty', 'empty',
                None, None,
                [], [],
                '''                Match if fragments header is present.
                ''',
                'fragments',
                'Cisco-IOS-XR-ipv6-acl-cfg', False),
            _MetaInfoClassMember('authen', ATTRIBUTE, 'Empty', 'empty',
                None, None,
                [], [],
                '''                Match if authen header is present.
                ''',
                'authen',
                'Cisco-IOS-XR-ipv6-acl-cfg', False),
            ],
            'Cisco-IOS-XR-ipv6-acl-cfg',
            'header-flags',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-ipv6-acl-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_acl_cfg',
        ),
    },
    'Ipv6AclAndPrefixList.Accesses.Access.AccessListEntries.AccessListEntry' : {
        'meta_info' : _MetaInfoClass('Ipv6AclAndPrefixList.Accesses.Access.AccessListEntries.AccessListEntry', REFERENCE_LIST,
            '''An ACL entry; either a description (remark)
or anAccess List Entry to match against''',
            False, 
            [
            _MetaInfoClassMember('sequence-number', ATTRIBUTE, 'int', 'dt2:Ipv6-acl-sequence-number-range',
                None, None,
                [('1', '2147483643')], [],
                '''                Sequence number of access list entry
                ''',
                'sequence_number',
                'Cisco-IOS-XR-ipv6-acl-cfg', True),
            _MetaInfoClassMember('grant', REFERENCE_ENUM_CLASS, 'Ipv6AclGrantEnum', 'ipv6-acl-dt:Ipv6-acl-grant-enum',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_acl_datatypes', 'Ipv6AclGrantEnum',
                [], [],
                '''                Forwarding action for the packet. This is required
                for any non-remark ACE. Leave unspecified otherwise.
                ''',
                'grant',
                'Cisco-IOS-XR-ipv6-acl-cfg', False),
            _MetaInfoClassMember('protocol-operator', REFERENCE_ENUM_CLASS, 'Ipv6AclOperatorEnum', 'ipv6-acl-dt:Ipv6-acl-operator-enum',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_acl_datatypes', 'Ipv6AclOperatorEnum',
                [], [],
                '''                Protocol operator. User can specify equal or leave
                it unspecified for singleton protocol match, or
                specify range for protocol range match.
                ''',
                'protocol_operator',
                'Cisco-IOS-XR-ipv6-acl-cfg', False),
            _MetaInfoClassMember('protocol', REFERENCE_UNION, 'str', 'ipv6-acl-dt:Ipv6-acl-protocol-number',
                None, None,
                [], [],
                '''                Protocol number to match. It can be used for the lower
                bound (range operator) or single value (equal operator).
                Any value not in the permissible range will be rejected.
                When leave unspecified, default value is ipv6.
                ''',
                'protocol',
                'Cisco-IOS-XR-ipv6-acl-cfg', False, [
                    _MetaInfoClassMember('protocol', REFERENCE_ENUM_CLASS, 'Ipv6AclProtocolNumber', 'enumeration',
                        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_acl_datatypes', 'Ipv6AclProtocolNumber',
                        [], [],
                        '''                        Protocol number to match. It can be used for the lower
                        bound (range operator) or single value (equal operator).
                        Any value not in the permissible range will be rejected.
                        When leave unspecified, default value is ipv6.
                        ''',
                        'protocol',
                        'Cisco-IOS-XR-ipv6-acl-cfg', False),
                    _MetaInfoClassMember('protocol', ATTRIBUTE, 'int', 'uint32',
                        None, None,
                        [('0', '255')], [],
                        '''                        Protocol number to match. It can be used for the lower
                        bound (range operator) or single value (equal operator).
                        Any value not in the permissible range will be rejected.
                        When leave unspecified, default value is ipv6.
                        ''',
                        'protocol',
                        'Cisco-IOS-XR-ipv6-acl-cfg', False),
                ]),
            _MetaInfoClassMember('protocol2', REFERENCE_UNION, 'str', 'ipv6-acl-dt:Ipv6-acl-protocol-number',
                None, None,
                [], [],
                '''                Protocol2 to match. It is used in upper bound (range
                operator). Any value not in the permissible range will
                be rejected.
                ''',
                'protocol2',
                'Cisco-IOS-XR-ipv6-acl-cfg', False, [
                    _MetaInfoClassMember('protocol2', REFERENCE_ENUM_CLASS, 'Ipv6AclProtocolNumber', 'enumeration',
                        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_acl_datatypes', 'Ipv6AclProtocolNumber',
                        [], [],
                        '''                        Protocol2 to match. It is used in upper bound (range
                        operator). Any value not in the permissible range will
                        be rejected.
                        ''',
                        'protocol2',
                        'Cisco-IOS-XR-ipv6-acl-cfg', False),
                    _MetaInfoClassMember('protocol2', ATTRIBUTE, 'int', 'uint32',
                        None, None,
                        [('0', '255')], [],
                        '''                        Protocol2 to match. It is used in upper bound (range
                        operator). Any value not in the permissible range will
                        be rejected.
                        ''',
                        'protocol2',
                        'Cisco-IOS-XR-ipv6-acl-cfg', False),
                ]),
            _MetaInfoClassMember('source-network', REFERENCE_CLASS, 'SourceNetwork', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_acl_cfg', 'Ipv6AclAndPrefixList.Accesses.Access.AccessListEntries.AccessListEntry.SourceNetwork',
                [], [],
                '''                Source network settings.
                ''',
                'source_network',
                'Cisco-IOS-XR-ipv6-acl-cfg', False),
            _MetaInfoClassMember('destination-network', REFERENCE_CLASS, 'DestinationNetwork', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_acl_cfg', 'Ipv6AclAndPrefixList.Accesses.Access.AccessListEntries.AccessListEntry.DestinationNetwork',
                [], [],
                '''                Destination network settings.
                ''',
                'destination_network',
                'Cisco-IOS-XR-ipv6-acl-cfg', False),
            _MetaInfoClassMember('source-port', REFERENCE_CLASS, 'SourcePort', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_acl_cfg', 'Ipv6AclAndPrefixList.Accesses.Access.AccessListEntries.AccessListEntry.SourcePort',
                [], [],
                '''                Source port settings.
                ''',
                'source_port',
                'Cisco-IOS-XR-ipv6-acl-cfg', False, has_when=True),
            _MetaInfoClassMember('destination-port', REFERENCE_CLASS, 'DestinationPort', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_acl_cfg', 'Ipv6AclAndPrefixList.Accesses.Access.AccessListEntries.AccessListEntry.DestinationPort',
                [], [],
                '''                Destination port settings.
                ''',
                'destination_port',
                'Cisco-IOS-XR-ipv6-acl-cfg', False, has_when=True),
            _MetaInfoClassMember('icmp', REFERENCE_CLASS, 'Icmp', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_acl_cfg', 'Ipv6AclAndPrefixList.Accesses.Access.AccessListEntries.AccessListEntry.Icmp',
                [], [],
                '''                ICMP settings.
                ''',
                'icmp',
                'Cisco-IOS-XR-ipv6-acl-cfg', False, has_when=True),
            _MetaInfoClassMember('tcp', REFERENCE_CLASS, 'Tcp', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_acl_cfg', 'Ipv6AclAndPrefixList.Accesses.Access.AccessListEntries.AccessListEntry.Tcp',
                [], [],
                '''                TCP settings.
                ''',
                'tcp',
                'Cisco-IOS-XR-ipv6-acl-cfg', False, has_when=True),
            _MetaInfoClassMember('packet-length', REFERENCE_CLASS, 'PacketLength', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_acl_cfg', 'Ipv6AclAndPrefixList.Accesses.Access.AccessListEntries.AccessListEntry.PacketLength',
                [], [],
                '''                Packet length settings.
                ''',
                'packet_length',
                'Cisco-IOS-XR-ipv6-acl-cfg', False),
            _MetaInfoClassMember('time-to-live', REFERENCE_CLASS, 'TimeToLive', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_acl_cfg', 'Ipv6AclAndPrefixList.Accesses.Access.AccessListEntries.AccessListEntry.TimeToLive',
                [], [],
                '''                TTL settings.
                ''',
                'time_to_live',
                'Cisco-IOS-XR-ipv6-acl-cfg', False),
            _MetaInfoClassMember('DSCPValues', REFERENCE_CLASS, 'DSCPValues', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_acl_cfg', 'Ipv6AclAndPrefixList.Accesses.Access.AccessListEntries.AccessListEntry.DSCPValues',
                [], [],
                '''                DSCP settings.
                ''',
                'dscpvalues',
                'Cisco-IOS-XR-ipv6-acl-cfg', False),
            _MetaInfoClassMember('dscp', REFERENCE_UNION, 'str', 'ipv6-acl-dt:Ipv6-acl-dscp-number',
                None, None,
                [], [],
                '''                DSCP value to match without any operators.
                Any value not in the permissible range will be rejected.
                Leave unspecified if DSCP comparison is not to be
                performed. For Setting dscp values, use the dscp
                container as this leaf will be deprecated soon.
                ''',
                'dscp',
                'Cisco-IOS-XR-ipv6-acl-cfg', False, [
                    _MetaInfoClassMember('dscp', REFERENCE_ENUM_CLASS, 'Ipv6AclDscpNumber', 'enumeration',
                        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_acl_datatypes', 'Ipv6AclDscpNumber',
                        [], [],
                        '''                        DSCP value to match without any operators.
                        Any value not in the permissible range will be rejected.
                        Leave unspecified if DSCP comparison is not to be
                        performed. For Setting dscp values, use the dscp
                        container as this leaf will be deprecated soon.
                        ''',
                        'dscp',
                        'Cisco-IOS-XR-ipv6-acl-cfg', False),
                    _MetaInfoClassMember('dscp', ATTRIBUTE, 'int', 'uint32',
                        None, None,
                        [('0', '63')], [],
                        '''                        DSCP value to match without any operators.
                        Any value not in the permissible range will be rejected.
                        Leave unspecified if DSCP comparison is not to be
                        performed. For Setting dscp values, use the dscp
                        container as this leaf will be deprecated soon.
                        ''',
                        'dscp',
                        'Cisco-IOS-XR-ipv6-acl-cfg', False),
                ]),
            _MetaInfoClassMember('precedence', REFERENCE_UNION, 'str', 'ipv6-acl-dt:Ipv6-acl-precedence-number',
                None, None,
                [], [],
                '''                Precedence value to match (if a protocol was specified).
                Any value not in the permissible range will be rejected.
                Leave unspecified if precedence comparion is not to be
                performed.
                ''',
                'precedence',
                'Cisco-IOS-XR-ipv6-acl-cfg', False, [
                    _MetaInfoClassMember('precedence', REFERENCE_ENUM_CLASS, 'Ipv6AclPrecedenceNumber', 'enumeration',
                        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_acl_datatypes', 'Ipv6AclPrecedenceNumber',
                        [], [],
                        '''                        Precedence value to match (if a protocol was specified).
                        Any value not in the permissible range will be rejected.
                        Leave unspecified if precedence comparion is not to be
                        performed.
                        ''',
                        'precedence',
                        'Cisco-IOS-XR-ipv6-acl-cfg', False),
                    _MetaInfoClassMember('precedence', ATTRIBUTE, 'int', 'uint32',
                        None, None,
                        [('0', '7')], [],
                        '''                        Precedence value to match (if a protocol was specified).
                        Any value not in the permissible range will be rejected.
                        Leave unspecified if precedence comparion is not to be
                        performed.
                        ''',
                        'precedence',
                        'Cisco-IOS-XR-ipv6-acl-cfg', False),
                ]),
            _MetaInfoClassMember('next-hop', REFERENCE_CLASS, 'NextHop', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_acl_cfg', 'Ipv6AclAndPrefixList.Accesses.Access.AccessListEntries.AccessListEntry.NextHop',
                [], [],
                '''                Next-hop settings.
                ''',
                'next_hop',
                'Cisco-IOS-XR-ipv6-acl-cfg', False),
            _MetaInfoClassMember('counter-name', ATTRIBUTE, 'str', 'string',
                None, None,
                [(1, 64)], [],
                '''                Name of counter to aggregate hardware statistics.
                ''',
                'counter_name',
                'Cisco-IOS-XR-ipv6-acl-cfg', False),
            _MetaInfoClassMember('log-option', REFERENCE_ENUM_CLASS, 'Ipv6AclLoggingEnum', 'ipv6-acl-dt:Ipv6-acl-logging-enum',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_acl_datatypes', 'Ipv6AclLoggingEnum',
                [], [],
                '''                Log the packet on this access-list-entry/rule.
                ''',
                'log_option',
                'Cisco-IOS-XR-ipv6-acl-cfg', False),
            _MetaInfoClassMember('capture', ATTRIBUTE, 'bool', 'boolean',
                None, None,
                [], [],
                '''                Enable capture if set to TRUE.
                ''',
                'capture',
                'Cisco-IOS-XR-ipv6-acl-cfg', False),
            _MetaInfoClassMember('undetermined-transport', ATTRIBUTE, 'bool', 'boolean',
                None, None,
                [], [],
                '''                Enable undetermined-transport if set to TRUE.
                ''',
                'undetermined_transport',
                'Cisco-IOS-XR-ipv6-acl-cfg', False),
            _MetaInfoClassMember('icmp-off', ATTRIBUTE, 'Empty', 'empty',
                None, None,
                [], [],
                '''                To turn off ICMP generation for deny ACEs.
                ''',
                'icmp_off',
                'Cisco-IOS-XR-ipv6-acl-cfg', False),
            _MetaInfoClassMember('qos-group', ATTRIBUTE, 'int', 'ipv6-acl-dt:Ipv6-acl-qos-group-number',
                None, None,
                [('0', '512')], [],
                '''                Set qos-group number. Any value not in the permissible
                range will be rejected.
                ''',
                'qos_group',
                'Cisco-IOS-XR-ipv6-acl-cfg', False),
            _MetaInfoClassMember('set-ttl', ATTRIBUTE, 'int', 'ipv6-acl-dt:Ipv6-acl-ttl-range',
                None, None,
                [('0', '255')], [],
                '''                Set TTL Value. Any value not in the permissible range
                will be rejected.
                ''',
                'set_ttl',
                'Cisco-IOS-XR-ipv6-acl-cfg', False),
            _MetaInfoClassMember('header-flags', REFERENCE_CLASS, 'HeaderFlags', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_acl_cfg', 'Ipv6AclAndPrefixList.Accesses.Access.AccessListEntries.AccessListEntry.HeaderFlags',
                [], [],
                '''                Match if header-flag is present.
                ''',
                'header_flags',
                'Cisco-IOS-XR-ipv6-acl-cfg', False),
            _MetaInfoClassMember('remark', ATTRIBUTE, 'str', 'string',
                None, None,
                [(0, 255)], [],
                '''                Description for the access-list-entry/rules.
                ''',
                'remark',
                'Cisco-IOS-XR-ipv6-acl-cfg', False),
            _MetaInfoClassMember('source-prefix-group', ATTRIBUTE, 'str', 'string',
                None, None,
                [(1, 64)], [],
                '''                IPv6 source network object group name.
                ''',
                'source_prefix_group',
                'Cisco-IOS-XR-ipv6-acl-cfg', False),
            _MetaInfoClassMember('destination-prefix-group', ATTRIBUTE, 'str', 'string',
                None, None,
                [(1, 64)], [],
                '''                IPv6 destination network object group name.
                ''',
                'destination_prefix_group',
                'Cisco-IOS-XR-ipv6-acl-cfg', False),
            _MetaInfoClassMember('source-port-group', ATTRIBUTE, 'str', 'string',
                None, None,
                [(1, 64)], [],
                '''                Source port object group name.
                ''',
                'source_port_group',
                'Cisco-IOS-XR-ipv6-acl-cfg', False),
            _MetaInfoClassMember('destination-port-group', ATTRIBUTE, 'str', 'string',
                None, None,
                [(1, 64)], [],
                '''                Destination port object group name.
                ''',
                'destination_port_group',
                'Cisco-IOS-XR-ipv6-acl-cfg', False),
            _MetaInfoClassMember('sequence-str', ATTRIBUTE, 'str', 'string',
                None, None,
                [(1, 64)], [],
                '''                Sequence String for the ace.
                ''',
                'sequence_str',
                'Cisco-IOS-XR-ipv6-acl-cfg', False),
            ],
            'Cisco-IOS-XR-ipv6-acl-cfg',
            'access-list-entry',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-ipv6-acl-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_acl_cfg',
        ),
    },
    'Ipv6AclAndPrefixList.Accesses.Access.AccessListEntries' : {
        'meta_info' : _MetaInfoClass('Ipv6AclAndPrefixList.Accesses.Access.AccessListEntries', REFERENCE_CLASS,
            '''ACL entry table; contains list of access list
entries''',
            False, 
            [
            _MetaInfoClassMember('access-list-entry', REFERENCE_LIST, 'AccessListEntry', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_acl_cfg', 'Ipv6AclAndPrefixList.Accesses.Access.AccessListEntries.AccessListEntry',
                [], [],
                '''                An ACL entry; either a description (remark)
                or anAccess List Entry to match against
                ''',
                'access_list_entry',
                'Cisco-IOS-XR-ipv6-acl-cfg', False),
            ],
            'Cisco-IOS-XR-ipv6-acl-cfg',
            'access-list-entries',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-ipv6-acl-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_acl_cfg',
        ),
    },
    'Ipv6AclAndPrefixList.Accesses.Access' : {
        'meta_info' : _MetaInfoClass('Ipv6AclAndPrefixList.Accesses.Access', REFERENCE_LIST,
            '''An ACL''',
            False, 
            [
            _MetaInfoClassMember('name', ATTRIBUTE, 'str', 'dt2:Ipv6-acl-prefix-list-name',
                None, None,
                [(1, 64)], [],
                '''                Name of the access list
                ''',
                'name',
                'Cisco-IOS-XR-ipv6-acl-cfg', True),
            _MetaInfoClassMember('access-list-entries', REFERENCE_CLASS, 'AccessListEntries', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_acl_cfg', 'Ipv6AclAndPrefixList.Accesses.Access.AccessListEntries',
                [], [],
                '''                ACL entry table; contains list of access list
                entries
                ''',
                'access_list_entries',
                'Cisco-IOS-XR-ipv6-acl-cfg', False),
            ],
            'Cisco-IOS-XR-ipv6-acl-cfg',
            'access',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-ipv6-acl-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_acl_cfg',
        ),
    },
    'Ipv6AclAndPrefixList.Accesses' : {
        'meta_info' : _MetaInfoClass('Ipv6AclAndPrefixList.Accesses', REFERENCE_CLASS,
            '''Table of access lists''',
            False, 
            [
            _MetaInfoClassMember('access', REFERENCE_LIST, 'Access', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_acl_cfg', 'Ipv6AclAndPrefixList.Accesses.Access',
                [], [],
                '''                An ACL
                ''',
                'access',
                'Cisco-IOS-XR-ipv6-acl-cfg', False),
            ],
            'Cisco-IOS-XR-ipv6-acl-cfg',
            'accesses',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-ipv6-acl-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_acl_cfg',
        ),
    },
    'Ipv6AclAndPrefixList' : {
        'meta_info' : _MetaInfoClass('Ipv6AclAndPrefixList', REFERENCE_CLASS,
            '''IPv6 ACL configuration data''',
            False, 
            [
            _MetaInfoClassMember('prefixes', REFERENCE_CLASS, 'Prefixes', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_acl_cfg', 'Ipv6AclAndPrefixList.Prefixes',
                [], [],
                '''                Table of prefix lists
                ''',
                'prefixes',
                'Cisco-IOS-XR-ipv6-acl-cfg', False),
            _MetaInfoClassMember('log-update', REFERENCE_CLASS, 'LogUpdate', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_acl_cfg', 'Ipv6AclAndPrefixList.LogUpdate',
                [], [],
                '''                Control access lists log updates
                ''',
                'log_update',
                'Cisco-IOS-XR-ipv6-acl-cfg', False),
            _MetaInfoClassMember('accesses', REFERENCE_CLASS, 'Accesses', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_acl_cfg', 'Ipv6AclAndPrefixList.Accesses',
                [], [],
                '''                Table of access lists
                ''',
                'accesses',
                'Cisco-IOS-XR-ipv6-acl-cfg', False),
            ],
            'Cisco-IOS-XR-ipv6-acl-cfg',
            'ipv6-acl-and-prefix-list',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-ipv6-acl-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_acl_cfg',
        ),
    },
}
_meta_table['Ipv6AclAndPrefixList.Prefixes.Prefix.PrefixListEntries.PrefixListEntry']['meta_info'].parent =_meta_table['Ipv6AclAndPrefixList.Prefixes.Prefix.PrefixListEntries']['meta_info']
_meta_table['Ipv6AclAndPrefixList.Prefixes.Prefix.PrefixListEntries']['meta_info'].parent =_meta_table['Ipv6AclAndPrefixList.Prefixes.Prefix']['meta_info']
_meta_table['Ipv6AclAndPrefixList.Prefixes.Prefix']['meta_info'].parent =_meta_table['Ipv6AclAndPrefixList.Prefixes']['meta_info']
_meta_table['Ipv6AclAndPrefixList.Accesses.Access.AccessListEntries.AccessListEntry.NextHop.NextHop1']['meta_info'].parent =_meta_table['Ipv6AclAndPrefixList.Accesses.Access.AccessListEntries.AccessListEntry.NextHop']['meta_info']
_meta_table['Ipv6AclAndPrefixList.Accesses.Access.AccessListEntries.AccessListEntry.NextHop.NextHop2']['meta_info'].parent =_meta_table['Ipv6AclAndPrefixList.Accesses.Access.AccessListEntries.AccessListEntry.NextHop']['meta_info']
_meta_table['Ipv6AclAndPrefixList.Accesses.Access.AccessListEntries.AccessListEntry.NextHop.NextHop3']['meta_info'].parent =_meta_table['Ipv6AclAndPrefixList.Accesses.Access.AccessListEntries.AccessListEntry.NextHop']['meta_info']
_meta_table['Ipv6AclAndPrefixList.Accesses.Access.AccessListEntries.AccessListEntry.SourceNetwork']['meta_info'].parent =_meta_table['Ipv6AclAndPrefixList.Accesses.Access.AccessListEntries.AccessListEntry']['meta_info']
_meta_table['Ipv6AclAndPrefixList.Accesses.Access.AccessListEntries.AccessListEntry.DestinationNetwork']['meta_info'].parent =_meta_table['Ipv6AclAndPrefixList.Accesses.Access.AccessListEntries.AccessListEntry']['meta_info']
_meta_table['Ipv6AclAndPrefixList.Accesses.Access.AccessListEntries.AccessListEntry.SourcePort']['meta_info'].parent =_meta_table['Ipv6AclAndPrefixList.Accesses.Access.AccessListEntries.AccessListEntry']['meta_info']
_meta_table['Ipv6AclAndPrefixList.Accesses.Access.AccessListEntries.AccessListEntry.DestinationPort']['meta_info'].parent =_meta_table['Ipv6AclAndPrefixList.Accesses.Access.AccessListEntries.AccessListEntry']['meta_info']
_meta_table['Ipv6AclAndPrefixList.Accesses.Access.AccessListEntries.AccessListEntry.Icmp']['meta_info'].parent =_meta_table['Ipv6AclAndPrefixList.Accesses.Access.AccessListEntries.AccessListEntry']['meta_info']
_meta_table['Ipv6AclAndPrefixList.Accesses.Access.AccessListEntries.AccessListEntry.Tcp']['meta_info'].parent =_meta_table['Ipv6AclAndPrefixList.Accesses.Access.AccessListEntries.AccessListEntry']['meta_info']
_meta_table['Ipv6AclAndPrefixList.Accesses.Access.AccessListEntries.AccessListEntry.PacketLength']['meta_info'].parent =_meta_table['Ipv6AclAndPrefixList.Accesses.Access.AccessListEntries.AccessListEntry']['meta_info']
_meta_table['Ipv6AclAndPrefixList.Accesses.Access.AccessListEntries.AccessListEntry.TimeToLive']['meta_info'].parent =_meta_table['Ipv6AclAndPrefixList.Accesses.Access.AccessListEntries.AccessListEntry']['meta_info']
_meta_table['Ipv6AclAndPrefixList.Accesses.Access.AccessListEntries.AccessListEntry.DSCPValues']['meta_info'].parent =_meta_table['Ipv6AclAndPrefixList.Accesses.Access.AccessListEntries.AccessListEntry']['meta_info']
_meta_table['Ipv6AclAndPrefixList.Accesses.Access.AccessListEntries.AccessListEntry.NextHop']['meta_info'].parent =_meta_table['Ipv6AclAndPrefixList.Accesses.Access.AccessListEntries.AccessListEntry']['meta_info']
_meta_table['Ipv6AclAndPrefixList.Accesses.Access.AccessListEntries.AccessListEntry.HeaderFlags']['meta_info'].parent =_meta_table['Ipv6AclAndPrefixList.Accesses.Access.AccessListEntries.AccessListEntry']['meta_info']
_meta_table['Ipv6AclAndPrefixList.Accesses.Access.AccessListEntries.AccessListEntry']['meta_info'].parent =_meta_table['Ipv6AclAndPrefixList.Accesses.Access.AccessListEntries']['meta_info']
_meta_table['Ipv6AclAndPrefixList.Accesses.Access.AccessListEntries']['meta_info'].parent =_meta_table['Ipv6AclAndPrefixList.Accesses.Access']['meta_info']
_meta_table['Ipv6AclAndPrefixList.Accesses.Access']['meta_info'].parent =_meta_table['Ipv6AclAndPrefixList.Accesses']['meta_info']
_meta_table['Ipv6AclAndPrefixList.Prefixes']['meta_info'].parent =_meta_table['Ipv6AclAndPrefixList']['meta_info']
_meta_table['Ipv6AclAndPrefixList.LogUpdate']['meta_info'].parent =_meta_table['Ipv6AclAndPrefixList']['meta_info']
_meta_table['Ipv6AclAndPrefixList.Accesses']['meta_info'].parent =_meta_table['Ipv6AclAndPrefixList']['meta_info']
