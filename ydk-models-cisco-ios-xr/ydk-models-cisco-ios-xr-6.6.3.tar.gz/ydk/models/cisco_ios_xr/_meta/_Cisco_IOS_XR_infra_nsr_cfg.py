
'''
This is auto-generated file,
which includes metadata for module Cisco_IOS_XR_infra_nsr_cfg
'''

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_LIST, REFERENCE_LEAFLIST, REFERENCE_BITS, REFERENCE_UNION
from ydk._core._dm_meta_info import REFERENCE_CLASS, REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, ANYXML_CLASS
from ydk._core._importer import _yang_ns

_meta_table = {
    'Nsr.ProcessFailure' : {
        'meta_info' : _MetaInfoClass('Nsr.ProcessFailure', REFERENCE_CLASS,
            '''Recovery action for process failures on active
RP/DRP''',
            False, 
            [
            _MetaInfoClassMember('switchover', ATTRIBUTE, 'Empty', 'empty',
                None, None,
                [], [],
                '''                Enable RP/DRP switchover on process failures
                ''',
                'switchover',
                'Cisco-IOS-XR-infra-nsr-cfg', False),
            ],
            'Cisco-IOS-XR-infra-nsr-cfg',
            'process-failure',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-infra-nsr-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_nsr_cfg',
        ),
    },
    'Nsr' : {
        'meta_info' : _MetaInfoClass('Nsr', REFERENCE_CLASS,
            '''NSR global configuration''',
            False, 
            [
            _MetaInfoClassMember('process-failure', REFERENCE_CLASS, 'ProcessFailure', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_nsr_cfg', 'Nsr.ProcessFailure',
                [], [],
                '''                Recovery action for process failures on active
                RP/DRP
                ''',
                'process_failure',
                'Cisco-IOS-XR-infra-nsr-cfg', False),
            ],
            'Cisco-IOS-XR-infra-nsr-cfg',
            'nsr',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-infra-nsr-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_nsr_cfg',
        ),
    },
}
_meta_table['Nsr.ProcessFailure']['meta_info'].parent =_meta_table['Nsr']['meta_info']
