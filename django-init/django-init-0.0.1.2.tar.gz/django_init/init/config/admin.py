from django.contrib import admin
from django.db import models
from django.forms import Textarea
from django.utils.html import format_html

from .forms import RobotsAdminForm
from .models import Config, Robots


@admin.register(Config)
class ConfigAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'list_value', 'key', 'is_active')
    list_editable = ('is_active',)

    def list_value(self, obj):
        return format_html(u'<div style="width:400px">{}</div>', obj.value if obj.value else '')

    list_value.short_description = u'Значение'
    list_value.allow_tags = True


# @admin.register(ConfigFile)
class ConfigFileAdmin(admin.ModelAdmin):
    list_display = ('title', 'key', 'sort')
    list_editable = ('sort',)

    def list_value(self, obj):
        return format_html(u'<div style="width:400px">{}</div>', obj.value if obj.value else '')

    list_value.short_description = u'Значение'
    list_value.allow_tags = True


@admin.register(Robots)
class RobotsAdmin(admin.ModelAdmin):
    form = RobotsAdminForm
    list_display = ['list_value', 'updated']
    readonly_fields = ['updated']
    fields = ['updated', 'value']
    formfield_overrides = {
        models.TextField: {'widget': Textarea(attrs={'rows': 25, 'style': 'width:40em;'})},
    }
    actions = None

    def has_add_permission(self, request):
        return False

    def has_delete_permission(self, request, obj=None):
        return False

    def list_value(self, obj):
        return format_html(u'Robots.txt')

    list_value.short_description = u'Файл'
