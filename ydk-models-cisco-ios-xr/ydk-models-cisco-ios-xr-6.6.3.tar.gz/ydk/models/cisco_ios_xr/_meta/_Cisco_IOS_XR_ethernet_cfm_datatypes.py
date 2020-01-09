
'''
This is auto-generated file,
which includes metadata for module Cisco_IOS_XR_ethernet_cfm_datatypes
'''

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_LIST, REFERENCE_LEAFLIST, REFERENCE_BITS, REFERENCE_UNION
from ydk._core._dm_meta_info import REFERENCE_CLASS, REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, ANYXML_CLASS
from ydk._core._importer import _yang_ns

_meta_table = {
    'CfmBandwidthNotificationState' : _MetaInfoEnum('CfmBandwidthNotificationState',
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_datatypes', 'CfmBandwidthNotificationState',
        '''Cfm bandwidth notification state''',
        {
            'ok':'ok',
            'degraded':'degraded',
        }, 'Cisco-IOS-XR-ethernet-cfm-datatypes', _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-ethernet-cfm-datatypes']),
    'CfmCcmInterval' : _MetaInfoEnum('CfmCcmInterval',
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_datatypes', 'CfmCcmInterval',
        '''Cfm ccm interval''',
        {
            '3.3ms':'Y_3__DOT__3ms',
            '10ms':'Y_10ms',
            '100ms':'Y_100ms',
            '1s':'Y_1s',
            '10s':'Y_10s',
            '1m':'Y_1m',
            '10m':'Y_10m',
        }, 'Cisco-IOS-XR-ethernet-cfm-datatypes', _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-ethernet-cfm-datatypes']),
    'CfmAisInterval' : _MetaInfoEnum('CfmAisInterval',
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_datatypes', 'CfmAisInterval',
        '''Cfm ais interval''',
        {
            '1s':'Y_1s',
            '1m':'Y_1m',
        }, 'Cisco-IOS-XR-ethernet-cfm-datatypes', _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-ethernet-cfm-datatypes']),
    'CfmMepDir' : _MetaInfoEnum('CfmMepDir',
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_datatypes', 'CfmMepDir',
        '''Cfm mep dir''',
        {
            'up':'up',
            'down':'down',
        }, 'Cisco-IOS-XR-ethernet-cfm-datatypes', _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-ethernet-cfm-datatypes']),
}
