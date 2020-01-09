
'''
This is auto-generated file,
which includes metadata for module Cisco_IOS_XR_sysadmin_types
'''

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_LIST, REFERENCE_LEAFLIST, REFERENCE_BITS, REFERENCE_UNION
from ydk._core._dm_meta_info import REFERENCE_CLASS, REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, ANYXML_CLASS
from ydk._core._importer import _yang_ns

_meta_table = {
    'RackId' : _MetaInfoEnum('RackId',
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_types', 'RackId',
        '''Identifies the rack number of FCC/LCC.
LCC racks are identified by numbers rack0..7
FCC racks are identified by numbers F0..F3
BSC racks are identified by numbers 128..129''',
        {
            'L0':'L0',
            'L1':'L1',
            'L2':'L2',
            'L3':'L3',
            'L4':'L4',
            'L5':'L5',
            'L6':'L6',
            'L7':'L7',
            'L8':'L8',
            'L9':'L9',
            'L10':'L10',
            'L11':'L11',
            'L12':'L12',
            'L13':'L13',
            'L14':'L14',
            'L15':'L15',
            'F0':'F0',
            'F1':'F1',
            'F2':'F2',
            'F3':'F3',
            'B0':'B0',
            'B1':'B1',
        }, 'Cisco-IOS-XR-sysadmin-types', _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-sysadmin-types']),
    'Adminstate' : _MetaInfoEnum('Adminstate',
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_types', 'Adminstate',
        ''' ''',
        {
            'disable':'disable',
        }, 'Cisco-IOS-XR-sysadmin-types', _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-sysadmin-types']),
    'GenericOperStatus' : _MetaInfoEnum('GenericOperStatus',
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_types', 'GenericOperStatus',
        ''' ''',
        {
            'up':'up',
            'down':'down',
        }, 'Cisco-IOS-XR-sysadmin-types', _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-sysadmin-types']),
    'GenericOperStatus_' : _MetaInfoEnum('GenericOperStatus_',
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_types', 'GenericOperStatus_',
        ''' ''',
        {
            'up':'up',
            'down':'down',
        }, 'Cisco-IOS-XR-sysadmin-types', _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-sysadmin-types']),
    'GenericOperStatus__' : _MetaInfoEnum('GenericOperStatus__',
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_types', 'GenericOperStatus__',
        ''' ''',
        {
            'up':'up',
            'down':'down',
        }, 'Cisco-IOS-XR-sysadmin-types', _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-sysadmin-types']),
    'GenericHaRole' : _MetaInfoEnum('GenericHaRole',
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_types', 'GenericHaRole',
        ''' ''',
        {
            'no-ha-role':'no_ha_role',
            'Active':'Active',
            'Standby':'Standby',
        }, 'Cisco-IOS-XR-sysadmin-types', _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-sysadmin-types']),
    'FabricLinkTypes' : _MetaInfoEnum('FabricLinkTypes',
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_types', 'FabricLinkTypes',
        ''' ''',
        {
            'S1':'S1',
            'S2':'S2',
            'S3':'S3',
        }, 'Cisco-IOS-XR-sysadmin-types', _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-sysadmin-types']),
}
