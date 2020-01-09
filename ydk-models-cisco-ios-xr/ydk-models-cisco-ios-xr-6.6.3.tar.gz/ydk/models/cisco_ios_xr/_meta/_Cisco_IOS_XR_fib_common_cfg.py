
'''
This is auto-generated file,
which includes metadata for module Cisco_IOS_XR_fib_common_cfg
'''

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_LIST, REFERENCE_LEAFLIST, REFERENCE_BITS, REFERENCE_UNION
from ydk._core._dm_meta_info import REFERENCE_CLASS, REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, ANYXML_CLASS
from ydk._core._importer import _yang_ns

_meta_table = {
    'FibPbtsForwardClass' : _MetaInfoEnum('FibPbtsForwardClass',
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_fib_common_cfg', 'FibPbtsForwardClass',
        ''' ''',
        {
            'any':'any',
        }, 'Cisco-IOS-XR-fib-common-cfg', _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-fib-common-cfg']),
    'FibPbtsFallback' : _MetaInfoEnum('FibPbtsFallback',
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_fib_common_cfg', 'FibPbtsFallback',
        '''Fib pbts fallback''',
        {
            'list':'list',
            'any':'any',
            'drop':'drop',
        }, 'Cisco-IOS-XR-fib-common-cfg', _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-fib-common-cfg']),
    'Fib.PbtsForwardClassFallbacks.PbtsForwardClassFallback' : {
        'meta_info' : _MetaInfoClass('Fib.PbtsForwardClassFallbacks.PbtsForwardClassFallback', REFERENCE_LIST,
            '''Set PBTS class for fallback''',
            False, 
            [
            _MetaInfoClassMember('forward-class-number', REFERENCE_UNION, 'str', 'Fib-pbts-forward-class',
                None, None,
                [], [],
                '''                PBTS forward class number
                ''',
                'forward_class_number',
                'Cisco-IOS-XR-fib-common-cfg', True, [
                    _MetaInfoClassMember('forward-class-number', REFERENCE_ENUM_CLASS, 'FibPbtsForwardClass', 'enumeration',
                        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_fib_common_cfg', 'FibPbtsForwardClass',
                        [], [],
                        '''                        PBTS forward class number
                        ''',
                        'forward_class_number',
                        'Cisco-IOS-XR-fib-common-cfg', True),
                    _MetaInfoClassMember('forward-class-number', ATTRIBUTE, 'int', 'uint32',
                        None, None,
                        [('0', '8')], [],
                        '''                        PBTS forward class number
                        ''',
                        'forward_class_number',
                        'Cisco-IOS-XR-fib-common-cfg', True),
                ]),
            _MetaInfoClassMember('fallback-type', REFERENCE_ENUM_CLASS, 'FibPbtsFallback', 'Fib-pbts-fallback',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_fib_common_cfg', 'FibPbtsFallback',
                [], [],
                '''                Set PBTS fallback type
                ''',
                'fallback_type',
                'Cisco-IOS-XR-fib-common-cfg', False, is_mandatory=True),
            _MetaInfoClassMember('fallback-class-number-array', REFERENCE_LEAFLIST, 'int', 'uint32',
                None, None,
                [('0', '7')], [],
                '''                Set PBTS fallback class number array
                ''',
                'fallback_class_number_array',
                'Cisco-IOS-XR-fib-common-cfg', False, max_elements=7),
            ],
            'Cisco-IOS-XR-fib-common-cfg',
            'pbts-forward-class-fallback',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-fib-common-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_fib_common_cfg',
        ),
    },
    'Fib.PbtsForwardClassFallbacks' : {
        'meta_info' : _MetaInfoClass('Fib.PbtsForwardClassFallbacks', REFERENCE_CLASS,
            '''PBTS class configuration''',
            False, 
            [
            _MetaInfoClassMember('pbts-forward-class-fallback', REFERENCE_LIST, 'PbtsForwardClassFallback', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_fib_common_cfg', 'Fib.PbtsForwardClassFallbacks.PbtsForwardClassFallback',
                [], [],
                '''                Set PBTS class for fallback
                ''',
                'pbts_forward_class_fallback',
                'Cisco-IOS-XR-fib-common-cfg', False),
            ],
            'Cisco-IOS-XR-fib-common-cfg',
            'pbts-forward-class-fallbacks',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-fib-common-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_fib_common_cfg',
        ),
    },
    'Fib.Platform.LabelSwitchedMulticast' : {
        'meta_info' : _MetaInfoClass('Fib.Platform.LabelSwitchedMulticast', REFERENCE_CLASS,
            '''Options for label-switched-multicast parameters''',
            False, 
            [
            _MetaInfoClassMember('frr-holdtime', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('3', '180')], [],
                '''                Set time to keep FRR slots programmed post FRR
                ''',
                'frr_holdtime',
                'Cisco-IOS-XR-fib-common-cfg', False),
            ],
            'Cisco-IOS-XR-fib-common-cfg',
            'label-switched-multicast',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-fib-common-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_fib_common_cfg',
        ),
    },
    'Fib.Platform' : {
        'meta_info' : _MetaInfoClass('Fib.Platform', REFERENCE_CLASS,
            '''FIB platform parameters''',
            False, 
            [
            _MetaInfoClassMember('label-switched-multicast', REFERENCE_CLASS, 'LabelSwitchedMulticast', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_fib_common_cfg', 'Fib.Platform.LabelSwitchedMulticast',
                [], [],
                '''                Options for label-switched-multicast parameters
                ''',
                'label_switched_multicast',
                'Cisco-IOS-XR-fib-common-cfg', False),
            ],
            'Cisco-IOS-XR-fib-common-cfg',
            'platform',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-fib-common-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_fib_common_cfg',
        ),
    },
    'Fib' : {
        'meta_info' : _MetaInfoClass('Fib', REFERENCE_CLASS,
            '''CEF configuration''',
            False, 
            [
            _MetaInfoClassMember('pbts-forward-class-fallbacks', REFERENCE_CLASS, 'PbtsForwardClassFallbacks', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_fib_common_cfg', 'Fib.PbtsForwardClassFallbacks',
                [], [],
                '''                PBTS class configuration
                ''',
                'pbts_forward_class_fallbacks',
                'Cisco-IOS-XR-fib-common-cfg', False),
            _MetaInfoClassMember('platform', REFERENCE_CLASS, 'Platform', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_fib_common_cfg', 'Fib.Platform',
                [], [],
                '''                FIB platform parameters
                ''',
                'platform',
                'Cisco-IOS-XR-fib-common-cfg', False),
            _MetaInfoClassMember('auto-hash-recover', ATTRIBUTE, 'bool', 'boolean',
                None, None,
                [], [],
                '''                Set option for automatcially recovering
                consistent-hashing state on interface up
                ''',
                'auto_hash_recover',
                'Cisco-IOS-XR-fib-common-cfg', False),
            _MetaInfoClassMember('prefer-aib-routes', ATTRIBUTE, 'bool', 'boolean',
                None, None,
                [], [],
                '''                Set options for adjacency routes overriding RIB
                routes
                ''',
                'prefer_aib_routes',
                'Cisco-IOS-XR-fib-common-cfg', False),
            _MetaInfoClassMember('encap-sharing-disable', ATTRIBUTE, 'bool', 'boolean',
                None, None,
                [], [],
                '''                Set true to disable encapsulation sharing
                ''',
                'encap_sharing_disable',
                'Cisco-IOS-XR-fib-common-cfg', False),
            _MetaInfoClassMember('frr-follow-bgp-pic', ATTRIBUTE, 'bool', 'boolean',
                None, None,
                [], [],
                '''                Set option for fast-reroute to follow BGP PIC
                update, not to wait for timeout
                ''',
                'frr_follow_bgp_pic',
                'Cisco-IOS-XR-fib-common-cfg', False),
            ],
            'Cisco-IOS-XR-fib-common-cfg',
            'fib',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-fib-common-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_fib_common_cfg',
        ),
    },
}
_meta_table['Fib.PbtsForwardClassFallbacks.PbtsForwardClassFallback']['meta_info'].parent =_meta_table['Fib.PbtsForwardClassFallbacks']['meta_info']
_meta_table['Fib.Platform.LabelSwitchedMulticast']['meta_info'].parent =_meta_table['Fib.Platform']['meta_info']
_meta_table['Fib.PbtsForwardClassFallbacks']['meta_info'].parent =_meta_table['Fib']['meta_info']
_meta_table['Fib.Platform']['meta_info'].parent =_meta_table['Fib']['meta_info']
