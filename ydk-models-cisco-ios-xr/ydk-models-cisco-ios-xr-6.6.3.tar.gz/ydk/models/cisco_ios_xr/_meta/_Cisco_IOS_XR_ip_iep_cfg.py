
'''
This is auto-generated file,
which includes metadata for module Cisco_IOS_XR_ip_iep_cfg
'''

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_LIST, REFERENCE_LEAFLIST, REFERENCE_BITS, REFERENCE_UNION
from ydk._core._dm_meta_info import REFERENCE_CLASS, REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, ANYXML_CLASS
from ydk._core._importer import _yang_ns

_meta_table = {
    'IpIepNum' : _MetaInfoEnum('IpIepNum',
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_iep_cfg', 'IpIepNum',
        '''Ip iep num''',
        {
            'unnumbered':'unnumbered',
            'numbered':'numbered',
        }, 'Cisco-IOS-XR-ip-iep-cfg', _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-ip-iep-cfg']),
    'IpIepHop' : _MetaInfoEnum('IpIepHop',
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_iep_cfg', 'IpIepHop',
        '''Ip iep hop''',
        {
            'next-strict':'next_strict',
            'next-loose':'next_loose',
            'exclude':'exclude',
            'exclude-srlg':'exclude_srlg',
            'next-label':'next_label',
        }, 'Cisco-IOS-XR-ip-iep-cfg', _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-ip-iep-cfg']),
    'IpIepPath' : _MetaInfoEnum('IpIepPath',
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_iep_cfg', 'IpIepPath',
        '''Ip iep path''',
        {
            'identifier':'identifier',
            'name':'name',
        }, 'Cisco-IOS-XR-ip-iep-cfg', _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-ip-iep-cfg']),
    'IpExplicitPaths.Paths.Path.Name.Hops.Hop' : {
        'meta_info' : _MetaInfoClass('IpExplicitPaths.Paths.Path.Name.Hops.Hop', REFERENCE_LIST,
            '''Hop Information''',
            False, 
            [
            _MetaInfoClassMember('index-number', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('1', '65535')], [],
                '''                Index number
                ''',
                'index_number',
                'Cisco-IOS-XR-ip-iep-cfg', True),
            _MetaInfoClassMember('ip-address', ATTRIBUTE, 'str', 'inet:ipv4-address-no-zone',
                None, None,
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'],
                '''                IP address of the hop
                ''',
                'ip_address',
                'Cisco-IOS-XR-ip-iep-cfg', False, default_value="'0.0.0.0'", has_when=True),
            _MetaInfoClassMember('hop-type', REFERENCE_ENUM_CLASS, 'IpIepHop', 'Ip-iep-hop',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_iep_cfg', 'IpIepHop',
                [], [],
                '''                Include or exclude this hop in the path
                ''',
                'hop_type',
                'Cisco-IOS-XR-ip-iep-cfg', False, default_value='Cisco_IOS_XR_ip_iep_cfg.IpIepHop.next_strict'),
            _MetaInfoClassMember('if-index', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('0', '4294967295')], [],
                '''                Ifindex value
                ''',
                'if_index',
                'Cisco-IOS-XR-ip-iep-cfg', False, default_value="0", has_when=True),
            _MetaInfoClassMember('num-type', REFERENCE_ENUM_CLASS, 'IpIepNum', 'Ip-iep-num',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_iep_cfg', 'IpIepNum',
                [], [],
                '''                Number type Numbered or Unnumbered
                ''',
                'num_type',
                'Cisco-IOS-XR-ip-iep-cfg', False, default_value='Cisco_IOS_XR_ip_iep_cfg.IpIepNum.numbered', has_when=True),
            _MetaInfoClassMember('mpls-label', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('0', '1048575')], [],
                '''                MPLS Label
                ''',
                'mpls_label',
                'Cisco-IOS-XR-ip-iep-cfg', False, has_when=True),
            ],
            'Cisco-IOS-XR-ip-iep-cfg',
            'hop',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-ip-iep-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_iep_cfg',
        ),
    },
    'IpExplicitPaths.Paths.Path.Name.Hops' : {
        'meta_info' : _MetaInfoClass('IpExplicitPaths.Paths.Path.Name.Hops', REFERENCE_CLASS,
            '''List of Hops''',
            False, 
            [
            _MetaInfoClassMember('hop', REFERENCE_LIST, 'Hop', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_iep_cfg', 'IpExplicitPaths.Paths.Path.Name.Hops.Hop',
                [], [],
                '''                Hop Information
                ''',
                'hop',
                'Cisco-IOS-XR-ip-iep-cfg', False),
            ],
            'Cisco-IOS-XR-ip-iep-cfg',
            'hops',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-ip-iep-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_iep_cfg',
        ),
    },
    'IpExplicitPaths.Paths.Path.Name' : {
        'meta_info' : _MetaInfoClass('IpExplicitPaths.Paths.Path.Name', REFERENCE_LIST,
            '''name''',
            False, 
            [
            _MetaInfoClassMember('name', ATTRIBUTE, 'str', 'xr:Cisco-ios-xr-string',
                None, None,
                [], [b'[\\w\\-\\.:,_@#%$\\+=\\|;]+'],
                '''                Path name
                ''',
                'name',
                'Cisco-IOS-XR-ip-iep-cfg', True),
            _MetaInfoClassMember('hops', REFERENCE_CLASS, 'Hops', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_iep_cfg', 'IpExplicitPaths.Paths.Path.Name.Hops',
                [], [],
                '''                List of Hops
                ''',
                'hops',
                'Cisco-IOS-XR-ip-iep-cfg', False),
            _MetaInfoClassMember('disable', ATTRIBUTE, 'Empty', 'empty',
                None, None,
                [], [],
                '''                Disable the explicit path
                ''',
                'disable',
                'Cisco-IOS-XR-ip-iep-cfg', False),
            ],
            'Cisco-IOS-XR-ip-iep-cfg',
            'name',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-ip-iep-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_iep_cfg',
            has_when=True,
        ),
    },
    'IpExplicitPaths.Paths.Path.Identifier.Hops.Hop' : {
        'meta_info' : _MetaInfoClass('IpExplicitPaths.Paths.Path.Identifier.Hops.Hop', REFERENCE_LIST,
            '''Hop Information''',
            False, 
            [
            _MetaInfoClassMember('index-number', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('1', '65535')], [],
                '''                Index number
                ''',
                'index_number',
                'Cisco-IOS-XR-ip-iep-cfg', True),
            _MetaInfoClassMember('ip-address', ATTRIBUTE, 'str', 'inet:ipv4-address-no-zone',
                None, None,
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'],
                '''                IP address of the hop
                ''',
                'ip_address',
                'Cisco-IOS-XR-ip-iep-cfg', False, default_value="'0.0.0.0'", has_when=True),
            _MetaInfoClassMember('hop-type', REFERENCE_ENUM_CLASS, 'IpIepHop', 'Ip-iep-hop',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_iep_cfg', 'IpIepHop',
                [], [],
                '''                Include or exclude this hop in the path
                ''',
                'hop_type',
                'Cisco-IOS-XR-ip-iep-cfg', False, default_value='Cisco_IOS_XR_ip_iep_cfg.IpIepHop.next_strict'),
            _MetaInfoClassMember('if-index', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('0', '4294967295')], [],
                '''                Ifindex value
                ''',
                'if_index',
                'Cisco-IOS-XR-ip-iep-cfg', False, default_value="0", has_when=True),
            _MetaInfoClassMember('num-type', REFERENCE_ENUM_CLASS, 'IpIepNum', 'Ip-iep-num',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_iep_cfg', 'IpIepNum',
                [], [],
                '''                Number type Numbered or Unnumbered
                ''',
                'num_type',
                'Cisco-IOS-XR-ip-iep-cfg', False, default_value='Cisco_IOS_XR_ip_iep_cfg.IpIepNum.numbered', has_when=True),
            _MetaInfoClassMember('mpls-label', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('0', '1048575')], [],
                '''                MPLS Label
                ''',
                'mpls_label',
                'Cisco-IOS-XR-ip-iep-cfg', False, has_when=True),
            ],
            'Cisco-IOS-XR-ip-iep-cfg',
            'hop',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-ip-iep-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_iep_cfg',
        ),
    },
    'IpExplicitPaths.Paths.Path.Identifier.Hops' : {
        'meta_info' : _MetaInfoClass('IpExplicitPaths.Paths.Path.Identifier.Hops', REFERENCE_CLASS,
            '''List of Hops''',
            False, 
            [
            _MetaInfoClassMember('hop', REFERENCE_LIST, 'Hop', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_iep_cfg', 'IpExplicitPaths.Paths.Path.Identifier.Hops.Hop',
                [], [],
                '''                Hop Information
                ''',
                'hop',
                'Cisco-IOS-XR-ip-iep-cfg', False),
            ],
            'Cisco-IOS-XR-ip-iep-cfg',
            'hops',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-ip-iep-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_iep_cfg',
        ),
    },
    'IpExplicitPaths.Paths.Path.Identifier' : {
        'meta_info' : _MetaInfoClass('IpExplicitPaths.Paths.Path.Identifier', REFERENCE_LIST,
            '''identifier''',
            False, 
            [
            _MetaInfoClassMember('id', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('1', '65535')], [],
                '''                Path identifier
                ''',
                'id',
                'Cisco-IOS-XR-ip-iep-cfg', True),
            _MetaInfoClassMember('hops', REFERENCE_CLASS, 'Hops', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_iep_cfg', 'IpExplicitPaths.Paths.Path.Identifier.Hops',
                [], [],
                '''                List of Hops
                ''',
                'hops',
                'Cisco-IOS-XR-ip-iep-cfg', False),
            _MetaInfoClassMember('disable', ATTRIBUTE, 'Empty', 'empty',
                None, None,
                [], [],
                '''                Disable the explicit path
                ''',
                'disable',
                'Cisco-IOS-XR-ip-iep-cfg', False),
            ],
            'Cisco-IOS-XR-ip-iep-cfg',
            'identifier',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-ip-iep-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_iep_cfg',
            has_when=True,
        ),
    },
    'IpExplicitPaths.Paths.Path' : {
        'meta_info' : _MetaInfoClass('IpExplicitPaths.Paths.Path', REFERENCE_LIST,
            '''Config data for a specific explicit path''',
            False, 
            [
            _MetaInfoClassMember('type', REFERENCE_ENUM_CLASS, 'IpIepPath', 'Ip-iep-path',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_iep_cfg', 'IpIepPath',
                [], [],
                '''                Path type
                ''',
                'type',
                'Cisco-IOS-XR-ip-iep-cfg', True),
            _MetaInfoClassMember('name', REFERENCE_LIST, 'Name', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_iep_cfg', 'IpExplicitPaths.Paths.Path.Name',
                [], [],
                '''                name
                ''',
                'name',
                'Cisco-IOS-XR-ip-iep-cfg', False, has_when=True),
            _MetaInfoClassMember('identifier', REFERENCE_LIST, 'Identifier', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_iep_cfg', 'IpExplicitPaths.Paths.Path.Identifier',
                [], [],
                '''                identifier
                ''',
                'identifier',
                'Cisco-IOS-XR-ip-iep-cfg', False, has_when=True),
            ],
            'Cisco-IOS-XR-ip-iep-cfg',
            'path',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-ip-iep-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_iep_cfg',
            has_must=True,
        ),
    },
    'IpExplicitPaths.Paths' : {
        'meta_info' : _MetaInfoClass('IpExplicitPaths.Paths', REFERENCE_CLASS,
            '''A list of explicit paths''',
            False, 
            [
            _MetaInfoClassMember('path', REFERENCE_LIST, 'Path', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_iep_cfg', 'IpExplicitPaths.Paths.Path',
                [], [],
                '''                Config data for a specific explicit path
                ''',
                'path',
                'Cisco-IOS-XR-ip-iep-cfg', False, has_must=True),
            ],
            'Cisco-IOS-XR-ip-iep-cfg',
            'paths',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-ip-iep-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_iep_cfg',
        ),
    },
    'IpExplicitPaths' : {
        'meta_info' : _MetaInfoClass('IpExplicitPaths', REFERENCE_CLASS,
            '''IP Explicit Path config data''',
            False, 
            [
            _MetaInfoClassMember('paths', REFERENCE_CLASS, 'Paths', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_iep_cfg', 'IpExplicitPaths.Paths',
                [], [],
                '''                A list of explicit paths
                ''',
                'paths',
                'Cisco-IOS-XR-ip-iep-cfg', False),
            ],
            'Cisco-IOS-XR-ip-iep-cfg',
            'ip-explicit-paths',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-ip-iep-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_iep_cfg',
        ),
    },
}
_meta_table['IpExplicitPaths.Paths.Path.Name.Hops.Hop']['meta_info'].parent =_meta_table['IpExplicitPaths.Paths.Path.Name.Hops']['meta_info']
_meta_table['IpExplicitPaths.Paths.Path.Name.Hops']['meta_info'].parent =_meta_table['IpExplicitPaths.Paths.Path.Name']['meta_info']
_meta_table['IpExplicitPaths.Paths.Path.Identifier.Hops.Hop']['meta_info'].parent =_meta_table['IpExplicitPaths.Paths.Path.Identifier.Hops']['meta_info']
_meta_table['IpExplicitPaths.Paths.Path.Identifier.Hops']['meta_info'].parent =_meta_table['IpExplicitPaths.Paths.Path.Identifier']['meta_info']
_meta_table['IpExplicitPaths.Paths.Path.Name']['meta_info'].parent =_meta_table['IpExplicitPaths.Paths.Path']['meta_info']
_meta_table['IpExplicitPaths.Paths.Path.Identifier']['meta_info'].parent =_meta_table['IpExplicitPaths.Paths.Path']['meta_info']
_meta_table['IpExplicitPaths.Paths.Path']['meta_info'].parent =_meta_table['IpExplicitPaths.Paths']['meta_info']
_meta_table['IpExplicitPaths.Paths']['meta_info'].parent =_meta_table['IpExplicitPaths']['meta_info']
