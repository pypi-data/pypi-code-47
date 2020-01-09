
'''
This is auto-generated file,
which includes metadata for module tailf_actions
'''

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_LIST, REFERENCE_LEAFLIST, REFERENCE_BITS, REFERENCE_UNION
from ydk._core._dm_meta_info import REFERENCE_CLASS, REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, ANYXML_CLASS
from ydk._core._importer import _yang_ns

_meta_table = {
    'Action.Input' : {
        'meta_info' : _MetaInfoClass('Action.Input', REFERENCE_CLASS,
            ''' ''',
            False, 
            [
            _MetaInfoClassMember('data', ANYXML_CLASS, 'object', '',
                None, None,
                [], [],
                '''                Data section of the YANG action hierarchy.
                ''',
                'data',
                'tailf-actions', False),
            ],
            'tailf-actions',
            'input',
            _yang_ns.NAMESPACE_LOOKUP['tailf-actions'],
            'ydk.models.cisco_ios_xr.tailf_actions',
        ),
    },
    'Action.Output' : {
        'meta_info' : _MetaInfoClass('Action.Output', REFERENCE_CLASS,
            ''' ''',
            False, 
            [
            _MetaInfoClassMember('data', ANYXML_CLASS, 'object', '',
                None, None,
                [], [],
                '''                Data and messages returned by the Tail-F ConfD agent.
                ''',
                'data',
                'tailf-actions', False),
            ],
            'tailf-actions',
            'output',
            _yang_ns.NAMESPACE_LOOKUP['tailf-actions'],
            'ydk.models.cisco_ios_xr.tailf_actions',
        ),
    },
    'Action' : {
        'meta_info' : _MetaInfoClass('Action', REFERENCE_CLASS,
            '''Support Tail-F actions rpc format.''',
            False, 
            [
            _MetaInfoClassMember('input', REFERENCE_CLASS, 'Input', '',
                'ydk.models.cisco_ios_xr.tailf_actions', 'Action.Input',
                [], [],
                '''                ''',
                'input',
                'tailf-actions', False),
            _MetaInfoClassMember('output', REFERENCE_CLASS, 'Output', '',
                'ydk.models.cisco_ios_xr.tailf_actions', 'Action.Output',
                [], [],
                '''                ''',
                'output',
                'tailf-actions', False),
            ],
            'tailf-actions',
            'action',
            _yang_ns.NAMESPACE_LOOKUP['tailf-actions'],
            'ydk.models.cisco_ios_xr.tailf_actions',
        ),
    },
}
_meta_table['Action.Input']['meta_info'].parent =_meta_table['Action']['meta_info']
_meta_table['Action.Output']['meta_info'].parent =_meta_table['Action']['meta_info']
