from djangoldp.permissions import LDPPermissions
from rest_framework.exceptions import PermissionDenied


# auxiliary function tests user is an admin for specified project
def is_user_admin_of_project(user, project):
    from .models import Member

    try:
        project_member = Member.objects.get(user=user, project=project)
        return project_member.is_admin

    except:
        return False


class ProjectPermissions(LDPPermissions):
    def has_permission(self, request, view):
        # anonymous users have no rights
        if request.user.is_anonymous and not request.method == 'OPTIONS':
            return False

        # request on an existing resource - this will be reviewed by has_object_permission
        if request.method == 'PATCH' or request.method == 'DELETE' or request.method == 'PUT':
            return True

        return super().has_permission(request, view)

    def has_object_permission(self, request, view, obj):
        from .models import Member

        # anonymous users have no rights
        if request.user.is_anonymous and not request.method == 'OPTIONS':
            return False

        # admins have full permissions
        if is_user_admin_of_project(request.user, obj):
            return True

        # other members can perform GET only
        if request.method != 'GET':
            raise PermissionDenied(detail='You must be an admin to perform this action')

        if not Member.objects.filter(user=request.user, project=obj).exists():
            raise PermissionDenied(detail='You must be a member of this project to perform this action')

        return super().has_object_permission(request, view, obj)


class ProjectMemberPermissions(LDPPermissions):
    def has_permission(self, request, view):
        from djangoldp.models import Model

        # anonymous users have no rights
        if request.user.is_anonymous and not request.method == 'OPTIONS':
            return False

        # request on an existing resource - this will be reviewed by has_object_permission
        if request.method == 'PATCH' or request.method == 'DELETE' or request.method == 'PUT':
            return True

        # only admins can add new members to a project
        if request.method == 'POST':
            obj = Model.resolve_id(request._request.path)
            if is_user_admin_of_project(request.user, obj.project):
                return True
            else:
                raise PermissionDenied(detail='You must be an admin to perform this action')

        return super().has_permission(request, view)

    def has_object_permission(self, request, view, obj):
        # anonymous users have no rights
        if request.user.is_anonymous and not request.method == 'OPTIONS':
            return False

        # I can remove myself
        if obj.user.pk == request.user.pk:
            return True

        # admins have full permissions
        if is_user_admin_of_project(request.user, obj.project):
            if request.method == 'DELETE':
                # I cannot remove myself if I am the last admin
                if obj.pk == request.user.pk:
                    if obj.project.get_admins().count() == 1:
                        raise PermissionDenied(detail='To leave this project, you must first set up a new administrator'
                                                      ' through the project panel')

                # I cannot remove another admin
                elif obj.is_admin:
                    raise PermissionDenied(detail='You cannot remove another admin')

            return True

        return super().has_object_permission(request, view, obj)
