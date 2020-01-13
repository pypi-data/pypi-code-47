import logging

from django.db.models import BigIntegerField, BooleanField

from isc_common.fields.name_field import NameField
from isc_common.fields.related import ForeignKeyProtect
from isc_common.models.audit import AuditManager, AuditQuerySet, AuditModel
from isc_common.models.tree_audit import TreeAuditModelManager
from isc_common.number import DelProps
from kaf_pas.ckk.models.item_line import Item_lineManager
from kaf_pas.kd.models.document_attributes import Document_attributes
from kaf_pas.kd.models.documents import Documents
from kaf_pas.kd.models.lotsman_documents_hierarcy import Lotsman_documents_hierarcyManager

logger = logging.getLogger(__name__)


class Lotsman_documents_hierarcy_viewQuerySet(AuditQuerySet):
    def delete(self):
        return super().delete()

    def create(self, **kwargs):
        return super().create(**kwargs)

    def filter(self, *args, **kwargs):
        return super().filter(*args, **kwargs)


class Lotsman_documents_hierarcy_viewManager(AuditManager):

    @staticmethod
    def getRecord(record):
        res = {
            'id': record.id,
            'parent': record.parent_id,
            'editing': record.editing,
            'deliting': record.deliting,
            'document_id': record.document.id,

            'STMP_1_id': record.STMP_1.id if record.STMP_1 else None,
            'STMP_1_value_str': record.STMP_1.value_str if record.STMP_1 else None,
            'STMP_2_id': record.STMP_2.id if record.STMP_2 else None,
            'STMP_2_value_str': record.STMP_2.value_str if record.STMP_2 else None,
            'STMP_120_id': record.STMP_120.id if record.STMP_120 else None,
            'STMP_120_value_str': record.STMP_120.value_str if record.STMP_120 else None,

            'SPC_CLM_FORMAT_id': record.SPC_CLM_FORMAT.id if record.SPC_CLM_FORMAT else None,
            'SPC_CLM_FORMAT_value_str': record.SPC_CLM_FORMAT.value_str if record.SPC_CLM_FORMAT else None,
            'SPC_CLM_ZONE_id': record.SPC_CLM_ZONE.id  if record.SPC_CLM_ZONE else None,
            'SPC_CLM_ZONE_value_str': record.SPC_CLM_ZONE.value_str  if record.SPC_CLM_ZONE else None,
            'SPC_CLM_POS_id': record.SPC_CLM_POS.id if record.SPC_CLM_POS else None,
            'SPC_CLM_POS_value_int': record.SPC_CLM_POS.value_int if record.SPC_CLM_POS else None,
            'SPC_CLM_MARK_id': record.SPC_CLM_MARK.id if record.SPC_CLM_MARK else None,
            'SPC_CLM_MARK_value_str': record.SPC_CLM_MARK.value_str if record.SPC_CLM_MARK else None,
            'SPC_CLM_NAME_id': record.SPC_CLM_NAME.id if record.SPC_CLM_NAME else None,
            'SPC_CLM_NAME_value_str': record.SPC_CLM_NAME.value_str if record.SPC_CLM_NAME else None,
            'SPC_CLM_COUNT_id': record.SPC_CLM_COUNT.id if record.SPC_CLM_COUNT else None,
            'SPC_CLM_COUNT_value_str': record.SPC_CLM_COUNT.value_str if record.SPC_CLM_COUNT else None,
            'SPC_CLM_NOTE_id': record.SPC_CLM_NOTE.id if record.SPC_CLM_NOTE else None,
            'SPC_CLM_NOTE_value_str': record.SPC_CLM_NOTE.value_str if record.SPC_CLM_NOTE else None,
            'SPC_CLM_MASSA_id': record.SPC_CLM_MASSA.id if record.SPC_CLM_MASSA else None,
            'SPC_CLM_MASSA_value_str': record.SPC_CLM_MASSA.value_str if record.SPC_CLM_MASSA else None,
            'SPC_CLM_MATERIAL_id': record.SPC_CLM_MATERIAL.id if record.SPC_CLM_MATERIAL else None,
            'SPC_CLM_MATERIAL_value_str': record.SPC_CLM_MATERIAL.value_str if record.SPC_CLM_MATERIAL else None,
            'SPC_CLM_USER_id': record.SPC_CLM_USER.id if record.SPC_CLM_USER else None,
            'SPC_CLM_USER_value_str': record.SPC_CLM_USER.value_str if record.SPC_CLM_USER else None,
            'SPC_CLM_KOD_id': record.SPC_CLM_KOD.id if record.SPC_CLM_KOD else None,
            'SPC_CLM_KOD_value_str': record.SPC_CLM_KOD.value_str if record.SPC_CLM_KOD else None,
            'SPC_CLM_FACTORY_id': record.SPC_CLM_FACTORY.id if record.SPC_CLM_FACTORY else None,
            'SPC_CLM_FACTORY_value_str': record.SPC_CLM_FACTORY.value_str if record.SPC_CLM_FACTORY else None,

            'section': record.section,
            'subsection': record.subsection,
            'attr_name': record.attr_name,
            'isFolder': record.isFolder,
            'icon': Item_lineManager.getIcon(record)
        }
        return DelProps(res)

    def get_queryset(self):
        return Lotsman_documents_hierarcy_viewQuerySet(self.model, using=self._db)


