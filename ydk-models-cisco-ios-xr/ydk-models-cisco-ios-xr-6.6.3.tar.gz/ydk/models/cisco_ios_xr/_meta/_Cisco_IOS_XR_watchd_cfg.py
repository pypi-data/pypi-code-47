
'''
This is auto-generated file,
which includes metadata for module Cisco_IOS_XR_watchd_cfg
'''

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_LIST, REFERENCE_LEAFLIST, REFERENCE_BITS, REFERENCE_UNION
from ydk._core._dm_meta_info import REFERENCE_CLASS, REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, ANYXML_CLASS
from ydk._core._importer import _yang_ns

_meta_table = {
    'Watchdog.ThresholdMemory' : {
        'meta_info' : _MetaInfoClass('Watchdog.ThresholdMemory', REFERENCE_CLASS,
            '''Memory thresholds''',
            False, 
            [
            _MetaInfoClassMember('minor', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('5', '40')], [],
                '''                Threshold, Range (5, 40)
                ''',
                'minor',
                'Cisco-IOS-XR-watchd-cfg', False),
            _MetaInfoClassMember('severe', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('4', '40')], [],
                '''                Threshold, Range (4, minor)
                ''',
                'severe',
                'Cisco-IOS-XR-watchd-cfg', False),
            _MetaInfoClassMember('critical', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('3', '40')], [],
                '''                Threshold, Range (3, severe)
                ''',
                'critical',
                'Cisco-IOS-XR-watchd-cfg', False),
            ],
            'Cisco-IOS-XR-watchd-cfg',
            'threshold-memory',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-watchd-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_watchd_cfg',
        ),
    },
    'Watchdog.DiskLimit' : {
        'meta_info' : _MetaInfoClass('Watchdog.DiskLimit', REFERENCE_CLASS,
            '''Disk thresholds''',
            False, 
            [
            _MetaInfoClassMember('minor', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('5', '40')], [],
                '''                Threshold, Range (5, 40)
                ''',
                'minor',
                'Cisco-IOS-XR-watchd-cfg', False),
            _MetaInfoClassMember('severe', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('4', '40')], [],
                '''                Threshold, Range (4, minor)
                ''',
                'severe',
                'Cisco-IOS-XR-watchd-cfg', False),
            _MetaInfoClassMember('critical', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('3', '40')], [],
                '''                Threshold, Range (3, severe)
                ''',
                'critical',
                'Cisco-IOS-XR-watchd-cfg', False),
            ],
            'Cisco-IOS-XR-watchd-cfg',
            'disk-limit',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-watchd-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_watchd_cfg',
        ),
    },
    'Watchdog' : {
        'meta_info' : _MetaInfoClass('Watchdog', REFERENCE_CLASS,
            '''Watchdog configuration commands''',
            False, 
            [
            _MetaInfoClassMember('threshold-memory', REFERENCE_CLASS, 'ThresholdMemory', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_watchd_cfg', 'Watchdog.ThresholdMemory',
                [], [],
                '''                Memory thresholds
                ''',
                'threshold_memory',
                'Cisco-IOS-XR-watchd-cfg', False),
            _MetaInfoClassMember('disk-limit', REFERENCE_CLASS, 'DiskLimit', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_watchd_cfg', 'Watchdog.DiskLimit',
                [], [],
                '''                Disk thresholds
                ''',
                'disk_limit',
                'Cisco-IOS-XR-watchd-cfg', False),
            _MetaInfoClassMember('overload-notification', ATTRIBUTE, 'Empty', 'empty',
                None, None,
                [], [],
                '''                Disable critical event notification
                ''',
                'overload_notification',
                'Cisco-IOS-XR-watchd-cfg', False),
            _MetaInfoClassMember('restart-deadlock-disable', ATTRIBUTE, 'Empty', 'empty',
                None, None,
                [], [],
                '''                Disable watchdog restart deadlock
                ''',
                'restart_deadlock_disable',
                'Cisco-IOS-XR-watchd-cfg', False),
            _MetaInfoClassMember('restart-memoryhog-disable', ATTRIBUTE, 'Empty', 'empty',
                None, None,
                [], [],
                '''                Disable watchdog restart memory-hog
                ''',
                'restart_memoryhog_disable',
                'Cisco-IOS-XR-watchd-cfg', False),
            _MetaInfoClassMember('overload-throttle-timeout', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('5', '120')], [],
                '''                Watchdog overload throttle timeout configuration
                ''',
                'overload_throttle_timeout',
                'Cisco-IOS-XR-watchd-cfg', False),
            ],
            'Cisco-IOS-XR-watchd-cfg',
            'watchdog',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-watchd-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_watchd_cfg',
        ),
    },
    'Watchd' : {
        'meta_info' : _MetaInfoClass('Watchd', REFERENCE_CLASS,
            '''watchd''',
            False, 
            [
            _MetaInfoClassMember('timeout', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('1', '10')], [],
                '''                Length of timeout in seconds
                ''',
                'timeout',
                'Cisco-IOS-XR-watchd-cfg', False),
            ],
            'Cisco-IOS-XR-watchd-cfg',
            'watchd',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-watchd-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_watchd_cfg',
        ),
    },
}
_meta_table['Watchdog.ThresholdMemory']['meta_info'].parent =_meta_table['Watchdog']['meta_info']
_meta_table['Watchdog.DiskLimit']['meta_info'].parent =_meta_table['Watchdog']['meta_info']
