from django.contrib.auth.backends import ModelBackend

class ModelUserWithIdentityBackend(ModelBackend):

    def authenticate(self, request, username=None, password=None, **kwargs):
        from django_pgpy.models import Identity

        user = super().authenticate(request, username, password, **kwargs)
        if user and user.is_authenticated and not Identity.objects.exists_for_user(user):
            Identity.objects.create(user, password)
        return user


class ModelUserWithIdentityAndSuperuserRestorersBackend(ModelBackend):

    def authenticate(self, request, username=None, password=None, **kwargs):
        from django_pgpy.models import Identity

        user = super().authenticate(request, username, password, **kwargs)
        superuser_identities = Identity.objects.filter(user__is_superuser=True).exclude(user=user)
        if user and user.is_authenticated and not Identity.objects.exists_for_user(user):
            Identity.objects.create(user, password, list(superuser_identities))

        self._add_superusers_to_identities(user, password, superuser_identities)
        return user

    def _add_superusers_to_identities(self, user, password, superuser_identities):
        from django_pgpy.models import Identity

        if user:
            identity = Identity.objects.get(user=user)
            if list(identity.encrypters.all().order_by('user__id')) != list(superuser_identities.all().order_by('user__id')):
                identity.add_restorers(password, list(superuser_identities.all().order_by('user__id')))
