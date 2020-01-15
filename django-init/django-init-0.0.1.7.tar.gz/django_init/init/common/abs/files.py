from common.abs import AbsSort, AbsTitleDescription, AbsTitleSort, AbsDescription
from django.utils.translation import ugettext_lazy as _
from django.core.exceptions import ValidationError
from django.utils.safestring import mark_safe
from django.db import models
from easy_thumbnails.files import get_thumbnailer
from django.utils.deconstruct import deconstructible
# from embed_video.fields import EmbedVideoField
from urllib.parse import urlparse, parse_qs
import os
from pytils.translit import translify, slugify


def get_thumb(image, width, height, crop=True):
    if image:
        try:
            thumb = get_thumbnailer(image).get_thumbnail({'size': (width, height), 'crop': crop})
            return mark_safe('<img src="%s">' % thumb.url)
        except Exception as e:
            print(e)
            return None
    return ''


@deconstructible
class UploadPath(object):
    def __init__(self, sub_path):
        self.path = sub_path  # + datetime.now().strftime('/%Y/%m')

    def __call__(self, instance, filename):
        name, ext = os.path.splitext(filename)
        filename = '{}{}'.format(slugify(translify(name)), ext)
        return os.path.join(self.path, instance._meta.app_label, filename)


class Icon(models.Model):
    upload_path = UploadPath('icons')
    icon_1 = models.ImageField(upload_to=upload_path, blank=True, verbose_name=u'Иконка 1')
    icon_2 = models.ImageField(upload_to=upload_path, blank=True, verbose_name=u'Иконка 2')

    def thumbnail_icon_1(self):
        return get_thumb(self.icon_1, 0, 50)

    thumbnail_icon_1.short_description = 'Превью'

    def thumbnail_icon_2(self):
        return get_thumb(self.icon_2, 0, 50)

    thumbnail_icon_2.short_description = 'Превью'

    class Meta:
        abstract = True
        verbose_name = 'иконка'
        verbose_name_plural = 'иконки'


class AbsImageDescription(AbsDescription):
    title = models.CharField(_('Заголовок'), max_length=100, default='', blank=True)

    class Meta:
        abstract = True


class AbsPhotoSimple(models.Model):
    upload_path = UploadPath('photo')
    image = models.ImageField('изображение', upload_to=upload_path, blank=True)

    def __str__(self):
        return '%s' % self.id

    def thumbnail_tag(self):
        return get_thumb(self.image, 0, 100)

    thumbnail_tag.short_description = 'Превью'

    def thumbnail_tag_icon(self):
        return get_thumb(self.image, 50, 0)

    thumbnail_tag_icon.short_description = 'Превью1'
    # thumbnail_tag_icon.allow_tags = True

    def list_thumbnail_tag(self):
        return get_thumb(self.image, 100, 0)

    list_thumbnail_tag.short_description = 'Превью'

    class Meta:
        abstract = True
        verbose_name = 'изображение'
        verbose_name_plural = 'изображения'


class AbsPhoto(AbsImageDescription, AbsPhotoSimple):
    class Meta(AbsPhotoSimple.Meta):
        abstract = True


class AbsBack(models.Model):
    back_title = models.CharField('заголовок фона', max_length=100, blank=True)
    back_description = models.CharField('описание фона', max_length=255, default='', blank=True)
    back = models.ImageField(upload_to=UploadPath('backgrounds'), blank=True, verbose_name=u'фон')
    is_show_back = models.BooleanField('показывать фон', default=False)

    def __str__(self):
        return '%s' % self.id

    def thumbnail_back(self):
        return get_thumb(self.back, 0, 100)

    thumbnail_back.short_description = 'Превью'

    class Meta:
        abstract = True
        verbose_name = 'фон'
        verbose_name_plural = 'фоны'


class AbsPhotoSort(AbsPhoto, AbsSort):
    class Meta(AbsPhoto.Meta):
        ordering = ('-sort', 'title')
        abstract = True


class AbsCoverSimple(models.Model):
    upload_path = UploadPath('covers')
    cover = models.ImageField('Обложка', upload_to=upload_path, blank=True)

    def thumbnail_cover(self):
        return get_thumb(self.cover, 200, 0)
    thumbnail_cover.short_description = 'Превью'

    def thumbnail_cover_small(self):
        return get_thumb(self.cover, 50, 0)
    thumbnail_cover_small.short_description = 'Превью'

    class Meta:
        abstract = True
        verbose_name = 'обложка'
        verbose_name_plural = 'обложки'


class AbsCover(AbsCoverSimple):
    cover_title = models.CharField('Заголовок обложки', max_length=100, default='', blank=True)
    cover_description = models.CharField('Описание обложки', max_length=255, default='', blank=True)
    is_show_cover = models.BooleanField('Показывать обложку', default=False)

    class Meta(AbsCoverSimple.Meta):
        abstract = True


class CoversSimpleDouble(models.Model):
    cover_2 = models.ImageField(upload_to=AbsCoverSimple.upload_path, blank=True, verbose_name=u'Обложка 2')

    def thumbnail_tag_2_small(self):
        return get_thumb(self.cover_2, 100, 0)

    thumbnail_tag_2_small.short_description = 'Превью'

    class Meta(AbsCoverSimple.Meta):
        abstract = True


class CoversDouble(CoversSimpleDouble):
    is_show_cover_2 = models.BooleanField('показывать обложку 2', default=False)

    class Meta(AbsCoverSimple.Meta):
        abstract = True


class AbsVideo(models.Model):
    title = models.CharField('название', max_length=255)
    video_mp4 = models.FileField('видео mp4', upload_to='videos', blank=True)
    video_webm = models.FileField('видео webm', upload_to='videos', blank=True)
    video_ogv = models.FileField('видео ogv', upload_to='videos', blank=True)

    class Meta:
        abstract = True
        verbose_name = _('видео')
        verbose_name_plural = _('видео')
        ordering = ('title',)

    def __str__(self):
        return self.title

    def clean(self):
        if self.video_mp4 or self.video_webm or self.video_ogv:
            return
        raise ValidationError('Необходимо загрузить видео как минимум в одном формате.')

    def get_source_tags(self):
        tags = []
        tpl = '<source src="{}" type="video/{}">'
        if self.video_mp4:
            tags.append(tpl.format(self.video_mp4.url, 'mp4'))
        if self.video_webm:
            tags.append(tpl.format(self.video_webm.url, 'webm'))
        if self.video_ogv:
            tags.append(tpl.format(self.video_ogv.url, 'ogg'))
        return map(mark_safe, tags)