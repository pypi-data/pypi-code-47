from django.core.management.base import CommandError
from common.utils.commands import InitBaseCommand
from sections.models import Article


class Command(InitBaseCommand):
    help = 'Initial data for Article'
    cls = Article
    init = [
        (1, 'article-detail', 'Статья'),
        (2, 'contact', 'Контакты'),
        (3, 'article-list', 'Список статей'),
        (4, 'section-detail', 'Раздел'),
        (5, 'section-list', 'Список разделов'),
        (6, 'product-detail', 'Товар'),
        (7, 'catalog', 'Список товаров'),
        (8, 'card', 'Корзина'),
        (9, 'checkout', 'Корзина форма'),
        (10, 'delivery', 'Доставка'),
        (11, 'payment', 'Оплата'),
        (12, 'order', 'Заказ'),
    ]

    def load(self):
        self.cls.objects.all().delete()
        for id, path, title in self.init:
            try:
                data = dict(
                    slug=path,
                    title=title,
                    template_id=id
                )
                obj, created = self.cls.objects.update_or_create(id=id, defaults=data)
            except Exception as e:
                print(e)
                raise CommandError('Article "%s" does not created' % path)
            act = 'created' if created else 'updated'
            self.stdout.write(self.style.SUCCESS('Successfully %s article: %s' % (act, title)))

    def handle(self, *args, **options):
        while True:
            query = input('Do you want to update multiple rows from %s? [Y/n]' % self.cls().__class__.__name__)
            if query == '' or not query.lower() in ['yes', 'y', 'no', 'n']:
                print('Please answer with yes or no!')
            else:
                if query.lower()[0] == 'y':
                    self.load()
                break
