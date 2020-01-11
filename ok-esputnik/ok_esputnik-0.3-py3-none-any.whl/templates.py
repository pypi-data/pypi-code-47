"""
Set of templates to transform data into format, acceptable by ESputnik API
"""

from functools import partial

from trafaret import Dict, String, List, Key, Enum, URL, Bool, Int, Any, Float

from esputnik.consts import (
    MEDIA_CHANNEL_TYPES,
    CONTACT_FIELDS_CHOICES,
    UNIQUENESS_CONTACT_CHOICES
)

__all__ = (
    'CONTACT',
    'CONTACTS',
    'CONTACT_SUBSCRIBE',
    'CONTACT_SEARCH',
    'CONTACT_UPLOAD',
    'EMAIL',
    'EMAIL_SEND',
    'EMAIL_SMARTSEND',
    'EVENT',
    'ORDER',
    'SMS',
    'VIBER',
    'prepare_contact',
    'prepare_contacts',
    'prepare_contact_subscribe',
    'prepare_contact_search',
    'prepare_contact_upload',
    'prepare_email',
    'prepare_event',
    'prepare_order',
    'prepare_send_email',
    'prepare_smartsend_email',
    'prepare_sms',
    'prepare_viber_message'
)

CHANNELS = List(
    Dict({
        Key('type') >> 'type': Enum(*MEDIA_CHANNEL_TYPES),
        Key('value') >> 'value': String,
    }, ignore_extra='*'),
    min_length=1
)

ADDRESS = Dict({
        Key('region') >> 'region': String,
        Key('town') >> 'town': String,
        Key('address') >> 'address': String,
        Key('postcode') >> 'postcode': String,
    }, ignore_extra='*'
)

FIELDS = List(
    Dict({
        Key('id') >> 'id': Int,
    }, ignore_extra='*'),
    min_length=1,
)

GROUPS = List(
    Dict({
        Key('id', optional=True) >> 'id': String,
        Key('name') >> 'name': String,
        Key('type', optional=True) >> 'type': String,
    }, ignore_extra='*'),
    min_length=1,
)


CONTACT = Dict({
    Key('first_name', optional=True) >> 'firstName': String,
    Key('last_name', optional=True) >> 'lastName': String,
    Key('channels') >> 'channels': CHANNELS,
    Key('address', optional=True) >> 'address': ADDRESS,
    Key('fields', optional=True) >> 'fields': FIELDS,
    Key('groups', optional=True) >> 'groups': GROUPS,
}, ignore_extra='*')


CONTACTS = Dict({
    Key('contacts') >> 'contacts': List(  # List of contacts (max 3000), which will be added/updated.
        Dict({
            Key('first_name', optional=True) >> 'firstName': String,
            Key('last_name', optional=True) >> 'lastName': String,
            Key('channels') >> 'channels': CHANNELS,
            Key('address', optional=True) >> 'address': ADDRESS,
            Key('fields', optional=True) >> 'fields': FIELDS,
            Key('groups', optional=True) >> 'groups': GROUPS,
        }, ignore_extra='*')
    ),
    Key('dedupe_on', default='email') >> 'dedupeOn': Enum(*UNIQUENESS_CONTACT_CHOICES),
    Key('field_id', optional=True) >> 'fieldId': Int,  # Custom field for determining uniqueness of the contact.
                                                       # Takes into account only if dedupeOnProperty set to fieldId.
    Key('contact_fields') >> 'contactFields': List(
        Enum(*CONTACT_FIELDS_CHOICES)
    ),  # List of contact's fields which will be updated.
    Key('custom_fields_ids', optional=True) >> 'customFieldsIDs': List(Int),  # List of custom fields IDs which
                                                                              # will be updated.
    Key('group_names') >> 'groupNames': List(String, min_length=1),  # List of segment names new/updated contacts
                                                                     # will be added to.

    Key('group_names_exclude', optional=True) >> 'groupNamesExclude': List(String, min_length=1),
    Key('restore_deleted', default=True) >> 'restoreDeleted': Bool,  # Add previously deleted contacts
    # Event type key identifier. Will be generated for each new contact.
    Key('event_key_for_new_contacts', optional=True) >> 'eventKeyForNewContacts': String
}, ignore_extra='*')


