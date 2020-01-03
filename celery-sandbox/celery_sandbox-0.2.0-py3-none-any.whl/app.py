import os
from celery import Celery

# Fix for running on Windows,  See:  https://github.com/celery/celery/pull/4078/files
os.environ.setdefault('FORKED_BY_MULTIPROCESSING', '1')

app = Celery()
app.config_from_object('celery_sandbox.celeryconfig')
