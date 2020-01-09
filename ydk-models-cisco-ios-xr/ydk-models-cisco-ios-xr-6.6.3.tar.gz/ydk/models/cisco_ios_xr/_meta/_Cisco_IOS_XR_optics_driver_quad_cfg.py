
'''
This is auto-generated file,
which includes metadata for module Cisco_IOS_XR_optics_driver_quad_cfg
'''

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_LIST, REFERENCE_LEAFLIST, REFERENCE_BITS, REFERENCE_UNION
from ydk._core._dm_meta_info import REFERENCE_CLASS, REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, ANYXML_CLASS
from ydk._core._importer import _yang_ns

_meta_table = {
    'Node.Acts.Act.QuadConfigs.QuadConfig.Mode' : {
        'meta_info' : _MetaInfoClass('Node.Acts.Act.QuadConfigs.QuadConfig.Mode', REFERENCE_CLASS,
            '''select mode 10g or 25g for a quad(group of 4
ports).''',
            False, 
            [
            _MetaInfoClassMember('speed', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                speed 10g or 25g
                ''',
                'speed',
                'Cisco-IOS-XR-optics-driver-quad-cfg', False),
            ],
            'Cisco-IOS-XR-optics-driver-quad-cfg',
            'mode',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-optics-driver-quad-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_optics_driver_quad_cfg',
        ),
    },
    'Node.Acts.Act.QuadConfigs.QuadConfig' : {
        'meta_info' : _MetaInfoClass('Node.Acts.Act.QuadConfigs.QuadConfig', REFERENCE_LIST,
            '''none''',
            False, 
            [
            _MetaInfoClassMember('id1', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('0', '4294967295')], [],
                '''                none
                ''',
                'id1',
                'Cisco-IOS-XR-optics-driver-quad-cfg', True),
            _MetaInfoClassMember('mode', REFERENCE_CLASS, 'Mode', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_optics_driver_quad_cfg', 'Node.Acts.Act.QuadConfigs.QuadConfig.Mode',
                [], [],
                '''                select mode 10g or 25g for a quad(group of 4
                ports).
                ''',
                'mode',
                'Cisco-IOS-XR-optics-driver-quad-cfg', False),
            ],
            'Cisco-IOS-XR-optics-driver-quad-cfg',
            'quad-config',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-optics-driver-quad-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_optics_driver_quad_cfg',
        ),
    },
    'Node.Acts.Act.QuadConfigs' : {
        'meta_info' : _MetaInfoClass('Node.Acts.Act.QuadConfigs', REFERENCE_CLASS,
            '''quad configuration''',
            False, 
            [
            _MetaInfoClassMember('quad-config', REFERENCE_LIST, 'QuadConfig', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_optics_driver_quad_cfg', 'Node.Acts.Act.QuadConfigs.QuadConfig',
                [], [],
                '''                none
                ''',
                'quad_config',
                'Cisco-IOS-XR-optics-driver-quad-cfg', False),
            ],
            'Cisco-IOS-XR-optics-driver-quad-cfg',
            'quad-configs',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-optics-driver-quad-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_optics_driver_quad_cfg',
        ),
    },
    'Node.Acts.Act' : {
        'meta_info' : _MetaInfoClass('Node.Acts.Act', REFERENCE_LIST,
            '''Nodename''',
            False, 
            [
            _MetaInfoClassMember('node-name', ATTRIBUTE, 'str', 'xr:Cisco-ios-xr-string',
                None, None,
                [], [b'[\\w\\-\\.:,_@#%$\\+=\\|;]+'],
                '''                NodeName
                ''',
                'node_name',
                'Cisco-IOS-XR-optics-driver-quad-cfg', True),
            _MetaInfoClassMember('quad-configs', REFERENCE_CLASS, 'QuadConfigs', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_optics_driver_quad_cfg', 'Node.Acts.Act.QuadConfigs',
                [], [],
                '''                quad configuration
                ''',
                'quad_configs',
                'Cisco-IOS-XR-optics-driver-quad-cfg', False),
            ],
            'Cisco-IOS-XR-optics-driver-quad-cfg',
            'act',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-optics-driver-quad-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_optics_driver_quad_cfg',
        ),
    },
    'Node.Acts' : {
        'meta_info' : _MetaInfoClass('Node.Acts', REFERENCE_CLASS,
            '''none''',
            False, 
            [
            _MetaInfoClassMember('act', REFERENCE_LIST, 'Act', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_optics_driver_quad_cfg', 'Node.Acts.Act',
                [], [],
                '''                Nodename
                ''',
                'act',
                'Cisco-IOS-XR-optics-driver-quad-cfg', False),
            ],
            'Cisco-IOS-XR-optics-driver-quad-cfg',
            'acts',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-optics-driver-quad-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_optics_driver_quad_cfg',
        ),
    },
    'Node' : {
        'meta_info' : _MetaInfoClass('Node', REFERENCE_CLASS,
            '''HW module Quad Config''',
            False, 
            [
            _MetaInfoClassMember('acts', REFERENCE_CLASS, 'Acts', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_optics_driver_quad_cfg', 'Node.Acts',
                [], [],
                '''                none
                ''',
                'acts',
                'Cisco-IOS-XR-optics-driver-quad-cfg', False),
            ],
            'Cisco-IOS-XR-optics-driver-quad-cfg',
            'node',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-optics-driver-quad-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_optics_driver_quad_cfg',
        ),
    },
}
_meta_table['Node.Acts.Act.QuadConfigs.QuadConfig.Mode']['meta_info'].parent =_meta_table['Node.Acts.Act.QuadConfigs.QuadConfig']['meta_info']
_meta_table['Node.Acts.Act.QuadConfigs.QuadConfig']['meta_info'].parent =_meta_table['Node.Acts.Act.QuadConfigs']['meta_info']
_meta_table['Node.Acts.Act.QuadConfigs']['meta_info'].parent =_meta_table['Node.Acts.Act']['meta_info']
_meta_table['Node.Acts.Act']['meta_info'].parent =_meta_table['Node.Acts']['meta_info']
_meta_table['Node.Acts']['meta_info'].parent =_meta_table['Node']['meta_info']
