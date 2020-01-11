from django.core.management.base import BaseCommand
from ...services import populate_carriers


class Command(BaseCommand):
    help = 'Populates 17track carriers from external api'

    def handle(self, *args, **options):
        populate_carriers()
