from django.contrib.auth.models import Group, User

from django_magnificent_messages import constants
from django_magnificent_messages.models import Message


class TestMessagesMixin:
    """
    For message testing next situation is used:
        * There are 3 users (Alice, Bob and Carol) and two groups (group1 and group2)
        * Alice is in group1, Bob is in group1 and group2, Carol is not in any group
        * Alice sent message "Alice message to Bob" to Bob
        * Bob sent message "Bob message go group1" to group1
        * Carol sent two messages "Read message" and "Archived message" to alice and group2
        * Bob and Alice marked "Read message" as read
        * Bob and Alice archived "Archived message"

    This is situation with messages at the start of every test.

    All users checked theirs inboxes very long time ago
    """

    def create_test_messages(self):
        self.alice_message_to_bob = Message.objects.create(pk=1, level=constants.INFO, raw_text="Alice message to Bob",
                                                           author=self.alice, user_generated=True)
        self.alice_message_to_bob.sent_to_users.add(self.bob)

        self.bob_message_to_group1 = Message.objects.create(pk=2, level=constants.INFO, raw_text="Bob message go group1",
                                                            author=self.bob, user_generated=True)
        self.bob_message_to_group1.sent_to_groups.add(self.group1)

        self.read_message = Message.objects.create(pk=3, level=constants.INFO, raw_text="Read message", author=self.carol,
                                                   user_generated=True)
        self.read_message.sent_to_users.add(self.alice)
        self.read_message.sent_to_groups.add(self.group2)
        self.read_message.read_by.set([self.alice, self.bob])

        self.archived_message = Message.objects.create(pk=4, level=constants.INFO, raw_text="Archived message",
                                                       author=self.carol, user_generated=True)
        self.archived_message.sent_to_users.add(self.alice)
        self.archived_message.sent_to_groups.add(self.group2)
        self.archived_message.archived_by.set([self.alice, self.bob])

    def create_test_users(self):
        self.group1 = Group.objects.create(name="group1")
        self.group2 = Group.objects.create(name="group2")
        self.alice = User.objects.create_user('alice', 'lennon@thebeatles.com', 'password')
        self.bob = User.objects.create_user('bob', 'lennon@thebeatles.com', 'password')
        self.carol = User.objects.create_user('carol', 'lennon@thebeatles.com', 'password')
        self.alice.groups.set([self.group1])
        self.bob.groups.set([self.group1, self.group2])
