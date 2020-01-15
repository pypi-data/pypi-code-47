from django.urls import re_path, path

from .views import *

app_name = 'sections-api'

urlpatterns = [
    path('', SectionApiView.as_view({'get': 'list'}), name='sections'),
]