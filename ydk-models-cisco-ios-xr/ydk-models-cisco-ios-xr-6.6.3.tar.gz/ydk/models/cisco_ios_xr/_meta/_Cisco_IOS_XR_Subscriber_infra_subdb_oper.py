
'''
This is auto-generated file,
which includes metadata for module Cisco_IOS_XR_Subscriber_infra_subdb_oper
'''

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_LIST, REFERENCE_LEAFLIST, REFERENCE_BITS, REFERENCE_UNION
from ydk._core._dm_meta_info import REFERENCE_CLASS, REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, ANYXML_CLASS
from ydk._core._importer import _yang_ns

_meta_table = {
    'SessionState' : _MetaInfoEnum('SessionState',
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_Subscriber_infra_subdb_oper', 'SessionState',
        '''Session states''',
        {
            'init':'init',
            'destroy':'destroy',
            'config-generate':'config_generate',
            'feature-registration-wait':'feature_registration_wait',
            'config-apply':'config_apply',
            'config-done':'config_done',
            'config-removed':'config_removed',
            'config-error':'config_error',
            'error':'error',
            'sync':'sync',
        }, 'Cisco-IOS-XR-Subscriber-infra-subdb-oper', _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-Subscriber-infra-subdb-oper']),
    'SubdbObjectTypeData' : _MetaInfoEnum('SubdbObjectTypeData',
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_Subscriber_infra_subdb_oper', 'SubdbObjectTypeData',
        '''Template types''',
        {
            'user-profile':'user_profile',
            'service-profile':'service_profile',
            'subscriber-service':'subscriber_service',
            'ppp':'ppp',
            'ip-subscriber':'ip_subscriber',
        }, 'Cisco-IOS-XR-Subscriber-infra-subdb-oper', _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-Subscriber-infra-subdb-oper']),
    'SubscriberDatabase.Nodes.Node.SubdbAssoc.Labels.Label.Template.AssociatedTemplate' : {
        'meta_info' : _MetaInfoClass('SubscriberDatabase.Nodes.Node.SubdbAssoc.Labels.Label.Template.AssociatedTemplate', REFERENCE_LIST,
            '''Associated templates''',
            False, 
            [
            _MetaInfoClassMember('template-type', REFERENCE_ENUM_CLASS, 'SubdbObjectTypeData', 'Subdb-object-type-data',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_Subscriber_infra_subdb_oper', 'SubdbObjectTypeData',
                [], [],
                '''                Template type
                ''',
                'template_type',
                'Cisco-IOS-XR-Subscriber-infra-subdb-oper', False, is_config=False),
            _MetaInfoClassMember('template-name', ATTRIBUTE, 'str', 'string',
                None, None,
                [(0, 65)], [],
                '''                Template name
                ''',
                'template_name',
                'Cisco-IOS-XR-Subscriber-infra-subdb-oper', False, is_config=False),
            _MetaInfoClassMember('varlist', ATTRIBUTE, 'str', 'string',
                None, None,
                [(0, 1000)], [],
                '''                Varlist
                ''',
                'varlist',
                'Cisco-IOS-XR-Subscriber-infra-subdb-oper', False, is_config=False),
            ],
            'Cisco-IOS-XR-Subscriber-infra-subdb-oper',
            'associated-template',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-Subscriber-infra-subdb-oper'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_Subscriber_infra_subdb_oper',
            is_config=False,
        ),
    },
    'SubscriberDatabase.Nodes.Node.SubdbAssoc.Labels.Label.Template' : {
        'meta_info' : _MetaInfoClass('SubscriberDatabase.Nodes.Node.SubdbAssoc.Labels.Label.Template', REFERENCE_CLASS,
            '''Subdb template''',
            False, 
            [
            _MetaInfoClassMember('associated-template', REFERENCE_LIST, 'AssociatedTemplate', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_Subscriber_infra_subdb_oper', 'SubscriberDatabase.Nodes.Node.SubdbAssoc.Labels.Label.Template.AssociatedTemplate',
                [], [],
                '''                Associated templates
                ''',
                'associated_template',
                'Cisco-IOS-XR-Subscriber-infra-subdb-oper', False, is_config=False),
            ],
            'Cisco-IOS-XR-Subscriber-infra-subdb-oper',
            'template',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-Subscriber-infra-subdb-oper'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_Subscriber_infra_subdb_oper',
            is_config=False,
        ),
    },
    'SubscriberDatabase.Nodes.Node.SubdbAssoc.Labels.Label' : {
        'meta_info' : _MetaInfoClass('SubscriberDatabase.Nodes.Node.SubdbAssoc.Labels.Label', REFERENCE_LIST,
            '''Association for a given subscriber label''',
            False, 
            [
            _MetaInfoClassMember('subscriber-label', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('0', '4294967295')], [],
                '''                Subscriber label
                ''',
                'subscriber_label',
                'Cisco-IOS-XR-Subscriber-infra-subdb-oper', True, is_config=False),
            _MetaInfoClassMember('template', REFERENCE_CLASS, 'Template', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_Subscriber_infra_subdb_oper', 'SubscriberDatabase.Nodes.Node.SubdbAssoc.Labels.Label.Template',
                [], [],
                '''                Subdb template
                ''',
                'template',
                'Cisco-IOS-XR-Subscriber-infra-subdb-oper', False, is_config=False),
            _MetaInfoClassMember('session-id', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('0', '4294967295')], [],
                '''                Session ID
                ''',
                'session_id',
                'Cisco-IOS-XR-Subscriber-infra-subdb-oper', False, is_config=False),
            _MetaInfoClassMember('interface-name', ATTRIBUTE, 'str', 'xr:Interface-name',
                None, None,
                [], [b'[a-zA-Z0-9._/-]+'],
                '''                Interface name
                ''',
                'interface_name',
                'Cisco-IOS-XR-Subscriber-infra-subdb-oper', False, is_config=False),
            _MetaInfoClassMember('associations', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('0', '4294967295')], [],
                '''                Association count which reflects number of
                entries in AssociatedTemplates
                ''',
                'associations',
                'Cisco-IOS-XR-Subscriber-infra-subdb-oper', False, is_config=False),
            _MetaInfoClassMember('varlist-id', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('0', '4294967295')], [],
                '''                Varlist Id
                ''',
                'varlist_id',
                'Cisco-IOS-XR-Subscriber-infra-subdb-oper', False, is_config=False),
            ],
            'Cisco-IOS-XR-Subscriber-infra-subdb-oper',
            'label',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-Subscriber-infra-subdb-oper'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_Subscriber_infra_subdb_oper',
            is_config=False,
        ),
    },
    'SubscriberDatabase.Nodes.Node.SubdbAssoc.Labels' : {
        'meta_info' : _MetaInfoClass('SubscriberDatabase.Nodes.Node.SubdbAssoc.Labels', REFERENCE_CLASS,
            '''List of associated subscriber labels''',
            False, 
            [
            _MetaInfoClassMember('label', REFERENCE_LIST, 'Label', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_Subscriber_infra_subdb_oper', 'SubscriberDatabase.Nodes.Node.SubdbAssoc.Labels.Label',
                [], [],
                '''                Association for a given subscriber label
                ''',
                'label',
                'Cisco-IOS-XR-Subscriber-infra-subdb-oper', False, is_config=False),
            ],
            'Cisco-IOS-XR-Subscriber-infra-subdb-oper',
            'labels',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-Subscriber-infra-subdb-oper'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_Subscriber_infra_subdb_oper',
            is_config=False,
        ),
    },
    'SubscriberDatabase.Nodes.Node.SubdbAssoc' : {
        'meta_info' : _MetaInfoClass('SubscriberDatabase.Nodes.Node.SubdbAssoc', REFERENCE_CLASS,
            '''Subscriber data for associated templates''',
            False, 
            [
            _MetaInfoClassMember('labels', REFERENCE_CLASS, 'Labels', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_Subscriber_infra_subdb_oper', 'SubscriberDatabase.Nodes.Node.SubdbAssoc.Labels',
                [], [],
                '''                List of associated subscriber labels
                ''',
                'labels',
                'Cisco-IOS-XR-Subscriber-infra-subdb-oper', False, is_config=False),
            ],
            'Cisco-IOS-XR-Subscriber-infra-subdb-oper',
            'subdb-assoc',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-Subscriber-infra-subdb-oper'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_Subscriber_infra_subdb_oper',
            is_config=False,
        ),
    },
    'SubscriberDatabase.Nodes.Node.Association.Labels.Label.Template.AssociatedTemplate' : {
        'meta_info' : _MetaInfoClass('SubscriberDatabase.Nodes.Node.Association.Labels.Label.Template.AssociatedTemplate', REFERENCE_LIST,
            '''Associated templates''',
            False, 
            [
            _MetaInfoClassMember('template-type', REFERENCE_ENUM_CLASS, 'SubdbObjectTypeData', 'Subdb-object-type-data',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_Subscriber_infra_subdb_oper', 'SubdbObjectTypeData',
                [], [],
                '''                Template type
                ''',
                'template_type',
                'Cisco-IOS-XR-Subscriber-infra-subdb-oper', False, is_config=False),
            _MetaInfoClassMember('template-name', ATTRIBUTE, 'str', 'string',
                None, None,
                [(0, 65)], [],
                '''                Template name
                ''',
                'template_name',
                'Cisco-IOS-XR-Subscriber-infra-subdb-oper', False, is_config=False),
            _MetaInfoClassMember('varlist', ATTRIBUTE, 'str', 'string',
                None, None,
                [(0, 1000)], [],
                '''                Varlist
                ''',
                'varlist',
                'Cisco-IOS-XR-Subscriber-infra-subdb-oper', False, is_config=False),
            ],
            'Cisco-IOS-XR-Subscriber-infra-subdb-oper',
            'associated-template',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-Subscriber-infra-subdb-oper'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_Subscriber_infra_subdb_oper',
            is_config=False,
        ),
    },
    'SubscriberDatabase.Nodes.Node.Association.Labels.Label.Template' : {
        'meta_info' : _MetaInfoClass('SubscriberDatabase.Nodes.Node.Association.Labels.Label.Template', REFERENCE_CLASS,
            '''Subdb template''',
            False, 
            [
            _MetaInfoClassMember('associated-template', REFERENCE_LIST, 'AssociatedTemplate', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_Subscriber_infra_subdb_oper', 'SubscriberDatabase.Nodes.Node.Association.Labels.Label.Template.AssociatedTemplate',
                [], [],
                '''                Associated templates
                ''',
                'associated_template',
                'Cisco-IOS-XR-Subscriber-infra-subdb-oper', False, is_config=False),
            ],
            'Cisco-IOS-XR-Subscriber-infra-subdb-oper',
            'template',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-Subscriber-infra-subdb-oper'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_Subscriber_infra_subdb_oper',
            is_config=False,
        ),
    },
    'SubscriberDatabase.Nodes.Node.Association.Labels.Label' : {
        'meta_info' : _MetaInfoClass('SubscriberDatabase.Nodes.Node.Association.Labels.Label', REFERENCE_LIST,
            '''Association for a given subscriber label''',
            False, 
            [
            _MetaInfoClassMember('subscriber-label', ATTRIBUTE, 'str', 'xr:Hex-integer',
                None, None,
                [], [b'[0-9a-fA-F]{1,8}'],
                '''                Subscriber label
                ''',
                'subscriber_label',
                'Cisco-IOS-XR-Subscriber-infra-subdb-oper', True, is_config=False),
            _MetaInfoClassMember('template', REFERENCE_CLASS, 'Template', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_Subscriber_infra_subdb_oper', 'SubscriberDatabase.Nodes.Node.Association.Labels.Label.Template',
                [], [],
                '''                Subdb template
                ''',
                'template',
                'Cisco-IOS-XR-Subscriber-infra-subdb-oper', False, is_config=False),
            _MetaInfoClassMember('session-id', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('0', '4294967295')], [],
                '''                Session ID
                ''',
                'session_id',
                'Cisco-IOS-XR-Subscriber-infra-subdb-oper', False, is_config=False),
            _MetaInfoClassMember('interface-name', ATTRIBUTE, 'str', 'xr:Interface-name',
                None, None,
                [], [b'[a-zA-Z0-9._/-]+'],
                '''                Interface name
                ''',
                'interface_name',
                'Cisco-IOS-XR-Subscriber-infra-subdb-oper', False, is_config=False),
            _MetaInfoClassMember('associations', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('0', '4294967295')], [],
                '''                Association count which reflects number of
                entries in AssociatedTemplates
                ''',
                'associations',
                'Cisco-IOS-XR-Subscriber-infra-subdb-oper', False, is_config=False),
            _MetaInfoClassMember('varlist-id', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('0', '4294967295')], [],
                '''                Varlist Id
                ''',
                'varlist_id',
                'Cisco-IOS-XR-Subscriber-infra-subdb-oper', False, is_config=False),
            ],
            'Cisco-IOS-XR-Subscriber-infra-subdb-oper',
            'label',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-Subscriber-infra-subdb-oper'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_Subscriber_infra_subdb_oper',
            is_config=False,
        ),
    },
    'SubscriberDatabase.Nodes.Node.Association.Labels' : {
        'meta_info' : _MetaInfoClass('SubscriberDatabase.Nodes.Node.Association.Labels', REFERENCE_CLASS,
            '''List of associated subscriber labels''',
            False, 
            [
            _MetaInfoClassMember('label', REFERENCE_LIST, 'Label', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_Subscriber_infra_subdb_oper', 'SubscriberDatabase.Nodes.Node.Association.Labels.Label',
                [], [],
                '''                Association for a given subscriber label
                ''',
                'label',
                'Cisco-IOS-XR-Subscriber-infra-subdb-oper', False, is_config=False),
            ],
            'Cisco-IOS-XR-Subscriber-infra-subdb-oper',
            'labels',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-Subscriber-infra-subdb-oper'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_Subscriber_infra_subdb_oper',
            is_config=False,
        ),
    },
    'SubscriberDatabase.Nodes.Node.Association' : {
        'meta_info' : _MetaInfoClass('SubscriberDatabase.Nodes.Node.Association', REFERENCE_CLASS,
            '''Subscriber data for associated templates''',
            False, 
            [
            _MetaInfoClassMember('labels', REFERENCE_CLASS, 'Labels', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_Subscriber_infra_subdb_oper', 'SubscriberDatabase.Nodes.Node.Association.Labels',
                [], [],
                '''                List of associated subscriber labels
                ''',
                'labels',
                'Cisco-IOS-XR-Subscriber-infra-subdb-oper', False, is_config=False),
            ],
            'Cisco-IOS-XR-Subscriber-infra-subdb-oper',
            'association',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-Subscriber-infra-subdb-oper'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_Subscriber_infra_subdb_oper',
            is_config=False,
        ),
    },
    'SubscriberDatabase.Nodes.Node.Summary' : {
        'meta_info' : _MetaInfoClass('SubscriberDatabase.Nodes.Node.Summary', REFERENCE_CLASS,
            '''Subscriber data for associated templates''',
            False, 
            [
            _MetaInfoClassMember('assoc-db-entries', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('0', '4294967295')], [],
                '''                Number of Entries in Association DB
                ''',
                'assoc_db_entries',
                'Cisco-IOS-XR-Subscriber-infra-subdb-oper', False, is_config=False),
            _MetaInfoClassMember('assoc-db-associations', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('0', '4294967295')], [],
                '''                Number of Associations in Association DB
                ''',
                'assoc_db_associations',
                'Cisco-IOS-XR-Subscriber-infra-subdb-oper', False, is_config=False),
            _MetaInfoClassMember('derived-db-entries', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('0', '4294967295')], [],
                '''                Number of Entries in Derived DB
                ''',
                'derived_db_entries',
                'Cisco-IOS-XR-Subscriber-infra-subdb-oper', False, is_config=False),
            _MetaInfoClassMember('config-db-entries', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('0', '4294967295')], [],
                '''                Number of Entries in Configuration DB
                ''',
                'config_db_entries',
                'Cisco-IOS-XR-Subscriber-infra-subdb-oper', False, is_config=False),
            _MetaInfoClassMember('interface-db-entries', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('0', '4294967295')], [],
                '''                Number of Entries in Interface DB
                ''',
                'interface_db_entries',
                'Cisco-IOS-XR-Subscriber-infra-subdb-oper', False, is_config=False),
            _MetaInfoClassMember('num-ipsub-dhcp', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('0', '4294967295')], [],
                '''                Number of IPSUB DHCP subscribers
                ''',
                'num_ipsub_dhcp',
                'Cisco-IOS-XR-Subscriber-infra-subdb-oper', False, is_config=False),
            _MetaInfoClassMember('num-ipsub-inband', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('0', '4294967295')], [],
                '''                Number of IPSUB Inband subscribers
                ''',
                'num_ipsub_inband',
                'Cisco-IOS-XR-Subscriber-infra-subdb-oper', False, is_config=False),
            _MetaInfoClassMember('num-pppoe', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('0', '4294967295')], [],
                '''                Number of PPPOE subscribers
                ''',
                'num_pppoe',
                'Cisco-IOS-XR-Subscriber-infra-subdb-oper', False, is_config=False),
            _MetaInfoClassMember('subdb-obj-counts-by-type', REFERENCE_LEAFLIST, 'int', 'uint32',
                None, None,
                [('0', '4294967295')], [],
                '''                The count of the various configuration objects
                by type
                ''',
                'subdb_obj_counts_by_type',
                'Cisco-IOS-XR-Subscriber-infra-subdb-oper', False, max_elements=16, is_config=False),
            _MetaInfoClassMember('num-subscribers-in-state', REFERENCE_LEAFLIST, 'int', 'uint32',
                None, None,
                [('0', '4294967295')], [],
                '''                Number of subscribers in the various states
                ''',
                'num_subscribers_in_state',
                'Cisco-IOS-XR-Subscriber-infra-subdb-oper', False, max_elements=32, is_config=False),
            _MetaInfoClassMember('num-transitions-through-state', REFERENCE_LEAFLIST, 'int', 'uint32',
                None, None,
                [('0', '4294967295')], [],
                '''                Cumulative number of transitions through the
                various states
                ''',
                'num_transitions_through_state',
                'Cisco-IOS-XR-Subscriber-infra-subdb-oper', False, max_elements=32, is_config=False),
            ],
            'Cisco-IOS-XR-Subscriber-infra-subdb-oper',
            'summary',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-Subscriber-infra-subdb-oper'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_Subscriber_infra_subdb_oper',
            is_config=False,
        ),
    },
    'SubscriberDatabase.Nodes.Node.Session.Labels.Label' : {
        'meta_info' : _MetaInfoClass('SubscriberDatabase.Nodes.Node.Session.Labels.Label', REFERENCE_LIST,
            '''Session information for a subscriber label''',
            False, 
            [
            _MetaInfoClassMember('subscriber-label', ATTRIBUTE, 'str', 'xr:Hex-integer',
                None, None,
                [], [b'[0-9a-fA-F]{1,8}'],
                '''                Subscriber label
                ''',
                'subscriber_label',
                'Cisco-IOS-XR-Subscriber-infra-subdb-oper', True, is_config=False),
            _MetaInfoClassMember('session-state', REFERENCE_ENUM_CLASS, 'SessionState', 'Session-state',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_Subscriber_infra_subdb_oper', 'SessionState',
                [], [],
                '''                Subscriber session state
                ''',
                'session_state',
                'Cisco-IOS-XR-Subscriber-infra-subdb-oper', False, is_config=False),
            _MetaInfoClassMember('activate-request-id', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('0', '4294967295')], [],
                '''                Activate request identifier
                ''',
                'activate_request_id',
                'Cisco-IOS-XR-Subscriber-infra-subdb-oper', False, is_config=False),
            _MetaInfoClassMember('transaction-id', ATTRIBUTE, 'int', 'int32',
                None, None,
                [('-2147483648', '2147483647')], [],
                '''                Transaction identifier associated with a
                particular 'produce_done' or 'produce_all_done'
                request  default value is 0xffffffff which
                represents 'None'
                ''',
                'transaction_id',
                'Cisco-IOS-XR-Subscriber-infra-subdb-oper', False, is_config=False),
            _MetaInfoClassMember('produce-done-request-id', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('0', '4294967295')], [],
                '''                Produce done request ID
                ''',
                'produce_done_request_id',
                'Cisco-IOS-XR-Subscriber-infra-subdb-oper', False, is_config=False),
            _MetaInfoClassMember('destroy-req-received', ATTRIBUTE, 'bool', 'boolean',
                None, None,
                [], [],
                '''                Flags indicating if a destroy request is
                received
                ''',
                'destroy_req_received',
                'Cisco-IOS-XR-Subscriber-infra-subdb-oper', False, is_config=False),
            _MetaInfoClassMember('destroy-request-id', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('0', '4294967295')], [],
                '''                Destroy request ID
                ''',
                'destroy_request_id',
                'Cisco-IOS-XR-Subscriber-infra-subdb-oper', False, is_config=False),
            _MetaInfoClassMember('is-config-changed', ATTRIBUTE, 'bool', 'boolean',
                None, None,
                [], [],
                '''                Is true if configuration change due to template
                change only and not due to a produce done
                request
                ''',
                'is_config_changed',
                'Cisco-IOS-XR-Subscriber-infra-subdb-oper', False, is_config=False),
            _MetaInfoClassMember('is-creator-gone', ATTRIBUTE, 'bool', 'boolean',
                None, None,
                [], [],
                '''                Is true if the creator of the connection is
                destroyed
                ''',
                'is_creator_gone',
                'Cisco-IOS-XR-Subscriber-infra-subdb-oper', False, is_config=False),
            _MetaInfoClassMember('is-delete-notify-done', ATTRIBUTE, 'bool', 'boolean',
                None, None,
                [], [],
                '''                Is true if the deleted features have all been
                notified and all 'apply done' ack messages have
                been received
                ''',
                'is_delete_notify_done',
                'Cisco-IOS-XR-Subscriber-infra-subdb-oper', False, is_config=False),
            _MetaInfoClassMember('add-modify-done', ATTRIBUTE, 'bool', 'boolean',
                None, None,
                [], [],
                '''                Is true if added/modified features have all been
                notified and all 'apply done' ack messages have
                been received
                ''',
                'add_modify_done',
                'Cisco-IOS-XR-Subscriber-infra-subdb-oper', False, is_config=False),
            _MetaInfoClassMember('is-rollback-needed', ATTRIBUTE, 'bool', 'boolean',
                None, None,
                [], [],
                '''                Is true if the subscriber should be rolled back
                to the configuration prior to this transaction
                when all the outstanding  backend programming
                interface requests are replied
                ''',
                'is_rollback_needed',
                'Cisco-IOS-XR-Subscriber-infra-subdb-oper', False, is_config=False),
            _MetaInfoClassMember('is-rollback-in-progress', ATTRIBUTE, 'bool', 'boolean',
                None, None,
                [], [],
                '''                Is true if subscriber's configuration is being
                rolled back
                ''',
                'is_rollback_in_progress',
                'Cisco-IOS-XR-Subscriber-infra-subdb-oper', False, is_config=False),
            _MetaInfoClassMember('is-server-restart-apply', ATTRIBUTE, 'bool', 'boolean',
                None, None,
                [], [],
                '''                Is true if the subscriber's configuration is
                being applied due to subscriber database server
                restart
                ''',
                'is_server_restart_apply',
                'Cisco-IOS-XR-Subscriber-infra-subdb-oper', False, is_config=False),
            _MetaInfoClassMember('is-rollback-performed', ATTRIBUTE, 'bool', 'boolean',
                None, None,
                [], [],
                '''                Is true if rollback has previously been
                performed for this subscriber
                ''',
                'is_rollback_performed',
                'Cisco-IOS-XR-Subscriber-infra-subdb-oper', False, is_config=False),
            _MetaInfoClassMember('repl-pending', ATTRIBUTE, 'bool', 'boolean',
                None, None,
                [], [],
                '''                Flags indicating if there is pending replication
                ''',
                'repl_pending',
                'Cisco-IOS-XR-Subscriber-infra-subdb-oper', False, is_config=False),
            _MetaInfoClassMember('activate-timer-running', ATTRIBUTE, 'bool', 'boolean',
                None, None,
                [], [],
                '''                Flags indicating if activate timer is running
                ''',
                'activate_timer_running',
                'Cisco-IOS-XR-Subscriber-infra-subdb-oper', False, is_config=False),
            _MetaInfoClassMember('apply-timer-running', ATTRIBUTE, 'bool', 'boolean',
                None, None,
                [], [],
                '''                Flags indicating if apply timer is running
                ''',
                'apply_timer_running',
                'Cisco-IOS-XR-Subscriber-infra-subdb-oper', False, is_config=False),
            _MetaInfoClassMember('event-queue-size', ATTRIBUTE, 'bool', 'boolean',
                None, None,
                [], [],
                '''                the current size of the event queue
                ''',
                'event_queue_size',
                'Cisco-IOS-XR-Subscriber-infra-subdb-oper', False, is_config=False),
            _MetaInfoClassMember('restarts', ATTRIBUTE, 'str', 'yang:hex-string',
                None, None,
                [], [b'([0-9a-fA-F]{2}(:[0-9a-fA-F]{2})*)?'],
                '''                Restart vector to keep track of the restart
                state
                ''',
                'restarts',
                'Cisco-IOS-XR-Subscriber-infra-subdb-oper', False, is_config=False),
            _MetaInfoClassMember('template-interface-id', ATTRIBUTE, 'int', 'uint32',
                None, None,
                [('0', '4294967295')], [],
                '''                Template Interface Identifier
                ''',
                'template_interface_id',
                'Cisco-IOS-XR-Subscriber-infra-subdb-oper', False, is_config=False),
            ],
            'Cisco-IOS-XR-Subscriber-infra-subdb-oper',
            'label',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-Subscriber-infra-subdb-oper'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_Subscriber_infra_subdb_oper',
            is_config=False,
        ),
    },
    'SubscriberDatabase.Nodes.Node.Session.Labels' : {
        'meta_info' : _MetaInfoClass('SubscriberDatabase.Nodes.Node.Session.Labels', REFERENCE_CLASS,
            '''Subscriber management list of subscriber
labels''',
            False, 
            [
            _MetaInfoClassMember('label', REFERENCE_LIST, 'Label', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_Subscriber_infra_subdb_oper', 'SubscriberDatabase.Nodes.Node.Session.Labels.Label',
                [], [],
                '''                Session information for a subscriber label
                ''',
                'label',
                'Cisco-IOS-XR-Subscriber-infra-subdb-oper', False, is_config=False),
            ],
            'Cisco-IOS-XR-Subscriber-infra-subdb-oper',
            'labels',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-Subscriber-infra-subdb-oper'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_Subscriber_infra_subdb_oper',
            is_config=False,
        ),
    },
    'SubscriberDatabase.Nodes.Node.Session' : {
        'meta_info' : _MetaInfoClass('SubscriberDatabase.Nodes.Node.Session', REFERENCE_CLASS,
            '''Subscriber management session information''',
            False, 
            [
            _MetaInfoClassMember('labels', REFERENCE_CLASS, 'Labels', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_Subscriber_infra_subdb_oper', 'SubscriberDatabase.Nodes.Node.Session.Labels',
                [], [],
                '''                Subscriber management list of subscriber
                labels
                ''',
                'labels',
                'Cisco-IOS-XR-Subscriber-infra-subdb-oper', False, is_config=False),
            ],
            'Cisco-IOS-XR-Subscriber-infra-subdb-oper',
            'session',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-Subscriber-infra-subdb-oper'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_Subscriber_infra_subdb_oper',
            is_config=False,
        ),
    },
    'SubscriberDatabase.Nodes.Node' : {
        'meta_info' : _MetaInfoClass('SubscriberDatabase.Nodes.Node', REFERENCE_LIST,
            '''Subscriber data for a particular node''',
            False, 
            [
            _MetaInfoClassMember('node-name', ATTRIBUTE, 'str', 'xr:Node-id',
                None, None,
                [], [b'([a-zA-Z0-9_]*\\d+/){1,2}([a-zA-Z0-9_]*\\d+)'],
                '''                Node name
                ''',
                'node_name',
                'Cisco-IOS-XR-Subscriber-infra-subdb-oper', True, is_config=False),
            _MetaInfoClassMember('subdb-assoc', REFERENCE_CLASS, 'SubdbAssoc', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_Subscriber_infra_subdb_oper', 'SubscriberDatabase.Nodes.Node.SubdbAssoc',
                [], [],
                '''                Subscriber data for associated templates
                ''',
                'subdb_assoc',
                'Cisco-IOS-XR-Subscriber-infra-subdb-oper', False, is_config=False),
            _MetaInfoClassMember('association', REFERENCE_CLASS, 'Association', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_Subscriber_infra_subdb_oper', 'SubscriberDatabase.Nodes.Node.Association',
                [], [],
                '''                Subscriber data for associated templates
                ''',
                'association',
                'Cisco-IOS-XR-Subscriber-infra-subdb-oper', False, is_config=False),
            _MetaInfoClassMember('summary', REFERENCE_CLASS, 'Summary', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_Subscriber_infra_subdb_oper', 'SubscriberDatabase.Nodes.Node.Summary',
                [], [],
                '''                Subscriber data for associated templates
                ''',
                'summary',
                'Cisco-IOS-XR-Subscriber-infra-subdb-oper', False, is_config=False),
            _MetaInfoClassMember('session', REFERENCE_CLASS, 'Session', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_Subscriber_infra_subdb_oper', 'SubscriberDatabase.Nodes.Node.Session',
                [], [],
                '''                Subscriber management session information
                ''',
                'session',
                'Cisco-IOS-XR-Subscriber-infra-subdb-oper', False, is_config=False),
            ],
            'Cisco-IOS-XR-Subscriber-infra-subdb-oper',
            'node',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-Subscriber-infra-subdb-oper'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_Subscriber_infra_subdb_oper',
            is_config=False,
        ),
    },
    'SubscriberDatabase.Nodes' : {
        'meta_info' : _MetaInfoClass('SubscriberDatabase.Nodes', REFERENCE_CLASS,
            '''List of nodes for which subscriber data is
collected''',
            False, 
            [
            _MetaInfoClassMember('node', REFERENCE_LIST, 'Node', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_Subscriber_infra_subdb_oper', 'SubscriberDatabase.Nodes.Node',
                [], [],
                '''                Subscriber data for a particular node
                ''',
                'node',
                'Cisco-IOS-XR-Subscriber-infra-subdb-oper', False, is_config=False),
            ],
            'Cisco-IOS-XR-Subscriber-infra-subdb-oper',
            'nodes',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-Subscriber-infra-subdb-oper'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_Subscriber_infra_subdb_oper',
            is_config=False,
        ),
    },
    'SubscriberDatabase' : {
        'meta_info' : _MetaInfoClass('SubscriberDatabase', REFERENCE_CLASS,
            '''Subscriber database operational data''',
            False, 
            [
            _MetaInfoClassMember('nodes', REFERENCE_CLASS, 'Nodes', '',
                'ydk.models.cisco_ios_xr.Cisco_IOS_XR_Subscriber_infra_subdb_oper', 'SubscriberDatabase.Nodes',
                [], [],
                '''                List of nodes for which subscriber data is
                collected
                ''',
                'nodes',
                'Cisco-IOS-XR-Subscriber-infra-subdb-oper', False, is_config=False),
            ],
            'Cisco-IOS-XR-Subscriber-infra-subdb-oper',
            'subscriber-database',
            _yang_ns.NAMESPACE_LOOKUP['Cisco-IOS-XR-Subscriber-infra-subdb-oper'],
            'ydk.models.cisco_ios_xr.Cisco_IOS_XR_Subscriber_infra_subdb_oper',
            is_config=False,
        ),
    },
}
_meta_table['SubscriberDatabase.Nodes.Node.SubdbAssoc.Labels.Label.Template.AssociatedTemplate']['meta_info'].parent =_meta_table['SubscriberDatabase.Nodes.Node.SubdbAssoc.Labels.Label.Template']['meta_info']
_meta_table['SubscriberDatabase.Nodes.Node.SubdbAssoc.Labels.Label.Template']['meta_info'].parent =_meta_table['SubscriberDatabase.Nodes.Node.SubdbAssoc.Labels.Label']['meta_info']
_meta_table['SubscriberDatabase.Nodes.Node.SubdbAssoc.Labels.Label']['meta_info'].parent =_meta_table['SubscriberDatabase.Nodes.Node.SubdbAssoc.Labels']['meta_info']
_meta_table['SubscriberDatabase.Nodes.Node.SubdbAssoc.Labels']['meta_info'].parent =_meta_table['SubscriberDatabase.Nodes.Node.SubdbAssoc']['meta_info']
_meta_table['SubscriberDatabase.Nodes.Node.Association.Labels.Label.Template.AssociatedTemplate']['meta_info'].parent =_meta_table['SubscriberDatabase.Nodes.Node.Association.Labels.Label.Template']['meta_info']
_meta_table['SubscriberDatabase.Nodes.Node.Association.Labels.Label.Template']['meta_info'].parent =_meta_table['SubscriberDatabase.Nodes.Node.Association.Labels.Label']['meta_info']
_meta_table['SubscriberDatabase.Nodes.Node.Association.Labels.Label']['meta_info'].parent =_meta_table['SubscriberDatabase.Nodes.Node.Association.Labels']['meta_info']
_meta_table['SubscriberDatabase.Nodes.Node.Association.Labels']['meta_info'].parent =_meta_table['SubscriberDatabase.Nodes.Node.Association']['meta_info']
_meta_table['SubscriberDatabase.Nodes.Node.Session.Labels.Label']['meta_info'].parent =_meta_table['SubscriberDatabase.Nodes.Node.Session.Labels']['meta_info']
_meta_table['SubscriberDatabase.Nodes.Node.Session.Labels']['meta_info'].parent =_meta_table['SubscriberDatabase.Nodes.Node.Session']['meta_info']
_meta_table['SubscriberDatabase.Nodes.Node.SubdbAssoc']['meta_info'].parent =_meta_table['SubscriberDatabase.Nodes.Node']['meta_info']
_meta_table['SubscriberDatabase.Nodes.Node.Association']['meta_info'].parent =_meta_table['SubscriberDatabase.Nodes.Node']['meta_info']
_meta_table['SubscriberDatabase.Nodes.Node.Summary']['meta_info'].parent =_meta_table['SubscriberDatabase.Nodes.Node']['meta_info']
_meta_table['SubscriberDatabase.Nodes.Node.Session']['meta_info'].parent =_meta_table['SubscriberDatabase.Nodes.Node']['meta_info']
_meta_table['SubscriberDatabase.Nodes.Node']['meta_info'].parent =_meta_table['SubscriberDatabase.Nodes']['meta_info']
_meta_table['SubscriberDatabase.Nodes']['meta_info'].parent =_meta_table['SubscriberDatabase']['meta_info']
