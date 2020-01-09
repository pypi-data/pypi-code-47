
'''
This is auto-generated file,
which includes metadata for module Cisco_IOS_XR_ipv4_hsrp_cfg
'''

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_LIST, REFERENCE_LEAFLIST, REFERENCE_BITS, REFERENCE_UNION
from ydk._core._dm_meta_info import REFERENCE_CLASS, REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, ANYXML_CLASS
from ydk._core._importer import _yang_ns

_meta_table = {
    'HsrpLinklocal' : _MetaInfoEnum('HsrpLinklocal',
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_hsrp_cfg', 'HsrpLinklocal',
        '''Hsrp linklocal''',
        {
            'manual':'manual',
            'auto':'auto',
            'legacy':'legacy',
        }, 'Cisco-IOS-XR-ipv4-hsrp-cfg', _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-ipv4-hsrp-cfg']),
    'Hsrp.Interfaces.Interface.Ipv6.Version2.Groups.Group.Bfd' : {
        'meta_info' : _MetaInfoClass('Hsrp.Interfaces.Interface.Ipv6.Version2.Groups.Group.Bfd', REFERENCE_CLASS,
            '''Enable use of Bidirectional Forwarding
Detection''',
            False, 
            [
            _MetaInfoClassMember('address', ATTRIBUTE, 'str', 'inet:ipv6-address-no-zone',
                None, None,
                [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'],
                '''                Enable BFD for this remote IP
                ''',
                'address',
                'Cisco-IOS-XR-ipv4-hsrp-cfg', False),
            _MetaInfoClassMember('interface-name', ATTRIBUTE, 'str', 'xr:Interface-name',
                None, None,
                [], [b'[a-zA-Z0-9._/-]+'],
                '''                Interface name to run BFD
                ''',
                'interface_name',
                'Cisco-IOS-XR-ipv4-hsrp-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-hsrp-cfg',
            'bfd',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-ipv4-hsrp-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_hsrp_cfg',
        ),
    },
    'Hsrp.Interfaces.Interface.Ipv6.Version2.Groups.Group.TrackedInterfaces.TrackedInterface' : {
        'meta_info' : _MetaInfoClass('Hsrp.Interfaces.Interface.Ipv6.Version2.Groups.Group.TrackedInterfaces.TrackedInterface', REFERENCE_LIST,
            '''Interface being tracked''',
            False, 
            [
            _MetaInfoClassMember('interface-name', ATTRIBUTE, 'str', 'xr:Interface-name',
                None, None,
                [], [b'[a-zA-Z0-9._/-]+'],
                '''                Interface being tracked
                ''',
                'interface_name',
                'Cisco-IOS-XR-ipv4-hsrp-cfg', True),
            _MetaInfoClassMember('priority-decrement', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('1', '255')], [],
                '''                Priority decrement
                ''',
                'priority_decrement',
                'Cisco-IOS-XR-ipv4-hsrp-cfg', False, is_mandatory=True),
            ],
            'Cisco-IOS-XR-ipv4-hsrp-cfg',
            'tracked-interface',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-ipv4-hsrp-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_hsrp_cfg',
        ),
    },
    'Hsrp.Interfaces.Interface.Ipv6.Version2.Groups.Group.TrackedInterfaces' : {
        'meta_info' : _MetaInfoClass('Hsrp.Interfaces.Interface.Ipv6.Version2.Groups.Group.TrackedInterfaces', REFERENCE_CLASS,
            '''The HSRP tracked interface configuration
table''',
            False, 
            [
            _MetaInfoClassMember('tracked-interface', REFERENCE_LIST, 'TrackedInterface', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_hsrp_cfg', 'Hsrp.Interfaces.Interface.Ipv6.Version2.Groups.Group.TrackedInterfaces.TrackedInterface',
                [], [],
                '''                Interface being tracked
                ''',
                'tracked_interface',
                'Cisco-IOS-XR-ipv4-hsrp-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-hsrp-cfg',
            'tracked-interfaces',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-ipv4-hsrp-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_hsrp_cfg',
        ),
    },
    'Hsrp.Interfaces.Interface.Ipv6.Version2.Groups.Group.TrackedObjects.TrackedObject' : {
        'meta_info' : _MetaInfoClass('Hsrp.Interfaces.Interface.Ipv6.Version2.Groups.Group.TrackedObjects.TrackedObject', REFERENCE_LIST,
            '''Object being tracked''',
            False, 
            [
            _MetaInfoClassMember('object-name', ATTRIBUTE, 'str', 'xr:Cisco-ios-xr-string',
                None, None,
                [], [b'[\\w\\-\\.:,_@#%$\\+=\\|;]+'],
                '''                Interface being tracked
                ''',
                'object_name',
                'Cisco-IOS-XR-ipv4-hsrp-cfg', True),
            _MetaInfoClassMember('priority-decrement', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('1', '255')], [],
                '''                Priority decrement
                ''',
                'priority_decrement',
                'Cisco-IOS-XR-ipv4-hsrp-cfg', False, is_mandatory=True),
            ],
            'Cisco-IOS-XR-ipv4-hsrp-cfg',
            'tracked-object',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-ipv4-hsrp-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_hsrp_cfg',
        ),
    },
    'Hsrp.Interfaces.Interface.Ipv6.Version2.Groups.Group.TrackedObjects' : {
        'meta_info' : _MetaInfoClass('Hsrp.Interfaces.Interface.Ipv6.Version2.Groups.Group.TrackedObjects', REFERENCE_CLASS,
            '''The HSRP tracked interface configuration
table''',
            False, 
            [
            _MetaInfoClassMember('tracked-object', REFERENCE_LIST, 'TrackedObject', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_hsrp_cfg', 'Hsrp.Interfaces.Interface.Ipv6.Version2.Groups.Group.TrackedObjects.TrackedObject',
                [], [],
                '''                Object being tracked
                ''',
                'tracked_object',
                'Cisco-IOS-XR-ipv4-hsrp-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-hsrp-cfg',
            'tracked-objects',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-ipv4-hsrp-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_hsrp_cfg',
        ),
    },
    'Hsrp.Interfaces.Interface.Ipv6.Version2.Groups.Group.Timers' : {
        'meta_info' : _MetaInfoClass('Hsrp.Interfaces.Interface.Ipv6.Version2.Groups.Group.Timers', REFERENCE_CLASS,
            '''Hello and hold timers''',
            False, 
            [
            _MetaInfoClassMember('hello-msec-flag', ATTRIBUTE, 'bool', 'boolean',
                None, None,
                [], [],
                '''                TRUE - Hello time configured in
                milliseconds, FALSE - Hello time
                configured in seconds
                ''',
                'hello_msec_flag',
                'Cisco-IOS-XR-ipv4-hsrp-cfg', False, default_value='False'),
            _MetaInfoClassMember('hello-msec', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('100', '3000')], [],
                '''                Hello time in msecs
                ''',
                'hello_msec',
                'Cisco-IOS-XR-ipv4-hsrp-cfg', False),
            _MetaInfoClassMember('hello-sec', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('1', '255')], [],
                '''                Hello time in seconds
                ''',
                'hello_sec',
                'Cisco-IOS-XR-ipv4-hsrp-cfg', False, default_value="3"),
            _MetaInfoClassMember('hold-msec-flag', ATTRIBUTE, 'bool', 'boolean',
                None, None,
                [], [],
                '''                TRUE - Hold time configured in
                milliseconds, FALSE - Hold time
                configured in seconds
                ''',
                'hold_msec_flag',
                'Cisco-IOS-XR-ipv4-hsrp-cfg', False, default_value='False'),
            _MetaInfoClassMember('hold-msec', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('100', '3000')], [],
                '''                Hold time in msecs
                ''',
                'hold_msec',
                'Cisco-IOS-XR-ipv4-hsrp-cfg', False),
            _MetaInfoClassMember('hold-sec', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('1', '255')], [],
                '''                Hold time in seconds
                ''',
                'hold_sec',
                'Cisco-IOS-XR-ipv4-hsrp-cfg', False, default_value="10"),
            ],
            'Cisco-IOS-XR-ipv4-hsrp-cfg',
            'timers',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-ipv4-hsrp-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_hsrp_cfg',
        ),
    },
    'Hsrp.Interfaces.Interface.Ipv6.Version2.Groups.Group.LinkLocalIpv6Address' : {
        'meta_info' : _MetaInfoClass('Hsrp.Interfaces.Interface.Ipv6.Version2.Groups.Group.LinkLocalIpv6Address', REFERENCE_CLASS,
            '''The HSRP IPv6 virtual linklocal address''',
            False, 
            [
            _MetaInfoClassMember('address', ATTRIBUTE, 'str', 'inet:ipv6-address-no-zone',
                None, None,
                [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'],
                '''                HSRP IPv6 virtual linklocal address
                ''',
                'address',
                'Cisco-IOS-XR-ipv4-hsrp-cfg', False, has_when=True),
            _MetaInfoClassMember('auto-configure', REFERENCE_ENUM_CLASS, 'HsrpLinklocal', 'Hsrp-linklocal',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_hsrp_cfg', 'HsrpLinklocal',
                [], [],
                '''                Linklocal Configuration Type
                ''',
                'auto_configure',
                'Cisco-IOS-XR-ipv4-hsrp-cfg', False, default_value='Cisco_IOS_XR_ipv4_hsrp_cfg.HsrpLinklocal.manual'),
            ],
            'Cisco-IOS-XR-ipv4-hsrp-cfg',
            'link-local-ipv6-address',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-ipv4-hsrp-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_hsrp_cfg',
        ),
    },
    'Hsrp.Interfaces.Interface.Ipv6.Version2.Groups.Group.GlobalIpv6Addresses.GlobalIpv6Address' : {
        'meta_info' : _MetaInfoClass('Hsrp.Interfaces.Interface.Ipv6.Version2.Groups.Group.GlobalIpv6Addresses.GlobalIpv6Address', REFERENCE_LIST,
            '''A HSRP virtual global IPv6 IP address''',
            False, 
            [
            _MetaInfoClassMember('address', ATTRIBUTE, 'str', 'inet:ipv6-address-no-zone',
                None, None,
                [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'],
                '''                HSRP virtual global IPv6 address
                ''',
                'address',
                'Cisco-IOS-XR-ipv4-hsrp-cfg', True),
            ],
            'Cisco-IOS-XR-ipv4-hsrp-cfg',
            'global-ipv6-address',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-ipv4-hsrp-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_hsrp_cfg',
        ),
    },
    'Hsrp.Interfaces.Interface.Ipv6.Version2.Groups.Group.GlobalIpv6Addresses' : {
        'meta_info' : _MetaInfoClass('Hsrp.Interfaces.Interface.Ipv6.Version2.Groups.Group.GlobalIpv6Addresses', REFERENCE_CLASS,
            '''The table of HSRP virtual global IPv6
addresses''',
            False, 
            [
            _MetaInfoClassMember('global-ipv6-address', REFERENCE_LIST, 'GlobalIpv6Address', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_hsrp_cfg', 'Hsrp.Interfaces.Interface.Ipv6.Version2.Groups.Group.GlobalIpv6Addresses.GlobalIpv6Address',
                [], [],
                '''                A HSRP virtual global IPv6 IP address
                ''',
                'global_ipv6_address',
                'Cisco-IOS-XR-ipv4-hsrp-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-hsrp-cfg',
            'global-ipv6-addresses',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-ipv4-hsrp-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_hsrp_cfg',
        ),
    },
    'Hsrp.Interfaces.Interface.Ipv6.Version2.Groups.Group' : {
        'meta_info' : _MetaInfoClass('Hsrp.Interfaces.Interface.Ipv6.Version2.Groups.Group', REFERENCE_LIST,
            '''The HSRP group being configured''',
            False, 
            [
            _MetaInfoClassMember('group-number', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('0', '4095')], [],
                '''                HSRP group number
                ''',
                'group_number',
                'Cisco-IOS-XR-ipv4-hsrp-cfg', True),
            _MetaInfoClassMember('bfd', REFERENCE_CLASS, 'Bfd', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_hsrp_cfg', 'Hsrp.Interfaces.Interface.Ipv6.Version2.Groups.Group.Bfd',
                [], [],
                '''                Enable use of Bidirectional Forwarding
                Detection
                ''',
                'bfd',
                'Cisco-IOS-XR-ipv4-hsrp-cfg', False),
            _MetaInfoClassMember('tracked-interfaces', REFERENCE_CLASS, 'TrackedInterfaces', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_hsrp_cfg', 'Hsrp.Interfaces.Interface.Ipv6.Version2.Groups.Group.TrackedInterfaces',
                [], [],
                '''                The HSRP tracked interface configuration
                table
                ''',
                'tracked_interfaces',
                'Cisco-IOS-XR-ipv4-hsrp-cfg', False),
            _MetaInfoClassMember('tracked-objects', REFERENCE_CLASS, 'TrackedObjects', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_hsrp_cfg', 'Hsrp.Interfaces.Interface.Ipv6.Version2.Groups.Group.TrackedObjects',
                [], [],
                '''                The HSRP tracked interface configuration
                table
                ''',
                'tracked_objects',
                'Cisco-IOS-XR-ipv4-hsrp-cfg', False),
            _MetaInfoClassMember('timers', REFERENCE_CLASS, 'Timers', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_hsrp_cfg', 'Hsrp.Interfaces.Interface.Ipv6.Version2.Groups.Group.Timers',
                [], [],
                '''                Hello and hold timers
                ''',
                'timers',
                'Cisco-IOS-XR-ipv4-hsrp-cfg', False),
            _MetaInfoClassMember('link-local-ipv6-address', REFERENCE_CLASS, 'LinkLocalIpv6Address', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_hsrp_cfg', 'Hsrp.Interfaces.Interface.Ipv6.Version2.Groups.Group.LinkLocalIpv6Address',
                [], [],
                '''                The HSRP IPv6 virtual linklocal address
                ''',
                'link_local_ipv6_address',
                'Cisco-IOS-XR-ipv4-hsrp-cfg', False),
            _MetaInfoClassMember('global-ipv6-addresses', REFERENCE_CLASS, 'GlobalIpv6Addresses', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_hsrp_cfg', 'Hsrp.Interfaces.Interface.Ipv6.Version2.Groups.Group.GlobalIpv6Addresses',
                [], [],
                '''                The table of HSRP virtual global IPv6
                addresses
                ''',
                'global_ipv6_addresses',
                'Cisco-IOS-XR-ipv4-hsrp-cfg', False),
            _MetaInfoClassMember('priority', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('0', '255')], [],
                '''                Priority value
                ''',
                'priority',
                'Cisco-IOS-XR-ipv4-hsrp-cfg', False, default_value="100"),
            _MetaInfoClassMember('preempt', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('0', '4294967295')], [],
                '''                Force active if higher priority
                ''',
                'preempt',
                'Cisco-IOS-XR-ipv4-hsrp-cfg', False, default_value="0"),
            _MetaInfoClassMember('session-name', ATTRIBUTE, 'str', 'xr:Cisco-ios-xr-string',
                None, None,
                [(1, 16)], [],
                '''                HSRP Session name (for MGO)
                ''',
                'session_name',
                'Cisco-IOS-XR-ipv4-hsrp-cfg', False),
            _MetaInfoClassMember('virtual-mac-address', ATTRIBUTE, 'str', 'yang:mac-address',
                None, None,
                [], [b'[0-9a-fA-F]{2}(:[0-9a-fA-F]{2}){5}'],
                '''                HSRP MAC address
                ''',
                'virtual_mac_address',
                'Cisco-IOS-XR-ipv4-hsrp-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-hsrp-cfg',
            'group',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-ipv4-hsrp-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_hsrp_cfg',
        ),
    },
    'Hsrp.Interfaces.Interface.Ipv6.Version2.Groups' : {
        'meta_info' : _MetaInfoClass('Hsrp.Interfaces.Interface.Ipv6.Version2.Groups', REFERENCE_CLASS,
            '''The HSRP group configuration table''',
            False, 
            [
            _MetaInfoClassMember('group', REFERENCE_LIST, 'Group', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_hsrp_cfg', 'Hsrp.Interfaces.Interface.Ipv6.Version2.Groups.Group',
                [], [],
                '''                The HSRP group being configured
                ''',
                'group',
                'Cisco-IOS-XR-ipv4-hsrp-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-hsrp-cfg',
            'groups',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-ipv4-hsrp-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_hsrp_cfg',
        ),
    },
    'Hsrp.Interfaces.Interface.Ipv6.Version2' : {
        'meta_info' : _MetaInfoClass('Hsrp.Interfaces.Interface.Ipv6.Version2', REFERENCE_CLASS,
            '''Version 2 HSRP configuration''',
            False, 
            [
            _MetaInfoClassMember('groups', REFERENCE_CLASS, 'Groups', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_hsrp_cfg', 'Hsrp.Interfaces.Interface.Ipv6.Version2.Groups',
                [], [],
                '''                The HSRP group configuration table
                ''',
                'groups',
                'Cisco-IOS-XR-ipv4-hsrp-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-hsrp-cfg',
            'version2',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-ipv4-hsrp-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_hsrp_cfg',
        ),
    },
    'Hsrp.Interfaces.Interface.Ipv6.SlaveGroups.SlaveGroup.LinkLocalIpv6Address' : {
        'meta_info' : _MetaInfoClass('Hsrp.Interfaces.Interface.Ipv6.SlaveGroups.SlaveGroup.LinkLocalIpv6Address', REFERENCE_CLASS,
            '''The HSRP IPv6 virtual linklocal address''',
            False, 
            [
            _MetaInfoClassMember('address', ATTRIBUTE, 'str', 'inet:ipv6-address-no-zone',
                None, None,
                [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'],
                '''                HSRP IPv6 virtual linklocal address
                ''',
                'address',
                'Cisco-IOS-XR-ipv4-hsrp-cfg', False, has_when=True),
            _MetaInfoClassMember('auto-configure', REFERENCE_ENUM_CLASS, 'HsrpLinklocal', 'Hsrp-linklocal',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_hsrp_cfg', 'HsrpLinklocal',
                [], [],
                '''                Linklocal Configuration Type
                ''',
                'auto_configure',
                'Cisco-IOS-XR-ipv4-hsrp-cfg', False, default_value='Cisco_IOS_XR_ipv4_hsrp_cfg.HsrpLinklocal.manual'),
            ],
            'Cisco-IOS-XR-ipv4-hsrp-cfg',
            'link-local-ipv6-address',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-ipv4-hsrp-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_hsrp_cfg',
        ),
    },
    'Hsrp.Interfaces.Interface.Ipv6.SlaveGroups.SlaveGroup.GlobalIpv6Addresses.GlobalIpv6Address' : {
        'meta_info' : _MetaInfoClass('Hsrp.Interfaces.Interface.Ipv6.SlaveGroups.SlaveGroup.GlobalIpv6Addresses.GlobalIpv6Address', REFERENCE_LIST,
            '''A HSRP virtual global IPv6 IP address''',
            False, 
            [
            _MetaInfoClassMember('address', ATTRIBUTE, 'str', 'inet:ipv6-address-no-zone',
                None, None,
                [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'],
                '''                HSRP virtual global IPv6 address
                ''',
                'address',
                'Cisco-IOS-XR-ipv4-hsrp-cfg', True),
            ],
            'Cisco-IOS-XR-ipv4-hsrp-cfg',
            'global-ipv6-address',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-ipv4-hsrp-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_hsrp_cfg',
        ),
    },
    'Hsrp.Interfaces.Interface.Ipv6.SlaveGroups.SlaveGroup.GlobalIpv6Addresses' : {
        'meta_info' : _MetaInfoClass('Hsrp.Interfaces.Interface.Ipv6.SlaveGroups.SlaveGroup.GlobalIpv6Addresses', REFERENCE_CLASS,
            '''The table of HSRP virtual global IPv6
addresses''',
            False, 
            [
            _MetaInfoClassMember('global-ipv6-address', REFERENCE_LIST, 'GlobalIpv6Address', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_hsrp_cfg', 'Hsrp.Interfaces.Interface.Ipv6.SlaveGroups.SlaveGroup.GlobalIpv6Addresses.GlobalIpv6Address',
                [], [],
                '''                A HSRP virtual global IPv6 IP address
                ''',
                'global_ipv6_address',
                'Cisco-IOS-XR-ipv4-hsrp-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-hsrp-cfg',
            'global-ipv6-addresses',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-ipv4-hsrp-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_hsrp_cfg',
        ),
    },
    'Hsrp.Interfaces.Interface.Ipv6.SlaveGroups.SlaveGroup' : {
        'meta_info' : _MetaInfoClass('Hsrp.Interfaces.Interface.Ipv6.SlaveGroups.SlaveGroup', REFERENCE_LIST,
            '''The HSRP slave group being configured''',
            False, 
            [
            _MetaInfoClassMember('slave-group-number', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('0', '4095')], [],
                '''                HSRP group number
                ''',
                'slave_group_number',
                'Cisco-IOS-XR-ipv4-hsrp-cfg', True),
            _MetaInfoClassMember('link-local-ipv6-address', REFERENCE_CLASS, 'LinkLocalIpv6Address', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_hsrp_cfg', 'Hsrp.Interfaces.Interface.Ipv6.SlaveGroups.SlaveGroup.LinkLocalIpv6Address',
                [], [],
                '''                The HSRP IPv6 virtual linklocal address
                ''',
                'link_local_ipv6_address',
                'Cisco-IOS-XR-ipv4-hsrp-cfg', False),
            _MetaInfoClassMember('global-ipv6-addresses', REFERENCE_CLASS, 'GlobalIpv6Addresses', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_hsrp_cfg', 'Hsrp.Interfaces.Interface.Ipv6.SlaveGroups.SlaveGroup.GlobalIpv6Addresses',
                [], [],
                '''                The table of HSRP virtual global IPv6
                addresses
                ''',
                'global_ipv6_addresses',
                'Cisco-IOS-XR-ipv4-hsrp-cfg', False),
            _MetaInfoClassMember('follow', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                HSRP Group name for this slave to follow
                ''',
                'follow',
                'Cisco-IOS-XR-ipv4-hsrp-cfg', False),
            _MetaInfoClassMember('virtual-mac-address', ATTRIBUTE, 'str', 'yang:mac-address',
                None, None,
                [], [b'[0-9a-fA-F]{2}(:[0-9a-fA-F]{2}){5}'],
                '''                HSRP MAC address
                ''',
                'virtual_mac_address',
                'Cisco-IOS-XR-ipv4-hsrp-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-hsrp-cfg',
            'slave-group',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-ipv4-hsrp-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_hsrp_cfg',
        ),
    },
    'Hsrp.Interfaces.Interface.Ipv6.SlaveGroups' : {
        'meta_info' : _MetaInfoClass('Hsrp.Interfaces.Interface.Ipv6.SlaveGroups', REFERENCE_CLASS,
            '''The HSRP slave group configuration table''',
            False, 
            [
            _MetaInfoClassMember('slave-group', REFERENCE_LIST, 'SlaveGroup', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_hsrp_cfg', 'Hsrp.Interfaces.Interface.Ipv6.SlaveGroups.SlaveGroup',
                [], [],
                '''                The HSRP slave group being configured
                ''',
                'slave_group',
                'Cisco-IOS-XR-ipv4-hsrp-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-hsrp-cfg',
            'slave-groups',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-ipv4-hsrp-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_hsrp_cfg',
        ),
    },
    'Hsrp.Interfaces.Interface.Ipv6' : {
        'meta_info' : _MetaInfoClass('Hsrp.Interfaces.Interface.Ipv6', REFERENCE_CLASS,
            '''IPv6 HSRP configuration''',
            False, 
            [
            _MetaInfoClassMember('version2', REFERENCE_CLASS, 'Version2', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_hsrp_cfg', 'Hsrp.Interfaces.Interface.Ipv6.Version2',
                [], [],
                '''                Version 2 HSRP configuration
                ''',
                'version2',
                'Cisco-IOS-XR-ipv4-hsrp-cfg', False),
            _MetaInfoClassMember('slave-groups', REFERENCE_CLASS, 'SlaveGroups', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_hsrp_cfg', 'Hsrp.Interfaces.Interface.Ipv6.SlaveGroups',
                [], [],
                '''                The HSRP slave group configuration table
                ''',
                'slave_groups',
                'Cisco-IOS-XR-ipv4-hsrp-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-hsrp-cfg',
            'ipv6',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-ipv4-hsrp-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_hsrp_cfg',
        ),
    },
    'Hsrp.Interfaces.Interface.Bfd' : {
        'meta_info' : _MetaInfoClass('Hsrp.Interfaces.Interface.Bfd', REFERENCE_CLASS,
            '''BFD configuration''',
            False, 
            [
            _MetaInfoClassMember('detection-multiplier', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('2', '50')], [],
                '''                Detection multiplier for BFD sessions created
                by hsrp
                ''',
                'detection_multiplier',
                'Cisco-IOS-XR-ipv4-hsrp-cfg', False),
            _MetaInfoClassMember('interval', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('3', '30000')], [],
                '''                Hello interval for BFD sessions created by
                hsrp
                ''',
                'interval',
                'Cisco-IOS-XR-ipv4-hsrp-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-hsrp-cfg',
            'bfd',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-ipv4-hsrp-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_hsrp_cfg',
        ),
    },
    'Hsrp.Interfaces.Interface.Delay' : {
        'meta_info' : _MetaInfoClass('Hsrp.Interfaces.Interface.Delay', REFERENCE_CLASS,
            '''Minimum and Reload Delay''',
            False, 
            [
            _MetaInfoClassMember('minimum-delay', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('0', '10000')], [],
                '''                Minimum delay in seconds
                ''',
                'minimum_delay',
                'Cisco-IOS-XR-ipv4-hsrp-cfg', False, is_mandatory=True),
            _MetaInfoClassMember('reload-delay', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('0', '10000')], [],
                '''                Reload delay in seconds
                ''',
                'reload_delay',
                'Cisco-IOS-XR-ipv4-hsrp-cfg', False, is_mandatory=True),
            ],
            'Cisco-IOS-XR-ipv4-hsrp-cfg',
            'delay',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-ipv4-hsrp-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_hsrp_cfg',
            is_presence=True,
        ),
    },
    'Hsrp.Interfaces.Interface.Ipv4.SlaveGroups.SlaveGroup.SecondaryIpv4Addresses.SecondaryIpv4Address' : {
        'meta_info' : _MetaInfoClass('Hsrp.Interfaces.Interface.Ipv4.SlaveGroups.SlaveGroup.SecondaryIpv4Addresses.SecondaryIpv4Address', REFERENCE_LIST,
            '''Secondary HSRP IP address''',
            False, 
            [
            _MetaInfoClassMember('address', ATTRIBUTE, 'str', 'inet:ipv4-address-no-zone',
                None, None,
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'],
                '''                HSRP IP address
                ''',
                'address',
                'Cisco-IOS-XR-ipv4-hsrp-cfg', True),
            ],
            'Cisco-IOS-XR-ipv4-hsrp-cfg',
            'secondary-ipv4-address',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-ipv4-hsrp-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_hsrp_cfg',
        ),
    },
    'Hsrp.Interfaces.Interface.Ipv4.SlaveGroups.SlaveGroup.SecondaryIpv4Addresses' : {
        'meta_info' : _MetaInfoClass('Hsrp.Interfaces.Interface.Ipv4.SlaveGroups.SlaveGroup.SecondaryIpv4Addresses', REFERENCE_CLASS,
            '''Secondary HSRP IP address Table''',
            False, 
            [
            _MetaInfoClassMember('secondary-ipv4-address', REFERENCE_LIST, 'SecondaryIpv4Address', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_hsrp_cfg', 'Hsrp.Interfaces.Interface.Ipv4.SlaveGroups.SlaveGroup.SecondaryIpv4Addresses.SecondaryIpv4Address',
                [], [],
                '''                Secondary HSRP IP address
                ''',
                'secondary_ipv4_address',
                'Cisco-IOS-XR-ipv4-hsrp-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-hsrp-cfg',
            'secondary-ipv4-addresses',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-ipv4-hsrp-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_hsrp_cfg',
        ),
    },
    'Hsrp.Interfaces.Interface.Ipv4.SlaveGroups.SlaveGroup' : {
        'meta_info' : _MetaInfoClass('Hsrp.Interfaces.Interface.Ipv4.SlaveGroups.SlaveGroup', REFERENCE_LIST,
            '''The HSRP slave group being configured''',
            False, 
            [
            _MetaInfoClassMember('slave-group-number', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('0', '4095')], [],
                '''                HSRP group number
                ''',
                'slave_group_number',
                'Cisco-IOS-XR-ipv4-hsrp-cfg', True),
            _MetaInfoClassMember('secondary-ipv4-addresses', REFERENCE_CLASS, 'SecondaryIpv4Addresses', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_hsrp_cfg', 'Hsrp.Interfaces.Interface.Ipv4.SlaveGroups.SlaveGroup.SecondaryIpv4Addresses',
                [], [],
                '''                Secondary HSRP IP address Table
                ''',
                'secondary_ipv4_addresses',
                'Cisco-IOS-XR-ipv4-hsrp-cfg', False),
            _MetaInfoClassMember('follow', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                HSRP Group name for this slave to follow
                ''',
                'follow',
                'Cisco-IOS-XR-ipv4-hsrp-cfg', False),
            _MetaInfoClassMember('virtual-mac-address', ATTRIBUTE, 'str', 'yang:mac-address',
                None, None,
                [], [b'[0-9a-fA-F]{2}(:[0-9a-fA-F]{2}){5}'],
                '''                HSRP MAC address
                ''',
                'virtual_mac_address',
                'Cisco-IOS-XR-ipv4-hsrp-cfg', False),
            _MetaInfoClassMember('primary-ipv4-address', ATTRIBUTE, 'str', 'inet:ipv4-address-no-zone',
                None, None,
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'],
                '''                Primary HSRP IP address
                ''',
                'primary_ipv4_address',
                'Cisco-IOS-XR-ipv4-hsrp-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-hsrp-cfg',
            'slave-group',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-ipv4-hsrp-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_hsrp_cfg',
        ),
    },
    'Hsrp.Interfaces.Interface.Ipv4.SlaveGroups' : {
        'meta_info' : _MetaInfoClass('Hsrp.Interfaces.Interface.Ipv4.SlaveGroups', REFERENCE_CLASS,
            '''The HSRP slave group configuration table''',
            False, 
            [
            _MetaInfoClassMember('slave-group', REFERENCE_LIST, 'SlaveGroup', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_hsrp_cfg', 'Hsrp.Interfaces.Interface.Ipv4.SlaveGroups.SlaveGroup',
                [], [],
                '''                The HSRP slave group being configured
                ''',
                'slave_group',
                'Cisco-IOS-XR-ipv4-hsrp-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-hsrp-cfg',
            'slave-groups',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-ipv4-hsrp-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_hsrp_cfg',
        ),
    },
    'Hsrp.Interfaces.Interface.Ipv4.Version1.Groups.Group.TrackedInterfaces.TrackedInterface' : {
        'meta_info' : _MetaInfoClass('Hsrp.Interfaces.Interface.Ipv4.Version1.Groups.Group.TrackedInterfaces.TrackedInterface', REFERENCE_LIST,
            '''Interface being tracked''',
            False, 
            [
            _MetaInfoClassMember('interface-name', ATTRIBUTE, 'str', 'xr:Interface-name',
                None, None,
                [], [b'[a-zA-Z0-9._/-]+'],
                '''                Interface being tracked
                ''',
                'interface_name',
                'Cisco-IOS-XR-ipv4-hsrp-cfg', True),
            _MetaInfoClassMember('priority-decrement', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('1', '255')], [],
                '''                Priority decrement
                ''',
                'priority_decrement',
                'Cisco-IOS-XR-ipv4-hsrp-cfg', False, is_mandatory=True),
            ],
            'Cisco-IOS-XR-ipv4-hsrp-cfg',
            'tracked-interface',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-ipv4-hsrp-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_hsrp_cfg',
        ),
    },
    'Hsrp.Interfaces.Interface.Ipv4.Version1.Groups.Group.TrackedInterfaces' : {
        'meta_info' : _MetaInfoClass('Hsrp.Interfaces.Interface.Ipv4.Version1.Groups.Group.TrackedInterfaces', REFERENCE_CLASS,
            '''The HSRP tracked interface configuration
table''',
            False, 
            [
            _MetaInfoClassMember('tracked-interface', REFERENCE_LIST, 'TrackedInterface', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_hsrp_cfg', 'Hsrp.Interfaces.Interface.Ipv4.Version1.Groups.Group.TrackedInterfaces.TrackedInterface',
                [], [],
                '''                Interface being tracked
                ''',
                'tracked_interface',
                'Cisco-IOS-XR-ipv4-hsrp-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-hsrp-cfg',
            'tracked-interfaces',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-ipv4-hsrp-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_hsrp_cfg',
        ),
    },
    'Hsrp.Interfaces.Interface.Ipv4.Version1.Groups.Group.Bfd' : {
        'meta_info' : _MetaInfoClass('Hsrp.Interfaces.Interface.Ipv4.Version1.Groups.Group.Bfd', REFERENCE_CLASS,
            '''Enable use of Bidirectional Forwarding
Detection''',
            False, 
            [
            _MetaInfoClassMember('address', ATTRIBUTE, 'str', 'inet:ipv4-address-no-zone',
                None, None,
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'],
                '''                Enable BFD for this remote IP
                ''',
                'address',
                'Cisco-IOS-XR-ipv4-hsrp-cfg', False),
            _MetaInfoClassMember('interface-name', ATTRIBUTE, 'str', 'xr:Interface-name',
                None, None,
                [], [b'[a-zA-Z0-9._/-]+'],
                '''                Interface name to run BFD
                ''',
                'interface_name',
                'Cisco-IOS-XR-ipv4-hsrp-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-hsrp-cfg',
            'bfd',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-ipv4-hsrp-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_hsrp_cfg',
        ),
    },
    'Hsrp.Interfaces.Interface.Ipv4.Version1.Groups.Group.TrackedObjects.TrackedObject' : {
        'meta_info' : _MetaInfoClass('Hsrp.Interfaces.Interface.Ipv4.Version1.Groups.Group.TrackedObjects.TrackedObject', REFERENCE_LIST,
            '''Object being tracked''',
            False, 
            [
            _MetaInfoClassMember('object-name', ATTRIBUTE, 'str', 'xr:Cisco-ios-xr-string',
                None, None,
                [], [b'[\\w\\-\\.:,_@#%$\\+=\\|;]+'],
                '''                Interface being tracked
                ''',
                'object_name',
                'Cisco-IOS-XR-ipv4-hsrp-cfg', True),
            _MetaInfoClassMember('priority-decrement', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('1', '255')], [],
                '''                Priority decrement
                ''',
                'priority_decrement',
                'Cisco-IOS-XR-ipv4-hsrp-cfg', False, is_mandatory=True),
            ],
            'Cisco-IOS-XR-ipv4-hsrp-cfg',
            'tracked-object',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-ipv4-hsrp-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_hsrp_cfg',
        ),
    },
    'Hsrp.Interfaces.Interface.Ipv4.Version1.Groups.Group.TrackedObjects' : {
        'meta_info' : _MetaInfoClass('Hsrp.Interfaces.Interface.Ipv4.Version1.Groups.Group.TrackedObjects', REFERENCE_CLASS,
            '''The HSRP tracked interface configuration
table''',
            False, 
            [
            _MetaInfoClassMember('tracked-object', REFERENCE_LIST, 'TrackedObject', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_hsrp_cfg', 'Hsrp.Interfaces.Interface.Ipv4.Version1.Groups.Group.TrackedObjects.TrackedObject',
                [], [],
                '''                Object being tracked
                ''',
                'tracked_object',
                'Cisco-IOS-XR-ipv4-hsrp-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-hsrp-cfg',
            'tracked-objects',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-ipv4-hsrp-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_hsrp_cfg',
        ),
    },
    'Hsrp.Interfaces.Interface.Ipv4.Version1.Groups.Group.Timers' : {
        'meta_info' : _MetaInfoClass('Hsrp.Interfaces.Interface.Ipv4.Version1.Groups.Group.Timers', REFERENCE_CLASS,
            '''Hello and hold timers''',
            False, 
            [
            _MetaInfoClassMember('hello-msec-flag', ATTRIBUTE, 'bool', 'boolean',
                None, None,
                [], [],
                '''                TRUE - Hello time configured in
                milliseconds, FALSE - Hello time
                configured in seconds
                ''',
                'hello_msec_flag',
                'Cisco-IOS-XR-ipv4-hsrp-cfg', False, default_value='False'),
            _MetaInfoClassMember('hello-msec', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('100', '3000')], [],
                '''                Hello time in msecs
                ''',
                'hello_msec',
                'Cisco-IOS-XR-ipv4-hsrp-cfg', False),
            _MetaInfoClassMember('hello-sec', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('1', '255')], [],
                '''                Hello time in seconds
                ''',
                'hello_sec',
                'Cisco-IOS-XR-ipv4-hsrp-cfg', False, default_value="3"),
            _MetaInfoClassMember('hold-msec-flag', ATTRIBUTE, 'bool', 'boolean',
                None, None,
                [], [],
                '''                TRUE - Hold time configured in
                milliseconds, FALSE - Hold time
                configured in seconds
                ''',
                'hold_msec_flag',
                'Cisco-IOS-XR-ipv4-hsrp-cfg', False, default_value='False'),
            _MetaInfoClassMember('hold-msec', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('100', '3000')], [],
                '''                Hold time in msecs
                ''',
                'hold_msec',
                'Cisco-IOS-XR-ipv4-hsrp-cfg', False),
            _MetaInfoClassMember('hold-sec', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('1', '255')], [],
                '''                Hold time in seconds
                ''',
                'hold_sec',
                'Cisco-IOS-XR-ipv4-hsrp-cfg', False, default_value="10"),
            ],
            'Cisco-IOS-XR-ipv4-hsrp-cfg',
            'timers',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-ipv4-hsrp-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_hsrp_cfg',
        ),
    },
    'Hsrp.Interfaces.Interface.Ipv4.Version1.Groups.Group.PrimaryIpv4Address' : {
        'meta_info' : _MetaInfoClass('Hsrp.Interfaces.Interface.Ipv4.Version1.Groups.Group.PrimaryIpv4Address', REFERENCE_CLASS,
            '''Primary HSRP IP address''',
            False, 
            [
            _MetaInfoClassMember('virtual-ip-learn', ATTRIBUTE, 'bool', 'boolean',
                None, None,
                [], [],
                '''                TRUE if the HSRP protocol is to learn the
                virtual IP address it is to use
                ''',
                'virtual_ip_learn',
                'Cisco-IOS-XR-ipv4-hsrp-cfg', False),
            _MetaInfoClassMember('address', ATTRIBUTE, 'str', 'inet:ipv4-address-no-zone',
                None, None,
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'],
                '''                HSRP IP address.
                ''',
                'address',
                'Cisco-IOS-XR-ipv4-hsrp-cfg', False, has_when=True),
            ],
            'Cisco-IOS-XR-ipv4-hsrp-cfg',
            'primary-ipv4-address',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-ipv4-hsrp-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_hsrp_cfg',
        ),
    },
    'Hsrp.Interfaces.Interface.Ipv4.Version1.Groups.Group.SecondaryIpv4Addresses.SecondaryIpv4Address' : {
        'meta_info' : _MetaInfoClass('Hsrp.Interfaces.Interface.Ipv4.Version1.Groups.Group.SecondaryIpv4Addresses.SecondaryIpv4Address', REFERENCE_LIST,
            '''Secondary HSRP IP address''',
            False, 
            [
            _MetaInfoClassMember('address', ATTRIBUTE, 'str', 'inet:ipv4-address-no-zone',
                None, None,
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'],
                '''                HSRP IP address
                ''',
                'address',
                'Cisco-IOS-XR-ipv4-hsrp-cfg', True),
            ],
            'Cisco-IOS-XR-ipv4-hsrp-cfg',
            'secondary-ipv4-address',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-ipv4-hsrp-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_hsrp_cfg',
        ),
    },
    'Hsrp.Interfaces.Interface.Ipv4.Version1.Groups.Group.SecondaryIpv4Addresses' : {
        'meta_info' : _MetaInfoClass('Hsrp.Interfaces.Interface.Ipv4.Version1.Groups.Group.SecondaryIpv4Addresses', REFERENCE_CLASS,
            '''Secondary HSRP IP address Table''',
            False, 
            [
            _MetaInfoClassMember('secondary-ipv4-address', REFERENCE_LIST, 'SecondaryIpv4Address', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_hsrp_cfg', 'Hsrp.Interfaces.Interface.Ipv4.Version1.Groups.Group.SecondaryIpv4Addresses.SecondaryIpv4Address',
                [], [],
                '''                Secondary HSRP IP address
                ''',
                'secondary_ipv4_address',
                'Cisco-IOS-XR-ipv4-hsrp-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-hsrp-cfg',
            'secondary-ipv4-addresses',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-ipv4-hsrp-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_hsrp_cfg',
        ),
    },
    'Hsrp.Interfaces.Interface.Ipv4.Version1.Groups.Group' : {
        'meta_info' : _MetaInfoClass('Hsrp.Interfaces.Interface.Ipv4.Version1.Groups.Group', REFERENCE_LIST,
            '''The HSRP group being configured''',
            False, 
            [
            _MetaInfoClassMember('group-number', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('0', '255')], [],
                '''                HSRP group number
                ''',
                'group_number',
                'Cisco-IOS-XR-ipv4-hsrp-cfg', True),
            _MetaInfoClassMember('tracked-interfaces', REFERENCE_CLASS, 'TrackedInterfaces', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_hsrp_cfg', 'Hsrp.Interfaces.Interface.Ipv4.Version1.Groups.Group.TrackedInterfaces',
                [], [],
                '''                The HSRP tracked interface configuration
                table
                ''',
                'tracked_interfaces',
                'Cisco-IOS-XR-ipv4-hsrp-cfg', False),
            _MetaInfoClassMember('bfd', REFERENCE_CLASS, 'Bfd', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_hsrp_cfg', 'Hsrp.Interfaces.Interface.Ipv4.Version1.Groups.Group.Bfd',
                [], [],
                '''                Enable use of Bidirectional Forwarding
                Detection
                ''',
                'bfd',
                'Cisco-IOS-XR-ipv4-hsrp-cfg', False),
            _MetaInfoClassMember('tracked-objects', REFERENCE_CLASS, 'TrackedObjects', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_hsrp_cfg', 'Hsrp.Interfaces.Interface.Ipv4.Version1.Groups.Group.TrackedObjects',
                [], [],
                '''                The HSRP tracked interface configuration
                table
                ''',
                'tracked_objects',
                'Cisco-IOS-XR-ipv4-hsrp-cfg', False),
            _MetaInfoClassMember('timers', REFERENCE_CLASS, 'Timers', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_hsrp_cfg', 'Hsrp.Interfaces.Interface.Ipv4.Version1.Groups.Group.Timers',
                [], [],
                '''                Hello and hold timers
                ''',
                'timers',
                'Cisco-IOS-XR-ipv4-hsrp-cfg', False),
            _MetaInfoClassMember('primary-ipv4-address', REFERENCE_CLASS, 'PrimaryIpv4Address', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_hsrp_cfg', 'Hsrp.Interfaces.Interface.Ipv4.Version1.Groups.Group.PrimaryIpv4Address',
                [], [],
                '''                Primary HSRP IP address
                ''',
                'primary_ipv4_address',
                'Cisco-IOS-XR-ipv4-hsrp-cfg', False),
            _MetaInfoClassMember('secondary-ipv4-addresses', REFERENCE_CLASS, 'SecondaryIpv4Addresses', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_hsrp_cfg', 'Hsrp.Interfaces.Interface.Ipv4.Version1.Groups.Group.SecondaryIpv4Addresses',
                [], [],
                '''                Secondary HSRP IP address Table
                ''',
                'secondary_ipv4_addresses',
                'Cisco-IOS-XR-ipv4-hsrp-cfg', False),
            _MetaInfoClassMember('authentication', ATTRIBUTE, 'str', 'string',
                None, None,
                [(1, 8)], [],
                '''                Authentication string
                ''',
                'authentication',
                'Cisco-IOS-XR-ipv4-hsrp-cfg', False, default_value="'cisco'"),
            _MetaInfoClassMember('session-name', ATTRIBUTE, 'str', 'xr:Cisco-ios-xr-string',
                None, None,
                [(1, 16)], [],
                '''                HSRP Session name (for MGO)
                ''',
                'session_name',
                'Cisco-IOS-XR-ipv4-hsrp-cfg', False),
            _MetaInfoClassMember('priority', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('0', '255')], [],
                '''                Priority value
                ''',
                'priority',
                'Cisco-IOS-XR-ipv4-hsrp-cfg', False, default_value="100"),
            _MetaInfoClassMember('preempt', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('0', '4294967295')], [],
                '''                Force active if higher priority
                ''',
                'preempt',
                'Cisco-IOS-XR-ipv4-hsrp-cfg', False, default_value="0"),
            _MetaInfoClassMember('virtual-mac-address', ATTRIBUTE, 'str', 'yang:mac-address',
                None, None,
                [], [b'[0-9a-fA-F]{2}(:[0-9a-fA-F]{2}){5}'],
                '''                HSRP MAC address
                ''',
                'virtual_mac_address',
                'Cisco-IOS-XR-ipv4-hsrp-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-hsrp-cfg',
            'group',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-ipv4-hsrp-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_hsrp_cfg',
        ),
    },
    'Hsrp.Interfaces.Interface.Ipv4.Version1.Groups' : {
        'meta_info' : _MetaInfoClass('Hsrp.Interfaces.Interface.Ipv4.Version1.Groups', REFERENCE_CLASS,
            '''The HSRP group configuration table''',
            False, 
            [
            _MetaInfoClassMember('group', REFERENCE_LIST, 'Group', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_hsrp_cfg', 'Hsrp.Interfaces.Interface.Ipv4.Version1.Groups.Group',
                [], [],
                '''                The HSRP group being configured
                ''',
                'group',
                'Cisco-IOS-XR-ipv4-hsrp-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-hsrp-cfg',
            'groups',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-ipv4-hsrp-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_hsrp_cfg',
        ),
    },
    'Hsrp.Interfaces.Interface.Ipv4.Version1' : {
        'meta_info' : _MetaInfoClass('Hsrp.Interfaces.Interface.Ipv4.Version1', REFERENCE_CLASS,
            '''Version 1 HSRP configuration''',
            False, 
            [
            _MetaInfoClassMember('groups', REFERENCE_CLASS, 'Groups', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_hsrp_cfg', 'Hsrp.Interfaces.Interface.Ipv4.Version1.Groups',
                [], [],
                '''                The HSRP group configuration table
                ''',
                'groups',
                'Cisco-IOS-XR-ipv4-hsrp-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-hsrp-cfg',
            'version1',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-ipv4-hsrp-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_hsrp_cfg',
        ),
    },
    'Hsrp.Interfaces.Interface.Ipv4.Version2.Groups.Group.SecondaryIpv4Addresses.SecondaryIpv4Address' : {
        'meta_info' : _MetaInfoClass('Hsrp.Interfaces.Interface.Ipv4.Version2.Groups.Group.SecondaryIpv4Addresses.SecondaryIpv4Address', REFERENCE_LIST,
            '''Secondary HSRP IP address''',
            False, 
            [
            _MetaInfoClassMember('address', ATTRIBUTE, 'str', 'inet:ipv4-address-no-zone',
                None, None,
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'],
                '''                HSRP IP address
                ''',
                'address',
                'Cisco-IOS-XR-ipv4-hsrp-cfg', True),
            ],
            'Cisco-IOS-XR-ipv4-hsrp-cfg',
            'secondary-ipv4-address',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-ipv4-hsrp-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_hsrp_cfg',
        ),
    },
    'Hsrp.Interfaces.Interface.Ipv4.Version2.Groups.Group.SecondaryIpv4Addresses' : {
        'meta_info' : _MetaInfoClass('Hsrp.Interfaces.Interface.Ipv4.Version2.Groups.Group.SecondaryIpv4Addresses', REFERENCE_CLASS,
            '''Secondary HSRP IP address Table''',
            False, 
            [
            _MetaInfoClassMember('secondary-ipv4-address', REFERENCE_LIST, 'SecondaryIpv4Address', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_hsrp_cfg', 'Hsrp.Interfaces.Interface.Ipv4.Version2.Groups.Group.SecondaryIpv4Addresses.SecondaryIpv4Address',
                [], [],
                '''                Secondary HSRP IP address
                ''',
                'secondary_ipv4_address',
                'Cisco-IOS-XR-ipv4-hsrp-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-hsrp-cfg',
            'secondary-ipv4-addresses',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-ipv4-hsrp-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_hsrp_cfg',
        ),
    },
    'Hsrp.Interfaces.Interface.Ipv4.Version2.Groups.Group.Bfd' : {
        'meta_info' : _MetaInfoClass('Hsrp.Interfaces.Interface.Ipv4.Version2.Groups.Group.Bfd', REFERENCE_CLASS,
            '''Enable use of Bidirectional Forwarding
Detection''',
            False, 
            [
            _MetaInfoClassMember('address', ATTRIBUTE, 'str', 'inet:ipv4-address-no-zone',
                None, None,
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'],
                '''                Enable BFD for this remote IP
                ''',
                'address',
                'Cisco-IOS-XR-ipv4-hsrp-cfg', False),
            _MetaInfoClassMember('interface-name', ATTRIBUTE, 'str', 'xr:Interface-name',
                None, None,
                [], [b'[a-zA-Z0-9._/-]+'],
                '''                Interface name to run BFD
                ''',
                'interface_name',
                'Cisco-IOS-XR-ipv4-hsrp-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-hsrp-cfg',
            'bfd',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-ipv4-hsrp-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_hsrp_cfg',
        ),
    },
    'Hsrp.Interfaces.Interface.Ipv4.Version2.Groups.Group.PrimaryIpv4Address' : {
        'meta_info' : _MetaInfoClass('Hsrp.Interfaces.Interface.Ipv4.Version2.Groups.Group.PrimaryIpv4Address', REFERENCE_CLASS,
            '''Primary HSRP IP address''',
            False, 
            [
            _MetaInfoClassMember('virtual-ip-learn', ATTRIBUTE, 'bool', 'boolean',
                None, None,
                [], [],
                '''                TRUE if the HSRP protocol is to learn the
                virtual IP address it is to use
                ''',
                'virtual_ip_learn',
                'Cisco-IOS-XR-ipv4-hsrp-cfg', False),
            _MetaInfoClassMember('address', ATTRIBUTE, 'str', 'inet:ipv4-address-no-zone',
                None, None,
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'],
                '''                HSRP IP address.
                ''',
                'address',
                'Cisco-IOS-XR-ipv4-hsrp-cfg', False, has_when=True),
            ],
            'Cisco-IOS-XR-ipv4-hsrp-cfg',
            'primary-ipv4-address',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-ipv4-hsrp-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_hsrp_cfg',
        ),
    },
    'Hsrp.Interfaces.Interface.Ipv4.Version2.Groups.Group.TrackedObjects.TrackedObject' : {
        'meta_info' : _MetaInfoClass('Hsrp.Interfaces.Interface.Ipv4.Version2.Groups.Group.TrackedObjects.TrackedObject', REFERENCE_LIST,
            '''Object being tracked''',
            False, 
            [
            _MetaInfoClassMember('object-name', ATTRIBUTE, 'str', 'xr:Cisco-ios-xr-string',
                None, None,
                [], [b'[\\w\\-\\.:,_@#%$\\+=\\|;]+'],
                '''                Interface being tracked
                ''',
                'object_name',
                'Cisco-IOS-XR-ipv4-hsrp-cfg', True),
            _MetaInfoClassMember('priority-decrement', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('1', '255')], [],
                '''                Priority decrement
                ''',
                'priority_decrement',
                'Cisco-IOS-XR-ipv4-hsrp-cfg', False, is_mandatory=True),
            ],
            'Cisco-IOS-XR-ipv4-hsrp-cfg',
            'tracked-object',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-ipv4-hsrp-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_hsrp_cfg',
        ),
    },
    'Hsrp.Interfaces.Interface.Ipv4.Version2.Groups.Group.TrackedObjects' : {
        'meta_info' : _MetaInfoClass('Hsrp.Interfaces.Interface.Ipv4.Version2.Groups.Group.TrackedObjects', REFERENCE_CLASS,
            '''The HSRP tracked interface configuration
table''',
            False, 
            [
            _MetaInfoClassMember('tracked-object', REFERENCE_LIST, 'TrackedObject', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_hsrp_cfg', 'Hsrp.Interfaces.Interface.Ipv4.Version2.Groups.Group.TrackedObjects.TrackedObject',
                [], [],
                '''                Object being tracked
                ''',
                'tracked_object',
                'Cisco-IOS-XR-ipv4-hsrp-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-hsrp-cfg',
            'tracked-objects',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-ipv4-hsrp-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_hsrp_cfg',
        ),
    },
    'Hsrp.Interfaces.Interface.Ipv4.Version2.Groups.Group.TrackedInterfaces.TrackedInterface' : {
        'meta_info' : _MetaInfoClass('Hsrp.Interfaces.Interface.Ipv4.Version2.Groups.Group.TrackedInterfaces.TrackedInterface', REFERENCE_LIST,
            '''Interface being tracked''',
            False, 
            [
            _MetaInfoClassMember('interface-name', ATTRIBUTE, 'str', 'xr:Interface-name',
                None, None,
                [], [b'[a-zA-Z0-9._/-]+'],
                '''                Interface being tracked
                ''',
                'interface_name',
                'Cisco-IOS-XR-ipv4-hsrp-cfg', True),
            _MetaInfoClassMember('priority-decrement', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('1', '255')], [],
                '''                Priority decrement
                ''',
                'priority_decrement',
                'Cisco-IOS-XR-ipv4-hsrp-cfg', False, is_mandatory=True),
            ],
            'Cisco-IOS-XR-ipv4-hsrp-cfg',
            'tracked-interface',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-ipv4-hsrp-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_hsrp_cfg',
        ),
    },
    'Hsrp.Interfaces.Interface.Ipv4.Version2.Groups.Group.TrackedInterfaces' : {
        'meta_info' : _MetaInfoClass('Hsrp.Interfaces.Interface.Ipv4.Version2.Groups.Group.TrackedInterfaces', REFERENCE_CLASS,
            '''The HSRP tracked interface configuration
table''',
            False, 
            [
            _MetaInfoClassMember('tracked-interface', REFERENCE_LIST, 'TrackedInterface', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_hsrp_cfg', 'Hsrp.Interfaces.Interface.Ipv4.Version2.Groups.Group.TrackedInterfaces.TrackedInterface',
                [], [],
                '''                Interface being tracked
                ''',
                'tracked_interface',
                'Cisco-IOS-XR-ipv4-hsrp-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-hsrp-cfg',
            'tracked-interfaces',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-ipv4-hsrp-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_hsrp_cfg',
        ),
    },
    'Hsrp.Interfaces.Interface.Ipv4.Version2.Groups.Group.Timers' : {
        'meta_info' : _MetaInfoClass('Hsrp.Interfaces.Interface.Ipv4.Version2.Groups.Group.Timers', REFERENCE_CLASS,
            '''Hello and hold timers''',
            False, 
            [
            _MetaInfoClassMember('hello-msec-flag', ATTRIBUTE, 'bool', 'boolean',
                None, None,
                [], [],
                '''                TRUE - Hello time configured in
                milliseconds, FALSE - Hello time
                configured in seconds
                ''',
                'hello_msec_flag',
                'Cisco-IOS-XR-ipv4-hsrp-cfg', False, default_value='False'),
            _MetaInfoClassMember('hello-msec', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('100', '3000')], [],
                '''                Hello time in msecs
                ''',
                'hello_msec',
                'Cisco-IOS-XR-ipv4-hsrp-cfg', False),
            _MetaInfoClassMember('hello-sec', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('1', '255')], [],
                '''                Hello time in seconds
                ''',
                'hello_sec',
                'Cisco-IOS-XR-ipv4-hsrp-cfg', False, default_value="3"),
            _MetaInfoClassMember('hold-msec-flag', ATTRIBUTE, 'bool', 'boolean',
                None, None,
                [], [],
                '''                TRUE - Hold time configured in
                milliseconds, FALSE - Hold time
                configured in seconds
                ''',
                'hold_msec_flag',
                'Cisco-IOS-XR-ipv4-hsrp-cfg', False, default_value='False'),
            _MetaInfoClassMember('hold-msec', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('100', '3000')], [],
                '''                Hold time in msecs
                ''',
                'hold_msec',
                'Cisco-IOS-XR-ipv4-hsrp-cfg', False),
            _MetaInfoClassMember('hold-sec', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('1', '255')], [],
                '''                Hold time in seconds
                ''',
                'hold_sec',
                'Cisco-IOS-XR-ipv4-hsrp-cfg', False, default_value="10"),
            ],
            'Cisco-IOS-XR-ipv4-hsrp-cfg',
            'timers',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-ipv4-hsrp-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_hsrp_cfg',
        ),
    },
    'Hsrp.Interfaces.Interface.Ipv4.Version2.Groups.Group' : {
        'meta_info' : _MetaInfoClass('Hsrp.Interfaces.Interface.Ipv4.Version2.Groups.Group', REFERENCE_LIST,
            '''The HSRP group being configured''',
            False, 
            [
            _MetaInfoClassMember('group-number', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('0', '4095')], [],
                '''                HSRP group number
                ''',
                'group_number',
                'Cisco-IOS-XR-ipv4-hsrp-cfg', True),
            _MetaInfoClassMember('secondary-ipv4-addresses', REFERENCE_CLASS, 'SecondaryIpv4Addresses', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_hsrp_cfg', 'Hsrp.Interfaces.Interface.Ipv4.Version2.Groups.Group.SecondaryIpv4Addresses',
                [], [],
                '''                Secondary HSRP IP address Table
                ''',
                'secondary_ipv4_addresses',
                'Cisco-IOS-XR-ipv4-hsrp-cfg', False),
            _MetaInfoClassMember('bfd', REFERENCE_CLASS, 'Bfd', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_hsrp_cfg', 'Hsrp.Interfaces.Interface.Ipv4.Version2.Groups.Group.Bfd',
                [], [],
                '''                Enable use of Bidirectional Forwarding
                Detection
                ''',
                'bfd',
                'Cisco-IOS-XR-ipv4-hsrp-cfg', False),
            _MetaInfoClassMember('primary-ipv4-address', REFERENCE_CLASS, 'PrimaryIpv4Address', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_hsrp_cfg', 'Hsrp.Interfaces.Interface.Ipv4.Version2.Groups.Group.PrimaryIpv4Address',
                [], [],
                '''                Primary HSRP IP address
                ''',
                'primary_ipv4_address',
                'Cisco-IOS-XR-ipv4-hsrp-cfg', False),
            _MetaInfoClassMember('tracked-objects', REFERENCE_CLASS, 'TrackedObjects', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_hsrp_cfg', 'Hsrp.Interfaces.Interface.Ipv4.Version2.Groups.Group.TrackedObjects',
                [], [],
                '''                The HSRP tracked interface configuration
                table
                ''',
                'tracked_objects',
                'Cisco-IOS-XR-ipv4-hsrp-cfg', False),
            _MetaInfoClassMember('tracked-interfaces', REFERENCE_CLASS, 'TrackedInterfaces', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_hsrp_cfg', 'Hsrp.Interfaces.Interface.Ipv4.Version2.Groups.Group.TrackedInterfaces',
                [], [],
                '''                The HSRP tracked interface configuration
                table
                ''',
                'tracked_interfaces',
                'Cisco-IOS-XR-ipv4-hsrp-cfg', False),
            _MetaInfoClassMember('timers', REFERENCE_CLASS, 'Timers', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_hsrp_cfg', 'Hsrp.Interfaces.Interface.Ipv4.Version2.Groups.Group.Timers',
                [], [],
                '''                Hello and hold timers
                ''',
                'timers',
                'Cisco-IOS-XR-ipv4-hsrp-cfg', False),
            _MetaInfoClassMember('preempt', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('0', '4294967295')], [],
                '''                Force active if higher priority
                ''',
                'preempt',
                'Cisco-IOS-XR-ipv4-hsrp-cfg', False, default_value="0"),
            _MetaInfoClassMember('priority', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('0', '255')], [],
                '''                Priority value
                ''',
                'priority',
                'Cisco-IOS-XR-ipv4-hsrp-cfg', False, default_value="100"),
            _MetaInfoClassMember('virtual-mac-address', ATTRIBUTE, 'str', 'yang:mac-address',
                None, None,
                [], [b'[0-9a-fA-F]{2}(:[0-9a-fA-F]{2}){5}'],
                '''                HSRP MAC address
                ''',
                'virtual_mac_address',
                'Cisco-IOS-XR-ipv4-hsrp-cfg', False),
            _MetaInfoClassMember('session-name', ATTRIBUTE, 'str', 'xr:Cisco-ios-xr-string',
                None, None,
                [(1, 16)], [],
                '''                HSRP Session name (for MGO)
                ''',
                'session_name',
                'Cisco-IOS-XR-ipv4-hsrp-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-hsrp-cfg',
            'group',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-ipv4-hsrp-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_hsrp_cfg',
        ),
    },
    'Hsrp.Interfaces.Interface.Ipv4.Version2.Groups' : {
        'meta_info' : _MetaInfoClass('Hsrp.Interfaces.Interface.Ipv4.Version2.Groups', REFERENCE_CLASS,
            '''The HSRP group configuration table''',
            False, 
            [
            _MetaInfoClassMember('group', REFERENCE_LIST, 'Group', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_hsrp_cfg', 'Hsrp.Interfaces.Interface.Ipv4.Version2.Groups.Group',
                [], [],
                '''                The HSRP group being configured
                ''',
                'group',
                'Cisco-IOS-XR-ipv4-hsrp-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-hsrp-cfg',
            'groups',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-ipv4-hsrp-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_hsrp_cfg',
        ),
    },
    'Hsrp.Interfaces.Interface.Ipv4.Version2' : {
        'meta_info' : _MetaInfoClass('Hsrp.Interfaces.Interface.Ipv4.Version2', REFERENCE_CLASS,
            '''Version 2 HSRP configuration''',
            False, 
            [
            _MetaInfoClassMember('groups', REFERENCE_CLASS, 'Groups', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_hsrp_cfg', 'Hsrp.Interfaces.Interface.Ipv4.Version2.Groups',
                [], [],
                '''                The HSRP group configuration table
                ''',
                'groups',
                'Cisco-IOS-XR-ipv4-hsrp-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-hsrp-cfg',
            'version2',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-ipv4-hsrp-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_hsrp_cfg',
        ),
    },
    'Hsrp.Interfaces.Interface.Ipv4' : {
        'meta_info' : _MetaInfoClass('Hsrp.Interfaces.Interface.Ipv4', REFERENCE_CLASS,
            '''IPv4 HSRP configuration''',
            False, 
            [
            _MetaInfoClassMember('slave-groups', REFERENCE_CLASS, 'SlaveGroups', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_hsrp_cfg', 'Hsrp.Interfaces.Interface.Ipv4.SlaveGroups',
                [], [],
                '''                The HSRP slave group configuration table
                ''',
                'slave_groups',
                'Cisco-IOS-XR-ipv4-hsrp-cfg', False),
            _MetaInfoClassMember('version1', REFERENCE_CLASS, 'Version1', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_hsrp_cfg', 'Hsrp.Interfaces.Interface.Ipv4.Version1',
                [], [],
                '''                Version 1 HSRP configuration
                ''',
                'version1',
                'Cisco-IOS-XR-ipv4-hsrp-cfg', False),
            _MetaInfoClassMember('version2', REFERENCE_CLASS, 'Version2', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_hsrp_cfg', 'Hsrp.Interfaces.Interface.Ipv4.Version2',
                [], [],
                '''                Version 2 HSRP configuration
                ''',
                'version2',
                'Cisco-IOS-XR-ipv4-hsrp-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-hsrp-cfg',
            'ipv4',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-ipv4-hsrp-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_hsrp_cfg',
        ),
    },
    'Hsrp.Interfaces.Interface' : {
        'meta_info' : _MetaInfoClass('Hsrp.Interfaces.Interface', REFERENCE_LIST,
            '''Per-interface HSRP configuration''',
            False, 
            [
            _MetaInfoClassMember('interface-name', ATTRIBUTE, 'str', 'xr:Interface-name',
                None, None,
                [], [b'[a-zA-Z0-9._/-]+'],
                '''                Interface name
                ''',
                'interface_name',
                'Cisco-IOS-XR-ipv4-hsrp-cfg', True),
            _MetaInfoClassMember('ipv6', REFERENCE_CLASS, 'Ipv6', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_hsrp_cfg', 'Hsrp.Interfaces.Interface.Ipv6',
                [], [],
                '''                IPv6 HSRP configuration
                ''',
                'ipv6',
                'Cisco-IOS-XR-ipv4-hsrp-cfg', False),
            _MetaInfoClassMember('bfd', REFERENCE_CLASS, 'Bfd', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_hsrp_cfg', 'Hsrp.Interfaces.Interface.Bfd',
                [], [],
                '''                BFD configuration
                ''',
                'bfd',
                'Cisco-IOS-XR-ipv4-hsrp-cfg', False),
            _MetaInfoClassMember('delay', REFERENCE_CLASS, 'Delay', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_hsrp_cfg', 'Hsrp.Interfaces.Interface.Delay',
                [], [],
                '''                Minimum and Reload Delay
                ''',
                'delay',
                'Cisco-IOS-XR-ipv4-hsrp-cfg', False, is_presence=True),
            _MetaInfoClassMember('ipv4', REFERENCE_CLASS, 'Ipv4', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_hsrp_cfg', 'Hsrp.Interfaces.Interface.Ipv4',
                [], [],
                '''                IPv4 HSRP configuration
                ''',
                'ipv4',
                'Cisco-IOS-XR-ipv4-hsrp-cfg', False),
            _MetaInfoClassMember('mac-refresh', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('0', '10000')], [],
                '''                HSRP MGO slave MAC refresh rate
                ''',
                'mac_refresh',
                'Cisco-IOS-XR-ipv4-hsrp-cfg', False, default_value="60"),
            _MetaInfoClassMember('use-bia', ATTRIBUTE, 'Empty', 'empty',
                None, None,
                [], [],
                '''                Use burned-in address
                ''',
                'use_bia',
                'Cisco-IOS-XR-ipv4-hsrp-cfg', False),
            _MetaInfoClassMember('redirects-disable', ATTRIBUTE, 'Empty', 'empty',
                None, None,
                [], [],
                '''                Disable HSRP filtered ICMP redirects
                ''',
                'redirects_disable',
                'Cisco-IOS-XR-ipv4-hsrp-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-hsrp-cfg',
            'interface',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-ipv4-hsrp-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_hsrp_cfg',
        ),
    },
    'Hsrp.Interfaces' : {
        'meta_info' : _MetaInfoClass('Hsrp.Interfaces', REFERENCE_CLASS,
            '''Interface Table for HSRP configuration''',
            False, 
            [
            _MetaInfoClassMember('interface', REFERENCE_LIST, 'Interface', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_hsrp_cfg', 'Hsrp.Interfaces.Interface',
                [], [],
                '''                Per-interface HSRP configuration
                ''',
                'interface',
                'Cisco-IOS-XR-ipv4-hsrp-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-hsrp-cfg',
            'interfaces',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-ipv4-hsrp-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_hsrp_cfg',
        ),
    },
    'Hsrp.Logging' : {
        'meta_info' : _MetaInfoClass('Hsrp.Logging', REFERENCE_CLASS,
            '''HSRP logging options''',
            False, 
            [
            _MetaInfoClassMember('state-change-disable', ATTRIBUTE, 'Empty', 'empty',
                None, None,
                [], [],
                '''                HSRP state change IOS messages disable
                ''',
                'state_change_disable',
                'Cisco-IOS-XR-ipv4-hsrp-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-hsrp-cfg',
            'logging',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-ipv4-hsrp-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_hsrp_cfg',
        ),
    },
    'Hsrp' : {
        'meta_info' : _MetaInfoClass('Hsrp', REFERENCE_CLASS,
            '''HSRP configuration''',
            False, 
            [
            _MetaInfoClassMember('interfaces', REFERENCE_CLASS, 'Interfaces', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_hsrp_cfg', 'Hsrp.Interfaces',
                [], [],
                '''                Interface Table for HSRP configuration
                ''',
                'interfaces',
                'Cisco-IOS-XR-ipv4-hsrp-cfg', False),
            _MetaInfoClassMember('logging', REFERENCE_CLASS, 'Logging', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_hsrp_cfg', 'Hsrp.Logging',
                [], [],
                '''                HSRP logging options
                ''',
                'logging',
                'Cisco-IOS-XR-ipv4-hsrp-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-hsrp-cfg',
            'hsrp',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-ipv4-hsrp-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_hsrp_cfg',
        ),
    },
}
_meta_table['Hsrp.Interfaces.Interface.Ipv6.Version2.Groups.Group.TrackedInterfaces.TrackedInterface']['meta_info'].parent =_meta_table['Hsrp.Interfaces.Interface.Ipv6.Version2.Groups.Group.TrackedInterfaces']['meta_info']
_meta_table['Hsrp.Interfaces.Interface.Ipv6.Version2.Groups.Group.TrackedObjects.TrackedObject']['meta_info'].parent =_meta_table['Hsrp.Interfaces.Interface.Ipv6.Version2.Groups.Group.TrackedObjects']['meta_info']
_meta_table['Hsrp.Interfaces.Interface.Ipv6.Version2.Groups.Group.GlobalIpv6Addresses.GlobalIpv6Address']['meta_info'].parent =_meta_table['Hsrp.Interfaces.Interface.Ipv6.Version2.Groups.Group.GlobalIpv6Addresses']['meta_info']
_meta_table['Hsrp.Interfaces.Interface.Ipv6.Version2.Groups.Group.Bfd']['meta_info'].parent =_meta_table['Hsrp.Interfaces.Interface.Ipv6.Version2.Groups.Group']['meta_info']
_meta_table['Hsrp.Interfaces.Interface.Ipv6.Version2.Groups.Group.TrackedInterfaces']['meta_info'].parent =_meta_table['Hsrp.Interfaces.Interface.Ipv6.Version2.Groups.Group']['meta_info']
_meta_table['Hsrp.Interfaces.Interface.Ipv6.Version2.Groups.Group.TrackedObjects']['meta_info'].parent =_meta_table['Hsrp.Interfaces.Interface.Ipv6.Version2.Groups.Group']['meta_info']
_meta_table['Hsrp.Interfaces.Interface.Ipv6.Version2.Groups.Group.Timers']['meta_info'].parent =_meta_table['Hsrp.Interfaces.Interface.Ipv6.Version2.Groups.Group']['meta_info']
_meta_table['Hsrp.Interfaces.Interface.Ipv6.Version2.Groups.Group.LinkLocalIpv6Address']['meta_info'].parent =_meta_table['Hsrp.Interfaces.Interface.Ipv6.Version2.Groups.Group']['meta_info']
_meta_table['Hsrp.Interfaces.Interface.Ipv6.Version2.Groups.Group.GlobalIpv6Addresses']['meta_info'].parent =_meta_table['Hsrp.Interfaces.Interface.Ipv6.Version2.Groups.Group']['meta_info']
_meta_table['Hsrp.Interfaces.Interface.Ipv6.Version2.Groups.Group']['meta_info'].parent =_meta_table['Hsrp.Interfaces.Interface.Ipv6.Version2.Groups']['meta_info']
_meta_table['Hsrp.Interfaces.Interface.Ipv6.Version2.Groups']['meta_info'].parent =_meta_table['Hsrp.Interfaces.Interface.Ipv6.Version2']['meta_info']
_meta_table['Hsrp.Interfaces.Interface.Ipv6.SlaveGroups.SlaveGroup.GlobalIpv6Addresses.GlobalIpv6Address']['meta_info'].parent =_meta_table['Hsrp.Interfaces.Interface.Ipv6.SlaveGroups.SlaveGroup.GlobalIpv6Addresses']['meta_info']
_meta_table['Hsrp.Interfaces.Interface.Ipv6.SlaveGroups.SlaveGroup.LinkLocalIpv6Address']['meta_info'].parent =_meta_table['Hsrp.Interfaces.Interface.Ipv6.SlaveGroups.SlaveGroup']['meta_info']
_meta_table['Hsrp.Interfaces.Interface.Ipv6.SlaveGroups.SlaveGroup.GlobalIpv6Addresses']['meta_info'].parent =_meta_table['Hsrp.Interfaces.Interface.Ipv6.SlaveGroups.SlaveGroup']['meta_info']
_meta_table['Hsrp.Interfaces.Interface.Ipv6.SlaveGroups.SlaveGroup']['meta_info'].parent =_meta_table['Hsrp.Interfaces.Interface.Ipv6.SlaveGroups']['meta_info']
_meta_table['Hsrp.Interfaces.Interface.Ipv6.Version2']['meta_info'].parent =_meta_table['Hsrp.Interfaces.Interface.Ipv6']['meta_info']
_meta_table['Hsrp.Interfaces.Interface.Ipv6.SlaveGroups']['meta_info'].parent =_meta_table['Hsrp.Interfaces.Interface.Ipv6']['meta_info']
_meta_table['Hsrp.Interfaces.Interface.Ipv4.SlaveGroups.SlaveGroup.SecondaryIpv4Addresses.SecondaryIpv4Address']['meta_info'].parent =_meta_table['Hsrp.Interfaces.Interface.Ipv4.SlaveGroups.SlaveGroup.SecondaryIpv4Addresses']['meta_info']
_meta_table['Hsrp.Interfaces.Interface.Ipv4.SlaveGroups.SlaveGroup.SecondaryIpv4Addresses']['meta_info'].parent =_meta_table['Hsrp.Interfaces.Interface.Ipv4.SlaveGroups.SlaveGroup']['meta_info']
_meta_table['Hsrp.Interfaces.Interface.Ipv4.SlaveGroups.SlaveGroup']['meta_info'].parent =_meta_table['Hsrp.Interfaces.Interface.Ipv4.SlaveGroups']['meta_info']
_meta_table['Hsrp.Interfaces.Interface.Ipv4.Version1.Groups.Group.TrackedInterfaces.TrackedInterface']['meta_info'].parent =_meta_table['Hsrp.Interfaces.Interface.Ipv4.Version1.Groups.Group.TrackedInterfaces']['meta_info']
_meta_table['Hsrp.Interfaces.Interface.Ipv4.Version1.Groups.Group.TrackedObjects.TrackedObject']['meta_info'].parent =_meta_table['Hsrp.Interfaces.Interface.Ipv4.Version1.Groups.Group.TrackedObjects']['meta_info']
_meta_table['Hsrp.Interfaces.Interface.Ipv4.Version1.Groups.Group.SecondaryIpv4Addresses.SecondaryIpv4Address']['meta_info'].parent =_meta_table['Hsrp.Interfaces.Interface.Ipv4.Version1.Groups.Group.SecondaryIpv4Addresses']['meta_info']
_meta_table['Hsrp.Interfaces.Interface.Ipv4.Version1.Groups.Group.TrackedInterfaces']['meta_info'].parent =_meta_table['Hsrp.Interfaces.Interface.Ipv4.Version1.Groups.Group']['meta_info']
_meta_table['Hsrp.Interfaces.Interface.Ipv4.Version1.Groups.Group.Bfd']['meta_info'].parent =_meta_table['Hsrp.Interfaces.Interface.Ipv4.Version1.Groups.Group']['meta_info']
_meta_table['Hsrp.Interfaces.Interface.Ipv4.Version1.Groups.Group.TrackedObjects']['meta_info'].parent =_meta_table['Hsrp.Interfaces.Interface.Ipv4.Version1.Groups.Group']['meta_info']
_meta_table['Hsrp.Interfaces.Interface.Ipv4.Version1.Groups.Group.Timers']['meta_info'].parent =_meta_table['Hsrp.Interfaces.Interface.Ipv4.Version1.Groups.Group']['meta_info']
_meta_table['Hsrp.Interfaces.Interface.Ipv4.Version1.Groups.Group.PrimaryIpv4Address']['meta_info'].parent =_meta_table['Hsrp.Interfaces.Interface.Ipv4.Version1.Groups.Group']['meta_info']
_meta_table['Hsrp.Interfaces.Interface.Ipv4.Version1.Groups.Group.SecondaryIpv4Addresses']['meta_info'].parent =_meta_table['Hsrp.Interfaces.Interface.Ipv4.Version1.Groups.Group']['meta_info']
_meta_table['Hsrp.Interfaces.Interface.Ipv4.Version1.Groups.Group']['meta_info'].parent =_meta_table['Hsrp.Interfaces.Interface.Ipv4.Version1.Groups']['meta_info']
_meta_table['Hsrp.Interfaces.Interface.Ipv4.Version1.Groups']['meta_info'].parent =_meta_table['Hsrp.Interfaces.Interface.Ipv4.Version1']['meta_info']
_meta_table['Hsrp.Interfaces.Interface.Ipv4.Version2.Groups.Group.SecondaryIpv4Addresses.SecondaryIpv4Address']['meta_info'].parent =_meta_table['Hsrp.Interfaces.Interface.Ipv4.Version2.Groups.Group.SecondaryIpv4Addresses']['meta_info']
_meta_table['Hsrp.Interfaces.Interface.Ipv4.Version2.Groups.Group.TrackedObjects.TrackedObject']['meta_info'].parent =_meta_table['Hsrp.Interfaces.Interface.Ipv4.Version2.Groups.Group.TrackedObjects']['meta_info']
_meta_table['Hsrp.Interfaces.Interface.Ipv4.Version2.Groups.Group.TrackedInterfaces.TrackedInterface']['meta_info'].parent =_meta_table['Hsrp.Interfaces.Interface.Ipv4.Version2.Groups.Group.TrackedInterfaces']['meta_info']
_meta_table['Hsrp.Interfaces.Interface.Ipv4.Version2.Groups.Group.SecondaryIpv4Addresses']['meta_info'].parent =_meta_table['Hsrp.Interfaces.Interface.Ipv4.Version2.Groups.Group']['meta_info']
_meta_table['Hsrp.Interfaces.Interface.Ipv4.Version2.Groups.Group.Bfd']['meta_info'].parent =_meta_table['Hsrp.Interfaces.Interface.Ipv4.Version2.Groups.Group']['meta_info']
_meta_table['Hsrp.Interfaces.Interface.Ipv4.Version2.Groups.Group.PrimaryIpv4Address']['meta_info'].parent =_meta_table['Hsrp.Interfaces.Interface.Ipv4.Version2.Groups.Group']['meta_info']
_meta_table['Hsrp.Interfaces.Interface.Ipv4.Version2.Groups.Group.TrackedObjects']['meta_info'].parent =_meta_table['Hsrp.Interfaces.Interface.Ipv4.Version2.Groups.Group']['meta_info']
_meta_table['Hsrp.Interfaces.Interface.Ipv4.Version2.Groups.Group.TrackedInterfaces']['meta_info'].parent =_meta_table['Hsrp.Interfaces.Interface.Ipv4.Version2.Groups.Group']['meta_info']
_meta_table['Hsrp.Interfaces.Interface.Ipv4.Version2.Groups.Group.Timers']['meta_info'].parent =_meta_table['Hsrp.Interfaces.Interface.Ipv4.Version2.Groups.Group']['meta_info']
_meta_table['Hsrp.Interfaces.Interface.Ipv4.Version2.Groups.Group']['meta_info'].parent =_meta_table['Hsrp.Interfaces.Interface.Ipv4.Version2.Groups']['meta_info']
_meta_table['Hsrp.Interfaces.Interface.Ipv4.Version2.Groups']['meta_info'].parent =_meta_table['Hsrp.Interfaces.Interface.Ipv4.Version2']['meta_info']
_meta_table['Hsrp.Interfaces.Interface.Ipv4.SlaveGroups']['meta_info'].parent =_meta_table['Hsrp.Interfaces.Interface.Ipv4']['meta_info']
_meta_table['Hsrp.Interfaces.Interface.Ipv4.Version1']['meta_info'].parent =_meta_table['Hsrp.Interfaces.Interface.Ipv4']['meta_info']
_meta_table['Hsrp.Interfaces.Interface.Ipv4.Version2']['meta_info'].parent =_meta_table['Hsrp.Interfaces.Interface.Ipv4']['meta_info']
_meta_table['Hsrp.Interfaces.Interface.Ipv6']['meta_info'].parent =_meta_table['Hsrp.Interfaces.Interface']['meta_info']
_meta_table['Hsrp.Interfaces.Interface.Bfd']['meta_info'].parent =_meta_table['Hsrp.Interfaces.Interface']['meta_info']
_meta_table['Hsrp.Interfaces.Interface.Delay']['meta_info'].parent =_meta_table['Hsrp.Interfaces.Interface']['meta_info']
_meta_table['Hsrp.Interfaces.Interface.Ipv4']['meta_info'].parent =_meta_table['Hsrp.Interfaces.Interface']['meta_info']
_meta_table['Hsrp.Interfaces.Interface']['meta_info'].parent =_meta_table['Hsrp.Interfaces']['meta_info']
_meta_table['Hsrp.Interfaces']['meta_info'].parent =_meta_table['Hsrp']['meta_info']
_meta_table['Hsrp.Logging']['meta_info'].parent =_meta_table['Hsrp']['meta_info']
