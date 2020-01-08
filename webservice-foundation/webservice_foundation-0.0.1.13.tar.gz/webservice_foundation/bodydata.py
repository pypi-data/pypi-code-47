class BodyData(dict):

    def __init__(self, data):
        for k, v in data.items():
            self[k] = v
            setattr(self, k, v)

    def __setitem__(self, key, value):
        if not isinstance(key, str):
            raise ValueError('Key must be string.')
        return super(BodyData, self).__setitem__(key, value)

    def __getitem__(self, key):
        try:
            return super(BodyData, self).__getitem__(key)
        except:
            return None


class ConcatBodyData(dict):
    BODY = 'body'
    BODY_ARGS = 'body_args'
    QUERY_ARGS = 'query_args'

    def __init__(self, iterable):
        super(ConcatBodyData, self).__init__(iterable)

    def get(self, key, default=None):
        _keyerror = None

        def _get(parent):
            try:
                return super(ConcatBodyData, self).get(parent).get(key)
            except KeyError as e:
                return None
        if key == self.BODY or key == self.BODY_ARGS or key == self.QUERY_ARGS:
            return super(ConcatBodyData, self).get(key)
        body = _get(self.BODY)
        body_arg = _get(self.BODY_ARGS)
        quey_arg = _get(self.QUERY_ARGS)
        return body or body_arg or quey_arg or default

    def __getitem__(self, key):

        def _getitem(parent):
            try:
                return super(ConcatBodyData, self).__getitem__(parent).__getitem__(key)
            except KeyError:
                return None
        if key == self.BODY or key == self.BODY_ARGS or key == self.QUERY_ARGS:
            return super(ConcatBodyData, self).__getitem__(key)
        body = _getitem(self.BODY)
        body_arg = _getitem(self.BODY_ARGS)
        quey_arg = _getitem(self.QUERY_ARGS)
        return body or body_arg or quey_arg or None
