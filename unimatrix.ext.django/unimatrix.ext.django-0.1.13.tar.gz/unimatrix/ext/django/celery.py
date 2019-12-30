import os

from celery import Celery


app = Celery(os.getenv('CELERY_APP_NAME') or 'unimatrix')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()


@app.task(bind=True)
def debug_task(self):
    print('Request: {0!r}'.format(self.request))
