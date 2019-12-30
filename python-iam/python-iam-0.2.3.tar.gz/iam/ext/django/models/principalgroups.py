import uuid

from django.db import models
from django.contrib.auth.models import Group


class PrincipalGroup(Group):
    kind = 'Group'

    _parent = models.OneToOneField(
        Group,
        blank=False,
        null=False,
        primary_key=True,
        parent_link=True,
        related_name='principal',
        on_delete=models.CASCADE,
        db_column='id'
    )

    resource_id = models.UUIDField(
        blank=False,
        null=False,
        default=uuid.uuid4,
        db_column='resource_id'
    )

    def add(self, principal):
        """Adds a principal to the :class:`PrincipalGroup`."""
        principal.groups.add(self._parent)

    def get_resource_id(self):
        """Returns the resource identifier."""
        return self.resource_id

    class Meta:
        app_label = 'iam'
        default_permissions = []
        db_table = 'principalgroups'
