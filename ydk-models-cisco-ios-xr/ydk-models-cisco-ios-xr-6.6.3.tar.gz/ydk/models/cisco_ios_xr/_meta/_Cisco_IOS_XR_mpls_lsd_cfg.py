
'''
This is auto-generated file,
which includes metadata for module Cisco_IOS_XR_mpls_lsd_cfg
'''

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_LIST, REFERENCE_LEAFLIST, REFERENCE_BITS, REFERENCE_UNION
from ydk._core._dm_meta_info import REFERENCE_CLASS, REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, ANYXML_CLASS
from ydk._core._importer import _yang_ns

_meta_table = {
    'LabelBlock' : _MetaInfoEnum('LabelBlock',
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_lsd_cfg', 'LabelBlock',
        '''Label block''',
        {
            'cbf':'cbf',
        }, 'Cisco-IOS-XR-mpls-lsd-cfg', _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-mpls-lsd-cfg']),
    'LabelRange' : _MetaInfoEnum('LabelRange',
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_lsd_cfg', 'LabelRange',
        '''Label range''',
        {
            'lower-upper':'lower_upper',
            'lower-size':'lower_size',
        }, 'Cisco-IOS-XR-mpls-lsd-cfg', _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-mpls-lsd-cfg']),
    'MplsIpTtlPropagateDisable' : _MetaInfoEnum('MplsIpTtlPropagateDisable',
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_lsd_cfg', 'MplsIpTtlPropagateDisable',
        '''Mpls ip ttl propagate disable''',
        {
            'all':'all',
            'forward':'forward',
            'local':'local',
        }, 'Cisco-IOS-XR-mpls-lsd-cfg', _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-mpls-lsd-cfg']),
    'MplsLsd.Ipv6' : {
        'meta_info' : _MetaInfoClass('MplsLsd.Ipv6', REFERENCE_CLASS,
            '''Configure IPv6 parameters''',
            False, 
            [
            _MetaInfoClassMember('ttl-expiration-pop', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('1', '10')], [],
                '''                Number of labels to pop upon MPLS IP TTL expiry
                ''',
                'ttl_expiration_pop',
                'Cisco-IOS-XR-mpls-lsd-cfg', False),
            ],
            'Cisco-IOS-XR-mpls-lsd-cfg',
            'ipv6',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-mpls-lsd-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_lsd_cfg',
        ),
    },
    'MplsLsd.Ipv4' : {
        'meta_info' : _MetaInfoClass('MplsLsd.Ipv4', REFERENCE_CLASS,
            '''Configure IPv4 parameters''',
            False, 
            [
            _MetaInfoClassMember('ttl-expiration-pop', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('1', '10')], [],
                '''                Number of labels to pop upon MPLS IP TTL expiry
                ''',
                'ttl_expiration_pop',
                'Cisco-IOS-XR-mpls-lsd-cfg', False),
            ],
            'Cisco-IOS-XR-mpls-lsd-cfg',
            'ipv4',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-mpls-lsd-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_lsd_cfg',
        ),
    },
    'MplsLsd.LabelDatabases.LabelDatabase.LabelRange' : {
        'meta_info' : _MetaInfoClass('MplsLsd.LabelDatabases.LabelDatabase.LabelRange', REFERENCE_CLASS,
            '''Label range''',
            False, 
            [
            _MetaInfoClassMember('minvalue', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('16000', '1048575')], [],
                '''                Minimum label value
                ''',
                'minvalue',
                'Cisco-IOS-XR-mpls-lsd-cfg', False),
            _MetaInfoClassMember('max-value', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('16000', '1048575')], [],
                '''                Maximum label value
                ''',
                'max_value',
                'Cisco-IOS-XR-mpls-lsd-cfg', False),
            _MetaInfoClassMember('min-static-value', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('0', '1048575')], [],
                '''                Minimum static label value
                ''',
                'min_static_value',
                'Cisco-IOS-XR-mpls-lsd-cfg', False),
            _MetaInfoClassMember('max-static-value', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('0', '1048575')], [],
                '''                Maximum static label value
                ''',
                'max_static_value',
                'Cisco-IOS-XR-mpls-lsd-cfg', False),
            ],
            'Cisco-IOS-XR-mpls-lsd-cfg',
            'label-range',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-mpls-lsd-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_lsd_cfg',
        ),
    },
    'MplsLsd.LabelDatabases.LabelDatabase.LabelBlocks.LabelBlock' : {
        'meta_info' : _MetaInfoClass('MplsLsd.LabelDatabases.LabelDatabase.LabelBlocks.LabelBlock', REFERENCE_LIST,
            '''Label block''',
            False, 
            [
            _MetaInfoClassMember('block-name', ATTRIBUTE, 'str', 'xr:Cisco-ios-xr-string',
                None, None,
                [], [b'[\\w\\-\\.:,_@#%$\\+=\\|;]+'],
                '''                Label block identifier
                ''',
                'block_name',
                'Cisco-IOS-XR-mpls-lsd-cfg', True),
            _MetaInfoClassMember('block-type', REFERENCE_ENUM_CLASS, 'LabelBlock', 'Label-block',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_lsd_cfg', 'LabelBlock',
                [], [],
                '''                Label block type
                ''',
                'block_type',
                'Cisco-IOS-XR-mpls-lsd-cfg', False, default_value='Cisco_IOS_XR_mpls_lsd_cfg.LabelBlock.cbf'),
            _MetaInfoClassMember('range-type', REFERENCE_ENUM_CLASS, 'LabelRange', 'Label-range',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_lsd_cfg', 'LabelRange',
                [], [],
                '''                Label range type
                ''',
                'range_type',
                'Cisco-IOS-XR-mpls-lsd-cfg', False, default_value='Cisco_IOS_XR_mpls_lsd_cfg.LabelRange.lower_upper'),
            _MetaInfoClassMember('lower-bound', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('16000', '1048575')], [],
                '''                Lower bound of block
                ''',
                'lower_bound',
                'Cisco-IOS-XR-mpls-lsd-cfg', False, default_value="16000"),
            _MetaInfoClassMember('upper-bound', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('16000', '1048575')], [],
                '''                Upper bound of block
                ''',
                'upper_bound',
                'Cisco-IOS-XR-mpls-lsd-cfg', False, default_value="16000", has_when=True),
            _MetaInfoClassMember('block-size', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('1', '1032576')], [],
                '''                Size of block
                ''',
                'block_size',
                'Cisco-IOS-XR-mpls-lsd-cfg', False, default_value="1", has_when=True),
            _MetaInfoClassMember('client-instance-name', ATTRIBUTE, 'str', 'Label-block-client-name',
                None, None,
                [(1, 48)], [],
                '''                Client instance name
                ''',
                'client_instance_name',
                'Cisco-IOS-XR-mpls-lsd-cfg', False, default_value="'any'"),
            ],
            'Cisco-IOS-XR-mpls-lsd-cfg',
            'label-block',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-mpls-lsd-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_lsd_cfg',
        ),
    },
    'MplsLsd.LabelDatabases.LabelDatabase.LabelBlocks' : {
        'meta_info' : _MetaInfoClass('MplsLsd.LabelDatabases.LabelDatabase.LabelBlocks', REFERENCE_CLASS,
            '''A label blocks database''',
            False, 
            [
            _MetaInfoClassMember('label-block', REFERENCE_LIST, 'LabelBlock', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_lsd_cfg', 'MplsLsd.LabelDatabases.LabelDatabase.LabelBlocks.LabelBlock',
                [], [],
                '''                Label block
                ''',
                'label_block',
                'Cisco-IOS-XR-mpls-lsd-cfg', False),
            ],
            'Cisco-IOS-XR-mpls-lsd-cfg',
            'label-blocks',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-mpls-lsd-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_lsd_cfg',
        ),
    },
    'MplsLsd.LabelDatabases.LabelDatabase' : {
        'meta_info' : _MetaInfoClass('MplsLsd.LabelDatabases.LabelDatabase', REFERENCE_LIST,
            '''A label database''',
            False, 
            [
            _MetaInfoClassMember('label-database-id', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('0', '0')], [],
                '''                Label database identifier
                ''',
                'label_database_id',
                'Cisco-IOS-XR-mpls-lsd-cfg', True),
            _MetaInfoClassMember('label-range', REFERENCE_CLASS, 'LabelRange', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_lsd_cfg', 'MplsLsd.LabelDatabases.LabelDatabase.LabelRange',
                [], [],
                '''                Label range
                ''',
                'label_range',
                'Cisco-IOS-XR-mpls-lsd-cfg', False),
            _MetaInfoClassMember('label-blocks', REFERENCE_CLASS, 'LabelBlocks', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_lsd_cfg', 'MplsLsd.LabelDatabases.LabelDatabase.LabelBlocks',
                [], [],
                '''                A label blocks database
                ''',
                'label_blocks',
                'Cisco-IOS-XR-mpls-lsd-cfg', False),
            ],
            'Cisco-IOS-XR-mpls-lsd-cfg',
            'label-database',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-mpls-lsd-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_lsd_cfg',
        ),
    },
    'MplsLsd.LabelDatabases' : {
        'meta_info' : _MetaInfoClass('MplsLsd.LabelDatabases', REFERENCE_CLASS,
            '''Table of label databases''',
            False, 
            [
            _MetaInfoClassMember('label-database', REFERENCE_LIST, 'LabelDatabase', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_lsd_cfg', 'MplsLsd.LabelDatabases.LabelDatabase',
                [], [],
                '''                A label database
                ''',
                'label_database',
                'Cisco-IOS-XR-mpls-lsd-cfg', False),
            ],
            'Cisco-IOS-XR-mpls-lsd-cfg',
            'label-databases',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-mpls-lsd-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_lsd_cfg',
        ),
    },
    'MplsLsd' : {
        'meta_info' : _MetaInfoClass('MplsLsd', REFERENCE_CLASS,
            '''MPLS LSD configuration data''',
            False, 
            [
            _MetaInfoClassMember('ipv6', REFERENCE_CLASS, 'Ipv6', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_lsd_cfg', 'MplsLsd.Ipv6',
                [], [],
                '''                Configure IPv6 parameters
                ''',
                'ipv6',
                'Cisco-IOS-XR-mpls-lsd-cfg', False),
            _MetaInfoClassMember('ipv4', REFERENCE_CLASS, 'Ipv4', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_lsd_cfg', 'MplsLsd.Ipv4',
                [], [],
                '''                Configure IPv4 parameters
                ''',
                'ipv4',
                'Cisco-IOS-XR-mpls-lsd-cfg', False),
            _MetaInfoClassMember('label-databases', REFERENCE_CLASS, 'LabelDatabases', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_lsd_cfg', 'MplsLsd.LabelDatabases',
                [], [],
                '''                Table of label databases
                ''',
                'label_databases',
                'Cisco-IOS-XR-mpls-lsd-cfg', False),
            _MetaInfoClassMember('ltrace-multiplier', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('2', '5')], [],
                '''                Multiply the MPLS LSD Ltrace buffer length
                ''',
                'ltrace_multiplier',
                'Cisco-IOS-XR-mpls-lsd-cfg', False),
            _MetaInfoClassMember('app-reg-delay-disable', ATTRIBUTE, 'Empty', 'empty',
                None, None,
                [], [],
                '''                Disable LSD application reg delay
                ''',
                'app_reg_delay_disable',
                'Cisco-IOS-XR-mpls-lsd-cfg', False),
            _MetaInfoClassMember('mpls-entropy-label', ATTRIBUTE, 'Empty', 'empty',
                None, None,
                [], [],
                '''                Enable MPLS Entropy Label
                ''',
                'mpls_entropy_label',
                'Cisco-IOS-XR-mpls-lsd-cfg', False),
            _MetaInfoClassMember('mpls-ip-ttl-propagate-disable', REFERENCE_ENUM_CLASS, 'MplsIpTtlPropagateDisable', 'Mpls-ip-ttl-propagate-disable',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_lsd_cfg', 'MplsIpTtlPropagateDisable',
                [], [],
                '''                Disable Propagation of IP TTL onto the label
                stack
                ''',
                'mpls_ip_ttl_propagate_disable',
                'Cisco-IOS-XR-mpls-lsd-cfg', False),
            ],
            'Cisco-IOS-XR-mpls-lsd-cfg',
            'mpls-lsd',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-mpls-lsd-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_lsd_cfg',
        ),
    },
}
_meta_table['MplsLsd.LabelDatabases.LabelDatabase.LabelBlocks.LabelBlock']['meta_info'].parent =_meta_table['MplsLsd.LabelDatabases.LabelDatabase.LabelBlocks']['meta_info']
_meta_table['MplsLsd.LabelDatabases.LabelDatabase.LabelRange']['meta_info'].parent =_meta_table['MplsLsd.LabelDatabases.LabelDatabase']['meta_info']
_meta_table['MplsLsd.LabelDatabases.LabelDatabase.LabelBlocks']['meta_info'].parent =_meta_table['MplsLsd.LabelDatabases.LabelDatabase']['meta_info']
_meta_table['MplsLsd.LabelDatabases.LabelDatabase']['meta_info'].parent =_meta_table['MplsLsd.LabelDatabases']['meta_info']
_meta_table['MplsLsd.Ipv6']['meta_info'].parent =_meta_table['MplsLsd']['meta_info']
_meta_table['MplsLsd.Ipv4']['meta_info'].parent =_meta_table['MplsLsd']['meta_info']
_meta_table['MplsLsd.LabelDatabases']['meta_info'].parent =_meta_table['MplsLsd']['meta_info']
