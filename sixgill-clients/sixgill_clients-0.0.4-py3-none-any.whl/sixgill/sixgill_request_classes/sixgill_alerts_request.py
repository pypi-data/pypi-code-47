from sixgill.sixgill_request_classes.sixgill_base_post_auth_request import SixgillBasePostAuthRequest


class SixgillAlertsRequest(SixgillBasePostAuthRequest):
    end_point = 'alerts/actionable-alert'
    method = 'GET'

    def __init__(self, channel_code, access_token, bulk_size, is_read: bool, offset: int = 0, threat_type=None,
                 threat_level=None, severity=None):
        super(SixgillAlertsRequest, self).__init__(channel_code, access_token)

        self.request.params['sort_order'] = 'asc'
        self.request.params['is_read'] = 'unread' if is_read is False else None
        self.request.params['fetch_size'] = bulk_size
        self.request.params['threat_type'] = threat_type
        self.request.params['threat_level'] = threat_level
        self.request.params['severity'] = severity
        self.request.params['offset'] = offset
