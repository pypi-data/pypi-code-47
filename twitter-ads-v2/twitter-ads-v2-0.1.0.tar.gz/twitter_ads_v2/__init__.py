VERSION = (0, 1, 0)
API_VERSION = '6'

from twitter_ads_v2.utils import get_version
from twitter_ads_v2.client import Client  # noqa

__version__ = get_version()
