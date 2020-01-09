
'''
This is auto-generated file,
which includes metadata for module Cisco_IOS_XR_accounting_cfg
'''

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_LIST, REFERENCE_LEAFLIST, REFERENCE_BITS, REFERENCE_UNION
from ydk._core._dm_meta_info import REFERENCE_CLASS, REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, ANYXML_CLASS
from ydk._core._importer import _yang_ns

_meta_table = {
    'Accounting.Interfaces.Mpls' : {
        'meta_info' : _MetaInfoClass('Accounting.Interfaces.Mpls', REFERENCE_CLASS,
            '''Interfaces MPLS configuration''',
            False, 
            [
            _MetaInfoClassMember('enable', ATTRIBUTE, 'Empty', 'empty',
                None, None,
                [], [],
                '''                Enable accounting on MPLS
                ''',
                'enable',
                'Cisco-IOS-XR-accounting-cfg', False),
            _MetaInfoClassMember('enable-v4rsvpte', ATTRIBUTE, 'Empty', 'empty',
                None, None,
                [], [],
                '''                Enable accounting on MPLS IPv4 RSVP TE
                ''',
                'enable_v4rsvpte',
                'Cisco-IOS-XR-accounting-cfg', False),
            ],
            'Cisco-IOS-XR-accounting-cfg',
            'mpls',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-accounting-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_accounting_cfg',
        ),
    },
    'Accounting.Interfaces.SegmentRouting' : {
        'meta_info' : _MetaInfoClass('Accounting.Interfaces.SegmentRouting', REFERENCE_CLASS,
            '''Interfaces Segment Routing configuration''',
            False, 
            [
            _MetaInfoClassMember('enable', ATTRIBUTE, 'Empty', 'empty',
                None, None,
                [], [],
                '''                Enable accounting on Segment Routing
                ''',
                'enable',
                'Cisco-IOS-XR-accounting-cfg', False),
            _MetaInfoClassMember('enable-mplsv4', ATTRIBUTE, 'Empty', 'empty',
                None, None,
                [], [],
                '''                Enable accounting on Segment Routing MPLS IPv4
                ''',
                'enable_mplsv4',
                'Cisco-IOS-XR-accounting-cfg', False),
            _MetaInfoClassMember('enable-mplsv6', ATTRIBUTE, 'Empty', 'empty',
                None, None,
                [], [],
                '''                Enable accounting on Segment Routing MPLS IPv6
                ''',
                'enable_mplsv6',
                'Cisco-IOS-XR-accounting-cfg', False),
            ],
            'Cisco-IOS-XR-accounting-cfg',
            'segment-routing',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-accounting-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_accounting_cfg',
        ),
    },
    'Accounting.Interfaces' : {
        'meta_info' : _MetaInfoClass('Accounting.Interfaces', REFERENCE_CLASS,
            '''Interfaces configuration''',
            False, 
            [
            _MetaInfoClassMember('mpls', REFERENCE_CLASS, 'Mpls', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_accounting_cfg', 'Accounting.Interfaces.Mpls',
                [], [],
                '''                Interfaces MPLS configuration
                ''',
                'mpls',
                'Cisco-IOS-XR-accounting-cfg', False),
            _MetaInfoClassMember('segment-routing', REFERENCE_CLASS, 'SegmentRouting', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_accounting_cfg', 'Accounting.Interfaces.SegmentRouting',
                [], [],
                '''                Interfaces Segment Routing configuration
                ''',
                'segment_routing',
                'Cisco-IOS-XR-accounting-cfg', False),
            _MetaInfoClassMember('enable', ATTRIBUTE, 'Empty', 'empty',
                None, None,
                [], [],
                '''                Enable accounting on Interfaces
                ''',
                'enable',
                'Cisco-IOS-XR-accounting-cfg', False),
            ],
            'Cisco-IOS-XR-accounting-cfg',
            'interfaces',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-accounting-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_accounting_cfg',
        ),
    },
    'Accounting' : {
        'meta_info' : _MetaInfoClass('Accounting', REFERENCE_CLASS,
            '''Global Accounting configuration commands''',
            False, 
            [
            _MetaInfoClassMember('interfaces', REFERENCE_CLASS, 'Interfaces', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_accounting_cfg', 'Accounting.Interfaces',
                [], [],
                '''                Interfaces configuration
                ''',
                'interfaces',
                'Cisco-IOS-XR-accounting-cfg', False),
            _MetaInfoClassMember('enable', ATTRIBUTE, 'Empty', 'empty',
                None, None,
                [], [],
                '''                Enable Accounting
                ''',
                'enable',
                'Cisco-IOS-XR-accounting-cfg', False),
            ],
            'Cisco-IOS-XR-accounting-cfg',
            'accounting',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-accounting-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_accounting_cfg',
        ),
    },
}
_meta_table['Accounting.Interfaces.Mpls']['meta_info'].parent =_meta_table['Accounting.Interfaces']['meta_info']
_meta_table['Accounting.Interfaces.SegmentRouting']['meta_info'].parent =_meta_table['Accounting.Interfaces']['meta_info']
_meta_table['Accounting.Interfaces']['meta_info'].parent =_meta_table['Accounting']['meta_info']
