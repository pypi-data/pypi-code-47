import locale
from typing import Tuple

from django.utils.encoding import DEFAULT_LOCALE_ENCODING
from django.utils.functional import lazy
from django.utils.translation import get_language, to_locale

from .calendarweek import CalendarWeek


def i18n_day_names() -> Tuple[str]:
    """ Return a tuple of day names for the current locale. """

    loc = to_locale(get_language()) + "." + DEFAULT_LOCALE_ENCODING

    try:
        return CalendarWeek.day_names(loc)
    except locale.Error:
        return CalendarWeek.day_names()


def i18n_day_abbrs() -> Tuple[str]:
    """ Return a tuple of day name abbreviations for the current locale. """

    loc = to_locale(get_language()) + "." + DEFAULT_LOCALE_ENCODING

    try:
        return CalendarWeek.day_abbrs(loc)
    except locale.Error:
        return CalendarWeek.day_abbrs()


def i18n_day_name_choices() -> Tuple[Tuple[int, str]]:
    """ Return an enumeration of day names for the current locale. """

    return enumerate(i18n_day_names())


def i18n_day_abbr_choices() -> Tuple[Tuple[int, str]]:
    """ Return an enumeration of day name abbreviations for the current locale. """

    return enumerate(i18n_day_abbrs())


i18n_day_names_lazy = lazy(i18n_day_names, tuple)
i18n_day_abbrs_lazy = lazy(i18n_day_abbrs, tuple)
i18n_day_name_choices_lazy = lazy(i18n_day_name_choices, tuple)
i18n_day_abbr_choices_lazy = lazy(i18n_day_abbr_choices, tuple)
