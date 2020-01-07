#!/usr/bin/env python
# -*- coding:utf-8 -*-

__author__ = 'zhangyue'

# Create your models here.
import os, csv, random, json, requests, datetime, pytz
from datetime import timedelta
from django.db import models, transaction
from django.db.models import Sum
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User
from django.conf import settings
from smart_selects.db_fields import ChainedForeignKey
from django.core.files.storage import FileSystemStorage
from dss.Serializer import serializer
from django.utils import timezone
from bee_django_richtext.custom_fields import RichTextField

LOCAL_TIMEZONE = pytz.timezone('Asia/Shanghai')
# 性别
PREUSER_GENDER_CHOICES = ((1, '男'), (2, '女'))
# 意向
PREUSER_GRADE_CHOICES = ((0, '无'), (1, '弱'), (2, '强'))
# 申请表的问题类型
APPLICATION_QUESTION_INPUT_TYPE_CHOICES = ((1, '输入框'), (2, '单选（圆钮）'), (3, '单选（下拉）'), (4, "多选（方钮）"))
# 级别
PREUSER_LEVEL_CHOICES = ((0, '全部'), (1, '小白'), (2, '申请'), (3, '缴费'), (4, '课程卡'))
# 合同周期
CONTRACT_PERIOD_CHOICES = ((1, '天'), (7, '周'), (31, '月'), (9999, '长期'))
CRM_POSTER_PHOTO_PATH = "bee_django_crm/poster_photo"  # 生成海报的文件路径，前面不带/
test = ''


def get_user_table():
    return settings.AUTH_USER_MODEL


def get_user_name_field():
    if settings.USER_NAME_FIELD:
        return settings.USER_NAME_FIELD
    else:
        return settings.CRM_USER_NAME_FIELD


# 省市区联动
class Province(models.Model):
    name = models.CharField(max_length=180, null=True)

    class Meta:
        db_table = 'bee_django_crm_province'
        app_label = 'bee_django_crm'

    def __unicode__(self):
        return self.name


class City(models.Model):
    province = models.ForeignKey(Province)
    name = models.CharField(max_length=180, null=True)

    class Meta:
        db_table = 'bee_django_crm_city'
        app_label = 'bee_django_crm'

    def __unicode__(self):
        return self.name


class District(models.Model):
    city = models.ForeignKey(City)
    # city=ChainedForeignKey(City,chained_field='continent',show_all=False,auto_choose=True,sort=True)
    name = models.CharField(max_length=180, null=True)

    class Meta:
        db_table = 'bee_django_crm_district'
        app_label = 'bee_django_crm'

    def __unicode__(self):
        return self.name


PREUSER_PAY_STATUS_CHOICES = ((0, '未缴费'), (1, "全款缴清"), (2, "分期中"))


