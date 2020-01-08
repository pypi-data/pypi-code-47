from django.contrib import admin
from django.db.models import Q
from django.contrib.admin.options import BaseModelAdmin
from django.contrib.admin.options import InlineModelAdmin



class ItemOwnerMixin(BaseModelAdmin):

    owner_field_name = "owner"

    def get_queryset(self, request):
        queryset = super().get_queryset(request)
        filter_expr = Q(**{
            self.owner_field_name: request.user,
        })
        if isinstance(self, ItemShareMixin):
            filter_expr = filter_expr | Q(**{
                self.share_users_field_name: request.user
            }) 
            tmp_queryset = queryset.filter(filter_expr)
            pks = [obj.pk for obj in tmp_queryset]
            queryset = queryset.filter(pk__in=pks)
        else:
            queryset = queryset.filter(filter_expr)
        print(queryset.query)
        return queryset


class ItemShareMixin(BaseModelAdmin):

    share_users_field_name = "share_users"

    def get_queryset(self, request):
        queryset = super().get_queryset(request)
        if isinstance(self, ItemOwnerMixin):
            return queryset
        kwargs = {
            self.share_users_field_name: request.user,
        }
        queryset = queryset.filter(**kwargs)
        return queryset