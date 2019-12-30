# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import logging

from werkzeug.exceptions import NotFound

from udata.models import User, Organization, Reuse, Dataset

from .client import analyze
from .download_counter import DailyDownloadCounter
from .metrics import (
    DatasetViews, ReuseViews, OrganizationViews, UserViews, OrgDatasetsViews,
    OrgReusesViews, aggregate_datasets_daily, aggregate_reuses_daily,
    upsert_metric_for_day, clear_metrics_for_day,
)
from .utils import is_today, route_from, RouteNotFound

log = logging.getLogger(__name__)


class Counter(object):
    '''Handle view count and delegate download count to DailyDownloadCounter'''
    def __init__(self):
        self.routes = {}

    def route(self, endpoint):
        def wrapper(func):
            self.routes[endpoint] = func
            return func
        return wrapper

    def count_for(self, day):
        clear_metrics_for_day(day)
        self.count_views(day)
        dl_counter = DailyDownloadCounter(day)
        dl_counter.count()

    def count_views(self, day):
        params = {
            'period': 'day',
            'date': day,
            'expanded': 1
        }
        for row in analyze('Actions.getPageUrls', **params):
            self.handle_views(row, day)

    def handle_views(self, row, day):
        if 'url' in row:
            try:
                endpoint, kwargs = route_from(row['url'])
                if endpoint in self.routes:
                    log.debug('Found matching route %s for %s',
                              endpoint, row['url'])
                    handler = self.routes[endpoint]
                    handler(row, day, **kwargs)
            except (NotFound, RouteNotFound):
                pass
            except Exception:
                log.exception('Unable to count page views for %s', row['url'])
        if 'subtable' in row:
            for subrow in row['subtable']:
                self.handle_views(subrow, day)


counter = Counter()


@counter.route('datasets.show')
def on_dataset_display(data, day, dataset, **kwargs):
    if isinstance(dataset, Dataset):
        upsert_metric_for_day(dataset, day, data)
        if is_today(day):
            try:
                dataset.save()
            except Exception:
                log.exception('Unable to save dataset %s', dataset.id)
        DatasetViews(dataset).compute()
        if dataset.organization:
            OrgDatasetsViews(dataset.organization).compute()
            aggregate_datasets_daily(dataset.organization, day)


@counter.route('reuses.show')
def on_reuse_display(data, day, reuse, **kwargs):
    if isinstance(reuse, Reuse):
        upsert_metric_for_day(reuse, day, data)
        if is_today(day):
            try:
                reuse.save()
            except Exception:
                log.exception('Unable to save reuse %s', reuse.id)
        ReuseViews(reuse).compute()
        if reuse.organization:
            OrgReusesViews(reuse.organization).compute()
            aggregate_reuses_daily(reuse.organization, day)


@counter.route('organizations.show')
def on_org_display(data, day, org, **kwargs):
    if isinstance(org, Organization):
        upsert_metric_for_day(org, day, data)
        if is_today(day):
            try:
                org.save()
            except Exception:
                log.exception('Unable to save organization %s', org.id)
        OrganizationViews(org).compute()


@counter.route('users.show')
def on_user_display(data, day, user, **kwargs):
    if isinstance(user, User):
        upsert_metric_for_day(user, day, data)
        if is_today(day):
            try:
                user.save()
            except Exception:
                log.exception('Unable to save user %s', user.id)
        UserViews(user).compute()
