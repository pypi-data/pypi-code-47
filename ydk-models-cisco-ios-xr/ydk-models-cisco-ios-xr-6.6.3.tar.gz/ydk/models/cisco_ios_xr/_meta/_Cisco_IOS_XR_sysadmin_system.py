
'''
This is auto-generated file,
which includes metadata for module Cisco_IOS_XR_sysadmin_system
'''

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_LIST, REFERENCE_LEAFLIST, REFERENCE_BITS, REFERENCE_UNION
from ydk._core._dm_meta_info import REFERENCE_CLASS, REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, ANYXML_CLASS
from ydk._core._importer import _yang_ns

_meta_table = {
    'Mgmt.Ipv4' : {
        'meta_info' : _MetaInfoClass('Mgmt.Ipv4', REFERENCE_CLASS,
            ''' ''',
            False, 
            [
            _MetaInfoClassMember('address', ATTRIBUTE, 'str', 'calvados-ipv4-with-optional-subnet-bits',
                None, None,
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(/(([0-9])|([1-2][0-9])|(3[0-2])))?'],
                '''                ''',
                'address',
                'Cisco-IOS-XR-sysadmin-system', False, has_must=True),
            _MetaInfoClassMember('subnet-mask-ip', REFERENCE_UNION, 'str', 'ipv4-subnet-mask-ip',
                None, None,
                [], [],
                '''                ''',
                'subnet_mask_ip',
                'Cisco-IOS-XR-sysadmin-system', False, [
                    _MetaInfoClassMember('subnet-mask-ip', ATTRIBUTE, 'str', 'inet:ipv4-address',
                        None, None,
                        [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'],
                        '''                        ''',
                        'subnet_mask_ip',
                        'Cisco-IOS-XR-sysadmin-system', False, has_must=True),
                    _MetaInfoClassMember('subnet-mask-ip', ATTRIBUTE, 'str', 'inet:ipv6-address',
                        None, None,
                        [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'],
                        '''                        ''',
                        'subnet_mask_ip',
                        'Cisco-IOS-XR-sysadmin-system', False, has_must=True),
                ], has_must=True),
            ],
            'Cisco-IOS-XR-sysadmin-system',
            'ipv4',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-sysadmin-system'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_system',
        ),
    },
    'Mgmt.Ipv6' : {
        'meta_info' : _MetaInfoClass('Mgmt.Ipv6', REFERENCE_CLASS,
            ''' ''',
            False, 
            [
            _MetaInfoClassMember('address', ATTRIBUTE, 'str', 'calvados-ipv6-with-optional-prefix',
                None, None,
                [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(/(([0-9])|([0-9]{2})|(1[0-1][0-9])|(12[0-8])))?'],
                '''                ''',
                'address',
                'Cisco-IOS-XR-sysadmin-system', False, has_must=True),
            _MetaInfoClassMember('prefix', ATTRIBUTE, 'int', 'ipv6-prefix',
                None, None,
                [('0', '128')], [],
                '''                ''',
                'prefix',
                'Cisco-IOS-XR-sysadmin-system', False, has_must=True),
            ],
            'Cisco-IOS-XR-sysadmin-system',
            'ipv6',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-sysadmin-system'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_system',
        ),
    },
    'Mgmt' : {
        'meta_info' : _MetaInfoClass('Mgmt', REFERENCE_CLASS,
            ''' ''',
            False, 
            [
            _MetaInfoClassMember('ipv4', REFERENCE_CLASS, 'Ipv4', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_system', 'Mgmt.Ipv4',
                [], [],
                '''                ''',
                'ipv4',
                'Cisco-IOS-XR-sysadmin-system', False),
            _MetaInfoClassMember('ipv6', REFERENCE_CLASS, 'Ipv6', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_system', 'Mgmt.Ipv6',
                [], [],
                '''                ''',
                'ipv6',
                'Cisco-IOS-XR-sysadmin-system', False),
            ],
            'Cisco-IOS-XR-sysadmin-system',
            'mgmt',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-sysadmin-system'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_system',
        ),
    },
}
_meta_table['Mgmt.Ipv4']['meta_info'].parent =_meta_table['Mgmt']['meta_info']
_meta_table['Mgmt.Ipv6']['meta_info'].parent =_meta_table['Mgmt']['meta_info']
