from django.contrib.sites.models import Site
from django.test import TestCase

from iam.ext.django.models import Subject
import iam.const


class BasicSubjectPermissionTestCase(TestCase):
    fixtures = ['testusers']

    def setUp(self):
        self.site = Site.objects.get(pk=iam.const.DEFAULT_SITE_ID)
        self.superuser = Subject.objects.get(
            key=iam.const.DEFAULT_SUPERUSER)
        self.user1 = Subject.objects.get(
            key=iam.const.DEFAULT_USER1)

    def test_subject_is_disabled_after_manager_invocation(self):
        self.assertTrue(not self.user1.disabled)
        Subject.objects.disable(pk=self.user1.pk)

        user = Subject.objects.get(pk=self.user1.pk)
        self.assertTrue(user.disabled)

    def test_subject_is_disabled_after_queryset_invocation(self):
        self.assertTrue(not self.user1.disabled)
        Subject.objects.filter(pk=self.user1.pk).disable()

        user = Subject.objects.get(pk=self.user1.pk)
        self.assertTrue(user.disabled)

    def test_subject_is_enabled_after_manager_invocation(self):
        self.assertTrue(not self.user1.disabled)
        self.user1.disabled = True
        self.user1.save()

        Subject.objects.enable(pk=self.user1.pk)
        user = Subject.objects.get(pk=self.user1.pk)
        self.assertTrue(not user.disabled)

    def test_subject_is_enabled_after_queryset_invocation(self):
        self.assertTrue(not self.user1.disabled)
        self.user1.disabled = True
        self.user1.save()

        Subject.objects.filter(pk=self.user1.pk).enable()
        user = Subject.objects.get(pk=self.user1.pk)
        self.assertTrue(not user.disabled)
