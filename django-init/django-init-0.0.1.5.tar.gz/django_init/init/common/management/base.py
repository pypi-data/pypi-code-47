import os

from django.apps import apps
from django.core import serializers
from django.core.management.base import BaseCommand


def create_fixture(model):
    try:
        app_label, model_label = model.__module__.split('.')
        app_config = apps.get_app_config(app_label)
        path = '%s/fixtures/' % app_config.path
        file = '%s%s.json' % (path, model._meta.model_name)

        if not os.path.exists(path):
            try:
                os.mkdir(path)
            except Exception as e:
                raise SystemExit(e)

        with open(file, 'w') as out:
            serializers.serialize('json', model.objects.all(), stream=out, indent=2)
    except Exception as e:
        print(e)


class InitBaseCommand(BaseCommand):
    help = 'Initial data for ... '
    model = None

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

    def load(self):
        """
        The actual logic of the command. Subclasses must implement
        this method.
        Example:
        for id, path, title in self.init:
            try:
                data = dict(
                    path=path,
                    title=title
                )
                obj, created = self.model.objects.update_or_create(id=id, defaults=data)
            except Exception as e:
                print(e)
                raise CommandError('%s %s - does not created' % (self.model().__class__.__name__, title))
            action = 'created' if created else 'updated'
            self.stdout.write(self.style.SUCCESS('Successfully %s %s: %s' % (action, self.model().__class__.__name__, obj)))
        """
        raise NotImplementedError('subclasses of InitBaseCommand must provide a load() method')

    def confirm_init(self, *args, **options):
        if not self.model:
            raise NameError('Model is not defined')
        else:
            try:
                self.model._meta.model_name
            except AttributeError as e:
                print('Model is not defined')

        if options['yes']:
            self.load()
        else:
            while True:
                query = input('Do you want to update or create multiple rows from %s? [Y/n]' % self.model().__class__.__name__)
                if query == '' or not query.lower() in ['yes', 'y', 'no', 'n']:
                    print('Please answer with yes or no!')
                else:
                    if query.lower()[0] == 'y':
                        self.load()
                    break

    def handle(self, *args, **options):
        self.confirm_init(*args, **options)
        if options['fixture']:
            create_fixture(self.model)
