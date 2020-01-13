from django.conf import settings
from rest_framework.authentication import BaseAuthentication

EXPIRE_MINUTES = getattr(settings, 'REST_FRAMEWORK_TOKEN_EXPIRE_MINUTES', 1)


class Authentication(BaseAuthentication):
    def authenticate(self, request):
        user = request.session.get('userinfo')
        return user, None