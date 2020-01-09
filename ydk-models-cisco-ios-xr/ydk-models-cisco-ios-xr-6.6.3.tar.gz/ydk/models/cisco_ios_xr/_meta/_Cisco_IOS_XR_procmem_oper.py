
'''
This is auto-generated file,
which includes metadata for module Cisco_IOS_XR_procmem_oper
'''

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_LIST, REFERENCE_LEAFLIST, REFERENCE_BITS, REFERENCE_UNION
from ydk._core._dm_meta_info import REFERENCE_CLASS, REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, ANYXML_CLASS
from ydk._core._importer import _yang_ns

_meta_table = {
    'ProcessesMemory.Nodes.Node.ProcessIds.ProcessId' : {
        'meta_info' : _MetaInfoClass('ProcessesMemory.Nodes.Node.ProcessIds.ProcessId', REFERENCE_LIST,
            '''Process Id''',
            False, 
            [
            _MetaInfoClassMember('process-id', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('0', '4294967295')], [],
                '''                Process Id
                ''',
                'process_id',
                'Cisco-IOS-XR-procmem-oper', True, is_config=False),
            _MetaInfoClassMember('name', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                Process name
                ''',
                'name',
                'Cisco-IOS-XR-procmem-oper', False, is_config=False),
            _MetaInfoClassMember('jid', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('0', '4294967295')], [],
                '''                Job ID
                ''',
                'jid',
                'Cisco-IOS-XR-procmem-oper', False, is_config=False),
            _MetaInfoClassMember('pid', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('0', '4294967295')], [],
                '''                Process ID
                ''',
                'pid',
                'Cisco-IOS-XR-procmem-oper', False, is_config=False),
            _MetaInfoClassMember('text-seg-size', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('0', '4294967295')], [],
                '''                Text Segment Size in KB
                ''',
                'text_seg_size',
                'Cisco-IOS-XR-procmem-oper', False, is_config=False),
            _MetaInfoClassMember('data-seg-size', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('0', '4294967295')], [],
                '''                Data Segment Size in KB
                ''',
                'data_seg_size',
                'Cisco-IOS-XR-procmem-oper', False, is_config=False),
            _MetaInfoClassMember('stack-seg-size', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('0', '4294967295')], [],
                '''                Stack Segment Size in KB
                ''',
                'stack_seg_size',
                'Cisco-IOS-XR-procmem-oper', False, is_config=False),
            _MetaInfoClassMember('malloc-size', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('0', '4294967295')], [],
                '''                Malloced Memory Size in KB
                ''',
                'malloc_size',
                'Cisco-IOS-XR-procmem-oper', False, is_config=False),
            _MetaInfoClassMember('dyn-limit', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('0', '4294967295')], [],
                '''                Dynamic memory limit in KB (4294967295 for
                RLIM_INFINITY)
                ''',
                'dyn_limit',
                'Cisco-IOS-XR-procmem-oper', False, is_config=False),
            _MetaInfoClassMember('shared-mem', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('0', '4294967295')], [],
                '''                Shared memory size in KB
                ''',
                'shared_mem',
                'Cisco-IOS-XR-procmem-oper', False, is_config=False),
            _MetaInfoClassMember('physical-mem', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('0', '4294967295')], [],
                '''                Physical memory size in KB
                ''',
                'physical_mem',
                'Cisco-IOS-XR-procmem-oper', False, is_config=False),
            ],
            'Cisco-IOS-XR-procmem-oper',
            'process-id',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-procmem-oper'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_procmem_oper',
            is_config=False,
        ),
    },
    'ProcessesMemory.Nodes.Node.ProcessIds' : {
        'meta_info' : _MetaInfoClass('ProcessesMemory.Nodes.Node.ProcessIds', REFERENCE_CLASS,
            '''List of jobs''',
            False, 
            [
            _MetaInfoClassMember('process-id', REFERENCE_LIST, 'ProcessId', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_procmem_oper', 'ProcessesMemory.Nodes.Node.ProcessIds.ProcessId',
                [], [],
                '''                Process Id
                ''',
                'process_id',
                'Cisco-IOS-XR-procmem-oper', False, is_config=False),
            ],
            'Cisco-IOS-XR-procmem-oper',
            'process-ids',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-procmem-oper'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_procmem_oper',
            is_config=False,
        ),
    },
    'ProcessesMemory.Nodes.Node' : {
        'meta_info' : _MetaInfoClass('ProcessesMemory.Nodes.Node', REFERENCE_LIST,
            '''Node ID''',
            False, 
            [
            _MetaInfoClassMember('node-name', ATTRIBUTE, 'str', 'xr:Node-id',
                None, None,
                [], [b'([a-zA-Z0-9_]*\\d+/){1,2}([a-zA-Z0-9_]*\\d+)'],
                '''                Node name
                ''',
                'node_name',
                'Cisco-IOS-XR-procmem-oper', True, is_config=False),
            _MetaInfoClassMember('process-ids', REFERENCE_CLASS, 'ProcessIds', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_procmem_oper', 'ProcessesMemory.Nodes.Node.ProcessIds',
                [], [],
                '''                List of jobs
                ''',
                'process_ids',
                'Cisco-IOS-XR-procmem-oper', False, is_config=False),
            ],
            'Cisco-IOS-XR-procmem-oper',
            'node',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-procmem-oper'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_procmem_oper',
            is_config=False,
        ),
    },
    'ProcessesMemory.Nodes' : {
        'meta_info' : _MetaInfoClass('ProcessesMemory.Nodes', REFERENCE_CLASS,
            '''List of nodes''',
            False, 
            [
            _MetaInfoClassMember('node', REFERENCE_LIST, 'Node', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_procmem_oper', 'ProcessesMemory.Nodes.Node',
                [], [],
                '''                Node ID
                ''',
                'node',
                'Cisco-IOS-XR-procmem-oper', False, is_config=False),
            ],
            'Cisco-IOS-XR-procmem-oper',
            'nodes',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-procmem-oper'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_procmem_oper',
            is_config=False,
        ),
    },
    'ProcessesMemory' : {
        'meta_info' : _MetaInfoClass('ProcessesMemory', REFERENCE_CLASS,
            '''Process statistics''',
            False, 
            [
            _MetaInfoClassMember('nodes', REFERENCE_CLASS, 'Nodes', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_procmem_oper', 'ProcessesMemory.Nodes',
                [], [],
                '''                List of nodes
                ''',
                'nodes',
                'Cisco-IOS-XR-procmem-oper', False, is_config=False),
            ],
            'Cisco-IOS-XR-procmem-oper',
            'processes-memory',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-procmem-oper'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_procmem_oper',
            is_config=False,
        ),
    },
}
_meta_table['ProcessesMemory.Nodes.Node.ProcessIds.ProcessId']['meta_info'].parent =_meta_table['ProcessesMemory.Nodes.Node.ProcessIds']['meta_info']
_meta_table['ProcessesMemory.Nodes.Node.ProcessIds']['meta_info'].parent =_meta_table['ProcessesMemory.Nodes.Node']['meta_info']
_meta_table['ProcessesMemory.Nodes.Node']['meta_info'].parent =_meta_table['ProcessesMemory.Nodes']['meta_info']
_meta_table['ProcessesMemory.Nodes']['meta_info'].parent =_meta_table['ProcessesMemory']['meta_info']