# 预备学员
class PreUser(models.Model):
    nickname = models.CharField(verbose_name='昵称', max_length=180, null=True, blank=True)  # 昵称
    name = models.CharField(verbose_name='姓名', max_length=20)  # 姓名
    mobile = models.CharField(verbose_name='电话', max_length=100)  # 手机
    gender = models.IntegerField(choices=PREUSER_GENDER_CHOICES, verbose_name='性别', null=True, blank=True,
                                 default=0)  # 性别
    wx = models.CharField(verbose_name='微信', max_length=180, null=True, blank=True)  # 微信
    birthday = models.DateField(verbose_name='出生日期', null=True, blank=True)
    province = models.ForeignKey(Province, null=True, blank=True, verbose_name='省')
    city = ChainedForeignKey(
        City,
        chained_field="province",
        chained_model_field="province",
        show_all=False,
        auto_choose=True,
        sort=True,
        null=True,
        blank=True,
        verbose_name='市')
    source = models.ForeignKey("bee_django_crm.Source", verbose_name='来源', null=True, blank=True)  # 来源
    referral_user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='bee_crm_referral_user', null=True,
                                      blank=True,
                                      verbose_name='原推荐人')  # 推荐人

    referral_user1 = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='bee_crm_referral_user1', null=True,
                                       blank=True,
                                       verbose_name='推荐人')  # 推荐人
    referral_user2 = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='bee_crm_referral_user2', null=True,
                                       blank=True,
                                       verbose_name='接引人')  # 接引人
    level = models.IntegerField(verbose_name='级别', default=1)  # 级别 1-小白，2-已申请 3-已缴费4-课程卡
    grade = models.IntegerField(verbose_name='意向', null=True, blank=True)  # 意向 1-弱 2-强

    address = models.TextField(verbose_name='地址', null=True, blank=True)

    job = models.CharField(verbose_name='工作', max_length=180, null=True, blank=True)
    email = models.CharField(verbose_name='邮箱', max_length=180, null=True, blank=True)
    hobby = models.TextField(verbose_name='爱好', null=True, blank=True)
    married = models.CharField(verbose_name='婚姻状况', max_length=180, null=True, blank=True)  # 婚否
    children = models.CharField(verbose_name='孩子状况', max_length=180, null=True, blank=True)  # 有几个孩子
    job_info = models.TextField(verbose_name='工作详情', null=True, blank=True)  # 工作详情
    family = models.TextField(verbose_name='家庭详情', null=True, blank=True)  # 家庭情况
    # 缴费记录
    contract_id = models.IntegerField(verbose_name='合同', null=True, blank=True)
    fee = models.FloatField(verbose_name='缴费金额', null=True, blank=True)
    info = models.TextField(verbose_name='备注', null=True, blank=True)
    is_add_coin = models.IntegerField(verbose_name='加缦币', default=0, null=True, blank=True)  # 0-未加缦币，1-已加缦币
    attended_date = models.DateField(verbose_name='入学日期', null=True, blank=True)  # 入学日期
    pay_datetime = models.DateField(verbose_name='缴费日期', null=True, blank=True)  # 缴费日期
    # coupon = models.ForeignKey("other.Coupon", related_name='bee_crm_preUser_coupon', null=True)  # 注册时使用的课程卡
    #
    created_at = models.DateTimeField(auto_now_add=True, null=True)  # 注册时间
    applied_at = models.DateTimeField(null=True)  # 提交申请表时间
    paid_at = models.DateTimeField(null=True)  # 缴费时间
    pay_status = models.IntegerField(default=0, choices=PREUSER_PAY_STATUS_CHOICES, verbose_name='缴费情况')

    class Meta:
        db_table = 'bee_django_crm_preuser'
        app_label = 'bee_django_crm'
        ordering = ["-created_at"]
        verbose_name = 'crm预备用户'
        permissions = (
            ('can_manage_crm', '可以进入crm管理页'),
            ('view_crm_preuser', '可以查看crm用户'),
            ('view_crm_doc', '可以查看帮助文档'),
        )

    def get_absolute_url(self):
        return reverse('bee_django_crm:preuser_detail', kwargs={'pk': self.pk})

    def get_gender(self):
        if not self.gender:
            return ""
        for g in PREUSER_GENDER_CHOICES:
            if self.gender == g[0]:
                return g[1]
        return ""

    def get_grade(self):
        if not self.grade:
            return ""
        for g in PREUSER_GRADE_CHOICES:
            if self.grade == g[0]:
                return g[1]
        return ""

    def get_pay_status(self):
        if not self.pay_status:
            return ""
        for g in PREUSER_PAY_STATUS_CHOICES:
            if self.pay_status == g[0]:
                return g[1]
        return ""

    def get_source(self):
        if not self.source:
            return ""
        return self.source.name

    def get_level(self):
        if not self.level:
            return ""
        for g in PREUSER_LEVEL_CHOICES:
            if self.level == g[0]:
                return g[1]
        return ""

    def __unicode__(self):
        return ("PreUser->name:" + self.name)

    @classmethod
    def init_pay_status(cls):
        users = cls.objects.all()
        for user in users:
            if user.level <= 2:
                user.pay_status = 0
            elif user.level == 3:
                user.pay_status = 1
            user.save()

    # 获取学号，即学生用户名
    def get_user_username(self):
        try:
            return self.userprofile.user.username
        except:
            return ''

    # 获取学生姓名
    def get_user_name(self):
        try:
            return self.userprofile.user.first_name
        except:
            return ''


