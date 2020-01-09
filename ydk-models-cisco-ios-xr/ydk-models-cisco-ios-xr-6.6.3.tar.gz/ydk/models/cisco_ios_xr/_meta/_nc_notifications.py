
'''
This is auto-generated file,
which includes metadata for module nc_notifications
'''

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_LIST, REFERENCE_LEAFLIST, REFERENCE_BITS, REFERENCE_UNION
from ydk._core._dm_meta_info import REFERENCE_CLASS, REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, ANYXML_CLASS
from ydk._core._importer import _yang_ns

_meta_table = {
    'Netconf.Streams.Stream' : {
        'meta_info' : _MetaInfoClass('Netconf.Streams.Stream', REFERENCE_LIST,
            '''Stream name, description and other information.''',
            False, 
            [
            _MetaInfoClassMember('name', ATTRIBUTE, 'str', 'ncEvent:streamNameType',
                None, None,
                [], [],
                '''                The name of the event stream. If this is the default
                NETCONF stream, this must have the value 'NETCONF'.
                ''',
                'name',
                'nc-notifications', True, is_config=False),
            _MetaInfoClassMember('description', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                A description of the event stream, including such
                information as the type of events that are sent over
                this stream.
                ''',
                'description',
                'nc-notifications', False, is_config=False, is_mandatory=True),
            _MetaInfoClassMember('replaySupport', ATTRIBUTE, 'bool', 'boolean',
                None, None,
                [], [],
                '''                A description of the event stream, including such
                information as the type of events that are sent over
                this stream.
                ''',
                'replaysupport',
                'nc-notifications', False, is_config=False, is_mandatory=True),
            _MetaInfoClassMember('replayLogCreationTime', ATTRIBUTE, 'str', 'yang:date-and-time',
                None, None,
                [], [b'\\d{4}-\\d{2}-\\d{2}T\\d{2}:\\d{2}:\\d{2}(\\.\\d+)?(Z|[\\+\\-]\\d{2}:\\d{2})'],
                '''                The timestamp of the creation of the log used to support
                the replay function on this stream. Note that this might
                be earlier then the earliest available notification in
                the log. This object is updated if the log resets for 
                some reason.  This object MUST be present if replay is
                supported.
                ''',
                'replaylogcreationtime',
                'nc-notifications', False, is_config=False),
            ],
            'nc-notifications',
            'stream',
            _yang_ns.NAMESPACE_LOOKUP['nc-notifications'],
            'ydk.models.cisco_ios_xr.nc_notifications',
            is_config=False,
        ),
    },
    'Netconf.Streams' : {
        'meta_info' : _MetaInfoClass('Netconf.Streams', REFERENCE_CLASS,
            '''The list of event streams supported by the system. When
a query is issued, the returned set of streams is 
determined based on user privileges.''',
            False, 
            [
            _MetaInfoClassMember('stream', REFERENCE_LIST, 'Stream', '',
                'ydk.models.cisco_ios_xr.nc_notifications', 'Netconf.Streams.Stream',
                [], [],
                '''                Stream name, description and other information.
                ''',
                'stream',
                'nc-notifications', False, min_elements=1, is_config=False),
            ],
            'nc-notifications',
            'streams',
            _yang_ns.NAMESPACE_LOOKUP['nc-notifications'],
            'ydk.models.cisco_ios_xr.nc_notifications',
            is_config=False,
        ),
    },
    'Netconf' : {
        'meta_info' : _MetaInfoClass('Netconf', REFERENCE_CLASS,
            '''Top-level element in the notification namespace''',
            False, 
            [
            _MetaInfoClassMember('streams', REFERENCE_CLASS, 'Streams', '',
                'ydk.models.cisco_ios_xr.nc_notifications', 'Netconf.Streams',
                [], [],
                '''                The list of event streams supported by the system. When
                a query is issued, the returned set of streams is 
                determined based on user privileges.
                ''',
                'streams',
                'nc-notifications', False, is_config=False),
            ],
            'nc-notifications',
            'netconf',
            _yang_ns.NAMESPACE_LOOKUP['nc-notifications'],
            'ydk.models.cisco_ios_xr.nc_notifications',
            is_config=False,
        ),
    },
}
_meta_table['Netconf.Streams.Stream']['meta_info'].parent =_meta_table['Netconf.Streams']['meta_info']
_meta_table['Netconf.Streams']['meta_info'].parent =_meta_table['Netconf']['meta_info']
