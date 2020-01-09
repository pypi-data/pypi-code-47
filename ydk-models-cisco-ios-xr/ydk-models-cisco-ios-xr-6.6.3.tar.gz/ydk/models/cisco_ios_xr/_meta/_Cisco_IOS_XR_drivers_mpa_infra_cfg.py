
'''
This is auto-generated file,
which includes metadata for module Cisco_IOS_XR_drivers_mpa_infra_cfg
'''

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_LIST, REFERENCE_LEAFLIST, REFERENCE_BITS, REFERENCE_UNION
from ydk._core._dm_meta_info import REFERENCE_CLASS, REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, ANYXML_CLASS
from ydk._core._importer import _yang_ns

_meta_table = {
    'HwModuleShutdownPowerMode' : _MetaInfoEnum('HwModuleShutdownPowerMode',
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_drivers_mpa_infra_cfg', 'HwModuleShutdownPowerMode',
        '''Hw module shutdown power mode''',
        {
            'powered':'powered',
        }, 'Cisco-IOS-XR-drivers-mpa-infra-cfg', _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-drivers-mpa-infra-cfg']),
    'HardwareModule.Nodes.Node' : {
        'meta_info' : _MetaInfoClass('HardwareModule.Nodes.Node', REFERENCE_LIST,
            '''The identifier for a SPA node''',
            False, 
            [
            _MetaInfoClassMember('node-name', ATTRIBUTE, 'str', 'xr:Node-id',
                None, None,
                [], [b'([a-zA-Z0-9_]*\\d+/){1,2}([a-zA-Z0-9_]*\\d+)'],
                '''                A SPA node
                ''',
                'node_name',
                'Cisco-IOS-XR-drivers-mpa-infra-cfg', True),
            _MetaInfoClassMember('shutdown', REFERENCE_ENUM_CLASS, 'HwModuleShutdownPowerMode', 'Hw-module-shutdown-power-mode',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_drivers_mpa_infra_cfg', 'HwModuleShutdownPowerMode',
                [], [],
                '''                Shutdown a subslot h/w module
                ''',
                'shutdown',
                'Cisco-IOS-XR-drivers-mpa-infra-cfg', False),
            ],
            'Cisco-IOS-XR-drivers-mpa-infra-cfg',
            'node',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-drivers-mpa-infra-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_drivers_mpa_infra_cfg',
        ),
    },
    'HardwareModule.Nodes' : {
        'meta_info' : _MetaInfoClass('HardwareModule.Nodes', REFERENCE_CLASS,
            ''' subslot h/w module''',
            False, 
            [
            _MetaInfoClassMember('node', REFERENCE_LIST, 'Node', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_drivers_mpa_infra_cfg', 'HardwareModule.Nodes.Node',
                [], [],
                '''                The identifier for a SPA node
                ''',
                'node',
                'Cisco-IOS-XR-drivers-mpa-infra-cfg', False),
            ],
            'Cisco-IOS-XR-drivers-mpa-infra-cfg',
            'nodes',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-drivers-mpa-infra-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_drivers_mpa_infra_cfg',
        ),
    },
    'HardwareModule' : {
        'meta_info' : _MetaInfoClass('HardwareModule', REFERENCE_CLASS,
            '''Configure subslot h/w module''',
            False, 
            [
            _MetaInfoClassMember('nodes', REFERENCE_CLASS, 'Nodes', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_drivers_mpa_infra_cfg', 'HardwareModule.Nodes',
                [], [],
                '''                 subslot h/w module
                ''',
                'nodes',
                'Cisco-IOS-XR-drivers-mpa-infra-cfg', False),
            ],
            'Cisco-IOS-XR-drivers-mpa-infra-cfg',
            'hardware-module',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-drivers-mpa-infra-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_drivers_mpa_infra_cfg',
        ),
    },
}
_meta_table['HardwareModule.Nodes.Node']['meta_info'].parent =_meta_table['HardwareModule.Nodes']['meta_info']
_meta_table['HardwareModule.Nodes']['meta_info'].parent =_meta_table['HardwareModule']['meta_info']
