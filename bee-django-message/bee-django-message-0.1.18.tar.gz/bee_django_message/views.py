#!/usr/bin/env python
# -*- coding:utf-8 -*-
from __future__ import unicode_literals

import json
from django.utils import timezone
from django.shortcuts import render, reverse, redirect
from django.core.urlresolvers import reverse_lazy
from django.utils.decorators import method_decorator
from django.contrib.auth import get_user_model
from django.core.mail import EmailMultiAlternatives
from django.conf import settings
from xml.etree import ElementTree
from django.views.decorators.csrf import csrf_exempt

from .decorators import cls_decorator, func_decorator
from django.views.generic import ListView, DetailView, TemplateView
from django.db.models import Q, Sum, Count
from django.http import HttpResponse
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Message, SendRecord, WeixinService
from .forms import MessageForm, RecordChangeDoneForm, RecordSearchForm, SendRecordForm
from .utils import get_user_name, JSONResponse
from .weixin import check_signature, receiveText, receiveEvent
from .exports import send_message
from .signals import send_message_signal

User = get_user_model()


# Create your views here.
# =======course=======
def test(request):
    from exports import send_message
    from django.contrib.auth.models import User
    user = User.objects.all().first()
    res = send_message(to_user=None, from_user=user, message_identity='course_alert', title='test', url=None)
    print(res)
    return HttpResponse('OK')


@method_decorator(cls_decorator(cls_name='MessageList'), name='dispatch')
class MessageList(ListView):
    template_name = 'bee_django_message/message/message_list.html'
    context_object_name = 'message_list'
    paginate_by = 20
    queryset = Message.objects.all()


@method_decorator(cls_decorator(cls_name='MessageDetail'), name='dispatch')
class MessageDetail(DetailView):
    model = Message
    template_name = 'bee_django_message/message/message_detail.html'
    context_object_name = 'message'


@method_decorator(cls_decorator(cls_name='MessageCreate'), name='dispatch')
class MessageCreate(CreateView):
    model = Message
    form_class = MessageForm
    template_name = 'bee_django_message/message/message_form.html'


@method_decorator(cls_decorator(cls_name='MessageUpdate'), name='dispatch')
class MessageUpdate(UpdateView):
    model = Message
    form_class = MessageForm
    template_name = 'bee_django_message/message/message_form.html'


@method_decorator(cls_decorator(cls_name='MessageDelete'), name='dispatch')
class MessageDelete(DeleteView):
    model = Message
    success_url = reverse_lazy('bee_django_message:message_list')

    def get(self, request, *args, **kwargs):
        return self.http_method_not_allowed(request, *args, **kwargs)


# 后台显示消息记录
class RecordList(ListView):
    template_name = 'bee_django_message/record/message_record_list.html'
    context_object_name = 'record_list'
    paginate_by = 20
    queryset = None

    def get_message(self):
        message_id = self.kwargs["message_id"]
        if message_id in [0, '0', None]:
            return None
        message = Message.objects.get(id=message_id)
        return message

    def search(self):
        is_done = self.request.GET.get("is_done")
        has_from_user = self.request.GET.get("has_from_user")
        message = self.get_message()
        self.queryset = SendRecord.objects.filter(message=message)

        is_done_value = None
        if not is_done in ["0", 0, None, ""]:
            if is_done in [1, "1"]:
                is_done_value = True
            elif is_done in [-1, "-1"]:
                is_done_value = False
            self.queryset = self.queryset.filter(is_done=is_done_value)
        if not has_from_user in ["0", 0, None, ""]:
            self.queryset = self.queryset.filter(from_user__isnull=False)
        return self.queryset

    def get_queryset(self):
        return self.search()

    def get_context_data(self, **kwargs):
        context = super(RecordList, self).get_context_data(**kwargs)
        message = self.get_message()
        is_done = self.request.GET.get("is_done")
        context['message'] = message
        context['search_form'] = RecordSearchForm({"is_done": is_done})
        return context


class RecordDetail(DetailView):
    model = SendRecord
    template_name = 'bee_django_message/record/record_detail.html'
    context_object_name = 'record'


