from datetime import datetime
from typing import Optional


def get_timestamp_in_milliseconds(now: Optional[float] = None) -> int:
    if now is None:
        now = datetime.utcnow().timestamp()
    return int(round(now * 1000))


def get_timestamp_difference_in_seconds(timestamp: int, now: Optional[float] = None) -> float:
    """returns the difference between a timestamp and now in seconds."""
    if now is None:
        now = datetime.utcnow().timestamp()
    _timestamp = timestamp / 1000
    return now - _timestamp
