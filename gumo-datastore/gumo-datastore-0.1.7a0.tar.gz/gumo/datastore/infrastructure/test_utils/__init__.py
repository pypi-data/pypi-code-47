import typing
from gumo.datastore.infrastructure.repository import DatastoreRepositoryMixin


class DatastoreRepositoryMixinForTest(DatastoreRepositoryMixin):
    KIND = None
    KINDS = None

    def cleanup_entities(self):
        if self.KIND is not None:
            self.cleanup_entities_of_kind(kind=self.KIND)

        if self.KINDS is not None and isinstance(self.KINDS, typing.Iterable):
            for kind in self.KINDS:
                self.cleanup_entities_of_kind(kind=kind)

    def count_entities(self) -> int:
        if self.KIND is None:
            raise RuntimeError('KIND must be present.')

        return self.count_entities_of_kind(kind=self.KIND)

    def cleanup_entities_of_kind(self, kind: str):
        query = self.datastore_client.query(kind=kind)
        query.keys_only()
        self.datastore_client.delete_multi(keys=[entity.key for entity in query.fetch()])

    def count_entities_of_kind(self, kind: str) -> int:
        query = self.datastore_client.query(kind=kind)
        query.keys_only()
        return len(list(query.fetch()))
