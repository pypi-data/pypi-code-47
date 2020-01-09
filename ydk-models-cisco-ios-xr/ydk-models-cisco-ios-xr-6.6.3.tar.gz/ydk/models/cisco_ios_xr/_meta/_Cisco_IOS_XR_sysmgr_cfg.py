
'''
This is auto-generated file,
which includes metadata for module Cisco_IOS_XR_sysmgr_cfg
'''

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_LIST, REFERENCE_LEAFLIST, REFERENCE_BITS, REFERENCE_UNION
from ydk._core._dm_meta_info import REFERENCE_CLASS, REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, ANYXML_CLASS
from ydk._core._importer import _yang_ns

_meta_table = {
    'ProcessMandatory.Nodes.Node.Processes.Process' : {
        'meta_info' : _MetaInfoClass('ProcessMandatory.Nodes.Node.Processes.Process', REFERENCE_LIST,
            '''Name of the executable process''',
            False, 
            [
            _MetaInfoClassMember('process-name', ATTRIBUTE, 'str', 'xr:Cisco-ios-xr-string',
                None, None,
                [], [b'[\\w\\-\\.:,_@#%$\\+=\\|;]+'],
                '''                Process name
                ''',
                'process_name',
                'Cisco-IOS-XR-sysmgr-cfg', True),
            ],
            'Cisco-IOS-XR-sysmgr-cfg',
            'process',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-sysmgr-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysmgr_cfg',
        ),
    },
    'ProcessMandatory.Nodes.Node.Processes' : {
        'meta_info' : _MetaInfoClass('ProcessMandatory.Nodes.Node.Processes', REFERENCE_CLASS,
            '''Table of processes''',
            False, 
            [
            _MetaInfoClassMember('process', REFERENCE_LIST, 'Process', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysmgr_cfg', 'ProcessMandatory.Nodes.Node.Processes.Process',
                [], [],
                '''                Name of the executable process
                ''',
                'process',
                'Cisco-IOS-XR-sysmgr-cfg', False),
            ],
            'Cisco-IOS-XR-sysmgr-cfg',
            'processes',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-sysmgr-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysmgr_cfg',
        ),
    },
    'ProcessMandatory.Nodes.Node' : {
        'meta_info' : _MetaInfoClass('ProcessMandatory.Nodes.Node', REFERENCE_LIST,
            '''Mandatory node''',
            False, 
            [
            _MetaInfoClassMember('node-name', ATTRIBUTE, 'str', 'xr:Node-id',
                None, None,
                [], [b'([a-zA-Z0-9_]*\\d+/){1,2}([a-zA-Z0-9_]*\\d+)'],
                '''                Node name
                ''',
                'node_name',
                'Cisco-IOS-XR-sysmgr-cfg', True),
            _MetaInfoClassMember('processes', REFERENCE_CLASS, 'Processes', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysmgr_cfg', 'ProcessMandatory.Nodes.Node.Processes',
                [], [],
                '''                Table of processes
                ''',
                'processes',
                'Cisco-IOS-XR-sysmgr-cfg', False),
            ],
            'Cisco-IOS-XR-sysmgr-cfg',
            'node',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-sysmgr-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysmgr_cfg',
        ),
    },
    'ProcessMandatory.Nodes' : {
        'meta_info' : _MetaInfoClass('ProcessMandatory.Nodes', REFERENCE_CLASS,
            '''Table of mandatory nodes''',
            False, 
            [
            _MetaInfoClassMember('node', REFERENCE_LIST, 'Node', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysmgr_cfg', 'ProcessMandatory.Nodes.Node',
                [], [],
                '''                Mandatory node
                ''',
                'node',
                'Cisco-IOS-XR-sysmgr-cfg', False),
            ],
            'Cisco-IOS-XR-sysmgr-cfg',
            'nodes',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-sysmgr-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysmgr_cfg',
        ),
    },
    'ProcessMandatory.All.Processes.Process' : {
        'meta_info' : _MetaInfoClass('ProcessMandatory.All.Processes.Process', REFERENCE_LIST,
            '''Name of the executable process''',
            False, 
            [
            _MetaInfoClassMember('process-name', ATTRIBUTE, 'str', 'xr:Cisco-ios-xr-string',
                None, None,
                [], [b'[\\w\\-\\.:,_@#%$\\+=\\|;]+'],
                '''                Process name
                ''',
                'process_name',
                'Cisco-IOS-XR-sysmgr-cfg', True),
            ],
            'Cisco-IOS-XR-sysmgr-cfg',
            'process',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-sysmgr-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysmgr_cfg',
        ),
    },
    'ProcessMandatory.All.Processes' : {
        'meta_info' : _MetaInfoClass('ProcessMandatory.All.Processes', REFERENCE_CLASS,
            '''Table of processes''',
            False, 
            [
            _MetaInfoClassMember('process', REFERENCE_LIST, 'Process', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysmgr_cfg', 'ProcessMandatory.All.Processes.Process',
                [], [],
                '''                Name of the executable process
                ''',
                'process',
                'Cisco-IOS-XR-sysmgr-cfg', False),
            ],
            'Cisco-IOS-XR-sysmgr-cfg',
            'processes',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-sysmgr-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysmgr_cfg',
        ),
    },
    'ProcessMandatory.All' : {
        'meta_info' : _MetaInfoClass('ProcessMandatory.All', REFERENCE_CLASS,
            '''Mandatory for all nodes''',
            False, 
            [
            _MetaInfoClassMember('processes', REFERENCE_CLASS, 'Processes', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysmgr_cfg', 'ProcessMandatory.All.Processes',
                [], [],
                '''                Table of processes
                ''',
                'processes',
                'Cisco-IOS-XR-sysmgr-cfg', False),
            ],
            'Cisco-IOS-XR-sysmgr-cfg',
            'all',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-sysmgr-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysmgr_cfg',
        ),
    },
    'ProcessMandatory' : {
        'meta_info' : _MetaInfoClass('ProcessMandatory', REFERENCE_CLASS,
            '''Process mandatory configuration''',
            False, 
            [
            _MetaInfoClassMember('nodes', REFERENCE_CLASS, 'Nodes', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysmgr_cfg', 'ProcessMandatory.Nodes',
                [], [],
                '''                Table of mandatory nodes
                ''',
                'nodes',
                'Cisco-IOS-XR-sysmgr-cfg', False),
            _MetaInfoClassMember('all', REFERENCE_CLASS, 'All', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysmgr_cfg', 'ProcessMandatory.All',
                [], [],
                '''                Mandatory for all nodes
                ''',
                'all',
                'Cisco-IOS-XR-sysmgr-cfg', False),
            ],
            'Cisco-IOS-XR-sysmgr-cfg',
            'process-mandatory',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-sysmgr-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysmgr_cfg',
        ),
    },
    'ProcessSingleCrash' : {
        'meta_info' : _MetaInfoClass('ProcessSingleCrash', REFERENCE_CLASS,
            '''process single crash''',
            False, 
            [
            _MetaInfoClassMember('crashes', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('1', '500')], [],
                '''                Number of crashes for a process to trigger
                reboot
                ''',
                'crashes',
                'Cisco-IOS-XR-sysmgr-cfg', False, is_mandatory=True),
            _MetaInfoClassMember('minimum-up-time', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('0', '4294967295')], [],
                '''                Minimum process up time (in seconds) to reset
                crash count
                ''',
                'minimum_up_time',
                'Cisco-IOS-XR-sysmgr-cfg', False, default_value="0"),
            ],
            'Cisco-IOS-XR-sysmgr-cfg',
            'process-single-crash',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-sysmgr-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysmgr_cfg',
            is_presence=True,
        ),
    },
}
_meta_table['ProcessMandatory.Nodes.Node.Processes.Process']['meta_info'].parent =_meta_table['ProcessMandatory.Nodes.Node.Processes']['meta_info']
_meta_table['ProcessMandatory.Nodes.Node.Processes']['meta_info'].parent =_meta_table['ProcessMandatory.Nodes.Node']['meta_info']
_meta_table['ProcessMandatory.Nodes.Node']['meta_info'].parent =_meta_table['ProcessMandatory.Nodes']['meta_info']
_meta_table['ProcessMandatory.All.Processes.Process']['meta_info'].parent =_meta_table['ProcessMandatory.All.Processes']['meta_info']
_meta_table['ProcessMandatory.All.Processes']['meta_info'].parent =_meta_table['ProcessMandatory.All']['meta_info']
_meta_table['ProcessMandatory.Nodes']['meta_info'].parent =_meta_table['ProcessMandatory']['meta_info']
_meta_table['ProcessMandatory.All']['meta_info'].parent =_meta_table['ProcessMandatory']['meta_info']
