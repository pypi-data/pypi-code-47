
'''
This is auto-generated file,
which includes metadata for module Cisco_IOS_XR_infra_statsd_cfg
'''

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_LIST, REFERENCE_LEAFLIST, REFERENCE_BITS, REFERENCE_UNION
from ydk._core._dm_meta_info import REFERENCE_CLASS, REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, ANYXML_CLASS
from ydk._core._importer import _yang_ns

_meta_table = {
    'Statistics.Period.ServiceAccounting' : {
        'meta_info' : _MetaInfoClass('Statistics.Period.ServiceAccounting', REFERENCE_CLASS,
            '''Collection polling period for service
accounting collectors''',
            False, 
            [
            _MetaInfoClassMember('polling-period', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('30', '3600')], [],
                '''                Collection polling period for service
                accounting collectors
                ''',
                'polling_period',
                'Cisco-IOS-XR-infra-statsd-cfg', False, has_must=True),
            _MetaInfoClassMember('polling-disable', ATTRIBUTE, 'Empty', 'empty',
                None, None,
                [], [],
                '''                Disable periodic statistics polling for
                service accounting collectors
                ''',
                'polling_disable',
                'Cisco-IOS-XR-infra-statsd-cfg', False, has_must=True),
            ],
            'Cisco-IOS-XR-infra-statsd-cfg',
            'service-accounting',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-infra-statsd-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_statsd_cfg',
        ),
    },
    'Statistics.Period' : {
        'meta_info' : _MetaInfoClass('Statistics.Period', REFERENCE_CLASS,
            '''Collection period for statistics polling''',
            False, 
            [
            _MetaInfoClassMember('service-accounting', REFERENCE_CLASS, 'ServiceAccounting', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_statsd_cfg', 'Statistics.Period.ServiceAccounting',
                [], [],
                '''                Collection polling period for service
                accounting collectors
                ''',
                'service_accounting',
                'Cisco-IOS-XR-infra-statsd-cfg', False),
            ],
            'Cisco-IOS-XR-infra-statsd-cfg',
            'period',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-infra-statsd-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_statsd_cfg',
        ),
    },
    'Statistics' : {
        'meta_info' : _MetaInfoClass('Statistics', REFERENCE_CLASS,
            '''Global statistics configuration''',
            False, 
            [
            _MetaInfoClassMember('period', REFERENCE_CLASS, 'Period', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_statsd_cfg', 'Statistics.Period',
                [], [],
                '''                Collection period for statistics polling
                ''',
                'period',
                'Cisco-IOS-XR-infra-statsd-cfg', False),
            ],
            'Cisco-IOS-XR-infra-statsd-cfg',
            'statistics',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-infra-statsd-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_statsd_cfg',
        ),
    },
}
_meta_table['Statistics.Period.ServiceAccounting']['meta_info'].parent =_meta_table['Statistics.Period']['meta_info']
_meta_table['Statistics.Period']['meta_info'].parent =_meta_table['Statistics']['meta_info']
