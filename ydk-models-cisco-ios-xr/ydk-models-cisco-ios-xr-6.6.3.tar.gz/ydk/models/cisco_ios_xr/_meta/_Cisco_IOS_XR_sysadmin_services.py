
'''
This is auto-generated file,
which includes metadata for module Cisco_IOS_XR_sysadmin_services
'''

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_LIST, REFERENCE_LEAFLIST, REFERENCE_BITS, REFERENCE_UNION
from ydk._core._dm_meta_info import REFERENCE_CLASS, REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, ANYXML_CLASS
from ydk._core._importer import _yang_ns

_meta_table = {
    'Service.Cli.Interactive' : {
        'meta_info' : _MetaInfoClass('Service.Cli.Interactive', REFERENCE_CLASS,
            ''' ''',
            False, 
            [
            _MetaInfoClassMember('enabled', ATTRIBUTE, 'bool', 'boolean',
                None, None,
                [], [],
                '''                ''',
                'enabled',
                'Cisco-IOS-XR-sysadmin-services', False, default_value='True'),
            ],
            'Cisco-IOS-XR-sysadmin-services',
            'interactive',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-sysadmin-services'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_services',
        ),
    },
    'Service.Cli' : {
        'meta_info' : _MetaInfoClass('Service.Cli', REFERENCE_CLASS,
            ''' ''',
            False, 
            [
            _MetaInfoClassMember('interactive', REFERENCE_CLASS, 'Interactive', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_services', 'Service.Cli.Interactive',
                [], [],
                '''                ''',
                'interactive',
                'Cisco-IOS-XR-sysadmin-services', False),
            ],
            'Cisco-IOS-XR-sysadmin-services',
            'cli',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-sysadmin-services'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_services',
        ),
    },
    'Service' : {
        'meta_info' : _MetaInfoClass('Service', REFERENCE_CLASS,
            ''' ''',
            False, 
            [
            _MetaInfoClassMember('cli', REFERENCE_CLASS, 'Cli', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_services', 'Service.Cli',
                [], [],
                '''                ''',
                'cli',
                'Cisco-IOS-XR-sysadmin-services', False),
            ],
            'Cisco-IOS-XR-sysadmin-services',
            'service',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-sysadmin-services'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_services',
        ),
    },
}
_meta_table['Service.Cli.Interactive']['meta_info'].parent =_meta_table['Service.Cli']['meta_info']
_meta_table['Service.Cli']['meta_info'].parent =_meta_table['Service']['meta_info']
