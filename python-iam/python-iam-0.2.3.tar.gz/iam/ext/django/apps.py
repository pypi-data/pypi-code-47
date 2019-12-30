import ioc
from django.apps import AppConfig

import iam.domain
from .services import ResourceAuthorizationService


class IAMConfig(AppConfig):
    name = 'iam.ext.django'
    label= 'iam'

    def ready(self):
        ioc.provide('AuthorizationService',
            ResourceAuthorizationService())
        ioc.provide('iam.PrincipalFactory',
            iam.domain.PrincipalFactory())
