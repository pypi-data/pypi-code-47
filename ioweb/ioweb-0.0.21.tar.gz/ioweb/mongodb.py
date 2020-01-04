import logging
from pprint import pprint, pformat
import time
#from collections import defaultdict

from pymongo import UpdateOne, InsertOne
from pymongo.errors import BulkWriteError


def bulk_write(db, item_type, ops, stat=None, retries=3):
    """
    Tries to apply `ops` Update operations to `item_type`
    collection with `bulk_write` method.
    Gives up if `retries` retries failed.

    Args:
        db - pymongo collection object
        item_type - name of collection
        ops - list of operations like UpdateOne
        stat - instance of `ioweb.stat:Stat`
        retries - number of retries
    """
    if stat:
        stat.inc('bulk-write-%s' % item_type)
    for retry in range(retries):
        try:
            res = db[item_type].bulk_write(ops, ordered=False)
        except BulkWriteError as ex:
            if retry == (retries - 1):
                logging.error(
                    'First failed operation:\n%s' % (
                        pformat(ex.details['writeErrors'][0])
                    )
                )
                raise
            else:
                if stat:
                    stat.inc('bulk-write-%s-retry' % item_type)
        else:
            if stat:
                stat.inc(
                    'bulk-write-%s-upsert' % item_type,
                    res.bulk_api_result['nUpserted']
                )
                stat.inc(
                    'bulk-write-%s-change' % item_type,
                    res.bulk_api_result['nModified']
                )
            break
    return res


class BulkWriter(object):
    def __init__(self, db, item_type, bulk_size=100, stat=None, retries=3):
        self.db = db
        self.item_type = item_type
        self.stat = stat
        self.retries = retries
        self.bulk_size = bulk_size
        self.ops = []

    def _write_ops(self):
        bulk_write(self.db, self.item_type, self.ops, self.stat)
        self.ops = []

    def update_one(self, *args, **kwargs):
        self.ops.append(UpdateOne(*args, **kwargs))
        if len(self.ops) >= self.bulk_size:
            self._write_ops()

    def insert_one(self, *args, **kwargs):
        self.ops.append(InsertOne(*args, **kwargs))
        if len(self.ops) >= self.bulk_size:
            self._write_ops()

    def flush(self):
        if len(self.ops):
            self._write_ops()


def iterate_collection(
        db, item_type, query, sort_field, iter_chunk=1000,
        fields=None, infinite=False, limit=None
    ):
    """
    Iterate over `db[item_type]` collection items matching `query`
    sorted by `sort_field`.

    Intenally, it fetches chunk of `iter_chunk` items at once and
    iterates over it. Then fetch next chunk.
    """
    recent_id = None
    count = 0
    while True:
        if recent_id:
            query[sort_field] = {'$gt': recent_id}
        items = list(db[item_type].find(
            query, fields, sort=[(sort_field, 1)], limit=iter_chunk
        ))
        if not items:
            if infinite:
                sleep_time = 5
                logging.debug(
                    'No items to process. Sleeping %d seconds'
                    % sleep_time
                )
                time.sleep(sleep_time)
                recent_id = None
            else:
                return
        else:
            for item in items:
                yield item
                recent_id = item[sort_field]
                count += 1
                if limit and count >= limit:
                    return
