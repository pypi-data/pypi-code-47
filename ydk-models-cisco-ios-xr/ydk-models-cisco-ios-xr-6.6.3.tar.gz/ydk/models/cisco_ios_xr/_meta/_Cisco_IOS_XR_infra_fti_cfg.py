
'''
This is auto-generated file,
which includes metadata for module Cisco_IOS_XR_infra_fti_cfg
'''

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_LIST, REFERENCE_LEAFLIST, REFERENCE_BITS, REFERENCE_UNION
from ydk._core._dm_meta_info import REFERENCE_CLASS, REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, ANYXML_CLASS
from ydk._core._importer import _yang_ns

_meta_table = {
    'DciFabricInterconnect.Fabrics.Fabric.Controllers.Controller' : {
        'meta_info' : _MetaInfoClass('DciFabricInterconnect.Fabrics.Fabric.Controllers.Controller', REFERENCE_LIST,
            '''Enter Spine IP address''',
            False, 
            [
            _MetaInfoClassMember('ip1', ATTRIBUTE, 'str', 'inet:ipv4-address-no-zone',
                None, None,
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'],
                '''                Enter Spine IP address
                ''',
                'ip1',
                'Cisco-IOS-XR-infra-fti-cfg', True),
            ],
            'Cisco-IOS-XR-infra-fti-cfg',
            'controller',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-infra-fti-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_fti_cfg',
        ),
    },
    'DciFabricInterconnect.Fabrics.Fabric.Controllers' : {
        'meta_info' : _MetaInfoClass('DciFabricInterconnect.Fabrics.Fabric.Controllers', REFERENCE_CLASS,
            '''Enter Opflex peer info''',
            False, 
            [
            _MetaInfoClassMember('controller', REFERENCE_LIST, 'Controller', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_fti_cfg', 'DciFabricInterconnect.Fabrics.Fabric.Controllers.Controller',
                [], [],
                '''                Enter Spine IP address
                ''',
                'controller',
                'Cisco-IOS-XR-infra-fti-cfg', False),
            ],
            'Cisco-IOS-XR-infra-fti-cfg',
            'controllers',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-infra-fti-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_fti_cfg',
        ),
    },
    'DciFabricInterconnect.Fabrics.Fabric' : {
        'meta_info' : _MetaInfoClass('DciFabricInterconnect.Fabrics.Fabric', REFERENCE_LIST,
            '''Enter fabric identifier''',
            False, 
            [
            _MetaInfoClassMember('id1', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('1000', '9999')], [],
                '''                fabric identifier
                ''',
                'id1',
                'Cisco-IOS-XR-infra-fti-cfg', True),
            _MetaInfoClassMember('controllers', REFERENCE_CLASS, 'Controllers', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_fti_cfg', 'DciFabricInterconnect.Fabrics.Fabric.Controllers',
                [], [],
                '''                Enter Opflex peer info
                ''',
                'controllers',
                'Cisco-IOS-XR-infra-fti-cfg', False),
            _MetaInfoClassMember('ssl', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                Disabled or Path to certificate
                ''',
                'ssl',
                'Cisco-IOS-XR-infra-fti-cfg', False),
            ],
            'Cisco-IOS-XR-infra-fti-cfg',
            'fabric',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-infra-fti-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_fti_cfg',
        ),
    },
    'DciFabricInterconnect.Fabrics' : {
        'meta_info' : _MetaInfoClass('DciFabricInterconnect.Fabrics', REFERENCE_CLASS,
            '''Configure fabric parameters''',
            False, 
            [
            _MetaInfoClassMember('fabric', REFERENCE_LIST, 'Fabric', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_fti_cfg', 'DciFabricInterconnect.Fabrics.Fabric',
                [], [],
                '''                Enter fabric identifier
                ''',
                'fabric',
                'Cisco-IOS-XR-infra-fti-cfg', False),
            ],
            'Cisco-IOS-XR-infra-fti-cfg',
            'fabrics',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-infra-fti-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_fti_cfg',
        ),
    },
    'DciFabricInterconnect.Acp.BdRange' : {
        'meta_info' : _MetaInfoClass('DciFabricInterconnect.Acp.BdRange', REFERENCE_CLASS,
            '''Specify BD pool range''',
            False, 
            [
            _MetaInfoClassMember('bd-min', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('1', '4000')], [],
                '''                BD Range:min value
                ''',
                'bd_min',
                'Cisco-IOS-XR-infra-fti-cfg', False),
            _MetaInfoClassMember('bd-max', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('0', '4294967295')], [],
                '''                BD Range:max value
                ''',
                'bd_max',
                'Cisco-IOS-XR-infra-fti-cfg', False),
            ],
            'Cisco-IOS-XR-infra-fti-cfg',
            'bd-range',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-infra-fti-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_fti_cfg',
        ),
    },
    'DciFabricInterconnect.Acp.VniRange' : {
        'meta_info' : _MetaInfoClass('DciFabricInterconnect.Acp.VniRange', REFERENCE_CLASS,
            '''Specify VNI pool range''',
            False, 
            [
            _MetaInfoClassMember('vni-min', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('1', '4000')], [],
                '''                VNI Range:min value
                ''',
                'vni_min',
                'Cisco-IOS-XR-infra-fti-cfg', False),
            _MetaInfoClassMember('vni-max', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('0', '4294967295')], [],
                '''                VNI Range:max value
                ''',
                'vni_max',
                'Cisco-IOS-XR-infra-fti-cfg', False),
            ],
            'Cisco-IOS-XR-infra-fti-cfg',
            'vni-range',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-infra-fti-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_fti_cfg',
        ),
    },
    'DciFabricInterconnect.Acp.BviRange' : {
        'meta_info' : _MetaInfoClass('DciFabricInterconnect.Acp.BviRange', REFERENCE_CLASS,
            '''Specify BVI pool range''',
            False, 
            [
            _MetaInfoClassMember('bvi-min', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('1', '4000')], [],
                '''                BVI Range:min value
                ''',
                'bvi_min',
                'Cisco-IOS-XR-infra-fti-cfg', False),
            _MetaInfoClassMember('bvi-max', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('0', '4294967295')], [],
                '''                BVI Range:max value
                ''',
                'bvi_max',
                'Cisco-IOS-XR-infra-fti-cfg', False),
            ],
            'Cisco-IOS-XR-infra-fti-cfg',
            'bvi-range',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-infra-fti-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_fti_cfg',
        ),
    },
    'DciFabricInterconnect.Acp.Vrfs.Vrf' : {
        'meta_info' : _MetaInfoClass('DciFabricInterconnect.Acp.Vrfs.Vrf', REFERENCE_LIST,
            '''vrf name''',
            False, 
            [
            _MetaInfoClassMember('vrf-name', ATTRIBUTE, 'str', 'xr:Cisco-ios-xr-string',
                None, None,
                [], [b'[\\w\\-\\.:,_@#%$\\+=\\|;]+'],
                '''                vrf name
                ''',
                'vrf_name',
                'Cisco-IOS-XR-infra-fti-cfg', True),
            _MetaInfoClassMember('bvi-vrf-ip', ATTRIBUTE, 'str', 'inet:ipv4-address-no-zone',
                None, None,
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'],
                '''                BVI override IP address
                ''',
                'bvi_vrf_ip',
                'Cisco-IOS-XR-infra-fti-cfg', False),
            ],
            'Cisco-IOS-XR-infra-fti-cfg',
            'vrf',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-infra-fti-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_fti_cfg',
        ),
    },
    'DciFabricInterconnect.Acp.Vrfs' : {
        'meta_info' : _MetaInfoClass('DciFabricInterconnect.Acp.Vrfs', REFERENCE_CLASS,
            '''Configure local VRF parameters''',
            False, 
            [
            _MetaInfoClassMember('vrf', REFERENCE_LIST, 'Vrf', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_fti_cfg', 'DciFabricInterconnect.Acp.Vrfs.Vrf',
                [], [],
                '''                vrf name
                ''',
                'vrf',
                'Cisco-IOS-XR-infra-fti-cfg', False),
            ],
            'Cisco-IOS-XR-infra-fti-cfg',
            'vrfs',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-infra-fti-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_fti_cfg',
        ),
    },
    'DciFabricInterconnect.Acp' : {
        'meta_info' : _MetaInfoClass('DciFabricInterconnect.Acp', REFERENCE_CLASS,
            '''Configure Auto Config Pool parameters''',
            False, 
            [
            _MetaInfoClassMember('bd-range', REFERENCE_CLASS, 'BdRange', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_fti_cfg', 'DciFabricInterconnect.Acp.BdRange',
                [], [],
                '''                Specify BD pool range
                ''',
                'bd_range',
                'Cisco-IOS-XR-infra-fti-cfg', False),
            _MetaInfoClassMember('vni-range', REFERENCE_CLASS, 'VniRange', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_fti_cfg', 'DciFabricInterconnect.Acp.VniRange',
                [], [],
                '''                Specify VNI pool range
                ''',
                'vni_range',
                'Cisco-IOS-XR-infra-fti-cfg', False),
            _MetaInfoClassMember('bvi-range', REFERENCE_CLASS, 'BviRange', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_fti_cfg', 'DciFabricInterconnect.Acp.BviRange',
                [], [],
                '''                Specify BVI pool range
                ''',
                'bvi_range',
                'Cisco-IOS-XR-infra-fti-cfg', False),
            _MetaInfoClassMember('vrfs', REFERENCE_CLASS, 'Vrfs', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_fti_cfg', 'DciFabricInterconnect.Acp.Vrfs',
                [], [],
                '''                Configure local VRF parameters
                ''',
                'vrfs',
                'Cisco-IOS-XR-infra-fti-cfg', False),
            _MetaInfoClassMember('nve-id', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('0', '4294967295')], [],
                '''                Specify NVE interface id
                ''',
                'nve_id',
                'Cisco-IOS-XR-infra-fti-cfg', False),
            _MetaInfoClassMember('bgp-as', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('0', '4294967295')], [],
                '''                Specify BGP AS number
                ''',
                'bgp_as',
                'Cisco-IOS-XR-infra-fti-cfg', False),
            _MetaInfoClassMember('bg-name', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                Specify Bridge-group name
                ''',
                'bg_name',
                'Cisco-IOS-XR-infra-fti-cfg', False),
            ],
            'Cisco-IOS-XR-infra-fti-cfg',
            'acp',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-infra-fti-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_fti_cfg',
        ),
    },
    'DciFabricInterconnect' : {
        'meta_info' : _MetaInfoClass('DciFabricInterconnect', REFERENCE_CLASS,
            '''Configure FTI parameters/sub-parameters''',
            False, 
            [
            _MetaInfoClassMember('fabrics', REFERENCE_CLASS, 'Fabrics', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_fti_cfg', 'DciFabricInterconnect.Fabrics',
                [], [],
                '''                Configure fabric parameters
                ''',
                'fabrics',
                'Cisco-IOS-XR-infra-fti-cfg', False),
            _MetaInfoClassMember('acp', REFERENCE_CLASS, 'Acp', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_fti_cfg', 'DciFabricInterconnect.Acp',
                [], [],
                '''                Configure Auto Config Pool parameters
                ''',
                'acp',
                'Cisco-IOS-XR-infra-fti-cfg', False),
            _MetaInfoClassMember('identity', ATTRIBUTE, 'str', 'inet:ipv4-address-no-zone',
                None, None,
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'],
                '''                Identity (Loopback IP address)<x.x.x.x>
                ''',
                'identity',
                'Cisco-IOS-XR-infra-fti-cfg', False),
            ],
            'Cisco-IOS-XR-infra-fti-cfg',
            'dci-fabric-interconnect',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-infra-fti-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_fti_cfg',
        ),
    },
}
_meta_table['DciFabricInterconnect.Fabrics.Fabric.Controllers.Controller']['meta_info'].parent =_meta_table['DciFabricInterconnect.Fabrics.Fabric.Controllers']['meta_info']
_meta_table['DciFabricInterconnect.Fabrics.Fabric.Controllers']['meta_info'].parent =_meta_table['DciFabricInterconnect.Fabrics.Fabric']['meta_info']
_meta_table['DciFabricInterconnect.Fabrics.Fabric']['meta_info'].parent =_meta_table['DciFabricInterconnect.Fabrics']['meta_info']
_meta_table['DciFabricInterconnect.Acp.Vrfs.Vrf']['meta_info'].parent =_meta_table['DciFabricInterconnect.Acp.Vrfs']['meta_info']
_meta_table['DciFabricInterconnect.Acp.BdRange']['meta_info'].parent =_meta_table['DciFabricInterconnect.Acp']['meta_info']
_meta_table['DciFabricInterconnect.Acp.VniRange']['meta_info'].parent =_meta_table['DciFabricInterconnect.Acp']['meta_info']
_meta_table['DciFabricInterconnect.Acp.BviRange']['meta_info'].parent =_meta_table['DciFabricInterconnect.Acp']['meta_info']
_meta_table['DciFabricInterconnect.Acp.Vrfs']['meta_info'].parent =_meta_table['DciFabricInterconnect.Acp']['meta_info']
_meta_table['DciFabricInterconnect.Fabrics']['meta_info'].parent =_meta_table['DciFabricInterconnect']['meta_info']
_meta_table['DciFabricInterconnect.Acp']['meta_info'].parent =_meta_table['DciFabricInterconnect']['meta_info']