class RegCode(models.Model):
    reg_number = models.IntegerField(unique=True, null=True)
    reg_name = models.CharField(max_length=180, verbose_name='注册卡号')
    reg_code = models.CharField(max_length=50, verbose_name='注册卡密')
    created_at = models.DateTimeField(default=timezone.now)
    used_at = models.DateTimeField(null=True, blank=True, verbose_name='使用日期')
    used_preuser = models.ForeignKey(PreUser, null=True, blank=True, verbose_name='被谁使用', on_delete=models.SET_NULL)
    course_days = models.IntegerField(null=True, verbose_name='可学习课程天数')

    class Meta:
        db_table = 'bee_django_crm_code'
        app_label = 'bee_django_crm'
        ordering = ["-pk"]
        permissions = (
            ('can_ckeck_code', '可以验证卡密'),
            ('can_get_code', '可以获取卡密'),
        )

    # password_str:密码中出现的字符
    # password_count：密码的位数
    # count：生成数量

    @classmethod
    @transaction.atomic
    def _generate_reg_code(cls, count=0, password_str="1234567890", password_count=10, course_days=None):
        existing_number = cls.objects.all().order_by('reg_number')
        if existing_number.exists():
            number_begin_with = existing_number.last().reg_number + 1
        else:
            number_begin_with = 1

        # csv文件
        file_dir = settings.BASE_DIR + '/media/bee_django_crm/'
        if not os.path.exists(file_dir):
            os.makedirs(file_dir)
        file_name = file_dir + timezone.localtime().strftime("%Y%m%d") + '-' + count.__str__() + ".csv"
        csvfile = open(file_name, 'w')
        writer = csv.writer(csvfile)
        writer.writerow(['number', 'password'])

        # code_list = random.sample(xrange(range_low, range_high), count)
        for code in range(0, count):
            reg_number = number_begin_with
            reg_name = '{:08d}'.format(reg_number)
            first_password_str = password_str.replace("0", '')
            first_password = random.choice(first_password_str)
            _password = cls.generator_password(password_count - 1, password_str)
            reg_code = first_password + _password
            cls.objects.create(reg_code=reg_code, reg_name=reg_name, reg_number=reg_number, course_days=course_days)
            number_begin_with += 1
            writer.writerow([reg_name, reg_code])
        csvfile.close()
        return

    @classmethod
    def generator_password(cls, size, chars):
        return ''.join(random.choice(chars) for _ in range(size))

    # # 生成随机注册码，默认6位数字
    # @classmethod
    # @transaction.atomic
    # def _generate_reg_code(cls, range_low=1000000000000001, range_high=9999999999999999, count=3200,
    #                        number_begin_with=1):
    #     try:
    #         code_list = random.sample(xrange(range_low, range_high), count)
    #         existing_number = cls.objects.order_by('reg_number')
    #         if existing_number.exists():
    #             number_begin_with = existing_number.last().reg_number + 1
    #         else:
    #             number_begin_with = number_begin_with
    #
    #         for code in code_list:
    #             reg_number = number_begin_with
    #             reg_name = '{:08d}'.format(reg_number)
    #             reg_code = code
    #             cls.objects.create(reg_code=reg_code, reg_name=reg_name, reg_number=reg_number)
    #             number_begin_with += 1
    #     except ValueError:
    #         print u'数量超出限定范围'
    #
    #     return count

    @classmethod
    def check_code(cls, reg_name, reg_code):
        code = cls.objects.get(reg_name__exact=reg_name, reg_code__exact=reg_code)

        if code.used_at or code.used_preuser:
            return code.used_preuser, code.used_at
        else:
            return None, None


# 来源
class Source(models.Model):
    name = models.CharField(max_length=60, verbose_name="来源名称")  # 名称
    reg_name = models.CharField(max_length=60, verbose_name="注册页显示名称", null=True, blank=True)  # 注册页显示名称
    created_at = models.DateTimeField(auto_now_add=True)  # 时间
    is_poster = models.BooleanField(default=False, verbose_name='是否海报类型', blank=True)
    is_show = models.BooleanField(default=False, verbose_name='编辑时是否显示', blank=True)

    # reg_unique=models.BooleanField(default=False,verbose_name='是否只能注册一次')

    class Meta:
        db_table = 'bee_django_crm_source'
        app_label = 'bee_django_crm'
        ordering = ['-created_at']
        verbose_name = 'crm渠道'
        permissions = (
            ('view_crm_source', '可以查看渠道'),
            ('can_change_source_name', '可以修改渠道名称'),
        )

    def __unicode__(self):
        return (self.name)

    def get_absolute_url(self):
        return reverse('bee_django_crm:source_list')

    def get_is_poster(self):
        if self.is_poster == True:
            return "是"
        elif self.is_poster == False:
            return "否"

    def get_show_posters(self):
        return self.poster_set.filter(is_show=True)


