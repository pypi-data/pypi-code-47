# coding: utf-8
from django.conf import settings

# The jwt secret key。If this key not set or set with '',
# OPENauth will get the key from redis
OPENAUTH_JWT_SECRET = getattr(settings, 'OPENAUTH_JWT_SECRET', '')
# 企业微信统一认证平台的url，注意这个 url 在使用中，会再增加跳转地址
QYWX_LOGIN_URL = getattr(
    settings, 'QYWX_LOGIN_URL',
    'https://open.taijihuabao.com/api/openauth/qywx?next=')

# OPENAUTH_REDIS_HOST = getattr(settings, 'OPENAUTH_REDIS_HOST', 'localhost')
# OPENAUTH_REDIS_PORT = getattr(settings, 'OPENAUTH_REDIS_PORT', '6379')
# OPENAUTH_REDIS_DB = getattr(settings, 'OPENAUTH_REDIS_DB', '9')
# OPENAUTH_REDIS_PASSWORD = getattr(settings, 'OPENAUTH_REDIS_PASSWORD', '')
