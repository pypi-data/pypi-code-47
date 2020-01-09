
'''
This is auto-generated file,
which includes metadata for module notifications
'''

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_LIST, REFERENCE_LEAFLIST, REFERENCE_BITS, REFERENCE_UNION
from ydk._core._dm_meta_info import REFERENCE_CLASS, REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, ANYXML_CLASS
from ydk._core._importer import _yang_ns

_meta_table = {
    'CreateSubscription.Input' : {
        'meta_info' : _MetaInfoClass('CreateSubscription.Input', REFERENCE_CLASS,
            ''' ''',
            False, 
            [
            _MetaInfoClassMember('stream', ATTRIBUTE, 'str', 'streamNameType',
                None, None,
                [], [],
                '''                An optional parameter that indicates which stream of 
                events is of interest. If not present, then events in the
                default NETCONF stream will be sent.
                ''',
                'stream',
                'notifications', False, default_value="'NETCONF'"),
            _MetaInfoClassMember('filter', ANYXML_CLASS, 'object', '',
                None, None,
                [], [],
                '''                An optional parameter that indicates which subset of all
                possible events is of interest. The format of this
                parameter is the same as that of the filter parameter
                in the NETCONF protocol operations. If not present,
                all events not precluded by other parameters will 
                be sent.
                ''',
                'filter',
                'notifications', False),
            _MetaInfoClassMember('startTime', ATTRIBUTE, 'str', 'yang:date-and-time',
                None, None,
                [], [b'\\d{4}-\\d{2}-\\d{2}T\\d{2}:\\d{2}:\\d{2}(\\.\\d+)?(Z|[\\+\\-]\\d{2}:\\d{2})'],
                '''                A parameter used to trigger the replay feature and
                indicates that the replay should start at the time
                specified. If start time is not present, this is not a
                replay subscription.
                ''',
                'starttime',
                'notifications', False),
            _MetaInfoClassMember('stopTime', ATTRIBUTE, 'str', 'yang:date-and-time',
                None, None,
                [], [b'\\d{4}-\\d{2}-\\d{2}T\\d{2}:\\d{2}:\\d{2}(\\.\\d+)?(Z|[\\+\\-]\\d{2}:\\d{2})'],
                '''                An optional parameter used with the optional replay
                feature to indicate the newest notifications of
                interest. If stop time is not present, the notifications
                will continue until the subscription is terminated.
                Must be used with startTime.
                ''',
                'stoptime',
                'notifications', False),
            ],
            'notifications',
            'input',
            _yang_ns.NAMESPACE_LOOKUP['notifications'],
            'ydk.models.cisco_ios_xr.notifications',
        ),
    },
    'CreateSubscription' : {
        'meta_info' : _MetaInfoClass('CreateSubscription', REFERENCE_CLASS,
            '''The command to create a notification subscription. It
takes as argument the name of the notification stream
and filter. Both of those options limit the content of
the subscription. In addition, there are two time-related
parameters, startTime and stopTime, which can be used to 
select the time interval of interest to the notification
replay feature.''',
            False, 
            [
            _MetaInfoClassMember('input', REFERENCE_CLASS, 'Input', '',
                'ydk.models.cisco_ios_xr.notifications', 'CreateSubscription.Input',
                [], [],
                '''                ''',
                'input',
                'notifications', False),
            ],
            'notifications',
            'create-subscription',
            _yang_ns.NAMESPACE_LOOKUP['notifications'],
            'ydk.models.cisco_ios_xr.notifications',
        ),
    },
}
_meta_table['CreateSubscription.Input']['meta_info'].parent =_meta_table['CreateSubscription']['meta_info']
