
'''
This is auto-generated file,
which includes metadata for module Cisco_IOS_XR_hwmod_mpa_reload_act
'''

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_LIST, REFERENCE_LEAFLIST, REFERENCE_BITS, REFERENCE_UNION
from ydk._core._dm_meta_info import REFERENCE_CLASS, REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, ANYXML_CLASS
from ydk._core._importer import _yang_ns

_meta_table = {
    'HwModuleSubslot.Input' : {
        'meta_info' : _MetaInfoClass('HwModuleSubslot.Input', REFERENCE_CLASS,
            ''' ''',
            False, 
            [
            _MetaInfoClassMember('subslot', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                Fully qualified location specification
                ''',
                'subslot',
                'Cisco-IOS-XR-hwmod-mpa-reload-act', False),
            _MetaInfoClassMember('reload', ATTRIBUTE, 'Empty', 'empty',
                None, None,
                [], [],
                '''                Cycle subslot h/w reset
                ''',
                'reload',
                'Cisco-IOS-XR-hwmod-mpa-reload-act', False),
            ],
            'Cisco-IOS-XR-hwmod-mpa-reload-act',
            'input',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-hwmod-mpa-reload-act'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_hwmod_mpa_reload_act',
        ),
    },
    'HwModuleSubslot' : {
        'meta_info' : _MetaInfoClass('HwModuleSubslot', REFERENCE_CLASS,
            '''Execute subslot h/w module operations''',
            False, 
            [
            _MetaInfoClassMember('input', REFERENCE_CLASS, 'Input', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_hwmod_mpa_reload_act', 'HwModuleSubslot.Input',
                [], [],
                '''                ''',
                'input',
                'Cisco-IOS-XR-hwmod-mpa-reload-act', False),
            ],
            'Cisco-IOS-XR-hwmod-mpa-reload-act',
            'hw-module-subslot',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-hwmod-mpa-reload-act'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_hwmod_mpa_reload_act',
        ),
    },
}
_meta_table['HwModuleSubslot.Input']['meta_info'].parent =_meta_table['HwModuleSubslot']['meta_info']
