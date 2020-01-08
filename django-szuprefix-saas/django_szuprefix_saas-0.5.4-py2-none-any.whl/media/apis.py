# -*- coding:utf-8 -*-
from __future__ import division, unicode_literals
from django_szuprefix.api.mixins import UserApiMixin
from django_szuprefix_saas.saas.mixins import PartyMixin
from .apps import Config
from rest_framework.response import Response

__author__ = 'denishuang'
from . import models, serializers
from rest_framework import viewsets, decorators
from django_szuprefix.api.helper import register


class VideoViewSet(PartyMixin, UserApiMixin, viewsets.ModelViewSet):
    queryset = models.Video.objects.all()
    serializer_class = serializers.VideoSerializer
    search_fields = ('name',)
    filter_fields = {
        'id': ['in', 'exact'],
        'is_active': ['exact'],
        'owner_type': ['exact'],
        'owner_id': ['exact', 'in'],
    }
    ordering_fields = ('is_active', 'name', 'create_time', 'owner_type')

    @decorators.list_route(['POST'])
    def batch_active(self, request):
        rows = self.filter_queryset(self.get_queryset()) \
            .filter(id__in=request.data.get('id__in', [])) \
            .update(is_active=request.data.get('is_active', True))
        return Response({'rows': rows})

    @decorators.list_route(['GET', 'POST'])
    def signature(self, request):
        from xyz_qcloud.vod import gen_signature
        return Response({'signature': gen_signature(extra_params="procedure=流畅")})


register(Config.label, 'video', VideoViewSet)