CONTACT_SUBSCRIBE = Dict({
    Key('contact') >> 'contact': Dict({
        Key('first_name', optional=True) >> 'firstName': String,
        Key('last_name', optional=True) >> 'lastName': String,
        Key('channels') >> 'channels': CHANNELS,
        Key('address', optional=True) >> 'address': ADDRESS,
        Key('fields', optional=True) >> 'fields': FIELDS,
        Key('address_book_id', optional=True) >> 'addressBookId': String,
        Key('id', optional=True) >> 'id': Int,
        Key('contact_key', optional=True) >> 'contactKey': String,
        Key('groups', optional=True) >> 'groups': GROUPS,
    }, ignore_extra='*'),
    Key('groups', optional=True) >> 'groups': List(String),
    Key('form_type', optional=True) >> 'formType': String,
}, ignore_extra='*')


CONTACT_SEARCH = Dict({
    Key('email', optional=True) >> 'email': String,
    Key('sms', optional=True) >> 'sms': String,
    Key('first_name', optional=True) >> 'firstname': String,
    Key('last_name', optional=True) >> 'lastname': String,
    Key('start_index', optional=True) >> 'startindex': Int,
    Key('max_rows', optional=True) >> 'maxrows': Int
}, ignore_extra='*')


CONTACT_UPLOAD = Dict({
    Key('dedupe_on') >> 'dedupeOn': Enum(*UNIQUENESS_CONTACT_CHOICES),
    Key('link') >> 'link': URL,
    Key('group_names') >> 'groupNames': List(String, min_length=1),
    Key('group_names_exclude', optional=True) >> 'groupNamesExclude': List(String, min_length=1),
    Key('restore_deleted', default=False) >> 'restoreDeleted': Bool,
    Key('event_key_for_new_contacts', optional=True) >> 'eventKeyForNewContacts': String
}, ignore_extra='*')


EMAIL = Dict({
    Key('from') >> 'from': String,
    Key('subject') >> 'subject': String,
    Key('html_text') >> 'htmlText': String,
    Key('plain_text') >> 'plainText': String,
    Key('emails') >> 'emails': List(String, min_length=1),
}, ignore_extra='*')

EMAIL_SEND = Dict({
    Key('params') >> 'params': List(
        Dict({
            Key('key') >> 'key': String,
            Key('value') >> 'value': String,
        }, ignore_extra='*'),
        min_length=1
    ),
    Key('recipients', optional=True) >> 'recipients': List(String, min_length=1),
    Key('group_id', optional=True) >> 'groupId': Int,
}, ignore_extra='*')


EMAIL_SMARTSEND = Dict({
    Key('recipients') >> 'recipients': List(
        Dict({
            Key('locator') >> 'locator': String,
            Key('json_param') >> 'jsonParam': String,
        }, ignore_extra='*'),
        min_length=1
    ),
}, ignore_extra='*')


EVENT = Dict({
    Key('event_type_key') >> 'eventTypeKey': String,
    Key('key_value') >> 'keyValue': String,
    Key('params') >> 'params': List(
        Dict({
            Key('name') >> 'name': String,
            Key('value') >> 'value': Any,
        }, ignore_extra='*'),
        min_length=1
    )
}, ignore_extra='*')


