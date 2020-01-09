
'''
This is auto-generated file,
which includes metadata for module Cisco_IOS_XR_sysdb_oper
'''

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_LIST, REFERENCE_LEAFLIST, REFERENCE_BITS, REFERENCE_UNION
from ydk._core._dm_meta_info import REFERENCE_CLASS, REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, ANYXML_CLASS
from ydk._core._importer import _yang_ns

_meta_table = {
    'SysdbConnections.Nodes.Node' : {
        'meta_info' : _MetaInfoClass('SysdbConnections.Nodes.Node', REFERENCE_LIST,
            '''Per-node Sysdb health on connection''',
            False, 
            [
            _MetaInfoClassMember('node-name', ATTRIBUTE, 'str', 'xr:Node-id',
                None, None,
                [], [b'([a-zA-Z0-9_]*\\d+/){1,2}([a-zA-Z0-9_]*\\d+)'],
                '''                Node name
                ''',
                'node_name',
                'Cisco-IOS-XR-sysdb-oper', True, is_config=False),
            _MetaInfoClassMember('connections', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                Per-node Sysdb Client Connections
                ''',
                'connections',
                'Cisco-IOS-XR-sysdb-oper', False, is_config=False),
            ],
            'Cisco-IOS-XR-sysdb-oper',
            'node',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-sysdb-oper'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysdb_oper',
            is_config=False,
        ),
    },
    'SysdbConnections.Nodes' : {
        'meta_info' : _MetaInfoClass('SysdbConnections.Nodes', REFERENCE_CLASS,
            '''Node operational data''',
            False, 
            [
            _MetaInfoClassMember('node', REFERENCE_LIST, 'Node', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysdb_oper', 'SysdbConnections.Nodes.Node',
                [], [],
                '''                Per-node Sysdb health on connection
                ''',
                'node',
                'Cisco-IOS-XR-sysdb-oper', False, is_config=False),
            ],
            'Cisco-IOS-XR-sysdb-oper',
            'nodes',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-sysdb-oper'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysdb_oper',
            is_config=False,
        ),
    },
    'SysdbConnections' : {
        'meta_info' : _MetaInfoClass('SysdbConnections', REFERENCE_CLASS,
            '''Sysdb health on client connections''',
            False, 
            [
            _MetaInfoClassMember('nodes', REFERENCE_CLASS, 'Nodes', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysdb_oper', 'SysdbConnections.Nodes',
                [], [],
                '''                Node operational data
                ''',
                'nodes',
                'Cisco-IOS-XR-sysdb-oper', False, is_config=False),
            ],
            'Cisco-IOS-XR-sysdb-oper',
            'sysdb-connections',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-sysdb-oper'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysdb_oper',
            is_config=False,
        ),
    },
    'Sysdb' : {
        'meta_info' : _MetaInfoClass('Sysdb', REFERENCE_CLASS,
            '''sysdb''',
            False, 
            [
            _MetaInfoClassMember('configuration-space', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                Sysdb health for configuration space
                ''',
                'configuration_space',
                'Cisco-IOS-XR-sysdb-oper', False, is_config=False),
            _MetaInfoClassMember('memory', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                Sysdb health on memory consumption
                ''',
                'memory',
                'Cisco-IOS-XR-sysdb-oper', False, is_config=False),
            _MetaInfoClassMember('ipc-space', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                Sysdb health for operational space
                ''',
                'ipc_space',
                'Cisco-IOS-XR-sysdb-oper', False, is_config=False),
            _MetaInfoClassMember('cpu', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                Sysdb health on cpu consumption
                ''',
                'cpu',
                'Cisco-IOS-XR-sysdb-oper', False, is_config=False),
            ],
            'Cisco-IOS-XR-sysdb-oper',
            'sysdb',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-sysdb-oper'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysdb_oper',
            is_config=False,
        ),
    },
}
_meta_table['SysdbConnections.Nodes.Node']['meta_info'].parent =_meta_table['SysdbConnections.Nodes']['meta_info']
_meta_table['SysdbConnections.Nodes']['meta_info'].parent =_meta_table['SysdbConnections']['meta_info']
