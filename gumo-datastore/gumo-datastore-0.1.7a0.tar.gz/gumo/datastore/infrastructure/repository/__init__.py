import typing
from contextlib import contextmanager

from gumo.core.injector import injector
from gumo.core import EntityKey
from gumo.core import NoneKey
from gumo.datastore.infrastructure.configuration import DatastoreConfiguration
from gumo.datastore.infrastructure.entity_key_mapper import EntityKeyMapper

from google.cloud import datastore


class DatastoreRepositoryMixin:
    _datastore_client = None
    _entity_key_mapper = None

    DatastoreEntity = datastore.Entity

    @property
    def datastore_client(self) -> datastore.Client:
        if self._datastore_client is None:
            configuration = injector.get(DatastoreConfiguration)  # type: DatastoreConfiguration
            self._datastore_client = configuration.client

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


@contextmanager
def datastore_transaction():
    datastore_client = injector.get(DatastoreConfiguration).client  # type: datastore.Client

    with datastore_client.transaction():
        yield
