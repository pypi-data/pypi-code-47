import os
import yaml
import pymysql

def get_config(path):
    return yaml.load(open(path).read())

def create_connection(path):
    config = get_config(path)
    connection = pymysql.connect(host=config['host'],
                                 user=config['user'],
                                 password=config['password'])
    return connection

if __name__ == '__main__':
    connection = create_connection()
    connection.close()
