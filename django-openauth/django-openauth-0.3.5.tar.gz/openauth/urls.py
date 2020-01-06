# coding: utf-8
from openauth import views
from django.urls import path

urlpatterns = [
    path('login/', views.OpenAuthView.as_view(), name='login'),
]
