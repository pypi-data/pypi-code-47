from django.db import models
from django.conf import settings
from django_global_request.middleware import get_request


class ItemOwnerMixin(models.Model):

    owner_field_name = "owner"

    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, blank=True, editable=False, related_name="+")

    class Meta:
        abstract = True

    def save(self, *args, **kwargs):
        if not hasattr(self, self.owner_field_name) or not getattr(self, self.owner_field_name):
            request = get_request()
            if request.user and request.user.pk:
                setattr(self, self.owner_field_name, request.user)
        super().save(*args, **kwargs)


class ItemShareMixin(models.Model):

    share_users = models.ManyToManyField(settings.AUTH_USER_MODEL, blank=True, related_name="+")

    class Meta:
        abstract = True

