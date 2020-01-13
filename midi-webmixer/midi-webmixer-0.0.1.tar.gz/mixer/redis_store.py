import redis
import json


class data:

    def __init__(self, redis_host='localhost', redis_port=6379):

        self.redis = redis.Redis(host=redis_host, port=redis_port, db=0)

    def set(self, key, data):

        return self.redis.set(key, json.dumps(data))

    def get(self, key):

        try:
            d = json.loads(self.redis.get(key))
            return d
        except TypeError:
            return None
