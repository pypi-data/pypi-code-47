
'''
This is auto-generated file,
which includes metadata for module Cisco_IOS_XR_clear_counters_act
'''

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_LIST, REFERENCE_LEAFLIST, REFERENCE_BITS, REFERENCE_UNION
from ydk._core._dm_meta_info import REFERENCE_CLASS, REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, ANYXML_CLASS
from ydk._core._importer import _yang_ns

_meta_table = {
    'ClearCounters.Input' : {
        'meta_info' : _MetaInfoClass('ClearCounters.Input', REFERENCE_CLASS,
            ''' ''',
            False, 
            [
            _MetaInfoClassMember('controller', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                Controller name in R/S/I/P format
                ''',
                'controller',
                'Cisco-IOS-XR-clear-counters-act', False),
            ],
            'Cisco-IOS-XR-clear-counters-act',
            'input',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-clear-counters-act'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clear_counters_act',
        ),
    },
    'ClearCounters' : {
        'meta_info' : _MetaInfoClass('ClearCounters', REFERENCE_CLASS,
            '''Execute clear counters operations''',
            False, 
            [
            _MetaInfoClassMember('input', REFERENCE_CLASS, 'Input', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clear_counters_act', 'ClearCounters.Input',
                [], [],
                '''                ''',
                'input',
                'Cisco-IOS-XR-clear-counters-act', False),
            ],
            'Cisco-IOS-XR-clear-counters-act',
            'clear-counters',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-clear-counters-act'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clear_counters_act',
        ),
    },
}
_meta_table['ClearCounters.Input']['meta_info'].parent =_meta_table['ClearCounters']['meta_info']
