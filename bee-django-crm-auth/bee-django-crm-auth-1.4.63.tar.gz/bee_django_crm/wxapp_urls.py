#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'bee'
from django.conf.urls import include, url
from django.contrib.auth import views as auth_views

from . import wxapp


urlpatterns = [
    url(r'^login$', wxapp.login),
    url(r'^test$', wxapp.test),
    # url(r'^share/image/(?P<reward_id>[0-9]+)$', wxapp.share_image),

    url(r'^campaign/my/detail/(?P<wxuser_id>[0-9]+)/(?P<reward_id>[0-9]+)$', wxapp.campaign_my_detail),
    url(r'^campaign/detail/(?P<pk>[0-9]+)$', wxapp.CampaignRecordDetail.as_view()),
    url(r'^campaign/create$', wxapp.campaign_record_create),
    url(r'^campaign/bind/user$', wxapp.campaign_bind_user),
    url(r'^campaign/bind/preuser$', wxapp.campaign_bind_preuser),

    url(r'^bargain/list/(?P<campaign_id>[0-9]+)$', wxapp.BargainList.as_view()),
    url(r'^bargain/detail/(?P<pk>[0-9]+)$', wxapp.BargainRecordDetail.as_view()),
    url(r'^bargain/create$', wxapp.bargain_record_create),
]
