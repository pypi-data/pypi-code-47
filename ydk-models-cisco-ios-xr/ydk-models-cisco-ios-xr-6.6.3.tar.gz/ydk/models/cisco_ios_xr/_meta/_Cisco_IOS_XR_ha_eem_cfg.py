
'''
This is auto-generated file,
which includes metadata for module Cisco_IOS_XR_ha_eem_cfg
'''

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_LIST, REFERENCE_LEAFLIST, REFERENCE_BITS, REFERENCE_UNION
from ydk._core._dm_meta_info import REFERENCE_CLASS, REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, ANYXML_CLASS
from ydk._core._importer import _yang_ns

_meta_table = {
    'EventManagerChecksum' : _MetaInfoEnum('EventManagerChecksum',
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ha_eem_cfg', 'EventManagerChecksum',
        '''Event manager checksum''',
        {
            'sha-1':'sha_1',
            'md5':'md5',
        }, 'Cisco-IOS-XR-ha-eem-cfg', _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-ha-eem-cfg']),
    'EventManagerPolicySec' : _MetaInfoEnum('EventManagerPolicySec',
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ha_eem_cfg', 'EventManagerPolicySec',
        '''Event manager policy sec''',
        {
            'rsa-2048':'rsa_2048',
            'trust':'trust',
        }, 'Cisco-IOS-XR-ha-eem-cfg', _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-ha-eem-cfg']),
    'EventManagerPolicyMode' : _MetaInfoEnum('EventManagerPolicyMode',
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ha_eem_cfg', 'EventManagerPolicyMode',
        '''Event manager policy mode''',
        {
            'cisco':'cisco',
            'trust':'trust',
        }, 'Cisco-IOS-XR-ha-eem-cfg', _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-ha-eem-cfg']),
    'EventManagerPolicy' : _MetaInfoEnum('EventManagerPolicy',
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ha_eem_cfg', 'EventManagerPolicy',
        '''Event manager policy''',
        {
            'system':'system',
            'user':'user',
        }, 'Cisco-IOS-XR-ha-eem-cfg', _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-ha-eem-cfg']),
    'EventManager.Policies.Policy' : {
        'meta_info' : _MetaInfoClass('EventManager.Policies.Policy', REFERENCE_LIST,
            '''Name of the policy file''',
            False, 
            [
            _MetaInfoClassMember('policy-name', ATTRIBUTE, 'str', 'xr:Cisco-ios-xr-string',
                None, None,
                [], [b'[\\w\\-\\.:,_@#%$\\+=\\|;]+'],
                '''                Name of the policy file
                ''',
                'policy_name',
                'Cisco-IOS-XR-ha-eem-cfg', True),
            _MetaInfoClassMember('username', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                A configured username
                ''',
                'username',
                'Cisco-IOS-XR-ha-eem-cfg', False, is_mandatory=True),
            _MetaInfoClassMember('persist-time', ATTRIBUTE, 'int', 'Event-manager-persist-time',
                None, None,
                [('0', '4294967295')], [],
                '''                Time of validity (in seconds) for cached AAA
                taskmap of username (default is 3600)
                ''',
                'persist_time',
                'Cisco-IOS-XR-ha-eem-cfg', False, is_mandatory=True),
            _MetaInfoClassMember('policy-type', REFERENCE_ENUM_CLASS, 'EventManagerPolicy', 'Event-manager-policy',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ha_eem_cfg', 'EventManagerPolicy',
                [], [],
                '''                Event manager type of this policy
                ''',
                'policy_type',
                'Cisco-IOS-XR-ha-eem-cfg', False),
            _MetaInfoClassMember('checksum-type', REFERENCE_ENUM_CLASS, 'EventManagerChecksum', 'Event-manager-checksum',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ha_eem_cfg', 'EventManagerChecksum',
                [], [],
                '''                Specify Embedded Event Manager policy checksum
                ''',
                'checksum_type',
                'Cisco-IOS-XR-ha-eem-cfg', False),
            _MetaInfoClassMember('check-sum-value', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                CheckSum Value
                ''',
                'check_sum_value',
                'Cisco-IOS-XR-ha-eem-cfg', False),
            _MetaInfoClassMember('policy-security-mode', REFERENCE_ENUM_CLASS, 'EventManagerPolicyMode', 'Event-manager-policy-mode',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ha_eem_cfg', 'EventManagerPolicyMode',
                [], [],
                '''                Specify Embedded Event Manager policy security
                mode
                ''',
                'policy_security_mode',
                'Cisco-IOS-XR-ha-eem-cfg', False),
            _MetaInfoClassMember('policy-security-level', REFERENCE_ENUM_CLASS, 'EventManagerPolicySec', 'Event-manager-policy-sec',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ha_eem_cfg', 'EventManagerPolicySec',
                [], [],
                '''                Event Manager policy security Level
                ''',
                'policy_security_level',
                'Cisco-IOS-XR-ha-eem-cfg', False),
            ],
            'Cisco-IOS-XR-ha-eem-cfg',
            'policy',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-ha-eem-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ha_eem_cfg',
        ),
    },
    'EventManager.Policies' : {
        'meta_info' : _MetaInfoClass('EventManager.Policies', REFERENCE_CLASS,
            '''Register an event manager policy''',
            False, 
            [
            _MetaInfoClassMember('policy', REFERENCE_LIST, 'Policy', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ha_eem_cfg', 'EventManager.Policies.Policy',
                [], [],
                '''                Name of the policy file
                ''',
                'policy',
                'Cisco-IOS-XR-ha-eem-cfg', False),
            ],
            'Cisco-IOS-XR-ha-eem-cfg',
            'policies',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-ha-eem-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ha_eem_cfg',
        ),
    },
    'EventManager.SchedulerScript.ThreadClasses.ThreadClass' : {
        'meta_info' : _MetaInfoClass('EventManager.SchedulerScript.ThreadClasses.ThreadClass', REFERENCE_LIST,
            '''scheduler classs type argument''',
            False, 
            [
            _MetaInfoClassMember('thread-class-name', ATTRIBUTE, 'str', 'xr:Cisco-ios-xr-string',
                None, None,
                [], [b'[\\w\\-\\.:,_@#%$\\+=\\|;]+'],
                '''                Name of the global variable
                ''',
                'thread_class_name',
                'Cisco-IOS-XR-ha-eem-cfg', True),
            _MetaInfoClassMember('num-threads', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('1', '5')], [],
                '''                number of scheduler threads
                ''',
                'num_threads',
                'Cisco-IOS-XR-ha-eem-cfg', False, is_mandatory=True),
            ],
            'Cisco-IOS-XR-ha-eem-cfg',
            'thread-class',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-ha-eem-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ha_eem_cfg',
        ),
    },
    'EventManager.SchedulerScript.ThreadClasses' : {
        'meta_info' : _MetaInfoClass('EventManager.SchedulerScript.ThreadClasses', REFERENCE_CLASS,
            '''scheduler thread classs ''',
            False, 
            [
            _MetaInfoClassMember('thread-class', REFERENCE_LIST, 'ThreadClass', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ha_eem_cfg', 'EventManager.SchedulerScript.ThreadClasses.ThreadClass',
                [], [],
                '''                scheduler classs type argument
                ''',
                'thread_class',
                'Cisco-IOS-XR-ha-eem-cfg', False),
            ],
            'Cisco-IOS-XR-ha-eem-cfg',
            'thread-classes',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-ha-eem-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ha_eem_cfg',
        ),
    },
    'EventManager.SchedulerScript' : {
        'meta_info' : _MetaInfoClass('EventManager.SchedulerScript', REFERENCE_CLASS,
            '''scheduler classs type''',
            False, 
            [
            _MetaInfoClassMember('thread-classes', REFERENCE_CLASS, 'ThreadClasses', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ha_eem_cfg', 'EventManager.SchedulerScript.ThreadClasses',
                [], [],
                '''                scheduler thread classs 
                ''',
                'thread_classes',
                'Cisco-IOS-XR-ha-eem-cfg', False),
            ],
            'Cisco-IOS-XR-ha-eem-cfg',
            'scheduler-script',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-ha-eem-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ha_eem_cfg',
        ),
    },
    'EventManager.Environments.Environment' : {
        'meta_info' : _MetaInfoClass('EventManager.Environments.Environment', REFERENCE_LIST,
            '''Name of the global variable''',
            False, 
            [
            _MetaInfoClassMember('environment-name', ATTRIBUTE, 'str', 'xr:Cisco-ios-xr-string',
                None, None,
                [], [b'[\\w\\-\\.:,_@#%$\\+=\\|;]+'],
                '''                Name of the global variable
                ''',
                'environment_name',
                'Cisco-IOS-XR-ha-eem-cfg', True),
            _MetaInfoClassMember('environment-value', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                Value of the global variable
                ''',
                'environment_value',
                'Cisco-IOS-XR-ha-eem-cfg', False, is_mandatory=True),
            ],
            'Cisco-IOS-XR-ha-eem-cfg',
            'environment',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-ha-eem-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ha_eem_cfg',
        ),
    },
    'EventManager.Environments' : {
        'meta_info' : _MetaInfoClass('EventManager.Environments', REFERENCE_CLASS,
            '''Set an event manager global variable for event
manager policies''',
            False, 
            [
            _MetaInfoClassMember('environment', REFERENCE_LIST, 'Environment', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ha_eem_cfg', 'EventManager.Environments.Environment',
                [], [],
                '''                Name of the global variable
                ''',
                'environment',
                'Cisco-IOS-XR-ha-eem-cfg', False),
            ],
            'Cisco-IOS-XR-ha-eem-cfg',
            'environments',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-ha-eem-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ha_eem_cfg',
        ),
    },
    'EventManager' : {
        'meta_info' : _MetaInfoClass('EventManager', REFERENCE_CLASS,
            '''Event manager configuration''',
            False, 
            [
            _MetaInfoClassMember('policies', REFERENCE_CLASS, 'Policies', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ha_eem_cfg', 'EventManager.Policies',
                [], [],
                '''                Register an event manager policy
                ''',
                'policies',
                'Cisco-IOS-XR-ha-eem-cfg', False),
            _MetaInfoClassMember('scheduler-script', REFERENCE_CLASS, 'SchedulerScript', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ha_eem_cfg', 'EventManager.SchedulerScript',
                [], [],
                '''                scheduler classs type
                ''',
                'scheduler_script',
                'Cisco-IOS-XR-ha-eem-cfg', False),
            _MetaInfoClassMember('environments', REFERENCE_CLASS, 'Environments', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ha_eem_cfg', 'EventManager.Environments',
                [], [],
                '''                Set an event manager global variable for event
                manager policies
                ''',
                'environments',
                'Cisco-IOS-XR-ha-eem-cfg', False),
            _MetaInfoClassMember('refresh-time', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('10', '4294967295')], [],
                '''                Set refresh time (in seconds) for policy
                username's AAA taskmap
                ''',
                'refresh_time',
                'Cisco-IOS-XR-ha-eem-cfg', False, default_value="1800"),
            _MetaInfoClassMember('schedule-suspend', ATTRIBUTE, 'bool', 'boolean',
                None, None,
                [], [],
                '''                Enable suspend policy scheduling
                ''',
                'schedule_suspend',
                'Cisco-IOS-XR-ha-eem-cfg', False),
            _MetaInfoClassMember('directory-user-policy', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                Set event manager user policy directory
                ''',
                'directory_user_policy',
                'Cisco-IOS-XR-ha-eem-cfg', False),
            _MetaInfoClassMember('directory-user-library', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                Path of the user policy library directory
                ''',
                'directory_user_library',
                'Cisco-IOS-XR-ha-eem-cfg', False),
            ],
            'Cisco-IOS-XR-ha-eem-cfg',
            'event-manager',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-ha-eem-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ha_eem_cfg',
        ),
    },
}
_meta_table['EventManager.Policies.Policy']['meta_info'].parent =_meta_table['EventManager.Policies']['meta_info']
_meta_table['EventManager.SchedulerScript.ThreadClasses.ThreadClass']['meta_info'].parent =_meta_table['EventManager.SchedulerScript.ThreadClasses']['meta_info']
_meta_table['EventManager.SchedulerScript.ThreadClasses']['meta_info'].parent =_meta_table['EventManager.SchedulerScript']['meta_info']
_meta_table['EventManager.Environments.Environment']['meta_info'].parent =_meta_table['EventManager.Environments']['meta_info']
_meta_table['EventManager.Policies']['meta_info'].parent =_meta_table['EventManager']['meta_info']
_meta_table['EventManager.SchedulerScript']['meta_info'].parent =_meta_table['EventManager']['meta_info']
_meta_table['EventManager.Environments']['meta_info'].parent =_meta_table['EventManager']['meta_info']
