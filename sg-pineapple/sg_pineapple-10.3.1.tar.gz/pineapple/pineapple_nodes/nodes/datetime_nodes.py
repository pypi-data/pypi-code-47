from pineapple_core.core.node import node
from pineapple_core.core.types import Any, SumType
import datetime


@node(module="Datetime", name="DatetimeObject", autotrigger=False)
def datetime_object_node(*args: Any, **kwargs: Any) -> datetime.datetime:
    return datetime.datetime(*args, **kwargs)


@node(module="Datetime", name="DatetimeNow", autotrigger=False)
def datetime_now_node(*args: Any, **kwargs: Any) -> datetime.datetime:
    return datetime.datetime.now(*args, **kwargs)


@node(module="Datetime", name="IsoFormat", autotrigger=True)
def isoformat_node(
        timestamp: SumType(
            datetime.datetime,
            datetime.date,
            datetime.time),
        *args: Any,
        **kwargs: Any) -> str:
    return timestamp.isoformat(*args, **kwargs)


@node(module="Datetime", name="DatetimeMinusDatetime", autotrigger=True)
def datetime_minus_datetime(
            datetime1: datetime.datetime,
            datetime2: datetime.datetime
        ) -> datetime.timedelta:
    return datetime1 - datetime2
