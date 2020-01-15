class BaseMetrecordException(Exception):
    pass


class MetrecordAPIException(BaseMetrecordException):
    def __init__(self, status_code, error):
        self.status_code = status_code
        self.error = error

    def __repr__(self):
        return '<MetrecordAPIException(status_code={}, error={})>'.format(self.status_code, self.error)