import logging

from django.db.models import BooleanField

from isc_common.fields.related import ForeignKeyCascade
from isc_common.managers.common_managet_with_lookup_fields import CommonManagetWithLookUpFieldsManager, CommonManagetWithLookUpFieldsQuerySet
from isc_common.models.base_ref import BaseRefHierarcy
from kaf_pas.planing.models.operation_types import Operation_types

logger = logging.getLogger(__name__)


class Operations_viewQuerySet(CommonManagetWithLookUpFieldsQuerySet):
    def filter(self, *args, **kwargs):
        return super().filter(*args, **kwargs)


class Operations_viewManager(CommonManagetWithLookUpFieldsManager):

    @staticmethod
    def getRecord(record):
        res = {
            "id": record.id,
            "code": record.code,
            "name": record.name,
            "full_name": record.full_name,
            "description": record.description,
            "parent_id": record.parent_id,
            "lastmodified": record.lastmodified,
            'isFolder': record.isFolder,
            'editing': record.editing,
            'deliting': record.deliting,
            'planing_operation_type_id': record.planing_operation_type.id if record.planing_operation_type else None,
            'planing_operation_type__code': record.planing_operation_type.code if record.planing_operation_type else None,
            'planing_operation_type__full_name': record.planing_operation_type.full_name if record.planing_operation_type else None,
        }
        return res

    def get_queryset(self):
        return Operations_viewQuerySet(self.model, using=self._db)


class Operations_view(BaseRefHierarcy):
    planing_operation_type = ForeignKeyCascade(Operation_types, null=True, blank=True, related_name='planing_operation_type_view')
    isFolder = BooleanField()
    objects = Operations_viewManager()

    def _get_planing_operation_type(self, parent):
        if parent:
            if parent.planing_operation_type:
                return parent.planing_operation_type
            else:
                return self._get_planing_operation_type(parent=parent.parent)
        else:
            return None

    @property
    def get_planing_operation_type(self):
        if self.planing_operation_type:
            return self.planing_operation_type

        return self._get_planing_operation_type(parent=self.parent)

    def __str__(self):
        return f"ID={self.id}, code={self.code}, name={self.name}, description={self.description}"

    class Meta:
        db_table = 'production_operations_view'
        managed = False
        verbose_name = 'Операции'
