
'''
This is auto-generated file,
which includes metadata for module Cisco_IOS_XR_syslog_act
'''

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_LIST, REFERENCE_LEAFLIST, REFERENCE_BITS, REFERENCE_UNION
from ydk._core._dm_meta_info import REFERENCE_CLASS, REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, ANYXML_CLASS
from ydk._core._importer import _yang_ns

_meta_table = {
    'Logmsg.Input' : {
        'meta_info' : _MetaInfoClass('Logmsg.Input', REFERENCE_CLASS,
            ''' ''',
            False, 
            [
            _MetaInfoClassMember('severity', REFERENCE_ENUM_CLASS, 'Severity', 'log:severity',
                'ydk.models.ietf.ietf_syslog_types', 'Severity',
                [], [],
                '''                Set serverity level
                ''',
                'severity',
                'Cisco-IOS-XR-syslog-act', False, is_mandatory=True),
            _MetaInfoClassMember('message', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                Message body.
                ''',
                'message',
                'Cisco-IOS-XR-syslog-act', False, is_mandatory=True),
            ],
            'Cisco-IOS-XR-syslog-act',
            'input',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-syslog-act'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_syslog_act',
        ),
    },
    'Logmsg' : {
        'meta_info' : _MetaInfoClass('Logmsg', REFERENCE_CLASS,
            ''' ''',
            False, 
            [
            _MetaInfoClassMember('input', REFERENCE_CLASS, 'Input', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_syslog_act', 'Logmsg.Input',
                [], [],
                '''                ''',
                'input',
                'Cisco-IOS-XR-syslog-act', False),
            ],
            'Cisco-IOS-XR-syslog-act',
            'logmsg',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-syslog-act'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_syslog_act',
        ),
    },
}
_meta_table['Logmsg.Input']['meta_info'].parent =_meta_table['Logmsg']['meta_info']
