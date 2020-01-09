
'''
This is auto-generated file,
which includes metadata for module Cisco_IOS_XR_controller_ains_act
'''

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_LIST, REFERENCE_LEAFLIST, REFERENCE_BITS, REFERENCE_UNION
from ydk._core._dm_meta_info import REFERENCE_CLASS, REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, ANYXML_CLASS
from ydk._core._importer import _yang_ns

_meta_table = {
    'ControllerAinsSoak.Input' : {
        'meta_info' : _MetaInfoClass('ControllerAinsSoak.Input', REFERENCE_CLASS,
            ''' ''',
            False, 
            [
            _MetaInfoClassMember('controller', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                Controller name in R/S/I/P format
                ''',
                'controller',
                'Cisco-IOS-XR-controller-ains-act', False),
            _MetaInfoClassMember('hours', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('0', '48')], [],
                '''                Hours in range of 0-48
                ''',
                'hours',
                'Cisco-IOS-XR-controller-ains-act', False),
            _MetaInfoClassMember('minutes', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('0', '59')], [],
                '''                Minutes in range of 0-59
                ''',
                'minutes',
                'Cisco-IOS-XR-controller-ains-act', False),
            ],
            'Cisco-IOS-XR-controller-ains-act',
            'input',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-controller-ains-act'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_ains_act',
        ),
    },
    'ControllerAinsSoak' : {
        'meta_info' : _MetaInfoClass('ControllerAinsSoak', REFERENCE_CLASS,
            '''Execute ains soak configuration operations''',
            False, 
            [
            _MetaInfoClassMember('input', REFERENCE_CLASS, 'Input', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_ains_act', 'ControllerAinsSoak.Input',
                [], [],
                '''                ''',
                'input',
                'Cisco-IOS-XR-controller-ains-act', False),
            ],
            'Cisco-IOS-XR-controller-ains-act',
            'controller-ains-soak',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-controller-ains-act'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_ains_act',
        ),
    },
}
_meta_table['ControllerAinsSoak.Input']['meta_info'].parent =_meta_table['ControllerAinsSoak']['meta_info']
