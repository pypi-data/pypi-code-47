
'''
This is auto-generated file,
which includes metadata for module Cisco_IOS_XR_infra_serg_cfg
'''

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_LIST, REFERENCE_LEAFLIST, REFERENCE_BITS, REFERENCE_UNION
from ydk._core._dm_meta_info import REFERENCE_CLASS, REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, ANYXML_CLASS
from ydk._core._importer import _yang_ns

_meta_table = {
    'SessionRedundancyGroupRole' : _MetaInfoEnum('SessionRedundancyGroupRole',
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_serg_cfg', 'SessionRedundancyGroupRole',
        '''Session redundancy group role''',
        {
            'master':'master',
            'slave':'slave',
        }, 'Cisco-IOS-XR-infra-serg-cfg', _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-infra-serg-cfg']),
    'SergAddrFamily' : _MetaInfoEnum('SergAddrFamily',
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_serg_cfg', 'SergAddrFamily',
        '''Serg addr family''',
        {
            'ipv4':'ipv4',
            'ipv6':'ipv6',
        }, 'Cisco-IOS-XR-infra-serg-cfg', _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-infra-serg-cfg']),
    'SessionRedundancy.Groups.Group.Peer.Ipaddress' : {
        'meta_info' : _MetaInfoClass('SessionRedundancy.Groups.Group.Peer.Ipaddress', REFERENCE_CLASS,
            '''IPv4 or IPv6 Address of SERG Peer''',
            False, 
            [
            _MetaInfoClassMember('address-family', REFERENCE_ENUM_CLASS, 'SergAddrFamily', 'Serg-addr-family',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_serg_cfg', 'SergAddrFamily',
                [], [],
                '''                Type of IPv4/IPv6 address
                ''',
                'address_family',
                'Cisco-IOS-XR-infra-serg-cfg', False),
            _MetaInfoClassMember('prefix-string', REFERENCE_UNION, 'str', 'inet:ip-address-no-zone',
                None, None,
                [], [],
                '''                IPv4/IPv6 address
                ''',
                'prefix_string',
                'Cisco-IOS-XR-infra-serg-cfg', False, [
                    _MetaInfoClassMember('prefix-string', ATTRIBUTE, 'str', 'inet:ipv4-address-no-zone',
                        None, None,
                        [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'],
                        '''                        IPv4/IPv6 address
                        ''',
                        'prefix_string',
                        'Cisco-IOS-XR-infra-serg-cfg', False),
                    _MetaInfoClassMember('prefix-string', ATTRIBUTE, 'str', 'inet:ipv6-address-no-zone',
                        None, None,
                        [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'],
                        '''                        IPv4/IPv6 address
                        ''',
                        'prefix_string',
                        'Cisco-IOS-XR-infra-serg-cfg', False),
                ]),
            ],
            'Cisco-IOS-XR-infra-serg-cfg',
            'ipaddress',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-infra-serg-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_serg_cfg',
        ),
    },
    'SessionRedundancy.Groups.Group.Peer' : {
        'meta_info' : _MetaInfoClass('SessionRedundancy.Groups.Group.Peer', REFERENCE_CLASS,
            '''None''',
            False, 
            [
            _MetaInfoClassMember('ipaddress', REFERENCE_CLASS, 'Ipaddress', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_serg_cfg', 'SessionRedundancy.Groups.Group.Peer.Ipaddress',
                [], [],
                '''                IPv4 or IPv6 Address of SERG Peer
                ''',
                'ipaddress',
                'Cisco-IOS-XR-infra-serg-cfg', False),
            ],
            'Cisco-IOS-XR-infra-serg-cfg',
            'peer',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-infra-serg-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_serg_cfg',
        ),
    },
    'SessionRedundancy.Groups.Group.RevertiveTimer' : {
        'meta_info' : _MetaInfoClass('SessionRedundancy.Groups.Group.RevertiveTimer', REFERENCE_CLASS,
            '''None''',
            False, 
            [
            _MetaInfoClassMember('max-value', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('1', '65535')], [],
                '''                Value of MAX Revertive Timer
                ''',
                'max_value',
                'Cisco-IOS-XR-infra-serg-cfg', False),
            _MetaInfoClassMember('value', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('1', '65535')], [],
                '''                Value of revertive time in minutes
                ''',
                'value',
                'Cisco-IOS-XR-infra-serg-cfg', False),
            ],
            'Cisco-IOS-XR-infra-serg-cfg',
            'revertive-timer',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-infra-serg-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_serg_cfg',
        ),
    },
    'SessionRedundancy.Groups.Group.InterfaceList.InterfaceRanges.InterfaceRange' : {
        'meta_info' : _MetaInfoClass('SessionRedundancy.Groups.Group.InterfaceList.InterfaceRanges.InterfaceRange', REFERENCE_LIST,
            '''Interface for this Group''',
            False, 
            [
            _MetaInfoClassMember('interface-name', ATTRIBUTE, 'str', 'xr:Interface-name',
                None, None,
                [], [b'[a-zA-Z0-9._/-]+'],
                '''                Interface name
                ''',
                'interface_name',
                'Cisco-IOS-XR-infra-serg-cfg', True),
            _MetaInfoClassMember('sub-interface-range-start', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('0', '2147483647')], [],
                '''                Sub Interface Start Range
                ''',
                'sub_interface_range_start',
                'Cisco-IOS-XR-infra-serg-cfg', True),
            _MetaInfoClassMember('sub-interface-range-end', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('0', '2147483647')], [],
                '''                Sub Interface End Range
                ''',
                'sub_interface_range_end',
                'Cisco-IOS-XR-infra-serg-cfg', True),
            _MetaInfoClassMember('interface-id-range-start', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('1', '65535')], [],
                '''                Interface ID Start Range
                ''',
                'interface_id_range_start',
                'Cisco-IOS-XR-infra-serg-cfg', False),
            _MetaInfoClassMember('interface-id-range-end', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('1', '65535')], [],
                '''                Interface ID End Range
                ''',
                'interface_id_range_end',
                'Cisco-IOS-XR-infra-serg-cfg', False),
            ],
            'Cisco-IOS-XR-infra-serg-cfg',
            'interface-range',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-infra-serg-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_serg_cfg',
        ),
    },
    'SessionRedundancy.Groups.Group.InterfaceList.InterfaceRanges' : {
        'meta_info' : _MetaInfoClass('SessionRedundancy.Groups.Group.InterfaceList.InterfaceRanges', REFERENCE_CLASS,
            '''Table of InterfaceRange''',
            False, 
            [
            _MetaInfoClassMember('interface-range', REFERENCE_LIST, 'InterfaceRange', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_serg_cfg', 'SessionRedundancy.Groups.Group.InterfaceList.InterfaceRanges.InterfaceRange',
                [], [],
                '''                Interface for this Group
                ''',
                'interface_range',
                'Cisco-IOS-XR-infra-serg-cfg', False),
            ],
            'Cisco-IOS-XR-infra-serg-cfg',
            'interface-ranges',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-infra-serg-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_serg_cfg',
        ),
    },
    'SessionRedundancy.Groups.Group.InterfaceList.Interfaces.Interface' : {
        'meta_info' : _MetaInfoClass('SessionRedundancy.Groups.Group.InterfaceList.Interfaces.Interface', REFERENCE_LIST,
            '''Interface for this Group''',
            False, 
            [
            _MetaInfoClassMember('interface-name', ATTRIBUTE, 'str', 'xr:Interface-name',
                None, None,
                [], [b'[a-zA-Z0-9._/-]+'],
                '''                Interface name
                ''',
                'interface_name',
                'Cisco-IOS-XR-infra-serg-cfg', True),
            _MetaInfoClassMember('interface-id', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('1', '65535')], [],
                '''                Interface Id for the interface
                ''',
                'interface_id',
                'Cisco-IOS-XR-infra-serg-cfg', False, is_mandatory=True),
            ],
            'Cisco-IOS-XR-infra-serg-cfg',
            'interface',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-infra-serg-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_serg_cfg',
        ),
    },
    'SessionRedundancy.Groups.Group.InterfaceList.Interfaces' : {
        'meta_info' : _MetaInfoClass('SessionRedundancy.Groups.Group.InterfaceList.Interfaces', REFERENCE_CLASS,
            '''Table of Interface''',
            False, 
            [
            _MetaInfoClassMember('interface', REFERENCE_LIST, 'Interface', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_serg_cfg', 'SessionRedundancy.Groups.Group.InterfaceList.Interfaces.Interface',
                [], [],
                '''                Interface for this Group
                ''',
                'interface',
                'Cisco-IOS-XR-infra-serg-cfg', False),
            ],
            'Cisco-IOS-XR-infra-serg-cfg',
            'interfaces',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-infra-serg-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_serg_cfg',
        ),
    },
    'SessionRedundancy.Groups.Group.InterfaceList' : {
        'meta_info' : _MetaInfoClass('SessionRedundancy.Groups.Group.InterfaceList', REFERENCE_CLASS,
            '''List of Interfaces for this Group''',
            False, 
            [
            _MetaInfoClassMember('interface-ranges', REFERENCE_CLASS, 'InterfaceRanges', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_serg_cfg', 'SessionRedundancy.Groups.Group.InterfaceList.InterfaceRanges',
                [], [],
                '''                Table of InterfaceRange
                ''',
                'interface_ranges',
                'Cisco-IOS-XR-infra-serg-cfg', False),
            _MetaInfoClassMember('interfaces', REFERENCE_CLASS, 'Interfaces', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_serg_cfg', 'SessionRedundancy.Groups.Group.InterfaceList.Interfaces',
                [], [],
                '''                Table of Interface
                ''',
                'interfaces',
                'Cisco-IOS-XR-infra-serg-cfg', False),
            _MetaInfoClassMember('enable', ATTRIBUTE, 'Empty', 'empty',
                None, None,
                [], [],
                '''                Enable List of Interfaces for this Group.
                Deletion of this object also causes deletion
                of all associated objects under InterfaceList
                .
                ''',
                'enable',
                'Cisco-IOS-XR-infra-serg-cfg', False),
            ],
            'Cisco-IOS-XR-infra-serg-cfg',
            'interface-list',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-infra-serg-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_serg_cfg',
        ),
    },
    'SessionRedundancy.Groups.Group.PoolList.PoolNames.PoolName' : {
        'meta_info' : _MetaInfoClass('SessionRedundancy.Groups.Group.PoolList.PoolNames.PoolName', REFERENCE_LIST,
            '''Address Pool Name''',
            False, 
            [
            _MetaInfoClassMember('pool-name', ATTRIBUTE, 'str', 'xr:Cisco-ios-xr-string',
                None, None,
                [], [b'[\\w\\-\\.:,_@#%$\\+=\\|;]+'],
                '''                Pool name
                ''',
                'pool_name',
                'Cisco-IOS-XR-infra-serg-cfg', True),
            ],
            'Cisco-IOS-XR-infra-serg-cfg',
            'pool-name',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-infra-serg-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_serg_cfg',
        ),
    },
    'SessionRedundancy.Groups.Group.PoolList.PoolNames' : {
        'meta_info' : _MetaInfoClass('SessionRedundancy.Groups.Group.PoolList.PoolNames', REFERENCE_CLASS,
            '''Table of PoolName''',
            False, 
            [
            _MetaInfoClassMember('pool-name', REFERENCE_LIST, 'PoolName', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_serg_cfg', 'SessionRedundancy.Groups.Group.PoolList.PoolNames.PoolName',
                [], [],
                '''                Address Pool Name
                ''',
                'pool_name',
                'Cisco-IOS-XR-infra-serg-cfg', False),
            ],
            'Cisco-IOS-XR-infra-serg-cfg',
            'pool-names',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-infra-serg-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_serg_cfg',
        ),
    },
    'SessionRedundancy.Groups.Group.PoolList' : {
        'meta_info' : _MetaInfoClass('SessionRedundancy.Groups.Group.PoolList', REFERENCE_CLASS,
            '''List of Pool-names for this Group''',
            False, 
            [
            _MetaInfoClassMember('pool-names', REFERENCE_CLASS, 'PoolNames', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_serg_cfg', 'SessionRedundancy.Groups.Group.PoolList.PoolNames',
                [], [],
                '''                Table of PoolName
                ''',
                'pool_names',
                'Cisco-IOS-XR-infra-serg-cfg', False),
            _MetaInfoClassMember('enable', ATTRIBUTE, 'Empty', 'empty',
                None, None,
                [], [],
                '''                Enable List of Pool-names for this Group.
                Deletion of this object also causes deletion
                of all associated objects under PoolList.
                ''',
                'enable',
                'Cisco-IOS-XR-infra-serg-cfg', False),
            ],
            'Cisco-IOS-XR-infra-serg-cfg',
            'pool-list',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-infra-serg-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_serg_cfg',
        ),
    },
    'SessionRedundancy.Groups.Group' : {
        'meta_info' : _MetaInfoClass('SessionRedundancy.Groups.Group', REFERENCE_LIST,
            '''Redundancy Group configuration''',
            False, 
            [
            _MetaInfoClassMember('group-id', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('1', '500')], [],
                '''                Group ID
                ''',
                'group_id',
                'Cisco-IOS-XR-infra-serg-cfg', True),
            _MetaInfoClassMember('peer', REFERENCE_CLASS, 'Peer', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_serg_cfg', 'SessionRedundancy.Groups.Group.Peer',
                [], [],
                '''                None
                ''',
                'peer',
                'Cisco-IOS-XR-infra-serg-cfg', False),
            _MetaInfoClassMember('revertive-timer', REFERENCE_CLASS, 'RevertiveTimer', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_serg_cfg', 'SessionRedundancy.Groups.Group.RevertiveTimer',
                [], [],
                '''                None
                ''',
                'revertive_timer',
                'Cisco-IOS-XR-infra-serg-cfg', False),
            _MetaInfoClassMember('interface-list', REFERENCE_CLASS, 'InterfaceList', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_serg_cfg', 'SessionRedundancy.Groups.Group.InterfaceList',
                [], [],
                '''                List of Interfaces for this Group
                ''',
                'interface_list',
                'Cisco-IOS-XR-infra-serg-cfg', False),
            _MetaInfoClassMember('pool-list', REFERENCE_CLASS, 'PoolList', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_serg_cfg', 'SessionRedundancy.Groups.Group.PoolList',
                [], [],
                '''                List of Pool-names for this Group
                ''',
                'pool_list',
                'Cisco-IOS-XR-infra-serg-cfg', False),
            _MetaInfoClassMember('core-tracking-object', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                Core Tracking Object for this Group
                ''',
                'core_tracking_object',
                'Cisco-IOS-XR-infra-serg-cfg', False),
            _MetaInfoClassMember('disable-tracking-object', ATTRIBUTE, 'Empty', 'empty',
                None, None,
                [], [],
                '''                Disable Tracking Object for this Group
                ''',
                'disable_tracking_object',
                'Cisco-IOS-XR-infra-serg-cfg', False),
            _MetaInfoClassMember('redundancy-disable', ATTRIBUTE, 'Empty', 'empty',
                None, None,
                [], [],
                '''                Disable
                ''',
                'redundancy_disable',
                'Cisco-IOS-XR-infra-serg-cfg', False),
            _MetaInfoClassMember('enable', ATTRIBUTE, 'Empty', 'empty',
                None, None,
                [], [],
                '''                Enable Redundancy Group configuration.
                Deletion of this object also causes deletion
                of all associated objects under Group.
                ''',
                'enable',
                'Cisco-IOS-XR-infra-serg-cfg', False),
            _MetaInfoClassMember('description', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                Description for this Group
                ''',
                'description',
                'Cisco-IOS-XR-infra-serg-cfg', False),
            _MetaInfoClassMember('access-tracking-object', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                Access Tracking Object for this Group
                ''',
                'access_tracking_object',
                'Cisco-IOS-XR-infra-serg-cfg', False),
            _MetaInfoClassMember('preferred-role', REFERENCE_ENUM_CLASS, 'SessionRedundancyGroupRole', 'Session-redundancy-group-role',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_serg_cfg', 'SessionRedundancyGroupRole',
                [], [],
                '''                Set preferred role
                ''',
                'preferred_role',
                'Cisco-IOS-XR-infra-serg-cfg', False),
            _MetaInfoClassMember('hold-timer', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('1', '65535')], [],
                '''                Set hold time (in Minutes)
                ''',
                'hold_timer',
                'Cisco-IOS-XR-infra-serg-cfg', False),
            _MetaInfoClassMember('mode-active', ATTRIBUTE, 'Empty', 'empty',
                None, None,
                [], [],
                '''                Set operation mode
                ''',
                'mode_active',
                'Cisco-IOS-XR-infra-serg-cfg', False),
            ],
            'Cisco-IOS-XR-infra-serg-cfg',
            'group',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-infra-serg-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_serg_cfg',
        ),
    },
    'SessionRedundancy.Groups' : {
        'meta_info' : _MetaInfoClass('SessionRedundancy.Groups', REFERENCE_CLASS,
            '''Table of Group''',
            False, 
            [
            _MetaInfoClassMember('group', REFERENCE_LIST, 'Group', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_serg_cfg', 'SessionRedundancy.Groups.Group',
                [], [],
                '''                Redundancy Group configuration
                ''',
                'group',
                'Cisco-IOS-XR-infra-serg-cfg', False),
            ],
            'Cisco-IOS-XR-infra-serg-cfg',
            'groups',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-infra-serg-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_serg_cfg',
        ),
    },
    'SessionRedundancy.RevertiveTimer' : {
        'meta_info' : _MetaInfoClass('SessionRedundancy.RevertiveTimer', REFERENCE_CLASS,
            '''None''',
            False, 
            [
            _MetaInfoClassMember('max-value', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('1', '65535')], [],
                '''                Value of MAX Revertive Timer
                ''',
                'max_value',
                'Cisco-IOS-XR-infra-serg-cfg', False),
            _MetaInfoClassMember('value', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('1', '65535')], [],
                '''                Value of revertive time in minutes
                ''',
                'value',
                'Cisco-IOS-XR-infra-serg-cfg', False),
            ],
            'Cisco-IOS-XR-infra-serg-cfg',
            'revertive-timer',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-infra-serg-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_serg_cfg',
        ),
    },
    'SessionRedundancy' : {
        'meta_info' : _MetaInfoClass('SessionRedundancy', REFERENCE_CLASS,
            '''Session Redundancy configuration''',
            False, 
            [
            _MetaInfoClassMember('groups', REFERENCE_CLASS, 'Groups', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_serg_cfg', 'SessionRedundancy.Groups',
                [], [],
                '''                Table of Group
                ''',
                'groups',
                'Cisco-IOS-XR-infra-serg-cfg', False),
            _MetaInfoClassMember('revertive-timer', REFERENCE_CLASS, 'RevertiveTimer', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_serg_cfg', 'SessionRedundancy.RevertiveTimer',
                [], [],
                '''                None
                ''',
                'revertive_timer',
                'Cisco-IOS-XR-infra-serg-cfg', False),
            _MetaInfoClassMember('redundancy-disable', ATTRIBUTE, 'Empty', 'empty',
                None, None,
                [], [],
                '''                Disable
                ''',
                'redundancy_disable',
                'Cisco-IOS-XR-infra-serg-cfg', False),
            _MetaInfoClassMember('enable', ATTRIBUTE, 'Empty', 'empty',
                None, None,
                [], [],
                '''                Enable Session Redundancy configuration.
                Deletion of this object also causes deletion of
                all associated objects under SessionRedundancy.
                ''',
                'enable',
                'Cisco-IOS-XR-infra-serg-cfg', False),
            _MetaInfoClassMember('source-interface', ATTRIBUTE, 'str', 'xr:Interface-name',
                None, None,
                [], [b'[a-zA-Z0-9._/-]+'],
                '''                Source Interface for Redundancy Peer
                Communication
                ''',
                'source_interface',
                'Cisco-IOS-XR-infra-serg-cfg', False),
            _MetaInfoClassMember('preferred-role', REFERENCE_ENUM_CLASS, 'SessionRedundancyGroupRole', 'Session-redundancy-group-role',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_serg_cfg', 'SessionRedundancyGroupRole',
                [], [],
                '''                Set preferred role
                ''',
                'preferred_role',
                'Cisco-IOS-XR-infra-serg-cfg', False),
            _MetaInfoClassMember('hold-timer', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('1', '65535')], [],
                '''                Set hold time (in Minutes)
                ''',
                'hold_timer',
                'Cisco-IOS-XR-infra-serg-cfg', False),
            ],
            'Cisco-IOS-XR-infra-serg-cfg',
            'session-redundancy',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-infra-serg-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_serg_cfg',
        ),
    },
}
_meta_table['SessionRedundancy.Groups.Group.Peer.Ipaddress']['meta_info'].parent =_meta_table['SessionRedundancy.Groups.Group.Peer']['meta_info']
_meta_table['SessionRedundancy.Groups.Group.InterfaceList.InterfaceRanges.InterfaceRange']['meta_info'].parent =_meta_table['SessionRedundancy.Groups.Group.InterfaceList.InterfaceRanges']['meta_info']
_meta_table['SessionRedundancy.Groups.Group.InterfaceList.Interfaces.Interface']['meta_info'].parent =_meta_table['SessionRedundancy.Groups.Group.InterfaceList.Interfaces']['meta_info']
_meta_table['SessionRedundancy.Groups.Group.InterfaceList.InterfaceRanges']['meta_info'].parent =_meta_table['SessionRedundancy.Groups.Group.InterfaceList']['meta_info']
_meta_table['SessionRedundancy.Groups.Group.InterfaceList.Interfaces']['meta_info'].parent =_meta_table['SessionRedundancy.Groups.Group.InterfaceList']['meta_info']
_meta_table['SessionRedundancy.Groups.Group.PoolList.PoolNames.PoolName']['meta_info'].parent =_meta_table['SessionRedundancy.Groups.Group.PoolList.PoolNames']['meta_info']
_meta_table['SessionRedundancy.Groups.Group.PoolList.PoolNames']['meta_info'].parent =_meta_table['SessionRedundancy.Groups.Group.PoolList']['meta_info']
_meta_table['SessionRedundancy.Groups.Group.Peer']['meta_info'].parent =_meta_table['SessionRedundancy.Groups.Group']['meta_info']
_meta_table['SessionRedundancy.Groups.Group.RevertiveTimer']['meta_info'].parent =_meta_table['SessionRedundancy.Groups.Group']['meta_info']
_meta_table['SessionRedundancy.Groups.Group.InterfaceList']['meta_info'].parent =_meta_table['SessionRedundancy.Groups.Group']['meta_info']
_meta_table['SessionRedundancy.Groups.Group.PoolList']['meta_info'].parent =_meta_table['SessionRedundancy.Groups.Group']['meta_info']
_meta_table['SessionRedundancy.Groups.Group']['meta_info'].parent =_meta_table['SessionRedundancy.Groups']['meta_info']
_meta_table['SessionRedundancy.Groups']['meta_info'].parent =_meta_table['SessionRedundancy']['meta_info']
_meta_table['SessionRedundancy.RevertiveTimer']['meta_info'].parent =_meta_table['SessionRedundancy']['meta_info']
