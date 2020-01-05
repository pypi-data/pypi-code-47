# -*- coding: utf-8 -*-

from __future__ import absolute_import, unicode_literals
import os
import datetime as dt
import unittest
from uuid import UUID

from scrapy.spiders import Spider

import scrapyjobparameters.extension as ext


class NoopSpider(Spider):
    name = 'test'


class TestSpiderMetas(unittest.TestCase):

    # fixtures
    fake_job_name = '1/2/3'

    def setUp(self):
        self.metas = ext.SpiderMetas()

    def test_init_state(self):
        self.assertIsNone(self.metas.project_id)
        self.assertIsNone(self.metas.spider_id)
        self.assertIsNone(self.metas.job_id)

        # should be a datetime setup earlier
        self.assertTrue(self.metas.job_time < dt.datetime.utcnow())

    def test_job_name_default(self):
        os.environ['SCRAPY_JOB'] = self.fake_job_name
        metas = ext.SpiderMetas()
        self.assertEqual(metas.job_name, self.fake_job_name)
        os.environ.pop('SCRAPY_JOB')

    def test_job_name_fallback(self):
        # make sure it is not set (should be useless)
        # os.environ.pop('SCRAPY_JOB', None)
        metas = ext.SpiderMetas()
        self.assertNotEqual(metas.job_name, self.fake_job_name)

        partials = metas.job_name.split('/')
        self.assertEqual(len(partials), 3)
        self.assertTrue(UUID(partials[-1], version=4))

    def test_fallback_without_project_id(self):
        project, spider, job = ext.SpiderMetas._fallback(self.fake_job_name)
        self.assertIsNone(project)
        self.assertIsNone(spider)
        self.assertEqual(job, self.fake_job_name)

    def test_fallback(self):
        os.environ['SCRAPY_PROJECT_ID'] = self.fake_job_name
        project, _, _ = ext.SpiderMetas._fallback(self.fake_job_name)
        self.assertEqual(project, self.fake_job_name)
        os.environ.pop('SCRAPY_PROJECT_ID')
