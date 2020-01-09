# -*- coding: utf-8 -*-
import sys
import os
curPath = os.path.abspath(os.path.dirname(__file__))
sys.path.append(curPath)
import redis

class RedisTools(object):
    def __init__(self,ip='127.0.0.1',db_num=1,port=6379):
        self.con = redis.Redis(
            host=ip,
            port=port,
            db=db_num,
            decode_responses=True  # 设置为True返回的数据格式就是str类型
        )

    def get_all_keys(self):
        '''查看所有的key'''
        return self.con.keys('*')

    def set_key(self,key,value):
        return self.con.set(key,value)

    def get_key(self,key):
        return self.con.get(key)

    def append_key(self,key,value):
        return self.con.append(key,value)

    def del_key(self,key_name):
        '''删除key，返回删除的个数'''
        return self.con.delete(key_name)




