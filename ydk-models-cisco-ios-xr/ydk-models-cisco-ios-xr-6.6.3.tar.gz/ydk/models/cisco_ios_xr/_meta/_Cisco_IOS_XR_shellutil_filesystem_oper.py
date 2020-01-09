
'''
This is auto-generated file,
which includes metadata for module Cisco_IOS_XR_shellutil_filesystem_oper
'''

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_LIST, REFERENCE_LEAFLIST, REFERENCE_BITS, REFERENCE_UNION
from ydk._core._dm_meta_info import REFERENCE_CLASS, REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, ANYXML_CLASS
from ydk._core._importer import _yang_ns

_meta_table = {
    'FileSystem.Node.FileSystem_' : {
        'meta_info' : _MetaInfoClass('FileSystem.Node.FileSystem_', REFERENCE_LIST,
            '''Available file systems''',
            False, 
            [
            _MetaInfoClassMember('size', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                Size of the file system in bytes
                ''',
                'size',
                'Cisco-IOS-XR-shellutil-filesystem-oper', False, is_config=False),
            _MetaInfoClassMember('free', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                Free space in the file system in bytes
                ''',
                'free',
                'Cisco-IOS-XR-shellutil-filesystem-oper', False, is_config=False),
            _MetaInfoClassMember('type', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                Type of file system
                ''',
                'type',
                'Cisco-IOS-XR-shellutil-filesystem-oper', False, is_config=False),
            _MetaInfoClassMember('flags', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                Flags of file system
                ''',
                'flags',
                'Cisco-IOS-XR-shellutil-filesystem-oper', False, is_config=False),
            _MetaInfoClassMember('prefixes', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                Prefixes of file system
                ''',
                'prefixes',
                'Cisco-IOS-XR-shellutil-filesystem-oper', False, is_config=False),
            ],
            'Cisco-IOS-XR-shellutil-filesystem-oper',
            'file-system',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-shellutil-filesystem-oper'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_shellutil_filesystem_oper',
            is_config=False,
        ),
    },
    'FileSystem.Node' : {
        'meta_info' : _MetaInfoClass('FileSystem.Node', REFERENCE_LIST,
            '''Node ID''',
            False, 
            [
            _MetaInfoClassMember('node-name', ATTRIBUTE, 'str', 'xr:Node-id',
                None, None,
                [], [b'([a-zA-Z0-9_]*\\d+/){1,2}([a-zA-Z0-9_]*\\d+)'],
                '''                Node name
                ''',
                'node_name',
                'Cisco-IOS-XR-shellutil-filesystem-oper', True, is_config=False),
            _MetaInfoClassMember('file-system', REFERENCE_LIST, 'FileSystem_', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_shellutil_filesystem_oper', 'FileSystem.Node.FileSystem_',
                [], [],
                '''                Available file systems
                ''',
                'file_system',
                'Cisco-IOS-XR-shellutil-filesystem-oper', False, is_config=False),
            ],
            'Cisco-IOS-XR-shellutil-filesystem-oper',
            'node',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-shellutil-filesystem-oper'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_shellutil_filesystem_oper',
            is_config=False,
        ),
    },
    'FileSystem' : {
        'meta_info' : _MetaInfoClass('FileSystem', REFERENCE_CLASS,
            '''List of filesystems''',
            False, 
            [
            _MetaInfoClassMember('node', REFERENCE_LIST, 'Node', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_shellutil_filesystem_oper', 'FileSystem.Node',
                [], [],
                '''                Node ID
                ''',
                'node',
                'Cisco-IOS-XR-shellutil-filesystem-oper', False, is_config=False),
            ],
            'Cisco-IOS-XR-shellutil-filesystem-oper',
            'file-system',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-shellutil-filesystem-oper'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_shellutil_filesystem_oper',
            is_config=False,
        ),
    },
}
_meta_table['FileSystem.Node.FileSystem_']['meta_info'].parent =_meta_table['FileSystem.Node']['meta_info']
_meta_table['FileSystem.Node']['meta_info'].parent =_meta_table['FileSystem']['meta_info']
