#!/usr/bin/env python
# -*- coding:utf-8 -*-
from __future__ import unicode_literals
import datetime, pytz
from django.core.urlresolvers import reverse
from django.db import models, transaction
from django.contrib.auth.models import User
from django.utils import timezone
from django.conf import settings
from django.db.models.functions import TruncMonth, TruncDay

import os, random
from django.dispatch import receiver
from django.db.models.signals import post_save
from .signals import ucs_passed
from PIL import Image, ExifTags
from django.db.models import Q, Sum, Count
from django.db import connection
from .signals import user_course_changed, user_certify_update_status
# Create your models here.
from .dt import get_datetime_with_scope_offset, LOCAL_TIMEZONE
from django.conf import settings
from bee_django_object_field.custom_fields import DictField

if hasattr(settings, 'ASSIGNMENT_IMG_SIZE'):
    ASSIGNMENT_IMG_SIZE = settings.ASSIGNMENT_IMG_SIZE
else:
    ASSIGNMENT_IMG_SIZE = (1024, 768)

if hasattr(settings, 'COURSE_IMG_SIZE'):
    COURSE_IMG_SIZE = settings.COURSE_IMG_SIZE
else:
    COURSE_IMG_SIZE = (800, 600)


# 压缩上传作业图片
def resize_assignment_image(img_field):
    img = Image.open(img_field)

    try:
        for orientation in ExifTags.TAGS.keys():
            if ExifTags.TAGS[orientation] == 'Orientation':
                exif = dict(img._getexif().items())

                if exif[orientation] == 3:
                    img = img.rotate(180, expand=True)
                elif exif[orientation] == 6:
                    img = img.rotate(270, expand=True)
                elif exif[orientation] == 8:
                    img = img.rotate(90, expand=True)

                break
    except:
        pass

    img.thumbnail(ASSIGNMENT_IMG_SIZE, Image.ANTIALIAS)
    img.save(img_field.path)

    img.close()


# 压缩课程课件配图
def resize_course_image(img_field):
    img = Image.open(img_field)

    try:
        for orientation in ExifTags.TAGS.keys():
            if ExifTags.TAGS[orientation] == 'Orientation':
                exif = dict(img._getexif().items())

                if exif[orientation] == 3:
                    img = img.rotate(180, expand=True)
                elif exif[orientation] == 6:
                    img = img.rotate(270, expand=True)
                elif exif[orientation] == 8:
                    img = img.rotate(90, expand=True)

                break
    except:
        pass

    img.thumbnail(COURSE_IMG_SIZE, Image.ANTIALIAS)
    img.save(img_field.path)

    img.close()


# 课程
class Course(models.Model):
    name = models.CharField(max_length=180, verbose_name='课程名字')  # 名字
    subtitle = models.CharField(max_length=180, null=True, verbose_name='课程副标题', blank=True)  # 副标题
    level = models.IntegerField(default=0, verbose_name='课程的level', blank=True)  # 课程的level
    is_del = models.IntegerField(default=0)
    created_at = models.DateTimeField(default=timezone.now)
    teacher = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, blank=True, verbose_name='授课老师')
    image = models.ImageField(null=True, blank=True, verbose_name='配图', upload_to='course/face')
    status = models.IntegerField(verbose_name='状态', default=0)  # 0 不显示，1 显示在列表
    template = models.CharField(max_length=180, null=True, blank=True, verbose_name='模版',
                                help_text='在项目中custom_user下新建模版文件custom_user_course_section_list_[template].html')
    punch_period = models.IntegerField(choices=((1, '天'),), verbose_name='周期', help_text='用于课程打卡，如不需要可不填写', null=True,
                                       blank=True)  # month/week/day
    punch_duration = models.IntegerField(verbose_name='时长', null=True, blank=True, help_text='用于课程打卡，如不需要可不填写')  # 时长

    class Meta:
        db_table = 'bee_django_course_course'
        app_label = 'bee_django_course'
        ordering = ["-id"]
        verbose_name = 'course课程'
        permissions = (
            ('can_manage_course', '可以进入课程管理页'),
            ('view_all_courses', '可以查看所有课程'),
            ('can_choose_course', 'can choose course'),
        )

    def __unicode__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('bee_django_course:course_detail', kwargs={'pk': self.pk})

    def is_my_course(self, user):
        user_course = UserCourse.objects.filter(user=user, course=self)
        if user_course.exists():
            return user_course.first()
        else:
            return None

    def get_punch_period_str(self):
        if self.punch_period == 1:
            return '天'
        if self.punch_period == 7:
            return '天'
        return ''


