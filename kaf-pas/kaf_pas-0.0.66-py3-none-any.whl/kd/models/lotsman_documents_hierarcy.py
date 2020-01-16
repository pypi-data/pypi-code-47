import logging

from bitfield import BitField
from django.db import transaction
from django.db.models import BigIntegerField

from isc_common import Stack
from isc_common.fields.related import ForeignKeyProtect
from isc_common.http.DSRequest import DSRequest
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
    def make_lines(parent, items_pairs, logger):
        from kaf_pas.ckk.models.item import Item
        from kaf_pas.kd.models.lotsman_documents_hierarcy_view import Lotsman_documents_hierarcy_view
        from kaf_pas.ckk.models.item_line import Item_line
        from kaf_pas.ckk.models.item_line import Item_lineManager

        if not isinstance(parent, Item):
            raise Exception(f'item mut be Item instnce.')

        for lotsman_documents_hierarcy in Lotsman_documents_hierarcy_view.objects_tree.get_descendants(
                child_id='id',
                child_parent_value=parent.lotsman_document.id,
                where_clause=f'where props=1',
                order_by_clause='order by level',
                include_self=False):

            item, _ = Lotsman_documents_hierarcyManager.get_item(lotsman_documents_hierarcy, 'id', items_pairs, logger)

            if lotsman_documents_hierarcy.attr_name != 'Материал':

                if lotsman_documents_hierarcy.section == None:
                    if lotsman_documents_hierarcy.attr_name in ['Чертеж', 'Спецификация']:
                        lotsman_documents_hierarcy.section = 'Документация'
                    elif lotsman_documents_hierarcy.attr_name in ['Сборочная единица']:
                        lotsman_documents_hierarcy.section = 'Сборочные единицы'

                if lotsman_documents_hierarcy.section == None:
                    raise Exception(f'\n\nNot Founf section in \n {lotsman_documents_hierarcy}')

                Документ_на_материал = None
                Наименование_материала = None
                Документ_на_сортамент = None
                Наименование_сортамента = None

                for lotsman_documents_hierarcy_view in Lotsman_documents_hierarcy_view.objects.filter(parent_id=lotsman_documents_hierarcy.id):
                    if lotsman_documents_hierarcy_view.attr_name == 'Материал':
                        Документ_на_материал = lotsman_documents_hierarcy_view.Документ_на_материал
                        Наименование_материала = lotsman_documents_hierarcy_view.Наименование_материала
                        Документ_на_сортамент = lotsman_documents_hierarcy_view.Документ_на_сортамент
                        Наименование_сортамента = lotsman_documents_hierarcy_view.Наименование_сортамента
                        break

                item_line, created = Item_line.objects.update_or_create(
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
                        SPC_CLM_MATERIAL=lotsman_documents_hierarcy.SPC_CLM_MATERIAL if lotsman_documents_hierarcy.SPC_CLM_MATERIAL else Наименование_материала,
                        SPC_CLM_USER=lotsman_documents_hierarcy.SPC_CLM_USER,
                        SPC_CLM_KOD=lotsman_documents_hierarcy.SPC_CLM_KOD,
                        SPC_CLM_FACTORY=lotsman_documents_hierarcy.SPC_CLM_FACTORY,
                        Документ_на_материал=Документ_на_материал,
                        Наименование_материала=Наименование_материала,
                        Документ_на_сортамент=Документ_на_сортамент,
                        Наименование_сортамента=Наименование_сортамента,
                        section=lotsman_documents_hierarcy.section,
                        section_num=Item_lineManager.section_num(lotsman_documents_hierarcy.section),
                        subsection=lotsman_documents_hierarcy.subsection,
                    )
                )

                # if logger and created:
                #     logger.logging(f'\nAdded line: {item_line}', 'debug')

    @staticmethod
    def get_item(lotsman_documents_hierarcy, attribute, items_pairs, logger):
        from kaf_pas.ckk.models.item import Item

        items = [item[1] for item in items_pairs.stack if item[0] == lotsman_documents_hierarcy.__getattribute__(attribute)]
        if len(items) == 0:
            STMP_1 = lotsman_documents_hierarcy.SPC_CLM_NAME
            STMP_2 = lotsman_documents_hierarcy.SPC_CLM_MARK

            item, created = Item.objects.get_or_create(
                STMP_1=STMP_1,
                STMP_2=STMP_2,
                props=Item.props.relevant | Item.props.from_lotsman,
                version=lotsman_documents_hierarcy._Version.value_int,
                defaults=dict(
                    lotsman_document_id=lotsman_documents_hierarcy.id,
                )
            )
            items_pairs.push((lotsman_documents_hierarcy.id, item))

            DocumentManager.link_image_to_lotsman_item(item, logger)

            # if logger and created:
            #     logger.logging(f'\nAdded parent: {item}', 'debug')

            return item, created
        elif len(items) == 1:
            return items[0], False
        else:
            raise Exception(f'Неоднозначный выбор.')

    @staticmethod
    def make_items(logger, owner=None):
        from kaf_pas.ckk.models.item import Item
        from kaf_pas.ckk.models.item_refs import Item_refs
        from kaf_pas.kd.models.document_attributes import Document_attributesManager
        from kaf_pas.kd.models.lotsman_documents_hierarcy_view import Lotsman_documents_hierarcy_view

        items_pairs = Stack()

        with transaction.atomic():
            imp_frpm_lotsman_label = 'Импорт из Лоцмана'

            parent, created = Item.objects.get_or_create(
                STMP_1=Document_attributesManager.get_or_create_attribute(
                    attr_codes='STMP_1',
                    value_str=imp_frpm_lotsman_label,
                    logger=logger
                ),
                props=Item.props.relevant | Item.props.from_lotsman
            )

            from kaf_pas.system.models.contants import Contants
            item_top_level, _ = Contants.objects.update_or_create(code='top_level', defaults=dict(name='Вершины товарных позиций'))
            const4, _ = Contants.objects.update_or_create(code='lotsman_top_level', defaults=dict(parent=item_top_level, name=imp_frpm_lotsman_label, value=parent.id))

            Item_refs.objects.get_or_create(
                child=parent
            )

            cnt = Lotsman_documents_hierarcy_view.objects_tree.get_descendants_count(
                child_id='id',
                where_clause=f'where props=1',
                include_self=False)

            cnt *= 2

            if cnt > 0:
                if owner != None:
                    owner.cnt += cnt

                for lotsman_documents_hierarcy in Lotsman_documents_hierarcy_view.objects_tree.get_descendants(
                        child_id='id',
                        where_clause=f'where props=1',
                        order_by_clause='order by level',
                        include_self=False):

                    if lotsman_documents_hierarcy.attr_name.lower() != 'Материал'.lower():
                        item, created1 = Lotsman_documents_hierarcyManager.get_item(
                            lotsman_documents_hierarcy=lotsman_documents_hierarcy,
                            attribute='id',
                            items_pairs=items_pairs,
                            logger=logger
                        )

                        if lotsman_documents_hierarcy.parent_id != None:
                            parent, created1 = Lotsman_documents_hierarcyManager.get_item(
                                lotsman_documents_hierarcy=lotsman_documents_hierarcy,
                                attribute='parent_id',
                                items_pairs=items_pairs,
                                logger=logger
                            )

                        if parent != item:
                            item_refs, created2 = Item_refs.objects.get_or_create(parent=parent, child=item)

                        # FOR DEBUG
                        if created == True or created1 == True or created2 == True:
                            pass
                        # END FOR DEBUG

                    if owner != None:
                        owner.pbar_progress()

                for lotsman_documents_hierarcy in Lotsman_documents_hierarcy_view.objects_tree.get_descendants(
                        child_id='id',
                        where_clause=f'where props=1',
                        order_by_clause='order by level',
                        include_self=False):

                    if lotsman_documents_hierarcy.attr_name.lower() == 'Сборочная единица'.lower():
                        item, _ = Lotsman_documents_hierarcyManager.get_item(lotsman_documents_hierarcy, 'id', items_pairs, logger)

                        Lotsman_documents_hierarcyManager.make_lines(parent=item, items_pairs=items_pairs, logger=logger)

                    Lotsman_documents_hierarcy.objects.update_or_create(
                        id=lotsman_documents_hierarcy.id,
                        defaults=dict(
                            props=lotsman_documents_hierarcy.props | Lotsman_documents_hierarcy.props.beenItemed
                        ))

                    if owner != None:
                        owner.pbar_progress()

                # FOR DEBUG
                pass
                # END FOR DEBUG

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
        m_view_recurs_name = 'kd_lotsman_documents_hierarcy_recurs_view'

        sql_array.append(f'DROP VIEW IF EXISTS {m_view_recurs_name} CASCADE')
        sql_array.append(f'DROP MATERIALIZED VIEW IF EXISTS {m_view_name} CASCADE')
        sql_array.append(f'''CREATE MATERIALIZED VIEW {m_view_name} AS SELECT lts.id,
                                                                                   lts.deleted_at,
                                                                                   lts.editing,
                                                                                   lts.deliting,
                                                                                   lts.lastmodified,                                                                                
                                                                                   ltsr.parent_id,
                                                                                   lts.props,
                                                                                   lts.attr_type_id,
                                                                                   lts.document_id,
                                                                                   CASE
                                                                                        WHEN (select count(1) as count
                                                                                              from kd_lotsman_documents_hierarcy_refs hr                                                            	
                                                                                              where hr.parent_id = lts.id) > 0 THEN true
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
            logger.debug(f'{m_view_name} recreated')

            sql_array = []
            sql_array.append(f'''CREATE VIEW {m_view_recurs_name} AS select * from (WITH RECURSIVE r AS (
                                    SELECT *, 1 AS level
                                    FROM {m_view_name}
                                    WHERE parent_id IS NULL
                                
                                    union all
                                
                                    SELECT {m_view_name}.*, r.level + 1 AS level
                                    FROM {m_view_name}
                                             JOIN r
                                                  ON {m_view_name}.parent_id = r.id)                                
                                select * from r order by level) as a''')
            sql_str = ';\n'.join(sql_array)
            logger.debug(f'\n{sql_str}')
            cursor.execute(sql_str)
            logger.debug(f'{m_view_recurs_name} recreated')

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
