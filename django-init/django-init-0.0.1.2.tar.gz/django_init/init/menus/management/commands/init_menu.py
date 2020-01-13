from django.core.management.base import BaseCommand, CommandError
from common.utils.commands import InitBaseCommand
from common.menus.models import *


class Command(BaseCommand):
    help = 'Initial data for Menus'
    init = [
        (1, '/article-detail/', 'Статья'),
        (2, '/article-list/', 'Список статей'),
        (3, '/section-detail/', 'Раздел'),
        (4, '/section-list/', 'Список разделов'),
        (5, '/contact/', 'Контакты'),
        (6, '/catalog/', 'Каталог'),
    ]

    def handle(self, *args, **options):
        try:
            obj = Menu(title='Главное меню', key='main', is_active=True)
            obj.save()
        except Exception as e:
            print(e)

        for id, path, title in self.init:
            data = dict(
                path=path,
                title=title,
                menu_id=1,
                is_active=True,
            )
            try:
                MenuItem.objects.update_or_create(id=id, defaults=data)
            except Exception as e:
                print(e)
                raise CommandError('Menu item %s - %s does not created' % (title, path))
            self.stdout.write(self.style.SUCCESS('Successfully created menu item: %s - %s' % (title, path)))
