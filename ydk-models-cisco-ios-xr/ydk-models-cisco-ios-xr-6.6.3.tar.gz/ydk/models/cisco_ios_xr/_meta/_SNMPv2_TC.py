
'''
This is auto-generated file,
which includes metadata for module SNMPv2_TC
'''

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_LIST, REFERENCE_LEAFLIST, REFERENCE_BITS, REFERENCE_UNION
from ydk._core._dm_meta_info import REFERENCE_CLASS, REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, ANYXML_CLASS
from ydk._core._importer import _yang_ns

_meta_table = {
    'TruthValue' : _MetaInfoEnum('TruthValue',
        'ydk.models.cisco_ios_xr.SNMPv2_TC', 'TruthValue',
        ''' ''',
        {
            'true':'true',
            'false':'false',
        }, 'SNMPv2-TC', _yang_ns.NAMESPACE_LOOKUP['SNMPv2-TC']),
    'RowStatus' : _MetaInfoEnum('RowStatus',
        'ydk.models.cisco_ios_xr.SNMPv2_TC', 'RowStatus',
        ''' ''',
        {
            'active':'active',
            'notInService':'notInService',
            'notReady':'notReady',
            'createAndGo':'createAndGo',
            'createAndWait':'createAndWait',
            'destroy':'destroy',
        }, 'SNMPv2-TC', _yang_ns.NAMESPACE_LOOKUP['SNMPv2-TC']),
    'StorageType' : _MetaInfoEnum('StorageType',
        'ydk.models.cisco_ios_xr.SNMPv2_TC', 'StorageType',
        ''' ''',
        {
            'other':'other',
            'volatile':'volatile',
            'nonVolatile':'nonVolatile',
            'permanent':'permanent',
            'readOnly':'readOnly',
        }, 'SNMPv2-TC', _yang_ns.NAMESPACE_LOOKUP['SNMPv2-TC']),
}
