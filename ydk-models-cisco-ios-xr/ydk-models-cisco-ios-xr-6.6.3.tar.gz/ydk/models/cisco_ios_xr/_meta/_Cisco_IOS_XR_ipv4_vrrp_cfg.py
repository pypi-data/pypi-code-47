
'''
This is auto-generated file,
which includes metadata for module Cisco_IOS_XR_ipv4_vrrp_cfg
'''

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_LIST, REFERENCE_LEAFLIST, REFERENCE_BITS, REFERENCE_UNION
from ydk._core._dm_meta_info import REFERENCE_CLASS, REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, ANYXML_CLASS
from ydk._core._importer import _yang_ns

_meta_table = {
    'Vrrp.Logging' : {
        'meta_info' : _MetaInfoClass('Vrrp.Logging', REFERENCE_CLASS,
            '''VRRP logging options''',
            False, 
            [
            _MetaInfoClassMember('state-change-disable', ATTRIBUTE, 'Empty', 'empty',
                None, None,
                [], [],
                '''                VRRP state change IOS messages disable
                ''',
                'state_change_disable',
                'Cisco-IOS-XR-ipv4-vrrp-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-vrrp-cfg',
            'logging',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-ipv4-vrrp-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_vrrp_cfg',
        ),
    },
    'Vrrp.Interfaces.Interface.Ipv6.Version3.VirtualRouters.VirtualRouter.GlobalIpv6Addresses.GlobalIpv6Address' : {
        'meta_info' : _MetaInfoClass('Vrrp.Interfaces.Interface.Ipv6.Version3.VirtualRouters.VirtualRouter.GlobalIpv6Addresses.GlobalIpv6Address', REFERENCE_LIST,
            '''A VRRP virtual global IPv6 IP address''',
            False, 
            [
            _MetaInfoClassMember('ip-address', REFERENCE_UNION, 'str', 'inet:ip-address-no-zone',
                None, None,
                [], [],
                '''                VRRP virtual global IPv6 address
                ''',
                'ip_address',
                'Cisco-IOS-XR-ipv4-vrrp-cfg', True, [
                    _MetaInfoClassMember('ip-address', ATTRIBUTE, 'str', 'inet:ipv4-address-no-zone',
                        None, None,
                        [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'],
                        '''                        VRRP virtual global IPv6 address
                        ''',
                        'ip_address',
                        'Cisco-IOS-XR-ipv4-vrrp-cfg', True),
                    _MetaInfoClassMember('ip-address', ATTRIBUTE, 'str', 'inet:ipv6-address-no-zone',
                        None, None,
                        [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'],
                        '''                        VRRP virtual global IPv6 address
                        ''',
                        'ip_address',
                        'Cisco-IOS-XR-ipv4-vrrp-cfg', True),
                ]),
            ],
            'Cisco-IOS-XR-ipv4-vrrp-cfg',
            'global-ipv6-address',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-ipv4-vrrp-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_vrrp_cfg',
        ),
    },
    'Vrrp.Interfaces.Interface.Ipv6.Version3.VirtualRouters.VirtualRouter.GlobalIpv6Addresses' : {
        'meta_info' : _MetaInfoClass('Vrrp.Interfaces.Interface.Ipv6.Version3.VirtualRouters.VirtualRouter.GlobalIpv6Addresses', REFERENCE_CLASS,
            '''The table of VRRP virtual global IPv6
addresses''',
            False, 
            [
            _MetaInfoClassMember('global-ipv6-address', REFERENCE_LIST, 'GlobalIpv6Address', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_vrrp_cfg', 'Vrrp.Interfaces.Interface.Ipv6.Version3.VirtualRouters.VirtualRouter.GlobalIpv6Addresses.GlobalIpv6Address',
                [], [],
                '''                A VRRP virtual global IPv6 IP address
                ''',
                'global_ipv6_address',
                'Cisco-IOS-XR-ipv4-vrrp-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-vrrp-cfg',
            'global-ipv6-addresses',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-ipv4-vrrp-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_vrrp_cfg',
        ),
    },
    'Vrrp.Interfaces.Interface.Ipv6.Version3.VirtualRouters.VirtualRouter.Tracks.Track' : {
        'meta_info' : _MetaInfoClass('Vrrp.Interfaces.Interface.Ipv6.Version3.VirtualRouters.VirtualRouter.Tracks.Track', REFERENCE_LIST,
            '''Object to be tracked''',
            False, 
            [
            _MetaInfoClassMember('interface-name', ATTRIBUTE, 'str', 'xr:Interface-name',
                None, None,
                [], [b'[a-zA-Z0-9._/-]+'],
                '''                Object to be tracked, interface name for
                interfaces
                ''',
                'interface_name',
                'Cisco-IOS-XR-ipv4-vrrp-cfg', True),
            _MetaInfoClassMember('priority', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('1', '254')], [],
                '''                Priority decrement
                ''',
                'priority',
                'Cisco-IOS-XR-ipv4-vrrp-cfg', False, is_mandatory=True),
            ],
            'Cisco-IOS-XR-ipv4-vrrp-cfg',
            'track',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-ipv4-vrrp-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_vrrp_cfg',
        ),
    },
    'Vrrp.Interfaces.Interface.Ipv6.Version3.VirtualRouters.VirtualRouter.Tracks' : {
        'meta_info' : _MetaInfoClass('Vrrp.Interfaces.Interface.Ipv6.Version3.VirtualRouters.VirtualRouter.Tracks', REFERENCE_CLASS,
            '''Track an item, reducing priority if it
goes down''',
            False, 
            [
            _MetaInfoClassMember('track', REFERENCE_LIST, 'Track', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_vrrp_cfg', 'Vrrp.Interfaces.Interface.Ipv6.Version3.VirtualRouters.VirtualRouter.Tracks.Track',
                [], [],
                '''                Object to be tracked
                ''',
                'track',
                'Cisco-IOS-XR-ipv4-vrrp-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-vrrp-cfg',
            'tracks',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-ipv4-vrrp-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_vrrp_cfg',
        ),
    },
    'Vrrp.Interfaces.Interface.Ipv6.Version3.VirtualRouters.VirtualRouter.Timer' : {
        'meta_info' : _MetaInfoClass('Vrrp.Interfaces.Interface.Ipv6.Version3.VirtualRouters.VirtualRouter.Timer', REFERENCE_CLASS,
            '''Set advertisement timer''',
            False, 
            [
            _MetaInfoClassMember('advertisement-time-in-msec', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('100', '40950')], [],
                '''                Advertisement time in milliseconds
                ''',
                'advertisement_time_in_msec',
                'Cisco-IOS-XR-ipv4-vrrp-cfg', False),
            _MetaInfoClassMember('advertisement-time-in-sec', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('1', '40')], [],
                '''                Advertisement time in seconds
                ''',
                'advertisement_time_in_sec',
                'Cisco-IOS-XR-ipv4-vrrp-cfg', False),
            _MetaInfoClassMember('forced', ATTRIBUTE, 'Empty', 'empty',
                None, None,
                [], [],
                '''                TRUE - Force configured timer values to
                be used, required when configured in
                milliseconds
                ''',
                'forced',
                'Cisco-IOS-XR-ipv4-vrrp-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-vrrp-cfg',
            'timer',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-ipv4-vrrp-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_vrrp_cfg',
        ),
    },
    'Vrrp.Interfaces.Interface.Ipv6.Version3.VirtualRouters.VirtualRouter.TrackedObjects.TrackedObject' : {
        'meta_info' : _MetaInfoClass('Vrrp.Interfaces.Interface.Ipv6.Version3.VirtualRouters.VirtualRouter.TrackedObjects.TrackedObject', REFERENCE_LIST,
            '''Object to be tracked''',
            False, 
            [
            _MetaInfoClassMember('object-name', ATTRIBUTE, 'str', 'xr:Cisco-ios-xr-string',
                None, None,
                [], [b'[\\w\\-\\.:,_@#%$\\+=\\|;]+'],
                '''                Object to be tracked, interface name for
                interfaces
                ''',
                'object_name',
                'Cisco-IOS-XR-ipv4-vrrp-cfg', True),
            _MetaInfoClassMember('priority-decrement', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('1', '254')], [],
                '''                Priority decrement
                ''',
                'priority_decrement',
                'Cisco-IOS-XR-ipv4-vrrp-cfg', False, is_mandatory=True),
            ],
            'Cisco-IOS-XR-ipv4-vrrp-cfg',
            'tracked-object',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-ipv4-vrrp-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_vrrp_cfg',
        ),
    },
    'Vrrp.Interfaces.Interface.Ipv6.Version3.VirtualRouters.VirtualRouter.TrackedObjects' : {
        'meta_info' : _MetaInfoClass('Vrrp.Interfaces.Interface.Ipv6.Version3.VirtualRouters.VirtualRouter.TrackedObjects', REFERENCE_CLASS,
            '''Track an object, reducing priority if it
goes down''',
            False, 
            [
            _MetaInfoClassMember('tracked-object', REFERENCE_LIST, 'TrackedObject', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_vrrp_cfg', 'Vrrp.Interfaces.Interface.Ipv6.Version3.VirtualRouters.VirtualRouter.TrackedObjects.TrackedObject',
                [], [],
                '''                Object to be tracked
                ''',
                'tracked_object',
                'Cisco-IOS-XR-ipv4-vrrp-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-vrrp-cfg',
            'tracked-objects',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-ipv4-vrrp-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_vrrp_cfg',
        ),
    },
    'Vrrp.Interfaces.Interface.Ipv6.Version3.VirtualRouters.VirtualRouter.LinkLocalIpv6Address' : {
        'meta_info' : _MetaInfoClass('Vrrp.Interfaces.Interface.Ipv6.Version3.VirtualRouters.VirtualRouter.LinkLocalIpv6Address', REFERENCE_CLASS,
            '''The VRRP IPv6 virtual linklocal address''',
            False, 
            [
            _MetaInfoClassMember('ip-address', REFERENCE_UNION, 'str', 'inet:ip-address-no-zone',
                None, None,
                [], [],
                '''                VRRP IPv6 virtual linklocal address
                ''',
                'ip_address',
                'Cisco-IOS-XR-ipv4-vrrp-cfg', False, [
                    _MetaInfoClassMember('ip-address', ATTRIBUTE, 'str', 'inet:ipv4-address-no-zone',
                        None, None,
                        [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'],
                        '''                        VRRP IPv6 virtual linklocal address
                        ''',
                        'ip_address',
                        'Cisco-IOS-XR-ipv4-vrrp-cfg', False, has_when=True),
                    _MetaInfoClassMember('ip-address', ATTRIBUTE, 'str', 'inet:ipv6-address-no-zone',
                        None, None,
                        [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'],
                        '''                        VRRP IPv6 virtual linklocal address
                        ''',
                        'ip_address',
                        'Cisco-IOS-XR-ipv4-vrrp-cfg', False, has_when=True),
                ], has_when=True),
            _MetaInfoClassMember('auto-configure', ATTRIBUTE, 'bool', 'boolean',
                None, None,
                [], [],
                '''                TRUE if the virtual linklocal address is
                to be autoconfigured FALSE if an IPv6
                virtual linklocal address is configured
                ''',
                'auto_configure',
                'Cisco-IOS-XR-ipv4-vrrp-cfg', False, default_value='False'),
            ],
            'Cisco-IOS-XR-ipv4-vrrp-cfg',
            'link-local-ipv6-address',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-ipv4-vrrp-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_vrrp_cfg',
        ),
    },
    'Vrrp.Interfaces.Interface.Ipv6.Version3.VirtualRouters.VirtualRouter' : {
        'meta_info' : _MetaInfoClass('Vrrp.Interfaces.Interface.Ipv6.Version3.VirtualRouters.VirtualRouter', REFERENCE_LIST,
            '''The VRRP virtual router being configured''',
            False, 
            [
            _MetaInfoClassMember('vr-id', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('1', '255')], [],
                '''                VRID Virtual Router Identifier
                ''',
                'vr_id',
                'Cisco-IOS-XR-ipv4-vrrp-cfg', True),
            _MetaInfoClassMember('global-ipv6-addresses', REFERENCE_CLASS, 'GlobalIpv6Addresses', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_vrrp_cfg', 'Vrrp.Interfaces.Interface.Ipv6.Version3.VirtualRouters.VirtualRouter.GlobalIpv6Addresses',
                [], [],
                '''                The table of VRRP virtual global IPv6
                addresses
                ''',
                'global_ipv6_addresses',
                'Cisco-IOS-XR-ipv4-vrrp-cfg', False),
            _MetaInfoClassMember('tracks', REFERENCE_CLASS, 'Tracks', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_vrrp_cfg', 'Vrrp.Interfaces.Interface.Ipv6.Version3.VirtualRouters.VirtualRouter.Tracks',
                [], [],
                '''                Track an item, reducing priority if it
                goes down
                ''',
                'tracks',
                'Cisco-IOS-XR-ipv4-vrrp-cfg', False),
            _MetaInfoClassMember('timer', REFERENCE_CLASS, 'Timer', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_vrrp_cfg', 'Vrrp.Interfaces.Interface.Ipv6.Version3.VirtualRouters.VirtualRouter.Timer',
                [], [],
                '''                Set advertisement timer
                ''',
                'timer',
                'Cisco-IOS-XR-ipv4-vrrp-cfg', False),
            _MetaInfoClassMember('tracked-objects', REFERENCE_CLASS, 'TrackedObjects', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_vrrp_cfg', 'Vrrp.Interfaces.Interface.Ipv6.Version3.VirtualRouters.VirtualRouter.TrackedObjects',
                [], [],
                '''                Track an object, reducing priority if it
                goes down
                ''',
                'tracked_objects',
                'Cisco-IOS-XR-ipv4-vrrp-cfg', False),
            _MetaInfoClassMember('link-local-ipv6-address', REFERENCE_CLASS, 'LinkLocalIpv6Address', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_vrrp_cfg', 'Vrrp.Interfaces.Interface.Ipv6.Version3.VirtualRouters.VirtualRouter.LinkLocalIpv6Address',
                [], [],
                '''                The VRRP IPv6 virtual linklocal address
                ''',
                'link_local_ipv6_address',
                'Cisco-IOS-XR-ipv4-vrrp-cfg', False),
            _MetaInfoClassMember('bfd', REFERENCE_UNION, 'str', 'inet:ip-address-no-zone',
                None, None,
                [], [],
                '''                Enable use of Bidirectional Forwarding
                Detection for this IP
                ''',
                'bfd',
                'Cisco-IOS-XR-ipv4-vrrp-cfg', False, [
                    _MetaInfoClassMember('bfd', ATTRIBUTE, 'str', 'inet:ipv4-address-no-zone',
                        None, None,
                        [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'],
                        '''                        Enable use of Bidirectional Forwarding
                        Detection for this IP
                        ''',
                        'bfd',
                        'Cisco-IOS-XR-ipv4-vrrp-cfg', False),
                    _MetaInfoClassMember('bfd', ATTRIBUTE, 'str', 'inet:ipv6-address-no-zone',
                        None, None,
                        [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'],
                        '''                        Enable use of Bidirectional Forwarding
                        Detection for this IP
                        ''',
                        'bfd',
                        'Cisco-IOS-XR-ipv4-vrrp-cfg', False),
                ]),
            _MetaInfoClassMember('priority', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('1', '254')], [],
                '''                Priority value
                ''',
                'priority',
                'Cisco-IOS-XR-ipv4-vrrp-cfg', False, default_value="100"),
            _MetaInfoClassMember('accept-mode-disable', ATTRIBUTE, 'Empty', 'empty',
                None, None,
                [], [],
                '''                Disable Accept Mode for this virtual
                IPAddress
                ''',
                'accept_mode_disable',
                'Cisco-IOS-XR-ipv4-vrrp-cfg', False),
            _MetaInfoClassMember('preempt', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('0', '3600')], [],
                '''                Preempt Master router if higher priority
                ''',
                'preempt',
                'Cisco-IOS-XR-ipv4-vrrp-cfg', False, default_value="0"),
            _MetaInfoClassMember('session-name', ATTRIBUTE, 'str', 'xr:Cisco-ios-xr-string',
                None, None,
                [(1, 16)], [],
                '''                VRRP Session Name
                ''',
                'session_name',
                'Cisco-IOS-XR-ipv4-vrrp-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-vrrp-cfg',
            'virtual-router',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-ipv4-vrrp-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_vrrp_cfg',
        ),
    },
    'Vrrp.Interfaces.Interface.Ipv6.Version3.VirtualRouters' : {
        'meta_info' : _MetaInfoClass('Vrrp.Interfaces.Interface.Ipv6.Version3.VirtualRouters', REFERENCE_CLASS,
            '''The VRRP virtual router configuration table''',
            False, 
            [
            _MetaInfoClassMember('virtual-router', REFERENCE_LIST, 'VirtualRouter', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_vrrp_cfg', 'Vrrp.Interfaces.Interface.Ipv6.Version3.VirtualRouters.VirtualRouter',
                [], [],
                '''                The VRRP virtual router being configured
                ''',
                'virtual_router',
                'Cisco-IOS-XR-ipv4-vrrp-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-vrrp-cfg',
            'virtual-routers',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-ipv4-vrrp-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_vrrp_cfg',
        ),
    },
    'Vrrp.Interfaces.Interface.Ipv6.Version3' : {
        'meta_info' : _MetaInfoClass('Vrrp.Interfaces.Interface.Ipv6.Version3', REFERENCE_CLASS,
            '''Version 3 VRRP configuration''',
            False, 
            [
            _MetaInfoClassMember('virtual-routers', REFERENCE_CLASS, 'VirtualRouters', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_vrrp_cfg', 'Vrrp.Interfaces.Interface.Ipv6.Version3.VirtualRouters',
                [], [],
                '''                The VRRP virtual router configuration table
                ''',
                'virtual_routers',
                'Cisco-IOS-XR-ipv4-vrrp-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-vrrp-cfg',
            'version3',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-ipv4-vrrp-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_vrrp_cfg',
        ),
    },
    'Vrrp.Interfaces.Interface.Ipv6.SlaveVirtualRouters.SlaveVirtualRouter.LinkLocalIpv6Address' : {
        'meta_info' : _MetaInfoClass('Vrrp.Interfaces.Interface.Ipv6.SlaveVirtualRouters.SlaveVirtualRouter.LinkLocalIpv6Address', REFERENCE_CLASS,
            '''The VRRP IPv6 virtual linklocal address''',
            False, 
            [
            _MetaInfoClassMember('ip-address', REFERENCE_UNION, 'str', 'inet:ip-address-no-zone',
                None, None,
                [], [],
                '''                VRRP IPv6 virtual linklocal address
                ''',
                'ip_address',
                'Cisco-IOS-XR-ipv4-vrrp-cfg', False, [
                    _MetaInfoClassMember('ip-address', ATTRIBUTE, 'str', 'inet:ipv4-address-no-zone',
                        None, None,
                        [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'],
                        '''                        VRRP IPv6 virtual linklocal address
                        ''',
                        'ip_address',
                        'Cisco-IOS-XR-ipv4-vrrp-cfg', False, has_when=True),
                    _MetaInfoClassMember('ip-address', ATTRIBUTE, 'str', 'inet:ipv6-address-no-zone',
                        None, None,
                        [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'],
                        '''                        VRRP IPv6 virtual linklocal address
                        ''',
                        'ip_address',
                        'Cisco-IOS-XR-ipv4-vrrp-cfg', False, has_when=True),
                ], has_when=True),
            _MetaInfoClassMember('auto-configure', ATTRIBUTE, 'bool', 'boolean',
                None, None,
                [], [],
                '''                TRUE if the virtual linklocal address is
                to be autoconfigured FALSE if an IPv6
                virtual linklocal address is configured
                ''',
                'auto_configure',
                'Cisco-IOS-XR-ipv4-vrrp-cfg', False, default_value='False'),
            ],
            'Cisco-IOS-XR-ipv4-vrrp-cfg',
            'link-local-ipv6-address',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-ipv4-vrrp-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_vrrp_cfg',
        ),
    },
    'Vrrp.Interfaces.Interface.Ipv6.SlaveVirtualRouters.SlaveVirtualRouter.GlobalIpv6Addresses.GlobalIpv6Address' : {
        'meta_info' : _MetaInfoClass('Vrrp.Interfaces.Interface.Ipv6.SlaveVirtualRouters.SlaveVirtualRouter.GlobalIpv6Addresses.GlobalIpv6Address', REFERENCE_LIST,
            '''A VRRP virtual global IPv6 IP address''',
            False, 
            [
            _MetaInfoClassMember('ip-address', REFERENCE_UNION, 'str', 'inet:ip-address-no-zone',
                None, None,
                [], [],
                '''                VRRP virtual global IPv6 address
                ''',
                'ip_address',
                'Cisco-IOS-XR-ipv4-vrrp-cfg', True, [
                    _MetaInfoClassMember('ip-address', ATTRIBUTE, 'str', 'inet:ipv4-address-no-zone',
                        None, None,
                        [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'],
                        '''                        VRRP virtual global IPv6 address
                        ''',
                        'ip_address',
                        'Cisco-IOS-XR-ipv4-vrrp-cfg', True),
                    _MetaInfoClassMember('ip-address', ATTRIBUTE, 'str', 'inet:ipv6-address-no-zone',
                        None, None,
                        [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'],
                        '''                        VRRP virtual global IPv6 address
                        ''',
                        'ip_address',
                        'Cisco-IOS-XR-ipv4-vrrp-cfg', True),
                ]),
            ],
            'Cisco-IOS-XR-ipv4-vrrp-cfg',
            'global-ipv6-address',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-ipv4-vrrp-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_vrrp_cfg',
        ),
    },
    'Vrrp.Interfaces.Interface.Ipv6.SlaveVirtualRouters.SlaveVirtualRouter.GlobalIpv6Addresses' : {
        'meta_info' : _MetaInfoClass('Vrrp.Interfaces.Interface.Ipv6.SlaveVirtualRouters.SlaveVirtualRouter.GlobalIpv6Addresses', REFERENCE_CLASS,
            '''The table of VRRP virtual global IPv6
addresses''',
            False, 
            [
            _MetaInfoClassMember('global-ipv6-address', REFERENCE_LIST, 'GlobalIpv6Address', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_vrrp_cfg', 'Vrrp.Interfaces.Interface.Ipv6.SlaveVirtualRouters.SlaveVirtualRouter.GlobalIpv6Addresses.GlobalIpv6Address',
                [], [],
                '''                A VRRP virtual global IPv6 IP address
                ''',
                'global_ipv6_address',
                'Cisco-IOS-XR-ipv4-vrrp-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-vrrp-cfg',
            'global-ipv6-addresses',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-ipv4-vrrp-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_vrrp_cfg',
        ),
    },
    'Vrrp.Interfaces.Interface.Ipv6.SlaveVirtualRouters.SlaveVirtualRouter' : {
        'meta_info' : _MetaInfoClass('Vrrp.Interfaces.Interface.Ipv6.SlaveVirtualRouters.SlaveVirtualRouter', REFERENCE_LIST,
            '''The VRRP slave being configured''',
            False, 
            [
            _MetaInfoClassMember('slave-virtual-router-id', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('1', '255')], [],
                '''                Virtual Router ID
                ''',
                'slave_virtual_router_id',
                'Cisco-IOS-XR-ipv4-vrrp-cfg', True),
            _MetaInfoClassMember('link-local-ipv6-address', REFERENCE_CLASS, 'LinkLocalIpv6Address', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_vrrp_cfg', 'Vrrp.Interfaces.Interface.Ipv6.SlaveVirtualRouters.SlaveVirtualRouter.LinkLocalIpv6Address',
                [], [],
                '''                The VRRP IPv6 virtual linklocal address
                ''',
                'link_local_ipv6_address',
                'Cisco-IOS-XR-ipv4-vrrp-cfg', False),
            _MetaInfoClassMember('global-ipv6-addresses', REFERENCE_CLASS, 'GlobalIpv6Addresses', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_vrrp_cfg', 'Vrrp.Interfaces.Interface.Ipv6.SlaveVirtualRouters.SlaveVirtualRouter.GlobalIpv6Addresses',
                [], [],
                '''                The table of VRRP virtual global IPv6
                addresses
                ''',
                'global_ipv6_addresses',
                'Cisco-IOS-XR-ipv4-vrrp-cfg', False),
            _MetaInfoClassMember('follow', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                VRRP Session name for this slave to follow
                ''',
                'follow',
                'Cisco-IOS-XR-ipv4-vrrp-cfg', False),
            _MetaInfoClassMember('accept-mode-disable', ATTRIBUTE, 'Empty', 'empty',
                None, None,
                [], [],
                '''                Disable Accept Mode for this virtual
                IPAddress
                ''',
                'accept_mode_disable',
                'Cisco-IOS-XR-ipv4-vrrp-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-vrrp-cfg',
            'slave-virtual-router',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-ipv4-vrrp-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_vrrp_cfg',
        ),
    },
    'Vrrp.Interfaces.Interface.Ipv6.SlaveVirtualRouters' : {
        'meta_info' : _MetaInfoClass('Vrrp.Interfaces.Interface.Ipv6.SlaveVirtualRouters', REFERENCE_CLASS,
            '''The VRRP slave group configuration table''',
            False, 
            [
            _MetaInfoClassMember('slave-virtual-router', REFERENCE_LIST, 'SlaveVirtualRouter', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_vrrp_cfg', 'Vrrp.Interfaces.Interface.Ipv6.SlaveVirtualRouters.SlaveVirtualRouter',
                [], [],
                '''                The VRRP slave being configured
                ''',
                'slave_virtual_router',
                'Cisco-IOS-XR-ipv4-vrrp-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-vrrp-cfg',
            'slave-virtual-routers',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-ipv4-vrrp-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_vrrp_cfg',
        ),
    },
    'Vrrp.Interfaces.Interface.Ipv6' : {
        'meta_info' : _MetaInfoClass('Vrrp.Interfaces.Interface.Ipv6', REFERENCE_CLASS,
            '''IPv6 VRRP configuration''',
            False, 
            [
            _MetaInfoClassMember('version3', REFERENCE_CLASS, 'Version3', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_vrrp_cfg', 'Vrrp.Interfaces.Interface.Ipv6.Version3',
                [], [],
                '''                Version 3 VRRP configuration
                ''',
                'version3',
                'Cisco-IOS-XR-ipv4-vrrp-cfg', False),
            _MetaInfoClassMember('slave-virtual-routers', REFERENCE_CLASS, 'SlaveVirtualRouters', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_vrrp_cfg', 'Vrrp.Interfaces.Interface.Ipv6.SlaveVirtualRouters',
                [], [],
                '''                The VRRP slave group configuration table
                ''',
                'slave_virtual_routers',
                'Cisco-IOS-XR-ipv4-vrrp-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-vrrp-cfg',
            'ipv6',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-ipv4-vrrp-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_vrrp_cfg',
        ),
    },
    'Vrrp.Interfaces.Interface.Delay' : {
        'meta_info' : _MetaInfoClass('Vrrp.Interfaces.Interface.Delay', REFERENCE_CLASS,
            '''Minimum and Reload Delay''',
            False, 
            [
            _MetaInfoClassMember('min-delay', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('0', '10000')], [],
                '''                Minimum delay in seconds
                ''',
                'min_delay',
                'Cisco-IOS-XR-ipv4-vrrp-cfg', False, is_mandatory=True),
            _MetaInfoClassMember('reload-delay', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('0', '10000')], [],
                '''                Reload delay in seconds
                ''',
                'reload_delay',
                'Cisco-IOS-XR-ipv4-vrrp-cfg', False, is_mandatory=True),
            ],
            'Cisco-IOS-XR-ipv4-vrrp-cfg',
            'delay',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-ipv4-vrrp-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_vrrp_cfg',
            is_presence=True,
        ),
    },
    'Vrrp.Interfaces.Interface.Ipv4.Version3.VirtualRouters.VirtualRouter.Timer' : {
        'meta_info' : _MetaInfoClass('Vrrp.Interfaces.Interface.Ipv4.Version3.VirtualRouters.VirtualRouter.Timer', REFERENCE_CLASS,
            '''Set advertisement timer''',
            False, 
            [
            _MetaInfoClassMember('advertisement-time-in-msec', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('100', '40950')], [],
                '''                Advertisement time in milliseconds
                ''',
                'advertisement_time_in_msec',
                'Cisco-IOS-XR-ipv4-vrrp-cfg', False),
            _MetaInfoClassMember('advertisement-time-in-sec', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('1', '40')], [],
                '''                Advertisement time in seconds
                ''',
                'advertisement_time_in_sec',
                'Cisco-IOS-XR-ipv4-vrrp-cfg', False),
            _MetaInfoClassMember('forced', ATTRIBUTE, 'Empty', 'empty',
                None, None,
                [], [],
                '''                TRUE - Force configured timer values to
                be used, required when configured in
                milliseconds
                ''',
                'forced',
                'Cisco-IOS-XR-ipv4-vrrp-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-vrrp-cfg',
            'timer',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-ipv4-vrrp-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_vrrp_cfg',
        ),
    },
    'Vrrp.Interfaces.Interface.Ipv4.Version3.VirtualRouters.VirtualRouter.SecondaryIpv4Addresses.SecondaryIpv4Address' : {
        'meta_info' : _MetaInfoClass('Vrrp.Interfaces.Interface.Ipv4.Version3.VirtualRouters.VirtualRouter.SecondaryIpv4Addresses.SecondaryIpv4Address', REFERENCE_LIST,
            '''A VRRP secondary IPv4 address''',
            False, 
            [
            _MetaInfoClassMember('ip-address', ATTRIBUTE, 'str', 'inet:ipv4-address-no-zone',
                None, None,
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'],
                '''                VRRP Secondary IPv4 address
                ''',
                'ip_address',
                'Cisco-IOS-XR-ipv4-vrrp-cfg', True),
            ],
            'Cisco-IOS-XR-ipv4-vrrp-cfg',
            'secondary-ipv4-address',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-ipv4-vrrp-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_vrrp_cfg',
        ),
    },
    'Vrrp.Interfaces.Interface.Ipv4.Version3.VirtualRouters.VirtualRouter.SecondaryIpv4Addresses' : {
        'meta_info' : _MetaInfoClass('Vrrp.Interfaces.Interface.Ipv4.Version3.VirtualRouters.VirtualRouter.SecondaryIpv4Addresses', REFERENCE_CLASS,
            '''The table of VRRP secondary IPv4 addresses''',
            False, 
            [
            _MetaInfoClassMember('secondary-ipv4-address', REFERENCE_LIST, 'SecondaryIpv4Address', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_vrrp_cfg', 'Vrrp.Interfaces.Interface.Ipv4.Version3.VirtualRouters.VirtualRouter.SecondaryIpv4Addresses.SecondaryIpv4Address',
                [], [],
                '''                A VRRP secondary IPv4 address
                ''',
                'secondary_ipv4_address',
                'Cisco-IOS-XR-ipv4-vrrp-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-vrrp-cfg',
            'secondary-ipv4-addresses',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-ipv4-vrrp-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_vrrp_cfg',
        ),
    },
    'Vrrp.Interfaces.Interface.Ipv4.Version3.VirtualRouters.VirtualRouter.TrackedObjects.TrackedObject' : {
        'meta_info' : _MetaInfoClass('Vrrp.Interfaces.Interface.Ipv4.Version3.VirtualRouters.VirtualRouter.TrackedObjects.TrackedObject', REFERENCE_LIST,
            '''Object to be tracked''',
            False, 
            [
            _MetaInfoClassMember('object-name', ATTRIBUTE, 'str', 'xr:Cisco-ios-xr-string',
                None, None,
                [], [b'[\\w\\-\\.:,_@#%$\\+=\\|;]+'],
                '''                Object to be tracked, interface name for
                interfaces
                ''',
                'object_name',
                'Cisco-IOS-XR-ipv4-vrrp-cfg', True),
            _MetaInfoClassMember('priority-decrement', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('1', '254')], [],
                '''                Priority decrement
                ''',
                'priority_decrement',
                'Cisco-IOS-XR-ipv4-vrrp-cfg', False, is_mandatory=True),
            ],
            'Cisco-IOS-XR-ipv4-vrrp-cfg',
            'tracked-object',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-ipv4-vrrp-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_vrrp_cfg',
        ),
    },
    'Vrrp.Interfaces.Interface.Ipv4.Version3.VirtualRouters.VirtualRouter.TrackedObjects' : {
        'meta_info' : _MetaInfoClass('Vrrp.Interfaces.Interface.Ipv4.Version3.VirtualRouters.VirtualRouter.TrackedObjects', REFERENCE_CLASS,
            '''Track an object, reducing priority if it
goes down''',
            False, 
            [
            _MetaInfoClassMember('tracked-object', REFERENCE_LIST, 'TrackedObject', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_vrrp_cfg', 'Vrrp.Interfaces.Interface.Ipv4.Version3.VirtualRouters.VirtualRouter.TrackedObjects.TrackedObject',
                [], [],
                '''                Object to be tracked
                ''',
                'tracked_object',
                'Cisco-IOS-XR-ipv4-vrrp-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-vrrp-cfg',
            'tracked-objects',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-ipv4-vrrp-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_vrrp_cfg',
        ),
    },
    'Vrrp.Interfaces.Interface.Ipv4.Version3.VirtualRouters.VirtualRouter.Tracks.Track' : {
        'meta_info' : _MetaInfoClass('Vrrp.Interfaces.Interface.Ipv4.Version3.VirtualRouters.VirtualRouter.Tracks.Track', REFERENCE_LIST,
            '''Object to be tracked''',
            False, 
            [
            _MetaInfoClassMember('interface-name', ATTRIBUTE, 'str', 'xr:Interface-name',
                None, None,
                [], [b'[a-zA-Z0-9._/-]+'],
                '''                Object to be tracked, interface name for
                interfaces
                ''',
                'interface_name',
                'Cisco-IOS-XR-ipv4-vrrp-cfg', True),
            _MetaInfoClassMember('priority', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('1', '254')], [],
                '''                Priority decrement
                ''',
                'priority',
                'Cisco-IOS-XR-ipv4-vrrp-cfg', False, is_mandatory=True),
            ],
            'Cisco-IOS-XR-ipv4-vrrp-cfg',
            'track',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-ipv4-vrrp-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_vrrp_cfg',
        ),
    },
    'Vrrp.Interfaces.Interface.Ipv4.Version3.VirtualRouters.VirtualRouter.Tracks' : {
        'meta_info' : _MetaInfoClass('Vrrp.Interfaces.Interface.Ipv4.Version3.VirtualRouters.VirtualRouter.Tracks', REFERENCE_CLASS,
            '''Track an item, reducing priority if it
goes down''',
            False, 
            [
            _MetaInfoClassMember('track', REFERENCE_LIST, 'Track', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_vrrp_cfg', 'Vrrp.Interfaces.Interface.Ipv4.Version3.VirtualRouters.VirtualRouter.Tracks.Track',
                [], [],
                '''                Object to be tracked
                ''',
                'track',
                'Cisco-IOS-XR-ipv4-vrrp-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-vrrp-cfg',
            'tracks',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-ipv4-vrrp-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_vrrp_cfg',
        ),
    },
    'Vrrp.Interfaces.Interface.Ipv4.Version3.VirtualRouters.VirtualRouter' : {
        'meta_info' : _MetaInfoClass('Vrrp.Interfaces.Interface.Ipv4.Version3.VirtualRouters.VirtualRouter', REFERENCE_LIST,
            '''The VRRP virtual router being configured''',
            False, 
            [
            _MetaInfoClassMember('vr-id', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('1', '255')], [],
                '''                VRID Virtual Router Identifier
                ''',
                'vr_id',
                'Cisco-IOS-XR-ipv4-vrrp-cfg', True),
            _MetaInfoClassMember('timer', REFERENCE_CLASS, 'Timer', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_vrrp_cfg', 'Vrrp.Interfaces.Interface.Ipv4.Version3.VirtualRouters.VirtualRouter.Timer',
                [], [],
                '''                Set advertisement timer
                ''',
                'timer',
                'Cisco-IOS-XR-ipv4-vrrp-cfg', False),
            _MetaInfoClassMember('secondary-ipv4-addresses', REFERENCE_CLASS, 'SecondaryIpv4Addresses', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_vrrp_cfg', 'Vrrp.Interfaces.Interface.Ipv4.Version3.VirtualRouters.VirtualRouter.SecondaryIpv4Addresses',
                [], [],
                '''                The table of VRRP secondary IPv4 addresses
                ''',
                'secondary_ipv4_addresses',
                'Cisco-IOS-XR-ipv4-vrrp-cfg', False),
            _MetaInfoClassMember('tracked-objects', REFERENCE_CLASS, 'TrackedObjects', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_vrrp_cfg', 'Vrrp.Interfaces.Interface.Ipv4.Version3.VirtualRouters.VirtualRouter.TrackedObjects',
                [], [],
                '''                Track an object, reducing priority if it
                goes down
                ''',
                'tracked_objects',
                'Cisco-IOS-XR-ipv4-vrrp-cfg', False),
            _MetaInfoClassMember('tracks', REFERENCE_CLASS, 'Tracks', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_vrrp_cfg', 'Vrrp.Interfaces.Interface.Ipv4.Version3.VirtualRouters.VirtualRouter.Tracks',
                [], [],
                '''                Track an item, reducing priority if it
                goes down
                ''',
                'tracks',
                'Cisco-IOS-XR-ipv4-vrrp-cfg', False),
            _MetaInfoClassMember('session-name', ATTRIBUTE, 'str', 'xr:Cisco-ios-xr-string',
                None, None,
                [(1, 16)], [],
                '''                VRRP Session Name
                ''',
                'session_name',
                'Cisco-IOS-XR-ipv4-vrrp-cfg', False),
            _MetaInfoClassMember('bfd', ATTRIBUTE, 'str', 'inet:ipv4-address-no-zone',
                None, None,
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'],
                '''                Enable use of Bidirectional Forwarding
                Detection for this IP
                ''',
                'bfd',
                'Cisco-IOS-XR-ipv4-vrrp-cfg', False),
            _MetaInfoClassMember('primary-ipv4-address', ATTRIBUTE, 'str', 'inet:ipv4-address-no-zone',
                None, None,
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'],
                '''                The Primary VRRP IPv4 address
                ''',
                'primary_ipv4_address',
                'Cisco-IOS-XR-ipv4-vrrp-cfg', False),
            _MetaInfoClassMember('preempt', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('0', '3600')], [],
                '''                Preempt Master router if higher priority
                ''',
                'preempt',
                'Cisco-IOS-XR-ipv4-vrrp-cfg', False, default_value="0"),
            _MetaInfoClassMember('accept-mode-disable', ATTRIBUTE, 'Empty', 'empty',
                None, None,
                [], [],
                '''                Disable Accept Mode for this virtual
                IPAddress
                ''',
                'accept_mode_disable',
                'Cisco-IOS-XR-ipv4-vrrp-cfg', False),
            _MetaInfoClassMember('priority', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('1', '254')], [],
                '''                Priority value
                ''',
                'priority',
                'Cisco-IOS-XR-ipv4-vrrp-cfg', False, default_value="100"),
            ],
            'Cisco-IOS-XR-ipv4-vrrp-cfg',
            'virtual-router',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-ipv4-vrrp-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_vrrp_cfg',
        ),
    },
    'Vrrp.Interfaces.Interface.Ipv4.Version3.VirtualRouters' : {
        'meta_info' : _MetaInfoClass('Vrrp.Interfaces.Interface.Ipv4.Version3.VirtualRouters', REFERENCE_CLASS,
            '''The VRRP virtual router configuration table''',
            False, 
            [
            _MetaInfoClassMember('virtual-router', REFERENCE_LIST, 'VirtualRouter', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_vrrp_cfg', 'Vrrp.Interfaces.Interface.Ipv4.Version3.VirtualRouters.VirtualRouter',
                [], [],
                '''                The VRRP virtual router being configured
                ''',
                'virtual_router',
                'Cisco-IOS-XR-ipv4-vrrp-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-vrrp-cfg',
            'virtual-routers',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-ipv4-vrrp-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_vrrp_cfg',
        ),
    },
    'Vrrp.Interfaces.Interface.Ipv4.Version3' : {
        'meta_info' : _MetaInfoClass('Vrrp.Interfaces.Interface.Ipv4.Version3', REFERENCE_CLASS,
            '''Version 3 VRRP configuration''',
            False, 
            [
            _MetaInfoClassMember('virtual-routers', REFERENCE_CLASS, 'VirtualRouters', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_vrrp_cfg', 'Vrrp.Interfaces.Interface.Ipv4.Version3.VirtualRouters',
                [], [],
                '''                The VRRP virtual router configuration table
                ''',
                'virtual_routers',
                'Cisco-IOS-XR-ipv4-vrrp-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-vrrp-cfg',
            'version3',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-ipv4-vrrp-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_vrrp_cfg',
        ),
    },
    'Vrrp.Interfaces.Interface.Ipv4.SlaveVirtualRouters.SlaveVirtualRouter.SecondaryIpv4Addresses.SecondaryIpv4Address' : {
        'meta_info' : _MetaInfoClass('Vrrp.Interfaces.Interface.Ipv4.SlaveVirtualRouters.SlaveVirtualRouter.SecondaryIpv4Addresses.SecondaryIpv4Address', REFERENCE_LIST,
            '''A VRRP secondary IPv4 address''',
            False, 
            [
            _MetaInfoClassMember('ip-address', ATTRIBUTE, 'str', 'inet:ipv4-address-no-zone',
                None, None,
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'],
                '''                VRRP Secondary IPv4 address
                ''',
                'ip_address',
                'Cisco-IOS-XR-ipv4-vrrp-cfg', True),
            ],
            'Cisco-IOS-XR-ipv4-vrrp-cfg',
            'secondary-ipv4-address',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-ipv4-vrrp-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_vrrp_cfg',
        ),
    },
    'Vrrp.Interfaces.Interface.Ipv4.SlaveVirtualRouters.SlaveVirtualRouter.SecondaryIpv4Addresses' : {
        'meta_info' : _MetaInfoClass('Vrrp.Interfaces.Interface.Ipv4.SlaveVirtualRouters.SlaveVirtualRouter.SecondaryIpv4Addresses', REFERENCE_CLASS,
            '''The table of VRRP secondary IPv4 addresses''',
            False, 
            [
            _MetaInfoClassMember('secondary-ipv4-address', REFERENCE_LIST, 'SecondaryIpv4Address', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_vrrp_cfg', 'Vrrp.Interfaces.Interface.Ipv4.SlaveVirtualRouters.SlaveVirtualRouter.SecondaryIpv4Addresses.SecondaryIpv4Address',
                [], [],
                '''                A VRRP secondary IPv4 address
                ''',
                'secondary_ipv4_address',
                'Cisco-IOS-XR-ipv4-vrrp-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-vrrp-cfg',
            'secondary-ipv4-addresses',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-ipv4-vrrp-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_vrrp_cfg',
        ),
    },
    'Vrrp.Interfaces.Interface.Ipv4.SlaveVirtualRouters.SlaveVirtualRouter' : {
        'meta_info' : _MetaInfoClass('Vrrp.Interfaces.Interface.Ipv4.SlaveVirtualRouters.SlaveVirtualRouter', REFERENCE_LIST,
            '''The VRRP slave being configured''',
            False, 
            [
            _MetaInfoClassMember('slave-virtual-router-id', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('1', '255')], [],
                '''                Virtual Router ID
                ''',
                'slave_virtual_router_id',
                'Cisco-IOS-XR-ipv4-vrrp-cfg', True),
            _MetaInfoClassMember('secondary-ipv4-addresses', REFERENCE_CLASS, 'SecondaryIpv4Addresses', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_vrrp_cfg', 'Vrrp.Interfaces.Interface.Ipv4.SlaveVirtualRouters.SlaveVirtualRouter.SecondaryIpv4Addresses',
                [], [],
                '''                The table of VRRP secondary IPv4 addresses
                ''',
                'secondary_ipv4_addresses',
                'Cisco-IOS-XR-ipv4-vrrp-cfg', False),
            _MetaInfoClassMember('follow', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                VRRP Session name for this slave to follow
                ''',
                'follow',
                'Cisco-IOS-XR-ipv4-vrrp-cfg', False),
            _MetaInfoClassMember('accept-mode-disable', ATTRIBUTE, 'Empty', 'empty',
                None, None,
                [], [],
                '''                Disable Accept Mode for this virtual
                IPAddress
                ''',
                'accept_mode_disable',
                'Cisco-IOS-XR-ipv4-vrrp-cfg', False),
            _MetaInfoClassMember('primary-ipv4-address', ATTRIBUTE, 'str', 'inet:ipv4-address-no-zone',
                None, None,
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'],
                '''                The Primary VRRP IPv4 address
                ''',
                'primary_ipv4_address',
                'Cisco-IOS-XR-ipv4-vrrp-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-vrrp-cfg',
            'slave-virtual-router',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-ipv4-vrrp-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_vrrp_cfg',
        ),
    },
    'Vrrp.Interfaces.Interface.Ipv4.SlaveVirtualRouters' : {
        'meta_info' : _MetaInfoClass('Vrrp.Interfaces.Interface.Ipv4.SlaveVirtualRouters', REFERENCE_CLASS,
            '''The VRRP slave group configuration table''',
            False, 
            [
            _MetaInfoClassMember('slave-virtual-router', REFERENCE_LIST, 'SlaveVirtualRouter', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_vrrp_cfg', 'Vrrp.Interfaces.Interface.Ipv4.SlaveVirtualRouters.SlaveVirtualRouter',
                [], [],
                '''                The VRRP slave being configured
                ''',
                'slave_virtual_router',
                'Cisco-IOS-XR-ipv4-vrrp-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-vrrp-cfg',
            'slave-virtual-routers',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-ipv4-vrrp-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_vrrp_cfg',
        ),
    },
    'Vrrp.Interfaces.Interface.Ipv4.Version2.VirtualRouters.VirtualRouter.Timer' : {
        'meta_info' : _MetaInfoClass('Vrrp.Interfaces.Interface.Ipv4.Version2.VirtualRouters.VirtualRouter.Timer', REFERENCE_CLASS,
            '''Set advertisement timer''',
            False, 
            [
            _MetaInfoClassMember('advertisement-time-in-msec', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('100', '40950')], [],
                '''                Advertisement time in milliseconds
                ''',
                'advertisement_time_in_msec',
                'Cisco-IOS-XR-ipv4-vrrp-cfg', False),
            _MetaInfoClassMember('advertisement-time-in-sec', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('1', '255')], [],
                '''                Advertisement time in seconds
                ''',
                'advertisement_time_in_sec',
                'Cisco-IOS-XR-ipv4-vrrp-cfg', False),
            _MetaInfoClassMember('forced', ATTRIBUTE, 'Empty', 'empty',
                None, None,
                [], [],
                '''                TRUE - Force configured timer values to
                be used, required when configured in
                milliseconds
                ''',
                'forced',
                'Cisco-IOS-XR-ipv4-vrrp-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-vrrp-cfg',
            'timer',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-ipv4-vrrp-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_vrrp_cfg',
        ),
    },
    'Vrrp.Interfaces.Interface.Ipv4.Version2.VirtualRouters.VirtualRouter.SecondaryIpv4Addresses.SecondaryIpv4Address' : {
        'meta_info' : _MetaInfoClass('Vrrp.Interfaces.Interface.Ipv4.Version2.VirtualRouters.VirtualRouter.SecondaryIpv4Addresses.SecondaryIpv4Address', REFERENCE_LIST,
            '''A VRRP secondary IPv4 address''',
            False, 
            [
            _MetaInfoClassMember('ip-address', ATTRIBUTE, 'str', 'inet:ipv4-address-no-zone',
                None, None,
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'],
                '''                VRRP Secondary IPv4 address
                ''',
                'ip_address',
                'Cisco-IOS-XR-ipv4-vrrp-cfg', True),
            ],
            'Cisco-IOS-XR-ipv4-vrrp-cfg',
            'secondary-ipv4-address',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-ipv4-vrrp-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_vrrp_cfg',
        ),
    },
    'Vrrp.Interfaces.Interface.Ipv4.Version2.VirtualRouters.VirtualRouter.SecondaryIpv4Addresses' : {
        'meta_info' : _MetaInfoClass('Vrrp.Interfaces.Interface.Ipv4.Version2.VirtualRouters.VirtualRouter.SecondaryIpv4Addresses', REFERENCE_CLASS,
            '''The table of VRRP secondary IPv4 addresses''',
            False, 
            [
            _MetaInfoClassMember('secondary-ipv4-address', REFERENCE_LIST, 'SecondaryIpv4Address', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_vrrp_cfg', 'Vrrp.Interfaces.Interface.Ipv4.Version2.VirtualRouters.VirtualRouter.SecondaryIpv4Addresses.SecondaryIpv4Address',
                [], [],
                '''                A VRRP secondary IPv4 address
                ''',
                'secondary_ipv4_address',
                'Cisco-IOS-XR-ipv4-vrrp-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-vrrp-cfg',
            'secondary-ipv4-addresses',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-ipv4-vrrp-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_vrrp_cfg',
        ),
    },
    'Vrrp.Interfaces.Interface.Ipv4.Version2.VirtualRouters.VirtualRouter.Tracks.Track' : {
        'meta_info' : _MetaInfoClass('Vrrp.Interfaces.Interface.Ipv4.Version2.VirtualRouters.VirtualRouter.Tracks.Track', REFERENCE_LIST,
            '''Object to be tracked''',
            False, 
            [
            _MetaInfoClassMember('interface-name', ATTRIBUTE, 'str', 'xr:Interface-name',
                None, None,
                [], [b'[a-zA-Z0-9._/-]+'],
                '''                Object to be tracked, interface name for
                interfaces
                ''',
                'interface_name',
                'Cisco-IOS-XR-ipv4-vrrp-cfg', True),
            _MetaInfoClassMember('priority', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('1', '254')], [],
                '''                Priority decrement
                ''',
                'priority',
                'Cisco-IOS-XR-ipv4-vrrp-cfg', False, is_mandatory=True),
            ],
            'Cisco-IOS-XR-ipv4-vrrp-cfg',
            'track',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-ipv4-vrrp-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_vrrp_cfg',
        ),
    },
    'Vrrp.Interfaces.Interface.Ipv4.Version2.VirtualRouters.VirtualRouter.Tracks' : {
        'meta_info' : _MetaInfoClass('Vrrp.Interfaces.Interface.Ipv4.Version2.VirtualRouters.VirtualRouter.Tracks', REFERENCE_CLASS,
            '''Track an item, reducing priority if it
goes down''',
            False, 
            [
            _MetaInfoClassMember('track', REFERENCE_LIST, 'Track', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_vrrp_cfg', 'Vrrp.Interfaces.Interface.Ipv4.Version2.VirtualRouters.VirtualRouter.Tracks.Track',
                [], [],
                '''                Object to be tracked
                ''',
                'track',
                'Cisco-IOS-XR-ipv4-vrrp-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-vrrp-cfg',
            'tracks',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-ipv4-vrrp-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_vrrp_cfg',
        ),
    },
    'Vrrp.Interfaces.Interface.Ipv4.Version2.VirtualRouters.VirtualRouter.TrackedObjects.TrackedObject' : {
        'meta_info' : _MetaInfoClass('Vrrp.Interfaces.Interface.Ipv4.Version2.VirtualRouters.VirtualRouter.TrackedObjects.TrackedObject', REFERENCE_LIST,
            '''Object to be tracked''',
            False, 
            [
            _MetaInfoClassMember('object-name', ATTRIBUTE, 'str', 'xr:Cisco-ios-xr-string',
                None, None,
                [], [b'[\\w\\-\\.:,_@#%$\\+=\\|;]+'],
                '''                Object to be tracked, interface name for
                interfaces
                ''',
                'object_name',
                'Cisco-IOS-XR-ipv4-vrrp-cfg', True),
            _MetaInfoClassMember('priority-decrement', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('1', '254')], [],
                '''                Priority decrement
                ''',
                'priority_decrement',
                'Cisco-IOS-XR-ipv4-vrrp-cfg', False, is_mandatory=True),
            ],
            'Cisco-IOS-XR-ipv4-vrrp-cfg',
            'tracked-object',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-ipv4-vrrp-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_vrrp_cfg',
        ),
    },
    'Vrrp.Interfaces.Interface.Ipv4.Version2.VirtualRouters.VirtualRouter.TrackedObjects' : {
        'meta_info' : _MetaInfoClass('Vrrp.Interfaces.Interface.Ipv4.Version2.VirtualRouters.VirtualRouter.TrackedObjects', REFERENCE_CLASS,
            '''Track an object, reducing priority if it
goes down''',
            False, 
            [
            _MetaInfoClassMember('tracked-object', REFERENCE_LIST, 'TrackedObject', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_vrrp_cfg', 'Vrrp.Interfaces.Interface.Ipv4.Version2.VirtualRouters.VirtualRouter.TrackedObjects.TrackedObject',
                [], [],
                '''                Object to be tracked
                ''',
                'tracked_object',
                'Cisco-IOS-XR-ipv4-vrrp-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-vrrp-cfg',
            'tracked-objects',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-ipv4-vrrp-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_vrrp_cfg',
        ),
    },
    'Vrrp.Interfaces.Interface.Ipv4.Version2.VirtualRouters.VirtualRouter' : {
        'meta_info' : _MetaInfoClass('Vrrp.Interfaces.Interface.Ipv4.Version2.VirtualRouters.VirtualRouter', REFERENCE_LIST,
            '''The VRRP virtual router being configured''',
            False, 
            [
            _MetaInfoClassMember('vr-id', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('1', '255')], [],
                '''                VRID Virtual Router Identifier
                ''',
                'vr_id',
                'Cisco-IOS-XR-ipv4-vrrp-cfg', True),
            _MetaInfoClassMember('timer', REFERENCE_CLASS, 'Timer', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_vrrp_cfg', 'Vrrp.Interfaces.Interface.Ipv4.Version2.VirtualRouters.VirtualRouter.Timer',
                [], [],
                '''                Set advertisement timer
                ''',
                'timer',
                'Cisco-IOS-XR-ipv4-vrrp-cfg', False),
            _MetaInfoClassMember('secondary-ipv4-addresses', REFERENCE_CLASS, 'SecondaryIpv4Addresses', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_vrrp_cfg', 'Vrrp.Interfaces.Interface.Ipv4.Version2.VirtualRouters.VirtualRouter.SecondaryIpv4Addresses',
                [], [],
                '''                The table of VRRP secondary IPv4 addresses
                ''',
                'secondary_ipv4_addresses',
                'Cisco-IOS-XR-ipv4-vrrp-cfg', False),
            _MetaInfoClassMember('tracks', REFERENCE_CLASS, 'Tracks', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_vrrp_cfg', 'Vrrp.Interfaces.Interface.Ipv4.Version2.VirtualRouters.VirtualRouter.Tracks',
                [], [],
                '''                Track an item, reducing priority if it
                goes down
                ''',
                'tracks',
                'Cisco-IOS-XR-ipv4-vrrp-cfg', False),
            _MetaInfoClassMember('tracked-objects', REFERENCE_CLASS, 'TrackedObjects', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_vrrp_cfg', 'Vrrp.Interfaces.Interface.Ipv4.Version2.VirtualRouters.VirtualRouter.TrackedObjects',
                [], [],
                '''                Track an object, reducing priority if it
                goes down
                ''',
                'tracked_objects',
                'Cisco-IOS-XR-ipv4-vrrp-cfg', False),
            _MetaInfoClassMember('priority', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('1', '254')], [],
                '''                Priority value
                ''',
                'priority',
                'Cisco-IOS-XR-ipv4-vrrp-cfg', False, default_value="100"),
            _MetaInfoClassMember('primary-ipv4-address', ATTRIBUTE, 'str', 'inet:ipv4-address-no-zone',
                None, None,
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'],
                '''                The Primary VRRP IPv4 address
                ''',
                'primary_ipv4_address',
                'Cisco-IOS-XR-ipv4-vrrp-cfg', False),
            _MetaInfoClassMember('preempt', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('0', '3600')], [],
                '''                Preempt Master router if higher priority
                ''',
                'preempt',
                'Cisco-IOS-XR-ipv4-vrrp-cfg', False, default_value="0"),
            _MetaInfoClassMember('text-password', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                Authentication password, 8 chars max
                ''',
                'text_password',
                'Cisco-IOS-XR-ipv4-vrrp-cfg', False),
            _MetaInfoClassMember('bfd', ATTRIBUTE, 'str', 'inet:ipv4-address-no-zone',
                None, None,
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'],
                '''                Enable use of Bidirectional Forwarding
                Detection for this IP
                ''',
                'bfd',
                'Cisco-IOS-XR-ipv4-vrrp-cfg', False),
            _MetaInfoClassMember('session-name', ATTRIBUTE, 'str', 'xr:Cisco-ios-xr-string',
                None, None,
                [(1, 16)], [],
                '''                VRRP Session Name
                ''',
                'session_name',
                'Cisco-IOS-XR-ipv4-vrrp-cfg', False),
            _MetaInfoClassMember('accept-mode-disable', ATTRIBUTE, 'Empty', 'empty',
                None, None,
                [], [],
                '''                Disable Accept Mode for this virtual
                IPAddress
                ''',
                'accept_mode_disable',
                'Cisco-IOS-XR-ipv4-vrrp-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-vrrp-cfg',
            'virtual-router',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-ipv4-vrrp-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_vrrp_cfg',
        ),
    },
    'Vrrp.Interfaces.Interface.Ipv4.Version2.VirtualRouters' : {
        'meta_info' : _MetaInfoClass('Vrrp.Interfaces.Interface.Ipv4.Version2.VirtualRouters', REFERENCE_CLASS,
            '''The VRRP virtual router configuration table''',
            False, 
            [
            _MetaInfoClassMember('virtual-router', REFERENCE_LIST, 'VirtualRouter', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_vrrp_cfg', 'Vrrp.Interfaces.Interface.Ipv4.Version2.VirtualRouters.VirtualRouter',
                [], [],
                '''                The VRRP virtual router being configured
                ''',
                'virtual_router',
                'Cisco-IOS-XR-ipv4-vrrp-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-vrrp-cfg',
            'virtual-routers',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-ipv4-vrrp-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_vrrp_cfg',
        ),
    },
    'Vrrp.Interfaces.Interface.Ipv4.Version2' : {
        'meta_info' : _MetaInfoClass('Vrrp.Interfaces.Interface.Ipv4.Version2', REFERENCE_CLASS,
            '''Version 2 VRRP configuration''',
            False, 
            [
            _MetaInfoClassMember('virtual-routers', REFERENCE_CLASS, 'VirtualRouters', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_vrrp_cfg', 'Vrrp.Interfaces.Interface.Ipv4.Version2.VirtualRouters',
                [], [],
                '''                The VRRP virtual router configuration table
                ''',
                'virtual_routers',
                'Cisco-IOS-XR-ipv4-vrrp-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-vrrp-cfg',
            'version2',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-ipv4-vrrp-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_vrrp_cfg',
        ),
    },
    'Vrrp.Interfaces.Interface.Ipv4' : {
        'meta_info' : _MetaInfoClass('Vrrp.Interfaces.Interface.Ipv4', REFERENCE_CLASS,
            '''IPv4 VRRP configuration''',
            False, 
            [
            _MetaInfoClassMember('version3', REFERENCE_CLASS, 'Version3', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_vrrp_cfg', 'Vrrp.Interfaces.Interface.Ipv4.Version3',
                [], [],
                '''                Version 3 VRRP configuration
                ''',
                'version3',
                'Cisco-IOS-XR-ipv4-vrrp-cfg', False),
            _MetaInfoClassMember('slave-virtual-routers', REFERENCE_CLASS, 'SlaveVirtualRouters', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_vrrp_cfg', 'Vrrp.Interfaces.Interface.Ipv4.SlaveVirtualRouters',
                [], [],
                '''                The VRRP slave group configuration table
                ''',
                'slave_virtual_routers',
                'Cisco-IOS-XR-ipv4-vrrp-cfg', False),
            _MetaInfoClassMember('version2', REFERENCE_CLASS, 'Version2', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_vrrp_cfg', 'Vrrp.Interfaces.Interface.Ipv4.Version2',
                [], [],
                '''                Version 2 VRRP configuration
                ''',
                'version2',
                'Cisco-IOS-XR-ipv4-vrrp-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-vrrp-cfg',
            'ipv4',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-ipv4-vrrp-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_vrrp_cfg',
        ),
    },
    'Vrrp.Interfaces.Interface.Bfd' : {
        'meta_info' : _MetaInfoClass('Vrrp.Interfaces.Interface.Bfd', REFERENCE_CLASS,
            '''BFD configuration''',
            False, 
            [
            _MetaInfoClassMember('interval', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('3', '30000')], [],
                '''                Hello interval for BFD sessions created by
                vrrp
                ''',
                'interval',
                'Cisco-IOS-XR-ipv4-vrrp-cfg', False),
            _MetaInfoClassMember('detection-multiplier', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('2', '50')], [],
                '''                Detection multiplier for BFD sessions created
                by vrrp
                ''',
                'detection_multiplier',
                'Cisco-IOS-XR-ipv4-vrrp-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-vrrp-cfg',
            'bfd',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-ipv4-vrrp-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_vrrp_cfg',
        ),
    },
    'Vrrp.Interfaces.Interface' : {
        'meta_info' : _MetaInfoClass('Vrrp.Interfaces.Interface', REFERENCE_LIST,
            '''The interface being configured''',
            False, 
            [
            _MetaInfoClassMember('interface-name', ATTRIBUTE, 'str', 'xr:Interface-name',
                None, None,
                [], [b'[a-zA-Z0-9._/-]+'],
                '''                Interface name to configure
                ''',
                'interface_name',
                'Cisco-IOS-XR-ipv4-vrrp-cfg', True),
            _MetaInfoClassMember('ipv6', REFERENCE_CLASS, 'Ipv6', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_vrrp_cfg', 'Vrrp.Interfaces.Interface.Ipv6',
                [], [],
                '''                IPv6 VRRP configuration
                ''',
                'ipv6',
                'Cisco-IOS-XR-ipv4-vrrp-cfg', False),
            _MetaInfoClassMember('delay', REFERENCE_CLASS, 'Delay', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_vrrp_cfg', 'Vrrp.Interfaces.Interface.Delay',
                [], [],
                '''                Minimum and Reload Delay
                ''',
                'delay',
                'Cisco-IOS-XR-ipv4-vrrp-cfg', False, is_presence=True),
            _MetaInfoClassMember('ipv4', REFERENCE_CLASS, 'Ipv4', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_vrrp_cfg', 'Vrrp.Interfaces.Interface.Ipv4',
                [], [],
                '''                IPv4 VRRP configuration
                ''',
                'ipv4',
                'Cisco-IOS-XR-ipv4-vrrp-cfg', False),
            _MetaInfoClassMember('bfd', REFERENCE_CLASS, 'Bfd', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_vrrp_cfg', 'Vrrp.Interfaces.Interface.Bfd',
                [], [],
                '''                BFD configuration
                ''',
                'bfd',
                'Cisco-IOS-XR-ipv4-vrrp-cfg', False),
            _MetaInfoClassMember('mac-refresh', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('0', '10000')], [],
                '''                VRRP Slave MAC-refresh rate in seconds
                ''',
                'mac_refresh',
                'Cisco-IOS-XR-ipv4-vrrp-cfg', False, default_value="60"),
            ],
            'Cisco-IOS-XR-ipv4-vrrp-cfg',
            'interface',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-ipv4-vrrp-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_vrrp_cfg',
        ),
    },
    'Vrrp.Interfaces' : {
        'meta_info' : _MetaInfoClass('Vrrp.Interfaces', REFERENCE_CLASS,
            '''Interface configuration table''',
            False, 
            [
            _MetaInfoClassMember('interface', REFERENCE_LIST, 'Interface', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_vrrp_cfg', 'Vrrp.Interfaces.Interface',
                [], [],
                '''                The interface being configured
                ''',
                'interface',
                'Cisco-IOS-XR-ipv4-vrrp-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-vrrp-cfg',
            'interfaces',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-ipv4-vrrp-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_vrrp_cfg',
        ),
    },
    'Vrrp' : {
        'meta_info' : _MetaInfoClass('Vrrp', REFERENCE_CLASS,
            '''VRRP configuration''',
            False, 
            [
            _MetaInfoClassMember('logging', REFERENCE_CLASS, 'Logging', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_vrrp_cfg', 'Vrrp.Logging',
                [], [],
                '''                VRRP logging options
                ''',
                'logging',
                'Cisco-IOS-XR-ipv4-vrrp-cfg', False),
            _MetaInfoClassMember('interfaces', REFERENCE_CLASS, 'Interfaces', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_vrrp_cfg', 'Vrrp.Interfaces',
                [], [],
                '''                Interface configuration table
                ''',
                'interfaces',
                'Cisco-IOS-XR-ipv4-vrrp-cfg', False),
            _MetaInfoClassMember('enable', ATTRIBUTE, 'Empty', 'empty',
                None, None,
                [], [],
                '''                Enable vrrp process
                ''',
                'enable',
                'Cisco-IOS-XR-ipv4-vrrp-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-vrrp-cfg',
            'vrrp',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-ipv4-vrrp-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_vrrp_cfg',
        ),
    },
}
_meta_table['Vrrp.Interfaces.Interface.Ipv6.Version3.VirtualRouters.VirtualRouter.GlobalIpv6Addresses.GlobalIpv6Address']['meta_info'].parent =_meta_table['Vrrp.Interfaces.Interface.Ipv6.Version3.VirtualRouters.VirtualRouter.GlobalIpv6Addresses']['meta_info']
_meta_table['Vrrp.Interfaces.Interface.Ipv6.Version3.VirtualRouters.VirtualRouter.Tracks.Track']['meta_info'].parent =_meta_table['Vrrp.Interfaces.Interface.Ipv6.Version3.VirtualRouters.VirtualRouter.Tracks']['meta_info']
_meta_table['Vrrp.Interfaces.Interface.Ipv6.Version3.VirtualRouters.VirtualRouter.TrackedObjects.TrackedObject']['meta_info'].parent =_meta_table['Vrrp.Interfaces.Interface.Ipv6.Version3.VirtualRouters.VirtualRouter.TrackedObjects']['meta_info']
_meta_table['Vrrp.Interfaces.Interface.Ipv6.Version3.VirtualRouters.VirtualRouter.GlobalIpv6Addresses']['meta_info'].parent =_meta_table['Vrrp.Interfaces.Interface.Ipv6.Version3.VirtualRouters.VirtualRouter']['meta_info']
_meta_table['Vrrp.Interfaces.Interface.Ipv6.Version3.VirtualRouters.VirtualRouter.Tracks']['meta_info'].parent =_meta_table['Vrrp.Interfaces.Interface.Ipv6.Version3.VirtualRouters.VirtualRouter']['meta_info']
_meta_table['Vrrp.Interfaces.Interface.Ipv6.Version3.VirtualRouters.VirtualRouter.Timer']['meta_info'].parent =_meta_table['Vrrp.Interfaces.Interface.Ipv6.Version3.VirtualRouters.VirtualRouter']['meta_info']
_meta_table['Vrrp.Interfaces.Interface.Ipv6.Version3.VirtualRouters.VirtualRouter.TrackedObjects']['meta_info'].parent =_meta_table['Vrrp.Interfaces.Interface.Ipv6.Version3.VirtualRouters.VirtualRouter']['meta_info']
_meta_table['Vrrp.Interfaces.Interface.Ipv6.Version3.VirtualRouters.VirtualRouter.LinkLocalIpv6Address']['meta_info'].parent =_meta_table['Vrrp.Interfaces.Interface.Ipv6.Version3.VirtualRouters.VirtualRouter']['meta_info']
_meta_table['Vrrp.Interfaces.Interface.Ipv6.Version3.VirtualRouters.VirtualRouter']['meta_info'].parent =_meta_table['Vrrp.Interfaces.Interface.Ipv6.Version3.VirtualRouters']['meta_info']
_meta_table['Vrrp.Interfaces.Interface.Ipv6.Version3.VirtualRouters']['meta_info'].parent =_meta_table['Vrrp.Interfaces.Interface.Ipv6.Version3']['meta_info']
_meta_table['Vrrp.Interfaces.Interface.Ipv6.SlaveVirtualRouters.SlaveVirtualRouter.GlobalIpv6Addresses.GlobalIpv6Address']['meta_info'].parent =_meta_table['Vrrp.Interfaces.Interface.Ipv6.SlaveVirtualRouters.SlaveVirtualRouter.GlobalIpv6Addresses']['meta_info']
_meta_table['Vrrp.Interfaces.Interface.Ipv6.SlaveVirtualRouters.SlaveVirtualRouter.LinkLocalIpv6Address']['meta_info'].parent =_meta_table['Vrrp.Interfaces.Interface.Ipv6.SlaveVirtualRouters.SlaveVirtualRouter']['meta_info']
_meta_table['Vrrp.Interfaces.Interface.Ipv6.SlaveVirtualRouters.SlaveVirtualRouter.GlobalIpv6Addresses']['meta_info'].parent =_meta_table['Vrrp.Interfaces.Interface.Ipv6.SlaveVirtualRouters.SlaveVirtualRouter']['meta_info']
_meta_table['Vrrp.Interfaces.Interface.Ipv6.SlaveVirtualRouters.SlaveVirtualRouter']['meta_info'].parent =_meta_table['Vrrp.Interfaces.Interface.Ipv6.SlaveVirtualRouters']['meta_info']
_meta_table['Vrrp.Interfaces.Interface.Ipv6.Version3']['meta_info'].parent =_meta_table['Vrrp.Interfaces.Interface.Ipv6']['meta_info']
_meta_table['Vrrp.Interfaces.Interface.Ipv6.SlaveVirtualRouters']['meta_info'].parent =_meta_table['Vrrp.Interfaces.Interface.Ipv6']['meta_info']
_meta_table['Vrrp.Interfaces.Interface.Ipv4.Version3.VirtualRouters.VirtualRouter.SecondaryIpv4Addresses.SecondaryIpv4Address']['meta_info'].parent =_meta_table['Vrrp.Interfaces.Interface.Ipv4.Version3.VirtualRouters.VirtualRouter.SecondaryIpv4Addresses']['meta_info']
_meta_table['Vrrp.Interfaces.Interface.Ipv4.Version3.VirtualRouters.VirtualRouter.TrackedObjects.TrackedObject']['meta_info'].parent =_meta_table['Vrrp.Interfaces.Interface.Ipv4.Version3.VirtualRouters.VirtualRouter.TrackedObjects']['meta_info']
_meta_table['Vrrp.Interfaces.Interface.Ipv4.Version3.VirtualRouters.VirtualRouter.Tracks.Track']['meta_info'].parent =_meta_table['Vrrp.Interfaces.Interface.Ipv4.Version3.VirtualRouters.VirtualRouter.Tracks']['meta_info']
_meta_table['Vrrp.Interfaces.Interface.Ipv4.Version3.VirtualRouters.VirtualRouter.Timer']['meta_info'].parent =_meta_table['Vrrp.Interfaces.Interface.Ipv4.Version3.VirtualRouters.VirtualRouter']['meta_info']
_meta_table['Vrrp.Interfaces.Interface.Ipv4.Version3.VirtualRouters.VirtualRouter.SecondaryIpv4Addresses']['meta_info'].parent =_meta_table['Vrrp.Interfaces.Interface.Ipv4.Version3.VirtualRouters.VirtualRouter']['meta_info']
_meta_table['Vrrp.Interfaces.Interface.Ipv4.Version3.VirtualRouters.VirtualRouter.TrackedObjects']['meta_info'].parent =_meta_table['Vrrp.Interfaces.Interface.Ipv4.Version3.VirtualRouters.VirtualRouter']['meta_info']
_meta_table['Vrrp.Interfaces.Interface.Ipv4.Version3.VirtualRouters.VirtualRouter.Tracks']['meta_info'].parent =_meta_table['Vrrp.Interfaces.Interface.Ipv4.Version3.VirtualRouters.VirtualRouter']['meta_info']
_meta_table['Vrrp.Interfaces.Interface.Ipv4.Version3.VirtualRouters.VirtualRouter']['meta_info'].parent =_meta_table['Vrrp.Interfaces.Interface.Ipv4.Version3.VirtualRouters']['meta_info']
_meta_table['Vrrp.Interfaces.Interface.Ipv4.Version3.VirtualRouters']['meta_info'].parent =_meta_table['Vrrp.Interfaces.Interface.Ipv4.Version3']['meta_info']
_meta_table['Vrrp.Interfaces.Interface.Ipv4.SlaveVirtualRouters.SlaveVirtualRouter.SecondaryIpv4Addresses.SecondaryIpv4Address']['meta_info'].parent =_meta_table['Vrrp.Interfaces.Interface.Ipv4.SlaveVirtualRouters.SlaveVirtualRouter.SecondaryIpv4Addresses']['meta_info']
_meta_table['Vrrp.Interfaces.Interface.Ipv4.SlaveVirtualRouters.SlaveVirtualRouter.SecondaryIpv4Addresses']['meta_info'].parent =_meta_table['Vrrp.Interfaces.Interface.Ipv4.SlaveVirtualRouters.SlaveVirtualRouter']['meta_info']
_meta_table['Vrrp.Interfaces.Interface.Ipv4.SlaveVirtualRouters.SlaveVirtualRouter']['meta_info'].parent =_meta_table['Vrrp.Interfaces.Interface.Ipv4.SlaveVirtualRouters']['meta_info']
_meta_table['Vrrp.Interfaces.Interface.Ipv4.Version2.VirtualRouters.VirtualRouter.SecondaryIpv4Addresses.SecondaryIpv4Address']['meta_info'].parent =_meta_table['Vrrp.Interfaces.Interface.Ipv4.Version2.VirtualRouters.VirtualRouter.SecondaryIpv4Addresses']['meta_info']
_meta_table['Vrrp.Interfaces.Interface.Ipv4.Version2.VirtualRouters.VirtualRouter.Tracks.Track']['meta_info'].parent =_meta_table['Vrrp.Interfaces.Interface.Ipv4.Version2.VirtualRouters.VirtualRouter.Tracks']['meta_info']
_meta_table['Vrrp.Interfaces.Interface.Ipv4.Version2.VirtualRouters.VirtualRouter.TrackedObjects.TrackedObject']['meta_info'].parent =_meta_table['Vrrp.Interfaces.Interface.Ipv4.Version2.VirtualRouters.VirtualRouter.TrackedObjects']['meta_info']
_meta_table['Vrrp.Interfaces.Interface.Ipv4.Version2.VirtualRouters.VirtualRouter.Timer']['meta_info'].parent =_meta_table['Vrrp.Interfaces.Interface.Ipv4.Version2.VirtualRouters.VirtualRouter']['meta_info']
_meta_table['Vrrp.Interfaces.Interface.Ipv4.Version2.VirtualRouters.VirtualRouter.SecondaryIpv4Addresses']['meta_info'].parent =_meta_table['Vrrp.Interfaces.Interface.Ipv4.Version2.VirtualRouters.VirtualRouter']['meta_info']
_meta_table['Vrrp.Interfaces.Interface.Ipv4.Version2.VirtualRouters.VirtualRouter.Tracks']['meta_info'].parent =_meta_table['Vrrp.Interfaces.Interface.Ipv4.Version2.VirtualRouters.VirtualRouter']['meta_info']
_meta_table['Vrrp.Interfaces.Interface.Ipv4.Version2.VirtualRouters.VirtualRouter.TrackedObjects']['meta_info'].parent =_meta_table['Vrrp.Interfaces.Interface.Ipv4.Version2.VirtualRouters.VirtualRouter']['meta_info']
_meta_table['Vrrp.Interfaces.Interface.Ipv4.Version2.VirtualRouters.VirtualRouter']['meta_info'].parent =_meta_table['Vrrp.Interfaces.Interface.Ipv4.Version2.VirtualRouters']['meta_info']
_meta_table['Vrrp.Interfaces.Interface.Ipv4.Version2.VirtualRouters']['meta_info'].parent =_meta_table['Vrrp.Interfaces.Interface.Ipv4.Version2']['meta_info']
_meta_table['Vrrp.Interfaces.Interface.Ipv4.Version3']['meta_info'].parent =_meta_table['Vrrp.Interfaces.Interface.Ipv4']['meta_info']
_meta_table['Vrrp.Interfaces.Interface.Ipv4.SlaveVirtualRouters']['meta_info'].parent =_meta_table['Vrrp.Interfaces.Interface.Ipv4']['meta_info']
_meta_table['Vrrp.Interfaces.Interface.Ipv4.Version2']['meta_info'].parent =_meta_table['Vrrp.Interfaces.Interface.Ipv4']['meta_info']
_meta_table['Vrrp.Interfaces.Interface.Ipv6']['meta_info'].parent =_meta_table['Vrrp.Interfaces.Interface']['meta_info']
_meta_table['Vrrp.Interfaces.Interface.Delay']['meta_info'].parent =_meta_table['Vrrp.Interfaces.Interface']['meta_info']
_meta_table['Vrrp.Interfaces.Interface.Ipv4']['meta_info'].parent =_meta_table['Vrrp.Interfaces.Interface']['meta_info']
_meta_table['Vrrp.Interfaces.Interface.Bfd']['meta_info'].parent =_meta_table['Vrrp.Interfaces.Interface']['meta_info']
_meta_table['Vrrp.Interfaces.Interface']['meta_info'].parent =_meta_table['Vrrp.Interfaces']['meta_info']
_meta_table['Vrrp.Logging']['meta_info'].parent =_meta_table['Vrrp']['meta_info']
_meta_table['Vrrp.Interfaces']['meta_info'].parent =_meta_table['Vrrp']['meta_info']
