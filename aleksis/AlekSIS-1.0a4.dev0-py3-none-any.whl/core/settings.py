import os
import sys
from glob import glob

from django.utils.translation import ugettext_lazy as _

from dynaconf import LazySettings
from easy_thumbnails.conf import Settings as thumbnail_settings

from .util.core_helpers import get_app_packages

ENVVAR_PREFIX_FOR_DYNACONF = "ALEKSIS"
DIRS_FOR_DYNACONF = ["/etc/aleksis"]

SETTINGS_FILE_FOR_DYNACONF = []
for directory in DIRS_FOR_DYNACONF:
    SETTINGS_FILE_FOR_DYNACONF += glob(os.path.join(directory, "*.ini"))
    SETTINGS_FILE_FOR_DYNACONF += glob(os.path.join(directory, "*.yaml"))
    SETTINGS_FILE_FOR_DYNACONF += glob(os.path.join(directory, "*.toml"))

_settings = LazySettings(
    ENVVAR_PREFIX_FOR_DYNACONF=ENVVAR_PREFIX_FOR_DYNACONF,
    SETTINGS_FILE_FOR_DYNACONF=SETTINGS_FILE_FOR_DYNACONF,
)

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = _settings.get("secret_key", "DoNotUseInProduction")

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = _settings.get("maintenance.debug", False)
INTERNAL_IPS = _settings.get("maintenance.internal_ips", [])
DEBUG_TOOLBAR_CONFIG = {
    "RENDER_PANELS": True,
    "SHOW_COLLAPSED": True,
    "JQUERY_URL": "",
    "SHOW_TOOLBAR_CALLBACK": "aleksis.core.util.core_helpers.dt_show_toolbar",
}

ALLOWED_HOSTS = _settings.get("http.allowed_hosts", [])

# Application definition
INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "django_global_request",
    "settings_context_processor",
    "sass_processor",
    "easyaudit",
    "dbsettings",
    "django_any_js",
    "django_yarnpkg",
    "django_tables2",
    "easy_thumbnails",
    "image_cropping",
    "maintenance_mode",
    "menu_generator",
    "phonenumber_field",
    "debug_toolbar",
    "django_select2",
    "hattori",
    "django_otp.plugins.otp_totp",
    "django_otp.plugins.otp_static",
    "django_otp",
    "otp_yubikey",
    "aleksis.core",
    "impersonate",
    "two_factor",
    "material"
]

INSTALLED_APPS += get_app_packages()

STATICFILES_FINDERS = [
    "django.contrib.staticfiles.finders.FileSystemFinder",
    "django.contrib.staticfiles.finders.AppDirectoriesFinder",
    "django_yarnpkg.finders.NodeModulesFinder",
    "sass_processor.finders.CssFinder",
]


MIDDLEWARE = [
    #    'django.middleware.cache.UpdateCacheMiddleware',
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.locale.LocaleMiddleware",
    "django_global_request.middleware.GlobalRequestMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "debug_toolbar.middleware.DebugToolbarMiddleware",
    "django_otp.middleware.OTPMiddleware",
    "impersonate.middleware.ImpersonateMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "easyaudit.middleware.easyaudit.EasyAuditMiddleware",
    "maintenance_mode.middleware.MaintenanceModeMiddleware",
    #    'django.middleware.cache.FetchFromCacheMiddleware'
]

ROOT_URLCONF = "aleksis.core.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
                "maintenance_mode.context_processors.maintenance_mode",
                "settings_context_processor.context_processors.settings",
            ],
        },
    },
]

THUMBNAIL_PROCESSORS = (
    "image_cropping.thumbnail_processors.crop_corners",
) + thumbnail_settings.THUMBNAIL_PROCESSORS

# Already included by base template / Bootstrap
IMAGE_CROPPING_JQUERY_URL = None

WSGI_APPLICATION = "aleksis.core.wsgi.application"


