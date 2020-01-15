from django.urls import re_path, path

from .views import SectionView, HomeView

app_name = 'sections'

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    re_path(r'^(?P<full_slug>[0-9a-zA-Z-_/]+)/$', SectionView.as_view(), name='section'),
]
