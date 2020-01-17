from sixgill.sixgill_request_classes.sixgill_headers_request import SixgillHeadersRequest


class SixgillDarkFeedDigestedRequest(SixgillHeadersRequest):
    end_point = 'darkfeed/ioc/ack'
    method = 'POST'
