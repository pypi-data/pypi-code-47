
'''
This is auto-generated file,
which includes metadata for module Cisco_IOS_XR_ptp_datatypes
'''

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_LIST, REFERENCE_LEAFLIST, REFERENCE_BITS, REFERENCE_UNION
from ydk._core._dm_meta_info import REFERENCE_CLASS, REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, ANYXML_CLASS
from ydk._core._importer import _yang_ns

_meta_table = {
    'PtpTime' : _MetaInfoEnum('PtpTime',
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ptp_datatypes', 'PtpTime',
        '''Ptp time''',
        {
            'interval':'interval',
            'frequency':'frequency',
        }, 'Cisco-IOS-XR-ptp-datatypes', _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-ptp-datatypes']),
    'PtpClockAdvertisementMode' : _MetaInfoEnum('PtpClockAdvertisementMode',
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ptp_datatypes', 'PtpClockAdvertisementMode',
        '''Ptp clock advertisement mode''',
        {
            '1588v2':'Y_1588v2',
            'telecom-profile':'telecom_profile',
        }, 'Cisco-IOS-XR-ptp-datatypes', _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-ptp-datatypes']),
    'PtpEncap' : _MetaInfoEnum('PtpEncap',
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ptp_datatypes', 'PtpEncap',
        '''Ptp encap''',
        {
            'ethernet':'ethernet',
            'ipv4':'ipv4',
            'ipv6':'ipv6',
        }, 'Cisco-IOS-XR-ptp-datatypes', _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-ptp-datatypes']),
    'PtpTimePeriod' : _MetaInfoEnum('PtpTimePeriod',
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ptp_datatypes', 'PtpTimePeriod',
        '''Ptp time period''',
        {
            '1':'Y_1',
            '2':'Y_2',
            '4':'Y_4',
            '8':'Y_8',
            '16':'Y_16',
            '32':'Y_32',
            '64':'Y_64',
            '128':'Y_128',
        }, 'Cisco-IOS-XR-ptp-datatypes', _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-ptp-datatypes']),
    'PtpClockOperation' : _MetaInfoEnum('PtpClockOperation',
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ptp_datatypes', 'PtpClockOperation',
        '''Ptp clock operation''',
        {
            'two-step':'two_step',
            'one-step':'one_step',
        }, 'Cisco-IOS-XR-ptp-datatypes', _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-ptp-datatypes']),
    'PtpClockSelectionMode' : _MetaInfoEnum('PtpClockSelectionMode',
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ptp_datatypes', 'PtpClockSelectionMode',
        '''Ptp clock selection mode''',
        {
            '1588v2':'Y_1588v2',
            'telecom-profile':'telecom_profile',
        }, 'Cisco-IOS-XR-ptp-datatypes', _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-ptp-datatypes']),
    'PtpTimescale' : _MetaInfoEnum('PtpTimescale',
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ptp_datatypes', 'PtpTimescale',
        '''Ptp timescale''',
        {
            'ptp':'ptp',
            'arb':'arb',
        }, 'Cisco-IOS-XR-ptp-datatypes', _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-ptp-datatypes']),
    'PtpDelayAsymmetryUnits' : _MetaInfoEnum('PtpDelayAsymmetryUnits',
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ptp_datatypes', 'PtpDelayAsymmetryUnits',
        '''Ptp delay asymmetry units''',
        {
            'nanoseconds':'nanoseconds',
            'microseconds':'microseconds',
            'milliseconds':'milliseconds',
        }, 'Cisco-IOS-XR-ptp-datatypes', _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-ptp-datatypes']),
    'PtpTimeSource' : _MetaInfoEnum('PtpTimeSource',
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ptp_datatypes', 'PtpTimeSource',
        '''Ptp time source''',
        {
            'unknown':'unknown',
            'atomic-clock':'atomic_clock',
            'gps':'gps',
            'terrestrial-radio':'terrestrial_radio',
            'ptp':'ptp',
            'ntp':'ntp',
            'hand-set':'hand_set',
            'other':'other',
            'internal-oscillator':'internal_oscillator',
        }, 'Cisco-IOS-XR-ptp-datatypes', _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-ptp-datatypes']),
    'PtpPortState' : _MetaInfoEnum('PtpPortState',
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ptp_datatypes', 'PtpPortState',
        '''Ptp port state''',
        {
            'any':'any',
            'slave-only':'slave_only',
            'master-only':'master_only',
        }, 'Cisco-IOS-XR-ptp-datatypes', _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-ptp-datatypes']),
    'PtpClockProfile' : _MetaInfoEnum('PtpClockProfile',
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ptp_datatypes', 'PtpClockProfile',
        '''Ptp clock profile''',
        {
            'default':'default',
            'g82651':'g82651',
            'g82751':'g82751',
            'g82752':'g82752',
        }, 'Cisco-IOS-XR-ptp-datatypes', _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-ptp-datatypes']),
    'PtpTransport' : _MetaInfoEnum('PtpTransport',
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ptp_datatypes', 'PtpTransport',
        '''Ptp transport''',
        {
            'unicast':'unicast',
            'mixed-mode':'mixed_mode',
            'multicast':'multicast',
        }, 'Cisco-IOS-XR-ptp-datatypes', _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-ptp-datatypes']),
    'PtpClockId' : _MetaInfoEnum('PtpClockId',
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ptp_datatypes', 'PtpClockId',
        '''Ptp clock id''',
        {
            'router-mac':'router_mac',
            'user-mac':'user_mac',
            'eui':'eui',
        }, 'Cisco-IOS-XR-ptp-datatypes', _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-ptp-datatypes']),
    'PtpInvalidUnicastGrantRequestResponse' : _MetaInfoEnum('PtpInvalidUnicastGrantRequestResponse',
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ptp_datatypes', 'PtpInvalidUnicastGrantRequestResponse',
        '''Ptp invalid unicast grant request response''',
        {
            'reduce':'reduce',
            'deny':'deny',
        }, 'Cisco-IOS-XR-ptp-datatypes', _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-ptp-datatypes']),
    'PtpTelecomClock' : _MetaInfoEnum('PtpTelecomClock',
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ptp_datatypes', 'PtpTelecomClock',
        '''Ptp telecom clock''',
        {
            'telecom-grandmaster':'telecom_grandmaster',
            'telecom-boundary':'telecom_boundary',
            'telecom-slave':'telecom_slave',
        }, 'Cisco-IOS-XR-ptp-datatypes', _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-ptp-datatypes']),
}