class Section(models.Model):
    name = models.CharField(max_length=180, verbose_name='课件名字')  # 名字
    info = models.TextField(null=True, blank=True, verbose_name='正文')
    videos = models.ManyToManyField("bee_django_course.Video")
    has_textwork = models.BooleanField(verbose_name='是否需要文字作业', default=False)
    textwork_info = models.TextField(verbose_name='作业说明', null=True, blank=True)
    has_videowork = models.BooleanField(verbose_name='是否需要视频录制', default=False)
    has_imagework = models.BooleanField(verbose_name='是否需要上传图片', default=False)
    has_questionwork = models.BooleanField(verbose_name='是否需要回答问题', default=False)
    question_passed_at = models.DateTimeField(verbose_name='问答通过时间', null=True, blank=True)
    video_length_req = models.IntegerField(verbose_name='要求录制时长(分钟)', default=0)
    image_count_req = models.IntegerField(verbose_name='要求提交图片数量', default=0)

    has_to_finish_course_video = models.BooleanField(verbose_name='是否需要看完课件所有视频', default=False)

    created_at = models.DateTimeField(default=timezone.now)
    auto_pass = models.BooleanField(default=False, verbose_name='是否自动通过')  # 课件是否自动通过
    pass_cooldown = models.IntegerField(default=0, verbose_name='间隔天数', help_text='通过时距离上一课件的间隔天数')
    type = models.IntegerField(default=0)  # 0 普通课件，1 预备课件

    image = models.ImageField(null=True, blank=True, verbose_name='配图', upload_to='section/face')

    need_certify = models.BooleanField(verbose_name='是否需要认证', default=False)

    #                                    help_text='认证课件将在其他条件达标后 显示认证按钮')

    class Meta:
        db_table = 'bee_django_course_section'
        app_label = 'bee_django_course'
        ordering = ["-id"]
        verbose_name = 'course课件'
        permissions = (
            ('view_all_sections', '可以查看所有课件'),
        )

    def __unicode__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('bee_django_course:section_detail', kwargs={'pk': self.pk})

    def get_auto_pass_text(self):
        if self.auto_pass:
            return '是'
        else:
            return '否'

    def get_questions(self):
        return self.sectionquestion_set.all()

    # 添加问题
    def add_question(self, question_type):
        question = SectionQuestion()
        question.section = self
        question.question_type = question_type
        question.question = '新建问题'
        question.save()
        return question


# 课件的用户笔记
class UserSectionNote(models.Model):
    section = models.ForeignKey(Section)
    user = models.ForeignKey(settings.AUTH_USER_MODEL)
    note = models.TextField(verbose_name='学习笔记')
    is_open = models.BooleanField(default=True, verbose_name='公开笔记')
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(default=timezone.now)
    is_stick = models.BooleanField(default=False, verbose_name='是否置顶')
    is_digest = models.BooleanField(default=False, verbose_name='是否精华')


# 课件的附件
class SectionAttach(models.Model):
    name = models.CharField(max_length=180, verbose_name='附件名称', null=True, blank=True)
    section = models.ForeignKey(Section)
    file = models.FileField(verbose_name='附件', upload_to='sections/%Y/%m/%d/')
    upload_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'bee_django_course_section_attach'

    def file_name(self):
        if self.name:
            return self.name
        else:
            return os.path.basename(self.file.name)


# 课程课件中间件
class CourseSectionMid(models.Model):
    course = models.ForeignKey("bee_django_course.Course", verbose_name='课程')  # 课程
    section = models.ForeignKey("bee_django_course.Section", verbose_name="课件")  # 课程包
    points = models.IntegerField(default=0, verbose_name='通过后获得的M币')
    order_by = models.IntegerField(default=0, verbose_name="顺序")  # 顺序
    mins = models.IntegerField(null=True, blank=True, verbose_name='达标分钟数')  # 达标分钟数 #可能弃用
    pre_name = models.CharField(max_length=180, verbose_name='前缀标题', null=True, blank=True)

    class Meta:
        db_table = 'bee_django_course_section_mid'
        app_label = 'bee_django_course'
        ordering = ['order_by']

    def __unicode__(self):
        return ("CourseSectionMid->course:" + self.course.name)


