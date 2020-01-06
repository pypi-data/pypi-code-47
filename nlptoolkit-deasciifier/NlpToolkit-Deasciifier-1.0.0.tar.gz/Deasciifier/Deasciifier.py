from abc import abstractmethod

from Corpus.Sentence import Sentence


class Deasciifier:

    """
    The deasciify method which takes a Sentence as an input and also returns a Sentence as the output.

    PARAMETERS
    ----------
    sentence : Sentence
        Sentence type input.

    RETURNS
    -------
    Sentence
        Sentence result.
    """
    @abstractmethod
    def deasciify(self, sentence: Sentence) -> Sentence:
        pass
