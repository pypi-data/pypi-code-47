from collections import OrderedDict

from django.conf.urls import url
from rest_framework.routers import (
    SimpleRouter as _SimpleRouter,
    APIRootView,
    SchemaView,
    SchemaGenerator
)
from rest_framework.settings import api_settings
from rest_framework.urlpatterns import format_suffix_patterns
from orm88.connector import ORM88


class SimpleRouter(_SimpleRouter):

    def get_default_basename(self, viewset):
        """
        If `basename` is not specified, attempt to automatically determine
        it from the viewset.
        """
        queryset = getattr(viewset, 'queryset', None)  # type: ORM88

        assert queryset is not None, (
            '`basename` argument not specified, '
            'and could not automatically determine '
            'the name from the viewset, as it does '
            'not have a `.queryset` attribute.'
        )

        return queryset._model_name.lower()


class DefaultRouter(SimpleRouter):
    """
        The default router extends the SimpleRouter, but also adds in a default
        API root view, and adds format suffix patterns to the URLs.
        """
    include_root_view = True
    include_format_suffixes = True
    root_view_name = 'api-root'
    default_schema_renderers = None
    APIRootView = APIRootView
    APISchemaView = SchemaView
    SchemaGenerator = SchemaGenerator

    def __init__(self, *args, **kwargs):
        if 'root_renderers' in kwargs:
            self.root_renderers = kwargs.pop('root_renderers')
        else:
            self.root_renderers = list(api_settings.DEFAULT_RENDERER_CLASSES)
        super().__init__(*args, **kwargs)

    def get_api_root_view(self, api_urls=None):
        """
        Return a basic root view.
        """
        api_root_dict = OrderedDict()
        list_name = self.routes[0].name
        for prefix, viewset, basename in self.registry:
            api_root_dict[prefix] = list_name.format(basename=basename)

        return self.APIRootView.as_view(api_root_dict=api_root_dict)

    def get_urls(self):
        """
        Generate the list of URL patterns, including a default root view
        for the API, and appending `.json` style format suffixes.
        """
        urls = super().get_urls()

        if self.include_root_view:
            view = self.get_api_root_view(api_urls=urls)
            root_url = url(r'^$', view, name=self.root_view_name)
            urls.append(root_url)

        if self.include_format_suffixes:
            urls = format_suffix_patterns(urls)

        return urls
