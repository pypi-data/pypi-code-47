from sixgill.sixgill_request_classes.sixgill_base_post_auth_request import SixgillBasePostAuthRequest


class SixgillDarkFeedDigestedRequest(SixgillBasePostAuthRequest):
    end_point = 'alerts/feed'
    method = 'PUT'

    def __init__(self, channel_code, access_token, digested_ids):
        super(SixgillDarkFeedDigestedRequest, self).__init__(channel_code, access_token)

        self.request.params['consumer'] = channel_code
        self.request.json = digested_ids
