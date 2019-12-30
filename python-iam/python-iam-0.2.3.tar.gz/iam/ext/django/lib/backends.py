import uuid

from django.conf import settings
from django.contrib.auth.backends import ModelBackend
from django.contrib.auth.models import Permission

from iam.domain.mixins import Authorizable


class AuthorizedModelBackend(ModelBackend):

    def get_all_permissions(self, principal, obj=None):
        """Returns all permissions for the given user, based
        on its group and optionally for a specific resource.
        """
        perms = super().get_all_permissions(principal, None)
        if obj is None:
            return perms
        assert hasattr(principal, '_perm_cache')
        assert isinstance(principal._perm_cache, set)
        if not hasattr(principal, '_object_perm_cache'):
            principal._object_perm_cache = {}
        qualname, object_perms = self.get_object_permissions(principal, obj)
        if qualname:
            principal._object_perm_cache[qualname] = object_perms
        return perms | principal._object_perm_cache[qualname]

    def get_object_permissions(self, principal, obj):
        """Return a tuple containing a string representing the qualified
        name of the resource and a set of strings indicating the
        permissions that the subject has on the given object.
        """
        if obj is None:
            return None, set()

        if issubclass(type(obj), Authorizable):
            return obj.get_subject_authorizations(principal)

        resource_class = f"{obj._meta.app_label}.{obj._meta.object_name}".lower()
        resource_id = self.get_resource_id(obj)

        # Bail out early if the user is a superuser, since it will have
        # all permissions on the resource.
        if principal.is_superuser:
            perms = Permission.objects.all()\
                .values_list('content_type__app_label', 'codename')
            return qualname, set([str.lower(f'{x}.{y}') for x, y in perms])

        qs = Permission.objects.filter(
            authorizations__kind=principal.kind,
            authorizations__principal_id=principal.get_principal_id(),
            authorizations__resource_id=resource_id,
            authorizations__resource_class__iexact=resource_class,
            authorizations__revoked=False
        )
        perms = [str.lower(f'{x}.{y}') for x, y
            in qs.values_list('content_type__app_label', 'codename')]

        # Load the group permissions.
        groups = [x.principal.resource_id for x
            in principal.groups.filter(principal__isnull=False)]
        qs = Permission.objects.filter(
            authorizations__kind='Group',
            authorizations__principal_id__in=groups,
            authorizations__resource_id=resource_id,
            authorizations__resource_class__iexact=resource_class,
            authorizations__revoked=False
        )
        perms.extend([str.lower(f'{x}.{y}') for x, y
            in qs.values_list('content_type__app_label', 'codename')])

        return f'{resource_class}:{resource_id}',\
            set(perms) - self.get_denied_permissions(principal, obj)

    def get_denied_permissions(self, principal, obj):
        """Return a set holding the permissions that are denied
        on this object, either to the user explicitely or through
        its group membership.
        """
        if principal.is_superuser:
            return set()
        resource_class = f"{obj._meta.app_label}.{obj._meta.object_name}".lower()
        resource_id = self.get_resource_id(obj)
        qs = Permission.objects.filter(
            authorizations__kind=principal.kind,
            authorizations__principal_id=principal.get_principal_id(),
            authorizations__resource_id=resource_id,
            authorizations__resource_class__iexact=resource_class,
            authorizations__revoked=True
        )
        perms = [str.lower(f'{x}.{y}') for x, y
            in qs.values_list('content_type__app_label', 'codename')]

        # Load the group permissions.
        groups = [x.principal.resource_id for x
            in principal.groups.filter(principal__isnull=False)]
        qs = Permission.objects.filter(
            authorizations__kind='Group',
            authorizations__principal_id__in=groups,
            authorizations__resource_id=resource_id,
            authorizations__resource_class__iexact=resource_class,
            authorizations__revoked=True
        )
        perms.extend([str.lower(f'{x}.{y}') for x, y
            in qs.values_list('content_type__app_label', 'codename')])

        return set(perms)

    def get_resource_id(self, resource):
        """Returns an UUID string representing the primary key
        of the resource.
        """
        pk = resource.pk
        if not isinstance(pk, (int, uuid.UUID)):
            raise ValueError(
                "Cannot determine resource identifier from primary key.")
        if isinstance(pk, int):
            resource_id = uuid.UUID(int=pk)
        elif isinstance(pk, uuid.UUID):
            resource_id = pk
        return pk
