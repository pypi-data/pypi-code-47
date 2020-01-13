import logging

from django.core.management import BaseCommand
from isc_common.logger.Logger import Logger

from kaf_pas.kd.models.documents import Documents

logger = logging.getLogger(__name__)
logger.__class__ = Logger


class Command(BaseCommand):
    help = 'Создание товаоных позиций после импорта из Лоцмана'
    def handle(self, *args, **options):
        try:
            from kaf_pas.kd.models.lotsman_documents_hierarcy import Lotsman_documents_hierarcyManager
            Lotsman_documents_hierarcyManager.make_items(document=Documents.objects.get(id=242742), logger=logger)
        except Exception as ex:
            raise ex
