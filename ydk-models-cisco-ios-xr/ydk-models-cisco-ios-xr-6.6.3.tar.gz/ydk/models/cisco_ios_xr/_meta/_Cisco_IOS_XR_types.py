
'''
This is auto-generated file,
which includes metadata for module Cisco_IOS_XR_types
'''

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_LIST, REFERENCE_LEAFLIST, REFERENCE_BITS, REFERENCE_UNION
from ydk._core._dm_meta_info import REFERENCE_CLASS, REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, ANYXML_CLASS
from ydk._core._importer import _yang_ns

_meta_table = {
    'EncryptionType' : _MetaInfoEnum('EncryptionType',
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_types', 'EncryptionType',
        '''The type of encryption used on a password string.''',
        {
            'none':'none',
            'md5':'md5',
            'proprietary':'proprietary',
            'type6':'type6',
        }, 'Cisco-IOS-XR-types', _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-types']),
}
