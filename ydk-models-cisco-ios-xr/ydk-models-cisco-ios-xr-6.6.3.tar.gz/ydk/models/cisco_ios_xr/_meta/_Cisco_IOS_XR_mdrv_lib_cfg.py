
'''
This is auto-generated file,
which includes metadata for module Cisco_IOS_XR_mdrv_lib_cfg
'''

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_LIST, REFERENCE_LEAFLIST, REFERENCE_BITS, REFERENCE_UNION
from ydk._core._dm_meta_info import REFERENCE_CLASS, REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, ANYXML_CLASS
from ydk._core._importer import _yang_ns

_meta_table = {
    'FastShutdown' : {
        'meta_info' : _MetaInfoClass('FastShutdown', REFERENCE_CLASS,
            '''Fast Shutdown configuration''',
            False, 
            [
            _MetaInfoClassMember('ethernet', ATTRIBUTE, 'Empty', 'empty',
                None, None,
                [], [],
                '''                Enable Fast Shutdown for all Ethernet interfaces
                ''',
                'ethernet',
                'Cisco-IOS-XR-mdrv-lib-cfg', False),
            ],
            'Cisco-IOS-XR-mdrv-lib-cfg',
            'fast-shutdown',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-mdrv-lib-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mdrv_lib_cfg',
        ),
    },
}
