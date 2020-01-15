from django.utils.translation import ugettext_lazy as _
from mptt.fields import TreeForeignKey
from mptt.models import MPTTModel

from .models import *


# class AbsMPTTModel(MPTTModel, AbsTitle, AbsSort):
#     parent = TreeForeignKey('self', verbose_name=_('Родитель'), null=True, blank=True, db_index=True, on_delete=models.SET_NULL, related_name='children')
#     slug = models.SlugField(_('Ссылка'), max_length=255, help_text='URL для этого элемента')
#     full_slug = models.SlugField(_('Полная URL ссылка'))
#
#     class Meta:
#         ordering = ['-sort']
#         abstract = True
#
#     class MPTTMeta:
#         level_attr = 'mptt_level'
#         order_insertion_by = ['slug', 'title', 'sort']
#
#     def __str__(self):
#         return self.title
#
#     def get_breadcrumbs(self):
#         breadcrumbs = [{'name': self.title, 'url': self.full_slug}]
#         return breadcrumbs if self.parent else breadcrumbs

    # def get_full_path(self):
    #     if self.slug == '{main}': return '/'
    #     url = '/%s' % self.slug
    #     page = self
    #     while page.parent:
    #         url = '/%s%s' % (page.parent.slug, url)
    #         page = page.parent
    #     return add_slash_right(url)

class AbsMPTTModel(MPTTModel, AbsTitleSort, AbsFullSlug):
    parent = TreeForeignKey('self', related_name='children', null=True, blank=True, verbose_name=_('Родитель'),
                            db_index=True, on_delete=models.PROTECT)

    class Meta:
        ordering = ['-sort']
        abstract = True

    class MPTTMeta:
        level_attr = 'mptt_level'
        order_insertion_by = ['slug', 'title', 'sort']

    def __str__(self):
        return self.title

    def get_breadcrumbs(self):
        breadcrumbs = [{'title': self.title, 'full_slug': self.full_slug}]
        return self.parent.get_breadcrumbs() + breadcrumbs if self.parent else breadcrumbs

    def get_full_path(self):
        if self.slug == '{main}':
            return '/'
        url = '/%s' % self.slug
        page = self
        while page.parent:
            url = '/%s%s' % (page.parent.slug, url)
            page = page.parent
        return page
        # return add_slash(url)  # format /slug/slug/

    def save(self, *args, **kwargs):
        # Если модель служебная - нельзя менять slug и удалять
        if self.slug:
            self.full_slug = self.slug
            if self.parent:
                self.full_slug = '%s/%s' % (self.parent.slug, self.slug)
            # orig = get_object_or_none(Section, pk=self.pk)
            # if not orig:
            #     return
            # self.slug = orig.slug
            # self.full_slug = orig.full_slug
        super(AbsMPTTModel, self).save(*args, **kwargs)


class AbsMPTTModelActive(AbsMPTTModel, AbsActive):
    class Meta(AbsMPTTModel.Meta):
        abstract = True

    def get_sub_sections(self):
        return self.get_descendants().filter(is_active=True)

    def get_descendants_active(self):
        return self.get_descendants().filter(is_active=True)

    def get_family_active(self):
        return self.get_family().filter(is_active=True)

    def get_siblings_active(self):
        return self.get_siblings(include_self=True).filter(is_active=True)

    def get_children_active(self):
        return self.get_children().filter(is_active=True)