class RecordCreate(CreateView):
    model = SendRecord
    form_class = SendRecordForm
    template_name = 'bee_django_message/record/record_create.html'

    def form_valid(self, form):
        form.instance.from_user = self.request.user
        return super(RecordCreate, self).form_valid(form)

    def get_success_url(self):
        return reverse_lazy('bee_django_message:record_list', kwargs={"message_id": 0}) + "?has_from_user=1"


class RecordCustomDetail(RecordDetail):
    template_name = 'bee_django_message/record/record_custom_detail.html'


# 修改后台显示的消息
class RecordUpdate(UpdateView):
    model = SendRecord
    form_class = RecordChangeDoneForm
    template_name = 'bee_django_message/record/record_change_done.html'

    def get_success_url(self):
        return reverse_lazy('bee_django_message:record_detail', kwargs=self.kwargs)

    def get_context_data(self, **kwargs):
        record = SendRecord.objects.get(id=self.kwargs["pk"])
        context = super(RecordUpdate, self).get_context_data(**kwargs)
        context['record'] = record
        return context

    def form_valid(self, form):
        record = form.instance
        record.is_done = True
        record.done_at = timezone.now()
        record.done_by = self.request.user
        if record.message.need_reply:
            send_message(to_user=record.from_user, title=record.get_reply_title(), info=record.get_reply_info())
        return super(RecordUpdate, self).form_valid(form)


# 发送记录
@method_decorator(cls_decorator(cls_name='UserRecordList'), name='dispatch')
class CustomUserRecordList(ListView):
    template_name = 'bee_django_message/record/custom_user_record_list.html'
    context_object_name = 'record_list'
    paginate_by = 20
    queryset = None

    def get_user(self):
        user_id = self.kwargs["user_id"]
        if user_id in [None, "0"]:
            return None
        user = User.objects.get(id=user_id)
        return user

    def get_queryset(self):
        user = self.get_user()
        self.queryset = SendRecord.objects.filter(to_user=user)
        return self.queryset

    def get_context_data(self, **kwargs):
        user = self.get_user()
        context = super(CustomUserRecordList, self).get_context_data(**kwargs)
        context['user'] = user
        return context


@method_decorator(cls_decorator(cls_name='UserRecordClick'), name='dispatch')
class UserRecordClick(TemplateView):
    def post(self, request, *args, **kwargs):
        record_id = request.POST.get("record_id")
        record = SendRecord.objects.get(id=record_id)
        record.is_view = True
        record.save()
        return JSONResponse(json.dumps({"url": record.url}, ensure_ascii=False))


class UserRecordAllClick(TemplateView):
    def post(self, request, *args, **kwargs):
        user_id = request.POST.get("user_id")
        try:
            user = User.objects.get(id=user_id)
            pass
        except:
            res = {"error": 1, "message": "参数错误"}
            return JSONResponse(json.dumps(res, ensure_ascii=False))
        record_list = SendRecord.objects.filter(to_user=user, is_view=False)
        for record in record_list:
            record.is_view = True
            record.save()
        res = {"error": 0, "message": "操作成功"}
        return JSONResponse(json.dumps(res, ensure_ascii=False))


# 微信
@csrf_exempt
def serve(request):
    if request.method == 'GET':
        response = HttpResponse(check_signature(request))
        return response
    else:
        # 消息处理
        xml_str = request.body
        xml = ElementTree.fromstring(xml_str)
        msg_type = xml.find('MsgType').text
        if msg_type == 'text':
            # 文本消息
            responseStr = receiveText(xml)
        elif msg_type == 'event':
            # 事件消息
            responseStr = receiveEvent(xml)
        else:
            responseStr = ""

        return HttpResponse(responseStr)


@csrf_exempt
def send_wx_message(request):
    keyword = request.POST.get("keyword")
    subject = request.POST.get("subject")
    date = request.POST.get("date")
    remark = request.POST.get("remark")
    url = request.POST.get("url")
    open_id = request.POST.get("open_id")
    template_identity = request.POST.get("template_identity")

    res = WeixinService.send_wx_message(
        template_identity=template_identity,
        openId=open_id,
        first=keyword,
        keyword1=subject,
        keyword2=date,
        remark=remark,
        url=url
    )
    return JSONResponse(json.dumps(res, ensure_ascii=False))
