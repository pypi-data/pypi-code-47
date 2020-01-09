
'''
This is auto-generated file,
which includes metadata for module Cisco_IOS_XR_hwmod_bcc_disable_cfg
'''

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_LIST, REFERENCE_LEAFLIST, REFERENCE_BITS, REFERENCE_UNION
from ydk._core._dm_meta_info import REFERENCE_CLASS, REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, ANYXML_CLASS
from ydk._core._importer import _yang_ns

_meta_table = {
    'HardwareModuleBccDisable.Bcc.Node.All' : {
        'meta_info' : _MetaInfoClass('HardwareModuleBccDisable.Bcc.Node.All', REFERENCE_CLASS,
            '''all node configuration''',
            False, 
            [
            _MetaInfoClassMember('disable', ATTRIBUTE, 'Empty', 'empty',
                None, None,
                [], [],
                '''                bcc disable config
                ''',
                'disable',
                'Cisco-IOS-XR-hwmod-bcc-disable-cfg', False),
            ],
            'Cisco-IOS-XR-hwmod-bcc-disable-cfg',
            'all',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-hwmod-bcc-disable-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_hwmod_bcc_disable_cfg',
        ),
    },
    'HardwareModuleBccDisable.Bcc.Node' : {
        'meta_info' : _MetaInfoClass('HardwareModuleBccDisable.Bcc.Node', REFERENCE_CLASS,
            '''Node''',
            False, 
            [
            _MetaInfoClassMember('all', REFERENCE_CLASS, 'All', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_hwmod_bcc_disable_cfg', 'HardwareModuleBccDisable.Bcc.Node.All',
                [], [],
                '''                all node configuration
                ''',
                'all',
                'Cisco-IOS-XR-hwmod-bcc-disable-cfg', False),
            ],
            'Cisco-IOS-XR-hwmod-bcc-disable-cfg',
            'node',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-hwmod-bcc-disable-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_hwmod_bcc_disable_cfg',
        ),
    },
    'HardwareModuleBccDisable.Bcc' : {
        'meta_info' : _MetaInfoClass('HardwareModuleBccDisable.Bcc', REFERENCE_CLASS,
            '''bundle configuration''',
            False, 
            [
            _MetaInfoClassMember('node', REFERENCE_CLASS, 'Node', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_hwmod_bcc_disable_cfg', 'HardwareModuleBccDisable.Bcc.Node',
                [], [],
                '''                Node
                ''',
                'node',
                'Cisco-IOS-XR-hwmod-bcc-disable-cfg', False),
            ],
            'Cisco-IOS-XR-hwmod-bcc-disable-cfg',
            'bcc',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-hwmod-bcc-disable-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_hwmod_bcc_disable_cfg',
        ),
    },
    'HardwareModuleBccDisable' : {
        'meta_info' : _MetaInfoClass('HardwareModuleBccDisable', REFERENCE_CLASS,
            '''HW module BCC Disable config''',
            False, 
            [
            _MetaInfoClassMember('bcc', REFERENCE_CLASS, 'Bcc', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_hwmod_bcc_disable_cfg', 'HardwareModuleBccDisable.Bcc',
                [], [],
                '''                bundle configuration
                ''',
                'bcc',
                'Cisco-IOS-XR-hwmod-bcc-disable-cfg', False),
            ],
            'Cisco-IOS-XR-hwmod-bcc-disable-cfg',
            'hardware-module-bcc-disable',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-hwmod-bcc-disable-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_hwmod_bcc_disable_cfg',
        ),
    },
}
_meta_table['HardwareModuleBccDisable.Bcc.Node.All']['meta_info'].parent =_meta_table['HardwareModuleBccDisable.Bcc.Node']['meta_info']
_meta_table['HardwareModuleBccDisable.Bcc.Node']['meta_info'].parent =_meta_table['HardwareModuleBccDisable.Bcc']['meta_info']
_meta_table['HardwareModuleBccDisable.Bcc']['meta_info'].parent =_meta_table['HardwareModuleBccDisable']['meta_info']
