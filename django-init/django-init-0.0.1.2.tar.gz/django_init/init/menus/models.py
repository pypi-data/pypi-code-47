# -*- coding: utf-8 -*-
from common.menus.choices import MENUS_REGIONES
from django.db import models
from mptt.models import MPTTModel, TreeForeignKey
from django.utils.translation import ugettext_lazy as _
from django.dispatch import receiver
from django.core.cache import cache
from common.abs import *


# class BlockMenu(models.Model):
#     title = models.CharField(_('название'), max_length=50)
#     key = models.CharField(max_length=255, verbose_name='Ключ (служебное)')
#
#     class Meta:
#         verbose_name = 'Блок'
#         verbose_name_plural = 'Блоки'
#         db_table = 'menus_block'
#
#     def __str__(self):
#         return self.title


class Menu(AbsTitleSortActive, AbsKey):

    class Meta:
        verbose_name = 'Меню'
        verbose_name_plural = 'Меню'
        ordering = ('-sort', 'title')

    def __str__(self):
        return self.title

    # @classmethod
    # def get_menus(cls, block, region=0):  # Returns all active
    #     menus = cls.objects.filter(active=True, block__key=block, region=region)
    #     return menus[0].menu_items.filter(active=True) if menus else cls.objects.none()


class MenuItem(MPTTModel, AbsTitleSortActive):
    menu = models.ForeignKey(Menu, verbose_name=_('Меню'), null=True, related_name='menu_items', on_delete=models.SET_NULL)
    parent = TreeForeignKey('self', blank=True, null=True, related_name='children', verbose_name=_('Родитель'), on_delete=models.SET_NULL)
    path = models.CharField(_('URL'), max_length=255, blank=True, help_text=_('URL, например /about/ или http://foo.com/'))
    anchor = models.CharField(_('Якорь'), max_length=20, blank=True, help_text=_('Например #anchor'))
    new_window = models.BooleanField(_('В окне'), default=False, help_text=_('Открывать в новом окне?'))

    class MPTTMeta:
        level_attr = 'mptt_level'
        order_insertion_by = ('-sort',)

    class Meta:
        verbose_name = 'Пункт меню'
        verbose_name_plural = 'Пункты меню'
        db_table = 'menus_menu_items'
        ordering = ['lft', '-sort']

    def __str__(self):
        return self.title

    @classmethod
    def get_items(cls, key):
        return cls.get_active().filter(menu__key=key, menu__is_active=True)

    def title_with_spacer(self):  # make title with spaces for show in admin
        spacer = ''
        for i in range(0, self.mptt_level):
            spacer += u'&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;'
        return spacer + self.title

    def get_sub_menus(self):  # Returns all active
        return self.get_descendants().filter(active=True)

    def has_descendants(self, link):
        return self.get_descendants().filter(active=True, link=link)


# @receiver(models.signals.post_save, sender=MenuItem)
# @receiver(models.signals.pre_delete, sender=MenuItem)
# def invalidate(instance, **kwargs):
#   cache.delete('treemenu/%s' % (instance.menu.slug))
