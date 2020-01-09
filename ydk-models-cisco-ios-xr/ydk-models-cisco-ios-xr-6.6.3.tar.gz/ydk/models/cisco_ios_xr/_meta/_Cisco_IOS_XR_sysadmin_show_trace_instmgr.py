
'''
This is auto-generated file,
which includes metadata for module Cisco_IOS_XR_sysadmin_show_trace_instmgr
'''

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_LIST, REFERENCE_LEAFLIST, REFERENCE_BITS, REFERENCE_UNION
from ydk._core._dm_meta_info import REFERENCE_CLASS, REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, ANYXML_CLASS
from ydk._core._importer import _yang_ns

_meta_table = {
    'Instmgr.Trace.Location.AllOptions.TraceBlocks' : {
        'meta_info' : _MetaInfoClass('Instmgr.Trace.Location.AllOptions.TraceBlocks', REFERENCE_LIST,
            ''' ''',
            False, 
            [
            _MetaInfoClassMember('data', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                Trace output block
                ''',
                'data',
                'Cisco-IOS-XR-sysadmin-show-trace-instmgr', False, is_config=False),
            ],
            'Cisco-IOS-XR-sysadmin-show-trace-instmgr',
            'trace-blocks',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-sysadmin-show-trace-instmgr'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_show_trace_instmgr',
            is_config=False,
        ),
    },
    'Instmgr.Trace.Location.AllOptions' : {
        'meta_info' : _MetaInfoClass('Instmgr.Trace.Location.AllOptions', REFERENCE_LIST,
            ''' ''',
            False, 
            [
            _MetaInfoClassMember('option', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                ''',
                'option',
                'Cisco-IOS-XR-sysadmin-show-trace-instmgr', True, is_config=False),
            _MetaInfoClassMember('trace-blocks', REFERENCE_LIST, 'TraceBlocks', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_show_trace_instmgr', 'Instmgr.Trace.Location.AllOptions.TraceBlocks',
                [], [],
                '''                ''',
                'trace_blocks',
                'Cisco-IOS-XR-sysadmin-show-trace-instmgr', False, is_config=False),
            ],
            'Cisco-IOS-XR-sysadmin-show-trace-instmgr',
            'all-options',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-sysadmin-show-trace-instmgr'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_show_trace_instmgr',
            is_config=False,
        ),
    },
    'Instmgr.Trace.Location' : {
        'meta_info' : _MetaInfoClass('Instmgr.Trace.Location', REFERENCE_LIST,
            ''' ''',
            False, 
            [
            _MetaInfoClassMember('location_name', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                ''',
                'location_name',
                'Cisco-IOS-XR-sysadmin-show-trace-instmgr', True, is_config=False),
            _MetaInfoClassMember('all-options', REFERENCE_LIST, 'AllOptions', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_show_trace_instmgr', 'Instmgr.Trace.Location.AllOptions',
                [], [],
                '''                ''',
                'all_options',
                'Cisco-IOS-XR-sysadmin-show-trace-instmgr', False, is_config=False),
            ],
            'Cisco-IOS-XR-sysadmin-show-trace-instmgr',
            'location',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-sysadmin-show-trace-instmgr'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_show_trace_instmgr',
            is_config=False,
        ),
    },
    'Instmgr.Trace' : {
        'meta_info' : _MetaInfoClass('Instmgr.Trace', REFERENCE_LIST,
            '''show traceable processes''',
            False, 
            [
            _MetaInfoClassMember('buffer', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                ''',
                'buffer',
                'Cisco-IOS-XR-sysadmin-show-trace-instmgr', True, is_config=False),
            _MetaInfoClassMember('location', REFERENCE_LIST, 'Location', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_show_trace_instmgr', 'Instmgr.Trace.Location',
                [], [],
                '''                ''',
                'location',
                'Cisco-IOS-XR-sysadmin-show-trace-instmgr', False, is_config=False),
            ],
            'Cisco-IOS-XR-sysadmin-show-trace-instmgr',
            'trace',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-sysadmin-show-trace-instmgr'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_show_trace_instmgr',
            is_config=False,
        ),
    },
    'Instmgr' : {
        'meta_info' : _MetaInfoClass('Instmgr', REFERENCE_CLASS,
            ''' ''',
            False, 
            [
            _MetaInfoClassMember('trace', REFERENCE_LIST, 'Trace', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_show_trace_instmgr', 'Instmgr.Trace',
                [], [],
                '''                show traceable processes
                ''',
                'trace',
                'Cisco-IOS-XR-sysadmin-show-trace-instmgr', False, is_config=False),
            ],
            'Cisco-IOS-XR-sysadmin-show-trace-instmgr',
            'instmgr',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-sysadmin-show-trace-instmgr'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_show_trace_instmgr',
            is_config=False,
        ),
    },
}
_meta_table['Instmgr.Trace.Location.AllOptions.TraceBlocks']['meta_info'].parent =_meta_table['Instmgr.Trace.Location.AllOptions']['meta_info']
_meta_table['Instmgr.Trace.Location.AllOptions']['meta_info'].parent =_meta_table['Instmgr.Trace.Location']['meta_info']
_meta_table['Instmgr.Trace.Location']['meta_info'].parent =_meta_table['Instmgr.Trace']['meta_info']
_meta_table['Instmgr.Trace']['meta_info'].parent =_meta_table['Instmgr']['meta_info']
