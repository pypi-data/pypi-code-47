
'''
This is auto-generated file,
which includes metadata for module Cisco_IOS_XR_snmp_agent_cfg
'''

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_LIST, REFERENCE_LEAFLIST, REFERENCE_BITS, REFERENCE_UNION
from ydk._core._dm_meta_info import REFERENCE_CLASS, REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, ANYXML_CLASS
from ydk._core._importer import _yang_ns

_meta_table = {
    'SnmpTos' : _MetaInfoEnum('SnmpTos',
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg', 'SnmpTos',
        '''Snmp tos''',
        {
            'precedence':'precedence',
            'dscp':'dscp',
        }, 'Cisco-IOS-XR-snmp-agent-cfg', _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-snmp-agent-cfg']),
    'SnmpHashAlgorithm' : _MetaInfoEnum('SnmpHashAlgorithm',
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg', 'SnmpHashAlgorithm',
        '''Snmp hash algorithm''',
        {
            'none':'none',
            'md5':'md5',
            'sha':'sha',
        }, 'Cisco-IOS-XR-snmp-agent-cfg', _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-snmp-agent-cfg']),
    'SnmpPrivAlgorithm' : _MetaInfoEnum('SnmpPrivAlgorithm',
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg', 'SnmpPrivAlgorithm',
        '''Snmp priv algorithm''',
        {
            'none':'none',
            'des':'des',
            '3des':'Y_3des',
            'aes128':'aes128',
            'aes192':'aes192',
            'aes256':'aes256',
        }, 'Cisco-IOS-XR-snmp-agent-cfg', _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-snmp-agent-cfg']),
    'SnmpOwnerAccess' : _MetaInfoEnum('SnmpOwnerAccess',
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg', 'SnmpOwnerAccess',
        '''Snmp owner access''',
        {
            'sdr-owner':'sdr_owner',
            'system-owner':'system_owner',
        }, 'Cisco-IOS-XR-snmp-agent-cfg', _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-snmp-agent-cfg']),
    'SnmpBulkstatSchema' : _MetaInfoEnum('SnmpBulkstatSchema',
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg', 'SnmpBulkstatSchema',
        '''Snmp bulkstat schema''',
        {
            'exact-interface':'exact_interface',
            'exact-oid':'exact_oid',
            'wild-interface':'wild_interface',
            'wild-oid':'wild_oid',
            'range-oid':'range_oid',
            'repeat-oid':'repeat_oid',
        }, 'Cisco-IOS-XR-snmp-agent-cfg', _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-snmp-agent-cfg']),
    'Snmpacl' : _MetaInfoEnum('Snmpacl',
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg', 'Snmpacl',
        '''Snmpacl''',
        {
            'ipv4':'ipv4',
            'ipv6':'ipv6',
        }, 'Cisco-IOS-XR-snmp-agent-cfg', _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-snmp-agent-cfg']),
    'SnmpDscpValue' : _MetaInfoEnum('SnmpDscpValue',
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg', 'SnmpDscpValue',
        ''' ''',
        {
            'default':'default',
            'af11':'af11',
            'af12':'af12',
            'af13':'af13',
            'af21':'af21',
            'af22':'af22',
            'af23':'af23',
            'af31':'af31',
            'af32':'af32',
            'af33':'af33',
            'af41':'af41',
            'af42':'af42',
            'af43':'af43',
            'ef':'ef',
            'cs1':'cs1',
            'cs2':'cs2',
            'cs3':'cs3',
            'cs4':'cs4',
            'cs5':'cs5',
            'cs6':'cs6',
            'cs7':'cs7',
        }, 'Cisco-IOS-XR-snmp-agent-cfg', _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-snmp-agent-cfg']),
    'SnmpPrecedenceValue1' : _MetaInfoEnum('SnmpPrecedenceValue1',
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg', 'SnmpPrecedenceValue1',
        ''' ''',
        {
            'routine':'routine',
            'priority':'priority',
            'immediate':'immediate',
            'flash':'flash',
            'flash-override':'flash_override',
            'critical':'critical',
            'internet':'internet',
            'network':'network',
        }, 'Cisco-IOS-XR-snmp-agent-cfg', _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-snmp-agent-cfg']),
    'SnmpSecurityModel' : _MetaInfoEnum('SnmpSecurityModel',
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg', 'SnmpSecurityModel',
        '''Snmp security model''',
        {
            'no-authentication':'no_authentication',
            'authentication':'authentication',
            'privacy':'privacy',
        }, 'Cisco-IOS-XR-snmp-agent-cfg', _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-snmp-agent-cfg']),
    'SnmpMibViewInclusion' : _MetaInfoEnum('SnmpMibViewInclusion',
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg', 'SnmpMibViewInclusion',
        '''Snmp mib view inclusion''',
        {
            'included':'included',
            'excluded':'excluded',
        }, 'Cisco-IOS-XR-snmp-agent-cfg', _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-snmp-agent-cfg']),
    'SnmpBulkstatFileFormat' : _MetaInfoEnum('SnmpBulkstatFileFormat',
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg', 'SnmpBulkstatFileFormat',
        '''Snmp bulkstat file format''',
        {
            'schema-ascii':'schema_ascii',
            'bulk-ascii':'bulk_ascii',
            'bulk-binary':'bulk_binary',
        }, 'Cisco-IOS-XR-snmp-agent-cfg', _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-snmp-agent-cfg']),
    'SnmpAccessLevel' : _MetaInfoEnum('SnmpAccessLevel',
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg', 'SnmpAccessLevel',
        '''Snmp access level''',
        {
            'read-only':'read_only',
            'read-write':'read_write',
        }, 'Cisco-IOS-XR-snmp-agent-cfg', _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-snmp-agent-cfg']),
    'SnmpContext' : _MetaInfoEnum('SnmpContext',
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg', 'SnmpContext',
        '''Snmp context''',
        {
            'vrf':'vrf',
            'bridge':'bridge',
            'ospf':'ospf',
            'ospfv3':'ospfv3',
        }, 'Cisco-IOS-XR-snmp-agent-cfg', _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-snmp-agent-cfg']),
    'GroupSnmpVersion' : _MetaInfoEnum('GroupSnmpVersion',
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg', 'GroupSnmpVersion',
        '''Group snmp version''',
        {
            'v1':'v1',
            'v2c':'v2c',
            'v3':'v3',
        }, 'Cisco-IOS-XR-snmp-agent-cfg', _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-snmp-agent-cfg']),
    'UserSnmpVersion' : _MetaInfoEnum('UserSnmpVersion',
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg', 'UserSnmpVersion',
        '''User snmp version''',
        {
            'v1':'v1',
            'v2c':'v2c',
            'v3':'v3',
        }, 'Cisco-IOS-XR-snmp-agent-cfg', _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-snmp-agent-cfg']),
    'Snmp.EncryptedCommunityMaps.EncryptedCommunityMap' : {
        'meta_info' : _MetaInfoClass('Snmp.EncryptedCommunityMaps.EncryptedCommunityMap', REFERENCE_LIST,
            '''Clear/encrypted SNMP community map''',
            False, 
            [
            _MetaInfoClassMember('community-name', ATTRIBUTE, 'str', 'xr:Cisco-ios-xr-string',
                None, None,
                [], [b'[\\w\\-\\.:,_@#%$\\+=\\|;]+'],
                '''                SNMP community map
                ''',
                'community_name',
                'Cisco-IOS-XR-snmp-agent-cfg', True),
            _MetaInfoClassMember('context', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                SNMP Context Name 
                ''',
                'context',
                'Cisco-IOS-XR-snmp-agent-cfg', False),
            _MetaInfoClassMember('security', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                SNMP Security Name 
                ''',
                'security',
                'Cisco-IOS-XR-snmp-agent-cfg', False),
            _MetaInfoClassMember('target-list', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                target list name 
                ''',
                'target_list',
                'Cisco-IOS-XR-snmp-agent-cfg', False),
            ],
            'Cisco-IOS-XR-snmp-agent-cfg',
            'encrypted-community-map',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-snmp-agent-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg',
        ),
    },
    'Snmp.EncryptedCommunityMaps' : {
        'meta_info' : _MetaInfoClass('Snmp.EncryptedCommunityMaps', REFERENCE_CLASS,
            '''Container class to hold clear/encrypted
communitie maps''',
            False, 
            [
            _MetaInfoClassMember('encrypted-community-map', REFERENCE_LIST, 'EncryptedCommunityMap', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg', 'Snmp.EncryptedCommunityMaps.EncryptedCommunityMap',
                [], [],
                '''                Clear/encrypted SNMP community map
                ''',
                'encrypted_community_map',
                'Cisco-IOS-XR-snmp-agent-cfg', False),
            ],
            'Cisco-IOS-XR-snmp-agent-cfg',
            'encrypted-community-maps',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-snmp-agent-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg',
        ),
    },
    'Snmp.Views.View' : {
        'meta_info' : _MetaInfoClass('Snmp.Views.View', REFERENCE_LIST,
            '''Name of the view''',
            False, 
            [
            _MetaInfoClassMember('view-name', ATTRIBUTE, 'str', 'xr:Cisco-ios-xr-string',
                None, None,
                [], [b'[\\w\\-\\.:,_@#%$\\+=\\|;]+'],
                '''                Name of the view
                ''',
                'view_name',
                'Cisco-IOS-XR-snmp-agent-cfg', True),
            _MetaInfoClassMember('family', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                MIB view family name
                ''',
                'family',
                'Cisco-IOS-XR-snmp-agent-cfg', True),
            _MetaInfoClassMember('view-inclusion', REFERENCE_ENUM_CLASS, 'SnmpMibViewInclusion', 'Snmp-mib-view-inclusion',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg', 'SnmpMibViewInclusion',
                [], [],
                '''                MIB view to be included or excluded
                ''',
                'view_inclusion',
                'Cisco-IOS-XR-snmp-agent-cfg', False, is_mandatory=True),
            ],
            'Cisco-IOS-XR-snmp-agent-cfg',
            'view',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-snmp-agent-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg',
        ),
    },
    'Snmp.Views' : {
        'meta_info' : _MetaInfoClass('Snmp.Views', REFERENCE_CLASS,
            '''Class to configure a SNMPv2 MIB view''',
            False, 
            [
            _MetaInfoClassMember('view', REFERENCE_LIST, 'View', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg', 'Snmp.Views.View',
                [], [],
                '''                Name of the view
                ''',
                'view',
                'Cisco-IOS-XR-snmp-agent-cfg', False),
            ],
            'Cisco-IOS-XR-snmp-agent-cfg',
            'views',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-snmp-agent-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg',
        ),
    },
    'Snmp.Logging.Threshold' : {
        'meta_info' : _MetaInfoClass('Snmp.Logging.Threshold', REFERENCE_CLASS,
            '''SNMP logging threshold''',
            False, 
            [
            _MetaInfoClassMember('oid-processing', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('0', '20000')], [],
                '''                SNMP logging threshold for OID processing
                ''',
                'oid_processing',
                'Cisco-IOS-XR-snmp-agent-cfg', False, default_value="500"),
            _MetaInfoClassMember('pdu-processing', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('0', '20000')], [],
                '''                SNMP logging threshold for PDU processing
                ''',
                'pdu_processing',
                'Cisco-IOS-XR-snmp-agent-cfg', False, default_value="20000"),
            ],
            'Cisco-IOS-XR-snmp-agent-cfg',
            'threshold',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-snmp-agent-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg',
        ),
    },
    'Snmp.Logging' : {
        'meta_info' : _MetaInfoClass('Snmp.Logging', REFERENCE_CLASS,
            '''SNMP logging''',
            False, 
            [
            _MetaInfoClassMember('threshold', REFERENCE_CLASS, 'Threshold', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg', 'Snmp.Logging.Threshold',
                [], [],
                '''                SNMP logging threshold
                ''',
                'threshold',
                'Cisco-IOS-XR-snmp-agent-cfg', False),
            ],
            'Cisco-IOS-XR-snmp-agent-cfg',
            'logging',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-snmp-agent-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg',
        ),
    },
    'Snmp.Administration.DefaultCommunities.DefaultCommunity' : {
        'meta_info' : _MetaInfoClass('Snmp.Administration.DefaultCommunities.DefaultCommunity', REFERENCE_LIST,
            '''Unencrpted SNMP community string and access
priviledges''',
            False, 
            [
            _MetaInfoClassMember('community-name', ATTRIBUTE, 'str', 'string',
                None, None,
                [(1, 128)], [],
                '''                SNMP community string
                ''',
                'community_name',
                'Cisco-IOS-XR-snmp-agent-cfg', True),
            _MetaInfoClassMember('priviledge', REFERENCE_ENUM_CLASS, 'SnmpAccessLevel', 'Snmp-access-level',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg', 'SnmpAccessLevel',
                [], [],
                '''                Read/Write Access
                ''',
                'priviledge',
                'Cisco-IOS-XR-snmp-agent-cfg', False),
            _MetaInfoClassMember('view-name', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                MIB view to which the community has access
                ''',
                'view_name',
                'Cisco-IOS-XR-snmp-agent-cfg', False),
            _MetaInfoClassMember('v4acl-type', REFERENCE_ENUM_CLASS, 'Snmpacl', 'Snmpacl',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg', 'Snmpacl',
                [], [],
                '''                Access-list type
                ''',
                'v4acl_type',
                'Cisco-IOS-XR-snmp-agent-cfg', False),
            _MetaInfoClassMember('v4-access-list', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                Ipv4 Access-list name
                ''',
                'v4_access_list',
                'Cisco-IOS-XR-snmp-agent-cfg', False),
            _MetaInfoClassMember('v6acl-type', REFERENCE_ENUM_CLASS, 'Snmpacl', 'Snmpacl',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg', 'Snmpacl',
                [], [],
                '''                Access-list type
                ''',
                'v6acl_type',
                'Cisco-IOS-XR-snmp-agent-cfg', False),
            _MetaInfoClassMember('v6-access-list', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                Ipv6 Access-list name
                ''',
                'v6_access_list',
                'Cisco-IOS-XR-snmp-agent-cfg', False),
            _MetaInfoClassMember('owner', REFERENCE_ENUM_CLASS, 'SnmpOwnerAccess', 'Snmp-owner-access',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg', 'SnmpOwnerAccess',
                [], [],
                '''                Logical Router or System owner access
                ''',
                'owner',
                'Cisco-IOS-XR-snmp-agent-cfg', False),
            ],
            'Cisco-IOS-XR-snmp-agent-cfg',
            'default-community',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-snmp-agent-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg',
        ),
    },
    'Snmp.Administration.DefaultCommunities' : {
        'meta_info' : _MetaInfoClass('Snmp.Administration.DefaultCommunities', REFERENCE_CLASS,
            '''Container class to hold unencrpted communities''',
            False, 
            [
            _MetaInfoClassMember('default-community', REFERENCE_LIST, 'DefaultCommunity', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg', 'Snmp.Administration.DefaultCommunities.DefaultCommunity',
                [], [],
                '''                Unencrpted SNMP community string and access
                priviledges
                ''',
                'default_community',
                'Cisco-IOS-XR-snmp-agent-cfg', False),
            ],
            'Cisco-IOS-XR-snmp-agent-cfg',
            'default-communities',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-snmp-agent-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg',
        ),
    },
    'Snmp.Administration.EncryptedCommunities.EncryptedCommunity' : {
        'meta_info' : _MetaInfoClass('Snmp.Administration.EncryptedCommunities.EncryptedCommunity', REFERENCE_LIST,
            '''Clear/encrypted SNMP community string and
access priviledges''',
            False, 
            [
            _MetaInfoClassMember('community-name', ATTRIBUTE, 'str', 'xr:Cisco-ios-xr-string',
                None, None,
                [], [b'[\\w\\-\\.:,_@#%$\\+=\\|;]+'],
                '''                SNMP community string
                ''',
                'community_name',
                'Cisco-IOS-XR-snmp-agent-cfg', True),
            _MetaInfoClassMember('priviledge', REFERENCE_ENUM_CLASS, 'SnmpAccessLevel', 'Snmp-access-level',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg', 'SnmpAccessLevel',
                [], [],
                '''                Read/Write Access
                ''',
                'priviledge',
                'Cisco-IOS-XR-snmp-agent-cfg', False),
            _MetaInfoClassMember('view-name', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                MIB view to which the community has access
                ''',
                'view_name',
                'Cisco-IOS-XR-snmp-agent-cfg', False),
            _MetaInfoClassMember('v4acl-type', REFERENCE_ENUM_CLASS, 'Snmpacl', 'Snmpacl',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg', 'Snmpacl',
                [], [],
                '''                Access-list type
                ''',
                'v4acl_type',
                'Cisco-IOS-XR-snmp-agent-cfg', False),
            _MetaInfoClassMember('v4-access-list', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                Ipv4 Access-list name
                ''',
                'v4_access_list',
                'Cisco-IOS-XR-snmp-agent-cfg', False),
            _MetaInfoClassMember('v6acl-type', REFERENCE_ENUM_CLASS, 'Snmpacl', 'Snmpacl',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg', 'Snmpacl',
                [], [],
                '''                Access-list type
                ''',
                'v6acl_type',
                'Cisco-IOS-XR-snmp-agent-cfg', False),
            _MetaInfoClassMember('v6-access-list', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                Ipv6 Access-list name
                ''',
                'v6_access_list',
                'Cisco-IOS-XR-snmp-agent-cfg', False),
            _MetaInfoClassMember('owner', REFERENCE_ENUM_CLASS, 'SnmpOwnerAccess', 'Snmp-owner-access',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg', 'SnmpOwnerAccess',
                [], [],
                '''                Logical Router or System owner access
                ''',
                'owner',
                'Cisco-IOS-XR-snmp-agent-cfg', False),
            ],
            'Cisco-IOS-XR-snmp-agent-cfg',
            'encrypted-community',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-snmp-agent-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg',
        ),
    },
    'Snmp.Administration.EncryptedCommunities' : {
        'meta_info' : _MetaInfoClass('Snmp.Administration.EncryptedCommunities', REFERENCE_CLASS,
            '''Container class to hold clear/encrypted
communities''',
            False, 
            [
            _MetaInfoClassMember('encrypted-community', REFERENCE_LIST, 'EncryptedCommunity', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg', 'Snmp.Administration.EncryptedCommunities.EncryptedCommunity',
                [], [],
                '''                Clear/encrypted SNMP community string and
                access priviledges
                ''',
                'encrypted_community',
                'Cisco-IOS-XR-snmp-agent-cfg', False),
            ],
            'Cisco-IOS-XR-snmp-agent-cfg',
            'encrypted-communities',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-snmp-agent-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg',
        ),
    },
    'Snmp.Administration' : {
        'meta_info' : _MetaInfoClass('Snmp.Administration', REFERENCE_CLASS,
            '''Container class for SNMP administration''',
            False, 
            [
            _MetaInfoClassMember('default-communities', REFERENCE_CLASS, 'DefaultCommunities', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg', 'Snmp.Administration.DefaultCommunities',
                [], [],
                '''                Container class to hold unencrpted communities
                ''',
                'default_communities',
                'Cisco-IOS-XR-snmp-agent-cfg', False),
            _MetaInfoClassMember('encrypted-communities', REFERENCE_CLASS, 'EncryptedCommunities', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg', 'Snmp.Administration.EncryptedCommunities',
                [], [],
                '''                Container class to hold clear/encrypted
                communities
                ''',
                'encrypted_communities',
                'Cisco-IOS-XR-snmp-agent-cfg', False),
            ],
            'Cisco-IOS-XR-snmp-agent-cfg',
            'administration',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-snmp-agent-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg',
        ),
    },
    'Snmp.Agent.EngineId.Remotes.Remote' : {
        'meta_info' : _MetaInfoClass('Snmp.Agent.EngineId.Remotes.Remote', REFERENCE_LIST,
            '''engineID of the remote agent''',
            False, 
            [
            _MetaInfoClassMember('remote-address', REFERENCE_UNION, 'str', 'inet:ip-address-no-zone',
                None, None,
                [], [],
                '''                IP address of remote SNMP entity
                ''',
                'remote_address',
                'Cisco-IOS-XR-snmp-agent-cfg', True, [
                    _MetaInfoClassMember('remote-address', ATTRIBUTE, 'str', 'inet:ipv4-address-no-zone',
                        None, None,
                        [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'],
                        '''                        IP address of remote SNMP entity
                        ''',
                        'remote_address',
                        'Cisco-IOS-XR-snmp-agent-cfg', True),
                    _MetaInfoClassMember('remote-address', ATTRIBUTE, 'str', 'inet:ipv6-address-no-zone',
                        None, None,
                        [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'],
                        '''                        IP address of remote SNMP entity
                        ''',
                        'remote_address',
                        'Cisco-IOS-XR-snmp-agent-cfg', True),
                ]),
            _MetaInfoClassMember('remote-engine-id', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                engine ID octet string
                ''',
                'remote_engine_id',
                'Cisco-IOS-XR-snmp-agent-cfg', False),
            _MetaInfoClassMember('port', ATTRIBUTE, 'int', 'xr:Cisco-ios-xr-port-number',
                None, None,
                [('1', '65535')], [],
                '''                UDP port number
                ''',
                'port',
                'Cisco-IOS-XR-snmp-agent-cfg', False),
            ],
            'Cisco-IOS-XR-snmp-agent-cfg',
            'remote',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-snmp-agent-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg',
        ),
    },
    'Snmp.Agent.EngineId.Remotes' : {
        'meta_info' : _MetaInfoClass('Snmp.Agent.EngineId.Remotes', REFERENCE_CLASS,
            '''SNMPv3 remote SNMP Entity''',
            False, 
            [
            _MetaInfoClassMember('remote', REFERENCE_LIST, 'Remote', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg', 'Snmp.Agent.EngineId.Remotes.Remote',
                [], [],
                '''                engineID of the remote agent
                ''',
                'remote',
                'Cisco-IOS-XR-snmp-agent-cfg', False),
            ],
            'Cisco-IOS-XR-snmp-agent-cfg',
            'remotes',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-snmp-agent-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg',
        ),
    },
    'Snmp.Agent.EngineId' : {
        'meta_info' : _MetaInfoClass('Snmp.Agent.EngineId', REFERENCE_CLASS,
            '''SNMPv3 engineID''',
            False, 
            [
            _MetaInfoClassMember('remotes', REFERENCE_CLASS, 'Remotes', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg', 'Snmp.Agent.EngineId.Remotes',
                [], [],
                '''                SNMPv3 remote SNMP Entity
                ''',
                'remotes',
                'Cisco-IOS-XR-snmp-agent-cfg', False),
            _MetaInfoClassMember('local', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                engineID of the local agent
                ''',
                'local',
                'Cisco-IOS-XR-snmp-agent-cfg', False),
            ],
            'Cisco-IOS-XR-snmp-agent-cfg',
            'engine-id',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-snmp-agent-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg',
        ),
    },
    'Snmp.Agent' : {
        'meta_info' : _MetaInfoClass('Snmp.Agent', REFERENCE_CLASS,
            '''The heirarchy point for SNMP Agent
configurations''',
            False, 
            [
            _MetaInfoClassMember('engine-id', REFERENCE_CLASS, 'EngineId', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg', 'Snmp.Agent.EngineId',
                [], [],
                '''                SNMPv3 engineID
                ''',
                'engine_id',
                'Cisco-IOS-XR-snmp-agent-cfg', False),
            ],
            'Cisco-IOS-XR-snmp-agent-cfg',
            'agent',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-snmp-agent-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg',
        ),
    },
    'Snmp.Trap' : {
        'meta_info' : _MetaInfoClass('Snmp.Trap', REFERENCE_CLASS,
            '''Class to hold trap configurations''',
            False, 
            [
            _MetaInfoClassMember('timeout', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('1', '1000')], [],
                '''                Timeout for TRAP message retransmissions
                ''',
                'timeout',
                'Cisco-IOS-XR-snmp-agent-cfg', False),
            _MetaInfoClassMember('throttle-time', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('10', '500')], [],
                '''                Set throttle time for handling traps
                ''',
                'throttle_time',
                'Cisco-IOS-XR-snmp-agent-cfg', False),
            _MetaInfoClassMember('queue-length', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('1', '5000')], [],
                '''                Message queue length for each TRAP host
                ''',
                'queue_length',
                'Cisco-IOS-XR-snmp-agent-cfg', False),
            ],
            'Cisco-IOS-XR-snmp-agent-cfg',
            'trap',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-snmp-agent-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg',
        ),
    },
    'Snmp.DropPacket' : {
        'meta_info' : _MetaInfoClass('Snmp.DropPacket', REFERENCE_CLASS,
            '''SNMP packet drop config''',
            False, 
            [
            _MetaInfoClassMember('unknown-user', ATTRIBUTE, 'Empty', 'empty',
                None, None,
                [], [],
                '''                Enable drop unknown user name
                ''',
                'unknown_user',
                'Cisco-IOS-XR-snmp-agent-cfg', False),
            ],
            'Cisco-IOS-XR-snmp-agent-cfg',
            'drop-packet',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-snmp-agent-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg',
        ),
    },
    'Snmp.Ipv6.Tos' : {
        'meta_info' : _MetaInfoClass('Snmp.Ipv6.Tos', REFERENCE_CLASS,
            '''Type of TOS''',
            False, 
            [
            _MetaInfoClassMember('type', REFERENCE_ENUM_CLASS, 'SnmpTos', 'Snmp-tos',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg', 'SnmpTos',
                [], [],
                '''                SNMP TOS type DSCP or Precedence
                ''',
                'type',
                'Cisco-IOS-XR-snmp-agent-cfg', False),
            _MetaInfoClassMember('precedence', REFERENCE_UNION, 'str', 'Snmp-precedence-value1',
                None, None,
                [], [],
                '''                SNMP Precedence value
                ''',
                'precedence',
                'Cisco-IOS-XR-snmp-agent-cfg', False, [
                    _MetaInfoClassMember('precedence', REFERENCE_ENUM_CLASS, 'SnmpPrecedenceValue1', 'enumeration',
                        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg', 'SnmpPrecedenceValue1',
                        [], [],
                        '''                        SNMP Precedence value
                        ''',
                        'precedence',
                        'Cisco-IOS-XR-snmp-agent-cfg', False, has_when=True),
                    _MetaInfoClassMember('precedence', ATTRIBUTE, 'int', 'uint32',
                        None, None,
                        [('0', '7')], [],
                        '''                        SNMP Precedence value
                        ''',
                        'precedence',
                        'Cisco-IOS-XR-snmp-agent-cfg', False, has_when=True),
                ], has_when=True),
            _MetaInfoClassMember('dscp', REFERENCE_UNION, 'str', 'Snmp-dscp-value',
                None, None,
                [], [],
                '''                SNMP DSCP value
                ''',
                'dscp',
                'Cisco-IOS-XR-snmp-agent-cfg', False, [
                    _MetaInfoClassMember('dscp', REFERENCE_ENUM_CLASS, 'SnmpDscpValue', 'enumeration',
                        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg', 'SnmpDscpValue',
                        [], [],
                        '''                        SNMP DSCP value
                        ''',
                        'dscp',
                        'Cisco-IOS-XR-snmp-agent-cfg', False, has_when=True),
                    _MetaInfoClassMember('dscp', ATTRIBUTE, 'int', 'uint32',
                        None, None,
                        [('0', '63')], [],
                        '''                        SNMP DSCP value
                        ''',
                        'dscp',
                        'Cisco-IOS-XR-snmp-agent-cfg', False, has_when=True),
                ], has_when=True),
            ],
            'Cisco-IOS-XR-snmp-agent-cfg',
            'tos',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-snmp-agent-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg',
        ),
    },
    'Snmp.Ipv6' : {
        'meta_info' : _MetaInfoClass('Snmp.Ipv6', REFERENCE_CLASS,
            '''SNMP TOS bit for outgoing packets''',
            False, 
            [
            _MetaInfoClassMember('tos', REFERENCE_CLASS, 'Tos', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg', 'Snmp.Ipv6.Tos',
                [], [],
                '''                Type of TOS
                ''',
                'tos',
                'Cisco-IOS-XR-snmp-agent-cfg', False),
            ],
            'Cisco-IOS-XR-snmp-agent-cfg',
            'ipv6',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-snmp-agent-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg',
        ),
    },
    'Snmp.Ipv4.Tos' : {
        'meta_info' : _MetaInfoClass('Snmp.Ipv4.Tos', REFERENCE_CLASS,
            '''Type of TOS''',
            False, 
            [
            _MetaInfoClassMember('type', REFERENCE_ENUM_CLASS, 'SnmpTos', 'Snmp-tos',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg', 'SnmpTos',
                [], [],
                '''                SNMP TOS type DSCP or Precedence
                ''',
                'type',
                'Cisco-IOS-XR-snmp-agent-cfg', False),
            _MetaInfoClassMember('precedence', REFERENCE_UNION, 'str', 'Snmp-precedence-value1',
                None, None,
                [], [],
                '''                SNMP Precedence value
                ''',
                'precedence',
                'Cisco-IOS-XR-snmp-agent-cfg', False, [
                    _MetaInfoClassMember('precedence', REFERENCE_ENUM_CLASS, 'SnmpPrecedenceValue1', 'enumeration',
                        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg', 'SnmpPrecedenceValue1',
                        [], [],
                        '''                        SNMP Precedence value
                        ''',
                        'precedence',
                        'Cisco-IOS-XR-snmp-agent-cfg', False, has_when=True),
                    _MetaInfoClassMember('precedence', ATTRIBUTE, 'int', 'uint32',
                        None, None,
                        [('0', '7')], [],
                        '''                        SNMP Precedence value
                        ''',
                        'precedence',
                        'Cisco-IOS-XR-snmp-agent-cfg', False, has_when=True),
                ], has_when=True),
            _MetaInfoClassMember('dscp', REFERENCE_UNION, 'str', 'Snmp-dscp-value',
                None, None,
                [], [],
                '''                SNMP DSCP value
                ''',
                'dscp',
                'Cisco-IOS-XR-snmp-agent-cfg', False, [
                    _MetaInfoClassMember('dscp', REFERENCE_ENUM_CLASS, 'SnmpDscpValue', 'enumeration',
                        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg', 'SnmpDscpValue',
                        [], [],
                        '''                        SNMP DSCP value
                        ''',
                        'dscp',
                        'Cisco-IOS-XR-snmp-agent-cfg', False, has_when=True),
                    _MetaInfoClassMember('dscp', ATTRIBUTE, 'int', 'uint32',
                        None, None,
                        [('0', '63')], [],
                        '''                        SNMP DSCP value
                        ''',
                        'dscp',
                        'Cisco-IOS-XR-snmp-agent-cfg', False, has_when=True),
                ], has_when=True),
            ],
            'Cisco-IOS-XR-snmp-agent-cfg',
            'tos',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-snmp-agent-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg',
        ),
    },
    'Snmp.Ipv4' : {
        'meta_info' : _MetaInfoClass('Snmp.Ipv4', REFERENCE_CLASS,
            '''SNMP TOS bit for outgoing packets''',
            False, 
            [
            _MetaInfoClassMember('tos', REFERENCE_CLASS, 'Tos', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg', 'Snmp.Ipv4.Tos',
                [], [],
                '''                Type of TOS
                ''',
                'tos',
                'Cisco-IOS-XR-snmp-agent-cfg', False),
            ],
            'Cisco-IOS-XR-snmp-agent-cfg',
            'ipv4',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-snmp-agent-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg',
        ),
    },
    'Snmp.System' : {
        'meta_info' : _MetaInfoClass('Snmp.System', REFERENCE_CLASS,
            '''container to hold system information''',
            False, 
            [
            _MetaInfoClassMember('chassis-id', ATTRIBUTE, 'str', 'string',
                None, None,
                [(1, 255)], [],
                '''                String to uniquely identify this chassis
                ''',
                'chassis_id',
                'Cisco-IOS-XR-snmp-agent-cfg', False),
            _MetaInfoClassMember('location', ATTRIBUTE, 'str', 'string',
                None, None,
                [(1, 255)], [],
                '''                The physical location of this node
                ''',
                'location',
                'Cisco-IOS-XR-snmp-agent-cfg', False),
            _MetaInfoClassMember('contact', ATTRIBUTE, 'str', 'string',
                None, None,
                [(1, 255)], [],
                '''                identification of the contact person for this
                managed node
                ''',
                'contact',
                'Cisco-IOS-XR-snmp-agent-cfg', False),
            ],
            'Cisco-IOS-XR-snmp-agent-cfg',
            'system',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-snmp-agent-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg',
        ),
    },
    'Snmp.Target.Targets.Target_.VrfNames.VrfName' : {
        'meta_info' : _MetaInfoClass('Snmp.Target.Targets.Target_.VrfNames.VrfName', REFERENCE_LIST,
            '''VRF name of the target''',
            False, 
            [
            _MetaInfoClassMember('name', ATTRIBUTE, 'str', 'xr:Cisco-ios-xr-string',
                None, None,
                [], [b'[\\w\\-\\.:,_@#%$\\+=\\|;]+'],
                '''                VRF Name
                ''',
                'name',
                'Cisco-IOS-XR-snmp-agent-cfg', True),
            ],
            'Cisco-IOS-XR-snmp-agent-cfg',
            'vrf-name',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-snmp-agent-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg',
        ),
    },
    'Snmp.Target.Targets.Target_.VrfNames' : {
        'meta_info' : _MetaInfoClass('Snmp.Target.Targets.Target_.VrfNames', REFERENCE_CLASS,
            '''List of VRF Name for a target list''',
            False, 
            [
            _MetaInfoClassMember('vrf-name', REFERENCE_LIST, 'VrfName', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg', 'Snmp.Target.Targets.Target_.VrfNames.VrfName',
                [], [],
                '''                VRF name of the target
                ''',
                'vrf_name',
                'Cisco-IOS-XR-snmp-agent-cfg', False),
            ],
            'Cisco-IOS-XR-snmp-agent-cfg',
            'vrf-names',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-snmp-agent-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg',
        ),
    },
    'Snmp.Target.Targets.Target_.TargetAddresses.TargetAddress' : {
        'meta_info' : _MetaInfoClass('Snmp.Target.Targets.Target_.TargetAddresses.TargetAddress', REFERENCE_LIST,
            '''IP Address to be configured for the Target''',
            False, 
            [
            _MetaInfoClassMember('ip-address', REFERENCE_UNION, 'str', 'inet:ip-address-no-zone',
                None, None,
                [], [],
                '''                IPv4/Ipv6 address
                ''',
                'ip_address',
                'Cisco-IOS-XR-snmp-agent-cfg', True, [
                    _MetaInfoClassMember('ip-address', ATTRIBUTE, 'str', 'inet:ipv4-address-no-zone',
                        None, None,
                        [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'],
                        '''                        IPv4/Ipv6 address
                        ''',
                        'ip_address',
                        'Cisco-IOS-XR-snmp-agent-cfg', True),
                    _MetaInfoClassMember('ip-address', ATTRIBUTE, 'str', 'inet:ipv6-address-no-zone',
                        None, None,
                        [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'],
                        '''                        IPv4/Ipv6 address
                        ''',
                        'ip_address',
                        'Cisco-IOS-XR-snmp-agent-cfg', True),
                ]),
            ],
            'Cisco-IOS-XR-snmp-agent-cfg',
            'target-address',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-snmp-agent-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg',
        ),
    },
    'Snmp.Target.Targets.Target_.TargetAddresses' : {
        'meta_info' : _MetaInfoClass('Snmp.Target.Targets.Target_.TargetAddresses', REFERENCE_CLASS,
            '''SNMP Target address configurations''',
            False, 
            [
            _MetaInfoClassMember('target-address', REFERENCE_LIST, 'TargetAddress', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg', 'Snmp.Target.Targets.Target_.TargetAddresses.TargetAddress',
                [], [],
                '''                IP Address to be configured for the Target
                ''',
                'target_address',
                'Cisco-IOS-XR-snmp-agent-cfg', False),
            ],
            'Cisco-IOS-XR-snmp-agent-cfg',
            'target-addresses',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-snmp-agent-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg',
        ),
    },
    'Snmp.Target.Targets.Target_' : {
        'meta_info' : _MetaInfoClass('Snmp.Target.Targets.Target_', REFERENCE_LIST,
            '''Name of the target list''',
            False, 
            [
            _MetaInfoClassMember('target-list-name', ATTRIBUTE, 'str', 'xr:Cisco-ios-xr-string',
                None, None,
                [], [b'[\\w\\-\\.:,_@#%$\\+=\\|;]+'],
                '''                Name of the target list
                ''',
                'target_list_name',
                'Cisco-IOS-XR-snmp-agent-cfg', True),
            _MetaInfoClassMember('vrf-names', REFERENCE_CLASS, 'VrfNames', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg', 'Snmp.Target.Targets.Target_.VrfNames',
                [], [],
                '''                List of VRF Name for a target list
                ''',
                'vrf_names',
                'Cisco-IOS-XR-snmp-agent-cfg', False),
            _MetaInfoClassMember('target-addresses', REFERENCE_CLASS, 'TargetAddresses', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg', 'Snmp.Target.Targets.Target_.TargetAddresses',
                [], [],
                '''                SNMP Target address configurations
                ''',
                'target_addresses',
                'Cisco-IOS-XR-snmp-agent-cfg', False),
            ],
            'Cisco-IOS-XR-snmp-agent-cfg',
            'target',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-snmp-agent-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg',
        ),
    },
    'Snmp.Target.Targets' : {
        'meta_info' : _MetaInfoClass('Snmp.Target.Targets', REFERENCE_CLASS,
            '''List of targets''',
            False, 
            [
            _MetaInfoClassMember('target', REFERENCE_LIST, 'Target_', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg', 'Snmp.Target.Targets.Target_',
                [], [],
                '''                Name of the target list
                ''',
                'target',
                'Cisco-IOS-XR-snmp-agent-cfg', False),
            ],
            'Cisco-IOS-XR-snmp-agent-cfg',
            'targets',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-snmp-agent-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg',
        ),
    },
    'Snmp.Target' : {
        'meta_info' : _MetaInfoClass('Snmp.Target', REFERENCE_CLASS,
            '''SNMP target configurations''',
            False, 
            [
            _MetaInfoClassMember('targets', REFERENCE_CLASS, 'Targets', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg', 'Snmp.Target.Targets',
                [], [],
                '''                List of targets
                ''',
                'targets',
                'Cisco-IOS-XR-snmp-agent-cfg', False),
            ],
            'Cisco-IOS-XR-snmp-agent-cfg',
            'target',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-snmp-agent-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg',
        ),
    },
    'Snmp.Notification.Snmp_' : {
        'meta_info' : _MetaInfoClass('Snmp.Notification.Snmp_', REFERENCE_CLASS,
            '''SNMP notification configuration''',
            False, 
            [
            _MetaInfoClassMember('authentication', ATTRIBUTE, 'Empty', 'empty',
                None, None,
                [], [],
                '''                Enable authentication notification
                ''',
                'authentication',
                'Cisco-IOS-XR-snmp-agent-cfg', False),
            _MetaInfoClassMember('cold-start', ATTRIBUTE, 'Empty', 'empty',
                None, None,
                [], [],
                '''                Enable cold start notification
                ''',
                'cold_start',
                'Cisco-IOS-XR-snmp-agent-cfg', False),
            _MetaInfoClassMember('warm-start', ATTRIBUTE, 'Empty', 'empty',
                None, None,
                [], [],
                '''                Enable warm start notification
                ''',
                'warm_start',
                'Cisco-IOS-XR-snmp-agent-cfg', False),
            _MetaInfoClassMember('enable', ATTRIBUTE, 'Empty', 'empty',
                None, None,
                [], [],
                '''                Enable SNMP notifications
                ''',
                'enable',
                'Cisco-IOS-XR-snmp-agent-cfg', False),
            _MetaInfoClassMember('link-down', ATTRIBUTE, 'Empty', 'empty',
                None, None,
                [], [],
                '''                Enable link down notification
                ''',
                'link_down',
                'Cisco-IOS-XR-snmp-ifmib-cfg', False),
            _MetaInfoClassMember('link-up', ATTRIBUTE, 'Empty', 'empty',
                None, None,
                [], [],
                '''                Enable link up notification
                ''',
                'link_up',
                'Cisco-IOS-XR-snmp-ifmib-cfg', False),
            ],
            'Cisco-IOS-XR-snmp-agent-cfg',
            'snmp',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-snmp-agent-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg',
        ),
    },
    'Snmp.Notification.SelectiveVrfDownload' : {
        'meta_info' : _MetaInfoClass('Snmp.Notification.SelectiveVrfDownload', REFERENCE_CLASS,
            '''CISCO-SELECTIVE-VRF-DOWNLOAD-MIB notification
configuration''',
            False, 
            [
            _MetaInfoClassMember('role-change', ATTRIBUTE, 'Empty', 'empty',
                None, None,
                [], [],
                '''                Enable csvdEntityRoleChangeNotification
                notification
                ''',
                'role_change',
                'Cisco-IOS-XR-infra-rsi-cfg', False),
            ],
            'Cisco-IOS-XR-infra-rsi-cfg',
            'selective-vrf-download',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-infra-rsi-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg',
        ),
    },
    'Snmp.Notification.Vpls' : {
        'meta_info' : _MetaInfoClass('Snmp.Notification.Vpls', REFERENCE_CLASS,
            '''CISCO-IETF-VPLS-GENERIC-MIB notification
configuration''',
            False, 
            [
            _MetaInfoClassMember('full-clear', ATTRIBUTE, 'Empty', 'empty',
                None, None,
                [], [],
                '''                Enable cvplsFwdFullAlarmCleared notification
                ''',
                'full_clear',
                'Cisco-IOS-XR-l2vpn-cfg', False),
            _MetaInfoClassMember('status', ATTRIBUTE, 'Empty', 'empty',
                None, None,
                [], [],
                '''                Enable cvplsStatusChanged notification
                ''',
                'status',
                'Cisco-IOS-XR-l2vpn-cfg', False),
            _MetaInfoClassMember('enable', ATTRIBUTE, 'Empty', 'empty',
                None, None,
                [], [],
                '''                Enable CISCO-IETF-VPLS-GENERIC-MIB
                notifications
                ''',
                'enable',
                'Cisco-IOS-XR-l2vpn-cfg', False),
            _MetaInfoClassMember('full-raise', ATTRIBUTE, 'Empty', 'empty',
                None, None,
                [], [],
                '''                Enable cvplsFwdFullAlarmRaised notification
                ''',
                'full_raise',
                'Cisco-IOS-XR-l2vpn-cfg', False),
            ],
            'Cisco-IOS-XR-l2vpn-cfg',
            'vpls',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-l2vpn-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg',
        ),
    },
    'Snmp.Notification.L2vpn' : {
        'meta_info' : _MetaInfoClass('Snmp.Notification.L2vpn', REFERENCE_CLASS,
            '''CISCO-IETF-PW-MIB notification configuration''',
            False, 
            [
            _MetaInfoClassMember('cisco', ATTRIBUTE, 'Empty', 'empty',
                None, None,
                [], [],
                '''                Enable Cisco format including extra varbinds
                ''',
                'cisco',
                'Cisco-IOS-XR-l2vpn-cfg', False),
            _MetaInfoClassMember('enable', ATTRIBUTE, 'Empty', 'empty',
                None, None,
                [], [],
                '''                Enable CISCO-IETF-PW-MIB notifications
                ''',
                'enable',
                'Cisco-IOS-XR-l2vpn-cfg', False),
            _MetaInfoClassMember('vc-down', ATTRIBUTE, 'Empty', 'empty',
                None, None,
                [], [],
                '''                Enable cpwVcDown notification
                ''',
                'vc_down',
                'Cisco-IOS-XR-l2vpn-cfg', False),
            _MetaInfoClassMember('vc-up', ATTRIBUTE, 'Empty', 'empty',
                None, None,
                [], [],
                '''                Enable cpwVcUp notification
                ''',
                'vc_up',
                'Cisco-IOS-XR-l2vpn-cfg', False),
            ],
            'Cisco-IOS-XR-l2vpn-cfg',
            'l2vpn',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-l2vpn-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg',
        ),
    },
    'Snmp.Notification.Entity' : {
        'meta_info' : _MetaInfoClass('Snmp.Notification.Entity', REFERENCE_CLASS,
            '''Enable ENTITY-MIB notifications''',
            False, 
            [
            _MetaInfoClassMember('enable', ATTRIBUTE, 'Empty', 'empty',
                None, None,
                [], [],
                '''                Enable entityMIB notifications
                ''',
                'enable',
                'Cisco-IOS-XR-snmp-entitymib-cfg', False),
            ],
            'Cisco-IOS-XR-snmp-entitymib-cfg',
            'entity',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-snmp-entitymib-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg',
        ),
    },
    'Snmp.Notification.Bridge' : {
        'meta_info' : _MetaInfoClass('Snmp.Notification.Bridge', REFERENCE_CLASS,
            '''BRIDGE-MIB notification configuration''',
            False, 
            [
            _MetaInfoClassMember('enable', ATTRIBUTE, 'Empty', 'empty',
                None, None,
                [], [],
                '''                Enable dot1dBridge notifications
                ''',
                'enable',
                'Cisco-IOS-XR-snmp-bridgemib-cfg', False),
            ],
            'Cisco-IOS-XR-snmp-bridgemib-cfg',
            'bridge',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-snmp-bridgemib-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg',
        ),
    },
    'Snmp.Notification.Rf' : {
        'meta_info' : _MetaInfoClass('Snmp.Notification.Rf', REFERENCE_CLASS,
            '''CISCO-RF-MIB notification configuration''',
            False, 
            [
            _MetaInfoClassMember('enable', ATTRIBUTE, 'Empty', 'empty',
                None, None,
                [], [],
                '''                Enable ciscoRFMIB notifications
                ''',
                'enable',
                'Cisco-IOS-XR-snmp-mib-rfmib-cfg', False),
            ],
            'Cisco-IOS-XR-snmp-mib-rfmib-cfg',
            'rf',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-snmp-mib-rfmib-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg',
        ),
    },
    'Snmp.Notification.Ntp' : {
        'meta_info' : _MetaInfoClass('Snmp.Notification.Ntp', REFERENCE_CLASS,
            '''CISCO-NTP-MIB notification configuration''',
            False, 
            [
            _MetaInfoClassMember('enable', ATTRIBUTE, 'Empty', 'empty',
                None, None,
                [], [],
                '''                Enable ciscoNtpMIB notification configuration
                ''',
                'enable',
                'Cisco-IOS-XR-ip-ntp-cfg', False),
            ],
            'Cisco-IOS-XR-ip-ntp-cfg',
            'ntp',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-ip-ntp-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg',
        ),
    },
    'Snmp.Notification.Otn' : {
        'meta_info' : _MetaInfoClass('Snmp.Notification.Otn', REFERENCE_CLASS,
            '''CISCO-OTN-IF-MIB notification configuration''',
            False, 
            [
            _MetaInfoClassMember('enable', ATTRIBUTE, 'Empty', 'empty',
                None, None,
                [], [],
                '''                Enable ciscoOtnIfMIB notifications
                ''',
                'enable',
                'Cisco-IOS-XR-otnifmib-cfg', False),
            ],
            'Cisco-IOS-XR-otnifmib-cfg',
            'otn',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-otnifmib-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg',
        ),
    },
    'Snmp.Notification.AddresspoolMib' : {
        'meta_info' : _MetaInfoClass('Snmp.Notification.AddresspoolMib', REFERENCE_CLASS,
            '''Enable SNMP daps traps''',
            False, 
            [
            _MetaInfoClassMember('high', ATTRIBUTE, 'bool', 'boolean',
                None, None,
                [], [],
                '''                Enable SNMP Address Pool High Threshold trap
                ''',
                'high',
                'Cisco-IOS-XR-ip-daps-mib-cfg', False),
            _MetaInfoClassMember('low', ATTRIBUTE, 'bool', 'boolean',
                None, None,
                [], [],
                '''                Enable SNMP Address Pool Low Threshold trap
                ''',
                'low',
                'Cisco-IOS-XR-ip-daps-mib-cfg', False),
            ],
            'Cisco-IOS-XR-ip-daps-mib-cfg',
            'addresspool-mib',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-ip-daps-mib-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg',
        ),
    },
    'Snmp.Notification.System' : {
        'meta_info' : _MetaInfoClass('Snmp.Notification.System', REFERENCE_CLASS,
            '''CISCO-SYSTEM-MIB notification configuration''',
            False, 
            [
            _MetaInfoClassMember('enable', ATTRIBUTE, 'Empty', 'empty',
                None, None,
                [], [],
                '''                Enable ciscoSystemMIB notifications
                ''',
                'enable',
                'Cisco-IOS-XR-infra-systemmib-cfg', False),
            ],
            'Cisco-IOS-XR-infra-systemmib-cfg',
            'system',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-infra-systemmib-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg',
        ),
    },
    'Snmp.Notification.Rsvp' : {
        'meta_info' : _MetaInfoClass('Snmp.Notification.Rsvp', REFERENCE_CLASS,
            '''Enable RSVP-MIB notifications''',
            False, 
            [
            _MetaInfoClassMember('lost-flow', ATTRIBUTE, 'Empty', 'empty',
                None, None,
                [], [],
                '''                Enable lostFlow notification
                ''',
                'lost_flow',
                'Cisco-IOS-XR-ip-rsvp-cfg', False),
            _MetaInfoClassMember('new-flow', ATTRIBUTE, 'Empty', 'empty',
                None, None,
                [], [],
                '''                Enable newFlow notification
                ''',
                'new_flow',
                'Cisco-IOS-XR-ip-rsvp-cfg', False),
            _MetaInfoClassMember('enable', ATTRIBUTE, 'Empty', 'empty',
                None, None,
                [], [],
                '''                Enable all RSVP notifications
                ''',
                'enable',
                'Cisco-IOS-XR-ip-rsvp-cfg', False),
            ],
            'Cisco-IOS-XR-ip-rsvp-cfg',
            'rsvp',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-ip-rsvp-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg',
        ),
    },
    'Snmp.Notification.Sensor' : {
        'meta_info' : _MetaInfoClass('Snmp.Notification.Sensor', REFERENCE_CLASS,
            '''CISCO-ENTITY-SENSOR-MIB notification
configuration''',
            False, 
            [
            _MetaInfoClassMember('enable', ATTRIBUTE, 'Empty', 'empty',
                None, None,
                [], [],
                '''                Enable entitySensorMIB notifications
                ''',
                'enable',
                'Cisco-IOS-XR-snmp-ciscosensormib-cfg', False),
            ],
            'Cisco-IOS-XR-snmp-ciscosensormib-cfg',
            'sensor',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-snmp-ciscosensormib-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg',
        ),
    },
    'Snmp.Notification.MplsLdp' : {
        'meta_info' : _MetaInfoClass('Snmp.Notification.MplsLdp', REFERENCE_CLASS,
            '''MPLS-LDP-STD-MIB notification configuration''',
            False, 
            [
            _MetaInfoClassMember('session-up', ATTRIBUTE, 'Empty', 'empty',
                None, None,
                [], [],
                '''                Enable mplsLdpSessionUp notification
                ''',
                'session_up',
                'Cisco-IOS-XR-mpls-ldp-cfg', False),
            _MetaInfoClassMember('init-session-threshold-exceeded', ATTRIBUTE, 'Empty', 'empty',
                None, None,
                [], [],
                '''                Enable mplsLdpInitSessionThresholdExceeded
                notification
                ''',
                'init_session_threshold_exceeded',
                'Cisco-IOS-XR-mpls-ldp-cfg', False),
            _MetaInfoClassMember('session-down', ATTRIBUTE, 'Empty', 'empty',
                None, None,
                [], [],
                '''                Enable mplsLdpSessionDown notification
                ''',
                'session_down',
                'Cisco-IOS-XR-mpls-ldp-cfg', False),
            ],
            'Cisco-IOS-XR-mpls-ldp-cfg',
            'mpls-ldp',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-mpls-ldp-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg',
        ),
    },
    'Snmp.Notification.SubscriberMib.SessionAggregate' : {
        'meta_info' : _MetaInfoClass('Snmp.Notification.SubscriberMib.SessionAggregate', REFERENCE_CLASS,
            '''Session aggregation''',
            False, 
            [
            _MetaInfoClassMember('node', ATTRIBUTE, 'Empty', 'empty',
                None, None,
                [], [],
                '''                Subscriber notification at node level
                ''',
                'node',
                'Cisco-IOS-XR-subscriber-session-mon-mibs-cfg', False),
            _MetaInfoClassMember('access-interface', ATTRIBUTE, 'Empty', 'empty',
                None, None,
                [], [],
                '''                Subscriber notification at access interface
                level
                ''',
                'access_interface',
                'Cisco-IOS-XR-subscriber-session-mon-mibs-cfg', False),
            ],
            'Cisco-IOS-XR-subscriber-session-mon-mibs-cfg',
            'session-aggregate',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-subscriber-session-mon-mibs-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg',
        ),
    },
    'Snmp.Notification.SubscriberMib' : {
        'meta_info' : _MetaInfoClass('Snmp.Notification.SubscriberMib', REFERENCE_CLASS,
            '''Subscriber notification commands''',
            False, 
            [
            _MetaInfoClassMember('session-aggregate', REFERENCE_CLASS, 'SessionAggregate', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg', 'Snmp.Notification.SubscriberMib.SessionAggregate',
                [], [],
                '''                Session aggregation
                ''',
                'session_aggregate',
                'Cisco-IOS-XR-subscriber-session-mon-mibs-cfg', False),
            ],
            'Cisco-IOS-XR-subscriber-session-mon-mibs-cfg',
            'subscriber-mib',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-subscriber-session-mon-mibs-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg',
        ),
    },
    'Snmp.Notification.Flash' : {
        'meta_info' : _MetaInfoClass('Snmp.Notification.Flash', REFERENCE_CLASS,
            '''CISCO-FLASH-MIB notification configuration''',
            False, 
            [
            _MetaInfoClassMember('insertion', ATTRIBUTE, 'Empty', 'empty',
                None, None,
                [], [],
                '''                Enable ciscoFlashDeviceInsertedNotif
                notification
                ''',
                'insertion',
                'Cisco-IOS-XR-flashmib-cfg', False),
            _MetaInfoClassMember('removal', ATTRIBUTE, 'Empty', 'empty',
                None, None,
                [], [],
                '''                Enable ciscoFlashDeviceRemovedNotif
                notification
                ''',
                'removal',
                'Cisco-IOS-XR-flashmib-cfg', False),
            ],
            'Cisco-IOS-XR-flashmib-cfg',
            'flash',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-flashmib-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg',
        ),
    },
    'Snmp.Notification.ConfigCopy' : {
        'meta_info' : _MetaInfoClass('Snmp.Notification.ConfigCopy', REFERENCE_CLASS,
            '''CISCO-CONFIG-COPY-MIB notification configuration''',
            False, 
            [
            _MetaInfoClassMember('completion', ATTRIBUTE, 'Empty', 'empty',
                None, None,
                [], [],
                '''                Enable ccCopyCompletion notification
                ''',
                'completion',
                'Cisco-IOS-XR-infra-confcopymib-cfg', False),
            ],
            'Cisco-IOS-XR-infra-confcopymib-cfg',
            'config-copy',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-infra-confcopymib-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg',
        ),
    },
    'Snmp.Notification.Hsrp' : {
        'meta_info' : _MetaInfoClass('Snmp.Notification.Hsrp', REFERENCE_CLASS,
            '''CISCO-HSRP-MIB notification configuration''',
            False, 
            [
            _MetaInfoClassMember('enable', ATTRIBUTE, 'Empty', 'empty',
                None, None,
                [], [],
                '''                Enable CISCO-HSRP-MIB notifications
                ''',
                'enable',
                'Cisco-IOS-XR-ipv4-hsrp-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-hsrp-cfg',
            'hsrp',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-ipv4-hsrp-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg',
        ),
    },
    'Snmp.Notification.EntityRedundancy' : {
        'meta_info' : _MetaInfoClass('Snmp.Notification.EntityRedundancy', REFERENCE_CLASS,
            '''CISCO-ENTITY-REDUNDANCY-MIB notification
configuration''',
            False, 
            [
            _MetaInfoClassMember('switchover', ATTRIBUTE, 'Empty', 'empty',
                None, None,
                [], [],
                '''                Enable switchover notification
                ''',
                'switchover',
                'Cisco-IOS-XR-infra-ceredundancymib-cfg', False),
            _MetaInfoClassMember('enable', ATTRIBUTE, 'Empty', 'empty',
                None, None,
                [], [],
                '''                Enable CISCO-ENTITY-REDUNDANCY-MIB notification
                ''',
                'enable',
                'Cisco-IOS-XR-infra-ceredundancymib-cfg', False),
            _MetaInfoClassMember('status', ATTRIBUTE, 'Empty', 'empty',
                None, None,
                [], [],
                '''                Enable status change notification
                ''',
                'status',
                'Cisco-IOS-XR-infra-ceredundancymib-cfg', False),
            ],
            'Cisco-IOS-XR-infra-ceredundancymib-cfg',
            'entity-redundancy',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-infra-ceredundancymib-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg',
        ),
    },
    'Snmp.Notification.Isis' : {
        'meta_info' : _MetaInfoClass('Snmp.Notification.Isis', REFERENCE_CLASS,
            '''Enable ISIS-MIB notifications''',
            False, 
            [
            _MetaInfoClassMember('database-overflow', REFERENCE_ENUM_CLASS, 'IsisMibDatabaseOverFlowBoolean', 'Isis-mib-database-over-flow-boolean',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'IsisMibDatabaseOverFlowBoolean',
                [], [],
                '''                Enable or disable
                ''',
                'database_overflow',
                'Cisco-IOS-XR-clns-isis-cfg', False, default_value='Cisco_IOS_XR_clns_isis_cfg.IsisMibDatabaseOverFlowBoolean.false'),
            _MetaInfoClassMember('manual-address-drops', REFERENCE_ENUM_CLASS, 'IsisMibManualAddressDropsBoolean', 'Isis-mib-manual-address-drops-boolean',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'IsisMibManualAddressDropsBoolean',
                [], [],
                '''                Enable or disable
                ''',
                'manual_address_drops',
                'Cisco-IOS-XR-clns-isis-cfg', False, default_value='Cisco_IOS_XR_clns_isis_cfg.IsisMibManualAddressDropsBoolean.false'),
            _MetaInfoClassMember('corrupted-lsp-detected', REFERENCE_ENUM_CLASS, 'IsisMibCorruptedLspDetectedBoolean', 'Isis-mib-corrupted-lsp-detected-boolean',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'IsisMibCorruptedLspDetectedBoolean',
                [], [],
                '''                Enable or disable
                ''',
                'corrupted_lsp_detected',
                'Cisco-IOS-XR-clns-isis-cfg', False, default_value='Cisco_IOS_XR_clns_isis_cfg.IsisMibCorruptedLspDetectedBoolean.false'),
            _MetaInfoClassMember('attempt-to-exceed-max-sequence', REFERENCE_ENUM_CLASS, 'IsisMibAttemptToExceedMaxSequenceBoolean', 'Isis-mib-attempt-to-exceed-max-sequence-boolean',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'IsisMibAttemptToExceedMaxSequenceBoolean',
                [], [],
                '''                Enable or disable
                ''',
                'attempt_to_exceed_max_sequence',
                'Cisco-IOS-XR-clns-isis-cfg', False, default_value='Cisco_IOS_XR_clns_isis_cfg.IsisMibAttemptToExceedMaxSequenceBoolean.false'),
            _MetaInfoClassMember('id-length-mismatch', REFERENCE_ENUM_CLASS, 'IsisMibIdLengthMismatchBoolean', 'Isis-mib-id-length-mismatch-boolean',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'IsisMibIdLengthMismatchBoolean',
                [], [],
                '''                Enable or disable
                ''',
                'id_length_mismatch',
                'Cisco-IOS-XR-clns-isis-cfg', False, default_value='Cisco_IOS_XR_clns_isis_cfg.IsisMibIdLengthMismatchBoolean.false'),
            _MetaInfoClassMember('max-area-address-mismatch', REFERENCE_ENUM_CLASS, 'IsisMibMaxAreaAddressMismatchBoolean', 'Isis-mib-max-area-address-mismatch-boolean',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'IsisMibMaxAreaAddressMismatchBoolean',
                [], [],
                '''                Enable or disable
                ''',
                'max_area_address_mismatch',
                'Cisco-IOS-XR-clns-isis-cfg', False, default_value='Cisco_IOS_XR_clns_isis_cfg.IsisMibMaxAreaAddressMismatchBoolean.false'),
            _MetaInfoClassMember('own-lsp-purge', REFERENCE_ENUM_CLASS, 'IsisMibOwnLspPurgeBoolean', 'Isis-mib-own-lsp-purge-boolean',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'IsisMibOwnLspPurgeBoolean',
                [], [],
                '''                Enable or disable
                ''',
                'own_lsp_purge',
                'Cisco-IOS-XR-clns-isis-cfg', False, default_value='Cisco_IOS_XR_clns_isis_cfg.IsisMibOwnLspPurgeBoolean.false'),
            _MetaInfoClassMember('sequence-number-skip', REFERENCE_ENUM_CLASS, 'IsisMibSequenceNumberSkipBoolean', 'Isis-mib-sequence-number-skip-boolean',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'IsisMibSequenceNumberSkipBoolean',
                [], [],
                '''                Enable or disable
                ''',
                'sequence_number_skip',
                'Cisco-IOS-XR-clns-isis-cfg', False, default_value='Cisco_IOS_XR_clns_isis_cfg.IsisMibSequenceNumberSkipBoolean.false'),
            _MetaInfoClassMember('authentication-type-failure', REFERENCE_ENUM_CLASS, 'IsisMibAuthenticationTypeFailureBoolean', 'Isis-mib-authentication-type-failure-boolean',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'IsisMibAuthenticationTypeFailureBoolean',
                [], [],
                '''                Enable or disable
                ''',
                'authentication_type_failure',
                'Cisco-IOS-XR-clns-isis-cfg', False, default_value='Cisco_IOS_XR_clns_isis_cfg.IsisMibAuthenticationTypeFailureBoolean.false'),
            _MetaInfoClassMember('authentication-failure', REFERENCE_ENUM_CLASS, 'IsisMibAuthenticationFailureBoolean', 'Isis-mib-authentication-failure-boolean',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'IsisMibAuthenticationFailureBoolean',
                [], [],
                '''                Enable or disable
                ''',
                'authentication_failure',
                'Cisco-IOS-XR-clns-isis-cfg', False, default_value='Cisco_IOS_XR_clns_isis_cfg.IsisMibAuthenticationFailureBoolean.false'),
            _MetaInfoClassMember('version-skew', REFERENCE_ENUM_CLASS, 'IsisMibVersionSkewBoolean', 'Isis-mib-version-skew-boolean',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'IsisMibVersionSkewBoolean',
                [], [],
                '''                Enable or disable
                ''',
                'version_skew',
                'Cisco-IOS-XR-clns-isis-cfg', False, default_value='Cisco_IOS_XR_clns_isis_cfg.IsisMibVersionSkewBoolean.false'),
            _MetaInfoClassMember('area-mismatch', REFERENCE_ENUM_CLASS, 'IsisMibAreaMismatchBoolean', 'Isis-mib-area-mismatch-boolean',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'IsisMibAreaMismatchBoolean',
                [], [],
                '''                Enable or disable
                ''',
                'area_mismatch',
                'Cisco-IOS-XR-clns-isis-cfg', False, default_value='Cisco_IOS_XR_clns_isis_cfg.IsisMibAreaMismatchBoolean.false'),
            _MetaInfoClassMember('rejected-adjacency', REFERENCE_ENUM_CLASS, 'IsisMibRejectedAdjacencyBoolean', 'Isis-mib-rejected-adjacency-boolean',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'IsisMibRejectedAdjacencyBoolean',
                [], [],
                '''                Enable or disable
                ''',
                'rejected_adjacency',
                'Cisco-IOS-XR-clns-isis-cfg', False, default_value='Cisco_IOS_XR_clns_isis_cfg.IsisMibRejectedAdjacencyBoolean.false'),
            _MetaInfoClassMember('lsp-too-large-to-propagate', REFERENCE_ENUM_CLASS, 'IsisMibLspTooLargeToPropagateBoolean', 'Isis-mib-lsp-too-large-to-propagate-boolean',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'IsisMibLspTooLargeToPropagateBoolean',
                [], [],
                '''                Enable or disable
                ''',
                'lsp_too_large_to_propagate',
                'Cisco-IOS-XR-clns-isis-cfg', False, default_value='Cisco_IOS_XR_clns_isis_cfg.IsisMibLspTooLargeToPropagateBoolean.false'),
            _MetaInfoClassMember('originated-lsp-buffer-size-mismatch', REFERENCE_ENUM_CLASS, 'IsisMibOriginatedLspBufferSizeMismatchBoolean', 'Isis-mib-originated-lsp-buffer-size-mismatch-boolean',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'IsisMibOriginatedLspBufferSizeMismatchBoolean',
                [], [],
                '''                Enable or disable
                ''',
                'originated_lsp_buffer_size_mismatch',
                'Cisco-IOS-XR-clns-isis-cfg', False, default_value='Cisco_IOS_XR_clns_isis_cfg.IsisMibOriginatedLspBufferSizeMismatchBoolean.false'),
            _MetaInfoClassMember('protocols-supported-mismatch', REFERENCE_ENUM_CLASS, 'IsisMibProtocolsSupportedMismatchBoolean', 'Isis-mib-protocols-supported-mismatch-boolean',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'IsisMibProtocolsSupportedMismatchBoolean',
                [], [],
                '''                Enable or disable
                ''',
                'protocols_supported_mismatch',
                'Cisco-IOS-XR-clns-isis-cfg', False, default_value='Cisco_IOS_XR_clns_isis_cfg.IsisMibProtocolsSupportedMismatchBoolean.false'),
            _MetaInfoClassMember('adjacency-change', REFERENCE_ENUM_CLASS, 'IsisMibAdjacencyChangeBoolean', 'Isis-mib-adjacency-change-boolean',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'IsisMibAdjacencyChangeBoolean',
                [], [],
                '''                Enable or disable
                ''',
                'adjacency_change',
                'Cisco-IOS-XR-clns-isis-cfg', False, default_value='Cisco_IOS_XR_clns_isis_cfg.IsisMibAdjacencyChangeBoolean.false'),
            _MetaInfoClassMember('lsp-error-detected', REFERENCE_ENUM_CLASS, 'IsisMibLspErrorDetectedBoolean', 'Isis-mib-lsp-error-detected-boolean',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'IsisMibLspErrorDetectedBoolean',
                [], [],
                '''                Enable or disable
                ''',
                'lsp_error_detected',
                'Cisco-IOS-XR-clns-isis-cfg', False, default_value='Cisco_IOS_XR_clns_isis_cfg.IsisMibLspErrorDetectedBoolean.false'),
            _MetaInfoClassMember('all', REFERENCE_ENUM_CLASS, 'IsisMibAllBoolean', 'Isis-mib-all-boolean',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'IsisMibAllBoolean',
                [], [],
                '''                Enable all isisMIB notifications
                ''',
                'all',
                'Cisco-IOS-XR-clns-isis-cfg', False, default_value='Cisco_IOS_XR_clns_isis_cfg.IsisMibAllBoolean.false'),
            ],
            'Cisco-IOS-XR-clns-isis-cfg',
            'isis',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-clns-isis-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg',
        ),
    },
    'Snmp.Notification.Vrrp' : {
        'meta_info' : _MetaInfoClass('Snmp.Notification.Vrrp', REFERENCE_CLASS,
            '''VRRP-MIB notification configuration''',
            False, 
            [
            _MetaInfoClassMember('enable', ATTRIBUTE, 'Empty', 'empty',
                None, None,
                [], [],
                '''                Enable VRRP-MIB notifications
                ''',
                'enable',
                'Cisco-IOS-XR-ipv4-vrrp-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-vrrp-cfg',
            'vrrp',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-ipv4-vrrp-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg',
        ),
    },
    'Snmp.Notification.IpSec' : {
        'meta_info' : _MetaInfoClass('Snmp.Notification.IpSec', REFERENCE_CLASS,
            '''Enable CISCO-IPSEC-FLOW-MONITOR-MIB
notifications''',
            False, 
            [
            _MetaInfoClassMember('tunnel-stop', ATTRIBUTE, 'Empty', 'empty',
                None, None,
                [], [],
                '''                Enable cipSecTunnelStop notification
                ''',
                'tunnel_stop',
                'Cisco-IOS-XR-crypto-mibs-ipsecflowmon-cfg', False),
            _MetaInfoClassMember('tunnel-start', ATTRIBUTE, 'Empty', 'empty',
                None, None,
                [], [],
                '''                Enable cipSecTunnelStart notification
                ''',
                'tunnel_start',
                'Cisco-IOS-XR-crypto-mibs-ipsecflowmon-cfg', False),
            ],
            'Cisco-IOS-XR-crypto-mibs-ipsecflowmon-cfg',
            'ip-sec',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-crypto-mibs-ipsecflowmon-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg',
        ),
    },
    'Snmp.Notification.Isakmp' : {
        'meta_info' : _MetaInfoClass('Snmp.Notification.Isakmp', REFERENCE_CLASS,
            '''Enable CISCO-IPSEC-FLOW-MONITOR-MIB
notifications''',
            False, 
            [
            _MetaInfoClassMember('tunnel-stop', ATTRIBUTE, 'Empty', 'empty',
                None, None,
                [], [],
                '''                Enable cikeTunnelStop notification
                ''',
                'tunnel_stop',
                'Cisco-IOS-XR-crypto-mibs-ipsecflowmon-cfg', False),
            _MetaInfoClassMember('tunnel-start', ATTRIBUTE, 'Empty', 'empty',
                None, None,
                [], [],
                '''                Enable cikeTunnelStart notification
                ''',
                'tunnel_start',
                'Cisco-IOS-XR-crypto-mibs-ipsecflowmon-cfg', False),
            ],
            'Cisco-IOS-XR-crypto-mibs-ipsecflowmon-cfg',
            'isakmp',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-crypto-mibs-ipsecflowmon-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg',
        ),
    },
    'Snmp.Notification.CiscoEntityExt' : {
        'meta_info' : _MetaInfoClass('Snmp.Notification.CiscoEntityExt', REFERENCE_CLASS,
            '''Enable CISCO-ENTITY-EXT-MIB notifications''',
            False, 
            [
            _MetaInfoClassMember('enable', ATTRIBUTE, 'Empty', 'empty',
                None, None,
                [], [],
                '''                Enable CISCO-ENTITY-EXT-MIB notifications
                ''',
                'enable',
                'Cisco-IOS-XR-snmp-entityextmib-cfg', False),
            ],
            'Cisco-IOS-XR-snmp-entityextmib-cfg',
            'cisco-entity-ext',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-snmp-entityextmib-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg',
        ),
    },
    'Snmp.Notification.Ospf.Lsa' : {
        'meta_info' : _MetaInfoClass('Snmp.Notification.Ospf.Lsa', REFERENCE_CLASS,
            '''SNMP notifications related to LSAs''',
            False, 
            [
            _MetaInfoClassMember('max-age-lsa', ATTRIBUTE, 'Empty', 'empty',
                None, None,
                [], [],
                '''                Enable ospfMaxAgeLsa notification
                ''',
                'max_age_lsa',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('originate-lsa', ATTRIBUTE, 'Empty', 'empty',
                None, None,
                [], [],
                '''                Enable ospfOriginateLsa notification
                ''',
                'originate_lsa',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-ospf-cfg',
            'lsa',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-ipv4-ospf-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg',
        ),
    },
    'Snmp.Notification.Ospf.StateChange' : {
        'meta_info' : _MetaInfoClass('Snmp.Notification.Ospf.StateChange', REFERENCE_CLASS,
            '''SNMP notifications for OSPF state change''',
            False, 
            [
            _MetaInfoClassMember('interface', ATTRIBUTE, 'Empty', 'empty',
                None, None,
                [], [],
                '''                Enable ospfIfStateChange notification
                ''',
                'interface',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('virtual-interface', ATTRIBUTE, 'Empty', 'empty',
                None, None,
                [], [],
                '''                Enable ospfVirtIfStateChange notification
                ''',
                'virtual_interface',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('virtual-neighbor', ATTRIBUTE, 'Empty', 'empty',
                None, None,
                [], [],
                '''                Enable ospfVirtNbrStateChange notification
                ''',
                'virtual_neighbor',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('neighbor', ATTRIBUTE, 'Empty', 'empty',
                None, None,
                [], [],
                '''                Enable ospfNbrStateChange notification
                ''',
                'neighbor',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-ospf-cfg',
            'state-change',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-ipv4-ospf-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg',
        ),
    },
    'Snmp.Notification.Ospf.Retransmit' : {
        'meta_info' : _MetaInfoClass('Snmp.Notification.Ospf.Retransmit', REFERENCE_CLASS,
            '''SNMP notifications for packet retransmissions''',
            False, 
            [
            _MetaInfoClassMember('virtual-packet', ATTRIBUTE, 'Empty', 'empty',
                None, None,
                [], [],
                '''                Enable ospfVirtIfTxRetransmit notification
                ''',
                'virtual_packet',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('packet', ATTRIBUTE, 'Empty', 'empty',
                None, None,
                [], [],
                '''                Enable ospfTxRetransmit notification
                ''',
                'packet',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-ospf-cfg',
            'retransmit',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-ipv4-ospf-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg',
        ),
    },
    'Snmp.Notification.Ospf.Error' : {
        'meta_info' : _MetaInfoClass('Snmp.Notification.Ospf.Error', REFERENCE_CLASS,
            '''SNMP notifications for OSPF errors''',
            False, 
            [
            _MetaInfoClassMember('config-error', ATTRIBUTE, 'Empty', 'empty',
                None, None,
                [], [],
                '''                Enable ospfIfConfigError notification
                ''',
                'config_error',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('authentication-failure', ATTRIBUTE, 'Empty', 'empty',
                None, None,
                [], [],
                '''                Enable ospfIfAuthFailure notification
                ''',
                'authentication_failure',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('virtual-config-error', ATTRIBUTE, 'Empty', 'empty',
                None, None,
                [], [],
                '''                Enable ospfVirtIfConfigError notification
                ''',
                'virtual_config_error',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('virtual-authentication-failure', ATTRIBUTE, 'Empty', 'empty',
                None, None,
                [], [],
                '''                Enable ospfVirtIfAuthFailure notification
                ''',
                'virtual_authentication_failure',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('bad-packet', ATTRIBUTE, 'Empty', 'empty',
                None, None,
                [], [],
                '''                Enable ospfIfRxBadPacket notification
                ''',
                'bad_packet',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('virtual-bad-packet', ATTRIBUTE, 'Empty', 'empty',
                None, None,
                [], [],
                '''                Enable ospfVirtIfRxBadPacket notification
                ''',
                'virtual_bad_packet',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-ospf-cfg',
            'error',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-ipv4-ospf-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg',
        ),
    },
    'Snmp.Notification.Ospf' : {
        'meta_info' : _MetaInfoClass('Snmp.Notification.Ospf', REFERENCE_CLASS,
            '''OSPF-MIB notification configuration''',
            False, 
            [
            _MetaInfoClassMember('lsa', REFERENCE_CLASS, 'Lsa', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg', 'Snmp.Notification.Ospf.Lsa',
                [], [],
                '''                SNMP notifications related to LSAs
                ''',
                'lsa',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('state-change', REFERENCE_CLASS, 'StateChange', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg', 'Snmp.Notification.Ospf.StateChange',
                [], [],
                '''                SNMP notifications for OSPF state change
                ''',
                'state_change',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('retransmit', REFERENCE_CLASS, 'Retransmit', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg', 'Snmp.Notification.Ospf.Retransmit',
                [], [],
                '''                SNMP notifications for packet retransmissions
                ''',
                'retransmit',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('error', REFERENCE_CLASS, 'Error', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg', 'Snmp.Notification.Ospf.Error',
                [], [],
                '''                SNMP notifications for OSPF errors
                ''',
                'error',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-ospf-cfg',
            'ospf',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-ipv4-ospf-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg',
        ),
    },
    'Snmp.Notification.Cfm' : {
        'meta_info' : _MetaInfoClass('Snmp.Notification.Cfm', REFERENCE_CLASS,
            '''802.1ag Connectivity Fault Management MIB
notification configuration''',
            False, 
            [
            _MetaInfoClassMember('enable', ATTRIBUTE, 'Empty', 'empty',
                None, None,
                [], [],
                '''                Enable 802.1ag Connectivity Fault Management
                MIB notifications
                ''',
                'enable',
                'Cisco-IOS-XR-ethernet-cfm-cfg', False),
            ],
            'Cisco-IOS-XR-ethernet-cfm-cfg',
            'cfm',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-ethernet-cfm-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg',
        ),
    },
    'Snmp.Notification.L2tun' : {
        'meta_info' : _MetaInfoClass('Snmp.Notification.L2tun', REFERENCE_CLASS,
            '''Enable SNMP l2tun traps''',
            False, 
            [
            _MetaInfoClassMember('tunnel-up', ATTRIBUTE, 'bool', 'boolean',
                None, None,
                [], [],
                '''                Enable L2TUN tunnel UP traps
                ''',
                'tunnel_up',
                'Cisco-IOS-XR-tunnel-l2tun-proto-mibs-cfg', False),
            _MetaInfoClassMember('tunnel-down', ATTRIBUTE, 'bool', 'boolean',
                None, None,
                [], [],
                '''                Enable L2TUN tunnel DOWN traps
                ''',
                'tunnel_down',
                'Cisco-IOS-XR-tunnel-l2tun-proto-mibs-cfg', False),
            _MetaInfoClassMember('pseudowire-status', ATTRIBUTE, 'bool', 'boolean',
                None, None,
                [], [],
                '''                Enable traps for L2TPv3 PW status
                ''',
                'pseudowire_status',
                'Cisco-IOS-XR-tunnel-l2tun-proto-mibs-cfg', False),
            _MetaInfoClassMember('sessions', ATTRIBUTE, 'bool', 'boolean',
                None, None,
                [], [],
                '''                Enable L2TUN sessions traps
                ''',
                'sessions',
                'Cisco-IOS-XR-tunnel-l2tun-proto-mibs-cfg', False),
            ],
            'Cisco-IOS-XR-tunnel-l2tun-proto-mibs-cfg',
            'l2tun',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-tunnel-l2tun-proto-mibs-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg',
        ),
    },
    'Snmp.Notification.Bgp.Bgp4mib' : {
        'meta_info' : _MetaInfoClass('Snmp.Notification.Bgp.Bgp4mib', REFERENCE_CLASS,
            '''Enable BGP4-MIB and CISCO-BGP4-MIB IPv4-only
notifications: bgpEstablishedNotification,
bgpBackwardTransNotification,
cbgpFsmStateChange, cbgpBackwardTransition,
cbgpPrefixThresholdExceeded,
cbgpPrefixThresholdClear.''',
            False, 
            [
            _MetaInfoClassMember('enable', ATTRIBUTE, 'Empty', 'empty',
                None, None,
                [], [],
                '''                Enable BGP4-MIB and CISCO-BGP4-MIB IPv4-only
                notifications
                ''',
                'enable',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('up-down', ATTRIBUTE, 'Empty', 'empty',
                None, None,
                [], [],
                '''                Enable BGP4-MIB and CISCO-BGP4-MIB IPv4-only
                up/down notifications
                ''',
                'up_down',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-bgp-cfg',
            'bgp4mib',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-ipv4-bgp-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg',
        ),
    },
    'Snmp.Notification.Bgp.CiscoBgp4mib' : {
        'meta_info' : _MetaInfoClass('Snmp.Notification.Bgp.CiscoBgp4mib', REFERENCE_CLASS,
            '''Enable CISCO-BGP4-MIB v2 notifications:
cbgpPeer2EstablishedNotification,
cbgpPeer2BackwardTransNotification,
cbgpPeer2FsmStateChange,
cbgpPeer2BackwardTransition,
cbgpPeer2PrefixThresholdExceeded,
cbgpPeer2PrefixThresholdClear.''',
            False, 
            [
            _MetaInfoClassMember('enable', ATTRIBUTE, 'Empty', 'empty',
                None, None,
                [], [],
                '''                Enable CISCO-BGP4-MIB v2 notifications
                ''',
                'enable',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('up-down', ATTRIBUTE, 'Empty', 'empty',
                None, None,
                [], [],
                '''                Enable CISCO-BGP4-MIB v2 up/down notifications
                ''',
                'up_down',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-bgp-cfg',
            'cisco-bgp4mib',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-ipv4-bgp-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg',
        ),
    },
    'Snmp.Notification.Bgp' : {
        'meta_info' : _MetaInfoClass('Snmp.Notification.Bgp', REFERENCE_CLASS,
            '''BGP4-MIB and CISCO-BGP4-MIB notification
configuration''',
            False, 
            [
            _MetaInfoClassMember('bgp4mib', REFERENCE_CLASS, 'Bgp4mib', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg', 'Snmp.Notification.Bgp.Bgp4mib',
                [], [],
                '''                Enable BGP4-MIB and CISCO-BGP4-MIB IPv4-only
                notifications: bgpEstablishedNotification,
                bgpBackwardTransNotification,
                cbgpFsmStateChange, cbgpBackwardTransition,
                cbgpPrefixThresholdExceeded,
                cbgpPrefixThresholdClear.
                ''',
                'bgp4mib',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('cisco-bgp4mib', REFERENCE_CLASS, 'CiscoBgp4mib', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg', 'Snmp.Notification.Bgp.CiscoBgp4mib',
                [], [],
                '''                Enable CISCO-BGP4-MIB v2 notifications:
                cbgpPeer2EstablishedNotification,
                cbgpPeer2BackwardTransNotification,
                cbgpPeer2FsmStateChange,
                cbgpPeer2BackwardTransition,
                cbgpPeer2PrefixThresholdExceeded,
                cbgpPeer2PrefixThresholdClear.
                ''',
                'cisco_bgp4mib',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-bgp-cfg',
            'bgp',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-ipv4-bgp-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg',
        ),
    },
    'Snmp.Notification.EntityState' : {
        'meta_info' : _MetaInfoClass('Snmp.Notification.EntityState', REFERENCE_CLASS,
            '''ENTITY-STATE-MIB notification configuration''',
            False, 
            [
            _MetaInfoClassMember('switchover', ATTRIBUTE, 'Empty', 'empty',
                None, None,
                [], [],
                '''                Enable ceStateExtStandbySwitchover notification
                ''',
                'switchover',
                'Cisco-IOS-XR-snmp-entstatemib-cfg', False),
            _MetaInfoClassMember('oper-status', ATTRIBUTE, 'Empty', 'empty',
                None, None,
                [], [],
                '''                Enable entStateOperEnable and
                entStateOperDisable notifications
                ''',
                'oper_status',
                'Cisco-IOS-XR-snmp-entstatemib-cfg', False),
            ],
            'Cisco-IOS-XR-snmp-entstatemib-cfg',
            'entity-state',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-snmp-entstatemib-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg',
        ),
    },
    'Snmp.Notification.FrequencySynchronization' : {
        'meta_info' : _MetaInfoClass('Snmp.Notification.FrequencySynchronization', REFERENCE_CLASS,
            '''Frequency Synchronization trap configuration''',
            False, 
            [
            _MetaInfoClassMember('enable', ATTRIBUTE, 'Empty', 'empty',
                None, None,
                [], [],
                '''                Enable Frequency Synchronization traps
                ''',
                'enable',
                'Cisco-IOS-XR-freqsync-cfg', False),
            ],
            'Cisco-IOS-XR-freqsync-cfg',
            'frequency-synchronization',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-freqsync-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg',
        ),
    },
    'Snmp.Notification.MplsTeP2mp' : {
        'meta_info' : _MetaInfoClass('Snmp.Notification.MplsTeP2mp', REFERENCE_CLASS,
            '''CISCO-MPLS-TE-P2MP-STD-MIB notification
configuration''',
            False, 
            [
            _MetaInfoClassMember('up', ATTRIBUTE, 'Empty', 'empty',
                None, None,
                [], [],
                '''                Enable cmplsTeP2mpTunnelDestUp notification
                ''',
                'up',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('down', ATTRIBUTE, 'Empty', 'empty',
                None, None,
                [], [],
                '''                Enable cmplsTeP2mpTunnelDestDown notification
                ''',
                'down',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            ],
            'Cisco-IOS-XR-mpls-te-cfg',
            'mpls-te-p2mp',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-mpls-te-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg',
        ),
    },
    'Snmp.Notification.MplsTe.CiscoExtension' : {
        'meta_info' : _MetaInfoClass('Snmp.Notification.MplsTe.CiscoExtension', REFERENCE_CLASS,
            '''CISCO-MPLS-TE-STD-EXT-MIB notification
configuration''',
            False, 
            [
            _MetaInfoClassMember('preempt', ATTRIBUTE, 'Empty', 'empty',
                None, None,
                [], [],
                '''                Enable cmplsTunnelPreempt notification
                ''',
                'preempt',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('insufficient-bandwidth', ATTRIBUTE, 'Empty', 'empty',
                None, None,
                [], [],
                '''                Enable cmplsTunnelInsuffBW notification
                ''',
                'insufficient_bandwidth',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('re-route-pending-clear', ATTRIBUTE, 'Empty', 'empty',
                None, None,
                [], [],
                '''                Enable cmplsTunnelReRoutePendingClear
                notification
                ''',
                're_route_pending_clear',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('bringup-fail', ATTRIBUTE, 'Empty', 'empty',
                None, None,
                [], [],
                '''                Enable cmplsTunnelBringupFail notification
                ''',
                'bringup_fail',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('re-route-pending', ATTRIBUTE, 'Empty', 'empty',
                None, None,
                [], [],
                '''                Enable cmplsTunnelReRoutePending notification
                ''',
                're_route_pending',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            ],
            'Cisco-IOS-XR-mpls-te-cfg',
            'cisco-extension',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-mpls-te-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg',
        ),
    },
    'Snmp.Notification.MplsTe' : {
        'meta_info' : _MetaInfoClass('Snmp.Notification.MplsTe', REFERENCE_CLASS,
            '''MPLS-TE-STD-MIB notification configuration''',
            False, 
            [
            _MetaInfoClassMember('cisco-extension', REFERENCE_CLASS, 'CiscoExtension', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg', 'Snmp.Notification.MplsTe.CiscoExtension',
                [], [],
                '''                CISCO-MPLS-TE-STD-EXT-MIB notification
                configuration
                ''',
                'cisco_extension',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('cisco', ATTRIBUTE, 'Empty', 'empty',
                None, None,
                [], [],
                '''                Enable MPLS TE tunnel Cisco format (default
                IETF) notification
                ''',
                'cisco',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('up', ATTRIBUTE, 'Empty', 'empty',
                None, None,
                [], [],
                '''                Enable mplsTunnelUp notification
                ''',
                'up',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('reoptimize', ATTRIBUTE, 'Empty', 'empty',
                None, None,
                [], [],
                '''                Enable mplsTunnelReoptimized notification
                ''',
                'reoptimize',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('reroute', ATTRIBUTE, 'Empty', 'empty',
                None, None,
                [], [],
                '''                Enable mplsTunnelRerouted notification
                ''',
                'reroute',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('down', ATTRIBUTE, 'Empty', 'empty',
                None, None,
                [], [],
                '''                Enable mplsTunnelDown notification
                ''',
                'down',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            ],
            'Cisco-IOS-XR-mpls-te-cfg',
            'mpls-te',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-mpls-te-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg',
        ),
    },
    'Snmp.Notification.MplsFrr' : {
        'meta_info' : _MetaInfoClass('Snmp.Notification.MplsFrr', REFERENCE_CLASS,
            '''CISCO-IETF-FRR-MIB notification configuration''',
            False, 
            [
            _MetaInfoClassMember('unprotected', ATTRIBUTE, 'Empty', 'empty',
                None, None,
                [], [],
                '''                Enable cmplsFrrUnProtected notification
                ''',
                'unprotected',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('enable', ATTRIBUTE, 'Empty', 'empty',
                None, None,
                [], [],
                '''                Enable cmplsFrrMIB notifications
                ''',
                'enable',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('protected', ATTRIBUTE, 'Empty', 'empty',
                None, None,
                [], [],
                '''                Enable cmplsFrrProtected notification
                ''',
                'protected',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            ],
            'Cisco-IOS-XR-mpls-te-cfg',
            'mpls-frr',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-mpls-te-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg',
        ),
    },
    'Snmp.Notification.Oam' : {
        'meta_info' : _MetaInfoClass('Snmp.Notification.Oam', REFERENCE_CLASS,
            '''802.3 OAM MIB notification configuration''',
            False, 
            [
            _MetaInfoClassMember('enable', ATTRIBUTE, 'Empty', 'empty',
                None, None,
                [], [],
                '''                Enable 802.3 OAM MIB notifications
                ''',
                'enable',
                'Cisco-IOS-XR-ethernet-link-oam-cfg', False),
            ],
            'Cisco-IOS-XR-ethernet-link-oam-cfg',
            'oam',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-ethernet-link-oam-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg',
        ),
    },
    'Snmp.Notification.MplsL3vpn' : {
        'meta_info' : _MetaInfoClass('Snmp.Notification.MplsL3vpn', REFERENCE_CLASS,
            '''MPLS-L3VPN-STD-MIB notification configuration''',
            False, 
            [
            _MetaInfoClassMember('max-threshold-reissue-notification-time', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('0', '4294967295')], [],
                '''                Time interval (secs) for re-issuing
                max-threshold notification
                ''',
                'max_threshold_reissue_notification_time',
                'Cisco-IOS-XR-mpls-vpn-cfg', False),
            _MetaInfoClassMember('max-threshold-exceeded', ATTRIBUTE, 'Empty', 'empty',
                None, None,
                [], [],
                '''                Enable mplsL3VpnVrfNumVrfRouteMaxThreshExceeded
                notification
                ''',
                'max_threshold_exceeded',
                'Cisco-IOS-XR-mpls-vpn-cfg', False),
            _MetaInfoClassMember('max-threshold-cleared', ATTRIBUTE, 'Empty', 'empty',
                None, None,
                [], [],
                '''                Enable mplsL3VpnNumVrfRouteMaxThreshCleared
                notification
                ''',
                'max_threshold_cleared',
                'Cisco-IOS-XR-mpls-vpn-cfg', False),
            _MetaInfoClassMember('mid-threshold-exceeded', ATTRIBUTE, 'Empty', 'empty',
                None, None,
                [], [],
                '''                Enable mplsL3VpnVrfRouteMidThreshExceeded
                notification
                ''',
                'mid_threshold_exceeded',
                'Cisco-IOS-XR-mpls-vpn-cfg', False),
            _MetaInfoClassMember('enable', ATTRIBUTE, 'Empty', 'empty',
                None, None,
                [], [],
                '''                Enable mplsL3VpnMIB notifications
                ''',
                'enable',
                'Cisco-IOS-XR-mpls-vpn-cfg', False),
            _MetaInfoClassMember('vrf-down', ATTRIBUTE, 'Empty', 'empty',
                None, None,
                [], [],
                '''                Enable mplsL3VpnVrfDown notification
                ''',
                'vrf_down',
                'Cisco-IOS-XR-mpls-vpn-cfg', False),
            _MetaInfoClassMember('vrf-up', ATTRIBUTE, 'Empty', 'empty',
                None, None,
                [], [],
                '''                Enable mplsL3VpnVrfUp notification
                ''',
                'vrf_up',
                'Cisco-IOS-XR-mpls-vpn-cfg', False),
            ],
            'Cisco-IOS-XR-mpls-vpn-cfg',
            'mpls-l3vpn',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-mpls-vpn-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg',
        ),
    },
    'Snmp.Notification.ConfigMan' : {
        'meta_info' : _MetaInfoClass('Snmp.Notification.ConfigMan', REFERENCE_CLASS,
            '''CISCO-CONFIG-MAN-MIB notification configurations''',
            False, 
            [
            _MetaInfoClassMember('enable', ATTRIBUTE, 'Empty', 'empty',
                None, None,
                [], [],
                '''                Enable ciscoConfigManMIB notifications
                ''',
                'enable',
                'Cisco-IOS-XR-config-mibs-cfg', False),
            ],
            'Cisco-IOS-XR-config-mibs-cfg',
            'config-man',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-config-mibs-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg',
        ),
    },
    'Snmp.Notification.Diametermib' : {
        'meta_info' : _MetaInfoClass('Snmp.Notification.Diametermib', REFERENCE_CLASS,
            '''Enable SNMP diameter traps''',
            False, 
            [
            _MetaInfoClassMember('protocolerror', ATTRIBUTE, 'bool', 'boolean',
                None, None,
                [], [],
                '''                Enable SNMP diameter protocol error
                notification
                ''',
                'protocolerror',
                'Cisco-IOS-XR-aaa-diameter-base-mib-cfg', False),
            _MetaInfoClassMember('permanentfail', ATTRIBUTE, 'bool', 'boolean',
                None, None,
                [], [],
                '''                Enable SNMP diameter permanent failure
                notification
                ''',
                'permanentfail',
                'Cisco-IOS-XR-aaa-diameter-base-mib-cfg', False),
            _MetaInfoClassMember('peerdown', ATTRIBUTE, 'bool', 'boolean',
                None, None,
                [], [],
                '''                Enable SNMP diameter peer connection down
                notification
                ''',
                'peerdown',
                'Cisco-IOS-XR-aaa-diameter-base-mib-cfg', False),
            _MetaInfoClassMember('peerup', ATTRIBUTE, 'bool', 'boolean',
                None, None,
                [], [],
                '''                Enable SNMP diameter peer connection up
                notification
                ''',
                'peerup',
                'Cisco-IOS-XR-aaa-diameter-base-mib-cfg', False),
            _MetaInfoClassMember('transientfail', ATTRIBUTE, 'bool', 'boolean',
                None, None,
                [], [],
                '''                Enable SNMP diameter transient failure
                notification
                ''',
                'transientfail',
                'Cisco-IOS-XR-aaa-diameter-base-mib-cfg', False),
            ],
            'Cisco-IOS-XR-aaa-diameter-base-mib-cfg',
            'diametermib',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-aaa-diameter-base-mib-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg',
        ),
    },
    'Snmp.Notification.FruControl' : {
        'meta_info' : _MetaInfoClass('Snmp.Notification.FruControl', REFERENCE_CLASS,
            '''CISCO-ENTITY-FRU-CONTROL-MIB notification
configuration''',
            False, 
            [
            _MetaInfoClassMember('enable', ATTRIBUTE, 'Empty', 'empty',
                None, None,
                [], [],
                '''                Enable ciscoEntityFRUControlMIB notifications
                ''',
                'enable',
                'Cisco-IOS-XR-snmp-frucontrolmib-cfg', False),
            ],
            'Cisco-IOS-XR-snmp-frucontrolmib-cfg',
            'fru-control',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-snmp-frucontrolmib-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg',
        ),
    },
    'Snmp.Notification.Syslog' : {
        'meta_info' : _MetaInfoClass('Snmp.Notification.Syslog', REFERENCE_CLASS,
            '''CISCO-SYSLOG-MIB notification configuration''',
            False, 
            [
            _MetaInfoClassMember('enable', ATTRIBUTE, 'Empty', 'empty',
                None, None,
                [], [],
                '''                Enable ciscoSyslogMIB notifications
                ''',
                'enable',
                'Cisco-IOS-XR-snmp-syslogmib-cfg', False),
            ],
            'Cisco-IOS-XR-snmp-syslogmib-cfg',
            'syslog',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-snmp-syslogmib-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg',
        ),
    },
    'Snmp.Notification.Bfd' : {
        'meta_info' : _MetaInfoClass('Snmp.Notification.Bfd', REFERENCE_CLASS,
            '''CISCO-IETF-BFD-MIB notification configuration''',
            False, 
            [
            _MetaInfoClassMember('enable', ATTRIBUTE, 'Empty', 'empty',
                None, None,
                [], [],
                '''                Enable CISCO-IETF-BFD-MIB notifications
                ''',
                'enable',
                'Cisco-IOS-XR-ip-bfd-cfg', False),
            ],
            'Cisco-IOS-XR-ip-bfd-cfg',
            'bfd',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-ip-bfd-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg',
        ),
    },
    'Snmp.Notification.OpticalOts' : {
        'meta_info' : _MetaInfoClass('Snmp.Notification.OpticalOts', REFERENCE_CLASS,
            '''CISCO-OPTICAL-OTS-MIB notification configuration''',
            False, 
            [
            _MetaInfoClassMember('enable', ATTRIBUTE, 'Empty', 'empty',
                None, None,
                [], [],
                '''                Enable OpticalOtsmib notifications
                ''',
                'enable',
                'Cisco-IOS-XR-opticalotsmib-cfg', False),
            ],
            'Cisco-IOS-XR-opticalotsmib-cfg',
            'optical-ots',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-opticalotsmib-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg',
        ),
    },
    'Snmp.Notification.Optical' : {
        'meta_info' : _MetaInfoClass('Snmp.Notification.Optical', REFERENCE_CLASS,
            '''CISCO-OPTICAL-MIB notification configuration''',
            False, 
            [
            _MetaInfoClassMember('enable', ATTRIBUTE, 'Empty', 'empty',
                None, None,
                [], [],
                '''                Enable Opticalmib notifications
                ''',
                'enable',
                'Cisco-IOS-XR-opticalmib-cfg', False),
            ],
            'Cisco-IOS-XR-opticalmib-cfg',
            'optical',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-opticalmib-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg',
        ),
    },
    'Snmp.Notification.Ospfv3.Error' : {
        'meta_info' : _MetaInfoClass('Snmp.Notification.Ospfv3.Error', REFERENCE_CLASS,
            '''SNMP notifications for OSPF errors''',
            False, 
            [
            _MetaInfoClassMember('config-error', ATTRIBUTE, 'Empty', 'empty',
                None, None,
                [], [],
                '''                Enable ospfv3IfConfigError notification
                ''',
                'config_error',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            _MetaInfoClassMember('bad-packet', ATTRIBUTE, 'Empty', 'empty',
                None, None,
                [], [],
                '''                Enable ospfv3IfRxBadPacket notification
                ''',
                'bad_packet',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            _MetaInfoClassMember('virtual-bad-packet', ATTRIBUTE, 'Empty', 'empty',
                None, None,
                [], [],
                '''                Enable ospfv3VirtIfRxBadPacket notification
                ''',
                'virtual_bad_packet',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            _MetaInfoClassMember('virtual-config-error', ATTRIBUTE, 'Empty', 'empty',
                None, None,
                [], [],
                '''                Enable ospfv3VirtIfConfigError notification
                ''',
                'virtual_config_error',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            ],
            'Cisco-IOS-XR-ipv6-ospfv3-cfg',
            'error',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-ipv6-ospfv3-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg',
        ),
    },
    'Snmp.Notification.Ospfv3.StateChange' : {
        'meta_info' : _MetaInfoClass('Snmp.Notification.Ospfv3.StateChange', REFERENCE_CLASS,
            '''SNMP notifications for OSPF state change''',
            False, 
            [
            _MetaInfoClassMember('restart-virtual-helper', ATTRIBUTE, 'Empty', 'empty',
                None, None,
                [], [],
                '''                Enable ospfv3VirtNbrRestartHelperStatusChange
                notification
                ''',
                'restart_virtual_helper',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            _MetaInfoClassMember('nssa-translator', ATTRIBUTE, 'Empty', 'empty',
                None, None,
                [], [],
                '''                Enable ospfv3NssaTranslatorStatusChange
                notification
                ''',
                'nssa_translator',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            _MetaInfoClassMember('interface', ATTRIBUTE, 'Empty', 'empty',
                None, None,
                [], [],
                '''                Enable ospfv3IfStateChange notification
                ''',
                'interface',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            _MetaInfoClassMember('restart', ATTRIBUTE, 'Empty', 'empty',
                None, None,
                [], [],
                '''                Enable ospfv3RestartStatusChange notification
                ''',
                'restart',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            _MetaInfoClassMember('neighbor', ATTRIBUTE, 'Empty', 'empty',
                None, None,
                [], [],
                '''                Enable ospfv3NbrStateChange notification
                ''',
                'neighbor',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            _MetaInfoClassMember('virtual-interface', ATTRIBUTE, 'Empty', 'empty',
                None, None,
                [], [],
                '''                Enable ospfv3VirtIfStateChange notification
                ''',
                'virtual_interface',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            _MetaInfoClassMember('restart-helper', ATTRIBUTE, 'Empty', 'empty',
                None, None,
                [], [],
                '''                Enable ospfv3NbrRestartHelperStatusChange
                notification
                ''',
                'restart_helper',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            _MetaInfoClassMember('virtual-neighbor', ATTRIBUTE, 'Empty', 'empty',
                None, None,
                [], [],
                '''                Enable ospfv3VirtNbrStateChange notification
                ''',
                'virtual_neighbor',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            ],
            'Cisco-IOS-XR-ipv6-ospfv3-cfg',
            'state-change',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-ipv6-ospfv3-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg',
        ),
    },
    'Snmp.Notification.Ospfv3' : {
        'meta_info' : _MetaInfoClass('Snmp.Notification.Ospfv3', REFERENCE_CLASS,
            '''OSPFv3-MIB notification configuration''',
            False, 
            [
            _MetaInfoClassMember('error', REFERENCE_CLASS, 'Error', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg', 'Snmp.Notification.Ospfv3.Error',
                [], [],
                '''                SNMP notifications for OSPF errors
                ''',
                'error',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            _MetaInfoClassMember('state-change', REFERENCE_CLASS, 'StateChange', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg', 'Snmp.Notification.Ospfv3.StateChange',
                [], [],
                '''                SNMP notifications for OSPF state change
                ''',
                'state_change',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            ],
            'Cisco-IOS-XR-ipv6-ospfv3-cfg',
            'ospfv3',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-ipv6-ospfv3-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg',
        ),
    },
    'Snmp.Notification' : {
        'meta_info' : _MetaInfoClass('Snmp.Notification', REFERENCE_CLASS,
            '''Enable SNMP notifications''',
            False, 
            [
            _MetaInfoClassMember('snmp', REFERENCE_CLASS, 'Snmp_', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg', 'Snmp.Notification.Snmp_',
                [], [],
                '''                SNMP notification configuration
                ''',
                'snmp',
                'Cisco-IOS-XR-snmp-agent-cfg', False),
            _MetaInfoClassMember('selective-vrf-download', REFERENCE_CLASS, 'SelectiveVrfDownload', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg', 'Snmp.Notification.SelectiveVrfDownload',
                [], [],
                '''                CISCO-SELECTIVE-VRF-DOWNLOAD-MIB notification
                configuration
                ''',
                'selective_vrf_download',
                'Cisco-IOS-XR-infra-rsi-cfg', False),
            _MetaInfoClassMember('vpls', REFERENCE_CLASS, 'Vpls', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg', 'Snmp.Notification.Vpls',
                [], [],
                '''                CISCO-IETF-VPLS-GENERIC-MIB notification
                configuration
                ''',
                'vpls',
                'Cisco-IOS-XR-l2vpn-cfg', False),
            _MetaInfoClassMember('l2vpn', REFERENCE_CLASS, 'L2vpn', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg', 'Snmp.Notification.L2vpn',
                [], [],
                '''                CISCO-IETF-PW-MIB notification configuration
                ''',
                'l2vpn',
                'Cisco-IOS-XR-l2vpn-cfg', False),
            _MetaInfoClassMember('entity', REFERENCE_CLASS, 'Entity', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg', 'Snmp.Notification.Entity',
                [], [],
                '''                Enable ENTITY-MIB notifications
                ''',
                'entity_',
                'Cisco-IOS-XR-snmp-entitymib-cfg', False),
            _MetaInfoClassMember('bridge', REFERENCE_CLASS, 'Bridge', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg', 'Snmp.Notification.Bridge',
                [], [],
                '''                BRIDGE-MIB notification configuration
                ''',
                'bridge',
                'Cisco-IOS-XR-snmp-bridgemib-cfg', False),
            _MetaInfoClassMember('rf', REFERENCE_CLASS, 'Rf', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg', 'Snmp.Notification.Rf',
                [], [],
                '''                CISCO-RF-MIB notification configuration
                ''',
                'rf',
                'Cisco-IOS-XR-snmp-mib-rfmib-cfg', False),
            _MetaInfoClassMember('ntp', REFERENCE_CLASS, 'Ntp', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg', 'Snmp.Notification.Ntp',
                [], [],
                '''                CISCO-NTP-MIB notification configuration
                ''',
                'ntp',
                'Cisco-IOS-XR-ip-ntp-cfg', False),
            _MetaInfoClassMember('otn', REFERENCE_CLASS, 'Otn', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg', 'Snmp.Notification.Otn',
                [], [],
                '''                CISCO-OTN-IF-MIB notification configuration
                ''',
                'otn',
                'Cisco-IOS-XR-otnifmib-cfg', False),
            _MetaInfoClassMember('addresspool-mib', REFERENCE_CLASS, 'AddresspoolMib', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg', 'Snmp.Notification.AddresspoolMib',
                [], [],
                '''                Enable SNMP daps traps
                ''',
                'addresspool_mib',
                'Cisco-IOS-XR-ip-daps-mib-cfg', False),
            _MetaInfoClassMember('system', REFERENCE_CLASS, 'System', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg', 'Snmp.Notification.System',
                [], [],
                '''                CISCO-SYSTEM-MIB notification configuration
                ''',
                'system',
                'Cisco-IOS-XR-infra-systemmib-cfg', False),
            _MetaInfoClassMember('rsvp', REFERENCE_CLASS, 'Rsvp', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg', 'Snmp.Notification.Rsvp',
                [], [],
                '''                Enable RSVP-MIB notifications
                ''',
                'rsvp',
                'Cisco-IOS-XR-ip-rsvp-cfg', False),
            _MetaInfoClassMember('sensor', REFERENCE_CLASS, 'Sensor', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg', 'Snmp.Notification.Sensor',
                [], [],
                '''                CISCO-ENTITY-SENSOR-MIB notification
                configuration
                ''',
                'sensor',
                'Cisco-IOS-XR-snmp-ciscosensormib-cfg', False),
            _MetaInfoClassMember('mpls-ldp', REFERENCE_CLASS, 'MplsLdp', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg', 'Snmp.Notification.MplsLdp',
                [], [],
                '''                MPLS-LDP-STD-MIB notification configuration
                ''',
                'mpls_ldp',
                'Cisco-IOS-XR-mpls-ldp-cfg', False),
            _MetaInfoClassMember('subscriber-mib', REFERENCE_CLASS, 'SubscriberMib', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg', 'Snmp.Notification.SubscriberMib',
                [], [],
                '''                Subscriber notification commands
                ''',
                'subscriber_mib',
                'Cisco-IOS-XR-subscriber-session-mon-mibs-cfg', False),
            _MetaInfoClassMember('flash', REFERENCE_CLASS, 'Flash', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg', 'Snmp.Notification.Flash',
                [], [],
                '''                CISCO-FLASH-MIB notification configuration
                ''',
                'flash',
                'Cisco-IOS-XR-flashmib-cfg', False),
            _MetaInfoClassMember('config-copy', REFERENCE_CLASS, 'ConfigCopy', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg', 'Snmp.Notification.ConfigCopy',
                [], [],
                '''                CISCO-CONFIG-COPY-MIB notification configuration
                ''',
                'config_copy',
                'Cisco-IOS-XR-infra-confcopymib-cfg', False),
            _MetaInfoClassMember('hsrp', REFERENCE_CLASS, 'Hsrp', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg', 'Snmp.Notification.Hsrp',
                [], [],
                '''                CISCO-HSRP-MIB notification configuration
                ''',
                'hsrp',
                'Cisco-IOS-XR-ipv4-hsrp-cfg', False),
            _MetaInfoClassMember('entity-redundancy', REFERENCE_CLASS, 'EntityRedundancy', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg', 'Snmp.Notification.EntityRedundancy',
                [], [],
                '''                CISCO-ENTITY-REDUNDANCY-MIB notification
                configuration
                ''',
                'entity_redundancy',
                'Cisco-IOS-XR-infra-ceredundancymib-cfg', False),
            _MetaInfoClassMember('isis', REFERENCE_CLASS, 'Isis', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg', 'Snmp.Notification.Isis',
                [], [],
                '''                Enable ISIS-MIB notifications
                ''',
                'isis',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            _MetaInfoClassMember('vrrp', REFERENCE_CLASS, 'Vrrp', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg', 'Snmp.Notification.Vrrp',
                [], [],
                '''                VRRP-MIB notification configuration
                ''',
                'vrrp',
                'Cisco-IOS-XR-ipv4-vrrp-cfg', False),
            _MetaInfoClassMember('ip-sec', REFERENCE_CLASS, 'IpSec', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg', 'Snmp.Notification.IpSec',
                [], [],
                '''                Enable CISCO-IPSEC-FLOW-MONITOR-MIB
                notifications
                ''',
                'ip_sec',
                'Cisco-IOS-XR-crypto-mibs-ipsecflowmon-cfg', False),
            _MetaInfoClassMember('isakmp', REFERENCE_CLASS, 'Isakmp', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg', 'Snmp.Notification.Isakmp',
                [], [],
                '''                Enable CISCO-IPSEC-FLOW-MONITOR-MIB
                notifications
                ''',
                'isakmp',
                'Cisco-IOS-XR-crypto-mibs-ipsecflowmon-cfg', False),
            _MetaInfoClassMember('cisco-entity-ext', REFERENCE_CLASS, 'CiscoEntityExt', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg', 'Snmp.Notification.CiscoEntityExt',
                [], [],
                '''                Enable CISCO-ENTITY-EXT-MIB notifications
                ''',
                'cisco_entity_ext',
                'Cisco-IOS-XR-snmp-entityextmib-cfg', False),
            _MetaInfoClassMember('ospf', REFERENCE_CLASS, 'Ospf', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg', 'Snmp.Notification.Ospf',
                [], [],
                '''                OSPF-MIB notification configuration
                ''',
                'ospf',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('cfm', REFERENCE_CLASS, 'Cfm', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg', 'Snmp.Notification.Cfm',
                [], [],
                '''                802.1ag Connectivity Fault Management MIB
                notification configuration
                ''',
                'cfm',
                'Cisco-IOS-XR-ethernet-cfm-cfg', False),
            _MetaInfoClassMember('l2tun', REFERENCE_CLASS, 'L2tun', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg', 'Snmp.Notification.L2tun',
                [], [],
                '''                Enable SNMP l2tun traps
                ''',
                'l2tun',
                'Cisco-IOS-XR-tunnel-l2tun-proto-mibs-cfg', False),
            _MetaInfoClassMember('bgp', REFERENCE_CLASS, 'Bgp', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg', 'Snmp.Notification.Bgp',
                [], [],
                '''                BGP4-MIB and CISCO-BGP4-MIB notification
                configuration
                ''',
                'bgp',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('entity-state', REFERENCE_CLASS, 'EntityState', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg', 'Snmp.Notification.EntityState',
                [], [],
                '''                ENTITY-STATE-MIB notification configuration
                ''',
                'entity_state',
                'Cisco-IOS-XR-snmp-entstatemib-cfg', False),
            _MetaInfoClassMember('frequency-synchronization', REFERENCE_CLASS, 'FrequencySynchronization', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg', 'Snmp.Notification.FrequencySynchronization',
                [], [],
                '''                Frequency Synchronization trap configuration
                ''',
                'frequency_synchronization',
                'Cisco-IOS-XR-freqsync-cfg', False),
            _MetaInfoClassMember('mpls-te-p2mp', REFERENCE_CLASS, 'MplsTeP2mp', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg', 'Snmp.Notification.MplsTeP2mp',
                [], [],
                '''                CISCO-MPLS-TE-P2MP-STD-MIB notification
                configuration
                ''',
                'mpls_te_p2mp',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('mpls-te', REFERENCE_CLASS, 'MplsTe', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg', 'Snmp.Notification.MplsTe',
                [], [],
                '''                MPLS-TE-STD-MIB notification configuration
                ''',
                'mpls_te',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('mpls-frr', REFERENCE_CLASS, 'MplsFrr', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg', 'Snmp.Notification.MplsFrr',
                [], [],
                '''                CISCO-IETF-FRR-MIB notification configuration
                ''',
                'mpls_frr',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('oam', REFERENCE_CLASS, 'Oam', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg', 'Snmp.Notification.Oam',
                [], [],
                '''                802.3 OAM MIB notification configuration
                ''',
                'oam',
                'Cisco-IOS-XR-ethernet-link-oam-cfg', False),
            _MetaInfoClassMember('mpls-l3vpn', REFERENCE_CLASS, 'MplsL3vpn', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg', 'Snmp.Notification.MplsL3vpn',
                [], [],
                '''                MPLS-L3VPN-STD-MIB notification configuration
                ''',
                'mpls_l3vpn',
                'Cisco-IOS-XR-mpls-vpn-cfg', False),
            _MetaInfoClassMember('config-man', REFERENCE_CLASS, 'ConfigMan', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg', 'Snmp.Notification.ConfigMan',
                [], [],
                '''                CISCO-CONFIG-MAN-MIB notification configurations
                ''',
                'config_man',
                'Cisco-IOS-XR-config-mibs-cfg', False),
            _MetaInfoClassMember('diametermib', REFERENCE_CLASS, 'Diametermib', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg', 'Snmp.Notification.Diametermib',
                [], [],
                '''                Enable SNMP diameter traps
                ''',
                'diametermib',
                'Cisco-IOS-XR-aaa-diameter-base-mib-cfg', False),
            _MetaInfoClassMember('fru-control', REFERENCE_CLASS, 'FruControl', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg', 'Snmp.Notification.FruControl',
                [], [],
                '''                CISCO-ENTITY-FRU-CONTROL-MIB notification
                configuration
                ''',
                'fru_control',
                'Cisco-IOS-XR-snmp-frucontrolmib-cfg', False),
            _MetaInfoClassMember('syslog', REFERENCE_CLASS, 'Syslog', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg', 'Snmp.Notification.Syslog',
                [], [],
                '''                CISCO-SYSLOG-MIB notification configuration
                ''',
                'syslog',
                'Cisco-IOS-XR-snmp-syslogmib-cfg', False),
            _MetaInfoClassMember('ipsla', ATTRIBUTE, 'bool', 'boolean',
                None, None,
                [], [],
                '''                Enable SNMP RTTMON-MIB IPSLA traps
                ''',
                'ipsla',
                'Cisco-IOS-XR-man-ipsla-cfg', False),
            _MetaInfoClassMember('bfd', REFERENCE_CLASS, 'Bfd', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg', 'Snmp.Notification.Bfd',
                [], [],
                '''                CISCO-IETF-BFD-MIB notification configuration
                ''',
                'bfd',
                'Cisco-IOS-XR-ip-bfd-cfg', False),
            _MetaInfoClassMember('optical-ots', REFERENCE_CLASS, 'OpticalOts', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg', 'Snmp.Notification.OpticalOts',
                [], [],
                '''                CISCO-OPTICAL-OTS-MIB notification configuration
                ''',
                'optical_ots',
                'Cisco-IOS-XR-opticalotsmib-cfg', False),
            _MetaInfoClassMember('optical', REFERENCE_CLASS, 'Optical', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg', 'Snmp.Notification.Optical',
                [], [],
                '''                CISCO-OPTICAL-MIB notification configuration
                ''',
                'optical',
                'Cisco-IOS-XR-opticalmib-cfg', False),
            _MetaInfoClassMember('ospfv3', REFERENCE_CLASS, 'Ospfv3', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg', 'Snmp.Notification.Ospfv3',
                [], [],
                '''                OSPFv3-MIB notification configuration
                ''',
                'ospfv3',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            ],
            'Cisco-IOS-XR-snmp-agent-cfg',
            'notification',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-snmp-agent-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg',
        ),
    },
    'Snmp.Correlator.Rules.Rule.RootCauses.RootCause.VarBinds.VarBind.Match' : {
        'meta_info' : _MetaInfoClass('Snmp.Correlator.Rules.Rule.RootCauses.RootCause.VarBinds.VarBind.Match', REFERENCE_CLASS,
            '''VarBind match conditions''',
            False, 
            [
            _MetaInfoClassMember('value', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                Regular Expression to match value
                ''',
                'value',
                'Cisco-IOS-XR-snmp-agent-cfg', False),
            _MetaInfoClassMember('index', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                Regular Expression to match index
                ''',
                'index',
                'Cisco-IOS-XR-snmp-agent-cfg', False),
            ],
            'Cisco-IOS-XR-snmp-agent-cfg',
            'match',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-snmp-agent-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg',
        ),
    },
    'Snmp.Correlator.Rules.Rule.RootCauses.RootCause.VarBinds.VarBind' : {
        'meta_info' : _MetaInfoClass('Snmp.Correlator.Rules.Rule.RootCauses.RootCause.VarBinds.VarBind', REFERENCE_LIST,
            '''Varbind match conditions''',
            False, 
            [
            _MetaInfoClassMember('oid', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                OID of varbind (dotted decimal)
                ''',
                'oid',
                'Cisco-IOS-XR-snmp-agent-cfg', True),
            _MetaInfoClassMember('match', REFERENCE_CLASS, 'Match', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg', 'Snmp.Correlator.Rules.Rule.RootCauses.RootCause.VarBinds.VarBind.Match',
                [], [],
                '''                VarBind match conditions
                ''',
                'match',
                'Cisco-IOS-XR-snmp-agent-cfg', False),
            ],
            'Cisco-IOS-XR-snmp-agent-cfg',
            'var-bind',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-snmp-agent-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg',
        ),
    },
    'Snmp.Correlator.Rules.Rule.RootCauses.RootCause.VarBinds' : {
        'meta_info' : _MetaInfoClass('Snmp.Correlator.Rules.Rule.RootCauses.RootCause.VarBinds', REFERENCE_CLASS,
            '''Varbinds to match''',
            False, 
            [
            _MetaInfoClassMember('var-bind', REFERENCE_LIST, 'VarBind', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg', 'Snmp.Correlator.Rules.Rule.RootCauses.RootCause.VarBinds.VarBind',
                [], [],
                '''                Varbind match conditions
                ''',
                'var_bind',
                'Cisco-IOS-XR-snmp-agent-cfg', False),
            ],
            'Cisco-IOS-XR-snmp-agent-cfg',
            'var-binds',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-snmp-agent-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg',
        ),
    },
    'Snmp.Correlator.Rules.Rule.RootCauses.RootCause' : {
        'meta_info' : _MetaInfoClass('Snmp.Correlator.Rules.Rule.RootCauses.RootCause', REFERENCE_LIST,
            '''The rootcause - maximum of one can be
configured per rule''',
            False, 
            [
            _MetaInfoClassMember('oid', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                OID of rootcause trap (dotted decimal)
                ''',
                'oid',
                'Cisco-IOS-XR-snmp-agent-cfg', True),
            _MetaInfoClassMember('created', ATTRIBUTE, 'Empty', 'empty',
                None, None,
                [], [],
                '''                Create rootcause
                ''',
                'created',
                'Cisco-IOS-XR-snmp-agent-cfg', False),
            _MetaInfoClassMember('var-binds', REFERENCE_CLASS, 'VarBinds', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg', 'Snmp.Correlator.Rules.Rule.RootCauses.RootCause.VarBinds',
                [], [],
                '''                Varbinds to match
                ''',
                'var_binds',
                'Cisco-IOS-XR-snmp-agent-cfg', False),
            ],
            'Cisco-IOS-XR-snmp-agent-cfg',
            'root-cause',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-snmp-agent-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg',
        ),
    },
    'Snmp.Correlator.Rules.Rule.RootCauses' : {
        'meta_info' : _MetaInfoClass('Snmp.Correlator.Rules.Rule.RootCauses', REFERENCE_CLASS,
            '''Table of configured rootcause (only one entry
allowed)''',
            False, 
            [
            _MetaInfoClassMember('root-cause', REFERENCE_LIST, 'RootCause', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg', 'Snmp.Correlator.Rules.Rule.RootCauses.RootCause',
                [], [],
                '''                The rootcause - maximum of one can be
                configured per rule
                ''',
                'root_cause',
                'Cisco-IOS-XR-snmp-agent-cfg', False),
            ],
            'Cisco-IOS-XR-snmp-agent-cfg',
            'root-causes',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-snmp-agent-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg',
        ),
    },
    'Snmp.Correlator.Rules.Rule.NonRootCauses.NonRootCause.VarBinds.VarBind.Match' : {
        'meta_info' : _MetaInfoClass('Snmp.Correlator.Rules.Rule.NonRootCauses.NonRootCause.VarBinds.VarBind.Match', REFERENCE_CLASS,
            '''VarBind match conditions''',
            False, 
            [
            _MetaInfoClassMember('value', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                Regular Expression to match value
                ''',
                'value',
                'Cisco-IOS-XR-snmp-agent-cfg', False),
            _MetaInfoClassMember('index', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                Regular Expression to match index
                ''',
                'index',
                'Cisco-IOS-XR-snmp-agent-cfg', False),
            ],
            'Cisco-IOS-XR-snmp-agent-cfg',
            'match',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-snmp-agent-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg',
        ),
    },
    'Snmp.Correlator.Rules.Rule.NonRootCauses.NonRootCause.VarBinds.VarBind' : {
        'meta_info' : _MetaInfoClass('Snmp.Correlator.Rules.Rule.NonRootCauses.NonRootCause.VarBinds.VarBind', REFERENCE_LIST,
            '''Varbind match conditions''',
            False, 
            [
            _MetaInfoClassMember('oid', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                OID of varbind (dotted decimal)
                ''',
                'oid',
                'Cisco-IOS-XR-snmp-agent-cfg', True),
            _MetaInfoClassMember('match', REFERENCE_CLASS, 'Match', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg', 'Snmp.Correlator.Rules.Rule.NonRootCauses.NonRootCause.VarBinds.VarBind.Match',
                [], [],
                '''                VarBind match conditions
                ''',
                'match',
                'Cisco-IOS-XR-snmp-agent-cfg', False),
            ],
            'Cisco-IOS-XR-snmp-agent-cfg',
            'var-bind',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-snmp-agent-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg',
        ),
    },
    'Snmp.Correlator.Rules.Rule.NonRootCauses.NonRootCause.VarBinds' : {
        'meta_info' : _MetaInfoClass('Snmp.Correlator.Rules.Rule.NonRootCauses.NonRootCause.VarBinds', REFERENCE_CLASS,
            '''Varbinds to match''',
            False, 
            [
            _MetaInfoClassMember('var-bind', REFERENCE_LIST, 'VarBind', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg', 'Snmp.Correlator.Rules.Rule.NonRootCauses.NonRootCause.VarBinds.VarBind',
                [], [],
                '''                Varbind match conditions
                ''',
                'var_bind',
                'Cisco-IOS-XR-snmp-agent-cfg', False),
            ],
            'Cisco-IOS-XR-snmp-agent-cfg',
            'var-binds',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-snmp-agent-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg',
        ),
    },
    'Snmp.Correlator.Rules.Rule.NonRootCauses.NonRootCause' : {
        'meta_info' : _MetaInfoClass('Snmp.Correlator.Rules.Rule.NonRootCauses.NonRootCause', REFERENCE_LIST,
            '''A non-rootcause''',
            False, 
            [
            _MetaInfoClassMember('oid', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                OID of nonrootcause trap (dotted decimal)
                ''',
                'oid',
                'Cisco-IOS-XR-snmp-agent-cfg', True),
            _MetaInfoClassMember('created', ATTRIBUTE, 'Empty', 'empty',
                None, None,
                [], [],
                '''                Create nonrootcause
                ''',
                'created',
                'Cisco-IOS-XR-snmp-agent-cfg', False),
            _MetaInfoClassMember('var-binds', REFERENCE_CLASS, 'VarBinds', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg', 'Snmp.Correlator.Rules.Rule.NonRootCauses.NonRootCause.VarBinds',
                [], [],
                '''                Varbinds to match
                ''',
                'var_binds',
                'Cisco-IOS-XR-snmp-agent-cfg', False),
            ],
            'Cisco-IOS-XR-snmp-agent-cfg',
            'non-root-cause',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-snmp-agent-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg',
        ),
    },
    'Snmp.Correlator.Rules.Rule.NonRootCauses' : {
        'meta_info' : _MetaInfoClass('Snmp.Correlator.Rules.Rule.NonRootCauses', REFERENCE_CLASS,
            '''Table of configured non-rootcause''',
            False, 
            [
            _MetaInfoClassMember('non-root-cause', REFERENCE_LIST, 'NonRootCause', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg', 'Snmp.Correlator.Rules.Rule.NonRootCauses.NonRootCause',
                [], [],
                '''                A non-rootcause
                ''',
                'non_root_cause',
                'Cisco-IOS-XR-snmp-agent-cfg', False),
            ],
            'Cisco-IOS-XR-snmp-agent-cfg',
            'non-root-causes',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-snmp-agent-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg',
        ),
    },
    'Snmp.Correlator.Rules.Rule.AppliedTo.Hosts.Host' : {
        'meta_info' : _MetaInfoClass('Snmp.Correlator.Rules.Rule.AppliedTo.Hosts.Host', REFERENCE_LIST,
            '''A destination host''',
            False, 
            [
            _MetaInfoClassMember('ip-address', REFERENCE_UNION, 'str', 'inet:ip-address-no-zone',
                None, None,
                [], [],
                '''                IP address
                ''',
                'ip_address',
                'Cisco-IOS-XR-snmp-agent-cfg', True, [
                    _MetaInfoClassMember('ip-address', ATTRIBUTE, 'str', 'inet:ipv4-address-no-zone',
                        None, None,
                        [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'],
                        '''                        IP address
                        ''',
                        'ip_address',
                        'Cisco-IOS-XR-snmp-agent-cfg', True),
                    _MetaInfoClassMember('ip-address', ATTRIBUTE, 'str', 'inet:ipv6-address-no-zone',
                        None, None,
                        [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'],
                        '''                        IP address
                        ''',
                        'ip_address',
                        'Cisco-IOS-XR-snmp-agent-cfg', True),
                ]),
            _MetaInfoClassMember('port', ATTRIBUTE, 'int', 'xr:Cisco-ios-xr-port-number',
                None, None,
                [('1', '65535')], [],
                '''                Port (specify 162 for default)
                ''',
                'port',
                'Cisco-IOS-XR-snmp-agent-cfg', True),
            ],
            'Cisco-IOS-XR-snmp-agent-cfg',
            'host',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-snmp-agent-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg',
        ),
    },
    'Snmp.Correlator.Rules.Rule.AppliedTo.Hosts' : {
        'meta_info' : _MetaInfoClass('Snmp.Correlator.Rules.Rule.AppliedTo.Hosts', REFERENCE_CLASS,
            '''Table of configured hosts to apply rules to''',
            False, 
            [
            _MetaInfoClassMember('host', REFERENCE_LIST, 'Host', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg', 'Snmp.Correlator.Rules.Rule.AppliedTo.Hosts.Host',
                [], [],
                '''                A destination host
                ''',
                'host',
                'Cisco-IOS-XR-snmp-agent-cfg', False),
            ],
            'Cisco-IOS-XR-snmp-agent-cfg',
            'hosts',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-snmp-agent-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg',
        ),
    },
    'Snmp.Correlator.Rules.Rule.AppliedTo' : {
        'meta_info' : _MetaInfoClass('Snmp.Correlator.Rules.Rule.AppliedTo', REFERENCE_CLASS,
            '''Applied to the Rule or Ruleset''',
            False, 
            [
            _MetaInfoClassMember('hosts', REFERENCE_CLASS, 'Hosts', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg', 'Snmp.Correlator.Rules.Rule.AppliedTo.Hosts',
                [], [],
                '''                Table of configured hosts to apply rules to
                ''',
                'hosts',
                'Cisco-IOS-XR-snmp-agent-cfg', False),
            _MetaInfoClassMember('all', ATTRIBUTE, 'Empty', 'empty',
                None, None,
                [], [],
                '''                Apply to all of the device
                ''',
                'all',
                'Cisco-IOS-XR-snmp-agent-cfg', False),
            ],
            'Cisco-IOS-XR-snmp-agent-cfg',
            'applied-to',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-snmp-agent-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg',
        ),
    },
    'Snmp.Correlator.Rules.Rule' : {
        'meta_info' : _MetaInfoClass('Snmp.Correlator.Rules.Rule', REFERENCE_LIST,
            '''Rule name''',
            False, 
            [
            _MetaInfoClassMember('name', ATTRIBUTE, 'str', 'string',
                None, None,
                [(1, 32)], [],
                '''                Rule name
                ''',
                'name',
                'Cisco-IOS-XR-snmp-agent-cfg', True),
            _MetaInfoClassMember('root-causes', REFERENCE_CLASS, 'RootCauses', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg', 'Snmp.Correlator.Rules.Rule.RootCauses',
                [], [],
                '''                Table of configured rootcause (only one entry
                allowed)
                ''',
                'root_causes',
                'Cisco-IOS-XR-snmp-agent-cfg', False),
            _MetaInfoClassMember('non-root-causes', REFERENCE_CLASS, 'NonRootCauses', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg', 'Snmp.Correlator.Rules.Rule.NonRootCauses',
                [], [],
                '''                Table of configured non-rootcause
                ''',
                'non_root_causes',
                'Cisco-IOS-XR-snmp-agent-cfg', False),
            _MetaInfoClassMember('timeout', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('1', '600000')], [],
                '''                Timeout (time to wait for active correlation)
                in milliseconds
                ''',
                'timeout',
                'Cisco-IOS-XR-snmp-agent-cfg', False),
            _MetaInfoClassMember('applied-to', REFERENCE_CLASS, 'AppliedTo', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg', 'Snmp.Correlator.Rules.Rule.AppliedTo',
                [], [],
                '''                Applied to the Rule or Ruleset
                ''',
                'applied_to',
                'Cisco-IOS-XR-snmp-agent-cfg', False),
            ],
            'Cisco-IOS-XR-snmp-agent-cfg',
            'rule',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-snmp-agent-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg',
        ),
    },
    'Snmp.Correlator.Rules' : {
        'meta_info' : _MetaInfoClass('Snmp.Correlator.Rules', REFERENCE_CLASS,
            '''Table of configured rules''',
            False, 
            [
            _MetaInfoClassMember('rule', REFERENCE_LIST, 'Rule', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg', 'Snmp.Correlator.Rules.Rule',
                [], [],
                '''                Rule name
                ''',
                'rule',
                'Cisco-IOS-XR-snmp-agent-cfg', False),
            ],
            'Cisco-IOS-XR-snmp-agent-cfg',
            'rules',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-snmp-agent-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg',
        ),
    },
    'Snmp.Correlator.RuleSets.RuleSet.Rulenames.Rulename' : {
        'meta_info' : _MetaInfoClass('Snmp.Correlator.RuleSets.RuleSet.Rulenames.Rulename', REFERENCE_LIST,
            '''A rulename''',
            False, 
            [
            _MetaInfoClassMember('rulename', ATTRIBUTE, 'str', 'string',
                None, None,
                [(1, 32)], [],
                '''                Rule name
                ''',
                'rulename',
                'Cisco-IOS-XR-snmp-agent-cfg', True),
            ],
            'Cisco-IOS-XR-snmp-agent-cfg',
            'rulename',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-snmp-agent-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg',
        ),
    },
    'Snmp.Correlator.RuleSets.RuleSet.Rulenames' : {
        'meta_info' : _MetaInfoClass('Snmp.Correlator.RuleSets.RuleSet.Rulenames', REFERENCE_CLASS,
            '''Table of configured rulenames''',
            False, 
            [
            _MetaInfoClassMember('rulename', REFERENCE_LIST, 'Rulename', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg', 'Snmp.Correlator.RuleSets.RuleSet.Rulenames.Rulename',
                [], [],
                '''                A rulename
                ''',
                'rulename',
                'Cisco-IOS-XR-snmp-agent-cfg', False),
            ],
            'Cisco-IOS-XR-snmp-agent-cfg',
            'rulenames',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-snmp-agent-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg',
        ),
    },
    'Snmp.Correlator.RuleSets.RuleSet.AppliedTo.Hosts.Host' : {
        'meta_info' : _MetaInfoClass('Snmp.Correlator.RuleSets.RuleSet.AppliedTo.Hosts.Host', REFERENCE_LIST,
            '''A destination host''',
            False, 
            [
            _MetaInfoClassMember('ip-address', REFERENCE_UNION, 'str', 'inet:ip-address-no-zone',
                None, None,
                [], [],
                '''                IP address
                ''',
                'ip_address',
                'Cisco-IOS-XR-snmp-agent-cfg', True, [
                    _MetaInfoClassMember('ip-address', ATTRIBUTE, 'str', 'inet:ipv4-address-no-zone',
                        None, None,
                        [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'],
                        '''                        IP address
                        ''',
                        'ip_address',
                        'Cisco-IOS-XR-snmp-agent-cfg', True),
                    _MetaInfoClassMember('ip-address', ATTRIBUTE, 'str', 'inet:ipv6-address-no-zone',
                        None, None,
                        [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'],
                        '''                        IP address
                        ''',
                        'ip_address',
                        'Cisco-IOS-XR-snmp-agent-cfg', True),
                ]),
            _MetaInfoClassMember('port', ATTRIBUTE, 'int', 'xr:Cisco-ios-xr-port-number',
                None, None,
                [('1', '65535')], [],
                '''                Port (specify 162 for default)
                ''',
                'port',
                'Cisco-IOS-XR-snmp-agent-cfg', True),
            ],
            'Cisco-IOS-XR-snmp-agent-cfg',
            'host',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-snmp-agent-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg',
        ),
    },
    'Snmp.Correlator.RuleSets.RuleSet.AppliedTo.Hosts' : {
        'meta_info' : _MetaInfoClass('Snmp.Correlator.RuleSets.RuleSet.AppliedTo.Hosts', REFERENCE_CLASS,
            '''Table of configured hosts to apply rules to''',
            False, 
            [
            _MetaInfoClassMember('host', REFERENCE_LIST, 'Host', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg', 'Snmp.Correlator.RuleSets.RuleSet.AppliedTo.Hosts.Host',
                [], [],
                '''                A destination host
                ''',
                'host',
                'Cisco-IOS-XR-snmp-agent-cfg', False),
            ],
            'Cisco-IOS-XR-snmp-agent-cfg',
            'hosts',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-snmp-agent-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg',
        ),
    },
    'Snmp.Correlator.RuleSets.RuleSet.AppliedTo' : {
        'meta_info' : _MetaInfoClass('Snmp.Correlator.RuleSets.RuleSet.AppliedTo', REFERENCE_CLASS,
            '''Applied to the Rule or Ruleset''',
            False, 
            [
            _MetaInfoClassMember('hosts', REFERENCE_CLASS, 'Hosts', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg', 'Snmp.Correlator.RuleSets.RuleSet.AppliedTo.Hosts',
                [], [],
                '''                Table of configured hosts to apply rules to
                ''',
                'hosts',
                'Cisco-IOS-XR-snmp-agent-cfg', False),
            _MetaInfoClassMember('all', ATTRIBUTE, 'Empty', 'empty',
                None, None,
                [], [],
                '''                Apply to all of the device
                ''',
                'all',
                'Cisco-IOS-XR-snmp-agent-cfg', False),
            ],
            'Cisco-IOS-XR-snmp-agent-cfg',
            'applied-to',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-snmp-agent-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg',
        ),
    },
    'Snmp.Correlator.RuleSets.RuleSet' : {
        'meta_info' : _MetaInfoClass('Snmp.Correlator.RuleSets.RuleSet', REFERENCE_LIST,
            '''Ruleset name''',
            False, 
            [
            _MetaInfoClassMember('name', ATTRIBUTE, 'str', 'string',
                None, None,
                [(1, 32)], [],
                '''                Ruleset name
                ''',
                'name',
                'Cisco-IOS-XR-snmp-agent-cfg', True),
            _MetaInfoClassMember('rulenames', REFERENCE_CLASS, 'Rulenames', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg', 'Snmp.Correlator.RuleSets.RuleSet.Rulenames',
                [], [],
                '''                Table of configured rulenames
                ''',
                'rulenames',
                'Cisco-IOS-XR-snmp-agent-cfg', False),
            _MetaInfoClassMember('applied-to', REFERENCE_CLASS, 'AppliedTo', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg', 'Snmp.Correlator.RuleSets.RuleSet.AppliedTo',
                [], [],
                '''                Applied to the Rule or Ruleset
                ''',
                'applied_to',
                'Cisco-IOS-XR-snmp-agent-cfg', False),
            ],
            'Cisco-IOS-XR-snmp-agent-cfg',
            'rule-set',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-snmp-agent-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg',
        ),
    },
    'Snmp.Correlator.RuleSets' : {
        'meta_info' : _MetaInfoClass('Snmp.Correlator.RuleSets', REFERENCE_CLASS,
            '''Table of configured rulesets''',
            False, 
            [
            _MetaInfoClassMember('rule-set', REFERENCE_LIST, 'RuleSet', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg', 'Snmp.Correlator.RuleSets.RuleSet',
                [], [],
                '''                Ruleset name
                ''',
                'rule_set',
                'Cisco-IOS-XR-snmp-agent-cfg', False),
            ],
            'Cisco-IOS-XR-snmp-agent-cfg',
            'rule-sets',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-snmp-agent-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg',
        ),
    },
    'Snmp.Correlator' : {
        'meta_info' : _MetaInfoClass('Snmp.Correlator', REFERENCE_CLASS,
            '''Configure properties of the trap correlator''',
            False, 
            [
            _MetaInfoClassMember('rules', REFERENCE_CLASS, 'Rules', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg', 'Snmp.Correlator.Rules',
                [], [],
                '''                Table of configured rules
                ''',
                'rules',
                'Cisco-IOS-XR-snmp-agent-cfg', False),
            _MetaInfoClassMember('rule-sets', REFERENCE_CLASS, 'RuleSets', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg', 'Snmp.Correlator.RuleSets',
                [], [],
                '''                Table of configured rulesets
                ''',
                'rule_sets',
                'Cisco-IOS-XR-snmp-agent-cfg', False),
            _MetaInfoClassMember('buffer-size', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('1024', '52428800')], [],
                '''                Configure size of the correlator buffer
                ''',
                'buffer_size',
                'Cisco-IOS-XR-snmp-agent-cfg', False),
            ],
            'Cisco-IOS-XR-snmp-agent-cfg',
            'correlator',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-snmp-agent-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg',
        ),
    },
    'Snmp.BulkStats.Schemas.Schema.Instance' : {
        'meta_info' : _MetaInfoClass('Snmp.BulkStats.Schemas.Schema.Instance', REFERENCE_CLASS,
            '''Object instance information''',
            False, 
            [
            _MetaInfoClassMember('type', REFERENCE_ENUM_CLASS, 'SnmpBulkstatSchema', 'Snmp-bulkstat-schema',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg', 'SnmpBulkstatSchema',
                [], [],
                '''                Type of the instance
                ''',
                'type',
                'Cisco-IOS-XR-snmp-agent-cfg', False, is_mandatory=True),
            _MetaInfoClassMember('instance', ATTRIBUTE, 'str', 'xr:Interface-name',
                None, None,
                [], [b'[a-zA-Z0-9._/-]+'],
                '''                Instance of the schema
                ''',
                'instance',
                'Cisco-IOS-XR-snmp-agent-cfg', False),
            _MetaInfoClassMember('start', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                Start Instance OID for repetition
                ''',
                'start',
                'Cisco-IOS-XR-snmp-agent-cfg', False, is_mandatory=True),
            _MetaInfoClassMember('end', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                End Instance OID for repetition
                ''',
                'end',
                'Cisco-IOS-XR-snmp-agent-cfg', False, is_mandatory=True),
            _MetaInfoClassMember('max', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('0', '4294967295')], [],
                '''                Max value of Instance repetition
                ''',
                'max',
                'Cisco-IOS-XR-snmp-agent-cfg', False, is_mandatory=True),
            _MetaInfoClassMember('sub-interface', ATTRIBUTE, 'bool', 'boolean',
                None, None,
                [], [],
                '''                Include all the subinterface
                ''',
                'sub_interface',
                'Cisco-IOS-XR-snmp-agent-cfg', False, is_mandatory=True),
            ],
            'Cisco-IOS-XR-snmp-agent-cfg',
            'instance',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-snmp-agent-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg',
            is_presence=True,
        ),
    },
    'Snmp.BulkStats.Schemas.Schema' : {
        'meta_info' : _MetaInfoClass('Snmp.BulkStats.Schemas.Schema', REFERENCE_LIST,
            '''The name of the Schema''',
            False, 
            [
            _MetaInfoClassMember('schema-name', ATTRIBUTE, 'str', 'xr:Cisco-ios-xr-string',
                None, None,
                [(1, 32)], [],
                '''                The name of the schema
                ''',
                'schema_name',
                'Cisco-IOS-XR-snmp-agent-cfg', True),
            _MetaInfoClassMember('instance', REFERENCE_CLASS, 'Instance', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg', 'Snmp.BulkStats.Schemas.Schema.Instance',
                [], [],
                '''                Object instance information
                ''',
                'instance',
                'Cisco-IOS-XR-snmp-agent-cfg', False, is_presence=True),
            _MetaInfoClassMember('type', ATTRIBUTE, 'Empty', 'empty',
                None, None,
                [], [],
                '''                Configure schema name
                ''',
                'type',
                'Cisco-IOS-XR-snmp-agent-cfg', False),
            _MetaInfoClassMember('schema-object-list', ATTRIBUTE, 'str', 'xr:Cisco-ios-xr-string',
                None, None,
                [(1, 32)], [],
                '''                Name of an object List
                ''',
                'schema_object_list',
                'Cisco-IOS-XR-snmp-agent-cfg', False),
            _MetaInfoClassMember('poll-interval', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('1', '20000')], [],
                '''                Periodicity for polling of objects in this
                schema in minutes
                ''',
                'poll_interval',
                'Cisco-IOS-XR-snmp-agent-cfg', False),
            ],
            'Cisco-IOS-XR-snmp-agent-cfg',
            'schema',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-snmp-agent-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg',
        ),
    },
    'Snmp.BulkStats.Schemas' : {
        'meta_info' : _MetaInfoClass('Snmp.BulkStats.Schemas', REFERENCE_CLASS,
            '''Configure schema definition''',
            False, 
            [
            _MetaInfoClassMember('schema', REFERENCE_LIST, 'Schema', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg', 'Snmp.BulkStats.Schemas.Schema',
                [], [],
                '''                The name of the Schema
                ''',
                'schema',
                'Cisco-IOS-XR-snmp-agent-cfg', False),
            ],
            'Cisco-IOS-XR-snmp-agent-cfg',
            'schemas',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-snmp-agent-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg',
        ),
    },
    'Snmp.BulkStats.Objects.Object.Objects_.Object_' : {
        'meta_info' : _MetaInfoClass('Snmp.BulkStats.Objects.Object.Objects_.Object_', REFERENCE_LIST,
            '''Object name or OID''',
            False, 
            [
            _MetaInfoClassMember('oid', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                Object name or OID 
                ''',
                'oid',
                'Cisco-IOS-XR-snmp-agent-cfg', True),
            ],
            'Cisco-IOS-XR-snmp-agent-cfg',
            'object',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-snmp-agent-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg',
        ),
    },
    'Snmp.BulkStats.Objects.Object.Objects_' : {
        'meta_info' : _MetaInfoClass('Snmp.BulkStats.Objects.Object.Objects_', REFERENCE_CLASS,
            '''Configure an object List''',
            False, 
            [
            _MetaInfoClassMember('object', REFERENCE_LIST, 'Object_', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg', 'Snmp.BulkStats.Objects.Object.Objects_.Object_',
                [], [],
                '''                Object name or OID
                ''',
                'object',
                'Cisco-IOS-XR-snmp-agent-cfg', False),
            ],
            'Cisco-IOS-XR-snmp-agent-cfg',
            'objects',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-snmp-agent-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg',
        ),
    },
    'Snmp.BulkStats.Objects.Object' : {
        'meta_info' : _MetaInfoClass('Snmp.BulkStats.Objects.Object', REFERENCE_LIST,
            '''Name of the object List''',
            False, 
            [
            _MetaInfoClassMember('object-list-name', ATTRIBUTE, 'str', 'xr:Cisco-ios-xr-string',
                None, None,
                [(1, 32)], [],
                '''                Name of the object List
                ''',
                'object_list_name',
                'Cisco-IOS-XR-snmp-agent-cfg', True),
            _MetaInfoClassMember('objects', REFERENCE_CLASS, 'Objects_', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg', 'Snmp.BulkStats.Objects.Object.Objects_',
                [], [],
                '''                Configure an object List
                ''',
                'objects',
                'Cisco-IOS-XR-snmp-agent-cfg', False),
            _MetaInfoClassMember('type', ATTRIBUTE, 'Empty', 'empty',
                None, None,
                [], [],
                '''                Configure object list name
                ''',
                'type',
                'Cisco-IOS-XR-snmp-agent-cfg', False),
            ],
            'Cisco-IOS-XR-snmp-agent-cfg',
            'object',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-snmp-agent-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg',
        ),
    },
    'Snmp.BulkStats.Objects' : {
        'meta_info' : _MetaInfoClass('Snmp.BulkStats.Objects', REFERENCE_CLASS,
            '''Configure an Object List ''',
            False, 
            [
            _MetaInfoClassMember('object', REFERENCE_LIST, 'Object', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg', 'Snmp.BulkStats.Objects.Object',
                [], [],
                '''                Name of the object List
                ''',
                'object',
                'Cisco-IOS-XR-snmp-agent-cfg', False),
            ],
            'Cisco-IOS-XR-snmp-agent-cfg',
            'objects',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-snmp-agent-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg',
        ),
    },
    'Snmp.BulkStats.Transfers.Transfer.TransferSchemas.TransferSchema' : {
        'meta_info' : _MetaInfoClass('Snmp.BulkStats.Transfers.Transfer.TransferSchemas.TransferSchema', REFERENCE_LIST,
            '''Schema that contains objects to be collected''',
            False, 
            [
            _MetaInfoClassMember('schema-name', ATTRIBUTE, 'str', 'xr:Cisco-ios-xr-string',
                None, None,
                [(1, 32)], [],
                '''                Schema that contains objects to be
                collected
                ''',
                'schema_name',
                'Cisco-IOS-XR-snmp-agent-cfg', True),
            ],
            'Cisco-IOS-XR-snmp-agent-cfg',
            'transfer-schema',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-snmp-agent-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg',
        ),
    },
    'Snmp.BulkStats.Transfers.Transfer.TransferSchemas' : {
        'meta_info' : _MetaInfoClass('Snmp.BulkStats.Transfers.Transfer.TransferSchemas', REFERENCE_CLASS,
            '''Schema that contains objects to be collected''',
            False, 
            [
            _MetaInfoClassMember('transfer-schema', REFERENCE_LIST, 'TransferSchema', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg', 'Snmp.BulkStats.Transfers.Transfer.TransferSchemas.TransferSchema',
                [], [],
                '''                Schema that contains objects to be collected
                ''',
                'transfer_schema',
                'Cisco-IOS-XR-snmp-agent-cfg', False),
            ],
            'Cisco-IOS-XR-snmp-agent-cfg',
            'transfer-schemas',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-snmp-agent-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg',
        ),
    },
    'Snmp.BulkStats.Transfers.Transfer' : {
        'meta_info' : _MetaInfoClass('Snmp.BulkStats.Transfers.Transfer', REFERENCE_LIST,
            '''Name of bulk transfer''',
            False, 
            [
            _MetaInfoClassMember('transfer-name', ATTRIBUTE, 'str', 'xr:Cisco-ios-xr-string',
                None, None,
                [(1, 32)], [],
                '''                Name of bulk transfer
                ''',
                'transfer_name',
                'Cisco-IOS-XR-snmp-agent-cfg', True),
            _MetaInfoClassMember('transfer-schemas', REFERENCE_CLASS, 'TransferSchemas', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg', 'Snmp.BulkStats.Transfers.Transfer.TransferSchemas',
                [], [],
                '''                Schema that contains objects to be collected
                ''',
                'transfer_schemas',
                'Cisco-IOS-XR-snmp-agent-cfg', False),
            _MetaInfoClassMember('secondary', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                FTP or rcp or TFTP can be used for file
                transfer
                ''',
                'secondary',
                'Cisco-IOS-XR-snmp-agent-cfg', False),
            _MetaInfoClassMember('type', ATTRIBUTE, 'Empty', 'empty',
                None, None,
                [], [],
                '''                Configure transfer list name
                ''',
                'type',
                'Cisco-IOS-XR-snmp-agent-cfg', False),
            _MetaInfoClassMember('buffer-size', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('1024', '2147483647')], [],
                '''                Bulkstat data file maximum size in bytes
                ''',
                'buffer_size',
                'Cisco-IOS-XR-snmp-agent-cfg', False),
            _MetaInfoClassMember('retain', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('0', '20000')], [],
                '''                Retention period in minutes
                ''',
                'retain',
                'Cisco-IOS-XR-snmp-agent-cfg', False),
            _MetaInfoClassMember('format', REFERENCE_ENUM_CLASS, 'SnmpBulkstatFileFormat', 'Snmp-bulkstat-file-format',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg', 'SnmpBulkstatFileFormat',
                [], [],
                '''                Format of the bulk data file
                ''',
                'format',
                'Cisco-IOS-XR-snmp-agent-cfg', False),
            _MetaInfoClassMember('retry', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('0', '100')], [],
                '''                Number of transmission retries
                ''',
                'retry',
                'Cisco-IOS-XR-snmp-agent-cfg', False),
            _MetaInfoClassMember('enable', ATTRIBUTE, 'Empty', 'empty',
                None, None,
                [], [],
                '''                Start Data Collection for this Configuration
                ''',
                'enable',
                'Cisco-IOS-XR-snmp-agent-cfg', False),
            _MetaInfoClassMember('primary', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                FTP or rcp or TFTP can be used for file
                transfer
                ''',
                'primary',
                'Cisco-IOS-XR-snmp-agent-cfg', False),
            _MetaInfoClassMember('interval', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('0', '4294967295')], [],
                '''                Periodicity for the transfer of bulk data in
                minutes
                ''',
                'interval',
                'Cisco-IOS-XR-snmp-agent-cfg', False),
            ],
            'Cisco-IOS-XR-snmp-agent-cfg',
            'transfer',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-snmp-agent-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg',
        ),
    },
    'Snmp.BulkStats.Transfers' : {
        'meta_info' : _MetaInfoClass('Snmp.BulkStats.Transfers', REFERENCE_CLASS,
            '''Periodicity for the transfer of bulk data in
minutes''',
            False, 
            [
            _MetaInfoClassMember('transfer', REFERENCE_LIST, 'Transfer', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg', 'Snmp.BulkStats.Transfers.Transfer',
                [], [],
                '''                Name of bulk transfer
                ''',
                'transfer',
                'Cisco-IOS-XR-snmp-agent-cfg', False),
            ],
            'Cisco-IOS-XR-snmp-agent-cfg',
            'transfers',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-snmp-agent-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg',
        ),
    },
    'Snmp.BulkStats' : {
        'meta_info' : _MetaInfoClass('Snmp.BulkStats', REFERENCE_CLASS,
            '''SNMP bulk stats configuration commands''',
            False, 
            [
            _MetaInfoClassMember('schemas', REFERENCE_CLASS, 'Schemas', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg', 'Snmp.BulkStats.Schemas',
                [], [],
                '''                Configure schema definition
                ''',
                'schemas',
                'Cisco-IOS-XR-snmp-agent-cfg', False),
            _MetaInfoClassMember('objects', REFERENCE_CLASS, 'Objects', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg', 'Snmp.BulkStats.Objects',
                [], [],
                '''                Configure an Object List 
                ''',
                'objects',
                'Cisco-IOS-XR-snmp-agent-cfg', False),
            _MetaInfoClassMember('transfers', REFERENCE_CLASS, 'Transfers', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg', 'Snmp.BulkStats.Transfers',
                [], [],
                '''                Periodicity for the transfer of bulk data in
                minutes
                ''',
                'transfers',
                'Cisco-IOS-XR-snmp-agent-cfg', False),
            _MetaInfoClassMember('memory', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('100', '200000')], [],
                '''                per process memory limit in kilo bytes
                ''',
                'memory',
                'Cisco-IOS-XR-snmp-agent-cfg', False),
            ],
            'Cisco-IOS-XR-snmp-agent-cfg',
            'bulk-stats',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-snmp-agent-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg',
        ),
    },
    'Snmp.DefaultCommunityMaps.DefaultCommunityMap' : {
        'meta_info' : _MetaInfoClass('Snmp.DefaultCommunityMaps.DefaultCommunityMap', REFERENCE_LIST,
            '''Unencrpted SNMP community map name ''',
            False, 
            [
            _MetaInfoClassMember('community-name', ATTRIBUTE, 'str', 'xr:Cisco-ios-xr-string',
                None, None,
                [(1, 128)], [],
                '''                SNMP community map
                ''',
                'community_name',
                'Cisco-IOS-XR-snmp-agent-cfg', True),
            _MetaInfoClassMember('context', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                SNMP Context Name 
                ''',
                'context',
                'Cisco-IOS-XR-snmp-agent-cfg', False),
            _MetaInfoClassMember('security', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                SNMP Security Name 
                ''',
                'security',
                'Cisco-IOS-XR-snmp-agent-cfg', False),
            _MetaInfoClassMember('target-list', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                target list name 
                ''',
                'target_list',
                'Cisco-IOS-XR-snmp-agent-cfg', False),
            ],
            'Cisco-IOS-XR-snmp-agent-cfg',
            'default-community-map',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-snmp-agent-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg',
        ),
    },
    'Snmp.DefaultCommunityMaps' : {
        'meta_info' : _MetaInfoClass('Snmp.DefaultCommunityMaps', REFERENCE_CLASS,
            '''Container class to hold unencrpted community map''',
            False, 
            [
            _MetaInfoClassMember('default-community-map', REFERENCE_LIST, 'DefaultCommunityMap', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg', 'Snmp.DefaultCommunityMaps.DefaultCommunityMap',
                [], [],
                '''                Unencrpted SNMP community map name 
                ''',
                'default_community_map',
                'Cisco-IOS-XR-snmp-agent-cfg', False),
            ],
            'Cisco-IOS-XR-snmp-agent-cfg',
            'default-community-maps',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-snmp-agent-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg',
        ),
    },
    'Snmp.OverloadControl' : {
        'meta_info' : _MetaInfoClass('Snmp.OverloadControl', REFERENCE_CLASS,
            '''Set overload control params for handling
incoming messages''',
            False, 
            [
            _MetaInfoClassMember('drop-time', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('0', '300')], [],
                '''                Drop time in seconds for incoming queue
                (default 1 sec)
                ''',
                'drop_time',
                'Cisco-IOS-XR-snmp-agent-cfg', False, is_mandatory=True),
            _MetaInfoClassMember('throttle-rate', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('0', '1000')], [],
                '''                Throttle time in milliseconds for incoming
                queue (default 500 msec)
                ''',
                'throttle_rate',
                'Cisco-IOS-XR-snmp-agent-cfg', False, is_mandatory=True),
            ],
            'Cisco-IOS-XR-snmp-agent-cfg',
            'overload-control',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-snmp-agent-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg',
            is_presence=True,
        ),
    },
    'Snmp.Timeouts' : {
        'meta_info' : _MetaInfoClass('Snmp.Timeouts', REFERENCE_CLASS,
            '''SNMP timeouts''',
            False, 
            [
            _MetaInfoClassMember('duplicates', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('0', '20')], [],
                '''                Duplicate request feature timeout
                ''',
                'duplicates',
                'Cisco-IOS-XR-snmp-agent-cfg', False, default_value="1"),
            _MetaInfoClassMember('in-qdrop', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('0', '20')], [],
                '''                incoming queue drop feature timeout
                ''',
                'in_qdrop',
                'Cisco-IOS-XR-snmp-agent-cfg', False, default_value="10"),
            _MetaInfoClassMember('threshold', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('0', '100000')], [],
                '''                Threshold request feature timeout
                ''',
                'threshold',
                'Cisco-IOS-XR-snmp-agent-cfg', False, default_value="50000"),
            _MetaInfoClassMember('subagent', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('1', '20')], [],
                '''                Sub-Agent Request timeout
                ''',
                'subagent',
                'Cisco-IOS-XR-snmp-agent-cfg', False, default_value="10"),
            _MetaInfoClassMember('pdu-stats', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('1', '10')], [],
                '''                SNMP pdu statistics timeout
                ''',
                'pdu_stats',
                'Cisco-IOS-XR-snmp-agent-cfg', False, default_value="2"),
            ],
            'Cisco-IOS-XR-snmp-agent-cfg',
            'timeouts',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-snmp-agent-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg',
        ),
    },
    'Snmp.Users.User' : {
        'meta_info' : _MetaInfoClass('Snmp.Users.User', REFERENCE_LIST,
            '''Name of the user''',
            False, 
            [
            _MetaInfoClassMember('user-name', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                Name of the user
                ''',
                'user_name',
                'Cisco-IOS-XR-snmp-agent-cfg', True),
            _MetaInfoClassMember('group-name', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                Group to which the user belongs
                ''',
                'group_name',
                'Cisco-IOS-XR-snmp-agent-cfg', False, is_mandatory=True),
            _MetaInfoClassMember('version', REFERENCE_ENUM_CLASS, 'UserSnmpVersion', 'User-snmp-version',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg', 'UserSnmpVersion',
                [], [],
                '''                SNMP version to be used. v1,v2c or v3
                ''',
                'version',
                'Cisco-IOS-XR-snmp-agent-cfg', False, is_mandatory=True),
            _MetaInfoClassMember('authentication-password-configured', ATTRIBUTE, 'Empty', 'empty',
                None, None,
                [], [],
                '''                Flag to indicate that authentication password
                is configred for version 3
                ''',
                'authentication_password_configured',
                'Cisco-IOS-XR-snmp-agent-cfg', False),
            _MetaInfoClassMember('algorithm', REFERENCE_ENUM_CLASS, 'SnmpHashAlgorithm', 'Snmp-hash-algorithm',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg', 'SnmpHashAlgorithm',
                [], [],
                '''                The algorithm used md5 or sha
                ''',
                'algorithm',
                'Cisco-IOS-XR-snmp-agent-cfg', False),
            _MetaInfoClassMember('authentication-password', ATTRIBUTE, 'str', 'xr:Proprietary-password',
                None, None,
                [], [b'(!.+)|([^!].+)'],
                '''                The authentication password
                ''',
                'authentication_password',
                'Cisco-IOS-XR-snmp-agent-cfg', False),
            _MetaInfoClassMember('privacy-password-configured', ATTRIBUTE, 'Empty', 'empty',
                None, None,
                [], [],
                '''                Flag to indicate that the privacy password is
                configured for version 3
                ''',
                'privacy_password_configured',
                'Cisco-IOS-XR-snmp-agent-cfg', False),
            _MetaInfoClassMember('priv-algorithm', REFERENCE_ENUM_CLASS, 'SnmpPrivAlgorithm', 'Snmp-priv-algorithm',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg', 'SnmpPrivAlgorithm',
                [], [],
                '''                The algorithm used des56 or aes128 or aes192or
                aes256 or 3des
                ''',
                'priv_algorithm',
                'Cisco-IOS-XR-snmp-agent-cfg', False),
            _MetaInfoClassMember('privacy-password', ATTRIBUTE, 'str', 'xr:Proprietary-password',
                None, None,
                [], [b'(!.+)|([^!].+)'],
                '''                The privacy password
                ''',
                'privacy_password',
                'Cisco-IOS-XR-snmp-agent-cfg', False),
            _MetaInfoClassMember('v4acl-type', REFERENCE_ENUM_CLASS, 'Snmpacl', 'Snmpacl',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg', 'Snmpacl',
                [], [],
                '''                Access-list type
                ''',
                'v4acl_type',
                'Cisco-IOS-XR-snmp-agent-cfg', False),
            _MetaInfoClassMember('v4-access-list', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                Ipv4 Access-list name
                ''',
                'v4_access_list',
                'Cisco-IOS-XR-snmp-agent-cfg', False),
            _MetaInfoClassMember('v6acl-type', REFERENCE_ENUM_CLASS, 'Snmpacl', 'Snmpacl',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg', 'Snmpacl',
                [], [],
                '''                Access-list type
                ''',
                'v6acl_type',
                'Cisco-IOS-XR-snmp-agent-cfg', False),
            _MetaInfoClassMember('v6-access-list', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                Ipv6 Access-list name
                ''',
                'v6_access_list',
                'Cisco-IOS-XR-snmp-agent-cfg', False),
            _MetaInfoClassMember('owner', REFERENCE_ENUM_CLASS, 'SnmpOwnerAccess', 'Snmp-owner-access',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg', 'SnmpOwnerAccess',
                [], [],
                '''                The system access either SDROwner or
                SystemOwner
                ''',
                'owner',
                'Cisco-IOS-XR-snmp-agent-cfg', False),
            _MetaInfoClassMember('remote-address', REFERENCE_UNION, 'str', 'inet:ip-address-no-zone',
                None, None,
                [], [],
                '''                IP address of remote SNMP entity
                ''',
                'remote_address',
                'Cisco-IOS-XR-snmp-agent-cfg', False, [
                    _MetaInfoClassMember('remote-address', ATTRIBUTE, 'str', 'inet:ipv4-address-no-zone',
                        None, None,
                        [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'],
                        '''                        IP address of remote SNMP entity
                        ''',
                        'remote_address',
                        'Cisco-IOS-XR-snmp-agent-cfg', False),
                    _MetaInfoClassMember('remote-address', ATTRIBUTE, 'str', 'inet:ipv6-address-no-zone',
                        None, None,
                        [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'],
                        '''                        IP address of remote SNMP entity
                        ''',
                        'remote_address',
                        'Cisco-IOS-XR-snmp-agent-cfg', False),
                ]),
            _MetaInfoClassMember('port', ATTRIBUTE, 'int', 'xr:Cisco-ios-xr-port-number',
                None, None,
                [('1', '65535')], [],
                '''                UDP port number
                ''',
                'port',
                'Cisco-IOS-XR-snmp-agent-cfg', False),
            ],
            'Cisco-IOS-XR-snmp-agent-cfg',
            'user',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-snmp-agent-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg',
        ),
    },
    'Snmp.Users' : {
        'meta_info' : _MetaInfoClass('Snmp.Users', REFERENCE_CLASS,
            '''Define a user who can access the SNMP engine''',
            False, 
            [
            _MetaInfoClassMember('user', REFERENCE_LIST, 'User', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg', 'Snmp.Users.User',
                [], [],
                '''                Name of the user
                ''',
                'user',
                'Cisco-IOS-XR-snmp-agent-cfg', False),
            ],
            'Cisco-IOS-XR-snmp-agent-cfg',
            'users',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-snmp-agent-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg',
        ),
    },
    'Snmp.Vrfs.Vrf.TrapHosts.TrapHost.EncryptedUserCommunities.EncryptedUserCommunity' : {
        'meta_info' : _MetaInfoClass('Snmp.Vrfs.Vrf.TrapHosts.TrapHost.EncryptedUserCommunities.EncryptedUserCommunity', REFERENCE_LIST,
            '''Clear/Encrypt Community name associated with
a trap host''',
            False, 
            [
            _MetaInfoClassMember('community-name', ATTRIBUTE, 'str', 'xr:Cisco-ios-xr-string',
                None, None,
                [], [b'[\\w\\-\\.:,_@#%$\\+=\\|;]+'],
                '''                SNMPv1/v2c community string or SNMPv3 user
                ''',
                'community_name',
                'Cisco-IOS-XR-snmp-agent-cfg', True),
            _MetaInfoClassMember('port', ATTRIBUTE, 'int', 'xr:Cisco-ios-xr-port-number',
                None, None,
                [('1', '65535')], [],
                '''                UDP port number
                ''',
                'port',
                'Cisco-IOS-XR-snmp-agent-cfg', False, default_value="162"),
            _MetaInfoClassMember('version', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                SNMP Version to be used 1/2c/3
                ''',
                'version',
                'Cisco-IOS-XR-snmp-agent-cfg', False, default_value="'1'"),
            _MetaInfoClassMember('security-level', REFERENCE_ENUM_CLASS, 'SnmpSecurityModel', 'Snmp-security-model',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg', 'SnmpSecurityModel',
                [], [],
                '''                Security level to be used noauth/auth/priv
                ''',
                'security_level',
                'Cisco-IOS-XR-snmp-agent-cfg', False),
            _MetaInfoClassMember('basic-trap-types', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('0', '4294967295')], [],
                '''                Number to signify the feature traps that
                needs to be setBasicTrapTypes is used for
                all traps except copy-completeSet this value
                to an integer corresponding to the trapBGP
                8192, CONFIG 4096,SYSLOG 131072,SNMP_TRAP
                1COPY_COMPLETE_TRAP 64To provide a
                combination of trap Add the respective
                numbersValue must be set to 0 for all traps
                ''',
                'basic_trap_types',
                'Cisco-IOS-XR-snmp-agent-cfg', False, default_value="0"),
            _MetaInfoClassMember('advanced-trap-types1', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('0', '4294967295')], [],
                '''                Number to signify the feature traps that
                needs to be setUse this for providing
                copy-complete trapValue must be set to 0 if
                not used
                ''',
                'advanced_trap_types1',
                'Cisco-IOS-XR-snmp-agent-cfg', False, default_value="0"),
            _MetaInfoClassMember('advanced-trap-types2', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('0', '4294967295')], [],
                '''                Number to signify the feature traps that
                needs to be setvalue should always to set as
                0
                ''',
                'advanced_trap_types2',
                'Cisco-IOS-XR-snmp-agent-cfg', False, default_value="0"),
            ],
            'Cisco-IOS-XR-snmp-agent-cfg',
            'encrypted-user-community',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-snmp-agent-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg',
        ),
    },
    'Snmp.Vrfs.Vrf.TrapHosts.TrapHost.EncryptedUserCommunities' : {
        'meta_info' : _MetaInfoClass('Snmp.Vrfs.Vrf.TrapHosts.TrapHost.EncryptedUserCommunities', REFERENCE_CLASS,
            '''Container class for defining Clear/encrypt
communities for a trap host''',
            False, 
            [
            _MetaInfoClassMember('encrypted-user-community', REFERENCE_LIST, 'EncryptedUserCommunity', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg', 'Snmp.Vrfs.Vrf.TrapHosts.TrapHost.EncryptedUserCommunities.EncryptedUserCommunity',
                [], [],
                '''                Clear/Encrypt Community name associated with
                a trap host
                ''',
                'encrypted_user_community',
                'Cisco-IOS-XR-snmp-agent-cfg', False),
            ],
            'Cisco-IOS-XR-snmp-agent-cfg',
            'encrypted-user-communities',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-snmp-agent-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg',
        ),
    },
    'Snmp.Vrfs.Vrf.TrapHosts.TrapHost.InformHost.InformUserCommunities.InformUserCommunity' : {
        'meta_info' : _MetaInfoClass('Snmp.Vrfs.Vrf.TrapHosts.TrapHost.InformHost.InformUserCommunities.InformUserCommunity', REFERENCE_LIST,
            '''Unencrpted Community name associated with a
inform host''',
            False, 
            [
            _MetaInfoClassMember('community-name', ATTRIBUTE, 'str', 'xr:Cisco-ios-xr-string',
                None, None,
                [(1, 128)], [],
                '''                SNMPv2c community string or SNMPv3 user
                ''',
                'community_name',
                'Cisco-IOS-XR-snmp-agent-cfg', True),
            _MetaInfoClassMember('port', ATTRIBUTE, 'int', 'xr:Cisco-ios-xr-port-number',
                None, None,
                [('1', '65535')], [],
                '''                UDP port number
                ''',
                'port',
                'Cisco-IOS-XR-snmp-agent-cfg', False, default_value="162"),
            _MetaInfoClassMember('version', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                SNMP Version to be used 2c/3
                ''',
                'version',
                'Cisco-IOS-XR-snmp-agent-cfg', False, default_value="'2c'"),
            _MetaInfoClassMember('security-level', REFERENCE_ENUM_CLASS, 'SnmpSecurityModel', 'Snmp-security-model',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg', 'SnmpSecurityModel',
                [], [],
                '''                Security level to be used noauth/auth/priv
                ''',
                'security_level',
                'Cisco-IOS-XR-snmp-agent-cfg', False),
            _MetaInfoClassMember('basic-trap-types', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('0', '4294967295')], [],
                '''                Number to signify the feature traps that
                needs to be setBasicTrapTypes is used for
                all traps except copy-completeSet this
                value to an integer corresponding to the
                trapBGP 8192, CONFIG 4096,SYSLOG 131072
                ,SNMP_TRAP 1COPY_COMPLETE_TRAP 64To provide
                a combination of trap Add the respective
                numbersValue must be set to 0 for all traps
                ''',
                'basic_trap_types',
                'Cisco-IOS-XR-snmp-agent-cfg', False, default_value="0"),
            _MetaInfoClassMember('advanced-trap-types1', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('0', '4294967295')], [],
                '''                Number to signify the feature traps that
                needs to be setUse this for providing
                copy-complete trapValue must be set to 0 if
                not used
                ''',
                'advanced_trap_types1',
                'Cisco-IOS-XR-snmp-agent-cfg', False, default_value="0"),
            _MetaInfoClassMember('advanced-trap-types2', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('0', '4294967295')], [],
                '''                Number to signify the feature traps that
                needs to be setvalue should always to set
                as 0
                ''',
                'advanced_trap_types2',
                'Cisco-IOS-XR-snmp-agent-cfg', False, default_value="0"),
            ],
            'Cisco-IOS-XR-snmp-agent-cfg',
            'inform-user-community',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-snmp-agent-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg',
        ),
    },
    'Snmp.Vrfs.Vrf.TrapHosts.TrapHost.InformHost.InformUserCommunities' : {
        'meta_info' : _MetaInfoClass('Snmp.Vrfs.Vrf.TrapHosts.TrapHost.InformHost.InformUserCommunities', REFERENCE_CLASS,
            '''Container class for defining communities for
a inform host''',
            False, 
            [
            _MetaInfoClassMember('inform-user-community', REFERENCE_LIST, 'InformUserCommunity', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg', 'Snmp.Vrfs.Vrf.TrapHosts.TrapHost.InformHost.InformUserCommunities.InformUserCommunity',
                [], [],
                '''                Unencrpted Community name associated with a
                inform host
                ''',
                'inform_user_community',
                'Cisco-IOS-XR-snmp-agent-cfg', False),
            ],
            'Cisco-IOS-XR-snmp-agent-cfg',
            'inform-user-communities',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-snmp-agent-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg',
        ),
    },
    'Snmp.Vrfs.Vrf.TrapHosts.TrapHost.InformHost.InformEncryptedUserCommunities.InformEncryptedUserCommunity' : {
        'meta_info' : _MetaInfoClass('Snmp.Vrfs.Vrf.TrapHosts.TrapHost.InformHost.InformEncryptedUserCommunities.InformEncryptedUserCommunity', REFERENCE_LIST,
            '''Clear/Encrypt Community name associated with
a inform host''',
            False, 
            [
            _MetaInfoClassMember('community-name', ATTRIBUTE, 'str', 'xr:Cisco-ios-xr-string',
                None, None,
                [], [b'[\\w\\-\\.:,_@#%$\\+=\\|;]+'],
                '''                SNMPv2c community string or SNMPv3 user
                ''',
                'community_name',
                'Cisco-IOS-XR-snmp-agent-cfg', True),
            _MetaInfoClassMember('port', ATTRIBUTE, 'int', 'xr:Cisco-ios-xr-port-number',
                None, None,
                [('1', '65535')], [],
                '''                UDP port number
                ''',
                'port',
                'Cisco-IOS-XR-snmp-agent-cfg', False, default_value="162"),
            _MetaInfoClassMember('version', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                SNMP Version to be used 2c/3
                ''',
                'version',
                'Cisco-IOS-XR-snmp-agent-cfg', False, default_value="'2c'"),
            _MetaInfoClassMember('security-level', REFERENCE_ENUM_CLASS, 'SnmpSecurityModel', 'Snmp-security-model',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg', 'SnmpSecurityModel',
                [], [],
                '''                Security level to be used noauth/auth/priv
                ''',
                'security_level',
                'Cisco-IOS-XR-snmp-agent-cfg', False),
            _MetaInfoClassMember('basic-trap-types', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('0', '4294967295')], [],
                '''                Number to signify the feature traps that
                needs to be setBasicTrapTypes is used for
                all traps except copy-completeSet this
                value to an integer corresponding to the
                trapBGP 8192, CONFIG 4096,SYSLOG 131072
                ,SNMP_TRAP 1COPY_COMPLETE_TRAP 64To provide
                a combination of trap Add the respective
                numbersValue must be set to 0 for all traps
                ''',
                'basic_trap_types',
                'Cisco-IOS-XR-snmp-agent-cfg', False, default_value="0"),
            _MetaInfoClassMember('advanced-trap-types1', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('0', '4294967295')], [],
                '''                Number to signify the feature traps that
                needs to be setUse this for providing
                copy-complete trapValue must be set to 0 if
                not used
                ''',
                'advanced_trap_types1',
                'Cisco-IOS-XR-snmp-agent-cfg', False, default_value="0"),
            _MetaInfoClassMember('advanced-trap-types2', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('0', '4294967295')], [],
                '''                Number to signify the feature traps that
                needs to be setvalue should always to set
                as 0
                ''',
                'advanced_trap_types2',
                'Cisco-IOS-XR-snmp-agent-cfg', False, default_value="0"),
            ],
            'Cisco-IOS-XR-snmp-agent-cfg',
            'inform-encrypted-user-community',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-snmp-agent-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg',
        ),
    },
    'Snmp.Vrfs.Vrf.TrapHosts.TrapHost.InformHost.InformEncryptedUserCommunities' : {
        'meta_info' : _MetaInfoClass('Snmp.Vrfs.Vrf.TrapHosts.TrapHost.InformHost.InformEncryptedUserCommunities', REFERENCE_CLASS,
            '''Container class for defining Clear/encrypt
communities for a inform host''',
            False, 
            [
            _MetaInfoClassMember('inform-encrypted-user-community', REFERENCE_LIST, 'InformEncryptedUserCommunity', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg', 'Snmp.Vrfs.Vrf.TrapHosts.TrapHost.InformHost.InformEncryptedUserCommunities.InformEncryptedUserCommunity',
                [], [],
                '''                Clear/Encrypt Community name associated with
                a inform host
                ''',
                'inform_encrypted_user_community',
                'Cisco-IOS-XR-snmp-agent-cfg', False),
            ],
            'Cisco-IOS-XR-snmp-agent-cfg',
            'inform-encrypted-user-communities',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-snmp-agent-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg',
        ),
    },
    'Snmp.Vrfs.Vrf.TrapHosts.TrapHost.InformHost' : {
        'meta_info' : _MetaInfoClass('Snmp.Vrfs.Vrf.TrapHosts.TrapHost.InformHost', REFERENCE_CLASS,
            '''Container class for defining notification type
for a Inform host''',
            False, 
            [
            _MetaInfoClassMember('inform-user-communities', REFERENCE_CLASS, 'InformUserCommunities', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg', 'Snmp.Vrfs.Vrf.TrapHosts.TrapHost.InformHost.InformUserCommunities',
                [], [],
                '''                Container class for defining communities for
                a inform host
                ''',
                'inform_user_communities',
                'Cisco-IOS-XR-snmp-agent-cfg', False),
            _MetaInfoClassMember('inform-encrypted-user-communities', REFERENCE_CLASS, 'InformEncryptedUserCommunities', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg', 'Snmp.Vrfs.Vrf.TrapHosts.TrapHost.InformHost.InformEncryptedUserCommunities',
                [], [],
                '''                Container class for defining Clear/encrypt
                communities for a inform host
                ''',
                'inform_encrypted_user_communities',
                'Cisco-IOS-XR-snmp-agent-cfg', False),
            ],
            'Cisco-IOS-XR-snmp-agent-cfg',
            'inform-host',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-snmp-agent-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg',
        ),
    },
    'Snmp.Vrfs.Vrf.TrapHosts.TrapHost.DefaultUserCommunities.DefaultUserCommunity' : {
        'meta_info' : _MetaInfoClass('Snmp.Vrfs.Vrf.TrapHosts.TrapHost.DefaultUserCommunities.DefaultUserCommunity', REFERENCE_LIST,
            '''Unencrpted Community name associated with a
trap host''',
            False, 
            [
            _MetaInfoClassMember('community-name', ATTRIBUTE, 'str', 'xr:Cisco-ios-xr-string',
                None, None,
                [(1, 128)], [],
                '''                SNMPv1/v2c community string or SNMPv3 user
                ''',
                'community_name',
                'Cisco-IOS-XR-snmp-agent-cfg', True),
            _MetaInfoClassMember('port', ATTRIBUTE, 'int', 'xr:Cisco-ios-xr-port-number',
                None, None,
                [('1', '65535')], [],
                '''                UDP port number
                ''',
                'port',
                'Cisco-IOS-XR-snmp-agent-cfg', False, default_value="162"),
            _MetaInfoClassMember('version', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                SNMP Version to be used 1/2c/3
                ''',
                'version',
                'Cisco-IOS-XR-snmp-agent-cfg', False, default_value="'1'"),
            _MetaInfoClassMember('security-level', REFERENCE_ENUM_CLASS, 'SnmpSecurityModel', 'Snmp-security-model',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg', 'SnmpSecurityModel',
                [], [],
                '''                Security level to be used noauth/auth/priv
                ''',
                'security_level',
                'Cisco-IOS-XR-snmp-agent-cfg', False),
            _MetaInfoClassMember('basic-trap-types', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('0', '4294967295')], [],
                '''                Number to signify the feature traps that
                needs to be setBasicTrapTypes is used for
                all traps except copy-completeSet this value
                to an integer corresponding to the trapBGP
                8192, CONFIG 4096,SYSLOG 131072,SNMP_TRAP
                1COPY_COMPLETE_TRAP 64To provide a
                combination of trap Add the respective
                numbersValue must be set to 0 for all traps
                ''',
                'basic_trap_types',
                'Cisco-IOS-XR-snmp-agent-cfg', False, default_value="0"),
            _MetaInfoClassMember('advanced-trap-types1', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('0', '4294967295')], [],
                '''                Number to signify the feature traps that
                needs to be setUse this for providing
                copy-complete trapValue must be set to 0 if
                not used
                ''',
                'advanced_trap_types1',
                'Cisco-IOS-XR-snmp-agent-cfg', False, default_value="0"),
            _MetaInfoClassMember('advanced-trap-types2', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('0', '4294967295')], [],
                '''                Number to signify the feature traps that
                needs to be setvalue should always to set as
                0
                ''',
                'advanced_trap_types2',
                'Cisco-IOS-XR-snmp-agent-cfg', False, default_value="0"),
            ],
            'Cisco-IOS-XR-snmp-agent-cfg',
            'default-user-community',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-snmp-agent-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg',
        ),
    },
    'Snmp.Vrfs.Vrf.TrapHosts.TrapHost.DefaultUserCommunities' : {
        'meta_info' : _MetaInfoClass('Snmp.Vrfs.Vrf.TrapHosts.TrapHost.DefaultUserCommunities', REFERENCE_CLASS,
            '''Container class for defining communities for a
trap host''',
            False, 
            [
            _MetaInfoClassMember('default-user-community', REFERENCE_LIST, 'DefaultUserCommunity', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg', 'Snmp.Vrfs.Vrf.TrapHosts.TrapHost.DefaultUserCommunities.DefaultUserCommunity',
                [], [],
                '''                Unencrpted Community name associated with a
                trap host
                ''',
                'default_user_community',
                'Cisco-IOS-XR-snmp-agent-cfg', False),
            ],
            'Cisco-IOS-XR-snmp-agent-cfg',
            'default-user-communities',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-snmp-agent-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg',
        ),
    },
    'Snmp.Vrfs.Vrf.TrapHosts.TrapHost' : {
        'meta_info' : _MetaInfoClass('Snmp.Vrfs.Vrf.TrapHosts.TrapHost', REFERENCE_LIST,
            '''Specify hosts to receive SNMP notifications''',
            False, 
            [
            _MetaInfoClassMember('ip-address', REFERENCE_UNION, 'str', 'inet:ip-address-no-zone',
                None, None,
                [], [],
                '''                IP address of SNMP notification host
                ''',
                'ip_address',
                'Cisco-IOS-XR-snmp-agent-cfg', True, [
                    _MetaInfoClassMember('ip-address', ATTRIBUTE, 'str', 'inet:ipv4-address-no-zone',
                        None, None,
                        [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'],
                        '''                        IP address of SNMP notification host
                        ''',
                        'ip_address',
                        'Cisco-IOS-XR-snmp-agent-cfg', True),
                    _MetaInfoClassMember('ip-address', ATTRIBUTE, 'str', 'inet:ipv6-address-no-zone',
                        None, None,
                        [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'],
                        '''                        IP address of SNMP notification host
                        ''',
                        'ip_address',
                        'Cisco-IOS-XR-snmp-agent-cfg', True),
                ]),
            _MetaInfoClassMember('encrypted-user-communities', REFERENCE_CLASS, 'EncryptedUserCommunities', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg', 'Snmp.Vrfs.Vrf.TrapHosts.TrapHost.EncryptedUserCommunities',
                [], [],
                '''                Container class for defining Clear/encrypt
                communities for a trap host
                ''',
                'encrypted_user_communities',
                'Cisco-IOS-XR-snmp-agent-cfg', False),
            _MetaInfoClassMember('inform-host', REFERENCE_CLASS, 'InformHost', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg', 'Snmp.Vrfs.Vrf.TrapHosts.TrapHost.InformHost',
                [], [],
                '''                Container class for defining notification type
                for a Inform host
                ''',
                'inform_host',
                'Cisco-IOS-XR-snmp-agent-cfg', False),
            _MetaInfoClassMember('default-user-communities', REFERENCE_CLASS, 'DefaultUserCommunities', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg', 'Snmp.Vrfs.Vrf.TrapHosts.TrapHost.DefaultUserCommunities',
                [], [],
                '''                Container class for defining communities for a
                trap host
                ''',
                'default_user_communities',
                'Cisco-IOS-XR-snmp-agent-cfg', False),
            ],
            'Cisco-IOS-XR-snmp-agent-cfg',
            'trap-host',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-snmp-agent-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg',
        ),
    },
    'Snmp.Vrfs.Vrf.TrapHosts' : {
        'meta_info' : _MetaInfoClass('Snmp.Vrfs.Vrf.TrapHosts', REFERENCE_CLASS,
            '''Specify hosts to receive SNMP notifications''',
            False, 
            [
            _MetaInfoClassMember('trap-host', REFERENCE_LIST, 'TrapHost', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg', 'Snmp.Vrfs.Vrf.TrapHosts.TrapHost',
                [], [],
                '''                Specify hosts to receive SNMP notifications
                ''',
                'trap_host',
                'Cisco-IOS-XR-snmp-agent-cfg', False),
            ],
            'Cisco-IOS-XR-snmp-agent-cfg',
            'trap-hosts',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-snmp-agent-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg',
        ),
    },
    'Snmp.Vrfs.Vrf.Contexts.Context' : {
        'meta_info' : _MetaInfoClass('Snmp.Vrfs.Vrf.Contexts.Context', REFERENCE_LIST,
            '''Context Name''',
            False, 
            [
            _MetaInfoClassMember('context-name', ATTRIBUTE, 'str', 'xr:Cisco-ios-xr-string',
                None, None,
                [], [b'[\\w\\-\\.:,_@#%$\\+=\\|;]+'],
                '''                Context Name
                ''',
                'context_name',
                'Cisco-IOS-XR-snmp-agent-cfg', True),
            ],
            'Cisco-IOS-XR-snmp-agent-cfg',
            'context',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-snmp-agent-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg',
        ),
    },
    'Snmp.Vrfs.Vrf.Contexts' : {
        'meta_info' : _MetaInfoClass('Snmp.Vrfs.Vrf.Contexts', REFERENCE_CLASS,
            '''List of Context Names''',
            False, 
            [
            _MetaInfoClassMember('context', REFERENCE_LIST, 'Context', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg', 'Snmp.Vrfs.Vrf.Contexts.Context',
                [], [],
                '''                Context Name
                ''',
                'context',
                'Cisco-IOS-XR-snmp-agent-cfg', False),
            ],
            'Cisco-IOS-XR-snmp-agent-cfg',
            'contexts',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-snmp-agent-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg',
        ),
    },
    'Snmp.Vrfs.Vrf.ContextMappings.ContextMapping' : {
        'meta_info' : _MetaInfoClass('Snmp.Vrfs.Vrf.ContextMappings.ContextMapping', REFERENCE_LIST,
            '''Context mapping name''',
            False, 
            [
            _MetaInfoClassMember('context-mapping-name', ATTRIBUTE, 'str', 'xr:Cisco-ios-xr-string',
                None, None,
                [], [b'[\\w\\-\\.:,_@#%$\\+=\\|;]+'],
                '''                Context mapping name
                ''',
                'context_mapping_name',
                'Cisco-IOS-XR-snmp-agent-cfg', True),
            _MetaInfoClassMember('context', REFERENCE_ENUM_CLASS, 'SnmpContext', 'Snmp-context',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg', 'SnmpContext',
                [], [],
                '''                SNMP context feature type
                ''',
                'context',
                'Cisco-IOS-XR-snmp-agent-cfg', False),
            _MetaInfoClassMember('instance-name', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                OSPF protocol instance
                ''',
                'instance_name',
                'Cisco-IOS-XR-snmp-agent-cfg', False),
            _MetaInfoClassMember('vrf-name', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                VRF name associated with the context
                ''',
                'vrf_name',
                'Cisco-IOS-XR-snmp-agent-cfg', False),
            _MetaInfoClassMember('topology-name', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                Topology name associated with the context
                ''',
                'topology_name',
                'Cisco-IOS-XR-snmp-agent-cfg', False),
            ],
            'Cisco-IOS-XR-snmp-agent-cfg',
            'context-mapping',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-snmp-agent-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg',
        ),
    },
    'Snmp.Vrfs.Vrf.ContextMappings' : {
        'meta_info' : _MetaInfoClass('Snmp.Vrfs.Vrf.ContextMappings', REFERENCE_CLASS,
            '''List of context names''',
            False, 
            [
            _MetaInfoClassMember('context-mapping', REFERENCE_LIST, 'ContextMapping', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg', 'Snmp.Vrfs.Vrf.ContextMappings.ContextMapping',
                [], [],
                '''                Context mapping name
                ''',
                'context_mapping',
                'Cisco-IOS-XR-snmp-agent-cfg', False),
            ],
            'Cisco-IOS-XR-snmp-agent-cfg',
            'context-mappings',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-snmp-agent-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg',
        ),
    },
    'Snmp.Vrfs.Vrf' : {
        'meta_info' : _MetaInfoClass('Snmp.Vrfs.Vrf', REFERENCE_LIST,
            '''VRF name''',
            False, 
            [
            _MetaInfoClassMember('name', ATTRIBUTE, 'str', 'xr:Cisco-ios-xr-string',
                None, None,
                [], [b'[\\w\\-\\.:,_@#%$\\+=\\|;]+'],
                '''                VRF name
                ''',
                'name',
                'Cisco-IOS-XR-snmp-agent-cfg', True),
            _MetaInfoClassMember('trap-hosts', REFERENCE_CLASS, 'TrapHosts', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg', 'Snmp.Vrfs.Vrf.TrapHosts',
                [], [],
                '''                Specify hosts to receive SNMP notifications
                ''',
                'trap_hosts',
                'Cisco-IOS-XR-snmp-agent-cfg', False),
            _MetaInfoClassMember('contexts', REFERENCE_CLASS, 'Contexts', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg', 'Snmp.Vrfs.Vrf.Contexts',
                [], [],
                '''                List of Context Names
                ''',
                'contexts',
                'Cisco-IOS-XR-snmp-agent-cfg', False),
            _MetaInfoClassMember('context-mappings', REFERENCE_CLASS, 'ContextMappings', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg', 'Snmp.Vrfs.Vrf.ContextMappings',
                [], [],
                '''                List of context names
                ''',
                'context_mappings',
                'Cisco-IOS-XR-snmp-agent-cfg', False),
            ],
            'Cisco-IOS-XR-snmp-agent-cfg',
            'vrf',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-snmp-agent-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg',
        ),
    },
    'Snmp.Vrfs' : {
        'meta_info' : _MetaInfoClass('Snmp.Vrfs', REFERENCE_CLASS,
            '''SNMP VRF configuration commands''',
            False, 
            [
            _MetaInfoClassMember('vrf', REFERENCE_LIST, 'Vrf', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg', 'Snmp.Vrfs.Vrf',
                [], [],
                '''                VRF name
                ''',
                'vrf',
                'Cisco-IOS-XR-snmp-agent-cfg', False),
            ],
            'Cisco-IOS-XR-snmp-agent-cfg',
            'vrfs',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-snmp-agent-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg',
        ),
    },
    'Snmp.Groups.Group' : {
        'meta_info' : _MetaInfoClass('Snmp.Groups.Group', REFERENCE_LIST,
            '''Name of the group''',
            False, 
            [
            _MetaInfoClassMember('name', ATTRIBUTE, 'str', 'xr:Cisco-ios-xr-string',
                None, None,
                [(1, 128)], [],
                '''                Name of the group
                ''',
                'name',
                'Cisco-IOS-XR-snmp-agent-cfg', True),
            _MetaInfoClassMember('snmp-version', REFERENCE_ENUM_CLASS, 'GroupSnmpVersion', 'Group-snmp-version',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg', 'GroupSnmpVersion',
                [], [],
                '''                snmp version
                ''',
                'snmp_version',
                'Cisco-IOS-XR-snmp-agent-cfg', False, is_mandatory=True),
            _MetaInfoClassMember('security-model', REFERENCE_ENUM_CLASS, 'SnmpSecurityModel', 'Snmp-security-model',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg', 'SnmpSecurityModel',
                [], [],
                '''                security model like auth/noAuth/Priv
                applicable for v3
                ''',
                'security_model',
                'Cisco-IOS-XR-snmp-agent-cfg', False),
            _MetaInfoClassMember('notify-view', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                notify view name
                ''',
                'notify_view',
                'Cisco-IOS-XR-snmp-agent-cfg', False),
            _MetaInfoClassMember('read-view', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                read view name
                ''',
                'read_view',
                'Cisco-IOS-XR-snmp-agent-cfg', False),
            _MetaInfoClassMember('write-view', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                write view name
                ''',
                'write_view',
                'Cisco-IOS-XR-snmp-agent-cfg', False),
            _MetaInfoClassMember('v4acl-type', REFERENCE_ENUM_CLASS, 'Snmpacl', 'Snmpacl',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg', 'Snmpacl',
                [], [],
                '''                Access-list type
                ''',
                'v4acl_type',
                'Cisco-IOS-XR-snmp-agent-cfg', False),
            _MetaInfoClassMember('v4-access-list', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                Ipv4 Access-list name
                ''',
                'v4_access_list',
                'Cisco-IOS-XR-snmp-agent-cfg', False),
            _MetaInfoClassMember('v6acl-type', REFERENCE_ENUM_CLASS, 'Snmpacl', 'Snmpacl',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg', 'Snmpacl',
                [], [],
                '''                Access-list type
                ''',
                'v6acl_type',
                'Cisco-IOS-XR-snmp-agent-cfg', False),
            _MetaInfoClassMember('v6-access-list', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                Ipv6 Access-list name
                ''',
                'v6_access_list',
                'Cisco-IOS-XR-snmp-agent-cfg', False),
            _MetaInfoClassMember('context-name', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                Context name
                ''',
                'context_name',
                'Cisco-IOS-XR-snmp-agent-cfg', False),
            ],
            'Cisco-IOS-XR-snmp-agent-cfg',
            'group',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-snmp-agent-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg',
        ),
    },
    'Snmp.Groups' : {
        'meta_info' : _MetaInfoClass('Snmp.Groups', REFERENCE_CLASS,
            '''Define a User Security Model group''',
            False, 
            [
            _MetaInfoClassMember('group', REFERENCE_LIST, 'Group', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg', 'Snmp.Groups.Group',
                [], [],
                '''                Name of the group
                ''',
                'group',
                'Cisco-IOS-XR-snmp-agent-cfg', False),
            ],
            'Cisco-IOS-XR-snmp-agent-cfg',
            'groups',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-snmp-agent-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg',
        ),
    },
    'Snmp.TrapHosts.TrapHost.EncryptedUserCommunities.EncryptedUserCommunity' : {
        'meta_info' : _MetaInfoClass('Snmp.TrapHosts.TrapHost.EncryptedUserCommunities.EncryptedUserCommunity', REFERENCE_LIST,
            '''Clear/Encrypt Community name associated with
a trap host''',
            False, 
            [
            _MetaInfoClassMember('community-name', ATTRIBUTE, 'str', 'xr:Cisco-ios-xr-string',
                None, None,
                [], [b'[\\w\\-\\.:,_@#%$\\+=\\|;]+'],
                '''                SNMPv1/v2c community string or SNMPv3 user
                ''',
                'community_name',
                'Cisco-IOS-XR-snmp-agent-cfg', True),
            _MetaInfoClassMember('port', ATTRIBUTE, 'int', 'xr:Cisco-ios-xr-port-number',
                None, None,
                [('1', '65535')], [],
                '''                UDP port number
                ''',
                'port',
                'Cisco-IOS-XR-snmp-agent-cfg', False, default_value="162"),
            _MetaInfoClassMember('version', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                SNMP Version to be used 1/2c/3
                ''',
                'version',
                'Cisco-IOS-XR-snmp-agent-cfg', False, default_value="'1'"),
            _MetaInfoClassMember('security-level', REFERENCE_ENUM_CLASS, 'SnmpSecurityModel', 'Snmp-security-model',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg', 'SnmpSecurityModel',
                [], [],
                '''                Security level to be used noauth/auth/priv
                ''',
                'security_level',
                'Cisco-IOS-XR-snmp-agent-cfg', False),
            _MetaInfoClassMember('basic-trap-types', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('0', '4294967295')], [],
                '''                Number to signify the feature traps that
                needs to be setBasicTrapTypes is used for
                all traps except copy-completeSet this value
                to an integer corresponding to the trapBGP
                8192, CONFIG 4096,SYSLOG 131072,SNMP_TRAP
                1COPY_COMPLETE_TRAP 64To provide a
                combination of trap Add the respective
                numbersValue must be set to 0 for all traps
                ''',
                'basic_trap_types',
                'Cisco-IOS-XR-snmp-agent-cfg', False, default_value="0"),
            _MetaInfoClassMember('advanced-trap-types1', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('0', '4294967295')], [],
                '''                Number to signify the feature traps that
                needs to be setUse this for providing
                copy-complete trapValue must be set to 0 if
                not used
                ''',
                'advanced_trap_types1',
                'Cisco-IOS-XR-snmp-agent-cfg', False, default_value="0"),
            _MetaInfoClassMember('advanced-trap-types2', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('0', '4294967295')], [],
                '''                Number to signify the feature traps that
                needs to be setvalue should always to set as
                0
                ''',
                'advanced_trap_types2',
                'Cisco-IOS-XR-snmp-agent-cfg', False, default_value="0"),
            ],
            'Cisco-IOS-XR-snmp-agent-cfg',
            'encrypted-user-community',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-snmp-agent-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg',
        ),
    },
    'Snmp.TrapHosts.TrapHost.EncryptedUserCommunities' : {
        'meta_info' : _MetaInfoClass('Snmp.TrapHosts.TrapHost.EncryptedUserCommunities', REFERENCE_CLASS,
            '''Container class for defining Clear/encrypt
communities for a trap host''',
            False, 
            [
            _MetaInfoClassMember('encrypted-user-community', REFERENCE_LIST, 'EncryptedUserCommunity', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg', 'Snmp.TrapHosts.TrapHost.EncryptedUserCommunities.EncryptedUserCommunity',
                [], [],
                '''                Clear/Encrypt Community name associated with
                a trap host
                ''',
                'encrypted_user_community',
                'Cisco-IOS-XR-snmp-agent-cfg', False),
            ],
            'Cisco-IOS-XR-snmp-agent-cfg',
            'encrypted-user-communities',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-snmp-agent-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg',
        ),
    },
    'Snmp.TrapHosts.TrapHost.InformHost.InformUserCommunities.InformUserCommunity' : {
        'meta_info' : _MetaInfoClass('Snmp.TrapHosts.TrapHost.InformHost.InformUserCommunities.InformUserCommunity', REFERENCE_LIST,
            '''Unencrpted Community name associated with a
inform host''',
            False, 
            [
            _MetaInfoClassMember('community-name', ATTRIBUTE, 'str', 'xr:Cisco-ios-xr-string',
                None, None,
                [(1, 128)], [],
                '''                SNMPv2c community string or SNMPv3 user
                ''',
                'community_name',
                'Cisco-IOS-XR-snmp-agent-cfg', True),
            _MetaInfoClassMember('port', ATTRIBUTE, 'int', 'xr:Cisco-ios-xr-port-number',
                None, None,
                [('1', '65535')], [],
                '''                UDP port number
                ''',
                'port',
                'Cisco-IOS-XR-snmp-agent-cfg', False, default_value="162"),
            _MetaInfoClassMember('version', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                SNMP Version to be used 2c/3
                ''',
                'version',
                'Cisco-IOS-XR-snmp-agent-cfg', False, default_value="'2c'"),
            _MetaInfoClassMember('security-level', REFERENCE_ENUM_CLASS, 'SnmpSecurityModel', 'Snmp-security-model',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg', 'SnmpSecurityModel',
                [], [],
                '''                Security level to be used noauth/auth/priv
                ''',
                'security_level',
                'Cisco-IOS-XR-snmp-agent-cfg', False),
            _MetaInfoClassMember('basic-trap-types', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('0', '4294967295')], [],
                '''                Number to signify the feature traps that
                needs to be setBasicTrapTypes is used for
                all traps except copy-completeSet this
                value to an integer corresponding to the
                trapBGP 8192, CONFIG 4096,SYSLOG 131072
                ,SNMP_TRAP 1COPY_COMPLETE_TRAP 64To provide
                a combination of trap Add the respective
                numbersValue must be set to 0 for all traps
                ''',
                'basic_trap_types',
                'Cisco-IOS-XR-snmp-agent-cfg', False, default_value="0"),
            _MetaInfoClassMember('advanced-trap-types1', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('0', '4294967295')], [],
                '''                Number to signify the feature traps that
                needs to be setUse this for providing
                copy-complete trapValue must be set to 0 if
                not used
                ''',
                'advanced_trap_types1',
                'Cisco-IOS-XR-snmp-agent-cfg', False, default_value="0"),
            _MetaInfoClassMember('advanced-trap-types2', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('0', '4294967295')], [],
                '''                Number to signify the feature traps that
                needs to be setvalue should always to set
                as 0
                ''',
                'advanced_trap_types2',
                'Cisco-IOS-XR-snmp-agent-cfg', False, default_value="0"),
            ],
            'Cisco-IOS-XR-snmp-agent-cfg',
            'inform-user-community',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-snmp-agent-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg',
        ),
    },
    'Snmp.TrapHosts.TrapHost.InformHost.InformUserCommunities' : {
        'meta_info' : _MetaInfoClass('Snmp.TrapHosts.TrapHost.InformHost.InformUserCommunities', REFERENCE_CLASS,
            '''Container class for defining communities for
a inform host''',
            False, 
            [
            _MetaInfoClassMember('inform-user-community', REFERENCE_LIST, 'InformUserCommunity', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg', 'Snmp.TrapHosts.TrapHost.InformHost.InformUserCommunities.InformUserCommunity',
                [], [],
                '''                Unencrpted Community name associated with a
                inform host
                ''',
                'inform_user_community',
                'Cisco-IOS-XR-snmp-agent-cfg', False),
            ],
            'Cisco-IOS-XR-snmp-agent-cfg',
            'inform-user-communities',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-snmp-agent-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg',
        ),
    },
    'Snmp.TrapHosts.TrapHost.InformHost.InformEncryptedUserCommunities.InformEncryptedUserCommunity' : {
        'meta_info' : _MetaInfoClass('Snmp.TrapHosts.TrapHost.InformHost.InformEncryptedUserCommunities.InformEncryptedUserCommunity', REFERENCE_LIST,
            '''Clear/Encrypt Community name associated with
a inform host''',
            False, 
            [
            _MetaInfoClassMember('community-name', ATTRIBUTE, 'str', 'xr:Cisco-ios-xr-string',
                None, None,
                [], [b'[\\w\\-\\.:,_@#%$\\+=\\|;]+'],
                '''                SNMPv2c community string or SNMPv3 user
                ''',
                'community_name',
                'Cisco-IOS-XR-snmp-agent-cfg', True),
            _MetaInfoClassMember('port', ATTRIBUTE, 'int', 'xr:Cisco-ios-xr-port-number',
                None, None,
                [('1', '65535')], [],
                '''                UDP port number
                ''',
                'port',
                'Cisco-IOS-XR-snmp-agent-cfg', False, default_value="162"),
            _MetaInfoClassMember('version', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                SNMP Version to be used 2c/3
                ''',
                'version',
                'Cisco-IOS-XR-snmp-agent-cfg', False, default_value="'2c'"),
            _MetaInfoClassMember('security-level', REFERENCE_ENUM_CLASS, 'SnmpSecurityModel', 'Snmp-security-model',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg', 'SnmpSecurityModel',
                [], [],
                '''                Security level to be used noauth/auth/priv
                ''',
                'security_level',
                'Cisco-IOS-XR-snmp-agent-cfg', False),
            _MetaInfoClassMember('basic-trap-types', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('0', '4294967295')], [],
                '''                Number to signify the feature traps that
                needs to be setBasicTrapTypes is used for
                all traps except copy-completeSet this
                value to an integer corresponding to the
                trapBGP 8192, CONFIG 4096,SYSLOG 131072
                ,SNMP_TRAP 1COPY_COMPLETE_TRAP 64To provide
                a combination of trap Add the respective
                numbersValue must be set to 0 for all traps
                ''',
                'basic_trap_types',
                'Cisco-IOS-XR-snmp-agent-cfg', False, default_value="0"),
            _MetaInfoClassMember('advanced-trap-types1', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('0', '4294967295')], [],
                '''                Number to signify the feature traps that
                needs to be setUse this for providing
                copy-complete trapValue must be set to 0 if
                not used
                ''',
                'advanced_trap_types1',
                'Cisco-IOS-XR-snmp-agent-cfg', False, default_value="0"),
            _MetaInfoClassMember('advanced-trap-types2', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('0', '4294967295')], [],
                '''                Number to signify the feature traps that
                needs to be setvalue should always to set
                as 0
                ''',
                'advanced_trap_types2',
                'Cisco-IOS-XR-snmp-agent-cfg', False, default_value="0"),
            ],
            'Cisco-IOS-XR-snmp-agent-cfg',
            'inform-encrypted-user-community',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-snmp-agent-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg',
        ),
    },
    'Snmp.TrapHosts.TrapHost.InformHost.InformEncryptedUserCommunities' : {
        'meta_info' : _MetaInfoClass('Snmp.TrapHosts.TrapHost.InformHost.InformEncryptedUserCommunities', REFERENCE_CLASS,
            '''Container class for defining Clear/encrypt
communities for a inform host''',
            False, 
            [
            _MetaInfoClassMember('inform-encrypted-user-community', REFERENCE_LIST, 'InformEncryptedUserCommunity', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg', 'Snmp.TrapHosts.TrapHost.InformHost.InformEncryptedUserCommunities.InformEncryptedUserCommunity',
                [], [],
                '''                Clear/Encrypt Community name associated with
                a inform host
                ''',
                'inform_encrypted_user_community',
                'Cisco-IOS-XR-snmp-agent-cfg', False),
            ],
            'Cisco-IOS-XR-snmp-agent-cfg',
            'inform-encrypted-user-communities',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-snmp-agent-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg',
        ),
    },
    'Snmp.TrapHosts.TrapHost.InformHost' : {
        'meta_info' : _MetaInfoClass('Snmp.TrapHosts.TrapHost.InformHost', REFERENCE_CLASS,
            '''Container class for defining notification type
for a Inform host''',
            False, 
            [
            _MetaInfoClassMember('inform-user-communities', REFERENCE_CLASS, 'InformUserCommunities', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg', 'Snmp.TrapHosts.TrapHost.InformHost.InformUserCommunities',
                [], [],
                '''                Container class for defining communities for
                a inform host
                ''',
                'inform_user_communities',
                'Cisco-IOS-XR-snmp-agent-cfg', False),
            _MetaInfoClassMember('inform-encrypted-user-communities', REFERENCE_CLASS, 'InformEncryptedUserCommunities', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg', 'Snmp.TrapHosts.TrapHost.InformHost.InformEncryptedUserCommunities',
                [], [],
                '''                Container class for defining Clear/encrypt
                communities for a inform host
                ''',
                'inform_encrypted_user_communities',
                'Cisco-IOS-XR-snmp-agent-cfg', False),
            ],
            'Cisco-IOS-XR-snmp-agent-cfg',
            'inform-host',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-snmp-agent-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg',
        ),
    },
    'Snmp.TrapHosts.TrapHost.DefaultUserCommunities.DefaultUserCommunity' : {
        'meta_info' : _MetaInfoClass('Snmp.TrapHosts.TrapHost.DefaultUserCommunities.DefaultUserCommunity', REFERENCE_LIST,
            '''Unencrpted Community name associated with a
trap host''',
            False, 
            [
            _MetaInfoClassMember('community-name', ATTRIBUTE, 'str', 'xr:Cisco-ios-xr-string',
                None, None,
                [(1, 128)], [],
                '''                SNMPv1/v2c community string or SNMPv3 user
                ''',
                'community_name',
                'Cisco-IOS-XR-snmp-agent-cfg', True),
            _MetaInfoClassMember('port', ATTRIBUTE, 'int', 'xr:Cisco-ios-xr-port-number',
                None, None,
                [('1', '65535')], [],
                '''                UDP port number
                ''',
                'port',
                'Cisco-IOS-XR-snmp-agent-cfg', False, default_value="162"),
            _MetaInfoClassMember('version', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                SNMP Version to be used 1/2c/3
                ''',
                'version',
                'Cisco-IOS-XR-snmp-agent-cfg', False, default_value="'1'"),
            _MetaInfoClassMember('security-level', REFERENCE_ENUM_CLASS, 'SnmpSecurityModel', 'Snmp-security-model',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg', 'SnmpSecurityModel',
                [], [],
                '''                Security level to be used noauth/auth/priv
                ''',
                'security_level',
                'Cisco-IOS-XR-snmp-agent-cfg', False),
            _MetaInfoClassMember('basic-trap-types', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('0', '4294967295')], [],
                '''                Number to signify the feature traps that
                needs to be setBasicTrapTypes is used for
                all traps except copy-completeSet this value
                to an integer corresponding to the trapBGP
                8192, CONFIG 4096,SYSLOG 131072,SNMP_TRAP
                1COPY_COMPLETE_TRAP 64To provide a
                combination of trap Add the respective
                numbersValue must be set to 0 for all traps
                ''',
                'basic_trap_types',
                'Cisco-IOS-XR-snmp-agent-cfg', False, default_value="0"),
            _MetaInfoClassMember('advanced-trap-types1', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('0', '4294967295')], [],
                '''                Number to signify the feature traps that
                needs to be setUse this for providing
                copy-complete trapValue must be set to 0 if
                not used
                ''',
                'advanced_trap_types1',
                'Cisco-IOS-XR-snmp-agent-cfg', False, default_value="0"),
            _MetaInfoClassMember('advanced-trap-types2', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('0', '4294967295')], [],
                '''                Number to signify the feature traps that
                needs to be setvalue should always to set as
                0
                ''',
                'advanced_trap_types2',
                'Cisco-IOS-XR-snmp-agent-cfg', False, default_value="0"),
            ],
            'Cisco-IOS-XR-snmp-agent-cfg',
            'default-user-community',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-snmp-agent-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg',
        ),
    },
    'Snmp.TrapHosts.TrapHost.DefaultUserCommunities' : {
        'meta_info' : _MetaInfoClass('Snmp.TrapHosts.TrapHost.DefaultUserCommunities', REFERENCE_CLASS,
            '''Container class for defining communities for a
trap host''',
            False, 
            [
            _MetaInfoClassMember('default-user-community', REFERENCE_LIST, 'DefaultUserCommunity', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg', 'Snmp.TrapHosts.TrapHost.DefaultUserCommunities.DefaultUserCommunity',
                [], [],
                '''                Unencrpted Community name associated with a
                trap host
                ''',
                'default_user_community',
                'Cisco-IOS-XR-snmp-agent-cfg', False),
            ],
            'Cisco-IOS-XR-snmp-agent-cfg',
            'default-user-communities',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-snmp-agent-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg',
        ),
    },
    'Snmp.TrapHosts.TrapHost' : {
        'meta_info' : _MetaInfoClass('Snmp.TrapHosts.TrapHost', REFERENCE_LIST,
            '''Specify hosts to receive SNMP notifications''',
            False, 
            [
            _MetaInfoClassMember('ip-address', REFERENCE_UNION, 'str', 'inet:ip-address-no-zone',
                None, None,
                [], [],
                '''                IP address of SNMP notification host
                ''',
                'ip_address',
                'Cisco-IOS-XR-snmp-agent-cfg', True, [
                    _MetaInfoClassMember('ip-address', ATTRIBUTE, 'str', 'inet:ipv4-address-no-zone',
                        None, None,
                        [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'],
                        '''                        IP address of SNMP notification host
                        ''',
                        'ip_address',
                        'Cisco-IOS-XR-snmp-agent-cfg', True),
                    _MetaInfoClassMember('ip-address', ATTRIBUTE, 'str', 'inet:ipv6-address-no-zone',
                        None, None,
                        [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'],
                        '''                        IP address of SNMP notification host
                        ''',
                        'ip_address',
                        'Cisco-IOS-XR-snmp-agent-cfg', True),
                ]),
            _MetaInfoClassMember('encrypted-user-communities', REFERENCE_CLASS, 'EncryptedUserCommunities', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg', 'Snmp.TrapHosts.TrapHost.EncryptedUserCommunities',
                [], [],
                '''                Container class for defining Clear/encrypt
                communities for a trap host
                ''',
                'encrypted_user_communities',
                'Cisco-IOS-XR-snmp-agent-cfg', False),
            _MetaInfoClassMember('inform-host', REFERENCE_CLASS, 'InformHost', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg', 'Snmp.TrapHosts.TrapHost.InformHost',
                [], [],
                '''                Container class for defining notification type
                for a Inform host
                ''',
                'inform_host',
                'Cisco-IOS-XR-snmp-agent-cfg', False),
            _MetaInfoClassMember('default-user-communities', REFERENCE_CLASS, 'DefaultUserCommunities', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg', 'Snmp.TrapHosts.TrapHost.DefaultUserCommunities',
                [], [],
                '''                Container class for defining communities for a
                trap host
                ''',
                'default_user_communities',
                'Cisco-IOS-XR-snmp-agent-cfg', False),
            ],
            'Cisco-IOS-XR-snmp-agent-cfg',
            'trap-host',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-snmp-agent-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg',
        ),
    },
    'Snmp.TrapHosts' : {
        'meta_info' : _MetaInfoClass('Snmp.TrapHosts', REFERENCE_CLASS,
            '''Specify hosts to receive SNMP notifications''',
            False, 
            [
            _MetaInfoClassMember('trap-host', REFERENCE_LIST, 'TrapHost', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg', 'Snmp.TrapHosts.TrapHost',
                [], [],
                '''                Specify hosts to receive SNMP notifications
                ''',
                'trap_host',
                'Cisco-IOS-XR-snmp-agent-cfg', False),
            ],
            'Cisco-IOS-XR-snmp-agent-cfg',
            'trap-hosts',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-snmp-agent-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg',
        ),
    },
    'Snmp.Contexts.Context' : {
        'meta_info' : _MetaInfoClass('Snmp.Contexts.Context', REFERENCE_LIST,
            '''Context Name''',
            False, 
            [
            _MetaInfoClassMember('context-name', ATTRIBUTE, 'str', 'xr:Cisco-ios-xr-string',
                None, None,
                [], [b'[\\w\\-\\.:,_@#%$\\+=\\|;]+'],
                '''                Context Name
                ''',
                'context_name',
                'Cisco-IOS-XR-snmp-agent-cfg', True),
            ],
            'Cisco-IOS-XR-snmp-agent-cfg',
            'context',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-snmp-agent-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg',
        ),
    },
    'Snmp.Contexts' : {
        'meta_info' : _MetaInfoClass('Snmp.Contexts', REFERENCE_CLASS,
            '''List of Context Names''',
            False, 
            [
            _MetaInfoClassMember('context', REFERENCE_LIST, 'Context', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg', 'Snmp.Contexts.Context',
                [], [],
                '''                Context Name
                ''',
                'context',
                'Cisco-IOS-XR-snmp-agent-cfg', False),
            ],
            'Cisco-IOS-XR-snmp-agent-cfg',
            'contexts',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-snmp-agent-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg',
        ),
    },
    'Snmp.ContextMappings.ContextMapping' : {
        'meta_info' : _MetaInfoClass('Snmp.ContextMappings.ContextMapping', REFERENCE_LIST,
            '''Context mapping name''',
            False, 
            [
            _MetaInfoClassMember('context-mapping-name', ATTRIBUTE, 'str', 'xr:Cisco-ios-xr-string',
                None, None,
                [], [b'[\\w\\-\\.:,_@#%$\\+=\\|;]+'],
                '''                Context mapping name
                ''',
                'context_mapping_name',
                'Cisco-IOS-XR-snmp-agent-cfg', True),
            _MetaInfoClassMember('context', REFERENCE_ENUM_CLASS, 'SnmpContext', 'Snmp-context',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg', 'SnmpContext',
                [], [],
                '''                SNMP context feature type
                ''',
                'context',
                'Cisco-IOS-XR-snmp-agent-cfg', False),
            _MetaInfoClassMember('instance-name', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                OSPF protocol instance
                ''',
                'instance_name',
                'Cisco-IOS-XR-snmp-agent-cfg', False),
            _MetaInfoClassMember('vrf-name', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                VRF name associated with the context
                ''',
                'vrf_name',
                'Cisco-IOS-XR-snmp-agent-cfg', False),
            _MetaInfoClassMember('topology-name', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                Topology name associated with the context
                ''',
                'topology_name',
                'Cisco-IOS-XR-snmp-agent-cfg', False),
            ],
            'Cisco-IOS-XR-snmp-agent-cfg',
            'context-mapping',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-snmp-agent-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg',
        ),
    },
    'Snmp.ContextMappings' : {
        'meta_info' : _MetaInfoClass('Snmp.ContextMappings', REFERENCE_CLASS,
            '''List of context names''',
            False, 
            [
            _MetaInfoClassMember('context-mapping', REFERENCE_LIST, 'ContextMapping', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg', 'Snmp.ContextMappings.ContextMapping',
                [], [],
                '''                Context mapping name
                ''',
                'context_mapping',
                'Cisco-IOS-XR-snmp-agent-cfg', False),
            ],
            'Cisco-IOS-XR-snmp-agent-cfg',
            'context-mappings',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-snmp-agent-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg',
        ),
    },
    'Snmp' : {
        'meta_info' : _MetaInfoClass('Snmp', REFERENCE_CLASS,
            '''The heirarchy point for all the SNMP
configurations''',
            False, 
            [
            _MetaInfoClassMember('encrypted-community-maps', REFERENCE_CLASS, 'EncryptedCommunityMaps', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg', 'Snmp.EncryptedCommunityMaps',
                [], [],
                '''                Container class to hold clear/encrypted
                communitie maps
                ''',
                'encrypted_community_maps',
                'Cisco-IOS-XR-snmp-agent-cfg', False),
            _MetaInfoClassMember('views', REFERENCE_CLASS, 'Views', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg', 'Snmp.Views',
                [], [],
                '''                Class to configure a SNMPv2 MIB view
                ''',
                'views',
                'Cisco-IOS-XR-snmp-agent-cfg', False),
            _MetaInfoClassMember('logging', REFERENCE_CLASS, 'Logging', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg', 'Snmp.Logging',
                [], [],
                '''                SNMP logging
                ''',
                'logging',
                'Cisco-IOS-XR-snmp-agent-cfg', False),
            _MetaInfoClassMember('administration', REFERENCE_CLASS, 'Administration', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg', 'Snmp.Administration',
                [], [],
                '''                Container class for SNMP administration
                ''',
                'administration',
                'Cisco-IOS-XR-snmp-agent-cfg', False),
            _MetaInfoClassMember('agent', REFERENCE_CLASS, 'Agent', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg', 'Snmp.Agent',
                [], [],
                '''                The heirarchy point for SNMP Agent
                configurations
                ''',
                'agent',
                'Cisco-IOS-XR-snmp-agent-cfg', False),
            _MetaInfoClassMember('trap', REFERENCE_CLASS, 'Trap', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg', 'Snmp.Trap',
                [], [],
                '''                Class to hold trap configurations
                ''',
                'trap',
                'Cisco-IOS-XR-snmp-agent-cfg', False),
            _MetaInfoClassMember('drop-packet', REFERENCE_CLASS, 'DropPacket', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg', 'Snmp.DropPacket',
                [], [],
                '''                SNMP packet drop config
                ''',
                'drop_packet',
                'Cisco-IOS-XR-snmp-agent-cfg', False),
            _MetaInfoClassMember('ipv6', REFERENCE_CLASS, 'Ipv6', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg', 'Snmp.Ipv6',
                [], [],
                '''                SNMP TOS bit for outgoing packets
                ''',
                'ipv6',
                'Cisco-IOS-XR-snmp-agent-cfg', False),
            _MetaInfoClassMember('ipv4', REFERENCE_CLASS, 'Ipv4', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg', 'Snmp.Ipv4',
                [], [],
                '''                SNMP TOS bit for outgoing packets
                ''',
                'ipv4',
                'Cisco-IOS-XR-snmp-agent-cfg', False),
            _MetaInfoClassMember('system', REFERENCE_CLASS, 'System', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg', 'Snmp.System',
                [], [],
                '''                container to hold system information
                ''',
                'system',
                'Cisco-IOS-XR-snmp-agent-cfg', False),
            _MetaInfoClassMember('target', REFERENCE_CLASS, 'Target', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg', 'Snmp.Target',
                [], [],
                '''                SNMP target configurations
                ''',
                'target',
                'Cisco-IOS-XR-snmp-agent-cfg', False),
            _MetaInfoClassMember('notification', REFERENCE_CLASS, 'Notification', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg', 'Snmp.Notification',
                [], [],
                '''                Enable SNMP notifications
                ''',
                'notification',
                'Cisco-IOS-XR-snmp-agent-cfg', False),
            _MetaInfoClassMember('correlator', REFERENCE_CLASS, 'Correlator', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg', 'Snmp.Correlator',
                [], [],
                '''                Configure properties of the trap correlator
                ''',
                'correlator',
                'Cisco-IOS-XR-snmp-agent-cfg', False),
            _MetaInfoClassMember('bulk-stats', REFERENCE_CLASS, 'BulkStats', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg', 'Snmp.BulkStats',
                [], [],
                '''                SNMP bulk stats configuration commands
                ''',
                'bulk_stats',
                'Cisco-IOS-XR-snmp-agent-cfg', False),
            _MetaInfoClassMember('default-community-maps', REFERENCE_CLASS, 'DefaultCommunityMaps', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg', 'Snmp.DefaultCommunityMaps',
                [], [],
                '''                Container class to hold unencrpted community map
                ''',
                'default_community_maps',
                'Cisco-IOS-XR-snmp-agent-cfg', False),
            _MetaInfoClassMember('overload-control', REFERENCE_CLASS, 'OverloadControl', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg', 'Snmp.OverloadControl',
                [], [],
                '''                Set overload control params for handling
                incoming messages
                ''',
                'overload_control',
                'Cisco-IOS-XR-snmp-agent-cfg', False, is_presence=True),
            _MetaInfoClassMember('timeouts', REFERENCE_CLASS, 'Timeouts', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg', 'Snmp.Timeouts',
                [], [],
                '''                SNMP timeouts
                ''',
                'timeouts',
                'Cisco-IOS-XR-snmp-agent-cfg', False),
            _MetaInfoClassMember('users', REFERENCE_CLASS, 'Users', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg', 'Snmp.Users',
                [], [],
                '''                Define a user who can access the SNMP engine
                ''',
                'users',
                'Cisco-IOS-XR-snmp-agent-cfg', False),
            _MetaInfoClassMember('vrfs', REFERENCE_CLASS, 'Vrfs', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg', 'Snmp.Vrfs',
                [], [],
                '''                SNMP VRF configuration commands
                ''',
                'vrfs',
                'Cisco-IOS-XR-snmp-agent-cfg', False),
            _MetaInfoClassMember('groups', REFERENCE_CLASS, 'Groups', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg', 'Snmp.Groups',
                [], [],
                '''                Define a User Security Model group
                ''',
                'groups',
                'Cisco-IOS-XR-snmp-agent-cfg', False),
            _MetaInfoClassMember('inform-retries', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('0', '100')], [],
                '''                Number of times to retry an Inform request
                (default 3)
                ''',
                'inform_retries',
                'Cisco-IOS-XR-snmp-agent-cfg', False),
            _MetaInfoClassMember('trap-port', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('1024', '65535')], [],
                '''                Change the source port of all traps
                ''',
                'trap_port',
                'Cisco-IOS-XR-snmp-agent-cfg', False),
            _MetaInfoClassMember('oid-poll-stats', ATTRIBUTE, 'Empty', 'empty',
                None, None,
                [], [],
                '''                Enable Poll OID statistics
                ''',
                'oid_poll_stats',
                'Cisco-IOS-XR-snmp-agent-cfg', False),
            _MetaInfoClassMember('trap-source', ATTRIBUTE, 'str', 'xr:Interface-name',
                None, None,
                [], [b'[a-zA-Z0-9._/-]+'],
                '''                Assign an interface for the source address of
                all traps
                ''',
                'trap_source',
                'Cisco-IOS-XR-snmp-agent-cfg', False),
            _MetaInfoClassMember('vrf-authentication-trap-disable', ATTRIBUTE, 'Empty', 'empty',
                None, None,
                [], [],
                '''                Disable authentication traps for packets on a
                vrf
                ''',
                'vrf_authentication_trap_disable',
                'Cisco-IOS-XR-snmp-agent-cfg', False),
            _MetaInfoClassMember('inform-timeout', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('1', '42949671')], [],
                '''                Timeout value in seconds for Inform request
                (default 15 sec)
                ''',
                'inform_timeout',
                'Cisco-IOS-XR-snmp-agent-cfg', False),
            _MetaInfoClassMember('trap-source-ipv6', ATTRIBUTE, 'str', 'xr:Interface-name',
                None, None,
                [], [b'[a-zA-Z0-9._/-]+'],
                '''                Assign an interface for the source IPV6 address
                of all traps
                ''',
                'trap_source_ipv6',
                'Cisco-IOS-XR-snmp-agent-cfg', False),
            _MetaInfoClassMember('packet-size', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('484', '65500')], [],
                '''                Largest SNMP packet size
                ''',
                'packet_size',
                'Cisco-IOS-XR-snmp-agent-cfg', False),
            _MetaInfoClassMember('throttle-time', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('50', '1000')], [],
                '''                Throttle time for incoming queue (default 0
                msec)
                ''',
                'throttle_time',
                'Cisco-IOS-XR-snmp-agent-cfg', False),
            _MetaInfoClassMember('trap-source-ipv4', ATTRIBUTE, 'str', 'xr:Interface-name',
                None, None,
                [], [b'[a-zA-Z0-9._/-]+'],
                '''                Assign an interface for the source address of
                all traps
                ''',
                'trap_source_ipv4',
                'Cisco-IOS-XR-snmp-agent-cfg', False),
            _MetaInfoClassMember('inform-pending', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('0', '4294967295')], [],
                '''                Max nmber of informs to hold in queue, (default
                25)
                ''',
                'inform_pending',
                'Cisco-IOS-XR-snmp-agent-cfg', False),
            _MetaInfoClassMember('trap-hosts', REFERENCE_CLASS, 'TrapHosts', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg', 'Snmp.TrapHosts',
                [], [],
                '''                Specify hosts to receive SNMP notifications
                ''',
                'trap_hosts',
                'Cisco-IOS-XR-snmp-agent-cfg', False),
            _MetaInfoClassMember('contexts', REFERENCE_CLASS, 'Contexts', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg', 'Snmp.Contexts',
                [], [],
                '''                List of Context Names
                ''',
                'contexts',
                'Cisco-IOS-XR-snmp-agent-cfg', False),
            _MetaInfoClassMember('context-mappings', REFERENCE_CLASS, 'ContextMappings', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg', 'Snmp.ContextMappings',
                [], [],
                '''                List of context names
                ''',
                'context_mappings',
                'Cisco-IOS-XR-snmp-agent-cfg', False),
            ],
            'Cisco-IOS-XR-snmp-agent-cfg',
            'snmp',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-snmp-agent-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg',
        ),
    },
    'Mib.NotificationLogMib' : {
        'meta_info' : _MetaInfoClass('Mib.NotificationLogMib', REFERENCE_CLASS,
            '''Notification log MIB configuration''',
            False, 
            [
            _MetaInfoClassMember('global-age-out', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('1', '4294967295')], [],
                '''                GlobalAgeOut is the minutes associated with the
                mib
                ''',
                'global_age_out',
                'Cisco-IOS-XR-infra-notification-log-mib-cfg', False),
            _MetaInfoClassMember('disable', ATTRIBUTE, 'Empty', 'empty',
                None, None,
                [], [],
                '''                Disable, to disable the logging in default log
                ''',
                'disable',
                'Cisco-IOS-XR-infra-notification-log-mib-cfg', False),
            _MetaInfoClassMember('default', ATTRIBUTE, 'Empty', 'empty',
                None, None,
                [], [],
                '''                To create a default log
                ''',
                'default',
                'Cisco-IOS-XR-infra-notification-log-mib-cfg', False),
            _MetaInfoClassMember('global-size', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('1', '15000')], [],
                '''                GlobalSize, max number of notifications that
                can be logged in all logs
                ''',
                'global_size',
                'Cisco-IOS-XR-infra-notification-log-mib-cfg', False),
            _MetaInfoClassMember('default-size', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('1', '15000')], [],
                '''                The max number of notifications that this log
                (default) can hold
                ''',
                'default_size',
                'Cisco-IOS-XR-infra-notification-log-mib-cfg', False),
            ],
            'Cisco-IOS-XR-infra-notification-log-mib-cfg',
            'notification-log-mib',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-infra-notification-log-mib-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg',
        ),
    },
    'Mib.EntityMib' : {
        'meta_info' : _MetaInfoClass('Mib.EntityMib', REFERENCE_CLASS,
            '''Entity MIB''',
            False, 
            [
            _MetaInfoClassMember('entity-index-persistence', ATTRIBUTE, 'Empty', 'empty',
                None, None,
                [], [],
                '''                Enable entPhysicalIndex persistence
                ''',
                'entity_index_persistence',
                'Cisco-IOS-XR-snmp-entitymib-cfg', False),
            ],
            'Cisco-IOS-XR-snmp-entitymib-cfg',
            'entity-mib',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-snmp-entitymib-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg',
        ),
    },
    'Mib.InterfaceMib.Interfaces.Interface' : {
        'meta_info' : _MetaInfoClass('Mib.InterfaceMib.Interfaces.Interface', REFERENCE_LIST,
            '''Interface to configure''',
            False, 
            [
            _MetaInfoClassMember('interface-name', ATTRIBUTE, 'str', 'xr:Interface-name',
                None, None,
                [], [b'[a-zA-Z0-9._/-]+'],
                '''                The name of the interface
                ''',
                'interface_name',
                'Cisco-IOS-XR-snmp-ifmib-cfg', True),
            _MetaInfoClassMember('link-up-down', ATTRIBUTE, 'bool', 'boolean',
                None, None,
                [], [],
                '''                Enable or disable LinkUpDown notification
                ''',
                'link_up_down',
                'Cisco-IOS-XR-snmp-ifmib-cfg', False),
            _MetaInfoClassMember('index-persistence', ATTRIBUTE, 'bool', 'boolean',
                None, None,
                [], [],
                '''                Enable or disable index persistence
                ''',
                'index_persistence',
                'Cisco-IOS-XR-snmp-ifmib-cfg', False),
            ],
            'Cisco-IOS-XR-snmp-ifmib-cfg',
            'interface',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-snmp-ifmib-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg',
        ),
    },
    'Mib.InterfaceMib.Interfaces' : {
        'meta_info' : _MetaInfoClass('Mib.InterfaceMib.Interfaces', REFERENCE_CLASS,
            '''Enter the SNMP interface configuration commands''',
            False, 
            [
            _MetaInfoClassMember('interface', REFERENCE_LIST, 'Interface', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg', 'Mib.InterfaceMib.Interfaces.Interface',
                [], [],
                '''                Interface to configure
                ''',
                'interface',
                'Cisco-IOS-XR-snmp-ifmib-cfg', False),
            ],
            'Cisco-IOS-XR-snmp-ifmib-cfg',
            'interfaces',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-snmp-ifmib-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg',
        ),
    },
    'Mib.InterfaceMib.Notification' : {
        'meta_info' : _MetaInfoClass('Mib.InterfaceMib.Notification', REFERENCE_CLASS,
            '''MIB notification configuration''',
            False, 
            [
            _MetaInfoClassMember('link-ietf', ATTRIBUTE, 'Empty', 'empty',
                None, None,
                [], [],
                '''                Set the varbind of linkupdown trap to the RFC
                specified varbinds (default cisco)
                ''',
                'link_ietf',
                'Cisco-IOS-XR-snmp-ifmib-cfg', False),
            ],
            'Cisco-IOS-XR-snmp-ifmib-cfg',
            'notification',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-snmp-ifmib-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg',
        ),
    },
    'Mib.InterfaceMib.Subsets.Subset.LinkUpDown' : {
        'meta_info' : _MetaInfoClass('Mib.InterfaceMib.Subsets.Subset.LinkUpDown', REFERENCE_CLASS,
            '''SNMP linkUp and linkDown notifications''',
            False, 
            [
            _MetaInfoClassMember('enable', ATTRIBUTE, 'bool', 'boolean',
                None, None,
                [], [],
                '''                Enable or disable linkupdown notification
                ''',
                'enable',
                'Cisco-IOS-XR-snmp-ifmib-cfg', False),
            _MetaInfoClassMember('regular-expression', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                Regular expression to match ifName
                ''',
                'regular_expression',
                'Cisco-IOS-XR-snmp-ifmib-cfg', False),
            ],
            'Cisco-IOS-XR-snmp-ifmib-cfg',
            'link-up-down',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-snmp-ifmib-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg',
        ),
    },
    'Mib.InterfaceMib.Subsets.Subset' : {
        'meta_info' : _MetaInfoClass('Mib.InterfaceMib.Subsets.Subset', REFERENCE_LIST,
            '''Subset priorityID to group ifNames based on
Regular Expression''',
            False, 
            [
            _MetaInfoClassMember('subset-id', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('1', '255')], [],
                '''                The interface subset PriorityID
                ''',
                'subset_id',
                'Cisco-IOS-XR-snmp-ifmib-cfg', True),
            _MetaInfoClassMember('link-up-down', REFERENCE_CLASS, 'LinkUpDown', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg', 'Mib.InterfaceMib.Subsets.Subset.LinkUpDown',
                [], [],
                '''                SNMP linkUp and linkDown notifications
                ''',
                'link_up_down',
                'Cisco-IOS-XR-snmp-ifmib-cfg', False),
            ],
            'Cisco-IOS-XR-snmp-ifmib-cfg',
            'subset',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-snmp-ifmib-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg',
        ),
    },
    'Mib.InterfaceMib.Subsets' : {
        'meta_info' : _MetaInfoClass('Mib.InterfaceMib.Subsets', REFERENCE_CLASS,
            '''Add configuration for an interface subset''',
            False, 
            [
            _MetaInfoClassMember('subset', REFERENCE_LIST, 'Subset', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg', 'Mib.InterfaceMib.Subsets.Subset',
                [], [],
                '''                Subset priorityID to group ifNames based on
                Regular Expression
                ''',
                'subset',
                'Cisco-IOS-XR-snmp-ifmib-cfg', False),
            ],
            'Cisco-IOS-XR-snmp-ifmib-cfg',
            'subsets',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-snmp-ifmib-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg',
        ),
    },
    'Mib.InterfaceMib' : {
        'meta_info' : _MetaInfoClass('Mib.InterfaceMib', REFERENCE_CLASS,
            '''Interface MIB configuration''',
            False, 
            [
            _MetaInfoClassMember('interfaces', REFERENCE_CLASS, 'Interfaces', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg', 'Mib.InterfaceMib.Interfaces',
                [], [],
                '''                Enter the SNMP interface configuration commands
                ''',
                'interfaces',
                'Cisco-IOS-XR-snmp-ifmib-cfg', False),
            _MetaInfoClassMember('notification', REFERENCE_CLASS, 'Notification', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg', 'Mib.InterfaceMib.Notification',
                [], [],
                '''                MIB notification configuration
                ''',
                'notification',
                'Cisco-IOS-XR-snmp-ifmib-cfg', False),
            _MetaInfoClassMember('subsets', REFERENCE_CLASS, 'Subsets', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg', 'Mib.InterfaceMib.Subsets',
                [], [],
                '''                Add configuration for an interface subset
                ''',
                'subsets',
                'Cisco-IOS-XR-snmp-ifmib-cfg', False),
            _MetaInfoClassMember('internal-cache', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('0', '60')], [],
                '''                Get cached interface statistics
                ''',
                'internal_cache',
                'Cisco-IOS-XR-snmp-ifmib-cfg', False, default_value="15"),
            _MetaInfoClassMember('interface-alias-long', ATTRIBUTE, 'Empty', 'empty',
                None, None,
                [], [],
                '''                Enable support for ifAlias values longer than
                64 characters
                ''',
                'interface_alias_long',
                'Cisco-IOS-XR-snmp-ifmib-cfg', False),
            _MetaInfoClassMember('ip-subscriber', ATTRIBUTE, 'Empty', 'empty',
                None, None,
                [], [],
                '''                Enable IP subscriber interfaces in IFMIB
                ''',
                'ip_subscriber',
                'Cisco-IOS-XR-snmp-ifmib-cfg', False),
            _MetaInfoClassMember('interface-index-persistence', ATTRIBUTE, 'Empty', 'empty',
                None, None,
                [], [],
                '''                Enable ifindex persistence
                ''',
                'interface_index_persistence',
                'Cisco-IOS-XR-snmp-ifmib-cfg', False),
            _MetaInfoClassMember('statistics-cache', ATTRIBUTE, 'Empty', 'empty',
                None, None,
                [], [],
                '''                Enable cached interface statistics
                ''',
                'statistics_cache',
                'Cisco-IOS-XR-snmp-ifmib-cfg', False),
            ],
            'Cisco-IOS-XR-snmp-ifmib-cfg',
            'interface-mib',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-snmp-ifmib-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg',
        ),
    },
    'Mib.Subscriber.Threshold.Delta.Evaluation.AccessInterfaces.AccessInterface' : {
        'meta_info' : _MetaInfoClass('Mib.Subscriber.Threshold.Delta.Evaluation.AccessInterfaces.AccessInterface', REFERENCE_LIST,
            '''Access interface''',
            False, 
            [
            _MetaInfoClassMember('interface-name', ATTRIBUTE, 'str', 'xr:Interface-name',
                None, None,
                [], [b'[a-zA-Z0-9._/-]+'],
                '''                Interface name
                ''',
                'interface_name',
                'Cisco-IOS-XR-subscriber-session-mon-mibs-cfg', True),
            _MetaInfoClassMember('session-count', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('1', '4294967294')], [],
                '''                Session count
                ''',
                'session_count',
                'Cisco-IOS-XR-subscriber-session-mon-mibs-cfg', False),
            _MetaInfoClassMember('interval', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('30', '3600')], [],
                '''                Interval value in multiples of 10
                ''',
                'interval',
                'Cisco-IOS-XR-subscriber-session-mon-mibs-cfg', False),
            ],
            'Cisco-IOS-XR-subscriber-session-mon-mibs-cfg',
            'access-interface',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-subscriber-session-mon-mibs-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg',
        ),
    },
    'Mib.Subscriber.Threshold.Delta.Evaluation.AccessInterfaces' : {
        'meta_info' : _MetaInfoClass('Mib.Subscriber.Threshold.Delta.Evaluation.AccessInterfaces', REFERENCE_CLASS,
            '''Table of AccessInterface''',
            False, 
            [
            _MetaInfoClassMember('access-interface', REFERENCE_LIST, 'AccessInterface', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg', 'Mib.Subscriber.Threshold.Delta.Evaluation.AccessInterfaces.AccessInterface',
                [], [],
                '''                Access interface
                ''',
                'access_interface',
                'Cisco-IOS-XR-subscriber-session-mon-mibs-cfg', False),
            ],
            'Cisco-IOS-XR-subscriber-session-mon-mibs-cfg',
            'access-interfaces',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-subscriber-session-mon-mibs-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg',
        ),
    },
    'Mib.Subscriber.Threshold.Delta.Evaluation.Nodes.Node' : {
        'meta_info' : _MetaInfoClass('Mib.Subscriber.Threshold.Delta.Evaluation.Nodes.Node', REFERENCE_LIST,
            '''Rising node level''',
            False, 
            [
            _MetaInfoClassMember('node-name', ATTRIBUTE, 'str', 'xr:Node-id',
                None, None,
                [], [b'([a-zA-Z0-9_]*\\d+/){1,2}([a-zA-Z0-9_]*\\d+)'],
                '''                location
                ''',
                'node_name',
                'Cisco-IOS-XR-subscriber-session-mon-mibs-cfg', True),
            _MetaInfoClassMember('session-count', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('1', '4294967294')], [],
                '''                Session count
                ''',
                'session_count',
                'Cisco-IOS-XR-subscriber-session-mon-mibs-cfg', False),
            _MetaInfoClassMember('interval', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('30', '3600')], [],
                '''                interval value in multiples of 10
                ''',
                'interval',
                'Cisco-IOS-XR-subscriber-session-mon-mibs-cfg', False),
            ],
            'Cisco-IOS-XR-subscriber-session-mon-mibs-cfg',
            'node',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-subscriber-session-mon-mibs-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg',
        ),
    },
    'Mib.Subscriber.Threshold.Delta.Evaluation.Nodes' : {
        'meta_info' : _MetaInfoClass('Mib.Subscriber.Threshold.Delta.Evaluation.Nodes', REFERENCE_CLASS,
            '''Table of Node''',
            False, 
            [
            _MetaInfoClassMember('node', REFERENCE_LIST, 'Node', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg', 'Mib.Subscriber.Threshold.Delta.Evaluation.Nodes.Node',
                [], [],
                '''                Rising node level
                ''',
                'node',
                'Cisco-IOS-XR-subscriber-session-mon-mibs-cfg', False),
            ],
            'Cisco-IOS-XR-subscriber-session-mon-mibs-cfg',
            'nodes',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-subscriber-session-mon-mibs-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg',
        ),
    },
    'Mib.Subscriber.Threshold.Delta.Evaluation' : {
        'meta_info' : _MetaInfoClass('Mib.Subscriber.Threshold.Delta.Evaluation', REFERENCE_CLASS,
            '''Evaluation keyword''',
            False, 
            [
            _MetaInfoClassMember('access-interfaces', REFERENCE_CLASS, 'AccessInterfaces', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg', 'Mib.Subscriber.Threshold.Delta.Evaluation.AccessInterfaces',
                [], [],
                '''                Table of AccessInterface
                ''',
                'access_interfaces',
                'Cisco-IOS-XR-subscriber-session-mon-mibs-cfg', False),
            _MetaInfoClassMember('nodes', REFERENCE_CLASS, 'Nodes', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg', 'Mib.Subscriber.Threshold.Delta.Evaluation.Nodes',
                [], [],
                '''                Table of Node
                ''',
                'nodes',
                'Cisco-IOS-XR-subscriber-session-mon-mibs-cfg', False),
            ],
            'Cisco-IOS-XR-subscriber-session-mon-mibs-cfg',
            'evaluation',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-subscriber-session-mon-mibs-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg',
        ),
    },
    'Mib.Subscriber.Threshold.Delta.Percent.AccessInterfaces.AccessInterface' : {
        'meta_info' : _MetaInfoClass('Mib.Subscriber.Threshold.Delta.Percent.AccessInterfaces.AccessInterface', REFERENCE_LIST,
            '''Access interface''',
            False, 
            [
            _MetaInfoClassMember('interface-name', ATTRIBUTE, 'str', 'xr:Interface-name',
                None, None,
                [], [b'[a-zA-Z0-9._/-]+'],
                '''                Interface name
                ''',
                'interface_name',
                'Cisco-IOS-XR-subscriber-session-mon-mibs-cfg', True),
            _MetaInfoClassMember('session-count', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('1', '4294967294')], [],
                '''                Session count
                ''',
                'session_count',
                'Cisco-IOS-XR-subscriber-session-mon-mibs-cfg', False),
            _MetaInfoClassMember('interval', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('30', '3600')], [],
                '''                Interval value in multiples of 10
                ''',
                'interval',
                'Cisco-IOS-XR-subscriber-session-mon-mibs-cfg', False),
            ],
            'Cisco-IOS-XR-subscriber-session-mon-mibs-cfg',
            'access-interface',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-subscriber-session-mon-mibs-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg',
        ),
    },
    'Mib.Subscriber.Threshold.Delta.Percent.AccessInterfaces' : {
        'meta_info' : _MetaInfoClass('Mib.Subscriber.Threshold.Delta.Percent.AccessInterfaces', REFERENCE_CLASS,
            '''Table of AccessInterface''',
            False, 
            [
            _MetaInfoClassMember('access-interface', REFERENCE_LIST, 'AccessInterface', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg', 'Mib.Subscriber.Threshold.Delta.Percent.AccessInterfaces.AccessInterface',
                [], [],
                '''                Access interface
                ''',
                'access_interface',
                'Cisco-IOS-XR-subscriber-session-mon-mibs-cfg', False),
            ],
            'Cisco-IOS-XR-subscriber-session-mon-mibs-cfg',
            'access-interfaces',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-subscriber-session-mon-mibs-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg',
        ),
    },
    'Mib.Subscriber.Threshold.Delta.Percent.Nodes.Node' : {
        'meta_info' : _MetaInfoClass('Mib.Subscriber.Threshold.Delta.Percent.Nodes.Node', REFERENCE_LIST,
            '''Rising node level''',
            False, 
            [
            _MetaInfoClassMember('node-name', ATTRIBUTE, 'str', 'xr:Node-id',
                None, None,
                [], [b'([a-zA-Z0-9_]*\\d+/){1,2}([a-zA-Z0-9_]*\\d+)'],
                '''                location
                ''',
                'node_name',
                'Cisco-IOS-XR-subscriber-session-mon-mibs-cfg', True),
            _MetaInfoClassMember('session-count', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('1', '4294967294')], [],
                '''                Session count
                ''',
                'session_count',
                'Cisco-IOS-XR-subscriber-session-mon-mibs-cfg', False),
            _MetaInfoClassMember('interval', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('30', '3600')], [],
                '''                interval value in multiples of 10
                ''',
                'interval',
                'Cisco-IOS-XR-subscriber-session-mon-mibs-cfg', False),
            ],
            'Cisco-IOS-XR-subscriber-session-mon-mibs-cfg',
            'node',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-subscriber-session-mon-mibs-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg',
        ),
    },
    'Mib.Subscriber.Threshold.Delta.Percent.Nodes' : {
        'meta_info' : _MetaInfoClass('Mib.Subscriber.Threshold.Delta.Percent.Nodes', REFERENCE_CLASS,
            '''Table of Node''',
            False, 
            [
            _MetaInfoClassMember('node', REFERENCE_LIST, 'Node', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg', 'Mib.Subscriber.Threshold.Delta.Percent.Nodes.Node',
                [], [],
                '''                Rising node level
                ''',
                'node',
                'Cisco-IOS-XR-subscriber-session-mon-mibs-cfg', False),
            ],
            'Cisco-IOS-XR-subscriber-session-mon-mibs-cfg',
            'nodes',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-subscriber-session-mon-mibs-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg',
        ),
    },
    'Mib.Subscriber.Threshold.Delta.Percent' : {
        'meta_info' : _MetaInfoClass('Mib.Subscriber.Threshold.Delta.Percent', REFERENCE_CLASS,
            '''Delta loss percent''',
            False, 
            [
            _MetaInfoClassMember('access-interfaces', REFERENCE_CLASS, 'AccessInterfaces', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg', 'Mib.Subscriber.Threshold.Delta.Percent.AccessInterfaces',
                [], [],
                '''                Table of AccessInterface
                ''',
                'access_interfaces',
                'Cisco-IOS-XR-subscriber-session-mon-mibs-cfg', False),
            _MetaInfoClassMember('nodes', REFERENCE_CLASS, 'Nodes', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg', 'Mib.Subscriber.Threshold.Delta.Percent.Nodes',
                [], [],
                '''                Table of Node
                ''',
                'nodes',
                'Cisco-IOS-XR-subscriber-session-mon-mibs-cfg', False),
            ],
            'Cisco-IOS-XR-subscriber-session-mon-mibs-cfg',
            'percent',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-subscriber-session-mon-mibs-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg',
        ),
    },
    'Mib.Subscriber.Threshold.Delta' : {
        'meta_info' : _MetaInfoClass('Mib.Subscriber.Threshold.Delta', REFERENCE_CLASS,
            '''Delta loss keyword''',
            False, 
            [
            _MetaInfoClassMember('evaluation', REFERENCE_CLASS, 'Evaluation', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg', 'Mib.Subscriber.Threshold.Delta.Evaluation',
                [], [],
                '''                Evaluation keyword
                ''',
                'evaluation',
                'Cisco-IOS-XR-subscriber-session-mon-mibs-cfg', False),
            _MetaInfoClassMember('percent', REFERENCE_CLASS, 'Percent', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg', 'Mib.Subscriber.Threshold.Delta.Percent',
                [], [],
                '''                Delta loss percent
                ''',
                'percent',
                'Cisco-IOS-XR-subscriber-session-mon-mibs-cfg', False),
            ],
            'Cisco-IOS-XR-subscriber-session-mon-mibs-cfg',
            'delta',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-subscriber-session-mon-mibs-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg',
        ),
    },
    'Mib.Subscriber.Threshold.AccessInterfaceSub.Subsets.Subset.RegularExpression.Notification.RisingFalling' : {
        'meta_info' : _MetaInfoClass('Mib.Subscriber.Threshold.AccessInterfaceSub.Subsets.Subset.RegularExpression.Notification.RisingFalling', REFERENCE_CLASS,
            '''Rising-falling threshold''',
            False, 
            [
            _MetaInfoClassMember('disable', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                Disable the notifications on access
                interfaces
                ''',
                'disable',
                'Cisco-IOS-XR-subscriber-session-mon-mibs-cfg', False),
            ],
            'Cisco-IOS-XR-subscriber-session-mon-mibs-cfg',
            'rising-falling',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-subscriber-session-mon-mibs-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg',
        ),
    },
    'Mib.Subscriber.Threshold.AccessInterfaceSub.Subsets.Subset.RegularExpression.Notification' : {
        'meta_info' : _MetaInfoClass('Mib.Subscriber.Threshold.AccessInterfaceSub.Subsets.Subset.RegularExpression.Notification', REFERENCE_CLASS,
            '''Notification keyword''',
            False, 
            [
            _MetaInfoClassMember('rising-falling', REFERENCE_CLASS, 'RisingFalling', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg', 'Mib.Subscriber.Threshold.AccessInterfaceSub.Subsets.Subset.RegularExpression.Notification.RisingFalling',
                [], [],
                '''                Rising-falling threshold
                ''',
                'rising_falling',
                'Cisco-IOS-XR-subscriber-session-mon-mibs-cfg', False),
            ],
            'Cisco-IOS-XR-subscriber-session-mon-mibs-cfg',
            'notification',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-subscriber-session-mon-mibs-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg',
        ),
    },
    'Mib.Subscriber.Threshold.AccessInterfaceSub.Subsets.Subset.RegularExpression' : {
        'meta_info' : _MetaInfoClass('Mib.Subscriber.Threshold.AccessInterfaceSub.Subsets.Subset.RegularExpression', REFERENCE_CLASS,
            '''Regular expression''',
            False, 
            [
            _MetaInfoClassMember('notification', REFERENCE_CLASS, 'Notification', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg', 'Mib.Subscriber.Threshold.AccessInterfaceSub.Subsets.Subset.RegularExpression.Notification',
                [], [],
                '''                Notification keyword
                ''',
                'notification',
                'Cisco-IOS-XR-subscriber-session-mon-mibs-cfg', False),
            ],
            'Cisco-IOS-XR-subscriber-session-mon-mibs-cfg',
            'regular-expression',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-subscriber-session-mon-mibs-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg',
        ),
    },
    'Mib.Subscriber.Threshold.AccessInterfaceSub.Subsets.Subset' : {
        'meta_info' : _MetaInfoClass('Mib.Subscriber.Threshold.AccessInterfaceSub.Subsets.Subset', REFERENCE_LIST,
            '''Subset command''',
            False, 
            [
            _MetaInfoClassMember('subset-id', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('1', '255')], [],
                '''                Subset number
                ''',
                'subset_id',
                'Cisco-IOS-XR-subscriber-session-mon-mibs-cfg', True),
            _MetaInfoClassMember('regular-expression', REFERENCE_CLASS, 'RegularExpression', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg', 'Mib.Subscriber.Threshold.AccessInterfaceSub.Subsets.Subset.RegularExpression',
                [], [],
                '''                Regular expression
                ''',
                'regular_expression',
                'Cisco-IOS-XR-subscriber-session-mon-mibs-cfg', False),
            ],
            'Cisco-IOS-XR-subscriber-session-mon-mibs-cfg',
            'subset',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-subscriber-session-mon-mibs-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg',
        ),
    },
    'Mib.Subscriber.Threshold.AccessInterfaceSub.Subsets' : {
        'meta_info' : _MetaInfoClass('Mib.Subscriber.Threshold.AccessInterfaceSub.Subsets', REFERENCE_CLASS,
            '''Table of Subset''',
            False, 
            [
            _MetaInfoClassMember('subset', REFERENCE_LIST, 'Subset', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg', 'Mib.Subscriber.Threshold.AccessInterfaceSub.Subsets.Subset',
                [], [],
                '''                Subset command
                ''',
                'subset',
                'Cisco-IOS-XR-subscriber-session-mon-mibs-cfg', False),
            ],
            'Cisco-IOS-XR-subscriber-session-mon-mibs-cfg',
            'subsets',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-subscriber-session-mon-mibs-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg',
        ),
    },
    'Mib.Subscriber.Threshold.AccessInterfaceSub' : {
        'meta_info' : _MetaInfoClass('Mib.Subscriber.Threshold.AccessInterfaceSub', REFERENCE_CLASS,
            '''Access interface for regular expression''',
            False, 
            [
            _MetaInfoClassMember('subsets', REFERENCE_CLASS, 'Subsets', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg', 'Mib.Subscriber.Threshold.AccessInterfaceSub.Subsets',
                [], [],
                '''                Table of Subset
                ''',
                'subsets',
                'Cisco-IOS-XR-subscriber-session-mon-mibs-cfg', False),
            ],
            'Cisco-IOS-XR-subscriber-session-mon-mibs-cfg',
            'access-interface-sub',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-subscriber-session-mon-mibs-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg',
        ),
    },
    'Mib.Subscriber.Threshold.Falling.AccessInterfaces.AccessInterface' : {
        'meta_info' : _MetaInfoClass('Mib.Subscriber.Threshold.Falling.AccessInterfaces.AccessInterface', REFERENCE_LIST,
            '''Access interface''',
            False, 
            [
            _MetaInfoClassMember('interface-name', ATTRIBUTE, 'str', 'xr:Interface-name',
                None, None,
                [], [b'[a-zA-Z0-9._/-]+'],
                '''                Interface name
                ''',
                'interface_name',
                'Cisco-IOS-XR-subscriber-session-mon-mibs-cfg', True),
            _MetaInfoClassMember('session-count', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('1', '4294967294')], [],
                '''                Session count
                ''',
                'session_count',
                'Cisco-IOS-XR-subscriber-session-mon-mibs-cfg', False),
            _MetaInfoClassMember('interval', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('30', '3600')], [],
                '''                Interval value in multiples of 10
                ''',
                'interval',
                'Cisco-IOS-XR-subscriber-session-mon-mibs-cfg', False),
            ],
            'Cisco-IOS-XR-subscriber-session-mon-mibs-cfg',
            'access-interface',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-subscriber-session-mon-mibs-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg',
        ),
    },
    'Mib.Subscriber.Threshold.Falling.AccessInterfaces' : {
        'meta_info' : _MetaInfoClass('Mib.Subscriber.Threshold.Falling.AccessInterfaces', REFERENCE_CLASS,
            '''Table of AccessInterface''',
            False, 
            [
            _MetaInfoClassMember('access-interface', REFERENCE_LIST, 'AccessInterface', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg', 'Mib.Subscriber.Threshold.Falling.AccessInterfaces.AccessInterface',
                [], [],
                '''                Access interface
                ''',
                'access_interface',
                'Cisco-IOS-XR-subscriber-session-mon-mibs-cfg', False),
            ],
            'Cisco-IOS-XR-subscriber-session-mon-mibs-cfg',
            'access-interfaces',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-subscriber-session-mon-mibs-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg',
        ),
    },
    'Mib.Subscriber.Threshold.Falling.Nodes.Node' : {
        'meta_info' : _MetaInfoClass('Mib.Subscriber.Threshold.Falling.Nodes.Node', REFERENCE_LIST,
            '''Rising node level''',
            False, 
            [
            _MetaInfoClassMember('node-name', ATTRIBUTE, 'str', 'xr:Node-id',
                None, None,
                [], [b'([a-zA-Z0-9_]*\\d+/){1,2}([a-zA-Z0-9_]*\\d+)'],
                '''                location
                ''',
                'node_name',
                'Cisco-IOS-XR-subscriber-session-mon-mibs-cfg', True),
            _MetaInfoClassMember('session-count', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('1', '4294967294')], [],
                '''                Session count
                ''',
                'session_count',
                'Cisco-IOS-XR-subscriber-session-mon-mibs-cfg', False),
            _MetaInfoClassMember('interval', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('30', '3600')], [],
                '''                interval value in multiples of 10
                ''',
                'interval',
                'Cisco-IOS-XR-subscriber-session-mon-mibs-cfg', False),
            ],
            'Cisco-IOS-XR-subscriber-session-mon-mibs-cfg',
            'node',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-subscriber-session-mon-mibs-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg',
        ),
    },
    'Mib.Subscriber.Threshold.Falling.Nodes' : {
        'meta_info' : _MetaInfoClass('Mib.Subscriber.Threshold.Falling.Nodes', REFERENCE_CLASS,
            '''Table of Node''',
            False, 
            [
            _MetaInfoClassMember('node', REFERENCE_LIST, 'Node', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg', 'Mib.Subscriber.Threshold.Falling.Nodes.Node',
                [], [],
                '''                Rising node level
                ''',
                'node',
                'Cisco-IOS-XR-subscriber-session-mon-mibs-cfg', False),
            ],
            'Cisco-IOS-XR-subscriber-session-mon-mibs-cfg',
            'nodes',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-subscriber-session-mon-mibs-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg',
        ),
    },
    'Mib.Subscriber.Threshold.Falling' : {
        'meta_info' : _MetaInfoClass('Mib.Subscriber.Threshold.Falling', REFERENCE_CLASS,
            '''Falling threshold''',
            False, 
            [
            _MetaInfoClassMember('access-interfaces', REFERENCE_CLASS, 'AccessInterfaces', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg', 'Mib.Subscriber.Threshold.Falling.AccessInterfaces',
                [], [],
                '''                Table of AccessInterface
                ''',
                'access_interfaces',
                'Cisco-IOS-XR-subscriber-session-mon-mibs-cfg', False),
            _MetaInfoClassMember('nodes', REFERENCE_CLASS, 'Nodes', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg', 'Mib.Subscriber.Threshold.Falling.Nodes',
                [], [],
                '''                Table of Node
                ''',
                'nodes',
                'Cisco-IOS-XR-subscriber-session-mon-mibs-cfg', False),
            ],
            'Cisco-IOS-XR-subscriber-session-mon-mibs-cfg',
            'falling',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-subscriber-session-mon-mibs-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg',
        ),
    },
    'Mib.Subscriber.Threshold.Rising.AccessInterfaces.AccessInterface' : {
        'meta_info' : _MetaInfoClass('Mib.Subscriber.Threshold.Rising.AccessInterfaces.AccessInterface', REFERENCE_LIST,
            '''Access interface''',
            False, 
            [
            _MetaInfoClassMember('interface-name', ATTRIBUTE, 'str', 'xr:Interface-name',
                None, None,
                [], [b'[a-zA-Z0-9._/-]+'],
                '''                Interface name
                ''',
                'interface_name',
                'Cisco-IOS-XR-subscriber-session-mon-mibs-cfg', True),
            _MetaInfoClassMember('session-count', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('1', '4294967294')], [],
                '''                Session count
                ''',
                'session_count',
                'Cisco-IOS-XR-subscriber-session-mon-mibs-cfg', False),
            _MetaInfoClassMember('interval', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('30', '3600')], [],
                '''                Interval value in multiples of 10
                ''',
                'interval',
                'Cisco-IOS-XR-subscriber-session-mon-mibs-cfg', False),
            ],
            'Cisco-IOS-XR-subscriber-session-mon-mibs-cfg',
            'access-interface',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-subscriber-session-mon-mibs-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg',
        ),
    },
    'Mib.Subscriber.Threshold.Rising.AccessInterfaces' : {
        'meta_info' : _MetaInfoClass('Mib.Subscriber.Threshold.Rising.AccessInterfaces', REFERENCE_CLASS,
            '''Table of AccessInterface''',
            False, 
            [
            _MetaInfoClassMember('access-interface', REFERENCE_LIST, 'AccessInterface', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg', 'Mib.Subscriber.Threshold.Rising.AccessInterfaces.AccessInterface',
                [], [],
                '''                Access interface
                ''',
                'access_interface',
                'Cisco-IOS-XR-subscriber-session-mon-mibs-cfg', False),
            ],
            'Cisco-IOS-XR-subscriber-session-mon-mibs-cfg',
            'access-interfaces',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-subscriber-session-mon-mibs-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg',
        ),
    },
    'Mib.Subscriber.Threshold.Rising.Nodes.Node' : {
        'meta_info' : _MetaInfoClass('Mib.Subscriber.Threshold.Rising.Nodes.Node', REFERENCE_LIST,
            '''Rising node level''',
            False, 
            [
            _MetaInfoClassMember('node-name', ATTRIBUTE, 'str', 'xr:Node-id',
                None, None,
                [], [b'([a-zA-Z0-9_]*\\d+/){1,2}([a-zA-Z0-9_]*\\d+)'],
                '''                location
                ''',
                'node_name',
                'Cisco-IOS-XR-subscriber-session-mon-mibs-cfg', True),
            _MetaInfoClassMember('session-count', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('1', '4294967294')], [],
                '''                Session count
                ''',
                'session_count',
                'Cisco-IOS-XR-subscriber-session-mon-mibs-cfg', False),
            _MetaInfoClassMember('interval', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('30', '3600')], [],
                '''                interval value in multiples of 10
                ''',
                'interval',
                'Cisco-IOS-XR-subscriber-session-mon-mibs-cfg', False),
            ],
            'Cisco-IOS-XR-subscriber-session-mon-mibs-cfg',
            'node',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-subscriber-session-mon-mibs-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg',
        ),
    },
    'Mib.Subscriber.Threshold.Rising.Nodes' : {
        'meta_info' : _MetaInfoClass('Mib.Subscriber.Threshold.Rising.Nodes', REFERENCE_CLASS,
            '''Table of Node''',
            False, 
            [
            _MetaInfoClassMember('node', REFERENCE_LIST, 'Node', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg', 'Mib.Subscriber.Threshold.Rising.Nodes.Node',
                [], [],
                '''                Rising node level
                ''',
                'node',
                'Cisco-IOS-XR-subscriber-session-mon-mibs-cfg', False),
            ],
            'Cisco-IOS-XR-subscriber-session-mon-mibs-cfg',
            'nodes',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-subscriber-session-mon-mibs-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg',
        ),
    },
    'Mib.Subscriber.Threshold.Rising' : {
        'meta_info' : _MetaInfoClass('Mib.Subscriber.Threshold.Rising', REFERENCE_CLASS,
            '''Rising threshold''',
            False, 
            [
            _MetaInfoClassMember('access-interfaces', REFERENCE_CLASS, 'AccessInterfaces', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg', 'Mib.Subscriber.Threshold.Rising.AccessInterfaces',
                [], [],
                '''                Table of AccessInterface
                ''',
                'access_interfaces',
                'Cisco-IOS-XR-subscriber-session-mon-mibs-cfg', False),
            _MetaInfoClassMember('nodes', REFERENCE_CLASS, 'Nodes', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg', 'Mib.Subscriber.Threshold.Rising.Nodes',
                [], [],
                '''                Table of Node
                ''',
                'nodes',
                'Cisco-IOS-XR-subscriber-session-mon-mibs-cfg', False),
            ],
            'Cisco-IOS-XR-subscriber-session-mon-mibs-cfg',
            'rising',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-subscriber-session-mon-mibs-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg',
        ),
    },
    'Mib.Subscriber.Threshold' : {
        'meta_info' : _MetaInfoClass('Mib.Subscriber.Threshold', REFERENCE_CLASS,
            '''Subscriber threshold commands''',
            False, 
            [
            _MetaInfoClassMember('delta', REFERENCE_CLASS, 'Delta', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg', 'Mib.Subscriber.Threshold.Delta',
                [], [],
                '''                Delta loss keyword
                ''',
                'delta',
                'Cisco-IOS-XR-subscriber-session-mon-mibs-cfg', False),
            _MetaInfoClassMember('access-interface-sub', REFERENCE_CLASS, 'AccessInterfaceSub', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg', 'Mib.Subscriber.Threshold.AccessInterfaceSub',
                [], [],
                '''                Access interface for regular expression
                ''',
                'access_interface_sub',
                'Cisco-IOS-XR-subscriber-session-mon-mibs-cfg', False),
            _MetaInfoClassMember('falling', REFERENCE_CLASS, 'Falling', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg', 'Mib.Subscriber.Threshold.Falling',
                [], [],
                '''                Falling threshold
                ''',
                'falling',
                'Cisco-IOS-XR-subscriber-session-mon-mibs-cfg', False),
            _MetaInfoClassMember('rising', REFERENCE_CLASS, 'Rising', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg', 'Mib.Subscriber.Threshold.Rising',
                [], [],
                '''                Rising threshold
                ''',
                'rising',
                'Cisco-IOS-XR-subscriber-session-mon-mibs-cfg', False),
            ],
            'Cisco-IOS-XR-subscriber-session-mon-mibs-cfg',
            'threshold',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-subscriber-session-mon-mibs-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg',
        ),
    },
    'Mib.Subscriber' : {
        'meta_info' : _MetaInfoClass('Mib.Subscriber', REFERENCE_CLASS,
            '''Subscriber threshold commands''',
            False, 
            [
            _MetaInfoClassMember('threshold', REFERENCE_CLASS, 'Threshold', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg', 'Mib.Subscriber.Threshold',
                [], [],
                '''                Subscriber threshold commands
                ''',
                'threshold',
                'Cisco-IOS-XR-subscriber-session-mon-mibs-cfg', False),
            ],
            'Cisco-IOS-XR-subscriber-session-mon-mibs-cfg',
            'subscriber',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-subscriber-session-mon-mibs-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg',
        ),
    },
    'Mib.CbQosmib.Cache' : {
        'meta_info' : _MetaInfoClass('Mib.CbQosmib.Cache', REFERENCE_CLASS,
            '''CBQoSMIB statistics data caching''',
            False, 
            [
            _MetaInfoClassMember('enable', ATTRIBUTE, 'Empty', 'empty',
                None, None,
                [], [],
                '''                Enable CBQoSMIB statistics data caching
                ''',
                'enable',
                'Cisco-IOS-XR-qos-mibs-cfg', False),
            _MetaInfoClassMember('refresh-time', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('5', '60')], [],
                '''                Cache refresh time in seconds
                ''',
                'refresh_time',
                'Cisco-IOS-XR-qos-mibs-cfg', False),
            _MetaInfoClassMember('service-policy-count', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('1', '5000')], [],
                '''                Maximum number of service policies to cache
                the statistics for
                ''',
                'service_policy_count',
                'Cisco-IOS-XR-qos-mibs-cfg', False),
            ],
            'Cisco-IOS-XR-qos-mibs-cfg',
            'cache',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-qos-mibs-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg',
        ),
    },
    'Mib.CbQosmib' : {
        'meta_info' : _MetaInfoClass('Mib.CbQosmib', REFERENCE_CLASS,
            '''CBQoSMIB configuration''',
            False, 
            [
            _MetaInfoClassMember('cache', REFERENCE_CLASS, 'Cache', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg', 'Mib.CbQosmib.Cache',
                [], [],
                '''                CBQoSMIB statistics data caching
                ''',
                'cache',
                'Cisco-IOS-XR-qos-mibs-cfg', False),
            _MetaInfoClassMember('member-interface-stats', ATTRIBUTE, 'Empty', 'empty',
                None, None,
                [], [],
                '''                Enable bundle member interface statistics
                retrieval.
                ''',
                'member_interface_stats',
                'Cisco-IOS-XR-qos-mibs-cfg', False),
            _MetaInfoClassMember('persist', ATTRIBUTE, 'Empty', 'empty',
                None, None,
                [], [],
                '''                Persist CBQoSMIB config, service-policy and
                object indices
                ''',
                'persist',
                'Cisco-IOS-XR-qos-mibs-cfg', False),
            ],
            'Cisco-IOS-XR-qos-mibs-cfg',
            'cb-qosmib',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-qos-mibs-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg',
        ),
    },
    'Mib.MplsTeMib' : {
        'meta_info' : _MetaInfoClass('Mib.MplsTeMib', REFERENCE_CLASS,
            '''MPLS TE MIB configuration''',
            False, 
            [
            _MetaInfoClassMember('cache-garbage-collect-timer', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('0', '3600')], [],
                '''                Configure the cache garbage collector time for
                the mib.
                ''',
                'cache_garbage_collect_timer',
                'Cisco-IOS-XR-mpls-te-cfg', False, default_value="1800"),
            _MetaInfoClassMember('cache-timer', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('0', '600')], [],
                '''                Configure the cache time for the mib.
                ''',
                'cache_timer',
                'Cisco-IOS-XR-mpls-te-cfg', False, default_value="60"),
            ],
            'Cisco-IOS-XR-mpls-te-cfg',
            'mpls-te-mib',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-mpls-te-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg',
        ),
    },
    'Mib.MplsP2mpMib' : {
        'meta_info' : _MetaInfoClass('Mib.MplsP2mpMib', REFERENCE_CLASS,
            '''MPLS P2MP MIB configuration''',
            False, 
            [
            _MetaInfoClassMember('cache-timer', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('0', '600')], [],
                '''                Configure the cache time for the mib.
                ''',
                'cache_timer',
                'Cisco-IOS-XR-mpls-te-cfg', False, default_value="60"),
            ],
            'Cisco-IOS-XR-mpls-te-cfg',
            'mpls-p2mp-mib',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-mpls-te-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg',
        ),
    },
    'Mib.MplsTeExtStdMib' : {
        'meta_info' : _MetaInfoClass('Mib.MplsTeExtStdMib', REFERENCE_CLASS,
            '''MPLS TE EXT STD MIB configuration''',
            False, 
            [
            _MetaInfoClassMember('cache-timer', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('0', '600')], [],
                '''                Configure the cache time for the mib.
                ''',
                'cache_timer',
                'Cisco-IOS-XR-mpls-te-cfg', False, default_value="60"),
            ],
            'Cisco-IOS-XR-mpls-te-cfg',
            'mpls-te-ext-std-mib',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-mpls-te-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg',
        ),
    },
    'Mib.MplsTeExtMib' : {
        'meta_info' : _MetaInfoClass('Mib.MplsTeExtMib', REFERENCE_CLASS,
            '''MPLS TE EXT MIB configuration''',
            False, 
            [
            _MetaInfoClassMember('cache-timer', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('0', '600')], [],
                '''                Configure the cache time for the mib.
                ''',
                'cache_timer',
                'Cisco-IOS-XR-mpls-te-cfg', False, default_value="60"),
            ],
            'Cisco-IOS-XR-mpls-te-cfg',
            'mpls-te-ext-mib',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-mpls-te-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg',
        ),
    },
    'Mib.MplsFrrMib' : {
        'meta_info' : _MetaInfoClass('Mib.MplsFrrMib', REFERENCE_CLASS,
            '''FRR MIB configuration''',
            False, 
            [
            _MetaInfoClassMember('cache-timer', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('0', '600')], [],
                '''                Configure the cache time for the mib.
                ''',
                'cache_timer',
                'Cisco-IOS-XR-mpls-te-cfg', False, default_value="60"),
            ],
            'Cisco-IOS-XR-mpls-te-cfg',
            'mpls-frr-mib',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-mpls-te-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg',
        ),
    },
    'Mib' : {
        'meta_info' : _MetaInfoClass('Mib', REFERENCE_CLASS,
            '''mib''',
            False, 
            [
            _MetaInfoClassMember('notification-log-mib', REFERENCE_CLASS, 'NotificationLogMib', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg', 'Mib.NotificationLogMib',
                [], [],
                '''                Notification log MIB configuration
                ''',
                'notification_log_mib',
                'Cisco-IOS-XR-infra-notification-log-mib-cfg', False),
            _MetaInfoClassMember('entity-mib', REFERENCE_CLASS, 'EntityMib', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg', 'Mib.EntityMib',
                [], [],
                '''                Entity MIB
                ''',
                'entity_mib',
                'Cisco-IOS-XR-snmp-entitymib-cfg', False),
            _MetaInfoClassMember('interface-mib', REFERENCE_CLASS, 'InterfaceMib', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg', 'Mib.InterfaceMib',
                [], [],
                '''                Interface MIB configuration
                ''',
                'interface_mib',
                'Cisco-IOS-XR-snmp-ifmib-cfg', False),
            _MetaInfoClassMember('sensor-mib-cache', ATTRIBUTE, 'Empty', 'empty',
                None, None,
                [], [],
                '''                Get cached Sesnsor MIB statistics
                ''',
                'sensor_mib_cache',
                'Cisco-IOS-XR-snmp-ciscosensormib-cfg', False),
            _MetaInfoClassMember('subscriber', REFERENCE_CLASS, 'Subscriber', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg', 'Mib.Subscriber',
                [], [],
                '''                Subscriber threshold commands
                ''',
                'subscriber',
                'Cisco-IOS-XR-subscriber-session-mon-mibs-cfg', False),
            _MetaInfoClassMember('cb-qosmib', REFERENCE_CLASS, 'CbQosmib', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg', 'Mib.CbQosmib',
                [], [],
                '''                CBQoSMIB configuration
                ''',
                'cb_qosmib',
                'Cisco-IOS-XR-qos-mibs-cfg', False),
            _MetaInfoClassMember('mpls-te-mib', REFERENCE_CLASS, 'MplsTeMib', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg', 'Mib.MplsTeMib',
                [], [],
                '''                MPLS TE MIB configuration
                ''',
                'mpls_te_mib',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('mpls-p2mp-mib', REFERENCE_CLASS, 'MplsP2mpMib', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg', 'Mib.MplsP2mpMib',
                [], [],
                '''                MPLS P2MP MIB configuration
                ''',
                'mpls_p2mp_mib',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('mpls-te-ext-std-mib', REFERENCE_CLASS, 'MplsTeExtStdMib', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg', 'Mib.MplsTeExtStdMib',
                [], [],
                '''                MPLS TE EXT STD MIB configuration
                ''',
                'mpls_te_ext_std_mib',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('mpls-te-ext-mib', REFERENCE_CLASS, 'MplsTeExtMib', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg', 'Mib.MplsTeExtMib',
                [], [],
                '''                MPLS TE EXT MIB configuration
                ''',
                'mpls_te_ext_mib',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('mpls-frr-mib', REFERENCE_CLASS, 'MplsFrrMib', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg', 'Mib.MplsFrrMib',
                [], [],
                '''                FRR MIB configuration
                ''',
                'mpls_frr_mib',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            ],
            'Cisco-IOS-XR-snmp-agent-cfg',
            'mib',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-snmp-agent-cfg'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg',
        ),
    },
}
_meta_table['Snmp.EncryptedCommunityMaps.EncryptedCommunityMap']['meta_info'].parent =_meta_table['Snmp.EncryptedCommunityMaps']['meta_info']
_meta_table['Snmp.Views.View']['meta_info'].parent =_meta_table['Snmp.Views']['meta_info']
_meta_table['Snmp.Logging.Threshold']['meta_info'].parent =_meta_table['Snmp.Logging']['meta_info']
_meta_table['Snmp.Administration.DefaultCommunities.DefaultCommunity']['meta_info'].parent =_meta_table['Snmp.Administration.DefaultCommunities']['meta_info']
_meta_table['Snmp.Administration.EncryptedCommunities.EncryptedCommunity']['meta_info'].parent =_meta_table['Snmp.Administration.EncryptedCommunities']['meta_info']
_meta_table['Snmp.Administration.DefaultCommunities']['meta_info'].parent =_meta_table['Snmp.Administration']['meta_info']
_meta_table['Snmp.Administration.EncryptedCommunities']['meta_info'].parent =_meta_table['Snmp.Administration']['meta_info']
_meta_table['Snmp.Agent.EngineId.Remotes.Remote']['meta_info'].parent =_meta_table['Snmp.Agent.EngineId.Remotes']['meta_info']
_meta_table['Snmp.Agent.EngineId.Remotes']['meta_info'].parent =_meta_table['Snmp.Agent.EngineId']['meta_info']
_meta_table['Snmp.Agent.EngineId']['meta_info'].parent =_meta_table['Snmp.Agent']['meta_info']
_meta_table['Snmp.Ipv6.Tos']['meta_info'].parent =_meta_table['Snmp.Ipv6']['meta_info']
_meta_table['Snmp.Ipv4.Tos']['meta_info'].parent =_meta_table['Snmp.Ipv4']['meta_info']
_meta_table['Snmp.Target.Targets.Target_.VrfNames.VrfName']['meta_info'].parent =_meta_table['Snmp.Target.Targets.Target_.VrfNames']['meta_info']
_meta_table['Snmp.Target.Targets.Target_.TargetAddresses.TargetAddress']['meta_info'].parent =_meta_table['Snmp.Target.Targets.Target_.TargetAddresses']['meta_info']
_meta_table['Snmp.Target.Targets.Target_.VrfNames']['meta_info'].parent =_meta_table['Snmp.Target.Targets.Target_']['meta_info']
_meta_table['Snmp.Target.Targets.Target_.TargetAddresses']['meta_info'].parent =_meta_table['Snmp.Target.Targets.Target_']['meta_info']
_meta_table['Snmp.Target.Targets.Target_']['meta_info'].parent =_meta_table['Snmp.Target.Targets']['meta_info']
_meta_table['Snmp.Target.Targets']['meta_info'].parent =_meta_table['Snmp.Target']['meta_info']
_meta_table['Snmp.Notification.SubscriberMib.SessionAggregate']['meta_info'].parent =_meta_table['Snmp.Notification.SubscriberMib']['meta_info']
_meta_table['Snmp.Notification.Ospf.Lsa']['meta_info'].parent =_meta_table['Snmp.Notification.Ospf']['meta_info']
_meta_table['Snmp.Notification.Ospf.StateChange']['meta_info'].parent =_meta_table['Snmp.Notification.Ospf']['meta_info']
_meta_table['Snmp.Notification.Ospf.Retransmit']['meta_info'].parent =_meta_table['Snmp.Notification.Ospf']['meta_info']
_meta_table['Snmp.Notification.Ospf.Error']['meta_info'].parent =_meta_table['Snmp.Notification.Ospf']['meta_info']
_meta_table['Snmp.Notification.Bgp.Bgp4mib']['meta_info'].parent =_meta_table['Snmp.Notification.Bgp']['meta_info']
_meta_table['Snmp.Notification.Bgp.CiscoBgp4mib']['meta_info'].parent =_meta_table['Snmp.Notification.Bgp']['meta_info']
_meta_table['Snmp.Notification.MplsTe.CiscoExtension']['meta_info'].parent =_meta_table['Snmp.Notification.MplsTe']['meta_info']
_meta_table['Snmp.Notification.Ospfv3.Error']['meta_info'].parent =_meta_table['Snmp.Notification.Ospfv3']['meta_info']
_meta_table['Snmp.Notification.Ospfv3.StateChange']['meta_info'].parent =_meta_table['Snmp.Notification.Ospfv3']['meta_info']
_meta_table['Snmp.Notification.Snmp_']['meta_info'].parent =_meta_table['Snmp.Notification']['meta_info']
_meta_table['Snmp.Notification.SelectiveVrfDownload']['meta_info'].parent =_meta_table['Snmp.Notification']['meta_info']
_meta_table['Snmp.Notification.Vpls']['meta_info'].parent =_meta_table['Snmp.Notification']['meta_info']
_meta_table['Snmp.Notification.L2vpn']['meta_info'].parent =_meta_table['Snmp.Notification']['meta_info']
_meta_table['Snmp.Notification.Entity']['meta_info'].parent =_meta_table['Snmp.Notification']['meta_info']
_meta_table['Snmp.Notification.Bridge']['meta_info'].parent =_meta_table['Snmp.Notification']['meta_info']
_meta_table['Snmp.Notification.Rf']['meta_info'].parent =_meta_table['Snmp.Notification']['meta_info']
_meta_table['Snmp.Notification.Ntp']['meta_info'].parent =_meta_table['Snmp.Notification']['meta_info']
_meta_table['Snmp.Notification.Otn']['meta_info'].parent =_meta_table['Snmp.Notification']['meta_info']
_meta_table['Snmp.Notification.AddresspoolMib']['meta_info'].parent =_meta_table['Snmp.Notification']['meta_info']
_meta_table['Snmp.Notification.System']['meta_info'].parent =_meta_table['Snmp.Notification']['meta_info']
_meta_table['Snmp.Notification.Rsvp']['meta_info'].parent =_meta_table['Snmp.Notification']['meta_info']
_meta_table['Snmp.Notification.Sensor']['meta_info'].parent =_meta_table['Snmp.Notification']['meta_info']
_meta_table['Snmp.Notification.MplsLdp']['meta_info'].parent =_meta_table['Snmp.Notification']['meta_info']
_meta_table['Snmp.Notification.SubscriberMib']['meta_info'].parent =_meta_table['Snmp.Notification']['meta_info']
_meta_table['Snmp.Notification.Flash']['meta_info'].parent =_meta_table['Snmp.Notification']['meta_info']
_meta_table['Snmp.Notification.ConfigCopy']['meta_info'].parent =_meta_table['Snmp.Notification']['meta_info']
_meta_table['Snmp.Notification.Hsrp']['meta_info'].parent =_meta_table['Snmp.Notification']['meta_info']
_meta_table['Snmp.Notification.EntityRedundancy']['meta_info'].parent =_meta_table['Snmp.Notification']['meta_info']
_meta_table['Snmp.Notification.Isis']['meta_info'].parent =_meta_table['Snmp.Notification']['meta_info']
_meta_table['Snmp.Notification.Vrrp']['meta_info'].parent =_meta_table['Snmp.Notification']['meta_info']
_meta_table['Snmp.Notification.IpSec']['meta_info'].parent =_meta_table['Snmp.Notification']['meta_info']
_meta_table['Snmp.Notification.Isakmp']['meta_info'].parent =_meta_table['Snmp.Notification']['meta_info']
_meta_table['Snmp.Notification.CiscoEntityExt']['meta_info'].parent =_meta_table['Snmp.Notification']['meta_info']
_meta_table['Snmp.Notification.Ospf']['meta_info'].parent =_meta_table['Snmp.Notification']['meta_info']
_meta_table['Snmp.Notification.Cfm']['meta_info'].parent =_meta_table['Snmp.Notification']['meta_info']
_meta_table['Snmp.Notification.L2tun']['meta_info'].parent =_meta_table['Snmp.Notification']['meta_info']
_meta_table['Snmp.Notification.Bgp']['meta_info'].parent =_meta_table['Snmp.Notification']['meta_info']
_meta_table['Snmp.Notification.EntityState']['meta_info'].parent =_meta_table['Snmp.Notification']['meta_info']
_meta_table['Snmp.Notification.FrequencySynchronization']['meta_info'].parent =_meta_table['Snmp.Notification']['meta_info']
_meta_table['Snmp.Notification.MplsTeP2mp']['meta_info'].parent =_meta_table['Snmp.Notification']['meta_info']
_meta_table['Snmp.Notification.MplsTe']['meta_info'].parent =_meta_table['Snmp.Notification']['meta_info']
_meta_table['Snmp.Notification.MplsFrr']['meta_info'].parent =_meta_table['Snmp.Notification']['meta_info']
_meta_table['Snmp.Notification.Oam']['meta_info'].parent =_meta_table['Snmp.Notification']['meta_info']
_meta_table['Snmp.Notification.MplsL3vpn']['meta_info'].parent =_meta_table['Snmp.Notification']['meta_info']
_meta_table['Snmp.Notification.ConfigMan']['meta_info'].parent =_meta_table['Snmp.Notification']['meta_info']
_meta_table['Snmp.Notification.Diametermib']['meta_info'].parent =_meta_table['Snmp.Notification']['meta_info']
_meta_table['Snmp.Notification.FruControl']['meta_info'].parent =_meta_table['Snmp.Notification']['meta_info']
_meta_table['Snmp.Notification.Syslog']['meta_info'].parent =_meta_table['Snmp.Notification']['meta_info']
_meta_table['Snmp.Notification.Bfd']['meta_info'].parent =_meta_table['Snmp.Notification']['meta_info']
_meta_table['Snmp.Notification.OpticalOts']['meta_info'].parent =_meta_table['Snmp.Notification']['meta_info']
_meta_table['Snmp.Notification.Optical']['meta_info'].parent =_meta_table['Snmp.Notification']['meta_info']
_meta_table['Snmp.Notification.Ospfv3']['meta_info'].parent =_meta_table['Snmp.Notification']['meta_info']
_meta_table['Snmp.Correlator.Rules.Rule.RootCauses.RootCause.VarBinds.VarBind.Match']['meta_info'].parent =_meta_table['Snmp.Correlator.Rules.Rule.RootCauses.RootCause.VarBinds.VarBind']['meta_info']
_meta_table['Snmp.Correlator.Rules.Rule.RootCauses.RootCause.VarBinds.VarBind']['meta_info'].parent =_meta_table['Snmp.Correlator.Rules.Rule.RootCauses.RootCause.VarBinds']['meta_info']
_meta_table['Snmp.Correlator.Rules.Rule.RootCauses.RootCause.VarBinds']['meta_info'].parent =_meta_table['Snmp.Correlator.Rules.Rule.RootCauses.RootCause']['meta_info']
_meta_table['Snmp.Correlator.Rules.Rule.RootCauses.RootCause']['meta_info'].parent =_meta_table['Snmp.Correlator.Rules.Rule.RootCauses']['meta_info']
_meta_table['Snmp.Correlator.Rules.Rule.NonRootCauses.NonRootCause.VarBinds.VarBind.Match']['meta_info'].parent =_meta_table['Snmp.Correlator.Rules.Rule.NonRootCauses.NonRootCause.VarBinds.VarBind']['meta_info']
_meta_table['Snmp.Correlator.Rules.Rule.NonRootCauses.NonRootCause.VarBinds.VarBind']['meta_info'].parent =_meta_table['Snmp.Correlator.Rules.Rule.NonRootCauses.NonRootCause.VarBinds']['meta_info']
_meta_table['Snmp.Correlator.Rules.Rule.NonRootCauses.NonRootCause.VarBinds']['meta_info'].parent =_meta_table['Snmp.Correlator.Rules.Rule.NonRootCauses.NonRootCause']['meta_info']
_meta_table['Snmp.Correlator.Rules.Rule.NonRootCauses.NonRootCause']['meta_info'].parent =_meta_table['Snmp.Correlator.Rules.Rule.NonRootCauses']['meta_info']
_meta_table['Snmp.Correlator.Rules.Rule.AppliedTo.Hosts.Host']['meta_info'].parent =_meta_table['Snmp.Correlator.Rules.Rule.AppliedTo.Hosts']['meta_info']
_meta_table['Snmp.Correlator.Rules.Rule.AppliedTo.Hosts']['meta_info'].parent =_meta_table['Snmp.Correlator.Rules.Rule.AppliedTo']['meta_info']
_meta_table['Snmp.Correlator.Rules.Rule.RootCauses']['meta_info'].parent =_meta_table['Snmp.Correlator.Rules.Rule']['meta_info']
_meta_table['Snmp.Correlator.Rules.Rule.NonRootCauses']['meta_info'].parent =_meta_table['Snmp.Correlator.Rules.Rule']['meta_info']
_meta_table['Snmp.Correlator.Rules.Rule.AppliedTo']['meta_info'].parent =_meta_table['Snmp.Correlator.Rules.Rule']['meta_info']
_meta_table['Snmp.Correlator.Rules.Rule']['meta_info'].parent =_meta_table['Snmp.Correlator.Rules']['meta_info']
_meta_table['Snmp.Correlator.RuleSets.RuleSet.Rulenames.Rulename']['meta_info'].parent =_meta_table['Snmp.Correlator.RuleSets.RuleSet.Rulenames']['meta_info']
_meta_table['Snmp.Correlator.RuleSets.RuleSet.AppliedTo.Hosts.Host']['meta_info'].parent =_meta_table['Snmp.Correlator.RuleSets.RuleSet.AppliedTo.Hosts']['meta_info']
_meta_table['Snmp.Correlator.RuleSets.RuleSet.AppliedTo.Hosts']['meta_info'].parent =_meta_table['Snmp.Correlator.RuleSets.RuleSet.AppliedTo']['meta_info']
_meta_table['Snmp.Correlator.RuleSets.RuleSet.Rulenames']['meta_info'].parent =_meta_table['Snmp.Correlator.RuleSets.RuleSet']['meta_info']
_meta_table['Snmp.Correlator.RuleSets.RuleSet.AppliedTo']['meta_info'].parent =_meta_table['Snmp.Correlator.RuleSets.RuleSet']['meta_info']
_meta_table['Snmp.Correlator.RuleSets.RuleSet']['meta_info'].parent =_meta_table['Snmp.Correlator.RuleSets']['meta_info']
_meta_table['Snmp.Correlator.Rules']['meta_info'].parent =_meta_table['Snmp.Correlator']['meta_info']
_meta_table['Snmp.Correlator.RuleSets']['meta_info'].parent =_meta_table['Snmp.Correlator']['meta_info']
_meta_table['Snmp.BulkStats.Schemas.Schema.Instance']['meta_info'].parent =_meta_table['Snmp.BulkStats.Schemas.Schema']['meta_info']
_meta_table['Snmp.BulkStats.Schemas.Schema']['meta_info'].parent =_meta_table['Snmp.BulkStats.Schemas']['meta_info']
_meta_table['Snmp.BulkStats.Objects.Object.Objects_.Object_']['meta_info'].parent =_meta_table['Snmp.BulkStats.Objects.Object.Objects_']['meta_info']
_meta_table['Snmp.BulkStats.Objects.Object.Objects_']['meta_info'].parent =_meta_table['Snmp.BulkStats.Objects.Object']['meta_info']
_meta_table['Snmp.BulkStats.Objects.Object']['meta_info'].parent =_meta_table['Snmp.BulkStats.Objects']['meta_info']
_meta_table['Snmp.BulkStats.Transfers.Transfer.TransferSchemas.TransferSchema']['meta_info'].parent =_meta_table['Snmp.BulkStats.Transfers.Transfer.TransferSchemas']['meta_info']
_meta_table['Snmp.BulkStats.Transfers.Transfer.TransferSchemas']['meta_info'].parent =_meta_table['Snmp.BulkStats.Transfers.Transfer']['meta_info']
_meta_table['Snmp.BulkStats.Transfers.Transfer']['meta_info'].parent =_meta_table['Snmp.BulkStats.Transfers']['meta_info']
_meta_table['Snmp.BulkStats.Schemas']['meta_info'].parent =_meta_table['Snmp.BulkStats']['meta_info']
_meta_table['Snmp.BulkStats.Objects']['meta_info'].parent =_meta_table['Snmp.BulkStats']['meta_info']
_meta_table['Snmp.BulkStats.Transfers']['meta_info'].parent =_meta_table['Snmp.BulkStats']['meta_info']
_meta_table['Snmp.DefaultCommunityMaps.DefaultCommunityMap']['meta_info'].parent =_meta_table['Snmp.DefaultCommunityMaps']['meta_info']
_meta_table['Snmp.Users.User']['meta_info'].parent =_meta_table['Snmp.Users']['meta_info']
_meta_table['Snmp.Vrfs.Vrf.TrapHosts.TrapHost.EncryptedUserCommunities.EncryptedUserCommunity']['meta_info'].parent =_meta_table['Snmp.Vrfs.Vrf.TrapHosts.TrapHost.EncryptedUserCommunities']['meta_info']
_meta_table['Snmp.Vrfs.Vrf.TrapHosts.TrapHost.InformHost.InformUserCommunities.InformUserCommunity']['meta_info'].parent =_meta_table['Snmp.Vrfs.Vrf.TrapHosts.TrapHost.InformHost.InformUserCommunities']['meta_info']
_meta_table['Snmp.Vrfs.Vrf.TrapHosts.TrapHost.InformHost.InformEncryptedUserCommunities.InformEncryptedUserCommunity']['meta_info'].parent =_meta_table['Snmp.Vrfs.Vrf.TrapHosts.TrapHost.InformHost.InformEncryptedUserCommunities']['meta_info']
_meta_table['Snmp.Vrfs.Vrf.TrapHosts.TrapHost.InformHost.InformUserCommunities']['meta_info'].parent =_meta_table['Snmp.Vrfs.Vrf.TrapHosts.TrapHost.InformHost']['meta_info']
_meta_table['Snmp.Vrfs.Vrf.TrapHosts.TrapHost.InformHost.InformEncryptedUserCommunities']['meta_info'].parent =_meta_table['Snmp.Vrfs.Vrf.TrapHosts.TrapHost.InformHost']['meta_info']
_meta_table['Snmp.Vrfs.Vrf.TrapHosts.TrapHost.DefaultUserCommunities.DefaultUserCommunity']['meta_info'].parent =_meta_table['Snmp.Vrfs.Vrf.TrapHosts.TrapHost.DefaultUserCommunities']['meta_info']
_meta_table['Snmp.Vrfs.Vrf.TrapHosts.TrapHost.EncryptedUserCommunities']['meta_info'].parent =_meta_table['Snmp.Vrfs.Vrf.TrapHosts.TrapHost']['meta_info']
_meta_table['Snmp.Vrfs.Vrf.TrapHosts.TrapHost.InformHost']['meta_info'].parent =_meta_table['Snmp.Vrfs.Vrf.TrapHosts.TrapHost']['meta_info']
_meta_table['Snmp.Vrfs.Vrf.TrapHosts.TrapHost.DefaultUserCommunities']['meta_info'].parent =_meta_table['Snmp.Vrfs.Vrf.TrapHosts.TrapHost']['meta_info']
_meta_table['Snmp.Vrfs.Vrf.TrapHosts.TrapHost']['meta_info'].parent =_meta_table['Snmp.Vrfs.Vrf.TrapHosts']['meta_info']
_meta_table['Snmp.Vrfs.Vrf.Contexts.Context']['meta_info'].parent =_meta_table['Snmp.Vrfs.Vrf.Contexts']['meta_info']
_meta_table['Snmp.Vrfs.Vrf.ContextMappings.ContextMapping']['meta_info'].parent =_meta_table['Snmp.Vrfs.Vrf.ContextMappings']['meta_info']
_meta_table['Snmp.Vrfs.Vrf.TrapHosts']['meta_info'].parent =_meta_table['Snmp.Vrfs.Vrf']['meta_info']
_meta_table['Snmp.Vrfs.Vrf.Contexts']['meta_info'].parent =_meta_table['Snmp.Vrfs.Vrf']['meta_info']
_meta_table['Snmp.Vrfs.Vrf.ContextMappings']['meta_info'].parent =_meta_table['Snmp.Vrfs.Vrf']['meta_info']
_meta_table['Snmp.Vrfs.Vrf']['meta_info'].parent =_meta_table['Snmp.Vrfs']['meta_info']
_meta_table['Snmp.Groups.Group']['meta_info'].parent =_meta_table['Snmp.Groups']['meta_info']
_meta_table['Snmp.TrapHosts.TrapHost.EncryptedUserCommunities.EncryptedUserCommunity']['meta_info'].parent =_meta_table['Snmp.TrapHosts.TrapHost.EncryptedUserCommunities']['meta_info']
_meta_table['Snmp.TrapHosts.TrapHost.InformHost.InformUserCommunities.InformUserCommunity']['meta_info'].parent =_meta_table['Snmp.TrapHosts.TrapHost.InformHost.InformUserCommunities']['meta_info']
_meta_table['Snmp.TrapHosts.TrapHost.InformHost.InformEncryptedUserCommunities.InformEncryptedUserCommunity']['meta_info'].parent =_meta_table['Snmp.TrapHosts.TrapHost.InformHost.InformEncryptedUserCommunities']['meta_info']
_meta_table['Snmp.TrapHosts.TrapHost.InformHost.InformUserCommunities']['meta_info'].parent =_meta_table['Snmp.TrapHosts.TrapHost.InformHost']['meta_info']
_meta_table['Snmp.TrapHosts.TrapHost.InformHost.InformEncryptedUserCommunities']['meta_info'].parent =_meta_table['Snmp.TrapHosts.TrapHost.InformHost']['meta_info']
_meta_table['Snmp.TrapHosts.TrapHost.DefaultUserCommunities.DefaultUserCommunity']['meta_info'].parent =_meta_table['Snmp.TrapHosts.TrapHost.DefaultUserCommunities']['meta_info']
_meta_table['Snmp.TrapHosts.TrapHost.EncryptedUserCommunities']['meta_info'].parent =_meta_table['Snmp.TrapHosts.TrapHost']['meta_info']
_meta_table['Snmp.TrapHosts.TrapHost.InformHost']['meta_info'].parent =_meta_table['Snmp.TrapHosts.TrapHost']['meta_info']
_meta_table['Snmp.TrapHosts.TrapHost.DefaultUserCommunities']['meta_info'].parent =_meta_table['Snmp.TrapHosts.TrapHost']['meta_info']
_meta_table['Snmp.TrapHosts.TrapHost']['meta_info'].parent =_meta_table['Snmp.TrapHosts']['meta_info']
_meta_table['Snmp.Contexts.Context']['meta_info'].parent =_meta_table['Snmp.Contexts']['meta_info']
_meta_table['Snmp.ContextMappings.ContextMapping']['meta_info'].parent =_meta_table['Snmp.ContextMappings']['meta_info']
_meta_table['Snmp.EncryptedCommunityMaps']['meta_info'].parent =_meta_table['Snmp']['meta_info']
_meta_table['Snmp.Views']['meta_info'].parent =_meta_table['Snmp']['meta_info']
_meta_table['Snmp.Logging']['meta_info'].parent =_meta_table['Snmp']['meta_info']
_meta_table['Snmp.Administration']['meta_info'].parent =_meta_table['Snmp']['meta_info']
_meta_table['Snmp.Agent']['meta_info'].parent =_meta_table['Snmp']['meta_info']
_meta_table['Snmp.Trap']['meta_info'].parent =_meta_table['Snmp']['meta_info']
_meta_table['Snmp.DropPacket']['meta_info'].parent =_meta_table['Snmp']['meta_info']
_meta_table['Snmp.Ipv6']['meta_info'].parent =_meta_table['Snmp']['meta_info']
_meta_table['Snmp.Ipv4']['meta_info'].parent =_meta_table['Snmp']['meta_info']
_meta_table['Snmp.System']['meta_info'].parent =_meta_table['Snmp']['meta_info']
_meta_table['Snmp.Target']['meta_info'].parent =_meta_table['Snmp']['meta_info']
_meta_table['Snmp.Notification']['meta_info'].parent =_meta_table['Snmp']['meta_info']
_meta_table['Snmp.Correlator']['meta_info'].parent =_meta_table['Snmp']['meta_info']
_meta_table['Snmp.BulkStats']['meta_info'].parent =_meta_table['Snmp']['meta_info']
_meta_table['Snmp.DefaultCommunityMaps']['meta_info'].parent =_meta_table['Snmp']['meta_info']
_meta_table['Snmp.OverloadControl']['meta_info'].parent =_meta_table['Snmp']['meta_info']
_meta_table['Snmp.Timeouts']['meta_info'].parent =_meta_table['Snmp']['meta_info']
_meta_table['Snmp.Users']['meta_info'].parent =_meta_table['Snmp']['meta_info']
_meta_table['Snmp.Vrfs']['meta_info'].parent =_meta_table['Snmp']['meta_info']
_meta_table['Snmp.Groups']['meta_info'].parent =_meta_table['Snmp']['meta_info']
_meta_table['Snmp.TrapHosts']['meta_info'].parent =_meta_table['Snmp']['meta_info']
_meta_table['Snmp.Contexts']['meta_info'].parent =_meta_table['Snmp']['meta_info']
_meta_table['Snmp.ContextMappings']['meta_info'].parent =_meta_table['Snmp']['meta_info']
_meta_table['Mib.InterfaceMib.Interfaces.Interface']['meta_info'].parent =_meta_table['Mib.InterfaceMib.Interfaces']['meta_info']
_meta_table['Mib.InterfaceMib.Subsets.Subset.LinkUpDown']['meta_info'].parent =_meta_table['Mib.InterfaceMib.Subsets.Subset']['meta_info']
_meta_table['Mib.InterfaceMib.Subsets.Subset']['meta_info'].parent =_meta_table['Mib.InterfaceMib.Subsets']['meta_info']
_meta_table['Mib.InterfaceMib.Interfaces']['meta_info'].parent =_meta_table['Mib.InterfaceMib']['meta_info']
_meta_table['Mib.InterfaceMib.Notification']['meta_info'].parent =_meta_table['Mib.InterfaceMib']['meta_info']
_meta_table['Mib.InterfaceMib.Subsets']['meta_info'].parent =_meta_table['Mib.InterfaceMib']['meta_info']
_meta_table['Mib.Subscriber.Threshold.Delta.Evaluation.AccessInterfaces.AccessInterface']['meta_info'].parent =_meta_table['Mib.Subscriber.Threshold.Delta.Evaluation.AccessInterfaces']['meta_info']
_meta_table['Mib.Subscriber.Threshold.Delta.Evaluation.Nodes.Node']['meta_info'].parent =_meta_table['Mib.Subscriber.Threshold.Delta.Evaluation.Nodes']['meta_info']
_meta_table['Mib.Subscriber.Threshold.Delta.Evaluation.AccessInterfaces']['meta_info'].parent =_meta_table['Mib.Subscriber.Threshold.Delta.Evaluation']['meta_info']
_meta_table['Mib.Subscriber.Threshold.Delta.Evaluation.Nodes']['meta_info'].parent =_meta_table['Mib.Subscriber.Threshold.Delta.Evaluation']['meta_info']
_meta_table['Mib.Subscriber.Threshold.Delta.Percent.AccessInterfaces.AccessInterface']['meta_info'].parent =_meta_table['Mib.Subscriber.Threshold.Delta.Percent.AccessInterfaces']['meta_info']
_meta_table['Mib.Subscriber.Threshold.Delta.Percent.Nodes.Node']['meta_info'].parent =_meta_table['Mib.Subscriber.Threshold.Delta.Percent.Nodes']['meta_info']
_meta_table['Mib.Subscriber.Threshold.Delta.Percent.AccessInterfaces']['meta_info'].parent =_meta_table['Mib.Subscriber.Threshold.Delta.Percent']['meta_info']
_meta_table['Mib.Subscriber.Threshold.Delta.Percent.Nodes']['meta_info'].parent =_meta_table['Mib.Subscriber.Threshold.Delta.Percent']['meta_info']
_meta_table['Mib.Subscriber.Threshold.Delta.Evaluation']['meta_info'].parent =_meta_table['Mib.Subscriber.Threshold.Delta']['meta_info']
_meta_table['Mib.Subscriber.Threshold.Delta.Percent']['meta_info'].parent =_meta_table['Mib.Subscriber.Threshold.Delta']['meta_info']
_meta_table['Mib.Subscriber.Threshold.AccessInterfaceSub.Subsets.Subset.RegularExpression.Notification.RisingFalling']['meta_info'].parent =_meta_table['Mib.Subscriber.Threshold.AccessInterfaceSub.Subsets.Subset.RegularExpression.Notification']['meta_info']
_meta_table['Mib.Subscriber.Threshold.AccessInterfaceSub.Subsets.Subset.RegularExpression.Notification']['meta_info'].parent =_meta_table['Mib.Subscriber.Threshold.AccessInterfaceSub.Subsets.Subset.RegularExpression']['meta_info']
_meta_table['Mib.Subscriber.Threshold.AccessInterfaceSub.Subsets.Subset.RegularExpression']['meta_info'].parent =_meta_table['Mib.Subscriber.Threshold.AccessInterfaceSub.Subsets.Subset']['meta_info']
_meta_table['Mib.Subscriber.Threshold.AccessInterfaceSub.Subsets.Subset']['meta_info'].parent =_meta_table['Mib.Subscriber.Threshold.AccessInterfaceSub.Subsets']['meta_info']
_meta_table['Mib.Subscriber.Threshold.AccessInterfaceSub.Subsets']['meta_info'].parent =_meta_table['Mib.Subscriber.Threshold.AccessInterfaceSub']['meta_info']
_meta_table['Mib.Subscriber.Threshold.Falling.AccessInterfaces.AccessInterface']['meta_info'].parent =_meta_table['Mib.Subscriber.Threshold.Falling.AccessInterfaces']['meta_info']
_meta_table['Mib.Subscriber.Threshold.Falling.Nodes.Node']['meta_info'].parent =_meta_table['Mib.Subscriber.Threshold.Falling.Nodes']['meta_info']
_meta_table['Mib.Subscriber.Threshold.Falling.AccessInterfaces']['meta_info'].parent =_meta_table['Mib.Subscriber.Threshold.Falling']['meta_info']
_meta_table['Mib.Subscriber.Threshold.Falling.Nodes']['meta_info'].parent =_meta_table['Mib.Subscriber.Threshold.Falling']['meta_info']
_meta_table['Mib.Subscriber.Threshold.Rising.AccessInterfaces.AccessInterface']['meta_info'].parent =_meta_table['Mib.Subscriber.Threshold.Rising.AccessInterfaces']['meta_info']
_meta_table['Mib.Subscriber.Threshold.Rising.Nodes.Node']['meta_info'].parent =_meta_table['Mib.Subscriber.Threshold.Rising.Nodes']['meta_info']
_meta_table['Mib.Subscriber.Threshold.Rising.AccessInterfaces']['meta_info'].parent =_meta_table['Mib.Subscriber.Threshold.Rising']['meta_info']
_meta_table['Mib.Subscriber.Threshold.Rising.Nodes']['meta_info'].parent =_meta_table['Mib.Subscriber.Threshold.Rising']['meta_info']
_meta_table['Mib.Subscriber.Threshold.Delta']['meta_info'].parent =_meta_table['Mib.Subscriber.Threshold']['meta_info']
_meta_table['Mib.Subscriber.Threshold.AccessInterfaceSub']['meta_info'].parent =_meta_table['Mib.Subscriber.Threshold']['meta_info']
_meta_table['Mib.Subscriber.Threshold.Falling']['meta_info'].parent =_meta_table['Mib.Subscriber.Threshold']['meta_info']
_meta_table['Mib.Subscriber.Threshold.Rising']['meta_info'].parent =_meta_table['Mib.Subscriber.Threshold']['meta_info']
_meta_table['Mib.Subscriber.Threshold']['meta_info'].parent =_meta_table['Mib.Subscriber']['meta_info']
_meta_table['Mib.CbQosmib.Cache']['meta_info'].parent =_meta_table['Mib.CbQosmib']['meta_info']
_meta_table['Mib.NotificationLogMib']['meta_info'].parent =_meta_table['Mib']['meta_info']
_meta_table['Mib.EntityMib']['meta_info'].parent =_meta_table['Mib']['meta_info']
_meta_table['Mib.InterfaceMib']['meta_info'].parent =_meta_table['Mib']['meta_info']
_meta_table['Mib.Subscriber']['meta_info'].parent =_meta_table['Mib']['meta_info']
_meta_table['Mib.CbQosmib']['meta_info'].parent =_meta_table['Mib']['meta_info']
_meta_table['Mib.MplsTeMib']['meta_info'].parent =_meta_table['Mib']['meta_info']
_meta_table['Mib.MplsP2mpMib']['meta_info'].parent =_meta_table['Mib']['meta_info']
_meta_table['Mib.MplsTeExtStdMib']['meta_info'].parent =_meta_table['Mib']['meta_info']
_meta_table['Mib.MplsTeExtMib']['meta_info'].parent =_meta_table['Mib']['meta_info']
_meta_table['Mib.MplsFrrMib']['meta_info'].parent =_meta_table['Mib']['meta_info']