# Database
# https://docs.djangoproject.com/en/2.1/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": _settings.get("database.name", "aleksis"),
        "USER": _settings.get("database.username", "aleksis"),
        "PASSWORD": _settings.get("database.password", None),
        "HOST": _settings.get("database.host", "127.0.0.1"),
        "PORT": _settings.get("database.port", "5432"),
        "ATOMIC_REQUESTS": True,
    }
}

if _settings.get("caching.memcached.enabled", True):
    CACHES = {
        "default": {
            "BACKEND": "django.core.cache.backends.memcached.MemcachedCache",
            "LOCATION": _settings.get("caching.memcached.address", "127.0.0.1:11211"),
        }
    }

# Password validation
# https://docs.djangoproject.com/en/2.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {"NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",},
    {"NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",},
    {"NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",},
    {"NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",},
]

# Authentication backends are dynamically populated
AUTHENTICATION_BACKENDS = []

if _settings.get("ldap.uri", None):
    # LDAP dependencies are not necessarily installed, so import them here
    import ldap  # noqa
    from django_auth_ldap.config import LDAPSearch, GroupOfNamesType  # noqa

    # Enable Django's integration to LDAP
    AUTHENTICATION_BACKENDS.append("django_auth_ldap.backend.LDAPBackend")

    AUTH_LDAP_SERVER_URI = _settings.get("ldap.uri")

    # Optional: non-anonymous bind
    if _settings.get("ldap.bind.dn", None):
        AUTH_LDAP_BIND_DN = _settings.get("ldap.bind.dn")
        AUTH_LDAP_BIND_PASSWORD = _settings.get("ldap.bind.password")

    # Search attributes to find users by username
    AUTH_LDAP_USER_SEARCH = LDAPSearch(
        _settings.get("ldap.users.base"),
        ldap.SCOPE_SUBTREE,
        _settings.get("ldap.users.filter", "(uid=%(user)s)"),
    )

    # Mapping of LDAP attributes to Django model fields
    AUTH_LDAP_USER_ATTR_MAP = {
        "first_name": _settings.get("ldap.map.first_name", "givenName"),
        "last_name": _settings.get("ldap.map.first_name", "sn"),
        "email": _settings.get("ldap.map.email", "mail"),
    }

# Add ModelBckend last so all other backends get a chance
# to verify passwords first
AUTHENTICATION_BACKENDS.append("django.contrib.auth.backends.ModelBackend")

# Internationalization
# https://docs.djangoproject.com/en/2.1/topics/i18n/

LANGUAGES = [
    ("de", _("German")),
    ("en", _("English")),
]
LANGUAGE_CODE = _settings.get("l10n.lang", "en")
TIME_ZONE = _settings.get("l10n.tz", "UTC")
USE_I18N = True
USE_L10N = True
USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.1/howto/static-files/


STATIC_URL = _settings.get("static.url", "/static/")
MEDIA_URL = _settings.get("media.url", "/media/")

LOGIN_REDIRECT_URL = "index"
LOGOUT_REDIRECT_URL = "index"

STATIC_ROOT = _settings.get("static.root", os.path.join(BASE_DIR, "static"))
MEDIA_ROOT = _settings.get("media.root", os.path.join(BASE_DIR, "media"))
NODE_MODULES_ROOT = _settings.get("node_modules.root", os.path.join(BASE_DIR, "node_modules"))

YARN_INSTALLED_APPS = ["datatables", "highlight.js", "jquery", "manup", "materialize-css", "moment", "popper.js", "prop-types", "react", "react-dom", "material-design-icons-iconfont", "select2"]

JS_URL = _settings.get("js_assets.url", STATIC_URL)
JS_ROOT = _settings.get("js_assets.root", NODE_MODULES_ROOT + "/node_modules")

SELECT2_CSS = JS_URL + "/select2/dist/css/select2.min.css"
SELECT2_JS = JS_URL + "/select2/dist/js/select2.min.js"
SELECT2_I18N_PATH = JS_URL + "/select2/dist/js/i18n"

