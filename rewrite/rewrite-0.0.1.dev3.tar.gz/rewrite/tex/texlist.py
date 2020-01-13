# Standard Library
None

# Third Party
from pylatex.base_classes import Container
from pylatex import SmallText, NewPage

# Local
from rewrite import tex

class TexList(Container):

    content_separator = '\n'

    def dumps(self):
        return self.dumps_content()

class NewPageMessage(TexList):

    def __init__(self, message=r'Please continue on the next page.'):
        r"""
        Parameters
        ----------
        message: str
            The message to display before starting a new page.
        """

        self.message = message
        super().__init__(
            data=[
                SmallText(tex.Bold(self.message)),
                NewPage(),
            ]
        )