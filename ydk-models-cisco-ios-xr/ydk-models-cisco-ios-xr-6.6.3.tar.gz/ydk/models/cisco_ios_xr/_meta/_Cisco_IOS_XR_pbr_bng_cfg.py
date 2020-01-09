
'''
This is auto-generated file,
which includes metadata for module Cisco_IOS_XR_pbr_bng_cfg
'''

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_LIST, REFERENCE_LEAFLIST, REFERENCE_BITS, REFERENCE_UNION
from ydk._core._dm_meta_info import REFERENCE_CLASS, REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, ANYXML_CLASS
from ydk._core._importer import _yang_ns

_meta_table = {
    'BngPbrHttpEnrichmentParams' : _MetaInfoEnum('BngPbrHttpEnrichmentParams',
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_pbr_bng_cfg', 'BngPbrHttpEnrichmentParams',
        '''Bng pbr http enrichment params''',
        {
            'subscriber-mac':'subscriber_mac',
            'subscriber-ip':'subscriber_ip',
            'host-name':'host_name',
            'bng-identifier-interface':'bng_identifier_interface',
        }, 'Cisco-IOS-XR-pbr-bng-cfg', _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-pbr-bng-cfg']),
    'BngPbr.HttpEnrichment.Parameters' : {
        'meta_info' : _MetaInfoClass('BngPbr.HttpEnrichment.Parameters', REFERENCE_CLASS,
            '''HTTP Enrichment parameters''',
            False, 
            [
            _MetaInfoClassMember('arg1', REFERENCE_ENUM_CLASS, 'BngPbrHttpEnrichmentParams', 'Bng-pbr-http-enrichment-params',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_pbr_bng_cfg', 'BngPbrHttpEnrichmentParams',
                [], [],
                '''                first argument 
                ''',
                'arg1',
                'Cisco-IOS-XR-pbr-bng-cfg', False, is_mandatory=True),
            _MetaInfoClassMember('arg2', REFERENCE_ENUM_CLASS, 'BngPbrHttpEnrichmentParams', 'Bng-pbr-http-enrichment-params',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_pbr_bng_cfg', 'BngPbrHttpEnrichmentParams',
                [], [],
                '''                second argument 
                ''',
                'arg2',
                'Cisco-IOS-XR-pbr-bng-cfg', False),
            _MetaInfoClassMember('arg3', REFERENCE_ENUM_CLASS, 'BngPbrHttpEnrichmentParams', 'Bng-pbr-http-enrichment-params',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_pbr_bng_cfg', 'BngPbrHttpEnrichmentParams',
                [], [],
                '''                Third argument 
                ''',
                'arg3',
                'Cisco-IOS-XR-pbr-bng-cfg', False),
            _MetaInfoClassMember('arg4', REFERENCE_ENUM_CLASS, 'BngPbrHttpEnrichmentParams', 'Bng-pbr-http-enrichment-params',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_pbr_bng_cfg', 'BngPbrHttpEnrichmentParams',
                [], [],
                '''                Fourth argument 
                ''',
                'arg4',
                'Cisco-IOS-XR-pbr-bng-cfg', False),
            ],
            'Cisco-IOS-XR-pbr-bng-cfg',
            'parameters',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-pbr-bng-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_pbr_bng_cfg',
            is_presence=True,
        ),
    },
    'BngPbr.HttpEnrichment' : {
        'meta_info' : _MetaInfoClass('BngPbr.HttpEnrichment', REFERENCE_CLASS,
            '''HTTP Enrichment''',
            False, 
            [
            _MetaInfoClassMember('parameters', REFERENCE_CLASS, 'Parameters', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_pbr_bng_cfg', 'BngPbr.HttpEnrichment.Parameters',
                [], [],
                '''                HTTP Enrichment parameters
                ''',
                'parameters',
                'Cisco-IOS-XR-pbr-bng-cfg', False, is_presence=True),
            ],
            'Cisco-IOS-XR-pbr-bng-cfg',
            'http-enrichment',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-pbr-bng-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_pbr_bng_cfg',
        ),
    },
    'BngPbr' : {
        'meta_info' : _MetaInfoClass('BngPbr', REFERENCE_CLASS,
            '''Subscriber PBR configuration''',
            False, 
            [
            _MetaInfoClassMember('http-enrichment', REFERENCE_CLASS, 'HttpEnrichment', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_pbr_bng_cfg', 'BngPbr.HttpEnrichment',
                [], [],
                '''                HTTP Enrichment
                ''',
                'http_enrichment',
                'Cisco-IOS-XR-pbr-bng-cfg', False),
            _MetaInfoClassMember('bng-interface', ATTRIBUTE, 'str', 'xr:Interface-name',
                None, None,
                [], [b'[a-zA-Z0-9._/-]+'],
                '''                Interface for source address
                ''',
                'bng_interface',
                'Cisco-IOS-XR-pbr-bng-cfg', False),
            ],
            'Cisco-IOS-XR-pbr-bng-cfg',
            'bng-pbr',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-pbr-bng-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_pbr_bng_cfg',
        ),
    },
}
_meta_table['BngPbr.HttpEnrichment.Parameters']['meta_info'].parent =_meta_table['BngPbr.HttpEnrichment']['meta_info']
_meta_table['BngPbr.HttpEnrichment']['meta_info'].parent =_meta_table['BngPbr']['meta_info']
