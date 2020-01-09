
'''
This is auto-generated file,
which includes metadata for module SNMP_FRAMEWORK_MIB
'''

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_LIST, REFERENCE_LEAFLIST, REFERENCE_BITS, REFERENCE_UNION
from ydk._core._dm_meta_info import REFERENCE_CLASS, REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, ANYXML_CLASS
from ydk._core._importer import _yang_ns

_meta_table = {
    'SnmpSecurityLevel' : _MetaInfoEnum('SnmpSecurityLevel',
        'ydk.models.cisco_ios_xr.SNMP_FRAMEWORK_MIB', 'SnmpSecurityLevel',
        ''' ''',
        {
            'noAuthNoPriv':'noAuthNoPriv',
            'authNoPriv':'authNoPriv',
            'authPriv':'authPriv',
        }, 'SNMP-FRAMEWORK-MIB', _yang_ns.NAMESPACE_LOOKUP['SNMP-FRAMEWORK-MIB']),
    'SNMPFRAMEWORKMIB.SnmpEngine' : {
        'meta_info' : _MetaInfoClass('SNMPFRAMEWORKMIB.SnmpEngine', REFERENCE_CLASS,
            ''' ''',
            False, 
            [
            _MetaInfoClassMember('snmpEngineID', ATTRIBUTE, 'str', 'SnmpEngineID',
                None, None,
                [], [b'(([0-9a-fA-F]){2}(:([0-9a-fA-F]){2})*)?'],
                '''                ''',
                'snmpengineid',
                'SNMP-FRAMEWORK-MIB', False, is_config=False),
            _MetaInfoClassMember('snmpEngineBoots', ATTRIBUTE, 'int', 'snmpEngineBootsType',
                None, None,
                [('1', '2147483647')], [],
                '''                ''',
                'snmpengineboots',
                'SNMP-FRAMEWORK-MIB', False, is_config=False),
            _MetaInfoClassMember('snmpEngineTime', ATTRIBUTE, 'int', 'snmpEngineTimeType',
                None, None,
                [('0', '2147483647')], [],
                '''                ''',
                'snmpenginetime',
                'SNMP-FRAMEWORK-MIB', False, is_config=False),
            _MetaInfoClassMember('snmpEngineMaxMessageSize', ATTRIBUTE, 'int', 'snmpEngineMaxMessageSizeType',
                None, None,
                [('484', '2147483647')], [],
                '''                ''',
                'snmpenginemaxmessagesize',
                'SNMP-FRAMEWORK-MIB', False, is_config=False),
            ],
            'SNMP-FRAMEWORK-MIB',
            'snmpEngine',
            _yang_ns.NAMESPACE_LOOKUP['SNMP-FRAMEWORK-MIB'],
            'ydk.models.cisco_ios_xr.SNMP_FRAMEWORK_MIB',
            is_config=False,
        ),
    },
    'SNMPFRAMEWORKMIB' : {
        'meta_info' : _MetaInfoClass('SNMPFRAMEWORKMIB', REFERENCE_CLASS,
            ''' ''',
            False, 
            [
            _MetaInfoClassMember('snmpEngine', REFERENCE_CLASS, 'SnmpEngine', '',
                'ydk.models.cisco_ios_xr.SNMP_FRAMEWORK_MIB', 'SNMPFRAMEWORKMIB.SnmpEngine',
                [], [],
                '''                ''',
                'snmpengine',
                'SNMP-FRAMEWORK-MIB', False, is_config=False),
            ],
            'SNMP-FRAMEWORK-MIB',
            'SNMP-FRAMEWORK-MIB',
            _yang_ns.NAMESPACE_LOOKUP['SNMP-FRAMEWORK-MIB'],
            'ydk.models.cisco_ios_xr.SNMP_FRAMEWORK_MIB',
            is_config=False,
        ),
    },
}
_meta_table['SNMPFRAMEWORKMIB.SnmpEngine']['meta_info'].parent =_meta_table['SNMPFRAMEWORKMIB']['meta_info']
