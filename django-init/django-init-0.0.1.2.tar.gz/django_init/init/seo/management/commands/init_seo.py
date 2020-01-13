from django.core.management.base import BaseCommand, CommandError
from django.utils.translation import ugettext_lazy as _

from common.seo.models import ConfigSEO
from sections.models import Section


class Command(BaseCommand):
    help = 'Initial seo data'
    groups = [
        {'group': 'home', 'group_title': _('Главная страница'), 'model': None},
        {'group': 'section', 'group_title': _('Разделы'), 'model': Section},
        # {'group': 'article', 'group_title': _('Статьи', 'model'): ConfigSEO},
        # {'group': 'category', 'group_title': _('Категории'), 'model': ConfigSEO},
        # {'group': 'product', 'group_title': _('Товары'), 'model': ConfigSEO},
    ]
    keys = dict(
        title=_('Заголовок'),
        keywords=_('Ключевые слова'),
        description=_('Описание'),
        h1='H1',
    )

    def get_fields(self, model):
        if model:
            return ', '.join(sorted([f.name for f in model._meta.get_fields()]))
        return ''

    def handle(self, *args, **options):
        i = 1
        # ConfigSEO.objects.all().delete()
        for item in self.groups:
            for k, v in self.keys.items():
                data = dict(
                    group_title=item['group_title'],
                    group=item['group'],
                    title=v,
                    key=k,
                    description=self.get_fields(item['model']),
                    value=v if item['group'] == 'home' else ''
                )
                try:
                    ConfigSEO.objects.update_or_create(id=i, defaults=data)
                except Exception as e:
                    print(e)
                    raise CommandError('Seo data "%s" does not created - %s' % (item['group_title'], k))
                self.stdout.write(self.style.SUCCESS('Successfully created seo data: %s - %s' % (item['group_title'], k)))
                i += 1
