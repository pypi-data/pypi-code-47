import typing
from gumo.datastore.infrastructure.repository import DatastoreRepositoryMixin


class DatastoreRepositoryMixinForTest(DatastoreRepositoryMixin):
    KIND = None
    KINDS = None

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
        client.delete_multi(keys=[entity.key for entity in query.fetch()])

    @classmethod
    def count_entities_of_kind(cls, kind: str) -> int:
        query = cls.get_datastore_client().query(kind=kind)
        query.keys_only()
        return len(list(query.fetch()))
