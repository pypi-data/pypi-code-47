
'''
This is auto-generated file,
which includes metadata for module SNMP_MPD_MIB
'''

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_LIST, REFERENCE_LEAFLIST, REFERENCE_BITS, REFERENCE_UNION
from ydk._core._dm_meta_info import REFERENCE_CLASS, REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, ANYXML_CLASS
from ydk._core._importer import _yang_ns

_meta_table = {
    'SNMPMPDMIB.SnmpMPDStats' : {
        'meta_info' : _MetaInfoClass('SNMPMPDMIB.SnmpMPDStats', REFERENCE_CLASS,
            ''' ''',
            False, 
            [
            _MetaInfoClassMember('snmpUnknownSecurityModels', ATTRIBUTE, 'int', 'yang:counter32',
                None, None,
                [('0', '4294967295')], [],
                '''                ''',
                'snmpunknownsecuritymodels',
                'SNMP-MPD-MIB', False, is_config=False),
            _MetaInfoClassMember('snmpInvalidMsgs', ATTRIBUTE, 'int', 'yang:counter32',
                None, None,
                [('0', '4294967295')], [],
                '''                ''',
                'snmpinvalidmsgs',
                'SNMP-MPD-MIB', False, is_config=False),
            _MetaInfoClassMember('snmpUnknownPDUHandlers', ATTRIBUTE, 'int', 'yang:counter32',
                None, None,
                [('0', '4294967295')], [],
                '''                ''',
                'snmpunknownpduhandlers',
                'SNMP-MPD-MIB', False, is_config=False),
            ],
            'SNMP-MPD-MIB',
            'snmpMPDStats',
            _yang_ns.NAMESPACE_LOOKUP['SNMP-MPD-MIB'],
            'ydk.models.cisco_ios_xr.SNMP_MPD_MIB',
            is_config=False,
        ),
    },
    'SNMPMPDMIB' : {
        'meta_info' : _MetaInfoClass('SNMPMPDMIB', REFERENCE_CLASS,
            ''' ''',
            False, 
            [
            _MetaInfoClassMember('snmpMPDStats', REFERENCE_CLASS, 'SnmpMPDStats', '',
                'ydk.models.cisco_ios_xr.SNMP_MPD_MIB', 'SNMPMPDMIB.SnmpMPDStats',
                [], [],
                '''                ''',
                'snmpmpdstats',
                'SNMP-MPD-MIB', False, is_config=False),
            ],
            'SNMP-MPD-MIB',
            'SNMP-MPD-MIB',
            _yang_ns.NAMESPACE_LOOKUP['SNMP-MPD-MIB'],
            'ydk.models.cisco_ios_xr.SNMP_MPD_MIB',
            is_config=False,
        ),
    },
}
_meta_table['SNMPMPDMIB.SnmpMPDStats']['meta_info'].parent =_meta_table['SNMPMPDMIB']['meta_info']
