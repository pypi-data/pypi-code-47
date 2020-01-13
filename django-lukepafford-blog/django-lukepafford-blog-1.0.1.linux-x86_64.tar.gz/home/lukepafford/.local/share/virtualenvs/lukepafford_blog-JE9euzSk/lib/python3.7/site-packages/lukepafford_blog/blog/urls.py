from django.urls import path
from .views import HomeView, PostList, PostUpload, PostDetail

urlpatterns = [
    path("", PostList.as_view(), name="posts_list"),
    path("posts/<slug:slug>/", PostDetail.as_view(), name="posts_detail"),
    path("upload/", PostUpload.as_view(), name="posts_upload"),
]
