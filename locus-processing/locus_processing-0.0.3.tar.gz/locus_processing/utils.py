class Result(object):
    def __init__(self, success, values=None, errors=None,
                 warnings=None):
        self.success = success
        self.values = values
        self.errors = errors
        self.warnings = warnings

    @property
    def is_success(self):
        return self.success

    @property
    def is_failure(self):
        return not self.success
