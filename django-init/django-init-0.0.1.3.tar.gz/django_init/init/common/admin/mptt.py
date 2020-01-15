# from common.abscreated.choices import *
# from common.utils.common import add_slash
from mptt.admin import MPTTModelAdmin
# from .models import AbsStatus
# from django.contrib import admin
#
# from django.db import models
# from django.forms import TextInput, Textarea
from django.forms import ModelForm, ValidationError
#
#
# class ModelAdmin(admin.ModelAdmin):
#     """ Abstract admin models for columns updated_by and created_by """
#     exclude = ('updated_by', 'created_by',)
#
#     def save_form(self, request, form, change):
#         obj = super(ModelAdmin, self).save_form(request, form, change)
#
#         if hasattr(obj, 'updated_by'):
#             obj.updated_by = str(request.user)
#
#         if hasattr(obj, 'created_by') and not obj.created_by:
#             obj.created_by = str(request.user)
#
#         return obj
#
#
# class StatusAdmin(admin.ModelAdmin):
#     """ Abstract admin models for AbsStatus """
#
#     def save_form(self, request, form, change):
#         obj = super(StatusAdmin, self).save_form(request, form, change)
#         if obj.status == STATUS_NEW:
#             obj.status = STATUS_VIEWED
#         return obj
#
#
# class IsNewAdmin(admin.ModelAdmin):
#     """ Abstract admin models for AbsStatus """
#
#     def save_form(self, request, form, change):
#         obj = super(IsNewAdmin, self).save_form(request, form, change)
#         if obj.is_new:
#             obj.is_new = False
#         return obj
#
#
class AbsMPTTModelForm(ModelForm):
    def clean(self):
        cleaned_data = self.cleaned_data
        slug = cleaned_data.get("slug")
        if slug:
            qs = self.Meta.model.objects.filter(slug=slug)
            if qs and qs.count() > 1 or qs and qs[0].id != self.instance.id:
                raise ValidationError("Ссылка с таким именем уже существует")
        super(AbsMPTTModelForm, self).clean()  # important - let admin do its work on data!
        return cleaned_data


class AbsMPTTModelAdmin(MPTTModelAdmin):
    form = AbsMPTTModelForm

    def full_path_link(self, obj):
        return '<a href="/{}/" target="_blank">/{}/</a>'.format(obj.full_slug, obj.full_slug)

    full_path_link.short_description = 'Полная ссылка'
    full_path_link.allow_tags = True

    def save_model(self, request, obj, form, change):
        path_section = obj.section.get_full_path()[:-1] if hasattr(obj, 'section') and obj.section else ''
        full_slug = add_slash(obj.parent.get_full_path() + obj.slug) if obj.parent else obj.get_full_path()
        full_slug = path_section + full_slug
        obj.full_slug = full_slug[1:-1]
        obj.save()
        for child in obj.get_descendants():
            full_slug = path_section + child.get_full_path()
            child.full_slug = full_slug[1:-1]
            child.save()


def article_full_path(self, obj):
    d = obj.section.get_full_path()[:-1] + obj.get_full_path() if obj.section else obj.get_full_path()
    return '<a href="{}" target="_blank">{}</a>'.format(d, d)


article_full_path.short_description = 'Полная ссылка'
article_full_path.allow_tags = True