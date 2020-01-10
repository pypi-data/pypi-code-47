from pymongo import MongoClient
from pymongo import ReadPreference
from sshtunnel import SSHTunnelForwarder


#封装过的Mongdo客户端
class MongoDBC:
    conn = None
    ser = None

    def __init__(self, use_ssh=False, read_preference=ReadPreference.PRIMARY):
        if not use_ssh:
            # 获取MongoDB链接
            # 15秒超时
            # 关闭读写重试（防止卡死）
            connStr = "mongodb://root:123456@localhost:57017/"
            self.conn = MongoClient(
                connStr,
                socketTimeoutMS=60000,
                connectTimeoutMS=60000,
                maxIdleTimeMS=60000,
                retryWrites=True,
                retryReads=True,
                read_preference=read_preference,
            )
            # print(f"max_idle:{self.conn.max_idle_time_ms}")
        else:
            self.ser = SSHTunnelForwarder(
                ('47.97.126.223', 22),  # 跳板机
                ssh_username="root",
                ssh_pkey="~/.ssh/wy_ht_mbp_rsa",
                remote_bind_address=(
                    'dds-bp106fff87e553d42.mongodb.rds.aliyuncs.com',
                    3717),  # 远程的Redis服务器
                local_bind_address=('0.0.0.0', 10022)  # 开启本地转发端口
            )

    #with 拿到一个对象，触发enter方法
    def __enter__(self):
        self.ser.start()
        self.conn = MongoClient(
            "mongodb://root:ydMongo20181101@127.0.0.1:10022/")
        #给出返回值
        return self

    # with 退出
    def __exit__(self, exc_type, exc_val, exc_tb):
        self.conn.close()
        if self.ser:
            self.ser.close()

    def get_create_index(self,
                         db,
                         col,
                         index,
                         background=True,
                         unique=False,
                         expireAfterSeconds=None):
        index_list = [
            i for i in self.conn.get_database(db).get_collection(
                col).index_information()
        ]
        i_name = ""
        for i in index:
            i_name += f"{i[0]}_{i[1]}_"
        i_name = i_name[:-1]
        if i_name in index_list:
            print(f"索引[{i_name}]存在")
        else:
            if not expireAfterSeconds:
                print(f"创建索引[{i_name}]")
                self.conn.get_database(db).get_collection(col).create_index(
                    index,
                    background=background,
                    unique=unique,
                )
            else:
                print(f"创建TTL索引[{i_name}]")
                self.conn.get_database(db).get_collection(col).create_index(
                    index,
                    background=background,
                    unique=unique,
                    expireAfterSeconds=expireAfterSeconds,
                )