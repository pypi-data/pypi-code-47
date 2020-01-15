from .base import AccountAPI


class PaymentPolicyAPI(AccountAPI):
    resource = 'payment_policy'


class CreatePaymentPolicy(PaymentPolicyAPI):
    method_type = 'POST'


class DeletePaymentPolicy(PaymentPolicyAPI):
    method_type = 'DELETE'
    required_path_params = ['payment_policy_id']


class GetPaymentPolicy(PaymentPolicyAPI):
    method_type = 'GET'
    required_path_params = ['payment_policy_id']


class GetPaymentPolicies(PaymentPolicyAPI):
    method_type = 'GET'
    required_query_params = ['marketplace_id']


class GetPaymentPolicyByName(PaymentPolicyAPI):
    method_type = 'GET'
    url_postfix = 'get_by_policy_name'
    required_query_params = ['marketplace_id', 'name']


class UpdatePaymentPolicy(PaymentPolicyAPI):
    method_type = 'PUT'
    required_path_params = ['payment_policy_id']
