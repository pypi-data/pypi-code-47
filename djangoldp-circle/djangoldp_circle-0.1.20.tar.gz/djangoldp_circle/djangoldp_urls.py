from django.conf.urls import url
from .views import CirclesJoinableViewset

urlpatterns = [
    url(r'^circles/joinable/', CirclesJoinableViewset.urls(model_prefix="circles-joinable")),
]
