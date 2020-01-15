from .base import AccountAPI


class ReturnPolicyAPI(AccountAPI):
    resource = 'return_policy'


class CreateReturnPolicy(ReturnPolicyAPI):
    method_type = 'POST'


class DeleteReturnPolicy(ReturnPolicyAPI):
    method_type = 'DELETE'
    required_path_params = ['return_policy_id']


class GetReturnPolicy(ReturnPolicyAPI):
    method_type = 'GET'
    required_path_params = ['return_policy_id']


class GetReturnPolicies(ReturnPolicyAPI):
    method_type = 'GET'
    required_query_params = ['marketplace_id']


class GetReturnPolicyByName(ReturnPolicyAPI):
    method_type = 'GET'
    url_postfix = 'get_by_policy_name'
    required_query_params = ['marketplace_id', 'name']


class UpdateReturnPolicy(ReturnPolicyAPI):
    method_type = 'PUT'
    required_path_params = ['return_policy_id']
