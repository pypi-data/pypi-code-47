
'''
This is auto-generated file,
which includes metadata for module Cisco_IOS_XR_linux_os_reboot_history_oper
'''

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_LIST, REFERENCE_LEAFLIST, REFERENCE_BITS, REFERENCE_UNION
from ydk._core._dm_meta_info import REFERENCE_CLASS, REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, ANYXML_CLASS
from ydk._core._importer import _yang_ns

_meta_table = {
    'RebootHistory.Node.RebootHistory_' : {
        'meta_info' : _MetaInfoClass('RebootHistory.Node.RebootHistory_', REFERENCE_LIST,
            '''Last Reboots''',
            False, 
            [
            _MetaInfoClassMember('no', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('0', '4294967295')], [],
                '''                Number count
                ''',
                'no',
                'Cisco-IOS-XR-linux-os-reboot-history-oper', False, is_config=False),
            _MetaInfoClassMember('time', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                Time of reboot
                ''',
                'time',
                'Cisco-IOS-XR-linux-os-reboot-history-oper', False, is_config=False),
            _MetaInfoClassMember('cause-code', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('0', '4294967295')], [],
                '''                Cause code for reboot
                ''',
                'cause_code',
                'Cisco-IOS-XR-linux-os-reboot-history-oper', False, is_config=False),
            _MetaInfoClassMember('reason', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                Reason for reboot
                ''',
                'reason',
                'Cisco-IOS-XR-linux-os-reboot-history-oper', False, is_config=False),
            ],
            'Cisco-IOS-XR-linux-os-reboot-history-oper',
            'reboot-history',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-linux-os-reboot-history-oper'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_linux_os_reboot_history_oper',
            is_config=False,
        ),
    },
    'RebootHistory.Node' : {
        'meta_info' : _MetaInfoClass('RebootHistory.Node', REFERENCE_LIST,
            '''Node ID''',
            False, 
            [
            _MetaInfoClassMember('node-name', ATTRIBUTE, 'str', 'xr:Node-id',
                None, None,
                [], [b'([a-zA-Z0-9_]*\\d+/){1,2}([a-zA-Z0-9_]*\\d+)'],
                '''                Node name
                ''',
                'node_name',
                'Cisco-IOS-XR-linux-os-reboot-history-oper', True, is_config=False),
            _MetaInfoClassMember('reboot-history', REFERENCE_LIST, 'RebootHistory_', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_linux_os_reboot_history_oper', 'RebootHistory.Node.RebootHistory_',
                [], [],
                '''                Last Reboots
                ''',
                'reboot_history',
                'Cisco-IOS-XR-linux-os-reboot-history-oper', False, is_config=False),
            ],
            'Cisco-IOS-XR-linux-os-reboot-history-oper',
            'node',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-linux-os-reboot-history-oper'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_linux_os_reboot_history_oper',
            is_config=False,
        ),
    },
    'RebootHistory' : {
        'meta_info' : _MetaInfoClass('RebootHistory', REFERENCE_CLASS,
            '''Reboot History information''',
            False, 
            [
            _MetaInfoClassMember('node', REFERENCE_LIST, 'Node', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_linux_os_reboot_history_oper', 'RebootHistory.Node',
                [], [],
                '''                Node ID
                ''',
                'node',
                'Cisco-IOS-XR-linux-os-reboot-history-oper', False, is_config=False),
            ],
            'Cisco-IOS-XR-linux-os-reboot-history-oper',
            'reboot-history',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-linux-os-reboot-history-oper'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_linux_os_reboot_history_oper',
            is_config=False,
        ),
    },
}
_meta_table['RebootHistory.Node.RebootHistory_']['meta_info'].parent =_meta_table['RebootHistory.Node']['meta_info']
_meta_table['RebootHistory.Node']['meta_info'].parent =_meta_table['RebootHistory']['meta_info']
