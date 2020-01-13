import os

from db import col

TASK_ID = os.environ.get('CRAWLAB_TASK_ID')


class CrawlabMongoPipeline(object):
    def process_item(self, item, spider):
        col.save(dict(item))
        return item
