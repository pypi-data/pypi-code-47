# -*- coding: utf-8 -*-

import datetime

from django.conf import settings
from django.utils import timezone

from haystack import indexes

from .models import Event


class EventIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)

    def get_model(self):
        return Event

    def index_queryset(self, using=None):
        if getattr(settings, 'GLITTER_EVENTS_SEARCH_INDEX_EXPIRED', None):
            today = datetime.datetime.combine(date=datetime.date.today(), time=datetime.time.min)
            today = timezone.make_aware(today)
            qs = self.get_model().objects.filter(start__gte=today).select_related()

        else:
            qs = self.get_model().objects.published().select_related()
        return qs
