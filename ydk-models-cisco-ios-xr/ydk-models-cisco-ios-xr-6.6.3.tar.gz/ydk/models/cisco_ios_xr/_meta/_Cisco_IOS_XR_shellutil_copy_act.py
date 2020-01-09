
'''
This is auto-generated file,
which includes metadata for module Cisco_IOS_XR_shellutil_copy_act
'''

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_LIST, REFERENCE_LEAFLIST, REFERENCE_BITS, REFERENCE_UNION
from ydk._core._dm_meta_info import REFERENCE_CLASS, REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, ANYXML_CLASS
from ydk._core._importer import _yang_ns

_meta_table = {
    'Copy.Input' : {
        'meta_info' : _MetaInfoClass('Copy.Input', REFERENCE_CLASS,
            ''' ''',
            False, 
            [
            _MetaInfoClassMember('sourcename', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                source file name to copy
                ''',
                'sourcename',
                'Cisco-IOS-XR-shellutil-copy-act', False),
            _MetaInfoClassMember('destinationname', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                destination file name
                ''',
                'destinationname',
                'Cisco-IOS-XR-shellutil-copy-act', False, is_mandatory=True),
            _MetaInfoClassMember('sourcefilesystem', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                source file system e.g disk0: tftp
                ''',
                'sourcefilesystem',
                'Cisco-IOS-XR-shellutil-copy-act', False, is_mandatory=True),
            _MetaInfoClassMember('destinationfilesystem', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                destination file system e.g disk0:, tftp:
                ''',
                'destinationfilesystem',
                'Cisco-IOS-XR-shellutil-copy-act', False, is_mandatory=True),
            _MetaInfoClassMember('sourcelocation', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                source location
                ''',
                'sourcelocation',
                'Cisco-IOS-XR-shellutil-copy-act', False),
            _MetaInfoClassMember('destinationlocation', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                destination location
                ''',
                'destinationlocation',
                'Cisco-IOS-XR-shellutil-copy-act', False),
            _MetaInfoClassMember('vrf', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                vrf name
                ''',
                'vrf',
                'Cisco-IOS-XR-shellutil-copy-act', False),
            _MetaInfoClassMember('recurse', ATTRIBUTE, 'bool', 'boolean',
                None, None,
                [], [],
                '''                recurse files to copy
                ''',
                'recurse',
                'Cisco-IOS-XR-shellutil-copy-act', False),
            ],
            'Cisco-IOS-XR-shellutil-copy-act',
            'input',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-shellutil-copy-act'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_shellutil_copy_act',
        ),
    },
    'Copy.Output' : {
        'meta_info' : _MetaInfoClass('Copy.Output', REFERENCE_CLASS,
            ''' ''',
            False, 
            [
            _MetaInfoClassMember('response', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                Status of copy operation
                ''',
                'response',
                'Cisco-IOS-XR-shellutil-copy-act', False),
            ],
            'Cisco-IOS-XR-shellutil-copy-act',
            'output',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-shellutil-copy-act'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_shellutil_copy_act',
        ),
    },
    'Copy' : {
        'meta_info' : _MetaInfoClass('Copy', REFERENCE_CLASS,
            ''' ''',
            False, 
            [
            _MetaInfoClassMember('input', REFERENCE_CLASS, 'Input', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_shellutil_copy_act', 'Copy.Input',
                [], [],
                '''                ''',
                'input',
                'Cisco-IOS-XR-shellutil-copy-act', False),
            _MetaInfoClassMember('output', REFERENCE_CLASS, 'Output', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_shellutil_copy_act', 'Copy.Output',
                [], [],
                '''                ''',
                'output',
                'Cisco-IOS-XR-shellutil-copy-act', False),
            ],
            'Cisco-IOS-XR-shellutil-copy-act',
            'copy',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-shellutil-copy-act'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_shellutil_copy_act',
        ),
    },
}
_meta_table['Copy.Input']['meta_info'].parent =_meta_table['Copy']['meta_info']
_meta_table['Copy.Output']['meta_info'].parent =_meta_table['Copy']['meta_info']
