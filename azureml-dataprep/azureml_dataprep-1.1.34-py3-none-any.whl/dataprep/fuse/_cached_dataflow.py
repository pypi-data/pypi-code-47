import os
import sys
import threading
from uuid import uuid4

from azureml.dataprep import read_preppy
from azureml.dataprep.api._loggerfactory import _LoggerFactory


log = _LoggerFactory.get_logger('dprep.fuse._cached_dataflow')


class CachedDataflow:
    def __init__(self, dataflow, cache_dir):
        self._dataflow = dataflow
        self._cache_dir = os.path.join(cache_dir, '__dprep_preppy_{}__'.format(str(uuid4())))
        self._cached = False
        self._cache_lock = threading.Lock()

    @property
    def dataflow(self):
        try:
            self._cache_lock.acquire()
            if not self._cached or not os.path.isfile(os.path.join(self._cache_dir, '_SUCCESS')):
                self._dataflow.write_to_preppy(self._cache_dir).run_local()
                self._cached = True
            return read_preppy(self._cache_dir, include_path=True, verify_exists=True)
        except Exception as e:
            log.warning('Error encountered while caching dataflow: %s', str(e), exc_info=sys.exc_info())
            self._cached = False
            # fallback to use raw dataflow without cache
            return self._dataflow
        finally:
            self._cache_lock.release()
