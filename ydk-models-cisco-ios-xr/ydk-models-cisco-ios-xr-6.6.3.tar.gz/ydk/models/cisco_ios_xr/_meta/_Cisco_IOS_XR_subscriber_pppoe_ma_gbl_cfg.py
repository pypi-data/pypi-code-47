
'''
This is auto-generated file,
which includes metadata for module Cisco_IOS_XR_subscriber_pppoe_ma_gbl_cfg
'''

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_LIST, REFERENCE_LEAFLIST, REFERENCE_BITS, REFERENCE_UNION
from ydk._core._dm_meta_info import REFERENCE_CLASS, REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, ANYXML_CLASS
from ydk._core._importer import _yang_ns

_meta_table = {
    'PppoeInvalidSessionIdBehavior' : _MetaInfoEnum('PppoeInvalidSessionIdBehavior',
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_pppoe_ma_gbl_cfg', 'PppoeInvalidSessionIdBehavior',
        '''Pppoe invalid session id behavior''',
        {
            'drop':'drop',
            'log':'log',
        }, 'Cisco-IOS-XR-subscriber-pppoe-ma-gbl-cfg', _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-subscriber-pppoe-ma-gbl-cfg']),
    'PppoeCfg.PppoeBbaGroups.PppoeBbaGroup.Tag.Padr' : {
        'meta_info' : _MetaInfoClass('PppoeCfg.PppoeBbaGroups.PppoeBbaGroup.Tag.Padr', REFERENCE_CLASS,
            '''PADR packets''',
            False, 
            [
            _MetaInfoClassMember('session-unique-relay-session-id', ATTRIBUTE, 'Empty', 'empty',
                None, None,
                [], [],
                '''                Allow sessions to come up with unique
                relay-session-id in padr
                ''',
                'session_unique_relay_session_id',
                'Cisco-IOS-XR-subscriber-pppoe-ma-gbl-cfg', False),
            _MetaInfoClassMember('invalid-payload-allow', ATTRIBUTE, 'Empty', 'empty',
                None, None,
                [], [],
                '''                Allow sessions to come up with
                invalid-payload
                ''',
                'invalid_payload_allow',
                'Cisco-IOS-XR-subscriber-pppoe-ma-gbl-cfg', False),
            ],
            'Cisco-IOS-XR-subscriber-pppoe-ma-gbl-cfg',
            'padr',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-subscriber-pppoe-ma-gbl-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_pppoe_ma_gbl_cfg',
        ),
    },
    'PppoeCfg.PppoeBbaGroups.PppoeBbaGroup.Tag.ServiceNameConfigureds.ServiceNameConfigured' : {
        'meta_info' : _MetaInfoClass('PppoeCfg.PppoeBbaGroups.PppoeBbaGroup.Tag.ServiceNameConfigureds.ServiceNameConfigured', REFERENCE_LIST,
            '''Service name supported on this group''',
            False, 
            [
            _MetaInfoClassMember('name', ATTRIBUTE, 'str', 'xr:Cisco-ios-xr-string',
                None, None,
                [], [b'[\\w\\-\\.:,_@#%$\\+=\\|;]+'],
                '''                Service name
                ''',
                'name',
                'Cisco-IOS-XR-subscriber-pppoe-ma-gbl-cfg', True),
            ],
            'Cisco-IOS-XR-subscriber-pppoe-ma-gbl-cfg',
            'service-name-configured',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-subscriber-pppoe-ma-gbl-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_pppoe_ma_gbl_cfg',
        ),
    },
    'PppoeCfg.PppoeBbaGroups.PppoeBbaGroup.Tag.ServiceNameConfigureds' : {
        'meta_info' : _MetaInfoClass('PppoeCfg.PppoeBbaGroups.PppoeBbaGroup.Tag.ServiceNameConfigureds', REFERENCE_CLASS,
            '''Service name''',
            False, 
            [
            _MetaInfoClassMember('service-name-configured', REFERENCE_LIST, 'ServiceNameConfigured', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_pppoe_ma_gbl_cfg', 'PppoeCfg.PppoeBbaGroups.PppoeBbaGroup.Tag.ServiceNameConfigureds.ServiceNameConfigured',
                [], [],
                '''                Service name supported on this group
                ''',
                'service_name_configured',
                'Cisco-IOS-XR-subscriber-pppoe-ma-gbl-cfg', False),
            ],
            'Cisco-IOS-XR-subscriber-pppoe-ma-gbl-cfg',
            'service-name-configureds',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-subscriber-pppoe-ma-gbl-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_pppoe_ma_gbl_cfg',
        ),
    },
    'PppoeCfg.PppoeBbaGroups.PppoeBbaGroup.Tag.PppMaxPayload' : {
        'meta_info' : _MetaInfoClass('PppoeCfg.PppoeBbaGroups.PppoeBbaGroup.Tag.PppMaxPayload', REFERENCE_CLASS,
            '''Minimum and maximum payloads''',
            False, 
            [
            _MetaInfoClassMember('min', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('500', '2000')], [],
                '''                Minimum payload
                ''',
                'min',
                'Cisco-IOS-XR-subscriber-pppoe-ma-gbl-cfg', False, is_mandatory=True),
            _MetaInfoClassMember('max', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('500', '2000')], [],
                '''                Maximum payload
                ''',
                'max',
                'Cisco-IOS-XR-subscriber-pppoe-ma-gbl-cfg', False, is_mandatory=True),
            ],
            'Cisco-IOS-XR-subscriber-pppoe-ma-gbl-cfg',
            'ppp-max-payload',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-subscriber-pppoe-ma-gbl-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_pppoe_ma_gbl_cfg',
            is_presence=True,
        ),
    },
    'PppoeCfg.PppoeBbaGroups.PppoeBbaGroup.Tag' : {
        'meta_info' : _MetaInfoClass('PppoeCfg.PppoeBbaGroups.PppoeBbaGroup.Tag', REFERENCE_CLASS,
            '''PPPoE tag configuration data''',
            False, 
            [
            _MetaInfoClassMember('padr', REFERENCE_CLASS, 'Padr', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_pppoe_ma_gbl_cfg', 'PppoeCfg.PppoeBbaGroups.PppoeBbaGroup.Tag.Padr',
                [], [],
                '''                PADR packets
                ''',
                'padr',
                'Cisco-IOS-XR-subscriber-pppoe-ma-gbl-cfg', False),
            _MetaInfoClassMember('service-name-configureds', REFERENCE_CLASS, 'ServiceNameConfigureds', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_pppoe_ma_gbl_cfg', 'PppoeCfg.PppoeBbaGroups.PppoeBbaGroup.Tag.ServiceNameConfigureds',
                [], [],
                '''                Service name
                ''',
                'service_name_configureds',
                'Cisco-IOS-XR-subscriber-pppoe-ma-gbl-cfg', False),
            _MetaInfoClassMember('ppp-max-payload', REFERENCE_CLASS, 'PppMaxPayload', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_pppoe_ma_gbl_cfg', 'PppoeCfg.PppoeBbaGroups.PppoeBbaGroup.Tag.PppMaxPayload',
                [], [],
                '''                Minimum and maximum payloads
                ''',
                'ppp_max_payload',
                'Cisco-IOS-XR-subscriber-pppoe-ma-gbl-cfg', False, is_presence=True),
            _MetaInfoClassMember('ppp-max-payload-deny', ATTRIBUTE, 'Empty', 'empty',
                None, None,
                [], [],
                '''                Ignore the ppp-max-payload tag
                ''',
                'ppp_max_payload_deny',
                'Cisco-IOS-XR-subscriber-pppoe-ma-gbl-cfg', False),
            _MetaInfoClassMember('service-selection-disable', ATTRIBUTE, 'Empty', 'empty',
                None, None,
                [], [],
                '''                Disable advertising of unrequested service
                names
                ''',
                'service_selection_disable',
                'Cisco-IOS-XR-subscriber-pppoe-ma-gbl-cfg', False),
            _MetaInfoClassMember('ac-name', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                The name to include in the AC tag
                ''',
                'ac_name',
                'Cisco-IOS-XR-subscriber-pppoe-ma-gbl-cfg', False),
            ],
            'Cisco-IOS-XR-subscriber-pppoe-ma-gbl-cfg',
            'tag',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-subscriber-pppoe-ma-gbl-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_pppoe_ma_gbl_cfg',
        ),
    },
    'PppoeCfg.PppoeBbaGroups.PppoeBbaGroup.Sessions.VlanThrottle' : {
        'meta_info' : _MetaInfoClass('PppoeCfg.PppoeBbaGroups.PppoeBbaGroup.Sessions.VlanThrottle', REFERENCE_CLASS,
            '''Set VLAN (inner + outer tags) session
throttle''',
            False, 
            [
            _MetaInfoClassMember('throttle', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('1', '65535')], [],
                '''                Number of requests at which to throttle
                ''',
                'throttle',
                'Cisco-IOS-XR-subscriber-pppoe-ma-gbl-cfg', False, is_mandatory=True),
            _MetaInfoClassMember('request-period', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('1', '100')], [],
                '''                Throttle request period
                ''',
                'request_period',
                'Cisco-IOS-XR-subscriber-pppoe-ma-gbl-cfg', False, is_mandatory=True),
            _MetaInfoClassMember('blocking-period', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('1', '100')], [],
                '''                Throttle blocking period
                ''',
                'blocking_period',
                'Cisco-IOS-XR-subscriber-pppoe-ma-gbl-cfg', False, is_mandatory=True),
            ],
            'Cisco-IOS-XR-subscriber-pppoe-ma-gbl-cfg',
            'vlan-throttle',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-subscriber-pppoe-ma-gbl-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_pppoe_ma_gbl_cfg',
            is_presence=True,
        ),
    },
    'PppoeCfg.PppoeBbaGroups.PppoeBbaGroup.Sessions.InnerVlanThrottle' : {
        'meta_info' : _MetaInfoClass('PppoeCfg.PppoeBbaGroups.PppoeBbaGroup.Sessions.InnerVlanThrottle', REFERENCE_CLASS,
            '''Set Inner VLAN session throttle''',
            False, 
            [
            _MetaInfoClassMember('throttle', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('1', '65535')], [],
                '''                Number of requests at which to throttle
                ''',
                'throttle',
                'Cisco-IOS-XR-subscriber-pppoe-ma-gbl-cfg', False, is_mandatory=True),
            _MetaInfoClassMember('request-period', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('1', '100')], [],
                '''                Throttle request period
                ''',
                'request_period',
                'Cisco-IOS-XR-subscriber-pppoe-ma-gbl-cfg', False, is_mandatory=True),
            _MetaInfoClassMember('blocking-period', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('1', '100')], [],
                '''                Throttle blocking period
                ''',
                'blocking_period',
                'Cisco-IOS-XR-subscriber-pppoe-ma-gbl-cfg', False, is_mandatory=True),
            ],
            'Cisco-IOS-XR-subscriber-pppoe-ma-gbl-cfg',
            'inner-vlan-throttle',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-subscriber-pppoe-ma-gbl-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_pppoe_ma_gbl_cfg',
            is_presence=True,
        ),
    },
    'PppoeCfg.PppoeBbaGroups.PppoeBbaGroup.Sessions.RemoteIdLimit' : {
        'meta_info' : _MetaInfoClass('PppoeCfg.PppoeBbaGroups.PppoeBbaGroup.Sessions.RemoteIdLimit', REFERENCE_CLASS,
            '''Set Remote ID session limit and threshold''',
            False, 
            [
            _MetaInfoClassMember('limit', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('1', '65535')], [],
                '''                Per-Remote ID limit
                ''',
                'limit',
                'Cisco-IOS-XR-subscriber-pppoe-ma-gbl-cfg', False, is_mandatory=True),
            _MetaInfoClassMember('threshold', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('1', '65535')], [],
                '''                Per-Remote ID threshold
                ''',
                'threshold',
                'Cisco-IOS-XR-subscriber-pppoe-ma-gbl-cfg', False),
            ],
            'Cisco-IOS-XR-subscriber-pppoe-ma-gbl-cfg',
            'remote-id-limit',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-subscriber-pppoe-ma-gbl-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_pppoe_ma_gbl_cfg',
            is_presence=True,
        ),
    },
    'PppoeCfg.PppoeBbaGroups.PppoeBbaGroup.Sessions.MacIwfAccessInterfaceThrottle' : {
        'meta_info' : _MetaInfoClass('PppoeCfg.PppoeBbaGroups.PppoeBbaGroup.Sessions.MacIwfAccessInterfaceThrottle', REFERENCE_CLASS,
            '''Set per-MAC/Access interface throttle for IWF
sessions''',
            False, 
            [
            _MetaInfoClassMember('throttle', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('1', '65535')], [],
                '''                Number of requests at which to throttle
                ''',
                'throttle',
                'Cisco-IOS-XR-subscriber-pppoe-ma-gbl-cfg', False, is_mandatory=True),
            _MetaInfoClassMember('request-period', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('1', '100')], [],
                '''                Throttle request period
                ''',
                'request_period',
                'Cisco-IOS-XR-subscriber-pppoe-ma-gbl-cfg', False, is_mandatory=True),
            _MetaInfoClassMember('blocking-period', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('1', '100')], [],
                '''                Throttle blocking period
                ''',
                'blocking_period',
                'Cisco-IOS-XR-subscriber-pppoe-ma-gbl-cfg', False, is_mandatory=True),
            ],
            'Cisco-IOS-XR-subscriber-pppoe-ma-gbl-cfg',
            'mac-iwf-access-interface-throttle',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-subscriber-pppoe-ma-gbl-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_pppoe_ma_gbl_cfg',
            is_presence=True,
        ),
    },
    'PppoeCfg.PppoeBbaGroups.PppoeBbaGroup.Sessions.AccessInterfaceLimit' : {
        'meta_info' : _MetaInfoClass('PppoeCfg.PppoeBbaGroups.PppoeBbaGroup.Sessions.AccessInterfaceLimit', REFERENCE_CLASS,
            '''Set per-access interface limit''',
            False, 
            [
            _MetaInfoClassMember('limit', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('1', '65535')], [],
                '''                Per-access interface session limit
                ''',
                'limit',
                'Cisco-IOS-XR-subscriber-pppoe-ma-gbl-cfg', False, is_mandatory=True),
            _MetaInfoClassMember('threshold', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('1', '65535')], [],
                '''                Per-access interface session threshold
                ''',
                'threshold',
                'Cisco-IOS-XR-subscriber-pppoe-ma-gbl-cfg', False),
            ],
            'Cisco-IOS-XR-subscriber-pppoe-ma-gbl-cfg',
            'access-interface-limit',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-subscriber-pppoe-ma-gbl-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_pppoe_ma_gbl_cfg',
            is_presence=True,
        ),
    },
    'PppoeCfg.PppoeBbaGroups.PppoeBbaGroup.Sessions.MacAccessInterfaceThrottle' : {
        'meta_info' : _MetaInfoClass('PppoeCfg.PppoeBbaGroups.PppoeBbaGroup.Sessions.MacAccessInterfaceThrottle', REFERENCE_CLASS,
            '''Set per-MAC/Access Interface throttle''',
            False, 
            [
            _MetaInfoClassMember('throttle', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('1', '65535')], [],
                '''                Number of requests at which to throttle
                ''',
                'throttle',
                'Cisco-IOS-XR-subscriber-pppoe-ma-gbl-cfg', False, is_mandatory=True),
            _MetaInfoClassMember('request-period', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('1', '100')], [],
                '''                Throttle request period
                ''',
                'request_period',
                'Cisco-IOS-XR-subscriber-pppoe-ma-gbl-cfg', False, is_mandatory=True),
            _MetaInfoClassMember('blocking-period', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('1', '100')], [],
                '''                Throttle blocking period
                ''',
                'blocking_period',
                'Cisco-IOS-XR-subscriber-pppoe-ma-gbl-cfg', False, is_mandatory=True),
            ],
            'Cisco-IOS-XR-subscriber-pppoe-ma-gbl-cfg',
            'mac-access-interface-throttle',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-subscriber-pppoe-ma-gbl-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_pppoe_ma_gbl_cfg',
            is_presence=True,
        ),
    },
    'PppoeCfg.PppoeBbaGroups.PppoeBbaGroup.Sessions.OuterVlanLimit' : {
        'meta_info' : _MetaInfoClass('PppoeCfg.PppoeBbaGroups.PppoeBbaGroup.Sessions.OuterVlanLimit', REFERENCE_CLASS,
            '''Set Outer VLAN session limit and threshold''',
            False, 
            [
            _MetaInfoClassMember('limit', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('1', '65535')], [],
                '''                Per-Outer VLAN limit
                ''',
                'limit',
                'Cisco-IOS-XR-subscriber-pppoe-ma-gbl-cfg', False, is_mandatory=True),
            _MetaInfoClassMember('threshold', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('1', '65535')], [],
                '''                Per-Outer VLAN threshold
                ''',
                'threshold',
                'Cisco-IOS-XR-subscriber-pppoe-ma-gbl-cfg', False),
            ],
            'Cisco-IOS-XR-subscriber-pppoe-ma-gbl-cfg',
            'outer-vlan-limit',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-subscriber-pppoe-ma-gbl-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_pppoe_ma_gbl_cfg',
            is_presence=True,
        ),
    },
    'PppoeCfg.PppoeBbaGroups.PppoeBbaGroup.Sessions.CircuitIdThrottle' : {
        'meta_info' : _MetaInfoClass('PppoeCfg.PppoeBbaGroups.PppoeBbaGroup.Sessions.CircuitIdThrottle', REFERENCE_CLASS,
            '''Set Circuit ID session throttle''',
            False, 
            [
            _MetaInfoClassMember('throttle', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('1', '65535')], [],
                '''                Number of requests at which to throttle
                ''',
                'throttle',
                'Cisco-IOS-XR-subscriber-pppoe-ma-gbl-cfg', False, is_mandatory=True),
            _MetaInfoClassMember('request-period', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('1', '100')], [],
                '''                Throttle request period
                ''',
                'request_period',
                'Cisco-IOS-XR-subscriber-pppoe-ma-gbl-cfg', False, is_mandatory=True),
            _MetaInfoClassMember('blocking-period', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('1', '100')], [],
                '''                Throttle blocking period
                ''',
                'blocking_period',
                'Cisco-IOS-XR-subscriber-pppoe-ma-gbl-cfg', False, is_mandatory=True),
            ],
            'Cisco-IOS-XR-subscriber-pppoe-ma-gbl-cfg',
            'circuit-id-throttle',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-subscriber-pppoe-ma-gbl-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_pppoe_ma_gbl_cfg',
            is_presence=True,
        ),
    },
    'PppoeCfg.PppoeBbaGroups.PppoeBbaGroup.Sessions.MacLimit' : {
        'meta_info' : _MetaInfoClass('PppoeCfg.PppoeBbaGroups.PppoeBbaGroup.Sessions.MacLimit', REFERENCE_CLASS,
            '''Set per-MAC address session limit and
threshold''',
            False, 
            [
            _MetaInfoClassMember('limit', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('1', '65535')], [],
                '''                Per-MAC session limit
                ''',
                'limit',
                'Cisco-IOS-XR-subscriber-pppoe-ma-gbl-cfg', False, is_mandatory=True),
            _MetaInfoClassMember('threshold', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('1', '65535')], [],
                '''                Per-MAC session threshold
                ''',
                'threshold',
                'Cisco-IOS-XR-subscriber-pppoe-ma-gbl-cfg', False),
            ],
            'Cisco-IOS-XR-subscriber-pppoe-ma-gbl-cfg',
            'mac-limit',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-subscriber-pppoe-ma-gbl-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_pppoe_ma_gbl_cfg',
            is_presence=True,
        ),
    },
    'PppoeCfg.PppoeBbaGroups.PppoeBbaGroup.Sessions.CircuitIdLimit' : {
        'meta_info' : _MetaInfoClass('PppoeCfg.PppoeBbaGroups.PppoeBbaGroup.Sessions.CircuitIdLimit', REFERENCE_CLASS,
            '''Set Circuit ID session limit and threshold''',
            False, 
            [
            _MetaInfoClassMember('limit', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('1', '65535')], [],
                '''                Per-Circuit ID limit
                ''',
                'limit',
                'Cisco-IOS-XR-subscriber-pppoe-ma-gbl-cfg', False, is_mandatory=True),
            _MetaInfoClassMember('threshold', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('1', '65535')], [],
                '''                Per-Circuit ID threshold
                ''',
                'threshold',
                'Cisco-IOS-XR-subscriber-pppoe-ma-gbl-cfg', False),
            ],
            'Cisco-IOS-XR-subscriber-pppoe-ma-gbl-cfg',
            'circuit-id-limit',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-subscriber-pppoe-ma-gbl-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_pppoe_ma_gbl_cfg',
            is_presence=True,
        ),
    },
    'PppoeCfg.PppoeBbaGroups.PppoeBbaGroup.Sessions.MacIwfLimit' : {
        'meta_info' : _MetaInfoClass('PppoeCfg.PppoeBbaGroups.PppoeBbaGroup.Sessions.MacIwfLimit', REFERENCE_CLASS,
            '''Set per-MAC session limit and threshold for
IWF sessions''',
            False, 
            [
            _MetaInfoClassMember('limit', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('1', '65535')], [],
                '''                Per-MAC session limit for IWF sessions
                ''',
                'limit',
                'Cisco-IOS-XR-subscriber-pppoe-ma-gbl-cfg', False, is_mandatory=True),
            _MetaInfoClassMember('threshold', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('1', '65535')], [],
                '''                Per-MAC session threshold for IWF sessions
                ''',
                'threshold',
                'Cisco-IOS-XR-subscriber-pppoe-ma-gbl-cfg', False),
            ],
            'Cisco-IOS-XR-subscriber-pppoe-ma-gbl-cfg',
            'mac-iwf-limit',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-subscriber-pppoe-ma-gbl-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_pppoe_ma_gbl_cfg',
            is_presence=True,
        ),
    },
    'PppoeCfg.PppoeBbaGroups.PppoeBbaGroup.Sessions.MacIwfAccessInterfaceLimit' : {
        'meta_info' : _MetaInfoClass('PppoeCfg.PppoeBbaGroups.PppoeBbaGroup.Sessions.MacIwfAccessInterfaceLimit', REFERENCE_CLASS,
            '''Set per-MAC access interface session limit
and threshold for IWF sessions''',
            False, 
            [
            _MetaInfoClassMember('limit', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('1', '65535')], [],
                '''                Per-MAC access interface session limit for
                IWF sessions
                ''',
                'limit',
                'Cisco-IOS-XR-subscriber-pppoe-ma-gbl-cfg', False, is_mandatory=True),
            _MetaInfoClassMember('threshold', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('1', '65535')], [],
                '''                Per-MAC access interface session threshold
                for IWF sessions
                ''',
                'threshold',
                'Cisco-IOS-XR-subscriber-pppoe-ma-gbl-cfg', False),
            ],
            'Cisco-IOS-XR-subscriber-pppoe-ma-gbl-cfg',
            'mac-iwf-access-interface-limit',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-subscriber-pppoe-ma-gbl-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_pppoe_ma_gbl_cfg',
            is_presence=True,
        ),
    },
    'PppoeCfg.PppoeBbaGroups.PppoeBbaGroup.Sessions.InnerVlanLimit' : {
        'meta_info' : _MetaInfoClass('PppoeCfg.PppoeBbaGroups.PppoeBbaGroup.Sessions.InnerVlanLimit', REFERENCE_CLASS,
            '''Set Inner VLAN session limit and threshold''',
            False, 
            [
            _MetaInfoClassMember('limit', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('1', '65535')], [],
                '''                Per-Inner VLAN limit
                ''',
                'limit',
                'Cisco-IOS-XR-subscriber-pppoe-ma-gbl-cfg', False, is_mandatory=True),
            _MetaInfoClassMember('threshold', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('1', '65535')], [],
                '''                Per-Inner VLAN threshold
                ''',
                'threshold',
                'Cisco-IOS-XR-subscriber-pppoe-ma-gbl-cfg', False),
            ],
            'Cisco-IOS-XR-subscriber-pppoe-ma-gbl-cfg',
            'inner-vlan-limit',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-subscriber-pppoe-ma-gbl-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_pppoe_ma_gbl_cfg',
            is_presence=True,
        ),
    },
    'PppoeCfg.PppoeBbaGroups.PppoeBbaGroup.Sessions.OuterVlanThrottle' : {
        'meta_info' : _MetaInfoClass('PppoeCfg.PppoeBbaGroups.PppoeBbaGroup.Sessions.OuterVlanThrottle', REFERENCE_CLASS,
            '''Set Outer VLAN session throttle''',
            False, 
            [
            _MetaInfoClassMember('throttle', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('1', '65535')], [],
                '''                Number of requests at which to throttle
                ''',
                'throttle',
                'Cisco-IOS-XR-subscriber-pppoe-ma-gbl-cfg', False, is_mandatory=True),
            _MetaInfoClassMember('request-period', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('1', '100')], [],
                '''                Throttle request period
                ''',
                'request_period',
                'Cisco-IOS-XR-subscriber-pppoe-ma-gbl-cfg', False, is_mandatory=True),
            _MetaInfoClassMember('blocking-period', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('1', '100')], [],
                '''                Throttle blocking period
                ''',
                'blocking_period',
                'Cisco-IOS-XR-subscriber-pppoe-ma-gbl-cfg', False, is_mandatory=True),
            ],
            'Cisco-IOS-XR-subscriber-pppoe-ma-gbl-cfg',
            'outer-vlan-throttle',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-subscriber-pppoe-ma-gbl-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_pppoe_ma_gbl_cfg',
            is_presence=True,
        ),
    },
    'PppoeCfg.PppoeBbaGroups.PppoeBbaGroup.Sessions.MacThrottle' : {
        'meta_info' : _MetaInfoClass('PppoeCfg.PppoeBbaGroups.PppoeBbaGroup.Sessions.MacThrottle', REFERENCE_CLASS,
            '''Set per-MAC throttle''',
            False, 
            [
            _MetaInfoClassMember('throttle', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('1', '65535')], [],
                '''                Number of requests at which to throttle
                ''',
                'throttle',
                'Cisco-IOS-XR-subscriber-pppoe-ma-gbl-cfg', False, is_mandatory=True),
            _MetaInfoClassMember('request-period', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('1', '100')], [],
                '''                Throttle request period
                ''',
                'request_period',
                'Cisco-IOS-XR-subscriber-pppoe-ma-gbl-cfg', False, is_mandatory=True),
            _MetaInfoClassMember('blocking-period', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('1', '100')], [],
                '''                Throttle blocking period
                ''',
                'blocking_period',
                'Cisco-IOS-XR-subscriber-pppoe-ma-gbl-cfg', False, is_mandatory=True),
            ],
            'Cisco-IOS-XR-subscriber-pppoe-ma-gbl-cfg',
            'mac-throttle',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-subscriber-pppoe-ma-gbl-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_pppoe_ma_gbl_cfg',
            is_presence=True,
        ),
    },
    'PppoeCfg.PppoeBbaGroups.PppoeBbaGroup.Sessions.CircuitIdAndRemoteIdLimit' : {
        'meta_info' : _MetaInfoClass('PppoeCfg.PppoeBbaGroups.PppoeBbaGroup.Sessions.CircuitIdAndRemoteIdLimit', REFERENCE_CLASS,
            '''Set Circuit ID and Remote ID session
limit/threshold''',
            False, 
            [
            _MetaInfoClassMember('limit', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('1', '65535')], [],
                '''                Per-Circuit ID limit
                ''',
                'limit',
                'Cisco-IOS-XR-subscriber-pppoe-ma-gbl-cfg', False, is_mandatory=True),
            _MetaInfoClassMember('threshold', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('1', '65535')], [],
                '''                Per-Circuit ID threshold
                ''',
                'threshold',
                'Cisco-IOS-XR-subscriber-pppoe-ma-gbl-cfg', False),
            ],
            'Cisco-IOS-XR-subscriber-pppoe-ma-gbl-cfg',
            'circuit-id-and-remote-id-limit',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-subscriber-pppoe-ma-gbl-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_pppoe_ma_gbl_cfg',
            is_presence=True,
        ),
    },
    'PppoeCfg.PppoeBbaGroups.PppoeBbaGroup.Sessions.VlanLimit' : {
        'meta_info' : _MetaInfoClass('PppoeCfg.PppoeBbaGroups.PppoeBbaGroup.Sessions.VlanLimit', REFERENCE_CLASS,
            '''Set VLAN (inner + outer tags) session limit
and threshold''',
            False, 
            [
            _MetaInfoClassMember('limit', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('1', '65535')], [],
                '''                Per-VLAN (inner + outer tags) limit
                ''',
                'limit',
                'Cisco-IOS-XR-subscriber-pppoe-ma-gbl-cfg', False, is_mandatory=True),
            _MetaInfoClassMember('threshold', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('1', '65535')], [],
                '''                Per-VLAN (inner + outer tags) threshold
                ''',
                'threshold',
                'Cisco-IOS-XR-subscriber-pppoe-ma-gbl-cfg', False),
            ],
            'Cisco-IOS-XR-subscriber-pppoe-ma-gbl-cfg',
            'vlan-limit',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-subscriber-pppoe-ma-gbl-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_pppoe_ma_gbl_cfg',
            is_presence=True,
        ),
    },
    'PppoeCfg.PppoeBbaGroups.PppoeBbaGroup.Sessions.MacAccessInterfaceLimit' : {
        'meta_info' : _MetaInfoClass('PppoeCfg.PppoeBbaGroups.PppoeBbaGroup.Sessions.MacAccessInterfaceLimit', REFERENCE_CLASS,
            '''Set per-MAC access interface session limit
and threshold''',
            False, 
            [
            _MetaInfoClassMember('limit', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('1', '65535')], [],
                '''                Per-MAC access interface session limit
                ''',
                'limit',
                'Cisco-IOS-XR-subscriber-pppoe-ma-gbl-cfg', False, is_mandatory=True),
            _MetaInfoClassMember('threshold', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('1', '65535')], [],
                '''                Per-MAC access interface session threshold
                ''',
                'threshold',
                'Cisco-IOS-XR-subscriber-pppoe-ma-gbl-cfg', False),
            ],
            'Cisco-IOS-XR-subscriber-pppoe-ma-gbl-cfg',
            'mac-access-interface-limit',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-subscriber-pppoe-ma-gbl-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_pppoe_ma_gbl_cfg',
            is_presence=True,
        ),
    },
    'PppoeCfg.PppoeBbaGroups.PppoeBbaGroup.Sessions.RemoteIdThrottle' : {
        'meta_info' : _MetaInfoClass('PppoeCfg.PppoeBbaGroups.PppoeBbaGroup.Sessions.RemoteIdThrottle', REFERENCE_CLASS,
            '''Set Remote ID session throttle''',
            False, 
            [
            _MetaInfoClassMember('throttle', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('1', '65535')], [],
                '''                Number of requests at which to throttle
                ''',
                'throttle',
                'Cisco-IOS-XR-subscriber-pppoe-ma-gbl-cfg', False, is_mandatory=True),
            _MetaInfoClassMember('request-period', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('1', '100')], [],
                '''                Throttle request period
                ''',
                'request_period',
                'Cisco-IOS-XR-subscriber-pppoe-ma-gbl-cfg', False, is_mandatory=True),
            _MetaInfoClassMember('blocking-period', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('1', '100')], [],
                '''                Throttle blocking period
                ''',
                'blocking_period',
                'Cisco-IOS-XR-subscriber-pppoe-ma-gbl-cfg', False, is_mandatory=True),
            ],
            'Cisco-IOS-XR-subscriber-pppoe-ma-gbl-cfg',
            'remote-id-throttle',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-subscriber-pppoe-ma-gbl-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_pppoe_ma_gbl_cfg',
            is_presence=True,
        ),
    },
    'PppoeCfg.PppoeBbaGroups.PppoeBbaGroup.Sessions.MaxLimit' : {
        'meta_info' : _MetaInfoClass('PppoeCfg.PppoeBbaGroups.PppoeBbaGroup.Sessions.MaxLimit', REFERENCE_CLASS,
            '''Set per-card session limit and threshold''',
            False, 
            [
            _MetaInfoClassMember('limit', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('1', '65535')], [],
                '''                Per-card session limit
                ''',
                'limit',
                'Cisco-IOS-XR-subscriber-pppoe-ma-gbl-cfg', False, is_mandatory=True),
            _MetaInfoClassMember('threshold', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('1', '65535')], [],
                '''                Per-card session threshold
                ''',
                'threshold',
                'Cisco-IOS-XR-subscriber-pppoe-ma-gbl-cfg', False),
            ],
            'Cisco-IOS-XR-subscriber-pppoe-ma-gbl-cfg',
            'max-limit',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-subscriber-pppoe-ma-gbl-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_pppoe_ma_gbl_cfg',
            is_presence=True,
        ),
    },
    'PppoeCfg.PppoeBbaGroups.PppoeBbaGroup.Sessions.CircuitIdAndRemoteIdThrottle' : {
        'meta_info' : _MetaInfoClass('PppoeCfg.PppoeBbaGroups.PppoeBbaGroup.Sessions.CircuitIdAndRemoteIdThrottle', REFERENCE_CLASS,
            '''Set Circuit ID and Remote ID session throttle''',
            False, 
            [
            _MetaInfoClassMember('throttle', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('1', '65535')], [],
                '''                Number of requests at which to throttle
                ''',
                'throttle',
                'Cisco-IOS-XR-subscriber-pppoe-ma-gbl-cfg', False, is_mandatory=True),
            _MetaInfoClassMember('request-period', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('1', '100')], [],
                '''                Throttle request period
                ''',
                'request_period',
                'Cisco-IOS-XR-subscriber-pppoe-ma-gbl-cfg', False, is_mandatory=True),
            _MetaInfoClassMember('blocking-period', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('1', '100')], [],
                '''                Throttle blocking period
                ''',
                'blocking_period',
                'Cisco-IOS-XR-subscriber-pppoe-ma-gbl-cfg', False, is_mandatory=True),
            ],
            'Cisco-IOS-XR-subscriber-pppoe-ma-gbl-cfg',
            'circuit-id-and-remote-id-throttle',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-subscriber-pppoe-ma-gbl-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_pppoe_ma_gbl_cfg',
            is_presence=True,
        ),
    },
    'PppoeCfg.PppoeBbaGroups.PppoeBbaGroup.Sessions' : {
        'meta_info' : _MetaInfoClass('PppoeCfg.PppoeBbaGroups.PppoeBbaGroup.Sessions', REFERENCE_CLASS,
            '''PPPoE session configuration data''',
            False, 
            [
            _MetaInfoClassMember('vlan-throttle', REFERENCE_CLASS, 'VlanThrottle', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_pppoe_ma_gbl_cfg', 'PppoeCfg.PppoeBbaGroups.PppoeBbaGroup.Sessions.VlanThrottle',
                [], [],
                '''                Set VLAN (inner + outer tags) session
                throttle
                ''',
                'vlan_throttle',
                'Cisco-IOS-XR-subscriber-pppoe-ma-gbl-cfg', False, is_presence=True),
            _MetaInfoClassMember('inner-vlan-throttle', REFERENCE_CLASS, 'InnerVlanThrottle', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_pppoe_ma_gbl_cfg', 'PppoeCfg.PppoeBbaGroups.PppoeBbaGroup.Sessions.InnerVlanThrottle',
                [], [],
                '''                Set Inner VLAN session throttle
                ''',
                'inner_vlan_throttle',
                'Cisco-IOS-XR-subscriber-pppoe-ma-gbl-cfg', False, is_presence=True),
            _MetaInfoClassMember('remote-id-limit', REFERENCE_CLASS, 'RemoteIdLimit', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_pppoe_ma_gbl_cfg', 'PppoeCfg.PppoeBbaGroups.PppoeBbaGroup.Sessions.RemoteIdLimit',
                [], [],
                '''                Set Remote ID session limit and threshold
                ''',
                'remote_id_limit',
                'Cisco-IOS-XR-subscriber-pppoe-ma-gbl-cfg', False, is_presence=True),
            _MetaInfoClassMember('mac-iwf-access-interface-throttle', REFERENCE_CLASS, 'MacIwfAccessInterfaceThrottle', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_pppoe_ma_gbl_cfg', 'PppoeCfg.PppoeBbaGroups.PppoeBbaGroup.Sessions.MacIwfAccessInterfaceThrottle',
                [], [],
                '''                Set per-MAC/Access interface throttle for IWF
                sessions
                ''',
                'mac_iwf_access_interface_throttle',
                'Cisco-IOS-XR-subscriber-pppoe-ma-gbl-cfg', False, is_presence=True),
            _MetaInfoClassMember('access-interface-limit', REFERENCE_CLASS, 'AccessInterfaceLimit', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_pppoe_ma_gbl_cfg', 'PppoeCfg.PppoeBbaGroups.PppoeBbaGroup.Sessions.AccessInterfaceLimit',
                [], [],
                '''                Set per-access interface limit
                ''',
                'access_interface_limit',
                'Cisco-IOS-XR-subscriber-pppoe-ma-gbl-cfg', False, is_presence=True),
            _MetaInfoClassMember('mac-access-interface-throttle', REFERENCE_CLASS, 'MacAccessInterfaceThrottle', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_pppoe_ma_gbl_cfg', 'PppoeCfg.PppoeBbaGroups.PppoeBbaGroup.Sessions.MacAccessInterfaceThrottle',
                [], [],
                '''                Set per-MAC/Access Interface throttle
                ''',
                'mac_access_interface_throttle',
                'Cisco-IOS-XR-subscriber-pppoe-ma-gbl-cfg', False, is_presence=True),
            _MetaInfoClassMember('outer-vlan-limit', REFERENCE_CLASS, 'OuterVlanLimit', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_pppoe_ma_gbl_cfg', 'PppoeCfg.PppoeBbaGroups.PppoeBbaGroup.Sessions.OuterVlanLimit',
                [], [],
                '''                Set Outer VLAN session limit and threshold
                ''',
                'outer_vlan_limit',
                'Cisco-IOS-XR-subscriber-pppoe-ma-gbl-cfg', False, is_presence=True),
            _MetaInfoClassMember('circuit-id-throttle', REFERENCE_CLASS, 'CircuitIdThrottle', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_pppoe_ma_gbl_cfg', 'PppoeCfg.PppoeBbaGroups.PppoeBbaGroup.Sessions.CircuitIdThrottle',
                [], [],
                '''                Set Circuit ID session throttle
                ''',
                'circuit_id_throttle',
                'Cisco-IOS-XR-subscriber-pppoe-ma-gbl-cfg', False, is_presence=True),
            _MetaInfoClassMember('mac-limit', REFERENCE_CLASS, 'MacLimit', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_pppoe_ma_gbl_cfg', 'PppoeCfg.PppoeBbaGroups.PppoeBbaGroup.Sessions.MacLimit',
                [], [],
                '''                Set per-MAC address session limit and
                threshold
                ''',
                'mac_limit',
                'Cisco-IOS-XR-subscriber-pppoe-ma-gbl-cfg', False, is_presence=True),
            _MetaInfoClassMember('circuit-id-limit', REFERENCE_CLASS, 'CircuitIdLimit', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_pppoe_ma_gbl_cfg', 'PppoeCfg.PppoeBbaGroups.PppoeBbaGroup.Sessions.CircuitIdLimit',
                [], [],
                '''                Set Circuit ID session limit and threshold
                ''',
                'circuit_id_limit',
                'Cisco-IOS-XR-subscriber-pppoe-ma-gbl-cfg', False, is_presence=True),
            _MetaInfoClassMember('mac-iwf-limit', REFERENCE_CLASS, 'MacIwfLimit', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_pppoe_ma_gbl_cfg', 'PppoeCfg.PppoeBbaGroups.PppoeBbaGroup.Sessions.MacIwfLimit',
                [], [],
                '''                Set per-MAC session limit and threshold for
                IWF sessions
                ''',
                'mac_iwf_limit',
                'Cisco-IOS-XR-subscriber-pppoe-ma-gbl-cfg', False, is_presence=True),
            _MetaInfoClassMember('mac-iwf-access-interface-limit', REFERENCE_CLASS, 'MacIwfAccessInterfaceLimit', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_pppoe_ma_gbl_cfg', 'PppoeCfg.PppoeBbaGroups.PppoeBbaGroup.Sessions.MacIwfAccessInterfaceLimit',
                [], [],
                '''                Set per-MAC access interface session limit
                and threshold for IWF sessions
                ''',
                'mac_iwf_access_interface_limit',
                'Cisco-IOS-XR-subscriber-pppoe-ma-gbl-cfg', False, is_presence=True),
            _MetaInfoClassMember('inner-vlan-limit', REFERENCE_CLASS, 'InnerVlanLimit', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_pppoe_ma_gbl_cfg', 'PppoeCfg.PppoeBbaGroups.PppoeBbaGroup.Sessions.InnerVlanLimit',
                [], [],
                '''                Set Inner VLAN session limit and threshold
                ''',
                'inner_vlan_limit',
                'Cisco-IOS-XR-subscriber-pppoe-ma-gbl-cfg', False, is_presence=True),
            _MetaInfoClassMember('outer-vlan-throttle', REFERENCE_CLASS, 'OuterVlanThrottle', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_pppoe_ma_gbl_cfg', 'PppoeCfg.PppoeBbaGroups.PppoeBbaGroup.Sessions.OuterVlanThrottle',
                [], [],
                '''                Set Outer VLAN session throttle
                ''',
                'outer_vlan_throttle',
                'Cisco-IOS-XR-subscriber-pppoe-ma-gbl-cfg', False, is_presence=True),
            _MetaInfoClassMember('mac-throttle', REFERENCE_CLASS, 'MacThrottle', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_pppoe_ma_gbl_cfg', 'PppoeCfg.PppoeBbaGroups.PppoeBbaGroup.Sessions.MacThrottle',
                [], [],
                '''                Set per-MAC throttle
                ''',
                'mac_throttle',
                'Cisco-IOS-XR-subscriber-pppoe-ma-gbl-cfg', False, is_presence=True),
            _MetaInfoClassMember('circuit-id-and-remote-id-limit', REFERENCE_CLASS, 'CircuitIdAndRemoteIdLimit', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_pppoe_ma_gbl_cfg', 'PppoeCfg.PppoeBbaGroups.PppoeBbaGroup.Sessions.CircuitIdAndRemoteIdLimit',
                [], [],
                '''                Set Circuit ID and Remote ID session
                limit/threshold
                ''',
                'circuit_id_and_remote_id_limit',
                'Cisco-IOS-XR-subscriber-pppoe-ma-gbl-cfg', False, is_presence=True),
            _MetaInfoClassMember('vlan-limit', REFERENCE_CLASS, 'VlanLimit', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_pppoe_ma_gbl_cfg', 'PppoeCfg.PppoeBbaGroups.PppoeBbaGroup.Sessions.VlanLimit',
                [], [],
                '''                Set VLAN (inner + outer tags) session limit
                and threshold
                ''',
                'vlan_limit',
                'Cisco-IOS-XR-subscriber-pppoe-ma-gbl-cfg', False, is_presence=True),
            _MetaInfoClassMember('mac-access-interface-limit', REFERENCE_CLASS, 'MacAccessInterfaceLimit', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_pppoe_ma_gbl_cfg', 'PppoeCfg.PppoeBbaGroups.PppoeBbaGroup.Sessions.MacAccessInterfaceLimit',
                [], [],
                '''                Set per-MAC access interface session limit
                and threshold
                ''',
                'mac_access_interface_limit',
                'Cisco-IOS-XR-subscriber-pppoe-ma-gbl-cfg', False, is_presence=True),
            _MetaInfoClassMember('remote-id-throttle', REFERENCE_CLASS, 'RemoteIdThrottle', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_pppoe_ma_gbl_cfg', 'PppoeCfg.PppoeBbaGroups.PppoeBbaGroup.Sessions.RemoteIdThrottle',
                [], [],
                '''                Set Remote ID session throttle
                ''',
                'remote_id_throttle',
                'Cisco-IOS-XR-subscriber-pppoe-ma-gbl-cfg', False, is_presence=True),
            _MetaInfoClassMember('max-limit', REFERENCE_CLASS, 'MaxLimit', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_pppoe_ma_gbl_cfg', 'PppoeCfg.PppoeBbaGroups.PppoeBbaGroup.Sessions.MaxLimit',
                [], [],
                '''                Set per-card session limit and threshold
                ''',
                'max_limit',
                'Cisco-IOS-XR-subscriber-pppoe-ma-gbl-cfg', False, is_presence=True),
            _MetaInfoClassMember('circuit-id-and-remote-id-throttle', REFERENCE_CLASS, 'CircuitIdAndRemoteIdThrottle', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_pppoe_ma_gbl_cfg', 'PppoeCfg.PppoeBbaGroups.PppoeBbaGroup.Sessions.CircuitIdAndRemoteIdThrottle',
                [], [],
                '''                Set Circuit ID and Remote ID session throttle
                ''',
                'circuit_id_and_remote_id_throttle',
                'Cisco-IOS-XR-subscriber-pppoe-ma-gbl-cfg', False, is_presence=True),
            ],
            'Cisco-IOS-XR-subscriber-pppoe-ma-gbl-cfg',
            'sessions',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-subscriber-pppoe-ma-gbl-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_pppoe_ma_gbl_cfg',
        ),
    },
    'PppoeCfg.PppoeBbaGroups.PppoeBbaGroup.ControlPackets' : {
        'meta_info' : _MetaInfoClass('PppoeCfg.PppoeBbaGroups.PppoeBbaGroup.ControlPackets', REFERENCE_CLASS,
            '''PPPoE control-packet configuration data''',
            False, 
            [
            _MetaInfoClassMember('priority', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('0', '7')], [],
                '''                Set the Priority to use for PPP and PPPoE
                control packets
                ''',
                'priority',
                'Cisco-IOS-XR-subscriber-pppoe-ma-gbl-cfg', False),
            ],
            'Cisco-IOS-XR-subscriber-pppoe-ma-gbl-cfg',
            'control-packets',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-subscriber-pppoe-ma-gbl-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_pppoe_ma_gbl_cfg',
        ),
    },
    'PppoeCfg.PppoeBbaGroups.PppoeBbaGroup.PaDoDelay.RemoteIdSubstrings.RemoteIdSubstring' : {
        'meta_info' : _MetaInfoClass('PppoeCfg.PppoeBbaGroups.PppoeBbaGroup.PaDoDelay.RemoteIdSubstrings.RemoteIdSubstring', REFERENCE_LIST,
            '''Delay the PADO response when the received
Remote ID contains the given string''',
            False, 
            [
            _MetaInfoClassMember('name', ATTRIBUTE, 'str', 'xr:Cisco-ios-xr-string',
                None, None,
                [], [b'[\\w\\-\\.:,_@#%$\\+=\\|;]+'],
                '''                The string to be contained within the
                received Remote ID
                ''',
                'name',
                'Cisco-IOS-XR-subscriber-pppoe-ma-gbl-cfg', True),
            _MetaInfoClassMember('delay', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('0', '10000')], [],
                '''                PADO delay (in milliseconds)
                ''',
                'delay',
                'Cisco-IOS-XR-subscriber-pppoe-ma-gbl-cfg', False, is_mandatory=True),
            ],
            'Cisco-IOS-XR-subscriber-pppoe-ma-gbl-cfg',
            'remote-id-substring',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-subscriber-pppoe-ma-gbl-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_pppoe_ma_gbl_cfg',
        ),
    },
    'PppoeCfg.PppoeBbaGroups.PppoeBbaGroup.PaDoDelay.RemoteIdSubstrings' : {
        'meta_info' : _MetaInfoClass('PppoeCfg.PppoeBbaGroups.PppoeBbaGroup.PaDoDelay.RemoteIdSubstrings', REFERENCE_CLASS,
            '''Delay the PADO response when the received
Remote ID contains the given string''',
            False, 
            [
            _MetaInfoClassMember('remote-id-substring', REFERENCE_LIST, 'RemoteIdSubstring', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_pppoe_ma_gbl_cfg', 'PppoeCfg.PppoeBbaGroups.PppoeBbaGroup.PaDoDelay.RemoteIdSubstrings.RemoteIdSubstring',
                [], [],
                '''                Delay the PADO response when the received
                Remote ID contains the given string
                ''',
                'remote_id_substring',
                'Cisco-IOS-XR-subscriber-pppoe-ma-gbl-cfg', False),
            ],
            'Cisco-IOS-XR-subscriber-pppoe-ma-gbl-cfg',
            'remote-id-substrings',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-subscriber-pppoe-ma-gbl-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_pppoe_ma_gbl_cfg',
        ),
    },
    'PppoeCfg.PppoeBbaGroups.PppoeBbaGroup.PaDoDelay.RemoteIdStrings.RemoteIdString' : {
        'meta_info' : _MetaInfoClass('PppoeCfg.PppoeBbaGroups.PppoeBbaGroup.PaDoDelay.RemoteIdStrings.RemoteIdString', REFERENCE_LIST,
            '''Delay the PADO response when there is an
exact match on the received Remote ID''',
            False, 
            [
            _MetaInfoClassMember('name', ATTRIBUTE, 'str', 'xr:Cisco-ios-xr-string',
                None, None,
                [], [b'[\\w\\-\\.:,_@#%$\\+=\\|;]+'],
                '''                The string to exactly match the received
                Remote ID
                ''',
                'name',
                'Cisco-IOS-XR-subscriber-pppoe-ma-gbl-cfg', True),
            _MetaInfoClassMember('delay', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('0', '10000')], [],
                '''                PADO delay (in milliseconds)
                ''',
                'delay',
                'Cisco-IOS-XR-subscriber-pppoe-ma-gbl-cfg', False, is_mandatory=True),
            ],
            'Cisco-IOS-XR-subscriber-pppoe-ma-gbl-cfg',
            'remote-id-string',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-subscriber-pppoe-ma-gbl-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_pppoe_ma_gbl_cfg',
        ),
    },
    'PppoeCfg.PppoeBbaGroups.PppoeBbaGroup.PaDoDelay.RemoteIdStrings' : {
        'meta_info' : _MetaInfoClass('PppoeCfg.PppoeBbaGroups.PppoeBbaGroup.PaDoDelay.RemoteIdStrings', REFERENCE_CLASS,
            '''Delay the PADO response when there is an
exact match on the received Remote ID''',
            False, 
            [
            _MetaInfoClassMember('remote-id-string', REFERENCE_LIST, 'RemoteIdString', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_pppoe_ma_gbl_cfg', 'PppoeCfg.PppoeBbaGroups.PppoeBbaGroup.PaDoDelay.RemoteIdStrings.RemoteIdString',
                [], [],
                '''                Delay the PADO response when there is an
                exact match on the received Remote ID
                ''',
                'remote_id_string',
                'Cisco-IOS-XR-subscriber-pppoe-ma-gbl-cfg', False),
            ],
            'Cisco-IOS-XR-subscriber-pppoe-ma-gbl-cfg',
            'remote-id-strings',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-subscriber-pppoe-ma-gbl-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_pppoe_ma_gbl_cfg',
        ),
    },
    'PppoeCfg.PppoeBbaGroups.PppoeBbaGroup.PaDoDelay.ServiceNameStrings.ServiceNameString' : {
        'meta_info' : _MetaInfoClass('PppoeCfg.PppoeBbaGroups.PppoeBbaGroup.PaDoDelay.ServiceNameStrings.ServiceNameString', REFERENCE_LIST,
            '''Delay the PADO response when there is an
exact match on the received Service Name''',
            False, 
            [
            _MetaInfoClassMember('name', ATTRIBUTE, 'str', 'xr:Cisco-ios-xr-string',
                None, None,
                [], [b'[\\w\\-\\.:,_@#%$\\+=\\|;]+'],
                '''                The string to exactly match the received
                Service Name
                ''',
                'name',
                'Cisco-IOS-XR-subscriber-pppoe-ma-gbl-cfg', True),
            _MetaInfoClassMember('delay', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('0', '10000')], [],
                '''                PADO delay (in milliseconds)
                ''',
                'delay',
                'Cisco-IOS-XR-subscriber-pppoe-ma-gbl-cfg', False, is_mandatory=True),
            ],
            'Cisco-IOS-XR-subscriber-pppoe-ma-gbl-cfg',
            'service-name-string',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-subscriber-pppoe-ma-gbl-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_pppoe_ma_gbl_cfg',
        ),
    },
    'PppoeCfg.PppoeBbaGroups.PppoeBbaGroup.PaDoDelay.ServiceNameStrings' : {
        'meta_info' : _MetaInfoClass('PppoeCfg.PppoeBbaGroups.PppoeBbaGroup.PaDoDelay.ServiceNameStrings', REFERENCE_CLASS,
            '''Delay the PADO response when there is an
exact match on the received Service Name''',
            False, 
            [
            _MetaInfoClassMember('service-name-string', REFERENCE_LIST, 'ServiceNameString', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_pppoe_ma_gbl_cfg', 'PppoeCfg.PppoeBbaGroups.PppoeBbaGroup.PaDoDelay.ServiceNameStrings.ServiceNameString',
                [], [],
                '''                Delay the PADO response when there is an
                exact match on the received Service Name
                ''',
                'service_name_string',
                'Cisco-IOS-XR-subscriber-pppoe-ma-gbl-cfg', False),
            ],
            'Cisco-IOS-XR-subscriber-pppoe-ma-gbl-cfg',
            'service-name-strings',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-subscriber-pppoe-ma-gbl-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_pppoe_ma_gbl_cfg',
        ),
    },
    'PppoeCfg.PppoeBbaGroups.PppoeBbaGroup.PaDoDelay.CircuitIdSubstrings.CircuitIdSubstring' : {
        'meta_info' : _MetaInfoClass('PppoeCfg.PppoeBbaGroups.PppoeBbaGroup.PaDoDelay.CircuitIdSubstrings.CircuitIdSubstring', REFERENCE_LIST,
            '''Delay the PADO response when the received
Circuit ID contains the given string''',
            False, 
            [
            _MetaInfoClassMember('name', ATTRIBUTE, 'str', 'xr:Cisco-ios-xr-string',
                None, None,
                [], [b'[\\w\\-\\.:,_@#%$\\+=\\|;]+'],
                '''                The string to be contained within the
                received Circuit ID
                ''',
                'name',
                'Cisco-IOS-XR-subscriber-pppoe-ma-gbl-cfg', True),
            _MetaInfoClassMember('delay', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('0', '10000')], [],
                '''                PADO delay (in milliseconds)
                ''',
                'delay',
                'Cisco-IOS-XR-subscriber-pppoe-ma-gbl-cfg', False, is_mandatory=True),
            ],
            'Cisco-IOS-XR-subscriber-pppoe-ma-gbl-cfg',
            'circuit-id-substring',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-subscriber-pppoe-ma-gbl-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_pppoe_ma_gbl_cfg',
        ),
    },
    'PppoeCfg.PppoeBbaGroups.PppoeBbaGroup.PaDoDelay.CircuitIdSubstrings' : {
        'meta_info' : _MetaInfoClass('PppoeCfg.PppoeBbaGroups.PppoeBbaGroup.PaDoDelay.CircuitIdSubstrings', REFERENCE_CLASS,
            '''Delay the PADO response when the received
Circuit ID contains the given string''',
            False, 
            [
            _MetaInfoClassMember('circuit-id-substring', REFERENCE_LIST, 'CircuitIdSubstring', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_pppoe_ma_gbl_cfg', 'PppoeCfg.PppoeBbaGroups.PppoeBbaGroup.PaDoDelay.CircuitIdSubstrings.CircuitIdSubstring',
                [], [],
                '''                Delay the PADO response when the received
                Circuit ID contains the given string
                ''',
                'circuit_id_substring',
                'Cisco-IOS-XR-subscriber-pppoe-ma-gbl-cfg', False),
            ],
            'Cisco-IOS-XR-subscriber-pppoe-ma-gbl-cfg',
            'circuit-id-substrings',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-subscriber-pppoe-ma-gbl-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_pppoe_ma_gbl_cfg',
        ),
    },
    'PppoeCfg.PppoeBbaGroups.PppoeBbaGroup.PaDoDelay.ServiceNameSubstrings.ServiceNameSubstring' : {
        'meta_info' : _MetaInfoClass('PppoeCfg.PppoeBbaGroups.PppoeBbaGroup.PaDoDelay.ServiceNameSubstrings.ServiceNameSubstring', REFERENCE_LIST,
            '''Delay the PADO response when the received
Service Name contains the given string''',
            False, 
            [
            _MetaInfoClassMember('name', ATTRIBUTE, 'str', 'xr:Cisco-ios-xr-string',
                None, None,
                [], [b'[\\w\\-\\.:,_@#%$\\+=\\|;]+'],
                '''                The string to be contained within the
                received Service Name
                ''',
                'name',
                'Cisco-IOS-XR-subscriber-pppoe-ma-gbl-cfg', True),
            _MetaInfoClassMember('delay', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('0', '10000')], [],
                '''                PADO delay (in milliseconds)
                ''',
                'delay',
                'Cisco-IOS-XR-subscriber-pppoe-ma-gbl-cfg', False, is_mandatory=True),
            ],
            'Cisco-IOS-XR-subscriber-pppoe-ma-gbl-cfg',
            'service-name-substring',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-subscriber-pppoe-ma-gbl-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_pppoe_ma_gbl_cfg',
        ),
    },
    'PppoeCfg.PppoeBbaGroups.PppoeBbaGroup.PaDoDelay.ServiceNameSubstrings' : {
        'meta_info' : _MetaInfoClass('PppoeCfg.PppoeBbaGroups.PppoeBbaGroup.PaDoDelay.ServiceNameSubstrings', REFERENCE_CLASS,
            '''Delay the PADO response when the received
Service Name contains the given string''',
            False, 
            [
            _MetaInfoClassMember('service-name-substring', REFERENCE_LIST, 'ServiceNameSubstring', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_pppoe_ma_gbl_cfg', 'PppoeCfg.PppoeBbaGroups.PppoeBbaGroup.PaDoDelay.ServiceNameSubstrings.ServiceNameSubstring',
                [], [],
                '''                Delay the PADO response when the received
                Service Name contains the given string
                ''',
                'service_name_substring',
                'Cisco-IOS-XR-subscriber-pppoe-ma-gbl-cfg', False),
            ],
            'Cisco-IOS-XR-subscriber-pppoe-ma-gbl-cfg',
            'service-name-substrings',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-subscriber-pppoe-ma-gbl-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_pppoe_ma_gbl_cfg',
        ),
    },
    'PppoeCfg.PppoeBbaGroups.PppoeBbaGroup.PaDoDelay.CircuitIdStrings.CircuitIdString' : {
        'meta_info' : _MetaInfoClass('PppoeCfg.PppoeBbaGroups.PppoeBbaGroup.PaDoDelay.CircuitIdStrings.CircuitIdString', REFERENCE_LIST,
            '''Delay the PADO response when there is an
exact match on the received Circuit ID''',
            False, 
            [
            _MetaInfoClassMember('name', ATTRIBUTE, 'str', 'xr:Cisco-ios-xr-string',
                None, None,
                [], [b'[\\w\\-\\.:,_@#%$\\+=\\|;]+'],
                '''                The string to exactly match the received
                Circuit ID
                ''',
                'name',
                'Cisco-IOS-XR-subscriber-pppoe-ma-gbl-cfg', True),
            _MetaInfoClassMember('delay', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('0', '10000')], [],
                '''                PADO delay (in milliseconds)
                ''',
                'delay',
                'Cisco-IOS-XR-subscriber-pppoe-ma-gbl-cfg', False, is_mandatory=True),
            ],
            'Cisco-IOS-XR-subscriber-pppoe-ma-gbl-cfg',
            'circuit-id-string',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-subscriber-pppoe-ma-gbl-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_pppoe_ma_gbl_cfg',
        ),
    },
    'PppoeCfg.PppoeBbaGroups.PppoeBbaGroup.PaDoDelay.CircuitIdStrings' : {
        'meta_info' : _MetaInfoClass('PppoeCfg.PppoeBbaGroups.PppoeBbaGroup.PaDoDelay.CircuitIdStrings', REFERENCE_CLASS,
            '''Delay the PADO response when there is an
exact match on the received Circuit ID''',
            False, 
            [
            _MetaInfoClassMember('circuit-id-string', REFERENCE_LIST, 'CircuitIdString', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_pppoe_ma_gbl_cfg', 'PppoeCfg.PppoeBbaGroups.PppoeBbaGroup.PaDoDelay.CircuitIdStrings.CircuitIdString',
                [], [],
                '''                Delay the PADO response when there is an
                exact match on the received Circuit ID
                ''',
                'circuit_id_string',
                'Cisco-IOS-XR-subscriber-pppoe-ma-gbl-cfg', False),
            ],
            'Cisco-IOS-XR-subscriber-pppoe-ma-gbl-cfg',
            'circuit-id-strings',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-subscriber-pppoe-ma-gbl-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_pppoe_ma_gbl_cfg',
        ),
    },
    'PppoeCfg.PppoeBbaGroups.PppoeBbaGroup.PaDoDelay' : {
        'meta_info' : _MetaInfoClass('PppoeCfg.PppoeBbaGroups.PppoeBbaGroup.PaDoDelay', REFERENCE_CLASS,
            '''PPPoE PADO delay configuration data''',
            False, 
            [
            _MetaInfoClassMember('remote-id-substrings', REFERENCE_CLASS, 'RemoteIdSubstrings', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_pppoe_ma_gbl_cfg', 'PppoeCfg.PppoeBbaGroups.PppoeBbaGroup.PaDoDelay.RemoteIdSubstrings',
                [], [],
                '''                Delay the PADO response when the received
                Remote ID contains the given string
                ''',
                'remote_id_substrings',
                'Cisco-IOS-XR-subscriber-pppoe-ma-gbl-cfg', False),
            _MetaInfoClassMember('remote-id-strings', REFERENCE_CLASS, 'RemoteIdStrings', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_pppoe_ma_gbl_cfg', 'PppoeCfg.PppoeBbaGroups.PppoeBbaGroup.PaDoDelay.RemoteIdStrings',
                [], [],
                '''                Delay the PADO response when there is an
                exact match on the received Remote ID
                ''',
                'remote_id_strings',
                'Cisco-IOS-XR-subscriber-pppoe-ma-gbl-cfg', False),
            _MetaInfoClassMember('service-name-strings', REFERENCE_CLASS, 'ServiceNameStrings', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_pppoe_ma_gbl_cfg', 'PppoeCfg.PppoeBbaGroups.PppoeBbaGroup.PaDoDelay.ServiceNameStrings',
                [], [],
                '''                Delay the PADO response when there is an
                exact match on the received Service Name
                ''',
                'service_name_strings',
                'Cisco-IOS-XR-subscriber-pppoe-ma-gbl-cfg', False),
            _MetaInfoClassMember('circuit-id-substrings', REFERENCE_CLASS, 'CircuitIdSubstrings', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_pppoe_ma_gbl_cfg', 'PppoeCfg.PppoeBbaGroups.PppoeBbaGroup.PaDoDelay.CircuitIdSubstrings',
                [], [],
                '''                Delay the PADO response when the received
                Circuit ID contains the given string
                ''',
                'circuit_id_substrings',
                'Cisco-IOS-XR-subscriber-pppoe-ma-gbl-cfg', False),
            _MetaInfoClassMember('service-name-substrings', REFERENCE_CLASS, 'ServiceNameSubstrings', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_pppoe_ma_gbl_cfg', 'PppoeCfg.PppoeBbaGroups.PppoeBbaGroup.PaDoDelay.ServiceNameSubstrings',
                [], [],
                '''                Delay the PADO response when the received
                Service Name contains the given string
                ''',
                'service_name_substrings',
                'Cisco-IOS-XR-subscriber-pppoe-ma-gbl-cfg', False),
            _MetaInfoClassMember('circuit-id-strings', REFERENCE_CLASS, 'CircuitIdStrings', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_pppoe_ma_gbl_cfg', 'PppoeCfg.PppoeBbaGroups.PppoeBbaGroup.PaDoDelay.CircuitIdStrings',
                [], [],
                '''                Delay the PADO response when there is an
                exact match on the received Circuit ID
                ''',
                'circuit_id_strings',
                'Cisco-IOS-XR-subscriber-pppoe-ma-gbl-cfg', False),
            _MetaInfoClassMember('default', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('0', '10000')], [],
                '''                PADO delay (in milliseconds)
                ''',
                'default',
                'Cisco-IOS-XR-subscriber-pppoe-ma-gbl-cfg', False, is_mandatory=True),
            _MetaInfoClassMember('circuit-id', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('0', '10000')], [],
                '''                Configure PADO delay dependent on the
                received Circuit ID
                ''',
                'circuit_id',
                'Cisco-IOS-XR-subscriber-pppoe-ma-gbl-cfg', False),
            _MetaInfoClassMember('remote-id', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('0', '10000')], [],
                '''                Configure PADO delay dependent on the
                received Remote ID
                ''',
                'remote_id',
                'Cisco-IOS-XR-subscriber-pppoe-ma-gbl-cfg', False),
            ],
            'Cisco-IOS-XR-subscriber-pppoe-ma-gbl-cfg',
            'pa-do-delay',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-subscriber-pppoe-ma-gbl-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_pppoe_ma_gbl_cfg',
            is_presence=True,
        ),
    },
    'PppoeCfg.PppoeBbaGroups.PppoeBbaGroup' : {
        'meta_info' : _MetaInfoClass('PppoeCfg.PppoeBbaGroups.PppoeBbaGroup', REFERENCE_LIST,
            '''PPPoE BBA-Group configuration data''',
            False, 
            [
            _MetaInfoClassMember('bba-group', ATTRIBUTE, 'str', 'xr:Cisco-ios-xr-string',
                None, None,
                [], [b'[\\w\\-\\.:,_@#%$\\+=\\|;]+'],
                '''                BBA-Group name
                ''',
                'bba_group',
                'Cisco-IOS-XR-subscriber-pppoe-ma-gbl-cfg', True),
            _MetaInfoClassMember('tag', REFERENCE_CLASS, 'Tag', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_pppoe_ma_gbl_cfg', 'PppoeCfg.PppoeBbaGroups.PppoeBbaGroup.Tag',
                [], [],
                '''                PPPoE tag configuration data
                ''',
                'tag',
                'Cisco-IOS-XR-subscriber-pppoe-ma-gbl-cfg', False),
            _MetaInfoClassMember('sessions', REFERENCE_CLASS, 'Sessions', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_pppoe_ma_gbl_cfg', 'PppoeCfg.PppoeBbaGroups.PppoeBbaGroup.Sessions',
                [], [],
                '''                PPPoE session configuration data
                ''',
                'sessions',
                'Cisco-IOS-XR-subscriber-pppoe-ma-gbl-cfg', False),
            _MetaInfoClassMember('control-packets', REFERENCE_CLASS, 'ControlPackets', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_pppoe_ma_gbl_cfg', 'PppoeCfg.PppoeBbaGroups.PppoeBbaGroup.ControlPackets',
                [], [],
                '''                PPPoE control-packet configuration data
                ''',
                'control_packets',
                'Cisco-IOS-XR-subscriber-pppoe-ma-gbl-cfg', False),
            _MetaInfoClassMember('pa-do-delay', REFERENCE_CLASS, 'PaDoDelay', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_pppoe_ma_gbl_cfg', 'PppoeCfg.PppoeBbaGroups.PppoeBbaGroup.PaDoDelay',
                [], [],
                '''                PPPoE PADO delay configuration data
                ''',
                'pa_do_delay',
                'Cisco-IOS-XR-subscriber-pppoe-ma-gbl-cfg', False, is_presence=True),
            _MetaInfoClassMember('enable-renegotiate-on-padi', ATTRIBUTE, 'Empty', 'empty',
                None, None,
                [], [],
                '''                Disconnect on padi with same host_uniq
                ''',
                'enable_renegotiate_on_padi',
                'Cisco-IOS-XR-subscriber-pppoe-ma-gbl-cfg', False),
            _MetaInfoClassMember('completion-timeout', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('30', '600')], [],
                '''                PPPoE session completion timeout
                ''',
                'completion_timeout',
                'Cisco-IOS-XR-subscriber-pppoe-ma-gbl-cfg', False),
            _MetaInfoClassMember('invalid-session-id', REFERENCE_ENUM_CLASS, 'PppoeInvalidSessionIdBehavior', 'Pppoe-invalid-session-id-behavior',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_pppoe_ma_gbl_cfg', 'PppoeInvalidSessionIdBehavior',
                [], [],
                '''                Invalid session-ID behavior
                ''',
                'invalid_session_id',
                'Cisco-IOS-XR-subscriber-pppoe-ma-gbl-cfg', False),
            _MetaInfoClassMember('enable-padt-after-shut-down', ATTRIBUTE, 'Empty', 'empty',
                None, None,
                [], [],
                '''                Enable padt after shutdown
                ''',
                'enable_padt_after_shut_down',
                'Cisco-IOS-XR-subscriber-pppoe-ma-gbl-cfg', False),
            _MetaInfoClassMember('mtu', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('500', '2000')], [],
                '''                PPPoE default MTU
                ''',
                'mtu',
                'Cisco-IOS-XR-subscriber-pppoe-ma-gbl-cfg', False),
            ],
            'Cisco-IOS-XR-subscriber-pppoe-ma-gbl-cfg',
            'pppoe-bba-group',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-subscriber-pppoe-ma-gbl-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_pppoe_ma_gbl_cfg',
        ),
    },
    'PppoeCfg.PppoeBbaGroups' : {
        'meta_info' : _MetaInfoClass('PppoeCfg.PppoeBbaGroups', REFERENCE_CLASS,
            '''PPPoE BBA-Group configuration data''',
            False, 
            [
            _MetaInfoClassMember('pppoe-bba-group', REFERENCE_LIST, 'PppoeBbaGroup', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_pppoe_ma_gbl_cfg', 'PppoeCfg.PppoeBbaGroups.PppoeBbaGroup',
                [], [],
                '''                PPPoE BBA-Group configuration data
                ''',
                'pppoe_bba_group',
                'Cisco-IOS-XR-subscriber-pppoe-ma-gbl-cfg', False),
            ],
            'Cisco-IOS-XR-subscriber-pppoe-ma-gbl-cfg',
            'pppoe-bba-groups',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-subscriber-pppoe-ma-gbl-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_pppoe_ma_gbl_cfg',
        ),
    },
    'PppoeCfg' : {
        'meta_info' : _MetaInfoClass('PppoeCfg', REFERENCE_CLASS,
            '''PPPOE configuration data''',
            False, 
            [
            _MetaInfoClassMember('pppoe-bba-groups', REFERENCE_CLASS, 'PppoeBbaGroups', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_pppoe_ma_gbl_cfg', 'PppoeCfg.PppoeBbaGroups',
                [], [],
                '''                PPPoE BBA-Group configuration data
                ''',
                'pppoe_bba_groups',
                'Cisco-IOS-XR-subscriber-pppoe-ma-gbl-cfg', False),
            _MetaInfoClassMember('session-id-space-flat', ATTRIBUTE, 'Empty', 'empty',
                None, None,
                [], [],
                '''                Disable per-parent session ID spaces
                ''',
                'session_id_space_flat',
                'Cisco-IOS-XR-subscriber-pppoe-ma-gbl-cfg', False),
            _MetaInfoClassMember('in-flight-window', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('1', '20000')], [],
                '''                Set the PPPoE in-flight window size
                ''',
                'in_flight_window',
                'Cisco-IOS-XR-subscriber-pppoe-ma-gbl-cfg', False),
            ],
            'Cisco-IOS-XR-subscriber-pppoe-ma-gbl-cfg',
            'pppoe-cfg',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-subscriber-pppoe-ma-gbl-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_pppoe_ma_gbl_cfg',
        ),
    },
}
_meta_table['PppoeCfg.PppoeBbaGroups.PppoeBbaGroup.Tag.ServiceNameConfigureds.ServiceNameConfigured']['meta_info'].parent =_meta_table['PppoeCfg.PppoeBbaGroups.PppoeBbaGroup.Tag.ServiceNameConfigureds']['meta_info']
_meta_table['PppoeCfg.PppoeBbaGroups.PppoeBbaGroup.Tag.Padr']['meta_info'].parent =_meta_table['PppoeCfg.PppoeBbaGroups.PppoeBbaGroup.Tag']['meta_info']
_meta_table['PppoeCfg.PppoeBbaGroups.PppoeBbaGroup.Tag.ServiceNameConfigureds']['meta_info'].parent =_meta_table['PppoeCfg.PppoeBbaGroups.PppoeBbaGroup.Tag']['meta_info']
_meta_table['PppoeCfg.PppoeBbaGroups.PppoeBbaGroup.Tag.PppMaxPayload']['meta_info'].parent =_meta_table['PppoeCfg.PppoeBbaGroups.PppoeBbaGroup.Tag']['meta_info']
_meta_table['PppoeCfg.PppoeBbaGroups.PppoeBbaGroup.Sessions.VlanThrottle']['meta_info'].parent =_meta_table['PppoeCfg.PppoeBbaGroups.PppoeBbaGroup.Sessions']['meta_info']
_meta_table['PppoeCfg.PppoeBbaGroups.PppoeBbaGroup.Sessions.InnerVlanThrottle']['meta_info'].parent =_meta_table['PppoeCfg.PppoeBbaGroups.PppoeBbaGroup.Sessions']['meta_info']
_meta_table['PppoeCfg.PppoeBbaGroups.PppoeBbaGroup.Sessions.RemoteIdLimit']['meta_info'].parent =_meta_table['PppoeCfg.PppoeBbaGroups.PppoeBbaGroup.Sessions']['meta_info']
_meta_table['PppoeCfg.PppoeBbaGroups.PppoeBbaGroup.Sessions.MacIwfAccessInterfaceThrottle']['meta_info'].parent =_meta_table['PppoeCfg.PppoeBbaGroups.PppoeBbaGroup.Sessions']['meta_info']
_meta_table['PppoeCfg.PppoeBbaGroups.PppoeBbaGroup.Sessions.AccessInterfaceLimit']['meta_info'].parent =_meta_table['PppoeCfg.PppoeBbaGroups.PppoeBbaGroup.Sessions']['meta_info']
_meta_table['PppoeCfg.PppoeBbaGroups.PppoeBbaGroup.Sessions.MacAccessInterfaceThrottle']['meta_info'].parent =_meta_table['PppoeCfg.PppoeBbaGroups.PppoeBbaGroup.Sessions']['meta_info']
_meta_table['PppoeCfg.PppoeBbaGroups.PppoeBbaGroup.Sessions.OuterVlanLimit']['meta_info'].parent =_meta_table['PppoeCfg.PppoeBbaGroups.PppoeBbaGroup.Sessions']['meta_info']
_meta_table['PppoeCfg.PppoeBbaGroups.PppoeBbaGroup.Sessions.CircuitIdThrottle']['meta_info'].parent =_meta_table['PppoeCfg.PppoeBbaGroups.PppoeBbaGroup.Sessions']['meta_info']
_meta_table['PppoeCfg.PppoeBbaGroups.PppoeBbaGroup.Sessions.MacLimit']['meta_info'].parent =_meta_table['PppoeCfg.PppoeBbaGroups.PppoeBbaGroup.Sessions']['meta_info']
_meta_table['PppoeCfg.PppoeBbaGroups.PppoeBbaGroup.Sessions.CircuitIdLimit']['meta_info'].parent =_meta_table['PppoeCfg.PppoeBbaGroups.PppoeBbaGroup.Sessions']['meta_info']
_meta_table['PppoeCfg.PppoeBbaGroups.PppoeBbaGroup.Sessions.MacIwfLimit']['meta_info'].parent =_meta_table['PppoeCfg.PppoeBbaGroups.PppoeBbaGroup.Sessions']['meta_info']
_meta_table['PppoeCfg.PppoeBbaGroups.PppoeBbaGroup.Sessions.MacIwfAccessInterfaceLimit']['meta_info'].parent =_meta_table['PppoeCfg.PppoeBbaGroups.PppoeBbaGroup.Sessions']['meta_info']
_meta_table['PppoeCfg.PppoeBbaGroups.PppoeBbaGroup.Sessions.InnerVlanLimit']['meta_info'].parent =_meta_table['PppoeCfg.PppoeBbaGroups.PppoeBbaGroup.Sessions']['meta_info']
_meta_table['PppoeCfg.PppoeBbaGroups.PppoeBbaGroup.Sessions.OuterVlanThrottle']['meta_info'].parent =_meta_table['PppoeCfg.PppoeBbaGroups.PppoeBbaGroup.Sessions']['meta_info']
_meta_table['PppoeCfg.PppoeBbaGroups.PppoeBbaGroup.Sessions.MacThrottle']['meta_info'].parent =_meta_table['PppoeCfg.PppoeBbaGroups.PppoeBbaGroup.Sessions']['meta_info']
_meta_table['PppoeCfg.PppoeBbaGroups.PppoeBbaGroup.Sessions.CircuitIdAndRemoteIdLimit']['meta_info'].parent =_meta_table['PppoeCfg.PppoeBbaGroups.PppoeBbaGroup.Sessions']['meta_info']
_meta_table['PppoeCfg.PppoeBbaGroups.PppoeBbaGroup.Sessions.VlanLimit']['meta_info'].parent =_meta_table['PppoeCfg.PppoeBbaGroups.PppoeBbaGroup.Sessions']['meta_info']
_meta_table['PppoeCfg.PppoeBbaGroups.PppoeBbaGroup.Sessions.MacAccessInterfaceLimit']['meta_info'].parent =_meta_table['PppoeCfg.PppoeBbaGroups.PppoeBbaGroup.Sessions']['meta_info']
_meta_table['PppoeCfg.PppoeBbaGroups.PppoeBbaGroup.Sessions.RemoteIdThrottle']['meta_info'].parent =_meta_table['PppoeCfg.PppoeBbaGroups.PppoeBbaGroup.Sessions']['meta_info']
_meta_table['PppoeCfg.PppoeBbaGroups.PppoeBbaGroup.Sessions.MaxLimit']['meta_info'].parent =_meta_table['PppoeCfg.PppoeBbaGroups.PppoeBbaGroup.Sessions']['meta_info']
_meta_table['PppoeCfg.PppoeBbaGroups.PppoeBbaGroup.Sessions.CircuitIdAndRemoteIdThrottle']['meta_info'].parent =_meta_table['PppoeCfg.PppoeBbaGroups.PppoeBbaGroup.Sessions']['meta_info']
_meta_table['PppoeCfg.PppoeBbaGroups.PppoeBbaGroup.PaDoDelay.RemoteIdSubstrings.RemoteIdSubstring']['meta_info'].parent =_meta_table['PppoeCfg.PppoeBbaGroups.PppoeBbaGroup.PaDoDelay.RemoteIdSubstrings']['meta_info']
_meta_table['PppoeCfg.PppoeBbaGroups.PppoeBbaGroup.PaDoDelay.RemoteIdStrings.RemoteIdString']['meta_info'].parent =_meta_table['PppoeCfg.PppoeBbaGroups.PppoeBbaGroup.PaDoDelay.RemoteIdStrings']['meta_info']
_meta_table['PppoeCfg.PppoeBbaGroups.PppoeBbaGroup.PaDoDelay.ServiceNameStrings.ServiceNameString']['meta_info'].parent =_meta_table['PppoeCfg.PppoeBbaGroups.PppoeBbaGroup.PaDoDelay.ServiceNameStrings']['meta_info']
_meta_table['PppoeCfg.PppoeBbaGroups.PppoeBbaGroup.PaDoDelay.CircuitIdSubstrings.CircuitIdSubstring']['meta_info'].parent =_meta_table['PppoeCfg.PppoeBbaGroups.PppoeBbaGroup.PaDoDelay.CircuitIdSubstrings']['meta_info']
_meta_table['PppoeCfg.PppoeBbaGroups.PppoeBbaGroup.PaDoDelay.ServiceNameSubstrings.ServiceNameSubstring']['meta_info'].parent =_meta_table['PppoeCfg.PppoeBbaGroups.PppoeBbaGroup.PaDoDelay.ServiceNameSubstrings']['meta_info']
_meta_table['PppoeCfg.PppoeBbaGroups.PppoeBbaGroup.PaDoDelay.CircuitIdStrings.CircuitIdString']['meta_info'].parent =_meta_table['PppoeCfg.PppoeBbaGroups.PppoeBbaGroup.PaDoDelay.CircuitIdStrings']['meta_info']
_meta_table['PppoeCfg.PppoeBbaGroups.PppoeBbaGroup.PaDoDelay.RemoteIdSubstrings']['meta_info'].parent =_meta_table['PppoeCfg.PppoeBbaGroups.PppoeBbaGroup.PaDoDelay']['meta_info']
_meta_table['PppoeCfg.PppoeBbaGroups.PppoeBbaGroup.PaDoDelay.RemoteIdStrings']['meta_info'].parent =_meta_table['PppoeCfg.PppoeBbaGroups.PppoeBbaGroup.PaDoDelay']['meta_info']
_meta_table['PppoeCfg.PppoeBbaGroups.PppoeBbaGroup.PaDoDelay.ServiceNameStrings']['meta_info'].parent =_meta_table['PppoeCfg.PppoeBbaGroups.PppoeBbaGroup.PaDoDelay']['meta_info']
_meta_table['PppoeCfg.PppoeBbaGroups.PppoeBbaGroup.PaDoDelay.CircuitIdSubstrings']['meta_info'].parent =_meta_table['PppoeCfg.PppoeBbaGroups.PppoeBbaGroup.PaDoDelay']['meta_info']
_meta_table['PppoeCfg.PppoeBbaGroups.PppoeBbaGroup.PaDoDelay.ServiceNameSubstrings']['meta_info'].parent =_meta_table['PppoeCfg.PppoeBbaGroups.PppoeBbaGroup.PaDoDelay']['meta_info']
_meta_table['PppoeCfg.PppoeBbaGroups.PppoeBbaGroup.PaDoDelay.CircuitIdStrings']['meta_info'].parent =_meta_table['PppoeCfg.PppoeBbaGroups.PppoeBbaGroup.PaDoDelay']['meta_info']
_meta_table['PppoeCfg.PppoeBbaGroups.PppoeBbaGroup.Tag']['meta_info'].parent =_meta_table['PppoeCfg.PppoeBbaGroups.PppoeBbaGroup']['meta_info']
_meta_table['PppoeCfg.PppoeBbaGroups.PppoeBbaGroup.Sessions']['meta_info'].parent =_meta_table['PppoeCfg.PppoeBbaGroups.PppoeBbaGroup']['meta_info']
_meta_table['PppoeCfg.PppoeBbaGroups.PppoeBbaGroup.ControlPackets']['meta_info'].parent =_meta_table['PppoeCfg.PppoeBbaGroups.PppoeBbaGroup']['meta_info']
_meta_table['PppoeCfg.PppoeBbaGroups.PppoeBbaGroup.PaDoDelay']['meta_info'].parent =_meta_table['PppoeCfg.PppoeBbaGroups.PppoeBbaGroup']['meta_info']
_meta_table['PppoeCfg.PppoeBbaGroups.PppoeBbaGroup']['meta_info'].parent =_meta_table['PppoeCfg.PppoeBbaGroups']['meta_info']
_meta_table['PppoeCfg.PppoeBbaGroups']['meta_info'].parent =_meta_table['PppoeCfg']['meta_info']
