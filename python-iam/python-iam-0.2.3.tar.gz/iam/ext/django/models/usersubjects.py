from django.db import models

from .subjects import Subject


class User(Subject):

    subject = models.OneToOneField(
        Subject,
        parent_link=True,
        primary_key=True,
        on_delete=models.PROTECT,
        db_column='subject_id'
    )

    first_name = models.CharField(
        max_length=128,
        blank=False,
        null=False,
        db_column='first_name'
    )

    last_name = models.CharField(
        max_length=128,
        blank=False,
        null=False,
        db_column='last_name'
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if not self.kind:
            self.kind = 'User'

    class Meta:
        app_label = 'iam'
        default_permissions = []
        db_table = 'usersubjects'
