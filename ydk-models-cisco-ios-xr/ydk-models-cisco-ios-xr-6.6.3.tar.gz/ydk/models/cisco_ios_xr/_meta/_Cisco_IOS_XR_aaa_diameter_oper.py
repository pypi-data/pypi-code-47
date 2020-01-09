
'''
This is auto-generated file,
which includes metadata for module Cisco_IOS_XR_aaa_diameter_oper
'''

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_LIST, REFERENCE_LEAFLIST, REFERENCE_BITS, REFERENCE_UNION
from ydk._core._dm_meta_info import REFERENCE_CLASS, REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, ANYXML_CLASS
from ydk._core._importer import _yang_ns

_meta_table = {
    'PeerStateValue' : _MetaInfoEnum('PeerStateValue',
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_diameter_oper', 'PeerStateValue',
        '''Peer State Values''',
        {
            'state-none':'state_none',
            'closed':'closed',
            'wait-connection-ack':'wait_connection_ack',
            'wait-cea':'wait_cea',
            'state-open':'state_open',
            'closing':'closing',
            'suspect':'suspect',
        }, 'Cisco-IOS-XR-aaa-diameter-oper', _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-aaa-diameter-oper']),
    'WhoInitiatedDisconnect' : _MetaInfoEnum('WhoInitiatedDisconnect',
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_diameter_oper', 'WhoInitiatedDisconnect',
        '''Who initiated to disconnect''',
        {
            'none':'none',
            'host':'host',
            'peer':'peer',
        }, 'Cisco-IOS-XR-aaa-diameter-oper', _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-aaa-diameter-oper']),
    'DisconnectCause' : _MetaInfoEnum('DisconnectCause',
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_diameter_oper', 'DisconnectCause',
        '''Disconnect cause values''',
        {
            'reboot':'reboot',
            'busy':'busy',
            'do-not-wait-to-talk':'do_not_wait_to_talk',
        }, 'Cisco-IOS-XR-aaa-diameter-oper', _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-aaa-diameter-oper']),
    'Peer' : _MetaInfoEnum('Peer',
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_diameter_oper', 'Peer',
        ''' Peer type values''',
        {
            'undefined':'undefined',
            'server':'server',
        }, 'Cisco-IOS-XR-aaa-diameter-oper', _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-aaa-diameter-oper']),
    'SecurityTypeValue' : _MetaInfoEnum('SecurityTypeValue',
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_diameter_oper', 'SecurityTypeValue',
        '''Security type values''',
        {
            'security-type-none':'security_type_none',
            'type':'type',
            'ipsec':'ipsec',
        }, 'Cisco-IOS-XR-aaa-diameter-oper', _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-aaa-diameter-oper']),
    'ProtocolTypeValue' : _MetaInfoEnum('ProtocolTypeValue',
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_diameter_oper', 'ProtocolTypeValue',
        '''Protocol type values''',
        {
            'protocol-none':'protocol_none',
            'tcp':'tcp',
        }, 'Cisco-IOS-XR-aaa-diameter-oper', _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-aaa-diameter-oper']),
}
