from datetime import datetime


def get_timestamp_in_milliseconds(now: float = datetime.utcnow().timestamp()) -> int:
    return int(round(now * 1000))


def get_timestamp_difference_in_seconds(timestamp: int, now: float = datetime.utcnow().timestamp()) -> float:
    """returns the difference between a timestamp and now in seconds."""
    _timestamp = timestamp / 1000
    return now - _timestamp
