from colour import web2hex
from sass import SassColor

from aleksis.core.models import theme_settings


def get_colour(html_colour: str) -> SassColor:
    rgb = web2hex(html_colour, force_long=True)[1:]
    r, g, b = int(rgb[0:2], 16), int(rgb[2:4], 16), int(rgb[4:6], 16)

    return SassColor(r, g, b, 255)


def get_theme_setting(setting: str) -> str:
    return getattr(theme_settings, setting, "")
