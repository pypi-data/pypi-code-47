
'''
This is auto-generated file,
which includes metadata for module Cisco_IOS_XR_ip_raw_cfg
'''

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_LIST, REFERENCE_LEAFLIST, REFERENCE_BITS, REFERENCE_UNION
from ydk._core._dm_meta_info import REFERENCE_CLASS, REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, ANYXML_CLASS
from ydk._core._importer import _yang_ns

_meta_table = {
    'IpRaw.NumThread' : {
        'meta_info' : _MetaInfoClass('IpRaw.NumThread', REFERENCE_CLASS,
            '''RAW InQueue and OutQueue threads''',
            False, 
            [
            _MetaInfoClassMember('raw-in-q-threads', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('1', '16')], [],
                '''                InQ Threads
                ''',
                'raw_in_q_threads',
                'Cisco-IOS-XR-ip-raw-cfg', False, is_mandatory=True),
            _MetaInfoClassMember('raw-out-q-threads', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('1', '16')], [],
                '''                OutQ Threads
                ''',
                'raw_out_q_threads',
                'Cisco-IOS-XR-ip-raw-cfg', False, is_mandatory=True),
            ],
            'Cisco-IOS-XR-ip-raw-cfg',
            'num-thread',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-ip-raw-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_raw_cfg',
            is_presence=True,
        ),
    },
    'IpRaw.Directory' : {
        'meta_info' : _MetaInfoClass('IpRaw.Directory', REFERENCE_CLASS,
            '''RAW directory details''',
            False, 
            [
            _MetaInfoClassMember('directoryname', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                Directory name
                ''',
                'directoryname',
                'Cisco-IOS-XR-ip-raw-cfg', False, is_mandatory=True),
            _MetaInfoClassMember('max-raw-debug-files', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('1', '18000')], [],
                '''                Set number of Debug files
                ''',
                'max_raw_debug_files',
                'Cisco-IOS-XR-ip-raw-cfg', False, default_value="256"),
            _MetaInfoClassMember('max-file-size-files', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('1024', '4294967295')], [],
                '''                Set size of debug files in bytes
                ''',
                'max_file_size_files',
                'Cisco-IOS-XR-ip-raw-cfg', False),
            ],
            'Cisco-IOS-XR-ip-raw-cfg',
            'directory',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-ip-raw-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_raw_cfg',
            is_presence=True,
        ),
    },
    'IpRaw' : {
        'meta_info' : _MetaInfoClass('IpRaw', REFERENCE_CLASS,
            '''Global IP RAW configuration''',
            False, 
            [
            _MetaInfoClassMember('num-thread', REFERENCE_CLASS, 'NumThread', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_raw_cfg', 'IpRaw.NumThread',
                [], [],
                '''                RAW InQueue and OutQueue threads
                ''',
                'num_thread',
                'Cisco-IOS-XR-ip-raw-cfg', False, is_presence=True),
            _MetaInfoClassMember('directory', REFERENCE_CLASS, 'Directory', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_raw_cfg', 'IpRaw.Directory',
                [], [],
                '''                RAW directory details
                ''',
                'directory',
                'Cisco-IOS-XR-ip-raw-cfg', False, is_presence=True),
            _MetaInfoClassMember('receive-q', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('40', '800')], [],
                '''                RAW receive Queue Size
                ''',
                'receive_q',
                'Cisco-IOS-XR-ip-raw-cfg', False),
            ],
            'Cisco-IOS-XR-ip-raw-cfg',
            'ip-raw',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-ip-raw-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_raw_cfg',
        ),
    },
}
_meta_table['IpRaw.NumThread']['meta_info'].parent =_meta_table['IpRaw']['meta_info']
_meta_table['IpRaw.Directory']['meta_info'].parent =_meta_table['IpRaw']['meta_info']
