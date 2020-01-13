import sys

from tabulate import tabulate


class Databases:
    def connect(self):
        raise NotImplementedError('%s class must provide a %s() method' %
                                  (self.__class__.__name__, sys._getframe().f_code.co_name))

    def disconnect(self):
        raise NotImplementedError('%s class must provide a %s() method' %
                                  (self.__class__.__name__, sys._getframe().f_code.co_name))

    def show_dbs(self):
        raise NotImplementedError('%s class must provide a %s() method' %
                                  (self.__class__.__name__, sys._getframe().f_code.co_name))

    def create_db(self, db_name):
        raise NotImplementedError('%s class must provide a %s() method' %
                                  (self.__class__.__name__, sys._getframe().f_code.co_name))

    def drop_db(self, db_name):
        raise NotImplementedError('%s class must provide a %s() method' %
                                  (self.__class__.__name__, sys._getframe().f_code.co_name))


class DatabaseBase(Databases):
    client = None
    conn = None
    cursor = None

    msg_connect = 'Connected successfully'
    msg_create_db = 'Database %s created successfully'
    msg_drop_db = 'Database %s dropped successfully'
    msg_disconnect = 'Disconnected successfully'

    sql_show_dbs = "SHOW DATABASES"
    sql_create_db = "CREATE DATABASE %s DEFAULT CHARACTER SET utf8 DEFAULT COLLATE utf8_general_ci"
    sql_drop_db = "DROP database %s"

    def __init__(self):
        self.connect()

    def __del__(self):
        self.disconnect()

    def connect(self):
        try:
            self.conn = self.client.connect(**config)
            self.cursor = self.conn.cursor()
        except Exception as e:
            print(e)
        else:
            print(self.msg_connect)

    def disconnect(self):
        try:
            self.cursor.close()
            self.conn.close()
        except Exception as e:
            print(e)
        else:
            print(self.msg_disconnect)

    def show_dbs(self):
        sql = self.sql_show_dbs
        try:
            self.cursor.execute(sql)
            data = self.cursor.fetchall()
            table = tabulate(data, headers=['DATABASE'])
        except Exception as e:
            print(e)
        else:
            print(table)

    def create_db(self, db_name):
        sql = self.sql_create_db % db_name
        try:
            self.cursor.execute(sql)
        except Exception as e:
            print(e)
        else:
            print(self.msg_create_db % db_name)

    def drop_db(self, db_name):
        sql = self.sql_drop_db % db_name
        try:
            self.cursor.execute(sql)
        except Exception as e:
            print(e)
        else:
            print(self.msg_drop_db % db_name)
