from django.test import TestCase
from django.urls import reverse

from django_magnificent_messages.storage.message_storage.db import DatabaseStorage
from tests.message_storage_tests.base import BaseMessageStorageTestCases


class DatabaseStorageExistingTestCase(BaseMessageStorageTestCases.ExistingMessagesTestCase):
    STORAGE = DatabaseStorage

    def test_anonymous_api(self):
        """API should always return 0 messages for anonymous user"""
        show_url = reverse('messages_show', args=(1,))
        response = self.client.get(show_url)
        self.assertIn('dmm', response.context)
        self.assertEqual(0, response.context['dmm']['messages']['all_count'])
        self.assertEqual(0, response.context['dmm']['messages']['read_count'])
        self.assertEqual(0, response.context['dmm']['messages']['unread_count'])
        self.assertEqual(0, response.context['dmm']['messages']['archived_count'])
        self.assertEqual(0, response.context['dmm']['messages']['new_count'])
        self.assertEqual([], list(response.context['dmm']["messages"]["new"]))
        self.assertEqual([], list(response.context['dmm']["messages"]["all"]))
        self.assertEqual([], list(response.context['dmm']["messages"]["read"]))
        self.assertEqual([], list(response.context['dmm']["messages"]["unread"]))
        self.assertEqual([], list(response.context['dmm']["messages"]["archived"]))


class DatabaseStorageClearTestCase(BaseMessageStorageTestCases.ClearTestCase):
    STORAGE = DatabaseStorage
