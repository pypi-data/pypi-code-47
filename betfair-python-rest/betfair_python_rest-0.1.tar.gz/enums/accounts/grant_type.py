from ..base import BaseEnum


class GrantType(BaseEnum):
    AUTHORIZATION_CODE = '''Returned via the Vendor Web API 
    token request. The authorization code will be valid 
    for a single use for 10 minutes.'''
    REFRESH_TOKEN = '''A token that can be used to create a new access token when using the Vendor Web API'''
