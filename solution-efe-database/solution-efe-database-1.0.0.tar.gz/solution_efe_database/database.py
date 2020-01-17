import pymysql
from solution_efe_config import configConstants
DATABASE_HOST=configConstants.MYSQL['host']
DATABASE_PORT=configConstants.MYSQL['port']
DATABASE_USER=configConstants.MYSQL['user']
DATABASE_PASSWORD=configConstants.MYSQL['password']
DATABASE_NAME=configConstants.MYSQL['name']

class Connection():
    def __init__(self):
        host = DATABASE_HOST
        port = DATABASE_PORT
        user = DATABASE_USER
        password = DATABASE_PASSWORD
        db = DATABASE_NAME
        self.con = pymysql.connect(host=host,port=port,user=user,password=password,db= db,charset='utf8mb4',cursorclass=pymysql.cursors.DictCursor)
        self.cur = self.con.cursor()

    def queryfetchall(self, query):
        try:
            self.cur.execute(query)
            result = self.cur.fetchall()
            return {'status': True,'data':result}
        except Exception as e:
            return {'status': False,'data':str(e)}

    def queryfetchone(self, query):
        try:
            self.cur.execute(query)
            result=self.cur.fetchone()
            return {'status': True, 'data': result}
        except Exception as e:
            return {'status': False,'data':str(e)}

    def queryUpdate(self,query):
        try:
            self.cur.execute(query)
            self.con.commit()
            return {'status':True,'data':'Query Success'}
        except Exception as e:
            return {'status': False,'data':str(e)}

    def close(self):
        self.cur.close()
        self.con.close()