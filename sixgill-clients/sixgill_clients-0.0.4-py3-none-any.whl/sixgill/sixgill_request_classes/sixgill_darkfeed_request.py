from sixgill.sixgill_request_classes.sixgill_base_post_auth_request import SixgillBasePostAuthRequest


class SixgillDarkFeedRequest(SixgillBasePostAuthRequest):
    end_point = 'alerts/feed'
    method = 'GET'

    def __init__(self, channel_code: str, access_token: str, include_delivered_items: bool, bulk_size: int):
        super(SixgillDarkFeedRequest, self).__init__(channel_code, access_token)

        self.request.params['consumer'] = channel_code
        self.request.params['include_delivered_items'] = include_delivered_items
        self.request.params['limit'] = bulk_size
        self.request.params['skip'] = 0
