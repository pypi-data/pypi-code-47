# coding=utf-8
__author__ = 'bee'
import os, datetime, json

from django.core.management.base import BaseCommand, CommandError
from django.utils import timezone

from bee_django_course.utils import gensee_vod_sync


class Command(BaseCommand):
    def handle(self, *args, **options):
        sync_count = gensee_vod_sync()
        print("[" + timezone.localtime().strftime(
            "%Y-%m-%d %H:%M:%S") + "] gensee_vod_sync_count: " + sync_count.__str__())
        return
