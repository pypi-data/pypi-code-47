
'''
This is auto-generated file,
which includes metadata for module Cisco_IOS_XR_ip_iep_oper
'''

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_LIST, REFERENCE_LEAFLIST, REFERENCE_BITS, REFERENCE_UNION
from ydk._core._dm_meta_info import REFERENCE_CLASS, REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, ANYXML_CLASS
from ydk._core._importer import _yang_ns

_meta_table = {
    'IepHop' : _MetaInfoEnum('IepHop',
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_iep_oper', 'IepHop',
        '''Hop types of the next-address configured''',
        {
            'strict':'strict',
            'loose':'loose',
        }, 'Cisco-IOS-XR-ip-iep-oper', _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-ip-iep-oper']),
    'IepAddress' : _MetaInfoEnum('IepAddress',
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_iep_oper', 'IepAddress',
        '''Address types''',
        {
            'next':'next',
            'exclude':'exclude',
            'exclude-srlg':'exclude_srlg',
        }, 'Cisco-IOS-XR-ip-iep-oper', _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-ip-iep-oper']),
    'IepStatus' : _MetaInfoEnum('IepStatus',
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_iep_oper', 'IepStatus',
        '''Status of the path''',
        {
            'enabled':'enabled',
            'disabled':'disabled',
        }, 'Cisco-IOS-XR-ip-iep-oper', _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-ip-iep-oper']),
    'ExplicitPaths.Identifiers.Identifier.Address' : {
        'meta_info' : _MetaInfoClass('ExplicitPaths.Identifiers.Identifier.Address', REFERENCE_LIST,
            '''List of IP addresses configured in the explicit
path''',
            False, 
            [
            _MetaInfoClassMember('index', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('0', '4294967295')], [],
                '''                Index number at which the path entry is inserted
                or modified
                ''',
                'index',
                'Cisco-IOS-XR-ip-iep-oper', False, is_config=False),
            _MetaInfoClassMember('if-index', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('0', '4294967295')], [],
                '''                Interface Index of the path
                ''',
                'if_index',
                'Cisco-IOS-XR-ip-iep-oper', False, is_config=False),
            _MetaInfoClassMember('address-type', REFERENCE_ENUM_CLASS, 'IepAddress', 'Iep-address',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_iep_oper', 'IepAddress',
                [], [],
                '''                Specifies the address type
                ''',
                'address_type',
                'Cisco-IOS-XR-ip-iep-oper', False, is_config=False),
            _MetaInfoClassMember('hop-type', REFERENCE_ENUM_CLASS, 'IepHop', 'Iep-hop',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_iep_oper', 'IepHop',
                [], [],
                '''                Specifies the next unicast address in the path
                as a strict or loose hop
                ''',
                'hop_type',
                'Cisco-IOS-XR-ip-iep-oper', False, is_config=False),
            _MetaInfoClassMember('address', ATTRIBUTE, 'str', 'inet:ipv4-address',
                None, None,
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'],
                '''                IPv4 unicast address
                ''',
                'address',
                'Cisco-IOS-XR-ip-iep-oper', False, is_config=False),
            _MetaInfoClassMember('mpls-label', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('0', '4294967295')], [],
                '''                MPLS label
                ''',
                'mpls_label',
                'Cisco-IOS-XR-ip-iep-oper', False, is_config=False),
            ],
            'Cisco-IOS-XR-ip-iep-oper',
            'address',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-ip-iep-oper'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_iep_oper',
            is_config=False,
        ),
    },
    'ExplicitPaths.Identifiers.Identifier' : {
        'meta_info' : _MetaInfoClass('ExplicitPaths.Identifiers.Identifier', REFERENCE_LIST,
            '''IP explicit path configured for a particular
identifier''',
            False, 
            [
            _MetaInfoClassMember('identifier-id', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('0', '4294967295')], [],
                '''                Identifier ID
                ''',
                'identifier_id',
                'Cisco-IOS-XR-ip-iep-oper', True, is_config=False),
            _MetaInfoClassMember('status', REFERENCE_ENUM_CLASS, 'IepStatus', 'Iep-status',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_iep_oper', 'IepStatus',
                [], [],
                '''                Status of the path
                ''',
                'status',
                'Cisco-IOS-XR-ip-iep-oper', False, is_config=False),
            _MetaInfoClassMember('address', REFERENCE_LIST, 'Address', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_iep_oper', 'ExplicitPaths.Identifiers.Identifier.Address',
                [], [],
                '''                List of IP addresses configured in the explicit
                path
                ''',
                'address',
                'Cisco-IOS-XR-ip-iep-oper', False, is_config=False),
            ],
            'Cisco-IOS-XR-ip-iep-oper',
            'identifier',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-ip-iep-oper'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_iep_oper',
            is_config=False,
        ),
    },
    'ExplicitPaths.Identifiers' : {
        'meta_info' : _MetaInfoClass('ExplicitPaths.Identifiers', REFERENCE_CLASS,
            '''List of configured IP explicit path identifiers,
this corresponds to mplsTunnelHopTable in TE MIB''',
            False, 
            [
            _MetaInfoClassMember('identifier', REFERENCE_LIST, 'Identifier', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_iep_oper', 'ExplicitPaths.Identifiers.Identifier',
                [], [],
                '''                IP explicit path configured for a particular
                identifier
                ''',
                'identifier',
                'Cisco-IOS-XR-ip-iep-oper', False, is_config=False),
            ],
            'Cisco-IOS-XR-ip-iep-oper',
            'identifiers',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-ip-iep-oper'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_iep_oper',
            is_config=False,
        ),
    },
    'ExplicitPaths.Names.Name.Address' : {
        'meta_info' : _MetaInfoClass('ExplicitPaths.Names.Name.Address', REFERENCE_LIST,
            '''List of IP addresses configured in the explicit
path''',
            False, 
            [
            _MetaInfoClassMember('index', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('0', '4294967295')], [],
                '''                Index number at which the path entry is inserted
                or modified
                ''',
                'index',
                'Cisco-IOS-XR-ip-iep-oper', False, is_config=False),
            _MetaInfoClassMember('if-index', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('0', '4294967295')], [],
                '''                Interface Index of the path
                ''',
                'if_index',
                'Cisco-IOS-XR-ip-iep-oper', False, is_config=False),
            _MetaInfoClassMember('address-type', REFERENCE_ENUM_CLASS, 'IepAddress', 'Iep-address',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_iep_oper', 'IepAddress',
                [], [],
                '''                Specifies the address type
                ''',
                'address_type',
                'Cisco-IOS-XR-ip-iep-oper', False, is_config=False),
            _MetaInfoClassMember('hop-type', REFERENCE_ENUM_CLASS, 'IepHop', 'Iep-hop',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_iep_oper', 'IepHop',
                [], [],
                '''                Specifies the next unicast address in the path
                as a strict or loose hop
                ''',
                'hop_type',
                'Cisco-IOS-XR-ip-iep-oper', False, is_config=False),
            _MetaInfoClassMember('address', ATTRIBUTE, 'str', 'inet:ipv4-address',
                None, None,
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'],
                '''                IPv4 unicast address
                ''',
                'address',
                'Cisco-IOS-XR-ip-iep-oper', False, is_config=False),
            _MetaInfoClassMember('mpls-label', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('0', '4294967295')], [],
                '''                MPLS label
                ''',
                'mpls_label',
                'Cisco-IOS-XR-ip-iep-oper', False, is_config=False),
            ],
            'Cisco-IOS-XR-ip-iep-oper',
            'address',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-ip-iep-oper'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_iep_oper',
            is_config=False,
        ),
    },
    'ExplicitPaths.Names.Name' : {
        'meta_info' : _MetaInfoClass('ExplicitPaths.Names.Name', REFERENCE_LIST,
            '''IP explicit path configured for a particular
path name''',
            False, 
            [
            _MetaInfoClassMember('path-name', ATTRIBUTE, 'str', 'xr:Cisco-ios-xr-string',
                None, None,
                [], [b'[\\w\\-\\.:,_@#%$\\+=\\|;]+'],
                '''                Path name
                ''',
                'path_name',
                'Cisco-IOS-XR-ip-iep-oper', True, is_config=False),
            _MetaInfoClassMember('status', REFERENCE_ENUM_CLASS, 'IepStatus', 'Iep-status',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_iep_oper', 'IepStatus',
                [], [],
                '''                Status of the path
                ''',
                'status',
                'Cisco-IOS-XR-ip-iep-oper', False, is_config=False),
            _MetaInfoClassMember('address', REFERENCE_LIST, 'Address', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_iep_oper', 'ExplicitPaths.Names.Name.Address',
                [], [],
                '''                List of IP addresses configured in the explicit
                path
                ''',
                'address',
                'Cisco-IOS-XR-ip-iep-oper', False, is_config=False),
            ],
            'Cisco-IOS-XR-ip-iep-oper',
            'name',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-ip-iep-oper'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_iep_oper',
            is_config=False,
        ),
    },
    'ExplicitPaths.Names' : {
        'meta_info' : _MetaInfoClass('ExplicitPaths.Names', REFERENCE_CLASS,
            '''List of configured IP explicit path names, this
corresponds to mplsTunnelHopTable in TE MIB''',
            False, 
            [
            _MetaInfoClassMember('name', REFERENCE_LIST, 'Name', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_iep_oper', 'ExplicitPaths.Names.Name',
                [], [],
                '''                IP explicit path configured for a particular
                path name
                ''',
                'name',
                'Cisco-IOS-XR-ip-iep-oper', False, is_config=False),
            ],
            'Cisco-IOS-XR-ip-iep-oper',
            'names',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-ip-iep-oper'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_iep_oper',
            is_config=False,
        ),
    },
    'ExplicitPaths' : {
        'meta_info' : _MetaInfoClass('ExplicitPaths', REFERENCE_CLASS,
            '''Configured IP explicit paths''',
            False, 
            [
            _MetaInfoClassMember('identifiers', REFERENCE_CLASS, 'Identifiers', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_iep_oper', 'ExplicitPaths.Identifiers',
                [], [],
                '''                List of configured IP explicit path identifiers,
                this corresponds to mplsTunnelHopTable in TE MIB
                ''',
                'identifiers',
                'Cisco-IOS-XR-ip-iep-oper', False, is_config=False),
            _MetaInfoClassMember('names', REFERENCE_CLASS, 'Names', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_iep_oper', 'ExplicitPaths.Names',
                [], [],
                '''                List of configured IP explicit path names, this
                corresponds to mplsTunnelHopTable in TE MIB
                ''',
                'names',
                'Cisco-IOS-XR-ip-iep-oper', False, is_config=False),
            ],
            'Cisco-IOS-XR-ip-iep-oper',
            'explicit-paths',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-ip-iep-oper'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_iep_oper',
            is_config=False,
        ),
    },
}
_meta_table['ExplicitPaths.Identifiers.Identifier.Address']['meta_info'].parent =_meta_table['ExplicitPaths.Identifiers.Identifier']['meta_info']
_meta_table['ExplicitPaths.Identifiers.Identifier']['meta_info'].parent =_meta_table['ExplicitPaths.Identifiers']['meta_info']
_meta_table['ExplicitPaths.Names.Name.Address']['meta_info'].parent =_meta_table['ExplicitPaths.Names.Name']['meta_info']
_meta_table['ExplicitPaths.Names.Name']['meta_info'].parent =_meta_table['ExplicitPaths.Names']['meta_info']
_meta_table['ExplicitPaths.Identifiers']['meta_info'].parent =_meta_table['ExplicitPaths']['meta_info']
_meta_table['ExplicitPaths.Names']['meta_info'].parent =_meta_table['ExplicitPaths']['meta_info']
