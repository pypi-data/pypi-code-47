
'''
This is auto-generated file,
which includes metadata for module Cisco_IOS_XR_infra_infra_cfg
'''

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_LIST, REFERENCE_LEAFLIST, REFERENCE_BITS, REFERENCE_UNION
from ydk._core._dm_meta_info import REFERENCE_CLASS, REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, ANYXML_CLASS
from ydk._core._importer import _yang_ns

_meta_table = {
    'Banner' : _MetaInfoEnum('Banner',
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_infra_cfg', 'Banner',
        '''Banner''',
        {
            'exec':'exec_',
            'incoming':'incoming',
            'motd':'motd',
            'login':'login',
            'slip-ppp':'slip_ppp',
            'prompt-timeout':'prompt_timeout',
        }, 'Cisco-IOS-XR-infra-infra-cfg', _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-infra-infra-cfg']),
    'Banners.Banner' : {
        'meta_info' : _MetaInfoClass('Banners.Banner', REFERENCE_LIST,
            '''Select a Banner Type''',
            False, 
            [
            _MetaInfoClassMember('banner-name', REFERENCE_ENUM_CLASS, 'Banner', 'Banner',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_infra_cfg', 'Banner',
                [], [],
                '''                Banner Type
                ''',
                'banner_name',
                'Cisco-IOS-XR-infra-infra-cfg', True),
            _MetaInfoClassMember('banner-text', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                Banner text message
                ''',
                'banner_text',
                'Cisco-IOS-XR-infra-infra-cfg', False, is_mandatory=True),
            ],
            'Cisco-IOS-XR-infra-infra-cfg',
            'banner',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-infra-infra-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_infra_cfg',
        ),
    },
    'Banners' : {
        'meta_info' : _MetaInfoClass('Banners', REFERENCE_CLASS,
            '''Schema for Banner configuration commands''',
            False, 
            [
            _MetaInfoClassMember('banner', REFERENCE_LIST, 'Banner', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_infra_cfg', 'Banners.Banner',
                [], [],
                '''                Select a Banner Type
                ''',
                'banner',
                'Cisco-IOS-XR-infra-infra-cfg', False),
            ],
            'Cisco-IOS-XR-infra-infra-cfg',
            'banners',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-infra-infra-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_infra_cfg',
        ),
    },
}
_meta_table['Banners.Banner']['meta_info'].parent =_meta_table['Banners']['meta_info']
