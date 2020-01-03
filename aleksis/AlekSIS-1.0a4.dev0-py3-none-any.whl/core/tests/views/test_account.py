from django.conf import settings
from django.urls import reverse

import pytest

pytestmark = pytest.mark.django_db


def test_index_not_logged_in(client):
    response = client.get("/")

    assert response.status_code == 200
    assert reverse(settings.LOGIN_URL) in response.content.decode("utf-8")


def test_login(client, django_user_model):
    username = "foo"
    password = "bar"

    django_user_model.objects.create_user(username=username, password=password)
    client.login(username=username, password=password)

    response = client.get("/")

    assert response.status_code == 200
    assert reverse(settings.LOGIN_URL) not in response.content.decode("utf-8")


def test_index_not_linked_to_person(client, django_user_model):
    username = "foo"
    password = "bar"

    django_user_model.objects.create_user(username=username, password=password)
    client.login(username=username, password=password)

    response = client.get("/")

    assert response.status_code == 200
    assert "You are not linked to a person" in response.content.decode("utf-8")


def test_logout(client, django_user_model):
    username = "foo"
    password = "bar"

    django_user_model.objects.create_user(username=username, password=password)
    client.login(username=username, password=password)

    response = client.get("/")
    assert response.status_code == 200

    response = client.get(reverse("logout"), follow=True)

    assert response.status_code == 200
    assert reverse(settings.LOGIN_URL) in response.content.decode("utf-8")
