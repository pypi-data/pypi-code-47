"""
Django settings for schoolapps project.
"""

import os
import ldap
from django_auth_ldap.config import LDAPSearch, PosixGroupType, GroupOfNamesType, LDAPGroupType
import logging
from .secure_settings import *

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

DEBUG = True

# PDB debugger option
POST_MORTEM = True

ALLOWED_HOSTS = [
    'info.katharineum.de',
    '178.63.239.184',
    '159.69.181.50',
    'localhost',
    '127.0.0.1',
    '13049d63.ngrok.io'
]

INTERNAL_IPS = [
    '127.0.0.1',
]

# Application definition

INSTALLED_APPS = [
    'dashboard.apps.DashboardConfig',
    "debug.apps.DebugConfig",
    'aub.apps.AubConfig',
    'fibu.apps.FibuConfig',
    'untisconnect.apps.UntisconnectConfig',
    'timetable.apps.TimetableConfig',
    'menu.apps.MenuConfig',
    'support.apps.SupportConfig',
    'faq.apps.FaqConfig',
    'dbsettings',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'material',
    'django_react_templatetags',
    'martor',
    'widget_tweaks',
    'pwa',
    'templatetags.apps.TemplatetagsConfig',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'schoolapps.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(BASE_DIR, 'templates')
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'django_react_templatetags.context_processors.react_context_processor',
                'meta.meta_processor',
            ],
        },
    },
]

WSGI_APPLICATION = 'schoolapps.wsgi.application'

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

# Internationalization

LANGUAGE_CODE = 'de-de'
TIME_ZONE = 'Europe/Berlin'
USE_I18N = True
USE_L10N = True
USE_TZ = True

# Static files (CSS, JavaScript, Images)

STATIC_URL = '/static/'
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static')
]
STATIC_ROOT = os.path.join(BASE_DIR, 'staticcollect')

# Redirect to home URL after login (Default redirects to /accounts/profile/)
LOGIN_REDIRECT_URL = '/'

# EMAIL
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'

# TIMETABLE
TIMETABLE_WIDTH = 5
TIMETABLE_HEIGHT = 9
LESSONS = [('8:00', '1.'), ('8:45', '2.'), ('9:45', '3.'), ('10:35', '4.'), ('11:35', '5.'),
           ('12:25', '6.'), ('13:15', '7.'), ('14:05', '8.'), ('14:50', '9.')]
SHORT_WEEK_DAYS = ["Mo", "Di", "Mi", "Do", "Fr"]
LONG_WEEK_DAYS = [("Montag", 0), ("Dienstag", 1), ("Mittwoch", 2), ("Donnerstag", 3), ("Freitag", 4)]

# LDAP

# Baseline configuration.
AUTH_LDAP_SERVER_URI = "ldap://127.0.0.1"
AUTH_LDAP_USER_SEARCH = LDAPSearch("dc=skole,dc=skolelinux,dc=no",
                                   ldap.SCOPE_SUBTREE, "(&(objectClass=posixAccount)(uid=%(user)s))")
AUTH_LDAP_GROUP_SEARCH = LDAPSearch("dc=skole,dc=skolelinux,dc=no", ldap.SCOPE_SUBTREE,
                                    "(&(objectClass=posixGroup))")
AUTH_LDAP_GROUP_TYPE = PosixGroupType()
AUTH_LDAP_USER_ATTR_MAP = {
    "first_name": "givenName",
    "last_name": "sn",
    "email": "mail"
}
AUTH_LDAP_USER_FLAGS_BY_GROUP = {
    "is_staff": "cn=schoolapps-admins,ou=group,dc=skole,dc=skolelinux,dc=no",
    "is_superuser": "cn=schoolapps-admins,ou=group,dc=skole,dc=skolelinux,dc=no",
}

AUTH_LDAP_ALWAYS_UPDATE_USER = True
AUTH_LDAP_MIRROR_GROUPS = True
AUTH_LDAP_CACHE_GROUPS = True
AUTH_LDAP_GROUP_CACHE_TIMEOUT = 300

# Keep ModelBackend around for per-user permissions and maybe a local superuser.
AUTHENTICATION_BACKENDS = (
    'django_auth_ldap.backend.LDAPBackend',
    'django.contrib.auth.backends.ModelBackend',
)

if DEBUG:
    logger = logging.getLogger('django_auth_ldap')
    logger.addHandler(logging.StreamHandler())
    logger.setLevel(logging.DEBUG)

# Media
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# Use cache for db settings (only on production)
DBSETTINGS_USE_CACHE = not DEBUG

# Cache configs (only on production)
TEST_MEMCACHE = False
if not DEBUG or TEST_MEMCACHE:
    CACHES = {
        'default': {
            'BACKEND': 'django.core.cache.backends.memcached.MemcachedCache',
            'LOCATION': '127.0.0.1:11211',
        }
    }
else:
    CACHES = {
        'default': {
            'BACKEND': 'django.core.cache.backends.dummy.DummyCache',
        }
    }

# PWA
PWA_APP_NAME = 'SchoolApps'
PWA_APP_DESCRIPTION = "Eine Sammlung an nützlichen Apps für den Schulalltag am Katharineum zu Lübeck"
PWA_APP_THEME_COLOR = '#da1f3d'
PWA_APP_BACKGROUND_COLOR = '#ffffff'
PWA_APP_DISPLAY = 'standalone'
PWA_APP_SCOPE = '/'
PWA_APP_ORIENTATION = 'any'
PWA_APP_START_URL = '/'
PWA_APP_ICONS = [
    {
        "src": "/static/icons/android_192.png",
        "sizes": "192x192",
        "type": "image/png"
    },
    {
        "src": "/static/icons/android_512.png",
        "sizes": "512x512",
        "type": "image/png"
    }
]
PWA_APP_SPLASH_SCREEN = [
    {
        'src': '/static/icons/android_512.png',
        'media': '(device-width: 320px) and (device-height: 568px) and (-webkit-device-pixel-ratio: 2)'
    }
]
PWA_APP_DIR = 'ltr'
PWA_SERVICE_WORKER_PATH = os.path.join(BASE_DIR, 'static/common', 'serviceworker.js')
PWA_APP_LANG = 'de-DE'

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'console': {
            'level': 'INFO',
            'class': 'logging.StreamHandler',
        },
        'file': {
            'level': 'DEBUG',
            'class': 'logging.FileHandler',
            'filename': 'log.django',
        },
    },
    'loggers': {
        'django': {
            'handlers': ['console', 'file'],
            'level': os.getenv('DJANGO_LOG_LEVEL', 'DEBUG'),
        },
    },
}
