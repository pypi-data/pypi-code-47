
'''
This is auto-generated file,
which includes metadata for module Cisco_IOS_XR_aaa_nacm_cfg
'''

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_LIST, REFERENCE_LEAFLIST, REFERENCE_BITS, REFERENCE_UNION
from ydk._core._dm_meta_info import REFERENCE_CLASS, REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, ANYXML_CLASS
from ydk._core._importer import _yang_ns

_meta_table = {
    'NacmAction' : _MetaInfoEnum('NacmAction',
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_nacm_cfg', 'NacmAction',
        '''Nacm action''',
        {
            'permit':'permit',
            'deny':'deny',
        }, 'Cisco-IOS-XR-aaa-nacm-cfg', _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-aaa-nacm-cfg']),
    'NacmRule' : _MetaInfoEnum('NacmRule',
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_nacm_cfg', 'NacmRule',
        '''Nacm rule''',
        {
            'protocol-operation':'protocol_operation',
            'data-node':'data_node',
            'notification':'notification',
        }, 'Cisco-IOS-XR-aaa-nacm-cfg', _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-aaa-nacm-cfg']),
    'Nacm.Groups.Group' : {
        'meta_info' : _MetaInfoClass('Nacm.Groups.Group', REFERENCE_LIST,
            '''One NACM Group Entry''',
            False, 
            [
            _MetaInfoClassMember('group-name', ATTRIBUTE, 'str', 'xr:Cisco-ios-xr-string',
                None, None,
                [(1, 63)], [],
                '''                User group name
                ''',
                'group_name',
                'Cisco-IOS-XR-aaa-nacm-cfg', True),
            _MetaInfoClassMember('user-name', REFERENCE_LEAFLIST, 'str', 'xr:Cisco-ios-xr-string',
                None, None,
                [(1, 63)], [],
                '''                User name
                ''',
                'user_name',
                'Cisco-IOS-XR-aaa-nacm-cfg', False, max_elements=16, min_elements=1),
            ],
            'Cisco-IOS-XR-aaa-nacm-cfg',
            'group',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-aaa-nacm-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_nacm_cfg',
        ),
    },
    'Nacm.Groups' : {
        'meta_info' : _MetaInfoClass('Nacm.Groups', REFERENCE_CLASS,
            '''NETCONF Access Control Groups''',
            False, 
            [
            _MetaInfoClassMember('group', REFERENCE_LIST, 'Group', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_nacm_cfg', 'Nacm.Groups.Group',
                [], [],
                '''                One NACM Group Entry
                ''',
                'group',
                'Cisco-IOS-XR-aaa-nacm-cfg', False),
            ],
            'Cisco-IOS-XR-aaa-nacm-cfg',
            'groups',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-aaa-nacm-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_nacm_cfg',
        ),
    },
    'Nacm.RulelistClasses.RulelistClass.GroupNames' : {
        'meta_info' : _MetaInfoClass('Nacm.RulelistClasses.RulelistClass.GroupNames', REFERENCE_CLASS,
            '''List of groups that will be assigned with the
rule''',
            False, 
            [
            _MetaInfoClassMember('group-name', REFERENCE_LEAFLIST, 'str', 'xr:Cisco-ios-xr-string',
                None, None,
                [(1, 63)], [],
                '''                Group name
                ''',
                'group_name',
                'Cisco-IOS-XR-aaa-nacm-cfg', False, max_elements=16),
            ],
            'Cisco-IOS-XR-aaa-nacm-cfg',
            'group-names',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-aaa-nacm-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_nacm_cfg',
        ),
    },
    'Nacm.RulelistClasses.RulelistClass.Rules.Rule.RuleType' : {
        'meta_info' : _MetaInfoClass('Nacm.RulelistClasses.RulelistClass.Rules.Rule.RuleType', REFERENCE_CLASS,
            '''Rule Type associated with this rule''',
            False, 
            [
            _MetaInfoClassMember('type', REFERENCE_ENUM_CLASS, 'NacmRule', 'Nacm-rule',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_nacm_cfg', 'NacmRule',
                [], [],
                '''                Rule Type
                ''',
                'type',
                'Cisco-IOS-XR-aaa-nacm-cfg', False),
            _MetaInfoClassMember('value', ATTRIBUTE, 'str', 'string',
                None, None,
                [(1, 511)], [],
                '''                Rule Value
                ''',
                'value',
                'Cisco-IOS-XR-aaa-nacm-cfg', False),
            ],
            'Cisco-IOS-XR-aaa-nacm-cfg',
            'rule-type',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-aaa-nacm-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_nacm_cfg',
        ),
    },
    'Nacm.RulelistClasses.RulelistClass.Rules.Rule.AccessOperations' : {
        'meta_info' : _MetaInfoClass('Nacm.RulelistClasses.RulelistClass.Rules.Rule.AccessOperations', REFERENCE_CLASS,
            '''Access operations associated with this rule''',
            False, 
            [
            _MetaInfoClassMember('create', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('0', '4294967295')], [],
                '''                Enable Create
                ''',
                'create',
                'Cisco-IOS-XR-aaa-nacm-cfg', False),
            _MetaInfoClassMember('read', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('0', '4294967295')], [],
                '''                Enable Read
                ''',
                'read',
                'Cisco-IOS-XR-aaa-nacm-cfg', False),
            _MetaInfoClassMember('update', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('0', '4294967295')], [],
                '''                Enable Update
                ''',
                'update',
                'Cisco-IOS-XR-aaa-nacm-cfg', False),
            _MetaInfoClassMember('delete', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('0', '4294967295')], [],
                '''                Enable Delete
                ''',
                'delete',
                'Cisco-IOS-XR-aaa-nacm-cfg', False),
            _MetaInfoClassMember('exec', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('0', '4294967295')], [],
                '''                Enable Exec
                ''',
                'exec_',
                'Cisco-IOS-XR-aaa-nacm-cfg', False),
            _MetaInfoClassMember('all', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('0', '4294967295')], [],
                '''                Enable All permissions
                ''',
                'all',
                'Cisco-IOS-XR-aaa-nacm-cfg', False),
            ],
            'Cisco-IOS-XR-aaa-nacm-cfg',
            'access-operations',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-aaa-nacm-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_nacm_cfg',
        ),
    },
    'Nacm.RulelistClasses.RulelistClass.Rules.Rule' : {
        'meta_info' : _MetaInfoClass('Nacm.RulelistClasses.RulelistClass.Rules.Rule', REFERENCE_LIST,
            '''Each rule in a rulelist''',
            False, 
            [
            _MetaInfoClassMember('ordering-index', ATTRIBUTE, 'str', 'xr:Cisco-ios-xr-string',
                None, None,
                [(1, 15)], [],
                '''                This is used to sort the rules in the order
                of precedence
                ''',
                'ordering_index',
                'Cisco-IOS-XR-aaa-nacm-cfg', True),
            _MetaInfoClassMember('rule-name', ATTRIBUTE, 'str', 'xr:Cisco-ios-xr-string',
                None, None,
                [(1, 63)], [],
                '''                Rule name
                ''',
                'rule_name',
                'Cisco-IOS-XR-aaa-nacm-cfg', True),
            _MetaInfoClassMember('rule-type', REFERENCE_CLASS, 'RuleType', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_nacm_cfg', 'Nacm.RulelistClasses.RulelistClass.Rules.Rule.RuleType',
                [], [],
                '''                Rule Type associated with this rule
                ''',
                'rule_type',
                'Cisco-IOS-XR-aaa-nacm-cfg', False),
            _MetaInfoClassMember('access-operations', REFERENCE_CLASS, 'AccessOperations', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_nacm_cfg', 'Nacm.RulelistClasses.RulelistClass.Rules.Rule.AccessOperations',
                [], [],
                '''                Access operations associated with this rule
                ''',
                'access_operations',
                'Cisco-IOS-XR-aaa-nacm-cfg', False),
            _MetaInfoClassMember('module-name', ATTRIBUTE, 'str', 'string',
                None, None,
                [(1, 63)], [],
                '''                Name of the module associated with this rule
                ''',
                'module_name',
                'Cisco-IOS-XR-aaa-nacm-cfg', False),
            _MetaInfoClassMember('action', REFERENCE_ENUM_CLASS, 'NacmAction', 'Nacm-action',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_nacm_cfg', 'NacmAction',
                [], [],
                '''                The access control action associated with
                the rule
                ''',
                'action',
                'Cisco-IOS-XR-aaa-nacm-cfg', False, is_mandatory=True),
            _MetaInfoClassMember('comment', ATTRIBUTE, 'str', 'string',
                None, None,
                [(1, 255)], [],
                '''                Textual description of the access rule
                ''',
                'comment',
                'Cisco-IOS-XR-aaa-nacm-cfg', False),
            ],
            'Cisco-IOS-XR-aaa-nacm-cfg',
            'rule',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-aaa-nacm-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_nacm_cfg',
        ),
    },
    'Nacm.RulelistClasses.RulelistClass.Rules' : {
        'meta_info' : _MetaInfoClass('Nacm.RulelistClasses.RulelistClass.Rules', REFERENCE_CLASS,
            '''Set of rules in a rulelist''',
            False, 
            [
            _MetaInfoClassMember('rule', REFERENCE_LIST, 'Rule', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_nacm_cfg', 'Nacm.RulelistClasses.RulelistClass.Rules.Rule',
                [], [],
                '''                Each rule in a rulelist
                ''',
                'rule',
                'Cisco-IOS-XR-aaa-nacm-cfg', False),
            ],
            'Cisco-IOS-XR-aaa-nacm-cfg',
            'rules',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-aaa-nacm-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_nacm_cfg',
        ),
    },
    'Nacm.RulelistClasses.RulelistClass' : {
        'meta_info' : _MetaInfoClass('Nacm.RulelistClasses.RulelistClass', REFERENCE_LIST,
            '''Each rule list of NACM''',
            False, 
            [
            _MetaInfoClassMember('ordering-index', ATTRIBUTE, 'str', 'xr:Cisco-ios-xr-string',
                None, None,
                [(1, 15)], [],
                '''                This is used to sort the rulelists in the
                order of precedence
                ''',
                'ordering_index',
                'Cisco-IOS-XR-aaa-nacm-cfg', True),
            _MetaInfoClassMember('rulelist-name', ATTRIBUTE, 'str', 'xr:Cisco-ios-xr-string',
                None, None,
                [(1, 63)], [],
                '''                Rulelist key name
                ''',
                'rulelist_name',
                'Cisco-IOS-XR-aaa-nacm-cfg', True),
            _MetaInfoClassMember('group-names', REFERENCE_CLASS, 'GroupNames', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_nacm_cfg', 'Nacm.RulelistClasses.RulelistClass.GroupNames',
                [], [],
                '''                List of groups that will be assigned with the
                rule
                ''',
                'group_names',
                'Cisco-IOS-XR-aaa-nacm-cfg', False),
            _MetaInfoClassMember('rules', REFERENCE_CLASS, 'Rules', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_nacm_cfg', 'Nacm.RulelistClasses.RulelistClass.Rules',
                [], [],
                '''                Set of rules in a rulelist
                ''',
                'rules',
                'Cisco-IOS-XR-aaa-nacm-cfg', False),
            ],
            'Cisco-IOS-XR-aaa-nacm-cfg',
            'rulelist-class',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-aaa-nacm-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_nacm_cfg',
        ),
    },
    'Nacm.RulelistClasses' : {
        'meta_info' : _MetaInfoClass('Nacm.RulelistClasses', REFERENCE_CLASS,
            '''Contains all rule lists of NACM''',
            False, 
            [
            _MetaInfoClassMember('rulelist-class', REFERENCE_LIST, 'RulelistClass', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_nacm_cfg', 'Nacm.RulelistClasses.RulelistClass',
                [], [],
                '''                Each rule list of NACM
                ''',
                'rulelist_class',
                'Cisco-IOS-XR-aaa-nacm-cfg', False),
            ],
            'Cisco-IOS-XR-aaa-nacm-cfg',
            'rulelist-classes',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-aaa-nacm-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_nacm_cfg',
        ),
    },
    'Nacm' : {
        'meta_info' : _MetaInfoClass('Nacm', REFERENCE_CLASS,
            '''Parameters for NETCONF Access Control Model''',
            False, 
            [
            _MetaInfoClassMember('groups', REFERENCE_CLASS, 'Groups', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_nacm_cfg', 'Nacm.Groups',
                [], [],
                '''                NETCONF Access Control Groups
                ''',
                'groups',
                'Cisco-IOS-XR-aaa-nacm-cfg', False),
            _MetaInfoClassMember('rulelist-classes', REFERENCE_CLASS, 'RulelistClasses', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_nacm_cfg', 'Nacm.RulelistClasses',
                [], [],
                '''                Contains all rule lists of NACM
                ''',
                'rulelist_classes',
                'Cisco-IOS-XR-aaa-nacm-cfg', False),
            _MetaInfoClassMember('enable-nacm', ATTRIBUTE, 'bool', 'boolean',
                None, None,
                [], [],
                '''                Enables or Disables all NETCONF access control
                enforcement
                ''',
                'enable_nacm',
                'Cisco-IOS-XR-aaa-nacm-cfg', False),
            _MetaInfoClassMember('write-default', REFERENCE_ENUM_CLASS, 'NacmAction', 'Nacm-action',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_nacm_cfg', 'NacmAction',
                [], [],
                '''                Controls write access if no appropriate rule is
                found
                ''',
                'write_default',
                'Cisco-IOS-XR-aaa-nacm-cfg', False),
            _MetaInfoClassMember('exec-default', REFERENCE_ENUM_CLASS, 'NacmAction', 'Nacm-action',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_nacm_cfg', 'NacmAction',
                [], [],
                '''                Controls exec access if no appropriate rule is
                found
                ''',
                'exec_default',
                'Cisco-IOS-XR-aaa-nacm-cfg', False),
            _MetaInfoClassMember('enable-external-groups', ATTRIBUTE, 'bool', 'boolean',
                None, None,
                [], [],
                '''                Controls whether the server uses the groups
                reported by NETCONF transport layer
                ''',
                'enable_external_groups',
                'Cisco-IOS-XR-aaa-nacm-cfg', False),
            _MetaInfoClassMember('read-default', REFERENCE_ENUM_CLASS, 'NacmAction', 'Nacm-action',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_nacm_cfg', 'NacmAction',
                [], [],
                '''                Controls read access if no appropriate rule is
                found
                ''',
                'read_default',
                'Cisco-IOS-XR-aaa-nacm-cfg', False),
            ],
            'Cisco-IOS-XR-aaa-nacm-cfg',
            'nacm',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-aaa-nacm-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_nacm_cfg',
        ),
    },
}
_meta_table['Nacm.Groups.Group']['meta_info'].parent =_meta_table['Nacm.Groups']['meta_info']
_meta_table['Nacm.RulelistClasses.RulelistClass.Rules.Rule.RuleType']['meta_info'].parent =_meta_table['Nacm.RulelistClasses.RulelistClass.Rules.Rule']['meta_info']
_meta_table['Nacm.RulelistClasses.RulelistClass.Rules.Rule.AccessOperations']['meta_info'].parent =_meta_table['Nacm.RulelistClasses.RulelistClass.Rules.Rule']['meta_info']
_meta_table['Nacm.RulelistClasses.RulelistClass.Rules.Rule']['meta_info'].parent =_meta_table['Nacm.RulelistClasses.RulelistClass.Rules']['meta_info']
_meta_table['Nacm.RulelistClasses.RulelistClass.GroupNames']['meta_info'].parent =_meta_table['Nacm.RulelistClasses.RulelistClass']['meta_info']
_meta_table['Nacm.RulelistClasses.RulelistClass.Rules']['meta_info'].parent =_meta_table['Nacm.RulelistClasses.RulelistClass']['meta_info']
_meta_table['Nacm.RulelistClasses.RulelistClass']['meta_info'].parent =_meta_table['Nacm.RulelistClasses']['meta_info']
_meta_table['Nacm.Groups']['meta_info'].parent =_meta_table['Nacm']['meta_info']
_meta_table['Nacm.RulelistClasses']['meta_info'].parent =_meta_table['Nacm']['meta_info']
