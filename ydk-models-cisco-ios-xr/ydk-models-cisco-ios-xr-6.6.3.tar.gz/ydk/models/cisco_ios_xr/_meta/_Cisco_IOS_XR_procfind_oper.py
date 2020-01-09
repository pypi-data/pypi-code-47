
'''
This is auto-generated file,
which includes metadata for module Cisco_IOS_XR_procfind_oper
'''

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_LIST, REFERENCE_LEAFLIST, REFERENCE_BITS, REFERENCE_UNION
from ydk._core._dm_meta_info import REFERENCE_CLASS, REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, ANYXML_CLASS
from ydk._core._importer import _yang_ns

_meta_table = {
    'ProcDistribution.Nodes.Node.Process.FilterType' : {
        'meta_info' : _MetaInfoClass('ProcDistribution.Nodes.Node.Process.FilterType', REFERENCE_LIST,
            '''Process distribution information''',
            False, 
            [
            _MetaInfoClassMember('filter-type', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                Filter Type
                ''',
                'filter_type',
                'Cisco-IOS-XR-procfind-oper', True, is_config=False),
            _MetaInfoClassMember('nodeid', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('0', '4294967295')], [],
                '''                Node ID
                ''',
                'nodeid',
                'Cisco-IOS-XR-procfind-oper', False, is_config=False),
            _MetaInfoClassMember('nodetype', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('0', '4294967295')], [],
                '''                Node type
                ''',
                'nodetype',
                'Cisco-IOS-XR-procfind-oper', False, is_config=False),
            _MetaInfoClassMember('pid', ATTRIBUTE, 'int', 'int32',
                None, None,
                [('-2147483648', '2147483647')], [],
                '''                Process ID
                ''',
                'pid',
                'Cisco-IOS-XR-procfind-oper', False, is_config=False),
            _MetaInfoClassMember('jid', ATTRIBUTE, 'int', 'int32',
                None, None,
                [('-2147483648', '2147483647')], [],
                '''                Job ID
                ''',
                'jid',
                'Cisco-IOS-XR-procfind-oper', False, is_config=False),
            _MetaInfoClassMember('num-threads', ATTRIBUTE, 'int', 'int32',
                None, None,
                [('-2147483648', '2147483647')], [],
                '''                Number of threads
                ''',
                'num_threads',
                'Cisco-IOS-XR-procfind-oper', False, is_config=False),
            _MetaInfoClassMember('name', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                Process name
                ''',
                'name',
                'Cisco-IOS-XR-procfind-oper', False, is_config=False),
            ],
            'Cisco-IOS-XR-procfind-oper',
            'filter-type',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-procfind-oper'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_procfind_oper',
            is_config=False,
        ),
    },
    'ProcDistribution.Nodes.Node.Process' : {
        'meta_info' : _MetaInfoClass('ProcDistribution.Nodes.Node.Process', REFERENCE_LIST,
            '''Process distribution information''',
            False, 
            [
            _MetaInfoClassMember('proc-name', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                Process Name
                ''',
                'proc_name',
                'Cisco-IOS-XR-procfind-oper', True, is_config=False),
            _MetaInfoClassMember('filter-type', REFERENCE_LIST, 'FilterType', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_procfind_oper', 'ProcDistribution.Nodes.Node.Process.FilterType',
                [], [],
                '''                Process distribution information
                ''',
                'filter_type',
                'Cisco-IOS-XR-procfind-oper', False, is_config=False),
            ],
            'Cisco-IOS-XR-procfind-oper',
            'process',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-procfind-oper'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_procfind_oper',
            is_config=False,
        ),
    },
    'ProcDistribution.Nodes.Node' : {
        'meta_info' : _MetaInfoClass('ProcDistribution.Nodes.Node', REFERENCE_LIST,
            '''Process distribution information per node''',
            False, 
            [
            _MetaInfoClassMember('node-name', ATTRIBUTE, 'str', 'xr:Node-id',
                None, None,
                [], [b'([a-zA-Z0-9_]*\\d+/){1,2}([a-zA-Z0-9_]*\\d+)'],
                '''                The node name
                ''',
                'node_name',
                'Cisco-IOS-XR-procfind-oper', True, is_config=False),
            _MetaInfoClassMember('process', REFERENCE_LIST, 'Process', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_procfind_oper', 'ProcDistribution.Nodes.Node.Process',
                [], [],
                '''                Process distribution information
                ''',
                'process',
                'Cisco-IOS-XR-procfind-oper', False, is_config=False),
            ],
            'Cisco-IOS-XR-procfind-oper',
            'node',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-procfind-oper'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_procfind_oper',
            is_config=False,
        ),
    },
    'ProcDistribution.Nodes' : {
        'meta_info' : _MetaInfoClass('ProcDistribution.Nodes', REFERENCE_CLASS,
            '''List of nodes''',
            False, 
            [
            _MetaInfoClassMember('node', REFERENCE_LIST, 'Node', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_procfind_oper', 'ProcDistribution.Nodes.Node',
                [], [],
                '''                Process distribution information per node
                ''',
                'node',
                'Cisco-IOS-XR-procfind-oper', False, is_config=False),
            ],
            'Cisco-IOS-XR-procfind-oper',
            'nodes',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-procfind-oper'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_procfind_oper',
            is_config=False,
        ),
    },
    'ProcDistribution' : {
        'meta_info' : _MetaInfoClass('ProcDistribution', REFERENCE_CLASS,
            '''Process distribution information''',
            False, 
            [
            _MetaInfoClassMember('nodes', REFERENCE_CLASS, 'Nodes', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_procfind_oper', 'ProcDistribution.Nodes',
                [], [],
                '''                List of nodes
                ''',
                'nodes',
                'Cisco-IOS-XR-procfind-oper', False, is_config=False),
            ],
            'Cisco-IOS-XR-procfind-oper',
            'proc-distribution',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-procfind-oper'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_procfind_oper',
            is_config=False,
        ),
    },
}
_meta_table['ProcDistribution.Nodes.Node.Process.FilterType']['meta_info'].parent =_meta_table['ProcDistribution.Nodes.Node.Process']['meta_info']
_meta_table['ProcDistribution.Nodes.Node.Process']['meta_info'].parent =_meta_table['ProcDistribution.Nodes.Node']['meta_info']
_meta_table['ProcDistribution.Nodes.Node']['meta_info'].parent =_meta_table['ProcDistribution.Nodes']['meta_info']
_meta_table['ProcDistribution.Nodes']['meta_info'].parent =_meta_table['ProcDistribution']['meta_info']
