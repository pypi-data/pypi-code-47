class BuddyNSAPIError(RuntimeError):
    pass

class AuthenticationFailed(BuddyNSAPIError):
    pass

class PermissionDenied(BuddyNSAPIError):
    pass

class DoesNotExist(BuddyNSAPIError):
    pass


