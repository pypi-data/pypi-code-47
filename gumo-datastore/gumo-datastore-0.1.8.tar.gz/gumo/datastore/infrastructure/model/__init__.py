import dataclasses
import datetime
import typing

from gumo.datastore.infrastructure.alias import DatastoreEntity
from gumo.datastore.infrastructure.alias import DatastoreKey


@dataclasses.dataclass()
class DataModel:
    key: DatastoreKey

    exclude_from_indexes: typing.ClassVar[typing.List[str]] = []
    DatastoreEntity: typing.ClassVar = DatastoreEntity
    DatastoreKey: typing.ClassVar = DatastoreKey

    def to_datastore_entity(self) -> DatastoreEntity:
        raise NotImplementedError()

    @classmethod
    def from_datastore_entity(cls, doc: DatastoreEntity) -> "DataModel":
        raise NotImplementedError()

    @classmethod
    def convert_optional_datetime(
        cls, t: typing.Optional[datetime.datetime]
    ) -> typing.Optional[datetime.datetime]:
        if t is None:
            return None

        return cls.convert_datetime(t)

    @classmethod
    def convert_datetime(cls, t: datetime.datetime) -> datetime.datetime:
        return datetime.datetime(
            year=t.year,
            month=t.month,
            day=t.day,
            hour=t.hour,
            minute=t.minute,
            second=t.second,
            microsecond=t.microsecond,
            tzinfo=datetime.timezone.utc,
        )
