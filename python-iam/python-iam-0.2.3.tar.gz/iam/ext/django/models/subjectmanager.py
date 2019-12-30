from django.apps import apps
from django.contrib.auth.models import BaseUserManager
from django.db import models


class SubjectManager(BaseUserManager):

    class queryset_class(models.QuerySet):

        def disable(self):
            """Disables all :class:`Subject` instances in the
            :class:`~django.db.models.QuerySet`.
            """
            return self.update(disabled=True)

        def enable(self):
            """Enables all :class:`Subject` instances in the
            :class:`~django.db.models.QuerySet`.
            """
            return self.update(disabled=False)

    def get_queryset(self):
        return self.queryset_class(self.model, using=self._db)

    def disable(self, **params):
        """Disables all :class:`Subject` entities filtered
        by the given parameters.
        """
        return self.filter(**params).disable()

    def enable(self, **params):
        """Enable all :class:`Subject` entities filtered
        by the given parameters.
        """
        return self.filter(**params).enable()

    def create_user(self, kind, **kwargs):
        Subject = apps.get_model('iam', kind)
        if Subject is None:
            raise ValueError(f"Invalid kind: {kind}")
        return Subject.objects.create(**kwargs)
