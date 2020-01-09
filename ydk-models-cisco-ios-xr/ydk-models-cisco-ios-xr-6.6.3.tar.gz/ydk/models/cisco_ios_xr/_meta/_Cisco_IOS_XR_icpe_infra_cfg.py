
'''
This is auto-generated file,
which includes metadata for module Cisco_IOS_XR_icpe_infra_cfg
'''

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_LIST, REFERENCE_LEAFLIST, REFERENCE_BITS, REFERENCE_UNION
from ydk._core._dm_meta_info import REFERENCE_CLASS, REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, ANYXML_CLASS
from ydk._core._importer import _yang_ns

_meta_table = {
    'NvSatelliteGlobal.ChassisMac' : {
        'meta_info' : _MetaInfoClass('NvSatelliteGlobal.ChassisMac', REFERENCE_CLASS,
            '''Chassis MAC address''',
            False, 
            [
            _MetaInfoClassMember('mac1', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('0', '2147483647')], [],
                '''                First two bytes of MAC address
                ''',
                'mac1',
                'Cisco-IOS-XR-icpe-infra-cfg', False),
            _MetaInfoClassMember('mac2', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('0', '2147483647')], [],
                '''                Second two bytes of MAC address
                ''',
                'mac2',
                'Cisco-IOS-XR-icpe-infra-cfg', False),
            _MetaInfoClassMember('mac3', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('0', '2147483647')], [],
                '''                Third two bytes of MAC address
                ''',
                'mac3',
                'Cisco-IOS-XR-icpe-infra-cfg', False),
            ],
            'Cisco-IOS-XR-icpe-infra-cfg',
            'chassis-mac',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-icpe-infra-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_icpe_infra_cfg',
        ),
    },
    'NvSatelliteGlobal' : {
        'meta_info' : _MetaInfoClass('NvSatelliteGlobal', REFERENCE_CLASS,
            '''nV Satellite Global configuration''',
            False, 
            [
            _MetaInfoClassMember('chassis-mac', REFERENCE_CLASS, 'ChassisMac', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_icpe_infra_cfg', 'NvSatelliteGlobal.ChassisMac',
                [], [],
                '''                Chassis MAC address
                ''',
                'chassis_mac',
                'Cisco-IOS-XR-icpe-infra-cfg', False),
            ],
            'Cisco-IOS-XR-icpe-infra-cfg',
            'nv-satellite-global',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-icpe-infra-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_icpe_infra_cfg',
        ),
    },
    'NvSatellites.NvSatellite.UpgradeOnConnect.ConnectType' : _MetaInfoEnum('ConnectType',
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_icpe_infra_cfg', 'NvSatellites.NvSatellite.UpgradeOnConnect.ConnectType',
        '''When to upgrade the satellite''',
        {
            'on-connection':'on_connection',
            'on-first-connection':'on_first_connection',
        }, 'Cisco-IOS-XR-icpe-infra-cfg', _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-icpe-infra-cfg']),
    'NvSatellites.NvSatellite.UpgradeOnConnect' : {
        'meta_info' : _MetaInfoClass('NvSatellites.NvSatellite.UpgradeOnConnect', REFERENCE_CLASS,
            '''Satellite auto-upgrade capability''',
            False, 
            [
            _MetaInfoClassMember('connect-type', REFERENCE_ENUM_CLASS, 'ConnectType', 'enumeration',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_icpe_infra_cfg', 'NvSatellites.NvSatellite.UpgradeOnConnect.ConnectType',
                [], [],
                '''                When to upgrade the satellite
                ''',
                'connect_type',
                'Cisco-IOS-XR-icpe-infra-cfg', False),
            _MetaInfoClassMember('reference', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                Reference name
                ''',
                'reference',
                'Cisco-IOS-XR-icpe-infra-cfg', False),
            _MetaInfoClassMember('image-reference', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                Image Reference name
                ''',
                'image_reference',
                'Cisco-IOS-XR-icpe-infra-cfg', False),
            ],
            'Cisco-IOS-XR-icpe-infra-cfg',
            'upgrade-on-connect',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-icpe-infra-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_icpe_infra_cfg',
        ),
    },
    'NvSatellites.NvSatellite.CandidateFabricPorts.CandidateFabricPort' : {
        'meta_info' : _MetaInfoClass('NvSatellites.NvSatellite.CandidateFabricPorts.CandidateFabricPort', REFERENCE_LIST,
            '''Enable interfaces on the satellite to be used
as fabric ports''',
            False, 
            [
            _MetaInfoClassMember('port-type', ATTRIBUTE, 'str', 'xr:Cisco-ios-xr-string',
                None, None,
                [], [b'[\\w\\-\\.:,_@#%$\\+=\\|;]+'],
                '''                Port type
                ''',
                'port_type',
                'Cisco-IOS-XR-icpe-infra-cfg', True),
            _MetaInfoClassMember('slot', ATTRIBUTE, 'int', 'Icpe-slot',
                None, None,
                [('0', '8')], [],
                '''                Slot
                ''',
                'slot',
                'Cisco-IOS-XR-icpe-infra-cfg', True),
            _MetaInfoClassMember('sub-slot', ATTRIBUTE, 'int', 'Icpe-subslot',
                None, None,
                [('0', '8')], [],
                '''                Sub slot
                ''',
                'sub_slot',
                'Cisco-IOS-XR-icpe-infra-cfg', True),
            _MetaInfoClassMember('port-range', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                Port range
                ''',
                'port_range',
                'Cisco-IOS-XR-icpe-infra-cfg', False, is_mandatory=True),
            ],
            'Cisco-IOS-XR-icpe-infra-cfg',
            'candidate-fabric-port',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-icpe-infra-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_icpe_infra_cfg',
        ),
    },
    'NvSatellites.NvSatellite.CandidateFabricPorts' : {
        'meta_info' : _MetaInfoClass('NvSatellites.NvSatellite.CandidateFabricPorts', REFERENCE_CLASS,
            '''Enable interfaces on the satellite to be used
as fabric ports table''',
            False, 
            [
            _MetaInfoClassMember('candidate-fabric-port', REFERENCE_LIST, 'CandidateFabricPort', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_icpe_infra_cfg', 'NvSatellites.NvSatellite.CandidateFabricPorts.CandidateFabricPort',
                [], [],
                '''                Enable interfaces on the satellite to be used
                as fabric ports
                ''',
                'candidate_fabric_port',
                'Cisco-IOS-XR-icpe-infra-cfg', False),
            ],
            'Cisco-IOS-XR-icpe-infra-cfg',
            'candidate-fabric-ports',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-icpe-infra-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_icpe_infra_cfg',
        ),
    },
    'NvSatellites.NvSatellite.ConnectionInfo' : {
        'meta_info' : _MetaInfoClass('NvSatellites.NvSatellite.ConnectionInfo', REFERENCE_CLASS,
            '''Satellite User''',
            False, 
            [
            _MetaInfoClassMember('username', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                Satellite Username
                ''',
                'username',
                'Cisco-IOS-XR-icpe-infra-cfg', False),
            _MetaInfoClassMember('password', ATTRIBUTE, 'str', 'xr:Md5-password',
                None, None,
                [], [b'(!.+)|([^!].+)'],
                '''                Encrypted password for the user
                ''',
                'password',
                'Cisco-IOS-XR-icpe-infra-cfg', False),
            ],
            'Cisco-IOS-XR-icpe-infra-cfg',
            'connection-info',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-icpe-infra-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_icpe_infra_cfg',
        ),
    },
    'NvSatellites.NvSatellite.Redundancy' : {
        'meta_info' : _MetaInfoClass('NvSatellites.NvSatellite.Redundancy', REFERENCE_CLASS,
            '''Redundancy submode''',
            False, 
            [
            _MetaInfoClassMember('host-priority', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('0', '255')], [],
                '''                Priority for this host for the given satellite
                ''',
                'host_priority',
                'Cisco-IOS-XR-icpe-infra-cfg', False),
            ],
            'Cisco-IOS-XR-icpe-infra-cfg',
            'redundancy',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-icpe-infra-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_icpe_infra_cfg',
        ),
    },
    'NvSatellites.NvSatellite' : {
        'meta_info' : _MetaInfoClass('NvSatellites.NvSatellite', REFERENCE_LIST,
            '''Satellite Configuration''',
            False, 
            [
            _MetaInfoClassMember('satellite-id', ATTRIBUTE, 'int', 'Icpe-sat-id',
                None, None,
                [('100', '65534')], [],
                '''                Satellite ID
                ''',
                'satellite_id',
                'Cisco-IOS-XR-icpe-infra-cfg', True),
            _MetaInfoClassMember('upgrade-on-connect', REFERENCE_CLASS, 'UpgradeOnConnect', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_icpe_infra_cfg', 'NvSatellites.NvSatellite.UpgradeOnConnect',
                [], [],
                '''                Satellite auto-upgrade capability
                ''',
                'upgrade_on_connect',
                'Cisco-IOS-XR-icpe-infra-cfg', False),
            _MetaInfoClassMember('candidate-fabric-ports', REFERENCE_CLASS, 'CandidateFabricPorts', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_icpe_infra_cfg', 'NvSatellites.NvSatellite.CandidateFabricPorts',
                [], [],
                '''                Enable interfaces on the satellite to be used
                as fabric ports table
                ''',
                'candidate_fabric_ports',
                'Cisco-IOS-XR-icpe-infra-cfg', False),
            _MetaInfoClassMember('connection-info', REFERENCE_CLASS, 'ConnectionInfo', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_icpe_infra_cfg', 'NvSatellites.NvSatellite.ConnectionInfo',
                [], [],
                '''                Satellite User
                ''',
                'connection_info',
                'Cisco-IOS-XR-icpe-infra-cfg', False),
            _MetaInfoClassMember('redundancy', REFERENCE_CLASS, 'Redundancy', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_icpe_infra_cfg', 'NvSatellites.NvSatellite.Redundancy',
                [], [],
                '''                Redundancy submode
                ''',
                'redundancy',
                'Cisco-IOS-XR-icpe-infra-cfg', False),
            _MetaInfoClassMember('vrf', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                VRF for Satellite IP Address
                ''',
                'vrf',
                'Cisco-IOS-XR-icpe-infra-cfg', False),
            _MetaInfoClassMember('timeout-warning', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('0', '4294967295')], [],
                '''                Discovery timeout warning for the satellite
                ''',
                'timeout_warning',
                'Cisco-IOS-XR-icpe-infra-cfg', False),
            _MetaInfoClassMember('device-name', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                Satellite Name
                ''',
                'device_name',
                'Cisco-IOS-XR-icpe-infra-cfg', False),
            _MetaInfoClassMember('description', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                Satellite Description
                ''',
                'description',
                'Cisco-IOS-XR-icpe-infra-cfg', False),
            _MetaInfoClassMember('type', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                Satellite Type
                ''',
                'type',
                'Cisco-IOS-XR-icpe-infra-cfg', False, is_mandatory=True),
            _MetaInfoClassMember('enable', ATTRIBUTE, 'Empty', 'empty',
                None, None,
                [], [],
                '''                Enable
                ''',
                'enable',
                'Cisco-IOS-XR-icpe-infra-cfg', False, is_mandatory=True),
            _MetaInfoClassMember('disc-timeout', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('0', '4294967295')], [],
                '''                Discovery timeout for the satellite
                ''',
                'disc_timeout',
                'Cisco-IOS-XR-icpe-infra-cfg', False),
            _MetaInfoClassMember('delayed-switchback', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('0', '4294967295')], [],
                '''                Timer (in seconds) for delaying switchback in a
                dual home setup
                ''',
                'delayed_switchback',
                'Cisco-IOS-XR-icpe-infra-cfg', False),
            _MetaInfoClassMember('serial-number', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                Satellite Serial Number
                ''',
                'serial_number',
                'Cisco-IOS-XR-icpe-infra-cfg', False),
            _MetaInfoClassMember('secret', ATTRIBUTE, 'str', 'xr:Md5-password',
                None, None,
                [], [b'(!.+)|([^!].+)'],
                '''                Encrypted password for the Satellite
                ''',
                'secret',
                'Cisco-IOS-XR-icpe-infra-cfg', False),
            _MetaInfoClassMember('ip-address', REFERENCE_UNION, 'str', 'inet:ip-address-no-zone',
                None, None,
                [], [],
                '''                Satellite IP Address
                ''',
                'ip_address',
                'Cisco-IOS-XR-icpe-infra-cfg', False, [
                    _MetaInfoClassMember('ip-address', ATTRIBUTE, 'str', 'inet:ipv4-address-no-zone',
                        None, None,
                        [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'],
                        '''                        Satellite IP Address
                        ''',
                        'ip_address',
                        'Cisco-IOS-XR-icpe-infra-cfg', False),
                    _MetaInfoClassMember('ip-address', ATTRIBUTE, 'str', 'inet:ipv6-address-no-zone',
                        None, None,
                        [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'],
                        '''                        Satellite IP Address
                        ''',
                        'ip_address',
                        'Cisco-IOS-XR-icpe-infra-cfg', False),
                ]),
            ],
            'Cisco-IOS-XR-icpe-infra-cfg',
            'nv-satellite',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-icpe-infra-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_icpe_infra_cfg',
        ),
    },
    'NvSatellites' : {
        'meta_info' : _MetaInfoClass('NvSatellites', REFERENCE_CLASS,
            '''nv satellites''',
            False, 
            [
            _MetaInfoClassMember('nv-satellite', REFERENCE_LIST, 'NvSatellite', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_icpe_infra_cfg', 'NvSatellites.NvSatellite',
                [], [],
                '''                Satellite Configuration
                ''',
                'nv_satellite',
                'Cisco-IOS-XR-icpe-infra-cfg', False),
            ],
            'Cisco-IOS-XR-icpe-infra-cfg',
            'nv-satellites',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-icpe-infra-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_icpe_infra_cfg',
        ),
    },
}
_meta_table['NvSatelliteGlobal.ChassisMac']['meta_info'].parent =_meta_table['NvSatelliteGlobal']['meta_info']
_meta_table['NvSatellites.NvSatellite.CandidateFabricPorts.CandidateFabricPort']['meta_info'].parent =_meta_table['NvSatellites.NvSatellite.CandidateFabricPorts']['meta_info']
_meta_table['NvSatellites.NvSatellite.UpgradeOnConnect']['meta_info'].parent =_meta_table['NvSatellites.NvSatellite']['meta_info']
_meta_table['NvSatellites.NvSatellite.CandidateFabricPorts']['meta_info'].parent =_meta_table['NvSatellites.NvSatellite']['meta_info']
_meta_table['NvSatellites.NvSatellite.ConnectionInfo']['meta_info'].parent =_meta_table['NvSatellites.NvSatellite']['meta_info']
_meta_table['NvSatellites.NvSatellite.Redundancy']['meta_info'].parent =_meta_table['NvSatellites.NvSatellite']['meta_info']
_meta_table['NvSatellites.NvSatellite']['meta_info'].parent =_meta_table['NvSatellites']['meta_info']
