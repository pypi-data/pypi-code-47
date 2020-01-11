from django.core.exceptions import ImproperlyConfigured
from django.db import models
from common.abs import *
from django.utils.translation import ugettext_lazy as _

# from common.functions import UploadPath


class Robots(models.Model):
    updated = models.DateTimeField(_('Дата изменения'), auto_now=True)
    value = models.TextField(_('Содержимое'), blank=True, null=True, default=None)

    class Meta:
        verbose_name = 'robots.txt'
        verbose_name_plural = 'robots.txt'
        db_table = 'config_robots'

    def __str__(self):
        return self.value


class AbsBaseConfig(AbsTitle, AbsKey, AbsDescription):
    # title = models.CharField(verbose_name=u'Название', max_length=255)
    # description = models.CharField(verbose_name=u'Описание', max_length=255, blank=True, default='')
    # key = models.CharField(verbose_name=u'Ключ', max_length=255, help_text=u'Служебное поле')

    class Meta:
        abstract = True

    @classmethod
    def get_config(cls, name):
        config_list = cls.get_config_list()
        if name in config_list:
            return config_list[name]
        raise ImproperlyConfigured('Parameter "%s" is not defined in site settings.' % name)

    @classmethod
    def get_config_object(cls, name):
        config_object_list = cls.get_config_object_list()
        if name in config_object_list:
            return config_object_list[name]
        raise ImproperlyConfigured('Parameter "%s" is not defined in site settings.' % name)

    @classmethod
    def get_config_object_list(cls):
        if not hasattr(cls, 'config_object_list'):
            cls.config_object_list = dict((item.key, {'value': item.value, 'description': item.description}) for item in cls.objects.all())
        return cls.config_object_list

    """каждый раз, когда меняется какая-то текстовая (файловая) настройка сайта в админке,
    нужно рестартить сервер, чтобы изменения отобразились на сайте
    cls.config_list - сохраняется один раз при запуске/перезапуске сервера
    один sql-запрос в базу при запуске сайта"""

    @classmethod
    def get_cached_config_list(cls):
        if not hasattr(cls, 'config_list'):
            cls.config_list = dict((item.key, item.value) for item in cls.objects.all())
        return cls.config_list

    """когда меняется текстовая (файловая) настройка сайта, не нужно рестартить сервер
    cls.config_list - сохраняется каждый раз при переходе на какую-нибудь страницу
    sql-запрос выполняется каждый раз при переходе на какую-нибудь страницу"""

    @classmethod
    def get_config_list(cls):
        cls.config_list = dict((item.key, item.value) for item in cls.objects.all())
        return cls.config_list


class Config(AbsBaseConfig):
    value = models.TextField(_('Значение'), blank=True, null=True, default=None)
    is_active = models.BooleanField(default=True, verbose_name=u'Активен?')

    class Meta:
        verbose_name = _('Текстовая настройка')
        verbose_name_plural = _('Текстовые настройки')
        ordering = ('id',)

    def __str__(self):
        return self.title

    @classmethod
    def get_configs(cls):
        if not hasattr(cls, 'sys_configs'):
            cls.sys_configs = dict((sys_config.key, sys_config.value) for sys_config in cls.objects.all())

        return cls.sys_configs

    @classmethod
    def get_domain(cls):
        domain, created = Config.objects.get_or_create(
            key="DOMAIN", defaults={'title': u'MAIL: Доменное имя (для генерации ссылок E-mail)', 'value': 'your_domain.ru'})
        return domain.value

    @classmethod
    def get_site_name(cls):
        site_name, created = Config.objects.get_or_create(
            key="SITE_NAME", defaults={'title': u'MAIL: Наименование сайта', 'value': 'your_sitename'})
        return site_name.value

    @classmethod
    def get_email_to(cls):
        email_to, created = Config.objects.get_or_create(

            defaults={'title': u"MAIL: E-mail'ы, на которые будут приходить уведомления. Через запятую", 'value': 'sample@email.ru'})
        return email_to.value

    # @classmethod
    # def get_meta_keywords(cls):
    #     obj, created = Config.objects.get_or_create(
    #         key="meta_keywords", defaults={'title': u'МЕТА: Ключевые слова', 'value': ''})
    #     return obj.value
    #
    # @classmethod
    # def get_meta_description(cls):
    #     obj, created = Config.objects.get_or_create(
    #         key="meta_descr", defaults={'title': u'МЕТА: Описание', 'value': ''})
    #     return obj.value
    #
    # @classmethod
    # def get_meta_title(cls):
    #     obj, created = Config.objects.get_or_create(
    #         key="main_title", defaults={'title': u'Заголовок сайта', 'value': 'Заголовок сайта'})
    #     return obj.value


class ConfigFile(AbsBaseConfig):
    value = models.FileField(u'Файл', upload_to=UploadPath('config'), blank=True, null=True)
    sort = models.IntegerField(u'Сортировка', default=0)

    class Meta:
        verbose_name = u'файловая настройка'
        verbose_name_plural = u'файловые настройки'
        db_table = 'config_file'
        ordering = ('-sort', 'id',)

    def __str__(self):
        return self.title



