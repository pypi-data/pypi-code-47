
'''
This is auto-generated file,
which includes metadata for module Cisco_IOS_XR_mpls_io_oper
'''

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_LIST, REFERENCE_LEAFLIST, REFERENCE_BITS, REFERENCE_UNION
from ydk._core._dm_meta_info import REFERENCE_CLASS, REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, ANYXML_CLASS
from ydk._core._importer import _yang_ns

_meta_table = {
    'MplsEa.Nodes.Node.Interfaces.Interface' : {
        'meta_info' : _MetaInfoClass('MplsEa.Nodes.Node.Interfaces.Interface', REFERENCE_LIST,
            '''MPLS IO EA NODE Interface data ''',
            False, 
            [
            _MetaInfoClassMember('interface-name', ATTRIBUTE, 'str', 'xr:Interface-name',
                None, None,
                [], [b'[a-zA-Z0-9._/-]+'],
                '''                Interface name
                ''',
                'interface_name',
                'Cisco-IOS-XR-mpls-io-oper', True, is_config=False),
            _MetaInfoClassMember('mtu', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('0', '4294967295')], [],
                '''                MTU for fragmentation
                ''',
                'mtu',
                'Cisco-IOS-XR-mpls-io-oper', False, is_config=False),
            _MetaInfoClassMember('bkp-label-stack-depth', ATTRIBUTE, 'int', 'uint8',
                None, None,
                [('0', '255')], [],
                '''                Bkp Label Stack Depth
                ''',
                'bkp_label_stack_depth',
                'Cisco-IOS-XR-mpls-io-oper', False, is_config=False),
            _MetaInfoClassMember('srte-label-stack-depth', ATTRIBUTE, 'int', 'uint8',
                None, None,
                [('0', '255')], [],
                '''                Srte Label Stack Depth
                ''',
                'srte_label_stack_depth',
                'Cisco-IOS-XR-mpls-io-oper', False, is_config=False),
            _MetaInfoClassMember('pri-label-stack-depth', ATTRIBUTE, 'int', 'uint8',
                None, None,
                [('0', '255')], [],
                '''                Pri Label Stack Depth
                ''',
                'pri_label_stack_depth',
                'Cisco-IOS-XR-mpls-io-oper', False, is_config=False),
            ],
            'Cisco-IOS-XR-mpls-io-oper',
            'interface',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-mpls-io-oper'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_io_oper',
            is_config=False,
        ),
    },
    'MplsEa.Nodes.Node.Interfaces' : {
        'meta_info' : _MetaInfoClass('MplsEa.Nodes.Node.Interfaces', REFERENCE_CLASS,
            '''MPLS IO EA Interfaces information ''',
            False, 
            [
            _MetaInfoClassMember('interface', REFERENCE_LIST, 'Interface', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_io_oper', 'MplsEa.Nodes.Node.Interfaces.Interface',
                [], [],
                '''                MPLS IO EA NODE Interface data 
                ''',
                'interface',
                'Cisco-IOS-XR-mpls-io-oper', False, is_config=False),
            ],
            'Cisco-IOS-XR-mpls-io-oper',
            'interfaces',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-mpls-io-oper'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_io_oper',
            is_config=False,
        ),
    },
    'MplsEa.Nodes.Node' : {
        'meta_info' : _MetaInfoClass('MplsEa.Nodes.Node', REFERENCE_LIST,
            '''Per node MPLS IO EA operational data''',
            False, 
            [
            _MetaInfoClassMember('node-name', ATTRIBUTE, 'str', 'xr:Node-id',
                None, None,
                [], [b'([a-zA-Z0-9_]*\\d+/){1,2}([a-zA-Z0-9_]*\\d+)'],
                '''                Node ID
                ''',
                'node_name',
                'Cisco-IOS-XR-mpls-io-oper', True, is_config=False),
            _MetaInfoClassMember('interfaces', REFERENCE_CLASS, 'Interfaces', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_io_oper', 'MplsEa.Nodes.Node.Interfaces',
                [], [],
                '''                MPLS IO EA Interfaces information 
                ''',
                'interfaces',
                'Cisco-IOS-XR-mpls-io-oper', False, is_config=False),
            ],
            'Cisco-IOS-XR-mpls-io-oper',
            'node',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-mpls-io-oper'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_io_oper',
            is_config=False,
        ),
    },
    'MplsEa.Nodes' : {
        'meta_info' : _MetaInfoClass('MplsEa.Nodes', REFERENCE_CLASS,
            '''NODE container class for MPLS IO EA operational
data''',
            False, 
            [
            _MetaInfoClassMember('node', REFERENCE_LIST, 'Node', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_io_oper', 'MplsEa.Nodes.Node',
                [], [],
                '''                Per node MPLS IO EA operational data
                ''',
                'node',
                'Cisco-IOS-XR-mpls-io-oper', False, is_config=False),
            ],
            'Cisco-IOS-XR-mpls-io-oper',
            'nodes',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-mpls-io-oper'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_io_oper',
            is_config=False,
        ),
    },
    'MplsEa' : {
        'meta_info' : _MetaInfoClass('MplsEa', REFERENCE_CLASS,
            '''MPLS IO EA operational data''',
            False, 
            [
            _MetaInfoClassMember('nodes', REFERENCE_CLASS, 'Nodes', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_io_oper', 'MplsEa.Nodes',
                [], [],
                '''                NODE container class for MPLS IO EA operational
                data
                ''',
                'nodes',
                'Cisco-IOS-XR-mpls-io-oper', False, is_config=False),
            ],
            'Cisco-IOS-XR-mpls-io-oper',
            'mpls-ea',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-mpls-io-oper'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_io_oper',
            is_config=False,
        ),
    },
    'MplsMa.Nodes.Node.Interfaces.Interface' : {
        'meta_info' : _MetaInfoClass('MplsMa.Nodes.Node.Interfaces.Interface', REFERENCE_LIST,
            '''MPLS IO MA NODE Interface data ''',
            False, 
            [
            _MetaInfoClassMember('interface-name', ATTRIBUTE, 'str', 'xr:Interface-name',
                None, None,
                [], [b'[a-zA-Z0-9._/-]+'],
                '''                Interface name
                ''',
                'interface_name',
                'Cisco-IOS-XR-mpls-io-oper', True, is_config=False),
            _MetaInfoClassMember('mtu', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('0', '4294967295')], [],
                '''                MTU for fragmentation
                ''',
                'mtu',
                'Cisco-IOS-XR-mpls-io-oper', False, is_config=False),
            _MetaInfoClassMember('bkp-label-stack-depth', ATTRIBUTE, 'int', 'uint8',
                None, None,
                [('0', '255')], [],
                '''                Bkp Label Stack Depth
                ''',
                'bkp_label_stack_depth',
                'Cisco-IOS-XR-mpls-io-oper', False, is_config=False),
            _MetaInfoClassMember('srte-label-stack-depth', ATTRIBUTE, 'int', 'uint8',
                None, None,
                [('0', '255')], [],
                '''                Srte Label Stack Depth
                ''',
                'srte_label_stack_depth',
                'Cisco-IOS-XR-mpls-io-oper', False, is_config=False),
            _MetaInfoClassMember('pri-label-stack-depth', ATTRIBUTE, 'int', 'uint8',
                None, None,
                [('0', '255')], [],
                '''                Pri Label Stack Depth
                ''',
                'pri_label_stack_depth',
                'Cisco-IOS-XR-mpls-io-oper', False, is_config=False),
            ],
            'Cisco-IOS-XR-mpls-io-oper',
            'interface',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-mpls-io-oper'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_io_oper',
            is_config=False,
        ),
    },
    'MplsMa.Nodes.Node.Interfaces' : {
        'meta_info' : _MetaInfoClass('MplsMa.Nodes.Node.Interfaces', REFERENCE_CLASS,
            '''MPLS IO MA Interfaces information ''',
            False, 
            [
            _MetaInfoClassMember('interface', REFERENCE_LIST, 'Interface', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_io_oper', 'MplsMa.Nodes.Node.Interfaces.Interface',
                [], [],
                '''                MPLS IO MA NODE Interface data 
                ''',
                'interface',
                'Cisco-IOS-XR-mpls-io-oper', False, is_config=False),
            ],
            'Cisco-IOS-XR-mpls-io-oper',
            'interfaces',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-mpls-io-oper'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_io_oper',
            is_config=False,
        ),
    },
    'MplsMa.Nodes.Node' : {
        'meta_info' : _MetaInfoClass('MplsMa.Nodes.Node', REFERENCE_LIST,
            '''Per node MPLS IO MA operational data''',
            False, 
            [
            _MetaInfoClassMember('node-name', ATTRIBUTE, 'str', 'xr:Node-id',
                None, None,
                [], [b'([a-zA-Z0-9_]*\\d+/){1,2}([a-zA-Z0-9_]*\\d+)'],
                '''                Node ID
                ''',
                'node_name',
                'Cisco-IOS-XR-mpls-io-oper', True, is_config=False),
            _MetaInfoClassMember('interfaces', REFERENCE_CLASS, 'Interfaces', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_io_oper', 'MplsMa.Nodes.Node.Interfaces',
                [], [],
                '''                MPLS IO MA Interfaces information 
                ''',
                'interfaces',
                'Cisco-IOS-XR-mpls-io-oper', False, is_config=False),
            ],
            'Cisco-IOS-XR-mpls-io-oper',
            'node',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-mpls-io-oper'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_io_oper',
            is_config=False,
        ),
    },
    'MplsMa.Nodes' : {
        'meta_info' : _MetaInfoClass('MplsMa.Nodes', REFERENCE_CLASS,
            '''NODE container class for MPLS IO MA operational
data''',
            False, 
            [
            _MetaInfoClassMember('node', REFERENCE_LIST, 'Node', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_io_oper', 'MplsMa.Nodes.Node',
                [], [],
                '''                Per node MPLS IO MA operational data
                ''',
                'node',
                'Cisco-IOS-XR-mpls-io-oper', False, is_config=False),
            ],
            'Cisco-IOS-XR-mpls-io-oper',
            'nodes',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-mpls-io-oper'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_io_oper',
            is_config=False,
        ),
    },
    'MplsMa' : {
        'meta_info' : _MetaInfoClass('MplsMa', REFERENCE_CLASS,
            '''mpls ma''',
            False, 
            [
            _MetaInfoClassMember('nodes', REFERENCE_CLASS, 'Nodes', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_io_oper', 'MplsMa.Nodes',
                [], [],
                '''                NODE container class for MPLS IO MA operational
                data
                ''',
                'nodes',
                'Cisco-IOS-XR-mpls-io-oper', False, is_config=False),
            ],
            'Cisco-IOS-XR-mpls-io-oper',
            'mpls-ma',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-mpls-io-oper'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_io_oper',
            is_config=False,
        ),
    },
}
_meta_table['MplsEa.Nodes.Node.Interfaces.Interface']['meta_info'].parent =_meta_table['MplsEa.Nodes.Node.Interfaces']['meta_info']
_meta_table['MplsEa.Nodes.Node.Interfaces']['meta_info'].parent =_meta_table['MplsEa.Nodes.Node']['meta_info']
_meta_table['MplsEa.Nodes.Node']['meta_info'].parent =_meta_table['MplsEa.Nodes']['meta_info']
_meta_table['MplsEa.Nodes']['meta_info'].parent =_meta_table['MplsEa']['meta_info']
_meta_table['MplsMa.Nodes.Node.Interfaces.Interface']['meta_info'].parent =_meta_table['MplsMa.Nodes.Node.Interfaces']['meta_info']
_meta_table['MplsMa.Nodes.Node.Interfaces']['meta_info'].parent =_meta_table['MplsMa.Nodes.Node']['meta_info']
_meta_table['MplsMa.Nodes.Node']['meta_info'].parent =_meta_table['MplsMa.Nodes']['meta_info']
_meta_table['MplsMa.Nodes']['meta_info'].parent =_meta_table['MplsMa']['meta_info']
