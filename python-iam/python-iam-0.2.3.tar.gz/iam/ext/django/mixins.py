from iam.domain.mixins import Authorizable


class AuthorizableModel(Authorizable):

    @classmethod
    def get_resource_class(cls):
        m = cls._meta
        return f"{m.app_label}.{m.object_name}"

    def get_resource_qualname(self):
        return f"{self.get_resource_class}:{self.pk}"
