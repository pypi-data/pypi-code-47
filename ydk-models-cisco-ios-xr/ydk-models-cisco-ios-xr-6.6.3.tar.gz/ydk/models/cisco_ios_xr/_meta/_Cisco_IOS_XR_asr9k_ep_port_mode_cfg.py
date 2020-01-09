
'''
This is auto-generated file,
which includes metadata for module Cisco_IOS_XR_asr9k_ep_port_mode_cfg
'''

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_LIST, REFERENCE_LEAFLIST, REFERENCE_BITS, REFERENCE_UNION
from ydk._core._dm_meta_info import REFERENCE_CLASS, REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, ANYXML_CLASS
from ydk._core._importer import _yang_ns

_meta_table = {
    'HwModuleEpIfPortMode' : _MetaInfoEnum('HwModuleEpIfPortMode',
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_ep_port_mode_cfg', 'HwModuleEpIfPortMode',
        '''Hw module ep if port mode''',
        {
            '2xhundredgige-16qam':'Y_2xhundredgige_16qam',
            '2xhundredgige-8qam':'Y_2xhundredgige_8qam',
        }, 'Cisco-IOS-XR-asr9k-ep-port-mode-cfg', _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-asr9k-ep-port-mode-cfg']),
    'HwModuleEpPortMode.EpPortModeConfiguration.Node.Bays.Bay.Ports.Port' : {
        'meta_info' : _MetaInfoClass('HwModuleEpPortMode.EpPortModeConfiguration.Node.Bays.Bay.Ports.Port', REFERENCE_LIST,
            '''Optics port number''',
            False, 
            [
            _MetaInfoClassMember('port-number', ATTRIBUTE, 'str', 'xr:Cisco-ios-xr-string',
                None, None,
                [], [b'[\\w\\-\\.:,_@#%$\\+=\\|;]+'],
                '''                Optics port number
                ''',
                'port_number',
                'Cisco-IOS-XR-asr9k-ep-port-mode-cfg', True),
            _MetaInfoClassMember('if-port-mode', REFERENCE_ENUM_CLASS, 'HwModuleEpIfPortMode', 'Hw-module-ep-if-port-mode',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_ep_port_mode_cfg', 'HwModuleEpIfPortMode',
                [], [],
                '''                port-mode type
                ''',
                'if_port_mode',
                'Cisco-IOS-XR-asr9k-ep-port-mode-cfg', False),
            ],
            'Cisco-IOS-XR-asr9k-ep-port-mode-cfg',
            'port',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-asr9k-ep-port-mode-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_ep_port_mode_cfg',
        ),
    },
    'HwModuleEpPortMode.EpPortModeConfiguration.Node.Bays.Bay.Ports' : {
        'meta_info' : _MetaInfoClass('HwModuleEpPortMode.EpPortModeConfiguration.Node.Bays.Bay.Ports', REFERENCE_CLASS,
            '''port-mode configuration for port number''',
            False, 
            [
            _MetaInfoClassMember('port', REFERENCE_LIST, 'Port', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_ep_port_mode_cfg', 'HwModuleEpPortMode.EpPortModeConfiguration.Node.Bays.Bay.Ports.Port',
                [], [],
                '''                Optics port number
                ''',
                'port',
                'Cisco-IOS-XR-asr9k-ep-port-mode-cfg', False),
            ],
            'Cisco-IOS-XR-asr9k-ep-port-mode-cfg',
            'ports',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-asr9k-ep-port-mode-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_ep_port_mode_cfg',
        ),
    },
    'HwModuleEpPortMode.EpPortModeConfiguration.Node.Bays.Bay' : {
        'meta_info' : _MetaInfoClass('HwModuleEpPortMode.EpPortModeConfiguration.Node.Bays.Bay', REFERENCE_LIST,
            '''EP Bay number''',
            False, 
            [
            _MetaInfoClassMember('bay-number', ATTRIBUTE, 'str', 'xr:Cisco-ios-xr-string',
                None, None,
                [], [b'[\\w\\-\\.:,_@#%$\\+=\\|;]+'],
                '''                bay number
                ''',
                'bay_number',
                'Cisco-IOS-XR-asr9k-ep-port-mode-cfg', True),
            _MetaInfoClassMember('ports', REFERENCE_CLASS, 'Ports', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_ep_port_mode_cfg', 'HwModuleEpPortMode.EpPortModeConfiguration.Node.Bays.Bay.Ports',
                [], [],
                '''                port-mode configuration for port number
                ''',
                'ports',
                'Cisco-IOS-XR-asr9k-ep-port-mode-cfg', False),
            ],
            'Cisco-IOS-XR-asr9k-ep-port-mode-cfg',
            'bay',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-asr9k-ep-port-mode-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_ep_port_mode_cfg',
        ),
    },
    'HwModuleEpPortMode.EpPortModeConfiguration.Node.Bays' : {
        'meta_info' : _MetaInfoClass('HwModuleEpPortMode.EpPortModeConfiguration.Node.Bays', REFERENCE_CLASS,
            '''port-mode configuration for EP bay number''',
            False, 
            [
            _MetaInfoClassMember('bay', REFERENCE_LIST, 'Bay', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_ep_port_mode_cfg', 'HwModuleEpPortMode.EpPortModeConfiguration.Node.Bays.Bay',
                [], [],
                '''                EP Bay number
                ''',
                'bay',
                'Cisco-IOS-XR-asr9k-ep-port-mode-cfg', False),
            ],
            'Cisco-IOS-XR-asr9k-ep-port-mode-cfg',
            'bays',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-asr9k-ep-port-mode-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_ep_port_mode_cfg',
        ),
    },
    'HwModuleEpPortMode.EpPortModeConfiguration.Node' : {
        'meta_info' : _MetaInfoClass('HwModuleEpPortMode.EpPortModeConfiguration.Node', REFERENCE_LIST,
            '''line-card node location''',
            False, 
            [
            _MetaInfoClassMember('location', ATTRIBUTE, 'str', 'xr:Cisco-ios-xr-string',
                None, None,
                [], [b'[\\w\\-\\.:,_@#%$\\+=\\|;]+'],
                '''                Fully qualified line-card location
                ''',
                'location',
                'Cisco-IOS-XR-asr9k-ep-port-mode-cfg', True),
            _MetaInfoClassMember('bays', REFERENCE_CLASS, 'Bays', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_ep_port_mode_cfg', 'HwModuleEpPortMode.EpPortModeConfiguration.Node.Bays',
                [], [],
                '''                port-mode configuration for EP bay number
                ''',
                'bays',
                'Cisco-IOS-XR-asr9k-ep-port-mode-cfg', False),
            ],
            'Cisco-IOS-XR-asr9k-ep-port-mode-cfg',
            'node',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-asr9k-ep-port-mode-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_ep_port_mode_cfg',
        ),
    },
    'HwModuleEpPortMode.EpPortModeConfiguration' : {
        'meta_info' : _MetaInfoClass('HwModuleEpPortMode.EpPortModeConfiguration', REFERENCE_LIST,
            '''active or pre configuration''',
            False, 
            [
            _MetaInfoClassMember('active', ATTRIBUTE, 'str', 'xr:Cisco-ios-xr-string',
                None, None,
                [], [b'[\\w\\-\\.:,_@#%$\\+=\\|;]+'],
                '''                act or pre configuration
                ''',
                'active',
                'Cisco-IOS-XR-asr9k-ep-port-mode-cfg', True),
            _MetaInfoClassMember('node', REFERENCE_LIST, 'Node', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_ep_port_mode_cfg', 'HwModuleEpPortMode.EpPortModeConfiguration.Node',
                [], [],
                '''                line-card node location
                ''',
                'node',
                'Cisco-IOS-XR-asr9k-ep-port-mode-cfg', False),
            ],
            'Cisco-IOS-XR-asr9k-ep-port-mode-cfg',
            'ep-port-mode-configuration',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-asr9k-ep-port-mode-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_ep_port_mode_cfg',
        ),
    },
    'HwModuleEpPortMode' : {
        'meta_info' : _MetaInfoClass('HwModuleEpPortMode', REFERENCE_CLASS,
            '''HW Module EP port-mode configuration''',
            False, 
            [
            _MetaInfoClassMember('ep-port-mode-configuration', REFERENCE_LIST, 'EpPortModeConfiguration', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_ep_port_mode_cfg', 'HwModuleEpPortMode.EpPortModeConfiguration',
                [], [],
                '''                active or pre configuration
                ''',
                'ep_port_mode_configuration',
                'Cisco-IOS-XR-asr9k-ep-port-mode-cfg', False),
            ],
            'Cisco-IOS-XR-asr9k-ep-port-mode-cfg',
            'hw-module-ep-port-mode',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-asr9k-ep-port-mode-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_ep_port_mode_cfg',
        ),
    },
}
_meta_table['HwModuleEpPortMode.EpPortModeConfiguration.Node.Bays.Bay.Ports.Port']['meta_info'].parent =_meta_table['HwModuleEpPortMode.EpPortModeConfiguration.Node.Bays.Bay.Ports']['meta_info']
_meta_table['HwModuleEpPortMode.EpPortModeConfiguration.Node.Bays.Bay.Ports']['meta_info'].parent =_meta_table['HwModuleEpPortMode.EpPortModeConfiguration.Node.Bays.Bay']['meta_info']
_meta_table['HwModuleEpPortMode.EpPortModeConfiguration.Node.Bays.Bay']['meta_info'].parent =_meta_table['HwModuleEpPortMode.EpPortModeConfiguration.Node.Bays']['meta_info']
_meta_table['HwModuleEpPortMode.EpPortModeConfiguration.Node.Bays']['meta_info'].parent =_meta_table['HwModuleEpPortMode.EpPortModeConfiguration.Node']['meta_info']
_meta_table['HwModuleEpPortMode.EpPortModeConfiguration.Node']['meta_info'].parent =_meta_table['HwModuleEpPortMode.EpPortModeConfiguration']['meta_info']
_meta_table['HwModuleEpPortMode.EpPortModeConfiguration']['meta_info'].parent =_meta_table['HwModuleEpPortMode']['meta_info']
