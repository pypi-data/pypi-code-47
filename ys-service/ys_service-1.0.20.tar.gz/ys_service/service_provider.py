#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# @Time    : 2019/11/11 17:19
# @Author  : v5yangzai
# @Site    : https://github.com/v5yangzai
# @File    : service_provider.py
# @project : ys_module
# @Software: PyCharm
# @Desc    :
import json
import time
from decimal import Decimal
from datetime import datetime, timedelta
from ys_service.db_service import DBService, MongoService, MysqlService, RedisService, SqlServerService

from ys_service.http_service.mq_service import CreateMQ
from ys_service.http_service.log_service import LogCreate
from ys_service.http_service.http_service import HTTPService
from ys_service.http_service.attach_data_service import CreateAttachDataService
from ys_service.http_service.reservation_service import CreateReservation
from ys_service.http_service.config_center_service import CreateConfigCenterService
from ys_service.http_service.realtime_notice_service import CreateRealtimeNoticeService
from ys_service.http_service.web_service_client import CreateWebServiceClient
from ys_service.http_service.ys_requests import YsRequests


class ServiceProvider(object):

    def __init__(self):
        # 数据库对象
        self.db_service = DBService()
        self.http_service = HTTPService()
    @property
    def mongo_client(self) -> MongoService:
        """
        获取mongo服务
        :return:
        """
        return self.db_service.mongo_client

    @property
    def mysql_client(self) -> MysqlService:
        """
        获取mysql服务
        :return:
        """
        return self.db_service.mysql_client

    @property
    def redis_client(self) -> RedisService:
        """
        获取redis服务
        :return:
        """
        return self.db_service.redis_client

    @property
    def sql_server_client(self) -> SqlServerService:
        return self.db_service.sql_server_client

    def _strptime(self, time_str, f=None):
        """
        将时间字符串格式化为时间类型
        :param f: 时间格式
        :param time_str: 时间字符串
        :return:
        """
        if f:
            return datetime.strptime(time_str, f)

        try:
            return datetime.strptime(time_str, "%Y-%m-%d %H:%M:%S")
        except ValueError:
            pass

        try:
            return datetime.strptime(time_str, "%Y/%m/%d %H:%M:%S")
        except ValueError:
            pass

        try:
            return datetime.strptime(time_str, "%Y-%m-%d")
        except ValueError:
            pass

        try:
            return datetime.strptime(time_str, "%Y/%m/%d")
        except ValueError:
            pass

        try:
            return datetime.strptime(time_str, "%Y-%m-%d %H:%M:%S AM")
        except ValueError:
            pass

        try:
            d = datetime.strptime(time_str, "%Y/%m/%d %H:%M:%S PM")
            return d + self.timedelta(hours=12)
        except ValueError:
            pass

        try:
            return datetime.strptime(time_str, "%Y-%m-%d %H:%M:%S.%f0")
        except ValueError:
            pass

        try:
            return datetime.strptime(time_str, "%Y/%m/%d %H:%M:%S.%f0")
        except ValueError:
            pass

        try:
            return datetime.strptime(time_str, "%m/%d/%Y %H:%M:%S")
        except ValueError:
            pass

        try:
             return datetime.strptime(time_str, f"%m-%d-%y %H:%M:%S AM")
        except ValueError:
            pass

        try:
            return datetime.strptime(time_str, f"%m/%d/%y %H:%M:%S AM")
        except ValueError:
            pass

        try:
            return datetime.strptime(time_str, f"%m-%d-%y %H:%M:%S PM") + self.timedelta(hours=12)
        except ValueError:
            pass

        try:
            return datetime.strptime(time_str, f"%m/%d/%y %H:%M:%S PM") + self.timedelta(hours=12)
        except ValueError:
            pass

        try:
            return datetime.strptime(time_str, f"%Y-%m-%d %H:%M")
        except ValueError:
            pass

        try:
            return datetime.strptime(time_str, f"%Y/%m/%d %H:%M")
        except ValueError:
            pass

        try:
            return datetime.strptime(time_str, f"%Y/%m/%d %H:%M:%S")
        except ValueError:
            pass

    def strptime(self, time_str, f=None):
        return self._strptime(time_str, f) - self.timedelta(hours=8)

    @property
    def time(self):
        """
        获取
        :return:
        """
        return time

    @property
    def datetime(self):
        return datetime

    @property
    def timedelta(self):
        return timedelta

    @staticmethod
    def marshal(value):
        return json.dumps(value, ensure_ascii=False)

    @property
    def now(self):
        return datetime.utcnow()

    @property
    def local_now(self):
        return datetime.now()

    def get_three_code(self, s):
        redis = self.redis_client.connect(host="192.168.0.100", port=6379, password="O0qtw1wHPddwCC5T", db=0)
        d = redis.hget("System:BaseInfo:AirlineInfo", s)

        return json.loads(d).get("ThreeCode") if d else ""

    @staticmethod
    def parse_to_float(d):

        try:
            money = float(d)
        except ValueError:
            money = 0
        return money

    @staticmethod
    def parse_to_decimal(d):

        try:
            money = Decimal(d)
        except ValueError:
            money = Decimal(0)
        return money

    def log_factory(self):
        """
        创建日志中心对象
        :return:
        """
        return LogCreate()

    @property
    def mq_service(self):
        """
        创建mq服务对象
        :return:
        """
        print("CreateWebServiceClient",CreateWebServiceClient)
        return CreateMQ()

    @property
    def reservation_service(self):
        """
        创建预约服务对象
        :return:
        """
        return CreateReservation()

    @property
    def realtime_notice_service(self):
        """
        创建定时消息对象
        :return:
        """
        return CreateRealtimeNoticeService()

    @property
    def config_center_service(self):
        """
        创建配置中心对象
        :return:
        """
        return CreateConfigCenterService()

    @property
    def attach_data_service(self):
        """
        获取附加消息对象
        :return:
        """
        return CreateAttachDataService()

    @property
    def ws_client(self):
        """
        获取webservice client对象
        :return:
        """
        return CreateWebServiceClient()

    @property
    def ys_requests(self):
        return YsRequests
