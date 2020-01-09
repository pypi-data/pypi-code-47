
'''
This is auto-generated file,
which includes metadata for module Cisco_IOS_XR_iedge4710_cfg
'''

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_LIST, REFERENCE_LEAFLIST, REFERENCE_BITS, REFERENCE_UNION
from ydk._core._dm_meta_info import REFERENCE_CLASS, REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, ANYXML_CLASS
from ydk._core._importer import _yang_ns

_meta_table = {
    'SubscriberManager.Accounting.SendStop.SetupFailure' : {
        'meta_info' : _MetaInfoClass('SubscriberManager.Accounting.SendStop.SetupFailure', REFERENCE_CLASS,
            '''Setup failure feature''',
            False, 
            [
            _MetaInfoClassMember('method-list-name', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                AAA List name either default or preconfigured
                ''',
                'method_list_name',
                'Cisco-IOS-XR-iedge4710-cfg', False),
            ],
            'Cisco-IOS-XR-iedge4710-cfg',
            'setup-failure',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-iedge4710-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_cfg',
        ),
    },
    'SubscriberManager.Accounting.SendStop' : {
        'meta_info' : _MetaInfoClass('SubscriberManager.Accounting.SendStop', REFERENCE_CLASS,
            '''Accounting send stop feature''',
            False, 
            [
            _MetaInfoClassMember('setup-failure', REFERENCE_CLASS, 'SetupFailure', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_cfg', 'SubscriberManager.Accounting.SendStop.SetupFailure',
                [], [],
                '''                Setup failure feature
                ''',
                'setup_failure',
                'Cisco-IOS-XR-iedge4710-cfg', False),
            ],
            'Cisco-IOS-XR-iedge4710-cfg',
            'send-stop',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-iedge4710-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_cfg',
        ),
    },
    'SubscriberManager.Accounting.Interim.Variation' : {
        'meta_info' : _MetaInfoClass('SubscriberManager.Accounting.Interim.Variation', REFERENCE_CLASS,
            '''variation of first session or service interim
record from configured timeout''',
            False, 
            [
            _MetaInfoClassMember('maximum-percentage-variation', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('0', '50')], [],
                '''                maximum percentage variation (maximum
                absolute variation is 15 minutes)
                ''',
                'maximum_percentage_variation',
                'Cisco-IOS-XR-iedge4710-cfg', False),
            ],
            'Cisco-IOS-XR-iedge4710-cfg',
            'variation',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-iedge4710-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_cfg',
        ),
    },
    'SubscriberManager.Accounting.Interim' : {
        'meta_info' : _MetaInfoClass('SubscriberManager.Accounting.Interim', REFERENCE_CLASS,
            '''interim accounting related''',
            False, 
            [
            _MetaInfoClassMember('variation', REFERENCE_CLASS, 'Variation', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_cfg', 'SubscriberManager.Accounting.Interim.Variation',
                [], [],
                '''                variation of first session or service interim
                record from configured timeout
                ''',
                'variation',
                'Cisco-IOS-XR-iedge4710-cfg', False),
            ],
            'Cisco-IOS-XR-iedge4710-cfg',
            'interim',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-iedge4710-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_cfg',
        ),
    },
    'SubscriberManager.Accounting' : {
        'meta_info' : _MetaInfoClass('SubscriberManager.Accounting', REFERENCE_CLASS,
            '''iEdge accounting feature''',
            False, 
            [
            _MetaInfoClassMember('send-stop', REFERENCE_CLASS, 'SendStop', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_cfg', 'SubscriberManager.Accounting.SendStop',
                [], [],
                '''                Accounting send stop feature
                ''',
                'send_stop',
                'Cisco-IOS-XR-iedge4710-cfg', False),
            _MetaInfoClassMember('interim', REFERENCE_CLASS, 'Interim', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_cfg', 'SubscriberManager.Accounting.Interim',
                [], [],
                '''                interim accounting related
                ''',
                'interim',
                'Cisco-IOS-XR-iedge4710-cfg', False),
            ],
            'Cisco-IOS-XR-iedge4710-cfg',
            'accounting',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-iedge4710-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_cfg',
        ),
    },
    'SubscriberManager.Srg' : {
        'meta_info' : _MetaInfoClass('SubscriberManager.Srg', REFERENCE_CLASS,
            '''SRG specific config''',
            False, 
            [
            _MetaInfoClassMember('sync-account-session-id', ATTRIBUTE, 'Empty', 'empty',
                None, None,
                [], [],
                '''                sync account session id from master to slave
                ''',
                'sync_account_session_id',
                'Cisco-IOS-XR-iedge4710-cfg', False),
            ],
            'Cisco-IOS-XR-iedge4710-cfg',
            'srg',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-iedge4710-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_cfg',
        ),
    },
    'SubscriberManager' : {
        'meta_info' : _MetaInfoClass('SubscriberManager', REFERENCE_CLASS,
            '''iEdge subscriber manager configuration''',
            False, 
            [
            _MetaInfoClassMember('accounting', REFERENCE_CLASS, 'Accounting', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_cfg', 'SubscriberManager.Accounting',
                [], [],
                '''                iEdge accounting feature
                ''',
                'accounting',
                'Cisco-IOS-XR-iedge4710-cfg', False),
            _MetaInfoClassMember('srg', REFERENCE_CLASS, 'Srg', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_cfg', 'SubscriberManager.Srg',
                [], [],
                '''                SRG specific config
                ''',
                'srg',
                'Cisco-IOS-XR-iedge4710-cfg', False),
            ],
            'Cisco-IOS-XR-iedge4710-cfg',
            'subscriber-manager',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-iedge4710-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_cfg',
        ),
    },
    'SubscriberFeaturette.FeaturetteName' : {
        'meta_info' : _MetaInfoClass('SubscriberFeaturette.FeaturetteName', REFERENCE_LIST,
            '''enable featurette processing''',
            False, 
            [
            _MetaInfoClassMember('featurette', ATTRIBUTE, 'str', 'xr:Cisco-ios-xr-string',
                None, None,
                [], [b'[\\w\\-\\.:,_@#%$\\+=\\|;]+'],
                '''                subscriber feature
                ''',
                'featurette',
                'Cisco-IOS-XR-iedge4710-cfg', True),
            _MetaInfoClassMember('enable', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('0', '4294967295')], [],
                '''                instance of featurette
                ''',
                'enable',
                'Cisco-IOS-XR-iedge4710-cfg', False),
            ],
            'Cisco-IOS-XR-iedge4710-cfg',
            'featurette-name',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-iedge4710-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_cfg',
        ),
    },
    'SubscriberFeaturette' : {
        'meta_info' : _MetaInfoClass('SubscriberFeaturette', REFERENCE_CLASS,
            '''subscriber featurette''',
            False, 
            [
            _MetaInfoClassMember('featurette-name', REFERENCE_LIST, 'FeaturetteName', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_cfg', 'SubscriberFeaturette.FeaturetteName',
                [], [],
                '''                enable featurette processing
                ''',
                'featurette_name',
                'Cisco-IOS-XR-iedge4710-cfg', False),
            ],
            'Cisco-IOS-XR-iedge4710-cfg',
            'subscriber-featurette',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-iedge4710-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_cfg',
        ),
    },
    'IedgeLicenseManager' : {
        'meta_info' : _MetaInfoClass('IedgeLicenseManager', REFERENCE_CLASS,
            '''iedge license manager''',
            False, 
            [
            _MetaInfoClassMember('session-limit', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('1', '200000')], [],
                '''                Session limit configured on linecard
                ''',
                'session_limit',
                'Cisco-IOS-XR-iedge4710-cfg', False),
            ],
            'Cisco-IOS-XR-iedge4710-cfg',
            'iedge-license-manager',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-iedge4710-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_cfg',
        ),
    },
    'SubManager.Location.Trace' : {
        'meta_info' : _MetaInfoClass('SubManager.Location.Trace', REFERENCE_CLASS,
            '''Subscriber manager trace''',
            False, 
            [
            _MetaInfoClassMember('trace-level', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('0', '4294967295')], [],
                '''                Subscriber manager trace level
                ''',
                'trace_level',
                'Cisco-IOS-XR-iedge4710-cfg', False),
            ],
            'Cisco-IOS-XR-iedge4710-cfg',
            'trace',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-iedge4710-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_cfg',
        ),
    },
    'SubManager.Location' : {
        'meta_info' : _MetaInfoClass('SubManager.Location', REFERENCE_LIST,
            '''Select location''',
            False, 
            [
            _MetaInfoClassMember('location1', ATTRIBUTE, 'str', 'xr:Cisco-ios-xr-string',
                None, None,
                [], [b'[\\w\\-\\.:,_@#%$\\+=\\|;]+'],
                '''                Specify location
                ''',
                'location1',
                'Cisco-IOS-XR-iedge4710-cfg', True),
            _MetaInfoClassMember('trace', REFERENCE_CLASS, 'Trace', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_cfg', 'SubManager.Location.Trace',
                [], [],
                '''                Subscriber manager trace
                ''',
                'trace',
                'Cisco-IOS-XR-iedge4710-cfg', False),
            _MetaInfoClassMember('history', ATTRIBUTE, 'Empty', 'empty',
                None, None,
                [], [],
                '''                Disable history for subscriber manager
                ''',
                'history',
                'Cisco-IOS-XR-iedge4710-cfg', False),
            ],
            'Cisco-IOS-XR-iedge4710-cfg',
            'location',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-iedge4710-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_cfg',
        ),
    },
    'SubManager' : {
        'meta_info' : _MetaInfoClass('SubManager', REFERENCE_CLASS,
            '''sub manager''',
            False, 
            [
            _MetaInfoClassMember('location', REFERENCE_LIST, 'Location', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_cfg', 'SubManager.Location',
                [], [],
                '''                Select location
                ''',
                'location',
                'Cisco-IOS-XR-iedge4710-cfg', False),
            ],
            'Cisco-IOS-XR-iedge4710-cfg',
            'sub-manager',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-iedge4710-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_cfg',
        ),
    },
}
_meta_table['SubscriberManager.Accounting.SendStop.SetupFailure']['meta_info'].parent =_meta_table['SubscriberManager.Accounting.SendStop']['meta_info']
_meta_table['SubscriberManager.Accounting.Interim.Variation']['meta_info'].parent =_meta_table['SubscriberManager.Accounting.Interim']['meta_info']
_meta_table['SubscriberManager.Accounting.SendStop']['meta_info'].parent =_meta_table['SubscriberManager.Accounting']['meta_info']
_meta_table['SubscriberManager.Accounting.Interim']['meta_info'].parent =_meta_table['SubscriberManager.Accounting']['meta_info']
_meta_table['SubscriberManager.Accounting']['meta_info'].parent =_meta_table['SubscriberManager']['meta_info']
_meta_table['SubscriberManager.Srg']['meta_info'].parent =_meta_table['SubscriberManager']['meta_info']
_meta_table['SubscriberFeaturette.FeaturetteName']['meta_info'].parent =_meta_table['SubscriberFeaturette']['meta_info']
_meta_table['SubManager.Location.Trace']['meta_info'].parent =_meta_table['SubManager.Location']['meta_info']
_meta_table['SubManager.Location']['meta_info'].parent =_meta_table['SubManager']['meta_info']
