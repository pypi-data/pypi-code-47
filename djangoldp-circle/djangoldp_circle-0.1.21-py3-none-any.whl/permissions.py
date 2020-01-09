from djangoldp.permissions import LDPPermissions
from rest_framework.exceptions import PermissionDenied


# auxiliary function tests user is an admin for specified circle
def is_user_admin_of_circle(user, circle):
    from .models import CircleMember

    if user.is_anonymous:
        return False

    try:
        circle_member = CircleMember.objects.get(user=user, circle=circle)
        return circle_member.is_admin

    except:
        return False


class CirclePermissions(LDPPermissions):
    def has_permission(self, request, view):
        # anonymous users have no permissions
        if request.user.is_anonymous and not request.method == 'OPTIONS':
            return False

        # request on an existing resource - this will be reviewed by has_object_permission
        if request.method == 'PATCH' or request.method == 'DELETE' or request.method == 'PUT':
            return True

        return super().has_permission(request, view)

    def has_object_permission(self, request, view, obj):
        from .models import CircleMember

        # anonymous users have no permissions
        if request.user.is_anonymous and not request.method == 'OPTIONS':
            return False

        # admins have full permissions
        if is_user_admin_of_circle(request.user, obj):
            return True

        # other members can perform GET only
        if obj.status != 'Public':
            if request.user.is_anonymous:
                return False

            if not CircleMember.objects.filter(user=request.user, circle=obj).exists():
                raise PermissionDenied(detail='You must be a member of this circle to perform this action')

            if request.method != 'GET':
                raise PermissionDenied(detail='You must be an admin to perform this action')

        return super().has_object_permission(request, view, obj)


class CircleMemberPermissions(LDPPermissions):
    def has_permission(self, request, view):
        # anonymous users have no permissions
        if request.user.is_anonymous and not request.method == 'OPTIONS':
            return False

        # request on an existing resource - this will be reviewed by has_object_permission
        if request.method == 'PATCH' or request.method == 'DELETE' or request.method == 'PUT':
            return True

        return super().has_permission(request, view)

    def has_object_permission(self, request, view, obj):
        from .models import CircleMember

        # anonymous users have no permissions
        if request.user.is_anonymous and not request.method == 'OPTIONS':
            return False

        # I can remove myself
        if obj.user.pk == request.user.pk:
            return True

        # admins have full permissions
        if is_user_admin_of_circle(request.user, obj.circle):
            if request.method == 'DELETE':
                # I cannot remove myself if I am the last admin
                if obj.pk == request.user.pk:
                    if obj.circle.get_admins().count() == 1:
                        raise PermissionDenied(detail='To leave this circle, you must first set up a new administrator through the admin panel')

                # I cannot remove another admin
                elif obj.is_admin:
                    raise PermissionDenied(detail='You cannot remove another admin')

            return True

        # anyone can perform GET if it's public
        if obj.circle.status == 'Public':
            if request.method == 'GET':
                return True

        # private circles, members can GET/POST
        elif obj.circle.status == 'Private':
            if request.method == 'GET' or request.method == 'POST':
                return CircleMember.objects.filter(user=request.user, circle=obj.circle).exists()

        return super().has_object_permission(request, view, obj)
