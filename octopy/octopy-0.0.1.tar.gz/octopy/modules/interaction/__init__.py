from .organization import Organization
from .repository import Repository


class Interaction:

    """
    Official GITHUB documentation: https://developer.github.com/v3/interactions/
    """

    """
    API Documentation: https://github.com/monzita/octopy/wiki/Interaction.md
    """

    def __init__(self, url, headers):
        self.organization = Organization(url, headers)
        self.repository = Repository(url, headers)
