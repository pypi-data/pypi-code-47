import MySQLdb

from django_init.db.base import DatabaseBase

config = {
    'host': 'localhost',
    'user': 'root',
    'passwd': 'root',
}


class DatabaseMySQL(DatabaseBase):
    client = MySQLdb
