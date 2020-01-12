import requests
import datetime

from rest_framework.views import APIView
from django.http import HttpResponseRedirect
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework.exceptions import PermissionDenied, NotAcceptable

from .mixins import CredentialMixin
from .pagination import LimitOffsetPaginationListAPIView


class BaseCredentialModelViewSet(CredentialMixin, ModelViewSet):
    queryset = None
    serializer_class = None

    def get_queryset(self):
        if not self.queryset:
            raise NotImplementedError("model must be declare")
        return self.queryset

    def create(self, request, format=None):
        raise NotImplementedError()

    def retrieve(self, request, *args, **kwargs):
        """
        ---
        parameters:
            - Authorization token in headers
        """

        _ = self.get_check_dash_auth(request)
        return super().retrieve(request, *args, **kwargs)

    def list(self, request, *args, **kwargs):
        """
        ---
        parameters:
            - Authorization token in headers
        """
        _ = self.get_check_dash_auth(request)

        return super().list(request, *args, **kwargs)


# base View model
class BaseReportListAPIView(LimitOffsetPaginationListAPIView):
    serializer_class = None
    model = None

    def get_model(self):
        if not self.model:
            raise NotImplementedError("model must be declare")
        return self.model

    def get_queryset(self):
        credential = self.get_check_admin(self.request)
        if not credential:
            raise PermissionDenied({"status": "error", "message": "This endpoint only for admin users."})
        integration_id = self.request.GET.get("integration_id")
        last_week = self.request.GET.get("last_week", "")
        last_3_days = self.request.GET.get("last_3_days", "")
        date_from = self.request.GET.get("date_from", "")
        date_to = self.request.GET.get("date_to", "")

        if last_week == "true":
            date_to = datetime.datetime.today().strftime('%Y-%m-%d')
            last_date = datetime.datetime.today() - datetime.timedelta(days=7)
            date_from = last_date.strftime('%Y-%m-%d')
        elif last_3_days == "true":
            date_to = datetime.datetime.today().strftime('%Y-%m-%d')
            last_date = datetime.datetime.today() - datetime.timedelta(days=3)
            date_from = last_date.strftime('%Y-%m-%d')

        if not date_from and not date_to:
            raise NotAcceptable({"status": "error", "message": "miss data params"})

        if integration_id:
            qs = self.get_model().objects.filter(integration_id=integration_id, date__range=[date_from, date_to])
        else:
            qs = self.get_model().objects.filter(date__range=[date_from, date_to])

        return qs


class BaseGetCredentialAPIView(CredentialMixin, APIView):

    def get_redirect_uri(self):
        """Create in this method redirect uri
            Example: https://oauth.yandex.ru/authorize?response_type=code&client_id={settings.YANDEX_APP_CLIENT_ID}&state={self.get_state()}&redirect_uri={redirect_url}
        """
        raise NotImplementedError()

    def check_auth_params(self):
        """This method for check auth params"""
        if "callback_url" not in self.request.GET \
                or "token" not in self.request.GET \
                or "platform_id" not in self.request.GET:
            raise PermissionDenied({"status": "error", "message": "You dont have permission to access."})
        return self.request

    def get_state(self):
        """
            Create state in this method
            Excample:
                user_info = self.get_user_info(request, get_token=True)
                user_id = user_info["id"]
                main_user = user_info["username"]
                # user_id = 16
                # main_user = "main_user"

                state = {
                    "callback_url": request.GET['callback_url'],
                    "user_id": user_id,
                    "main_user": main_user,
                    "platform_id": request.GET['platform_id']
                }
                return state
        """
        raise NotImplemented()

    def get(self, request, format=None):
        """
        ---
        parameters:
            - Authorization token in headers
            - 'callback_url' in GET params
        """

        return HttpResponseRedirect(self.get_redirect_uri())


class HomeAPIView(CredentialMixin, APIView):
    def get(self, request, format=None):
        return Response({"status": "success", "message": "smart integration api"})
