from rediscluster import RedisCluster


class ConnectionFactory(object):
    def __init__(self, options):
        self.options = options

    def make_connection_params(self, url):
        """
        参数扩展的代码
        """
        params = dict(startup_nodes=url, decode_responses=False)

        options = self.options.get("OPTIONS", {})
        password = options.get("password", None)
        if password:
            params.update(password=password)
        ssl = options.get("ssl", False)
        if ssl:
            params.update(ssl=True)
        return params

    def connect(self, url):
        """
        连接 rediscluster客户端
        """
        params = self.make_connection_params(url)
        connection = self.get_connection(**params)
        return connection

    def get_connection(self, **kwargs):
        return RedisCluster(**kwargs)
