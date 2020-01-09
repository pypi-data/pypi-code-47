
'''
This is auto-generated file,
which includes metadata for module Cisco_IOS_XR_infra_statsd_act
'''

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_LIST, REFERENCE_LEAFLIST, REFERENCE_BITS, REFERENCE_UNION
from ydk._core._dm_meta_info import REFERENCE_CLASS, REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, ANYXML_CLASS
from ydk._core._importer import _yang_ns

_meta_table = {
    'ClearCountersController.Input' : {
        'meta_info' : _MetaInfoClass('ClearCountersController.Input', REFERENCE_CLASS,
            ''' ''',
            False, 
            [
            _MetaInfoClassMember('controller-name', ATTRIBUTE, 'str', 'csc:Interface-name',
                None, None,
                [], [b'[a-zA-Z0-9._/-]+'],
                '''                Controller name
                ''',
                'controller_name',
                'Cisco-IOS-XR-infra-statsd-act', False, is_mandatory=True),
            ],
            'Cisco-IOS-XR-infra-statsd-act',
            'input',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-infra-statsd-act'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_statsd_act',
        ),
    },
    'ClearCountersController' : {
        'meta_info' : _MetaInfoClass('ClearCountersController', REFERENCE_CLASS,
            '''Controller name.
''',
            False, 
            [
            _MetaInfoClassMember('input', REFERENCE_CLASS, 'Input', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_statsd_act', 'ClearCountersController.Input',
                [], [],
                '''                ''',
                'input',
                'Cisco-IOS-XR-infra-statsd-act', False),
            ],
            'Cisco-IOS-XR-infra-statsd-act',
            'clear-counters-controller',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-infra-statsd-act'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_statsd_act',
        ),
    },
    'ClearCountersAll' : {
        'meta_info' : _MetaInfoClass('ClearCountersAll', REFERENCE_CLASS,
            '''Clear counters on all interfaces.
''',
            False, 
            [
            ],
            'Cisco-IOS-XR-infra-statsd-act',
            'clear-counters-all',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-infra-statsd-act'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_statsd_act',
        ),
    },
    'ClearCountersInterface.Input' : {
        'meta_info' : _MetaInfoClass('ClearCountersInterface.Input', REFERENCE_CLASS,
            ''' ''',
            False, 
            [
            _MetaInfoClassMember('interface-name', ATTRIBUTE, 'str', 'csc:Interface-name',
                None, None,
                [], [b'[a-zA-Z0-9._/-]+'],
                '''                Interface name
                ''',
                'interface_name',
                'Cisco-IOS-XR-infra-statsd-act', False, is_mandatory=True),
            ],
            'Cisco-IOS-XR-infra-statsd-act',
            'input',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-infra-statsd-act'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_statsd_act',
        ),
    },
    'ClearCountersInterface' : {
        'meta_info' : _MetaInfoClass('ClearCountersInterface', REFERENCE_CLASS,
            '''Clear counters for interface.
''',
            False, 
            [
            _MetaInfoClassMember('input', REFERENCE_CLASS, 'Input', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_statsd_act', 'ClearCountersInterface.Input',
                [], [],
                '''                ''',
                'input',
                'Cisco-IOS-XR-infra-statsd-act', False),
            ],
            'Cisco-IOS-XR-infra-statsd-act',
            'clear-counters-interface',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-infra-statsd-act'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_statsd_act',
        ),
    },
}
_meta_table['ClearCountersController.Input']['meta_info'].parent =_meta_table['ClearCountersController']['meta_info']
_meta_table['ClearCountersInterface.Input']['meta_info'].parent =_meta_table['ClearCountersInterface']['meta_info']
