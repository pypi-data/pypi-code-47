#!/usr/bin/env python
# -*- coding:utf-8 -*-

from django.conf import settings

# 微信公众号
class WeixinService():
    token='Manxuetang'
    appid = 'wxd9c89c4c644961ff'
    app_secret = '66d12e8d8696f461ea866739b1a905fc'

    class Template():
        bind = "udMZmNX3qcu5CBT1Q2GxW0KozvcfPAXjb_ZkRIkdEfQ"  # to all：绑定通知
        course_up_req = 'hjv8iLMzlUtLSeZw495jDG01FsgaWvofCAoyI6H0fHc'  # to助教：提醒事项-到达要求
        course_pass = 'TLtYaznjdQOAWJHFWF0BmnsicJn-2UFyS0fy0I4vgQI'  # to学生：课程通过提醒

# CRM中砍价小程序 文暄社
class WEIXINAPP_GIFT():
    appid = 'wxc0a58ce74b898212'
    app_secret = '64de157ddadeca2e45ee0ea32c676f8e'

# 邮件配置
class Email():
    backend = 'django.core.mail.backends.smtp.EmailBackend'
    use_tls = True
    host = 'smtp.exmail.qq.com' # SMTP地址
    port = 587 # SMTP端口
    host_user = 'zhangyue@zhenpuedu.com'
    host_password = 'Pbu883' #邮箱密码
    subject_prefix = '[缦学堂]'
    default_from_emial= '958206195@qq.com'
    server_email= '958206195@qq.com'  # The email address that error messages come from, such as those sent to ADMINS and MANAGERS.
    admins = (('bee', '958206195@qq.com'))


def init_settings():
    # 初始化
    # 微信公众号
    if hasattr(settings,"MESSAGE_WEIXIN_SERVICE") and settings.MESSAGE_WEIXIN_SERVICE==True:
        settings.WEIXIN_SERVICE_CONFIG=WeixinService()
    # crm中微信砍价小程序
    if hasattr(settings,"MESSAGE_WEIXINAPP_GIFT") and settings.MESSAGE_WEIXINAPP_GIFT==True:
        settings.WEIXINAPP_GIFT_CONFIG=WEIXINAPP_GIFT()
    # 邮件配置
    if hasattr(settings,"MESSAGE_EMAIL") and settings.MESSAGE_EMAIL==True:
        settings.EMAIL_CONFIG=Email