# -*- coding: utf-8 -*-
from django.contrib import admin
from django.utils.html import format_html

from .models import *


@admin.register(Feedback)
class FeedbackAdmin(admin.ModelAdmin):
    list_display = ('name', 'subject', 'email', 'phone')
    fields = ['name', 'subject', 'email', 'phone', 'message', 'get_file']
    readonly_fields = ['get_file']

    def get_file(self, obj):
        if obj.file:
            return format_html('<p><a href="{0}" target="_blank">{0}</a></p>', obj.file.url)
        return ''
    get_file.short_description = 'Файл'
    get_file.allow_tags = True


@admin.register(FeedConfig)
class FeedConfigAdmin(admin.ModelAdmin):
    list_display = ('email_subject', 'subject', 'email_message', 'email', 'is_active')
    fields = ['subject', 'email_subject', 'email_message', 'email', 'is_active']
    list_editable = ['is_active']
