import ioc
import django.test
from aorta.messaging import CommandMessage
from aorta.messaging.runner import MessageRunner

import iam.const
from iam.ext.django.models import Subject


class DisableSubjectTestCase(django.test.TestCase):
    fixtures = ["testusers"]

    @ioc.inject('commands', 'CommandHandlerProvider')
    def setUp(self, commands):
        super().setUp()
        self.runner = MessageRunner(commands)
        self.message = CommandMessage()
        self.subject = Subject.objects.get(key=iam.const.DEFAULT_USER1)

        self.message.set_object_type('unimatrix.iam.DisableSubject')
        self.message.body = {
            'subject': {'id': self.subject.id}
        }

    def test_command_disables_subject(self):
        self.assertTrue(not self.subject.disabled)
        self.assertEqual(self.runner.run(self.message), 1)

        subject = Subject.objects.get(pk=self.subject.pk)
        self.assertTrue(subject.disabled)
