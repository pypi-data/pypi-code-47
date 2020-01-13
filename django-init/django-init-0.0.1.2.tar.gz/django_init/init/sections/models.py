from django.db import models
from django.utils.translation import ugettext_lazy as _

from common.abs import *

# from common.photo.models import *
# from django.contrib.contenttypes.fields import GenericRelation
# from django.utils import timezone

# from ckeditor_uploader.fields import RichTextUploadingField
# from common.seo.models import AbsSEO
# from common.utils.common import *


class Template(AbsTitleSort, AbsActive):
    help_text = _(_('Путь к шаблону. Например: sections/article-detail.html'))
    path = models.CharField(_('Шаблон'), max_length=255, help_text=help_text)

    class Meta:
        verbose_name = _("Шаблон")
        verbose_name_plural = _("Шаблоны")
        db_table = 'templates'
        ordering = ('sort', 'id')

    def __str__(self):
        return self.title


class Section(AbsMPTTModelActive, AbsText, AbsCover, AbsSEO, AbsInSitemap, AbsCreated):
    help_text = _('Если раздел является "служебным" - запрещается изменять URL ссылку и удалять данный раздел')
    template = models.ForeignKey(Template, verbose_name=_('Шаблон'), null=True, on_delete=models.SET_NULL, default=1)
    description = RichTextUploadingField(_('Описание'), blank=True)
    is_service = models.BooleanField(_('Служебный'), default=False, help_text=help_text)

    class Meta:
        verbose_name = _('Раздел')
        verbose_name_plural = _('Разделы')
        db_table = 'sections'

    def __str__(self):
        return self.title


class Article(AbsTitleSortActive, AbsSlug, AbsText, AbsCover, AbsSEO, AbsInSitemap, AbsCreated):
    section = models.ForeignKey('Section', verbose_name=_('Раздел'), null=True, on_delete=models.SET_NULL)
    # attached_tags = GenericRelation('tags.AttachedTag', related_query_name='articles')
    template = models.ForeignKey(Template, verbose_name=_('Шаблон'), null=True, on_delete=models.SET_NULL, default=1)
    on_main = models.BooleanField(_('Показывать на главной?'), default=True)
    author = models.CharField(_('Автор'), max_length=255, blank=True)
    date = models.DateField(_('Дата'), blank=True, null=True)

    class Meta:
        verbose_name = _('Статья')
        verbose_name_plural = _('Статьи')
        db_table = 'sections_article'
        ordering = ('sort', 'id')


class ArticleImage(AbsPhotoSort, AbsLink):
    article = models.ForeignKey(Article, verbose_name=_('Статья'), related_name='image_list',  on_delete=models.CASCADE)

    class Meta:
        verbose_name = _('Изображение')
        verbose_name_plural = _('Изображения')
        db_table = 'sections_article_images'
        ordering = ('-sort', 'title')


# class ArticleFile(AbsFile, AbsSort):
#     article = models.ForeignKey(Article, related_name='file_list', verbose_name=_('Статья'))
#
#     class Meta:
#         verbose_name = _('Файл')
#         verbose_name_plural = _('Файлы')
#         db_table = 'sections_article_files'
#         ordering = ('-sort', 'title')
#
#     def extension(self):
#         print('6145')
#         name, extension = os.path.splitext(self.file.name)
#         return extension[1:]

#
# class ArticleBanner(AbsSort, AbsActive):
#     banner = models.ForeignKey(Banners, verbose_name='баннеры')
#     article = models.ForeignKey(Article, related_name='article_banner_list', verbose_name=_('Статья'))
#
#     def __str__(self):
#         return self.banner.title
#
#     class Meta:
#         verbose_name = 'Баннер'
#         verbose_name_plural = 'Баннеры'
#         db_table = 'sections_article_banner'
#         ordering = ['-sort', 'banner__title']
