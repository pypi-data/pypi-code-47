from rest_framework.permissions import BasePermission
from config.settings import base as BASE


class Permission(BasePermission):
    def __init__(self, *args, **kwargs):
        self.enable = BASE.PERMISSION_ENABLE

    def has_permission(self, request, view):
        permission_ip = self.has_permission_ip(request)
        if permission_ip is None:
            return bool(request.user)
        return permission_ip

    def has_permission_ip(self, request):
        if self.enable:
            ips = BASE.PERMISSION_HOSTS
            remote_ip = request.META['REMOTE_ADDR']
            if remote_ip in ips:
                return True
            return False
        return None