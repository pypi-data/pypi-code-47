from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


# Create your models here.

class Account(models.Model):
    """用户账号信息"""
    user = models.ForeignKey(User, blank=True, null=True, on_delete=models.SET_NULL)
    provider = models.CharField(max_length=128)
    uid = models.CharField(max_length=256)
    extra = models.TextField(blank=True, null=True)
    created = models.DateTimeField()
