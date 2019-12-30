import uuid

from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.db import models

from .subjectmanager import SubjectManager


class Subject(AbstractBaseUser, PermissionsMixin):
    """A :class:`Subject` represents the source of a request to
    a system. It may be any entity, such as a person or service.
    """
    objects = SubjectManager()
    EMAIL_FIELD = 'key'
    USERNAME_FIELD = EMAIL_FIELD
    REQUIRED_FIELDS = [
        'kind',
        'key'
    ]
    if USERNAME_FIELD in REQUIRED_FIELDS:
        REQUIRED_FIELDS.remove(USERNAME_FIELD)

    #: A randomly generated UUID.
    id = models.UUIDField(
        blank=False,
        null=False,
        default=uuid.uuid4,
        primary_key=True,
        db_column='id'
    )

    #: Specifies the kind of :class:`Subject`. Supported values are
    #: ``User`` and ``ServiceAccount``.
    kind = models.CharField(
        max_length=32,
        blank=False,
        null=False,
        choices=[
            ('User', "User"),
            ("ServiceAccount", "Service Account")
        ],
        db_column='kind'
    )

    #: The natural identifier of the :class:`Subject`. The
    #: format is ``local-part@domain``, where ``local-part``
    #: consists of letters, digits and hyphens and ``domain``
    #: is a valid, non-internationalized hostname; commonly
    #: referred to as *email address*.
    key = models.CharField(
        max_length=255,
        blank=False,
        null=False,
        unique=True,
        db_column='key'
    )

    #: Flag to disable access to a system for the :class:`Subject`.
    disabled = models.BooleanField(
        default=False,
        blank=False,
        null=False,
        db_column='disabled'
    )

    def get_principal_id(self):
        """Return a string holding an UUID representing the
        (surrogate) primary key of the resource.
        """
        return str(self.id)

    class Meta:
        app_label = 'iam'
        db_table = 'subjects'
        default_permissions = []
