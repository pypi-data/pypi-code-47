
'''
This is auto-generated file,
which includes metadata for module Cisco_IOS_XR_ipv4_filesystems_cfg
'''

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_LIST, REFERENCE_LEAFLIST, REFERENCE_BITS, REFERENCE_UNION
from ydk._core._dm_meta_info import REFERENCE_CLASS, REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, ANYXML_CLASS
from ydk._core._importer import _yang_ns

_meta_table = {
    'Rcp.RcpClient' : {
        'meta_info' : _MetaInfoClass('Rcp.RcpClient', REFERENCE_CLASS,
            '''RCP client configuration''',
            False, 
            [
            _MetaInfoClassMember('username', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                Specify username for connections
                ''',
                'username',
                'Cisco-IOS-XR-ipv4-filesystems-cfg', False),
            _MetaInfoClassMember('source-interface', ATTRIBUTE, 'str', 'xr:Interface-name',
                None, None,
                [], [b'[a-zA-Z0-9._/-]+'],
                '''                Specify interface for source address in
                connections
                ''',
                'source_interface',
                'Cisco-IOS-XR-ipv4-filesystems-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-filesystems-cfg',
            'rcp-client',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-ipv4-filesystems-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_filesystems_cfg',
        ),
    },
    'Rcp' : {
        'meta_info' : _MetaInfoClass('Rcp', REFERENCE_CLASS,
            '''RCP configuration''',
            False, 
            [
            _MetaInfoClassMember('rcp-client', REFERENCE_CLASS, 'RcpClient', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_filesystems_cfg', 'Rcp.RcpClient',
                [], [],
                '''                RCP client configuration
                ''',
                'rcp_client',
                'Cisco-IOS-XR-ipv4-filesystems-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-filesystems-cfg',
            'rcp',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-ipv4-filesystems-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_filesystems_cfg',
        ),
    },
    'Ftp.FtpClient.Vrfs.Vrf' : {
        'meta_info' : _MetaInfoClass('Ftp.FtpClient.Vrfs.Vrf', REFERENCE_LIST,
            '''VRF specific data''',
            False, 
            [
            _MetaInfoClassMember('vrf-name', ATTRIBUTE, 'str', 'xr:Cisco-ios-xr-string',
                None, None,
                [], [b'[\\w\\-\\.:,_@#%$\\+=\\|;]+'],
                '''                Name of the VRF instance
                ''',
                'vrf_name',
                'Cisco-IOS-XR-ipv4-filesystems-cfg', True),
            _MetaInfoClassMember('source-interface', ATTRIBUTE, 'str', 'xr:Interface-name',
                None, None,
                [], [b'[a-zA-Z0-9._/-]+'],
                '''                Specify interface for source address in
                connections
                ''',
                'source_interface',
                'Cisco-IOS-XR-ipv4-filesystems-cfg', False),
            _MetaInfoClassMember('username', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                Specify username for connections
                ''',
                'username',
                'Cisco-IOS-XR-ipv4-filesystems-cfg', False),
            _MetaInfoClassMember('anonymous-password', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                Password for anonymous user (ftp server
                dependent)
                ''',
                'anonymous_password',
                'Cisco-IOS-XR-ipv4-filesystems-cfg', False),
            _MetaInfoClassMember('password', ATTRIBUTE, 'str', 'xr:Proprietary-password',
                None, None,
                [], [b'(!.+)|([^!].+)'],
                '''                Specify password for ftp connnection
                ''',
                'password',
                'Cisco-IOS-XR-ipv4-filesystems-cfg', False),
            _MetaInfoClassMember('passive', ATTRIBUTE, 'Empty', 'empty',
                None, None,
                [], [],
                '''                Enable connect using passive mode
                ''',
                'passive',
                'Cisco-IOS-XR-ipv4-filesystems-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-filesystems-cfg',
            'vrf',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-ipv4-filesystems-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_filesystems_cfg',
        ),
    },
    'Ftp.FtpClient.Vrfs' : {
        'meta_info' : _MetaInfoClass('Ftp.FtpClient.Vrfs', REFERENCE_CLASS,
            '''VRF table''',
            False, 
            [
            _MetaInfoClassMember('vrf', REFERENCE_LIST, 'Vrf', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_filesystems_cfg', 'Ftp.FtpClient.Vrfs.Vrf',
                [], [],
                '''                VRF specific data
                ''',
                'vrf',
                'Cisco-IOS-XR-ipv4-filesystems-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-filesystems-cfg',
            'vrfs',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-ipv4-filesystems-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_filesystems_cfg',
        ),
    },
    'Ftp.FtpClient' : {
        'meta_info' : _MetaInfoClass('Ftp.FtpClient', REFERENCE_CLASS,
            '''FTP client configuration''',
            False, 
            [
            _MetaInfoClassMember('vrfs', REFERENCE_CLASS, 'Vrfs', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_filesystems_cfg', 'Ftp.FtpClient.Vrfs',
                [], [],
                '''                VRF table
                ''',
                'vrfs',
                'Cisco-IOS-XR-ipv4-filesystems-cfg', False),
            _MetaInfoClassMember('passive', ATTRIBUTE, 'Empty', 'empty',
                None, None,
                [], [],
                '''                Enable connect using passive mode
                ''',
                'passive',
                'Cisco-IOS-XR-ipv4-filesystems-cfg', False),
            _MetaInfoClassMember('password', ATTRIBUTE, 'str', 'xr:Proprietary-password',
                None, None,
                [], [b'(!.+)|([^!].+)'],
                '''                Specify password for ftp connnection
                ''',
                'password',
                'Cisco-IOS-XR-ipv4-filesystems-cfg', False),
            _MetaInfoClassMember('anonymous-password', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                Password for anonymous user (ftp server
                dependent)
                ''',
                'anonymous_password',
                'Cisco-IOS-XR-ipv4-filesystems-cfg', False),
            _MetaInfoClassMember('username', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                Specify username for connections
                ''',
                'username',
                'Cisco-IOS-XR-ipv4-filesystems-cfg', False),
            _MetaInfoClassMember('source-interface', ATTRIBUTE, 'str', 'xr:Interface-name',
                None, None,
                [], [b'[a-zA-Z0-9._/-]+'],
                '''                Specify interface for source address in
                connections
                ''',
                'source_interface',
                'Cisco-IOS-XR-ipv4-filesystems-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-filesystems-cfg',
            'ftp-client',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-ipv4-filesystems-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_filesystems_cfg',
        ),
    },
    'Ftp' : {
        'meta_info' : _MetaInfoClass('Ftp', REFERENCE_CLASS,
            '''ftp''',
            False, 
            [
            _MetaInfoClassMember('ftp-client', REFERENCE_CLASS, 'FtpClient', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_filesystems_cfg', 'Ftp.FtpClient',
                [], [],
                '''                FTP client configuration
                ''',
                'ftp_client',
                'Cisco-IOS-XR-ipv4-filesystems-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-filesystems-cfg',
            'ftp',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-ipv4-filesystems-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_filesystems_cfg',
        ),
    },
    'Tftp.TftpClient.Vrfs.Vrf' : {
        'meta_info' : _MetaInfoClass('Tftp.TftpClient.Vrfs.Vrf', REFERENCE_LIST,
            '''VRF specific data''',
            False, 
            [
            _MetaInfoClassMember('vrf-name', ATTRIBUTE, 'str', 'xr:Cisco-ios-xr-string',
                None, None,
                [], [b'[\\w\\-\\.:,_@#%$\\+=\\|;]+'],
                '''                Name of the VRF instance
                ''',
                'vrf_name',
                'Cisco-IOS-XR-ipv4-filesystems-cfg', True),
            _MetaInfoClassMember('source-interface', ATTRIBUTE, 'str', 'xr:Interface-name',
                None, None,
                [], [b'[a-zA-Z0-9._/-]+'],
                '''                Specify interface for source address in
                connections
                ''',
                'source_interface',
                'Cisco-IOS-XR-ipv4-filesystems-cfg', False),
            _MetaInfoClassMember('retry', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('0', '256')], [],
                '''                Specify the number of retries when client
                requests TFTP connections
                ''',
                'retry',
                'Cisco-IOS-XR-ipv4-filesystems-cfg', False),
            _MetaInfoClassMember('timeout', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('0', '256')], [],
                '''                Specify the timeout for every TFTP connection
                in seconds
                ''',
                'timeout',
                'Cisco-IOS-XR-ipv4-filesystems-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-filesystems-cfg',
            'vrf',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-ipv4-filesystems-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_filesystems_cfg',
        ),
    },
    'Tftp.TftpClient.Vrfs' : {
        'meta_info' : _MetaInfoClass('Tftp.TftpClient.Vrfs', REFERENCE_CLASS,
            '''VRF table''',
            False, 
            [
            _MetaInfoClassMember('vrf', REFERENCE_LIST, 'Vrf', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_filesystems_cfg', 'Tftp.TftpClient.Vrfs.Vrf',
                [], [],
                '''                VRF specific data
                ''',
                'vrf',
                'Cisco-IOS-XR-ipv4-filesystems-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-filesystems-cfg',
            'vrfs',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-ipv4-filesystems-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_filesystems_cfg',
        ),
    },
    'Tftp.TftpClient' : {
        'meta_info' : _MetaInfoClass('Tftp.TftpClient', REFERENCE_CLASS,
            '''TFTP client configuration''',
            False, 
            [
            _MetaInfoClassMember('vrfs', REFERENCE_CLASS, 'Vrfs', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_filesystems_cfg', 'Tftp.TftpClient.Vrfs',
                [], [],
                '''                VRF table
                ''',
                'vrfs',
                'Cisco-IOS-XR-ipv4-filesystems-cfg', False),
            _MetaInfoClassMember('retry', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('0', '256')], [],
                '''                Specify the number of retries when client
                requests TFTP connections
                ''',
                'retry',
                'Cisco-IOS-XR-ipv4-filesystems-cfg', False),
            _MetaInfoClassMember('timeout', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('0', '256')], [],
                '''                Specify the timeout for every TFTP connection
                in seconds
                ''',
                'timeout',
                'Cisco-IOS-XR-ipv4-filesystems-cfg', False),
            _MetaInfoClassMember('source-interface', ATTRIBUTE, 'str', 'xr:Interface-name',
                None, None,
                [], [b'[a-zA-Z0-9._/-]+'],
                '''                Specify interface for source address in
                connections
                ''',
                'source_interface',
                'Cisco-IOS-XR-ipv4-filesystems-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-filesystems-cfg',
            'tftp-client',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-ipv4-filesystems-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_filesystems_cfg',
        ),
    },
    'Tftp' : {
        'meta_info' : _MetaInfoClass('Tftp', REFERENCE_CLASS,
            '''tftp''',
            False, 
            [
            _MetaInfoClassMember('tftp-client', REFERENCE_CLASS, 'TftpClient', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_filesystems_cfg', 'Tftp.TftpClient',
                [], [],
                '''                TFTP client configuration
                ''',
                'tftp_client',
                'Cisco-IOS-XR-ipv4-filesystems-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-filesystems-cfg',
            'tftp',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-ipv4-filesystems-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_filesystems_cfg',
        ),
    },
}
_meta_table['Rcp.RcpClient']['meta_info'].parent =_meta_table['Rcp']['meta_info']
_meta_table['Ftp.FtpClient.Vrfs.Vrf']['meta_info'].parent =_meta_table['Ftp.FtpClient.Vrfs']['meta_info']
_meta_table['Ftp.FtpClient.Vrfs']['meta_info'].parent =_meta_table['Ftp.FtpClient']['meta_info']
_meta_table['Ftp.FtpClient']['meta_info'].parent =_meta_table['Ftp']['meta_info']
_meta_table['Tftp.TftpClient.Vrfs.Vrf']['meta_info'].parent =_meta_table['Tftp.TftpClient.Vrfs']['meta_info']
_meta_table['Tftp.TftpClient.Vrfs']['meta_info'].parent =_meta_table['Tftp.TftpClient']['meta_info']
_meta_table['Tftp.TftpClient']['meta_info'].parent =_meta_table['Tftp']['meta_info']
