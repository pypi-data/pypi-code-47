
'''
This is auto-generated file,
which includes metadata for module tailf_confd_monitoring
'''

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_LIST, REFERENCE_LEAFLIST, REFERENCE_BITS, REFERENCE_UNION
from ydk._core._dm_meta_info import REFERENCE_CLASS, REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, ANYXML_CLASS
from ydk._core._importer import _yang_ns

_meta_table = {
    'ConfdState.Smp' : {
        'meta_info' : _MetaInfoClass('ConfdState.Smp', REFERENCE_CLASS,
            ''' ''',
            False, 
            [
            _MetaInfoClassMember('number-of-threads', ATTRIBUTE, 'int', 'uint16',
                None, None,
                [('0', '65535')], [],
                '''                Number of threads used by the daemon.
                ''',
                'number_of_threads',
                'tailf-confd-monitoring', False, is_config=False),
            ],
            'tailf-confd-monitoring',
            'smp',
            _yang_ns.NAMESPACE_LOOKUP['tailf-confd-monitoring'],
            'ydk.models.cisco_ios_xr.tailf_confd_monitoring',
            is_config=False,
            is_presence=True,
        ),
    },
    'ConfdState.Ha.Mode' : _MetaInfoEnum('Mode',
        'ydk.models.cisco_ios_xr.tailf_confd_monitoring', 'ConfdState.Ha.Mode',
        '''The current HA mode of the node in the HA cluster.''',
        {
            'none':'none',
            'slave':'slave',
            'master':'master',
            'relay-slave':'relay_slave',
        }, 'tailf-common-monitoring', _yang_ns.NAMESPACE_LOOKUP['tailf-common-monitoring']),
    'ConfdState.Ha' : {
        'meta_info' : _MetaInfoClass('ConfdState.Ha', REFERENCE_CLASS,
            ''' ''',
            False, 
            [
            _MetaInfoClassMember('mode', REFERENCE_ENUM_CLASS, 'Mode', 'enumeration',
                'ydk.models.cisco_ios_xr.tailf_confd_monitoring', 'ConfdState.Ha.Mode',
                [], [],
                '''                The current HA mode of the node in the HA cluster.
                ''',
                'mode',
                'tailf-confd-monitoring', False, is_config=False),
            _MetaInfoClassMember('node-id', ATTRIBUTE, 'str', 'ha-node-id',
                None, None,
                [], [],
                '''                The node identifier of this node in the HA cluster.
                ''',
                'node_id',
                'tailf-confd-monitoring', False, is_config=False, has_when=True),
            _MetaInfoClassMember('master-node-id', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                The node identifier of this node's parent node.
                This is the HA cluster's master node unless relay slaves
                are used.
                ''',
                'master_node_id',
                'tailf-confd-monitoring', False, is_config=False, has_when=True),
            _MetaInfoClassMember('connected-slave', REFERENCE_LEAFLIST, 'str', 'string',
                None, None,
                [], [],
                '''                The node identifiers of the currently connected slaves.
                ''',
                'connected_slave',
                'tailf-confd-monitoring', False, is_config=False, has_when=True),
            _MetaInfoClassMember('pending-slave', REFERENCE_LEAFLIST, 'str', 'string',
                None, None,
                [], [],
                '''                The node identifiers of slaves with pending acknowledgement
                of synchronous replication.
                ''',
                'pending_slave',
                'tailf-confd-monitoring', False, is_config=False, has_when=True),
            ],
            'tailf-confd-monitoring',
            'ha',
            _yang_ns.NAMESPACE_LOOKUP['tailf-confd-monitoring'],
            'ydk.models.cisco_ios_xr.tailf_confd_monitoring',
            is_config=False,
            is_presence=True,
        ),
    },
    'ConfdState.LoadedDataModels.DataModel.ExportedTo' : _MetaInfoEnum('ExportedTo',
        'ydk.models.cisco_ios_xr.tailf_confd_monitoring', 'ConfdState.LoadedDataModels.DataModel.ExportedTo',
        ''' ''',
        {
            'netconf':'netconf',
            'cli':'cli',
            'webui':'webui',
            'rest':'rest',
            'snmp':'snmp',
        }, 'tailf-common-monitoring', _yang_ns.NAMESPACE_LOOKUP['tailf-common-monitoring']),
    'ConfdState.LoadedDataModels.DataModel' : {
        'meta_info' : _MetaInfoClass('ConfdState.LoadedDataModels.DataModel', REFERENCE_LIST,
            '''This list contains all loaded YANG data modules.

This list is a superset of the 'schema' list defined in
ietf-netconf-monitoring, which only lists modules exported
through NETCONF.''',
            False, 
            [
            _MetaInfoClassMember('name', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                The YANG module name.
                ''',
                'name',
                'tailf-confd-monitoring', True, is_config=False),
            _MetaInfoClassMember('revision', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                The YANG module revision.
                ''',
                'revision',
                'tailf-confd-monitoring', False, is_config=False),
            _MetaInfoClassMember('namespace', ATTRIBUTE, 'str', 'inet:uri',
                None, None,
                [], [],
                '''                The YANG module namespace.
                ''',
                'namespace',
                'tailf-confd-monitoring', False, is_config=False),
            _MetaInfoClassMember('prefix', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                The prefix defined in the YANG module.
                ''',
                'prefix',
                'tailf-confd-monitoring', False, is_config=False),
            _MetaInfoClassMember('exported-to-all', ATTRIBUTE, 'Empty', 'empty',
                None, None,
                [], [],
                '''                This leaf is present if the module is exported to all
                northbound interfaces.
                ''',
                'exported_to_all',
                'tailf-confd-monitoring', False, is_config=False),
            _MetaInfoClassMember('exported-to', REFERENCE_UNION, 'str', 'union',
                None, None,
                [], [],
                '''                A list of the contexts (northbound interfaces) this module
                is exported to.
                ''',
                'exported_to',
                'tailf-confd-monitoring', False, [
                    _MetaInfoClassMember('exported-to', REFERENCE_LEAFLIST, 'ConfdState.LoadedDataModels.DataModel.ExportedTo', 'enumeration',
                        'ydk.models.cisco_ios_xr.tailf_confd_monitoring', 'ConfdState.LoadedDataModels.DataModel.ExportedTo',
                        [], [],
                        '''                        A list of the contexts (northbound interfaces) this module
                        is exported to.
                        ''',
                        'exported_to',
                        'tailf-confd-monitoring', False, is_config=False),
                    _MetaInfoClassMember('exported-to', REFERENCE_LEAFLIST, 'str', 'string',
                        None, None,
                        [], [],
                        '''                        A list of the contexts (northbound interfaces) this module
                        is exported to.
                        ''',
                        'exported_to',
                        'tailf-confd-monitoring', False, is_config=False),
                ], is_config=False),
            ],
            'tailf-confd-monitoring',
            'data-model',
            _yang_ns.NAMESPACE_LOOKUP['tailf-confd-monitoring'],
            'ydk.models.cisco_ios_xr.tailf_confd_monitoring',
            is_config=False,
        ),
    },
    'ConfdState.LoadedDataModels' : {
        'meta_info' : _MetaInfoClass('ConfdState.LoadedDataModels', REFERENCE_CLASS,
            ''' ''',
            False, 
            [
            _MetaInfoClassMember('data-model', REFERENCE_LIST, 'DataModel', '',
                'ydk.models.cisco_ios_xr.tailf_confd_monitoring', 'ConfdState.LoadedDataModels.DataModel',
                [], [],
                '''                This list contains all loaded YANG data modules.
                
                This list is a superset of the 'schema' list defined in
                ietf-netconf-monitoring, which only lists modules exported
                through NETCONF.
                ''',
                'data_model',
                'tailf-confd-monitoring', False, is_config=False),
            ],
            'tailf-confd-monitoring',
            'loaded-data-models',
            _yang_ns.NAMESPACE_LOOKUP['tailf-confd-monitoring'],
            'ydk.models.cisco_ios_xr.tailf_confd_monitoring',
            is_config=False,
        ),
    },
    'ConfdState.Netconf.Listen.Tcp' : {
        'meta_info' : _MetaInfoClass('ConfdState.Netconf.Listen.Tcp', REFERENCE_LIST,
            ''' ''',
            False, 
            [
            _MetaInfoClassMember('ip', REFERENCE_UNION, 'str', 'inet:ip-address',
                None, None,
                [], [],
                '''                ''',
                'ip',
                'tailf-confd-monitoring', False, [
                    _MetaInfoClassMember('ip', ATTRIBUTE, 'str', 'inet:ipv4-address',
                        None, None,
                        [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'],
                        '''                        ''',
                        'ip',
                        'tailf-confd-monitoring', False, is_config=False),
                    _MetaInfoClassMember('ip', ATTRIBUTE, 'str', 'inet:ipv6-address',
                        None, None,
                        [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'],
                        '''                        ''',
                        'ip',
                        'tailf-confd-monitoring', False, is_config=False),
                ], is_config=False),
            _MetaInfoClassMember('port', ATTRIBUTE, 'int', 'inet:port-number',
                None, None,
                [('0', '65535')], [],
                '''                ''',
                'port',
                'tailf-confd-monitoring', False, is_config=False),
            ],
            'tailf-confd-monitoring',
            'tcp',
            _yang_ns.NAMESPACE_LOOKUP['tailf-confd-monitoring'],
            'ydk.models.cisco_ios_xr.tailf_confd_monitoring',
            is_config=False,
        ),
    },
    'ConfdState.Netconf.Listen.Ssh' : {
        'meta_info' : _MetaInfoClass('ConfdState.Netconf.Listen.Ssh', REFERENCE_LIST,
            ''' ''',
            False, 
            [
            _MetaInfoClassMember('ip', REFERENCE_UNION, 'str', 'inet:ip-address',
                None, None,
                [], [],
                '''                ''',
                'ip',
                'tailf-confd-monitoring', False, [
                    _MetaInfoClassMember('ip', ATTRIBUTE, 'str', 'inet:ipv4-address',
                        None, None,
                        [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'],
                        '''                        ''',
                        'ip',
                        'tailf-confd-monitoring', False, is_config=False),
                    _MetaInfoClassMember('ip', ATTRIBUTE, 'str', 'inet:ipv6-address',
                        None, None,
                        [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'],
                        '''                        ''',
                        'ip',
                        'tailf-confd-monitoring', False, is_config=False),
                ], is_config=False),
            _MetaInfoClassMember('port', ATTRIBUTE, 'int', 'inet:port-number',
                None, None,
                [('0', '65535')], [],
                '''                ''',
                'port',
                'tailf-confd-monitoring', False, is_config=False),
            ],
            'tailf-confd-monitoring',
            'ssh',
            _yang_ns.NAMESPACE_LOOKUP['tailf-confd-monitoring'],
            'ydk.models.cisco_ios_xr.tailf_confd_monitoring',
            is_config=False,
        ),
    },
    'ConfdState.Netconf.Listen' : {
        'meta_info' : _MetaInfoClass('ConfdState.Netconf.Listen', REFERENCE_CLASS,
            '''The transport addresses the NETCONF server is listening on.

Note that other mechanisms can be put in front of the TCP
addresses below, e.g., an OpenSSH server.  Such mechanisms
are not known to the daemon and not listed here.''',
            False, 
            [
            _MetaInfoClassMember('tcp', REFERENCE_LIST, 'Tcp', '',
                'ydk.models.cisco_ios_xr.tailf_confd_monitoring', 'ConfdState.Netconf.Listen.Tcp',
                [], [],
                '''                ''',
                'tcp',
                'tailf-confd-monitoring', False, is_config=False),
            _MetaInfoClassMember('ssh', REFERENCE_LIST, 'Ssh', '',
                'ydk.models.cisco_ios_xr.tailf_confd_monitoring', 'ConfdState.Netconf.Listen.Ssh',
                [], [],
                '''                ''',
                'ssh',
                'tailf-confd-monitoring', False, is_config=False),
            ],
            'tailf-confd-monitoring',
            'listen',
            _yang_ns.NAMESPACE_LOOKUP['tailf-confd-monitoring'],
            'ydk.models.cisco_ios_xr.tailf_confd_monitoring',
            is_config=False,
        ),
    },
    'ConfdState.Netconf' : {
        'meta_info' : _MetaInfoClass('ConfdState.Netconf', REFERENCE_CLASS,
            ''' ''',
            False, 
            [
            _MetaInfoClassMember('listen', REFERENCE_CLASS, 'Listen', '',
                'ydk.models.cisco_ios_xr.tailf_confd_monitoring', 'ConfdState.Netconf.Listen',
                [], [],
                '''                The transport addresses the NETCONF server is listening on.
                
                Note that other mechanisms can be put in front of the TCP
                addresses below, e.g., an OpenSSH server.  Such mechanisms
                are not known to the daemon and not listed here.
                ''',
                'listen',
                'tailf-confd-monitoring', False, is_config=False),
            ],
            'tailf-confd-monitoring',
            'netconf',
            _yang_ns.NAMESPACE_LOOKUP['tailf-confd-monitoring'],
            'ydk.models.cisco_ios_xr.tailf_confd_monitoring',
            is_config=False,
            is_presence=True,
        ),
    },
    'ConfdState.Cli.Listen.Ssh' : {
        'meta_info' : _MetaInfoClass('ConfdState.Cli.Listen.Ssh', REFERENCE_LIST,
            ''' ''',
            False, 
            [
            _MetaInfoClassMember('ip', REFERENCE_UNION, 'str', 'inet:ip-address',
                None, None,
                [], [],
                '''                ''',
                'ip',
                'tailf-confd-monitoring', False, [
                    _MetaInfoClassMember('ip', ATTRIBUTE, 'str', 'inet:ipv4-address',
                        None, None,
                        [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'],
                        '''                        ''',
                        'ip',
                        'tailf-confd-monitoring', False, is_config=False),
                    _MetaInfoClassMember('ip', ATTRIBUTE, 'str', 'inet:ipv6-address',
                        None, None,
                        [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'],
                        '''                        ''',
                        'ip',
                        'tailf-confd-monitoring', False, is_config=False),
                ], is_config=False),
            _MetaInfoClassMember('port', ATTRIBUTE, 'int', 'inet:port-number',
                None, None,
                [('0', '65535')], [],
                '''                ''',
                'port',
                'tailf-confd-monitoring', False, is_config=False),
            ],
            'tailf-confd-monitoring',
            'ssh',
            _yang_ns.NAMESPACE_LOOKUP['tailf-confd-monitoring'],
            'ydk.models.cisco_ios_xr.tailf_confd_monitoring',
            is_config=False,
        ),
    },
    'ConfdState.Cli.Listen' : {
        'meta_info' : _MetaInfoClass('ConfdState.Cli.Listen', REFERENCE_CLASS,
            '''The transport addresses the CLI server is listening on.

In addition to the SSH addresses listen below, the CLI can
always be invoked through the daemons IPC port.

Note that other mechanisms can be put in front of the IPC
port, e.g., an OpenSSH server.  Such mechanisms are not
known to the daemon and not listed here.''',
            False, 
            [
            _MetaInfoClassMember('ssh', REFERENCE_LIST, 'Ssh', '',
                'ydk.models.cisco_ios_xr.tailf_confd_monitoring', 'ConfdState.Cli.Listen.Ssh',
                [], [],
                '''                ''',
                'ssh',
                'tailf-confd-monitoring', False, is_config=False),
            ],
            'tailf-confd-monitoring',
            'listen',
            _yang_ns.NAMESPACE_LOOKUP['tailf-confd-monitoring'],
            'ydk.models.cisco_ios_xr.tailf_confd_monitoring',
            is_config=False,
        ),
    },
    'ConfdState.Cli' : {
        'meta_info' : _MetaInfoClass('ConfdState.Cli', REFERENCE_CLASS,
            ''' ''',
            False, 
            [
            _MetaInfoClassMember('listen', REFERENCE_CLASS, 'Listen', '',
                'ydk.models.cisco_ios_xr.tailf_confd_monitoring', 'ConfdState.Cli.Listen',
                [], [],
                '''                The transport addresses the CLI server is listening on.
                
                In addition to the SSH addresses listen below, the CLI can
                always be invoked through the daemons IPC port.
                
                Note that other mechanisms can be put in front of the IPC
                port, e.g., an OpenSSH server.  Such mechanisms are not
                known to the daemon and not listed here.
                ''',
                'listen',
                'tailf-confd-monitoring', False, is_config=False),
            ],
            'tailf-confd-monitoring',
            'cli',
            _yang_ns.NAMESPACE_LOOKUP['tailf-confd-monitoring'],
            'ydk.models.cisco_ios_xr.tailf_confd_monitoring',
            is_config=False,
            is_presence=True,
        ),
    },
    'ConfdState.Webui.Listen.Tcp' : {
        'meta_info' : _MetaInfoClass('ConfdState.Webui.Listen.Tcp', REFERENCE_LIST,
            ''' ''',
            False, 
            [
            _MetaInfoClassMember('ip', REFERENCE_UNION, 'str', 'inet:ip-address',
                None, None,
                [], [],
                '''                ''',
                'ip',
                'tailf-confd-monitoring', False, [
                    _MetaInfoClassMember('ip', ATTRIBUTE, 'str', 'inet:ipv4-address',
                        None, None,
                        [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'],
                        '''                        ''',
                        'ip',
                        'tailf-confd-monitoring', False, is_config=False),
                    _MetaInfoClassMember('ip', ATTRIBUTE, 'str', 'inet:ipv6-address',
                        None, None,
                        [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'],
                        '''                        ''',
                        'ip',
                        'tailf-confd-monitoring', False, is_config=False),
                ], is_config=False),
            _MetaInfoClassMember('port', ATTRIBUTE, 'int', 'inet:port-number',
                None, None,
                [('0', '65535')], [],
                '''                ''',
                'port',
                'tailf-confd-monitoring', False, is_config=False),
            ],
            'tailf-confd-monitoring',
            'tcp',
            _yang_ns.NAMESPACE_LOOKUP['tailf-confd-monitoring'],
            'ydk.models.cisco_ios_xr.tailf_confd_monitoring',
            is_config=False,
        ),
    },
    'ConfdState.Webui.Listen.Ssl' : {
        'meta_info' : _MetaInfoClass('ConfdState.Webui.Listen.Ssl', REFERENCE_LIST,
            ''' ''',
            False, 
            [
            _MetaInfoClassMember('ip', REFERENCE_UNION, 'str', 'inet:ip-address',
                None, None,
                [], [],
                '''                ''',
                'ip',
                'tailf-confd-monitoring', False, [
                    _MetaInfoClassMember('ip', ATTRIBUTE, 'str', 'inet:ipv4-address',
                        None, None,
                        [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'],
                        '''                        ''',
                        'ip',
                        'tailf-confd-monitoring', False, is_config=False),
                    _MetaInfoClassMember('ip', ATTRIBUTE, 'str', 'inet:ipv6-address',
                        None, None,
                        [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'],
                        '''                        ''',
                        'ip',
                        'tailf-confd-monitoring', False, is_config=False),
                ], is_config=False),
            _MetaInfoClassMember('port', ATTRIBUTE, 'int', 'inet:port-number',
                None, None,
                [('0', '65535')], [],
                '''                ''',
                'port',
                'tailf-confd-monitoring', False, is_config=False),
            ],
            'tailf-confd-monitoring',
            'ssl',
            _yang_ns.NAMESPACE_LOOKUP['tailf-confd-monitoring'],
            'ydk.models.cisco_ios_xr.tailf_confd_monitoring',
            is_config=False,
        ),
    },
    'ConfdState.Webui.Listen' : {
        'meta_info' : _MetaInfoClass('ConfdState.Webui.Listen', REFERENCE_CLASS,
            '''The transport addresses the WebUI server is listening on.''',
            False, 
            [
            _MetaInfoClassMember('tcp', REFERENCE_LIST, 'Tcp', '',
                'ydk.models.cisco_ios_xr.tailf_confd_monitoring', 'ConfdState.Webui.Listen.Tcp',
                [], [],
                '''                ''',
                'tcp',
                'tailf-confd-monitoring', False, is_config=False),
            _MetaInfoClassMember('ssl', REFERENCE_LIST, 'Ssl', '',
                'ydk.models.cisco_ios_xr.tailf_confd_monitoring', 'ConfdState.Webui.Listen.Ssl',
                [], [],
                '''                ''',
                'ssl',
                'tailf-confd-monitoring', False, is_config=False),
            ],
            'tailf-confd-monitoring',
            'listen',
            _yang_ns.NAMESPACE_LOOKUP['tailf-confd-monitoring'],
            'ydk.models.cisco_ios_xr.tailf_confd_monitoring',
            is_config=False,
        ),
    },
    'ConfdState.Webui' : {
        'meta_info' : _MetaInfoClass('ConfdState.Webui', REFERENCE_CLASS,
            ''' ''',
            False, 
            [
            _MetaInfoClassMember('listen', REFERENCE_CLASS, 'Listen', '',
                'ydk.models.cisco_ios_xr.tailf_confd_monitoring', 'ConfdState.Webui.Listen',
                [], [],
                '''                The transport addresses the WebUI server is listening on.
                ''',
                'listen',
                'tailf-confd-monitoring', False, is_config=False),
            ],
            'tailf-confd-monitoring',
            'webui',
            _yang_ns.NAMESPACE_LOOKUP['tailf-confd-monitoring'],
            'ydk.models.cisco_ios_xr.tailf_confd_monitoring',
            is_config=False,
            is_presence=True,
        ),
    },
    'ConfdState.Rest.Listen.Tcp' : {
        'meta_info' : _MetaInfoClass('ConfdState.Rest.Listen.Tcp', REFERENCE_LIST,
            ''' ''',
            False, 
            [
            _MetaInfoClassMember('ip', REFERENCE_UNION, 'str', 'inet:ip-address',
                None, None,
                [], [],
                '''                ''',
                'ip',
                'tailf-confd-monitoring', False, [
                    _MetaInfoClassMember('ip', ATTRIBUTE, 'str', 'inet:ipv4-address',
                        None, None,
                        [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'],
                        '''                        ''',
                        'ip',
                        'tailf-confd-monitoring', False, is_config=False),
                    _MetaInfoClassMember('ip', ATTRIBUTE, 'str', 'inet:ipv6-address',
                        None, None,
                        [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'],
                        '''                        ''',
                        'ip',
                        'tailf-confd-monitoring', False, is_config=False),
                ], is_config=False),
            _MetaInfoClassMember('port', ATTRIBUTE, 'int', 'inet:port-number',
                None, None,
                [('0', '65535')], [],
                '''                ''',
                'port',
                'tailf-confd-monitoring', False, is_config=False),
            ],
            'tailf-confd-monitoring',
            'tcp',
            _yang_ns.NAMESPACE_LOOKUP['tailf-confd-monitoring'],
            'ydk.models.cisco_ios_xr.tailf_confd_monitoring',
            is_config=False,
        ),
    },
    'ConfdState.Rest.Listen.Ssl' : {
        'meta_info' : _MetaInfoClass('ConfdState.Rest.Listen.Ssl', REFERENCE_LIST,
            ''' ''',
            False, 
            [
            _MetaInfoClassMember('ip', REFERENCE_UNION, 'str', 'inet:ip-address',
                None, None,
                [], [],
                '''                ''',
                'ip',
                'tailf-confd-monitoring', False, [
                    _MetaInfoClassMember('ip', ATTRIBUTE, 'str', 'inet:ipv4-address',
                        None, None,
                        [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'],
                        '''                        ''',
                        'ip',
                        'tailf-confd-monitoring', False, is_config=False),
                    _MetaInfoClassMember('ip', ATTRIBUTE, 'str', 'inet:ipv6-address',
                        None, None,
                        [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'],
                        '''                        ''',
                        'ip',
                        'tailf-confd-monitoring', False, is_config=False),
                ], is_config=False),
            _MetaInfoClassMember('port', ATTRIBUTE, 'int', 'inet:port-number',
                None, None,
                [('0', '65535')], [],
                '''                ''',
                'port',
                'tailf-confd-monitoring', False, is_config=False),
            ],
            'tailf-confd-monitoring',
            'ssl',
            _yang_ns.NAMESPACE_LOOKUP['tailf-confd-monitoring'],
            'ydk.models.cisco_ios_xr.tailf_confd_monitoring',
            is_config=False,
        ),
    },
    'ConfdState.Rest.Listen' : {
        'meta_info' : _MetaInfoClass('ConfdState.Rest.Listen', REFERENCE_CLASS,
            '''The transport addresses the REST server is listening on.''',
            False, 
            [
            _MetaInfoClassMember('tcp', REFERENCE_LIST, 'Tcp', '',
                'ydk.models.cisco_ios_xr.tailf_confd_monitoring', 'ConfdState.Rest.Listen.Tcp',
                [], [],
                '''                ''',
                'tcp',
                'tailf-confd-monitoring', False, is_config=False),
            _MetaInfoClassMember('ssl', REFERENCE_LIST, 'Ssl', '',
                'ydk.models.cisco_ios_xr.tailf_confd_monitoring', 'ConfdState.Rest.Listen.Ssl',
                [], [],
                '''                ''',
                'ssl',
                'tailf-confd-monitoring', False, is_config=False),
            ],
            'tailf-confd-monitoring',
            'listen',
            _yang_ns.NAMESPACE_LOOKUP['tailf-confd-monitoring'],
            'ydk.models.cisco_ios_xr.tailf_confd_monitoring',
            is_config=False,
        ),
    },
    'ConfdState.Rest' : {
        'meta_info' : _MetaInfoClass('ConfdState.Rest', REFERENCE_CLASS,
            ''' ''',
            False, 
            [
            _MetaInfoClassMember('listen', REFERENCE_CLASS, 'Listen', '',
                'ydk.models.cisco_ios_xr.tailf_confd_monitoring', 'ConfdState.Rest.Listen',
                [], [],
                '''                The transport addresses the REST server is listening on.
                ''',
                'listen',
                'tailf-confd-monitoring', False, is_config=False),
            ],
            'tailf-confd-monitoring',
            'rest',
            _yang_ns.NAMESPACE_LOOKUP['tailf-confd-monitoring'],
            'ydk.models.cisco_ios_xr.tailf_confd_monitoring',
            is_config=False,
            is_presence=True,
        ),
    },
    'ConfdState.Snmp.Listen.Udp' : {
        'meta_info' : _MetaInfoClass('ConfdState.Snmp.Listen.Udp', REFERENCE_LIST,
            ''' ''',
            False, 
            [
            _MetaInfoClassMember('ip', REFERENCE_UNION, 'str', 'inet:ip-address',
                None, None,
                [], [],
                '''                ''',
                'ip',
                'tailf-confd-monitoring', False, [
                    _MetaInfoClassMember('ip', ATTRIBUTE, 'str', 'inet:ipv4-address',
                        None, None,
                        [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'],
                        '''                        ''',
                        'ip',
                        'tailf-confd-monitoring', False, is_config=False),
                    _MetaInfoClassMember('ip', ATTRIBUTE, 'str', 'inet:ipv6-address',
                        None, None,
                        [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'],
                        '''                        ''',
                        'ip',
                        'tailf-confd-monitoring', False, is_config=False),
                ], is_config=False),
            _MetaInfoClassMember('port', ATTRIBUTE, 'int', 'inet:port-number',
                None, None,
                [('0', '65535')], [],
                '''                ''',
                'port',
                'tailf-confd-monitoring', False, is_config=False),
            ],
            'tailf-confd-monitoring',
            'udp',
            _yang_ns.NAMESPACE_LOOKUP['tailf-confd-monitoring'],
            'ydk.models.cisco_ios_xr.tailf_confd_monitoring',
            is_config=False,
        ),
    },
    'ConfdState.Snmp.Listen' : {
        'meta_info' : _MetaInfoClass('ConfdState.Snmp.Listen', REFERENCE_CLASS,
            '''The transport addresses the SNMP agent is listening on.''',
            False, 
            [
            _MetaInfoClassMember('udp', REFERENCE_LIST, 'Udp', '',
                'ydk.models.cisco_ios_xr.tailf_confd_monitoring', 'ConfdState.Snmp.Listen.Udp',
                [], [],
                '''                ''',
                'udp',
                'tailf-confd-monitoring', False, is_config=False),
            ],
            'tailf-confd-monitoring',
            'listen',
            _yang_ns.NAMESPACE_LOOKUP['tailf-confd-monitoring'],
            'ydk.models.cisco_ios_xr.tailf_confd_monitoring',
            is_config=False,
        ),
    },
    'ConfdState.Snmp.Version' : {
        'meta_info' : _MetaInfoClass('ConfdState.Snmp.Version', REFERENCE_CLASS,
            '''SNMP version used by the engine.''',
            False, 
            [
            _MetaInfoClassMember('v1', ATTRIBUTE, 'Empty', 'empty',
                None, None,
                [], [],
                '''                ''',
                'v1',
                'tailf-confd-monitoring', False, is_config=False),
            _MetaInfoClassMember('v2c', ATTRIBUTE, 'Empty', 'empty',
                None, None,
                [], [],
                '''                ''',
                'v2c',
                'tailf-confd-monitoring', False, is_config=False),
            _MetaInfoClassMember('v3', ATTRIBUTE, 'Empty', 'empty',
                None, None,
                [], [],
                '''                ''',
                'v3',
                'tailf-confd-monitoring', False, is_config=False),
            ],
            'tailf-confd-monitoring',
            'version',
            _yang_ns.NAMESPACE_LOOKUP['tailf-confd-monitoring'],
            'ydk.models.cisco_ios_xr.tailf_confd_monitoring',
            is_config=False,
        ),
    },
    'ConfdState.Snmp' : {
        'meta_info' : _MetaInfoClass('ConfdState.Snmp', REFERENCE_CLASS,
            ''' ''',
            False, 
            [
            _MetaInfoClassMember('listen', REFERENCE_CLASS, 'Listen', '',
                'ydk.models.cisco_ios_xr.tailf_confd_monitoring', 'ConfdState.Snmp.Listen',
                [], [],
                '''                The transport addresses the SNMP agent is listening on.
                ''',
                'listen',
                'tailf-confd-monitoring', False, is_config=False),
            _MetaInfoClassMember('mib', REFERENCE_LEAFLIST, 'str', 'string',
                None, None,
                [], [],
                '''                MIBs loaded by the SNMP agent.
                ''',
                'mib',
                'tailf-confd-monitoring', False, is_config=False),
            _MetaInfoClassMember('version', REFERENCE_CLASS, 'Version', '',
                'ydk.models.cisco_ios_xr.tailf_confd_monitoring', 'ConfdState.Snmp.Version',
                [], [],
                '''                SNMP version used by the engine.
                ''',
                'version',
                'tailf-confd-monitoring', False, is_config=False),
            _MetaInfoClassMember('engine-id', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [b'([0-9a-fA-F]){2}(:([0-9a-fA-F]){2}){4,31}'],
                '''                The local Engine ID specified as a list of colon-specified
                hexadecimal octets e.g. '4F:4C:41:71'.
                ''',
                'engine_id',
                'tailf-confd-monitoring', False, is_config=False),
            ],
            'tailf-confd-monitoring',
            'snmp',
            _yang_ns.NAMESPACE_LOOKUP['tailf-confd-monitoring'],
            'ydk.models.cisco_ios_xr.tailf_confd_monitoring',
            is_config=False,
            is_presence=True,
        ),
    },
    'ConfdState.Internal.Callpoints.Callpoint.Daemon.Error' : _MetaInfoEnum('Error',
        'ydk.models.cisco_ios_xr.tailf_confd_monitoring', 'ConfdState.Internal.Callpoints.Callpoint.Daemon.Error',
        '''If this leaf exists, there is a problem
with the daemon registration.''',
        {
            'PENDING':'PENDING',
        }, 'tailf-common-monitoring', _yang_ns.NAMESPACE_LOOKUP['tailf-common-monitoring']),
    'ConfdState.Internal.Callpoints.Callpoint.Daemon' : {
        'meta_info' : _MetaInfoClass('ConfdState.Internal.Callpoints.Callpoint.Daemon', REFERENCE_CLASS,
            ''' ''',
            False, 
            [
            _MetaInfoClassMember('id', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('0', '4294967295')], [],
                '''                The numerical id assigned to the application daemon
                that has registered for a callpoint.
                ''',
                'id',
                'tailf-confd-monitoring', False, is_config=False),
            _MetaInfoClassMember('name', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                The name of the application daemon that has
                registered for a callpoint.
                ''',
                'name',
                'tailf-confd-monitoring', False, is_config=False),
            _MetaInfoClassMember('error', REFERENCE_ENUM_CLASS, 'Error', 'enumeration',
                'ydk.models.cisco_ios_xr.tailf_confd_monitoring', 'ConfdState.Internal.Callpoints.Callpoint.Daemon.Error',
                [], [],
                '''                If this leaf exists, there is a problem
                with the daemon registration.
                ''',
                'error',
                'tailf-confd-monitoring', False, is_config=False),
            ],
            'tailf-confd-monitoring',
            'daemon',
            _yang_ns.NAMESPACE_LOOKUP['tailf-confd-monitoring'],
            'ydk.models.cisco_ios_xr.tailf_confd_monitoring',
            is_config=False,
        ),
    },
    'ConfdState.Internal.Callpoints.Callpoint.Range.Daemon.Error' : _MetaInfoEnum('Error',
        'ydk.models.cisco_ios_xr.tailf_confd_monitoring', 'ConfdState.Internal.Callpoints.Callpoint.Range.Daemon.Error',
        '''If this leaf exists, there is a problem
with the daemon registration.''',
        {
            'PENDING':'PENDING',
        }, 'tailf-common-monitoring', _yang_ns.NAMESPACE_LOOKUP['tailf-common-monitoring']),
    'ConfdState.Internal.Callpoints.Callpoint.Range.Daemon' : {
        'meta_info' : _MetaInfoClass('ConfdState.Internal.Callpoints.Callpoint.Range.Daemon', REFERENCE_CLASS,
            ''' ''',
            False, 
            [
            _MetaInfoClassMember('id', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('0', '4294967295')], [],
                '''                The numerical id assigned to the application daemon
                that has registered for a callpoint.
                ''',
                'id',
                'tailf-confd-monitoring', False, is_config=False),
            _MetaInfoClassMember('name', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                The name of the application daemon that has
                registered for a callpoint.
                ''',
                'name',
                'tailf-confd-monitoring', False, is_config=False),
            _MetaInfoClassMember('error', REFERENCE_ENUM_CLASS, 'Error', 'enumeration',
                'ydk.models.cisco_ios_xr.tailf_confd_monitoring', 'ConfdState.Internal.Callpoints.Callpoint.Range.Daemon.Error',
                [], [],
                '''                If this leaf exists, there is a problem
                with the daemon registration.
                ''',
                'error',
                'tailf-confd-monitoring', False, is_config=False),
            ],
            'tailf-confd-monitoring',
            'daemon',
            _yang_ns.NAMESPACE_LOOKUP['tailf-confd-monitoring'],
            'ydk.models.cisco_ios_xr.tailf_confd_monitoring',
            is_config=False,
        ),
    },
    'ConfdState.Internal.Callpoints.Callpoint.Range' : {
        'meta_info' : _MetaInfoClass('ConfdState.Internal.Callpoints.Callpoint.Range', REFERENCE_LIST,
            ''' ''',
            False, 
            [
            _MetaInfoClassMember('lower', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                The space-separated set of keys that defines the lower
                endpoint of the range for a non-default registration.
                ''',
                'lower',
                'tailf-confd-monitoring', False, is_config=False),
            _MetaInfoClassMember('upper', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                The space-separated set of keys that defines the upper
                endpoint of the range for a non-default registration.
                ''',
                'upper',
                'tailf-confd-monitoring', False, is_config=False),
            _MetaInfoClassMember('default', ATTRIBUTE, 'Empty', 'empty',
                None, None,
                [], [],
                '''                If this leaf exists, this is a default registration
                - in this case 'lower' and 'upper' do not exist.
                ''',
                'default',
                'tailf-confd-monitoring', False, is_config=False),
            _MetaInfoClassMember('daemon', REFERENCE_CLASS, 'Daemon', '',
                'ydk.models.cisco_ios_xr.tailf_confd_monitoring', 'ConfdState.Internal.Callpoints.Callpoint.Range.Daemon',
                [], [],
                '''                ''',
                'daemon',
                'tailf-confd-monitoring', False, is_config=False),
            ],
            'tailf-confd-monitoring',
            'range',
            _yang_ns.NAMESPACE_LOOKUP['tailf-confd-monitoring'],
            'ydk.models.cisco_ios_xr.tailf_confd_monitoring',
            is_config=False,
        ),
    },
    'ConfdState.Internal.Callpoints.Callpoint.Error' : _MetaInfoEnum('Error',
        'ydk.models.cisco_ios_xr.tailf_confd_monitoring', 'ConfdState.Internal.Callpoints.Callpoint.Error',
        '''If this leaf exists, there is a problem
with the callpoint registration.''',
        {
            'NOT-REGISTERED':'NOT_REGISTERED',
            'UNKNOWN':'UNKNOWN',
        }, 'tailf-common-monitoring', _yang_ns.NAMESPACE_LOOKUP['tailf-common-monitoring']),
    'ConfdState.Internal.Callpoints.Callpoint' : {
        'meta_info' : _MetaInfoClass('ConfdState.Internal.Callpoints.Callpoint', REFERENCE_LIST,
            ''' ''',
            False, 
            [
            _MetaInfoClassMember('id', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                Callpoint id
                ''',
                'id',
                'tailf-confd-monitoring', True, is_config=False),
            _MetaInfoClassMember('daemon', REFERENCE_CLASS, 'Daemon', '',
                'ydk.models.cisco_ios_xr.tailf_confd_monitoring', 'ConfdState.Internal.Callpoints.Callpoint.Daemon',
                [], [],
                '''                ''',
                'daemon',
                'tailf-confd-monitoring', False, is_config=False),
            _MetaInfoClassMember('path', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                The path of the list that a range registration
                pertains to.
                ''',
                'path',
                'tailf-confd-monitoring', False, is_config=False),
            _MetaInfoClassMember('range', REFERENCE_LIST, 'Range', '',
                'ydk.models.cisco_ios_xr.tailf_confd_monitoring', 'ConfdState.Internal.Callpoints.Callpoint.Range',
                [], [],
                '''                ''',
                'range',
                'tailf-confd-monitoring', False, is_config=False),
            _MetaInfoClassMember('file', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                The pathname of the shared object implementing the type
                for a typepoint.
                ''',
                'file',
                'tailf-confd-monitoring', False, is_config=False),
            _MetaInfoClassMember('error', REFERENCE_ENUM_CLASS, 'Error', 'enumeration',
                'ydk.models.cisco_ios_xr.tailf_confd_monitoring', 'ConfdState.Internal.Callpoints.Callpoint.Error',
                [], [],
                '''                If this leaf exists, there is a problem
                with the callpoint registration.
                ''',
                'error',
                'tailf-confd-monitoring', False, is_config=False),
            ],
            'tailf-confd-monitoring',
            'callpoint',
            _yang_ns.NAMESPACE_LOOKUP['tailf-confd-monitoring'],
            'ydk.models.cisco_ios_xr.tailf_confd_monitoring',
            is_config=False,
        ),
    },
    'ConfdState.Internal.Callpoints.Validationpoint.Daemon.Error' : _MetaInfoEnum('Error',
        'ydk.models.cisco_ios_xr.tailf_confd_monitoring', 'ConfdState.Internal.Callpoints.Validationpoint.Daemon.Error',
        '''If this leaf exists, there is a problem
with the daemon registration.''',
        {
            'PENDING':'PENDING',
        }, 'tailf-common-monitoring', _yang_ns.NAMESPACE_LOOKUP['tailf-common-monitoring']),
    'ConfdState.Internal.Callpoints.Validationpoint.Daemon' : {
        'meta_info' : _MetaInfoClass('ConfdState.Internal.Callpoints.Validationpoint.Daemon', REFERENCE_CLASS,
            ''' ''',
            False, 
            [
            _MetaInfoClassMember('id', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('0', '4294967295')], [],
                '''                The numerical id assigned to the application daemon
                that has registered for a callpoint.
                ''',
                'id',
                'tailf-confd-monitoring', False, is_config=False),
            _MetaInfoClassMember('name', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                The name of the application daemon that has
                registered for a callpoint.
                ''',
                'name',
                'tailf-confd-monitoring', False, is_config=False),
            _MetaInfoClassMember('error', REFERENCE_ENUM_CLASS, 'Error', 'enumeration',
                'ydk.models.cisco_ios_xr.tailf_confd_monitoring', 'ConfdState.Internal.Callpoints.Validationpoint.Daemon.Error',
                [], [],
                '''                If this leaf exists, there is a problem
                with the daemon registration.
                ''',
                'error',
                'tailf-confd-monitoring', False, is_config=False),
            ],
            'tailf-confd-monitoring',
            'daemon',
            _yang_ns.NAMESPACE_LOOKUP['tailf-confd-monitoring'],
            'ydk.models.cisco_ios_xr.tailf_confd_monitoring',
            is_config=False,
        ),
    },
    'ConfdState.Internal.Callpoints.Validationpoint.Range.Daemon.Error' : _MetaInfoEnum('Error',
        'ydk.models.cisco_ios_xr.tailf_confd_monitoring', 'ConfdState.Internal.Callpoints.Validationpoint.Range.Daemon.Error',
        '''If this leaf exists, there is a problem
with the daemon registration.''',
        {
            'PENDING':'PENDING',
        }, 'tailf-common-monitoring', _yang_ns.NAMESPACE_LOOKUP['tailf-common-monitoring']),
    'ConfdState.Internal.Callpoints.Validationpoint.Range.Daemon' : {
        'meta_info' : _MetaInfoClass('ConfdState.Internal.Callpoints.Validationpoint.Range.Daemon', REFERENCE_CLASS,
            ''' ''',
            False, 
            [
            _MetaInfoClassMember('id', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('0', '4294967295')], [],
                '''                The numerical id assigned to the application daemon
                that has registered for a callpoint.
                ''',
                'id',
                'tailf-confd-monitoring', False, is_config=False),
            _MetaInfoClassMember('name', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                The name of the application daemon that has
                registered for a callpoint.
                ''',
                'name',
                'tailf-confd-monitoring', False, is_config=False),
            _MetaInfoClassMember('error', REFERENCE_ENUM_CLASS, 'Error', 'enumeration',
                'ydk.models.cisco_ios_xr.tailf_confd_monitoring', 'ConfdState.Internal.Callpoints.Validationpoint.Range.Daemon.Error',
                [], [],
                '''                If this leaf exists, there is a problem
                with the daemon registration.
                ''',
                'error',
                'tailf-confd-monitoring', False, is_config=False),
            ],
            'tailf-confd-monitoring',
            'daemon',
            _yang_ns.NAMESPACE_LOOKUP['tailf-confd-monitoring'],
            'ydk.models.cisco_ios_xr.tailf_confd_monitoring',
            is_config=False,
        ),
    },
    'ConfdState.Internal.Callpoints.Validationpoint.Range' : {
        'meta_info' : _MetaInfoClass('ConfdState.Internal.Callpoints.Validationpoint.Range', REFERENCE_LIST,
            ''' ''',
            False, 
            [
            _MetaInfoClassMember('lower', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                The space-separated set of keys that defines the lower
                endpoint of the range for a non-default registration.
                ''',
                'lower',
                'tailf-confd-monitoring', False, is_config=False),
            _MetaInfoClassMember('upper', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                The space-separated set of keys that defines the upper
                endpoint of the range for a non-default registration.
                ''',
                'upper',
                'tailf-confd-monitoring', False, is_config=False),
            _MetaInfoClassMember('default', ATTRIBUTE, 'Empty', 'empty',
                None, None,
                [], [],
                '''                If this leaf exists, this is a default registration
                - in this case 'lower' and 'upper' do not exist.
                ''',
                'default',
                'tailf-confd-monitoring', False, is_config=False),
            _MetaInfoClassMember('daemon', REFERENCE_CLASS, 'Daemon', '',
                'ydk.models.cisco_ios_xr.tailf_confd_monitoring', 'ConfdState.Internal.Callpoints.Validationpoint.Range.Daemon',
                [], [],
                '''                ''',
                'daemon',
                'tailf-confd-monitoring', False, is_config=False),
            ],
            'tailf-confd-monitoring',
            'range',
            _yang_ns.NAMESPACE_LOOKUP['tailf-confd-monitoring'],
            'ydk.models.cisco_ios_xr.tailf_confd_monitoring',
            is_config=False,
        ),
    },
    'ConfdState.Internal.Callpoints.Validationpoint.Error' : _MetaInfoEnum('Error',
        'ydk.models.cisco_ios_xr.tailf_confd_monitoring', 'ConfdState.Internal.Callpoints.Validationpoint.Error',
        '''If this leaf exists, there is a problem
with the callpoint registration.''',
        {
            'NOT-REGISTERED':'NOT_REGISTERED',
            'UNKNOWN':'UNKNOWN',
        }, 'tailf-common-monitoring', _yang_ns.NAMESPACE_LOOKUP['tailf-common-monitoring']),
    'ConfdState.Internal.Callpoints.Validationpoint' : {
        'meta_info' : _MetaInfoClass('ConfdState.Internal.Callpoints.Validationpoint', REFERENCE_LIST,
            ''' ''',
            False, 
            [
            _MetaInfoClassMember('id', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                Callpoint id
                ''',
                'id',
                'tailf-confd-monitoring', True, is_config=False),
            _MetaInfoClassMember('daemon', REFERENCE_CLASS, 'Daemon', '',
                'ydk.models.cisco_ios_xr.tailf_confd_monitoring', 'ConfdState.Internal.Callpoints.Validationpoint.Daemon',
                [], [],
                '''                ''',
                'daemon',
                'tailf-confd-monitoring', False, is_config=False),
            _MetaInfoClassMember('path', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                The path of the list that a range registration
                pertains to.
                ''',
                'path',
                'tailf-confd-monitoring', False, is_config=False),
            _MetaInfoClassMember('range', REFERENCE_LIST, 'Range', '',
                'ydk.models.cisco_ios_xr.tailf_confd_monitoring', 'ConfdState.Internal.Callpoints.Validationpoint.Range',
                [], [],
                '''                ''',
                'range',
                'tailf-confd-monitoring', False, is_config=False),
            _MetaInfoClassMember('file', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                The pathname of the shared object implementing the type
                for a typepoint.
                ''',
                'file',
                'tailf-confd-monitoring', False, is_config=False),
            _MetaInfoClassMember('error', REFERENCE_ENUM_CLASS, 'Error', 'enumeration',
                'ydk.models.cisco_ios_xr.tailf_confd_monitoring', 'ConfdState.Internal.Callpoints.Validationpoint.Error',
                [], [],
                '''                If this leaf exists, there is a problem
                with the callpoint registration.
                ''',
                'error',
                'tailf-confd-monitoring', False, is_config=False),
            ],
            'tailf-confd-monitoring',
            'validationpoint',
            _yang_ns.NAMESPACE_LOOKUP['tailf-confd-monitoring'],
            'ydk.models.cisco_ios_xr.tailf_confd_monitoring',
            is_config=False,
        ),
    },
    'ConfdState.Internal.Callpoints.Actionpoint.Daemon.Error' : _MetaInfoEnum('Error',
        'ydk.models.cisco_ios_xr.tailf_confd_monitoring', 'ConfdState.Internal.Callpoints.Actionpoint.Daemon.Error',
        '''If this leaf exists, there is a problem
with the daemon registration.''',
        {
            'PENDING':'PENDING',
        }, 'tailf-common-monitoring', _yang_ns.NAMESPACE_LOOKUP['tailf-common-monitoring']),
    'ConfdState.Internal.Callpoints.Actionpoint.Daemon' : {
        'meta_info' : _MetaInfoClass('ConfdState.Internal.Callpoints.Actionpoint.Daemon', REFERENCE_CLASS,
            ''' ''',
            False, 
            [
            _MetaInfoClassMember('id', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('0', '4294967295')], [],
                '''                The numerical id assigned to the application daemon
                that has registered for a callpoint.
                ''',
                'id',
                'tailf-confd-monitoring', False, is_config=False),
            _MetaInfoClassMember('name', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                The name of the application daemon that has
                registered for a callpoint.
                ''',
                'name',
                'tailf-confd-monitoring', False, is_config=False),
            _MetaInfoClassMember('error', REFERENCE_ENUM_CLASS, 'Error', 'enumeration',
                'ydk.models.cisco_ios_xr.tailf_confd_monitoring', 'ConfdState.Internal.Callpoints.Actionpoint.Daemon.Error',
                [], [],
                '''                If this leaf exists, there is a problem
                with the daemon registration.
                ''',
                'error',
                'tailf-confd-monitoring', False, is_config=False),
            ],
            'tailf-confd-monitoring',
            'daemon',
            _yang_ns.NAMESPACE_LOOKUP['tailf-confd-monitoring'],
            'ydk.models.cisco_ios_xr.tailf_confd_monitoring',
            is_config=False,
        ),
    },
    'ConfdState.Internal.Callpoints.Actionpoint.Range.Daemon.Error' : _MetaInfoEnum('Error',
        'ydk.models.cisco_ios_xr.tailf_confd_monitoring', 'ConfdState.Internal.Callpoints.Actionpoint.Range.Daemon.Error',
        '''If this leaf exists, there is a problem
with the daemon registration.''',
        {
            'PENDING':'PENDING',
        }, 'tailf-common-monitoring', _yang_ns.NAMESPACE_LOOKUP['tailf-common-monitoring']),
    'ConfdState.Internal.Callpoints.Actionpoint.Range.Daemon' : {
        'meta_info' : _MetaInfoClass('ConfdState.Internal.Callpoints.Actionpoint.Range.Daemon', REFERENCE_CLASS,
            ''' ''',
            False, 
            [
            _MetaInfoClassMember('id', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('0', '4294967295')], [],
                '''                The numerical id assigned to the application daemon
                that has registered for a callpoint.
                ''',
                'id',
                'tailf-confd-monitoring', False, is_config=False),
            _MetaInfoClassMember('name', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                The name of the application daemon that has
                registered for a callpoint.
                ''',
                'name',
                'tailf-confd-monitoring', False, is_config=False),
            _MetaInfoClassMember('error', REFERENCE_ENUM_CLASS, 'Error', 'enumeration',
                'ydk.models.cisco_ios_xr.tailf_confd_monitoring', 'ConfdState.Internal.Callpoints.Actionpoint.Range.Daemon.Error',
                [], [],
                '''                If this leaf exists, there is a problem
                with the daemon registration.
                ''',
                'error',
                'tailf-confd-monitoring', False, is_config=False),
            ],
            'tailf-confd-monitoring',
            'daemon',
            _yang_ns.NAMESPACE_LOOKUP['tailf-confd-monitoring'],
            'ydk.models.cisco_ios_xr.tailf_confd_monitoring',
            is_config=False,
        ),
    },
    'ConfdState.Internal.Callpoints.Actionpoint.Range' : {
        'meta_info' : _MetaInfoClass('ConfdState.Internal.Callpoints.Actionpoint.Range', REFERENCE_LIST,
            ''' ''',
            False, 
            [
            _MetaInfoClassMember('lower', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                The space-separated set of keys that defines the lower
                endpoint of the range for a non-default registration.
                ''',
                'lower',
                'tailf-confd-monitoring', False, is_config=False),
            _MetaInfoClassMember('upper', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                The space-separated set of keys that defines the upper
                endpoint of the range for a non-default registration.
                ''',
                'upper',
                'tailf-confd-monitoring', False, is_config=False),
            _MetaInfoClassMember('default', ATTRIBUTE, 'Empty', 'empty',
                None, None,
                [], [],
                '''                If this leaf exists, this is a default registration
                - in this case 'lower' and 'upper' do not exist.
                ''',
                'default',
                'tailf-confd-monitoring', False, is_config=False),
            _MetaInfoClassMember('daemon', REFERENCE_CLASS, 'Daemon', '',
                'ydk.models.cisco_ios_xr.tailf_confd_monitoring', 'ConfdState.Internal.Callpoints.Actionpoint.Range.Daemon',
                [], [],
                '''                ''',
                'daemon',
                'tailf-confd-monitoring', False, is_config=False),
            ],
            'tailf-confd-monitoring',
            'range',
            _yang_ns.NAMESPACE_LOOKUP['tailf-confd-monitoring'],
            'ydk.models.cisco_ios_xr.tailf_confd_monitoring',
            is_config=False,
        ),
    },
    'ConfdState.Internal.Callpoints.Actionpoint.Error' : _MetaInfoEnum('Error',
        'ydk.models.cisco_ios_xr.tailf_confd_monitoring', 'ConfdState.Internal.Callpoints.Actionpoint.Error',
        '''If this leaf exists, there is a problem
with the callpoint registration.''',
        {
            'NOT-REGISTERED':'NOT_REGISTERED',
            'UNKNOWN':'UNKNOWN',
        }, 'tailf-common-monitoring', _yang_ns.NAMESPACE_LOOKUP['tailf-common-monitoring']),
    'ConfdState.Internal.Callpoints.Actionpoint' : {
        'meta_info' : _MetaInfoClass('ConfdState.Internal.Callpoints.Actionpoint', REFERENCE_LIST,
            ''' ''',
            False, 
            [
            _MetaInfoClassMember('id', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                Callpoint id
                ''',
                'id',
                'tailf-confd-monitoring', True, is_config=False),
            _MetaInfoClassMember('daemon', REFERENCE_CLASS, 'Daemon', '',
                'ydk.models.cisco_ios_xr.tailf_confd_monitoring', 'ConfdState.Internal.Callpoints.Actionpoint.Daemon',
                [], [],
                '''                ''',
                'daemon',
                'tailf-confd-monitoring', False, is_config=False),
            _MetaInfoClassMember('path', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                The path of the list that a range registration
                pertains to.
                ''',
                'path',
                'tailf-confd-monitoring', False, is_config=False),
            _MetaInfoClassMember('range', REFERENCE_LIST, 'Range', '',
                'ydk.models.cisco_ios_xr.tailf_confd_monitoring', 'ConfdState.Internal.Callpoints.Actionpoint.Range',
                [], [],
                '''                ''',
                'range',
                'tailf-confd-monitoring', False, is_config=False),
            _MetaInfoClassMember('file', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                The pathname of the shared object implementing the type
                for a typepoint.
                ''',
                'file',
                'tailf-confd-monitoring', False, is_config=False),
            _MetaInfoClassMember('error', REFERENCE_ENUM_CLASS, 'Error', 'enumeration',
                'ydk.models.cisco_ios_xr.tailf_confd_monitoring', 'ConfdState.Internal.Callpoints.Actionpoint.Error',
                [], [],
                '''                If this leaf exists, there is a problem
                with the callpoint registration.
                ''',
                'error',
                'tailf-confd-monitoring', False, is_config=False),
            ],
            'tailf-confd-monitoring',
            'actionpoint',
            _yang_ns.NAMESPACE_LOOKUP['tailf-confd-monitoring'],
            'ydk.models.cisco_ios_xr.tailf_confd_monitoring',
            is_config=False,
        ),
    },
    'ConfdState.Internal.Callpoints.SnmpInformCallback.Daemon.Error' : _MetaInfoEnum('Error',
        'ydk.models.cisco_ios_xr.tailf_confd_monitoring', 'ConfdState.Internal.Callpoints.SnmpInformCallback.Daemon.Error',
        '''If this leaf exists, there is a problem
with the daemon registration.''',
        {
            'PENDING':'PENDING',
        }, 'tailf-common-monitoring', _yang_ns.NAMESPACE_LOOKUP['tailf-common-monitoring']),
    'ConfdState.Internal.Callpoints.SnmpInformCallback.Daemon' : {
        'meta_info' : _MetaInfoClass('ConfdState.Internal.Callpoints.SnmpInformCallback.Daemon', REFERENCE_CLASS,
            ''' ''',
            False, 
            [
            _MetaInfoClassMember('id', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('0', '4294967295')], [],
                '''                The numerical id assigned to the application daemon
                that has registered for a callpoint.
                ''',
                'id',
                'tailf-confd-monitoring', False, is_config=False),
            _MetaInfoClassMember('name', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                The name of the application daemon that has
                registered for a callpoint.
                ''',
                'name',
                'tailf-confd-monitoring', False, is_config=False),
            _MetaInfoClassMember('error', REFERENCE_ENUM_CLASS, 'Error', 'enumeration',
                'ydk.models.cisco_ios_xr.tailf_confd_monitoring', 'ConfdState.Internal.Callpoints.SnmpInformCallback.Daemon.Error',
                [], [],
                '''                If this leaf exists, there is a problem
                with the daemon registration.
                ''',
                'error',
                'tailf-confd-monitoring', False, is_config=False),
            ],
            'tailf-confd-monitoring',
            'daemon',
            _yang_ns.NAMESPACE_LOOKUP['tailf-confd-monitoring'],
            'ydk.models.cisco_ios_xr.tailf_confd_monitoring',
            is_config=False,
        ),
    },
    'ConfdState.Internal.Callpoints.SnmpInformCallback.Range.Daemon.Error' : _MetaInfoEnum('Error',
        'ydk.models.cisco_ios_xr.tailf_confd_monitoring', 'ConfdState.Internal.Callpoints.SnmpInformCallback.Range.Daemon.Error',
        '''If this leaf exists, there is a problem
with the daemon registration.''',
        {
            'PENDING':'PENDING',
        }, 'tailf-common-monitoring', _yang_ns.NAMESPACE_LOOKUP['tailf-common-monitoring']),
    'ConfdState.Internal.Callpoints.SnmpInformCallback.Range.Daemon' : {
        'meta_info' : _MetaInfoClass('ConfdState.Internal.Callpoints.SnmpInformCallback.Range.Daemon', REFERENCE_CLASS,
            ''' ''',
            False, 
            [
            _MetaInfoClassMember('id', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('0', '4294967295')], [],
                '''                The numerical id assigned to the application daemon
                that has registered for a callpoint.
                ''',
                'id',
                'tailf-confd-monitoring', False, is_config=False),
            _MetaInfoClassMember('name', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                The name of the application daemon that has
                registered for a callpoint.
                ''',
                'name',
                'tailf-confd-monitoring', False, is_config=False),
            _MetaInfoClassMember('error', REFERENCE_ENUM_CLASS, 'Error', 'enumeration',
                'ydk.models.cisco_ios_xr.tailf_confd_monitoring', 'ConfdState.Internal.Callpoints.SnmpInformCallback.Range.Daemon.Error',
                [], [],
                '''                If this leaf exists, there is a problem
                with the daemon registration.
                ''',
                'error',
                'tailf-confd-monitoring', False, is_config=False),
            ],
            'tailf-confd-monitoring',
            'daemon',
            _yang_ns.NAMESPACE_LOOKUP['tailf-confd-monitoring'],
            'ydk.models.cisco_ios_xr.tailf_confd_monitoring',
            is_config=False,
        ),
    },
    'ConfdState.Internal.Callpoints.SnmpInformCallback.Range' : {
        'meta_info' : _MetaInfoClass('ConfdState.Internal.Callpoints.SnmpInformCallback.Range', REFERENCE_LIST,
            ''' ''',
            False, 
            [
            _MetaInfoClassMember('lower', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                The space-separated set of keys that defines the lower
                endpoint of the range for a non-default registration.
                ''',
                'lower',
                'tailf-confd-monitoring', False, is_config=False),
            _MetaInfoClassMember('upper', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                The space-separated set of keys that defines the upper
                endpoint of the range for a non-default registration.
                ''',
                'upper',
                'tailf-confd-monitoring', False, is_config=False),
            _MetaInfoClassMember('default', ATTRIBUTE, 'Empty', 'empty',
                None, None,
                [], [],
                '''                If this leaf exists, this is a default registration
                - in this case 'lower' and 'upper' do not exist.
                ''',
                'default',
                'tailf-confd-monitoring', False, is_config=False),
            _MetaInfoClassMember('daemon', REFERENCE_CLASS, 'Daemon', '',
                'ydk.models.cisco_ios_xr.tailf_confd_monitoring', 'ConfdState.Internal.Callpoints.SnmpInformCallback.Range.Daemon',
                [], [],
                '''                ''',
                'daemon',
                'tailf-confd-monitoring', False, is_config=False),
            ],
            'tailf-confd-monitoring',
            'range',
            _yang_ns.NAMESPACE_LOOKUP['tailf-confd-monitoring'],
            'ydk.models.cisco_ios_xr.tailf_confd_monitoring',
            is_config=False,
        ),
    },
    'ConfdState.Internal.Callpoints.SnmpInformCallback.Error' : _MetaInfoEnum('Error',
        'ydk.models.cisco_ios_xr.tailf_confd_monitoring', 'ConfdState.Internal.Callpoints.SnmpInformCallback.Error',
        '''If this leaf exists, there is a problem
with the callpoint registration.''',
        {
            'NOT-REGISTERED':'NOT_REGISTERED',
            'UNKNOWN':'UNKNOWN',
        }, 'tailf-common-monitoring', _yang_ns.NAMESPACE_LOOKUP['tailf-common-monitoring']),
    'ConfdState.Internal.Callpoints.SnmpInformCallback' : {
        'meta_info' : _MetaInfoClass('ConfdState.Internal.Callpoints.SnmpInformCallback', REFERENCE_LIST,
            ''' ''',
            False, 
            [
            _MetaInfoClassMember('id', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                Callpoint id
                ''',
                'id',
                'tailf-confd-monitoring', True, is_config=False),
            _MetaInfoClassMember('daemon', REFERENCE_CLASS, 'Daemon', '',
                'ydk.models.cisco_ios_xr.tailf_confd_monitoring', 'ConfdState.Internal.Callpoints.SnmpInformCallback.Daemon',
                [], [],
                '''                ''',
                'daemon',
                'tailf-confd-monitoring', False, is_config=False),
            _MetaInfoClassMember('path', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                The path of the list that a range registration
                pertains to.
                ''',
                'path',
                'tailf-confd-monitoring', False, is_config=False),
            _MetaInfoClassMember('range', REFERENCE_LIST, 'Range', '',
                'ydk.models.cisco_ios_xr.tailf_confd_monitoring', 'ConfdState.Internal.Callpoints.SnmpInformCallback.Range',
                [], [],
                '''                ''',
                'range',
                'tailf-confd-monitoring', False, is_config=False),
            _MetaInfoClassMember('file', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                The pathname of the shared object implementing the type
                for a typepoint.
                ''',
                'file',
                'tailf-confd-monitoring', False, is_config=False),
            _MetaInfoClassMember('error', REFERENCE_ENUM_CLASS, 'Error', 'enumeration',
                'ydk.models.cisco_ios_xr.tailf_confd_monitoring', 'ConfdState.Internal.Callpoints.SnmpInformCallback.Error',
                [], [],
                '''                If this leaf exists, there is a problem
                with the callpoint registration.
                ''',
                'error',
                'tailf-confd-monitoring', False, is_config=False),
            ],
            'tailf-confd-monitoring',
            'snmp-inform-callback',
            _yang_ns.NAMESPACE_LOOKUP['tailf-confd-monitoring'],
            'ydk.models.cisco_ios_xr.tailf_confd_monitoring',
            is_config=False,
        ),
    },
    'ConfdState.Internal.Callpoints.SnmpNotificationSubscription.Daemon.Error' : _MetaInfoEnum('Error',
        'ydk.models.cisco_ios_xr.tailf_confd_monitoring', 'ConfdState.Internal.Callpoints.SnmpNotificationSubscription.Daemon.Error',
        '''If this leaf exists, there is a problem
with the daemon registration.''',
        {
            'PENDING':'PENDING',
        }, 'tailf-common-monitoring', _yang_ns.NAMESPACE_LOOKUP['tailf-common-monitoring']),
    'ConfdState.Internal.Callpoints.SnmpNotificationSubscription.Daemon' : {
        'meta_info' : _MetaInfoClass('ConfdState.Internal.Callpoints.SnmpNotificationSubscription.Daemon', REFERENCE_CLASS,
            ''' ''',
            False, 
            [
            _MetaInfoClassMember('id', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('0', '4294967295')], [],
                '''                The numerical id assigned to the application daemon
                that has registered for a callpoint.
                ''',
                'id',
                'tailf-confd-monitoring', False, is_config=False),
            _MetaInfoClassMember('name', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                The name of the application daemon that has
                registered for a callpoint.
                ''',
                'name',
                'tailf-confd-monitoring', False, is_config=False),
            _MetaInfoClassMember('error', REFERENCE_ENUM_CLASS, 'Error', 'enumeration',
                'ydk.models.cisco_ios_xr.tailf_confd_monitoring', 'ConfdState.Internal.Callpoints.SnmpNotificationSubscription.Daemon.Error',
                [], [],
                '''                If this leaf exists, there is a problem
                with the daemon registration.
                ''',
                'error',
                'tailf-confd-monitoring', False, is_config=False),
            ],
            'tailf-confd-monitoring',
            'daemon',
            _yang_ns.NAMESPACE_LOOKUP['tailf-confd-monitoring'],
            'ydk.models.cisco_ios_xr.tailf_confd_monitoring',
            is_config=False,
        ),
    },
    'ConfdState.Internal.Callpoints.SnmpNotificationSubscription.Range.Daemon.Error' : _MetaInfoEnum('Error',
        'ydk.models.cisco_ios_xr.tailf_confd_monitoring', 'ConfdState.Internal.Callpoints.SnmpNotificationSubscription.Range.Daemon.Error',
        '''If this leaf exists, there is a problem
with the daemon registration.''',
        {
            'PENDING':'PENDING',
        }, 'tailf-common-monitoring', _yang_ns.NAMESPACE_LOOKUP['tailf-common-monitoring']),
    'ConfdState.Internal.Callpoints.SnmpNotificationSubscription.Range.Daemon' : {
        'meta_info' : _MetaInfoClass('ConfdState.Internal.Callpoints.SnmpNotificationSubscription.Range.Daemon', REFERENCE_CLASS,
            ''' ''',
            False, 
            [
            _MetaInfoClassMember('id', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('0', '4294967295')], [],
                '''                The numerical id assigned to the application daemon
                that has registered for a callpoint.
                ''',
                'id',
                'tailf-confd-monitoring', False, is_config=False),
            _MetaInfoClassMember('name', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                The name of the application daemon that has
                registered for a callpoint.
                ''',
                'name',
                'tailf-confd-monitoring', False, is_config=False),
            _MetaInfoClassMember('error', REFERENCE_ENUM_CLASS, 'Error', 'enumeration',
                'ydk.models.cisco_ios_xr.tailf_confd_monitoring', 'ConfdState.Internal.Callpoints.SnmpNotificationSubscription.Range.Daemon.Error',
                [], [],
                '''                If this leaf exists, there is a problem
                with the daemon registration.
                ''',
                'error',
                'tailf-confd-monitoring', False, is_config=False),
            ],
            'tailf-confd-monitoring',
            'daemon',
            _yang_ns.NAMESPACE_LOOKUP['tailf-confd-monitoring'],
            'ydk.models.cisco_ios_xr.tailf_confd_monitoring',
            is_config=False,
        ),
    },
    'ConfdState.Internal.Callpoints.SnmpNotificationSubscription.Range' : {
        'meta_info' : _MetaInfoClass('ConfdState.Internal.Callpoints.SnmpNotificationSubscription.Range', REFERENCE_LIST,
            ''' ''',
            False, 
            [
            _MetaInfoClassMember('lower', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                The space-separated set of keys that defines the lower
                endpoint of the range for a non-default registration.
                ''',
                'lower',
                'tailf-confd-monitoring', False, is_config=False),
            _MetaInfoClassMember('upper', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                The space-separated set of keys that defines the upper
                endpoint of the range for a non-default registration.
                ''',
                'upper',
                'tailf-confd-monitoring', False, is_config=False),
            _MetaInfoClassMember('default', ATTRIBUTE, 'Empty', 'empty',
                None, None,
                [], [],
                '''                If this leaf exists, this is a default registration
                - in this case 'lower' and 'upper' do not exist.
                ''',
                'default',
                'tailf-confd-monitoring', False, is_config=False),
            _MetaInfoClassMember('daemon', REFERENCE_CLASS, 'Daemon', '',
                'ydk.models.cisco_ios_xr.tailf_confd_monitoring', 'ConfdState.Internal.Callpoints.SnmpNotificationSubscription.Range.Daemon',
                [], [],
                '''                ''',
                'daemon',
                'tailf-confd-monitoring', False, is_config=False),
            ],
            'tailf-confd-monitoring',
            'range',
            _yang_ns.NAMESPACE_LOOKUP['tailf-confd-monitoring'],
            'ydk.models.cisco_ios_xr.tailf_confd_monitoring',
            is_config=False,
        ),
    },
    'ConfdState.Internal.Callpoints.SnmpNotificationSubscription.Error' : _MetaInfoEnum('Error',
        'ydk.models.cisco_ios_xr.tailf_confd_monitoring', 'ConfdState.Internal.Callpoints.SnmpNotificationSubscription.Error',
        '''If this leaf exists, there is a problem
with the callpoint registration.''',
        {
            'NOT-REGISTERED':'NOT_REGISTERED',
            'UNKNOWN':'UNKNOWN',
        }, 'tailf-common-monitoring', _yang_ns.NAMESPACE_LOOKUP['tailf-common-monitoring']),
    'ConfdState.Internal.Callpoints.SnmpNotificationSubscription' : {
        'meta_info' : _MetaInfoClass('ConfdState.Internal.Callpoints.SnmpNotificationSubscription', REFERENCE_LIST,
            ''' ''',
            False, 
            [
            _MetaInfoClassMember('id', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                Callpoint id
                ''',
                'id',
                'tailf-confd-monitoring', True, is_config=False),
            _MetaInfoClassMember('daemon', REFERENCE_CLASS, 'Daemon', '',
                'ydk.models.cisco_ios_xr.tailf_confd_monitoring', 'ConfdState.Internal.Callpoints.SnmpNotificationSubscription.Daemon',
                [], [],
                '''                ''',
                'daemon',
                'tailf-confd-monitoring', False, is_config=False),
            _MetaInfoClassMember('path', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                The path of the list that a range registration
                pertains to.
                ''',
                'path',
                'tailf-confd-monitoring', False, is_config=False),
            _MetaInfoClassMember('range', REFERENCE_LIST, 'Range', '',
                'ydk.models.cisco_ios_xr.tailf_confd_monitoring', 'ConfdState.Internal.Callpoints.SnmpNotificationSubscription.Range',
                [], [],
                '''                ''',
                'range',
                'tailf-confd-monitoring', False, is_config=False),
            _MetaInfoClassMember('file', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                The pathname of the shared object implementing the type
                for a typepoint.
                ''',
                'file',
                'tailf-confd-monitoring', False, is_config=False),
            _MetaInfoClassMember('error', REFERENCE_ENUM_CLASS, 'Error', 'enumeration',
                'ydk.models.cisco_ios_xr.tailf_confd_monitoring', 'ConfdState.Internal.Callpoints.SnmpNotificationSubscription.Error',
                [], [],
                '''                If this leaf exists, there is a problem
                with the callpoint registration.
                ''',
                'error',
                'tailf-confd-monitoring', False, is_config=False),
            ],
            'tailf-confd-monitoring',
            'snmp-notification-subscription',
            _yang_ns.NAMESPACE_LOOKUP['tailf-confd-monitoring'],
            'ydk.models.cisco_ios_xr.tailf_confd_monitoring',
            is_config=False,
        ),
    },
    'ConfdState.Internal.Callpoints.ErrorFormattingCallback.Daemon.Error' : _MetaInfoEnum('Error',
        'ydk.models.cisco_ios_xr.tailf_confd_monitoring', 'ConfdState.Internal.Callpoints.ErrorFormattingCallback.Daemon.Error',
        '''If this leaf exists, there is a problem
with the daemon registration.''',
        {
            'PENDING':'PENDING',
        }, 'tailf-common-monitoring', _yang_ns.NAMESPACE_LOOKUP['tailf-common-monitoring']),
    'ConfdState.Internal.Callpoints.ErrorFormattingCallback.Daemon' : {
        'meta_info' : _MetaInfoClass('ConfdState.Internal.Callpoints.ErrorFormattingCallback.Daemon', REFERENCE_CLASS,
            ''' ''',
            False, 
            [
            _MetaInfoClassMember('id', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('0', '4294967295')], [],
                '''                The numerical id assigned to the application daemon
                that has registered for a callpoint.
                ''',
                'id',
                'tailf-confd-monitoring', False, is_config=False),
            _MetaInfoClassMember('name', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                The name of the application daemon that has
                registered for a callpoint.
                ''',
                'name',
                'tailf-confd-monitoring', False, is_config=False),
            _MetaInfoClassMember('error', REFERENCE_ENUM_CLASS, 'Error', 'enumeration',
                'ydk.models.cisco_ios_xr.tailf_confd_monitoring', 'ConfdState.Internal.Callpoints.ErrorFormattingCallback.Daemon.Error',
                [], [],
                '''                If this leaf exists, there is a problem
                with the daemon registration.
                ''',
                'error',
                'tailf-confd-monitoring', False, is_config=False),
            ],
            'tailf-confd-monitoring',
            'daemon',
            _yang_ns.NAMESPACE_LOOKUP['tailf-confd-monitoring'],
            'ydk.models.cisco_ios_xr.tailf_confd_monitoring',
            is_config=False,
        ),
    },
    'ConfdState.Internal.Callpoints.ErrorFormattingCallback.Range.Daemon.Error' : _MetaInfoEnum('Error',
        'ydk.models.cisco_ios_xr.tailf_confd_monitoring', 'ConfdState.Internal.Callpoints.ErrorFormattingCallback.Range.Daemon.Error',
        '''If this leaf exists, there is a problem
with the daemon registration.''',
        {
            'PENDING':'PENDING',
        }, 'tailf-common-monitoring', _yang_ns.NAMESPACE_LOOKUP['tailf-common-monitoring']),
    'ConfdState.Internal.Callpoints.ErrorFormattingCallback.Range.Daemon' : {
        'meta_info' : _MetaInfoClass('ConfdState.Internal.Callpoints.ErrorFormattingCallback.Range.Daemon', REFERENCE_CLASS,
            ''' ''',
            False, 
            [
            _MetaInfoClassMember('id', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('0', '4294967295')], [],
                '''                The numerical id assigned to the application daemon
                that has registered for a callpoint.
                ''',
                'id',
                'tailf-confd-monitoring', False, is_config=False),
            _MetaInfoClassMember('name', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                The name of the application daemon that has
                registered for a callpoint.
                ''',
                'name',
                'tailf-confd-monitoring', False, is_config=False),
            _MetaInfoClassMember('error', REFERENCE_ENUM_CLASS, 'Error', 'enumeration',
                'ydk.models.cisco_ios_xr.tailf_confd_monitoring', 'ConfdState.Internal.Callpoints.ErrorFormattingCallback.Range.Daemon.Error',
                [], [],
                '''                If this leaf exists, there is a problem
                with the daemon registration.
                ''',
                'error',
                'tailf-confd-monitoring', False, is_config=False),
            ],
            'tailf-confd-monitoring',
            'daemon',
            _yang_ns.NAMESPACE_LOOKUP['tailf-confd-monitoring'],
            'ydk.models.cisco_ios_xr.tailf_confd_monitoring',
            is_config=False,
        ),
    },
    'ConfdState.Internal.Callpoints.ErrorFormattingCallback.Range' : {
        'meta_info' : _MetaInfoClass('ConfdState.Internal.Callpoints.ErrorFormattingCallback.Range', REFERENCE_LIST,
            ''' ''',
            False, 
            [
            _MetaInfoClassMember('lower', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                The space-separated set of keys that defines the lower
                endpoint of the range for a non-default registration.
                ''',
                'lower',
                'tailf-confd-monitoring', False, is_config=False),
            _MetaInfoClassMember('upper', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                The space-separated set of keys that defines the upper
                endpoint of the range for a non-default registration.
                ''',
                'upper',
                'tailf-confd-monitoring', False, is_config=False),
            _MetaInfoClassMember('default', ATTRIBUTE, 'Empty', 'empty',
                None, None,
                [], [],
                '''                If this leaf exists, this is a default registration
                - in this case 'lower' and 'upper' do not exist.
                ''',
                'default',
                'tailf-confd-monitoring', False, is_config=False),
            _MetaInfoClassMember('daemon', REFERENCE_CLASS, 'Daemon', '',
                'ydk.models.cisco_ios_xr.tailf_confd_monitoring', 'ConfdState.Internal.Callpoints.ErrorFormattingCallback.Range.Daemon',
                [], [],
                '''                ''',
                'daemon',
                'tailf-confd-monitoring', False, is_config=False),
            ],
            'tailf-confd-monitoring',
            'range',
            _yang_ns.NAMESPACE_LOOKUP['tailf-confd-monitoring'],
            'ydk.models.cisco_ios_xr.tailf_confd_monitoring',
            is_config=False,
        ),
    },
    'ConfdState.Internal.Callpoints.ErrorFormattingCallback.Error' : _MetaInfoEnum('Error',
        'ydk.models.cisco_ios_xr.tailf_confd_monitoring', 'ConfdState.Internal.Callpoints.ErrorFormattingCallback.Error',
        '''If this leaf exists, there is a problem
with the callpoint registration.''',
        {
            'NOT-REGISTERED':'NOT_REGISTERED',
            'UNKNOWN':'UNKNOWN',
        }, 'tailf-common-monitoring', _yang_ns.NAMESPACE_LOOKUP['tailf-common-monitoring']),
    'ConfdState.Internal.Callpoints.ErrorFormattingCallback' : {
        'meta_info' : _MetaInfoClass('ConfdState.Internal.Callpoints.ErrorFormattingCallback', REFERENCE_LIST,
            ''' ''',
            False, 
            [
            _MetaInfoClassMember('id', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                Callpoint id
                ''',
                'id',
                'tailf-confd-monitoring', True, is_config=False),
            _MetaInfoClassMember('daemon', REFERENCE_CLASS, 'Daemon', '',
                'ydk.models.cisco_ios_xr.tailf_confd_monitoring', 'ConfdState.Internal.Callpoints.ErrorFormattingCallback.Daemon',
                [], [],
                '''                ''',
                'daemon',
                'tailf-confd-monitoring', False, is_config=False),
            _MetaInfoClassMember('path', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                The path of the list that a range registration
                pertains to.
                ''',
                'path',
                'tailf-confd-monitoring', False, is_config=False),
            _MetaInfoClassMember('range', REFERENCE_LIST, 'Range', '',
                'ydk.models.cisco_ios_xr.tailf_confd_monitoring', 'ConfdState.Internal.Callpoints.ErrorFormattingCallback.Range',
                [], [],
                '''                ''',
                'range',
                'tailf-confd-monitoring', False, is_config=False),
            _MetaInfoClassMember('file', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                The pathname of the shared object implementing the type
                for a typepoint.
                ''',
                'file',
                'tailf-confd-monitoring', False, is_config=False),
            _MetaInfoClassMember('error', REFERENCE_ENUM_CLASS, 'Error', 'enumeration',
                'ydk.models.cisco_ios_xr.tailf_confd_monitoring', 'ConfdState.Internal.Callpoints.ErrorFormattingCallback.Error',
                [], [],
                '''                If this leaf exists, there is a problem
                with the callpoint registration.
                ''',
                'error',
                'tailf-confd-monitoring', False, is_config=False),
            ],
            'tailf-confd-monitoring',
            'error-formatting-callback',
            _yang_ns.NAMESPACE_LOOKUP['tailf-confd-monitoring'],
            'ydk.models.cisco_ios_xr.tailf_confd_monitoring',
            is_config=False,
        ),
    },
    'ConfdState.Internal.Callpoints.Typepoint.Daemon.Error' : _MetaInfoEnum('Error',
        'ydk.models.cisco_ios_xr.tailf_confd_monitoring', 'ConfdState.Internal.Callpoints.Typepoint.Daemon.Error',
        '''If this leaf exists, there is a problem
with the daemon registration.''',
        {
            'PENDING':'PENDING',
        }, 'tailf-common-monitoring', _yang_ns.NAMESPACE_LOOKUP['tailf-common-monitoring']),
    'ConfdState.Internal.Callpoints.Typepoint.Daemon' : {
        'meta_info' : _MetaInfoClass('ConfdState.Internal.Callpoints.Typepoint.Daemon', REFERENCE_CLASS,
            ''' ''',
            False, 
            [
            _MetaInfoClassMember('id', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('0', '4294967295')], [],
                '''                The numerical id assigned to the application daemon
                that has registered for a callpoint.
                ''',
                'id',
                'tailf-confd-monitoring', False, is_config=False),
            _MetaInfoClassMember('name', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                The name of the application daemon that has
                registered for a callpoint.
                ''',
                'name',
                'tailf-confd-monitoring', False, is_config=False),
            _MetaInfoClassMember('error', REFERENCE_ENUM_CLASS, 'Error', 'enumeration',
                'ydk.models.cisco_ios_xr.tailf_confd_monitoring', 'ConfdState.Internal.Callpoints.Typepoint.Daemon.Error',
                [], [],
                '''                If this leaf exists, there is a problem
                with the daemon registration.
                ''',
                'error',
                'tailf-confd-monitoring', False, is_config=False),
            ],
            'tailf-confd-monitoring',
            'daemon',
            _yang_ns.NAMESPACE_LOOKUP['tailf-confd-monitoring'],
            'ydk.models.cisco_ios_xr.tailf_confd_monitoring',
            is_config=False,
        ),
    },
    'ConfdState.Internal.Callpoints.Typepoint.Range.Daemon.Error' : _MetaInfoEnum('Error',
        'ydk.models.cisco_ios_xr.tailf_confd_monitoring', 'ConfdState.Internal.Callpoints.Typepoint.Range.Daemon.Error',
        '''If this leaf exists, there is a problem
with the daemon registration.''',
        {
            'PENDING':'PENDING',
        }, 'tailf-common-monitoring', _yang_ns.NAMESPACE_LOOKUP['tailf-common-monitoring']),
    'ConfdState.Internal.Callpoints.Typepoint.Range.Daemon' : {
        'meta_info' : _MetaInfoClass('ConfdState.Internal.Callpoints.Typepoint.Range.Daemon', REFERENCE_CLASS,
            ''' ''',
            False, 
            [
            _MetaInfoClassMember('id', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('0', '4294967295')], [],
                '''                The numerical id assigned to the application daemon
                that has registered for a callpoint.
                ''',
                'id',
                'tailf-confd-monitoring', False, is_config=False),
            _MetaInfoClassMember('name', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                The name of the application daemon that has
                registered for a callpoint.
                ''',
                'name',
                'tailf-confd-monitoring', False, is_config=False),
            _MetaInfoClassMember('error', REFERENCE_ENUM_CLASS, 'Error', 'enumeration',
                'ydk.models.cisco_ios_xr.tailf_confd_monitoring', 'ConfdState.Internal.Callpoints.Typepoint.Range.Daemon.Error',
                [], [],
                '''                If this leaf exists, there is a problem
                with the daemon registration.
                ''',
                'error',
                'tailf-confd-monitoring', False, is_config=False),
            ],
            'tailf-confd-monitoring',
            'daemon',
            _yang_ns.NAMESPACE_LOOKUP['tailf-confd-monitoring'],
            'ydk.models.cisco_ios_xr.tailf_confd_monitoring',
            is_config=False,
        ),
    },
    'ConfdState.Internal.Callpoints.Typepoint.Range' : {
        'meta_info' : _MetaInfoClass('ConfdState.Internal.Callpoints.Typepoint.Range', REFERENCE_LIST,
            ''' ''',
            False, 
            [
            _MetaInfoClassMember('lower', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                The space-separated set of keys that defines the lower
                endpoint of the range for a non-default registration.
                ''',
                'lower',
                'tailf-confd-monitoring', False, is_config=False),
            _MetaInfoClassMember('upper', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                The space-separated set of keys that defines the upper
                endpoint of the range for a non-default registration.
                ''',
                'upper',
                'tailf-confd-monitoring', False, is_config=False),
            _MetaInfoClassMember('default', ATTRIBUTE, 'Empty', 'empty',
                None, None,
                [], [],
                '''                If this leaf exists, this is a default registration
                - in this case 'lower' and 'upper' do not exist.
                ''',
                'default',
                'tailf-confd-monitoring', False, is_config=False),
            _MetaInfoClassMember('daemon', REFERENCE_CLASS, 'Daemon', '',
                'ydk.models.cisco_ios_xr.tailf_confd_monitoring', 'ConfdState.Internal.Callpoints.Typepoint.Range.Daemon',
                [], [],
                '''                ''',
                'daemon',
                'tailf-confd-monitoring', False, is_config=False),
            ],
            'tailf-confd-monitoring',
            'range',
            _yang_ns.NAMESPACE_LOOKUP['tailf-confd-monitoring'],
            'ydk.models.cisco_ios_xr.tailf_confd_monitoring',
            is_config=False,
        ),
    },
    'ConfdState.Internal.Callpoints.Typepoint.Error' : _MetaInfoEnum('Error',
        'ydk.models.cisco_ios_xr.tailf_confd_monitoring', 'ConfdState.Internal.Callpoints.Typepoint.Error',
        '''If this leaf exists, there is a problem
with the callpoint registration.''',
        {
            'NOT-REGISTERED':'NOT_REGISTERED',
            'UNKNOWN':'UNKNOWN',
        }, 'tailf-common-monitoring', _yang_ns.NAMESPACE_LOOKUP['tailf-common-monitoring']),
    'ConfdState.Internal.Callpoints.Typepoint' : {
        'meta_info' : _MetaInfoClass('ConfdState.Internal.Callpoints.Typepoint', REFERENCE_LIST,
            ''' ''',
            False, 
            [
            _MetaInfoClassMember('id', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                Callpoint id
                ''',
                'id',
                'tailf-confd-monitoring', True, is_config=False),
            _MetaInfoClassMember('daemon', REFERENCE_CLASS, 'Daemon', '',
                'ydk.models.cisco_ios_xr.tailf_confd_monitoring', 'ConfdState.Internal.Callpoints.Typepoint.Daemon',
                [], [],
                '''                ''',
                'daemon',
                'tailf-confd-monitoring', False, is_config=False),
            _MetaInfoClassMember('path', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                The path of the list that a range registration
                pertains to.
                ''',
                'path',
                'tailf-confd-monitoring', False, is_config=False),
            _MetaInfoClassMember('range', REFERENCE_LIST, 'Range', '',
                'ydk.models.cisco_ios_xr.tailf_confd_monitoring', 'ConfdState.Internal.Callpoints.Typepoint.Range',
                [], [],
                '''                ''',
                'range',
                'tailf-confd-monitoring', False, is_config=False),
            _MetaInfoClassMember('file', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                The pathname of the shared object implementing the type
                for a typepoint.
                ''',
                'file',
                'tailf-confd-monitoring', False, is_config=False),
            _MetaInfoClassMember('error', REFERENCE_ENUM_CLASS, 'Error', 'enumeration',
                'ydk.models.cisco_ios_xr.tailf_confd_monitoring', 'ConfdState.Internal.Callpoints.Typepoint.Error',
                [], [],
                '''                If this leaf exists, there is a problem
                with the callpoint registration.
                ''',
                'error',
                'tailf-confd-monitoring', False, is_config=False),
            ],
            'tailf-confd-monitoring',
            'typepoint',
            _yang_ns.NAMESPACE_LOOKUP['tailf-confd-monitoring'],
            'ydk.models.cisco_ios_xr.tailf_confd_monitoring',
            is_config=False,
        ),
    },
    'ConfdState.Internal.Callpoints.NotificationStreamReplay.Daemon.Error' : _MetaInfoEnum('Error',
        'ydk.models.cisco_ios_xr.tailf_confd_monitoring', 'ConfdState.Internal.Callpoints.NotificationStreamReplay.Daemon.Error',
        '''If this leaf exists, there is a problem
with the daemon registration.''',
        {
            'PENDING':'PENDING',
        }, 'tailf-common-monitoring', _yang_ns.NAMESPACE_LOOKUP['tailf-common-monitoring']),
    'ConfdState.Internal.Callpoints.NotificationStreamReplay.Daemon' : {
        'meta_info' : _MetaInfoClass('ConfdState.Internal.Callpoints.NotificationStreamReplay.Daemon', REFERENCE_CLASS,
            ''' ''',
            False, 
            [
            _MetaInfoClassMember('id', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('0', '4294967295')], [],
                '''                The numerical id assigned to the application daemon
                that has registered for a callpoint.
                ''',
                'id',
                'tailf-confd-monitoring', False, is_config=False),
            _MetaInfoClassMember('name', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                The name of the application daemon that has
                registered for a callpoint.
                ''',
                'name',
                'tailf-confd-monitoring', False, is_config=False),
            _MetaInfoClassMember('error', REFERENCE_ENUM_CLASS, 'Error', 'enumeration',
                'ydk.models.cisco_ios_xr.tailf_confd_monitoring', 'ConfdState.Internal.Callpoints.NotificationStreamReplay.Daemon.Error',
                [], [],
                '''                If this leaf exists, there is a problem
                with the daemon registration.
                ''',
                'error',
                'tailf-confd-monitoring', False, is_config=False),
            ],
            'tailf-confd-monitoring',
            'daemon',
            _yang_ns.NAMESPACE_LOOKUP['tailf-confd-monitoring'],
            'ydk.models.cisco_ios_xr.tailf_confd_monitoring',
            is_config=False,
        ),
    },
    'ConfdState.Internal.Callpoints.NotificationStreamReplay.Range.Daemon.Error' : _MetaInfoEnum('Error',
        'ydk.models.cisco_ios_xr.tailf_confd_monitoring', 'ConfdState.Internal.Callpoints.NotificationStreamReplay.Range.Daemon.Error',
        '''If this leaf exists, there is a problem
with the daemon registration.''',
        {
            'PENDING':'PENDING',
        }, 'tailf-common-monitoring', _yang_ns.NAMESPACE_LOOKUP['tailf-common-monitoring']),
    'ConfdState.Internal.Callpoints.NotificationStreamReplay.Range.Daemon' : {
        'meta_info' : _MetaInfoClass('ConfdState.Internal.Callpoints.NotificationStreamReplay.Range.Daemon', REFERENCE_CLASS,
            ''' ''',
            False, 
            [
            _MetaInfoClassMember('id', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('0', '4294967295')], [],
                '''                The numerical id assigned to the application daemon
                that has registered for a callpoint.
                ''',
                'id',
                'tailf-confd-monitoring', False, is_config=False),
            _MetaInfoClassMember('name', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                The name of the application daemon that has
                registered for a callpoint.
                ''',
                'name',
                'tailf-confd-monitoring', False, is_config=False),
            _MetaInfoClassMember('error', REFERENCE_ENUM_CLASS, 'Error', 'enumeration',
                'ydk.models.cisco_ios_xr.tailf_confd_monitoring', 'ConfdState.Internal.Callpoints.NotificationStreamReplay.Range.Daemon.Error',
                [], [],
                '''                If this leaf exists, there is a problem
                with the daemon registration.
                ''',
                'error',
                'tailf-confd-monitoring', False, is_config=False),
            ],
            'tailf-confd-monitoring',
            'daemon',
            _yang_ns.NAMESPACE_LOOKUP['tailf-confd-monitoring'],
            'ydk.models.cisco_ios_xr.tailf_confd_monitoring',
            is_config=False,
        ),
    },
    'ConfdState.Internal.Callpoints.NotificationStreamReplay.Range' : {
        'meta_info' : _MetaInfoClass('ConfdState.Internal.Callpoints.NotificationStreamReplay.Range', REFERENCE_LIST,
            ''' ''',
            False, 
            [
            _MetaInfoClassMember('lower', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                The space-separated set of keys that defines the lower
                endpoint of the range for a non-default registration.
                ''',
                'lower',
                'tailf-confd-monitoring', False, is_config=False),
            _MetaInfoClassMember('upper', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                The space-separated set of keys that defines the upper
                endpoint of the range for a non-default registration.
                ''',
                'upper',
                'tailf-confd-monitoring', False, is_config=False),
            _MetaInfoClassMember('default', ATTRIBUTE, 'Empty', 'empty',
                None, None,
                [], [],
                '''                If this leaf exists, this is a default registration
                - in this case 'lower' and 'upper' do not exist.
                ''',
                'default',
                'tailf-confd-monitoring', False, is_config=False),
            _MetaInfoClassMember('daemon', REFERENCE_CLASS, 'Daemon', '',
                'ydk.models.cisco_ios_xr.tailf_confd_monitoring', 'ConfdState.Internal.Callpoints.NotificationStreamReplay.Range.Daemon',
                [], [],
                '''                ''',
                'daemon',
                'tailf-confd-monitoring', False, is_config=False),
            ],
            'tailf-confd-monitoring',
            'range',
            _yang_ns.NAMESPACE_LOOKUP['tailf-confd-monitoring'],
            'ydk.models.cisco_ios_xr.tailf_confd_monitoring',
            is_config=False,
        ),
    },
    'ConfdState.Internal.Callpoints.NotificationStreamReplay.Error' : _MetaInfoEnum('Error',
        'ydk.models.cisco_ios_xr.tailf_confd_monitoring', 'ConfdState.Internal.Callpoints.NotificationStreamReplay.Error',
        '''If this leaf exists, there is a problem
with the callpoint registration.''',
        {
            'NOT-REGISTERED':'NOT_REGISTERED',
            'UNKNOWN':'UNKNOWN',
        }, 'tailf-common-monitoring', _yang_ns.NAMESPACE_LOOKUP['tailf-common-monitoring']),
    'ConfdState.Internal.Callpoints.NotificationStreamReplay.ReplaySupport' : _MetaInfoEnum('ReplaySupport',
        'ydk.models.cisco_ios_xr.tailf_confd_monitoring', 'ConfdState.Internal.Callpoints.NotificationStreamReplay.ReplaySupport',
        ''' ''',
        {
            'none':'none',
            'builtin':'builtin',
            'external':'external',
        }, 'tailf-common-monitoring', _yang_ns.NAMESPACE_LOOKUP['tailf-common-monitoring']),
    'ConfdState.Internal.Callpoints.NotificationStreamReplay' : {
        'meta_info' : _MetaInfoClass('ConfdState.Internal.Callpoints.NotificationStreamReplay', REFERENCE_LIST,
            ''' ''',
            False, 
            [
            _MetaInfoClassMember('name', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                Name of the notification stream.
                ''',
                'name',
                'tailf-confd-monitoring', True, is_config=False),
            _MetaInfoClassMember('replay-support', REFERENCE_ENUM_CLASS, 'ReplaySupport', 'enumeration',
                'ydk.models.cisco_ios_xr.tailf_confd_monitoring', 'ConfdState.Internal.Callpoints.NotificationStreamReplay.ReplaySupport',
                [], [],
                '''                ''',
                'replay_support',
                'tailf-confd-monitoring', False, is_config=False),
            _MetaInfoClassMember('daemon', REFERENCE_CLASS, 'Daemon', '',
                'ydk.models.cisco_ios_xr.tailf_confd_monitoring', 'ConfdState.Internal.Callpoints.NotificationStreamReplay.Daemon',
                [], [],
                '''                ''',
                'daemon',
                'tailf-confd-monitoring', False, is_config=False),
            _MetaInfoClassMember('path', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                The path of the list that a range registration
                pertains to.
                ''',
                'path',
                'tailf-confd-monitoring', False, is_config=False),
            _MetaInfoClassMember('range', REFERENCE_LIST, 'Range', '',
                'ydk.models.cisco_ios_xr.tailf_confd_monitoring', 'ConfdState.Internal.Callpoints.NotificationStreamReplay.Range',
                [], [],
                '''                ''',
                'range',
                'tailf-confd-monitoring', False, is_config=False),
            _MetaInfoClassMember('file', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                The pathname of the shared object implementing the type
                for a typepoint.
                ''',
                'file',
                'tailf-confd-monitoring', False, is_config=False),
            _MetaInfoClassMember('error', REFERENCE_ENUM_CLASS, 'Error', 'enumeration',
                'ydk.models.cisco_ios_xr.tailf_confd_monitoring', 'ConfdState.Internal.Callpoints.NotificationStreamReplay.Error',
                [], [],
                '''                If this leaf exists, there is a problem
                with the callpoint registration.
                ''',
                'error',
                'tailf-confd-monitoring', False, is_config=False),
            ],
            'tailf-confd-monitoring',
            'notification-stream-replay',
            _yang_ns.NAMESPACE_LOOKUP['tailf-confd-monitoring'],
            'ydk.models.cisco_ios_xr.tailf_confd_monitoring',
            is_config=False,
        ),
    },
    'ConfdState.Internal.Callpoints.AuthenticationCallback.Daemon.Error' : _MetaInfoEnum('Error',
        'ydk.models.cisco_ios_xr.tailf_confd_monitoring', 'ConfdState.Internal.Callpoints.AuthenticationCallback.Daemon.Error',
        '''If this leaf exists, there is a problem
with the daemon registration.''',
        {
            'PENDING':'PENDING',
        }, 'tailf-common-monitoring', _yang_ns.NAMESPACE_LOOKUP['tailf-common-monitoring']),
    'ConfdState.Internal.Callpoints.AuthenticationCallback.Daemon' : {
        'meta_info' : _MetaInfoClass('ConfdState.Internal.Callpoints.AuthenticationCallback.Daemon', REFERENCE_CLASS,
            ''' ''',
            False, 
            [
            _MetaInfoClassMember('id', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('0', '4294967295')], [],
                '''                The numerical id assigned to the application daemon
                that has registered for a callpoint.
                ''',
                'id',
                'tailf-confd-monitoring', False, is_config=False),
            _MetaInfoClassMember('name', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                The name of the application daemon that has
                registered for a callpoint.
                ''',
                'name',
                'tailf-confd-monitoring', False, is_config=False),
            _MetaInfoClassMember('error', REFERENCE_ENUM_CLASS, 'Error', 'enumeration',
                'ydk.models.cisco_ios_xr.tailf_confd_monitoring', 'ConfdState.Internal.Callpoints.AuthenticationCallback.Daemon.Error',
                [], [],
                '''                If this leaf exists, there is a problem
                with the daemon registration.
                ''',
                'error',
                'tailf-confd-monitoring', False, is_config=False),
            ],
            'tailf-confd-monitoring',
            'daemon',
            _yang_ns.NAMESPACE_LOOKUP['tailf-confd-monitoring'],
            'ydk.models.cisco_ios_xr.tailf_confd_monitoring',
            is_config=False,
        ),
    },
    'ConfdState.Internal.Callpoints.AuthenticationCallback.Range.Daemon.Error' : _MetaInfoEnum('Error',
        'ydk.models.cisco_ios_xr.tailf_confd_monitoring', 'ConfdState.Internal.Callpoints.AuthenticationCallback.Range.Daemon.Error',
        '''If this leaf exists, there is a problem
with the daemon registration.''',
        {
            'PENDING':'PENDING',
        }, 'tailf-common-monitoring', _yang_ns.NAMESPACE_LOOKUP['tailf-common-monitoring']),
    'ConfdState.Internal.Callpoints.AuthenticationCallback.Range.Daemon' : {
        'meta_info' : _MetaInfoClass('ConfdState.Internal.Callpoints.AuthenticationCallback.Range.Daemon', REFERENCE_CLASS,
            ''' ''',
            False, 
            [
            _MetaInfoClassMember('id', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('0', '4294967295')], [],
                '''                The numerical id assigned to the application daemon
                that has registered for a callpoint.
                ''',
                'id',
                'tailf-confd-monitoring', False, is_config=False),
            _MetaInfoClassMember('name', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                The name of the application daemon that has
                registered for a callpoint.
                ''',
                'name',
                'tailf-confd-monitoring', False, is_config=False),
            _MetaInfoClassMember('error', REFERENCE_ENUM_CLASS, 'Error', 'enumeration',
                'ydk.models.cisco_ios_xr.tailf_confd_monitoring', 'ConfdState.Internal.Callpoints.AuthenticationCallback.Range.Daemon.Error',
                [], [],
                '''                If this leaf exists, there is a problem
                with the daemon registration.
                ''',
                'error',
                'tailf-confd-monitoring', False, is_config=False),
            ],
            'tailf-confd-monitoring',
            'daemon',
            _yang_ns.NAMESPACE_LOOKUP['tailf-confd-monitoring'],
            'ydk.models.cisco_ios_xr.tailf_confd_monitoring',
            is_config=False,
        ),
    },
    'ConfdState.Internal.Callpoints.AuthenticationCallback.Range' : {
        'meta_info' : _MetaInfoClass('ConfdState.Internal.Callpoints.AuthenticationCallback.Range', REFERENCE_LIST,
            ''' ''',
            False, 
            [
            _MetaInfoClassMember('lower', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                The space-separated set of keys that defines the lower
                endpoint of the range for a non-default registration.
                ''',
                'lower',
                'tailf-confd-monitoring', False, is_config=False),
            _MetaInfoClassMember('upper', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                The space-separated set of keys that defines the upper
                endpoint of the range for a non-default registration.
                ''',
                'upper',
                'tailf-confd-monitoring', False, is_config=False),
            _MetaInfoClassMember('default', ATTRIBUTE, 'Empty', 'empty',
                None, None,
                [], [],
                '''                If this leaf exists, this is a default registration
                - in this case 'lower' and 'upper' do not exist.
                ''',
                'default',
                'tailf-confd-monitoring', False, is_config=False),
            _MetaInfoClassMember('daemon', REFERENCE_CLASS, 'Daemon', '',
                'ydk.models.cisco_ios_xr.tailf_confd_monitoring', 'ConfdState.Internal.Callpoints.AuthenticationCallback.Range.Daemon',
                [], [],
                '''                ''',
                'daemon',
                'tailf-confd-monitoring', False, is_config=False),
            ],
            'tailf-confd-monitoring',
            'range',
            _yang_ns.NAMESPACE_LOOKUP['tailf-confd-monitoring'],
            'ydk.models.cisco_ios_xr.tailf_confd_monitoring',
            is_config=False,
        ),
    },
    'ConfdState.Internal.Callpoints.AuthenticationCallback.Error' : _MetaInfoEnum('Error',
        'ydk.models.cisco_ios_xr.tailf_confd_monitoring', 'ConfdState.Internal.Callpoints.AuthenticationCallback.Error',
        '''If this leaf exists, there is a problem
with the callpoint registration.''',
        {
            'NOT-REGISTERED':'NOT_REGISTERED',
            'UNKNOWN':'UNKNOWN',
        }, 'tailf-common-monitoring', _yang_ns.NAMESPACE_LOOKUP['tailf-common-monitoring']),
    'ConfdState.Internal.Callpoints.AuthenticationCallback' : {
        'meta_info' : _MetaInfoClass('ConfdState.Internal.Callpoints.AuthenticationCallback', REFERENCE_CLASS,
            ''' ''',
            False, 
            [
            _MetaInfoClassMember('enabled', ATTRIBUTE, 'bool', 'boolean',
                None, None,
                [], [],
                '''                ''',
                'enabled',
                'tailf-confd-monitoring', False, is_config=False),
            _MetaInfoClassMember('daemon', REFERENCE_CLASS, 'Daemon', '',
                'ydk.models.cisco_ios_xr.tailf_confd_monitoring', 'ConfdState.Internal.Callpoints.AuthenticationCallback.Daemon',
                [], [],
                '''                ''',
                'daemon',
                'tailf-confd-monitoring', False, is_config=False),
            _MetaInfoClassMember('path', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                The path of the list that a range registration
                pertains to.
                ''',
                'path',
                'tailf-confd-monitoring', False, is_config=False),
            _MetaInfoClassMember('range', REFERENCE_LIST, 'Range', '',
                'ydk.models.cisco_ios_xr.tailf_confd_monitoring', 'ConfdState.Internal.Callpoints.AuthenticationCallback.Range',
                [], [],
                '''                ''',
                'range',
                'tailf-confd-monitoring', False, is_config=False),
            _MetaInfoClassMember('file', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                The pathname of the shared object implementing the type
                for a typepoint.
                ''',
                'file',
                'tailf-confd-monitoring', False, is_config=False),
            _MetaInfoClassMember('error', REFERENCE_ENUM_CLASS, 'Error', 'enumeration',
                'ydk.models.cisco_ios_xr.tailf_confd_monitoring', 'ConfdState.Internal.Callpoints.AuthenticationCallback.Error',
                [], [],
                '''                If this leaf exists, there is a problem
                with the callpoint registration.
                ''',
                'error',
                'tailf-confd-monitoring', False, is_config=False),
            ],
            'tailf-confd-monitoring',
            'authentication-callback',
            _yang_ns.NAMESPACE_LOOKUP['tailf-confd-monitoring'],
            'ydk.models.cisco_ios_xr.tailf_confd_monitoring',
            is_config=False,
            is_presence=True,
        ),
    },
    'ConfdState.Internal.Callpoints.AuthorizationCallbacks.Daemon.Error' : _MetaInfoEnum('Error',
        'ydk.models.cisco_ios_xr.tailf_confd_monitoring', 'ConfdState.Internal.Callpoints.AuthorizationCallbacks.Daemon.Error',
        '''If this leaf exists, there is a problem
with the daemon registration.''',
        {
            'PENDING':'PENDING',
        }, 'tailf-common-monitoring', _yang_ns.NAMESPACE_LOOKUP['tailf-common-monitoring']),
    'ConfdState.Internal.Callpoints.AuthorizationCallbacks.Daemon' : {
        'meta_info' : _MetaInfoClass('ConfdState.Internal.Callpoints.AuthorizationCallbacks.Daemon', REFERENCE_CLASS,
            ''' ''',
            False, 
            [
            _MetaInfoClassMember('id', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('0', '4294967295')], [],
                '''                The numerical id assigned to the application daemon
                that has registered for a callpoint.
                ''',
                'id',
                'tailf-confd-monitoring', False, is_config=False),
            _MetaInfoClassMember('name', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                The name of the application daemon that has
                registered for a callpoint.
                ''',
                'name',
                'tailf-confd-monitoring', False, is_config=False),
            _MetaInfoClassMember('error', REFERENCE_ENUM_CLASS, 'Error', 'enumeration',
                'ydk.models.cisco_ios_xr.tailf_confd_monitoring', 'ConfdState.Internal.Callpoints.AuthorizationCallbacks.Daemon.Error',
                [], [],
                '''                If this leaf exists, there is a problem
                with the daemon registration.
                ''',
                'error',
                'tailf-confd-monitoring', False, is_config=False),
            ],
            'tailf-confd-monitoring',
            'daemon',
            _yang_ns.NAMESPACE_LOOKUP['tailf-confd-monitoring'],
            'ydk.models.cisco_ios_xr.tailf_confd_monitoring',
            is_config=False,
        ),
    },
    'ConfdState.Internal.Callpoints.AuthorizationCallbacks.Range.Daemon.Error' : _MetaInfoEnum('Error',
        'ydk.models.cisco_ios_xr.tailf_confd_monitoring', 'ConfdState.Internal.Callpoints.AuthorizationCallbacks.Range.Daemon.Error',
        '''If this leaf exists, there is a problem
with the daemon registration.''',
        {
            'PENDING':'PENDING',
        }, 'tailf-common-monitoring', _yang_ns.NAMESPACE_LOOKUP['tailf-common-monitoring']),
    'ConfdState.Internal.Callpoints.AuthorizationCallbacks.Range.Daemon' : {
        'meta_info' : _MetaInfoClass('ConfdState.Internal.Callpoints.AuthorizationCallbacks.Range.Daemon', REFERENCE_CLASS,
            ''' ''',
            False, 
            [
            _MetaInfoClassMember('id', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('0', '4294967295')], [],
                '''                The numerical id assigned to the application daemon
                that has registered for a callpoint.
                ''',
                'id',
                'tailf-confd-monitoring', False, is_config=False),
            _MetaInfoClassMember('name', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                The name of the application daemon that has
                registered for a callpoint.
                ''',
                'name',
                'tailf-confd-monitoring', False, is_config=False),
            _MetaInfoClassMember('error', REFERENCE_ENUM_CLASS, 'Error', 'enumeration',
                'ydk.models.cisco_ios_xr.tailf_confd_monitoring', 'ConfdState.Internal.Callpoints.AuthorizationCallbacks.Range.Daemon.Error',
                [], [],
                '''                If this leaf exists, there is a problem
                with the daemon registration.
                ''',
                'error',
                'tailf-confd-monitoring', False, is_config=False),
            ],
            'tailf-confd-monitoring',
            'daemon',
            _yang_ns.NAMESPACE_LOOKUP['tailf-confd-monitoring'],
            'ydk.models.cisco_ios_xr.tailf_confd_monitoring',
            is_config=False,
        ),
    },
    'ConfdState.Internal.Callpoints.AuthorizationCallbacks.Range' : {
        'meta_info' : _MetaInfoClass('ConfdState.Internal.Callpoints.AuthorizationCallbacks.Range', REFERENCE_LIST,
            ''' ''',
            False, 
            [
            _MetaInfoClassMember('lower', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                The space-separated set of keys that defines the lower
                endpoint of the range for a non-default registration.
                ''',
                'lower',
                'tailf-confd-monitoring', False, is_config=False),
            _MetaInfoClassMember('upper', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                The space-separated set of keys that defines the upper
                endpoint of the range for a non-default registration.
                ''',
                'upper',
                'tailf-confd-monitoring', False, is_config=False),
            _MetaInfoClassMember('default', ATTRIBUTE, 'Empty', 'empty',
                None, None,
                [], [],
                '''                If this leaf exists, this is a default registration
                - in this case 'lower' and 'upper' do not exist.
                ''',
                'default',
                'tailf-confd-monitoring', False, is_config=False),
            _MetaInfoClassMember('daemon', REFERENCE_CLASS, 'Daemon', '',
                'ydk.models.cisco_ios_xr.tailf_confd_monitoring', 'ConfdState.Internal.Callpoints.AuthorizationCallbacks.Range.Daemon',
                [], [],
                '''                ''',
                'daemon',
                'tailf-confd-monitoring', False, is_config=False),
            ],
            'tailf-confd-monitoring',
            'range',
            _yang_ns.NAMESPACE_LOOKUP['tailf-confd-monitoring'],
            'ydk.models.cisco_ios_xr.tailf_confd_monitoring',
            is_config=False,
        ),
    },
    'ConfdState.Internal.Callpoints.AuthorizationCallbacks.Error' : _MetaInfoEnum('Error',
        'ydk.models.cisco_ios_xr.tailf_confd_monitoring', 'ConfdState.Internal.Callpoints.AuthorizationCallbacks.Error',
        '''If this leaf exists, there is a problem
with the callpoint registration.''',
        {
            'NOT-REGISTERED':'NOT_REGISTERED',
            'UNKNOWN':'UNKNOWN',
        }, 'tailf-common-monitoring', _yang_ns.NAMESPACE_LOOKUP['tailf-common-monitoring']),
    'ConfdState.Internal.Callpoints.AuthorizationCallbacks' : {
        'meta_info' : _MetaInfoClass('ConfdState.Internal.Callpoints.AuthorizationCallbacks', REFERENCE_CLASS,
            ''' ''',
            False, 
            [
            _MetaInfoClassMember('enabled', ATTRIBUTE, 'bool', 'boolean',
                None, None,
                [], [],
                '''                ''',
                'enabled',
                'tailf-confd-monitoring', False, is_config=False),
            _MetaInfoClassMember('daemon', REFERENCE_CLASS, 'Daemon', '',
                'ydk.models.cisco_ios_xr.tailf_confd_monitoring', 'ConfdState.Internal.Callpoints.AuthorizationCallbacks.Daemon',
                [], [],
                '''                ''',
                'daemon',
                'tailf-confd-monitoring', False, is_config=False),
            _MetaInfoClassMember('path', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                The path of the list that a range registration
                pertains to.
                ''',
                'path',
                'tailf-confd-monitoring', False, is_config=False),
            _MetaInfoClassMember('range', REFERENCE_LIST, 'Range', '',
                'ydk.models.cisco_ios_xr.tailf_confd_monitoring', 'ConfdState.Internal.Callpoints.AuthorizationCallbacks.Range',
                [], [],
                '''                ''',
                'range',
                'tailf-confd-monitoring', False, is_config=False),
            _MetaInfoClassMember('file', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                The pathname of the shared object implementing the type
                for a typepoint.
                ''',
                'file',
                'tailf-confd-monitoring', False, is_config=False),
            _MetaInfoClassMember('error', REFERENCE_ENUM_CLASS, 'Error', 'enumeration',
                'ydk.models.cisco_ios_xr.tailf_confd_monitoring', 'ConfdState.Internal.Callpoints.AuthorizationCallbacks.Error',
                [], [],
                '''                If this leaf exists, there is a problem
                with the callpoint registration.
                ''',
                'error',
                'tailf-confd-monitoring', False, is_config=False),
            ],
            'tailf-confd-monitoring',
            'authorization-callbacks',
            _yang_ns.NAMESPACE_LOOKUP['tailf-confd-monitoring'],
            'ydk.models.cisco_ios_xr.tailf_confd_monitoring',
            is_config=False,
            is_presence=True,
        ),
    },
    'ConfdState.Internal.Callpoints' : {
        'meta_info' : _MetaInfoClass('ConfdState.Internal.Callpoints', REFERENCE_CLASS,
            ''' ''',
            False, 
            [
            _MetaInfoClassMember('callpoint', REFERENCE_LIST, 'Callpoint', '',
                'ydk.models.cisco_ios_xr.tailf_confd_monitoring', 'ConfdState.Internal.Callpoints.Callpoint',
                [], [],
                '''                ''',
                'callpoint',
                'tailf-confd-monitoring', False, is_config=False),
            _MetaInfoClassMember('validationpoint', REFERENCE_LIST, 'Validationpoint', '',
                'ydk.models.cisco_ios_xr.tailf_confd_monitoring', 'ConfdState.Internal.Callpoints.Validationpoint',
                [], [],
                '''                ''',
                'validationpoint',
                'tailf-confd-monitoring', False, is_config=False),
            _MetaInfoClassMember('actionpoint', REFERENCE_LIST, 'Actionpoint', '',
                'ydk.models.cisco_ios_xr.tailf_confd_monitoring', 'ConfdState.Internal.Callpoints.Actionpoint',
                [], [],
                '''                ''',
                'actionpoint',
                'tailf-confd-monitoring', False, is_config=False),
            _MetaInfoClassMember('snmp-inform-callback', REFERENCE_LIST, 'SnmpInformCallback', '',
                'ydk.models.cisco_ios_xr.tailf_confd_monitoring', 'ConfdState.Internal.Callpoints.SnmpInformCallback',
                [], [],
                '''                ''',
                'snmp_inform_callback',
                'tailf-confd-monitoring', False, is_config=False),
            _MetaInfoClassMember('snmp-notification-subscription', REFERENCE_LIST, 'SnmpNotificationSubscription', '',
                'ydk.models.cisco_ios_xr.tailf_confd_monitoring', 'ConfdState.Internal.Callpoints.SnmpNotificationSubscription',
                [], [],
                '''                ''',
                'snmp_notification_subscription',
                'tailf-confd-monitoring', False, is_config=False),
            _MetaInfoClassMember('error-formatting-callback', REFERENCE_LIST, 'ErrorFormattingCallback', '',
                'ydk.models.cisco_ios_xr.tailf_confd_monitoring', 'ConfdState.Internal.Callpoints.ErrorFormattingCallback',
                [], [],
                '''                ''',
                'error_formatting_callback',
                'tailf-confd-monitoring', False, is_config=False),
            _MetaInfoClassMember('typepoint', REFERENCE_LIST, 'Typepoint', '',
                'ydk.models.cisco_ios_xr.tailf_confd_monitoring', 'ConfdState.Internal.Callpoints.Typepoint',
                [], [],
                '''                ''',
                'typepoint',
                'tailf-confd-monitoring', False, is_config=False),
            _MetaInfoClassMember('notification-stream-replay', REFERENCE_LIST, 'NotificationStreamReplay', '',
                'ydk.models.cisco_ios_xr.tailf_confd_monitoring', 'ConfdState.Internal.Callpoints.NotificationStreamReplay',
                [], [],
                '''                ''',
                'notification_stream_replay',
                'tailf-confd-monitoring', False, is_config=False),
            _MetaInfoClassMember('authentication-callback', REFERENCE_CLASS, 'AuthenticationCallback', '',
                'ydk.models.cisco_ios_xr.tailf_confd_monitoring', 'ConfdState.Internal.Callpoints.AuthenticationCallback',
                [], [],
                '''                ''',
                'authentication_callback',
                'tailf-confd-monitoring', False, is_config=False, is_presence=True),
            _MetaInfoClassMember('authorization-callbacks', REFERENCE_CLASS, 'AuthorizationCallbacks', '',
                'ydk.models.cisco_ios_xr.tailf_confd_monitoring', 'ConfdState.Internal.Callpoints.AuthorizationCallbacks',
                [], [],
                '''                ''',
                'authorization_callbacks',
                'tailf-confd-monitoring', False, is_config=False, is_presence=True),
            ],
            'tailf-confd-monitoring',
            'callpoints',
            _yang_ns.NAMESPACE_LOOKUP['tailf-confd-monitoring'],
            'ydk.models.cisco_ios_xr.tailf_confd_monitoring',
            is_config=False,
        ),
    },
    'ConfdState.Internal.Cdb.Datastore.PendingSubscriptionSync.Notification' : {
        'meta_info' : _MetaInfoClass('ConfdState.Internal.Cdb.Datastore.PendingSubscriptionSync.Notification', REFERENCE_LIST,
            ''' ''',
            False, 
            [
            _MetaInfoClassMember('client-name', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                The name of the client that is the recipient of the
                notification.
                ''',
                'client_name',
                'tailf-confd-monitoring', False, is_config=False),
            _MetaInfoClassMember('subscription-ids', REFERENCE_LEAFLIST, 'int', 'subscription-id',
                None, None,
                [('0', '4294967295')], [],
                '''                The subscription identifiers for the subscriptions that
                generated the notification.
                ''',
                'subscription_ids',
                'tailf-confd-monitoring', False, is_config=False),
            ],
            'tailf-confd-monitoring',
            'notification',
            _yang_ns.NAMESPACE_LOOKUP['tailf-confd-monitoring'],
            'ydk.models.cisco_ios_xr.tailf_confd_monitoring',
            is_config=False,
        ),
    },
    'ConfdState.Internal.Cdb.Datastore.PendingSubscriptionSync.TimeRemaining' : _MetaInfoEnum('TimeRemaining',
        'ydk.models.cisco_ios_xr.tailf_confd_monitoring', 'ConfdState.Internal.Cdb.Datastore.PendingSubscriptionSync.TimeRemaining',
        ''' ''',
        {
            'infinity':'infinity',
        }, 'tailf-common-monitoring', _yang_ns.NAMESPACE_LOOKUP['tailf-common-monitoring']),
    'ConfdState.Internal.Cdb.Datastore.PendingSubscriptionSync' : {
        'meta_info' : _MetaInfoClass('ConfdState.Internal.Cdb.Datastore.PendingSubscriptionSync', REFERENCE_CLASS,
            '''Information pertaining to subscription notifications that have
been delivered to, but not yet acknowledged by, subscribing
clients. Not present for the 'startup' datastore.''',
            False, 
            [
            _MetaInfoClassMember('priority', ATTRIBUTE, 'int', 'subscription-priority',
                None, None,
                [('-2147483648', '2147483647')], [],
                '''                The priority of the subscriptions that generated the
                notifications that are waiting for acknowledgement.
                Not present for the 'operational' datastore.
                ''',
                'priority',
                'tailf-confd-monitoring', False, is_config=False),
            _MetaInfoClassMember('notification', REFERENCE_LIST, 'Notification', '',
                'ydk.models.cisco_ios_xr.tailf_confd_monitoring', 'ConfdState.Internal.Cdb.Datastore.PendingSubscriptionSync.Notification',
                [], [],
                '''                ''',
                'notification',
                'tailf-confd-monitoring', False, is_config=False),
            _MetaInfoClassMember('time-remaining', REFERENCE_UNION, 'str', 'union',
                None, None,
                [], [],
                '''                The remaining time in seconds until subscribing clients
                that have not acknowledged their notifications are
                considered unresponsive and will be disconnected. See
                /confdConfig/cdb/clientTimeout in the confd.conf(5) manual
                page. The value 'infinity' means that no timeout has been
                configured in confd.conf.
                ''',
                'time_remaining',
                'tailf-confd-monitoring', False, [
                    _MetaInfoClassMember('time-remaining', ATTRIBUTE, 'int', 'uint64',
                        None, None,
                        [('0', '18446744073709551615')], [],
                        '''                        The remaining time in seconds until subscribing clients
                        that have not acknowledged their notifications are
                        considered unresponsive and will be disconnected. See
                        /confdConfig/cdb/clientTimeout in the confd.conf(5) manual
                        page. The value 'infinity' means that no timeout has been
                        configured in confd.conf.
                        ''',
                        'time_remaining',
                        'tailf-confd-monitoring', False, is_config=False),
                    _MetaInfoClassMember('time-remaining', REFERENCE_ENUM_CLASS, 'ConfdState.Internal.Cdb.Datastore.PendingSubscriptionSync.TimeRemaining', 'enumeration',
                        'ydk.models.cisco_ios_xr.tailf_confd_monitoring', 'ConfdState.Internal.Cdb.Datastore.PendingSubscriptionSync.TimeRemaining',
                        [], [],
                        '''                        The remaining time in seconds until subscribing clients
                        that have not acknowledged their notifications are
                        considered unresponsive and will be disconnected. See
                        /confdConfig/cdb/clientTimeout in the confd.conf(5) manual
                        page. The value 'infinity' means that no timeout has been
                        configured in confd.conf.
                        ''',
                        'time_remaining',
                        'tailf-confd-monitoring', False, is_config=False),
                ], is_config=False),
            ],
            'tailf-confd-monitoring',
            'pending-subscription-sync',
            _yang_ns.NAMESPACE_LOOKUP['tailf-confd-monitoring'],
            'ydk.models.cisco_ios_xr.tailf_confd_monitoring',
            is_config=False,
            is_presence=True,
        ),
    },
    'ConfdState.Internal.Cdb.Datastore.PendingNotificationQueue.Notification' : {
        'meta_info' : _MetaInfoClass('ConfdState.Internal.Cdb.Datastore.PendingNotificationQueue.Notification', REFERENCE_LIST,
            ''' ''',
            False, 
            [
            _MetaInfoClassMember('priority', ATTRIBUTE, 'int', 'subscription-priority',
                None, None,
                [('-2147483648', '2147483647')], [],
                '''                The priority of the subscriptions that generated the
                notification. Not present for the the 'operational'
                datastore.
                ''',
                'priority',
                'tailf-confd-monitoring', False, is_config=False),
            _MetaInfoClassMember('client-name', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                The name of the client that is the recipient of the
                notification.
                ''',
                'client_name',
                'tailf-confd-monitoring', False, is_config=False),
            _MetaInfoClassMember('subscription-ids', REFERENCE_LEAFLIST, 'int', 'subscription-id',
                None, None,
                [('0', '4294967295')], [],
                '''                The subscription identifiers for the subscriptions that
                generated the notification.
                ''',
                'subscription_ids',
                'tailf-confd-monitoring', False, is_config=False),
            ],
            'tailf-confd-monitoring',
            'notification',
            _yang_ns.NAMESPACE_LOOKUP['tailf-confd-monitoring'],
            'ydk.models.cisco_ios_xr.tailf_confd_monitoring',
            is_config=False,
        ),
    },
    'ConfdState.Internal.Cdb.Datastore.PendingNotificationQueue' : {
        'meta_info' : _MetaInfoClass('ConfdState.Internal.Cdb.Datastore.PendingNotificationQueue', REFERENCE_LIST,
            '''Queues of notifications that have been generated but not
yet delivered to subscribing clients. Not present for the
'startup' datastore.''',
            False, 
            [
            _MetaInfoClassMember('notification', REFERENCE_LIST, 'Notification', '',
                'ydk.models.cisco_ios_xr.tailf_confd_monitoring', 'ConfdState.Internal.Cdb.Datastore.PendingNotificationQueue.Notification',
                [], [],
                '''                ''',
                'notification',
                'tailf-confd-monitoring', False, is_config=False),
            ],
            'tailf-confd-monitoring',
            'pending-notification-queue',
            _yang_ns.NAMESPACE_LOOKUP['tailf-confd-monitoring'],
            'ydk.models.cisco_ios_xr.tailf_confd_monitoring',
            is_config=False,
        ),
    },
    'ConfdState.Internal.Cdb.Datastore' : {
        'meta_info' : _MetaInfoClass('ConfdState.Internal.Cdb.Datastore', REFERENCE_LIST,
            ''' ''',
            False, 
            [
            _MetaInfoClassMember('name', REFERENCE_ENUM_CLASS, 'ConfdState.Internal.DatastoreName', 'datastore-name',
                'ydk.models.cisco_ios_xr.tailf_confd_monitoring', 'ConfdState.Internal.DatastoreName',
                [], [],
                '''                ''',
                'name',
                'tailf-confd-monitoring', True, is_config=False),
            _MetaInfoClassMember('transaction-id', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                The id of the last committed transaction for the 'running'
                datastore, or the last update for the 'operational' datastore.
                For the 'operational' datastore, it is only present when HA
                is enabled.
                ''',
                'transaction_id',
                'tailf-confd-monitoring', False, is_config=False),
            _MetaInfoClassMember('write-queue', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('0', '4294967295')], [],
                '''                Number of pending write requests for the 'operational'
                datastore on a HA slave that is in the process of syncronizing
                with the master.
                ''',
                'write_queue',
                'tailf-confd-monitoring', False, is_config=False),
            _MetaInfoClassMember('filename', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                The pathname of the file that is used for persistent storage
                for the datastore. Not present for 'running' when 'startup'
                exists.
                ''',
                'filename',
                'tailf-confd-monitoring', False, is_config=False),
            _MetaInfoClassMember('disk-size', ATTRIBUTE, 'int', 'size-in-bytes',
                None, None,
                [('0', '18446744073709551615')], [],
                '''                The size of the file that is used for persistent storage
                for the datastore. Only present if 'filename' is present.
                ''',
                'disk_size',
                'tailf-confd-monitoring', False, is_config=False),
            _MetaInfoClassMember('ram-size', ATTRIBUTE, 'int', 'size-in-bytes',
                None, None,
                [('0', '18446744073709551615')], [],
                '''                The size of the in-memory representation of the datastore.
                ''',
                'ram_size',
                'tailf-confd-monitoring', False, is_config=False),
            _MetaInfoClassMember('read-locks', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('0', '4294967295')], [],
                '''                The number of read locks on the datastore. Not present for
                the 'operational' data store.
                ''',
                'read_locks',
                'tailf-confd-monitoring', False, is_config=False),
            _MetaInfoClassMember('write-lock-set', ATTRIBUTE, 'bool', 'boolean',
                None, None,
                [], [],
                '''                Indicates whether a write lock is in effect for the datastore.
                Not present for the 'operational' datastore.
                ''',
                'write_lock_set',
                'tailf-confd-monitoring', False, is_config=False),
            _MetaInfoClassMember('subscription-lock-set', ATTRIBUTE, 'bool', 'boolean',
                None, None,
                [], [],
                '''                Indicates whether a subscription lock is in effect for the
                'operational' datastore.
                ''',
                'subscription_lock_set',
                'tailf-confd-monitoring', False, is_config=False),
            _MetaInfoClassMember('waiting-for-replication-sync', ATTRIBUTE, 'bool', 'boolean',
                None, None,
                [], [],
                '''                Indicates whether synchronous replication from HA master to
                HA slave is in progress for the datastore. Not present for the
                'operational' datastore.
                ''',
                'waiting_for_replication_sync',
                'tailf-confd-monitoring', False, is_config=False),
            _MetaInfoClassMember('pending-subscription-sync', REFERENCE_CLASS, 'PendingSubscriptionSync', '',
                'ydk.models.cisco_ios_xr.tailf_confd_monitoring', 'ConfdState.Internal.Cdb.Datastore.PendingSubscriptionSync',
                [], [],
                '''                Information pertaining to subscription notifications that have
                been delivered to, but not yet acknowledged by, subscribing
                clients. Not present for the 'startup' datastore.
                ''',
                'pending_subscription_sync',
                'tailf-confd-monitoring', False, is_config=False, is_presence=True),
            _MetaInfoClassMember('pending-notification-queue', REFERENCE_LIST, 'PendingNotificationQueue', '',
                'ydk.models.cisco_ios_xr.tailf_confd_monitoring', 'ConfdState.Internal.Cdb.Datastore.PendingNotificationQueue',
                [], [],
                '''                Queues of notifications that have been generated but not
                yet delivered to subscribing clients. Not present for the
                'startup' datastore.
                ''',
                'pending_notification_queue',
                'tailf-confd-monitoring', False, is_config=False),
            ],
            'tailf-confd-monitoring',
            'datastore',
            _yang_ns.NAMESPACE_LOOKUP['tailf-confd-monitoring'],
            'ydk.models.cisco_ios_xr.tailf_confd_monitoring',
            is_config=False,
        ),
    },
    'ConfdState.Internal.Cdb.Client.Subscription.Error' : _MetaInfoEnum('Error',
        'ydk.models.cisco_ios_xr.tailf_confd_monitoring', 'ConfdState.Internal.Cdb.Client.Subscription.Error',
        '''If this leaf exists, there is a problem
 with the subscription.''',
        {
            'PENDING':'PENDING',
        }, 'tailf-common-monitoring', _yang_ns.NAMESPACE_LOOKUP['tailf-common-monitoring']),
    'ConfdState.Internal.Cdb.Client.Subscription' : {
        'meta_info' : _MetaInfoClass('ConfdState.Internal.Cdb.Client.Subscription', REFERENCE_LIST,
            ''' ''',
            False, 
            [
            _MetaInfoClassMember('datastore', REFERENCE_ENUM_CLASS, 'ConfdState.Internal.DatastoreName', 'datastore-name',
                'ydk.models.cisco_ios_xr.tailf_confd_monitoring', 'ConfdState.Internal.DatastoreName',
                [], [],
                '''                The name of the datastore for the subscription - only
                'running' and 'operational' can have subscriptions.
                ''',
                'datastore',
                'tailf-confd-monitoring', False, is_config=False),
            _MetaInfoClassMember('twophase', ATTRIBUTE, 'Empty', 'empty',
                None, None,
                [], [],
                '''                Present if this is a 'twophase' subscription, i.e.
                notifications will be delivered at 'prepare' in addition
                to 'commit'. Only for the 'running' datastore.
                ''',
                'twophase',
                'tailf-confd-monitoring', False, is_config=False),
            _MetaInfoClassMember('priority', ATTRIBUTE, 'int', 'subscription-priority',
                None, None,
                [('-2147483648', '2147483647')], [],
                '''                The priority of the subscription.
                ''',
                'priority',
                'tailf-confd-monitoring', False, is_config=False),
            _MetaInfoClassMember('id', ATTRIBUTE, 'int', 'subscription-id',
                None, None,
                [('0', '4294967295')], [],
                '''                The subscription identifier for the subscription.
                ''',
                'id',
                'tailf-confd-monitoring', False, is_config=False),
            _MetaInfoClassMember('path', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                The path that the subscription pertains to.
                ''',
                'path',
                'tailf-confd-monitoring', False, is_config=False),
            _MetaInfoClassMember('error', REFERENCE_ENUM_CLASS, 'Error', 'enumeration',
                'ydk.models.cisco_ios_xr.tailf_confd_monitoring', 'ConfdState.Internal.Cdb.Client.Subscription.Error',
                [], [],
                '''                If this leaf exists, there is a problem
                 with the subscription.
                ''',
                'error',
                'tailf-confd-monitoring', False, is_config=False),
            ],
            'tailf-confd-monitoring',
            'subscription',
            _yang_ns.NAMESPACE_LOOKUP['tailf-confd-monitoring'],
            'ydk.models.cisco_ios_xr.tailf_confd_monitoring',
            is_config=False,
        ),
    },
    'ConfdState.Internal.Cdb.Client.Datastore' : _MetaInfoEnum('Datastore',
        'ydk.models.cisco_ios_xr.tailf_confd_monitoring', 'ConfdState.Internal.Cdb.Client.Datastore',
        ''' ''',
        {
            'pre_commit_running':'pre_commit_running',
        }, 'tailf-common-monitoring', _yang_ns.NAMESPACE_LOOKUP['tailf-common-monitoring']),
    'ConfdState.Internal.Cdb.Client.Lock' : _MetaInfoEnum('Lock',
        'ydk.models.cisco_ios_xr.tailf_confd_monitoring', 'ConfdState.Internal.Cdb.Client.Lock',
        '''Set when 'type' = 'client' and the client has requested or
acquired a lock on the datastore. The 'pending-read' and
'pending-subscription' values indicate that the client has
requested but not yet acquired the corresponding lock.
A 'read' lock is never taken for the 'operational' datastore,
a 'subscription' lock is never taken for any other datastore
than 'operational'.''',
        {
            'read':'read',
            'subscription':'subscription',
            'pending-read':'pending_read',
            'pending-subscription':'pending_subscription',
        }, 'tailf-common-monitoring', _yang_ns.NAMESPACE_LOOKUP['tailf-common-monitoring']),
    'ConfdState.Internal.Cdb.Client.Type' : _MetaInfoEnum('Type',
        'ydk.models.cisco_ios_xr.tailf_confd_monitoring', 'ConfdState.Internal.Cdb.Client.Type',
        '''The type of client: 'inactive' is a client connection without
any specific state. 'client' means that the client has an
active session towards a datastore. A 'subscriber' has made
one or more subscriptions. 'waiting' means that the client is
waiting for completion of a call such as cdb_wait_start().''',
        {
            'inactive':'inactive',
            'client':'client',
            'subscriber':'subscriber',
            'waiting':'waiting',
        }, 'tailf-common-monitoring', _yang_ns.NAMESPACE_LOOKUP['tailf-common-monitoring']),
    'ConfdState.Internal.Cdb.Client' : {
        'meta_info' : _MetaInfoClass('ConfdState.Internal.Cdb.Client', REFERENCE_LIST,
            ''' ''',
            False, 
            [
            _MetaInfoClassMember('name', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                The client name.
                ''',
                'name',
                'tailf-confd-monitoring', False, is_config=False),
            _MetaInfoClassMember('info', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                Additional information about the client obtained at connect
                time. If present, it consists of client PID and socket file
                descriptor number.
                ''',
                'info',
                'tailf-confd-monitoring', False, is_config=False),
            _MetaInfoClassMember('type', REFERENCE_ENUM_CLASS, 'Type', 'enumeration',
                'ydk.models.cisco_ios_xr.tailf_confd_monitoring', 'ConfdState.Internal.Cdb.Client.Type',
                [], [],
                '''                The type of client: 'inactive' is a client connection without
                any specific state. 'client' means that the client has an
                active session towards a datastore. A 'subscriber' has made
                one or more subscriptions. 'waiting' means that the client is
                waiting for completion of a call such as cdb_wait_start().
                ''',
                'type',
                'tailf-confd-monitoring', False, is_config=False),
            _MetaInfoClassMember('datastore', REFERENCE_UNION, 'str', 'union',
                None, None,
                [], [],
                '''                The name of the datastore when 'type' = 'client'. The value
                'pre_commit_running' is the 'pseudo' datastore representing
                'running' before a commit.
                ''',
                'datastore',
                'tailf-confd-monitoring', False, [
                    _MetaInfoClassMember('datastore', REFERENCE_ENUM_CLASS, 'ConfdState.Internal.DatastoreName', 'datastore-name',
                        'ydk.models.cisco_ios_xr.tailf_confd_monitoring', 'ConfdState.Internal.DatastoreName',
                        [], [],
                        '''                        The name of the datastore when 'type' = 'client'. The value
                        'pre_commit_running' is the 'pseudo' datastore representing
                        'running' before a commit.
                        ''',
                        'datastore',
                        'tailf-confd-monitoring', False, is_config=False),
                    _MetaInfoClassMember('datastore', REFERENCE_ENUM_CLASS, 'ConfdState.Internal.Cdb.Client.Datastore', 'enumeration',
                        'ydk.models.cisco_ios_xr.tailf_confd_monitoring', 'ConfdState.Internal.Cdb.Client.Datastore',
                        [], [],
                        '''                        The name of the datastore when 'type' = 'client'. The value
                        'pre_commit_running' is the 'pseudo' datastore representing
                        'running' before a commit.
                        ''',
                        'datastore',
                        'tailf-confd-monitoring', False, is_config=False),
                ], is_config=False),
            _MetaInfoClassMember('lock', REFERENCE_ENUM_CLASS, 'Lock', 'enumeration',
                'ydk.models.cisco_ios_xr.tailf_confd_monitoring', 'ConfdState.Internal.Cdb.Client.Lock',
                [], [],
                '''                Set when 'type' = 'client' and the client has requested or
                acquired a lock on the datastore. The 'pending-read' and
                'pending-subscription' values indicate that the client has
                requested but not yet acquired the corresponding lock.
                A 'read' lock is never taken for the 'operational' datastore,
                a 'subscription' lock is never taken for any other datastore
                than 'operational'.
                ''',
                'lock',
                'tailf-confd-monitoring', False, is_config=False),
            _MetaInfoClassMember('subscription', REFERENCE_LIST, 'Subscription', '',
                'ydk.models.cisco_ios_xr.tailf_confd_monitoring', 'ConfdState.Internal.Cdb.Client.Subscription',
                [], [],
                '''                ''',
                'subscription',
                'tailf-confd-monitoring', False, is_config=False),
            ],
            'tailf-confd-monitoring',
            'client',
            _yang_ns.NAMESPACE_LOOKUP['tailf-confd-monitoring'],
            'ydk.models.cisco_ios_xr.tailf_confd_monitoring',
            is_config=False,
        ),
    },
    'ConfdState.Internal.Cdb' : {
        'meta_info' : _MetaInfoClass('ConfdState.Internal.Cdb', REFERENCE_CLASS,
            ''' ''',
            False, 
            [
            _MetaInfoClassMember('datastore', REFERENCE_LIST, 'Datastore', '',
                'ydk.models.cisco_ios_xr.tailf_confd_monitoring', 'ConfdState.Internal.Cdb.Datastore',
                [], [],
                '''                ''',
                'datastore',
                'tailf-confd-monitoring', False, is_config=False),
            _MetaInfoClassMember('client', REFERENCE_LIST, 'Client', '',
                'ydk.models.cisco_ios_xr.tailf_confd_monitoring', 'ConfdState.Internal.Cdb.Client',
                [], [],
                '''                ''',
                'client',
                'tailf-confd-monitoring', False, is_config=False),
            ],
            'tailf-confd-monitoring',
            'cdb',
            _yang_ns.NAMESPACE_LOOKUP['tailf-confd-monitoring'],
            'ydk.models.cisco_ios_xr.tailf_confd_monitoring',
            is_config=False,
        ),
    },
    'ConfdState.Internal.DatastoreName' : _MetaInfoEnum('DatastoreName',
        'ydk.models.cisco_ios_xr.tailf_confd_monitoring', 'ConfdState.Internal.DatastoreName',
        '''Name of one of the datastores implemented by CDB.''',
        {
            'running':'running',
            'startup':'startup',
            'operational':'operational',
        }, 'tailf-common-monitoring', _yang_ns.NAMESPACE_LOOKUP['tailf-common-monitoring']),
    'ConfdState.Internal' : {
        'meta_info' : _MetaInfoClass('ConfdState.Internal', REFERENCE_CLASS,
            ''' ''',
            False, 
            [
            _MetaInfoClassMember('callpoints', REFERENCE_CLASS, 'Callpoints', '',
                'ydk.models.cisco_ios_xr.tailf_confd_monitoring', 'ConfdState.Internal.Callpoints',
                [], [],
                '''                ''',
                'callpoints',
                'tailf-confd-monitoring', False, is_config=False),
            _MetaInfoClassMember('cdb', REFERENCE_CLASS, 'Cdb', '',
                'ydk.models.cisco_ios_xr.tailf_confd_monitoring', 'ConfdState.Internal.Cdb',
                [], [],
                '''                ''',
                'cdb',
                'tailf-confd-monitoring', False, is_config=False),
            ],
            'tailf-confd-monitoring',
            'internal',
            _yang_ns.NAMESPACE_LOOKUP['tailf-confd-monitoring'],
            'ydk.models.cisco_ios_xr.tailf_confd_monitoring',
            is_config=False,
        ),
    },
    'ConfdState.DaemonStatus' : _MetaInfoEnum('DaemonStatus',
        'ydk.models.cisco_ios_xr.tailf_confd_monitoring', 'ConfdState.DaemonStatus',
        ''' ''',
        {
            'starting':'starting',
            'phase0':'phase0',
            'phase1':'phase1',
            'started':'started',
            'stopping':'stopping',
        }, 'tailf-common-monitoring', _yang_ns.NAMESPACE_LOOKUP['tailf-common-monitoring']),
    'ConfdState' : {
        'meta_info' : _MetaInfoClass('ConfdState', REFERENCE_CLASS,
            ''' ''',
            False, 
            [
            _MetaInfoClassMember('version', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                Tail-f product version number.
                ''',
                'version',
                'tailf-confd-monitoring', False, is_config=False),
            _MetaInfoClassMember('smp', REFERENCE_CLASS, 'Smp', '',
                'ydk.models.cisco_ios_xr.tailf_confd_monitoring', 'ConfdState.Smp',
                [], [],
                '''                ''',
                'smp',
                'tailf-confd-monitoring', False, is_config=False, is_presence=True),
            _MetaInfoClassMember('epoll', ATTRIBUTE, 'bool', 'boolean',
                None, None,
                [], [],
                '''                Indicates whether an enhanced poll() function is used
                ''',
                'epoll',
                'tailf-confd-monitoring', False, is_config=False),
            _MetaInfoClassMember('daemon-status', REFERENCE_ENUM_CLASS, 'DaemonStatus', 'enumeration',
                'ydk.models.cisco_ios_xr.tailf_confd_monitoring', 'ConfdState.DaemonStatus',
                [], [],
                '''                ''',
                'daemon_status',
                'tailf-confd-monitoring', False, is_config=False),
            _MetaInfoClassMember('read-only-mode', ATTRIBUTE, 'Empty', 'empty',
                None, None,
                [], [],
                '''                ''',
                'read_only_mode',
                'tailf-confd-monitoring', False, is_config=False),
            _MetaInfoClassMember('upgrade-mode', ATTRIBUTE, 'Empty', 'empty',
                None, None,
                [], [],
                '''                Note that if the node is in upgrade mode, it is not possible to
                get any information from the system over NETCONF.
                The error-app-tag will be upgrade-in-progress.
                
                Existing CLI sessions can get system information.
                ''',
                'upgrade_mode',
                'tailf-confd-monitoring', False, is_config=False),
            _MetaInfoClassMember('ha', REFERENCE_CLASS, 'Ha', '',
                'ydk.models.cisco_ios_xr.tailf_confd_monitoring', 'ConfdState.Ha',
                [], [],
                '''                ''',
                'ha',
                'tailf-confd-monitoring', False, is_config=False, is_presence=True),
            _MetaInfoClassMember('loaded-data-models', REFERENCE_CLASS, 'LoadedDataModels', '',
                'ydk.models.cisco_ios_xr.tailf_confd_monitoring', 'ConfdState.LoadedDataModels',
                [], [],
                '''                ''',
                'loaded_data_models',
                'tailf-confd-monitoring', False, is_config=False),
            _MetaInfoClassMember('netconf', REFERENCE_CLASS, 'Netconf', '',
                'ydk.models.cisco_ios_xr.tailf_confd_monitoring', 'ConfdState.Netconf',
                [], [],
                '''                ''',
                'netconf',
                'tailf-confd-monitoring', False, is_config=False, is_presence=True),
            _MetaInfoClassMember('cli', REFERENCE_CLASS, 'Cli', '',
                'ydk.models.cisco_ios_xr.tailf_confd_monitoring', 'ConfdState.Cli',
                [], [],
                '''                ''',
                'cli',
                'tailf-confd-monitoring', False, is_config=False, is_presence=True),
            _MetaInfoClassMember('webui', REFERENCE_CLASS, 'Webui', '',
                'ydk.models.cisco_ios_xr.tailf_confd_monitoring', 'ConfdState.Webui',
                [], [],
                '''                ''',
                'webui',
                'tailf-confd-monitoring', False, is_config=False, is_presence=True),
            _MetaInfoClassMember('rest', REFERENCE_CLASS, 'Rest', '',
                'ydk.models.cisco_ios_xr.tailf_confd_monitoring', 'ConfdState.Rest',
                [], [],
                '''                ''',
                'rest',
                'tailf-confd-monitoring', False, is_config=False, is_presence=True),
            _MetaInfoClassMember('snmp', REFERENCE_CLASS, 'Snmp', '',
                'ydk.models.cisco_ios_xr.tailf_confd_monitoring', 'ConfdState.Snmp',
                [], [],
                '''                ''',
                'snmp',
                'tailf-confd-monitoring', False, is_config=False, is_presence=True),
            _MetaInfoClassMember('internal', REFERENCE_CLASS, 'Internal', '',
                'ydk.models.cisco_ios_xr.tailf_confd_monitoring', 'ConfdState.Internal',
                [], [],
                '''                ''',
                'internal',
                'tailf-confd-monitoring', False, is_config=False),
            ],
            'tailf-confd-monitoring',
            'confd-state',
            _yang_ns.NAMESPACE_LOOKUP['tailf-confd-monitoring'],
            'ydk.models.cisco_ios_xr.tailf_confd_monitoring',
            is_config=False,
        ),
    },
}
_meta_table['ConfdState.LoadedDataModels.DataModel']['meta_info'].parent =_meta_table['ConfdState.LoadedDataModels']['meta_info']
_meta_table['ConfdState.Netconf.Listen.Tcp']['meta_info'].parent =_meta_table['ConfdState.Netconf.Listen']['meta_info']
_meta_table['ConfdState.Netconf.Listen.Ssh']['meta_info'].parent =_meta_table['ConfdState.Netconf.Listen']['meta_info']
_meta_table['ConfdState.Netconf.Listen']['meta_info'].parent =_meta_table['ConfdState.Netconf']['meta_info']
_meta_table['ConfdState.Cli.Listen.Ssh']['meta_info'].parent =_meta_table['ConfdState.Cli.Listen']['meta_info']
_meta_table['ConfdState.Cli.Listen']['meta_info'].parent =_meta_table['ConfdState.Cli']['meta_info']
_meta_table['ConfdState.Webui.Listen.Tcp']['meta_info'].parent =_meta_table['ConfdState.Webui.Listen']['meta_info']
_meta_table['ConfdState.Webui.Listen.Ssl']['meta_info'].parent =_meta_table['ConfdState.Webui.Listen']['meta_info']
_meta_table['ConfdState.Webui.Listen']['meta_info'].parent =_meta_table['ConfdState.Webui']['meta_info']
_meta_table['ConfdState.Rest.Listen.Tcp']['meta_info'].parent =_meta_table['ConfdState.Rest.Listen']['meta_info']
_meta_table['ConfdState.Rest.Listen.Ssl']['meta_info'].parent =_meta_table['ConfdState.Rest.Listen']['meta_info']
_meta_table['ConfdState.Rest.Listen']['meta_info'].parent =_meta_table['ConfdState.Rest']['meta_info']
_meta_table['ConfdState.Snmp.Listen.Udp']['meta_info'].parent =_meta_table['ConfdState.Snmp.Listen']['meta_info']
_meta_table['ConfdState.Snmp.Listen']['meta_info'].parent =_meta_table['ConfdState.Snmp']['meta_info']
_meta_table['ConfdState.Snmp.Version']['meta_info'].parent =_meta_table['ConfdState.Snmp']['meta_info']
_meta_table['ConfdState.Internal.Callpoints.Callpoint.Range.Daemon']['meta_info'].parent =_meta_table['ConfdState.Internal.Callpoints.Callpoint.Range']['meta_info']
_meta_table['ConfdState.Internal.Callpoints.Callpoint.Daemon']['meta_info'].parent =_meta_table['ConfdState.Internal.Callpoints.Callpoint']['meta_info']
_meta_table['ConfdState.Internal.Callpoints.Callpoint.Range']['meta_info'].parent =_meta_table['ConfdState.Internal.Callpoints.Callpoint']['meta_info']
_meta_table['ConfdState.Internal.Callpoints.Validationpoint.Range.Daemon']['meta_info'].parent =_meta_table['ConfdState.Internal.Callpoints.Validationpoint.Range']['meta_info']
_meta_table['ConfdState.Internal.Callpoints.Validationpoint.Daemon']['meta_info'].parent =_meta_table['ConfdState.Internal.Callpoints.Validationpoint']['meta_info']
_meta_table['ConfdState.Internal.Callpoints.Validationpoint.Range']['meta_info'].parent =_meta_table['ConfdState.Internal.Callpoints.Validationpoint']['meta_info']
_meta_table['ConfdState.Internal.Callpoints.Actionpoint.Range.Daemon']['meta_info'].parent =_meta_table['ConfdState.Internal.Callpoints.Actionpoint.Range']['meta_info']
_meta_table['ConfdState.Internal.Callpoints.Actionpoint.Daemon']['meta_info'].parent =_meta_table['ConfdState.Internal.Callpoints.Actionpoint']['meta_info']
_meta_table['ConfdState.Internal.Callpoints.Actionpoint.Range']['meta_info'].parent =_meta_table['ConfdState.Internal.Callpoints.Actionpoint']['meta_info']
_meta_table['ConfdState.Internal.Callpoints.SnmpInformCallback.Range.Daemon']['meta_info'].parent =_meta_table['ConfdState.Internal.Callpoints.SnmpInformCallback.Range']['meta_info']
_meta_table['ConfdState.Internal.Callpoints.SnmpInformCallback.Daemon']['meta_info'].parent =_meta_table['ConfdState.Internal.Callpoints.SnmpInformCallback']['meta_info']
_meta_table['ConfdState.Internal.Callpoints.SnmpInformCallback.Range']['meta_info'].parent =_meta_table['ConfdState.Internal.Callpoints.SnmpInformCallback']['meta_info']
_meta_table['ConfdState.Internal.Callpoints.SnmpNotificationSubscription.Range.Daemon']['meta_info'].parent =_meta_table['ConfdState.Internal.Callpoints.SnmpNotificationSubscription.Range']['meta_info']
_meta_table['ConfdState.Internal.Callpoints.SnmpNotificationSubscription.Daemon']['meta_info'].parent =_meta_table['ConfdState.Internal.Callpoints.SnmpNotificationSubscription']['meta_info']
_meta_table['ConfdState.Internal.Callpoints.SnmpNotificationSubscription.Range']['meta_info'].parent =_meta_table['ConfdState.Internal.Callpoints.SnmpNotificationSubscription']['meta_info']
_meta_table['ConfdState.Internal.Callpoints.ErrorFormattingCallback.Range.Daemon']['meta_info'].parent =_meta_table['ConfdState.Internal.Callpoints.ErrorFormattingCallback.Range']['meta_info']
_meta_table['ConfdState.Internal.Callpoints.ErrorFormattingCallback.Daemon']['meta_info'].parent =_meta_table['ConfdState.Internal.Callpoints.ErrorFormattingCallback']['meta_info']
_meta_table['ConfdState.Internal.Callpoints.ErrorFormattingCallback.Range']['meta_info'].parent =_meta_table['ConfdState.Internal.Callpoints.ErrorFormattingCallback']['meta_info']
_meta_table['ConfdState.Internal.Callpoints.Typepoint.Range.Daemon']['meta_info'].parent =_meta_table['ConfdState.Internal.Callpoints.Typepoint.Range']['meta_info']
_meta_table['ConfdState.Internal.Callpoints.Typepoint.Daemon']['meta_info'].parent =_meta_table['ConfdState.Internal.Callpoints.Typepoint']['meta_info']
_meta_table['ConfdState.Internal.Callpoints.Typepoint.Range']['meta_info'].parent =_meta_table['ConfdState.Internal.Callpoints.Typepoint']['meta_info']
_meta_table['ConfdState.Internal.Callpoints.NotificationStreamReplay.Range.Daemon']['meta_info'].parent =_meta_table['ConfdState.Internal.Callpoints.NotificationStreamReplay.Range']['meta_info']
_meta_table['ConfdState.Internal.Callpoints.NotificationStreamReplay.Daemon']['meta_info'].parent =_meta_table['ConfdState.Internal.Callpoints.NotificationStreamReplay']['meta_info']
_meta_table['ConfdState.Internal.Callpoints.NotificationStreamReplay.Range']['meta_info'].parent =_meta_table['ConfdState.Internal.Callpoints.NotificationStreamReplay']['meta_info']
_meta_table['ConfdState.Internal.Callpoints.AuthenticationCallback.Range.Daemon']['meta_info'].parent =_meta_table['ConfdState.Internal.Callpoints.AuthenticationCallback.Range']['meta_info']
_meta_table['ConfdState.Internal.Callpoints.AuthenticationCallback.Daemon']['meta_info'].parent =_meta_table['ConfdState.Internal.Callpoints.AuthenticationCallback']['meta_info']
_meta_table['ConfdState.Internal.Callpoints.AuthenticationCallback.Range']['meta_info'].parent =_meta_table['ConfdState.Internal.Callpoints.AuthenticationCallback']['meta_info']
_meta_table['ConfdState.Internal.Callpoints.AuthorizationCallbacks.Range.Daemon']['meta_info'].parent =_meta_table['ConfdState.Internal.Callpoints.AuthorizationCallbacks.Range']['meta_info']
_meta_table['ConfdState.Internal.Callpoints.AuthorizationCallbacks.Daemon']['meta_info'].parent =_meta_table['ConfdState.Internal.Callpoints.AuthorizationCallbacks']['meta_info']
_meta_table['ConfdState.Internal.Callpoints.AuthorizationCallbacks.Range']['meta_info'].parent =_meta_table['ConfdState.Internal.Callpoints.AuthorizationCallbacks']['meta_info']
_meta_table['ConfdState.Internal.Callpoints.Callpoint']['meta_info'].parent =_meta_table['ConfdState.Internal.Callpoints']['meta_info']
_meta_table['ConfdState.Internal.Callpoints.Validationpoint']['meta_info'].parent =_meta_table['ConfdState.Internal.Callpoints']['meta_info']
_meta_table['ConfdState.Internal.Callpoints.Actionpoint']['meta_info'].parent =_meta_table['ConfdState.Internal.Callpoints']['meta_info']
_meta_table['ConfdState.Internal.Callpoints.SnmpInformCallback']['meta_info'].parent =_meta_table['ConfdState.Internal.Callpoints']['meta_info']
_meta_table['ConfdState.Internal.Callpoints.SnmpNotificationSubscription']['meta_info'].parent =_meta_table['ConfdState.Internal.Callpoints']['meta_info']
_meta_table['ConfdState.Internal.Callpoints.ErrorFormattingCallback']['meta_info'].parent =_meta_table['ConfdState.Internal.Callpoints']['meta_info']
_meta_table['ConfdState.Internal.Callpoints.Typepoint']['meta_info'].parent =_meta_table['ConfdState.Internal.Callpoints']['meta_info']
_meta_table['ConfdState.Internal.Callpoints.NotificationStreamReplay']['meta_info'].parent =_meta_table['ConfdState.Internal.Callpoints']['meta_info']
_meta_table['ConfdState.Internal.Callpoints.AuthenticationCallback']['meta_info'].parent =_meta_table['ConfdState.Internal.Callpoints']['meta_info']
_meta_table['ConfdState.Internal.Callpoints.AuthorizationCallbacks']['meta_info'].parent =_meta_table['ConfdState.Internal.Callpoints']['meta_info']
_meta_table['ConfdState.Internal.Cdb.Datastore.PendingSubscriptionSync.Notification']['meta_info'].parent =_meta_table['ConfdState.Internal.Cdb.Datastore.PendingSubscriptionSync']['meta_info']
_meta_table['ConfdState.Internal.Cdb.Datastore.PendingNotificationQueue.Notification']['meta_info'].parent =_meta_table['ConfdState.Internal.Cdb.Datastore.PendingNotificationQueue']['meta_info']
_meta_table['ConfdState.Internal.Cdb.Datastore.PendingSubscriptionSync']['meta_info'].parent =_meta_table['ConfdState.Internal.Cdb.Datastore']['meta_info']
_meta_table['ConfdState.Internal.Cdb.Datastore.PendingNotificationQueue']['meta_info'].parent =_meta_table['ConfdState.Internal.Cdb.Datastore']['meta_info']
_meta_table['ConfdState.Internal.Cdb.Client.Subscription']['meta_info'].parent =_meta_table['ConfdState.Internal.Cdb.Client']['meta_info']
_meta_table['ConfdState.Internal.Cdb.Datastore']['meta_info'].parent =_meta_table['ConfdState.Internal.Cdb']['meta_info']
_meta_table['ConfdState.Internal.Cdb.Client']['meta_info'].parent =_meta_table['ConfdState.Internal.Cdb']['meta_info']
_meta_table['ConfdState.Internal.Callpoints']['meta_info'].parent =_meta_table['ConfdState.Internal']['meta_info']
_meta_table['ConfdState.Internal.Cdb']['meta_info'].parent =_meta_table['ConfdState.Internal']['meta_info']
_meta_table['ConfdState.Smp']['meta_info'].parent =_meta_table['ConfdState']['meta_info']
_meta_table['ConfdState.Ha']['meta_info'].parent =_meta_table['ConfdState']['meta_info']
_meta_table['ConfdState.LoadedDataModels']['meta_info'].parent =_meta_table['ConfdState']['meta_info']
_meta_table['ConfdState.Netconf']['meta_info'].parent =_meta_table['ConfdState']['meta_info']
_meta_table['ConfdState.Cli']['meta_info'].parent =_meta_table['ConfdState']['meta_info']
_meta_table['ConfdState.Webui']['meta_info'].parent =_meta_table['ConfdState']['meta_info']
_meta_table['ConfdState.Rest']['meta_info'].parent =_meta_table['ConfdState']['meta_info']
_meta_table['ConfdState.Snmp']['meta_info'].parent =_meta_table['ConfdState']['meta_info']
_meta_table['ConfdState.Internal']['meta_info'].parent =_meta_table['ConfdState']['meta_info']
