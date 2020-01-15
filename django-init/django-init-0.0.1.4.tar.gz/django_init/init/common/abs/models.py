from ckeditor_uploader.fields import RichTextUploadingField
from django.db import models
from django.urls import reverse
from django.utils.html import format_html
from django.utils.translation import ugettext_lazy as _

# from banners.choices import POSITIONS, POSITION_LEFT
# from common.abscreated import choices
# from common.utils.common import add_slash_right
# from django.utils import timezone


"""
Date adn time fields
"""


class AbsCreated(models.Model):
    created_at = models.DateTimeField(_('Дата создания'), auto_now_add=True)
    updated_at = models.DateTimeField(_('Дата обновления'), auto_now=True)

    class Meta:
        abstract = True


class AbsByCreated(AbsCreated):
    created_by = models.CharField(_('Создана кем'), blank=True)
    updated_by = models.CharField(_('Обновлена кем'), blank=True)

    class Meta:
        abstract = True


"""
Boolean fields
"""


class AbsActive(models.Model):
    is_active = models.BooleanField(_('Активен'), default=True)

    class Meta:
        abstract = True

    @classmethod
    def get_active(cls):
        return cls.objects.filter(is_active=True)


class AbsNew(models.Model):
    is_new = models.BooleanField(_('Новое'), default=True)

    class Meta:
        abstract = True

    @classmethod
    def get_new(cls):
        return cls.objects.filter(is_active=True)


class AbsShow(models.Model):
    is_show = models.BooleanField(_('Показывать'), default=True)

    class Meta:
        abstract = True

    @classmethod
    def get_show(cls):
        return cls.objects.filter(is_show=True)


class AbsHide(models.Model):
    is_hide = models.BooleanField(_('Скрыть'), default=False)

    class Meta:
        abstract = True

    @classmethod
    def get_hide(cls):
        return cls.objects.filter(is_hide=True)


class AbsNewWindow(models.Model):
    new_window = models.BooleanField(_('Открывать в новом окне'), default=False)

    class Meta:
        abstract = True


class AbsInSitemap(models.Model):
    in_sitemap = models.BooleanField(_('В sitemap.xml'), default=True)

    class Meta:
        abstract = True

    @classmethod
    def get_in_sitemap(cls):
        return cls.objects.filter(in_sitemap=True)


class AbsOnMainPage(models.Model):
    on_main = models.BooleanField(_('Показывать на главной'), default=False)

    class Meta:
        abstract = True

    @classmethod
    def get_on_main(cls):
        return cls.objects.filter(on_main=True)


"""
........... fields
"""


class AbsSort(models.Model):
    sort = models.IntegerField(_('Сортировка'), default=0)

    class Meta:
        abstract = True


class AbsSortActive(AbsSort, AbsActive):

    class Meta:
        abstract = True


class AbsValue(models.Model):
    value = models.CharField(_('Значение'), max_length=255)

    class Meta:
        abstract = True


class AbsKey(models.Model):
    key = models.CharField(_('Ключ'), unique=True, db_index=True, max_length=100)

    class Meta:
        abstract = True


class AbsTitle(models.Model):
    title = models.CharField(_('Название'), max_length=255)

    class Meta:
        abstract = True


class AbsTitleSort(AbsTitle, AbsSort):
    class Meta:
        abstract = True
        ordering = ['-sort', 'title']


class AbsTitleSortActive(AbsTitle, AbsSort, AbsActive):
    class Meta:
        abstract = True
        ordering = ['-sort', 'title']


class AbsDescription(models.Model):
    description = models.CharField(_('Описание'), max_length=255, blank=True)

    class Meta:
        abstract = True


class AbsTitleDescription(AbsTitle, AbsDescription):
    class Meta:
        abstract = True


# class AbsFile(AbsCreated, AbsTitleDescription):
#     file = models.FileField(_('Файл'), upload_to=UploadPath('file'), blank=True)
#
#     class Meta:
#         abstract = True


class AbsSlug(models.Model):
    slug = models.SlugField(_('Ссылка'), max_length=255, db_index=False, help_text='URL для этой страницы')

    class Meta:
        abstract = True

    def get_url(self):
        return reverse('home')

    def get_url_link(self):
        return format_html('<a href="{}" target="_blank">{}</a>', self.get_url(), self.get_url())
    get_url_link.short_description = _('URL')
    get_url_link.allow_tags = True


