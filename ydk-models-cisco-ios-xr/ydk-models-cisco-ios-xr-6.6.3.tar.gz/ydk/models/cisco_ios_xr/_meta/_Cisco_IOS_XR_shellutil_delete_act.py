
'''
This is auto-generated file,
which includes metadata for module Cisco_IOS_XR_shellutil_delete_act
'''

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_LIST, REFERENCE_LEAFLIST, REFERENCE_BITS, REFERENCE_UNION
from ydk._core._dm_meta_info import REFERENCE_CLASS, REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, ANYXML_CLASS
from ydk._core._importer import _yang_ns

_meta_table = {
    'Delete.Input' : {
        'meta_info' : _MetaInfoClass('Delete.Input', REFERENCE_CLASS,
            ''' ''',
            False, 
            [
            _MetaInfoClassMember('name', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                file name
                ''',
                'name',
                'Cisco-IOS-XR-shellutil-delete-act', False, is_mandatory=True),
            _MetaInfoClassMember('location', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                location
                ''',
                'location',
                'Cisco-IOS-XR-shellutil-delete-act', False),
            _MetaInfoClassMember('recurse', ATTRIBUTE, 'bool', 'boolean',
                None, None,
                [], [],
                '''                Files in dir
                ''',
                'recurse',
                'Cisco-IOS-XR-shellutil-delete-act', False),
            ],
            'Cisco-IOS-XR-shellutil-delete-act',
            'input',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-shellutil-delete-act'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_shellutil_delete_act',
        ),
    },
    'Delete.Output' : {
        'meta_info' : _MetaInfoClass('Delete.Output', REFERENCE_CLASS,
            ''' ''',
            False, 
            [
            _MetaInfoClassMember('response', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                Status of delete operation
                ''',
                'response',
                'Cisco-IOS-XR-shellutil-delete-act', False),
            ],
            'Cisco-IOS-XR-shellutil-delete-act',
            'output',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-shellutil-delete-act'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_shellutil_delete_act',
        ),
    },
    'Delete' : {
        'meta_info' : _MetaInfoClass('Delete', REFERENCE_CLASS,
            ''' ''',
            False, 
            [
            _MetaInfoClassMember('input', REFERENCE_CLASS, 'Input', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_shellutil_delete_act', 'Delete.Input',
                [], [],
                '''                ''',
                'input',
                'Cisco-IOS-XR-shellutil-delete-act', False),
            _MetaInfoClassMember('output', REFERENCE_CLASS, 'Output', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_shellutil_delete_act', 'Delete.Output',
                [], [],
                '''                ''',
                'output',
                'Cisco-IOS-XR-shellutil-delete-act', False),
            ],
            'Cisco-IOS-XR-shellutil-delete-act',
            'delete',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-shellutil-delete-act'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_shellutil_delete_act',
        ),
    },
}
_meta_table['Delete.Input']['meta_info'].parent =_meta_table['Delete']['meta_info']
_meta_table['Delete.Output']['meta_info'].parent =_meta_table['Delete']['meta_info']
