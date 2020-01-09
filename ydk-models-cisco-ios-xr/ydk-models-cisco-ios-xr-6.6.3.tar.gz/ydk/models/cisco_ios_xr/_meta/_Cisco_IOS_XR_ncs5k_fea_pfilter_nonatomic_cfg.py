
'''
This is auto-generated file,
which includes metadata for module Cisco_IOS_XR_ncs5k_fea_pfilter_nonatomic_cfg
'''

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_LIST, REFERENCE_LEAFLIST, REFERENCE_BITS, REFERENCE_UNION
from ydk._core._dm_meta_info import REFERENCE_CLASS, REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, ANYXML_CLASS
from ydk._core._importer import _yang_ns

_meta_table = {
    'AtomicDisableDfltActn' : _MetaInfoEnum('AtomicDisableDfltActn',
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5k_fea_pfilter_nonatomic_cfg', 'AtomicDisableDfltActn',
        '''Atomic disable dflt actn''',
        {
            'default-action-deny':'default_action_deny',
            'default-action-permit':'default_action_permit',
        }, 'Cisco-IOS-XR-ncs5k-fea-pfilter-nonatomic-cfg', _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-ncs5k-fea-pfilter-nonatomic-cfg']),
    'Hardware.AccessList' : {
        'meta_info' : _MetaInfoClass('Hardware.AccessList', REFERENCE_CLASS,
            '''Access-list option''',
            False, 
            [
            _MetaInfoClassMember('atomic-disable', REFERENCE_ENUM_CLASS, 'AtomicDisableDfltActn', 'Atomic-disable-dflt-actn',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5k_fea_pfilter_nonatomic_cfg', 'AtomicDisableDfltActn',
                [], [],
                '''                Specify Option for Atomic disable
                ''',
                'atomic_disable',
                'Cisco-IOS-XR-ncs5k-fea-pfilter-nonatomic-cfg', False),
            ],
            'Cisco-IOS-XR-ncs5k-fea-pfilter-nonatomic-cfg',
            'access-list',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-ncs5k-fea-pfilter-nonatomic-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5k_fea_pfilter_nonatomic_cfg',
        ),
    },
    'Hardware' : {
        'meta_info' : _MetaInfoClass('Hardware', REFERENCE_CLASS,
            '''Hardware''',
            False, 
            [
            _MetaInfoClassMember('access-list', REFERENCE_CLASS, 'AccessList', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5k_fea_pfilter_nonatomic_cfg', 'Hardware.AccessList',
                [], [],
                '''                Access-list option
                ''',
                'access_list',
                'Cisco-IOS-XR-ncs5k-fea-pfilter-nonatomic-cfg', False),
            ],
            'Cisco-IOS-XR-ncs5k-fea-pfilter-nonatomic-cfg',
            'hardware',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-ncs5k-fea-pfilter-nonatomic-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5k_fea_pfilter_nonatomic_cfg',
        ),
    },
}
_meta_table['Hardware.AccessList']['meta_info'].parent =_meta_table['Hardware']['meta_info']
