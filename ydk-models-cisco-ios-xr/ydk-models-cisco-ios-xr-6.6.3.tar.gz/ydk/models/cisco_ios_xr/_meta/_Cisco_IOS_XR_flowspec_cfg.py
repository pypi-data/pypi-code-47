
'''
This is auto-generated file,
which includes metadata for module Cisco_IOS_XR_flowspec_cfg
'''

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_LIST, REFERENCE_LEAFLIST, REFERENCE_BITS, REFERENCE_UNION
from ydk._core._dm_meta_info import REFERENCE_CLASS, REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, ANYXML_CLASS
from ydk._core._importer import _yang_ns

_meta_table = {
    'FsVrfAf' : _MetaInfoEnum('FsVrfAf',
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_flowspec_cfg', 'FsVrfAf',
        '''Fs vrf af''',
        {
            'ipv4':'ipv4',
            'ipv6':'ipv6',
        }, 'Cisco-IOS-XR-flowspec-cfg', _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-flowspec-cfg']),
    'FsAfP' : _MetaInfoEnum('FsAfP',
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_flowspec_cfg', 'FsAfP',
        '''Fs af p''',
        {
            'pbr':'pbr',
        }, 'Cisco-IOS-XR-flowspec-cfg', _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-flowspec-cfg']),
    'FsAddf' : _MetaInfoEnum('FsAddf',
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_flowspec_cfg', 'FsAddf',
        '''Fs addf''',
        {
            'ipv4':'ipv4',
            'ipv6':'ipv6',
        }, 'Cisco-IOS-XR-flowspec-cfg', _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-flowspec-cfg']),
    'FsVrfAfP' : _MetaInfoEnum('FsVrfAfP',
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_flowspec_cfg', 'FsVrfAfP',
        '''Fs vrf af p''',
        {
            'pbr':'pbr',
        }, 'Cisco-IOS-XR-flowspec-cfg', _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-flowspec-cfg']),
    'FlowSpec.Afs.Af.ServicePolicies.ServicePolicy' : {
        'meta_info' : _MetaInfoClass('FlowSpec.Afs.Af.ServicePolicies.ServicePolicy', REFERENCE_LIST,
            '''Service Policy configuration''',
            False, 
            [
            _MetaInfoClassMember('policy-type', REFERENCE_ENUM_CLASS, 'FsAfP', 'Fs-af-p',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_flowspec_cfg', 'FsAfP',
                [], [],
                '''                Choose the Policy type
                ''',
                'policy_type',
                'Cisco-IOS-XR-flowspec-cfg', True),
            _MetaInfoClassMember('policy-name', ATTRIBUTE, 'str', 'xr:Cisco-ios-xr-string',
                None, None,
                [], [b'[\\w\\-\\.:,_@#%$\\+=\\|;]+'],
                '''                Policy map name
                ''',
                'policy_name',
                'Cisco-IOS-XR-flowspec-cfg', True),
            _MetaInfoClassMember('local', ATTRIBUTE, 'bool', 'boolean',
                None, None,
                [], [],
                '''                Set constant integer
                ''',
                'local',
                'Cisco-IOS-XR-flowspec-cfg', False, is_mandatory=True),
            ],
            'Cisco-IOS-XR-flowspec-cfg',
            'service-policy',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-flowspec-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_flowspec_cfg',
        ),
    },
    'FlowSpec.Afs.Af.ServicePolicies' : {
        'meta_info' : _MetaInfoClass('FlowSpec.Afs.Af.ServicePolicies', REFERENCE_CLASS,
            '''Table of ServicePolicy''',
            False, 
            [
            _MetaInfoClassMember('service-policy', REFERENCE_LIST, 'ServicePolicy', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_flowspec_cfg', 'FlowSpec.Afs.Af.ServicePolicies.ServicePolicy',
                [], [],
                '''                Service Policy configuration
                ''',
                'service_policy',
                'Cisco-IOS-XR-flowspec-cfg', False),
            ],
            'Cisco-IOS-XR-flowspec-cfg',
            'service-policies',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-flowspec-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_flowspec_cfg',
        ),
    },
    'FlowSpec.Afs.Af' : {
        'meta_info' : _MetaInfoClass('FlowSpec.Afs.Af', REFERENCE_LIST,
            '''Address Family Identifier Type (IPv4/IPv6)''',
            False, 
            [
            _MetaInfoClassMember('af-name', REFERENCE_ENUM_CLASS, 'FsAddf', 'Fs-addf',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_flowspec_cfg', 'FsAddf',
                [], [],
                '''                AFI type
                ''',
                'af_name',
                'Cisco-IOS-XR-flowspec-cfg', True),
            _MetaInfoClassMember('service-policies', REFERENCE_CLASS, 'ServicePolicies', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_flowspec_cfg', 'FlowSpec.Afs.Af.ServicePolicies',
                [], [],
                '''                Table of ServicePolicy
                ''',
                'service_policies',
                'Cisco-IOS-XR-flowspec-cfg', False),
            _MetaInfoClassMember('interface-all', ATTRIBUTE, 'Empty', 'empty',
                None, None,
                [], [],
                '''                Install FlowSpec policy on all interfaces
                ''',
                'interface_all',
                'Cisco-IOS-XR-flowspec-cfg', False),
            ],
            'Cisco-IOS-XR-flowspec-cfg',
            'af',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-flowspec-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_flowspec_cfg',
        ),
    },
    'FlowSpec.Afs' : {
        'meta_info' : _MetaInfoClass('FlowSpec.Afs', REFERENCE_CLASS,
            '''Table of AF''',
            False, 
            [
            _MetaInfoClassMember('af', REFERENCE_LIST, 'Af', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_flowspec_cfg', 'FlowSpec.Afs.Af',
                [], [],
                '''                Address Family Identifier Type (IPv4/IPv6)
                ''',
                'af',
                'Cisco-IOS-XR-flowspec-cfg', False),
            ],
            'Cisco-IOS-XR-flowspec-cfg',
            'afs',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-flowspec-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_flowspec_cfg',
        ),
    },
    'FlowSpec.Vrfs.Vrf.Afs.Af.ServicePolicies.ServicePolicy' : {
        'meta_info' : _MetaInfoClass('FlowSpec.Vrfs.Vrf.Afs.Af.ServicePolicies.ServicePolicy', REFERENCE_LIST,
            '''Service Policy configuration''',
            False, 
            [
            _MetaInfoClassMember('policy-type', REFERENCE_ENUM_CLASS, 'FsAfP', 'Fs-af-p',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_flowspec_cfg', 'FsAfP',
                [], [],
                '''                Choose the Policy type
                ''',
                'policy_type',
                'Cisco-IOS-XR-flowspec-cfg', True),
            _MetaInfoClassMember('policy-name', ATTRIBUTE, 'str', 'xr:Cisco-ios-xr-string',
                None, None,
                [], [b'[\\w\\-\\.:,_@#%$\\+=\\|;]+'],
                '''                Policy map name
                ''',
                'policy_name',
                'Cisco-IOS-XR-flowspec-cfg', True),
            _MetaInfoClassMember('local', ATTRIBUTE, 'bool', 'boolean',
                None, None,
                [], [],
                '''                Set constant integer
                ''',
                'local',
                'Cisco-IOS-XR-flowspec-cfg', False, is_mandatory=True),
            ],
            'Cisco-IOS-XR-flowspec-cfg',
            'service-policy',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-flowspec-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_flowspec_cfg',
        ),
    },
    'FlowSpec.Vrfs.Vrf.Afs.Af.ServicePolicies' : {
        'meta_info' : _MetaInfoClass('FlowSpec.Vrfs.Vrf.Afs.Af.ServicePolicies', REFERENCE_CLASS,
            '''Table of ServicePolicy''',
            False, 
            [
            _MetaInfoClassMember('service-policy', REFERENCE_LIST, 'ServicePolicy', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_flowspec_cfg', 'FlowSpec.Vrfs.Vrf.Afs.Af.ServicePolicies.ServicePolicy',
                [], [],
                '''                Service Policy configuration
                ''',
                'service_policy',
                'Cisco-IOS-XR-flowspec-cfg', False),
            ],
            'Cisco-IOS-XR-flowspec-cfg',
            'service-policies',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-flowspec-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_flowspec_cfg',
        ),
    },
    'FlowSpec.Vrfs.Vrf.Afs.Af' : {
        'meta_info' : _MetaInfoClass('FlowSpec.Vrfs.Vrf.Afs.Af', REFERENCE_LIST,
            '''Address Family Identifier Type (IPv4/IPv6)''',
            False, 
            [
            _MetaInfoClassMember('af-name', REFERENCE_ENUM_CLASS, 'FsVrfAf', 'Fs-vrf-af',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_flowspec_cfg', 'FsVrfAf',
                [], [],
                '''                AFI type
                ''',
                'af_name',
                'Cisco-IOS-XR-flowspec-cfg', True),
            _MetaInfoClassMember('service-policies', REFERENCE_CLASS, 'ServicePolicies', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_flowspec_cfg', 'FlowSpec.Vrfs.Vrf.Afs.Af.ServicePolicies',
                [], [],
                '''                Table of ServicePolicy
                ''',
                'service_policies',
                'Cisco-IOS-XR-flowspec-cfg', False),
            _MetaInfoClassMember('interface-all', ATTRIBUTE, 'Empty', 'empty',
                None, None,
                [], [],
                '''                Install FlowSpec policy on all interfaces
                ''',
                'interface_all',
                'Cisco-IOS-XR-flowspec-cfg', False),
            ],
            'Cisco-IOS-XR-flowspec-cfg',
            'af',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-flowspec-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_flowspec_cfg',
        ),
    },
    'FlowSpec.Vrfs.Vrf.Afs' : {
        'meta_info' : _MetaInfoClass('FlowSpec.Vrfs.Vrf.Afs', REFERENCE_CLASS,
            '''Table of AF''',
            False, 
            [
            _MetaInfoClassMember('af', REFERENCE_LIST, 'Af', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_flowspec_cfg', 'FlowSpec.Vrfs.Vrf.Afs.Af',
                [], [],
                '''                Address Family Identifier Type (IPv4/IPv6)
                ''',
                'af',
                'Cisco-IOS-XR-flowspec-cfg', False),
            ],
            'Cisco-IOS-XR-flowspec-cfg',
            'afs',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-flowspec-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_flowspec_cfg',
        ),
    },
    'FlowSpec.Vrfs.Vrf' : {
        'meta_info' : _MetaInfoClass('FlowSpec.Vrfs.Vrf', REFERENCE_LIST,
            '''VRF configuration''',
            False, 
            [
            _MetaInfoClassMember('vrf-name', ATTRIBUTE, 'str', 'xr:Cisco-ios-xr-string',
                None, None,
                [(1, 32)], [],
                '''                VRF Name
                ''',
                'vrf_name',
                'Cisco-IOS-XR-flowspec-cfg', True),
            _MetaInfoClassMember('afs', REFERENCE_CLASS, 'Afs', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_flowspec_cfg', 'FlowSpec.Vrfs.Vrf.Afs',
                [], [],
                '''                Table of AF
                ''',
                'afs',
                'Cisco-IOS-XR-flowspec-cfg', False),
            ],
            'Cisco-IOS-XR-flowspec-cfg',
            'vrf',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-flowspec-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_flowspec_cfg',
        ),
    },
    'FlowSpec.Vrfs' : {
        'meta_info' : _MetaInfoClass('FlowSpec.Vrfs', REFERENCE_CLASS,
            '''Table of VRF''',
            False, 
            [
            _MetaInfoClassMember('vrf', REFERENCE_LIST, 'Vrf', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_flowspec_cfg', 'FlowSpec.Vrfs.Vrf',
                [], [],
                '''                VRF configuration
                ''',
                'vrf',
                'Cisco-IOS-XR-flowspec-cfg', False),
            ],
            'Cisco-IOS-XR-flowspec-cfg',
            'vrfs',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-flowspec-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_flowspec_cfg',
        ),
    },
    'FlowSpec' : {
        'meta_info' : _MetaInfoClass('FlowSpec', REFERENCE_CLASS,
            '''FlowSpec configuration''',
            False, 
            [
            _MetaInfoClassMember('afs', REFERENCE_CLASS, 'Afs', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_flowspec_cfg', 'FlowSpec.Afs',
                [], [],
                '''                Table of AF
                ''',
                'afs',
                'Cisco-IOS-XR-flowspec-cfg', False),
            _MetaInfoClassMember('vrfs', REFERENCE_CLASS, 'Vrfs', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_flowspec_cfg', 'FlowSpec.Vrfs',
                [], [],
                '''                Table of VRF
                ''',
                'vrfs',
                'Cisco-IOS-XR-flowspec-cfg', False),
            _MetaInfoClassMember('enable', ATTRIBUTE, 'Empty', 'empty',
                None, None,
                [], [],
                '''                Enable FlowSpec configuration. Deletion of this
                object also causes deletion of all associated
                objects under FlowSpec.
                ''',
                'enable',
                'Cisco-IOS-XR-flowspec-cfg', False),
            _MetaInfoClassMember('interface-all', ATTRIBUTE, 'Empty', 'empty',
                None, None,
                [], [],
                '''                Install FlowSpec policy on all interfaces
                ''',
                'interface_all',
                'Cisco-IOS-XR-flowspec-cfg', False),
            ],
            'Cisco-IOS-XR-flowspec-cfg',
            'flow-spec',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-flowspec-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_flowspec_cfg',
        ),
    },
}
_meta_table['FlowSpec.Afs.Af.ServicePolicies.ServicePolicy']['meta_info'].parent =_meta_table['FlowSpec.Afs.Af.ServicePolicies']['meta_info']
_meta_table['FlowSpec.Afs.Af.ServicePolicies']['meta_info'].parent =_meta_table['FlowSpec.Afs.Af']['meta_info']
_meta_table['FlowSpec.Afs.Af']['meta_info'].parent =_meta_table['FlowSpec.Afs']['meta_info']
_meta_table['FlowSpec.Vrfs.Vrf.Afs.Af.ServicePolicies.ServicePolicy']['meta_info'].parent =_meta_table['FlowSpec.Vrfs.Vrf.Afs.Af.ServicePolicies']['meta_info']
_meta_table['FlowSpec.Vrfs.Vrf.Afs.Af.ServicePolicies']['meta_info'].parent =_meta_table['FlowSpec.Vrfs.Vrf.Afs.Af']['meta_info']
_meta_table['FlowSpec.Vrfs.Vrf.Afs.Af']['meta_info'].parent =_meta_table['FlowSpec.Vrfs.Vrf.Afs']['meta_info']
_meta_table['FlowSpec.Vrfs.Vrf.Afs']['meta_info'].parent =_meta_table['FlowSpec.Vrfs.Vrf']['meta_info']
_meta_table['FlowSpec.Vrfs.Vrf']['meta_info'].parent =_meta_table['FlowSpec.Vrfs']['meta_info']
_meta_table['FlowSpec.Afs']['meta_info'].parent =_meta_table['FlowSpec']['meta_info']
_meta_table['FlowSpec.Vrfs']['meta_info'].parent =_meta_table['FlowSpec']['meta_info']