# 联络记录
class PreUserTrack(models.Model):
    user = models.ForeignKey("bee_django_crm.PreUser", related_name='bee_crm_track_user')  # 追踪人
    created_at = models.DateTimeField(auto_now_add=True)  # 记录时间
    tracked_at = models.DateTimeField(verbose_name='联络时间')  # 追踪时间
    info = models.TextField(verbose_name="详情")  # 详情
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, related_name='bee_crm_created_by_user')  # 操作人

    class Meta:
        db_table = 'bee_django_crm_preuser_track'
        app_label = 'bee_django_crm'

    def __unicode__(self):
        return ("PerUserTrack->info:" + self.user.name)

    def get_absolute_url(self):
        return reverse('bee_django_crm:preuser_detail', kwargs={'pk': self.user.pk})


# 申请表问题
class ApplicationQuestion(models.Model):
    name = models.CharField(max_length=180, unique=True, verbose_name='问题')  # 问题
    order_by = models.IntegerField(verbose_name='顺序')  # 顺序
    input_type = models.IntegerField(choices=APPLICATION_QUESTION_INPUT_TYPE_CHOICES, verbose_name='类型')  # 类型
    is_required = models.BooleanField(default=False, verbose_name='是否必填', help_text='只对输入框和单选有效')

    class Meta:
        db_table = 'bee_django_crm_application_question'
        app_label = 'bee_django_crm'
        ordering = ["order_by"]
        verbose_name = 'crm申请表问题'
        permissions = (
            ('view_crm_application', '可以查看申请表问题列表页'),
        )

    def __unicode__(self):
        return ("ApplicationQuestion->question:" + self.name)

    def get_absolute_url(self):
        return reverse('bee_django_crm:application_question_list')

    def get_type_name(self):
        if not self.input_type:
            return ""
        for g in APPLICATION_QUESTION_INPUT_TYPE_CHOICES:
            if self.input_type == g[0]:
                return g[1]
        return ""


# 申请表问题的选项
class ApplicationOption(models.Model):
    question = models.ForeignKey('bee_django_crm.ApplicationQuestion', verbose_name='问题')
    name = models.CharField(verbose_name='选项', max_length=180, unique=True)
    order_by = models.IntegerField(verbose_name='顺序')

    class Meta:
        db_table = 'bee_django_crm_application_options'
        app_label = 'bee_django_crm'
        ordering = ["order_by"]

    def __unicode__(self):
        return ("ApplicationOption->option:" + self.name)


# 学生填的申请表内容# 学生填的申请表内容
class PreUserApplication(models.Model):
    preuser = models.ForeignKey('bee_django_crm.PreUser', related_name='bee_crm_user_applications')
    question = models.ForeignKey('bee_django_crm.ApplicationQuestion')
    answer = models.TextField()

    class Meta:
        db_table = 'bee_django_crm_preuser_application'
        app_label = 'bee_django_crm'

    def __unicode__(self):
        return ("PreUserApplication->preuser:" + self.preuser.name)


# 合同
class Contract(models.Model):
    name = models.CharField(verbose_name='合同名称', max_length=180, unique=True)  # 合同名称
    period = models.IntegerField(verbose_name='周期')  # 月／周／天/长期
    duration = models.IntegerField(verbose_name='时长', null=True, blank=True, help_text="如【周期】为【长期】，则不用填写此字段")  # 时长
    price = models.FloatField(verbose_name='金额')  # 金额
    agreement = RichTextField(verbose_name='须知', null=True, app_name='bee_django_crm', model_name='Contract')
    type = models.IntegerField(default=1, choices=((1, "普通合同"), (2, "亲子合同")), verbose_name='合同类型')

    class Meta:
        db_table = 'bee_django_crm_contract'
        app_label = 'bee_django_crm'
        ordering = ["-id"]
        verbose_name = 'crm合同'
        permissions = (
            ('view_crm_contract', '可以查看合同'),
        )

    def __unicode__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('bee_django_crm:contract_list')

    def get_peruser(self):
        preusers = PreUser.objects.filter(preusercontract__contract=self).distinct()
        return preusers

    # 获取合同时长天数显示
    def get_contract_days(self):
        if self.period == 1:
            return self.duration.__str__() + "天"
        elif self.period == 7:
            return self.duration.__str__() + "周"
        elif self.period in [30, 31]:
            return self.duration.__str__() + "月"
        elif self.period == 9999:
            return "长期"

    def get_contract_type(self):
        if self.type == 1:
            return '普通合同'
        elif self.type == 2:
            return '亲子合同'
        return ''


