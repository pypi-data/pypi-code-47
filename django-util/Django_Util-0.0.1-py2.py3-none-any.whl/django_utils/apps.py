from django.apps import AppConfig

import os


# # https://docs.djangoproject.com/en/dev/ref/applications/#django.apps.AppConfig
class UtilConfig(AppConfig):
    # https://docs.djangoproject.com/en/dev/ref/applications/#django.apps.AppConfig.name
    name = 'django_utils'

    # https://docs.djangoproject.com/en/dev/ref/applications/#django.apps.AppConfig.label
    label = 'DjangoUtils'

    # https://docs.djangoproject.com/en/dev/ref/applications/#django.apps.AppConfig.verbose_name
    verbose_name = 'Django Utilities'

    # https://docs.djangoproject.com/en/dev/ref/applications/#django.apps.AppConfig.path
    path = os.path.dirname(__file__)
