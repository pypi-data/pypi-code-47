from django.contrib import admin
from django.utils.translation import ugettext_lazy as _

from .models import *

FIELDSETS_PAGES_SEO = (_('ПОИСКОВАЯ ОПТИМИЗАЦИЯ'),
                       {'fields': ['seo_title', 'seo_h1', 'seo_keywords', 'seo_description'], 'classes': ['collapse']})


@admin.register(ConfigSEO)
class ConfigSEOAdmin(admin.ModelAdmin):
    list_display = ('title', 'group_title', 'description', 'value', 'is_active')
    list_editable = ('value', 'is_active')
    list_filter = ('group_title',)
    readonly_fields = ('title', 'group', 'key', 'group_title', 'description',)
    fieldsets = [
        (None, {'fields': ['title', 'group_title', 'group', 'key', 'description']}),
        (_('ОТОБРАЖЕНИЕ'), {'fields': ['is_active', 'value']})]

    def has_delete_permission(self, request, obj=None):
        return False

