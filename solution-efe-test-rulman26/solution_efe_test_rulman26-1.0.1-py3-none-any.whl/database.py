import pymysql
import os
class Connection():
    def __init__(self):
        host = os.getenv('DATABASE_HOST',"internal.mysql.tismart.com")
        user = os.getenv('DATABASE_USER',"efdev")
        port = os.getenv('DATABASE_PORT',3306)
        password = os.getenv('DATABASE_PASSWORD',"Ex3cut1v3+")
        db = os.getenv('DATABASE_NAME',"executiveforumv2")
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