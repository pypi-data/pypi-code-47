from django.apps import AppConfig


class OpenauthConfig(AppConfig):
    name = 'openauth'
    verbose_name = '统一认证'

    def ready(self):
        # 改写 LoginView 为 OpenAuthView
        from django.contrib.auth import views
        from openauth.views import OpenAuthView
        views.LoginView = OpenAuthView

        # 增加 user 合并社交账号 方法

        from django.contrib.auth.admin import UserAdmin

        def combine_users(self, request, qs):
            from .models import Account
            users = list(qs.order_by('id'))
            Account.objects.filter(user__in=qs).update(user=users[0])
            combines_uid_msg = ','.join(map(lambda x: x.username, users))
            self.message_user(request, '合并成功 %s => %s' % (combines_uid_msg, users[0].username))

        combine_users.short_description = '合并用户社交账号(以先创建的为主)'

        UserAdmin.actions = [combine_users, ]
