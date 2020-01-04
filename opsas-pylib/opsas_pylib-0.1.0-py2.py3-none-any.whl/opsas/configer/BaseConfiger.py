class BaseConfiger:

    def __init__(self, logger=None):
        if logger is None:
            import logging
            logger = logging.getLogger(__name__)
        self.logger = logger

    def set_logger(self, logger):
        self.logger = logger

    def render_data_map(self):
        raise NotImplementedError

    def get(self, key, verbose=False):
        _config = self.data_map.get(key)
        if _config is None:
            value = None
            source = None
        else:
            value = _config['value']
            source = _config['source']
        if verbose is True:
            return value, source
        else:
            return value
