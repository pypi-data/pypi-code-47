import psycopg2

from django_init.db.base import DatabaseBase

"""
config = {
    'dbname': 'postgres',
    'user': 'root',
    'password': 'root',
    'host': 'localhost',
}
"""


class DatabasePostgreSQL(DatabaseBase):
    client = psycopg2

    sql_show_dbs = "SELECT * FROM pg_database"
    sql_create_db = "CREATE DATABASE %s WITH OWNER = %s"

    def connect(self):
        try:
            self.conn = self.client.connect(**self.config)
            self.conn.autocommit = True
            self.cursor = self.conn.cursor()
        except Exception as e:
            print(e)
        else:
            print(self.msg_connect)

    def create_db(self, db_name):
        user = self.config.get('user')
        sql = self.sql_create_db % (db_name, user)
        try:
            self.cursor.execute(sql)
        except Exception as e:
            print(e)
        else:
            print(self.msg_create_db % db_name)
