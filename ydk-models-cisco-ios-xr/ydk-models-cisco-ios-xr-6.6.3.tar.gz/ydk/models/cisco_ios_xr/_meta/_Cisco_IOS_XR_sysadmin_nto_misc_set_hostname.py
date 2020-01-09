
'''
This is auto-generated file,
which includes metadata for module Cisco_IOS_XR_sysadmin_nto_misc_set_hostname
'''

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_LIST, REFERENCE_LEAFLIST, REFERENCE_BITS, REFERENCE_UNION
from ydk._core._dm_meta_info import REFERENCE_CLASS, REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, ANYXML_CLASS
from ydk._core._importer import _yang_ns

_meta_table = {
    'Hostname' : {
        'meta_info' : _MetaInfoClass('Hostname', REFERENCE_CLASS,
            '''Set system`s network name''',
            False, 
            [
            _MetaInfoClassMember('name', ATTRIBUTE, 'str', 'string',
                None, None,
                [(1, 255)], [],
                '''                ''',
                'name',
                'Cisco-IOS-XR-sysadmin-nto-misc-set-hostname', False),
            ],
            'Cisco-IOS-XR-sysadmin-nto-misc-set-hostname',
            'hostname',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-sysadmin-nto-misc-set-hostname'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_nto_misc_set_hostname',
        ),
    },
}
