import importlib
import os
import sys
import inspect

from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from django.urls import include


urlpatterns = []
if getattr(settings, 'STATIC_SERVE', False):
    urlpatterns += static(settings.STATIC_URL,
        document_root=settings.STATIC_ROOT)


# Provide a configuration to enable or disable the
# Django Rest Framework API browser.
if getattr(settings, 'API_BROWSER_ENABLED', False)\
and 'rest_framework' in settings.INSTALLED_APPS:
    urlpatterns += [
        path(getattr(settings, 'API_BROWSER_PATH', 'browse/'),
            include('rest_framework.urls'))
    ]

# Since we use unimatrix.ext.django.settings.runtime,
# we know that 1) UNIMATRIX_SETTINGS_MODULE is defined
# in the environment and 2) we imported it succesfully.
# No need to perform any checks here.
base_settings = importlib.import_module(
    os.environ['UNIMATRIX_SETTINGS_MODULE'])

module_name = os.environ.get('UNIMATRIX_URLS_MODULE')\
    or base_settings.ROOT_URLCONF
urls = importlib.import_module(module_name)
if not hasattr(urls, 'urlpatterns'):
    raise ValueError(
        "%s must declare urlpatterns" % os.environ['UNIMATRIX_SETTINGS_MODULE'])

urlpatterns.extend(urls.urlpatterns)
