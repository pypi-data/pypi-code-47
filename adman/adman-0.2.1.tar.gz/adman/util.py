from datetime import datetime, timedelta, timezone

def single(seq, cond=None):
    """Extract a single item from a sequence matching condition `cond`

    Raises IndexError if there is not exactly one item matching the condition.
    """
    NOMATCH = object()

    result = single_or(seq, NOMATCH, cond)

    if result is NOMATCH:
        raise IndexError("No items found")
    return result


def single_or(seq, default, cond=None):
    """Extract a single item from a sequence matching condition `cond`

    Returns `default` if no item is found.

    Raises IndexError if there is more than one item matching the condition.
    """
    if cond is None:
        cond = lambda x: True

    NOMATCH = object()
    result = NOMATCH

    for x in seq:
        if not cond(x):
            continue
        if result is not NOMATCH:
            raise IndexError("Multiple items found")
        result = x

    if result is NOMATCH:
        result = default
    return result

def int_from_bytes(data, offset, length, byteorder):
    chunk = data[offset : offset+length]
    if len(chunk) != length:
        raise ValueError("Truncated data")

    return int.from_bytes(chunk, byteorder)


# FILETIME is stored as a large integer that represents the number of
# 100-nanosecond intervals since January 1, 1601 (UTC).
MS_EPOCH = datetime(year=1601, month=1, day=1, tzinfo=timezone.utc)
INT64_MAX = (1<<63)-1

def FILETIME_to_datetime(ts):
    dt = timedelta(microseconds=ts/10)
    try:
        return MS_EPOCH + dt
    except OverflowError:
        # AD can return INT64_MAX which is in year 30848, and can't be
        # represented by datetime. We return datetime.max as a sentinel.
        return datetime.max

def datetime_to_FILETIME(date):
    if date == datetime.max:
        return INT64_MAX
    dt = date - MS_EPOCH
    sec = dt.days*24*60*60 + dt.seconds
    usec = sec*1000*1000 + dt.microseconds
    return usec * 10

def utcnow():
    return datetime.now(timezone.utc)
