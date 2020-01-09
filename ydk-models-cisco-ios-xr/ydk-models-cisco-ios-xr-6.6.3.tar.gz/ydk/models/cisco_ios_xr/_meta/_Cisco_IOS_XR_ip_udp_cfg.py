
'''
This is auto-generated file,
which includes metadata for module Cisco_IOS_XR_ip_udp_cfg
'''

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_LIST, REFERENCE_LEAFLIST, REFERENCE_BITS, REFERENCE_UNION
from ydk._core._dm_meta_info import REFERENCE_CLASS, REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, ANYXML_CLASS
from ydk._core._importer import _yang_ns

_meta_table = {
    'IpUdp.NumThread' : {
        'meta_info' : _MetaInfoClass('IpUdp.NumThread', REFERENCE_CLASS,
            '''UDP InQueue and OutQueue threads''',
            False, 
            [
            _MetaInfoClassMember('udp-in-q-threads', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('1', '16')], [],
                '''                InQ Threads
                ''',
                'udp_in_q_threads',
                'Cisco-IOS-XR-ip-udp-cfg', False, is_mandatory=True),
            _MetaInfoClassMember('udp-out-q-threads', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('1', '16')], [],
                '''                OutQ Threads
                ''',
                'udp_out_q_threads',
                'Cisco-IOS-XR-ip-udp-cfg', False, is_mandatory=True),
            ],
            'Cisco-IOS-XR-ip-udp-cfg',
            'num-thread',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-ip-udp-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_udp_cfg',
            is_presence=True,
        ),
    },
    'IpUdp.Directory' : {
        'meta_info' : _MetaInfoClass('IpUdp.Directory', REFERENCE_CLASS,
            '''UDP directory details''',
            False, 
            [
            _MetaInfoClassMember('directoryname', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                Directory name
                ''',
                'directoryname',
                'Cisco-IOS-XR-ip-udp-cfg', False, is_mandatory=True),
            _MetaInfoClassMember('max-udp-debug-files', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('1', '5000')], [],
                '''                Set number of Debug files
                ''',
                'max_udp_debug_files',
                'Cisco-IOS-XR-ip-udp-cfg', False, default_value="256"),
            _MetaInfoClassMember('max-file-size-files', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('1024', '4294967295')], [],
                '''                Set size of debug files in bytes
                ''',
                'max_file_size_files',
                'Cisco-IOS-XR-ip-udp-cfg', False),
            ],
            'Cisco-IOS-XR-ip-udp-cfg',
            'directory',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-ip-udp-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_udp_cfg',
            is_presence=True,
        ),
    },
    'IpUdp' : {
        'meta_info' : _MetaInfoClass('IpUdp', REFERENCE_CLASS,
            '''Global IP UDP configuration''',
            False, 
            [
            _MetaInfoClassMember('num-thread', REFERENCE_CLASS, 'NumThread', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_udp_cfg', 'IpUdp.NumThread',
                [], [],
                '''                UDP InQueue and OutQueue threads
                ''',
                'num_thread',
                'Cisco-IOS-XR-ip-udp-cfg', False, is_presence=True),
            _MetaInfoClassMember('directory', REFERENCE_CLASS, 'Directory', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_udp_cfg', 'IpUdp.Directory',
                [], [],
                '''                UDP directory details
                ''',
                'directory',
                'Cisco-IOS-XR-ip-udp-cfg', False, is_presence=True),
            _MetaInfoClassMember('receive-q', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('40', '800')], [],
                '''                UDP receive Queue Size
                ''',
                'receive_q',
                'Cisco-IOS-XR-ip-udp-cfg', False),
            ],
            'Cisco-IOS-XR-ip-udp-cfg',
            'ip-udp',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-ip-udp-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_udp_cfg',
        ),
    },
}
_meta_table['IpUdp.NumThread']['meta_info'].parent =_meta_table['IpUdp']['meta_info']
_meta_table['IpUdp.Directory']['meta_info'].parent =_meta_table['IpUdp']['meta_info']
