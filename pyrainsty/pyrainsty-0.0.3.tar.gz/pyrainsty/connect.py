#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
@author: rainsty
@file:   connect.py
@time:   2019-12-29 10:06:29
@description: connect data source
"""

import pymysql


class MysqlConnect(object):
    """
    example:
        from pyrainsty import connect
        config = dict(
            host='127.0.0.1',
            port=3306,
            user='root',
            password='123456',
            database='test',
            charset='utf8'
        )

        mc = connect.MysqlConnect(config)
        mc.create_connect()
        state, result = mc.get_sql_data('select * from test.test limit 1')
        if not state:
            print(result)

        print(result)
    """

    def __init__(self, config, **kwargs):
        self.__config = config
        self.__kwargs = kwargs
        self.__conn = None
        self.__cursor = None

    @property
    def get_conn(self):
        return self.__conn

    @property
    def get_cursor(self):
        return self.__cursor

    def create_connect(self):
        self.__conn = pymysql.Connection(**self.__config, **self.__kwargs)
        self.__cursor = self.__conn.cursor()

    def check_connect(self):
        try:
            self.__conn.ping()
        except AttributeError as e:
            del e
            self.create_connect()

    def close_connect(self):
        self.__cursor.close()
        self.__conn.close()
        self.__cursor = None
        self.__conn = None

    def __del__(self):
        self.close_connect()

    def get_sql_data(self, sql, params=None):
        try:
            self.check_connect()
            if params:
                self.__cursor.execute(sql, params)
            else:
                self.__cursor.execute(sql)

            _data = self.__cursor.fetchall()
            _column = self.__cursor.description

            _list = []
            for d in _data:
                _dict = {}
                for i in range(len(d)):
                    _dict[_column[i][0]] = d[i]
                if _dict:
                    _list.append(_dict)

            return True, _list
        except BaseException as e:
            return False, e

    def exec_sql_cmd(self, sql, params=None):
        try:
            self.check_connect()
            if params:
                self.__cursor.execute(sql, params)
            else:
                self.__cursor.execute(sql)

            return True, None
        except BaseException as e:
            return False, e
