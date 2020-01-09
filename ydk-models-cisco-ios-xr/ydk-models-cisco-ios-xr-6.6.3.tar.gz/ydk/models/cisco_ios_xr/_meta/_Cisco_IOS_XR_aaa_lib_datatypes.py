
'''
This is auto-generated file,
which includes metadata for module Cisco_IOS_XR_aaa_lib_datatypes
'''

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_LIST, REFERENCE_LEAFLIST, REFERENCE_BITS, REFERENCE_UNION
from ydk._core._dm_meta_info import REFERENCE_CLASS, REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, ANYXML_CLASS
from ydk._core._importer import _yang_ns

_meta_table = {
    'AaaAccounting' : _MetaInfoEnum('AaaAccounting',
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_datatypes', 'AaaAccounting',
        '''Aaa accounting''',
        {
            'not-set':'not_set',
            'start-stop':'start_stop',
            'stop-only':'stop_only',
        }, 'Cisco-IOS-XR-aaa-lib-datatypes', _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-aaa-lib-datatypes']),
    'AaaAccountingRpFailover' : _MetaInfoEnum('AaaAccountingRpFailover',
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_datatypes', 'AaaAccountingRpFailover',
        '''Aaa accounting rp failover''',
        {
            'disable':'disable',
            'enable':'enable',
        }, 'Cisco-IOS-XR-aaa-lib-datatypes', _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-aaa-lib-datatypes']),
    'AaaAccountingBroadcast' : _MetaInfoEnum('AaaAccountingBroadcast',
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_datatypes', 'AaaAccountingBroadcast',
        '''Aaa accounting broadcast''',
        {
            'disable':'disable',
            'enable':'enable',
        }, 'Cisco-IOS-XR-aaa-lib-datatypes', _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-aaa-lib-datatypes']),
    'AaaMethodAccounting' : _MetaInfoEnum('AaaMethodAccounting',
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_datatypes', 'AaaMethodAccounting',
        '''Aaa method accounting''',
        {
            'not-set':'not_set',
            'none':'none',
            'radius':'radius',
            'tacacs-plus':'tacacs_plus',
            'dsmd':'dsmd',
            'sgbp':'sgbp',
            'acct-d':'acct_d',
            'error':'error',
            'if-authenticated':'if_authenticated',
            'server-group':'server_group',
            'server-group-not-defined':'server_group_not_defined',
            'line':'line',
            'enable':'enable',
            'kerberos':'kerberos',
            'diameter':'diameter',
            'last':'last',
            'local':'local',
        }, 'Cisco-IOS-XR-aaa-lib-datatypes', _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-aaa-lib-datatypes']),
    'AaaMethod' : _MetaInfoEnum('AaaMethod',
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_datatypes', 'AaaMethod',
        '''Aaa method''',
        {
            'not-set':'not_set',
            'none':'none',
            'local':'local',
            'radius':'radius',
            'tacacs-plus':'tacacs_plus',
            'dsmd':'dsmd',
            'sgbp':'sgbp',
            'acct-d':'acct_d',
            'error':'error',
            'if-authenticated':'if_authenticated',
            'server-group':'server_group',
            'server-group-not-defined':'server_group_not_defined',
            'line':'line',
            'enable':'enable',
            'kerberos':'kerberos',
            'diameter':'diameter',
            'last':'last',
        }, 'Cisco-IOS-XR-aaa-lib-datatypes', _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-aaa-lib-datatypes']),
    'AaaAccountingUpdate' : _MetaInfoEnum('AaaAccountingUpdate',
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_datatypes', 'AaaAccountingUpdate',
        '''Aaa accounting update''',
        {
            'none':'none',
            'newinfo':'newinfo',
            'periodic':'periodic',
        }, 'Cisco-IOS-XR-aaa-lib-datatypes', _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-aaa-lib-datatypes']),
}
