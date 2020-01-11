from django.conf import settings

__all__ = (
    'TRACK17_API_KEY',
    'TRACK17_API_KEY_FUNCTION',
    'TRACK17_COUNTRIES_URL',
    'TRACK17_CARRIERS_URL'
)


TRACK17_API_KEY = getattr(settings, 'TRACK17_API_KEY', '')
TRACK17_API_KEY_FUNCTION = getattr(settings, 'TRACK17_API_KEY_FUNCTION', None)
TRACK17_COUNTRIES_URL = getattr(
    settings,
    'TRACK17_COUNTRIES_URL',
    'https://www.17track.net/en/apicountry'
)
TRACK17_CARRIERS_URL = getattr(
    settings,
    'TRACK17_CARRIERS_URL',
    'https://www.17track.net/en/apicarrier'
)
