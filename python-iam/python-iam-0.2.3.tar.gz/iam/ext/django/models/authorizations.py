import uuid

from django.db import models


class AuthorizationManager(models.Manager):

    def get_by_natural_key(self, name):
        return self.get(name=name)


class Authorization(models.Model):
    objects = AuthorizationManager()

    id = models.AutoField(
        primary_key=True,
        blank=False,
        null=False,
        db_column='id'
    )

    name = models.CharField(
        max_length=128,
        blank=False,
        null=False,
        unique=True,
        db_column='name'
    )

    def natural_key(self):
        return (self.name,)

    class Meta:
        app_label = 'iam'
        default_permissions = []
        db_table = 'authorizations'
