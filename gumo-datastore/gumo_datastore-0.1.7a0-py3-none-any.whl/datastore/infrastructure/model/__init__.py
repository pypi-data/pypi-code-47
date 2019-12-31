import dataclasses
import datetime
import typing

from google.cloud import datastore


@dataclasses.dataclass()
class DataModel:
    key: datastore.Key

    exclude_from_indexes: typing.ClassVar[typing.List[str]] = []
    DatastoreEntity: typing.ClassVar = datastore.Entity
    DatastoreKey: typing.ClassVar = datastore.Key

    def to_datastore_entity(self) -> "DataModel.DatastoreEntity":
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
