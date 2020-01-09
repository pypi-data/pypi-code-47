
'''
This is auto-generated file,
which includes metadata for module Cisco_IOS_XR_rgmgr_cfg
'''

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_LIST, REFERENCE_LEAFLIST, REFERENCE_BITS, REFERENCE_UNION
from ydk._core._dm_meta_info import REFERENCE_CLASS, REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, ANYXML_CLASS
from ydk._core._importer import _yang_ns

_meta_table = {
    'IccpMode' : _MetaInfoEnum('IccpMode',
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_rgmgr_cfg', 'IccpMode',
        '''Iccp mode''',
        {
            'singleton':'singleton',
        }, 'Cisco-IOS-XR-rgmgr-cfg', _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-rgmgr-cfg']),
    'RedundancyGroupManager.Aps.DefaultRedundancyGroup' : {
        'meta_info' : _MetaInfoClass('RedundancyGroupManager.Aps.DefaultRedundancyGroup', REFERENCE_CLASS,
            '''Default SONET controller backup configuration''',
            False, 
            [
            _MetaInfoClassMember('next-hop-address', ATTRIBUTE, 'str', 'inet:ipv4-address-no-zone',
                None, None,
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'],
                '''                IPv4 address of remote peer
                ''',
                'next_hop_address',
                'Cisco-IOS-XR-rgmgr-cfg', False),
            _MetaInfoClassMember('backup-interface-name', ATTRIBUTE, 'str', 'xr:Interface-name',
                None, None,
                [], [b'[a-zA-Z0-9._/-]+'],
                '''                Backup interface name
                ''',
                'backup_interface_name',
                'Cisco-IOS-XR-rgmgr-cfg', False),
            ],
            'Cisco-IOS-XR-rgmgr-cfg',
            'default-redundancy-group',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-rgmgr-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_rgmgr_cfg',
        ),
    },
    'RedundancyGroupManager.Aps.Groups.Group.Controllers.Controller' : {
        'meta_info' : _MetaInfoClass('RedundancyGroupManager.Aps.Groups.Group.Controllers.Controller', REFERENCE_LIST,
            '''none''',
            False, 
            [
            _MetaInfoClassMember('controller-name', ATTRIBUTE, 'str', 'xr:Interface-name',
                None, None,
                [], [b'[a-zA-Z0-9._/-]+'],
                '''                Controller Name
                ''',
                'controller_name',
                'Cisco-IOS-XR-rgmgr-cfg', True),
            _MetaInfoClassMember('next-hop-address', ATTRIBUTE, 'str', 'inet:ipv4-address-no-zone',
                None, None,
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'],
                '''                IPv4 address of remote peer
                ''',
                'next_hop_address',
                'Cisco-IOS-XR-rgmgr-cfg', False),
            _MetaInfoClassMember('backup-interface-name', ATTRIBUTE, 'str', 'xr:Interface-name',
                None, None,
                [], [b'[a-zA-Z0-9._/-]+'],
                '''                Backup interface name
                ''',
                'backup_interface_name',
                'Cisco-IOS-XR-rgmgr-cfg', False),
            ],
            'Cisco-IOS-XR-rgmgr-cfg',
            'controller',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-rgmgr-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_rgmgr_cfg',
        ),
    },
    'RedundancyGroupManager.Aps.Groups.Group.Controllers' : {
        'meta_info' : _MetaInfoClass('RedundancyGroupManager.Aps.Groups.Group.Controllers', REFERENCE_CLASS,
            '''Controller configuration''',
            False, 
            [
            _MetaInfoClassMember('controller', REFERENCE_LIST, 'Controller', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_rgmgr_cfg', 'RedundancyGroupManager.Aps.Groups.Group.Controllers.Controller',
                [], [],
                '''                none
                ''',
                'controller',
                'Cisco-IOS-XR-rgmgr-cfg', False),
            ],
            'Cisco-IOS-XR-rgmgr-cfg',
            'controllers',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-rgmgr-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_rgmgr_cfg',
        ),
    },
    'RedundancyGroupManager.Aps.Groups.Group' : {
        'meta_info' : _MetaInfoClass('RedundancyGroupManager.Aps.Groups.Group', REFERENCE_LIST,
            '''Redundancy Group Configuration''',
            False, 
            [
            _MetaInfoClassMember('group-id', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('1', '32')], [],
                '''                The redundancy group ID
                ''',
                'group_id',
                'Cisco-IOS-XR-rgmgr-cfg', True),
            _MetaInfoClassMember('controllers', REFERENCE_CLASS, 'Controllers', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_rgmgr_cfg', 'RedundancyGroupManager.Aps.Groups.Group.Controllers',
                [], [],
                '''                Controller configuration
                ''',
                'controllers',
                'Cisco-IOS-XR-rgmgr-cfg', False),
            ],
            'Cisco-IOS-XR-rgmgr-cfg',
            'group',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-rgmgr-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_rgmgr_cfg',
        ),
    },
    'RedundancyGroupManager.Aps.Groups' : {
        'meta_info' : _MetaInfoClass('RedundancyGroupManager.Aps.Groups', REFERENCE_CLASS,
            '''Redundancy Group Table''',
            False, 
            [
            _MetaInfoClassMember('group', REFERENCE_LIST, 'Group', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_rgmgr_cfg', 'RedundancyGroupManager.Aps.Groups.Group',
                [], [],
                '''                Redundancy Group Configuration
                ''',
                'group',
                'Cisco-IOS-XR-rgmgr-cfg', False),
            ],
            'Cisco-IOS-XR-rgmgr-cfg',
            'groups',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-rgmgr-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_rgmgr_cfg',
        ),
    },
    'RedundancyGroupManager.Aps' : {
        'meta_info' : _MetaInfoClass('RedundancyGroupManager.Aps', REFERENCE_CLASS,
            '''MR-APS groups''',
            False, 
            [
            _MetaInfoClassMember('default-redundancy-group', REFERENCE_CLASS, 'DefaultRedundancyGroup', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_rgmgr_cfg', 'RedundancyGroupManager.Aps.DefaultRedundancyGroup',
                [], [],
                '''                Default SONET controller backup configuration
                ''',
                'default_redundancy_group',
                'Cisco-IOS-XR-rgmgr-cfg', False),
            _MetaInfoClassMember('groups', REFERENCE_CLASS, 'Groups', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_rgmgr_cfg', 'RedundancyGroupManager.Aps.Groups',
                [], [],
                '''                Redundancy Group Table
                ''',
                'groups',
                'Cisco-IOS-XR-rgmgr-cfg', False),
            ],
            'Cisco-IOS-XR-rgmgr-cfg',
            'aps',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-rgmgr-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_rgmgr_cfg',
        ),
    },
    'RedundancyGroupManager.Iccp.IccpGroups.IccpGroup.Backbones.Backbone' : {
        'meta_info' : _MetaInfoClass('RedundancyGroupManager.Iccp.IccpGroups.IccpGroup.Backbones.Backbone', REFERENCE_LIST,
            '''ICCP backbone interface configuration''',
            False, 
            [
            _MetaInfoClassMember('backbone-name', ATTRIBUTE, 'str', 'xr:Interface-name',
                None, None,
                [], [b'[a-zA-Z0-9._/-]+'],
                '''                none
                ''',
                'backbone_name',
                'Cisco-IOS-XR-rgmgr-cfg', True),
            ],
            'Cisco-IOS-XR-rgmgr-cfg',
            'backbone',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-rgmgr-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_rgmgr_cfg',
        ),
    },
    'RedundancyGroupManager.Iccp.IccpGroups.IccpGroup.Backbones' : {
        'meta_info' : _MetaInfoClass('RedundancyGroupManager.Iccp.IccpGroups.IccpGroup.Backbones', REFERENCE_CLASS,
            '''ICCP backbone configuration''',
            False, 
            [
            _MetaInfoClassMember('backbone', REFERENCE_LIST, 'Backbone', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_rgmgr_cfg', 'RedundancyGroupManager.Iccp.IccpGroups.IccpGroup.Backbones.Backbone',
                [], [],
                '''                ICCP backbone interface configuration
                ''',
                'backbone',
                'Cisco-IOS-XR-rgmgr-cfg', False),
            ],
            'Cisco-IOS-XR-rgmgr-cfg',
            'backbones',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-rgmgr-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_rgmgr_cfg',
        ),
    },
    'RedundancyGroupManager.Iccp.IccpGroups.IccpGroup.Members.Member' : {
        'meta_info' : _MetaInfoClass('RedundancyGroupManager.Iccp.IccpGroups.IccpGroup.Members.Member', REFERENCE_LIST,
            '''ICCP member configuration''',
            False, 
            [
            _MetaInfoClassMember('neighbor-address', ATTRIBUTE, 'str', 'inet:ipv4-address-no-zone',
                None, None,
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'],
                '''                Neighbor IP address
                ''',
                'neighbor_address',
                'Cisco-IOS-XR-rgmgr-cfg', True),
            ],
            'Cisco-IOS-XR-rgmgr-cfg',
            'member',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-rgmgr-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_rgmgr_cfg',
        ),
    },
    'RedundancyGroupManager.Iccp.IccpGroups.IccpGroup.Members' : {
        'meta_info' : _MetaInfoClass('RedundancyGroupManager.Iccp.IccpGroups.IccpGroup.Members', REFERENCE_CLASS,
            '''ICCP member configuration''',
            False, 
            [
            _MetaInfoClassMember('member', REFERENCE_LIST, 'Member', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_rgmgr_cfg', 'RedundancyGroupManager.Iccp.IccpGroups.IccpGroup.Members.Member',
                [], [],
                '''                ICCP member configuration
                ''',
                'member',
                'Cisco-IOS-XR-rgmgr-cfg', False),
            ],
            'Cisco-IOS-XR-rgmgr-cfg',
            'members',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-rgmgr-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_rgmgr_cfg',
        ),
    },
    'RedundancyGroupManager.Iccp.IccpGroups.IccpGroup.NvSatellite' : {
        'meta_info' : _MetaInfoClass('RedundancyGroupManager.Iccp.IccpGroups.IccpGroup.NvSatellite', REFERENCE_CLASS,
            '''nV Satellite configuration''',
            False, 
            [
            _MetaInfoClassMember('system-mac', ATTRIBUTE, 'str', 'yang:mac-address',
                None, None,
                [], [b'[0-9a-fA-F]{2}(:[0-9a-fA-F]{2}){5}'],
                '''                Optional identifier for this system
                ''',
                'system_mac',
                'Cisco-IOS-XR-icpe-infra-cfg', False),
            ],
            'Cisco-IOS-XR-icpe-infra-cfg',
            'nv-satellite',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-icpe-infra-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_rgmgr_cfg',
        ),
    },
    'RedundancyGroupManager.Iccp.IccpGroups.IccpGroup.Mlacp' : {
        'meta_info' : _MetaInfoClass('RedundancyGroupManager.Iccp.IccpGroups.IccpGroup.Mlacp', REFERENCE_CLASS,
            '''Multi-chassis Link Aggregation Control Protocol
commands''',
            False, 
            [
            _MetaInfoClassMember('connect-timeout', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('0', '65534')], [],
                '''                Number of seconds to wait before assuming mLACP
                peer is down.
                ''',
                'connect_timeout',
                'Cisco-IOS-XR-bundlemgr-cfg', False),
            _MetaInfoClassMember('system-mac', ATTRIBUTE, 'str', 'yang:mac-address',
                None, None,
                [], [b'[0-9a-fA-F]{2}(:[0-9a-fA-F]{2}){5}'],
                '''                Unique LACP identifier for this system.
                ''',
                'system_mac',
                'Cisco-IOS-XR-bundlemgr-cfg', False),
            _MetaInfoClassMember('node', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('0', '7')], [],
                '''                Unique identifier for this system in the ICCP
                Group.
                ''',
                'node',
                'Cisco-IOS-XR-bundlemgr-cfg', False),
            _MetaInfoClassMember('system-priority', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('1', '65535')], [],
                '''                Priority for this system. Lower value is higher
                priority.
                ''',
                'system_priority',
                'Cisco-IOS-XR-bundlemgr-cfg', False),
            ],
            'Cisco-IOS-XR-bundlemgr-cfg',
            'mlacp',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-bundlemgr-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_rgmgr_cfg',
        ),
    },
    'RedundancyGroupManager.Iccp.IccpGroups.IccpGroup' : {
        'meta_info' : _MetaInfoClass('RedundancyGroupManager.Iccp.IccpGroups.IccpGroup', REFERENCE_LIST,
            '''Redundancy Group Configuration''',
            False, 
            [
            _MetaInfoClassMember('group-number', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('1', '4294967295')], [],
                '''                The redundancy icc group number
                ''',
                'group_number',
                'Cisco-IOS-XR-rgmgr-cfg', True),
            _MetaInfoClassMember('backbones', REFERENCE_CLASS, 'Backbones', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_rgmgr_cfg', 'RedundancyGroupManager.Iccp.IccpGroups.IccpGroup.Backbones',
                [], [],
                '''                ICCP backbone configuration
                ''',
                'backbones',
                'Cisco-IOS-XR-rgmgr-cfg', False),
            _MetaInfoClassMember('members', REFERENCE_CLASS, 'Members', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_rgmgr_cfg', 'RedundancyGroupManager.Iccp.IccpGroups.IccpGroup.Members',
                [], [],
                '''                ICCP member configuration
                ''',
                'members',
                'Cisco-IOS-XR-rgmgr-cfg', False),
            _MetaInfoClassMember('isolation-recovery-delay', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('30', '600')], [],
                '''                ICCP isolation recovery delay
                ''',
                'isolation_recovery_delay',
                'Cisco-IOS-XR-rgmgr-cfg', False),
            _MetaInfoClassMember('mode', REFERENCE_ENUM_CLASS, 'IccpMode', 'Iccp-mode',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_rgmgr_cfg', 'IccpMode',
                [], [],
                '''                ICCP mode
                ''',
                'mode',
                'Cisco-IOS-XR-rgmgr-cfg', False),
            _MetaInfoClassMember('nv-satellite', REFERENCE_CLASS, 'NvSatellite', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_rgmgr_cfg', 'RedundancyGroupManager.Iccp.IccpGroups.IccpGroup.NvSatellite',
                [], [],
                '''                nV Satellite configuration
                ''',
                'nv_satellite',
                'Cisco-IOS-XR-icpe-infra-cfg', False),
            _MetaInfoClassMember('mlacp', REFERENCE_CLASS, 'Mlacp', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_rgmgr_cfg', 'RedundancyGroupManager.Iccp.IccpGroups.IccpGroup.Mlacp',
                [], [],
                '''                Multi-chassis Link Aggregation Control Protocol
                commands
                ''',
                'mlacp',
                'Cisco-IOS-XR-bundlemgr-cfg', False),
            ],
            'Cisco-IOS-XR-rgmgr-cfg',
            'iccp-group',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-rgmgr-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_rgmgr_cfg',
        ),
    },
    'RedundancyGroupManager.Iccp.IccpGroups' : {
        'meta_info' : _MetaInfoClass('RedundancyGroupManager.Iccp.IccpGroups', REFERENCE_CLASS,
            '''Redundancy Group Table Configuration''',
            False, 
            [
            _MetaInfoClassMember('iccp-group', REFERENCE_LIST, 'IccpGroup', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_rgmgr_cfg', 'RedundancyGroupManager.Iccp.IccpGroups.IccpGroup',
                [], [],
                '''                Redundancy Group Configuration
                ''',
                'iccp_group',
                'Cisco-IOS-XR-rgmgr-cfg', False),
            ],
            'Cisco-IOS-XR-rgmgr-cfg',
            'iccp-groups',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-rgmgr-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_rgmgr_cfg',
        ),
    },
    'RedundancyGroupManager.Iccp' : {
        'meta_info' : _MetaInfoClass('RedundancyGroupManager.Iccp', REFERENCE_CLASS,
            '''ICCP configuration''',
            False, 
            [
            _MetaInfoClassMember('iccp-groups', REFERENCE_CLASS, 'IccpGroups', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_rgmgr_cfg', 'RedundancyGroupManager.Iccp.IccpGroups',
                [], [],
                '''                Redundancy Group Table Configuration
                ''',
                'iccp_groups',
                'Cisco-IOS-XR-rgmgr-cfg', False),
            ],
            'Cisco-IOS-XR-rgmgr-cfg',
            'iccp',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-rgmgr-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_rgmgr_cfg',
        ),
    },
    'RedundancyGroupManager' : {
        'meta_info' : _MetaInfoClass('RedundancyGroupManager', REFERENCE_CLASS,
            '''Redundancy Group Manager Configuration''',
            False, 
            [
            _MetaInfoClassMember('aps', REFERENCE_CLASS, 'Aps', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_rgmgr_cfg', 'RedundancyGroupManager.Aps',
                [], [],
                '''                MR-APS groups
                ''',
                'aps',
                'Cisco-IOS-XR-rgmgr-cfg', False),
            _MetaInfoClassMember('iccp', REFERENCE_CLASS, 'Iccp', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_rgmgr_cfg', 'RedundancyGroupManager.Iccp',
                [], [],
                '''                ICCP configuration
                ''',
                'iccp',
                'Cisco-IOS-XR-rgmgr-cfg', False),
            _MetaInfoClassMember('enable', ATTRIBUTE, 'Empty', 'empty',
                None, None,
                [], [],
                '''                Enable redundancy group manager
                ''',
                'enable',
                'Cisco-IOS-XR-rgmgr-cfg', False),
            ],
            'Cisco-IOS-XR-rgmgr-cfg',
            'redundancy-group-manager',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-rgmgr-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_rgmgr_cfg',
        ),
    },
}
_meta_table['RedundancyGroupManager.Aps.Groups.Group.Controllers.Controller']['meta_info'].parent =_meta_table['RedundancyGroupManager.Aps.Groups.Group.Controllers']['meta_info']
_meta_table['RedundancyGroupManager.Aps.Groups.Group.Controllers']['meta_info'].parent =_meta_table['RedundancyGroupManager.Aps.Groups.Group']['meta_info']
_meta_table['RedundancyGroupManager.Aps.Groups.Group']['meta_info'].parent =_meta_table['RedundancyGroupManager.Aps.Groups']['meta_info']
_meta_table['RedundancyGroupManager.Aps.DefaultRedundancyGroup']['meta_info'].parent =_meta_table['RedundancyGroupManager.Aps']['meta_info']
_meta_table['RedundancyGroupManager.Aps.Groups']['meta_info'].parent =_meta_table['RedundancyGroupManager.Aps']['meta_info']
_meta_table['RedundancyGroupManager.Iccp.IccpGroups.IccpGroup.Backbones.Backbone']['meta_info'].parent =_meta_table['RedundancyGroupManager.Iccp.IccpGroups.IccpGroup.Backbones']['meta_info']
_meta_table['RedundancyGroupManager.Iccp.IccpGroups.IccpGroup.Members.Member']['meta_info'].parent =_meta_table['RedundancyGroupManager.Iccp.IccpGroups.IccpGroup.Members']['meta_info']
_meta_table['RedundancyGroupManager.Iccp.IccpGroups.IccpGroup.Backbones']['meta_info'].parent =_meta_table['RedundancyGroupManager.Iccp.IccpGroups.IccpGroup']['meta_info']
_meta_table['RedundancyGroupManager.Iccp.IccpGroups.IccpGroup.Members']['meta_info'].parent =_meta_table['RedundancyGroupManager.Iccp.IccpGroups.IccpGroup']['meta_info']
_meta_table['RedundancyGroupManager.Iccp.IccpGroups.IccpGroup.NvSatellite']['meta_info'].parent =_meta_table['RedundancyGroupManager.Iccp.IccpGroups.IccpGroup']['meta_info']
_meta_table['RedundancyGroupManager.Iccp.IccpGroups.IccpGroup.Mlacp']['meta_info'].parent =_meta_table['RedundancyGroupManager.Iccp.IccpGroups.IccpGroup']['meta_info']
_meta_table['RedundancyGroupManager.Iccp.IccpGroups.IccpGroup']['meta_info'].parent =_meta_table['RedundancyGroupManager.Iccp.IccpGroups']['meta_info']
_meta_table['RedundancyGroupManager.Iccp.IccpGroups']['meta_info'].parent =_meta_table['RedundancyGroupManager.Iccp']['meta_info']
_meta_table['RedundancyGroupManager.Aps']['meta_info'].parent =_meta_table['RedundancyGroupManager']['meta_info']
_meta_table['RedundancyGroupManager.Iccp']['meta_info'].parent =_meta_table['RedundancyGroupManager']['meta_info']
