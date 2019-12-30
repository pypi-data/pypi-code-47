from django.conf import settings

# Where to redirect after successful login..
LOGIN_REDIRECT_URL = getattr(
    settings, "WEBAUTHIN_LOGIN_REDIRECT_URL", settings.LOGIN_REDIRECT_URL
)

# Where to redirect after login errors.
LOGIN_ERROR_URL = getattr(settings, "WEBAUTHIN_LOGIN_ERROR_URL", settings.LOGIN_URL)

# Where to redirect after successful key registration.
REGISTRATION_REDIRECT_URL = getattr(
    settings, "WEBAUTHIN_REGISTRATION_REDIRECT_URL", settings.LOGIN_REDIRECT_URL
)

# Where to redirect after key registration error.
REGISTRATION_ERROR_URL = getattr(
    settings, "WEBAUTHIN_REGISTRATION_ERROR_URL", settings.LOGIN_REDIRECT_URL
)
