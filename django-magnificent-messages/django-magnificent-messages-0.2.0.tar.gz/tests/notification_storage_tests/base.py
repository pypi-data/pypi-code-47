from django.http import HttpRequest, HttpResponse
from django.test import modify_settings, override_settings
from django.urls import reverse
from django.utils.translation import gettext_lazy

from django_magnificent_messages import constants, get_level, set_level, MessageBackend
from django_magnificent_messages.notifications import NotificationFailure
from django_magnificent_messages.storage.base import Message
from django_magnificent_messages.storage.notification_storage.base import BaseNotificationStorage


def add_level_messages(storage):
    """
    Add 7 messages from different levels (including a custom one) to a notification storage
    instance.
    """
    storage.add(constants.INFO, 'A generic info text')
    storage.add(29, 'Some custom level')
    storage.add(constants.PRIMARY, 'A primary text', extra='extra')
    storage.add(constants.SECONDARY, 'A secondary text', )
    storage.add(constants.WARNING, 'A warning')
    storage.add(constants.ERROR, 'An error')
    storage.add(constants.SUCCESS, 'This was a triumph.')


class BaseTests:
    storage_class = BaseNotificationStorage
    levels = {
        'SECONDARY': constants.SECONDARY,
        'PRIMARY': constants.PRIMARY,
        'INFO': constants.INFO,
        'SUCCESS': constants.SUCCESS,
        'WARNING': constants.WARNING,
        'ERROR': constants.ERROR,
    }

    def setUp(self):
        self.settings_override = override_settings(
            ROOT_URLCONF='tests.urls',
            MESSAGE_TAGS={},
            DMM_NOTIFICATION_STORAGE='%s.%s' % (self.storage_class.__module__, self.storage_class.__name__),
            SESSION_SERIALIZER='django.contrib.sessions.serializers.JSONSerializer',
        )
        self.settings_override.enable()

    def tearDown(self):
        self.settings_override.disable()

    def get_request(self):
        return HttpRequest()

    def get_response(self):
        return HttpResponse()

    def get_storage(self, data=None):
        """
        Return the notification storage, setting its loaded data to the ``data``
        argument.

        This method avoids the notification_storage ``_get`` method from getting called so
        that other parts of the notification storage can be tested independent of
        the retrieval logic.
        """
        storage = self.storage_class(self.get_request())
        storage._loaded_data = data or []
        return storage

    def test_add(self):
        storage = self.get_storage()
        self.assertFalse(storage.added_new)
        storage.add(constants.INFO, 'Test text 1')
        self.assertTrue(storage.added_new)
        storage.add(constants.INFO, 'Test text 2', extra="extra-tag")
        self.assertEqual(len(storage), 2)

    def test_add_lazy_translation(self):
        storage = self.get_storage()
        response = self.get_response()

        storage.add(constants.INFO, gettext_lazy('lazy text'))
        storage.update(response)

        storing = self.stored_notifications_count(storage, response)
        self.assertEqual(storing, 1)

    def test_no_update(self):
        storage = self.get_storage()
        response = self.get_response()
        storage.update(response)
        storing = self.stored_notifications_count(storage, response)
        self.assertEqual(storing, 0)

    def test_add_update(self):
        storage = self.get_storage()
        response = self.get_response()

        storage.add(constants.INFO, 'Test text 1')
        storage.add(constants.INFO, 'Test text 1', extra='tag')
        storage.update(response)

        storing = self.stored_notifications_count(storage, response)
        self.assertEqual(storing, 2)

    def test_existing_add_read_update(self):
        storage = self.get_existing_storage()
        response = self.get_response()

        storage.add(constants.INFO, 'Test text 3')
        list(storage)   # Simulates a read
        storage.update(response)

        storing = self.stored_notifications_count(storage, response)
        self.assertEqual(storing, 0)

    def test_existing_read_add_update(self):
        storage = self.get_existing_storage()
        response = self.get_response()

        list(storage)   # Simulates a read
        storage.add(constants.INFO, 'Test text 3')
        storage.update(response)

        storing = self.stored_notifications_count(storage, response)
        self.assertEqual(storing, 1)

    @override_settings(DMM_MINIMAL_LEVEL=0)
    def test_full_request_response_cycle(self):
        """
        With the message middleware enabled, messages are properly stored and
        retrieved across the full request/redirect/response cycle.
        """
        data = {
            'notifications': ['Test text %d' % x for x in range(5)],
        }
        show_url = reverse('show_notification')
        for level in ('secondary', 'primary', 'info', 'success', 'warning', 'error'):
            add_url = reverse('add-notification', args=(level,))
            response = self.client.post(add_url, data, follow=True)
            self.assertRedirects(response, show_url)
            self.assertIn('dmm', response.context)
            notifications = [Message(self.levels[level.upper()], msg) for msg in data['notifications']]
            self.assertEqual(list(response.context['dmm']['notifications']['all']), notifications)
            for msg in data['notifications']:
                self.assertContains(response, msg)

    @override_settings(DMM_MINIMAL_LEVEL=constants.SECONDARY)
    def test_with_template_response(self):
        data = {
            'messages': ['Test text %d' % x for x in range(5)],
        }
        show_url = reverse('show_template_response_notification')
        for level in self.levels:
            add_url = reverse('notifications_add_template_response', args=(level.lower(),))
            response = self.client.post(add_url, data, follow=True)
            self.assertRedirects(response, show_url)
            self.assertIn('dmm', response.context)
            for msg in data['messages']:
                self.assertContains(response, msg)

            # there shouldn't be any messages on second GET request
            response = self.client.get(show_url)
            for msg in data['messages']:
                self.assertNotContains(response, msg)

    @override_settings(DMM_MINIMAL_LEVEL=constants.SECONDARY)
    def test_multiple_posts(self):
        """
        Messages persist properly when multiple POSTs are made before a GET.
        """
        data = {
            'notifications': ['Test text %d' % x for x in range(5)],
        }
        show_url = reverse('show_notification')
        notifications = []
        for level in ('primary', 'info', 'success', 'warning', 'error'):
            notifications.extend(Message(self.levels[level.upper()], msg) for msg in data['notifications'])
            add_url = reverse('add-notification', args=(level,))
            self.client.post(add_url, data)
        response = self.client.get(show_url)
        self.assertIn('dmm', response.context)
        self.assertEqual(list(response.context['dmm']['notifications']['all']), notifications)
        for msg in data['notifications']:
            self.assertContains(response, msg)

    @modify_settings(
        INSTALLED_APPS={'remove': "django_magnificent_messages.apps.DjangoMagnificentMessagesConfig"},
        MIDDLEWARE={'remove': "django_magnificent_messages.middleware.MessageMiddleware"},
    )
    @override_settings(
        DMM_MINIMAL_LEVEL=constants.SECONDARY,
        TEMPLATES=[{
            'BACKEND': 'django.template.backends.django.DjangoTemplates',
            'DIRS': [],
            'APP_DIRS': True,
        }],
    )
    def test_middleware_disabled(self):
        """
        When the middleware is disabled, an exception is raised when one
        attempts to store a text.
        """
        data = {
            'notifications': ['Test text %d' % x for x in range(5)],
        }
        reverse('show_notification')
        for level in ('secondary', 'primary', 'info', 'success', 'warning', 'error'):
            add_url = reverse('add-notification', args=(level,))
            with self.assertRaises(NotificationFailure):
                self.client.post(add_url, data, follow=True)

    @modify_settings(
        INSTALLED_APPS={'remove': "django_magnificent_messages.apps.DjangoMagnificentMessagesConfig"},
        MIDDLEWARE={'remove': "django_magnificent_messages.middleware.MessageMiddleware"},
    )
    @override_settings(
        TEMPLATES=[{
            'BACKEND': 'django.template.backends.django.DjangoTemplates',
            'DIRS': [],
            'APP_DIRS': True,
        }],
    )
    def test_middleware_disabled_fail_silently(self):
        """
        When the middleware is disabled, an exception is not raised
        if 'fail_silently' is True.
        """
        data = {
            'messages': ['Test text %d' % x for x in range(5)],
            'fail_silently': True,
        }
        show_url = reverse('show_notification')
        for level in ('secondary', 'primary', 'info', 'success', 'warning', 'error'):
            add_url = reverse('add-notification', args=(level,))
            response = self.client.post(add_url, data, follow=True)
            self.assertRedirects(response, show_url)
            self.assertNotIn('dmm', response.context)

    def stored_notifications_count(self, storage, response):
        """
        Return the number of messages being stored after a
        ``notification_storage.update()`` call.
        """
        raise NotImplementedError('This method must be set by a subclass.')

    def test_get(self):
        raise NotImplementedError('This method must be set by a subclass.')

    def get_existing_storage(self):
        return self.get_storage([
            Message(constants.INFO, 'Test text 1'),
            Message(constants.INFO, 'Test text 2', extra_tags='tag'),
        ])

    def test_existing_read(self):
        """
        Reading the existing notification_storage doesn't cause the data to be lost.
        """
        storage = self.get_existing_storage()
        self.assertFalse(storage.used)
        # After iterating the notification_storage engine directly, the used flag is set.
        data = list(storage)
        self.assertTrue(storage.used)
        # The data does not disappear because it has been iterated.
        self.assertEqual(data, list(storage))

    def test_existing_add(self):
        storage = self.get_existing_storage()
        self.assertFalse(storage.added_new)
        storage.add(constants.INFO, 'Test text 3')
        self.assertTrue(storage.added_new)

    def test_default_level(self):
        # get_level works even with no notification_storage on the request.
        request = self.get_request()
        self.assertEqual(get_level(request), constants.INFO)

        # get_level returns the default level if it hasn't been set.
        storage = self.get_storage()
        request._messages = storage
        self.assertEqual(get_level(request), constants.INFO)

        # Only messages of sufficient level get recorded.
        add_level_messages(storage)
        self.assertEqual(len(storage), 4)

    def test_low_level(self):
        request = self.get_request()
        storage = self.storage_class(request)
        backend = MessageBackend(request)
        backend._notification_storage = storage
        request.dmm_backend = backend

        self.assertTrue(set_level(request, 5))
        self.assertEqual(get_level(request), 5)

        add_level_messages(storage)
        self.assertEqual(len(storage), 7)

    def test_high_level(self):
        request = self.get_request()
        storage = self.storage_class(request)
        backend = MessageBackend(request)
        backend._notification_storage = storage
        request.dmm_backend = backend

        self.assertTrue(set_level(request, 50))
        self.assertEqual(get_level(request), 50)

        add_level_messages(storage)
        self.assertEqual(len(storage), 2)

    @override_settings(DMM_MINIMAL_LEVEL=29)
    def test_settings_level(self):
        request = self.get_request()
        storage = self.storage_class(request)

        self.assertEqual(get_level(request), 29)

        add_level_messages(storage)
        self.assertEqual(len(storage), 5)

    def test_level_tag(self):
        storage = self.get_storage()
        storage.level = 0
        add_level_messages(storage)
        tags = [msg.level_tag for msg in storage]
        self.assertEqual(tags, ['info', '', 'primary', 'secondary',  'warning', 'danger', 'success'])

    @override_settings(DMM_LEVEL_TAGS={
        constants.INFO: 'info',
        constants.SECONDARY: '',
        constants.PRIMARY: '',
        constants.ERROR: 'bad',
        29: 'custom',
    })
    def test_custom_tags(self):
        storage = self.get_storage()
        storage.level = 0
        add_level_messages(storage)
        tags = [msg.level_tag for msg in storage]
        self.assertEqual(tags, ['info', 'custom', '', '', '', 'bad', ''])
