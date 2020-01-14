import os
import sqlite3
import datetime
from sqlite3 import Error
import time

from Spitzer.result import result
from Spitzer.print import print_warning, print_error

class Export():

    conn = None
    cursor = None

    def __init__(self, path):
        info = result.get_hosts()
        self.create_connection(path)
        if self.conn is None:
            print_error('Connection failed!')
            return

        self.cursor = self.conn.cursor()
        self.create_table()
        self.add_info(info)

        self.conn.commit()
        self.cursor.close()
        self.conn.close()

    def create_connection(self, path):
        try:
            if not os.path.isfile(path):
                print_warning('DB file does not exsist, creating...')
            self.conn = sqlite3.connect(path)
        except Error as e:
            print_error(e)
        

    def create_table(self):

        date = datetime.datetime.today().strftime('%d_%m_%Y')

        query = ''' CREATE TABLE IF NOT EXISTS scan_{} (
                    id integer PRIMARY KEY,
                    ip text NOT NULL,
                    port integer NOT NULL,
                    service text,
                    version text
                ); '''.format(date)

        self.execute_sql(query)

    def add_info(self, info):
        date = datetime.datetime.today().strftime('%d_%m_%Y')

        query = ''' INSERT INTO scan_{}(ip,port,service,version)
                    VALUES(?,?,?,?) '''.format(date)

        print(info)
        for host in info:
            for port in info[host]:
                service = info[host][port][1]
                if service == '':
                    service = info[host][port][0]

                task = (host, port, service, info[host][port][2])
                self.execute_sql(query, task)    

    def execute_sql(self, query, task=None):
        try:
            if task is None:
                self.cursor.execute(query)
            else:
                self.cursor.execute(query, task)
            self.conn.commit()
        except Error as e:
            print_error(e)
    