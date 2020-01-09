
'''
This is auto-generated file,
which includes metadata for module Cisco_IOS_XR_atm_common_datatypes
'''

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_LIST, REFERENCE_LEAFLIST, REFERENCE_BITS, REFERENCE_UNION
from ydk._core._dm_meta_info import REFERENCE_CLASS, REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, ANYXML_CLASS
from ydk._core._importer import _yang_ns

_meta_table = {
    'AtmVpShaping' : _MetaInfoEnum('AtmVpShaping',
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_atm_common_datatypes', 'AtmVpShaping',
        '''Atm vp shaping''',
        {
            'cbr':'cbr',
            'vbr-nrt':'vbr_nrt',
            'vbr-rt':'vbr_rt',
            'ubr':'ubr',
        }, 'Cisco-IOS-XR-atm-common-datatypes', _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-atm-common-datatypes']),
    'AtmPvcShaping' : _MetaInfoEnum('AtmPvcShaping',
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_atm_common_datatypes', 'AtmPvcShaping',
        '''Atm pvc shaping''',
        {
            'cbr':'cbr',
            'vbr-nrt':'vbr_nrt',
            'vbr-rt':'vbr_rt',
            'ubr':'ubr',
        }, 'Cisco-IOS-XR-atm-common-datatypes', _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-atm-common-datatypes']),
    'AtmPvcData' : _MetaInfoEnum('AtmPvcData',
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_atm_common_datatypes', 'AtmPvcData',
        '''Atm pvc data''',
        {
            'data':'data',
            'ilmi':'ilmi',
            'layer2':'layer2',
        }, 'Cisco-IOS-XR-atm-common-datatypes', _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-atm-common-datatypes']),
    'AtmPvcEncapsulation' : _MetaInfoEnum('AtmPvcEncapsulation',
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_atm_common_datatypes', 'AtmPvcEncapsulation',
        '''Atm pvc encapsulation''',
        {
            'snap':'snap',
            'vc-mux':'vc_mux',
            'nlpid':'nlpid',
            'aal0':'aal0',
            'aal5':'aal5',
        }, 'Cisco-IOS-XR-atm-common-datatypes', _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-atm-common-datatypes']),
}
