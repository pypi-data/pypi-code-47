import logging
import uuid

from django.conf import settings
from django.db import transaction, connection
from django.forms import model_to_dict

from isc_common.datetime import DateToStr
from isc_common.fields.related import ForeignKeyProtect
from isc_common.models.audit import AuditManager, AuditModel, AuditQuerySet
from isc_common.ws.progressStack import ProgressStack
from kaf_pas.planing.models.operation_types import Operation_types
from kaf_pas.planing.models.status_operation_types import Status_operation_types
from kaf_pas.production.models.launch_operation_material import Launch_operations_material
from kaf_pas.production.models.launch_operation_resources import Launch_operation_resources
from kaf_pas.production.models.launch_operations_item import Launch_operations_item

logger = logging.getLogger(__name__)


class OperationsQuerySet(AuditQuerySet):
    def delete(self):
        return super().delete()

    def create(self, **kwargs):
        return super().create(**kwargs)

    def filter(self, *args, **kwargs):
        return super().filter(*args, **kwargs)


class OperationsManager(AuditManager):

    @staticmethod
    def make_routing(data):
        from isc_common.auth.models.user import User
        from kaf_pas.planing.models.operation_item import Operation_item
        from kaf_pas.planing.models.operation_material import Operation_material
        from kaf_pas.planing.models.operation_refs import Operation_refs
        from kaf_pas.planing.models.operation_resources import Operation_resources
        from kaf_pas.planing.models.operation_standard_prod import Operation_standard_prod
        from kaf_pas.production.models.launches import Launches
        from kaf_pas.planing.models.operation_locations import Operation_locations
        from kaf_pas.planing.models.operation_launches import Operation_launches
        from kaf_pas.planing.models.operation_level import Operation_level

        logger.debug(f'data: {data}')

        OperationsManager.clean_routing(data=data)

        launch_id = data.get('id')

        launch = Launches.objects.get(id=launch_id)

        user = User.objects.get(id=data.get('user_id'))

        progress = ProgressStack(
            host=settings.WS_HOST,
            port=settings.WS_PORT,
            channel=f'common_{user.username}',
        )

        id_progress1 = f'launch_{launch.id}_{user.id}'

        demand_str = f'<h3>Подготовка данных для Маршрутизации/Расписания : Запуск № {launch.code} от {DateToStr(launch.date)}</h3>'

        cnt = 0
        mat_view_name = f'tmp_{str(uuid.uuid4()).replace("-", "_")}'
        items = []

        sql_txt = f'''CREATE MATERIALIZED VIEW public.{mat_view_name}
                    TABLESPACE informica
                    AS 
                    with recursive r as (
                                            select *,
                                                   1 as level
                                            from production_launch_item_refs
                                            where parent_id is null
                                              and launch_id = {launch_id}
                                            union all
                                            select production_launch_item_refs.*,
                                                   r.level + 1 as level
                                            from production_launch_item_refs
                                                     join r
                                                          on
                                                              production_launch_item_refs.parent_id = r.child_id)
                                        
                                        select r1.id,
                                               r1.parent_id,
                                               r1.child_id,
                                               r1.launch_id,
                                               r1.stmp1,
                                               r1.stmp2,
                                               r1.qty,
                                               r1.level
                                        from (select distinct r.id,
                                                              r.parent_id,
                                                              r.child_id,
                                                              stmp1.value_str                         stmp1,
                                                              stmp2.value_str                         stmp2,
                                                              r.launch_id,
                                                              (
                                                                  select coalesce(kda.value_int, kda.value_str::numeric(19, 4), 0)
                                                                  from production_launch_item_line plil
                                                                           join kd_document_attributes kda on kda.id = plil."SPC_CLM_COUNT_id"
                                                                  where plil.child_id = r.child_id
                                                                    and plil.parent_id = r.parent_id
                                                                    and plil.launch_id = r.launch_id) qty,
                                                              (
                                                                  select plil.section
                                                                  from production_launch_item_line plil
                                                                  where plil.child_id = r.child_id
                                                                    and plil.parent_id = r.parent_id
                                                                    and plil.launch_id = r.launch_id) section,
                                                              level
                                              from r
                                                       join ckk_item ci on ci.id = r.child_id
                                                       join kd_document_attributes stmp1 on stmp1.id = ci."STMP_1_id"
                                                       join kd_document_attributes stmp2 on stmp2.id = ci."STMP_2_id"
                                              where r.launch_id = {launch_id}
                                              order by level desc) r1
                                        where lower(r1.section) != 'документация'
                                 WITH DATA;'''

        with transaction.atomic():
            with connection.cursor() as cursor:
                status, _ = Status_operation_types.objects.get_or_create(
                    opertype=settings.OPERS_TYPES_STACK.ROUTING_TASK,
                    code='none',
                    defaults=dict(name='не определен', deliting=False, editing=False)
                )

                cursor.execute(sql_txt)

                cursor.execute(f'select count(*) from {mat_view_name}')
                count, = cursor.fetchone()

                logger.debug(f'{mat_view_name} count(*): {count}')

                progress.show(
                    title=f'<b>Обработано товарных позиций</b>',
                    label_contents=demand_str,
                    cntAll=count * 2,
                    id=id_progress1
                )

                cursor.execute(f'select * from {mat_view_name} order by level desc')
                rows = cursor.fetchall()
                for row in rows:
                    id, parent_id, child_id, launch_id, stmp1, stmp2, qty, level = row

                    if len([item for item in items if item.get('item_id') == child_id]) == 0:
                        operation_income = None
                        cnt1 = Launch_operations_item.objects.filter(item_id=child_id, launch_id=launch_id).count()
                        if cnt1 > 0:
                            first_operation = None
                            for launch_operations_item in Launch_operations_item.objects.filter(item_id=child_id, launch_id=launch_id).order_by('num'):
                                operation_outcome = Operations.objects.create(
                                    opertype=settings.OPERS_TYPES_STACK.ROUTING_TASK,
                                    status=status
                                )

                                Operation_launches.objects.create(operation=operation_outcome, launch=launch)
                                Operation_level.objects.create(operation=operation_outcome, level=level)

                                if operation_income == None:
                                    first_operation = operation_outcome

                                Operation_item.objects.get_or_create(operation=operation_outcome, item=launch_operations_item.item)

                                for launch_operation_material in Launch_operations_material.objects.filter(launch_operationitem=launch_operations_item):
                                    if launch_operation_material.material_askon != None:
                                        Operation_material.objects.get_or_create(operation=operation_outcome, material=launch_operation_material.material_askon)
                                    if launch_operation_material.material != None:
                                        Operation_standard_prod.objects.get_or_create(operation=operation_outcome, material=launch_operation_material.material)

                                if Launch_operation_resources.objects.filter(launch_operationitem=launch_operations_item) == 0:
                                    raise Exception(f'Для : {stmp1} : {stmp2} ID={child_id} не задан ресурс.')

                                for launch_operation_resources in Launch_operation_resources.objects.filter(launch_operationitem=launch_operations_item):
                                    if launch_operation_resources.resource != None:
                                        Operation_resources.objects.get_or_create(operation=operation_outcome, resource=launch_operation_resources.resource)
                                    if launch_operation_resources.location != None:
                                        Operation_locations.objects.get_or_create(operation=operation_outcome, location=launch_operation_resources.location)

                                Operation_refs.objects.get_or_create(income=operation_income, outcome=operation_outcome)
                                operation_income = operation_outcome
                                cnt1 -= 1
                                if cnt1 == 0:
                                    items.append(dict(item_id=child_id, first_operation=first_operation, last_operation=operation_outcome))
                        else:
                            raise Exception(f'Для : {stmp1} : {stmp2} ID={child_id} не задано ни одной операции.')

                    progress.setCntDone(cnt=cnt, id=id_progress1)
                    cnt += 1

                for row in rows:
                    id, parent_id, child_id, launch_id, stmp1, stmp2, qty, level = row

                    if len([item for item in items if item.get('item_id') == parent_id]) == 0:

                        operation_income = None
                        cnt1 = Launch_operations_item.objects.filter(item_id=parent_id, launch_id=launch_id).count()
                        if cnt1 > 0:
                            first_operation = None
                            for launch_operations_item in Launch_operations_item.objects.filter(item_id=parent_id, launch_id=launch_id).order_by('num'):
                                operation_outcome = Operations.objects.create(
                                    opertype=settings.OPERS_TYPES_STACK.ROUTING_TASK,
                                    status=status
                                )

                                Operation_launches.objects.create(operation=operation_outcome, launch=launch)

                                if operation_income == None:
                                    first_operation = operation_outcome

                                Operation_item.objects.get_or_create(operation=operation_outcome, item=launch_operations_item.item)
                                Operation_level.objects.create(operation=operation_outcome, level=level)

                                for launch_operation_material in Launch_operations_material.objects.filter(launch_operationitem=launch_operations_item):
                                    if launch_operation_material.material_askon != None:
                                        Operation_material.objects.get_or_create(operation=operation_outcome, material=launch_operation_material.material_askon)
                                    if launch_operation_material.material != None:
                                        Operation_standard_prod.objects.get_or_create(operation=operation_outcome, material=launch_operation_material.material)

                                if Launch_operation_resources.objects.filter(launch_operationitem=launch_operations_item) == 0:
                                    raise Exception(f'Для : {stmp1} : {stmp2} ID={child_id} не задан ресурс.')

                                for launch_operation_resources in Launch_operation_resources.objects.filter(launch_operationitem=launch_operations_item):
                                    if launch_operation_resources.resource != None:
                                        Operation_resources.objects.get_or_create(operation=operation_outcome, resources=launch_operation_resources.resource)
                                    if launch_operation_resources.location != None:
                                        Operation_locations.objects.get_or_create(operation=operation_outcome, location=launch_operation_resources.location)

                                Operation_refs.objects.get_or_create(income=operation_income, outcome=operation_outcome)
                                operation_income = operation_outcome
                                cnt1 -= 1
                                if cnt1 == 0:
                                    items.append(dict(item_id=parent_id, first_operation=first_operation, last_operation=operation_outcome))
                        else:
                            raise Exception(f'Для : {stmp1} : {stmp2} не задано ни одной операции.')

                    sql_parents = f'''select child_id, stmp1, stmp2 from {mat_view_name} where parent_id = %s'''
                    cursor.execute(sql_parents, [parent_id])
                    parents_rows = cursor.fetchall()
                    for parents_row in parents_rows:
                        _child_id, stmp1, stmp2 = parents_row
                        _childs = [item for item in items if item.get('item_id') == _child_id]
                        if len(_childs) == 0:
                            raise Exception(f'Для {stmp1} : {stmp2} ID={_child_id} не найдена операция.')
                        elif len(_childs) > 1:
                            raise Exception(f'Для {stmp1} : {stmp2} ID={_child_id} неоднозначная операция.')

                        _child = _childs[0]

                        Operation_refs.objects.get_or_create(income=_child.get('last_operation'), outcome=first_operation)
                        deleted, _ = Operation_refs.objects.filter(income__isnull=True, outcome=first_operation).delete()
                    progress.setCntDone(cnt=cnt, id=id_progress1)
                    cnt += 1

                progress.close(id=id_progress1)
                cursor.execute(f'DROP MATERIALIZED VIEW {mat_view_name}')

            launch.props |= Launches.props.routing_maked
            launch.save()

    def clean_routing(data):
        from kaf_pas.production.models.launches import Launches
        from kaf_pas.planing.models.operation_launches import Operation_launches
        from isc_common.auth.models.user import User

        logger.debug(f'data: {data}')

        launch_id = data.get('id')
        launch = Launches.objects.get(id=launch_id)

        cntAll = Operation_launches.objects.filter(launch=launch).count()

        if cntAll > 0:
            user = User.objects.get(id=data.get('user_id'))

            progress = ProgressStack(
                host=settings.WS_HOST,
                port=settings.WS_PORT,
                channel=f'common_{user.username}',
            )

            with transaction.atomic():
                id_progress1 = f'launch_{launch.id}_{user.id}'

                demand_str = f'<h3>Очистка данных Маршрутизации/Расписания : Запуск № {launch.code} от {DateToStr(launch.date)}</h3>'


                launch.props &= ~Launches.props.routing_maked
                launch.save()

                progress.show(
                    title=f'<b>Обработано товарных позиций</b>',
                    label_contents=demand_str,
                    cntAll=Operation_launches.objects.filter(launch=launch).count(),
                    id=id_progress1
                )

                cnt = 0

                for operation_launches in Operation_launches.objects.filter(launch=launch):
                    operation_launches.operation.delete()
                    progress.setCntDone(cnt=cnt, id=id_progress1)
                    cnt += 1

                progress.close(id=id_progress1)
        return model_to_dict(launch)


    @staticmethod
    def getRecord(record):
        res = {
            'id': record.id,
            'opertype_id': record.opertype.id,
            'opertype_full_name': record.opertype.full_name,
            'value': record.value,
        }
        return res

    def get_queryset(self):
        return OperationsQuerySet(self.model, using=self._db)


class Operations(AuditModel):
    opertype = ForeignKeyProtect(Operation_types)
    status = ForeignKeyProtect(Status_operation_types)

    objects = OperationsManager()

    def __str__(self):
        return f"ID:{self.id}, opertype: [{self.opertype}], status: [{self.status}]"

    def __repr__(self):
        return self.__str__()

    class Meta:
        verbose_name = 'Опреации учавствующие в планировании'
