
'''
This is auto-generated file,
which includes metadata for module Cisco_IOS_XR_bundlemgr_cfg
'''

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_LIST, REFERENCE_LEAFLIST, REFERENCE_BITS, REFERENCE_UNION
from ydk._core._dm_meta_info import REFERENCE_CLASS, REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, ANYXML_CLASS
from ydk._core._importer import _yang_ns

_meta_table = {
    'BfdMode' : _MetaInfoEnum('BfdMode',
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_bundlemgr_cfg', 'BfdMode',
        '''Bfd mode''',
        {
            'no-cfg':'no_cfg',
            'cisco':'cisco',
            'ietf':'ietf',
        }, 'Cisco-IOS-XR-bundlemgr-cfg', _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-bundlemgr-cfg']),
    'ChurnLogging' : _MetaInfoEnum('ChurnLogging',
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_bundlemgr_cfg', 'ChurnLogging',
        '''Churn logging''',
        {
            'actor':'actor',
            'partner':'partner',
            'both':'both',
        }, 'Cisco-IOS-XR-bundlemgr-cfg', _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-bundlemgr-cfg']),
    'BundleMode' : _MetaInfoEnum('BundleMode',
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_bundlemgr_cfg', 'BundleMode',
        '''Bundle mode''',
        {
            'on':'on',
            'active':'active',
            'passive':'passive',
        }, 'Cisco-IOS-XR-bundlemgr-cfg', _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-bundlemgr-cfg']),
    'BundleMinimumBandwidthRange' : _MetaInfoEnum('BundleMinimumBandwidthRange',
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_bundlemgr_cfg', 'BundleMinimumBandwidthRange',
        '''Bundle minimum bandwidth range''',
        {
            'none':'none',
            'kbps':'kbps',
            'mbps':'mbps',
            'gbps':'gbps',
        }, 'Cisco-IOS-XR-bundlemgr-cfg', _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-bundlemgr-cfg']),
    'PeriodShortEnum' : _MetaInfoEnum('PeriodShortEnum',
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_bundlemgr_cfg', 'PeriodShortEnum',
        ''' ''',
        {
            'true':'true',
        }, 'Cisco-IOS-XR-bundlemgr-cfg', _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-bundlemgr-cfg']),
    'BundleCiscoExtTypes' : _MetaInfoEnum('BundleCiscoExtTypes',
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_bundlemgr_cfg', 'BundleCiscoExtTypes',
        '''Bundle cisco ext types''',
        {
            'lon-signaling-off':'lon_signaling_off',
            'lon-signaling-on':'lon_signaling_on',
        }, 'Cisco-IOS-XR-bundlemgr-cfg', _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-bundlemgr-cfg']),
    'BundleMaximumActiveLinksMode' : _MetaInfoEnum('BundleMaximumActiveLinksMode',
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_bundlemgr_cfg', 'BundleMaximumActiveLinksMode',
        '''Bundle maximum active links mode''',
        {
            'default':'default',
            'hot-standby':'hot_standby',
        }, 'Cisco-IOS-XR-bundlemgr-cfg', _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-bundlemgr-cfg']),
    'MlacpSwitchover' : _MetaInfoEnum('MlacpSwitchover',
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_bundlemgr_cfg', 'MlacpSwitchover',
        '''Mlacp switchover''',
        {
            'brute-force':'brute_force',
            'revertive':'revertive',
        }, 'Cisco-IOS-XR-bundlemgr-cfg', _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-bundlemgr-cfg']),
    'BundleLoadBalance' : _MetaInfoEnum('BundleLoadBalance',
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_bundlemgr_cfg', 'BundleLoadBalance',
        '''Bundle load balance''',
        {
            'default':'default',
            'efp-auto':'efp_auto',
            'efp-value':'efp_value',
            'source-ip':'source_ip',
            'destination-ip':'destination_ip',
        }, 'Cisco-IOS-XR-bundlemgr-cfg', _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-bundlemgr-cfg']),
    'BundlePortActivity' : _MetaInfoEnum('BundlePortActivity',
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_bundlemgr_cfg', 'BundlePortActivity',
        '''Bundle port activity''',
        {
            'on':'on',
            'active':'active',
            'passive':'passive',
            'inherit':'inherit',
        }, 'Cisco-IOS-XR-bundlemgr-cfg', _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-bundlemgr-cfg']),
    'MlacpMaximizeParameter' : _MetaInfoEnum('MlacpMaximizeParameter',
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_bundlemgr_cfg', 'MlacpMaximizeParameter',
        '''Mlacp maximize parameter''',
        {
            'links':'links',
            'bandwidth':'bandwidth',
        }, 'Cisco-IOS-XR-bundlemgr-cfg', _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-bundlemgr-cfg']),
    'BundlePeriod' : _MetaInfoEnum('BundlePeriod',
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_bundlemgr_cfg', 'BundlePeriod',
        ''' ''',
        {
            'true':'true',
        }, 'Cisco-IOS-XR-bundlemgr-cfg', _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-bundlemgr-cfg']),
    'Lacp' : {
        'meta_info' : _MetaInfoClass('Lacp', REFERENCE_CLASS,
            '''Link Aggregation Control Protocol commands''',
            False, 
            [
            _MetaInfoClassMember('system-mac', ATTRIBUTE, 'str', 'yang:mac-address',
                None, None,
                [], [b'[0-9a-fA-F]{2}(:[0-9a-fA-F]{2}){5}'],
                '''                Unique identifier for this system.
                ''',
                'system_mac',
                'Cisco-IOS-XR-bundlemgr-cfg', False),
            _MetaInfoClassMember('system-priority', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('1', '65535')], [],
                '''                Priority for this system. Lower value is higher
                priority.
                ''',
                'system_priority',
                'Cisco-IOS-XR-bundlemgr-cfg', False, default_value="32768"),
            ],
            'Cisco-IOS-XR-bundlemgr-cfg',
            'lacp',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-bundlemgr-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_bundlemgr_cfg',
        ),
    },
}
