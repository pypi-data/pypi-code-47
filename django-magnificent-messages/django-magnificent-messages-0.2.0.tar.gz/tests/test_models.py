from django.contrib.auth.models import Group, User
from django.core.exceptions import ValidationError
from django.test import TestCase

from django_magnificent_messages import constants
from django_magnificent_messages.models import Message, MessageNotSentToUserError, Inbox
from tests.utils import TestMessagesMixin


class MessageModelTestCase(TestMessagesMixin, TestCase):
    def setUp(self) -> None:
        self.create_test_users()
        self.create_test_messages()

    def test_mark_read_to_you(self):
        self.alice_message_to_bob.mark_read(self.bob)
        self.assertEqual(1, self.alice_message_to_bob.read_by.count())
        self.assertIn(self.bob, self.alice_message_to_bob.read_by.all())

    def test_mark_read_to_your_group(self):
        self.bob_message_to_group1.mark_read(self.alice)
        self.assertEqual(1, self.bob_message_to_group1.read_by.count())
        self.assertIn(self.alice, self.bob_message_to_group1.read_by.all())

    def test_mark_read_not_to_you(self):
        with self.assertRaisesMessage(MessageNotSentToUserError,
                                      "<Message: 2> was not sent to user, who tried to mark it as read"):
            self.bob_message_to_group1.mark_read(self.carol)

    def test_archieve_to_you(self):
        self.alice_message_to_bob.archive(self.bob)
        self.assertEqual(1, self.alice_message_to_bob.archived_by.count())
        self.assertIn(self.bob, self.alice_message_to_bob.archived_by.all())

    def test_archive_to_your_group(self):
        self.bob_message_to_group1.archive(self.alice)
        self.assertEqual(1, self.bob_message_to_group1.archived_by.count())
        self.assertIn(self.alice, self.bob_message_to_group1.archived_by.all())

    def test_archive_not_to_you(self):
        with self.assertRaisesMessage(MessageNotSentToUserError,
                                      "<Message: 2> was not sent to user, who tried to archive"):
            self.bob_message_to_group1.archive(self.carol)

    def test_mark_unread_to_you(self):
        self.read_message.mark_unread(self.bob)
        self.assertNotIn(self.bob, self.read_message.read_by.all())

    def test_mark_unread_to_your_group(self):
        self.read_message.mark_unread(self.alice)
        self.assertNotIn(self.alice, self.bob_message_to_group1.read_by.all())

    def test_mark_unread_not_to_you(self):
        with self.assertRaisesMessage(MessageNotSentToUserError,
                                      "<Message: 3> was not sent to user, who tried to mark it as unread"):
            self.read_message.mark_unread(self.carol)

    def test_unarchive_to_you(self):
        self.archived_message.unarchive(self.bob)
        self.assertNotIn(self.bob, self.read_message.archived_by.all())

    def test_unarchive_to_your_group(self):
        self.archived_message.unarchive(self.alice)
        self.assertNotIn(self.alice, self.bob_message_to_group1.archived_by.all())

    def test_unarchive_not_to_you(self):
        with self.assertRaisesMessage(MessageNotSentToUserError,
                                      "<Message: 4> was not sent to user, who tried to unarchive"):
            self.archived_message.unarchive(self.carol)


