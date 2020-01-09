
'''
This is auto-generated file,
which includes metadata for module Cisco_IOS_XR_sysadmin_entity_state_tc_mib
'''

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_LIST, REFERENCE_LEAFLIST, REFERENCE_BITS, REFERENCE_UNION
from ydk._core._dm_meta_info import REFERENCE_CLASS, REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, ANYXML_CLASS
from ydk._core._importer import _yang_ns

_meta_table = {
    'EntityAdminState' : _MetaInfoEnum('EntityAdminState',
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_entity_state_tc_mib', 'EntityAdminState',
        ''' ''',
        {
            'unknown':'unknown',
            'locked':'locked',
            'shuttingDown':'shuttingDown',
            'unlocked':'unlocked',
        }, 'Cisco-IOS-XR-sysadmin-entity-state-tc-mib', _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-sysadmin-entity-state-tc-mib']),
    'EntityOperState' : _MetaInfoEnum('EntityOperState',
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_entity_state_tc_mib', 'EntityOperState',
        ''' ''',
        {
            'unknown':'unknown',
            'disabled':'disabled',
            'enabled':'enabled',
            'testing':'testing',
        }, 'Cisco-IOS-XR-sysadmin-entity-state-tc-mib', _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-sysadmin-entity-state-tc-mib']),
    'EntityUsageState' : _MetaInfoEnum('EntityUsageState',
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_entity_state_tc_mib', 'EntityUsageState',
        ''' ''',
        {
            'unknown':'unknown',
            'idle':'idle',
            'active':'active',
            'busy':'busy',
        }, 'Cisco-IOS-XR-sysadmin-entity-state-tc-mib', _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-sysadmin-entity-state-tc-mib']),
    'EntityStandbyStatus' : _MetaInfoEnum('EntityStandbyStatus',
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_entity_state_tc_mib', 'EntityStandbyStatus',
        ''' ''',
        {
            'unknown':'unknown',
            'hotStandby':'hotStandby',
            'coldStandby':'coldStandby',
            'providingService':'providingService',
        }, 'Cisco-IOS-XR-sysadmin-entity-state-tc-mib', _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-sysadmin-entity-state-tc-mib']),
}
