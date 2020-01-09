
'''
This is auto-generated file,
which includes metadata for module Cisco_IOS_XR_aaa_aaacore_cfg
'''

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_LIST, REFERENCE_LEAFLIST, REFERENCE_BITS, REFERENCE_UNION
from ydk._core._dm_meta_info import REFERENCE_CLASS, REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, ANYXML_CLASS
from ydk._core._importer import _yang_ns

_meta_table = {
    'NasPortValue' : _MetaInfoEnum('NasPortValue',
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_aaacore_cfg', 'NasPortValue',
        '''Nas port value''',
        {
            'async':'async_',
            'sync':'sync',
            'isdn':'isdn',
            'isdn-async-v120':'isdn_async_v120',
            'isdn-async-v110':'isdn_async_v110',
            'virtual':'virtual',
            'isdn-async-piafs':'isdn_async_piafs',
            'x75':'x75',
            'ethernet':'ethernet',
            'pppoa':'pppoa',
            'pppoeoa':'pppoeoa',
            'pppoeoe':'pppoeoe',
            'pppoeovlan':'pppoeovlan',
            'pppoeoqinq':'pppoeoqinq',
            'virtual-pppoeoe':'virtual_pppoeoe',
            'virtual-pppoeovlan':'virtual_pppoeovlan',
            'virtual-pppoeoqinaq':'virtual_pppoeoqinaq',
            'ipsec':'ipsec',
            'ipoeoe':'ipoeoe',
            'ipoeovlan':'ipoeovlan',
            'ipoeoqinq':'ipoeoqinq',
            'virtual-ipoeoe':'virtual_ipoeoe',
            'virtual-ipoeovlan':'virtual_ipoeovlan',
            'virtual-ipoeoqinq':'virtual_ipoeoqinq',
        }, 'Cisco-IOS-XR-aaa-aaacore-cfg', _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-aaa-aaacore-cfg']),
    'AaaServiceAccounting' : _MetaInfoEnum('AaaServiceAccounting',
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_aaacore_cfg', 'AaaServiceAccounting',
        '''Aaa service accounting''',
        {
            'none':'none',
            'extended':'extended',
            'brief':'brief',
        }, 'Cisco-IOS-XR-aaa-aaacore-cfg', _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-aaa-aaacore-cfg']),
}
