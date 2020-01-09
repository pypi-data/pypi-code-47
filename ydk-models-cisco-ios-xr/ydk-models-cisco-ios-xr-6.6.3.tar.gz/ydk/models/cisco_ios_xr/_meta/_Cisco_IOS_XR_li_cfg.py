
'''
This is auto-generated file,
which includes metadata for module Cisco_IOS_XR_li_cfg
'''

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_LIST, REFERENCE_LEAFLIST, REFERENCE_BITS, REFERENCE_UNION
from ydk._core._dm_meta_info import REFERENCE_CLASS, REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, ANYXML_CLASS
from ydk._core._importer import _yang_ns

_meta_table = {
    'LawfulIntercept' : {
        'meta_info' : _MetaInfoClass('LawfulIntercept', REFERENCE_CLASS,
            '''Lawful intercept configuration''',
            False, 
            [
            _MetaInfoClassMember('disable', ATTRIBUTE, 'Empty', 'empty',
                None, None,
                [], [],
                '''                Disable lawful intercept feature
                ''',
                'disable',
                'Cisco-IOS-XR-li-cfg', False),
            ],
            'Cisco-IOS-XR-li-cfg',
            'lawful-intercept',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-li-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_li_cfg',
        ),
    },
}