class InboxModelTestCase(TestMessagesMixin, TestCase):
    def setUp(self) -> None:
        """
        Create messages and get user inboxes
        """
        self.create_test_users()
        self.create_test_messages()
        self.alice_inbox, _ = Inbox.objects.get_or_create(user=self.alice, main=True)
        self.bob_inbox, _ = Inbox.objects.get_or_create(user=self.bob, main=True)
        self.carol_inbox, _ = Inbox.objects.get_or_create(user=self.carol, main=True)

    def test_all_count(self):
        """
        Archived messages never counts, so
            * Alice has 2 messages ("Bob message go group1", "Read message")
            * Bob has 3 messages ("Alice message to Bob", "Bob message go group1", "Read message")
            * Carol has 0 messages
        """
        self.assertEqual(2, self.alice_inbox.all_count)
        self.assertEqual(3, self.bob_inbox.all_count)
        self.assertEqual(0, self.carol_inbox.all_count)

    def test_read_count(self):
        """
        Archived messages never counts, so
            * Alice and Bob have 1 read message ("Read message")
            * Carol has 0 messages
        """
        self.assertEqual(1, self.alice_inbox.read_count)
        self.assertEqual(1, self.bob_inbox.read_count)
        self.assertEqual(0, self.carol_inbox.read_count)

    def test_unread_count(self):
        """
        Archived messages never counts, so
            * Alice has 1 messages ("Bob message go group1")
            * Bob has 2 messages ("Alice message to Bob", "Bob message go group1")
            * Carol has 0 messages
        """
        self.assertEqual(1, self.alice_inbox.unread_count)
        self.assertEqual(2, self.bob_inbox.unread_count)
        self.assertEqual(0, self.carol_inbox.unread_count)

    def test_archived_count(self):
        """
        Bob and Alice have 1 archived message ("Archived message")
        """
        self.assertEqual(1, self.alice_inbox.archived_count)
        self.assertEqual(1, self.bob_inbox.archived_count)
        self.assertEqual(0, self.carol_inbox.archived_count)

    def test_new_count(self):
        """
        Archived messages never counts and users never checked their inboxes, so
            * Alice has 2 messages ("Bob message go group1", "Read message")
            * Bob has 3 messages ("Alice message to Bob", "Bob message go group1", "Read message")
            * Carol has 0 messages
        """
        self.assertEqual(2, self.alice_inbox.new_count)
        self.assertEqual(3, self.bob_inbox.new_count)
        self.assertEqual(0, self.carol_inbox.new_count)
        self.assertEqual(2, self.alice_inbox.new_count_update_last_checked)
        self.assertEqual(3, self.bob_inbox.new_count_update_last_checked)
        self.assertEqual(0, self.carol_inbox.new_count_update_last_checked)

    def test_alice_all(self):
        """
        Alice has 2 messages - "Bob message go group1", "Read message".
        Archived message should not be here.
        All other messages in system should not be in her inbox.
        """
        messages = list(self.alice_inbox.all)
        self.assertEqual(2, len(messages))
        self.assertIn(self.bob_message_to_group1, messages)
        self.assertIn(self.read_message, messages)
        self.assertNotIn(self.alice_message_to_bob, messages)
        self.assertNotIn(self.archived_message, messages)

    def test_alice_read(self):
        """
        Alice has 1 read message ("Read message")
        All other messages in system should not be here
        """
        messages = list(self.alice_inbox.read)
        self.assertEqual(1, len(messages))
        self.assertNotIn(self.bob_message_to_group1, messages)
        self.assertIn(self.read_message, messages)
        self.assertNotIn(self.alice_message_to_bob, messages)
        self.assertNotIn(self.archived_message, messages)

    def test_alice_unread(self):
        """
        Alice has 1 unread message ("Bob message go group1")
        Archived message should not be here.
        All other messages in system should not be here
        """
        messages = list(self.alice_inbox.unread)
        self.assertEqual(1, len(messages))
        self.assertIn(self.bob_message_to_group1, messages)
        self.assertNotIn(self.read_message, messages)
        self.assertNotIn(self.alice_message_to_bob, messages)
        self.assertNotIn(self.archived_message, messages)

    def test_alice_new(self):
        """
        Alice has never checked inbox, so all her messages other then "Archived message" should be here.
        """
        messages = list(self.alice_inbox.new)
        self.assertEqual(2, len(messages))
        self.assertIn(self.bob_message_to_group1, messages)
        self.assertIn(self.read_message, messages)
        self.assertNotIn(self.alice_message_to_bob, messages)
        self.assertNotIn(self.archived_message, messages)

    def test_bob_all(self):
        """
        Bob has 3 messages - "Alice message to Bob", "Bob message go group1", "Read message".
        Archived message should not be here.
        """
        messages = list(self.bob_inbox.all)
        self.assertEqual(3, len(messages))
        self.assertIn(self.bob_message_to_group1, messages)
        self.assertIn(self.read_message, messages)
        self.assertIn(self.alice_message_to_bob, messages)
        self.assertNotIn(self.archived_message, messages)

    def test_bob_read(self):
        """
        Bob has 1 read message ("Read message")
        All other messages in system should not be here
        """
        messages = list(self.bob_inbox.read)
        self.assertEqual(1, len(messages))
        self.assertNotIn(self.bob_message_to_group1, messages)
        self.assertIn(self.read_message, messages)
        self.assertNotIn(self.alice_message_to_bob, messages)
        self.assertNotIn(self.archived_message, messages)

    def test_bob_unread(self):
        """
        Alice has 2 unread message ("Alice message to Bob", "Bob message go group1")
        Archived message should not be here.
        All other messages in system should not be here
        """
        messages = list(self.bob_inbox.unread)
        self.assertEqual(2, len(messages))
        self.assertIn(self.bob_message_to_group1, messages)
        self.assertNotIn(self.read_message, messages)
        self.assertIn(self.alice_message_to_bob, messages)
        self.assertNotIn(self.archived_message, messages)

    def test_bob_new(self):
        """
        Bob has never checked inbox, so all his messages other then "Archived message" should be here.
        """
        messages = list(self.bob_inbox.new)
        self.assertEqual(3, len(messages))
        self.assertIn(self.bob_message_to_group1, messages)
        self.assertIn(self.read_message, messages)
        self.assertIn(self.alice_message_to_bob, messages)
        self.assertNotIn(self.archived_message, messages)

    def test_carol(self):
        """
        Carol has totally empty inbox
        """
        self.assertEqual(0, len(self.carol_inbox.all))
        self.assertEqual(0, len(self.carol_inbox.read))
        self.assertEqual(0, len(self.carol_inbox.unread))
        self.assertEqual(0, len(self.carol_inbox.archived))
        self.assertEqual(0, len(self.carol_inbox.new))

    def test_all_iterate_last_checked(self):
        """
        After iterate through all inbox.last_checked should increase
        """
        old_last_check = self.alice_inbox.last_checked
        # Emulate iterate
        messages = list(self.alice_inbox.all)
        self.assertGreater(self.alice_inbox.last_checked, old_last_check)

    def test_unread_iterate_last_checked(self):
        """
        After iterate through unread inbox.last_checked should increase
        """
        old_last_check = self.alice_inbox.last_checked
        # Emulate iterate
        messages = list(self.alice_inbox.unread)
        self.assertGreater(self.alice_inbox.last_checked, old_last_check)

    def test_new_iterate_last_checked(self):
        """
        After iterate through new inbox.last_checked should increase
        """
        old_last_check = self.alice_inbox.last_checked
        # Emulate iterate
        messages = list(self.alice_inbox.new)
        self.assertGreater(self.alice_inbox.last_checked, old_last_check)

    def test_read_iterate_last_checked(self):
        """
        After iterate through read inbox.last_checked should stay the same
        """
        old_last_check = self.alice_inbox.last_checked
        # Emulate iterate
        messages = list(self.alice_inbox.read)
        self.assertEqual(self.alice_inbox.last_checked, old_last_check)

    def test_archived_iterate_last_checked(self):
        """
        After iterate through archived inbox.last_checked should stay the same
        """
        old_last_check = self.alice_inbox.last_checked
        # Emulate iterate
        messages = list(self.alice_inbox.archived)
        self.assertEqual(self.alice_inbox.last_checked, old_last_check)

    def test_all_no_iterate_last_check(self):
        """
        All can be passed around as variable, but before we iterate over it, inbox.last_checked should stay the same
        """
        old_last_check = self.alice_inbox.last_checked
        # Assigment
        messages = self.alice_inbox.all
        self.assertEqual(self.alice_inbox.last_checked, old_last_check)

    def test_read_no_iterate_last_check(self):
        """
        Read can be passed around as variable, but before we iterate over it, inbox.last_checked should stay the same
        """
        old_last_check = self.alice_inbox.last_checked
        # Assigment
        messages = self.alice_inbox.read
        self.assertEqual(self.alice_inbox.last_checked, old_last_check)

    def test_unread_no_iterate_last_check(self):
        """
        Unread can be passed around as variable, but before we iterate over it, inbox.last_checked should stay the same
        """
        old_last_check = self.alice_inbox.last_checked
        # Assigment
        messages = self.alice_inbox.unread
        self.assertEqual(self.alice_inbox.last_checked, old_last_check)

    def test_archived_no_iterate_last_check(self):
        """
        Archived can be passed around as variable, but before we iterate over it, inbox.last_checked should stay
        the same
        """
        old_last_check = self.alice_inbox.last_checked
        # Assigment
        messages = self.alice_inbox.archived
        self.assertEqual(self.alice_inbox.last_checked, old_last_check)

    def test_new_no_iterate_last_check(self):
        """
        New can be passed around as variable, but before we iterate over it, inbox.last_checked should stay
        the same
        """
        old_last_check = self.alice_inbox.last_checked
        # Assigment
        messages = self.alice_inbox.new_count_update_last_checked
        self.assertGreater(self.alice_inbox.last_checked, old_last_check)

    def test_count_last_check(self):
        """
        All counts other then new_count_update_last_checked should not change inbox.last_checked
        """
        old_last_check = self.alice_inbox.last_checked
        c = self.alice_inbox.all_count
        self.assertEqual(old_last_check, self.alice_inbox.last_checked)
        c = self.alice_inbox.read_count
        self.assertEqual(old_last_check, self.alice_inbox.last_checked)
        c = self.alice_inbox.unread_count
        self.assertEqual(old_last_check, self.alice_inbox.last_checked)
        c = self.alice_inbox.archived_count
        self.assertEqual(old_last_check, self.alice_inbox.last_checked)
        c = self.alice_inbox.new_count
        self.assertEqual(old_last_check, self.alice_inbox.last_checked)

    def test_new_count_update_last_checked(self):
        """
        new_count_update_last_checked should change inbox.last_checked
        """
        old_last_check = self.alice_inbox.last_checked
        c = self.alice_inbox.all_count
        self.assertEqual(old_last_check, self.alice_inbox.last_checked)

    def test_new_after_check(self):
        """
        new should respect inbox.last_checked
        """
        # Emulate inbox check
        list(self.alice_inbox.all)

        # Right after inbox check user has no new messages
        self.assertEqual(0, self.alice_inbox.new_count)
        self.assertEqual(0, len(list(self.alice_inbox.new)))

        # New message
        new_message = Message.objects.create(level=constants.INFO, raw_text="Alice message to Bob",
                                             author=self.bob, user_generated=True)
        new_message.sent_to_users.add(self.alice)

        # Now user has 1 new message
        self.assertEqual(1, self.alice_inbox.new_count)
        new_messages = list(self.alice_inbox.new)
        self.assertEqual(1, len(new_messages))
        self.assertIn(new_message, new_messages)

    def test_subsequent_new_messages(self):
        """
        If multiple messages sent to user after his last inbox check, all this messages should be in inbox.new
        when user finally checks his inbox
        """
        # Emulate inbox check
        list(self.alice_inbox.all)

        messages = []
        for i in range(5):
            new_message = Message.objects.create(level=constants.INFO, raw_text="Message {0}".format(i + 1),
                                                 author=self.bob, user_generated=True)
            new_message.sent_to_users.add(self.alice)
            messages.append(new_message)
            self.assertEqual(i + 1, self.alice_inbox.new_count)

        self.assertEqual(5, self.alice_inbox.new_count)
        messages.reverse()
        self.assertSequenceEqual(messages, self.alice_inbox.new)

        self.assertEqual(0, self.alice_inbox.new_count)
        self.assertSequenceEqual([], self.alice_inbox.new)

    def test_create_multiple_main_inboxes(self):
        with self.assertRaisesMessage(ValidationError, "User alice already has main inbox"):
            Inbox.objects.create(user=self.alice, main=True)