# 用户的合同表
class PreUserContract(models.Model):
    preuser = models.ForeignKey('bee_django_crm.PreUser')
    contract = models.ForeignKey('bee_django_crm.Contract', verbose_name='合同')
    price = models.FloatField(verbose_name='应收金额')  # 金额
    created_at = models.DateTimeField(auto_now_add=True)

    info = models.TextField(null=True, blank=True, verbose_name='备注')
    is_user_agree = models.BooleanField(default=False, verbose_name='用户是否同意')
    study_at = models.DateTimeField(verbose_name='开课日期', null=True, blank=True)
    finish_at = models.DateTimeField(verbose_name='结课日期', null=True, blank=True)
    is_migrate = models.BooleanField(default=False)
    # is_after_check = models.IntegerField(default=False,null=True)
    paid_at = models.DateTimeField(verbose_name='缴费日期', null=True)
    is_checked = models.BooleanField(verbose_name='审核', default=False, blank=True)
    checked_at = models.DateTimeField(null=True)
    checked_by = models.ForeignKey(settings.AUTH_USER_MODEL, null=True)
    after_checked_at = models.DateTimeField(null=True)

    class Meta:
        db_table = 'bee_django_crm_preuser_contract'
        app_label = 'bee_django_crm'
        ordering = ['-created_at']
        permissions = (
            ('view_crm_preuser_contract', '可以查看用户合同'),
        )

    def __unicode__(self):
        return ("PreUserContract->name:" + self.preuser.name)

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        if not self.finish_at:
            self.finish_at = self.get_finish_at()
        return super(PreUserContract, self).save(force_insert, force_update, using,
                                                 update_fields)

    def get_finish_at(self):
        # if self.finish_at:
        #     return self.finish_at
        finish_at = None
        contract = self.contract
        if contract.period == 9999:
            finish_at = '2999-12-31 23:59:59+0800'
        else:
            days = contract.period * contract.duration
            if self.study_at:
                finish_at = self.study_at + timedelta(days=days)
        return finish_at

    def get_finish_at_str(self):
        if not self.finish_at.year >= 2999:
            return self.finish_at
        else:
            return '长期无限制'

    @classmethod
    def migrate_to_fee(cls):
        preuser_contract_list = PreUserContract.objects.filter(is_migrate=False)
        for preuser_contract in preuser_contract_list:
            preuser_fee = PreUserFee()
            preuser_fee.preuser = preuser_contract.preuser
            preuser_fee.preuser_contract = preuser_contract
            preuser_fee.price = preuser_contract.price
            preuser_fee.is_checked = preuser_contract.is_checked
            preuser_fee.checked_at = preuser_contract.checked_at
            preuser_fee.checked_by = preuser_contract.checked_by
            preuser_fee.after_checked_at = preuser_contract.after_checked_at
            preuser_fee.paid_at = preuser_contract.paid_at
            preuser_fee.study_at = preuser_contract.study_at
            preuser_fee.save()
            preuser_contract.is_migrate = True
            preuser_contract.save()


PREUSER_FEE_PAY_STATUS_CHOICES = ((1, "全款"), (2, "分期头款"), (3, "分期中"), (4, "分期尾款"))


class PreUserFee(models.Model):
    preuser = models.ForeignKey('bee_django_crm.PreUser')
    preuser_contract = models.ForeignKey(PreUserContract)
    price = models.FloatField(verbose_name='实收金额')  # 金额
    paid_at = models.DateTimeField(verbose_name='缴费日期')
    pay_status = models.IntegerField(default=1, choices=PREUSER_FEE_PAY_STATUS_CHOICES, verbose_name='付款方式及状态')
    is_checked = models.BooleanField(verbose_name='审核', default=False, blank=True)
    checked_at = models.DateTimeField(null=True)
    checked_by = models.ForeignKey(settings.AUTH_USER_MODEL, null=True,related_name='checked_by')
    after_checked_at = models.DateTimeField(null=True)
    info = models.TextField(null=True, blank=True, verbose_name='备注')
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, null=True,related_name='fee_created_by')
    created_at = models.DateTimeField(auto_now_add=True)
    # 弃用
    study_at = models.DateTimeField(verbose_name='开课日期', null=True, blank=True,
                                    help_text="【全款】及【分期头款】时，此字段必填。其他付款方式可不填写")

    class Meta:
        db_table = 'bee_django_crm_preuser_fee'
        app_label = 'bee_django_crm'
        ordering = ['-paid_at', '-created_at']
        permissions = (
            ('add_crm_preuser_fee', '可以添加用户缴费'),
            ('view_crm_preuser_fee', '可以查看用户缴费'),
            ('can_check_crm_preuser_fee', '可以审核用户缴费'),
            ('can_after_checked_fee', '审核缴费后可以后续操作'),
        )

    def __unicode__(self):
        return ("PreUserFee->name:" + self.preuser.name)

    def get_pay_status(self):
        if not self.pay_status:
            return ""
        for g in PREUSER_FEE_PAY_STATUS_CHOICES:
            if self.pay_status == g[0]:
                return g[1]
        return ""

    # 后续成功
    def after_success(self):
        self.after_checked_at = timezone.now()
        self.save()
        # fee_after_success.send(sender=PreUserFee,preuser_fee=self)


