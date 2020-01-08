# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import os, requests, json, random, datetime
from django.db import transaction
from django.shortcuts import HttpResponse
from django.conf import settings
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import authenticate
from dss.Serializer import serializer
from django.http import JsonResponse
from django.utils import timezone
from django.views.generic import ListView, DetailView, TemplateView
from dss.Mixin import MultipleJsonResponseMixin, JsonResponseMixin, FormJsonResponseMixin
from django.contrib.auth import authenticate
from django.contrib.auth import get_user_model

from .models import WXUser, CampaignRecord, BargainRecord, PreUser
from .utils import LOCAL_TIMEZONE, create_wxapp_qrcode, encode, decode, check_bargain_create

JSCODE2SESSION_URL = 'https://api.weixin.qq.com/sns/jscode2session?grant_type=authorization_code'
# APPID = "wxcb508410e0530d63"
# APPSECRET = "1eb1e52b42e36f3baa2a9ef0158e6597"
User = get_user_model()


def test(request):
    import requests
    import os

    pid = os.fork()
    if pid == 0:
        a = requests.post('http://127.0.0.1:8000/crm/wxapp/a')

    else:
        b = requests.post('http://127.0.0.1:8000/crm/wxapp/a')

    # os._exit(0)
    return


@csrf_exempt
@transaction.atomic
def a(request):
    z = BargainRecord.objects.filter(op_wxuser_id=16, campaign_record_id=35)
    if z.exists():
        print ("error1")
    try:
        BargainRecord.objects.create(op_wxuser_id=16, campaign_record_id=35, result=11,
                                     wx_nickname="aaa", wx_avatar_url="http://aaa")
        print ("ok")
    except:
        print ("error2")
    return JsonResponse(data={
        'errCode': 0,
        'errMsg': "成功",
    })


def login(request):
    code = request.GET.get('code')
    source_mkuser_id = request.GET.get('source_mkuser_id')
    campaign_record_id = request.GET.get('campaign_record_id')
    appid = settings.WEIXINAPP_GIFT_CONFIG.appid
    app_secret = settings.WEIXINAPP_GIFT_CONFIG.app_secret
    url = JSCODE2SESSION_URL + '&appid=' + appid + '&secret=' + app_secret + '&js_code=' + code
    # login(request, user)
    r = requests.get(url).json()
    open_id = r['openid']
    wxuser, is_create = WXUser.objects.get_or_create(open_id=open_id)
    if is_create:
        if source_mkuser_id:
            user = User.objects.get(id=source_mkuser_id)
            wxuser.user = user
            wxuser.save()
        elif campaign_record_id:
            campaign = CampaignRecord.objects.get(id=campaign_record_id)
            wxuser.user = campaign.wxuser.user
            wxuser.save()
    wxuser_token = encode(wxuser.pk.__str__())
    return JsonResponse(data={
        'errCode': 0,
        "wxuser_token": wxuser_token,
        'wxuser': wxuser.to_json(),
        'errMsg': "成功",
    })


#
# def share_image(request,reward_id):
#     print ("init", hasattr(settings, "a"))
#     print ("init", hasattr(settings, "REFERRAL_QRCODE_PRE_URL"))
#     print ("share_image")
#     try:
#         from bee_django_message.models import WeixinServiceAccessToken
#     except Exception as e:
#         return HttpResponse(e)
#     token = WeixinServiceAccessToken.get_token(2)
#     url="https://api.weixin.qq.com/wxa/getwxacodeunlimit?access_token="+token
#     res = api_post(url,{"page":"pages/index/index","scene":"a=1"})
#     try:
#         _dict = json.loads(res)
#         print _dict
#         if hasattr(_dict,'errcode'):
#             print ('error')
#             return
#     except:
#         pass
#     from .utils import merge_img
# error, msg, img = merge_img(referral_base_path=os.path.join(settings.BASE_DIR,'bee_django_crm','static',"bee_django_crm",'img','preuser_done.jpg'),
#                             qrcode_img=res, qrcode_pos=(0, 0),
#                             qrcode_size=(200, 200))
# print error,msg,img
# if img:
#     response = HttpResponse(content_type='image/jpg')
#     img.save(response, "JPEG")
#     return response

# dir = os.path.join(settings.BASE_DIR,'media','crm')
# if not os.path.exists(dir):
#     os.makedirs(dir)
# with open(os.path.join(settings.BASE_DIR,dir,'bb.jpg'),"wb") as f:
#     f.write(res)
#
# return


