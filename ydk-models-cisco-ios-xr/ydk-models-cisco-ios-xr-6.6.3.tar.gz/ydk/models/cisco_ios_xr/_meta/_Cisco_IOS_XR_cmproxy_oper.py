
'''
This is auto-generated file,
which includes metadata for module Cisco_IOS_XR_cmproxy_oper
'''

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_LIST, REFERENCE_LEAFLIST, REFERENCE_BITS, REFERENCE_UNION
from ydk._core._dm_meta_info import REFERENCE_CLASS, REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, ANYXML_CLASS
from ydk._core._importer import _yang_ns

_meta_table = {
    'SdrInventoryVm.Nodes.Node.NodeEntries.NodeEntry' : {
        'meta_info' : _MetaInfoClass('SdrInventoryVm.Nodes.Node.NodeEntries.NodeEntry', REFERENCE_LIST,
            '''VM information for a node''',
            False, 
            [
            _MetaInfoClassMember('name', ATTRIBUTE, 'str', 'xr:Cisco-ios-xr-string',
                None, None,
                [], [b'[\\w\\-\\.:,_@#%$\\+=\\|;]+'],
                '''                Node name
                ''',
                'name',
                'Cisco-IOS-XR-cmproxy-oper', True, is_config=False),
            _MetaInfoClassMember('valid', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('0', '4294967295')], [],
                '''                valid flag
                ''',
                'valid',
                'Cisco-IOS-XR-cmproxy-oper', False, is_config=False),
            _MetaInfoClassMember('card-type', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('0', '4294967295')], [],
                '''                card type
                ''',
                'card_type',
                'Cisco-IOS-XR-cmproxy-oper', False, is_config=False),
            _MetaInfoClassMember('card-type-string', ATTRIBUTE, 'str', 'string',
                None, None,
                [(0, 32)], [],
                '''                card type string
                ''',
                'card_type_string',
                'Cisco-IOS-XR-cmproxy-oper', False, is_config=False),
            _MetaInfoClassMember('nodeid', ATTRIBUTE, 'int', 'int32',
                None, None,
                [('-2147483648', '2147483647')], [],
                '''                node ID
                ''',
                'nodeid',
                'Cisco-IOS-XR-cmproxy-oper', False, is_config=False),
            _MetaInfoClassMember('node-name', ATTRIBUTE, 'str', 'string',
                None, None,
                [(0, 32)], [],
                '''                node name string
                ''',
                'node_name',
                'Cisco-IOS-XR-cmproxy-oper', False, is_config=False),
            _MetaInfoClassMember('partner-id', ATTRIBUTE, 'int', 'int32',
                None, None,
                [('-2147483648', '2147483647')], [],
                '''                partner node id
                ''',
                'partner_id',
                'Cisco-IOS-XR-cmproxy-oper', False, is_config=False),
            _MetaInfoClassMember('partner-name', ATTRIBUTE, 'str', 'string',
                None, None,
                [(0, 32)], [],
                '''                partner name string
                ''',
                'partner_name',
                'Cisco-IOS-XR-cmproxy-oper', False, is_config=False),
            _MetaInfoClassMember('red-state', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('0', '4294967295')], [],
                '''                redundancy state
                ''',
                'red_state',
                'Cisco-IOS-XR-cmproxy-oper', False, is_config=False),
            _MetaInfoClassMember('red-state-string', ATTRIBUTE, 'str', 'string',
                None, None,
                [(0, 32)], [],
                '''                redundancy state string
                ''',
                'red_state_string',
                'Cisco-IOS-XR-cmproxy-oper', False, is_config=False),
            _MetaInfoClassMember('node-sw-state', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('0', '4294967295')], [],
                '''                current software state
                ''',
                'node_sw_state',
                'Cisco-IOS-XR-cmproxy-oper', False, is_config=False),
            _MetaInfoClassMember('node-sw-state-string', ATTRIBUTE, 'str', 'string',
                None, None,
                [(0, 32)], [],
                '''                current software state string
                ''',
                'node_sw_state_string',
                'Cisco-IOS-XR-cmproxy-oper', False, is_config=False),
            _MetaInfoClassMember('prev-sw-state', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('0', '4294967295')], [],
                '''                previous software state
                ''',
                'prev_sw_state',
                'Cisco-IOS-XR-cmproxy-oper', False, is_config=False),
            _MetaInfoClassMember('prev-sw-state-string', ATTRIBUTE, 'str', 'string',
                None, None,
                [(0, 32)], [],
                '''                previous software state string
                ''',
                'prev_sw_state_string',
                'Cisco-IOS-XR-cmproxy-oper', False, is_config=False),
            _MetaInfoClassMember('node-ip', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('0', '4294967295')], [],
                '''                node IP address
                ''',
                'node_ip',
                'Cisco-IOS-XR-cmproxy-oper', False, is_config=False),
            _MetaInfoClassMember('node-ipv4-string', ATTRIBUTE, 'str', 'string',
                None, None,
                [(0, 16)], [],
                '''                node IPv4 address string
                ''',
                'node_ipv4_string',
                'Cisco-IOS-XR-cmproxy-oper', False, is_config=False),
            ],
            'Cisco-IOS-XR-cmproxy-oper',
            'node-entry',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-cmproxy-oper'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_cmproxy_oper',
            is_config=False,
        ),
    },
    'SdrInventoryVm.Nodes.Node.NodeEntries' : {
        'meta_info' : _MetaInfoClass('SdrInventoryVm.Nodes.Node.NodeEntries', REFERENCE_CLASS,
            '''VM Information''',
            False, 
            [
            _MetaInfoClassMember('node-entry', REFERENCE_LIST, 'NodeEntry', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_cmproxy_oper', 'SdrInventoryVm.Nodes.Node.NodeEntries.NodeEntry',
                [], [],
                '''                VM information for a node
                ''',
                'node_entry',
                'Cisco-IOS-XR-cmproxy-oper', False, is_config=False),
            ],
            'Cisco-IOS-XR-cmproxy-oper',
            'node-entries',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-cmproxy-oper'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_cmproxy_oper',
            is_config=False,
        ),
    },
    'SdrInventoryVm.Nodes.Node' : {
        'meta_info' : _MetaInfoClass('SdrInventoryVm.Nodes.Node', REFERENCE_LIST,
            '''Node name''',
            False, 
            [
            _MetaInfoClassMember('name', ATTRIBUTE, 'str', 'xr:Cisco-ios-xr-string',
                None, None,
                [], [b'[\\w\\-\\.:,_@#%$\\+=\\|;]+'],
                '''                Node name
                ''',
                'name',
                'Cisco-IOS-XR-cmproxy-oper', True, is_config=False),
            _MetaInfoClassMember('node-entries', REFERENCE_CLASS, 'NodeEntries', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_cmproxy_oper', 'SdrInventoryVm.Nodes.Node.NodeEntries',
                [], [],
                '''                VM Information
                ''',
                'node_entries',
                'Cisco-IOS-XR-cmproxy-oper', False, is_config=False),
            ],
            'Cisco-IOS-XR-cmproxy-oper',
            'node',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-cmproxy-oper'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_cmproxy_oper',
            is_config=False,
        ),
    },
    'SdrInventoryVm.Nodes' : {
        'meta_info' : _MetaInfoClass('SdrInventoryVm.Nodes', REFERENCE_CLASS,
            '''Node directory''',
            False, 
            [
            _MetaInfoClassMember('node', REFERENCE_LIST, 'Node', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_cmproxy_oper', 'SdrInventoryVm.Nodes.Node',
                [], [],
                '''                Node name
                ''',
                'node',
                'Cisco-IOS-XR-cmproxy-oper', False, is_config=False),
            ],
            'Cisco-IOS-XR-cmproxy-oper',
            'nodes',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-cmproxy-oper'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_cmproxy_oper',
            is_config=False,
        ),
    },
    'SdrInventoryVm' : {
        'meta_info' : _MetaInfoClass('SdrInventoryVm', REFERENCE_CLASS,
            '''Platform VM information''',
            False, 
            [
            _MetaInfoClassMember('nodes', REFERENCE_CLASS, 'Nodes', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_cmproxy_oper', 'SdrInventoryVm.Nodes',
                [], [],
                '''                Node directory
                ''',
                'nodes',
                'Cisco-IOS-XR-cmproxy-oper', False, is_config=False),
            ],
            'Cisco-IOS-XR-cmproxy-oper',
            'sdr-inventory-vm',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-cmproxy-oper'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_cmproxy_oper',
            is_config=False,
        ),
    },
}
_meta_table['SdrInventoryVm.Nodes.Node.NodeEntries.NodeEntry']['meta_info'].parent =_meta_table['SdrInventoryVm.Nodes.Node.NodeEntries']['meta_info']
_meta_table['SdrInventoryVm.Nodes.Node.NodeEntries']['meta_info'].parent =_meta_table['SdrInventoryVm.Nodes.Node']['meta_info']
_meta_table['SdrInventoryVm.Nodes.Node']['meta_info'].parent =_meta_table['SdrInventoryVm.Nodes']['meta_info']
_meta_table['SdrInventoryVm.Nodes']['meta_info'].parent =_meta_table['SdrInventoryVm']['meta_info']
