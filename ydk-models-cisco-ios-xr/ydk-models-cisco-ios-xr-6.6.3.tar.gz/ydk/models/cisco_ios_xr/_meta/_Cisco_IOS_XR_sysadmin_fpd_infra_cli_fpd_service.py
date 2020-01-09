
'''
This is auto-generated file,
which includes metadata for module Cisco_IOS_XR_sysadmin_fpd_infra_cli_fpd_service
'''

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_LIST, REFERENCE_LEAFLIST, REFERENCE_BITS, REFERENCE_UNION
from ydk._core._dm_meta_info import REFERENCE_CLASS, REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, ANYXML_CLASS
from ydk._core._importer import _yang_ns

_meta_table = {
    'Location.Fpd2' : {
        'meta_info' : _MetaInfoClass('Location.Fpd2', REFERENCE_LIST,
            ''' ''',
            False, 
            [
            _MetaInfoClassMember('name', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                ''',
                'name',
                'Cisco-IOS-XR-sysadmin-fpd-infra-cli-fpd-service', True, is_config=False),
            ],
            'Cisco-IOS-XR-sysadmin-fpd-infra-cli-fpd-service',
            'fpd2',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-sysadmin-fpd-infra-cli-fpd-service'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_fpd_infra_cli_fpd_service',
            is_config=False,
        ),
    },
    'Location' : {
        'meta_info' : _MetaInfoClass('Location', REFERENCE_LIST,
            ''' ''',
            False, 
            [
            _MetaInfoClassMember('loc', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                ''',
                'loc',
                'Cisco-IOS-XR-sysadmin-fpd-infra-cli-fpd-service', True, is_config=False),
            _MetaInfoClassMember('fpd2', REFERENCE_LIST, 'Fpd2', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_fpd_infra_cli_fpd_service', 'Location.Fpd2',
                [], [],
                '''                ''',
                'fpd2',
                'Cisco-IOS-XR-sysadmin-fpd-infra-cli-fpd-service', False, is_config=False),
            ],
            'Cisco-IOS-XR-sysadmin-fpd-infra-cli-fpd-service',
            'location',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-sysadmin-fpd-infra-cli-fpd-service'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_fpd_infra_cli_fpd_service',
            is_config=False,
        ),
    },
}
_meta_table['Location.Fpd2']['meta_info'].parent =_meta_table['Location']['meta_info']
