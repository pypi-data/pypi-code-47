from pymongo import MongoClient


class MongoView:
    def __init__(
        self,
        host="localhost",
        port=27017,
        database="fenrys",
        collection="event_store",
        username=None,
        password=None,
    ):
        super().__init__()
        self.__host = host
        self.__port = port
        self.__database_name = database
        self.__collection_name = collection
        self.__username = username
        self.__password = password

    def __enter__(self):
        if self.__username is not None and self.__password is not None:
            self.__client = MongoClient(
                self.__host,
                self.__port,
                username=self.__username,
                password=self.__password,
            )
        else:
            self.__client = MongoClient(self.__host, self.__port)

        self.__db = self.__client[self.__database_name]
        self.collection = self.__db[self.__collection_name]

    def __exit__(self, *args, **kwargs):
        self.__client.close()
        self.__db = None
        self.collection = None
