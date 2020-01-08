"""
GoodWan client library: helpers
"""
import datetime
import re

IN_NORMALIZED_FORMAT = "%Y-%m-%dT%H:%M:%S%z"
OUT_FORMAT = "%Y-%m-%dT%H:%M:%S%z"
IN_RE = re.compile(
    r"^(?P<y>\d{4})-(?P<m>\d{2})-(?P<d>\d{2})"
    r"T(?P<h>\d{2}):(?P<i>\d{2}):(?P<s>\d{2})"
    r"(?:\.(?P<ms>\d{1,6}))?"
    r"\+(?P<of_h>\d{2}):?(?P<of_m>\d{2})$"
)


def str_to_datetime(date_string, timezone):
    """
    Convert string to datetime
    :param date_string: date string
    :type date_string: str
    :param timezone: pytz timezone
    :type timezone: pytz.timezone
    :return: datetime
    :rtype: datetime.datetime
    """
    matches = IN_RE.match(date_string)
    if not matches:
        raise ValueError("Wrong date format \"{}\"".format(date_string))

    ms = matches.group("ms")
    microseconds = 10**(6 - len(ms)) * int(ms) if ms else 0
    normalized_str = "{}-{}-{}T{}:{}:{}+{}{}".format(
        matches.group("y"),
        matches.group("m"),
        matches.group("d"),
        matches.group("h"),
        matches.group("i"),
        matches.group("s"),
        matches.group("of_h"),
        matches.group("of_m"),
    )
    result = datetime.datetime.strptime(normalized_str, IN_NORMALIZED_FORMAT)
    result = result.replace(microsecond=microseconds)

    if result.tzinfo is None:
        result = timezone.localize(result, is_dst=None)
    else:
        result = result.astimezone(timezone)

    return result


def datetime_to_str(datetime_value, timezone):
    """
    Convert datetime to string
    :param datetime_value: datetime value
    :type datetime_value: datetime.datetime
    :param timezone: pytz timezone
    :type timezone: pytz.timezone
    :return: datetime string
    :rtype: str
    """
    if datetime_value.tzinfo is None:
        datetime_value = timezone.localize(datetime_value)
    return datetime_value.strftime("%Y-%m-%dT%H:%M:%S%z")
