
'''
This is auto-generated file,
which includes metadata for module Cisco_IOS_XR_asr9k_lc_pwrglide_cfg
'''

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_LIST, REFERENCE_LEAFLIST, REFERENCE_BITS, REFERENCE_UNION
from ydk._core._dm_meta_info import REFERENCE_CLASS, REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, ANYXML_CLASS
from ydk._core._importer import _yang_ns

_meta_table = {
    'HardwareModulePortMode.ConfigMode.Node.PortMode' : {
        'meta_info' : _MetaInfoClass('HardwareModulePortMode.ConfigMode.Node.PortMode', REFERENCE_CLASS,
            '''Linecard port-mode''',
            False, 
            [
            _MetaInfoClassMember('if-port-mode', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                Linecard interface port-mode
                ''',
                'if_port_mode',
                'Cisco-IOS-XR-asr9k-lc-pwrglide-cfg', False),
            ],
            'Cisco-IOS-XR-asr9k-lc-pwrglide-cfg',
            'port-mode',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-asr9k-lc-pwrglide-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_lc_pwrglide_cfg',
        ),
    },
    'HardwareModulePortMode.ConfigMode.Node' : {
        'meta_info' : _MetaInfoClass('HardwareModulePortMode.ConfigMode.Node', REFERENCE_LIST,
            '''A node''',
            False, 
            [
            _MetaInfoClassMember('id2', ATTRIBUTE, 'str', 'xr:Cisco-ios-xr-string',
                None, None,
                [], [b'[\\w\\-\\.:,_@#%$\\+=\\|;]+'],
                '''                Fully qualified line card specification
                ''',
                'id2',
                'Cisco-IOS-XR-asr9k-lc-pwrglide-cfg', True),
            _MetaInfoClassMember('port-mode', REFERENCE_CLASS, 'PortMode', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_lc_pwrglide_cfg', 'HardwareModulePortMode.ConfigMode.Node.PortMode',
                [], [],
                '''                Linecard port-mode
                ''',
                'port_mode',
                'Cisco-IOS-XR-asr9k-lc-pwrglide-cfg', False),
            ],
            'Cisco-IOS-XR-asr9k-lc-pwrglide-cfg',
            'node',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-asr9k-lc-pwrglide-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_lc_pwrglide_cfg',
        ),
    },
    'HardwareModulePortMode.ConfigMode' : {
        'meta_info' : _MetaInfoClass('HardwareModulePortMode.ConfigMode', REFERENCE_LIST,
            '''Active or Pre configuration''',
            False, 
            [
            _MetaInfoClassMember('id1', ATTRIBUTE, 'str', 'xr:Cisco-ios-xr-string',
                None, None,
                [], [b'[\\w\\-\\.:,_@#%$\\+=\\|;]+'],
                '''                act- or pre-config
                ''',
                'id1',
                'Cisco-IOS-XR-asr9k-lc-pwrglide-cfg', True),
            _MetaInfoClassMember('node', REFERENCE_LIST, 'Node', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_lc_pwrglide_cfg', 'HardwareModulePortMode.ConfigMode.Node',
                [], [],
                '''                A node
                ''',
                'node',
                'Cisco-IOS-XR-asr9k-lc-pwrglide-cfg', False),
            ],
            'Cisco-IOS-XR-asr9k-lc-pwrglide-cfg',
            'config-mode',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-asr9k-lc-pwrglide-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_lc_pwrglide_cfg',
        ),
    },
    'HardwareModulePortMode' : {
        'meta_info' : _MetaInfoClass('HardwareModulePortMode', REFERENCE_CLASS,
            '''HW module port-mode config''',
            False, 
            [
            _MetaInfoClassMember('config-mode', REFERENCE_LIST, 'ConfigMode', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_lc_pwrglide_cfg', 'HardwareModulePortMode.ConfigMode',
                [], [],
                '''                Active or Pre configuration
                ''',
                'config_mode',
                'Cisco-IOS-XR-asr9k-lc-pwrglide-cfg', False),
            ],
            'Cisco-IOS-XR-asr9k-lc-pwrglide-cfg',
            'hardware-module-port-mode',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-asr9k-lc-pwrglide-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_lc_pwrglide_cfg',
        ),
    },
}
_meta_table['HardwareModulePortMode.ConfigMode.Node.PortMode']['meta_info'].parent =_meta_table['HardwareModulePortMode.ConfigMode.Node']['meta_info']
_meta_table['HardwareModulePortMode.ConfigMode.Node']['meta_info'].parent =_meta_table['HardwareModulePortMode.ConfigMode']['meta_info']
_meta_table['HardwareModulePortMode.ConfigMode']['meta_info'].parent =_meta_table['HardwareModulePortMode']['meta_info']
