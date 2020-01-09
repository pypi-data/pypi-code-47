
'''
This is auto-generated file,
which includes metadata for module Cisco_IOS_XR_subscriber_accounting_cfg
'''

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_LIST, REFERENCE_LEAFLIST, REFERENCE_BITS, REFERENCE_UNION
from ydk._core._dm_meta_info import REFERENCE_CLASS, REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, ANYXML_CLASS
from ydk._core._importer import _yang_ns

_meta_table = {
    'SubscriberAccounting.PrepaidConfigurations.PrepaidConfiguration' : {
        'meta_info' : _MetaInfoClass('SubscriberAccounting.PrepaidConfigurations.PrepaidConfiguration', REFERENCE_LIST,
            '''Prepaid configuration name or default''',
            False, 
            [
            _MetaInfoClassMember('prepaid-config-name', ATTRIBUTE, 'str', 'xr:Cisco-ios-xr-string',
                None, None,
                [(1, 64)], [],
                '''                Prepaid configuration name or default
                ''',
                'prepaid_config_name',
                'Cisco-IOS-XR-subscriber-accounting-cfg', True),
            _MetaInfoClassMember('password', ATTRIBUTE, 'str', 'string',
                None, None,
                [(1, 64)], [],
                '''                Password to be used when placing prepaid
                (re)authorization requests
                ''',
                'password',
                'Cisco-IOS-XR-subscriber-accounting-cfg', False),
            _MetaInfoClassMember('volume-threshold', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('0', '4294967295')], [],
                '''                Threshold at which to send prepaid volume
                quota request
                ''',
                'volume_threshold',
                'Cisco-IOS-XR-subscriber-accounting-cfg', False),
            _MetaInfoClassMember('accounting-method-list', ATTRIBUTE, 'str', 'string',
                None, None,
                [(1, 64)], [],
                '''                Method list to be used when placing prepaid
                accounting requests
                ''',
                'accounting_method_list',
                'Cisco-IOS-XR-subscriber-accounting-cfg', False),
            _MetaInfoClassMember('time-hold', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('0', '4294967295')], [],
                '''                Idle Threshold for which prepaid quota is
                valid
                ''',
                'time_hold',
                'Cisco-IOS-XR-subscriber-accounting-cfg', False),
            _MetaInfoClassMember('author-method-list', ATTRIBUTE, 'str', 'string',
                None, None,
                [(1, 64)], [],
                '''                Method list to be used when placing prepaid
                (re)authorization requests
                ''',
                'author_method_list',
                'Cisco-IOS-XR-subscriber-accounting-cfg', False),
            _MetaInfoClassMember('traffic-direction', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                Prepaid quota traffic direction
                ''',
                'traffic_direction',
                'Cisco-IOS-XR-subscriber-accounting-cfg', False),
            _MetaInfoClassMember('time-threshold', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('0', '4294967295')], [],
                '''                Threshold at which to send prepaid time quota
                request
                ''',
                'time_threshold',
                'Cisco-IOS-XR-subscriber-accounting-cfg', False),
            _MetaInfoClassMember('time-valid', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('0', '4294967295')], [],
                '''                Threshold for which prepaid quota is valid
                ''',
                'time_valid',
                'Cisco-IOS-XR-subscriber-accounting-cfg', False),
            ],
            'Cisco-IOS-XR-subscriber-accounting-cfg',
            'prepaid-configuration',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-subscriber-accounting-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_accounting_cfg',
        ),
    },
    'SubscriberAccounting.PrepaidConfigurations' : {
        'meta_info' : _MetaInfoClass('SubscriberAccounting.PrepaidConfigurations', REFERENCE_CLASS,
            '''Subscriber Prepaid Feature Configuration''',
            False, 
            [
            _MetaInfoClassMember('prepaid-configuration', REFERENCE_LIST, 'PrepaidConfiguration', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_accounting_cfg', 'SubscriberAccounting.PrepaidConfigurations.PrepaidConfiguration',
                [], [],
                '''                Prepaid configuration name or default
                ''',
                'prepaid_configuration',
                'Cisco-IOS-XR-subscriber-accounting-cfg', False),
            ],
            'Cisco-IOS-XR-subscriber-accounting-cfg',
            'prepaid-configurations',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-subscriber-accounting-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_accounting_cfg',
        ),
    },
    'SubscriberAccounting' : {
        'meta_info' : _MetaInfoClass('SubscriberAccounting', REFERENCE_CLASS,
            '''Subscriber Configuration''',
            False, 
            [
            _MetaInfoClassMember('prepaid-configurations', REFERENCE_CLASS, 'PrepaidConfigurations', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_accounting_cfg', 'SubscriberAccounting.PrepaidConfigurations',
                [], [],
                '''                Subscriber Prepaid Feature Configuration
                ''',
                'prepaid_configurations',
                'Cisco-IOS-XR-subscriber-accounting-cfg', False),
            ],
            'Cisco-IOS-XR-subscriber-accounting-cfg',
            'subscriber-accounting',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-subscriber-accounting-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_accounting_cfg',
        ),
    },
}
_meta_table['SubscriberAccounting.PrepaidConfigurations.PrepaidConfiguration']['meta_info'].parent =_meta_table['SubscriberAccounting.PrepaidConfigurations']['meta_info']
_meta_table['SubscriberAccounting.PrepaidConfigurations']['meta_info'].parent =_meta_table['SubscriberAccounting']['meta_info']