def campaign_my_detail(request, wxuser_id, reward_id):
    campaign_records = CampaignRecord.objects.filter(wxuser_id=wxuser_id, reward_id=reward_id)
    if campaign_records.exists():
        campaign_info = campaign_records.first().to_json()
    else:
        campaign_info = None
    return JsonResponse(data={
        'errCode': 0,
        "campaign_info": campaign_info,
        'errMsg': "成功",
    })


class CampaignRecordDetail(JsonResponseMixin, DetailView):
    model = CampaignRecord
    datetime_type = 'string'
    pk_url_kwarg = 'pk'

    def get_object(self, queryset=None):
        campaign_record = CampaignRecord.objects.get(id=self.kwargs["pk"])
        # 补充分享图
        if not campaign_record.share_qrcode:
            img_dir = os.path.join(settings.BASE_DIR, 'media', "bee_django_crm", "gift", "campaign_record",
                                   "share_qrcode")
            img_name = campaign_record.pk.__str__() + ".jpg"
            errcode, errmsg, image = create_wxapp_qrcode(
                parameters={"page": "pages/index/index", "scene": "0_" + campaign_record.id.__str__()},
                img_dir=img_dir, img_name=img_name)
            if errcode == 0:
                campaign_record.share_qrcode = 'bee_django_crm/gift/campaign_record/share_qrcode/' + img_name
                campaign_record.save()
        campaign_record.add_wxuser()
        campaign_record.add_bind_name()
        return campaign_record


@csrf_exempt
def campaign_record_create(request):
    # class CampaignRecordCreate(TemplateView):

    # def post(self, request, *args, **kwargs):
    wxuser_id = request.POST.get("wxuser_id")
    reward_id = request.POST.get("reward_id")
    user_info = request.POST.get("user_info")
    try:
        wxuser = WXUser.objects.get(id=wxuser_id)
    except:
        return JsonResponse(data={
            'errCode': 1,
            'errMsg': '参数错误'
        })

    record, is_create = CampaignRecord.objects.get_or_create(wxuser=wxuser, reward_id=reward_id)

    # 更新微信信息
    try:
        user_dict = json.loads(user_info)
        wxuser = WXUser.objects.get(id=record.wxuser_id)
        wxuser.update_wx_info(user_dict)
    except Exception as e:
        print (e)
        pass

    if is_create == True:
        #  生成分享二维码
        try:
            img_dir = os.path.join(settings.BASE_DIR, 'media', "bee_django_crm", "gift", "campaign_record", "share_qrcode")
            img_name = record.pk.__str__() + ".jpg"
            errcode, errmsg, image = create_wxapp_qrcode(
                parameters={"page": "pages/index/index", "scene": "0_" + record.id.__str__()},
                img_dir=img_dir, img_name=img_name)
            if errcode == 0:
                record.share_qrcode = 'bee_django_crm/gift/campaign_record/share_qrcode/' + img_name
                record.save()
        except:
            pass
        # 自己先砍一刀
        # 添加前检查
        errcode, errmsg, r = check_bargain_create(record, wxuser)
        if errcode == 0:
            try:
                bargain_result = BargainRecord.objects.create(op_wxuser=wxuser, campaign_record=record, result=r,
                                                              wx_nickname=wxuser.nickname,
                                                              wx_avatar_url=wxuser.avatar_url)
            except:
                pass

    return JsonResponse(data={
        'errCode': 0,
        "campaign_info": record.to_json(),
        'errMsg': "成功",
    })


@csrf_exempt
def campaign_bind_user(request):
    campaign_id = request.POST.get("campaign_id")
    username = request.POST.get("username")
    password = request.POST.get("password")
    name = request.POST.get("name")
    try:
        campaign = CampaignRecord.objects.get(id=campaign_id)
    except:
        return JsonResponse(data={
            'errCode': 1,
            'errMsg': "参数错误",
        })
    if campaign.bind_user or campaign.bind_preuser:
        return JsonResponse(data={
            'errCode': 2,
            'errMsg': "已绑定过账号"
        })
    # user = authenticate(username=username, password=password)
    user = WXUser.get_bind_user(username=username,password=password,name=name)
    if user is None:
        return JsonResponse(data={
            'errCode': 4,
            'errMsg': "输入的信息有误"
        })

    records = CampaignRecord.objects.filter(bind_user=user)
    if records.exists():
        return JsonResponse(data={
            'errCode': 5,
            'errMsg': "该用户已绑定过"
        })
    campaign.bind_user = user
    campaign.is_mk = True
    campaign.save()
    return JsonResponse(data={
        'errCode': 0,
        'errMsg': "成功"
    })


