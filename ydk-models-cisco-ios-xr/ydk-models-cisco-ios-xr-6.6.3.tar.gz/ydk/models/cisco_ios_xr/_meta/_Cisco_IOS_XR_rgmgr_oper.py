
'''
This is auto-generated file,
which includes metadata for module Cisco_IOS_XR_rgmgr_oper
'''

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_LIST, REFERENCE_LEAFLIST, REFERENCE_BITS, REFERENCE_UNION
from ydk._core._dm_meta_info import REFERENCE_CLASS, REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, ANYXML_CLASS
from ydk._core._importer import _yang_ns

_meta_table = {
    'RedundancyGroupManager.Controllers.Controller' : {
        'meta_info' : _MetaInfoClass('RedundancyGroupManager.Controllers.Controller', REFERENCE_LIST,
            '''Display redundancy group by controller name''',
            False, 
            [
            _MetaInfoClassMember('controller-name', ATTRIBUTE, 'str', 'xr:Interface-name',
                None, None,
                [], [b'[a-zA-Z0-9._/-]+'],
                '''                Controller name
                ''',
                'controller_name',
                'Cisco-IOS-XR-rgmgr-oper', True, is_config=False),
            _MetaInfoClassMember('multi-router-aps-group-number', ATTRIBUTE, 'str', 'string',
                None, None,
                [(0, 64)], [],
                '''                Configured interchassis redundancy group number
                ''',
                'multi_router_aps_group_number',
                'Cisco-IOS-XR-rgmgr-oper', False, is_config=False),
            _MetaInfoClassMember('controller-name-xr', ATTRIBUTE, 'str', 'string',
                None, None,
                [(0, 64)], [],
                '''                Name of controller being backed up
                ''',
                'controller_name_xr',
                'Cisco-IOS-XR-rgmgr-oper', False, is_config=False),
            _MetaInfoClassMember('controller-handle', ATTRIBUTE, 'str', 'xr:Interface-name',
                None, None,
                [], [b'[a-zA-Z0-9._/-]+'],
                '''                Handle of controller being backed up
                ''',
                'controller_handle',
                'Cisco-IOS-XR-rgmgr-oper', False, is_config=False),
            _MetaInfoClassMember('backup-interface-name', ATTRIBUTE, 'str', 'string',
                None, None,
                [(0, 64)], [],
                '''                Backup interface name
                ''',
                'backup_interface_name',
                'Cisco-IOS-XR-rgmgr-oper', False, is_config=False),
            _MetaInfoClassMember('backup-interface-handle', ATTRIBUTE, 'str', 'xr:Interface-name',
                None, None,
                [], [b'[a-zA-Z0-9._/-]+'],
                '''                Backup interface handle
                ''',
                'backup_interface_handle',
                'Cisco-IOS-XR-rgmgr-oper', False, is_config=False),
            _MetaInfoClassMember('backup-interface-next-hop-ip-address', ATTRIBUTE, 'str', 'inet:ipv4-address',
                None, None,
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'],
                '''                Backup interface next hop IP address
                ''',
                'backup_interface_next_hop_ip_address',
                'Cisco-IOS-XR-rgmgr-oper', False, is_config=False),
            _MetaInfoClassMember('inter-chassis-group-state', ATTRIBUTE, 'str', 'string',
                None, None,
                [(0, 64)], [],
                '''                Configured interchassis redundancy group state
                ''',
                'inter_chassis_group_state',
                'Cisco-IOS-XR-rgmgr-oper', False, is_config=False),
            ],
            'Cisco-IOS-XR-rgmgr-oper',
            'controller',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-rgmgr-oper'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_rgmgr_oper',
            is_config=False,
        ),
    },
    'RedundancyGroupManager.Controllers' : {
        'meta_info' : _MetaInfoClass('RedundancyGroupManager.Controllers', REFERENCE_CLASS,
            '''Redundancy group manager data''',
            False, 
            [
            _MetaInfoClassMember('controller', REFERENCE_LIST, 'Controller', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_rgmgr_oper', 'RedundancyGroupManager.Controllers.Controller',
                [], [],
                '''                Display redundancy group by controller name
                ''',
                'controller',
                'Cisco-IOS-XR-rgmgr-oper', False, is_config=False),
            ],
            'Cisco-IOS-XR-rgmgr-oper',
            'controllers',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-rgmgr-oper'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_rgmgr_oper',
            is_config=False,
        ),
    },
    'RedundancyGroupManager' : {
        'meta_info' : _MetaInfoClass('RedundancyGroupManager', REFERENCE_CLASS,
            '''Redundancy group manager operational data''',
            False, 
            [
            _MetaInfoClassMember('controllers', REFERENCE_CLASS, 'Controllers', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_rgmgr_oper', 'RedundancyGroupManager.Controllers',
                [], [],
                '''                Redundancy group manager data
                ''',
                'controllers',
                'Cisco-IOS-XR-rgmgr-oper', False, is_config=False),
            ],
            'Cisco-IOS-XR-rgmgr-oper',
            'redundancy-group-manager',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-rgmgr-oper'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_rgmgr_oper',
            is_config=False,
        ),
    },
}
_meta_table['RedundancyGroupManager.Controllers.Controller']['meta_info'].parent =_meta_table['RedundancyGroupManager.Controllers']['meta_info']
_meta_table['RedundancyGroupManager.Controllers']['meta_info'].parent =_meta_table['RedundancyGroupManager']['meta_info']
