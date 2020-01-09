
'''
This is auto-generated file,
which includes metadata for module Cisco_IOS_XR_cdp_cfg
'''

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_LIST, REFERENCE_LEAFLIST, REFERENCE_BITS, REFERENCE_UNION
from ydk._core._dm_meta_info import REFERENCE_CLASS, REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, ANYXML_CLASS
from ydk._core._importer import _yang_ns

_meta_table = {
    'Cdp' : {
        'meta_info' : _MetaInfoClass('Cdp', REFERENCE_CLASS,
            '''Global CDP configuration data''',
            False, 
            [
            _MetaInfoClassMember('timer', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('5', '254')], [],
                '''                Specify the rate at which CDP packets are sent
                ''',
                'timer',
                'Cisco-IOS-XR-cdp-cfg', False, default_value="60"),
            _MetaInfoClassMember('advertise-v1-only', ATTRIBUTE, 'Empty', 'empty',
                None, None,
                [], [],
                '''                Enable CDPv1 only advertisements
                ''',
                'advertise_v1_only',
                'Cisco-IOS-XR-cdp-cfg', False),
            _MetaInfoClassMember('enable', ATTRIBUTE, 'bool', 'boolean',
                None, None,
                [], [],
                '''                Enable or disable CDP globally
                ''',
                'enable',
                'Cisco-IOS-XR-cdp-cfg', False, default_value='True'),
            _MetaInfoClassMember('hold-time', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('10', '255')], [],
                '''                Length of time (in sec) that the receiver must
                keep a CDP packet
                ''',
                'hold_time',
                'Cisco-IOS-XR-cdp-cfg', False, default_value="180"),
            _MetaInfoClassMember('log-adjacency', ATTRIBUTE, 'Empty', 'empty',
                None, None,
                [], [],
                '''                Enable logging of adjacency changes
                ''',
                'log_adjacency',
                'Cisco-IOS-XR-cdp-cfg', False),
            ],
            'Cisco-IOS-XR-cdp-cfg',
            'cdp',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-cdp-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_cdp_cfg',
        ),
    },
}
