from celery import Celery
from munch import Munch

from config import annotation

yml = Munch.fromDict(annotation.REMOTE_YML_CONFIG)

celery = Celery('tasks')
celery.config_from_object('cloudcelery.celery_config')
celery.conf.timezone = 'Asia/Shanghai'

redis_url = yml.redis.url
try:
    redis_password = yml.redis.password
except:
    redis_password = None

url = f'redis://{f":{redis_password}@" if redis_password is not None else ""}{redis_url}/0'

celery.conf.broker_url = url        #中间件
celery.conf.result_backend = url        #结果存储
