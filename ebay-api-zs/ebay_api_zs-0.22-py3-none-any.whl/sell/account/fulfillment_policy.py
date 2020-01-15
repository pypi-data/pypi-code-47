from .base import AccountAPI


class FulfillmentPolicyAPI(AccountAPI):
    resource = 'fulfillment_policy'


class CreateFulfillmentPolicy(FulfillmentPolicyAPI):
    method_type = 'POST'


class DeleteFulfillmentPolicy(FulfillmentPolicyAPI):
    method_type = 'DELETE'
    required_path_params = ['fulfillment_policy_id']


class GetFulfillmentPolicy(FulfillmentPolicyAPI):
    method_type = 'GET'
    required_path_params = ['fulfillment_policy_id']


class GetFulfillmentPolicies(FulfillmentPolicyAPI):
    method_type = 'GET'
    required_query_params = ['marketplace_id']


class GetFulfillmentPolicyByName(FulfillmentPolicyAPI):
    method_type = 'GET'
    url_postfix = 'get_by_policy_name'
    required_query_params = ['marketplace_id', 'name']


class UpdateFulfillmentPolicy(FulfillmentPolicyAPI):
    method_type = 'PUT'
    required_path_params = ['fulfillment_policy_id']
