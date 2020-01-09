
'''
This is auto-generated file,
which includes metadata for module Cisco_IOS_XR_aaa_protocol_radius_cfg
'''

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_LIST, REFERENCE_LEAFLIST, REFERENCE_BITS, REFERENCE_UNION
from ydk._core._dm_meta_info import REFERENCE_CLASS, REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, ANYXML_CLASS
from ydk._core._importer import _yang_ns

_meta_table = {
    'AaaDscpValue' : _MetaInfoEnum('AaaDscpValue',
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_protocol_radius_cfg', 'AaaDscpValue',
        ''' ''',
        {
            'af11':'af11',
            'af12':'af12',
            'af13':'af13',
            'af21':'af21',
            'af22':'af22',
            'af23':'af23',
            'af31':'af31',
            'af32':'af32',
            'af33':'af33',
            'af41':'af41',
            'af42':'af42',
            'af43':'af43',
            'cs1':'cs1',
            'cs2':'cs2',
            'cs3':'cs3',
            'cs4':'cs4',
            'cs5':'cs5',
            'cs6':'cs6',
            'cs7':'cs7',
            'default':'default',
            'ef':'ef',
        }, 'Cisco-IOS-XR-aaa-protocol-radius-cfg', _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-aaa-protocol-radius-cfg']),
    'AaaAction' : _MetaInfoEnum('AaaAction',
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_protocol_radius_cfg', 'AaaAction',
        '''Aaa action''',
        {
            'accept':'accept',
            'reject':'reject',
        }, 'Cisco-IOS-XR-aaa-protocol-radius-cfg', _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-aaa-protocol-radius-cfg']),
    'AaaAuthentication' : _MetaInfoEnum('AaaAuthentication',
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_protocol_radius_cfg', 'AaaAuthentication',
        '''Aaa authentication''',
        {
            'all':'all',
            'any':'any',
            'session-key':'session_key',
        }, 'Cisco-IOS-XR-aaa-protocol-radius-cfg', _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-aaa-protocol-radius-cfg']),
    'AaaSelectKey' : _MetaInfoEnum('AaaSelectKey',
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_protocol_radius_cfg', 'AaaSelectKey',
        '''Aaa select key''',
        {
            'server-key':'server_key',
            'session-key':'session_key',
        }, 'Cisco-IOS-XR-aaa-protocol-radius-cfg', _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-aaa-protocol-radius-cfg']),
    'AaaDirection' : _MetaInfoEnum('AaaDirection',
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_protocol_radius_cfg', 'AaaDirection',
        '''Aaa direction''',
        {
            'inbound':'inbound',
            'outbound':'outbound',
        }, 'Cisco-IOS-XR-aaa-protocol-radius-cfg', _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-aaa-protocol-radius-cfg']),
    'AaaConfig' : _MetaInfoEnum('AaaConfig',
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_protocol_radius_cfg', 'AaaConfig',
        '''Aaa config''',
        {
            'false':'false',
            'true':'true',
        }, 'Cisco-IOS-XR-aaa-protocol-radius-cfg', _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-aaa-protocol-radius-cfg']),
}