class Lotsman_documents_hierarcy_view(AuditModel):
    id = BigIntegerField(primary_key=True, verbose_name="Идентификатор")
    parent_id = BigIntegerField(null=True, blank=True)
    document = ForeignKeyProtect(Documents)

    STMP_1 = ForeignKeyProtect(Document_attributes, related_name='STMP_1_Lotsman_documents_hierarcy_view', null=True, blank=True)
    STMP_2 = ForeignKeyProtect(Document_attributes, related_name='STMP_2_Lotsman_documents_hierarcy_view', null=True, blank=True)
    STMP_120 = ForeignKeyProtect(Document_attributes, related_name='STMP_120_Lotsman_documents_hierarcy_view', null=True, blank=True)

    SPC_CLM_KOD = ForeignKeyProtect(Document_attributes, related_name='SPC_CLM_KOD_Lotsman_documents_hierarcy_view', null=True, blank=True)
    SPC_CLM_FORMAT = ForeignKeyProtect(Document_attributes, related_name='SPC_CLM_FORMAT_Lotsman_documents_hierarcy_view', null=True, blank=True)
    SPC_CLM_COUNT = ForeignKeyProtect(Document_attributes, related_name='SPC_CLM_COUNT_Lotsman_documents_hierarcy_view', null=True, blank=True)
    SPC_CLM_ZONE = ForeignKeyProtect(Document_attributes, related_name='SPC_CLM_ZONE_Lotsman_documents_hierarcy_view', null=True, blank=True)
    SPC_CLM_MASSA = ForeignKeyProtect(Document_attributes, related_name='SPC_CLM_MASSA_Lotsman_documents_hierarcy_view', null=True, blank=True)
    SPC_CLM_POS = ForeignKeyProtect(Document_attributes, related_name='SPC_CLM_POS_Lotsman_documents_hierarcy_view', null=True, blank=True)
    SPC_CLM_NAME = ForeignKeyProtect(Document_attributes, related_name='SPC_CLM_NAME_Lotsman_documents_hierarcy_view', null=True, blank=True)
    SPC_CLM_MARK = ForeignKeyProtect(Document_attributes, related_name='SPC_CLM_MARK_Lotsman_documents_hierarcy_view', null=True, blank=True)
    SPC_CLM_NOTE = ForeignKeyProtect(Document_attributes, related_name='SPC_CLM_NOTE_Lotsman_documents_hierarcy_view', null=True, blank=True)
    SPC_CLM_USER = ForeignKeyProtect(Document_attributes, related_name='SPC_CLM_USER_Lotsman_documents_hierarcy_view', null=True, blank=True)
    SPC_CLM_FACTORY = ForeignKeyProtect(Document_attributes, related_name='SPC_CLM_FACTORY_Lotsman_documents_hierarcy_view', null=True, blank=True)
    SPC_CLM_MATERIAL = ForeignKeyProtect(Document_attributes, related_name='SPC_CLM_MATERIAL_Lotsman_documents_hierarcy_view', null=True, blank=True)

    Документ_на_материал = ForeignKeyProtect(Document_attributes, related_name='Документ_на_материал_Lotsman_documents_hierarcy_view', null=True, blank=True)
    Наименование_материала = ForeignKeyProtect(Document_attributes, related_name='Наименование_материала_Lotsman_documents_hierarcy_view', null=True, blank=True)
    Документ_на_сортамент = ForeignKeyProtect(Document_attributes, related_name='Документ_на_сортамент_Lotsman_documents_hierarcy_view', null=True, blank=True)
    Наименование_сортамента = ForeignKeyProtect(Document_attributes, related_name='Наименование_сортамента_Lotsman_documents_hierarcy_view', null=True, blank=True)

    section = NameField(null=True, blank=True)
    subsection = NameField(null=True, blank=True)
    attr_name = NameField(null=True, blank=True)
    isFolder = BooleanField(null=True, blank=True)
    props = Lotsman_documents_hierarcyManager.get_props()

    objects = Lotsman_documents_hierarcy_viewManager()
    objects_tree = TreeAuditModelManager()

    def __str__(self):
        return f'ID:{self.id}'

    def __repr__(self):
        return self.__str__()

    # @property
    # def SPC_CLM_MATERIAL_value_str(self):
    #     mat = f'{self.Документ_на_материал_value_str if self.Документ_на_материал_value_str else ""} ' \
    #           f'{self.Наименование_материала_value_str if self.Наименование_материала_value_str else ""} '
    #
    #     if mat.strip() != '':
    #         mat += ' \ '
    #
    #     return mat + \
    #            f'{self.Документ_на_сортамент_value_str if self.Документ_на_сортамент_value_str else ""} ' \
    #            f'{self.Наименование_сортамента_value_str if self.Наименование_сортамента_value_str else ""}'
    #
    # @property
    # def SPC_CLM_MATERIAL_id(self):
    #     from kaf_pas.kd.models.document_attributes import Document_attributes
    #     from kaf_pas.ckk.models.attr_type import Attr_type
    #     from kaf_pas.kd.models.lotsman_document_attr_cross import Lotsman_document_attr_cross
    #
    #     SPC_CLM_MATERIAL_type = Attr_type.objects.get(code='SPC_CLM_MATERIAL')
    #     attribute, _ = Document_attributes.objects.get_or_create(attr_type=SPC_CLM_MATERIAL_type, value_str=self.SPC_CLM_MATERIAL_value_str)
    #     Lotsman_document_attr_cross.objects.get_or_create(document_id=self.id, attribute=attribute)
    #     return attribute.id

    class Meta:
        verbose_name = 'Иерархия документа из Лоцмана'
        managed = False
        db_table = 'kd_lotsman_documents_hierarcy_mview'
