from .blob import Blob
from .commit import Commit
from .reference import Reference
from .tag import Tag
from .tree import Tree


class GitData:

    """
    Official GITHUB documentation: https://developer.github.com/v3/git/
    """

    """
    API Documentation: https://github.com/monzita/octopy/wiki/GitData.md
    """

    def __init__(self, url, headers):
        self.blobs = Blob(url, headers)
        self.commits = Commit(url, headers)
        self.references = Reference(url, headers)
        self.tags = Tag(url, headers)
        self.trees = Tree(url, headers)
