from django.core.management.base import BaseCommand

from django_init.management import add_arguments
from django_init.apps.app import AppsManagement


class Command(BaseCommand):
    help = (
        "Creates a Django project directory structure for the given project "
        "name in the current directory or optionally in the given directory."
    )
    # missing_args_message = "You must provide a project name."

    def add_arguments(self, parser):
        add_arguments(parser)

    def handle(self, *args, **options):
        app = AppsManagement()
        app.create_project('app')
