from django.test import TestCase, override_settings
from django.utils.translation import gettext_lazy as _

from django_magnificent_messages import constants
from django_magnificent_messages.storage.base import Message


class MessageTestCase(TestCase):
    def test_prepare_text(self):
        m = Message(1, _("Lazy text"))
        m.prepare()
        self.assertEqual("Lazy text", m.text)
        self.assertTrue(isinstance(m.text, str))

    def test_prepare_subject(self):
        m = Message(1, "Text", subject=_("Lazy text"))
        m.prepare()
        self.assertEqual("Lazy text", m.subject)
        self.assertTrue(isinstance(m.subject, str))

    def test_equal(self):
        m1 = Message(10, "Text", "Subject", extra=[1, 2, 3])
        m2 = Message(10, "Text", "Subject", extra=[1, 2, 3])
        self.assertEqual(m1, m2)

    def test_str(self):
        m = Message(20, "Message text", "Message subject")
        self.assertEqual("[Message subject] Message text", str(m))

    def test_secondary_level_tag(self):
        m = Message(constants.SECONDARY, "text", "subj")
        self.assertEqual("secondary", m.level_tag)

    def test_primary_level_tag(self):
        m = Message(constants.PRIMARY, "text", "subj")
        self.assertEqual("primary", m.level_tag)

    def test_info_level_tag(self):
        m = Message(constants.INFO, "text", "subj")
        self.assertEqual("info", m.level_tag)

    def test_success_level_tag(self):
        m = Message(constants.SUCCESS, "text", "subj")
        self.assertEqual("success", m.level_tag)

    def test_warning_level_tag(self):
        m = Message(constants.WARNING, "text", "subj")
        self.assertEqual("warning", m.level_tag)

    def test_error_level_tag(self):
        m = Message(constants.ERROR, "text", "subj")
        self.assertEqual("danger", m.level_tag)

    @override_settings(DMM_LEVEL_TAGS={27: 'custom_level'})
    def test_custom_level_tag(self):
        m = Message(27, "text", "subj")
        self.assertEqual("custom_level", m.level_tag)

    def test_to_dict(self):
        d = {
            "level": constants.INFO,
            "text": "Text",
            "subject": "Subject",
            "extra": {"1": ["a", "b"], "2": {3: 4, 5: 6}, "3": "aaaa", "4": 4}
        }
        m = Message(constants.INFO, "Text", "Subject", {"1": ["a", "b"], "2": {3: 4, 5: 6}, "3": "aaaa", "4": 4})
        self.assertEqual(d, m.to_dict())

    def test_from_dict(self):
        d = {
            "level": constants.INFO,
            "text": "Text",
            "subject": "Subject",
            "extra": {"1": ["a", "b"], "2": {3: 4, 5: 6}, "3": "aaaa", "4": 4}
        }
        m = Message(constants.INFO, "Text", "Subject", {"1": ["a", "b"], "2": {3: 4, 5: 6}, "3": "aaaa", "4": 4})
        self.assertEqual(Message(**d), m)

