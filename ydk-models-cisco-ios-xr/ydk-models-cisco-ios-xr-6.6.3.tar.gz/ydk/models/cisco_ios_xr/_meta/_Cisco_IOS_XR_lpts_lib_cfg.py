
'''
This is auto-generated file,
which includes metadata for module Cisco_IOS_XR_lpts_lib_cfg
'''

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_LIST, REFERENCE_LEAFLIST, REFERENCE_BITS, REFERENCE_UNION
from ydk._core._dm_meta_info import REFERENCE_CLASS, REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, ANYXML_CLASS
from ydk._core._importer import _yang_ns

_meta_table = {
    'Lpts.Ipolicer.Acls.Acl.AfiTypes.AfiType.VrfNames.VrfName' : {
        'meta_info' : _MetaInfoClass('Lpts.Ipolicer.Acls.Acl.AfiTypes.AfiType.VrfNames.VrfName', REFERENCE_LIST,
            '''VRF name''',
            False, 
            [
            _MetaInfoClassMember('vrf-name', ATTRIBUTE, 'str', 'xr:Cisco-ios-xr-string',
                None, None,
                [], [b'[\\w\\-\\.:,_@#%$\\+=\\|;]+'],
                '''                VRF name
                ''',
                'vrf_name',
                'Cisco-IOS-XR-lpts-pre-ifib-cfg', True),
            _MetaInfoClassMember('acl-rate', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('0', '100000')], [],
                '''                pre-ifib policer rate config commands
                ''',
                'acl_rate',
                'Cisco-IOS-XR-lpts-pre-ifib-cfg', False),
            ],
            'Cisco-IOS-XR-lpts-pre-ifib-cfg',
            'vrf-name',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-lpts-pre-ifib-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lpts_lib_cfg',
        ),
    },
    'Lpts.Ipolicer.Acls.Acl.AfiTypes.AfiType.VrfNames' : {
        'meta_info' : _MetaInfoClass('Lpts.Ipolicer.Acls.Acl.AfiTypes.AfiType.VrfNames', REFERENCE_CLASS,
            '''VRF list''',
            False, 
            [
            _MetaInfoClassMember('vrf-name', REFERENCE_LIST, 'VrfName', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lpts_lib_cfg', 'Lpts.Ipolicer.Acls.Acl.AfiTypes.AfiType.VrfNames.VrfName',
                [], [],
                '''                VRF name
                ''',
                'vrf_name',
                'Cisco-IOS-XR-lpts-pre-ifib-cfg', False),
            ],
            'Cisco-IOS-XR-lpts-pre-ifib-cfg',
            'vrf-names',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-lpts-pre-ifib-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lpts_lib_cfg',
        ),
    },
    'Lpts.Ipolicer.Acls.Acl.AfiTypes.AfiType' : {
        'meta_info' : _MetaInfoClass('Lpts.Ipolicer.Acls.Acl.AfiTypes.AfiType', REFERENCE_LIST,
            '''AFI Family type''',
            False, 
            [
            _MetaInfoClassMember('afi-family-type', REFERENCE_ENUM_CLASS, 'Lptsafi', 'Lptsafi',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lpts_pre_ifib_cfg', 'Lptsafi',
                [], [],
                '''                AFI Family Type
                ''',
                'afi_family_type',
                'Cisco-IOS-XR-lpts-pre-ifib-cfg', True),
            _MetaInfoClassMember('vrf-names', REFERENCE_CLASS, 'VrfNames', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lpts_lib_cfg', 'Lpts.Ipolicer.Acls.Acl.AfiTypes.AfiType.VrfNames',
                [], [],
                '''                VRF list
                ''',
                'vrf_names',
                'Cisco-IOS-XR-lpts-pre-ifib-cfg', False),
            ],
            'Cisco-IOS-XR-lpts-pre-ifib-cfg',
            'afi-type',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-lpts-pre-ifib-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lpts_lib_cfg',
        ),
    },
    'Lpts.Ipolicer.Acls.Acl.AfiTypes' : {
        'meta_info' : _MetaInfoClass('Lpts.Ipolicer.Acls.Acl.AfiTypes', REFERENCE_CLASS,
            '''AFI Family''',
            False, 
            [
            _MetaInfoClassMember('afi-type', REFERENCE_LIST, 'AfiType', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lpts_lib_cfg', 'Lpts.Ipolicer.Acls.Acl.AfiTypes.AfiType',
                [], [],
                '''                AFI Family type
                ''',
                'afi_type',
                'Cisco-IOS-XR-lpts-pre-ifib-cfg', False),
            ],
            'Cisco-IOS-XR-lpts-pre-ifib-cfg',
            'afi-types',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-lpts-pre-ifib-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lpts_lib_cfg',
        ),
    },
    'Lpts.Ipolicer.Acls.Acl' : {
        'meta_info' : _MetaInfoClass('Lpts.Ipolicer.Acls.Acl', REFERENCE_LIST,
            '''ACL name''',
            False, 
            [
            _MetaInfoClassMember('acl-name', ATTRIBUTE, 'str', 'xr:Cisco-ios-xr-string',
                None, None,
                [], [b'[\\w\\-\\.:,_@#%$\\+=\\|;]+'],
                '''                ACL name
                ''',
                'acl_name',
                'Cisco-IOS-XR-lpts-pre-ifib-cfg', True),
            _MetaInfoClassMember('afi-types', REFERENCE_CLASS, 'AfiTypes', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lpts_lib_cfg', 'Lpts.Ipolicer.Acls.Acl.AfiTypes',
                [], [],
                '''                AFI Family
                ''',
                'afi_types',
                'Cisco-IOS-XR-lpts-pre-ifib-cfg', False),
            ],
            'Cisco-IOS-XR-lpts-pre-ifib-cfg',
            'acl',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-lpts-pre-ifib-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lpts_lib_cfg',
        ),
    },
    'Lpts.Ipolicer.Acls' : {
        'meta_info' : _MetaInfoClass('Lpts.Ipolicer.Acls', REFERENCE_CLASS,
            '''Table for ACLs''',
            False, 
            [
            _MetaInfoClassMember('acl', REFERENCE_LIST, 'Acl', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lpts_lib_cfg', 'Lpts.Ipolicer.Acls.Acl',
                [], [],
                '''                ACL name
                ''',
                'acl',
                'Cisco-IOS-XR-lpts-pre-ifib-cfg', False),
            ],
            'Cisco-IOS-XR-lpts-pre-ifib-cfg',
            'acls',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-lpts-pre-ifib-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lpts_lib_cfg',
        ),
    },
    'Lpts.Ipolicer.PolicerDomains.PolicerDomain.Flows.Flow.Precedences' : {
        'meta_info' : _MetaInfoClass('Lpts.Ipolicer.PolicerDomains.PolicerDomain.Flows.Flow.Precedences', REFERENCE_CLASS,
            '''TOS Precedence value(s)''',
            False, 
            [
            _MetaInfoClassMember('precedence', REFERENCE_UNION, 'str', 'Lpts-pre-i-fib-precedence-number',
                None, None,
                [], [],
                '''                Precedence values
                ''',
                'precedence',
                'Cisco-IOS-XR-lpts-pre-ifib-cfg', False, [
                    _MetaInfoClassMember('precedence', REFERENCE_LEAFLIST, 'LptsPreIFibPrecedenceNumber', 'enumeration',
                        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lpts_pre_ifib_cfg', 'LptsPreIFibPrecedenceNumber',
                        [], [],
                        '''                        Precedence values
                        ''',
                        'precedence',
                        'Cisco-IOS-XR-lpts-pre-ifib-cfg', False, max_elements=8),
                    _MetaInfoClassMember('precedence', REFERENCE_LEAFLIST, 'int', 'uint32',
                        None, None,
                        [('0', '7')], [],
                        '''                        Precedence values
                        ''',
                        'precedence',
                        'Cisco-IOS-XR-lpts-pre-ifib-cfg', False, max_elements=8),
                ], max_elements=8),
            ],
            'Cisco-IOS-XR-lpts-pre-ifib-cfg',
            'precedences',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-lpts-pre-ifib-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lpts_lib_cfg',
        ),
    },
    'Lpts.Ipolicer.PolicerDomains.PolicerDomain.Flows.Flow' : {
        'meta_info' : _MetaInfoClass('Lpts.Ipolicer.PolicerDomains.PolicerDomain.Flows.Flow', REFERENCE_LIST,
            '''selected flow type''',
            False, 
            [
            _MetaInfoClassMember('flow-type', REFERENCE_ENUM_CLASS, 'LptsFlow', 'Lpts-flow',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lpts_pre_ifib_cfg', 'LptsFlow',
                [], [],
                '''                LPTS Flow Type
                ''',
                'flow_type',
                'Cisco-IOS-XR-lpts-pre-ifib-cfg', True),
            _MetaInfoClassMember('precedences', REFERENCE_CLASS, 'Precedences', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lpts_lib_cfg', 'Lpts.Ipolicer.PolicerDomains.PolicerDomain.Flows.Flow.Precedences',
                [], [],
                '''                TOS Precedence value(s)
                ''',
                'precedences',
                'Cisco-IOS-XR-lpts-pre-ifib-cfg', False),
            _MetaInfoClassMember('rate', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('0', '4294967295')], [],
                '''                Configured rate value
                ''',
                'rate',
                'Cisco-IOS-XR-lpts-pre-ifib-cfg', False),
            ],
            'Cisco-IOS-XR-lpts-pre-ifib-cfg',
            'flow',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-lpts-pre-ifib-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lpts_lib_cfg',
        ),
    },
    'Lpts.Ipolicer.PolicerDomains.PolicerDomain.Flows' : {
        'meta_info' : _MetaInfoClass('Lpts.Ipolicer.PolicerDomains.PolicerDomain.Flows', REFERENCE_CLASS,
            '''Table for Flows''',
            False, 
            [
            _MetaInfoClassMember('flow', REFERENCE_LIST, 'Flow', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lpts_lib_cfg', 'Lpts.Ipolicer.PolicerDomains.PolicerDomain.Flows.Flow',
                [], [],
                '''                selected flow type
                ''',
                'flow',
                'Cisco-IOS-XR-lpts-pre-ifib-cfg', False),
            ],
            'Cisco-IOS-XR-lpts-pre-ifib-cfg',
            'flows',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-lpts-pre-ifib-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lpts_lib_cfg',
        ),
    },
    'Lpts.Ipolicer.PolicerDomains.PolicerDomain' : {
        'meta_info' : _MetaInfoClass('Lpts.Ipolicer.PolicerDomains.PolicerDomain', REFERENCE_LIST,
            '''Domain name''',
            False, 
            [
            _MetaInfoClassMember('domain-name', ATTRIBUTE, 'str', 'xr:Cisco-ios-xr-string',
                None, None,
                [], [b'[\\w\\-\\.:,_@#%$\\+=\\|;]+'],
                '''                Domain name
                ''',
                'domain_name',
                'Cisco-IOS-XR-lpts-pre-ifib-cfg', True),
            _MetaInfoClassMember('flows', REFERENCE_CLASS, 'Flows', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lpts_lib_cfg', 'Lpts.Ipolicer.PolicerDomains.PolicerDomain.Flows',
                [], [],
                '''                Table for Flows
                ''',
                'flows',
                'Cisco-IOS-XR-lpts-pre-ifib-cfg', False),
            ],
            'Cisco-IOS-XR-lpts-pre-ifib-cfg',
            'policer-domain',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-lpts-pre-ifib-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lpts_lib_cfg',
        ),
    },
    'Lpts.Ipolicer.PolicerDomains' : {
        'meta_info' : _MetaInfoClass('Lpts.Ipolicer.PolicerDomains', REFERENCE_CLASS,
            '''Policer Domain Table''',
            False, 
            [
            _MetaInfoClassMember('policer-domain', REFERENCE_LIST, 'PolicerDomain', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lpts_lib_cfg', 'Lpts.Ipolicer.PolicerDomains.PolicerDomain',
                [], [],
                '''                Domain name
                ''',
                'policer_domain',
                'Cisco-IOS-XR-lpts-pre-ifib-cfg', False),
            ],
            'Cisco-IOS-XR-lpts-pre-ifib-cfg',
            'policer-domains',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-lpts-pre-ifib-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lpts_lib_cfg',
        ),
    },
    'Lpts.Ipolicer.Flows.Flow.Precedences' : {
        'meta_info' : _MetaInfoClass('Lpts.Ipolicer.Flows.Flow.Precedences', REFERENCE_CLASS,
            '''TOS Precedence value(s)''',
            False, 
            [
            _MetaInfoClassMember('precedence', REFERENCE_UNION, 'str', 'Lpts-pre-i-fib-precedence-number',
                None, None,
                [], [],
                '''                Precedence values
                ''',
                'precedence',
                'Cisco-IOS-XR-lpts-pre-ifib-cfg', False, [
                    _MetaInfoClassMember('precedence', REFERENCE_LEAFLIST, 'LptsPreIFibPrecedenceNumber', 'enumeration',
                        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lpts_pre_ifib_cfg', 'LptsPreIFibPrecedenceNumber',
                        [], [],
                        '''                        Precedence values
                        ''',
                        'precedence',
                        'Cisco-IOS-XR-lpts-pre-ifib-cfg', False, max_elements=8),
                    _MetaInfoClassMember('precedence', REFERENCE_LEAFLIST, 'int', 'uint32',
                        None, None,
                        [('0', '7')], [],
                        '''                        Precedence values
                        ''',
                        'precedence',
                        'Cisco-IOS-XR-lpts-pre-ifib-cfg', False, max_elements=8),
                ], max_elements=8),
            ],
            'Cisco-IOS-XR-lpts-pre-ifib-cfg',
            'precedences',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-lpts-pre-ifib-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lpts_lib_cfg',
        ),
    },
    'Lpts.Ipolicer.Flows.Flow' : {
        'meta_info' : _MetaInfoClass('Lpts.Ipolicer.Flows.Flow', REFERENCE_LIST,
            '''selected flow type''',
            False, 
            [
            _MetaInfoClassMember('flow-type', REFERENCE_ENUM_CLASS, 'LptsFlow', 'Lpts-flow',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lpts_pre_ifib_cfg', 'LptsFlow',
                [], [],
                '''                LPTS Flow Type
                ''',
                'flow_type',
                'Cisco-IOS-XR-lpts-pre-ifib-cfg', True),
            _MetaInfoClassMember('precedences', REFERENCE_CLASS, 'Precedences', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lpts_lib_cfg', 'Lpts.Ipolicer.Flows.Flow.Precedences',
                [], [],
                '''                TOS Precedence value(s)
                ''',
                'precedences',
                'Cisco-IOS-XR-lpts-pre-ifib-cfg', False),
            _MetaInfoClassMember('rate', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('0', '4294967295')], [],
                '''                Configured rate value
                ''',
                'rate',
                'Cisco-IOS-XR-lpts-pre-ifib-cfg', False),
            ],
            'Cisco-IOS-XR-lpts-pre-ifib-cfg',
            'flow',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-lpts-pre-ifib-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lpts_lib_cfg',
        ),
    },
    'Lpts.Ipolicer.Flows' : {
        'meta_info' : _MetaInfoClass('Lpts.Ipolicer.Flows', REFERENCE_CLASS,
            '''Table for Flows''',
            False, 
            [
            _MetaInfoClassMember('flow', REFERENCE_LIST, 'Flow', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lpts_lib_cfg', 'Lpts.Ipolicer.Flows.Flow',
                [], [],
                '''                selected flow type
                ''',
                'flow',
                'Cisco-IOS-XR-lpts-pre-ifib-cfg', False),
            ],
            'Cisco-IOS-XR-lpts-pre-ifib-cfg',
            'flows',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-lpts-pre-ifib-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lpts_lib_cfg',
        ),
    },
    'Lpts.Ipolicer' : {
        'meta_info' : _MetaInfoClass('Lpts.Ipolicer', REFERENCE_CLASS,
            '''Pre IFiB Policer Configuration ''',
            False, 
            [
            _MetaInfoClassMember('acls', REFERENCE_CLASS, 'Acls', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lpts_lib_cfg', 'Lpts.Ipolicer.Acls',
                [], [],
                '''                Table for ACLs
                ''',
                'acls',
                'Cisco-IOS-XR-lpts-pre-ifib-cfg', False),
            _MetaInfoClassMember('enable', ATTRIBUTE, 'Empty', 'empty',
                None, None,
                [], [],
                '''                Enabled
                ''',
                'enable',
                'Cisco-IOS-XR-lpts-pre-ifib-cfg', False, is_mandatory=True),
            _MetaInfoClassMember('policer-domains', REFERENCE_CLASS, 'PolicerDomains', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lpts_lib_cfg', 'Lpts.Ipolicer.PolicerDomains',
                [], [],
                '''                Policer Domain Table
                ''',
                'policer_domains',
                'Cisco-IOS-XR-lpts-pre-ifib-cfg', False),
            _MetaInfoClassMember('flows', REFERENCE_CLASS, 'Flows', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lpts_lib_cfg', 'Lpts.Ipolicer.Flows',
                [], [],
                '''                Table for Flows
                ''',
                'flows',
                'Cisco-IOS-XR-lpts-pre-ifib-cfg', False),
            ],
            'Cisco-IOS-XR-lpts-pre-ifib-cfg',
            'ipolicer',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-lpts-pre-ifib-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lpts_lib_cfg',
            is_presence=True,
        ),
    },
    'Lpts.DomainNames.DomainName.InterfaceNames.InterfaceName' : {
        'meta_info' : _MetaInfoClass('Lpts.DomainNames.DomainName.InterfaceNames.InterfaceName', REFERENCE_LIST,
            '''pre-ifib Domain Single interface
configuration''',
            False, 
            [
            _MetaInfoClassMember('domain-interface-name', ATTRIBUTE, 'str', 'xr:Interface-name',
                None, None,
                [], [b'[a-zA-Z0-9._/-]+'],
                '''                Interface Name
                ''',
                'domain_interface_name',
                'Cisco-IOS-XR-lpts-pre-ifib-cfg', True),
            _MetaInfoClassMember('domain-interface-name-xr', ATTRIBUTE, 'bool', 'boolean',
                None, None,
                [], [],
                '''                Enabled or disabled
                ''',
                'domain_interface_name_xr',
                'Cisco-IOS-XR-lpts-pre-ifib-cfg', False, is_mandatory=True),
            ],
            'Cisco-IOS-XR-lpts-pre-ifib-cfg',
            'interface-name',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-lpts-pre-ifib-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lpts_lib_cfg',
        ),
    },
    'Lpts.DomainNames.DomainName.InterfaceNames' : {
        'meta_info' : _MetaInfoClass('Lpts.DomainNames.DomainName.InterfaceNames', REFERENCE_CLASS,
            '''Domain Interface''',
            False, 
            [
            _MetaInfoClassMember('interface-name', REFERENCE_LIST, 'InterfaceName', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lpts_lib_cfg', 'Lpts.DomainNames.DomainName.InterfaceNames.InterfaceName',
                [], [],
                '''                pre-ifib Domain Single interface
                configuration
                ''',
                'interface_name',
                'Cisco-IOS-XR-lpts-pre-ifib-cfg', False),
            ],
            'Cisco-IOS-XR-lpts-pre-ifib-cfg',
            'interface-names',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-lpts-pre-ifib-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lpts_lib_cfg',
        ),
    },
    'Lpts.DomainNames.DomainName' : {
        'meta_info' : _MetaInfoClass('Lpts.DomainNames.DomainName', REFERENCE_LIST,
            '''Domain name''',
            False, 
            [
            _MetaInfoClassMember('domain-name', ATTRIBUTE, 'str', 'xr:Cisco-ios-xr-string',
                None, None,
                [], [b'[\\w\\-\\.:,_@#%$\\+=\\|;]+'],
                '''                Domain name
                ''',
                'domain_name',
                'Cisco-IOS-XR-lpts-pre-ifib-cfg', True),
            _MetaInfoClassMember('interface-names', REFERENCE_CLASS, 'InterfaceNames', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lpts_lib_cfg', 'Lpts.DomainNames.DomainName.InterfaceNames',
                [], [],
                '''                Domain Interface
                ''',
                'interface_names',
                'Cisco-IOS-XR-lpts-pre-ifib-cfg', False),
            ],
            'Cisco-IOS-XR-lpts-pre-ifib-cfg',
            'domain-name',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-lpts-pre-ifib-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lpts_lib_cfg',
        ),
    },
    'Lpts.DomainNames' : {
        'meta_info' : _MetaInfoClass('Lpts.DomainNames', REFERENCE_CLASS,
            '''Pre IFiB Domains Configuration ''',
            False, 
            [
            _MetaInfoClassMember('domain-name', REFERENCE_LIST, 'DomainName', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lpts_lib_cfg', 'Lpts.DomainNames.DomainName',
                [], [],
                '''                Domain name
                ''',
                'domain_name',
                'Cisco-IOS-XR-lpts-pre-ifib-cfg', False),
            ],
            'Cisco-IOS-XR-lpts-pre-ifib-cfg',
            'domain-names',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-lpts-pre-ifib-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lpts_lib_cfg',
        ),
    },
    'Lpts.IpuntPolicer.PuntTypeTable.PuntType.Rate' : {
        'meta_info' : _MetaInfoClass('Lpts.IpuntPolicer.PuntTypeTable.PuntType.Rate', REFERENCE_CLASS,
            '''Enable or Disable Punt Police and corresponding
Rate in PPS''',
            False, 
            [
            _MetaInfoClassMember('is-enabled', ATTRIBUTE, 'bool', 'boolean',
                None, None,
                [], [],
                '''                Is Punt Policer enabled
                ''',
                'is_enabled',
                'Cisco-IOS-XR-lpts-pre-ifib-cfg', False, is_mandatory=True),
            _MetaInfoClassMember('rate', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('0', '4294967295')], [],
                '''                Configured rate value
                ''',
                'rate',
                'Cisco-IOS-XR-lpts-pre-ifib-cfg', False),
            ],
            'Cisco-IOS-XR-lpts-pre-ifib-cfg',
            'rate',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-lpts-pre-ifib-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lpts_lib_cfg',
            is_presence=True,
        ),
    },
    'Lpts.IpuntPolicer.PuntTypeTable.PuntType' : {
        'meta_info' : _MetaInfoClass('Lpts.IpuntPolicer.PuntTypeTable.PuntType', REFERENCE_LIST,
            '''Punt Protocol Type''',
            False, 
            [
            _MetaInfoClassMember('punt-id', REFERENCE_ENUM_CLASS, 'LptsPunt', 'Lpts-punt',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lpts_pre_ifib_cfg', 'LptsPunt',
                [], [],
                '''                Punt Type
                ''',
                'punt_id',
                'Cisco-IOS-XR-lpts-pre-ifib-cfg', True),
            _MetaInfoClassMember('rate', REFERENCE_CLASS, 'Rate', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lpts_lib_cfg', 'Lpts.IpuntPolicer.PuntTypeTable.PuntType.Rate',
                [], [],
                '''                Enable or Disable Punt Police and corresponding
                Rate in PPS
                ''',
                'rate',
                'Cisco-IOS-XR-lpts-pre-ifib-cfg', False, is_presence=True),
            ],
            'Cisco-IOS-XR-lpts-pre-ifib-cfg',
            'punt-type',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-lpts-pre-ifib-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lpts_lib_cfg',
        ),
    },
    'Lpts.IpuntPolicer.PuntTypeTable' : {
        'meta_info' : _MetaInfoClass('Lpts.IpuntPolicer.PuntTypeTable', REFERENCE_CLASS,
            '''Punt Policer Table''',
            False, 
            [
            _MetaInfoClassMember('punt-type', REFERENCE_LIST, 'PuntType', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lpts_lib_cfg', 'Lpts.IpuntPolicer.PuntTypeTable.PuntType',
                [], [],
                '''                Punt Protocol Type
                ''',
                'punt_type',
                'Cisco-IOS-XR-lpts-pre-ifib-cfg', False),
            ],
            'Cisco-IOS-XR-lpts-pre-ifib-cfg',
            'punt-type-table',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-lpts-pre-ifib-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lpts_lib_cfg',
        ),
    },
    'Lpts.IpuntPolicer.PuntPolicerDomains.PuntPolicerDomain.PuntTypeDomainTable.PuntType.Rate' : {
        'meta_info' : _MetaInfoClass('Lpts.IpuntPolicer.PuntPolicerDomains.PuntPolicerDomain.PuntTypeDomainTable.PuntType.Rate', REFERENCE_CLASS,
            '''Enable or Disable Punt Police and corresponding
Rate in PPS''',
            False, 
            [
            _MetaInfoClassMember('is-enabled', ATTRIBUTE, 'bool', 'boolean',
                None, None,
                [], [],
                '''                Is Punt Policer enabled
                ''',
                'is_enabled',
                'Cisco-IOS-XR-lpts-pre-ifib-cfg', False, is_mandatory=True),
            _MetaInfoClassMember('rate', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('0', '4294967295')], [],
                '''                Configured rate value
                ''',
                'rate',
                'Cisco-IOS-XR-lpts-pre-ifib-cfg', False),
            ],
            'Cisco-IOS-XR-lpts-pre-ifib-cfg',
            'rate',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-lpts-pre-ifib-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lpts_lib_cfg',
            is_presence=True,
        ),
    },
    'Lpts.IpuntPolicer.PuntPolicerDomains.PuntPolicerDomain.PuntTypeDomainTable.PuntType' : {
        'meta_info' : _MetaInfoClass('Lpts.IpuntPolicer.PuntPolicerDomains.PuntPolicerDomain.PuntTypeDomainTable.PuntType', REFERENCE_LIST,
            '''Punt Protocol Type''',
            False, 
            [
            _MetaInfoClassMember('punt-id', REFERENCE_ENUM_CLASS, 'LptsPunt', 'Lpts-punt',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lpts_pre_ifib_cfg', 'LptsPunt',
                [], [],
                '''                Punt Type
                ''',
                'punt_id',
                'Cisco-IOS-XR-lpts-pre-ifib-cfg', True),
            _MetaInfoClassMember('rate', REFERENCE_CLASS, 'Rate', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lpts_lib_cfg', 'Lpts.IpuntPolicer.PuntPolicerDomains.PuntPolicerDomain.PuntTypeDomainTable.PuntType.Rate',
                [], [],
                '''                Enable or Disable Punt Police and corresponding
                Rate in PPS
                ''',
                'rate',
                'Cisco-IOS-XR-lpts-pre-ifib-cfg', False, is_presence=True),
            ],
            'Cisco-IOS-XR-lpts-pre-ifib-cfg',
            'punt-type',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-lpts-pre-ifib-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lpts_lib_cfg',
        ),
    },
    'Lpts.IpuntPolicer.PuntPolicerDomains.PuntPolicerDomain.PuntTypeDomainTable' : {
        'meta_info' : _MetaInfoClass('Lpts.IpuntPolicer.PuntPolicerDomains.PuntPolicerDomain.PuntTypeDomainTable', REFERENCE_CLASS,
            '''Punt Policer Table''',
            False, 
            [
            _MetaInfoClassMember('punt-type', REFERENCE_LIST, 'PuntType', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lpts_lib_cfg', 'Lpts.IpuntPolicer.PuntPolicerDomains.PuntPolicerDomain.PuntTypeDomainTable.PuntType',
                [], [],
                '''                Punt Protocol Type
                ''',
                'punt_type',
                'Cisco-IOS-XR-lpts-pre-ifib-cfg', False),
            ],
            'Cisco-IOS-XR-lpts-pre-ifib-cfg',
            'punt-type-domain-table',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-lpts-pre-ifib-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lpts_lib_cfg',
        ),
    },
    'Lpts.IpuntPolicer.PuntPolicerDomains.PuntPolicerDomain' : {
        'meta_info' : _MetaInfoClass('Lpts.IpuntPolicer.PuntPolicerDomains.PuntPolicerDomain', REFERENCE_LIST,
            '''Domain name''',
            False, 
            [
            _MetaInfoClassMember('domain-name', ATTRIBUTE, 'str', 'xr:Cisco-ios-xr-string',
                None, None,
                [], [b'[\\w\\-\\.:,_@#%$\\+=\\|;]+'],
                '''                Domain name
                ''',
                'domain_name',
                'Cisco-IOS-XR-lpts-pre-ifib-cfg', True),
            _MetaInfoClassMember('punt-type-domain-table', REFERENCE_CLASS, 'PuntTypeDomainTable', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lpts_lib_cfg', 'Lpts.IpuntPolicer.PuntPolicerDomains.PuntPolicerDomain.PuntTypeDomainTable',
                [], [],
                '''                Punt Policer Table
                ''',
                'punt_type_domain_table',
                'Cisco-IOS-XR-lpts-pre-ifib-cfg', False),
            ],
            'Cisco-IOS-XR-lpts-pre-ifib-cfg',
            'punt-policer-domain',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-lpts-pre-ifib-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lpts_lib_cfg',
        ),
    },
    'Lpts.IpuntPolicer.PuntPolicerDomains' : {
        'meta_info' : _MetaInfoClass('Lpts.IpuntPolicer.PuntPolicerDomains', REFERENCE_CLASS,
            '''Punt Policer Domain Table''',
            False, 
            [
            _MetaInfoClassMember('punt-policer-domain', REFERENCE_LIST, 'PuntPolicerDomain', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lpts_lib_cfg', 'Lpts.IpuntPolicer.PuntPolicerDomains.PuntPolicerDomain',
                [], [],
                '''                Domain name
                ''',
                'punt_policer_domain',
                'Cisco-IOS-XR-lpts-pre-ifib-cfg', False),
            ],
            'Cisco-IOS-XR-lpts-pre-ifib-cfg',
            'punt-policer-domains',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-lpts-pre-ifib-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lpts_lib_cfg',
        ),
    },
    'Lpts.IpuntPolicer.PuntPolicerInterfaceNames.PuntPolicerInterfaceName.PuntTypeInterfaceTable.PuntType.Rate' : {
        'meta_info' : _MetaInfoClass('Lpts.IpuntPolicer.PuntPolicerInterfaceNames.PuntPolicerInterfaceName.PuntTypeInterfaceTable.PuntType.Rate', REFERENCE_CLASS,
            '''Enable or Disable Punt Police and corresponding
Rate in PPS''',
            False, 
            [
            _MetaInfoClassMember('is-enabled', ATTRIBUTE, 'bool', 'boolean',
                None, None,
                [], [],
                '''                Is Punt Policer enabled
                ''',
                'is_enabled',
                'Cisco-IOS-XR-lpts-pre-ifib-cfg', False, is_mandatory=True),
            _MetaInfoClassMember('rate', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('0', '4294967295')], [],
                '''                Configured rate value
                ''',
                'rate',
                'Cisco-IOS-XR-lpts-pre-ifib-cfg', False),
            ],
            'Cisco-IOS-XR-lpts-pre-ifib-cfg',
            'rate',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-lpts-pre-ifib-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lpts_lib_cfg',
            is_presence=True,
        ),
    },
    'Lpts.IpuntPolicer.PuntPolicerInterfaceNames.PuntPolicerInterfaceName.PuntTypeInterfaceTable.PuntType' : {
        'meta_info' : _MetaInfoClass('Lpts.IpuntPolicer.PuntPolicerInterfaceNames.PuntPolicerInterfaceName.PuntTypeInterfaceTable.PuntType', REFERENCE_LIST,
            '''Punt Protocol Type''',
            False, 
            [
            _MetaInfoClassMember('punt-id', REFERENCE_ENUM_CLASS, 'LptsPunt', 'Lpts-punt',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lpts_pre_ifib_cfg', 'LptsPunt',
                [], [],
                '''                Punt Type
                ''',
                'punt_id',
                'Cisco-IOS-XR-lpts-pre-ifib-cfg', True),
            _MetaInfoClassMember('rate', REFERENCE_CLASS, 'Rate', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lpts_lib_cfg', 'Lpts.IpuntPolicer.PuntPolicerInterfaceNames.PuntPolicerInterfaceName.PuntTypeInterfaceTable.PuntType.Rate',
                [], [],
                '''                Enable or Disable Punt Police and corresponding
                Rate in PPS
                ''',
                'rate',
                'Cisco-IOS-XR-lpts-pre-ifib-cfg', False, is_presence=True),
            ],
            'Cisco-IOS-XR-lpts-pre-ifib-cfg',
            'punt-type',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-lpts-pre-ifib-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lpts_lib_cfg',
        ),
    },
    'Lpts.IpuntPolicer.PuntPolicerInterfaceNames.PuntPolicerInterfaceName.PuntTypeInterfaceTable' : {
        'meta_info' : _MetaInfoClass('Lpts.IpuntPolicer.PuntPolicerInterfaceNames.PuntPolicerInterfaceName.PuntTypeInterfaceTable', REFERENCE_CLASS,
            '''Punt Policer Table''',
            False, 
            [
            _MetaInfoClassMember('punt-type', REFERENCE_LIST, 'PuntType', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lpts_lib_cfg', 'Lpts.IpuntPolicer.PuntPolicerInterfaceNames.PuntPolicerInterfaceName.PuntTypeInterfaceTable.PuntType',
                [], [],
                '''                Punt Protocol Type
                ''',
                'punt_type',
                'Cisco-IOS-XR-lpts-pre-ifib-cfg', False),
            ],
            'Cisco-IOS-XR-lpts-pre-ifib-cfg',
            'punt-type-interface-table',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-lpts-pre-ifib-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lpts_lib_cfg',
        ),
    },
    'Lpts.IpuntPolicer.PuntPolicerInterfaceNames.PuntPolicerInterfaceName' : {
        'meta_info' : _MetaInfoClass('Lpts.IpuntPolicer.PuntPolicerInterfaceNames.PuntPolicerInterfaceName', REFERENCE_LIST,
            '''Pre-ifib Punt Policer Interface Configuration''',
            False, 
            [
            _MetaInfoClassMember('punt-interface-name', ATTRIBUTE, 'str', 'xr:Interface-name',
                None, None,
                [], [b'[a-zA-Z0-9._/-]+'],
                '''                Interface Name
                ''',
                'punt_interface_name',
                'Cisco-IOS-XR-lpts-pre-ifib-cfg', True),
            _MetaInfoClassMember('punt-type-interface-table', REFERENCE_CLASS, 'PuntTypeInterfaceTable', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lpts_lib_cfg', 'Lpts.IpuntPolicer.PuntPolicerInterfaceNames.PuntPolicerInterfaceName.PuntTypeInterfaceTable',
                [], [],
                '''                Punt Policer Table
                ''',
                'punt_type_interface_table',
                'Cisco-IOS-XR-lpts-pre-ifib-cfg', False),
            ],
            'Cisco-IOS-XR-lpts-pre-ifib-cfg',
            'punt-policer-interface-name',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-lpts-pre-ifib-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lpts_lib_cfg',
        ),
    },
    'Lpts.IpuntPolicer.PuntPolicerInterfaceNames' : {
        'meta_info' : _MetaInfoClass('Lpts.IpuntPolicer.PuntPolicerInterfaceNames', REFERENCE_CLASS,
            '''Punt Policer Interface''',
            False, 
            [
            _MetaInfoClassMember('punt-policer-interface-name', REFERENCE_LIST, 'PuntPolicerInterfaceName', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lpts_lib_cfg', 'Lpts.IpuntPolicer.PuntPolicerInterfaceNames.PuntPolicerInterfaceName',
                [], [],
                '''                Pre-ifib Punt Policer Interface Configuration
                ''',
                'punt_policer_interface_name',
                'Cisco-IOS-XR-lpts-pre-ifib-cfg', False),
            ],
            'Cisco-IOS-XR-lpts-pre-ifib-cfg',
            'punt-policer-interface-names',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-lpts-pre-ifib-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lpts_lib_cfg',
        ),
    },
    'Lpts.IpuntPolicer' : {
        'meta_info' : _MetaInfoClass('Lpts.IpuntPolicer', REFERENCE_CLASS,
            '''Pre IFiB Punt Policer Configuration ''',
            False, 
            [
            _MetaInfoClassMember('punt-type-table', REFERENCE_CLASS, 'PuntTypeTable', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lpts_lib_cfg', 'Lpts.IpuntPolicer.PuntTypeTable',
                [], [],
                '''                Punt Policer Table
                ''',
                'punt_type_table',
                'Cisco-IOS-XR-lpts-pre-ifib-cfg', False),
            _MetaInfoClassMember('enable', ATTRIBUTE, 'Empty', 'empty',
                None, None,
                [], [],
                '''                Enabled
                ''',
                'enable',
                'Cisco-IOS-XR-lpts-pre-ifib-cfg', False, is_mandatory=True),
            _MetaInfoClassMember('punt-policer-domains', REFERENCE_CLASS, 'PuntPolicerDomains', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lpts_lib_cfg', 'Lpts.IpuntPolicer.PuntPolicerDomains',
                [], [],
                '''                Punt Policer Domain Table
                ''',
                'punt_policer_domains',
                'Cisco-IOS-XR-lpts-pre-ifib-cfg', False),
            _MetaInfoClassMember('punt-policer-interface-names', REFERENCE_CLASS, 'PuntPolicerInterfaceNames', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lpts_lib_cfg', 'Lpts.IpuntPolicer.PuntPolicerInterfaceNames',
                [], [],
                '''                Punt Policer Interface
                ''',
                'punt_policer_interface_names',
                'Cisco-IOS-XR-lpts-pre-ifib-cfg', False),
            ],
            'Cisco-IOS-XR-lpts-pre-ifib-cfg',
            'ipunt-policer',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-lpts-pre-ifib-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lpts_lib_cfg',
            is_presence=True,
        ),
    },
    'Lpts.Punt.Flowtrap.PenaltyRates.PenaltyRate' : {
        'meta_info' : _MetaInfoClass('Lpts.Punt.Flowtrap.PenaltyRates.PenaltyRate', REFERENCE_LIST,
            '''none''',
            False, 
            [
            _MetaInfoClassMember('protocol-name', REFERENCE_ENUM_CLASS, 'LptsPuntFlowtrapProtoId', 'Lpts-punt-flowtrap-proto-id',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lpts_punt_flowtrap_cfg', 'LptsPuntFlowtrapProtoId',
                [], [],
                '''                none
                ''',
                'protocol_name',
                'Cisco-IOS-XR-lpts-punt-flowtrap-cfg', True),
            _MetaInfoClassMember('rate', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('2', '100')], [],
                '''                Penalty policer rate in packets-per-second
                ''',
                'rate',
                'Cisco-IOS-XR-lpts-punt-flowtrap-cfg', False, is_mandatory=True),
            ],
            'Cisco-IOS-XR-lpts-punt-flowtrap-cfg',
            'penalty-rate',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-lpts-punt-flowtrap-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lpts_lib_cfg',
        ),
    },
    'Lpts.Punt.Flowtrap.PenaltyRates' : {
        'meta_info' : _MetaInfoClass('Lpts.Punt.Flowtrap.PenaltyRates', REFERENCE_CLASS,
            '''Configure penalty policing rate''',
            False, 
            [
            _MetaInfoClassMember('penalty-rate', REFERENCE_LIST, 'PenaltyRate', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lpts_lib_cfg', 'Lpts.Punt.Flowtrap.PenaltyRates.PenaltyRate',
                [], [],
                '''                none
                ''',
                'penalty_rate',
                'Cisco-IOS-XR-lpts-punt-flowtrap-cfg', False),
            ],
            'Cisco-IOS-XR-lpts-punt-flowtrap-cfg',
            'penalty-rates',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-lpts-punt-flowtrap-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lpts_lib_cfg',
        ),
    },
    'Lpts.Punt.Flowtrap.PenaltyTimeouts.PenaltyTimeout' : {
        'meta_info' : _MetaInfoClass('Lpts.Punt.Flowtrap.PenaltyTimeouts.PenaltyTimeout', REFERENCE_LIST,
            '''none''',
            False, 
            [
            _MetaInfoClassMember('protocol-name', REFERENCE_ENUM_CLASS, 'LptsPuntFlowtrapProtoId', 'Lpts-punt-flowtrap-proto-id',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lpts_punt_flowtrap_cfg', 'LptsPuntFlowtrapProtoId',
                [], [],
                '''                none
                ''',
                'protocol_name',
                'Cisco-IOS-XR-lpts-punt-flowtrap-cfg', True),
            _MetaInfoClassMember('timeout', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('1', '1000')], [],
                '''                Timeout value in minutes
                ''',
                'timeout',
                'Cisco-IOS-XR-lpts-punt-flowtrap-cfg', False, is_mandatory=True),
            ],
            'Cisco-IOS-XR-lpts-punt-flowtrap-cfg',
            'penalty-timeout',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-lpts-punt-flowtrap-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lpts_lib_cfg',
        ),
    },
    'Lpts.Punt.Flowtrap.PenaltyTimeouts' : {
        'meta_info' : _MetaInfoClass('Lpts.Punt.Flowtrap.PenaltyTimeouts', REFERENCE_CLASS,
            '''Configure penalty timeout value''',
            False, 
            [
            _MetaInfoClassMember('penalty-timeout', REFERENCE_LIST, 'PenaltyTimeout', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lpts_lib_cfg', 'Lpts.Punt.Flowtrap.PenaltyTimeouts.PenaltyTimeout',
                [], [],
                '''                none
                ''',
                'penalty_timeout',
                'Cisco-IOS-XR-lpts-punt-flowtrap-cfg', False),
            ],
            'Cisco-IOS-XR-lpts-punt-flowtrap-cfg',
            'penalty-timeouts',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-lpts-punt-flowtrap-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lpts_lib_cfg',
        ),
    },
    'Lpts.Punt.Flowtrap.Exclude.InterfaceNames.InterfaceName' : {
        'meta_info' : _MetaInfoClass('Lpts.Punt.Flowtrap.Exclude.InterfaceNames.InterfaceName', REFERENCE_LIST,
            '''Name of interface to exclude from all traps''',
            False, 
            [
            _MetaInfoClassMember('ifname', ATTRIBUTE, 'str', 'xr:Interface-name',
                None, None,
                [], [b'[a-zA-Z0-9._/-]+'],
                '''                Name of interface to exclude from all traps
                ''',
                'ifname',
                'Cisco-IOS-XR-lpts-punt-flowtrap-cfg', True),
            _MetaInfoClassMember('id1', ATTRIBUTE, 'bool', 'boolean',
                None, None,
                [], [],
                '''                Enabled or disabled
                ''',
                'id1',
                'Cisco-IOS-XR-lpts-punt-flowtrap-cfg', False, is_mandatory=True),
            ],
            'Cisco-IOS-XR-lpts-punt-flowtrap-cfg',
            'interface-name',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-lpts-punt-flowtrap-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lpts_lib_cfg',
        ),
    },
    'Lpts.Punt.Flowtrap.Exclude.InterfaceNames' : {
        'meta_info' : _MetaInfoClass('Lpts.Punt.Flowtrap.Exclude.InterfaceNames', REFERENCE_CLASS,
            '''none''',
            False, 
            [
            _MetaInfoClassMember('interface-name', REFERENCE_LIST, 'InterfaceName', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lpts_lib_cfg', 'Lpts.Punt.Flowtrap.Exclude.InterfaceNames.InterfaceName',
                [], [],
                '''                Name of interface to exclude from all traps
                ''',
                'interface_name',
                'Cisco-IOS-XR-lpts-punt-flowtrap-cfg', False),
            ],
            'Cisco-IOS-XR-lpts-punt-flowtrap-cfg',
            'interface-names',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-lpts-punt-flowtrap-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lpts_lib_cfg',
        ),
    },
    'Lpts.Punt.Flowtrap.Exclude' : {
        'meta_info' : _MetaInfoClass('Lpts.Punt.Flowtrap.Exclude', REFERENCE_CLASS,
            '''Exclude an item from all traps''',
            False, 
            [
            _MetaInfoClassMember('interface-names', REFERENCE_CLASS, 'InterfaceNames', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lpts_lib_cfg', 'Lpts.Punt.Flowtrap.Exclude.InterfaceNames',
                [], [],
                '''                none
                ''',
                'interface_names',
                'Cisco-IOS-XR-lpts-punt-flowtrap-cfg', False),
            ],
            'Cisco-IOS-XR-lpts-punt-flowtrap-cfg',
            'exclude',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-lpts-punt-flowtrap-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lpts_lib_cfg',
        ),
    },
    'Lpts.Punt.Flowtrap' : {
        'meta_info' : _MetaInfoClass('Lpts.Punt.Flowtrap', REFERENCE_CLASS,
            '''excessive punt flow trap configuration commands''',
            False, 
            [
            _MetaInfoClassMember('penalty-rates', REFERENCE_CLASS, 'PenaltyRates', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lpts_lib_cfg', 'Lpts.Punt.Flowtrap.PenaltyRates',
                [], [],
                '''                Configure penalty policing rate
                ''',
                'penalty_rates',
                'Cisco-IOS-XR-lpts-punt-flowtrap-cfg', False),
            _MetaInfoClassMember('penalty-timeouts', REFERENCE_CLASS, 'PenaltyTimeouts', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lpts_lib_cfg', 'Lpts.Punt.Flowtrap.PenaltyTimeouts',
                [], [],
                '''                Configure penalty timeout value
                ''',
                'penalty_timeouts',
                'Cisco-IOS-XR-lpts-punt-flowtrap-cfg', False),
            _MetaInfoClassMember('exclude', REFERENCE_CLASS, 'Exclude', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lpts_lib_cfg', 'Lpts.Punt.Flowtrap.Exclude',
                [], [],
                '''                Exclude an item from all traps
                ''',
                'exclude',
                'Cisco-IOS-XR-lpts-punt-flowtrap-cfg', False),
            _MetaInfoClassMember('max-flow-gap', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('1', '60000')], [],
                '''                Maximum flow gap in milliseconds
                ''',
                'max_flow_gap',
                'Cisco-IOS-XR-lpts-punt-flowtrap-cfg', False),
            _MetaInfoClassMember('et-size', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('1', '128')], [],
                '''                Should be power of 2. Any one of 1,2,4,8,16,32
                ,64,128
                ''',
                'et_size',
                'Cisco-IOS-XR-lpts-punt-flowtrap-cfg', False),
            _MetaInfoClassMember('eviction-threshold', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('1', '65535')], [],
                '''                Eviction threshold, should be less than
                report-threshold
                ''',
                'eviction_threshold',
                'Cisco-IOS-XR-lpts-punt-flowtrap-cfg', False),
            _MetaInfoClassMember('report-threshold', ATTRIBUTE, 'int', 'xr:Cisco-ios-xr-port-number',
                None, None,
                [('1', '65535')], [],
                '''                Threshold to cross for a flow to be considered
                as bad actor flow
                ''',
                'report_threshold',
                'Cisco-IOS-XR-lpts-punt-flowtrap-cfg', False),
            _MetaInfoClassMember('non-subscriber-interfaces', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('0', '4294967295')], [],
                '''                Enable trap based on source mac on
                non-subscriber interface
                ''',
                'non_subscriber_interfaces',
                'Cisco-IOS-XR-lpts-punt-flowtrap-cfg', False),
            _MetaInfoClassMember('sample-prob', ATTRIBUTE, 'str', 'string',
                None, None,
                [(1, 32)], [],
                '''                Probability of packets to be sampled
                ''',
                'sample_prob',
                'Cisco-IOS-XR-lpts-punt-flowtrap-cfg', False),
            _MetaInfoClassMember('eviction-search-limit', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('1', '128')], [],
                '''                Eviction search limit, should be less than
                trap-size
                ''',
                'eviction_search_limit',
                'Cisco-IOS-XR-lpts-punt-flowtrap-cfg', False),
            _MetaInfoClassMember('routing-protocols-enable', ATTRIBUTE, 'bool', 'boolean',
                None, None,
                [], [],
                '''                Allow routing protocols to pass through copp
                sampler
                ''',
                'routing_protocols_enable',
                'Cisco-IOS-XR-lpts-punt-flowtrap-cfg', False),
            _MetaInfoClassMember('subscriber-interfaces', ATTRIBUTE, 'bool', 'boolean',
                None, None,
                [], [],
                '''                Enable the trap on subscriber interfaces
                ''',
                'subscriber_interfaces',
                'Cisco-IOS-XR-lpts-punt-flowtrap-cfg', False),
            _MetaInfoClassMember('interface-based-flow', ATTRIBUTE, 'bool', 'boolean',
                None, None,
                [], [],
                '''                Identify flow based on interface and flowtype
                ''',
                'interface_based_flow',
                'Cisco-IOS-XR-lpts-punt-flowtrap-cfg', False),
            _MetaInfoClassMember('dampening', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('5000', '60000')], [],
                '''                Dampening period for a bad actor flow in
                milliseconds
                ''',
                'dampening',
                'Cisco-IOS-XR-lpts-punt-flowtrap-cfg', False),
            ],
            'Cisco-IOS-XR-lpts-punt-flowtrap-cfg',
            'flowtrap',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-lpts-punt-flowtrap-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lpts_lib_cfg',
        ),
    },
    'Lpts.Punt' : {
        'meta_info' : _MetaInfoClass('Lpts.Punt', REFERENCE_CLASS,
            '''Configure penalty timeout value''',
            False, 
            [
            _MetaInfoClassMember('flowtrap', REFERENCE_CLASS, 'Flowtrap', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lpts_lib_cfg', 'Lpts.Punt.Flowtrap',
                [], [],
                '''                excessive punt flow trap configuration commands
                ''',
                'flowtrap',
                'Cisco-IOS-XR-lpts-punt-flowtrap-cfg', False),
            ],
            'Cisco-IOS-XR-lpts-punt-flowtrap-cfg',
            'punt',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-lpts-punt-flowtrap-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lpts_lib_cfg',
        ),
    },
    'Lpts' : {
        'meta_info' : _MetaInfoClass('Lpts', REFERENCE_CLASS,
            '''lpts configuration commands''',
            False, 
            [
            _MetaInfoClassMember('ipolicer', REFERENCE_CLASS, 'Ipolicer', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lpts_lib_cfg', 'Lpts.Ipolicer',
                [], [],
                '''                Pre IFiB Policer Configuration 
                ''',
                'ipolicer',
                'Cisco-IOS-XR-lpts-pre-ifib-cfg', False, is_presence=True),
            _MetaInfoClassMember('domain-names', REFERENCE_CLASS, 'DomainNames', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lpts_lib_cfg', 'Lpts.DomainNames',
                [], [],
                '''                Pre IFiB Domains Configuration 
                ''',
                'domain_names',
                'Cisco-IOS-XR-lpts-pre-ifib-cfg', False),
            _MetaInfoClassMember('ipunt-policer', REFERENCE_CLASS, 'IpuntPolicer', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lpts_lib_cfg', 'Lpts.IpuntPolicer',
                [], [],
                '''                Pre IFiB Punt Policer Configuration 
                ''',
                'ipunt_policer',
                'Cisco-IOS-XR-lpts-pre-ifib-cfg', False, is_presence=True),
            _MetaInfoClassMember('punt', REFERENCE_CLASS, 'Punt', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lpts_lib_cfg', 'Lpts.Punt',
                [], [],
                '''                Configure penalty timeout value
                ''',
                'punt',
                'Cisco-IOS-XR-lpts-punt-flowtrap-cfg', False),
            ],
            'Cisco-IOS-XR-lpts-lib-cfg',
            'lpts',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-lpts-lib-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lpts_lib_cfg',
        ),
    },
}
_meta_table['Lpts.Ipolicer.Acls.Acl.AfiTypes.AfiType.VrfNames.VrfName']['meta_info'].parent =_meta_table['Lpts.Ipolicer.Acls.Acl.AfiTypes.AfiType.VrfNames']['meta_info']
_meta_table['Lpts.Ipolicer.Acls.Acl.AfiTypes.AfiType.VrfNames']['meta_info'].parent =_meta_table['Lpts.Ipolicer.Acls.Acl.AfiTypes.AfiType']['meta_info']
_meta_table['Lpts.Ipolicer.Acls.Acl.AfiTypes.AfiType']['meta_info'].parent =_meta_table['Lpts.Ipolicer.Acls.Acl.AfiTypes']['meta_info']
_meta_table['Lpts.Ipolicer.Acls.Acl.AfiTypes']['meta_info'].parent =_meta_table['Lpts.Ipolicer.Acls.Acl']['meta_info']
_meta_table['Lpts.Ipolicer.Acls.Acl']['meta_info'].parent =_meta_table['Lpts.Ipolicer.Acls']['meta_info']
_meta_table['Lpts.Ipolicer.PolicerDomains.PolicerDomain.Flows.Flow.Precedences']['meta_info'].parent =_meta_table['Lpts.Ipolicer.PolicerDomains.PolicerDomain.Flows.Flow']['meta_info']
_meta_table['Lpts.Ipolicer.PolicerDomains.PolicerDomain.Flows.Flow']['meta_info'].parent =_meta_table['Lpts.Ipolicer.PolicerDomains.PolicerDomain.Flows']['meta_info']
_meta_table['Lpts.Ipolicer.PolicerDomains.PolicerDomain.Flows']['meta_info'].parent =_meta_table['Lpts.Ipolicer.PolicerDomains.PolicerDomain']['meta_info']
_meta_table['Lpts.Ipolicer.PolicerDomains.PolicerDomain']['meta_info'].parent =_meta_table['Lpts.Ipolicer.PolicerDomains']['meta_info']
_meta_table['Lpts.Ipolicer.Flows.Flow.Precedences']['meta_info'].parent =_meta_table['Lpts.Ipolicer.Flows.Flow']['meta_info']
_meta_table['Lpts.Ipolicer.Flows.Flow']['meta_info'].parent =_meta_table['Lpts.Ipolicer.Flows']['meta_info']
_meta_table['Lpts.Ipolicer.Acls']['meta_info'].parent =_meta_table['Lpts.Ipolicer']['meta_info']
_meta_table['Lpts.Ipolicer.PolicerDomains']['meta_info'].parent =_meta_table['Lpts.Ipolicer']['meta_info']
_meta_table['Lpts.Ipolicer.Flows']['meta_info'].parent =_meta_table['Lpts.Ipolicer']['meta_info']
_meta_table['Lpts.DomainNames.DomainName.InterfaceNames.InterfaceName']['meta_info'].parent =_meta_table['Lpts.DomainNames.DomainName.InterfaceNames']['meta_info']
_meta_table['Lpts.DomainNames.DomainName.InterfaceNames']['meta_info'].parent =_meta_table['Lpts.DomainNames.DomainName']['meta_info']
_meta_table['Lpts.DomainNames.DomainName']['meta_info'].parent =_meta_table['Lpts.DomainNames']['meta_info']
_meta_table['Lpts.IpuntPolicer.PuntTypeTable.PuntType.Rate']['meta_info'].parent =_meta_table['Lpts.IpuntPolicer.PuntTypeTable.PuntType']['meta_info']
_meta_table['Lpts.IpuntPolicer.PuntTypeTable.PuntType']['meta_info'].parent =_meta_table['Lpts.IpuntPolicer.PuntTypeTable']['meta_info']
_meta_table['Lpts.IpuntPolicer.PuntPolicerDomains.PuntPolicerDomain.PuntTypeDomainTable.PuntType.Rate']['meta_info'].parent =_meta_table['Lpts.IpuntPolicer.PuntPolicerDomains.PuntPolicerDomain.PuntTypeDomainTable.PuntType']['meta_info']
_meta_table['Lpts.IpuntPolicer.PuntPolicerDomains.PuntPolicerDomain.PuntTypeDomainTable.PuntType']['meta_info'].parent =_meta_table['Lpts.IpuntPolicer.PuntPolicerDomains.PuntPolicerDomain.PuntTypeDomainTable']['meta_info']
_meta_table['Lpts.IpuntPolicer.PuntPolicerDomains.PuntPolicerDomain.PuntTypeDomainTable']['meta_info'].parent =_meta_table['Lpts.IpuntPolicer.PuntPolicerDomains.PuntPolicerDomain']['meta_info']
_meta_table['Lpts.IpuntPolicer.PuntPolicerDomains.PuntPolicerDomain']['meta_info'].parent =_meta_table['Lpts.IpuntPolicer.PuntPolicerDomains']['meta_info']
_meta_table['Lpts.IpuntPolicer.PuntPolicerInterfaceNames.PuntPolicerInterfaceName.PuntTypeInterfaceTable.PuntType.Rate']['meta_info'].parent =_meta_table['Lpts.IpuntPolicer.PuntPolicerInterfaceNames.PuntPolicerInterfaceName.PuntTypeInterfaceTable.PuntType']['meta_info']
_meta_table['Lpts.IpuntPolicer.PuntPolicerInterfaceNames.PuntPolicerInterfaceName.PuntTypeInterfaceTable.PuntType']['meta_info'].parent =_meta_table['Lpts.IpuntPolicer.PuntPolicerInterfaceNames.PuntPolicerInterfaceName.PuntTypeInterfaceTable']['meta_info']
_meta_table['Lpts.IpuntPolicer.PuntPolicerInterfaceNames.PuntPolicerInterfaceName.PuntTypeInterfaceTable']['meta_info'].parent =_meta_table['Lpts.IpuntPolicer.PuntPolicerInterfaceNames.PuntPolicerInterfaceName']['meta_info']
_meta_table['Lpts.IpuntPolicer.PuntPolicerInterfaceNames.PuntPolicerInterfaceName']['meta_info'].parent =_meta_table['Lpts.IpuntPolicer.PuntPolicerInterfaceNames']['meta_info']
_meta_table['Lpts.IpuntPolicer.PuntTypeTable']['meta_info'].parent =_meta_table['Lpts.IpuntPolicer']['meta_info']
_meta_table['Lpts.IpuntPolicer.PuntPolicerDomains']['meta_info'].parent =_meta_table['Lpts.IpuntPolicer']['meta_info']
_meta_table['Lpts.IpuntPolicer.PuntPolicerInterfaceNames']['meta_info'].parent =_meta_table['Lpts.IpuntPolicer']['meta_info']
_meta_table['Lpts.Punt.Flowtrap.PenaltyRates.PenaltyRate']['meta_info'].parent =_meta_table['Lpts.Punt.Flowtrap.PenaltyRates']['meta_info']
_meta_table['Lpts.Punt.Flowtrap.PenaltyTimeouts.PenaltyTimeout']['meta_info'].parent =_meta_table['Lpts.Punt.Flowtrap.PenaltyTimeouts']['meta_info']
_meta_table['Lpts.Punt.Flowtrap.Exclude.InterfaceNames.InterfaceName']['meta_info'].parent =_meta_table['Lpts.Punt.Flowtrap.Exclude.InterfaceNames']['meta_info']
_meta_table['Lpts.Punt.Flowtrap.Exclude.InterfaceNames']['meta_info'].parent =_meta_table['Lpts.Punt.Flowtrap.Exclude']['meta_info']
_meta_table['Lpts.Punt.Flowtrap.PenaltyRates']['meta_info'].parent =_meta_table['Lpts.Punt.Flowtrap']['meta_info']
_meta_table['Lpts.Punt.Flowtrap.PenaltyTimeouts']['meta_info'].parent =_meta_table['Lpts.Punt.Flowtrap']['meta_info']
_meta_table['Lpts.Punt.Flowtrap.Exclude']['meta_info'].parent =_meta_table['Lpts.Punt.Flowtrap']['meta_info']
_meta_table['Lpts.Punt.Flowtrap']['meta_info'].parent =_meta_table['Lpts.Punt']['meta_info']
_meta_table['Lpts.Ipolicer']['meta_info'].parent =_meta_table['Lpts']['meta_info']
_meta_table['Lpts.DomainNames']['meta_info'].parent =_meta_table['Lpts']['meta_info']
_meta_table['Lpts.IpuntPolicer']['meta_info'].parent =_meta_table['Lpts']['meta_info']
_meta_table['Lpts.Punt']['meta_info'].parent =_meta_table['Lpts']['meta_info']