# 海报
POSTER_SHOW_CHOICES = ((1, '显示'), (0, '不显示'))


class Poster(models.Model):
    source = models.ForeignKey('bee_django_crm.Source')
    # name = models.CharField(max_length=180, verbose_name='海报名称')
    is_show = models.BooleanField(default=False, verbose_name='是否显示', blank=True)
    # is_clear = models.BooleanField(default=False, verbose_name='是否清空文件', blank=True)
    qrcode_width = models.IntegerField(verbose_name='二维码宽度', null=True, default=0)
    qrcode_height = models.IntegerField(verbose_name='二维码高度', null=True, default=0)
    qrcode_pos_x = models.IntegerField(verbose_name='二维码x轴坐标', null=True, default=0)
    qrcode_pos_y = models.IntegerField(verbose_name='二维码y轴坐标', null=True, default=0)
    qrcode_color = models.CharField(max_length=8, verbose_name='二维码颜色', default='#000000', null=True)
    photo = models.ImageField(upload_to=CRM_POSTER_PHOTO_PATH, null=True)

    class Meta:
        db_table = 'bee_django_crm_poster'
        app_label = 'bee_django_crm'

    def __unicode__(self):
        return self.source.name

    def get_temp_image(self):
        return os.path.join(CRM_POSTER_PHOTO_PATH, self.id.__str__() + '_temp.jpg')

    def get_image_count(self):
        image_dir = os.path.join(CRM_POSTER_PHOTO_PATH, self.id.__str__())
        if not os.path.exists(image_dir):
            return 0
        return len([name for name in os.listdir(image_dir) if os.path.isfile(os.path.join(image_dir, name))])

    def get_is_show(self):
        if self.is_show == True:
            return "是"
        elif self.is_show == False:
            return "否"


# =========微信砍价==========
# 微信用户
class WXUser(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, blank=True, verbose_name='来源缦客id')
    nickname = models.CharField(max_length=180, verbose_name='微信昵称', null=True)
    avatar_url = models.URLField(verbose_name='头像链接', null=True)
    gender = models.IntegerField(choices=((1, "男"), (2, "女"),), null=True, blank=True, verbose_name='微信性别')
    tel = models.CharField(max_length=20, null=True, blank=True, verbose_name='微信电话')
    city = models.CharField(max_length=20, null=True, blank=True, verbose_name='微信城市')
    province = models.CharField(max_length=20, null=True, blank=True, verbose_name='微信省份')
    country = models.CharField(max_length=20, null=True, blank=True, verbose_name='微信国家')
    open_id = models.CharField(max_length=180, verbose_name='微信openid')
    # source_mkuser_id = models.IntegerField(null=True, verbose_name='来源缦客id')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'bee_django_crm_wx_user'
        app_label = 'bee_django_crm'

    def __unicode__(self):
        if self.nickname:
            return self.nickname
        else:
            return u'匿名用户' + self.pk.__str__()

    def get_gender(self):
        if self.gender == 1:
            return "男"
        elif self.gender == 2:
            return '女'
        else:
            return ""

    def update_wx_info(self, user_dict):
        self.nickname = user_dict["nickName"]
        self.avatar_url = user_dict["avatarUrl"]
        self.gender = user_dict["gender"]
        self.city = user_dict["city"]
        self.province = user_dict["province"]
        self.country = user_dict["country"]
        self.country = user_dict["country"]
        self.save()
        return

    def to_json(self):
        result = serializer(data=self, output_type='json', datetime_format='string', include_attr=('id', "nickname"))
        result_dict = json.loads(result)
        return json.dumps(result_dict)

    @classmethod
    def get_bind_user(cls, username, password, name, kwargs=None):
        username=username.lower()
        try:
            return User.objects.get(username=username, first_name=name)
        except:
            return None

