from django.contrib.auth import authenticate
from django.contrib.auth import login
from django.contrib.sessions.middleware import SessionMiddleware
from django.test import TestCase
from django.test import RequestFactory

import iam.const


class BasicLoginTestCase(TestCase):
    fixtures = ['testusers']

    def setUp(self):
        self.factory = RequestFactory()
        self.request = self.factory.get('/')
        SessionMiddleware().process_request(self.request)

    def test_standard_authenticate_with_valid_password(self):
        subject = authenticate(self.request,
            key=iam.const.DEFAULT_SUPERUSER,
            password=iam.const.DEFAULT_PASSWORD)
        self.assertTrue(subject is not None)

    def test_standard_authenticate_with_invalid_password(self):
        subject = authenticate(self.request,
            key=iam.const.DEFAULT_SUPERUSER,
            password=str.upper(iam.const.DEFAULT_PASSWORD))
        self.assertTrue(subject is None)

    def test_standard_login_with_valid_password(self):
        subject = authenticate(self.request,
            key=iam.const.DEFAULT_SUPERUSER,
            password=iam.const.DEFAULT_PASSWORD)
        self.assertTrue(subject is not None)
        login(self.request, subject)
