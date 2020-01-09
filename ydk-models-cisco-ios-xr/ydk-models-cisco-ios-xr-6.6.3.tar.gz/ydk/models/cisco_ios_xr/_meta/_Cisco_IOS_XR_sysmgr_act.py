
'''
This is auto-generated file,
which includes metadata for module Cisco_IOS_XR_sysmgr_act
'''

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_LIST, REFERENCE_LEAFLIST, REFERENCE_BITS, REFERENCE_UNION
from ydk._core._dm_meta_info import REFERENCE_CLASS, REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, ANYXML_CLASS
from ydk._core._importer import _yang_ns

_meta_table = {
    'SysmgrProcessRestart.Input' : {
        'meta_info' : _MetaInfoClass('SysmgrProcessRestart.Input', REFERENCE_CLASS,
            ''' ''',
            False, 
            [
            _MetaInfoClassMember('process-name', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                XR process name or Job Id e.g. bgp, ospf
                ''',
                'process_name',
                'Cisco-IOS-XR-sysmgr-act', False, is_mandatory=True),
            _MetaInfoClassMember('location', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                XR node identifier e.g. 0/RP0/CPU0, 0/0/CPU0
                ''',
                'location',
                'Cisco-IOS-XR-sysmgr-act', False),
            ],
            'Cisco-IOS-XR-sysmgr-act',
            'input',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-sysmgr-act'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysmgr_act',
        ),
    },
    'SysmgrProcessRestart' : {
        'meta_info' : _MetaInfoClass('SysmgrProcessRestart', REFERENCE_CLASS,
            '''Restart an XR process''',
            False, 
            [
            _MetaInfoClassMember('input', REFERENCE_CLASS, 'Input', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysmgr_act', 'SysmgrProcessRestart.Input',
                [], [],
                '''                ''',
                'input',
                'Cisco-IOS-XR-sysmgr-act', False),
            ],
            'Cisco-IOS-XR-sysmgr-act',
            'sysmgr-process-restart',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-sysmgr-act'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysmgr_act',
        ),
    },
}
_meta_table['SysmgrProcessRestart.Input']['meta_info'].parent =_meta_table['SysmgrProcessRestart']['meta_info']
