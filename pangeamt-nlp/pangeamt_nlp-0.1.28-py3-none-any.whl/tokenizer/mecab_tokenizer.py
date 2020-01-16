from pangeamt_nlp.tokenizer.tokenizer_base import TokenizerBase

class MecabTokenizer(TokenizerBase):
    NAME = 'mecab'
    LANGS = ['ja']

    def __init__(self, lang):
        super().__init__(lang)

    def tokenize(self, text):
        pass
        # TODO

    def detokenize(self, text):
        pass
        # TODO
