from django.core.management.base import BaseCommand, CommandError
from sections.models import Template
from functools import wraps


def confirm_init(func):
    @wraps(func)
    def _wrapper(*args, **kwargs):
        while True:
            query = input('Do you want to update multiple rows from %s? [Y/n]' % self.cls().__class__.__name__)
            if query == '' or not query.lower() in ['yes', 'y', 'no', 'n']:
                print('Please answer with yes or no!')
            else:
                if query.lower()[0] == 'y':
                    func(*args, **kwargs)
                break
    return _wrapper


class InitBaseCommand(BaseCommand):
    help = 'Initial data for ... '
    model = None

    # def add_arguments(self, parser):
    #     parser.add_argument('poll_ids', nargs='+', type=int)

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
            act = 'created' if created else 'updated'
            self.stdout.write(self.style.SUCCESS('Successfully %s %s: %s' % (act, self.model().__class__.__name__, obj)))
        """
        raise NotImplementedError('subclasses of InitBaseCommand must provide a load() method')

    def confirm_init(self):
        if not self.model:
            raise NameError('Model is not defined')
        while True:
            query = input('Do you want to update or create multiple rows from %s? [Y/n]' % self.model().__class__.__name__)
            if query == '' or not query.lower() in ['yes', 'y', 'no', 'n']:
                print('Please answer with yes or no!')
            else:
                if query.lower()[0] == 'y':
                    self.load()
                break

    def handle(self, *args, **options):
        self.confirm_init()
