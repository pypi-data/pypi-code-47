enable_utc = True
timezone = 'America/New_York'
backend = 'amqp://127.0.0.1:5672',
broker = 'pyamqp://',
include = ['celery_sandbox.tasks', ]
result_backend = 'rpc'
result_expires = 3600
