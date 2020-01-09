
'''
This is auto-generated file,
which includes metadata for module Cisco_IOS_XR_ascii_ltrace_oper
'''

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_LIST, REFERENCE_LEAFLIST, REFERENCE_BITS, REFERENCE_UNION
from ydk._core._dm_meta_info import REFERENCE_CLASS, REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, ANYXML_CLASS
from ydk._core._importer import _yang_ns

_meta_table = {
    'Ltrace.Features.Feature.Traces.Trace' : {
        'meta_info' : _MetaInfoClass('Ltrace.Features.Feature.Traces.Trace', REFERENCE_LIST,
            '''trace''',
            False, 
            [
            _MetaInfoClassMember('ltrace-id', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('0', '4294967295')], [],
                '''                Ltrace ID of ltrace
                ''',
                'ltrace_id',
                'Cisco-IOS-XR-ascii-ltrace-oper', True, is_config=False),
            _MetaInfoClassMember('timestamp', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                timestamp
                ''',
                'timestamp',
                'Cisco-IOS-XR-ascii-ltrace-oper', False, is_config=False),
            _MetaInfoClassMember('line', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                a single line of a trace point
                ''',
                'line',
                'Cisco-IOS-XR-ascii-ltrace-oper', False, is_config=False),
            ],
            'Cisco-IOS-XR-ascii-ltrace-oper',
            'trace',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-ascii-ltrace-oper'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ascii_ltrace_oper',
            is_config=False,
        ),
    },
    'Ltrace.Features.Feature.Traces' : {
        'meta_info' : _MetaInfoClass('Ltrace.Features.Feature.Traces', REFERENCE_CLASS,
            '''trace''',
            False, 
            [
            _MetaInfoClassMember('trace', REFERENCE_LIST, 'Trace', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ascii_ltrace_oper', 'Ltrace.Features.Feature.Traces.Trace',
                [], [],
                '''                trace
                ''',
                'trace',
                'Cisco-IOS-XR-ascii-ltrace-oper', False, is_config=False),
            ],
            'Cisco-IOS-XR-ascii-ltrace-oper',
            'traces',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-ascii-ltrace-oper'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ascii_ltrace_oper',
            is_config=False,
        ),
    },
    'Ltrace.Features.Feature' : {
        'meta_info' : _MetaInfoClass('Ltrace.Features.Feature', REFERENCE_LIST,
            '''feature''',
            False, 
            [
            _MetaInfoClassMember('traces', REFERENCE_CLASS, 'Traces', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ascii_ltrace_oper', 'Ltrace.Features.Feature.Traces',
                [], [],
                '''                trace
                ''',
                'traces',
                'Cisco-IOS-XR-ascii-ltrace-oper', False, is_config=False),
            _MetaInfoClassMember('feature-name', ATTRIBUTE, 'str', 'xr:Cisco-ios-xr-string',
                None, None,
                [], [b'[\\w\\-\\.:,_@#%$\\+=\\|;]+'],
                '''                feature name
                ''',
                'feature_name',
                'Cisco-IOS-XR-ascii-ltrace-oper', False, is_config=False),
            _MetaInfoClassMember('trace-buf', ATTRIBUTE, 'str', 'xr:Cisco-ios-xr-string',
                None, None,
                [], [b'[\\w\\-\\.:,_@#%$\\+=\\|;]+'],
                '''                trace buffer name
                ''',
                'trace_buf',
                'Cisco-IOS-XR-ascii-ltrace-oper', False, is_config=False),
            ],
            'Cisco-IOS-XR-ascii-ltrace-oper',
            'feature',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-ascii-ltrace-oper'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ascii_ltrace_oper',
            is_config=False,
        ),
    },
    'Ltrace.Features' : {
        'meta_info' : _MetaInfoClass('Ltrace.Features', REFERENCE_CLASS,
            '''feature''',
            False, 
            [
            _MetaInfoClassMember('feature', REFERENCE_LIST, 'Feature', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ascii_ltrace_oper', 'Ltrace.Features.Feature',
                [], [],
                '''                feature
                ''',
                'feature',
                'Cisco-IOS-XR-ascii-ltrace-oper', False, is_config=False),
            ],
            'Cisco-IOS-XR-ascii-ltrace-oper',
            'features',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-ascii-ltrace-oper'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ascii_ltrace_oper',
            is_config=False,
        ),
    },
    'Ltrace' : {
        'meta_info' : _MetaInfoClass('Ltrace', REFERENCE_CLASS,
            '''ASCII ltrace data''',
            False, 
            [
            _MetaInfoClassMember('features', REFERENCE_CLASS, 'Features', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ascii_ltrace_oper', 'Ltrace.Features',
                [], [],
                '''                feature
                ''',
                'features',
                'Cisco-IOS-XR-ascii-ltrace-oper', False, is_config=False),
            ],
            'Cisco-IOS-XR-ascii-ltrace-oper',
            'ltrace',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-ascii-ltrace-oper'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ascii_ltrace_oper',
            is_config=False,
        ),
    },
}
_meta_table['Ltrace.Features.Feature.Traces.Trace']['meta_info'].parent =_meta_table['Ltrace.Features.Feature.Traces']['meta_info']
_meta_table['Ltrace.Features.Feature.Traces']['meta_info'].parent =_meta_table['Ltrace.Features.Feature']['meta_info']
_meta_table['Ltrace.Features.Feature']['meta_info'].parent =_meta_table['Ltrace.Features']['meta_info']
_meta_table['Ltrace.Features']['meta_info'].parent =_meta_table['Ltrace']['meta_info']
