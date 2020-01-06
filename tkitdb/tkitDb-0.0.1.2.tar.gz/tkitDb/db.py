from unqlite import UnQLite
# db = UnQLite('data.db') # Create an in-memory database.
import os
import ast
# sqlitedict==1.6.0
# class Sdb:
#     """
#     基于SQLite3的简单封装
#     """
import plyvel
import json
from tqdm import tqdm

class LDB:
    """
    数据库
    plyvel
    https://plyvel.readthedocs.io/
    Plyvel is a fast and feature-rich Python interface to LevelDB.
    
    """
    def __init__(self,path="tmp/lv.db",prefix="default"):

        self.rootdb = plyvel.DB(path, create_if_missing=True)
        #默认加载 default
        self.load(prefix)
    def __del__(self):
       self.rootdb.close()
       del self.rootdb
    def load(self,prefix):
        """
        切换表前缀 类似表功能
        """
        prefix=self.tobytes(prefix)
        self.db = self.rootdb.prefixed_db(prefix)
        pass
    def tobytes(self,data):
        """
        数据转化为bytes
        """
        tp=type(data)
        # print(tp)
        if tp==str:
            return  str.encode(data)
        elif tp==dict:
            return self.dict_bytes(data)
        else:
            return data
    def str_dict(self,data):
        """
        字符串转化为字典
        """
        data = json.loads(data)
        return data


    def dict_bytes(self,odict):
        """
        字典转化为bytes
        """
        # user_dict = {'name': 'dinesh', 'code': 'dr-01'}
        user_encode_data = json.dumps(odict, indent=2).encode('utf-8')
        return user_encode_data
    def put(self,key,value):
        """
        添加数据
        """
        key=self.tobytes(key)
        value=self.tobytes(value)
        self.db.put(key,value)
    def put_data(self,data):
        """
        批量保存
        data格式 
        data=[('key','dddd')]
        """
        wb = self.db.write_batch()

        for key,value in tqdm(data):
            self.put(key,value)
            pass #
        wb.write()
    def decode(self,data):
        return bytes.decode(data)
    def get(self,key):
        """
        获取数据
        """
        # with db.snapshot() as sn:
        key=self.tobytes(key)
        # value=self.tobytes(value)
        value=self.db.get(key)
        # print(type(bytes.decode(value)))
        return bytes.decode(value)
    def get_sn(self,key):
        """
        获取数据
        """
        with db.snapshot() as sn:
            key=self.tobytes(key)
            value=sn.get(key)
            return bytes.decode(value)
    def get_all(self):
        #         遍历键范围
        # 通过提供start和/或stop参数可以限制希望迭代器迭代的值的范围：

        # >>> for key, value in db.iterator(start=b'key-2', stop=b'key-4'):
        # ...     print(key)
        # ...
        # key-2
        # key-3
        # start和stop参数的任何组合都是可能的。例如，要从特定的开始键进行迭代直到数据库结束：

        # >>> for key, value in db.iterator(start=b'key-3'):
        # ...     print(key)
        # ...
        for key,value in self.db.iterator():
            # print(key)
            yield bytes.decode(key),self.get(key)
    def delete(self,key):
        """
        删除数据
        """
        key=self.tobytes(key)
        return self.db.delete(key)








class Db:
    """
    基于UnQLite的nosql数据存贮
    """
    def __init__(self,dbpath='data.db'):
        # UnQLite.__init__(self,dbpath)
        self.db= UnQLite(dbpath)
        self.dbpath=dbpath
    def __del__(self):
        self.db.close()
    def add(self,key,value):
        """
        添加数据
        key ='2eas'
        value={}
        """
        self.db[key]=value
        # print('222')
    def reload(self):
        self.db= UnQLite(self.dbpath)
        pass

    def get(self,key):
        """
        获取数据
        自动转换成字典

        """
        
        # print('value',value)
        try:
            value=str(self.db[key],"utf-8")
            value=ast.literal_eval(value)
        except:
            return None
            pass
        return value
    def get_all(self):
        with self.db.cursor() as cursor:
            for key, value in cursor:
                yield key, self.get(key)

    def delete(self,key):
        """
        删除数据
        """
        # del self.db[key]
        self.db.delete(key)
    def col(self,key):
        self.col = self.db.collection(key)
        self.col.create()  # Create the collection if it does not exist.
        self.col.exists()
        return self.col

    # def col_add(self,value):
    #     self.col.store(value)
    # def col_all(self):
    #    return self.col.all()


