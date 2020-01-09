
'''
This is auto-generated file,
which includes metadata for module Cisco_IOS_XR_sysadmin_debug_trace
'''

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_LIST, REFERENCE_LEAFLIST, REFERENCE_BITS, REFERENCE_UNION
from ydk._core._dm_meta_info import REFERENCE_CLASS, REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, ANYXML_CLASS
from ydk._core._importer import _yang_ns

_meta_table = {
    'Config.Debug.Trace' : {
        'meta_info' : _MetaInfoClass('Config.Debug.Trace', REFERENCE_LIST,
            ''' ''',
            False, 
            [
            _MetaInfoClassMember('connection_type', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                ''',
                'connection_type',
                'Cisco-IOS-XR-sysadmin-debug-trace', True),
            _MetaInfoClassMember('enable', ATTRIBUTE, 'Empty', 'empty',
                None, None,
                [], [],
                '''                ''',
                'enable',
                'Cisco-IOS-XR-sysadmin-debug-trace', False),
            _MetaInfoClassMember('disable', ATTRIBUTE, 'Empty', 'empty',
                None, None,
                [], [],
                '''                ''',
                'disable',
                'Cisco-IOS-XR-sysadmin-debug-trace', False),
            ],
            'Cisco-IOS-XR-sysadmin-debug-trace',
            'trace',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-sysadmin-debug-trace'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_debug_trace',
        ),
    },
    'Config.Debug' : {
        'meta_info' : _MetaInfoClass('Config.Debug', REFERENCE_CLASS,
            ''' ''',
            False, 
            [
            _MetaInfoClassMember('trace', REFERENCE_LIST, 'Trace', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_debug_trace', 'Config.Debug.Trace',
                [], [],
                '''                ''',
                'trace',
                'Cisco-IOS-XR-sysadmin-debug-trace', False, max_elements=16),
            ],
            'Cisco-IOS-XR-sysadmin-debug-trace',
            'debug',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-sysadmin-debug-trace'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_debug_trace',
        ),
    },
    'Config' : {
        'meta_info' : _MetaInfoClass('Config', REFERENCE_CLASS,
            ''' ''',
            False, 
            [
            _MetaInfoClassMember('debug', REFERENCE_CLASS, 'Debug', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_debug_trace', 'Config.Debug',
                [], [],
                '''                ''',
                'debug',
                'Cisco-IOS-XR-sysadmin-debug-trace', False),
            ],
            'Cisco-IOS-XR-sysadmin-debug-trace',
            'config',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-sysadmin-debug-trace'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_debug_trace',
        ),
    },
}
_meta_table['Config.Debug.Trace']['meta_info'].parent =_meta_table['Config.Debug']['meta_info']
_meta_table['Config.Debug']['meta_info'].parent =_meta_table['Config']['meta_info']
