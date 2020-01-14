import logging
import sys
from _blake2 import blake2b
from typing import Any

from django.conf import settings
from django.utils.formats import date_format
from django.utils import timezone as tz

logger = logging.getLogger(__name__)


# region BTC sign manager parse features


def parse_certificate(cert_info_string: str, info_tag: str, default: Any = '') -> str:
    """
    For parsing certificate string
    :param cert_info_string: certificate data string
    :param info_tag: name of the data tag (CN =, E = etc.)
    :param default: default value if there is no tag in the string "cert_info_string"
    """

    info_string = None
    if info_tag and info_tag in cert_info_string:
        info_tag_value_pos = cert_info_string.find(info_tag) + len(info_tag)
        info_string = cert_info_string[info_tag_value_pos:200]
        if ',' in info_string:
            info_string = info_string.split(',')[0]

    return info_string if info_string else default

# endregion


# region BTC sign manager date/datetime formatting

def format_date(date: Any, output_format: str = 'd.m.Y', default: Any = '') -> Any:
    """
    Function that returns formatted datetime object
    """

    if date is not None:
        if isinstance(date, tz.datetime) and tz.is_aware(date):
            date = tz.localtime(date)
        return date_format(date, output_format)
    return default

# endregion


# region BTC sign manager class handlers

def get_class_from_path(path: str, split_symbol: str = '.') -> Any:
    class_object = None
    if path and split_symbol in path:
        class_path = path.rsplit(split_symbol, 1)
        module = sys.modules.get(class_path[0])
        class_object = getattr(module, class_path[1], None)
    return class_object


def get_class_from_settings(settings_var_name: str, error_message: str, default: Any) -> Any:
    class_path_from_settings = getattr(settings, settings_var_name, None)
    class_from_settings = get_class_from_path(class_path_from_settings)
    if class_path_from_settings and not class_from_settings:
        logger.error(error_message)
    return class_from_settings or default

# endregion


# region BTC sign manager UUID mapping/hashing


def get_str_hash(data_string: str, digest_size: int) -> blake2b:
    """
    Function for hash generating hash
    :param data_string: string to convert
    :param digest_size: maximum number of bytes
    :return: blake2b
    """

    result_hash = blake2b(digest_size=digest_size)
    result_hash.update(data_string.encode())
    return result_hash.hexdigest()

# endregion
