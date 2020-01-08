from django.db import models
from django.contrib.postgres.fields import JSONField


class BaseSnapshot(models.Model):
    scraped_at = models.DateTimeField(auto_now_add=True, editable=False)
    data = JSONField()

    class Meta:
        abstract = True
