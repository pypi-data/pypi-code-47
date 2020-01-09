
'''
This is auto-generated file,
which includes metadata for module Cisco_IOS_XR_mpls_ldp_cfg_datatypes
'''

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_LIST, REFERENCE_LEAFLIST, REFERENCE_BITS, REFERENCE_UNION
from ydk._core._dm_meta_info import REFERENCE_CLASS, REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, ANYXML_CLASS
from ydk._core._importer import _yang_ns

_meta_table = {
    'MplsLdpNbrPassword' : _MetaInfoEnum('MplsLdpNbrPassword',
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_ldp_cfg_datatypes', 'MplsLdpNbrPassword',
        '''Mpls ldp nbr password''',
        {
            'disable':'disable',
            'specified':'specified',
        }, 'Cisco-IOS-XR-mpls-ldp-cfg-datatypes', _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-mpls-ldp-cfg-datatypes']),
    'MplsLdpDownstreamOnDemand' : _MetaInfoEnum('MplsLdpDownstreamOnDemand',
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_ldp_cfg_datatypes', 'MplsLdpDownstreamOnDemand',
        '''Mpls ldp downstream on demand''',
        {
            'peer-acl':'peer_acl',
        }, 'Cisco-IOS-XR-mpls-ldp-cfg-datatypes', _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-mpls-ldp-cfg-datatypes']),
    'MplsLdpRouterId' : _MetaInfoEnum('MplsLdpRouterId',
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_ldp_cfg_datatypes', 'MplsLdpRouterId',
        '''Mpls ldp router id''',
        {
            'address':'address',
        }, 'Cisco-IOS-XR-mpls-ldp-cfg-datatypes', _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-mpls-ldp-cfg-datatypes']),
    'MplsLdpafName' : _MetaInfoEnum('MplsLdpafName',
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_ldp_cfg_datatypes', 'MplsLdpafName',
        '''Mpls ldpaf name''',
        {
            'ipv4':'ipv4',
            'ipv6':'ipv6',
        }, 'Cisco-IOS-XR-mpls-ldp-cfg-datatypes', _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-mpls-ldp-cfg-datatypes']),
    'MplsLdpSessionProtection' : _MetaInfoEnum('MplsLdpSessionProtection',
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_ldp_cfg_datatypes', 'MplsLdpSessionProtection',
        '''Mpls ldp session protection''',
        {
            'all':'all',
            'for':'for_',
            'all-with-duration':'all_with_duration',
            'for-with-duration':'for_with_duration',
            'all-with-forever':'all_with_forever',
            'for-with-forever':'for_with_forever',
        }, 'Cisco-IOS-XR-mpls-ldp-cfg-datatypes', _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-mpls-ldp-cfg-datatypes']),
}
