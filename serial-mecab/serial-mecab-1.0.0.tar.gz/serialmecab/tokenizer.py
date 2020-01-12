"""Expose a class for tokenization."""
from logging import getLogger
from typing import List
import os
import MeCab


class MecabTokenizer:
    """A Tokenizer that uses MeCab."""

    logger = getLogger(__name__)

    def __init__(self, tagger: MeCab.Tagger):
        """Take a client for MeCab."""
        self.tagger = tagger

    def __call__(self, text: str) -> List[str]:
        """Tokenize a text."""
        segments = self.tagger.parse(text)
        tokens = [segment.split('\t')[0]
                  for segment in segments.split(os.linesep)][:-2]
        return tokens

    def __getstate__(self):
        """Exclude :py:attr:`tagger` because it is not picklable."""
        return {}

    def __setstate__(self, _):
        """Revert :py:attr:`tagger`.

        Set :py:attr:`tagger` to a new :py:class:`MeCab.Tagger` object.
        """
        self.tagger = self._create_tagger()
        self.logger = getLogger(__name__)

    @classmethod
    def create(cls):
        """Create a :py:class:`MecabTokenizer` object."""
        return MecabTokenizer(cls._create_tagger())

    @classmethod
    def _create_tagger(
            cls, dicdir=os.getenv('MECAB_DICDIR', None)) -> MeCab.Tagger:
        """Create a :py:class:`MeCab.Tagger` object."""
        cls.logger.info('mecab system dictionary is %s.', dicdir)
        return MeCab.Tagger(f'-d {dicdir}') if dicdir else MeCab.Tagger()
