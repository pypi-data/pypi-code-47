import logging

from isc_common.fields.name_field import NameStrictField
from isc_common.fields.related import ForeignKeyCascade
from isc_common.managers.common_managet_with_lookup_fields import CommonManagetWithLookUpFieldsManager, CommonManagetWithLookUpFieldsQuerySet
from isc_common.models.base_ref import BaseRefHierarcy
from kaf_pas.planing.models.operation_types import Operation_types

logger = logging.getLogger(__name__)


class OperationsQuerySet(CommonManagetWithLookUpFieldsQuerySet):

    def filter(self, *args, **kwargs):
        return super().filter(*args, **kwargs)


class OperationsManager(CommonManagetWithLookUpFieldsManager):

    @staticmethod
    def getRecord(record):
        res = {
            'id': record.id,
            'code': record.code,
            'name': record.name,
            'full_name': record.full_name,
            'description': record.description,
            'parent_id': record.parent_id,
            'planing_operation_type_id': record.planing_operation_type.id if record.planing_operation_type else None,
            'planing_operation_type__code': record.planing_operation_type.code if record.planing_operation_type else None,
            'planing_operation_type__full_name': record.planing_operation_type.full_name if record.planing_operation_type else None,
            'lastmodified': record.lastmodified,
            'editing': record.editing,
            'deliting': record.deliting,
        }
        return res

    def get_queryset(self):
        return OperationsQuerySet(self.model, using=self._db)


class Operations(BaseRefHierarcy):
    name = NameStrictField()
    planing_operation_type = ForeignKeyCascade(Operation_types, null=True, blank=True, related_name='planing_operation_type')
    objects = OperationsManager()

    def __str__(self):
        return f'ID={self.id}, code={self.code}, name={self.name}, description={self.description}'

    class Meta:
        verbose_name = 'Операции'
