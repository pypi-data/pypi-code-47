from .run import Run
from .suite import Suite


class Check:

    """
    Official GITHUB documentation: https://developer.github.com/v3/checks
    """

    """
    API Documentation: https://github.com/monzita/octopy/wiki/Check.md
    """

    def __init__(self, url, headers):
        self.runs = Run(url, headers)
        self.suites = Suite(url, headers)
