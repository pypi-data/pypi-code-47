from django.contrib import admin
from . import models as m


# Register your models here.

@admin.register(m.Account)
class AccountAdmin(admin.ModelAdmin):
    list_display = ('id', 'provider', 'uid', 'user', 'created')
