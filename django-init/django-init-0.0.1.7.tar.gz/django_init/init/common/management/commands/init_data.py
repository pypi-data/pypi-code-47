from django.core.management import call_command
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = 'Load all initial data'

    def add_arguments(self, parser):
        parser.add_argument(
            '-f',
            '--fixture',
            action='store_true',
            help='Create fixture of model'
        )

        parser.add_argument(
            '-y',
            '--yes',
            action='store_true',
            help='Automatic yes to prompts'
        )

    def handle(self, *args, **options):
        call_command('init_currencies', **options)
        call_command('init_rates', **options)
        call_command('init_users', **options)
        call_command('init_transfers', **options)
