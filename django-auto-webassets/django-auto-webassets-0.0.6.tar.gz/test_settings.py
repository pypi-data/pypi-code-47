import os
from uuid import uuid4

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

SECRET_KEY = 'CHANGEME'

DEBUG = True

ROOT_URLCONF = 'django_auto_webassets.tests.urls_for_tests'

INSTALLED_APPS = [
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django_assets',
    'django_auto_webassets'
    ]

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'django_auto_webassets', 'tests', 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

STATIC_URL = '/static/'

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'django_auto_webassets', 'tests', "static"),
]

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    'django_assets.finders.AssetsFinder',
)

TEST_RUNNER = 'django_auto_webassets.tests.runner.TestRunner'

WEBASSETS_R_JS = 'django_auto_webassets/tests/node_modules/.bin/r.js'
WEBASSETS_OPTIMIZE = False
ASSETS_DEBUG = False

USE_XVFB = True

ASSETS_MODULES = ['django_auto_webassets.tests.assets.assets']