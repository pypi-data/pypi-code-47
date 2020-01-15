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
        parser.add_argument('command_name', help='Name of command')
        parser.add_argument('project_name', nargs='?', help='Name of project')

    def handle(self, *args, **options):
        app = AppsManagement()
        project_name = options.get('project_name')

        if project_name:
            if project_name == 'base':
                app.create_project()
                app.create_app('logs')
                app.create_app('common')
                app.create_app('config')
                app.create_app('menus')
                app.create_app('seo')
                app.create_app('accounts')
                app.create_app('feedback')
                app.create_app('templates')
            else:
                print('Unknown name of command: %r' % project_name)
        else:
            app.create_project()
