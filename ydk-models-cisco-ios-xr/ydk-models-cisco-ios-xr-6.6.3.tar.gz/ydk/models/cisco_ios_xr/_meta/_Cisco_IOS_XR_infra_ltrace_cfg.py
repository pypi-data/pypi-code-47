
'''
This is auto-generated file,
which includes metadata for module Cisco_IOS_XR_infra_ltrace_cfg
'''

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_LIST, REFERENCE_LEAFLIST, REFERENCE_BITS, REFERENCE_UNION
from ydk._core._dm_meta_info import REFERENCE_CLASS, REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, ANYXML_CLASS
from ydk._core._importer import _yang_ns

_meta_table = {
    'InfraLtraceMode' : _MetaInfoEnum('InfraLtraceMode',
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_ltrace_cfg', 'InfraLtraceMode',
        '''Infra ltrace mode''',
        {
            'static':'static',
            'dynamic':'dynamic',
        }, 'Cisco-IOS-XR-infra-ltrace-cfg', _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-infra-ltrace-cfg']),
    'InfraLtraceScale' : _MetaInfoEnum('InfraLtraceScale',
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_ltrace_cfg', 'InfraLtraceScale',
        '''Infra ltrace scale''',
        {
            '0':'Y_0',
            '1':'Y_1',
            '2':'Y_2',
            '4':'Y_4',
            '8':'Y_8',
            '16':'Y_16',
        }, 'Cisco-IOS-XR-infra-ltrace-cfg', _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-infra-ltrace-cfg']),
}
