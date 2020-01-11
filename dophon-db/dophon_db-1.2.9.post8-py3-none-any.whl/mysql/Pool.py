# coding: utf-8
#  连接
import datetime
import threading

import pymysql
from DBUtils.PooledDB import PooledDB
from dophon_logger import *

from dophon_db import properties
from dophon_db.mysql import Connection

logger = get_logger(eval(properties.log_types))

"""
连接池
author:CallMeE
date:2018-06-01
"""

logger.inject_logger(globals())

single_pool = None  # 单例模式获取连接池
cluster_pool = None  # 单例模式获取连接池

pool_action_log = {}

lock = threading.Lock()  # 全局线程锁


def record_support(f):
    def inner_method(*args, **kwargs):
        result = f(*args, **kwargs)
        obj_id = id(result)
        pool_action_log[obj_id] = datetime.datetime.now().timestamp()
        return result

    return inner_method


def record_return(f):
    def inner_method(*args, **kwargs):
        obj_id = id(args[1])
        if hasattr(properties, 'db_pool_exe_time') and getattr(properties, 'db_pool_exe_time'):
            logger.debug(
                '用时:' + (datetime.datetime.now().timestamp() - pool_action_log[obj_id]) + '毫秒'
            )
        f(*args, **kwargs)

    return inner_method


def get_pool(conn_kwargs: dict = {}):
    return get_single_pool(conn_kwargs)


def get_single_pool(conn_kwargs: dict = {}):
    global single_pool
    if single_pool:
        return single_pool
    pool = Pool()
    pool.init_pool(properties.pool_conn_num, Connection.Connection, conn_kwargs=conn_kwargs)
    single_pool = pool
    return single_pool


class Pool():
    _size = 0
    cache_conn_kwargs = {}

    _host = properties.pydc_host
    _user = properties.pydc_user
    _password = properties.pydc_password
    _database = properties.pydc_database
    _port = properties.pydc_port
    _charset = 'UTF8MB4'

    # 初始化连接池
    def init_pool(self, num: int, Conn: Connection, conn_kwargs: dict = {}):
        __host = conn_kwargs['host'] if 'host' in conn_kwargs else (
            conn_kwargs['__host'] if '__host' in conn_kwargs else self._host)
        __port = conn_kwargs['port'] if 'port' in conn_kwargs else (
            conn_kwargs['__port'] if '__port' in conn_kwargs else self._port)
        __user = conn_kwargs['user'] if 'user' in conn_kwargs else (
            conn_kwargs['__user'] if '__user' in conn_kwargs else self._user)
        __password = conn_kwargs['password'] if 'password' in conn_kwargs else (
            conn_kwargs['__password'] if '__password' in conn_kwargs else self._password)
        __database = conn_kwargs['database'] if 'database' in conn_kwargs else (
            conn_kwargs['__database'] if '__database' in conn_kwargs else self._database)
        __charset = conn_kwargs['charset'] if 'charset' in conn_kwargs else (
            conn_kwargs['__charset'] if '__charset' in conn_kwargs else self._charset)
        _pool = PooledDB(
            creator=pymysql,  # 使用链接数据库的模块
            maxconnections=6,  # 连接池允许的最大连接数，0和None表示不限制连接数
            mincached=2,  # 初始化时，链接池中至少创建的空闲的链接，0表示不创建
            maxcached=5,  # 链接池中最多闲置的链接，0和None不限制
            maxshared=3,
            # 链接池中最多共享的链接数量，0和None表示全部共享。PS: 无用，因为pymysql和MySQLdb等模块的 threadsafety都为1，所有值无论设置为多少，_maxcached永远为0，所以永远是所有链接都共享。
            blocking=True,  # 连接池中如果没有可用连接后，是否阻塞等待。True，等待；False，不等待然后报错
            maxusage=None,  # 一个链接最多被重复使用的次数，None表示无限制
            setsession=[
                f'set names {__charset}',
                f'set time_zone = \'{str(datetime.datetime.now().astimezone().timetz())[-6:]}\''
            ],
            # 开始会话前执行的命令列表。如：["set datestyle to ...", "set time zone ..."]
            ping=0,
            # ping MySQL服务端，检查是否服务可用。# 如：0 = None = never, 1 = default = whenever it is requested, 2 = when a cursor is created, 4 = when a query is executed, 7 = always
            host=__host,
            port=__port,
            user=__user,
            password=__password,
            database=__database,
        )
        # _pool = []
        # self._Conn = Conn
        # self.cache_conn_kwargs = conn_kwargs
        # for item_c in range(num):
        #     # 遍历定义连接放入连接池
        #     conn = Conn(**conn_kwargs)
        #     _pool.append(conn)
        self._pool = _pool
        self._size = num
        return self

    def __init__(self):
        logger.debug(f'初始化连接池 => ({id(self)})')

    # 定义取出连接
    @record_support
    def get_conn(self) -> Connection:
        __pool = self._pool
        return __pool.connection(shareable=False)
        # if __pool:
        #     lock.acquire(blocking=True)
        #     currConn = __pool.pop(0)
        #     if currConn.test_conn():
        #         # 连接有效
        #         # 不作处理
        #         pass
        #     else:
        #         logger.error('连接无效')
        #         currConn.re_conn()
        #     lock.release()
        #     return currConn
        # else:
        #     # 连接数不足则新增连接
        #     conn = Connection.Connection(**self.cache_conn_kwargs)
        #     self._pool.append(conn)
        #     return self.get_conn()

    # 定义归还连接
    @record_return
    def close_conn(self, conn):
        # self._pool.append(conn)
        pass

    # 定义查询连接池连接数
    def size(self):
        return self._size

    # 定义释放所有连接
    def free_pool(self):
        for conn in self._pool:
            conn.getConnect().close()
