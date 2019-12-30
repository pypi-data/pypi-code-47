import uuid

from django.db import models

from .authorizations import Authorization


class SubjectRoleType(models.Model):
    """Represents a role that may be assigned to a
    :class:`~iam.ext.django.models.Subject`.
    """
    #: A surrogate primary key.
    id = models.UUIDField(
        primary_key=True,
        blank=False,
        null=False,
        default=uuid.uuid4,
        db_column='id'
    )

    #: The codename for the role.
    name = models.CharField(
        max_length=128,
        blank=False,
        null=False,
        db_column='name'
    )

    #: A friendly descriptive name for the role.
    title = models.CharField(
        max_length=128,
        blank=False,
        null=False,
        db_column='title'
    )

    #: An optional description of the role.
    description = models.CharField(
        max_length=1024,
        blank=False,
        null=False,
        default='',
        db_column='description'
    )

    #: Indicates if the role is an integral part of a
    #: system; as opposed to user-defined roles (if the
    #: system supports this functionality).
    system = models.BooleanField(
        blank=False,
        null=False,
        default=False,
        db_column='system'
    )

    #: If the system supports user-defined roles, this flag
    #: indicates that the role may be assigned to any user.
    isglobal = models.BooleanField(
        blank=False,
        null=False,
        default=False,
        db_column='isglobal'
    )

    #: The authorizations that were granted to this role.
    authorizations = models.ManyToManyField(
        Authorization,
        related_name='roles',
        db_table='subjectroletypeauthorizations'
    )

    class Meta:
        app_label = 'iam'
        default_permissions = []
        db_table = 'subjectroletypes'
