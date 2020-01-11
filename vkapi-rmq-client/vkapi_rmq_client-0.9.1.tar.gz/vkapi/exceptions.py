
class VkException(Exception):
    pass


class VkAPIError(VkException):
    __slots__ = ['error', 'code', 'message', 'request_params', 'redirect_uri']

    def __init__(self, vk_error_data):
        super(VkAPIError, self).__init__()
        self.error_data = vk_error_data
        self.code = vk_error_data.get('error_code')
        self.message = vk_error_data.get('error_msg')
        self.request_params = self.get_pretty_request_params(vk_error_data)
        self.redirect_uri = vk_error_data.get('redirect_uri')

    @staticmethod
    def get_pretty_request_params(error_data):
        request_params = error_data.get('request_params', ())
        request_params = {param['key']: param['value']
                          for param in request_params}
        return request_params

    def __str__(self):
        tokens = ['error_code=%s' % self.code,
                  'message=\'%s\'' % self.message,
                  'request_params=%s' % self.request_params]
        if self.redirect_uri:
            tokens.append('redirect_uri=\'%s\'' % self.redirect_uri)
        return ', '.join(tokens)

    def __repr__(self):
        return '%s(%s)' % (self.__class__.__name__, self)
