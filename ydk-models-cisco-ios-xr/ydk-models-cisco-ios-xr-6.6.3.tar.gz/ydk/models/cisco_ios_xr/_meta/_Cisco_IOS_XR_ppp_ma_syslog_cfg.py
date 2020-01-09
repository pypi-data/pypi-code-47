
'''
This is auto-generated file,
which includes metadata for module Cisco_IOS_XR_ppp_ma_syslog_cfg
'''

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_LIST, REFERENCE_LEAFLIST, REFERENCE_BITS, REFERENCE_UNION
from ydk._core._dm_meta_info import REFERENCE_CLASS, REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, ANYXML_CLASS
from ydk._core._importer import _yang_ns

_meta_table = {
    'Ppp.Syslog' : {
        'meta_info' : _MetaInfoClass('Ppp.Syslog', REFERENCE_CLASS,
            '''syslog option for session status''',
            False, 
            [
            _MetaInfoClassMember('enable-session-status', ATTRIBUTE, 'Empty', 'empty',
                None, None,
                [], [],
                '''                Enable syslog for ppp session status
                ''',
                'enable_session_status',
                'Cisco-IOS-XR-ppp-ma-syslog-cfg', False),
            ],
            'Cisco-IOS-XR-ppp-ma-syslog-cfg',
            'syslog',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-ppp-ma-syslog-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ppp_ma_syslog_cfg',
        ),
    },
    'Ppp' : {
        'meta_info' : _MetaInfoClass('Ppp', REFERENCE_CLASS,
            '''PPP configuration''',
            False, 
            [
            _MetaInfoClassMember('syslog', REFERENCE_CLASS, 'Syslog', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ppp_ma_syslog_cfg', 'Ppp.Syslog',
                [], [],
                '''                syslog option for session status
                ''',
                'syslog',
                'Cisco-IOS-XR-ppp-ma-syslog-cfg', False),
            ],
            'Cisco-IOS-XR-ppp-ma-syslog-cfg',
            'ppp',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-ppp-ma-syslog-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ppp_ma_syslog_cfg',
        ),
    },
}
_meta_table['Ppp.Syslog']['meta_info'].parent =_meta_table['Ppp']['meta_info']
