
'''
This is auto-generated file,
which includes metadata for module Cisco_IOS_XR_man_netconf_cfg
'''

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_LIST, REFERENCE_LEAFLIST, REFERENCE_BITS, REFERENCE_UNION
from ydk._core._dm_meta_info import REFERENCE_CLASS, REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, ANYXML_CLASS
from ydk._core._importer import _yang_ns

_meta_table = {
    'NetconfYang.Agent.Models.Openconfig' : {
        'meta_info' : _MetaInfoClass('NetconfYang.Agent.Models.Openconfig', REFERENCE_CLASS,
            '''Type of models: openconfig''',
            False, 
            [
            _MetaInfoClassMember('disabled', ATTRIBUTE, 'Empty', 'empty',
                None, None,
                [], [],
                '''                Disable the specified model type
                ''',
                'disabled',
                'Cisco-IOS-XR-man-netconf-cfg', False),
            ],
            'Cisco-IOS-XR-man-netconf-cfg',
            'openconfig',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-man-netconf-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_netconf_cfg',
        ),
    },
    'NetconfYang.Agent.Models' : {
        'meta_info' : _MetaInfoClass('NetconfYang.Agent.Models', REFERENCE_CLASS,
            '''Models to be disabled''',
            False, 
            [
            _MetaInfoClassMember('openconfig', REFERENCE_CLASS, 'Openconfig', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_netconf_cfg', 'NetconfYang.Agent.Models.Openconfig',
                [], [],
                '''                Type of models: openconfig
                ''',
                'openconfig',
                'Cisco-IOS-XR-man-netconf-cfg', False),
            ],
            'Cisco-IOS-XR-man-netconf-cfg',
            'models',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-man-netconf-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_netconf_cfg',
        ),
    },
    'NetconfYang.Agent.Ssh' : {
        'meta_info' : _MetaInfoClass('NetconfYang.Agent.Ssh', REFERENCE_CLASS,
            '''NETCONF YANG agent over SSH connection''',
            False, 
            [
            _MetaInfoClassMember('enable', ATTRIBUTE, 'Empty', 'empty',
                None, None,
                [], [],
                '''                Enable NETCONF YANG agent over SSH connection
                ''',
                'enable',
                'Cisco-IOS-XR-man-netconf-cfg', False),
            ],
            'Cisco-IOS-XR-man-netconf-cfg',
            'ssh',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-man-netconf-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_netconf_cfg',
        ),
    },
    'NetconfYang.Agent.Session' : {
        'meta_info' : _MetaInfoClass('NetconfYang.Agent.Session', REFERENCE_CLASS,
            '''Session settings''',
            False, 
            [
            _MetaInfoClassMember('limit', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('1', '50')], [],
                '''                Count of allowable concurrent netconf-yang
                sessions
                ''',
                'limit',
                'Cisco-IOS-XR-man-netconf-cfg', False, default_value="50"),
            _MetaInfoClassMember('absolute-timeout', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('1', '1440')], [],
                '''                Absolute timeout in minutes
                ''',
                'absolute_timeout',
                'Cisco-IOS-XR-man-netconf-cfg', False),
            _MetaInfoClassMember('idle-timeout', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('1', '1440')], [],
                '''                Non-active session lifetime
                ''',
                'idle_timeout',
                'Cisco-IOS-XR-man-netconf-cfg', False),
            ],
            'Cisco-IOS-XR-man-netconf-cfg',
            'session',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-man-netconf-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_netconf_cfg',
        ),
    },
    'NetconfYang.Agent' : {
        'meta_info' : _MetaInfoClass('NetconfYang.Agent', REFERENCE_CLASS,
            '''NETCONF YANG agent configuration commands''',
            False, 
            [
            _MetaInfoClassMember('models', REFERENCE_CLASS, 'Models', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_netconf_cfg', 'NetconfYang.Agent.Models',
                [], [],
                '''                Models to be disabled
                ''',
                'models',
                'Cisco-IOS-XR-man-netconf-cfg', False),
            _MetaInfoClassMember('ssh', REFERENCE_CLASS, 'Ssh', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_netconf_cfg', 'NetconfYang.Agent.Ssh',
                [], [],
                '''                NETCONF YANG agent over SSH connection
                ''',
                'ssh',
                'Cisco-IOS-XR-man-netconf-cfg', False),
            _MetaInfoClassMember('session', REFERENCE_CLASS, 'Session', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_netconf_cfg', 'NetconfYang.Agent.Session',
                [], [],
                '''                Session settings
                ''',
                'session',
                'Cisco-IOS-XR-man-netconf-cfg', False),
            _MetaInfoClassMember('rate-limit', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('4096', '4294967295')], [],
                '''                Number of bytes to process per sec
                ''',
                'rate_limit',
                'Cisco-IOS-XR-man-netconf-cfg', False),
            ],
            'Cisco-IOS-XR-man-netconf-cfg',
            'agent',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-man-netconf-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_netconf_cfg',
        ),
    },
    'NetconfYang' : {
        'meta_info' : _MetaInfoClass('NetconfYang', REFERENCE_CLASS,
            '''NETCONF YANG configuration commands''',
            False, 
            [
            _MetaInfoClassMember('agent', REFERENCE_CLASS, 'Agent', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_netconf_cfg', 'NetconfYang.Agent',
                [], [],
                '''                NETCONF YANG agent configuration commands
                ''',
                'agent',
                'Cisco-IOS-XR-man-netconf-cfg', False),
            ],
            'Cisco-IOS-XR-man-netconf-cfg',
            'netconf-yang',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-man-netconf-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_netconf_cfg',
        ),
    },
}
_meta_table['NetconfYang.Agent.Models.Openconfig']['meta_info'].parent =_meta_table['NetconfYang.Agent.Models']['meta_info']
_meta_table['NetconfYang.Agent.Models']['meta_info'].parent =_meta_table['NetconfYang.Agent']['meta_info']
_meta_table['NetconfYang.Agent.Ssh']['meta_info'].parent =_meta_table['NetconfYang.Agent']['meta_info']
_meta_table['NetconfYang.Agent.Session']['meta_info'].parent =_meta_table['NetconfYang.Agent']['meta_info']
_meta_table['NetconfYang.Agent']['meta_info'].parent =_meta_table['NetconfYang']['meta_info']
