
'''
This is auto-generated file,
which includes metadata for module Cisco_IOS_XR_sysadmin_dumper
'''

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_LIST, REFERENCE_LEAFLIST, REFERENCE_BITS, REFERENCE_UNION
from ydk._core._dm_meta_info import REFERENCE_CLASS, REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, ANYXML_CLASS
from ydk._core._importer import _yang_ns

_meta_table = {
    'Exception.Choice' : {
        'meta_info' : _MetaInfoClass('Exception.Choice', REFERENCE_LIST,
            ''' ''',
            False, 
            [
            _MetaInfoClassMember('order', ATTRIBUTE, 'int', 'int32',
                None, None,
                [('1', '3')], [],
                '''                ''',
                'order',
                'Cisco-IOS-XR-sysadmin-dumper', True),
            _MetaInfoClassMember('filepath', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                ''',
                'filepath',
                'Cisco-IOS-XR-sysadmin-dumper', False, is_mandatory=True),
            ],
            'Cisco-IOS-XR-sysadmin-dumper',
            'choice',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-sysadmin-dumper'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_dumper',
        ),
    },
    'Exception' : {
        'meta_info' : _MetaInfoClass('Exception', REFERENCE_CLASS,
            ''' ''',
            False, 
            [
            _MetaInfoClassMember('choice', REFERENCE_LIST, 'Choice', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_dumper', 'Exception.Choice',
                [], [],
                '''                ''',
                'choice',
                'Cisco-IOS-XR-sysadmin-dumper', False),
            ],
            'Cisco-IOS-XR-sysadmin-dumper',
            'exception',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-sysadmin-dumper'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_dumper',
        ),
    },
}
_meta_table['Exception.Choice']['meta_info'].parent =_meta_table['Exception']['meta_info']
