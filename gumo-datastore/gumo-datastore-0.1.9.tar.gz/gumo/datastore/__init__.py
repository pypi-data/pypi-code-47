from logging import getLogger

from gumo.core import EntityKey
from gumo.core import EntityKeyFactory

from gumo.datastore._configuration import configure, get_config, get_datastore_client
from gumo.datastore.infrastructure.configuration import DatastoreConfiguration

from gumo.datastore.infrastructure.repository import datastore_transaction


__all__ = [
    configure.__name__,
    get_config.__name__,
    get_datastore_client.__name__,

    EntityKey.__name__,
    EntityKeyFactory.__name__,
    DatastoreConfiguration.__name__,

    datastore_transaction.__name__,
]

logger = getLogger('gumo.datastore')


configure()