class Video(models.Model):
    video_id = models.CharField(max_length=180, null=True)  # 视频 id，16位 hex 字符串
    status = models.CharField(max_length=180, null=True)  # 视频状态。”OK”表示视频处理成功，”FAIL”表示视频处理失败。
    duration = models.CharField(max_length=180, null=True)  # 片长（单位:秒）
    image = models.CharField(max_length=180, null=True)  # 视频截图地址
    # ===========
    title = models.CharField(max_length=180, null=True, verbose_name='标题')  # 视频标题
    file_name = models.CharField(max_length=180, null=True, blank=True, verbose_name='视频文件名')  # 七牛
    info = models.TextField(verbose_name='说明', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    # created_by = models.ForeignKey("users.User", related_name='cc_video_user', null=True)  # 由谁上传
    # video_status = models.IntegerField(default=1, null=True)  # 状态 1-正常，2-正常（删除视频）

    class Meta:
        db_table = 'bee_django_course_video'
        app_label = 'bee_django_course'
        ordering = ['-created_at']
        verbose_name = 'course视频'
        permissions = (
            ('view_all_videos', '可以查看所有视频'),
        )

    def __unicode__(self):
        return ("视频:" + self.title)

    def get_absolute_url(self):
        # return reverse('bee_django_course:video_detail', kwargs={'pk': self.pk})
        return reverse('bee_django_course:video_list')


class SectionVideo(models.Model):
    section = models.ForeignKey(Section, verbose_name='关联的课件')
    video = models.ForeignKey(Video, verbose_name='关联的视频')
    created_at = models.DateTimeField(auto_now_add=True)
    order = models.IntegerField(default=0, verbose_name='在课件里的排序')

    class Meta:
        db_table = 'bee_django_course_section_video'
        ordering = ['order']


COURSE_SECTION_QUESTION_TYPE_CHOICES = ((1, "单选"), (2, "多选"))


class SectionQuestion(models.Model):
    section = models.ForeignKey(Section, verbose_name='关联的课件')
    question = models.CharField(max_length=180, verbose_name='问题')
    question_type = models.IntegerField(default=1, verbose_name='问题类型', choices=COURSE_SECTION_QUESTION_TYPE_CHOICES)
    order_by = models.IntegerField(default=0, verbose_name='顺序')
    options = models.ManyToManyField("bee_django_course.SectionQuestionOption")
    tip_wrong = models.TextField(null=True, verbose_name="错误时提示词")
    tip_correct = models.TextField(null=True, verbose_name="正确时提示词")

    class Meta:
        db_table = 'bee_django_course_section_question'
        ordering = ['order_by']
        permissions = (
            ('view_sectionquestion', '可以查看问题列表'),
        )

    # 添加选项
    def add_options(self, count=1):
        # 单选 或多选
        if int(self.question_type) == 1 or int(self.question_type) == 2:
            new_options = []
            for i in range(1, count + 1):
                option = SectionQuestionOption()
                option.question = self
                option.option = '选项' + i.__str__()
                option.order_by = i
                option.save()
                self.options.add(option)
                new_options.append(option)
            return new_options

    # 获取答题的正确答案
    def get_correct_options(self):
        return SectionQuestionOption.objects.filter(question=self, is_correct=True)

    # 获取【无】正确答案的问题
    @classmethod
    def get_has_correct_questions(cls, has_correct=False):
        if has_correct:
            return cls.objects.filter(options__is_correct=True)
        else:
            return cls.objects.exclude(options__is_correct=True)


class SectionQuestionOption(models.Model):
    question = models.ForeignKey(SectionQuestion, verbose_name='问题')
    option = models.CharField(max_length=180, verbose_name='选项')
    order_by = models.IntegerField(default=0, verbose_name='顺序')
    is_correct = models.BooleanField(default=False, verbose_name='是否正确答案')

    class Meta:
        app_label = "bee_django_course"
        db_table = 'bee_django_course_section_question_option'
        ordering = ['order_by']


# 每添加一个问题，自动创建选项
@receiver(post_save, sender=SectionQuestion)
def create_user(sender, **kwargs):
    section_question = kwargs['instance']
    if kwargs['created']:
        section_question.add_options(3)


class UserQuestionAnswerRecord(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL)  # 学生
    question = models.ForeignKey(SectionQuestion)  # 问题
    answer = models.ForeignKey(SectionQuestionOption)  # 答案
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'bee_django_course_user_question_answer_record'
        app_label = 'bee_django_course'
        ordering = ['-created_at']

    def __unicode__(self):
        return ("UserQuestionAnswerRecord->user:" + self.user.username + ",question:" + self.question.question)

    @classmethod
    def get_user_question_answer_options(cls, question, user):
        return cls.objects.filter(question=question, user=user)
        # answer_option_list = []
        # for record in records:
        #     option_id_list.append(record.answer)
        # return SectionQuestionOption.objects.filter(id__in=option_id_list)


class UserLive(models.Model):
    provider_name = models.CharField(max_length=180, default=u'cc')  # 平台商
    cc_user_id = models.CharField(max_length=180, null=True)  # CC账号
    room_id = models.CharField(max_length=180, null=True)  # 直播间ID
    live_id = models.CharField(max_length=180, null=True)  # 直播ID
    stop_status = models.CharField(max_length=180, null=True)  # 直播结束状态，10：正常结束，20：非正常结束
    record_status = models.CharField(max_length=180, null=True)  # 直播录制状态，10：录制成功，20：录制失败，30：直播过长
    record_video_id = models.CharField(max_length=180, null=True)  # 录制视频ID（如果录制成功，则返回该参数）
    replay_url = models.CharField(max_length=180, null=True)  # 直播回放地址（如果录制成功，则返回该参数）
    start_time = models.DateTimeField(null=True)  # 直播开始时间
    end_time = models.DateTimeField(null=True)  # 直播结束时间
    user = models.ForeignKey(settings.AUTH_USER_MODEL)  # 学生
    duration = models.IntegerField(null=True)  # 秒
    record_video_duration = models.IntegerField(null=True)  # 秒 返回的视频时间
    status = models.IntegerField(default=1, null=True)  # 状态 1-正常，2-正常（删除视频），-1：删除 -2 删除（删除视频）
    created_at = models.DateTimeField(auto_now_add=True)
    call_count = models.IntegerField(default=1)  # 回调了几次
    coin_multiple = models.IntegerField(default=0)  # 加了几倍M币
    is_star = models.BooleanField(default=False)  # 是否标星
    is_certify = models.BooleanField(default=False)  # 是否是认证视频
    # ucs = models.ForeignKey('bee_django_course.UserCourseSection',null=True,blank=True) # 目前仅认证用
    is_mentor_view = models.BooleanField(default=False)  # 助教是否观看
    view_mentor_id = models.IntegerField(null=True)  # 观看的助教id，检查用，可删除

    class Meta:
        db_table = 'bee_django_course_user_live'
        app_label = 'bee_django_course'
        ordering = ['-created_at']
        verbose_name = 'course学生录播'
        permissions = (
            ('view_all_userlives', '可以查看所有学生的录播'),
            ('view_teach_userlives', '可以查看所教的学生的录播'),
            ('view_child_userlives', '可以查看亲子学生的录播'),
            ('view_expired_userlives', '可以查看超过指定时间的录播'),
        )

    def __unicode__(self):
        return ("UserLive->id:" + self.pk.__str__())

    # 获取开始时间的筛选条件
    @classmethod
    def get_start_time_filter(cls, scope=None, offset=None):
        if scope in ["day", 'week', "month"]:
            start_dt, end_dt = get_datetime_with_scope_offset(scope, offset)
            return Q(start_time__range=[start_dt, end_dt])
        else:
            return None

    def get_duration_str(self, format_str=None):
        if not self.duration:
            return 0
        # print(type(seconds))
        # seconds=int(seconds)
        hour = self.duration / 3600
        min = (self.duration - hour * 3600) / 60
        second = (self.duration - hour * 3600 - min * 60)

        if not format_str:
            return '%02d:%02d:%02d' % (hour, min, second)

        elif format_str == 'min':
            return '%s' % (hour * 60 + min)

        return

    @classmethod
    # 获取某[些]学生的：直播分钟数，直播次数，直播天数，助教观看次数，观看天数
    def get_user_live_report(cls, user_list, start_dt, end_dt):
        user_live_list = cls.objects.filter(user__in=user_list, status__in=[1, 2])
        if start_dt:
            user_live_list = user_live_list.filter(start_time__gte=start_dt)
        if end_dt:
            user_live_list = user_live_list.filter(start_time__lt=end_dt)
        if not user_live_list.exists():
            return 0, 0, 0, 0, 0
        # 分钟数
        user_live_mins_res = user_live_list.aggregate(Sum("duration"))
        if user_live_mins_res["duration__sum"]:
            mins = user_live_mins_res["duration__sum"] / 60
        else:
            mins = 0
        # 次数
        user_live_count_res = user_live_list.aggregate(Count("id"))
        if user_live_count_res["id__count"]:
            count = user_live_count_res["id__count"]
        else:
            count = 0
        # 练习天数
        user_live_days_res = user_live_list.annotate(day=TruncDay('start_time', tzinfo=LOCAL_TIMEZONE)).values(
            'day').annotate(count=Count('id'), total=Sum('duration')).values('day', 'count', 'total').order_by('day')
        days = user_live_days_res.count()
        # 助教观看次数
        mentor_view_list = user_live_list.filter(is_mentor_view=True)
        mentor_view_count = mentor_view_list.count()
        # 助教观看天数
        mentor_view_days_res = mentor_view_list.annotate(day=TruncDay('start_time', tzinfo=LOCAL_TIMEZONE)).values(
            'day').annotate(count=Count('id'), total=Sum('duration')).values('day', 'count', 'total').order_by('day')
        mentor_view_days = mentor_view_days_res.count()
        return mins, count, days, mentor_view_count, mentor_view_days

    # 获取某[些]学生的直播分钟数，直播次数，助教观看次数 准备弃用，改用get_user_live_report
    @classmethod
    def get_user_live_detail(cls, user_list, scope=None, offset=None):
        user_live_list = cls.objects.filter(user__in=user_list, status__in=[1, 2])
        q = cls.get_start_time_filter(scope, offset)
        if q:
            user_live_list = user_live_list.filter(q)
        # if start_dt:
        #     user_live_list=user_live_list.filter(start_time__gte=start_dt)
        # if end_dt:
        #     user_live_list=user_live_list.filter(start_time__lt=end_dt)
        if not user_live_list.exists():
            return 0, 0, 0
        # 分钟数
        user_live_mins_res = user_live_list.aggregate(Sum("duration"))
        if user_live_mins_res["duration__sum"]:
            mins = user_live_mins_res["duration__sum"] / 60
        else:
            mins = 0
        # 次数
        user_live_count_res = user_live_list.aggregate(Count("id"))
        if user_live_count_res["id__count"]:
            count = user_live_count_res["id__count"]
        else:
            count = 0

        mentor_view_list = user_live_list.filter(is_mentor_view=True)
        mentor_view_count = mentor_view_list.count()
        return mins, count, mentor_view_count

    # 检查学员的助教是否点评了此次录播
    def get_mentor_comments_status(self):
        user_profile = self.user.userprofile
        if user_profile:
            user_class = self.user.userprofile.user_class
            if user_class:
                mentor = user_class.assistant
                if mentor:
                    mentor_comments = self.userlivecomment_set.filter(user=mentor)
                    if mentor_comments.exists():
                        return True
                    else:
                        return False
                else:
                    return False
            else:
                return False
        else:
            return False

    # 助教评论了学生的几个录播数
    @classmethod
    def get_mentor_comment_count(cls, user, start_dt=None, end_dt=None):
        user_live_list = cls.objects.filter(user=user, status__in=[1, 2])
        if start_dt:
            user_live_list = user_live_list.filter(start_time__gte=start_dt)
        if end_dt:
            user_live_list = user_live_list.filter(start_time__lt=end_dt)
        mentor = User.get_assistant()
        if not mentor:
            return 0
        if not user_live_list.exists():
            return 0

        user_live_list = user_live_list.filter(userlivecomment__user=mentor)
        if start_dt:
            user_live_list = user_live_list.filter(userlivecomment__submit_date__gte=start_dt)
        if end_dt:
            user_live_list = user_live_list.filter(userlivecomment__submit_date__lt=end_dt)
        return user_live_list.count()


class UserLiveComment(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name='作者')
    user_live = models.ForeignKey(UserLive)
    comment = models.TextField(verbose_name='评论')
    submit_date = models.DateTimeField(verbose_name='提交日期', default=timezone.now, db_index=True)


# 课件info中富文本的图片
class UserImage(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, blank=True)
    image = models.ImageField(verbose_name='图片', upload_to='course/%Y/%m/%d')
    upload_at = models.DateTimeField(verbose_name='上传时间', auto_now_add=True)

    class Meta:
        db_table = 'bee_django_course_user_image'


class UserCourse(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL)
    course = models.ForeignKey(Course, verbose_name='课程')
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(default=0, verbose_name='状态')  # 0 学习中，1 已完成
    passed_at = models.DateTimeField(null=True, blank=True)

    class Meta:
        db_table = 'bee_django_course_user_course'
        permissions = [
            ('assign_user_course', '能给学生分配课程'),
        ]

    def get_pass(self):
        self.status = 1
        self.passed_at = timezone.now()
        self.save()
        user_course_changed.send(sender=self.__class__, user_course=self, status=1)

    # 打卡统计
    def get_user_course_punch_count(self):
        course = self.course
        count = 0
        created_at = self.created_at
        # 按天打卡
        if course.punch_period == 1:
            sql = '''
            select count(*)from(select start_time::date as m from "public".bee_django_course_user_live where user_id = %s and start_time >= %s union select question_passed_at::date as m from "public".bee_django_course_user_course_section where user_course_id = %s and question_passed_at >= %s union select upload_at::date as m from "public".bee_django_course_user_assignment_image where user_course_section_id in (select id from "public".bee_django_course_user_course_section where user_course_id = %s) and upload_at >= %s union select created_at::date as m from "public".bee_django_course_user_assignment where user_course_section_id in (select id from "public".bee_django_course_user_course_section where user_course_id = %s) and created_at >= %s) as a where a.m >= %s and a.m <= %s;
            '''
            with connection.cursor() as cursor:
                cursor.execute(sql, [self.user.id, created_at, self.id, created_at, self.id, created_at, self.id,
                                     created_at, created_at.strftime('%Y-%m-%d'),
                                     (self.passed_at or timezone.now()).strftime('%Y-%m-%d')])
                row = cursor.fetchone()
                count = row[0]
            if count > course.punch_duration:
                count = course.punch_duration
        # 按周打卡
        if course.punch_period == 7:
            pass
        return count


class UserCourseSection(models.Model):
    user_course = models.ForeignKey(UserCourse)
    section = models.ForeignKey(Section)
    created_at = models.DateTimeField(auto_now_add=True)
    learned_at = models.DateTimeField(verbose_name='开始学习时间', blank=True, null=True)
    passed_at = models.DateTimeField(verbose_name='课件通过时间', blank=True, null=True)
    status = models.IntegerField(default=0)  # 0 未开始， 1 学习中，2 通过，3 退回重修（删除）, 4 提交（删除）
    score = models.IntegerField(blank=True, null=True, verbose_name='得分')
    work_time = models.IntegerField(verbose_name='总共练习时间',
                                    null=True, blank=True, default=0)  # 学生总共练习时间
    minus_live_mins = models.IntegerField(verbose_name='扣减的时间', default=0)
    teacher_add_mins = models.IntegerField(verbose_name='助教增加的练习时间', null=True, blank=True)
    teacher_add_at = models.DateTimeField(verbose_name='助教操作时间', null=True, blank=True)
    send_message_at = models.DateTimeField(verbose_name='给助教发消息时间', null=True, blank=True)
    comment = models.TextField(null=True, blank=True, verbose_name='评语')  # 弃用
    question_passed = models.BooleanField(default=False)
    question_passed_at = models.DateTimeField(null=True, blank=True)

    # 准备弃用
    updated_at = models.DateTimeField(default=timezone.now)

    class Meta:
        db_table = 'bee_django_course_user_course_section'
        ordering = ['-created_at']
        verbose_name = 'course学生课件'
        permissions = [
            ('view_all_usercoursesection', '查看所有学生课件'),
            ('view_teach_usercoursessection', '查看所教的学生课件'),
            ('view_child_usercoursesection', '查看亲子学生课件'),
            ('pass_ucs_super', '能无条件通过学生课件'),
            ('pass_ucs', '能通过学生课件'),  # 达到要求后才能通过
            ('close_ucs', '能关闭学生课件'),
            ('open_ucs', '能开启学生课件'),
            ('minus_live_mins', '能扣减学生直播时长'),
            ('review_ucs', '能查看学生作业'),
            ('score_ucs', '能给学生作业评分'),
        ]

    def close(self):
        self.status = 0
        self.work_time = 0
        self.score = 0
        self.comment = None
        self.updated_at = timezone.now()
        self.save()

    def has_user_finished_this_video(self, video_id):
        check_list = UserCourseSectionVideo.objects.filter(user_course_section=self, video_id=video_id)
        if check_list.exists():
            return True
        else:
            return False

    def pass_check(self, check_certify=True):
        section = self.section

        # 找到最近通过的UCS，检查在指定的间隔天数里，是否有通过的课程
        if section.pass_cooldown != 0:
            latest_passed_ucs = UserCourseSection.objects.filter(user_course=self.user_course, status=2).order_by(
                '-passed_at')
            if latest_passed_ucs.exists():
                pass_date = latest_passed_ucs.first().passed_at
                if not pass_date:
                    return False
                timedelta = (timezone.now().date() - pass_date.date()).days
                if timedelta < section.pass_cooldown:
                    return False

        if section.has_imagework:
            image_count = self.userassignmentimage_set.count()
            if image_count < section.image_count_req:
                return False

        if section.has_videowork:
            if self.work_time - self.minus_live_mins < section.video_length_req + self.teacher_add_mins:
                return False

        if section.has_questionwork:
            if not self.question_passed:
                return False

        if section.has_to_finish_course_video:
            return self.check_video_watch_status()

        if section.has_textwork:
            if not self.userassignment_set.exists():
                return False

        if check_certify:
            if not self.check_certify_pass() == True:
                return False

        # 所有检查条件都通过，才可自动通过
        return True

    def auto_pass_check(self):
        if not self.section.auto_pass:
            return False

        return self.pass_check(check_certify=True)

    def open_ucs(self):
        # 如果课件为自动通过 先检查是否满足通过条件
        rc = self.auto_pass_check()

        if rc:
            self.get_pass()
        else:
            self.status = 1
            self.learned_at = timezone.now()
            self.updated_at = timezone.now()
            self.save()

    def is_learning(self):
        return self.status == 1

    def is_passed(self):
        return self.status == 2

    def is_rejected(self):
        return self.status == 3

    def is_submit(self):
        return self.status == 4

    def be_submit(self):
        self.updated_at = timezone.now()
        self.save()

    def is_tip(self):
        if self.section.type == 1:
            return True
        else:
            return False

    @transaction.atomic
    def get_pass(self, score=0, comment=None):
        if self.status == 2:  # 避免重复操作
            return

        self.score = score
        self.comment = comment
        if not self.learned_at:
            self.learned_at = timezone.now()
        self.passed_at = timezone.now()
        self.updated_at = timezone.now()
        self.status = 2
        self.save()

        # 发送通过的信号
        ucs_passed.send(sender=UserCourseSection, user_course_section=self)

        # 检查是否还有其他开启的课程
        learning_ucs = self.user_course.usercoursesection_set.filter(status=1)
        if learning_ucs.count() == 0:
            # 自动开启下一课
            next_section = self.next_section()
            if next_section:
                next_section.open_ucs()
            else:
                self.user_course.get_pass()  # 所有课程都通过了，则此课学习完成，通过

    @transaction.atomic
    def reject(self):
        self.score = None
        self.updated_at = timezone.now()
        self.comment = None
        self.status = 3
        self.save()

    def update_work_time(self, minutes):
        if not self.work_time:
            self.work_time = 0
        self.work_time += minutes
        self.save()

        # 检查是否可以自动通过
        rc = self.auto_pass_check()
        if rc:
            self.get_pass()

    # 如果有直播需要，则计算时间倍数，给各个项目独立使用
    # 1倍：发消息 2倍：发邮件
    def get_time_multiple(self):
        if not self.section.has_videowork:
            return 0
        work_time = self.work_time - self.minus_live_mins
        req_time = self.section.video_length_req
        if req_time > 0:
            return work_time / req_time
        else:
            return 0

    def next_section(self, is_open=False):
        order_sets = CourseSectionMid.objects.filter(course=self.user_course.course,
                                                     section=self.section)
        if order_sets.exists():
            order = order_sets.first().order_by
            mids = CourseSectionMid.objects.filter(course=self.user_course.course, order_by__gt=order)
            if mids.exists():
                mid = mids.first()
                if is_open:
                    ucs = UserCourseSection.objects.filter(user_course=self.user_course,
                                                           status__in=[1, 2, 3, 4],
                                                           section=mid.section)
                else:
                    ucs = UserCourseSection.objects.filter(user_course=self.user_course, section=mid.section)
                if ucs.exists():
                    return ucs.first()
                else:
                    return None
            else:
                return None
        else:
            return None

    def get_section_mid_prename(self):
        try:
            mid = CourseSectionMid.objects.get(course=self.user_course.course, section=self.section)
            return mid.pre_name
        except:
            return None

    def get_section_mid_points(self):
        try:
            mid = CourseSectionMid.objects.get(course=self.user_course.course, section=self.section)
            return mid.points
        except:
            return 0

    # 获取学生已通过的课件
    @classmethod
    def get_user_pass_sections(cls, user_course):
        return cls.objects.filter(user_course=user_course, status=2)

    # 获取某时间段内学生学的最后一个课件
    @classmethod
    def get_user_last_course_section(cls, user, start_dt=None, end_dt=None):
        ucs_list = cls.objects.filter(user_course__user=user).order_by('-updated_at')
        if ucs_list.exists():
            if start_dt:
                ucs_list = ucs_list.filter(updated_at__gte=start_dt)
            if end_dt:
                ucs_list = ucs_list.filter(updated_at__lte=end_dt)
            list = ucs_list.filter(status=1)
            if list.exists():
                return list.first()
            else:
                finished = ucs_list.filter(status__in=[2, 4])
                if finished.exists():
                    return finished.first()
                else:
                    return None
        else:
            return None

    def get_section_name(self):
        return self.section.name

    def get_course_name(self):
        return self.user_course.course.name

    def get_punch(self):
        return self.user_course.get_user_course_punch_count()

    def get_course_punch(self):
        return self.user_course.course.punch_duration

    def get_assignment_img_count(self):
        return self.userassignmentimage_set.count()

    def check_video_watch_status(self):
        for e in self.section.sectionvideo_set.all():
            if not self.has_user_finished_this_video(e.video.id):
                return False
        return True

    def is_open_certify(self):
        if not self.section.need_certify:
            return False
        if not self.is_learning():
            return False
        records = self.usercertifyrecord_set.filter(status__in=[0, 1, 2])
        if records.exists():
            return False
        # 其他要求的检查
        r = self.pass_check(check_certify=False)
        if not r:
            return False
        return True

    # 认证
    def do_certify(self, userlive=None):
        if not userlive:
            return
        if not self.section.need_certify:
            return
        records = self.usercertifyrecord_set.filter(status=0)
        if records.exists():
            record = records.first()
        else:
            return
        userlive.is_certify = True
        userlive.save()
        record._submit(userlive)

        return

    # 检查认证是否通过
    def check_certify_pass(self):
        if not self.section.need_certify:
            return True
        records = self.usercertifyrecord_set.filter(status=2)
        if records.exists():
            return True
        return False


# 记录用户是否看过课件的某个视频
# 主要给用户看完视频是否自动通过进行判断
class UserCourseSectionVideo(models.Model):
    user_course_section = models.ForeignKey(UserCourseSection)
    video = models.ForeignKey(Video)
    finish_at = models.DateTimeField(default=timezone.now)


class UserAssignment(models.Model):
    user_course_section = models.ForeignKey(UserCourseSection)
    content = models.TextField(verbose_name='正文', null=True, blank=True)  # 文字作业
    created_at = models.DateTimeField(auto_now_add=True)
    score = models.IntegerField(blank=True, null=True, verbose_name='得分')

    class Meta:
        permissions = (
            ('can_review', 'can review'),
        )
        db_table = 'bee_django_course_user_assignment'

    def submit(self):
        self.status = 1
        self.submit_at = timezone.now()
        self.save()

    def reject(self):
        self.status = 2
        self.rejected_at = timezone.now()
        self.save()


# 删除原图，用压缩的图片代替
class UserAssignmentImage(models.Model):
    user_course_section = models.ForeignKey(UserCourseSection, null=True, blank=True)
    image = models.ImageField(verbose_name='图片作业', upload_to='assignments/%Y/%m/%d')
    upload_at = models.DateTimeField(verbose_name='上传时间', auto_now_add=True)

    class Meta:
        db_table = 'bee_django_course_user_assignment_image'


@receiver(post_save, sender=UserAssignmentImage)
def resize_assignment_image_handler(sender, **kwargs):
    assignment_image = kwargs['instance']
    if kwargs['created']:
        resize_assignment_image(assignment_image.image)


class Preference(models.Model):
    how_to_pass = models.IntegerField(verbose_name='课程通过模式', default=0)  # 0 自动， 1 手动


class UserCertifyRecord(models.Model):
    user_course_section = models.ForeignKey(UserCourseSection)
    status = models.IntegerField(verbose_name='状态', choices=((0, '未提交'), (1, '已提交'), (2, '通过'), (3, '驳回'), (4, '关闭'),),
                                 default=0)  # 0 未提交，1 已提交，2 通过，3 驳回，4 关闭(重新录制认证）
    created_at = models.DateTimeField(auto_now_add=True)
    operator = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name='操作者', null=True, blank=True)
    operated_at = models.DateTimeField(null=True, blank=True, verbose_name='操作时间')
    detail = DictField(verbose_name="添加时的详细数据", null=True, blank=True)
    user_live = models.ForeignKey(UserLive, null=True, blank=True)

    class Meta:
        app_label = 'bee_django_course'
        db_table = 'bee_django_course_user_certify_record'
        ordering = ["-id"]

    def get_status(self):
        if self.status == 0:
            return '已开启，未提交'
        elif self.status == 1:
            return '已提交，待认证'
        elif self.status == 2:
            return '已通过'
        elif self.status == 3:
            return '未通过'
        elif self.status == 4:
            return '已关闭'
        else:
            return ''

    @classmethod
    def _create(cls, ucs):
        section = ucs.section
        detail = {}
        # TODO
        if section.has_videowork:
            detail["live_mins"] = ucs.work_time
        cls.objects.create(user_course_section=ucs, status=0, detail=detail)
        return

    def _submit(self, userlive=None):
        self.user_live = userlive
        self.status = 1
        self.save()
        rc = self.user_course_section.auto_pass_check()
        if rc:
            self.user_course_section.get_pass()
        user_certify_update_status.send(sender=self.__class__, user_certify=self, status="submit")

    def _pass(self, operator=None):
        self.status = 2
        self.operator = operator
        self.operated_at = timezone.now()
        self.save()
        # 检查是否可以自动通过
        rc = self.user_course_section.auto_pass_check()
        if rc:
            self.user_course_section.get_pass()
        return

    def _reject(self, operator=None):
        self.status = 3
        self.operator = operator
        self.operated_at = timezone.now()
        if self.user_course_section.section.has_videowork:
            live_mins = self.detail["live_mins"]  # 学生提交时已练时间
            self.user_course_section.teacher_add_mins = live_mins
            self.user_course_section.save()
        self.save()

    def _close(self, operator=None):
        self.status = 4
        self.operator = operator
        self.operated_at = timezone.now()
        self.save()
