
'''
This is auto-generated file,
which includes metadata for module Cisco_IOS_XR_sysadmin_zapdisk
'''

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_LIST, REFERENCE_LEAFLIST, REFERENCE_BITS, REFERENCE_UNION
from ydk._core._dm_meta_info import REFERENCE_CLASS, REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, ANYXML_CLASS
from ydk._core._importer import _yang_ns

_meta_table = {
    'Zapdisk.Input.CzapdiskUnset' : {
        'meta_info' : _MetaInfoClass('Zapdisk.Input.CzapdiskUnset', REFERENCE_CLASS,
            ''' ''',
            False, 
            [
            _MetaInfoClassMember('unset', ATTRIBUTE, 'Empty', 'empty',
                None, None,
                [], [],
                '''                ''',
                'unset',
                'Cisco-IOS-XR-sysadmin-zapdisk', False),
            ],
            'Cisco-IOS-XR-sysadmin-zapdisk',
            'czapdisk-unset',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-sysadmin-zapdisk'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_zapdisk',
        ),
    },
    'Zapdisk.Input' : {
        'meta_info' : _MetaInfoClass('Zapdisk.Input', REFERENCE_CLASS,
            ''' ''',
            False, 
            [
            _MetaInfoClassMember('set', ATTRIBUTE, 'Empty', 'empty',
                None, None,
                [], [],
                '''                ''',
                'set',
                'Cisco-IOS-XR-sysadmin-zapdisk', False),
            _MetaInfoClassMember('czapdisk-unset', REFERENCE_CLASS, 'CzapdiskUnset', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_zapdisk', 'Zapdisk.Input.CzapdiskUnset',
                [], [],
                '''                ''',
                'czapdisk_unset',
                'Cisco-IOS-XR-sysadmin-zapdisk', False),
            ],
            'Cisco-IOS-XR-sysadmin-zapdisk',
            'input',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-sysadmin-zapdisk'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_zapdisk',
        ),
    },
    'Zapdisk.Output' : {
        'meta_info' : _MetaInfoClass('Zapdisk.Output', REFERENCE_CLASS,
            ''' ''',
            False, 
            [
            _MetaInfoClassMember('result', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                ''',
                'result',
                'Cisco-IOS-XR-sysadmin-zapdisk', False, is_mandatory=True),
            ],
            'Cisco-IOS-XR-sysadmin-zapdisk',
            'output',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-sysadmin-zapdisk'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_zapdisk',
        ),
    },
    'Zapdisk' : {
        'meta_info' : _MetaInfoClass('Zapdisk', REFERENCE_CLASS,
            ''' ''',
            False, 
            [
            _MetaInfoClassMember('input', REFERENCE_CLASS, 'Input', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_zapdisk', 'Zapdisk.Input',
                [], [],
                '''                ''',
                'input',
                'Cisco-IOS-XR-sysadmin-zapdisk', False),
            _MetaInfoClassMember('output', REFERENCE_CLASS, 'Output', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_zapdisk', 'Zapdisk.Output',
                [], [],
                '''                ''',
                'output',
                'Cisco-IOS-XR-sysadmin-zapdisk', False),
            ],
            'Cisco-IOS-XR-sysadmin-zapdisk',
            'zapdisk',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-sysadmin-zapdisk'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_zapdisk',
        ),
    },
}
_meta_table['Zapdisk.Input.CzapdiskUnset']['meta_info'].parent =_meta_table['Zapdisk.Input']['meta_info']
_meta_table['Zapdisk.Input']['meta_info'].parent =_meta_table['Zapdisk']['meta_info']
_meta_table['Zapdisk.Output']['meta_info'].parent =_meta_table['Zapdisk']['meta_info']
