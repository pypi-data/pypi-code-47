
'''
This is auto-generated file,
which includes metadata for module Cisco_IOS_XR_sysadmin_external_usb
'''

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_LIST, REFERENCE_LEAFLIST, REFERENCE_BITS, REFERENCE_UNION
from ydk._core._dm_meta_info import REFERENCE_CLASS, REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, ANYXML_CLASS
from ydk._core._importer import _yang_ns

_meta_table = {
    'ExternalUsb.Config' : {
        'meta_info' : _MetaInfoClass('ExternalUsb.Config', REFERENCE_CLASS,
            ''' ''',
            False, 
            [
            _MetaInfoClassMember('disable', ATTRIBUTE, 'Empty', 'empty',
                None, None,
                [], [],
                '''                ''',
                'disable',
                'Cisco-IOS-XR-sysadmin-external-usb', False),
            ],
            'Cisco-IOS-XR-sysadmin-external-usb',
            'config',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-sysadmin-external-usb'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_external_usb',
        ),
    },
    'ExternalUsb' : {
        'meta_info' : _MetaInfoClass('ExternalUsb', REFERENCE_CLASS,
            ''' ''',
            False, 
            [
            _MetaInfoClassMember('config', REFERENCE_CLASS, 'Config', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_external_usb', 'ExternalUsb.Config',
                [], [],
                '''                ''',
                'config',
                'Cisco-IOS-XR-sysadmin-external-usb', False),
            ],
            'Cisco-IOS-XR-sysadmin-external-usb',
            'external-usb',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-sysadmin-external-usb'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_external_usb',
        ),
    },
}
_meta_table['ExternalUsb.Config']['meta_info'].parent =_meta_table['ExternalUsb']['meta_info']
