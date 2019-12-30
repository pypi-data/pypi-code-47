import time

from django.apps import apps
from django.contrib.auth import get_user_model


class ResourceAuthorizationService:

    def isgrantable(self, principal, permission):
        """Return a boolean indicating if the :class:`Subject`
        identified by `subject_id` is authorized to grant the
        given `permission`.
        """
        app_label, codename = str.split(permission, '.', 1)
        Permission = apps.get_model('auth', 'Permission')

        # TODO: This only supports Subjects as principals atm.
        subject = get_user_model()\
            .objects.get(id=principal.id)
        permission = Permission.objects.get(
            content_type__app_label=app_label,
            codename=codename
        )
        return subject.has_perm('iam.grant', permission)

    def grant(self, granter, principal, qualname, resource=None, expires=None, ttl=None):
        """Grant the authorization identified by `qualname` as
        `granter` to :class:`Principal` `principal`, optionally
        expiring at `expires` or with a restricted lifetime `ttl`.

        Args:
            granter (:class:`Principal`): identifies the granter.
            principal (:class:`Principal`): identifies the principal to
                which the permission is granted.
            resource (:class:`Resource`): optionally a specific resource
                on which the permission is granted.
            expires (int): the date/time at which the grant expires,
                in milliseconds since the UNIX epoch. May not be used in
                combination with `ttl`.
            ttl (int): time-to-live, in milliseconds. May not be used in
                combination with `expires`.

        Returns:
            None
        """
        if not self.isgrantable(granter, qualname, not bool(resource)):
            raise NotAuthorized

        if expires and ttl:
            raise ValueError(
                "Specify either `expires` or `ttl`")
        granted = int(time.time() * 1000)
        if ttl:
            expires = granted + ttl
