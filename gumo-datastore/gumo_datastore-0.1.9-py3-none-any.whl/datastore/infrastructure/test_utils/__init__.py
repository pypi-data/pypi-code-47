import typing

from google.cloud.datastore import Query
from gumo.core.injector import injector

from gumo.datastore.infrastructure import EntityKeyMapper
from gumo.datastore.infrastructure.repository import DatastoreRepositoryMixin


class DatastoreRepositoryMixinForTest(DatastoreRepositoryMixin):
    KIND = None
    KINDS = None

    @classmethod
    def get_entity_key_mapper(cls) -> EntityKeyMapper:
        if cls._entity_key_mapper is None:
            cls._entity_key_mapper: EntityKeyMapper = injector.get(EntityKeyMapper)

        return cls._entity_key_mapper

    @classmethod
    def cleanup_entities(cls):
        if cls.KIND is not None:
            cls.cleanup_entities_of_kind(kind=cls.KIND)

        if cls.KINDS is not None and isinstance(cls.KINDS, typing.Iterable):
            for kind in cls.KINDS:
                cls.cleanup_entities_of_kind(kind=kind)

    @classmethod
    def count_entities(cls) -> int:
        if cls.KIND is None:
            raise RuntimeError('KIND must be present.')

        return cls.count_entities_of_kind(kind=cls.KIND)

    @classmethod
    def cleanup_entities_of_kind(cls, kind: str):
        client = cls.get_datastore_client()
        query = client.query(kind=kind)
        query.keys_only()
        while True:
            keys = [entity.key for entity in query.fetch(limit=500)]
            if len(keys) == 0:
                break
            client.delete_multi(keys=keys)

    @classmethod
    def count_entities_of_kind(cls, kind: str) -> int:
        query = cls.get_datastore_client().query(kind=kind)
        query.keys_only()
        return len(list(query.fetch()))

    @classmethod
    def fetch_kinds(cls):
        query = cls.get_datastore_client().query(kind="__kind__")
        query.keys_only()

        kinds = [entity.key.id_or_name for entity in query.fetch()]
        return kinds

    @classmethod
    def cleanup_all_entities(cls):
        for kind in cls.fetch_kinds():
            cls.cleanup_entities_of_kind(kind=kind)

    @classmethod
    def fetch_keys_of_kind(cls, kind: str):
        entity_key_mapper = cls.get_entity_key_mapper()
        client = cls.get_datastore_client()
        query = client.query(kind=kind)
        query.keys_only()
        for entity in query.fetch():
            yield entity_key_mapper.to_entity_key(datastore_key=entity.key)

    @classmethod
    def fetch_keys_of_query(cls, query: Query):
        entity_key_mapper = cls.get_entity_key_mapper()
        query.keys_only()
        for entity in query.fetch():
            yield entity_key_mapper.to_entity_key(datastore_key=entity.key)
