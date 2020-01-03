"""Expose classes relevant to tokenized articles."""
from dataclasses import dataclass
from typing import List, Callable
from . types import T


@dataclass
class Token:
    """Represents a token of a text."""

    token: str


@dataclass
class Tokens:
    """A tokenized text."""

    tokens: [Token]

    def to_primitive(self) -> List[str]:
        """Return list of strings."""
        return [token.token for token in self.tokens]

    def filter_by(self, token_filter: Callable[[Token], bool]):
        """Return tokens that satisfy a predicate.

        Parameters
        ----------
        token_filter: function
            Take a :py:class:`Token`, returning a boolean value.

        Returns
        -------
        Tokens
           tokens that meet `token_filter`.

        """
        return Tokens([token for token in self.tokens if token_filter(token)])

    def apply_function(
            self, function: Callable[[Token], T]) -> List[T]:
        """Apply a function to the tokens, returning the results."""
        return [function(token) for token in self.tokens]
