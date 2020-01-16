from django.test import TestCase, RequestFactory

from django_magnificent_messages import messages, INFO, system_messages, notifications
from django_magnificent_messages.messages import MessageFailure
from django_magnificent_messages.notifications import NotificationFailure


class TestApiExceptions(TestCase):
    def setUp(self) -> None:
        self.rf = RequestFactory()

    def test_request_type(self):
        with self.assertRaisesMessage(TypeError, "add() argument must be an HttpRequest object, not 'object'."):
            messages.add(object(), INFO, "Test")
        with self.assertRaisesMessage(TypeError, "add() argument must be an HttpRequest object, not 'object'."):
            system_messages.add(object(), INFO, "Test")
        with self.assertRaisesMessage(TypeError, "add() argument must be an HttpRequest object, not 'object'."):
            notifications.add(object(), INFO, "Test")

    def test_no_middleware_no_silent(self):
        r = self.rf.get("/")
        with self.assertRaisesMessage(MessageFailure, 'You cannot add messages without installing '
                                                      'django_magnificent_messages.middleware.MessageMiddleware'):
            messages.add(r, INFO, "Test")
        with self.assertRaisesMessage(MessageFailure, 'You cannot add messages without installing '
                                                      'django_magnificent_messages.middleware.MessageMiddleware'):
            system_messages.add(r, INFO, "Test")
        with self.assertRaisesMessage(NotificationFailure, 'You cannot add notifications without installing '
                                                           'django_magnificent_messages.middleware.MessageMiddleware'):
            notifications.add(r, INFO, "Test")

    def test_no_middleware_silent(self):
        r = self.rf.get("/")
        messages.add(r, INFO, "Test", fail_silently=True)
        system_messages.add(r, INFO, "Test", fail_silently=True)
        notifications.add(r, INFO, "Test", fail_silently=True)

    def test_no_middleware_get(self):
        r = self.rf.get("/")

        self.assertEqual([], notifications.get(r))
        self.assertEqual([], messages.new(r))
        self.assertEqual([], messages.all(r))
        self.assertEqual([], messages.read(r))
        self.assertEqual([], messages.unread(r))
        self.assertEqual([], messages.archived(r))

    def test_no_middleware_count(self):
        r = self.rf.get("/")

        self.assertEqual(0, notifications.count(r))
        self.assertEqual(0, messages.new_count_update_last_checked(r))
        self.assertEqual(0, messages.new_count(r))
        self.assertEqual(0, messages.all_count(r))
        self.assertEqual(0, messages.read_count(r))
        self.assertEqual(0, messages.unread_count(r))
        self.assertEqual(0, messages.archived_count(r))
