
'''
This is auto-generated file,
which includes metadata for module Cisco_IOS_XR_shellutil_oper
'''

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_LIST, REFERENCE_LEAFLIST, REFERENCE_BITS, REFERENCE_UNION
from ydk._core._dm_meta_info import REFERENCE_CLASS, REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, ANYXML_CLASS
from ydk._core._importer import _yang_ns

_meta_table = {
    'TimeSource' : _MetaInfoEnum('TimeSource',
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_shellutil_oper', 'TimeSource',
        '''Time source''',
        {
            'error':'error',
            'none':'none',
            'ntp':'ntp',
            'manual':'manual',
            'calendar':'calendar',
        }, 'Cisco-IOS-XR-shellutil-oper', _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-shellutil-oper']),
    'SystemTime.Clock' : {
        'meta_info' : _MetaInfoClass('SystemTime.Clock', REFERENCE_CLASS,
            '''System clock information''',
            False, 
            [
            _MetaInfoClassMember('year', ATTRIBUTE, 'int', 'uint16',
                None, None,
                [('0', '65535')], [],
                '''                Year [0..65535]
                ''',
                'year',
                'Cisco-IOS-XR-shellutil-oper', False, is_config=False),
            _MetaInfoClassMember('month', ATTRIBUTE, 'int', 'uint8',
                None, None,
                [('0', '255')], [],
                '''                Month [1..12]
                ''',
                'month',
                'Cisco-IOS-XR-shellutil-oper', False, is_config=False),
            _MetaInfoClassMember('day', ATTRIBUTE, 'int', 'uint8',
                None, None,
                [('0', '255')], [],
                '''                Day [1..31]
                ''',
                'day',
                'Cisco-IOS-XR-shellutil-oper', False, is_config=False),
            _MetaInfoClassMember('hour', ATTRIBUTE, 'int', 'uint8',
                None, None,
                [('0', '255')], [],
                '''                Hour [0..23]
                ''',
                'hour',
                'Cisco-IOS-XR-shellutil-oper', False, is_config=False),
            _MetaInfoClassMember('minute', ATTRIBUTE, 'int', 'uint8',
                None, None,
                [('0', '255')], [],
                '''                Minute [0..59]
                ''',
                'minute',
                'Cisco-IOS-XR-shellutil-oper', False, is_config=False),
            _MetaInfoClassMember('second', ATTRIBUTE, 'int', 'uint8',
                None, None,
                [('0', '255')], [],
                '''                Second [0..60], use 60 for leap-second
                ''',
                'second',
                'Cisco-IOS-XR-shellutil-oper', False, is_config=False),
            _MetaInfoClassMember('millisecond', ATTRIBUTE, 'int', 'uint16',
                None, None,
                [('0', '65535')], [],
                '''                Millisecond [0..999]
                ''',
                'millisecond',
                'Cisco-IOS-XR-shellutil-oper', False, is_config=False),
            _MetaInfoClassMember('wday', ATTRIBUTE, 'int', 'uint16',
                None, None,
                [('0', '65535')], [],
                '''                Week Day [0..6]
                ''',
                'wday',
                'Cisco-IOS-XR-shellutil-oper', False, is_config=False),
            _MetaInfoClassMember('time-zone', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                Time zone
                ''',
                'time_zone',
                'Cisco-IOS-XR-shellutil-oper', False, is_config=False),
            _MetaInfoClassMember('time-source', REFERENCE_ENUM_CLASS, 'TimeSource', 'Time-source',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_shellutil_oper', 'TimeSource',
                [], [],
                '''                Time source
                ''',
                'time_source',
                'Cisco-IOS-XR-shellutil-oper', False, is_config=False),
            ],
            'Cisco-IOS-XR-shellutil-oper',
            'clock',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-shellutil-oper'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_shellutil_oper',
            is_config=False,
        ),
    },
    'SystemTime.Uptime' : {
        'meta_info' : _MetaInfoClass('SystemTime.Uptime', REFERENCE_CLASS,
            '''System uptime information''',
            False, 
            [
            _MetaInfoClassMember('host-name', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                Host name
                ''',
                'host_name',
                'Cisco-IOS-XR-shellutil-oper', False, is_config=False),
            _MetaInfoClassMember('uptime', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('0', '4294967295')], [],
                '''                Amount of time in seconds since this system
                was last initialized
                ''',
                'uptime',
                'Cisco-IOS-XR-shellutil-oper', False, is_config=False),
            ],
            'Cisco-IOS-XR-shellutil-oper',
            'uptime',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-shellutil-oper'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_shellutil_oper',
            is_config=False,
        ),
    },
    'SystemTime' : {
        'meta_info' : _MetaInfoClass('SystemTime', REFERENCE_CLASS,
            '''System time information''',
            False, 
            [
            _MetaInfoClassMember('clock', REFERENCE_CLASS, 'Clock', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_shellutil_oper', 'SystemTime.Clock',
                [], [],
                '''                System clock information
                ''',
                'clock',
                'Cisco-IOS-XR-shellutil-oper', False, is_config=False),
            _MetaInfoClassMember('uptime', REFERENCE_CLASS, 'Uptime', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_shellutil_oper', 'SystemTime.Uptime',
                [], [],
                '''                System uptime information
                ''',
                'uptime',
                'Cisco-IOS-XR-shellutil-oper', False, is_config=False),
            ],
            'Cisco-IOS-XR-shellutil-oper',
            'system-time',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-shellutil-oper'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_shellutil_oper',
            is_config=False,
        ),
    },
}
_meta_table['SystemTime.Clock']['meta_info'].parent =_meta_table['SystemTime']['meta_info']
_meta_table['SystemTime.Uptime']['meta_info'].parent =_meta_table['SystemTime']['meta_info']
