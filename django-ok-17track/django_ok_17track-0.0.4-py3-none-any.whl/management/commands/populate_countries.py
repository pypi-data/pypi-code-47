from django.core.management.base import BaseCommand
from ...services import populate_countries


class Command(BaseCommand):
    help = 'Populates 17track countries from external api'

    def handle(self, *args, **options):
        populate_countries()
