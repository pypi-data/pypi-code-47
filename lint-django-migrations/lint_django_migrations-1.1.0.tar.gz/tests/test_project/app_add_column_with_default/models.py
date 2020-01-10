from django.db import models


class A(models.Model):
    null_field = models.IntegerField(null=True)
    new_nullable_field_with_default = models.IntegerField(default=1, null=True)
