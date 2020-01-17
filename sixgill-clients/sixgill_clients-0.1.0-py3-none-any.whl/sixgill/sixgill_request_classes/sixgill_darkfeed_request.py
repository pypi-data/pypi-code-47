from sixgill.sixgill_request_classes.sixgill_headers_request import SixgillHeadersRequest


class SixgillDarkFeedRequest(SixgillHeadersRequest):
    end_point = 'darkfeed/ioc'
    method = 'GET'

    def __init__(self, channel_id: str, access_token: str, limit: int):
        super(SixgillDarkFeedRequest, self).__init__(channel_id, access_token)

        self.request.params['limit'] = limit
