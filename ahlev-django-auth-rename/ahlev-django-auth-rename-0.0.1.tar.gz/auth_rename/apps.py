from django.contrib.auth.apps import AuthConfig
from django.utils.html import format_html
from . import __version__ as VERSION

class AuthRenameConfig(AuthConfig):
    verbose_name = format_html("User Management <span class='version'>{}</span>", VERSION)
