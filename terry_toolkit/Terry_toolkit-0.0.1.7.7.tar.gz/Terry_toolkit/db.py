from unqlite import UnQLite
# db = UnQLite('data.db') # Create an in-memory database.

import ast
class Db:
    """
    基于UnQLite的nosql数据存贮
    """
    def __init__(self,dbpath='data.db'):
        # UnQLite.__init__(self,dbpath)
        self.db= UnQLite(dbpath)
    def add(self,key,value):
        """
        添加数据
        key ='2eas'
        value={}
        """
        self.db[key]=value
        # print('222')
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
            return []
            pass
        return value
    def delete(self,key):
        """
        删除数据
        """
        del self.db[key]
    def col(self,key):
        self.col = self.db.collection(key)
        self.col.create()  # Create the collection if it does not exist.
        self.col.exists()
        return self.col

    # def col_add(self,value):
    #     self.col.store(value)
    # def col_all(self):
    #    return self.col.all()


