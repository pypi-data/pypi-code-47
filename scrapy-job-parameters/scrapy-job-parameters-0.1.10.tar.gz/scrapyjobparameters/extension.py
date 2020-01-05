# -*- coding: utf-8 -*-

from __future__ import absolute_import, unicode_literals
import datetime as dt
import logging
import os
from uuid import uuid4

from scrapy import signals

logger = logging.getLogger(__name__)


def _job_name_fallback():
    """SHUB-like unique job name generation"""
    return '0/0/{}'.format(str(uuid4()))


class SpiderMetas(object):
    """Databag of interesting metas information about the spider env.

    As of now we fill the following data:
        - Project ID: parse(job_name) || environ['SCRAPY_PROJECT_ID'] || None
        - Spider ID:  parse(job_name) || None
        - Job ID:     parse(job_name) || job_name
        - Job name:   environ['SCRAPY_JOB'] || uuidv4
        - Job time:   utcnow()
    """

    def __init__(self):
        self.project_id, self.spider_id, self.job_id = None, None, None

        self.job_time = dt.datetime.utcnow()
        self.job_name = os.getenv('SCRAPY_JOB', _job_name_fallback())

    @staticmethod
    def _fallback(job_name):
        """Set default values on the properties we want.

        Returns:
            (str, str, str): respectively job_id, spider_id and project_id

        """
        # if not enough value to unpack this is not a SH id, so keep the whole string
        return os.environ.get('SCRAPY_PROJECT_ID'), None, job_name

    def _parse_job_name(self, job):
        # NOTE our other extension (datadog) uses other settings to find
        # project_id and spider_id values. While it is certainly not a good
        # idea to link their code, I guess we should be consistent and use the
        # same most effective solution.

        # for ScrapingHub, job_id is 'PROJECT_ID/SPIDER_ID/JOB_ID'
        try:
            (project_id, spider_id, job_id) = job.split('/')
        except (ValueError, AttributeError) as e:
            logger.warning('failed to parse job name ({}): {}'.format(job, e))
            (project_id, spider_id, job_id) = self._fallback(job)

        return project_id, spider_id, job_id

    def populate(self):
        self.project_id, self.spider_id, self.job_id = self._parse_job_name(self.job_name)

    def to_dict(self):
        return {
            'project_id': self.project_id,
            'spider_id': self.spider_id,
            'job_id': self.job_id,

            'job_time': self.job_time,
            'job_name': self.job_name,
        }

    def __repr__(self):
        return 'Metas(project={}, spider={}, job={}, time={})'.format(self.project_id,
                                                                      self.spider_id,
                                                                      self.job_id,
                                                                      self.job_time)


# NOTE use enable parameter
class JobParametersExtension(object):

    def __init__(self):
        # namespacing those parameters under a `metas` attribute would be great
        # nut scrapy `feedexport` uses `getattr(spider, key)` to bind those
        # information. So we can't nest objects.
        self.metas = SpiderMetas()

    @classmethod
    def from_crawler(cls, crawler):
        # instantiate the extension object
        ext = cls()

        # connect the extension object to signals
        crawler.signals.connect(ext.spider_opened, signal=signals.spider_opened)

        return ext

    def spider_opened(self, spider):
        """Finally expose to the spider the settings."""
        self.metas.populate()
        for k, v in self.metas.to_dict().items():
            logger.debug('binding meta attribute to spider: {}={}'.format(k, v))
            setattr(spider, k, v)
