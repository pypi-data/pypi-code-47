class VkApiError(Exception):
    def __init__(self, response):
        self.code = response["error"]["error_code"]
        self.msg = response["error"]["error_msg"]
        self.params = response["error"]["request_params"]

    def __str__(self):
        return "%s: %s | Request parameters: %s" % (self.code, self.msg, self.params)
