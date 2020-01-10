from .organization import Organization
from .source_import import SourceImport
from .user import User


class Migration:

    """
    Official GITHUB documentation: https://developer.github.com/v3/migrations/
    """

    """
    API Documentation: https://github.com/monzita/octopy/wiki/Migration.md
    """

    def __init__(self, url, headers):
        self.organizations = Organization(url, headers)
        self.source_imports = SourceImport(url, headers)
        self.users = User(url, headers)
