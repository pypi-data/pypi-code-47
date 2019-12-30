import uuid

from django.db import models
from django.contrib.auth.models import Permission


class ResourceAuthorizationManager(models.Manager):

    def grant(self, granter, principal, qualname, resource):
        """Create a :class:`~iam.ext.django.models.ResourceAuthorization`
        instance representing a grant of the permission `qualname` to
        `principal` by `granter` on `resource`.
        """
        app_label, codename = str.split(qualname, '.', 1)
        permission = Permission.objects.get(
            content_type__app_label=app_label,
            codename=codename
        )
        return self.create(
            kind=principal.kind,
            principal_id=principal.resource_id,
            resource_class=resource.kind,
            resource_id=resource.resource_id,
            permission=permission
        )

    def revoke(self, granter, principal, qualname, resource):
        """Revoke an existing permission for a principal."""
        app_label, codename = str.split(qualname, '.', 1)
        permission = Permission.objects.get(
            content_type__app_label=app_label,
            codename=codename
        )
        return self.filter(
            kind=principal.kind,
            principal_id=principal.resource_id,
            resource_class=resource.kind,
            resource_id=resource.resource_id,
            permission=permission
        ).delete()

    def deny(self, granter, principal, qualname, resource):
        """Explicitely deny the permission to the principal."""
        self.revoke(granter, principal, qualname, resource)
        app_label, codename = str.split(qualname, '.', 1)
        permission = Permission.objects.get(
            content_type__app_label=app_label,
            codename=codename
        )
        return self.create(
            kind=principal.kind,
            principal_id=principal.resource_id,
            resource_class=resource.kind,
            resource_id=resource.resource_id,
            permission=permission,
            revoked=True
        )