ANY_JS = {
    "DataTables": {"js_url": JS_URL + "/datatables/media/js/jquery.dataTables.min.js"},
    "materialize": {"js_url": JS_URL + "/materialize-css/dist/js/materialize.min.js"},
    "jQuery": {"js_url": JS_URL + "/jquery/dist/jquery.min.js"},
    "material-design-icons": {"css_url": JS_URL + "/material-design-icons-iconfont/dist/material-design-icons.css"},
}

SASS_PROCESSOR_AUTO_INCLUDE = False
SASS_PROCESSOR_CUSTOM_FUNCTIONS = {
    "get-colour": "aleksis.core.util.sass_helpers.get_colour",
    "get-theme-setting": "aleksis.core.util.sass_helpers.get_theme_setting",
}
SASS_PROCESSOR_INCLUDE_DIRS = [_settings.get("materialize.sass_path", JS_ROOT + "/materialize-css/sass/"), STATIC_ROOT]

ADMINS = _settings.get("contact.admins", [])
SERVER_EMAIL = _settings.get("contact.from", "root@localhost")
DEFAULT_FROM_EMAIL = _settings.get("contact.from", "root@localhost")
MANAGERS = _settings.get("contact.admins", [])

if _settings.get("mail.server.host", None):
    EMAIL_HOST = _settings.get("mail.server.host")
    EMAIL_USE_TLS = _settings.get("mail.server.tls", False)
    EMAIL_USE_SSL = _settings.get("mail.server.ssl", False)
    if _settings.get("mail.server.port", None):
        EMAIL_PORT = _settings.get("mail.server.port")
    if _settings.get("mail.server.user", None):
        EMAIL_HOST_USER = _settings.get("mail.server.user")
        EMAIL_HOST_PASSWORD = _settings.get("mail.server.password")

TEMPLATE_VISIBLE_SETTINGS = ["ADMINS", "DEBUG"]

MAINTENANCE_MODE = _settings.get("maintenance.enabled", None)
MAINTENANCE_MODE_IGNORE_IP_ADDRESSES = _settings.get(
    "maintenance.ignore_ips", _settings.get("maintenance.internal_ips", [])
)
MAINTENANCE_MODE_GET_CLIENT_IP_ADDRESS = "ipware.ip.get_ip"
MAINTENANCE_MODE_IGNORE_SUPERUSER = True
MAINTENANCE_MODE_STATE_FILE_PATH = _settings.get(
    "maintenance.statefile", "maintenance_mode_state.txt"
)

IMPERSONATE = {"USE_HTTP_REFERER": True, "REQUIRE_SUPERUSER": True, "ALLOW_SUPERUSER": True}

DJANGO_TABLES2_TEMPLATE = "django_tables2/bootstrap4.html"

ANONYMIZE_ENABLED = _settings.get("maintenance.anonymisable", True)

LOGIN_URL = "two_factor:login"

if _settings.get("2fa.call.enabled", False):
    TWO_FACTOR_CALL_GATEWAY = "two_factor.gateways.twilio.gateway.Twilio"

if _settings.get("2fa.sms.enabled", False):
    TWO_FACTOR_SMS_GATEWAY = "two_factor.gateways.twilio.gateway.Twilio"

if _settings.get("2fa.twilio.sid", None):
    MIDDLEWARE.insert(
        MIDDLEWARE.index("django_otp.middleware.OTPMiddleware") + 1,
        "two_factor.middleware.threadlocals.ThreadLocals",
    )
    TWILIO_SID = _settings.get("2fa.twilio.sid")
    TWILIO_TOKEN = _settings.get("2fa.twilio.token")
    TWILIO_CALLER_ID = _settings.get("2fa.twilio.callerid")

_settings.populate_obj(sys.modules[__name__])
