
'''
This is auto-generated file,
which includes metadata for module Cisco_IOS_XR_invmgr_cfg
'''

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_LIST, REFERENCE_LEAFLIST, REFERENCE_BITS, REFERENCE_UNION
from ydk._core._dm_meta_info import REFERENCE_CLASS, REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, ANYXML_CLASS
from ydk._core._importer import _yang_ns

_meta_table = {
    'InventoryConfigurations.Entity' : {
        'meta_info' : _MetaInfoClass('InventoryConfigurations.Entity', REFERENCE_LIST,
            '''Entity name''',
            False, 
            [
            _MetaInfoClassMember('name', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                Entity name
                ''',
                'name',
                'Cisco-IOS-XR-invmgr-cfg', True),
            _MetaInfoClassMember('name-xr', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                Entity name
                ''',
                'name_xr',
                'Cisco-IOS-XR-invmgr-cfg', False, is_mandatory=True),
            ],
            'Cisco-IOS-XR-invmgr-cfg',
            'entity',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-invmgr-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_invmgr_cfg',
        ),
    },
    'InventoryConfigurations' : {
        'meta_info' : _MetaInfoClass('InventoryConfigurations', REFERENCE_CLASS,
            '''Configuration for inventory entities''',
            False, 
            [
            _MetaInfoClassMember('entity', REFERENCE_LIST, 'Entity', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_invmgr_cfg', 'InventoryConfigurations.Entity',
                [], [],
                '''                Entity name
                ''',
                'entity_',
                'Cisco-IOS-XR-invmgr-cfg', False),
            ],
            'Cisco-IOS-XR-invmgr-cfg',
            'inventory-configurations',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-invmgr-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_invmgr_cfg',
        ),
    },
}
_meta_table['InventoryConfigurations.Entity']['meta_info'].parent =_meta_table['InventoryConfigurations']['meta_info']
