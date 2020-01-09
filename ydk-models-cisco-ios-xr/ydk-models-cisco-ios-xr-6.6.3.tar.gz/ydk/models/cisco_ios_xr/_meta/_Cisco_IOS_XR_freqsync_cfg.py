
'''
This is auto-generated file,
which includes metadata for module Cisco_IOS_XR_freqsync_cfg
'''

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_LIST, REFERENCE_LEAFLIST, REFERENCE_BITS, REFERENCE_UNION
from ydk._core._dm_meta_info import REFERENCE_CLASS, REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, ANYXML_CLASS
from ydk._core._importer import _yang_ns

_meta_table = {
    'FsyncSystemTimingMode' : _MetaInfoEnum('FsyncSystemTimingMode',
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_cfg', 'FsyncSystemTimingMode',
        '''Fsync system timing mode''',
        {
            'line-only':'line_only',
            'clock-only':'clock_only',
        }, 'Cisco-IOS-XR-freqsync-cfg', _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-freqsync-cfg']),
    'FsyncClockSource' : _MetaInfoEnum('FsyncClockSource',
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_cfg', 'FsyncClockSource',
        '''Fsync clock source''',
        {
            'system':'system',
            'independent':'independent',
        }, 'Cisco-IOS-XR-freqsync-cfg', _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-freqsync-cfg']),
    'FsyncSourceSelectionLogging' : _MetaInfoEnum('FsyncSourceSelectionLogging',
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_cfg', 'FsyncSourceSelectionLogging',
        '''Fsync source selection logging''',
        {
            'changes':'changes',
            'errors':'errors',
        }, 'Cisco-IOS-XR-freqsync-cfg', _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-freqsync-cfg']),
    'FrequencySynchronization' : {
        'meta_info' : _MetaInfoClass('FrequencySynchronization', REFERENCE_CLASS,
            '''frequency synchronization''',
            False, 
            [
            _MetaInfoClassMember('quality-level-option', REFERENCE_ENUM_CLASS, 'FsyncQlOption', 'dt1:Fsync-ql-option',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_datatypes', 'FsyncQlOption',
                [], [],
                '''                Quality level option
                ''',
                'quality_level_option',
                'Cisco-IOS-XR-freqsync-cfg', False, default_value='Cisco_IOS_XR_freqsync_datatypes.FsyncQlOption.option_1'),
            _MetaInfoClassMember('enable', ATTRIBUTE, 'Empty', 'empty',
                None, None,
                [], [],
                '''                Enable Frequency Synchronization
                ''',
                'enable',
                'Cisco-IOS-XR-freqsync-cfg', False),
            _MetaInfoClassMember('source-selection-logging', REFERENCE_ENUM_CLASS, 'FsyncSourceSelectionLogging', 'Fsync-source-selection-logging',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_cfg', 'FsyncSourceSelectionLogging',
                [], [],
                '''                Source selection logging option
                ''',
                'source_selection_logging',
                'Cisco-IOS-XR-freqsync-cfg', False),
            _MetaInfoClassMember('clock-interface-source-type', REFERENCE_ENUM_CLASS, 'FsyncClockSource', 'Fsync-clock-source',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_cfg', 'FsyncClockSource',
                [], [],
                '''                Clock interface source type
                ''',
                'clock_interface_source_type',
                'Cisco-IOS-XR-freqsync-cfg', False),
            _MetaInfoClassMember('system-timing-mode', REFERENCE_ENUM_CLASS, 'FsyncSystemTimingMode', 'Fsync-system-timing-mode',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_cfg', 'FsyncSystemTimingMode',
                [], [],
                '''                System timing mode
                ''',
                'system_timing_mode',
                'Cisco-IOS-XR-freqsync-cfg', False),
            ],
            'Cisco-IOS-XR-freqsync-cfg',
            'frequency-synchronization',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-freqsync-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_cfg',
        ),
    },
}