class AbsFullSlug(AbsSlug):
    full_slug = models.CharField(_('Полная URL ссылка'), max_length=255, db_index=True, unique=True, help_text='URL для этой страницы')

    class Meta:
        abstract = True


class AbsLink(AbsNewWindow):
    link_url = models.CharField(_('URL ссылки'), max_length=255, blank=True)

    class Meta:
        abstract = True


# class AbsPosition(models.Model):
#     position = models.CharField(_('позиция'), max_length=15, choices=POSITIONS, default=POSITION_LEFT)
#
#     class Meta:
#         abstract = True

class AbsOneText(models.Model):
    text = RichTextUploadingField(_('Текст'), blank=True)

    class Meta:
        abstract = True


class AbsText(models.Model):
    short_text = RichTextUploadingField(_('Короткий текст'), blank=True)
    full_text = RichTextUploadingField(_('Полный текст'), blank=True)

    class Meta:
        abstract = True


"""
SEO fields
"""


class AbsSEO(models.Model):
    seo_title = models.CharField(verbose_name=_('Заголовок (SEO)'), max_length=255, blank=True)
    seo_h1 = models.CharField(verbose_name=_('H1 (SEO)'), max_length=255, blank=True)
    seo_keywords = models.CharField(verbose_name=_('Ключевые слова (SEO)'), max_length=255, blank=True)
    seo_description = models.TextField(verbose_name=_('Описание (SEO)'), max_length=255, blank=True)

    class Meta:
        abstract = True


"""
Person fields
"""


class AbsFLName(models.Model):
    first_name = models.CharField(_('Имя'), max_length=255)
    last_name = models.CharField(_('Фамилия'), max_length=255)

    class Meta:
        abstract = True


class AbsPatronymic(models.Model):
    patronymic = models.CharField(_('Отчество'), max_length=255, blank=True)

    class Meta:
        abstract = True


class AbsPhone(models.Model):
    phone = models.CharField(_('Телефон'), max_length=20, blank=True)

    class Meta:
        abstract = True


class AbsEmail(models.Model):
    email = models.EmailField(_('E-mail'), blank=True)

    class Meta:
        abstract = True


class AbsMessage(models.Model):
    message = models.TextField(_('Сообщение'), blank=True)

    class Meta:
        abstract = True


class AbsCity(models.Model):
    city = models.CharField(_('Город'), max_length=100, blank=True)

    class Meta:
        abstract = True


class AbsAddress(models.Model):
    address = models.CharField(_('Адрес'), max_length=255, blank=True)

    class Meta:
        abstract = True


class AbsSubject(models.Model):
    subject = models.CharField(_('Тема обращения'), max_length=255, blank=True)

    class Meta:
        abstract = True


class AbsPerson(AbsFLName, AbsEmail, AbsPhone):

    class Meta:
        abstract = True


"""
Catalog fields
"""


class AbsPrice(models.Model):
    price = models.DecimalField(_('Цена'), max_digits=10, decimal_places=2)

    class Meta:
        abstract = True


class AbsQuantity(models.Model):
    quantity = models.PositiveIntegerField(_('Количество'))

    class Meta:
        abstract = True


class AbsDiscount(models.Model):
    discount = models.PositiveIntegerField(_('Скидка'))

    class Meta:
        abstract = True


class AbsTotal(models.Model):
    total = models.PositiveIntegerField(_('Сумма'))

    class Meta:
        abstract = True


class AbsOrder(AbsPrice, AbsQuantity, AbsDiscount, AbsTotal):

    class Meta:
        abstract = True

# class AbsStatus(models.Model):
#     status = models.PositiveSmallIntegerField(_('статус заявки'), choices=choices.FEEDBACK_STATUSES,
#                                               default=choices.STATUS_NEW)
#
#     class Meta:
#         abstract = True
#
#     @property
#     def status_name(self):
#         statuses = dict(self.statuses)
#         return statuses.get(self.status, _('статус не определён'))
#
#     @classmethod
#     def for_new(cls):
#         return cls.objects.filter(status=choices.STATUS_NEW)
#
#
# class AbsMessage(models.Model):
#     message = models.TextField(_('Сообщение'), default='', blank=True)
#
#     class Meta:
#         abstract = True
