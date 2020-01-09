
'''
This is auto-generated file,
which includes metadata for module Cisco_IOS_XR_spirit_corehelper_cfg
'''

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_LIST, REFERENCE_LEAFLIST, REFERENCE_BITS, REFERENCE_UNION
from ydk._core._dm_meta_info import REFERENCE_CLASS, REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, ANYXML_CLASS
from ydk._core._importer import _yang_ns

_meta_table = {
    'Exception.File' : {
        'meta_info' : _MetaInfoClass('Exception.File', REFERENCE_CLASS,
            '''Container for the order of preference''',
            False, 
            [
            _MetaInfoClassMember('choice2', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                Preference of the dump location
                ''',
                'choice2',
                'Cisco-IOS-XR-spirit-corehelper-cfg', False),
            _MetaInfoClassMember('choice1', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                Preference of the dump location
                ''',
                'choice1',
                'Cisco-IOS-XR-spirit-corehelper-cfg', False),
            _MetaInfoClassMember('choice3', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                Preference of the dump location
                ''',
                'choice3',
                'Cisco-IOS-XR-spirit-corehelper-cfg', False),
            ],
            'Cisco-IOS-XR-spirit-corehelper-cfg',
            'file',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-spirit-corehelper-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_spirit_corehelper_cfg',
        ),
    },
    'Exception' : {
        'meta_info' : _MetaInfoClass('Exception', REFERENCE_CLASS,
            '''Core dump configuration commands''',
            False, 
            [
            _MetaInfoClassMember('file', REFERENCE_CLASS, 'File', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_spirit_corehelper_cfg', 'Exception.File',
                [], [],
                '''                Container for the order of preference
                ''',
                'file',
                'Cisco-IOS-XR-spirit-corehelper-cfg', False),
            ],
            'Cisco-IOS-XR-spirit-corehelper-cfg',
            'exception',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-spirit-corehelper-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_spirit_corehelper_cfg',
        ),
    },
}
_meta_table['Exception.File']['meta_info'].parent =_meta_table['Exception']['meta_info']
