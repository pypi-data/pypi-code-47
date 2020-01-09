#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'bee'
import hashlib, calendar, random
from xml.etree import ElementTree
from datetime import datetime
from django.conf import settings
from django.http import HttpResponse


def check_signature(request):
    signature = request.GET.get('signature', None)
    timestamp = request.GET.get('timestamp', None)
    nonce = request.GET.get('nonce', None)
    echostr = request.GET.get('echostr', None)
    token = settings.WEIXIN_SERVICE_CONFIG.token

    tmplist = [token, timestamp, nonce]
    tmplist.sort()
    tmpstr = "%s%s%s" % tuple(tmplist)
    tmpstr = hashlib.sha1(tmpstr).hexdigest()
    if tmpstr == signature:
        return HttpResponse(echostr)
    else:
        return HttpResponse("")


def receiveText(xml):
    openId = xml.find('FromUserName').text
    content = xml.find('Content').text
    if content == 'test':
        return transmitText(xml, '已经收到啦,发消息open id为：' + openId)
    return ""


def receiveEvent(xml):
    event = xml.find('Event').text
    if event == 'subscribe' or event == 'unsubscribe' or event == 'SCAN':
        # responseStr = weixin_menu.menuEvent(xml)
        #
        responseStr = qrcodeEvent(xml)
    elif event == 'CLICK':
        responseStr = menuEvent(xml)
    else:
        responseStr = ""
    return responseStr


def transmitText(xml, content):
    ToUserName = xml.find('FromUserName').text
    FromUserName = xml.find('ToUserName').text
    CreateTime = str(calendar.timegm(datetime.now().utctimetuple()))

    reply_xml = "<xml><ToUserName><![CDATA[%s]]></ToUserName><FromUserName><![CDATA[%s]]></FromUserName><CreateTime>%s</CreateTime><MsgType><![CDATA[text]]></MsgType><Content><![CDATA[%s]]></Content></xml>" % (
        ToUserName, FromUserName, CreateTime, content)
    return reply_xml


# ======事件========
def menuEvent(xml):
    # print('==========menuEvent===========')
    content = ""
    event = xml.find('Event').text
    openId = xml.find('FromUserName').text
    event_key = xml.find('EventKey').text
    try:
        from bee_django_user.models import UserProfile
        user_profile = UserProfile.objects.get(wxservice_openid=openId)
    except:
        user_profile = None

    if event_key == "USER_INFO":
        if user_profile:
            content = u'缦客号：MK' + user_profile.student_id.__str__() + "\n"
            content += u'姓    名：' + user_profile.user.first_name + "\n"
        else:
            content = get_bind_html(openId)
    elif event_key == "UNBIND_USER":
        if user_profile:
            user_profile.wxservice_openid = None
            user_profile.save()
            content = u'解绑成功'
        else:
            content = get_bind_html(openId)
    return transmitText(xml, content)


def qrcodeEvent(xml):
    content = ""
    event = xml.find('Event').text
    openId = xml.find('FromUserName').text
    event_key = xml.find('EventKey').text

    if event == "subscribe":
        content += "欢迎关注缦学堂在线" + "\n"
        content += get_bind_html(openId)
        if event_key:
            content += "，您的二维码参数为" + event_key[8:]
    elif event == 'SCAN':
        content += "您已经关注了本公众号，您的二维码参数为" + event_key
    elif event == 'unsubscribe':
        try:
            from bee_django_user.models import UserProfile
            user_profile = UserProfile.objects.get(wxservice_openid=openId)
            user_profile.wxservice_openid = None
            user_profile.save()
        except:
            pass
        return ""

    return transmitText(xml, content)


def get_bind_html(openid):
    return u"您还未绑定用户" + "\n" + u"<a href='https://manxuetang.com/user/wxService/user/bind?openid=" + openid + u"'>如需绑定，请点击此处</a>"