# 奖品
class BargainReward(models.Model):
    title = models.CharField(max_length=180, verbose_name='奖励名称')
    start_time = models.DateTimeField(null=True,verbose_name='活动开始时间',blank=True)
    end_time = models.DateTimeField(null=True,verbose_name='活动结束时间',blank=True)
    max_bargain = models.IntegerField(default=1,verbose_name='最大砍价次数')
    start_money= models.FloatField(verbose_name='起始金额',null=True,blank=True)
    end_money= models.FloatField(verbose_name='完成金额',null=True,blank=True)
    bargain_low = models.FloatField(verbose_name='砍价最低值',null=True,blank=True)
    bargain_high = models.FloatField(verbose_name='砍价最高值',null=True,blank=True)
    class Meta:
        db_table = 'bee_django_bargain_reward'
        app_label = 'bee_django_crm'

    def __unicode__(self):
        return self.title

    @classmethod
    def update_wxapp_qrcode(cls,file_path,user):
        return


# 参与记录
class CampaignRecord(models.Model):
    wxuser = models.ForeignKey(WXUser, verbose_name='微信用户')
    reward = models.ForeignKey(BargainReward, verbose_name='奖品')
    count = models.IntegerField(verbose_name='砍价次数', default=0)
    result = models.FloatField(verbose_name='砍价结果', default=0)
    status = models.IntegerField(choices=((1, "进行中"), (2, "已完成"), (3, "已消费"),), default=1)
    share_qrcode = models.ImageField(upload_to='bee_django_crm/gift/campaign_record/share_qrcode', null=True, blank=True,
                                     verbose_name='小程序二维码')
    created_at = models.DateTimeField(auto_now_add=True)
    bind_user = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, blank=True, verbose_name='红包发放用户账号')
    bind_preuser = models.ForeignKey(PreUser, null=True, blank=True, verbose_name='红包发放新peruser账号',on_delete=models.SET_NULL)
    is_mk = models.NullBooleanField(verbose_name='是否是老缦客',null=True)
    history = models.TextField(verbose_name='历史记录', null=True, blank=True)

    class Meta:
        unique_together = (('wxuser', 'reward'),)
        db_table = 'bee_django_crm_bargain_campaign_record'
        app_label = 'bee_django_crm'
        ordering = ["-created_at"]
        permissions = (
            ('view_campaign_record_list', 'view_campaign_record_list'),  # 查看参加活动列表
            ('view_campaign_record_detail', 'view_campaign_record_detail'),  # 查看参加活动详情页
        )

    def __unicode__(self):
        return self.pk.__str__()

    def get_status(self):
        if self.status == 1:
            return '进行中'
        elif self.status == 2:
            return '已完成'
        elif self.status == 3:
            return '已消费'
        return ''

    def add_wxuser(self):
        wxuser = WXUser.objects.get(id=self.wxuser.id)
        wxuser_dict = {"nickname": wxuser.nickname, "id": wxuser.id, "avatar_url": wxuser.avatar_url}
        setattr(self, 'wxuser_info', wxuser_dict)

    def add_bind_name(self):
        if self.bind_user:
            bind_name = self.bind_user.first_name[0] + "***"
        elif self.bind_preuser:
            bind_name = self.bind_preuser.name[0] + "***"
        else:
            bind_name = None
        setattr(self, 'bind_name', bind_name)

    def to_json(self):
        self.add_wxuser()
        self.add_bind_name()
        result = serializer(data=self, output_type='json', datetime_format='string',
                            include_attr=('id', "count", "result", "status", "wxuser_info"))
        result_dict = json.loads(result)
        return json.dumps(result_dict)

    def update_result(self):
        record_list = BargainRecord.objects.filter(campaign_record=self).aggregate(Sum('result'))
        sum = record_list["result__sum"]
        self.result = sum
        if sum >= self.reward.end_money:
            self.status = 2
        self.save()
        return

    def update_history(self, request_user_name, info=None):
        now_str = timezone.localtime(timezone=LOCAL_TIMEZONE).strftime("%Y-%m-%d %H:%M:%S")
        history = u"<p>由【" + request_user_name + u"】于【" + now_str + u"】修改"
        if info:
            history += u"：" + info
        history += "</p>"
        if self.history:
            self.history += history
        else:
            self.history = history
        self.save()



    # def create_wxapp_qrcode(self,parameters, img_dir, img_name,text=None,text_color=(255,255,0),text_pos=(0,0)):
    #     try:
    #         from bee_django_message.models import WeixinServiceAccessToken
    #     except Exception as e:
    #         return 1, e, None
    #     token = WeixinServiceAccessToken.get_token(2)
    #     url = "https://api.weixin.qq.com/wxa/getwxacodeunlimit?access_token=" + token
    #     data = json.dumps(parameters)
    #     res_data = requests.post(url=url, data=data, timeout=10, headers={'content-type': 'application/json'})
    #     if res_data.status_code == 200:
    #         res = res_data.content
    #     else:
    #         return 2, '请求失败', None
    #     try:
    #         _dict = json.loads(res)
    #         if hasattr(_dict, 'errcode'):
    #             print ('error')
    #             return 3, '请求失败', None
    #     except:
    #         pass
    #
    #     # dir = os.path.join(settings.BASE_DIR, 'media', 'campaign_record', 'share_qrcode')
    #     # name = self.pk.__str__() + '.jpg'
    #     if not os.path.exists(img_dir):
    #         os.makedirs(img_dir)
    #     from PIL import Image
    #     from PIL import ImageDraw
    #     _file = os.path.join(settings.BASE_DIR, img_dir, img_name)
    #     with open(_file, "wb") as f:
    #         f.write(res)
    #         # 添加文字
    #         if text:
    #             # 打开底版图片
    #             im1 = Image.open(_file)
    #             # 在图片上添加文字 1
    #             draw = ImageDraw.Draw(im1)
    #             draw.text(text_pos, text, text_color)
    #             draw = ImageDraw.Draw(im1)
    #             # 保存
    #             im1.save(_file)
    #             pass
    #     return 0, '', f
            # referral_img = Image.open(referral_base_path)
            # qrcode_img = qrcode_img.resize(qrcode_size, Image.ANTIALIAS)
            # referral_img.paste(qrcode_img, qrcode_pos)

    # def update_qrcode(self, url, parameters):
    #     try:
    #         from bee_django_message.models import WeixinServiceAccessToken
    #     except Exception as e:
    #         return e
    #     token = WeixinServiceAccessToken.get_token(2)
    #     url = "https://api.weixin.qq.com/wxa/getwxacodeunlimit?access_token=" + token
    #     data = json.dumps(parameters)
    #     res_data = requests.post(url=url, data=data, timeout=10, headers={'content-type': 'application/json'})
    #     if res_data.status_code == 200:
    #         return res_data.content
    #     else:
    #         return None
    #
    #     res = api_post(url, {"page": "pages/index/index", "scene": "a=1"}, )
    #     try:
    #         _dict = json.loads(res)
    #         print _dict
    #         if hasattr(_dict, 'errcode'):
    #             print ('error')
    #             return
    #     except:
    #         pass