ORDER = Dict({
    Key('orders') >> 'orders': List(
        Dict({
            Key('id') >> 'externalOrderId': String,
            Key('user_id') >> 'externalCustomerId': String,
            Key('total_cost') >> 'totalCost': Float,  # decimal in docs
            Key('status', default='INITIALIZED') >> 'status': String,
            Key('date') >> 'date': Any,
            Key('email') >> 'email': String,
            Key('phone', optional=True) >> 'phone': String(allow_blank=True),
            Key('first_name', optional=True) >> 'firstName': String(allow_blank=True),
            Key('last_name', optional=True) >> 'lastName': String(allow_blank=True),
            Key('currency', optional=True, default='UAH') >> 'currency': String,
            Key('shipping', optional=True) >> 'shipping': Float,  # decimal in docs
            Key('discount', optional=True) >> 'discount': Float,  # decimal in docs
            Key('taxes', optional=True) >> 'taxes': Float,  # decimal in docs
            Key('order_url', optional=True) >> 'restoreUrl': String(allow_blank=True),
            Key('status_description', optional=True) >> 'statusDescription': String(allow_blank=True),
            Key('store_id', optional=True) >> 'storeId': String(allow_blank=True),
            Key('delivery_method', optional=True) >> 'deliveryMethod': String(allow_blank=True),
            Key('payment_method', optional=True) >> 'paymentMethod': String(allow_blank=True),
            Key('delivery_address', optional=True) >> 'deliveryAddress': String(allow_blank=True),
            Key('source', optional=True) >> 'source': String(allow_blank=True),
            Key('items') >> 'items': List(
                Dict({
                    Key('id') >> 'externalItemId': String,
                    Key('name') >> 'name': String,
                    Key('quantity') >> 'quantity': Int,
                    Key('cost') >> 'cost': Float,  # decimal in docs
                    Key('url') >> 'url': String,
                    Key('image_url') >> 'imageUrl': String,
                    Key('category') >> 'category': String,
                    Key('description', optional=True) >> 'description': String,
                }, ignore_extra='*'),
                min_length=1
            )
        }, ignore_extra='*'),
        min_length=1
    )
}, ignore_extra='*')


SMS = Dict({
    Key('from') >> 'from': String,
    Key('text') >> 'text': String,
    Key('phone_numbers') >> 'phoneNumbers': List(String, min_length=1),
    Key('group_id', optional=True) >> 'groupId': Int,
    Key('tags', optional=True) >> 'tags': List(String),  # List of tags to be assigned to the message.
}, ignore_extra='*')


VIBER = Dict({
    Key('text') >> 'text': String,
    Key('ttl_seconds', optional=True) >> 'ttlSeconds': Int,  # Message lifetime in seconds, the default is day.
    Key('img', optional=True) >> 'img': URL,  # Link to the picture.
    Key('caption') >> 'caption': String,  # Button name.
    Key('action') >> 'action': URL,  # Link to go when clicking on a picture or button.
    Key('ios_expirity_text') >> 'iosExpirityText': String,  # Notification that Viber user will receive if
                                                            # a message will delivered after the expiration
                                                            # of the message’s lifetime.
    Key('phone_numbers') >> 'phoneNumbers': List(String),
    Key('tags', optional=True) >> 'tags': List(String),  # List of tags to be assigned to the message.
    Key('group_id', optional=True) >> 'groupId': Int,
}, ignore_extra='*')


def _extract(template, *args, **kwargs):
    return template.transform(*args, **kwargs)


prepare_contact = partial(_extract, CONTACT)
prepare_contacts = partial(_extract, CONTACTS)
prepare_contact_subscribe = partial(_extract, CONTACT_SUBSCRIBE)
prepare_contact_search = partial(_extract, CONTACT_SEARCH)
prepare_contact_upload = partial(_extract, CONTACT_UPLOAD)
prepare_email = partial(_extract, EMAIL)
prepare_event = partial(_extract, EVENT)
prepare_order = partial(_extract, ORDER)
prepare_send_email = partial(_extract, EMAIL_SEND)
prepare_smartsend_email = partial(_extract, EMAIL_SMARTSEND)
prepare_sms = partial(_extract, SMS)
prepare_viber_message = partial(_extract, VIBER)
