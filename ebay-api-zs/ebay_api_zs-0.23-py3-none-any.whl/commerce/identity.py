from .base import CommerceAPI


class IdentityAPI(CommerceAPI):
    api_name = 'identity'
    api_version = 'v1'


class GetUser(IdentityAPI):
    api_location_domain = 'apiz'
    resource = 'user'
    method_type = 'GET'