# 砍价记录
class BargainRecord(models.Model):
    campaign_record = models.ForeignKey(CampaignRecord, verbose_name='参与记录')
    # bargain_wxuser = models.ForeignKey(WXUser,verbose_name='被助力的微信用户',related_name='bargain_wxuser')
    op_wxuser = models.ForeignKey(WXUser, verbose_name='助力的微信用户', related_name='op_wxuser')
    result = models.FloatField(verbose_name='砍价结果')
    wx_nickname = models.CharField(max_length=180, verbose_name='微信昵称', null=True)
    wx_avatar_url = models.URLField(verbose_name='头像链接', null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = (('campaign_record', 'op_wxuser'),)
        db_table = 'bee_django_crm_bargain_record'
        app_label = 'bee_django_crm'
        ordering = ["-created_at"]

    def __unicode__(self):
        return self.pk.__str__()

    def add_wxuser(self):
        wxuser = WXUser.objects.get(id=self.op_wxuser_id)
        if wxuser.nickname:
            if wxuser.nickname.__len__() <= 2:
                nickname = wxuser.nickname[0] + '*'
            else:
                nickname = wxuser.nickname[0] + '*' + wxuser.nickname[-1]
        else:
            nickname = '微信用户'
        wxuser_dict = {"nickname": nickname, "avatar_url": wxuser.avatar_url}
        setattr(self, 'op_wxuser_info', wxuser_dict)

    def re_name(self):
        if self.wx_nickname.__len__() <= 2:
            re_nickname = self.wx_nickname[0] + '***'
        else:
            re_nickname = self.wx_nickname[0] + '**' + self.wx_nickname[-1]
        setattr(self, 'wx_nickname', re_nickname)

    def to_json(self):
        self.add_wxuser()
        result = serializer(data=self, output_type='json', datetime_format='string',
                            include_attr=('id', "campaign_record_id", "result", "created_at"))
        result_dict = json.loads(result)
        return json.dumps(result_dict)

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        super(BargainRecord, self).save(force_insert, force_update, using, update_fields)
        self.campaign_record.update_result()
        return
