
'''
This is auto-generated file,
which includes metadata for module Cisco_IOS_XR_Ethernet_SPAN_cfg
'''

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_LIST, REFERENCE_LEAFLIST, REFERENCE_BITS, REFERENCE_UNION
from ydk._core._dm_meta_info import REFERENCE_CLASS, REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, ANYXML_CLASS
from ydk._core._importer import _yang_ns

_meta_table = {
    'SpanTrafficDirection' : _MetaInfoEnum('SpanTrafficDirection',
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_Ethernet_SPAN_cfg', 'SpanTrafficDirection',
        '''Span traffic direction''',
        {
            'rx-only':'rx_only',
            'tx-only':'tx_only',
        }, 'Cisco-IOS-XR-Ethernet-SPAN-cfg', _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-Ethernet-SPAN-cfg']),
    'SpanMirrorInterval' : _MetaInfoEnum('SpanMirrorInterval',
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_Ethernet_SPAN_cfg', 'SpanMirrorInterval',
        '''Span mirror interval''',
        {
            '512':'Y_512',
            '1k':'Y_1k',
            '2k':'Y_2k',
            '4k':'Y_4k',
            '8k':'Y_8k',
            '16k':'Y_16k',
        }, 'Cisco-IOS-XR-Ethernet-SPAN-cfg', _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-Ethernet-SPAN-cfg']),
    'SpanDestination' : _MetaInfoEnum('SpanDestination',
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_Ethernet_SPAN_cfg', 'SpanDestination',
        '''Span destination''',
        {
            'interface':'interface',
            'pseudowire':'pseudowire',
            'ipv4-address':'ipv4_address',
            'ipv6-address':'ipv6_address',
        }, 'Cisco-IOS-XR-Ethernet-SPAN-cfg', _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-Ethernet-SPAN-cfg']),
    'SpanMonitorSession.Sessions.Session.Destination' : {
        'meta_info' : _MetaInfoClass('SpanMonitorSession.Sessions.Session.Destination', REFERENCE_CLASS,
            '''Specify a destination''',
            False, 
            [
            _MetaInfoClassMember('destination-type', REFERENCE_ENUM_CLASS, 'SpanDestination', 'Span-destination',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_Ethernet_SPAN_cfg', 'SpanDestination',
                [], [],
                '''                Specify the type of destination
                ''',
                'destination_type',
                'Cisco-IOS-XR-Ethernet-SPAN-cfg', False),
            _MetaInfoClassMember('destination-interface-name', ATTRIBUTE, 'str', 'xr:Interface-name',
                None, None,
                [], [b'[a-zA-Z0-9._/-]+'],
                '''                Specify the destination interface name
                ''',
                'destination_interface_name',
                'Cisco-IOS-XR-Ethernet-SPAN-cfg', False, has_when=True),
            _MetaInfoClassMember('destination-ipv4-address', ATTRIBUTE, 'str', 'inet:ipv4-address-no-zone',
                None, None,
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'],
                '''                Specify the destination next-hop IPv4 address
                ''',
                'destination_ipv4_address',
                'Cisco-IOS-XR-Ethernet-SPAN-cfg', False, has_when=True),
            _MetaInfoClassMember('destination-ipv6-address', ATTRIBUTE, 'str', 'inet:ipv6-address-no-zone',
                None, None,
                [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'],
                '''                Specify the destination next-hop IPv6 address
                ''',
                'destination_ipv6_address',
                'Cisco-IOS-XR-Ethernet-SPAN-cfg', False, has_when=True),
            ],
            'Cisco-IOS-XR-Ethernet-SPAN-cfg',
            'destination',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-Ethernet-SPAN-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_Ethernet_SPAN_cfg',
        ),
    },
    'SpanMonitorSession.Sessions.Session' : {
        'meta_info' : _MetaInfoClass('SpanMonitorSession.Sessions.Session', REFERENCE_LIST,
            '''Configuration for a particular Monitor Session''',
            False, 
            [
            _MetaInfoClassMember('session', ATTRIBUTE, 'str', 'dt1:Span-session-name',
                None, None,
                [(1, 79)], [],
                '''                Session Name
                ''',
                'session',
                'Cisco-IOS-XR-Ethernet-SPAN-cfg', True),
            _MetaInfoClassMember('destination', REFERENCE_CLASS, 'Destination', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_Ethernet_SPAN_cfg', 'SpanMonitorSession.Sessions.Session.Destination',
                [], [],
                '''                Specify a destination
                ''',
                'destination',
                'Cisco-IOS-XR-Ethernet-SPAN-cfg', False),
            _MetaInfoClassMember('class', REFERENCE_ENUM_CLASS, 'SpanSessionClass', 'dt1:Span-session-class',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_Ethernet_SPAN_datatypes', 'SpanSessionClass',
                [], [],
                '''                Enable a Monitor Session.  Setting this item
                causes the Monitor Session to be created.
                ''',
                'class_',
                'Cisco-IOS-XR-Ethernet-SPAN-cfg', False, default_value='Cisco_IOS_XR_Ethernet_SPAN_datatypes.SpanSessionClass.ethernet'),
            _MetaInfoClassMember('discard-class', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('0', '7')], [],
                '''                Specify the discard class value to be set on
                all traffic mirrored to the destination
                ''',
                'discard_class',
                'Cisco-IOS-XR-Ethernet-SPAN-cfg', False),
            _MetaInfoClassMember('inject-interface', ATTRIBUTE, 'str', 'xr:Interface-name',
                None, None,
                [], [b'[a-zA-Z0-9._/-]+'],
                '''                Specify the inject interface name
                ''',
                'inject_interface',
                'Cisco-IOS-XR-Ethernet-SPAN-cfg', False),
            _MetaInfoClassMember('traffic-class', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('0', '7')], [],
                '''                Specify the traffic class value to be set on
                all traffic mirrored to the destination
                ''',
                'traffic_class',
                'Cisco-IOS-XR-Ethernet-SPAN-cfg', False),
            ],
            'Cisco-IOS-XR-Ethernet-SPAN-cfg',
            'session',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-Ethernet-SPAN-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_Ethernet_SPAN_cfg',
        ),
    },
    'SpanMonitorSession.Sessions' : {
        'meta_info' : _MetaInfoClass('SpanMonitorSession.Sessions', REFERENCE_CLASS,
            '''Monitor-session configuration commands''',
            False, 
            [
            _MetaInfoClassMember('session', REFERENCE_LIST, 'Session', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_Ethernet_SPAN_cfg', 'SpanMonitorSession.Sessions.Session',
                [], [],
                '''                Configuration for a particular Monitor Session
                ''',
                'session',
                'Cisco-IOS-XR-Ethernet-SPAN-cfg', False),
            ],
            'Cisco-IOS-XR-Ethernet-SPAN-cfg',
            'sessions',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-Ethernet-SPAN-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_Ethernet_SPAN_cfg',
        ),
    },
    'SpanMonitorSession' : {
        'meta_info' : _MetaInfoClass('SpanMonitorSession', REFERENCE_CLASS,
            '''none''',
            False, 
            [
            _MetaInfoClassMember('sessions', REFERENCE_CLASS, 'Sessions', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_Ethernet_SPAN_cfg', 'SpanMonitorSession.Sessions',
                [], [],
                '''                Monitor-session configuration commands
                ''',
                'sessions',
                'Cisco-IOS-XR-Ethernet-SPAN-cfg', False),
            ],
            'Cisco-IOS-XR-Ethernet-SPAN-cfg',
            'span-monitor-session',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-Ethernet-SPAN-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_Ethernet_SPAN_cfg',
        ),
    },
}
_meta_table['SpanMonitorSession.Sessions.Session.Destination']['meta_info'].parent =_meta_table['SpanMonitorSession.Sessions.Session']['meta_info']
_meta_table['SpanMonitorSession.Sessions.Session']['meta_info'].parent =_meta_table['SpanMonitorSession.Sessions']['meta_info']
_meta_table['SpanMonitorSession.Sessions']['meta_info'].parent =_meta_table['SpanMonitorSession']['meta_info']
