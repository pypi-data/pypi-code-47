
'''
This is auto-generated file,
which includes metadata for module Cisco_IOS_XR_config_cfgmgr_cfg
'''

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_LIST, REFERENCE_LEAFLIST, REFERENCE_BITS, REFERENCE_UNION
from ydk._core._dm_meta_info import REFERENCE_CLASS, REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, ANYXML_CLASS
from ydk._core._importer import _yang_ns

_meta_table = {
    'Cfgmgr' : {
        'meta_info' : _MetaInfoClass('Cfgmgr', REFERENCE_CLASS,
            '''Cfgmgr configuration''',
            False, 
            [
            _MetaInfoClassMember('mode-exclusive', ATTRIBUTE, 'bool', 'boolean',
                None, None,
                [], [],
                '''                Enabled or Disabled
                ''',
                'mode_exclusive',
                'Cisco-IOS-XR-config-cfgmgr-cfg', False, default_value='True'),
            ],
            'Cisco-IOS-XR-config-cfgmgr-cfg',
            'cfgmgr',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-config-cfgmgr-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_config_cfgmgr_cfg',
        ),
    },
}
