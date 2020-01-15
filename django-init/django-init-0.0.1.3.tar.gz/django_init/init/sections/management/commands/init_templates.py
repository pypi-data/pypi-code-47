from django.core.management.base import CommandError

from common.utils.commands import InitBaseCommand
from sections.models import Template


class Command(InitBaseCommand):
    help = 'Initial data for Template'
    model = Template
    init = [
        (1, 'sections/article-detail.html', 'Статья'),
        (2, 'sections/contact.html', 'Контакты'),
        (3, 'sections/article-list.html', 'Список статей'),
        (4, 'sections/section-detail.html', 'Раздел'),
        (5, 'sections/section-list.html', 'Список разделов'),
        (6, 'catalog/product-detail.html', 'Товар'),
        (7, 'catalog/product-list.html', 'Список товаров'),
        (8, 'orders/cart.html', 'Корзина'),
        (9, 'orders/checkout.html', 'Корзина форма'),
        (10, 'orders/delivery.html', 'Доставка'),
        (11, 'orders/payment.html', 'Оплата'),
        (12, 'orders/order.html', 'Заказ'),
    ]

    def load(self):
        for id, path, title in self.init:
            try:
                data = dict(
                    path=path,
                    title=title
                )
                obj, created = self.model.objects.update_or_create(id=id, defaults=data)
            except Exception as e:
                print(e)
                raise CommandError('%s %s - %s does not created' % (self.model().__class__.__name__, title, path))
            act = 'created' if created else 'updated'
            self.stdout.write(
                self.style.SUCCESS('Successfully %s %s: %s' % (act, self.model().__class__.__name__, obj)))
