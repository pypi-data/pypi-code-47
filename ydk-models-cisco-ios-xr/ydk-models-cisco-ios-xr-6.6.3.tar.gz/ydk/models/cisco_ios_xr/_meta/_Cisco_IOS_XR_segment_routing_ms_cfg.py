
'''
This is auto-generated file,
which includes metadata for module Cisco_IOS_XR_segment_routing_ms_cfg
'''

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_LIST, REFERENCE_LEAFLIST, REFERENCE_BITS, REFERENCE_UNION
from ydk._core._dm_meta_info import REFERENCE_CLASS, REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, ANYXML_CLASS
from ydk._core._importer import _yang_ns

_meta_table = {
    'SrmsMiFlag' : _MetaInfoEnum('SrmsMiFlag',
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_segment_routing_ms_cfg', 'SrmsMiFlag',
        '''Srms mi flag''',
        {
            'disable':'disable',
            'enable':'enable',
        }, 'Cisco-IOS-XR-segment-routing-ms-cfg', _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-segment-routing-ms-cfg']),
    'SrmsAddressFamily' : _MetaInfoEnum('SrmsAddressFamily',
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_segment_routing_ms_cfg', 'SrmsAddressFamily',
        '''Srms address family''',
        {
            'ipv4':'ipv4',
            'ipv6':'ipv6',
        }, 'Cisco-IOS-XR-segment-routing-ms-cfg', _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-segment-routing-ms-cfg']),
    'SidTypeList' : _MetaInfoEnum('SidTypeList',
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_segment_routing_ms_cfg', 'SidTypeList',
        '''Sid type list''',
        {
            'absolute':'absolute',
            'index':'index',
        }, 'Cisco-IOS-XR-segment-routing-ms-cfg', _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-segment-routing-ms-cfg']),
    'Sr.LocalBlock' : {
        'meta_info' : _MetaInfoClass('Sr.LocalBlock', REFERENCE_CLASS,
            '''Segment Routing Local Block of Labels''',
            False, 
            [
            _MetaInfoClassMember('lower-bound', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('15000', '1048574')], [],
                '''                SRLB Lower Bound
                ''',
                'lower_bound',
                'Cisco-IOS-XR-segment-routing-ms-cfg', False, is_mandatory=True),
            _MetaInfoClassMember('upper-bound', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('15001', '1048575')], [],
                '''                SRLB Upper Bound
                ''',
                'upper_bound',
                'Cisco-IOS-XR-segment-routing-ms-cfg', False, is_mandatory=True),
            ],
            'Cisco-IOS-XR-segment-routing-ms-cfg',
            'local-block',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-segment-routing-ms-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_segment_routing_ms_cfg',
            is_presence=True,
        ),
    },
    'Sr.Mappings.Mapping' : {
        'meta_info' : _MetaInfoClass('Sr.Mappings.Mapping', REFERENCE_LIST,
            '''IP prefix to SID mapping''',
            False, 
            [
            _MetaInfoClassMember('af', REFERENCE_ENUM_CLASS, 'SrmsAddressFamily', 'Srms-address-family',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_segment_routing_ms_cfg', 'SrmsAddressFamily',
                [], [],
                '''                Address Family
                ''',
                'af',
                'Cisco-IOS-XR-segment-routing-ms-cfg', True),
            _MetaInfoClassMember('ip', REFERENCE_UNION, 'str', 'inet:ip-address-no-zone',
                None, None,
                [], [],
                '''                IP prefix
                ''',
                'ip',
                'Cisco-IOS-XR-segment-routing-ms-cfg', True, [
                    _MetaInfoClassMember('ip', ATTRIBUTE, 'str', 'inet:ipv4-address-no-zone',
                        None, None,
                        [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'],
                        '''                        IP prefix
                        ''',
                        'ip',
                        'Cisco-IOS-XR-segment-routing-ms-cfg', True),
                    _MetaInfoClassMember('ip', ATTRIBUTE, 'str', 'inet:ipv6-address-no-zone',
                        None, None,
                        [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'],
                        '''                        IP prefix
                        ''',
                        'ip',
                        'Cisco-IOS-XR-segment-routing-ms-cfg', True),
                ]),
            _MetaInfoClassMember('mask', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('1', '128')], [],
                '''                Mask
                ''',
                'mask',
                'Cisco-IOS-XR-segment-routing-ms-cfg', True),
            _MetaInfoClassMember('sid-start', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('0', '1048575')], [],
                '''                Start of SID index range
                ''',
                'sid_start',
                'Cisco-IOS-XR-segment-routing-ms-cfg', False),
            _MetaInfoClassMember('sid-range', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('0', '65535')], [],
                '''                Range (number of SIDs)
                ''',
                'sid_range',
                'Cisco-IOS-XR-segment-routing-ms-cfg', False),
            _MetaInfoClassMember('flag-attached', REFERENCE_ENUM_CLASS, 'SrmsMiFlag', 'Srms-mi-flag',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_segment_routing_ms_cfg', 'SrmsMiFlag',
                [], [],
                '''                Enable/Disable Attached flag
                ''',
                'flag_attached',
                'Cisco-IOS-XR-segment-routing-ms-cfg', False),
            ],
            'Cisco-IOS-XR-segment-routing-ms-cfg',
            'mapping',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-segment-routing-ms-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_segment_routing_ms_cfg',
        ),
    },
    'Sr.Mappings' : {
        'meta_info' : _MetaInfoClass('Sr.Mappings', REFERENCE_CLASS,
            '''Mapping Server''',
            False, 
            [
            _MetaInfoClassMember('mapping', REFERENCE_LIST, 'Mapping', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_segment_routing_ms_cfg', 'Sr.Mappings.Mapping',
                [], [],
                '''                IP prefix to SID mapping
                ''',
                'mapping',
                'Cisco-IOS-XR-segment-routing-ms-cfg', False),
            ],
            'Cisco-IOS-XR-segment-routing-ms-cfg',
            'mappings',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-segment-routing-ms-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_segment_routing_ms_cfg',
        ),
    },
    'Sr.AdjacencySid.Interfaces.Interface.AddressFamilies.AddressFamily.NextHops.NextHop.L2AdjacencySid' : {
        'meta_info' : _MetaInfoClass('Sr.AdjacencySid.Interfaces.Interface.AddressFamilies.AddressFamily.NextHops.NextHop.L2AdjacencySid', REFERENCE_CLASS,
            '''L2 Adjacency SID type and value''',
            False, 
            [
            _MetaInfoClassMember('sid-type', REFERENCE_ENUM_CLASS, 'SidTypeList', 'Sid-type-list',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_segment_routing_ms_cfg', 'SidTypeList',
                [], [],
                '''                SID type
                ''',
                'sid_type',
                'Cisco-IOS-XR-segment-routing-ms-cfg', False),
            _MetaInfoClassMember('absolute-sid', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('15000', '1048575')], [],
                '''                SID value
                ''',
                'absolute_sid',
                'Cisco-IOS-XR-segment-routing-ms-cfg', False, has_when=True),
            _MetaInfoClassMember('index-sid', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('0', '1048575')], [],
                '''                SID value
                ''',
                'index_sid',
                'Cisco-IOS-XR-segment-routing-ms-cfg', False, has_when=True),
            _MetaInfoClassMember('srlb', ATTRIBUTE, 'str', 'Srlb-string',
                None, None,
                [], [b'(srlb_default)'],
                '''                SRLB block name
                ''',
                'srlb',
                'Cisco-IOS-XR-segment-routing-ms-cfg', False, is_mandatory=True, has_when=True),
            ],
            'Cisco-IOS-XR-segment-routing-ms-cfg',
            'l2-adjacency-sid',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-segment-routing-ms-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_segment_routing_ms_cfg',
        ),
    },
    'Sr.AdjacencySid.Interfaces.Interface.AddressFamilies.AddressFamily.NextHops.NextHop' : {
        'meta_info' : _MetaInfoClass('Sr.AdjacencySid.Interfaces.Interface.AddressFamilies.AddressFamily.NextHops.NextHop', REFERENCE_LIST,
            '''Segment Routing Adjacency SID Interface
Address Family NextHop, use a single
ANYADDR (0.0.0.0 or ::) NextHop for point
to point links''',
            False, 
            [
            _MetaInfoClassMember('ip-addr', REFERENCE_UNION, 'str', 'inet:ip-address-no-zone',
                None, None,
                [], [],
                '''                NextHop IP address
                ''',
                'ip_addr',
                'Cisco-IOS-XR-segment-routing-ms-cfg', True, [
                    _MetaInfoClassMember('ip-addr', ATTRIBUTE, 'str', 'inet:ipv4-address-no-zone',
                        None, None,
                        [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'],
                        '''                        NextHop IP address
                        ''',
                        'ip_addr',
                        'Cisco-IOS-XR-segment-routing-ms-cfg', True),
                    _MetaInfoClassMember('ip-addr', ATTRIBUTE, 'str', 'inet:ipv6-address-no-zone',
                        None, None,
                        [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'],
                        '''                        NextHop IP address
                        ''',
                        'ip_addr',
                        'Cisco-IOS-XR-segment-routing-ms-cfg', True),
                ]),
            _MetaInfoClassMember('l2-adjacency-sid', REFERENCE_CLASS, 'L2AdjacencySid', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_segment_routing_ms_cfg', 'Sr.AdjacencySid.Interfaces.Interface.AddressFamilies.AddressFamily.NextHops.NextHop.L2AdjacencySid',
                [], [],
                '''                L2 Adjacency SID type and value
                ''',
                'l2_adjacency_sid',
                'Cisco-IOS-XR-segment-routing-ms-cfg', False),
            ],
            'Cisco-IOS-XR-segment-routing-ms-cfg',
            'next-hop',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-segment-routing-ms-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_segment_routing_ms_cfg',
            has_must=True,
        ),
    },
    'Sr.AdjacencySid.Interfaces.Interface.AddressFamilies.AddressFamily.NextHops' : {
        'meta_info' : _MetaInfoClass('Sr.AdjacencySid.Interfaces.Interface.AddressFamilies.AddressFamily.NextHops', REFERENCE_CLASS,
            '''Segment Routing Adjacency SID Interface
Address Family NextHop Table''',
            False, 
            [
            _MetaInfoClassMember('next-hop', REFERENCE_LIST, 'NextHop', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_segment_routing_ms_cfg', 'Sr.AdjacencySid.Interfaces.Interface.AddressFamilies.AddressFamily.NextHops.NextHop',
                [], [],
                '''                Segment Routing Adjacency SID Interface
                Address Family NextHop, use a single
                ANYADDR (0.0.0.0 or ::) NextHop for point
                to point links
                ''',
                'next_hop',
                'Cisco-IOS-XR-segment-routing-ms-cfg', False, has_must=True),
            ],
            'Cisco-IOS-XR-segment-routing-ms-cfg',
            'next-hops',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-segment-routing-ms-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_segment_routing_ms_cfg',
        ),
    },
    'Sr.AdjacencySid.Interfaces.Interface.AddressFamilies.AddressFamily' : {
        'meta_info' : _MetaInfoClass('Sr.AdjacencySid.Interfaces.Interface.AddressFamilies.AddressFamily', REFERENCE_LIST,
            '''Segment Routing Adjacency SID Interface
Address Family''',
            False, 
            [
            _MetaInfoClassMember('address-family', REFERENCE_ENUM_CLASS, 'SrmsAddressFamily', 'Srms-address-family',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_segment_routing_ms_cfg', 'SrmsAddressFamily',
                [], [],
                '''                Address Family
                ''',
                'address_family',
                'Cisco-IOS-XR-segment-routing-ms-cfg', True),
            _MetaInfoClassMember('next-hops', REFERENCE_CLASS, 'NextHops', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_segment_routing_ms_cfg', 'Sr.AdjacencySid.Interfaces.Interface.AddressFamilies.AddressFamily.NextHops',
                [], [],
                '''                Segment Routing Adjacency SID Interface
                Address Family NextHop Table
                ''',
                'next_hops',
                'Cisco-IOS-XR-segment-routing-ms-cfg', False),
            ],
            'Cisco-IOS-XR-segment-routing-ms-cfg',
            'address-family',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-segment-routing-ms-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_segment_routing_ms_cfg',
        ),
    },
    'Sr.AdjacencySid.Interfaces.Interface.AddressFamilies' : {
        'meta_info' : _MetaInfoClass('Sr.AdjacencySid.Interfaces.Interface.AddressFamilies', REFERENCE_CLASS,
            '''Segment Routing Adjacency SID Interface
Address Family Table''',
            False, 
            [
            _MetaInfoClassMember('address-family', REFERENCE_LIST, 'AddressFamily', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_segment_routing_ms_cfg', 'Sr.AdjacencySid.Interfaces.Interface.AddressFamilies.AddressFamily',
                [], [],
                '''                Segment Routing Adjacency SID Interface
                Address Family
                ''',
                'address_family',
                'Cisco-IOS-XR-segment-routing-ms-cfg', False),
            ],
            'Cisco-IOS-XR-segment-routing-ms-cfg',
            'address-families',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-segment-routing-ms-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_segment_routing_ms_cfg',
        ),
    },
    'Sr.AdjacencySid.Interfaces.Interface' : {
        'meta_info' : _MetaInfoClass('Sr.AdjacencySid.Interfaces.Interface', REFERENCE_LIST,
            '''Segment Routing Adjacency SID Interface''',
            False, 
            [
            _MetaInfoClassMember('interface', ATTRIBUTE, 'str', 'xr:Interface-name',
                None, None,
                [], [b'[a-zA-Z0-9._/-]+'],
                '''                Interface name
                ''',
                'interface',
                'Cisco-IOS-XR-segment-routing-ms-cfg', True),
            _MetaInfoClassMember('address-families', REFERENCE_CLASS, 'AddressFamilies', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_segment_routing_ms_cfg', 'Sr.AdjacencySid.Interfaces.Interface.AddressFamilies',
                [], [],
                '''                Segment Routing Adjacency SID Interface
                Address Family Table
                ''',
                'address_families',
                'Cisco-IOS-XR-segment-routing-ms-cfg', False),
            ],
            'Cisco-IOS-XR-segment-routing-ms-cfg',
            'interface',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-segment-routing-ms-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_segment_routing_ms_cfg',
        ),
    },
    'Sr.AdjacencySid.Interfaces' : {
        'meta_info' : _MetaInfoClass('Sr.AdjacencySid.Interfaces', REFERENCE_CLASS,
            '''Segment Routing Adjacency SID Interface Table''',
            False, 
            [
            _MetaInfoClassMember('interface', REFERENCE_LIST, 'Interface', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_segment_routing_ms_cfg', 'Sr.AdjacencySid.Interfaces.Interface',
                [], [],
                '''                Segment Routing Adjacency SID Interface
                ''',
                'interface',
                'Cisco-IOS-XR-segment-routing-ms-cfg', False),
            ],
            'Cisco-IOS-XR-segment-routing-ms-cfg',
            'interfaces',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-segment-routing-ms-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_segment_routing_ms_cfg',
        ),
    },
    'Sr.AdjacencySid' : {
        'meta_info' : _MetaInfoClass('Sr.AdjacencySid', REFERENCE_CLASS,
            '''Segment Routing Adjacency SID''',
            False, 
            [
            _MetaInfoClassMember('interfaces', REFERENCE_CLASS, 'Interfaces', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_segment_routing_ms_cfg', 'Sr.AdjacencySid.Interfaces',
                [], [],
                '''                Segment Routing Adjacency SID Interface Table
                ''',
                'interfaces',
                'Cisco-IOS-XR-segment-routing-ms-cfg', False),
            ],
            'Cisco-IOS-XR-segment-routing-ms-cfg',
            'adjacency-sid',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-segment-routing-ms-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_segment_routing_ms_cfg',
        ),
    },
    'Sr.GlobalBlock' : {
        'meta_info' : _MetaInfoClass('Sr.GlobalBlock', REFERENCE_CLASS,
            '''Global Block Segment Routing''',
            False, 
            [
            _MetaInfoClassMember('lower-bound', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('16000', '1048574')], [],
                '''                SRGB Lower Bound
                ''',
                'lower_bound',
                'Cisco-IOS-XR-segment-routing-ms-cfg', False, is_mandatory=True),
            _MetaInfoClassMember('upper-bound', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('16001', '1048575')], [],
                '''                SRGB Upper Bound
                ''',
                'upper_bound',
                'Cisco-IOS-XR-segment-routing-ms-cfg', False, is_mandatory=True),
            ],
            'Cisco-IOS-XR-segment-routing-ms-cfg',
            'global-block',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-segment-routing-ms-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_segment_routing_ms_cfg',
            is_presence=True,
        ),
    },
    'Sr.Srv6.Logging' : {
        'meta_info' : _MetaInfoClass('Sr.Srv6.Logging', REFERENCE_CLASS,
            '''Enable logging''',
            False, 
            [
            _MetaInfoClassMember('locator-status', ATTRIBUTE, 'Empty', 'empty',
                None, None,
                [], [],
                '''                Enable logging for locator status changes
                ''',
                'locator_status',
                'Cisco-IOS-XR-segment-routing-srv6-cfg', False),
            ],
            'Cisco-IOS-XR-segment-routing-srv6-cfg',
            'logging',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-segment-routing-srv6-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_segment_routing_ms_cfg',
        ),
    },
    'Sr.Srv6.Locators.Locators_.Locator.Prefix' : {
        'meta_info' : _MetaInfoClass('Sr.Srv6.Locators.Locators_.Locator.Prefix', REFERENCE_CLASS,
            '''Specify locator prefix value''',
            False, 
            [
            _MetaInfoClassMember('prefix', REFERENCE_UNION, 'str', 'inet:ip-address-no-zone',
                None, None,
                [], [],
                '''                IPv6 Prefix
                ''',
                'prefix',
                'Cisco-IOS-XR-segment-routing-srv6-cfg', False, [
                    _MetaInfoClassMember('prefix', ATTRIBUTE, 'str', 'inet:ipv4-address-no-zone',
                        None, None,
                        [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'],
                        '''                        IPv6 Prefix
                        ''',
                        'prefix',
                        'Cisco-IOS-XR-segment-routing-srv6-cfg', False),
                    _MetaInfoClassMember('prefix', ATTRIBUTE, 'str', 'inet:ipv6-address-no-zone',
                        None, None,
                        [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'],
                        '''                        IPv6 Prefix
                        ''',
                        'prefix',
                        'Cisco-IOS-XR-segment-routing-srv6-cfg', False),
                ]),
            _MetaInfoClassMember('prefix-length', ATTRIBUTE, 'int', 'dt1:Srv6-locator-len',
                None, None,
                [('32', '112')], [],
                '''                Prefix length
                ''',
                'prefix_length',
                'Cisco-IOS-XR-segment-routing-srv6-cfg', False),
            ],
            'Cisco-IOS-XR-segment-routing-srv6-cfg',
            'prefix',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-segment-routing-srv6-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_segment_routing_ms_cfg',
        ),
    },
    'Sr.Srv6.Locators.Locators_.Locator' : {
        'meta_info' : _MetaInfoClass('Sr.Srv6.Locators.Locators_.Locator', REFERENCE_LIST,
            '''Configure a SRv6 locator''',
            False, 
            [
            _MetaInfoClassMember('name', ATTRIBUTE, 'str', 'dt1:Srv6-locator-name',
                None, None,
                [(1, 58)], [],
                '''                Locator name
                ''',
                'name',
                'Cisco-IOS-XR-segment-routing-srv6-cfg', True),
            _MetaInfoClassMember('prefix', REFERENCE_CLASS, 'Prefix', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_segment_routing_ms_cfg', 'Sr.Srv6.Locators.Locators_.Locator.Prefix',
                [], [],
                '''                Specify locator prefix value
                ''',
                'prefix',
                'Cisco-IOS-XR-segment-routing-srv6-cfg', False),
            _MetaInfoClassMember('locator-enable', ATTRIBUTE, 'Empty', 'empty',
                None, None,
                [], [],
                '''                Enable a SRv6 locator
                ''',
                'locator_enable',
                'Cisco-IOS-XR-segment-routing-srv6-cfg', False),
            ],
            'Cisco-IOS-XR-segment-routing-srv6-cfg',
            'locator',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-segment-routing-srv6-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_segment_routing_ms_cfg',
        ),
    },
    'Sr.Srv6.Locators.Locators_' : {
        'meta_info' : _MetaInfoClass('Sr.Srv6.Locators.Locators_', REFERENCE_CLASS,
            '''Configure SRv6 table of locators''',
            False, 
            [
            _MetaInfoClassMember('locator', REFERENCE_LIST, 'Locator', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_segment_routing_ms_cfg', 'Sr.Srv6.Locators.Locators_.Locator',
                [], [],
                '''                Configure a SRv6 locator
                ''',
                'locator',
                'Cisco-IOS-XR-segment-routing-srv6-cfg', False),
            ],
            'Cisco-IOS-XR-segment-routing-srv6-cfg',
            'locators',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-segment-routing-srv6-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_segment_routing_ms_cfg',
        ),
    },
    'Sr.Srv6.Locators' : {
        'meta_info' : _MetaInfoClass('Sr.Srv6.Locators', REFERENCE_CLASS,
            '''Configure SRv6 locators parameters''',
            False, 
            [
            _MetaInfoClassMember('locators', REFERENCE_CLASS, 'Locators_', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_segment_routing_ms_cfg', 'Sr.Srv6.Locators.Locators_',
                [], [],
                '''                Configure SRv6 table of locators
                ''',
                'locators',
                'Cisco-IOS-XR-segment-routing-srv6-cfg', False),
            ],
            'Cisco-IOS-XR-segment-routing-srv6-cfg',
            'locators',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-segment-routing-srv6-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_segment_routing_ms_cfg',
        ),
    },
    'Sr.Srv6.Encapsulation.HopLimit' : {
        'meta_info' : _MetaInfoClass('Sr.Srv6.Encapsulation.HopLimit', REFERENCE_CLASS,
            '''Configure IPv6 Hop-Limit options''',
            False, 
            [
            _MetaInfoClassMember('option', REFERENCE_ENUM_CLASS, 'Srv6EncapsulationHopLimitOption', 'dt1:Srv6-encapsulation-hop-limit-option',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_segment_routing_srv6_datatypes', 'Srv6EncapsulationHopLimitOption',
                [], [],
                '''                Hop-Limit config option
                ''',
                'option',
                'Cisco-IOS-XR-segment-routing-srv6-cfg', False),
            _MetaInfoClassMember('value', ATTRIBUTE, 'int', 'dt1:Srv6-encapsulation-hop-limit-value',
                None, None,
                [('1', '255')], [],
                '''                Count for Hop-limit
                ''',
                'value',
                'Cisco-IOS-XR-segment-routing-srv6-cfg', False, has_when=True),
            ],
            'Cisco-IOS-XR-segment-routing-srv6-cfg',
            'hop-limit',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-segment-routing-srv6-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_segment_routing_ms_cfg',
        ),
    },
    'Sr.Srv6.Encapsulation' : {
        'meta_info' : _MetaInfoClass('Sr.Srv6.Encapsulation', REFERENCE_CLASS,
            '''Configure encapsulation related parameters''',
            False, 
            [
            _MetaInfoClassMember('hop-limit', REFERENCE_CLASS, 'HopLimit', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_segment_routing_ms_cfg', 'Sr.Srv6.Encapsulation.HopLimit',
                [], [],
                '''                Configure IPv6 Hop-Limit options
                ''',
                'hop_limit',
                'Cisco-IOS-XR-segment-routing-srv6-cfg', False),
            _MetaInfoClassMember('source-address', REFERENCE_UNION, 'str', 'inet:ip-address-no-zone',
                None, None,
                [], [],
                '''                Configure a source address
                ''',
                'source_address',
                'Cisco-IOS-XR-segment-routing-srv6-cfg', False, [
                    _MetaInfoClassMember('source-address', ATTRIBUTE, 'str', 'inet:ipv4-address-no-zone',
                        None, None,
                        [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'],
                        '''                        Configure a source address
                        ''',
                        'source_address',
                        'Cisco-IOS-XR-segment-routing-srv6-cfg', False),
                    _MetaInfoClassMember('source-address', ATTRIBUTE, 'str', 'inet:ipv6-address-no-zone',
                        None, None,
                        [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'],
                        '''                        Configure a source address
                        ''',
                        'source_address',
                        'Cisco-IOS-XR-segment-routing-srv6-cfg', False),
                ]),
            ],
            'Cisco-IOS-XR-segment-routing-srv6-cfg',
            'encapsulation',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-segment-routing-srv6-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_segment_routing_ms_cfg',
        ),
    },
    'Sr.Srv6' : {
        'meta_info' : _MetaInfoClass('Sr.Srv6', REFERENCE_CLASS,
            '''Segment Routing with IPv6 dataplane''',
            False, 
            [
            _MetaInfoClassMember('logging', REFERENCE_CLASS, 'Logging', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_segment_routing_ms_cfg', 'Sr.Srv6.Logging',
                [], [],
                '''                Enable logging
                ''',
                'logging',
                'Cisco-IOS-XR-segment-routing-srv6-cfg', False),
            _MetaInfoClassMember('locators', REFERENCE_CLASS, 'Locators', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_segment_routing_ms_cfg', 'Sr.Srv6.Locators',
                [], [],
                '''                Configure SRv6 locators parameters
                ''',
                'locators',
                'Cisco-IOS-XR-segment-routing-srv6-cfg', False),
            _MetaInfoClassMember('encapsulation', REFERENCE_CLASS, 'Encapsulation', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_segment_routing_ms_cfg', 'Sr.Srv6.Encapsulation',
                [], [],
                '''                Configure encapsulation related parameters
                ''',
                'encapsulation',
                'Cisco-IOS-XR-segment-routing-srv6-cfg', False),
            _MetaInfoClassMember('enable', ATTRIBUTE, 'Empty', 'empty',
                None, None,
                [], [],
                '''                Enable SRv6
                ''',
                'enable',
                'Cisco-IOS-XR-segment-routing-srv6-cfg', False),
            _MetaInfoClassMember('sid-holdtime', ATTRIBUTE, 'int', 'dt1:Srv6sid-holdtime',
                None, None,
                [('0', '60')], [],
                '''                Configure SID holdtime for a stale/freed SID
                ''',
                'sid_holdtime',
                'Cisco-IOS-XR-segment-routing-srv6-cfg', False),
            ],
            'Cisco-IOS-XR-segment-routing-srv6-cfg',
            'srv6',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-segment-routing-srv6-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_segment_routing_ms_cfg',
        ),
    },
    'Sr.TrafficEngineering.OutOfResources' : {
        'meta_info' : _MetaInfoClass('Sr.TrafficEngineering.OutOfResources', REFERENCE_CLASS,
            '''SR-TE out-of-resources handling configuration''',
            False, 
            [
            _MetaInfoClassMember('maximum-paths-batch', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('0', '4294967295')], [],
                '''                Maximum total number of LSP path operations in
                a single batch
                ''',
                'maximum_paths_batch',
                'Cisco-IOS-XR-infra-xtc-agent-cfg', False, default_value="0"),
            _MetaInfoClassMember('maximum-paths', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('0', '4294967295')], [],
                '''                Maximum total number of LSP paths that can be
                created
                ''',
                'maximum_paths',
                'Cisco-IOS-XR-infra-xtc-agent-cfg', False, default_value="0"),
            ],
            'Cisco-IOS-XR-infra-xtc-agent-cfg',
            'out-of-resources',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-infra-xtc-agent-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_segment_routing_ms_cfg',
        ),
    },
    'Sr.TrafficEngineering.OnDemandColors.OnDemandColor.OnDemandColorDynMpls.OnDemandColorDynMplsMetric.MetricMargin' : {
        'meta_info' : _MetaInfoClass('Sr.TrafficEngineering.OnDemandColors.OnDemandColor.OnDemandColorDynMpls.OnDemandColorDynMplsMetric.MetricMargin', REFERENCE_CLASS,
            '''Metric Margin''',
            False, 
            [
            _MetaInfoClassMember('value-type', REFERENCE_ENUM_CLASS, 'XtcMetricValue', 'Xtc-metric-value',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_agent_cfg', 'XtcMetricValue',
                [], [],
                '''                Metric margin type
                ''',
                'value_type',
                'Cisco-IOS-XR-infra-xtc-agent-cfg', False),
            _MetaInfoClassMember('absolute-value', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('0', '2147483647')], [],
                '''                Absolute metric value
                ''',
                'absolute_value',
                'Cisco-IOS-XR-infra-xtc-agent-cfg', False, has_when=True),
            _MetaInfoClassMember('relative-value', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('0', '2147483647')], [],
                '''                Relative metric value
                ''',
                'relative_value',
                'Cisco-IOS-XR-infra-xtc-agent-cfg', False, has_when=True),
            ],
            'Cisco-IOS-XR-infra-xtc-agent-cfg',
            'metric-margin',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-infra-xtc-agent-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_segment_routing_ms_cfg',
        ),
    },
    'Sr.TrafficEngineering.OnDemandColors.OnDemandColor.OnDemandColorDynMpls.OnDemandColorDynMplsMetric' : {
        'meta_info' : _MetaInfoClass('Sr.TrafficEngineering.OnDemandColors.OnDemandColor.OnDemandColorDynMpls.OnDemandColorDynMplsMetric', REFERENCE_CLASS,
            '''Metric type''',
            False, 
            [
            _MetaInfoClassMember('metric-type', REFERENCE_ENUM_CLASS, 'XtcMetric', 'Xtc-metric',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_agent_cfg', 'XtcMetric',
                [], [],
                '''                Metric Type
                ''',
                'metric_type',
                'Cisco-IOS-XR-infra-xtc-agent-cfg', False),
            _MetaInfoClassMember('enable', ATTRIBUTE, 'Empty', 'empty',
                None, None,
                [], [],
                '''                Metric submode Enable
                ''',
                'enable',
                'Cisco-IOS-XR-infra-xtc-agent-cfg', False),
            _MetaInfoClassMember('metric-margin', REFERENCE_CLASS, 'MetricMargin', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_segment_routing_ms_cfg', 'Sr.TrafficEngineering.OnDemandColors.OnDemandColor.OnDemandColorDynMpls.OnDemandColorDynMplsMetric.MetricMargin',
                [], [],
                '''                Metric Margin
                ''',
                'metric_margin',
                'Cisco-IOS-XR-infra-xtc-agent-cfg', False),
            ],
            'Cisco-IOS-XR-infra-xtc-agent-cfg',
            'on-demand-color-dyn-mpls-metric',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-infra-xtc-agent-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_segment_routing_ms_cfg',
        ),
    },
    'Sr.TrafficEngineering.OnDemandColors.OnDemandColor.OnDemandColorDynMpls.OnDemandColorDynMplsPce' : {
        'meta_info' : _MetaInfoClass('Sr.TrafficEngineering.OnDemandColors.OnDemandColor.OnDemandColorDynMpls.OnDemandColorDynMplsPce', REFERENCE_CLASS,
            '''Use Path Computation Element''',
            False, 
            [
            _MetaInfoClassMember('enable', ATTRIBUTE, 'Empty', 'empty',
                None, None,
                [], [],
                '''                PCE submode Enable
                ''',
                'enable',
                'Cisco-IOS-XR-infra-xtc-agent-cfg', False),
            ],
            'Cisco-IOS-XR-infra-xtc-agent-cfg',
            'on-demand-color-dyn-mpls-pce',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-infra-xtc-agent-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_segment_routing_ms_cfg',
        ),
    },
    'Sr.TrafficEngineering.OnDemandColors.OnDemandColor.OnDemandColorDynMpls.DisjointPath' : {
        'meta_info' : _MetaInfoClass('Sr.TrafficEngineering.OnDemandColors.OnDemandColor.OnDemandColorDynMpls.DisjointPath', REFERENCE_CLASS,
            '''Disjoint path''',
            False, 
            [
            _MetaInfoClassMember('group-id', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('1', '65535')], [],
                '''                Group ID
                ''',
                'group_id',
                'Cisco-IOS-XR-infra-xtc-agent-cfg', False, is_mandatory=True),
            _MetaInfoClassMember('disjointness-type', REFERENCE_ENUM_CLASS, 'XtcDisjointness', 'Xtc-disjointness',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_agent_cfg', 'XtcDisjointness',
                [], [],
                '''                Disjointness Type
                ''',
                'disjointness_type',
                'Cisco-IOS-XR-infra-xtc-agent-cfg', False, is_mandatory=True),
            _MetaInfoClassMember('sub-id', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('1', '65535')], [],
                '''                Sub ID
                ''',
                'sub_id',
                'Cisco-IOS-XR-infra-xtc-agent-cfg', False),
            ],
            'Cisco-IOS-XR-infra-xtc-agent-cfg',
            'disjoint-path',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-infra-xtc-agent-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_segment_routing_ms_cfg',
            is_presence=True,
        ),
    },
    'Sr.TrafficEngineering.OnDemandColors.OnDemandColor.OnDemandColorDynMpls.AffinityRules.AffinityRule.AffinityName' : {
        'meta_info' : _MetaInfoClass('Sr.TrafficEngineering.OnDemandColors.OnDemandColor.OnDemandColorDynMpls.AffinityRules.AffinityRule.AffinityName', REFERENCE_LIST,
            '''Affinity rule name''',
            False, 
            [
            _MetaInfoClassMember('affinity-name', ATTRIBUTE, 'str', 'xr:Cisco-ios-xr-string',
                None, None,
                [(1, 32)], [],
                '''                Affinity name
                ''',
                'affinity_name',
                'Cisco-IOS-XR-infra-xtc-agent-cfg', True),
            ],
            'Cisco-IOS-XR-infra-xtc-agent-cfg',
            'affinity-name',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-infra-xtc-agent-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_segment_routing_ms_cfg',
        ),
    },
    'Sr.TrafficEngineering.OnDemandColors.OnDemandColor.OnDemandColorDynMpls.AffinityRules.AffinityRule' : {
        'meta_info' : _MetaInfoClass('Sr.TrafficEngineering.OnDemandColors.OnDemandColor.OnDemandColorDynMpls.AffinityRules.AffinityRule', REFERENCE_LIST,
            '''SR path computation and verification affinity
rule''',
            False, 
            [
            _MetaInfoClassMember('rule', REFERENCE_ENUM_CLASS, 'XtcAffinityRule', 'Xtc-affinity-rule',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_agent_cfg', 'XtcAffinityRule',
                [], [],
                '''                Affinity rule type
                ''',
                'rule',
                'Cisco-IOS-XR-infra-xtc-agent-cfg', True),
            _MetaInfoClassMember('affinity-name', REFERENCE_LIST, 'AffinityName', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_segment_routing_ms_cfg', 'Sr.TrafficEngineering.OnDemandColors.OnDemandColor.OnDemandColorDynMpls.AffinityRules.AffinityRule.AffinityName',
                [], [],
                '''                Affinity rule name
                ''',
                'affinity_name',
                'Cisco-IOS-XR-infra-xtc-agent-cfg', False),
            ],
            'Cisco-IOS-XR-infra-xtc-agent-cfg',
            'affinity-rule',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-infra-xtc-agent-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_segment_routing_ms_cfg',
        ),
    },
    'Sr.TrafficEngineering.OnDemandColors.OnDemandColor.OnDemandColorDynMpls.AffinityRules' : {
        'meta_info' : _MetaInfoClass('Sr.TrafficEngineering.OnDemandColors.OnDemandColor.OnDemandColorDynMpls.AffinityRules', REFERENCE_CLASS,
            '''SR path computation and verification affinity
rules''',
            False, 
            [
            _MetaInfoClassMember('affinity-rule', REFERENCE_LIST, 'AffinityRule', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_segment_routing_ms_cfg', 'Sr.TrafficEngineering.OnDemandColors.OnDemandColor.OnDemandColorDynMpls.AffinityRules.AffinityRule',
                [], [],
                '''                SR path computation and verification affinity
                rule
                ''',
                'affinity_rule',
                'Cisco-IOS-XR-infra-xtc-agent-cfg', False),
            ],
            'Cisco-IOS-XR-infra-xtc-agent-cfg',
            'affinity-rules',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-infra-xtc-agent-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_segment_routing_ms_cfg',
        ),
    },
    'Sr.TrafficEngineering.OnDemandColors.OnDemandColor.OnDemandColorDynMpls' : {
        'meta_info' : _MetaInfoClass('Sr.TrafficEngineering.OnDemandColors.OnDemandColor.OnDemandColorDynMpls', REFERENCE_CLASS,
            '''Dynamic MPLS path properties''',
            False, 
            [
            _MetaInfoClassMember('on-demand-color-dyn-mpls-metric', REFERENCE_CLASS, 'OnDemandColorDynMplsMetric', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_segment_routing_ms_cfg', 'Sr.TrafficEngineering.OnDemandColors.OnDemandColor.OnDemandColorDynMpls.OnDemandColorDynMplsMetric',
                [], [],
                '''                Metric type
                ''',
                'on_demand_color_dyn_mpls_metric',
                'Cisco-IOS-XR-infra-xtc-agent-cfg', False),
            _MetaInfoClassMember('on-demand-color-dyn-mpls-pce', REFERENCE_CLASS, 'OnDemandColorDynMplsPce', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_segment_routing_ms_cfg', 'Sr.TrafficEngineering.OnDemandColors.OnDemandColor.OnDemandColorDynMpls.OnDemandColorDynMplsPce',
                [], [],
                '''                Use Path Computation Element
                ''',
                'on_demand_color_dyn_mpls_pce',
                'Cisco-IOS-XR-infra-xtc-agent-cfg', False),
            _MetaInfoClassMember('disjoint-path', REFERENCE_CLASS, 'DisjointPath', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_segment_routing_ms_cfg', 'Sr.TrafficEngineering.OnDemandColors.OnDemandColor.OnDemandColorDynMpls.DisjointPath',
                [], [],
                '''                Disjoint path
                ''',
                'disjoint_path',
                'Cisco-IOS-XR-infra-xtc-agent-cfg', False, is_presence=True),
            _MetaInfoClassMember('on-demand-color-dyn-mpls-flex-algorithm', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('128', '255')], [],
                '''                Prefix-SID algorithm
                ''',
                'on_demand_color_dyn_mpls_flex_algorithm',
                'Cisco-IOS-XR-infra-xtc-agent-cfg', False),
            _MetaInfoClassMember('enable', ATTRIBUTE, 'Empty', 'empty',
                None, None,
                [], [],
                '''                Dynamic MPLS path properties submode Enable
                ''',
                'enable',
                'Cisco-IOS-XR-infra-xtc-agent-cfg', False),
            _MetaInfoClassMember('affinity-rules', REFERENCE_CLASS, 'AffinityRules', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_segment_routing_ms_cfg', 'Sr.TrafficEngineering.OnDemandColors.OnDemandColor.OnDemandColorDynMpls.AffinityRules',
                [], [],
                '''                SR path computation and verification affinity
                rules
                ''',
                'affinity_rules',
                'Cisco-IOS-XR-infra-xtc-agent-cfg', False),
            ],
            'Cisco-IOS-XR-infra-xtc-agent-cfg',
            'on-demand-color-dyn-mpls',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-infra-xtc-agent-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_segment_routing_ms_cfg',
        ),
    },
    'Sr.TrafficEngineering.OnDemandColors.OnDemandColor.SourceAddress' : {
        'meta_info' : _MetaInfoClass('Sr.TrafficEngineering.OnDemandColors.OnDemandColor.SourceAddress', REFERENCE_CLASS,
            '''Source address of a candidate path. EndPointType
, Source''',
            False, 
            [
            _MetaInfoClassMember('ip-address-type', REFERENCE_ENUM_CLASS, 'XtcEndPoint', 'Xtc-end-point',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_agent_cfg', 'XtcEndPoint',
                [], [],
                '''                IP address type
                ''',
                'ip_address_type',
                'Cisco-IOS-XR-infra-xtc-agent-cfg', False, is_mandatory=True),
            _MetaInfoClassMember('source-address', REFERENCE_UNION, 'str', 'inet:ip-address-no-zone',
                None, None,
                [], [],
                '''                Source address
                ''',
                'source_address',
                'Cisco-IOS-XR-infra-xtc-agent-cfg', False, [
                    _MetaInfoClassMember('source-address', ATTRIBUTE, 'str', 'inet:ipv4-address-no-zone',
                        None, None,
                        [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'],
                        '''                        Source address
                        ''',
                        'source_address',
                        'Cisco-IOS-XR-infra-xtc-agent-cfg', False, is_mandatory=True),
                    _MetaInfoClassMember('source-address', ATTRIBUTE, 'str', 'inet:ipv6-address-no-zone',
                        None, None,
                        [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'],
                        '''                        Source address
                        ''',
                        'source_address',
                        'Cisco-IOS-XR-infra-xtc-agent-cfg', False, is_mandatory=True),
                ], is_mandatory=True),
            ],
            'Cisco-IOS-XR-infra-xtc-agent-cfg',
            'source-address',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-infra-xtc-agent-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_segment_routing_ms_cfg',
            is_presence=True,
        ),
    },
    'Sr.TrafficEngineering.OnDemandColors.OnDemandColor' : {
        'meta_info' : _MetaInfoClass('Sr.TrafficEngineering.OnDemandColors.OnDemandColor', REFERENCE_LIST,
            '''On-demand color configuration''',
            False, 
            [
            _MetaInfoClassMember('color', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('1', '4294967295')], [],
                '''                Color
                ''',
                'color',
                'Cisco-IOS-XR-infra-xtc-agent-cfg', True),
            _MetaInfoClassMember('on-demand-color-dyn-mpls', REFERENCE_CLASS, 'OnDemandColorDynMpls', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_segment_routing_ms_cfg', 'Sr.TrafficEngineering.OnDemandColors.OnDemandColor.OnDemandColorDynMpls',
                [], [],
                '''                Dynamic MPLS path properties
                ''',
                'on_demand_color_dyn_mpls',
                'Cisco-IOS-XR-infra-xtc-agent-cfg', False),
            _MetaInfoClassMember('bandwidth', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('1', '4294967295')], [],
                '''                The value of the bandwidth reserved by this
                policy in kbps
                ''',
                'bandwidth',
                'Cisco-IOS-XR-infra-xtc-agent-cfg', False),
            _MetaInfoClassMember('maximum-sid-depth', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('1', '255')], [],
                '''                Maximum SID Depth Configuration
                ''',
                'maximum_sid_depth',
                'Cisco-IOS-XR-infra-xtc-agent-cfg', False),
            _MetaInfoClassMember('source-address', REFERENCE_CLASS, 'SourceAddress', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_segment_routing_ms_cfg', 'Sr.TrafficEngineering.OnDemandColors.OnDemandColor.SourceAddress',
                [], [],
                '''                Source address of a candidate path. EndPointType
                , Source
                ''',
                'source_address',
                'Cisco-IOS-XR-infra-xtc-agent-cfg', False, is_presence=True),
            _MetaInfoClassMember('enable', ATTRIBUTE, 'Empty', 'empty',
                None, None,
                [], [],
                '''                True only
                ''',
                'enable',
                'Cisco-IOS-XR-infra-xtc-agent-cfg', False),
            ],
            'Cisco-IOS-XR-infra-xtc-agent-cfg',
            'on-demand-color',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-infra-xtc-agent-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_segment_routing_ms_cfg',
        ),
    },
    'Sr.TrafficEngineering.OnDemandColors' : {
        'meta_info' : _MetaInfoClass('Sr.TrafficEngineering.OnDemandColors', REFERENCE_CLASS,
            '''On-demand color configuration''',
            False, 
            [
            _MetaInfoClassMember('on-demand-color', REFERENCE_LIST, 'OnDemandColor', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_segment_routing_ms_cfg', 'Sr.TrafficEngineering.OnDemandColors.OnDemandColor',
                [], [],
                '''                On-demand color configuration
                ''',
                'on_demand_color',
                'Cisco-IOS-XR-infra-xtc-agent-cfg', False),
            ],
            'Cisco-IOS-XR-infra-xtc-agent-cfg',
            'on-demand-colors',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-infra-xtc-agent-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_segment_routing_ms_cfg',
        ),
    },
    'Sr.TrafficEngineering.Segments.Segment.Segments_.Segment_' : {
        'meta_info' : _MetaInfoClass('Sr.TrafficEngineering.Segments.Segment.Segments_.Segment_', REFERENCE_LIST,
            '''Configure Segment/hop at the index''',
            False, 
            [
            _MetaInfoClassMember('segment-index', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('1', '65535')], [],
                '''                Segment index
                ''',
                'segment_index',
                'Cisco-IOS-XR-infra-xtc-agent-cfg', True),
            _MetaInfoClassMember('segment-type', REFERENCE_ENUM_CLASS, 'XtcSegment', 'Xtc-segment',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_agent_cfg', 'XtcSegment',
                [], [],
                '''                Segment/hop type
                ''',
                'segment_type',
                'Cisco-IOS-XR-infra-xtc-agent-cfg', False),
            _MetaInfoClassMember('address', ATTRIBUTE, 'str', 'inet:ipv4-address-no-zone',
                None, None,
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'],
                '''                IPv4 Address
                ''',
                'address',
                'Cisco-IOS-XR-infra-xtc-agent-cfg', False, has_when=True),
            _MetaInfoClassMember('mpls-label', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('0', '1048575')], [],
                '''                MPLS Label
                ''',
                'mpls_label',
                'Cisco-IOS-XR-infra-xtc-agent-cfg', False, has_when=True),
            ],
            'Cisco-IOS-XR-infra-xtc-agent-cfg',
            'segment',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-infra-xtc-agent-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_segment_routing_ms_cfg',
        ),
    },
    'Sr.TrafficEngineering.Segments.Segment.Segments_' : {
        'meta_info' : _MetaInfoClass('Sr.TrafficEngineering.Segments.Segment.Segments_', REFERENCE_CLASS,
            '''Segments/hops configuration for given
Segment-list''',
            False, 
            [
            _MetaInfoClassMember('segment', REFERENCE_LIST, 'Segment_', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_segment_routing_ms_cfg', 'Sr.TrafficEngineering.Segments.Segment.Segments_.Segment_',
                [], [],
                '''                Configure Segment/hop at the index
                ''',
                'segment',
                'Cisco-IOS-XR-infra-xtc-agent-cfg', False),
            ],
            'Cisco-IOS-XR-infra-xtc-agent-cfg',
            'segments',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-infra-xtc-agent-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_segment_routing_ms_cfg',
        ),
    },
    'Sr.TrafficEngineering.Segments.Segment' : {
        'meta_info' : _MetaInfoClass('Sr.TrafficEngineering.Segments.Segment', REFERENCE_LIST,
            '''Segment-list configuration''',
            False, 
            [
            _MetaInfoClassMember('path-name', ATTRIBUTE, 'str', 'xr:Cisco-ios-xr-string',
                None, None,
                [(1, 128)], [],
                '''                Segment-list name
                ''',
                'path_name',
                'Cisco-IOS-XR-infra-xtc-agent-cfg', True),
            _MetaInfoClassMember('segments', REFERENCE_CLASS, 'Segments_', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_segment_routing_ms_cfg', 'Sr.TrafficEngineering.Segments.Segment.Segments_',
                [], [],
                '''                Segments/hops configuration for given
                Segment-list
                ''',
                'segments',
                'Cisco-IOS-XR-infra-xtc-agent-cfg', False),
            _MetaInfoClassMember('enable', ATTRIBUTE, 'Empty', 'empty',
                None, None,
                [], [],
                '''                True only
                ''',
                'enable',
                'Cisco-IOS-XR-infra-xtc-agent-cfg', False),
            ],
            'Cisco-IOS-XR-infra-xtc-agent-cfg',
            'segment',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-infra-xtc-agent-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_segment_routing_ms_cfg',
        ),
    },
    'Sr.TrafficEngineering.Segments' : {
        'meta_info' : _MetaInfoClass('Sr.TrafficEngineering.Segments', REFERENCE_CLASS,
            '''Segment-lists configuration''',
            False, 
            [
            _MetaInfoClassMember('segment', REFERENCE_LIST, 'Segment', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_segment_routing_ms_cfg', 'Sr.TrafficEngineering.Segments.Segment',
                [], [],
                '''                Segment-list configuration
                ''',
                'segment',
                'Cisco-IOS-XR-infra-xtc-agent-cfg', False),
            ],
            'Cisco-IOS-XR-infra-xtc-agent-cfg',
            'segments',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-infra-xtc-agent-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_segment_routing_ms_cfg',
        ),
    },
    'Sr.TrafficEngineering.Logging' : {
        'meta_info' : _MetaInfoClass('Sr.TrafficEngineering.Logging', REFERENCE_CLASS,
            '''Logging configuration''',
            False, 
            [
            _MetaInfoClassMember('pcep-peer-status', ATTRIBUTE, 'Empty', 'empty',
                None, None,
                [], [],
                '''                Enable logging for pcep peer status
                ''',
                'pcep_peer_status',
                'Cisco-IOS-XR-infra-xtc-agent-cfg', False),
            _MetaInfoClassMember('policy-status', ATTRIBUTE, 'Empty', 'empty',
                None, None,
                [], [],
                '''                Enable logging for policy status
                ''',
                'policy_status',
                'Cisco-IOS-XR-infra-xtc-agent-cfg', False),
            ],
            'Cisco-IOS-XR-infra-xtc-agent-cfg',
            'logging',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-infra-xtc-agent-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_segment_routing_ms_cfg',
        ),
    },
    'Sr.TrafficEngineering.Timers' : {
        'meta_info' : _MetaInfoClass('Sr.TrafficEngineering.Timers', REFERENCE_CLASS,
            '''SR-TE timers configuration''',
            False, 
            [
            _MetaInfoClassMember('candidate-path-cleanup-delay', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('0', '86400')], [],
                '''                Delay before cleaning up candidate paths
                ''',
                'candidate_path_cleanup_delay',
                'Cisco-IOS-XR-infra-xtc-agent-cfg', False, default_value="120"),
            _MetaInfoClassMember('initial-verify-restart', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('10', '10000')], [],
                '''                Timer to wait for topology convergence after
                topology starts populating for restart case
                ''',
                'initial_verify_restart',
                'Cisco-IOS-XR-infra-xtc-agent-cfg', False, default_value="40"),
            _MetaInfoClassMember('initial-verify-switchover', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('10', '10000')], [],
                '''                Timer to wait for topology convergence after
                topology starts populating for switchover case
                ''',
                'initial_verify_switchover',
                'Cisco-IOS-XR-infra-xtc-agent-cfg', False, default_value="60"),
            _MetaInfoClassMember('initial-verify-startup', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('10', '10000')], [],
                '''                Timer to wait for topology convergence after
                topology starts populating for startup case
                ''',
                'initial_verify_startup',
                'Cisco-IOS-XR-infra-xtc-agent-cfg', False, default_value="300"),
            _MetaInfoClassMember('cleanup-delay', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('0', '300')], [],
                '''                Delay before cleaning up previous path
                ''',
                'cleanup_delay',
                'Cisco-IOS-XR-infra-xtc-agent-cfg', False, default_value="10"),
            _MetaInfoClassMember('install-delay', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('0', '300')], [],
                '''                Delay before switching to a reoptimized path
                ''',
                'install_delay',
                'Cisco-IOS-XR-infra-xtc-agent-cfg', False, default_value="10"),
            _MetaInfoClassMember('periodic-reoptimization', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('0', '86400')], [],
                '''                How often to perform periodic reoptimization
                of policies
                ''',
                'periodic_reoptimization',
                'Cisco-IOS-XR-infra-xtc-agent-cfg', False, default_value="600"),
            ],
            'Cisco-IOS-XR-infra-xtc-agent-cfg',
            'timers',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-infra-xtc-agent-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_segment_routing_ms_cfg',
        ),
    },
    'Sr.TrafficEngineering.BindingSidRules.Explicit' : {
        'meta_info' : _MetaInfoClass('Sr.TrafficEngineering.BindingSidRules.Explicit', REFERENCE_CLASS,
            '''Binding sid explicit options''',
            False, 
            [
            _MetaInfoClassMember('rule', REFERENCE_ENUM_CLASS, 'XtcBindingSidexplicitRule', 'Xtc-binding-sidexplicit-rule',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_agent_cfg', 'XtcBindingSidexplicitRule',
                [], [],
                '''                Binding sid explicit rule
                ''',
                'rule',
                'Cisco-IOS-XR-infra-xtc-agent-cfg', False, is_mandatory=True),
            ],
            'Cisco-IOS-XR-infra-xtc-agent-cfg',
            'explicit',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-infra-xtc-agent-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_segment_routing_ms_cfg',
            is_presence=True,
        ),
    },
    'Sr.TrafficEngineering.BindingSidRules.DynamicBindingSidRules' : {
        'meta_info' : _MetaInfoClass('Sr.TrafficEngineering.BindingSidRules.DynamicBindingSidRules', REFERENCE_CLASS,
            '''Dynamic binding SID options''',
            False, 
            [
            _MetaInfoClassMember('dynamic-binding-sid-rule', REFERENCE_ENUM_CLASS, 'XtcBindingSidDynamicRule', 'Xtc-binding-sid-dynamic-rule',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_agent_cfg', 'XtcBindingSidDynamicRule',
                [], [],
                '''                Binding SID dynamic rule
                ''',
                'dynamic_binding_sid_rule',
                'Cisco-IOS-XR-infra-xtc-agent-cfg', False, is_mandatory=True),
            ],
            'Cisco-IOS-XR-infra-xtc-agent-cfg',
            'dynamic-binding-sid-rules',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-infra-xtc-agent-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_segment_routing_ms_cfg',
            is_presence=True,
        ),
    },
    'Sr.TrafficEngineering.BindingSidRules' : {
        'meta_info' : _MetaInfoClass('Sr.TrafficEngineering.BindingSidRules', REFERENCE_CLASS,
            '''Binding sid rules''',
            False, 
            [
            _MetaInfoClassMember('explicit', REFERENCE_CLASS, 'Explicit', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_segment_routing_ms_cfg', 'Sr.TrafficEngineering.BindingSidRules.Explicit',
                [], [],
                '''                Binding sid explicit options
                ''',
                'explicit',
                'Cisco-IOS-XR-infra-xtc-agent-cfg', False, is_presence=True),
            _MetaInfoClassMember('dynamic-binding-sid-rules', REFERENCE_CLASS, 'DynamicBindingSidRules', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_segment_routing_ms_cfg', 'Sr.TrafficEngineering.BindingSidRules.DynamicBindingSidRules',
                [], [],
                '''                Dynamic binding SID options
                ''',
                'dynamic_binding_sid_rules',
                'Cisco-IOS-XR-infra-xtc-agent-cfg', False, is_presence=True),
            ],
            'Cisco-IOS-XR-infra-xtc-agent-cfg',
            'binding-sid-rules',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-infra-xtc-agent-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_segment_routing_ms_cfg',
        ),
    },
    'Sr.TrafficEngineering.Policies.Policy.Steering.Applications.Application' : {
        'meta_info' : _MetaInfoClass('Sr.TrafficEngineering.Policies.Policy.Steering.Applications.Application', REFERENCE_LIST,
            '''Application that steering options need to
be applied''',
            False, 
            [
            _MetaInfoClassMember('application', REFERENCE_ENUM_CLASS, 'XtcSteeringApplication', 'Xtc-steering-application',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_agent_cfg', 'XtcSteeringApplication',
                [], [],
                '''                Steering application
                ''',
                'application',
                'Cisco-IOS-XR-infra-xtc-agent-cfg', True),
            _MetaInfoClassMember('disable', ATTRIBUTE, 'Empty', 'empty',
                None, None,
                [], [],
                '''                Disable all steering services
                ''',
                'disable',
                'Cisco-IOS-XR-infra-xtc-agent-cfg', False),
            ],
            'Cisco-IOS-XR-infra-xtc-agent-cfg',
            'application',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-infra-xtc-agent-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_segment_routing_ms_cfg',
        ),
    },
    'Sr.TrafficEngineering.Policies.Policy.Steering.Applications' : {
        'meta_info' : _MetaInfoClass('Sr.TrafficEngineering.Policies.Policy.Steering.Applications', REFERENCE_CLASS,
            '''Application table that steering options need
to be applied''',
            False, 
            [
            _MetaInfoClassMember('application', REFERENCE_LIST, 'Application', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_segment_routing_ms_cfg', 'Sr.TrafficEngineering.Policies.Policy.Steering.Applications.Application',
                [], [],
                '''                Application that steering options need to
                be applied
                ''',
                'application',
                'Cisco-IOS-XR-infra-xtc-agent-cfg', False),
            ],
            'Cisco-IOS-XR-infra-xtc-agent-cfg',
            'applications',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-infra-xtc-agent-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_segment_routing_ms_cfg',
        ),
    },
    'Sr.TrafficEngineering.Policies.Policy.Steering' : {
        'meta_info' : _MetaInfoClass('Sr.TrafficEngineering.Policies.Policy.Steering', REFERENCE_CLASS,
            '''Steering options for the policy''',
            False, 
            [
            _MetaInfoClassMember('applications', REFERENCE_CLASS, 'Applications', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_segment_routing_ms_cfg', 'Sr.TrafficEngineering.Policies.Policy.Steering.Applications',
                [], [],
                '''                Application table that steering options need
                to be applied
                ''',
                'applications',
                'Cisco-IOS-XR-infra-xtc-agent-cfg', False),
            ],
            'Cisco-IOS-XR-infra-xtc-agent-cfg',
            'steering',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-infra-xtc-agent-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_segment_routing_ms_cfg',
        ),
    },
    'Sr.TrafficEngineering.Policies.Policy.BindingSid' : {
        'meta_info' : _MetaInfoClass('Sr.TrafficEngineering.Policies.Policy.BindingSid', REFERENCE_CLASS,
            '''Binding Segment ID''',
            False, 
            [
            _MetaInfoClassMember('binding-sid-type', REFERENCE_ENUM_CLASS, 'XtcBindingSid', 'Xtc-binding-sid',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_agent_cfg', 'XtcBindingSid',
                [], [],
                '''                Binding SID type
                ''',
                'binding_sid_type',
                'Cisco-IOS-XR-infra-xtc-agent-cfg', False),
            _MetaInfoClassMember('mpls-label', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('16', '1048575')], [],
                '''                MPLS Label
                ''',
                'mpls_label',
                'Cisco-IOS-XR-infra-xtc-agent-cfg', False, has_when=True),
            ],
            'Cisco-IOS-XR-infra-xtc-agent-cfg',
            'binding-sid',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-infra-xtc-agent-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_segment_routing_ms_cfg',
        ),
    },
    'Sr.TrafficEngineering.Policies.Policy.PolicyColorEndpoint' : {
        'meta_info' : _MetaInfoClass('Sr.TrafficEngineering.Policies.Policy.PolicyColorEndpoint', REFERENCE_CLASS,
            '''Color and endpoint of a policyColor,
EndPointType, Endpoint''',
            False, 
            [
            _MetaInfoClassMember('color', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('1', '4294967295')], [],
                '''                Color
                ''',
                'color',
                'Cisco-IOS-XR-infra-xtc-agent-cfg', False, is_mandatory=True),
            _MetaInfoClassMember('end-point-type', REFERENCE_ENUM_CLASS, 'XtcEndPoint', 'Xtc-end-point',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_agent_cfg', 'XtcEndPoint',
                [], [],
                '''                End point type
                ''',
                'end_point_type',
                'Cisco-IOS-XR-infra-xtc-agent-cfg', False, is_mandatory=True),
            _MetaInfoClassMember('end-point-address', REFERENCE_UNION, 'str', 'inet:ip-address-no-zone',
                None, None,
                [], [],
                '''                End point address
                ''',
                'end_point_address',
                'Cisco-IOS-XR-infra-xtc-agent-cfg', False, [
                    _MetaInfoClassMember('end-point-address', ATTRIBUTE, 'str', 'inet:ipv4-address-no-zone',
                        None, None,
                        [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'],
                        '''                        End point address
                        ''',
                        'end_point_address',
                        'Cisco-IOS-XR-infra-xtc-agent-cfg', False, is_mandatory=True),
                    _MetaInfoClassMember('end-point-address', ATTRIBUTE, 'str', 'inet:ipv6-address-no-zone',
                        None, None,
                        [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'],
                        '''                        End point address
                        ''',
                        'end_point_address',
                        'Cisco-IOS-XR-infra-xtc-agent-cfg', False, is_mandatory=True),
                ], is_mandatory=True),
            ],
            'Cisco-IOS-XR-infra-xtc-agent-cfg',
            'policy-color-endpoint',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-infra-xtc-agent-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_segment_routing_ms_cfg',
            is_presence=True,
        ),
    },
    'Sr.TrafficEngineering.Policies.Policy.AutoRoute.AutoRouteMetric' : {
        'meta_info' : _MetaInfoClass('Sr.TrafficEngineering.Policies.Policy.AutoRoute.AutoRouteMetric', REFERENCE_CLASS,
            '''Autoroute metric''',
            False, 
            [
            _MetaInfoClassMember('autoroute-metric-type', REFERENCE_ENUM_CLASS, 'XtcAutoRouteMetric', 'Xtc-auto-route-metric',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_agent_cfg', 'XtcAutoRouteMetric',
                [], [],
                '''                Metric type
                ''',
                'autoroute_metric_type',
                'Cisco-IOS-XR-infra-xtc-agent-cfg', False),
            _MetaInfoClassMember('metric-relative-value', ATTRIBUTE, 'int', 'int32',
                None, None,
                [('-10', '10')], [],
                '''                Autoroute relative metric
                ''',
                'metric_relative_value',
                'Cisco-IOS-XR-infra-xtc-agent-cfg', False),
            _MetaInfoClassMember('metric-constant-value', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('1', '2147483647')], [],
                '''                Autoroute constant metric
                ''',
                'metric_constant_value',
                'Cisco-IOS-XR-infra-xtc-agent-cfg', False),
            ],
            'Cisco-IOS-XR-infra-xtc-agent-cfg',
            'auto-route-metric',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-infra-xtc-agent-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_segment_routing_ms_cfg',
        ),
    },
    'Sr.TrafficEngineering.Policies.Policy.AutoRoute.IncludePrefixes.IncludePrefix' : {
        'meta_info' : _MetaInfoClass('Sr.TrafficEngineering.Policies.Policy.AutoRoute.IncludePrefixes.IncludePrefix', REFERENCE_LIST,
            '''Autoroute IP prefix to include''',
            False, 
            [
            _MetaInfoClassMember('af-type', REFERENCE_ENUM_CLASS, 'XtcAddressFamily', 'Xtc-address-family',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_agent_cfg', 'XtcAddressFamily',
                [], [],
                '''                Address family type
                ''',
                'af_type',
                'Cisco-IOS-XR-infra-xtc-agent-cfg', True),
            _MetaInfoClassMember('prefix-address', REFERENCE_UNION, 'str', 'inet:ip-address-no-zone',
                None, None,
                [], [],
                '''                Autoroute prefix IP address
                ''',
                'prefix_address',
                'Cisco-IOS-XR-infra-xtc-agent-cfg', True, [
                    _MetaInfoClassMember('prefix-address', ATTRIBUTE, 'str', 'inet:ipv4-address-no-zone',
                        None, None,
                        [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'],
                        '''                        Autoroute prefix IP address
                        ''',
                        'prefix_address',
                        'Cisco-IOS-XR-infra-xtc-agent-cfg', True),
                    _MetaInfoClassMember('prefix-address', ATTRIBUTE, 'str', 'inet:ipv6-address-no-zone',
                        None, None,
                        [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'],
                        '''                        Autoroute prefix IP address
                        ''',
                        'prefix_address',
                        'Cisco-IOS-XR-infra-xtc-agent-cfg', True),
                ]),
            _MetaInfoClassMember('prefix-length', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('0', '32')], [],
                '''                Autoroute IP prefix length
                ''',
                'prefix_length',
                'Cisco-IOS-XR-infra-xtc-agent-cfg', True),
            ],
            'Cisco-IOS-XR-infra-xtc-agent-cfg',
            'include-prefix',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-infra-xtc-agent-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_segment_routing_ms_cfg',
        ),
    },
    'Sr.TrafficEngineering.Policies.Policy.AutoRoute.IncludePrefixes' : {
        'meta_info' : _MetaInfoClass('Sr.TrafficEngineering.Policies.Policy.AutoRoute.IncludePrefixes', REFERENCE_CLASS,
            '''Autoroute include prefix table configuration''',
            False, 
            [
            _MetaInfoClassMember('include-prefix', REFERENCE_LIST, 'IncludePrefix', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_segment_routing_ms_cfg', 'Sr.TrafficEngineering.Policies.Policy.AutoRoute.IncludePrefixes.IncludePrefix',
                [], [],
                '''                Autoroute IP prefix to include
                ''',
                'include_prefix',
                'Cisco-IOS-XR-infra-xtc-agent-cfg', False),
            ],
            'Cisco-IOS-XR-infra-xtc-agent-cfg',
            'include-prefixes',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-infra-xtc-agent-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_segment_routing_ms_cfg',
        ),
    },
    'Sr.TrafficEngineering.Policies.Policy.AutoRoute' : {
        'meta_info' : _MetaInfoClass('Sr.TrafficEngineering.Policies.Policy.AutoRoute', REFERENCE_CLASS,
            '''Autoroute configuration''',
            False, 
            [
            _MetaInfoClassMember('auto-route-metric', REFERENCE_CLASS, 'AutoRouteMetric', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_segment_routing_ms_cfg', 'Sr.TrafficEngineering.Policies.Policy.AutoRoute.AutoRouteMetric',
                [], [],
                '''                Autoroute metric
                ''',
                'auto_route_metric',
                'Cisco-IOS-XR-infra-xtc-agent-cfg', False),
            _MetaInfoClassMember('include-prefixes', REFERENCE_CLASS, 'IncludePrefixes', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_segment_routing_ms_cfg', 'Sr.TrafficEngineering.Policies.Policy.AutoRoute.IncludePrefixes',
                [], [],
                '''                Autoroute include prefix table configuration
                ''',
                'include_prefixes',
                'Cisco-IOS-XR-infra-xtc-agent-cfg', False),
            _MetaInfoClassMember('force-sr-include', ATTRIBUTE, 'Empty', 'empty',
                None, None,
                [], [],
                '''                Force autoroute policy to be safe for
                carrying SR labelled traffic
                ''',
                'force_sr_include',
                'Cisco-IOS-XR-infra-xtc-agent-cfg', False),
            _MetaInfoClassMember('forward-class', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('0', '7')], [],
                '''                Forward class associated with the policy
                ''',
                'forward_class',
                'Cisco-IOS-XR-infra-xtc-agent-cfg', False),
            _MetaInfoClassMember('enable', ATTRIBUTE, 'Empty', 'empty',
                None, None,
                [], [],
                '''                True only
                ''',
                'enable',
                'Cisco-IOS-XR-infra-xtc-agent-cfg', False),
            ],
            'Cisco-IOS-XR-infra-xtc-agent-cfg',
            'auto-route',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-infra-xtc-agent-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_segment_routing_ms_cfg',
        ),
    },
    'Sr.TrafficEngineering.Policies.Policy.CandidatePaths.Preferences.Preference.Constraints.DisjointPath' : {
        'meta_info' : _MetaInfoClass('Sr.TrafficEngineering.Policies.Policy.CandidatePaths.Preferences.Preference.Constraints.DisjointPath', REFERENCE_CLASS,
            '''Disjoint path''',
            False, 
            [
            _MetaInfoClassMember('group-id', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('1', '65535')], [],
                '''                Group ID
                ''',
                'group_id',
                'Cisco-IOS-XR-infra-xtc-agent-cfg', False, is_mandatory=True),
            _MetaInfoClassMember('disjointness-type', REFERENCE_ENUM_CLASS, 'XtcDisjointness', 'Xtc-disjointness',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_agent_cfg', 'XtcDisjointness',
                [], [],
                '''                Disjointness Type
                ''',
                'disjointness_type',
                'Cisco-IOS-XR-infra-xtc-agent-cfg', False, is_mandatory=True),
            _MetaInfoClassMember('sub-id', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('1', '65535')], [],
                '''                Sub ID
                ''',
                'sub_id',
                'Cisco-IOS-XR-infra-xtc-agent-cfg', False),
            ],
            'Cisco-IOS-XR-infra-xtc-agent-cfg',
            'disjoint-path',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-infra-xtc-agent-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_segment_routing_ms_cfg',
            is_presence=True,
        ),
    },
    'Sr.TrafficEngineering.Policies.Policy.CandidatePaths.Preferences.Preference.Constraints.SegmentRules' : {
        'meta_info' : _MetaInfoClass('Sr.TrafficEngineering.Policies.Policy.CandidatePaths.Preferences.Preference.Constraints.SegmentRules', REFERENCE_CLASS,
            '''SR path computation segment specific
rules''',
            False, 
            [
            _MetaInfoClassMember('sid-algorithm', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('128', '255')], [],
                '''                Prefix-SID algorithm
                ''',
                'sid_algorithm',
                'Cisco-IOS-XR-infra-xtc-agent-cfg', False, is_mandatory=True),
            ],
            'Cisco-IOS-XR-infra-xtc-agent-cfg',
            'segment-rules',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-infra-xtc-agent-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_segment_routing_ms_cfg',
            is_presence=True,
        ),
    },
    'Sr.TrafficEngineering.Policies.Policy.CandidatePaths.Preferences.Preference.Constraints.AffinityRules.AffinityRule.AffinityName' : {
        'meta_info' : _MetaInfoClass('Sr.TrafficEngineering.Policies.Policy.CandidatePaths.Preferences.Preference.Constraints.AffinityRules.AffinityRule.AffinityName', REFERENCE_LIST,
            '''Affinity rule name''',
            False, 
            [
            _MetaInfoClassMember('affinity-name', ATTRIBUTE, 'str', 'xr:Cisco-ios-xr-string',
                None, None,
                [(1, 32)], [],
                '''                Affinity name
                ''',
                'affinity_name',
                'Cisco-IOS-XR-infra-xtc-agent-cfg', True),
            ],
            'Cisco-IOS-XR-infra-xtc-agent-cfg',
            'affinity-name',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-infra-xtc-agent-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_segment_routing_ms_cfg',
        ),
    },
    'Sr.TrafficEngineering.Policies.Policy.CandidatePaths.Preferences.Preference.Constraints.AffinityRules.AffinityRule' : {
        'meta_info' : _MetaInfoClass('Sr.TrafficEngineering.Policies.Policy.CandidatePaths.Preferences.Preference.Constraints.AffinityRules.AffinityRule', REFERENCE_LIST,
            '''SR path computation and verification affinity
rule''',
            False, 
            [
            _MetaInfoClassMember('rule', REFERENCE_ENUM_CLASS, 'XtcAffinityRule', 'Xtc-affinity-rule',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_agent_cfg', 'XtcAffinityRule',
                [], [],
                '''                Affinity rule type
                ''',
                'rule',
                'Cisco-IOS-XR-infra-xtc-agent-cfg', True),
            _MetaInfoClassMember('affinity-name', REFERENCE_LIST, 'AffinityName', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_segment_routing_ms_cfg', 'Sr.TrafficEngineering.Policies.Policy.CandidatePaths.Preferences.Preference.Constraints.AffinityRules.AffinityRule.AffinityName',
                [], [],
                '''                Affinity rule name
                ''',
                'affinity_name',
                'Cisco-IOS-XR-infra-xtc-agent-cfg', False),
            ],
            'Cisco-IOS-XR-infra-xtc-agent-cfg',
            'affinity-rule',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-infra-xtc-agent-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_segment_routing_ms_cfg',
        ),
    },
    'Sr.TrafficEngineering.Policies.Policy.CandidatePaths.Preferences.Preference.Constraints.AffinityRules' : {
        'meta_info' : _MetaInfoClass('Sr.TrafficEngineering.Policies.Policy.CandidatePaths.Preferences.Preference.Constraints.AffinityRules', REFERENCE_CLASS,
            '''SR path computation and verification affinity
rules''',
            False, 
            [
            _MetaInfoClassMember('affinity-rule', REFERENCE_LIST, 'AffinityRule', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_segment_routing_ms_cfg', 'Sr.TrafficEngineering.Policies.Policy.CandidatePaths.Preferences.Preference.Constraints.AffinityRules.AffinityRule',
                [], [],
                '''                SR path computation and verification affinity
                rule
                ''',
                'affinity_rule',
                'Cisco-IOS-XR-infra-xtc-agent-cfg', False),
            ],
            'Cisco-IOS-XR-infra-xtc-agent-cfg',
            'affinity-rules',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-infra-xtc-agent-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_segment_routing_ms_cfg',
        ),
    },
    'Sr.TrafficEngineering.Policies.Policy.CandidatePaths.Preferences.Preference.Constraints' : {
        'meta_info' : _MetaInfoClass('Sr.TrafficEngineering.Policies.Policy.CandidatePaths.Preferences.Preference.Constraints', REFERENCE_CLASS,
            '''SR path computation and verification
constraints''',
            False, 
            [
            _MetaInfoClassMember('disjoint-path', REFERENCE_CLASS, 'DisjointPath', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_segment_routing_ms_cfg', 'Sr.TrafficEngineering.Policies.Policy.CandidatePaths.Preferences.Preference.Constraints.DisjointPath',
                [], [],
                '''                Disjoint path
                ''',
                'disjoint_path',
                'Cisco-IOS-XR-infra-xtc-agent-cfg', False, is_presence=True),
            _MetaInfoClassMember('segment-rules', REFERENCE_CLASS, 'SegmentRules', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_segment_routing_ms_cfg', 'Sr.TrafficEngineering.Policies.Policy.CandidatePaths.Preferences.Preference.Constraints.SegmentRules',
                [], [],
                '''                SR path computation segment specific
                rules
                ''',
                'segment_rules',
                'Cisco-IOS-XR-infra-xtc-agent-cfg', False, is_presence=True),
            _MetaInfoClassMember('affinity-rules', REFERENCE_CLASS, 'AffinityRules', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_segment_routing_ms_cfg', 'Sr.TrafficEngineering.Policies.Policy.CandidatePaths.Preferences.Preference.Constraints.AffinityRules',
                [], [],
                '''                SR path computation and verification affinity
                rules
                ''',
                'affinity_rules',
                'Cisco-IOS-XR-infra-xtc-agent-cfg', False),
            ],
            'Cisco-IOS-XR-infra-xtc-agent-cfg',
            'constraints',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-infra-xtc-agent-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_segment_routing_ms_cfg',
        ),
    },
    'Sr.TrafficEngineering.Policies.Policy.CandidatePaths.Preferences.Preference.PathInfos.PathInfo.Metric.MetricMargin' : {
        'meta_info' : _MetaInfoClass('Sr.TrafficEngineering.Policies.Policy.CandidatePaths.Preferences.Preference.PathInfos.PathInfo.Metric.MetricMargin', REFERENCE_CLASS,
            '''Metric Margin''',
            False, 
            [
            _MetaInfoClassMember('value-type', REFERENCE_ENUM_CLASS, 'XtcMetricValue', 'Xtc-metric-value',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_agent_cfg', 'XtcMetricValue',
                [], [],
                '''                Metric margin type
                ''',
                'value_type',
                'Cisco-IOS-XR-infra-xtc-agent-cfg', False),
            _MetaInfoClassMember('absolute-value', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('0', '2147483647')], [],
                '''                Absolute metric value
                ''',
                'absolute_value',
                'Cisco-IOS-XR-infra-xtc-agent-cfg', False, has_when=True),
            _MetaInfoClassMember('relative-value', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('0', '2147483647')], [],
                '''                Relative metric value
                ''',
                'relative_value',
                'Cisco-IOS-XR-infra-xtc-agent-cfg', False, has_when=True),
            ],
            'Cisco-IOS-XR-infra-xtc-agent-cfg',
            'metric-margin',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-infra-xtc-agent-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_segment_routing_ms_cfg',
        ),
    },
    'Sr.TrafficEngineering.Policies.Policy.CandidatePaths.Preferences.Preference.PathInfos.PathInfo.Metric' : {
        'meta_info' : _MetaInfoClass('Sr.TrafficEngineering.Policies.Policy.CandidatePaths.Preferences.Preference.PathInfos.PathInfo.Metric', REFERENCE_CLASS,
            '''Metric configuration, valid only for
dynamic path-options''',
            False, 
            [
            _MetaInfoClassMember('sid-limit', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('1', '255')], [],
                '''                Maximum number of SIDs
                ''',
                'sid_limit',
                'Cisco-IOS-XR-infra-xtc-agent-cfg', False),
            _MetaInfoClassMember('metric-type', REFERENCE_ENUM_CLASS, 'XtcMetric', 'Xtc-metric',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_agent_cfg', 'XtcMetric',
                [], [],
                '''                Metric type
                ''',
                'metric_type',
                'Cisco-IOS-XR-infra-xtc-agent-cfg', False),
            _MetaInfoClassMember('enable', ATTRIBUTE, 'Empty', 'empty',
                None, None,
                [], [],
                '''                True only
                ''',
                'enable',
                'Cisco-IOS-XR-infra-xtc-agent-cfg', False),
            _MetaInfoClassMember('metric-margin', REFERENCE_CLASS, 'MetricMargin', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_segment_routing_ms_cfg', 'Sr.TrafficEngineering.Policies.Policy.CandidatePaths.Preferences.Preference.PathInfos.PathInfo.Metric.MetricMargin',
                [], [],
                '''                Metric Margin
                ''',
                'metric_margin',
                'Cisco-IOS-XR-infra-xtc-agent-cfg', False),
            ],
            'Cisco-IOS-XR-infra-xtc-agent-cfg',
            'metric',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-infra-xtc-agent-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_segment_routing_ms_cfg',
        ),
    },
    'Sr.TrafficEngineering.Policies.Policy.CandidatePaths.Preferences.Preference.PathInfos.PathInfo.Pcep' : {
        'meta_info' : _MetaInfoClass('Sr.TrafficEngineering.Policies.Policy.CandidatePaths.Preferences.Preference.PathInfos.PathInfo.Pcep', REFERENCE_CLASS,
            '''Path Computation Element Protocol''',
            False, 
            [
            _MetaInfoClassMember('enable', ATTRIBUTE, 'Empty', 'empty',
                None, None,
                [], [],
                '''                True only
                ''',
                'enable',
                'Cisco-IOS-XR-infra-xtc-agent-cfg', False),
            ],
            'Cisco-IOS-XR-infra-xtc-agent-cfg',
            'pcep',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-infra-xtc-agent-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_segment_routing_ms_cfg',
        ),
    },
    'Sr.TrafficEngineering.Policies.Policy.CandidatePaths.Preferences.Preference.PathInfos.PathInfo' : {
        'meta_info' : _MetaInfoClass('Sr.TrafficEngineering.Policies.Policy.CandidatePaths.Preferences.Preference.PathInfos.PathInfo', REFERENCE_LIST,
            '''Policy configuration''',
            False, 
            [
            _MetaInfoClassMember('type', REFERENCE_ENUM_CLASS, 'XtcPath', 'Xtc-path',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_agent_cfg', 'XtcPath',
                [], [],
                '''                Path-option type
                ''',
                'type',
                'Cisco-IOS-XR-infra-xtc-agent-cfg', True),
            _MetaInfoClassMember('hop-type', REFERENCE_ENUM_CLASS, 'XtcPathHop', 'Xtc-path-hop',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_agent_cfg', 'XtcPathHop',
                [], [],
                '''                Type of dynamic path to be computed
                ''',
                'hop_type',
                'Cisco-IOS-XR-infra-xtc-agent-cfg', True),
            _MetaInfoClassMember('segment-list-name', ATTRIBUTE, 'str', 'xr:Cisco-ios-xr-string',
                None, None,
                [(1, 128)], [],
                '''                Segment-list name
                ''',
                'segment_list_name',
                'Cisco-IOS-XR-infra-xtc-agent-cfg', True),
            _MetaInfoClassMember('metric', REFERENCE_CLASS, 'Metric', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_segment_routing_ms_cfg', 'Sr.TrafficEngineering.Policies.Policy.CandidatePaths.Preferences.Preference.PathInfos.PathInfo.Metric',
                [], [],
                '''                Metric configuration, valid only for
                dynamic path-options
                ''',
                'metric',
                'Cisco-IOS-XR-infra-xtc-agent-cfg', False),
            _MetaInfoClassMember('pcep', REFERENCE_CLASS, 'Pcep', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_segment_routing_ms_cfg', 'Sr.TrafficEngineering.Policies.Policy.CandidatePaths.Preferences.Preference.PathInfos.PathInfo.Pcep',
                [], [],
                '''                Path Computation Element Protocol
                ''',
                'pcep',
                'Cisco-IOS-XR-infra-xtc-agent-cfg', False),
            _MetaInfoClassMember('weight', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('1', '4294967295')], [],
                '''                Path-option weight
                ''',
                'weight',
                'Cisco-IOS-XR-infra-xtc-agent-cfg', False),
            _MetaInfoClassMember('enable', ATTRIBUTE, 'Empty', 'empty',
                None, None,
                [], [],
                '''                True only
                ''',
                'enable',
                'Cisco-IOS-XR-infra-xtc-agent-cfg', False),
            ],
            'Cisco-IOS-XR-infra-xtc-agent-cfg',
            'path-info',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-infra-xtc-agent-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_segment_routing_ms_cfg',
        ),
    },
    'Sr.TrafficEngineering.Policies.Policy.CandidatePaths.Preferences.Preference.PathInfos' : {
        'meta_info' : _MetaInfoClass('Sr.TrafficEngineering.Policies.Policy.CandidatePaths.Preferences.Preference.PathInfos', REFERENCE_CLASS,
            '''Policy path-option preference
configuration''',
            False, 
            [
            _MetaInfoClassMember('path-info', REFERENCE_LIST, 'PathInfo', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_segment_routing_ms_cfg', 'Sr.TrafficEngineering.Policies.Policy.CandidatePaths.Preferences.Preference.PathInfos.PathInfo',
                [], [],
                '''                Policy configuration
                ''',
                'path_info',
                'Cisco-IOS-XR-infra-xtc-agent-cfg', False),
            ],
            'Cisco-IOS-XR-infra-xtc-agent-cfg',
            'path-infos',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-infra-xtc-agent-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_segment_routing_ms_cfg',
        ),
    },
    'Sr.TrafficEngineering.Policies.Policy.CandidatePaths.Preferences.Preference' : {
        'meta_info' : _MetaInfoClass('Sr.TrafficEngineering.Policies.Policy.CandidatePaths.Preferences.Preference', REFERENCE_LIST,
            '''Policy path-option preference entry''',
            False, 
            [
            _MetaInfoClassMember('path-index', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('1', '65535')], [],
                '''                Path-option preference
                ''',
                'path_index',
                'Cisco-IOS-XR-infra-xtc-agent-cfg', True),
            _MetaInfoClassMember('constraints', REFERENCE_CLASS, 'Constraints', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_segment_routing_ms_cfg', 'Sr.TrafficEngineering.Policies.Policy.CandidatePaths.Preferences.Preference.Constraints',
                [], [],
                '''                SR path computation and verification
                constraints
                ''',
                'constraints',
                'Cisco-IOS-XR-infra-xtc-agent-cfg', False),
            _MetaInfoClassMember('path-infos', REFERENCE_CLASS, 'PathInfos', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_segment_routing_ms_cfg', 'Sr.TrafficEngineering.Policies.Policy.CandidatePaths.Preferences.Preference.PathInfos',
                [], [],
                '''                Policy path-option preference
                configuration
                ''',
                'path_infos',
                'Cisco-IOS-XR-infra-xtc-agent-cfg', False),
            _MetaInfoClassMember('enable', ATTRIBUTE, 'Empty', 'empty',
                None, None,
                [], [],
                '''                True only
                ''',
                'enable',
                'Cisco-IOS-XR-infra-xtc-agent-cfg', False),
            ],
            'Cisco-IOS-XR-infra-xtc-agent-cfg',
            'preference',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-infra-xtc-agent-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_segment_routing_ms_cfg',
        ),
    },
    'Sr.TrafficEngineering.Policies.Policy.CandidatePaths.Preferences' : {
        'meta_info' : _MetaInfoClass('Sr.TrafficEngineering.Policies.Policy.CandidatePaths.Preferences', REFERENCE_CLASS,
            '''Policy path-option preference table''',
            False, 
            [
            _MetaInfoClassMember('preference', REFERENCE_LIST, 'Preference', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_segment_routing_ms_cfg', 'Sr.TrafficEngineering.Policies.Policy.CandidatePaths.Preferences.Preference',
                [], [],
                '''                Policy path-option preference entry
                ''',
                'preference',
                'Cisco-IOS-XR-infra-xtc-agent-cfg', False),
            ],
            'Cisco-IOS-XR-infra-xtc-agent-cfg',
            'preferences',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-infra-xtc-agent-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_segment_routing_ms_cfg',
        ),
    },
    'Sr.TrafficEngineering.Policies.Policy.CandidatePaths' : {
        'meta_info' : _MetaInfoClass('Sr.TrafficEngineering.Policies.Policy.CandidatePaths', REFERENCE_CLASS,
            '''Policy candidate-paths configuration''',
            False, 
            [
            _MetaInfoClassMember('preferences', REFERENCE_CLASS, 'Preferences', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_segment_routing_ms_cfg', 'Sr.TrafficEngineering.Policies.Policy.CandidatePaths.Preferences',
                [], [],
                '''                Policy path-option preference table
                ''',
                'preferences',
                'Cisco-IOS-XR-infra-xtc-agent-cfg', False),
            _MetaInfoClassMember('enable', ATTRIBUTE, 'Empty', 'empty',
                None, None,
                [], [],
                '''                True only
                ''',
                'enable',
                'Cisco-IOS-XR-infra-xtc-agent-cfg', False),
            ],
            'Cisco-IOS-XR-infra-xtc-agent-cfg',
            'candidate-paths',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-infra-xtc-agent-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_segment_routing_ms_cfg',
        ),
    },
    'Sr.TrafficEngineering.Policies.Policy.SourceAddress' : {
        'meta_info' : _MetaInfoClass('Sr.TrafficEngineering.Policies.Policy.SourceAddress', REFERENCE_CLASS,
            '''Source address of a candidate path. EndPointType
, Source''',
            False, 
            [
            _MetaInfoClassMember('ip-address-type', REFERENCE_ENUM_CLASS, 'XtcEndPoint', 'Xtc-end-point',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_agent_cfg', 'XtcEndPoint',
                [], [],
                '''                IP address type
                ''',
                'ip_address_type',
                'Cisco-IOS-XR-infra-xtc-agent-cfg', False, is_mandatory=True),
            _MetaInfoClassMember('source-address', REFERENCE_UNION, 'str', 'inet:ip-address-no-zone',
                None, None,
                [], [],
                '''                Source address
                ''',
                'source_address',
                'Cisco-IOS-XR-infra-xtc-agent-cfg', False, [
                    _MetaInfoClassMember('source-address', ATTRIBUTE, 'str', 'inet:ipv4-address-no-zone',
                        None, None,
                        [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'],
                        '''                        Source address
                        ''',
                        'source_address',
                        'Cisco-IOS-XR-infra-xtc-agent-cfg', False, is_mandatory=True),
                    _MetaInfoClassMember('source-address', ATTRIBUTE, 'str', 'inet:ipv6-address-no-zone',
                        None, None,
                        [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'],
                        '''                        Source address
                        ''',
                        'source_address',
                        'Cisco-IOS-XR-infra-xtc-agent-cfg', False, is_mandatory=True),
                ], is_mandatory=True),
            ],
            'Cisco-IOS-XR-infra-xtc-agent-cfg',
            'source-address',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-infra-xtc-agent-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_segment_routing_ms_cfg',
            is_presence=True,
        ),
    },
    'Sr.TrafficEngineering.Policies.Policy' : {
        'meta_info' : _MetaInfoClass('Sr.TrafficEngineering.Policies.Policy', REFERENCE_LIST,
            '''Policy configuration''',
            False, 
            [
            _MetaInfoClassMember('policy-name', ATTRIBUTE, 'str', 'xr:Cisco-ios-xr-string',
                None, None,
                [(1, 59)], [],
                '''                Policy name
                ''',
                'policy_name',
                'Cisco-IOS-XR-infra-xtc-agent-cfg', True),
            _MetaInfoClassMember('steering', REFERENCE_CLASS, 'Steering', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_segment_routing_ms_cfg', 'Sr.TrafficEngineering.Policies.Policy.Steering',
                [], [],
                '''                Steering options for the policy
                ''',
                'steering',
                'Cisco-IOS-XR-infra-xtc-agent-cfg', False),
            _MetaInfoClassMember('binding-sid', REFERENCE_CLASS, 'BindingSid', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_segment_routing_ms_cfg', 'Sr.TrafficEngineering.Policies.Policy.BindingSid',
                [], [],
                '''                Binding Segment ID
                ''',
                'binding_sid',
                'Cisco-IOS-XR-infra-xtc-agent-cfg', False),
            _MetaInfoClassMember('policy-color-endpoint', REFERENCE_CLASS, 'PolicyColorEndpoint', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_segment_routing_ms_cfg', 'Sr.TrafficEngineering.Policies.Policy.PolicyColorEndpoint',
                [], [],
                '''                Color and endpoint of a policyColor,
                EndPointType, Endpoint
                ''',
                'policy_color_endpoint',
                'Cisco-IOS-XR-infra-xtc-agent-cfg', False, is_presence=True),
            _MetaInfoClassMember('auto-route', REFERENCE_CLASS, 'AutoRoute', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_segment_routing_ms_cfg', 'Sr.TrafficEngineering.Policies.Policy.AutoRoute',
                [], [],
                '''                Autoroute configuration
                ''',
                'auto_route',
                'Cisco-IOS-XR-infra-xtc-agent-cfg', False),
            _MetaInfoClassMember('candidate-paths', REFERENCE_CLASS, 'CandidatePaths', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_segment_routing_ms_cfg', 'Sr.TrafficEngineering.Policies.Policy.CandidatePaths',
                [], [],
                '''                Policy candidate-paths configuration
                ''',
                'candidate_paths',
                'Cisco-IOS-XR-infra-xtc-agent-cfg', False),
            _MetaInfoClassMember('ipv6-disable', ATTRIBUTE, 'Empty', 'empty',
                None, None,
                [], [],
                '''                IPv6 disable
                ''',
                'ipv6_disable',
                'Cisco-IOS-XR-infra-xtc-agent-cfg', False),
            _MetaInfoClassMember('shutdown', ATTRIBUTE, 'Empty', 'empty',
                None, None,
                [], [],
                '''                Administratively shutdown policy
                ''',
                'shutdown',
                'Cisco-IOS-XR-infra-xtc-agent-cfg', False),
            _MetaInfoClassMember('bandwidth', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('1', '4294967295')], [],
                '''                The value of the bandwidth reserved by this
                policy in kbps
                ''',
                'bandwidth',
                'Cisco-IOS-XR-infra-xtc-agent-cfg', False),
            _MetaInfoClassMember('source-address', REFERENCE_CLASS, 'SourceAddress', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_segment_routing_ms_cfg', 'Sr.TrafficEngineering.Policies.Policy.SourceAddress',
                [], [],
                '''                Source address of a candidate path. EndPointType
                , Source
                ''',
                'source_address',
                'Cisco-IOS-XR-infra-xtc-agent-cfg', False, is_presence=True),
            _MetaInfoClassMember('enable', ATTRIBUTE, 'Empty', 'empty',
                None, None,
                [], [],
                '''                True only
                ''',
                'enable',
                'Cisco-IOS-XR-infra-xtc-agent-cfg', False),
            ],
            'Cisco-IOS-XR-infra-xtc-agent-cfg',
            'policy',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-infra-xtc-agent-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_segment_routing_ms_cfg',
        ),
    },
    'Sr.TrafficEngineering.Policies' : {
        'meta_info' : _MetaInfoClass('Sr.TrafficEngineering.Policies', REFERENCE_CLASS,
            '''Policy configuration''',
            False, 
            [
            _MetaInfoClassMember('policy', REFERENCE_LIST, 'Policy', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_segment_routing_ms_cfg', 'Sr.TrafficEngineering.Policies.Policy',
                [], [],
                '''                Policy configuration
                ''',
                'policy',
                'Cisco-IOS-XR-infra-xtc-agent-cfg', False),
            ],
            'Cisco-IOS-XR-infra-xtc-agent-cfg',
            'policies',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-infra-xtc-agent-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_segment_routing_ms_cfg',
        ),
    },
    'Sr.TrafficEngineering.SrteInterfaces.SrteInterface.InterfaceAffinities.InterfaceAffinity' : {
        'meta_info' : _MetaInfoClass('Sr.TrafficEngineering.SrteInterfaces.SrteInterface.InterfaceAffinities.InterfaceAffinity', REFERENCE_LIST,
            '''Set user defined interface attribute flags''',
            False, 
            [
            _MetaInfoClassMember('affinity-name', ATTRIBUTE, 'str', 'xr:Cisco-ios-xr-string',
                None, None,
                [(1, 32)], [],
                '''                Interface affinity names
                ''',
                'affinity_name',
                'Cisco-IOS-XR-infra-xtc-agent-cfg', True),
            ],
            'Cisco-IOS-XR-infra-xtc-agent-cfg',
            'interface-affinity',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-infra-xtc-agent-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_segment_routing_ms_cfg',
        ),
    },
    'Sr.TrafficEngineering.SrteInterfaces.SrteInterface.InterfaceAffinities' : {
        'meta_info' : _MetaInfoClass('Sr.TrafficEngineering.SrteInterfaces.SrteInterface.InterfaceAffinities', REFERENCE_CLASS,
            '''Set user defined interface attribute flags''',
            False, 
            [
            _MetaInfoClassMember('interface-affinity', REFERENCE_LIST, 'InterfaceAffinity', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_segment_routing_ms_cfg', 'Sr.TrafficEngineering.SrteInterfaces.SrteInterface.InterfaceAffinities.InterfaceAffinity',
                [], [],
                '''                Set user defined interface attribute flags
                ''',
                'interface_affinity',
                'Cisco-IOS-XR-infra-xtc-agent-cfg', False),
            ],
            'Cisco-IOS-XR-infra-xtc-agent-cfg',
            'interface-affinities',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-infra-xtc-agent-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_segment_routing_ms_cfg',
        ),
    },
    'Sr.TrafficEngineering.SrteInterfaces.SrteInterface' : {
        'meta_info' : _MetaInfoClass('Sr.TrafficEngineering.SrteInterfaces.SrteInterface', REFERENCE_LIST,
            '''SR-TE interface''',
            False, 
            [
            _MetaInfoClassMember('srte-interface-name', ATTRIBUTE, 'str', 'xr:Interface-name',
                None, None,
                [], [b'[a-zA-Z0-9._/-]+'],
                '''                SR-TE Interface name
                ''',
                'srte_interface_name',
                'Cisco-IOS-XR-infra-xtc-agent-cfg', True),
            _MetaInfoClassMember('interface-affinities', REFERENCE_CLASS, 'InterfaceAffinities', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_segment_routing_ms_cfg', 'Sr.TrafficEngineering.SrteInterfaces.SrteInterface.InterfaceAffinities',
                [], [],
                '''                Set user defined interface attribute flags
                ''',
                'interface_affinities',
                'Cisco-IOS-XR-infra-xtc-agent-cfg', False),
            _MetaInfoClassMember('interface-metric', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('0', '2147483647')], [],
                '''                Interface TE metric configuration
                ''',
                'interface_metric',
                'Cisco-IOS-XR-infra-xtc-agent-cfg', False),
            _MetaInfoClassMember('enable', ATTRIBUTE, 'Empty', 'empty',
                None, None,
                [], [],
                '''                True only
                ''',
                'enable',
                'Cisco-IOS-XR-infra-xtc-agent-cfg', False),
            ],
            'Cisco-IOS-XR-infra-xtc-agent-cfg',
            'srte-interface',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-infra-xtc-agent-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_segment_routing_ms_cfg',
        ),
    },
    'Sr.TrafficEngineering.SrteInterfaces' : {
        'meta_info' : _MetaInfoClass('Sr.TrafficEngineering.SrteInterfaces', REFERENCE_CLASS,
            '''SR-TE interfaces''',
            False, 
            [
            _MetaInfoClassMember('srte-interface', REFERENCE_LIST, 'SrteInterface', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_segment_routing_ms_cfg', 'Sr.TrafficEngineering.SrteInterfaces.SrteInterface',
                [], [],
                '''                SR-TE interface
                ''',
                'srte_interface',
                'Cisco-IOS-XR-infra-xtc-agent-cfg', False),
            ],
            'Cisco-IOS-XR-infra-xtc-agent-cfg',
            'srte-interfaces',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-infra-xtc-agent-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_segment_routing_ms_cfg',
        ),
    },
    'Sr.TrafficEngineering.Pcc.PcePeers.PcePeer' : {
        'meta_info' : _MetaInfoClass('Sr.TrafficEngineering.Pcc.PcePeers.PcePeer', REFERENCE_LIST,
            '''PCE peer''',
            False, 
            [
            _MetaInfoClassMember('pce-address', REFERENCE_UNION, 'str', 'inet:ip-address-no-zone',
                None, None,
                [], [],
                '''                Remote PCE address
                ''',
                'pce_address',
                'Cisco-IOS-XR-infra-xtc-agent-cfg', True, [
                    _MetaInfoClassMember('pce-address', ATTRIBUTE, 'str', 'inet:ipv4-address-no-zone',
                        None, None,
                        [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'],
                        '''                        Remote PCE address
                        ''',
                        'pce_address',
                        'Cisco-IOS-XR-infra-xtc-agent-cfg', True),
                    _MetaInfoClassMember('pce-address', ATTRIBUTE, 'str', 'inet:ipv6-address-no-zone',
                        None, None,
                        [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'],
                        '''                        Remote PCE address
                        ''',
                        'pce_address',
                        'Cisco-IOS-XR-infra-xtc-agent-cfg', True),
                ]),
            _MetaInfoClassMember('password', ATTRIBUTE, 'str', 'string',
                None, None,
                [(1, 25)], [],
                '''                PCC Peer MD5 Password
                ''',
                'password',
                'Cisco-IOS-XR-infra-xtc-agent-cfg', False),
            _MetaInfoClassMember('keychain', ATTRIBUTE, 'str', 'string',
                None, None,
                [(1, 32)], [],
                '''                PCC Peer Keychain
                ''',
                'keychain',
                'Cisco-IOS-XR-infra-xtc-agent-cfg', False),
            _MetaInfoClassMember('enable', ATTRIBUTE, 'Empty', 'empty',
                None, None,
                [], [],
                '''                PCC Peer Enable
                ''',
                'enable',
                'Cisco-IOS-XR-infra-xtc-agent-cfg', False),
            _MetaInfoClassMember('precedence', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('0', '255')], [],
                '''                Precedence value of this PCE
                ''',
                'precedence',
                'Cisco-IOS-XR-infra-xtc-agent-cfg', False),
            ],
            'Cisco-IOS-XR-infra-xtc-agent-cfg',
            'pce-peer',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-infra-xtc-agent-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_segment_routing_ms_cfg',
        ),
    },
    'Sr.TrafficEngineering.Pcc.PcePeers' : {
        'meta_info' : _MetaInfoClass('Sr.TrafficEngineering.Pcc.PcePeers', REFERENCE_CLASS,
            '''PCE peer configuration''',
            False, 
            [
            _MetaInfoClassMember('pce-peer', REFERENCE_LIST, 'PcePeer', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_segment_routing_ms_cfg', 'Sr.TrafficEngineering.Pcc.PcePeers.PcePeer',
                [], [],
                '''                PCE peer
                ''',
                'pce_peer',
                'Cisco-IOS-XR-infra-xtc-agent-cfg', False),
            ],
            'Cisco-IOS-XR-infra-xtc-agent-cfg',
            'pce-peers',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-infra-xtc-agent-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_segment_routing_ms_cfg',
        ),
    },
    'Sr.TrafficEngineering.Pcc.Profiles.Profile.ProfileAutoRoute' : {
        'meta_info' : _MetaInfoClass('Sr.TrafficEngineering.Pcc.Profiles.Profile.ProfileAutoRoute', REFERENCE_CLASS,
            '''Autoroute configuration''',
            False, 
            [
            _MetaInfoClassMember('include-all', ATTRIBUTE, 'Empty', 'empty',
                None, None,
                [], [],
                '''                Include all prefixes to autoroute
                ''',
                'include_all',
                'Cisco-IOS-XR-infra-xtc-agent-cfg', False),
            _MetaInfoClassMember('forward-class', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('0', '7')], [],
                '''                Forward class associated with the policy
                ''',
                'forward_class',
                'Cisco-IOS-XR-infra-xtc-agent-cfg', False),
            ],
            'Cisco-IOS-XR-infra-xtc-agent-cfg',
            'profile-auto-route',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-infra-xtc-agent-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_segment_routing_ms_cfg',
        ),
    },
    'Sr.TrafficEngineering.Pcc.Profiles.Profile' : {
        'meta_info' : _MetaInfoClass('Sr.TrafficEngineering.Pcc.Profiles.Profile', REFERENCE_LIST,
            '''Path profile configuration''',
            False, 
            [
            _MetaInfoClassMember('profile-id', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('1', '65534')], [],
                '''                Profile unique identifier
                ''',
                'profile_id',
                'Cisco-IOS-XR-infra-xtc-agent-cfg', True),
            _MetaInfoClassMember('profile-auto-route', REFERENCE_CLASS, 'ProfileAutoRoute', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_segment_routing_ms_cfg', 'Sr.TrafficEngineering.Pcc.Profiles.Profile.ProfileAutoRoute',
                [], [],
                '''                Autoroute configuration
                ''',
                'profile_auto_route',
                'Cisco-IOS-XR-infra-xtc-agent-cfg', False),
            _MetaInfoClassMember('enable', ATTRIBUTE, 'Empty', 'empty',
                None, None,
                [], [],
                '''                True only
                ''',
                'enable',
                'Cisco-IOS-XR-infra-xtc-agent-cfg', False),
            ],
            'Cisco-IOS-XR-infra-xtc-agent-cfg',
            'profile',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-infra-xtc-agent-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_segment_routing_ms_cfg',
        ),
    },
    'Sr.TrafficEngineering.Pcc.Profiles' : {
        'meta_info' : _MetaInfoClass('Sr.TrafficEngineering.Pcc.Profiles', REFERENCE_CLASS,
            '''Path profiles configuration''',
            False, 
            [
            _MetaInfoClassMember('profile', REFERENCE_LIST, 'Profile', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_segment_routing_ms_cfg', 'Sr.TrafficEngineering.Pcc.Profiles.Profile',
                [], [],
                '''                Path profile configuration
                ''',
                'profile',
                'Cisco-IOS-XR-infra-xtc-agent-cfg', False),
            ],
            'Cisco-IOS-XR-infra-xtc-agent-cfg',
            'profiles',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-infra-xtc-agent-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_segment_routing_ms_cfg',
        ),
    },
    'Sr.TrafficEngineering.Pcc' : {
        'meta_info' : _MetaInfoClass('Sr.TrafficEngineering.Pcc', REFERENCE_CLASS,
            '''Path Computation Client''',
            False, 
            [
            _MetaInfoClassMember('pce-peers', REFERENCE_CLASS, 'PcePeers', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_segment_routing_ms_cfg', 'Sr.TrafficEngineering.Pcc.PcePeers',
                [], [],
                '''                PCE peer configuration
                ''',
                'pce_peers',
                'Cisco-IOS-XR-infra-xtc-agent-cfg', False),
            _MetaInfoClassMember('profiles', REFERENCE_CLASS, 'Profiles', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_segment_routing_ms_cfg', 'Sr.TrafficEngineering.Pcc.Profiles',
                [], [],
                '''                Path profiles configuration
                ''',
                'profiles',
                'Cisco-IOS-XR-infra-xtc-agent-cfg', False),
            _MetaInfoClassMember('dead-timer-interval', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('1', '255')], [],
                '''                Amount of time after which the peer can
                declare this session down, if no PCEP message
                has been received
                ''',
                'dead_timer_interval',
                'Cisco-IOS-XR-infra-xtc-agent-cfg', False),
            _MetaInfoClassMember('pcc-centric', ATTRIBUTE, 'Empty', 'empty',
                None, None,
                [], [],
                '''                Enable PCC centric model, where PCC only
                allows the lowest precedence PCE to initiate
                policies
                ''',
                'pcc_centric',
                'Cisco-IOS-XR-infra-xtc-agent-cfg', False),
            _MetaInfoClassMember('report-all', ATTRIBUTE, 'Empty', 'empty',
                None, None,
                [], [],
                '''                Report all local SR policies to connected PCEP
                peers
                ''',
                'report_all',
                'Cisco-IOS-XR-infra-xtc-agent-cfg', False),
            _MetaInfoClassMember('keepalive-timer-interval', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('0', '255')], [],
                '''                Maximum time between two consecutive PCEP
                messages sent by this node
                ''',
                'keepalive_timer_interval',
                'Cisco-IOS-XR-infra-xtc-agent-cfg', False),
            _MetaInfoClassMember('initiated-state-interval', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('15', '14400')], [],
                '''                Amount of time a PCE Initiated policy can
                remain orphan
                ''',
                'initiated_state_interval',
                'Cisco-IOS-XR-infra-xtc-agent-cfg', False),
            _MetaInfoClassMember('source-address', REFERENCE_UNION, 'str', 'inet:ip-address-no-zone',
                None, None,
                [], [],
                '''                Local source IP address to use on PCEP
                sessions
                ''',
                'source_address',
                'Cisco-IOS-XR-infra-xtc-agent-cfg', False, [
                    _MetaInfoClassMember('source-address', ATTRIBUTE, 'str', 'inet:ipv4-address-no-zone',
                        None, None,
                        [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'],
                        '''                        Local source IP address to use on PCEP
                        sessions
                        ''',
                        'source_address',
                        'Cisco-IOS-XR-infra-xtc-agent-cfg', False),
                    _MetaInfoClassMember('source-address', ATTRIBUTE, 'str', 'inet:ipv6-address-no-zone',
                        None, None,
                        [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'],
                        '''                        Local source IP address to use on PCEP
                        sessions
                        ''',
                        'source_address',
                        'Cisco-IOS-XR-infra-xtc-agent-cfg', False),
                ]),
            _MetaInfoClassMember('enable', ATTRIBUTE, 'Empty', 'empty',
                None, None,
                [], [],
                '''                PCC Enable
                ''',
                'enable',
                'Cisco-IOS-XR-infra-xtc-agent-cfg', False),
            _MetaInfoClassMember('initiated-orphan-interval', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('10', '180')], [],
                '''                Amount of time that a policy will be owned by
                a PCE after that PCE has gone down
                ''',
                'initiated_orphan_interval',
                'Cisco-IOS-XR-infra-xtc-agent-cfg', False),
            _MetaInfoClassMember('delegation-timeout', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('0', '3600')], [],
                '''                The maximum time delegated SR-TE policies can
                remain up without an active connection to a
                PCE
                ''',
                'delegation_timeout',
                'Cisco-IOS-XR-infra-xtc-agent-cfg', False),
            ],
            'Cisco-IOS-XR-infra-xtc-agent-cfg',
            'pcc',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-infra-xtc-agent-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_segment_routing_ms_cfg',
        ),
    },
    'Sr.TrafficEngineering.AffinityMaps.AffinityMap' : {
        'meta_info' : _MetaInfoClass('Sr.TrafficEngineering.AffinityMaps.AffinityMap', REFERENCE_LIST,
            '''Affinity-map entry''',
            False, 
            [
            _MetaInfoClassMember('affinity-name', ATTRIBUTE, 'str', 'xr:Cisco-ios-xr-string',
                None, None,
                [(1, 32)], [],
                '''                Affinity-map bit-position
                ''',
                'affinity_name',
                'Cisco-IOS-XR-infra-xtc-agent-cfg', True),
            _MetaInfoClassMember('bit-position', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('0', '255')], [],
                '''                Affinity-map bit-position
                ''',
                'bit_position',
                'Cisco-IOS-XR-infra-xtc-agent-cfg', False, is_mandatory=True),
            ],
            'Cisco-IOS-XR-infra-xtc-agent-cfg',
            'affinity-map',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-infra-xtc-agent-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_segment_routing_ms_cfg',
        ),
    },
    'Sr.TrafficEngineering.AffinityMaps' : {
        'meta_info' : _MetaInfoClass('Sr.TrafficEngineering.AffinityMaps', REFERENCE_CLASS,
            '''Affinity-map configuration''',
            False, 
            [
            _MetaInfoClassMember('affinity-map', REFERENCE_LIST, 'AffinityMap', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_segment_routing_ms_cfg', 'Sr.TrafficEngineering.AffinityMaps.AffinityMap',
                [], [],
                '''                Affinity-map entry
                ''',
                'affinity_map',
                'Cisco-IOS-XR-infra-xtc-agent-cfg', False),
            ],
            'Cisco-IOS-XR-infra-xtc-agent-cfg',
            'affinity-maps',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-infra-xtc-agent-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_segment_routing_ms_cfg',
        ),
    },
    'Sr.TrafficEngineering.CandidatePathTypes.CandidatePathType.CandidatePathTypeAllOrCandidatePathTypeLocalOrCandidatePathTypeBgpOdnOrCandidatePathTypeBgpSrteOrCandidatePathTypePcep.SourceAddress' : {
        'meta_info' : _MetaInfoClass('Sr.TrafficEngineering.CandidatePathTypes.CandidatePathType.CandidatePathTypeAllOrCandidatePathTypeLocalOrCandidatePathTypeBgpOdnOrCandidatePathTypeBgpSrteOrCandidatePathTypePcep.SourceAddress', REFERENCE_CLASS,
            '''Source address of a candidate path. EndPointType
, Source''',
            False, 
            [
            _MetaInfoClassMember('ip-address-type', REFERENCE_ENUM_CLASS, 'XtcEndPoint', 'Xtc-end-point',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_agent_cfg', 'XtcEndPoint',
                [], [],
                '''                IP address type
                ''',
                'ip_address_type',
                'Cisco-IOS-XR-infra-xtc-agent-cfg', False, is_mandatory=True),
            _MetaInfoClassMember('source-address', REFERENCE_UNION, 'str', 'inet:ip-address-no-zone',
                None, None,
                [], [],
                '''                Source address
                ''',
                'source_address',
                'Cisco-IOS-XR-infra-xtc-agent-cfg', False, [
                    _MetaInfoClassMember('source-address', ATTRIBUTE, 'str', 'inet:ipv4-address-no-zone',
                        None, None,
                        [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'],
                        '''                        Source address
                        ''',
                        'source_address',
                        'Cisco-IOS-XR-infra-xtc-agent-cfg', False, is_mandatory=True),
                    _MetaInfoClassMember('source-address', ATTRIBUTE, 'str', 'inet:ipv6-address-no-zone',
                        None, None,
                        [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'],
                        '''                        Source address
                        ''',
                        'source_address',
                        'Cisco-IOS-XR-infra-xtc-agent-cfg', False, is_mandatory=True),
                ], is_mandatory=True),
            ],
            'Cisco-IOS-XR-infra-xtc-agent-cfg',
            'source-address',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-infra-xtc-agent-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_segment_routing_ms_cfg',
            is_presence=True,
        ),
    },
    'Sr.TrafficEngineering.CandidatePathTypes.CandidatePathType.CandidatePathTypeAllOrCandidatePathTypeLocalOrCandidatePathTypeBgpOdnOrCandidatePathTypeBgpSrteOrCandidatePathTypePcep' : {
        'meta_info' : _MetaInfoClass('Sr.TrafficEngineering.CandidatePathTypes.CandidatePathType.CandidatePathTypeAllOrCandidatePathTypeLocalOrCandidatePathTypeBgpOdnOrCandidatePathTypeBgpSrteOrCandidatePathTypePcep', REFERENCE_CLASS,
            '''candidate path type all or candidate path
type local or candidate path type bgp odn or
candidate path type bgp srte or candidate
path type pcep''',
            False, 
            [
            _MetaInfoClassMember('source-address', REFERENCE_CLASS, 'SourceAddress', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_segment_routing_ms_cfg', 'Sr.TrafficEngineering.CandidatePathTypes.CandidatePathType.CandidatePathTypeAllOrCandidatePathTypeLocalOrCandidatePathTypeBgpOdnOrCandidatePathTypeBgpSrteOrCandidatePathTypePcep.SourceAddress',
                [], [],
                '''                Source address of a candidate path. EndPointType
                , Source
                ''',
                'source_address',
                'Cisco-IOS-XR-infra-xtc-agent-cfg', False, is_presence=True),
            _MetaInfoClassMember('enable', ATTRIBUTE, 'Empty', 'empty',
                None, None,
                [], [],
                '''                True only
                ''',
                'enable',
                'Cisco-IOS-XR-infra-xtc-agent-cfg', False),
            ],
            'Cisco-IOS-XR-infra-xtc-agent-cfg',
            'candidate-path-type-all-or-candidate-path-type-local-or-candidate-path-type-bgp-odn-or-candidate-path-type-bgp-srte-or-candidate-path-type-pcep',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-infra-xtc-agent-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_segment_routing_ms_cfg',
            is_presence=True,
            has_when=True,
        ),
    },
    'Sr.TrafficEngineering.CandidatePathTypes.CandidatePathType' : {
        'meta_info' : _MetaInfoClass('Sr.TrafficEngineering.CandidatePathTypes.CandidatePathType', REFERENCE_LIST,
            '''Configurations for candidate paths of specific
type.''',
            False, 
            [
            _MetaInfoClassMember('candidate-path-type', REFERENCE_ENUM_CLASS, 'XtcCpath', 'Xtc-cpath',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_agent_cfg', 'XtcCpath',
                [], [],
                '''                Candidate-path type
                ''',
                'candidate_path_type',
                'Cisco-IOS-XR-infra-xtc-agent-cfg', True),
            _MetaInfoClassMember('candidate-path-type-all-or-candidate-path-type-local-or-candidate-path-type-bgp-odn-or-candidate-path-type-bgp-srte-or-candidate-path-type-pcep', REFERENCE_CLASS, 'CandidatePathTypeAllOrCandidatePathTypeLocalOrCandidatePathTypeBgpOdnOrCandidatePathTypeBgpSrteOrCandidatePathTypePcep', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_segment_routing_ms_cfg', 'Sr.TrafficEngineering.CandidatePathTypes.CandidatePathType.CandidatePathTypeAllOrCandidatePathTypeLocalOrCandidatePathTypeBgpOdnOrCandidatePathTypeBgpSrteOrCandidatePathTypePcep',
                [], [],
                '''                candidate path type all or candidate path
                type local or candidate path type bgp odn or
                candidate path type bgp srte or candidate
                path type pcep
                ''',
                'candidate_path_type_all_or_candidate_path_type_local_or_candidate_path_type_bgp_odn_or_candidate_path_type_bgp_srte_or_candidate_path_type_pcep',
                'Cisco-IOS-XR-infra-xtc-agent-cfg', False, is_presence=True, has_when=True),
            ],
            'Cisco-IOS-XR-infra-xtc-agent-cfg',
            'candidate-path-type',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-infra-xtc-agent-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_segment_routing_ms_cfg',
            has_must=True,
        ),
    },
    'Sr.TrafficEngineering.CandidatePathTypes' : {
        'meta_info' : _MetaInfoClass('Sr.TrafficEngineering.CandidatePathTypes', REFERENCE_CLASS,
            '''Configurations for candidate paths.''',
            False, 
            [
            _MetaInfoClassMember('candidate-path-type', REFERENCE_LIST, 'CandidatePathType', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_segment_routing_ms_cfg', 'Sr.TrafficEngineering.CandidatePathTypes.CandidatePathType',
                [], [],
                '''                Configurations for candidate paths of specific
                type.
                ''',
                'candidate_path_type',
                'Cisco-IOS-XR-infra-xtc-agent-cfg', False, has_must=True),
            ],
            'Cisco-IOS-XR-infra-xtc-agent-cfg',
            'candidate-path-types',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-infra-xtc-agent-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_segment_routing_ms_cfg',
        ),
    },
    'Sr.TrafficEngineering' : {
        'meta_info' : _MetaInfoClass('Sr.TrafficEngineering', REFERENCE_CLASS,
            '''Traffic Engineering configuration data''',
            False, 
            [
            _MetaInfoClassMember('out-of-resources', REFERENCE_CLASS, 'OutOfResources', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_segment_routing_ms_cfg', 'Sr.TrafficEngineering.OutOfResources',
                [], [],
                '''                SR-TE out-of-resources handling configuration
                ''',
                'out_of_resources',
                'Cisco-IOS-XR-infra-xtc-agent-cfg', False),
            _MetaInfoClassMember('on-demand-colors', REFERENCE_CLASS, 'OnDemandColors', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_segment_routing_ms_cfg', 'Sr.TrafficEngineering.OnDemandColors',
                [], [],
                '''                On-demand color configuration
                ''',
                'on_demand_colors',
                'Cisco-IOS-XR-infra-xtc-agent-cfg', False),
            _MetaInfoClassMember('segments', REFERENCE_CLASS, 'Segments', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_segment_routing_ms_cfg', 'Sr.TrafficEngineering.Segments',
                [], [],
                '''                Segment-lists configuration
                ''',
                'segments',
                'Cisco-IOS-XR-infra-xtc-agent-cfg', False),
            _MetaInfoClassMember('logging', REFERENCE_CLASS, 'Logging', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_segment_routing_ms_cfg', 'Sr.TrafficEngineering.Logging',
                [], [],
                '''                Logging configuration
                ''',
                'logging',
                'Cisco-IOS-XR-infra-xtc-agent-cfg', False),
            _MetaInfoClassMember('timers', REFERENCE_CLASS, 'Timers', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_segment_routing_ms_cfg', 'Sr.TrafficEngineering.Timers',
                [], [],
                '''                SR-TE timers configuration
                ''',
                'timers',
                'Cisco-IOS-XR-infra-xtc-agent-cfg', False),
            _MetaInfoClassMember('binding-sid-rules', REFERENCE_CLASS, 'BindingSidRules', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_segment_routing_ms_cfg', 'Sr.TrafficEngineering.BindingSidRules',
                [], [],
                '''                Binding sid rules
                ''',
                'binding_sid_rules',
                'Cisco-IOS-XR-infra-xtc-agent-cfg', False),
            _MetaInfoClassMember('policies', REFERENCE_CLASS, 'Policies', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_segment_routing_ms_cfg', 'Sr.TrafficEngineering.Policies',
                [], [],
                '''                Policy configuration
                ''',
                'policies',
                'Cisco-IOS-XR-infra-xtc-agent-cfg', False),
            _MetaInfoClassMember('srte-interfaces', REFERENCE_CLASS, 'SrteInterfaces', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_segment_routing_ms_cfg', 'Sr.TrafficEngineering.SrteInterfaces',
                [], [],
                '''                SR-TE interfaces
                ''',
                'srte_interfaces',
                'Cisco-IOS-XR-infra-xtc-agent-cfg', False),
            _MetaInfoClassMember('pcc', REFERENCE_CLASS, 'Pcc', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_segment_routing_ms_cfg', 'Sr.TrafficEngineering.Pcc',
                [], [],
                '''                Path Computation Client
                ''',
                'pcc',
                'Cisco-IOS-XR-infra-xtc-agent-cfg', False),
            _MetaInfoClassMember('affinity-maps', REFERENCE_CLASS, 'AffinityMaps', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_segment_routing_ms_cfg', 'Sr.TrafficEngineering.AffinityMaps',
                [], [],
                '''                Affinity-map configuration
                ''',
                'affinity_maps',
                'Cisco-IOS-XR-infra-xtc-agent-cfg', False),
            _MetaInfoClassMember('candidate-path-types', REFERENCE_CLASS, 'CandidatePathTypes', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_segment_routing_ms_cfg', 'Sr.TrafficEngineering.CandidatePathTypes',
                [], [],
                '''                Configurations for candidate paths.
                ''',
                'candidate_path_types',
                'Cisco-IOS-XR-infra-xtc-agent-cfg', False),
            _MetaInfoClassMember('te-latency', ATTRIBUTE, 'Empty', 'empty',
                None, None,
                [], [],
                '''                Use TE-latency algorithm
                ''',
                'te_latency',
                'Cisco-IOS-XR-infra-xtc-agent-cfg', False),
            _MetaInfoClassMember('maximum-sid-depth', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('1', '255')], [],
                '''                Maximum SID Depth Configuration
                ''',
                'maximum_sid_depth',
                'Cisco-IOS-XR-infra-xtc-agent-cfg', False),
            _MetaInfoClassMember('enable', ATTRIBUTE, 'Empty', 'empty',
                None, None,
                [], [],
                '''                True only
                ''',
                'enable',
                'Cisco-IOS-XR-infra-xtc-agent-cfg', False),
            ],
            'Cisco-IOS-XR-infra-xtc-agent-cfg',
            'traffic-engineering',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-infra-xtc-agent-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_segment_routing_ms_cfg',
        ),
    },
    'Sr' : {
        'meta_info' : _MetaInfoClass('Sr', REFERENCE_CLASS,
            '''Segment Routing''',
            False, 
            [
            _MetaInfoClassMember('local-block', REFERENCE_CLASS, 'LocalBlock', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_segment_routing_ms_cfg', 'Sr.LocalBlock',
                [], [],
                '''                Segment Routing Local Block of Labels
                ''',
                'local_block',
                'Cisco-IOS-XR-segment-routing-ms-cfg', False, is_presence=True),
            _MetaInfoClassMember('mappings', REFERENCE_CLASS, 'Mappings', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_segment_routing_ms_cfg', 'Sr.Mappings',
                [], [],
                '''                Mapping Server
                ''',
                'mappings',
                'Cisco-IOS-XR-segment-routing-ms-cfg', False),
            _MetaInfoClassMember('adjacency-sid', REFERENCE_CLASS, 'AdjacencySid', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_segment_routing_ms_cfg', 'Sr.AdjacencySid',
                [], [],
                '''                Segment Routing Adjacency SID
                ''',
                'adjacency_sid',
                'Cisco-IOS-XR-segment-routing-ms-cfg', False),
            _MetaInfoClassMember('global-block', REFERENCE_CLASS, 'GlobalBlock', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_segment_routing_ms_cfg', 'Sr.GlobalBlock',
                [], [],
                '''                Global Block Segment Routing
                ''',
                'global_block',
                'Cisco-IOS-XR-segment-routing-ms-cfg', False, is_presence=True),
            _MetaInfoClassMember('enable', ATTRIBUTE, 'Empty', 'empty',
                None, None,
                [], [],
                '''                enable SR
                ''',
                'enable',
                'Cisco-IOS-XR-segment-routing-ms-cfg', False),
            _MetaInfoClassMember('srv6', REFERENCE_CLASS, 'Srv6', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_segment_routing_ms_cfg', 'Sr.Srv6',
                [], [],
                '''                Segment Routing with IPv6 dataplane
                ''',
                'srv6',
                'Cisco-IOS-XR-segment-routing-srv6-cfg', False),
            _MetaInfoClassMember('traffic-engineering', REFERENCE_CLASS, 'TrafficEngineering', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_segment_routing_ms_cfg', 'Sr.TrafficEngineering',
                [], [],
                '''                Traffic Engineering configuration data
                ''',
                'traffic_engineering',
                'Cisco-IOS-XR-infra-xtc-agent-cfg', False),
            ],
            'Cisco-IOS-XR-segment-routing-ms-cfg',
            'sr',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-segment-routing-ms-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_segment_routing_ms_cfg',
        ),
    },
}
_meta_table['Sr.Mappings.Mapping']['meta_info'].parent =_meta_table['Sr.Mappings']['meta_info']
_meta_table['Sr.AdjacencySid.Interfaces.Interface.AddressFamilies.AddressFamily.NextHops.NextHop.L2AdjacencySid']['meta_info'].parent =_meta_table['Sr.AdjacencySid.Interfaces.Interface.AddressFamilies.AddressFamily.NextHops.NextHop']['meta_info']
_meta_table['Sr.AdjacencySid.Interfaces.Interface.AddressFamilies.AddressFamily.NextHops.NextHop']['meta_info'].parent =_meta_table['Sr.AdjacencySid.Interfaces.Interface.AddressFamilies.AddressFamily.NextHops']['meta_info']
_meta_table['Sr.AdjacencySid.Interfaces.Interface.AddressFamilies.AddressFamily.NextHops']['meta_info'].parent =_meta_table['Sr.AdjacencySid.Interfaces.Interface.AddressFamilies.AddressFamily']['meta_info']
_meta_table['Sr.AdjacencySid.Interfaces.Interface.AddressFamilies.AddressFamily']['meta_info'].parent =_meta_table['Sr.AdjacencySid.Interfaces.Interface.AddressFamilies']['meta_info']
_meta_table['Sr.AdjacencySid.Interfaces.Interface.AddressFamilies']['meta_info'].parent =_meta_table['Sr.AdjacencySid.Interfaces.Interface']['meta_info']
_meta_table['Sr.AdjacencySid.Interfaces.Interface']['meta_info'].parent =_meta_table['Sr.AdjacencySid.Interfaces']['meta_info']
_meta_table['Sr.AdjacencySid.Interfaces']['meta_info'].parent =_meta_table['Sr.AdjacencySid']['meta_info']
_meta_table['Sr.Srv6.Locators.Locators_.Locator.Prefix']['meta_info'].parent =_meta_table['Sr.Srv6.Locators.Locators_.Locator']['meta_info']
_meta_table['Sr.Srv6.Locators.Locators_.Locator']['meta_info'].parent =_meta_table['Sr.Srv6.Locators.Locators_']['meta_info']
_meta_table['Sr.Srv6.Locators.Locators_']['meta_info'].parent =_meta_table['Sr.Srv6.Locators']['meta_info']
_meta_table['Sr.Srv6.Encapsulation.HopLimit']['meta_info'].parent =_meta_table['Sr.Srv6.Encapsulation']['meta_info']
_meta_table['Sr.Srv6.Logging']['meta_info'].parent =_meta_table['Sr.Srv6']['meta_info']
_meta_table['Sr.Srv6.Locators']['meta_info'].parent =_meta_table['Sr.Srv6']['meta_info']
_meta_table['Sr.Srv6.Encapsulation']['meta_info'].parent =_meta_table['Sr.Srv6']['meta_info']
_meta_table['Sr.TrafficEngineering.OnDemandColors.OnDemandColor.OnDemandColorDynMpls.OnDemandColorDynMplsMetric.MetricMargin']['meta_info'].parent =_meta_table['Sr.TrafficEngineering.OnDemandColors.OnDemandColor.OnDemandColorDynMpls.OnDemandColorDynMplsMetric']['meta_info']
_meta_table['Sr.TrafficEngineering.OnDemandColors.OnDemandColor.OnDemandColorDynMpls.AffinityRules.AffinityRule.AffinityName']['meta_info'].parent =_meta_table['Sr.TrafficEngineering.OnDemandColors.OnDemandColor.OnDemandColorDynMpls.AffinityRules.AffinityRule']['meta_info']
_meta_table['Sr.TrafficEngineering.OnDemandColors.OnDemandColor.OnDemandColorDynMpls.AffinityRules.AffinityRule']['meta_info'].parent =_meta_table['Sr.TrafficEngineering.OnDemandColors.OnDemandColor.OnDemandColorDynMpls.AffinityRules']['meta_info']
_meta_table['Sr.TrafficEngineering.OnDemandColors.OnDemandColor.OnDemandColorDynMpls.OnDemandColorDynMplsMetric']['meta_info'].parent =_meta_table['Sr.TrafficEngineering.OnDemandColors.OnDemandColor.OnDemandColorDynMpls']['meta_info']
_meta_table['Sr.TrafficEngineering.OnDemandColors.OnDemandColor.OnDemandColorDynMpls.OnDemandColorDynMplsPce']['meta_info'].parent =_meta_table['Sr.TrafficEngineering.OnDemandColors.OnDemandColor.OnDemandColorDynMpls']['meta_info']
_meta_table['Sr.TrafficEngineering.OnDemandColors.OnDemandColor.OnDemandColorDynMpls.DisjointPath']['meta_info'].parent =_meta_table['Sr.TrafficEngineering.OnDemandColors.OnDemandColor.OnDemandColorDynMpls']['meta_info']
_meta_table['Sr.TrafficEngineering.OnDemandColors.OnDemandColor.OnDemandColorDynMpls.AffinityRules']['meta_info'].parent =_meta_table['Sr.TrafficEngineering.OnDemandColors.OnDemandColor.OnDemandColorDynMpls']['meta_info']
_meta_table['Sr.TrafficEngineering.OnDemandColors.OnDemandColor.OnDemandColorDynMpls']['meta_info'].parent =_meta_table['Sr.TrafficEngineering.OnDemandColors.OnDemandColor']['meta_info']
_meta_table['Sr.TrafficEngineering.OnDemandColors.OnDemandColor.SourceAddress']['meta_info'].parent =_meta_table['Sr.TrafficEngineering.OnDemandColors.OnDemandColor']['meta_info']
_meta_table['Sr.TrafficEngineering.OnDemandColors.OnDemandColor']['meta_info'].parent =_meta_table['Sr.TrafficEngineering.OnDemandColors']['meta_info']
_meta_table['Sr.TrafficEngineering.Segments.Segment.Segments_.Segment_']['meta_info'].parent =_meta_table['Sr.TrafficEngineering.Segments.Segment.Segments_']['meta_info']
_meta_table['Sr.TrafficEngineering.Segments.Segment.Segments_']['meta_info'].parent =_meta_table['Sr.TrafficEngineering.Segments.Segment']['meta_info']
_meta_table['Sr.TrafficEngineering.Segments.Segment']['meta_info'].parent =_meta_table['Sr.TrafficEngineering.Segments']['meta_info']
_meta_table['Sr.TrafficEngineering.BindingSidRules.Explicit']['meta_info'].parent =_meta_table['Sr.TrafficEngineering.BindingSidRules']['meta_info']
_meta_table['Sr.TrafficEngineering.BindingSidRules.DynamicBindingSidRules']['meta_info'].parent =_meta_table['Sr.TrafficEngineering.BindingSidRules']['meta_info']
_meta_table['Sr.TrafficEngineering.Policies.Policy.Steering.Applications.Application']['meta_info'].parent =_meta_table['Sr.TrafficEngineering.Policies.Policy.Steering.Applications']['meta_info']
_meta_table['Sr.TrafficEngineering.Policies.Policy.Steering.Applications']['meta_info'].parent =_meta_table['Sr.TrafficEngineering.Policies.Policy.Steering']['meta_info']
_meta_table['Sr.TrafficEngineering.Policies.Policy.AutoRoute.IncludePrefixes.IncludePrefix']['meta_info'].parent =_meta_table['Sr.TrafficEngineering.Policies.Policy.AutoRoute.IncludePrefixes']['meta_info']
_meta_table['Sr.TrafficEngineering.Policies.Policy.AutoRoute.AutoRouteMetric']['meta_info'].parent =_meta_table['Sr.TrafficEngineering.Policies.Policy.AutoRoute']['meta_info']
_meta_table['Sr.TrafficEngineering.Policies.Policy.AutoRoute.IncludePrefixes']['meta_info'].parent =_meta_table['Sr.TrafficEngineering.Policies.Policy.AutoRoute']['meta_info']
_meta_table['Sr.TrafficEngineering.Policies.Policy.CandidatePaths.Preferences.Preference.Constraints.AffinityRules.AffinityRule.AffinityName']['meta_info'].parent =_meta_table['Sr.TrafficEngineering.Policies.Policy.CandidatePaths.Preferences.Preference.Constraints.AffinityRules.AffinityRule']['meta_info']
_meta_table['Sr.TrafficEngineering.Policies.Policy.CandidatePaths.Preferences.Preference.Constraints.AffinityRules.AffinityRule']['meta_info'].parent =_meta_table['Sr.TrafficEngineering.Policies.Policy.CandidatePaths.Preferences.Preference.Constraints.AffinityRules']['meta_info']
_meta_table['Sr.TrafficEngineering.Policies.Policy.CandidatePaths.Preferences.Preference.Constraints.DisjointPath']['meta_info'].parent =_meta_table['Sr.TrafficEngineering.Policies.Policy.CandidatePaths.Preferences.Preference.Constraints']['meta_info']
_meta_table['Sr.TrafficEngineering.Policies.Policy.CandidatePaths.Preferences.Preference.Constraints.SegmentRules']['meta_info'].parent =_meta_table['Sr.TrafficEngineering.Policies.Policy.CandidatePaths.Preferences.Preference.Constraints']['meta_info']
_meta_table['Sr.TrafficEngineering.Policies.Policy.CandidatePaths.Preferences.Preference.Constraints.AffinityRules']['meta_info'].parent =_meta_table['Sr.TrafficEngineering.Policies.Policy.CandidatePaths.Preferences.Preference.Constraints']['meta_info']
_meta_table['Sr.TrafficEngineering.Policies.Policy.CandidatePaths.Preferences.Preference.PathInfos.PathInfo.Metric.MetricMargin']['meta_info'].parent =_meta_table['Sr.TrafficEngineering.Policies.Policy.CandidatePaths.Preferences.Preference.PathInfos.PathInfo.Metric']['meta_info']
_meta_table['Sr.TrafficEngineering.Policies.Policy.CandidatePaths.Preferences.Preference.PathInfos.PathInfo.Metric']['meta_info'].parent =_meta_table['Sr.TrafficEngineering.Policies.Policy.CandidatePaths.Preferences.Preference.PathInfos.PathInfo']['meta_info']
_meta_table['Sr.TrafficEngineering.Policies.Policy.CandidatePaths.Preferences.Preference.PathInfos.PathInfo.Pcep']['meta_info'].parent =_meta_table['Sr.TrafficEngineering.Policies.Policy.CandidatePaths.Preferences.Preference.PathInfos.PathInfo']['meta_info']
_meta_table['Sr.TrafficEngineering.Policies.Policy.CandidatePaths.Preferences.Preference.PathInfos.PathInfo']['meta_info'].parent =_meta_table['Sr.TrafficEngineering.Policies.Policy.CandidatePaths.Preferences.Preference.PathInfos']['meta_info']
_meta_table['Sr.TrafficEngineering.Policies.Policy.CandidatePaths.Preferences.Preference.Constraints']['meta_info'].parent =_meta_table['Sr.TrafficEngineering.Policies.Policy.CandidatePaths.Preferences.Preference']['meta_info']
_meta_table['Sr.TrafficEngineering.Policies.Policy.CandidatePaths.Preferences.Preference.PathInfos']['meta_info'].parent =_meta_table['Sr.TrafficEngineering.Policies.Policy.CandidatePaths.Preferences.Preference']['meta_info']
_meta_table['Sr.TrafficEngineering.Policies.Policy.CandidatePaths.Preferences.Preference']['meta_info'].parent =_meta_table['Sr.TrafficEngineering.Policies.Policy.CandidatePaths.Preferences']['meta_info']
_meta_table['Sr.TrafficEngineering.Policies.Policy.CandidatePaths.Preferences']['meta_info'].parent =_meta_table['Sr.TrafficEngineering.Policies.Policy.CandidatePaths']['meta_info']
_meta_table['Sr.TrafficEngineering.Policies.Policy.Steering']['meta_info'].parent =_meta_table['Sr.TrafficEngineering.Policies.Policy']['meta_info']
_meta_table['Sr.TrafficEngineering.Policies.Policy.BindingSid']['meta_info'].parent =_meta_table['Sr.TrafficEngineering.Policies.Policy']['meta_info']
_meta_table['Sr.TrafficEngineering.Policies.Policy.PolicyColorEndpoint']['meta_info'].parent =_meta_table['Sr.TrafficEngineering.Policies.Policy']['meta_info']
_meta_table['Sr.TrafficEngineering.Policies.Policy.AutoRoute']['meta_info'].parent =_meta_table['Sr.TrafficEngineering.Policies.Policy']['meta_info']
_meta_table['Sr.TrafficEngineering.Policies.Policy.CandidatePaths']['meta_info'].parent =_meta_table['Sr.TrafficEngineering.Policies.Policy']['meta_info']
_meta_table['Sr.TrafficEngineering.Policies.Policy.SourceAddress']['meta_info'].parent =_meta_table['Sr.TrafficEngineering.Policies.Policy']['meta_info']
_meta_table['Sr.TrafficEngineering.Policies.Policy']['meta_info'].parent =_meta_table['Sr.TrafficEngineering.Policies']['meta_info']
_meta_table['Sr.TrafficEngineering.SrteInterfaces.SrteInterface.InterfaceAffinities.InterfaceAffinity']['meta_info'].parent =_meta_table['Sr.TrafficEngineering.SrteInterfaces.SrteInterface.InterfaceAffinities']['meta_info']
_meta_table['Sr.TrafficEngineering.SrteInterfaces.SrteInterface.InterfaceAffinities']['meta_info'].parent =_meta_table['Sr.TrafficEngineering.SrteInterfaces.SrteInterface']['meta_info']
_meta_table['Sr.TrafficEngineering.SrteInterfaces.SrteInterface']['meta_info'].parent =_meta_table['Sr.TrafficEngineering.SrteInterfaces']['meta_info']
_meta_table['Sr.TrafficEngineering.Pcc.PcePeers.PcePeer']['meta_info'].parent =_meta_table['Sr.TrafficEngineering.Pcc.PcePeers']['meta_info']
_meta_table['Sr.TrafficEngineering.Pcc.Profiles.Profile.ProfileAutoRoute']['meta_info'].parent =_meta_table['Sr.TrafficEngineering.Pcc.Profiles.Profile']['meta_info']
_meta_table['Sr.TrafficEngineering.Pcc.Profiles.Profile']['meta_info'].parent =_meta_table['Sr.TrafficEngineering.Pcc.Profiles']['meta_info']
_meta_table['Sr.TrafficEngineering.Pcc.PcePeers']['meta_info'].parent =_meta_table['Sr.TrafficEngineering.Pcc']['meta_info']
_meta_table['Sr.TrafficEngineering.Pcc.Profiles']['meta_info'].parent =_meta_table['Sr.TrafficEngineering.Pcc']['meta_info']
_meta_table['Sr.TrafficEngineering.AffinityMaps.AffinityMap']['meta_info'].parent =_meta_table['Sr.TrafficEngineering.AffinityMaps']['meta_info']
_meta_table['Sr.TrafficEngineering.CandidatePathTypes.CandidatePathType.CandidatePathTypeAllOrCandidatePathTypeLocalOrCandidatePathTypeBgpOdnOrCandidatePathTypeBgpSrteOrCandidatePathTypePcep.SourceAddress']['meta_info'].parent =_meta_table['Sr.TrafficEngineering.CandidatePathTypes.CandidatePathType.CandidatePathTypeAllOrCandidatePathTypeLocalOrCandidatePathTypeBgpOdnOrCandidatePathTypeBgpSrteOrCandidatePathTypePcep']['meta_info']
_meta_table['Sr.TrafficEngineering.CandidatePathTypes.CandidatePathType.CandidatePathTypeAllOrCandidatePathTypeLocalOrCandidatePathTypeBgpOdnOrCandidatePathTypeBgpSrteOrCandidatePathTypePcep']['meta_info'].parent =_meta_table['Sr.TrafficEngineering.CandidatePathTypes.CandidatePathType']['meta_info']
_meta_table['Sr.TrafficEngineering.CandidatePathTypes.CandidatePathType']['meta_info'].parent =_meta_table['Sr.TrafficEngineering.CandidatePathTypes']['meta_info']
_meta_table['Sr.TrafficEngineering.OutOfResources']['meta_info'].parent =_meta_table['Sr.TrafficEngineering']['meta_info']
_meta_table['Sr.TrafficEngineering.OnDemandColors']['meta_info'].parent =_meta_table['Sr.TrafficEngineering']['meta_info']
_meta_table['Sr.TrafficEngineering.Segments']['meta_info'].parent =_meta_table['Sr.TrafficEngineering']['meta_info']
_meta_table['Sr.TrafficEngineering.Logging']['meta_info'].parent =_meta_table['Sr.TrafficEngineering']['meta_info']
_meta_table['Sr.TrafficEngineering.Timers']['meta_info'].parent =_meta_table['Sr.TrafficEngineering']['meta_info']
_meta_table['Sr.TrafficEngineering.BindingSidRules']['meta_info'].parent =_meta_table['Sr.TrafficEngineering']['meta_info']
_meta_table['Sr.TrafficEngineering.Policies']['meta_info'].parent =_meta_table['Sr.TrafficEngineering']['meta_info']
_meta_table['Sr.TrafficEngineering.SrteInterfaces']['meta_info'].parent =_meta_table['Sr.TrafficEngineering']['meta_info']
_meta_table['Sr.TrafficEngineering.Pcc']['meta_info'].parent =_meta_table['Sr.TrafficEngineering']['meta_info']
_meta_table['Sr.TrafficEngineering.AffinityMaps']['meta_info'].parent =_meta_table['Sr.TrafficEngineering']['meta_info']
_meta_table['Sr.TrafficEngineering.CandidatePathTypes']['meta_info'].parent =_meta_table['Sr.TrafficEngineering']['meta_info']
_meta_table['Sr.LocalBlock']['meta_info'].parent =_meta_table['Sr']['meta_info']
_meta_table['Sr.Mappings']['meta_info'].parent =_meta_table['Sr']['meta_info']
_meta_table['Sr.AdjacencySid']['meta_info'].parent =_meta_table['Sr']['meta_info']
_meta_table['Sr.GlobalBlock']['meta_info'].parent =_meta_table['Sr']['meta_info']
_meta_table['Sr.Srv6']['meta_info'].parent =_meta_table['Sr']['meta_info']
_meta_table['Sr.TrafficEngineering']['meta_info'].parent =_meta_table['Sr']['meta_info']
