"""Provide classes relevant to text."""
from dataclasses import dataclass
import re


@dataclass
class Text:
    """Represent a text.

    Attributes
    ----------
    text: str

    """

    text: str

    def concat(self, text):
        """Concatenation of itself and `text`.

        Parameters
        ----------
        text: Text
            a text to be concatenated.

        """
        if text.is_empty():
            return self
        return Text(f'{self.text}。{text.text}')

    def is_empty(self) -> bool:
        """Return `True` iff empty."""
        return len(self.text) == 0

    def strip(self):
        """Return the Stripped text.

        Returns
        -------
        Text

        """
        text = self.text.strip()
        return Text(text)

    def split_by_newlines(self):
        r"""Split :py:attr:`text` by '\n+'.

        Returns
        -------
        Texts

        """
        texts = re.split(r'\n+', self.text)
        return Texts([Text(text) for text in texts])

    def empty():
        """Return an emtpy :py:class:`Text`."""
        return Text('')

    def extract_tokens(
            self, tokenizer, token_filter):
        """Return the tokens that satisfy a predicate.

        Returns
        -------
        yoshio.core.token.Tokens

        """
        tokens = tokenizer(self)
        return tokens.filter_by(token_filter)


@dataclass
class Texts:
    """Represent a collection of :py:class:`Text` s."""

    texts: [Text]

    def __getitem__(self, key):
        """Access the specified items."""
        return self.texts.__getitem__(key)
