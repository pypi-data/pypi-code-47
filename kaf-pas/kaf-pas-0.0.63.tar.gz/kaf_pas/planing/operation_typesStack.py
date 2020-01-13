import logging

from django.db import ProgrammingError

logger = logging.getLogger(__name__)


class Operation_typesStack:
    def get_first_item_of_tuple(self, tp):
        res, _ = tp
        return res

    def __init__(self):
        from kaf_pas.planing.models.operation_types import Operation_types

        try:
            self.ASSEMBLY_TASK = self.get_first_item_of_tuple(Operation_types.objects.update_or_create(code='AS_TSK', defaults=dict(
                props=Operation_types.props.isoper |
                      Operation_types.props.plus,
                name='Задание на комплектацию',
                editing=False,
                deliting=False,
            )))

            self.PRODUCTION_TASK = self.get_first_item_of_tuple(Operation_types.objects.update_or_create(code='PRD_TSK', defaults=dict(
                props=Operation_types.props.isoper |
                      Operation_types.props.plus,
                name='Задание на производство',
                editing=False,
                deliting=False,
            )))

            self.ROUTING_TASK = self.get_first_item_of_tuple(Operation_types.objects.update_or_create(code='RT_TSK', defaults=dict(
                props=Operation_types.props.isoper,
                name='Маршрутизация',
                editing=False,
                deliting=False,
            )))
        except ProgrammingError as ex:
            logger.warning(ex)
