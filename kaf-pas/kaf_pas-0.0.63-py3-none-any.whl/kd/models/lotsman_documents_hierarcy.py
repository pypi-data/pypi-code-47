import logging

from bitfield import BitField
from django.db import transaction, connection
from django.db.models import BigIntegerField

from isc_common import Stack
from isc_common.fields.related import ForeignKeyProtect
from isc_common.http.DSRequest import DSRequest
from isc_common.management.commands.refresh_mat_views import refresh_mat_view
from isc_common.models.audit import AuditManager, AuditQuerySet, AuditModel
from kaf_pas.ckk.models.attr_type import Attr_type
from kaf_pas.kd.models.documents import Documents, DocumentManager

logger = logging.getLogger(__name__)


class Lotsman_documents_hierarcyQuerySet(AuditQuerySet):
    def delete(self):
        return super().delete()

    def create(self, **kwargs):
        return super().create(**kwargs)

    def filter(self, *args, **kwargs):
        return super().filter(*args, **kwargs)


class Lotsman_documents_hierarcyManager(AuditManager):
    @staticmethod
    def get_props():
        return BitField(flags=(
            ('relevant', 'Актуальность'),
            ('beenItemed', 'Был внесен в состав изделий'),
        ), default=1, db_index=True)

    @staticmethod
    def refresh_lotsman_kd():

        with connection.cursor() as cursor:
            cursor.execute('''delete
                                from kd_lotsman_documents_hierarcy_refs
                                where child_id in (select child_id
                                                   from kd_lotsman_documents_hierarcy_refs
                                                   where parent_id is null)
                                  and parent_id is not null''')

    @staticmethod
    def make_items(document, logger, owner=None):
        from kaf_pas.ckk.models.item import Item
        from kaf_pas.ckk.models.item_line import Item_line
        from kaf_pas.ckk.models.item_line import Item_lineManager
        from kaf_pas.ckk.models.item_refs import Item_refs
        from kaf_pas.kd.models.document_attributes import Document_attributesManager
        from kaf_pas.kd.models.lotsman_documents_hierarcy_view import Lotsman_documents_hierarcy_view

        if not isinstance(document, Documents):
            raise Exception(f'document must be Lotsman_documents_hierarcy_view type')

        Lotsman_documents_hierarcyManager.refresh_lotsman_kd()

        items_pairs = Stack()

        def get_item(lotsman_id):
            items = [item[1] for item in items_pairs.stack if item[0] == lotsman_id]
            if len(items) == 0:
                item, created = Item.objects.get_or_create(
                    STMP_1_id=STMP_1_id,
                    STMP_2_id=STMP_2_id,
                    props=Item.props.relevant | Item.props.from_lotsman,
                    lotsman_document_id=lotsman_documents_hierarcy.id,
                )
                items_pairs.push((lotsman_documents_hierarcy.id, item))

                DocumentManager.link_image_to_lotsman_item(item, logger)

                if logger and created:
                    logger.logging(f'\nAdded parent: {item}', 'debug')
            elif len(items) == 1:
                item = items[0]
            else:
                raise Exception(f'Неоднозначный выбор.')
            return item

        with transaction.atomic():
            # lotsman_documents_parent_id = None
            parent, created = Item.objects.get_or_create(
                STMP_1=Document_attributesManager.get_or_create_attribute(
                    attr_codes='STMP_1',
                    value_str='Импорт из Лоцмана',
                    logger=logger
                ),
                props=Item.props.relevant | Item.props.from_lotsman
            )

            Item_refs.objects.get_or_create(
                child=parent
            )

            cnt = Lotsman_documents_hierarcy_view.objects_tree.get_descendants_count(
                child_id='id',
                where_clause=f'where document_id={document.id} and props=1',
                include_self=False)

            if cnt > 0:
                if owner != None:
                    owner.cnt += cnt

                for lotsman_documents_hierarcy in Lotsman_documents_hierarcy_view.objects_tree.get_descendants(
                        child_id='id',
                        where_clause=f'where document_id={document.id} and props=1',
                        order_by_clause='order by level',
                        include_self=False):

                    STMP_1_id = lotsman_documents_hierarcy.STMP_1.id
                    STMP_2_id = lotsman_documents_hierarcy.STMP_2.id

                    item = get_item(lotsman_documents_hierarcy.id)

                    if lotsman_documents_hierarcy.parent_id != None:
                        parent = get_item(lotsman_documents_hierarcy.parent_id)

                    Item_refs.objects.get_or_create(parent=parent, child=item)
                    item_line, created = Item_line.objects.get_or_create(
                        parent=parent,
                        child=item,
                        defaults=dict(
                            SPC_CLM_FORMAT=lotsman_documents_hierarcy.SPC_CLM_FORMAT,
                            SPC_CLM_ZONE=lotsman_documents_hierarcy.SPC_CLM_ZONE,
                            SPC_CLM_POS=lotsman_documents_hierarcy.SPC_CLM_POS,
                            SPC_CLM_MARK=lotsman_documents_hierarcy.SPC_CLM_MARK,
                            SPC_CLM_NAME=lotsman_documents_hierarcy.SPC_CLM_NAME,
                            SPC_CLM_COUNT=lotsman_documents_hierarcy.SPC_CLM_COUNT,
                            SPC_CLM_NOTE=lotsman_documents_hierarcy.SPC_CLM_NOTE,
                            SPC_CLM_MASSA=lotsman_documents_hierarcy.SPC_CLM_MASSA,
                            SPC_CLM_MATERIAL=lotsman_documents_hierarcy.SPC_CLM_MATERIAL,
                            SPC_CLM_USER=lotsman_documents_hierarcy.SPC_CLM_USER,
                            SPC_CLM_KOD=lotsman_documents_hierarcy.SPC_CLM_KOD,
                            SPC_CLM_FACTORY=lotsman_documents_hierarcy.SPC_CLM_FACTORY,
                            section=lotsman_documents_hierarcy.section,
                            section_num=Item_lineManager.section_num(lotsman_documents_hierarcy.section),
                            subsection=lotsman_documents_hierarcy.subsection,
                        )
                    )

                    if logger and created:
                        logger.logging(f'\nAdded line: {item_line}', 'debug')

                    Lotsman_documents_hierarcy.objects.update_or_create(
                        id=lotsman_documents_hierarcy.id,
                        defaults=dict(
                            props=lotsman_documents_hierarcy.props | Lotsman_documents_hierarcy.props.beenItemed
                        ))

                    if owner != None:
                        owner.pbar_progress()

                    document.props |= Documents.props.beenItemed
                    document.save()

        if cnt > 0:
            if owner != None:
                refresh_mat_view('kd_lotsman_documents_hierarcy_mview')

    @staticmethod
    def make_mview():
        from kaf_pas.system.models.contants import Contants
        from django.db import connection

        fields_sql = []
        sql_array = []

        parent_system_const, _ = Contants.objects.update_or_create(
            code='lotsman_attibutes',
            defaults=dict(name='Атрибуты товарных позиций импортированных из Лоцмана')
        )

        attr_map = {
            'Зона': 'SPC_CLM_ZONE',
            'Код': 'SPC_CLM_KOD',
            'Масса': 'SPC_CLM_MASSA',
            'Материал': 'SPC_CLM_MATERIAL',
            'Наименование': 'SPC_CLM_NAME',
            'Обозначение': 'SPC_CLM_MARK',
            'Позиция': 'SPC_CLM_POS',
            'Пользовательская': 'SPC_CLM_USER',
            'Предприятие - изготовитель': 'SPC_CLM_FACTORY',
            'Примечание': 'SPC_CLM_NOTE',
            'Формат': 'SPC_CLM_FORMAT',
        }

        for name, code in attr_map.items():
            Contants.objects.update_or_create(
                code=code,
                defaults=dict(
                    name=name,
                    parent=parent_system_const
                )
            )

        m_view_name = 'kd_lotsman_documents_hierarcy_mview'
        sql_array.append(f'DROP MATERIALIZED VIEW IF EXISTS {m_view_name}')
        sql_array.append(f'''CREATE MATERIALIZED VIEW {m_view_name} AS SELECT lts.id,
                                                                                   lts.deleted_at,
                                                                                   lts.editing,
                                                                                   lts.deliting,
                                                                                   lts.lastmodified,                                                                                
                                                                                   ltsr.parent_id,
                                                                                   lts.props,
                                                                                   lts.document_id,
                                                                                   CASE
                                                                                        WHEN (select count(1) as count
                                                                                              from kd_lotsman_documents_hierarcy_refs hr
                                                                                              join kd_lotsman_documents_hierarcy lh on lh.id=hr.child_id	
                                                                                              where hr.parent_id = lts.id
                                                                                                and lh.document_id = lts.document_id) > 0 THEN true
                                                                                        ELSE false
                                                                                   END AS "isFolder",                                                                                 
                                                                                   ltsr.section, 
                                                                                   ltsr.subsection,
                                                                                   att.code attr_code,
                                                                                   att.name attr_name
                                                                                   $COMMA
                                                                                   $FIELDS     
                                                                            FROM kd_lotsman_documents_hierarcy lts
                                                                                    join kd_lotsman_documents_hierarcy_refs ltsr on ltsr.child_id = lts.id
                                                                                    join ckk_attr_type att on att.id = lts.attr_type_id  WITH DATA''')

        for field in Contants.objects.filter(parent__code='lotsman_attibutes'):
            fields_sql.append(f'''( SELECT kat.id
                                               FROM kd_document_attributes kat
                                                 JOIN kd_lotsman_document_attr_cross dc ON kat.id = dc.attribute_id
                                                 JOIN ckk_attr_type att ON att.id = kat.attr_type_id
                                              WHERE dc.document_id = lts.id AND att.code::text = '{field.code}'::text limit 1) AS "{field.code}_id"''')
            # fields_sql.append(f'''( SELECT kat.value_str
            #                                    FROM kd_document_attributes kat
            #                                      JOIN kd_lotsman_document_attr_cross dc ON kat.id = dc.attribute_id
            #                                      JOIN ckk_attr_type att ON att.id = kat.attr_type_id
            #                                   WHERE dc.document_id = lts.id AND att.code::text = '{field.code}'::text limit 1) AS "{field.code}_value_str"''')
            # fields_sql.append(f'''( SELECT kat.value_int
            #                                    FROM kd_document_attributes kat
            #                                      JOIN kd_lotsman_document_attr_cross dc ON kat.id = dc.attribute_id
            #                                      JOIN ckk_attr_type att ON att.id = kat.attr_type_id
            #                                   WHERE dc.document_id = lts.id AND att.code::text = '{field.code}'::text limit 1) AS "{field.code}_value_int"''')
        # sql_array.append(f'REFRESH MATERIALIZED VIEW {m_view_name};')

        if len(fields_sql) > 0:
            sql_str = ';\n'.join(sql_array).replace('$FIELDS', ',\n'.join(fields_sql))
            sql_str = sql_str.replace('$COMMA', ',')
        else:
            sql_str = ';\n'.join(sql_array).replace('$FIELDS', '')
            sql_str = sql_str.replace('$COMMA', '')

        with connection.cursor() as cursor:
            logger.debug(f'\n{sql_str}')
            cursor.execute(sql_str)
            logger.debug(f'kd_lotsman_documents_hierarcy_mview recreated')

    @staticmethod
    def getRecord(record):
        res = {
            'id': record.id,
            'parent': record.parent.id if record.parent else None,
            'editing': record.editing,
            'deliting': record.deliting,
        }
        return res

    def get_queryset(self):
        return Lotsman_documents_hierarcyQuerySet(self.model, using=self._db)

    def deleteFromRequest(self, request, removed=None, ):
        request = DSRequest(request=request)
        res = 0
        tuple_ids = request.get_tuple_ids()
        with transaction.atomic():
            for id, mode in tuple_ids:
                if mode == 'hide':
                    super().filter(id=id).soft_delete()
                else:
                    qty, _ = super().filter(id=id).delete()
                res += qty
        return res


class Lotsman_documents_hierarcy(AuditModel):
    id = BigIntegerField(primary_key=True, verbose_name="Идентификатор")
    attr_type = ForeignKeyProtect(Attr_type, verbose_name='Тип документа')
    document = ForeignKeyProtect(Documents)
    props = Lotsman_documents_hierarcyManager.get_props()

    objects = Lotsman_documents_hierarcyManager()

    def __str__(self):
        return f'ID:{self.id}, attr_type: {self.attr_type}, document: {self.document}, props: {self.props}'

    def __repr__(self):
        return self.__str__()

    class Meta:
        verbose_name = 'Иерархия документа из Лоцмана'
