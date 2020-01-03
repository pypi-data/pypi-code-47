import pkgutil
from importlib import import_module
from typing import Sequence

from django.conf import settings
from django.http import HttpRequest


def dt_show_toolbar(request: HttpRequest) -> bool:
    from debug_toolbar.middleware import show_toolbar  # noqa

    if not settings.DEBUG:
        return False

    if show_toolbar(request):
        return True
    elif hasattr(request, "user") and request.user.is_superuser:
        return True

    return False


def get_app_packages() -> Sequence[str]:
    """ Find all packages within the aleksis.apps namespace. """

    # Import error are non-fatal here because probably simply no app is installed.
    try:
        import aleksis.apps
    except ImportError:
        return []

    pkgs = []
    for pkg in pkgutil.iter_modules(aleksis.apps.__path__):
        mod = import_module("aleksis.apps.%s" % pkg[1])

        # Add additional apps defined in module's INSTALLED_APPS constant
        additional_apps = getattr(mod, "INSTALLED_APPS", [])
        for app in additional_apps:
            if app not in pkgs:
                pkgs.append(app)

        pkgs.append("aleksis.apps.%s" % pkg[1])

    return pkgs


def is_impersonate(request: HttpRequest) -> bool:
    if hasattr(request, "user"):
        return getattr(request.user, "is_impersonate", False)
    else:
        return False


def has_person(request: HttpRequest) -> bool:
    if hasattr(request, "user"):
        return getattr(request.user, "person", None) is not None
    else:
        return False
