
'''
This is auto-generated file,
which includes metadata for module Cisco_IOS_XR_freqsync_datatypes
'''

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_LIST, REFERENCE_LEAFLIST, REFERENCE_BITS, REFERENCE_UNION
from ydk._core._dm_meta_info import REFERENCE_CLASS, REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, ANYXML_CLASS
from ydk._core._importer import _yang_ns

_meta_table = {
    'FsyncQlOption' : _MetaInfoEnum('FsyncQlOption',
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_datatypes', 'FsyncQlOption',
        '''Fsync ql option''',
        {
            'option-1':'option_1',
            'option-2,-generation-1':'option_2__COMMA___generation_1',
            'option-2,-generation-2':'option_2__COMMA___generation_2',
        }, 'Cisco-IOS-XR-freqsync-datatypes', _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-freqsync-datatypes']),
    'Gnss1ppsPolarity' : _MetaInfoEnum('Gnss1ppsPolarity',
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_datatypes', 'Gnss1ppsPolarity',
        '''Gnss1pps polarity''',
        {
            'positive':'positive',
            'negative':'negative',
        }, 'Cisco-IOS-XR-freqsync-datatypes', _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-freqsync-datatypes']),
    'GnssConstellation' : _MetaInfoEnum('GnssConstellation',
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_datatypes', 'GnssConstellation',
        '''Gnss constellation''',
        {
            'auto':'auto',
            'gps':'gps',
            'galileo':'galileo',
            'bei-dou':'bei_dou',
            'qzss':'qzss',
            'glonass':'glonass',
            'sbas':'sbas',
            'irnss':'irnss',
        }, 'Cisco-IOS-XR-freqsync-datatypes', _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-freqsync-datatypes']),
    'FsyncClock' : _MetaInfoEnum('FsyncClock',
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_datatypes', 'FsyncClock',
        '''Fsync clock''',
        {
            'sync':'sync',
            'internal':'internal',
            'gnss':'gnss',
        }, 'Cisco-IOS-XR-freqsync-datatypes', _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-freqsync-datatypes']),
    'FsyncQlValue' : _MetaInfoEnum('FsyncQlValue',
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_datatypes', 'FsyncQlValue',
        '''Fsync ql value''',
        {
            'dnu':'dnu',
            'o1-prc':'o1_prc',
            'o1-ssu-a':'o1_ssu_a',
            'o1-ssu-b':'o1_ssu_b',
            'o1-sec':'o1_sec',
            'o2-g1-prs':'o2_g1_prs',
            'o2-g1-stu':'o2_g1_stu',
            'o2-g1-st2':'o2_g1_st2',
            'o2-g1-st3':'o2_g1_st3',
            'o2-g1-smc':'o2_g1_smc',
            'o2-g1-st4':'o2_g1_st4',
            'o2-g2-prs':'o2_g2_prs',
            'o2-g2-stu':'o2_g2_stu',
            'o2-g2-st2':'o2_g2_st2',
            'o2-g2-st3':'o2_g2_st3',
            'o2-g2-tnc':'o2_g2_tnc',
            'o2-g2-st3e':'o2_g2_st3e',
            'o2-g2-smc':'o2_g2_smc',
            'o2-g2-st4':'o2_g2_st4',
        }, 'Cisco-IOS-XR-freqsync-datatypes', _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-freqsync-datatypes']),
}
