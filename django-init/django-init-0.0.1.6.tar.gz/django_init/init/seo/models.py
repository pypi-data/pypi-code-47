from django.utils.translation import ugettext_lazy as _

from common.abs import *


class ConfigSEO(AbsTitle, AbsActive):
    key = models.CharField(_('Ключ'), max_length=15)
    group = models.CharField(_('Группа'), db_index=True, max_length=15)
    group_title = models.CharField(_('Название группы'), max_length=20)
    description = models.TextField(_('Переменные'), blank=True)
    value = models.CharField(_('Значение'), max_length=255, blank=True, help_text='Пример: Заголовок {{title}} страницы')

    class Meta:
        verbose_name = 'SEO'
        verbose_name_plural = 'SEO'
        ordering = ('id',)
        db_table = 'config_seo'

    def __str__(self):
        return self.title
