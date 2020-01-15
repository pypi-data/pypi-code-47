from django.core.management.base import BaseCommand

from django_init.apps.app import AppsManagement


class Command(BaseCommand):
    help = 'Creates a Django app directory structure for the given app name in the current directory or the given destination.'

    def add_arguments(self, parser):
        parser.add_argument('command_name', help='Name of command')
        parser.add_argument('apps_name', nargs='*', help='Names of the application or project.')

    def handle(self, *args, **options):
        print(options)
        app = AppsManagement()
        # if options['all']:
        #     app = AppsManagement()
        #     app.create_all()
        if options['apps_name']:
            for app_name in options['apps_name']:
                if app_name == 'app':
                    app.create_project()
                else:
                    app.create_app(app_name)
        else:
            print('Available applications:')
            for _, app_name in app.get_apps():
                print('    %s' % app_name)
