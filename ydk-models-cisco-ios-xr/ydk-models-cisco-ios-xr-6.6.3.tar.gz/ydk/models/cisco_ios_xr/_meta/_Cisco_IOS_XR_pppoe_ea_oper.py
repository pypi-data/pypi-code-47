
'''
This is auto-generated file,
which includes metadata for module Cisco_IOS_XR_pppoe_ea_oper
'''

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_LIST, REFERENCE_LEAFLIST, REFERENCE_BITS, REFERENCE_UNION
from ydk._core._dm_meta_info import REFERENCE_CLASS, REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, ANYXML_CLASS
from ydk._core._importer import _yang_ns

_meta_table = {
    'PppoeEa.Nodes.Node.ParentInterfaceIds.ParentInterfaceId.SrgvMac' : {
        'meta_info' : _MetaInfoClass('PppoeEa.Nodes.Node.ParentInterfaceIds.ParentInterfaceId.SrgvMac', REFERENCE_CLASS,
            '''SRG VMac-address''',
            False, 
            [
            _MetaInfoClassMember('macaddr', ATTRIBUTE, 'str', 'yang:hex-string',
                None, None,
                [], [b'([0-9a-fA-F]{2}(:[0-9a-fA-F]{2})*)?'],
                '''                macaddr
                ''',
                'macaddr',
                'Cisco-IOS-XR-pppoe-ea-oper', False, is_config=False),
            ],
            'Cisco-IOS-XR-pppoe-ea-oper',
            'srgv-mac',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-pppoe-ea-oper'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_pppoe_ea_oper',
            is_config=False,
        ),
    },
    'PppoeEa.Nodes.Node.ParentInterfaceIds.ParentInterfaceId' : {
        'meta_info' : _MetaInfoClass('PppoeEa.Nodes.Node.ParentInterfaceIds.ParentInterfaceId', REFERENCE_LIST,
            '''PPPoE parent interface info''',
            False, 
            [
            _MetaInfoClassMember('parent-interface-name', ATTRIBUTE, 'str', 'xr:Interface-name',
                None, None,
                [], [b'[a-zA-Z0-9._/-]+'],
                '''                Interface Name
                ''',
                'parent_interface_name',
                'Cisco-IOS-XR-pppoe-ea-oper', True, is_config=False),
            _MetaInfoClassMember('srgv-mac', REFERENCE_CLASS, 'SrgvMac', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_pppoe_ea_oper', 'PppoeEa.Nodes.Node.ParentInterfaceIds.ParentInterfaceId.SrgvMac',
                [], [],
                '''                SRG VMac-address
                ''',
                'srgv_mac',
                'Cisco-IOS-XR-pppoe-ea-oper', False, is_config=False),
            _MetaInfoClassMember('interface', ATTRIBUTE, 'str', 'xr:Interface-name',
                None, None,
                [], [b'[a-zA-Z0-9._/-]+'],
                '''                Interface
                ''',
                'interface',
                'Cisco-IOS-XR-pppoe-ea-oper', False, is_config=False),
            _MetaInfoClassMember('is-in-sync', ATTRIBUTE, 'bool', 'boolean',
                None, None,
                [], [],
                '''                Is in sync
                ''',
                'is_in_sync',
                'Cisco-IOS-XR-pppoe-ea-oper', False, is_config=False),
            ],
            'Cisco-IOS-XR-pppoe-ea-oper',
            'parent-interface-id',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-pppoe-ea-oper'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_pppoe_ea_oper',
            is_config=False,
        ),
    },
    'PppoeEa.Nodes.Node.ParentInterfaceIds' : {
        'meta_info' : _MetaInfoClass('PppoeEa.Nodes.Node.ParentInterfaceIds', REFERENCE_CLASS,
            '''PPPoE parent interface info''',
            False, 
            [
            _MetaInfoClassMember('parent-interface-id', REFERENCE_LIST, 'ParentInterfaceId', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_pppoe_ea_oper', 'PppoeEa.Nodes.Node.ParentInterfaceIds.ParentInterfaceId',
                [], [],
                '''                PPPoE parent interface info
                ''',
                'parent_interface_id',
                'Cisco-IOS-XR-pppoe-ea-oper', False, is_config=False),
            ],
            'Cisco-IOS-XR-pppoe-ea-oper',
            'parent-interface-ids',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-pppoe-ea-oper'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_pppoe_ea_oper',
            is_config=False,
        ),
    },
    'PppoeEa.Nodes.Node.InterfaceIds.InterfaceId.PeerMac' : {
        'meta_info' : _MetaInfoClass('PppoeEa.Nodes.Node.InterfaceIds.InterfaceId.PeerMac', REFERENCE_CLASS,
            '''Peer Mac-address''',
            False, 
            [
            _MetaInfoClassMember('macaddr', ATTRIBUTE, 'str', 'yang:hex-string',
                None, None,
                [], [b'([0-9a-fA-F]{2}(:[0-9a-fA-F]{2})*)?'],
                '''                macaddr
                ''',
                'macaddr',
                'Cisco-IOS-XR-pppoe-ea-oper', False, is_config=False),
            ],
            'Cisco-IOS-XR-pppoe-ea-oper',
            'peer-mac',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-pppoe-ea-oper'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_pppoe_ea_oper',
            is_config=False,
        ),
    },
    'PppoeEa.Nodes.Node.InterfaceIds.InterfaceId.LocalMac' : {
        'meta_info' : _MetaInfoClass('PppoeEa.Nodes.Node.InterfaceIds.InterfaceId.LocalMac', REFERENCE_CLASS,
            '''Local Mac-address''',
            False, 
            [
            _MetaInfoClassMember('macaddr', ATTRIBUTE, 'str', 'yang:hex-string',
                None, None,
                [], [b'([0-9a-fA-F]{2}(:[0-9a-fA-F]{2})*)?'],
                '''                macaddr
                ''',
                'macaddr',
                'Cisco-IOS-XR-pppoe-ea-oper', False, is_config=False),
            ],
            'Cisco-IOS-XR-pppoe-ea-oper',
            'local-mac',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-pppoe-ea-oper'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_pppoe_ea_oper',
            is_config=False,
        ),
    },
    'PppoeEa.Nodes.Node.InterfaceIds.InterfaceId.SrgvMac' : {
        'meta_info' : _MetaInfoClass('PppoeEa.Nodes.Node.InterfaceIds.InterfaceId.SrgvMac', REFERENCE_CLASS,
            '''SRG VMac-address''',
            False, 
            [
            _MetaInfoClassMember('macaddr', ATTRIBUTE, 'str', 'yang:hex-string',
                None, None,
                [], [b'([0-9a-fA-F]{2}(:[0-9a-fA-F]{2})*)?'],
                '''                macaddr
                ''',
                'macaddr',
                'Cisco-IOS-XR-pppoe-ea-oper', False, is_config=False),
            ],
            'Cisco-IOS-XR-pppoe-ea-oper',
            'srgv-mac',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-pppoe-ea-oper'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_pppoe_ea_oper',
            is_config=False,
        ),
    },
    'PppoeEa.Nodes.Node.InterfaceIds.InterfaceId' : {
        'meta_info' : _MetaInfoClass('PppoeEa.Nodes.Node.InterfaceIds.InterfaceId', REFERENCE_LIST,
            '''PPPoE interface info''',
            False, 
            [
            _MetaInfoClassMember('interface-name', ATTRIBUTE, 'str', 'xr:Interface-name',
                None, None,
                [], [b'[a-zA-Z0-9._/-]+'],
                '''                Interface Name
                ''',
                'interface_name',
                'Cisco-IOS-XR-pppoe-ea-oper', True, is_config=False),
            _MetaInfoClassMember('peer-mac', REFERENCE_CLASS, 'PeerMac', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_pppoe_ea_oper', 'PppoeEa.Nodes.Node.InterfaceIds.InterfaceId.PeerMac',
                [], [],
                '''                Peer Mac-address
                ''',
                'peer_mac',
                'Cisco-IOS-XR-pppoe-ea-oper', False, is_config=False),
            _MetaInfoClassMember('local-mac', REFERENCE_CLASS, 'LocalMac', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_pppoe_ea_oper', 'PppoeEa.Nodes.Node.InterfaceIds.InterfaceId.LocalMac',
                [], [],
                '''                Local Mac-address
                ''',
                'local_mac',
                'Cisco-IOS-XR-pppoe-ea-oper', False, is_config=False),
            _MetaInfoClassMember('srgv-mac', REFERENCE_CLASS, 'SrgvMac', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_pppoe_ea_oper', 'PppoeEa.Nodes.Node.InterfaceIds.InterfaceId.SrgvMac',
                [], [],
                '''                SRG VMac-address
                ''',
                'srgv_mac',
                'Cisco-IOS-XR-pppoe-ea-oper', False, is_config=False),
            _MetaInfoClassMember('interface', ATTRIBUTE, 'str', 'xr:Interface-name',
                None, None,
                [], [b'[a-zA-Z0-9._/-]+'],
                '''                Interface
                ''',
                'interface',
                'Cisco-IOS-XR-pppoe-ea-oper', False, is_config=False),
            _MetaInfoClassMember('session-id', ATTRIBUTE, 'int', 'uint16',
                None, None,
                [('0', '65535')], [],
                '''                Session ID
                ''',
                'session_id',
                'Cisco-IOS-XR-pppoe-ea-oper', False, is_config=False),
            _MetaInfoClassMember('parent-interface', ATTRIBUTE, 'str', 'xr:Interface-name',
                None, None,
                [], [b'[a-zA-Z0-9._/-]+'],
                '''                Parent Interface
                ''',
                'parent_interface',
                'Cisco-IOS-XR-pppoe-ea-oper', False, is_config=False),
            _MetaInfoClassMember('is-priority-set', ATTRIBUTE, 'bool', 'boolean',
                None, None,
                [], [],
                '''                Is Priority Set
                ''',
                'is_priority_set',
                'Cisco-IOS-XR-pppoe-ea-oper', False, is_config=False),
            _MetaInfoClassMember('priority', ATTRIBUTE, 'int', 'uint8',
                None, None,
                [('0', '255')], [],
                '''                Priority
                ''',
                'priority',
                'Cisco-IOS-XR-pppoe-ea-oper', False, is_config=False),
            _MetaInfoClassMember('is-in-sync', ATTRIBUTE, 'bool', 'boolean',
                None, None,
                [], [],
                '''                Is in sync
                ''',
                'is_in_sync',
                'Cisco-IOS-XR-pppoe-ea-oper', False, is_config=False),
            _MetaInfoClassMember('is-platform-created', ATTRIBUTE, 'bool', 'boolean',
                None, None,
                [], [],
                '''                Is Platform created
                ''',
                'is_platform_created',
                'Cisco-IOS-XR-pppoe-ea-oper', False, is_config=False),
            _MetaInfoClassMember('vlanid', REFERENCE_LEAFLIST, 'int', 'uint16',
                None, None,
                [('0', '65535')], [],
                '''                VLAN Ids
                ''',
                'vlanid',
                'Cisco-IOS-XR-pppoe-ea-oper', False, max_elements=2, is_config=False),
            ],
            'Cisco-IOS-XR-pppoe-ea-oper',
            'interface-id',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-pppoe-ea-oper'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_pppoe_ea_oper',
            is_config=False,
        ),
    },
    'PppoeEa.Nodes.Node.InterfaceIds' : {
        'meta_info' : _MetaInfoClass('PppoeEa.Nodes.Node.InterfaceIds', REFERENCE_CLASS,
            '''PPPoE interface info''',
            False, 
            [
            _MetaInfoClassMember('interface-id', REFERENCE_LIST, 'InterfaceId', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_pppoe_ea_oper', 'PppoeEa.Nodes.Node.InterfaceIds.InterfaceId',
                [], [],
                '''                PPPoE interface info
                ''',
                'interface_id',
                'Cisco-IOS-XR-pppoe-ea-oper', False, is_config=False),
            ],
            'Cisco-IOS-XR-pppoe-ea-oper',
            'interface-ids',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-pppoe-ea-oper'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_pppoe_ea_oper',
            is_config=False,
        ),
    },
    'PppoeEa.Nodes.Node' : {
        'meta_info' : _MetaInfoClass('PppoeEa.Nodes.Node', REFERENCE_LIST,
            '''PPPOE-EA operational data for a particular node''',
            False, 
            [
            _MetaInfoClassMember('node-name', ATTRIBUTE, 'str', 'xr:Node-id',
                None, None,
                [], [b'([a-zA-Z0-9_]*\\d+/){1,2}([a-zA-Z0-9_]*\\d+)'],
                '''                Node name
                ''',
                'node_name',
                'Cisco-IOS-XR-pppoe-ea-oper', True, is_config=False),
            _MetaInfoClassMember('parent-interface-ids', REFERENCE_CLASS, 'ParentInterfaceIds', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_pppoe_ea_oper', 'PppoeEa.Nodes.Node.ParentInterfaceIds',
                [], [],
                '''                PPPoE parent interface info
                ''',
                'parent_interface_ids',
                'Cisco-IOS-XR-pppoe-ea-oper', False, is_config=False),
            _MetaInfoClassMember('interface-ids', REFERENCE_CLASS, 'InterfaceIds', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_pppoe_ea_oper', 'PppoeEa.Nodes.Node.InterfaceIds',
                [], [],
                '''                PPPoE interface info
                ''',
                'interface_ids',
                'Cisco-IOS-XR-pppoe-ea-oper', False, is_config=False),
            ],
            'Cisco-IOS-XR-pppoe-ea-oper',
            'node',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-pppoe-ea-oper'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_pppoe_ea_oper',
            is_config=False,
        ),
    },
    'PppoeEa.Nodes' : {
        'meta_info' : _MetaInfoClass('PppoeEa.Nodes', REFERENCE_CLASS,
            '''PPPOE_EA list of nodes''',
            False, 
            [
            _MetaInfoClassMember('node', REFERENCE_LIST, 'Node', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_pppoe_ea_oper', 'PppoeEa.Nodes.Node',
                [], [],
                '''                PPPOE-EA operational data for a particular node
                ''',
                'node',
                'Cisco-IOS-XR-pppoe-ea-oper', False, is_config=False),
            ],
            'Cisco-IOS-XR-pppoe-ea-oper',
            'nodes',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-pppoe-ea-oper'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_pppoe_ea_oper',
            is_config=False,
        ),
    },
    'PppoeEa' : {
        'meta_info' : _MetaInfoClass('PppoeEa', REFERENCE_CLASS,
            '''PPPoE Ea data''',
            False, 
            [
            _MetaInfoClassMember('nodes', REFERENCE_CLASS, 'Nodes', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_pppoe_ea_oper', 'PppoeEa.Nodes',
                [], [],
                '''                PPPOE_EA list of nodes
                ''',
                'nodes',
                'Cisco-IOS-XR-pppoe-ea-oper', False, is_config=False),
            ],
            'Cisco-IOS-XR-pppoe-ea-oper',
            'pppoe-ea',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-pppoe-ea-oper'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_pppoe_ea_oper',
            is_config=False,
        ),
    },
}
_meta_table['PppoeEa.Nodes.Node.ParentInterfaceIds.ParentInterfaceId.SrgvMac']['meta_info'].parent =_meta_table['PppoeEa.Nodes.Node.ParentInterfaceIds.ParentInterfaceId']['meta_info']
_meta_table['PppoeEa.Nodes.Node.ParentInterfaceIds.ParentInterfaceId']['meta_info'].parent =_meta_table['PppoeEa.Nodes.Node.ParentInterfaceIds']['meta_info']
_meta_table['PppoeEa.Nodes.Node.InterfaceIds.InterfaceId.PeerMac']['meta_info'].parent =_meta_table['PppoeEa.Nodes.Node.InterfaceIds.InterfaceId']['meta_info']
_meta_table['PppoeEa.Nodes.Node.InterfaceIds.InterfaceId.LocalMac']['meta_info'].parent =_meta_table['PppoeEa.Nodes.Node.InterfaceIds.InterfaceId']['meta_info']
_meta_table['PppoeEa.Nodes.Node.InterfaceIds.InterfaceId.SrgvMac']['meta_info'].parent =_meta_table['PppoeEa.Nodes.Node.InterfaceIds.InterfaceId']['meta_info']
_meta_table['PppoeEa.Nodes.Node.InterfaceIds.InterfaceId']['meta_info'].parent =_meta_table['PppoeEa.Nodes.Node.InterfaceIds']['meta_info']
_meta_table['PppoeEa.Nodes.Node.ParentInterfaceIds']['meta_info'].parent =_meta_table['PppoeEa.Nodes.Node']['meta_info']
_meta_table['PppoeEa.Nodes.Node.InterfaceIds']['meta_info'].parent =_meta_table['PppoeEa.Nodes.Node']['meta_info']
_meta_table['PppoeEa.Nodes.Node']['meta_info'].parent =_meta_table['PppoeEa.Nodes']['meta_info']
_meta_table['PppoeEa.Nodes']['meta_info'].parent =_meta_table['PppoeEa']['meta_info']
