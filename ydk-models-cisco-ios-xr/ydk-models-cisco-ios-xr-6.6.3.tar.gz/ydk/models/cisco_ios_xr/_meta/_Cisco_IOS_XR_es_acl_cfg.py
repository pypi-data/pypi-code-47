
'''
This is auto-generated file,
which includes metadata for module Cisco_IOS_XR_es_acl_cfg
'''

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_LIST, REFERENCE_LEAFLIST, REFERENCE_BITS, REFERENCE_UNION
from ydk._core._dm_meta_info import REFERENCE_CLASS, REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, ANYXML_CLASS
from ydk._core._importer import _yang_ns

_meta_table = {
    'EsAclGrantEnum' : _MetaInfoEnum('EsAclGrantEnum',
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_es_acl_cfg', 'EsAclGrantEnum',
        '''ES ACL forwarding action.''',
        {
            'deny':'deny',
            'permit':'permit',
        }, 'Cisco-IOS-XR-es-acl-cfg', _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-es-acl-cfg']),
    'EsAcl.Accesses.Access.AccessListEntries.AccessListEntry.SourceNetwork' : {
        'meta_info' : _MetaInfoClass('EsAcl.Accesses.Access.AccessListEntries.AccessListEntry.SourceNetwork', REFERENCE_CLASS,
            '''Source network settings.''',
            False, 
            [
            _MetaInfoClassMember('source-address', ATTRIBUTE, 'str', 'es-acl-address',
                None, None,
                [], [b'([0-9a-fA-F]{1,4}(\\.[0-9a-fA-F]{1,4}){2})'],
                '''                Source address to match, leave unspecified
                for any.
                ''',
                'source_address',
                'Cisco-IOS-XR-es-acl-cfg', False),
            _MetaInfoClassMember('source-wild-card-bits', ATTRIBUTE, 'str', 'es-acl-address',
                None, None,
                [], [b'([0-9a-fA-F]{1,4}(\\.[0-9a-fA-F]{1,4}){2})'],
                '''                Wildcard bits to apply to source address
                (if specified), leave unspecified for no
                wildcarding.
                ''',
                'source_wild_card_bits',
                'Cisco-IOS-XR-es-acl-cfg', False),
            ],
            'Cisco-IOS-XR-es-acl-cfg',
            'source-network',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-es-acl-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_es_acl_cfg',
        ),
    },
    'EsAcl.Accesses.Access.AccessListEntries.AccessListEntry.DestinationNetwork' : {
        'meta_info' : _MetaInfoClass('EsAcl.Accesses.Access.AccessListEntries.AccessListEntry.DestinationNetwork', REFERENCE_CLASS,
            '''Destination network settings.''',
            False, 
            [
            _MetaInfoClassMember('destination-address', ATTRIBUTE, 'str', 'es-acl-address',
                None, None,
                [], [b'([0-9a-fA-F]{1,4}(\\.[0-9a-fA-F]{1,4}){2})'],
                '''                Destination address to match (if a protocol
                was specified), leave unspecified for any.
                ''',
                'destination_address',
                'Cisco-IOS-XR-es-acl-cfg', False),
            _MetaInfoClassMember('destination-wild-card-bits', ATTRIBUTE, 'str', 'es-acl-address',
                None, None,
                [], [b'([0-9a-fA-F]{1,4}(\\.[0-9a-fA-F]{1,4}){2})'],
                '''                Wildcard bits to apply to destination address
                (if specified), leave unspecified for no
                wildcarding.
                ''',
                'destination_wild_card_bits',
                'Cisco-IOS-XR-es-acl-cfg', False),
            ],
            'Cisco-IOS-XR-es-acl-cfg',
            'destination-network',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-es-acl-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_es_acl_cfg',
        ),
    },
    'EsAcl.Accesses.Access.AccessListEntries.AccessListEntry' : {
        'meta_info' : _MetaInfoClass('EsAcl.Accesses.Access.AccessListEntries.AccessListEntry', REFERENCE_LIST,
            '''An ACL entry; either a description (remark)
or anAccess List Entry to match against''',
            False, 
            [
            _MetaInfoClassMember('sequence-number', ATTRIBUTE, 'int', 'dt1:Acl-sequence-number-range',
                None, None,
                [('1', '2147483646')], [],
                '''                Sequence number of access list entry
                ''',
                'sequence_number',
                'Cisco-IOS-XR-es-acl-cfg', True),
            _MetaInfoClassMember('grant', REFERENCE_ENUM_CLASS, 'EsAclGrantEnum', 'es-acl-grant-enum',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_es_acl_cfg', 'EsAclGrantEnum',
                [], [],
                '''                Forwarding action for the packet. This is required
                for any non-remark ACE. Leave unspecified otherwise.
                ''',
                'grant',
                'Cisco-IOS-XR-es-acl-cfg', False),
            _MetaInfoClassMember('source-network', REFERENCE_CLASS, 'SourceNetwork', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_es_acl_cfg', 'EsAcl.Accesses.Access.AccessListEntries.AccessListEntry.SourceNetwork',
                [], [],
                '''                Source network settings.
                ''',
                'source_network',
                'Cisco-IOS-XR-es-acl-cfg', False),
            _MetaInfoClassMember('destination-network', REFERENCE_CLASS, 'DestinationNetwork', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_es_acl_cfg', 'EsAcl.Accesses.Access.AccessListEntries.AccessListEntry.DestinationNetwork',
                [], [],
                '''                Destination network settings.
                ''',
                'destination_network',
                'Cisco-IOS-XR-es-acl-cfg', False),
            _MetaInfoClassMember('vlan1', ATTRIBUTE, 'int', 'es-acl-dt:Es-acl-vlan-range',
                None, None,
                [('0', '4095')], [],
                '''                This 12-bit VLAN-ID in the VLAN Tag header uniquely
                identifies the VLAN. It can be used for the lower bound
                (in range) or single value. Any value not in the
                permissible range will be rejected.
                ''',
                'vlan1',
                'Cisco-IOS-XR-es-acl-cfg', False),
            _MetaInfoClassMember('vlan2', ATTRIBUTE, 'int', 'es-acl-dt:Es-acl-vlan-range',
                None, None,
                [('0', '4095')], [],
                '''                This 12 bit VLAN-ID in the VLAN Tag header uniquely
                identifies the VLAN. It is used in the upper bound
                (in range). Any value not in the permissible range
                will be rejected.
                ''',
                'vlan2',
                'Cisco-IOS-XR-es-acl-cfg', False),
            _MetaInfoClassMember('cos', ATTRIBUTE, 'int', 'es-acl-dt:Es-acl-cos-range',
                None, None,
                [('0', '7')], [],
                '''                Class of Service value. Any value not in the
                permissible range will be rejected.
                ''',
                'cos',
                'Cisco-IOS-XR-es-acl-cfg', False),
            _MetaInfoClassMember('dei', ATTRIBUTE, 'int', 'es-acl-dt:Es-acl-dei-range',
                None, None,
                [('0', '1')], [],
                '''                Discard Eligibility Indication bit. User can specify
                1 to indicate the bit is set. Leave unspecified
                otherwise.
                ''',
                'dei',
                'Cisco-IOS-XR-es-acl-cfg', False),
            _MetaInfoClassMember('inner-vlan1', ATTRIBUTE, 'int', 'es-acl-dt:Es-acl-vlan-range',
                None, None,
                [('0', '4095')], [],
                '''                This represents the QinQ vlan identifier. It can be used for
                the lower bound (in range) or single value. Any value not
                in the permissible range will be rejected.
                ''',
                'inner_vlan1',
                'Cisco-IOS-XR-es-acl-cfg', False),
            _MetaInfoClassMember('inner-vlan2', ATTRIBUTE, 'int', 'es-acl-dt:Es-acl-vlan-range',
                None, None,
                [('0', '4095')], [],
                '''                This represents the QinQ vlan identifier. It is used in
                the upper bound (in range). Any value not in the permissible
                range will be rejected.
                ''',
                'inner_vlan2',
                'Cisco-IOS-XR-es-acl-cfg', False),
            _MetaInfoClassMember('inner-cos', ATTRIBUTE, 'int', 'es-acl-dt:Es-acl-cos-range',
                None, None,
                [('0', '7')], [],
                '''                Class of Service of Inner Header. Any value not in the
                permissible range will be rejected.
                ''',
                'inner_cos',
                'Cisco-IOS-XR-es-acl-cfg', False),
            _MetaInfoClassMember('inner-dei', ATTRIBUTE, 'int', 'es-acl-dt:Es-acl-dei-range',
                None, None,
                [('0', '1')], [],
                '''                Discard Eligibility Indication for Inner Header. User
                can specify 1 to indicate the bit is set. Leave
                unspecified otherwise.
                ''',
                'inner_dei',
                'Cisco-IOS-XR-es-acl-cfg', False),
            _MetaInfoClassMember('remark', ATTRIBUTE, 'str', 'string',
                None, None,
                [(0, 255)], [],
                '''                Description for the access-list-entry/rule.
                ''',
                'remark',
                'Cisco-IOS-XR-es-acl-cfg', False),
            _MetaInfoClassMember('ether-type-number', ATTRIBUTE, 'str', 'xr:Hex-integer-16',
                None, None,
                [], [b'[0-9a-fA-F]{1,4}'],
                '''                Ethernet type Number in Hex. Any value not in the
                permissible range will be rejected.
                ''',
                'ether_type_number',
                'Cisco-IOS-XR-es-acl-cfg', False),
            _MetaInfoClassMember('capture', ATTRIBUTE, 'bool', 'boolean',
                None, None,
                [], [],
                '''                Enable capture if set to TRUE.
                ''',
                'capture',
                'Cisco-IOS-XR-es-acl-cfg', False),
            _MetaInfoClassMember('log-option', ATTRIBUTE, 'int', 'es-acl-dt:Es-acl-log-range',
                None, None,
                [('0', '1')], [],
                '''                Log the packet on this access-list-entry/rule.
                User can specify 1 to enable logging
                the match, leave unspecified otherwise.
                ''',
                'log_option',
                'Cisco-IOS-XR-es-acl-cfg', False),
            _MetaInfoClassMember('sequence-str', ATTRIBUTE, 'str', 'string',
                None, None,
                [(1, 64)], [],
                '''                Sequence String for the ace.
                ''',
                'sequence_str',
                'Cisco-IOS-XR-es-acl-cfg', False),
            ],
            'Cisco-IOS-XR-es-acl-cfg',
            'access-list-entry',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-es-acl-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_es_acl_cfg',
        ),
    },
    'EsAcl.Accesses.Access.AccessListEntries' : {
        'meta_info' : _MetaInfoClass('EsAcl.Accesses.Access.AccessListEntries', REFERENCE_CLASS,
            '''ACL entry table; contains list of access list
entries''',
            False, 
            [
            _MetaInfoClassMember('access-list-entry', REFERENCE_LIST, 'AccessListEntry', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_es_acl_cfg', 'EsAcl.Accesses.Access.AccessListEntries.AccessListEntry',
                [], [],
                '''                An ACL entry; either a description (remark)
                or anAccess List Entry to match against
                ''',
                'access_list_entry',
                'Cisco-IOS-XR-es-acl-cfg', False),
            ],
            'Cisco-IOS-XR-es-acl-cfg',
            'access-list-entries',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-es-acl-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_es_acl_cfg',
        ),
    },
    'EsAcl.Accesses.Access' : {
        'meta_info' : _MetaInfoClass('EsAcl.Accesses.Access', REFERENCE_LIST,
            '''An ACL''',
            False, 
            [
            _MetaInfoClassMember('name', ATTRIBUTE, 'str', 'Es-acl-name',
                None, None,
                [(1, 64)], [],
                '''                Name of the access list
                ''',
                'name',
                'Cisco-IOS-XR-es-acl-cfg', True),
            _MetaInfoClassMember('access-list-entries', REFERENCE_CLASS, 'AccessListEntries', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_es_acl_cfg', 'EsAcl.Accesses.Access.AccessListEntries',
                [], [],
                '''                ACL entry table; contains list of access list
                entries
                ''',
                'access_list_entries',
                'Cisco-IOS-XR-es-acl-cfg', False),
            ],
            'Cisco-IOS-XR-es-acl-cfg',
            'access',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-es-acl-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_es_acl_cfg',
        ),
    },
    'EsAcl.Accesses' : {
        'meta_info' : _MetaInfoClass('EsAcl.Accesses', REFERENCE_CLASS,
            '''Table of access lists''',
            False, 
            [
            _MetaInfoClassMember('access', REFERENCE_LIST, 'Access', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_es_acl_cfg', 'EsAcl.Accesses.Access',
                [], [],
                '''                An ACL
                ''',
                'access',
                'Cisco-IOS-XR-es-acl-cfg', False),
            ],
            'Cisco-IOS-XR-es-acl-cfg',
            'accesses',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-es-acl-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_es_acl_cfg',
        ),
    },
    'EsAcl' : {
        'meta_info' : _MetaInfoClass('EsAcl', REFERENCE_CLASS,
            '''Layer 2 ACL configuration data''',
            False, 
            [
            _MetaInfoClassMember('accesses', REFERENCE_CLASS, 'Accesses', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_es_acl_cfg', 'EsAcl.Accesses',
                [], [],
                '''                Table of access lists
                ''',
                'accesses',
                'Cisco-IOS-XR-es-acl-cfg', False),
            ],
            'Cisco-IOS-XR-es-acl-cfg',
            'es-acl',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-es-acl-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_es_acl_cfg',
        ),
    },
}
_meta_table['EsAcl.Accesses.Access.AccessListEntries.AccessListEntry.SourceNetwork']['meta_info'].parent =_meta_table['EsAcl.Accesses.Access.AccessListEntries.AccessListEntry']['meta_info']
_meta_table['EsAcl.Accesses.Access.AccessListEntries.AccessListEntry.DestinationNetwork']['meta_info'].parent =_meta_table['EsAcl.Accesses.Access.AccessListEntries.AccessListEntry']['meta_info']
_meta_table['EsAcl.Accesses.Access.AccessListEntries.AccessListEntry']['meta_info'].parent =_meta_table['EsAcl.Accesses.Access.AccessListEntries']['meta_info']
_meta_table['EsAcl.Accesses.Access.AccessListEntries']['meta_info'].parent =_meta_table['EsAcl.Accesses.Access']['meta_info']
_meta_table['EsAcl.Accesses.Access']['meta_info'].parent =_meta_table['EsAcl.Accesses']['meta_info']
_meta_table['EsAcl.Accesses']['meta_info'].parent =_meta_table['EsAcl']['meta_info']
