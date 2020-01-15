from django.core.management.base import BaseCommand

from django_init.management import add_arguments
from django_init.apps.app import AppsManagement


class Command(BaseCommand):
    help = 'Creates a Django app directory structure for the given app name in the current directory or the given destination.'

    def add_arguments(self, parser):
        add_arguments(parser)

    def handle(self, *args, **options):
        if options['all']:
            app = AppsManagement()
            app.create_all()
        elif options['values']:
            app = AppsManagement()
            for app_name in options['values']:
                app.create_app(app_name)
