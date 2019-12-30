from django.contrib import admin

from .models import AuthData


@admin.register(AuthData)
class AuthDataAdmin(admin.ModelAdmin):
    list_display = ["user", "credential_id", "created_on", "last_used_on"]
    search_fields = ["credential_id"]
