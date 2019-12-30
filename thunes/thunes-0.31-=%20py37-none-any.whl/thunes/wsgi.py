"""
WSGI config for thunes project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

# use the settings for the develop
profile = os.environ.get('PROJECT_PROFILE', 'develop')
# use the settings for the product
# profile = os.environ.get('PROJECT_PROFILE', 'product')
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'thunes.settings.%s' % profile)

application = get_wsgi_application()
