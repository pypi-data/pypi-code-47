from .code_of_conduct import CodeOfConduct
from .emoji import Emoji
from .gitignore import Gitignore
from .license import License
from .markdown import Markdown
from .meta import Meta
from .rate_limit import RateLimit


class Miscellaneous:

    """
    Official GITHUB documentation: https://developer.github.com/v3/misc/
    """

    """
    API Documentation: https://github.com/monzita/octopy/wiki/Miscellaneous.md
    """

    def __init__(self, url, headers):
        self.code_of_conduct = CodeOfConduct(url, headers)
        self.emojis = Emoji(url, headers)
        self.gitignore = Gitignore(url, headers)
        self.licenses = License(url, headers)
        self.markdown = Markdown(url, headers)
        self.meta = Meta(url, headers)
        self.rate_limit = RateLimit(url, headers)
