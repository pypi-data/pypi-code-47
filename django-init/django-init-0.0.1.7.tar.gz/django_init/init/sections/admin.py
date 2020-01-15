from django.contrib import admin
from django.utils.translation import ugettext_lazy as _
from mptt.admin import MPTTModelAdmin

from common.admin import *
from sections.models import *


@admin.register(Template)
class TemplateAdmin(admin.ModelAdmin):
    list_display = ('title', 'path', 'sort', 'is_active')
    list_editable = ('sort', 'is_active',)
    fieldsets = [
        (None, {'fields': ['title', 'path']}),
        (_('ОТОБРАЖЕНИЕ'), {'fields': ['is_active', 'sort']}),
    ]


@admin.register(Section)
class SectionAdmin(MPTTModelAdmin):
    # list_display = ['title', 'full_path_link', 'is_service', 'thumbnail_cover_small', 'sort', 'is_active']
    # readonly_fields = ['is_service', 'full_path_link', 'thumbnail_cover_small', 'thumbnail_cover']
    list_display = ['title', 'get_url_link', 'thumbnail_cover_small', 'sort', 'is_active']
    readonly_fields = ['thumbnail_cover_small', 'thumbnail_cover']
    prepopulated_fields = {'slug': ('title',)}
    list_editable = ['sort', 'is_active']
    list_filter = ['is_active']

    fieldsets = [
        (None, {'fields': ['title', 'slug', 'parent']}),
        (_('ОТОБРАЖЕНИЕ'), {'fields': ['is_active', ('sort', 'is_service'), 'in_sitemap']}),
        FIELDSETS_PAGES_SEO,
        FIELDSETS_COVER_FULL,
        FIELDSETS_TEXT,
    ]


class ArticleImageInline(admin.TabularInline):
    model = ArticleImage
    fields = ['list_thumbnail_tag', 'image', 'title', 'description', 'link_url', 'new_window', 'sort']
    readonly_fields = ['list_thumbnail_tag']
    extra = 0


# class ArticleFileInline(admin.TabularInline):
#     model = ArticleFile
#     fields = ['file', 'title', 'description', 'sort']
#     extra = 0


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ['title', 'get_url_link', 'template', 'sort', 'is_active']
    # readonly_fields = ['get_url_link']
    prepopulated_fields = {'slug': ('title',)}
    list_editable = ['sort', 'is_active']
    list_filter = ['is_active']
    inlines = (ArticleImageInline,)

    fieldsets = [
        (None, {'fields': ['title', 'slug']}),
        (_('ОТОБРАЖЕНИЕ'), {'fields': ['is_active', 'template', 'sort', 'in_sitemap']}),
        FIELDSETS_PAGES_SEO,
        # FIELDSETS_COVER_FULL,
        FIELDSETS_TEXT,
    ]
