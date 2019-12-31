import typing
from contextlib import contextmanager
from injector import singleton

from gumo.core.injector import injector
from gumo.core import EntityKey
from gumo.core import NoneKey
from gumo.datastore.infrastructure.configuration import DatastoreConfiguration
from gumo.datastore.infrastructure.entity_key_mapper import EntityKeyMapper

from google.cloud import datastore
from google.cloud.datastore import Query


class DatastoreRepositoryMixin:
    _datastore_client = None
    _entity_key_mapper = None

    DatastoreEntity = datastore.Entity

    @classmethod
    def get_datastore_client(cls) -> datastore.Client:
        if cls._datastore_client is None:
            configuration: DatastoreConfiguration = injector.get(DatastoreConfiguration, scope=singleton)
            cls._datastore_client = configuration.client

        return cls._datastore_client

    @property
    def datastore_client(self) -> datastore.Client:
        if self._datastore_client is None:
            self.get_datastore_client()

        return self._datastore_client

    @property
    def entity_key_mapper(self) -> EntityKeyMapper:
        if self._entity_key_mapper is None:
            self._entity_key_mapper = injector.get(EntityKeyMapper)  # type: EntityKeyMapper

        return self._entity_key_mapper

    def to_entity_key(self, datastore_key: typing.Optional[datastore.Key]) -> EntityKey:
        return self.entity_key_mapper.to_entity_key(datastore_key=datastore_key)

    def to_datastore_key(self, entity_key: typing.Union[EntityKey, NoneKey, None]) -> typing.Optional[datastore.Key]:
        return self.entity_key_mapper.to_datastore_key(entity_key=entity_key)

    def _fetch_page(
        self, query: Query, limit: int, start_cursor: typing.Optional[bytes]
    ) -> typing.Tuple[typing.List[DatastoreEntity], typing.Optional[str], bool]:
        query_iterator = query.fetch(limit=limit, start_cursor=start_cursor)
        pages = query_iterator.pages
        page = next(pages)
        entities = list(page)

        next_cursor = (
            query_iterator.next_page_token.decode("utf-8")
            if query_iterator.next_page_token
            else None
        )
        if next_cursor:
            has_more = len(list(query.fetch(limit=1, start_cursor=next_cursor))) > 0
        else:
            has_more = False

        if not has_more:
            next_cursor = None

        return entities, next_cursor, has_more


@contextmanager
def datastore_transaction():
    datastore_client = injector.get(DatastoreConfiguration).client  # type: datastore.Client

    with datastore_client.transaction():
        yield
