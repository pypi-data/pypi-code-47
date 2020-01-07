# -*- coding:utf-8 -*-
import time, datetime
from django.core.management.base import BaseCommand
from bee_django_course.models import UserAssignmentImage
from django.utils import timezone

class Command(BaseCommand):

    def add_arguments(self, parser):
        parser.add_argument('days', type=int, nargs='?', default=90)

    def handle(self, *args, **options):
        # 默认删除2个月前传的图片
        days = options["days"]
        for e in UserAssignmentImage.objects.filter(upload_at__lt=timezone.now() - datetime.timedelta(days=days)):
            e.image.delete()
            # 只删除图片，保留model记录

        return
