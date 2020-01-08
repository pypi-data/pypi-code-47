from django.db import models


class BaseSnapshotManager(models.Manager):
    '''
    Snapshot models manager. Used to add query iterator with limit-offset feature.
    This feature allows querying the whole table in batches without loading all the rows
    in memory.
    '''

    def get_import_model(self):
        '''
        Should return the import_model
        '''
        raise NotImplementedError

    def get_latest_timestamp(self):
        latest = self.get_import_model().objects.order_by('scraped_at').last()
        if latest:
            return latest.scraped_at
        return None

    def get_query(self):
        '''
        Returns all records or records since last imported timestamp.
        '''
        latest_timestamp = self.get_latest_timestamp()
        if latest_timestamp:
            return self.model.objects.filter(scraped_at__gt=latest_timestamp)
        return self.model.objects.all()

    def query_iterator(self, limit):
        '''
        Iterates over all records and returns
        them in sets. The size of the sets is defined
        by the limit parameter.
        '''
        queryset = self.get_query()

        index = limit
        offset = 0

        while True:
            query = queryset[offset:index]

            if not query:
                break
            yield query

            offset += limit
            index += limit

    def limit_offset_iterator(self, chunk):
        '''
        Iterates over all records and returns
        them one by one, using limit and offset instead of a db cursor.

        The default .iterator() Uses db cursor which forces the db
        load all the records in memory at the db server. We want to avoid that here
        because it is expected for the raw models to have millions of records

        Attributes:
        ----------
        chunk: int
            The amount of records to retrieve from the db at one time
        '''
        queryset = self.get_query()

        limit = chunk
        index = limit
        offset = 0

        while True:
            query = queryset[offset:index]

            if not query:
                break

            for item in query:
                yield item

            offset += limit
            index += limit
