
'''
This is auto-generated file,
which includes metadata for module Cisco_IOS_XR_l2_eth_infra_datatypes
'''

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_LIST, REFERENCE_LEAFLIST, REFERENCE_BITS, REFERENCE_UNION
from ydk._core._dm_meta_info import REFERENCE_CLASS, REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, ANYXML_CLASS
from ydk._core._importer import _yang_ns

_meta_table = {
    'VsMode' : _MetaInfoEnum('VsMode',
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2_eth_infra_datatypes', 'VsMode',
        '''Vs mode''',
        {
            'trunk':'trunk',
            'access':'access',
        }, 'Cisco-IOS-XR-l2-eth-infra-datatypes', _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-l2-eth-infra-datatypes']),
    'VlanTagOrCvp' : _MetaInfoEnum('VlanTagOrCvp',
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2_eth_infra_datatypes', 'VlanTagOrCvp',
        ''' ''',
        {
            'native-with-cvlan-preservation':'native_with_cvlan_preservation',
        }, 'Cisco-IOS-XR-l2-eth-infra-datatypes', _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-l2-eth-infra-datatypes']),
    'Vlan' : _MetaInfoEnum('Vlan',
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2_eth_infra_datatypes', 'Vlan',
        '''Vlan''',
        {
            'vlan-type-dot1ad':'vlan_type_dot1ad',
            'vlan-type-dot1q':'vlan_type_dot1q',
        }, 'Cisco-IOS-XR-l2-eth-infra-datatypes', _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-l2-eth-infra-datatypes']),
    'VlanTagOrNative' : _MetaInfoEnum('VlanTagOrNative',
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2_eth_infra_datatypes', 'VlanTagOrNative',
        ''' ''',
        {
            'native':'native',
            'native-with-cvlan-preservation':'native_with_cvlan_preservation',
        }, 'Cisco-IOS-XR-l2-eth-infra-datatypes', _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-l2-eth-infra-datatypes']),
    'VlanTagOrNull' : _MetaInfoEnum('VlanTagOrNull',
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2_eth_infra_datatypes', 'VlanTagOrNull',
        ''' ''',
        {
            'any':'any',
        }, 'Cisco-IOS-XR-l2-eth-infra-datatypes', _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-l2-eth-infra-datatypes']),
    'Rewrite' : _MetaInfoEnum('Rewrite',
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2_eth_infra_datatypes', 'Rewrite',
        '''Rewrite''',
        {
            'pop1':'pop1',
            'pop2':'pop2',
            'push1':'push1',
            'push2':'push2',
            'translate1to1':'translate1to1',
            'translate1to2':'translate1to2',
            'translate2to1':'translate2to1',
            'translate2to2':'translate2to2',
        }, 'Cisco-IOS-XR-l2-eth-infra-datatypes', _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-l2-eth-infra-datatypes']),
    'Match' : _MetaInfoEnum('Match',
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2_eth_infra_datatypes', 'Match',
        '''Match''',
        {
            'match-default':'match_default',
            'match-untagged':'match_untagged',
            'match-dot1q':'match_dot1q',
            'match-dot1ad':'match_dot1ad',
            'match-dot1q-priority':'match_dot1q_priority',
            'match-dot1ad-priority':'match_dot1ad_priority',
        }, 'Cisco-IOS-XR-l2-eth-infra-datatypes', _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-l2-eth-infra-datatypes']),
    'EthertypeMatch' : _MetaInfoEnum('EthertypeMatch',
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2_eth_infra_datatypes', 'EthertypeMatch',
        '''Ethertype match''',
        {
            'ppp-over-ethernet':'ppp_over_ethernet',
        }, 'Cisco-IOS-XR-l2-eth-infra-datatypes', _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-l2-eth-infra-datatypes']),
    'VlanTagOrAny' : _MetaInfoEnum('VlanTagOrAny',
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2_eth_infra_datatypes', 'VlanTagOrAny',
        ''' ''',
        {
            'any':'any',
        }, 'Cisco-IOS-XR-l2-eth-infra-datatypes', _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-l2-eth-infra-datatypes']),
}