@csrf_exempt
def campaign_bind_preuser(request):
    campaign_id = request.POST.get("campaign_id")
    name = request.POST.get("name")
    tel = request.POST.get("tel")
    source_id = request.POST.get("source_id")
    # referral_user_id = request.POST.get("source_mkuser_id")

    try:
        campaign = CampaignRecord.objects.get(id=campaign_id)
    except:
        return JsonResponse(data={
            'errCode': 1,
            'errMsg': "参数错误",
        })
    if campaign.bind_user or campaign.bind_preuser:
        return JsonResponse(data={
            'errCode': 2,
            'errMsg': "已绑定过账号"
        })
    try:
        user = campaign.wxuser.user
    except:
        user = None
    preuser = PreUser.objects.create(nickname=name, name=name, mobile=tel, source_id=source_id, referral_user1=user,
                                     level=1)
    campaign.bind_preuser = preuser
    campaign.is_mk = False

    campaign.save()
    return JsonResponse(data={
        'errCode': 0,
        'errMsg': "成功"
    })


class BargainList(MultipleJsonResponseMixin, ListView):
    model = BargainRecord
    query_set = None
    paginate_by = 100
    datetime_type = 'string'

    def get_queryset(self):
        campaign_id = self.kwargs["campaign_id"]
        bargain_list = BargainRecord.objects.filter(campaign_record_id=campaign_id)
        map(self.rename, bargain_list)
        # map(self.add_attr, bargain_list)
        return bargain_list

    def rename(self, bargain_record):
        bargain_record.re_name()

    def add_attr(self, bargain_record):
        bargain_record.add_wxuser()
        # wxuser = WXUser.objects.get(id=bargain_record.op_wxuser_id)
        # wxuser_dict={"nickname":wxuser.nickname}
        # setattr(bargain_record, 'op_wxuser_info', wxuser_dict)


class BargainRecordDetail(JsonResponseMixin, DetailView):
    model = BargainRecord
    datetime_type = 'string'
    pk_url_kwarg = 'pk'

    # def get_object(self, queryset=None):
    #     bargain_record = BargainRecord.objects.get(id=self.kwargs["pk"])
    #     bargain_record.add_wxuser()
    #     return campaign_record


@csrf_exempt
def bargain_record_create(request):
    wxuser_id = request.POST.get("wxuser_id")
    wxuser_token = request.POST.get("wxuser_token")
    campaign_id = request.POST.get("campaign_id")
    user_info = request.POST.get("user_info")

    try:
        campaign = CampaignRecord.objects.get(id=campaign_id)
    except:
        return JsonResponse(data={
            'errCode': 1,
            'errMsg': "参数错误"
        })

    try:
        op_wxuser = WXUser.objects.get(id=wxuser_id)
    except:
        return JsonResponse(data={
            'errCode': 1,
            'errMsg': "参数错误"
        })

    try:
        id_str = decode(wxuser_token)
    except:
        return JsonResponse(data={
            'errCode': 6,
            'errMsg': "token错误"
        })
    if not id_str == wxuser_id.__str__():
        return JsonResponse(data={
            'errCode': 6,
            'errMsg': "token错误"
        })

    # 添加前检查
    errcode, errmsg, r = check_bargain_create(campaign, op_wxuser)
    if not errcode == 0:
        return JsonResponse(data={
            'errCode': errcode,
            'errMsg': errmsg
        })

    user_dict = json.loads(user_info)
    try:
        bargain_result = BargainRecord.objects.create(op_wxuser_id=wxuser_id, campaign_record=campaign, result=r,
                                                      wx_nickname=user_dict["nickName"],
                                                      wx_avatar_url=user_dict["avatarUrl"])
    except:
        return JsonResponse(data={
            'errCode': 8,
            'errMsg': "错误"
        })
    # 更新微信信息
    try:
        wxuser = WXUser.objects.get(id=wxuser_id)
        wxuser.update_wx_info(user_dict)
    except Exception as e:
        print (e)
        pass
    return JsonResponse(data={
        'errCode': 0,
        "bargain_result": r,
        'errMsg': "成功",
    })
