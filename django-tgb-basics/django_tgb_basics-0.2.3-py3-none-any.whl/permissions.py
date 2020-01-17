"""
Define algunos permisos estándar para utilizar a lo largo de toda la
aplicación.
"""
import logging

from rest_framework.permissions import BasePermission


logger = logging.getLogger(__name__)


class IsOwnerAdminOrReadOnly(BasePermission):
    """
    Permite la lectura a través del método ``GET`` para
    cualquier usuario.

    Cualquier otro tipo de operación estará limitada a que el usuario que
    realiza la petición sea usuario administrador o que coincida con el valor
    del atributo ``user`` del objeto.
    """

    def has_object_permission(self, request, view, obj):
        if request.method == "GET":
            return True
        return obj.user == request.user or request.user.is_superuser


class IsOwnerOrAdmin(BasePermission):
    """
    Cualquier operación de acceso estará limitada a que el usuario que
    realiza la petición sea usuario administrador o que coincida con el valor
    del atributo ``user`` del objeto.
    """

    def has_object_permission(self, request, view, obj):
        logger.debug("Current user: %s", request.user)
        logger.debug(
            "Is current user authenticated?: %s", request.user.is_authenticated
        )
        logger.debug("Is current user an admin user?: %s", request.user.is_superuser)
        return request.user.is_authenticated and (
            obj.user == request.user or request.user.is_superuser
        )
