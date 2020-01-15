from ..base_api import EbayAPI


class DeveloperAPI(EbayAPI):
    api_type_name = 'developer'
    api_name = 'analytics'
    api_version = 'v1_beta'
    method_type = 'GET'
    allowed_query_params = ['api_name', 'api_context']


class GetAppRateLimits(DeveloperAPI):
    resource = 'rate_limit'


class GetUserRateLimits(DeveloperAPI):
    resource = 'user_rate_limit'
