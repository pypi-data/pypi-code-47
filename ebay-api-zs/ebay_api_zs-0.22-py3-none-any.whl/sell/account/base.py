from ..base import SellAPI


class AccountAPI(SellAPI):
    api_name = 'account'


class GetPrivileges(AccountAPI):
    resource = 'privilege'
    method_type = 'GET'
