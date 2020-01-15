from django.conf.urls.defaults import *
from marty import views

urlpatterns = [
    url(r'update$',     views.update,          name='update'),
]
