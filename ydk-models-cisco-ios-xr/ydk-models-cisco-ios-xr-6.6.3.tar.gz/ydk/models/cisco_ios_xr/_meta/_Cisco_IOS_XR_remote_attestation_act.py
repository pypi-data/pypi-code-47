
'''
This is auto-generated file,
which includes metadata for module Cisco_IOS_XR_remote_attestation_act
'''

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_LIST, REFERENCE_LEAFLIST, REFERENCE_BITS, REFERENCE_UNION
from ydk._core._dm_meta_info import REFERENCE_CLASS, REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, ANYXML_CLASS
from ydk._core._importer import _yang_ns

_meta_table = {
    'GetCertificate.Input' : {
        'meta_info' : _MetaInfoClass('GetCertificate.Input', REFERENCE_CLASS,
            ''' ''',
            False, 
            [
            _MetaInfoClassMember('nonce', ATTRIBUTE, 'str', 'binary',
                None, None,
                [(0, 64)], [],
                '''                Nonce to be included in the attested output
                to prevent replay attacks
                ''',
                'nonce',
                'Cisco-IOS-XR-remote-attestation-act', False),
            _MetaInfoClassMember('certificate-identifier', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                Certificate identifier
                ''',
                'certificate_identifier',
                'Cisco-IOS-XR-remote-attestation-act', False),
            _MetaInfoClassMember('location', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                In a distributed system get the data from a specific node
                identified by the location. If this field is not specified
                data associated with each node forming the system will be
                returned.
                ''',
                'location',
                'Cisco-IOS-XR-remote-attestation-act', False),
            ],
            'Cisco-IOS-XR-remote-attestation-act',
            'input',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-remote-attestation-act'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_remote_attestation_act',
        ),
    },
    'GetCertificate.Output.GetCertificateResponse.SystemCertificates.Certificates.Certificate' : {
        'meta_info' : _MetaInfoClass('GetCertificate.Output.GetCertificateResponse.SystemCertificates.Certificates.Certificate', REFERENCE_LIST,
            '''A X.509 certificate''',
            False, 
            [
            _MetaInfoClassMember('name', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                A node-unique certificate identifier
                ''',
                'name',
                'Cisco-IOS-XR-remote-attestation-act', True),
            _MetaInfoClassMember('value', ATTRIBUTE, 'str', 'binary',
                None, None,
                [], [],
                '''                Certificate content in DER format.
                ''',
                'value',
                'Cisco-IOS-XR-remote-attestation-act', False),
            ],
            'Cisco-IOS-XR-remote-attestation-act',
            'certificate',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-remote-attestation-act'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_remote_attestation_act',
        ),
    },
    'GetCertificate.Output.GetCertificateResponse.SystemCertificates.Certificates' : {
        'meta_info' : _MetaInfoClass('GetCertificate.Output.GetCertificateResponse.SystemCertificates.Certificates', REFERENCE_CLASS,
            '''Certificates chain associated with the certificate
being queried''',
            False, 
            [
            _MetaInfoClassMember('certificate', REFERENCE_LIST, 'Certificate', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_remote_attestation_act', 'GetCertificate.Output.GetCertificateResponse.SystemCertificates.Certificates.Certificate',
                [], [],
                '''                A X.509 certificate
                ''',
                'certificate',
                'Cisco-IOS-XR-remote-attestation-act', False),
            ],
            'Cisco-IOS-XR-remote-attestation-act',
            'certificates',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-remote-attestation-act'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_remote_attestation_act',
        ),
    },
    'GetCertificate.Output.GetCertificateResponse.SystemCertificates' : {
        'meta_info' : _MetaInfoClass('GetCertificate.Output.GetCertificateResponse.SystemCertificates', REFERENCE_LIST,
            '''Certificate data of a node in a distributed system
identified by the location''',
            False, 
            [
            _MetaInfoClassMember('node-location', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                Location of the node in the distributed system
                ''',
                'node_location',
                'Cisco-IOS-XR-remote-attestation-act', True),
            _MetaInfoClassMember('nonce', ATTRIBUTE, 'str', 'binary',
                None, None,
                [(0, 64)], [],
                '''                Nonce used for this output
                ''',
                'nonce',
                'Cisco-IOS-XR-remote-attestation-act', False),
            _MetaInfoClassMember('certificates', REFERENCE_CLASS, 'Certificates', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_remote_attestation_act', 'GetCertificate.Output.GetCertificateResponse.SystemCertificates.Certificates',
                [], [],
                '''                Certificates chain associated with the certificate
                being queried
                ''',
                'certificates',
                'Cisco-IOS-XR-remote-attestation-act', False),
            _MetaInfoClassMember('signature_version', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('0', '4294967295')], [],
                '''                Signature version designates
                the format of the signed data.
                ''',
                'signature_version',
                'Cisco-IOS-XR-remote-attestation-act', False),
            _MetaInfoClassMember('signature', ATTRIBUTE, 'str', 'binary',
                None, None,
                [], [],
                '''                The optional RSA or ECDSA signature across
                the certificates,the signature version and
                the input nonce.Signed data format is:
                Nonce || UINT32 signature version ||
                [Certificate included in the response in DER format].
                ''',
                'signature',
                'Cisco-IOS-XR-remote-attestation-act', False),
            ],
            'Cisco-IOS-XR-remote-attestation-act',
            'system-certificates',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-remote-attestation-act'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_remote_attestation_act',
        ),
    },
    'GetCertificate.Output.GetCertificateResponse' : {
        'meta_info' : _MetaInfoClass('GetCertificate.Output.GetCertificateResponse', REFERENCE_CLASS,
            ''' ''',
            False, 
            [
            _MetaInfoClassMember('system-certificates', REFERENCE_LIST, 'SystemCertificates', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_remote_attestation_act', 'GetCertificate.Output.GetCertificateResponse.SystemCertificates',
                [], [],
                '''                Certificate data of a node in a distributed system
                identified by the location
                ''',
                'system_certificates',
                'Cisco-IOS-XR-remote-attestation-act', False),
            ],
            'Cisco-IOS-XR-remote-attestation-act',
            'get-certificate-response',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-remote-attestation-act'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_remote_attestation_act',
        ),
    },
    'GetCertificate.Output' : {
        'meta_info' : _MetaInfoClass('GetCertificate.Output', REFERENCE_CLASS,
            ''' ''',
            False, 
            [
            _MetaInfoClassMember('get-certificate-response', REFERENCE_CLASS, 'GetCertificateResponse', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_remote_attestation_act', 'GetCertificate.Output.GetCertificateResponse',
                [], [],
                '''                ''',
                'get_certificate_response',
                'Cisco-IOS-XR-remote-attestation-act', False),
            ],
            'Cisco-IOS-XR-remote-attestation-act',
            'output',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-remote-attestation-act'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_remote_attestation_act',
        ),
    },
    'GetCertificate' : {
        'meta_info' : _MetaInfoClass('GetCertificate', REFERENCE_CLASS,
            '''Query certificate.
Returns certificate chain
associated with the queried certificate.
An optional nonce can be provided, that is then used to
return a signature over the certificate contents returned.''',
            False, 
            [
            _MetaInfoClassMember('input', REFERENCE_CLASS, 'Input', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_remote_attestation_act', 'GetCertificate.Input',
                [], [],
                '''                ''',
                'input',
                'Cisco-IOS-XR-remote-attestation-act', False),
            _MetaInfoClassMember('output', REFERENCE_CLASS, 'Output', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_remote_attestation_act', 'GetCertificate.Output',
                [], [],
                '''                ''',
                'output',
                'Cisco-IOS-XR-remote-attestation-act', False),
            ],
            'Cisco-IOS-XR-remote-attestation-act',
            'get-certificate',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-remote-attestation-act'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_remote_attestation_act',
        ),
    },
    'AttestPlatformConfigRegisters.Input' : {
        'meta_info' : _MetaInfoClass('AttestPlatformConfigRegisters.Input', REFERENCE_CLASS,
            ''' ''',
            False, 
            [
            _MetaInfoClassMember('pcr-index', REFERENCE_LEAFLIST, 'int', 'uint16',
                None, None,
                [('0', '65535')], [],
                '''                PCR register indices to be included in the attested output
                ''',
                'pcr_index',
                'Cisco-IOS-XR-remote-attestation-act', False, min_elements=1),
            _MetaInfoClassMember('nonce', ATTRIBUTE, 'str', 'binary',
                None, None,
                [(0, 64)], [],
                '''                Nonce to be included in the attested output
                to prevent replay attacks
                ''',
                'nonce',
                'Cisco-IOS-XR-remote-attestation-act', False),
            _MetaInfoClassMember('attestation-certificate-identifier', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                Identifier of the certificate to be used for attestation
                ''',
                'attestation_certificate_identifier',
                'Cisco-IOS-XR-remote-attestation-act', False),
            _MetaInfoClassMember('location', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                In a distributed system get the data from a specific node
                identified by the location. If this field is not specified
                data associated with each node forming the system will be
                returned.
                ''',
                'location',
                'Cisco-IOS-XR-remote-attestation-act', False),
            ],
            'Cisco-IOS-XR-remote-attestation-act',
            'input',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-remote-attestation-act'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_remote_attestation_act',
        ),
    },
    'AttestPlatformConfigRegisters.Output.PlatformConfigRegisters.NodeData.PCR' : {
        'meta_info' : _MetaInfoClass('AttestPlatformConfigRegisters.Output.PlatformConfigRegisters.NodeData.PCR', REFERENCE_LIST,
            '''List of requested PCR contents''',
            False, 
            [
            _MetaInfoClassMember('index', ATTRIBUTE, 'int', 'uint16',
                None, None,
                [('0', '65535')], [],
                '''                PCR index
                ''',
                'index',
                'Cisco-IOS-XR-remote-attestation-act', True),
            _MetaInfoClassMember('value', REFERENCE_LEAFLIST, 'int', 'uint8',
                None, None,
                [('0', '255')], [],
                '''                PCR register content
                ''',
                'value',
                'Cisco-IOS-XR-remote-attestation-act', False, max_elements=64, min_elements=20),
            ],
            'Cisco-IOS-XR-remote-attestation-act',
            'PCR',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-remote-attestation-act'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_remote_attestation_act',
        ),
    },
    'AttestPlatformConfigRegisters.Output.PlatformConfigRegisters.NodeData' : {
        'meta_info' : _MetaInfoClass('AttestPlatformConfigRegisters.Output.PlatformConfigRegisters.NodeData', REFERENCE_LIST,
            '''Certificate data of a node in a distributed system
identified by the location''',
            False, 
            [
            _MetaInfoClassMember('node-location', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                Location of the node in the distributed system
                ''',
                'node_location',
                'Cisco-IOS-XR-remote-attestation-act', True),
            _MetaInfoClassMember('up-time', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('0', '4294967295')], [],
                '''                Uptime in seconds of this node reporting its data
                ''',
                'up_time',
                'Cisco-IOS-XR-remote-attestation-act', False),
            _MetaInfoClassMember('PCR', REFERENCE_LIST, 'PCR', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_remote_attestation_act', 'AttestPlatformConfigRegisters.Output.PlatformConfigRegisters.NodeData.PCR',
                [], [],
                '''                List of requested PCR contents
                ''',
                'pcr',
                'Cisco-IOS-XR-remote-attestation-act', False),
            _MetaInfoClassMember('pcr-quote', ATTRIBUTE, 'str', 'binary',
                None, None,
                [], [],
                '''                TPM PCR Quote
                ''',
                'pcr_quote',
                'Cisco-IOS-XR-remote-attestation-act', False),
            _MetaInfoClassMember('pcr-quote-signature', ATTRIBUTE, 'str', 'binary',
                None, None,
                [], [],
                '''                PCR Quote signature using TPM-held
                ECC or RSA restricted key
                ''',
                'pcr_quote_signature',
                'Cisco-IOS-XR-remote-attestation-act', False),
            ],
            'Cisco-IOS-XR-remote-attestation-act',
            'node-data',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-remote-attestation-act'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_remote_attestation_act',
        ),
    },
    'AttestPlatformConfigRegisters.Output.PlatformConfigRegisters' : {
        'meta_info' : _MetaInfoClass('AttestPlatformConfigRegisters.Output.PlatformConfigRegisters', REFERENCE_CLASS,
            '''Attested Platform Config Register values''',
            False, 
            [
            _MetaInfoClassMember('nonce', ATTRIBUTE, 'str', 'binary',
                None, None,
                [(0, 64)], [],
                '''                Nonce used for this output
                ''',
                'nonce',
                'Cisco-IOS-XR-remote-attestation-act', False),
            _MetaInfoClassMember('node-data', REFERENCE_LIST, 'NodeData', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_remote_attestation_act', 'AttestPlatformConfigRegisters.Output.PlatformConfigRegisters.NodeData',
                [], [],
                '''                Certificate data of a node in a distributed system
                identified by the location
                ''',
                'node_data',
                'Cisco-IOS-XR-remote-attestation-act', False),
            ],
            'Cisco-IOS-XR-remote-attestation-act',
            'platform-config-registers',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-remote-attestation-act'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_remote_attestation_act',
        ),
    },
    'AttestPlatformConfigRegisters.Output' : {
        'meta_info' : _MetaInfoClass('AttestPlatformConfigRegisters.Output', REFERENCE_CLASS,
            ''' ''',
            False, 
            [
            _MetaInfoClassMember('platform-config-registers', REFERENCE_CLASS, 'PlatformConfigRegisters', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_remote_attestation_act', 'AttestPlatformConfigRegisters.Output.PlatformConfigRegisters',
                [], [],
                '''                Attested Platform Config Register values
                ''',
                'platform_config_registers',
                'Cisco-IOS-XR-remote-attestation-act', False),
            ],
            'Cisco-IOS-XR-remote-attestation-act',
            'output',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-remote-attestation-act'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_remote_attestation_act',
        ),
    },
    'AttestPlatformConfigRegisters' : {
        'meta_info' : _MetaInfoClass('AttestPlatformConfigRegisters', REFERENCE_CLASS,
            '''Attest Platform Configuration Register(PCRs)''',
            False, 
            [
            _MetaInfoClassMember('input', REFERENCE_CLASS, 'Input', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_remote_attestation_act', 'AttestPlatformConfigRegisters.Input',
                [], [],
                '''                ''',
                'input',
                'Cisco-IOS-XR-remote-attestation-act', False),
            _MetaInfoClassMember('output', REFERENCE_CLASS, 'Output', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_remote_attestation_act', 'AttestPlatformConfigRegisters.Output',
                [], [],
                '''                ''',
                'output',
                'Cisco-IOS-XR-remote-attestation-act', False),
            ],
            'Cisco-IOS-XR-remote-attestation-act',
            'attest-platform-config-registers',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-remote-attestation-act'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_remote_attestation_act',
        ),
    },
    'GetPlatformBootIntegrityEventLogs.Input' : {
        'meta_info' : _MetaInfoClass('GetPlatformBootIntegrityEventLogs.Input', REFERENCE_CLASS,
            ''' ''',
            False, 
            [
            _MetaInfoClassMember('location', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                In a distributed system get the data from a specific node
                identified by the location. If this field is not specified
                data associated with each node forming the system will be
                returned.
                ''',
                'location',
                'Cisco-IOS-XR-remote-attestation-act', False),
            _MetaInfoClassMember('start-event-number', ATTRIBUTE, 'int', 'uint64',
                None, None,
                [('0', '18446744073709551615')], [],
                '''                To filter event logs to be retrieved.
                - If set only events with sequence number
                greater than that specified in this argument
                will be returned.
                ''',
                'start_event_number',
                'Cisco-IOS-XR-remote-attestation-act', False),
            _MetaInfoClassMember('end-event-number', ATTRIBUTE, 'int', 'uint64',
                None, None,
                [('0', '18446744073709551615')], [],
                '''                To control event logs to be retrieved.
                - If set only events with sequence number
                in the range of start-event-number to end-event-number
                will be returned.
                ''',
                'end_event_number',
                'Cisco-IOS-XR-remote-attestation-act', False, has_must=True),
            ],
            'Cisco-IOS-XR-remote-attestation-act',
            'input',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-remote-attestation-act'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_remote_attestation_act',
        ),
    },
    'GetPlatformBootIntegrityEventLogs.Output.SystemBootIntegrity.NodeData.EventLog.DigestList.DigestHashAlgorithm' : _MetaInfoEnum('DigestHashAlgorithm',
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_remote_attestation_act', 'GetPlatformBootIntegrityEventLogs.Output.SystemBootIntegrity.NodeData.EventLog.DigestList.DigestHashAlgorithm',
        '''Algorithm for this digest''',
        {
            'SHA1':'SHA1',
            'SHA256':'SHA256',
            'SHA384':'SHA384',
            'SHA512':'SHA512',
        }, 'Cisco-IOS-XR-remote-attestation-act', _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-remote-attestation-act']),
    'GetPlatformBootIntegrityEventLogs.Output.SystemBootIntegrity.NodeData.EventLog.DigestList' : {
        'meta_info' : _MetaInfoClass('GetPlatformBootIntegrityEventLogs.Output.SystemBootIntegrity.NodeData.EventLog.DigestList', REFERENCE_LIST,
            '''Hash of event data''',
            False, 
            [
            _MetaInfoClassMember('digest-hash-algorithm', REFERENCE_ENUM_CLASS, 'DigestHashAlgorithm', 'enumeration',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_remote_attestation_act', 'GetPlatformBootIntegrityEventLogs.Output.SystemBootIntegrity.NodeData.EventLog.DigestList.DigestHashAlgorithm',
                [], [],
                '''                Algorithm for this digest
                ''',
                'digest_hash_algorithm',
                'Cisco-IOS-XR-remote-attestation-act', True),
            _MetaInfoClassMember('digest', ATTRIBUTE, 'str', 'binary',
                None, None,
                [], [],
                '''                The hash of the event data
                ''',
                'digest',
                'Cisco-IOS-XR-remote-attestation-act', False),
            ],
            'Cisco-IOS-XR-remote-attestation-act',
            'digest-list',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-remote-attestation-act'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_remote_attestation_act',
        ),
    },
    'GetPlatformBootIntegrityEventLogs.Output.SystemBootIntegrity.NodeData.EventLog' : {
        'meta_info' : _MetaInfoClass('GetPlatformBootIntegrityEventLogs.Output.SystemBootIntegrity.NodeData.EventLog', REFERENCE_LIST,
            '''Ordered list of TCG described event log
that extended the PCRs in the order they
were logged''',
            False, 
            [
            _MetaInfoClassMember('event-number', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('0', '4294967295')], [],
                '''                Unique event number of this event
                ''',
                'event_number',
                'Cisco-IOS-XR-remote-attestation-act', True),
            _MetaInfoClassMember('event-type', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('0', '4294967295')], [],
                '''                log event type
                ''',
                'event_type',
                'Cisco-IOS-XR-remote-attestation-act', False),
            _MetaInfoClassMember('pcr-index', ATTRIBUTE, 'int', 'uint16',
                None, None,
                [('0', '65535')], [],
                '''                Defines the PCR index that this event extended
                ''',
                'pcr_index',
                'Cisco-IOS-XR-remote-attestation-act', False),
            _MetaInfoClassMember('digest-list', REFERENCE_LIST, 'DigestList', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_remote_attestation_act', 'GetPlatformBootIntegrityEventLogs.Output.SystemBootIntegrity.NodeData.EventLog.DigestList',
                [], [],
                '''                Hash of event data
                ''',
                'digest_list',
                'Cisco-IOS-XR-remote-attestation-act', False),
            _MetaInfoClassMember('event-size', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('0', '4294967295')], [],
                '''                Size of the event data
                ''',
                'event_size',
                'Cisco-IOS-XR-remote-attestation-act', False),
            _MetaInfoClassMember('event-data', ATTRIBUTE, 'str', 'binary',
                None, None,
                [], [],
                '''                the event data size determined by event-size
                ''',
                'event_data',
                'Cisco-IOS-XR-remote-attestation-act', False),
            ],
            'Cisco-IOS-XR-remote-attestation-act',
            'event_log',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-remote-attestation-act'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_remote_attestation_act',
        ),
    },
    'GetPlatformBootIntegrityEventLogs.Output.SystemBootIntegrity.NodeData' : {
        'meta_info' : _MetaInfoClass('GetPlatformBootIntegrityEventLogs.Output.SystemBootIntegrity.NodeData', REFERENCE_LIST,
            '''Boot integrity event logs of a node in a distributed system
identified by the location''',
            False, 
            [
            _MetaInfoClassMember('node-location', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                Location of the node in the distributed system
                ''',
                'node_location',
                'Cisco-IOS-XR-remote-attestation-act', True),
            _MetaInfoClassMember('up-time', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('0', '4294967295')], [],
                '''                Uptime in seconds of this node reporting its data
                ''',
                'up_time',
                'Cisco-IOS-XR-remote-attestation-act', False),
            _MetaInfoClassMember('event_log', REFERENCE_LIST, 'EventLog', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_remote_attestation_act', 'GetPlatformBootIntegrityEventLogs.Output.SystemBootIntegrity.NodeData.EventLog',
                [], [],
                '''                Ordered list of TCG described event log
                that extended the PCRs in the order they
                were logged
                ''',
                'event_log',
                'Cisco-IOS-XR-remote-attestation-act', False),
            ],
            'Cisco-IOS-XR-remote-attestation-act',
            'node-data',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-remote-attestation-act'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_remote_attestation_act',
        ),
    },
    'GetPlatformBootIntegrityEventLogs.Output.SystemBootIntegrity' : {
        'meta_info' : _MetaInfoClass('GetPlatformBootIntegrityEventLogs.Output.SystemBootIntegrity', REFERENCE_CLASS,
            '''Boot integrity event logs''',
            False, 
            [
            _MetaInfoClassMember('node-data', REFERENCE_LIST, 'NodeData', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_remote_attestation_act', 'GetPlatformBootIntegrityEventLogs.Output.SystemBootIntegrity.NodeData',
                [], [],
                '''                Boot integrity event logs of a node in a distributed system
                identified by the location
                ''',
                'node_data',
                'Cisco-IOS-XR-remote-attestation-act', False),
            ],
            'Cisco-IOS-XR-remote-attestation-act',
            'system-boot-integrity',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-remote-attestation-act'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_remote_attestation_act',
        ),
    },
    'GetPlatformBootIntegrityEventLogs.Output' : {
        'meta_info' : _MetaInfoClass('GetPlatformBootIntegrityEventLogs.Output', REFERENCE_CLASS,
            ''' ''',
            False, 
            [
            _MetaInfoClassMember('system-boot-integrity', REFERENCE_CLASS, 'SystemBootIntegrity', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_remote_attestation_act', 'GetPlatformBootIntegrityEventLogs.Output.SystemBootIntegrity',
                [], [],
                '''                Boot integrity event logs
                ''',
                'system_boot_integrity',
                'Cisco-IOS-XR-remote-attestation-act', False),
            ],
            'Cisco-IOS-XR-remote-attestation-act',
            'output',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-remote-attestation-act'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_remote_attestation_act',
        ),
    },
    'GetPlatformBootIntegrityEventLogs' : {
        'meta_info' : _MetaInfoClass('GetPlatformBootIntegrityEventLogs', REFERENCE_CLASS,
            '''Get platform's boot integrity''',
            False, 
            [
            _MetaInfoClassMember('input', REFERENCE_CLASS, 'Input', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_remote_attestation_act', 'GetPlatformBootIntegrityEventLogs.Input',
                [], [],
                '''                ''',
                'input',
                'Cisco-IOS-XR-remote-attestation-act', False),
            _MetaInfoClassMember('output', REFERENCE_CLASS, 'Output', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_remote_attestation_act', 'GetPlatformBootIntegrityEventLogs.Output',
                [], [],
                '''                ''',
                'output',
                'Cisco-IOS-XR-remote-attestation-act', False),
            ],
            'Cisco-IOS-XR-remote-attestation-act',
            'get-platform-boot-integrity-event-logs',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-remote-attestation-act'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_remote_attestation_act',
        ),
    },
    'GetPlatformImaEventLogs.Input' : {
        'meta_info' : _MetaInfoClass('GetPlatformImaEventLogs.Input', REFERENCE_CLASS,
            ''' ''',
            False, 
            [
            _MetaInfoClassMember('location', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                In a distributed system get the data from a specific node
                identified by the location. If this field is not specified
                data associated with each node forming the system will be
                returned.
                ''',
                'location',
                'Cisco-IOS-XR-remote-attestation-act', False),
            _MetaInfoClassMember('start-event-number', ATTRIBUTE, 'int', 'uint64',
                None, None,
                [('0', '18446744073709551615')], [],
                '''                To filter event logs to be retrieved.
                - If set only events with sequence number
                greater than that specified in this argument
                will be returned.
                ''',
                'start_event_number',
                'Cisco-IOS-XR-remote-attestation-act', False),
            _MetaInfoClassMember('end-event-number', ATTRIBUTE, 'int', 'uint64',
                None, None,
                [('0', '18446744073709551615')], [],
                '''                To control event logs to be retrieved.
                - If set only events with sequence number
                in the range of start-event-number to end-event-number
                will be returned.
                ''',
                'end_event_number',
                'Cisco-IOS-XR-remote-attestation-act', False, has_must=True),
            ],
            'Cisco-IOS-XR-remote-attestation-act',
            'input',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-remote-attestation-act'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_remote_attestation_act',
        ),
    },
    'GetPlatformImaEventLogs.Output.SystemIma.NodeData.ImaEventLog' : {
        'meta_info' : _MetaInfoClass('GetPlatformImaEventLogs.Output.SystemIma.NodeData.ImaEventLog', REFERENCE_LIST,
            '''Ordered list of ima event logs by event-number''',
            False, 
            [
            _MetaInfoClassMember('event-number', ATTRIBUTE, 'int', 'uint64',
                None, None,
                [('0', '18446744073709551615')], [],
                '''                Unique number for this event for sequencing
                ''',
                'event_number',
                'Cisco-IOS-XR-remote-attestation-act', True),
            _MetaInfoClassMember('ima-template', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                Name of the template used for event
                for e.g. ima, ima-ng
                ''',
                'ima_template',
                'Cisco-IOS-XR-remote-attestation-act', False),
            _MetaInfoClassMember('filename-hint', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                File that was measured
                ''',
                'filename_hint',
                'Cisco-IOS-XR-remote-attestation-act', False),
            _MetaInfoClassMember('filedata-hash', ATTRIBUTE, 'str', 'binary',
                None, None,
                [], [],
                '''                Hash of filedata
                ''',
                'filedata_hash',
                'Cisco-IOS-XR-remote-attestation-act', False),
            _MetaInfoClassMember('template-hash-algorithm', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                Algorithm used for template-hash
                ''',
                'template_hash_algorithm',
                'Cisco-IOS-XR-remote-attestation-act', False),
            _MetaInfoClassMember('template-hash', ATTRIBUTE, 'str', 'binary',
                None, None,
                [], [],
                '''                 hash(filedata-hash, filename-hint)
                ''',
                'template_hash',
                'Cisco-IOS-XR-remote-attestation-act', False),
            _MetaInfoClassMember('pcr-index', ATTRIBUTE, 'int', 'uint16',
                None, None,
                [('0', '65535')], [],
                '''                Defines the PCR index that this event extended
                ''',
                'pcr_index',
                'Cisco-IOS-XR-remote-attestation-act', False),
            _MetaInfoClassMember('signature', ATTRIBUTE, 'str', 'binary',
                None, None,
                [], [],
                '''                The file signature
                ''',
                'signature',
                'Cisco-IOS-XR-remote-attestation-act', False),
            ],
            'Cisco-IOS-XR-remote-attestation-act',
            'ima-event-log',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-remote-attestation-act'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_remote_attestation_act',
        ),
    },
    'GetPlatformImaEventLogs.Output.SystemIma.NodeData' : {
        'meta_info' : _MetaInfoClass('GetPlatformImaEventLogs.Output.SystemIma.NodeData', REFERENCE_LIST,
            '''IMA event logs of a node in a distributed system
identified by the location''',
            False, 
            [
            _MetaInfoClassMember('node-location', ATTRIBUTE, 'str', 'string',
                None, None,
                [], [],
                '''                Location of the node in the distributed system
                ''',
                'node_location',
                'Cisco-IOS-XR-remote-attestation-act', True),
            _MetaInfoClassMember('up-time', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('0', '4294967295')], [],
                '''                Uptime in seconds of this node reporting its data
                ''',
                'up_time',
                'Cisco-IOS-XR-remote-attestation-act', False),
            _MetaInfoClassMember('ima-event-log', REFERENCE_LIST, 'ImaEventLog', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_remote_attestation_act', 'GetPlatformImaEventLogs.Output.SystemIma.NodeData.ImaEventLog',
                [], [],
                '''                Ordered list of ima event logs by event-number
                ''',
                'ima_event_log',
                'Cisco-IOS-XR-remote-attestation-act', False),
            ],
            'Cisco-IOS-XR-remote-attestation-act',
            'node-data',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-remote-attestation-act'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_remote_attestation_act',
        ),
    },
    'GetPlatformImaEventLogs.Output.SystemIma' : {
        'meta_info' : _MetaInfoClass('GetPlatformImaEventLogs.Output.SystemIma', REFERENCE_CLASS,
            '''Runtime integrity measurement event logs''',
            False, 
            [
            _MetaInfoClassMember('node-data', REFERENCE_LIST, 'NodeData', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_remote_attestation_act', 'GetPlatformImaEventLogs.Output.SystemIma.NodeData',
                [], [],
                '''                IMA event logs of a node in a distributed system
                identified by the location
                ''',
                'node_data',
                'Cisco-IOS-XR-remote-attestation-act', False),
            ],
            'Cisco-IOS-XR-remote-attestation-act',
            'system-ima',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-remote-attestation-act'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_remote_attestation_act',
        ),
    },
    'GetPlatformImaEventLogs.Output' : {
        'meta_info' : _MetaInfoClass('GetPlatformImaEventLogs.Output', REFERENCE_CLASS,
            ''' ''',
            False, 
            [
            _MetaInfoClassMember('system-ima', REFERENCE_CLASS, 'SystemIma', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_remote_attestation_act', 'GetPlatformImaEventLogs.Output.SystemIma',
                [], [],
                '''                Runtime integrity measurement event logs
                ''',
                'system_ima',
                'Cisco-IOS-XR-remote-attestation-act', False),
            ],
            'Cisco-IOS-XR-remote-attestation-act',
            'output',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-remote-attestation-act'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_remote_attestation_act',
        ),
    },
    'GetPlatformImaEventLogs' : {
        'meta_info' : _MetaInfoClass('GetPlatformImaEventLogs', REFERENCE_CLASS,
            '''Get platform IMA event logs''',
            False, 
            [
            _MetaInfoClassMember('input', REFERENCE_CLASS, 'Input', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_remote_attestation_act', 'GetPlatformImaEventLogs.Input',
                [], [],
                '''                ''',
                'input',
                'Cisco-IOS-XR-remote-attestation-act', False),
            _MetaInfoClassMember('output', REFERENCE_CLASS, 'Output', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_remote_attestation_act', 'GetPlatformImaEventLogs.Output',
                [], [],
                '''                ''',
                'output',
                'Cisco-IOS-XR-remote-attestation-act', False),
            ],
            'Cisco-IOS-XR-remote-attestation-act',
            'get-platform-ima-event-logs',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-remote-attestation-act'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_remote_attestation_act',
        ),
    },
}
_meta_table['GetCertificate.Output.GetCertificateResponse.SystemCertificates.Certificates.Certificate']['meta_info'].parent =_meta_table['GetCertificate.Output.GetCertificateResponse.SystemCertificates.Certificates']['meta_info']
_meta_table['GetCertificate.Output.GetCertificateResponse.SystemCertificates.Certificates']['meta_info'].parent =_meta_table['GetCertificate.Output.GetCertificateResponse.SystemCertificates']['meta_info']
_meta_table['GetCertificate.Output.GetCertificateResponse.SystemCertificates']['meta_info'].parent =_meta_table['GetCertificate.Output.GetCertificateResponse']['meta_info']
_meta_table['GetCertificate.Output.GetCertificateResponse']['meta_info'].parent =_meta_table['GetCertificate.Output']['meta_info']
_meta_table['GetCertificate.Input']['meta_info'].parent =_meta_table['GetCertificate']['meta_info']
_meta_table['GetCertificate.Output']['meta_info'].parent =_meta_table['GetCertificate']['meta_info']
_meta_table['AttestPlatformConfigRegisters.Output.PlatformConfigRegisters.NodeData.PCR']['meta_info'].parent =_meta_table['AttestPlatformConfigRegisters.Output.PlatformConfigRegisters.NodeData']['meta_info']
_meta_table['AttestPlatformConfigRegisters.Output.PlatformConfigRegisters.NodeData']['meta_info'].parent =_meta_table['AttestPlatformConfigRegisters.Output.PlatformConfigRegisters']['meta_info']
_meta_table['AttestPlatformConfigRegisters.Output.PlatformConfigRegisters']['meta_info'].parent =_meta_table['AttestPlatformConfigRegisters.Output']['meta_info']
_meta_table['AttestPlatformConfigRegisters.Input']['meta_info'].parent =_meta_table['AttestPlatformConfigRegisters']['meta_info']
_meta_table['AttestPlatformConfigRegisters.Output']['meta_info'].parent =_meta_table['AttestPlatformConfigRegisters']['meta_info']
_meta_table['GetPlatformBootIntegrityEventLogs.Output.SystemBootIntegrity.NodeData.EventLog.DigestList']['meta_info'].parent =_meta_table['GetPlatformBootIntegrityEventLogs.Output.SystemBootIntegrity.NodeData.EventLog']['meta_info']
_meta_table['GetPlatformBootIntegrityEventLogs.Output.SystemBootIntegrity.NodeData.EventLog']['meta_info'].parent =_meta_table['GetPlatformBootIntegrityEventLogs.Output.SystemBootIntegrity.NodeData']['meta_info']
_meta_table['GetPlatformBootIntegrityEventLogs.Output.SystemBootIntegrity.NodeData']['meta_info'].parent =_meta_table['GetPlatformBootIntegrityEventLogs.Output.SystemBootIntegrity']['meta_info']
_meta_table['GetPlatformBootIntegrityEventLogs.Output.SystemBootIntegrity']['meta_info'].parent =_meta_table['GetPlatformBootIntegrityEventLogs.Output']['meta_info']
_meta_table['GetPlatformBootIntegrityEventLogs.Input']['meta_info'].parent =_meta_table['GetPlatformBootIntegrityEventLogs']['meta_info']
_meta_table['GetPlatformBootIntegrityEventLogs.Output']['meta_info'].parent =_meta_table['GetPlatformBootIntegrityEventLogs']['meta_info']
_meta_table['GetPlatformImaEventLogs.Output.SystemIma.NodeData.ImaEventLog']['meta_info'].parent =_meta_table['GetPlatformImaEventLogs.Output.SystemIma.NodeData']['meta_info']
_meta_table['GetPlatformImaEventLogs.Output.SystemIma.NodeData']['meta_info'].parent =_meta_table['GetPlatformImaEventLogs.Output.SystemIma']['meta_info']
_meta_table['GetPlatformImaEventLogs.Output.SystemIma']['meta_info'].parent =_meta_table['GetPlatformImaEventLogs.Output']['meta_info']
_meta_table['GetPlatformImaEventLogs.Input']['meta_info'].parent =_meta_table['GetPlatformImaEventLogs']['meta_info']
_meta_table['GetPlatformImaEventLogs.Output']['meta_info'].parent =_meta_table['GetPlatformImaEventLogs']['meta_info']
