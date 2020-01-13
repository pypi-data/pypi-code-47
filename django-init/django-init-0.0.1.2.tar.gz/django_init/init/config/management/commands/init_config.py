from django.core.management.base import CommandError
from common.utils.commands import InitBaseCommand
from common.menus.models import *


class Command(InitBaseCommand):
    help = 'Initial data for Menus'
    cls = MenuItem
    init = [
        (1, 'article-detail', 'Статья'),
        (2, 'article-list', 'Список статей'),
        (3, 'section-detail', 'Раздел'),
        (4, 'section-list', 'Список разделов'),
        (5, 'contact', 'Контакты'),
    ]

    def load(self):
        self.cls.objects.all().delete()
        for id, path, title in self.init:
            try:
                obj = self.cls(id=id, path=path, title=title, menu_id=1)
                obj.save()
            except Exception as e:
                print(e)
                raise CommandError('Template "%s" does not create' % path)
            self.stdout.write(self.style.SUCCESS('Successfully created template "%s"' % path))
