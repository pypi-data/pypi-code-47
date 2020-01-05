class MissingExperimentContextError(Exception):
    def __init__(self, message=None):
        super(self, MissingExperimentContextError).__init__(
            message or 'Current directry might not be a valid fuga experiment'
            'Could not find any valid fuga configuration files '
            '(`fuga.yml`) within working directory and its '
            'ancestors')
