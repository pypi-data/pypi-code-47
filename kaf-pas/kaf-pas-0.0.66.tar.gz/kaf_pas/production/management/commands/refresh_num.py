import logging

from django.core.management import BaseCommand
from django.db import transaction, connection

from kaf_pas.production.models.operations_item import Operations_item, Operations_itemManager
from kaf_pas.production.models.ready_2_launch import Ready_2_launchManager

logger = logging.getLogger(__name__)


class Command(BaseCommand):
    help = "Тестирование"

    def handle(self, *args, **options):
        Operations_itemManager.refresh_num()
