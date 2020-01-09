
'''
This is auto-generated file,
which includes metadata for module Cisco_IOS_XR_qos_ma_cfg
'''

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_LIST, REFERENCE_LEAFLIST, REFERENCE_BITS, REFERENCE_UNION
from ydk._core._dm_meta_info import REFERENCE_CLASS, REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, ANYXML_CLASS
from ydk._core._importer import _yang_ns

_meta_table = {
    'QosFieldNotSupported' : _MetaInfoEnum('QosFieldNotSupported',
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_qos_ma_cfg', 'QosFieldNotSupported',
        '''Qos field not supported''',
        {
            'not-supported':'not_supported',
        }, 'Cisco-IOS-XR-qos-ma-cfg', _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-qos-ma-cfg']),
    'QosPolicyAccount' : _MetaInfoEnum('QosPolicyAccount',
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_qos_ma_cfg', 'QosPolicyAccount',
        '''Qos policy account''',
        {
            'layer1':'layer1',
            'layer2':'layer2',
            'nolayer2':'nolayer2',
            'user-defined':'user_defined',
        }, 'Cisco-IOS-XR-qos-ma-cfg', _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-qos-ma-cfg']),
    'Qos' : {
        'meta_info' : _MetaInfoClass('Qos', REFERENCE_CLASS,
            '''Global QOS configuration.''',
            False, 
            [
            _MetaInfoClassMember('fabric-service-policy', ATTRIBUTE, 'str', 'xr:Cisco-ios-xr-string',
                None, None,
                [(0, 63)], [],
                '''                Name of the fabric service policy
                ''',
                'fabric_service_policy',
                'Cisco-IOS-XR-qos-ma-cfg', False),
            ],
            'Cisco-IOS-XR-qos-ma-cfg',
            'qos',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-qos-ma-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_qos_ma_cfg',
        ),
    },
}
