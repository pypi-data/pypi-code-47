from django.db import models
from django.contrib.auth.models import Permission

from .resourceauthorizationmanager import ResourceAuthorizationManager


class ResourceAuthorization(models.Model):
    """Represents an authorization on a specific resource to
    a principal.
    """
    objects = ResourceAuthorizationManager()

    #: The realm in which the resource is granted to the
    #: principal; if your application does not implement
    #: the concept of realms, then leave this to its
    #: default value.
    realm = models.UUIDField(
        blank=False,
        null=False,
        default='00000000-0000-0000-0000-000000000000',
        db_column='realm'
    )

    #: Specifies the kind of principal to which this
    #: permission is granted. Allowed values are ``Subject``
    #: (all subject types), ``User`` (human users),
    #: ``ServiceAccount`` (service accounts) or ``Group``
    #: (groups).
    kind = models.CharField(
        max_length=128,
        choices=[
            ('Subject', "Subject"),
            ('User', "User"),
            ('ServiceAccount', "Service Account"),
            ('Group', "Group"),
            ('Role', "Role")
        ],
        blank=False,
        null=False,
        db_column='kind'
    )

    #: Either the :attr:`~django.contrib.auth.models.Group.id` represented
    #: as UUID) or the :class:`~iam.ext.django.models.Subject.id`. If you
    #: want to grant authorizations to other principal types, ensure that the
    #: (surrogate) primary key is either a :class:`uuid.UUID` or :class:`int`.
    principal_id = models.UUIDField(
        blank=False,
        null=False,
        db_column='principal_id'
    )

    #: Identifies the resource class. The convention is ``<app label>.<object name>``,
    #: but deviations are allowed when, for example, the resource is not represented
    #: as a Django model.
    resource_class = models.CharField(
        max_length=128,
        blank=False,
        null=False,
        db_column='resource_class'
    )

    #: The resource identifier, represented as a :class:`uuid.UUID`.
    resource_id = models.UUIDField(
        blank=False,
        null=False,
        db_column='resource_id'
    )

    #: The Django :class:`~django.contrib.auth.models.Permission`
    #: instance that represents the granted authorization.
    permission = models.ForeignKey(
        Permission,
        blank=False,
        null=False,
        on_delete=models.CASCADE,
        related_name='authorizations',
        db_column='permission_id'
    )

    #: Indicates when this authorization expires. If the grant does not
    #: expire, :attr:`ResourceAuthorization.expires` should be ``0``.
    expires = models.BigIntegerField(
        blank=False,
        null=False,
        default=0,
        db_column='expires'
    )

    #: Inverts the authorization logic; indicates if the
    #: :class:`ResourceAuthorization` is explicitely not
    #: granted.
    revoked = models.BooleanField(
        blank=False,
        null=False,
        default=False,
        db_column='revoked'
    )

    class Meta:
        app_label = 'iam'
        default_permissions = []
        db_table = 'resourceauthorizations'
        permissions = [
            ('login', 'Login'),
            ('grant', 'Grant'),
            ('revoke', 'Revoke'),
        ]
        unique_together = [('realm', 'resource_class', 'resource_id', 'permission', 'principal_id')]
