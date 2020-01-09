# -*- coding:utf-8 -*-
import time, datetime
from django.core.management.base import BaseCommand
from bee_django_course.models import UserCourseSection
from django.utils import timezone

class Command(BaseCommand):

    # 检查自动通过，并且设置间隔时间的课件，达标后自动通过
    def handle(self, *args, **options):
        ucs_list = UserCourseSection.objects.filter(section__auto_pass=True, status=1, section__pass_cooldown__gt=0)
        i = 0
        for ucs in ucs_list:
            if ucs.auto_pass_check():
                ucs.get_pass()
                i += 1
        print("["+timezone.localtime().strftime("%Y-%m-%d %H:%M:%S")+"] auto_pass_count: " + i.__str__() + "/" + ucs_list.count().__str__())
        return
