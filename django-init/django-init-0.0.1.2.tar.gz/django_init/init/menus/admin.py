from django import forms
from django.contrib import admin
from django.contrib.admin.templatetags.admin_list import result_list
from django.http import Http404, HttpResponseRedirect
from django.contrib.admin.utils import unquote
from django.utils.html import format_html
# from modeltranslation.admin import TabbedTranslationAdmin
from mptt.admin import MPTTModelAdmin
from .models import Menu, MenuItem
from django.conf.urls import url
from django.utils.translation import ugettext_lazy as _


class MenuItemAdminForm(forms.ModelForm):
    class Meta:
        model = MenuItem
        exclude = ('menu',)


class MenuItemAdmin(MPTTModelAdmin):
    """
    This class is used as a proxy by MenuAdmin to manipulate menu items.
    It should never be registered.
    """

    form = MenuItemAdminForm
    list_display = ('get_title', 'parent', 'path', 'anchor', 'sort', 'new_window', 'is_active',)
    list_editable = ('sort', 'new_window', 'is_active',)
    # ordering = ('id', 'lft', '-sort',)
    fieldsets = [
        (None, {'fields': ['title', 'path', 'anchor', 'parent']}),
        (_('ОТОБРАЖЕНИЕ'), {'fields': ['is_active', 'new_window', 'sort']}),
    ]

    def __init__(self, model, admin_site, menu):
        super(MenuItemAdmin, self).__init__(model, admin_site)
        self._menu = menu

    def save_model(self, request, obj, form, change):
        obj.menu = self._menu
        obj.save()

    def get_form(self, request, obj=None, **kwargs):

        form = super(MenuItemAdmin, self).get_form(request, obj, **kwargs)
        form.base_fields['parent'].queryset = MenuItem.objects.filter(menu=self._menu)
        return form

    def delete_view(self, request, object_id, extra_context=None):
        if request.method == 'POST':  # The user has already confirmed the deletion.
            # Delete and return to menu page
            obj = self.get_object(request, unquote(object_id))
            self.delete_model(request, obj)
            return HttpResponseRedirect("../../../")
        else:
            # Show confirmation page
            return super(MenuItemAdmin, self).delete_view(request, object_id, extra_context)

    def response_change(self, request, obj):
        # TODO Now for all action work redirect
        # We need make get responce to work right with actions
        return HttpResponseRedirect("../../")

    def response_add(self, request, obj, post_url_continue='../%s/'):
        # TODO Now for all action work redirect
        # We need make get responce to work right with actions

        # response = super(MenuItemAdmin, self).response_add(request, obj, post_url_continue)
        # if "_continue" in request.POST:
        #     return response
        # elif "_addanother" in request.POST:
        #     return HttpResponseRedirect(request.path)
        # elif "_popup" in request.POST:
        #     return response
        # else:
        return HttpResponseRedirect("../../")

    def get_actions(self, request):
        # Disable delete
        actions = super(MenuItemAdmin, self).get_actions(request)
        del actions['delete_selected']
        return actions

    def get_title(self, obj):
        return format_html(u'<div style="text-indent:{level}px"><a href="{link}">{title}</a></div>',
                           level=20 * obj.mptt_level, link=obj.pk, title=obj.title)
    get_title.short_description = _('Название пункта')

    # def has_delete_permission(self, request, obj=None):  # Disable delete
    #    return False


@admin.register(Menu)
class MenuAdmin(admin.ModelAdmin):
    menu_item_admin_class = MenuItemAdmin
    list_display = ('title', 'key', 'sort', 'is_active',)
    list_editable = ('is_active', )
    fieldsets = [
        (None, {'fields': ['title', 'key']}),
        (_('ОТОБРАЖЕНИЕ'), {'fields': ['is_active', 'sort']}),
    ]

    class Media:
        # js = ('js/admin/custom_admin.js',)
        css = {
            'all': ('css/admin/custom_admin.css',)
        }

    def __call__(self, request, url):
        pass

    def _get_menu(self, menu_pk):  # Try get menu

        try:
            return Menu.objects.get(pk=menu_pk)
        except Menu.DoesNotExist:
            raise Http404()

    def change_view(self, request, object_id, form_url='', extra_context=None, ):
        menu = self._get_menu(object_id)

        menu_item_admin = self.menu_item_admin_class(MenuItem, self.admin_site, menu)
        try:
            test = menu_item_admin.changelist_view(request)
            cl = test.context_data['cl']
            cl.result_list = cl.result_list.filter(menu=int(object_id))
            extra_context = extra_context or {}
            # extra_context['tree_structure'] = test.context_data.get('tree_structure')
            # extra_context['results'] = list(results(test.context_data['cl']))
            extra_context.update(result_list(cl))
        except Exception as e:
            print(e)
            pass
        return super(MenuAdmin, self).change_view(request, object_id, form_url, extra_context)

    def get_urls(self):
        urls = super(MenuAdmin, self).get_urls()

        app_urls = [
            url(r'^(?P<menu_pk>[-\w]+)/change/add/$', self.admin_site.admin_view(self.edit_menu_item)),
            url(r'^(?P<menu_pk>[-\w]+)/change/(?P<menu_item_pk>[-\w]+)/delete/$',
                self.admin_site.admin_view(self.delete_menu_item), name='menus_menuitem_delete'),
            url(r'^(?P<menu_pk>[-\w]+)/change/(?P<menu_item_pk>[-\w]+)/$',
                self.admin_site.admin_view(self.edit_menu_item)),
        ]
        return app_urls + urls

    def edit_menu_item(self, request, menu_pk, menu_item_pk=None):
        """
        Add and edit menu item
        """
        menu = self._get_menu(menu_pk)
        menu_item_admin = self.menu_item_admin_class(MenuItem, self.admin_site, menu)
        if menu_item_pk is not None:
            return menu_item_admin.change_view(request, menu_item_pk, extra_context={'menu': menu})
        else:
            return menu_item_admin.add_view(request, extra_context={'menu': menu})

    def delete_menu_item(self, request, menu_pk, menu_item_pk):
        menu = self._get_menu(menu_pk)
        menu_item_admin = self.menu_item_admin_class(MenuItem, self.admin_site, menu)
        return menu_item_admin.delete_view(request, menu_item_pk, extra_context={'menu': menu})
