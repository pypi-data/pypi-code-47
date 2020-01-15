from enum import Enum


class APINGExceptionsEnum(Enum):
    TOO_MUCH_DATA = '''The operation requested too much 
    data, exceeding the Market Data Request Limits.'''
    INVALID_INPUT_DATA = '''The data input is invalid. 
    A specific description is returned via 
    errorDetails as shown below.'''
    INVALID_SESSION_INFORMATION = '''The session token 
    hasn't been provided, is invalid or has expired.'''
    NO_APP_KEY = '''An application key header 
    ('X-Application') has not been provided in the request'''
    NO_SESSION = '''A session token header 
    ('X-Authentication') has not been provided in the request'''
    UNEXPECTED_ERROR = '''An unexpected internal error 
    occurred that prevented successful request processing.'''
    INVALID_APP_KEY = '''The application key passed 
    is invalid or is not present'''
    TOO_MANY_REQUESTS = '''There are too many pending 
    requests e.g. a listMarketBook with Order/Match 
    projections is limited to 3 concurrent requests.
     The error also applies to listCurrentOrders, 
     listMarketProfitAndLoss and listClearedOrders 
     if you have 3 or more requests currently in execution'''
    SERVICE_BUSY = '''The service is currently too busy
     to service this request.'''
    TIMEOUT_ERROR = '''The Internal call to downstream 
    service timed out'''
    REQUEST_SIZE_EXCEEDS_LIMIT = '''The request exceeds 
    the request size limit. Requests are limited to a
     total of 250 betId’s/marketId’s (or a combination of both).'''
    ACCESS_DENIED = '''The calling client is not
     permitted to perform the specific action e.g. 
     they have an App Key restriction in place or 
     attempting to place a bet from a restricted jurisdiction.'''

    # Accounts API Exceptions
    DUPLICATE_APP_NAME = '''Duplicate application name'''
    APP_KEY_CREATION_FAILED = '''Creating application key version has failed'''
    APP_CREATION_FAILED = '''Application creation has been failed'''
    SUBSCRIPTION_EXPIRED = '''An application key is required for this operation'''
    INVALID_SUBSCRIPTION_TOKEN = '''The subscription token provided doesn't exist'''
    INVALID_CLIENT_REF = '''Invalid length for the client reference'''
    WALLET_TRANSFER_ERROR = '''There was a problem transferring 
    funds between your wallets'''
    INVALID_VENDOR_CLIENT_ID = '''The vendor client ID is not 
    subscribed to this application key'''
    USER_NOT_SUBSCRIBED = '''The user making the request is not 
    subscribed to the application key they are trying to 
    perform the action on (e.g. creating an Authorisation Code)'''
    INVALID_SECRET = '''The vendor making the request has provided 
    a vendor secret that does not match our records'''
    INVALID_AUTH_CODE = '''The vendor making the request has not 
    provided a valid authorisation cod'''
    INVALID_GRANT_TYPE = '''The vendor making the request has not
     provided a valid grant_type, or the grant_type they have
      passed does not match the parameters (authCode/refreshToken)'''

    @classmethod
    def get_description(cls, status):
        return getattr(cls, status).value
