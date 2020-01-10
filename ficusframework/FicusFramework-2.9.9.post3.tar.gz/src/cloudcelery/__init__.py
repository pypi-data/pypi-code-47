from celery import Celery
from munch import Munch

import config
from config import annotation

yml = Munch.fromDict(annotation.REMOTE_YML_CONFIG)

celery = Celery('tasks')
celery.config_from_object('cloudcelery.celery_config')
celery.conf.timezone = 'Asia/Shanghai'
celery.conf.setdefault('CELERY_DEFAULT_QUEUE',config.actor_name)        # 关心的是actor_name类型的任务

try:
    concurrent_count = yml.celery.concurrency
except:
    concurrent_count = 1
celery.conf.setdefault('CELERYD_CONCURRENCY',concurrent_count)        # 设置任务并发数,默认是1


redis_url = yml.redis.url
try:
    redis_password = yml.redis.password
except:
    redis_password = None

url = f'redis://{f":{redis_password}@" if (redis_password is not None and redis_password!="") else ""}{redis_url}/0'

celery.conf.broker_url = url        #中间件
celery.conf.result_backend = url        #结果存储
