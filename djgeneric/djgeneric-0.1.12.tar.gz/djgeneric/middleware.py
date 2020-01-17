import re

from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from django.utils import translation

try:
    LANGUAGE_SESSION_KEY = translation.LANGUAGE_SESSION_KEY
except AttributeError:
    LANGUAGE_SESSION_KEY = '_language'

LANGUAGE_COOKIE_AGE = getattr(settings, "LANGUAGE_COOKIE_AGE", settings.SESSION_COOKIE_AGE)
LANGUAGE_COOKIE_PATH = getattr(settings, "LANGUAGE_COOKIE_PATH", settings.SESSION_COOKIE_PATH)
LANGUAGE_COOKIE_DOMAIN = getattr(settings, "ANGUAGE_COOKIE_DOMAIN", settings.SESSION_COOKIE_DOMAIN)


## From django 1.10
class MiddlewareMixin(object):
    def __init__(self, get_response=None):
        self.get_response = get_response
        super(MiddlewareMixin, self).__init__()

    def __call__(self, request):
        response = None
        if hasattr(self, 'process_request'):
            response = self.process_request(request)
        if not response:
            response = self.get_response(request)
        if hasattr(self, 'process_response'):
            response = self.process_response(request, response)
        return response


## from digital.models import Profile
class TimezoneMiddleware(MiddlewareMixin):
    def process_request(self, request):
        tz = None
        if request.user.is_authenticated:
            try:
                tz = request.user.profile.timezone
            except Profile.DoesNotExist:
                pass
        if tz:
            timezone.activate(tz)
        else:
            timezone.deactivate()


#
# From https://djangosnippets.org/snippets/1220/
#
class RequireLoginMiddleware(MiddlewareMixin):
    """
    Middleware component that wraps the login_required decorator around
    matching URL patterns. To use, add the class to MIDDLEWARE_CLASSES and
    define LOGIN_REQUIRED_URLS and LOGIN_REQUIRED_URLS_EXCEPTIONS in your
    settings.py. For example:
    ------
    LOGIN_REQUIRED_URLS = (
        r'/topsecret/(.*)$',
    )
    LOGIN_REQUIRED_URLS_EXCEPTIONS = (
        r'/topsecret/login(.*)$',
        r'/topsecret/logout(.*)$',
    )
    ------
    LOGIN_REQUIRED_URLS is where you define URL patterns; each pattern must
    be a valid regex.

    LOGIN_REQUIRED_URLS_EXCEPTIONS is, conversely, where you explicitly
    define any exceptions (like login and logout URLs).
    """

    def __init__(self, get_response=None):
        super(RequireLoginMiddleware, self).__init__(get_response)

        self.required = tuple(re.compile(url) for url in
                                      settings.LOGIN_REQUIRED_URLS)
        self.exceptions = tuple(re.compile(url) for url in
                                      settings.LOGIN_REQUIRED_URLS_EXCEPTIONS)

    def process_view(self, request, view_func, view_args, view_kwargs):
        # No need to process URLs if user already logged in
        if request.user.is_authenticated:
            return None

        # An exception match should immediately return None
        for url in self.exceptions:
            if url.match(request.path_info):
                return None

        # Requests matching a restricted URL pattern are returned
        # wrapped with the login_required decorator
        for url in self.required:
            if url.match(request.path_info):
                return login_required(view_func)(request,
                                        *view_args, **view_kwargs)

        # Explicitly return None for all non-matching requests
        return None


class GetParamLocaleMiddleware(MiddlewareMixin):
    """
    This Middleware sets the language from a GET param.
    """

    def get_lang_param(self, request):
        if request.method == 'GET' and request.GET.get('lang'):
            language = request.GET['lang']
            for lang in settings.LANGUAGES:
                if lang[0] == language:
                    return language
        return None

    def process_request(self, request):
        language = self.get_lang_param(request)
        if language:
            translation.activate(language)
            request.LANGUAGE_CODE = translation.get_language()

    def process_response(self, request, response):
        language = self.get_lang_param(request)
        if language:
            if hasattr(request, 'session'):
                request.session[LANGUAGE_SESSION_KEY] = language
            response.set_cookie(settings.LANGUAGE_COOKIE_NAME, language,
                                max_age=LANGUAGE_COOKIE_AGE,
                                path=LANGUAGE_COOKIE_PATH,
                                domain=LANGUAGE_COOKIE_DOMAIN)
        return response
